---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1807.04559v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1807.04559v1_Three-dimensional_nuclear_spin_positioning_using_coherent_radio-frequency_contro

> Source: 1807.04559v1_Three-dimensional_nuclear_spin_positioning_using_coherent_radio-frequency_contro.pdf

> Pages: 5

---


## Page 1


Three-dimensional nuclear spin positioning using coherent radio-frequency control
J. Zopes†, K. Herb†, K. S. Cujia†, C. L. Degen∗
Department of Physics, ETH Zurich, Otto Stern Weg 1, 8093 Zurich, Switzerland.
Distance measurements via the dipolar interaction are fundamental to the application of nuclear
magnetic resonance (NMR) to molecular structure determination, but they only provide information
on the absolute distance r and polar angle θ between spins. In this Letter, we present a protocol to
also retrieve the azimuth angle φ. Our method relies on measuring the nuclear precession phase after
application of a control pulse with a calibrated external radio-frequency coil. We experimentally
demonstrate three-dimensional positioning of individual 13C nuclear spins in a diamond host crystal
relative to the central electronic spin of a single nitrogen-vacancy center. The ability to pinpoint
three-dimensional nuclear locations is central for realizing a nanoscale NMR technique that can
image the structure of single molecules with atomic resolution.
Nuclear magnetic resonance (NMR) and electron para-
magnetic resonance (EPR) spectroscopy are among the
most important analytical methods in structural biol-
ogy and the chemical sciences.
By combining local
chemical information of atoms with pair-wise distance
constraints, it becomes possible to reconstruct three-
dimensional structures or structural changes of proteins
and other biomolecules. While conventional NMR typi-
cally analyzes large ensembles of molecules, considerable
eﬀort has recently been expended on advancing NMR
detection to the level of individual molecules [1–3].
If
successfully extended to the atomic scale, NMR could en-
able direct imaging of three-dimensional molecular struc-
tures, with many applications in structural biology and
the nanosciences. A promising platform for this task are
diamond chips containing near-surface nitrogen-vacancy
(NV) centers whose electronic spins can be exploited as
sensitive local NMR probes [4, 5].
Structural imaging of single molecules involves deter-
mining the three-dimensional coordinates and elemental
species of the constituent nuclei. In NV-NMR, informa-
tion on the spatial position can be gained from the dipo-
lar part of the hyperﬁne interaction between the nuclei
and the central electronic spin [6–8]. Because of the ax-
ial symmetry of the dipolar interaction, however, only
the absolute distance r and the polar (inter-spin) angle θ
can be inferred from a NMR spectroscopy measurement.
Although the axial symmetry can be broken by a static
[8] or dynamic [9] transverse magnetic ﬁeld, determina-
tion of the azimuth angle φ, required for reconstructing
the full three-dimensional distance vector ⃗r = (r, θ, φ),
has remained challenging [10–12].
In this Letter, we demonstrate a simple and precise
method for retrieving the azimuth φ of the inter-spin
vector, allowing us to perform full three-dimensional nu-
clear distance measurements.
Our technique relies on
measuring the nuclear precession phase after application
of a radio-frequency (rf) pulse by an external micro-coil.
We determine φ at low and high magnetic ﬁelds, and for
polarized as well as unpolarized nuclear spins. We ex-
emplify our method by mapping the three-dimensional
locations of 13C nuclei for distances up to 11 ˚A and an-
gular uncertainties below 4◦.
Our scheme for measuring the azimuth angle is intro-
duced in Fig. 1(a-d): starting from a polarized nuclear
state, we perform a π/2 rotation of the nuclear spin. The
rotation is generated either by modulating the hyper-
ﬁne ﬁeld of the NV center using microwave pulses (Fig.
1c), or by applying a rf pulse with an external coil (Fig.
1d).
Subsequently, we let the nuclear spin precess in
the equatorial plane of the Bloch sphere and detect the
frequency and phase of the precession by an AC magne-
tometry measurement with the NV center [13–15] (Fig.
1e).
Crucially, the starting phase of the nuclear preces-
sion at t1 = 0 is set by the axis of the π/2 rotation,
which is determined by the spatial direction of the rf
ﬁeld in the laboratory frame of reference. When driv-
ing the nuclear rotation via the hyperﬁne interaction,
the rf ﬁeld direction is given by ⃗Az/γn, where ⃗Az =
(a⊥cos φ, a⊥sin φ, a||) is the secular part of the hyperﬁne
tensor, a|| and a⊥are the parallel and transverse hyper-
ﬁne coupling parameters [16, 17], and γn is the nuclear
gyromagnetic ratio (Fig. 1a, blue). Conversely, if the
external coil is used to generate the rf ﬁeld, the rotation
axis is given by the in-plane component of the coil ﬁeld
⃗Bcoil (Fig. 1a, red). By comparing the phases of the pre-
cession signals, we directly obtain the relative angle ∆φ
between the unknown orientation of the hyperﬁne vector
φ and the calibrated orientation φcoil of the external coil
ﬁeld.
We experimentally determine the φ angles of three
13C nuclear spins from three diﬀerent NV centers in two
single-crystal diamond chips. We optically polarize and
read out the NV spin by short laser pulses (∼2 µs)
and detect the ﬂuorescence intensity in a confocal mi-
croscope arrangement. Microwave pulses at ∼2.5 GHz
are used to actuate the mS = 0 ↔mS = −1 electronic
spin transition. To polarize the nuclear spins, we transfer
polarization from the optically aligned NV center using
dynamic nuclear polarization with a repetitive initializa-
tion sequence [16, 18]. AC magnetometry is performed
by a periodic sequence of microwave π pulses with XY8
phase cycling [19] enclosed by two π/2 pulses that are
arXiv:1807.04559v1  [quant-ph]  12 Jul 2018


## Page 2


2
X


coil
Y
Z
B0 || z
a
Bcoil,xy
Polarize
NV readout
Time t
t=0
t1
t90°
AC magnetometry
 pulse
NV polarize
Nuclear  pulse
AC magnetometry
wave
pulses
t=0
t=t90°+t1








X
Y

(a)
(b)
(e)
rf pulse
t=0
(c)
(d)
NV hyperfine field
FIG. 1. (a) Bloch-sphere schematic of a nuclear spin before
(grey arrow) and after (colored arrows) application of a π/2
rotation.
The rotation is either mediated by the hyperﬁne
interaction (blue-dashed axis) or a radio-frequency pulse gen-
erated by an external micro-coil (orange-dashed axis). The
diﬀerent azimuth angles of the rotation axes are translated
into a phase diﬀerence ∆φ of the nuclear spin precession,
thereby linking the known orientation of the coil ﬁeld to the a
priori unknown azimuth orientation of the inter-spin vector.
(b) Pulse sequence used to measure the phase of the nuclear
spin precession. The nuclear π/2 pulse is implemented either
(c) by a modulation of the NV center’s hyperﬁne ﬁeld using
periodic microwave π pulses or (d) by driving with an exter-
nal rf coil. The modulation frequency 1/(2τ) is matched to
the resonance of the nuclear spin. (e) AC magnetometry is
implemented by a Carr-Purcell-Meiboom-Gill sequence of mi-
crowave pulses. The sequence maps the nuclear component
⟨ˆI⃗a⟩that is parallel to the hyperﬁne axis ⃗a ∝(cos φ, sin φ) onto
the optically detectable polarization state of the NV center.
To register the nuclear precession we sample ⟨ˆI⃗a⟩for a series
of waiting times t1.
phase-shifted by 90◦[13, 20]. We use a permanent mag-
net to apply bias ﬁelds of B0 ∼10 mT and 200 mT for
low ﬁeld and high ﬁeld experiments, respectively, aligned
to within 1◦of the NV quantization axis.
The key component of our experiment is the exter-
nal rf coil, whose ﬁeld orientation serves as the spatial
reference for the φ angle measurement.
Two genera-
tions of micro-coils are used: the ﬁrst coil has a 3-dB-
bandwidth of 77 kHz (deduced from the step response
recorded with the NV center) and is used for low ﬁeld
experiments.
The second coil reaches a bandwidth of
1.72 MHz. Both rf coils produce ﬁelds of ∼5 mT/A and
are operated with currents of up to 1 A. Crucial for our
experiments is a precise knowledge of the direction and
temporal shape of the coil magnetic ﬁeld.
We deter-
mine the three-dimensional vector of the coil magnetic
ﬁeld ⃗Bcoil using two other nearby NV centers with diﬀer-
ent crystallographic orientations with an uncertainty of
less than 15 µT in all three spatial components [9, 21].
We align our (x,y,z) laboratory reference frame to the
([1¯12],[¯110],[111]) crystallographic axes of the single crys-
tal diamond chips (up to an inversion symmetry about
the origin).
To calibrate the dynamic response of the
coil, we perform in situ measurements of the rf ﬁeld us-
ing time-resolved optically-detected magnetic resonance
(ODMR) spectroscopy (Fig. 2(a,e)). We acquire ODMR
spectra in snapshots of 400 ns (a) or 100 ns (e) over the
duration of the rf pulse, and determine the pulse proﬁle
by ﬁtting the peak positions of the resonance curves.
In Fig. 2(c,d), we show a ﬁrst set of measurements for
nuclear spin 13C1 carried out at low magnetic ﬁeld, B0 ∼
10 mT. The hyperﬁne coupling parameters of this nuclear
spin are (a||, a⊥) = 2π × (18.5(1) kHz, 41.4(2) kHz), cal-
ibrated by a separate correlation spectroscopy measure-
ment [17]. Fig. 2(c) shows the reference measurement of
the nuclear spin precession after application of the π/2
pulse using the hyperﬁne ﬁeld. Fig. 2(d) plots the cor-
responding precession signal after applying the π/2 ro-
tation with the rf coil. We observe a clear phase shift
∆φ between the two signals, indicating that the hyper-
ﬁne ﬁeld ⃗Az/γn and the coil ﬁeld ⃗Bcoil point in diﬀerent
spatial directions. We verify that the phase shift changes
if we vary the direction of ⃗Bcoil by moving the rf coil to
a diﬀerent position (green data in Fig. 2(d)).
For ideal rf pulses and exact timings, the observed
phase shift ∆φ corresponds to the diﬀerence φ −φcoil
between the azimuth angles of the hyperﬁne and coil
magnetic ﬁelds, allowing us to directly deduce φ. How-
ever, due to the limited bandwidth of the rf circuit and
the ﬁnite length of feed lines, the actual rf pulses tend
to be delayed and distorted, leading to a phase oﬀset.
In addition, the AC magnetometry measurement is very
sensitive to timing errors and resonance oﬀsets in the
microwave modulation, causing additional uncertainty in
the phase measurement. To compensate for these issues,
we determine φ by ﬁtting the experimental data with a
Levenberg-Marquardt algorithm using a density matrix
simulation [22] as ﬁt function and φ as ﬁt parameter. We
propagate the two-spin density matrix through the full
sequence shown in Fig. 1(b) using piece-wise constant
Hamiltonians for the nuclear spin propagation, taking
the calibrated vector ﬁeld and temporal shape of Fig.
2(a) as well as the hyperﬁne parameters (a||,a⊥) as in-
puts. By calculating the nuclear spin evolution in the
laboratory frame of reference, the simulation captures


## Page 3


3
f = 0.105 MHz
f = 2.193 MHz
48 osc.
20
10
0
0
5
10
15
0
5
10
20
15
-10
-20
15
10
5
0
-10
-5
-15
-0.2
0.2
0.1
0.0
-0.1
resonance offset (MHz)
-0.2
0.2
0.1
0.0
-0.1
time t (s)
time t1 (s)
0
0.5
1.0
2.0
1.5
time t1 (s)
0
0.5
21.5
22.0
time t (s)
Coil
position 1
Reference
Coil
position 2
ODMR contrast
1.0
0.75
(a)
(c)
(d)
(e)
(g)
(h)
(b)
(f)
Ia (a.u.)
Ia (a.u.)
FIG. 2.
(a-d) Precision measurement of the azimuth angle of
13C1 at low magnetic ﬁeld, B0 = 9.600(8) mT. (a) Waveform
of the pulse sent to the rf coil. (b) ODMR spectra (vertical
axis) of the rf coil magnetic ﬁeld recorded in time steps of
400 ns (horizontal axis).
The black vertical line marks the
start time t = 0 of the rf pulse. The white solid line connects
the resonance positions determined by Lorentzian ﬁts. For
comparison, we also plot the input waveform from (a) (white
dashed line). (c,d) Nuclear precession signal measured as a
function of t1.
Dots show the experimental data.
Colored
lines represent density matrix simulations (best ﬁt) discussed
in the text. Shaded areas specify 2σ conﬁdence intervals of
the ﬁts. Panel (c) shows the reference measurement (sequence
of Fig. 1(c)) and panel (d) measurements for two diﬀerent coil
positions (sequence of Fig. 1(d)). (e-h) Same experiment per-
formed on 13C3 at high magnetic ﬁeld, B0 = 204.902(9) mT.
the Bloch-Siegert shift [23] and the z-component of the
rf ﬁeld.
In addition, we directly retrieve the absolute
laboratory frame azimuth φ rather than the relative ∆φ
between ⃗Az and ⃗Bcoil.
We start the analysis by ﬁtting the simulation to the
reference measurement (Fig. 2(c)), which allows us to
determine B0 with an uncertainty smaller than 10 µT.
As B0 deﬁnes the nuclear precession frequency, this cal-
ibration is of paramount importance for a precise esti-
mate of φ.
Afterwards we determine φ with a second
ﬁt to the measurements with the rf pulse (Fig.
2(d))
while keeping B0 ﬁxed. All ﬁt results are shown by solid
lines in Fig.
2(c,d).
We ﬁnd an azimuth location of
φ = 191 ± 2 ◦. We have previously determined the three-
4Å
8Å
=12Å
Z || [111] 
Y || [110] 
X || [112] 
~1.5Å
0°
45°
90°
135°
180°
225°
270°
315°
C1
C3
C2
z=6.67Å
z=4.81Å
z=7.11Å
FIG. 3. Polar plot of the reconstructed nuclear spin positions
in the xy-plane of the laboratory frame. Shaded regions mark
the uncertainty in φ of the respective nuclear spin. Radial
distances ρ = r sin θ and vertical heights z = r| cos θ| of the
nuclear sites are determined from the parallel and perpendicu-
lar hyperﬁne parameters by inverting the point-dipole formula
[9]. The measurement uncertainties in z and ρ, neglecting de-
viations from the point-dipole model [9, 24, 25], are less than
0.02 ˚A for all nuclei. Grey points represent the lattice sites of
diamond. 13C1 and 13C3 are in good agreement with sites C47
and C390 (black circles) of a recent density functional theory
(DFT) simulation [25] (13C2 is not part of the simulation).
The oﬀset between experimental and best-ﬁtting DFT loca-
tions is due to the extended NV wave function that limits the
point-dipole approximation [9]. The through-space distance
of 13C2 is r = 11.5 ˚A.
dimensional coordinates of the same nuclear spin using
a diﬀerent positioning method [9], where φ = 197 ± 4 ◦,
in good agreement with the present result. The accuracy
of our experiment is presently limited by the calibration
uncertainty of the coil ﬁeld angle (∼1 ◦) and by the sta-
tistical ﬁt error of the precession phase (∼1 ◦). Addi-
tional sources of uncertainty, e.g., a misalignment of B0
or the inﬂuence of the local chemical environment are not
included in the analysis, but are expected to be insignif-
icant for our study. The estimated three-dimensional lo-
cation for this (13C1) and another nuclear spin (13C2;
(a||, a⊥) = 2π × (1.9(1) kHz, 19.2(1) kHz)) are shown in
Fig. 3.
Next, we demonstrate that our azimuth positioning
technique can be readily extended to high magnetic ﬁelds.
High bias ﬁelds are desirable in NMR because of a better
peak separation and a simpliﬁed interpretation of spec-
tra. In addition, in NV-NMR, more eﬃcient dynamical
decoupling control and repetitive readout schemes be-
come possible at higher ﬁelds [26].
In Fig.
2(e-h) we
show measurements carried out at ∼200 mT on a third
nuclear spin (13C3) with hyperﬁne coupling parameters
(a||, a⊥) = 2π × (98.4 kHz, 138.4 kHz).
Here, we ﬁnd


## Page 4


4
φ = 81 ± 4◦.
The three-dimensional location of 13C3
is also indicated in Fig. 3.
The φ uncertainty at high magnetic ﬁeld is larger than
at low ﬁeld because of timing errors. At 200 mT, the
nuclear Larmor period is only ∼460 ns, such that 1 ns of
timing uncertainty causes a phase uncertainty of about
0.8◦. For the rf pulse in Fig. 2(e), we ﬁnd a phase delay
of 12±3 ◦, corresponding to an overall timing uncertainty
of the ODMR calibration of ∼4 ns. Although the mea-
sured phase delay is in good agreement with the value
predicted from the electrical characteristics of the rf cir-
cuit (∼11◦), it already introduces the largest error to
the φ measurement. For future experiments carried out
in the high bias ﬁelds of superconducting magnets [27] a
precise calibration of control ﬁelds will therefore become
even more critical.
Finally, we discuss a complementary scheme for recon-
structing the azimuth angle that does not require pre-
polarization of nuclear spins.
Instead of recording the
nuclear precession signal as a function of t1, we inter-
sperse a correlation spectroscopy sequence [17, 28] with
a central rf π pulse to generate a nuclear spin echo at a
ﬁxed time t = 2t1 (Fig. 4(a)). By varying the pulse phase
φrf from 0−360◦, we modulate the amplitude of the spin
echo, leading to an oscillatory signal ∝cos(2φrf −2φ).
We then determine φ from the phase oﬀset of the oscil-
lation. Fig. 4(b) shows a spin echo oscillation for 13C3
measured at a bias ﬁeld of 204.9(1) mT. The compatible
angles are {88 ± 4◦, 268 ± 4◦}, in good agreement with
the result from Fig. 2(h). Note that the echo method is
aﬄicted by a 180◦ambiguity in the angle measurement,
because the echo oscillation repeats with φrf modulo π.
Although the ambiguity could possibly be resolved by
applying concomitant rf and microwave rotations or by
introducing dc ﬁeld pulses [9], it is unlikely to restrict
future experiments on single molecules where relative,
rather than absolute, positions are important. In addi-
tion, single-molecule NMR experiments can exploit in-
ternuclear interactions to further constrain the nuclear
positions.
In conclusion, we have introduced a simple method for
measuring the inter-spin azimuth φ, enabling us to per-
form three-dimensional distance measurements on single
nuclear spins. We demonstrate the potential of our tech-
nique by mapping the 3D location of individual 13C nu-
clei in diamond with a precision suﬃcient for assigning
discrete lattice sites. Future experiments will apply 3D
distance measurements to molecules deposited on the sur-
face of dedicated diamond NMR sensor chips [5, 30–32]
and provide an avenue to analyze the structure and con-
formation of single molecules with atomic resolution [33].
This work was supported by Swiss National Science
Foundation (SNFS) Project Grant No. 200020 175600,
the National Center of Competence in Research in
Quantum
Science
and
Technology
(NCCR
QSIT),
and the DIAmond Devices Enabled Metrology and
NV readout
NV polarize
t=2t1
t=0
rf  pulse
with phase rf
t1
t1
Time t
AC magnetometry
AC magnetometry
Correlation probability (a.u.)
0.3
0
45
90
135
180
Phase of rf pulse rf (°)
225
270
315
360
0.2
0.1
0.0
-0.1
-0.2
-0.3
(a)
(b)
FIG. 4. Measurement of the hyperﬁne φ angle by a nuclear
spin echo. (a) Pulse sequence of the experiment: The free
evolution time of a correlation spectroscopy sequence is in-
terspersed with a π pulse generated by the rf coil. A cosine-
square envelope [29] is used to suppress pulse transients, and
the pulse is selective to the nuclear spin transition associ-
ated with the electronic mS = 0 state. The correlation spec-
troscopy sequence is implemented by two AC magnetometry
blocks as in Fig. 1(e); the bar on the second block indicates
that the sequence is reversed. (b) Spin echo modulation de-
tected on 13C3. Black dots show the data and the green line
shows the density matrix simulation (best ﬁt with φ as free
parameter). The 2σ conﬁdence intervals of the ﬁt are indi-
cated by shaded areas. The evolution time is 2t1 = 31.36 µs.
Sensing (DIADEMS) program, Grant No.
611143, of
the European Commission. We thank A. Nizovtsev and
F. Jelezko for sharing details about the DFT simulation.
While ﬁnishing this manuscript, we learned about a
similar idea put forward by Sasaki and coworkers [12].
†These authors contributed equally to this work.
∗Email: degenc@ethz.ch
[1] M. Poggio and C. L. Degen, Nanotechnology 21, 342001
(2010).
[2] J. Wrachtrup and A. Finkler, J. Magn. Reson. 269, 225
(2016).
[3] I. Schwartz, J. Rosskopf, S. Schmitt, B. Tratzmiller,
Q. Chen, L. P. McGuinness, F. Jelezko, and M. B. Ple-
nio, arXiv:1706.07134 (2017).
[4] T. Staudacher, F. Shi, S. Pezzagna, J. Meijer, J. Du,
C. A. Meriles, F. Reinhard, and J. Wrachtrup, Science
339, 561 (2013).
[5] H. J. Mamin, M. Kim, M. H. Sherwood, C. T. Rettner,
K. Ohno, D. D. Awschalom, and D. Rugar, Science 339,
557 (2013).
[6] T. H. Taminiau, J. J. T. Wagenaar, T. V. der Sar,


## Page 5


5
F. Jelezko, V. V. Dobrovitski,
and R. Hanson, Phys.
Rev. Lett. 109, 137602 (2012).
[7] S. Kolkowitz, Q. P. Unterreithmeier, S. D. Bennett, and
M. D. Lukin, Phys. Rev. Lett. 109, 137601 (2012).
[8] N. Zhao, J. Honert, B. Schmid, M. Klas, J. Isoya,
M. Markham, D. Twitchen, F. Jelezko, R. Liu, H. Fed-
der, and J. Wrachtrup, Nature Nano. 7, 657 (2012).
[9] J. Zopes, K. S. Cujia, K. Sasaki, J. M. Boss, K. M. Itoh,
and C. L. Degen, arXiv:1806.04883 (2018).
[10] A. Laraoui, D. Pagliero, and C. A. Meriles, Phys. Rev.
B 91, 205410 (2015).
[11] Z.-Y. Wang, J. F. Haase, J. Casanova, and M. B. Plenio,
Phys. Rev. B 93, 174104 (2016).
[12] K. Sasaki, K. M. Itoh,
and E. Abe, arXiv:1806.00177
(2018).
[13] J. M. Taylor, P. Cappellaro, L. Childress, L. Jiang,
D. Budker, P. R. Hemmer, A.Yacoby, R. Walsworth, and
M. D. Lukin, Nat. Phys. 4, 810 (2008).
[14] G. D. Lange, D. Riste, V. V. Dobrovitski, and R. Han-
son, Phys. Rev. Lett. 106, 080802 (2011).
[15] S. Kotler, N. Akerman, Y. Glickman, A. Keselman, and
R. Ozeri, Nature 473, 61 (2011).
[16] T. H. Taminiau, J. Cramer, T. van der Sar, V. V. Do-
brovitski, and R. Hanson, Nature Nano. 9, 171 (2014).
[17] J. M. Boss, K. Chang, J. Armijo, K. Cujia, T. Rosskopf,
J. R. Maze,
and C. L. Degen, Phys. Rev. Lett. 116,
197601 (2016).
[18] K. S. Cujia, J. M. Boss, J. Zopes,
and C. L. Degen,
arXiv:1806.08243 (2018).
[19] T. Gullion, D. B. Baker,
and M. S. Conradi, J. Magn.
Res. 89, 479 (1990).
[20] J. M. Boss, K. S. Cujia, J. Zopes,
and C. L. Degen,
Science 356, 837 (2017).
[21] S. Steinert, F. Dolde, P. Neumann, A. Aird, B. Naydenov,
G. Balasubramanian, F. Jelezko, and J. Wrachtrup, Rev.
Sci. Instrum. 81, 43705 (2010).
[22] J. Johansson, P. Nation, and F. Nori, Computer Physics
Communications 184, 1234 (2013).
[23] A. Abragam, (Oxford University Press, Oxford, 1961).
[24] A. Gali, M. Fyta,
and E. Kaxiras, Phys. Rev. B 77,
155206 (2008).
[25] A. P. Nizovtsev, S. Y. Kilin, A. L. Pushkarchuk, V. A.
Pushkarchuk, S. A. Kuten, O. A. Zhikol, S. Schmitt,
T. Unden, and F. Jelezko, New Journal of Physics 20,
023022 (2018).
[26] P. Neumann, J. Beck, M. Steiner, F. Rempp, H. Fedder,
P. R. Hemmer, J. Wrachtrup,
and F. Jelezko, Science
329, 542 (2010).
[27] N. Aslam, M. Pfender, P. Neumann, R. Reuter, A. Zappe,
F. F. de Oliveira, A. Denisenko, H. Sumiya, S. On-
oda, J. Isoya,
and J. Wrachtrup, Science 357 (2017),
10.1126/science.aam8697.
[28] A.
Laraoui,
F.
Dolde,
C.
Burk,
F.
Reinhard,
J. Wrachtrup,
and C. A. Meriles, Nature Commun. 4,
1651 (2013).
[29] J. Zopes, K. Sasaki, K. S. Cujia, J. M. Boss, K. Chang,
T.
F.
Segawa,
K.
M.
Itoh,
and
C.
L.
Degen,
arXiv:1705.07968 (2017).
[30] K. Ohashi, T. Rosskopf, H. Watanabe, M. Loretz, Y. Tao,
R. Hauert, S. Tomizawa, T. Ishikawa, J. Ishi-hayase,
S. Shikata, C. L. Degen, and K. M. Itoh, Nano Letters
13, 4733 (2013).
[31] M. Loretz, S. Pezzagna, J. Meijer,
and C. L. Degen,
Appl. Phys. Lett. 104, 033102 (2014).
[32] I. Lovchinsky, A. O. Sushkov, E. Urbach, N. P. de Leon,
S. Choi, K. de Greve, R. Evans, R. Gertner, E. Bersin,
C. Muller, L. McGuinness, F. Jelezko, R. L. Walsworth,
H. Park, and M. D. Lukin, Science 351, 836 (2016).
[33] J. A. Sidles, Proc. Natl. Acad. Sci. USA 106, 2477 (2009).

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
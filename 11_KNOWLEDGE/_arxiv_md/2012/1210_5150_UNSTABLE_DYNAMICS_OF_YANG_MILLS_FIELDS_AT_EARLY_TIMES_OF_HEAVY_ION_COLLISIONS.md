---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1210.515
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1210.5150_Unstable_dynamics_of_Yang-Mills_fields_at_early_times_of_heavy_ion_collisions

> Source: 1210.5150_Unstable_dynamics_of_Yang-Mills_fields_at_early_times_of_heavy_ion_collisions.pdf

> Pages: 4

---


## Page 1


arXiv:1210.5150v1  [hep-ph]  18 Oct 2012
Unstable dynamics of Yang-Mills ﬁelds at early times
of heavy ion collisions
Andreas Ipp
Institut f¨ur Theoretische Physik, Technische Universit¨at Wien, Wiedner Hauptstraße 8-10,
A-1040 Vienna, Austria
E-mail: ipp@hep.itp.tuwien.ac.at
Abstract.
The quark gluon plasma as produced in heavy ion collisions is exposed to early
anisotropies in momentum space due to its rapid expansion.
Such anisotropies can lead to
non-abelian plasma instabilities, driven by unstable gluonic modes that can grow exponentially
fast. These plasma instabilities can be simulated using a discretized version of gauge-covariant
Boltzmann-Vlasov and Yang-Mills equations. In the stationary case, a turbulent cascade forms
in the strong-ﬁeld regime, which is associated with an approximately linear growth of energy in
collective ﬁelds. Early longitudinal expansion slows down the growth of unstable modes, and
the formation of soft gluonic ﬁelds depends crucially on the initial conditions assumed.
1. Introduction
Heavy ion colliders like RHIC or LHC create the quark-gluon plasma (QGP) in an anisotropic
state.
Due to its fast expansion, initially along the longitudinal but later also along the
transverse directions, the plasma cools quickly and only exists for a duration of about a few
tens of yoctoseconds (1 ys = 10−24 s).
At early times and close to the center of the QGP,
longitudinal expansion dominates over transverse expansion.
This quickly leads to strong
momentum anisotropies along the polar angle with respect to the collision axis [1]. Such early
polar momentum space anisotropies could allow for a violation of the viscosity bound [2], or lead
to the emission of photon double pulses that are separated merely by yoctoseconds [3]. Most
notably, polar momentum space anisotropies can induce Chromo-Weibel plasma instabilities,
which are generalizations of Weibel or ﬁlamentation instabilities in ordinary electromagnetic
plasmas [4]. It has been suggested early that these instabilities may play a fundamental role in
the QGP [5, 6, 7]. In fact, already an inﬁnitesimal amount of momentum space anisotropy causes
the appearance of instabilities in collisionless plasmas [8, 9]. In electromagnetic plasmas, the
current ﬁlamentation instability develops magnetic islands on a fast electron time scale induced
by the deﬂection of the original electron streams, which eventually leads to an isotropization
of the electron distribution [10]. This fast isotropization on a time scale which is faster than
ordinary perturbative scattering processes could explain the fast apparent isotropization and
thermalization that is suggested by hydrodynamic modeling of the early QGP evolution [11, 12].
Non-abelian plasma instabilities can be studied using real-time lattice simulations [14, 15, 16].
The eﬀective ﬁeld theory for the collective phenomena at the soft scales is provided by gauge-
covariant collisionless Boltzmann-Vlasov equations [17]. The corresponding eﬀective action is
nonlocal and nonlinear [18, 19], but can be made local using auxiliary ﬁelds in the adjoint


## Page 2


50
100
150
200
0
2
4
6
8
m¥t
@Energy DensityDHm¥
4 g2L
SUH5L
SUH4L
SUH3L
SUH2L
Figure
1.
Comparison of average total
ﬁeld energy densities E for SU(2) through
SU(5) on linear scale in 3+1 dimensional
simulations
for a stationary
system with
anisotropy parameter ξ = 10 [13].
0.2
0.5
1.0
2.0
5.0
0.2
0.5
1.0
2.0
k m¥
g2 k2 f EIkMm¥
2
SUH5L
SUH4L
SUH3L
SUH2L
Figure 2.
The power spectrum for the
electric distribution fE(k) for various gauge
groups SU(2) through SU(5) at late times
80 < m∞t < 150. The distance between the
lines is m∞∆t ≈11 [13].
representation Wβ(x; v) which encode the ﬂuctuations of the distribution function of colored
hard particles [20].
They depend on a spatial unit vector which appears in the velocity
vµ = pµ/|p| of a hard particle with momentum pµ. The Yang-Mills equations are given by
Dµ(A)F µν = jν,
(1)
where the current jν is calculated from the auxiliary ﬁelds
jµ[A] = −g2
Z
d3p
(2π)3
1
2|p| pµ ∂f(p)
∂pβ W β(x; v).
(2)
The non-abelian Boltzmann-Vlasov equation for soft ﬁelds reduces to
[v · D(A)]Wβ(x; v) = Fβγ(A)vγ,
(3)
with Dµ = ∂µ −ig[Aµ, ·]. The scale of the hard particles drops out from these equations. An
anisotropic distribution function f(p) is obtained by deforming an isotropic distribution fiso
according to
f(p) ∝fiso(p2 + ξp2
z)
(4)
with anisotropy parameter −1 < ξ < ∞[8]. In order to solve these equations numerically, the
3-dimensional conﬁguration space is divided in a cubic lattice, on which a discretized version
of the above non-abelian gauge-covariant Boltzmann-Vlasov equations is formulated [15]. The
unit sphere of velocities for the auxiliary ﬁelds is described by a discretized set of unit vectors
[21, 15] or by an expansion in terms of spherical harmonics [14].
2. Numerical results
In the stationary case, the exponential growth of non-abelian plasma instabilities is limited in
3+1 dimensions by non-abelian self-interactions. The exponential growth is limited by gluon
self-interactions that are no longer negligible at a certain magnitude of soft ﬁelds. These self-
interactions lead to a turbulence cascade which form a power-law distribution fk ∝k−ν with
a spectral index that turns out to be about ν ≈2. While simulations are usually based on


## Page 3


the gauge group SU(2) [22, 16, 23], it has been conﬁrmed that the same spectral index holds
also in the QCD gauge group SU(3) as well as in higher gauge groups [13]. The systematics
of the scaling with Nc in the non-abelian regime is shown in Fig. 1 where the gauge groups
SU(2) through SU(5) are compared. One observes that for diﬀerent gauge groups the energy
densities cease to grow at approximately the same value. In the following linear regime, larger
gauge groups grow faster than smaller ones. Figure 2 shows the late-time behavior of spectra
for various gauge groups. The spectra are multiplied by k2 so that a scaling with ν ≈2 would
correspond to a horizontal line. The slow growth at large momenta corresponds to the linear
growth regime of Fig. 1.
Figure 3.
Magnetic Weibel instabilities on
an expanding background.
The inﬂuence of
diﬀerent initial values is studied for modes
with wave vector ν = 30 in the direction of
the anisotropy [24].
0
1
2
3
4
5
6
7
τ∼ = Qs τ / 10
10
-5
10
-4
10
-3
10
-2
Field energy densities / (Qs
4 / g
2)
Total Energy
EL
ET
BL
BT
Figure 4. Chromoelectric, chromomagnetic,
and total energy densities as a function of
proper time. Proper time is normalized such
that for Qs
=
2 GeV each unit of ∆˜τ
corresponds to 1 fm/c [25].
A longitudinal expansion of the plasma at early times modiﬁes the exponential growth, as
there are two competing eﬀects: On the one hand, plasma instabilities drive the exponential
growth, on the other hand the longitudinal expansion suppresses the growth. The net eﬀect
is a reduction from a growth exponential in time to exponential in the square root of proper
time. This has been numerically observed using the color glass condensate scheme [26, 27] and
the discretized hard loop scheme [28, 29]. In those simulations, an uncomfortable delay of the
onset of plasma instabilities has been observed [29]. Collective ﬁelds decay and suppress Weibel
instabilities at early times of the expanding plasma. It has been pointed out though that this
suppression depends strongly on the initial conditions assumed [24]. In Fig. 3, the delay of the
growth is displayed for various possibilities of initial conditions. Early work concentrated on a
seed electric ﬁeld with only ˜Πi(τ0) ̸= 0 [28] or a seed magnetic ﬁeld with only ˜Ai(τ0) ̸= 0 [29].
Seed magnetic ﬁelds instead of seed electric ﬁelds increase the delay of plasma instabilities, as
do mixed initial conditions for the ﬁelds. Surprisingly, if one considers initial ﬂuctuations in the
currents with only ˜ji(τ0) ̸= 0, the delay is very strongly reduced [24].
This behavior has been conﬁrmed in numerical simulations in 3+1 dimensions.
Figure 4
shows various energy densities as a function of proper time for a longitudinally expanding
system. Initially, the soft ﬁelds are depleted by the longitudinal expansion. Only after some
time, the unstable modes overcome the depletion and all ﬁeld components reach approximately
the same magnitude. The growth rate is moderately reduced and transverse chromoelectric and


## Page 4


chromomagnetic ﬁelds begin to dominate the energy density. Contrary to the ﬁxed-anisotropy
simulations, a saturation of the roughly exponential growth is not observed [25].
Since plasma instabilities may cause the isotropization in plasmas, the question remains how
to measure the isotropization time. Direct photons would be a good indicator because they
leave the QGP likely without further interaction. Under certain conditions, that is non-central
collisions and photon production in a direction close to forward direction, non-trivial photon
pulse shapes may be expected due to intermediate non-isotropic photon emission [3]. In extreme
cases, these pulse envelopes may assume the shape of double pulses at the yoctosecond time scale.
While it will not be possible to resolve such time structures directly [30], it may be possible to
observe the eﬀect of such modiﬁcations to the pulse envelope through Hanbury Brown-Twiss
[31] correlation measurements. A photon detector in the required forward direction may be
installed during the ALICE detector upgrade by 2018 when the proposed Forward Calorimeter
may be installed. With a few hundred photon pairs expected per year, such a measurement may
be challenging, but not impossible. Thus, photons could provide valuable information about
the earliest times of the plasma evolution, where gluon dynamics may be subject to plasma
instabilities due to the rapid expansion along the beam axis.
Concluding, one can state that for heavy-ion collisions at RHIC, non-abelian plasma
instabilities probably may not have enough time to develop as they compete against the fast
longitudinal expansion, but depending on the initial conditions, non-abelian plasma instabilities
may play an important role at LHC energies [24, 25].
References
[1] Blaizot J P, Gelis F, Liao J F, McLerran L and Venugopalan R 2012 Nucl. Phys. A873 68–80
[2] Rebhan A and Steineder D 2012 Phys. Rev. Lett. 108 021601 (Preprint 1110.6825)
[3] Ipp A, Keitel C H and Evers J 2009 Phys. Rev. Lett. 103 152301 (Preprint 0904.4503)
[4] Weibel E S 1959 Phys. Rev. Lett. 2 83–84
[5] Mrowczynski S 1988 Phys. Lett. B214 587
[6] Mrowczynski S 1993 Phys. Lett. B314 118–121
[7] Pokrovsky Y E and Selikhov A V 1988 JETP Lett. 47 12–14
[8] Romatschke P and Strickland M 2003 Phys. Rev. D68 036004 (Preprint hep-ph/0304092)
[9] Romatschke P and Strickland M 2004 Phys. Rev. D70 116006 (Preprint hep-ph/0406188)
[10] Califano F, Attico N, Pegoraro F, Bertin G and Bulanov S V 2001 Phys. Rev. Lett. 86 5293
[11] Arnold P, Lenaghan J and Moore G D 2003 JHEP 08 002 (Preprint hep-ph/0307325)
[12] Arnold P, Lenaghan J, Moore G D and Yaﬀe L G 2005 Phys. Rev. Lett. 94 072302 (Preprint
nucl-th/0409068)
[13] Ipp A, Rebhan A and Strickland M 2011 Phys. Rev. D84 056003 (Preprint 1012.0298)
[14] Arnold P, Moore G D and Yaﬀe L G 2005 Phys. Rev. D72 054003 (Preprint hep-ph/0505212)
[15] Rebhan A, Romatschke P and Strickland M 2005 JHEP 09 041 (Preprint hep-ph/0505261)
[16] B¨odeker D and Rummukainen K 2007 JHEP 07 022 (Preprint arXiv:0705.0180[hep-ph])
[17] Blaizot J P and Iancu E 2002 Phys. Rept. 359 355–528 (Preprint hep-ph/0101103)
[18] Pisarski R D 1997 hep-ph/9710370
[19] Mrowczynski S, Rebhan A and Strickland M 2004 Phys. Rev. D70 025004 (Preprint hep-ph/0403256)
[20] Blaizot J P and Iancu E 1994 Nucl. Phys. B417 608–673 (Preprint hep-ph/9306294)
[21] Rebhan A, Romatschke P and Strickland M 2005 Phys. Rev. Lett. 94 102303 (Preprint hep-ph/0412016)
[22] Arnold P B and Moore G D 2006 Phys. Rev. D73 025006 (Preprint hep-ph/0509206)
[23] Arnold P and Moore G D 2007 Phys. Rev. D76 045009 (Preprint arXiv:0706.0490[hep-ph])
[24] Rebhan A and Steineder D 2010 Phys. Rev. D81 085044 (Preprint 0912.5383)
[25] Attems M, Rebhan A and Strickland M 2012 (Preprint 1207.5795)
[26] Romatschke P and Venugopalan R 2006 Phys. Rev. Lett. 96 062302 (Preprint hep-ph/0510121)
[27] Romatschke P and Venugopalan R 2006 Phys. Rev. D74 045011 (Preprint hep-ph/0605045)
[28] Romatschke P and Rebhan A 2006 Phys. Rev. Lett. 97 252301 (Preprint hep-ph/0605064)
[29] Rebhan A, Strickland M and Attems M 2008 Phys. Rev. D78 045023 (Preprint 0802.1714)
[30] Ipp A, Evers J, Keitel C H and Hatsagortsyan K Z 2011 Phys. Lett. B702 383–387 (Preprint 1008.0355)
[31] Ipp A and Somkuti P 2012 (Preprint 1207.0197)

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1210_5150_unstable_dynamics_of_yang_mills_fields_at_early_times_of_heavy_ion_collisions
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2012/1210_5150_UNSTABLE_DYNAMICS_OF_YANG_MILLS_FIELDS_AT_EARLY_TIMES_OF_HEAVY_ION_COLLISIONS.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

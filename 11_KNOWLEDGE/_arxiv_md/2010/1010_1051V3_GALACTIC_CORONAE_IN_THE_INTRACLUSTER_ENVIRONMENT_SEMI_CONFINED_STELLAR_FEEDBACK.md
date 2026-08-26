---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1010.1051v3
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1010.1051v3_Galactic_Coronae_in_the_Intracluster_Environment__Semi-confined_Stellar-feedback

> Source: 1010.1051v3_Galactic_Coronae_in_the_Intracluster_Environment__Semi-confined_Stellar-feedback.pdf

> Pages: 10

---


## Page 1


arXiv:1010.1051v3  [astro-ph.HE]  31 Dec 2010
Mon. Not. R. Astron. Soc. 000, 000–000 (0000)
Printed 15 November 2018
(MN LATEX style ﬁle v2.2)
Galactic Coronae in the Intracluster Environment:
Semi-conﬁned Stellar-feedback-driven Outﬂows
Zhankui Lu1 ⋆and Q. Daniel Wang1
1 Department of Astronomy at University of Massachusetts, Amherst, 01003, USA
ABSTRACT
Recently X-ray observations have shown the common presence of compact galac-
tic coronae around intermediate-mass spheroid galaxies embedded in the intraclus-
ter/intragroup medium (ICM). We conduct 2-D hydrodynamic simulations to study
the quasi-steady-state properties of such coronae as the natural products of the on-
going distributed stellar feedback semi-conﬁned by the thermal and ram pressures of
the ICM. We ﬁnd that the temperature of a simulated corona depends primarily on
the speciﬁc energy of the feedback, consistent with the lack of the correlation between
the observed hot gas temperature and K-band luminosity of galaxies. The simulated
coronae typically represent subsonic outﬂows, chieﬂy because of the semi-conﬁnement.
As a result, the hot gas density increases with the ICM thermal pressure. The ram
pressure, on the other hand, chieﬂy aﬀects the size and lopsidedness of the coronae.
The density increase could lead to the compression of cool gas clouds, if present, and
hence the formation of stars. The increase also enhances radiative cooling of the hot
gas, which may fuel central supermassive black holes, explaining the higher frequency
of active galactic nuclei observed in clusters than in the ﬁeld. The radiation enhance-
ment is consistent with a substantially higher surface brightness of the X-ray emission
detected from coronae in cluster environment. The total X-ray luminosity of a corona,
however, depends on the relative importance of the surrounding thermal and ram
pressures. These environment dependences should at least partly explain the large
dispersion in the observed diﬀuse X-ray luminosities of spheroids with similar stellar
properties. Furthermore, we show that an outﬂow powered by the distributed feedback
can naturally produce a positive radial gradient in the hot gas entropy, mimicking a
cooling ﬂow.
Key words: method: numerical ISM: kinematics and dynamics X-ray: galaxies: clus-
ters
1
INTRODUCTION
Though consisting of primarily old stars, galactic spheroids
(bulges of Sb-Sa spirals as well as S0 and elliptical galaxies)
are a major source of stellar feedback in form of mass loss
and Type Ia supernovae (e.g., Ciotti et al. 1991; Knapp et
al. 1992; Mannucci et al. 2004). The speciﬁc energy of this
feedback predicts that it should present primarily in X-ray-
emitting hot gas. Indeed, such hot gas has been detected
in and around spheroids, which typically contain little cool
gas. However, it has been shown repeatedly that the X-ray-
inferred hot gas mass and energy are far less than the empir-
ical predictions from the feedback inputs (e.g., David et al.
2006; Li et al. 2006; Li and Wang 2007; Li et al. 2007; Wang
2010). This missing stellar feedback has most likely escaped
into large-scale galactic halos, where the gas becomes too
⋆E-mail:lv@astro.umass.edu
tenuous to be detected in existing X-ray imaging observa-
tions (e.g., Tang et al. 2009a and references therein). The
implication of this scenario is profound, because the injec-
tion of the mass and energy into the halos could strongly
aﬀect the ecosystem of the galaxies and hence their evolu-
tion (Tang et al. 2009a).
While the above qualitative picture seems clear, there
are key issues that still need to be addressed to understand
both the stellar feedback itself and its interplay with the
environment. Signiﬁcant uncertainties are still present in
the mass and energy input rates of stars (§ 2). The en-
ergy input rate is inferred from observations of SNe in a
large sample of galaxies of diverse optical and near-IR lu-
minosities as well as types (e.g., Mannucci et al. 2005), as-
suming a certain explosion mechanical energy deposited into
the interstellar space. The stellar mass loss rate is based on
the modeling of the 12 µm emission from the circumstel-
lar medium of evolved stars (e.g., Knapp et al. 1992). These


## Page 2


2
semi-empirical rates, uncertain by a factor of at least ∼2 for
individual galaxies, can in principle be directly constrained
by the measured temperature and luminosity of galactic
coronae. Indeed, detailed simulations have been conducted
for relatively isolated “ﬁeld” spheroids and have been com-
pared with observations (Tang et al. 2009a,b; Tang & Wang
2010), which have led to a qualitative understanding of the
feedback processes and eﬀects on X-ray measurements. In
particular, the feedback model expects that the speciﬁc en-
ergy should not change substantially from one spheroid to
another, which is consistent with little correlation between
the measured temperatures and K-band luminosities LK
(e.g., David et al. 2006; Sun et al. 2007). But the measured
temperatures ( <
∼1 keV) are substantially lower than the
expected value from simulations. The measured iron abun-
dances of coronal gas are also typically lower than expected
for the Ia SN-enriched gas (§ 2). At least part of these dis-
crepancies can be accounted for by various 3-D eﬀects of the
Ia SN heating, which produces very low-density, hot, fast-
moving, and enriched bubbles that hardly radiate. When the
gas in these bubbles ﬁnally mixed with the material from the
stellar mass loss at large radii, the X-ray emission becomes
too weak and diﬀuse to be eﬀectively detected (Tang et al.
2009a,b; Tang & Wang 2010). The observed X-ray emission
thus gives only a biased view of the coronae. We expect that
this bias should be minimal for a corona in the ICM, how-
ever. The high external thermal and ram pressures tightly
conﬁne such coronae, resulting in a low outﬂow speed and
hence relatively local mixing of the feedback materials. Fur-
thermore, one can better characterize the ICM environment
from observations, important for a self-consistent modeling
of a corona. Therefore, coronae embedded in the ICM are
ideal sites to better constrain the feedback and its interplay
with the environment.
There have also been signiﬁcant eﬀorts in study-
ing stellar feedback-powered coronae embedded in the
ICM, mostly focusing on the ram-pressure stripping of
hot gas (e.g., Acreman et al. 2003; Stevens et al. 1999;
Toniazzo & Schindler 2001). It is shown that the global mor-
phological and integrated properties, such as gas mass and
luminosity, are strongly inﬂuenced by the environment. A
set of 2D simulations done by Stevens et al. (1999) show
that galactic coronae can be maintained by stellar feedback
in poor clusters while be eﬃciently stripped in rich ones.
Acreman et al. (2003) and Toniazzo & Schindler (2001) sim-
ulated galaxies falling into clusters and demonstrated that a
galactic corona reached a cyclic ”stripping replenishment”
dynamics due to the periodic orbital motion of the host
galaxy as well as the competing processes such as stripping
and stellar feedback.
We
focus
on
modeling
coronae
in
and
around
intermediate-mass spheroids that are embedded in the ICM.
Such a system is relatively simple with minimum eﬀects due
to the feedback from AGNs and to the radiative cooling of
hot gas. We expect that the hot gas is in a quasi-steady,
subsonic outﬂow semi-conﬁned by the thermal and ram-
pressures of the ICM. This state should be only sensitive
to the local properties of the ICM (see § 2 for more discus-
sion), avoiding large uncertainties in modeling the history
of the galactic feedback and the evolution of the environ-
ment, as would be needed for a ﬁeld spheroid (Tang et al.
2009a). The simulations can also be compared with an in-
creasing number of X-ray detections of galactic coronae of
such spheroids (e.g., Sun et al. 2007), leading to an improved
understanding of the feedback itself and its interplay with
the environment. In particular, we examine the dependence
of the corona properties on the speciﬁc energy of the stel-
lar feedback and on the thermal and ram pressures of the
ICM and check how measurements (e.g., temperature, sur-
face brightness, overall luminosity and morphology) may be
made to infer the parameters that cannot directly observed
(e.g., the ICM thermal and ram pressures local to an indi-
vidual galaxy). Here, we will present 2-D simulations only,
which allow for an eﬃcient exploration of a large parameter
space. The paper is organized as follows: We brieﬂy describe
our numerical model and setup in § 2 and present results in
§ 3; We discuss their implications in § 4; Finally in § 5, we
summarize our conclusions.
2
MODEL AND SIMULATION SETUP
2.1
Model Galaxies
Our model galaxy is composed of a stellar spheroid compo-
nent and a dark matter halo. We use the spherical Hernquist
density proﬁle (Hernquist 1990) to represent the stellar mass
distribution:
ρs(r) = Ms
2πa3
a4
r(r + a)3 ,
(1)
where Ms is the total stellar mass, and a is the scale radius.
This density proﬁle results in a gravitational potential
φ(r) = −GM
(r + a).
(2)
The above stellar mass distribution resembles the de Vau-
couleur’s Law; The relation between the half-light radius Re
and the scale radius is Re = 1.8513a.
We characterize the dark matter halo with the NFW
proﬁle (Navarro et al. 1997),
ρd(r) =
ρ0
(r/rd)(1 + r/rd)2 ,
(3)
where rd is the scale radius of the dark halo, and ρ0 is deﬁned
as
ρ0 = 1
3ρcritΩm∆vir
c3
ln(1 + c) −
c
(1+c)
,
(4)
in which ρcrit is the critical density of the universe. The dark
halo has a mass Mvir within the virial radius rvir, which is
deﬁned to have a density that is ∆vir times the mean matter
density of the universe ρcritΩm. We adopt ∆vir to be 250.
Therefore, we have the relation
Mvir = 4π
3 r3
vir∆virρcritΩm,
(5)
where c is the concentration factor deﬁned as c = rvir
rd
and
is related to Mvir. We set c = 13 (Eke et al. 2001). Thus,
for a given cosmology and a given Mvir, the mass proﬁle of
the dark halo is totally determined.
2.2
Stellar Feedback
The stellar mass and energy feedback in spheroids are dom-
inated by the mass loss and Ia SNe of evolved stars, respec-


## Page 3


Galactic Coronae in the ICM
3
tively. We neglect the energy input from the random motion
of stars and hence their ejecta. The total energy released by
type Ia SNe is
˙E = ESNnSN

LK
1010LK,⊙

,
(6)
where nSN = 0.00035 yr−1 for E/S0 galaxies according to
Mannucci et al. (2005). The empirical mass input rate from
the stellar mass loss is
˙M = m

LK
1010LK,⊙

,
(7)
where m = 0.021 M⊙yr−1 according to Knapp et al. (1992).
Assuming that the mechanical energy of each SN is 1051 erg,
the speciﬁc energy of stellar feedback is β =
˙E
˙
M ∼5 keV per
particle. To account for the uncertainties in these rates and
assumptions, we also sample three diﬀerent lower values of
the specﬁc energy for comparison with observations (Table
1). We assume that the energy and mass inputs follow the
distribution of the stellar mass.
In addition, each Ia SN produces ∼0.7M⊙of iron
ejecta. We assume that the iron abundance of the mass loss
from stars is solar. If the ejecta is fully and instantaneously
mixed with the mass loss, the expected iron abundance rel-
ative to the solar value is then
nsnMF e
m

/Z⊙∼
0.0018 × 0.7M⊙
0.2M⊙

/Z⊙= 5.5.
(8)
However, in observations, supersolar metallicity is quite rare.
Tang et al. (2009b) and Tang & Wang (2010) have shown
that Ia SN ejecta may not be eﬃciently mixed with stellar
mass loss on microscopic scale, resulting in a low eﬀective
metallicity of the ISM. While our focus is on the environ-
mental eﬀect. In our simulation, we set the iron abundance
of the input mass to the solar value.
2.3
Simulation Setup
The gas hydrodynamics and metal abundance distribution
with both the stellar feedback and radiative cooling can be
described by the following equations:
∂ρg
∂t + ∇· (ρgv)
=
Sm
∂(ρgv)
∂t
+ ∇· (ρgvv + P[I ])
=
ρgg
∂(ρge)
∂t
+ ∇· [(ρge + P)v]
=
Se −neniΛ(T, Z) + ρgg · v
∂(ρgXiron)
∂t
+ ∇· (ρgXironv)
=
Siron.
(9)
The ﬁrst equation is mass conservation law, with ρg denot-
ing the mass density of the coronal gas. The second is mo-
mentum equation. P is gas pressure and g is gravitational
acceleration. The third one is energy equation. e stands for
the speciﬁc energy of the gas, including both thermal and
kinetic components. The second term to the right is cooling
rate. We adopt the cooling curve from Sutherland & Dopita
(1993), assuming an optically-thin thermal plasma in colli-
sional ionization equilibrium. For calculation of the radia-
tion in a speciﬁc band, we use the Mekal model, extracted
from the X-ray spectral analysis software XSPEC. We use
the fourth equation to keep track on the iron mass fraction,
which is denoted by Xiron.
We conduct our simulations with the FLASH code
(Fryxell et al. 2000), an Eulerian astrophysical hydrody-
namics code with the adaptive mesh reﬁnement (AMR) ca-
pability. The simulated region is ﬁxed in the galaxy-rest
frame using cylindrical coordinates, with z ranging from
−50 kpc to 50 kpc and the radius from 0 to 50 kpc. The axis
of the cylinder is through the center of a simulated spheroid
and along the direction of its motion. The upper and lower
boundary conditions are ﬁxed so that the ICM ﬂows in and
out the simulation region at a constant speed. This mimics
the motion of galaxies through a local cluster environment.
We apply reﬂection boundary condition at r = 0 and diode
boundary condition, which only allows gas to ﬂow out, to
the right side of the simulation region. Compared with the
simulation box, which is 50 kpc by 100 kpc, the coronae are
only on the order of 1 kpc to 10 kpc across. Data near the
outer regions will be excluded in our analysis to avoid any
potential artifacts introduced by the assumed outer bound-
ary condition of the simulations. Also, the outer region will
not be shown in the following images. We allow the resolu-
tion to reach 0.1 kpc, so that the small coronae can be well
resolved.
When a simulation starts, there is no interstellar gas in
the galaxy. As the simulation progresses, the stellar feedback
gradually accumulates in and around the spheroid to form a
corona, which is characterized by its higher iron abundance.
In the mean time, the ram-pressure and turbulent motion
strips gas at the outer boundaries of the corona. We end the
simulation when it reaches a statistically quasi-steady state.
Empirically, the time to reach such a state is τg ∼0.2 Gyr,
while the time for the ICM to pass the simulation region
ranges from 0.05 Gyr to 0.2 Gyr. Representative results are
all extracted from the simulations after this time.
The presence of a local quasi-steady state is a reason-
able assumption for a compact corona. As a galaxy moves
through a cluster, the ICM condition can of course change
drastically. But the time scale for such a change is typically
much longer than the dynamic time for the corona to adapt
the local environment. For a cluster of a characteristic size of
∼1 Mpc and temperature of 2 keV, for example, the cross-
ing time for a galaxy moving roughly at the sound speed is
τc1 ∼2 Gyr. In contrast, for a corona of a typical size ∼5
kpc and temperature ∼0.8 keV, the sound crossing time
is only τc2 ∼20 Myr. Even if a corona is totally destroyed
at some point(e.g. at the central region of a cluster), the
re-building time scale τg, as dicussed above, is still shorter
than the environment change time scale. Therefore, the local
quasi-steady state is a reasonable assumption for character-
izating the environmental impact on galactic coronae.
3
RESULTS
We have simulated a set of cases to characterize the depen-
dence on key parameters. Table 1 lists our adopted model
parameter values. The diﬀerent combinations of the ICM
density (ni, the number density of all particles) and temper-
ature (Tj) as well as the Mach number (Mk) and speciﬁc
energy (βl) of the model galaxy form a set of 48 cases.
Here we present the gas properties extracted from the
simulations. We ﬁrst detail the results for a representative


## Page 4


4
Table 1. Model Parameters
Model galaxy
Stellar Mass(1011 M⊙)
2.0
Dark Halo Mass (1011 M⊙)
40
ICM properties
ICM density (10−4 cm−3)
3.3(n1), 10(n2)
ICM temperature (107 K)
2.0(T1), 6.0(T2)
Iron abundance ( Z⊙)
0.3
Mach number
0.6(M1), 1.2(M2), 1.8(M3)
Stellar feedback
Mass loss rate ( M⊙/1011 M⊙/yr)
0.32
Speciﬁc energy (keV)
1.2(β1), 1.8(β2), 3.0(β3), 4.8(β4)
Iron abundance ( Z⊙)
1.0
case n1T2M2β2 (§ 3.1) and then discuss the similarity and
signiﬁcant variation among the diﬀerent cases (§ 3.2).
3.1
Representative Case
Fig. 1 shows a snapshot of the representative simulation case
n1T2M2β2 in terms of the Mach number, thermal pressure,
density, and temperature distributions. At the very front of
the corona is a smooth and distinct boundary that sepa-
rates the corona from the ambient medium. This is a con-
tact discontinuity, across which the density, temperature and
metallicity change abruptly. Compared to the surrounding
medium, the corona is cooler and denser. The iron abun-
dance inside the corona is a constant which is equal to the
value of injected material (Fig. 2). Outside the corona the
abundance drops rapidly to the value of the ICM, although
it is contaminated by the local stellar feedback. Therefore,
we can use the abundance to trace the morphology of the
corona gas. Inside the corona, the Mach number of the gas
ﬂow is so low (∼0.1) that it is almost hydrostatic (see § 4.1).
While the main body of a corona can reach a nearly
steady state, both the interface with the surrounding ICM
and the tail are unstable. The individual features in these
later parts can strongly ﬂuctuate with time. The side horns
are characteristic sign of the Kelvin-Helmholtz (KH) insta-
bility. As a result, the corona gas is torn oﬀand pushed
back to form a chaotic tail. Therefore, the stripping is pri-
marily due to the hydrodynamic instability rather than the
ram-pressure itself. Similarly, the instability also leads to
the dynamic mixing of the corona gas with the ICM, al-
though numerically this is achieved on the spacial scale of
the simulation resolution.
Fig. 3 shows the 1-D distribution of the iron abundance,
density, temperature and entropy of the corona along the z
axis of the simulation box. Here the entropy is deﬁned as
S =
T
nγ−1 (γ is the speciﬁc heat ratio of the gas and is equal
to 5
3). The distributions are averaged over a time span of 50
Myr when the simulation has reached a quasi-steady state.
While the gas density drops substantially from the cen-
ter of the spheroid to the outer outskirt of the corona, the
temperature does not change much (Fig. 3). The speciﬁc en-
ergy of the feedback determines the speciﬁc enthalpy of the
corona gas and therefore the temperature (T =
β
2.5kB ) when
the radiative cooling is not important as in the present case.
The small drop of the temperature towards the outskirt (by
a factor of up to 1.2) is largely due to the outﬂow that needs
to climb out of the gravity potential. But, because of the dis-
tributed nature of the mass and energy injection, the drop
0
5 10 15 20 25 30
-40
-30
-20
-10
0
10
20
0
5 10 15 20 25 30
r /kpc
-40
-30
-20
-10
0
10
20
z/kpc
0.5
1.0
1.5
2.0
2.5
0
5 10 15 20 25 30
-40
-30
-20
-10
0
10
20
0
5 10 15 20 25 30
r /kpc
-40
-30
-20
-10
0
10
20
z/kpc
-12.0
-11.8
-11.6
-11.4
-11.2
-11.0
-10.8
0
5 10 15 20 25 30
-40
-30
-20
-10
0
10
20
0
5 10 15 20 25 30
r /kpc
-40
-30
-20
-10
0
10
20
z/kpc
-3.5
-3.0
-2.5
-2.0
0
5 10 15 20 25 30
-40
-30
-20
-10
0
10
20
0
5 10 15 20 25 30
r /kpc
-40
-30
-20
-10
0
10
20
z/kpc
6.8
7.0
7.2
7.4
7.6
7.8
Figure 1. Model n1T2M2β2 seen in the Mach number, thermal
pressure, density, and temperature.
is much smaller than what is predicted from the Bernoulli’s
law for ideal gas moving from the center to the outskirt.
Another interesting characteristic of the simulated
corona is the positive radial entropy gradient. This is ap-
parently caused by the nearly constant temperature proﬁle
and the steep density drop from the center to the outskirts,
as required to maintain a nearly hydrostatic state of the
corona (§ 4.1). Physically this positive entropy gradient is a
natural result of an outﬂow that is continuously heated by
the stars along the way out.
3.2
Similarity and Variance among the Cases
Here we focus on the similarity and signiﬁcant variance in
the hot gas properties of the various simulated cases, in ref-
erence to the representative one (n1T2M2β2) detailed above.


## Page 5


Galactic Coronae in the ICM
5
0
5
10
15
20
25
30
-40
-30
-20
-10
0
10
20
0
5
10
15
20
25
30
r /kpc
-40
-30
-20
-10
0
10
20
z/kpc
0.4
0.5
0.6
0.7
0.8
0.9
1.0
Figure 2. Iron abundance map for model n1T2M2β2.
In most of the simulation cases, the coronae are clearly
in the outﬂow state. The radiative cooling is not important,
except for some such as n2T1M1β1, n2T1M2β1, n1T2M1β1,
n2T2M1β1 and n2T2M2β1 , with combination of low spe-
ciﬁc energy and high ICM pressure. The gas at the spheroid
center is so dense that an inward cooling ﬂow is developed
in the inner region. (Fig. 4). Such cooling ﬂows, commonly
seen in similar models and simulations, may naturally in-
duce activities of the central supermassive black holes. The
feedback from such activities has been proposed to sub-
stantially reduce the net cooling (e.g. Mathews & Brighenti
2003; Fabian & Sanders 2009). While a study of this topic is
beyond the scope of the present work, we here keep our fo-
cus on discussing the morphological and physical properties
of the outﬂow cases, which probably represent more typical
cases of galactic coronae in the ICM.
For all the n2T2M3 cases, coronae fail to form due to
the high thermal and ram pressures, leaving only a track
with high iron abundance (Fig. 5). In each of these cases,
the density peaks away from the spheroid center.
Fig. 6 show outlines of the coronae. These outlines
are represented by the iso-abundance contours of the value
of Z⊙, or approximately the contact discontinuity between
corona gas purely ejected by the spheriods and the ICM.
The characteristic size of a corona is sensitive to the ther-
mal pressure of the surrounding ICM as can be seen in panel
(a) of Fig. 6. The corona in the ICM of n1T1, which is typical
of a group or poor cluster, is more than 10kpc across, while
the corona in the ICM of n2T2, which is typical of the core
region of a relatively rich cluster, is less than 3kpc across.
The motion of the host galaxy relative to the surrounding
medium, which is represented by the Mach number, mainly
inﬂuences lopsidedness of a corona. In the subsonic case, the
0.0
0.2
0.4
0.6
0.8
1.0
Z /Zsolar
-4.0
-3.5
-3.0
-2.5
-2.0
-1.5
lg(n /cm-3)
6.6
6.8
7.0
7.2
7.4
7.6
7.8
8.0
lg(T /K)
-40
-20
0
20
z /kpc
8.0
8.5
9.0
9.5
10.0
10.5
lg(S)
Figure 3. Iron abundance, denisty, temperature, and entropy
distributions along z-axis of the simulation of case n1T2M2β2.
The thick solid lines are time-averaged proﬁles over a time span
from 250 to 300 Myr (the residual wigglers are present due the
the limited number of snapshots used in averaging), while the
thin lines are extracted from several snapshots. The horizontal
red line in the temperature panel corresponds to T =
β
2.5kB .
0
1
2
3
4
5
-4
-2
0
2
4
0
1
2
3
4
5
r /kpc
-4
-2
0
2
4
z/kpc
0.4
0.5
0.6
0.7
0.8
0.9
1.0
0
1
2
3
4
5
-4
-2
0
2
4
0
1
2
3
4
5
r /kpc
-4
-2
0
2
4
z/kpc
-3
-2
-1
0
1
Figure 4. Iron abundance and density distributions in the
n1T2M1β1 case. The arrows represent the velocity ﬁeld. Note
the central density peak (the red spot) at the very center.
corona is almost spherical, while in the supersonic case with
the Mach number as high as 1.8, the corona is signiﬁcantly
narrowed and elongated. As the input energy of the stellar
feedback increases, the lopsidedness increases. This is not
surprising. As the stellar feedback becomes more energetic,
the density of the corona gas will be lower. As a result, the
gravitational restoring force become less important, com-
pared with the ram pressure.


## Page 6


6
0
1
2
3
4
5
-4
-2
0
2
4
0
1
2
3
4
5
r /kpc
-4
-2
0
2
4
z/kpc
0.4
0.5
0.6
0.7
0.8
0.9
0
1
2
3
4
5
-4
-2
0
2
4
0
1
2
3
4
5
r /kpc
-4
-2
0
2
4
z/kpc
-3.0
-2.8
-2.6
-2.4
-2.2
Figure 5. Iron abundance and density distributions in the
n1T2M1β1 case, in which the corona fails to form.
0
2
4
6
8
10
r /kpc
-10
-5
0
5
10
z /kpc
(a)
n1T1β2M2
n2T1β2M2
n1T2β2M2
n2T2β2M2
2
4
6
8
10
ρ /kpc
(b)
n1T2β2M1
n1T2β2M2
n1T2β2M3
2
4
6
8
10
ρ /kpc
(c)
n1T2β2M2
n1T2β3M2
n1T2β4M2
Figure 6. Outlines of the simulated coronae. The outline for each
case is deﬁned to be the contour of the iron abundance equal to
Z⊙. The reference model n1T2M2β2 is represented with solid
line in all the three ﬁgures. Panels (a), (b) and (c) correspond
to variation in nT, Mach number and β, respectively, illustrat-
ing how the coronae respond to the changes of the surrounding
environment and stellar feedback.
The dependence of the corona temperature on the spe-
ciﬁc energy of injected material can be clearly seen in Fig. 7.
The peak value of the corona temperature is always roughly
β
2.5kB ; it drops slightly outwards largely due to the presence
of gravitational potential as described in § 3.1.
We plot the peak density values of the coronae in Fig. 8
and selected density proﬁle along the z-axis in Fig. 9, illus-
trating how the coronae respond to the changes of surround-
ing environment and inner stellar feedback. Generally, the
corona density depends strongly on the thermal pressure of
the surrounding medium, but only weakly on the ram pres-
sure. In our simulation, the the Mach number ranges from
0.6 to 1.8, with the ratio between the largest ram pressure
and the smallest one as high as 9, the corona density changes
slightly except for case n2T2M1β2 and its high Mach num-
ber version n2T2M2β2. This makes sense because unlike
thermal pressure, which compresses a corona from all direc-
tions, ram-pressure only acts on the front side and therefore
mostly pushes the gas backwards rather than compressing
it. The coronae in cases of n2T1 are compressed more than
those in cases of n1T2, although the ICM thermal pressure
-5
0
5
z /kpc
106
107
108
T /K
(a)
n1T1β2M2
n2T1β2M2
n1T2β2M2
n2T2β2M2
-5
0
5
z /kpc
(b)
n1T2β2M1
n1T2β2M2
n1T2β2M3
-5
0
5
z /kpc
(c)
n1T2β2M2
n1T2β3M2
n1T2β4M2
Figure 7. Temperature proﬁles along z-axis. The red horizontal
lines in (c) represent
β
2.5kB . The reference model n1T2M2β2 is
represented with solid line in all the three ﬁgures. Panels (a),
(b) and (c) correspond to variation in nT, Mach number and β
respectively, illustrating how the coronae respond to the changes
of the surrounding environment and stellar feedback.
1.2
1.8
3.0
4.8
β /keV
0.01
0.10
n /cm-3
n2T2
n1T2
n2T1
n1T1
Figure 8. Peak density values of the coronae. Cases with central
cooling ﬂow and those in which the coronae fail to form are not
shown. Cases with diﬀerent ICM thermal states are represented
with diﬀerent symbols, while diﬀerent Mach numbers are coded
in diﬀerent colors with red for 1.8, green for 1.2 and blue for 0.6.
To avoid overlap among the symbols, the higher Mach number
models are shifted to the right a litte bit and the subsonic cases
to the left.
is the same. This is caused by larger focusing eﬀect of grav-
itational force of the galaxy on the ICM with lower temper-
ature.
Fig. 10 includes the luminosity of each simulated corona
in the 0.3 −2.0 keV X-ray band. For simplicity, we use the
iron abundance distribution to deﬁne the shape of a corona
as what we do to plot the outline of a corona. Every grid
point with iron abundance equal to the solar value is in-
cluded to measure the luminosity. The emissivity is a func-
tion that depends on both temperature and metallicity. If
we assume the metals, mostly iron, produced by Ia SNe, are
fully mixed in the corona gas, the total luminosity would be
enhanced by a factor of about 3. It is clear that the lumi-
nosity decreases with the increasing Mach number and/or β.
But the dependence on the ICM thermal pressure is not that
simple: the luminosity tends to increase with the pressure in


## Page 7


Galactic Coronae in the ICM
7
-5
0
5
z /kpc
0.001
0.010
0.100
n /cm-3
(a)
n1T1β2M2
n2T1β2M2
n1T2β2M2
n2T2β2M2
-5
0
5
z /kpc
(b)
n1T2β2M1
n1T2β2M2
n1T2β2M3
-5
0
5
z /kpc
(c)
n1T2β2M2
n1T2β3M2
n1T2β4M2
Figure 9. Density proﬁles along z axis. The reference model
n1T2M2β2 is represented with the solid lines. Panels (a), (b)
and (c) show the dependence on nT, Mach number, and β, re-
spectively.
1.2
1.8
3.0
4.8
β /keV
0.01
0.10
1.00
10.00
L /1039erg s-1
n2T2
n1T2
n2T1
n1T1
Figure 10. Luminosity of the coronae. Cases with central cooling
ﬂow and those in which the coronae fail to form are not shown.
Cases with diﬀerent ICM thermal states are represented with dif-
ferent symbols, while diﬀerent Mach numbers are coded in diﬀer-
ent colors with red for 1.8, green for 1.2 and blue for 0.6. To avoid
overlap among the symbols, the higher Mach number models are
shifted to the right a litte bit and the subsonic cases to the left.
subsonic cases (lower Mach numbers), while the trend goes
in the opposite direction in the supersonic cases.
4
DISCUSSION
The above results give a basic characterization of galactic
coronae powered by stellar feedback and semi-conﬁned by
the thermal and ram prssures of the ICM. In this section,
we ﬁrst give a physical account of the apparent ICM im-
pacts on the corona characteristics as described above, then
compare the results with observations to constrain the stel-
lar feedback, and ﬁnally discuss the implications for other
galactic properties.
Table 2. α for various cases.
β1
β2
β3
β4
n1, T1
0.99
1.47
2.30
3.33
n2, T1
0.33
0.49
0.77
1.11
n1, T2
0.33
0.49
0.77
1.11
n2, T2
0.11
0.16
0.25
0.37
4.1
ICM Impacts on the Coronae
The properties of a corona are aﬀected by several competing
processes, the stellar feedback, the galaxy gravitational at-
traction, and the thermal/ram pressures of the ICM. In the
simplest case, when the gravity and external pressure can
be neglected, the density at the center would then be deter-
mined entirely by the mass/energy injection. In this case,
we can deﬁne a characteristic density as
ρc,1 = 3
4π
˙M
a3 τ.
(10)
Here τ =
a
cs is the dynamic time scale of the corona, where
cs is the sound speed. Considering that the temperature is
determined by the speciﬁc energy β, the characterisitic value
of the pressure is
Pc,1 = 3
4π
˙M
a2
p
(γ −1)β
γ
.
(11)
In the other extreme, when the gravity is important
(i.e., the corona is nearly hydrostatic), the Mach number of
the outﬂow must be low. Clearly, in this case, the external
thermal pressure becomes important as well. Because the
corona is nearly isothermal, the pressure distribution is
ln(P) = ln(P0) −µmp(Φ −Φ0)
kBT
,
(12)
where P0 is the pressure at the outer boundary and Φ −Φ0
is the gravitational potential diﬀerence. Assuming that the
corona size is considerably larger than the scale a of the
stellar spheroid, we obtain a characteristic peak pressure as
Pc,2 = PICM exp
 
GMs
a
r
γ
(γ −1)β
!
.
(13)
To characterize the relative importance of the feedback to
the gravity, we deﬁne a dimensionless parameter as
α = Pc,1
Pc,2 .
(14)
The values of this parameter for the simulated cases are
listed in Table.2. Fig. 11 compares the hydrostatic solu-
tions (Eq. 13) to the simulations with three diﬀerent α pa-
rameters. In those cases with small α, such as n2T2M1β2,
in which the gravity dominates over the feedback, the hy-
drostatic solutions give nearly perfect matchs to the simu-
lated pressure proﬁles. While in a case like n1T1M1β4 (with
α = 3.3), where the feedback dominates, the deviation of the
hydrostatic solution from the simulated proﬁle is apparent.
For the cases which we think are plausible (β=1.8keV, see
§ 4.2), α is about 1.0 or much less than 1.0, and the coronae
are largely in hydrostatic state.
Although the same model galaxy (in terms of the stellar
and dark matter masses) is adopted for all the simulation


## Page 8


8
-5
0
5
0
z /kpc
10-12
10-11
10-10
P /dyncm-2
n2T2M1β2
α=0.16
-5
0
5
0
z /kpc
n1T1M1β2
α=1.5
-5
0
5
0
z /kpc
n1T1M1β4
α=3.3
Figure 11. Comparison between numerical pressure proﬁles and
the theoretical proﬁles with isothermal assumption. The solid
lines are the pressure proﬁles extracted from the simulations and
the dashed lines represent the corresponding hydrostatic solu-
tions. The region inside the coronae is colored in red. In each of
the panels, the peaks of both of the numerical proﬁle and theo-
retical one are positioned at the same point.
cases, the resultant X-ray luminosities can still diﬀer by up
to two orders of magnitude, due to the diﬀerent choices of
the Mach number, β, and/or thermal pressure values of the
ICM. Because the corona temperature is determined by β,
the gas density is
nc ∼PICM
β
,
(15)
if the corona is in a nearly hydrostatic state. Therefore, the
surface brightness of a corona provides a measure of the
ambient ICM pressure and thus may be used to estimate
the line-of-sight position in a cluster.
However, the X-ray luminosity of a corona depends
on several factors. Fig. 10 shows a clear anti-correlation
between the luminosity and speciﬁc energy β. This anti-
correlation is primarily due to the density decrease with the
increase of β, although it does not strongly aﬀect the size
of a corona. The ICM thermal pressure tends to squeeze
the corona, hence enhance its luminosity (subsonic cases).
But this eﬀect is complicated by the presence of the ram-
pressure. As the Mach number increases, the lumonosity
can decrease because the ram-pressure stripping reduces the
overall size ofthe corona. These dependences on the environ-
ment as well as the stellar feedback energetics may naturally
explain the observed large dispersion of Lx/LK for spheroids
of similar LK. The complications in the dependences may
also account for the lack of a clear observed trend in the
ICM environment eﬀect on X-ray luminosities of coronae
(Sun et al. 2007; Mulchaey & Jeltema 2010).
4.2
Implication for the Feedback Model
In our model of the galactic coronae, the gas temperature
is primarily determined by the speciﬁc energy of the stellar
feedback and thus should not change signiﬁcantly with the
stellar mass. This independence on the mass or LK is consis-
tent with the temperature measurements of the coronae of
intermediate-mass spheroids (David et al. 2006; Sun et al.
2007; Jeltema et al. 2008; Boroson et al. 2010). This is in
contrast to the correlation between the temperature and
LB for more massive systems such as clusters and groups
of galaxies (Helsdon & Ponman 2003). In particular, galaxy
clusters show a well-deﬁned scaling law between the temper-
ature and luminosity of the observed hot gas, which is a nat-
ural result of the predominant gravitational heating in the
self-similar cluster formation. The scaling law for lower mass
systems (e.g., groups of galaxies) is known to be slightly
diﬀerent from that for clusters (e.g., showing an ’entropy
ﬂoor’), which is believed to be an imprint of preheating(e.g.,
starburst and early AGNs). Correlation between LB and the
temperature of hot gas is observed in massive X-ray-bright
elliptical galaxies, especially for central galaxies in groups
and clusters (e.g,, O’Sullivan et al. 2003). But the entropies
are found lie below the entropy ﬂoor(∼109 K cm−2) discov-
ered in groups of galaxies. Radiative cooling could account
for the low entropy, although how this runaway process may
be balanced by the heating due to the mechanical inputs
from both stellar and AGN feedbacks remains unclear. We
have shown that the low value and the positive radial gra-
dient of the entropy are expected from the distributed feed-
back in intermediate-mass spheroids, in which the radiative
cooling is not important. Therefore, we may conclude that
the coronae of intermediate-mass spheroids represent the ex-
treme case in which the stellar feedback plays a dominant
role, which means they are produced by stellar mass loss
and heated by SNe.
We may further constrain the stellar feedback based
on the measured temperature of the coronae. Though with
a relative large dispersion, the measured temperatures are
mostly fall in the range of 0.5 −1.0 keV, which is signiﬁ-
cantly higher than those measured in ﬁeld spheroids, but is
still substantially lower than what is inferred from our 2-
D simulations if the canonical speciﬁc energy value of the
stellar feedback is assumed (∼5 keV; see § 2). Part of this
discrepancy could still be due to the 3-D eﬀects of discrete
heating by Ia SNe, as mentioned in § 1 (and characterized
in Tang et al. 2009b; Tang & Wang 2010). But we expect
that such eﬀect should be substantially weaker in the com-
pact coronae embedded in the high pressure ICM and that
the measured temperature should more faithfully reﬂect the
speciﬁc energy of the feedback. To match the measured tem-
perature range of the coronae requires a specﬁc energy of
∼1.5 −3 keV, or a factor of ∼2 −3 lower than the canon-
ical value (5 keV; § 2). This factor is probably still within
the uncertainties of the semi-emipirical mass and energy in-
jection rates. Further, the assumed mechanical energy per
Ia SN could be somewhat (e.g., a factor of ∼2) less than
1051 ergs. Also a considerable fraction of the energy can be
used to generate cosmic rays, magnetic ﬁeld and turbulent
motion. The diversion of the energy into these various forms
could signiﬁcantly reduces the temperature, although the
hydrodynamics of the coronae, hence the density and pres-
sure distributions, should not be signiﬁcantly aﬀected. The
simulated coronae with β = 1.8 keV generally have individ-
ual luminosties of a few times 1039 erg s−1, consistent with
the observed range of 1039 ∼1040 erg s−1 (Sun et al. 2007).
A considerably large value of β is not favored, because it
decreases the expected luminosity steeply (Fig. 10).
4.3
Impliﬁcations for Understanding Other
Galactic Components
We discuss here the potential impacts of the pressure or
density enhancement of the coronae on the fueling of the
central SMBHs and the evolution of cool gas, if present in
the spheroids.


## Page 9


Galactic Coronae in the ICM
9
1.2
1.8
3.0
4.8
β /keV
0.1
1.0
10.0
100.0
P / 1042erg s-1
n2T2
n1T2
n2T1
n1T1
Figure 12. Estimated AGN power. Cases with cooling ﬂow and
those in which the coronae fail to form are not shown. Diﬀerent
ICM thermal states are represented with diﬀerent symbols and
diﬀerent Mach numbers are coded in diﬀerent colors with red for
1.8, green for 1.2 and blue for 0.6. To avoid overlap among the
symbols, the higher Mach number models are shifted to the right
a litte bit and the subsonic cases to the left.
The simulation shows that the central density of a
corona is sensitive to the thermal pressure of the surround-
ing medium. To infer the power of a SMBH, we adopt the
Bondi accretion rate (Edgar 2004):
˙M = 4πG2M 2
BHρ
c3s
.
(16)
where MBH is the mass of the SMBH, while ρ and cs are the
density and sound speed at the center of a corona. Assuming
the fraction of the accretion energy released is η = 0.1, the
power of the SMBH can be approximated as
2.12×1041 erg s−1 MBH
108 M⊙
2
n
cm−3

T
7.0 × 107 K
−1.5
(17)
The SMBH mass can be estimated from its correlation with
the spheroid mass MBH ∼0.006Mbulge (Magorrian et al.
1998). Fig. 12 shows the dependence of the power on the
ICM state, the Mach number of spheroid, and the speciﬁc
energy of the feedback.
In particular the luminosity for the most plausible β2
cases is about 1043 erg s−1, which falls in the range of the
X-ray power of a low luminosity AGN. This indicates that
a compact corona built up by stellar feedback and embed-
ded in cluster environment could feed a moderate AGN. The
ICM pressure also tends to enhance the accretion, consistent
with the ﬁnding that the galaxies with Lx > 1042 erg s−1
AGNs are more centrally concentrated than ones without
(Martini et al. 2007). These galaxies with AGNs are not
dominated by galaxies that have recently entered the clus-
ters. Similar conclusions are also reached in more recent
studies, such as the one by Hart et al. (2009), based on the
analysis of a sample of P1.4GHz > 3 × 1023 WHz−1 radio
galaxies and L0.3−8keV > 1042 erg s−1 point sources.
The pressure enhancement could also have signiﬁ-
cant impacts on cool gas in a galaxy. Under high pres-
sure, cool gas exists preferentially in molecular form rather
than atomic one. The compression of cold gas because
of the ICM pressure could further lead to star forma-
tion (Bekki & Couch 2003), depriving the galaxy of the
gas further. Thus it is expected that galaxies contain less
amounts of cool gas in clusters than in the ﬁeld. These
impacts should aﬀect cool gas not only in spheroids, but
in spirals as well, consistent with existing observations
(Young & Scoville 1991).
5
SUMMARY
We have conducted a range of 2-D hydrodynamic simual-
tions of galactic coronae that result from gradual energy
and mass feedback in stellar spheroids moving in the ICM
enviornment. We have focused on spheroids that are in the
intermediate-mass range (corresponding to LK ∼1011 −
1012LK,⊙) so that both the AGN feedback and the radia-
tive cooling of the hot gas could largely be neglected. We
explore the dependence of corona properties on the speciﬁc
energy of the stellar feedback as well as on the ram and ther-
mal pressures of the ICM. Our major results and conclusions
are as follows:
(i) X-ray coronae embedded in clusters could be naturally
explained by the subsonic outﬂow driven by the stellar feed-
back, semi-conﬁned by the ram-pressure and compressed by
thermal pressure of the surrounding ICM. The corona tem-
perature depends primarily on the speciﬁc energy of the in-
put material in such a way that T ∼
β
2.5kB . The decrease
of the thermal energy due to the climbing of the gravita-
tional potential and the expansion is largely compensated
by the distributed heating by Ia SNe. This result naturally
explains the lack of the correlation between the temperature
and K-band luminosity for the spheroids in our considered
mass range. An outﬂow powered by a distributed feedback
also has a positive radial entropy proﬁle, mimicking what
may be produced by a ”cooling ﬂow”.
(ii) The coronal gas is typically in an approximate hydro-
static state. As a result, the density of the corona gas de-
pends strongly on the thermal pressure of the ICM, but only
weakly on the ram pressure. Therefore, the surface bright-
ness of X-ray emission is a good measurement of the thermal
ICM pressure, which may be used to estimate the line-of-
sight location of a spheroid in a cluster. The total X-ray
luminosity of a corona decreases with the increase of the
feedback speciﬁc energy. The thermal pressure tends to in-
crease (or reduce) the luminosity in subsonic (supersonic)
cases.
(iii) The semi-conﬁnement of the coronae by the ICM al-
lows a good constraint on the energetics of the stellar feed-
back. To be consistent with the observed X-ray luminos-
ity and temperature, the speciﬁc energy of the feedback
should be ∼1.5 −3 keV, a factor of 2-3 smaller than the
value inferred from the commonly accepted semi-empirical
Ia SN and mass-loss rates, assuming the mechanical energy
of 1051 ergs s−1 per SN.
(iv) The relatively high pressure of the coronae in the
ICM may have important implications for understanding the
AGN activity as well as the cool gas properties in spheroids.
The density increase caused by the ICM pressure, for exam-
ple, could enhance the Bondi accretion, which may explain
the observed central concentration of AGNs in clusters. The


## Page 10


10
high pressure can further compress the gas to form molec-
ular clouds and enhance star formation. The combination
of the enhanced consumption and the ram-pressure striping
can naturally lead to the deprivation of gas and subsequent
passive evolution of galaxies in clusters.
6
ACKNOWLEDGEMENTS
We thank S.-K. Tang for his help in the initial setting up
of the simulations. The software used in this work was in
part developed by the DOE-supported ASC/Alliance Center
for Astrophysical Thermonuclear Flashes at the University
of Chicago. Simulations were performed at the Pittsburgh
Supercomputing Center supported by the NSF. The project
is partly supported by NASA through grant NNX10AE85G.
REFERENCES
Acreman D.M., Stevens I.R., Ponman T.J. & Sakelliou I.,
2003, MNRAS, 341, 1333
Bekki K. & Couch W.J., 2003, ApJ, 596, 13
Boroson
B.,
Kim
D.W.
&
Fabbiano
G.,
2010,
arXiv:1011.2529v1
David L.P., Jones C., Forman W., Vargas I.M., & Nulsen
P., 2006, ApJ, 653, 207
Edgar R.G., 2004, New Astron. Rev., 48, 843
Eke V.R., Navarro J.F. & Steinmetz M., 2001, ApJ, 554,
114
Fabian A.C., & Sanders J.S., 2009, arXiv:0909.2577
Fryxell B., Olson K., Ricker P., Timmes F.X., Zingale M.,
Lamb D.Q., MacNeice P., Rosner R., Truran J. W., &
Tufo H., 2000, ApJS, 131, 273
Hart Q.N., Stocke J.T. & Hallman E.J., 2009, ApJ, 705,
854
Helsdon S.F. & Ponman T.J., 2003, MNRAS, 340, 485
Hernquist L., 1990, ApJ, 356, 359
Jeltema T. E., Binder B., & Mulchaey J. S., 2009, ApJ,
679, 1162
Kim D.-W., Kim E., Fabbiano G., & Trinchieri G., 2008,
ApJ, 688, 931
Knapp G.R., Gunn J.E., & Wynn-Williams C.G., 1992,
ApJ, 399, 76
Li Z., Wang Q.D., Irwin J.A., & Chaves T., 2006, MNRAS,
371, 147
Li Z., & Wang Q.D., 2007, ApJ, 668, 39
Li Z., Wang Q.D., & Hameed S., 2007, MNRAS, 376, 960
Machacek M., Dosaj A., Forman W., Jones C., Markevitch
M., Vikhlinin A., Warmﬂash A., & Kraft R., 2005, ApJ,
621, 663
Machacek M., Jones C., Forman W.R., & Nulsen P., 2006,
ApJ, 644, 155
Magorrian J., Tremaine S., Richstone D., Bender R., Bower
G., Dressler A., Faber S.M., Gebhardt K., Green R., Grill-
mair C., Kormendy J., Lauer T., 1998, AJ, 115, 2285
Mannucci F., Della Valle M., Panagia N., Cappellaro E.,
Cresci G., Maiolino R., Petrosian A., & Turatto M., 2005,
AA, 433, 807
Martini P., Mulchaey J.S. & Kelson D.D., 2007, ApJ, 664,
761
Mathews W.G. & Brighenti F., 2003, ARAA, 41, 191
Mulchaey J.S. & Jeltema T.E., 2010, ApJ, 751, L1
Navarro J.F., Frenk C.S., & White S.D.M., 1997, ApJ, 490,
493
O’Sullivan E., Ponman T.J., & Collins R.S., 2003, MNRAS,
340, 1375
Sato S. & Tawara Y., 1999, ApJ, 514, 765
Stevens I.R., Acreman D.M. & Ponman T.J., 1999, MN-
RAS, 310, 663
Sun M., Jones C., Forman W., Nulsen P.E.J., Donahue M.,
& Voit G.M., 2006, ApJ, 637, 81
Sun M., Jones C., Forman W., Vikhlinin A., Donahue M.,
& Voit M., 2007, ApJ 657, 197
Sutherland R.S. & Dopita M.A., 1993, ApJS, 88, 253
Tang S., & Wang Q.D. 2010, MNRAS, in press
Tang S., Wang Q.D., Lu Y., & Mo H., 2009, MNRAS, 392,
77
Tang S., Wang Q.D., MacLow M., & Joung M.R., 2009,
MNRAS, 398, 1468
Temi P., Brighenti F., & Mathews W.G., 2008, ApJ, 672,
244
Toniazzo T. & Schindler S., 2001, MNRAS, 325, 509
Wang Q.D., 2010, PNAS, 107, 7168
Young J.S. & Scoville N.Z., 1991, ARAA, 29, 581

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

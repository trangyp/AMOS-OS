---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1904.01699v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1904.01699v2_Resolution_Study_for_Three-dimensional_Supernova_Simulations_with_the_Prometheus

> Source: 1904.01699v2_Resolution_Study_for_Three-dimensional_Supernova_Simulations_with_the_Prometheus.pdf

> Pages: 37

---


## Page 1


Draft version February 4, 2020
Preprint typeset using LATEX style AASTeX6 v. 1.0
RESOLUTION STUDY FOR THREE-DIMENSIONAL SUPERNOVA SIMULATIONS WITH THE
PROMETHEUS-VERTEX CODE
Tobias Melson1, Daniel Kresse1,2, and Hans-Thomas Janka1
1Max-Planck-Institut f¨ur Astrophysik, Karl-Schwarzschild-Str. 1, 85748 Garching, Germany
2Physik-Department, Technische Universit¨at M¨unchen, James-Franck-Str. 1, 85748 Garching, Germany
ABSTRACT
We present a carefully designed, systematic study of the angular resolution dependence of simula-
tions with the Prometheus-Vertex neutrino-hydrodynamics code. Employing a simpliﬁed neutrino
heating-cooling scheme in the Prometheus hydrodynamics module allows us to sample the angular
resolution between 4◦and 0.5◦. With a newly-implemented static mesh reﬁnement (SMR) technique
on the Yin-Yang grid, the angular coordinates can be reﬁned in concentric shells, compensating for the
diverging structure of the spherical grid. In contrast to previous studies with Prometheus and other
codes, we ﬁnd that higher angular resolution and therefore lower numerical viscosity provides more
favorable explosion conditions and faster shock expansion. We discuss the possible reasons for the
discrepant results. The overall dynamics seem to converge at a resolution of about 1◦. Applying the
SMR setup to marginally exploding progenitors is disadvantageous for the shock expansion, however,
because kinetic energy of downﬂows is dissipated to internal energy at resolution interfaces, leading
to a loss of turbulent pressure support and a steeper temperature gradient. We also present a way
to estimate the numerical viscosity on grounds of the measured turbulent kinetic-energy spectrum,
leading to smaller values that are better compatible with the ﬂow behavior witnessed in our simula-
tions than results following calculations in previous literature. Interestingly, the numerical Reynolds
numbers in the turbulent, neutrino-heated postshock layer (some 10 to several 100) are in the ballpark
of expected neutrino-drag eﬀects on the relevant length scales. We provide a formal derivation and
quantitative assessment of the neutrino drag terms in an appendix.
Keywords: supernovae:general — hydrodynamics — instabilities — convection — turbulence — neu-
trinos
1. INTRODUCTION
The explosion mechanism of core-collapse supernovae,
whether energized by neutrino heating or mediated
by magnetic ﬁelds, is a generically multi-dimensional
phenomenon, in which hydrodynamic instabilities play
a crucial role.
They do not only foster the explo-
sion but also create initial asymmetries that determine
the emerging geometry of the stellar blast.
Three-
dimensional (3D) hydrodynamical simulations are there-
fore indispensable, and because of the increasing power
of modern massively parallel supercomputers they have
recently become possible in combination with elaborate
energy-dependent three-ﬂavor neutrino transport (for a
review of recent developments, see Janka et al. 2016).
Correspondingly, the pool of 3D stellar core-collapse
and explosion simulations with substantially diﬀerent
treatments of neutrino transport and physics is growing
rapidly (e.g., Takiwaki et al. 2012, 2014; Melson et al.
2015a,b; Lentz et al. 2015; Roberts et al. 2016; M¨uller
et al. 2017, 2019; Summa et al. 2018; Ott et al. 2018;
O’Connor & Couch 2018; Kuroda et al. 2018; Glas et al.
2019; Vartanyan et al. 2019; Burrows et al. 2019).
These simulations were conducted with diﬀerent grid
geometries (Cartesian grids with static or adaptive mesh
reﬁnement, cubed-sphere multi-block grids, polar coor-
dinates, Yin-Yang spherical grids, spherical grids with
polar mesh coarsening) and with largely diﬀerent numer-
ical resolutions. While a number of resolution studies
have already been performed by varying, within rather
close limits, the mesh spacing for ﬁxed grid geometries
(e.g., Hanke et al. 2012; Couch & O’Connor 2014; Ab-
dikamalov et al. 2015; Roberts et al. 2016; Radice et al.
2016; Summa et al. 2018; O’Connor & Couch 2018), pos-
sible numerical artifacts of the grid geometries them-
selves are still completely unexplored in 3D supernova
calculations.
The recognition that nonradial mass motions and
buoyant bubble rise in the neutrino-heating layer have
an impact on the shock evolution that can be coined
in terms of turbulent (pressure, energy transport, dissi-
arXiv:1904.01699v2  [astro-ph.HE]  3 Feb 2020


## Page 2


2
T. Melson, D. Kresse, & H.-T. Janka
pation) eﬀects (e.g., Murphy et al. 2013; Couch & Ott
2015; M¨uller & Janka 2015; Radice et al. 2016; Mabanta
& Murphy 2018), has led to increasing interest in the res-
olution dependence of the turbulent kinetic-energy cas-
cade for the postshock ﬂow in supernova models (Ab-
dikamalov et al. 2015; Radice et al. 2015, 2016, 2018).
Low resolution can be imagined to cause enhanced nu-
merical viscosity, which might quench the growth of con-
vective buoyancy, damp nonradial ﬂows, and lead to vis-
cous dissipation of kinetic energy and associated numeri-
cal heating. In the regime where growth of the standing
accretion-shock instability (SASI; Blondin et al. 2003;
Blondin & Mezzacappa 2007) rather than neutrino-
driven convection is favored (see Foglizzo et al. 2006,
2007), low radial resolution can suppress the growth of
SASI (Sato et al. 2009), whereas reduced angular resolu-
tion can strengthen SASI activity because of weaker or
absent parasitic Kelvin-Helmholtz and Rayleigh-Taylor
instabilities, which would redistribute kinetic energy
from the large SASI scales to vortex ﬂows on smaller
scales (Guilet et al. 2010). These expectations from the-
oretical and toy-model considerations are in line with
full-ﬂedged supernova simulations (Summa et al. 2018).
Moreover, Radice et al. (2015, 2016) diagnosed the so-
called bottleneck eﬀect, where the lack of resolution pre-
vents kinetic-energy cascading to small scales and leads
to an accumulation of kinetic energy on scales larger
than the dissipation scale. For this reason the turbulent
energy spectra exhibit enhanced power on these scales
and display a more shallow decline than expected in
the inertial range from Kolmogorov’s classical theory.
The authors argued that this circumstance might ex-
plain why in previous studies by Hanke et al. (2012)
with the Prometheus supernova code—and conﬁrmed
by others (e.g., Couch & O’Connor 2014; Abdikamalov
et al. 2015; Roberts et al. 2016) with diﬀerent numeri-
cal methods—lower resolution had fostered earlier and
stronger explosions in 3D simulations.
In the present work we report results of a recent, care-
fully designed resolution study with the Prometheus-
Vertex code, sampling angular cell sizes between 4◦
and 0.5◦in full-4π simulations of the post-bounce evo-
lution of collapsing and exploding 9 M⊙and 20 M⊙
stars. We employ full-ﬂedged ray-by-ray neutrino trans-
port with state-of-the-art neutrino interactions, or, al-
ternatively for systematic resolution variations, a sim-
ple neutrino-heating and cooling scheme in the form of
an improved version of the treatment by Hanke et al.
(2012).
Our results reveal exactly the opposite resolution de-
pendence compared to previous investigations, namely
that better resolution leads to improved explosion con-
ditions and faster shock expansion in 3D. Our results
challenge the interpretation of the previous ﬁndings as
discussed by Couch & O’Connor (2014), Abdikamalov
et al. (2015), and Radice et al. (2016). We understand
the behavior witnessed in our models as a consequence
of the fact that lower numerical viscosity in the case of
higher resolution permits an enhanced level of nonradial
(turbulent) kinetic energy in the postshock layer. The
conﬂict with the simulations by Hanke et al. (2012) can
be resolved when one takes into account the numerical
artifacts associated with the polar axis of the spheri-
cal coordinate grid used in those older simulations. In
contrast, the supernova models generated in the present
work employed the axis-free Yin-Yang grid (Kageyama
& Sato 2004; Wongwathanarat et al. 2010). The Yin-
Yang grid reduces numerical artifacts to a much lower
level by avoiding axis features as well as eﬀects caused
by the nonuniform sizes of azimuthal grid cells at dif-
ferent latitudes, which implies ﬁner spatial resolution
near the poles. The question arises why Cartesian 3D
simulations reproduced the polar-axis-triggered resolu-
tion trend seen by Hanke et al. (2012). We speculate,
however without having any foundation by own results,
that numerical noise induced on radial ﬂows by Carte-
sian grids could play an important role. A decreased
level of such perturbations when the resolution was im-
proved, might have delayed the onset of explosions in
the better-resolved simulations performed by Couch &
O’Connor (2014), Abdikamalov et al. (2015), Roberts
et al. (2016) and O’Connor & Couch (2018).
We also discuss results obtained with a static mesh
reﬁnement (SMR) technique that we implemented on
the Yin-Yang grid of the Prometheus-Vertex code.
Despite oﬀering enhanced angular resolution in the tur-
bulent postshock layer, it turned out to have an unfa-
vorable inﬂuence on the onset and development of explo-
sions in cases that were marginally hitting success. We
could trace this back to a conversion of kinetic energy
to thermal energy (with the sum of both conserved) in
mass ﬂows crossing the borders from grid domains with
better to those with coarser resolution. This might sug-
gest additional artifacts that could be associated with
the use of static or adaptive mesh reﬁnement procedures
used in most applications of Cartesian grids.
Our resolution study indicates that convergence of the
shock evolution might be approached at an angular res-
olution of about 1◦. An even more detailed realization
of the turbulent power spectrum than it is possible with
this resolution seems to have a minor impact on the over-
all post-bounce dynamics in the supernova core, as most
of the energy is contained on the largest scales. Increas-
ing the resolution beyond this point to accurately follow
the turbulent energy cascade needs to take into account
the eﬀects of neutrino drag, because even for our lowest-
resolved simulations neutrino-drag eﬀects begin to com-
pete with the consequences of numerical viscosity on all


## Page 3


Resolution Study with Prometheus-Vertex
3
scales that yield relevant contributions to the turbulent
kinetic energy. We provide detailed estimates of the nu-
merical viscosity and Reynolds number (deduced from
the numerically realized turbulent kinetic energy spec-
trum) as well as, in an extended appendix, a detailed
discussion of the neutrino-drag eﬀects in the gain layer
behind the supernova shock.
Our paper is structured as follows. In Section 2, we
brieﬂy describe the numerical setup of our models. The
results of our 3D simulations with Vertex neutrino
transport are discussed in Section 3.
Our systematic
resolution study employing the simple neutrino-heating
and cooling scheme is presented in Section 4. In Sec-
tion 5, we focus on a discussion of turbulence in our
models and present our method of deducing the numer-
ical viscosity. An assessment of our results in a broader
context is the contents of Sect. 6, followed by our sum-
mary and conclusions in Section 7. Appendix A provides
a concise description of our SMR technique, and Ap-
pendix B contains a detailed derivation of the neutrino-
drag terms with order-of-magnitude estimates for su-
pernova conditions as well as an evaluation based on
simulation results with full neutrino transport.
2. NUMERICAL SETUP
We performed one-dimensional (1D), two-dimensional
(2D), and three-dimensional (3D) core-collapse super-
nova
simulations
using
two
neutrino
treatments.
The
ﬁrst
set
of
models
was
computed
with
the
Prometheus-Vertex code (Rampp & Janka 2002;
Buras et al. 2006), whereas the second model set
was simulated using only the hydrodynamics module
Prometheus (Fryxell et al. 1989, 1991; M¨uller et al.
1991) with a simpliﬁed heating-cooling (HTCL) scheme,
based on an improved version of the treatment applied
by Hanke et al. (2012).
Prometheus is an imple-
mentation of the Piecewise Parabolic Method (PPM;
Colella & Woodward 1984)—a Godunov-type scheme
being second-order accurate in space and second-order
in time.
In all simulations presented in this work, the col-
lapse phase was computed in spherical symmetry with
the Prometheus-Vertex code using multi-group neu-
trino transport and state-of-the-art neutrino interac-
tions. Gravity was treated in spherical symmetry with
general-relativistic corrections (Marek et al. 2006, Case
A). The high-density equation of state by Lattimer &
Swesty (1991) with a nuclear incompressibility of K =
220 MeV was employed.
For the present study, we selected various angular grid
resolutions, while the radial grid was kept unchanged for
a given progenitor for comparison. In addition to 3D
simulations with uniform angular resolution in the whole
computational domain, we also made use of a newly-
implemented static mesh reﬁnement (SMR) procedure.
It allows us to change the angular resolution in radial
layers of the spherical grid. A detailed description of
this method can be found in Appendix A.
In Table 1, we present an overview of all simulations
discussed in this work.
2.1. Models with neutrino transport
The
ﬁrst
model
set
was
computed
using
the
Prometheus-Vertex code with three-ﬂavor, energy-
dependent, ray-by-ray-plus neutrino transport including
state-of-the art neutrino interactions. We simulated the
post-bounce evolution of a 9 M⊙star (s9.0; Woosley &
Heger 2015) and a 20 M⊙progenitor (s20; Woosley &
Heger 2007). When mapping from 1D to 3D at 10 ms
after bounce, random cell-to-cell density perturbations
of 0.1 % were imposed to break spherical symmetry.
Besides a setup with uniform angular resolution of 3.5◦
and 2◦, respectively, we also used an SMR setup with
a ﬁrst reﬁnement step from 2◦to 1◦at the bottom of
the gain layer. To maintain a high resolution in the gain
layer over time, this SMR interface follows the contrac-
tion of the gain radius. A second reﬁnement region with
a resolution of 0.5◦was added at 70 ms after bounce ex-
terior to a ﬁxed radius of 160 km. Thus, the resolution
was improved twice by a factor of two.
The s20 simulation with a constant 2◦angular res-
olution was published before in Melson et al. (2015a)
and computed on a spherical polar grid with a core of
10 km treated spherically symmetrically. All other runs
in this model set were evolved on the Yin-Yang grid
(Kageyama & Sato 2004; Wongwathanarat et al. 2010)
with a smaller 1D core of 1.6 km radius. The radial grid
was gradually reﬁned from 400 zones to more than 600
to account for the steepening of the density gradient at
the proton-neutron star surface.
2.2. Models with simpliﬁed heating-cooling scheme
For the HTCL model set, the 20 M⊙progenitor from
Woosley & Heger (2007) was selected. The multi-dimen-
sional simulations were started from a 1D collapse run
and mapped to 2D/3D at 15 ms after bounce. At this
stage, random cell-to-cell density perturbations were im-
posed with an amplitude of 0.1 %.
The radial grid was set to 400 zones in all models and
kept constant in time. Since the proto-neutron star re-
mains larger in the HTCL simulations and no transport
is applied, this radial grid yields suﬃcient resolution,
compatible with what is used in Prometheus-Vertex
for neutron stars of similar radius. Note that the simpli-
ﬁed HTCL scheme is not subject to the same resolution
constraints as detailed neutrino transport.
Moreover,
the purpose of our simulations with the HTCL treat-
ment is not a most accurate description of the neutron


## Page 4


4
T. Melson, D. Kresse, & H.-T. Janka
Table 1. Overview of the simulations discussed in this work.
Model
Progenitor mass
Neutrino scheme
Dimensionality
Angular resolution
1D core
s9.0
9 M⊙
Full transport
3D (Yin-Yang grid)
3.5◦
1.6 km
3D (Yin-Yang grid)
SMR (up to 0.5◦)
1.6 km
s20
20 M⊙
Full transport
3D (Spherical polar grid)
2◦
10 km
3D (Yin-Yang grid)
SMR (up to 0.5◦)
1.6 km
HTCL 4.0
20 M⊙
HTCL with Lν,52 = 4
1D
-
-
2D
0.5◦to 4◦
1012 g cm−3
3D (Yin-Yang grid)
0.5◦to 4◦
1012 g cm−3
3D (Yin-Yang grid)
SMR (up to 0.5◦)
1012 g cm−3
HTCL 3.96
20 M⊙
HTCL with Lν,52 = 3.96
1D
-
-
2D
0.5◦to 4◦
1012 g cm−3
3D (Yin-Yang grid)
0.5◦to 4◦
1012 g cm−3
3D (Yin-Yang grid)
SMR (up to 0.5◦)
1012 g cm−3
Note— For all models, we list the model name, the zero-age main sequence mass of the progenitor, the treatment of the
neutrinos, the dimensionality including the grid setup (for 3D cases), the angular resolution, and the criterion (either radius or
density) for the outer boundary of the spherically symmetric inner core employed for relaxing the time step constraints near the
grid origin.
star and its near-surface layers, but instead the goal is
a study of turbulence and resolution eﬀects in the post-
shock domain.
The central region enclosed by the density contour
of 1012 g cm−3 was treated in spherical symmetry, cor-
responding to a radius of 42–46 km.
This radius is
considerably larger than in the simulations with full-
ﬂedged neutrino transport, because the simpliﬁed HTCL
scheme weakens the contraction of the proto-neutron
star. We will comment on the consequences of this fact
at several places in the discussion of our results.
All 3D simulations in this model set were computed
on the Yin-Yang grid. Besides the runs with a constant
angular resolution in the entire computational domain,
we used the SMR grid with a resolution of 2◦up to a
radius of 123 km and 1◦outside. At 150 ms after bounce,
an additional layer of 0.5◦angular resolution was added
outside a radius of 162 km, thus improving the resolution
a second time by a factor of two. Note that the imposed
initial perturbation patterns were identical in the SMR
case and the 2◦run.
The HTCL scheme was used already in a 3D study
by Hanke et al. (2012). However, our implementation
of this scheme and other aspects of our presented study
diﬀer in some details. First, Hanke et al. (2012) used a
spherical polar grid instead of the Yin-Yang grid. Sec-
ond, they employed a Newtonian gravitational potential
without general-relativistic corrections. Third, the high-
density equation of state of Lattimer & Swesty (1991)
with K = 180 MeV was used in their work. Also our
formulation of the heating and cooling terms was modi-
ﬁed compared to theirs. Our heating and cooling terms
read, respectively,
˙qheat =1.544 × 1020

Lν
1052 erg s−1
 100 km
r
2
×

Tν
4 MeV
2
(Yn + Yp) e−τeff/2 erg g−1 s−1,
(1)
and
˙qcool =1.399 × 1020

T
2 MeV
6
(Yn + Yp)
× e−τeff/2 erg g−1 s−1,
(2)
where r is the radius and T is the temperature.
Yn
and Yp are the neutron and proton number fractions,
respectively. Lν,52 ≡Lν/(1052 erg s−1) is a free parame-
ter with two diﬀerent values of 3.96 and 4.0 in this work.
The neutrino temperature Tν is set to 4 MeV. The ex-
ponential term τeﬀis given by
τeﬀ(r) =
Z ∞
r
dr′ κeﬀ(r′),
(3)
with
κeﬀ= 7.5 × 10−8

ρ
1010 g cm−3
 
Tν
4 MeV
2
cm−1,
(4)
where ρ is the mass density.
Because of the combination of all diﬀerences, the pa-
rameter Lν,52 in our scheme is about a factor of four
higher than in the work by Hanke et al. (2012) in order
to trigger shock revival.


## Page 5


Resolution Study with Prometheus-Vertex
5
0
100
200
300
400
500
600
⟨Rsh⟩[km]
s9.0
3D
SMR
3.5◦
0
100
200
300
400
500
600
⟨Rsh⟩[km]
s20
3D
SMR
2◦
0.0
0.1
0.2
0.3
0.4
tpb [s]
0.00
0.25
0.50
0.75
1.00
1.25
1.50
Egain
kin,θ,φ [1049 erg]
SMR
3.5◦
0.0
0.1
0.2
0.3
0.4
tpb [s]
0.00
0.25
0.50
0.75
1.00
1.25
1.50
Egain
kin,θ,φ [1049 erg]
SMR
2◦
160 km
Figure 1.
Post-bounce evolution of the 3D models computed with full neutrino transport, s9.0 (left) and s20 (right), for
diﬀerent angular grid resolutions. Top: Angle-averaged shock radius, ⟨Rsh⟩. The gray dashed line in the zoom inset of the right
panel indicates the location of the outer SMR reﬁnement interface. Bottom: Nonradial kinetic energy in the gain layer, Egain
kin,θ,φ.
3. MODELS WITH NEUTRINO TRANSPORT
In Fig. 1, we show the angle-averaged shock radii as
functions of post-bounce time for the two progenitors
evolved with full neutrino transport. In the s9.0 case,
the temporal evolution of the shock remains nearly un-
aﬀected by a change of the angular resolution from a
uniform 3.5◦grid to the SMR setup.
Only between
∼100 ms and ∼250 ms after bounce, the shock in the
SMR case has a slightly larger radius.
However, the
time of shock revival and also the shock expansion ve-
locity are nearly identical in both setups. The reason for
this is the robustness of the explosion in the s9.0 model.
It is well beyond the critical explosion threshold, because
the mass-accretion rate in this low-mass progenitor de-
creases rapidly at the silicon/silicon+oxygen interface
leading to a signiﬁcant drop in the ram pressure at the
shock.
In the s20 model, the simulation with a uniform grid
behaves entirely diﬀerently from the SMR case.
The
former explodes, while the latter does not experience
shock revival until we stopped the simulation at 400 ms
after core bounce. Between 200 and 300 ms, the SMR
model seems to have more favorable explosion conditions
because of a larger shock radius.
Also the nonradial
kinetic energy in the gain layer, deﬁned by
Egain
kin,θ,φ ≡
Z
Rgain<r<Rsh(θ,φ)
dV 1
2ρ
 v2
θ + v2
φ

(5)
and shown in the lower row of Fig. 1, is much higher
during this time interval, because of a strong SASI spi-
ral mode being present in the SMR model. Rgain is the
angle-averaged gain radius. At about 350 ms, however,
this picture changes and the simulation with a ﬁxed res-
olution of 2◦explodes, whereas the kinetic energy in the
gain layer decreases continuously in the SMR case.
In contrast, the s9.0 simulations do not diﬀer much in
their lateral kinetic energies in the gain layer at the time
when the explosions set it. Although the SMR model
develops higher values transiently, convective overturn
becomes similar in both simulations after 250 ms.
In order to understand why the SMR setup with its
angular resolution of 1◦in the gain layer and even 0.5◦
above 160 km prevents shock revival in the s20 model
despite the higher nonradial kinetic energy over a pe-
riod of 200 ms, we investigate the dissipation of kinetic
energy at the interfaces between resolution layers. We
speculate that this eﬀect might be crucial especially in
regions close to the gain radius, where neutrino heat-
ing is strongest and its interplay with the turbulent ﬂow
dynamics most pronounced.


## Page 6


6
T. Melson, D. Kresse, & H.-T. Janka
−4
−2
0
2
4
∆
 ˙Ekin
vr<0
˙Mvr<0
!
[1017 erg g−1]
SMR
2◦
0.0
0.1
0.2
0.3
0.4
tpb [s]
−4
−2
0
2
4
∆
 ˙Ekin
vr>0
˙Mvr>0
!
[1017 erg g−1]
Figure 2. Diﬀerence of the radial kinetic energy ﬂux divided
by the radial mass ﬂux as a function of post-bounce time, tpb,
for the s20 models computed with full neutrino transport.
The values at a radius 1 km below the inner SMR resolution
interface are subtracted from the values at a radius 1 km
above it, thus probing the ﬂux conservation at this interface,
which is moved inward from initially 105 km to 64 km during
the simulation. At this radius, the angular resolution increas-
es outward from 2◦to 1◦in the SMR run. Note that both
the minuend and the subtrahend are always positive. The
plotted values are time-averaged with a window of 10 ms. We
diﬀerentiate between inﬂows (top) and outﬂows (bottom).
In Fig. 2, we thus show diﬀerences of the radial ﬂuxes
of kinetic energy across the inner SMR interface (which
is located at the bottom of the gain layer) for inﬂowing
and outﬂowing material for the s20 models. The kinetic
energy ﬂuxes are computed according to
˙Ekin
vr<0 ≡r2
Z
dΩΘ(−vr) 1
2ρ
 v2
r + v2
θ + v2
φ

vr,
(6)
˙Ekin
vr>0 ≡r2
Z
dΩΘ(vr) 1
2ρ
 v2
r + v2
θ + v2
φ

vr,
(7)
and the mass ﬂuxes are given by
˙Mvr<0 ≡r2
Z
dΩΘ(−vr) ρvr,
(8)
˙Mvr>0 ≡r2
Z
dΩΘ(vr) ρvr,
(9)
where Θ(x) is the Heaviside step function. Both quanti-
ties are evaluated as integrals over inﬂows (vr < 0) and
outﬂows (vr > 0) separately. The diﬀerences are calcu-
lated by subtracting the speciﬁc kinetic energy ﬂuxes at
a radius 1 km below the inner SMR resolution interface,
r1, from their values at a radius 1 km above it, r2. For
0.0
0.1
0.2
0.3
0.4
tpb [s]
0.0
0.5
1.0
1.5
2.0
2.5
3.0
˙M [M⊙s−1]
Figure 3. Mass-accretion rate,
˙M, of the s20 progenitor as
a function of post-bounce time, tpb, measured at a radius of
400 km.
outﬂows, for example, we get
∆
 ˙Ekin
vr>0
˙Mvr>0
!
=
˙Ekin
vr>0(r2)
˙Mvr>0(r2)
−
˙Ekin
vr>0(r1)
˙Mvr>0(r1)
.
(10)
This allows us to investigate the ﬂux conservation at this
resolution interface, which is moved inward during the
simulation from initially 105 km down to 64 km, roughly
following the contraction of the gain radius. The indi-
vidual terms in Eq. (10) are always positive at both radii
so that a positive diﬀerence represents a higher ﬂux at
the outer radius for both ﬂow directions.
On the SMR grid, matter ﬂowing inwards is passing
from the region with an angular resolution of 1◦to the
layer with a grid spacing of 2◦at the inner SMR inter-
face. We wonder whether dissipation of kinetic energy
occurs as a consequence of the averaging over neigh-
boring grid cells when the grid resolution decreases (see
Appendix A). Especially, investigating this eﬀect at the
arrival time of the silicon/silicon+oxygen interface is im-
portant, because this is the crucial phase for shock re-
vival. At that time, the preshock mass-accretion rate
deﬁned (at 400 km) by
˙M ≡−r2
Z
dΩρvr
(11)
and thus also the ram pressure at the shock drops sig-
niﬁcantly, which happens at about 230 ms in the s20
progenitor (cf. Fig. 3). Until about that time, the en-
ergy diﬀerences are very similar in both models (Fig. 2,
upper panel). But shortly after that, at about 240 ms,
the diﬀerence in the speciﬁc kinetic energy ﬂuxes as dis-
played in the top panel of Fig. 2 starts to rise steeply in
the SMR simulation. In contrast, it remains even below
zero in the model with uniform 2◦resolution, meaning
that the absolute value of the inward ﬂux of kinetic en-
ergy per unit of mass at the inner radius, r1, is higher
than at the outer radius, r2. The negative value points
to a gravitational acceleration of the inward ﬂow.
In
the SMR model, the steep rise of the energy diﬀerence


## Page 7


Resolution Study with Prometheus-Vertex
7
to positive values implies that kinetic energy is dissi-
pated in this case at the resolution interface, which is
crossed by matter ﬂow into the coarser-resolved region.
Such a dissipation of kinetic energy does not happen in
the non-SMR case.
In the bottom panel of Fig. 2, we present the same
analysis for outﬂowing material.
Because matter is
propagating into the ﬁner-resolved layer in the SMR
model, we do not expect kinetic energy to be dissipated
into thermal energy. Indeed, the diﬀerence of the spe-
ciﬁc kinetic energy ﬂuxes around the resolution interface
remains close to zero for outﬂowing material, both in the
SMR and in the 2◦simulation.
Analogously, dissipation of kinetic energy (of down-
ﬂows) should also occur at the outer resolution interface
of the SMR model, which is located at a ﬁxed radius of
160 km. However, performing the same analysis at this
position is complicated by the presence of the deformed
shock over an extended period of time.1 The shock de-
celerates the radially infalling pre-shock material and
thus accounts for most of the reduction in ˙Ekin
vr<0/ ˙Mvr<0
during this phase, covering the dissipation eﬀect of the
grid geometry.2 Nevertheless, it is suspicious that the
average shock radius in the SMR run stagnates just af-
ter the shock has passed the interface at 160 km (see
zoom inset in Fig. 1). This possibly points towards the
dissipation eﬀect associated with the SMR grid.
The question remains, why the dissipation of kinetic
energy in the SMR simulation of the s20 model ham-
pers shock revival. Radice et al. (2015) discussed the
eﬀects of thermal and turbulent pressure contributions
in comparison. With the energy density e and the adi-
abatic index γ, the pressure is given by p = (γ −1)e.
For the thermal pressure in the radiation (e± pairs and
photons) dominated postshock layer, γ ≈4/3, whereas
for anisotropic turbulence as characteristic for the post-
shock layer, one has γ = 2.
When turbulent kinetic
energy is dissipated into thermal energy, the pressure
contribution therefore decreases per unit of energy den-
sity. For this reason, energy dissipation at SMR resolu-
tion interfaces reduces the pressure support behind the
shock and possibly prohibits shock revival.
1 In the SMR run, the maximum shock radius crosses the outer
resolution interface at around 230 ms, while the minimum shock
radius never reaches 160 km. In the simulation with uniform 2◦
resolution, the deformed shock is passing the radius of 160 km
between 240 ms and 380 ms after bounce.
2 On the contrary, no dissipation of kinetic energy is expected at
the outer resolution interface as long as the shock did not yet reach
it. In regions where pre-shock matter is still radially infalling, the
ﬂow geometry is spherically symmetric to ﬁrst order, and therefore
a change in the angular resolution should not matter.
4. MODELS WITH SIMPLIFIED
HEATING-COOLING SCHEME
As described in the previous section, the usage of the
SMR grid impeded the revival of the shock in the s20
model, although the angular grid resolution was eﬀec-
tively enhanced with this setup. It is therefore crucial
to disentangle the inﬂuence of a higher uniform grid
resolution from the possible detrimental eﬀects of the
SMR procedure. We thus performed simulations of the
s20 progenitor with a simpliﬁed heating-cooling (HTCL)
scheme replacing the computing-intense neutrino trans-
port.
In Fig. 4, we present the angle-averaged shock radii of
the entire model set. We selected two diﬀerent choices
for the HTCL parameter Lν,52, 3.96 and 4.0, to control
the tendency to get an explosion, namely the strength
of neutrino heating to overcome the ram pressure of in-
falling material.
In almost all simulations of this set, shock revival oc-
curs at the arrival time of the silicon/silicon+oxygen
interface (cf. Fig. 3). Only the simulations with a very
coarse angular resolution of 4◦and the 1D models do
not explode. The latter show the well-known oscillating
behavior of the shock radius during the shock stagnation
phase. It needs to be pointed out that the simple cooling
prescription reduces lepton-number and energy losses by
the proto-neutron star and thus weakens its contraction.
This, in turn, allows for a larger shock-stagnation radius
than in our full-ﬂedged supernova simulations and dis-
favors SASI activity, in particular in 3D.
The shock expansion velocity at tpb ≳230 ms is ba-
sically a monotonic function of the angular resolution.
Higher angular resolution accelerates the propagation of
the shock after its revival. This is true both in 2D and
3D, although the angle-averaged shock in 2D propagates
in a more oscillatory manner. Note that the presence of
the symmetry axis in the 2D models collimates the ﬂow
along this axis and enhances the tendency for shock-
sloshing motions (see, e.g., Glas et al. 2019). The axial
symmetry fosters shock expansion predominantly along
the axis, leading to a prolate shape of the shock surface,
and because of the importance of shock-sloshing mo-
tions it leads to large statistical variations of the angle-
averaged shock radius in 2D.
Both simulation sets with Lν,52 = 4 and Lν,52 = 3.96
show the same behavior and resolution dependence. Ex-
plosions in the latter runs are weaker with a lower shock
expansion velocity. In the following discussion, we will
focus on the Lν,52 = 4 model set, because we were able
to perform a simulation with a uniform resolution of 0.5◦
for this choice of the heating parameter, which was not
possible for Lν,52 = 3.96 due to computing time limita-
tions.


## Page 8


8
T. Melson, D. Kresse, & H.-T. Janka
0
100
200
300
400
500
600
⟨Rsh⟩[km]
HTCL 4.0
3D
4◦
2◦
2◦
1◦
0.5◦
SMR
0
100
200
300
400
500
600
⟨Rsh⟩[km]
HTCL 4.0
1D & 2D
4◦
2◦
1◦
0.5◦
1D
0.0
0.1
0.2
0.3
0.4
tpb [s]
0
100
200
300
400
500
600
⟨Rsh⟩[km]
HTCL 3.96
3D
4◦
2◦
1◦
SMR
0.0
0.1
0.2
0.3
0.4
tpb [s]
0
100
200
300
400
500
600
⟨Rsh⟩[km]
HTCL 3.96
1D & 2D
4◦
2◦
1◦
0.5◦
1D
Figure 4. Angle-averaged shock radii of the HTCL models as a function of time with parameter choices Lν,52 = 4 (top) and
Lν,52 = 3.96 (bottom) in 3D (left), as well as 1D and 2D (right). The 3D model with Lν,52 = 4 and an angular resolution of 2◦
was repeated twice with diﬀerent initial random perturbation patterns. The model sequences for Lν,52 = 3.96 exhibit a stronger
sensitivity and wider spread in dependence on the angular resolution (in particular for the 2◦cases), because the runs are closer
to the explosion threshold.
In the 3D models with 1◦and 0.5◦resolution of the
Lν,52 = 4 model set, the shock trajectories behave very
similarly until 370 ms.
The diﬀerence between these
two cases is much smaller than relative deviations be-
tween any other simulations.
We recommend not to
overinterpret the diﬀerence of the shock trajectories in
Fig. 4 between the 1◦and 0.5◦simulations after 370 ms.
This diﬀerence may be a transient feature connected to
the faster rise of a buoyant bubble, which would be a
stochastic phenomenon that can change from model to
model. To clarify this issue, however, the simulations
would have to be continued to later times. For these
two cases, we are therefore tempted to conclude that the
overall dynamics in 3D converge at about 1◦angular res-
olution, in particular because most of the kinetic energy
is contained in the turbulent ﬂow on the largest scales.
However, a ﬁnal conﬁrmation of convergence would re-
quire simulations with increased radial resolution and
signiﬁcantly better angular resolution than 0.5◦.
The 3D SMR simulations follow their corresponding
highest-resolved uniformly gridded counterparts for a
long time. Only after about 300 ms for Lν,52 = 4 and
350 ms for Lν,52 = 3.96, the shock velocity decreases.
The reason for this behavior is the dissipation of kinetic
energy at resolution interfaces, similarly to our ﬁndings
for the model set with full neutrino transport discussed
above. We will analyze this eﬀect in more detail later.
To prove that our analysis does not suﬀer from
stochastical variations in 3D, we repeated the 2◦model
in the Lν,52 = 4 set with a diﬀerent random cell-to-cell
perturbation pattern. Until more than 350 ms, the shock
trajectories of the two 2◦simulations remain nearly iden-
tical.
Only in the very last phase, they start to dif-
fer slightly.
The resolution trend we see in our mod-
els is therefore unlikely to be simply a manifestation of
stochastical diﬀerences.
In Fig. 5, we show cross-sectional slices through the
3D models with Lν,52 = 4 at 300 ms, 350 ms, and 400 ms
after bounce. All models are dominated by convection
and do not develop visible SASI activity, because the
shock does not retreat far enough during its stagnation
phase to provide suitable conditions for SASI growth.
The color-coded entropy clearly shows that the vortex
structures become ﬁner with increasing angular resolu-
tion, and downﬂows develop smaller-structured Kelvin-
Helmholtz ﬂow patterns.
Especially a comparison of
the 0.5◦model with the SMR case does not reveal any
noticeable diﬀerence. The SMR grid setup seems to pro-


## Page 9


Resolution Study with Prometheus-Vertex
9
−400
−200
0
200
400
y [km]
4◦
300 ms
350 ms
400 ms
−400
−200
0
200
400
y [km]
2◦
−400
−200
0
200
400
y [km]
1◦
−400
−200
0
200
400
y [km]
0.5◦
−400−200
0
200 400
x [km]
−400
−200
0
200
400
y [km]
SMR
−400−200
0
200 400
x [km]
−400−200
0
200 400
x [km]
5
10
15
20
s [kB/by]
5
10
15
20
s [kB/by]
5
10
15
20
s [kB/by]
5
10
15
20
s [kB/by]
5
10
15
20
s [kB/by]
Figure 5. Cross-sectional cuts through the 3D HTCL models of the Lν,52 = 4 model set at 300 ms, 350 ms, and 400 ms after
bounce with the color-coded entropy per baryon, s.


## Page 10


10
T. Melson, D. Kresse, & H.-T. Janka
−400
−200
0
200
400
y [km]
4◦
300 ms
350 ms
400 ms
−400
−200
0
200
400
y [km]
2◦
−400
−200
0
200
400
y [km]
1◦
−400
−200
0
200
400
y [km]
0.5◦
−400−200
0
200 400
x [km]
−400
−200
0
200
400
y [km]
SMR
−400−200
0
200 400
x [km]
−400−200
0
200 400
x [km]
0
1
2
3
4
log10
 |∇× v| [s−1]

0
1
2
3
4
log10
 |∇× v| [s−1]

0
1
2
3
4
log10
 |∇× v| [s−1]

0
1
2
3
4
log10
 |∇× v| [s−1]

−1
0
1
2
3
4
log10
 |∇× v| [s−1]

Figure 6. Same as Fig. 5, but with the color-coded vorticity, |∇× v|.


## Page 11


Resolution Study with Prometheus-Vertex
11
vide enough resolution where necessary to allow for the
small structures to develop.
In all simulations, we observe clearly separated high-
entropy plumes.
This is in contrast to the work by
Radice et al. (2016), who argued that high-entropy bub-
bles are embedded in a low-entropy surrounding medium
only if the resolution is too low, and that these bubbles
should instead form diﬀuse “clouds”. In our models, we
also see that the laminar layer behind the shock surface
is similarly structured in all cases and its thickness does
not depend on the angular resolution.
The vorticity, |∇× v|, shown in Fig. 6 depicts tur-
bulence in the gain layer, with typical values of ∼
102 −104 s−1 (red colors). With increasing angular res-
olution, the volume ﬁlled with small-scale turbulent ed-
dies grows.
The magnitude of the vorticity, however,
does not depend strongly on the resolution.
Again,
a clear diﬀerence between the highest-resolved uniform
grid of 0.5◦and the SMR setup cannot be spotted. The
radially infalling material ahead of the shock has signiﬁ-
cantly smaller values of the vorticity compared to the
neutrino-heated postshock matter (grey colors).
The
ﬁlament-like structures in this region are a consequence
of the random density perturbations of 0.1 % amplitude,
which are imposed in the whole computational volume
at 15 ms after bounce to break the spherical symmetry
of the progenitor model.
At around 150 ms, the higher-resolved 3D models ex-
perience a phase of slight shock expansion by about
15 km on average.
This is due to convection in the
neutrino-heating layer, which gains strength at this
time.
The nonradial kinetic energy in the gain layer
plotted in Fig. 7 shows that postshock convection starts
early at ∼120 ms in the models with an angular reso-
lution of at least 1◦. In lower-resolved cases, this oc-
curs about 100 ms later.
The onset of turbulent con-
vection depends on the angular resolution, because low
resolution corresponds to a higher numerical viscosity
that dampens the rise of buoyant bubbles. In this con-
text, the SMR models behave similarly to the cases with
1◦angular resolution, because this is precisely the res-
olution of the gain layer during the shock stagnation
phase in the SMR setup. Note that our simulations do
not develop strong SASI activity, because the shock ra-
dius does not retreat, disfavoring SASI growth. This is
another reason why the lower-resolution models do not
develop postshock turbulence before the shock expands
after the passage of the silicon/silicon+oxygen interface.
After shock revival, there remains a less pronounced
dependence of the lateral kinetic energy on the angular
resolution, except for the lowest-resolved models of 4◦,
which falls clearly behind the others. This relative in-
sensitivity to the resolution is compatible with the fact
that most of the kinetic energy is contained by vortex
0.0
0.5
1.0
1.5
Egain
kin,θ,φ [1049 erg]
HTCL 4.0
4◦
2◦
1◦
0.5◦
SMR
0.0
0.1
0.2
0.3
0.4
tpb [s]
0.0
0.5
1.0
1.5
Egain
kin,θ,φ [1049 erg]
HTCL 3.96
4◦
2◦
1◦
SMR
Figure 7.
Nonradial kinetic energy in the gain layer as a
function of time for the two HTCL model sets with Lν,52 = 4
(top) and Lν,52 = 3.96 (bottom).
0.00
0.05
0.10
0.15
0.20
ηconv,θ,φ
HTCL 4.0
4◦
2◦
1◦
0.5◦
SMR
0.0
0.1
0.2
0.3
0.4
tpb [s]
0.00
0.05
0.10
0.15
0.20
ηconv,θ,φ
HTCL 3.96
4◦
2◦
1◦
SMR
Figure 8. Eﬃciency factor for the conversion of heating into
(nonradial) turbulent kinetic energy as a function of time for
the two HTCL model sets with Lν,52 = 4 (top) and Lν,52 =
3.96 (bottom).
ﬂows on the largest scales.


## Page 12


12
T. Melson, D. Kresse, & H.-T. Janka
0
200
400
600
r [km]
4◦
2◦
0.0
0.1
0.2
0.3
0.4
tpb [s]
0
200
400
600
r [km]
1◦
0.0
0.1
0.2
0.3
0.4
tpb [s]
0.5◦
0.0
0.1
0.2
0.3
0.4
tpb [s]
SMR
0
1
2
3
4
5
6
7
8
Dq
v2
θ + v2
φ
E
[108 cm s−1]
Figure 9.
Minimum and maximum shock radii as functions of post-bounce time (green lines) for the HTCL models with
Lν,52 = 4. Color-coded is the density-weighted angle-average of the lateral velocity,

(v2
θ + v2
φ)0.5
. The zoom inset attached to
the lower right panel shows the positions of the two SMR resolution interfaces (123 and 162 km, black arrows), where nonradial
kinetic energy of downﬂows is converted to thermal energy. The loss of nonradial kinetic energy is visible as faint discontinuities
in the color shading at the radial locations of the two black arrows.
As in M¨uller et al. (2017), we analyze the eﬃciency
for the conversion of neutrino energy deposited in the
gain layer into turbulent kinetic energy,
ηconv,θ,φ =
Egain
kin,θ,φ
h
˙Qgain (⟨Rsh⟩−Rgain)
i2/3
M 1/3
gain
,
(12)
where Rgain and Mgain are the average gain radius and
the gain-layer mass, respectively. The net heating term
is given by
˙Qgain ≡
Z
Rgain<r<Rsh(θ,φ)
dV ρ ( ˙qheat −˙qcool) .
(13)
The values of ηconv,θ,φ are shown in Fig. 8. Before the ar-
rival of the silicon/silicon+oxygen interface, we see the
same dependence on the resolution as in Fig. 7. The
models with a resolution of at least 1◦reach an eﬃ-
ciency of about 0.15, while the lower-resolved cases re-
main convectively less vigorous. After the onset of shock
runaway, the conversion eﬃciency ηconv,θ,φ loses its de-
pendency on the angular resolution if the grid spacing
is at least 2◦.
The time evolution of the lateral velocities is presented
in Fig. 9 as a radius-time diagram. It can be clearly
seen that the onset of convection in the gain layer oc-
curs earlier with higher angular resolution, which we
have discussed already before. The slight shock expan-
sion at 150 ms after bounce in the models with at least
1◦resolution can be explained by the growing strength
of convection at that time. Models that remain convec-
tively quiet do not show this eﬀect. After the revival of
the shock, the convective strength, i.e., the magnitude
of the lateral velocity is roughly equal in all models pre-
sented in Fig. 9. This is in line with the ﬁnding that the
nonradial kinetic energy does not depend on the angular
resolution after the arrival of the silicon/silicon+oxygen
interface except for still lower values in the 4◦model.
We have shown above that the SMR setup resembles
a uniform grid with a resolution of 0.5◦in the over-
all ﬂuid structures. Also the temporal evolution of the
angle-averaged shock is identical until at least 70 ms af-
ter shock revival. Afterwards, however, the expansion
velocity of the shock decreases and falls below the case
of 1◦resolution.
This can again be explained by the
dissipation of kinetic energy at the interfaces between
layers of diﬀerent angular resolution (see black arrows
in the zoom inset of Fig. 9).
In Fig. 10, the radial speciﬁc kinetic energy ﬂuxes are
evaluated at two diﬀerent radii. The value at 122 km is
subtracted from the value at 124 km, to investigate the
ﬂux conservation at the SMR interface at 123 km. This
analysis is performed in the same way as for the model
set with full neutrino transport above, but now with
r1 = 122 km and r2 = 124 km in Eq. (10). Note that the
individual values are always positive for infalling and
outﬂowing ﬂuid elements so that a larger ﬂux at the
outer radius results in a positive ﬂux diﬀerence.
Again, we see that the outﬂowing ﬂuxes do not show
any evidence for dissipation of kinetic energy. This is as-


## Page 13


Resolution Study with Prometheus-Vertex
13
−10
−5
0
5
10
∆
 ˙Ekin
vr<0
˙Mvr<0
!
[1016 erg g−1]
4◦
2◦
1◦
0.5◦
SMR
0.0
0.1
0.2
0.3
0.4
tpb [s]
−10
−5
0
5
10
∆
 ˙Ekin
vr>0
˙Mvr>0
!
[1016 erg g−1]
Figure 10.
Same as Fig. 2, but for the HTCL model set
with Lν,52 = 4. The diﬀerence of the radial speciﬁc kinetic
energy ﬂux is evaluated around a radius of 123 km, i.e., the
speciﬁc energy ﬂux at 122 km is subtracted from its value at
124 km. We diﬀerentiate between inﬂows (top) and outﬂows
(bottom).
suring especially for the SMR model, where matter ﬂow-
ing outwards is propagating from a coarser grid spacing
of 2◦into a ﬁner grid of 1◦resolution. Infalling material,
however, behaves diﬀerently in this comparison.
The
ﬂux diﬀerences in the models with a uniform grid spac-
ing are rather similar and stay close to zero, whereas in
the SMR simulation they are distinctly higher by factors
of a few during times of increased nonradial velocities in
the gain layer. Kinetic energy is therefore dissipated on
the SMR grid with its resolution interface at 123 km as
matter ﬂows from 124 km to 122 km.
This eﬀect can
also be spotted in the bottom right panel of Fig. 9,
where the boundaries of the diﬀerent resolution layers
of the SMR grid display as faint horizontal discontinu-
ities in the color shading (see associated zoom inset).
The magnitude of the lateral velocity decreases visibly
at 162 and 123 km from outside inwards, which would
not be the case without kinetic energy dissipation.
When kinetic energy is dissipated into thermal energy
in the SMR model, the temperature should increase di-
rectly below a resolution interface.3
To analyze this,
3 Our hydro and SMR scheme are implemented in a conservative
form, which means that ﬂuxes conserve the sum of internal and
kinetic energies (see Appendix A).
110
120
130
140
150
160
170
r [km]
3.10
3.12
3.14
3.16
3.18
3.20
r ⟨T⟩[1017 K cm]
4◦
2◦
1◦
0.5◦
SMR
Figure 11.
Angle- and time-averaged temperature multi-
plied with radius for the HTCL simulations with Lν,52 = 4.
The time average was calculated in the interval from 300
to 400 ms. The angular resolution in the SMR model is 2◦,
1◦, and 0.5◦for r < 123 km, 123 km < r < 162 km, and
r > 162 km, respectively. The boundaries of these regions
are indicated by vertical dashed lines.
we show radial proﬁles of the angle- and time-averaged
temperature multiplied with the radius in Fig. 11. This
visualization roughly compensates for the r−1 scaling of
the temperature and allows us to closely analyze tem-
perature gradients.
The temperature proﬁle in the SMR case clearly dif-
fers from all other models. It is much steeper and shows
an even further increased gradient directly below the in-
ner resolution interface at a radius of 123 km. Between
the two resolution layers, i.e. between the two dashed
lines in Fig. 11, the SMR proﬁle does not ﬂatten, be-
cause the dissipation of kinetic energy does not happen
instantaneously as the ﬂow moves inwards. With a ra-
dial velocity of about −3 × 108 cm s−1, a ﬂuid element
needs only about 15 ms to propagate through the region
of 1◦angular resolution.
We have thus shown that the dissipation of kinetic
energy in downﬂows increases the thermal energy and
changes the average temperature proﬁle at the expense
of turbulent kinetic energy.
For the anisotropic post-
shock turbulence in the supernova core, kinetic energy
and turbulent pressure are coupled by an eﬀective adi-
abatic index of γturb = 2 (Radice et al. 2015). In con-
trast, thermal energy of the plasma in the postshock
layer, where relativistic electron-positron pairs and pho-
tons dominate the energy density, provides thermal pres-
sure only with a thermodynamical adiabatic index of
γthermal ≈4/3.
This suggests that the conversion of
turbulent kinetic energy to thermal energy reduces the
ability of the postshock layer to provide outward push to
the supernova shock. This explains why at later times,
tpb ≳300 ms, the expansion of the shock in the SMR
models begins to slightly lag behind the shock of the 1◦
and 0.5◦simulations (see Fig. 4).


## Page 14


14
T. Melson, D. Kresse, & H.-T. Janka
5. RESOLUTION DEPENDENCE OF
TURBULENCE
In this section, we will investigate how the angular grid
resolution inﬂuences the turbulent cascade, following the
discussion in Melson (2016).
5.1. Turbulent kinetic energy spectra
A ﬂuid transitions from the laminar to the turbu-
lent regime above a certain critical Reynolds number
Re. Turbulence is described phenomenologically and un-
derstood as a superposition of eddies on various scales
(Landau & Lifshitz 1987; Pope 2000). In the common
picture sharpened by Kolmogorov (1941), kinetic energy
is steadily injected at some large scale L, which is sim-
ilar to the size of the largest turbulent eddies. These
eddies break up into smaller structures and thus trans-
port energy to successively smaller scales. Eventually,
below some small scale L, kinetic energy is dissipated
into internal energy by viscous eﬀects.
Kolmogorov (1941) assumed that this turbulent en-
ergy cascade only depends on the energy dissipation
rate and the viscosity.
In the inertial range roughly
between L and L, kinetic energy is carried to smaller
scales without losses. From a self-similarity ansatz, it
follows that the kinetic energy spectrum E(k)—with
k being the wave number—has a universal shape of
E(k) ∝k−5/3 in the inertial range.4
These ﬁndings
only hold if the ﬂuid structures are locally isotropic,
i.e., large-scale anisotropies due to boundary eﬀects can
be neglected for suﬃciently small scales below L (Pope
2000). Moreover, ideal conditions require that the ﬂuid
is incompressible and the ﬂow is stationary. The last
two aspects are certainly not fulﬁlled in the supernova
environment. It is also not clear whether the ﬁrst as-
sumption is valid during the shock stagnation phase,
because the accretion ﬂow through the gain layer might
impose a preferred direction not only on the largest tur-
bulent eddies but also on smaller-scale structures (see,
e.g., Murphy et al. 2013; Couch & Ott 2015).
Here, we assume that Kolmogorov’s theory of turbu-
lence is applicable to the core-collapse supernova con-
ditions. In order to quantify the turbulent transport of
energy across various scales, the kinetic energy spectra
are calculated for the 3D HTCL models with Lν,52 = 4
at diﬀerent times after core bounce. Since we consider
stellar cores, which are spherical objects to ﬁrst order,
the kinetic energy is decomposed into spherical harmon-
ics instead of Cartesian wave numbers.
4 To clarify the notation, we write Ek and Eℓinstead of E(k)
and E(ℓ) from now on, because the symbol E is also used for the
total kinetic energy.
Let the complex spherical harmonics be deﬁned as
Y m
ℓ(θ, φ) = N m
ℓP m
ℓ(cos θ) eimφ
(14)
with normalization factors
N m
ℓ
=
s
2ℓ+ 1
4π
(ℓ−m)!
(ℓ+ m)!
(15)
and associated Legendre polynomials P m
ℓ(cos θ).
The
decomposition of the nonradial kinetic energy density
at a given radius is then determined by
Eℓ= 1
2
ℓ
X
m=−ℓ

Z
dΩ
r
ρ

v2
θ + v2
φ

Y m
ℓ(θ, φ)

2
.
(16)
This spectrum is normalized such that the total nonra-
dial kinetic energy density on a spherical shell is the sum
over all components of the spectrum,
E ≡1
2
Z
dΩρ
 v2
θ + v2
φ

=
∞
X
ℓ=0
Eℓ.
(17)
The decomposition applied here was similarly used in
other works that analyzed the turbulent cascade, for ex-
ample, Hanke et al. (2012), Couch & O’Connor (2014),
Hanke (2014), and Abdikamalov et al. (2015).
Note
that from a numerical perspective, accurate results of
the integrals in Eq. (16) can only be achieved by apply-
ing Gauss-Legendre quadrature, thus ensuring that the
spherical harmonics are sampled on a ﬁner grid than the
computational mesh of the simulation.
For the discussion later in this chapter, we also deﬁne
the spectrum of the speciﬁc kinetic energy as
Eℓ= 1
2
ℓ
X
m=−ℓ

Z
dΩ
q
v2
θ + v2
φ Y m
ℓ(θ, φ)

2
.
(18)
Again, the sum over the coeﬃcients gives the total non-
radial speciﬁc kinetic energy on a spherical shell,
1
2
Z
dΩ
 v2
θ + v2
φ

=
∞
X
ℓ=0
Eℓ.
(19)
In Fig. 12, we present energy spectra for the HTCL
simulations with Lν,52 = 4 at certain times after core
bounce. The spectra are measured at a radius R0 be-
tween the angle-averaged gain radius, Rgain, and the
minimum shock radius, i.e.,
R0 = 1
2 (Rgain + min(Rsh)) .
(20)
This choice assures that we do not include contributions
from pre-shock material in our analysis.
In order to
smooth the data, we computed volume-weighted spatial
averages of the energy spectra in the range R0 ± 5 km
with an additional time-averaging in the interval t ±
2.5 ms. To guarantee consistency, this procedure is also


## Page 15


Resolution Study with Prometheus-Vertex
15
10−6
10−5
10−4
10−3
10−2
10−1
Eℓ/E
160 ms
4◦
2◦
1◦
0.5◦
SMR
10−6
10−5
10−4
10−3
10−2
10−1
Eℓ/E
200 ms
10−6
10−5
10−4
10−3
10−2
10−1
Eℓ/E
250 ms
10−6
10−5
10−4
10−3
10−2
10−1
Eℓ/E
300 ms
100
101
102
ℓ
10−6
10−5
10−4
10−3
10−2
10−1
Eℓ/E
350 ms
100
101
102
ℓ
10−6
10−5
10−4
10−3
10−2
10−1
Eℓ/E
400 ms
Figure 12. Normalized spectra of the nonradial turbulent kinetic energy for the HTCL model set with Lν,52 = 4, measured
between the gain radius and the minimum shock radius. The spectra are averaged over 10 km around R0 and a time interval
of 5 ms. Open circles mark the beginning of the dissipation range, ℓdiss. The dotted lines indicate the (−5/3)-power-law slope
expected for Kolmogorov turbulence in the inertial range. At 300 ms the spectra of the simulations with SMR grid and 0.5◦
resolution become very similar, whereas at earlier times the spectra of SMR and 1◦simulations are more similar. This is fully
compatible with the growing resolution of the SMR grid as the shock moves to larger radii.
applied to the total kinetic energy density E used for
the normalization of the spectra.
From the angular grid resolution α of the 3D mod-
els, we can calculate the maximum multipole order ℓmax
roughly according to ℓmax ≈180◦/α. In the SMR simu-
lation, α = 1◦until ∼250 ms and α = 0.5◦at later times,
depending on the location of R0 at the time when the
spectrum is measured. However, due to round-oﬀerrors
caused by limited computational accuracy, we are not
able to compute spherical harmonics for ℓ> 150.
We can estimate the multipole order of the largest ed-
dies ℓL from simple considerations about their size. The
largest possible extension of turbulent vortex structures
in the gain layer depends on the thickness of this shell
and is
L = ⟨Rsh⟩−Rgain.
(21)
As explained, for example, by Foglizzo et al. (2006), this


## Page 16


16
T. Melson, D. Kresse, & H.-T. Janka
can be translated into a multipole order according to
ℓL = πR0
L .
(22)
In the HTCL model set with Lν,52 = 4, we ﬁnd ℓL ∼
7−10 during the phase of shock stagnation and ℓL ∼2−5
towards the end of the simulations, which roughly co-
incides with the peak positions, ℓpeak, of the kinetic
power spectra. The multipole order of the largest ed-
dies is nearly the same in all models, which is expected
on grounds of the geometrical considerations for deter-
mining ℓL.
An important aspect of Kolmogorov’s theory of tur-
bulence is the presence of a k−5/3 scaling in the inertial
range of the energy spectrum. As we will show below,
this translates into an ℓ−5/3 behavior in our decompo-
sition.
Hence, we added dotted lines of this slope in
Fig. 12 to visualize the inertial range. The power spec-
tra of our highest-resolved models are indeed close to a
(−5/3) power law for ℓ≳30, whereas for 10 ≲ℓ≲30
the spectra are better described by a (−1)-power-law
slope.
The value of ℓ, above which kinetic energy is dissi-
pated into internal energy, ℓdiss, depends strongly on
the grid resolution. It is visualized by a circle in Fig. 12
and also given in Table 2. In models with a resolution of
2◦or worse, we do not see any clear Kolmogorov regime.
In better resolved models, the ℓ−5/3 behavior breaks
down near ℓ∼100, i.e. on an angular scale of about
2◦, which means that dissipation sets in at the level of
a few grid cells. According to Porter et al. (1998) and
Sytine et al. (2000), the Piecewise Parabolic Method
(PPM; Colella & Woodward 1984) that is applied in
Vertex-Prometheus dissipates kinetic energy below
2 to 12 grid cells, which is roughly consistent with our
ﬁnding.
To sum up, the similarity of our numerical spectra
to Kolmogorov’s theory of steady-state isotropic turbu-
lence can be used as a motivation to (approximately)
apply relations from this theory during phases of shock
stagnation in our models. This seems justiﬁed in con-
ditions where SASI does not introduce global large-
amplitude variations by pumping kinetic energy into the
lowest modes ℓ≲2. In the high-resolution simulations
of at least 1◦, we see a clear separation between the in-
ertial range with its characteristic slope of −5/3 and the
dissipation range with a steeper decay.
5.2. Numerical viscosity and eﬀective Reynolds number
The kinematic shear viscosity of the stellar medium in
the gain layer is of the order of 0.1 cm2 s−1 and thus ex-
tremely low (e.g., Abdikamalov et al. 2015). Because the
corresponding Reynolds numbers are extremely high, of
order ∼1017, the evolution of the stellar plasma is de-
scribed by the Euler equations instead of solving the
Navier-Stokes equations, which include terms that ac-
count for viscous eﬀects.
However, the viscosity as-
sociated with the numerical scheme is many orders of
magnitude larger than the physical viscosity of the stel-
lar plasma (see., e.g., M¨uller 1998). Interestingly, the
interaction of neutrinos with matter in the gain layer
produces a damping force on ﬂuid motions—a neutrino
drag—whose inﬂuence on the plasma ﬂow is in the ball-
park of the eﬀects of numerical viscosity on the relevant
scales (see Appendix B for a derivation and discussion
of the neutrino drag in detail).
As in all other state-of-the-art core-collapse supernova
models, we rely on the implicit large eddy simulation
(ILES; Grinstein et al. 2007) paradigm. It assumes that
dissipative eﬀects on the smallest scales are implicitly ac-
counted for by the numerical viscosity. Instead of solving
ﬁltered hydrodynamic equations and creating a sub-grid
model for the dissipation of kinetic energy (Boris et al.
1992), the ILES approach assumes that such a sub-grid
model is implicitly included at the level of the grid cell
size.
Estimating the eﬀective viscosity of a numerical
scheme, νN, is diﬃcult. It depends not only on the algo-
rithm itself, but also on its implementation. Even if the
numerical viscosity is known for one simulation code, it
is not justiﬁed to assume an equal viscosity for all codes
that make use of the same algorithm for treating the
hydrodynamics. Consequently, the numerical viscosity
and the eﬀective Reynolds number must be determined
for every code separately in order to estimate the inﬂu-
ence of dissipative eﬀects. This can only be achieved
by measuring characteristic quantities from the output
data.
In the following two sections, we will discuss two meth-
ods for determining the numerical viscosity and the ef-
fective Reynolds number from properties of the kinetic
energy spectrum. Both approaches will be applied to
our 3D simulations. The ﬁrst procedure was proposed
by Abdikamalov et al. (2015), while the second method
has been developed by us and was presented in Melson
(2016) before. As in the previous section, the energy
spectra are averaged over 10 km and 5 ms, and measured
at a radius R0 halfway between the angle-averaged gain
radius and the minimum shock radius.
5.2.1. Based on the Taylor microscale
The method of Abdikamalov et al. (2015) is based
on determining the so-called Taylor microscale, which is
given by (Frisch 1995; Pope 2000)
λ =
r
5E
Z ,
(23)


## Page 17


Resolution Study with Prometheus-Vertex
17
where E is the total kinetic energy density of nonradial
ﬂuid motions,
E ≈
ℓmax
X
ℓ=0
Eℓ,
(24)
and Z is the enstrophy, which can be approximated by
Z ≈1
R2
0
ℓmax
X
ℓ=0
ℓ(ℓ+ 1) Eℓ.
(25)
For the upper bound ℓmax, Abdikamalov et al. (2015)
picked a value of 120, while we calculate it from the
angular resolution of the model.
The Taylor microscale λ has no direct physical inter-
pretation. It is situated somewhere between the char-
acteristic scale of the smallest eddies—the Kolmogorov
scale—and the size of the largest structures (Pope 2000).
Abdikamalov et al. (2015) derived a relation for the
eﬀective Reynolds number,
Re = 5
˜L2
λ2 ,
(26)
which is, however, not fully consistent with the litera-
ture. Commonly, a factor of 10 (Pope 2000; Schmidt
2014) or even 15 (Tennekes & Lumley 1972) instead of
5 is applied. Nevertheless, in order to compare with the
results of Abdikamalov et al. (2015), we also use their
factor 5 here. At the end of this section, we will further
discuss this issue.
The size of the energy-containing eddies ˜L is calcu-
lated by Abdikamalov et al. (2015) from the energy spec-
trum according to (motivated by Eq. (22))
˜L = πR0
 
1 + 1
E
ℓmax
X
ℓ=0
ℓEℓ
!−1
.
(27)
Finally, the kinematic numerical viscosity can be deter-
mined from the fundamental relation
νN = v0 ˜L
Re .
(28)
The characteristic velocity v0 of the largest eddies is
deduced from the total kinetic energy density (Eq. (17))
by
v2
0 ≡1
4π
Z
dΩ
 v2
θ + v2
φ

≈
E
2πρ0
.
(29)
Note that in addition to E, also the density ρ0 is aver-
aged over a radial shell deﬁned by R0 ±5 km and a time
interval of t ± 2.5 ms.
The method of Abdikamalov et al. (2015) suﬀers from
the uncertainty in Eq. (26) and in the scale deﬁned in
Eq. (27). Their application is debatable, because there
might be factors of 2 or even 3 missing. This issue will
be discussed later in this section. Furthermore, this ap-
proach yields Reynolds numbers being implausibly low
and showing only a weak resolution dependence (see Ta-
ble 2), which suggests a marginally turbulent ﬂow for
all resolutions tested, in obvious conﬂict with the situ-
ation observed in Figs. 5 and 6, and the presence of a
Kolmogorov-like power spectrum over roughly one order
of magnitude of ℓin Fig. 12.
For the reasons mentioned, we have developed a diﬀer-
ent procedure, which yields more realistic values of the
numerical viscosity and the eﬀective Reynolds number.
5.2.2. Based on the energy dissipation rate
Our method for measuring the numerical viscosity and
the Reynolds number is based on more fundamental
properties of the turbulent energy cascade. In the in-
ertial range, the kinetic energy spectrum only depends
on the speciﬁc energy dissipation rate ε and is given by
(Landau & Lifshitz 1987; Pope 2000)
Ek = C ε2/3 k−5/3,
(30)
where Ek dk is the speciﬁc turbulent kinetic energy of
the ﬂuid in the interval [k, k + dk].
In order to be consistent with the literature, we em-
ploy the spectrum of the speciﬁc kinetic energy as de-
ﬁned in Eq. (18) rather than that of the kinetic energy
density. The factor C is a universal constant of C = 1.62
and independent of the Reynolds number (Sreenivasan
1995; Yeung & Zhou 1997).
Since we decompose the spectrum by making use of
spherical harmonics, it must be written as a function
of the multipole order ℓinstead of the wave number k.
This transformation reads
k =
p
ℓ(ℓ+ 1)
R0
≈ℓ
R0
,
(31)
where the latter approximation is valid for suﬃciently
high values of ℓ. The energy spectrum as a function of
k,
Ek dk = C ε2/3 k−5/3 dk,
(32)
can then be written as
Eℓdℓ= C ε2/3 R5/3
0
ℓ−5/3 dℓ
R0
.
(33)
From this relation, we obtain an equation for the speciﬁc
energy dissipation rate,
ε(ℓ) =
s
E3
ℓℓ5
R2
0 C3 ,
(34)
which allows for directly measuring its value from the
spectrum, using Eq. (18) for Eℓand Eq. (20) for R0. To-
gether with the speciﬁc enstrophy Z calculated approx-
imately (becoming exact for ℓmax −→∞) according to
Z ≈1
R2
0
ℓmax
X
ℓ=0
ℓ(ℓ+ 1) Eℓ,
(35)


## Page 18


18
T. Melson, D. Kresse, & H.-T. Janka
we can determine the numerical viscosity from the equa-
tion (Tennekes & Lumley 1972; Pope 2000)
νN =
ε
2Z .
(36)
Note that the enstrophies deﬁned in Eqs. (25) and (35)
are connected to each other by the relation Z ≈ρ0Z.
The question arises, at which multipole order ℓthe
energy dissipation rate should be measured for our pur-
poses. If ideal Kolmogorov turbulence would apply, ε
would actually by constant in the inertial range. Be-
cause of deviations from this perfect Kolmogorov case,
the most conservative approach is taking the peak value
of ε to evaluate Eq. (36), since we want to maximize our
estimate of the numerical viscosity, which is known to
be large. In practice, however, the spectra ε(ℓ) turn out
to possess a very broad maximum, compatible with the
Kolmogorov-like behavior.
Ultimately, we can calculate the eﬀective Reynolds
number as
Re = v0L
νN
,
(37)
where L is taken from Eq. (21) and v0 is the characteris-
tic velocity of the largest eddies given by (see Eq. (19))
v2
0 = 1
2π
∞
X
ℓ=0
Eℓ≈1
2π
ℓmax
X
ℓ=0
Eℓ.
(38)
In contrast to the previous method, L is assumed to be
equal to the radial thickness of the gain layer (Eq. (21)).
The values of v0 obtained with Eqs. (38) and (29) are
extremely similar (see Table 2).
5.2.3. Comparison of the methods
We present the Reynolds numbers and numerical
viscosities calculated with the two methods described
above in Table 2. The procedure of Abdikamalov et al.
(2015) based on the Taylor microscale is denoted by
AOR+ and compared to our method (denoted by MKJ)
based on the energy dissipation rate.
The Reynolds numbers computed with the AOR+
method have only a very weak resolution dependence
and exhibit only marginal changes after 200 ms post
bounce in models with developed postshock turbulence.
Note that in Table 2, numbers for Re and νN are set
in parentheses when the corresponding models had not
yet developed such turbulent conditions in the postshock
layer.
While the grid spacing in our model with 0.5◦an-
gular resolution is a factor of eight ﬁner in each angu-
lar direction than in the 4◦case, the Reynolds number
for the AOR+ estimate increases only by a factor of
∼2 to values around 60. Such values of the Reynolds
numbers seem to be too low in view of the well devel-
oped Kolmogorov-like turbulent cascade witnessed over
roughly one order of magnitude of ℓin Fig. 12, and
they appear to be underestimated also in comparison
to other results discussed in the literature.
Based on
a systematic study of Porter & Woodward (1994), Keil
et al. (1996), for example, estimated values of Re ∼1000
for 2D simulations with 1.5◦resolution performed with
Prometheus.
With our method (MKJ), we obtain values for Re
that are more consistent with the observed ﬂow behav-
ior in the neutrino-heated postshock layer. During the
shock-stagnation phase (which lasts until ∼230 ms after
bounce), Reynolds numbers of up to ∼200 are reached
in the models with at least 1◦angular resolution.
From 200 ms to 225 ms, the Reynolds numbers remain
relatively constant for ﬁxed resolution in our analysis.
This indicates that the turbulent cascade is in steady-
state conditions during this period. We do not witness
any evidence that the scaling relations of classical turbu-
lence theory might not be applicable here. After 250 ms,
the shock expansion leads to an increasing value of L
and a corresponding increase of the Reynolds number,
in contrast to values obtained with the AOR+ approach.
With increasing angular resolution of the simulations,
we see also increasing Reynolds numbers because of de-
creasing values of the numerical viscosity, as expected
from the point of view that better resolution should
reduce viscous damping of the turbulent ﬂow by dis-
sipative eﬀects associated with the grid discretization.
Models that do not follow this trend have not yet fully
developed turbulence in the postshock layer, for which
reason the MKJ estimates become unreliable. The cor-
responding numerical results are set in parentheses in
Table 2. The numbers of Re and νN for the SMR mod-
els are close to those models with ﬁxed resolution that
match the resolution of the SMR models at the radius
of evaluation, R0.
The two approaches, AOR+ and MKJ, described
above yield Reynolds numbers and numerical viscosities
that diﬀer signiﬁcantly. In order to analyze why this is
the case, we divide Eqs. (26) and (28) by Eqs. (37) and
(36), respectively, i.e., we divide the values calculated
with the method of Abdikamalov et al. (2015, AOR+)
by the values obtained with our procedure (MKJ). The
ratio of the Reynolds numbers reads
RRe ≡ReAOR+
ReMKJ =
˜L2Z/E
2Zv0L/ε =
ε˜L2
4πv3
0L,
(39)
and the ratio of the numerical viscosities is given by
RνN ≡νAOR+
N
νMKJ
N
= v0E/˜LZ
ε/2Z
= 4πv3
0
ε˜L
,
(40)
where in addition to the mentioned equations we also
made use of Eqs. (23) and (29), and of Z ≈ρ0Z. Ideally,
both quantities —RRe and RνN— should be unity. How-


## Page 19


Resolution Study with Prometheus-Vertex
19
Table 2. Numerical Reynolds numbers and corresponding numerical viscosities evaluated using the AOR+ and MKJ methods
for the 3D simulations of the HTCL model set with Lν,52 = 4.
Abdikamalov et al. (2015, AOR+)
This work (MKJ)
tpb
3D model
Re
νN
˜L
v0
Re
νN
L
v0
ℓdiss
R0
[ms]
[1013 cm2 s−1]
[km]
[108 cm s−1]
[1013 cm2 s−1]
[km]
[108 cm s−1]
[km]
160
4◦. . . . . . . . .
(41)
(0.05)
134
0.02
(40)
(0.02)
46
0.02
-
141
2◦. . . . . . . . .
(50)
(0.03)
87
0.02
(60)
(0.01)
46
0.02
-
141
1◦. . . . . . . . .
47
8.4
99
3.9
87
2.6
56
4.0
83
140
0.5◦. . . . . . .
58
5.7
61
5.4
195
1.8
65
5.5
93
144
SMR (1◦) .
43
11.0
103
4.6
55
4.8
56
4.7
85
141
200
4◦. . . . . . . . .
(35)
(0.6)
137
0.2
(12)
(0.6)
45
0.2
-
139
2◦. . . . . . . . .
(46)
(0.6)
96
0.3
(21)
(0.6)
44
0.3
-
139
1◦. . . . . . . . .
54
6.8
68
5.3
153
2.2
61
5.4
86
141
0.5◦. . . . . . .
58
5.9
57
5.9
199
1.9
64
6.0
93
142
SMR (1◦) .
59
6.4
68
5.6
163
2.1
61
5.7
88
141
225
4◦. . . . . . . . .
(18)
(1.2)
97
0.2
(10)
(0.9)
41
0.2
-
134
2◦. . . . . . . . .
22
6.0
83
1.6
13
5.6
43
1.6
-
134
1◦. . . . . . . . .
54
6.1
67
4.9
132
2.1
57
5.0
81
137
0.5◦. . . . . . .
59
5.5
54
6.0
197
1.8
59
6.1
97
138
SMR (1◦) .
57
6.4
66
5.5
129
2.5
57
5.6
83
137
250
4◦. . . . . . . . .
(39)
(0.8)
159
0.2
(48)
(0.4)
92
0.2
-
161
2◦. . . . . . . . .
39
4.1
124
1.3
46
2.6
92
1.3
-
160
1◦. . . . . . . . .
54
6.8
77
4.7
230
2.2
106
4.8
85
163
0.5◦. . . . . . .
60
5.3
62
5.1
306
1.8
109
5.1
96
165
SMR (0.5◦)
61
6.0
73
5.0
279
2.0
108
5.0
86
163
300
4◦. . . . . . . . .
36
25.5
173
5.3
101
8.8
168
5.3
-
182
2◦. . . . . . . . .
47
19.6
137
6.6
183
7.3
198
6.7
-
197
1◦. . . . . . . . .
55
11.4
97
6.4
368
3.8
216
6.5
86
206
0.5◦. . . . . . .
59
9.3
83
6.7
443
3.3
219
6.7
96
204
SMR (0.5◦)
62
10.2
92
6.9
515
3.0
217
7.0
110
207
350
4◦. . . . . . . . .
34
33.6
184
6.2
97
13.2
206
6.2
-
198
2◦. . . . . . . . .
47
23.3
150
7.3
322
6.4
281
7.3
-
220
1◦. . . . . . . . .
56
15.9
121
7.3
413
5.6
312
7.4
84
238
0.5◦. . . . . . .
57
12.8
96
7.6
631
3.8
313
7.7
92
229
SMR (0.5◦)
63
13.3
109
7.7
535
4.3
293
7.8
88
231
400
4◦. . . . . . . . .
35
35.8
172
7.3
132
11.5
208
7.3
-
175
2◦. . . . . . . . .
45
27.6
168
7.3
286
9.5
362
7.5
-
240
1◦. . . . . . . . .
58
20.8
156
7.6
549
6.2
437
7.8
88
279
0.5◦. . . . . . .
59
14.5
111
7.7
682
4.6
400
7.9
86
250
SMR (0.5◦)
63
14.6
111
8.3
715
4.1
348
8.4
94
233
Note— Numerical Reynolds numbers, Re, corresponding numerical viscosities, νN, estimates of the energy-containing eddy
scales, ˜L and L, respectively, and characteristic velocities of the largest eddies, v0. We show the results of the two evaluation
methods under consideration, namely once based on the Taylor microscale (AOR+) and a second case based on the energy
dissipation rate (MKJ). Note that the two methods are meaningful only at times when postshock turbulence is fully developed.
When this is not the case, the values of Re and νN are set in parentheses. ℓdiss represents the spherical harmonics mode at
which clear deviations from a Kolmogorov-like energy spectrum become evident and the dissipation range of kinetic energy sets
in (see open circles in Fig. 12). R0 is the radius of evaluation as deﬁned in Eq. (20). In the SMR model, R0 lies in the layer
of 1◦angular resolution until ∼250 ms, and in the region with 0.5◦resolution at later times (see values in parentheses in the
second column).


## Page 20


20
T. Melson, D. Kresse, & H.-T. Janka
ever, the ratio RRe can be as small as 0.1, while RνN can
reach values of 3–4 (see Table 2). Since the estimates of
v0 from both methods are basically identical and ˜L and
L do not diﬀer by more than 2–3 in most cases (see Ta-
ble 2), we conclude that our MKJ appoach yields lower
estimates for the numerical energy-dissipation rate, ε.
In other words, the method of AOR+ intrinsically over-
estimates the numerical energy-dissipation rate.
In our approach, the energy-dissipation rate ε is di-
rectly measured from the energy spectrum according to
Eq. (34). The only term in Eq. (34) being not precisely
known is the constant C. However, it was determined
to satisfactory accuracy and even the largest possible re-
duction of C within the error bars mentioned by Sreeni-
vasan (1995) would enhance ε only by 18%.
For the
proposed best value of C, we have measured the peak
amplitude of ε(ℓ) to maximize the numerical viscosity.
Hence, we conclude that a signiﬁcant underestimation
of the energy dissipation rate is unlikely.
Another ambiguity concerns the length scales of the
relevant turbulent eddies. The values in Table 2 suggest
that ˜L according to Abdikamalov et al. (2015) is some-
times too large, especially in cases where ˜L is larger
than the gain-layer width. Our calculated values of L
are often more than a factor of two diﬀerent from ˜L
(smaller at early times and larger towards the end of
our simulations). These values of L represent the true
size of the largest eddies, which marks an upper limit
for the energy-containing eddy scale, i.e. for ˜L. Deter-
mining the relevant length scale from the spectral shape
as done by Abdikamalov et al. (2015) seems problem-
atic, because ˜L varies signiﬁcantly with grid resolution,
whereas on grounds of physics one would expect that the
size of the energy-containing eddies, corresponding to
the energy-weighted mean of the multipole order, should
hardly depend on the grid resolution. Since the energy-
injection scale is determined by the thickness of the layer
of main neutrino-energy deposition, this scale should be
very similar between all simulations within the HTCL
model set. Also the location of the peak of the power
spectrum is fairly similar in all models with fully devel-
oped turbulence, as can be seen in Fig. 12. Moreover,
solely the radial thickness of the gain layer constrains
the diameter of the largest turbulent structures, which
is exactly the motivation for our choice of L in Eq. (21).
For all these reasons, it does not seem plausible that
the relevant scale for estimating the Reynolds number,
as in the approach of Abdikamalov et al. (2015), ex-
hibits a strong variation with the angular resolution of
the model.
We therefore suspect that the misjudgment of the rel-
evant turbulent eddy scale in the AOR+ method might
be the underlying cause for the counterintuitively weak
variation of the Reynolds number with angular resolu-
tion and for the strange fact that Re is basically in-
dependent of the growing radial diameter of the post-
shock layer at later times (Table 2). Furthermore, note
that due to the quadratic dependence in Eq. (26), the
Reynolds number in the AOR+ approach is more sensi-
tive to the length scale than in our method.
Besides these considerations of over- and underesti-
mated eddy scales, the numerical constant used in the
calculations of the Reynolds numbers in the approach of
Abdikamalov et al. (2015) appears to be too low in gen-
eral. The factor 5 in Eq. (26) is disputable, because it is
smaller than what is reported in the literature. Tennekes
& Lumley (1972) formulated Eq. (26) in a diﬀerent way,
namely as
Re = 15
A
˜L2
λ2 ,
(41)
where A is an “undetermined constant” of order unity.
Pope (2000) and Schmidt (2014) used A = 3/2, where-
as Abdikamalov et al. (2015) and also Couch & Ott
(2015) applied A = 3. Obviously, there is some ambi-
guity with respect to the value of this constant. The
Reynolds numbers of Abdikamalov et al. (2015) are
therefore likely to be more than a factor of two too small.
This highlights an important aspect of turbulence the-
ory. Many equations are obtained from self-similarity
considerations and therefore based only on proportion-
alities.
Scaling factors are then derived from further
assumptions or they remain undetermined.
Our approach to calculate the numerical viscosity re-
lies on the fundamental relations of Kolmogorov’s the-
ory and avoids the usage of other equations. Although
our values computed for the Reynolds numbers might be
slightly overestimated due to their sensitive dependence
on v0 and L, the numerical viscosities deduced from the
measured turbulent power spectra with our formalism
are not subject to corresponding uncertainties and can
therefore be considered as solid measures, provided that
turbulence is fully developed and that Kolmogorov’s the-
ory is applicable.
6. DISCUSSION
The main result of our resolution study, namely that
higher angular resolution is beneﬁcial for stronger shock
expansion and shock revival in 3D simulations, is in
contradiction with results of a previous investigation by
Hanke et al. (2012), whose 3D models with higher an-
gular resolution showed the tendency to explode later
or not at all, in spite of the success of lower-resolution
cases.
Both generations of simulations diﬀer in several as-
pects (see Section 2.2), namely in the use of slightly dif-
ferent versions of the high-density equation of state of
Lattimer & Swesty (1991), minor modiﬁcations in the
neutrino-cooling description, general relativistic correc-


## Page 21


Resolution Study with Prometheus-Vertex
21
tions in the gravitational potential instead of the New-
tonian gravity used by Hanke et al. (2012), and the
replacement of the previously employed spherical po-
lar grid by the axis-free Yin-Yang grid. While the ﬁrst
three aspects have the eﬀect of changing the value of the
neutrino luminosity needed to trigger shock revival, they
cannot explain the opposite dependence of the explosion
behavior on resolution.
The crucial change was the introduction of the Yin-
Yang grid, which allows for numerically cleaner resolu-
tion tests due to less grid-associated eﬀects. The po-
lar axis of regular spherical coordinate grids does not
only possess a coordinate singularity that can induce
artifacts, but also the nonuniform cell sizes of the an-
gular grid with smaller azimuthal cells near the polar
axis (and thus lower numerical viscosity) may have per-
turbative eﬀects. In all 3D simulations with a standard
polar grid, we can observe postshock convection appear-
ing earlier near the polar axis and becoming ﬁrst visible
by a buoyant plume that expands along the axis and de-
forms the shock. This shock deformation creates vortic-
ity and entropy perturbations in the postshock ﬂow and
thus triggers the development of neutrino-driven con-
vection or SASI mass motions, depending on which of
these instabilities is favored to grow faster by the phys-
ical conditions. Therefore, in all of the 3D simulations
performed by Hanke et al. (2012), even in the runs with
the lowest angular resolution of 3◦, shock asphericity
and nonradial kinetic energy were found to rise already
at 80–130 ms after bounce. This is in sharp contrast to
our current set of models, where due to numerical vis-
cosity in the low-resolution (2◦and 4◦) cases, nonradial
kinetic energy in the gain layer does not appear on a
visible level before 200 ms after bounce (see Figs. 7, 8,
and 9).
For this reason, the shock expansion and revival in
the simulations by Hanke et al. (2012) were strongly
inﬂuenced by the presence of the polar grid axis and
the variable cell sizes of the angular grid, which had
the consequence of enhancing nonradial mass motions
in the postshock region. With higher resolution (in 3D
it could be improved only moderately to 2◦instead of
3◦) this inﬂuence seems to have lost strength, which is
why the better resolved models showed a reduced ten-
dency to produce explosions. In the models of the cur-
rent study the angular cells of the Yin-Yang grid are
basically uniform and a polar axis is absent. Therefore,
grid-induced irregularities occur on a much lower level
and do not determine the development of nonradial ﬂows
in the postshock layer. Consequently, our models with
higher angular resolution and correspondingly lower nu-
merical viscosity exhibit stronger turbulence, which sup-
ports shock expansion and fosters explosions.
From this discussion another consequence arises:
Comparisons of our results based on the Prometheus
code to resolution studies discussed in the literature re-
quire great caution and are by no means straightforward.
Code-speciﬁc aspects such as the order of the employed
hydro solver and diﬀerent grid setups used by diﬀerent
groups could play a role. It is, for example, conspicu-
ous that the result of Hanke et al. (2012) of low resolu-
tion yielding more favorable conditions for explosions in
3D, was reproduced by studies that employed Cartesian
grids with static or adaptive mesh reﬁnement (AMR)
(Couch & O’Connor 2014; Couch & Ott 2015; Roberts
et al. 2016) or with a combination of overlapping grid
blocks in a cubed-sphere multi-block AMR system (Ab-
dikamalov et al. 2015), or, as in the study by Radice
et al. (2016), with a spherical mesh but a computational
domain that was constrained to an octant with inner
and outer radial boundaries, using periodicity in the an-
gular directions and a reﬂecting boundary condition at
the inner boundary. While possible artiﬁcial eﬀects of
such a constrained simulation volume with polar coor-
dinates have not been explored yet (Roberts et al. 2016
and O’Connor & Couch 2018 also investigated cases
with octant symmetry but employed Cartesian AMR),
it is known that Cartesian grids impose perturbations
on radial ﬂows.
Even the boundaries between AMR
or grid domains with diﬀerent resolutions or geometry
could have problematic numerical consequences, similar
to what we observed at the resolution boundaries of our
SMR grid.
One might speculate that Cartesian grids
with higher resolution create a lower level of numerical
noise, thus leading to weaker driving of postshock turbu-
lence and therefore less beneﬁcial conditions for explo-
sions. This might be the reason why Cartesian setups
with lower resolution produced faster explosions, while
the authors of the corresponding papers attributed this
result to greater nonradial kinetic energy on the lowest-
order multipolar scales because of suppressed cascading
of turbulent energy to high-ℓscales.
While more extended speculations about the possible
impact of grid eﬀects do not appear very productive in
default of investigations of how diﬀerent codes with dif-
ferent grid setups perform on the same well-controlled
test problems, it is clear from all of what was said above
that Cartesian results cannot be contrasted with results
from polar grids by simply identifying the size of the
Cartesian cells with an eﬀective angular resolution of a
spherical grid (see, e.g., Couch 2013; Ott et al. 2013; Ab-
dikamalov et al. 2015; Couch & Ott 2015; O’Connor &
Couch 2018). Numerical artifacts associated with Carte-
sian grids and polar grids are too diﬀerent and may even
govern the solutions. Moreover, changes of the resolu-
tion in radial and angular directions can have diﬀerent
consequences (see Hanke et al. 2012), but in Cartesian
simulations they cannot be varied independently. Corre-


## Page 22


22
T. Melson, D. Kresse, & H.-T. Janka
spondingly, in 3D supernova simulations with Cartesian
grids the minimum cell size in the vicinity of the steep
density decline near the surface of the proto-neutron star
is typically around 500 m or even more (e.g., Couch 2013;
Couch & O’Connor 2014; Couch & Ott 2015; Dolence
et al. 2013; Ott et al. 2013; Kuroda et al. 2016; Roberts
et al. 2016; O’Connor & Couch 2018), similar to what
was employed in recent 3D calculations with the For-
nax code using spherical (dendritic) coordinates (Var-
tanyan et al. 2019; Burrows et al. 2019). In contrast,
in applications of the Prometheus code with simpli-
ﬁed neutrino treatment as well as the Prometheus-
Vertex code with elaborate and computationally ex-
pensive neutrino transport, the radial resolution in the
same region is chosen to be much ﬁner, and it is im-
proved with time as the density gradient gradually steep-
ens, to become as good as 50–100 m after 500 ms post
bounce. It is evident that more studies, including di-
rect comparisons of diﬀerent codes with diﬀerent grids,
applied on the same test problems, are needed to dis-
entangle numerical and physical eﬀects in the growing
suite of 3D supernova models.
7. SUMMARY AND CONCLUSIONS
7.1. Summary
In this paper, we investigated the resolution depen-
dence and convergence properties of 3D simulations with
the Prometheus-Vertex supernova code.
Because
of limited computational resources, previous neutrino-
hydrodynamics calculations with this code, in particular
also the successful 3D explosion models reported by Mel-
son et al. (2015a,b) and Summa et al. (2018), were con-
ducted with an angular cell size of 2◦for the employed
polar and Yin-Yang grids. However, in regions where
hydrodynamic instabilities and turbulent eﬀects play a
role, in particular in the convectively unstable neutrino-
heating layer behind the stalled supernova shock, more
angular resolution is desirable. Therefore we introduced
a new static mesh reﬁnement (SMR) procedure in our
code, which can compensate the decreasing resolution
(in terms of absolute scales) associated with the geomet-
rical widening of the lateral and azimuthal grid zones
with growing distance from the coordinate center. This
SMR grid allows us to increase the number of angu-
lar grid cells in deﬁned radial regions without equally
increasing the number of angular zones (also termed ra-
dial “rays”) for the ray-by-ray-plus neutrino transport.
In the neutrino-heating layer and farther outside, where
neutrinos are nearly decoupled from the stellar back-
ground (the optical depth of these layers is typically
below 0.2), the use of less transport rays than angular
zones in the hydrodynamics solver is a viable approxima-
tion. Such an approach saves considerable amounts of
computer time because the transport module accounts
for the dominant part of the required computational re-
sources.
The results presented here show, however, that the
SMR technique comes with some downsides. While in
the case of a robustly exploding 9 M⊙progenitor we did
not observe any signiﬁcant diﬀerences between simula-
tions with uniformly spaced low-resolution (3.5◦) grid
and a high-resolution SMR setup, a 20 M⊙model that
evolved along the borderline between explosion and fail-
ure showed undesirable sensitivity to the chosen grid
setup. It developed an explosion with uniform 2◦an-
gular resolution, whereas it did not succeed to blow
up when the SMR grid was used.
The SMR model
failed despite the fact that its average shock radius was
transiently larger (reaching up to 170–180 km) than in
the case with uniform angular grid, where it was only
∼150 km.
We took this ﬁnding as a motivation for a system-
atic study that was intended to clarify the underlying
numerical reasons and to disentangle the consequences
of higher angular grid resolution from eﬀects associated
with the SMR method. To achieve this goal with ac-
ceptable investment of computing time, we replaced the
Vertex neutrino-transport treatment by a simpliﬁed
heating and cooling (HTCL) scheme and set up 20 M⊙
simulations such that the supernova shock reached a
stagnation radius of about 170–180 km as it did tem-
porarily in the 20 M⊙SMR model with full-ﬂedged neu-
trino transport. All exploding models in this carefully
controlled study with SMR grid and uniform resolutions
of 4◦, 2◦, 1◦, and 0.5◦experienced shock revival (or tem-
porary shock expansion) at the same time. This fact en-
abled a particularly clean and conclusive investigation of
the inﬂuence of varied angular resolution on the shock
evolution.
As in the simulations with full neutrino transport,
we observed that higher resolution leads to a slightly
larger shock stagnation radius.
Moreover, better re-
solved simulations do not only display a considerably
earlier onset of postshock convection in the neutrino-
heating layer but also show more ﬁne structure in the
postshock ﬂow once turbulent convection has developed.
This corresponds to diﬀerences in the normalized tur-
bulent power spectra with relatively less kinetic energy
on large multipolar scales (ℓ≲10) and relatively more
power on small scales, roughly following a Kolmogorov-
like ℓ−5/3 power law from ℓ∼30 up to the dissipation
scale around ℓ∼100 in all cases where the resolution
is better than ∼1◦. Low resolution obviously delays the
growth of nonradial postshock instabilities, and the as-
sociated higher numerical viscosity prevents cascading
of kinetic energy from the largest scales to turbulent
vortex ﬂows on smaller scales. This goes hand in hand


## Page 23


Resolution Study with Prometheus-Vertex
23
with lower nonradial kinetic energy and a reduced ef-
ﬁciency for conversion of neutrino heating to turbulent
kinetic energy. During this phase the highest-resolved
0.5◦model still exhibits noticeable diﬀerences compared
to the SMR and 1◦simulations.
Shock expansion in reaction to the arrival of the in-
falling silicon/silicon+oxygen interface at the stagnant
shock ﬁnally enables the onset of postshock convection
in all of our HTCL models, also in the coarse-resolved
ones, because the decreased accretion velocity in the
postshock ﬂow allows buoyant plumes to rise outward.
In this phase, the shock develops runaway expansion in
all cases except the 4◦-degree runs. The expansion veloc-
ity of the shock clearly shows a monotonic dependence
on the resolution with possible convergence at about 1◦.
Simulations that are closer to the explosion threshold
are more sensitive to resolution changes. Models with
a resolution of at least 1◦develop similar ﬂuid struc-
tures. The SMR run resembles simulations with a uni-
form resolution of 0.5◦in this respect.
Only towards
the end of the SMR simulation, the expansion velocity
of the shock drops slightly below the value of the 1◦and
0.5◦models.
Our analysis revealed that this eﬀect is
caused by the dissipation of kinetic energy at the inter-
faces of layers with diﬀerent angular resolutions in the
SMR setup. Downﬂows propagating from the ﬁner grid
to the layer with coarser resolution under the constraint
of total energy conservation lose kinetic energy that is
transformed into internal energy. This leads to reduced
pressure support of the expanding shock because ther-
mal energy provides pressure with an adiabatic index of
4/3, whereas turbulent pressure connects to turbulent
kinetic energy with an equivalent adiabatic index of 2
(see Radice et al. 2015).
The bottom line is that the dynamical evolution of
our 20 M⊙HTCL models during the shock stagnation
and shock revival phases is basically identical in 3D sim-
ulations with 1◦, 0.5◦, and SMR grid, despite remain-
ing resolution-dependent diﬀerences in various measures
of turbulence (e.g., the initial growth of convective ac-
tivity, the saturation level of the nonradial kinetic en-
ergy during shock stagnation, and the detailed shape of
the normalized mode spectrum of the kinetic energy).
Even the 2◦run follows closely when the shock expan-
sion sets in, while the 4◦model exhibits a visibly weaker
shock expansion because higher numerical viscosity at-
tenuates turbulent mass motions and reduces the turbu-
lent kinetic energy. A similar eﬀect, though less extreme,
could also be witnessed at the interfaces of domains of
diﬀerent angular resolution in our SMR setup, where
kinetic energy of ﬂows crossing boundaries from higher
to lower resolution is converted to thermal energy. The
grid resolution has a more sensitive inﬂuence in cases
that marginally overcome the explosion threshold.
In order to quantify the inﬂuence of numerical viscos-
ity, we introduced a method of calculation that is based
on the energy dissipation rate measured directly from
the turbulent energy spectrum. Our method diﬀers from
the approach used by Abdikamalov et al. (2015), who de-
rived results based on the Taylor scale. We determined
eﬀective numerical Reynolds numbers for the postshock
ﬂow in our high-resolution (0.5◦, 1◦, and SMR) runs
of up to several hundred, and in our 2◦and 4◦models
of a few dozens to a few hundred. Such values agree
with previous rough estimates for simulations of proto-
neutron star convection with the Prometheus code
(Keil et al. 1996), and they are consistent with those
reported by Handy et al. (2014). Our numerical viscosi-
ties, however, are lower by a factor of ∼2–4 compared
to the results we obtained with the formalism of Ab-
dikamalov et al. (2015), and our numerical Reynolds
numbers are considerably higher (by up to a factor of
∼10) than those computed according to these authors.
We consider our estimates as better compatible with the
ﬁne-structured vortex pattern witnessed in the convec-
tive postshock ﬂow of our high-resolution models, which
is mirrored by a near-Kolmogorov spectrum of the tur-
bulent kinetic energy over an order of magnitude in the
spherical harmonics modes ℓ.
We also presented a detailed evaluation of neutrino-
drag terms in the hydrodynamics equations for the con-
ditions between neutrinosphere and supernova shock in
Appendix B. Interestingly, the numerical Reynolds num-
bers of postshock turbulence even in our lowest-resolved
simulations, which range between several 10 and some
100 on the relevant scales, are in the ballpark of the
damping eﬀects associated with neutrino drag acting on
the ﬂow in the gain layer. Concerns were expressed that
current full-scale supernova models are severely underre-
solved and that much higher grid resolution is needed to
describe the turbulent energy cascading in the convec-
tive postshock layer in order to reproduce the self-similar
power-law spectrum of Kolmogorov’s classical theory in
the inertial range despite numerical viscosity (Couch &
Ott 2015; Radice et al. 2016, 2018). Such reservations,
however, must be confronted with the presence of neu-
trino drag in this region.
Neutrino drag has a non-
negligible inﬂuence on all structures in the postshock
ﬂow that are responsible for signiﬁcant contributions to
the turbulent kinetic energy. It is neither accounted for
by the leakage schemes applied for neutrino energy and
lepton sources in all previous resolution studies (e.g.,
Couch & O’Connor 2014; Couch & Ott 2015; Abdika-
malov et al. 2015; Radice et al. 2016) nor by the simple
heating and cooling treatment used in our work, but
it requires the inclusion of neutrino-momentum transfer
terms in the equation of motion (see Appendix B).


## Page 24


24
T. Melson, D. Kresse, & H.-T. Janka
7.2. Conclusions
In our systematic resolution study, designed in a very
careful way to avoid numerical perturbations (mainly
grid-induced “noise” and ﬂuctuations associated with
neutrino eﬀects) as much as possible, we witnessed a
beneﬁcial eﬀect of higher angular resolution on shock
revival. This can be understood by a lower level of nu-
merical viscosity, allowing for higher turbulent kinetic
energy because of reduced viscous damping and dissipa-
tion of nonspherical ﬂows. Convergence of the overall
shock dynamics in 3D seems to be approached at an
angular resolution of about 1◦, but simulations with a
resolution of 2◦are not far oﬀ, despite the fact that prop-
erties characterizing turbulence, for example the exact
shape of the turbulent energy spectrum and the scale
when dissipation sets in, still exhibit diﬀerences when
improving the resolution to 0.5◦. Also in this context,
our simulations with 1◦angular resolution match the re-
quirements of convergence to a Kolmogorov-like behav-
ior (at least for ℓ≳30) by displaying a clear separation
of inertial range and dissipation range in the turbulent
kinetic-energy spectra, contradicting a proposition by
Radice et al. (2018) that these two length scales are usu-
ally merged in core-collapse supernova simulations and
therefore misidentiﬁed.
The bottleneck eﬀect pointed out by Radice et al.
(2015, 2016, 2018), which is present in the turbulent
energy spectra even for the highest feasible resolutions,
seems to have a relatively minor inﬂuence on the overall
shock evolution. Such a possibility was also admitted by
Radice et al. (2016). This may be explained by the fact
that most of the turbulent kinetic energy, which pro-
duces turbulent pressure to support shock expansion, is
carried by vortex motions on large scales but not on the
smallest scales near the dissipation regime.
The convergence of the supernova dynamics seen
around 1◦angular resolution provides some back-up
to the successful 3D explosion models computed with
the Prometheus-Vertex and Alcar codes by Mel-
son et al. (2015a,b), Summa et al. (2018), and Glas et al.
(2019) with a resolution of 2◦. Higher angular resolution
has been found to be supportive of an explosion, and
resolution-dependent diﬀerences are mostly relevant for
cases whose postbounce evolution proceeds very close to
the threshold between successful explosion and failure.
Based on our estimates of the magnitudes of numeri-
cal viscosity and of neutrino drag acting on the ﬂow
in the gain layer, we infer that both eﬀects are in the
same ballpark for the numerical resolutions applied in
the models of this work. Increasing the resolution sig-
niﬁcantly beyond an angular resolution of 1◦–2◦is an
exercise of direct relevance for the case of core-collapse
supernovae only when neutrino viscosity (at high densi-
ties where neutrinos diﬀuse) and neutrino drag (outside
of the diﬀusion regime) are taken into account.
Using our new SMR grid setup for improving the an-
gular resolution in deﬁned computational domains had
the drawback that kinetic energy was converted to in-
ternal energy in ﬂows crossing the borders from ﬁner to
coarser grid under the constraint of total energy conser-
vation. In models evolving very close to the explosion
threshold, this undesirable eﬀect was found to weaken
the explosion, whereas robustly exploding models re-
mained unaﬀected. Finally, our result of higher angular
resolution being favorable for explosion in 3D contra-
dicts the trend seen by Hanke et al. (2012). The reason
for this diﬀerence is the use of a polar grid in the pre-
vious simulations, whereas an axis-free Yin-Yang grid
was applied in the current work. The presence of the
polar-axis singularity and smaller azimuthal grid cells
in the vicinity of the polar axis caused numerical arti-
facts that were stronger for lower-resolution runs. Corre-
spondingly enhanced turbulent activity in the postshock
region produced more favorable conditions for explosion
in the lower-resolved 3D models of Hanke et al. (2012).
In contrast, the cleaner setup of the resolution study
presented here revealed the opposite behavior. Our ﬁnd-
ings that grid eﬀects can have a severe inﬂuence on
the solutions should also be taken as a clear warning
that great caution is demanded when resolution stud-
ies based on Cartesian grids with AMR (e.g., Couch &
O’Connor 2014; Couch & Ott 2015; Abdikamalov et al.
2015) or based on constrained volumes with radial and
angular boundaries (e.g., the semiglobal setup consid-
ered by Radice et al. 2016) are interpreted. Boundary
artifacts and unavoidable numerical noise imposed on
radial ﬂows on Cartesian grids, whose scale and ampli-
tude diﬀer when the resolution is varied, could aﬀect the
results and might provoke misleading trends.
Our work constitutes a very careful investigation of
resolution eﬀects in 3D supernova simulations with the
Prometheus code for comparison with results and
their interpretation in the literature. It suggests that
previous studies revealed incorrect trends, namely op-
posite to our resolution-dependent results, because of
numerical artifacts associated with the existence of a
polar grid axis or numerical perturbations induced by
Cartesian grids. “Realistic” simulations of stellar core
collapse and explosions, however, are probably not seri-
ously jeopardized by any of these numerical shortcom-
ings, maybe not even by a moderate overestimation of
numerical viscosity in the neutrino-heating layer due to
the choice of modest spatial resolution, enforced by lim-
ited computational resources. The pre-collapse pertur-
bations in the infalling stellar matter that are caused
by ﬂuctuations associated with convective shell burning
in the progenitor stars (e.g., Couch & Ott 2013; M¨uller


## Page 25


Resolution Study with Prometheus-Vertex
25
& Janka 2015; Couch et al. 2015; M¨uller et al. 2016;
Yoshida et al. 2019; Yadav et al. 2019), provide a strong
driving force of postshock turbulence, which is likely to
easily dominate the damping eﬀects of numerical viscos-
ity in the currently best-resolved 3D supernova models
(e.g., M¨uller et al. 2017, 2019).
We thank Alexander Summa for stimulating discus-
sions, Robert Glas for improving the numerical accu-
racy of our analysis of the turbulent energy spectra, and
Bernhard M¨uller and Ewald M¨uller for their valuable
comments on the manuscript. The 3D simulations were
performed on SuperMUC at the Leibniz Supercomput-
ing Centre with resources granted by the Gauss Centre
for Supercomputing (LRZ project IDs: pr48ra, pr53yi).
For the computation of the 1D and 2D simulations and
for the postprocessing of the data, we employed the Hy-
dra system of the Max Planck Computing and Data
Facility (MPCDF). The project was supported by the
European Research Council through grant ERC-AdG
No. 341157-COCO2CASA and by the Deutsche For-
schungsgemeinschaft through Sonderforschungsbereich
SFB 1258 “Neutrinos and Dark Matter in Astro- and
Particle Physics” (NDM).
Software:
Prometheus-Vertex (Fryxell et al.
1989; Rampp & Janka 2002; Buras et al. 2006), NumPy
and Scipy (Oliphant 2007), IPython (Perez & Granger
2007), Matplotlib (Hunter 2007).
APPENDIX
A. STATIC MESH REFINEMENT
Both the spherical polar grid and the Yin-Yang
grid have a common disadvantage.
The surface ele-
ment dA = r2 sin θ dθ dφ is proportional to the radius
squared. For a given constant angular resolution, the ef-
fective size of the grid cells grows with increasing radius.
Fine angular resolution near the grid center can im-
pose severe constraints on the Courant-Friedrichs-Lewy
(CFL) time step, while coarse resolution at large radii
(behind the supernova shock) limits the possibility to
resolve turbulent ﬂows. Here, we present a static mesh
reﬁnement (SMR) technique, which compensates for the
diverging structure of these spherical grids.
The SMR setup allows us to deﬁne certain radial in-
tervals with diﬀerent angular resolutions. An example
for such a setup is given in Fig. A1 in two dimensions
for coordinates (r, θ). Although this was chosen for the
sake of simplicity here, the discussion is completely ana-
logue to the 3D case, where it applies to both angular
directions, θ and φ. Let us deﬁne the angular resolution
in Fig. A1 for r < r1 as ψ. Then, the resolution between
r1 and r2 is 2ψ, and further reﬁned to 6ψ for r > r2.
Generally, arbitrary integer reﬁnement steps and an
A
B
C
D
E
θ
r
r1
r2
Figure A1. Example of a setup with static mesh reﬁnement
(SMR) in two dimensions. The angular resolution increases
by a factor of 6 from the center to the outer edge of the grid.
The ghost cells for the green-shaded radial sweep between
r1 and r2 are illustrated as green hatched areas. Note that
unlike the exemplary setup shown in this ﬁgure, all supernova
applications with SMR grid discussed in the main text were
performed with doubling of the resolution in each angular
direction at both SMR interfaces.
arbitrary number of concentric layers can be chosen in
our implementation.
Note that the inner spherically
symmetric volume, which is used in our simulations to
allow for larger hydrodynamical time steps, can be un-
derstood as a special case with the lowest possible an-
gular resolution corresponding to the whole sphere.
The radial locations of the reﬁnement boundaries can
be adjusted manually in our implementation at each
restart of the code. Such a shift is motivated, for ex-
ample, by a contraction of the gain radius that should
roughly be followed by the grid setup.
M¨uller (2015) and Skinner et al. (2019) also imple-
mented a similar setup, however, with the motivation of
avoiding time-step constraints as the grid cells become
smaller towards the grid singularities at the axis and at
the origin. In their “dendritic” grid, they coarsen only
the polar grid (θ) to compensate for the diverging cell
size with increasing radius. The azimuthal mesh (φ) is
coarsened towards the axis, which is not required in our
setup when we use the axis-free Yin-Yang grid.
A.1. Treatment of the hydrodynamics
Generally, the SMR procedure only aﬀects the radial
direction. The computations of θ and φ sweeps remain
unchanged. Besides the spherical polar grid, using the
Yin-Yang grid is thus also possible and only requires a
slight modiﬁcation. As the angular resolution changes in
the computational domain, the Yin-Yang ghost cell posi-
tions providing the boundary conditions for the angular
sweeps are diﬀerent for each reﬁnement layer, which has
to be considered when data is exchanged between both
grid patches.
Radial sweeps are computed separately for every res-
olution layer. For an example, consider the green-ﬁlled
grid cells in Fig. A1, for which the radial sweep should


## Page 26


26
T. Melson, D. Kresse, & H.-T. Janka
be calculated.
Let us assume that one ghost cell is
needed below and one above this sweep, depicted as
green-hatched areas. On the lower side, the ghost cell
data can directly be taken from cell A. This is because
ﬁnite-volume methods generally assume that values in
a cell always represent averages. At the upper end of
the sweep, we need to average over cells B, C, and D to
get the required data. Generally, averaging is required
for the ghost cells located in the ﬁner neighboring layer.
This is the reason why only integer reﬁnement steps are
allowed in the SMR construction. Otherwise, computing
the averages would be diﬃcult and introduce additional
interpolation errors.
A.2. Flux correction
If we naively used the averaged ghost cell data from
the ﬁner layer at the outer end of a radial sweep, numer-
ical inaccuracies would occur resulting in the violation
of conservation laws. In order to ensure exact conserva-
tion of the conserved quantities in our hydrodynamical
scheme, a “ﬂux correction” algorithm is applied acting
on the outermost cell of each reﬁnement region. We will
explain this procedure with the aid of Fig. A1. Note
that the ﬂux correction is also done for the spherically
symmetric innermost volume, which is usually employed
in 3D to mitigate the time step constraints at the grid
origin.
In our example illustrated in Fig. A1, the ﬂux cor-
rection considers the interface between the cell E and
the cells B, C, and D at r2.
After all radial sweeps
have been calculated, the quantity X—a placeholder for
a conserved quantity in our hydrodynamical scheme—
should be exactly conserved. The considered interface
at r2 is part of four diﬀerent radial sweeps: the sweep
between r1 and r2 containing the cell E, and the three
sweeps beyond r2 containing the cells B, C, and D. In
the following, we discuss the diﬀerent Riemann ﬂuxes
of X at the interfaces between these four cells and their
corresponding ghost zones. Let FE be the ﬂux density of
X at the upper edge of the cell E. Likewise, FB, FC, and
FD, denote the ﬂux densities at the lower boundaries of
the cells B, C, and D, respectively. All these ﬂuxes are
evaluated at the interface r2 with positive values corre-
sponding to the radially outward direction. The areas
of the cell interfaces are labeled AE, AB, AC, and AD.
Theoretically, it should hold
FEAE
!= FBAB + FCAC + FDAD.
(A1)
This is, however, not guaranteed numerically. In order
to cure this problem, the value of X in cell E is updated
to
Xnew = X + ∆t FEAE −FBAB −FCAC −FDAD
VE
,
(A2)
where ∆t is the time step length and VE the volume
of cell E. In this way, diﬀerences of Riemann ﬂuxes are
converted into updates of conserved quantities. This is
done for all variables at all interfaces between layers of
diﬀerent angular resolution to ensure that global conser-
vation laws are fulﬁlled numerically.
A.3. Treatment of the neutrino transport
The implementation of the neutrino transport requires
some modiﬁcations when the SMR procedure is used.
Generally, the computational grids, on which the hy-
drodynamics and the neutrino transport are computed,
should be identical in the regime where neutrinos are
tightly coupled to the stellar matter.
Otherwise, the
source terms given by the transport solution are not
well-balanced with the internal energy density of the
ﬂuid, for which reason deviations from thermodynamic
equilibrium can arise (Rampp & Janka 2002). These,
in turn, can cause numerical ﬂuctuations perturbing the
simulation.
In the context of the SMR grid, the coarsest angular
grid of the innermost multi-dimensional reﬁnement layer
is chosen to coincide with the transport angular grid so
that the number of transport rays can remain unchanged
throughout the radial grid. For example, the complete
wedge shown in Fig. A1 would be one transport ray with
the ﬁrst reﬁnement step at r1 being placed in a region
where the neutrino opacity is already suﬃciently low and
neutrinos are not expected to reach equilibrium with the
ﬂuid. For r > r1, the input for the neutrino transport
solver is obtained by angular averages of the hydrody-
namical quantities, similar to the ﬁlling procedure of the
ghost cells of diﬀerent angular resolution patches. The
computed source terms for the hydrodynamical equa-
tions are ﬁnally applied to all hydrodynamic cells crossed
by the particular transport ray.
B. NEUTRINO DRAG IN THE GAIN LAYER
In the high-density regime of a hot neutron star, neu-
trino diﬀusion applies because the neutrino mean free
paths are much shorter than the length scales of struc-
tures and gradients of the stellar medium. In this limit
neutrino momentum transfer by scattering and absorp-
tion creates viscosity (e.g., Keil et al. 1996; Guilet et al.
2015, and references therein). Thus it aﬀects shear ﬂows,
has a damping inﬂuence on velocity ﬂuctuations, and
creates viscous dissipation of kinetic energy.
In the
turbulent neutrino-heating layer, however, the optical
depth for neutrinos is typically less than ∼0.2. The neu-
trino mean free paths are much longer than the scales of
velocity perturbations. In this case neutrino momentum
transfer cannot be treated as a viscous process but neu-
trinos exert a drag force on the stellar plasma. The drag
is connected to Doppler eﬀects seen from the comoving


## Page 27


Resolution Study with Prometheus-Vertex
27
frame of the ﬂuid and acts opposite to the direction of
the plasma motion. Since the neutrino-radiation ﬁeld is
highly anisotropic in the gain region, drag calculations
available in the literature (e.g., Subramanian & Barrow
1998; Nio et al. 1998; Agol & Krolik 1998; Guilet et al.
2015), which assume isotropic radiation in the labora-
tory, are not directly applicable. We therefore provide a
more detailed assessment for the relevant SN conditions
in the following.
B.1. Fundamental equations
In the ﬂuid momentum equation the radiation force
appears as a source term (Mihalas & Mihalas 1984;
Hubeny & Mihalas 2014):
∂(ρv)
∂t
+ ∇· [ ρ(v ⊗v) + p I −S ] = ρg + G ,
(B3)
where ρ, v, p, S, and g are the stellar-ﬂuid density, ve-
locity, pressure, viscous stress tensor, and gravitational
acceleration, I is the unit matrix, (a ⊗b)ij = aibj the
outer (dyadic) product of two vectors, and G the net
radiative force density on the material, i.e., the rate
with which radiation and matter exchange momentum
(in both directions) per unit volume:
G = 1
c
Z ∞
0
dϵ
I
dω n (χn,ϵIn,ϵ −ηn,ϵ) .
(B4)
Here In,ϵ = I(r, t; n, ϵ) denotes the radiation inten-
sity, which depends on time t, spatial position r, neu-
trino energy ϵ, and neutrino momentum direction n,
χn,ϵ = χ(r, t; n, ϵ) is the extinction coeﬃcient (opac-
ity) containing true absorption and scattering contri-
butions, and ηn,ϵ = η(r, t; n, ϵ) is the total emissivity
including a thermal-emission part and a scattering part.
G = G(r, t) also appears with the opposite sign on the
right-hand side (rhs) of the total radiation momentum
equation:
1
c2
∂F
∂t + ∇· P = −G
(B5)
with F = F (r, t) being the radiation ﬂux density and
P = P(r, t) the radiation pressure tensor.
All radiation quantities in these equations (radiation
intensity, radiation moments, energy, direction of mo-
tion) are measured in the laboratory frame. For evalu-
ating the radiation force density, it is most convenient
to consider G in its mixed-frame form where the ma-
terial coeﬃcients are computed in the comoving (rest)
frame of the stellar ﬂuid while radiation quantities and
energies are in the inertial (laboratory) frame. With χ0
and η0 denoting the ﬂuid-frame quantities, one gets to
ﬁrst order in (v/c) (Mihalas & Mihalas 1984):
G =
1
c
Z ∞
0
dϵ χt
0(ϵ)F (ϵ)
−v
c
Z ∞
0
dϵ 4π
c η0(ϵ)
−v
c ·
Z ∞
0
dϵ

χ0(ϵ) + ϵ ∂χ0
∂ϵ

P(ϵ) =
=
G(1) + G(2) + G(3),
(B6)
where in contrast to Mihalas & Mihalas (1984) we have
accounted for the anisotropy of neutrino-nucleon and
neutrino-nuclei scattering, which leads to the transport
opacity (indicated by the superscript “t” and deﬁned
in Section B.3) appearing in the ﬁrst term on the rhs
instead of the angle-integrated opacity. The ﬁrst term
on the rhs of Eq. (B6) corresponds to the force density
of the radiation acceleration, while the ﬂuid-velocity de-
pendent terms denote the force density for the radiation
drag.5 Equation (B6) is compatible with expressions for
the radiation drag applied, e.g., by Agol & Krolik (1998);
Nio et al. (1998). While these works focused on isotropic
radiation ﬁelds and (isotropic) Thomson scattering of
photons oﬀelectrons, we will evaluate Eq. (B6) in Sec-
tion B.3 for neutrino absorption, emission and scattering
in reactions with nucleons and nuclei in the gain layer,
taking into account the anisotropy of the neutrino mo-
mentum distribution in this region. In Section B.4, we
will quantify the neutrino-drag eﬀects in more detail by
evaluating results from a 20 M⊙core-collapse simulation
with Prometheus-Vertex.
B.2. Order of magnitude estimates
The force density for the neutrino radiation accelera-
tion (ﬁrst term) on the rhs of Eq. (B6) scales with the
product of the total neutrino opacity, χt
0 = κt = κa + κt
s
(absorption opacity plus transport opacity for scatter-
ing; see Section B.3), and the total (energy integrated)
neutrino ﬂux, F(r), which can be written also in terms
of the luminosity, F = L/(4π r2):
Gacc ∝1
c ⟨κt⟩F = 1
c
⟨κt⟩L
4π r2 ,
(B7)
where the angle brackets indicate a suitable average over
the radiated neutrino spectrum. Summing up the con-
tributions of all neutrino species νi (i running from 1 to 6
for νe, ¯νe and the four types of heavy-lepton neutrinos),
and setting the neutrino acceleration force in relation to
the gravitational force by the neutron star of mass M,
5 In Newtonian hydrodynamics the term G(2) should be omit-
ted, because it would be compensated in the special relativistic
modeling by a reduction of the relativistic mass (i.e., no change
of the velocity would take place).


## Page 28


28
T. Melson, D. Kresse, & H.-T. Janka
GMρ/r2 (G being the gravitational constant), one gets
P
i Gacc,νi
GMρ/r2
=
X
i
Lνi⟨κt⟩νi
4πc GMρ ∼
X
i
Lνi
⟨κt⟩
4πc GMρ . (B8)
In the transformation to the ﬁnal form we have assumed
that the opacities oﬀall kinds of neutrinos are (very
roughly) similar.
This is a valid assumption because
the dominant interactions of νe and ¯νe are charged-
current absorption as well as neutral-current scatter-
ing with free nucleons (and, if present, with nuclei),
whereas heavy-lepton neutrinos only undergo scatter-
ings but have signiﬁcantly higher root mean square en-
ergies (the cross sections of all mentioned processes scale
with the square of the neutrino energy). Now consider-
ing that the optical depth of the gain layer is typically
τgain ≈⟨κt⟩(Rsh −Rgain) and the width of the gain layer
(diﬀerence between average shock radius, Rsh, and av-
erage gain radius, Rgain) is typically around 107 cm, we
estimate that ⟨κt⟩∼10−8 cm−1, i.e., the average neu-
trino mean free path is roughly ten times larger than
the diameter of the gain layer. With that we obtain
Gacc
GMρ/r2 ≲1
40
Lν,53⟨κt⟩−8
M1.5 ρ9
,
(B9)
where Gacc = P
i Gacc,νi, Lν = P
i Lνi, and Lν, ⟨κt⟩, M,
and the density in the gain region, ρ, have been normal-
ized by 1053 erg s−1, 10−8 cm−1, 1.5 M⊙, and 109 g cm−3,
respectively. We thus conﬁrm the general understand-
ing that neutrino momentum transfer is a small eﬀect in
the gain layer because the neutrino luminosity is far be-
low the Eddington limit. This is just a manifestation of
the fact that neutrino-driven supernova explosions are
powered by neutrino heating rather than being caused
by neutrino-momentum transfer.
In the second and third terms on the rhs of Eq. (B6)
the emissivity 4π
c η0 as well as the integrand depending
on P scale similarly with the product of neutrino opacity
and the speciﬁc neutrino-energy density E(ϵ) = ∂E/∂ϵ
(see Section B.3). Thus we can recover the scaling rela-
tion used by Guilet et al. (2015) for the damping rate Γ
associated with the neutrino drag:
Gdrag ∝−ρ Γ v
(B10)
with6
Γ ∼E⟨κ⟩
ρ c
= F⟨κ⟩
⟨ξ⟩ρ c2 =
L⟨κ⟩
4πr2⟨ξ⟩ρ c2 ,
(B11)
where ⟨ξ⟩= ⟨ξ(r)⟩= F/(Ec) is the spectral average of
the ﬂux factor ξ. Using ⟨ξ⟩= ⟨ξ(r)⟩∼1 for the gain
layer and applying the same assumptions as employed
6 Note that κ in Eqs. (B11), (B12), and (B13) stands for χ0(ϵ)+
∂χ0/∂ϵ (see third term in Eq. (B6)), with χ0 = κ = κa + κs.
in the case of the neutrino acceleration term, we derive
Γ ∼
P
i Lνi⟨κ⟩νi
4π r2⟨ξ⟩ρ c2 ∼
 1 s−1 Lν,53⟨κ⟩−8
r2
7 ρ9
,
(B12)
where r7 = r/(107 cm) is a radial location between Rgain
and Rsh.
This result can be easily understood when
Eq. (B11) is slightly rewritten by introducing ρ = nBmB
(nB is the baryon number density and mB the average
baryon mass):
Γ ∼
P
i Fνi⟨κ⟩νi
⟨ξ⟩nB
·
1
mB c2 .
(B13)
Here, the ﬁrst factor is a multiple of the neutrino-heating
rate per baryon in the gain layer, because it includes
not only the heating reactions of νe and ¯νe absorp-
tions by nucleons but also the scattering processes of
all kinds of neutrinos with nucleons, which transfer a
similar amount of momentum per interaction. The total
eﬀect is therefore typically on the order of 1000 MeV s−1
per nucleon, to be compared with a nucleon rest mass-
energy of roughly mBc2 ≈940 MeV.
The Reynolds number for a viscous medium is deﬁned
as
Re ≡v l
µvis
,
(B14)
which weighs the importance of the inertial term ∇·
(ρv ⊗v) relative to the viscous term ∇· S with compo-
nents Sij ∝ρµvis(∂vi/∂xj). In Eq. (B14) v and l are
typical amplitudes and length scales of velocity pertur-
bations7 and µvis is the kinematic shear viscosity (with
units [cm2 s−1]). In analogy to Re one can also deﬁne
a “drag number”, Dr, to quantify the ratio of inertial
term and drag term. With Eq. (B10) this yields
Dr ≡
ρ v v
l |Gdrag| = v
l Γ .
(B15)
With the value of Γ estimated for the gain layer
(Eq. (B12)) and typical ﬂow velocities of v ∼109 cm s−1
on the largest spatial scales, l ∼Rsh −Rgain ∼107 cm,
we obtain a value for Dr of the order of
Dr ∼100 v9
l7

Γ
1 s−1
−1
.
(B16)
This means that the neutrino drag can be expected to
cause a damping inﬂuence on the ﬂuid motions on rel-
evant scales roughly in the ballpark of the numerical
viscosity eﬀects discussed in Section 5.2. However, in
contrast to the Reynolds number, which decreases with
smaller spatial scales, the drag number behaves in the
7 In this appendix, in contrast to the naming convention em-
ployed in Section 5 (see, e.g., Eq. (37)), we use l for the typical
length scales in order to avoid confusion with the luminosity, which
is labeled with L here.


## Page 29


Resolution Study with Prometheus-Vertex
29
opposite way. Assuming a turbulent ﬂow with a Kol-
mogorov spectrum, i.e. with a velocity vλ = v(λ/l)1/3
on spatial scales λ, one can write
Re(λ) = vλ λ
µvis
= v l
µvis
λ
l
4/3
,
(B17)
whereas we get
Dr(λ) = vλ
λ Γ = v
l Γ
 l
λ
2/3
.
(B18)
On small scales, i.e. for λ decreasing, the neutrino drag
loses its damping inﬂuence because the long neutrino
mean free paths prevent frequent neutrino interactions
in small volumes, diﬀerent from the action of viscous
shear in the ﬂuid. While on the largest scales in the gain
layer Dr ∼100 (Eq. (B16)), one expects for l/λ ∼100,
i.e. on the smallest well-resolved scales in the current
simulations (represented by a few grid cells), values
of Dr(λ) ∼2000.
Overall, these numbers are com-
patible with numerical Reynolds numbers in our best-
resolved 3D simulations (see Section 5.2 and Table 2).
We will evaluate the neutrino-drag more quantitatively
on grounds of results from full-ﬂedged neutrino trans-
port calculations in Section B.4 and compare it with
the magnitude of numerical-viscosity eﬀects.
B.3. Detailed evaluation
For a more accurate quantitative analysis we will now
evaluate the terms on the rhs of Eq. (B6) with the con-
ditions in the gain layer in greater detail.
B.3.1. Interaction coeﬃcients
The most relevant neutrino interaction processes for
momentum transfer around the gain layer (dominant on
a level of >95%) are νe and ¯νe absorption on free neu-
trons and protons, respectively, and, involving neutrinos
of all species, neutrino-nucleon scattering, as well as co-
herent neutrino scattering oﬀnuclei. The last process is
relevant only at conditions where nuclei are present, i.e.,
in the undissociated material in the infall region ahead
of the supernova shock and at temperatures T ≲1 MeV
behind the shock, where nucleons begin to recombine to
α-particles and later to heavier nuclei.
Accordingly, χ0 and χt
0 include additive contributions
from all of the mentioned reactions, evaluated in the rest
frame of the stellar ﬂuid. The corresponding opacities,
to lowest order in terms of the ratios of neutrino energy
ϵ to charged-fermion rest-mass energies, are (e.g., Tubbs
& Schramm 1975; Freedman et al. 1977; Bruenn 1985;
Janka 1991):
κ∗
a(ϵ)≈κa(ϵ) = 1 + 3g2
A
4
σ0

ϵ
mec2
2
n{n,p} ,
(B19)
κs,n(ϵ)= 1 + 3g2
A
16
σ0

ϵ
mec2
2
nn ,
(B20)
κs,p(ϵ)= 4(2 sin2θW−1
2)2 + 3g2
A
16
σ0

ϵ
mec2
2
np , (B21)
κs,A(ϵ)= A2
16

2 sin2θW−(1−2 sin2θW)

2Z
A −1
2
×
× σ0

ϵ
mec2
2
nA ,
(B22)
where mec2 ≈0.511 MeV is the rest-mass energy of elec-
trons, σ0 ≈1.76 × 10−44 cm2, gA ≈1.26, θW the Wein-
berg angle with sin2 θW ≈0.2315, and nn, np, and nA
are the number densities of free neutrons, free protons,
and nuclei with mass number A and charge number Z,
respectively. In Eq. (B19) the target particles are neu-
trons, n, for νe and protons, p, for ¯νe.
In the same
equation, κa and κ∗
a are distinguished by a factor Ψ(ϵ)
appearing in the latter quantity. It is deﬁned by (e.g.,
Cernohorsky et al. 1989)
Ψ(ϵ) = 1 −f{e−,e+}(ϵ)
1 −f{νe,¯νe}(ϵ) ,
(B23)
where fi(ϵ) = [1 + exp(ϵ/T −ψi)]−1 are the equilibrium
phase-space distributions of the fermions i with degen-
eracy parameters ψi and gas temperature T (measured
in energy units). This factor accounts for fermion-phase
space blocking (and ensures detailed balance). Because
of the high temperatures and relatively low densities,
fermions in the gain layer are nondegenerate and there-
fore Ψ ≈1. For this reason we can use κa instead of
κ∗
a.
For the scattering processes, the opacities for momen-
tum transfer (“transport opacities”), which appear in
the ﬁrst term on the rhs of Eq. (B6), are deﬁned by the
angle integral of the diﬀerential opacity including the
additional factor (1 −µ) in the integrand (µ = cos ϑs
with ϑs being the scattering angle between ingoing and
outgoing neutrino):
κt
s ≡
I
dω dκs
dω (1 −µ)
(B24)
(Cernohorsky et al. 1989; Janka 1991). Performing this


## Page 30


30
T. Melson, D. Kresse, & H.-T. Janka
integration one gets:
κt
s,n(ϵ) = 1 + 5g2
A
24
σ0

ϵ
mec2
2
nn ,
(B25)
κt
s,p(ϵ) = 4(2 sin2θW−1
2)2 + 5g2
A
24
σ0

ϵ
mec2
2
np , (B26)
κt
s,A(ϵ) = A2
24

2 sin2θW−(1−2 sin2θW)

2Z
A −1
2
×
× σ0

ϵ
mec2
2
nA ,
(B27)
Expressing the number densities ni in terms of the num-
ber fractions Yi or the mass fractions Xi, i.e.,
ni =
ρ
mB
Yi =
ρ
mB
Xi
Ai
,
(B28)
and using sin2 θW ≈0.25, we can write the total scat-
tering opacity κs as
κs(ϵ) = κs,n +κs,p +κs,A = Ks σ0

ϵ
mec2
2
ρ
mB
(B29)
with
Ks = 1
16
"
(1 + 3g2
A)Xn + 3g2
AXp +
X
i
N 2
i
Xi
Ai
#
,
(B30)
where the sum runs over all nuclear species including
and heavier than helium with neutron numbers Ni =
Ai −Zi. Analogously, the total transport opacity for
neutrino scattering is
κt
s(ϵ) = κt
s,n +κt
s,p +κt
s,A = Kt
s σ0

ϵ
mec2
2
ρ
mB
(B31)
with
Kt
s = 1
24
"
(1 + 5g2
A)Xn + 5g2
AXp +
X
i
N 2
i
Xi
Ai
#
.
(B32)
Introducing the deﬁnition
Ka,{n,p} = 1 + 3g2
A
4
X{n,p} ,
(B33)
the absorption opacity is
κa(ϵ) = Ka,{n,p} σ0

ϵ
mec2
2
ρ
mB
,
(B34)
where Ka,n applies for νe and Ka,p for ¯νe. Finally, the
total opacity χ0 and transport opacity χt
0, respectively,
in the comoving frame of the ﬂuid are
χ(t)
0 (ϵ) = K(t)
tot σ0

ϵ
mec2
2
ρ
mB
,
(B35)
where
K(t)
tot = Ka,{n,p} + K(t)
s
.
(B36)
With this we can straightforwardly obtain
χ0(ϵ) + ϵ ∂χ0(ϵ)
∂ϵ
= 3 Ktot σ0

ϵ
mec2
2
ρ
mB
,
(B37)
which is needed to evaluate the third integrand on the
rhs of Eq. (B6).
In terms of the absorption and scattering opacities,
the true emission and scattering contributions to the
emissivity coeﬃcient in the second integral of Eq. (B6)
read as follows (Mihalas & Mihalas 1984):
4π
c η0(ϵ)=κ∗
a(ϵ) Eeq
0 (ϵ) + κs(ϵ) E0(ϵ)
≈κa(ϵ) Eeq
0 (ϵ) + κs(ϵ) E(ϵ) ,
(B38)
where in the ﬁnal expression we have again assumed
that κ∗
a ≈κa for the absorption opacity of νe and ¯νe.
E(ϵ) = dE/dϵ is the diﬀerential energy density in the
lab frame and connected to the energy density in the
comoving frame of the ﬂuid by E0(ϵ) = E(ϵ) + O(v/c).
The additional term of order (v/c) is omitted because it
leads to a second-order correction in (v/c). The equilib-
rium energy density of νe or ¯νe is computed as
Eeq
0 (ϵ) = dEeq
0 (ϵ)
dϵ
=
4π
(hc)3
ϵ3
1 + exp(ϵ/T −ψν)
(B39)
with the degeneracy parameter ψν of the Fermi-Dirac
spectrum (h is Planck’s constant).
B.3.2. Emission model
In the following we assume that the neutron star ra-
diates neutrinos as a spherical source. In this case the
radiation ﬁeld is azimuthally invariant around the ra-
dial direction and depends only on the radius as spatial
coordinate and on the cosine of the angle θ relative to
the radial direction, µ = cos(θ). Moreover, the pressure
tensor P of the radiation ﬁeld is diagonal with compo-
nents Prr, Pθθ and Pφφ. This is a good approximation
for the situation in the gain layer even in the general 3D
case, because the diagonal elements of P dominate the
oﬀ-diagonal ones by at least an order of magnitude (see
Richers et al. 2017).
With the radiation intensity I(r; ϵ, µ) the radiation
moments (energy density, ﬂux, and pressure) can be
computed as
E(r; ϵ)= dE(ϵ)
dϵ
= 1
c
I
dω I = 2π
c
Z +1
−1
dµ I,
(B40)
F(r; ϵ)= dF(ϵ)
dϵ
=
I
dω µ I = 2π
Z +1
−1
dµ µ I,
(B41)
P(r; ϵ)= dP(ϵ)
dϵ
= 1
c
I
dω µ2I = 2π
c
Z +1
−1
dµ µ2I,(B42)
and the nonvanishing diagonal elements of the pressure


## Page 31


Resolution Study with Prometheus-Vertex
31
tensor are
Prr(ϵ) =P(ϵ) ,
(B43)
Pθθ(ϵ) =Pφφ(ϵ) = 1
2 [E(ϵ) −P(ϵ)] .
(B44)
For simplicity, let us also assume that the angular
and energy distributions of the radiated neutrinos can
be separated, i.e., we make the following ansatz for the
neutrino intensity:
I(r; ϵ, µ) ≡
c
(hc)3 N(r) ϵ fα(ϵ) g(µ) .
(B45)
Here N(r) is a normalization factor and fα(ϵ) is the
well established normalized alpha-ﬁt for the radiated
neutrino-number spectrum (Tamborra et al. 2014, and
references therein):
fα(ϵ) =
ϵα
Γα+1
α + 1
⟨ϵ⟩
α+1
exp

−(α + 1) ϵ
⟨ϵ⟩

(B46)
with the mean energy ⟨ϵ⟩and the gamma function
Γα+1 ≡
Z ∞
0
dx xα e−x = α Γα .
(B47)
The ﬁrst and second energy moments of fα yield the
normalization relation and the mean energy:
Z ∞
0
dϵ fα(ϵ) = 1
and
Z ∞
0
dϵ ϵ fα(ϵ) = ⟨ϵ⟩.
(B48)
To approximate the angular distribution function g(µ)
we assume that the neutrinos stream oﬀisotropically
and freely from a sharp neutrinosphere of radius Rν.
Therefore at radius r the emitted neutrinos ﬁll a cone
with half-opening angle θmax isotropically. This angle is
subtended by the radiating sphere when observed from
distance r and obeys the relation
µmin(r) = cos θmax(r) =
s
1 −
Rν
r
2
(B49)
for r ≥Rν. We therefore construct g(µ) by using the
Heaviside function Θ(µ −µmin) as
g(µ) = Θ(µ −µmin)
2π (1 −µmin) ,
(B50)
which satisﬁes the normalization condition
I
dω g(µ) =
Z 2π
0
dφ
Z +1
−1
dµ g(µ) = 1 .
(B51)
The normalization factor N(r) in Eq. (B45) can be
obtained by making use of the constraint that the angle-
energy integral of the intensity must yield the total lu-
minosity L. In our approximative emission model we
assume that the lab-frame luminosity L as well as the
corresponding neutrino energy spectrum and thus ⟨ϵ⟩
are conserved quantities exterior to the neutrinosphere:
L(r) = 4π r2
Z ∞
0
dϵ F(r; ϵ) = L(Rν) = L = const .
(B52)
Using now Eq. (B41) with Eqs. (B45), (B46), and (B50),
this yields:
N(r) =
L
2π r2 c (hc)−3 (1 + µmin) ⟨ϵ⟩.
(B53)
Introducing this and Eq. (B50) into Eq. (B45), we ﬁnally
obtain
I(r; ϵ, µ) =
L
4π2r2
ϵ
⟨ϵ⟩fα(ϵ) Θ(µ −µmin)
1 −µ2
min(r) .
(B54)
With the result of Eq. (B54) we can now com-
pute the angular integrals of the radiation intensity in
Eqs. (B40)–(B42),
E(r; ϵ)=
L
4π r2c
ϵ
⟨ϵ⟩fα(ϵ)
2
1 + µmin
,
(B55)
F(r; ϵ)=
L
4π r2
ϵ
⟨ϵ⟩fα(ϵ) ,
(B56)
P(r; ϵ)=
L
4π r2c
ϵ
⟨ϵ⟩fα(ϵ) 2
3
1 + µmin + µ2
min
1 + µmin
,(B57)
as well as the corresponding energy-integrated radiation
moments:
E(r)=
L
4π r2c
2
1 + µmin
,
(B58)
F(r)=
L
4π r2 ,
(B59)
P(r)=
L
4π r2c
2
3
1 + µmin + µ2
min
1 + µmin
.
(B60)
Because of the separation of energy and angle depen-
dence in I(r; ϵ, µ) the ﬂux factor is energy independent,
ξ(r)= F(r; ϵ)
E(r; ϵ) c = F(r)
E(r) c = 1
2 [1 + µmin(r)]
= 1
2

1 +
s
1 −
Rν
r
2

,
(B61)
with the limits ξ(Rν) = 1
2 and ξ(∞) = 1.
In order to evaluate the diﬀerent terms of the radiation
force density, Eq. (B6), we also need to compute the
third energy moment of fα(ϵ):
⟨ϵ3⟩=
Z ∞
0
dϵ ϵ3 fα(ϵ) = (α + 3)(α + 2)
(α + 1)2
⟨ϵ⟩3 .
(B62)
B.3.3. Radiation drag terms
Using the opacities discussed in Section B.3.1 and the
neutrino-emission model introduced in Section B.3.2, we


## Page 32


32
T. Melson, D. Kresse, & H.-T. Janka
Table 3. Numerical Reynolds numbers and estimates of gain-layer averaged neutrino-drag numbers for model s20.
tpb
Rgain
Rsh,min
R0
l
v
νN
Re
Γ
Dr
Lνe
L¯νe
Lνx
κνe
κ¯νe
κνx
[ms]
[km]
[km]
[km]
[km]
[109 cm/s]
[1013 cm2 s−1]
[s−1]
[1052 erg/s]
[10−8 cm−1]
200
66
88
77
53
1.19
4.0
158
16.2
14
6.58
6.23
4.01
5.99
4.98
2.36
300
54
131
93
94
1.11
4.4
238
9.1
13
4.42
4.56
3.43
1.51
1.37
0.58
400
46
198
122
216
1.28
7.1
389
4.8
12
4.02
4.32
3.20
0.62
0.56
0.24
500
40
513
277
722
1.09
15.4
511
0.5
31
3.29
3.58
2.86
0.05
0.05
0.02
Note— tpb is the post-bounce time, Rgain the average gain radius, Rsh,min the minimum shock radius, R0 the arithmetic mean
of Rgain and Rsh,min, l the length scale of the largest turbulent vortices (Eq. (B72)), v the characteristic nonradial velocity
measured at R0, νN the kinematic numerical viscosity, Re the corresponding Reynolds number, Γ the neutrino-damping rate
(Eq. (B70)), Dr the neutrino-drag number (Eq. (B15), using the listed values of Γ, v and l), Lνi are the luminosities of neutrino
species νi = νe, ¯νe, νx in the lab frame, and κνi ≡⟨χ0⟩νi the spectrally-averaged neutrino opacities in the comoving frame of
the ﬂuid. The numerical viscosity, νN, and corresponding Reynolds number, Re, are evaluated at radius R0 (as in Section 5),
whereas the neutrino-related quantities, Γ, Lνi, and κνi, are time-averaged over tpb ±2.5 ms and spatially averaged over a radial
shell extending from Rgain + 10 km to Rsh,min −10 km.
now provide the ﬁnal forms for the three terms of the
radiation force density on the rhs of Eq. (B6):
G = G(1) + G(2) + G(3) .
(B63)
Each of the three summands contains components from
all neutrino species:
G(j) = G(j)
νe + G(j)
¯νe + 4 G(j)
νx ,
(B64)
where j = 1, 2, 3 and we multiply the contribution of
an individual type of heavy-lepton neutrino (νx) by a
factor of 4 because of the near-equality of the emission
and interaction properties of the four species.
Because of the symmetry assumptions employed by us,
the only nonvanishing vector component of the radiation
acceleration is the radial one, G(1)
r . It is given by
G(1)
r,νi =Kt
tot,νi
ρ
mB
σ0
Lνi
4π r2c ×
×
(α + 3)(α + 2)
(α + 1)2

νi
 ⟨ϵ⟩νi
mec2
2
,
(B65)
where Kt
tot,νe = Ka,n + Kt
s, Kt
tot,¯νe = Ka,p + Kt
s, and
Kt
tot,νx = Kt
s with Ka,{n,p} from Eq. (B33) and Kt
s from
Eq. (B32).
For the radiation drag associated with the emission
term (true emission and outgoing scattering) we obtain
G(2)
νi =−v
c Ka,νi
ρ
mB
σ0
(mec2)2
4π
(hc)3 T 6 F5(ψνi)
−v
c Ks
ρ
mB
σ0
Lνi
4π r2c
2
1 + µmin(r) ×
×
(α + 3)(α + 2)
(α + 1)2

νi
 ⟨ϵ⟩νi
mec2
2
(B66)
with the Fermi integral F5(ψνi) =
R ∞
0
dx x5[1+exp(x−
ψνi)]−1 and the constants Ka,νe = Ka,n, Ka,¯νe = Ka,p,
Ka,νx = 0, and Ks from Eq. (B30).
Finally, making use of the diagonal nature of the radi-
ation pressure tensor in our emission model (Eqs. (B43)
and (B44) with Eq. (B57)), we ﬁnd for the force den-
sity of the radiation drag caused by momentum transfer
through neutrino absorption and ingoing scattering:
G(3)
νi =−v
c · M Ktot,νi
ρ
mB
σ0
Lνi
4π r2c
1
1 + µmin(r) ×
×
(α + 3)(α + 2)
(α + 1)2

νi
 ⟨ϵ⟩νi
mec2
2
,(B67)
where Ktot,νe = Ka,n + Ks, Ktot,¯νe = Ka,p + Ks, and
Ktot,νx = Ks with Ka,{n,p} from Eq. (B33) and Ks from
Eq. (B30).
Only the diagonal elements of M do not
vanish; they are
Mrr =2(1 + µmin + µ2
min) ,
(B68)
Mθθ =Mφφ = 2 −µmin −µ2
min .
(B69)
For the conditions in the gain layer the production of
νe and ¯νe plays a subordinated role compared to their
absorption. The ﬁrst summand in Eq. (B66) is therefore
negligible. From Eqs. (B68) and (B69) it is clear that
in the limit of radially streaming neutrinos at large dis-
tances (i.e., µmin →1) the nonradial components van-
ish and therefore, to ﬁrst order in v/c, radiation drag
acts only on the radial velocity component. Nonradial
eﬀects depend on Doppler shifts of the neutrino quan-
tities and have dropped out in Eq. (B6), because they
are of higher than linear order in v/c. During the accre-
tion phase of the stalled supernova shock the spectral
shape parameters α are typically between 2 and 3 (Mi-
rizzi et al. 2016; Tamborra et al. 2012).
The case of
α = 2 corresponds to a Maxwell-Boltzmann spectrum,
α ≈2.3 describes a Fermi-Dirac spectrum with vanish-
ing degeneracy parameter (ψ = 0), and α > 2.3 yields
pinched spectra with a faster decline beyond the maxi-
mum than the Fermi-Dirac distribution.


## Page 33


Resolution Study with Prometheus-Vertex
33
100 km
300 ms
100 km
400 ms
100 km
500 ms
100 km
300 ms
100 km
400 ms
100 km
500 ms
100 km
300 ms
100 km
400 ms
100 km
500 ms
100 km
300 ms
100 km
400 ms
100 km
500 ms
100 km
300 ms
100 km
400 ms
100 km
500 ms
0
5
10
15
20
25
30
Γ [s−1]
−10
−9
−8
−7
log10
 ⟨χ0⟩[cm−1]

0
1
2
log10 (lρ [km])
0
5
10
15
20
25
q
v2
θ + v2
φ [108 cm/s]
0
5
10
15
20
25
30
s [kB/by]
Figure B2. Cross-sectional cuts in the (x,y)-plane of model s20 with full neutrino transport and uniform 2◦angular resolution
at 300 ms, 400 ms, and 500 ms after bounce.
From top to bottom, the damping rate associated with the neutrino drag, Γ
(see Eq. (B70)), the spectrally-averaged neutrino opacity (in the ﬂuid frame) summed over all species, ⟨χ0⟩, the characteristic
hydrodynamic length scale, lρ (see Eq. (B73)), the nonradial velocity, (v2
θ + v2
φ)0.5, and the entropy per baryon, s, are shown.
The inner and outer dashed circles indicate the angle-averaged gain radius and the minimum shock radius, respectively.


## Page 34


34
T. Melson, D. Kresse, & H.-T. Janka
Table 4. Local evaluation of the neutrino-drag number, Dr,
at diﬀerent radii Rev for model s20.
tpb
Rev
lρ
v9
Γ
Dr
κνe
κ¯νe
κνx
[ms]
[km]
[km]
[s−1]
[10−9 cm−1]
200
76
29
1.19
16.7
24
63.2
52.1
24.7
78
31
1.19
15.7
25
58.0
48.4
22.9
R0
31
1.19
16.4
24
61.4
50.9
24.1
avg
30
1.18
16.2
24
59.9
49.8
23.6
300
64
23
1.32
20.5
28
40.7
35.3
14.5
100
55
1.03
8.1
23
12.7
11.5
4.9
121
94
0.94
5.4
19
9.4
8.5
3.7
R0
45
1.11
9.5
26
15.0
13.6
5.8
avg
60
1.07
9.1
20
15.1
13.7
5.8
400
56
19
1.75
30.1
30
46.6
40.4
16.1
100
48
1.44
8.5
35
10.1
9.2
3.9
150
101
1.06
3.4
31
4.3
3.9
1.7
188
215
0.90
1.9
22
2.8
2.6
1.1
R0
69
1.28
5.3
35
6.3
5.8
2.5
avg
113
1.16
4.8
21
6.2
5.6
2.4
500
50
17
2.34
34.1
41
41.0
36.1
14.1
100
52
1.55
7.6
39
6.5
6.0
2.5
150
84
1.35
2.9
55
2.6
2.4
1.0
200
115
1.25
1.4
79
1.3
1.2
0.5
250
185
1.15
0.8
82
0.7
0.7
0.3
300
217
1.03
0.4
118
0.4
0.4
0.2
350
320
0.96
0.2
123
0.3
0.3
0.1
400
420
0.89
0.1
142
0.2
0.2
0.1
450
636
0.82
0.1
125
0.1
0.1
0.1
500
722
0.77
0.1
165
0.1
0.1
0.1
R0
182
1.09
0.5
112
0.5
0.5
0.2
avg
438
0.95
0.5
45
0.5
0.5
0.2
Note— tpb is the post-bounce time, Rev the radius of the
evaluation, lρ the local characteristic hydrodynamical length
scale (Eq. (B73)), v9 = v/(109 cm s−1) the typical local tur-
bulent (nonradial) velocity, Γ the local neutrino-damping
rate (Eq. (B70)), Dr the corresponding local neutrino-drag
numbers (Eq. (B15)), and κνi ≡⟨χ0⟩νi are the spectrally-
averaged local neutrino opacities in the ﬂuid frame for νi =
νe, ¯νe, νx.
All quantities are averaged over radial shells of
10 km thickness around Rev and time-averaged over 5 ms.
Also listed are the values at radius R0, i.e., half-way be-
tween the mean gain radius and the minimum shock radius
as given in Table 3, and averages (“avg”) over the entire
shell of [Rgain +10 km, Rsh,min −10 km]. For the last case the
values of Γ and κνi are identical with those in Table 3.
B.4. Model-based evaluation
In order to quantify the neutrino-drag eﬀects in nu-
merical simulations, we analyse our 3D model s20 with
full neutrino transport and uniform angular resolution of
2◦(see Table 1). Since Prometheus-Vertex contains
a Newtonian hydrodynamics solver, we consider —in the
spirit of the remark in the footnote in Section B.1— only
the third term on the rhs of Eq. (B6). With their ray-
by-ray approach to neutrino transport, the simulations
provide results compatible with the symmetry assump-
tions for the neutrino-radiation ﬁeld considered in Sec-
tion B.3.
For the quantitative analysis, we apply several sim-
pliﬁcations, which ease the evaluation and are accept-
able in view of other approximations connected to the
ray-by-ray transport, which evolves only the radial com-
ponents of the neutrino ﬂuxes and assumes the neu-
trino phase-space distributions to be axially symmetric
around the radial direction. First, we focus on the radial
term of the neutrino drag, which dominates the nonra-
dial ones, as can be seen by comparing Eq. (B43) with
Eq. (B44) and Eq. (B68) with Eq. (B69). Second, we
do not transform the radiation quantities, in particular
the radiation-pressure tensor, P(ϵ), into the laboratory
frame.
Instead, we evaluate the drag terms with the
pressure tensor computed in the comoving frame of the
ﬂuid by the transport solver, in line with the available
opacities χ0. This simpliﬁcation is justiﬁed because on
the one hand the typical ﬂuid velocities in the postshock
layer are at most 5–10 % of the speed of light, and on
the other hand eﬀects of the transformation between lab
frame and comoving frame act in opposite directions in
convective downdrafts and outﬂows and therefore partly
compensate each other in the angle-averaged quantities
considered here. Third, we use only the nonradial ﬂuid
velocities in the postshock layer as a proxy of the turbu-
lent velocities in order to facilitate the direct comparison
with the numerical viscosity and Reynolds number along
the lines of their evaluation in Sect. 5.
Therefore, using Eq. (B10), we compute the damping
rate associated with the neutrino drag according to
Γ= |Gdrag|
ρ v
=
= 1
ρ c
X
νi
Z ∞
0
dϵ

χ0,νi + ϵ∂χ0,νi
∂ϵ

Pνi(ϵ) , (B70)
with Pνi(ϵ) given by the transport solver as integral of
the direction-dependent neutrino intensities according
to Eq. (B42). The neutrino-drag number, Dr, can then
be calculated with Eq. (B15). To directly compare Dr
with the numerical Reynolds numbers, Re, of our simu-
lation, we employ the same deﬁnitions for the character-
istic turbulent velocity, v, and for the length scale of the
largest turbulent eddies, l, as in Section 5.2.2, namely
v2 = 1
4π
Z
dΩ(v2
θ + v2
φ) ,
(B71)
l = Rsh −Rgain ,
(B72)
where Rsh and Rgain are the angle-averaged shock ra-


## Page 35


Resolution Study with Prometheus-Vertex
35
dius and gain radius, respectively. Note that we use a
diﬀerent naming convention here to avoid confusion of
the length scale, l, with the neutrino luminosity, L.
In Table 3 we list the neutrino-drag numbers, averaged
over the gain layer of model s20, at diﬀerent post-bounce
times, tpb, as well as the numerical Reynolds numbers,
Re, and numerical viscosities, νN, obtained with our
MKJ method based on the energy dissipation rate (see
Section 5.2.2).
As in Section 5, all hydrodynamical
quantities are measured at radius R0 (Eq. (20)) half-way
between the average gain radius and the minimum shock
radius, Rsh,min, and smoothed by performing an average
over a radial shell of R0 ± 5 km and an additional time
average over the interval tpb±2.5 ms. The neutrino-drag
numbers, Dr, are computed according to Eq. (B15) with
the neutrino-damping rate Γ from Eq. (B70) and with
the same values of v and l as used in the evaluation
of the numerical Reynolds numbers. Lνi are the neu-
trino luminosities (of species νi = νe, ¯νe, νx) in the lab
frame and κνi ≡⟨χ0⟩νi the spectrally-averaged neutrino
opacities in the comoving frame of the stellar ﬂuid. The
neutrino-related quantities, Γ, Lνi, and κνi, are spatially
averaged over a radial shell extending from Rgain+10 km
to Rsh,min −10 km and time-averaged over tpb ± 2.5 ms.
Since the matter density ρ, the neutrino opacities, and
the neutrino radiation quantities, all of which enter the
computation of the damping rate Γ (see Eq. (B70)) and
drag number Dr (Eq. (B15)), decline with increasing ra-
dius, we also investigate the radial dependence of the
neutrino drag in the gain layer.
Thus we intend to
test ambiguities in the determination of the neutrino-
drag eﬀects in terms of the characteristic parameter Dr.
Figure B2 displays some of the relevant quantities in
a cross-sectional plane at diﬀerent post-bounce times
to demonstrate their spatial variations in connection
with the convective vortex ﬂows. In order to perform a
radius-dependent analysis, we deﬁne a characteristic lo-
cal hydrodynamic length scale, constrained by the width
of the gain layer, as
lρ = min

¯ρ
|d¯ρ/dr| , Rsh −Rgain

,
(B73)
where ¯ρ is the angle-averaged matter density.
More-
over, we use local, shell-averaged values of the nonra-
dial (turbulent) velocity, v, and of the damping rate,
Γ (Eq. (B70)), in Eq. (B15) for estimating local val-
ues of Dr. The corresponding results are listed in Ta-
ble 4, where all local quantities are time-averaged over
5 ms and radially averaged over shells of 10 km thickness
around the locations of evaluation, Rev.
The data for the neutrino-drag number Dr in Tables 3
and 4 are consistent with our order-of-magnitude esti-
mate of Eq. (B16).
Typical values are several 10 up
to more than 100 in the gain layer. Naturally, the drag
numbers become particularly small when computed with
the radial width of the entire gain layer in Table 3, but
also the local values of Table 4 are only a factor of ∼2
bigger, except at large radii at 500 ms, where the neu-
trino opacities and neutrino pressure P(r), and corre-
spondingly the neutrino-damping rate, become small. A
comparison of the numerical Reynolds numbers, Re, and
the neutrino-drag numbers, Dr, in Table 3 conﬁrms that
on the scale of large and largest turbulent eddies in our
2◦simulation of model s20, the neutrino drag clearly
dominates the eﬀects of numerical viscosity.
Only on
scales smaller than l ≤
p
νN/Γ does damping by nu-
merical viscosity become compatible with the inﬂuence
of the neutrino drag on ﬂuid motions. This corresponds
to vortex ﬂows of less than 10–20 km diameter near the
gain radius (Rgain ∼50–70 km) and of less than 50–
60 km near the shock at a radius of about 200 km.
Neutrino-damping rates of ∼5–10 s−1 in the gain layer
suggest typical damping timescales of large-scale ﬂuid
motions on the order of 100–200 ms.
Such timescales
may be short enough to slightly delay or hamper the
onset of postshock convection.
A quantitative assess-
ment of such eﬀects and their potential consequences
for the onset of an explosion would require a compar-
ison with the model-speciﬁc growth timescales of con-
vection or SASI in the postshock layer. However, with
large-scale pre-collapse perturbations in the convective
silicon- and oxygen-burning shells of the progenitor (e.g.,
Couch & Ott 2013; M¨uller & Janka 2015; Couch et al.
2015; M¨uller et al. 2016; Yoshida et al. 2019; Yadav et al.
2019), the driving force for the growth of instabilities
(e.g., M¨uller et al. 2017; Kazeroni & Abdikamalov 2019)
should be suﬃciently strong to render neutrino drag a
subdominant eﬀect.
Our conclusions should not be severely aﬀected by
the simpliﬁcations made in our analysis as mentioned
at the beginning of this section.
Although consider-
ing nonradial velocities might moderately underestimate
the neutrino-drag number (because the radial velocities
may be somewhat higher), a rigorous evaluation of the
neutrino drag requires to sum up all components of the
vector-matrix product in the third term on the rhs of
Eq. (B6) with nonvanishing oﬀdiagonal matrix compo-
nents. This would increase the neutrino-damping rate
and reduce the drag number, thus countersteering the
velocity dependence. However, in order to account for
the eﬀects of the neutrino drag fully quantitatively, one
needs a transport treatment that does not only include
all velocity-dependent terms at least up to ﬁrst order
in v/c, but in addition it also requires a scheme that
reaches beyond the ray-by-ray approximation and there-
fore provides reliable values for the oﬀdiagonal elements
of the neutrino pressure tensor, too. All of these terms
must be included with proper frame dependences in the


## Page 36


36
T. Melson, D. Kresse, & H.-T. Janka
momentum equation of the stellar plasma as discussed
in Section B.1.
REFERENCES
Abdikamalov, E., Ott, C. D., Radice, D., et al. 2015, ApJ, 808,
70
Agol, E., & Krolik, J. 1998, ApJ, 507, 304
Blondin, J. M., & Mezzacappa, A. 2007, Nature, 445, 58
Blondin, J. M., Mezzacappa, A., & DeMarino, C. 2003, ApJ,
584, 971
Boris, J. P., Grinstein, F. F., Oran, E. S., & Kolbe, R. L. 1992,
FlDyR, 10, 199
Bruenn, S. W. 1985, ApJS, 58, 771
Buras, R., Rampp, M., Janka, H.-T., & Kifonidis, K. 2006,
A&A, 447, 1049
Burrows, A., Radice, D., & Vartanyan, D. 2019, MNRAS, 485,
3153
Cernohorsky, J., van den Horn, L. J., & Cooperstein, J. 1989,
JQSRT, 42, 603
Colella, P., & Woodward, P. R. 1984, JCoPh, 54, 174
Couch, S. M. 2013, ApJ, 775, 35
Couch, S. M., Chatzopoulos, E., Arnett, W. D., & Timmes,
F. X. 2015, ApJL, 808, L21
Couch, S. M., & O’Connor, E. P. 2014, ApJ, 785, 123
Couch, S. M., & Ott, C. D. 2013, ApJL, 778, L7
—. 2015, ApJ, 799, 5
Dolence, J. C., Burrows, A., Murphy, J. W., & Nordhaus, J.
2013, ApJ, 765, 110
Foglizzo, T., Galletti, P., Scheck, L., & Janka, H.-T. 2007, ApJ,
654, 1006
Foglizzo, T., Scheck, L., & Janka, H.-T. 2006, ApJ, 652, 1436
Freedman, D. Z., Schramm, D. N., & Tubbs, D. L. 1977,
ARNPS, 27, 167
Frisch, U. 1995, Turbulence (Cambridge University Press,
Cambridge)
Fryxell, B., M¨uller, E., & Arnett, D. 1989, in Proceedings of the
5th Workshop on Nuclear Astrophysics, ed. W. Hillebrandt &
E. M¨uller, 100
Fryxell, B., M¨uller, E., & Arnett, D. 1991, ApJ, 367, 619
Glas, R., Just, O., Janka, H. T., & Obergaulinger, M. 2019, ApJ,
873, 45
Grinstein, F. F., Margolin, L. G., & Rider, W. J. 2007, Implicit
Large Eddy Simulation (Cambridge University Press,
Cambridge)
Guilet, J., M¨uller, E., & Janka, H.-T. 2015, MNRAS, 447, 3992
Guilet, J., Sato, J., & Foglizzo, T. 2010, ApJ, 713, 1350
Handy, T., Plewa, T., & Odrzywo lek, A. 2014, ApJ, 783, 125
Hanke, F. 2014, PhD thesis, Technische Universit¨at M¨unchen
Hanke, F., Marek, A., M¨uller, B., & Janka, H.-T. 2012, ApJ,
755, 138
Hubeny, I., & Mihalas, D. 2014, Theory of Stellar Atmospheres
(Princeton University Press, Princeton)
Hunter, J. D. 2007, CSE, 9, 90
Janka, H.-T. 1991, PhD thesis, Technische Universit¨at M¨unchen
Janka, H.-T., Melson, T., & Summa, A. 2016, ARNPS, 66, 341
Kageyama, A., & Sato, T. 2004, GGG, 5, 9005
Kazeroni, R., & Abdikamalov, E. 2019, arXiv e-prints,
arXiv:1911.08819
Keil, W., Janka, H.-T., & M¨uller, E. 1996, ApJL, 473, L111
Kolmogorov, A. 1941, DoSSR, 30, 301
Kuroda, T., Kotake, K., Takiwaki, T., & Thielemann, F.-K.
2018, MNRAS, 477, L80
Kuroda, T., Takiwaki, T., & Kotake, K. 2016, ApJS, 222, 20
Landau, L. D., & Lifshitz, E. M. 1987, Fluid Mechanics
(Pergamon, Oxford)
Lattimer, J. M., & Swesty, F. D. 1991, NuPhA, 535, 331
Lentz, E. J., Bruenn, S. W., Hix, W. R., et al. 2015, ApJL, 807,
L31
Mabanta, Q. A., & Murphy, J. W. 2018, ApJ, 856, 22
Marek, A., Dimmelmeier, H., Janka, H.-T., M¨uller, E., & Buras,
R. 2006, A&A, 445, 273
Melson, T. 2016, PhD thesis, Technische Universit¨at M¨unchen
Melson, T., Janka, H.-T., Bollig, R., et al. 2015a, ApJL, 808, L42
Melson, T., Janka, H.-T., & Marek, A. 2015b, ApJL, 801, L24
Mihalas, D., & Mihalas, B. W. 1984, Foundations of radiation
hydrodynamics (Oxford University Press)
Mirizzi, A., Tamborra, I., Janka, H.-T., et al. 2016, NCimR, 39, 1
M¨uller, B. 2015, MNRAS, 453, 287
M¨uller, B., & Janka, H.-T. 2015, MNRAS, 448, 2141
M¨uller, B., Melson, T., Heger, A., & Janka, H.-T. 2017,
MNRAS, 472, 491
M¨uller, B., Viallet, M., Heger, A., & Janka, H.-T. 2016, ApJ,
833, 124
M¨uller, B., Tauris, T. M., Heger, A., et al. 2019, MNRAS, 484,
3307
M¨uller, E. 1998, in Saas-Fee Advanced Course 27:
Computational Methods for Astrophysical Fluid Flow, ed.
O. Steiner & A. Gautschy (Springer-Verlag, Berlin), 343
M¨uller, E., Fryxell, B., & Arnett, D. 1991, A&A, 251, 505
Murphy, J. W., Dolence, J. C., & Burrows, A. 2013, ApJ, 771, 52
Nio, T., Matsuda, T., & Fukue, J. 1998, PASJ, 50, 495
O’Connor, E. P., & Couch, S. M. 2018, ApJ, 865, 81
Oliphant, T. E. 2007, CSE, 9, 10
Ott, C. D., Roberts, L. F., da Silva Schneider, A., et al. 2018,
ApJL, 855, L3
Ott, C. D., Abdikamalov, E., M¨osta, P., et al. 2013, ApJ, 768,
115
Perez, F., & Granger, B. E. 2007, CSE, 9, 21
Pope, S. B. 2000, Turbulent Flows (Cambridge University Press,
Cambridge)
Porter, D. H., & Woodward, P. R. 1994, ApJS, 93, 309
Porter, D. H., Woodward, P. R., & Pouquet, A. 1998, PhFl, 10,
237
Radice, D., Abdikamalov, E., Ott, C. D., et al. 2018, JPhG, 45,
053003
Radice, D., Couch, S. M., & Ott, C. D. 2015, ComAC, 2, 7
Radice, D., Ott, C. D., Abdikamalov, E., et al. 2016, ApJ, 820,
76
Rampp, M., & Janka, H.-T. 2002, A&A, 396, 361
Richers, S., Nagakura, H., Ott, C. D., et al. 2017, ApJ, 847, 133
Roberts, L. F., Ott, C. D., Haas, R., et al. 2016, ApJ, 831, 98
Sato, J., Foglizzo, T., & Fromang, S. 2009, ApJ, 694, 833
Schmidt, W. 2014, Numerical Modelling of Astrophysical
Turbulence (Springer, Berlin)
Skinner, M. A., Dolence, J. C., Burrows, A., Radice, D., &
Vartanyan, D. 2019, ApJS, 241, 7
Sreenivasan, K. R. 1995, PhFl, 7, 2778
Subramanian, K., & Barrow, J. D. 1998, PhRvD, 58, 083502
Summa, A., Janka, H.-T., Melson, T., & Marek, A. 2018, ApJ,
852, 28
Sytine, I. V., Porter, D. H., Woodward, P. R., Hodson, S. W., &
Winkler, K.-H. 2000, JCoPh, 158, 225
Takiwaki, T., Kotake, K., & Suwa, Y. 2012, ApJ, 749, 98
—. 2014, ApJ, 786, 83
Tamborra, I., M¨uller, B., H¨udepohl, L., Janka, H.-T., & Raﬀelt,
G. 2012, PhRvD, 86, 125031
Tamborra, I., Raﬀelt, G., Hanke, F., Janka, H.-T., & M¨uller, B.
2014, PhRvD, 90, 045032


## Page 37


Resolution Study with Prometheus-Vertex
37
Tennekes, H., & Lumley, J. L. 1972, First Course in Turbulence
(MIT Press, Cambridge)
Tubbs, D. L., & Schramm, D. N. 1975, ApJ, 201, 467
Vartanyan, D., Burrows, A., Radice, D., Skinner, M. A., &
Dolence, J. 2019, MNRAS, 482, 351
Wongwathanarat, A., Hammer, N. J., & M¨uller, E. 2010, A&A,
514, A48
Woosley, S. E., & Heger, A. 2007, PhR, 442, 269
—. 2015, ApJ, 810, 34
Yadav, N., M¨uller, B., Janka, H. T., Melson, T., & Heger, A.
2019, arXiv e-prints, arXiv:1905.04378
Yeung, P. K., & Zhou, Y. 1997, PhRvE, 56, 1746
Yoshida, T., Takiwaki, T., Kotake, K., et al. 2019, ApJ, 881, 16

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1904_01699v2_resolution_study_for_three_dimensional_supernova_simulations_with_the_prometheus
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1904_01699V2_RESOLUTION_STUDY_FOR_THREE_DIMENSIONAL_SUPERNOVA_SIMULATIONS_WITH_THE_PROMETHEUS.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

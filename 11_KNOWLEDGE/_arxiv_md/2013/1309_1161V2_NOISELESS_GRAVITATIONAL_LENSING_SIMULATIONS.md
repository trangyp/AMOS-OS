---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1309.1161v2
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1309.1161v2_Noiseless_Gravitational_Lensing_Simulations

> Source: 1309.1161v2_Noiseless_Gravitational_Lensing_Simulations.pdf

> Pages: 13

---


## Page 1


arXiv:1309.1161v2  [astro-ph.CO]  25 Sep 2013
Mon. Not. R. Astron. Soc. 000, 1–13 (2013)
Printed 3 June 2021
(MN LATEX style ﬁle v2.2)
Noiseless Gravitational Lensing Simulations
Raul E. Angulo∗1,2, Ruizhu Chen2, Stefan Hilbert3& Tom Abel2,4
1Centro de Estudios de F´ısica del Cosmos de Arag´on, Plaza San Juan 1, Planta-2, 44001, Teruel, Spain.
2Kavli Institute for Particle Astrophysics and Cosmology,
Stanford University, SLAC National Accelerator Laboratory, Menlo Park, CA 94025, USA.
3 Max-Planck-Institute for Astrophysics, Karl-Schwarzschild-Str. 1, 85740 Garching, Germany.
4Institut Lagrange de Paris, Institut d’Astrophysique de Paris, 98 bis boulevard Arago - 75014 Paris, France.
3 June 2021
ABSTRACT
The microphysical properties of the DM particle can, in principle, be constrained by the
properties and abundance of substructures in DM halos, as measured through strong
gravitational lensing. Unfortunately, there is a lack of accurate theoretical predictions for
the lensing signal of substructures, mainly because of the discreteness noise inherent to
N-body simulations. Here we present Recursive-TCM, a method that is able to provide
lensing predictions with an arbitrarily low discreteness noise, without any free parameters
or smoothing scale. This solution is based on a novel way of interpreting the results of N-
body simulations, where particles simply trace the evolution and distortion of Lagrangian
phase-space volume elements. We discuss the advantages of this method over the widely
used cloud-in-cells and adaptive-kernel smoothing density estimators. Applying the new
method to a cluster-sized DM halo simulated in warm and cold DM scenarios, we show
how the expected diﬀerences in their substructure population translate into diﬀerences
in the convergence and magniﬁcation maps. We anticipate that our method will provide
the high-precision theoretical predictions required to interpret and fully exploit strong
gravitational lensing observations.
Key words:
gravitational lensing: strong – gravitational lensing: weak – cosmology:
theory – dark matter – large-scale structure of the Universe – methods: numerical
1
INTRODUCTION
Gravitational Lensing has become a powerful and robust tech-
nique to explore the “dark side” of our Universe (see Bartel-
mann 2010, for a recent review). In the near future, it is ex-
pected to probe the accelerated cosmic expansion, and to con-
strain the properties of the dark matter (DM) particle.
In the weak regime, lensing by the large-scale structure
of the Universe causes small distortions in the apparent shape
of galaxies and in the temperature ﬂuctuations maps at the
last scattering surface. This eﬀect can be detected statisti-
cally by future wide-ﬁeld surveys (e.g DES1, J-PAS2, Euclid3,
LSST4), and by Cosmic Microwave Background (CMB) ex-
periments (Planck5, SPT6, ACT7). From correlations in the
distortions, one can infer the amplitude, shape, and redshift
evolution of the matter power spectrum – quantities sensitive
∗Email: reangulo@cefca.es
1 http://www.darkenergysurvey.org/
2 http://j-pas.org/
3 http://sci.esa.int/euclid/
4 http://www.lsst.org/
5 http://www.esa.int/Our_Activities/Space_Science/Planck/
6 http://pole.uchicago.edu/
7 http://www.princeton.edu/act/
to the initial density perturbations, the law of gravity and the
cosmic expansion. Therefore, gravitational lensing measure-
ments are expected to contribute signiﬁcantly to our under-
standing of the Dark Energy and the physics of the early Uni-
verse (e.g. Huterer 2010; Marian et al. 2011; Oguri & Takada
2011; Hilbert et al. 2012; Giannantonio et al. 2012).
In the strong regime, eﬃcient lensing conﬁgurations can
produce multiple images of the same background galaxy or
quasar. Each of these images is further distorted by interven-
ing small-scale structures, thus the diﬀerences in their shape
and/or ﬂux can be used to constrain the substructure content
of galaxy and cluster haloes (Mao & Schneider 1998; Met-
calf & Madau 2001; Dalal & Kochanek 2002; Kochanek &
Dalal 2004; Natarajan & Springel 2004; Natarajan et al. 2007;
Vegetti et al. 2010). This method is, in fact, the only way
of detecting substructures in distant galaxies (Vegetti et al.
2012). The amount and compactness of halo substructures de-
pends strongly on the nature of the DM particle: colder candi-
dates produce more and denser substructures (e.g. Moore et al.
1999; Klypin et al. 1999; Diemand et al. 2007; Springel et al.
2008); particles with larger self-interaction cross-sections pro-
duce shallower and more spherical density proﬁles (Meneghetti
et al. 2001; Peter et al. 2013). Therefore, strong gravitational
lensing can probe the microphysical properties of the DM par-
c⃝2013 RAS


## Page 2


2
R. Angulo, R. Chen, S. Hilbert, T. Abel
ticle and thus provide a direct test of the Cold Dark Matter
(CDM) paradigm.
In order to fully exploit gravitational lensing measure-
ments in both strong and weak regimes, it is essential to have
accurate predictions for the nonlinear state of the mass dis-
tribution in the Universe. In particular, for the abundance,
spatial distribution and internal properties of DM halos and
their substructure. Among the diﬀerent theoretical approaches
available, cosmological N-body simulations appear as the only
robust and accurate method that meets these requirements.
Moreover, cosmological N-body simulations (e.g. Peebles
1971; Efstathiou & Eastwood 1981; Efstathiou et al. 1985;
Springel et al. 2005; Angulo et al. 2012) are also invaluable
cosmological tools: i) They are the most reliable and precise
method to follow the highly nonlinear evolution of primor-
dial density ﬂuctuations (e.g. Kuhlen et al. 2012, for a re-
cent review). ii) They provide virtual universes with which we
can test, predict, and interpret astronomical observations (e.g.
Overzier et al. 2013). iii) They allow us to experiment with the
laws of physics and the background cosmological model (e.g.
Fontanot et al. 2012, 2013). Thus, numerical simulations not
only can provide the theoretical predictions required by gravi-
tational lensing, but also can be particularly useful for testing
analysis algorithms and for exploring the connection between
lensing observations and the underlying cosmological model
(Bartelmann et al. 1998; Jain et al. 2000; Vale & White 2003;
Meneghetti et al. 2007; Hilbert et al. 2009).
Unfortunately, numerical simulations have a serious limi-
tation that is inherent to the formulation of the N-body prob-
lem: in order to eﬃciently solve the Poisson-Vlasov equation,
the initial cosmic density ﬁeld must be represented by a set of
discrete bodies. This discretization is necessary to eﬃciently
follow the dynamics and evolution of the DM ﬂuid, but it
introduces a small-scale noise that is very often larger than
the small-scale lensing signal itself. The noise decreases on
large scales and/or with better mass resolution. However, it
is still comparable to the strong lensing signal from most of
the substructure population, even with the highest resolution
simulations to date (Xu et al. 2009; Rau et al. 2013). In other
words, the substructure lensing properties that could allow us
to constrain the DM particle mass remain buried beneath the
discreteness noise. Hence, current theoretical predictions are
not suﬃciently accurate for upcoming lensing measurements.
In this paper, we propose Recursive-TCM8, a method
to create gravitational lensing simulations free of discreteness
noise, with no tunable parameters nor additional smoothing
scales. Our procedure builds on a recently proposed method
to solve for the collisionless dynamic of the DM ﬂuid (Abel
et al. 2012; Shandarin et al. 2012; Hahn et al. 2013; Kaehler
et al. 2012; Angulo et al. 2013). The novel approach considers
simulation particles as the vertices of Lagrangian phase-space
volume elements, not mass carriers as in the usual interpre-
tation of numerical simulations. The evolution and distortion
of these volume elements is described by the Eulerian coor-
dinates of simulation particles. Consequently, the DM density
ﬁeld is determined by the spatially overlapping phase-space
elements, these can be exactly deposited onto a target grid
using a recursive algorithm. The result is a continuous and
smooth density ﬁeld ideal for small-scale lensing simulations.9
8 The term Recursive-TCM abbreviates for ”Recursive deposit of
Tethrahedra approximated by their Center of Mass”.
9 The reduction of discreteness noise also helps to suppress the arti-
We devote this paper to the presentation and testing of
the algorithm. We start in Section 2 by describing how we
compute the gravitational lensing signal of a set of simulation
particles. We then apply our method to a cluster-size halo sim-
ulated in CDM and WDM cosmologies. These simulations are
described in Section 3. In Section 4, we compare our method
with standard approaches, and show how the noise in the sur-
face density and magniﬁcation maps is greatly reduced. This
allows us to explore the impact of substructure on the strong
lensing magniﬁcation ﬁelds for our CDM and WDM haloes.
We present our conclusions and a discussion of possible future
work in Section 5.
2
LENSING SIMULATIONS
We start by describing how the gravitational lensing signal of
a set of simulation particles is computed, including details of
our method to estimate the respective surface density maps.
2.1
Gravitational lensing
Within the plane lens approximation, the lensing distortions
produced by a concentrated mass distribution can be derived
from a lensing potential, Ψ(θ), (e.g. Bartelmann & Schneider
2001)
Ψ(θ) = 1
π
Z
d2θκ(θ) ln
θ −θ′ ,
(1)
where θ = (θ1, θ2) denotes an angular position on the (plane)
sky, and the convergence κ(θ) is deﬁned as
κ(θ) = Σang(θ)
Σang
c
.
(2)
Here, Σang(θ) denotes the projected angular surface mass den-
sity of the lens mass concentration. The critical angular surface
mass density is deﬁned as
Σang
c
=
c2
4πG
aLfLfS
fLS
,
(3)
with the speed of light c, gravitational constant G, scale factor
aL at lens redshift, and comoving angular diameter distances
fL, fS, and fLS from the observer to the lens, from the ob-
server to the source, and between the source and the lens,
respectively.
The deﬂection angle α(θ) =
 α1(θ), α2(θ)

, the complex
shear γ(θ) = γ1(θ) + iγ2(θ), and the magniﬁcation µ(θ), are
given by
α(θ) =
 Ψ1(θ), Ψ2(θ)

,
(4)
γ(θ) = 1
2 [Ψ22(θ) −Ψ11(θ)] −iΨ12(θ),
(5)
µ(θ) =

[1 −κ(θ)]2 −|γ(θ)|2	−1 .
(6)
where the subscripts refer to partial derivatives with respect
to one of the angular coordinates.
There are several ways of computing the lensing sig-
nal from numerical simulations (e.g Wambsganss et al. 1998;
Couchman et al. 1999; Jain et al. 2000; Aubert et al. 2007;
Hilbert et al. 2009). Here we choose one of the simplest, which
ﬁcial fragmentation of ﬁlaments seen in warm Dark Matter (WDM)
simulations (Hahn et al. 2013; Angulo et al. 2013).
c⃝2013 RAS, MNRAS 000, 1–13


## Page 3


Noiseless Lensing Simulations
3
consists in computing the surface density on a regular lattice
and then solving for the lensing potential in Fourier space:
ΨF (ℓ) = 1
π κF (ℓ) lnF (ℓ)
(7)
2π2ℓ2ΨF (ℓ) = −κF (ℓ)
(8)
where the superscript F indicates a Fourier transform. These
expressions can be readily evaluated by using Fast Fourier
Transforms (FFT). However, this requires additional correc-
tions, because FFT algorithms implicitly assume periodic
boundary conditions, while the appropriate conditions should
be vacuum boundary conditions. To suppress shear artefacts
induced by periodic images of the mass distribution, gener-
ous zero padding is employed.10 To recover the correct mean
convergence [which is lost in the FFT methods due to setting
κF (ℓ= 0) to zero], the potential from the FFT is corrected by
a term ∝θ2. Finally, the lensing deﬂection, shear, and magni-
ﬁcation can be obtained by computing derivatives of Ψ either
in Fourier space, or in real space by using ﬁnite diﬀerence
methods (Hilbert et al. 2009).
2.2
Recursive-TCM: A new density estimator
The problem is now reduced to obtain the surface mass den-
sity, Σ(θ), on a uniform grid from which the respective lensing
potential can be computed. Essentially, this step consists in
mapping a three-dimensional (3D) distribution of simulation
particles onto a two-dimensional (2D) grid. Although it is in
principle a simple task, in practice it is rather diﬃcult to accu-
rately carry out the mapping. Several authors have explored
diﬀerent projection methods and have concluded that all of
them gave rise to a noise ﬁeld of amplitude comparable to
the strong lensing signal produced by real DM substructures
(Bradaˇc et al. 2004; Li et al. 2006; Xu et al. 2009; Rau et al.
2013). This is true even for the highest mass resolution simula-
tions of DM haloes available to date. Similarly, large-scale N-
body simulations, with volumes comparable to that of future
wide-ﬁeld galaxy surveys, have typically low number densities
of simulation particles, which adds a Poisson shot-noise that
dominates the small-scale predictions for weak gravitational
lensing (e.g. Jain et al. 2000; Vale & White 2003; Sato et al.
2009; Hilbert et al. 2009).
There are several proposed ways of dealing with this prob-
lem. For strong lensing, one of the most common is to model
the smooth component of a DM halo with an analytic expres-
sion (e.g. a Single Isothermal Sphere), and then add on top
the substructure population (e.g. Xu et al. 2009). Although,
it is possible to incorporate the correct density proﬁle and the
triaxiality of the DM halo, this method washes out all other
higher-order or more subtle features of the DM halo substruc-
tures such as streams, caustics, etc. For weak lensing, maps
are often smoothed with a ﬁxed-size kernel, which decreases
the particle noise but also erases actual small-scale structure
(Hilbert et al. 2009; Takahashi et al. 2011).
Here, we discuss Recursive-TCM, a mass-depositing
scheme that captures a simulated density ﬁeld in all its com-
plexity without the noise introduced by the ﬁnite number of
particles, and without any smoothing parameter. The method
extends the techniques proposed by Abel et al. (2012); Hahn
et al. (2013); Kaehler et al. (2012); Angulo et al. (2013),
10 For simplicity, we refrain from also applying a force-range cut-
oﬀ.
and thus we refer to them for an extensive discussion of the
method. The key idea is to consider simulation particles as
vertices of Lagrangian phase-space tetrahedra. At any redshift,
the particles indicate the current positions of these vertices. To
create surface density maps, the matter represented by these
tetrahedra is distributed on a target mesh using a recursive
splitting scheme.
One way of interpreting our method is that it assigns to
each particle a smoothing kernel whose size and shape are
given by their Lagrangian (not Eulerian as in most smoothing
methods) neighbours. In particular, this kernel is anisotropic
and not even uniquely deﬁned in an Eulerian space. We also
note that our method is conceptually diﬀerent to those that
project a Delaunay or Voronoi tessellation built from the Eu-
lerian particle distribution (Schaap & van de Weygaert 2000;
Bradaˇc et al. 2004).
The four main steps of Recursive-TCM are:
1) Creating the Initial Tessellation: First, we need to
deﬁne a set of disjoint Lagrangian phase-space elements that
fully ﬁll the volume of a N-body simulation. In three dimen-
sions, the most natural choice is a Delaunay tessellation of the
unperturbed particle distribution. The result is a set of tetra-
hedra (six times more abundant than the number of particles)
whose corners are given by the simulation particles.11 The con-
nectivity of each tetrahedra is ﬁxed and stored (it can also be
trivially recovered from the particles’ ID number in case the
ID is related to the position of a particle in an unperturbed
lattice).
2) Reconstructing the Evolved Tessellation: After
the simulation has been evolved and the particles moved to
diﬀerent locations, the initial set of tetrahedra (which there-
fore also moved) is reconstructed using the stored connectiv-
ity. The internal density of each tetrahedron is assumed to be
uniform, and the density ﬁeld at any given location is simply
given by all those tetrahedra that intersect the target location.
We note that it is also possible to compute, at any point of
space, other quantities besides the density, such as the number
of streams, the velocity dispersion tensor, vorticity, etc. (Hahn
et al in prep).
3) Projecting the Density Field: The next step is to
compute the projected density ﬁeld on a grid, i.e, to map the
tetrahedra onto a 2D regular mesh. The simplest way, called
TCM by Hahn et al. (2013), is to represent each tetrahedron
by a single point mass located at the center of mass. Another
option is to represent each tetrahedra by 4 particles, preserving
the monopole and quadrupole of the parent polyhedra (Hahn
et al. 2013). Here we propose a more exact deposit, referred
to as Recursive-TCM, which consists in recursively biparting
each tetrahedron along its longest edge. The process continues
until all the child tetrahedra are completely contained inside
one grid cell, or a maximum number of levels in the recur-
sion is reached. Then, each child tetrahedra is subsequently
represented using a single particle of mass 2−lmtet (where l
is the recursion level and mtet is the mass of the top tetra-
hedron) that is deposited using a Nearest Grid Point (NGP)
assignment scheme.
11 Constructing the tessellation can be a computationally expen-
sive task for state-of-the-art simulations (e.g. Pandey et al. 2013).
However, this is trivial if the particle distribution is arranged in
a regular lattice (as opposite to a glass-like distribution): each set
of 8 grid points deﬁnes a cube that is subdivided into six disjoint
tetrahedra.
c⃝2013 RAS, MNRAS 000, 1–13


## Page 4


4
R. Angulo, R. Chen, S. Hilbert, T. Abel
4) Removing Density Biases: Over the range of scales
in which the mass resolution of a given simulation is adequate
to describe the evolution and distortion of Lagrangian phase-
space volumes, our method provides a very reliable proxy for
the density ﬁeld (Abel et al. 2012). However, tetrahedron-
based density calculations are biased if the distortion of an
initial phase-space volume can not be represented by linear
transformations. This happens in two situations. One is at
the center of DM haloes, which have high densities and short
dynamical times. As discussed in Hahn et al. (2013), this has
the net eﬀect of densities being overestimated at the halo cen-
ter, and underestimated at slightly outer regions. The second
situation regards the tidal stripping of substructures, where
some vertices of a given tetrahedron are stripped while others
might still be attached to the substructure. This has the net
eﬀect of underestimating the mass associated to substructures.
Fortunately, these biases in the density are small and can
be identiﬁed and corrected for. Moreover, the centers of haloes
are typically dominated by a stellar component (specially in
galaxy-sized DM haloes, where the observational search for
substructures is focused), and also are aﬀected by baryonic
processes absent in DM-only N-body simulations (such as
feedback, adiabatic compression, etc). Hence, any DM-only-
based predictions need to be altered to account for these and
produce realistic lensing eﬃciencies (e.g. Xu et al. 2009), so
an additional correction that remove biases of our density es-
timator can be easily included.
Here we propose and use a simple way to remove the bias:
4.1) We ﬁrst compute an unbiased 2D density map using a
traditional (noisier) estimator applied to the same object.
4.2) We then apply a correction factor, deﬁned as the aver-
age ratio between densities computed using a traditional es-
timator and the Recursive-TCM, in bins of Recursive-TCM
densities. This aims to correct the overestimation of central
densities.
4.3) We apply an additional correction factor to account for
spatially coherent, large-scale biases related to tidal strip-
ping of substructures. This extra factor is set to the ratio of
the density maps using the traditional and the Recursive-
TCM estimator (after the above correction is applied), both
Gaussian smoothed to keep only large-scale modes.
As we will show in the next section (cf.Section 3.4), this
simple correction procedure eliminates most biases in the sur-
face density maps, preserving the reduced noise properties.
We note, however, that more sophisticated correction methods
are possible and should decrease the biases even further. Some
possible extensions are applying corrections to 3D densities in-
stead of projected ones, and/or applying separate correction
factors for diﬀerent substructures.
3
RECURSIVE-TCM IN ACTION
For illustrative purposes, we now apply our new method to
numerical simulations of cold and warm DM cosmologies. We
start by presenting these N-body simulations, together with
one particular DM halo on which we focus our analysis. Then,
we provide details of our density estimator when applied to
these simulated objects.
3.1
Parent N-body runs
We employ two of the cosmological N-body calculations pre-
sented in Angulo et al. (2013), that simulate two diﬀerent
cosmological scenarios: i) a standard CDM, and ii) a Warm-
DM (WDM) model with a 250 eV DM particle mass. In
the latter, ﬂuctuations below k ∼1h Mpc−1 are suppressed,
which translates into a lack of collapsed structures below
M ∼2×1012h−1M⊙, and consequently into a strong suppres-
sion of the subhalo population of massive haloes. Although
this WDM model is ruled out by observations (Viel et al.
2013), we will consider it for illustrative purposes. The cos-
mological parameters for the simulations are consistent with
the WMAP7 data release (Komatsu et al. 2011): Ωm = 0.276,
ΩΛ = 0.724, Ωb = 0.045, h = 0.703, σ8 = 0.811 and spectral
index ns = 0.96.
Each of these two simulations corresponds to a cubic re-
gion of L = 80h−1Mpc side length, containing 10243 simu-
lation particles of mass 3.65 × 107h−1M⊙. The initial condi-
tions were created using the MUSIC code (Hahn & Abel 2011)
at z = 63. The particles were subsequently evolved using a
Tree-PM method, as implemented in the L-Gadget3 code (An-
gulo et al. 2012; Springel et al. 2005). Gravitational forces are
smoothed using a Plummer-equivalent softening length set to
5h−1kpc. Additionally, we have located DM haloes using a FoF
algorithm (Davis et al. 1985) (using a standard value for the
linking length b = 0.2), and identiﬁed self-bound substructures
(or subhalos) within these haloes using the SUBFIND algorithm
(Springel et al. 2001).
The numerical simulations were started using identical
phases and evolved with the same numerical parameters,
which allows a direct comparison of structure formation in
general, and of the gravitational lensing signatures explored
in our paper.
3.2
Target cluster-sized DM halo
For our strong gravitational lensing analysis, we will focus on
the most massive cluster present in our simulations at z = 0.
This object has a mass of M200 = 4.38×1014 h−1M⊙, and it is
resolved with more than 10 million particles. For comparison,
this corresponds roughly to the lowest resolution runs of the
clusters in the Phoenix project (Gao et al. 2012), and it is a
factor of 10 coarser than the main cluster employed by Rau
et al. (2013).12 The force resolution is ∼250 times smaller
than the halo’s virial radius, and thus the halo structure is
resolved adequately for our purposes.
The spherically averaged density proﬁle of the halo is well
ﬁtted by a cored NFW proﬁle (Navarro et al. 1996, 1997),
ρ(r)−1 ∝
p
(r/rs)2 + (rc/rs)2(1 + r/rs)2, with concentration
rs/r200 = 3.9, and core radius, rc = 5h−1kpc, both in CDM
and WDM. We note that the core is a numerical artifact, and
arises due to the lack of force resolution on scales smaller than
the simulation softening length.
Fig. 1 shows an image of the selected halo in our two cos-
mological scenarios. The DM halo displays the same overall
structure in WDM and in CDM, and the diﬀerences caused
by the DM particle mass are evident only in their small-scale
properties. In CDM, the halo contains a wealth of substruc-
ture: a large number of small clumps that are the remnants
12 Our force resolution is also much lower.
c⃝2013 RAS, MNRAS 000, 1–13


## Page 5


Noiseless Lensing Simulations
5
Figure 1.
Projected DM density, as computed by Recursive-TCM, for the most massive halo in our simulations at z = 0 (M200 =
4.38 × 1014h−1M⊙). Each image corresponds to a square region of 3.05h−1Mpc side length and 3h−1Mpc projection depth around the
cluster center. The white circle indicates the virial radius R200 = 1.229 h−1Mpc. The left panel shows the halo in a WDM scenario, the right
panel assumes a CDM cosmology.
of previously accreted DM haloes. These, in contrast, are al-
most absent when WDM is adopted, but caustics, streams
and ﬁlaments are instead much better deﬁned. Inside R200 of
the CDM halo, we ﬁnd 2121 substructures with more than 15
particles, which corresponds to a minimum subhalo mass of
Ms ⩾7.3 × 108h−1M⊙. Contrasting this, we found only 119
substructures inside the WDM halo – which are mostly a re-
sult of numerical fragmentation of ﬁlaments (Wang et al. 2007;
Angulo et al. 2013). The substructure population contributes
1.7% and 6.5% of the mass inside R200, respectively for our
WDM and CDM halo.
Considering
only
substructure
with
masses
above
1010 M⊙, the subhalo mass function in CDM follows a power
law dn/d log ms ∝m−0.79
s
. However, the slope decreases to
−0.66 when we consider all the subhalos detected. These val-
ues are shallower that the average slope found in other sim-
ulations (-0.9, e.g. Angulo et al. 2008; Gao et al. 2012). The
discrepancy is most likely caused by our low force resolution
compared to our mass resolution (many low-mass haloes are
tidally disrupted too eﬃciently due to our low force resolu-
tion, which makes our subhalo mass function being incomplete
up to higher subhalo masses than in simulations with smaller
softening lengths), which could explain the change in slope in
the subhalo mass function. Although these discrepancies are
not important for our work, we caution the reader that the
amount of substructure in our work is underestimated com-
pared to other simulations of similar mass resolution.
3.3
Recursive-TCM lensing simulations
We are now in position of applying our method to the WDM
and CDM halo described before. We artiﬁcially place the
haloes at z = 0.32, where the most massive galaxy clusters
are expected to be observed, and assume a background source
population located at z = 2. We consider the 3D particle
distribution inside a region of dimensions 0.6 × 0.6 h−1Mpc
(equal to 0.5 × R200) and 3 h−1Mpc deep centred on our halo,
and project it onto a 10002-pixels mesh. This yields a spa-
tial resolution of 0.6h−1kpc, suﬃcient to resolve the smallest
structures present in our simulation given our gravitational
resolution limit (5h−1kpc).
We apply our full Recursive-TCM algorithm using a max-
imum of ten recursion levels, i.e. every top-level tetrahedron is
split into 210 = 1024 smaller tetrahedra, at most. Using these
maps, we create convergence ﬁelds, compute the lensing po-
tential, and derive the associated µ, γ, and α, as described in
Section 2.1. We use a 327682 FFT mesh (this is approximately
a factor of thousand larger than the density mesh to allow for
non-periodic boundary conditions), and compute the spatial
derivatives in Fourier space. We note that by considering only
a small inner region, we are neglecting the weak lensing eﬀects
of structures further away from the cluster center. However,
we have explicitly checked that this is a good approximation
for the quantities explored here.
The computational cost of our Recursive-TCM algorithm
is higher than usual projection methods, but it is still negligi-
ble compared to the time employed in carrying out an N-body
simulation. For our particular data structure, data access and
target grid, and maximum recursion level, it took 123 min-
utes using 256 processors, i.e. 500 CPU hours. It is important
to remember that this corresponds to an implementation in
software for CPUs, and that less recursion levels signiﬁcantly
reduce the execution time. In addition, alternative algorithms
based on GPU-rendering routines can, in principle, achieve
signiﬁcantly better performances (Kaehler et al. 2012).
For comparison, we computed densities using two other
techniques, in addition to Recursive-TCM. The ﬁrst one, re-
ferred to as CiC, represents each particle by a cube of uni-
form density and size equal to the cell size of the target grid.
This is the most-common projection method in cosmology
(Hockney & Eastwood 1981). The second method, referred
to as Sph, employs a spherically-symmetric polynomial ker-
c⃝2013 RAS, MNRAS 000, 1–13


## Page 6


6
R. Angulo, R. Chen, S. Hilbert, T. Abel
Figure
2.
Relation
between
the
densities
estimated
using
Recursive-TCM and Sph, for 10002 pixels covering the inner 0.6 ×
0.6h−1Mpc region centred in our WDM cluster. The red line display
the mean value in logarithmic bins of ∆log ρrtcm = 0.1.
nel (Springel et al. 2005) to project each particle onto our
2D grid. The characteristic size of the kernel is given by the
local density about each particle, explicitly, by the 3D dis-
tance to the 32-th nearest neighbour. This approach is the
core of the Smoothed-Particle-Hydrodynamics (SPH, Mon-
aghan 1992) numerical formalism.
3.4
Bias correction
As discussed in Section 2.2, Recursive-TCM densities can be
biased in regions where heavy winding of the primordial phase-
space sheet occurs. Fortunately, we can use a noisy estimator
to correct for such biases, as we will show. In practice, we
follow the procedure described in §2.2 and apply a two-step
bias correction.
The ﬁrst step corrects for the overestimation of central
densities by an average factor, shown in Fig. 2. This factor was
computed as the geometric mean of the ratio between densi-
ties estimated using Sph and Recursive-TCM, in logarithmic
bins of ∆log ρrtcm = 0.1. Because the densities produced by
our tetrahedral approach are biased high in central regions of
DM haloes (see Section 2.2), the average ratio progressively
decreases at higher densities. The largest correction factor is
0.4 at the very center of our halo.
The second correction step accounts for spatially coher-
ent biases. In Fig. 3, we show the ratio between convergence
maps in Sph and in Recursive-TCM for our WDM halo and
after the ﬁrst correction has been applied. Ideally, this ﬁgure
would be a pure white-noise ﬁeld, however, we can clearly see
that there is a large-scale component in this ﬁeld. This arises
partially because the 2D projected density ﬁeld is not a one-
to-one function of the full 6D phase-space structure (which de-
termines the amount of winding and overestimation). Another
aspect contributing to this map is related to mass accretion
history and shortcomings of the tetrahedron-based densities to
Figure 3.
Fractional diﬀerences between the convergence maps
built using the Sph and Recursive-TCM methods. The region dis-
played correspond to the inner 0.6 × 0.6h−1Mpc centered in our
WDM halo.
represent the tidal stripping of infalling DM halos. In order to
correct for this, we further divide the Recursive-TCM map by
the a version of the map shown in Fig. 3, but smoothed with
a Gaussian kernel of size 50h−1kpc. We note that this scale is
set to be larger than those dominated by discreteness noise in
Sph. As we will see later, the simple procedure described here,
is successful in producing accurate lensing maps.
4
RESULTS
We now present and discuss the results of our lensing simula-
tions. We ﬁrst focus on the input surface density maps, and
then on the lensing magniﬁcation. In particular, we discuss
the performance of our algorithm and the role of discreteness
noise compared to the signal of DM substructures.
4.1
The surface densities and lensing convergence
Fig. 4 shows maps of the surface density in the inner regions
of our WDM (top row) and CDM haloes (bottom row). Each
column shows the result of one of our three projection meth-
ods, as indicated by the legend. Note that the colour scale is
identical in all six panels.
In both cosmological scenarios, we can appreciate how
the small-scale noise is decreased from left to right. The CiC
method shows the largest ﬂuctuations, though we note that
the visual impression of the noise depends on the target mesh
resolution, as this sets the size of the CiC smoothing kernel.
The Sph method reduces the noise signiﬁcantly in this case,
though still a considerable amount of spurious ﬂuctuations
remains. These two images illustrate the discretisation-related
noise in traditional density estimators.
In contrast, the new Recursive-TCM method, does not
c⃝2013 RAS, MNRAS 000, 1–13


## Page 7


Noiseless Lensing Simulations
7
Figure 4. The convergence κ in the central 0.6 × 0.6h−1Mpc region about our WDM (top row) and CDM clusters (bottom row), using CiC,
Sph, or Recursive-TCM density estimates. The colour scale is identical for all six sub-images. Note the diﬀerent noise levels present in the
diﬀerent projection methods. Recursive-TCM displays the least noise.
present any appreciable noise thanks to the extra sophisti-
cation in the mass deposit, nor presents appreciable biases
thanks to the correction method described in Section 2.2. We
note that despite being much smoother, all those peaks seen
clearly in the CiC and Sph maps also appear in the Recursive-
TCM maps. It is important to note that our method is the only
one that could in principle distinguish random ﬂuctuations in
surface density maps from those produced by halo substruc-
tures: compare the diﬀerences between the CDM and WDM
halo in rightmost column, with the diﬀerences seen in the left-
most column. In both SPH and CiC it is almost impossible to
visually distinguish CDM from WDM.
Fig. 5 shows the power spectrum of the surface over-
density, δ = Σ/⟨Σ⟩−1, as given by the three projection
methods applied to the WDM halo. We note that the mea-
surements are robust only until k ∼0.4 × knyq, where knyq =
1000/(0.6h−1Mpc) × π = 5235h Mpc−1 denotes the Nyquist
frequency of the surface density mesh. On smaller scales, alias-
ing and the mass assignment window introduce visible arte-
facts, damping the measured power spectra. We also display
the expectations of a white-noise ﬁeld with the same num-
ber of point particles as those projected in our surface density
maps. For comparison, we also show the expectations for a
(cored) NFW halo with the same mass and concentration as
the spherically-averaged density proﬁle of our DM haloes, but
without noise.
Comparing all the measured power spectra, we observe a
situation consistent with the visual impression provided be-
fore. On large and intermediate scales, all methods provide
essentially identical power spectra decreasing as k−4, as ex-
pected for an NFW proﬁle. This incidentally supports the va-
lidity of our simple approach to correct the biases in Recursive-
TCM densities.
On scales smaller than k ≳20 h Mpc−1 or roughly r ∼
50 h−1kpc (k > 0.08 × knyq) – a scale much larger than the
typical size of substructures – all methods begin to diﬀer. The
CiC spectrum follows the value expected for a 2D Poisson ﬁeld:
Pnoise = n−1 = 2.3 × 10−7. Interestingly, the Sph method
levels to this expectation at roughly the same scale as the
CiC spectrum, but then decays much more quickly. This is
because the Sph method heavily smooths the ﬁeld on scales
smaller than the kernel size. This smoothing also erases true
(specially anisotropic) small-scale density ﬂuctuations present
in our DM haloes. For instance, it can be trivially seen that
structures resolved with less than 32 particles will be smoothed
out.
The performance of Recursive-TCM appears to be con-
siderably better. The noise level is a few orders of magnitude
below that of the other projection methods. The noise mea-
surements are consistent with our expectations of reducing the
noise in a way proportional to the maximum level of recursion,
lmax, in the adaptive mass deposit: Pnoise = n−1 × 6 × 2lmax,
where n is the number density of bodies used in the map cre-
ation. The prefactor of six is understood in terms of the six
times more particles (one per tetrahedron) employed to de-
scribe the mass ﬁeld. This scaling predicts the Poisson noise
in our measurements to be a factor of 6 × 210 = 6144 smaller
c⃝2013 RAS, MNRAS 000, 1–13


## Page 8


8
R. Angulo, R. Chen, S. Hilbert, T. Abel
Figure 5. The power spectra of the 2D over-density δ = Σ/⟨Σ⟩−1,
produced by the three projection algorithms when applied to a
WDM halo. Wavelengths are shown in units of the Nyquist fre-
quency of the density mesh knyq = 5235h Mpc−1. The method pro-
posed here, Recursive-TCM, yields the lowest amplitude on small-
scale ﬂuctuations. Also shown are expectations for a smooth NFW
proﬁle without and with central core. The dotted horizontal line
indicates the white-noise level.
than the CiC method. This value is very close to the actual
diﬀerences (measured at k = 0.27h Mpc−1): 7136.7.
Finally, we can see that Recursive-TCM creates a pro-
jected mass power spectrum that is very close to that of an
ideal NFW halo, diﬀering only on the slope at high wavenum-
bers. On these scales, the core introduced by the softening
length in our simulations becomes relevant, and the Recursive-
TCM power spectrum follows that of a cored NFW proﬁle.
4.2
Mass resolution dependence
We now explore how the noise of our convergence maps vary
with the mass resolution of the underlying N-body simulation.
For this, we have down-sampled the ﬁeld by factors of 2, 4 and
8 in each coordinate, or equivalently, reducing the total num-
ber of particles in our N-body simulations by factors of 8, 64,
and 512. The most down-sampled case is equivalent to a 1283
particle simulation, where our WDM halo would be resolved
with only 20000 particles. For each case, we have created con-
vergence maps with maximum recursion levels set at 2 for the
original maps, and to 5, 8 and 11, respectively for the down-
sampled versions. The increased recursion level compensates
the sparser particle data, so that in all four cases the maps
are created with roughly the same number of tetrahedra (i.e.
keeping n−1 × 2lmax constant).
In Fig. 6 we show the four resulting convergence maps.
In all sub-panels we see that our method produces extremely
smooth surface density maps. Naturally, as we decrease the
eﬀective resolution, small-scale features slowly disappear, for
instance, the three substructures located on the bottom-right
side of the image. With low mass resolution, orbits and accre-
Figure 6.
Comparison of the convergence maps created by the
same particle distribution of the WDM halo down-sampled by fac-
tors of 8 (top-right), 64 (bottom-left) or 512 (bottom-right). There-
fore, these would correspond to haloes simulated with 10243, 5123,
2563 and 1283, respectively, as indicated by the legend. The original
map is shown on the top-left panel. We use an identical logarithmic
colour scale in all subpanels.
tion become discrete and subtle radial features appear. How-
ever, even in the lower-right case, which contains almost 3
orders of magnitude less particles than in our original simu-
lation, the small-scale noise is considerably smaller than with
the CiC method (compare to the leftmost panel of the top row
in Fig. 4). This shows that the limitation of our maps is in the
actual amount of structure that the parent N-body simulation
tracks correctly, and not in the discreteness noise associated
with the ﬁnite number of particles.
A quantitative comparison can be obtained from Fig. 7,
which shows the 2D power spectra of our four test cases, with
and without applying our density correction (cf. Section 3.4).
The overall shape of the power spectra is very similar among
all resolutions, as expected from the previous images, but
small diﬀerences arise due to the diﬀerent amount of structure
resolved in the diﬀerent cases. Nevertheless, the discreteness
noise appears at the same level and is set by the maximum
amount of deposited tetrahedra. This again shows that the
limitation of our gravitational lensing simulations reside on
the ability of the parent N-body simulation to represent DM
structures properly, and not in an artiﬁcial noise introduced
by our mass-projection method. In the next subsection we will
show that this has positive repercussions on simulated lensing
signals.
4.3
The lensing magniﬁcation
The magniﬁcation ﬁeld, µ(x), which gives the ratio of the area
of the lensed image to the original area of the source, depends
on second-order derivatives of the lensing potential (whereas
α(x) depends only on ﬁrst-order derivatives). Thus, µ(x) is
very sensitive to small perturbations to the lensing potential
c⃝2013 RAS, MNRAS 000, 1–13


## Page 9


Noiseless Lensing Simulations
9
Figure 7.
Comparison between the power spectra of projected
overdensity maps created from the WDM halo with the Recursive-
TCM method applied on progressively sparser data. The solid red
line show the result for our original dataset and a maximum level of
recursion set to 4, whereas the dot-dashed magenta line shows the
result for a case using 512 less particles but allowing seven further
levels of reﬁnements.
(such as those caused by subhalos). This is also the reason why
µ(x) is very susceptible to noise introduced by discretisation
in N-body simulations.
In Fig. 8 we display maps of the inverse of the magniﬁ-
cation ﬁeld, µ−1(x), created from each of the three projection
methods we consider. We highlight two places i) where the
magniﬁcation is formally inﬁnite, µ−1 = 0, which are known
as critical lines; and ii) where µ−1 = 0.6, which are useful to
explore the impact of noise and substructures in the topology
of the magniﬁcation ﬁeld. Note that our simulated cluster is
not a particularly eﬃcient lens, partly due to its particular dy-
namical state, and also because of our modest force resolution
and the lack of a modelling of a central stellar component.
While the magniﬁcation maps from CiC, Sph, and
Recursive-TCM agree on large scales, they diﬀer substantially
in the amount of associated small-scale noise. In the CiC case,
the noise ﬂuctuations make it almost impossible to distinguish
CDM from WDM based solely on the topology of iso-µ lines.
The same is true to some degree in for Sph. The method
Recursive-TCM is superior: The contours are not disturbed
by discreteness noise. This allows us to explore the magniﬁca-
tion ﬁeld with great detail. When applied to the WDM case,
we see contour lines that are extremely smooth. For the CDM
halo, the contour lines are also very smooth in most parts of
the map, but display many small protuberances with high sig-
niﬁcance. As we will see in the next section, these are caused
by the rich substructure population of this halo and thus are
a distinctive signature of the DM candidate properties.
Figure 9 shows frequency of magniﬁcation values pre-
dicted by the diﬀerent methods for the WDM (results for the
CDM halo are very similar). The noise in the CiC magniﬁ-
cation maps leads to substantially broader magniﬁcation dis-
tributions compared to those for Sph and Recursive-TCM. In
contrast, the distributions predicted by Sph and Recursive-
TCM are very similar. However, the probability densities pre-
dicted by Sph display more features, i.e. local deviations from
a smooth density function, which we attribute to residual noise
in the Sph maps.
4.4
The impact of substructures
In order to further explore the capabilities of our method, we
now focus on the impact of halo substructure on the mag-
niﬁcation and convergence maps. In Fig. 10 we show iso-
magniﬁcation lines, as computed in Recursive-TCM maps, to-
gether with the substructures identiﬁed with more than 50
particles in our simulated halo. Note that the small amount
of noise visible in the outer contour is a result of the maxi-
mum number of recursion levels (lmax = 10) employed in our
method. This noise can also be seen in the power spectra of the
projected density ﬁeld shown in Fig. 5, and, as we discussed
earlier, it can be reduced further by simply increasing lmax at
the expense of more CPU time.
We can clearly see the diﬀerences between CDM and
WDM. In the WDM case, there are only 13 substructures
in the ﬁeld, and consequently iso-µ lines are mostly smooth,
showing only a few notorious protuberances. In contrast, in
the CDM case, there are 89 substructures, and the iso-µ lines
show many protuberances, but are almost smooth otherwise.
As Fig. 10 illustrates, all protuberances in the iso-
magniﬁcation contours are associated with nearby substruc-
tures. However, the relation is not simple, and diﬀerent
substructures produce perturbations of diﬀerent importance.
Moreover, in some cases ﬂuctuations are not caused by a single
substructure, but by a group of them. This case is seen, for
example, in the lower right section of the CDM µ−1 = 0.2. On
the contrary, some substructures near contours do not strongly
perturb the magniﬁcation ﬁeld. These objects have typically
surface mass densities below average. For instance, the sub-
structure located at (−0.04, 0.05) in the WDM case, has a
projected density a factor of ten smaller than the substruc-
ture found at (0.14, −0.2).
In Fig. 11 we compare the signal of identiﬁed substruc-
tures among the convergence maps. The x-axis shows the true
subhalo mass Msub. The y-axis shows the ratio of the excess
convergence ∆κ with respect to a simple expectation κsub
based on the substructure properties. The measured value,
∆κ, is deﬁned as κhm −κback, where κhm is the mean conver-
gence within the half-mass radius Rhm, and the background
convergence κback is the given by the mean convergence in
an annulus with 1.5Rhm < R < 1.7Rhm. The expected value,
κsub, is deﬁned as 0.5Msub/(πR2
hm)/Σc.
The deviations of ∆κ/κsub from unity seen in Fig. 11 can
be explained, e.g., by particle noise (though not for Recursive-
TCM), projections eﬀects, triaxiality, or inaccuracies in the
background estimation. Note that the scatter in ∆κ/κsub is
much lower in our method than in the other two. This is thanks
to a less noisy estimation of both the signal itself and the
background. However, the average value of ∆κ is roughly a
factor of two smaller in Recursive-TCM than in the other two
methods. The discrepancy is originated by two factors. First, it
is due to an overestimation of the bias correction factor: since
this factor is essentially set by the background halo, it does not
capture the exact density biases for substructures, which have
diﬀerent central densities and dynamical times. The second
c⃝2013 RAS, MNRAS 000, 1–13


## Page 10


10
R. Angulo, R. Chen, S. Hilbert, T. Abel
Figure 8.
Map of the inverse of the magniﬁcation ﬁeld, µ−1, at the central region of our WDM (top) and CDM (bottom). The region
displayed matches that shown in Fig. 4. White and black lines shows contours where µ−1 = 0.6 and 0, respectively. Note we use the same
colour scale in all panels, ranging from −0.18 (white) to 0.85 (light yellow).
CiC
Sph
Recursive-TCM
WDM
1.0
5.0
2.0
3.0
1.5
7.0
0.01
0.1
1
ÈΜÈ
pdfHÈΜÈL
Figure 9. Probability density pdf(|µ|) of the magniﬁcation mod-
ulus |µ| computed with CiC (red dotted), Sph (blue dashed), and
Recursive-TCM (black solid lines) for the WDM halo.
aspect is an intrinsic underestimation of the mass associated to
subhalos in Recursive-TCM. This has an origin in tetrahedra
being stretched along a subhalo’s orbit by tidal stripping. We
estimated this eﬀect to cause an underestimation of about
30% in the mass inside subhalos for resolved substructures
in our CDM halo. It remains to be explored whether more
sophisticated correction procedures, or modiﬁcations to the
Recursive-TCM algorithm, will alleviate these discrepancies.
In order to quantify the performance of Recursive-TCM
concerning substructure lensing signals, we have implemented
a hierarchical peak ﬁnder algorithm. This proceeds as follows:
We start by smoothing the convergence ﬁeld with a Gaussian
kernel of size rs = 100h−1kpc and then identify local peaks in
the smoothed ﬁeld. Then, we progressively reduce the kernel
size and search for new peaks, discarding those that are inside
a larger peak. We repeat this procedure for 20 diﬀerent scales,
uniformly spaced in log rs, down to rs = 1h−1kpc. Finally,
we compute the signal associated to each peak as ∆κ = κrs −
κback, where κrs is the average convergence within rs and κback
is the local background value deﬁned as the average of the map
in an annulus of 1.5rs < r < 1.7rs.
The results are shown in Fig. 12, which displays the cumu-
lative number of peaks detected by our algorithm when applied
to CiC, Sph and Recursive-TCM maps, as a function of their
local convergence excess ∆κ. In addition, we plot as a black
line the substructures detected in 3D by SUBFIND. The associ-
ated ∆κ is computed in the same way as that of our peaks, but
using Rhm as the peak scale. Our algorithm ﬁnds 4241 (CiC),
1116 (Sph) and 125 (Recursive-TCM) peaks in the CDM map,
and 4477 (CiC), 1356 (Sph) and 29 (Recursive-TCM), peaks
in the WDM map.
It is clear that the CiC and Sph maps contain a large
amount of spurious peaks produced by the discreteness noise.
At all ∆κ there are between one and two orders of magnitude
more detected peaks than real substructures. Moreover, the
number of detected peaks is almost identical between CDM
and WDM, even though the actual amount of substructure is
very diﬀerent. This further exempliﬁes that in current lensing
c⃝2013 RAS, MNRAS 000, 1–13


## Page 11


Noiseless Lensing Simulations
11
Figure 10. The relation between substructure and perturbations in lensing magniﬁcation for our simulated CDM (left) and WDM (right)
halo. Black lines denote iso-magniﬁcation contours at µ−1 = 0.8, 0.7, 0.6, 0.4, 0.2 and 0 inwards. Red circles indicate the positions where sub-
structures were identiﬁed, and their radii is equal to the half-mass radius of the respective subhalo. Note the reduced number of substructures
in the WDM case, which result from the initial suppression of small-scale ﬂuctuations.
Figure 11. Ratio of the measured excess convergence ∆κ of sub-
structures and a simple expectation κsub, as a function of the sub-
halo mass, Msub, in maps constructed using the CiC, Sph and
Recursive-TCM. Solid lines show the median values in seven log-
arithmic bins in Msub.
simulations the impact of noise is comparable or larger than
that of real DM substructures.
In contrast, our method recovers roughly the correct
amount of peaks, which is an order of magnitude larger in
CDM than in WDM. Furthermore, 59% and 69% of the sub-
Figure 12. The cumulative number of local peaks in convergence
maps detected in our WDM (top) and CDM (bottom) cluster-sized
halo. In each case we show the results for a map created using three
density projection methods: CiC (red lines), Sph (green line) and
Recursive-TCM blue line. In addition, we show the abundance of
substructures detected in 3D by the SUBFIND algorithm.
structures can be matched to a peak in CDM and WDM, re-
spectively. Among those substructures not detected as peaks,
we mostly ﬁnd objects with a negative or very small ∆κ value,
which are also not detected in the CiC or Sph. This suggests
c⃝2013 RAS, MNRAS 000, 1–13


## Page 12


12
R. Angulo, R. Chen, S. Hilbert, T. Abel
Figure 13.
Zoom into a 100 × 100h−1kpc region, centred at
(∆x, ∆y) = (−0.23, −0.11)h−1Mpc relative to the main halo, show-
ing the convergence ﬁeld associated to a tidal feature. The left panel
shows a map computed using a Recursive-TCM projection method,
whereas the right panels shows one computed using the Sph method.
that these might indeed be the false-positives in SUBFIND or
special cases of projection eﬀects. However, it might also be
a consequence of the simplicity of our peak detection algo-
rithm. In order to quantify the implications for observational
constraints, this issue requires further study considering real-
istic input signals and analysis procedures, and perhaps more
sophisticated procedures to correct for Recursive-TCM biases.
There are also peaks in the convergence maps that are not
related to any identiﬁed 3D substructure. In many cases, these
are due our 3D substructure ﬁnder algorithm: a density peak
not found by SUBFIND, one that fell below our mass-resolution,
or one that is not a self-bound object. For instance, the large
peak located at (−0.27, −0.28). An object of a diﬀerent na-
ture is shown in Fig. 13. It does not correspond to a self-
bound spherical overdensity, but to a DM stream of a tidally
disrupted substructure. Such features are expected in hierar-
chical structure formation scenarios, and perhaps they could
be eventually detected trough their lensing signal. (Note that
this feature is barely distinguished over the noise in Sph). For
the moment, this detection serves as a further example of the
potential accuracy and precision of the lensing maps created
by the method presented and discussed here.
5
CONCLUSIONS
The next generation of gravitational lensing observations
might help us to decipher the mysteries of the Dark Universe:
Dark Energy and Dark Matter. However, high-precision theo-
retical predictions are essential to ensure the correct interpre-
tation of future datasets.
We presented Recursive-TCM, a method aimed at pre-
dicting the lensing signal from cosmological simulations with
the required accuracy. This algorithm originates from a novel
way of interpreting the results of N-body simulations and over-
comes one of the most serious limitations of current lensing
simulations: the noise introduced by the discrete nature of the
particle representation of the density ﬁeld.
We applied Recursive-TCM to cluster sized-haloes sim-
ulated in WDM and CDM universes. We showed that the
method produces convergence maps with noise several orders
of magnitude below that of traditional methods (here, a factor
of ∼7000 smaller than the formal shot-noise limit), and that
it recovers the underlying power spectrum of ﬂuctuations well
below the particle shot noise of the simulations.
With traditional projection methods, the discreteness
noise in lensing maps are comparable to the signal from DM
substructure. This is not true for Recursive-TCM, where the
features associated with real overdensities are preserved, but
the discreteness noise is absent. All this comes without free pa-
rameters or additional smoothing scales. We also showed that
there are density biases associated to Recursive-TCM, which,
however, can be mostly eliminated by simple correction proce-
dures. Therefore, this method is well suited for creating high-
precision predictions for the relation between the underlying
cosmological model and the expected signatures of small-cale
structure in strong gravitational lensing observations.
With Recursive-TCM, we were able to clearly show the
diﬀerences in the lensing properties between CDM and WDM.
The diﬀerences come mainly from their substructure popu-
lation, and thus lensing might be able to constrain the DM
particle mass. However, we found that the relation between
substructures and the associated lensing eﬀects is not trivial:
some substructures do not aﬀect the convergence noticeably;
many lensing perturbations are caused by more than a single
structure; and a few perturbations are not associated with any
self-bound substructure, but, e.g. with tidal debris. This sug-
gests that in order to interpret correctly the lensing measure-
ments of substructures, a rigorous study of the detectability
of substructures needs to be carried out.
In this paper, we have shown the feasibility of our method,
providing examples of its potential when applied to a rather
modest simulation. In the future, we expect our method to
enable many detailed theoretical studies, exploiting state-of-
the-art simulations of much higher force and mass resolu-
tion, also simulating more realistic WDM scenarios, and even
taking advantage of hydrodynamical simulations. The pre-
sented method will also be very useful for creating large-scale
weak lensing shear and magniﬁcation maps with high ﬁdelity
and low particle noise. Moreover, the method will be crucial
for testing and characterising the performance of algorithms
of extracting substructure information from observed lensed
galaxies, in particular methods for constraining the DM par-
ticle mass from image perturbations or ﬂux-ratio anomalies
in multiple-image systems. All this together will allow us to
understand better the impact of the underlying cosmological
model in lensing observations, and therefore help to unleash
the full potential of gravitational lensing.
ACKNOWLEDGEMENTS
We warmly thank Oliver Hahn and Ralf Kaehler for many en-
lightening discussions. We also thank Simon White for valu-
able suggestions that improved our paper. We acknowledge
useful comments on the manuscript from Carlo Giocoli, Yashar
Hezaveh, Phil Marshal, Ben Metcalf, Stefan Rau and Simona
Vegetti. T.A. gratefully acknowledges support by the National
Science foundation through award number AST-0808398 and
the LDRD program at the SLAC National Accelerator Labora-
tory as well as the Terman Fellowship at Stanford University.
We gratefully acknowledge the support of Stuart Marshall and
the SLAC computational team, as well as the computational
resources at SLAC. Parts of the computations were carried out
at the Rechenzentrum Garching (RZG) of the Max Planck So-
ciety.
c⃝2013 RAS, MNRAS 000, 1–13


## Page 13


Noiseless Lensing Simulations
13
REFERENCES
Abel T., Hahn O., Kaehler R., 2012, MNRAS, 427, 61
Angulo R. E., Baugh C. M., Lacey C. G., 2008, MNRAS,
387, 921
Angulo R. E., Hahn O., Abel T., 2013, arXiv:1304.2406
Angulo R. E., Springel V., White S. D. M., Jenkins A., Baugh
C. M., Frenk C. S., 2012, MNRAS, 426, 2046
Aubert D., Amara A., Metcalf R. B., 2007, MNRAS, 376,
113
Bartelmann M., 2010, Classical and Quantum Gravity, 27,
233001
Bartelmann M., Huss A., Colberg J. M., Jenkins A., Pearce
F. R., 1998, A&A, 330, 1
Bartelmann M., Schneider P., 2001, Phys. Rep., 340, 291
Bradaˇc M., Schneider P., Lombardi M., Steinmetz M., Koop-
mans L. V. E., Navarro J. F., 2004, A&A, 423, 797
Couchman H. M. P., Barber A. J., Thomas P. A., 1999, MN-
RAS, 308, 180
Dalal N., Kochanek C. S., 2002, ApJ, 572, 25
Davis M., Efstathiou G., Frenk C. S., White S. D. M., 1985,
ApJ, 292, 371
Diemand J., Kuhlen M., Madau P., 2007, ApJ, 667, 859
Efstathiou G., Davis M., White S. D. M., Frenk C. S., 1985,
ApJS, 57, 241
Efstathiou G., Eastwood J. W., 1981, MNRAS, 194, 503
Fontanot F., Puchwein E., Springel V., Bianchi D., 2013,
arXiv:1307.5065
Fontanot F., Springel V., Angulo R. E., Henriques B., 2012,
MNRAS, 426, 2335
Gao L., Navarro J. F., Frenk C. S., Jenkins A., Springel V.,
White S. D. M., 2012, MNRAS, 425, 2169
Giannantonio T., Porciani C., Carron J., Amara A., Pillepich
A., 2012, MNRAS, 422, 2854
Hahn O., Abel T., 2011, MNRAS, 415, 2101
Hahn O., Abel T., Kaehler R., 2013, MNRAS
Hilbert S., Hartlap J., White S. D. M., Schneider P., 2009,
A&A, 499, 31
Hilbert S., Marian L., Smith R. E., Desjacques V., 2012, MN-
RAS, 426, 2870
Hockney R. W., Eastwood J. W., 1981, Computer Simulation
Using Particles. Computer Simulation Using Particles, New
York: McGraw-Hill, 1981
Huterer D., 2010, General Relativity and Gravitation, 42,
2177
Jain B., Seljak U., White S., 2000, ApJ, 530, 547
Kaehler R., Hahn O., Abel T., 2012, arXiv:1208.3206
Klypin A., Kravtsov A. V., Valenzuela O., Prada F., 1999,
ApJ, 522, 82
Kochanek C. S., Dalal N., 2004, ApJ, 610, 69
Komatsu E. et al., 2011, ApJS, 192, 18
Kuhlen M., Vogelsberger M., Angulo R., 2012, Physics of the
Dark Universe, 1, 50
Li G.-L., Mao S., Jing Y. P., Kang X., Bartelmann M., 2006,
ApJ, 652, 43
Mao S., Schneider P., 1998, MNRAS, 295, 587
Marian L., Hilbert S., Smith R. E., Schneider P., Desjacques
V., 2011, ApJ, 728, L13
Meneghetti M., Argazzi R., Pace F., Moscardini L., Dolag
K., Bartelmann M., Li G., Oguri M., 2007, A&A, 461, 25
Meneghetti M., Yoshida N., Bartelmann M., Moscardini L.,
Springel V., Tormen G., White S. D. M., 2001, MNRAS,
325, 435
Metcalf R. B., Madau P., 2001, ApJ, 563, 9
Monaghan J. J., 1992, ARA&A, 30, 543
Moore B., Ghigna S., Governato F., Lake G., Quinn T.,
Stadel J., Tozzi P., 1999, ApJ, 524, L19
Natarajan P., De Lucia G., Springel V., 2007, MNRAS, 376,
180
Natarajan P., Springel V., 2004, ApJ, 617, L13
Navarro J. F., Frenk C. S., White S. D. M., 1996, ApJ, 462,
563
Navarro J. F., Frenk C. S., White S. D. M., 1997, ApJ, 490,
493
Oguri M., Takada M., 2011, Phys. Rev. D, 83, 023008
Overzier R., Lemson G., Angulo R. E., Bertin E., Blaizot J.,
Henriques B. M. B., Marleau G.-D., White S. D. M., 2013,
MNRAS, 428, 778
Pandey B., White S. D. M., Springel V., Angulo R., 2013,
arXiv:1301.3789
Peebles P. J. E., 1971, A&A, 11, 377
Peter A. H. G., Rocha M., Bullock J. S., Kaplinghat M.,
2013, MNRAS, 430, 105
Rau S., Vegetti S., White S. D. M., 2013, MNRAS, 430, 2232
Sato M., Hamana T., Takahashi R., Takada M., Yoshida N.,
Matsubara T., Sugiyama N., 2009, ApJ, 701, 945
Schaap W. E., van de Weygaert R., 2000, A&A, 363, L29
Shandarin S., Habib S., Heitmann K., 2012, Phys. Rev. D,
85, 083005
Springel V. et al., 2008, MNRAS, 391, 1685
Springel V. et al., 2005, Nature, 435, 629
Springel V., Yoshida N., White S. D. M., 2001, New Astron-
omy, 6, 79
Takahashi R., Oguri M., Sato M., Hamana T., 2011, ApJ,
742, 15
Vale C., White M., 2003, ApJ, 592, 699
Vegetti S., Koopmans L. V. E., Bolton A., Treu T., Gavazzi
R., 2010, MNRAS, 408, 1969
Vegetti S., Lagattuta D. J., McKean J. P., Auger M. W.,
Fassnacht C. D., Koopmans L. V. E., 2012, Nature, 481,
341
Viel M., Becker G. D., Bolton J. S., Haehnelt M. G., 2013,
Phys. Rev. D, 88, 043502
Wambsganss J., Cen R., Ostriker J. P., 1998, ApJ, 494, 29
Wang H. Y., Mo H. J., Jing Y. P., 2007, MNRAS, 375, 633
Xu D. D. et al., 2009, MNRAS, 398, 1235
c⃝2013 RAS, MNRAS 000, 1–13

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1309_1161v2_noiseless_gravitational_lensing_simulations
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2013/1309_1161V2_NOISELESS_GRAVITATIONAL_LENSING_SIMULATIONS.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
canon-group: reference
rscf-state: source-claim
arxiv_id: 906.2955
source: arxiv
tags: [arxiv, knowledge, math, quantum, reference]
---
# 0906.2955_Dark_Energy_Survey_Supernovae__Simulations_and_Survey_Strategy

> Source: 0906.2955_Dark_Energy_Survey_Supernovae__Simulations_and_Survey_Strategy.pdf

> Pages: 4

---


## Page 1


arXiv:0906.2955v1  [astro-ph.CO]  16 Jun 2009
Dark Energy Survey Supernovae: Simulations and Survey Strategy
J. P. Bernstein
Argonne National Laboratory, HEP Division, Argonne, IL 60439
R. Kessler
University of Chicago, KICP, Chicago, IL 60637
S. Kuhlmann and H. Spinka
Argonne National Laboratory, HEP Division, Argonne, IL 60439
For the Dark Energy Survey Collaboration
We present simulations for the Dark Energy Survey (DES) using a new code suite (SNANA)
that generates realistic supernova light curves accounting for atmospheric seeing conditions
and intrinsic supernova luminosity variations using MLCS2k2 or SALT2 models. Errors in-
clude stat-noise from photo-statistics and sky noise. We applied SNANA to simulate DES
supernova observations and employed an MLCS-based ﬁtter to obtain the distance modulus
for each simulated light curve. We harnessed the light curves in order to study selection biases
for high-redshift supernovae and to constrain the optimal DES observing strategy using the
Dark Energy Task Force ﬁgure of merit.
1
Introduction
The Dark Energy Survey (DES) is on track for ﬁrst light in 2011 and will carry out a deep
optical and near-infrared survey of 5000 square degrees of the South Galactic Cap to ∼24th
magnitude using a new 3 square-degree CCD camera (called DECam) to be mounted on the
Blanco 4-meter telescope at CTIO. DES uses thicker CCDs from Lawrence Berkeley National
Laboratory with greater red sensitivity as compared to previous surveys. In exchange for the
camera, CTIO will provide DES with 525 nights on the Blanco spread over 5 years. The survey
data will allow the measurement of the dark energy and dark matter densities and the dark
energy equation of state through four independent methods: galaxy clusters, weak gravitational
lensing tomography, galaxy angular clustering, and supernova (SN) distances. While the logistics
of the SNe survey are still being ﬁnalized, time allocation within the larger survey will be ∼1000
hrs (yet to be ﬁnalized) with maximal use of non-photometric time (up to 500 hrs). Likewise,
the spectroscopic follow-up strategy is still being ﬂeshed out. The working estimate is currently
25% with the remaining redshifts to be obtained via host-galaxy follow-up.
The DES SN working group has undertaken simulations of DES observations with the goal of
constraining the optimal SN survey strategy. Toward this end, we apply the SN simulation pack-
age (SNANA) developed by Kessler for the SDSS-II SN Survey and later modiﬁed for non-SDSS
surveys. SNANA generates realistic light curves accounting for atmospheric seeing conditions,
host-galaxy extinction, cadence, and intrinsic SN luminosity variations using MLCS2k2 (Jha et
al. 2007 [1]) or SALT2 (Guy et al. 2007 [2]) models. The simulation errors include stat-noise


## Page 2


DES_v11_103_1  SN 40039   z=0.2731   grizY-band
0
100
200
g
AV = 0.457 ± 0.039      ∆ = -0.161 ± 0.023
µ = 40.704 ± 0.044      χ2/dof = 0.3/0.400116
0
100
200
300
r
0
100
200
300
i
0
100
200
0
50
100
z
Tobs - 53366
Flux
0
50
100
150
200
0
50
100
Y
Tobs - 53366
Flux
(a) An SNANA light curve for redshift z∼0.27.
DES_v11_103_1  SN 40027   z=0.7467   grizY-band
-1
-0.5
0
0.5
1
g
AV = 0.028 ± 0.029      ∆ = -0.245 ± 0.038
µ = 43.525 ± 0.051      χ2/dof = -0.1/-0.215728
0
20
40
r
0
20
40
60
i
0
20
40
60
0
50
100
z
Tobs - 53308.9
Flux
0
20
40
60
0
50
100
Y
Tobs - 53308.9
Flux
(b) An SNANA light curve for redshift z∼0.75.
Figure 1: Plotted is ﬂux vs. time in days. Points are the simulated data, the blue dashed
line is with no extinction or ﬂuctuations, and the solid and dashed green lines are the best
realistic ﬁt and error bounds. The “red bump” at ∼40 days is characteristic of SNe Ia, is
clearly evident in the Y band for z∼0.27, and fades for z∼0.75.
from photo-statistics and sky noise. The package includes a light-curve ﬁtter that shares many
software tools, uses the MLCS2k2 model, with improvements, and ﬁts in ﬂux rather than mag-
nitudes. In this paper, we present light curve simulations for DES and describe a high-redshift
bias that arises when selection eﬀects are not accounted for in the analysis.
2
The SNANA Package
SNANA uses a mixture of C and FORTRAN routines to simulate and ﬁt SN light curves for a
range of redshifts (z). SNANA generates ﬁtted distance moduli, µ, and passes µ–z pairs to a
cosmology ﬁtter. It is publicly available a and requires CFITSIO and CERNLIB. The simulation
is designed to be fast, generating a few dozen light curves per second, while still providing
accurate and realistic SN light curves. Using the package requires the generation of a survey
library that includes the survey characteristics (e.g., the observing cadence, seeing conditions,
and CCD properties). Generating this library is easy post-survey; predicting it before the survey
is crucial to making realistic predictions for the light-curve quality. The light curve ﬁtter takes
longer to run, up to many hours depending on the number of SNe and number of ﬁt parameters.
3
Simulations
For the simulations presented here, we employed the MLCS2k2 model as the basis for generating
and ﬁtting SNe light curves. The free parameters are the epoch of maximum light in the B-
band (to), the distance modulus (µ), the luminosity/light curve shape parameter (∆), and the
extinction in magnitudes by dust in the host galaxy (parameterized by AV and RV from Cardelli
ahttp://www.hep.anl.gov/des/snana package


## Page 3


Wavelength (nm)
400
500
600
700
800
900
1000
Transmission or QE
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
g
r
i
z
Y
QE
Wavelength (nm)
400
500
600
700
800
900
1000
g
r
i
1
Z
Y
QE
Wavelength (nm)
400
500
600
700
800
900
1000
g
r
i
2
Z
Y
QE
Figure 2: The choice of DES z ﬁlters plotted with the DES quantum eﬃciency.
et al. 1989 [3]). Note that for this work we ﬁxed RV = 3.1 (the average for the Milky Way) but
will explore ﬁtting RV in the near future. Fig. 1 shows example light curves.
The DES supernova working group has begun optimizing DES SN survey strategy by ex-
ploring the 1) choice of z-like ﬁlter and 2) the survey depth. Under consideration are the griz,
griZ1Y, and griZ2Y ﬁlter sets (see Fig. 2). The griz ﬁlters are SDSS-like and the Y ﬁlter oc-
cupies the clean wavelength range between the atmospheric absorption bands at 0.95µm and
1.14µm. Z1 avoids the overlap with Y and Z2 avoids the Y overlap and the lower atmospheric
absorption feature. Also under consideration are 3, 9, and 27 square-degree ﬁelds corresponding
to “ultra-deep” (but narrow = 1 DES ﬁeld), “deep”, and “wide” (but shallow) surveys. Results
to date show that the survey depth has a much greater eﬀect than does the choice of z-like ﬁlter.
Therefore, we henceforth show examples using the z ﬁlter. Fig. 3 shows our DES light curve ﬁts.
4
Discussion
Fig. 3 shows a µ bias manifest in the diﬀerence between ﬁtted and simulated µ beyond z∼0.6.
The bias arises from not accounting for selection eﬃciencies and illustrates the magnitude of the
µ-correction that will be needed. The fact that AV trends to zero beyond z∼0.6 is consistent
with a selection bias as we interpret that to mean that only less extincted SNe can pass the cuts
as redshift increases. Fig. 3 also shows that the deep survey oﬀers a substantial improvement
in statistics relative to the ultra-deep survey while avoiding a signiﬁcant portion of the bias
suﬀered by the wide survey. Thus, we will move forward in constraining DES SN strategy by
considering both a deep survey and a hybrid approach with a mixture deep and wide ﬁelds.
Calculations made for the DES project proposal estimated that the survey would oﬀer an
improvement in the the Dark Energy Task Force ﬁgure of merit (fom) by a factor of 4.6 relative
to current SN surveys. The DES SN working group has implemented a cosmology ﬁtter in order
to obtain a more robust calculation of the fom for DES by harnessing SNANA simulated SN
surveys.
We currently have statistics-only fom estimates and are working on furthering our
SNANA analysis to account for estimates of DES SN systematics. Once completed, we will use
SNANA to constrain the optimal DES SN survey strategy and produce a detailed white paper.
References
1. S. Jha, A. G. Riess, R. P. Kirshner, ApJ 659, 122 (2007).
2. J. Guy et al, A&A 466, 11 (2007).
3. J. A. Cardelli, G. .C. Clayton, J. .S. Mathis, ApJ 345, 245 (1989).


## Page 4


Redshift
0
0.2
0.4
0.6
0.8
1
1.2
1.4
# post-cut SNe
0
100
200
300
400
500
600
700
800
900
Ultra-deep
Deep
Wide
1143 SNe  (2282 sim)
2590 SNe  (6782 sim)
5023 SNe (14450 sim)
Redshift
0
0.2
0.4
0.6
0.8
1
1.2
1.4
µ
 - True 
µ
Observed 
-0.3
-0.25
-0.2
-0.15
-0.1
-0.05
0
0.05
0.1
0.15
Ultra-deep (3 sq deg)
Deep          (9 sq deg)
Wide          (27 sq deg)
Redshift
0
0.2
0.4
0.6
0.8
1
1.2
1.4
µ
Average 
37
38
39
40
41
42
43
44
45
46
Fitted (ultra-deep)
Fitted (deep)
Fitted (wide)
Redshift
0
0.2
0.4
0.6
0.8
1
1.2
1.4
V
Average A
-0.3
-0.2
-0.1
0
0.1
0.2
0.3
0.4
0.5
0.6
Simulated (ultra-deep)
Simulated (deep)
Simulated (wide)
Redshift
0
0.2
0.4
0.6
0.8
1
1.2
1.4
/Sqrt(N)
µ
σ
0
0.005
0.01
0.015
0.02
0.025
0.03
0.035
Ultra-deep
Deep
Wide
Redshift
0
0.2
0.4
0.6
0.8
1
1.2
1.4
∆
Average 
-0.3
-0.2
-0.1
0
0.1
0.2
0.3
0.4
0.5
0.6
Simulated (ultra-deep)
Simulated (deep)
Simulated (wide)
Figure 3: Left: Number of SNe and the Hubble diagram (grizY ﬁlter set). Right: The redshift
run of the diﬀerence in ﬁtted (“observed”) and simulated (“true”) distance modulus (µ), host
extinction parameter (AV), and MLCS luminosity/shape parameter (∆). Both: cuts were ap-
plied by the ﬁtter such that each SN had at least 5 measurements and one ﬁlter measurement
with a signal to noise above 10 and any 3 ﬁlters above 5. Note that the large error bars and
deviations at the lowest (z<0.1) and highest (z>1.2) redshifts are due to low statistics.

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: 0906_2955_dark_energy_survey_supernovae_simulations_and_survey_strategy
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2009/0906_2955_DARK_ENERGY_SURVEY_SUPERNOVAE_SIMULATIONS_AND_SURVEY_STRATEGY.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

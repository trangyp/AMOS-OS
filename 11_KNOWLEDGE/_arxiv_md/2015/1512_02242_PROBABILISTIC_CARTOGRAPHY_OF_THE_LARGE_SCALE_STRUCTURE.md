---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1512.02242
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1512.02242_Probabilistic_cartography_of_the_large-scale_structure

> Source: 1512.02242_Probabilistic_cartography_of_the_large-scale_structure.pdf

> Pages: 4

---


## Page 1


Probabilistic cartography of the large-scale structure
Florent Leclercq,1, 2, 3, 4, a) Jens Jasche,5 Guilhem Lavaux,2, 3 and Benjamin Wandelt2, 3, 6, 7
1)Institute of Cosmology and Gravitation, University of Portsmouth,
Dennis Sciama Building, Burnaby Road, Portsmouth, PO1 3FX, United Kingdom
2)Institut d’Astrophysique de Paris (IAP), UMR 7095, CNRS – UPMC Universit´e Paris 6, Sorbonne Universit´es,
98bis boulevard Arago, F-75014 Paris, France
3)Institut Lagrange de Paris (ILP), Sorbonne Universit´es,
98bis boulevard Arago, F-75014 Paris, France
4) ´Ecole polytechnique ParisTech,
Route de Saclay, F-91128 Palaiseau, France
5)Excellence Cluster Universe, Technische Universit¨at M¨unchen,
Boltzmannstrasse 2, D-85748 Garching, Germany
6)Department of Physics, University of Illinois at Urbana-Champaign,
1110 West Green Street, Urbana, IL 61801, USA
7)Department of Astronomy, University of Illinois at Urbana-Champaign,
1002 West Green Street, Urbana, IL 61801, USA
(Dated: 20 August 2018)
The borg algorithm is an inference engine that derives the initial conditions given a cosmological model
and galaxy survey data, and produces physical reconstructions of the underlying large-scale structure by
assimilating the data into the model.
We present the application of borg to real galaxy catalogs and
describe the primordial and late-time large-scale structure in the considered volumes. We then show how
these results can be used for building various probabilistic maps of the large-scale structure, with rigorous
propagation of uncertainties. In particular, we study dynamic cosmic web elements and secondary eﬀects in
the cosmic microwave background.
I.
BAYESIAN LARGE-SCALE STRUCTURE INFERENCE
WITH BORG
Over the last few years, several models and software
packages aiming at full analysis of the three-dimensional
cosmological matter distribution have met some success.
Among them, borg (Bayesian Origin Reconstruction
from Galaxies, Jasche & Wandelt, 2013) is a full-scale
Bayesian inference framework for analyzing the linear
and mildly non-linear large-scale structure.
Contrary to previous approaches, which relied on phe-
nomenological density models, borg involves an addi-
tional layer of complexity by running several numerical
simulations of structure formation for each move in a
huge parameter space, comprising of the order of 107 pa-
rameters (the voxels of the discretized domain). In this
fashion, the data model jointly accounts for the shape of
three-dimensional matter ﬁeld and its formation history.
To allow feasible numerical analyses, borg relies on the
Hamiltonian Monte Carlo algorithm. The (approximate)
physical model for gravitational dynamics is second-order
Lagrangian perturbation theory (2LPT), linking initial
density ﬁelds (at a scale factor a = 10−3) to the presently
observed large-scale structure (at a = 1). The galaxy dis-
tribution is modeled as an inhomogeneous Poisson pro-
cess on top of evolved density ﬁelds. In its latest version,
borg also accounts for luminosity dependent galaxy bi-
ases and performs automatic calibration of correspond-
ing noise levels (Jasche, Leclercq & Wandelt, 2015). For
a)Electronic mail: ﬂorent.leclercq@polytechnique.org
a more extensive discussion of the borg data model, the
reader is referred to chapter 4 in Leclercq (2015).
Over the last two years, Bayesian large-scale struc-
ture inference with borg has moved beyond the proof-of-
concept stage, to routine application to real data such as
the Sloan Digital Sky Survey (SDSS) main galaxy sample
(Abazajian et al., 2009) and the 2M++ catalog (Lavaux
& Hudson, 2011): see Jasche, Leclercq & Wandelt (2015);
Lavaux & Jasche (2016).
In ﬁgure 1, we illustrate the results of Bayesian large-
scale structure inference with borg. The two leftmost
panels show slices through the reconstructed density in
one sample, in the initial conditions (at a = 10−3) and in
the corresponding ﬁnal conditions (at a = 1). The SDSS
galaxies are overplotted as red dots.
In our Bayesian
framework, each of the constrained samples is a full-scale
realization of the physical model (2LPT), and the vari-
ation between samples quantiﬁes uncertainties.
In the
two rightmost panels, we show the ensemble mean among
all the samples obtained in our analysis, which approxi-
mates the posterior mean, for initial and ﬁnal conditions.
The mean density ﬁeld exhibits a high degree of detail
where data constraints are available, but approaches cos-
mic mean density in unobserved regions (at high redshift
or out of the survey boundaries).
Beyond density reconstruction, Bayesian large-scale
structure inference with borg yields a rich variety of
scientiﬁc products. In the following, we illustrate with
two examples: cosmic web classiﬁcation and production
of templates for secondary eﬀects expected in the cos-
mic microwave background (CMB). A particular advan-
tage of this approach is that it automatically and self-
arXiv:1512.02242v1  [astro-ph.CO]  7 Dec 2015


## Page 2


2
0
100
200
300
400
500
z [Mpc/h]
500
400
300
200
100
0
−x [Mpc/h]
initial conditions
in one sample
-0.012 -0.006
0.0
0.006 0.012
δ
0
100
200
300
400
500
z [Mpc/h]
500
400
300
200
100
0
ﬁnal conditions
in one sample
0.0 0.4 0.8 1.2 1.6 2.0 2.4 2.8 3.2 3.6
ln(2 + δ)
0
100
200
300
400
500
z [Mpc/h]
500
400
300
200
100
0
posterior mean
(initial conditions)
-0.008
-0.004
0.0
0.004
0.008
δ
0
100
200
300
400
500
z [Mpc/h]
500
400
300
200
100
0
posterior mean
(ﬁnal conditions)
0.4 0.8 1.2 1.6 2.0 2.4 2.8 3.2
ln(2 + δ)
FIG. 1. Bayesian large-scale structure inference with borg in the SDSS main galaxy sample. Leftmost panels: slices through
one sample of the posterior for the initial and ﬁnal density ﬁelds. Rightmost panels: posterior mean in the initial and ﬁnal
conditions. The input galaxies are overplotted on the ﬁnal conditions as red dots.
0
100
200
300
400
500
z [Mpc/h]
500
400
300
200
100
0
−x [Mpc/h]
T-web
0
100
200
300
400
500
z [Mpc/h]
500
400
300
200
100
0
diva
0
100
200
300
400
500
z [Mpc/h]
500
400
300
200
100
0
origami
0.0
0.2
0.4
0.6
0.8
1.0
FIG. 2. Comparison of cosmic web classiﬁcation procedures in the SDSS volume. The panels show slices through the posterior
probability for voxels to belong to a void, as deﬁned by the T-web (left panel), by diva (middle panel) and by origami (right
panel).
consistently propagates observational uncertainties from
the inferred density to other physical quantities.
II.
COSMIC WEB CLASSIFICATION
As demonstrated in Leclercq,
Jasche & Wandelt
(2015b) for the SDSS, borg inference results can be used
as inputs for a detailed cosmic-web type analysis. The
large-scale structure is dissected and classiﬁed in terms
voids, sheets, ﬁlaments, and clusters. The resulting cos-
mic web maps are fully probabilistic: in each voxel, four
probabilities (summing up to unity) for each of the struc-
ture types are obtained.
In Leclercq, Jasche & Wandelt (2015b), the classiﬁ-
cation procedure adopted is the so-called T-web algo-
rithm (Hahn et al., 2007), which consists in looking at
the eigenvalues of the tidal tensor ﬁeld.
The number
of positive (resp.
negative) eigenvalues corresponds to
the number of axes along which gravitational collapse
(resp. expansion) occurs, which naturally classiﬁes the
environment into clusters, sheets, ﬁlaments and voids.
As the tidal tensor is directly derived from the density
ﬁeld, the T-web can be applied to ﬁnal conditions re-
constructed with any data model (see Jasche et al., 2010,
for an earlier application of the T-web to density ﬁelds
reconstructed using a log-normal density model). How-
ever, borg allows a chrono-cosmographic description of
the dynamic cosmic web, in the sense that it also in-
fers proto-structures present in the initial conditions and
their time evolution.
Further, the inference of the initial density ﬁeld by
borg now allows a description of the cosmic web in real
data using “Lagrangian classiﬁers” (Leclercq et al., in


## Page 3


3
iSW
iSWRS
RS
kSZ
FIG. 3. Templates for CMB secondary eﬀects. The four panels correspond to, respectively: iSW (using the linear gravitational
potential), iSWRS (using the fully non-linear gravitational potential), RS (obtained by subtracting the previous maps, i.e.
iSWRS−iSW) and kSZ.
prep a), i.e. algorithms that necessitate the initial posi-
tions of particles. Among them, diva (Lavaux & Wan-
delt, 2010) uses the eigenvalues of the Lagrangian dis-
placement ﬁeld, and origami (Falck, Neyrinck & Sza-
lay, 2012) counts the number of shell-crossings. This new
possibility oﬀered by physical large-scale structure infer-
ence is of special interest, because the use of Lagrangian
classiﬁers has so far been limited to simulations.
In ﬁgure 2, we compare probabilistic maps of the SDSS
volume for voids, as deﬁned by the T-web (left panel, re-
produced from Leclercq, Jasche & Wandelt, 2015b), by
diva (middle panel, reproduced from Leclercq et al., in
prep a) and by origami (right panel, reproduced from
Leclercq et al., in prep a). The T-web and diva maps
are visually similar, with an overall smoother structure
for the voids deﬁned by diva, which are sharply sepa-
rated by sheets and ﬁlaments. In contrast, with origami,
most of the volume is ﬁlled by voids (this is also true for
the prior) and more complex, shell-crossed structures are
rarely identiﬁed.
These developments naturally bring in a connection
between cosmic web analysis and information theory. In
Leclercq, Jasche & Wandelt (2015b), we examine the
Shannon entropy of the structure-type posterior prob-
ability distribution and quantify the information gain
due to SDSS galaxies. In Leclercq, Jasche & Wandelt
(2015a), we propose a decision criterion for classifying
structures in the presence of uncertainty. The resulting
decision-making procedure balances the posterior prob-
abilities and the strength of data constraints.
Finally,
in Leclercq et al. (in prep b), we extend the problem to
the space of classiﬁers, and introduce utility functions for
the optimal choice of a classiﬁer, speciﬁc to the applica-
tion of interest.
III.
SECONDARY EFFECTS IN THE COSMIC
MICROWAVE BACKGROUND
Beyond analyses of the large-scale structure as probed
by galaxies, borg inference results can be used to pro-
duce templates for secondary eﬀects expected in the
CMB: the kinetic Sunyaev-Zel’dovich (kSZ) eﬀect, the
integrated Sachs-Wolfe (iSW) and Rees-Sciama (RS) ef-
fects. The cross-correlation of such templates with CMB
maps, for example via a matched-ﬁlter approach (Li
et al., 2014), can then enhance the detectability of these
eﬀects.


## Page 4


4
Starting from initial conditions produced by the borg
2M++ analysis (Lavaux & Jasche, 2016), we generate a
large ensemble of constrained simulations using the fast
cola model (Tassev, Zaldarriaga & Eisenstein, 2013).
These simulations describe complex non-linear dynamics
in the nearby Universe, which imprints eﬀects on CMB
photons: the momentum ﬁeld of electrons (approximated
to the momentum ﬁeld of the matter ﬁeld), resulting in
the kSZ eﬀect; and the time evolution of the gravita-
tional potential (linear and non-linear), resulting in the
iSW and iSWRS eﬀects.
We use the kSZ data model
presented in Lavaux, Afshordi & Hudson (2013), and the
iSW/iSWRS models as well as the ray-tracing algorithm
presented in Cai et al. (2010). In Lavaux, Leclercq &
Jasche (in prep), we present the resulting templates and
show that better physical modeling, as made possible by
borg, yields higher signal-to-noise ratio when analyzing
CMB secondary eﬀects.
Figure 3 shows examples of templates, produced using
raytracing from 0 to 100 Mpc/h.
Only one sample is
shown here, but as before, the full Bayesian posterior is
available for thorough quantiﬁcation of uncertainties.
ACKNOWLEDGMENTS
FL thanks the organizers of the Rencontres du Vietnam
2015, Cosmology 50 years after CMB discovery, for a very
nice meeting and acknowledges support from the ´Ecole poly-
technique through an AMX grant and from the European Re-
search Council through grant 614030, Darksurvey. JJ is par-
tially supported by a Feodor Lynen Fellowship by the Alexan-
der von Humboldt foundation.
BW acknowledges funding
from an ANR Chaire d’Excellence (ANR-10-CEXC-004-01)
and the UPMC Chaire Internationale in Theoretical Cosmol-
ogy.
This work has been done within the Labex Institut
Lagrange de Paris (reference ANR-10-LABX-63) part of the
Idex SUPER, and received ﬁnancial state aid managed by the
Agence Nationale de la Recherche, as part of the programme
Investissements d’avenir under the reference ANR-11-IDEX-
0004-02. This research was supported by the DFG cluster of
excellence “Origin and Structure of the Universe”.
REFERENCES
(Abazajian et al.,
2009) K. N. Abazajian,
J. K. Adelman-
McCarthy, M. A. Ag¨ueros, S. S. Allam, C. Allende Prieto, D. An,
K. S. J. Anderson, S. F. Anderson, J. Annis, N. A. Bahcall, et al.,
The Seventh Data Release of the Sloan Digital Sky Survey, As-
trophys. J. Supp. 182, 543 (2009), arXiv:0812.0649.
(Cai et al., 2010) Y.-C. Cai, S. Cole, A. Jenkins, C. S. Frenk,
Full-sky map of the ISW and Rees-Sciama eﬀect from Gpc
simulations, Mon. Not. R. Astron. Soc. 407, 201 (2010),
arXiv:1003.0974 [astro-ph.CO].
(Falck, Neyrinck & Szalay, 2012) B. L. Falck, M. C. Neyrinck, A. S.
Szalay, ORIGAMI: Delineating Halos Using Phase-space Folds,
Astrophys. J. 754, 126 (2012), arXiv:1201.2353 [astro-ph.CO].
(Hahn et al., 2007) O. Hahn, C. Porciani, C. M. Carollo, A. Dekel,
Properties of dark matter haloes in clusters, ﬁlaments, sheets
and voids, Mon. Not. R. Astron. Soc. 375, 489 (2007), astro-
ph/0610280.
(Jasche & Wandelt, 2013) J. Jasche, B. D. Wandelt, Bayesian
physical reconstruction of initial conditions from large-scale
structure surveys, Mon. Not. R. Astron. Soc. 432, 894 (2013),
arXiv:1203.3639 [astro-ph.CO].
(Jasche, Leclercq & Wandelt, 2015) J. Jasche, F. Leclercq, B. D.
Wandelt, Past and present cosmic structure in the SDSS DR7
main sample, Journal of Cosmology and Astroparticle Physics
1, 036 (2015), arXiv:1409.6308.
(Jasche et al., 2010) J. Jasche, F. S. Kitaura, C. Li, T. A. Enßlin,
Bayesian non-linear large-scale structure inference of the Sloan
Digital Sky Survey Data Release 7, Mon. Not. R. Astron. Soc.
409, 355 (2010), arXiv:0911.2498 [astro-ph.CO].
(Lavaux & Jasche, 2016) G. Lavaux, J. Jasche, Unmasking the
masked Universe: the 2M++ catalogue through Bayesian eyes,
Mon. Not. R. Astron. Soc. 455, 3169 (2016), arXiv:1509.05040.
(Lavaux & Wandelt, 2010) G. Lavaux, B. D. Wandelt, Preci-
sion cosmology with voids: deﬁnition, methods, dynamics, Mon.
Not. R. Astron. Soc. 403, 1392 (2010), arXiv:0906.4101 [astro-
ph.CO].
(Lavaux & Hudson, 2011) G. Lavaux, M. J. Hudson, The 2M++
galaxy redshift catalogue, Mon. Not. R. Astron. Soc. 416, 2840
(2011), arXiv:1105.6107.
(Lavaux, Leclercq & Jasche, in prep.) G. Lavaux, F. Leclercq,
J. Jasche, (in prep.).
(Lavaux, Afshordi & Hudson, 2013) G. Lavaux, N. Afshordi, M. J.
Hudson, First measurement of the bulk ﬂow of nearby galaxies
using the cosmic microwave background, Mon. Not. R. Astron.
Soc. 430, 1617 (2013), arXiv:1207.1721.
(Leclercq,
2015)
F.
Leclercq,
Bayesian
large-scale
structure
inference
and
cosmic
web
analysis,
Ph.D.
thesis,
Institut
d’Astrophysique de Paris (2015).
(Leclercq, Jasche & Wandelt, 2015a) F. Leclercq, J. Jasche,
B. Wandelt, Cosmic web-type classiﬁcation using decision the-
ory, Astron. & Astrophys. 576, L17 (2015a), arXiv:1503.00730.
(Leclercq, Jasche & Wandelt, 2015b) F. Leclercq, J. Jasche,
B. Wandelt, Bayesian analysis of the dynamic cosmic web in
the SDSS galaxy survey, Journal of Cosmology and Astroparti-
cle Physics 6, 015 (2015b), arXiv:1502.02690.
(Leclercq et al., in prep. a) F. Leclercq, G. Lavaux, J. Jasche,
B. Wandelt, (in prep. a).
(Leclercq et al., in prep. b) F. Leclercq, J. Jasche, G. Lavaux,
B. Wandelt, (in prep. b).
(Li et al., 2014) M. Li, R. E. Angulo, S. D. M. White, J. Jasche,
Matched ﬁlter optimization of kSZ measurements with a recon-
structed cosmological ﬂow ﬁeld, Mon. Not. R. Astron. Soc. 443,
2311 (2014), arXiv:1404.0007.
(Tassev, Zaldarriaga & Eisenstein, 2013) S. Tassev, M. Zaldarriaga,
D. J. Eisenstein, Solving large scale structure in ten easy steps
with COLA, Journal of Cosmology and Astroparticle Physics 6,
036 (2013), arXiv:1301.0322 [astro-ph.CO].

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
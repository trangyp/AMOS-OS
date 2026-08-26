---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1710.089
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1710.08900_Accounting_for_the_diversity_in_stellar_environments

> Source: 1710.08900_Accounting_for_the_diversity_in_stellar_environments.pdf

> Pages: 4

---


## Page 1


Accounting for the diversity in stellar environments
Michael K¨uﬀmeier
kueffmeier@nbi.ku.dk
Centre for Star and Planet Formation, Niels Bohr Institute and Natural History Museum of Denmark, University
of Copenhagen, Øster Voldgade 5-7, DK-1350 Copenhagen K, Denmark
Troels Haugbølle
haugboel@nbi.ku.dk
Centre for Star and Planet Formation, Niels Bohr Institute and Natural History Museum of Denmark, University
of Copenhagen, Øster Voldgade 5-7, DK-1350 Copenhagen K, Denmark
˚
Ake Nordlund
aake@nbi.ku.dk
Centre for Star and Planet Formation, Niels Bohr Institute and Natural History Museum of Denmark, University
of Copenhagen, Øster Voldgade 5-7, DK-1350 Copenhagen K, Denmark
Abstract
Stars and their corresponding protoplanetary disks
form in diverse environments.
To account for these
natural variations, we investigate the formation pro-
cess around nine solar mass stars with a maximum
resolution of 2 AU in a Giant Molecular Cloud of (40
pc)3 in volume by using the adaptive mesh reﬁnement
code ramses. The magnetohydrodynamic simulations
reveal that the accretion process is heterogeneous in
time, in space, and among protostars of otherwise sim-
ilar mass. During the ﬁrst roughly 100 kyr of a proto-
star evolving to about a solar mass, the accretion rates
peak around 10−5 to 10−4 M⊙yr−1 shortly after its
birth, declining with time after that. The diﬀerent en-
vironments also aﬀect the spatial accretion, and infall
of material to the star-disk system is mostly through
ﬁlaments and sheets. Furthermore, the formation and
evolution of disks varies signiﬁcantly from star to star.
We interpret the variety in disk formation as a con-
sequence of the diﬀerences in the combined eﬀects of
magnetic ﬁelds and turbulence that may cause diﬀer-
ences in the eﬃciency of magnetic braking, as well as
diﬀerences in the strength and distribution of speciﬁc
angular momentum.
1. Introduction
Protoplanetary disks form around stars as a conse-
quence of pre-stellar cores collapsing in ﬁlaments of
Giant Molecular Clouds, which makes them the small-
est entity in a hierarchy of scales. Length scales range
from tens of parsecs for Giant Molecular Clouds to
protoplanetary disk sizes of ∼10 AU to ∼100 AU.
It is computationally very challenging to cover such
a broad range of scales in a single simulation. There-
fore, simulations of protostellar formation traditionally
start from initial conditions representing a collapsing
spherically symmetric cloud, as an approximation to
the pre-stellar core (Machida et al., 2004; 2006; 2007;
Proceedings of the Star Formation in Diﬀerent Environ-
ments, ICISE, Quy Nhon, Vietnam, 2016. PSFDE: volume
01. Copyright 2016 by the author(s).
Machida & Matsumoto, 2011; Joos et al., 2012; 2013;
Tomida et al., 2010; 2013; Li et al., 2011; Seifried et al.,
2011; 2012; Vaytet & Haugbølle, 2016). This approach
allows detailed parameter studies, but neglecting the
underlying turbulence in Giant Molecular Clouds and
the potential interactions with the surroundings could
potentially limit the applicability of such idealized ini-
tial conditions.
Considering the dynamics of Giant
Molecular Clouds, it is important to investigate how
they aﬀect the formation of protostars and protoplane-
tary disks. Given that most of the volume in the Giant
Molecular Cloud is of relatively low density and thus
of less interest for star formation, simulating the huge
range of scales becomes feasible by applying adaptive
mesh reﬁnement to the problem. First, we brieﬂy ex-
plain the concept behind our zoom-method, which al-
lowed us to resolve the accretion and disk formation
process, while simultaneously accounting for the large-
scale environment. Second, we present an overview of
the most signiﬁcant results obtained in our study be-
fore we discuss and summarize their consequences.
We use use a highly modiﬁed version of the adaptive
mesh-reﬁnement code ramses (Teyssier, 2002; Fro-
mang et al., 2006), which in principle can handle re-
ﬁnement over up to 29 factors of two (Nordlund et al.,
2014). In Fig. 1, we sketch the procedure and refer the
reader to (Kuﬀmeier et al., 2016; 2017a;b) for further
details.
We start from an already turbulent GMC model of
a cubic box of size (40 pc)3 with periodic boundary
conditions, consisting of self-gravitating, magnetized
gas.
The average H2 number density is 30 cm−3,
which yields a total mass of the box of approximately
105M⊙.
The assumed GMC lifetimes are in agree-
ment with the ’star formation in a crossing time’
paradigm (Elmegreen, 2000; Elmegreen & Shadmehri,
2003; Padoan et al., 2016), and with observational es-
timates (Murray, 2011), and the turbulence is driven
by massive stars that inject energy of 1051 erg of ther-
arXiv:1710.08900v3  [astro-ph.GA]  9 Nov 2017


## Page 2


Accounting for the diversity in stellar environments
4 Myr
0 Myr
100 kyr
0 kyr
maximum level of refinement 16; 
minimum cell size ~126 AU
maximum level of refinement 22; 
minimum cell size ~2 AU
~4 kAU
40 pc
40 pc
~100 AU
Figure 1. Sketch of the zoom-in procedure. First we evolve
a snapshot of an already turbulent GMC of (40 pc)3 in size
(upper left image) for about 4 Myr (upper right image).
During the evolution multiple sinks are created and at the
current time more than 500 stars have formed. We zoom
in on selected pre-stellar cores (lower left image) to re-
solve the formation process with higher resolution for up
to about 100 kyr after sink creation (lower right image).
This procedure is applied to altogether nine protostars.
mal energy into the GMC after a mass-dependent life-
time.
For the heating via UV-photons (Osterbrock
& Ferland, 2006), we apply the recipe of (Franco &
Cox, 1986) and use an optically thin cooling function
(Gnedin & Hollon, 2012) for the cold dense gas.
The combined eﬀects of turbulence and self-gravity in-
duce the formation of ﬁlaments, and subsequently star
formation inside the ﬁlaments. To make the problem
computationally tractable, we describe the collapse of
matter into stars with a sub-grid sink particle algo-
rithm.
As illustrated in Fig. 1, we ﬁrst evolve the
GMC with a minimum cell size of 126 AU before we
zoom-in onto the individual sinks of interest with a
minimum cell-size of 2 AU. This second stage provides
information about protostellar accretion, including the
subsequent formation of protoplanetary disks.
2. Results of the zoom-ins
The diﬀerent environments of the protostars cause dif-
ferences in the accretion process and disk formation
among the protostars. We illustrate the accretion pro-
ﬁles of nine sinks in the lower panel of Fig. 2. One can
see a general trend for the diﬀerent sinks, with a very
steep initial increase to values of about 10−4 M⊙yr−1
to 10−5 M⊙yr−1 followed by a general decrease. The
decrease varies between sinks and some of the sinks
still show accretion rates of more than 10−6 M⊙yr−1
after ∼100 kyr. Moreover, we can see that some of the
sinks show signiﬁcant ﬂuctuations during their evolu-
tion. Since we average over periods of 200 to 400 years
between the snapshots we are underestimating the am-
plitude of these episodic accretion events. Finally, we
note that the sinks accrete their mass through accre-
tion channels (Seifried et al., 2013) rather than uni-
0
20
40
60
80
100
Time after star formation in kyr
10
10
10 -5
10
Accretion rate in M yr−1
0
100
200
300
1000
Disk size in AU
-6
-7
-4
Figure 2.
Upper panel:
Evolution of the disk radius
around the diﬀerent sinks.
Lower panel: Accretion pro-
ﬁle for 9 sinks created in zoom-ins started with increased
resolution before sink creation.
formly in space.
Fig. 3 shows slices in the plane perpendicular to the
mean angular momentum vector at t = 50 kyr around
six sinks. The images and the upper panel in Fig. 2
reveal the variety in disk formation for the diﬀerent
stellar environments, and also the spatial variations
in the accretion process induced by ﬁlamentary arms
feeding the forming protoplanetary disk.
Also, the
disks show signs of spiral arms or inﬂowing gas streams
strikingly similar to what has been observed by ALMA
and with the Subaru Next Generation Adaptive Optics
(HiCIAO) (Liu et al., 2016).
3. Discussion and Conclusion
Using a numerical model that simultaneously encom-
pass the large-scale environment of a Giant Molecu-
lar Cloud and the the immediate environment of nine
protostars, covering seven orders of magnitude in dy-
namic range, we have investigated the environmental
eﬀects on the protostellar formation process. One ma-
jor result is that stellar accretion can be very diﬀerent


## Page 3


Accounting for the diversity in stellar environments
−100
−50
0
50
100
Image y (AU)
−100
−50
0
50
100
Image y (AU)
−100−50
0
50 100
Image x (AU)
−100
−50
0
50
100
Image y (AU)
−100−50
0
50 100
Image x (AU)
10−17
10−16
10−15
10−14
10−13
10−12
Density
  g
cm3

Figure 3. Slices in the plane vertical to the mean angular
momentum vector calculated for a sphere of 100 AU around
six diﬀerent sinks at t = 50 kyr. The upper left slice corre-
sponds to the sink with the blue dots in the accretion plot,
the upper right to the red triangles, the middle left to the
cyan squares, the middle right to the magenta asterisks,
the lower left to the yellow pluses, and the lower right to
the blue diamonds.
depending on the protostellar environment. We also
conclude that the diversity in the large-scale stellar
environment profoundly inﬂuences the formation and
evolution of protoplanetary disks.
If the magnetization of the surrounding gas is suﬃ-
ciently limited to avoid the magnetic braking catas-
trophe, protoplanetary disks of several tens of AU can
form as early as a few thousand years after star forma-
tion. In cases where the magnetization of the collaps-
ing gas is suﬃciently large (low mass-to-ﬂux ratios),
no disk of more than ≈10 AU in size will form around
the star. The main reason why the magnetic braking
catastrophe is avoided in many cases is the reduction
of magnetic braking caused by turbulence.
Acknowledgments
This research was supported by a grant from the Dan-
ish Council for Independent Research to ˚AN, a Sapere
Aude Starting Grant from the Danish Council for Inde-
pendent Research to TH. Research at Centre for Star
and Planet Formation is funded by the Danish Na-
tional Research Foundation (DNRF97). We acknowl-
edge PRACE for awarding us access to the computing
resource CURIE based in France at CEA for carrying
out part of the simulations. Archival storage and com-
puting nodes at the University of Copenhagen HPC
center, funded with a research grant (VKR023406)
from Villum Fonden, were used for carrying out part
of the simulations and the post-processing. Finally, we
acknowledge the developers of the python-based an-
alyzing tool yt (http://yt-project.org/) (Turk et al.,
2011) that simpliﬁed our analysis.
References
Elmegreen, B. G. 2000, ApJ, 530, 277
Elmegreen, B. G., & Shadmehri, M. 2003, MNRAS,
338, 817
Franco, J., & Cox, D. P. 1986, PASP, 98, 1076
Fromang, S., Hennebelle, P., & Teyssier, R. 2006,
A&A, 457, 371
Gnedin, N. Y., & Hollon, N. 2012, ApJS, 202, 13
Joos, M., Hennebelle, P., & Ciardi, A. 2012, A&A, 543,
A128
Joos, M., Hennebelle, P., Ciardi, A., & Fromang, S.
2013, A&A, 554, A17
Kuﬀmeier, M., Frostholm Mogensen, T., Haugbølle,
T., Bizzarro, M., & Nordlund, ˚A. 2016, ApJ, 826,
22
Kuﬀmeier M., Haugbølle T., Nordlund ˚A. 2017a, ApJ,
846, 7
Kuﬀmeier M., Frimann S., Jensen S. S., Haugbølle T.,
2017b, ArXiv e-prints, arXiv:1710.00931
Larson, R. B. 1981, MNRAS, 194, 809
Li, Z.-Y., Krasnopolsky, R., & Shang, H. 2011, ApJ,
738, 180
Liu, H. B., Takami, M., Kudo, T., et al. 2016, Science
Advances, 2, http://advances.sciencemag.org/
content/2/2/e1500875.full.pdf
Machida, M. N., Inutsuka, S.-i., & Matsumoto, T.
2007, ApJ, 670, 1198
Machida, M. N., & Matsumoto, T. 2011, MNRAS, 413,
2767
Machida, M. N., Matsumoto, T., Hanawa, T., &
Tomisaka, K. 2006, ApJ, 645, 1227
Machida, M. N., Tomisaka, K., & Matsumoto, T. 2004,
MNRAS, 348, L1
Murray, N. 2011, ApJ, 729, 133
Nordlund, ˚A., Haugbølle, T., K¨uﬀmeier, M., Padoan,
P., & Vasileiades, A. 2014, in IAU Symposium,
Vol. 299, IAU Symposium, ed. M. Booth, B. C.
Matthews, & J. R. Graham, 131–135
Osterbrock, D. E., & Ferland, G. J. 2006, Astrophysics
of gaseous nebulae and active galactic nuclei


## Page 4


Accounting for the diversity in stellar environments
Padoan, P., Pan, L., Haugbølle, T., & Nordlund, ˚A.
2016, ApJ, 822, 11
Seifried, D., Banerjee, R., Klessen, R. S., Duﬃn, D.,
& Pudritz, R. E. 2011, MNRAS, 417, 1054
Seifried, D., Banerjee, R., Pudritz, R. E., & Klessen,
R. S. 2013, MNRAS, 432, 3320
Seifried, D., Pudritz, R. E., Banerjee, R., Duﬃn, D.,
& Klessen, R. S. 2012, MNRAS, 422, 347
Teyssier, R. 2002, A&A, 385, 337
Tomida, K., Tomisaka, K., Matsumoto, T., et al. 2013,
ApJ, 763, 6
—. 2010, ApJ, 714, L58
Turk, M. J., Smith, B. D., Oishi, J. S., et al. 2011,
ApJS, 192, 9
Vaytet, N., & Haugbølle, T. 2016, A&A, 598, A116

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1710_08900_accounting_for_the_diversity_in_stellar_environments
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2017/1710_08900_ACCOUNTING_FOR_THE_DIVERSITY_IN_STELLAR_ENVIRONMENTS.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

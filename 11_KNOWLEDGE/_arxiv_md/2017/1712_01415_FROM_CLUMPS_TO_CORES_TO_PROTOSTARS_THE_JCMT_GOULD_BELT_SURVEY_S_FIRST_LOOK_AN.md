---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1712.01415
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1712.01415_From_Clumps_to_Cores_to_Protostars__The_JCMT_Gould_Belt_Survey_s__First-Look__an

> Source: 1712.01415_From_Clumps_to_Cores_to_Protostars__The_JCMT_Gould_Belt_Survey_s__First-Look__an.pdf

> Pages: 4

---


## Page 1


From Clumps to Cores to Protostars: The JCMT Gould Belt
Survey’s “First-Look” analysis of Southern Orion A using SCUBA-2
S. Mairs1,2, D. Johnstone2, H. Kirk2
smairs@uvic.ca
1University of Victoria, 3800 Finnerty Road, Victoria, BC, Canada, V8P 5C2
2Herzberg Astrophysics, National Research Council of Canada, 5071 West Saanich Road, Victoria, BC, V8N
3L3
Abstract
We present a subset of the James Clerk Maxwell Tele-
scope Gould Belt Survey’s “ﬁrst-look” results of the
southern extent of the Orion A molecular cloud. Em-
ploying a two-step structure identiﬁcation process, we
constructed individual catalogues for large-scale re-
gions of signiﬁcant emission labeled as “islands” and
smaller-scale subregions called “fragments” using the
850 µm continuum maps obtained using the Submil-
limetre Common-User Bolometer Array 2 (SCUBA-2).
We highlight the relationship between the concentra-
tion and Jeans stability for regions of signiﬁcant emis-
sion and present the results of an investigation into
the spatial distribution of Young Stellar Objects de-
tected using the Spitzer Space Telescope and the Her-
schel Space Observatory. We ﬁnd an apparent evolution
in the velocity dispersion from Class 0 to Class II ob-
jects which we derive from comparing our observations
to a simple model.
1. Introduction
The James Clerk Maxwell Telescope’s (JCMT) Gould
Belt Legacy Survey (GBS, Ward-Thompson et al.
2007) is a large-scale project which has mapped the no-
table star-forming regions within 500 pc of the Sun.In
these proceedings, we present a subset of the ﬁrst
results from the Southern Orion A region (Mairs et
al. 2016) observed at 850 µm with the Submillimetre
Common-User Bolometer Array 2 (SCUBA-2) instru-
ment (Holland et al. 2013).
The detected emission in Southern Orion A includes
several active sites of Galactic star formation such as
OMC-4, OMC-5, and L1641N. It contains dozens of
embedded sources (Johnstone et al. 2006; Ali et al.
2004; Chen et al. 1996), as well as several Herbig-
Haro objects. The SCUBA-2 observations presented
in Mairs et al. (2016) have a sensitivity which is an
order of magnitude deeper than previous maps (see
Johnstone et al. 2006) along with a much wider spa-
tial coverage (8100 arcmin2 compared to 2300 arcmin2
in the original Southern Orion A SCUBA data). Thus,
Proceedings of the Star Formation in Diﬀerent Environ-
ments, ICISE, Quy Nhon, Vietnam, 2016. PSFDE: volume
01. Copyright 2016 by the author(s).
we have a much better diagnostic to characterise the
dense, cold dust. To complement these new continuum
observations of dense, often gravitationally unstable
gas, we use extinction data taken in the J, H and K
bands (using the Two Micron All Sky Survey, 2MASS)
that were determined by the Near-infrared Color Ex-
cess (NICE) team (M. Lombardi, private communi-
cation, July 18th, 2015), and the young stellar object
(YSO) catalogues of Megeath et al. (2012) and Stutz et
al. (2013) obtained using the Spitzer Space Telescope
and the Herschel Space Observatory, respectively.
In Section 2, we present our structure identiﬁcation
procedure and highlight some of the key results with
regard to the continuum emission. In Section 3, we dis-
cuss the spatial distribution of Young Stellar Objects
(YSOs) and compare this result to a simple model as-
suming the YSOs were launched from dense cores cur-
rently showing evidence of star formation.
2. Fragmentation of Dense Structures
Southern Orion A contains a diverse set of objects de-
ﬁned by localized emission.
We consider a pixel to
be “signiﬁcant” if it has a value of at least 3σrms
(σrms = 3.1 mJy beam−1 ) in the 850 µm map.
We
ﬁrst extract the largest objects studied in this work
by simply drawing a contour at 3σrms and retaining
all enclosed structures larger than approximately one
beam (15” in circularly projected diameter). We ac-
complish this identiﬁcation using Starlink’s version of
the algorithm ClumpFind (Williams et al. 1994) as
implemented in the Cupid package (Berry et al. 2007)
by deﬁning only one ﬂux level over which signiﬁcant
structure is identiﬁed. Each non-spurious object de-
tected is referred to as an “island”; any ﬂux present
in the map outside of an island is considered to be
dominated by noise.
In the second step, we employ the JCMT Science
Archive algorithm jsa catalogue found in Starlink’s
PICARD package (Gibb et al. 2013). This algorithm
uses the FellWalker routine (Berry et al. 2015).
Brieﬂy, FellWalker marches through a given im-
age pixel by pixel and identiﬁes the steepest gradient
arXiv:1712.01415v1  [astro-ph.GA]  4 Dec 2017


## Page 2


Title Suppressed Due to Excessive Size
up to an emission peak. After performing tests to en-
sure that the peak is “real” and not just a noise spike,
the local maximum is assigned an identifying integer
and all the pixels above a user-deﬁned threshold that
were included in the path to the peak are given the
same identiﬁer. In this way, all of the robust peaks
in the image are catalogued and the structure asso-
ciated with each peak can be analyzed. These local-
ized peaks often separate emission contained within
the larger islands into multiple components. In this
way, the compact source catalogue generated reveals
the substructure present within the context of coin-
cident large-scale emission. For this reason, we label
the compact components as “fragments”. We refer to
an island which contains at least two fragments as a
“complex island” and an island that contains only one
fragment as a “monolithic island”.
2.1. Stability and Concentration
More so than islands, it is the compact, localized frag-
ments for which we expect Jeans unstable cases to
be forming (or to eventually go on to form) stars.
Thus, in Figure 1, we compare fragment concentra-
tions with their Jeans stabilities. The concentration,
C, is a useful metric to quantify whether or not a
structure is peaked. The concentration is calculated
by comparing the total ﬂux density measured across a
given island or fragment to a uniform structure of the
same area wherein each pixel is set to the peak bright-
ness, f850,peak.
Following Johnstone et al. (2001),
C = 1 −
1.13B2S850
πR2×f850,peak , where B is the beam width
in arcseconds, R is the radius of the source measured
in arcseconds, S850 is the total ﬂux of the source mea-
sured in Jy, and f850,peak is the peak brightness of
the source measured in Jy beam−1.
Highly concen-
trated sources are expected to have a higher degree of
self-gravity (see Johnstone et al. 2001 and Kirk et al.
2006), eventually collapsing and forming one to a few
stellar systems. To calculate the Jeans stability, we
compare the mass of a fragment, M, to its associated
Jeans mass, MJ (Mairs et al. 2016).
In Figure 1, each fragment is colour-coded by its as-
sociation with YSOs identiﬁed in the Megeath et al.
(2012) and Stutz et al. (2013) catalogues. Class 0+I
and ﬂat spectrum sources are denoted “P” for proto-
star. A green outline is given for protostars contained
within a fragment’s boundaries and a solid green point
is given for fragments which have a protostar within
15” (1 beam) of the peak ﬂux measurement.
Class
II+III objects are labelled “D” for disk sources. Red
(“RP”) and blue (“FP”) outlines are given for two
classes of protostar candidates, see Megeath et al.
−1.5
−1.0
−0.5
0.0
0.5
1.0
1.5
log(Mfragments/MJ,fragments)
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1.0
Concentration
Unstable
Peaked
No YSOs
D
RP
FP
P not at Peak
P
−1.5
−1.0
−0.5
0.0
0.5
1.0
1.5
log(Mfragments/MJ,fragments)
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1.0
Concentration
Sig. Unstable
Unstable
Peaked
No YSOs
D
RP
FP
P not at Peak
P
Fragments
Figure 1. Fragment concentration versus fragment stabil-
ity. The dashed green lines show a concentration of 0.5 on
the ordinate and the gravitational instability line on the ab-
scissa. The vertical dashed black line represents an M/MJ
ratio of 4 where we deﬁne sources to be signiﬁcantly unsta-
ble. Colours represent associations between the identiﬁed
fragment and several classes of YSOs as denoted in the
legend. Diamonds represent a fragment which belongs to
a complex island and a circle represents a fragment which
traces isolated, monolithic structure. This ﬁgure is taken
from Mairs et al. (2016).
2012). Green dashed lines indicate the nominal grav-
itational instability line M/MJ ≥1 (horizontal) and
C = 0.5 (vertical). C = 0.5 is chosen because it repre-
sents a relatively concentrated core approximately half
way between a uniform density (0.33) and self gravi-
tating Bonnor Ebert sphere (0.72) (see Johnstone et al.
2001). Note that the fragments fall broadly into two
regimes: 1. gravitationally stable and low concentra-
tion and 2. gravitationally unstable and with peaked
emission. We note as well that the diamond symbols
in Figure 1 represent a fragment which belongs to a
complex island (an island containing at least two frag-
ments) and a circle represents a fragment which traces
isolated, monolithic structure. We would expect the
gravitationally unstable, peaked fragments to be the
population which is associated with protostars. In gen-
eral, we see that this is the case. In Figure 1, only
8% of the fragments without discernible signs of YSOs
appear unstable and concentrated. Of those, the frag-
ments which were extracted from monolithic islands
(or have no island associations) are outnumbered by
those which were extracted from complex islands (21%
and 79%, respectively). Conversely, we would expect
the gravitationally stable, less peaked fragments to be
the population which is not actively forming stars. In-


## Page 3


Title Suppressed Due to Excessive Size
deed, only 23% of the stable and uniform fragments
appear to have YSOs. Almost all of these fragments
are associated with monolithic islands (83%); that is,
they do not have “siblings” within the same island. A
catalogue of interesting follow-up source candidates is
presented in Mairs et al. (2016).
3. The Young Stellar Object
Distribution
An analysis of the spatial distribution of YSOs with
respect to the location of the nearest fragment’s peak
emission is presented in Mairs et al. (2016). In that
analysis, it is clear that the surface densities of these
sources can be separated into two populations we la-
bel as “clustered” (away from the edges of the map
and close to fragments) and “distributed” (the spo-
radic sources at larger distances from the clustered
objects around fragments).
We attempted to recre-
ate both populations using a simple model assuming:
1. the currently observed structures are linked to the
formation of young stars and their present distribu-
tion, 2. all of the observed YSOs formed in fragments
which are calculated to be Jeans unstable and every
Jeans unstable fragment has the same probability of
producing a YSO, 3. the half-life age of disks is esti-
mated to be t0.5 = 2 Myr and we detect no discs older
than 10 Myr, 4. protostars to have an age ≤0.5 Myr,
and 5. the random 3D space velocities of the observed
YSOs follow a Maxwell-Boltzmann distribution with
a ﬁxed most probable speed, vp. Ten vp values were
tested from 0.1 km s−1 to 1.0 km s−1.
In order to recreate both the clustered and distributed
populations of YSOs simultaneously, it was necessary
to ﬁt diﬀerent vp values to the diﬀerent YSO classes
(younger protostars and more evolved disk sources).
The left panel of Figure 2 shows a comparison be-
tween the observed projected distance between pro-
tostar (Class 0+I and ﬂat spectrum sources) loca-
tions and the nearest fragment peak brightness loca-
tion and the results obtained from our model assuming
vp = 0.5 km s−1. We found that the vp value which
best ﬁts the protostar population between 0.2 km s−1
and 0.5 km s−1.
The right panel of Figure 2 shows
the same results for the disk sources (Class II+III) as-
suming the best ﬁtting vp value of 0.7 km s−1. Note
that Jorgensen et al. (2007), through observations of
the Perseus molecular cloud, and Frimann et al (2016),
through the MHD simulation RAMSES, found the ve-
locity dispersion of Class 0 objects to be ∼0.1-0.2 km
s−1. Thus, there appears to be a trend in the velocity
with YSO class. These velocities, however, are highly
dependent on the lifetimes of each type of object.
For more information on this work, including further
analyses and full catalogues of the observed structures,
see Mairs et al. (2016).
Acknowledgments
Steve Mairs was partially supported by the Natural
Sciences and Engineering Research Council (NSERC)
of Canada graduate scholarship program. Doug John-
stone is supported by the National Research Council
of Canada and by an NSERC Discovery Grant. The
authors wish to thank ICISE for hosting SFDE 2016
and extend our gratitude to both the LOC and SOC
for organising this conference.
References
B. Ali, A. Noriega-Crespo, ApJ. 613, 374 (2004)
D. Berry et al., ASPCS. 376, 425 (2007)
D. Berry Astronomy and Computing. 10, 22 (2015)
H. Chen et al., AJ. 112, 717 (1996)
S. Frimann et al., A&A. 587, A59 (2016)
A. G. Gibb et al., Starlink User Note 265. Joint
Astronomy Centre, HI. (2013)
W. S. Holland et al., MNRAS. 430, 2513 (2013)
D. Johnstone et al., ApJ. 559, 307 (2001)
D. Johnstone, J. Bally, ApJ. 653, 383 (2006)
J. K. Jørgensen et al., ApJ. 656, 293 (2007)
H. Kirk et al., ApJ. 646, 1009 (2006)
S. Mairs et al., MNRAS. 454, 2557 (2015)
S. Mairs et al., MNRAS. 461, 4022 (2016)
S. T. Megeath et al., AJ. 144, 192 (2012)
A. Stutz et al., ApJ. 767, 36 (2013)
D. Ward-Thompson et al., PASP. 119, 855 (2007)
J. P. Williams et al., ApJ. 428, 693 (1994)


## Page 4


Title Suppressed Due to Excessive Size
Projected Distance (pc)
Projected Distance (pc)
Number
Number
Vp = 0.5 km/s
Vp = 0.7 km/s
           
Figure 2. Left: The calculated projected distance between model protostar locations and the nearest fragment peak bright-
ness location assuming vp = 0.5 km s−1 (cyan, dashed lines) plotted along with the observed distribution (green, solid
lines). Right: The calculated projected distance between model disk source locations and the nearest fragment peak bright-
ness location assuming vp = 0.7 km s−1 (magenta, dashed lines) plotted along with the observed distribution (brown, solid
lines). This ﬁgure is taken from Mairs et al. (2016).

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
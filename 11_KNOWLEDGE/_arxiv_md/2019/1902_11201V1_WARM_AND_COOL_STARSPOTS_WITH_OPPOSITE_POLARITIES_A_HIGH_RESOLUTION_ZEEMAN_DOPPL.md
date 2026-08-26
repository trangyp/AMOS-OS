---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1902.11201v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1902.11201v1_Warm_and_cool_starspots_with_opposite_polarities__A_high-resolution_Zeeman-Doppl

> Source: 1902.11201v1_Warm_and_cool_starspots_with_opposite_polarities__A_high-resolution_Zeeman-Doppl.pdf

> Pages: 12

---


## Page 1


Astronomy & Astrophysics manuscript no. iipepsi˙strassmeier˙revised˙pdf
c⃝ESO 2019
March 1, 2019
Warm and cool starspots with opposite polarities⋆
A high-resolution Zeeman-Doppler-Imaging study of II Pegasi with PEPSI
K. G. Strassmeier1, T. A. Carroll1, and I. V. Ilyin1
Leibniz-Institut f¨ur Astrophysik Potsdam (AIP), An der Sternwarte 16, 14482 Potsdam, Germany
e-mail: kstrassmeier@aip.de
Received xxx x, 2018; accepted xxx x, 2019
ABSTRACT
Aims. We present a temperature and a magnetic-ﬁeld surface map of the K2 subgiant of the active binary II Peg. Employed are high
resolution Stokes IV spectra obtained with the new Potsdam Echelle Polarimetric and Spectroscopic Instrument (PEPSI) at the Large
Binocular Telescope (LBT).
Methods. Fourteen average line proﬁles are inverted using our iMap code. We have employed an iterative regularization scheme
without the need of a penalty function and incorporate a physical 3D description of the surface ﬁeld vector. The spectral resolution of
our data is 130 000 which converts to 20 resolution elements across the disk of II Peg.
Results. Our main result is that the temperature features on II Peg closely correlate with its magnetic ﬁeld topology. We ﬁnd a warm
spot (350 K warmer with respect to the eﬀective temperature) of positive polarity and radial ﬁeld density of 1.1 kG coexisting with a
cool spot (780 K cooler) of negative polarity of 2 kG. Several other cool features are reconstructed containing both polarities and with
(radial) ﬁeld densities of up to 2 kG. The largest cool spot is reconstructed with a temperature contrast of 550 K, an area of almost 10%
of the visible hemisphere, and with a multipolar magnetic morphology. A meridional and an azimuthal component of the ﬁeld of up to
±500 G is detected in two surface regions between spots with strong radial ﬁelds but diﬀerent polarities. A force-free magnetic-ﬁeld
extrapolation suggests that the diﬀerent polarities of cool spots and the positive polarity of warm spots are physically related through
a system of coronal loops of typical height of ≈2 R⋆. While the Hα line core and its red-side wing exhibit variations throughout all
rotational phases, a major increase of blue-shifted Hα emission was seen for the phases when the warm spot is approaching the stellar
central meridian indicating high-velocity mass motion within its loop.
Conclusions. Active stars such as II Peg can show coexisting cool and warm spots on the surface that we interpret resulting from two
diﬀerent formation mechanisms. We explain the warm spots due to photospheric heating by a shock front from a siphon-type ﬂow
between regions of diﬀerent polarities while the majority of the cool spots is likely formed due to the expected convective suppression
like on the Sun.
Key words. stars: imaging – stars: activity – stars: starspots – stars: individual: II Peg
1. Introduction
II Peg (HD 224085) is among the most active and spotted
RS CVn binaries known and its early-K subgiant component one
of the magnetically most active cool stars in the sky. Already 40
years ago, it had been center of many studies across the entire
electromagnetic spectrum, focussing on its extremely spotted
photosphere (e.g., Rucinski 1977, Vogt 1979), its chromosphere
(e.g., Byrne et al. 1987), corona (e.g., Schrijver et al. 1984, Mutel
& Lestrade 1985), large ﬂares (e.g., Doyle et al. 1991) or its mag-
netism in general (e.g., Vogt 1980). It was among the ﬁrst tar-
gets for which systematically Doppler imaging (DI) was applied.
Temperature and/or brightness maps were presented by Xiang et
al. (2013) for 2004, Hackman et al. (2012) for 2004-2010, by
Lindborg et al. (2011) for 1994-2002, by Carroll et al. (2007)
for 2004, by Gu et al. (2003) for 1999-2001, by Berdyugina et
al. (1999) for 1997-1998, by Weber (2004) for 1996-1997, by
Berdyugina et al. (1998) for 1992-1996, by Zboril (2003) for
1993, and by Hatzes (1995) for 1992-1994.
⋆Based on data acquired with PEPSI using the Large Binocular
Telescope (LBT). The LBT is an international collaboration among in-
stitutions in the United States, Italy, and Germany.
Direct magnetic ﬁeld measurements from Zeeman splitting
is not possible for II Peg due to its rotational line broaden-
ing of ≈22 km s−1. The ﬁrst detection of its magnetic ﬁeld was
achieved with a diﬀerential technique by Vogt (1980) which con-
sisted of a pair of consecutive spectra, the ﬁrst spectrum right-
circularly polarized and the second left-circularly polarized (es-
sentially Stokes V). In this way, a longitudinal magnetic ﬁeld
of strength −515 G was detected, but not regarded signiﬁcant.
However, Donati et al. (1992) conﬁrmed the detection later from
independent Stokes V data but with an eﬀective magnetic ﬁeld
density never exceeding 70 G.
The technique of Zeeman-Doppler imaging (ZDI) was in-
troduced three decades ago by Semel (1989) and had become
an indispensable technique for stellar magnetic ﬁeld studies as
noticed in many review papers (e.g., Strassmeier 2009, Donati
& Landstreet 2009, Reiners 2012). Among its main advantages
is that it resolves the polarity of magnetic features. However, it
took almost two decades that the ﬁrst ZDI of II Peg was con-
structed (Carroll et al. 2007 from SOFIN Stokes IV data). Their
ZDI map revealed local radial-ﬁeld densities of up to ±600 G
and was only possible with a multi-line principal component re-
construction because of the comparably weak polarimetric sig-
natures. Still, it is noted that the surface ﬁeld exhibited a strong
1
arXiv:1902.11201v1  [astro-ph.SR]  28 Feb 2019


## Page 2


Strassmeier, Carroll & Ilyin: II Peg with PEPSI
imbalance in the magnetic polarity and we believe that this im-
balance of magnetic ﬂux results, at least partially, from the in-
ability of the circular polarization signal to capture the whole
magnetic ﬂux of the star. A more extensive Stokes IV study fol-
lowed by Kochukhov et al. (2013) and revealed a complex and
evolving surface magnetic-ﬁeld morphology on II Peg.
Linear polarization (LP) in spectral lines of the Sun is typi-
cally up to ten times weaker than circular polarization (CP) (e.g.,
Stenﬂo 1989) and hardly accessible with reasonable signal-to-
noise ratio (S/N) in stars. However, Ros´en et al. (2013) found
strong and variable LP in II Peg. Ros´en et al. (2015) also noted
that the LP signal “cannot be readily seen in individual spectral
lines at the S/N of our observations” and thus made the applica-
tion of least-square deconvolution mandatory if to be included
in the ZDI inversion. Nevertheless, this spurred the ﬁrst ZDI of
a cool star using all four Stokes parameters (Ros´en et al. 2015).
It also led to a ﬁrst, and so far only, comparison of a ZDI map
generated from Stokes IV with a map from Stokes IQUV. The
ﬁeld strength of surface features was doubled or even quadru-
pled with respect to the Stokes IV map when LP was taken into
account, which the authors accounted to an increase in the over-
all complexity of the magnetic morphology. Same holds for the
total magnetic energy because the reconstructed ﬁeld got more
complex when IQUV was used.
In this paper, we present a Zeeman Doppler image from data
taken during the PEPSI-POL commissioning with the 2×8.4 m
LBT. Although only Stokes I and V were available at that time
in the commissioning, the spectral resolution is now 130 000 and
the LBT enabled a peak S/N of 1280 per pixel, that is, both
quantities twice as high as for previous data. We found that the
complexity of II Peg’s magnetic ﬁeld appears increased from
Stokes IV alone with respect to our earlier lower-resolution map
from SOFIN Stokes-IV data, which is in line with the ﬁndings
based on the full Stokes vector by Ros´en et al. (2015). Our new
observations are described in Sect. 2. Our ZDI code iMap is de-
scribed in Sect. 3 along with its assumptions, the input param-
eters, the creation of singular-value decomposition (SVD) line
proﬁles, and the resulting Doppler and Zeeman-Doppler images.
Section 4 discusses the results and Sect. 5 concludes and sum-
marizes our ﬁndings.
2. Observations
The polarimetric observations in this paper were obtained
with PEPSI at the 2×8.4 m LBT in Arizona. We employed
both polarimeters in the LBT’s two symmetric straight-through
Gregorian foci. Two pairs of octagonal 200µm ﬁbers per po-
larimeter feed the ordinary and extraordinary polarized beams
via a ﬁve-slice image slicer per ﬁber into the spectrograph. It pro-
duces four spectra per ´echelle order with a 4.2-pix spectral reso-
lution of R=130 000 that are recorded in a single exposure. The
two polarimeters are identical in design and construction but are
separately calibrated. Both are based on a classical dual-beam
design with a modiﬁed Foster prism as linear polarizer with
two orthogonally polarized beams exiting in parallel. The Foster
prism, atmospheric dispersion corrector (ADC), two ﬁber heads,
and two ﬁber viewing cameras are rotating as a single unit with
respect to the parallactic axis on the sky. The red-optimized poly-
methylmethacrylat (PMMA) quarter-wave retarder is inserted
into the optical beam in front of the Foster prism for the CP mea-
surements and retracted oﬀfor the LP measurements. This de-
sign allows us to avoid any cross-talk between CP and LP which
would be introduced in case of a half-wave retarder (Ilyin 2012).
The spectrograph and the polarimeters were described in detail
by Strassmeier et al. (2015, 2018).
Observations of II Peg commenced over seven consecutive
nights as part of the instrument commissioning in October 2017.
Fourteen spectra were taken simultaneously in two wavelength
regions with cross disperser (CD) III covering 4800–5441 Å and
with CD V covering 6278–7419 Å. We used the two 8.4 m LBT
mirrors (dubbed SX and DX) independently, that is CP with SX
and LP with DX simultaneously. Unfortunately, a problem with
the DX ADC did not allow the scientiﬁc use of LP. Retarder an-
gles of 45◦and 135◦were set for Stokes V, Foster prism position
angles of 0◦were set for Stokes Q and 45◦for Stokes U with
respect to the north. We note again that the retarder is removed
from the beam during the LP observations. Exposure time per
subintegration was 20 min (15 min and 25 min for some excep-
tions). Average S/N per pixel was around 1000 in CD V and
550 in CD III for a pair of exposures. The Stokes V polariza-
tion signatures in the spectra of II Peg are easily recognized by
eye. Figure 1 is a plot of the data around a wavelength of 6400 Å
within CD V. The log of all observations is given in the Appendix
in Table A.1.
Data reduction was done with the software package
SDS4PEPSI (“Spectroscopic Data Systems for PEPSI”) based
on Ilyin (2000), and described in some detail in Strassmeier et
al. (2018). The speciﬁc steps of image processing include bias
subtraction and variance estimation of the source images, super-
master ﬂat ﬁeld correction for the CCD spatial noise, scattered
light subtraction, deﬁnition of ´echelle orders, wavelength solu-
tion for the ThAr images, optimal extraction of image slicers and
cosmic spikes elimination, normalization to the master ﬂat ﬁeld
spectrum to remove CCD fringes and the blaze function, a global
2D ﬁt to the continuum, and the rectiﬁcation of all spectral or-
ders into a 1D spectrum.
3. Zeeman Doppler imaging
3.1. Stellar parameters of II Peg
Table 1 summarizes the adopted stellar input parameters for
II Peg. We basically adopt the same parameters already used
in the ZDI study by Ros´en et al. (2015) with some small
improvements. The most important changes are a lower pro-
jected rotational velocity of 21.6 km s−1 instead of 23 km s−1 and
a radial-tangential macroturbulence ζ of 3.6 km s−1 instead of
4.0 km s−1 as determined previously by Ottmann et al. (1998)
and Kochukhov et al. (2013).
The
new
Gaia
DR-2
parallax
for
II
Peg
(π=25.4046±0.0393 mas; distance 39.36±0.06 pc) converts
to a stellar radius of just 1.87±0.08 R⊙using Teﬀ=4750±100 K
and a maximum visual brightness Vmax=7.m30, along with
canonical solar values (Mbol=4.m83 and Teﬀ=5770 K) and the
assumption of zero interstellar absorption. On the contrary,
the minimum radius from the measured projected rotational
velocity (v sin i=21.6±0.5 km s−1) and the very precise rotation
period of 6.724 d is 2.87±0.07 R⊙. A likely inclination of the
rotational axis of 60◦± 10◦converts the minimum radius to a
likely radius of 3.3+1.0
−0.3 R⊙. The two radii determinations are
thus incompatible. Only if v sin i would be around 15 km s−1 or,
on the contrary, Teﬀ≈3500 K would the two radii agree, which
we can both safely exclude from our high-resolution spectra.
Only if a distance of ≈67 pc is assumed (or a visual magnitude
of 6.m0 instead of 7.m3) then the radii from the two methods
would be in agreement. This severe discrepancy already existed
for the Hipparcos parallax (23.62±0.89 mas) but appears now
2


## Page 3


Strassmeier, Carroll & Ilyin: II Peg with PEPSI
6400
6410
6420
6430
0.6
0.8
1
1.2
1.4
1.6
1.8
II Peg K2IV
Stokes V x10
null x50
Fig. 1. Spectra for an example wavelength region around 6400 Å. The bottom spectra are seven overplotted Stokes I spectra for one
spectrum per night (out of the 14 rotational phases of the full time series). Note that the rotation period of II Peg is 6.7 d. On top of
it are the same seven Stokes V spectra for the seven consecutive nights but shifted in relative intensity by 0.1 and enhanced in scale
by a factor of ten with respect to Stokes I. Time increases from bottom to top. The very top spectrum is the null spectrum enhanced
by a factor 50 with respect to Stokes I.
Table 1. Astrophysical properties of II Peg.
Parameter
Value
Based on
Classiﬁcation, MK
K2 IV
various
Eﬀective temperature, K
4750
Ros´en et al. (2015)
Log gravity, cgs
3.5
Ros´en et al. (2015)
v sin i, km s−1
21.6±0.5
this paper
Microturbulence, km s−1
2.0
Ros´en et al. (2015)
Macroturbulence, km s−1
3.6
this paper
Rotation period, d
6.7242078
=orbital period
Inclination, deg
60±10
this paper
Metallicity, [Fe/H]⊙
–0.25
Ros´en et al. (2015)
Distance, pc
39.36±0.06
Gaia DR-2
Radius, R⊙
1.87±0.08
from π, Teﬀ, Vmax
3.3+1.0
−0.3
from v sin i, i, Prot
Notes. π parallax, Teﬀeﬀective temperature, Vmax maximum brightness
in Johnson V; v sin i projected rotational velocity, i inclination of the
rotation axis with respect to the sky plane, Prot rotation period.
with higher weight due to the extremely precise Gaia parallax.
We have no readily explanation other than that the parallax
measures are fooled by the changing brightness center due to
II Peg’s huge spots. Because of this discrepancy we can not
convert our relative spot areas to absolute units.
The rotational phases φ in Table A.1 were calculated from
the orbital ephemeris given by Ros´en et al. (2015)
HJD = 2, 448, 942.428 + 6.7242078 × E ,
(1)
where the period is the orbital period and the zero point is a
time of maximum (positive) radial velocity. Note that photo-
metric period determinations (e.g., Rodon´o et al. 2000) always
agreed with the orbital period within their error bars and with
reasonable estimates for diﬀerential surface rotation.
3.2. iMAP speciﬁcs
All image reconstructions in this paper are done with the iMAP
code (Carroll et al. 2007, 2012). iMAP does not use a spher-
ical harmonics expansion for the magnetic ﬁeld description
but a physical 3D magnetic-ﬁeld vector (radial, meridional, az-
imuthal) per surface pixel. We also use an iterative regularization
where the step size and an appropriate stopping rule provides the
regularization of the inverse problem. The Stokes I and Stokes V
inversions are done simultaneously.
Our present inversion technique is thus penalty free and is
based on the Landweber iteration to minimize the sum of the
squared errors (for more details see Carroll et al. 2012 and ref-
erences therein). It can be written in a concise vector notation
as
1
2∥I(x) −O∥2 →min ,
(2)
where I is the synthetic model proﬁle over all spectral lines,
wavelengths, and rotational phases, and O is the corresponding
observation. The vector x contains all our free parameters of the
model, that is the temperature and the magnetic-ﬁeld vector for
each surface element. For the stopping rule, we use the respec-
tive largest standard error of the reconstructed Stokes proﬁles.
We note that the simultaneous inversion is dominated by the er-
ror in the Stokes V proﬁles.
The code can either perform multi-line inversions for a large
number of photospheric line proﬁles simultaneously or use a sin-
gle average SVD-extracted line proﬁle (again described in detail
3


## Page 4


Strassmeier, Carroll & Ilyin: II Peg with PEPSI
a.
b.
Fig. 2. Doppler images of II Peg. Panel a. Temperature image. Panel b. Magnetic-ﬁeld image. φ is the rotational phase. Spot
denominations in the top panel are: at phase φ=0.25 the large cool feature is called spot A; at phase φ=0.5 the equatorial cool
feature is called spot B and the high-latitude warm feature spot C; at phase φ=0.75 the cool feature is called spot D; and at phase
φ=0.00 the high-latitude warm feature is called spot E and the equatorial cool feature called spot F.
Radial
Latitude (deg)
90
60
30
0
-30
-60
0.00
0.25
0.50
0.75
1.00
360
270
180
90
0
Meridional
0.00
0.25
0.50
0.75
1.00
Longitude (deg)
360
270
180
90
0
Azimuthal
0.00
0.25
0.50
0.75
1.00
360
270
180
90
0
Field Strength [G]
2150
1075
0
-1075
-2150
Fig. 3. As in Fig. 2b but in Mercator-style projection and split into the three vector components. From left to right: radial-,
meridional-, and azimuthal component.
in Carroll et al. 2012). For the present application, we use the
former for Stokes I and the latter for Stokes V. Both approaches
apply our SVD technique. An eigenvalue decomposition of the
signal covariance matrix, that is a SVD of the observation ma-
trix, emphasizes the similarity of the individual Stokes proﬁles
and allows one to identify the most coherent and systematic fea-
tures. Incoherent features like noise and line blends etc. will be
dispersed along many dimensions in the transformed eigenspace.
For II Peg, we created SVD-denoised proﬁles from 1811 spectral
lines for the temperature inversion and SVD-averaged proﬁles
for the magnetic-ﬁeld inversion. We use the same 1811 spectral
lines for the Doppler image as well as for the Zeeman-Doppler
image. The diﬀerence is that the observation matrix for the inver-
sion in Stokes I still consist of the 1811 lines individually, each
one denoised with the use of all lines, while in Stokes V a single
SVD proﬁle (per phase) is used. The 1811 spectral lines were
selected upon line depths larger than 10% with respect to the lo-
cal continuum and as blend free as possible. The average wave-
length of the full line list is 5068 Å and the average Land´e factor
is 1.21. The individual Stokes-I proﬁle has a S/N of around 1000
per pixel as observed, and listed in Table A.1, but S/N≈13 000
per pixel per SVD-averaged proﬁle in Stokes V. A total of 14
rotational phases fairly equally distributed are available for the
inversion.
For the local line-proﬁle computation iMAP solves the radia-
tive transfer with the help of an artiﬁcial neural network (Carroll
et al. 2008). The atomic parameters for the line synthesis are
taken from the Vienna Atomic Line Database (e.g., Ryabchikova
et al. 2015). These are used with a grid of Kurucz ATLAS-9
model atmospheres (Castelli & Kurucz 2004) for local line pro-
ﬁles in 1D and in LTE. The grid covers temperatures between
4


## Page 5


Strassmeier, Carroll & Ilyin: II Peg with PEPSI
Table 2. Spots on II Peg in October 2017.
Spot
Long
Lat
∆T
A∆T
Bmax
ID
(◦)
(◦)
(K)
(% )
(G)
A
285
+50
+550
9.7
–2000 ...+1500
B
170
–5
+780
2.8
–2000
C
180
+50
–350
1.9
+1100
D
95
+40
+500
3.7
–1100 ...+1100
E
350
+35
–150
2.2
+500
F
25
–15
+150
2.2
+600
Notes. Longitudes and latitudes are given for the approximate spot cen-
ters. The spot temperature contrast, ∆T = Tphot −Tspot, refers to the
coolest (positive ∆T) and warmest (negative ∆T) part of the spot, while
spot area A is given for the entire size of the spot down to a threshold
contrast of 50 K in per cent of the visible hemisphere.
3500 K and 8000 K in steps of 250 K interpolated to the gravity,
metallicity, and microturbulence values from Table 1.
The stellar surface is partitioned into 5◦× 5◦segments,
resulting in 2592 surface pixels for the entire sphere. At
the average resolving power of λ/∆λ=130 000 (2.3 km s−1 at
6000 Å), and an average full width of the lines at continuum of
2 (λ/c) v sin i = 0.92 Å, we have 20 resolution elements across
the stellar disk of II Peg. This is twice as many compared to
previous maps based on, for example, CFHT and ESPaDOnS.
3.3. Results
Our ﬁnal DI and ZDI maps are shown in spherical projection
in Fig. 2 and in Mercator-style projection in Fig. 3. The line-
proﬁle ﬁts are given in the Appendix in Fig. A.1. The inversion
was ﬁrst done with Stokes I only. Its solution was then used as
the starting solution for the simultaneous Stokes-IV inversion.
iMAP performed a total of about 3000 iterations for the ﬁnal
solution.
3.3.1. Temperature map
In terms of surface area the temperature map is dominated by
a long and elongated cool spot group that extents via the po-
lar regions across adjacent longitudinal hemispheres, but possi-
bly bypasses the actual rotational pole itself. We call this fea-
ture spot A when looked at phase 0.25 (identiﬁed in Table 2).
Thus, no classical polar cap-like spot is seen during the epoch
of our observation but rather an appendage toward the pole. The
temperature of this spot complex appears diﬀerent in diﬀerent
places. While the average temperature is only ≈450 K cooler
than the unspotted photosphere, it is ≈550 K cooler in its cen-
tral parts and fades oﬀto ≈200 K cooler on its equatorial rim.
The connecting bridge around half of the visible pole is also
only ≈250 K cooler, but is still very well contrasted with respect
to the pole itself. The area of the entire feature A is 9.7% of
the visible hemisphere if we assume a likely temperature thresh-
old of 50 K with respect to the photospheric temperature. We
note that spot areas in this paper are computed with the formula
given in K¨unstler et al. (2015) and based on a maximal contrast
of (∆T)max = (Tphot −Tspot)max = 780 K in units of the visible
hemisphere.
In terms of contrast the DI map is dominated by a pair of
relatively round and compact-looking spots of which one is very
cool (∆T≈+780 K) and the other very warm (∆T≈–350 K). The
cool feature appears right on the stellar equator while the warm
feature is at a latitude of +50◦. Their respective central longi-
tudes are only diﬀerent by 10◦in the sense that the warm feature
is leading in the direction of stellar rotation. The relative areas
are 2.8% and 1.9% for the cool and the warm spot, respectively.
We call this pair spot B (the cool one) and spot C (the warm
one). These two features will later be of central interest. Both
spots appear isolated from the other spotted regions and are re-
constructed with relatively well-deﬁned edges compared to other
features.
A fourth feature, spot D, is located near a longitude of ≈95◦
(phase ≈0.8). It appears elongated and tilted with respect to a
meridional line and could even be seen as an extension of spot A
via the pole into the adjacent opposite hemisphere. Its center
near a latitude of +40◦is reconstructed with a temperature con-
trast of ≈+500 K and an area of 3.7% if considered an isolated
feature. This spot dominates the stellar disk when seen at phase
0.75 in Fig. 2a.
The remaining surface features are all comparably weak, yet
still signiﬁcant in terms of the achieved χ2 statistics. Note that
the proﬁle-ﬁt level approaches the S/N of the data of ≈1000 per
line to a very high degree (see Sect. 4.1). In an ideal world,
this converts to an average temperature threshold of ≈10 K (see
Carroll et al. 2012). Remaining conservative, we estimate our
threshold to be closer to 30 K, mostly limited by the imperfect
phase sampling and the still limiting spatial resolution in spite of
14 phases with 20 resolving elements across the disk per proﬁle.
Nevertheless, two weak features shall be mentioned here: the
warm spot E with an area of 2.2% and a contrast of ∆T≈–150 K,
and the cool suspiciously stretched spot F, also with an area of
2.2%, but a maximum temperature contrast of ∆T≈+150 K. It
may be worth mentioning that the two warm features on the sur-
face of II Peg (spots C and E) are almost exactly 180◦apart in
longitude and approximately at the same latitude.
3.3.2. Magnetic ﬁeld map
The visible polar area appears with a spatially oﬀset positive
ﬁeld of strength up to 1200 G, and is well correlated with a
similarly oﬀset cool region in the temperature map. The actual
rotational pole is reconstructed with less than half of this ﬁeld
density (≈500 G; see Fig. 3), if at all, because the pole carries in
principle no Doppler signal and positional errors are then largest.
The ﬁeld gradually converts to negative polarity at the adjacent
lower latitudes at around ≈+60◦where the polar ﬁeld becomes
comparably weak and never more than (–)100–200 G. The ﬁeld
there is likely too weak and too complex that the Stokes IV ZDI
could capture its meridional or azimuthal components. The lon-
gitudinally adjacent side of the polar asymmetry (by nearly ex-
actly 180◦or at rotational phase ≈0.4) is where the high-latitude
warm spot is reconstructed in the temperature map. This com-
plexity prevents a clear statement of the pole’s true magnetic
morphology, that is whether it is also of bipolar or of singular
polarity nature. Our reconstruction of the polar region gives an
upper limit of the actual ﬁeld density in a region of, say, 10◦ra-
dius around the pole of around +1 kG. We can not exclude the
possibility of a mixed morphology with a weak negative polarity
though.
In terms of ﬁeld density, or strength, the map is dominated
by the cool mixed-polarity spot A and the cool negative-polarity
spot B. The warm positive-polarity spot C with its peak value of
+1100 G is contrasted by the cool spots A and B with peak val-
ues of −2000 G. Most surprisingly, spots B & C seem to form an
opposite polarity pair at almost identical longitude but diﬀerent
latitude and appear to be the respective coolest and warmest fea-
5


## Page 6


Strassmeier, Carroll & Ilyin: II Peg with PEPSI
tures at that time on II Peg. We are very conﬁdent of their reality
because the two features are widely separated in latitude, were
also reconstructed in the magnetic map, and the code has basi-
cally no unconstrained surface region due to incomplete phase
coverage. If it were a typical artifact, for example caused by a
faulty single line proﬁle, the two hot-cool features would appear
close together or even adjacent in latitude because the code tries
to ﬁt the faulty proﬁle without bothering the other phases too
much.
The cool and large spot A is the most complex one and
is reconstructed from Stokes V with a detailed multi-polarity
morphology. Four individual polarity regions are identiﬁed with
peak ﬁeld densities between +400 G at the rotationally follow-
ing side, –1100 G in its central part, and +800 G at the leading
side. The coolest part of it is, as expected, also the strongest in
terms of ﬁeld density, and negative in polarity. The positive-ﬁeld
region of the leading side of spot A is close to but not related
with the second warm feature (spot E, φ≈0.0) which is of same
polarity but comparably weak (≤200 G). The ZDI map reveals
a truly complex ﬁeld morphology in this region (which is likely
only the tip of an iceberg). Although all features shown in Fig. 2b
are signiﬁcant within the stated ZDI assumptions, the very weak
magnetic feature are of course the most uncertain ones. Whether
the one or the other of these weak features is an artifact can
not be decided based on our data alone and we therefore add
some caution to their interpretation. The cooler part of the large
spot D appears of solely negative polarity (≈–1000 G) while the
weaker and high-latitude part of it appears to be of positive po-
larity (≈+1000 G).
Overall, the high ﬁeld densities strongly correlate with fea-
tures in the temperature map. The coolest spots are typically
the regions with highest ﬁeld density. On the contrary, there are
a few very weak (but still signiﬁcant) radial ﬁeld reconstruc-
tions even when no feature is seen in the temperature domain.
For example, the cool spot F in the temperature map is recon-
structed with positive polarity of ≈300 G and has a negative-
polarity counterpart of same strength at higher latitudes, which
itself has no counterpart in the temperature map. Another such
feature is the appendage of spot A toward the stellar equator at
ℓ≈230◦where a negative polarity of strength ≈300 G is recon-
structed on the equator but no feature is seen in the temperature
image below a latitude of +30◦. At this point we estimate our
average local ﬁeld-density threshold to be approximately ±50 G.
4. Discussion and conclusions
Here we discuss the robustness of our Stokes IV maps and its
magnetic-ﬁeld morphology, and the possible explanations and
consequences for the solar-stellar connection.
4.1. Image robustness
Figure A.1 shows the reconstructed set of Stokes V and Stokes
I proﬁles compared with the SVD-averaged data for all 14 rota-
tional phases. The standard errors are provided by the Bootstrap
method with a re-sampling number of 1000. For each velocity
bin, we obtained an estimate of the standard error which is con-
densed into a mean standard error averaged over the velocity do-
main. Its value is 9.2 10−4 for Stokes I and 7.6 10−5 for Stokes V,
both values are basically identical with the respective inverse
S/N due to the inversion stopping rule. To summarize, our ar-
guments in favor of the robustness of the current ZDI map rests
on the following items.
Initial data quality. Even the stronger CP signal in spectral
lines rarely exceeds 1% of the continuum intensity in super ac-
tive stars like II Peg. Kochukhov et al. (2013) ﬁnds a Stokes V
signature at the 2–3σ conﬁdence level in only a few of the
strongest spectral lines of II Peg in SOFIN data from the 2.4m
NOT as well as in ESPaDOnS data from the 3.6m CFHT. Our
PEPSI spectra in Fig. 1 from the 11.8m LBT show Stokes V sig-
natures at the 10σ level and were obtained with a twice as high
a spectral resolution than previous maps of II Peg. Given that
the phase sampling has no signiﬁcant voids, it resolves the stel-
lar surfaces also twice as good. A simple test conﬁrms this. We
de-convolved the PEPSI data with an instrumental proﬁle equal
to the R=65 000 spectral resolution as in previous ZDI work on
II Peg and then compared the map with that from the present
data (Appendix Fig. A.2). We see larger and less cool features
in the lower resolution temperature map as well as less struc-
tured features of lower ﬁeld strength in the magnetic map. Both
diﬀerences, in area and in ﬁeld strength, are approximately at
the 10–20% level. We recently found a similar impact with a
comparable test for the R =250 000 Stokes I spectra of EK Dra
(J¨arvinen et al. 2019).
Simultaneous T and B solution. In this paper, we had pro-
ceeded with an alternating minimization approach. That is, we
started the magnetic inversion with an already pre-iterated tem-
perature solution and then proceeded with the ﬁrst magnetic in-
version. After that, each iteration for the temperature was fol-
lowed by an inversion for the magnetic ﬁeld vector, which then
used the information of the previous iteration of the tempera-
ture minimization. Therefore, the inversion starts with the step
along the temperature gradient vector followed by a step along
the magnetic gradient vector as laid out in Eq. 28 in Carroll et
al. (2012). A total of 3000 such steps were performed. We found
that the dependence of DI on the magnetic inversion is not strong
while the dependence of ZDI on the temperature inversion is
strong and, if completely neglected, leads to a non-trivial scal-
ing of the Stokes V proﬁle amplitudes and widths and thus to a
false ZDI map (Carroll et al. 2012, Ros´en & Kochukhov 2012).
We also had done a test with diﬀerent starting solutions for the
alternate inversion. Instead of a pre-iterated initial temperature
image, we used a blank surface with the eﬀective temperature as
the starting image for the Stokes V inversion. The outcome was
identical but more iterations were needed.
Penalty-free inversion. Another important feature of our DI
and ZDI is its iterative regularization. This allows us to make the
inversion penalty free (for the expense of many iterations and
thus CPU time). It means that we do not impose any constraints
on the scale of the magnetic ﬁeld, that is we do not indirectly pre-
fer the large-scale surface structure over the small-scale structure
by deﬁnition. The latter is the case for the previous ZDI inver-
sions (Ros´en et al. 2015) due to their adopted l2 penalty function
(l is the angular harmonic expansion coeﬃcient that describes
the geometric scale of the magnetic ﬁeld). In iMAP, only the
surface gradient vector from one iteration to the next is used for
the regularization.
Magnetic ﬁeld density. How does one convert the observed
Stokes V signal into a local magnetic ﬁeld density (strength)?
This is a non-trivial question and, so far, was implicitly answered
through the assumption of the weak-ﬁeld approximation (Stenﬂo
1994, Carroll & Strassmeier 2014) from which we derive the
eﬀective and apparent longitudinal magnetic ﬁeld. Due to the
3D vector description of B in iMAP, we do not need a conver-
sion from harmonic expansion coeﬃcients. We therefore believe
that the radial-ﬁeld densities reconstructed by iMAP from just
Stokes IV are closer to reality than previous Stokes IV inver-
6


## Page 7


Strassmeier, Carroll & Ilyin: II Peg with PEPSI
sions and indirectly conﬁrm the enhanced radial ﬁeld strengths
on II Peg once Q&U are added (Ros´en et al. 2015). At this point
we can not make a more quantitative statement regarding the
even stronger meridional and azimuthal ﬁeld enhancement from
LP.
4.2. Magnetic surface morphology
We reconstruct surface features with a radial-ﬁeld density of up
to −2000 G and +1500 G, a meridional ﬁeld density of up to
±500 G, and an azimuthal ﬁeld density of up to −500 G. This is
to be compared to previous Stokes IV results of II Peg which re-
constructed features of approximately ±600 G. However, Ros´en
et al. (2015) found that the peak radial-ﬁeld densities doubled
when the linear component of the Stokes vector was included in
their inversion, and even quadrupled for the other two compo-
nents. Their IQUV-reconstructed peak local-ﬁeld densities were
therefore 1.3, 2.1 and 2.5 kG for the radial, meridional, and az-
imuthal ﬁeld components, respectively. While the radial compo-
nent of Ros´en et al.’s and ours is comparable the meridional and
azimuthal reconstructions are many times stronger than ours.
The total magnetic energy is with 99% almost exclusively in
the radial component (with a magnetic ﬂux of 86%) while the
meridional (0.6%) and azimuthal (0.4%) components are com-
parably weak. The ﬁeld distribution is 53% axisymmetric and
47% non-axisymmetric.
Ros´en et al. (2015) argued that cross-talk between the ra-
dial and meridional ﬁeld components can occur when only cir-
cular polarization is used in the magnetic inversion. This may be
because Stokes V is formally only sensitive to the line-of-sight
component of the magnetic ﬁeld. In Stokes IV maps the radial
component appears always to be the strongest of the three while
it is the weakest in the IQUV inversion of Ros´en et al. (2015).
We can not decide whether this is due to the missing linear polar-
ization in our case, or related to the l2 penalty function applied in
the inversion by Ros´en et al.. However, we have no analog from
the Sun to compare with, or any readily physical eﬀect, where
the ﬁeld density of a ﬁeld parallel to the solar or stellar surface
is higher than the radial-ﬁeld density. We also note that the polar
features in the magnetic maps by Ros´en et al. changed polar-
ity depending on whether Stokes IV or IQUV were used for the
inversion.
We compute a 3D magnetic-ﬁeld extrapolation based on our
ZDI map as the inner boundary condition. An outer boundary
condition is set as the potential ﬁeld source surface (PFSS) and
is deﬁned through the Alfv´en radius where the kinetic energy
density equals the magnetic energy density. We set this source
surface to three stellar radii. For the ﬁeld extrapolation we use
the potential ﬁeld source surface model of Altschuler & Newkirk
(1969) and Schatten et al. (1969). This model assumes that the
ﬁeld is potential and that the ﬁeld lines are opened by the kinetic
energy of the hot coronal gas at the source surface. For the ac-
tual calculation we use the SolarSoft PFSS package (Schrijver
& DeRosa 2003) that takes the radial component of the pho-
tospheric magnetic ﬁeld from the ZDI map as input. Figure 4
shows the extrapolations for the far-surface ﬁeld (< 2.2 R⋆) and
the near-surface ﬁeld (< 1.2 R⋆) and for one and the same rota-
tional phase. One can see that there are more closed ﬁeld lines
than open ﬁeld lines, in particular the closer to the stellar surface
one has chosen the outer boundary. Below ≈0.1 stellar radii the
extrapolation becomes unreliable because it is based mostly on
radial ﬁelds on the stellar surface.
4.3. Spot origins
Our most surprising result is the existence of a pair of well-
deﬁned compact warm and cool spots of high magnetic-ﬁeld
density but of opposite polarity; positive for the warm spot, neg-
ative for cool spot (spots C and B). A second warm spot, al-
though less signiﬁcant in terms of temperature contrast, appears
also with positive polarity but consequently with somewhat low-
ered ﬁeld density when compared to the dominating warm fea-
ture. The remaining cool spots on II Peg appear with intermin-
gled polarities.
Such a widely separated, bi-polar and cool/warm, photo-
spheric feature has no direct solar analog. Cool solar spots are
always formed due to a suppression of convection (Biermann
1938) while warm solar spots, called plages or faculae, are
lower-density regions in the chromosphere usually physically lo-
cated somewhat above the cool photospheric spots. In simple and
well isolated active regions spots and plages are conﬁned by the
same magnetic ﬁeld (e.g., Solanki 1999). However, solar surface
reality is also that there are no active regions of apparently single
polarity, only very young pores can appear with a single polarity
(the other polarity still hidden in the surrounding convective lay-
ers). Moreover, sunspot polarities invert in the two hemispheres
as well as in subsequent activity cycles (Hale’s law). On II Peg,
the bipolar feature (spots B&C) spans a latitude range of 50◦,
thus almost an entire hemisphere on the visible stellar surface.
Its cool spot is located almost exactly on the stellar equator while
the warm spot is at +50◦latitude. It resembles more a simpliﬁed
solar coronal magnetic loop as seen in extreme UV images and
movies (e.g., Schrijver & DeRosa 2003) but enhanced in dimen-
sions by a factor 10 or so.
Figure 5ab shows two excerpts from the magnetic-ﬁeld ex-
trapolation around the spot pair B&C and spot D, respectively.
The B&C pair consists of a warm (spot C) and a cool spot (B)
well separated, while spot D appears as a single cool spot in the
DI but is also reconstructed with dual polarity in the ZDI map
just as the well-separated pair B&C. Yet their connecting loop
structure appears to be of similar height and geometry and is
part of an even larger loop pattern across the entire hemisphere
(Fig. 4a).
We propose the following simple scenario to explain both
the existence of warm and cool features and their bi-polarity.
The ﬁeld lines between spots B and C, or A and E, recon-
nect and form a closed loop. Within this loop electrons must
be stripped from the negative polarity (on II Peg always a cool
spot) and be accelerated toward the positive polarity (on II Peg
always a warm spot). Eventually they shock near the loop end
and form a hot plasma that heats the impact region beneath
it. This region is then even visible in the optically-thin photo-
spheric absorption lines as a warm spot in contrast to the cool
background photosphere. This qualitative picture resembles very
much the siphon ﬂow model put forward to explain the Evershed
eﬀect in sunspots (e.g., Montesinos & Thomas 1997). However,
Warnecke et al. (2017) concluded that a one-dimensional coro-
nal loop model, or a force-free extrapolation, cannot capture the
complexity of the magnetic ﬁeld in such a loop. Their simula-
tions show that some ﬁeld lines within the loop appear with twist
angles of even 90◦which would likely lower the electron accel-
eration rate between the polarities and possibly even prevent a
classical shock front.
Some support for our loop scenario also comes from the
Balmer-line behavior. Figure 6 shows that when the warm fea-
ture (spot C) is near crossing the central meridian the Hα line
shows the strongest and widest residual emissions, this is also
7


## Page 8


Strassmeier, Carroll & Ilyin: II Peg with PEPSI
a.
b.
Fig. 4. Magnetic-ﬁeld extrapolation. Spherical projection for rotational phase 0.65. Open ﬁeld lines are depicted in color (magenta
negative polarity, red positive polarity), closed loops are in white. The ZDI map is color coded as in Fig. 2b. a. Far-surface ﬁeld with
closed loops that reach a height of 2.2 stellar radii. b. Near-surface ﬁeld with closed loops that reach a height of 1.2 stellar radii.
a.
b.
Fig. 5. Loop structure for two bipolar spot pairs on II Peg. Shown
are close-ups from the potential ﬁeld extrapolation. a. Spots
B&C (phase 0.65). b. Spot D (phase 0.65)
the case for the other Balmer lines from Hβ through Hϵ. Strongly
variable Ca ii H&K, IRT, and He i emission is evident in the spec-
tra as well. The width of the Hβ to Hϵ core emissions is between
2–3 Å (on average 150 km s−1) but 13 Å for Hα. The Balmer
Hα origin is clearly more complex, as initially already indicated
by its non-Gaussian shape and large equivalent width of –4.2 Å.
Prior to the spot-C central-meridian passage its blue proﬁle wing
becomes more extended than the red wing while the central self
reversal remains. All this indicates that most of the Balmer pro-
ﬁle is formed locally far above the stellar photosphere, partly
in the gas channeled along magnetic ﬁeld lines behind the (as-
sumed) siphon shock. Fairly constant He i 5876-Å emission dur-
ing all phases suggests continuously existing high temperatures
well above 10 000 K.
Besides the one particular pair of a warm and a cool spot,
the majority of the cool regions on II Peg appear containing both
polarities, just like we would expect from a scaled-up solar ac-
tive region. It is thus also likely that these features, in particu-
Fig. 6. Hα line-proﬁles changes during the time of the Doppler
imaging (wavelengths in Å). The blue-colored line proﬁle is for
phase 0.348 when the hot/cool spot pair B&C is close to crossing
the stellar central meridian. The red-colored line proﬁle is the
proﬁle at the preceding phase 0.198 while the proﬁle in-between
these two proﬁles (thin line) is for phase 0.386.
lar the multi-polar gigantic spot A, are regions where the tur-
bulent convective motion is suppressed and the ﬂow of energy
partly blocked or redirected. Therefore, the surface of II Peg can
host photospheric spots whose temperature originates from two
rather diﬀerent mechanisms at the same time, one related to a
shock in a siphon-type ﬂow and the other from the suppressed
convection.
8


## Page 9


Strassmeier, Carroll & Ilyin: II Peg with PEPSI
4.4. Relation to the other binary component?
The pair of warm and cold spots (spots B&C) crosses the stel-
lar central meridian very near phase 0.5, while the other warm
feature (spot E) crosses the meridian very near 0.0. This align-
ment may be by chance but is within expected errors exactly
180◦in separation, and at two distinct orbital locations. Because
our phase zero point is a point of largest positive radial velocity,
the two phases 0.0 and 0.5 refer to the two phases of quadrature.
This is at least suggestive for a relation with the orbital posi-
tion of the (unseen) secondary star. Because the orbit is circular
there is no particularly exposed position in terms of tidal eﬀects.
The only plausible adhoc explanation would be a magnetic link
between the two stellar components (that would trigger ﬂare ac-
tivity). Clearly, this requires further evaluation in future work.
5. Conclusions and summary
Although observed many times in the past, II Peg remains a stel-
lar system with surprises. We found now good evidence that
warm and cool features coexist on its surface. However, the
warm feature(s) on II Peg are likely not solar-analogs of plage
or faculae-like features but are spatially well separated from
the cool features. As such they are more like the foot points of
magnetic-ﬂux loops than a single up-scaled active region as for
the Sun. Our ZDI map showed that warm features on II Peg are
of positive polarity, at least at the time of our observations, and
that adjacent cool spots are of negative polarity. Other large cool
areas were reconstructed with a mixed-polarity morphology. We
interpret the loop connection to act like a siphon ﬂow with a
shock front that heats the local atmosphere near the loop end
and within a certain height range. When observed via optically-
thin photospheric absorption lines, these regions then appears as
warm spots. The simultaneous Hα line-proﬁle variations are in-
dicative of a mass ﬂow between the two polarities, prematurely
assuming a plasma ﬂow from negative to positive polarity, at
least for the spot pair B&C. The ﬁeld density, or strength, is
dominated by far by the radial-ﬁeld component reaching val-
ues of up to approximately ±2 kG. A comparably weak merid-
ional and azimuthal component (≈±300–500 G) is detected in
our ZDI whenever opposite polarity regions are in close spatial
vicinity. This is expected if the respective ﬁeld lines indeed con-
nect through loop-like structures as shown by our potential-ﬁeld
source-surface extrapolations. Future line-proﬁle inversions will
include also the LP components of the Stokes vector, as com-
monly used for high-resolution solar-surface inversions (e.g.,
Ruiz Cobo & del Toro Iniesta 1992) and pioneered for stars like
II Peg by Ros´en et al. (2015). Finally, we note again the severe
radius discrepancy from the parallax on the one hand and from
the stellar rotation on the other hand.
Acknowledgements. LBT Corporation partners are the University of Arizona
on behalf of the Arizona university system; Istituto Nazionale di Astroﬁsica,
Italy; LBT Beteiligungsgesellschaft, Germany, representing the Max-Planck
Society, the Leibniz-Institute for Astrophysics Potsdam (AIP), and Heidelberg
University; the Ohio State University; and the Research Corporation, on behalf
of the University of Notre Dame, University of Minnesota and University of
Virginia. It is a pleasure to thank the German Federal Ministry (BMBF) for the
year-long support for the construction of PEPSI through their Verbundforschung
grants 05AL2BA1/3 and 05A08BAC as well as the State of Brandenburg for the
continuing support of AIP and PEPSI (see https://pepsi.aip.de/). This work has
made use of the VALD database, operated at Uppsala University, the Institute of
Astronomy RAS in Moscow, and the University of Vienna.
This research has made use of NASA’s Astrophysics Data System and of CDS’s
Simbad database which we both gracefully acknowledge.
References
Altschuler, M. D., & Newkirk, G. Jr. 1969, SP, 9, 131
Berdyugina, S., Berdyugin, A., Ilyin, I., & Tuominen, I. 1998, A&A, 340, 437
Berdyugina, S., Berdyugin, A., Ilyin, I., & Tuominen, I. 1999, A&A, 350, 626
Biermann, L. 1938, AN, 264, 361
Byrne, P. B., Doyle, J. G., Brown, A., Linsky, J. L., & Rodono, M. 1987, A&A,
180, 172
Carroll, T. A., Kopf, M., Ilyin, I., & Strassmeier, K. G. 2007, AN, 328, 1043
Carroll, T. A., Kopf, M., & Strassmeier, K. G. 2008, A&A, 488, 781
Carroll, T. A., & Strassmeier, K. G. 2014, A&A, 563, A56
Carroll, T. A., Strassmeier, K. G., Rice, J. B., & K¨unstler, A. 2012, A&A, 548,
A95
Castelli, F., & Kurucz, R. L. 2004, ArXiv Astrophysics e-prints [astro-
ph/0405087]
Donati, J.-F. & Landstreet, J. 2009, ARA&A, 47, 333
Donati, J.-F., Semel, M., & Rees, D. E. 1992, A&A, 265, 669
Doyle, J. G., Kellett, B. J., Byrne, P. B. et al. 1991, MNRAS, 248, 503
Gu, S.-H., Tan, H.-S., Wang, X.-B., & Shan, H.-G. 2003, A&A, 405, 763
Hackman, T., Mantere, M. J., Lindborg, M. et al. 2012, A&A, 538, A126
Hatzes, A.P. 1995, in K. G. Strassmeier (ed.), Poster proceedings of IAU Symp.
176, University of Vienna, p.87
Ilyin, I. 2000, PhD Thesis, Univ. of Oulu, Finland
Ilyin, I. 2012, AN, 333, 213
J¨arvinen, S. P., Strassmeier, K. G., Carroll, T. A., Ilyin, I., & Weber, M. 2019,
A&A, 620, A162
Kochukhov, O., Mantere, M. J., Hackman, T., & Ilyin, I. 2013, A&A, 550, A84
K¨unstler, A., Carroll, T. A., & Strassmeier, K. G. 2015, A&A, 578, A101
Lindborg, M., Korpi, M. J., Hackman, T., et al. 2011, A&A, 526, A44
Montesinos, B., & Thomas, J. H. 1997, Nature, 390, 485
Mutel, R. L., & Lestrade, J. F. 1985, AJ, 90, 493
Ottmann, R., Pfeiﬀer, M. J., & Gehren, T. 1998, A&A, 338, 661
Reiners, A. 2012, Living Reviews in Solar Physics, 9
Rodon´o, M., Messina, S., Lanza, A. F., Cutispoto, G., & Teriaca L. 2000, A&A,
358, 624
Ros´en, L. & Kochukhov, O. 2012, A&A, 548, A8
Ros´en, L., Kochukhov, O., & Wade, G. A. 2013, MNRAS, 436, L10
Ros´en, L., Kochukhov, O., & Wade, G. A. 2015, ApJ, 805, 169
Rucinski, S. M. 1977, PASP, 89, 280
Ruiz Cobo, B., & del Toro Iniesta, J. C. 1992, ApJ, 398, 375
Ryabchikova, T., Piskunov, N., Kurucz, R. L., et al. 2015, Phys. Scr, 90, 054005
Schatten, K., Wilcox, J., & Ness, N. 1969, SP, 6, 442
Schrijver, C. J., & DeRosa, M. L. 2003, SP, 212, 165
Schrijver, C. J., Mewe, R., & Walter, F. M. 1984, A&A, 138, 258
Semel, M. 1989, A&A, 225, 456
Solanki, S. K. 1999, in Butles, C. J. & Doyle, J. G. (eds.), ASPC, 158, p.109
Stenﬂo, J. O. 1989, A&ARv, 1, 3
Stenﬂo, J. O. 1994, Solar Magnetic Fields: Polarized Radiation Diagnostics,
Astrophys. Space Sci. Lib. (Dordrecht; Boston: Kluwer Academic
Publishers), p. 189
Strassmeier, K. G. 2009, A&ARv, 17, 251
Strassmeier, K. G., Ilyin, I., J¨arvinen, A., et al. 2015, AN, 336, 324
Strassmeier, K. G., Ilyin, I., Weber, M., et al. 2018, Proc. SPIE, 10702, 1070212
Strassmeier, K. G., Ilyin, I., & Steﬀen, M. 2018, A&A, 612, A44
Vogt, S. S. 1979, PASP, 91, 616
Vogt, S. S. 1980, ApJ, 240, 567
Wang, Y.-M., & Sheeley, N. R. 1992, ApJ, 392, 310
Warnecke, J., Chen, F., Bingert, S., & Peter, H. 2017, A&A, 607, A53
Weber, M. 2004, PhD thesis, Univ. Potsdam
Xiang, Y., Gu, S.-H., Collier Cameron, A., & Barnes, J. R. 2013, MNRAS, 438,
2307
Zboril, M. 2003, in N. Piskunov, W.W. Weiss, and D.F. Gray. (eds.), Poster pro-
ceedings of IAU Symp. 210, Uppsala University, p. D9
Appendix A: Additional plots and tables
9


## Page 10


Strassmeier, Carroll & Ilyin: II Peg with PEPSI
Table A.1. Log of PEPSI observations.
Date
HJD
Total exp.
Stokes
CD III
CD V
φ
(UT)
(2,458,000+)
(min)
∆λ (Å)
S/N
∆λ (Å)
S/N
(Eq. 1)
14/10/2017
40.6288130
20
IV
4800 - 5441
596
6278 - 7419
1202
0.052
15/10/2017
41.6140278
20
IV
4800 - 5441
633
6278 - 7419
1230
0.198
16/10/2017
42.6196759
20
IV
4800 - 5441
514
6278 - 7419
1025
0.348
16/10/2017
42.8734476
25
IV
4800 - 5441
485
6278 - 7419
969
0.386
10/10/2017
36.6751209
25
IV
4800 - 5441
397
6278 - 7419
791
0.464
10/10/2017
36.8003129
20
IV
4800 - 5441
485
6278 - 7419
965
0.482
10/10/2017
36.9388681
20
IV
4800 - 5441
361
6278 - 7419
816
0.503
11/10/2017
37.8191406
15
IV
4800 - 5441
564
6278 - 7419
1064
0.634
11/10/2017
37.9113733
20
IV
4800 - 5441
565
6278 - 7419
1160
0.648
12/10/2017
38.6196109
20
IV
4800 - 5441
554
6278 - 7419
1128
0.753
12/10/2017
38.8294253
20
IV
4800 - 5441
632
6278 - 7419
1278
0.784
12/10/2017
38.9365060
20
IV
4800 - 5441
268
6278 - 7419
723
0.800
13/10/2017
39.6124016
20
IV
4800 - 5441
608
6278 - 7419
1228
0.901
13/10/2017
39.8910861
20
IV
4800 - 5441
470
6278 - 7419
1089
0.942
Notes. The second column gives the heliocentric Julian date for the time of mid exposure, the third column is the total exposure time for both
sub-exposures. S/N is per pixel and is the average from within the two wavelength regions ∆λ. The last column is the rotational phase based on
the ephemeris in Eq. (1).
10


## Page 11


Strassmeier, Carroll & Ilyin: II Peg with PEPSI
Stokes I
−50
0
50
Velocity [km/s]
1.0
1.2
1.4
1.6
1.8
2.0
I/IC 
0.052
0.198
0.348
0.386
0.464
0.482
0.503
0.634
0.648
0.753
0.784
0.800
0.901
0.942
Stokes V
−50
0
50
Velocity [km/s]
0.000
0.005
0.010
0.015
0.020
0.025
0.030
V/IC 
0.052
0.198
0.348
0.386
0.464
0.482
0.503
0.634
0.648
0.753
0.784
0.800
0.901
0.942
Fig. A.1. The observed (black dots) and inverted (red lines) line proﬁles for the temperature Doppler image (left) and the magnetic-
ﬁeld image (right). Proﬁles are labeled with their respective phases. Rotation advances from bottom to top.
11


## Page 12


Strassmeier, Carroll & Ilyin: II Peg with PEPSI
a. Original map with R=130 000
b. Map with R=65 000
c. Diﬀerence map
Fig. A.2. Zeeman Doppler images from data of diﬀerent spectral resolution. Panel a: based on the original data with a spectral
resolution of R = 130 000 (as in Fig. 2b). Panel b: based on the same data but downgraded to a spectral resolution of 65 000. Panel c:
diﬀerence map a −b.
12

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1902_11201v1_warm_and_cool_starspots_with_opposite_polarities_a_high_resolution_zeeman_doppl
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1902_11201V1_WARM_AND_COOL_STARSPOTS_WITH_OPPOSITE_POLARITIES_A_HIGH_RESOLUTION_ZEEMAN_DOPPL.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

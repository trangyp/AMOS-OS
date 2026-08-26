---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1710.03336v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1710.03336v1_Ammonia_in_Jupiter_s_troposphere_from_high-resolution_5-_textmu_m_spectroscopy

> Source: 1710.03336v1_Ammonia_in_Jupiter_s_troposphere_from_high-resolution_5-_textmu_m_spectroscopy.pdf

> Pages: 15

---


## Page 1


arXiv:1710.03336v1  [astro-ph.EP]  9 Oct 2017
Manuscript accepted for publication in Geophysical Research Letters
Ammonia in Jupiter’s troposphere from high-resolution 5-µm
spectroscopy
Rohini S. Giles1, Leigh N. Fletcher2, Patrick G. J. Irwin3, Glenn S. Orton1and James A.
Sinclair1
1Jet Propulsion Laboratory / California Institute of Technology, 4800 Oak Grove Drive, Pasadena, CA 91109, USA
2Department of Physics and Astronomy, University of Leicester, University Road, Leicester, LE1 7RH, UK
3Atmospheric, Oceanic & Planetary Physics, Department of Physics, University of Oxford, Clarendon Laboratory, Parks
Road, Oxford, OX1 3PU, UK
Key Points:
• Jupiter’s tropospheric ammonia abundance is studied using high-resolution 5-µm
spectroscopy from VLT/CRIRES
• The ammonia abundance decreases with altitude in the 1–4 bar pressure range at all
latitudes
• There is a strong localised enhancement in ammonia abundance at 4-6◦N
Corresponding author: R. S. Giles, rohini.s.giles@jpl.nasa.gov
–1–


## Page 2


Manuscript accepted for publication in Geophysical Research Letters
Abstract
Jupiter’s tropospheric ammonia (NH3) abundance is studied using spatially-resolved 5-µm
observations from CRIRES, a high resolution spectrometer at the European Southern Obser-
vatory’s Very Large Telescope. The high resolving power (R=96,000) allows the line shapes
of three NH3 absorption features to be resolved. We ﬁnd that within the 1–4 bar pressure
range, the NH3 abundance decreases with altitude. The instrument slit was aligned north-
south along Jupiter’s central meridian, allowing us to search for latitudinal variability. There
is considerable uncertainty in the large-scale latitudinal variability, as the increase in cloud
opacity in zones compared to belts can mask absorption features. However, we do ﬁnd evi-
dence for a strong NH3 enhancement at 4–6◦N, consistent with a localised ‘ammonia plume’
on the southern edge of Jupiter’s North Equatorial Belt.
1 Introduction
As a condensible species in Jupiter’s atmosphere, ammonia (NH3) plays an important
role in understanding the planet’s meteorology. At deep pressures in the atmosphere, the
NH3 abundance may be well-mixed, but the vertical proﬁle becomes complex at higher al-
titudes. Assuming solar abundances, a typical cloud condensation model from Atreya et al.
[1999] suggests that NH3 will start to dissolve in liquid water at ∼5.7 bar, and then will form
two distinct cloud decks of solid NH4SH and solid NH3 at 2.2 and 0.7 bar respectively. At
even higher altitudes, gaseous NH3 will be further depleted by photolysis due to UV solar ra-
diation [Atreya et al., 1977]. Because the volume mixing ratio varies with altitude, NH3 acts
as a tracer for atmospheric dynamics and observations of the spatial distribution of NH3 can
be used to constrain global circulation patterns [Showman and de Pater, 2005].
NH3 absorption features have been observed in jovian spectra across a wide range of
wavelengths. Diﬀerent spectral regions are sensitive to diﬀerent altitudes in Jupiter’s at-
mosphere and can be combined to constrain the vertical proﬁle of NH3. In the infrared,
there are NH3 features at 45 µm, 10 µm and 5 µm which probe the upper and middle parts
of the troposphere [Kunde et al., 1982; Irwin et al., 1998; Fouchet et al., 2000]. Addition-
ally, NH3 is a signiﬁcant contributor to the microwave radiation from the planet; from the
ground, this spectral region has been used to probe down to the 10-bar level in Jupiter’s at-
mosphere [de Pater et al., 2001] and the Microwave Radiometer (MWR) on the Juno mission
is sensitive to the NH3 abundance at pressures of up to 100 bar [Li et al., 2017].
–2–


## Page 3


Manuscript accepted for publication in Geophysical Research Letters
Previous 5-µm studies of Jupiter’s NH3 abundance have been conducted using a range
of data sources, including the Kuiper Airborne Observatory [Bjoraker et al., 1986], the In-
frared Space Observatory [Fouchet et al., 2000], and spacecraft instruments such as Galileo
NIMS [Roos-Serote et al., 1998] and Juno JIRAM [Grassi et al., 2017]. While the previous
microwave and long-wavelength infrared analyses of Jupiter’s NH3 abundance have explored
spatial variability, these 5-µm studies have typically either used disc-averaged spectra or fo-
cused on a speciﬁc area of interest, such as the 5-µm hot-spots [e.g. Grassi et al., 2017]. In
this paper, we present latitudinally-resolved high-spectral resolution observations of Jupiter
at 5 µm, and we use these measurements to study the spatial variability in Jupiter’s tropo-
spheric NH3 abundance. Sections 2 and 3 describe the observations and our retrieval code.
The results of the NH3 retrievals are then presented in Section 4 and discussed in Section 5.
2 Observations
2.1 CRIRES observations
The CRIRES instrument at the European Southern Observatory’s Very Large Tele-
scope (VLT) was used to make observations of Jupiter in the 5-µm atmospheric window.
CRIRES is a cryogenic high-resolution infrared echelle spectrograph [Käuﬂet al., 2004],
which provides long-slit (0.2×40”) spectroscopy with a resolving power of 96,000. The
CRIRES observations used in this paper have previously been used to study the latitudinal
variability in Jupiter’s tropospheric disequilibrium species [Giles et al., 2017] and the H3+
auroral emission [Giles et al., 2016]. In this paper, these CRIRES observations are used to
study NH3 absorption in the 5-µm window.
The observations used in this paper were made on 12 November 2012 at 05:30 UT.
As described in Giles et al. [2017], the slit was aligned north-south along Jupiter’s central
meridian (at a longitude of 104◦W), allowing us to measure spatial variability with latitude,
but not longitude. Observations were made in multiple wavelength settings across the 5-µm
spectral window, but this paper focuses on a single setting which covers the 5.15–5.19 µm
range and includes several strong NH3 lines. In addition to observations of Jupiter, observa-
tions were made of a standard star, Pi-2 Orionis (HIP 22509), in order to provide radiometric
calibration.
–3–


## Page 4


Manuscript accepted for publication in Geophysical Research Letters
2.2 Data reduction
The data reduction process is described in detail in Giles et al. [2017]. EsoRex, the
ESO Recipe Execution Tool [Ballester et al., 2006], was initially used to combine nodded
pairs into a single observation and to achieve wavelength calibration. Subsequent data reduc-
tion was performed independently of the EsoRex software. The observations were straight-
ened to correct observed distortions in both the spectral and spatial directions and were ra-
diometrically calibrated using the observations of the standard star. Geometric information
(including planetocentric latitude) was assigned to the observations using information from
JPL HORIZONS.
3 Spectral modelling
The CRIRES observations were analysed using the NEMESIS retrieval algorithm [Ir-
win et al., 2008]. NEMESIS uses a multiple-scattering radiative transfer forward model to
calculate the observed top-of-atmosphere spectral radiance for a given set of atmospheric pa-
rameters. These atmospheric parameters are then iteratively adjusted to match the observed
spectrum, following an optimal estimation approach. As with Giles et al. [2017], line-by-line
calculations are used in the forward model and this previous paper also details the sources
of the spectroscopic line data. Again following the approach of Giles et al. [2017], we add
a conservative 5% forward modelling error to the retrieval calculations, to take into account
inaccuracies in the model (e.g. line data). The error bars shown in Figures 1, 3 and 4 only
show the noise on the observations, and any small discrepancies between the observations
and the ﬁtted spectra are likely due to these inaccuracies in the model.
The reference atmospheric proﬁle is described as in Giles et al. [2015] and Giles et al.
[2017]. As with Giles et al. [2017], the atmosphere is divided into 39 pressure levels. The
NH3 abundance is allowed to vary continuously at each of the 39 pressure levels in order to
determine its vertical proﬁle. Although this paper focuses on NH3 absorption features, H2O
also has broad spectral features in the 5.15–5.19 µm range, which contribute to the contin-
uum radiance. In the retrievals presented in this paper, the H2O abundance was allowed to
vary via a single relative humidity value. As a test, retrievals were also carried out where the
H2O relative humidity was held ﬁxed at values ranging from 1% to 10% (approximate range
taken from Roos-Serote et al. [2000]); while this generally worsened the ﬁt to the data, it did
not aﬀect the qualitative NH3 results.
–4–


## Page 5


Manuscript accepted for publication in Geophysical Research Letters
In addition to gaseous species, tropospheric clouds also have a signiﬁcant impact on
the observed spectra at 5-µm. As shown in many previous studies [e.g. Gierasch et al., 1986;
Irwin et al., 2001; Giles et al., 2015], the banded appearance that Jupiter’s exhibits at 5 µm
is due to the presence of clouds located between roughly 0.7 and 1.5 bar, which vary be-
tween optically thick in the zones and optically thin in the belts. Giles et al. [2017] showed
that the CRIRES data could be modelled using a simple cloud model consisting of a sin-
gle, spectrally-ﬂat, compact cloud layer, located at 0.8 bar, with a single-scattering albedo
ω = 0.9 and a Henyey-Greenstein asymmetry parameter g = 0.8. This is used as the
cloud model in this paper, and the cloud’s optical thickness will be a free parameter in all
retrievals. It should be noted that because the cloud particles are both highly scattering, and
predominantly forward-scattering, the retrieved cloud optical thickness can be high, while
still allowing photons to pass through. The potential impact of an additional deep cloud layer
is discussed in Section 4.2.1.
4 Analysis
4.1 NH3 absorption features
Jupiter’s 5-µm window contain several NH3 absorption features. This paper focuses
on three absorption lines which fall within the 5.15–5.19 µm range. This spectral region was
used because (i) it is relatively free of terrestrial absorption lines, which can be diﬃcult to
remove cleanly; and (ii) it is relatively free from strong absorption features from other jovian
tropospheric species. The locations of the three NH3 absorption lines are shown by the ar-
rows in Figure 1(a). The lines at 5.156 and 5.157 µm are relatively strong, while the line at
5.184 µm is relatively weak. Depending on their strength, diﬀerent lines probe slightly dif-
ferent pressure levels in Jupiter’s atmosphere. Assuming the a priori atmospheric proﬁle and
a cloud-free atmosphere, the three absorption lines have a maximum sensitivity at 1.64, 1.56
and 3.19 bar respectively. By simultaneously ﬁtting all three lines, we can therefore constrain
the vertical proﬁle of NH3 within the ∼1–4 bar pressure range.
The black lines in Figure 1(a) show the CRIRES observations of Jupiter. This data is
taken from the planet’s warm, cloud-free South Equatorial Belt (SEB, 16◦S–6◦S); this part
of the planet is bright at 5 µm, so the noise on the data (shown by the error bars) is relatively
low. NEMESIS was used to perform a retrieval on this data, and the resulting ﬁtted spectrum
–5–


## Page 6


Manuscript accepted for publication in Geophysical Research Letters
5.152
5.156
5.160
Wavelength (µm)
0
10
20
30
40
50
Radiance (µWcm−2sr−1µm−1)
5.180
5.184
5.188
Wavelength (µm)
(a) Fitted spectrum
(b) Retrieved NH3 profile
10−10
10−8
10−6
10−4
10−2
Volume mixing ratio
10.0
1.0
0.1
Pressure (bar)
Figure 1.
NH3 absorption lines in the 5-µm window from Jupiter’s warm South Equatorial Belt (16◦S–
6◦S). (a) The ﬁtted spectrum (red) compared to the observational data (black). The blue line shows what the
same spectrum would look like in the absence of NH3. The arrows show the NH3 absorption line centres. (b)
The retrieved NH3 vertical proﬁle (red) compared to the a priori proﬁle (black).
is shown by the red line plotted on top of the data. For comparison, the blue line shows what
the same ﬁtted spectrum would look like if NH3 were not present in Jupiter’s atmosphere.
In order to ﬁt the CRIRES data, the NH3 abundance was allowed to vary at each of the
39 pressure levels in the model atmosphere. The retrieved vertical proﬁle is shown in red
in Figure 1(b), alongside the a priori proﬁle in black, taken from analyses of Cassini/CIRS
data [Fletcher et al., 2009]. As expected, the region of maximum sensitivity is at ∼1–4 bar;
outside this range, the retrieval tends towards the a priori due to a lack of other information
and the error bars tend towards the 100% errors placed on the a priori.
Although the a priori vertical proﬁle from Fletcher et al. [2009] assumes a constant
NH3 abundance at all pressures greater than 0.8 bar, the retrieved vertical proﬁle in Fig-
ure 1(b) deviates from this assumption. Instead, a higher abundance is required at higher
pressures (primarily driven by the 5.184 µm line) and a lower abundance is required at lower
pressures (primarily driven by the 5.156 and 5.157 µm lines). This agrees with previous re-
sults from Fouchet et al. [2000] and Section 4.2 shows that this pattern extends across the
planet.
4.2 Latitudinal variability
Section 4.1 focused on a single spatial region of the planet. In this section, we will now
explore how the NH3 vertical proﬁle varies with latitude across Jupiter. As described in Sec-
–6–


## Page 7


Manuscript accepted for publication in Geophysical Research Letters
(a) Cloud opacity
-60
-40
-20
0
20
40
60
Latitude
0
5
10
15
20
25
Optical thickness
EqZ
SEB
NEB
(b) NH3 volume mixing ratio at 3.3 bar
-60
-40
-20
0
20
40
60
Latitude
0
5
10
15
20
Volume mixing ratio (10-4)
EqZ
SEB
NEB
(c) NH3 volume mixing ratio at 1.6 bar
-60
-40
-20
0
20
40
60
Latitude
0
1
2
3
4
5
Volume mixing ratio (10-4)
EqZ
SEB
NEB
Figure 2.
Latitudinal retrieval of CRIRES observations. The retrieved cloud opacity as a function of lati-
tude is shown in (a). The retrieved NH3 volume mixing ratios at 3.3 and 1.6 bar are are shown in (b) and (c)
respectively.
–7–


## Page 8


Manuscript accepted for publication in Geophysical Research Letters
tion 2, the CRIRES observations provide latitudinally resolved spectra from Jupiter’s central
meridian. The spectra were smoothed in the latitudinal direction with a width of 5 pixels in
order to reduce the noise, and the sampling rate was 3 pixels. For each smoothed spectrum,
a retrieval was performed using NEMESIS where the NH3 vertical proﬁle was allowed to
vary continuously. As in Figure 1, the retrieval assumes a single cloud layer with a variable
optical thickness. The results are shown in Figure 2; (a) shows the retrieved cloud opacity as
a function of latitude, while (b) and (c) show the retrieved NH3 volume mixing ratios at 3.3
and 1.6 bar respectively. The previous section showed that the SEB retrievals lead to a vol-
ume mixing ratio that decrease with altitude in the 1–4 bar pressure range. Figure 2 shows
that this remains true at all latitudes, as (c) shows consistently lower abundances than (b).
As a comparison, retrievals were also performed where NH3 was assumed to be well-
mixed at high pressures, before dropping to zero at 0.8 bar (the approximate condensation
point of NH3). This led to a consistently poorer ﬁt to the data, but to varying degrees across
the planet. In the cool zones, this change did not have a large impact, increasing the goodness-
of-ﬁt parameter (χ2) by <5%. In the warm belts, the well-mixed vertical proﬁle increased χ2
by ∼20%. The greatest impact was from spectra near 5◦N, where a vertical proﬁle that de-
creases with altitude ﬁts the data 100% better than a well-mixed proﬁle.
4.2.1 Belt-zone variability
Figure 2(a) shows the belt-zone structure of Jupiter’s atmosphere. In the planet’s zones
(such as the Equatorial Zone), the clouds are optically thick. In the adjacent belts, the cloud
opacity drops signiﬁcantly. Figures 2(b) and (c) show that some of the retrieved variability
in the NH3 abundance coincides with the belt-zone structure, with higher retrieved abun-
dances in the belts. In particular, the increase in NH3 abundance that can be seen at 5–20◦S
in both (b) and (c) coincides with the SEB. While it is possible that these retrievals represent
a genuine increase in NH3 at these latitudes, it is also possible that this is an artefact due to
the tropospheric cloud structure. Bjoraker et al. [2015] and Giles et al. [2017] showed that
there is evidence for a ∼5-bar water cloud that varies between optically thick in the zones
and optically thin in the belts. Giles et al. [2017] also showed that the presence of this cloud
can explain similar apparent belt-zone variability in the line shapes of tropospheric gaseous
species.
–8–


## Page 9


Manuscript accepted for publication in Geophysical Research Letters
5.152
5.156
5.160
Wavelength (µm)
0
1
2
3
4
Radiance (µWcm−2sr−1µm−1)
5.180
5.184
5.188
Wavelength (µm)
(a) Fitted spectrum
(b) Retrieved NH3 profile
10−10
10−8
10−6
10−4
10−2
Volume mixing ratio
10.0
1.0
0.1
Pressure (bar)
Figure 3.
NH3 absorption lines in the 5-µm window from Jupiter’s cool Equatorial Zone (5◦S–4◦N). (a)
The ﬁtted spectrum assuming that there is no deep cloud (red) compared to the ﬁtted spectrum assuming that
there is an opaque cloud at 5 bar (blue). (b) The retrieved NH3 vertical proﬁles in the two cases: no deep
cloud (red) and opaque 5-bar cloud (blue).
This is shown further by Figure 3, which shows the NH3 absorption features from the
Equatorial Zone (EqZ, 5◦S–4◦N). When compared to Figure 1, it is clear that the absorption
features are much shallower in the EqZ than in the SEB. One interpretation of this is that the
NH3 abundance is higher in the SEB and lower in the EqZ. The red lines in Figure 3 show
the ﬁtted spectrum and retrieved proﬁle if there is no deep cloud present in the atmosphere,
and they lead to this conclusion. Over the sensitive 1–4 bar region, the retrieved abundances
shown in red in Figure 3(b) are signiﬁcantly lower than those in Figure 1(b). However, this
trend can be cancelled out, or even reversed, by the addition of a deep cloud layer in the EqZ.
Following Giles et al. [2017], an opaque cloud was inserted at 5 bar. The results of this re-
trieval are shown by the blue lines in Figure 3. While Figure 3(a) shows that the ﬁt remains
similar, the retrieved abundances in Figure 3(b) are fairly diﬀerent. Because the presence of
the deep cloud suppresses the absorption features, the retrieved abundances in the 1–4 bar
region are now higher. In fact, the 3-bar abundance is now slightly higher for the EqZ than
for the SEB. The deep cloud structure therefore leads to considerably uncertainty in the belt-
zone variability in NH3.
4.2.2 Small-scale variability
While deep tropospheric clouds can plausibly explain the retrieved NH3 enhancement
in the SEB, the same is not true for the observed spike at 5◦N shown in Figure 2(b). This
spike is oﬀset from the warm, cloud-free North Equatorial Belt (NEB). While NH3 abun-
–9–


## Page 10


Manuscript accepted for publication in Geophysical Research Letters
5.152
5.156
5.160
Wavelength (µm)
0
10
20
30
40
Radiance (µWcm−2sr−1µm−1)
5.180
5.184
5.188
Wavelength (µm)
(a) Fitted spectrum (5oN)
(b) Retrieved NH3 profile (5oN)
10−10
10−8
10−6
10−4
10−2
Volume mixing ratio
10.0
1.0
0.1
Pressure (bar)
5.152
5.156
5.160
Wavelength (µm)
0
10
20
30
40
Radiance (µWcm−2sr−1µm−1)
5.180
5.184
5.188
Wavelength (µm)
(c) Fitted spectrum (8oN)
(d) Retrieved NH3 profile (8oN)
10−10
10−8
10−6
10−4
10−2
Volume mixing ratio
10.0
1.0
0.1
Pressure (bar)
Figure 4.
NH3 absorption features from two diﬀerent points on the planet: 5◦N and 8◦N. (a) and (c) show
the ﬁtted spectrum (red) compared to the observational data (black). (b) and (d) show the retrieved NH3
vertical proﬁle (red) compared to the a priori proﬁle (black).
dance peaks at 5◦N, the minimum cloud opacity is at 7◦N, by which point the NH3 abun-
dance has dropped to a third of its maximum value. While Figure 2(a) shows the opacity of
the 0.8-bar cloud, Giles et al. [2017] demonstrated that the deep cloud structure follows the
same latitudinal pattern as the upper cloud, reaching a minimum in the centre of the belts.
Based on the cloud structure alone, we would expect the maximum retrieved NH3 abundance
to be at 7◦N. It therefore appears that there is a genuine enhancement of NH3 at 4–6◦N and a
corresponding relative depletion at 7-9◦N at 3.3 bar.
This is further demonstrated in Figure 4 which shows the results of the retrievals from
these two points on the planet. Figures 4(a) and 4(c) show the observed spectra from 5◦N
and 8◦N, along with the retrieved best-ﬁt spectrum (with a single 0.8-bar cloud layer). The
absorption features at 5◦N are deeper than the absorption features at 8◦N. The average ra-
diance in both cases is very similar; this is primarily determined by the cloud opacity, and
therefore shows that these two regions have similar amounts of cloud cover. The diﬀerences
between them are therefore primarily due to diﬀerences in the NH3 abundance. This is fur-
–10–


## Page 11


Manuscript accepted for publication in Geophysical Research Letters
ther emphasised by the fact that if there were any diﬀerences in the deep water cloud opacity,
the opacity is likely to be higher at 5◦N than at 8◦N, since the former is closer to the cloudy
Equatorial Zone. However, thick deep clouds have a tendency to obscure absorption features,
rather than enhance them, so they cannot explain the spectral diﬀerences between these two
cases.
The most striking diﬀerence between Figures 4(a) and 4(c) is in the depth of the ab-
sorption feature at 5.184 µm, which probes higher pressures in the atmosphere; it is signif-
icantly deeper at 5◦N than at 8◦N. In contrast, the features at 5.156 and 5.157 µm, which
probe lower pressures, are relatively similar in the two cases. The retrieved NH3 proﬁles
(Figure 4(b) and 4(d)) reﬂect these spectral similarities and diﬀerences; at higher pressures
(∼3 bar) there is a large diﬀerence between the retrieved NH3 abundances, but at lower pres-
sures (∼1 bar) the retrieved abundances are approximately the same. This is also reﬂected in
Figure 2, which shows a 5◦N enhancement, but a relatively ﬂat distribution at 1.6 bar.
5 Discussion and conclusions
High-resolution ground-based observations from the CRIRES instrument at the VLT
were used to analyse NH3 absorption features in Jupiter’s 5-µm spectrum. The three absorp-
tion features at 5.15–5.19 µm probe the 1–4 bar pressure range in Jupiter’s troposphere, al-
lowing the vertical proﬁle to be constrained. The CRIRES observations show that the NH3
abundance decreases with altitude over this pressure range. This is consistent with the results
of a previous 5-µm study by Fouchet et al. [2000], who found that the NH3 mixing ratio in-
creases downward to at least the 4-bar level. This agrees with the nominal cloud structure of
the planet [Atreya et al., 1999], in which NH3 forms cloud layers of aqueous-ammonia solu-
tion, ammonium hydrosulphide and ammonia ice at 5.7, 2.2 and 0.7 bar respectively.
The CRIRES observations were then used to study the latitudinal variability in the
NH3 abundance. Using a simple one-cloud model, there is some belt-zone variability in the
retrieved abundances, with higher volume mixing ratios observed in the cloud-free belts and
lower volume mixing ratios observed in the cloudy zones. However, this trend can be re-
moved by adding in an optically-thick 5-bar cloud in the zones, as previously shown by Giles
et al. [2017]. If this cloud is made opaque, the retrieved 3-bar NH3 abundance is actually
slightly higher in the EqZ than in the SEB. The eﬀects of the deep cloud add considerably
uncertainty comparisons of spectra from the belts and the zones.
–11–


## Page 12


Manuscript accepted for publication in Geophysical Research Letters
However, spectra from regions with similar cloud cover can be robustly compared, and
the CRIRES data provide evidence for smaller-scale spatial variability in NH3. We ﬁnd an
NH3 enhancement at 4–6◦N and a corresponding relative depletion at 7–9◦N, at a pressure of
3–4 bar, despite the fact that these two spatial regions have similar cloud opacities. In addi-
tion, we ﬁnd that this enhancement does not continue through to higher altitudes; by 1.6 bar,
the trend has disappeared.
This is consistent with the ‘ammonia plumes’ detected by Fletcher et al. [2016] us-
ing 10-µm observations from the TEXES instrument at NASA’s Infrared Telescope Facility.
TEXES was used to make global maps of the planet, and the spectra are sensitive to the NH3
abundance at the 500-mbar level. Fletcher et al. [2016] found a series of NH3-rich plumes
at latitudes of around 5◦N, located directly to the south-east of NH3-dessicated hot-spots. At
3–4 bar, the CRIRES observations show the same latitudinal proﬁle, albeit limited to a single
longitude. However, it is unclear why the plume would be evident at >3 bar and 500 mbar,
but be absent at 1.6 bar.
While the TEXES observations probed higher altitudes than CRIRES, observations
were recently made with the Juno MWR instrument that are sensitive to the NH3 abundance
at pressures ranging from 500 mbar up to 100 bar [Janssen et al., 2017]. Li et al. [2017]
found that NH3 had an asymmetrical distribution, with an enhancement at 0–5◦N and a de-
pletion at 5–15◦N. Like CRIRES, MWR shows a sharp contrast in NH3 abundance between
4–6◦N and 7–9◦N. However the strong equatorial enhancement seen by MWR is not ob-
served in the CRIRES data. This can be partially explained by the presence of deep, thick
clouds in the Equatorial Zone, which act to suppress the gaseous absorption features at 5-µm
and can therefore increase the retrieved abundances if they are included in the model. How-
ever, even an entirely opaque deep cloud cannot reproduce the strong enrichment at all pres-
sure levels that is seen at the equator in the MWR observations. The cause of the discrepancy
between the two spectral regimes is unclear and should be the focus of future studies; pos-
sible explanations could include temporal variability (between 2012 and 2016), temperature
variations, or additional complex cloud eﬀects.
Acknowledgments
This work is based on observations collected at the European Organisation for Astro-
nomical Research in the Southern Hemisphere under ESO programme 090.C-0053(A). The
–12–


## Page 13


Manuscript accepted for publication in Geophysical Research Letters
data is available from the ESO Science Archive Facility. The research was carried out in part
at the Jet Propulsion Laboratory, California Institute of Technology, under a contract with
the National Aeronautics and Space Administration. Giles and Sinclair were supported by
the NASA Postdoctoral Program, and Orton was supported by grants from NASA to the Jet
Propulsion Laboratory/California Institute of Technology. Fletcher was supported by a Royal
Society Fellowship at the University of Leicester and Irwin was supported by the UK Science
and Technology Facilities Council.
© 2017. All rights reserved
References
Atreya, S., M. Wong, T. Owen, P. Mahaﬀy, H. Niemann, I. De Pater, P. Drossart, and T. En-
crenaz (1999), A comparison of the atmospheres of Jupiter and Saturn: deep atmospheric
composition, cloud structure, vertical mixing, and origin, Planetary and Space Science,
47(10), 1243–1262.
Atreya, S. K., T. M. Donahue, and W. R. Kuhn (1977), The distribution of ammonia and its
photochemical products on Jupiter, Icarus, 31(3), 348–355.
Ballester, P., K. Banse, S. Castro, R. Hanuschik, R. Hook, C. Izzo, Y. Jung, A. Kaufer,
J. Larsen, T. Licha, et al. (2006), Data reduction pipelines for the Very Large Telescope,
in Proc. SPIE, vol. 6270.
Bjoraker, G., M. Wong, I. de Pater, and M. Ádámkovics (2015), Jupiter’s deep cloud struc-
ture revealed using Keck observations of spectrally resolved line shapes, The Astrophysical
Journal, 810(2), 122.
Bjoraker, G. L., H. P. Larson, and V. G. Kunde (1986), The gas composition of Jupiter de-
rived from 5-µm airborne spectroscopic observations, Icarus, 66(3), 579–609.
de Pater, I., D. Dunn, P. Romani, and K. Zahnle (2001), Reconciling Galileo probe data and
ground-based radio observations of ammonia on Jupiter, Icarus, 149(1), 66–78.
Fletcher, L., G. Orton, N. Teanby, and P. Irwin (2009), Phosphine on Jupiter and Saturn from
Cassini/CIRS, Icarus, 202(2), 543–564.
Fletcher, L. N., T. Greathouse, G. Orton, J. Sinclair, R. Giles, P. Irwin, and T. Encrenaz
(2016), Mid-infrared mapping of Jupiter’s temperatures, aerosol opacity and chemical dis-
tributions with IRTF/TEXES, Icarus, 278, 128–161.
–13–


## Page 14


Manuscript accepted for publication in Geophysical Research Letters
Fouchet, T., E. Lellouch, B. Bézard, T. Encrenaz, P. Drossart, H. Feuchtgruber, and
T. de Graauw (2000), ISO-SWS observations of Jupiter: measurement of the ammonia
tropospheric proﬁle and of the 15N/14N isotopic ratio, Icarus, 143(2), 223–243.
Gierasch, P. J., B. J. Conrath, and J. A. Magalhães (1986), Zonal mean properties of Jupiter’s
upper troposphere from Voyager infrared observations, Icarus, 67(3), 456–483.
Giles, R. S., L. N. Fletcher, and P. G. Irwin (2015), Cloud structure and composition of
Jupiter’s troposphere from 5-µm Cassini VIMS spectroscopy, Icarus, 257, 457–470.
Giles, R. S., L. N. Fletcher, P. G. Irwin, H. Melin, and T. S. Stallard (2016), Detection of
H3+ auroral emission in Jupiter’s 5-micron window auroral emission in Jupiter’s 5-micron
window, Astronomy & Astrophysics, 589, A67.
Giles, R. S., L. N. Fletcher, and P. G. Irwin (2017), Latitudinal variability in Jupiter’s tropo-
spheric disequilibrium species: GeH4, AsH3 and PH3, Icarus, 289, 254–269.
Grassi, D., A. Adriani, A. Mura, B. Dinelli, G. Sindoni, D. Turrini, G. Filacchione,
A. Migliorini, M. Moriconi, F. Tosi, et al. (2017), Preliminary results on the composition
of Jupiter’s troposphere in hot spot regions from the JIRAM/Juno instrument, Geophysical
Research Letters.
Irwin, P., A. Weir, S. Smith, F. Taylor, A. Lambert, S. Calcutt, P. Cameron-Smith, R. Carl-
son, K. Baines, G. Orton, et al. (1998), Cloud structure and atmospheric composition of
Jupiter retrieved from Galileo near-infrared mapping spectrometer real-time spectra, Jour-
nal of Geophysical Research: Planets (1991–2012), 103(E10), 23,001–23,021.
Irwin, P., A. Weir, F. Taylor, S. Calcutt, and R. Carlson (2001), The origin of belt/zone con-
trasts in the atmosphere of Jupiter and their correlation with 5-µm opacity, Icarus, 149(2),
397–415.
Irwin, P., N. Teanby, R. de Kok, L. Fletcher, C. Howett, C. Tsang, C. Wilson, S. Calcutt,
C. Nixon, and P. Parrish (2008), The NEMESIS planetary atmosphere radiative transfer
and retrieval tool, Journal of Quantitative Spectroscopy and Radiative Transfer, 109(6),
1136–1150.
Janssen, M., J. Oswald, S. Brown, S. Gulkis, S. Levin, S. Bolton, M. Allison, S. Atreya,
D. Gautier, A. Ingersoll, et al. (2017), MWR: Microwave radiometer for the Juno mission
to Jupiter, Space Science Reviews, pp. 1–47.
Käuﬂ, H. U., P. Ballester, P. Biereichel, B. Delabre, R. Donaldson, R. Dorn, E. Fedrigo,
G. Finger, G. Fischer, F. Franza, et al. (2004), CRIRES: a high resolution infrared spec-
trograph for ESO’s VLT, in Proc. SPIE, vol. 5492.
–14–


## Page 15


Manuscript accepted for publication in Geophysical Research Letters
Kunde, V., R. Hanel, W. Maguire, D. Gautier, J. Baluteau, A. Marten, A. Chedin, N. Hus-
son, and N. Scott (1982), The tropospheric gas composition of Jupiter’s North Equatorial
Belt (NH3, PH3, CH3D, GeH4, H2) and the jovian D/H isotopic ratio, The Astrophysical
Journal, 263, 443–467.
Li, C., A. Ingersoll, M. Janssen, S. Levin, S. Bolton, V. Adumitroaie, M. Allison, J. Arballo,
A. Bellotti, S. Brown, et al. (2017), The distribution of ammonia on Jupiter from a prelim-
inary inversion of Juno Microwave Radiometer data, Geophysical Research Letters.
Roos-Serote, M., P. Drossart, T. Encrenaz, E. Lellouch, R. Carlson, K. Baines, L. Kamp,
R. Mehlman, G. Orton, S. Calcutt, et al. (1998), Analysis of Jupiter North Equatorial Belt
hot spots in the 4–5 µm range from Galileo near-infrared mapping spectrometer observa-
tions: measurements of cloud opacity, water, and ammonia, Journal of Geophysical Re-
search: Planets (1991–2012), 103(E10), 23,023–23,041.
Roos-Serote, M., A. Vasavada, L. Kamp, P. Drossart, P. Irwin, C. Nixon, and R. Carlson
(2000), Proximate humid and dry regions in Jupiter’s atmosphere indicate complex local
meteorology, Nature, 405(6783), 158–160.
Showman, A. P., and I. de Pater (2005), Dynamical implications of Jupiter’s tropospheric
ammonia abundance, Icarus, 174(1), 192–204.
–15–

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1710_03336v1_ammonia_in_jupiter_s_troposphere_from_high_resolution_5_textmu_m_spectroscopy
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2017/1710_03336V1_AMMONIA_IN_JUPITER_S_TROPOSPHERE_FROM_HIGH_RESOLUTION_5_TEXTMU_M_SPECTROSCOPY.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

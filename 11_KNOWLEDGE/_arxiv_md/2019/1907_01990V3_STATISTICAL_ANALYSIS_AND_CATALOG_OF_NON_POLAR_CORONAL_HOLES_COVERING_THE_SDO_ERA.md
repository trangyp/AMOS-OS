---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1907.01990v3
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1907.01990v3_Statistical_Analysis_and_Catalog_of_Non-polar_Coronal_Holes_Covering_the_SDO-era

> Source: 1907.01990v3_Statistical_Analysis_and_Catalog_of_Non-polar_Coronal_Holes_Covering_the_SDO-era.pdf

> Pages: 30

---


## Page 1


Solar Physics
DOI: 10.1007/•••••-•••-•••-••••-•
Statistical Analysis and Catalog of Non–polar
Coronal Holes Covering the SDO–era using CATCH
Stephan G. Heinemann1
· Manuela
Temmer1
· Niko Heinemann1
· Karin
Dissauer1
· Evangelia Samara2,3
·
Veronika Jerˇci´c1,4
· Stefan J.
Hofmeister1
· Astrid M. Veronig1,5
c⃝Springer ••••
Abstract Coronal holes are usually deﬁned as dark structures as seen in the
extreme ultraviolet and X-ray spectrum which are generally associated with open
magnetic ﬁeld. Deriving reliably the coronal hole boundary is of high interest,
as its area, underlying magnetic ﬁeld, and other properties give important hints
towards high speed solar wind acceleration processes and on compression regions
arriving at Earth. In this study we present a new threshold based extraction
method that incorporates the intensity gradient along the coronal hole boundary,
which is implemented as a user-friendly SSWIDL GUI. The Collection of Analy-
sis Tools for Coronal Holes (CATCH) enables the user to download data, perform
guided coronal hole extraction and analyze the underlying photospheric magnetic
ﬁeld. We use CATCH to analyze non-polar coronal holes during the SDO-era,
based on 193 ˚A ﬁltergrams taken by the Atmospheric Imaging Assembly (AIA)
and magnetograms taken by the Heliospheric and Magnetic Imager (HMI), both
on board the Solar Dynamics Observatory (SDO). Between 2010 and 2019 we
investigate 707 coronal holes that are located close to the central meridian. We
ﬁnd coronal holes distributed across latitudes of about ±60o for which we derive
sizes between 1.6 × 109 and 1.8 × 1011 km2. The absolute value of the mean
signed magnetic ﬁeld strength tends towards an average of 2.9±1.9 G. As far as
B S.G.Heinemann
stephan.heinemann@hmail.at
1
University of Graz, Institute of Physics, Universit¨atsplatz 5, 8010 Graz, Austria
2
Centre of Mathematical Plasma Astrophysics, KU Leuven, Leuven, Belgium
3
Royal Observatory of Belgium, Brussels, Belgium
4
University of Zagreb, Faculty of Science, Department of Geophysics, Zagreb, Croatia
5
Kanzelh¨ohe Observatory for Solar and Environmental Research, University of Graz,
9521 Treﬀen, Austria
SOLA: main.tex; 7 October 2019; 0:52; p. 1
arXiv:1907.01990v3  [astro-ph.SR]  4 Oct 2019


## Page 2


S.G. Heinemann et al.
the abundance and size of coronal holes is concerned, we ﬁnd no distinct trend
towards the northern or southern hemisphere. We ﬁnd that variations in local
and global conditions may signiﬁcantly change the threshold needed for reliable
coronal hole extraction and thus, we can highlight the importance of individually
assessing and extracting coronal holes.
1. Introduction
Coronal holes (CHs) are large-scale features in the solar corona often charac-
terized by reduced emission in X-ray and extreme ultraviolet (EUV) which
are associated with open magnetic ﬁeld lines of a dominant polarity. Coronal
plasma is accelerated along the open ﬁeld lines causing a high velocity outﬂow
of particles, often referred to as fast solar wind or high speed solar wind stream
(HSS). The plasma depletion causes a reduction of density and temperature in
these regions in comparison to the surrounding solar corona. Thus, CHs can be
observed as dark structures in the EUV and X-ray emission (see e.g., Schwenn,
2006; Cranmer, 2002, 2009).
To investigate the morphology and intensity of CHs as observed in EUV,
as well as their underlying photospheric magnetic ﬁeld, the identiﬁcation and
extraction of CH boundaries are key. There exist multiple approaches to this
topic with one of the most popular using a single wavelength, intensity-based
threshold approach on EUV observations. Due to the high contrast and the
optimal ﬁlter sensitivity, the coronal emission line of eleven times ionized iron
(Fe xii: 193/195 ˚A) is often used to extract CHs (e.g., Krista and Gallagher,
2009; Rotter et al., 2012, 2015; Reiss et al., 2015; Caplan, Downs, and Linker,
2016; Boucheron, Valluri, and McAteer, 2016; Hofmeister et al., 2017; Heinemann
et al., 2018a). Other intensity based approaches include multi-thermal emission
recognition (Garton, Gallagher, and Murray, 2018) and spatial possibilistic clus-
tering (Verbeeck et al., 2014). A diﬀerent concept is to model the open ﬁeld,
that characterizes CHs, using photospheric magnetograms. Examples include
the potential ﬁeld source surface model (PFSS; Altschuler and Newkirk, 1969),
its improved version including the Schatten Current Sheet, the Wang-Sheeley-
Arge model (WSA model; Arge and Pizzo, 2000) and the MULTI-VP model
(Pinto and Rouillard, 2017). Studies comparing the two diﬀerent conceptual
approaches have shown signiﬁcant diﬀerences in the size, location, shape and
occurrence of the dark and/or open structure deﬁned as CHs (e.g., Lowder et al.,
2014; Lowder, Qiu, and Leamon, 2017; Linker et al., 2017; Wallace et al., 2019;
Huang, Lin, and Lee, 2019; Asvestari et al., 2019). Additionally new approaches
like machine learning/neural networks (e.g., Illarionov and Tlatov, 2018) and
extraction methods based on plasma properties (Diﬀerential Emission Measure;
Raymond and Doyle, 1981; Hahn, Landi, and Savin, 2011) are the topic of current
research.
Reliably deﬁning CH boundaries is not only relevant for studying coronal
and photospheric properties and their evolution but is also of major scientiﬁc
importance towards space weather research. Empirical relations between CH area
and measured solar wind speed at 1AU (e.g., Nolte et al., 1976; Vrˇsnak, Temmer,
SOLA: main.tex; 7 October 2019; 0:52; p. 2


## Page 3


CATCH
and Veronig, 2007; Tokumaru et al., 2017; Hofmeister et al., 2018) are used for
forecasting purposes (e.g., Rotter et al., 2012, 2015; Reiss et al., 2016; Temmer,
Hinterreiter, and Reiss, 2018). Moreover, the distance to CH boundary is an
important parameter for MHD models simulating the solar wind distribution
in interplanetary space (e.g., ENLIL: Odstrˇcil and Pizzo 1999, EUHFORIA:
Pomoell and Poedts 2018 and CORHEL: Riley et al. 2012). When considering
CH extraction, usually there is the choice between manual and automated al-
gorithms of which both have advantages and disadvantages. On the one hand,
manual extraction of CHs requires a lot of time and experience in order to get
reliable results. On the other hand, automated extraction methods are prone to
signiﬁcant errors and artifacts.
In the ﬁrst part of this study we present a new method for extracting CH
boundaries in EUV images by using an intensity threshold which is modulated
by the intensity gradient of the CH boundary. The method is based on the works
of Rotter et al. (2012), Rotter et al. (2015), and Krista and Gallagher (2009)
and is incorporated into an easy-to-use GUI application developed in SSW-
IDL. The Collection of Analysis Tools for Coronal Holes (CATCH) application
enables users to easily extract and analyze CHs in a supervised semi-automated
fashion. CATCH uses a modulated intensity threshold method to extract CH
boundaries from EUV images and analyzes the associated properties. In ad-
dition, it oﬀers the possibility to investigate the underlying magnetic ﬁeld. In
the second part, we use CATCH to investigate 707 CHs covering the complete
time range of the operational lifetime of the Solar Dynamics Observatory (SDO;
Pesnell, Thompson, and Chamberlin, 2012) so far, starting in May 2010 until
February 2019. We derive statistical CH properties of the area, intensity, and
the underlying magnetic ﬁeld including the magnetic ﬁne structure over nearly
the full Solar Cycle 24. Furthermore, we present how the parameters for an
optimal CH extraction vary during the Solar Cycle. The CH dataset is available
as an online catalogue under the CDS database using the Vizier catalogue service
(Ochsenbein, Bauer, and Marcout, 2000).
2. The “Collection of Analysis Tools for Coronal Holes”
The Collection of Analysis Tools for Coronal Holes (CATCH) was created in
order to collect and structure CH identiﬁcation, extraction and analysis in a
handy and fast way without the disadvantages of automatic algorithms as de-
scribed in the Sections 2.1 and 2.2. It enables the user to download and process
EUV ﬁltergrams (193/195 ˚A) and line–of–sight (Los) magnetograms. CATCH is
able to handle data from diﬀerent spacecraft missions covering the interval from
1996 until now. These are SDO, the Solar Terrestrial Relations Observatory
(STEREO; Kaiser et al., 2008) and the Solar and Heliospheric Observatory
(SOHO; Domingo, Fleck, and Poland, 1995). Data from the Atmospheric Imag-
ing Assembly (Lemen et al., 2012, AIA; 193˚A), the Extreme ultraviolet Imaging
Telescope (Delaboudini`ere et al., 1995, EIT; 195˚A) and the Extreme UltraViolet
Imager (Howard et al., 2008, EUVI; 195˚A) as well as from the Heliospheric
SOLA: main.tex; 7 October 2019; 0:52; p. 3


## Page 4


S.G. Heinemann et al.
and Magnetic Imager (HMI:
Schou et al., 2012; Couvidat et al., 2016) and
the Michelson Doppler Imager (MDI: Scherrer et al., 1995) can be processed.
Additionally, user supplied full–disk images can also be analyzed.
The user can perform CH boundary detection, extraction and analysis us-
ing a manually adjustable intensity threshold. The threshold range, in which
reasonable CH boundaries can be extracted, can be derived from the intensity
histogram of the solar disk. After specifying a threshold, it is applied to the
full solar disk and the user may select the structure of interest to calculate its
parameters and to get an estimate of the boundary stability and uncertainty.
Then by varying the threshold to minimize the boundary uncertainty (ϵA), the
user can ﬁnd an optimized CH boundary in an easy and fast way, even without
previous experience in CH extraction. For deriving the properties of a CH,
CATCH analyzes ﬁve boundaries in an interval of 1 DN (data number) centered
around the selected threshold and calculates the mean values. The maximum
deviation of the derived values from the calculated mean is the uncertainty.
After extracting a satisfactory boundary from EUV ﬁltergrams, CATCH can
analyze the properties of the CH. The boundary may then be used on LoS
magnetograms (if available) to analyze the underlying photospheric magnetic
ﬁeld of the CH and its ﬁne structure represented by FTs. Figure 3 shows an
example of how to ﬁnd the optimal threshold by considering the uncertainty of
the extracted CH boundary. The red contour represents the CH boundary (of the
chosen threshold), the blue shaded areas are the uncertainties of the boundary.
The best boundary for this CH can be identiﬁed as shown in panel (d), where
the blue shaded area is smallest in comparison to the area enclosed in the CH
boundary.
CATCH calculates a variety of properties of the extracted CH, which include
morphological properties, the intensity, boundary stability as well as properties
of the underlying photospheric magnetic ﬁeld and its ﬁne structure (for the full
list of calculated parameters see Tab. 1). The calculations are based on the
studies by Hofmeister et al. (2017), Heinemann et al. (2018a), and Heinemann
et al. (2018b).
For proper image processing and analysis the SSW (SolarSoftWare) package
under IDL (Interactive Data Language) is required, therefore the tool is written
in SSW-IDL and the code, including an user-manual, is available on the au-
thors GitHub page (https://github.com/sgheinemann/CATCH) or by contacting
the author directly via E-mail1. Figure 4 shows the GUI structure of CATCH,
displaying the main menu, the data download widget as well as the CH extraction
and the magnetic ﬁeld analysis widget. A more detailed description of CATCH
and its functionalities can be found in the user-manual.
1For questions, suggestions and the code please contact the main developer S. G. Heinemann
via E-mail (stephan.heinemann@hmail.at).
SOLA: main.tex; 7 October 2019; 0:52; p. 4


## Page 5


CATCH
Table 1. Parameters calculated with CATCH.
Parametera
Unit
Description
ACH
km2
Deprojected CH Areab
¯I
DN
Mean EUV 193/195˚A Intensity
eI
DN
Median EUV 193/195˚A Intensity
λCoM
◦
Longitude of the Center of Mass (CoM) of the CH
λ+
◦
Maximum Longitudinal Westward extent
λ−
◦
Maximum Longitudinal Eastward extent
ϕCoM
◦
Latitude of the Center of Mass of the CH
ϕ+
◦
Maximum Latitudinal Northward extent
ϕ−
◦
Maximum Latitudinal Southward extent
ζ
Category factor: an estimate of the boundary stability
¯B
G
Signed mean magnetic ﬁeld strength
¯Bus
G
Unsigned mean magnetic ﬁeld strength
γB
Skewness of the magnetic ﬁeld distribution
Φs
Mx
Signed magnetic ﬂux
Φus
Mx
Unsigned magnetic ﬂux
RΦ
%
Flux balance: ratio of signed to unsigned magnetic ﬂux
NFT
Nr
Flux Tube Number
rΦ
%
Flux ratio: ratio of signed ﬂux from FTs to the signed CH ﬂux
rA
%
Area ratio: ratio of area of FTs to the CH area
a Note, that all magnetic ﬁeld parameters are calculated using Line-of-Sight mag-
netograms, which have been corrected for the assumption of radial magnetic ﬁeld:
Bi,corr =
Bi
cos(αi).
b The deprojection was done using a pixel wise correction with Ai,corr =
Ai
cos(αi) and α
being the angular distance from the disk center.
2.1. Coronal Hole Extraction from EUV 193/195 ˚
A Filtergrams
2.1.1. Intensity Threshold
The basic principle under which CH extraction operates is an intensity-based
threshold technique applied to EUV ﬁltergrams of suﬃcient contrast, which was
developed by Rotter et al. (2012). To ﬁnd an optimal threshold Krista and
Gallagher (2009) derived that an intensity distribution of the solar disk (or a
subﬁeld) with a CH present diﬀers signiﬁcantly from a distribution where CHs
are absent. Figure 1 shows as an example the intensity distribution of the solar
disk on May 29, 2013. Hereby, the ﬁrst maximum, seen at lower intensities,
represents one or multiple dark structures on the solar disk. It was proposed
that an optimal threshold for a CH boundary lies somewhere in the following
minimum. However, note that this characteristic shape is often not well estab-
lished, especially if no large and well deﬁned CHs are present on the solar disk.
Also, it has been found that there is a strong Solar Cycle dependence of the solar
disk EUV intensity distribution, which is additionally amended by the current
conditions on the Sun (e.g., increased abundance of dark structures or bright
SOLA: main.tex; 7 October 2019; 0:52; p. 5


## Page 6


S.G. Heinemann et al.
active regions). As such, neither a ﬁxed threshold nor a median-intensity depen-
dent threshold, which aims to mitigate intensity variation, perform continuously
well. Frequent manual adjustments are needed for optimized results. Thus, the
aim is to use an adjustable threshold depending on the current solar conditions,
both locally and globally.
2.1.2. Intensity Gradient, Uncertainty Estimation and Calculation of CH
Properties
The common intensity-based methods have the drawback that the threshold
range in which the boundary is considered optimal, is large (see Figure 1, shaded
area). To narrow down the range of reasonable thresholds, we propose an inten-
sity gradient method to estimate the boundary stability and give relevant errors
to calculated properties. Recent studies, investigating CHs and their boundaries,
have revealed a steep intensity gradient at the CH boundary (Hofmeister et al.,
2017). This is due to a strong decrease of the plasma density of quiet Sun
temperatures around 1.6 MK (Hahn, Landi, and Savin, 2011). Figure 2 shows
a representative intensity proﬁle perpendicular to the CH boundary layer, from
inside of the CH (x = 0) to outside (x = 1) in arbitrary scale. The y-axis shows
the intensity that is scaled to the maximum in this interval which represents the
quiet Sun intensity. We see that within a small layer the intensity drops by at
least 40% from the quiet Sun level. This small layer represents the range where
CH boundaries are usually extracted. Assuming that the CH boundary is best
represented where the intensity proﬁle is changing most strongly, we deﬁne the
optimum boundary to be placed at the steepest intensity gradient (i.e., gradient
has a maximum). In an ideal case, the implication of this deﬁnition is that
the boundary is approximately constant for small threshold variations around
the maximum intensity gradient threshold. This physical 1D principle of the
maximum intensity gradient perpendicular to the boundary can be extended
to 2D to consider the entire boundary instead of one localized cross–section.
This can be done by calculating the change of the CH area for a given intensity
threshold by varying the threshold slightly. Using the assumption of a similar
intensity gradient along the full boundary, a minimum in the change of the area
indicates that, on average, the boundary is located at the maximum gradient,
i.e. the optimal threshold.
With this deﬁnition of the boundary we aim to minimize the variations in
diﬀerent parameters (ﬁrst of all the area) to properly estimate the boundary.
Practically, this is done by calculating the parameters not only for the bound-
ary deﬁned by the selected threshold but also for boundaries of slightly larger
and smaller thresholds. From this set of boundaries, a mean value ( ¯P) and its
uncertainty (ϵP ) is calculated. The uncertainty corresponds to the maximum
deviation between the determined values and the mean value.
A reasonable CH boundary can be determined by ﬁnding the threshold that
minimizes ϵA (uncertainty in the CH area) and the CH properties are then given
as:
PCH = ¯P ± ϵP .
(1)
SOLA: main.tex; 7 October 2019; 0:52; p. 6


## Page 7


CATCH
2.2. Analysis of the Underlying Photospheric Magnetic Field
To extract and investigate CHs, it is not suﬃcient to only use the information
extracted from EUV ﬁltergrams as it lacks information about the underlying
magnetic structure. The magnetic ﬁeld conﬁguration is what distinguishes CHs
from other dark structures (e.g., ﬁlament channels, coronal dimmings) in the
solar corona. Studies suggest that it may be possible to diﬀerentiate those struc-
tures purely from intensity ﬁltergrams (Reiss et al., 2014) but a clear distinction
cannot always be made. A much more precise approach is the deﬁnition based
on the underlying magnetic ﬁeld (Reiss et al., 2015; Delouille et al., 2018). CHs
are deﬁned by their open magnetic ﬁeld conﬁguration which is reﬂected in the
ratio of the total signed to the unsigned magnetic ﬂux inside the CH and in the
skewness of the magnetic ﬁeld distribution. Filaments and ﬁlament channels on
the other hand ideally show a symmetric distribution between pixels of positive
and negative magnetic ﬂux (closed magnetic structures), as they are located
along polarity inversion lines. Thus, analyzing the magnetic ﬁeld underlying an
extracted dark structure reveals its magnetic conﬁguration and enables a clearer
classiﬁcation as CH or ﬁlament.
The calculation of the photospheric magnetic ﬁeld underlying a CH is often
performed by a simple projection of the EUV extracted boundary onto the
photospheric magnetogram (line–of–sight or radial). However, it is important
to stress that there are several uncertainties in the extraction. First of all, the
height diﬀerence between coronal imaging in EUV (EUV 193 ˚A: 1.01−1.05 R⊙)
and photospheric magnetic ﬁeld (1.00 R⊙). Second, the unknown expansion
of the magnetic ﬁeld over the EUV height. Simple projections will have an
increased eﬀect on the CH boundary the further it is located away from the
center of the solar disk. Another source of uncertainty arises from the noise
level, resolution and smoothing of the magnetogram. This can cause non-trivial
eﬀects on parameters like the unsigned magnetic ﬂux, ﬂux balance and skewness
of the magnetic ﬁeld. This complicates a comparison of magnetic ﬁeld proper-
ties derived from diﬀerently prepared magnetograms. When interpreting such
parameters a relative comparison should be preferred rather than relying on
absolute values.
Hofmeister et al. (2019) showed that the photospheric magnetic ﬁeld underly-
ing CHs can be divided into 3 categories: ≈22 ± 4% of the signed magnetic ﬂux
is contributed by a slightly unbalanced background ﬁeld. ≈5 ± 0.1% come from
small scale unipolar magnetic elements (ﬂux tubes, FTs) nearly symmetrically
distributed over both polarities and which are associated with the super-, meso-
, and granular motion of the photosphere. The major contribution, on average
≈69±8%, comes from strong and long-lived FTs which have almost exclusively
the dominant polarity of the CH. To map these properties, we calculate the
contribution of FTs to various CH parameters. We deﬁne two FT categories,
strong and weak (with the category weak also covering medium FTs; for more
details see Heinemann et al. 2018b). FTs are extracted as structures of pixels
above a magnetic ﬁeld strength of 20 G and the mean magnetic ﬁeld strength of
each structure determines the category. If the mean magnetic ﬁeld strength of
one FT is between an absolute value of 20 to 50 G it is categorized as weak, if
exceeding 50 G then it is considered strong.
SOLA: main.tex; 7 October 2019; 0:52; p. 7


## Page 8


S.G. Heinemann et al.
3. Statistical Analysis
3.1. Data and Data Processing
For the presented statistical study, we did not exhaust all the possibilities of
CATCH but constrained the used dataset to one spacecraft. SDO was chosen
over STEREO because of the availability of magnetic ﬁeld maps, and over SOHO
because of the better resolution and contrast. The dataset ranges from May 2010
until February 2019. The EUV 193˚A ﬁltergrams observed by AIA/SDO as well
LoS magnetograms from HMI/SDO were acquired in a 1 day cadence using the
Joint Science Operations Center Servers via the CATCH download application.
For the magnetograms the 720s LoS data product was preferred over the 45s due
to the lower photon noise of ≈3 G measured near the disk center and a better
signal-to-noise ratio (Couvidat et al., 2016).
The EUV ﬁltergrams and magnetograms were prepared to level 1.5 using
standard SSW-IDL routines and the EUV ﬁltergrams were down-scaled from a
pixel scale of 4096 × 4096 to 1024 × 1024 to signiﬁcantly enhance the processing
speed. Before the extraction, the full–disk ﬁltergrams were corrected for limb-
brightening using the anulus limb brightening correction (Verbeeck et al., 2014)
which is available in CATCH. The boundaries were smoothed using circular
(2–pixel radius) morphological operators (open and close). To avoid the loss of
information on the magnetic ﬁne structure, the magnetograms were not down-
scaled. The EUV extracted boundaries were re-scaled to ﬁt the magnetograms
resolution.
Note that the eﬀects on boundary detection as well as on the calculation of
the parameters in the EUV due to down-scaling are negligible. E.g., we tested
for an isolated CH, located close to the disk center on May 29, 2013 how the area
of the extracted CH changes for a ﬁxed threshold (43% of the median solar disk
intensity). By varying only the resolutions between 4096×4096 and 1024×1024,
(without smoothing) we ﬁnd a deviation of the extracted CH of less than 0.5%.
Other parameter behave similar. As such, the uncertainties from using diﬀerent
ﬁltergram resolutions to extract CH boundaries is much lower than uncertainties
in the extraction itself.
From the daily EUV images, dark structures located close to the central
meridian were extracted (Center of Mass, CoM located ±10o). The extracted
structures were limited to the central meridian to reduce longitudinal projec-
tion eﬀects due to the spherical nature of the Sun. Polar CHs as well as polar
connected CHs were excluded for the same reason. Each structure was extracted
only once for each solar disk passage to avoid statistical biases because of similar
datapoints. The magnetic properties of each dark structure were investigated
and non-CH structures were identiﬁed (deﬁned as structures with a ﬂux balance
below 10% or a magnetic ﬁeld skewness below 1) and discarded from further
analysis. This approach yielded 707 CHs over a wide range of sizes and latitudes
spanning a timerange of more than 8 years.
SOLA: main.tex; 7 October 2019; 0:52; p. 8


## Page 9


CATCH
3.2. Results
We analyzed 707 CHs near their central meridian passage and categorized them
by their boundary stability. All the parameters presented here, are calculated
with CATCH. Our ﬁndings are as follows:
3.2.1. Assessment of the Stability of the Extracted Boundaries
First, we assessed the stability of the extracted CH boundaries by analyzing ϵA
for the optimal threshold for all 707 CHs. Figure 5a shows the CH area (ACH)
against its uncertainty (ϵA). We ﬁnd a dependence on the area which seems
to have two causes: (1) the larger impact of stray light for smaller CHs which
could partly be compensated by performing a PSF deconvolution before the
CH extraction and (2) the non-zero extent of the boundary layer whose area
is growing linearly in contrast to the total CH area (which grows according to
a power law). This causes larger percentage variation for smaller CH areas. To
correct for this dependence we introduce the category factor (ζ) which can be
given as:
ζ =
ϵA
fﬁt(ACH),
(2)
with fﬁt(A) being the ﬁt shown in Figure 5a as the red line. It is given by:
fﬁt = 3.31 × (ACH)−0.53 + 4.71,
(3)
with ACH in units of 1010 km2. The resulting ζ-factor as function of CH area is
shown in Figure 5b. From this we deﬁne three categories of boundary stability:
i) high: ζ ≤1
ii) medium: 1 < ζ ≤2
iii) low: ζ > 2
We ﬁnd that 60.0% of the CHs under study have a high boundary stability,
34.2% a medium and only 5.8% are of low boundary stability.
3.2.2. Thresholds
Second, we investigated how the optimal threshold to extract CHs is distributed
and varies over the course of the observed time period from 2010 to 2019. This
period nearly covers the whole Solar Cycle 24. Figure 6 shows the threshold over
time (a) in absolute counts (DN) and (b) in percent of the median intensity of the
solar disk. The black line in panel (d) shows the smoothed daily sunspot number
by SIDC/SILSO2, which acts as a proxy of the solar activity. We ﬁnd a clear
Solar Cycle dependence in the optimal threshold (between 25 −55 DN) which
cannot be correctly mitigated by modulation with the median solar disk intensity
(of the full solar disk). It seems that the correction is too strong, especially
2The daily sunspot number can be found via SIDC/SILSO http://www.sidc.be/silso/.
SOLA: main.tex; 7 October 2019; 0:52; p. 9


## Page 10


S.G. Heinemann et al.
during solar minimum. Additionally, because of the individual conﬁguration of
CHs, the optimal threshold may vary by up to ≈20 DN for any given time.
The distribution of thresholds (in DN) is shown in Figure 7a (cyan) with a
mean of 43.9 DN and a standard deviation of 12.1 DN. The distribution shifts
from 53.5 ± 8.6 DN during solar maximum (red, 2012 −2014) to 29.7 ± 4.6 DN
during decline and minimum (blue, 2017-2019). When considering the threshold
in percent of the median solar disk intensity (Figure 7b), the mean threshold is
40.4±6.3% with a variation between the solar maximum (red, 2012−2014) with
37.3 ± 5.0% and the decline and minimum (blue, 2017-2019) with 46.2 ± 5.5%.
We ﬁnd the threshold to be independent of the CH size. We believe that the
large change of the optimal threshold (in DN) is due to the change in intensity
due to the Solar Cycle evolution (e.g., number of active regions, higher quiet Sun
level, ...). Figure 8 shows six CHs extracted with a diﬀerent optimal threshold,
varying from 25 to 65 DN.
3.2.3. Area, Intensity, and Position
After investigating the extraction mechanism in terms of intensity threshold, we
analyze how CH properties are distributed in our data-set. Figure 9 gives an
overview of the main CH properties, i.e., the distribution of the areas, latitudes,
and intensities of all CHs under study. Figure 9a shows the distribution of the
deprojected areas. We ﬁnd CH areas ranging from 1.6 × 109 km2 to 1.8 × 1011
km2, with an average of (2.69 ± 2.73) × 1010 km2. CHs with an area below
2 × 1010 km2 account for 56% of all CHs, whereas only 5% of CHs exceed an
area of 8 × 1010 km2.
The CoM of CHs under study are distributed over latitudes ranging from −63o
to +63o (Figure 9b). 39% of all CHs, which are located between an absolute value
of 40o and 20o, can be considered medium-latitude CHs and 50% are considered
low-latitude CHs, located below 20o. We ﬁnd the CHs to be nearly balanced
between the hemispheres (South: 48% CHs; North: 52% CHs) without a clear
relation to the solar activity (see Figure 6c).
We calculate the median and mean intensity in the 193 ˚A wavelength for
each CH of the dataset. The mean of the median intensities is calculated to be
29.0 ± 8.5 DN (Figure 9c) and the mean of the mean intensities is 29.5 ± 8.4
DN (Figure 9d). When only considering the 50% and 25% pixel with the lowest
intensities we ﬁnd the mean intensity to be 23.9 ± 7.4 DN and 21.2 ± 6.9 DN
respectively.
We investigated the intensity proﬁle of the cross-section of the CHs. To that
end we cut the CHs longitudinally through their CoM and superpose the inten-
sity proﬁles. Figure 10a shows the superposed mean proﬁle (black line) with the
1σ uncertainties represented by the shaded area and the second panel (b) shows
the derivative of the mean proﬁle. Note, that the intensity proﬁles were scaled so
that the CH boundaries correspond to x = ±1. We ﬁnd that when using CATCH
to extract CHs the boundary is consequently extracted at the highest gradient
in the intensity, which was the initial assumption. With this we can highlight
the CH extraction according to a physical principle in contrast to an arbitrarily
chosen (or empirically found) value.
SOLA: main.tex; 7 October 2019; 0:52; p. 10


## Page 11


CATCH
3.2.4. Properties of the Underlying Photospheric Magnetic Field
The analysis of the magnetic ﬁeld properties underlying the CHs yielded a near
symmetric distribution of positive and negative polarity CHs (Figure 11a). The
mean of the absolute values of the signed mean magnetic ﬁeld strength (|Bs|) is
2.9 ± 1.9 G (Figure 12c). There seems to be no correlation between |Bs| and the
CH area (Figure 12a; see also Figure 14). There is however a slight diﬀerence in
the distribution of |Bs| between the solar maximum against the decaying and
minimum phase. In the maximum (2012 −2014) the absolute value of the mean
magnetic ﬁeld strength exhibits a slightly higher average and a wider spread
with 3.4 ± 2.1 G than in the decaying phase and solar minimum (2017-2019)
with 1.6 ± 0.8 G (Figure 12b,c). The increased magnetic ﬁeld strengths within
CHs during solar maximum may be the result of enhanced magnetic activity
during the reversal of the solar magnetic ﬁeld which causes more active regions
to appear and consequently decay (Karachik, Pevtsov, and Abramenko, 2010). In
Figure 11b the unsigned mean magnetic ﬁeld strength is shown. We ﬁnd the mean
to be 7.3±1.9 G and that 90% of the CHs have a value below 10 G. We note, that
the unsigned magnetic ﬂux is strongly dependent on the magnetogram resolution
and smoothing, as it is dominated by the sum of the noise of the magnetic ﬁeld
pixel distribution. Therefore, the unsigned magnetic ﬂux should be considered
in relative comparison (e.g., between two CHs) rather than in absolute values.
This is also true for the skewness and the ﬂux balance. E.g., for the isolated CH
located near the disk center on May 29, 2013 the skewness changes from 9.2 at
a resolution of 4096 × 4096 to 7.4 at a resolution of 1024 × 1024, and the ﬂux
balance changes from 57.2% to 66.7%, respectively.
The signed magnetic ﬂuxes of the CHs seem to be symmetrically distributed
between both polarities. The mean of the absolute value is given at (7.2±13.5)×
1020 Mx with a maximum value of 6.9 × 1021 Mx. The unsigned magnetic ﬂuxes
range from 7.2 × 1019 to 2.0 × 1022 Mx with a mean of (2.0 ± 3.7) × 1021 Mx
(Figure 11c,d). The ﬂux balance, the ratio of the signed magnetic ﬂux to the
unsigned magnetic ﬂux and with that hinting towards open magnetic ﬂux, shows
that the CHs are distributed from 10% to 87% with a mean of 36, 3 ± 16.3%
(Figure 11e). The 47% of CHs that show positive polarity have a mean ﬂux
balance of 37.4 ± 16.7% whereas the 53% of CHs that show negative polarity
have a mean of −(35.6 ± 15.7)%. The shift in the magnetic ﬁeld distribution
that characterizes CHs is shown in Figure 11f. The mean of the absolute value
of the skewness is 8.2±2.1, clearly showing the asymmetry in the magnetic ﬁeld
caused by the abundance of open magnetic ﬁeld lines. There is no clear diﬀerence
between polarities or boundary categories.
3.2.5. Flux Tubes
Besides the magnetic parameters for the global structure of a CH, CATCH can
analyze the ﬁne structure of the magnetic ﬁeld in form of FTs or magnetic
elements. We analyzed the contribution of the small unipolar FTs categorized
as weak (20 G < |Bs,FT| < 50 G) and strong (|Bs,FT| > 50 G) to the CH
parameters. Figure 13 shows the distribution of FT number (a,b), area ratio (c,d)
SOLA: main.tex; 7 October 2019; 0:52; p. 11


## Page 12


S.G. Heinemann et al.
and ﬂux ratio (e,f) for weak and strong FTs respectively. There is no signiﬁcant
diﬀerence for the three categories of boundary stability. The number of extracted
FTs ranges from 15 to 2670 for the weak and from 1 to 223 for the strong FTs.
This gives an average of 135 ± 30 FTs per 1010 km2 for weak and 15 ± 6 FTs
per 1010 km2 for strong FTs. The number of strong FTs per area scales with the
signed mean magnetic ﬁeld strength of the CH (Pearson Correlation Coeﬃcient
(ccp): 0.74 with a 95% conﬁdence interval (CI) of [0.70, 0.78]), whereas the weak
ones do not (ccp = −0.12 with a 95% CI of [−0.18, −0.06]).
When analyzing the contribution of the weak and the strong FTs to the area
and signed magnetic ﬂux of the CH we ﬁnd that the strong ones are dominating.
For most CHs (90%) the contribution of the strong FTs to the signed magnetic
ﬂux is between 40% and 80% with a mean of 58.1 ± 13.1%, although they only
cover between 0.5% and 6% of the CHs area (on average 2.6±1.8%). We ﬁnd that
the coverage of the strong FTs is strongly correlated with the mean magnetic
ﬁeld strength of the CH (ccp = 0.98 with a 95% CI of [0.97, 0.98]). In contrast,
the weak FTs only contribute 16.3 ± 8.8% of the signed magnetic ﬂux and cover
a rather constant CH area of 1.5 −4% (84% of CHs) without a correlation to
the mean magnetic ﬁeld strength of the CH (ccp = −0.02 with a 95% CI of
[−0.07, 0.03]).
We note that in the Appendix, Figure 14 the pairwise Spearman correlation
coeﬃcients of all parameters calculated in the statistical study using CATCH
can be viewed. We note, that not all correlations imply a causal relationship,
but might be correlated by deﬁnition.
4. Discussion
Using the intensity proﬁle perpendicular to the boundary layer of CHs we were
able to improve the intensity-based threshold method by Rotter et al. (2012),
based on the concept initially proposed by Krista and Gallagher (2009). By
adding an estimation of the boundary stability and uncertainty, local as well
as global inﬂuences on the CH intensity can be described and compensated.
By investigating the performance of the newly adjusted threshold method we
highlight the advantages of such a supervised method.
4.1. CATCH
Reliable extraction of CHs from EUV observations is an important step towards
understanding their conﬁguration, a necessary aspect in solar- and space weather
research and space weather applications. Without a precise deﬁnition of the CH
boundaries, which is then applied to all CHs under study, an analysis is often bi-
ased by diﬀerences in the extracted boundary and by local conditions which lead
to signiﬁcant problems in the comparison of diﬀerent studies. Approaches that
aim to optimize a threshold for full–disk images (Rotter et al., 2012; Hofmeister
et al., 2017; Garton, Gallagher, and Murray, 2018) or synoptic maps (Hamada
et al., 2018) can adjust for global changes in the intensity distribution, but do
SOLA: main.tex; 7 October 2019; 0:52; p. 12


## Page 13


CATCH
not take into account the local variations. In another study, a dual–threshold–
based approach (ezseg: Caplan, Downs, and Linker (2016)) was developed with
the aim to consider local variations, if the threshold pair is properly tuned.
Our analysis yielded that the optimal threshold (as deﬁned in Section 2)
between CHs in one single ﬁltergram may vary signiﬁcantly due to the abundance
and proximity of active regions, quiet Sun areas and bright loops. Wendeln and
Landi (2018) found from diﬀerential emission measure analysis (DEM), that
a signiﬁcant contribution within CHs comes from stray light of nearby active
regions, high overlying loops and the instrumental point spread function (PSF).
It is reasonable to suggest that these eﬀects also inﬂuence the CH extraction in
one (or multiple) wavelengths. However, by individually assessing the boundary
of each CH, eﬀects coming from local conditions can be mitigated. We also tested
the inﬂuence of the PSF by deconvoluting the images before extraction (this
option is available in CATCH using SSW-routines) and found clear enhancement
in the extraction process but dismissed it for the statistical study because of the
greatly increased processing time (up to a factor 100). There are faster options
to perform PSF deconvolution when not using IDL (e.g., Prato et al., 2012),
which have not been explored yet as CATCH is entirely written in SSW–IDL.
The intensity proﬁle perpendicular to the CH boundary is very dependent
on the coronal conﬁguration outside the CH. Active regions have signiﬁcantly
higher intensities than the quiet Sun, but also loops associated with activity
near the CH boundary show increased intensities. Enhancements near and at
the boundaries may be the result of the CH evolution through the process
of interchange reconnection (Madjarska and Wiegelmann, 2009; Edmondson
et al., 2010; Yang et al., 2011). It is a known drawback of this method that
by considering the average gradient along the full CH boundary, small scale
conditions are neglected. The method approximates that the intensity gradient
across the boundary of a given CH is constant along the boundary, which we
know is not always true. This leads to uncertainties, which we approximate
as presented in Section 2.1. To consider such small scale variations, a much
more precise deﬁnition of the boundary needs to be established which requires
a new approach for detecting CH boundaries. Automated threshold techniques
are fast, but may extract several CHs in close vicinity which may or may not
appear with merged boundaries depending on slight variations in the threshold.
However, the threshold–based method described here delivers consistent results
when manually supervised. This is due to the constrains set by the boundary
gradient approach.
We therefore pursued to further develop this approach, having in mind the
advantages of being computationally very inexpensive, fast and ﬂexible. From
the statistical results we derive, we ﬁnd that our method consistently performs
well (by standards of visual inspection) over the changing conditions of a full
Solar Cycle and also mitigates local variations. Comparing to the method using
a ﬁxed intensity threshold of 35% of the median solar disk intensity (Vrˇsnak,
Temmer, and Veronig, 2007; Rotter et al., 2012; Reiss et al., 2016; Hofmeister
et al., 2017; Heinemann et al., 2018a), we ﬁnd signiﬁcant deviations for the
boundary we would consider as optimal. This is expected as automated methods
are often judged by how close they come to manual or manually–tuned methods.
SOLA: main.tex; 7 October 2019; 0:52; p. 13


## Page 14


S.G. Heinemann et al.
We also ﬁnd that the 35% of the median solar disk intensity is a good estimate
for the mean threshold during solar maximum (Figure 6b red line; Figure 7).
In our study the mean threshold for the time period of the solar maximum
(2012 −2014) comes to 37.3 ± 5.0% of the median solar disk intensity. This is
very well shown in the Solar Cycle dependence of the threshold (Figure 6). The
threshold may vary even up to 20 DN for a given ﬁltergram but is additionally
modulated by a global trend.
By considering all these factors we can highlight the importance of indi-
vidually extracting CHs without neglecting the local variations on CH size
scales. Although manual input is needed, the extraction method implemented in
CATCH aims to be as objective as possible without specifying any underlying
extraction conditions except for the approach of the boundary gradient.
4.2. Distribution over CHs of Solar Cycle 24
By analyzing the CHs of the SDO-era we not only gain a large sample of diﬀerent
CHs but also cover nearly one full Solar Cycle. As such, the sample includes CHs
from the rising phase (≈2010/2011), the maximum phase (≈2012 −2014), the
decaying and minimum phase (≈2015 −2019) of this cycle.
The CH parameters derived from the dataset are in good agreement with the
study of Hofmeister et al. (2017) who studied 288 low-latitude CHs near the
maximum of Solar Cycle 24 and are as such a subset of this study. They found
that the CH sizes are distributed around a median of 2.39 × 1010 km2 which is
very close to the value derived in this study with a mean area of (2.69 ± 2.73) ×
1010 km2. Note here that the mean is strongly biased by the large amount of
small CHs, of which a large portion is present in solar maximum. The spread
in the CH sizes may also be inﬂuenced by the few large CHs (5% of CHs with
an area exceeding 8 × 1010 km2). We excluded all polar and polar–connected
CHs (as manually deﬁned by the threshold tuning) from this statistical analysis
which removes some of the largest CHs observed in this period from the study.
This might be the reason why the extracted CH areas do not show the cycle
dependence found by the Solar Cycle study by Lowder, Qiu, and Leamon (2017).
The mean signed magnetic ﬁeld strength in our study shows a wider spread
and higher average during the maximum phase than during the decaying and
minimum phase. This was also previously stated by Harvey, Sheeley, and Harvey
(1982), who studied 33 CHs at 63 occasions and found that CHs near solar
minima have magnetic ﬁeld strengths ranging from 1 to 7 G, while those detected
near solar maxima, range from 3 to 36 G. In comparison, our values for the
maximum (3.4±2.1 G) are signiﬁcantly lower but for the minimum we are in good
agreement. The diﬀerence may be due to the use of diﬀerent instrumentation,
as it has been shown that diﬀerent instruments measure signiﬁcantly diﬀerent
magnetic ﬁelds (e.g., Liu et al., 2012). Statistically, we ﬁnd the mean absolute
value of the mean magnetic ﬁeld strength for all CHs under study to be 2.9±1.9
G distributed from 0.4 to 14.0 G. Results from other studies are found inside
this range (≈3 G: Bohlin and Sheeley 1978, 1−5 G: Obridko and Shelting 1989;
Belenko 2001). Considering the property of the CHs open magnetic ﬁeld conﬁg-
uration, we ﬁnd that the ﬂux balance, the ratio of the signed to the unsigned
SOLA: main.tex; 7 October 2019; 0:52; p. 14


## Page 15


CATCH
magnetic ﬂux which is a measure of the percentage of open ﬂux, is distributed
from 10 to 87% which overlaps with the range found by Hofmeister et al. (2017)
of 6 to 81%. A likely reason for the wide spread in the abundance of percentual
open ﬂux is that CHs of all evolutionary states are included in the dataset.
The open magnetic ﬁeld of the majority of CHs has been shown to possibly be
due to the mean magnetic ﬁeld strength which varies with the evolution of a
CH (Heinemann et al., 2018b). This evolutionary process seems to be governed
especially by interchange reconnection (Wang and Sheeley, 2004; Madjarska,
Doyle, and van Driel-Gesztelyi, 2004; Krista, Gallagher, and Bloomﬁeld, 2011;
Ma et al., 2014; Kong et al., 2018) and ﬂux emergence (Cranmer, 2009) and
references therein).
Hofmeister et al. (2017), Hofmeister et al. (2019), and Heinemann et al.
(2018b) found that the abundance of the strong unipolar magnetic elements
(ﬂux tubes) is what deﬁnes the magnetic conﬁguration of a CH. Notwithstanding
that they cover only a small fraction of the CH area they contribute a major
part of the total signed magnetic ﬂux of the CH. Hofmeister et al. (2017) found
that strong FTs cover 1% of the CHs area and contribute 38% to the signed
ﬂux. These values are slightly lower than the ones we found in our study with
rA = 2.6 ± 1.8% and rΦ = 58 ± 13%. This might be due to the diﬀerences in the
extraction and deﬁnition of the strong FTs. Our results are in better agreement
with the study of Heinemann et al. (2018b) who found values of rA
⩽
5%
and rΦ = 48 to 71%. The recent study by Hofmeister et al. (2019) found that
these strong FTs have lifetimes larger that those of supergranular cells essentially
making them the fundamental building blocks of CHs, and are not governed by
the photospheric network motion.
5. Summary
In this comprehensive study we investigated the intensity gradient across the
CH boundary to develop a new CH extraction method using an intensity-based
threshold method as well as to estimate the uncertainties of the extracted CH
boundaries. We successfully implemented the ﬂexible and fast method into an
easy-to-use GUI and applied it to the SDO-era to extract CHs. We created a
CH catalogue of considerable size covering the time period from May 2010 to
February 2019, which includes 707 non-polar CHs that were closely analyzed.
Our major ﬁndings can be summarized as follows:
i) By incorporating the principle of the maximum gradient into the intensity-
based threshold method we were able to:
• Create, for the ﬁrst time, CH boundaries with reasonable estimates for the
uncertainties
• Achieve a high consistency between boundaries extracted by diﬀerent users
• Develop an objective as possible CH extraction method, without disregard-
ing the advantages of manual user input
ii) Changes in the threshold due to small scale variations in the vicinity of CHs
as well as global intensity variations as a consequence of the Solar Cycle show
the importance of the individual extraction of a CH.
SOLA: main.tex; 7 October 2019; 0:52; p. 15


## Page 16


S.G. Heinemann et al.
iii) By implementing the code into an SSW-IDL GUI we provide an user friendly
environment for more objectively extracting CHs for scientiﬁc analysis, in-
cluding reasonable uncertainties.
iv) Using CATCH we created an extensive catalogue for the CHs observed by
SDO between its operational start in 2010 and February 2019. Over this era,
we extracted and analyzed 707 non-polar CHs and found them to exist in
sizes ranging from 1.6 × 109 to 1.8 × 1011 km2. Small CHs (< 2 × 1010 km2)
were found to be most abundant (56%). The strength of the photospheric
magnetic ﬁeld underlying the CHs is distributed around 2.9 ± 1.9 G which is
in agreement with most results found in literature and shows that CHs are
mostly covered by low magnetic ﬁeld.
v) We conﬁrm previous studies (Hofmeister et al., 2017; Heinemann et al., 2018b;
Hofmeister et al., 2019) that the magnetic conﬁguration of CHs is highly
dependent on the abundance and ﬁeld strength of the small unipolar magnetic
elements (ﬂux tubes), that only cover a small fraction of the CH area.
We plan to continue to develop CATCH. Planned major upgrades are the
(partial–) implementation in Python and the option to use synoptic magne-
tograms. Also compatibility with Parker Solar Probe and Solar Orbiter are
planned. New functionalities and upgrades will be published on GitHub and
future user manual versions.
Appendix
Figure 14 shows the Spearman correlation coeﬃcients of all the CH proper-
ties derived in the statistical analysis. The top right side shows representative
squares for all correlation coeﬃcients and additionally the signiﬁcance level is
marked with black asterisks (*** indicates a signiﬁcance level of p ≤0.001, **
indicates p ≤0.01 and * indicates p ≤0.05). The left bottom side shows the
values of the correlation coeﬃcient with insigniﬁcant values (cc with p > 0.05)
were omitted. The values have been converted to percent in order to improve
visualization. Positive values correspond to a correlation and negative values to
an anti–correlation. The parameters listed from left to right and top to bottom
are the following: the optimal threshold as described in Section 2.1 in percent of
the median solar disk intensity (Thr) and in DN (ThrDN); the CH area (ACH);
the mean CH intensity (¯I) and the mean intensities of the lowest 50% and 25%
percentile of pixel intensities within the CH (¯I50, ¯I25); the same for the median in-
tensities (eI, eI50, eI25); the longitudinal (|λCoM|) and latitudinal (|ϕCoM|) position
in absolute values; the absolute value of the signed mean magnetic ﬁeld strength
(| ¯Bs|) and the unsigned mean magnetic ﬁeld strength ( ¯Bus); the absolute value
of the signed magnetic ﬂux (|Φs|) and the unsigned magnetic ﬂux (Φus); the ﬂux
balance (RΦ) and the absolute value of the skewness of the magnetic ﬁeld (|γB|);
the FT number, area ratio and ﬂux ratio for both strong and weak FTs (NFT,s,
rA,s, rΦ,s, NFT,w, rA,w, rΦ,w).
SOLA: main.tex; 7 October 2019; 0:52; p. 16


## Page 17


CATCH
Figure 1. Normalized distribution of AIA/SDO 193 ˚A intensities of the solar disk on May
29, 2013 12UT (see inset). The maximum around 20 DN represents pixel located inside the
CH boundary and the shaded area the reasonable threshold range as proposed by Krista and
Gallagher (2009).
Acknowledgments
The SDO image data is available by courtesy of NASA and the re-
spective science teams. This research has made use of the VizieR catalogue access tool, CDS,
Strasbourg, France (DOI : 10.26093/cds/vizier). The original description of the VizieR service
was published in A&AS 143, 23. S.G.H., M.T., K.D., and A.M.V. acknowledge funding by the
Austrian Space Applications Programme of the Austrian Research Promotion Agency FFG
(859729, SWAMI, ASAP-11 4900217, CORDIM and ASAP-14 865972, SSCME). S.J.H. ac-
knowledges support from the JungforscherInnenfonds der Steierm¨arkischen Sparkassen. S.G.H.
thanks Evangelia Samara for providing the concept for the CATCH logo and Dr. Eleanna
Asvestari for her incitement, which signiﬁcantly enhanced the writing process. S.G.H. would
also like to thank Aaron Hernandez-Perez for his input and support. A big thanks goes to
all the testers of CATCH, who provided substantial feedback in improving it. We thank the
anonymous referee for constructive comments, which helped to improve the manuscript and
the tool. Disclosure of Potential Conﬂicts of Interest: The authors declare that they have no
conﬂicts of interest.
References
Altschuler, M.D., Newkirk, G.: 1969, Magnetic Fields and the Structure of the Solar Corona.
I: Methods of Calculating Coronal Fields. Solar Phys. 9(1), 131. DOI. ADS.
SOLA: main.tex; 7 October 2019; 0:52; p. 17


## Page 18


S.G. Heinemann et al.
 
CH
QS
Threshold
Maximum
Gradient
0.0
0.2
0.4
0.6
0.8
1.0
x
0.5
0.6
0.7
0.8
0.9
1.0
IScaled
0.0
0.2
0.4
0.6
0.8
1.0
dI/dx
Figure 2. A representative intensity proﬁle perpendicular to the CH boundary and its deriva-
tive. Both are scaled to the maximum (Imax = 1). The x-axis represents the radial distance
from inside of the CH (x = 0) across the boundary to the surrounding quiet Sun (x = 1).
Arge, C.N., Pizzo, V.J.: 2000, Improvement in the prediction of solar wind conditions using
near-real time solar magnetic ﬁeld updates. Journal of Geophysical Research 105, 10465.
DOI. http://adsabs.harvard.edu/abs/2000JGR...10510465A.
Asvestari, E., G., H.S., Temmer, M., Pomoell, J., Kilpua, E., Magdalenic, J., Poedts, S.: 2019,
. J. Geophys. Res.. DOI.
Belenko, I.A.: 2001, Coronal Hole Evolution During 1996-1999. Solar Phys. 199(1), 23. DOI.
ADS.
Bohlin, J.D., Sheeley, N.R. Jr.: 1978, Extreme ultraviolet observations of coronal holes. II -
Association of holes with solar magnetic ﬁelds and a model for their formation during the
solar cycle. Solar Phys. 56, 125. DOI. ADS.
Boucheron, L.E., Valluri, M., McAteer, R.T.J.: 2016, Segmentation of coronal holes using active
contours without edges. Solar Physics 291(8), 2353. DOI. https://doi.org/10.1007/s11207-
016-0985-z.
Caplan, R.M., Downs, C., Linker, J.A.: 2016, Synchronic Coronal Hole Mapping Using Multi-
instrument EUV Images: Data Preparation and Detection Method. Astrophys. J. 823, 53.
DOI. ADS.
Couvidat, S., Schou, J., Hoeksema, J.T., Bogart, R.S., Bush, R.I., Duvall, T.L., Liu, Y., Norton,
A.A., Scherrer, P.H.: 2016, Observables Processing for the Helioseismic and Magnetic Imager
Instrument on the Solar Dynamics Observatory. Solar Phys. 291, 1887. DOI. ADS.
Cranmer, S.R.: 2002, Coronal Holes and the High-Speed Solar Wind.
Space Sci. Rev. 101,
229. ADS.
Cranmer, S.R.: 2009, Coronal Holes. Living Reviews in Solar Physics 6, 3. DOI. ADS.
Delaboudini`ere, J.-P., Artzner, G.E., Brunaud, J., Gabriel, A.H., Hochedez, J.F., Millier, F.,
Song, X.Y., Au, B., Dere, K.P., Howard, R.A., Kreplin, R., Michels, D.J., Moses, J.D.,
Deﬁse, J.M., Jamar, C., Rochus, P., Chauvineau, J.P., Marioge, J.P., Catura, R.C., Lemen,
SOLA: main.tex; 7 October 2019; 0:52; p. 18


## Page 19


CATCH
and the blue shaded areas are the uncertainties as described in Section 2.1. Panel
(a) shows the CH without boundaries and panel (b) with the CH boundary of
a threshold of 31 DN which gives an uncertainty of ϵA = 47%. In panel (c) a
threshold of 37 DN is used which gives an uncertainty of ϵA = 16%. The best
boundary for this case (e.g., the lowest uncertainty) is reached with a threshold
of 41 DN and is shown in panel (d) with ϵA = 10%.
Figure 3. Example images of boundary extraction of a CH on August 31, 2014. The red line
is the CH boundary (of the chosen threshold)
J.R., Shing, L., Stern, R.A., Gurman, J.B., Neupert, W.M., Maucherat, A., Clette, F.,
Cugnon, P., van Dessel, E.L.: 1995, EIT: Extreme-Ultraviolet Imaging Telescope for the
SOHO Mission. Solar Phys. 162, 291. DOI. ADS.
Delouille,
V.,
Hofmeister,
S.J.,
Reiss,
M.A.,
Mampaey,
B.,
Temmer,
M.,
Veronig,
A.:
2018,
Chapter
15
-
coronal
holes
detection
using
supervised
classiﬁcation.
In:
Camporeale,
E.,
Wing,
S.,
Johnson,
J.R.
(eds.)
Machine
Learning
Tech-
niques
for
Space
Weather,
Elsevier,
???,
365
.
ISBN
978-0-12-811788-0.
DOI.
http://www.sciencedirect.com/science/article/pii/B9780128117880000159.
Domingo, V., Fleck, B., Poland, A.I.: 1995, The SOHO Mission: an Overview. Solar Phys.
162, 1. DOI. ADS.
Edmondson, J.K., Antiochos, S.K., DeVore, C.R., Lynch, B.J., Zurbuchen, T.H.: 2010, In-
terchange Reconnection and Coronal Hole Dynamics.
Astrophys. J. 714, 517. DOI.
SOLA: main.tex; 7 October 2019; 0:52; p. 19


## Page 20


S.G. Heinemann et al.
Main Menu
Data Download
Coronal Hole Extraction
Magnetic Field Analysis
GUI showing the main menu (left bottom), the data download application (right
bottom), the coronal hole extraction option (left top) and the option for the
magnetic ﬁeld analysis (right top).
Figure 4. Screenshots of the CATCH
ADS.
Garton, T.M., Gallagher, P.T., Murray, S.A.: 2018, Automated coronal hole identiﬁcation via
multi-thermal intensity segmentation. Journal of Space Weather and Space Climate 8(27),
A02. DOI. ADS.
Hahn, M., Landi, E., Savin, D.W.: 2011, Diﬀerential Emission Measure Analysis of a Polar
Coronal Hole during the Solar Minimum in 2007. Astrophys. J. 736(2), 101. DOI. ADS.
Hamada, A., Asikainen, T., Virtanen, I., Mursula, K.: 2018, Automated Identiﬁcation of
Coronal Holes from Synoptic EUV Maps. Solar Phys. 293, 71. DOI. ADS.
Harvey, K.L., Sheeley, N.R. Jr., Harvey, J.W.: 1982, Magnetic measurements of coronal holes
during 1975-1980. Solar Phys. 79, 149. DOI. ADS.
Heinemann, S.G., Temmer, M., Hofmeister, S.J., Veronig, A.M., Vennerstrøm, S.: 2018a, Three-
phase Evolution of a Coronal Hole. I. 360◦Remote Sensing and In Situ Observations.
Astrophys. J. 861, 151. DOI. ADS.
Heinemann, S.G., Hofmeister, S.J., Veronig, A.M., Temmer, M.: 2018b, Three-phase Evolution
of a Coronal Hole. II. The Magnetic Field. Astrophys. J. 863, 29. DOI. ADS.
Hofmeister, S.J., Veronig, A., Reiss, M.A., Temmer, M., Vennerstrom, S., Vrˇsnak, B., Heber,
B.: 2017, Characteristics of Low-latitude Coronal Holes near the Maximum of Solar Cycle
24. Astrophys. J. 835, 268. DOI. ADS.
Hofmeister, S.J., Veronig, A., Temmer, M., Vennerstrom, S., Heber, B., Vrˇsnak, B.: 2018, The
Dependence of the Peak Velocity of High-Speed Solar Wind Streams as Measured in the
Ecliptic by ACE and the STEREO satellites on the Area and Co-latitude of Their Solar
Source Coronal Holes. Journal of Geophysical Research (Space Physics) 123, 1738. DOI.
ADS.
Hofmeister, S.J., Utz, D., Heinemann, S.G., Veronig, A.M., Temmer, M.: 2019, The Magnetic
Structure of Coronal Holes. Astron. Astrophys.. DOI.
Howard, R.A., Moses, J.D., Vourlidas, A., Newmark, J.S., Socker, D.G., Plunkett, S.P., Ko-
rendyke, C.M., Cook, J.W., Hurley, A., Davila, J.M., Thompson, W.T., St Cyr, O.C.,
SOLA: main.tex; 7 October 2019; 0:52; p. 20


## Page 21


CATCH
Figure 5. Panel (a) shows a scatterplot of the CH area against its maximum deviation as
given in Section 2.1. The red line shows the ﬁt which is used to calculate the category factor (ζ).
ζ is plotted against the area in panel (b). The shaded areas (green, orange and red) represent
the stability assessment of the boundaries as high, medium and low respectively.
Mentzell, E., Mehalick, K., Lemen, J.R., Wuelser, J.P., Duncan, D.W., Tarbell, T.D.,
Wolfson, C.J., Moore, A., Harrison, R.A., Waltham, N.R., Lang, J., Davis, C.J., Eyles,
C.J., Mapson-Menard, H., Simnett, G.M., Halain, J.P., Deﬁse, J.M., Mazy, E., Rochus, P.,
Mercier, R., Ravet, M.F., Delmotte, F., Auchere, F., Delaboudiniere, J.P., Bothmer, V.,
Deutsch, W., Wang, D., Rich, N., Cooper, S., Stephens, V., Maahs, G., Baugh, R., Mc-
Mullin, D., Carter, T.: 2008, Sun Earth Connection Coronal and Heliospheric Investigation
(SECCHI). Space Sci. Rev. 136, 67. DOI. ADS.
Huang, G.-H., Lin, C.-H., Lee, L.-C.: 2019, Examination of the EUV Intensity in the Open
Magnetic Field Regions Associated with Coronal Holes. Astrophys. J. 874, 45. DOI. ADS.
Illarionov, E.A., Tlatov, A.G.: 2018, Segmentation of coronal holes in solar disc images with a
convolutional neural network. Mon. Not. Roy. Astron. Soc. 481, 5014. DOI. ADS.
Kaiser, M.L., Kucera, T.A., Davila, J.M., St. Cyr, O.C., Guhathakurta, M., Christian, E.:
2008, The STEREO Mission: An Introduction. Space Sci. Rev. 136, 5. DOI. ADS.
Karachik, N.V., Pevtsov, A.A., Abramenko, V.I.: 2010, Formation of Coronal Holes on the
Ashes of Active Regions. Astrophys. J. 714(2), 1672. DOI. ADS.
Kong, D.F., Pan, G.M., Yan, X.L., Wang, J.C., Li, Q.L.: 2018, Observational Evidence of
Interchange Reconnection between a Solar Coronal Hole and a Small Emerging Active
Region. Astrophys. J. 863(2), L22. DOI. ADS.
Krista, L.D., Gallagher, P.T.: 2009, Automated Coronal Hole Detection Using Local Intensity
Thresholding Techniques. Solar Phys. 256, 87. DOI. ADS.
Krista, L.D., Gallagher, P.T., Bloomﬁeld, D.S.: 2011, Short-term Evolution of Coronal Hole
Boundaries. Astrophys. J. 731(2), L26. DOI. ADS.
Lemen, J.R., Title, A.M., Akin, D.J., Boerner, P.F., Chou, C., Drake, J.F., Duncan, D.W.,
Edwards, C.G., Friedlaender, F.M., Heyman, G.F., Hurlburt, N.E., Katz, N.L., Kushner,
SOLA: main.tex; 7 October 2019; 0:52; p. 21


## Page 22


S.G. Heinemann et al.
the often used threshold value of 35% of the median solar disk intensity. The
errorbars indicate the variation of the threshold for the uncertainty estimation
as described in Section 2.1. The third panel (c) shows the latitudinal positions
of the CoMs of the CHs under study. The bottom panel (d) shows the smoothed
daily sunspot number as provided by the SIDC/SILSO. The black line is the
total sunspot number while the red and blue lines show the sunspot number for
the northern and southern hemisphere respectively.
Figure 6. Evolution of the optimal intensity threshold for CH extraction as function of time.
Panel (a) shows the intensity in counts (DN) and panel (b) shows the threshold in percent of
the median intensity of the solar disk at the time of the extraction. The blue line represents
the mean value and the blue shaded area the 1σ range over the whole period studied. The
dashed-red line in panel (b) represents
G.D., Levay, M., Lindgren, R.W., Mathur, D.P., McFeaters, E.L., Mitchell, S., Rehse,
R.A., Schrijver, C.J., Springer, L.A., Stern, R.A., Tarbell, T.D., Wuelser, J.-P., Wolfson,
C.J., Yanari, C., Bookbinder, J.A., Cheimets, P.N., Caldwell, D., Deluca, E.E., Gates, R.,
Golub, L., Park, S., Podgorski, W.A., Bush, R.I., Scherrer, P.H., Gummin, M.A., Smith,
P., Auker, G., Jerram, P., Pool, P., Souﬂi, R., Windt, D.L., Beardsley, S., Clapp, M., Lang,
J., Waltham, N.: 2012, The Atmospheric Imaging Assembly (AIA) on the Solar Dynamics
Observatory (SDO). Solar Phys. 275, 17. DOI. ADS.
Linker, J.A., Caplan, R.M., Downs, C., Riley, P., Mikic, Z., Lionello, R., Henney, C.J., Arge,
C.N., Liu, Y., Derosa, M.L., Yeates, A., Owens, M.J.: 2017, The open ﬂux problem. The
Astrophysical Journal 848(1), 70. DOI. https://doi.org/10.3847%2F1538-4357%2Faa8a70.
Liu, Y., Hoeksema, J.T., Scherrer, P.H., Schou, J., Couvidat, S., Bush, R.I., Duvall, T.L.,
Hayashi, K., Sun, X., Zhao, X.: 2012, Comparison of Line-of-Sight Magnetograms Taken
by the Solar Dynamics Observatory/Helioseismic and Magnetic Imager and Solar and
SOLA: main.tex; 7 October 2019; 0:52; p. 22


## Page 23


CATCH
 
20
30
40
50
60
70
Threshold [DN]
0
10
20
30
40
50
60
N
 
25
30
35
40
45
50
55
60
Threshold [%]
0
10
20
30
40
50
60
N
2010-2019
2012-2014
2017-2019
2010-2019
2012-2014
2017-2019
(a)
(b)
Figure 7. Distribution of the optimal threshold during the entire SDO-era (cyan), covering
solar maximum (red) and the decline and minimum phase (blue). Panel (a) shows the threshold
in absolute counts (DN) and panel (b) in percent of the median solar disk intensity.
Heliospheric Observatory/Michelson Doppler Imager. Solar Phys. 279(1), 295. DOI. ADS.
Lowder, C., Qiu, J., Leamon, R.: 2017, Coronal Holes and Open Magnetic Flux over Cycles
23 and 24. Solar Phys. 292(1), 18. DOI. ADS.
Lowder, C., Qiu, J., Leamon, R., Liu, Y.: 2014, Measurements of EUV Coronal Holes and
Open Magnetic Flux. Astrophys. J. 783, 142. DOI. ADS.
Ma, L., Qu, Z.-Q., Yan, X.-L., Xue, Z.-K.: 2014, Interchange reconnection between an active
region and a coronal hole. Research in Astronomy and Astrophysics 14(2), 221. DOI. ADS.
Madjarska, M.S., Wiegelmann, T.: 2009, Coronal hole boundaries evolution at small scales. I.
EIT 195 ˚A and TRACE 171 ˚Aview. Astron. Astrophys. 503, 991. DOI. ADS.
Madjarska, M.S., Doyle, J.G., van Driel-Gesztelyi, L.: 2004, Evidence of Magnetic Reconnection
along Coronal Hole Boundaries. Astrophys. J. 603(1), L57. DOI. ADS.
Nolte, J.T., Krieger, A.S., Timothy, A.F., Gold, R.E., Roelof, E.C., Vaiana, G., Lazarus, A.J.,
Sullivan, J.D., McIntosh, P.S.: 1976, Coronal holes as sources of solar wind. Solar Phys. 46,
303. DOI. ADS.
Obridko, V.N., Shelting, B.D.: 1989, Coronal holes as indicators of large-scale magnetic ﬁelds
in the corona. Solar Phys. 124(1), 73. DOI. ADS.
Ochsenbein, F., Bauer, P., Marcout, J.: 2000, The VizieR database of astronomical catalogues.
Astron. Astrophys. Suppl. 143, 23. DOI. ADS.
Odstrˇcil, D., Pizzo, V.J.: 1999, Three-dimensional propagation of CMEs in a structured solar
wind ﬂow: 1. CME launched within the streamer belt.
J. Geophys. Res. 104, 483. DOI.
ADS.
Pesnell, W.D., Thompson, B.J., Chamberlin, P.C.: 2012, The Solar Dynamics Observatory
(SDO). Solar Phys. 275, 3. DOI. ADS.
Pinto, R.F., Rouillard, A.P.: 2017, A Multiple Flux-tube Solar Wind Model.
Astrophys. J.
838, 89. DOI. ADS.
SOLA: main.tex; 7 October 2019; 0:52; p. 23


## Page 24


S.G. Heinemann et al.
Figure 8. Sample of CHs extracted with varying optimal thresholds (as deﬁned in Section 2.1).
The sample represents the threshold value distribution as given in Figure 7. The optimal
thresholds range form 25 to 65 DN and are primarily caused by a diﬀerent intensity quiet
Sun level rather than large changes in the CH intensity. The red boundary corresponds to the
boundary derived by the optimal threshold and the blue shaded areas are the uncertainties
(see Section 2.1.2). All images are equally scaled.
Pomoell, J., Poedts, S.: 2018, EUHFORIA: European heliospheric forecasting information
asset. Journal of Space Weather and Space Climate 8(27), A35. DOI. ADS.
Prato, M., Cavicchioli, R., Zanni, L., Boccacci, P., Bertero, M.: 2012, Eﬃcient deconvolution
methods for astronomical imaging: algorithms and IDL-GPU codes.
Astron. Astrophys.
539, A133. DOI. ADS.
Raymond, J.C., Doyle, J.G.: 1981, The energy balance in coronal holes and average quiet-sun
regions. Astrophys. J. 247, 686. DOI. ADS.
Reiss, M.A., Hofmeister, S.J., De Visscher, R., Temmer, M., Veronig, A.M., Delouille, V.,
Mampaey, B., Ahammer, H.: 2015, Improvements on coronal hole detection in SDO/AIA
images using supervised classiﬁcation. Journal of Space Weather and Space Climate 5, A23.
DOI. ADS.
Reiss, M.A., Temmer, M., Veronig, A.M., Nikolic, L., Vennerstrom, S., Sch¨ongassner, F.,
Hofmeister, S.J.: 2016, Veriﬁcation of high-speed solar wind stream forecasts using
operational solar wind models. Space Weather 14, 495. DOI. ADS.
Reiss, M., Temmer, M., Rotter, T., Hofmeister, S.J., Veronig, A.M.: 2014, Identiﬁcation of
coronal holes and ﬁlament channels in SDO/AIA 193˚A images via geometrical classiﬁcation
methods. Central European Astrophysical Bulletin 38, 95. ADS.
Riley, P., Linker, J.A., Lionello, R., Mikic, Z.: 2012, Corotating interaction regions during
the recent solar minimum: The power and limitations of global MHD modeling. Journal of
Atmospheric and Solar-Terrestrial Physics 83, 1. DOI. ADS.
Rotter, T., Veronig, A.M., Temmer, M., Vrˇsnak, B.: 2012, Relation Between Coronal Hole
Areas on the Sun and the Solar Wind Parameters at 1 AU. Solar Phys. 281, 793. DOI.
ADS.
Rotter, T., Veronig, A.M., Temmer, M., Vrˇsnak, B.: 2015, Real-Time Solar Wind Prediction
Based on SDO/AIA Coronal Hole Data. Solar Phys. 290(5), 1355. DOI. ADS.
SOLA: main.tex; 7 October 2019; 0:52; p. 24


## Page 25


CATCH
 
0
2
4
6
8
10
12
14
ACH [10
10 km
2]
0
50
100
150
200
250
N
 
Binsize = 10
-60
-40
-20
0
20
40
60
φ [°]
0
20
40
60
80
100
120
N
 
Binsize = 2
10
20
30
40
50
IMedian [DN]
0
20
40
60
80
N
 
Binsize = 2
10
20
30
40
50
IMean [DN]
0
20
40
60
80
N
high
medium
low
(a)
(b)
(c)
(d)
Figure 9. Distribution of CH properties sorted corresponding to the category factor (green:
high, orange: medium and red: low). Panel (a) show the area distribution, panel (b) the
distribution of the latitudinal location of the center of mass and the panels (c) and (d) show
the distribution of the median and mean intensity within the extracted CH boundaries.
Scherrer, P.H., Bogart, R.S., Bush, R.I., Hoeksema, J.T., Kosovichev, A.G., Schou, J., Rosen-
berg, W., Springer, L., Tarbell, T.D., Title, A., Wolfson, C.J., Zayer, I., MDI Engineering
Team: 1995, The Solar Oscillations Investigation - Michelson Doppler Imager. Solar Phys.
162, 129. DOI. ADS.
Schou, J., Scherrer, P.H., Bush, R.I., Wachter, R., Couvidat, S., Rabello-Soares, M.C., Bogart,
R.S., Hoeksema, J.T., Liu, Y., Duvall, T.L., Akin, D.J., Allard, B.A., Miles, J.W., Rairden,
R., Shine, R.A., Tarbell, T.D., Title, A.M., Wolfson, C.J., Elmore, D.F., Norton, A.A.,
Tomczyk, S.: 2012, Design and Ground Calibration of the Helioseismic and Magnetic Imager
(HMI) Instrument on the Solar Dynamics Observatory (SDO). Solar Phys. 275, 229. DOI.
ADS.
Schwenn, R.: 2006, Solar Wind Sources and Their Variations Over the Solar Cycle. Space Sci.
Rev. 124, 51. DOI. ADS.
Temmer, M., Hinterreiter, J., Reiss, M.A.: 2018, Coronal hole evolution from multi-viewpoint
data as input for a stereo solar wind speed persistence model. J. Space Weather Space Clim.
8, A18. DOI. https://doi.org/10.1051/swsc/2018007.
Tokumaru, M., Satonaka, D., Fujiki, K., Hayashi, K., Hakamada, K.: 2017, Relation Between
Coronal Hole Areas and Solar Wind Speeds Derived from Interplanetary Scintillation
Measurements. Solar Phys. 292, 41. DOI. ADS.
Verbeeck, C., Delouille, V., Mampaey, B., De Visscher, R.: 2014, The SPoCA-suite: Software
for extraction, characterization, and tracking of active regions and coronal holes on EUV
images. Astron. Astrophys. 561, A29. DOI. ADS.
Vrˇsnak, B., Temmer, M., Veronig, A.M.: 2007, Coronal Holes and Solar Wind High-Speed
Streams: I. Forecasting the Solar Wind Parameters. Solar Phys. 240, 315. DOI. ADS.
SOLA: main.tex; 7 October 2019; 0:52; p. 25


## Page 26


S.G. Heinemann et al.
 
QS
QS
CH
-2
-1
0
1
2
x
0
20
40
60
80
100
120
140
I [DN]
 
QS
QS
CH
-2
-1
0
1
2
x
0.0
0.2
0.4
0.6
0.8
1.0
dI/dx
(a)
(b)
Figure 10. The superposed intensity proﬁle of the longitudinal cross-sections at the CoM of
the CHs under study (a) and its derivative (b). Before superposing, each intensity proﬁle is
scaled so that x ± 1 represents the CH boundaries. The black line is the mean proﬁle and the
shaded gray-blue area represents the 1σ standard deviation. The dotted vertical lines mark
the location of the CH boundary.
Wallace, S., Arge, C.N., Pattichis, M., Hock-Mysliwiec, R.A., Henney, C.J.: 2019, Estimating
Total Open Heliospheric Magnetic Flux. Solar Phys. 294, 19. DOI. ADS.
Wang, Y.-M., Sheeley, J. N. R.: 2004, Footpoint Switching and the Evolution of Coronal Holes.
Astrophys. J. 612(2), 1196. DOI. ADS.
Wendeln, C., Landi, E.: 2018, EUV Emission and Scattered Light Diagnostics of Equatorial
Coronal Holes as Seen by Hinode/EIS. Astrophys. J. 856, 28. DOI. ADS.
Yang, S., Zhang, J., Li, T., Liu, Y.: 2011, SDO Observations of Magnetic Reconnection At
Coronal Hole Boundaries. Astrophys. J. Lett. 732, L7. DOI. ADS.
SOLA: main.tex; 7 October 2019; 0:52; p. 26


## Page 27


CATCH
 
Binsize = 0.5
-10
-5
0
5
10
Bs [G]
0
10
20
30
40
50
60
70
N
 
Binsize = 0.5
5
10
15
20
Bus [G]
0
20
40
60
80
N
 
Binsize = 2
-30 -20 -10
0
10
20
30
Φs [10
20 Mx]
0
20
40
60
80
100
120
N
 
Binsize = 2
0
10
20
30
40
50
60
70
Φus [10
20 Mx]
0
20
40
60
80
100
N
 
Binsize = 5
-50
0
50
ΦB [%]
0
10
20
30
40
50
60
N
 
Binsize = 1
-15
-10
-5
0
5
10
15
γB
0
20
40
60
80
N
high
medium
low
(a)
(b)
(c)
(d)
(e)
(f)
Figure 11. Distribution of magnetic CH properties sorted corresponding to the category
factor (green: high, orange: medium and red: low). Panels (a) and (b) show the distribution of
the signed and unsigned mean magnetic ﬁeld strength of the photospheric ﬁeld below the CH.
The distributions of the signed and unsigned ﬂux are shown in the panels (c) and (d). The ﬂux
balance, the ratio between the signed and unsigned magnetic ﬂux is shown in panel (e). Panel
(f) shows the distribution of the values for the skewness of the magnetic ﬁeld distribution.
SOLA: main.tex; 7 October 2019; 0:52; p. 27


## Page 28


S.G. Heinemann et al.
 
0.1
1.0
10.0
ACH [10
10 km
2]
1
10
|Bs| [G]
 
2011 2012 2013 2014 2015 2016 2017 2018 2019
Time [Year]
1
10
|Bs| [G]
 
0
2
4
6
8
10
|Bs| [G]
0
20
40
60
80
100
120
N
2010-2019
2012-2014
2017-2019
(a)
(b)
(c)
Figure 12. In panel (a) the CH area is plotted against the absolute value of the signed mean
magnetic ﬁeld strength (|Bs|) in double logarithmic depiction. Panel (b) gives the temporal
evolution of the absolute value of the signed mean magnetic ﬁeld strength (y-axis is logarith-
mically scaled). Panel (c) shows the distribution of |Bs| for the whole dataset in cyan, for the
solar maximum in red and for the declining phase and the minimum in blue.
SOLA: main.tex; 7 October 2019; 0:52; p. 28


## Page 29


CATCH
 
Binsize = 50
NFT,w
0
20
40
60
80
100
120
140
N
 
Binsize = 10
NFT,s
0
50
100
150
200
N
 
Binsize = 0.5
0
2
4
6
8
rA,w [%]
0
50
100
150
200
250
N
 
Binsize = 0.5
0
2
4
6
8
rA,s [%]
0
20
40
60
80
100
120
140
N
 
Binsize = 5
0
10
20
30
40
50
60
rφ,w [%]
0
50
100
150
200
250
N
 
Binsize = 5
0
20
40
60
80
100
rφ,s [%]
0
20
40
60
80
100
120
140
N
0
200
400
600
800
1000
1200
1400
0
20
40
60
80
100
120
140
high
medium
low
(a)
(b)
(c)
(d)
(e)
(f)
Figure 13. Distribution of FT properties within the CH sorted corresponding to the category
factor (green: high, orange: medium and red: low). Panels (a) and (b) show the distribution of
the number of FTs per CH (weak and strong respectively). The distribution of the area ratio
of FTs for weak and strong FTs is shown in panel (c) and (d). Panels (e) and (f) show the
distribution of the FT ﬂux ratio for weak and strong FTs.
SOLA: main.tex; 7 October 2019; 0:52; p. 29


## Page 30


S.G. Heinemann et al.
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
−100
−75
−50
−25
0
25
50
75
100
Thr
ThrDN
ACH
I
I50
I25
I~
I~
50
I~
25
 λCoM
 ϕCoM
 Bs
Bus
 Φs
Φus
RΦ
γB
NFT, s
rA, s
rΦ, s
NFT, w
rA, w
rΦ, w
Thr
ThrDN
ACH
I
I50
I25
I~
I~
50
I~
25
 λCoM
 ϕCoM
 Bs
Bus
 Φs
Φus
RΦ
γB
NFT, s
rA, s
rΦ, s
NFT, w
rA, w
rΦ, w
100
58
57
9
0
−13
4
−1
−11
−5
−11
−10
2
42
54
−10
2
54
−1
25
53
3
−27
100
29
54
44
36
48
43
36
5
−36
−26
−16
8
19
−28
−21
20
−18
−12
29
−10
−6
100
−32
−46
−60
−36
−47
−58
4
36
10
51
85
97
−8
10
93
23
34
99
35
−25
100
96
90
99
95
90
17
−68
−55
−60
−50
−41
−44
−20
−42
−49
−32
−32
−33
0
100
97
97
100
97
10
−67
−51
−60
−60
−53
−40
−16
−53
−47
−34
−46
−34
6
100
91
97
100
8
−63
−44
−59
−68
−65
−31
−16
−62
−42
−38
−60
−34
12
100
96
91
15
−69
−58
−62
−55
−45
−47
−17
−47
−52
−34
−36
−34
3
100
97
11
−68
−50
−60
−60
−54
−38
−17
−53
−46
−36
−48
−33
8
100
8
−63
−44
−59
−66
−63
−32
−15
−60
−42
−37
−58
−34
10
100
−3
−11
2
3
6
−5
−42
2
−11
−46
8
20
52
100
71
85
68
53
57
18
52
68
41
43
77
−9
100
82
59
29
96
43
39
96
59
14
46
−34
100
83
66
67
19
68
87
50
55
76
−22
100
93
44
30
95
68
57
86
55
−38
100
12
16
97
40
45
97
47
−29
100
39
23
91
50
−5
35
−28
100
22
40
68
6
−25
−56
100
50
50
92
42
−37
100
62
26
49
−40
100
35
6
−84
100
42
−25
100
17
100
Thr
ThrDN
ACH
I
I50
I25
I~
I~
50
I~
25
 λCoM
 ϕCoM
 Bs
Bus
 Φs
Φus
RΦ
γB
NFT, s
rA, s
rΦ, s
NFT, w
rA, w
rΦ, w
Thr
ThrDN
ACH
I
I50
I25
I~
I~
50
I~
25
 λCoM
 ϕCoM
 Bs
Bus
 Φs
Φus
RΦ
γB
NFT, s
rA, s
rΦ, s
NFT, w
rA, w
rΦ, w
|     |
|    |
|     |
|         |
|         |
|         |
|         |
|     |
|     |
|    |
Figure 14. Spearman correlation matrix of all the CH properties derived in the statistical
analysis. The values, the square size as well as the color scheme represent the value of the
spearman correlation coeﬃcient which is given in percentual depiction. The black asterisks
mark the signiﬁcance level of the correlation: *** indicates a signiﬁcance level of p ≤0.001, **
indicates p ≤0.01 and * indicates p ≤0.05. The values for all correlation coeﬃcients with a
signiﬁcance level higher than 0.05 were omitted. The parameters are listed in the Appendix.
SOLA: main.tex; 7 October 2019; 0:52; p. 30

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
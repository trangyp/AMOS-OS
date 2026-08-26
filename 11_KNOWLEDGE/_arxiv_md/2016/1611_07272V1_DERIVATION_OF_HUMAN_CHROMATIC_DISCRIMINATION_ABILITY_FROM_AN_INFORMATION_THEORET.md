---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1611.07272v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1611.07272v1_Derivation_of_human_chromatic_discrimination_ability_from_an_information-theoret

> Source: 1611.07272v1_Derivation_of_human_chromatic_discrimination_ability_from_an_information-theoret.pdf

> Pages: 23

---


## Page 1


arXiv:1611.07272v1  [q-bio.NC]  22 Nov 2016
Derivation of human chromatic discrimination ability
from an information-theoretical notion of distance in
color space
Mar´ıa da Fonseca
In´es Samengo
Instituto Balseiro and Centro At´omico Bariloche, (8400) San Carlos de
Bariloche, Argentina.
Abstract
The accuracy with which humans can detect small chromatic differences varies through-
out color space. For example, we are far more precise when discriminating two similar
orange stimuli than two similar green stimuli. In order for two colors to be perceived as
different, the neurons representing chromatic information must respond differently, and the
difference must be larger than the trial-to-trial variability of the response to each separate
color. Photoreceptors constitute the ﬁrst stage in the processing of color information; many
more stages are required before humans can consciously report whether two stimuli are
perceived as chromatically distinguishable or not. Therefore, although photoreceptor ab-
sorption curves are expected to inﬂuence the accuracy of conscious discriminability, there
is no reason to believe that they should sufﬁce to explain it. Here we develop information-
theoretical tools based on the Fisher metric that demonstrate that photoreceptor absorption
properties explain ≈87% of the variance of human color discrimination ability, as tested
by previous behavioral experiments. In the context of this theory, the bottleneck in chro-
matic information processing is determined by photoreceptor absorption characteristics.
Subsequent encoding stages modify only marginally the chromatic discriminability at the
photoreceptor level.
1
Introduction
Perception is the subjective experience that results from the entire brain, not just photoreceptors.
Color discrimination tasks rely on the ability to detect small differences in the activity of higher
brain areas when two stimuli of similar chromatic composition are presented. Human color
discrimination ability has been measured by several authors with behavioral experiments ﬁrst
performed by Wright and Pitt (1934). In these studies, a bipartite ﬁeld was presented to a
1


## Page 2


human subject. One half of the ﬁeld, here called the reference ﬁeld, was illuminated by a
monochromatic beam, constructed by ﬁltering a broad-band light source. The second half, the
test ﬁeld, was also monochromatic, and its wavelength was controlled by the observer. Initially,
the two beams had the same wavelength and luminosity. The observer was instructed to displace
the wavelength of the test ﬁeld, until the ﬁrst noticeable difference in hue was perceived. At
this point, the difference ∆λ between the reference and test wavelengths was calculated. This
difference constitutes the discrimination error, that is, the interval in wavelengths below which
the two colors cannot be perceptually discriminated. The discrimination error was reported to be
a W-shaped function of wavelength, as displayed in Fig.1A (Wright and Pitt 1934; Pokorny and
Smith, 1970). Different curves correspond to different subjects. For all subjects, discrimination
 
 
 
 
 
 
 
 
 
 
 
 
Figure 1: Previous experimental results of human color discrimination ability. A: Discrim-
ination error ∆λ as a function of the wavelength λ of the reference beam, measured in behav-
ioral experiments for 9 different subjects. All subjects exhibit a local maximum at λ ≈550
nm. Subjects are separated in 3 groups, depending on the shape of the curve at λ ≈450 nm.
Top: Subjects exhibiting a local maximum. Middle: Subjects exhibiting a shoulder. Bottom:
Subjects with monotonically decreasing errors. Data from Wright and Pitt (1934) and Pokorny
and Smith (1970). B: MacAdam ellipses (MacAdam 1942) in the CIE 1931 xy chromaticity
diagram, reporting the region in color space that is confounded with the center. As customary,
each ellipse is enlarged 10 times in each dimension for better visualization.
errors were large towards the two borders of the visible spectrum, and at around 550 nm, roughly
at the center of the visible spectrum where luminosity sensitivity is maximal (Sharpe et al.
2005). At short wavelengths, the data show some variability across subjects. We have therefore
separated the 9 curves into 3 groups (displayed in different panels), depending on whether the
discrimination error exhibited an additional maximum at approximately 450 nm (top panel),
only a shoulder (middle panel), or a monotonic behavior (bottom panel).
In 1942, David MacAdam (1942) broadened these discriminability experiments testing the
ability to distinguish any two neighboring points in the entire color space, not just the subset of
light beams composed of a single wavelength. The concept of color, in fact, cannot be restricted
2


## Page 3


to wavelength. Blends of wavelengths produce a new chromatic sensation that emerges exclu-
sively from the mixture, the hue of which differs from the hues of the individual components. In
order to test human chromatic discrimination ability in the entire color space, MacAdam mea-
sured ellipses in the CIE 1931 xy chromaticity diagram, here shown in Fig. 1B. Points in this
space represent hue and saturation, and are independent of the total luminosity. Each ellipse in
the diagram indicates the area in color space (multiplied by 10, for better visualization) inside
which two different stimuli cannot be discriminated.
In this study, we test how much of the results in Fig. 1 can be explained from a given noise
model. The basic assumption is that two colors can be discriminated when the trial-to-trial
variability of their neural representations is smaller than the difference of the corresponding
means. The discriminability d′ of two colors is proportional to the square root of the Fisher
information (Seung and Sompolinsky, 1993). The Fisher information, in turn, introduces a
notion of distance in color space. Hence, our working hypothesis is that two colors become
distinguishable when the Fisher distance between them is larger than a given ﬁxed minimum:
the detection threshold.
Fisher Information has been successfully used as a tool to disclose computational strategies
in the nervous system for decades (see for example Abbot and Dayan 1999, Dayan and Abbot
2001, Brunel and Nadal 1998) and continues to be widely employed (Ganguli and Simoncelli
2014, Wei and Stocker 2015). Within the Fisher framework, two previous studies (Clark and
Skaff 2009; Zhaoping et al. 2011) have derived the discrimination accuracy expected by an ideal
observer that only has access to the number of photons absorbed by the three types of cones.
Both studies were restricted to light beams composed of a single wavelength, and succeeded
in explaining the W-shaped function of Fig. 1A. Our starting point is the work of Zhaoping et
al. (2011). We ﬁrst express the main result of their work in terms of an analytical expression
for the discrimination error. We use the theory to speculate how putative tetrachromat subjects
perceive the chromatic space. In the case of trichromats, we interpret the subject-to-subject
variations in Fig. 1A as resulting from the reported variability in the composition of the human
retina. More importantly, we derive new information-theoretical tools that expand the analysis
to the entire chromatic space, beyond monochromatic light beams. By considering mixtures
of wavelengths, we provide a theoretical framework to also explain Fig. 1B. By focusing our
attention on the curved border of the chromatic space of Fig. 1B, we also recover the previous
result with monochromatic light beams of Fig. 1A.
Our analysis concludes that 87% of the variance of MacAdam’s data can be explained by
properties of photoreceptors alone. Discrimination errors reported in behavioral experiments
are the result of the entire chain of hue-dependent computations intervening in chromatic per-
ception. Therefore, the agreement between experiment and theory implies that the bottleneck
in chromatic information processing seems to be mainly determined by photoreceptor activity.
Subsequent encoding stages either operate optimally or, if they do not, loose information in a
color-independent manner.
3


## Page 4


2
Representations of color space
Color is the subjective sensation that results when a light beam of spectrum I(λ) impinges the
eye. The set of all possible spectra has inﬁnite dimension, since for a continuum of wavelengths
λ the intensity I(λ) can vary arbitrarily. The human visual system, however, is insensitive to
most of these dimensions. Classical behavioral color-matching experiments demonstrated that
for most observers, three monochromatic light sources, conveniently mixed, sufﬁce to repro-
duce all visible colors. Therefore, the human visual system projects the space of all possible
spectra on a 3-dimensional subspace. All spectra sharing the same projection are metamers,
that is, are perceived as indistinguishable. To represent colors as 3-dimensional vectors, here
we use the coordinates (X,Y,Z) deﬁned in the CIE 1931 (Appendix A1). When two color vec-
tors (X1,Y1,Z1) and (X2,Y2,Z2) only differ in their length (they are proportional to one another),
they share the same hue and saturation, and can only be distinguished by their luminosity. In
some applications, it is desirable to discard the luminosity dimension, and only retain the two
remaining features. The CIE 1931 meeting also established a convention to carry out this re-
duction, by transforming the coordinates (X,Y,Z) into a new set of coordinates (x,y,Y) deﬁned
by
x =
X
X+Y+Z,
y =
Y
X+Y+Z, Y = Y.
(1)
The components x and y do not vary if X,Y and Z are all multiplied by the same factor, so x and
y no longer contain the luminosity dimension. The variable Y is associated with the sensation of
brightness, since for monochromatic spectra, the wavelength dependence ofY closely resembles
the apparent luminosity curve (Sharpe et al, 2005). MacAdam’s experiment was reported in CIE
xy chromatic space (Fig. 1).
3
Statistics of the photon shower
For monochromatic light sources of mean intensity I and wavelength λ, the probability P(−→
K |λ)
that −→
K = (KS,KM,KL) photons are absorbed by S,M and L cones is (Appendix A2)
P[−→
K |λ] =
∏
i∈{S,M,L}
Poisson[Ki|Iqi(λ)],
(2)
where Poisson(x|y) represents a Poisson distribution of the random variable x with mean y,
qi(λ) = βihi(λ), the functions hi(λ) are the spectral sensitivities of cones of type i illustrated
in Fig. 2, and the parameters βi are the normalized cross sections associated with each fate of
the photon. If A0 is the retinal area not covered by cones,
βi =
WiAi
A0 +∑j∈{S,M,L}WjAj
for i ∈{S,M,L},
β0 =
A0
A0 +∑j∈{S,M,L}WjAj
(3)
where Wi is the number of photoreceptors of type i, and Ai is the cross section of each cone.
4


## Page 5


400
500
600
700
0,0
0,5
1,0
Absorption
 (nm)
Figure 2: Quantal cone fundamentals for S (blue), M (green) and L (red) cones, and their
analytic approximations. Thin lines: Data from Stockman and Brainard (2009). Thick lines:
ﬁtted equation hi(λ) = exp[−(λ −λi)2/σ2
i ] with λS = 442.1 nm, λM = 542.8 nm, λL = 568.2
nm, σS = 32.96 nm, σM = 52.8 nm, and σL = 64.76 nm.
The light source is now assumed to have an arbitrary spectrum I(λ). Deﬁning the coefﬁ-
cients
αi =
Z
I(λ) qi(λ) dλ,
for i ∈{S,M,L},
(4)
we show in Appendix A2 that
P[−→
K |I(λ)] =
∏
ℓ∈{S,M,L}
Poisson(Ki|αi).
(5)
As expected, Eq. 5 reduces to Eq. 2 when the spectrum I(λ) represents a monochromatic source,
that is, for I(λ) = I δ(λ −λ0).
4
The geometry of color space
In simple discrimination experiments, the perceptual properties of color are contained in the
number of photons absorbed by S, M and L cones. The probability that S, M or L cones absorb
KS, KM and KL photons, respectively, depends on the properties of the impinging light beam.
Here we consider two types of experiments: Monochromatic beams of ﬁxed intensity and vary-
ing wavelength, and light sources composed of arbitrary spectra. In the ﬁrst case the light beam
is characterized by the wavelength λ, and in the second case, by the vector (αS,αM,αL). Dis-
tances in color space—in λ space, or in (αS,αM,αL) space—are deﬁned by the effect on the
number of absorbed photons −→
K caused by changes in the composition of the light source. The
Fisher information J is a metric tensor (Appendix A3) that deﬁnes scalar products and dis-
tances in color space. In the monochromatic case, since λ is a 1-dimensional parameter, the
Fisher tensor reduces to the scalar
J(λ) = −
 ∂2
∂λ 2 lnP
−→
K |λ

P
−→
K |λ
,
(6)
5


## Page 6


where the angular brackets indicate average with respect to the indicated distribution. In the case
of arbitrary mixtures of wavelengths, J is a tensor represented by a 3×3 matrix. In coordinates
−→
α = (αS,αM,αL) its components are
Ji j = −

∂2
∂αi∂αj
lnP
−→
K |−→
α

P
−→
K |−→
α
.
(7)
The Cram´er-Rao bound relates the Fisher tensor to the accuracy with which the random
vector −→
K can be used to estimate the coordinates of color space. Formally, this means that
the mean quadratic error of any unbiased estimator of the wavelength λ or the coordinates
(αS,αM,αL) from the absorbed photons −→
K is bounded from below (Appendix A3).
Metric tensors deﬁne scalar products. In Fig. 3A we see how such products operate in the
Figure 3: Scalar products in the space of parameters. A: The Fisher information metric
tensor deﬁnes scalar products between two vectors −→
α a and −→
α b with common origin at location
−→
α (Eq. 8). B: The set of all vectors at a constant distance from location −→
α deﬁnes an ellipsoid,
whose principal axes are displayed with dashed lines.
parameter space. The scalar product between two vectors −→
α a and −→
α b is
⟨−→
α a,−→
α b⟩= (−→
α a)T J(−→
α ) −→
α b,
(8)
where the supra-script T represents vector transposition. The length of a vector −→
α a originated
at −→
α is then
−→
α a =
q
⟨−→
α a,−→
α a⟩=
q
(−→
α a)T J(−→
α ) −→
α a.
(9)
Equation 9 implies that the set of vectors at a constant distance of a certain −→
α is a conic. Since
the eigenvalues of the Fisher tensor are always non-negative, the conic is an ellipsoid (Fig. 3B).
The directions of the principal axes of the ellipse are the eigenvectors of J(−→
α ), which are also
the eigenvectors of [J(−→
α )]−1. The lengths of those axes are proportional to the inverse of the
square root of the corresponding eigenvalues of J(−→
α ), or equivalently, to the square root of the
eigenvalues of [J(−→
α )]−1. Since J depends on −→
α , the size, excentricity and orientation of the
ellipse may well vary from point to point.
In Fig. 1B, the CIE 1931 xy chromatic space has coordinates (x,y). Each ellipse measured
by MacAdam represents the set of points in color space where the ﬁrst detectable chromatic
difference with the point at the center is perceived. The ellipses represent the points at dis-
tance δ from the center, where δ is the detection threshold. In this paper we aim at evaluating
6


## Page 7


up to which point the ellipses measured by MacAdam can be derived from the properties of
photoreceptors.
We now consider two different coordinate systems −→
α and −→
α ′ to represent colors. Let −→
F be
the vectorial function involved in the mapping between them:
−→
α ′ = −→
F (−→
α ).
(10)
The matrix representation of the Fisher tensor transforms as (Appendix A3)
J(−→
α ) = CT J′(−→
α ′) C,
(11)
with C deﬁned by the Jacobian matrix
C =




∂F1
∂α1
...
∂F1
∂αd
...
...
∂Fd
∂α1
...
∂Fd
∂αd



.
(12)
5
Discrimination of two similar wavelengths
For a monochromatic light beam of ﬁxed intensity I, Eq. 2 establishes a probabilistic mapping
between each wavelength λ and the vector −→
K . The components KS,KM and KL are converted
to electrical signals by photoreceptors, and then processed by the rest of the brain. From the
information-theoretic point of view, the data processing inequality (Amari and Nagaoka, 2000)
ensures that the chromatic information encoded in later processing stages cannot exceed the
amount of chromatic information contained in −→
K . A conscious subject, therefore, cannot have
better discrimination ability than that of an optimal estimator inferring the wavelength λ from
photoreceptor activity, that is, from −→
K . The optimal estimator is usually referred to as the
ideal observer. The Cram´er-Rao bound in this case reduces to its 1-dimensional form (Cram´er,
1946), ∆λ ≥1/
p
J(λ), implying that the minimal error of the ideal observer is the inverse of
the square root of the Fisher information J(λ).
Throughout the paper, spectral sensitivity curves were taken from the cone fundamentals
reported by Stockman and Brainard (2009). In order to work with differentiable functions, the
experimental curves were approximated by functions hi(λ) = exp[−(λ −λi)2/σ2
i ], with ﬁtting
parameters λi and σi, coinciding with the position of the peak and the width of the data. Both
the original and the ﬁtted curves are displayed in Fig. 2 (ﬁtted parameters in the ﬁgure caption).
Using this approximation, we insert Eq. 2 in Eq. 7 and get
J(λ) = I
∑
i∈{S,M,L}
[q′
i(λ)]2
qi(λ)
= 4I
∑
i∈{S,M,L}
(λ −λi)2
σ4
i
e−(λ−λi)2/σ2
i .
(13)
The formal expression of Eq. 13 was derived by Dayan and Abbot (2001), and was ﬁrst applied
to the chromatic context by Zhaoping et al (2011). Here we provide the analytical expression at
7


## Page 8


the right of Eq. 13. Note that the amount of Fisher information is proportional to the intensity
of the light source, in Eq. 13 represented by the mean number of photons I.
In Fig. 4, we display the minimal estimation error ∆λ = 1/
p
J(λ) obtained with Eq. 13, for
Figure 4: Minimal discrimination error ∆λ as a function of the reference wavelength λ,
obtained from Eq. 13. Different curves correspond to different proportions of S (blue), M
(green) and L (red) cones, as indicated in the legends. For all wavelengths, the mean number of
photons was taken as I = 1000.
subjects whose retinas contain different proportions of S, M and L cones. To draw the ﬁgure,
we set the mean number of photons to 1000, in order to match the experimental conditions,
where weak photopic illumination was employed. The shapes of the theoretical curves are
qualitatively similar to the ones measured experimentally (Fig. 1A).
Previous studies have shown that there is substantial subject-to-subject variation in the pro-
portions of different types of cones (Hofer et al. 2005). The variability in cone distribution
sufﬁces to explain the different types of behavioral results. Speciﬁcally, a shoulder appears in
the short-wavelength region only for subjects whose proportion of S cones exceeds 2%, whereas
a full local maximum requires βS ≥5%. The larger the proportion of S-cones, the higher the
peak at ∼450 nm.
The variability in the proportion of S-cones is the crucial factor determining the shape of
∆λ. Humans also display a remarkable variability in the relative proportion of M and L cones
(Roorda and Williams 1999), involved in Eq. 13 through the factors βM and βL. However, as
long as the total amount βM +βL remains constant, relative variations do not modify the shape
of the curve. The cone fundamentals of M and L cones are close to each other, so varying the
relative proportion βM/βL produces a negligible effect in ∆λ.
The theoretical framework developed here can also be used to predict the wavelength depen-
dence of discrimination in observers that are not available for experimentation, either for their
rarity, or for their non-human nature. Figure 5 displays the minimal discrimination errors in
fortunate subjects endowed with 4 different types of cones. In panel A, bird vision is discussed.
Absorption curves are approximately equidistant from each other (Hart et al. 2000) giving rise
to accurate color discrimination abilities that extend further into the ultraviolet spectrum. Four
8


## Page 9


0.0
0.5
1.0
300
400
500
600
700
0
3
6
9
 
 Absorption
 
B
(nm)
 
  
(nm)
(nm)
A
0.0
0.5
1.0
 
400
500
600
700
0
4
8
12
 
Figure 5: Minimal discrimination error ∆λ as a function of wavelength λ, obtained from a
generalization of Eq. 13 that considers 4 different types of cones. A. Top: Absorption curves
of estrilid ﬁnch (Hart et al. 2000) with local maxima at wavelengths λi = 368,445,508,565 nm,
and widths σi = 38.58,38.44,52.87,65.8 nm, respectively. Bottom: Predicted discrimination
error, with mean number of photons set to 1000. Parameters βi are set to 0.25 for all cones. B.
Top: Putative cone fundamentals of a human tetrachromat (Jordan et al. 2010). The additional
curve (in yellow) peaks at λy = 555 nm, and has width σy = 38.51 nm. Bottom: Predicted
discrimination error, with mean number of photons set to 1000. Parameters βi are set to 5%,
31.33%, 31.34% and 31.33% for S,M,Y, and L cones, respectively.
local maxima are visible in ∆λ, accounting for each of the 4 absorption curves.
In panel B, we display the results for a putative human tetrachromat, for which the extra
cone is hypothesized to lie between the M and L cones, as anomalous subject cDa29 studied by
Jordan et al. (2010). In spite of the incorporation of an additional curve, the discrimination abil-
ity of this subject is similar to that of normal trichromats. The substantial overlap between M
and L absorption curves of trichromats implies that the addition of one more absorption curve in
the same wavelength region makes virtually no difference. This does not mean that the putative
tetrachromat of Fig. 5B perceives the same color space as trichromats, since the present dis-
cussion is restricted to the discrimination of neighboring monochromatic beams. Color space
also includes mixtures of wavelengths (see below), and some mixtures, for example the pur-
ples obtained by mixing red and blue, are not metameric with any single monochromatic beam.
Tetrachromats may perceive many more mixtures that cannot be mapped on the trichromat color
space. Our analysis predicts, however, that their ability to discriminate neighboring monochro-
matic beams remains essentially unaltered.
5.1
Discrimination of spectra composed of mixtures of wavelengths
To extend the previous analysis to the entire color space, the Fisher information should be
written as a function of coordinates that describe the chromatic composition of an arbitrary
9


## Page 10


beam I(λ). Equation 5 implies that the probability distribution of the absorbed photons −→
K
is blind to all aspects of the spectrum I(λ) not contained in the vector −→
α deﬁned in Eq. 4.
Replacing Eq. 5 in 7, we get
J (−→
α ) =



1
αS
0
0
0
1
αM
0
0
0
1
αL


.
(14)
The metric tensor is diagonal, so the ellipsoids deﬁning the points at constant distance of a
given parameter −→
α have their principal axes aligned with the coordinate axes. The square root
of the inverse of J (−→
α ) deﬁnes an ellipsoid around each color −→
α where all points are at the same
distance from the central point −→
α (Fig. 6).
Figure 6: Ellipsoids indicating the regions of space −→
α lying at a ﬁxed distance of each
central point.
In order to compare with experimental data, we need to transform the metric tensor of
Eq. 14 from the parameter space −→
α to the CIE 1931 xy chromatic space where MacAdam
reported the minimal discriminable ellipses. We perform the transformation in two steps. First,
we change from (αS,αM,αL) to (X,Y,Z), and then from (X,Y,Z) to the triplet (x,y,Y). So far,
the two transformations are invertible. Once we have the Fisher matrix in the space xyY, we
take the submatrix associated to the components xy alone, in order to compare with MacAdam’s
experiment.
Each of the two transformations involves a C-matrix deﬁned in Eq. 12. If we call C1 the
matrix of the ﬁrst transformation, and C2 the one of the second, the two concatenated transfor-
mations are implemented by a matrix C = C1C2. To calculate C1 we analyze the way the color
matching functions transform, when passing from (αS, αM,αL) to (X,Y,Z). By ﬁtting a linear
transformation between the two, we deduce that


αS
αM
αL

= C1


X
Y
Z

,
with
C1 =


0.038βS
−0.043βS
0.48βS
−0.39βM
1.17βM
0.049βM
0.34βL
0.69βL
−0.076βL

.
To calculate C2, we invert Eq. 1 and ﬁnd
X = Y x/y
Y = Y
Z = Y (1−x−y)/y.
10


## Page 11


Using Eq. 12, we obtain
C2 =







Y
y
−xY
y2
x
y
0
0
1
−Y
y
−Y(1−x)
y2
1−x−y
y







.
With the resulting matrix C = C1C2, we calculate the Fisher tensor in space xyY, and then
focus on the submatrix corresponding to the ﬁrst two components. All the coefﬁcients of the
obtained 2 × 2 submatrix are proportional to the luminosity variable Y. Hence, the lengths of
the principal axes of the ellipses deﬁning the equidistant colors are proportional to Y −1/2, and
the area is proportional to 1/Y. Other than this scaling factor, the luminosity variable has no
additional effect. Since all other variables appearing in the Fisher tensor are adimensional, the
units with which we measure distances in the xy space are [Y]−1/2. Here we use MacAdam’s
unit of color difference (Wyszecki and Stiles 2000), implying that the distance between each
central point and the ellipse measured by MacAdam is unity. In this system, the coordinate Y is
adimensional.
In Fig. 7 the ellipses at distance 1 from 31 center points are displayed. In A, βS is varied
Figure 7: Ellipses obtained by transforming the ellipsoids in Fig. 6. xy CIE chromatic co-
ordinates represented by the horizontal and vertical axes, respectively. A: Dependence of el-
lipses on parameters βS and Y. We set βM = βL = (1 −βS)/2. B: Dependence of ellipses
on retinal composition, for Y = 2 × 105. The triangle represents the accessible area of the
space (βS,βM,βL). Indicated panels correspond to −→
β = (βS,βM,βL) = (0.8,0.1,0.1) (top),
(0.45,0.1,0.45),(0.1,0.1,0.8),(0.1,0.45,0.45),(0.1,0.8,0.1) and (0.45,0.45,0.1) as we rotate
clockwise. As customary, ellipses are enlarged 10 times in each dimension for better visualiza-
tion.
within the physiological range. As βS increases (from left to right) the ellipses become smaller,
11


## Page 12


and more compressed along the direction (1,−1). Increasing the value ofY (from top to bottom)
shrinks the ellipses.
In B, we display the ellipses for several retinal compositions, without restricting the values
of βi to the realistic range. In this context, any set of (βS,βM,βL) deﬁnes a possible retina, as
long as all βi are positive, and the three of them sum up to unity. In the space of possible −→
β
vectors, these conditions deﬁne the triangle illustrated in Fig. 7B. As we move along the bottom
border of the triangle, we conﬁrm that the relative proportion of βM and βL does not change the
ellipses qualitatively (three bottom panels). Increasing βS, instead (moving upward) reduces the
size of the ellipses in the direction (1,1), and augments them along the direction (−1,1). In
other words, increasing the proportion of βS helps discriminating blue vs. yellow stimuli, but
has a detrimental effect on the discrimination of red vs. green. The ellipses corresponding to
the inner area of the triangle smoothly interpolate those at the border.
In order to compare with MacAdam’s experiment, we need to ﬁt the parameters βS and Y,
both kept ﬁxed during the experiment. To do so, we systematically vary βS ∈(0,0.1) and Y ∈
(0,106) and compare the theoretical ellipses evaluated at the 25 points measured by MacAdam
with the 25 experimental ellipses. The optimal parameters are the ones that make both sets of
ellipses maximally similar. To do so, we need a criterion of similarity between ellipses. Two
concentric ellipses may differ in their size, their orientation, or their excentricity. In order to
evaluate the three aspects simultaneously, and to adequately weigh the relevance of each, we
deﬁne the distance between two concentric ellipses as the Kullback-Leibler divergence between
two Gaussian distributions whose covariance matrices are deﬁned by the tested ellipses. As
the two distributions become more and more similar, the two ellipses merge into one another,
implying a simultaneous match between size, elongation and excentricity. Averaging over the
25 measured points, βS and Y are ﬁtted by minimizing
D = 1
25
25
∑
i=1
DKL
h
N (ri,Σth
i )||N (ri,Σe
i )
i
,
where the sum runs over the 25 colors tested by MacAdam, DKL is the Kullback-Leibler diver-
gence, N (ri, Σ) is a normal bivariate distribution centered at the colors ri where MacAdam
performed his experiment, and with covariance matrix Σ. The supra-index th represents the the-
oretical matrix, and e the experimental one. The experimental covariance matrix is constructed
from the reported ellipses: We calculate the matrix whose eigenvectors are in the directions of
the principal axes reported by MacAdam, and whose eigenvalues coincide with the lengths of
the principal axes. The theoretical covariance matrix is the inverse of the Fisher information.
An analytical form for the Kullback-Leibler divergence for multivariate Gaussian distributions
is derived in Duchi (2014). When D is employed as a ﬁtting criterion, the goodness-of-ﬁt may
be deﬁned in terms of an R2-value deﬁned as R2 = 1−D/De, where De is the average Kullback-
Leibler divergence between all experimental ellipses.
In Fig. 8A we see the dependence of D with parameters βS and Y. The optimal values are
βS = 2.1% and Y = 184,000, for which D = 0.36, and R2 = 0.87. In Fig. 8B, we see the model
is effective in describing the variation of the size, orientation and excentricity of the ellipses
throughout the chromatic space. More quantitatively, the obtained R2 value implies that the
theory explains 87% of the variability of the experimental data.
12


## Page 13


Figure 8: Comparison between theory and experiment. A: Distance D between theoretical
and experimental ellipses as a function of parameters βS and Y. The green vertical line indicates
the location of the optimal parameter values βS = 2.1% and Y = 184,000. B: Ellipses measured
by MacAdam (green) compared to the ones derived from our theoretical model (red) for the
optimal parameters. As customary, each ellipse is enlarged 10 times in each dimension for
better visualization.
6
Discussion
Here we derived a metric in color space from a noise model of the representation of color in
the brain. Several classical studies have derived the minimal discrimination ellipses from line
elements (Wyszecki and Stiles, 2000). Those theories used heuristic arguments to propose a
distance in color space. Not being framed in the Fisher geometry, they do not entail a data
processing inequality nor a Cram´er-Rao bound. The advantage of the Fisher metric is that it
brings along a rigorous mathematical framework, ﬁrst, for deriving the metric from a noise
model, and then, for transforming the metric from one space to another. Given the noise model,
the Fisher metric is undisputable. Of course, there are many candidate noise models, depending
on which neuronal processes are described. The confrontation of the derived Fisher ellipses with
experimental data actually provides a systematic way to evaluate the adequacy of alternative
noise models.
Here we offer an attempt to perform such confrontation, using one particular noise model
based on the sole description of the photon absorption process. We conclude that a simple
Poisson model of the statistics of photoreceptor absorption account for ≈87% of the variance
of the behavioral results in the xy chromatic space. Our theory also predicts that the minimal
discrimination error is inversely proportional to the square root of the light intensity, follow-
ing a Rose-DeVries law, originally reported in contrast discrimination thresholds at low light
intensities (Rose 1948, DeVries 1943), and later conﬁrmed for chromatic discrimination exper-
iments (Rovamo et al 2001). Experiments show that this dependence holds in the low-intensity
13


## Page 14


photopic regime, but loses validity as the light intensity becomes larger (Rovamo et al 2001).
Therefore, additional optic or neural color-dependent processing stages not contained in the
Poisson photoreceptor model must come into play at high intensities.
In spite of having neglected all subsequent color processing stages beyond absorption, even
the voltage variations in the inner segments of photoreceptors, the distances derived from the
Fisher approach reproduce a large fraction of the experimental variability. The derived ellipses
are only guaranteed to coincide with the measured discrimination error when the Cram´er-Rao
bound is tight, that is, when further processing stages perform optimally, or at least, they do not
introduce additional color-dependent distortions. A priori, there is no reason to believe that such
should be the case. The similarity between the theoretical and the experimental results therefore
suggests that photon absorption constitutes the crucial stage in the chromatic dependence of
color processing ability, and it sufﬁces to explain most of the structure observed in experimental
data. All subsequent processing stages either perform optimally or, if they lose information,
they do so in a color-independent manner.
The Cram´er-Rao bound of Eq. 26 is only valid for unbiased estimators, a more complex
formula is required in the biased case (Cover and Thomas, 1991). However, in the presence of
achromatic backgrounds (as in all experiments explored here), discrimination errors have been
always reported to have zero mean, so we work under the assumption that the nervous system
is able to implement at least one unbiased estimator, for which Eq. 26 holds. Different is the
case where the target and test stimuli are presented against a chromatic background, where
subjects have been reported to bias their estimation of the target stimulus away from the hue of
the background (see for example Klaue and Wachtler 2015). In such cases, we suspect that the
more complex form of the Cram´er-Rao bound should be employed.
The Fisher tensor determines the distance between neighboring colors; the distance between
distant colors must be calculated by adding the inﬁnitesimal distances encountered along a
speciﬁc path. If one of the two colors lies at a border of the chromatic space, the path must
be entirely contained inside the space. When the path connecting two colors is short, all the
involved inﬁnitesimal distances are obtained from essentially the same Fisher tensor, since the
Fisher metric varies smoothly with location. When comparing the theoretical and experimental
ellipses, we have assumed that the Fisher distance between the central color and the ellipse
could be calculated with a single Fisher tensor: the one of the center. To assess the validity of
the approximation, we veriﬁed that inside each ellipse the eigenvalues of the theoretical Fisher
tensor vary at most 1.27 %, and the inclination angle at most 0.97◦(recall that all depicted
ellipses have been enlarged 10 times in each dimension, for better visibility).
We are aware of two other previous studies where chromatic discrimination ability was
modeled by information-theoretical methods. The ﬁrst one (Clark and Skaff, 2009) was based
on stronger assumptions as the ones used here, since the properties of chromatic perception were
explained in terms of a speciﬁc decoding process that takes place (explicitly or implicitly) in the
visual system. Our work neither supports nor refutes the proposed decoding, we simply show
that it is not strictly required to explain a large fraction of the variance in human discrimination
ability. The second study was developed by Zhaoping et al. (2011). Their approach was the
starting point for the present study. They also discussed how the Fisher metric varies with
14


## Page 15


mean light intensity. Instead here, we have focused on (a) providing an analytical formula
for the monochromatic case, (b) extending the analysis to the whole chromatic space, and (c)
discussing the discrimination ability of observers endowed with different retinal compositions.
Chromatic discrimination ability is limited by the imprecision with which neighboring col-
ors are represented in the brain. The stochasticity considered here regards the unpredictability
of the exact proportion of photons captured by S, M and L cones, given that the three absorption
curves overlap with each other. The variance of Ki is Kqi(1 −qi), and is maximal when both
qi and 1 −qi are far from zero. For M and L cones, this condition is met at approximately
550 nm, where both absorption probabilities are high. Human color discrimination error has a
local maximum at ≈550 nm, roughly coinciding with the wavelength where humans perceive
maximal luminosity (Sharpe et al. 2005). So far, this coincidence appeared as incidental. An
analysis of the equations involved in our study, however, reveals that color discrimination abil-
ity is determined by the derivative of the quantal cone fundamentals: The larger the derivative,
the larger the value of the Fisher information (Dayan and Abbott, 2001). Since L and M cone
fundamentals are very similar, and given that the variance is particularly large at ≈550 nm,
the two maxima cannot be separated apart, and discrimination error peaks at a wavelength that
is approximately the average of the wavelengths where L and M absorption curves reach their
maxima. The coincidence, hence, is grounded on the mathematical properties of the Fisher
information. If the number of S cones is large enough, a local maximum in discrimination er-
ror is also achieved at the wavelength where the S-cone absorption curve peaks, ≈450 nm.
Moreover, the theory also predicts how discrimination ability varies with retinal composition,
suggesting that the variability in anatomical properties of different observers may account for
the variability in the experimental data.
Throughout our work, we have only considered cones, although rod absorption is also mod-
ulated by wavelength. By a simple extension of our analysis, it is also possible to include rods in
the evaluation of chromatic discrimination ability. However, since rods and cones have different
luminosity sensitivity, the comparison with behavioral data should be performed with experi-
ments where the total light intensity was controlled. The parameters βi scaling the relevance
of each photoreceptor should also include a factor accounting for the different cross sections of
rods and cones, and their differential sensitivity depending on the total luminosity. The analysis
presented here is only valid for photopic illumination conditions (as reported by the experi-
ments) where rods are assumed to be saturated. Extensions to other models, including rods or
other optical and neural processes, are possible. Results can be expressed in the classical color
spaces employed here, through the transformation formulas of Sect. 4.
15


## Page 16


Appendix
A1: Transformations of the light spectrum leading to representations of
color
From the physical point of view, the spectrum I(λ) provides a complete characterization of
a light beam. The space of all possible spectra has inﬁnite dimensions. Color matching ex-
periments performed by Helmholtz and Young proved that by adjusting the intensity of three
monochromatic sources of ﬁxed wavelengths, human trichromats construct a beam that they
perceive as visually indistinguishable from a target light source of arbitrary spectrum. Hence,
the human visual system projects the high-dimensional space of all possible spectra onto three
dimensions (Fig. 9). When the target light source is monochromatic and has wavelength λ, the
Figure 9: Transformations between different representations of the composition of a light
beam. Top: The most complete representation is the spectrum I(λ), specifying the energy
density in each wavelength. The space of all possible spectra has inﬁnite dimensions. Middle:
The human visual system can only perceive 3 dimensions. The projection from the space of
spectra to the space of chromatic perceptions is linear (Grassmann’s law). There are many
representations of the 3-dimensional space perceived by humans. One of them is the CIE 1931
XYZ color space (middle bottom). Each spectrum at the top projects to a single point in the
three-dimensional space by means of a non-invertible transformation. Bottom: The CIE 1931
xy chromatic space is a nonlinear transformation of the CIE 1931 XYZ space that eliminates
the luminosity dimension, and only keeps variations in hue and saturation. Each point of the
three-dimensional space maps onto a point in the xy space.
three intensities required to construct the mixture deﬁne the color matching functions ¯b(λ), ¯g(λ)
and ¯r(λ), whose functional shape depends on the wavelengths of the three sources than com-
prise the mixture. The matching operation is linear, implying that the visual appearance of an
arbitrary spectrum I(λ) is governed by three numbers, deﬁned as
B =
R I(λ)¯b(λ) dλ,
G =
R I(λ) ¯g(λ) dλ,
R =
R I(λ)¯r(λ) dλ.
(15)
16


## Page 17


If the wavelengths of the three ﬁxed light sources are varied, the shape of the color match-
ing functions changes. Different (R,G,B) representations have thus appeared, depending on
the chosen wavelengths. In fact, any invertible linear transformation of one set of coordinates
(R,G,B) yields a new set of coordinates (R′,G′,B′) equally valid, represented in Fig. 9 as one
of the coordinate systems in the middle column. The new coordinates can also be obtained from
integrals like Eq. 15, but with new functions ¯b′(λ), ¯g′(λ), ¯r′(λ), derived from a linear transfor-
mation of the old functions. In 1931, the International Commission on Illumination (CIE, for
its initial in French) selected a particular set of coordinates (X,Y,Z), associated with speciﬁc
color matching functions usually notated as ¯x(λ), ¯y(λ), ¯z(λ) (Wyszecki and Stiles, 2000).
A2: Poisson absorption models
In this appendix, we derive Eqs. 2 and 5. Repeated use is made of the formulas
Binomial : (a+b)n =
n
∑
j=0
n!
j!(n−j)! aj bn−j;
Multinomial :
 
k
∑
i=1
ai
!n
= n! ∑
j1,..., jk
k
∏
ℓ=1
ajℓ
ℓ
jℓ!,
where the sum of the multinomial theorem runs over all sets of integers { j1,..., jk} fulﬁlling
the conditions 0 ≤jℓ≤n and n = j1 +...+ jk.
Monochromatic light source of ﬁxed intensity
When a photon of wavelength λ impinges on the retina under central photopic illumination
conditions, four outcomes are possible: The photon may be detected by a cone of type S, M
or L, or it may pass undetected. The probability of each outcome depends on the fraction of
S, M and L cones that tile the retina and on the probability that each cone absorbs a photon
of wavelength λ, also called the spectral sensitivity of each cone. Once these parameters are
known, from the statistical point of view, illuminating the retina with I0 photons of wavelength
λ is equivalent to randomly distributing I0 balls into 4 boxes whose cross sections depend on
the wavelength λ. The probability that NS,NM and NL fall on S,M and L-cones respectively,
and that N0 do not fall on cones is
P(−→
N |I0) = I0!
∏
i∈{S,M,L,0}
β Ni
i
Ni! ,
(16)
where −→
N = (NS,NM,NL). The components NS,NM,NL,N0 are not all independent, since they
must sum up to I0. Therefore, N0 is a shorthand notation for N0 = I0 −NS −NM −NL.
When Ni photons reach a cone of type i, the probability that Ki of them are absorbed is a
binomial distribution with absorption probability hi(λ) (Fig.2),
P(Ki|Ni) =
Ni!
Ki!(Ni −Ki)! hi(λ)Ki [1−hi(λ)]Ni−Ki,
for i ∈{S,M,L}.
(17)
17


## Page 18


When these two processes are coupled sequentially, the fate of each photon is decided through
the processes depicted in Fig. 10. The probability that KS,KM,KL photons are absorbed by
Figure 10: I0 photons of wavelength λ fall on S, M or L cones (colored boxes), or miss cones
altogether (black box). Each of the Ni photons that fall on cones of type i may either be absorbed
(and become one of the Ki photons absorbed by a photoreceptor of type i), or pass unabsorbed
(and become one of the ∆i photons not absorbed by a cone of type i). The total number of
photons absorbed by a cone of type i is Ki = Ni −∆i, and the number of photons that remain
unabsorbed is K0 = N0 +∆S +∆M +∆L. The process that transforms the K impinging photons
into (NS,NM,NL,N0) is governed by the multinomial distribution of Eq. 16, and the one that
transforms Ni into Ki, by the binomial of Eq. 17.
cones S,M,L and that K0 pass undetected is
P(−→
K |I0,λ) = ∑
N>K
P(−→
N |I0,λ)
∏
i∈{S,M,L}
P(Ki|Ni),
(18)
where the sum ranges over all vectors −→
N = (NS,NM,NL) that fulﬁll the conditions NS ≥KS,NM ≥
KM,NL ≥KL and NS +NM +NL ≤I0. Replacing Eqs. 16 and 17 in Eq. 18, deﬁning the scaled
absorption probabilities qi(λ) = βihi(λ), for i ∈{S,M,L}, and q0(λ) = 1 −qS(λ) −qM(λ) −
qL(λ) and the the numbers ∆S,∆M and ∆L of lost photons (see Fig. 10)
∆S = NS −KS,
∆M = NM −KM,
∆L = NL −KL,
we get, after some algebraic manipulations,
P(−→
K |I0,λ) = I0!
∏
i∈{S,M,L,0}
qi(λ)Ki
Ki!
.
(19)
The derivation involved the use of the binomial theorem three times. The composition of the
multinomial process of Eq. 16 and the binomial of Eq. 17 yields another multinomial distribu-
tion governed by the scaled absorption probabilities, combining the parameters governing the
two processes in play. In Eq. 19, the variables KS,KM and KL are not independent, since the
distribution also includes a factor that depends on K0 = I0 −KS −KM −KL.
18


## Page 19


Monochromatic light source of variable intensity
If the total number of photons I0 of wavelength λ is a stochastic variable governed by a Poisson
distribution of mean I
P[I0|I] = e−I II0
I0!,
(20)
then the probability of the absorbed photons is
P[−→
K |λ,I] =
+∞
∑
I0=0
P(−→
K |I0,λ) P[I0|I].
(21)
Replacing Eq. 19 and 20 in Eq. 21, and after some algebraic manipulations, we arrive at Eq. 2.
A light source with variable intensity, hence, gives rise to absorbed photon counts KS,KM,KL
that are independent from one another.
Light sources of arbitrary spectrum
We now consider a light source composed of photons of r different wavelengths λ j, where j
ranges between 1 and r. The mean number of photons of the different wavelengths deﬁnes an r-
dimensional vector −→I = (I(λ1),...,I(λr)). There are many ways in which S cones can absorb
KS photons: All the KS photons may have the same wavelength λ1, half of them may have
wavelength λ1 and the other half wavelength λ2, etc. Here we consider all the possibilities. We
deﬁne Gj
S as the number of photons of wavelength λ j absorbed by cones S, and arrange these
numbers in r-dimensional vectors
GS = (G1
S,...,Gr
S),
GM = (G1
M,...,Gr
M),
GL = (G1
L,...,Gr
L).
If the total numbers of absorbed photons are KS,KM and KL, the components of the three vectors
deﬁned above must sum up to these values, that is,
∑r
j=1 Gj
S = KS,
∑r
j=1 Gj
M = KM,
∑r
j=1Gj
L = KL.
(22)
We call US, UM and UL the sets of all vectors GS, GM and GL whose components are non-
negative integers fulﬁlling Eqs. 22. Mathematically, for i ∈{S,M,L},
Ui = {Gi/Gj
i ≥0 ∀j &
r
∑
j=1
Gj
i = Ki},
The probability of cones S,M and L of absorbing −→
K photons can be written in terms of the sum
of all possible spectral compositions of the absorbed photons, namely,
P(−→
K |⃗I ) = ∑
GS∈US ∑
GM∈UM ∑
GL∈UL
r
∏
j=1
P[Gj
S,Gj
M,Gj
L|I(λ j)],
(23)
where the probability P[Gj
S,Gj
M,Gj
L|I(λ j)] in the right-hand side of Eq. 23 is the same as the
one of Eq. 2, but is now evaluated in a G-vector (as opposed to a K-vector). The sums represent
the fact that many combination of wavelengths may contribute to the same −→
K .
19


## Page 20


Replacing Eq. 2 in Eq. 23, and using the multinomial theorem, we get
P(−→
K |⃗I) =
∏
ℓ∈{S,M,L}
exp[−∑r
i=1I(λi)qℓ(λi)]
Kℓ!
"
r
∑
j=1
I(λ j)qℓ(λ j)
#Kℓ
.
(24)
Deﬁning the coordinates (αS,αM,αL)
αi =
r
∑
j=1
I(λ j)qi(λ j),
for i ∈{S,M,L},
(25)
Eq. 24 yields Eq. 5. If the spectrum contains a continuum of wavelengths λ with mean spectral
energy I(λ), the calculations performed here remain unchanged, except for the fact that the
coefﬁcients αi must be deﬁned in terms of integrals (compare Eq. 4 and 25).
A3: The Fisher geometry
Here, the properties of the light beam that are relevant to color discrimination are represented by
a vector of parameters −→
α = (α1,...,αd). In this appendix, the parameter −→
α is not necessarily
deﬁned by Eqs. 4. For example, when applied to experiments performed with monochromatic
beams, we can take d = 1, and −→
α equal to the wavelength λ (or equivalently, any invertible
function of the wavelength). In the case of mixtures, we may take d = 3, and −→
α deﬁned by
Eqs. 4, or equivalently, as −→
α = (X,Y,Z). We may also consider d = 2 and −→
α = (x,y).
If the probability distribution of a random variable −→
K depends on the parameter −→
α , a notion
of distance can be deﬁned in the −→
α space, quantifying the effect of changing −→
α on P(−→
K |−→
α ).
It may well be the case that in certain regions of the −→
α space, a displacement of the parameter
in a certain amount d−→
α changes the distribution P(−→
K |−→
α ) radically, whereas in other regions
the same displacement hardly has an effect. In these circumstances, distances in the −→
α space
vary from point to point: The same displacement d−→
α corresponds to a large distance in the
ﬁrst case, and to small one in the second. The Fisher information introduced in Eq. 7 deﬁnes
a metric tensor that gives rise to a notion of distance in parameter space: the length of a vector
is given by Eq. 9, and the distance between two neighboring vectors −→
α a and −→
α b is the length
of −→
α a −−→
α b. The Cram´er-Rao bound relates the Fisher tensor to the accuracy with which the
random variable −→
K can be used to estimate the parameter −→
α . If the Fisher information is large,
sampling −→
K can provide a good estimate of −→
α , if an efﬁcient decoding procedure is used. A
low Fisher information, in contrast, implies that P(−→
K |−→
α ) hardly varies with −→
α and therefore,
it is impossible to make (on average) a good guess of the value of −→
α by sampling −→
K , not even
with an optimal decoding procedure. Formally, this means that the mean quadratic error of any
unbiased estimator ˆ−→
α (−→
K ) of the parameter −→
α is bounded from below. We deﬁne the mean
quadratic error as a d ×d matrix E, with elements
Ei j(−→
α ) =
Dh
ˆαi(−→
K )−αi
i ˆαj(x)−αj
E
P
−→
K |−→
α
 .
The Cram´er-Rao bound states that
E(−→
α )·J(−→
α ) ≥
1,
(26)
20


## Page 21


where
1 is the identity matrix, and the inequality implies that all the eigenvalues of the matrix
E · J cannot be smaller than unity. The Cram´er-Rao bound of Eq. 26 can also be expressed
as E ≥J−1. Therefore, J−1 is the minimal mean quadratic estimation error. The larger the
information, the smaller the error, and vice versa. The bound expressed in Eq. 26 is only valid
for unbiased estimators, a more complex formula is required in the biased case (Cover and
Thomas, 1991).
In Sect. 2, several representations of the composition of a light beam were introduced. One
may, for example, represent the light beam with the spectrum I(λ), or with speciﬁc coordinates
RGB, or with the CIE 1931 XYZ, or the reduced xy. Assume that new coordinates −→
α ′ are deﬁned
from old coordinates −→
α by means of a transformation −→
F (see Eq. 10). If the elements of the
Fisher information matrix for the representation −→
α are known, one may calculate their value in
the representation −→
α′. The transformation must be such as to preserve scalar products. If −→
α a
and −→
α b are two inﬁnitesimal displacements from the vector −→
α , the transformed inﬁnitesimal
displacements −→
α ′a and −→
α ′b are deﬁned from the ﬁrst order expansion of −→
F ,
−→
F (−→
α +−→
α a)
≈
−→
F (−→
α )+
h
(−→
α a)T−→
∇
i−→
F (−→
α ) ≡−→
α ′ +−→
α ′a
−→
F (−→
α +−→
α b)
≈
−→
F (−→
α )+
h
(−→
α b)T−→
∇
i−→
F (−→
α ) ≡−→
α ′ +−→
α ′b
Therefore, −→
α ′i =
h
(−→
α i)T−→
∇
i−→
F (−→
α ), for i ∈{a,b}. Preserving the scalar product means that
(−→
α a)T J(−→
α ) −→
α b = (−→
α ′a)T J′(−→
α ′) −→
α ′b.
Since the displacements −→
α a and −→
α b are arbitrary, we arrive at Eqs. 11 and 12. In general, the
matrix C depends on the parameter −→
α . Only if −→
F is a linear transformation, C reduces to a
constant matrix.
Acknowledgements
We thank Rodrigo Echeveste for very productive discussions.
References
- Abbot, L. F., & Dayan, P. (1999). The effect of correlated variability on the accuracy of a
population code. Neural Computation 11, 91-101.
- Amari, S.-I., & Nagaoka, H. (2000). Methods in information Geometry. Providence RI:
American Mathematical Society.
- Brunel N., & Nadal J. P. (1998). Mutual information, Fisher information and population
coding. Neural Computation 10(7), 1731-1757.
21


## Page 22


- Clark, J.J., & Skaff, S. (2009). A spectral theory of color perception. Journal of the
Optical Society of America 26(12), 2488-2502.
- Cover, T.M., & Thomas J. A. (1991). Elements of Information Theory. New York: Wiley.
- Cram´er, H. (1946). A contribution to the theory of statistical estimation, Scandinavian
Actuarial Journal 1946(1), 458-463.
- Dayan, P., & Abbot, L. F. (2001). Theoretical Neuroscience. Computational and Mathe-
matical Modeling of Neural Systems. Cambridge: MIT Press.
- DeVries, H. L. (1943). The quantum character of light and its bearing upon threshold of
vision, the differential sensitivity and the visual acuity of the eye. Physica 10: 553-564.
- Duchi, J. C. (2014). Derivations for Linear Algebra and Optimization. Resource docu-
ment. http://ai. stanford.edu/˜jduchi/projects/general notes.pdf. Accessed Jan 2016.
- Ganguli, D. & Simoncelli, E. P., (2014). Efﬁcient Sensory Encoding and Bayesian Infer-
ence with Heterogeneous Neural Populations. Neural Computation 26(19), 2103-2134.
- Hart, N. S., Partridge, J. C., Bennet, A. T. D., & Cuthill, I.C. (2000). Visual pigments,
cone oil droplets and ocular media in four species of estrildid ﬁnch. Journal of Compara-
tive Physiology A 186, 681-694.
- Hofer, H., Carroll, J., Neitz, J., Neitz, M., & Williams, D. R. (2005). Organization of the
Human Trichromatic Cone Mosaic. Journal of Neuroscience, 25(42), 9669-9679.
- Jordan, G., Deeb, S. S., Bosten, J. M., & Mollon, J. D. (2010). The dimensionality of
color vision in carriers of anomalous trichromacy. Journal of Vision 8(10), 1-19.
- Klaue, S., & Wachtler. T. (2015). Tilt in color space: Hue changes induced by chromatic
surrounds. Journal of Vision 15(13): 17, 111.
- MacAdam, D. L. (1942). Visual Sensitivities to Color Differences in Daylight. Journal
of the Optical Society of America 32(5), 247-274.
- Pokorny, J., & Smith, V. C. (1970). Wavelength discrimination in the presence of added
chromatic ﬁelds. Journal of the Optical Society of America 60(4), 562-569.
- Roorda, A., & Williams, D. R. (1999). The arrangement of the three cone classes in the
living human eye. Nature 397, 520-522.
- Rose, A. (1948) The sensitivity performance of the human eye on an absolute scale.
Journal of the Optical Society of America 28:196-208.
- Rovamo, J. M., Kankaanp¨a¨a, M. I., & Hallikainen, J. (2001) Spatial neural modulation
transfer function for human foveal visual system for equiluminous chromatic gratings.
Vision Research 41:1659-1667.
- Sharpe, L. T., Stockman, A., Jagla, W., & J¨agle, H. (2005). A luminous efﬁciency func-
tion V ∗(λ) for daylight adaptation. Journal of Vision 5, 948-968.
22


## Page 23


- Seung, H. S., & Sompolinsky, H. (1993). Simple models for reading neuronal population
codes. PNAS USA 90: 10749-10753.
- Stockman, A., & Brainard, D. H. (2009). Color vision mechanisms, in Bass, M. (ed.)
OSA Handbook of Optics, New York: McGraw-Hill.
- von Helmholtz, H. (1896). Handbuch der physiologischen Optik. Leipzig: Voss.
- Wei, X. X., & Stocker, A. A. (2015). A Bayesian observer model constrained by efﬁcient
coding can explain ’anti-Bayesian’ percepts. Nature Neuroscience 18, 1509-1517.
- Wright, W. D., & Pitt, F. H. G. (1934). Hue discrimination in normal colour vision.
Proceedings of the Physical Society 46, 459-473.
- Wyszecki, G., & Stiles, W. S. (2000). Color Science: Concepts and Methods, Quantitative
Data and Formulae. New York: Wiley Interscience.
- Zhaoping, L., Geisler, W. S., & May, K. A. (2011). Human Wavelength Discrimination of
Monochromatic Light Explained by Optimal Wavelength Decoding of Light of Unknown
Intensity. PLoS ONE 6(5), e19248. doi:10.1371/journal.pone. 0019248.
23

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1611_07272v1_derivation_of_human_chromatic_discrimination_ability_from_an_information_theoret
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2016/1611_07272V1_DERIVATION_OF_HUMAN_CHROMATIC_DISCRIMINATION_ABILITY_FROM_AN_INFORMATION_THEORET.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

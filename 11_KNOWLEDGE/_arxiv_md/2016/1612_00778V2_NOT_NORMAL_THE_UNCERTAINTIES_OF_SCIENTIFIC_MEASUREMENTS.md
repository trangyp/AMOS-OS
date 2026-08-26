---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1612.00778v2
source: arxiv
tags: [arxiv, knowledge, math, quantum, reference]
---
# 1612.00778v2_Not_Normal__the_uncertainties_of_scientific_measurements

> Source: 1612.00778v2_Not_Normal__the_uncertainties_of_scientific_measurements.pdf

> Pages: 17

---


## Page 1


Not Normal: the uncertainties of scientiﬁc measurements
David C. Bailey∗
Physics Department, University of Toronto, Toronto, ON, Canada M5S 1A7
(Dated: November 6, 2018)
Judging the signiﬁcance and reproducibility of quantitative research requires a good un-
derstanding of relevant uncertainties, but it is often unclear how well these have been eval-
uated and what they imply.
Reported scientiﬁc uncertainties were studied by analysing
41000 measurements of 3200 quantities from medicine, nuclear and particle physics, and
interlaboratory comparisons ranging from chemistry to toxicology. Outliers are common,
with 5σ disagreements up to ﬁve orders of magnitude more frequent than naively expected.
Uncertainty-normalized diﬀerences between multiple measurements of the same quantity are
consistent with heavy-tailed Student-t distributions that are often almost Cauchy, far from
a Gaussian Normal bell curve. Medical research uncertainties are generally as well evaluated
as those in physics, but physics uncertainty improves more rapidly, making feasible simple
signiﬁcance criteria such as the 5σ discovery convention in particle physics. Contributions to
measurement uncertainty from mistakes and unknown problems are not completely unpre-
dictable. Such errors appear to have power-law distributions consistent with how designed
complex systems fail, and how unknown systematic errors are constrained by researchers.
This better understanding may help improve analysis and meta-analysis of data, and help
scientists and the public have more realistic expectations of what scientiﬁc results imply.
I.
INTRODUCTION
What do reported uncertainties actually tell us about
the accuracy of scientiﬁc measurements and the likeli-
hood that diﬀerent measurements will disagree? No sci-
entist expects diﬀerent research studies to always agree,
but the frequent failure of published research to be con-
ﬁrmed has generated much concern about scientiﬁc re-
producibility [1, 2].
When scientists investigate many quantities in very
large amounts of data, interesting but ultimately false
results may occur by chance and are often published. In
particle physics, bitter experience with frequent failures
to conﬁrm such results eventually led to an ad hoc “5-
sigma” discovery criterion [3–6], i.e. a “discovery” is only
taken seriously if the estimated probability for observing
the result without new physics is less than the chance of
a single sample from a Normal distribution being more
than ﬁve standard deviations (“5σ”) from the mean.
In other ﬁelds, arguments that most novel discover-
ies are false [7] have caused increased emphasis on re-
porting the value and uncertainty of measured quanti-
ties, not just whether the value is statistically diﬀerent
from zero [8, 9]. Research conﬁrmation is then judged by
how well independent studies agree according to their re-
ported uncertainties, so assessing reproducibility requires
accurate evaluation and realistic understanding of these
uncertainties. This understanding is also required when
analysing data, combining studies in meta-analyses, or
making scientiﬁc, business, or policy judgments based
on research.
The experience of research ﬁelds such as
∗dbailey@physics.utoronto.ca
physics, where values and uncertainties have long been
regularly reported, may provide some guidance on what
reproducibility can reasonably be expected [10].
Most recent investigations into reproducibility focus
on how often observed eﬀects disappear in subsequent
research, revealing strong selection bias in published re-
sults. Removing such bias is extremely important, but
may not reduce the absolute number of false discoveries
since not publishing non-signiﬁcant results does not make
the “discoveries” go away. Controlling the rate of false
discoveries depends on establishing criteria that reﬂect
real measurement uncertainties, especially the likelihood
of extreme ﬂuctuations and outliers [11].
Outliers are observations that disagree by an abnor-
mal amount with other measurements of the same quan-
tity. Despite every scientist knowing that the rate of out-
liers is always greater than naively expected, there is no
widely accepted heuristic for estimating the size or shape
of these long tails. These estimates are often assumed to
be approximately Normal (Gaussian), but it is easy to
ﬁnd examples where this is clearly untrue [12–14].
To examine the accuracy of reported uncertainties, this
paper reviews multiple published measurements of many
diﬀerent quantities, looking at the diﬀerences between
measurements of each quantity normalized by their re-
ported uncertainties. Previous similar studies [15–20] re-
ported on only a few hundred to a few thousand measure-
ments, mostly in subatomic physics. This study reports
on how well multiple measurements of the same quantity
agree, and hence what are reasonable expectations for the
reproducibility of published scientiﬁc measurements. Of
particular interest is the frequency of large disagreements
which usually reﬂect unexpected systematic eﬀects.
arXiv:1612.00778v2  [stat.AP]  19 Jan 2017


## Page 2


2
A.
Systematic eﬀects
Sources of uncertainty are often categorized as statis-
tical or systematic, and their methods of evaluation clas-
siﬁed as Type A or B [21]. Type A evaluations are based
on observed frequency distributions; Type B evaluations
use other methods. Statistical uncertainties are always
evaluated from primary data using Type A methods, and
can in principle be made arbitrarily small by repeated
measurement or large enough sample size.
Uncertainties due to systematic eﬀects may be evalu-
ated by either Type A or B methods, and fall into sev-
eral overlapping classes [22]. Class 1 systematics, which
include many calibration and background uncertainties,
are evaluated by Type A methods using ancillary data.
Class 2 systematics are almost everything else that might
bias a measurement, and are caused by a lack of knowl-
edge or uncertainty in the measurement model, such as
the reading error of an instrument or the uncertainties
in Monte Carlo estimates of corrections to the measure-
ment. Class 3 systematics are theoretical uncertainties
in the interpretation of a measurement.
For example,
determining the proton radius using the Lamb shift of
muonic hydrogen requires over 20 theoretical corrections
[23] that are potential sources of uncertainty in the pro-
ton radius, even if the actual measurement of the Lamb
shift is perfect. The uncertainties associated with Class 2
and 3 systematic eﬀects cannot be made arbitrarily small
by simply getting more data.
When considering the likelihood of extreme ﬂuctu-
ations in measurements, mistakes and “unknown un-
knowns” are particularly important, but they are usually
assumed to be statistically intractable and are not often
considered in traditional uncertainty analysis. Mistakes
are “unknown knowns”, i.e. something that is thought
to be known but is not, and it is believed that good sci-
entists should not make mistakes.
“Unknown unknowns” are factors that aﬀect a mea-
surement but are unknown and unanticipated based on
past experience and knowledge [24]. For example, during
the ﬁrst 5 years of operation of LEP (the Large Electron
Positron collider), the eﬀect of local railway traﬃc on
measurements of the Z0 boson mass was an “unknown
unknown” that no-one thought about. Then improved
monitoring revealed unexpected variations in the accel-
erator magnetic ﬁeld, and after much investigation these
variations were found to be caused by electric rail line
ground leakage currents ﬂowing through the LEP vac-
uum pipe [25].
In general,
systematic eﬀects are challenging
to
estimate [12, 21, 22, 26–29], but can be partially con-
strained by researchers making multiple internal and ex-
ternal consistency checks: Is the result compatible with
previous data or theoretical expectations? Is the same
result obtained for diﬀerent times, places, assumptions,
instruments, or subgroups? As described by Dorsey [30],
scientists “change every condition that seems by any
chance likely to aﬀect the result, and some that do not,
in every case pushing the change well beyond any that
seems at all likely”. If an inconsistency is observed and
its cause understood, the problem can often be ﬁxed and
new data taken, or the eﬀect monitored and corrections
made. If the cause cannot be identiﬁed, however, then
the observed dispersion of values must be included in the
uncertainty.
The existence of unknown systematic eﬀects or mis-
takes may be revealed by consistency checks [31], but
small unknown systematics and mistakes are unlikely to
be noticed if they do not aﬀect the measurement by more
than the expected uncertainty. Even large problems can
be missed by chance (see Sec. IV D) or if the conditions
changed between consistency checks do not alter the size
of the systematic eﬀect. The power of consistency checks
is limited by the impossibility of completely changing
all apparatus, methods, theory, and researchers between
measurements, so one can never be certain that all sig-
niﬁcant systematic eﬀects have been identiﬁed.
II.
METHODS
A.
Data
Quantities were only included in this study if they are
signiﬁcant enough to have warranted at least ﬁve inde-
pendent measurements with clearly stated uncertainties.
Medical and health research data were extracted
from some of the many meta-analyses published by the
Cochrane collaboration [32]; a total of 5580 measure-
ments of 310 quantities generating 99433 comparison
pairs were included. Particle physics data (8469 measure-
ments, 864 quantities, 53988 pairs) were retrieved from
the Review of Particle Physics [33, 34]. Nuclear physics
data (12380 measurements, 1437 quantities, 66677 pairs)
were obtained from the Table of Radionuclides [35].
Most nuclear and particle physics measurements have
prior experimental or theoretical expectations which may
inﬂuence results from nominally independent experi-
ments [20, 36], and medical research has similar biases
[7], so this study also includes a large sample of inter-
laboratory studies that do not have precise prior expec-
tations for their results.
In these studies, multiple in-
dependent laboratories measure the same quantity and
compare results. For example, the same mass standard
might be measured by national laboratories in diﬀerent
countries, or an unknown archaeological sample might
be divided and distributed to many labs, with each lab
reporting back its Carbon-14 measurement of the sam-
ple’s age. None of the laboratories knows the expected
value for the quantity nor the results from other labs,
so there should be no expectation, selection, or publi-
cation biases.
These Interlab studies (14097 measure-
ments, 617 quantities, 965416 pairs) were selected from
a wide range of sources in ﬁelds such as analytical chem-
istry, environmental sciences, metrology, and toxicology.
The measurements ranged from genetic contamination of


## Page 3


3
food to high precision comparison of fundamental physi-
cal standards, and were carried out by a mix of national,
university, and commercial laboratories.
All quantities analysed are listed in the Supplementary
Materials [37].
B.
Data selection and collection
Data were entered using a variety of semi-automatic
scripts, optical-character recognition, and manual meth-
ods. No attempt was made to recalculate past results
based on current knowledge, or to remove results that
were later retracted or amended, since the original paper
was the best result at the time it was published. When
the Review of Particle Physics [34] noted that earlier
data had been dropped, the missing results were retrieved
from previous editions [38].
To ensure that measurements were as independent as
possible, measurements were excluded if they were ob-
viously not independent of other data already included.
Because relationships between measurements are often
obscure, however, there undoubtedly remain many cor-
relations between the published results used.
Medical and health data were selected from the 8105
reviews in the Cochrane database [32] as of 25 September
2013. Data were analysed from 221 Intervention Reviews
whose abstract mentioned ≥6 trials with ≥5000 total
participants, and which reported at least one analysis
with ≥5 studies with ≥3500 total participants. The av-
erage heterogeneity inconsistency index (I2 ≡1−dof/χ2)
[36, 39] is about 40% for the analyses reported here. Be-
cause analyses within a review may be correlated, only a
maximum of 3 analyses and 5 comparison groups were in-
cluded from any one review. About 80% of the Cochrane
results are the ratio of intervention and control bino-
mial probabilities, e.g.
mortality rates for a drug and
a placebo. Such ratios are not Normal [40], so they were
converted to diﬀerences that should be Normal in the
Gaussian limit, i.e. when the group size n and probabil-
ity p are such that n, np, and (1 −p)n are all >> 1, so
the binomial distribution converges towards a Gaussian
distribution. (The median observed values for these data
were n = 100, p = 0.16.) The 68.3% binomial probability
conﬁdence interval was calculated for both the interven-
tion and control groups to determine the uncertainties.
C.
Uncertainty evaluation
Measurements with uncertainties are typically re-
ported as x ± u, which means that the interval x −u to
x + u contains with some deﬁned probability “the values
that could reasonably be attributed to the measurand”
[21]. Most frequently, uncertainty intervals are given as
±kuS, where k is the coverage factor and uS is the “stan-
dard uncertainty”, i.e. the uncertainty of a measurement
expressed as the standard deviation of the expected dis-
persion of values. Uncertainties in particle physics and
medicine are often instead reported as the bounds of ei-
ther 68.3% or 95% conﬁdence intervals, which for a Nor-
mal distribution are equivalent to the k = 1 and 2 stan-
dard uncertainty intervals.
For this study, all uncertainties were converted to nom-
inal 68.3% conﬁdence interval uncertainties.
The vast
majority of measurements reported simple single uncer-
tainties, but if more than a single uncertainty was re-
ported, e.g.
“statistical” and “systematic”, they were
added in quadrature.
D.
Normalized diﬀerences
All measurements, xi ± ui, of a given quantity were
combined in all possible pairs and the diﬀerence between
the two measurements of each pair calculated in units of
their combined uncertainty uij:
zij = |xi −xj|
q
u2
i + u2
j
.
(1)
The dispersion of zij values can be used to judge whether
independent measurements of a quantity are “compati-
ble” [41]. A feature of z as a metric for measurement
agreement is that it does not require a reference value
for the quantity.
(The challenges and eﬀects of using
reference values are discussed in Section III C.)
The uncertainties in Equation 1 are combined in
quadrature, as expected for standard uncertainties of in-
dependent measurements. (The eﬀects of any lack of in-
dependence are discussed in Section III B.)
Uncertainties based on conﬁdence intervals may not be
symmetric about the reported value, which is the case for
about 13% of Particle, 6% of Medical, 0.3% of Nuclear,
and 0.06% of Interlab measurements. Following common
(albeit imperfect) practice [42], if the reported plus and
minus uncertainties were asymmetric, zij was calculated
from Eq. 1 using the uncertainty for the side towards the
other member of the comparison pair. For example, if
x1 = 80±3
2, x2 = 100±5
4, and x3 = 126±15
12, then z12 =
(100 −80)/
√
32 + 42 and z23 = (126 −100)/
√
52 + 122.
The distributions of the zij
diﬀerences are his-
togrammed in Fig. 1, with each pair weighted such that
the total weight for a quantity is the number of measure-
ments of that quantity. For example, if a quantity has
10 measurements, there are 45 possible pairs, and each
entry has a weight of 10/45. (Other weighting schemes
are discussed in Section III C.) The ﬁnal frequency dis-
tribution within each research area is then normalized so
that its total observed probability adds up to 1. If the
measurement uncertainties are well evaluated and corre-
spond to Normally distributed probabilities for x, then z
is expected to be Normally distributed with a standard
deviation σ = 1.


## Page 4


4
Probability distribution uncertainties (e.g. the verti-
cal error bars in Fig. 1) were evaluated using a bootstrap
Monte Carlo method where quantities were drawn ran-
domly with replacement from the actual data set until
the number of Monte Carlo quantities equaled the actual
number of quantities.
The resulting artiﬁcial data set
was histogrammed, the process repeated 1000 times, and
the standard deviations of the Monte Carlo probabilities
calculated for each z bin.
Random selection of measurements instead of quanti-
ties was not chosen for uncertainty evaluation because
of the corrections then required to avoid bias and arti-
facts. For example, if measurements are randomly drawn,
a quantity with only 5 measurements will often be miss-
ing from the artiﬁcial data set for having too few (< 5)
measurements drawn, or if it does have 5 measurements
some of them will be duplicates generating unrealistic
z = 0 values, or if duplicates are excluded then they will
always be the same 5 nonrandom measurements. With-
out correcting for such eﬀects, the resulting measurement
Monte Carlo generated uncertainties are too small to be
consistent with the observed bin-to-bin ﬂuctuations in
Fig. 1. Correcting for such eﬀects requires using charac-
teristics of the actual quantities and would be eﬀectively
equivalent to using random quantities.
E.
Data ﬁts
Attempts were made to ﬁt the data to a wide vari-
ety of functions, but by far the best ﬁts were to non-
standardized Student-t probability density distributions
with ν degrees of freedom.
Sν,σ(z) = Γ ((ν + 1)/2)
Γ (ν/2)
1
√νπσ
1
(1 + (z/σ)2/ν)(ν+1)/2
(2)
A
Student-t
distribution
is
essentially
a
smoothly
symmetric normalizable power-law,
with Sν,σ(z)
∼
(z/σ)−(ν+1) for |z| ≫σ√ν.
The ﬁtted parameter σ deﬁnes the core width and over-
all scale of the distribution and is equal to the standard
deviation in the ν →∞Gaussian limit and to the half-
width at half maximum in the ν →1 Cauchy (also known
as Lorentzian or Breit-Wigner) limit. The parameter ν
determines the size of the tails, with small ν correspond-
ing to large tails. The values and standard uncertain-
ties in σ and ν were determined from a non-linear least
squares ﬁt to the data that minimizes the nominal χ2
[43]:
χ2 =
Nbins
X
i=1
(Bi −Sν,σ(zi))2
u2
Bi
(3)
where zi, Bi and uBi are the bin z, contents, and uncer-
tainties of the observed z distributions shown in Fig. 1.
Possible values of z are sometimes limited by the al-
lowed range of measurement values, which could suppress
heavy tails. For example, many quantities are fractions
that must lie between 0 and 1, and there is less room
for two measurements with 10% uncertainty to disagree
by 5σ than for two 0.01% measurements.
The size of
this eﬀect was estimated using Monte Carlo methods to
generate simulated data based on the values and uncer-
tainties of the actual data, constrained by any obvious
bounds on their allowed values. The simulated data was
then ﬁt to see if applying the bounds changed the ﬁt-
ted values for σ and ν. The largest eﬀect was for Med-
ical data where ν was reduced by about 0.1 when mini-
mally restrictive bounds were assumed. Stronger bounds
might exist for some quantities, but determining them
would require careful measurement-by-measurement as-
sessment beyond the scope of this study. For example,
each measurement of the long-term duration of the ef-
fect of a medical drug or treatment would have an upper
bound set by the length of that study. Since correcting
for bounds can only make ν smaller (corresponding to
even heavier tails), and the observed eﬀects were neg-
ligible, no corrections were applied to the values of ν
reported here.
III.
RESULTS
A.
Observed distributions
Histograms of the z distributions for diﬀerent data sets
are shown in Fig. 1. The complementary cumulative dis-
tributions of the data are given in Table I and shown in
Fig. 2.
None of the data are close to Gaussian, but all can rea-
sonably be described by almost-Cauchy Student-t distri-
butions with ν ∼2−3. For comparison, ﬁts to these data
with L´evy stable distributions have nominal χ2 4 to 30
times worse than the ﬁts to Student-t distributions. The
number of “5σ” (i.e. z > 5) disagreements observed is
as high as 0.12, compared to the 6 × 10−7 expected for a
Normal distribution.
The ﬁtted values for ν and σ are shown in Table II. Also
shown in Table II are two data subsets expected to be of
higher quality, BIPM Interlaboratory Key comparisons
(372 quantities, 3712 measurements, 20245 pairs) and
Stable Particle properties (335 quantities, 3041 measure-
ments, 16649 pairs). The Key comparisons [44] should
deﬁne state-of-the-art accuracy, since they are measure-
ments of important metrological standards carried out
by national laboratories. Stable particles are often eas-
ier to study than other particles, so their properties are
expected to be better determined. Both “better” data
subsets do have narrower distributions consistent with
higher quality, but they still have heavy tails. More se-
lected data subsets are discussed in Section III D.
The probability distribution for the nominal χ2 statis-
tic is not expected to be an exact regular χ2 distribution.
The diﬀerences are due to the non-Gaussian uncertain-
ties of the low-population high-z bins, and because the


## Page 5


5
FIG. 1: Histograms of uncertainty normalized diﬀerences (zij from Eq. 1) per unit of z. Horizontal and vertical error
bars are the bin width and the standard uncertainty evaluated by a bootstrap Monte Carlo. The smooth curves are
best-ﬁt Student-t distributions. The dashed curves are Normal distributions.
TABLE I: Observed chance of experimental disagreement by more than z standard uncertainties for diﬀerent data
sets, compared to values expected for some theoretical distributions. Also listed are the z values that bound 95% of
the distribution, i.e. ptrue = 0.05, and p values for that z for a Normal distribution.
z >
1
2
3
5
10
z0.95
pNormal(z0.95)
Interlab
0.58
0.35
0.23
0.12
0.042
9.0
2 × 10−19
(Key)
0.46
0.23
0.13
0.062
0.016
5.7
1 × 10−8
Nuclear
0.38
0.16
0.082
0.033
0.009
4.0
6 × 10−5
Particle
0.41
0.16
0.075
0.024
0.004
3.7
2 × 10−4
(Stable)
0.31
0.091
0.033
0.007
0.0005
2.5
1 × 10−2
Medical
0.47
0.18
0.074
0.020
0.003
3.5
4 × 10−4
Constants
0.42
0.22
0.14
0.078
0.029
7.2
6 × 10−13
Normal (Gaussian)
0.32
0.046
0.0027
5.7 × 10−7
1.5 × 10−23
1.96
5 × 10−2
Student-t (ν = 10)
0.34
0.073
0.013
5.4 × 10−4
1.6 × 10−6
2.23
2.6 × 10−2
Exponential
0.37
0.14
0.050
0.007
4.5 × 10−5
3.0
2.7 × 10−3
Student-t (ν = 2)
0.42
0.18
0.095
0.038
0.010
4.3
2 × 10−15
Cauchy
0.50
0.30
0.20
0.13
0.063
12.8
2 × 10−37
bin contents are not independent since a single measure-
ment can contribute to multiple bins as part of diﬀerent
permutation pairs. Based on ﬁts of simulated data sets
with a mix of ν comparable to the observed data, the
range of nominal χ2 reported in Table II seems reason-
able, i.e. the chances of χ2/dof ≤0.6 or ≥1.9 were 15%
and 2% respectively.
To see if more important quantities are measured with
less disagreement, a small additional data set of mea-
surements of fundamental physical constants (7 quanti-
ties, 320 measurements, 9098 pairs) was also analysed.
The constants are Avogadro’s number, the ﬁne structure


## Page 6


6
TABLE II: Fitted Student-t parameters with nominal χ2 per degree-of-freedom. Also shown are parameters for
quantities with ≥10 measurements, for newer measurements made since the year 2000, and for the approximate
distribution of individual measurements. Uncertainties not shown for σ10, σnew, νx and σx are ≲0.1.
ν
σ
χ2/dof
ν10
σ10
νnew
σnew
νx σx
Interlab
1.64 ± 0.05 1.62 ± 0.05
1.1
1.6 ± 0.1
1.7
1.6 ± 0.1
1.7
1.5 1.3
Key
1.90 ± 0.10 1.12 ± 0.04
1.9
1.7 ± 0.1
1.1
1.9 ± 0.1
1.2
1.7 0.9
Nuclear
1.99 ± 0.06 0.90 ± 0.02
1.6
2.4 ± 0.2
1.1
2.1 ± 0.2
0.9
1.8 0.7
Particle
2.75 ± 0.10 1.05 ± 0.02
1.5
2.8 ± 0.1
1.1
2.6 ± 0.2
1.0
2.4 0.9
Stable 3.45 ± 0.16 0.86 ± 0.02
0.6
3.8 ± 0.4
0.9
7.6 ± 1.3
0.9
2.9 0.8
Medical
3.30 ± 0.11 1.18 ± 0.02
0.7
3.3 ± 0.1
1.2
3.2 ± 0.2
1.2
2.8 1.0
Constants 1.81 ± 0.15 0.89 ± 0.06
0.8
1.8 ± 0.2
0.9
1.3 ± 0.3
1.1
1.7 0.7
Normal
∞
1.0
∞1.0
Cauchy
1.0
√
2
∗
1.0 1.0
∗For uncertainties added in quadrature
FIG. 2: The observed probability of two measurements
disagreeing by more than z standard uncertainties for
diﬀerent data sets:
R ∞
z
P(x)dx. (See also Table I)
constant, the Planck constant, Newton’s gravitational
constant, the deuteron binding energy, the Rydberg con-
stant, and the speed of light (before it became a deﬁned
constant). These measurements have very heavy tails,
despite their importance in physical science. Quantities
with more interest do not seem to be better measured,
as is also shown by considering only quantities with at
least 10 published measurements, which do not have sig-
niﬁcantly smaller tails (see σ10,ν10 in Table II).
Fig. 1 shows that the comparison pairs zij are Student-
t distributed, but what does this imply about the disper-
sion of individual xi measurements? Except for the ν = 1
and ∞Cauchy and Normal limits, the distribution of dif-
ferences of values selected from a Student-t distribution
is not itself a t distribution, but it can be closely approx-
imated as one [45]. The distributions of the parent indi-
vidual x measurements were estimated by Monte Carlo
deconvolution. Artiﬁcial measurements were generated
from t distributions with parameters νx and σx, and these
measurements combined into permutation pairs to gen-
erate an artiﬁcial z distribution. This distribution was
compared to the observed z distributions, and then νx
and σx were iteratively adjusted until the best match was
achieved between the artiﬁcial and observed z distribu-
tions. As shown in Table II, the approximate Student-t
parameters (νx, σx) of the individual measurement pop-
ulations have νx<ν and hence are slightly more Cauchy-
like than the permutation pairs distributions.
B.
Combined uncertainty
The deﬁnition of z by Equation 1 assumes that the
measurements xi and xj are independent and that the
uncertainties ui and uj can be combined following the
rules for standard uncertainties.
If xi and xj are correlated, however, Equation 1 should
be replaced by
zij =
|xi −xj|
q
u2
i −2cov(xi, xj) + u2
j
.
(4)
where cov(xi, xj) is the covariance of xi and xj [21].
It is not in general possible to quantitatively evalu-
ate the covariance for individual pairs of measurements
in the data sets, but the eﬀects of any correlations are
not expected to be large, and they cannot explain the
observed heavy tails. Any positive covariance would de-
crease the denominator in Eq. 4 and increase the width
of the z distributions.
Correlations between measure-
ments are expected to be much more likely positive than
negative, but even perfect anti-correlation could only de-
crease z values by at most a factor of 1/
√
2 compared
to the uncorrelated case. (i.e. Changing cov(xi, xj) from
0 to −uiuj in Eq. 4 reduces zij by
√
2 if ui = uj, and
less if ui ̸= uj.)
Correlations are further discussed in
Section III F.


## Page 7


7
Another possible issue with Equation 1 is that its usual
derivation assumes that ui and uj are standard devia-
tions of the expected dispersion of possible values (e.g.
see Sec. E.3.1 of Ref. [21]). This assumption is a concern
since the standard deviation is an undeﬁned quantity for
Student-t distributions if ν < 2, and the observed z and
inferred x distributions have ν near or below this value.
Even if the variance of a distribution is undeﬁned, how-
ever, the dispersion of the diﬀerence of two independent
variables drawn from such distributions may still be cal-
culated numerically and in some cases analytically.
Cauchy uncertainties add linearly instead of in quadra-
ture, since the distribution of diﬀerences of two variables
drawn from two Cauchy distributions with widths σ1
and σ2 is simply another Cauchy distribution with width
σdiff = σ1 +σ2. The corresponding deﬁnition of z would
be
zCauchy
ij
= |xi −xj|
ui + uj
.
(5)
Almost-Cauchy distributions should almost follow the
rules for combination of Cauchy (ν = 1) distributions.
Applying Equation 5 to the data produces z distribu-
tions that appear almost identical to those in Fig. 1,
except that the ﬁtted values of σ for Interlab, Nu-
clear, Particle, Medical data are smaller by factors of
0.78, 0.80, 0.75, 0.74, while the the ﬁtted values of ν are
almost unchanged (νlinear/νquad = 0.99, 1.00, 0.98, 0.94).
The scale factor for σ would be 1/
√
2 = 0.71 if all mea-
surements of a quantity had equal uncertainties (ui =
uj), since switching from quadrature (Eq. 1) to linear
(Eq. 5) would simply scale all the calculated z values
by 1/
√
2 and not aﬀect ν. Similarly, if data with equal
ν = 1, σ = 1 Cauchy uncertainties were analysed using
Equation 1, the resulting permutation pairs would have
ν = 1, σ =
√
2, as shown in the last line of Table II.
C.
Alternate weighting schemes and compatibility
measures
There are several ways to weight data in the distribu-
tion plots, but the ﬁtted parameter values are not usually
greatly aﬀected by the choice (see Table III). The default
method was to give each measurement equal weight (“M”
in Table III). Jeng [20] gave equal weight to all measure-
ment pairs (“P”), but this gives extreme weight to quan-
tities with a large number (N) of measurements since
the number of permutations grows as (N −1)N/2. Giv-
ing each quantity equal weight (“Q”) also seems less fair,
since a quantity measured many times will be weighted
the same as a quantity measured only a few times.
Instead of using measurement pairs to study com-
patibility, Roos et al. [16] instead calculated the weighted
mean for each quantity, and then plotted the distribution
of the uncertainty-normalized diﬀerence (“h”) from that
TABLE III: Fitted Student-t parameters for weighting
by Quantities (Q), Measurements (M, the default),
Permutations (P), or using diﬀerence from weighted
mean (h).
ν
σ
χ2/dof
Interlab
Q
1.65 ± 0.12
1.35 ± 0.08
4.0
M
1.64 ± 0.05
1.62 ± 0.05
1.1
P
1.70 ± 0.04
1.76 ± 0.05
0.3
h
1.09 ± 0.08
2.06 ± 0.13
1.3
Nuclear
Q
1.93 ± 0.07
0.85 ± 0.02
1.8
M
1.99 ± 0.06
0.90 ± 0.02
1.6
P
2.19 ± 0.07
0.98 ± 0.03
1.4
h
1.82 ± 0.06
0.95 ± 0.02
1.4
Particle
Q
2.76 ± 0.11
1.01 ± 0.02
1.6
M
2.75 ± 0.10
1.05 ± 0.02
1.5
P
2.91 ± 0.09
1.14 ± 0.02
1.0
h
2.26 ± 0.12
1.10 ± 0.03
1.5
Medical
Q
3.44 ± 0.16
1.24 ± 0.02
1.2
M
3.30 ± 0.11
1.18 ± 0.02
0.7
P
3.59 ± 0.12
1.17 ± 0.03
0.4
h
3.00 ± 0.18
1.21 ± 0.04
0.8
mean for each measurement, i.e.
hi =
|xi −¯x|
p
u2
i + u2
¯x
(6)
where
¯x =
P
i
(xi/ui)2
P
i
1/u2
i
and
1
u2
¯x
=
X
i
1
u2
i
(7)
h is very similar to interlaboratory comparison ζ-scores
[46], which are the standard uncertainty normalized dif-
ferences between measurements and an externally as-
signed value for the quantity. The problem with using
actual ζ-scores is that they depend on having assigned
values for the quantity independent of the measurements.
Such values are not usually available for the quantities
studied here, so any assigned value must be determined
from the measurements themselves, and such “consen-
sus values” can be problematic [46]. The particular is-
sue with h is whether the weighted mean ¯x is the best
assigned value for a quantity given all the available mea-
surements. This is a reasonable assumption if the uncer-
tainties are Normal, since then ¯x from Equation 7 is the
maximum likelihood value for x [16]. If the uncertainties
are not Normal, however, ¯x may be far from maximum
likelihood, so it is not clear if ¯x is the best choice for


## Page 8


8
the assigned value. Because of these issues, z was pre-
ferred over h in this study, but the h and z distributions
are very similar. As can be seen from Table III, the ﬁt
quality and parameter values are comparable for h and z
distributions, except the tails appear even heavier in h.
D.
Selected data subsets
To further investigate the variance in the distributions
for diﬀerent types of measurements, several additional
data subsets were examined and their parameters listed
in Table IV.
The Key Metrology data subset is for electrical, ra-
dioactivity, length, mass, and other similar physical
metrology standards.
To see if the most experienced
national laboratories were more consistent, Table IV
also lists Selected Metrology data from only the six na-
tional labs that reported the most Key Metrology mea-
surements. These laboratories were PTB (Physikalisch-
Technische Bundesanstalt, Germany), NMIJ (National
Metrology Institute of Japan), NIST (National Insti-
tutes of Standards and Technology, USA), NPL (Na-
tional Physical Laboratory, UK), NRC (National Re-
search Council, Canada), and LNE (Laboratoire national
de m´etrologie et d’essais, France). Similarly, Key Ana-
lytical chemistry data selected from the same national
labs are also shown. These are for measurements such as
the amount of mercury in salmon, PCBs in sediment, or
chromium in steel. The metrology measurements by the
selected national laboratories do have much lighter tails
with ν ∼10, but this is not the case for their analytical
measurements where ν ∼2.
New Stable particle data have the lightest tail in Ta-
ble II, but it is not clear if this is because the newer
results have better determined uncertainties or are just
more correlated. The trend in particle physics is for fewer
but larger experiments, and more than a third of the
newer Stable measurements were made by just two very
similar experiments (BELLE and BaBar), so the New
Stable data is split into two groups in Table IV. There is
no signiﬁcant diﬀerence between the BELLE/Babar and
Other experiments data.
Nuclear lifetimes with small and large relative uncer-
tainties were compared. They have similar tails, but the
smaller uncertainty measurements appear to underesti-
mate their uncertainty scales.
Measurements of Newton’s gravitation constant are
notoriously variable [14, 47], so a data-set without GN
results was examined. The heavy tail is reduced, albeit
with large uncertainty.
E.
Relative uncertainty
The accuracy of uncertainty evaluations appears to be
similar in all ﬁelds, but unsurprisingly there are notice-
able diﬀerences in the relative sizes of the uncertainties.
In particular, although individual physics measurements
are not typically more reproducible than in medicine,
they often have smaller relative uncertainty (i.e. uncer-
tainty/value) as shown in Fig. 3.
FIG. 3: Distribution of the relative uncertainty for data
from Fig. 1.
FIG. 4: Median ratio of the relative uncertainties
(newer/older) for measurements in each z pair as a
function of the years between the two measurements:
Medical (brown circles), Particle (green triangles),
Nuclear (red squares), Stable (green dashed point-down
triangles), Constants (orange diamonds).
Perhaps more importantly for discovery reproducibil-
ity, uncertainty improves more rapidly in physics than in
medicine, as is shown in Fig. 4. This diﬀerence in rates
of improvement reﬂects the diﬀerence between measure-
ments that depend on steadily evolving technology versus
those using stable methods that are limited by sample
sizes and heterogeneity [48]. The expectation of reduced
uncertainty in physics means that it is feasible to take a
wait-and-see attitude towards new discoveries, since bet-
ter measurements will quickly conﬁrm or refute the new
result. Measurement uncertainty in Nuclear and Particle


## Page 9


9
TABLE IV: Fitted Student-t parameters for selected data, with number of quantities, measurements, and
comparison pairs.
ν
σ
Quant.
Meas.
Pairs
Key
1.9 ± 0.1
1.12 ± 0.04
372
3714
20308
Key Metrology
3.2 ± 0.2
0.94 ± 0.02
197
2030
12070
Selected Metrology
9.9 ± 2.6
0.90 ± 0.03
156
575
948
Key Analytical
1.9 ± 0.2
1.62 ± 0.13
133
1238
5938
Selected Analytical
2.1 ± 0.3
1.39 ± 0.08
127
503
848
New Stable (since 2000)
7.6 ± 1.3
0.90 ± 0.03
357
1278
2478
BABAR/BELLE Stable
6.7 ± 2.1
0.91 ± 0.04
172
435
468
Other New Stable
5.3 ± 0.8
0.79 ± 0.03
209
752
1395
Nuclear
2.0 ± 0.1
0.90 ± 0.02
1437
12380
66677
Lifetimes
2.1 ± 0.2
1.30 ± 0.09
152
1560
9779
ux/x > 0.005
2.2 ± 0.2
1.04 ± 0.06
125
759
3123
ux/x < 0.005
2.8 ± 0.5
1.89 ± 0.22
110
772
3503
Constants
1.8 ± 0.2
0.89 ± 0.06
7
320
9098
Constants without G
3.2 ± 0.5
0.99 ± 0.11
6
231
5182
physics typically improves by about a factor of 2 every
15 years. Constants data improve twice as fast, which is
unsurprising since more eﬀort is expected for more im-
portant quantities.
Physicists also tend not to make new measurements
unless they are expected to be more accurate than pre-
vious measurements. In the data sets reported here, the
median improvement in uncertainty of Nuclear measure-
ments compared to the best previous measurement of the
same quantity is ubest/unew = 2.0±0.3, and the improve-
ment factors for Constants, Particle, and Stable measure-
ments are 1.8 ± 0.3, 1.7 ± 0.2, and 1.3 ± 0.1. In contrast,
Medical measurements typically have greater uncertain-
ties than the best previous measurements, with median
ubest/unew = 0.62±0.03. This is an understandable con-
sequence of diﬀerent uncertainty to cost relationships in
physics and medicine. Study population size is a major
cost driver in medical research, so reducing the uncer-
tainty by a factor of two can cost almost four times as
much, which is rarely the case in physics.
F.
Expectations and correlations
Prior expectations exist for most measurements re-
ported here except for the Interlab data.
Such expec-
tations may suppress heavy tails by discouraging publi-
cation of the anomalous results that populate the tails,
since before publishing a result dramatically diﬀerent
from prior results or theoretical expectations, researchers
are likely to make great eﬀorts to ensure that they have
not made a mistake. Journal editors, referees and other
readers also ask tough questions of such results, either
preventing publication or inducing further investigation.
For example, initial claims [49, 50] of 6σ evidence for
faster-than-light neutrinos and cosmic inﬂation did not
survive to actual publication [51, 52].
FIG. 5: Median z value as a function of time diﬀerence
between the two measurements in each z pair: Medical
(brown circles), Particle (green point-up triangles),
Nuclear (red squares), Constants (orange diamonds),
and Stable (green dashed point-down triangles).
Fig. 5 shows that Physics (Particle, Nuclear, Con-
stants) measurements are more likely to agree if the dif-
ference in their publication dates is small. Such “band-
wagon eﬀects” [20, 36] are not observed in the Medical
data, and they are irrelevant for Interlab quantities which
are usually measured almost simultaneously. These cor-
relations imply that measurements are biased either by
expectations or common methodologies.
Such correla-
tions might explain the small (< 1) values of σx for Nu-
clear, Particle, and Constants data, or it could be that
researchers in these ﬁelds simply tend to overestimate
the scale of their uncertainties [53]. Removing expecta-
tion biases from the Physics data would likely make their
tails heavier.


## Page 10


10
Although Interlab data are not supposed to have any
expectation biases, they are subject to methodological
correlations due to common measurement models, pro-
cedures, and types of instrumentation, so even their tails
would likely increase if all measurements could be made
truly independent.
IV.
DISCUSSION
A.
Comparison with earlier studies
In a famous dispute with Cauchy in 1853, eminent
statistician Ir´en´ee-Jules Bienaym´e ridiculed the idea that
any sensible instrument had Cauchy uncertainties [54].
A century later, however, Harold Jeﬀreys noted that sys-
tematic errors may have a signiﬁcant Cauchy component,
and that the scale of the uncertainty contributed by sys-
tematic eﬀects depends on the size of the random errors
[55].
The results of this study agree with earlier research
that also observed Student-t tails, but only looked at a
handful of subatomic or astrophysics quantities up to z ∼
5 −10 [16, 19, 56–58]. Unsurprisingly, the tails reported
here are mostly heavier than those reported for repeated
measurements made with the same instrument (ν ∼3−9)
[59–61], which should be closer to Normal since they are
not independent and share most systematic eﬀects.
Instead of Student-t tails, exponential tails have been
reported for several nuclear and particle physics data sets
[15, 17, 18, 20], but in all cases some measurements were
excluded. For example, the largest of these studies [20]
looked at particle data (315 quantities, 53322 pairs) using
essentially the same method as this paper, but rejected
the 20% of the data that gave the largest contributions to
the χ2 for each quantity, suppressing the heaviest tails.
Despite this data selection, all these studies have supra-
exponential heavy tails for z ≳5, and so are qualitatively
consistent with the results of this paper. It is possible
that averaging diﬀerent quantities with exponential tails
might produce apparent power-laws [62], but this would
require wild variations in the accuracy of the uncertainty
estimates.
Instead of looking directly at the shapes of the mea-
surement consistency distributions, Hedges [10] com-
pared particle physics and psychology results and found
them to have similar compatibility, with typically almost
half of the quantities in both ﬁelds having statistically
signiﬁcant disagreements.
Thompson and Ellison reported substantial amounts
of “dark uncertainty” in chemical analysis interlabora-
tory comparisons [63]. Uncertainty is “dark” if it does
not appear as part of the known contributions to the un-
certainty of individual measurements, but is inferred to
exist because the dispersion of measured values is greater
than expected based on the reported uncertainties. For
example, six (21%) of 28 BIPM Key Comparisons stud-
ied had ratios (¯sexp/sobs) of expected to observed stan-
dard deviations less than 0.2. This agrees with the Key
Analytical results in Table IV (which include some of
the same Key Comparisons).
For sample sizes match-
ing the 28 Comparisons, 20% of samples drawn from a
ν = 2, σ = 1.4 Student-t distribution would be expected
to have ¯sexp/sobs < 0.2. Pavese also noted the high rate
of inconsistent Key Comparison measurements [64].
The Open Science Collaboration (OSC) recently repli-
cated 100 studies in psychology [65], providing some of
the most direct evidence yet for poor scientiﬁc repro-
ducibility. Using the OSC study’s supplementary infor-
mation, z can be calculated for 87 of the reported orig-
inal/replication measurement pairs, and 27 (31%) dis-
agree by more than 2σ, and 2 (2.3%) by more than 5σ.
This rate of disagreements is inconsistent with selection
bias acting on a Normal distribution unless the >5σ data
are excluded, but can be explained by selection biased
Student-t data with ν ∼3, consistent with the Medical
data reported in Table II.
B.
How measurements fail
When a measurement turns out to be wrong, the rea-
sons for this failure are often unknown, or at least un-
published, so it is interesting to look at examples where
the causes were later understood or can be inferred.
For medical research, heterogeneity in methods or pop-
ulations is a major source of variance. The largest in-
consistency in the Medical dataset is in a comparison of
fever rates after acellular versus whole-cell pertussis vac-
cines [66]. The large variance can likely be explained by
signiﬁcant diﬀerences among the study populations and
especially in how minor adverse events were deﬁned and
reported.
The biggest z values in the Particle data come
from complicated multi-channel partial wave analyses of
strong scattering processes, where many dozens of quan-
tities (particle masses, widths, helicities, . . . ) are simul-
taneously determined. Signiﬁcant correlations often exist
between the ﬁtted values of the parameters but are not
always clearly reported, and evaluations may not always
include the often large uncertainties from choices in data
and parameterization.
The largest disagreement in the Interlab data appears
to be an obvious mistake. In a comparison of radioac-
tivity in water [67], one lab reported an activity of
139352 ± 0.82 Bq/kg when the true value was about
31. Even without knowing the expected activity, the un-
reasonably small fractional uncertainty should probably
have ﬂagged this result. Such gross errors can produce
almost-Cauchy deviations. For example, if the numeri-
cal result of a measurement is simply considered as an
inﬁnite bit string, then any “typographical” glitch that
randomly ﬂips any bit with equal probability will produce
deviations with a 1/x distribution.
One can hope that the best research will not be sloppy,
but not even the most careful scientists can avoid all


## Page 11


11
unpleasant surprises.
In 1996 a team from PTB (the
National Metrological Institute of Germany) reported a
measurement of GN that diﬀered by 50σ from the ac-
cepted value; it took 8 years to track down the cause –
a plausible but erroneous assumption about their elec-
trostatic torque transmitter unit [68]. A 6.5σ diﬀerence
between the CODATA2006 and CODATA2010 ﬁne struc-
ture constant values was due to a mistake in the calcula-
tion of some eighth-order terms in the theoretical value
of the electron anomalous magnetic moment [69]. A 1999
determination [70] of Avogadro’s number by a team from
Japan’s National Research Laboratory of Metrology us-
ing the newer x-ray crystal density method was oﬀby
∼9σ due to subtle silicon inhomogeneities [71]. In an in-
terlaboratory comparison measuring PCB contamination
in sediments, the initial measurement by BAM (the Ger-
man Federal Institute for Materials Research and Test-
ing) disagreed by many standard uncertainties, but this
was later traced to cross-contamination in sample prepa-
ration [72]. Several nuclear half-lives measured by the
US National Institute for Standards and Technology were
known for some years to be inconsistent with other mea-
surements; it was ﬁnally discovered that a NIST sample
positioning ring had been slowly slipping over 35 years of
use [73].
Often discrepancies are never understood and are sim-
ply replaced by newer results.
For example, despite
bringing in a whole new research team to go over every
component and system, the reason for a discordant NIST
measurement of Planck’s constant was never found, but
newer measurements by the same group were not anoma-
lous [74].
C.
Causes of heavy tails
Heavy tails have many potential causes, including bias
[7], overconﬁdent uncertainty underestimates [75], and
uncertainty in the uncertainties [17], but it is not imme-
diately obvious how these would produce the observed t
distributions with so few degrees of freedom.
Even when the uncertainty u is evaluated from the
standard deviation of multiple measurements from a Nor-
mal distribution so that a Student-t distribution would
be expected, there are typically so many measurements
that ν should be much larger than what is observed. Ex-
ceptions to this are when calibration uncertainties dom-
inate, since often only a few independent calibration
points are available, or when uncertainties from system-
atic eﬀects are evaluated by making a few variations to
the measurements, but these cannot explain most of the
data.
Any reasonable publication bias applied to measure-
ments with Gaussian uncertainties cannot create very
heavy tails, just a distorted distribution with Gaussian
tails – to produce one false published 5 σ result would
require bias strong enough to reject millions of studies.
Underestimating σ does not produce a heavy tail, only a
broader Normal z distribution. Mixing multiple Normal
distributions does not naturally produce almost-Cauchy
distributions, except in special cases such as the ratio of
two zero-mean Gaussians.
The heavy tails are not caused by poor older results.
The heaviest-tailed data in Fig. 1 are actually the newest
– 93% of the interlaboratory data are less than 16 years
old – and eliminating older results taken prior to the year
2000 does not reduce the tails for most data as shown in
Table II.
Intentionally making up results, i.e. fraud, could cer-
tainly produce outliers, but this is unlikely to be a signiﬁ-
cant problem here. Since most of the data were extracted
from secondary meta-analyses (e.g.
Review of Parti-
cle Properties, Table of Radionuclides, and Cochrane
Systematic Reviews), results withdrawn for misconduct
prior to the time of the review would likely be excluded.
One meta-analysis in the Medical dataset does include
studies that were later shown to be fraudulent [76], but
the fraudulent results actually contribute slightly less
than average to the overall variance among the results
for that meta-analysis.
D.
Modelling
Modelling the heavy tails may help us understand the
observed distributions. One way is to assume that the
measurement values are normally distributed with stan-
dard deviation t that is unknown but which has a prob-
ability distribution f(t) [15, 17–19, 77]. The measured
value x is then expected to have a probability distribu-
tion
P(x) =
Z ∞
0
dtf(t)
1
√
2πte−x2/(2t2).
(8)
This is essentially a Bayesian estimate with prior f(t)
and a Normal likelihood with unknown variance. If the
uncertainties are accurately evaluated and Normal with
variance σ2, f(t) will be a narrow peak at t = σ. As-
suming that f(t) is a broad Normal distribution leads to
exponential tails [17] for large z.
In order to generate Student-t distributions, f(t) must
be a scaled inverse chi-squared (or Gamma) distribution
in t2 [19, 77]. This works mathematically, but why would
variations in σ for independent measurements have such
a distribution?
Heavy tails can only be generated by eﬀects that can
produce a wide range of variance, so we must model how
consistency testing is used by researchers to constrain
such eﬀects. Consistency is typically tested using a met-
ric such as the calculated chi-squared statistic for the
agreement of N measurements xi [43]
χ2
c(x, u) =
N
X
i=1
(xi −¯x)2
u2
i
(9)
where ¯x is the xi weighted mean and ui are the standard
uncertainties reported by the researchers. For accurate


## Page 12


12
standard uncertainties, χ2
c will have a chi-squared proba-
bility distribution with ν=N−1. If, however, the reported
uncertainties are incorrect and the true standard uncer-
tainties are tui, then it will be χ2
true(x, tu) = χ2
c(x, u)/t2
that is chi-squared distributed.
Researchers will likely search for problems if diﬀerent
consistency measurements have a poor χ2
c(x, u), which
typically means χ2
c(x, u) > ν. The larger an unknown
systematic error is, the more likely it is to be detected and
either corrected or included in the reported uncertainty,
so published results typically have χ2
c(x, u) ∼ν. Since
χ2
c(x, u)/t2 is expected to have a chi-squared distribu-
tion, a natural prior for t2 is indeed the scaled inverse chi-
squared distribution needed to generate Student-t distri-
butions from Equation 8.
More mechanistically, it could be assumed that a Nor-
mally distributed systematic error will be missed by Nm
independent measurements if their χ2(u) = (t2/u2)χ2(t)
is less than some threshold χ2
max ∼ν = Nm −1.
If
the distribution of all possible systematic eﬀects is P0(t),
then the probability distribution for the unfound errors
will be
f(t; ν) = P0 (t) F(χ2
max/t2; ν)
(10)
where F is the cumulative χ2 distribution. P0(t) is un-
known, but a common Bayesian scale-invariant choice is
P0(t) ∝1/tα, with α > 0.
Using this model with the reported uncertainty σ as
the lower integration bound, the curve generated from
Equations 8 and 10 is very close to a ν = Nm −1 + α
Student-t distribution.
The observed small values for
ν mean that both Nm and α must be small.
Making
truly independent consistency tests is diﬃcult, so it is
not surprising that the eﬀective number of checks (Nm)
is usually small.
This model is plausible, but why are systematic eﬀects
consistent with a P0(t) ∝1/tα power-law size distribu-
tion?
E.
Complex systems
Scientiﬁc measurements are made by complex systems
of people and procedures, hardware and software, so one
would expect the distribution of scientiﬁc errors to be
similar to those produced by other comparable systems.
Power-law behaviour is ubiquitous in complex sys-
tems [78], with the cumulative distributions of observed
sizes (s) for many eﬀects falling as 1/sα, and these heavy
tails exist even when the system has been designed and
reﬁned for optimal results.
A Student-t distribution has cumulative tail exponent
α = ν, and the values for ν reported here are consis-
tent with power-law tails observed in other designed com-
plex systems. The frequency of software errors typically
has a cumulative power-law tail corresponding to small
ν ∼2 −3 [79], and in scientiﬁc computing these errors
can lead to quantitative discrepancies orders of magni-
tude greater than expected [80]. The size distribution of
electrical power grid failures has ν ∼1.5 −2 [81], and
the frequency of spacecraft failures has ν ∼0.6−1.3 [82].
Even when designers and operators really, really want to
avoid mistakes, they still occur: the severity of nuclear
accidents falls oﬀonly as ν ∼0.7 [83], similar to the
power-laws observed for the sizes of industrial accidents
[84] and oil spills [85]. Some complex medical interven-
tions have power-law distributed outcomes with ν ∼3−4
[86].
Combining the observed power-law responses of com-
plex systems with the power-law constraints of consis-
tency checking for systematic eﬀects discussed in Section
IV D, leads naturally to the observed consistency distri-
butions with heavy power-law tails. There are also sev-
eral theoretical arguments that such distributions should
be expected.
A systematic error or mistake is an example of a risk
analysis incident, and power-law distributions are the
maximal entropy solutions for such incidents when there
are multiple nonlinear interdependent causes [85], which
is often the case when things go wrong in research.
Scientists want to make the best measurements possi-
ble with the limited resources they have available, so sci-
entiﬁc research endeavours are good examples of highly
structured complex systems designed to optimize out-
comes in the presence of constraints. Such systems are
expected to exhibit “highly optimized tolerance” [87, 88],
being very robust against designed-for uncertainties, but
also hypersensitive to unanticipated eﬀects, resulting
in power-law distributed responses. Simple continuous
models for highly optimized tolerant systems are consis-
tent with the heavy tails observed in this study. These
models predict that α ∼1 + 1/d [88, 89], where d(> 0)
is the eﬀective dimensionality of the system, but larger
values of α arise when some of the resources are used
to avoid large deviations [89], e.g. spending time doing
consistency checks.
F.
How can heavy tails be reduced?
If one believes that mistakes can be eliminated and all
systematic errors found if we just work hard enough and
apply the most rigorous methodological and statistical
techniques, then results from the best scientists should
not have heavy tails. Such a belief, however, is not consis-
tent with the experienced challenges of experimental sci-
ence, which are usually hidden in most papers reporting
scientiﬁc measurements [4, 90]. As Beveridge famously
noted [91], often everyone else believes an experiment
more than the experimenters themselves.
Researchers
always fear that there are unknown problems with their
work, and traditional error analysis cannot “include what
was not thought of” [47].
It is not easy to make accurate a priori identiﬁcations
of those measurements that are so well done that they


## Page 13


13
avoid having almost-Cauchy tails. Expert judgement is
subject to well-known biases [92], and obvious criteria
to identify better measurements may not work. For ex-
ample, the Open Science Collaboration found that re-
searchers’ experience or expertise did not signiﬁcantly
correlate with the reproducibility of their results [65] –
the best predictive factor was simply the statistical signif-
icance of the original result. The best researchers may be
better at identifying problems and not making mistakes,
but they also tend to choose the most diﬃcult challenges
that provide the most opportunities to go wrong.
Reducing heavy tails is challenging because complex
systems exhibit scale invariant behaviour such that re-
ducing the size of failures does not signiﬁcantly change
the shape of their distribution.
Improving sensitivity
makes previously unknown small systematic issues vis-
ible so they can be corrected or included in the total un-
certainty. This improvement reduces σ, but even smaller
systematic eﬀects now become signiﬁcant and tails may
even become heavier and ν smaller. Comparing Figures 1
and 3, it appears that data with higher average relative
uncertainty tend to have heavier tails. This relationship
between relative uncertainty and measurement disper-
sion is reminiscent of the empirical Horwitz power-law
in analytical chemistry [93], where the relative spread of
interlaboratory measurements increases as the required
sensitivity gets smaller, and of Taylor’s Law in ecology
where the variance grows with sample size so that the
uncertainty on the mean does not shrink as 1/
√
N [94].
In principle, statistical errors can be made arbitrar-
ily small by taking enough data, and ν can be made
arbitrarily large by making enough independent consis-
tency checks, but researchers have only ﬁnite time and
resources so choices must be made. Taking more consis-
tency check data limits the statistical uncertainty, since
it is risky to treat data taken under diﬀerent conditions
as a single data set. Consistency checks are never com-
pletely independent since it is impossible for diﬀerent
measurements of the same quantity not to share any peo-
ple, methods, apparatus, theory or biases, so researchers
must decide what tests are reasonable.
The observed
similar small values for ν may reﬂect similar spontaneous
and often unconscious cost-beneﬁt analyses made by re-
searchers.
The data showing the lightest tail reported here (in
Table IV) may provide some guidance and caution. The
high quality of the Selected Metrology standards mea-
surements by leading national laboratories shows that
heavy tails can be reduced by collaboratively taking great
care to ensure consistency by sharing methodology and
making regular comparisons. There are, however, limits
to what can be achieved, as illustrated by the much heav-
ier tail of the analytical standards measured by the same
leading labs. Secondly, consistency is easier than accu-
racy.
Interlaboratory comparisons typically take place
over relatively short periods of time, with participating
institutions using the best standard methods available at
that time. Biases in the standard methods may only be
later discovered when new methods are introduced. For
example, work towards a redeﬁnition of the kilogram and
the associated development of new silicon atom count-
ing technology revealed inconsistencies with earlier watt-
balance measurements, and this has driven improvements
in both methods [74]. Finally, selection bias that hides
anomalous results is hard to eliminate. For one metrol-
ogy key comparison, results from one quantity were not
published because some laboratories reported “incorrect
results” [95].
Reducing tails is particularly challenging for measure-
ments where the primary goal is improved sensitivity that
may lead to new scientiﬁc understanding. By deﬁnition,
a better measurement is not an identical measurement,
and every diﬀerence provides room for new systematic
errors, and every improvement that reduces the uncer-
tainty makes smaller systematic eﬀects more signiﬁcant.
Frontier measurements are always likely to have heavier
tails.
V.
CONCLUSIONS
Published scientiﬁc measurements typically have non-
Gaussian almost-Cauchy ν ∼2 −4 Student-t error dis-
tributions, with up to 10% of results in disagreement by
> 5σ. These heavy tails occur in even the most careful
modern research, and do not appear to be caused by se-
lection bias, old inaccurate data, or sloppy measurements
of uninteresting quantities. For even the best scientists
working on well understood measurements using similar
methodology, it appears diﬃcult to achieve consistency
better than ν ∼10, with about 0.1% of results expected
to be >5σ outliers, a rate a thousand times higher than
for a Normal distribution. These may, however, be un-
derestimates.
Because of selection/conﬁrmation biases
and methodological correlations, historical consistency
can only set lower bounds on heavy tails – multiple mea-
surements may all agree but all be (somewhat) wrong.
The eﬀects of unknown systematic problems are not
completely unpredictable.
Scientiﬁc measurement is a
complex process and the observed distributions are con-
sistent with unknown systematics following the low-
exponent power-laws that are theoretically expected and
experimentally observed for ﬂuctuations and failures in
almost all complex systems.
Researchers do determine the scale of their uncertain-
ties with fair accuracy, with the scale of Medical uncer-
tainties (σx ∼1) slightly more consistent with the ex-
pected value (σx = 1) than in Physics (σx ∼0.7 −0.8).
Medical and Physics research have comparable repro-
ducibility in terms of how well diﬀerent studies agree
within their uncertainties, consistent with a previous
comparison of particle physics with social sciences [10].
Medical research may have slightly lighter tails, while
Physics results typically have better relative uncertainty
and greater statistical signiﬁcance.
Understanding
that
error
distributions
are
often


## Page 14


14
almost-Cauchy should encourage use of t-based [96], me-
dian [97], and other robust statistical methods [98], and
supports choosing Student-t [99] or Cauchy [100] priors in
Bayesian analysis. Outlier-tolerant methods are already
common in modern meta-analysis, so there should be lit-
tle eﬀect on accepted values of quantities with multiple
published measurements, but this better understanding
of the uncertainty may help improve methods and en-
courage consistency.
False discoveries are more likely if researchers apply
Normal conventions to almost-Cauchy data.
Although
much abused, the historically common use of p < 0.05 as
a discovery criterion suggests that many scientists would
like to be wrong less than 5% of the time.
If so, the
results reported here support the nominal 5-sigma dis-
covery rule in particle physics, and may help discussion
of more rigorous signiﬁcance criteria in other ﬁelds [101–
103].
This study should help researchers better understand
the uncertainties in their measurements, and may help
decision makers and the public better interpret the
implications of scientiﬁc research [104].
If nothing
else, it should also remind everyone to never use Nor-
mal/Gaussian statistics when discussing the likelihood
of extreme results.
ACKNOWLEDGEMENTS
I thank the students of the University of Toronto Ad-
vanced Undergraduate Physics Lab for inspiring consid-
eration of realistic experimental expectations, and the
University of Auckland Physics Department for their hos-
pitality during very early stages of this work. I am grate-
ful to D. Pitman for patient and extensive feedback, to
R. Bailey for his constructive criticism, to R. Cousins,
D. Harrison, J. Rosenthal, and P. Sinervo for useful sug-
gestions and discussion, and to M. Cox for many helpful
comments on the manuscript.
DATA ACCESSIBILITY
The sources for all data analysed are listed in the as-
sociated ancillary ﬁle: UncertaintyDataDescription.xls.
[1] McNutt M. 2014 Journals unite for reproducibility. Science 346, 679. (doi:10.1126/science.aaa1724)
[2] Conrad J. 2015 Reproducibility: Don’t cry wolf. Nature 523, 27–28. (doi:10.1038/523027a)
[3] Rosenfeld AH. 1968 Are There Any Far-out Mesons Or Baryons? In Meson Spectroscopy (eds Baltay C, Rosenfeld
AH). New York, USA: W. A. Benjamin. pp. 455–483. (https://archive.org/details/MesonSpectroscopy)
[4] Franklin A. 2013 Shifting Standards: Experiments in Particle Physics in the Twentieth Century. Pittsburgh, USA:
University of Pittsburgh Press. (http://books.google.ca/books?id=jg4gAgAAQBAJ)
[5] Cousins RD. 2014 The Jeﬀreys-Lindley Paradox and Discovery Criteria in High Energy Physics. Synthese
doi:10.1007/s11229–014–0525–z. (doi:10.1007/s11229-014-0525-z)
[6] Dorigo T. 2015 Extraordinary claims: the 0.000029% solution. EPJ Web Conf. 95, 02003.
(doi:10.1051/epjconf/20149502003)
[7] Ioannidis JPA. 2005 Why most published research ﬁndings are false. PLOS Med. 2, 696–701.
(doi:10.1371/journal.pmed.0020124)
[8] Nakagawa S, Cuthill IC. 2007 Eﬀect size, conﬁdence interval and statistical signiﬁcance: a practical guide for
biologists. Biol. Rev. 82, 591–605. (doi:10.1111/j.1469-185X.2007.00027.x)
[9] Cumming G. 2014 The New Statistics: Why and How. Psychol. Sci. 25, 7–29. (doi:10.1177/0956797613504966)
[10] Hedges LV. 1987 How Hard is Hard Science, How Soft is Soft Science? The Empirical Cumulativeness of Research.
Am. Psychol. 42, 443–455. (doi:10.1037/0003-066X.42.5.443)
[11] Porter FC. 2006 The Signiﬁcance of HEP Observations. Int. J. Mod. Phys. A 21, 5574–5582.
(doi:10.1142/S0217751X06034768)
[12] Youden WJ. 1972 Enduring Values. Technometrics 14, 1–11. (doi:10.2307/1266913)
[13] Stigler SM. 1977 Do Robust Estimators Work With Real Data. Ann. Stat. 5, 1055–1098.
(doi:10.1214/aos/1176343997)
[14] Speake C, Quinn T. 2014 The search for Newton’s constant. Phys. Today 67, 27–33. (doi:10.1063/PT.3.2447)
[15] Bukhvostov AP. 1973 On the statistical meaning of experimental data. Leningrad Nucl. Phys. Inst. Rep. 45.
(http://inspirehep.net/record/898468/ﬁles/CM-P00100609.pdf)
[16] Roos M, Hietanen M, Luoma J. 1975 A new procedure for averaging particle properties. Physica Fennica 10, 21–33.
[17] Shlyakhter AI. 1994 An Improved Framework for Uncertainty Analysis: Accounting for Unsuspected Errors. Risk
Anal. 14, 441–447. (doi:10.1111/j.1539-6924.1994.tb00262.x)
[18] Bukhvostov AP. 1997 On the probability distribution of the experimental results. arXiv:hep-ph/9705387.
(http://arxiv.org/abs/hep-ph/9705387)


## Page 15


15
[19] Hanson KM. 2007 Lessons about likelihood functions from nuclear physics. AIP Conf. Proc. 954, 458–467.
(doi:10.1063/1.2821298)
[20] Jeng M. 2007 Bandwagon eﬀects and error bars in particle physics. Nucl. Instrum. Meth. A 571, 704–708.
(doi:10.1016/j.nima.2006.11.024)
[21] Joint Committee for Guides in Metrology. 2008 Guide to the expression of uncertainty in measurement. JCGM 100.
(http://www.iso.org/sites/JCGM/GUM-JCGM100.htm)
[22] Sinervo PK. 2003 Deﬁnition and Treatment of Systematic Uncertainties in High Energy Physics and Astrophysics.
In PHYSTAT 2003, Stanford, USA (eds Lyons L, Mount RP, Reitmeyer R). pp. 122–129.
(http://stanford.io/2fdpKta)
[23] Carlson CE. 2015 The proton radius puzzle. Prog. Part. Nucl. Phys. 82, 59–77. (doi:10.1016/j.ppnp.2015.01.002)
[24] Shields D. 2015 Giving credit where credit is due. Geotechnical Instrumentation News 33–34.
(http://bit.ly/2bc0vnU)
[25] Bravin E, Brun G, Dehning B, Drees A, Galbraith P, Geitz M, Henrichsen K, Koratzinos M, Mugnai G, Tonutti M.
1998 The inﬂuence of train leakage currents on the LEP dipole ﬁeld. Nucl. Instrum. Meth. A 417, 9–15.
(doi:10.1016/S0168-9002(98)00020-5)
[26] Colclough AR. 1987 Two Theories of Experimental Error. J. Res. Nat. Bur. Stand. 92, 167–185.
(doi:10.6028/jres.092.016)
[27] Barlow R. 2002 Systematic Errors: facts and ﬁctions. arXiv:hep-ex/0207026. (http://arxiv.org/abs/hep-ex/0207026)
[28] Pavese F. 2009 About the treatment of systematic eﬀects in metrology. Measurement 42, 1459–1462.
(doi:10.1016/j.measurement.2009.07.017)
[29] Attivissimo F, Cataldo A, Fabbiano L, Giaquinto N. 2011 Systematic errors and measurement uncertainty: An
experimental approach. Measurement 44, 1781–1789. (doi:10.1016/j.measurement.2011.07.011)
[30] Dorsey NE. 1944 The Velocity of Light. Trans. Amer. Philos. Soc. 34, 1–110. (doi:10.2307/1005532)
[31] Pomm´e S. 2016 When the model doesn’t cover reality: examples from radionuclide metrology. Metrologia 53,
S55–S64. (doi:10.1088/0026-1394/53/2/S55)
[32] Cochrane Collaboration. 2013 Cochrane Database of Systematic Reviews. (http://www.thecochranelibrary.com)
[33] Beringer J, et al. 2012 Review of Particle Physics. Phys. Rev. D 86, 010001. (doi:10.1103/PhysRevD.86.010001)
[34] Beringer J, et al. 2013 Review of Particle Physics 2013 partial update for the 2014 edition.
(http://pdg.lbl.gov/2013/tables/contents˙tables.html)
[35] B´e MM, et al. 2013 Table of Radionuclides (Comments on evaluation). Bureau international des poids et mesures
BIPM-5. (http://bit.ly/2fuoaU3)
[36] Baker RD, Jackson D. 2013 Meta-analysis inside and outside particle physics: two traditions that should converge?
Res. Synth. Meth. 4, 109–124. (doi:10.1002/jrsm.1065)
[37] Data description spreadsheet: BaileyDC Uncertainty Data Description.xls, available as arXiv ancillary ﬁle.
[38] Beringer J, et al. 2013 Archives and Errata for the Review of Particle Physics.
(http://pdg.lbl.gov/2013/html/rpp˙archives.html)
[39] Higgins JPT, Thompson SG, Deeks JJ, Altman DG. 2003 Measuring inconsistency in meta-analyses. Brit. Med. J.
327, 557–560. (doi:10.1136/bmj.327.7414.557)
[40] Mart´ın Andr´es A, ´Alvarez Hern´andez M. 2014 Two-tailed approximate conﬁdence intervals for the ratio of
proportions. Stat. Comput. 24, 65–75. (doi:10.1007/s11222-012-9353-5)
[41] Joint Committee for Guides in Metrology. 2012 International vocabulary of metrology – Basic and general concepts
and associated terms (VIM). JCGM 200. (http://www.bipm.org/en/publications/guides/vim.html)
[42] Barlow R. 2003 Asymmetric Errors. In PHYSTAT 2003, Stanford, USA (eds Lyons L, Mount RP, Reitmeyer R).
pp. 250–255.
(http://stanford.io/2gmFUQU)
[43] Bohm G, Zech G. 2010 Introduction to Statistics and Data Analysis for Physicists. Verlag Deutsches
Elektronen-Synchrotron. (doi:10.3204/DESY-BOOK/statistics)
[44] Bureau International des Poids et Mesures. 2014 The BIPM key comparison database. (http://kcdb.bipm.org)
[45] Willink R. 2004 Approximating the diﬀerence of two t-variables for all degrees of freedom using truncated variables.
Aust. N. Z. J. Stat. 46, 495–504. (doi:10.1111/j.1467-842X.2004.00346.x)
[46] International Standards Organization. 2005 Statistical methods for use in proﬁciency testing by interlaboratory
comparisons. ISO 13528:2005(E)
[47] Faller JE. 2014 Precision measurement, scientiﬁc personalities and error budgets: the sine quibus non for big G
determinations. Phil. Trans. R. Soc. A 372, 20140023. (doi:10.1098/rsta.2014.0023)
[48] Peterson D. 2015 All That Is Solid: Bench-Building at the Frontiers of Two Experimental Sciences. Am. Sociol.
Rev. 80, 1201–1225. (doi:10.1177/0003122415607230)
[49] Adam T, et al. 2011 Measurement of the neutrino velocity with the OPERA detector in the CNGS beam.
arXiv:1109.4897v1 [hep-ex]. (http://arxiv.org/abs/1109.4897v1)


## Page 16


16
[50] Ade PAR, et al. 2014 Detection of B-Mode Polarization at Degree Angular Scales by BICEP2. arXiv:1403.3985v1
[astro-ph.CO]. (http://arxiv.org/abs/1403.3985v1)
[51] Adam T, et al. 2012 Measurement of the neutrino velocity with the OPERA detector in the CNGS beam. JHEP
1210, 093. (doi:10.1007/JHEP10(2012)093)
[52] Ade PAR, et al. 2014 Detection of B-Mode Polarization at Degree Angular Scales by BICEP2. Phys. Rev. Lett. 112,
241101. (doi:10.1103/PhysRevLett.112.241101)
[53] Nachman B, Rudelius T. 2012 Evidence for conservatism in LHC SUSY searches. Eur. Phys. J. Plus 127, 157.
(doi:10.1140/epjp/i2012-12157-0)
[54] Bienaym´e M. 1853 Consid´erations a l’appui de la d´ecourverte de Laplace sur la loi de probabilit´e dans la m´ethode
des moindres carr´es. C. R. Acad. Sci. XXXVII, 309–324.
(https://books.google.com/books?id=QHJFAAAAcAAJ&pg=PA322)
[55] Jeﬀreys H. 1961 The Theory of Probability, 3rd ed. Oxford, UK: Oxford University Press.
[56] Chen G, Gott JR, Ratra B. 2003 Non-Gaussian error distribution of Hubble constant measurements. Publ. Astron.
Soc. Pac. 115, 1269–1279. (doi:10.1086/379219)
[57] Crandall S, Houston S, Ratra B. 2015 Non-Gaussian Error Distribution of 7Li Abundance Measurements. Mod.
Phys. Lett. A 30, 1550123. (doi:10.1142/S0217732315501230)
[58] Crandall S, Ratra B. 2015 Non-Gaussian Error Distributions Of LMC Distance Moduli Measurements. Astrophys. J.
815, 87. (doi:10.1088/0004-637X/815/2/87)
[59] Jeﬀreys H. 1938 The law of error and the combination of observations. Philos. Trans. R. Soc. Ser. A-Math. Phys.
Sci. 237, 231–271. (doi:10.1098/rsta.1938.0008)
[60] Jeﬀreys H. 1939 The law of error in the Greenwich variation of latitude observations. Mon. Not. Roy. Astron. Soc.
99, 703–709. (doi:10.1093/mnras/99.9.703)
[61] Dzhun’ IV. 2012 Distribution of errors in multiple large-volume observations. Meas. Tech. 55, 393–396.
(doi:10.1007/s11018-012-9970-6)
[62] Anderson R. 2001 The power law as an emergent property. Mem. Cogn. 29, 1061–1068. (doi:10.3758/BF03195767)
[63] Thompson M, Ellison SLR. 2011 Dark uncertainty. Accredit. Qual. Assur. 16, 483–487.
(doi:10.1007/s00769-011-0803-0)
[64] Pavese F. 2015 Key comparisons: the chance for discrepant results and some consequences. Acta IMEKO 4, 38–47.
(doi:10.21014/acta imeko.v4i4.267)
[65] Open Science Collaboration. 2015 Estimating the reproducibility of psychological science. Science 349, 6251.
(doi:10.1126/science.aac4716)
[66] Zhang L, Prietsch SO, Axelsson I, Halperin SA. 2012 Acellular vaccines for preventing whooping cough in children.
Cochrane Database of Systematic Reviews CD001478.pub5. (doi:10.1002/14651858.CD001478.pub5)
[67] Terrestrial Environment Laboratory, IAEA Seibersdorf. 2010 ALMERA Proﬁciency Test Determination of Naturally
Occurring Radionuclides in Phosphogypsum and Water (IAEA-CU-2008-04). Austria: International Atomic Energy
Agency IAEA/AQ/15. (http://www-pub.iaea.org/MTCD/publications/PDF/IAEA-AQ-15˙web.pdf)
[68] Michaelis W, Melcher J, Haars H. 2004 Supplementary investigations to PTB’s evaluation of G. Metrologia 41,
L29–L32. (doi:10.1088/0026-1394/41/6/L01)
[69] Mohr PJ, Taylor BN, Newell DB. 2012 CODATA Recommended Values of the Fundamental Physical Constants:
2010. J. Phys. Chem. Ref. Data 41, 043109. (doi:10.1063/1.4724320)
[70] Fujii K, Tanaka M, Nezu Y, Nakayama K, Fujimoto H, De Bievre P, Valkiers S. 1999 Determination of the
Avogadro constant by accurate measurement of the molar volume of a silicon crystal. Metrologia 36, 455–464.
(doi:10.1088/0026-1394/36/5/7)
[71] De Bievre P, et al. 2001 A reassessment of the molar volume of silicon and of the Avogadro constant. IEEE Trans.
Instrum. Meas. 50, 593–597. (doi:10.1109/19.918199)
[72] Schantz M, Wise S. 2004 CCQM-K25: Determination of PCB congeners in sediment. Metrologia 41, 08001.
(doi:10.1088/0026-1394/41/1A/08001)
[73] Pomm´e S. 2015 The uncertainty of the half-life. Metrologia 52, S51–S65. (doi:10.1088/0026-1394/52/3/S51)
[74] Gibney E. 2015 Experiments to redeﬁne kilogram converge at last. Nature 526, 305–306. (doi:10.1038/526305a)
[75] Henrion M, FischhoﬀB. 1986 Assessing uncertainty in physical constants. Am. J. Phys. 54, 791–798.
(doi:10.1119/1.14447)
[76] Carlisle J, Pace N, Cracknell J, Møller A, Pedersen T, Zacharias M. 2013 (5) What should the Cochrane
Collaboration do about research that is, or might be, fraudulent? Cochrane Database of Systematic Reviews.
(doi:10.1002/14651858.ED000060)
[77] Dose V, Von Der Linden W. 1999 Outlier Tolerant Parameter Estimation. In Maximum Entropy and Bayesian
Methods: Garching, Germany 1998 vol. 105 of Fundamental Theories of Physics. Netherlands: Springer. pp. 47–56.
(doi:10.1007/978-94-011-4710-1“˙4)


## Page 17


17
[78] Clauset A, Shalizi CR, Newman MEJ. 2009 Power-Law Distributions in Empirical Data. SIAM Rev. 51, 661–703.
(doi:10.1137/070710111)
[79] Hatton L. 2012 Defects, Scientiﬁc Computation and the Scientiﬁc Method. IFIP Advances in Information and
Communication Technology 377, 123–138. (doi:10.1007/978-3-642-32677-6˙8)
[80] Hatton L, Roberts A. 1994 How Accurate Is Scientiﬁc Software. IEEE Trans. Softw. Eng. 20, 785–797.
(doi:10.1109/32.328993)
[81] Dobson I, Carreras BA, Lynch VE, Newman DE. 2007 Complex systems analysis of series of blackouts: Cascading
failure, critical points, and self-organization. Chaos 17, 026103. (doi:10.1063/1.2737822)
[82] Karimova LM, Kruglun OA, Makarenko NG, Romanova NV. 2011 Power Law Distribution in Statistics of Failures in
Operation of Spacecraft Onboard Equipment. Cosm. Res. 49, 458–463. (doi:10.1134/S0010952511040058)
[83] Sornette D, Maillart T, Kroeger W. 2013 Exploring the limits of safety analysis in complex technological systems.
Int. J. Disaster Risk Reduct. 6, 59–66. (doi:10.1016/j.ijdrr.2013.04.002)
[84] Lopes AM, Tenreiro Machado JA. 2015 Power Law Behavior and Self-Similarity in Modern Industrial Accidents. Int.
J. Bifurc. Chaos 25, 1550004. (doi:10.1142/S0218127415500042)
[85] Englehardt J. 2002 Scale invariance of incident size distributions in response to sizes of their causes. Risk Anal. 22,
369–381. (doi:10.1111/0272-4332.00016)
[86] Burton C. 2012 Heavy Tailed Distributions of Eﬀect Sizes in Systematic Reviews of Complex Interventions. PLOS
ONE 7, e34222. (doi:10.1371/journal.pone.0034222)
[87] Carlson J, Doyle J. 1999 Highly optimized tolerance: A mechanism for power laws in designed systems. Phys. Rev.
E 60, 1412–1427. (doi:10.1103/PhysRevE.60.1412)
[88] Carlson J, Doyle J. 2002 Complexity and robustness. Proc. Natl. Acad. Sci. USA 99, 2538–2545.
(doi:10.1073/pnas.012582499)
[89] Newman M, Girvan M, Farmer J. 2002 Optimal design, robustness, and risk aversion. Phys. Rev. Lett. 89, 28301.
(doi:10.1103/PhysRevLett.89.028301)
[90] Collins HM. 2001 Tacit knowledge, trust and the Q of sapphire. Soc. Stud. Sci. 31, 71–85.
(doi:10.1177/030631201031001004)
[91] Beveridge WIB. 1957 The Art of Scientiﬁc Investigation. W. W. Norton, New York.
(https://archive.org/details/artofscientiﬁci00beve)
[92] Sutherland WJ, Burgman MA. 2015 Use experts wisely. Nature 526, 317–318. (doi:10.1038/526317a)
[93] Horwitz W, Albert R. 2006 The Horwitz ratio (HorRat): A useful index of method performance with respect to
precision. J. AOAC Int. 89, 1095–1109.
[94] Eisler Z, Bartos I, Kertesz J. 2008 Fluctuation scaling in complex systems: Taylor’s law and beyond. Adv. Phys. 57,
89–142. (doi:10.1080/00018730801893043)
[95] Thalmann R. 2002 CCL key comparison: calibration of gauge blocks by interferometry. Metrologia 39, 165–177.
(doi:10.1088/0026-1394/39/2/6)
[96] Lange KL, Little RJA, Taylor JMG. 1989 Robust Statistical Modeling Using the t Distribution. J. Am. Stat. Assoc.
84, 881–896. (doi:10.2307/2290063)
[97] Gott III JR, Vogeley MS, Podariu S, Ratra B. 2001 Median statistics, H0, and the accelerating universe. Astrophys.
J. 549, 1–17. (doi:10.1086/319055)
[98] Avella Medina M, Ronchetti E. 2015 Robust statistics: a selective overview and new directions. Wiley Interdiscip.
Rev. Comput. Stat. 7, 372–393. (doi:10.1002/wics.1363)
[99] Gelman A. 2006 Prior distributions for variance parameters in hierarchical models (Comment on an Article by
Browne and Draper). Bayesian Anal. 1, 515–533. (doi:10.1214/06-BA117A)
[100] Polson NG, Scott JG. 2012 On the Half-Cauchy Prior for a Global Scale Parameter. Bayesian Anal. 7, 887–901.
(doi:10.1214/12-BA730)
[101] Johnson VE. 2013 Revised standards for statistical evidence. Proc. Natl. Acad. Sci. USA 110, 19313–19317.
(doi:10.1073/pnas.1313476110)
[102] Gelman A, Robert CP. 2014 Revised evidence for statistical standards. Proc. Natl. Acad. Sci. USA 111, E1933.
(doi:10.1073/pnas.1322995111)
[103] Colquhoun D. 2014 An investigation of the false discovery rate and the misinterpretation of p-values. R. Soc. Open
Sci. 1, 140216. (doi:10.1098/rsos.140216)
[104] FischhoﬀB, Davis AL. 2014 Communicating scientiﬁc uncertainty. Proc. Natl. Acad. Sci. USA 111, 13664–13671.
(doi:10.1073/pnas.1317504111)

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1612_00778v2_not_normal_the_uncertainties_of_scientific_measurements
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2016/1612_00778V2_NOT_NORMAL_THE_UNCERTAINTIES_OF_SCIENTIFIC_MEASUREMENTS.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

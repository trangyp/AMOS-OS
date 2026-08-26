---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1801.05862v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1801.05862v1_Glauber-model_analysis_of_5_TeV___bf_p_-Pb_centrality_compared_to_a_two-componen

> Source: 1801.05862v1_Glauber-model_analysis_of_5_TeV___bf_p_-Pb_centrality_compared_to_a_two-componen.pdf

> Pages: 24

---


## Page 1


version 2.0
Glauber-model analysis of 5 TeV p-Pb centrality compared to a two-component (soft
+ hard) model of hadron production in high-energy nuclear collisions
Thomas A. Trainor
CENPA 354290, University of Washington, Seattle, WA 98195
(Dated: August 15, 2018)
A recent study of 5 TeV p-Pb centrality combined a Glauber model of p-Pb collision geometry
with an assumption of linear scaling between nch (charge) integrated within some η acceptance and
the number of nucleon participants Npart. The study concluded that Npart increases to nearly 16 in
central collisions, and the high-pt region of p-Pb pt spectra rescaled by the Glauber-estimated number
of p-N binary collisions remains consistent with a p-p spectrum for the same energy, independent
of p-Pb centrality. However, the relation between Npart and nch derived from a two-component
(soft + hard) model (TCM) study of ensemble-mean ¯pt data for the same system is quite diﬀerent.
This article reports a detailed analysis of the Glauber study and the question of centrality in p-A
collisions. The Glauber centrality model is compared with the ¯pt TCM to understand the sources
of major diﬀerences.
The assumption of linear proportionality between nch and Npart is found
to be inconsistent with ¯pt data. Properties of the convolution integral relating a diﬀerential cross
section and hadron production model to an event distribution on nch are examined. An alternative
diﬀerential-cross-section distribution is inferred from charge-multiplicity data, and the upper limit
on Npart is estimated to be near 8. The TCM centrality model is then applied to pt spectrum ratios
to predict results for p-Pb spectra. The spectrum TCM is tested with identiﬁed-pion spectra from 5
TeV p-Pb collisions and the result is consistent with previous p-p TCM results. A TCM prediction
that the spectrum ratio at high pt should increase to 14 for central p-Pb collisions due to quadratic
dependence of dijet production on nch is consistent with ¯pt data from the same system.
PACS numbers: 12.38.Qk, 13.87.Fh, 25.75.Ag, 25.75.Bh, 25.75.Ld, 25.75.Nq
I.
INTRODUCTION
Estimation of collision centrality (e.g. impact parame-
ter b) for nucleus-nucleus (A-A) collisions according to a
Glauber Monte Carlo (MC) model based on the eikonal
approximation seems well established and reasonably ac-
curate [1, 2]. The concept of centrality (or impact pa-
rameter) for p-p collisions has been invoked within some
Monte Carlo models (e.g. PYTHIA [3]), but its relevance
may be questioned [4, 5].
The centrality of asymmet-
ric p-A or d-A systems is important because of the role
such data are expected to play in verifying the forma-
tion of quark-gluon plasma (QGP) in more-central A-A
collisions. However, centrality estimation in asymmetric
systems is more diﬃcult as revealed in the present study.
Centrality determination requires deﬁnition of a quan-
titative relation between geometry parameters such as
participant nucleon number Npart or number of nucleon-
nucleon (N-N) binary collisions Nbin and a measured
quantity such as integrated charge multiplicity nch within
some angular acceptance ∆η.
A hadron production
model is required for such deﬁnition, and the accuracy of
centrality determination depends on the validity of the
model, especially its basis in various forms of data.
The two-component (soft + hard) model (TCM) of
hadron production near midrapidity (η ≈0) [6] has
been applied to hadron yield, spectrum and correlation
data from p-p, p-A and A-A collisions at the relativistic
heavy ion collider (RHIC) [4, 7–12] and the large hadron
collider (LHC) [13–15].
Based on substantial evidence
from data the soft component is interpreted to repre-
sent participant-nucleon dissociation to charge-neutral
hadron pairs, and the hard component is interpreted
to represent fragmentation of large-angle-scattered low-x
partons (gluons) to minimum-bias (MB) dijets.
The TCM has been applied recently to ensemble-mean
¯pt data from 5 TeV p-Pb collisions (as well as p-p and
Pb-Pb data) [16] and describes those data within their
uncertainties [13, 14]. The TCM thereby determines the
relation between Npart and nch for that system which, in
eﬀect, relates p-Pb centrality to a measured quantity.
A recent study of p-Pb centrality adopted an alterna-
tive strategy based on a Glauber MC model of the p-Pb
system including certain assumptions about collision ge-
ometry and hadron production, especially assumption of
linear scaling between Npart and nch [17]. The Glauber
study also reported the systematics of p-Pb pt spectra,
concluding that at higher pt (e.g. above 10 GeV/c) the
spectra exhibit binary-collision scaling: spectra divided
by Nbin = Npart −1 are consistent with p-p spectra in
that pt interval independent of nch or centrality. The in-
ferred relation between Npart (and other Glauber param-
eters) and nch diﬀers greatly from TCM-based ¯pt studies
reported in Refs. [13, 14]. The conclusion about binary-
collision scaling of the high-pt region of p-Pb spectra is
also at odds with TCM results as demonstrated below.
It is essential to determine the reasons for disagreement
and which centrality method, if either, is correct.
This article reports a detailed study of the Glauber
centrality method and its relation to the TCM. The in-
ternal consistency of the model is examined.
Glauber
results are compared step-by-step with TCM results. As
noted, major diﬀerences emerge concerning the assumed
arXiv:1801.05862v1  [hep-ph]  17 Jan 2018


## Page 2


2
relation between Npart and nch, between what is adopted
for the Glauber study and what is inferred from ¯pt data
for the TCM. The geometric Glauber MC used to de-
scribe p-Pb collisions and predict the cross-section dis-
tribution on Npart is a major issue. The centrality trend
for p-Pb spectrum ratios inferred via the Glauber model
conﬂicts with measured identiﬁed-pion spectra that pre-
cisely follow TCM predictions.
This article is arranged as follows: Section II brieﬂy
introduces the Glauber-model study of p-Pb centrality
from Ref. [17]. Section III describes the TCM for ¯pt data
from 5 TeV p-Pb collisions as reported in Ref. [14]. Sec-
tion IV provides a detailed description of the Glauber-
model analysis with some implications and possible in-
consistencies.
Section V compares the Glauber analy-
sis to TCM results and itemizes diﬀerences. Section VI
presents an alternative TCM centrality analysis and sug-
gests basic reasons for disagreement between Glauber
analysis and TCM. Section VII describes TCM predic-
tions for spectrum-ratio trends compared to those re-
ported in Ref. [17]. Identiﬁed-pion data from the p-Pb
collision system are introduced to test the predictions.
Section VIII discusses systematic uncertainties.
Sec-
tions IX and X include discussion and summary.
Ap-
pendix A presents the TCM for p-p pt spectrum data used
as a basis for the p-p and p-Pb ¯pt TCMs. Appendix B
describes the TCM for ¯pt data from p-p collisions.
II.
GLAUBER ANALYSIS OF p-Pb COLLISIONS
Reference [17] motivates the study of p-Pb centrality
with two issues: (a) p-A is a null hypothesis for QGP for-
mation in A-A collisions, and (b) recent claims of “collec-
tivity” in p-A and p-p systems [18] should be evaluated.
p-A collisions are intended to serve as a control or refer-
ence system “...to disentangle hot nuclear matter eﬀects
which are characteristic of the formation of the quark-
gluon plasma (QGP) from cold nuclear matter eﬀects”
– for instance, by comparisons of spectrum ratio RAA
from A-A collisions with ratio RpA from p-A collisions.
Whereas RAA ≪1 at higher pt for more-central collisions
is interpreted to indicate strong jet quenching consistent
with QGP formation RpA ≈1 (binary-collision scaling)
in the same pt interval and more-central p-A collisions
would indicate no jet quenching – a preferred null result.
However, the A-A–p-A ∼QGP–no-QGP dichotomy is
inconsistent with recent interpretations of data to indi-
cate collective manifestations (ﬂows) in smaller systems,
e.g. p-A or even p-p collisions [18].
Evidence is cited
(e.g. the ¯pt data reported in Ref. [16]) to claim that data
for lower pt in “...pPb collisions cannot be explained by
an incoherent [i.e. linear] superposition of pp [p-N] colli-
sions,” any deviations interpreted to signal “collectivity”
i.e. hydrodynamic ﬂows. The strength of collective eﬀects
is said to increase with nch and therefore with p-A cen-
trality, implying a strong collision-geometry dependence.
Determining p-A collision geometry is therefore essential.
Accurate estimation of collision geometry is also re-
quired to evaluate spectrum ratio RpA that includes num-
ber of binary collisions Nbin in the ratio. Reference [17]
concludes that “...particle production at high pT in pPb
collisions indeed can be approximated by an incoherent
[linear] superposition of pp collisions” because ratio es-
timates appear to be independent of p-Pb centrality in
that pt interval. But the conclusion depends on accurate
estimation of Nbin in relation to a measured quantity.
Centrality estimation is based on a Glauber MC used
to relate Npart to fractional cross section σ/σ0 and an
assumption that serves as a hadron production model:
Charge multiplicity nch integrated within some pseudo-
rapidity η interval is proportional to the number of par-
ticipant nucleons Npart. The two elements are combined
in a convolution integral to predict an event-frequency
distribution on nch which is then compared to data. Cen-
trality classes are deﬁned by cuts on nch and correspond-
ing parameter values for each class determined from the
MC: “For a given centrality class, deﬁned by selections in
the measured [nch] distribution, the information from the
Glauber MC in the corresponding generated distribution
is used to calculate [means of several Glauber parame-
ters, e.g. Npart].” The method is applied to the same 5
TeV p-Pb data sample that appears in Refs. [13, 14, 16].
The present study reviews the Glauber methods and
compares them to results from a TCM analysis [14] of
p-Pb ¯pt data from Ref. [16] wherein certain contradictions
emerge. An alternative centrality analysis derived from
the ¯pt TCM leads to quite diﬀerent results.
III.
¯pt TCM FOR p-Pb COLLISIONS
Appendix A describes a TCM for p-p pt spectra and
reviews systematic evolution with event multiplicity and
collision energy. pt spectrum structure is directly related
to ¯pt trends. Appendix B describes a TCM for ¯pt data
from p-p collisions as a basis for p-Pb ¯pt analysis. With
the dominant role of MB jets established for p-p (p-N,
N-N) collisions and elements of the p-p ¯pt TCM intro-
duced the p-Pb ¯pt TCM is presented here in greater de-
tail. Note that the TCM is a linear-superposition model.
The
TCM
for
complex
A-B
collisions
relies
on
participant-pair number Npart/2, number of N-N binary
collisions Nbin and mean number of binary collisions per
participant pair ν = 2Nbin/Npart. In addition, hard/soft
ratio x(ns) ≡¯ρhNN/¯ρsNN averaged over participant N-N
pairs within individual A-B collisions is a generalization
of x(ns) = ¯ρh/¯ρs for p-p collisions [7].
Reference [13]
reported a preliminary TCM analysis of ¯pt data from
Ref. [16].
Reference [14] describes an updated TCM
based on jet systematics in Refs. [15, 19]. As noted in
Ref. [14] the ¯pt trend for p-Pb collisions is identical to
the p-p trend at lower nch but deviates substantially at
higher nch, suggesting a formulation of the TCM for the
p-Pb collision system based on generalization of the prod-
uct x(ns)ν(ns), with soft multiplicity ns (∝total number


## Page 3


3
of participant low-x gluons) as the independent variable.
For p-p collisions ν ≡1 and x(ns) ≈α¯ρs based on spec-
trum studies [4, 7]. For A-A collisions ν is deﬁned by a
Glauber MC [2], and x(ν) is inferred from a measured
trend of per-participant hadron yields [20]. Correspond-
ing elements for p-Pb data are determined below.
A.
Formulating a p-Pb TCM
A universal TCM for hadron pt spectrum ¯ρ0(pt) is ex-
pressed for any A-B system as
¯ρ0(pt) ≈
1
pt
d2nch
dptdη
(1)
= ¯ρs(pt) + ¯ρh(pt)
= Npart
2
¯ρsNN ˆS0(pt) + Nbin¯ρhNN ˆH0(pt)
¯ρ0(pt)
¯ρs
= ˆS0(pt) + x(ns)ν(ns) ˆH0(pt),
where ¯ρx = nx/∆η are averaged over acceptance ∆η and
hats denote unit-integral (on pt or yt) quantities.
For
p-p collisions Npart/2 = Nbin ≡1. For composite A-B
systems hard and soft components factorize as shown.
With integration over pt or yt the mean charge density is
¯ρ0 = ¯ρs + ¯ρh
(2)
= Npart
2
¯ρsNN(ns) + Nbin¯ρhNN(ns)
2
Npart
¯ρ0 = ¯ρsNN(ns) [1 + x(ns)ν(ns)]
¯ρ0
¯ρs
= 1 + x(ns)ν(ns)
¯ρ′
0
¯ρs
= n′
ch
ns
= ξ + x(ns)ν(ns),
where x(ns) ≡¯ρhNN/¯ρsNN ≈α¯ρsNN for p-p or p-A
collisions, ¯ρs = [Npart(ns)/2] ¯ρsNN(ns) is a factorized
soft-component density for any system and ¯ρh(ns) =
Nbin(ns)¯ρhNN(ns) is a factorized hard component.
The ensemble-mean total pt integrated over some an-
gular acceptance ∆η is
¯Pt = ∆η
Z ∞
0
dpt p2
t ¯ρ0(pt) =
¯Pts + ¯Pth
(3)
= Npart
2
nsNN(ns)¯ptsNN + NbinnhNN(ns)¯pthNN.
Data indicate that ¯ptsNN →¯pts is a universal quantity.
The corresponding TCM for ¯p′
t with nonzero pt,cut is
¯P ′
t
n′
ch
≡¯p′
t ≈
¯pts + x(ns)ν(ns) ¯pthNN(ns)
ξ + x(ns) ν(ns)
(4)
n′
ch
ns
¯p′
t ≈
¯Pt
ns
= ¯pts + x(ns)ν(ns) ¯pthNN(ns),
where ξ is the fraction of ˆS0(pt) admitted by a low-pt
acceptance cut pt,cut and primes indicate correspond-
ing biased quantities. For p-A data evolution of factors
x(ns) ν(ns) from strictly p-p–like to alternative behavior
is observed near a transition point ¯ρs0, but ¯pthNN(ns) →
¯pth0 is assumed to maintain a ﬁxed p-p (N-N) value in
the p-A system (i.e. no jet modiﬁcation).
Soft density ¯ρs, interpreted to represent participant
low-x gluons, is adopted as a universal TCM parameter
for all collision systems. The factorization
¯ρs = [Npart(ns)/2] ¯ρsNN(ns)
(5)
then deﬁnes ¯ρsNN(ns) for any collision system wherein
Npart(ns)/2 is deﬁned, and x(ns) ≈α¯ρsNN(ns) for p-N
collisions within p-A collisions [4, 7].
It follows that
Npart(ns)/2 = α¯ρs/x(ns) given a model for x(ns). For
p-A collisions Nbin = Npart−1, and ν(ns) = 2Nbin/Npart
are then determined by x(ns). Based on previous analy-
sis in Ref. [14] p-Pb data indicate that ¯pt increases with
nch according to a p-p trend for lower nch but less rapidly
above a transition point, suggesting a similar structure
for x(ns). The simplest form is linear increase with ¯ρs
also above the transition point but with reduced slope.
Figure 1 (left) shows a model for x(ns) in the form
x(ns) =
α
{[1/¯ρs]n1 + [1/f(ns)]n1}1/n1 ,
(6)
where f(ns) = ¯ρs0 + m0(¯ρs −¯ρs0). Below the transition
at ¯ρs0, x(ns) ≈α¯ρs as for p-p collisions (dashed line).
Above the transition x(ns) increases with slope m0 < 1
(dotted line). Exponent n1 controls the transition width.
Speciﬁc parameter values for x(ns) are noted below. The
dotted line and hatched band indicate estimates for x(ns)
and ¯ρs from non-single-diﬀractive (NSD) p-p collisions.
0
0.05
0.1
0.15
0.2
0.25
0.3
0
20
40
60
80
ns / ∆η
x(ns)
α ρs
p-N
p-Pb
NSD
NSD
5 TeV
0
0.25
0.5
0.75
1
1.25
1.5
1.75
2
2.25
2.5
0
20
40
60
80
ns / ∆η
ν(ns)
p-N
p-Pb
NSD
Pb-Pb
5 TeV
2.76 TeV
FIG. 1:
Left: Evolution of TCM hard/soft parameter x(ns)
with mean soft charge density ¯ρs = ns/∆η following a linear
p-N (p-p) trend (dashed) for lower multiplicities and a trend
with ten-fold reduced slope for higher multiplicities (dotted)
to describe p-Pb ¯pt data. Right: Mean participant pathlength
ν ≡2Nbin/Npart vs ¯ρs (solid) as determined by the x(ns)
trend in the left panel (see text).
The ν trend for Pb-Pb
collisions (dash-dotted) is included for comparison.
Figure 1 (right) shows ν ≡2Nbin/Npart for p-Pb data
(solid curve) based on Npart(ns)/2 = α¯ρs/x(ns) and


## Page 4


4
Nbin = Npart −1 as noted above, with x(ns) as de-
scribed in the left panel (solid curve). The dash-dotted
curve indicates the ν = 2Nbin/Npart ≈(Npart/2)1/3
trend for Pb-Pb collisions for comparison, consistent with
the eikonal approximation assumed for the A-A Glauber
model. For Pb-Pb ν ∈[1, 6] whereas for p-Pb ν ∈[1, 2].
B.
TCM description of p-A data
Figure 2 (left) shows uncorrected ¯p′
t data for 106 mil-
lion 5 TeV p-Pb collisions vs corrected nch (points) from
Ref. [16]. The dashed curve is the TCM for 5 TeV p-p
collisions given by Eq. (B3) with α = 0.0113 derived from
the parametrization in Fig. 24 (right), ¯pts ≈0.4 GeV/c,
¯pth0 = 1.3 GeV/c and ξ = 0.73. The solid curve through
points is the TCM described by Eqs. (4) and (6) with pa-
rameters α = 0.0113 and ¯pth0 = 1.3 GeV/c held ﬁxed as
for 5 TeV p-p collisions (assuming no jet modiﬁcation).
Parameters ¯ρs0 ≈3¯ρsNSD ≈15 and m0 ≈0.10 are ad-
justed to accommodate the p-Pb data. Exponent n1 = 5
aﬀects the TCM shape only near ¯ρs0.
0.45
0.5
0.55
0.6
0.65
0.7
0.75
0.8
0.85
0.9
0
50
100
nch / ∆η
¯ p t ′ (GeV/c)
5 TeV p-p
5 TeV p-Pb
NSD
¯pts ′
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
0
20
40
60
80
ns / ∆η
(nch ′/ns)  ¯pt ′ (GeV/c)
NSD
¯pts
p-p
5 TeV p-Pb
FIG. 2:
Left: Uncorrected ensemble-mean ¯pt data from 5
TeV p-Pb collisions (open squares) vs corrected charge density
¯ρ0 = nch/∆η from Ref. [16]. The solid and dashed curves are
TCM data descriptions from Ref. [14].
Right: Curves and
data in the left panel transformed by factor ¯ρ′
0/¯ρs = n′
ch/ns
deﬁned by Eq. (2) (ﬁfth line).
Figure 2 (right) shows data in the left panel converted
to (n′
ch/ns) ¯p′
t ≈¯Pt/ns by factor ξ + x(ns)ν(ns) as in
Eq. (2) (ﬁfth line). The dashed line is the TCM for 5
TeV p-p collisions deﬁned by Eq. (B4). The solid curve
is the p-Pb TCM deﬁned by Eq. (4) (second line) corre-
sponding to the solid curve in the left panel. Transform-
ing data from left to right panels requires an estimate of
ns for the data to evaluate the required conversion factor
ξ + x(ns)ν(ns). The map ns →nch for the TCM from
Eq. (2) (second line) is inverted via linear interpolation
to provide the map nch →ns for data.
p-Pb ¯pt data provide understanding of the transition
from isolated p-p or N-N collisions to the geometry of
compound A-B systems, from noneikonal p-p to eikonal
A-A Glauber model. The central element is factoriza-
tion of the soft density ¯ρs = ¯ρsNN(ns) Npart(ns)/2 com-
bining N-N internal structure (¯ρsNN) and A-B geometry
(Npart). The p-Pb TCM is based on the key assumption
that the dijet production trend ¯ρhNN = α¯ρ2
sNN (aver-
aged over all N-N collisions) is universal, in which case
x(ns) ≡
¯ρhNN
¯ρsNN
=
α¯ρs
Npart/2
(7)
determines Npart(ns) given a model for x(ns). The p-A
x(ns) model is the simplest extrapolation of the p-p
x(ns) ≈α¯ρs linear trend possible: a continuing linear
trend but with reduced slope beyond a transition point as
in Eq. (6). For p-Pb collisions the other Glauber param-
eters are immediately determined as in Sec. III A above.
TCM x(ns) and ν(ns) parameters are portable across all
A-B systems, although their details may vary.
C.
p-Pb ¯pt data and the Glauber model
The p-Pb ¯pt analysis described above has direct bear-
ing on the Glauber analysis of Ref. [17] through the TCM
relation of p-Pb centrality to observed nch in the form of
inferred relation Npart(¯ρ0) and hadron production in the
form of the mean number of hadrons per participant pair.
Figure 3 (left) shows data (points) in the form of
Eq. (4) (second line) and Fig. 2 (right panel) inverted
to solve for ν and thus Npart = 2/(2−ν) using ¯pts ≈0.4,
¯pthNN ≈1.3 GeV/c and x(ns) as deﬁned in Eq. (6). The
corresponding TCM is the solid curve. Glauber-assumed
linear scaling of Npart with nch is represented by the
dash-dotted curve. The Glauber analysis of Ref. [17] em-
phasizes a joint distribution on (¯ρ0, Npart) simulated by
a MC based on the same linear scaling. The TCM ¯pt
analysis deﬁnes a “locus of modes” deﬁned by the solid
curve Npart(¯ρ0)—the most-probable points on the space
(¯ρ0, Npart) or approximately the mean values on ¯ρ0 with
Npart ﬁxed or on Npart with ¯ρ0 ﬁxed.
0
1
2
3
4
5
6
7
8
9
0
50
100
nch / ∆η
Npart(ρ0)
p-Pb TCM
p-Pb data
Glauber
NSD
data
limit
0
5
10
15
20
25
30
35
0
50
100
nch / ∆η
(2/Npart) ρ0
NSD
Glauber
5 TeV p-Pb
p-p TCM
p-Pb TCM
data
limit
FIG. 3:
Left: Npart(¯ρ0) (points) inferred from ¯pt data in
Fig. 2 (right) via Eq. (4) (second line) and the curves in Fig. 1.
The corresponding TCM is the solid curve. Right: The TCM
trends for number of hadrons per participant pair inferred for
5 TeV p-Pb data (solid) and p-p data (dashed) compared to
the assumed relation for the Glauber study (dash-dotted).
Figure 3 (right) shows hadron production per partici-
pant pair in the form (2/Npart)¯ρ0 vs ¯ρ0 (solid curve) as


## Page 5


5
inferred from the p-Pb ¯pt analysis in Ref. [14]. The p-p
trend is the dashed line with Npart/2 ≡1. The hadron
production model for the Glauber analysis assumes that
this quantity remains close to the NSD p-p value ≈5
(dash-dotted). TCM and Glauber descriptions of p-Pb
centrality are thus likely to be very diﬀerent.
To provide context for what follows some limiting pa-
rameter values may be useful. The ¯pt data for 7 TeV p-p
collisions in Fig. 25 (left) extend to ¯ρ0pp ≈10 ¯ρ0NSD ≈
60.
The ¯pt data for 5 TeV p-Pb collisions extend to
(2/Npart)¯ρ0 ≈6 ¯ρ0NSD ≈30 as in Fig. 3 (right).
At
that upper limit Npart ≈7.5 as in Fig. 3 (left) com-
pared to Npart ≈16 for (2/Npart)¯ρ0 ≈5 inferred from
the Glauber MC as reported in Ref. [17] and Table I be-
low. If placed tangent along a Pb nucleus (r ≈7.1 fm)
diameter the number of nucleons (r ≈0.85 fm) would be
about 8. The mean number of N-N binary collisions per
participant in Au-Au or Pb-Pb collisions is ν < 6 [9].
IV.
GLAUBER MODEL OF p-Pb CENTRALITY
Reference [17] presents a Glauber centrality model for
5 TeV p-Pb collisions that may be compare with re-
sults from the TCM analysis of p-Pb ¯pt data summa-
rized above. Glauber parameters Npart, Nbin and b are
obtained from Table 2, and mean charge densities at
midrapidity in the form ¯ρ0 = nch/∆η are estimated from
Fig. 16 for seven centrality classes of p-Pb collisions. Pa-
rameter values are summarized in Table I of this article.
The particle data sample for Ref. [17] is the same 106 mil-
lion 5 TeV NSD p-Pb collisions reported in Ref. [16] as
described in Sec. III. Thus, the TCM obtained from p-Pb
¯pt analysis is directly applicable to the Glauber analysis.
A.
p-Pb Glauber analysis strategy
The Glauber model of A-B collision geometry is used to
relate fractional cross section σ/σ0 (σ0 is a measured to-
tal cross section) to collision geometry parameters such as
impact parameter b, participant-nucleon number Npart,
N-N binary-collision number Nbin and the derived colli-
sion number per participant pair ν ≡2Nbin/Npart. A
Monte Carlo simulation including geometric models of
the collision partners and relevant cross sections is used
to relate those quantities on a statistical basis [2]. “The
Glauber-MC determines on an event-by-event basis the
properties of the collision geometry, such as ...Npart...,”
and an event ensemble determines statistical parameter
mean values and probability distributions, e.g. P(Npart).
Some deﬁnition of a particle-production model denoted
by conditional probability P(nch|Npart) is an essential
requirement and must include an assumed nch vs Npart
trend. The model in Ref. [17] is a NBD with parameters
µ and k and the assumption that those parameters scale
linearly with Npart (e.g. nch ∝Npart). Convolution of
P(nch|Npart) with P(Npart) yields a distribution on some
observable nch: P(nch) = P
Npart P(nch|Npart)P(Npart).
Model P(nch|Npart) is “validated” by comparing the con-
volution integral to a measured P(nch) distribution. It
is concluded that ﬁtted “values of parameters µ and k
are similar to those obtained by ﬁtting the correspond-
ing multiplicity distributions in pp collisions at 7 TeV”
(but see Sec. VI B).
Once P(nch|Npart) has been so validated it is used to
determine mean Npart for a given nch (centrality) inter-
val: “The collision geometry is determined by ﬁtting the
measured [e.g. V0A P(nch) deﬁned below] distribution
with [the convolution integral]” referred to as a NBD-
Glauber ﬁt. The average Npart (or other Glauber param-
eter) value for each of several deﬁned event classes (based
on nch bins) are obtained: “For a given centrality class,
deﬁned by selections in the measured [e.g. V0A] distribu-
tion, the information from the Glauber MC in the corre-
sponding generated distribution [emphasis added] is used
to calculate the mean number of participants ⟨Npart⟩
[here simply denoted Npart]....”
An alternative proce-
dure based on running integrals is described below.
B.
p-Pb Glauber-model results
Figure 4 (left) shows Monte Carlo data obtained from
Fig. 3 (left, Std-Glauber) of Ref. [17] (open squares) rep-
resenting a Glauber simulation of 5 TeV p-Pb collisions.
A function describing the Monte Carlo data (curve) is
p(Npart) = 0.05 exp{−[(Npart −11.4)/6.4]2} (8)
q(Npart) = 0.84/N 1.75
part[1 + (Npart/9.3)10]
1
σ0
dσ
dNpart
= p(Npart) + q(Npart)
employed below for data description. Beyond its inﬂec-
tion point near 10 the distribution is Gaussian: p(Npart).
The left panel in Fig. 3 of Ref. [17] is labeled “Events (arb
units)” but is consistent with a unit-normal probability
distribution modeling the diﬀerential cross section. Tail
structure for Npart > 20 is not relevant to measurements.
If p-N cross section σpN represented all p-N encoun-
ters then for a minimum-bias 5 TeV p-Pb event ensem-
ble ¯Nbin ≡AσpN/σpA with measured σpA ≈2.1 b and
σpN = 70 ± 5 mb [17]. ¯Nbin = 208 × 70/2100 = 6.9 ± 0.5
compares to mean ¯Npart = ¯Nbin + 1 = 8.3 obtained from
the Glauber distribution in Fig. 4 (left). The MC value
is consistent with the measured cross sections within the
7% uncertainty in σpN, but the measured cross sections
were inputs to the Glauber MC.
Figure 4 (right) shows running integrals of data from
Ref. [17] (open squares) and Eq. (8) (solid curve) in the
left panel.
Both integrals go to unity asymptotically
without further normalization.
The horizontal dotted
lines are centrality bin edges deﬁned in Ref. [17]. The
vertical dotted lines are centrality bin edges on Npart de-
termined by the solid curve and horizontal dotted lines.
Centrality bin centers on Npart are denoted by the solid


## Page 6


6
10
-6
10
-5
10
-4
10
-3
10
-2
10
-1
1
0
10
20
30
Npart
(1/σ0) dσ / dNpart
0.050
0.067
5 TeV p-Pb Glauber
0
0.2
0.4
0.6
0.8
1
0
5
10
15
20
Npart
1 - σ / σ0
p-Pb Glauber
FIG. 4:
Left:
Monte Carlo data from Fig. 3 (left, Std
Glauber) of Ref. [17] (open squares) representing a Glauber
simulation of 5 TeV p-Pb collisions. A function describing the
data (curve) is given by Eq. (8). Right: Running integrals of
data from Ref. [17] (open squares) and Eq. (8) (solid curve)
in the left panel. The solid points are discussed in the text.
triangles, also on the solid curve, with values denoted
Npart (unprimed) in Table I. The solid dots, represent-
ing N ′
part entries in Table I obtained from Table 2 of
Ref. [17], deviate substantially from the running inte-
grals. Whereas the integrals are consistent with a value
0.050 at the inﬂection point in the left panel the solid
dots are consistent with a value 0.067 (slope of the dash-
dotted line through solid dots). The Glauber parameter
values from Ref. [17] thus appear to be inconsistent with
the basic Monte Carlo data.
For experimental determination of collision centralities
a Glauber simulation must be related to a measurable
quantity (e.g. a particle multiplicity), of which several
are considered in Ref. [17]. For this study results from
a VZERO-A or V0A scintillator detector covering accep-
tance 2.8 < η < 5.1 in the Pb hemisphere provide an
example. The signal amplitude from the V0A detector is
denoted here by nx (to distinguish from nch or ¯ρ0 relating
to midrapidity). The main issue is the relation between
simulated Npart and measured nx determined through
the intermediary of a diﬀerential cross section.
Figure 5 (left) shows normalized event-frequency
(probability) distribution P(nx) on V0A multiplicity nx
(points) for 5 TeV p-Pb collisions from Fig. 1 of Ref. [17].
A model function (curve) describing the V0A data is
A(nx) = 0.0075 + 0.0145{1 + tanh[(nx −225)/90]}/2
P(nx) =
1
N0
dNevt
dnx
= exp

−
Z nx
0
dn′
x A(n′
x) −4.67

(9)
which is accurate to a few percent. To establish a con-
nection between Npart and nx it is apparently assumed
in Ref. [17] that P(nx) →(1/σ0)dσ/dnx or dNevt ∝dσ –
centrality classes σ/σ0 are deﬁned by binning P(nx). For
comparison the dashed curve is the Glauber diﬀerential
cross section in Fig. 4 (left) transformed from Npart to nx
with a Jacobian derived from the curve in Fig. 7 (left).
Figure 5 (right) shows a running integral on nx of the
P(nx) expression in Eq. (9) with asymptotic limit 1.02.
10
-6
10
-5
10
-4
10
-3
10
-2
0
200
400
nx
VOA event frequency P(nx)
5 TeV p-Pb
Pb hemisphere
2.8 < η < 5.1
0
0.2
0.4
0.6
0.8
1
0
100
200
300
nx
running integral of P(nx)
FIG. 5:
Left: Normalized event-frequency distribution P(nx)
on V0A amplitude nx (points) for 5 TeV p-Pb collisions from
Fig. 1 of Ref. [17]. A function describing the data (curve) is
given by Eq. (9). Right: The running integral on nx of the
P(nx) expression in Eq. (9) with centrality bins (dotted).
The horizontal dotted lines are centrality bin edges and
the vertical dotted lines are the corresponding bin edges
on nx from Fig. 1 of Ref. [17]. Correspondence with the
running integral supports the assertion that P(nx) →
(1/σ0)dσ/dnx is assumed for the p-Pb Glauber analysis.
Table I summarizes some results of the p-Pb Glauber
analysis from Table 2 of Ref. [17] relating to the V0A
detector.
Primed quantities are found to be biased in
the present study. The primed Glauber parameters cor-
respond to the solid dots in Fig. 4 (right) whereas the
unprimed Npart values correspond to the triangles on the
solid curve. The ¯ρ′
0 = n′
ch/∆η values, obtained from bin
edges on V0A multiplicity nx, do not correspond to the
deﬁned centrality bins, as established in Sec. VI below.
TABLE I: V0A Glauber parameters for 5 TeV p-Pb collisions
are from Table 2 and ¯ρ′
0 = n′
ch/∆η densities are from Fig. 16
of Ref. [17]. Primes indicate biased entries as determined in
the present study. The event sample is approximately NSD.
centrality (%) b′ (fm) N ′
part N ′
bin n′
ch/∆η Npart
0 - 5
3.12
15.7
14.7
44.6
18.5
5 - 10
3.50
14.0
13.0
35.9
15.8
10 - 20
3.85
12.7
11.7
30.0
13.65
20 - 40
4.54
10.4
9.36
23.0
10.5
40 - 60
5.57
7.42
6.42
15.8
7.0
60 - 80
6.63
4.81
3.81
9.7
4.0
80 - 100
7.51
2.94
1.94
4.2
2.3
Based on the key assumption that Npart ∝nx the V0A
data in Fig. 5 (left) were ﬁtted with a convolution in-
tegral including the Glauber-model result as in Fig. 4
(left) described by Eq. (8) and a parametrized p-p (p-N)
negative binomial distribution (NBD) P(nx; µ, k), where
µ = ¯nx and µ/k is a ﬂuctuation measure. If V0A multi-
plicity nx is assumed proportional to Glauber Npart then
P(nx; µ, k) →P(nx; Npartµ, Npartk) and µ and k values
are determined by ﬁtting the V0A distribution.
Figure 6 (left) shows the p-p NBD on nx inferred from
the 5 TeV p-Pb V0A ﬁt (dashed curve) with (µ, k) =


## Page 7


7
(11.0, 0.44) from Table 1 of Ref. [17]. To provide a refer-
ence from p-p data the solid curve is a double-NBD direct
ﬁt to 7 TeV NSD p-p data (150 million events) on nch as
in Ref. [21]. The open circles represent a single-NBD ﬁt
to the solid curve with parameters (µ, k) = (6.0, 1.1) for
direct comparison with the V0A results.
10
-3
10
-2
10
-1
0
10
20
30
nx, nch / ∆η
P(n)
|η| < 0.5
7 TeV NSD p-p on nch
5 TeV p-Pb
on nx
0
0.05
0.1
0.15
0.2
0.25
0
5
10
15
20
nx, nch / ∆η
P(n)
7 TeV NSD p-p
5 TeV
p-Pb
NSD
FIG. 6:
Left: p-p NBD on nx inferred from a 5 TeV p-Pb
V0A ﬁt (dashed). The solid curve is a double-NBD direct ﬁt
to 7 TeV NSD p-p data as in Ref. [21]. The open points are
discussed in the text. Right: Those curves and data in linear
format with NSD means ≈5 for 5 TeV and ≈6 for 7 TeV.
Figure 6 (right) shows the same results on a linear plot-
ting format. The hatched band encompasses the mea-
sured NSD p-p values on nch for 5 and 7 TeV. The 7
TeV NSD mean is ¯ρ0NSD ≈6.17 in agreement with NBD
µ = 6 from Ref. [21]. The ﬁtted p-N NBD on nx is deter-
mined by combining the Glauber distribution on Npart
with the Npart ∝nx assumption. The NBD mean µ = 11
on nx is consistent with the 5 TeV NSD value ¯ρ0NSD ≈5
according to the curve in Fig. 7 (right) below. The shapes
of the two NBD distributions are very diﬀerent, but the
diﬀerence is explained in Sec. VI. What follows is a deter-
mination of the relations among Npart, nx and nch that
result from the Ref. [17] Glauber p-Pb analysis.
Figure 7 (left) shows the correspondence (points) be-
tween centrality bin edges on Npart and on nx from
Figs. 4 (right) and 5 (right). The solid curve is
Npart(nx) = (nx/4.2)1/1.4
(10)
except that Npart ≥2 is imposed as a constraint via
Npart →[Npart
4 + 24]1/4.
(11)
Those relations establish a correspondence Npart ↔nx.
Figure 7 (right) shows pairs of bin edges on nx vs cor-
responding midrapidity centrality-mean values of ¯ρ′
0 ≡
n′
ch/∆η for seven V0A centrality bins from Table I in-
ferred from Fig. 16 (lower left) of Ref. [17]. The solid
curve nx1 deﬁned by Eq. (12) (ﬁrst line) is determined to
pass between pairs of bin edges, closer to the lower edges
per the V0A distribution on nx.
Final values for the
two constants were established by accommodating data
0
50
100
150
200
250
300
0
5
10
15
20
Npart
nx
0
50
100
150
200
250
300
0
20
40
60
nch / ∆η
V0A bin edges on nx
nx1
nx2
5 TeV p-Pb
FIG. 7:
Left: Centrality bin edges on Npart and nx (points)
from Figs. 4 (right) and 5 (right) that relate nx to Npart. The
solid curve is derived from Eqs. (10) and (11). Right: pairs of
bin edges on nx vs corresponding midrapidity centrality-mean
values of ¯ρ′
0 ≡n′
ch/∆η (solid points) for seven V0A centrality
bins. The dash-dotted and dotted curves are Eqs. (12). The
open circles are explained in the text.
in Fig. 8 (left, open circles) for a self-consistent system.
nx1(¯ρ0) =
Z ¯ρ0
0
d¯ρ′
0 6.8 tanh(¯ρ′
0/10)
(12)
nx2(¯ρ0) =
Z ¯ρ0
0
d¯ρ′
0 5.4 tanh(¯ρ′
0/12)
Equation (12) (second line) deﬁnes the dotted curve nx2
in the right panel and is derived by matching bin edges
from P(nx) in Fig. 5 (left) with bin edges from P(nch)
obtained from ¯pt data in Ref. [16] and appearing in
Fig. 13.
Since the same event ensemble is distributed
on nx and nch that is an apples-to-apples comparison.
Equations (12) establish correspondence nx ↔nch while
Eq. (10) establishes correspondence Npart ↔nx.
The
two relations can be combined to determine Npart ↔nch.
Figure 8 (left) shows ¯ρ′
0 = n′
ch/∆η vs N ′
part from Ta-
ble I (solid dots). The open circles represent the same ¯ρ′
0
values vs corrected Npart values from Fig. 4 (right) corre-
sponding to the solid triangles. The dash-dotted and dot-
ted curves are Eqs. (10), (11) and (12) combined to yield
¯ρ′
0(Npart). The prime indicates that the charge density
does not in fact correspond to the model Npart values ob-
tained from the p-Pb Glauber analysis, as demonstrated
below. The dashed curve is ¯ρ′
0 ≈(Npart/2)4.5 per the
assumption of proportionality in Ref. [17].
Figure 8 (right) shows Jacobians dNpart/d¯ρ0 for den-
sity transformations from one variable to the other. The
relation ¯ρ0 ≈¯ρ0NSDNpart/2 is indicated by the hatched
band for 5 TeV p-p and p-Pb collisions with ¯ρ0NSD ≈5.
The dash-dotted, dotted and dashed curves are derived
from corresponding curves in the left panel inferred from
the Glauber analysis. The Jacobians test the initial as-
sumption(s) of Ref. [17] that nch is linearly related to,
proportional to or “scales with” Npart, in which case the
Jacobian dNpart/d¯ρ0 should be approximately constant.
Interpreting the V0A probability distribution P(nx) as
a diﬀerential cross-section distribution deﬁnes p-Pb cen-
trality in terms of observable nx and the Glauber model


## Page 8


8
0
5
10
15
20
25
30
35
40
45
50
0
5
10
15
20
Npart
nch / ∆η
p-Pb Glauber
nx2
nx1
NSD
5 TeV
0
0.1
0.2
0.3
0.4
0.5
0.6
0
5
10
15
20
Npart
dNpart / dρ0
NSD
nx1
nx2
5 TeV p-Pb
FIG. 8:
Left: Relations between Glauber predicted Npart
and measured ¯ρ0 from Table I (solid and open points). The
curves are explained in the text. Right: Jacobians relating
Npart to ¯ρ0 derived from curves in the left panel.
of p-A geometry, e.g. parameters Npart and b. The cen-
trality bins on nx then deﬁne bin-averaged ¯ρ0 values at
midrapidity.
The combination of a Glauber model for
p-Pb centrality and a p-N NBD distribution with an as-
sumption of proportionality between Npart and nx leads
to inference of a p-p NBD on nx. The combination sug-
gests approximate proportionality between Npart and ¯ρ0,
seeming to close the circle. In the next section results of
the p-Pb Glauber analysis of Ref. [17] are compared to
geometry information inferred from ¯pt data in Ref. [14]
derived from the same underlying particle data.
V.
p-Pb GLAUBER MODEL vs ¯pt TCM
An analysis of ¯pt data for p-p, p-Pb and Pb-Pb colli-
sions for several LHC energies was reported in Ref. [14],
and pertinent details are reviewed in App. B and Sec.
III. A TCM for ¯pt data from each collision system relates
charge multiplicity to system centrality (where relevant)
via manifestations of MB dijet production. In this section
the p-Pb TCM ¯pt results are compared to the Glauber-
model description of p-Pb data. The principal issue is
apparent contradictions between the Npart(¯ρ0) trend in-
ferred from the ¯pt TCM and from the Glauber model of
p-Pb centrality.
Figure 9 (left) shows the p-Pb Glauber-model num-
ber of participants Npart vs charge density ¯ρ′
0 = n′
ch/∆η
(points) from Table I. Solid and open points represent
N ′
part and Npart respectively. The dash-dotted (nx1) and
dotted (nx2) curves are obtained from Eqs. (10), (11)
and (12). The dashed curve represents the assumption
that “the number of participants is proportional to the
number of charged hadrons,” e.g. nch ≈nchNSDNpart/2
[except Npart ≥2 per Eq. (11)]. The solid curve is from
the p-Pb TCM [14]. The large diﬀerence is apparent.
Figure 9 (right) shows (2/Npart)¯ρ0 obtained from Ta-
ble I entries (solid dots, N ′
part) and using corrected Npart
(open circles).
The corresponding TCM p-Pb trend is
the solid curve, and the dash-dotted and dotted curves
are obtained from the equivalent in the left panel. The
0
2
4
6
8
10
12
14
16
18
20
0
20
40
60
nch / ∆η
Npart
NSD
nx1
nx2
TCM
Glauber
NSD
0
2.5
5
7.5
10
12.5
15
17.5
20
22.5
25
0
20
40
60
nch / ∆η
(2/Npart) ρ0
NSD
NSD
nx2
5 TeV
p-Pb TCM
p-p TCM
p-Pb Glauber
FIG. 9:
Left:
Comparison of Npart(¯ρ0) trends from the
Glauber study in Ref. [17] (points and three curves) and the
p-Pb ¯pt TCM (solid) from Ref. [14]. Right: Hadron produc-
tion per participant pair: trends from the Glauber study in
Ref. [17] (points and three lower curves), from the p-Pb ¯pt
TCM (solid) and from the p-p TCM (dashed).
dashed curve is (2/Npart)¯ρ0 = 4.4 but with the constraint
Npart ≥2 imposed per Eq. (11). The hatched band is
¯ρ0NSD ≈5 corresponding to 5 TeV p-p collisions [15],
consistent with the basic Glauber assumption for p-Pb
analysis that ensemble-averaged N-N collisions are the
same as p-p NSD for all p-Pb centrality conditions and
increasing nch must be due entirely to increasing Npart.
Figure 10 (left) shows Nbin vs ¯ρ0 with Nbin ≡Npart−1
for p-A collisions. It is notable that the Glauber estimate
Nbin ≈2 applies to a centrality range where p-Pb is dom-
inated by p-N. Figure 10 (right) shows ν ≡2Nbin/Npart
obtained from Table I values (solid dots, N ′
part, N ′
bin) and
from corrected Npart (open circles) compared to the p-Pb
TCM (solid curve). The ν trend for Pb-Pb (dashed) is
included for comparison. It is notable that ν for p-Pb
from Ref. [17] exceeds that for Pb-Pb up to ¯ρ0 ≈50
whereas the p-Pb TCM parameter values near ¯ρ0 ≈40
are Npart ≈4, Nbin ≈3 and ν ≈1.5.
In that case
(2/Npart) ¯ρ0 ≈4.5¯ρ0NSD implies approximately 20-fold
increase in dijet production according to Ref. [7].
0
2
4
6
8
10
12
14
16
18
20
0
20
40
60
nch / ∆η
Nbin
p-Pb TCM
p-Pb Glauber
NSD
1
1.2
1.4
1.6
1.8
2
0
20
40
60
nch / ∆η
ν
p-Pb TCM
NSD
Pb-Pb
FIG. 10:
Left: Nbin vs ¯ρ0 with Nbin ≡Npart −1 for p-A
collisions. Right: ν ≡2Nbin/Npart obtained from Table I val-
ues (solid dots, N ′
part, N ′
bin) and from corrected Npart (open
circles) compared to the p-Pb TCM (solid curve).
Figure 11 (left) shows Glauber-model p-Pb centrality
vs ¯ρ0 from Ref. [17] where “centrality” is here measured


## Page 9


9
by impact-parameter ratio b/b0 (open squares) assuming
that centralities in percent in Table I represent 100σ/σ0
with σ/σ0 ≈(b/b0)2. The solid dots are obtained from
the p-Pb Glauber b estimates in Table I assuming b0 ≈8
fm (based on radii 7.1 fm and 0.85 fm for Pb and p).
The dash-dotted curve is derived from fractional cross
section 1 −σ/σ0 shown as the Glauber running integral
(dash-dotted curve) in Fig. 15 (left) below. The Glauber
analysis suggests that fully-central p-Pb collisions corre-
spond to ¯ρ0 ≈60, whereas ¯pt data from Ref. [16] extend
out to ¯ρ0 ≈115 (hatched band).
0
0.2
0.4
0.6
0.8
1
0
50
100
nch / ∆η
1 - b/b0
5 TeV p-Pb
Glauber
p-Pb
data
limit
0.45
0.5
0.55
0.6
0.65
0.7
0.75
0.8
0.85
0
50
100
nch / ∆η
¯p t ′ (GeV/c)
5 TeV p-Pb
¯pts ′
NSD
NSD
p-Pb Glauber
MC
FIG. 11:
Left: Glauber-model p-Pb centrality vs ¯ρ0 from
Ref. [17] measured by impact-parameter ratio b/b0 (open
squares) assuming that centralities in percent in Table I rep-
resent 100σ/σ0 and σ/σ0 ≈(b/b0)2.
The solid points are
from Table I. Right:
Uncorrected ensemble-mean pt or ¯p′
t
vs corrected ¯ρ0 = nch/∆η for 5 TeV p-Pb collisions from
Ref. [16] (open squares). The solid curve is the p-Pb TCM.
The solid points are predictions derived from the Glauber cen-
trality analysis in Ref. [17]. The Glauber MC curve (dotted)
is taken from Fig. 3 of Ref. [16]. The dotted line shows the
¯p′
t estimate for NSD p-p collisions and all else the same.
Figure 11 (right) shows uncorrected ensemble-mean ¯p′
t
vs corrected ¯ρ0 = nch/∆η data for 5 TeV p-Pb colli-
sions from Ref. [16] (open squares). The solid curve is
the corresponding TCM from Ref [14]. The solid points
and dash-dotted curve are ¯pt estimates based on results
from the p-Pb Glauber analysis of Ref. [17] using data
from Table I and Eq. (4) (ﬁrst line) repeated here for
convenience
¯p′
t ≈
¯pts + x(ns)ν(ns) ¯pthNN(ns)
ξ + x(ns) ν(ns)
.
(13)
Consistent with the p-Pb Glauber analysis x(ns) ≈
αρsNN up to ¯ρsNSD and then remains constant at the
NSD value ≈0.06. ν(ns) is described by the dash-dotted
curve in Fig. 10 (right) and ¯pthNN →¯pth0 = 1.3 GeV/c
with ¯pts ≈0.4 and ξ ≈0.73.
Those trends are con-
sistent with the assumption that average N-N collisions
for any p-Pb centrality should be equivalent to NSD p-p
collisions.
If that assumption were correct there is no
possibility to match the published p-Pb ¯pt data.
Ac-
cording to the Glauber analysis p-Pb data cannot ex-
tend beyond ¯ρ0 ≈55 (hatched band), yet the dotted
“Glauber MC” curve from Fig. 3 of Ref. [16] extends out
to ¯ρ0 ≈70/0.6 ≈115. The MC vertical displacement
from the other curves at small nch is equivalent to a 5%
change in the ineﬃciency parameter ξ in Eq. (13).
To summarize, Glauber-model results from Ref. [17]
appear to be inconsistent with ¯pt data from Ref. [16],
both from the same collaboration. There are three ma-
jor issues: (a) The Npart(¯ρ0) trend inferred from ¯pt data
via the TCM analysis of Ref. [14] is dramatically dif-
ferent from that assumed for the Glauber analysis. (b)
The Glauber model suggests that most-central p-Pb col-
lisions correspond to ¯ρ0 < 55 whereas ¯pt data extend to
¯ρ0 ≈115. (c) The ¯pt trend predicted by the Glauber
analysis is very diﬀerent from measurements in Ref. [16]
and described by the TCM in Ref. [14]. In the next sec-
tion possible sources of major diﬀerences are explored.
VI.
p-Pb GLAUBER-MODEL DISCUSSION
A description of centrality in A-B collisions includes
several elements: (a) measured total cross section σ0 =
πb2
0 distributed as diﬀerential cross section dσ = πdb2
manifesting as event frequency distributions on certain
parameters; (b) A-B collision geometry measured by sev-
eral internal geometry parameters, e.g. Npart; and (c)
external or observable quantities that depend on hadron
production, e.g. nch. One then relates nch to Npart via
(σ, b). Several questions arise: (a) which nucleons in A
and B are participants by what criteria, (b) what hadron
production mechanism(s) apply, (c) is dσ ∝dNevt valid.
Reference [17] relates Npart to (σ, b) via a geometric
Glauber MC, and dσ ∝dNevt on nch is assumed. The
combination of Npart ↔σ and σ ↔nch then closes the
circle with an inferred relation between Npart and nch.
A.
Npart vs nch scaling assumptions
A central element of the p-Pb Glauber analysis of
Ref. [17] is the assumed relation between Glauber Npart
and an observable quantity such as particle multiplicity
within some η acceptance, denoted by nx for simplicity.
The abstract includes “Under the assumption that the
multiplicity measured in the Pb-going rapidity region [i.e.
V0A nx] scales with the number of Pb-participants, an
approximate independence of the multiplicity per partic-
ipating nucleon measured at midrapitity [sic] of the num-
ber of participating nucleons is observed.” The summary
includes “In particular, we assume that the multiplicity
at mid-rapidity is proportional to Npart.... We ﬁnd... ii)
that the multiplicity of charged particles at mid-rapidity
scales linearly with the total number of participants....”
Similar statements appear elsewhere in the text.
Arguments for proportionality or “scaling” between
Npart and nch based in part on the wounded-nucleon
model of hadron production [22] rely on ﬁxed-target re-
sults at lower collision energies [23] or early data from
RHIC (with large systematic uncertainties and limited


## Page 10


10
centrality range) [24]. A description of Au-Au particle
production vs centrality (PHOBOS) includes the state-
ment “However, within the systematic errors, the total
[i.e. 4π] yield per participant pair is approximately con-
stant (within 10%) over the measured centrality range,
65 < Npart < 358, which corresponds to 3 < ¯ν < 6,
where ¯ν is the average number of collisions undergone
by each oncoming nucleon. [That interval includes only
the most-central 40% of the total cross section.] Thus,
it appears that only the ﬁrst few collisions have any ap-
preciable eﬀect on particle production...” [25]. The state-
ment cautions however “It should be noted that this sim-
ple scaling is not observed for [diﬀerential] particle yields
measured in a limited pseudorapidity range near midra-
pidity” [25]. The same collaboration further states that
“...in d + Au collisions the total multiplicity of charged
particles scales linearly with the total number of partici-
pants...” [26]. But that conclusion depends critically on
how Npart is estimated. If the Npart estimate is based
on assumed proportionality (as in Ref. [17]) the quoted
conclusion is trivial and the argument likely misleading.
B.
Alternative TCM p-Pb centrality analysis
As an alternative to the Glauber analysis of Ref. [17]
the following strategy is adopted. The TCM relation be-
tween Npart and ¯ρ0 near η = 0 inferred from ¯pt data
in Ref. [14] as in Fig. 9 (left, solid curve) is adopted as
the starting point. A frequency distribution P(nch) on
¯ρ0 near midrapidity is derived from ¯pt data reported in
Ref. [16]. A cross-section distribution on Npart is then
constructed by assuming that the geometric Glauber dis-
tribution in Fig. 4 (left) may be a good approximation for
peripheral collisions only and that P(nch) inferred from
¯pt data is determining for more-central collisions.
Figure 12 (left) shows Npart vs ¯ρ0 for the Glauber anal-
ysis of Ref. [17] (dash-dotted and dotted), for ideal Npart
scaling (dashed) and for the p-Pb ¯pt TCM (solid). The
solid TCM curve is the starting point for this alterna-
tive analysis. Whereas the Glauber trends are consistent
with numerous participants and smaller p-N multiplici-
ties the TCM trend is consistent with fewer participants
and larger p-N multiplicities.
Figure 12 (right) shows Jacobians dNpart/d¯ρ0 derived
from curves in the left panel. Note that Glauber curves
are scaled down by 1/5. The obvious large disagreement
between TCM Jacobian and Glauber versions is a cen-
tral issue for the present study: Assumption of Npart
“scaling” with some nx would result in a nearly constant
Jacobian proceeding from NSD nch, which is quite incon-
sistent with ¯pt data [14] and MB dijet results [27].
The Jacobians in Figs. 12 (right) and 16 (right) can
be used to transform probability distributions and dif-
ferential cross sections on Npart or nx to common pa-
rameter nch or ¯ρ0.
Note that for an eﬀective maxi-
mum value Npart ≈20 from the diﬀerential cross section
in Fig. 4 the corresponding maximum charge density is
0
2.5
5
7.5
10
12.5
15
17.5
20
0
50
100
nch / ∆η
Npart
TCM
Glauber
NSD
0
0.02
0.04
0.06
0.08
0.1
0
20
40
60
80
100
nch / ∆η
dNpart / dρ0
TCM
Glauber/5
NSD/5
FIG. 12:
Left:
Npart vs ¯ρ0 for the Glauber analysis of
Ref. [17] (dash-dotted and dotted), for ideal Npart scaling
(dashed) and for the p-Pb ¯pt TCM (solid). Right: Jacobians
dNpart/d¯ρ0 derived from the left panel. An upper limit on at-
tainable ¯ρ0 implied by the Glauber analysis is denoted by the
vertical hatched band. Glauber values are reduced by factor
1/5.
¯ρ0 ≈20/0.4 = 50 as indicated by the vertical hatched
band in the right panel. The TCM value of Npart for
¯ρ0 = 115 is just less than 8 as indicated in the left panel.
Reference [17] does not provide an event frequency dis-
tribution on charge density ¯ρ0 near midrapidity that can
relate directly to Fig. 12, but such a distribution can
be derived from ¯pt data in Ref. [16]. Assume δ¯pt/¯pt ≈
δNch/Nch ≈1/√∆η¯ρ0Nevt for Poisson statistics, where
Nch is a multiplicity-bin total charge integrated over all
events and within acceptance ∆η = 0.6. Given reported
statistical errors δ¯pt on ¯pt data vs ¯ρ0 solve for Nevt(nch)
to obtain event-frequency distribution P(nch) for η = 0.
Figure 13 (left) compares several curves of diﬀering ori-
gins (within the same plot context) obtained by transfor-
mations with relevant Jacobians. The dash-dotted curve
is the Glauber MC diﬀerential cross-section on Npart in
Fig. 4 (left) transformed with the dash-dotted Jacobian
in Fig. 12 (right) and is then nominally (1/σ0)dσ/d¯ρ0, a
diﬀerential cross-section distribution on ¯ρ0. The dashed
curve is the V0A distribution P(nx) in Fig. 5 transformed
with the dashed Jacobian in Fig. 16 (right) to obtain a
normalized event distribution on ¯ρ0. The open squares
represent the normalized event distribution P(nch) de-
rived from ¯pt statistical errors δ¯pt reported in Ref. [16]
as described above. The solid curve is an inferred TCM
diﬀerential cross section.
Figure 13 (right) shows the same results in a semilog
format. The TCM solid curves are derived as follows:
The geometric Glauber MC cross-section distribution
(1/σ0)dσ/dNpart in Fig. 4 (left) is assumed as a start-
ing point, applying at least to peripheral p-Pb collisions.
The TCM Jacobian dNpart/d¯ρ0 in Fig. 12 (right, solid)
is used to transform to (1/σ0)dσ/d¯ρ0 which then greatly
overshoots the mid-rapidity P(nch) (open squares) at
larger ¯ρ0 in the right panel.
A function is applied to
Glauber (1/σ0)dσ/dNpart in Fig. 4 (left) such that the
transformed distribution on ¯ρ0 follows the form of P(nch)
at larger ¯ρ0 (see Sec. VI D). The result is the TCM solid


## Page 11


11
0
0.01
0.02
0.03
0.04
0.05
0.06
0
20
40
60
nch / ∆η
P(nch),  (1/σ0) dσ / dρ0
P(nch)
Glauber
V0A
TCM
5 TeV p-Pb
NSD
10
-5
10
-4
10
-3
10
-2
0
50
100
nch / ∆η
P(nch),  (1/σ0) dσ / dρ0
Glauber
V0A
P(nch)
5 TeV p-Pb
TCM
FIG. 13:
Left: Comparison of diﬀerential cross sections and
probabilities obtained by transformations with relevant Jaco-
bians and plotted within the same context. Right: The same
curves in a semilog format. Curves are described in the text.
curves in the two panels. The applied function is
f = exp{−[(|Npart −3| + Npart −3)/2]2/3}. (14)
The dash-dotted Glauber curve drops oﬀrapidly at larger
nch whereas from Sec. VI D close correspondence with
dashed V0A P(nch) is expected, similar to the relation
between the TCM solid curve and P(nch) open boxes.
Figure 14 (left) repeats Fig. 4 (left) now including the
TCM cross-section distribution on Npart (solid) as mod-
iﬁed by Eq. (14). Transformation of that curve with the
Jacobian in Fig. 12 (right, solid) gives the TCM solid
curves in Fig. 13, suggesting that the true maximum par-
ticipant number in central p-Pb collisions is about 8.
10
-5
10
-4
10
-3
10
-2
10
-1
1
0
5
10
15
20
25
Npart
(1/σ0) dσ / dNpart
TCM
5 TeV p-Pb
Glauber
0
0.2
0.4
0.6
0.8
1
0
5
10
15
20
25
Npart
1 - b / b0
Glauber
TCM
FIG. 14:
Left: Diﬀerential cross sections on Npart derived
from the geometric Glauber MC (dash-dotted) and as modi-
ﬁed with Eq. (14) as a factor to represent the TCM (dashed).
Right: Running integrals 1 −σ/σ0 of curves on the left con-
verted to 1 −(b/b0 =
p
σ/σ0).
Figure 14 (right) shows running integrals of the diﬀer-
ential distributions in the left panel transformed to frac-
tional impact parameter b/b0 =
p
σ/σ0. Whereas the
Glauber trend (dash-dotted) extends out to Npart ≈24
the TCM trend (dashed), consistent with ¯pt data, ex-
tends to less than 8 (or Nbin < 7). For central Pb-Pb or
Au-Au collisions the mean Nbin per participant nucleon
(i.e. in each projectile nucleus) is ν < 6 [9].
Figure 15 (left) shows running integrals of dσ/d¯ρ0 and
P(nch) distributions in Fig. 13 with corresponding line
styles. The dashed V0A and dash-dotted Glauber MC
trends contrast with the TCM trend (solid). Diﬀerences
among V0A, Glauber, P(nch) and TCM distributions
are discussed further in Sec. VI D. The horizontal dot-
ted lines are centrality values deﬁned in Ref. [17]. The
solid dots are Glauber ¯ρ′
0 data from Table I consistent
with Glauber and V0A curves, although there are sub-
stantial diﬀerences between the two diﬀerential curves in
Fig. 13 (left). The triangles are corresponding TCM ¯ρ0
values lying on the solid curve. The TCM centrality bin
centers are systematically shifted to larger ¯ρ0.
0
0.2
0.4
0.6
0.8
1
0
20
40
60
nch / ∆η
1 − σ/σ0
NSD
TCM
VOA
5 TeV p-Pb
P(nch)
0
0.2
0.4
0.6
0.8
1
0
50
100
nch / ∆η
1 - b/b0
5 TeV p-Pb
TCM
Glauber
p-Pb data limit
FIG. 15:
Left: Running integrals of dσ/d¯ρ0 and P(nch)
distributions in Fig. 13 with corresponding line styles. Solid
points are from Table I. Solid triangles are explained in the
text. Right: Impact-parameter b/b0 =
p
σ/σ0 trends on ¯ρ0
illustrating extension of TCM centrality variation out to the
limits of ¯pt data from Ref. [14] (hatched band).
Figure 15 (right) shows impact-parameter b/b0 trends
on ¯ρ0. Whereas the Glauber cross section is already fully
integrated on nch (b/b0 →0) near ¯ρ0 = 60 the TCM
centrality trend attains its b/b0 →0 limit only near ¯ρ0 =
115 (the upper limit for ¯pt data from Ref. [16]).
Figure 15 demonstrates that TCM p-Pb centrality
solves two problems arising from the Glauber analysis:
(a) In an interval about ¯ρ0 ≈¯ρ0NSD where p-Pb ≈p-N,
1 −σ/σ0 ≈0 should persist as indicated by the TCM
trend in the left panel, but the Glauber equivalent rises
rapidly. (b) Signiﬁcant centrality variation should extend
out to ¯ρ0 ≈115 consistent with ¯pt data from Ref. [16],
as indicated by the TCM b/b0 trend in the right panel,
whereas the Glauber trend terminates near 60.
The structure of the p-N P(nch) distribution within
p-Pb collisions is critical for understanding p-Pb central-
ity. In the Glauber study of Ref. [17] NBD parameters
(µ, k) were inferred by ﬁtting a convolution integral to
the V0A Nevt distribution on nx P(nx). Using the ap-
propriate Jacobian that distribution can be transformed
to nch for direct comparison with measured p-p data.
Figure 16 (left) repeats p-p multiplicity distributions
shown in Fig. 6 (left) above. The solid curve is a double-
NBD on mid-rapidity nch ﬁtted to 7 TeV p-p data with
accuracy at the percent level [28]. The value µ = 6 is
consistent with the NSD ¯ρ0 value for 7 TeV. The dashed
curve is the single NBD on nx resulting from Glauber
analysis of 5 TeV p-Pb V0A data described in Sec. IV B,


## Page 12


12
with parameters (µ, k) = (11, 0.44). The two distribu-
tions as plotted are very diﬀerent, although Ref. [17]
concludes that “The values of the parameters µ and k
are similar to those obtained by ﬁtting the correspond-
ing multiplicity distributions in pp collisions at 7 TeV”
(text quoted in Sec. VI B above).
But that statement
contradicts the numbers above. Proper comparison re-
quires transformation of the ﬁtted density on nx to a
density on midrapidity ¯ρ0 with the correct Jacobian.
10
-3
10
-2
10
-1
0
10
20
nch / ∆η
P(nch)
7 TeV p-p
5 TeV p-Pb
Glauber
0.9
2.76
on nx
on nch
0
1
2
3
4
5
6
7
0
10
20
30
40
50
nch / ∆η
dnx / dρ0
nx1
nx2
FIG. 16:
Left: p-p multiplicity distributions shown in Fig. 6
(left) above. The dash-dotted curve on nch is the V0A curve
on nx (dashed) transformed with the Jacobian labeled nx1 in
the right panel. Right: Jacobians derived from Eqs. (12).
Figure 16 (right) shows Jacobians dnx/d¯ρ0 obtained
from Eqs. (12).
The bold dash-dotted curve on ¯ρ0 in
the left panel results from transforming the dashed curve
on nx with the nx1 Jacobian in the right panel.
The
transformed NBD is qualitatively similar to the 7 TeV p-p
solid curve, and a comparison is now legitimate. The bold
curve terminates at ¯ρ0 ≈10 (nx ≈30) due to limitations
in a routine to compute gamma functions. The thinner
dash-dotted curve is a single NBD on ¯ρ0 ﬁtted to the bold
curve with parameters (µ, k) = (5, 2). The value µ = 5
is consistent with NSD ¯ρ0 ≈5 for 5 TeV p-p collisions.
The important diﬀerence lies with the k values. Mul-
tiplicity ﬂuctuations can be measured by relative vari-
ance excess (compared to Poisson) σ2
n/¯n −1 = µ/k for
an NBD distribution.
Detailed measurements at LHC
energies [28] reveal that p-p collisions exhibit large nch
variations. Charge densities ¯ρ0 →10 ¯ρ0NSD ≈60 were
reported in Ref. [28]. The 7 TeV NBD describing data
has µ/k ≈6/1.1 = 5.5 whereas the NBD inferred from
the Glauber analysis has µ/k ≈5/2 = 2.5, a factor 2.3
smaller although the collision energies are close.
The
large diﬀerence is manifested in the tails of the distri-
butions: the Glauber ﬁt is an order of magnitude lower
than the measured p-p NBD tail near ¯ρ0 = 25 (a region
quite relevant to the p-Pb analysis). The nx2 Jacobian
would result in greater reduction. The assumptions in
Ref. [17] noted in Sec. VI A are equivalent to assuming
that average N-N encounters for any p-Pb nch condition
are equivalent to the p-p NSD mean.
A consequence of that assumption is inference of a
p-N multiplicity distribution [from the ﬁt to V0A P(nx)]
with suppressed large-nch tail sharply deviating from p-p
data. Double-NBD curves (dotted) ﬁtted to 0.9 TeV and
2.76 TeV p-p data [28] are shown for comparison. The
Glauber-inferred NBD for 5 TeV p-Pb collisions is simi-
lar at larger ¯ρ0 to a NBD for p-p collisions near 1 TeV.
The suppressed tail on p-N P(nx) is a consequence of
overestimating the p-Pb large-Npart tail in Fig. 14 (left).
C.
Joint probability distribution P(nch, Npart)
The diﬀerences between Glauber and TCM analy-
ses and proposed mechanisms can be further explored
by plotting joint probability distributions (normalized
event-frequency distributions) P(Npart, ¯ρ0) factorized as
P(Npart, ¯ρ0NN) = P(¯ρ0NN|Npart)(1/σ0)dσ/dNpart(15)
with ¯ρ0NN = (2/Npart)¯ρ0.
To simplify the exercise it
is assumed that P(¯ρ0NN|Npart) ≈P(¯ρ0) is described by
Glauber-inferred (dash-dotted) or p-p-data (solid) curves
on ¯ρ0 in Fig. 16 (left) and (1/σ0)dσ/dNpart is described
by Glauber or TCM curves on Npart in Fig. 14 (left).
Figure 17 (left) shows joint probability distribution
P(Npart, ¯ρ0NN) representing the Glauber analysis. The
z axis is logarithmic over interval (10−8,0.1). The dashed
curves are constraint loci deﬁned by ¯ρ0 = ¯ρ0NNNpart/2
with ¯ρ0 increasing in integral multiples of ¯ρ0NSD from
5 to 45.
The right-most dashed curve corresponds to
¯ρ0 = 115, the limiting value for the ¯pt analysis reported
in Ref. [16] and appearing in Figs. 2 and 11 (right). The
solid curve is the TCM curve in Fig. 9 (right) plotted
on Npart rather than ¯ρ0. The dash-dotted curve for the
Glauber analysis has the same relation to Fig. 9 (right).
The solid (TCM) and dash-dotted (Glauber) curves
predict the most probable values or locus of modes (ap-
proximately the mean values) of ﬂuctuating ¯ρ0NN and
Npart given the “centrality” constraint ¯ρ0 on the p-Pb
collision system. Up to ¯ρ0 ≈10 the actual locus appears
to follow the most-probable point for each dashed curve,
which corresponds to Npart ≈2. Beyond that point it
could be argued that probability values at larger Npart
and smaller ¯ρ0NN (the Glauber locus) may be greater.
Figure 17 (right) shows P(¯ρ0NN, Npart) constructed
with TCM versions of P(¯ρ0) and dσ/dNpart. The z axis
is logarithmic over the same interval as the left panel.
The dramatic diﬀerence from the left panel is apparent
and the Glauber locus is rejected here. The TCM locus,
inferred from ¯pt data as in Ref. [14], follows the most
probable points up to large ρ0 and intercepts the curve
for ¯ρ0 = 115 at Npart ≈7.5 and ¯ρ0NN ≈32. Note that
p-p data for P(nch) in Ref. [28] extend out to ¯ρ0NN ≈60
with Npart ≡2. The large range of the TCM joint distri-
bution on ¯ρ0NN is thus consistent with p-p data, whereas
the much smaller range in the left panel is a direct con-
sequence of the broad distribution on Npart required by
the geometric Glauber MC. p-Pb ¯pt data and p-p multi-
plicity distributions thus provide compelling evidence to
support the alternative TCM-based centrality analysis.


## Page 13


13
0
5
10
15
20
25
30
5
10
15
20
Npart
nchNN / ∆η
0
5
10
15
20
25
30
5
10
15
20
Npart
nchNN / ∆η
FIG. 17:
(Color online) Left: Joint probability distribution
P(Npart, ¯ρ0NN) representing the Glauber analysis of Ref. [17].
The z axis is logarithmic over interval (10−8,0.1).
Right:
P(¯ρ0NN, Npart) constructed with TCM versions of P(¯ρ0) and
dσ/dNpart. The z axis is logarithmic over the same interval
as the left panel.
D.
dσ vs dNevt and Laplace’s approximation
The distributions in Fig. 13 are in principle not com-
patible within the same format.
Normalized event-
frequency distributions P(nch) →P(¯ρ0) (e.g. dashed
curve, open squares) should be distinguished from dif-
ferential cross sections (1/σ0)dσ/d¯ρ0 (dash-dotted and
solid curves). The diﬀerence requires distinction between
event frequency Nevt and centrality-related cross section
σ: proportionality dσ ∝dNevt is not generally valid.
In Fig. 14 (left) cross section σ(Npart) depends solely
on Npart. Its relation to observed density ¯ρ0 results only
indirectly from the relation Npart(¯ρ0) describing the locus
of modes for the Nevt density on the space (Npart, ¯ρ0).
The cross section is simply transformed to a density on
¯ρ0 with a Jacobian (in Fig. 12, right, solid curve) as
dσ
d¯ρ0
= dNpart
d¯ρ0
dσ
dNpart
(16)
which gives the solid curves in Fig. 13. With nch ﬁxed
or integrated the relation dσ ∝dNevt is valid on Npart.
In contrast, Nevt(Npart, ¯ρ0) is a function of (at least)
two variables.
The Nevt marginal density P(¯ρ0) =
(1/N0)dNevt/d¯ρ0 is given by the convolution integral
P(¯ρ0) =
Z
dNpartP(¯ρ0|Npart)P(Npart),
(17)
where P(Npart) ≡(1/σ0)dσ/dNpart. Equation (17) has
the same structure as evidence E in Bayesian inference
deﬁned by the ﬁrst line of Eq. (5) in Ref. [29]. The second
line of Eq. (5) introduces Laplace’s approximation and
may be reformulated in the present context as
P(¯ρ0) ≈
Z ¯ρ0
0
d¯ρ′
0P(¯ρ′
0| ˜Npart)
dNpart
d¯ρ0
P(Npart)

˜
Npart
(18)
where P(¯ρ′
0| ˜Npart) is equivalent to the Bayesian likeli-
hood, and the quantity in square brackets is the diﬀer-
ential cross section on ¯ρ0 evaluated at ˜Npart(¯ρ0) on the
locus of modes for a given ¯ρ0.
The ﬁrst factor is ef-
fectively a running integral of hadron production model
P(¯ρ0|Npart) which distinguishes the form of dNevt/d¯ρ0
from the form of dσ/d¯ρ0, why dNevt ∝dσ is not valid in
that context.
The various relations can be illustrated more simply
by assuming that the locus of modes proceeds linearly
down to lower limit Npart = 2 at ¯ρ0NN ≈3 ¯ρ0NSD ≈15.
As ¯ρ0 increases from zero to the endpoint of the lo-
cus of modes the running integral increases accordingly,
with the factor in square brackets ﬁxed at the value for
lower limit Npart ≡2 and σ/σ0 ≡1. Above that point
Npart →˜Npart(¯ρ0) varies with ¯ρ0 according to the locus
of modes. The running integral should then remain at a
ﬁxed value P[¯ρ0| ˜Npart(¯ρ0)] while the quantity in square
brackets varies in accord with ˜Npart(¯ρ0).
Within that
interval dNevt ∝dσ is a good approximation.
Given
that argument interpreting an event-frequency distribu-
tion, e.g. V0A distribution P(nx) in Fig. 5, as a diﬀeren-
tial cross section would produce systematic errors in the
assigned cross-section intervals, as in Fig. 15 (left).
Figure 18 (left) shows the p-Pb TCM diﬀerential cross
section (solid curve) obtained from Ref. [16] ¯pt data and
event distribution P(nch) derived from ¯pt statistical er-
rors (open squares). Also plotted is a running integral
(dashed curve) of the 7 TeV solid curve in Fig. 16 (left)
approximating 5 TeV p-p P(nch) multiplied by 0.035, the
maximum value of the cross-section curve [corresponding
to the limiting value of the term in square brackets in
Eq. (18)]. Correspondence with the P(nch) data is good.
0
0.01
0.02
0.03
0.04
0.05
0.06
0
20
40
60
nch / ∆η
P(nch),  (1/σ0) dσ / dρ0
P(nch)
TCM
5 TeV p-Pb
NSD
0
0.01
0.02
0.03
0.04
0.05
0.06
0
20
40
60
nch / ∆η
P(nch),  (1/σ0) dσ / dρ0
Glauber
V0A P(nch)
5 TeV p-Pb
NSD
FIG. 18:
Left: p-Pb TCM diﬀerential cross section (solid
curve) derived from Ref. [16] ¯pt data and event distribu-
tion P(nch) derived from ¯pt statistical errors (open squares).
Right: Glauber cross-section and V0A P(nch) trends.
Figure 18 (right) shows the Glauber cross-section and
V0A P(nch) trends for comparison. The most important
diﬀerence is between the TCM diﬀerential cross section
(solid) and Glauber cross section (dash-dotted) at small
nch. The Glauber cross-section peak implies that p-Pb
centrality is varying with nch most rapidly near ¯ρ0 =
¯ρ0NSD corresponding to isolated p-N collisions, whereas
the TCM cross-section trend reasonably predicts little
change in centrality in that most-peripheral region.
Equation (17) can also be addressed as an inverse prob-
lem [30] wherein dNevt/d¯ρ0 is the “data,” dσ/dNpart is


## Page 14


14
the “model,” and P(¯ρ0|Npart) relating ¯ρ0 to Npart is the
“kernel.” An inverse problem is solved if given data and
kernel the model can be inferred.
For the analysis of
Ref. [17] a p-Pb geometry model was adopted from a
Glauber MC based on certain assumptions. The relation
of ¯ρ0 to Npart (hadron production model, the kernel) was
also assumed and the resulting convolution integral was
compared to V0A P(nch) data to “validate” the model.
But such a solution is not unique.
In the alternative
TCM analysis of Sec. VI B the kernel was derived from
p-p multiplicity data with the relation of ¯ρ0 to Npart de-
termined by p-Pb ¯pt data. The geometry model (cross-
section distribution) was then inferred from the “data”
by trial-and-error inversion. The TCM result is arguably
unique because of the several direct contacts with mea-
sured data.
VII.
p-Pb pt-SPECTRUM RATIOS
The abstract of Ref. [17] includes the statement “Fur-
thermore, at high-pT the p-Pb spectra are found to be
consistent with the pp spectra [when] scaled by Ncoll for
all centrality classes...” implying that deﬁned spectrum
ratio QpPb(pt) remains close to 1 above some pt value,
independent of nch. The p-Pb spectrum data are recon-
sidered here in the context of the present study.
A.
A TCM for spectrum ratios
In the context of the pt spectrum TCM of Ref. [15] the
spectrum ratio deﬁned in Ref. [17] can be expressed as
Q′
pPb ≡
1
N ′
bin
(Npart/2)¯ρsNN ˆS0(yt) + Nbin¯ρhNN ˆH0(yt)
¯ρspp ˆS0(yt) + ¯ρhpp ˆH0(yt)
=
Nbin
N ′
bin
1
ν
¯ρsNN ˆS0(yt) + ν ¯ρhNN ˆH0(yt)
¯ρspp ˆS0(yt) + ¯ρhpp ˆH0(yt)
(19)
=
Nbin
N ′
bin
1
ν
¯ρsNN
¯ρspp
1 + νxNNT0(yt)
1 + xppT0(yt)
→Nbin
N ′
bin
1
ν
¯ρsNN
¯ρspp
(low pt ⇒LO)
→Nbin
N ′
bin
¯ρsNNxNN
¯ρsppxpp
≈Nbin
N ′
bin
¯ρ2
sNN
¯ρ2spp
(high pt ⇒HI)
where the ﬁrst line is based on TCM pt spectrum mod-
els in Eqs. (1) and (A1) and the last two lines assume
xxx = α¯ρsxx for p-p and all p-N within p-A collisions.
The unprimed parameters are values from the p-Pb TCM
that accurately describe ¯pt data as in Sec. III. The N ′
bin
represents Glauber-model values taken from Table I.
Spectrum ratios from Ref. [17] are taken from Fig. 19
(lower left, V0A). The accessible information is the lim-
iting values in pt < 0.5 (LO) and pt > 10 (HI) GeV/c.
Variation of QpPb(pt) in the transition region from LO
to HI within 1-4 GeV/c is determined by ratio T0(yt) =
ˆH0(yy)/ ˆS0(yt) [15] – whether quantity νxNNT0 is ≫1
(HI) or ≪1 (LO). Details might permit reconstruction of
spectrum hard components as in Ref. [15], but ratio data
plotted on linear pt (as opposed to logarithmic transverse
rapidity yt) do not provide access to that information. If
the assumptions invoked for the Glauber analysis were
correct Nbin/N ′
bin →1 and ¯ρsNN/¯ρspp ≈1. According
to Eqs. (19) LO should then vary as 1/ν and HI remain
near 1, as for A-A collisions with no jet modiﬁcation.
The following analysis is based on the assumption that
¯ρ0 values in Table I determined by V0A centrality bins
correspond to spectrum ratios in Fig. 19 (V0A, lower
left) of Ref. [17]. For each ¯ρ0 value the TCM centrality is
determined from Fig. 15 (left) and the Nbin and ν values
from Fig. 16. Values of ¯ρs are obtained from ¯ρ0 by back
transforming Eq. (2) (third line) using the relations in
Fig. 1. The values of ¯ρsNN then follow from Eq. (5).
Table II shows nominal (primed) and TCM (unprimed)
fractional cross sections and Glauber parameters, midra-
pidity charge density ¯ρ0, N-N soft component ¯ρsNN and
TCM hard/soft ratio xNN required to evaluate Eqs. (19)
for comparison with spectrum ratios from Ref. [17].
TABLE II: Nominal (primed) and TCM (unprimed) fractional
cross sections and Glauber parameters, midrapidity charge
density ¯ρ0, N-N soft component ¯ρsNN and TCM hard/soft
ratio xNN used to evaluate 5 TeV p-Pb spectrum ratios.
σ′/σ0 σ/σ0 N ′
bin Nbin
ν′
ν
¯ρ0
¯ρsNN xNN
0.025 0.15 14.7 3.20 1.87 1.52 44.6 16.6 0.188
0.075 0.24 13.0 2.59 1.86 1.43 35.9 15.9 0.180
0.15
0.37 11.7 2.16 1.84 1.37 30.0 15.2 0.172
0.30
0.58
9.4
1.70 1.80 1.26 23.0 14.1 0.159
0.50
0.80 6.42 1.31 1.73 1.13 15.8 12.1 0.137
0.70
0.95 3.81 1.07 1.58 1.03 9.7
8.7
0.098
0.90
0.99 1.94 1.00 1.32 1.00 4.4
4.2
0.047
B.
Trends from measured spectrum ratios
Figure 19 (left) shows Q′
pPb (biased) LO and HI values
(solid points, dash-dotted curves) obtained from Fig. 19
(lower left) of Ref. [17] plotted vs unprimed (corrected)
TCM centralities σ/σ0 from Table II. The solid curves
are corresponding TCM trends obtained from Eqs. (19)
using appropriate values from Table II. Whereas the LO
values for TCM and Glauber correspond closely there is a
large diﬀerence between HI values. The Glauber HI trend
remains close to unity (as reported in Ref. [17]) but the
TCM HI trend increases strongly up to Q′
pPb ≈3. Lower
open squares are CL1 (at midrapidity) HI values obtained
from the upper-left panel in Fig. 19 of Ref. [17]. Those
data, when multiplied by factor 1.9, correspond closely
to the TCM values (also relevant to midrapidity). The
dashed curves show the TCM result if ¯ρsNN ≈¯ρspp for
all cases, as assumed for the Glauber p-Pb analysis.


## Page 15


15
0
0.5
1
1.5
2
2.5
3
3.5
0
0.25
0.5
0.75
1
1 - σ/σ0
Q′pPb  LO, HI
TCM HI
LO
HI
LO
Glauber HI
V0A
CL1
CL1 × 1.9
0
2
4
6
8
10
12
14
16
0
0.25
0.5
0.75
1
1 - σ/σ0
QpPb  LO, HI
ρsNN / 4.4
TCM HI
TCM LO
FIG. 19:
Left:
Q′
pPb (biased) LO and HI values (solid
points, dash-dotted curves) obtained from Fig. 19 (lower left)
of Ref. [17] plotted vs unprimed (corrected) TCM centralities
σ/σ0 from Table II. Other curves are explained in the text.
Right: QpPb trends (solid) that should be observed if Nbin
were obtained from the p-Pb TCM as in Table II (unprimed).
Figure 19 (right) shows Eqs. (19) with N ′
bin →Nbin
and all else the same (solid curves); i.e. QpPb trends
that should be observed if Nbin were inferred via the
TCM. The dashed curve is ratio ¯ρsNN/¯ρspp appearing
in Eqs. (19) with ¯ρspp →4.4 as in Fig. 9 (right) and
¯ρsNN from Table II. Those results are compatible with
the TCM ¯pt analysis of Ref. [14] as in Sec. III where large
¯pt increases result from MB dijet production increasing
quadratically with p-N (N-N) soft component ¯ρsNN.
Within the context of the Glauber p-Pb centrality anal-
ysis and its assumptions one should expect QpPb ≈1
for very peripheral p-Pb (i.e. p-N ≈p-p) collisions. LO
should then decrease ∝1/ν (i.e. toward 0.5 for p-A col-
lisions) and HI should remain constant near unity with
increasing centrality (e.g. V0A multiplicity). That the
very peripheral values are near 0.5 rather than 1 is al-
ready notable in Fig. 19 of Ref. [17]. The TCM analysis
reveals that the observed peripheral values correspond to
1/N ′
bin = 1/1.94 ≈0.51 – the Glauber estimate for binary
collision number in isolated p-N collisions is Nbin ≈2.
The p-Pb TCM, in the form of Eqs. (19) and unprimed
parameters in Table II, accurately predicts the observed
Glauber LO trend in the left panel – no parameters were
adjusted to accommodate the Q′
pPb data. The large dif-
ference between TCM and Glauber HI trends is then dif-
ﬁcult to explain, since according to Eqs. (19) the ratio
HI/LO is simply the quantity ν ¯ρsNN/¯ρspp and those fac-
tors, when included in Eqs. (19), describe the measured
LO trend accurately. It is also interesting to note that the
CL1 HI trend from Fig. 19 of Ref. [17] follows the TCM
HI trend closely when multiplied by constant factor 1.9.
The rapid increase of QpPb HI for peripheral p-Pb col-
lisions is simply explained in terms of Fig. 15 (left): With
an increasing nch or nx “centrality” condition the multi-
plicity of very peripheral p-Pb (i.e. individual p-N) col-
lisions increases accordingly with little change in the ac-
tual p-Pb centrality (b/b0 ≈1 persists). Peripheral p-Pb
basically follows the p-p nch trend as in Sec. III.
A general conclusion can be drawn from p-Pb QpPb
data in the context of a TCM describing ¯pt data from
the same collision system: In case jets are unmodiﬁed in
p-A collisions and there is linear superposition of p-N col-
lisions one should expect a large increase of QpPb (≫1)
in the high-pt or HI region with increasing nch due to
quadratically increasing MB dijet production in p-N col-
lisions. The LO region should increase modestly accord-
ing to competition between decreasing 1/ν and increasing
(not static as assumed) ¯ρsNN, both as in Fig. 19 (right).
The unexpected results in Fig. 19 of Ref. [17] arise in part
because of certain limitations in the Glauber analysis as
described above, but other aspects remain unexplained.
C.
Identiﬁed-pion spectra for 5 TeV p-Pb collisions
A critical test for the TCM description of QpPb trends
above can be established with published identiﬁed-pion
spectra for 5 TeV p-Pb collisions from Ref. [31].
Figure 20 (left) shows identiﬁed-pion spectra from the
same p-Pb collision system considered throughout this
article. The published spectra have been multiplied by
2π to be consistent with the η densities used in this
study and transformed to yt with Jacobian mtpt/yt. The
spectra are then normalized by soft-component density
¯ρs = (Npart/2)¯ρsNN as reported in Table II following
Eq. (1) (third line) except that an additional factor 0.8
is applied to ¯ρs values in Table II to reﬂect the pion frac-
tion of soft hadrons. The normalized spectra X(yt) can
then be compared with spectrum soft-component model
ˆS0(yt) shown as the bold dotted curve: a L´evy distribu-
tion with parameters T = 145 MeV and n = 8.3 appro-
priate for 5 TeV p-p collisions as reported in Ref. [15].
10
-3
10
-2
10
-1
1
1
2
3
4
yt
X(yt) = [2/Npart(ns)] ρ0(yt) / ρsNN
S0
10
-3
10
-2
10
-1
1
1
2
3
4
yt
[X(yt) − S0(yt)] / x(ns) ν(ns)
H0
FIG. 20:
Left:
Identiﬁed-pion spectra for 5 TeV p-Pb
collisions from Ref. [31] transformed to yt with Jacobian
mtpt/yt and normalized by TCM quantities in Table II (7
thinner curves of several styles). ˆS0(yt) is the soft-component
model.
Right:
Diﬀerence X(yt) −ˆS0(yt) normalized by
x(b)ν(b) = α¯ρsNNν(b) using TCM values from Table II re-
ported in Ref. [14] (thinner curves). The dashed curve is hard-
component model ˆH0(yt) with exponential tail. The dotted
curve is a Gaussian with the same parameters but no tail.
Figure 20 (right) shows the diﬀerence X(yt) −ˆS0(yt)
normalized by x(ns)ν(ns) = α¯ρsNNν(ns) with TCM val-
ues reported in Ref. [14] and Table II. There are no ad-


## Page 16


16
justments to accommodate the data. Given Eq. (1) the
result should be directly comparable to the p-p spectrum
hard-component model in the form ˆH0(yt) with model
parameters (¯yt, σyt, q) = (2.65, 0.59, 3.9) for 5 TeV p-p
collisions as reported in Ref. [15]. The dashed curve is
ˆH0(yt) with (¯yt, σyt, q) →(2.45, 0.605, 3.9).
A shift to
lower fragment momenta for pions is expected based on
Fig. 7 (left) of Ref. [32]: pion FFs are softer than kaon
FFs are softer than proton FFs. The overall TCM spec-
trum description is well within point-to-point data uncer-
tainties except for the lowest centrality class (solid curve)
where the large deviation is expected based on Ref. [15].
One may then conclude that the predictions for quantity
QpPb in Fig. 19 (right) are generally consistent with pub-
lished p-Pb pion spectrum data. The TCM description
of p-Pb spectra assumes linear superposition of p-N col-
lisions within p-Pb collisions. However, it also describes
realistically the changing properties of p-N collisions de-
pending on applied p-Pb nch condition. Those two panels
can be compared with Figs. 1 in Refs. [4, 15].
D.
Spectrum ratios for p-Pb identiﬁed pions
The TCM HI and LO trends in Fig. 19 (right) describe
limiting values. Using the pion pt spectra in Fig. 20 data-
model comparisons for diﬀerential QpPb(pt) are possible.
Figure 21 (left) shows identiﬁed-pion spectrum ratios
QpPb(pt) (bold curves of several styles to 3 GeV/c). The
most-peripheral TCM spectrum is adopted as the p-p
reference.
Unprimed TCM Nbin values from Table II
are used for all ratios. For the most-central 5 TeV p-Pb
spectrum the ratio αρsNNνT0(pt) of hard/soft spectrum
components crosses 1 near pt = 1 GeV/c and reaches
only 5 at pt = 3 GeV/c, the end of the published pion
spectra. The soft component therefore contributes sub-
stantially at that endpoint and asymptotic HI limits are
not attained. The LO limits are not resolved in this plot
format. The thinner TCM curves are discussed below.
Figure 21 (right) shows the same data and curves plot-
ted on logarithmic transverse rapidity yt. The LO trends
below 0.5 GeV/c (yt ≈2) are then clearly resolved, and
the correspondence with the TCM LO predictions (bold
lines with same line styles) is evident. The thinner curves
are TCM predictions based on ﬁxed TCM model func-
tions ˆS0(yt) and ˆH0(yt) in Eq. (19) that appear in Fig. 20.
There is good agreement with the spectrum data, and the
TCM ratios extrapolate to the predicted HI values
The systematic behavior of these spectrum ratios with
increasing p-Pb centrality is formally equivalent to the
variation of p-p spectrum ratios with increasing nch [15].
That similarity is further evidence that ¯ρsNN increases
strongly with p-Pb centrality as revealed by the TCM.
0
2
4
6
8
10
12
14
0
5
10
15
20
pt
QpPb(pt)
TCM HI
0
2
4
6
8
10
12
14
2
4
6
yt
QpPb(yt)
TCM
LO
TCM HI
FIG. 21:
Left:
Identiﬁed-pion spectrum ratios QpPb(pt)
(bold curves of several line styles to 3 GeV/c). The most-
peripheral TCM spectrum is adopted as the p-p reference.
Bold horizontal lines indicate TCM HI values from Fig. 19
(right).
Thinner curves extending to 20 GeV/c are TCM
model ratios. Right: The same data and curves plotted on
logarithmic transverse rapidity yt. Details in the LO region
are now resolved. Note that yt = 6 ⇒pt ≈28 GeV/c and
yt = 7 ⇒pt ≈76 GeV/c.
VIII.
SYSTEMATIC UNCERTAINTIES
The main subject of this study is inference of p-Pb
centrality from certain aspects of measured data. This
section considers systematic uncertainties for two com-
peting methods. Some issues to consider: Are TCM re-
sults relating to p-Pb collisions unique and reliable? Are
Glauber results unique given related physical assump-
tions. Are those assumptions realistic? Do the results
from either method “make sense” in relation to other
data and collision systems? Are certain conjectured bi-
ases considered in the Glauber study relevant to data?
A.
p-Pb TCM uncertainties
TCM uncertainties have been estimated for spectra
and correlations in several previous studies [4, 7–9, 15]
and especially for the recent ¯pt analysis [13]. TCM data
descriptions are typically within data uncertainties.
The relevant issue for this study is the accuracy of
hard/soft fraction x(ns) from which all other aspects of
the p-Pb TCM (e.g. Npart, ν) are derived.
According
to ¯pt data from Ref. [16] the p-Pb TCM is essentially
the p-p TCM below the transition point ¯ρs ≈3 ¯ρsNSD ≈
15 ≡¯ρs0 and inherits p-p uncertainties in that interval
which are described in Refs. [4, 7, 15]. Within that in-
terval x(ns) ≈α¯ρs is accurate to a few percent over a
10-fold increase in MB dijet production, implying that
Npart ≈2 within the same interval. Above ¯ρs0 the x(ns)
model is a conjecture based on (a) continued monotonic
increase with (b) the simplest form. The TCM then has
two adjustable parameters with which to accommodate
¯pt data and does at the percent level as shown in Fig. 2.
In all cases, elements of the TCM are derived based on
data trends, simplicity and self-consistency. The TCM


## Page 17


17
must describe or predict data from all available data sys-
tems or be falsiﬁed.
No ad hoc elements are invoked.
As noted, a key issue is the precise coincidence of p-p
and p-Pb ¯pt data over a substantial ¯ρ0 interval, implying
that p-Pb centrality does not change over that interval
(wherein b/b0 ≈1 and Npart ≈2). Whatever centrality
method is invoked should arrive at that common result.
B.
Geometric Glauber model – general issues
Estimation of systematic uncertainties relating to the
Glauber analysis is problematic given the large deviations
from published data and other analyses as demonstrated
in the present study. Within the context of the Glauber
analysis the key assumptions (a) applicability of a ge-
ometric Glauber model to p-A and (b) validity of the
nch ∝Npart assumption are of critical importance.
Assumption (a) represents a limiting case: Any tar-
get nucleon within an eikonal corridor deﬁned by the in-
vacuum σpp inelastic cross section must suﬀer a collision
with the single projectile proton. But no data support
that assumption. In symmetric A-A collisions there are
many projectile nucleons, and the mean number of binary
collisions per nucleon is less than 6. Most participants
may be created by a projectile with no prior collisions.
This assumption should be considered quite uncertain.
Assumption (b) is generally inconsistent with observa-
tions for more-central A-A collisions. Reference [25] cited
in support of that assumption warns “It should be noted
that this simple scaling [nch ∝Npart] is not observed
for [diﬀerential dnch/dη] particle yields measured in a
limited pseudorapidity range near midrapidity” as noted
in Sec. VI A. The nch ∝Npart trend, which describes
the TCM soft component only, is violated by 80% for
more-central Pb-Pb collisions at 2.76 TeV as in Ref. [14],
Sec. V-A. The large deviation results from the MB di-
jet contribution with nch ∝Nbin. The validity of this
assumption should therefore be considered unlikely. Fur-
ther qualitative issues (a) - (f) are itemized in Sec. X.
C.
Statistical bias and collision models
A statistical quantity or statistic is biased if it returns a
mean or median that is diﬀerent from the true value for a
given data population. In the case of centrality determi-
nation for instance values of Npart or b diﬀerent from the
true value for a given event sample would represent such
a bias. A related aspect is internal consistency wherein
statistical analysis of a given data population returns val-
ues consistent with one another whether biased or not,
for instance mean values of Npart for diﬀerent subsets of
an event ensemble following an expected trend.
Reference [17] refers to “dynamical” bias of central-
ity estimates based on particle multiplicities nch due to
large ﬂuctuations (e.g. of nch for ﬁxed Npart). “...cen-
trality classiﬁcation...based on [charge] multiplicity may
select a sample of [N-N] collisions which is biased...”
(p. 16) and “...generate a dynamical bias in centrality
classes” (abstract).
A proposed measure of such bias
as presented in Fig. 8 (left) of Ref. [17] is the quantity
R = ⟨Multiplicity⟩/[⟨Nancestor⟩µ], where Nancestor (clan
model) is apparently equivalent to Npart according to
the caption, and the data are obtained from the geomet-
ric Glauber MC coupled with NBD and ﬁtted to various
nx (e.g. V0A) distributions. Deviations of R from unity
are expected to indicate dynamical bias.
Figure 22 (left) shows a ratio equivalent to R above
for seven multiplicity bins (points) based on values in
Table I. The open circles correspond to unprimed Npart in
that table. The data points are assigned µ = ¯ρ0NSD = 5
from 5 TeV p-p collisions. The dashed curve represents
V0A data with µ = 11 per the NBD obtained from ﬁts
to those data and is derived from Eqs. (9), (10) and (11),
assuming as in Ref. [17] that P(nx) ≈(1/σ0)dσ/dnx. For
that curve ¯ρ0 →nx/2 is used to match Fig. 8 (left) of
Ref. [17], but note that ∆η = 2.3 for the V0A detector.
The correspondence between this dashed curve and the
V0A data points (solid squares) in Ref. [17] is good.
0
0.2
0.4
0.6
0.8
1
1.2
1.4
1.6
1.8
2
0
25
50
75
100
100 σ/σ0
(2/Npart) ρ0 / µ
Glauber model
b/b0 = 1
V0A
nx/2
0
1
2
3
4
5
6
0
25
50
75
100
100 σ/σ0
(2/Npart) ρ0 / µ
TCM
Glauber model
b/b0 = 1
FIG. 22:
Left: Midrapidity charge density per participant
pair (points) compared to NBD mean µ = ¯ρ0NSD = 5. Npart
and N ′
part values are from Table I. For the V0A curve (dashed)
¯ρ0 →nx/2 and µ = 11 are assumed so as to match Fig. 8 (left)
of Ref. [17]. Right: Similar to the left panel but the added
TCM trend is as described in the text. The open squares are
data from Ref. [17] with TCM Table II values for centralities
and Npart. The close agreement with the TCM is notable.
Figure 22 (right) shows the TCM equivalent (solid
curve) derived from Eqs. (6) for x(ns), (7) for Npart(ns),
(2) to determine ¯ρ0(ns) and the solid curve in Fig. 14
(left) to determine σ/σ0 vs Npart, with µ = ¯ρ0NSD = 5
as in the left panel. The open squares are the same ¯ρ0
values from Ref. [17] and Table I but with the other pa-
rameters in R given unprimed TCM values from Table II.
The Glauber results in the left panel are repeated for
comparison. Whereas the data points in the left panel
seem to deviate signiﬁcantly from a hypothesis based on
¯ρ0NSD ≈5, a property of 5 TeV p-p collisions reported
in Ref. [15], the same data in the right panel are in good
agreement with a TCM trend based on the same value.
The dotted lines represent the relation nch ∝Npart as-
sumed for the Glauber analysis in the form (2/Npart)¯ρ0 =


## Page 18


18
¯ρ0NSD. If that were a true property of the p-Pb data
ensemble then signiﬁcant deviations might indeed repre-
sent statistical bias. But the ¯pt analysis of Ref. [14] re-
veals that p-Pb data are better represented by the TCM
solid curve in the right panel as the “true” data trend.
In fact, individual p-N collisions within p-Pb collisions
are strongly biased relative to ensemble-averaged isolated
p-p collisions depending on the imposed p-Pb nch condi-
tion, just as isolated p-p collisions are biased as to the
mix of hadron production mechanisms depending on an
imposed p-p nch condition. That bias is accurately de-
scribed within the TCM, e.g. by the solid curve in Fig. 22.
The contrasting trends for peripheral collisions are no-
table. As the multiplicity nch condition increases from
zero the TCM curve remains within the b/b0 ≈1 hatched
band with Npart ≈2 for peripheral p-Pb, dominated
by isolated p-N collisions.
Above ¯ρ0 ≈2 ¯ρ0NSD p-Pb
centrality begins to increase (σ/σ0 decreases below 1)
and the p-N mean multiplicity increases toward a limit-
ing value ¯ρ0NN ≈6 ¯ρ0NSD ≈30 corresponding to up-
per limit Npart ≈8 as in Fig. 14 (left).
The prod-
uct (Npart/2)¯ρ0NN then corresponds to the upper limit
¯ρ0 ≈115 for the p-Pb event sample reported in Ref. [16].
In contrast, the V0A dashed curves immediately deviate
from the b/b0 ≈1 hatched bands as nch increases from
zero because the assumption P(nx) ≈(1/σ0)dσ/dnx is
incorrect, as discussed in Sec. VI D and demonstrated in
Fig. 18 (left). One result is the Glauber MC estimate
Nbin ≈2 for ¯ρ0 ≈¯ρ0NSD and isolated p-N collisions.
D.
Internal consistency and centrality strategies
The internal consistency of the Glauber implementa-
tion in Ref. [17] may be questioned. Glauber MC esti-
mates for Npart in Table I are inconsistent with a run-
ning integral of the Glauber diﬀerential cross section in
Fig. 4 (left) as shown in the right panel (solid dots vs solid
curve). The Glauber MC estimates for b in Table I (solid
dots) are inconsistent with the b/b0 trend (open boxes
and dash-dotted curve) in Fig. 11 (left) representing de-
ﬁned centralities. The p-Pb Glauber MC estimate for ν
(derived from Glauber Npart) in Fig. 10 (right) exceeds
the Pb-Pb trend over a substantial ¯ρ0 interval.
Reference [17] describes several strategies for determin-
ing p-Pb centrality depending on the η acceptance and
nature of detectors used to deﬁne centrality classes. The
several detectors include the V0A detector as described
above and a zero-degree neutron calorimeter (ZNA). Ref-
erence [17] asserts that whereas V0A and other charge-
multiplicity detectors may suﬀer from bias due to p-N
multiplicity ﬂuctuations (see previous subsection) no bias
is expected for estimates based on the ZNA assumed to
be causally disconnected from midrapidity nch. However,
diﬀerent η intervals involve diﬀerent combinations of soft
and hard components of hadron production which are not
well deﬁned. The TCM hard component, representing
MB dijets arising from low-x gluons, is strongly peaked
at midrapidity [33] where the TCM is well-established.
Figure 23 (left) shows fractional cross sections in the
form 1 −σ/σ0 vs participant number Npart. Several cen-
trality strategies are represented, including the V0A de-
tector emphasized in this study, the ZNA neutron de-
tector at zero degrees and the known impact parameter
b within the Glauber MC, whose results cluster around
the Glauber trend (dash-dotted curve) derived as a run-
ning integral of Eq. (8). The inverted triangles are points
on that curve corresponding to standard centrality val-
ues. The large disagreement with the TCM curve (solid)
inferred from ¯pt data has been noted above.
0
0.2
0.4
0.6
0.8
1
0
5
10
15
20
Npart
1 − σ/σ0
V0A
b
ZNA
integral
TCM
TCM
Glauber
0
0.2
0.4
0.6
0.8
1
0
20
40
60
nch / ∆η
1 − σ/σ0
NSD
V0A
ZNA
TCM
5 TeV p-Pb
Glauber
TCM
FIG. 23:
Left: Fractional cross section σ/σ0 vs Npart com-
paring several centrality strategies.
The points and curves
are described in the text. Right: Similar to the left panel but
with midrapidity ¯ρ0 instead of Npart. The diﬀerences between
Glauber MC and TCM in the two panels are complementary.
Figure 23 (right) shows fractional cross section vs
midrapidity charge density ¯ρ0.
The dash-dotted curve
is the corresponding Glauber MC curve in the left panel
transformed to ¯ρ0 via the Jacobian in Fig. 12 (right).
The dashed curve is derived from V0A P(nch) assumed
equivalent to a diﬀerential cross section. The ZNA ¯ρ0
values are taken from Fig. 16 (lower right) of Ref. [17].
The TCM curve is a running integral of the TCM diﬀer-
ential cross section in Fig. 13 deﬁned below that ﬁgure.
The V0A data (solid dots) are consistent with the V0A
curve or the Glauber MC curve. The ZNA data (open
circles) favor the V0A curve except for the most-central
points where there are large deviations. In eﬀect, changes
in the ZNA centrality condition there produce no corre-
sponding change in the measured quantity. Again there
is major disagreement with the TCM trend. Generally,
the systematic diﬀerences between alternative centrality
detectors are minor compared to the systematic Glauber-
TCM diﬀerence.
In the left panel the TCM-Glauber diﬀerence arises
from the preferred p-A collision model—what nucleons
within an eikonal corridor are actually “wounded”—
which is an experimental issue. The TCM result is in-
ferred inductively from ¯pt data whereas the geometric
Glauber MC is an assumed model. In the right panel,
the V0A-TCM diﬀerence at small ¯ρ0 arises from confus-
ing the V0A P(nch) with a diﬀerential cross section. The
result is a Glauber prediction that for ¯ρ0 ≈¯ρ0NSD the


## Page 19


19
p-Pb centrality is 90%, whereas the TCM prediction is
100% or b ≈b0, i.e. isolated p-N collisions. At larger ¯ρ0
the Glauber-TCM diﬀerence is complementary to the re-
sult in the left panel: The TCM describes larger charge
multiplicities for smaller Npart as a characteristic of p-N
collisions within p-A collisions, consistent with ¯pt data.
IX.
DISCUSSION
This section emphasizes four topics relating to p-Pb
centrality determination. (a) Any centrality model must
be related to an observable quantity based on a model of
hadron production within high-energy nuclear collisions.
(b) A major information source for formulating hadron
production models is pt spectra and ¯pt data.
(c) Any
model for p-A collisions must rely on the nature of the
proton projectile and its interaction with target nucleons
within a dense nucleus. And (d) MB dijets should play
a major role in the formulation of any collision model.
A.
TCM vs Glauber hadron production models
Hadron production in elementary p-p collisions is ob-
served to proceed via two dominant mechanisms repre-
sented by the TCM soft and hard components. The TCM
eﬃciently and accurately describes a broad array of yield,
spectrum and correlation data. The hard component rep-
resenting MB dijets plays a dominant role in evolution of
data structures with charge multiplicity nch and/or A-B
centrality measured for instance by nucleon participant
number Npart. More-central Au-Au or Pb-Pb collisions
are consistent with participant scaling for the nch soft
component, but the jet-related hard contribution varies
with Nbin in complex ways. The relation between Npart
and nch for p-A collisions is thus an open question that
should be resolved via quantitative analysis, for example
as described in Refs. [13, 14] and Sec. III.
The Glauber study relies on an assumed geometric
Glauber MC and a basic assumption about hadron pro-
duction: hadron multiplicity nch is simply proportional
to Npart. Based on that context larger values of Npart are
related to smaller nch. But p-Pb ¯pt data require smaller
Npart in combination with larger ¯ρ0NN to accommodate
noneikonal dijet production per the TCM. The geometric
Glauber MC is a common basis for centrality determina-
tion in A-A collisions and for several MC collision models
such as HIJING [34] and AMPT [35]. These p-Pb results
motivate reconsideration of the validity of such models.
The data and TCM trends in Fig. 1 and p-A ¯pt data in
Fig. 2 are consistent with the following scenario: Increase
of jet-related hadron production in p-A collisions may
proceed via two mechanisms depending on control pa-
rameter ¯ρs: (a) increasing depth of splitting cascades on
momentum fraction x within single p-N collision partners
that increases ¯ρsNN(ns) ≈¯ρs for the most-peripheral p-A
collisions or (b) increasing participant-nucleon number
Npart(ns) with increasing p-A centrality and ¯ρsNN(ns) <
¯ρs. The relative contributions depend on probabilities.
Below transition point ¯ρs0 single p-N collisions dominate
and the noneikonal ¯ρh ≈¯ρhNN ≈α¯ρ2
sNN trend for dijet
production observed in p-p collisions [4] is determining.
Above ¯ρs0 p-A centrality dominates and increasing p-N
binary-collision number Nbin plays the dominant role in
dijet production with ¯ρh(ns) ≈Nbin(ns)α¯ρ2
sNN(ns). Di-
jet manifestations provide an essential and eﬀective probe
of p-A centrality. A primary message from p-Pb ¯pt data is
the trend toward larger ¯ρ0NN = (2/Npart)¯ρ0 and smaller
Npart compared to expectations based on ¯ρ0 ∝Npart lin-
ear scaling as assumed for the Glauber study in Ref. [17].
B.
TCM for pt spectra vs ¯pt data
The TCM for pt spectra such as reported in Refs. [4, 7,
8] inspired the TCM for ¯pt data as in Ref. [14]. It is not
surprising then to ﬁnd structural equivalents. Normal-
ized spectra ¯ρ0(yt)/¯ρs in Fig. 20 (left) relative to univer-
sal soft-component model ˆS0(yt) are equivalent to ¯Pt/¯ρs
in Eq. (4) (second line) relative to universal soft compo-
nent ¯pts which may be derived from ˆS0(yt). Relative to
the soft components the hard components then vary with
common factors x(ns)ν(ns). Dividing by those factors
leaves ¯pthNN for ¯pt data and ˆH0(yt) for pt spectra from
which ¯pthNN may be derived. Spectrum ratios such as
QpPb are like ¯pt = ¯Pt/nch in that distinct soft and hard
components and their corresponding hadron production
mechanisms may be confused and obscured.
Hadron production in A-B collisions may be summa-
rized as follows: The product ¯ρs = (Npart/2)¯ρsNN ap-
plies generally.
In p-p collisions hadron production is
controlled by ¯ρsNN →¯ρs with noneikonal ¯ρh ∝¯ρ2
s and
Npart ≡2 ﬁxed. In A-A collisions hadron production is
controlled by Npart with eikonal Nbin ≈(Npart/2)4/3 and
¯ρsNN ≈¯ρsNSD approximately constant. Production in
p-A collisions is intermediate and must be determined by
experiment, for example by TCM analysis of p-Pb ¯pt data
where MB dijets dominate data variations.
Figure 20
conﬁrms that the Npart and ¯ρsNN trends in Table II in-
ferred from the ¯pt study in Ref. [14] accurately predict
p-Pb pt spectrum data for pions in Ref. [31]. It also val-
idates the assumption in Ref. [14] that jet production
in p-Pb is unmodiﬁed, since spectrum hard components
H(yt) from p-Pb spectra are consistent with p-p ˆH0(yt).
C.
The proton projectile within p-A collisions
A major issue arising from comparisons of the Glauber
MC and TCM for p-Pb collisions in Sec. VI is the large
diﬀerence between the upper limit on participant num-
ber Npart ≈16-19 for b ≈0 estimated with the geometric
Glauber MC and the much lower Npart ≈8 inferred from
TCM analysis of ¯pt data. The p-Pb Glauber MC is based


## Page 20


20
on the assumption that even for a central p-Pb collision
each of approximately 18 binary p-N encounters is equiv-
alent to an isolated in-vacuum p-p collision. But in most-
central Au-Au or Pb-Pb collisions the mean number of
binary collisions per participant is less than 6, and 18
successive binary p-N collisions has never been otherwise
observed. How a proton projectile interacts with target
nucleons after many p-N collisions and within a dense
nuclear environment is an open question. p-Pb data may
provide a unique basis for its resolution.
A participant nucleon within the target nucleus as de-
ﬁned has been eﬀectively struck by a projectile proton.
The geometric Glauber MC assumes that any target nu-
cleon residing within an “eikonal corridor” relative to the
projectile-proton trajectory (deﬁned by a p-N cross sec-
tion ≈σpp) becomes a participant. However, the eﬀec-
tive number of participants may be reduced in at least
two ways: (a) The capacity of the projectile proton to
“wound” a target nucleon may decrease along its trajec-
tory after multiple prior p-N collisions. (b) The capacity
of a projectile proton to “wound” at any point along its
trajectory within a dense nuclear environment may be
substantially less than predicted via the p-p cross sec-
tion.
Data from high-energy p-A collisions such as ¯pt
data from Ref. [16], spectrum data from Ref. [31] and
centrality data from Ref. [17] provide a unique opportu-
nity to explore such novel possibilities. A follow-up study
of that problem will be presented in a future article.
D.
MB dijets and p-Pb centrality determination
The distinction between soft and hard components of
yields, spectra and correlations from high-energy nuclear
collisions is the basis for the TCM. That separation is the
result of observed data structures rather than a priori
assumptions. Attribution of the hard component to MB
dijet production is also the result of comparisons between
measured data trends and measured jet characteristics.
MB dijets then provide the main source of information for
centrality determination in p-A collisions, as in Sec. III.
Generally, the importance of MB dijets for understanding
high-energy nuclear collisions should be emphasized [27].
Measured MB jet trends indicate that p-p collisions
are noneikonal based on the observed relation ¯ρh ∝¯ρ2
s.
There is no restricted “eikonal corridor” depending on
p-p impact parameter, all participant low-x partons in
each proton may interact within any collision. The same
relation in p-A collisions may then be used to track the
factorization ¯ρs = (Npart/2)¯ρsNN via the MB jet yield
per ¯ρhNN ∝¯ρ2
sNN, e.g. the ¯pt analysis of Ref. [14], from
which Npart(¯ρ0) may be inferred as in Fig. 3 (left).
Although ¯pt data may be very precise they retain lim-
ited spectrum information.
Predictions of full spectra
provide a more rigorous test of the TCM and the role
of MB jets in hadron production. The validity of TCM-
inferred Npart(¯ρ0) is conﬁrmed by accurate prediction of
p-Pb spectra and spectrum ratios in Figs. 20 and 21. In
contrast, the Glauber analysis apparently does not in-
corporate any aspect of jet production. The central as-
sumption ¯ρ0 ∝Npart is consistent with a solitary soft
component and no jet contribution, which contradicts a
broad array of A-B data [4, 7–9]. The geometric Glauber
MC is based on the eikonal approximation applied at the
p-N level as well as the composite A-B level, which con-
tradicts an assortment of p-p data [4, 7, 15, 19]
X.
SUMMARY
This article reports a comparative study of two meth-
ods for estimating the centrality of p-A (speciﬁcally
p-Pb) collisions.
One method is based on simulations
of projectile-proton interactions with Pb target nucleons
via a geometric Glauber Monte Carlo and an assump-
tion that hadron production is proportional to number of
participant nucleons as simulated. The other method is
based on a two-component (soft + hard) model (TCM) of
hadron production describing any A-B collision system.
The TCM has been applied successfully and accurately
to yields, spectra and two-particle correlations from a
variety of A-B collision systems over a broad range of
collision energies. The basic elements of the TCM, soft
(projectile dissociation) and hard (scattered-parton frag-
mentation to jets) hadron production mechanisms, reﬂect
high-energy physics results over several decades. Most
recently, the TCM was used to describe ensemble-mean
¯pt data from p-p, p-Pb and Pb-Pb within their uncer-
tainties. From the ¯pt study the inferred relation between
p-Pb participant-nucleon number Npart and charge den-
sity ¯ρ0 near midrapidity was obtained as a simple mod-
iﬁcation of the data trend for p-p collisions. According
to ¯pt data the noneikonal nature of p-p collisions—each
participant parton in one proton can interact with any
participant in the partner proton—continues for p-N col-
lisions within p-A collisions, and MB dijet production is
then related quadratically to the p-N charge density.
The Glauber Monte Carlo (MC) study reports rapid
increase of Npart with nch (as a centrality control pa-
rameter) to a mean value within 16-19 for most-central
density ¯ρ0 ≡nch/∆η ≈45, with ﬂuctuations of Npart to
as high as 30. In contrast, the TCM describes slow in-
crease of Npart, with maximum value near 8 for ¯ρ0 ≈115.
The present study aims to determine the origin of those
diﬀerences and which method, if either, may be correct.
Detailed comparison of the two methods leads to the
following observations: (a) The Glauber MC predicts a
diﬀerential cross section dσ/dNpart describing maximum
centrality variation for most-peripheral collisions (small-
est nch) where isolated p-N collisions should dominate,
whereas the TCM predicts minimal centrality variation
in the same interval. (b) The Glauber analysis locates
most-central p-Pb collisions below ¯ρ0 ≈50, whereas mea-
sured p-Pb ¯pt data extend out to 115. (c) The Glauber
study describes the number of hadrons per participant
pair as remaining near the p-p mean value 5, whereas


## Page 21


21
the TCM derived from 5 TeV p-Pb ¯pt data describes
rapid increase of that quantity for more-peripheral p-Pb
collisions, similar to p-p data, up to a maximum value
near 30. (d) Trends derived from the Glauber MC can
be combined to predict p-Pb ¯pt data, but the predicted
values are much smaller than measured ¯pt data and the
TCM description. (e) The tail of probability distribution
P(nch) for p-N collisions within p-Pb collisions inferred
via the Glauber MC drops oﬀmuch more rapidity than
measured distributions for p-p collisions. (f) The p-Pb/p-
p spectrum ratio QpPb(pt) (inferred by scaling with N-N
binary-collision number Nbin from the Glauber MC) is
said to remain near 1 for pt > 10 GeV/c for all p-Pb cen-
tralities, whereas the TCM derived from ¯pt data predicts
rapid increase of that ratio to about 14. The TCM ratio
prediction is found to be consistent with measured pion
spectra from 5 TeV p-Pb collisions.
Those observations, taken together, suggest that the
Glauber MC is not a valid description of p-Pb collisions
and/or that the basic assumption ¯ρ0 ∝Npart is not valid,
whereas the TCM accurately describes a variety of data.
One question that emerges concerning the basis for the
Glauber MC: To what extent is a projectile proton able
to “wound” a target nucleon and thereby produce a par-
ticipant? The Glauber MC assumes that any encounter
corresponding to a p-N cross section of 70 mb is a colli-
sion. TCM results suggest that the eﬀective participant
production rate may be only 1/3 of the Glauber estimate.
The geometric Glauber MC is a common basis for cen-
trality determination in A-A collisions and for several
MC collision models such as HIJING and AMPT. These
p-Pb results motivate reconsideration of the validity of
such models. As to recent claims of collectivity in p-A
systems, p-Pb pion spectra and their ratios indicate no
deviation from linear superposition of p-N collisions over
a large p-Pb nch and centrality interval. Jet production,
at least, appears to remain unmodiﬁed in p-Pb collisions.
Appendix A: TCM for p-p spectra
The TCM for hadron production in high energy nu-
clear collisions represents consistent observations [4, 7–
10, 13–15] that hadron production near midrapidity is
dominated by two mechanisms:
(a) projectile-nucleon
dissociation to charge-neutral hadron pairs (soft) and (b)
scattered-parton fragmentation to correlated hadron jets
(hard).
A TCM reference can be deﬁned in terms of
linear superposition of a basic process: low-x parton-
parton interactions within p-p collisions or nucleon-
nucleon (N-N) interactions within p-A and A-A collisions.
Deviations from a TCM reference may then reveal gen-
uine novelty (e.g. nonlinearity) in a composite system.
The TCM for pt spectra and ¯pt in p-Pb collisions can be
used to determine centrality in that system.
1.
Basic TCM description of p-p pt or yt spectra
The TCM for p-p collision data emerged from analysis
of 200 GeV pt spectrum data. Systematic analysis of the
nch dependence of pt spectra from 200 GeV p-p collisions
described in Ref. [7] led to a compact phenomenological
TCM with approximate factorization of multiplicity nch
and transverse-rapidity yt dependence in the form
d2nch
ytdytdη = Spp(yt, nch) + Hpp(yt, nch)
(A1)
≈¯ρs(nch) ˆS0(yt) + ¯ρh(nch) ˆH0(yt)
with mean angular densities ¯ρx = nx/∆η.
Transverse
rapidity yt ≡ln[(pt + mt)/mh] with transverse mass de-
ﬁned by m2
t = p2
t + m2
h provides improved visual access
to spectrum structure at lower pt or yt (for unidentiﬁed
hadrons pion mass mh = mπ is assumed). Unit-integral
soft-component model ˆS0(mt) is consistent with a L´evy
distribution on mt, while peaked hard-component model
ˆH0(yt) is well approximated by a Gaussian on yt centered
near yt ≈2.65 (pt ≈1 GeV/c) with exponential (on yt)
tail reﬂecting an underlying power-law (on pt) jet spec-
trum [19]. Conversion from pt or mt to yt is accomplished
with Jacobian ptmt/yt.
Integration of Eq. (A1) over yt results in the angular-
density TCM ¯ρ0 = ¯ρs+¯ρh. Spectrum [7, 15] and angular-
correlation [4] data reveal that soft and hard angular den-
sities are related by ¯ρh = α¯ρ2
s with α ≈0.006 within
∆η = 2 at 200 GeV. The two relations are equivalent
to a quadratic equation that uniquely deﬁnes ¯ρs and ¯ρh
in terms of ¯ρ0 (when corrected for ineﬃciencies). That
quadratic relation is valid over a ¯ρs interval correspond-
ing to 100-fold variation of MB dijet production.
2.
Recent TCM results for p-p pt spectra
The dijet production trend ¯ρh ∝¯ρ2
s inferred from
p-p hadron spectra as described above combined with
¯ρs ∝ln(√s/10 GeV) [15] describes jet-spectrum energy
trends over large p-p collision-energy and jet-energy inter-
vals [19]. Predicted jet-spectrum trends can then be com-
bined with measured fragmentation functions (FFs) [32]
to predict hadron-spectrum hard component H(yt) [36].
Figure 24 (left) shows ratio H(pt, √s)/¯ρs(√s)
≈
α(√s)¯ρs(√s) ˆH0(pt, √s) for NSD p-p collisions measuring
the spectrum hard component per soft-component hadron
corresponding (by hypothesis) to dijet production per
participant low-x gluon. The 13 TeV TCM solid curve is
compared to spectrum data (open points). The two dot-
ted curves are for 0.9 and 2.76 TeV and the dashed curve
is for 7 TeV. The 200 GeV summary includes paramet-
ric variation of ˆH0(yt, nch) for seven multiplicity classes
(thin solid curves).
Corresponding data (solid points)
represent NSD p-p collisions. Isolated hard components
clarify spectrum energy evolution and its relation to di-
jet production. The predictions for six collision energies


## Page 22


22
(curves) are compared to data from four energies (13, 7,
0.9 and 0.2 TeV) in Ref. [19]. The overall result is a com-
prehensive description of dijet contributions to pt spectra
vs p-p collision energy over three orders of magnitude.
10
-7
10
-6
10
-5
10
-4
10
-3
10
-2
10
-1
1
10
pt (GeV/c)
H(pt) / ρs
1/pt5.6
1/pt8.5
NSD p-p
0.2 TeV
13 TeV
17.3 GeV
0
0.2
0.4
0.6
0.8
1
1.2
1.4
1.6
1.8
10
10
2
10
3
10
4
√s (GeV)
100 α
∆η = 0.6
∆η = 1.6
∆η = 2
FIG. 24:
Left: A survey of spectrum hard components over
the currently accessible energy range from threshold of di-
jet production (10 GeV) to LHC top energy (13 TeV). The
curves are determined by TCM parameters for NSD p-p colli-
sions from Ref. [37]. The 200 GeV ﬁne solid curves illustrate
nch dependence. The points are from Refs. [4] (200 GeV) and
[37] (13 TeV). Right: TCM hard-soft ratio parameter α deter-
mined by analysis of spectrum-ratio data (solid points) from
Ref. [37]. The solid curve is deﬁned in Ref. [15]. The dashed
curve is the solid curve reduced by factor 0.83 corresponding
to the ∆η acceptance reduction. The open circles are derived
in Ref. [14] from p-p ¯pt data in Ref. [16].
Parameter α connecting soft and hard components of
p-p hadron yields is related to jet systematics by
α¯ρ2
sNSD = ¯ρhNSD = ϵ(∆η)fNSD2¯nch,j,
(A2)
where 2¯nch,j is the mean hadron fragment multiplicity
per dijet averaged over a jet spectrum for given collision
energy [32] and fNSD = (1/σNSD)dσjet/dη is the dijet
frequency and η density per NSD p-p collision [36]. The
energy trends for those quantities, inferred from isolated-
jet data, can be used to predict an energy trend for α.
Figure 24 (right) shows values for α(√s) (solid points)
obtained for 200 GeV and 13 TeV from Refs. [4, 15] re-
spectively.
The solid curve from Ref. [15] is based on
measured properties of isolated jets [19]. The open points
are inferred from ¯pt trends in Ref. [14] (described below).
The dashed curve is the solid curve reduced by factor
≈0.83 (≈0.5/0.6) corresponding to the reduced angular
acceptance ∆η = 0.6 in Ref. [16] compared to previous
results for ∆η = 2.0 [4, 7].
Appendix B: ¯pt TCM for p-p collisions
The present study emphasizes comparisons between ¯pt
analysis of p-p, p-Pb and Pb-Pb collisions and a Glauber
analysis of p-Pb centrality. This appendix brieﬂy reviews
basic ¯pt TCM analysis for elementary p-p collisions.
Reference [13] established that a TCM for ratio ¯pt =
¯Pt/nch constitutes a good description of LHC data from
p-p and Pb-Pb collisions at several energies and pro-
vided hints as to the mechanism of p-Pb ¯pt variation
– evolving from a p-p trend for smaller nch to a quan-
titatively diﬀerent but similar trend above a transition
point.
Reference [15] presented a detailed TCM anal-
ysis of p-p pt spectra for a range of energies from 17
GeV to 13 TeV. Soft component ˆS0(mt, √s) varies weakly
with energy and not at all with nch, but hard compo-
nent ˆH0(yt, ns, √s) varies strongly with energy (consis-
tent with jet properties) and signiﬁcantly with nch (as
established with 200 GeV spectra). Those new spectrum
results have been incorporated in a revised ¯pt analysis in
Ref. [14] summarized for p-p here and for p-Pb in Sec. III.
Quantities ¯pth(ns, √s), α(√s) and an eﬀective detec-
tor acceptance ratio ξ are used to update results from
Ref. [13]. The TCM for charge densities averaged over
some angular acceptance ∆η (e.g. 0.6 for Ref. [16]) is
¯ρ0 = ¯ρs + ¯ρh
(B1)
= ¯ρs[1 + x(ns)],
¯ρ′
0
¯ρs
= n′
ch
ns
= ξ + x(ns),
where x(ns) ≡
¯ρh/¯ρs
≈α¯ρs is the ratio of hard-
component to soft-component yields [7] and α(√s) is
shown in Fig. 24 (right).
Primes denote uncorrected
quantities. The TCM for ensemble-mean total pt inte-
grated over some angular acceptance ∆η from p-p colli-
sions for given (nch, √s) is expressed as
¯Pt =
¯Pts + ¯Pth
(B2)
= ns¯pts + nh¯pth.
The conventional intensive ratio of extensive quantities
¯P ′
t
n′
ch
≡¯p′
t ≈
¯pts + x(ns)¯pth
ξ + x(ns)
(B3)
(assuming ¯P ′
t ≈¯Pt [14]) in eﬀect partially cancels MB
dijet manifestations represented by ratio x(ns). The al-
ternative ratio
n′
ch
ns
¯p′
t ≈
¯Pt
ns
= ¯pts + x(ns)¯pth(ns)
(B4)
= ¯pts + α(√s) ¯ρs ¯pth(ns, √s)
preserves the simplicity of Eq. (B2) and provides a con-
venient basis for testing the TCM hypothesis precisely.
Figure 25 (left) shows ¯pt data for four p-p collision ener-
gies from the RHIC (solid triangles [7]), the Sp¯pS (open
boxes [38])and the LHC (upper points [16]) increasing
monotonically with charge density ¯ρ0 = nch/∆η. The
lower points and curves correspond to full pt acceptance.
For acceptance extending down to zero (ξ = 1), ¯p′
t →¯pt
in Eq. (B3) should vary between the universal lower limit
¯pts ≈0.4 GeV/c (nch = 0) and ¯pth (nch →∞) as lim-
iting cases. For a lower pt cut pt,cut > 0 the lower limit
is ¯p′
ts = ¯pts/ξ (dotted lines) and the data are systemati-
cally shifted upward (upper points and curves). The solid


## Page 23


23
curves represent the p-p ¯pt TCM from Ref. [14]. Note
that the 7 TeV ¯pt data extend to ¯ρ0 ≈10 ¯ρ0NSD ≈60
and were derived from 150 million p-p collision events.
0.4
0.5
0.6
0.7
0.8
0.9
0
20
40
60
nch / ∆η
¯pt ′  (GeV/c)
p-p
7 TeV
2.76
900 GeV
900
200
¯pts
¯pts ′
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
1.1
0
10
20
30
40
50
ns / ∆η
(nch ′/ns)  ¯pt ′ (GeV/c)
p-p
7 TeV
2.76
900 GeV
200
¯pts
FIG. 25:
Left: ¯pt vs nch for several collision energies. The
upper group of points from Ref. [16] are derived from particle
data with a lower pt cutoﬀ. The lower 900 GeV data from
Ref. [38] and 200 GeV data from Ref. [7] are extrapolated to
zero pt. Right: Data from the left panel multiplied by factor
n′
ch/ns that removes the jet contribution and the eﬀect of the
low-pt cut on the soft component from the denominator of ¯pt.
Figure 25 (right) shows data on the left transformed
via Eq. (B4) to (n′
ch/ns)¯p′
t ≈¯Pt/ns (points). The TCM
curves undergo the same transformation and the slopes of
the resulting straight lines are α(√s)¯pth0(√s). The data
deviate signiﬁcantly from the straight-line TCM because
of systematic variation with nch of the pt spectrum hard-
component shape as reported in Refs. [14, 15]. However,
those details are beyond the scope of the present study.
The success of the p-p ¯pt TCM conﬁrms that variation
of p-p ¯pt is dominated by jet fragments from large-angle-
scattered low-x gluons. The hard yield or angular den-
sity ¯ρh ≈α(√s) ¯ρ2
s represents the dijet fragment density
determined precisely by soft component ¯ρs. The pt spec-
trum TCM hard component and underlying jet energy
spectrum evolve according to the same rules [19]. The
quadratic relation ¯ρh ∝¯ρ2
s implies that p-p collisions are
noneikonal (compared to the eikonal trend ¯ρh ∝¯ρ4/3
s
).
The quadratic trend (each participant gluon in one pro-
ton can interact with any participant gluon in the partner
proton) implies that p-p collisions with large nch are very
jetty.
Reference [14] demonstrates a direct connection
between ¯pt hard component ¯pth(ns), pt spectrum hard
component H(pt, ns) [15] and jet spectra as in Ref. [19].
Thus, a variety of p-p data provide strong evidence that
MB dijets dominate p-p collisions and ¯pt(nch, √s) trends.
[1] M. L. Miller, K. Reygers, S. J. Sanders and P. Steinberg,
Ann. Rev. Nucl. Part. Sci. 57, 205 (2007).
[2] T. A. Trainor and D. J. Prindle, hep-ph/0411217.
[3] T. Sj¨ostrand, S. Mrenna and P. Z. Skands, Comput. Phys.
Commun. 178, 852 (2008); T. Sj¨ostrand and M. van Zijl,
Phys. Rev. D 36, 2019 (1987); T. Sj¨ostrand, Comput.
Phys. Commun. 82, 74 (1994);
[4] T. A. Trainor and D. J. Prindle, Phys. Rev. D 93, 014031
(2016).
[5] T. A. Trainor, Phys. Rev. D 87, 054005 (2013).
[6] D. Kharzeev and M. Nardi, Phys. Lett. B 507, 121
(2001).
[7] J. Adams et al. (STAR Collaboration), Phys. Rev. D 74,
032006 (2006).
[8] T. A. Trainor, Int. J. Mod. Phys. E 17, 1499 (2008).
[9] G. Agakishiev, et al. (STAR Collaboration), Phys. Rev.
C 86, 064902 (2012).
[10] T. A. Trainor and D. T. Kettler, Phys. Rev. C 83, 034903
(2011).
[11] R. J. Porter and T. A. Trainor (STAR Collaboration), J.
Phys. Conf. Ser. 27, 98 (2005).
[12] R. J. Porter and T. A. Trainor (STAR Collaboration),
PoS CFRNC2006, 004 (2006).
[13] T. A. Trainor, Phys. Rev. C 90, no. 2, 024909 (2014).
[14] T. A. Trainor, arXiv:1708.09412.
[15] T. A. Trainor, J. Phys. G 44, no. 7, 075008 (2017).
[16] B. B. Abelev et al. (ALICE Collaboration), Phys. Lett.
B 727, 371 (2013).
[17] J. Adam et al. (ALICE Collaboration), Phys. Rev. C 91,
no. 6, 064905 (2015).
[18] K. Dusling, W. Li and B. Schenke, Int. J. Mod. Phys. E
25, no. 01, 1630002 (2016).
[19] T. A. Trainor, Phys. Rev. D 89, 094011 (2014).
[20] K. Aamodt et al. (ALICE Collaboration), Phys. Rev.
Lett. 106, 032301 (2011).
[21] K. Aamodt et al. (ALICE Collaboration), Phys. Rev.
Lett. 106, 032301 (2011).
[22] A. Bialas, M. Bleszynski and W. Czyz, Nucl. Phys. B
111, 461 (1976).
[23] J. E. Elias, W. Busza, C. Halliwell, D. Luckey, P. Swartz,
L. Votta and C. Young, Phys. Rev. D 22, 13 (1980).
[24] B. B. Back et al. (PHOBOS Collaboration), Phys. Rev.
C 70, 021902 (2004).
[25] B. B. Back et al. (PHOBOS Collaboration),
nucl-
ex/0301017.
[26] B. B. Back et al. (PHOBOS Collaboration), Phys. Rev.
C 72, 031901 (2005).
[27] T. A. Trainor, arXiv:1701.07866.
[28] J. Adam et al. (ALICE Collaboration), Eur. Phys. J. C
77, no. 1, 33 (2017).
[29] M. B. De Kock, H. C. Eggers and T. A. Trainor, Phys.
Rev. C 92, no. 3, 034908 (2015).
[30] T. A. Trainor, R. J. Porter and D. J. Prindle, J. Phys. G
31, 809 (2005).
[31] B. B. Abelev et al. (ALICE Collaboration), Phys. Lett.
B 728, 25 (2014).
[32] T. A. Trainor and D. T. Kettler, Phys. Rev. D 74, 034012
(2006).
[33] G. Wolschin, Phys. Rev. C 91, no. 1, 014905 (2015).
[34] X.-N. Wang, Phys. Rev. D 46, R1900 (1992); X.-N. Wang
and M. Gyulassy, Phys. Rev. D 44, 3501 (1991).
[35] Z.-W. Lin, C. M. Ko, B.-A. Li, B. Zhang and S. Pal,
Phys. Rev. C 72, 064901 (2005).
[36] T. A. Trainor, Phys. Rev. C 80, 044901 (2009).


## Page 24


24
[37] J. Adam et al. (ALICE Collaboration), Phys. Lett. B
753, 319 (2016).
[38] C. Albajar et al. (UA1 Collaboration), Nucl. Phys. B
335, 261 (1990).

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
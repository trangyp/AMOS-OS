---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1805.09681v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1805.09681v1_Comparing_the_PYTHIA_Monte_Carlo_to_a_two-component__soft___hard__model_of_hadro

> Source: 1805.09681v1_Comparing_the_PYTHIA_Monte_Carlo_to_a_two-component__soft___hard__model_of_hadro.pdf

> Pages: 24

---


## Page 1


version 1.8
Comparing the PYTHIA Monte Carlo to a two-component (soft + hard) model of
hadron production in high-energy p-p collisions
Thomas A. Trainor
CENPA 354290, University of Washington, Seattle, WA 98195
(Dated: August 23, 2021)
The PYTHIA Monte Carlo (PMC), ﬁrst introduced more than thirty years ago, remains a popular
simulation tool both for analysis of p-p collision dynamics and for detector design and calibration.
The PMC assumes that almost all produced hadrons result from parton-parton scatterings (interac-
tions) described by pQCD (a hard component), and that multiple parton interactions per collision
event (MPIs) are a common occurrence. In contrast, a two-component (soft + hard) model (TCM)
of high-energy collisions, inferred inductively from a variety of data formats, attributes a majority
of ﬁnal-state hadrons to a soft component (projectile-nucleon dissociation) and a minority to a hard
component representing minimum-bias dijet production (corresponding to measured jet spectra and
fragmentation functions). The hard-component hadron yield is precisely proportional to the square
of the soft-component yield over an interval corresponding to 100-fold increase in dijet production.
The two data descriptions appear to be in conﬂict. This study presents a detailed comparison of
the two models and their relations to a broad array of collision data. The PMC appears to disagree
with some data, whereas the TCM provides an accurate and comprehensive data description.
PACS numbers: 12.38.Qk, 13.87.Fh, 25.75.Ag, 25.75.Bh, 25.75.Ld, 25.75.Nq
I.
INTRODUCTION
This study compares the PYTHIA Monte Carlo [1] to a
two-component (soft + hard) model (TCM) of p-p hadron
production near midrapidity [2, 3]. The two systems are
confronted with a variety of data from several collision
systems.
The general context for p-p Monte Carlos is
drawn from summaries reported in Refs. [4, 5].
General-purpose Monte Carlos (GPMCs) are intended
to explore physical models of high-energy p-p collisions
and (with detector-model Monte Carlos) to design and
calibrate detector systems. GPMCs combine perturba-
tive QCD (pQCD) at short distances and QCD-inspired
phenomenological models at longer distances [5].
The
main components of GPMCs are (a) a pQCD description
of hard parton scattering and parton splitting cascades
(showering), (b) a hadronization transition between par-
tonic and hadronic ﬁnal states and (c) a description of
“soft hadron physics” said to include an underlying event,
minimum-bias (MB) interactions and color reconnection.
QCD-inspired phenomenological models for item (b)
include string models (e.g. as in PYTHIA) and clus-
ter models (e.g. as in HERWIG). The string model or
Lund model [6] is based on strings (color ﬂux tubes)
joining color-connected energetic partons, which strings
then fragment into hadrons upon elongation. The clus-
ter model is said to “...force ‘by hand’ all gluons to
split into quark-antiquark pairs at the end of the parton
shower.”
Those “excited mesons” decay “isotropically
to two hadrons...” [5].
The cluster scenario is consis-
tent with the current TCM soft component and longitu-
dinal projectile-nucleon dissociation (Sec. II C). GPMC
hadronization models can be contrasted with measured
fragmentation functions (FFs) described by pQCD en-
ergy evolution and applied to ﬁnal-state hadrons [7].
Some models for item (c) – soft QCD and underlying
event physics – are based on multiple parton interactions
(MPIs), color reconnection (CR) and p-p impact param-
eter dependence. The underlying event (UE) is deﬁned
as the complement to a hard scatter (dijet): “In events
containing a hard parton-parton interaction, the under-
lying event represents the additional activity which is not
directly associated with that interaction” [4]. The UE as
such is deﬁned only in the context of a hard jet trigger.
The dominant contribution to the UE is said to come
from additional color exchanges (MPIs). The UE thus
remains perturbative, the trigger hard scatter being an
element of the high-pt tail of the MPI distribution. The
associated “jet pedestal” eﬀect “is interpreted as follows.
When two hadrons collide at non-zero impact parame-
ter, high-p⊥interactions can only take place inside the
overlapping region. Imposing a hard selection cut there-
fore statistically biases the event sample toward more
central collisions, which will also have more underly-
ing activity.
...
The shape of the pedestal...is there-
fore related to...modeling of the impact parameter depen-
dence” [4]. The primary motivation for the CR mecha-
nism is ensemble-mean ¯pt data: “Without colour recon-
nections, the predicted ⟨p⊥⟩(Nch) [i.e. ¯pt(nch)] distribu-
tions appear to rise too slowly with Nch” [4].
In an alternative scenario inelastic scattering is mod-
eled in terms of cut Pomerons relating “...diﬀractive and
non-diﬀractive scattering that is absent in the MPI-based
models.... [In the MPI formulation Pomeron exchange
is restricted to a small number of diﬀractive events.]
...the picture now is one of both hard and soft pomerons,
ideally with a smooth transition between the two” [4].
Pomerons have the quantum numbers of the vacuum and
thus do not color connect collision partners (e.g. projec-
tile protons or hard-scattered partons leading to jets).
The present study focuses on the PYTHIA Monte
Carlo (PMC) wherein MPIs are assumed to be the domi-
arXiv:1805.09681v1  [hep-ph]  23 May 2018


## Page 2


2
nant or exclusive mechanism for hadron production. The
PMC contains no feature comparable to the TCM soft
component. “MPI modeling has traditionally been a hall-
mark of PYTHIA” [4]. Non-diﬀractive inelastic scatter-
ing is modeled in the PMC by extending the pQCD par-
ton scattering cross section down to pt = 0, with collision-
energy-dependent soft cutoﬀparameter p⊥0 ∝Eϵ
CM.
Cutoﬀparameter p⊥0 “is thus one of the main ‘tuning’
parameters in such models” [4]. p-p centrality, described
by the Glauber model with eikonal approximation, is a
major feature of the model.
Color reconnection is as-
sumed so as to minimize the total string length (i.e. frag-
ment number) resulting from multiple hard parton scat-
ters (MPIs). The PMC is tuned to accommodate a spe-
ciﬁc subset of currently available data volumes and anal-
ysis methods, referred to as “key experimental data” [8].
This study contrasts a deductive approach based on
a priori assumptions (PMC) leading to predictions for
certain preferred observables with an inductive approach
based on a self-consistent phenomenological description
(TCM) of all information derivable from all available
data, expressed via the simplest algebraic formalism.
This article is arranged as follows: Section II intro-
duces the PYTHIA Monte Carlo and MPIs in the con-
text of the TCM. Section III describes the relation of
the PMC to certain data features conventionally em-
ployed for design and testing of that Monte Carlo. Sec-
tion IV presents a PMC-TCM model comparison strat-
egy. Section V reviews the TCM with illustrations from
p-p spectrum data. Section VI summarizes the relation of
minimum-bias (MB) jets to MPIs. Section VII considers
the underlying event (UE) and its relation to MB dijets.
Sections VIII and IX present discussion and summary.
II.
PYTHIA MONTE CARLO AND MPIs
The PMC has been applied broadly to simulations
of high-energy p-p and p-¯p collisions.
It was ﬁrst for-
mulated in the mid eighties in response to high-energy
data obtained from newly-constructed collider accelera-
tors. The PMC was conﬁgured to describe and explain
certain data features emerging from initial analysis of col-
lider data and includes several novel assumptions about
high-energy nuclear collisions. In this section PMC struc-
ture and development history are brieﬂy reviewed in the
context of the TCM.
A.
PYTHIA and related MC models
Historical development of the PMC is summarized in
Refs. [8, 9] which, taken together, provide some indica-
tion of its continuing development in recent years. The
initially introduced PMC served as a response to in-
formation newly obtained from the intersecting storage
rings (ISR) and the super proton-antiproton synchrotron
(Sp¯pS) by the mid eighties, especially strong jet contri-
butions to various collision manifestations. At that time
three issues dominated: hard parton scattering to form
eventwise-reconstructed dijets, soft (multi)Pomeron de-
scriptions of the underlying event (UE, complement to a
triggered hard dijet) and UA1 minijets [10].
Several outstanding data features drew attention: (a) a
broad minimum-bias (MB) distribution P(nch) on charge
multiplicity nch, its width increasing substantially with
collision energy, (b) ensemble-mean ¯pt(nch) increasing
strongly with nch (whereas the opposite trend had been
observed at lower energies), (c) correlated variation of
the UE with increasing jet trigger energy – the so called
pedestal eﬀect – and (d) strong “forward-backward” cor-
related ﬂuctuations of nch in separated pseudorapidity η
intervals. Those eﬀects could not be accommodated by
a simple model of hard jet plus soft Pomeron exchange.
The PMC approach was based on a uniﬁed descrip-
tion applicable to triggered hard jets, UA1 minijets and
the UE based on multiple interactions [9] or multipar-
ton interactions (MPIs) [8] wherein almost all hadrons
from almost all events arise from large-angle scattering
of constituent partons as described by pQCD. A trig-
gered hard jet is simply the most energetic MPI in an
event, UA1 minijets correspond to lower-energy MPIs,
and the UE is the complementary MPI spectrum extend-
ing down to low pt.
MPIs are said to arise naturally
from the composite nature of projectile protons lead-
ing to large nonPoisson ﬂuctuations and other notable
data features. The model excludes any necessity for soft
physics via Pomeron exchange except for a small minor-
ity of diﬀractive events (i.e. including no MPI) which are
modeled by a cut Pomeron or pair of strings connect-
ing valence quarks and diquarks in projectile protons.
Given that system “...it [was] possible to obtain a quite
reasonable description of essentially all the key experi-
mental data...” [8] [emphasis added]. The PMC assumes
exchange of colored objects, requiring complex color con-
nections via strings, whereas momentum transfer could
be dominated by soft and hard Pomerons [11, 12]. The
only color connection might then be between scattered
partons and their parent nucleons.
Further reﬁnement of the PMC lead to the following:
“In summary, most if not all of MB and UE physics
at collider energies is explained and reasonably well de-
scribed once the basic MPI framework has been comple-
mented by (a) a smooth turnoﬀof the [jet] cross section
for p⊥→0, (b) a requirement to have at least one MPI to
get an event, (c) an impact-parameter dependence [based
on the eikonal approximation applied to p-p collisions],
and (d) a colour reconnection mechanism [labels added].”
Reference [9] points out that “...a sound understanding of
multiple interactions [MPIs] is prerequisite for precision
physics involving jets and/or the underlying event.”
Although data features (a) through (d) were fairly well
accommodated by the PMC there remained outstanding
issues: The pt spectrum was underestimated at lower pt
and “...high-multiplicity pp events have properties similar
to those observed in heavy-ion AA collisions” [8] such as


## Page 3


3
(i) multistrange baryon enhancement, (ii) higher fraction
of heavy hadrons, (iii) ¯pt larger for heavy hadrons, (iv)
Lambda/kaon ratio has a peak near pt = 2.5 GeV/c, (v)
ridge on both sides of same-side jet peak, (vi) possible
azimuthal ﬂow v2 similar to A-A data. It was suggested
that “...plausible explanations start out from a MPI pic-
ture and add some kind of collective behaviour [a QGP-
like state within p-p collisions?] among the MPIs” [8].
B.
Multiparton interactions – MPIs
A signature element of the PMC is multiparton inter-
actions or MPIs, a concept motived as follows: Because
of the composite structure of protons (especially low-x
partons) several pairs of partons may collide (within a
p-p event), denoted by multiple interactions (scatterings).
“Viewing hadrons as ‘bunches’ of incoming partons, it
is apparent that when two hadrons collide it is possible
that several distinct pairs of partons collide with each
other...” [9]. “...most inelastic [p-p] events...are guaran-
teed to contain several perturbatively calculable [sic] inter-
actions” [13]. Thus, MPIs must exist and would lead to
more “activity” in the UE as apparently required by data.
“The crucial leap of imagination is to postulate that all
particle production in inelastic hadronic collisions derives
from the multiple-interactions [MPIs] mechanism. ...the
starting point is perturbative” [9].
The PMC is therefore a one-component model: almost
all hadrons must emerge from a hard component con-
sisting of MPIs (i.e. QCD jets). And for any non-single-
diﬀractive (NSD) p-p event “...each event has to have at
least one [partonic] interaction [MPI]...” [9].
The conventional pQCD jet-spectrum formula as-
sumed to represent MPIs within the PMC is [8]
dσ
dp2
t
= Σijk
Z
dx1dx2dˆt fi(x1, Q2)fj(x2, Q2)
(1)
×dˆσk
ij
dˆt δ

p2
t −
ˆtˆu
ˆs

.
Parton distribution functions (PDFs) f(x, Q2) are pre-
sumably ﬁxed mean-value distributions randomly sam-
pled within the PMC, an approach that can be ques-
tioned based on available data as mentioned in Sec. IV A.
If almost all ﬁnal-state hadrons are to be represented
by MPIs in the PMC the MPI spectrum must extend to
very low parton pt →ptmin where a perturbative for-
mulation may be questioned. One may ask how a very-
low-momentum parton might fragment to hadrons in the
context of measured fragmentation functions (FFs) from
the HERA, LEP and Fermilab [7].
Nevertheless, it is
assumed that MPIs dominate p-p hadron production.
Introduction of the PMC represented a transition from
a (multi)Pomeron-exchange description of soft events to
a formulation of multiple pQCD interactions (MPIs) that
combines MB (i.e. jet spectrum) and UE aspects: “The
p⊥0 [∼ptmin] parameter has to be chosen accordingly
small — since now the concept of no-interaction [no
MPI] low-p⊥events is gone...” [9]. “A hard-process event
would just be the high-p⊥tail of the MB class, and a soft-
process event just one where the hardest jet was too soft
to detect as such [by eventwise reconstruction]” [8].
The total cross section for MPIs is then the integral
σint(ptmin) =
Z s/4
p2
tmin
dp2
t
dσ
dp2
t
,
(2)
and the mean number of MPIs per NSD p-p collision is
¯nMP I(ptmin) = σint(ptmin)
σNSD
,
(3)
with the assumption ¯nMP I(ptmin) ≥1 establishing a con-
straint (upper limit) on ptmin. “At least one interaction
[MPI] must occur when two hadrons pass by for there to
be an event at all” [8]. It is assumed that MPIs are inde-
pendent (Poisson distributed) except for energy conser-
vation. The adopted assumption that almost all hadrons
proceed from MPIs suggests that nch ∝¯nMP I(ptmin),
but that leads to problems with observations that ¯pt(nch)
increases strongly with nch (see Sec. III B on color re-
connection for proposed resolution). A review of MPI-
related results from the LHC is presented in Ref. [14].
Other signiﬁcant issues for initial versions of the PMC
were (a) how to cut oﬀthe MPI spectrum: “A sharp
[pt] cutoﬀ, below which cross sections vanish [as for UA1
minijets at 5 GeV [10]], is not plausible” [8],1 (b) how to
deal with “soft” events seeming to have no MPIs, (c) how
to introduce a p-p impact parameter, and (d) how to scale
the model with p-p collision energy. Item (a) was resolved
with a soft cutoﬀin which pt →0 was permitted but
with increasing deviation from Eq. (1) below some cutoﬀ
parameter p⊥0 adjusted to accommodate data. The sup-
porting argument was based on the inability of lower-pt
gluons to resolve color charges.
Item (c) was resolved
by applying a geometric Glauber model with eikonal ap-
proximation to p-p collisions: “MPIs can be viewed as
occurring simultaneously in diﬀerent parts of the [p-p]
overlap region” [8].
C.
Two-component model: alternative viewpoint
As noted, the PMC is essentially a one-component
model (OCM, hard component only): almost all hadron
production arises from a single mechanism—production
of MPIs by pQCD-described large-angle parton scatter-
ing. In the same context the currently most-popular de-
scription of more-central A-A collisions at RHIC and the
1 The 5 GeV cutoﬀreﬂects a measurement limitation, not an as-
sumed limit to the physical jet spectrum. Spectrum data suggest
that the eﬀective lower limit for hadron jets is near 3 GeV [15, 16].


## Page 4


4
large hadron collider (LHC) is also a OCM (soft compo-
nent only) in that almost all hadrons are said to emerge
by “freezeout” from a locally-thermalized ﬂowing dense
medium or QGP. As a OCM the PMC can be contrasted
with the two-component combination of hadron produc-
tion within the TCM as applied within this study.
A two-component model separately describing soft and
hard processes was proposed in 1985 for Sp¯pS data [17],
essentially concurrent with introduction of the PMC.
A soft component representing the majority of pro-
duced hadrons was retained. However, it was intended
to “...separate the mini-jet contribution from the bulk
of many-parton interactions [soft component]” in re-
sponse to the following issues: (a) KNO scaling viola-
tions, (b) rise of NSD cross section, (c) increase of ¯pt
with nch, (d) rise of the “central plateau” and hence
log2(s) scaling of nch.
log2(s) scaling (hard, gluon
bremsstrahlung) was distinguished from log(s) scaling
(soft, quark bremsstrahlung) observed at lower energies.
With the startup of the hadron-electron ring acceler-
ator (HERA) and large electron-positron collider (LEP)
knowledge about jet production and nucleon structure
increased rapidly after 1990. In addition, operation of
the alternating gradient synchrotron (AGS) and super
proton synchrotron (SPS) in heavy-ion mode and prepa-
rations for operation of the relativistic heavy ion col-
lider (RHIC) led to major advances in the description of
nucleus-nucleus (A-A) collisions during the nineties. In-
cluded in that eﬀort was production of the HIJING MC
model for A-A collisions based on the p-p PMC coupled
with a TCM for hadron production in A-A collisions [18].
In Ref. [19] the TCM was summarized in comparison with
a gluon saturation model following the startup of RHIC.
The current TCM, with hard and soft components, is
intermediate between two extremes.
As demonstrated
in Sec. V the TCM is a simple inductive model based on
inference from a broad array of data. The PMC is a com-
plex deductive model based on certain a priori assump-
tions and includes an array of parameters adjusted to
accommodated a limited subset of data manifestations.
A previous study of p-p collision dynamics [20] fo-
cused on UE-related experimental methods and results
in the context of the TCM without emphasis on theoret-
ical Monte Carlos. The present study is essentially the
complement: direct comparison of the PMC and TCM
against a range of established and currently-available
analysis methods and data. The next section considers
the PMC within the context of selected p-p data features
and interpretations that motivated its development.
III.
CANONICAL DATA INTERPRETATIONS
Certain analysis methods and associated data features
have been emphasized in design and application of the
PMC and continue to be used for that purpose de-
spite more-recent alternatives.
As noted in Sec. II A
data features include (a) increasing width of multiplicity
distribution P(nch) with collision energy, (b) ensemble-
mean ¯pt increasing strongly with nch, (c) a triggered-
jet pedestal eﬀect on azimuth associated with the UE
and (d) long-range FB correlations indicating nonPoisson
ﬂuctuations. “...the broadening multiplicity distribution
and the strong forward-backward correlations oﬀer ...ev-
idence... strongly suggesting that the bulk of events have
several [MPIs]. We are not aware of any realistic alter-
native explanations for either of the observables” [9].
A.
Multiplicity distributions P(nch)
A major stimulus for introduction of MPIs as a basis
for the PMC was the increasing width of p-p multiplic-
ity distribution P(nch) = dP/dnch as CM collision en-
ergies increased, especially with the introduction of col-
lider accelerators. The increasing nonPoisson behavior
was identiﬁed with so-called KNO scaling [21].
“...al-
lowing at most one interaction [MPI] in p¯p events [and
assuming e+-e−hadronization] there is no (known) way
to accommodate the experimental multiplicity distribu-
tions [KNO scaling].... Either hadronization is very dif-
ferent in hadronic events from e+-e−ones, or one must
accept multiple interactions [MPIs] as a reality” [9].
KNO scaling is the hypothesis that p-p multiplicity n
distributions in the form ¯nP(n) vs n/¯n →Q(z) vs z
with z = n/¯n are approximately independent of collision
conditions, reﬂecting nonPoisson ﬂuctuations. While the
KNO trend seemed to describe ISR data substantial de-
viations were noted at higher energies. The signiﬁcance
of apparent KNO trends in p-p data was questioned in
Ref. [22] where it was pointed out that KNO scaling
is equivalent to invariance of statistical moments in the
form Cn = n2/¯n2, and the trend may be accidental.
Over a broad energy range P(n) data are accurately
described by the negative binomial distribution (NBD)
with parameters µ = ¯n and k [23].
Fluctuations can
be represented in the NBD context by σ2
n/¯n = 1 + ¯n/k.
Poisson ﬂuctuations correspond to 1/k →0. The KNO
hypothesis corresponds to C2 −1 ≈1/¯n + 1/k ≈con-
stant.
The ﬁrst term decreases strongly with collision
energy. KNO scaling thus implies that the second term,
representing nonPoisson ﬂuctuations, must be rapidly in-
creasing with collision energy in such a way that the sum
is approximately constant.
Reference [22] also points
out that p-p data at higher energies are consistent with
1/k ≈−0.104 + 0.058 ln(√s) ≈0.06 ln(√s/6 GeV). 1/k
then dominates C2 at higher energies and breaks KNO
scaling which is apparently a coincidence within the en-
ergy range of the ISR. However, the energy dependence
of 1/k has important implications for jet systematics as
described in Sec. VI D. In eﬀect, NBD ﬂuctuation mea-
sure 1/k can provide a constraint on MB jet spectra.


## Page 5


5
B.
Ensemble-mean pt and color reconnection
A second major inﬂuence on development of the PMC
was the trend of ¯pt vs nch at higher collision energies.
The trend at lower energies had been decrease, consis-
tent with momentum conservation. The trend observed
at and above ISR energies was strong increase for untrig-
gered or MB events, whereas events triggered with a (re-
constructed) jet exhibited ¯pt ≈constant. Since the only
mechanism for transport from longitudinal to transverse
phase space in the PMC is MPIs a problem then arises in
attempts to represent the increasing ¯pt(nch) trend. Sup-
pose Pt represents total pt integrated within some accep-
tance ∆η which also includes total charge nch. Then for
hadron production from independent MPIs per the PMC
¯Pt ∝¯nMP I(ptmin)
(4)
nch ∝¯nMP I(ptmin)
¯pt ≡
¯Pt/nch ≈constant.
If MPIs are independent systems then ¯pt(nch) is necessar-
ily constant within the PMC. An additional mechanism
is required to reproduce the observed ¯pt(nch) trend.
The response was color reconnection (CR): “To obtain
a rising ¯pt(nch) it is therefore essential to have a mecha-
nism to connect the diﬀerent MPI subsystems in colour,
not only at random but speciﬁcally so as to reduce the
total string length [and hence hadrons per string] of the
event, more and more the more MPIs there are [empha-
sis added]. Each further MPI on the average then con-
tributes less nch than the previous, while still the same
(semi)hard pt kick is to be shared between the hadrons,
thus inducing the rising trend.
This is precisely what
[color reconnection] is intended to do. It is the ﬁrst large-
scale application of colour reconnection (CR) ideas....”
By introducing a CR mechanism “Not only the slope but
also the absolute value of ⟨p⊥⟩[¯pt] is well reproduced,
without any need to modify the fragmentation pt width
tuned to e+-e−data.” The “...CR [mechanism] was es-
sential to obtain a rising ¯pt(nch), and that has remained
a constant argument over the years, still valid today: sep-
arate MPIs must be colour-connected in such a way that
topologies with a reduced λ measure...are favoured” [8].
CR determines how MPIs will hadronize in a correlated
way via a string mechanism: “Interactions gg →gg [are
conﬁgured] such that...each of the gluons is connected to
one of the strings ‘already’ present.” A color connection
“...which minimizes the total increase in string length is
chosen” [9] “...the λ measure is used to pick such recon-
nections.... A free strength parameter [λ, emphasis added]
is introduced to regulate the fraction of [scattered parton]
pairs that are being tested in this way. With this further
mechanism at hand it now again becomes possible to de-
scribe ¯pt(nch) data approximately” [8].
However, it is
cautioned that “Neither of these three [color connection
rules] follow naturally from any colour ﬂow rules...” [8].
The combination of ptmin and CR represents an ad
hoc reconﬁguration of the MB parton spectrum per
Eqs. (1) and (2) and the systematics of parton fragmen-
tation (modeled within the PMC by a string fragmen-
tation mechanism). But parton fragmentation is repre-
sented by measured fragmentation functions (FFs) as in
Refs. [7, 15], and eﬀective jet spectra (i.e. as manifested
by detected jet fragments) for various collision systems
have also been measured [15]. The PMC MPIs and CR
mechanism as summarized above eﬀectively redeﬁne the
MB jet spectrum and FFs (based on the density of scat-
tered partons) with free parameters used to match ¯pt
data. There is no guarantee that such a system is correct
within a QCD context or in comparison to other data.
C.
Triggered-jet pedestal eﬀect and the UE
A third major inﬂuence on development of the PMC
has been the so-called “pedestal eﬀect” – strong correla-
tion between an imposed jet trigger condition and a fea-
ture of the underlying event or UE. Triggered events in-
cluding a hard dijet show increased “activity” or particle
and momentum production (the pedestal) near the mid-
point between jet cones at φ∆= φ1−φ2 ≈π/2 (the trans
region or TR [24]). The pedestal increases up to trigger
condition Ejet ≈5 GeV and then saturates.
“Events
containing a hard jet also have an above-average level of
particle production well away from the jet core [emphasis
added], the ‘pedestal eﬀect’ ...The pedestal eﬀect is well
described, and explained [by the PMC tuned to data].
The rise is caused by a shift in the composition of events,
from one dominated by fairly peripheral collisions to one
strongly biased toward central ones” [8].
A more detailed and recent theoretical description is
as follows [25]. Hard particle production (i.e., large-angle
gluon scattering to dijets) should be most probable at
small p-p impact parameter because the transverse size of
the low-x gluon distribution in the proton inferred from
DIS data is substantially smaller than the overall pro-
ton size. “Soft” particle production (not associated with
a triggered dijet, i.e. MPIs in the context of the PMC)
should vary with b over a large range. Speciﬁcally, trans-
verse multiplicity N⊥(perpendicular to a trigger-particle
momentum and therefore to a dijet axis) may be strongly
correlated with b. It is assumed that jet production is
correlated with smaller b and therefore larger N⊥.
Indirect selection of jets may be established with a sin-
gle trigger-particle pt condition denoted by pt,trig. For
suﬃciently high pt,trig b should be relatively small and
nearly independent of the trigger condition.
Equiva-
lently, transverse multiplicity N⊥should be nearly in-
dependent of pt,trig and substantially larger than for
NSD p-p collisions. Reference [25] then poses the ques-
tion (given the several assumptions): above what critical
pt,trig value is hadron production dominated by “hard”
parton-parton interactions in more-central p-p collisions?
The assumption that an azimuth interval exists “well
away from the jet core[s]” – equivalent to the assump-
tion of “zero yield at minimum” or ZYAM invoked for


## Page 6


6
some analyses of triggered-jet azimuth correlations [26] –
is questionable [27]. As demonstrated in Sec. VII B, al-
though a high-energy dijet may appear to be concentrated
in two well-separated “cones” it must contribute substan-
tially to all azimuth regions. The relevance of centrality
to p-p collisions and the suggestion that protons appear
smaller in diameter at lower x whereas the opposite is
expected from Gribov diﬀusion [28] can be questioned:
reference [8] notes that “low-x partons should diﬀuse
out in b [r] during the evolution [splitting cascade] down
from higher-x ones.” UE analysis is discussed further in
Sec. VII. The p-p pedestal eﬀect and other interpretations
relating to the UE are also considered in Ref. [20].
D.
Long-range FB correlations on pseudorapidity
A fourth major inﬂuence on development of the PMC
was forward-backward (FB) correlations on pseudora-
pidity η.
“Long-range” FB correlations are measured
by Pearson’s normalized covariance [29, 30] bF B
≡
σ2
nF nB/
p
σ2nF σ2nB, where σ2
nF nB = nF nB −¯nF ¯nB is the
covariance of ﬂuctuating charges nF and nB in two η
bins nominally symmetric about midrapidity and sepa-
rated by some η interval (gap). (The σ2
nX are variances
within the individual bins.) Observed non-Poisson FB
correlations represent angular correlations spanning sub-
stantial intervals on η and therefore requiring a global
source mechanism. Within the PMC context the source
of such global ﬂuctuations is attributed to MPIs: “¯nMP I
is a kind of global quantum number of the event” [8]. FB
correlations are described as surprisingly large for ∆η
separations (gaps) over several units.
Statistical measure bF B as deﬁned above represents a
subset of all p-p angular correlations which have by now
been studied in considerable detail [3, 31, 32]. A more
general measure is ∆ρ/√ρref ∼σ2
nF nB/√¯nF ¯nB [3, 30,
33] where the statistical reference is represented by Pois-
son values for the two variances. That covariance density
distribution can be determined on a 2D binned system of
diﬀerence variables η∆= η1 −η2 and φ∆= φ1 −φ2.
Several correlation components are then resolved and
may be attributed to distinct hadron production mech-
anisms [3, 33, 34]. Even when extended to multiple η∆
values the 1D projection bF B(η∆) from 2D (η∆, φ∆) is
unable to establish such distinctions. While MB dijets
do represent a substantial contribution to angular corre-
lations details of measured angular-correlation structure
appear inconsistent with the hypothesis of multiple MPIs
per event and its implementation in the PMC [3, 15, 35].
IV.
MODEL COMPARISON STRATEGY
According to Refs. [8, 9] the PMC is a p-p OCM assum-
ing that most hadron production arises from scattered
partons fragmenting to jets (MPIs, hard component) and
any soft component is negligible. The ﬂow-QGP OCM
for A-A collisions asserts that almost all hadron produc-
tion is soft (freezeout from a thermalized QCD medium)
and any jet contribution comprises a small minority. The
TCM with soft and hard components oﬀers a compre-
hensive intermediate description. This section presents a
strategy for further comparisons.
A.
Speciﬁc model diﬀerences
The PMC by assumption includes no element(s) com-
parable to the TCM soft component.
The scattered-
parton pt spectrum extends down to zero, and the de-
tailed spectrum shape for smaller pt is tuned (via some
p⊥0) to match data within the PMC set of assumptions.
In order to describe ¯pt vs nch data a CR mechanism is
introduced that includes free parameter λ adjusted to
accommodate such data. The CR mechanism in eﬀect
creates a freely adjustable FF ensemble.
The PMC further assumes that p-p centrality is rele-
vant and can be modeled via a geometric Glauber model
based on the eikonal approximation. p-p centrality vari-
ation coupled with MPIs as the dominant hadron source
provide the principal source of ﬂuctuations. The relation
of MPIs to p-p centrality and hadron production should
lead to coupling between an imposed jet trigger and UE
production, as evidenced by the so-called pedestal eﬀect.
The TCM, inferred from observed nch dependence of
pt spectra and two-particle correlations, describes hadron
production in terms of a greater source (soft component)
arising from projectile-nucleon dissociation and a lesser
source (hard component) arising from MB dijets. The
soft component has universal properties including a L´evy
shape and slope parameter T ≈145 MeV [3, 15]. The
hard component (MB fragment distribution) is predicted
by a convolution of measured FFs and measured jet spec-
tra not adjusted to accommodate p-p pt spectrum data.
The eﬀective lower bound of the jet spectrum is the sin-
gle free parameter: spectrum data require a lower bound
near 3 GeV for all currently-accessible p-p collision ener-
gies [16, 36] consistent with analysis of jet spectra [15].
The precisely-determined quadratic relation between
TCM soft and hard components, persistent over a large
range of parton densities, precludes any role for collision
centrality.
In any p-p collision all participant partons
may freely interact in any combination. There is no re-
stricted “overlap region,” and the eikonal approximation
is not relevant to parton-parton interactions. Given the
noneikonal quadratic soft/hard relation and no centrality
(impact parameter b) variation, ﬂuctuations must arise
from soft-component production within individual pro-
jectile protons, suggesting that the mechanism is varying
depth on momentum fraction x of parton splitting cas-
cades, i.e. strong eventwise ﬂuctuation of nucleon PDFs.


## Page 7


7
B.
Relations among several forms of data
Certain relations among analysis methods and data
formats are relevant to the PMC-TCM comparison. The
TCM for ¯pt data [37] is simply related to the TCM for
pt spectra [2, 3]. The TCM spectrum hard component is
in turn directly and quantitatively related to measured
FFs [7, 15] and measured MB jet spectra [15] via a con-
volution integral [16]. Two-particle correlations [31, 32],
both (yt, yt) correlations and 2D angular correlations on
(η, φ), are described quantitatively by the TCM [3]. Soft
and hard components of (yt, yt) correlations correspond
directly to yt spectrum TCM (projection from 2D to 1D).
TCM soft and hard components are clearly distin-
guished by nch dependence, pt dependence, √s depen-
dence and correlation structure as demonstrated in sev-
eral studies [2, 3, 32, 36, 37]. The hard components of
spectra and two-particle correlations, corresponding di-
rectly to MB dijets, represent a minority fraction of total
hadron production. The majority fraction must then be
a nonjet contribution, i.e. the TCM soft component.
C.
Improved comparison strategy
This study emphasizes two themes: (a) reexamine mid-
eighties collider data trends invoked as motivating or sup-
porting the PMC at its inception and (b) present evi-
dence from more-recent data and interpretations against
basic assumptions of the PMC. Certain data features de-
scribed in Sec. II A, inferred from ISR and Sp¯pS data
and more recently from Fermilab and referred to as “key
experimental data” [8], have been favored for subsequent
development and support of the PMC. A large body of
additional data and methods relating to p-p, p-A and
A-A collisions and emerging in the intervening period
at the RHIC and LHC appear to be underemployed.
The present study extends model comparisons to bet-
ter utilize available data. Several topics are emphasized:
(a) quantitative relations between TCM soft and hard
components, (b) quantitative understanding of MB di-
jets in various manifestations, (c) UE systematics and
the pedestal eﬀect, (d) p-p collision geometry – relevance
thereof – and (e) ﬂuctuations and their sources.
Section V introduces details of the TCM and its rela-
tion to data to provide context for further comparisons.
The relation between the p-p TCM in isolation and a p-N
TCM within more-complex p-A collisions is emphasized.
Section VI compares arguments for conjectured MPIs
to experimentally-observed MB dijets.
Measured jet
spectra and fragmentation functions are linked directly
and quantitatively via convolution integral to pt spec-
trum hard components. That connection places a lower
bound on jet energy spectra that contradicts PMC as-
sumptions. It also challenges assumptions about the con-
jectured role of a CR mechanism and implicit variation
of FFs with scattered-parton density. MB dijet system-
atics and the relation between TCM spectrum soft and
hard components conﬂict with a PMC assumption about
p-p centrality. MB dijet cross sections imply that a ma-
jority of p-p events (soft) include no signiﬁcant jet struc-
ture (MPIs), consistent with the measured rate of double
parton scattering. The relation of the ¯pt statistic to pt
spectrum structure is evident. Variation of ¯pt with nch is
then simply explained within the TCM context in terms
of MB dijet properties and noneikonal p-p collisions.
Section VII considers assumed access to the UE and
its inferred properties in the context of the TCM and
MB dijets. In support of the PMC it is argued that re-
sponse of UE activity to a jet trigger signals the presence
of MPIs and relevance of p-p centrality. However, mea-
sured properties of MB dijets reveal a strong triggered-jet
contribution to the azimuth TR, i.e. the increased par-
ticle production referred to in the PMC context. Both
the N⊥yield within the TR and the dN⊥/dpt spectrum
are accurately predicted by the TCM based on measured
MB dijet properties and pt spectra.
A notable result:
application of a jet pt trigger does not change the soft
component, arguably the actual UE. There is no cou-
pling between an applied jet trigger and p-p centrality.
The role of ﬂuctuations is considered brieﬂy in Sec. VIII.
V.
TCM FOR p-p AND p-N COLLISIONS
As an introduction to the TCM the nch dependence of
pt spectra from 200 GeV p-p and 5 TeV p-Pb collision
systems is analyzed diﬀerentially.
Spectrum systemat-
ics are related to two-particle correlations on (yt, yt) and
(η∆, φ∆) to support interpretation of soft and hard TCM
components. Hard/soft ratio trends reveal a quadratic
relation between MB dijet production and soft hadron
production. In App. A a TCM parametrization directly
related to fundamental QCD processes spans a range of
collision systems to describe all data within their uncer-
tainties. In App. B the hadron density distribution on
η within |η| < 1 is decomposed into soft and hard com-
ponents. Some TCM results relevant to the PMC are:
(a) a TCM soft component representing a majority of
produced hadrons is required by data, (b) p-p centrality
is not relevant and (c) spectrum hard components are
isolated for comparison with measured jet properties.
A.
TCM description of p-p pt or yt spectra
The TCM for p-p collision data emerged from analysis
of 200 GeV pt spectrum data. Systematic analysis of the
nch dependence of pt spectra from 200 GeV p-p collisions
described in Ref. [2] led to a compact phenomenological
TCM with approximate factorization of multiplicity nch
and transverse-rapidity yt dependence in the form
d2nch
ytdytdη ≈¯ρ0(yt) = Spp(yt, nch) + Hpp(yt, nch) (5)
≈¯ρs(nch) ˆS0(yt) + ¯ρh(nch) ˆH0(yt)


## Page 8


8
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
1
2
3
4
yt
ρ0′(yt) / ρs
200 GeV p-p
S0
αρsH0(yt)
NSD
n = 1-6
10
-4
10
-3
10
-2
10
-1
1
2
3
4
yt
(1/αρs) [ρ0′(yt) / ρs − S0′(yt)]
H(yt) / αρs
2
n = 1-6
1/pt7
FIG. 1:
Left: Hadron yt spectra for six multiplicity classes of
200 GeV p-p collisions (thin curves) compared to ﬁxed refer-
ence ˆS0(yt) (bold dotted) [3]. Spectra ¯ρ′
0 are uncorrected for
low-pt ineﬃciencies (yt < 2). The bold dashed curve is the
corresponding hard-component model α¯ρs ˆH0(yt) for NSD p-p
collisions. Right: Hard-component distributions inferred from
spectra at left in the form H(nch, yt)/¯αρ2
s (several line styles)
compared to ﬁxed reference ˆH0(yt) (bold dashed). The dash-
dotted line in each panel indicates a power-law trend ≈1/p7
t
corresponding to the underlying 200 GeV jet energy spectrum.
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
trum [15]. Transformation from pt or mt to yt is simply
accomplished with Jacobian ptmt/yt.
Integration of Eq. (5) over yt results in the angular-
density TCM ¯ρ0 = ¯ρs+¯ρh. Spectrum [2, 36] and angular-
correlation [3] data reveal that soft and hard angular den-
sities are related by ¯ρh ≈α¯ρ2
s with α ≈0.006 within
∆η = 2 at 200 GeV. The two relations are equivalent
to a quadratic equation that uniquely deﬁnes ¯ρs and ¯ρh
in terms of ¯ρ0 (when corrected for ineﬃciencies). That
quadratic relation is valid over a ¯ρs interval correspond-
ing to 100-fold variation of MB dijet production [2, 3].
Figure 1 (left) shows uncorrected yt spectra for six p-p
multiplicity classes averaged over acceptance ∆η = 2 and
normalized by soft-component density ¯ρs = ns/∆η [3].
The bold dotted curve is soft-component L´evy model
ˆS0(yt) with model parameters T = 145 MeV and n =
12.5 [36]. The L´evy model is slightly modiﬁed at lower pt
(< 0.5 GeV/c) to match data tracking ineﬃciency there.
Figure 1 (right) shows hard-component data in-
ferred from the left panel via Eq. (5) in the form
Hpp(yt, nch)/α¯ρ2
s (thin curves) compared to a ﬁxed Gaus-
sian model function in the form ˆH0(yt) (bold dashed)
with centroid ¯yt ≈2.65 and width σyt ≈0.45 and with
coeﬃcient α ≈0.006 determined by the data-model com-
parison. Note that from a TCM analysis of pt spectra the
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
5 TeV p-Pb
200 GeV
5 TeV
10
-4
10
-3
10
-2
10
-1
1
2
3
4
yt
[X(yt) − S0(yt)] / x(ns) ν(ns)
H0
200 GeV
5 TeV
FIG. 2:
Left: Corrected identiﬁed-pion spectra for 5 TeV
p-Pb collisions from Ref. [39] transformed to yt with Jacobian
ptmt/yt and normalized by TCM values for Npart and ¯ρsNN
from Ref. [37] (7 thinner curves). ˆS0(yt) (bold dotted) is the
universal soft-component model. Right: Diﬀerence X(yt) −
ˆS0(yt) normalized by x(ns)ν(ns) = α¯ρsNNν(ns) using TCM
values from Ref. [37] (thin curves). The bold dashed curve
is the hard-component model ˆH0(yt) with exponential tail.
Thinner dotted and dashed curves denote 200 GeV models.
hard component (MB jet-fragment distribution) is explic-
itly determined for direct comparison with measured di-
jet properties and constitutes a minority of total hadron
production in all cases. In contrast, the PMC “hard com-
ponent” (MPIs) must represent the entire pt spectrum.
The p-p spectrum TCM can be extended to p-A colli-
sions assuming that dijet production is unchanged in the
more-complex p-A system. To do so requires determina-
tion of p-A centrality in the form of participant-nucleon
(N) number Npart and N-N binary-collision number Nbin
to isolate individual p-N collisions. The mean number of
binary collisions per participant pair is ν ≡2Nbin/Npart.
For the p-Pb centrality study in Ref. [38] centrality was
inferred from the systematics of ¯pt vs nch data [40].
Figure 2 (left) shows identiﬁed-pion spectra from 5 TeV
p-Pb collisions [39].
The published spectra have been
multiplied by 2π to be consistent with η densities as in
Fig. 1 and transformed to yt with Jacobian ptmt/yt. The
spectra are then normalized by soft-component density
¯ρs = (Npart/2)¯ρsNN as reported in Table II of Ref. [38],
except that an additional factor 0.8 is applied to ¯ρs val-
ues to reﬂect the pion fraction of soft hadrons.
Nor-
malized spectra X(yt) are then compared with spectrum
soft-component model ˆS0(yt) (bold dotted curve): a L´evy
model with parameters T = 145 MeV and n = 8.3 ap-
propriate for 5 TeV p-p collisions as reported in Ref. [36].
The 200 GeV soft component is included for comparison.
Figure 2 (right) shows diﬀerence X(yt) −ˆS0(yt) nor-
malized by x(ns)ν(ns) = α¯ρsNNν(ns) with TCM values
reported in Ref. [37] and Table II of Ref. [38]. The re-
sult should be directly comparable to the p-p spectrum
hard-component model in the form ˆH0(yt) with model
parameters (¯yt, σyt, q) = (2.65, 0.59, 3.9) for 5 TeV p-p
collisions as reported in Ref. [36]. The bold dashed curve
is ˆH0(yt) with (¯yt, σyt, q) →(2.45, 0.605, 3.9). A shift to
lower fragment momenta for pions is expected based on


## Page 9


9
Fig. 7 (left) of Ref. [7]: pion FFs are softer than kaon
FFs are softer than proton FFs.
The 200 GeV hard-
component model (for unidentiﬁed hadrons as in Fig. 1)
is included for comparison. The overall TCM description
is well within point-to-point data uncertainties except for
the lowest centrality class (solid curve) where the large
deviation is expected based on Ref. [36]. The TCM de-
scription of p-Pb spectra assumes linear superposition of
p-N collisions within p-Pb collisions.
However, it also
describes realistically the changing properties of p-N col-
lisions depending on an applied p-Pb nch condition.
In summary, the pt spectrum TCM is an accurate rep-
resentation of data from several collision systems based
on two simple QCD-based hadron production mecha-
nisms. Evolution of the TCM (and data) from 200 GeV
p-p to 5 TeV p-Pb is fully consistent with smooth log(√s)
dependences expected for QCD phenomena, as reported
in Refs. [36–38]. The independent energy evolution of soft
and hard spectrum TCM components is notable.
B.
Two-particle correlations
For a self-consistent data description the TCM for pt
spectra should have a corresponding description for two-
particle correlations: both (pt, pt) or (yt, yt) correlations
and angular correlations on (η, φ) formulated in terms of
diﬀerence variables η∆and φ∆deﬁned in Sec. III D.
Figure 3 (left) shows correlations on (yt, yt) from 200
GeV NSD p-p collisions for pt ∈[0.15, 6] GeV/c (yt ∈
[1, 4.5]) [31, 32]. Two peaked features are identiﬁed as
TCM soft and hard components as follows. The lower-yt
peak falls mainly below 0.5 GeV/c (yt < 2) and consists
exclusively of unlike-sign (US) pairs. Corresponding an-
gular correlations consist of a narrow 1D peak on η∆
centered at the origin. The combination suggests longi-
tudinal fragmentation of low-x gluons to charge-neutral
hadron pairs closely spaced on η and consistent with spec-
trum soft component Spp(yt, nch) in Eq. (5). The higher-
yt peak extends mainly above 0.5 GeV/c with mode near
pt = 1 GeV/c (yt ≈2.65) and is consistent with hard
component Hpp(yt, nch) in Eq. (5) and Fig. 1 (right).
Figure 3 (right) shows angular correlations for the
same collision system with the condition pt ≈0.6 GeV/c
(yt ≈2.15), i.e. near the lower boundary of the (yt, yt)
hard component in the left panel. Despite the low hadron
momentum the observed angular correlations exclude a
contribution from the soft component (see Sec. VII B),
exhibiting only structure expected for jets: a same-side
(SS, |φ∆| < π/2) 2D peak representing intra jet corre-
lations and an away-side (AS, |φ∆−π| < π/2) 1D peak
representing inter jet (back-to-back jet) correlations. The
SS peak is dominated by US pairs while the AS peak has
US ≈LS, consistent with fragmentation of back-to-back
charge-neutral gluons. Note that 2D angular correlations
from MB dijets are directly related to interpretations of
UE systematics vs a trigger pt condition and the so-called
pedestal eﬀect as discussed further in Sec. VII C.
yt
∆ρ / √ρref 
yt
1
2
3
4
1
2
3
4
0
0.02
0.04
0.06
φ∆
∆ρ / √ρref 
η∆
0
2
4
-1
0
1
0
0.02
0.04
FIG. 3:
(Color online) Two-particle correlations on (yt, yt)
and (η, φ) [31, 32]. Left: Minimum-bias correlated-pair den-
sity on 2D transverse-rapidity space (yt, yt) from 200 GeV p-p
collisions showing soft (smaller yt) and hard (larger yt) com-
ponents as peak structures. Right: Correlated-pair density on
2D angular diﬀerence space (η∆, φ∆). Although hadrons are
selected with pt ≈0.6 GeV/c (yt ≈2.15) features expected for
dijets are still observed: (i) same-side 2D peak representing
intrajet correlations and (ii) away-side 1D peak on azimuth
representing interjet (back-to-back jet) correlations.
C.
Hard/soft ratio trends vs ns
The relation ¯ρh ≈α¯ρ2
s plays a key role in understand-
ing the nature of p-p collisions, especially in the context of
evaluating the PMC. It is therefore important to consider
the evidence for and accuracy of that relation in terms
of ratios nh/ns and ¯Pt/ns vs soft-component density ¯ρs.
Figure 4 (left) shows ratio nh/ns = ¯ρh/¯ρs vs ¯ρs =
ns/∆η for ten multiplicity classes from Ref. [2, 41]. ¯ρh
is the yt integral of hard-component H(yt) appearing in
the form H(yt)/α¯ρ2
s in Fig. 1 (right). The linear trend for
nh/ns establishes the relation ¯ρh ∝¯ρ2
s. Soft-component
density ¯ρs may be interpreted as a proxy for the den-
sity of low-x gluons released from projectile nucleons
in a p-p collision.
p-p spectrum data then reveal that
the number of mid-rapidity dijets ∝¯ρh varies quadrat-
ically with number of participant gluons.
But for an
eikonal collision model the number of gluon-gluon binary
collisions should vary as the dashed curve representing
¯ρh ∝¯ρ4/3
s
, as assumed for a geometric Glauber model
and the PMC. These p-p data appear inconsistent with
the eikonal model. The noneikonal quadratic trend re-
mains accurate over a ¯ρs range corresponding to 100-fold
increase in dijet production or scattered-parton density.
Figure 4 (right) shows ¯Pt/ns (a ratio of integrated
quantities) vs soft-component mean density ¯ρs described
by a constant term (soft component ¯pts) plus linear
term (hard component ∝¯ρs).
The solid line is de-
rived from the spectrum ¯ρ0(pt) TCM of Eq. (5) with
¯Pt = ∆η
R ∞
0
dptp2
t ¯ρ0(pt). Given evidence in this section,
nh and ¯Pt variations with ¯ρs appear to be determined en-
tirely by a jet-related hard component, and the ¯Pt hard
component varies as ¯Pth ∝¯ρ2
s. As noted, the linear ratio
trends (quadratic relation between nh or ¯Pth and ¯ρs) ex-
tend accurately over a ¯ρs range corresponding to 100-fold
increase of dijet production (and hence scattered-parton
density).
That result conﬂicts with a conjectured CR


## Page 10


10
ns / ∆η
nh / ns
200 GeV p-p
eikonal trend
0
0.05
0.1
0
5
10
15
20
25
0.35
0.375
0.4
0.425
0.45
0.475
0.5
0.525
0.55
0
5
10
15
20
25
ns / ∆η
 ¯Pt / ns (GeV/c)
200 GeV p-p
¯pts
FIG. 4:
Left: Hard/soft multiplicity ratio nh/ns (points) vs
soft component ns consistent with a linear trend (line) [2, 41].
Assuming that ns represents the density of small-x partici-
pant partons (gluons) and nh represents dijet production by
parton scattering, an eikonal model of p-p collision geometry
(analogous to the Glauber model of A-A collisions) would pre-
dict an n1/3
s
trend for the ratio (dashed curve). Right: The
¯pt →¯Pt/ns trend predicted by the p-p spectrum TCM (line)
and as determined by direct spectrum integration (points).
The hatched band represents the uncertainty in soft compo-
nent ¯pts from extrapolating pt spectra to zero momentum.
mechanism and consequent parton density (MPI number
density) dependence of FFs (Sec. III B).
VI.
MPIs vs MINIMUM-BIAS DIJETS
As summarized in Sec. II B the PMC is based on as-
sumptions that (a) almost all hadrons arise from jets
(MPIs) – soft hadron production is negligible, (b) the
jet (MPI) spectrum extends to pt →0, (c) each inelastic
p-p collision therefore includes at least one MPI, (d) MPI
production is controlled by p-p centrality as described by
a geometric Glauber model based on the eikonal approx-
imation and (e) parton fragmentation to jets involves a
CR mechanism tuned to accommodate certain ¯pt data.
This section compares those assumptions to manifesta-
tions of MB dijets in several data formats.
A.
Systematics of MB dijets from ISR and Sp¯pS
Reconstructed-jet data available from the ISR and
Sp¯pS in the mid eighties are reviewed and described by
a simple parametrization inferred recently from p-p spec-
trum and correlation data in the context of the TCM [15].
A survey of various manifestations of MB dijets in several
data formats is reported in Ref. [42].
Figure 5 (left) shows MB jet spectra for ﬁve p-p col-
lision energies from the ISR (43 and 63 GeV [43]) and
Sp¯pS (200, 500 and 900 GeV [10]) plotted conventionally
on jet (parton) pt. Those innovative analyses provided
the ﬁrst access to very low jet energies. The solid curves
through data are deﬁned by Eq. (6) below.
Figure 5 (right) shows UA1 total cross sections for MB
jet production. The cross sections represent p-p events
pt (GeV)
d2σj / dptdη (mb/GeV)
UA1/R807
minijets
17
43
63 GeV
200
500
900
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
√s (GeV)
σj0 (mb)
UA1
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
10
2
10
3
FIG. 5:
Left:
Inclusive jet cross sections (points) from
ISR [43] and Sp¯pS [10] collisions at ﬁve energies extending
down to 5 GeV/c jet momentum. The curves are from Eq. (6).
The 17 GeV curve is a model extrapolation applicable to
Pb-Pb collisions at the SPS. Right: Jet (jet-event) total cross
sections for Et > 5 GeV within |η| < 2.5 from Ref. [10]. The
curve is described by Eq. (7) (second line).
that include at least one jet with Et > 5 GeV within
|η| < 2.5. The curve passing through data is described
by Eq. (7) (second). Point-to-point deviations are small
compared to ±20% systematic uncertainties (error bars).
To simplify jet spectrum parametrization certain log-
arithmic rapidity variables are deﬁned in terms of the
pion mass.
The jet (parton) rapidity is ymax
≡
ln(2Ejet/mπ) [7], with Ejet →pt for plotted jet spec-
tra, and the beam rapidity is yb ≡ln(√s/mπ).
The
conditional jet (scattered-parton) spectrum for a given
collision energy √s is denoted by d2σj/dymaxdη
≡
Sp(ymax|yb).
Systematic analysis of available jet pro-
duction data leads to a simple parametrization based on
quantities yb0 ≡ln(√s0/mπ) with √s0 ≈10 GeV and
ymax0 = ln(2Ecut/mπ). Diﬀerences ∆yb = yb −yb0 and
∆ymax = yb −ymax0 are deﬁned, with normalized diﬀer-
ential jet (parton) rapidity u = (ymax −ymax0)/∆ymax.
Section V established that hard-component density ¯ρh
(and presumably dijet production as dσj/dη) for 200 GeV
p-p collisions scales with the soft-component density as
¯ρh ∝¯ρ2
s due to the noneikonal nature of p-p collisions.
Given that relation and ¯ρs ≈0.81∆yb near mid-rapidity
at and above ISR energies [36] jet spectra near midrapid-
ity should scale vertically as dσj/dη ∝(∆yb)2. Based on
systematics of FFs deﬁned on ymax reported in Ref. [7] jet
rapidity as ymax−ymax0 is rescaled horizontally by factor
∆ymax to normalized rapidity u. Jet spectrum data then
collapse to a single locus consistent with a Gaussian if
parameter ymax0 corresponds to Ecut ≈3 GeV.
Figure 6 (left) shows data from Fig. 5 (left) with
the jet spectrum (points) rescaled vertically by factor
(∆yb)2 and parton rapidity ymax −ymax0 rescaled hor-
izontally to u by ∆ymax, with ymax0 ≈3.8 correspond-
ing to Ecut ≈3.0 GeV. All jet data for p-p collision en-
ergies below 1 TeV fall on a common ﬁtted Gaussian
0.15 exp(−u2/2σ2
u) (solid curve). The parton spectrum


## Page 11


11
parametrization, conditional on beam rapidity, is then
d2σj
dymaxdη = pt
d2σj
dptdη
(6)
≈0.052(∆yb)2
1
p
2πσ2u
e−u2/2σ2
u,
where 0.052/
p
2πσ2u ≈0.15 and σu ≈1/7 are determined
empirically from the jet data.2 As demonstrated by the
curves in Fig. 5 (left) from Eq. (6) the jet cross section is
represented over nine decades by parameters yb0, ymax0,
σu and σX, the last an overall cross-section scale. End-
points yb0 and ymax0 are related by kinematic limits on
charged-hadron jet production from low-x gluons, while
σu and σX represent PDF and pQCD ˆσ details in Eq. (1).
10
-10
10
-9
10
-8
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
0
0.2
0.4
0.6
0.8
1
u
(1/∆yb)2(1/∆ymax)  d2σj / du dη
beam energy (GeV)
900 UA1
630 UA1
630 UA2
546 UA1
500 UA1
200 UA1
  63 R807
  43 R807
UA1/UA2/R807
10
-2
10
-1
10
2
10
3
10
4
√s (GeV)
(1/σNSD) dσj / dη
FIG. 6:
Left:
Rescaled jet spectra for several ener-
gies [10, 43, 44] plotted vs normalized fragment rapidity u.
The data fall on a common curve 0.15 exp(−25.5u2). Right:
The energy trend of the dijet frequency or dijet η density per
NSD p-p collision fNSD = (1/σNSD)dσj/dη (solid curve) is
inferred from a σNSD(√s) parametrization in Ref. [15] and
from Eq. (7).
Integrating Eq. (6) over u ∈[0, 1] (ﬁrst line below) and
assuming an eﬀective 4π η interval ∆η4π ≈1.3∆yb [10]
(second line below) gives
dσj
dη
= 0.026(∆yb)2∆ymax
(7)
σj0 ≈0.034(∆yb)3∆ymax,
where the second line deﬁnes the solid curve in Fig. 5
(right). It is notable that the ISR spectrum data were
not included in determining the model parameters above.
The corresponding curves in Fig. 5 (left) then serve as
predictions that describe the ISR jet data well.
Figure 6 (right) shows a predicted collision-energy
trend for the jet η density per NSD p-p collision
fNSD = (1/σNSD)dσj/dη based on a parametrization of
σNSD(√s) [15] and on Eq. (7) (ﬁrst line). For 200 GeV
2 In Ref. [15] the coeﬃcient is given incorrectly as 0.026. Only half
the Gaussian is relevant to the jet cross section and therefore
integrates to
p
2πσ2u/2. Equations (7) remain correct.
p-p collisions fNSD ≈0.028 corresponds to dσj/dη ≈1
mb, σj0 ≈4 mb and σNSD ≈36 mb. Within the STAR
TPC acceptance ∆η = 2 the fraction of 200 GeV NSD
p-p collisions with a dijet is about 6%. 94% of p-p colli-
sions then have no signiﬁcant jet activity, thus qualifying
as soft events (i.e. no MPIs within the acceptance).
Jet spectrum data described by the model of Eq. (6)
as in Figs. 5 (left) and 6 (left) require a parameter ymax0
corresponding to Ecut ≈3 GeV, a value just below the
UA1 (mini)jet spectrum 5 GeV lower bound in Fig. 5
(left). The 5 GeV represents an estimated limitation on
eventwise jet reconstruction, not a physical limit to the
jet spectrum. As demonstrated below, diﬀerential MB
jet manifestations in hadron spectra and correlations are
more sensitive to the lower bound and conﬁrm an eﬀec-
tive physical cutoﬀnear 3 GeV. It is notable that the Ecut
parameter for Eq. (6) has no apparent energy dependence
according to data [15], whereas the PMC MPI spectrum
cutoﬀparameter p⊥0 must vary “like some power of CM
energy” [9] (e.g. ∼Eϵ
CM, Sec. I) to accommodate data.
B.
MB dijets and pt-spectrum hard components
One can describe or predict fragment distributions
(FDs) via a QCD convolution integral that combines ac-
curate parametrizations of measured p-p jet spectra as
in Sec. VI A and measured p-p FFs as in Refs. [7, 15].
FDs are then directly comparable with pt spectrum hard
components as inferred within the context of the TCM.
An ensemble-mean FD for MB dijets is deﬁned by the
convolution integral
¯D(yt) ≈
1
dσj/dη
Z ∞
0
dymax Dpp(yt|ymax)
d2σj
dymaxdη , (8)
where Dpp(yt|ymax) represents measured FFs from p-p
collisions [7, 15] and d2σj/dymaxdη is given by Eq. (6).
Assuming that spectrum TCM hard component H(yt)
represents hadron fragments from MB dijets it can be
related to ¯D(yt) by ytH(yt) ≈fNSD ϵ ¯D(yt), where fNSD
is obtained from Fig. 6 (right) and ϵ ≈0.6 within de-
tector acceptance ∆η = 2 [35]. The charge-density hard
component for NSD p-p collisions can be expressed in
terms of the integral on yt of Eq. (8)
¯ρh,NSD =
Z
dytytH(yt)
(9)
= fNSD ϵ2¯nch,j,
where 2¯nch,j is the mean fragment multiplicity per dijet.
Figure 7 (left) shows FF data (points) for ten dijet
energies from 78 to 573 GeV inferred from 1.8 TeV p-¯p
collisions (points) using eventwise jet reconstruction [45].
The solid curves are the Dpp parametrization used in
Eq. (8) [16]. Comparison with e+-e−FFs from Ref. [7]
(dashed curves for 2Ejet = 6 and 91 GeV) reveals that a
substantial portion of e+-e−dijet FFs at lower fragment
momenta may be missing from reconstructed p-¯p FFs.


## Page 12


12
0
1
2
3
4
5
6
7
8
0
2
4
6
8
y
Dpp(y|ymax)
1
10
100
p (GeV/c)
78
6
2Ejet =
573 GeV
91
CDF
yb
(1/f) ytH(yt), εDu(y), Sp(ymax)
1
10
pb (GeV/c)
Sp
εDu
ytH(yt)/f
Sp(ymax)
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
2
3
4
5
6
FIG. 7:
Left: Fragmentation functions for several dijet en-
ergies (points) from p-¯p collisions at 1.8 TeV [45]. The solid
curves represent a p-¯p parametrization derived from the e+-e−
parametrization in [7]. The dashed curves show the e+-e−
parametrization itself for two energies for comparison. Right:
The spectrum hard component for 200 GeV NSD p-p colli-
sions [2] in the form ytH(yt)/fNSD (solid points) compared
to calculated mean fragment distribution ¯D(yt) (dashed) with
yb = yt, y or ymax [16].
The jet spectrum that generated
¯D(yt) (dash-dotted) is deﬁned by Eq. (6). The open boxes
are 200 GeV p-p jet-spectrum data [10] transformed to ymax.
Fig. 7 (right) shows the corresponding mean FD
ϵ ¯D(yt) (dashed) described by Eq. (8) compared to hard-
component data from 200 GeV NSD p-p collisions (solid
points [2, 3]) in the form ytH(yt)/fNSD corresponding to
their relation in the text just below Eq. (8). The open
boxes are 200 GeV p-¯p jet-spectrum data from Ref. [10]
on ymax. The dash-dotted curve is Sp from Eq. (6).
This panel demonstrates that the combination in
Eq. (8) of a measured jet energy spectrum as in Fig. 5
(left) and measured p-p FFs as in Fig. 7 (left) accurately
describes a measured spectrum hard component from 200
GeV p-p collisions [16], supporting the interpretation that
spectrum hard components represent the full contribu-
tion from MB large-angle-scattered low-x gluons into an-
gular acceptance ∆η, at least for 200 GeV p-p collisions.
The result depends critically on the choice Ecut ≈3 GeV.
Similar conclusions are obtained for other energies [36].
Figure 8 (left) shows measured spectrum hard compo-
nents in the form H(pt, √s)/¯ρs(√s) (points) for 200 GeV
and 13 TeV NSD p-p collisions representing the spectrum
hard component per soft-component hadron correspond-
ing (by hypothesis) to dijet production per participant
low-x gluon. The curves are TCM model functions in the
form α(√s)¯ρs(√s) ˆH0(pt, √s) with
ˆH0(pt, √s) energy-
dependent parameters (¯yt, σyt, q) [46]. Isolated hard com-
ponents establish spectrum energy evolution and its rela-
tion to dijet production. The overall result is a compre-
hensive description of dijet contributions to pt spectra vs
p-p energy variation over three orders of magnitude [36].
Figure 8 (right) shows inverse values (solid points)
of exponents q = 5.15 for 200 GeV and q = 3.65 for
13 TeV from Ref. [36] plotted vs quantity ∆ymax ≡
ln(√s/6 GeV) observed to describe the energy trend for
jet spectrum widths ∝∆ymax from NSD p-p collisions as-
suming a jet spectrum low-energy cutoﬀnear 3 GeV [15]
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
0.14
0.16
0.18
0.2
0.22
0.24
0.26
0.28
0.3
0
2
4
6
8
∆ymax
1 / q
17.3 GeV
200 GeV
0.9 TeV
2.76
7
13
10 GeV
jet threshold
NSD p-p
FIG. 8:
Left: A survey of spectrum hard components over
the currently accessible p-p energy range from threshold of
dijet production (10 GeV) to LHC top energy (13 TeV). The
curves are determined by TCM parameters for NSD p-p col-
lisions from Ref. [46]. The 200 GeV ﬁne solid curves illus-
trate nch dependence.
The points are from Refs. [3] (200
GeV) and [46] (13 TeV). Right: Hard-component exponents
plotted in the form 1/q determined by analysis of spectrum
data (solid points) from Ref. [3]. The solid line is based on a
jet-spectrum parametrization in Ref. [15] that also describes
ensemble-mean-pt hard-component energy variation [37].
as in Fig. 6 (left). Inverse 1/q eﬀectively measures the
hard-component peak width at larger yt. The descrip-
tion of 5 TeV p-Pb spectra in Sec. V A is based on that
relation. Since the p-p pt-spectrum hard component can
be expressed as the convolution of a ﬁxed p-p FF ensem-
ble with a collision-energy-dependent jet spectrum [16],
and the jet-spectrum width trend has an energy depen-
dence ∝∆ymax [15] the relation 1/q ∝∆ymax (solid line)
should be expected. That the same relation applies to the
ensemble-mean ¯pt hard component was established in a
separate study [37] (and see the next subsection).
In summary, direct comparison of measured pt spec-
trum hard components with measured jet spectra and
FFs combined in a convolution integral conﬁrms an ef-
fective lower bound ≈3 GeV for MB jet spectra and a
dijet frequency fNSD ≈0.028 per unit η and per NSD
event for 200 GeV p-p collisions, in contrast to the PMC
assumptions of at least one MPI per inelastic p-p collision
and energy-dependent p⊥0 [9]. Multiple dijets per unit η
per p-p collision do occur if a large p-p nch condition is
imposed (e.g. 100-fold increase for data in Refs. [2, 3]).
C.
MB dijets and ¯pt-vs-nch trends
The relation of ensemble-mean ¯pt vs nch data to the
hadron pt spectrum TCM in Sec. V A and MB dijets
in the previous subsection is demonstrated in this sub-
section. The TCM for ensemble-mean integrated total
¯Pt within acceptance ∆η from p-p collisions for given


## Page 13


13
(nch, √s) follows from the pt spectrum TCM in Eqs. (5)
Pt = ∆η
Z ∞
0
dpt p2
t ¯ρ0(pt) = Pts + Pth
(10)
¯Pt = ns¯pts + nh¯pth,
where ¯pts and ¯pth can be obtained directly from TCM
model functions ˆS0(pt) and ˆH0(pt) in Eq. (5) or inferred
from ¯pt data systematics as described below. The con-
ventional intensive ratio of extensive quantities
¯p′
t ≡
¯P ′
t
n′
ch
≈
¯pts + x(ns)¯pth(ns)
ξ + x(ns)
(11)
conﬂates two simple TCM trends and in eﬀect partially
cancels MB dijet manifestations apparent in the form of
x(ns) ≡¯ρh/¯ρs = nh/ns ≈α¯ρs.
Primes indicate the
eﬀect of a pt acceptance cutoﬀ. Alternatively, the ratio
n′
ch
ns
¯p′
t ≈
¯Pt
ns
= ¯pts + x(ns)¯pth(ns)
(12)
≈¯pts + α(√s) ¯ρs ¯pth(ns, √s)
preserves the simplicity of Eq. (10) and provides a con-
venient basis for precise tests of the TCM hypothesis, for
instance in Fig. 4 (right).
Figure 9 (left) shows ¯pt data for four p-p collision ener-
gies from the RHIC (solid triangles [2]), the Sp¯pS (open
squares [47]) and the LHC (upper points [40]) increasing
monotonically with charge density ¯ρ0 = nch/∆η. The
lower points and curves correspond to full pt acceptance.
For acceptance extending down to zero (ξ = 1), ¯p′
t →¯pt
in Eq. (11) should vary between the universal lower limit
¯pts ≈0.40 GeV/c (nch →0) and ≈¯pth0 (nch →∞) as
limiting cases. For a lower-pt cut pt,cut > 0 the lower
limit is ¯p′
ts = ¯pts/ξ (upper dotted lines) and the data are
systematically shifted upward (upper points and curves).
Solid curves represent the p-p ¯pt TCM Eq. (11) [37].
Figure 9 (right) shows the result when, following
Eqs. (12), ¯p′
t data in the left panel are multiplied by
n′
ch/ns, ¯pts ≈0.4 GeV/c is subtracted from the prod-
uct and the diﬀerence is divided by x(√s) ≡α(√s) ¯ρs
to obtain ¯pth(ns, √s) vs ¯ρs.
The solid lines represent
the ¯pth0 derived from TCM spectrum hard components
as in Fig. 8 (left). Values for α(√s) from Ref. [37] are
consistent with the correspondence between ¯pth(ns, √s)
data (points) and ¯pth0 values (lines) as shown.
The
α(√s) values for various energies and detector systems
[parametrized by Eq. (A3)] are quantitatively consistent
to a few percent given the diﬀerences in acceptance ∆η
between diﬀerent detectors. Some nch dependence of ¯pth
mean values is expected based on results from Refs. [2, 36]
[see the corresponding 200 GeV nch dependence (thin
solid curves) in Fig. 8 (left)].
Figure 10 (left) shows 13 TeV TCM hard-component
models for several p-p multiplicity classes (curves) as re-
ported in Ref. [37]. The points are 13 TeV pt spectrum
data from Ref. [46]. The model-parameter variation for
7 TeV is determined by expressions interpolated from 13
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
0.9
1
1.1
1.2
1.3
1.4
1.5
0
10
20
30
40
ns / ∆η
¯pth (GeV/c)
7 TeV
2.76 TeV
900 GeV
200 GeV
p-p
FIG. 9:
Left: ¯pt vs nch for several collision energies. The up-
per group of points is from Ref. [40]. The lower 900 GeV data
from UA1 derived from a “power-law” spectrum model [47]
fall signiﬁcantly above the TCM for that energy (solid curve)
but are consistent with the TCM form with amplitude ad-
justed. The 200 GeV STAR data are spectrum integrals from
Ref. [2]. Right: Hard components ¯pth(ns) (points) isolated
from data at left per Eq. (12). The horizontal lines represent
mean values ¯pth0(√s) extracted from p-p spectra (Fig. 8, left).
The ¯pth(ns) data vary signiﬁcantly about those mean values
as expected from results in Ref. [36].
TeV to 7 TeV and extrapolated on ¯ρs from the rather
limited 13 TeV multiplicity range in Ref. [46].
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
1
2
3
4
5
yt
αH0(yt,nch)
13 TeV p-p
0.9
1
1.1
1.2
1.3
1.4
1.5
0
10
20
30
40
ns / ∆η
¯pth (GeV/c)
7 TeV p-p
FIG. 10:
Left:
pt spectrum hard-component models for
13 TeV p-p collisions and a range of nch based on a TCM
parametrization from Ref. [36] compared to spectrum data
from Ref. [46] for inelastic p-p collisions (points).
Right:
¯pth(ns) values inferred from 7 TeV p-p ¯pt data as in Ref. [37]
(points) compared to a ¯pth(ns) trend (curve) inferred from
the model functions in the left panel.
Figure 10 (right) shows 7 TeV ¯pth(ns) data from Fig. 9
(right) (points). The curve is determined by ¯pth(ns) val-
ues obtained from spectrum model functions in the left
panel. The correspondence between ¯pt data and TCM
is good.
In turn, there is quantitative correspondence
between p-p pt spectrum hard components and measured
jet properties accurate at the percent level as noted in
the previous subsections.
These detailed TCM results
further buttress the conclusion that ensemble-mean ¯pt
variation is completely determined by MB dijets.
In summary, the strong increase of ¯pt with nch as in
Fig. 9 (left) is simply described within the TCM by lin-
ear variation of relative fractions of ﬁxed soft and hard
spectrum components [37]. The hard component is de-


## Page 14


14
rived quantitatively from a measured MB jet spectrum
(with eﬀective cutoﬀnear 3 GeV determined by spectrum
data) and measured FFs [16, 36]. The linear hard/soft
ratio variation arises from the noneikonal nature of p-p
collisions that argues against any role for p-p centrality.
In contrast, variation of ¯pt with nch must be modeled in
the PMC by MPIs as the single source of hadrons. To
achieve monotonic increase of ¯pt an ad hoc CR mecha-
nism is then required. The CR mechanism in eﬀect alters
FFs (modeled by string fragmentation) by decreasing the
nch per MPI, supposedly to accommodate an increasing
MPI density attributed to increased p-p centrality [25].
D.
NBD 1/k and MB jet-spectrum lower limit
Further information on the eﬀective lower limit of MB
jet spectra can be derived from the systematics of P(nch)
distributions, speciﬁcally from ﬁtted NBD model param-
eters (µ, k). As noted in Sec. III A P(nch) distributions
for p-p collisions up to 1 TeV are well-described by a sin-
gle NBD distribution. Above that energy and for larger
nch a double NBD is required [23], but for the present
argument single-NBD ﬁts closer to the mode are suﬃ-
cient. In this subsection the energy dependence of NBD
parameter k is used to support the conclusion that the
MB jet spectrum has an eﬀective lower limit near 3 GeV.
Within a TCM context the p-p charge multiplicity
trend nch(√s) can be approximated at higher energies as
follows [36]: The total charge density near midrapidity is
¯ρ0 ≡nch/∆η = ¯ρs + ¯ρh, where ¯ρs ≈0.81 ln(√s/10 GeV)
(near and above ISR energies) is interpreted to represent
participant low-x gluons from proton dissociation. The
hard component is ¯ρh ≈α¯ρ2
s with α(√s) ≈O(0.01) as
described in Ref. [37] and Eq. (A3). For ISR and Sp¯pS en-
ergies ¯ρh ≪¯ρs so ¯ρ0 ≈¯ρs. As noted in Sec. III A Ref. [22]
reports the relation 1/k ≈0.06 ln(√s/6 GeV) (consistent
with Ecut ≈3 GeV). From Sec. VI A those expressions
can be rewritten as ¯ρ0 ≈0.81∆yb and 1/ˆk ≈0.48∆ymax,
where ˆk ≡k/∆η is a value averaged over the acceptance
(assuming UA5 acceptance ∆η4π ≈8 [48]).
A number variance σ2
n ≡n2 −¯n2 can be interpreted
to represent the number of correlated pairs within some
acceptance ∆η. For a NBD the variance is expressed as
σ2
n = ¯n + ¯n2/k.
(13)
The ﬁrst term is the number of self pairs, the Poisson ref-
erence σ2
n,ref = ¯n. The second term, the variance excess,
represents the eﬀective number of correlated pairs. Since
¯n2 is the total number of pairs (given ensemble mean ¯n)
1/k is the fraction of those pairs correlated within ∆η.
While k does increase monotonically with ∆η [22] it is
related to a running integral of underlying angular cor-
relations [30, 49]. ˆk may vary signiﬁcantly with ∆η.
Returning to p-p collisions, the number of correlated
pairs represented by an NBD variance excess ∆σ2
nch is
∆σ2
nch = σ2
nch −σ2
nch,ref = ¯n2
ch/k
(14)
≈∆η ¯ρ2
0/ˆk
∆σ2
nch/∆η ≈0.3 ∆y2
b ∆ymax
based on text above Eq. (13). The coeﬃcient 0.3 is an
upper limit based on UA5 acceptance ∆η4π ≈8. The
relevant value could be half that. Equation (14) (third
line) can be compared with the jet cross section in Eq. (7)
(ﬁrst line)
dσj/dη ≈0.026∆y2
b∆ymax
(15)
to conclude that at least in terms of energy dependence
∆σ2
nch/∆η ≈(5 - 10) × dσj/dη.
(16)
This result suggests that MB dijets may be the main
source of nonPoisson nch ﬂuctuations as manifested by
a variance excess for distribution P(nch).
The trend
for 1/k inferred from ISR and Sp¯pS data as reported in
Ref. [22] is consistent with 1/k ∝∆ymax ≡ln(√s/2Ecut)
if Ecut ≈3 GeV. Thus, a speciﬁc jet spectrum cutoﬀ
near 3 GeV is supported by measured jet spectra, by p-p
hadron pt spectra and by charge multiplicity ﬂuctuations.
E.
Double parton scattering
The PMC assumption that almost all hadrons arise
from MPIs (multiple parton scatters per NSD event) in
high-energy p-p collisions appears to conﬂict with the
systematics of MB dijets manifesting as the TCM hard
component, dominated by a single dijet per hard event
and fraction of hard events ≪1 within an NSD event
ensemble and typical acceptance ∆η [20]. However, the
TCM description does not exclude double parton scat-
tering (DPS) occurring with some (possibly small) prob-
ability, and p-p DPS has been demonstrated for example
in Ref. [50]. In this subsection evidence for DPS and its
properties from 1.8 TeV p-p collisions are reviewed.
For the DPS study in Ref. [50] the applied DPS event
trigger is γ + 3 jets.
Single events with that trigger
are compared with pileup event pairs satisfying single-
parton-scattering (SPS) triggers: γ + jet vs jet + jet.
The DPS probability can then be expressed as
PDP =
σDP
σNSD
≡m
2
σNSD
σeﬀ
σγj
σNSD
σjj
σNSD
,
(17)
where σNSD is a reference NSD cross section, and σeﬀis a
deﬁned eﬀective cross section for DPS events. Factor 1/2
corresponds to Poisson-distributed events and factor m
denotes distinguishable (2) vs indistinguishable (1) hard
scatters. Experimentally, m = 2 is established and the
two factors cancel. The corresponding expression for sin-
gle hard scatters in a pair of pileup events (DI) is
PDI =
σDI
σNSD
= 2 σγj
σNSD
σjj
σNSD
(18)


## Page 15


15
where factor 2 is the number of ways γ-jet and dijet
processes can be ordered within the DI pair.
For an
integrated luminosity Lt ≈16/10−12b event numbers
NDP = 7360 and NDI = 1060 were observed, giving
an inferred σeﬀcross section [50]
σeﬀ=
PDI
PDP
σNSD
2
(19)
=
NDI
NDP
ADP
ADI
Rc σNSD
≈1/6.9 × 1.04 × 2 × 50 mb ≈15 mb.
To place this DPS result in a TCM context requires
the following numbers for 1.8 TeV p-p collisions (inter-
polated from Ref. [15]): σNSD ≈50 mb, dσj/dη ≈5
mb →dσSP /dη and fSP ≡(1/σNSD)dσSP /dη ≈0.1.
It is clear from Fig. 15 (right) that MB dijets are local-
ized near midrapidity, so a cross-section density is more
appropriate for describing low-energy jets.
Expressing
Eq. (17) in terms of dijet frequency f (deﬁned in Ref. [2])
fDP ≡(1/σNSD)dσDP /dη
(20)
=
1
feﬀ
f 2
SP
≈5-10 × (0.1)2
≈0.05-0.1
dσDP /dη ≈2.5-5 mb
where feﬀ= (1/σNSD)dσeﬀ/dη ≈0.1-0.2 is estimated
from the result in Eq. (19). Those numbers suggest that
fDP ≪1 describes 1.8 TeV p-p collisions.
It is then
unlikely that MPIs (especially multiple hard scatters per
event) play a dominant role in hadron production from
NSD p-p collisions near midrapidity. Multiple dijets are
expected for p-p events with large nch because of the
quadratic dependence of dσj/dη on charge multiplicity.
VII.
UNDERLYING EVENT vs MB DIJETS
The UE for high-energy p-p collisions is by deﬁnition
complementary to an eventwise-triggered dijet or pQCD
leading-order process [51]. Access to the UE is expected
via the transverse (azimuth) region or TR component of
the single-particle charge density relative to the trigger
(or of 1D azimuth correlations as in Fig. 11, right), as-
sumed to have no contribution from the triggered dijet.
However, the structure of measured MB dijet 2D angular
correlations from 200 GeV p-p collisions can be used to
demonstrate a signiﬁcant triggered-dijet contribution to
the TR, contradicting UE-related assumptions.
The relation between an underlying event and TCM
descriptions of p-p data was considered previously in
Ref. [20] which distinguishes diﬀerent responses to nch
and pt,trig event selection conditions. An nch condition
controls the soft-component charge density ¯ρs and there-
fore the dijet production rate as measured by hard com-
ponent ¯ρh ∝ρ2
s. In contrast, a pt,trig condition selects the
fraction of hard events (at least one jet in the acceptance)
vs soft events (no jet in the acceptance) without chang-
ing the soft-component density signiﬁcantly and therefore
without changing MB dijet production, although it does
alter (bias) the eﬀective jet spectrum (see Sec. VII D).
A.
Conventional underlying-event analysis
The UE study reported in Ref. [51] considers charge-
jet evolution and properties of the UE within an accep-
tance pt > 0.5 GeV/c and |η| < 1. Trigger (leading) jets
(jet in each event with greatest PT 1 = P
i∈jet pti) fall
in the range PT 1 ∈[0.5, 50] GeV/c. The UE is assumed
to consist of beam-beam remnants, initial-state radia-
tion and possibly MPIs (but distinct from the leading
jet). The leading-jet axis is an azimuth reference relative
to which other hadrons are distributed. The transverse
region (TR) subtending |φ −π/2| < π/6 is said to be
“very sensitive to the underlying event” and is assumed
to exclude the leading jet (and its partner).
The UE
accompanying a hard scatter is said to be “considerably
more active (i.e. higher charged particle density and more
transverse momentum) than a soft [p-¯p] collision” [51],
which deﬁnes the term “activity” as associated with the
UE within the PMC context.
UE-related trends include TR-integrated charge N⊥
vs leading-jet pT 1 and TR pt spectrum dN⊥/dpt.
UE
data are modeled by several Monte Carlos (PYTHIA,
ISAJET, HERWIG). “For PYTHIA we include particles
that arise from the soft or semi-hard scattering in mul-
tiple parton interactions [MPIs] in the beam-beam rem-
nant component” [51]. That strategy is required if no
soft component is available. Simulated hard scattering
is limited to pt,hard > 3 GeV/c. MPIs extend to lower
momenta in PYTHIA (1.4 for V6.115 or 1.9 for V6.125
GeV/c).
In what follows jet-related correlation struc-
ture on φ, N⊥vs pT 1 and dN⊥/dpt data are reexamined
within the context of the TCM, with focus on the PMC.
B.
MB dijets from p-p collisions at 200 GeV
Figure 11 (left) shows measured 2D angular correla-
tions representing MB dijets from 200 GeV p-p colli-
sions [3].
No trigger condition is imposed—the distri-
bution represents all combinatoric pairs above a pt ac-
ceptance cut at 0.15 GeV/c (accepting 80% of the soft
component and all of the hard component). Contribu-
tions from a soft component (1D Gaussian on η∆), Bose-
Einstein (BE) correlations (narrow 2D exponential at ori-
gin) and uniform background are subtracted based on 2D
model ﬁts that describe data within statistical uncertain-
ties [3]. The data are corrected for ﬁnite η acceptance.
For conventional FB analysis (Sec. III D) the quantity
bF B(η∆) represents a projection of the 2D histogram at
left onto 1D η∆(symbol ∆η, here denoting a detector


## Page 16


16
acceptance, is also referred to as “η gap”). The 1D pro-
jection then superposes several correlation components:
(a) the TCM soft component – a narrow 1D peak on η∆,
(b) the SS 2D jet peak (in projection also a narrow 1D
peak on η∆), (c) the 2D BE peak, (d) the AS 1D jet
peak at π on azimuth contributing a constant oﬀset to
bF B(η∆). Each component has its own distinctive charge
combination (LS, US or neutral) that helps to identify its
source. Within the 1D projection of bF B(η∆) there is no
possibility to unravel the several production mechanisms.
φ∆
∆ρ / √ρref
η∆
φ∆
∆ρ / √ρref
TR
TR
TR
200 GeV
p-p
-1
0
1
0
2
4
0
0.02
0.04
0.06
0
0.01
0.02
0.03
0.04
0.05
0.06
0.07
0
2
4
FIG. 11:
(Color online) Left: Minimum-bias jet-related 2D
angular correlations from 200 GeV p-p collisions [3]. A same-
side 2D peak at the origin is elongated on azimuth.
The
away-side 1D peak is broad on azimuth and approximated
by a dipole cos φ∆form. These data are corrected for ﬁnite
η acceptance. Right: Projection by averaging of jet-related
angular correlations onto azimuth.
Dash-dotted and upper
dashed curves are ﬁtted models for SS and AS peaks. The
hatched areas represent the “transverse region” (TR) invoked
in underlying-event studies. The unhatched areas, denoting
“toward” (φ∆≈0) and “away” (φ∆≈π) regions, are con-
ventionally assumed to contain all triggered dijet structure.
The lower dashed curve describes uncorrected pairs and the
dotted curve is the actual distribution of jet-related pairs.
Figure 11 (right) shows the 2D data projected by aver-
aging onto 1D azimuth (solid histogram). Both the SS 2D
peak (dash-dotted) and the AS 1D peak (upper dashed)
are broad on azimuth. The AS peak width is approxi-
mately π/2, and the AS periodic peak array [27] is then
approximated by an azimuth dipole extending into the SS
region. The SS 2D peak for MB dijets in NSD p-p colli-
sions is elongated on azimuth with 2:1 aspect ratio. Thus,
untriggered SS and AS MB jet peaks are strongly overlap-
ping on azimuth within the TR. The AS pair structure –
azimuth dipole cos(φ∆−π) – is modiﬁed by a triangular
η-acceptance correction that overestimates accepted AS
pairs relative to the SS jet peak. The lower dashed curve
describes accepted jet-related AS pairs, and the dotted
curve is the distribution of all jet-related pairs.
The TR invoked in UE studies and indicated by the
hatched regions in the right panel (covering 1/3 of the
azimuth acceptance) is conventionally assumed to con-
tain no contribution from a triggered high-pt (di)jet (if
a triggered jet is conﬁned to a cone of radius R < 1)
and should therefore be particularly sensitive to the UE
complementary to the dijet [51]. Figure 11 reveals that
the TR must include a substantial fraction (about 30%)
of the fragment yield from MB dijets. The TR cannot be
distinguished from any other part of the MB jet struc-
ture and may be dominated by the TCM hard compo-
nent (MB jet fragments).
Since a hard event includes
by deﬁnition at least one dijet with mean fragment mul-
tiplicity ϵ2¯nch,j the TR in hard events should include
a hard-component jet-fragment density corresponding to
at least that multiplicity that can be inferred from data.
Compared to a MB jet sample eventwise triggering of
higher-pt jets would add higher-momentum hadrons suc-
cessively closer to φ∆= 0 and π (e.g. within a conven-
tional jet cone with radius R ≤1). However, the trigger
condition would not eliminate the MB base in Fig. 11,
common to any dijet, that should contribute a TCM hard
component as part of the triggered jet to any UE observ-
able contrary to UE assumptions.
That conclusion is
supported by pt spectra for transverse multiplicity N⊥
within the TR as discussed in Sec. VII D.
Similar issues emerge for trigger-associated (TA) stud-
ies of jet-related azimuth correlations where a zero-yield-
at-minimum (ZYAM) assumption is invoked: the jet frag-
ment distribution on azimuth relative to a high-pt trigger
hadron is assumed to fall to zero at a minimum in the
pair distribution (near or in the TR) [26]. That assump-
tion is challenged in Ref. [27]. A Bayesian analysis of
jet-related azimuth structure reported in Ref. [52] ﬁnds
that a MB jet model as in Fig. 11 is required by data.
C.
TR multiplicity N⊥vs pt,trig or Pj
Transverse multiplicity N⊥(pt,trig), integrated charge
within the TR for some trigger pt condition (single-
particle pt,trig or jet sum Pj), is employed to study UE
properties. In this subsection a parametrization derived
from the p-p TCM is applied to TR data. TCM energy
dependence relevant to N⊥is summarized in App. A.
For quantitative descriptions of N⊥(pt,trig) [20] certain
NSD data are required [35, 36]: For 200 GeV: ¯ρs ≈2.43,
¯ρh ≈0.006¯ρ2
s ≈0.035 and ¯ρ0 ≈2.5, with 2¯nch,j ≈2.1.
For 1.8 TeV: ¯ρs ≈4.2, ¯ρh ≈0.011¯ρ2
s ≈0.20 and ¯ρ0 ≈4.4,
with 2¯nch,j ≈3.4. Soft and hard event fractions λx are
expressed in terms of Poisson jet probabilities P0(nj) (no
jet) and [1 −P0(nj)] (at least one jet), where nj(nch) is
the mean jet number within an acceptance for p-p events
with multiplicity nch [15]. Also required are running in-
tegrals from above gx(yt,trig) of spectrum soft and hard
components. Acceptance factors γx represent the eﬀect
of a low-pt acceptance cut at 0.5 GeV/c for CDF data,
and factor ϵ ≈0.6 is the fraction of a dijet within ∆η = 2.
An expression for N⊥(pt,trig) derived from the TCM is
3
2N⊥(pt,trig) = λs(pt,trig)gs(pt,trig)γs¯ρs
(21)
+ λh(pt,trig)[gs(pt,trig)γs¯ρ′
s + gh(pt,trig)γhϵ2¯nch,j]
→γs¯ρ′
s + γhϵ2¯nch,j for pt,trig →∞,


## Page 17


17
where ¯ρ′
s is the soft component for hard (or triggered)
events and ¯ρ′
s ≈¯ρs is observed (see next subsection).
Note that instead of ¯ρh = fϵ2¯nch,j appearing in the ex-
pression for hard events (within square brackets) f →1
is assumed for a hard event induced by a pt trigger. A full
derivation of Eq. (21) is presented in Ref. [20]. For soft
events at 200 GeV with the CDF pt acceptance ¯ρs ≈2.43
and γs ≈0.25. For hard events ϵ2¯nch,j ≈1.26 [2] and
γh ≈0.95. For 1.8 TeV the numbers are ¯ρs ≈4.2 and
ϵ2¯nch,j ≈2.0 with limiting value N⊥≈2.0. For those
TCM results the most-probable jets are assumed to be
unbiased, having the same properties for any trigger. See
App. A 2 for further details.
Figure 12 (left) shows soft and hard event fractions
λs and λh vs trigger condition yt,trig for 200 GeV p-p
collisions. The fractions become equal for yt,trig ≈3 or
pt,trig = mπ sinh(yt,trig) ≈1.4 GeV/c.
yt,trig
event fraction
λh
λs
0
0.25
0.5
0.75
1
2
2.5
3
3.5
4
4.5
0
0.5
1
1.5
2
2.5
3
0
5
10
15
20
PT1 (GeV/c)
N⊥(PT1)
soft + hard
soft
200 GeV
1.8 TeV
FIG. 12:
Left: Event fractions λx for soft (s) and hard
(h) 200 GeV p-p collisions vs single-particle trigger condition
yt,trig.
Right: TR integrated yield N⊥vs summed trigger
(leading) jet momentum PT 1 data from Ref. [51] (points). The
curves are TCM results from Eq. (21) for for 200 GeV (dashed,
dotted) and 1.8 TeV (solid, dash-dotted) p-p collisions. The
two solid curves are explained in Sec. VII D and App. A.
Figure 12 (right) shows N⊥(PT 1) data for 1.8 TeV p-¯p
collisions from Ref. [51] (points) where PT 1 in that case
refers to summed pt per trigger jet PT 1 ≡P
i∈jet pti. The
TCM N⊥(PT 1) trends (curves) obtained from Eq. (21)
represent running integration from above of soft and hard
spectrum components (gx) and a transition from almost
all soft events to almost all hard events (λx). The 200
GeV curves stop near 10 GeV/c while the 1.8 TeV curves
extend to the limits of data.
The soft + hard curves
correspond to the ¯nch,j estimates above while the soft-
only curves correspond to setting ¯nch,j to zero. The two
solid curves are explained in Sec. VII D and App. A.
The 200 GeV curves are plotted vs pt,trig for illustra-
tion assuming a single trigger particle whereas the 1.8
TeV data correspond to a pt sum for a trigger jet. For a
leading-track (single-particle) trigger the plateau begins
near pt,trig ≈2.5 GeV/c, whereas for a leading-track-
jet trigger the plateau begins near PT 1 ≈5 GeV/c. To
model the diﬀerence pt,trig values applied to Eq. (21)
are converted for plotting to jet-sum approximations by
pt,trig →PT 1 ≈pt,trig +a p2
t,trig with a = 0.5 determined
by data. That expression is motivated by the observation
that for lower pt,trig a “jet” is more likely a single parti-
cle sampled from the soft component, with random soft
background contribution, whereas for higher pt,trig the
trigger particle is more likely associated with a real jet,
and multiple correlated jet fragments then contribute to
the PT 1 sum. See the jet-ﬁnding algorithm in Ref. [51]
for details.
The UE is expected to include only MPIs not identiﬁed
with the triggered jet, and the elevated plateau (extra UE
“activity”) is then interpreted to conﬁrm their presence.
But that expectation is not realistic for two reasons: (a)
a second signiﬁcant dijet is unlikely (less than 10% within
the CDF acceptance for 1.8 TeV NSD p-¯p collisions) ex-
cept for large-nch events and (b) the TR must include a
substantial contribution from any trigger jet as demon-
strated in the previous subsection. Figure 11 (right) con-
ﬁrms that for hard events (those including at least one
jet in the acceptance) the TR contains on average 1/3 of
the jet fragments from MB dijets, that is, from a trig-
gered dijet selected at random from a MB population.
The increase of TR “activity” with an applied trigger
noted in Ref. [9]3 actually represents the single trigger
dijet in hard events, to the extent that hard events are
preferred by the trigger condition, as well as a substantial
contribution from the TCM soft component.
These results demonstrate that a TCM description of
pt spectra and minimum-bias angular correlations pre-
dicts the general form of the N⊥(PT 1) trend with single-
particle or jet-sum pt condition.
For the CDF pt ac-
ceptance (pt > 0.5 GeV/c) the N⊥increase from zero
up to some plateau value includes a smaller contribu-
tion from the soft component (projectile nucleon disso-
ciation) and a larger contribution from the hard compo-
nent (large-angle base of any triggered dijet). However,
for a lower acceptance cutoﬀ(e.g. pt > 0.15 GeV/c) the
soft component (actual beam remnants) would dominate
N⊥(PT 1). Given the conventional UE analysis procedure
a “pedestal” would result even in the absence of jets.
D.
TR dN⊥/dpt spectrum structure
TR yield N⊥can also be characterized in terms of a
pt spectrum. In this subsection the TCM is applied to
dN⊥/dpt spectrum data to demonstrate that the N⊥soft
component has the same universal form inferred from
NSD p-p collisions, and the hard component is consistent
with a trigger condition that prefers p-p hard events with
at least one MB dijet. A previous analysis of dN⊥/dpt
data in Ref. [20], lacking detailed information on spec-
trum structure at higher collision energies, assumed TCM
3 The pedestal eﬀect: “events with high-p⊥jets on the average
contain more underlying [UE] activity than minimum-bias ones,
also well away from [trigger] jets themselves [emphasis added].”


## Page 18


18
model functions for 200 GeV p-p collisions and adjusted
certain Eq. (5) coeﬃcients to accommodate dN⊥/dpt
spectrum data. Given new information in Ref. [36] quan-
titative predictions are now possible.
Figure 13 (left) shows dN⊥/dpt data for 1.8 TeV p-p
collisions for speciﬁc trigger conditions: summed (high-
est) jet momentum Pj > 5 (solid points), Pj > 2 GeV/c
(open points) and Pj > 30 GeV/c (triangles) from Fig. 37
of Ref. [51].4 The N⊥spectrum data can be described
by Eq. (5) given transformation yt →pt and added fac-
tor pt. Based on the spectrum TCM from Ref. [36] and
parametrization of jet energy spectra from Ref. [15] the
N⊥spectrum data for 1.8 TeV p-p can be predicted by
interpolation. Spectrum soft component S (dashed) is
described by ¯ρs ≈4.2 (consistent with Ref. [51]), T ≈145
MeV and n = 9.0.
NSD hard component H (lowest
solid) is described by ¯ρh = fNSD ϵ2nch,j ≈α¯ρ2
s ≈0.20
with fNSD ≈0.1, ϵ = 0.6, ¯yt = 2.63, σyt = 0.55 and
q = 4.2.
Those values are taken from Refs. [15, 36].
TCM model functions include additional factor 2/3 rep-
resenting ∆η = 2 and TR azimuth acceptance 1/3 of 2π.
The N⊥TCM has one free parameter: the degree to
which a Pj trigger condition alters the eﬀective MB dijet
frequency f ≡(1/σNSD)dσjet/dη relative to fNSD ≈0.1
or the fraction of hard events λh. The bold solid curve H
corresponds to λh →0.5, implying that 50% of triggered
events include at least one dijet within acceptance ∆η
(i.e. are hard events). It also implies that 50% are soft
events with no signiﬁcant jet structure despite a “jet”
trigger. When that H is incorporated into Eq. (5) the
dash-dotted curve describing Pj > 5 GeV/c data results.
The upper solid curve corresponding to λh ≈1 is con-
sistent with Pj > 30 GeV/c data below pt ≈3 GeV/c
but falls increasingly below the data above that point.
In contrast, the Pj > 2 GeV/c data are consistent with
soft component S alone (λh ∼f ≈0), i.e. negligible dijet
production. Those results can be compared with Fig. 12
(left) plotted in terms of 200 GeV single-particle yt,trig.
For Pj > 2 or > 5 GeV/c triggers the data suggest sup-
pression at higher pt due to the trigger condition.
Figure 13 (right) shows the same data and curves on
transverse rapidity yt with factor 1/yt added. While pt
may be directly measured, details at smaller pt are ob-
scured compared to yt. The linear power-law trend evi-
dent at larger yt (compare with the dotted line at right) is
consistent with an underlying MB jet spectrum [15, 16].
dN⊥/dpt data for the Pj > 5 GeV/c trigger condition re-
veal spectrum structure consistent with a TCM descrip-
tion of triggered events where 50% (hard events) have at
least one MB jet per unit η and the complement (soft
events) have none. Data for the Pj > 2 GeV/c condition
suggest that almost all events are soft: The condition
4 Because jet spectra are steeply falling imposed lower limit Pj is
eﬀectively the same as the mode and mean value. Since PT 1 or
Pj represents the highest jet momentum it is also an upper limit.
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
0
2
4
6
8
pt (GeV/c)
dN⊥ / dpt (GeV/c)-1
H
S
NSD
Pj > 2 GeV/c
Pj > 5 GeV/c
Pj > 30 GeV/c
1.8 TeV p-p
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
2
3
4
5
yt
dN⊥ / ytdyt
S
H
NSD
|η| < 1
pt > 0.5 GeV/c
FIG. 13:
Left: TR pt spectra dN⊥/dpt for 1.8 TeV p-p
collisions from Fig. 37 of Ref. [51] within pt > 0.5 GeV/c
and |η| < 1 for jet triggers Pj > 5 (solid points), Pj > 2
(open circles) and for Pj > 30 GeV/c (triangles). Curve S
(dashed) is a TCM soft component with data normalization
corresponding to soft-component density ¯ρs = ns/∆η = 4.2.
NSD H is a 1.8 TeV hard component predicted from ¯ρs = 4.2
per Refs. [15, 36].
The dash-dotted curve is S + H for
Pj > 5 GeV/c. Right: Data and curves at left transformed to
dN⊥/ytdyt with Jacobian mt/yt. The vertical dotted line cor-
responds to pt = 0.5 GeV/c. The dotted line at right relates
to a power-law trend for an underlying MB jet spectrum.
that the highest “jet” momentum is ≈2 GeV/c is an ef-
fective antijet trigger. The Pj > 30 GeV/c data are con-
sistent both with a higher hard-event fraction (λh ≈1)
and with a biased jet spectrum that deviates substan-
tially from a MB distribution, as might be expected.
The trigger bias illustrated by the Pj > 30 GeV/c data
spectra in Fig. 13 refers back to the two solid curves in
Fig. 12 (right). The lower solid curve there corresponds
to the upper (thin) solid curve in Fig. 13 (left) assum-
ing no bias of the underlying jet spectrum and λh ≈1
(all hard events, each including at least a single dijet).
The upper solid curve in Fig. 12 (right) corresponds to a
25% increase of ϵ2¯nch,j that accommodates the 1.8 TeV
N⊥(PT 1) data. That increase can be compared with the
diﬀerence between the TCM upper thin solid curve in
Fig. 13 (left) and Pj > 30 GeV/c data (open triangles).
In summary, application of a jet momentum (Pj) trig-
ger has two consequences for dN⊥/dpt spectra: (a) the
fraction of hard events is altered from untriggered NSD
– greater or lesser depending on the trigger value – and
(b) the eﬀective jet spectrum is biased in a manner
also depending on the trigger value relative to a most-
probable jet energy near 3 GeV. The TCM soft- and
hard-component curves in Fig. 13 are predictions based
on independent jet- and hadron-spectrum measurements
with no adjustment to accommodate N⊥data. It is es-
pecially notable that three distinct trigger conditions re-
tain the same spectrum soft component S. Fixed S ar-
gues against assumptions that a jet-momentum trigger
condition should bias to more-central p-p collisions with
greater soft or UE charge densities (activity) [25], in-
stead buttresses the conclusion that centrality plays no
role in p-p collisions [3, 20]. N⊥pt spectrum behavior ap-
pears to conﬁrm a jet spectrum lower bound near 3 GeV


## Page 19


19
(a 2 GeV/c jet trigger eﬀectively excludes jets entirely
whereas a 5 GeV/c trigger selects a 50-50 mixture of soft
and hard events).
The N⊥pt spectrum also conﬁrms
that the trigger jet makes a substantial contribution to
the TR (the N⊥hard component changes dramatically
with varying trigger pt condition).
VIII.
DISCUSSION
This section considers several issues relating to the
PMC: (a) ﬂuctuations vs correlations vs MB dijets – re-
lating ﬂuctuation and correlation measurements of sev-
eral types to the PMC, (b) direct jet counting from data –
comparing diject production inferred from data to PMC
assumptions about MPIs, (c) a universal TCM soft com-
ponent that appears to dominate hadron production ac-
cording to several data manifestations but has no coun-
terpart within the PMC and (d) the PMC CR mechanism
compared to measured FFs and pt spectrum trends.
A.
Fluctuations vs correlations vs MB dijets
Fluctuations and correlations of total nch and total Pt
integrated within some angular acceptance (∆η, ∆φ) are
intimately related but conventionally treated as indepen-
dent topics. For instance, the well-studied structure of
P(nch) distributions as in Sec. III A is not considered in
parallel with corresponding P(Pt) distributions. In ei-
ther case distribution structure is strongly inﬂuenced by
a hard-component contribution from MB dijets [42, 49]
quadratically related to the soft component [2, 3, 36].
Within an A-A context deﬁned by expectations for QGP
formation, systematic trends for ensemble-mean ¯pt ≡
¯Pt/nch (radial ﬂow?) [40] are considered independently
of ﬂuctuations in eventwise mean ⟨pt⟩≡⟨Pt/nch⟩(tem-
perature ﬂuctuations?) [53], although data suggest that
both trends are again dominated by MB dijets as the
common element [37, 49]. Forward-backward (FB) nch
(but not Pt?) correlations on η (Sec. III D) are treated in
isolation, although FB correlations represent a 1D projec-
tion of 2D angular correlations on (η∆, φ∆) (Sec. VII B),
again dominated by MB dijets [3] and directly related to
nch and Pt ﬂuctuations and correlations [30, 49].
The assumed sources of ﬂuctuations are quite diﬀerent
for PMC and TCM. In a PMC context particle and pt
ﬂuctuations result primarily from p-p centrality variation
(modeled by geometric Glauber MC based on eikonal ap-
proximation) and Poisson ﬂuctuations of MPI number.
In a TCM context the relevance of p-p centrality is
challenged by the noneikonal quadratic relation between
soft and hard components – jet production ∝¯ρh ∝¯ρ2
s.
The soft component dominates, and for NSD p-p col-
lisions multiple dijets within a typical ∆η acceptance
(MPIs) are unlikely. Hard events with at least one di-
jet comprise only a few percent of the total at 200 GeV.
Instead, the most likely source of nch or ¯ρs ﬂuctuations is
the splitting cascades within inelastically-scattered pro-
jectile protons leading to large ﬂuctuations of the soft
component.5 Given ¯ρh ∝¯ρ2
s, dijet production must ﬂuc-
tuate to a greater degree (e.g. see Fig. 3 of Ref. [20]).
How those ﬂuctuations are revealed in statistical mea-
sures depends critically on the measure deﬁnition [42, 55].
For instance, the variance of integrated Pt within some
acceptance σ2
Pt = (Pt −¯Pt)2, with ¯Pt an ensemble mean,
is sensitive to all Pt ﬂuctuations [56]. However, condi-
tional variance σ2
Pt|nch ≡(Pt −nchˆpt)2, with ˆpt a single-
particle ensemble mean, is sensitive only to ﬂuctuations
in integrated Pt relative to what would be expected for
nch ﬂuctuations with ﬁxed ˆpt in every event [49]. Its scale
(bin size) dependence can be inverted to reconstruct un-
derlying pt angular correlations [30]. Those angular cor-
relations, e.g. from 200 GeV Au-Au collisions with N-N
collisions as a limit, are dominated by MB dijet struc-
ture [49, 57], a result consistent with Secs. V B and VII B
for p-p collisions. Equation (16) suggests that p-p charge
(number) nch ﬂuctuations are also associated with MB
dijets as the dominant source of two-particle correlations
near midrapidity (see Sec. VII B), one of several jet man-
ifestations represented by the TCM hard component.
B.
Jet counting and jet-related correlations
As a response to the PMC assumption that almost all
hadron production must result from MPIs it is possible
to derive actual jet production rates from several data
formats that present a consistent picture of the role of
MB dijets and are consistent with the TCM soft com-
ponent as the dominant mechanism for hadron produc-
tion. For example, jet-related angular correlations from
A-A collisions can be analyzed to determine the absolute
mean dijet number as a function of A-A centrality [35].
Such estimates are consistent with results from TCM pt
spectrum analysis [2, 3, 16], from ensemble-mean ¯pt anal-
ysis [37] and from jet spectrum analysis [15]. In each case
maximum information is derived from diverse data for-
mats and collision systems to develop a consistent TCM.
In contrast, the PMC addresses less-diﬀerential data
formats (e.g. the pedestal eﬀect, P(nch), FB correlations)
that do not include actual jet counting.
A restricted
data set is accommodated with a combination of jet spec-
trum lower cutoﬀp⊥0 and CR mechanism (variable FFs),
both adjusted to ﬁt data.
The TCM soft component
that is required by several data trends (e.g. spectrum [2]
and angular-correlations [3] nch dependence) is excluded,
leading to a requirement for unrealistically large dijet
production at very low jet energies (below 2 GeV [51])
5 “The proton substructure is represented by a parton [splitting]
cascade, which at high energies is described by BFKL evolution.
The ﬂuctuations in this evolution are known to be very large
[Ref. [54] of the present paper].” G. Gustafson, Ref. [14] p. 43.


## Page 20


20
where fragmentation to jets is unmeasured and unlikely.
The lower limit on jet energies is not λQCD but the den-
sity of hadronic ﬁnal states. For a jet spectrum termi-
nating near 3 GeV [15] the lowest-energy “jets” consist of
charge-neutral hadron (pion) pairs [31, 32]. Jet produc-
tion must then be strongly inhibited below that point.
C.
TCM soft component as true underlying event
The UE is conventionally deﬁned as complementary to
a triggered high-pt dijet and is by hypothesis expected to
include beam-beam remnants (projectile-nucleon disso-
ciation products), initial-state radiation and MPIs [51].
The UE is therefore ill-deﬁned because the triggered dijet
is conventionally misrepresented (illustrated for instance
in Sec. VII B) in that any dijet includes a substantial con-
tribution to the TR region not typically acknowledged.
In contrast, the TCM soft component is well-deﬁned phe-
nomenologically, with consistent manifestations in yields,
spectra and correlations, and is equivalent to “beam rem-
nants” within the context of the PMC. What should be
the established reference (soft component) is confused
with the ill-deﬁned UE, whereas what should be the ob-
ject of study – high-pt jets – is adopted as the reference.
As noted in Sec. II A soft events (“diﬀractive events”
with no MPI) are assumed to be rare. “Such events [with
no apparent hard scatter] are associated with nonpertur-
bative low-p⊥physics, and are simulated by exchang-
ing a very soft gluon between the two colliding hadrons,
making the hadron remnants colour-octet objects rather
than colour-singlet ones” [9].
The possibility that one
or two color singlets (e.g. soft or hard Pomerons) are
exchanged [11, 12] is not considered.
The statement
“Translated into modern terminology, each cut pomeron
corresponds to the exchange of a soft gluon, which results
in two ‘strings’ being drawn between the two beam rem-
nants” [9] implies that part of the soft component is ex-
cluded from the beam remnants, whereas the statement
“For PYTHIA we include particles that arise from the
soft or semi-hard scattering in multiple parton interac-
tions [MPIs] in the beam-beam remnant component” [51]
implies that beam remnants as simulated by the PMC
include MPIs as well as some unspeciﬁed fraction of the
projectile dissociation component.
Within the PMC model the “hard component” (i.e.
MPIs) must represent the entire pt spectrum. As a con-
sequence “The charged particle p⊥spectrum is underes-
timated at low p⊥scales” [8]. In contrast, the TCM soft
component is required by a broad array of data and de-
scribes the low-pt portion of hadron spectra within data
uncertainties, as demonstrated in Figs. 1 and 2.
The
spectrum soft component has a universal form with ﬁxed
slope parameter T ≈145 MeV corresponding to ﬁxed
¯pt soft component ¯pts ≈0.4 GeV/c consistent with all
presently available ¯pt data [37].
As demonstrated in Sec. VII D an imposed jet pt trig-
ger may bias the higher-pt hadron distribution (hard
component) but does nothing to inﬂuence the lower-pt
soft component, which qualiﬁes as the true “underlying
event” complementary to all dijet production. That a pt
trigger may prefer hard events but does not change the
soft-component multiplicity implies both that soft/hard
ratio in triggered events is no diﬀerent from NSD and that
p-p centrality is not a relevant degree of freedom, con-
tradicting Ref. [25] and the PMC. That all jet-triggered
events maintain the same ¯pt is also explained: the ratio of
TCM soft vs hard components in Eq. (11) remains ﬁxed.
D.
Color reconnection and MB dijets
The PMC must include a CR mechanism to accom-
modate ¯pt vs nch data [40], as noted in Sec. VI C. The
CR mechanism is in eﬀect equivalent to FFs strongly de-
pendent on scattered-parton (MPI) density.
Within a
TCM context FFs, such as Dpp in Eq. (8), are approx-
imately independent of the p-p collision system as im-
plied by TCM analysis of p-p spectrum data over a large
collision-energy interval [36]. ¯pt variation with nch is in-
terpreted to arise from noneikonal quadratic increase of
dijet production with increasing nch [3, 37].
According
to
assumptions
supporting
the
PMC
(Sec. III B) each MPI should contribute “the same
(semi)hard p⊥kick” [8] (e.g. some ¯pt0) to integrated ¯Pt
while the “hadrons per string” (jet fragment multiplicity)
would decrease with increasing ¯nMP I. That hypothesis
can be represented by rearranging Eq. (11) (with ξ →1)
describing ¯pt data within their statistical uncertainties
¯pt ≡
¯Pt
nch
≈
¯pts + x(ns)¯pth(ns)
1 + x(ns)
→
¯pt0 ¯nMP I
nch(¯nMP I)
(22)
2¯nch,j ≈nch(¯nMP I)
¯nMP I
≈¯pt0
¯pts
·
1 + α¯ρs
1 + α¯ρs ¯pth0/¯pts
,
where the second line gives the PMC mean fragment mul-
tiplicity per MPI via ¯pts ≈0.4 GeV/c from Fig. 9 (left),
¯pth0 ≈1.2 GeV/c from Fig. 9 (right), α ≈O(0.01) from
Eq. (A3) and ¯pt0, a free parameter within the CR model.
The CR-related expression then implies that the mean
jet fragment yield 2¯nch,j should decrease asymptotically
by factor 1/3 as nch (and dijet multiplicity) increases.
That relation contradicts the systematics of jet frag-
mentation wherein a ﬁxed mean fragment multiplicity
per dijet is determined by 2¯nch,j =
R
dyt ¯D(yt) with
¯D(yt) given by measured jet properties combined as in
Eq. (8). Data indicate that 2¯nch,j, described by Eq. (A4),
changes with p-p collision energy but not with nch or ¯ρs
and therefore does not depend on parton density (MPI
number?), which contradicts the PMC CR model. From
spectrum data 2¯nch,j =
R
dytytH(yt)/ϵfNSD actually in-
creases slightly with nch increase corresponding to 100-
fold increase of dijet production (Fig. 10 and Ref. [36]).


## Page 21


21
IX.
SUMMARY
The PYTHIA Monte Carlo (PMC) model of high-
energy p-p collisions, motivated by certain data features
emerging from the super proton-antiproton synchrotron
(Sp¯pS) program, includes several basic assumptions: (a)
almost all hadrons arise from multiparton interactions
(MPIs) described by perturbative QCD (pQCD), (b) the
scattered-parton (jet) spectrum extends down to zero pt
(or jet energy), (c) a color reconnection (CR) mechanism
controls parton fragmentation to jets and (d) p-p central-
ity, modeled by a geometric Glauber model based on the
eikonal approximation, controls hadron production.
The two-component (soft + hard) model (TCM) of
hadron production, introduced concurrently with the
PMC, provides an alternative description of hadron pro-
duction in A-B collisions. The TCM was inferred induc-
tively from measured data trends and describes a broad
array of collision systems and data formats accurately.
Whereas the PMC is a one-(hard)-component model the
TCM soft component appears to be required by data, e.g.
pt-spectrum, η-density and two-particle-correlation data
for 200 GeV p-p collisions. In any collision system the
TCM soft component represents the majority of hadrons.
The dijet-related TCM hard component exhibits a
noneikonal quadratic dependence on the soft component
interpreted to represent participant low-x partons (glu-
ons). The quadratic trend remains accurate at the per-
cent level over a soft-component range corresponding to
100-fold increase in dijet production.
The noneikonal
trend suggests no dependence on p-p centrality: each par-
ticipant parton in one projectile proton may interact with
any participant in the partner proton – all or nothing.
Diﬀerential spectrum analysis reveals that the TCM
model (including soft component) describes pt spec-
tra accurately down to very low pt, whereas the PMC
(hard component only) model fails at lower pt. The pt-
spectrum TCM hard component is predicted by convo-
luting jet spectra having a lower bound near 3 GeV with
fragmentation functions independent of parton density
(i.e. no CR) and consistent with measurements.
Detailed analysis of 2D angular correlations reveals
that any dijet from a MB ensemble must make a substan-
tial contribution to the “trans” region (TR) (including
φ = π/2 relative to the trigger direction) of azimuth an-
gular correlations that is assumed to be especially sensi-
tive to the underlying event (UE) for jet-triggered events.
Imposing a jet trigger (e.g. jet pt sum) results in contribu-
tions of the triggered jet to the TR, contradicting a basic
PMC assumption. The trigger condition does not change
the soft component, arguably the real “underlying event”
for any collision conditions, which also appears inconsis-
tent with any connection to p-p centrality dependence.
In conclusion, a variety of data manifestations is incon-
sistent with the basic assumptions of the PMC, whereas
the TCM is consistent with a large body of jet measure-
ments and provides a simple and accurate representation
of hadron production in a variety of collision systems.
These results have implications for other Monte Carlos
derived from the PMC, such as HIJING and AMPT.
Appendix A: TCM Hard-component collision-energy
dependence
This appendix combines MB dijet collision-energy de-
pendence in Sec. VI A and TCM hadron pt spectrum
collision-energy trends in Secs. V A and VI B to sup-
port UE analysis in Secs. VII C and VII D that requires
additional TCM elements. The object is self-consistent
quantitative representation of single-particle yields and
pt spectra vs N⊥yields and spectrum
1.
p-p spectra and MB dijets
The TCM hard component (various manifestations) is
related to QCD jets by the following expressions
¯ρh(nch, √s) = α(√s)¯ρ2
s
(A1)
= f(nch, √s) ϵ2¯nch,j(√s),
where the ﬁrst line is derived from p-p pt spectrum anal-
ysis [2, 3] and the second line is derived from jet analy-
sis [15]. From spectrum studies ¯ρs ≈0.81∆yb [36] with
∆yb = ln(√s/10 GeV). From jet systematics and a mea-
sured NSD cross section trend [15] the per-NSD-event
dijet η density is
fNSD ≡
1
σNSD
dσj
dη

NSD
≈0.037∆ymax∆y2
b
32 + ∆y2
b
, (A2)
where ∆ymax ≡ln(√s/6 GeV) and σNSD ≈0.85(32 +
∆y2
b). The trend of α(√s) values inferred from p-p pt
spectra [36] is given by
α ≈0.02 ∆y2
max
32 + ∆y2
b
.
(A3)
Combining Eqs. (A1), (A2) and (A3) gives [36]
2¯nch,j(√s) ≈0.60∆ymax
(A4)
and Eq. (A1) becomes
¯ρh ≈0.013∆y2
max∆y2
b
32 + ∆y2
b
.
(A5)
Table I presents NSD values from those relations eval-
uated for √s = 200 and 1800 GeV assuming accepted
dijet fraction ϵ ≈0.6 for acceptance ∆η ≈2.
The expressions above estimate NSD TCM parame-
ter values for any √s. For p-p collision ensembles other
than NSD (e.g. with some nch condition imposed) cor-
responding parameter values can be obtained by scal-
ing.
For instance f(nch) = (¯ρs/¯ρsNSD)2fNSD reﬂects
the noneikonal quadratic dependence of MB dijet pro-
duction on TCM soft component ¯ρs (i.e. ∝∆y2
b). On


## Page 22


22
TABLE I: TCM and jet parameters for NSD p-p collisions at
two energies. Must rescale otherwise based on above relations.
√s (GeV) ∆yb ∆ymax ¯ρsNSD
α
fNSD 2¯nch,j ¯ρhNSD
200
3.0
3.5
2.43
0.006 0.028
2.1
0.035
1800
5.2
5.7
4.20
0.011 0.097
3.4
0.20
the other hand, α(√s) and 2¯nch,j(√s) do not appear to
depend on p-p nch, and their energy dependence is con-
trolled by ∆ymax which measures the width of MB jet
spectra [15]. The lack of nch dependence for mean di-
jet fragment multiplicity 2¯nch,j(√s) suggests that parton
fragmentation does not depend on scattered-parton den-
sity (over a 100-fold variation [2, 3]) as implied by the CR
mechanism described in Refs. [8, 9]. Imposition of a pt
condition (single-particle pt,trig or jet sum Pj) on events
requires a diﬀerent treatment as reported in Ref. [20] and
summarized brieﬂy in Sec. VII C
2.
TR N⊥predictions from the TCM
The results of the previous subsection can be used to
predict TR N⊥trends. The TR pedestal eﬀect is related
to a varying pt (PT 1) condition placed on p-p collisions.
If hadron production in the TR were unbiased (no con-
dition) one expects the TCM spectrum description
3
2
dN⊥
ptdpt
= ¯ρs ˆS0(pt) + ¯ρh ˆH0(pt).
(A6)
Integrating that expression over the CDF pt acceptance
(pt > 0.5 GeV/c) gives [using unit-integral TCM ˆS0(pt)
and ˆH0(pt) models interpolated to 1.8 TeV [36]]
3
2N⊥= 0.25¯ρs + 0.95¯ρh.
(A7)
If a PT 1 condition is imposed such that only hard events
are selected (but with NSD soft and hard components)
then in Eq. (A1) ¯ρh →ϵ2¯nch,j, i.e. f →1. In that case
N⊥=
2
3(0.25 ¯ρs + 0.95 ϵ2¯nch,j)
(A8)
→0.70 + 1.29 ≈2.0
using NSD values from Table I. That asymptotic value
corresponds to the lower solid curve in Fig. 12 (right)
assuming that the TCM hard component is unbiased by
the imposed pt condition. Figure 13 makes clear that the
spectrum in the TR is biased by the trigger condition,
with an eﬀective increase of 2¯nch,j by factor 1.25. Note
that for 100% pt acceptance the saturation value becomes
N⊥→0.7/0.25 + 1.25 · 1.29/0.95 ≈2.8 + 1.7 = 4.5. That
is, ﬁxed soft component S actually dominates N⊥.
Appendix B: TCM description of ρ0(η) distributions
TCM η densities ¯ρ0, ¯ρs and ¯ρh appearing in Eqs. (5) are
mean values of diﬀerential densities ρx(η) averaged over
some acceptance ∆η. The hadron density near midrapid-
ity is represented by joint density ρ0(yt, η; nch). Based on
results from spectrum analysis in Ref. [2] the basic TCM
decomposition is given by the ﬁrst line of
ρ0(yt, η; n′
ch) = S(yt, η; n′
ch) + H(yt, η; n′
ch) (B1)
≈ρs0(n′
ch)S0(η) ˆS0(yt)
+ ρh0(n′
ch)H0(η) ˆH0(yt),
where n′
ch (with prime) is an uncorrected multiplicity
within ∆η. The second line invokes factorization of soft
and hard components. Soft component S(yt, η; n′
ch) is as-
sumed factorizable within some limited acceptance ∆η.
Hard component H(yt, η; n′
ch) may include signiﬁcant η-
yt covariances but factorization is also assumed here.
Unit integral (denoted by carets) spectrum models ˆS0(yt)
and ˆH0(yt) are as deﬁned in Ref. [2] over the full yt ac-
ceptance.
Model functions S0(η) and H0(η) on η are
newly deﬁned below, and the ρx0 represent soft and hard
hadron densities at η = 0 (not averaged over ∆η).
Integrating Eq. (B1) over a pt or yt acceptance with
nonzero lower limit (e.g. pt,cut ≈0.15 GeV/c) leads to
ρ′
0(η; n′
ch) ≈ρ′
s0(n′
ch)S0(η) + ρh0(n′
ch)H0(η)(B2)
ρ′
0(η; n′
ch, ∆η) ≈¯ρ′
s(n′
ch, ∆η) ˜S0(η; ∆η)
+ ¯ρh(n′
ch, ∆η) ˜H0(η; ∆η) within ∆η
where ˜X0(η; ∆η) ≡X0(η)/ ¯X0(∆η) are unit integral on
∆η, ¯ρx are charge densities averaged over ∆η and it is
assumed that the pt acceptance cut does not aﬀect the
hard component. The goal of analysis is to infer TCM
models ˜S0(η; ∆η) and ˜H0(η; ∆η) from ρ′
0(η; n′
ch) data.
Figure 14 (left) shows measured density distributions
dn′
ch/dη for seven nch classes of 200 GeV p-p collisions
normalized by uncorrected soft component ¯ρ′
s = n′
s/∆η
inferred from n′
ch values assuming α = 0.006 [3, 36]. Cor-
rected charge density ¯ρ0 varies from 1.76 to 18.8 corre-
sponding to a 100-fold increase in dijet production. An
η-symmetric ineﬃciency λ(η) ≤1 deviates from unity
only for two outer bins at the ends of the η acceptance.
The plotted data are corrected for λ(η), but a common
η-asymmetric distortion 1+g(η) remains due to diﬀerent
tracking eﬃciencies in two halves of the TPC detector.
Figure 14 (right) shows asymmetry-corrected renor-
malized densities ρ′
0(η; n′
ch)/¯ρ′
s(n′
ch)[1 + g(η)] (points).
Solid curves through data are described by Eq. (B2)
(lower line) with soft and hard model functions deﬁned
below. Dashed curve ˜S0(η) is deﬁned by Eq. (B5), the
soft-component limit to the ratio ρ′
0(η)/¯ρ′
s as n′
ch →0.
Data are modeled by ﬁxed ˜S0 plus hard component ∝¯ρs.
An iterative analysis method is described in detail in
Ref. [3].
Brieﬂy, diﬀerences between adjacent pairs of
multiplicity classes in Fig. 14 (right) are used to obtain


## Page 23


23
0.9
1
1.1
1.2
1.3
1.4
1.5
1.6
-1
-0.5
0
0.5
1η
[1/λ(η)] dnch′/dη / ρs′(nch′)
n = 1
n = 7
0.9
1
1.1
1.2
1.3
1.4
1.5
1.6
-1
-0.5
0
0.5
1
η
ρ0′(η,nch′) / ρs′(nch′) [1+g(η)]
S0
n = 1
n = 7
FIG. 14:
Left: Uncorrected η densities within ∆η = 2 for
seven multiplicity classes denoted by index n [3]. The curves
connecting data points guide the eye.
Right: Corrected η
densities within ∆η = 2 for seven multiplicity classes. The
dashed curve is normalized soft-component model ˜S0(η) ≡
S0(η)/ ¯S0(∆η) from Eq. (B5). The solid curves are Eq. (B2)
with TCM elements deﬁned in Eqs. (B3) and (B5).
estimates of (¯ρh/¯ρ′
s) ˜H0(η; ∆η) per Eq. (B2) (second line).
The ensemble of data diﬀerences is used to determine the
common hard-component model
˜H0(η; ∆η) ≡
H0(η)
¯H0(∆η) = 1.47 exp[−(η/0.6)2/2]. (B3)
With a provisional hard-component model deﬁned the
soft-component model is estimated from data as follows.
Figure 15 (left) shows the soft-component estimator
Sn(η)
¯S0(∆η) ≡ρ′
0(η)n/¯ρ′
s,n −(¯ρh,n/¯ρ′
s,n) ˜H0(η; ∆η), (B4)
for each multiplicity class n with ˜H0(η; ∆η) as deﬁned in
Eq. (B3). The inferred soft-component model for ∆η = 2
(solid curve) is deﬁned by
˜S0(η; ∆η)≡S0(η)
¯S0(∆η) = 1.09 −0.18 exp[−(η/0.44)2/2].(B5)
The form of the soft component appears to be stable
over a large nch interval. Small data deviations from the
model are consistent with statistical uncertainties. The
minimum at η = 0 is expected given the Jacobian for
η ↔yz, where an approximately uniform density on yz is
expected within a limited ∆yz acceptance about yz = 0.
Figure 15 (right) shows the hard component re-
estimated from ρ′
0(η; n′
ch) data using an alternative
method that assumes model ˜S0(η; ∆η) from Eq. (B5)
Hn(η)
¯H0(∆η) ≡ρ′
0(η)n/¯ρ′
s,n −˜S0(η; ∆η)
¯ρh,n/¯ρ′s,n
,
(B6)
which substantially reduces statistical noise in the diﬀer-
ences. The dashed curve is the hard-component model
˜H0(η; ∆η) deﬁned by Eq. (B3) demonstrating the overall
self-consistency of the TCM. The hard-component den-
sity in the right panel suggests that hadron fragments
from MB dijets are strongly peaked near η = 0, localized
0.85
0.9
0.95
1
1.05
1.1
1.15
-1
-0.5
0
0.5
1
η
S(η) / S0(∆η)
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
-1
-0.5
0
0.5
1
η
H(η) / H0(∆η)
FIG. 15:
Left: Data soft-component estimates as in Eq. (B4).
The solid curve is normalized soft-component model ˜S0(η) as
deﬁned by Eq. (B5). Right: Data hard-component estimates
as in Eq. (B6). The solid curve is normalized hard-component
model ˜H0(η) as deﬁned by Eq. (B3). The data for n = 1 (solid
dots) are signiﬁcantly low compared to the common trend.
mainly within ∆η = 2 and consistent with the dominant
dijet source being low-x gluons corresponding to small
yz or η. The functional form on η is also consistent with
a peaked “gluon-gluon source” component predicted by
Ref. [58]. Its N gg
ch ∝ln3(sNN/s0) collision-energy depen-
dence can be compared with Eq. (7) (ﬁrst line) below.
In summary, ¯ρ0(η) density distributions present an-
other case where TCM soft and hard components are
accurately separable, are quite diﬀerent (for understand-
able reasons) and do not share a common production
mechanism (i.e. MPIs) as assumed for the PMC.
[1] T. Sj¨ostrand, S. Mrenna and P. Z. Skands, Comput. Phys.
Commun. 178, 852 (2008); T. Sj¨ostrand, Comput. Phys.
Commun. 82, 74 (1994);
[2] J. Adams et al. (STAR Collaboration), Phys. Rev. D 74,
032006 (2006).
[3] T. A. Trainor and D. J. Prindle, Phys. Rev. D 93, 014031
(2016).
[4] A. Buckley et al., Phys. Rept. 504, 145 (2011).
[5] C. Patrignani et al. (Particle Data Group), Chin. Phys.
C 40, no. 10, 100001 (2016).
[6] B.
Andersson,
G.
Gustafson,
G.
Ingelman
and
T. Sj¨ostrand, Phys. Rept. 97, 31 (1983).
[7] T. A. Trainor and D. T. Kettler, Phys. Rev. D 74, 034012
(2006).
[8] T. Sj¨ostrand, arXiv:1706.02166].
[9] T. Sj¨ostrand and P. Z. Skands, JHEP 0403, 053 (2004).
[10] C. Albajar et al. (UA1 Collaboration), Nucl. Phys. B
309, 405 (1988).


## Page 24


24
[11] A. Donnachie and P. V. Landshoﬀ, Phys. Lett. B 437,
408 (1998).
[12] E. Levin, hep-ph/9808486.
[13] T. Sj¨ostrand and M. van Zijl, Phys. Rev. D 36 2019
(1987).
[14] P. Bartalini et al., arXiv:1111.0469.
[15] T. A. Trainor, Phys. Rev. D 89, 094011 (2014).
[16] T. A. Trainor, Phys. Rev. C 80, 044901 (2009).
[17] G. Pancheri and Y. Srivastava, Conf. Proc. C 850313,
28 (1985) [Phys. Lett. B 159, 69 (1985)].
[18] X.-N. Wang, Phys. Rev. D 46, R1900 (1992); X.-N. Wang
and M. Gyulassy, Phys. Rev. D 44, 3501 (1991).
[19] D. Kharzeev and M. Nardi, Phys. Lett. B 507, 121
(2001).
[20] T. A. Trainor, Phys. Rev. D 87, 054005 (2013).
[21] Z. Koba, H. B. Nielsen and P. Olesen, Nucl. Phys. B 40,
317 (1972).
[22] G. Altarelli and L. Di Lella, SINGAPORE: WORLD
SCIENTIFIC (1989) 404 P. (ADVANCED SERIES ON
DIRECTIONS IN HIGH ENERGY PHYSICS, 4).
[23] J. Adam et al. (ALICE Collaboration), Eur. Phys. J. C
77, no. 1, 33 (2017).
[24] R. Field, Acta Phys. Polon. B 42, 2631 (2011).
[25] L. Frankfurt, M. Strikman and C. Weiss, Phys. Rev. D
83, 054012 (2011).
[26] J. Adams et al. (STAR Collaboration), Phys. Rev. Lett.
95, 152301 (2005).
[27] T. A. Trainor, Phys. Rev. C 81, 014905 (2010).
[28] Y. L. Dokshitzer and D. E. Kharzeev, Ann. Rev. Nucl.
Part. Sci. 54, 487 (2004).
[29] B. S. Everitt and A. Skrondal, “The Cambridge Dic-
tionary of Statistics,” 4th Ed., (Cambridge University
Press, Cambridge, 2010), p. 107.
[30] T. A. Trainor, R. J. Porter and D. J. Prindle, J. Phys. G
31, 809 (2005).
[31] R. J. Porter and T. A. Trainor (STAR Collaboration), J.
Phys. Conf. Ser. 27, 98 (2005).
[32] R. J. Porter and T. A. Trainor (STAR Collaboration),
PoS CFRNC2006, 004 (2006).
[33] G. Agakishiev, et al. (STAR Collaboration), Phys. Rev.
C 86, 064902 (2012).
[34] J. Adams et al. (STAR Collaboration), Phys. Rev. C 73,
064907 (2006).
[35] T. A. Trainor and D. T. Kettler, Phys. Rev. C 83, 034903
(2011).
[36] T. A. Trainor, J. Phys. G 44, no. 7, 075008 (2017).
[37] T. A. Trainor, arXiv:1708.09412.
[38] T. A. Trainor, arXiv:1801.05862.
[39] B. B. Abelev et al. (ALICE Collaboration), Phys. Lett.
B 728, 25 (2014).
[40] B. B. Abelev et al. (ALICE Collaboration), Phys. Lett.
B 727, 371 (2013).
[41] T. A. Trainor, Phys. Rev. C 91, 044905 (2015)
[42] T. A. Trainor, arXiv:1701.07866.
[43] T. Akesson et al. (Axial Field Spectrometer Collabora-
tion), Phys. Lett. B 123, 133 (1983).
[44] J. Alitti et al. (UA2 Collaboration), Phys. Lett. B 257,
232 (1991).
[45] D. Acosta et al. (CDF Collaboration), Phys. Rev. D 68,
012003 (2003).
[46] J. Adam et al. (ALICE Collaboration), Phys. Lett. B
753, 319 (2016).
[47] C. Albajar et al. (UA1 Collaboration), Nucl. Phys. B
335, 261 (1990).
[48] G. J. Alner et al. (UA5 Collaboration), Z. Phys. C 32,
153 (1986).
[49] J. Adams et al. (STAR Collaboration), J. Phys. G 32,
L37 (2006).
[50] F. Abe et al. (CDF Collaboration), Phys. Rev. D 56,
3811 (1997).
[51] T. Aﬀolder et al. (CDF Collaboration), Phys. Rev. D 65,
092002 (2002).
[52] M. B. De Kock, H. C. Eggers and T. A. Trainor, Phys.
Rev. C 92, no. 3, 034908 (2015).
[53] B. B. Abelev et al. (ALICE Collaboration), Eur. Phys.
J. C 74, 3077 (2014).
[54] A. H. Mueller and G. P. Salam, Nucl. Phys. B 475, 293
(1996).
[55] T. A. Trainor, Phys. Rev. C 92, 024915 (2015).
[56] T. A. Trainor, hep-ph/0001148.
[57] J. Adams et al. (STAR Collaboration), J. Phys. G 34,
451 (2007).
[58] G. Wolschin, Phys. Rev. C 91, no. 1, 014905 (2015).

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1805_09681v1_comparing_the_pythia_monte_carlo_to_a_two_component_soft_hard_model_of_hadro
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2018/1805_09681V1_COMPARING_THE_PYTHIA_MONTE_CARLO_TO_A_TWO_COMPONENT_SOFT_HARD_MODEL_OF_HADRO.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

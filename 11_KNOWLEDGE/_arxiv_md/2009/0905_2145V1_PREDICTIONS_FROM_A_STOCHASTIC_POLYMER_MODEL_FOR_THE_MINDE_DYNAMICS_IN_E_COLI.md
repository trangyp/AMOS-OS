---
canon-group: reference
rscf-state: source-claim
arxiv_id: 0905.2145v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 0905.2145v1_Predictions_from_a_stochastic_polymer_model_for_the_MinDE_dynamics_in_E_coli

> Source: 0905.2145v1_Predictions_from_a_stochastic_polymer_model_for_the_MinDE_dynamics_in_E_coli.pdf

> Pages: 16

---


## Page 1


arXiv:0905.2145v1  [q-bio.SC]  13 May 2009
Predictions from a stochastic polymer model for the MinDE dynamics in E.coli
Peter Borowski∗
Department of Mathematics, University of British Columbia, 1984 Mathematics Road, Vancouver,
BC, V6T 1Z2 Canada; Paciﬁc Institute for the Mathematical Sciences, Vancouver, Canada
Eric N. Cytrynbaum†
Department of Mathematics, University of British Columbia,
1984 Mathematics Road, Vancouver, BC, V6T 1Z2 Canada
(Dated: March 8, 2022)
The spatiotemporal oscillations of the Min proteins in the bacterium Escherichia coli play an
important role in cell division. A number of diﬀerent models have been proposed to explain the
dynamics from the underlying biochemistry. Here, we extend a previously described discrete polymer
model from a deterministic to a stochastic formulation. We express the stochastic evolution of the
oscillatory system as a map from the probability distribution of maximum polymer length in one
period of the oscillation to the probability distribution of maximum polymer length half a period
later and solve for the ﬁxed point of the map with a combined analytical and numerical technique.
This solution gives a theoretical prediction of the distributions of both lengths of the polar MinD
zones and periods of oscillations – both of which are experimentally measurable. The model provides
an interesting example of a stochastic hybrid system that is, in some limits, analytically tractable.
PACS numbers:
87.16.A- Theory, modeling, and simulations 87.17.Ee Growth and division 87.10.Mn
Stochastic modeling
Keywords: Min proteins, polymer dynamics, stochastic oscillations, hybrid dynamical systems
I.
INTRODUCTION
The spatiotemporal oscillations of the Min proteins
in the bacterium Escherichia coli have been well stud-
ied both experimentally and theoretically (see [1] for a
recent review).
Whereas many of the proposed mod-
els [2, 3, 4, 5, 6, 7, 8] describe the oscillations as a
self-organised emergent property of a reaction-diﬀusion
system, only a few [9, 10, 11, 12] address the poly-
mer nature of the relevant proteins that is evident in
both in vitro [13, 14] and in vivo [15, 16] experiments.
Cytrynbaum and Marshall [11] described the oscillatory
dynamics of the Min proteins solely in terms of sim-
ple polymer assembly and disassembly dynamics coupled
with concentration-dependent conditions for switching
between these two states. Much of the experimentally
observed behaviour of wildtype cells can be explained
within this framework as can a number of mutant-study
observations.
Here we analyze a stochastic version of
the model introduced in [11] and build a set of quantita-
tive predictions that can be used to evaluate the model
against data and results of other models.
Our stochastic model consists of a set of four interact-
ing linear polymers, a pair of MinD and MinE polymers
at either pole of the cell, each of which can be in either a
growing or a shrinking state. For any ﬁxed combination
of states for the four polymers, the dynamics are deter-
ministic and described by a system of ordinary diﬀeren-
tial equations for the lengths of the polymers. The full
∗Electronic address: borowski@math.ubc.ca
†Electronic address: cytryn@math.ubc.ca
state of the system is thus determined by four discrete
state variables (growing/shrinking) and four continuous
variables (polymer lengths).
Stochastic transitions be-
tween the discrete states are dependent on the cytoplas-
mic concentrations of the Min proteins and so indirectly
on the polymer lengths.
Cytrynbaum and Marshall [11] analysed a determinis-
tic limit of inﬁnitely high cooperativity, the solutions of
which can be expressed easily in the form of ﬁxed points
of a one-dimensional map which we describe in the ﬁrst
subsection of Sec. IV. Formulating the model in this de-
terministic limit as a map is useful in understanding our
approach to the full stochastic model which we focus on
throughout the rest of Sec. IV. As with the determin-
istic model, the stochastic model can be reduced to a
map, in this case one that takes the probability distri-
bution for the maximum polymer length during a given
period of the oscillation to the probability distribution
for the same quantity half a period later. Our results
include analysis of this probability distribution map and
the calculation of its ﬁxed point. In addition, from the
analytical theory and numerical simulations, we calculate
the distributions of other properties that are easily mea-
sured experimentally. This enables us to narrow down
the parameter regime in which the results of our model
agree with experimental observations. In particular, a
high cooperativity (n ≈6) in the nucleation of the MinE
polymer is required. The cooperativity in nucleation of
the MinD polymer turns out to be less crucial (n ≈3 is
suﬃcient). Also, over a wide range of parameter values,
two stable solutions exist, one in which the Min proteins
are entirely in the cytosol and one in which polymers
form at either pole in an oscillatory manner. Stochastic
transitions between these bistable states are more or less


## Page 2


2
likely depending on parameter values. In the discussion,
we put this ﬁnding into the context of recent experimen-
tal observations [17], and compare our results to other
modelling studies in the literature.
II.
BIOLOGY
It is well established experimentally that two main pro-
cesses control the position at which the rod-shaped bac-
terium E.coli divides. Nucleoid occlusion [18] prevents
division at sites within close proximity of the nucleoid,
which – at the relevant time after DNA replication – is
everywhere in the cell except at the middle and near the
two poles. The latter two sites are ruled out by the coop-
erating action of a group of three proteins, the Min pro-
teins MinC, MinD, and MinE. In E.coli, a spatiotemporal
oscillatory pattern formed by these proteins restricts di-
vision to the middle of the cell.
MinD is an ATPase that, in its ATP-bound form, binds
to the inner cell membrane [19]. MinE is found to acti-
vate the ATPase activity of membrane-bound MinD and
thereby removes MinD from the membrane [20]. MinC
co-localises to membrane-bound MinD [21] and is known
to prevent assembly of FtsZ, one of the important players
in forming the apparatus that constricts the cell during
division [22]. Fluorescent labelling of MinD showed a pre-
ferred localisation to the polar regions of the membrane
and away from midcell [23]. This localisation appears to
be the result of spatiotemporal oscillatory dynamics pro-
duced by the membrane-dependent interaction of MinD
and MinE (for a review see [1]). The still-uncertain mech-
anism by which this oscillation occurs is the motivation
for our work.
The interaction of MinD and MinE in the presence of
ATP and lipid membranes has been studied in vitro and
MinD was found to accumulate into polymers and ﬁbre
bundles above certain concentrations [14]. In vivo, the
ﬂuorescently labelled Min proteins appear to be organ-
ised into helical structures on the inner wall of the cell
membrane [15, 16]. The qualitative agreement between
the in vitro and in vivo observation suggests that the Min
proteins organise in the form of polymers in the cell, an
assumption on which we base our theoretical model.
III.
MODEL – A HYBRID DYNAMICAL
SYSTEM
We assume that both MinD and MinE aggregate only
in the form of polymers on the inner side of the cell’s
membrane. The Min oscillation results from an interplay
between two MinD- and two MinE-polymers, one pair on
each side of the cell.
MinD monomers[34] from the cytosol can start a poly-
mer (i.e. nucleate) at one of the nucleation sites that are
assumed to be positioned at each pole of the cell, an idea
supported by recent experiments [24, 25, 26]. The proba-
bility of nucleation on an empty site is proportional to the
cytosolic MinD concentration raised to the power nnuc.
We assume that each nucleation site, when occupied by
a polymer, is incapable of nucleating a second polymer.
The MinD polymer then elongates towards midcell at a
rate proportional to the cytosolic MinD concentration.
A MinE polymer can nucleate at the growing tip of the
MinD polymer with a probability proportional to the cy-
tosolic MinE concentration raised to the power ncap. It
then grows backwards on top of the MinD polymer with
a rate proportional to the MinE concentration. By in-
ducing hydrolysis, the MinE subunits destabilise the un-
derlying MinD subunits which disassemble from the tip,
releasing both types of subunits into the cytosol.
The geometry of our model cell is that of a cylin-
der with ﬁxed length L and diameter 2r.
Reported
diﬀusion coeﬃcients for the Min proteins are around
10 µm2s−1 [27] so in a cell of length 2 −3 µm and with
characteristic reaction times on the order of seconds, the
cytosolic concentrations of MinD and MinE are essen-
tially uniform throughout the cell. Also, the time scale
of ADP-ATP exchange in cytosolic MinD is assumed to
be fast compared to the oscillatory dynamics [11].
The equations governing the dynamics of the polymers
are distinct for the diﬀerent discrete states between which
the system jumps. The system describing the behaviour
therefore is a hybrid dynamical system – a combination
of continuous and discrete dynamics [28]. In our case, the
continuous variables are four polymer-lengths lD
l/r and lE
l/r
whose dynamics are determined by the values of the re-
spective discrete state variables SD
l/r and SE
l/r. In the fol-
lowing, we will provide the model equations and rephrase
the model introduced in [11] using a slightly diﬀerent no-
tation.
A.
Polymer dynamics
For each of the four polymers (two MinD, two MinE),
we track the projection of the polymers onto the long axis
(x) of the cell (Fig. 1). The four variables lD
l , lE
l , lD
r and
lE
r describe these projected lengths for the polymers at-
tached to the left and right pole of the cell, respectively.
The relation between the full arc length of a helical poly-
mer and its projection is given by l/ cosθ, where θ is the
pitch of the helix. The parameter γ = d cos θ is used to
convert between the projected length l of a polymer and
the number of monomers it is made of (with monomer
size d).
1.
MinD
MinD polymerisation can start at either of two nucle-
ation sites located at the two poles of the cell, i.e. at the
positions x = 0 and x = L. We assume that one end
of the MinD-polymers is ﬁxed to one of these stationary
nucleation sites, whereas at the other end (the ‘tip’), the


## Page 3


3
polymer can elongate or shorten. Growth and shrinkage
are governed by the equations:
d
dtlD
l = γkD(SD
l ),
d
dtlD
r = γkD(SD
r ).
(1)
kD(SD
l/r) represents either constant disassembly or ﬁrst
order assembly and depends on the discrete state variable
SD
l/r of the polymer in question:
kD(SD
l/r) =





kD
oncD
if SD
l/r = 1
(D-polymer growing)
−koﬀ
if SD
l/r = 0
(D-polymer shrinking)
0
if SD
l/r = −1 (no D-polymer)
(2)
The dynamics of switching for the discrete state vari-
ables SD
l/r, between the three states −1, 0 and 1, will be
explained in the next subsection.
The cytosolic concentration cD of MinD is determined
by conservation of monomers:
λ
γV
 lD
l + lD
r

+ cD = cD,to
(3)
where V = πr2L is the volume of the cell (in µm3), λ ≈
1
602 µMµm3 converts between particles per µm3 and µM,
and cD,to is the total concentration of MinD monomers.
The largest possible extension of a D-polymer is
reached when all MinD is bound in one polymer. This is
the case at
lmax = γV
λ cD,to.
(4)
For high total MinD concentrations, lmax can come close
to L, i.e. the D-polymer would cover the whole cell from
pole to pole. To avoid further assumptions on what hap-
pens if a polymer hits the opposite cell wall, we restrict
ourselves here to total MinD concentrations that make
these events very unlikely or impossible. With the pa-
rameters from Tab. II, this means we consider maximal
total MinD concentrations of around 5 µM. In the simu-
lations, the polymer simply stops growing in the unlikely
case that it reaches the opposite cell wall.
2.
MinE
We assume that the MinE polymer nucleates on the
tip of the MinD polymer and grows on top of it towards
the pole. The diﬀerential equation describing the pro-
jected length of the MinE polymer has the same simple
structure as the one for the MinD polymer:
d
dtlE
l = γkE(SE
l ),
d
dtlE
r = γkE(SE
r ).
(5)
The same conversion factor γ is used since we assume
that MinE monomers bind to MinD monomers of the
helix one-to-one. The MinE-polymer always starts grow-
ing from the non-polar tip of the MinD-polymer (Fig. 1).
The non-polar end of the MinDE-polymer falls oﬀthe
membrane (with a slower speed than E-elongation) and
disassembles. The state variable SE
l/r deﬁnes the value of
the growth rate as follows:
kE(SE
l/r) =









kE
oncE −koﬀ
if SE
l/r = 1 (E-polymer growing)
−koﬀ
if SE
l/r = 0 (E-polymer reached
cell wall (lE
l/r = lD
l/r))
0
if SE
l/r = −1 (no E-polymer)
(6)
As for MinD, we assume the total number of MinE
monomers to be constant:
λ
γV
 lE
l + lE
r

+ cE = cE,to.
(7)
B.
Switching
We consider a stochastic description of switching be-
tween the three possible discrete states of the state
variables SD/E
l/r
where the probability of switching de-
pends on the cytosolic concentrations of MinD/E. To
capture the cooperative nature of the initiation of a
polymer (e.g. [29, 30]), we assume that the instanta-
neous rates of nucleation and capping are proportional
to a power of the respective cytosolic concentrations:
λnuc
l/r (t) = knuccnnuc
D
(t) and λcap
l/r (t) = kcapcncap
E
(t). nnuc
and ncap are the cooperativities for the nucleation and
the capping events, respectively.
A D-polymer starts
growing out of an empty nucleation site with probability
pnuc(t) = λnuc(t) dt during the time interval t..(t + dt)
and a growing D-polymer gets capped (i.e. an E-polymer
nucleates at its tip) with probability pcap(t) = λcap(t) dt
during the time interval t..(t + dt).
Our main results
involve calculating analytical expressions for the proba-
bility distributions when these switches happen.
As a simpliﬁed model, we ﬁrst consider the limit in
which the cooperativities go to inﬁnity.
More speciﬁ-
cally, we deﬁne the nucleation probability as λnuc
l/r (t) =
k′
nuc(cD(t)/cD,th)nnuc.
In the limit nnuc
→∞, the
stochastic switching becomes deterministic with the nu-
cleation event occurring as soon as cD reaches the nucle-
ation threshold cD,th. Capping is treated similarly.
Note that this deterministic limit of our model is
fundamentally diﬀerent from the deterministic model of
Drew et al. [9] in that Drew et al. consider the mean
ﬁeld behavior of a population of ﬁlaments that switch
between growing and shrinking states at average rates
whereas we have individual ﬁlaments that switch at spe-
ciﬁc concentration-determined times. The diﬀerence be-
tween these two models is that the mean ﬁeld model
fails to admit oscillations without further biochemical
assumptions (length-dependent growth speed), whereas


## Page 4


4
the individual-ﬁlament model has an oscillatory solution
over a large range of parameter values.
C.
Model summary
Eqs.
(1)–(7)
together
with
the
above-mentioned
switching dynamics of the discrete state variables SD/E
l/r
represent a hybrid dynamical system [28]. In the rest of
this article, we analyse this system and present both ana-
lytical as well as numerical results that can be interpreted
with regard to experimentally obtainable data.
A single MinD-polymer ‘life span’ includes nucleation,
growth, capping (nucleation of the MinE-polymer), and
disassembly as described for the deterministic case in
Tab. I.
The two poles can undergo alternating events of this
type, which then constitutes an oscillatory solution. Such
an oscillatory solution progresses in the following man-
ner (cf. Fig. 1 and Fig. 2 for notation). A MinD polymer
capped (at time tc
1) by a MinE polymer disassembles at
one pole while the nucleation site at the other pole is
either occupied by a disassembling MinDE polymer or
remains empty. As the MinE polymer disassembles at
the tip, it maintains a steady length by growing at its
other end (treadmilling). Throughout this process, cy-
tosolic MinD concentration increases thereby increasing
the probability of MinD-polymer nucleation at the empty
pole but cytosolic MinE concentration remains low. Once
nucleation occurs (at time tn
2), the nascent polymer grows
towards midcell, depleting the cytosolic MinD pool. Be-
cause of the ordering of critical concentrations for nucle-
ation and elongation, the existing MinE polymer elon-
gates in preference to nucleation of a new MinE polymer
capping the nascent MinD polymer. When the original
MinD polymer reaches the same length as the steady-
state-treadmilling MinE length, treadmilling is no longer
possible and the cytosolic MinE concentration begins to
rise. This raises the probability of capping the nascent
MinD polymer (at time tc
2). After capping, the system
is back to the state we began describing but with the
poles reversed. The ﬁrst MinDE polymer completely dis-
appears at time td
1.
For a speciﬁc subclass of the described oscillatory so-
lution we are able to derive an analytical description for
relevant probability distributions. This subclass we call
regular oscillations and it is deﬁned by tc
1 < tn
2 < tc
2 < td
1.
A section of it is shown in Fig. 2. This deﬁnition essen-
tially means that the growing phase (SD
l/r = 1) of one
polymer falls completely within the shrinking phase of
the other (SD
r/l = 0).
Table II gives an overview and numerical values for
the parameters we used in this model. Most of them are
taken in ranges reported in the experimental literature.
Some are adjusted to values that lead to reasonable re-
sults of the model.
IV.
RESULTS
A hybrid dynamical system must be solved piecewise
and care must be taken at points of discontinuity which,
in this case, occur each time a polymer switches state.
Within the appropriate parameter ranges and for a reg-
ular oscillation (as deﬁned above), we need only consider
the progression through three of the six possible com-
binations of discrete states of (SD
l , SD
r ) which occur in
the sequence (0, −1) →(0, 1) →(0, 0) during one half-
period. The evolution of the continuous variable, for any
given discrete state, requires a solution for disassembly
and assembly of polymers. The solution of Eq. 1 for a
shrinking D-polymer (SD
l/r = 0) is
lD
l/r(t) = lD
l/r(tc
l/r) −γkoﬀ(t −tc
l/r),
(8)
where tc
l/r is the time of the most recent capping of the
left or right D-polymer, respectively.
The solution of Eq. 1 for a growing D-polymer is de-
pendent on the dynamic cytosolic concentration. During
regular oscillations, a growing D-polymer only appears
while the other D-polymer is disassembling (i.e., discrete
state (SD
l/r, SD
r/l) = (0, 1)). Assuming the polymer on the
right is decaying, the cytosolic MinD concentration fol-
lows cD(t) = cD,to −
λ
γV (lD
l (t) + lD
r (tc
r) −γkoﬀ(t −tc
r)).
Substituting this into Eq. 1 and solving the resulting
equation with the initial condition lD
l (tn
l ) = 0 (tn
l is the
time at which the left polymer nucleates), one obtains
lD
l (t) =γV
λ

cD,to −koﬀ
kD
on

−lD
r (tc
r) + γkoﬀ(t −tc
r)
−
γV
λ

cD,to −koﬀ
kD
on

−lD
r (tc
r) + γkoﬀ(tn
l −tc
r)

· exp

−λkD
on
V
(t −tn
l )

.
(9)
Similar solutions can be found for the dynamics of the
E-polymers.
However, for the analytical treatment in
this article, we restrict ourselves to the limit of fast E-
ring formation: We assume that an E-polymer attains its
steady state length right after its nucleation (i.e. after
capping of the D-polymer). Equating the rate of polymer
decay at the medial end of the MinDE polymer with the
growth rate of the MinE polymer gives the steady state
E-polymer length lE,ss =
γV
λ

cE,to −koff
kE
on

.
With this
simpliﬁcation, the model reduces to a hybrid dynamical
system with two continuous (lD
l/r) and two discrete (SD
l/r)
variables. It is important to note that we make use of
this approximation only for obtaining analytical results.
In the numerical simulations we always model the full
system with explicit E-polymer dynamics.
For the rest of this article, we will drop the ‘D’ super-
script and denote the length of the D-polymer by l.


## Page 5


5
deterministic switching condition
SD
SE
(1) MinD polymer nucleates (nucleation event) cD(t) > cD,th
−1 →1
(2) MinE polymer nucleates (capping event)
cE(t) > cE,th
1 →0
−1 →1
(3) MinE polymer reaches cell wall
lE = lD
1 →0
(4) MinDE polymer reaches cell wall
lD = 0
0 →−1 0 →−1
TABLE I: The series of states a MinD polymer on one pole goes through during one ‘life span’.
lD
l = lE
l
lD
r
x = 0
x = L
x
SD
l/r: 0 / 1
SE
l/r: 0 / -1
ll1
lr1
0 / 0
0 / 1
lr1
-1 / 0
-1 / 1
ll1
lr1
1 / 0
-1 / 1
ll1
lr1
1 / 0
-1 / 0
FIG. 1: Scheme of the oscillations produced by the model. Shown are the two polymer helices (red – MinD, blue – MinE) on
the left and the right side of the cell at diﬀerent time points (time is increasing to the right). The values of the discrete state
variables SD
l , SE
l , SD
r and SE
r are given under the ﬁgures.
par.
value
unit
description
d
2.5
nm
increase in polymer length
by
addition
of
a
single
monomer (see footnote on
page 16) [14]
θ
1.4
rad
pitch of the helical poly-
mer [15]
cD,to
4
µM
total MinD monomer conc.
cE,to
1.5
µM
total MinE monomer conc.
koﬀ
80
s−1
depolymerisation rate of the
MinDE polymer
kD
on
150
(µM · s)−1
polymerisation rate of MinD
on the membrane
kE
on
320
(µM · s)−1
polymerisation rate of MinE
on the MinD polymer
cD,th
2.5
µM
threshold conc. for the nu-
cleation of a MinD polymer
cE,th
1.25
µM
threshold conc. for the nu-
cleation of a MinE polymer
L
3
µm
length of cell
r
0.5
µm
radius of cell
knuc
0.015 s−1µM−nnuc rate constant of nucleation
kcap
0.15 s−1µM−ncap rate constant of capping
nnuc/
ncap
3–6
cooperativity
of
nucle-
ation/capping
TABLE II: List of parameters used throughout this article.
The concentrations cD,to and cE,to are consistent with values
used in other modelling papers and are supported by exper-
iment [31]. The rates governing polymer growth and decay
are estimated from [32]. L and r are typical values seen in ex-
periments and the other parameters are chosen such that the
model produces reasonable results. A detailed discussion of
the numerical values of some of the parameters can be found
in [11].
T c
1
T f
2
T n
0
td
0
tn
1
tc
1
tn
2
ln
0
lc
1
lc
2
ld
1
ln
1
td
1
tn
3
tc
2
t
cell long axis x [µm]
L = 3
1.5
0
l
r
SD = 0
SD = −1
SD = 1
FIG. 2:
A section of the regular oscillation pattern with
stochastic switching to explain our notation. Shown is the
temporal dynamics of the tip-positions (x) of the D-polymers
as well as the value of the discrete state variables SD
l/r (shaded
areas). We use capital T for time diﬀerences and little t for
time points. Even indices refer to the polymer anchored at
the right pole of the cell and odd indices refer to the one
anchored at the left pole.
A.
Solution of the deterministic model
As a basis for further discussions we brieﬂy present
the solution to the simplest version of the model de-
scribed in the preceding section and previously addressed
by Cytrynbaum and Marshall [11]. We consider the case
of deterministic switching (see Subsec. III B) and fast E-
ring formation. The length of the MinD polymer at cap-
ping (the amplitude of the oscillation) on one side can
be expressed as a function of the capping length at the
preceding capping on the other side: lc
i+1 = f(lc
i) (cf.


## Page 6


6
 0
 0.1
 0.2
 0.3
 0.4
 0.5
 0.6
 0.7
 0.8
 0
 0.1
 0.2
 0.3
 0.4
 0.5
 0.6
 0.7
 0.8
 0
 0.1
 0.2
 0.3
 0.4
 0.5
 0.6
 0.7
 0.8
 0
 0.1
 0.2
 0.3
 0.4
 0.5
 0.6
 0.7
 0.8
 0
 0.1
 0.2
 0.3
 0.4
 0.5
 0.6
 0.7
 0.8
 0
 0.1
 0.2
 0.3
 0.4
 0.5
 0.6
 0.7
 0.8
 0
 0.1
 0.2
 0.3
 0.4
 0.5
 0.6
 0.7
 0.8
 0
 0.1
 0.2
 0.3
 0.4
 0.5
 0.6
 0.7
 0.8
 0
 0.1
 0.2
 0.3
 0.4
 0.5
 0.6
 0.7
 0.8
 0
 0.1
 0.2
 0.3
 0.4
 0.5
 0.6
 0.7
 0.8
lc
i/L
lc
i/L
lc
i/L
lc
i/L
lc
i/L
lc
i+1/L
lc
i+1/L
lc
i+1/L
lc
i+1/L
lc
i+1/L
cD,to = 3 µM
cD,to = 3 µM
cD,to = 3 µM
cD,to = 3 µM
cD,to = 3 µM
3.5
3.5
3.5
3.5
3.5
4
4.5
4.5
4.5
4.5
4.5
(a) varying cD,to
 0
 0.1
 0.2
 0.3
 0.4
 0.5
 0.6
 0.7
 0.8
 0
 0.1
 0.2
 0.3
 0.4
 0.5
 0.6
 0.7
 0.8
 0
 0.1
 0.2
 0.3
 0.4
 0.5
 0.6
 0.7
 0.8
 0
 0.1
 0.2
 0.3
 0.4
 0.5
 0.6
 0.7
 0.8
 0
 0.1
 0.2
 0.3
 0.4
 0.5
 0.6
 0.7
 0.8
 0
 0.1
 0.2
 0.3
 0.4
 0.5
 0.6
 0.7
 0.8
 0
 0.1
 0.2
 0.3
 0.4
 0.5
 0.6
 0.7
 0.8
 0
 0.1
 0.2
 0.3
 0.4
 0.5
 0.6
 0.7
 0.8
 0
 0.1
 0.2
 0.3
 0.4
 0.5
 0.6
 0.7
 0.8
 0
 0.1
 0.2
 0.3
 0.4
 0.5
 0.6
 0.7
 0.8
lc
i/L
lc
i/L
lc
i/L
lc
i/L
lc
i/L
lc
i+1/L
lc
i+1/L
lc
i+1/L
lc
i+1/L
lc
i+1/L
cE,to = 1.3 µM
cE,to = 1.3 µM
cE,to = 1.3 µM
cE,to = 1.3 µM
cE,to = 1.3 µM
1.5
1.5
1.5
1.5
1.5
1.7
1.7
1.7
1.7
1.7
1.9
1.9
1.9
1.9
1.9
(b) varying cE,to
FIG. 3: The dynamics of the deterministic version of the sim-
plest model (inﬁnitely fast E-ring formation) depicted in form
of a discrete map. It displays the length of the MinD poly-
mer relative to the cell length L as a function of this lengths
at the previous capping, i.e. the amplitude of the oscillation
(see App. A for the equations). For intuitive analysis of the
map, the identity line is added. Except for cD,to and cE,to,
standard parameters from Tab. II were used.
Fig. 2). Thus, the problem of ﬁnding a periodic solution
to the hybrid system is reduced to ﬁnding a ﬁxed point
of a one-dimensional map. Only in this simple version
of the model such a one-dimensional map can be found,
because only then the state of the system is completely
determined by the length of only one of the polymers.
The calculation and the equations for the map are
given in App. A. In Fig. 3 the map is plotted for varying
total concentrations of MinD and MinE.
The intersection of the map with lc
i+1 = lc
i shows three
ﬁxed points which in terms of the hybrid system corre-
spond to:
1. A stable cytosolic solution: There are no polymers
(lc = 0) and all the Min proteins are in the cytosol
as monomers.
2. An unstable oscillation (the map intersects the
identity line with a slope larger than one).
3. Stable (slope is equal to zero) oscillations with con-
stant amplitude (given in Eq. A.3).
Depending on the initial conditions (li(t = 0)), the sys-
tem converges to one of the two stable states, i.e. each
parameter set that allows for an oscillatory solution also
includes a solution where no polymer exists (the cytosolic
solution).
As can be seen from Fig. 3, the region of initial condi-
tions that lead to a stable oscillatory solution is biggest
when cD,to is large and cE,to is close to cE,th. If cD,to is too
small or cE,to is too high, the map does not intersect with
the identity line anymore and only the cytosolic solution
remains. This corresponds qualitatively to the condition
for the existence of oscillations as derived in [11] for a
simpliﬁed version of the model.
In the stochastic version of the model, low probability
switching events can, under certain circumstances, lead
to a transition between episodes of oscillations (with rel-
atively constant amplitude) and almost purely cytosolic
states. We will investigate this in the following sections
and will refer to Fig. 3 as the limiting case of inﬁnite
cooperativity.
B.
Probability distributions for experimentally
measurable quantities
More realistic than the deterministic-threshold limit
for nucleation and capping of the MinD polymer is
stochastic switching that models the random nature of
the underlying chemical reactions. From now on, we will
use the stochastic rules for switching between the dif-
ferent states of polymers as introduced in Subsec. III B.
In this section, we will characterise the changes such a
stochastic switching rule introduces to the system. We
will focus on two measures to characterise the robust-
ness of the oscillatory solution of the stochastic model:
the distribution of oscillation amplitudes and periods and
the possibility of skipping beats. Both of these measures
should be easy to obtain from experiments.
As long as the system undergoes regular oscillations,
conditional probability distributions can be derived for
the times at which nucleation and capping occur. Sup-
pose the polymer on the right disappears at time td
(Fig. 2) and, at that moment, the polymer on the left
is shrinking and has length ld. Given this, we denote the
probability that a new polymer nucleates on the right at
time t by Pnuc(t|ld). Thus, Pnuc(t|ld) dt is the probabil-
ity that nucleation on the right side happens in the time
interval t..(t + dt) where t > td. Similarly, if tn is the
time of nucleation on the right and the polymer on the
left is still shrinking and has length ln, then Pcap(t|ln) dt
describes the probability for the capping of the growing
polymer to happen in the time interval t..(t + dt) after
nucleation (t > tn). Analytical expressions for these two


## Page 7


7
probability distributions are computed in Apps. B and C
and plotted in Fig. 11.
Using the two conditional probability distributions for
nucleation and capping, analytical expressions for the
steady state probability distribution of polymer lengths
at capping and other relevant quantities can be derived.
Similar to the description of the deterministic system in
terms of a map (Subsec. IV A), we derive an integral re-
lationship that maps the probability distribution for the
polymer length ln (Fig. 2) onto a new probability distri-
bution of the same length half a period later. The deriva-
tion of this map P(ln
i ) = F(P(ln
i−1)) and the expression
for the map itself (Eq. D.6) is presented in App. D. The
expression for the operator F that relates two consec-
utive probability distributions involves complicated in-
tegrals and no general closed expression can be found.
However, through numerical integration, an approxima-
tion to the steady state probability distribution can be
computed iteratively. Typically, three or four iterates of
the map F (Eq. D.6) are adequate for convergence with
reasonable accuracy.
Only in the case of regular oscillations can the two
stochastic processes, nucleation and capping, be sepa-
rated and the probabilistic map (Eq. D.6) be derived.
Crucial for obtaining regular oscillations are high coop-
erativities in both capping and nucleation.
In the following, we present probability distributions
for the amplitude and period of the oscillations obtained
from numerical simulations[35].
We compare these re-
sults to analytical results that we obtain by iterating the
probabilistic map.
1.
Distribution of oscillation amplitude and dependence on
cooperativities
Fig. 4 shows the results of long simulation runs of the
full MinDE polymer model with stochastic switching.
Plotted is the distribution of MinD-polymer lengths at
capping (the amplitude of the oscillation) and the time
between consecutive capping events on the same side (the
period).
In experimental studies (both qualitative and quanti-
tative [31]), large deviations in the oscillation amplitude
and period are seldomly reported. For our model to re-
produce this narrow distribution, high cooperativities in
both nucleation and capping are crucial. Fig. 4 shows
that our model is especially sensitive to the cooperativ-
ity in capping: nnuc = 3 still leads to a fairly narrow
distribution, whereas both curves for ncap = 3 have big
contributions at unusually short capping lengths.
Fig. 5 shows the same simulation results as of Fig. 4(a)
together with the analytical result from the numerical
iteration of the probabilistic map (Eqs. D.6 and D.7).
The plots conﬁrm the applicability of our analytical
solution as discussed above. For regular oscillations, the
analytical result agrees well with the results from sim-
ulations. When cooperativities decrease, the increased
 0
 0.5
 1
 1.5
 2
 2.5
 3
 3.5
 0
 0.5
 1
 1.5
 2
 2.5
lc [µm]
p
nnuc/ncap
3/6
3/3
6/3
6/6
(a) distribution of oscillation amplitudes
 0
 0.005
 0.01
 0.015
 0.02
 0.025
 0.03
 0.035
 0.04
 0.045
 0.05
 0
 20
 40
 60
 80
 100
 120
 140
T [s]
p
nnuc/ncap
3/6
3/3
6/3
6/6
(b) distribution of periods
FIG. 4: Numerically obtained distributions for oscillation am-
plitude (polymer lengths at capping) and periods (time be-
tween consecutive cappings on the same side) with varying
cooperativity of nucleation (MinD) and capping. Standard
parameters as of Tab. II were used.
probability at small polymer lengths is not accounted for
by the analytical result. These are the events that are
too far away from the stable oscillation point in Fig. 3
and violate the regular oscillation assumption needed for
the calculations in App. D.
Since both the numerical
and the analytical distributions are normalised, the lat-
ter one shows higher values in the region corresponding
to regular oscillations. The broader capping probability
distribution in the case of lower ncap (cf. also Fig. 11(b))
can lead to capping at short polymer lengths, which even-
tually can lead to a transition to a purely cytosolic state
(see Subsec. IV C).


## Page 8


8
 0
 1
 2
 3
 4
 0
 0.5
 1
 1.5
 2
 2.5
lc [µm]
p
(a) nnuc = 6, ncap = 6
 0
 1
 2
 3
 0
 0.5
 1
 1.5
 2
 2.5
lc [µm]
p
(b) nnuc = 3, ncap = 6
 0
 1
 2
 0
 0.5
 1
 1.5
 2
 2.5
lc [µm]
p
(c) nnuc = 6, ncap = 3
 0
 0.5
 1
 1.5
 2
 0
 0.5
 1
 1.5
 2
 2.5
lc [µm]
p
(d) nnuc = 3, ncap = 3
FIG. 5: Comparison of the analytical result (line) with simu-
lations (points – same data as in Fig. 4(a)). For the analyti-
cal result, the probabilistic map (Eq. D.6) was applied three
consecutive times, starting with a uniform distribution. This
steady state distribution in ln was then transformed into a
distribution in lc by applying Eq. D.7.
2.
Distribution of oscillation periods and dependence on
total concentrations
Another quantity that can be easily obtained from ex-
periment is the period of the oscillations.
In Fig. 6,
we plot the probability distributions of the period T for
diﬀerent total concentrations of MinD and MinE as ob-
tained from simulations.
At higher concentrations of MinD (cD,to ≳3.75 µM)
and intermediate concentrations of MinE (cE,to
≈
1.5 µM), the distributions are sharply peaked around a
single value of T (see Fig. 6(a)). This parameter regime
leads to regular oscillations. The amplitude of the oscil-
lations decreases monotonically with cD,to, reﬂected in
the leftward shift of the peak in Fig. 6(a), consistent
with the analogous feature in the deterministic version
of the model (Fig. 3). The closer the amplitude comes
to the unstable ﬁxed point in Fig. 3, the more likely a
D-polymer will be capped at a small length. This early
capping at one pole leads to an earlier rise in MinE so
that the subsequent capping event of the other pole oc-
curs earlier as well. This positive feedback can drive the
cell into the predominantly cytosolic state which appears
in the stochastic version of the model as a second peak
close to T = 0 (Fig. 6(a), cD,to = 3.25 µM).
A similar distribution is obtained if the total MinE
concentration is chosen too high (shown in Fig. 6(b),
cE,to = 1.6 µM) with capping of the D-polymers occur-
ring quite early.
For low concentrations of MinE, the
instantaneous capping rate is reduced and capping of the
D-polymer can occur late (cf. also Fig. 11(b)). In ex-
 0
 0.005
 0.01
 0.015
 0.02
 0.025
 0.03
 0.035
 0.04
 0.045
 0.05
 0
 50
 100
 150
 200
3.25
3.75
4.5
5.25
cD,to [µM]
T [s]
p
(a) varying cD,to
 0
 0.005
 0.01
 0.015
 0.02
 0.025
 0.03
 0.035
 0.04
 0.045
 0
 50
 100
 150
 200
 250
 300
 350
0.8
1.2
1.4
1.6
cE,to [µM]
T [s]
p
(b) varying cE,to
FIG. 6: Distributions of oscillation periods T for diﬀerent to-
tal concentrations cD,to (upper panel) and cE,to (lower panel).
The data was obtained from simulations where the time be-
tween two consecutive cappings on the same side is considered
to be T (ignoring the dynamics on the other side). Both coop-
erativities (for nucleation and capping) are 6, cE,to = 1.5 µM
(upper panel), and cD,to = 4 µM (lower panel).
treme cases (cE,to = 0.8 µM) the D-polymer can reach
maximum length lmax (Eq. 4). Accordingly, the distribu-
tion of periods is shifted towards higher T and tails out
slowly.
Using the steady state probability distribution for ln,
an analytical integral expression for the probability dis-
tribution of the period T can be derived for the case of
regular oscillations (see App. E). Fig. 7 shows a compar-
ison of this analytical result with simulation data. Since
the analytical description only contains the regular os-
cillations, it fails to produce the peaks at short periods
in Fig. 7(a) and 7(d). Also, low total concentrations of
MinE (e.g., cE,to ≲1.2 µM) lead to an irregular oscil-
lation regime by violating the scheme shown in Fig. 2
in that capping of a new polymer is likely to occur after
complete disassembly of the existing polymer at the other


## Page 9


9
 0
 0.02
 0.04
 0
 20  40  60  80  100
T [s]
p
(a) 3.25 µM/1.5 µM
 0
 0.02
 0.04
 0
 25  50  75  100  125
T [s]
p
(b) 4 µM/1.5 µM
 0
 0.02
 0.04
 0
 100
 200
 300
T [s]
p
(c) 4 µM/0.8 µM
 0
 0.02
 0.04
 0
 25  50  75  100  125
T [s]
p
(d) 4 µM/1.6 µM
FIG. 7: Comparison of the analytical result (line) with sim-
ulations (points). For the analytical result, the probabilistic
map (Eq. D.6) was applied three consecutive times, starting
with a uniform distribution. This steady state distribution in
ln was then transformed into a distribution in the period T
by applying Eqs. E.1 and E.2. The simulation data in (a),
(c), and (d) is from Fig. 6, the data in (b) from Fig. 4. The
numbers in the subcaptions are cD,to/cE,to.
pole (through tc
i > td
i−1). Accordingly, the analytical so-
lution fails to give a good approximation (Fig. 7(c)). In
Fig. 7(b), the standard parameter set (Tab. II) is used
and analytical and numerical results agree.
Fig. 7(b)
and 5(a) represent the parameter values that provide the
closest match to the experimental observations of sus-
tained and regular oscillations.
To illustrate the range of validity of our analytical cal-
culation, we compare the means of the numerically and
analytically obtained probability distributions in Fig. 8.
The deviations in mean period in Fig. 8 reiterate that
the analytic expression is valid provided MinD concen-
tration is high and MinE concentration is intermediate,
ensuring regular oscillations. For small cD,to, the analyt-
ical result is always an overestimate of the numerical re-
sult, since the analytical treatment does not capture the
second peak in the distribution at short T (Fig. 7(a)).
The same overestimate results for high cE,to (Fig. 7(d)),
whereas for low cE,to, the analytical calculation provides
an underestimate of the period.
Here, the long tail
of the numerically obtained distributions is not covered
(Fig. 7(c)).
Our results as shown in Fig. 8 agree qualitatively with
experiments. Overexpression of MinD has been shown
to increase the oscillation period [21] and overexpres-
sion of MinE is known to disrupt the normal division
placement [33], probably due to destroying the oscilla-
tory pattern (which corresponds to our numerical solu-
tion of ¯T ≈0 s for high MinE concentration).
In the
deterministic version of the model, this corresponds to
 0
 20
 40
 60
 80
 100
 120
 140
 3
 3.5
 4
 4.5
 5
cD,to [µM]
¯T [s]
 0
 20
 40
 60
 80
 100
 120
 140
 160
 180
 200
 0.8
 1
 1.2
 1.4
 1.6
 1.8
cE,to [µM]
¯T [s]
FIG. 8: Mean oscillation period ¯T for varying total concen-
trations of the two Min proteins.
Both the analytical re-
sult (line) as well as results from simulations (points) are
shown. Cooperativities for nucleation and capping are both
6, cE,to = 1.5 µM in the upper panel and cD,to = 4 µM in the
lower.
the deterministic map not intersecting with the identity
line anymore (Fig. 3(b)).
3.
Beat-skipping
Stochastic switching (nucleation and capping) can also
lead to occasional skipping of beats, another property
that is easily quantiﬁed experimentally. Regular oscilla-
tions are characterized by the asynchronous and alter-
nating growth and disassembly of a polymer at each of
the two poles of the cell. A skipped beat is deﬁned as
a deviation from regular oscillations in which alternation
fails and a polymer reappears on the same pole before
the appearance of a polymer on the opposite pole. As a
criterion for our numerical analysis, we count the number
of cases where two consecutive cappings of MinD poly-
mers occur on the same side of the cell. The fraction of
these cases with respect to all cappings is shown in Fig. 9.
The ﬁgure shows numerically-obtained data for diﬀerent
cooperativities of nucleation and capping.
As a skipped beat is one way of deviating from regular
oscillations, the results in Fig. 9 recapitulate the observa-
tions described earlier in the context of Figs. 4, 6, and 8.
The high fraction of irregular capping events for low to-


## Page 10


10
 0.001
 0.01
 0.1
 1
 3
 3.5
 4
 4.5
 5
cD,to [µM]
fraction of skipped beats
nnuc/ncap
3/6
3/3
6/3
6/6
 0.0001
 0.001
 0.01
 0.1
 1
 0.6
 0.8
 1
 1.2
 1.4
 1.6
 1.8
cE,to [µM]
fraction of skipped beats
nnuc/ncap
3/6
3/3
6/3
6/6
FIG. 9: Numerical result for the regularity of the oscillations.
Plotted is the fraction of skipped beats (see text) depending
on both total concentrations of the Min proteins and coop-
erativities used for nucleation and capping, respectively. In
the upper panel, cE,to = 1.5 µM, in the lower cD,to = 4 µM.
Simulations were run such that the total number of cappings
are in the range of 105 for the low values and 103 −105 for
the high values. The errorbars are smaller than the pointsize
and the lines are guides to the eye.
tal MinD concentrations as well as for high total MinE
concentration correspond to the second peak in the prob-
ability distributions of periods in Fig. 6 at short T . If the
capping cooperativity is relatively low, there will always
be a signiﬁcant fraction of skipped beats, which corre-
sponds to the non-zero tails of the distributions at short
lengths for ncap = 3 in Fig. 4. For our standard param-
eter set nnuc = 6, ncap = 6, cD,to = 4 µM, cE,to = 1.5 µM
and for a range of concentrations around it, the fraction
of skipped beats is well below the 1% ﬁgure. The strong
deviation from our analytical result when cE,to is very
small (Fig. 7(c)) is a violation of the regular oscillation
pattern that does not lead to skipped beats, i.e. even in
this extreme case the alternating appearance of a poly-
mer on the left and the right side is still conserved.
C.
Bistability and stochastic transitions
As derived in Subsec. IV A, the deterministic system
is bistable for a large range of parameters. Under cer-
tain conditions, stochastic nucleation and capping of
polymers can lead to transitions between the two sta-
ble states: oscillatory episodes lasting for tens of peri-
ods and the cytosolic state. Fig. 10 shows examples of
this behaviour for three diﬀerent parameter sets. A clear
distinction between regular oscillations and the cytosolic
state is only possible for high cooperativity.
This be-
haviour can be explained qualitatively using the deter-
ministic map described in Subsec. IV A.
During regular oscillations, a D-polymer is most likely
capped at a length close to the peak of the respective con-
ditional probability distribution (Fig. 11(b) in App. C).
Due to the stochasticity of the capping process, there is a
small probability of the D-polymer being capped before
it reaches normal extension[36].
For high cooperativi-
ties, the deterministic map in Fig. 3 retains some validity
and one can think of the capping events in the stochas-
tic model as being a blurred version of the deterministic
map. Rare early and late capping events correspond to
events at the edge of the blurred region about each ﬁxed
point and can result in a transition from relatively stable
oscillations to a state that is mostly cytosolic and back
again. Since the events allowing for such transitions lie
outside the regular oscillation pattern (Subsec. III C), the
analytical approach in App. D does not provide the right
tools to describe this eﬀect. We restrict ourselves to a
qualitative discussion of a limiting case.
In order to get a better understanding of the stochastic
transitions we consider the special case of deterministic
nucleation of D-polymers and stochastic capping[37]. For
high values of ncap, the map in Fig. 3 can be used as a
rough guide for the stochastic transitions. In App. F, we
adjust this map to the speciﬁc case considered here.
In Fig. 10(d) we show three maps obtained as in
App. F: One representing our standard parameter set
cE,to = 1.5 µM, kcap = 0.15 s−1µM−6 (cf. Fig. 7(b)) and
the two parameter sets used in Fig. 10(a) and 10(b) (with
cD,th = 2.5 µM). One can think of the stochastic system
as producing a cloud of points in this map around the
stable steady states. A transition occurs if an extreme
capping event takes the system from a neighbourhood of
the pre-transition ﬁxed point over the unstable steady
state into a neighbourhood of the other ﬁxed point. For
our standard parameter set, due to the large distance
between stable and unstable ﬁxed points, this is unlikely
to happen. The system will stay in the vicinity of one
of the ﬁxed points with probability close to one. When
the total E-concentration is increased (Fig. 10(a)), the
map is shifted to the right and the distance an extreme
capping event has to cover in order for a transition to
occur, decreases. The same is valid for an increase in
the capping parameter kcap as observed for Fig. 10(b).
The map for this case is slightly shifted to the left com-
pared to the former case which leads to a reduced transi-


## Page 11


11
 0
 1
 2
 3
 0
 5000
 10000
t [s]
x [µm]
(a) ncap = 6, cE,to = 1.7,
kcap = 0.15
 0
 1
 2
 3
 0
 5000
 10000
t [s]
x [µm]
(b) ncap = 6, cE,to = 1.5,
kcap = 0.5
 0
 1
 2
 3
 0
 5000
 10000
t [s]
x [µm]
(c) ncap = 3, cE,to = 1.5,
kcap = 0.4
 0
 0.5
 1
 1.5
 0
 0.5
 1
 1.5
 0
 0.5
 1
 1.5
 0
 0.5
 1
 1.5
 0
 0.5
 1
 1.5
 0
 0.5
 1
 1.5
 0
 0.5
 1
 1.5
 0
 0.5
 1
 1.5
Fig. 7(b)
Fig. 7(b)
Fig. 7(b)
Fig. 7(b)
10(a)
10(a)
10(a)
10(a)
10(b)
10(b)
10(b)
10(b)
lc
i [µm]
lc
i [µm]
lc
i [µm]
lc
i [µm]
lc
i+1 [µm]
lc
i+1 [µm]
lc
i+1 [µm]
lc
i+1 [µm]
(d)
FIG. 10: Episodes of oscillatory dynamics alternating with the cytosolic state. Plotted is the position (along the cell long axis
x) of the two D-polymer tips over time. Note that, typically, the duration of one period in the oscillatory state is around
T ∼100 s. The map shown in (d) is used for a qualitative explanation in the text. Note, that contrary to our discussion in the
text, the time series presented in (a)–(c) were obtained from the full stochastic model (nucleation and capping stochastic).
tion rate. The main parameter controlling the extension
of the cloud of points is the capping cooperativity ncap.
When it decreases, the cloud becomes larger, rendering
the map interpretation less meaningful (cf. Fig. 4). More
transitions occur and the states are not as well deﬁned
anymore (Fig. 10(c)).
V.
DISCUSSION
The mechanisms underlying the Min oscillations in
E.coli are still subject to much debate among modellers
since none of the models proposed so far capture all the
properties and all the phenotypes displayed in wildtype
and mutant cells (see [11] for a discussion). The most ob-
vious qualitative features of the observed dynamics are
explained in many models which means that being able
to distinguish between these models will rely on careful
quantitative characterization of both the models and the
experimental data. The results presented here are a step
in this direction.
We generalized a recently published model to allow
for more realistic comparison with data by introducing
and analyzing stochasticity. From a mathematical view-
point, this model provides an example of a stochastic
hybrid dynamic system, whose solution can be found an-
alytically in the case of regular oscillations. Probability
distributions for easily measured quantities are provided,
making the model testable. Comparing our results to ex-
perimental data already available in the literature, the
main ﬁndings of this paper are as follows.
High cooperativity in the nucleation of the Min-
polymers (at least a power of 3 for the MinD and 6 for
MinE) are important.
Lower cooperativities allow too
many events that are inconsistent with observations. Re-
ported Hill coeﬃcients for the nucleation of MinD on a
lipid membrane are around 2 [29].
The model is relatively stable to changes in MinD con-
centration.
MinD concentrations greater than 3.5 µM
ensure regular oscillations. MinE concentration, on the
other hand, is more ﬁnely constrained and must fall be-
tween 1.2 and 1.6 µM.
Our results oﬀer an explanation for the variability in
the presence of oscillations observed in experiments. A
signiﬁcant fraction of cells usually do not show oscilla-
tions in experiments or go from an oscillatory state into a
cytosolic state during the course of observation (e.g. [23]).
Our model suggests an explanation for this in the form
of bistability of an oscillating state and a purely cytosolic
state. The model of Fange and Elf [7] also reports bista-
bility, whereas the models of Howard et al. [5] and Meacci
et al. [3] demonstrate qualitatively distinct solutions (cy-
tosolic or oscillating) as a function of parameters but not
bistability.
Transitions between the two states will be
a challenge to observe experimentally.
Evidence for a
transition in each direction would be necessary, requir-
ing long observation times. Photobleaching in the ﬂuo-
rescence microscopy studies limits the latter and other
factors might inﬂuence the existence and quality of the
observed oscillations (see, e.g. [23]).
In a recent experimental study, Downing et al. [17] ac-
tively controlled the MinD dynamics in E.coli by chang-
ing cationic concentrations in the surrounding medium.
They were able to stop, distort and restart the oscilla-
tions. Based on the bistability and stochastic transitions
described here, we speculate that the ion concentration
has an inﬂuence on the assembly dynamics of the MinE-
polymer. For example, if increased ion concentration in-
creases kcap, the system might be driven into a regime
where a stochastic transition into the cytosolic state be-
comes more likely. On the other hand, decreasing kcap
can lead to a freeze or or halt of the oscillations with
most of the MinD localised on one side of the cell.
Most other models [3, 10, 12] produce a similar depen-
dence of the oscillation period on the total Min concen-
trations and a few [6, 7] report on the variability of the


## Page 12


12
period or, as in our case, the full probability distribu-
tion [12].
The biggest diﬀerence between the reaction-diﬀusion-
type models and the polymer model described here is that
in the polymer model the spatial pattern of the Min os-
cillations is prescribed in the form of possible nucleation
sites of MinD in the membrane.
This assumption be-
comes most important when trying to model the striped
Min phenotypes observed in ﬁlamentous cells [23]. There
is an ongoing debate in the experimental literature about
the existence and possible nature of sites to which MinD
binds preferentially.
Recent work [24] has shown that
speciﬁc anionic phospholipids colocalise with MinD at
the poles and septum. An important as yet unanswered
question is which of these two determines the localisation
of the other or if there is some other factor upstream of
both.
APPENDIX A: THE DETERMINISTIC VERSION
AS A ONE-DIMENSIONAL MAP
In its simplest version (deterministic switching and fast
E-ring formation, cf. beginning of Sec. IV), our model
allows for a fully analytical solution in terms of a discrete
map. We choose to display the maximal length of the
MinD polymer as a function of the temporally previous
maximal length on the other side of the cell: lc
i+1 = f(lc
i)
(cf. Fig. 2).
To derive the map, we consider the following case: At
time t = 0, the DE-polymer on the left side (l) is decaying
(SD
l (0) = 0) and the D-polymer on the right side (r) is
growing. Without loss of generality, we choose t = 0 such
that the DE-polymer on the left just reached the length
ll(0) = γV
λ (cE,to −cE,th), which causes the cytosolic E-
concentration to grow above cE,th. This causes the D-
polymer on the right side to be capped: tc
r = 0 and
therefore its state to be switched: SD
r
: 1 →0.
We
assume that the D-polymer on the right had a length
lr(0) = lc
r at the time point of capping.
For a short
period of time, now both polymers are decaying: ll/r(t) =
ll/r(0)−γkoﬀt. At time td
l =
1
γkoff ll(0), the left nucleation
site becomes free for a new nucleation.
We now have to distinguish three diﬀerent cases:
1. The newly nucleated polymer on the left side gets
capped immediately if cE(td
l ) > cE,th. This is the
case if
lc
r < 2γV
λ (cE,to −cE,th).
(A.1)
Under this condition, the cytosolic MinE concen-
tration will never drop below cE,th. Any nucleating
MinD polymer will therefore be capped immedi-
ately, which evolves into the cytosolic state (i.e. no
polymer: lc
l = 0).
2. For slightly larger lc
r, nucleation on the left side
will happen right after the ﬁrst polymer (left) com-
pletely disassembled (ll = 0; tn
l = td
l ), as long as
cD(td
l ) > cD,th. Using tc
l =
1
γkoff [lc
r −γV
λ (cE,to −
cE,th)] in Eq. 9 leads to an expression for the length
of the D-polymer at the next capping:
lc
l =γV
λ

cD,to −koﬀ
kD
on
−cE,to + cE,th
−

cD,to −koﬀ
kD
on
+ cE,to −cE,th −λ
γV lc
r

· exp

−λkD
on
γkoﬀV

lc
r −2γV
λ (cE,to −cE,th)

.
(A.2)
3. If lc
r is even bigger (lc
r ≥γV
λ (cD,th + cE,to −cE,th)),
such that cD(td
l ) < cD,th, the new polymer on the
left will nucleate at tn
l =
1
γkoff [lc
r−γV
λ (cD,to−cD,th)].
Its capping will then happen at the stable ampli-
tude:
lc
l =γV
λ

cD,to −koﬀ
kD
on
−cE,to + cE,th
−

cD,th −koﬀ
kD
on

· exp

−kD
on
koﬀ
(cD,to −cD,th −cE,to + cE,th)

.
(A.3)
This is the amplitude of the stable oscillation and
all consecutive cappings will happen at this ampli-
tude, too.
The piecewise map derived above is displayed for var-
ious MinD and MinE concentrations in Fig. 3.
APPENDIX B: CONDITIONAL PROBABILITY
DISTRIBUTION FUNCTION FOR NUCLEATION
TIMES (REGULAR OSCILLATION)
In the stochastic version of our model, the probability
distribution function of the times one side of the cell is
free of polymer can be derived analytically if the system
is oscillating regularly (see Subsec. III C). This distribu-
tion function is conditional on the length ld of the poly-
mer present on the opposite side of the cell at the time
point where the nucleation site becomes polymer free (td
in Fig. 2). As described in Subsec. III B, we assume the
instantaneous probability for nucleation on a free nucle-
ation site at time t to be λnuc(t) = knuccnnuc
D
(t).
The probability for nucleation between times t and
t + dt is the probability of no nucleation until t and
then nucleating in t..(t + dt): Pnuc(t) dt = (1 −P(tn <
t))λnuc(t) dt.
P(tn < t) is the cumulative distribution
function. Without loss of generality, we assume td
l = 0
(i.e., the polymer on the left side just decayed completely
at time t = 0) and obtain
Pnuc(t) = λnuc(t) exp

−
Z t
0
λnuc(t′) dt′

.
(B.1)


## Page 13


13
The cytosolic D-concentration follows cD(t) = cD,to −
λ
γV (ld
r −γkoﬀt) for t ≤td
r (on the other side). For t ≥td
r,
there would only be cytosolic MinD (cD(t) = cD,to). We
do not consider this case, since it is outside the regular
oscillation pattern.
Putting cD(t) from above into Eq. B.1, one obtains
Pnuc(T f|ld) = knuc

cD,to −λ
γV ld + λ
V koﬀT f
nnuc
· exp
"
−
1
n + 1
knucV
λkoﬀ
 
cD,to −λ
γV ld + λ
V koﬀT f
nnuc+1
−

cD,to −λ
γV ld
nnuc+1!#
.
(B.2)
Fig. 11 shows typical shapes of this probability distri-
bution function (for a given ld) for high cooperativity in
nucleation and diﬀerent concentrations of MinD. From
Eq. B.2, it is obvious that the dependence of the prob-
ability distribution on ld is (up to a scaling factor) the
same as on cD,to.
APPENDIX C: CONDITIONAL PROBABILITY
DISTRIBUTION FUNCTION FOR CAPPING
TIMES (REGULAR OSCILLATION)
Equivalently to the preceding appendix, one can de-
rive an expression for the conditional probability distri-
bution function for the time of growth of a polymer.
In Subsec. III B we introduced the instantaneous prob-
ability for capping of a growing polymer at a time t:
λ(t) = kcapcncap
E
(t).
We only consider the approximative case of fast E-ring
formation (see Sec. IV).
The MinDE-polymer on the
right side is assumed to be decaying and has length ln
r
at time t = 0 (cf. Fig. 2). Without loss of generality
we assume that the D-polymer on the left side nucleates
and starts growing at time tn
l
= 0.
We now have to
distinguish three cases during the decay of the polymer
on the right side (td,E is the time when the growing tip
of the E-polymer reaches the cell wall):
1. First, the concentration of MinE monomers in the
cytosol is constant (lE
r = lE,ss
⇒
cE = cE,0 ≡
koff
kE
on ).
2. For td,E
r
< t < td
r, cE grows linearly: cE(t) = cE,0 +
λ
V koﬀ(t −td,E
r
).
3. After td
r, cE is constant again: cE = cE,to.
Putting these into the equivalent of Eq. B.1 gives the
conditional probability distribution function for the time,
at which the growing D-polymer on the left side gets
capped and switches states (see Eq. C.1 – we generalise
to T c and drop the side-dependence; cE,0 = koff
kE
on ; A =
λ
V koﬀ). Here, td =
1
γkoff ln and td,E =
1
γkoff (ln −lE,ss)
with lE,ss = γV
λ (cE,to −koff
kE
on ). The condition on ln only
enters through the dependencies in td,E and td.
Fig. 11 shows typical probability distribution functions
for capping (for a given ln) for high capping cooperativ-
ity and diﬀerent MinE concentrations. The dependence
of the probability distribution on ln is (up to a scaling
factor) the same as on cE,to for the important ﬁrst and
second part of the non-smooth Eq. C.1.
APPENDIX D: A MAP FOR THE PROBABILITY
DISTRIBUTION
Combining the two conditional probability distribu-
tions computed in Apps. B and C, one can derive a map
for the probability distribution of the amplitude during
regular oscillations. Here, we derive this map in the fol-
lowing form: Pn(ln
i ) = F(Pn(ln
i−1)), i.e.
the probabil-
ity distribution of lengths at nucleation (on the opposite
side) can be derived as a function of the distribution at
the previous nucleation (on this side – for notation see
Fig. 2).
We start with computing a relation between the two
probability distributions Pn(ln
i ) and Pd(ld
i ):
Pn(ln
i ) =
Z lmax
ln
i
p(ln
i |ld
i )Pd(ld
i ) dld
i .
(D.1)
The conditional probability distribution p(ln
i |ld
i ) can be
obtained from Eq. B.2 by replacing T f =
1
γkoff (ld
i −ln
i )
and multiplying with
1
γkoff (to ensure correct normalisa-
tion under the variable transformation). For the limits
of the integration one has to consider that ln
i will always
be smaller than ld
i (see Fig. 2). The upper limit is the
maximally possible length of a D-polymer (i.e. all MinD
is bound in one polymer (Eq. 4)).
With that, we obtain:
Pn(ln
i ) = knuc

cD,to −λ
γV ln
i
nnuc
exp

−
1
nnuc + 1
V knuc
λkoﬀ
·

cD,to −λ
γV ln
i
nnuc+1#
·
Z lmax
ln
i
exp

−
1
nnuc + 1
V knuc
λkoﬀ
·

cD,to −λ
γV ld
i
nnuc+1#
Pd(ld
i ) dld
i .
(D.2)
In a similar fashion, Pd(ld
i ) can be expressed as a func-
tion of Pn(ln
i−1):
Pd(ld
i ) =
Z lmax
ln
min
p(ld
i |ln
i−1)Pn(ln
i−1) dln
i−1.
(D.3)
The conditional probability distribution in Eq. D.3 can
be obtained from Eq. C.1 when replacing T c with the


## Page 14


14
Pcap(T c|ln) =
8
>
>
>
>
>
>
>
>
>
<
>
>
>
>
>
>
>
>
>
:
kcapc
ncap
E,0 exp
`
−kcapc
ncap
E,0 T c´
0 ≤T c < td,E
kcap(cE,0 + A(T c −td,E))ncap
· exp
“
−kcapc
ncap
E,0 td,E −
kcap
A(ncap+1)
h
(cE,0 + A(T c −td,E))ncap+1 −c
ncap+1
E,0
i”
td,E ≤T c < td
kcapc
ncap
E,to exp
“
−kcapc
ncap
E,0 td,E −
kcap
A(ncap+1)
·
h
(cE,0 + A(td −td,E))ncap+1 −c
ncap+1
E,0
i
−kcapc
ncap
E,to (T c −td)
”
T c ≥td
(C.1)
 0
 0.1
 0.2
 0.3
 0.4
 0.5
 0.6
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
4.3
4
3.7
T f [s]
p
cD,to [µM]
(a) Pnuc(T f |ld), ld = 1.5 µm
 0
 0.02
 0.04
 0.06
 0.08
 0.1
 0.12
 0.14
 0
 10
 20
 30
 40
 50
1.7
1.5
1.3
T c [s]
p
cE,to [µM]
(b) Pcap(T c|ln), ln = 1.5 µm
FIG. 11: Typical probability distributions for the time free of
polymer T f (top) and the duration of growth T c (bottom),
respectively. A number of curves are plotted for diﬀerent total
concentrations of MinD or MinE, respectively. The analyti-
cal expressions are given in Eq. B.2 for the upper panel and
Eq. C.1 for the lower one. Standard parameters as of Tab. II
are used and the probability distributions are given for the
conditions ld = 1.5 µm and ln = 1.5 µm, respectively. The
cooperativity for nucleation or capping is 6. For comparison,
the dotted lines show the probability distribution functions
for a reduced cooperativity nnuc/cap = 3. Note the broader
distributions for lower cooperativity as well as the noticeable
tail towards shorter T c in the lower panel for the dotted line.
solution of the deterministic relation that connects ld
i and
T c
i (Eqs. 8 and 9):
ld
i = −2ln
i−1 + 2γkoﬀT c
i + γV
λ

cD,to −koﬀ
kD
on

−
γV
λ

cD,to −koﬀ
kD
on

−ln
i−1

exp

−λkD
on
V
T c
i

.
(D.4)
Solving this equation for T c
i
gives a function T c
i
=
g(ln
i−1, ld
i ) that involves a LambertW function and can
therefore not be expressed in terms of elementary func-
tions.
For correct normalisation, the new conditional
probability distribution also has to be multiplied by the
derivative
∂g(ln
i−1,ld
i )
∂ld
i
.
The integration limits are the minimal and maximal
values of ln
i−1, such that the order of events in Fig. 2
(i.e. regular oscillations) is still fulﬁlled for a given ld
i .
The upper limit turns out to be lmax, whereas the lower
limit can be found as the solution to the polymer growth
equation with T c
i = T n
i−1. One ﬁnds
ln
min = −γV
λkD
on

koﬀLambertW

−
1
γV koﬀ
·
 −γV cD,tokD
on + γV koﬀ+ λkD
onld
i

· exp
cD,tokD
on −koﬀ
koﬀ

−cD,tokD
on + koﬀ

.
(D.5)
Putting Eq. D.1 and Eq. D.3 together, one obtains a
map from one probability distribution into the next one,
half a period later:
Pn(ln
i ) =
Z lmax
ln
i
1
γkoﬀ
Pnuc

T f = ld
i −ln
i
γkoﬀ
|ld
i

·
Z lmax
ln
min
∂g(ln
i−1, ld
i )
∂ld
i
Pcap
 T c = g(ln
i−1, ld
i )|ln
i−1

· Pn(ln
i−1) dln
i−1 dld
i .
(D.6)
The integrals can be computed numerically[38] and by
iterating Eq. D.6, a steady state probability distribution
can be obtained. A typical starting distribution for the
iteration would be a delta distribution or a uniform dis-
tribution and for typical parameter values, a steady state
distribution is reached after 3 to 5 iterations.
This approach is valid, as long as the vast majority
of events fall into the scheme depicted in Fig. 2, i.e. as
long as td
i > tc
i+1 and td
i > tn
i+1 (regular oscillations – see
Subsec. III C).
A more relevant quantity than ln, the length of a poly-
mer at the time of nucleation on the other side, is the
capping length lc, i.e. the amplitude of the oscillation.
To obtain the probability distribution for this length, one


## Page 15


15
needs to perform another integration:
Pc(lc) =
Z ln
max
ln
min
p(lc|ln)Pn(ln) dln.
(D.7)
The conditional probability distribution can be obtained
from Eq. C.1, when replacing T c with the appropriate
function of lc and ln that can be derived from a similar
relation as Eq. D.4. We obtain
p(lc|ln) = ∂T c(lc, ln)
∂lc
Pcap(T c = T c(lc, ln)|ln).
(D.8)
The lower limit of the integration is the same as in the
previous integration (Eq. D.5). For the upper limit one
needs to ﬁnd ln
i−1 such that ld
i = 0. This can be found by
solving Eq. D.4 with T c =
1
γkoff (ln −lc) for ln. In case
this solution is larger than lmax, lmax (Eq. 4) is the upper
limit.
APPENDIX E: PROBABILITY DISTRIBUTION
FUNCTION FOR THE PERIOD IN THE
OSCILLATORY STATE
Using the iterative approach described in the previous
appendix, the steady state probability distribution func-
tion for the lengths of D-polymers at a given time point
during regular oscillations can be found. Starting from
this distribution, we will compute the probability distri-
bution function for the period of the oscillations in this
appendix.
From Fig. 2, half a period T h (the time between two
consecutive nucleations on opposing sides) is found to be
T h = T n + T f and therefore Ph(T h) = R p(T f = T h −
T n|T n)p(T n) dT n. T n can be replaced by T n =
1
γkoff ln
and an additional probability distribution p(ld|ln) can be
introduced in order to obtain an equation involving only
distributions that have already been calculated:
Ph(T h) =
Z ln
max
0
Z ld
max
0
Pnuc(T f = T h −
1
γkoﬀ
ln|ld)
· p(ld|ln) dld Pn(ln) dln.
(E.1)
Pnuc(T f|ld) is given in Eq. B.2, how to obtain p(ld|ln)
is described in the preceding appendix and a steady
state distribution for Pn(ln) is also derived there (iter-
ating Eq. D.6).
The upper limits of the two integrals
are the smaller of {γkoﬀT h, lmax} for ln
max and ld
max is
the equivalent of Eq. D.5: ld
max =
γV
λ

cD,to −koff
kD
on

−
h
γV
λ

cD,to −koff
kD
on

−lni
· exp

−λkD
on
γkoffV ln
.
For the probability distribution function of the period
T = 2T h, one more integration is needed:
PT (T ) =
Z T
0
Ph(T h = T h′)Ph(T h = T −T h′) dT h′.
(E.2)
APPENDIX F: A LIMITING DETERMINISTIC
MAP FOR THE CASE OF HIGH
COOPERATIVITY
For the case of deterministic nucleation and stochas-
tic switching, we want to use the deterministic map as
shown in Fig. 3 as a rough guideline for the dynamics
of the system. In order to ﬁnd this underlying map, we
need to ﬁnd a replacement for the parameter cE,th in the
analytical expression of the map (Eqs. A.1– A.3) since
the MinE nucleation threshold does not have a meaning
if we assume stochastic capping. A natural choice is the
E-concentration at the median of the capping cumulative
distribution function Fcap(t). In the case of determinis-
tic switching this is a step function in cE with the step
at cE,th. For high ncap, Fcap(t) it is a steep sigmoidal
curve. For the vast majority of cases (kcap <
ln(2)
c
ncap
E,0 td,E
and kcap > ln(2)

cncap
E,0 td,E +
c
ncap+1
E,to
−c
ncap+1
E,0
A(ncap+1)
−1
), the
median capping time tM lies within td,E
≤
tM
≤
td.
With the integration of Eq. C.1 (and ln
=
γV
λ (cD,to −cD,th)) one ﬁnds the median time to be tM =
td,E + 1
A

−cE,0 +
h
cncap+1
E,0
−A(ncap+1)
kcap

kcapcncap
E,0 td,E −
ln(2)
i
1
ncap+1 
, which then leads to
cE(tM) =
h
cncap+1
E,0
−A(ncap + 1)
kcap
·

kcapcncap
E,0 td,E −ln(2)
i
1
ncap+1 .
(F.1)
We use this E-concentration as a replacement of cE,th
in Eqs. A.1–A.3 and plot the resulting maps in Fig. 10(d).
[1] J. Lutkenhaus, Adv. Exp. Med. Biol. 641, 49 (2008).
[2] H. Meinhardt and P. A. de Boer, Proc Natl Acad Sci U
S A 98, 14202 (2001).
[3] G. Meacci and K. Kruse, Phys Biol 2, 89 (2005).
[4] K. C. Huang, Y. Meir, and N. S. Wingreen, Proc Natl
Acad Sci U S A 100, 12724 (2003).
[5] M. Howard, A. D. Rutenberg, and S. de Vet, Phys Rev
Lett 87, 278102 (2001).
[6] R. Kerr, H. Levine, T. Sejnowski, and W. Rappel, Proc.
Natl. Acad. Sci. U.S.A. 103, 347 (2006).
[7] D. Fange and J. Elf, PLoS Comput. Biol. 2, e80 (2006).
[8] K. Kruse, Biophys. J. 82, 618 (2002).


## Page 16


16
[9] D. A. Drew, M. J. Osborn, and L. I. Rothﬁeld, Proc Natl
Acad Sci U S A 102, 6114 (2005).
[10] N. Pavin, H. C. Paljetak, and V. Krstic, Phys Rev E Stat
Nonlin Soft Matter Phys 73, 021904 (2006).
[11] E. N. Cytrynbaum and B. D. L. Marshall, Biophys J 93,
1134 (2007).
[12] F. Tostevin and M. Howard, Phys Biol 3, 1 (2006).
[13] Z. Hu, E. P. Gogol, and J. Lutkenhaus, Proc Natl Acad
Sci U S A 99, 6761 (2002).
[14] K. Suefuji, R. Valluzzi, and D. RayChaudhuri, Proc Natl
Acad Sci U S A 99, 16776 (2002).
[15] Y.-L. Shih, T. Le, and L. Rothﬁeld, Proc Natl Acad Sci
U S A 100, 7865 (2003).
[16] J. Szeto, N. F. Eng, S. Acharya, M. D. Rigden, and J.-
A. R. Dillon, Res Microbiol 156, 17 (2005).
[17] B. Downing, personal communication.
[18] X. C. Yu and W. Margolin, Mol Microbiol 32, 315 (1999).
[19] P. A. de Boer, R. E. Crossley, A. R. Hand, and L. I.
Rothﬁeld, EMBO J. 10, 4371 (1991).
[20] Z. Hu and J. Lutkenhaus, Mol. Cell 7, 1337 (2001).
[21] D. Raskin and P. de Boer, J. Bacteriol. 181, 6419 (1999).
[22] Z. Hu, A. Mukherjee, S. Pichoﬀ, and J. Lutkenhaus,
Proc. Natl. Acad. Sci. U.S.A. 96, 14819 (1999).
[23] D. M. Raskin and P. A. de Boer, Proc Natl Acad Sci U
S A 96, 4971 (1999).
[24] E. Mileykovskaya, A. C. Ryan, X. Mo, C. C. Lin, K. I.
Khalaf, W. Dowhan, and T. A. Garrett, J. Biol. Chem.
284, 2990 (2009).
[25] S. Mazor, T. Regev, E. Mileykovskaya, W. Margolin,
W. Dowhan, and I. Fishov, Biochim Biophys Acta 1778,
2505 (2008).
[26] A. Touhami, M. Jericho, and A. D. Rutenberg, J Bacte-
riol 188, 7661 (2006).
[27] G. Meacci, J. Ries, E. Fischer-Friedrich, N. Kahya,
P. Schwille, and K. Kruse, Phys Biol 3, 255 (2006).
[28] A. R. Champneys and M. di Bernardo, Scholarpedia 3,
4041 (2008).
[29] E. Mileykovskaya, I. Fishov, X. Fu, B. Corbin, W. Mar-
golin, and W. Dowhan, J. Biol. Chem. 278, 22193 (2003).
[30] F. Oosawa and S. Asakura, Thermodynamics of the Poly-
merization of Protein (Molecular Biology) (Academic
Press Inc, 1975).
[31] Y.-L. Shih, X. Fu, G. F. King, T. Le, and L. Rothﬁeld,
EMBO J 21, 3347 (2002).
[32] C. Hale, H. Meinhardt, and P. de Boer, EMBO J. 20,
1563 (2001).
[33] P. de Boer, R. Crossley, and L. Rothﬁeld, Cell 56, 641
(1989).
[34] To simplify the notation, we use the term monomer
throughout
this
paper,
even
though
the
original
model [11] as well as experiments suggest a polymer
formed of dimers.
[35] A simple Euler-forward routine (time step 10−4) was used
to solve the diﬀerential equations. To reduce error in av-
erages and to get smooth distributions, typically, simu-
lations were run for 106 −108 s of simulated time (i.e.
roughly 2 · 104 −2 · 106 capping events).
[36] If the capping occurs while the E-polymer on the oppo-
site side still has its steady state length lE,ss, our model
predicts a second E-ring of length zero. According to our
model equations, the E-polymer could nucleate (stochas-
tically) but the deterministic growth equation does not
support an elongation because cE is at the critical concen-
tration for elongation due to the presence of the other E-
ring. A more detailed model would incorporate stochastic
eﬀects in the growth and shrinking of the E- (and DE-)
polymer.
[37] In the opposite case (stochastic nucleation and determin-
istic capping), the transitions are not observed. In this
case, if the regular oscillation pattern is violated and
a D-polymer nucleates very late, cE > cE,th, and the
D-polymer as well as all following D-polymers will be
capped right away.
[38] To numerically compute the integrals, 5000 discrete
meshpoints were used over the interval 0 . . . L. After each
integration, the distribution is normalised.

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
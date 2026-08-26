---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1307.4583v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1307.4583v2_Simply_conceiving_the_Arrhenius_law_and_absolute_kinetic_constants_using_the_geo

> Source: 1307.4583v2_Simply_conceiving_the_Arrhenius_law_and_absolute_kinetic_constants_using_the_geo.pdf

> Pages: 8

---


## Page 1


Simply conceiving the Arrhenius law and absolute kinetic constants
using the geometric distribution
Denis Michel
Universite de Rennes1-IRSET. Campus de Beaulieu Bat. 13.
35042 Rennes cedex. denis.michel@live.fr
Although ﬁrst-order rate constants are
basic ingredients of physical chemistry,
biochemistry and systems modeling, their
innermost nature is derived from com-
plex physical chemistry mechanisms. The
present
study
suggests
that
equivalent
conclusions can be more straightly ob-
tained from simple statistics.
The dif-
ferent facets of kinetic constants are ﬁrst
classiﬁed and clariﬁed with respect to time
and energy and the equivalences between
traditional ﬂux rate and modern proba-
bilistic modeling are summarized.
Then,
a naive but rigorous approach is proposed
to concretely perceive how the Arrhenius
law naturally emerges from the geometric
distribution. It appears that (1) the dis-
tribution in time of chemical events as well
as (2) their mean frequency, are both dic-
tated by randomness only and as such, are
accurately described by time-based and
spatial exponential processes respectively.
Keywords:
Arrhenius law;
Rate constant;
Bose-Einstein distribution; Geometric law.
1
Introduction
Over zero kelvin, matter particles move, collide
and react with a certain probability. All these
events result from a transfer of energy provided
by either radiation or previous motions and ulti-
mately from a strong initial impulsion spreading
in the universe. Dynamic modeling of all molec-
ular systems, from enzymology to systems biol-
ogy, is grounded on the generalized use of kinetic
rates, usually written ”k” in traditional biochem-
istry.
Molecular events cover a wide range of
phenomena including motion, covalent modiﬁca-
tions or interactions. Although they are associ-
ated to all these events, kinetic rates are subtle
enough. Their physical meaning is generally ig-
nored by biochemists, who need only using the fa-
mous equation of Arrhenius [1] as a general rela-
tionship for the temperature dependence of rates
of reaction. According to this equation, derived
from the thermodynamic study of van’t Hoﬀ[2],
the logarithm of the rate constant is negatively
proportional to the inverse of temperature. Be-
side this macroscopic thermodynamic approach,
microscopic rate theories have then been devel-
oped, for example based on the probability of
occurrence of a transition state theory [3] or the
diﬀusion out of an energy well [4]. For complete
reviews on the subject, see [5, 6, 7]. Very atom-
istic models will not be considered here but the
simpliﬁed version of the transition state theory
most widespread in biochemistry textbooks will
be shown to suﬀer from several drawbacks. The
present study is aimed at recovering formally the
Arrhenius law and establishing a simple deﬁni-
tion of kinetic constants, expurgated from mech-
anistic considerations, using minimalist hypothe-
ses and simple statistical tools.
1
arXiv:1307.4583v2  [physics.data-an]  19 Dec 2013


## Page 2


2
Modeling the events
2.1
The classical ”mass action” ap-
proach to molecular events.
The very founder deﬁnition of chemical tran-
sitions is based on rate ﬂuxes, which are as-
sumed to be proportional to the amounts of
transformable reactants. In this view, which long
proved very eﬃcient, the constants k are coeﬃ-
cients of proportionality whose dimensions allow
to equalize the units in kinetic equations (time−1
for ﬁrst order reactions, or M−1time−1 for second
order reactions).
For example, the elementary
transition S
k→P can be modeled as follows
−d[S]
dt
= k[S]
(1a)
or
d[S]
[S] = −kdt
(1b)
yielding after integration,
ln [S]t
[S]0
= −k(t −t0)
(1c)
or
[S]t = [S]0e−kt
(1d)
Reciprocally,
[P]t = [S]0 −[S]t = [S]0(1 −e−kt)
(1e)
The probabilistic view described below can
be anticipated from this classical mass action ap-
proach if identifying the proportions of molecules
with probabilities, but the probabilistic view can
be introduced even more straightly.
2.2
Minimalist
mathematical
ap-
proaches more suitable for single
events in biochemistry
A living cell is not a dish as those used in chem-
istry labs, because certain subcellular compart-
ments contain very few macromolecules of the
same kind. For example, the notion of concen-
tration is obviously meaningless for a gene from
the X chromosome, present in a single copy in
each cell. To circumvent this problem, the single
molecule mathematical approach is preferable, il-
luminating for understanding biochemical mech-
anisms [8], and now widely used for modeling the
nonlinear mechanisms responsible for the reﬁned
behaviors of living systems [9]. The basic condi-
tion necessary to understand molecular events is
that they occur randomly, that is to say without
memory. If a given event is memoryless and has
a mean waiting time ⟨T⟩, then, the only possible
law governing its probability of occurrence is the
exponential distribution. At every time point t,
this probability is simply
P(X > t) = e−
t
⟨T ⟩
(2a)
P(X ≤t) = 1 −e−
t
⟨T ⟩
(2b)
This result can be easily demonstrated. The
absence of memory can be explicitly transcribed
into
∀t1, t2 ∈R+
P(X > t1 + t2 ∩X > t1) = P(X > t2)
(3)
Indeed,
P(X
>
t1 + t2|X
>
t1)
=
P(X > t1 + t2 ∩X > t1)/P(X > t1) = P(X >
t1 + t2)/P(X > t1)
Hence, Eq.(3) becomes
P(X > t1 + t2) = P(X > t1)P(X > t2)
(4a)
This relationship imposes to handle t as an
exponent, such that
e−k(t1+t2) = e−kt1e−kt2
(4b)
in which k is introduced to cancel the dimen-
sion of the exponent and turns to correspond to
a frequency (time−1) and the average transition
time is
⟨T⟩=
Z ∞
t=0
kt e−ktdt = 1
k
(5)
2.3
The ergodic correspondence
The recent outset of single molecule-based per-
spectives, particularly in biochemistry, radically
changed the traditional concepts of chemistry
(Table 1).
2


## Page 3


Table 1: Correspondences between the traditional bulk approach of chemistry and single molecule-
based perspective
Mass action approach
Single molecule approach
Concentration
State probability
Rate ﬂux
Poisson parameter
Total concentration of the leading macromolecule
1 (so that Vmax = kcat in enzymology)
Space
Time
Of particular interest is the replacement of
space (in which the concentration of reactants
is deﬁned), by time. This switch is fundamen-
tally rooted in the principle of ergodicity, ac-
cording to which the collection of states taken
at a single time by an inﬁnite number of parti-
cles, corresponds to those taken by a single par-
ticle during an inﬁnite time window.
Experi-
mental studies suggest that this assumption is
acceptable, as illustrated by the single enzyme
activity monitored in [10]. At equilibrium, the
classical Michaelis-Menten fraction of occupied
macromolecules can be deﬁned as well as a frac-
tional occupation time of a single macromolecule
[11]. Although the principle of ergodicity is gen-
erally presented as a non-demonstrated axiom,
the identical results obtained from the mass ac-
tion (section 2.1) and mathematical (section 2.2)
approaches allow to understand its basis.
3
Modeling the frequencies of
the events
3.1
Inconsistensies in the classical de-
scription of the transition state
theory
The version of the transition state theory most
widespread in textbooks suﬀers from several
drawbacks. Transitions from a starting point S
to a ﬁnal point P are supposed to follow a certain
delay because they are restricted by an energy
barrier. The transition is conditioned by prelim-
inary passage through an unstable reaction in-
termediate named activated complex and usually
written with a double-dagger label ‡. The result-
ing two-step reaction is represented in Fig.1.
Fig.1. The traditional energy barrier responsible for
reaction delays.
It is intriguing that when using this reasoning,
the elementary rate k to be deﬁned, is now re-
placed by 3 such rates (k1, k−1 and k2). The S‡
intermediate is considered as short-lived.
Ma-
nipulating rates as parameters of exponential
functions implies that the global transition from
S to P takes the form k = k1k2/(k−1 + k2). New
hypotheses should be introduced to simplify this
value
1st hypothesis, k2 >> k−1. Once gener-
ated, S‡ rapidly converts into P because of the
absence of energetic barrier between S‡ and P.
One haves k = k1 so that the deﬁnition of k is
simply replaced by that of k1, no way solving the
initial question: what is a k?
2d hypothesis, k2 << k−1.
This is the
hypothesis classically retained in the activated
complex theory. In this case, k = k2(k1/k−1), or
k = k2K‡. Now, the rate constant is deﬁned by
an equilibrium (as initially proposed by Arrhe-
nius himself, between normal and hypothetical
reaction-prone molecules).
K‡ = [S‡]
[S0] = e−∆E‡
kBT
(6)
from which the Arrhenius law can be recov-
ered
3


## Page 4


k = A e−Ea
kBT
(7)
In this expression, the mysterious constant
”A”, corresponding to a constant of integration
in the thermodynamic approach, is called ”pre-
exponential coeﬃcient” and is extremely impor-
tant since it gives to k the dimension of a rate
(time−1) [12]. In the present description, it cor-
responds to k2. According to physical principles,
this rate (written below k‡) includes an universal
component kBT/h time−1, corresponding to the
mean vibrational or translational energy (kBT)
where T is the temperature and kB is Boltz-
mann’s constant, divided by Planck’s constant h.
With kB = 1.38 10−23 J/K, T = 300 K and h =
6.63 10−34 J.s, one obtains kBT/h = 6.25 1012 /s,
which is very high indeed, but renders absurd the
initial hypothesis k2 << k−1.
3d hypothesis, k2 = k−1 = k‡.
In prin-
ciple, k‡ is expected to be similar for the two
barrier-free transitions starting from S‡, and in
the present case for the backward transition k−1,
such that
Then, k = k1k‡/(k‡ + k‡) = k1/2, letting un-
changed the initial question. In conclusion, we
see that this widespread description of rate con-
stants in textbooks is clearly not satisfying. An
alternative simple view of statistical distribution
of energy can be proposed.
3.2
The geometric approach to energy
distribution for systems capable of
unlimitedly storing energy
Consider a closed system in which every parti-
cle can store energy under diﬀerent forms (ro-
tational, vibrational or translational) which all
correspond to interchangeable energy quanta. If
a given number of energy quanta distribute ran-
domly over a given number of particles, then the
system can be compared to a very large pearl
necklace made of two kinds of pearls: B black
and W white pearls. The white beads are sup-
posed to correspond to energy quanta and the
black beads represent the separations between
the particles. Adjacent white beads clustered be-
tween two black beads correspond to the number
of energy quanta (written ε) in a single particle.
If the beads added to the string are drawn ran-
domly from a bag containing a huge number of
well-mixed black and white pearls (equivalent to
a drawing with replacement), then the probabil-
ity that any given bead on the string is white is
W/(W + B). Hence, the probability that an ar-
bitrarily chosen stretch of white beads contains
more than ε‡ beads is
P(ε > ε‡) =

W
B + W
ε‡
(8)
that can be rewritten, if deﬁning the ratio of
energy over particles W/B = ⟨ε⟩,
P(ε > ε‡) =

⟨ε⟩
1 + ⟨ε⟩
ε‡
(9)
For ⟨ε⟩and ε‡ large and of the same order of
magnitude and using the property of the expo-
nential function
lim
n→∞

1 + x
n
n
= ex
(10)
Eq.(9) approaches
P(ε > ε‡) ∼e−ε‡
⟨ε⟩
(11)
This exponential result is naturally expected
for large numbers of beads. Indeed, given that
the probability that any given bead on the string
is black is B/(W + B), then, when starting from
a black bead and walking along the string, the
number of beads to be examined to ﬁnd the fol-
lowing black one is, on average, the reciprocal of
the previous value (W+B)/B. As a consequence,
the average number of white beads in each inter-
val is [(W + B)/B] −1 = W/B, which is the
previously deﬁned entity ⟨ε⟩, or mean number of
energy quanta per particle. When switching to
a spatially continuous perspective by considering
a large pearl necklace with inﬁnitesimally small
beads, ε is the length of a white segment. Given
the randomness of bead sequence, the probabil-
ity that a segment is longer than ε‡ necessarily
follows an exponential distribution such that
4


## Page 5


P(ε > ε‡) = e−ε‡
⟨ε⟩
(12)
According to this probability, the kinetic rate
would be simply
k = k‡e−ε‡
⟨ε⟩
(13)
It is of course tempting to connect this result
to Boltzmann by identifying ⟨ε⟩with the mean
energy per particle.
This exponential function
should not be confused with the one deﬁned in
section 2.2, in which the unidimensional intensity
was conceived along time, whereas it is now spec-
iﬁed along the energy content. Consequently, the
probability that an event occurs at every time
point is an exponential of exponential
P(X > t) = e−k‡t.e
−ε‡
⟨ε⟩
(14)
This simple building of the Arrhenius law is
in fact related to the Bose-Einstein distribution,
assuming that energy quanta are inherently im-
material, permutable between the particles and
indeﬁnitely superposable in a single particle. Ac-
cording to the exponential relaxation observed
for many phenomena, this distribution is known
to approach the Maxwell-Boltzmann distribution
at high temperature.
Indeed, the probability
that a white stretch contains precisely ε‡ beads
follows a geometric law plus 1, such that the
(ε‡ + 1)th bead to be drawn should be black.
Hence,
P(ε = ε‡) =

⟨ε⟩
1 + ⟨ε⟩
ε‡
1
1 + ⟨ε⟩
(15)
illustrated in Fig.2 and whose maxima are
precisely obtained when ⟨ε⟩= ε‡. This simple
probability distribution indeed approaches the
Boltzmann’s one when ε is large enough. Eq.(15)
can be converted into its continuous version
P(ε = ε‡) ∼e−ε‡
⟨ε⟩

1 −e−1
⟨ε⟩

(16)
Fig.2. Probability distribution of particles with en-
ergy ε‡, when increasing the mean energy per particle
⟨ε⟩(that is to say the temperature).
and given that
∞
X
j=0
e−j
⟨ε⟩=

1 −e−1
⟨ε⟩
−1
(17)
one obtains
P(ε = ε‡) ∼
e−ε‡
⟨ε⟩
P∞
j=0 e−j
⟨ε⟩
(18)
which is similar to the celebrated formula of
Boltzmann, obtained using the entropy maximiz-
ing procedure and which predicts that the prob-
ability that any particle has an amount of energy
Ei is
P(Ei) = e−βEi/
n
X
j=0
e−βEj
(19)
where β = 1/kBT and the denominator is
the canonical partition function summed over
the n possible microstates [13]. Hence, there is
more than an analogy between the Boltzmann
and geometric treatments for the inﬁnitesimal
probabilities of large systems.
For small sys-
tems, the simple geometric plus 1 law of Eq.(15)
is preferable. The value of the rate constant of
Eq.(13) obtained using the simple necklace toy
model, is also very similar to the transition-state
rate derived from a Hamiltonian, described for
example in [5].
Most real systems are made of mixtures of
molecules of diﬀerent kinds, that can eventually
convert into each-others, but also continuously
exchange their energy quanta. These generalized
5


## Page 6


exchanges have large-scale energy buﬀering ef-
fects allowing the mean energy per type of parti-
cle to remain roughly constant, regardless of the
size of the considered subpopulation. This point
is important to understand that the deﬁnition of
rate constant proposed above remains true for
transient ﬂuxes in isothermal environments.
4
Transient ﬂuxes
The above developments hold in equilibrium con-
ditions, when the proportions of particles of the
same kind remain constant. This situation was
well described by Lewis [14] who compared the
diﬀerent populations of molecules to the habi-
tants of diﬀerent towns.
Although people are
constantly moving between diﬀerent towns, the
relative town sizes are metastable and remain
roughly constant in equilibrium.
But imagine
now that a given node is pulled out from the
network, such that the departures of molecules
are no longer compensated by arrivals: Is it pos-
sible to determine the exit rate in this situation?
Diﬀerent cases will be examined, under the as-
sumption that the exchanges of energy quanta
in the residual population of particles are more
rapid than the escape of particles.
4.1
Particle eﬄux in isothermal con-
ditions
This is the realistic situation holding for transient
phenomena in living cells, in which the overall
amount of energy quanta over all molecular com-
ponents roughly remains constant.
Under this
condition, although the arrival of new particles
is precluded, the mean energy per resident parti-
cle ⟨ε⟩remains constant, owing to collisions with
other types of components. In this case, the node
is expected to lose all its components with the
rate deﬁned in Eq.(13), in the same manner that
all boiling water disappears from a ban that is
constantly heated.
4.2
Eﬄux of particles from an ener-
getically isolated node
If, in addition to particle arrivals, the import and
export of pure energy between the node and its
environment are also precluded, then, the eﬄux
rate obviously decreases with time since energy
quanta accompany escaped particles. Moreover,
energy quanta are expected to disappear faster
than particles since only the most energy-rich
particles are ﬁltered by the threshold ε‡ for ﬂy-
ing away. Interestingly, the drop in total energy
resulting from the evasion of the ﬁrst particles
can prevent the remaining particles to obtain
their own travelling passport, rendering them
deﬁnitely prisoners in absence of energy refuel-
ing. A good illustration of this situation is the
rate of evaporation of water molecules from a hot
soup. Ordinary experience shows that evapora-
tion decreases as the soup cools. For modeling
this, let us transform the total number of en-
ergy quanta in the soup by a continuous variable
x(t) decreasing with time and the total number
of particles by a continuous variable y(t) also
decreasing with time. Let us suppose that the
medium is not sticky to allow the particles to
clear oﬀonce their energy content reaches ε‡.
Then, the eﬄux rate derived from the geomet-
ric distribution depends on the evolution of x(t)
and y(t) and obey the following system
k(t) = k‡

x(t)
y(t) + x(t)
ε‡
(20a)
with
˙x(t) = ε‡ ˙y(t)
(20b)
and
˙y(t) = −k(t)y(t)
(20c)
The fate of this system (Fig.3), depends on
the relative values of the reaction threshold ε‡
and of the starting amounts x0 and y0. If y0 ≤
x0/ε‡, then all the particles disappear, but if
y(t0) > x0/ε‡, then a fraction of the initial pop-
ulation of particles (y0 −x0/ε‡) remains stable,
such that
y∞= y0

1 −⟨ε⟩0
ε‡

(21)
6


## Page 7


It is amusing, but of course not necessary,
to recourse to Bose-Einstein to conceive that the
escape of the highest energy water molecules in
the form of vapor, can rapidly cool a bowl of hot
soup without signiﬁcantly reducing its volume,
in line with the right panel of Fig.3. It is also
clear that stirring the soup accelerates its cooling
by allowing the molecules whose energy content
is suﬃcient, to ﬂy away instead of unnecessarily
accumulating more energy.
Figure 3. Transient escape of energy (red lines) and particles (dark blue lines) from an energetically-isolated
subsystem. This unstable system can lose all its components or not, depending on the ratio between the initial
mean energy per particle and the threshold transition energy. Curves drawn to Eq.(20) using (k‡, ε‡, x0, y0)
= (6, 5, 40, 8) and (6, 8, 40, 20) for the left and right panel respectively.
5
Discussion
It is suggested here that the geometric distri-
bution is a simple substitute to traditional ap-
proaches to easily conceive the Arrhenius law,
without need for the accessory tools of statisti-
cal mechanics such as the Stirling approximation
and Lagrange multipliers and without recourse
to the particular mechanisms currently used in
rate theories, including collision, diﬀusion or S-
matrix theories. The fact that equivalent result-
ing behaviors are more directly obtained through
conveniently selected statistical approaches is not
a surprise. Boltzmann long proved that statisti-
cal and enumerating strategies are shortcuts to
recover previous physical results. Moreover, the
quest for simplicity does not forbid rigor, accord-
ing to the pragmatic recommendation of Josiah
Willard Gibbs: ”One of the principal objects of
theoretical research in any department of knowl-
edge is to ﬁnd the point of view from which the
subject appears in its greatest simplicity”. This
reductionist study suggests that the distribution
in time of chemical events, as well as the ener-
getic threshold over which they occur, are both
fundamentally related to the exponential law,
that is itself, together with its discrete counter-
part the geometric law, the exact formulation of
randomness.
Ackowledgement The author thanks Jean-
Christophe Breton and Benjamin Boutin for
helpful discussions.
References
[1] S.
Arrhenius,
Ober
die
reacktions-
geschwindigkeit bei der inversion von rohrzucker
durch sauren. Z. Physik. Chem. 4 (1889) 226-
248.
[2] J.H. Van’t Hoﬀ, Etudes de Dynamique Chim-
ique (Studies in Chemical Dynamics). Amster-
dam: (1884) F. Muller & Co.
[3] H. Eyring, The activated complex in chemical
reactions. J. Chem. Phys. 3 (1935) 107-115.
7


## Page 8


[4] H.A. Kramers,Brownian motion in a ﬁeld of
force and the diﬀusion model of chemical reac-
tions. Physica 7 (1940) 284-304.
[5] P. H¨anggi, P. Talkner, M. Borkovec, Reaction
rate theory: ﬁfty years after Kramers, Rev. Mod.
Phys. 62 (1990) 251-342.
[6] E. Pollak, P. Talkner, Reaction rate theory:
what it was, where is it today, and where is it
going? Chaos 15 (2005) 26116.
[7] Zhou, H.X. Rate theories for biologists. Q. Rev.
Biophys. 43 (2010) 219-293.
[8] Ninio, J. Kinetic and probabilistic thinking in
accuracy. In: Accuracy in Molecular Processes
(1986) (Kirkwood, TBL, Rosenberger, RF &
Galas, DJ, eds).
[9] D. Michel. Basic statistical recipes for the emer-
gence of biochemical discernment. Prog. Bio-
phys. Mol. Biol. 106 (2011) 498-516.
[10] H.P. Lu, L. Xun, X.S. Xie, Single-molecule enzy-
matic dynamics. Science 282 (1998) 1877-1882.
[11] D. Michel, Fine tuning gene expression through
short DNA-protein binding cycles. Biochimie 91
(2009) 933-941.
[12] K.J.
Laidler,
M.C.
King,
Development
of
transition-state theory. J. Phys. Chem. 87 (1983)
2657-2664.
[13] R.K. Pathria, Statistical mechanics, Second Edi-
tion (1996) (Butterworth-Heinemann).
[14] G.N. Lewis, G.N. A New Principle of Equilib-
rium. Proc. Natl. Acad. Sci. U.S.A. 11 (1925)
179-183.
8

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1307_4583v2_simply_conceiving_the_arrhenius_law_and_absolute_kinetic_constants_using_the_geo
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2013/1307_4583V2_SIMPLY_CONCEIVING_THE_ARRHENIUS_LAW_AND_ABSOLUTE_KINETIC_CONSTANTS_USING_THE_GEO.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

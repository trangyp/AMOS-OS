---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1502.06638v2
source: arxiv
tags: [arxiv, knowledge, quantum, reference]
---
# 1502.06638v2_Multiscale_modeling_of_exocytosis_in_the_fertilization_process

> Source: 1502.06638v2_Multiscale_modeling_of_exocytosis_in_the_fertilization_process.pdf

> Pages: 13

---


## Page 1


Multiscale modeling of exocytosis in the fertilization process
Aldo Ledesma Durán, I. Santamaría-Holek
UMDI-Facultad de Ciencias, Universidad Nacional Autónoma de México Campus Juriquilla, 76230, Querétaro, Mexico
We discuss the implementation of a multiscale biophysico-chemical model able to cope with the
main mechanisms underlying cumulative exocytosis in cells. The model is based on a diﬀusion equa-
tion in the presence of external forces that links calcium signaling and the biochemistry associated
to the activity of cytoskeletal-based protein motors. This multiscale model oﬀers an excellent quan-
titative spatio-temporal description of the cumulative exocytosis measured by means of ﬂuorescence
experiments. We also review pre-existing models reported in the literature on calcium waves, protein
motor activation and dynamics, and intracellular directed transport of vesicles. As an example of
the proposed model, we analyze the formation of the shield against polyspermy in the early events
of fertilization in sea urchin eggs.
Keywords: Calcium wave, protein motors, biochemical energy landscape, diﬀusion.
I.
INTRODUCTION
Biological processes frequently involve several mecha-
nisms and sub-processes that link diﬀerent temporal and
length scales such as, for example, intracellular molecu-
lar interactions to the scale of cells and beyond to the
behavior of collectives of cells and even organisms [1].
From an applied point of view, biomedical research often
performs experiments in which these scales are also im-
bricated [2]. The quantitative modeling of these systems
and the processes they perform often requires the exten-
sive use of computational simulations that have to incor-
porate several simulation techniques, each one according
to the time and space scale associated to the biological
process in question [3].
However, simple theoretical models able to cope with
these problems are less developed in the literature, al-
though they may be of great importance because they
can simplify the quantitative description without loss of
accuracy and, more important, by allowing to give clear
interpretations of the diﬀerent mechanisms in terms of
simple and well understood physicochemical laws.
In this short review, we aim to describe, link and use
three theoretical models reported in the literature that
allow to formulate a theoretical multiscale model able to
cope, with high precision, with intracellular processes in-
volving exocytosis, that is, with the process by which a
cell directs the contents of secretory vesicles out of the cell
membrane and into the extracellular space. We look at
this particular biological process due to its ubiquity and
biomedical importance ranging from transcelular trans-
port, insulin, neurotransmitter and enzyme secretions in
the energetic, nervous and early developmental metabolic
processes and pathways [4]. In particular, we will study
the case of the early events of fertilization, that is, the
formation of the shield against polyspermy in oocytes,
see Figure I.
Exocytosis is a very broad and complex process that
involves diﬀerent sub-processes such as the formation and
storage of vesicles in diﬀerent pools inside the cell, the
calcium signaling process, the active transport, and other
related processes such as vesicle docking, priming and the
ﬁnal fusion of the vesicle in the porosomes of the plas-
matic membrane[5, 6]. Many of these processes have been
studied experimentally and, as a consequence, several
proteins and enzymes have been discovered.
However,
beyond the knowledge of their existence and participa-
tion, there is still a fundamental lack of understanding
concerning the speciﬁc role they play in the secretion
process. [7].
Depending on the particular physiological function of
the exocytosis in each cell type, there are variations in
the rate of exocytosis, the lag time before it begins, its
time course, the proportion of vesicles that undergo fu-
sion in response to stimulation, the presence of single
or multiple granule types, and the nature of the regula-
tion of exocytosis by second messenger pathways [8]. For
example, in the particular case of fertilization of urchin
sea eggs, the exocytotic process involves sperm fusion
with cell membrane, the inﬂux of external calcium and
the subsequent elevation of calcium concentration due to
the internal pools. Subsequently, other fundamental pro-
cesses take place like the formation and storage of cortical
granules, the docking, priming and fusion of the secretory
vesicles with the plasma membrane, presumably through
SNARE proteins. Finally, the formation of the vitaline
envelope and the ﬁnal endocytosis and recycling of empty
vesicles are processes that may play an important role in
regulating the exocytosis [9].
The presence of micotubules and actin ﬁlaments may
play opposite roles depending on the cell type. In some
cases, the excytosis becomes favored by the presence of
the cytoskeleton, as in the case of serotonin and hyaline
secretion [10], whereas in other cases it may be inhibited
by the presence of the cytoskeleton that acts as a mechan-
ical barrier [11, 12]. Presumably, cytoskeleton based se-
cretion depends on the action of protein motors whereas
the opposite case suggest a diﬀusion controlled exocyto-
sis [13]. The distances travelled by the secretory vesicles
in both cases are very diﬀerent. In this review, we focus
arXiv:1502.06638v2  [q-bio.SC]  4 Jan 2016


## Page 2


2
Figure 1: Scheme showing the three main mechanisms associ-
ated to the initial events of oocyte fertilization. Sperm entry
through the acrosomic reaction liberates the genetic material
into the oocyte and triggers the local entrance of external
calcium and the subsequent propagation of a calcium wave
through the ooplasm. This process activates protein motors,
that actively transport clusters of cortical vesicles towards the
plasmatic membrane. Once fused, hyaline is released and ini-
tiates the gradual activation of the vitaline envelope until the
shield against polyspermy is completed.
on the ﬁrst case, that is, in which secretion is mediated
by cytoskeleton associated protein motors.
Therefore,
for the particular case of the urchin sea fertilization, we
have considered calcium signaling, vesicle diﬀusion and
protein motor activation and its processivity as the rate
controlling steps in the secretion process.
An appropriate measure of the cumulative exocytosis
by release site can be performed with the help of ﬂuores-
cence experiments [10, 14, 15]. In these experiments, a
ﬂuorescent dye is dissolved in the culture medium in such
a way that it is activated when becomes adsorbed in the
plasma membrane and is illuminated with the appropri-
ate light. During secretion, intracellular vesicles fuse with
the plasmatic membrane to release its contents. Exposed
to the culture medium, the membrane of the vesicles ad-
sorbs the dye and increases the local ﬂuorescence, see
Figure I.
In view of this, the theoretical description of cumula-
tive exocytosis is based on an apparently simple model.
The main question is to know the number of vesicles that
arrive to a given release site of area A in the membrane
and fuse with it as a function of time. Therefore, if J(t)
counts the number of cortical granules per unit area that
reach the release site at the membrane per unit time, then
the number n(t) of fused cortical granules as a function
of time is given by the relation
n(t) = Aξ
ˆ t
0
J(d, t′)dt′,
(1)
0
50
100
150
200
250
300
350
0
5
10
15
20
25
30
TimeHsecL
Cumulative Exocitosis
Figure 2: Sample traces of exocytosis in eggs for diﬀerent
external calcium concentrations. For each series, the number
of newly emerged exocytosis disks in each image frame was
counted.
This number plus the numbers from all previous
frames gave the cumulative number for this time point. Each
line correspond to diﬀerent values of external calcium: 0.4, 2
and 10mM for blue, orange and green points respectively. For
ﬁtting we use β = 1×10−6s−1, w = 223.6s−1 in equation (2).
Other parameters appear in the box inside the text.
where A is the measure area and d the initial position
of the vesicle cluster with respect to the plasmatic mem-
brane [15]. The fusion eﬃciency parameter ξ is the frac-
tion of vesicles that release its content with respect to
the total number of vesicles arriving at the plasma mem-
brane.
Here, for simplicity, we will assume that this
parameter is the unity. In principle, this simple model
quantiﬁes the cumulative exocytosis observed in experi-
ments [14, 15].
However, it is clear that the current J(t) must be deter-
mined explicitly in order to make a quantitative progress.
Determining J(t) is not a trivial task. The mechanism of
the secretion of the vesicular contents out of the cell is
a complex process that involves calcium signaling, acti-
vation and action of several cytoskeletal motors through
distances typically involving few microns. This is an en-
ergy consumption process due mainly to the activity of
the protein motors and pumps.
Therefore, this makes
very important to consider the detailed description of
the dynamics and energetics of these entities.
In fact, in order to obtain J(t) and perform the pro-
gram outlined, one needs to formulate a multiscale model
that accounts for the initial events of fertilization. In par-
ticular, we have to reproduce the reaction-diﬀusion wave
propagation of internal and external calcium and couple
it with a directed diﬀusion model describing the trans-
port of granule clusters containing hyaline to the plasma
membrane.
This second step considers in parallel the
biochemical kinetics of protein motors, kinesins, myosins
and dyneins [16]. As a consequence, our work gives quan-
titative evidence that the long time enzyme secretion of
cortical vesicles or granules is driven by protein motors,


## Page 3


3
mostly by kinesins.
The paper is organized as follows.
In Section 2 we
review previous theoretical works on reaction-diﬀusion
calcium signaling; protein motor biochemistry, energet-
ics and dynamics; and ﬁnally on diﬀusion in the presence
of external forces, that allow to propose an unifying view
of the exocytotic processes from the a physical chem-
istry point of view. In Section 3 we apply the multiscale
model to describe the slow formation of the shield against
polyspermy, which occurred when exocyted vesicles lift
the viteline envelope away. In particular, we join the re-
sults of the pre-existing models on calcium waves, protein
motors activation and intracellular directed transport of
vesicles in a cell for a successful quantiﬁcation of cumula-
tive exocytosis previously reported in experimental data.
Finally, Section 4 is devoted to present our main conclu-
sions.
II.
REVIEW OF THEORETICAL
BACKGROUNDS
As we have already mentioned, the exocytosis of sub-
stances by cells comprise several mechanisms whose in-
terplay is essential.
This interplay links several time
and length scales that should be modeled in a nested
way. Looking at the events, the entrance of external cal-
cium into the cell through the corresponding ion chan-
nels and its interaction with the intracellular calcium is
the triggering one of subsequent processes, like activa-
tion of cytoskeletal-based protein motors and their active
transport of vesicles and granules towards the plasmatic
membrane along microtubules. Here, we review previous
theoretical work reported on these three main processes.
In order to ﬁx ideas, we will discuss the general aspects
of the three models by considering the phenomenology as-
sociated to the fertilization of sea urchins eggs. This may
help the reader to create a clearer image of the secretion
process and the mechanisms involved.
A.
Locally-constrained and directed diﬀusion
The mechanisms participating in exocytotic processes
that we already discussed, calcium wave signaling and
protein motor action converting chemical energy into me-
chanical one, can be linked by means of a diﬀusion model
in the presence of external forces. Because this diﬀusion
equation is very general, we will ﬁrst discuss it in order
to show where the other mechanisms enter.
Mass transport inside cells is always aﬀected by ther-
mal agitation that induces a diﬀusive motion. This dif-
fusion is more or less important depending on the exter-
nal forces acting over the transported bio-particles. In
addition, the intracellular medium consists of a wide va-
riety of polymers and organelles whose presence causes
a viscoelastic behavior of the cytosol which, in princi-
ple, should be taken into account [17]. As a consequence
of this, when bio-particles undergo diﬀerent forms of pas-
sive diﬀusion in the intracellular medium they often show
anomalous diﬀusion (subdiﬀusion) [18, 19].
Subdiﬀusion has been observed in the passive transport
of particles in the cellular medium whereas an enhanced
diﬀusion has been reported for particles driven by pro-
tein motors [20]. This enhanced diﬀusion was analyzed
in terms of a generalized diﬀusion equation containing
forces due to the cytoskeleton network and to the pro-
tein motors [10, 13, 21]. However, when protein motors
carry bio-particles of diﬀerent sizes, this anomalous dif-
fusion is sometimes weak and normal diﬀusion can be
used to describe the motion with an eﬀective diﬀusion
coeﬃcient.
Local conﬁnement and protein motor action are there-
fore the key ingredients to explain vesicle transport in
cumulative exocytosis [10, 21].
Let us consider ρ(x, t) as the number of transported
vesicles per unit volume and Dv is the diﬀusion coeﬃcient
of vesicles in the cytoplasm. Then, the time evolution of
ρ(x, t) is described by the general equation
∂ρ
∂t (x, t) = Dv∇2ρ −1
β ∇· [ρF]
(2)
where F is a vector which represents the total force over
the transported vesicles and β is the friction coeﬃcient of
the transported vesicles. Here, it has been proposed that
force F could be a combination of harmonic radial forces
[10, 13, 21]: 1) a locally constraining force that keeps the
vesicles ﬁxed to microtubule an 2) a pulling force due to
the activity of molecular motors.
Thus, the ﬁrst force can be modeled as resulting from
a local harmonic force F = −w2x which is applied simul-
taneously with the force of the motors that move with
velocity v [10, 21, 22]. The total force applied on the
vesicles is an harmonic force displacing in the same di-
rection as the molecular motors with velocity v(t). As a
consequence of this, it may be modeled by means of the
relation
F = −w2 [x −xmotor(t)]
(3)
where xmotor(t) represents the position of the motor as
a function of time [10, 22]. Hence, if the protein motor
velocity is, in general, time dependent, then the force
takes the form
F(x, t) = −w2

(x −xo) −
ˆ t
t0
v(t′)dt′

er,
(4)
where xo is the initial position of the transported vesi-
cles with respect to the release site. In writing Eq. 4,
we have supposed that: 1) mobilization of motor does
not occurred until some critical time t0 when local Ca2+
has reached some critical value; 2) before its activation,


## Page 4


4
kinesin exerts a trapping force −w2(x−x0) over the vesi-
cles, and 3) once activated, the movement and inﬂuence
of the kinesin is only radially outward, being er the out-
ward unity vector. Calcium waves and the biochemistry
of molecular motors, that will be discussed in the follow-
ing subsections, allow to determine an explicit expres-
sion for the average motor velocity v(t) and its activation
time. In general, we may assume that the process starts
instantaneously when there exist saturation levels of ATP
and local Ca2+ concentration increases over a threshold
value. This situation can be taken into account through
a Heaviside function in the form v(t) →Θ(t −ti)v(t),
where ti depends on time and position through Ca2+
concentration.
Inserting Eq. (4) in (2), one can ﬁnd ρ using the appro-
priate initial and boundary conditions. The experiments
suggest that one may use three distinct pools of vesicles
as initial condition [14]: one very near membrane, other
in the center of the cell and one in intermediate position.
As a boundary condition, one may suppose that vesicles
reaching the membrane fuse to the plasmatic membrane
at the same rate at which they arrive.
From the previous equations, we can know the number
of cortical granules that reach cell membrane during ex-
ocytosis. To obtain this quantity, one must calculate the
current of vesicles J(x, t) implicitly deﬁned by the con-
servation equation ρt = ∇· J. Direct comparison with
equation (2) reveals that the current is given by
J(x, t) = −Dv∇ρ + β−1ρF.
(5)
Since we are interested in cumulative exocytosis, we
need to sum each vesicle arriving to the membrane as a
function of time. If J(d, t) counts the density of cortical
granules reaching the membrane from the initial position
d of the cluster, then the number n(t) of fused vesicles is
given by the relation (1).
As we have mentioned above, we need now to deter-
mine the time at which the motors are activated and the
time dependence of the molecular motors. In order to
see how this can be done, in the following subsections we
will discuss the role and phenomenology of calcium waves
and signaling, and of the biochemistry and dynamics of
the molecular motors.
B.
Calcium waves
Two main models are widely used to explain intracel-
lular oscillations and waves: 1) the calcium induced cal-
cium release model (CIRC) and 2) the two-pool model
(TPM). Both models are based on reaction-diﬀusion
equations for the Ca2+ concentration and one for the
calcium stored in the internal reservoirs Ca2+
i . The elec-
tion of the model should be based in accordance with cell
type and the kind of stimulation. By solving these mod-
els with the appropriate boundary condition, one obtains
the spatio-temporal behavior of the Ca2+
i
concentration.
Inside the cells, after the external stimulation, oscilla-
tions of the calcium concentration produce spatial non-
homogeneities along the cell. These non-homogeneities
seem to induce a spatio-temporal organization of cell’s
activity, that is, calcium waves act as a signal starting
diﬀerent processes at diﬀerent times and positions, and
is a function of the initial stimulation.
In vertebrates, the Ca2+ is mainly stored in bones,
from where it may be released to the blood after the ad-
equate hormonal stimulation. Inside many types of cells,
Ca2+ it is stored mainly in the endoplasmatic reticulum.
This allows to use it when necessary. Intracellular Ca2+
concentration is lower than the extracellular one, 0.1µM
and 1µM, respectively. This implies that the entrance of
Ca2+ through the corresponding ion-channels after mem-
brane depolarization is an spontaneous irreversible pro-
cess. This means that no energy is necessary to add in
order to perform this entrance. After the response of the
cell to the stimulation is completed, molecular pumps
regulate again the Ca2+ concentration inside the cell.
This one is an energy consuming process which is neces-
sary because Ca2+ may be toxic for high concentrations
in blood and cells.
Speciﬁcally, the Ca2+ is removed from the cytoplasm
in two ways: 1) pumping it out of the cell and 2) pumping
it inside several organelles like the mitochondria, the en-
doplasmic reticulum (ER) or the sarcoplasmic reticulum
(SR). Thus, during the initiation and the propagation of
a calcium wave, the inﬂux of Ca2+ occurs in two ways: 1)
the entrance of extracellular calcium and 2) the release
of calcium from the internal reservoirs.
The two internal calcium reservoirs are activated by
two types of receptors: ryanodine and IP3.
With the
attachment of these receptors on the membrane, the ion-
channels open allowing the release of calcium to the cy-
tosol. Ryanodine is more common in neurons and pitu-
itary cells whereas IP3 is mainly found in non-muscular
cells.
Calcium-Induced
Calcium-Release
model.
The
calcium-induced
calcium
release-model
(CIRC)
was
originally proposed by Friel in Ref. [23] and it is more
frequently use in ryanodine dependent processes.
The CIRC model is based on a balance of Ca2+ ﬂuxes
in the cell as it is shown in Figure 2.
A single in-
ternal reservoir (ER) exchanges Ca2+ with the cytosol
through the ﬂuxes JL2 and JP 2. The cytosol, in turn ex-
changes calcium with the extracellular environment with
the ﬂuxes JL1 y JP 1. Denoting the calcium Ca2+ con-
centration in the cytoplasm by c and cs the calcium con-
centration in the internal reservoir Ca2+
i , the model pos-
tulates the following dynamics


## Page 5


5
Figure 3: Flux diagram for the CICR model. In this case,
a single calcium reservoir is activated due to the increase of
internal calcium concentration.
dc
dt = JL1 −JP 1 + JL2 −JP 2,
(6)
dcs
dt
= −JL2 + JP 2,
(7)
where the ﬂuxes depend on the concentrations in the
following way:
JL1 = k1(ce −c),
Entrance.
JP 1 =
k2c,
Exclusion.
JL2 = k3(cs −c),
Release.
(8)
JP 2 =
k4c,
Absortion.
Here, ce is the external Ca2+ concentration that may be
assumed as constant due to the large concentration dif-
ference. However, because a linear model do not leads
to the concentration instabilities responsible for the ap-
pearance of waves and oscillations, it is assumed that
the reaction rate k3 depends in a non-linear way on the
cytosolic calcium c in the form
k3 = κ1 +
κ2cn
Kn
d + cn .
(9)
This simple model provides an excellent quantitative de-
scription of experimental cytosolic Ca2+ oscillations and
their periods, and predicts the observed ﬂows in each cy-
cle [23].
The two-pool model.
The two-pool model, originally
proposed by Goldbeter [24], suggested the existence of
two calcium reservoirs that are activated in series by dif-
ferent agonists. Speciﬁcally, the ﬁrst reservoir is sensitive
to IP3 whereas the second one is sensitive to Ca2+. The
second pool performs a CICR-exchange process with the
extracellular medium, see Figure 4. Several peculiarities
of calcium dynamics for diﬀerent cellular types can be
successfully reproduced using this model [24].
Figure 4: Flux diagram for the two-pool model. In this case,
two diﬀerent calcium reservoirs sensitive to diﬀerent agonists
are activated in series.
As in the CICR model, a calcium ﬂow balance between
pools and the exterior is performed.
However, in this
case, the ﬂuxes are given by non-linear relations that
are determined independently in the experiment.
The
important assumption of the model is that the calcium
concentration in the ﬁrst pool (sensitive to IP3) is con-
stant during the whole process. Thus, as in the CICR
model, only the cytosolic calcium concentration and the
concentration inside the second pool cs change with time.
Hence, assuming also that the IP3 gives rise to a con-
stant Ca2+ ﬂux r, and that the calcium is pumped to
the extracellular medium with rate −kc, then the whole
dynamics is given by
dc
dt = r −kc −g(c, cs),
(10)
dcs
dt = g(c, cs),
(11)
where g(c, cs) represents the rate of change of Ca2+ in
the second pool that depends on the uptake and release
ﬂows
g(c, cs) = Juptake + Jrelease −kfcs,
(12)
where
Juptake =
V1cl
Kl
1 + cl
(13)
Jrelease =

V2cm
s
Km
2 + cm
s
 
cp
Kp
3 + cp

.
(14)
Here, Juptake is the rate at which the Ca2+ is pumped
towards the second pool, that is, by means of an active
mechanism, and Jrelease is the rate at which calcium is
released from this second pool. This is an active feedback
mechanism for the Ca2+ that is essential for the appear-
ance of calcium oscillations in the cytosol. Finally, kfcs
is the rate at which the calcium is released to the extra-
cellular medium. The exponents l, m and p and the other
parameters should be chosen appropriately for each case.


## Page 6


6
Calcium waves and the two-pool model.
Frequently,
Ca2+ oscillations do not occur in an homogeneous way
inside the whole cell. On the contrary, these oscillations
are organized spatially in the form of waves. The velocity
of these waves is notably similar in many diﬀerent types
of cells (5-20µm/s).
In general, these waves are inde-
pendent of the extracellular calcium and they are often
concentric, plane or even have a spiral shape. The util-
ity of these waves can be attributed to the intracellular-
extracellular communication.
In order to model these waves, it is assumed that the
cytosolic calcium c diﬀuses, and therefore it is added a
diﬀusion term to the equation (10). Therefore, the re-
sulting two-pool model for calcium waves takes the form
dc
dt = Dc∇2c + r −kc −g(c, cs),
(15)
dcs
dt = g(c, cs),
(16)
where Dc is the Ca2+ diﬀusion coeﬃcient in the cyto-
plasm [25].
C.
Biochemistry and dynamics of protein motors
Kinesins, myosins and dyneis are large families of
cytoskeleton-based protein motors that participate in the
exocytosis-endocytosis cycles of cells, among many other
processes, by transporting organelles and vesicles from
the inner regions of the cell towards the periphery [26].
An important case in which these motors play a key
role is in the plasmatic membrane resealing of oocytes.
Here, as we mentioned in the Introduction section, we
will consider the model case of membrane resealing of
sea urchin eggs [27, 28]. In this case, it has been sug-
gested that protein motors are involved in the docking
and delivery of vesicles during exocytosis. Using a con-
focal microscope, in Ref.
[14] it was observed inhibi-
tion of exocytosis in sea urchin eggs injected with ki-
nesin and myosin inhibitors. This observations support
the hypothesis that kinesin and myosin motors mediate
two sequential transport steps that recruit vesicles to the
release sites of Ca2+-regulated exocytosis. From this ex-
periment, it was concluded that kinesin leads the slow
phase of exocytosis delivering vesicles along the micro-
tubules from inner regions of the cell, while myosin leads
the fast phase, dragging outer vesicles trough ﬁlaments
of F-actin[14]. It also exists evidence that slow and pro-
longed release of insulin in β-cells is also a process medi-
ated by protein motors like kinesins and myosins. Finally,
it is opportune to mention that theoretical modeling of-
fered clear support to the hypothesis that protein motors
are responsible for the translocation of vesicles contain-
ing neurotransmitters in the soma of serotonergic neurons
[10].
As proteins, enzymes and molecular complexes, the
processes developed by protein motors use chemical en-
ergy stored into molecules such as ATP or GTP, pro-
duced by the mitochondrial system of the cell [1]. This
is an interesting issue: protein and molecular motors are
strongly coupled to their environments, from which they
obtain the "fuel" necessary to perform work during the
same process they carry out. That is, molecular machines
have not their inner fuel reservoirs. As a consequence of
this, their energetics should be described jointly with that
of the surrounding medium.
In vitro experimental studies determined the depen-
dence of protein motor activity on ATP concentrations
with well controlled conditions. This approach has ad-
vantages. For instance, it allows for a better analysis of
the detailed dynamics of the motors irrespective of the
medium, but may hide some aspects of its performance
in in vivo conditions, such as the transport of proteins,
RNA, vesicles and even organelles [29] that may be re-
lated, for instance, to several exocytosis-endocytosis pro-
cesses [10, 27, 28, 30–32].
Protein motor biochemistry.
There are essentially
two models that represent the motion of protein motors.
Here, we will focus our attention on the so called hand-
over-hand model, that was ﬁrst developed to describe the
particular problem of intracellular transport via kinesin
motion due to ATP hydrolysis [33–36].
The biochemical reaction mechanism modeling the ac-
tivity of kinesin motors was originally proposed in Ref.
[34] and consists on a sequence of six reactions (see also
Refs. [37, 38]). The ﬁrst reaction describes the forma-
tion of the enzyme-substrate complex MKTα due to the
capture of an ATP molecule (T) by the microtubule (M)
kinesin (K) complex MK with the head α of the kinesin
attached at position to the microtubule (the head β is
free in a retrograde position):
MKα + T
k1
−−−⇀
↽−−−
k−1
MKTα .
(17)
In this scheme, the complex MK plays the role of an
enzyme that acts over substrate T through a catalytic
reaction [34].
The second reaction is controlled by thermal ﬂuctu-
ations that induce conformational changes of the dimer
constituting the motor stalk. This produces a secondary
enzyme-substrate complex MKT ′
α that favors a step for-
ward because corresponds to an advanced position of the
β head:
MKTα
K†
−−⇀
↽−−MKT ′
α .
(18)
In general, this step is inﬂuenced by the load f (cargo
weight) attached to the kinesin [34].
The next reaction describes the attachment of the
free head domain β to the microtubule using an ADP
molecule (D) and forming the complex MKTαDβ. This


## Page 7


7
step is considered the slow step of the reaction mechanism
and therefore the one determining the overall velocity of
the reaction [33]. It is described by
MKT ′
α
k2
−→MKTαDβ .
(19)
This reaction occurs over a high free-energy barrier that
cannot be surmounted by thermal ﬂuctuations.
After
this attachment, two reactions occur that prevent the
detachment of the kinesin from the microtubule
MKTαDβ
k3
−→MKβTα ,
(20)
and
MKβTα
k4
−→MKβ(D ◦P)α .
(21)
The ﬁnal reaction of the ﬁrst step corresponds to the
hydrolysis of ATP at the active site α of kinesin. This
reaction produces an ADP molecule and an inorganic
phosphate Pi [35]. Hydrolysis produces a large amount
of energy that allows the enzyme to liberate the head α
and, in this way, surmount the high free-energy barrier
associated to step (19)
MKβ(D ◦P)α
k5
−→MKβ + D + Pi .
(22)
After this reaction, the cycle is completed and one recov-
ers an initial state MKβ one step forward from the initial
position and with lower free-energy [see Eq. (17)]. The
number of repetitions of this cycle that the molecular
motor is capable to perform determines its processivity.
ATP dependence of motor velocities.
For our pur-
poses, it is now convenient to consider the dependence
of protein motors velocity on the ATP concentration in
the surrounding medium.
We ﬁrst recall that motors
are activated when cytosolic calcium in its surroundings
reaches some critical value cc
i. At this time t0, the mo-
tor or the collectivity of motors start their walk along
the microtubule carrying a cluster of vesicles towards the
cell membrane. The time of activation depends upon mo-
tor position in the cell with respect to the origin of the
calcium wave.
Once the motors have been activated, their average ve-
locity determines the rate at which cortical vesicles, both
docked to the membrane as far from it, reach an fuse with
the cell membrane and are exocyted. In Ref. [33] it was
suggested that this dependence of the velocity on ATP
follows a Michaelis-Menten (MM) kinetics, and therefore
the following ATP concentration ([T]) dependence
v([T]) =
vmax[T]
[T] + KM
,
(23)
where vmax represents the maximum speed of the motors
and KM is the MM constant of the process. We deter-
mine both constants from experiments reported in Ref.
[39] for kinesins in sea urchin eggs. In these experiments,
0.1
1
10
100
0
1
2
3
4
5
ATP concentrationHΜML
Velocity of motorHΜmsL
Figure 5:
Kinesin velocity as a function of ATP concen-
tration.
Fitting was made using Minimal-Squares with a
Michaelis-Menten dynamics, eq.(23).
We have found that
vmax = 5.25µms−1 and KM = 14.93µM.
kinesins adhered to a solid substrate move a ﬁlament of
microtubule for some µm in presence of several ATP con-
centrations. The velocity of the microtubule is found to
be [T]-dependent according to Eq. (23). In the following
section we will use this dependence to obtain vmax by
ﬁtting experimental data with good results.
ADP inhibition and ﬁnite time walks.
Several experi-
mental studies showed that ADP may inhibit the proces-
sivity of protein motors, since kinesin, myosin and dyne
in heads act as multi-substrate enzymes [35, 40–42].
More recently, it was probed theoretically in Refs.
[37, 38], that taking into account the inhibition by ADP
in the reaction scheme already discussed, yields a ﬁnite
number of steps of a single walk of a protein motor. In the
case of kinesins, the average number of processive steps
predicted was around 60 to 120, in excellent accordance
with experimental observations.
Time dependence of protein motors velocity.
A con-
sequence of this fact is that the velocity of the protein
motors is a function of time. This is clear since each step
uses an ATP molecule that, after hydrolysis produces at
least one ADP and one Pi molecules. This means: 1)
The ATP concentration [T] evolves in time following, in
ﬁrst approximation, a linear relation [37]
[T] = −vmaxt −[T]0,
(24)
where [T]0 is the initial ATP concentration. 2) Consider-
ing that the autocatalytic production of [ADP] inhibits
the whole reaction scheme, in particular the formation of
the MKT enzyme-substrate complex, after many cycles
of hydrolysis the ADP concentration can be modeled by
a ﬁrst order kinetics of the form [37, 38]
[D]t = [D]o + [T]o(1 −e−kvt).
(25)
After solving the corresponding evolution equations of
the chemical kinetics, it was shown that the velocity of


## Page 8


8
0
time  (s)
velocity  (nm/s)
 0
400
1
50
s
Figure 6: Translational velocity of a kinesin motor as a func-
tion of time given by Eq. (26) with the following values for
the constants: values:
[T]o =
1 mM, [D]o =
0, v‡
max =
900 nm s−1,
kcat = 113 s−1,
kv = 5, 600 s−1 and
K‡
M =
2.24 µm.
Except K‡
M, all values were taken from refer-
ence [35].
Signiﬁcant values that do not appear explicitly
in Eq. (26) like vmax = 11.25µM s−1, [MK]o = 100nM and
K†
M = 28µM were taken also from reference [35].
Figure
taken from Ref. [38].
a kinesin activated at time t0 can be written in the form
[37]
v(t) =
vmax[τ −(t −t0)]
α −βe−kv(t−t0) + [τ −(t −t0)],
(26)
where kv and α are are parameters that can be measured
in the experiments and the stopping time is given by
τ = [T]o/vmax. For the cases when ATP concentration
is low, ADP inhibition controls the dynamics of the ki-
nesin, making its velocity strongly dependent on time, as
it is shown in Figure 6. However, for usual ATP concen-
trations in living cells, kinesin velocity is practically con-
stant until it stops at a given time that depends on the
initial ATP concentrations and the catalytic constants.
In rough terms, the stopping time is around τ ∼70sec,
a time that can be correlated to that for the duration
of near pools exocytosis [14]. Long time exocytosis may
lasts around few hundreds of seconds. Here, it should
be stressed that the initial time t0 is determined by the
initial position of the molecular motor with respect to
position at which the calcium wave initiated, and also by
the calcium wave velocity.
III.
A QUANTITATIVE EXAMPLE: EARLY
EVENTS OF FERTILIZATION IN SEA URCHIN
EGGS
Fertilization in sea urchin eggs has been widely studied
by biologists of the last century. There is a great amount
of experimental evidence describing multiple processes
during activation since the contact of the sperm with the
jelly: acrosome reaction, calcium wave spreading over
the cell, exocytosis of cortical granules and formation of
the fertilization envelope.
It is known that a cascade
of ionic and metabolic changes occur in the sea urchin
egg after contact with the sperm [43]. The egg response
to the fertilization stimulus is a rapid depolarization of
plasma membrane potential establishing the fast block to
polyspermy at the time that the eggs demonstrate a brief
global contraction within the ﬁrst 30 sec after fertilization
[44].
Simultaneously, another signaling process induces the
production of inositol triphosphate (IP3) and diacyl-
glicerol.
An increase in (IP3) initiates the release of
Ca2+ from intracellular stores and produces a calcium
wave, some seconds after fertilization, that travels across
the egg form the site of sperm entry to the opposite pole
[45, 46]. This wave of elevated calcium propagates trough
the entire egg. The maximum of concentration occurs in
cortical cytoplasm. This wave is preceded by a distinct,
short transient spike of calcium in the cortex which cor-
relates with the time of sperm-egg binding [47].
The increase of the intracellular calcium concentration,
[Ca2+]i, stimulates in turn a wave of cortical granule exo-
cytosis, resulting in the elevation of the fertilization enve-
lope and formation of the hyaline layer [44]. It has been
suggested that this transport of vesicles is carried out by
protein motors like kinesins and myosins [14]. Measure-
ments of secreted hyaline, that is, of fused vesicules in
the plasma membrane has been reported in [14].
As we have mentioned earlier, kinesin walk is activated
and regulated by the presence of ATP and intracellular
calcium [14]. In fact, after the local increase of [Ca2+]i,
kinesins and myosins, powered by the hydrolysis of ATP,
load the cargo and move along microtubules transport-
ing it from the interior of the cell towards the periphery.
Using our multiscale model, we show that the calcium
wave elevates the [Ca2+]i allowing activation of kinesins
near the cortex of the cell and mobilizing cortical gran-
ules to the cell membrane where they fuse and spread
their content to the viteline envelope during the process
of exocytosis till fertilization envelope is completed.
A.
Results
Calcium waves.
During fertilization, after a period
of latency which lasts about ∼7-40 sec, the eggs of sea
urchins generate a single ∼5-min calcium transient that
spreads as a wave across the ooplasm [48]. In Lytechinus,
induced calcium wave is directly preceded by an inﬂux of
calcium leading to a cortical ﬂash and is followed by a
few post-fertilization calcium transients [47]. This wave
spreads throughout the entire egg with a spherical wave
front and velocity between 5-10µm/s [49].
It is known that external calcium is needed at the on-
set of sea urchin natural fertilization [1]. This calcium is
available from the sea water in the moment of sperm
entry during the acrosome reaction [50].
Unfertilized
sea urchin eggs can release internal calcium stores via


## Page 9


9
Figure 7:
Schematic representation of the calcium wave
spatio-temporal evolution according to the two-pool model.
Endoplasmatic reticulum is distributed in homogeneous form
helping to maintain and propagate the calcium wave. Cytoso-
lic calcium diﬀuses with diﬀusion coeﬃcient Dc.
IP3 or non-IP3 -mediated mechanisms [46].
Following
insemination, a calcium wave occurs in the presence of
inhibitors against inositol triphosphate receptors (IP3R
s) or ryanodine receptors (RyR’s) but not when both in-
hibitor types are used, suggesting that the two receptors
may redundantly participate during fertilization [51].
Therefore, we will assume that the calcium dynamics
within the fertilized egg can be modeled with the two-
pool extended model. We will suppose that the endo-
plasmic reticulum (ER) represent the only internal store
of calcium with the release modulated by both IP3 and
Ca2+.
In addition, we will suppose that the network
of the ER spreads approximately inside the entire cell
[52]. If c and cs represent concentrations of cytosolic and
stored Ca2+, respectively, and we assume that only the
ﬁrst one is free to diﬀuse at rate Dc, then the dynamics
of calcium is dictated by Eqs.(15) and (16).
We solved Eqs. (15) and (16) using a Finite Element
Method. As a domain, we used a circle of radius ∼50 mi-
crons [49] with a closed border except at the point marked
by the arrow in Figure III A, where an initial concentra-
tion slightly higher than the equilibrium concentrations
simulates the entrance of external calcium due to the
acrosomic reaction. For the equations (15, 16), we ﬁx
typical values of the chemical parameters and adjust the
coeﬃcients Dc and r in such a way that: 1) cytosolic cal-
cium spreads as a single wave over the cell, as observed
in experiments; 2) the wave spreads with a circular wave
front; and 3) the velocity were in accordance with the
experiments reported in Ref. [51], see also Refs. [44–
46, 53]. We obtained that the two-pool model reproduces
remarkably well the spatio-temporal evolution of the cal-
cium wave in the oopplasm. Our results are represented
Figure 8: The left panel shows the results from our simulation
of a calcium wave using the Finite Element method. Param-
eters in equations (15) and (16) are given by r = 0.0075µM,
V1 = 0.45µ M s−1, k1 = 0.9µM, V2 = 2.275µMs−1,k2 = 2µM,
k3 = 0.9µM, k = 0.04s−1, kf = 0.005s−1, Dc = 50µms−2,
l = 2, m = 2 and p = 4. Cytosolic and stored calcium are set
up at their equilibrium values c = 0.1666 M and cr = 2.92M
in almost all the domain, except by a perturbation in the ﬁrst
one of value 1.3µM in the upper left part of the cell. We have
used zero ﬂux boundary conditions. Images are taken every 4
sec. Red and blue correspond to maximum and minimum of
cytosolic calcium concentration respectively. The right panel
correspond was taken from Ref. [51] and shows an experi-
mentally observed calcium wave within a sea urchin egg.
in the left panel of Figure 8 where the time evolution of
the calcium wave is compared with the results observed
in Ref. [51], right panel. In this ﬁgure, at time t = 0, the
small red semicircle indicates the point at which takes
place the initial local elevation of calcium concentration,
that is, where the acrosomic reaction takes places. The
blue color indicates the low basal calcium concentration
inside the oocyte before stimulation. Front velocity and
shape are very similar to the experimental ones. This
allows to reproduce the formation of the vitaline enve-
lope because the activation of the motors occurs at times
very similar to the experimental ones. The model does
not represents well the time scale for the reduction of
calcium concentration which in the experiments may last
few minutes.
Protein motors activation and dynamics.
Once hav-
ing the calcium dynamics, then we proceeded to study the
dynamics of protein motors based on the model discussed
in Section II.C. One hypothesis of this model is that the
speed has a Michaelis-Menten dynamics type. In the case
of kinesin present in the sea urchin egg, this assumption
can be corroborated through the experiments reported in
Ref. [39]. In the cited work, a partially puriﬁed kinesin
is adsorbed to a glass coverslip and mixed with micro-
tubules and ATP. The translocating activity of kinesin


## Page 10


10
0
20
40
60
80
0
1
2
3
4
5
6
TimeHsecL
Velocity of motor HΜmsL
Figure 9: Possible velocity proﬁles of molecular motor as a
function of time. We ﬁx the values of α = 4.8s and β = 4.7s
in equation (26). The values of kv are 5.6×103s−1 for orange
and red lines, and 8.9×10−1s−1 for green and blue. Note that
a smaller value of this parameter softens engine acceleration
at the beginning of its walk. The values of vmax are 5.25, 3.25,
1.5 and 0.44 micrometers per second from top to bottom.
to microtubules is observed by contrast microscopy at
diﬀerent concentrations of ATP. Experimental data have
been ﬁtted with Eq. (23) by least squares, corroborating
that velocity follows a Michaelis-Menten dynamics.
This result gives the maximum velocity entering Eq.
(26) for the speed of kinesin as a function of time. In
Figure (9), we show several possible velocity proﬁles vary-
ing two diﬀerent parameters (k, and vmax). While vmax
clearly controls the maximum speed reached by a kinesin,
kv indicates how smoothly the kinesin started his walk.
In these ﬁttings, we have used that average kinesin walk
takes about 70 seconds, in accordance with experimental
results. The molecular motor is rapidly activated after
calcium increase and starts carrying the transported vesi-
cles to the plasmatic membrane of the oocyte.
It is convenient to stress that the time at which a mo-
tor starts its walk depends on its distance from the point
of fertilization and to the cell cortex. Vesicles near the
entry point of the sperm come quickly to the plasmatic
membrane.
Those initially located far away from the
stimulation point have a larger latency for the initializa-
tion time ti that depends on the calcium wave velocity
and shape. The important result represented in Figure
(9) is that, given the ATP ooplasm conditions, the ve-
locity of the protein motors is almost constant within
the duration of the exocytosis. Note from Figure 6, that
for large ADP concentrations present, the velocity proﬁle
as a complicated time dependence, see for instance, the
dashed-dotted line.
Directed diﬀusion and cumulative exocytosis.
Finally,
we quantify the results of cumulative exocytosis reported
in [14] by linking the previous theoretical results through
the diﬀusion model. In these experiments, the number of
color
Dv(µm2s−1) v(µms−1) d(µm) n
green
0.6
1.0
5
47
orange
0.7
0.2
8
76
blue
0.6
0.05
8
27
Table I: Parameters of the model for the three proﬁles of Fig-
ure I. See text for details.
vesicles that are secreted is counted as a function of time
over the plasmatic membrane of the egg using confocal
microscopy. Experiments show that decreasing the ex-
ternal calcium causes a slower rate of exocytosis. These
results can be understood, at least qualitatively, using
the diﬀusion model discussed in Section II A.
In view of the results already discussed for the time de-
pendence of motor velocity, we may simplify the numer-
ical resolution of the diﬀusion equation by assuming, in
ﬁrst approximation, that kinesin moves with a constant
velocity.
Then we solve numerically equation (2) and
reproduced the experimental data on cumulative exocy-
tosis by adjusting the parameters (diﬀusion coeﬃcient,
friction coeﬃcient, frequency, initial position of the vesi-
cles and motor velocity). As it is shown by the lines in
Figure I, the ﬁts of the cumulative exocytosis with this
model is excellent, and gives many important information
on vesicle distribution, motor speeds and the viscoelastic
properties of the cell that otherwise remain hidden. This
information is contained in Table I, where the values of
the diﬀusion coeﬃcient, the average protein motor veloc-
ities, the initial distance between the clusters of vesicles
with respect to the plasmatic membrane and the num-
ber of vesicles per cluster are reported.
These values
correlate well with those obtained in other works ([10]),
although in the present case the average velocity is much
higher, fact possibly related with the biological nature of
the response. The number of vesicles per cluster is only
indicative and approximate, since no direct comparison
with the ultrastructure of the cell allows to compare these
values. In addition, ﬂuorescence measurements should be
normalized to a given region and the eﬃciency of vesicle
fusion with the membrane was assumed equal to one.
B.
Discussion
The ﬁts of the calcium wave using the two-pool model
(with the inclusion of the diﬀusive term) correctly re-
produce the proﬁle and speed of the calcium wave in its
initial propagation through oocyte. Notwithstanding, for
the recovery period in which calcium concentration de-
creases to its basal value we have found (of about 60
seconds) is well below that found in ﬂuorescence exper-
iments of about 7 minutes [45]. This can be improved
in our model considering the continuous exchange of cal-


## Page 11


11
cium with the outside and not only at the time of the
initial application. Furthermore, in our present work, the
stores of calcium inside the cell are distributed homoge-
neously within the cell, and therefore could no replicate
the rapid increase of calcium near the cell membrane at
the moment of fertilization [47]. We thought this can be
due to the greater presence of calcium stored in outer
regions of the egg.
However, for qualitative purposes,
the occurrence of calcium waves founded with the two-
pool model helps to understand the exchange mechanism
which produces calcium waves inside the egg.
We have satisfactory found that engine speed obeys a
Michaelis-Menten dynamic, corroborating that a kinesin
can reach a speed of up 5.25µms−1 in in vitro exper-
iments with high concentrations of ATP. However, the
models presented in this work allow us to think that this
velocity may be much lower in the fertilized sea urchin
eggs, where the engine speed when carrying vesicles is
severely limited not only by the availability of intracellu-
lar ATP [38], but also by the conditions of friction or drag
of the intracellular environment where it moves [10, 13].
It is therefore not surprising that in our ﬁttings of cumu-
lative exocytosis, the eﬀective velocity we found on our
adjustments (between 1 and 0.05µms−1) is substantially
lower than that of in vitro experiments . For the pur-
poses of this model, we assumed a constant motor speed,
however, more accurate results may be obtained follow-
ing the time dependence reported in [38]. This may allow
one to understand that this is only an approximation for
intracellular processes with a time scale considered com-
parably high to the acceleration and deceleration of ki-
nesin. However, these speed changes can be crucial in
terms of energy to understand the processivity and stop
of these motor proteins.
The diﬀusion model and drag of the transported vesi-
cles within a cell proposed by Santamaría-Hólek in [10]
proves to be extremely successful in quantifying cumu-
lative exocytosis in eggs of sea urchins. However, when
coupled with the calcium wave patterns, processivity of
molecular motors, applicability of this model to this bi-
ological system could be expanded to explain and quan-
tify the formation vitaline envelope emerging into the
egg to prevent polyspermy. This is due to the fact that
the model perfectly diﬀerentiate the start and coupling
of each process: when the fertilization process starts, it
emerges a wave of calcium whose concentration is known
at each position as a function of time [25]; when the cal-
cium concentration reaches locally a critical value at time
ti, a molecular motor begins its walk dragging outward
a vesicle [38]; the rate and the number of vesicles arriv-
ing at each position can be determined by the conditions
of diﬀusion and drag of the medium [10]. Thus, except-
ing the numerical complexity of coupling all the required
equations, the above model would allow us in the future
to quantify the spatio-temporal distribution of secreted
vesicles and understand the formation of the envelope.
IV.
CONCLUSIONS.
The multi-scale models are very useful when trying to
describe processes whose causes are described in diﬀerent
spatio-temporal scales, fact which occurs in most biolog-
ical processes. In this paper, we have revisited the de-
scription and modeling of three particular physicochemi-
cal mechanisms that are essential in secretion processes:
a) formation of calcium waves, b) the dynamics of molec-
ular motors based on its biochemistry, and 3) directed
diﬀusion of vesicles within a fertilized egg.
Within this analysis and with the help of previously
published results in literature, it was found that the ex-
tended two-pool model can be used to understand the
propagation of calcium waves in the ooplasm of sea urchin
eggs. Furthermore, the approach we followed in our work
has the advantage of allowing the integration of speciﬁc
information of other cell types where these waves occur,
for instance: geometry, exchange ﬂows with the extracel-
lular medium, location of internal pools and intensity of
initial application. We also reviewed and used a model
for the processivity of protein motors which is based on
their biochemistry. This model yields the time dependent
velocity proﬁles for the kinesin, protein which plays a key
role in the translocation of clusters of vesicles in many cell
types. For this, we reviewed and solved a simple diﬀusion
model for vesicle transport that integrates various factors
aﬀecting the movement of vesicles before fusing with the
cell membrane, namely diﬀusion and drag forces due to
the activity of protein motors. By solving this three com-
ponent model, we have successfully quantiﬁed cumulative
exocytosis previously reported in literature.
More importantly, in this paper we have described how
these three schemes can be integrated to quantify with
accuracy the formation of the viteline envelope. For this,
in addition to the description of each model, we pro-
posed the relationships between each of them, relation-
ships which are essential to understand this complex pro-
cess. Thus, this work establishes a theoretical foundation
useful for the understanding and analysis of secretion
processes, whose diﬃculty now is merely based on the
numerical resolution of mathematical equations.
In future work, we pretend to propose a more detailed
quantitative model which will consider aspects related
to the kinetics of docking and priming of the vesicles in
the porosomes [5, 6], as well as the detailed mechanical
description of swelling of the vesicles and the expulsion
of its content.
V.
ACKNOWLEDGEMENTS
We acknowledge N. J. López-Alamilla for useful dis-
cussions.
ALD acknowledges CONACyT for ﬁnancial
support under fellowship 221505 and DGAPA UNAM
through the grant No. IN-113415.


## Page 12


12
[1] B. Alberts, A. Johnson, J. Lewis, M. Raﬀ, K. Roberts,
P. Walter, (2008),Molecular biology of the cell, Garland
Science: New York.
[2] W. M. Saltzman, (2009), Biomedical Engineering: Bridg-
ing Medicine and Technology,
Cambridge University
Press: Cambridge.
[3] M.Mier-Schellersheim,
I.D.C.
Fraser,
F.
Klauschen,
(2009),
Multi-scale
modeling
in
cell
biology,
Wi-
ley Interdisciplinary Reviews:
Systems Biology and
Medicine,1(1): 4-14.
[4] J.P. Keener, J. Sneyd, (1998), Mathematical Physiology,
Vol.8, Springer: New York.
[5] L.L. Anderson, (2006), Discovery of the porosome, the
universal secretory machinery in cells, Journal of cellular
and molecular medicine, 10(1): 126-131.
[6] B.P. Jena, (1997), Exocytotic fusion: total or transient?,
Cell biology international, 21(5): 257.
[7] R. Jahn, (2004), Principles of exocytosis and membrane
fusion, Annals of the New York Academy of Sciences,
1014(1): 170-178.
[8] R.D. Burgoyne, A. Morgan, (2003), Secretory granule
exocytosis, Physiological reviews, 83(2):581-632.
[9] J-L. Wong, G.M. Wessel, FRAP analysis of secretory
granule lipids and proteins in the sea urchin egg, in Exo-
cytosis and Endocytosis, pp. 61-76. Humana Press, 2008.
[10] F. F. de Miguel, I. Santamaría-Holek, P. Noguez, C.
Bustos, J. M. Rubi, (2012), Biophysics of active vesicle
transport, a step for serotonin exocytosis by the neuronal
soma, PLoS one, 7(10): e45454.
[11] M. Oheim, W Stuhmer, (2000), Tracking chromaﬃn
granules on their way through the actin cortex, European
Biophysics Journal, 29(2):67-89.
[12] T. Lang, et al, (2000), Role of actin cortex in the sub-
plasmalemmal transport of secretory granules in PC-12
cells, Biophysical journal, 78(6): 2863-2877.
[13] I. Santamaría-Holek et al., (2009), Protein motors in-
duced enhanced diﬀusion in intracellular transport, Phys-
ica A, 388(8):1515-1520.
[14] G.Q. Bi, R.L. Morris, G. Liao, J.M. Alderton, J.M. Scho-
ley, R.A. Steinhardt, (1997), Kinesin- and Myosin-driven
Steps of Vesicle Recruitment for Ca2+-regulated Exocy-
tosis, The Journal of Cell Biology, 138(5): 999-1008.
[15] P.F. Baker , M.J. Whitaker, (1978), Inﬂuence of ATP
and calcium on the cortical reaction in sea urchin eggs,
Nature, 276:513-515.
[16] A. O. Sperry, Ed., (2010), Molecular Motors: Methods
and Protocols, Humana Press Totowa: New Jersey.
[17] F. Gittes, B. Schnurr, P. D. Olmsted, F. C. MacKintosh,
C. F. Schmidt, (1997), Microscopic viscoelasticity: shear
moduli of soft materials determined from thermal ﬂuctu-
ations, Physical review letters, 79(17):3286 .
[18] T. Gisler and D. A. Weitz,(1999),Physical Review Letters
82(7):1606-1609.
[19] I. Santamaría-Holek, J. M. Rubi, (2006), Finite-size ef-
fects in microrheology, The Journal of chemical physics,
125(6):064907.
[20] A. Caspi, R. Granek, M. Elbaum, (2000), Enhanced Dif-
fusion in Active Intracellular Transport, Physical review
letters, 85(26),5655-5658.
[21] I. Santamaría-Holek, (2014), Termodinámica moderma,
Trillas, México.
[22] A. Ledesma-Durán,(2009), Bachelor Thesis Modelos sim-
ples para la secreción somática de serotonina, UNAM,
México
[23] D.Friel, (1995), [Ca2+]i oscillations in sympathetic neu-
rons: an experimental test of a theoretical model, Bio-
physical Journal 68(5): 1752-1766.
[24] A. Goldbeter, G. Dupont, M.J. Berridge, (1990) Mini-
mal model for signal-induced Ca2+ oscillations and for
their frequency encoding through protein phosphoryla-
tion, Proceedings of the National Academy of Sciences,
87(4):1461-1465.
[25] G. Dupont, A. Goldbeter, (1994) Properties of Intracel-
lular Ca2+ Waves Generated by a Model Based on Ca2+-
lnduced Ca2+ Release, Biophysical Journal, 67(6):2191-
2204.
[26] R.D. Vale, (2003), The Molecular Motor Toolbox for In-
tracellular Transport, Cell, 112(4):467-480.
[27] G.Q.
Bi,
J.M.
Alderton,
R.A.
Steinhardt,
(1995),
Calcium-regulated
Exocytosis
Is
Required
for
Cell
Membrane Resealing,
The Journal of Cell Biology,
131(6):1747-1758. nd
[28] R.A. Steinhardt, G.Q.Bi, J.M. Alderton, (1994), Cell
Membrane Resealing by a Vesicular Mechanism Simi-
lar to Neurotransmitter Release, Science, 263(5145):390-
393.
[29] M. P. Dodding, M. Way, (2011), Coupling viruses to
dynein and kinesin-1, The EMBO journal, 30(17):3527-
3539.
[30] A.I.Ivanov, I.C. McCall, B.Babbin, S.N. Samarin, A.
Nusrat, C.A. Parkos, (2006), Microtubules regulate dis-
assembly of epithelial apical junctions, BMC cell biology,
7(1):12.
[31] B.H. Kwok, L.C. Kapitein, J.H. Kim, E.J.G. Peterman,
C.F. Schmidt,T.M. Kapoor, (2006), Allosteric inhibition
of kinesin-5 modulates its processive directional motility,
Nature chemical biology, 2(9):480-485.
[32] M. Malacombe, M.F. Bader, S. Gasman, (2006), Ex-
ocytosis in neuroendocrine cells: New tasks for actin,
Biochimica et Biophysica Acta, 1763(11):1175-1183.
[33] K. Visscher and M. J. Schnitzer, S. M. Block, (1999),
Single kinesin molecules studied with a molecular force
clamp, Nature, 400(6740):184-189.
[34] K. Visscher, M. J. Schnitzer, S. M. Block,(2000),Force
production by single kinesin motors, Nature Cell Biology,
2(10):718-723.
[35] W. R. Schief, R. H. Clark, A. H. Crevenna, J. Howard,
(2004),Inhibition of kinesin motility by ADP and phos-
phate supports a hand-over-hand mechanism, Proceed-
ings of the National Academy of Sciences of the United
States of America, 101(5):1183-1188.
[36] J. Howard, A. J. Hudspeth, R. D. Vale, (1989), Move-
ment of microtubules by single kinesin molecules, Nature,
342(6246):154-158.
[37] N.J López-Alamilla and I. Santamaría-Holek, (2012),
Reconstructing the free-energy landscape associated to
molecular motors processivity, Biophysical Chemistry,
167:16-25.
[38] I. Santamaría-Holek and N. J. López-Alamilla, (2014)
Biochemical physics modeling of biological nano-motors,
AIP Conference Proceedings, 1579(1):102-111.
[39] M.E. Porter et al., (1987), Characterization of the Micro-
tubule Movement Produced by Sea Urchin Egg Kinesin,
The journal of Biological Chemistry, 262(6):2794-2802.
[40] D. D. Hakney, (1988), Kinesin ATPase: Rate-limiting


## Page 13


13
ADP release. Proceedings of the National Academy of Sci-
ences, 85(17):6314–6318.
[41] M. L. Moyer, S. P. Gilbert, K. A. Johnson,(1996), Pu-
riﬁcation and characterization of two monomeric kinesin
constructs,Biochemistry, 35(20):6321–6329.
[42] B. H. Kwok, L. C. Kapitein, J. H. Kim, E. J. G. Peter-
man, C. F. Schmidt, T. M. Kapoor, Allosteric inhibition
of kinesin-5 modulates its processive directional motility,
Nature Chemical Biology, 2(9):480-485.
[43] D.J. Bonder, E.M, Fishkind, (1995), Actin-Membrane
citoeskeletal Dynamics in early Sea Urchin Development,
in Citoeskeletal mechanism during animal development,
ed. by G. Capco, Academic Press Inc.
[44] A. Eisen, D.P. Kerhart, S.J. Wieland, G.T. Reynolds,
(1984), Temporal Sequence and Spatial Distribution of
Early Events of Fertilization in Single Sea Urchin Eggs,
The Journal of Cell Biology, 99(5):1647-1654.
[45] S.A.
Stricker,
V.E.
Centonze,
S.W.
Paddock,
G.
Schatenn,(1992), Confocal Microscopy of Fertilization-
Induced Calcium Dynamics in Sea Urchin Eggs, Devel-
opmental Biology, 149(2):370-380.
[46] M. Whitaker, K. Swann, (1993), Lighting the fuse at fer-
tilization, Development, 117(1):1-12.
[47] S.S. Shen, W.R. Buck, (1993), Sources of Calcium in Sea
Urchin Eggs during the Fertilization Response, Develop-
mental Biology, 157(1):157-169.
[48] R. Steinhardt, et. al, (1977), Intracellular Calcium Re-
lease at Fertilization in the Sea Urchin Egg, Develop-
mental Biology, 58(1):185-196
[49] S.A. Stricker, (1999), Comparative Biology of Calcium
Signaling during Fertilization and Egg Activation in An-
imals, Developmental Biology,211(2):157-176.
[50] R. Cretón,L.F. Jaﬀe, (1995), Role of calcium inﬂux dur-
ing the latent period in sea urchin fertilization, Develop-
ment, growth and diﬀerentiation, 37(6):703-709.
[51] A. Galione et al., (1993) Redundant Mechanisms of
Calcium-induced Calcium Release Underlying Calcium
Waves During Fertilization of Sea Urchin Eggs, Science,
261(5119):348-352.
[52] M. Terasaki, C. Sardet, (1991), Demonstration of Cal-
cium Uptake and Release by Sea Urchin Egg Cortical
Endoplasmic Reticulum, The Journal of Cell Biology,
115(4):1031-1037.
[53] K. Swann, M. Whitaker, (1986), The Part Played By
Inositol Trisphosphate and Calcium in the Propagation
of the Fertilization Wave in Sea Urchin Eggs, The Journal
of Cell Biology, 103(6)2333-2342.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
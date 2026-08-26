---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1509.02184v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1509.02184v1_Bacterial_hydrodynamics

> Source: 1509.02184v1_Bacterial_hydrodynamics.pdf

> Pages: 17

---


## Page 1


Bacterial Hydrodynamics∗
Eric Lauga†
Department of Applied Mathematics and Theoretical Physics, Centre for Mathematical Sciences, University of Cambridge,
Wilberforce Road, Cambridge, CB3 0WA, United Kingdom
(Dated: September 9, 2015)
Bacteria predate plants and animals by billions of years. Today, they are the world’s smallest
cells yet they represent the bulk of the world’s biomass, and the main reservoir of nutrients for
higher organisms.
Most bacteria can move on their own, and the majority of motile bacteria
are able to swim in viscous ﬂuids using slender helical appendages called ﬂagella. Low-Reynolds-
number hydrodynamics is at the heart of the ability of ﬂagella to generate propulsion at the micron
scale. In fact, ﬂuid dynamic forces impact many aspects of bacteriology, ranging from the ability
of cells to reorient and search their surroundings to their interactions within mechanically and
chemically-complex environments. Using hydrodynamics as an organizing framework, we review
the biomechanics of bacterial motility and look ahead to future challenges.
I. INTRODUCTION
Bacteria constitute the bulk of the biomass of our
planet.
However, since we need a microscope to see
them, we often forget their presence. Observing life in the
ocean, we see ﬁsh and crustaceans, but miss the marine
bacteria that outnumber them many times over. On land,
we see animals and plants, but often forget that a hu-
man body contains many more bacteria than mammalian
cells.
While they are responsible for many infectious
diseases, bacteria play a critical role in the life of soils
and higher organisms (including humans) by perform-
ing chemical reactions and providing nutrients (Madigan
et al., 2010).
Ever since microscopes were invented, scientists have
worked to decipher the rules dictating the behavior of
bacteria. In addition to quantifying the manner in which
bacteria shape our lives and teach us about our evolu-
tionary history, biologists have long recognized that the
behavior of bacteria is inﬂuenced by the physical con-
straints of their habitat, and by their evolution to maxi-
mize ﬁtness under these constraints. The most prominent
of these constraints is the presence of a surrounding ﬂuid
(Vogel, 1996). Not only are all bacteria found in ﬂuids,
but being typically less than a hundredth of a millime-
ter in length, they experience much larger viscous forces
than inertial forces, and have adapted their behavior in
response to these forces.
Most bacteria are motile (Jarrell & McBride, 2008;
Kearns, 2010) and this motility is essential for the eﬀec-
tiveness of many pathogens (Ottemann & Miller, 1997).
The most common form of bacterial motility is swim-
ming.
In order to swim, bacteria have evolved ﬂag-
ella (originally from secretory systems), which are slen-
der helical appendages rotated by specialized motors,
and whose motions in viscous environments propel the
∗to appear in: Annu. Rev. Fluid Mech. 48 (2016)
†e.lauga@damtp.cam.ac.uk
cells forward (Bray, 2000).
The surrounding ﬂuid can
be seen both as a constraint and an advantage.
It is
the presence of the ﬂuid itself and its interactions with
three-dimensional bacterial ﬂagellar ﬁlaments which al-
lows cells to move and sample their chemical environ-
ment – a crucial step for the cells to display robust and
adaptive chemotactic responses to both attractants and
repellents, for nutrients, but also temperature, pH, and
viscosity (Berg, 1993, 2004; Blair, 1995; Purcell, 1977).
But as they self-propel, bacteria are subject to the
external constraints set by the physical world, and in
particular by hydrodynamics. In this review, we high-
light the consequences of ﬂuid dynamics relevant to the
swimming of bacteria in viscous environments.
Natu-
rally, the biophysics of bacteria locomotion involves many
aspects of soft matter physics, including nonlinear elas-
ticity, screened electrostatics, and biochemical noise, and
hence ﬂuid dynamics represents but one feature of the
complex balance of forces dictating the behavior of cells
as they search their environment. The choice made here
is to use hydrodynamics as an organizing framework to
overview various aspects of cellular locomotion.
We start by a biological overview of bacteria as cells,
their geometry, the way they swim, and the variations
among diﬀerent species (§II). We then review the basic
hydrodynamics features of ﬂagellar propulsion (§III) fol-
lowed by the ﬂows induced by swimming bacteria (§IV).
We next address the ﬂagellar polymorphs, their compar-
ative hydrodynamics, and the potential relevance to evo-
lution of the ﬂagellum (§V). With individual ﬂagella un-
derstood, we detail how ﬂuid forces may play a role in
the actuation of multiple ﬂagella and be used by cells to
reorient (§VI). The last three sections are devoted to lo-
comotion near surfaces (§VII), in external ﬂows (§VIII)
and in complex ﬂuids (§IX).
Throughout this review, the focus will be on single-
cell behavior. Our purpose is to understand the way a
single bacterium exploits, and is subject to, the physi-
cal constraints from the surrounding ﬂuid. Other use-
ful reviews can be used as complementary reading, in
particular those highlighting the hydrodynamics of low-
arXiv:1509.02184v1  [physics.flu-dyn]  7 Sep 2015


## Page 2


2
FIG. 1 Atlas of ﬂagellated bacteria. (a) Peritrichous Escherichia coli (Howard Berg, Harvard University); (b) Polar monotric-
hous Pseudomonas aeruginosa (Fujii et al., 2008); (c) Polar lophotrichous Photobacterium ﬁscheri (Allen & Baumann, 1971);
(d) Polar amphitrichous Ectothiorhodospira hatochtoris (Imhoﬀ& Tr¨uper, 1977); (e) Spirochetes with endoﬂagella Borrelia
burgdorferi (Goldstein et al., 1996). All ﬁgures reproduced with permission.
Reynolds number swimming (Brennen & Winet, 1977;
Lauga & Powers, 2009; Lighthill, 1975), the ﬂuid dy-
namics of plankton (Goldstein, 2015; Guasto et al., 2012;
Pedley & Kessler, 1992), reproduction (Fauci & Dillon,
2006; Gaﬀney et al., 2011), and collective cell locomotion
(Koch & Subramanian, 2011).
II. BIOLOGICAL ATLAS
Bacteria come in many diﬀerent shapes (Madigan
et al., 2010). Those able to swim in ﬂuids can be roughly
divided into two categories: bacteria whose propulsion
is driven by helical ﬂagellar ﬁlaments located outside a
non-deforming cell body (the overwhelming majority, il-
lustrated in Fig. 1a-d) and those with spiral-like body
undergoing time-varying deformation (Fig. 1e).
Our understanding of how ﬂagellated bacteria swim
has its roots in a series of investigations in the 1970s
showing conclusively that – unlike the active ﬂagella of
eukaryotes, which are active and muscle-like (Bray, 2000)
– bacterial ﬂagellar ﬁlaments are passive organelles (Berg
& Anderson, 1973; Silverman & Simon, 1974). Typically
a few to ten microns in length, and only 40 nm in di-
ameter, bacterial ﬂagellar ﬁlaments are helical polymers
whose structure is discussed in detail in §V. Each ﬁla-
ment is attached to a short ﬂexible hook (≈60 nm in
length, see Fig. 2) acting as a universal joint. The hook
is turned by a stepper motor driven by ion ﬂuxes (bac-
terial rotary motor, Fig. 2) which is well characterized
molecularly (Berg, 2003).
Some ﬂagellated cells are called peritrichous and have
many motors (and thus many ﬂagella) located randomly
at various positions on the cell body (Fig. 1a). This is
the case for the bacterium Escherichia coli (or E. coli),
chosen as a model organism to study the fundamen-
tal biophysical aspects of cell motility and chemotaxis
(Berg, 2004).
In contrast, polar bacteria have motors
only located at poles of the body. Of the polar bacteria,
monotrichous bacteria only have one motor, and thus
one ﬁlament (Fig. 1b), lophotrichous cells have a tuft of
ﬂagella originating from a single pole (Fig. 1c) while am-
phitrichous bacteria have ﬂagella at each pole (Fig. 1d).
Note that variations in this classiﬁcation exist; for exam-
ple, some monotrichous or lophotrichous bacteria are not
polar. In all cases, the rotation of the motor is transmit-
ted to the hook, which in turn transmits it to the heli-
cal ﬁlament, leading to the generation of hydrodynamic
propulsive forces, as explained in detail in §III.
Fluid dynamics was used to determine the torque-
frequency relationship for the rotary motor by linking
tethered bacterial ﬂagella to beads of diﬀerent sizes in
ﬂuids of varying viscosity (Chen & Berg, 2000).
The
resulting change in the Stokes resistance to bead rota-
tion allowed to show that the rotary motor works at
constant torque for a wide range of frequencies in the
counter-clockwise (CCW) directions (the frequency range
depends strongly on temperature) before showing a linear
decrease of the torque at higher frequencies (Berg, 2003).
In contrast, when rotating in the clockwise (CW) direc-


## Page 3


3
FIG. 2 Schematic representation of a peritrichous bacterium with three ﬂagellar ﬁlaments showing a bacterial rotary motor
embedded in the cell wall (the stator part of the motor is not shown) (Berg, 2003) and a hook with its junction to a ﬂagellar
ﬁlament (K. Namba, Osaka University). All ﬁgures reproduced with permission.
tion, the motor torque linearly decreases with frequency
(Yuan et al., 2010).
In the range relevant to locomotion, the motor can be
assumed to behave as continuously rotating and produc-
ing a constant torque. The value of this torque is how-
ever still under debate and measurements are at odds
with theoretical predictions. While its stall torque has
been experimentally estimated to be on the order of
4, 600 pN nm (Berry & Berg, 1997), experiments us-
ing beads lead to the conclusion that the motor has
to be on the range 1260 ± 190 pN nm (Reid et al.,
2006).
In contrast, theoretical estimates using a sim-
pliﬁed model for the ﬂuid predict a signiﬁcantly smaller
value of 370 ± 100 pN nm (Darnton et al., 2007).
While the majority of swimming bacteria are powered
by ﬂagellar ﬁlaments rotating in the ﬂuid outside the
cells, two other modes of locomotion in ﬂuids are notable.
Bacteria of the spirochete family have a spiral shape and
undergo whole-body undulations powered also by ﬂag-
ella (Fig. 1e). However, in this case, the ﬁlaments are
constrained in the small space between the cytoplasmic
membrane and outer membrane of the cell body, and it is
the rotation in this tight space which leads to wave-like
whole-body undulations and in turn leads to locomotion
in a ﬂuid (Vig & Wolgemuth, 2012). Swimming with-
out ﬂagella has also been reported for Spiroplasma, a
type of helical bacterium whose body has no cell wall.
In that case, a wavelike motion is induced by contrac-
tion of the cell cytoskeleton leading to the propagation of
shape kinks along the body (Shaevitz et al., 2005; Wada
& Netz, 2007). At least one other bacterium, the marine
Synechococcus, swims in ﬂuids in manner which is as yet
undetermined (Ehlers & Oster, 2012).
To close this biological overview, we mention the other
mode of ﬂuid-based motility termed swarming (Jarrell &
McBride, 2008; Kearns, 2010). A few bacterial families,
when present in media-rich in nutrients, can undergo a
diﬀerentiation to a swarming state, where they become
more elongated, grow more ﬂagella and swim in closely-
packed groups, the physics of which is only beginning to
be unraveled (Copeland & Weibel, 2009; Darnton et al.,
2010).
III. HYDRODYNAMICS OF HELICAL PROPULSION
The most fundamental aspect of bacterial hydrody-
namics is the ability of rotating ﬂagella to produce
propulsive forces (Chwang & Wu, 1971; Higdon, 1979;
Lighthill, 1976). At the origin of this generation of forces
is the non-isotropic nature of hydrodynamic friction in
the Stokesian regime (Brennen & Winet, 1977; Lauga
& Powers, 2009).
At the low Reynolds numbers rele-
vant to swimming bacteria (typically ranging from 10−4
to 10−2), the ﬂows are governed by the incompressible
Stokes equations, and drag forces on rigid bodies scale
linearly with their instantaneous velocities relative to the
background ﬂuid. Because ﬂagellar ﬁlaments are slender
(their aspect ratio is at least 100), their physics can be
intuitively understood by analogy with the motion of a
rod. At a given velocity, a rod experiences a drag from
the ﬂuid about twice as large when translating perpen-
dicular to its long axis as that when moving along it. For
a non-symmetric velocity/rod orientation, the hydrody-
namic drag on the rod is thus not aligned with the di-
rection of its velocity but possesses a nonzero component
perpendicular to it – hence the possibility of drag-based


## Page 4


4
FIG. 3 Hydrodynamics of propulsion by a rotating helical ﬂagellar ﬁlament. A left-handed helix rotates in the CCW direction
(when viewed from the right) as indicated by a purple arrow. The local velocity of two material points on the helix relative
to the background ﬂuid are illustrated with gray arrows. Since the ﬂuid drag is larger (for a given velocity) for motion of
the local helix perpendicular than parallel to the local tangent, the net force density from the ﬂuid includes a component
directed everywhere along the helix axis (black arrows). A net moment opposing the rotation is also generated, resulting in
counter-rotation of the cell.
thrust.
The extension of this idea to case of a helical ﬁlament is
illustrated in Fig. 3. The ﬂagellar ﬁlament is taken here
to be left-handed and undergoes CCW rotation when
viewed from the right looking left (more on this in §V).
The local velocity of two material points on the helix is
illustrated by gray arrows: points in the foreground go
down while points in the background go up. The instan-
taneous drag force density resisting the rotation of the
helix in the ﬂuid is illustrated by black arrows. Because
of the higher resistance from the projection of the local
velocity in the direction perpendicular to the local tan-
gent to the helix, the total drag includes a nonzero com-
ponent along the axis of the helix, which in both cases
points to the left along the helix axis (this is exaggerated
in the ﬁgure for illustration purposes). Consequently, a
rotating helix is subject to a net viscous force aligned
with the helix axis with an orientation which depends on
the handedness of the helix and the direction of rotation.
From a Stokes ﬂow standpoint, the grand resistance
matrix for a helical ﬂagellar ﬁlament, which linearly re-
lates forces and moments to velocities and rotation rates,
includes therefore an oﬀ-diagonal term coupling axial ro-
tation with axial force (Kim & Karrila, 1991; Purcell,
1997).
Because the whole cell is force-free, it has to
swim in order to balance this force. This is the physi-
cal mechanism used by bacteria to self-propel in ﬂuids,
and it will in fact be intuitive to anybody having opened
a bottle of wine with a corkscrew where the rotation of
the screw induces its translation inside the cork. As a
diﬀerence with a corkscrew however, the propulsion of a
helix in a viscous ﬂuid produced by its rotation is very
ineﬃcient, both kinematically (small forward motion per
rotation) and energetically (only a few percent of the to-
tal work done by the helix is transmitted to propulsive
work) (Chattopadhyay et al., 2006; Purcell, 1997; Spag-
nolie & Lauga, 2011). The same hydrodynamic princi-
ples can be exploited to design artiﬁcial helical swimmers
powered by rotating magnetic ﬁelds (Ghosh & Fischer,
2009; Zhang et al., 2010). A famous illustration of helical
locomotion in ﬂuids is provided in G.I. Taylor’s movie on
low Reynolds number ﬂows (Taylor, 1967).
In addition to forces, the rotating ﬁlament in Fig. 3 is
subject to a net hydrodynamic moment resisting the ro-
tation. In order for the bacterium to remain torque-free,
the cell body needs therefore to counter-rotate.
With
ﬂagella typically rotating at ≈100 Hz, this is achieved
by a counter-rotation at smaller frequency ≈10 Hz due
to small rotational mobility of a large cell body (Chwang
& Wu, 1971; Magariyama et al., 1995). Because of this
balance of moments, locomotion powered by helical ﬂag-
ella is not possible in the absence of a cell body, a re-
sult qualitatively diﬀerent from locomotion induced by
planar waving deformation, for which a head is not re-
quired (Lauga & Powers, 2009). The resulting motion of
a bacterium in a ﬂuid consists thus of ﬂagellar ﬁlaments
rotating, the cell body counter-rotating, and the whole
cell moving forward approximately in a straight line, or
in helices of small amplitude when the axis of the ﬁla-
ments is not aligned with that of the cell body (Hyon
et al., 2012; Keller & Rubinow, 1976).
In general the
cell body does not induce additional propulsion, which
is all due to the ﬂagella, unless it is the right shape and
has the right orientation relative to the helical ﬂagellum
(Chwang et al., 1972; Liu et al., 2014b).
The hydrodynamic theories developed to calculate the
distribution of forces on rotating helical ﬂagella are of
three ﬂavors (Brennen & Winet, 1977; Lauga & Powers,
2009). The ﬁrst one, historically, considered the theo-
retical limit of very (exponentially) slender ﬁlaments to
compute forces as a perturbation expansion in the loga-
rithm of the aspect ratio of the ﬂagella. At leading order,
this so-called resistive-force theory predicts that the local
force density at one point along the ﬁlament is propor-
tional to its local velocity relative to the ﬂuid with a co-
eﬃcient of proportionality which depends on the relative


## Page 5


5
orientation of the velocity with respect to the local tan-
gent (Cox, 1970; Gray & Hancock, 1955; Lighthill, 1975).
This is therefore the natural extension of the physical
picture discussed above for rigid rods to deforming ﬁla-
ments. While this is the most widely used approach, and
one which is is able to provide basic physical pictures, it
is often not suﬃciently accurate as the associated relative
errors are only logarithmically small (Chattopadhyay &
Wu, 2009; Johnson & Brokaw, 1979).
More precise is
the second approach, termed slender-body theory, which
consists in distributing appropriate ﬂow singularities of
suitable strengths in order to match the boundary con-
dition on the surface of the ﬁlament at a required, alge-
braically small, precision (Hancock, 1953; Johnson, 1980;
Lighthill, 1976). In that case the equation relating the
distribution of velocity to the distribution of forces is non-
local, because of long-range hydrodynamic interactions,
and thus needs to be inverted numerically. A ﬁnal op-
tion is to use fully three-dimensional computations. The
most common method is an integration of the equations
of Stokes ﬂows using either boundary elements (Liu et al.,
2013; Phan-Thien et al., 1987), regularized ﬂow singular-
ities (Flores et al., 2005; Olson et al., 2013), or immersed
boundaries (Fauci & Dillon, 2006). Mesoscopic particle-
based methods have recently been proposed as an alter-
native approach (Reigh et al., 2012).
IV. FLOWS INDUCED BY BACTERIA
The general ﬂuid dynamics picture of a swimming bac-
terium powered by the rotation of a ﬂagellum is illus-
trated in Fig. 4a. We use purple arrows to indicate the lo-
cal forcing of the swimming cell on the surrounding ﬂuid.
Near the ﬁlament, the induced ﬂow is a combination of
rotation and polar axial pumping directed away from the
cell body. This is illustrated in Fig. 4b-c using slender-
body theory for a helical waveform of diameter 400 nm
and wavelength 2.3 µm (the so-called “normal” wave-
form, see discussion in §V) (Spagnolie & Lauga, 2011).
Looking further away from the cell, because the swim-
ming bacterium is force-free, it pushes on the ﬂuid with
an equal and opposite force to the one generated by
the rotating ﬁlament (Fig. 4a), and thus the leading
order ﬂow in the far-ﬁeld is a force-dipole, or stresslet,
as schematically illustrated in Fig. 4c (Batchelor, 1970;
Ishikawa et al., 2007). The type of associated dipole is
termed a pusher, in contrast with puller dipoles relevant
to cells which swim ﬂagella ﬁrst, for example planktonic
bi-ﬂagellates (Guasto et al., 2012). This ﬂow has been
measured for swimming E. coli using an experimental
tour-de-force (Drescher et al., 2011). The magnitude of
the induced ﬂow is shown in Fig. 4e (in µm/s), while the
theoretical dipolar prediction is shown in Fig. 4f, with a
diﬀerence shown in Fig. 4g. The dipole strength is on the
order of 0.1−1 N µm (Berke et al., 2008; Drescher et al.,
2011) and this dipolar picture is very accurate up to a
few body lengths away, at which point the ﬂow speeds
get overwhelmed by thermal noise.
While the leading-order ﬂow is a stresslet decaying spa-
tially as 1/r2, the velocity ﬁeld around a bacterium also
includes higher-order (decaying as 1/r3) ﬂow singulari-
ties which are important in the near ﬁeld. These include
source-dipoles and force quadrupoles (Chwang & Wu,
1975).
Force-quadrupoles, for example, dominate ve-
locity correlations between swimming bacteria, because
force-dipoles are front-back symmetric (Liao et al., 2007).
An important ﬂow near a swimming bacterium is a rotlet-
dipole. Since the ﬂagellum and the cell body rotate rela-
tive to the ﬂuid in opposite directions (Fig. 4a), they act
on the ﬂuid as two point moments (or rotlets) of equal
and opposite strengths, hence a rotlet-dipole, decaying
spatially as 1/r3, and shown schematically in Fig. 4h (a
rotlet dipole is a particular force quadrupole). A com-
putational illustration of the streamlines associated with
this ﬂow is shown in Fig. 4i (Watari & Larson, 2010).
Note that both the force-dipole and the rotlet-dipole can
be time-dependent, and in some cases induce instanta-
neous ﬂows stronger than their time averages (Watari &
Larson, 2010).
The ﬂows induced by swimming cells have been use-
ful in understanding two problems. First, ﬂows created
by populations of bacteria lead to enhanced transport
in the ﬂuid.
In addition to Brownian motion, passive
tracers (for example nutrient molecules, or much larger
suspended particles) also feel the sum of all hydrody-
namic ﬂows from the population of swimming bacteria,
and in general will thus display an increase in the rate
at which they are transported.
Enhanced diﬀusion by
swimming bacteria was ﬁrst reported experimentally for
ﬂagellated E. coli cells with non-Brownian particles (Wu
& Libchaber, 2000), followed by work on molecular dyes
(Kim & Breuer, 2004). Dilute theories and simulations
based on binary collisions between swimmers (possibly
with a ﬁnite persistence time or ﬁnite run length) and
passive tracers (possibly Brownian) have allowed to pre-
dict diﬀusion constants (Kasyap et al., 2014; Lin et al.,
2011; Mi˜no et al., 2013; Pushkin et al., 2013). In par-
ticular, it was shown that the extra diﬀusivity remains
linear with the concentration of bacteria well beyond
the dilute regime. The eﬀect, while negligible for small
molecules with high Brownian diﬀusivity, can be signiﬁ-
cant for large molecules or non-Brownian tracers.
The second topic where swimming-induced ﬂows are
critical is that of collective swimming.
Suspension of
swimming bacteria display modes of locomotion quali-
tatively diﬀerent from individual cells, with long orien-
tation and velocity correlation lengths, instabilities, and
an intrinsic randomness – a process recently referred to
as bacterial turbulence. Building on the standard theo-
retical description for Brownian suspensions (Doi & Ed-
wards, 1988), the modeling approach consists in describ-
ing the populations of swimming bacteria as continuua
using a probability density function in orientation and
position. Conservation of probability then establishes a
balance between changes in bacteria conﬁgurations and


## Page 6


6
FIG. 4 The ﬂows produced by swimming bacteria. (a) Schematic representation of the forcing induced locally by the bacterium
on the surrounding ﬂuid (purple arrows); (b) Rotational ﬂow near a rotating helical ﬁlament (Spagnolie & Lauga, 2011); (c)
Axial ﬂow along the axis of the helical ﬁlament, directed away from the cell body; (d) In the far-ﬁeld, the cell acts on the ﬂuid
as a force dipole; (e) Measurement of the ﬂow induced by swimming E. coli (Drescher et al., 2011); (f) Theoretical prediction
from force dipole; (g) Diﬀerence between measurement and theoretical prediction; (h) The rotation of the helical ﬁlament and
the counter rotation of the cell body acts on the ﬂuid as a rotlet dipole; (i) Simulation of this rotational ﬂow with streamlines
(Watari & Larson, 2010). All ﬁgures reproduced with permission.
diﬀusion, with changes in both position and orientation
which are brought about by the ﬂows (and their gra-
dients) induced by the swimming bacteria.
While the
current article is focused on single-cell behaviour, we re-
fer to the recent Annual Review on the topic (Koch &
Subramanian, 2011) and book (Spagnolie, 2015), and ref-
erences therein, for a more detailed overview.
V. POLYMORPHISM AND THE EVOLUTIONARY ROLE
OF HYDRODYNAMICS
It is one of nature’s wonders that bacterial ﬂagellar
ﬁlaments only exist in discrete helical shapes called ﬂag-
ellar polymorphs (Calladine, 1978; Hasegawa et al., 1998;
Namba & Vonderviszt, 1997). Each ﬁlament is a polymer
composed of a single protein (ﬂagellin) which assembles
in long protoﬁlaments.
Eleven of these protoﬁlaments
wrap around the circumference of the ﬁlament. Because
ﬂagellin (and thus each protoﬁlament) exists in two dis-
tinct conformation states, an integer number of diﬀerent
conformations is available for the ﬂagellum, of which only
twelve are molecularly and mechanically stable (Calla-
dine, 1978; Srigiriraju & Powers, 2006). These are the
helical “polymorphic” shapes, illustrated in Fig. 5a. Of
these 12 shapes, 2 are straight, and 10 are true helices.
Of these 10 helices, 9 have been observed experimentally,
induced by chemical, mechanical or temperature modi-
ﬁcations (Hotani, 1980, 1982; Leifson, 1960). Of the 10
non-straight shapes, 3 are left-handed – including the
most common one, called “normal,” whose polymorphic
number is #2 – and 7 are right handed – including the
important “semi-coiled,” which is #4, and “curly,” which
is #5.
As an elastic body, the force-extension curve of individ-
ual ﬂagellar ﬁlaments and the transitions between the dif-
ferent polymorphs have been precisely characterized ex-
perimentally using optical tweezers pulling on ﬁlaments
attached to a glass surface (Darnton & Berg, 2007). Fit-
ting the data to a Kirchoﬀelastic rod model with multiple


## Page 7


7
FIG. 5
(a) Illustration of the twelve polymorphic shapes of bacterial ﬂagella, numbered #0 to #11 (Darnton et al., 2007;
Hasegawa et al., 1998); (b) The intrinsic hydrodynamic eﬃciencies of each polymorph for Calladine’s theory (red) and for
experimentally-measured peritrichous (black) and polar (blue) ﬂagellar polymorphs (Purcell, 1997; Spagnolie & Lauga, 2011).
Left (resp. right)-handed helices are denoted with negative (resp. positive) wavelengths and the corresponding waveform with
ﬁlled (resp. empty) symbols, as seen in Fig. 5a. The circles allow diﬀerentiating peritrichous from polar polymorphs. All ﬁgures
reproduced with permission.
minima for curvature and twist allows then to determine
the elastic constants around polymorphic minima. The
bending rigidities so estimated are on the order of few
pN µm2, and the transition forces from one shape to the
next are on the order of a few pN (Darnton & Berg, 2007).
A variety of associated modeling approaches for ﬂagellar
mechanics have been developed to reproduce these ex-
perimental results (Vogel & Stark, 2010; Wada & Netz,
2008).
That ﬂagellar ﬁlaments are elastic means they
might deform under rotation, but during normal swim-
ming conditions this has been shown to be a small eﬀect
(Kim & Powers, 2005). It is however possible that the
moments and forces from the ﬂuid induce buckling of a
rotating ﬁlament, similar to elastic rods buckling under
their own weight. While the threshold rotation rates ap-
pear to be close to biological numbers (Vogel & Stark,
2012), no sign of ﬂagellar buckling has been reported so
far.
The fact that diﬀerent shapes exist is important for
locomotion because, as we see in the next section, when
a bacterium turns, the direction of rotation of one (or
more) bacterial motor is changing, which induces a rapid
polymorphic transformation for the associated ﬁlament,
and in particular a ﬂip of its chirality. This was mod-
eled in a biophysical study for the bacterium Rhodobac-
ter sphaeroides with two diﬀerent polymorphs (Vogel &
Stark, 2013). Similar chirality transformations have been
obtained in the lab using tethered ﬂagella in external
ﬂows (Coombs et al., 2002; Hotani, 1982).
A helical
ﬂagellum held in a uniform stream is subject to a ﬂow-
induced tension as well as hydrodynamic moments, which
are able to induce chirality reversal and cyclic transfor-
mations between right (curly or semi-coiled) and left-
handed (normal) helices.
One aspect of polymorphism where ﬂuid dynamics
plays a fascinating role is the propulsive performance of
each ﬂagellar waveforms. For each waveform, an intrin-
sic propulsive eﬃciency may be deﬁned from the mobility
matrix of the helix, comparing the power used for locomo-
tion to the power expanded by the rotary motor against
the ﬂuid (Purcell, 1997). Physically, eﬃcient helices are
those which maximize the propulsive coupling between
rotation and translation while minimizing the resistance
in both translation and rotation. A near-rod helix, such
as polymorph #9 in Fig. 5a, or one with a small wave-
length, such as polymorph #3, will be very ineﬃcient.
Which one of the diﬀerent shapes is the most eﬃcient?
This is illustrated in Fig. 5b which plots the isovalues of
the intrinsic hydrodynamic eﬃciency as a function of the
helix wavelength and the circumference of the cylinder
on which it is coiled (Spagnolie & Lauga, 2011). Left-
handed (resp. right-handed) helices are denoted with neg-
ative (resp. positive) wavelengths. Superimposed on the
color map are the geometrical measurements from the
actual polymorphs for peritrichous (black symbols) and
polar ﬂagella (blue symbols) together with the theoreti-
cal shapes predicted by molecular theories (red symbols)
(Calladine, 1978). Filled (resp. empty) symbols refer to
the left-handed (resp. right-handed) polymorphs shown
in Fig. 5a. The two circles allow one to distinguish be-
tween peritrichous and polar polymorphs. In all cases,
the most eﬃcient waveform is the left-handed normal
polymorph (#2 in Fig. 5a). This is the waveform dis-
played by bacteria during forward locomotion. Further,


## Page 8


8
FIG. 6 A run-to-tumble-to-run transition for swimming E. coli as a model for the reorientation mechanism of peritrichous
bacteria (Darnton et al., 2007; Turner et al., 2000). During a run all motors turn CCW while in a tumble at least one motor
turns CW which induces polymorphic changes in the associated ﬂagellar ﬁlament, typically from normal to semi-coiled and
then curly (unbundling) before returning to the normal shape at the beginning of a new run (bundling). All ﬁgures reproduced
with permission.
not only is the normal helix the most eﬃcient among all
polymorphs, it is in fact close to being the overall opti-
mal (which is at the intersection of the black circles and
the warm color in the map). In addition, further analy-
sis of the results reveals that the second and third most
eﬃcient waveforms are the right-handed semi-coiled (#4
in Fig. 5a) and curly (#5), both of which are the wave-
forms used by wild-type swimming bacteria to change
directions (see §VI). These results suggest that ﬂuid dy-
namics and mechanical eﬃciencies might have provided
strong physical constraints in the evolution of bacterial
ﬂagella.
VI. HYDRODYNAMICS OF REORIENTATIONS
Swimming is the mechanism which allows bacteria to
sample their environment (Purcell, 1977). Because they
are small, bacteria are not able to sustain directional
swimming for extended periods of time, and as a con-
sequence they always display diﬀusive behavior at long
times. For swimming at speed U for a time τ followed
by a random change of direction, the long-time behav-
ior is diﬀusive, r2 ∼Dt with the diﬀusivity scaling as
D ∼U 2τ, typically much larger than Brownian diﬀusivi-
ties (Berg, 1993). When this diﬀusive dynamics is biased
using sensing from the cells of their chemical environ-
ment, it leads to net drift and chemotaxis (Berg, 2004;
Schnitzer, 1993).
While the value of U is dictated by the hydrodynam-
ics of swimming, what sets the time scale τ and how
do cells manage to reorient? The time scale is set inter-
nally by the sensing apparatus of bacteria, a complex but
well-characterized internal protein network which chem-
ically links the information gathered by receptors on the
cell membrane to the action of the rotary motor (Falke
et al., 1997). In order for the cells to then reorient, three
mechanisms have been discovered, each taking advantage
of diﬀerent physics, and each involving ﬂuid dynamics
(Mitchell, 2002).
The ﬁrst one is termed run-and-stop, where a bac-
terium swims and then stops, simply waiting for thermal
noise to reorient the cell. The time scale is therefore set in
this case by a balance between the magnitude of thermal
noise and the viscous mobility of the whole cell in rota-
tion, leading to reorientation times on the order of sec-
onds. The second mechanism, termed run-and-reverse,
is used by many polar marine bacteria (Stocker & Sey-
mour, 2012). In that case, the rotary motor alternates
between CCW and CW rotations. Kinematic reversibil-
ity for the surrounding ﬂuid would predict that by doing
so the cells should keep retracing their steps. However,
the propulsive forcing from the ﬂuid on the ﬂagellar ﬁla-
ment, which is transmitted to the ﬂexible hook, is able to
induce buckling of the hook which leads to a random re-
orientation of the cell, thereby escaping the reversibility
argument (Son et al., 2013; Xie et al., 2011).
The third, and most-studied, mechanism is called run-
and-tumble, used by peritrichous bacteria such as E. coli,
and whose details were made clear by a pioneering experi-
ment allowing to visualize ﬂagellar ﬁlaments in real time
(Turner et al., 2000) (see illustration in Fig. 6). Criti-


## Page 9


9
cal to the eﬀective locomotion in this case is the ability
of multiple ﬂagellar ﬁlaments to bundle when they all ro-
tate in the same direction, and unbundle otherwise (Mac-
nab, 1977; Magariyama et al., 2001). When a bacterium
runs, all its ﬂagellar ﬁlamenta adopt the normal wave-
form, turn in a CCW fashion (when viewed from behind
the cell looking in), and are gathered in a tight, synchro-
nized helical bundle behind the cell. Based on chemical
clues from its environment, the cell might then initiate a
tumbling event (which is Poisson distributed), for which
at least one motor (but possibly more) switches its direc-
tion rotation to CW, inducing a polymorphic change of
its ﬂagellar ﬁlament from normal to semi-coiled (in most
cases) which at the same time ﬂies out of the bundle,
resulting in a change of orientation for the cell body. As
the motor continues to rotate CW, the ﬂagellum switches
to the curly shape, and then when the motor reverts back
to a CCW rotation, comes back to the normal shape and
returns into the bundle. These short tumbles typically
last τ ∼0.1s while the runs last about one second. Note
that many mutants of E. coli exist, either naturally oc-
curring or genetically induced in the lab, displaying some
variation in geometry or behavior; for example, the mu-
tant HCB-437 does not tumble and is smooth swimming
(Wolfe et al., 1988).
The bundling and unbundling of ﬂagellar ﬁlaments
compose a large-deformation ﬂuid-structure interaction
problem at low Reynolds numbers combined with short-
range ﬂagella-ﬂagella electrostatic repulsion (Lytle et al.,
2002; Weibull, 1950). Due to this complexity, physical
studies of bundling have taken two drastically diﬀerent
approaches. On one hand, investigations have been car-
ried out on very simpliﬁed geometries and setups, either
numerically (Kim & Powers, 2004; Reichert & Stark,
2005) or experimentally at the macroscopic scale (Kim
et al., 2003; Macnab, 1977; Qian et al., 2009), in order
to probe synchronization between driven identical helices
and their bundling. It was found that nonlocal hydro-
dynamic interactions between helices were suﬃcient to
induce attraction, wrapping, and synchronization pro-
vided the helices were of the right combination of chiral-
ity (both left-handed and rotating CCW or their mirror-
image equivalent) but some amount of elastic compliance
was required. Biologically, it was argued that this ﬂexi-
bility could be provided by the hook.
On the other hand, some groups have attempted to
tackle the complexity of the problem using realistic se-
tups of deforming ﬂagellar ﬁlaments from various (of-
ten formidable) computational angles, including the use
of regularized ﬂow singularities (Flores et al., 2005),
the immersed boundary method (Lim & Peskin, 2012),
mesoscale methods (Reigh et al., 2012), boundary ele-
ments (Kanehl & Ishikawa, 2014) and bead-spring mod-
els adapted from polymer physics (Janssen & Graham,
2011; Watari & Larson, 2010).
The numerical results
conﬁrm the physical picture of bundling and unbundling
driven by a combination of ﬂexibility and hydrodynamic
interactions, with a critical dependence on the geometri-
cal details, the relative conﬁguration of the ﬂagella, and
the value of the motor torques driving the rotation.
VII. BACTERIA SWIMMING NEAR SURFACES
Surfaces are known to aﬀect the behavior of bacte-
ria (Harshey, 2003; Vanloosdrecht et al., 1990). One of
the most striking aspect of locomotion near boundaries
is the tendency of swimming bacteria to be attracted
to surfaces, with steady-state concentration showing 10
fold-increases near surfaces (Berke et al., 2008).
This
is illustrated in Fig. 7a for smooth-swimming (i.e. non-
tumbling) E. coli cells. The attraction mechanism was
ﬁrst argued to be purely hydrodynamic in nature (Berke
et al., 2008; Hernandez-Ortiz et al., 2005), easily under-
stood as an image eﬀect. As seen in §IV, the ﬂow pertur-
bation induced by a swimming bacterium is (at leading
order in the far ﬁeld) a pusher force dipole. The hydrody-
namic image system necessary to enforce a no-slip bound-
ary condition on a ﬂat surface includes a force dipole, a
force quadrupole, and a source dipole, all located on the
other side of the surface (purple arrows in Fig. 7b) (Blake,
1971). The net eﬀect of these image singularities on the
original dipole is an hydrodynamic attraction toward the
wall (black arrow).
Intuitively, a pusher dipole draws
ﬂuid in from its side, and therefore pulls itself toward a
surface when swimming parallel to it. Similarly, the hy-
drodynamic moment induced by the image system is able
to rotate pusher dipoles so that their stable orientation
is swimming parallel to the surface (Berke et al., 2008),
leading to kinematic asymmetries for bacteria switching
between pusher and puller modes (Magariyama et al.,
2005).
Experimental measurements of the ﬂow induced by
bacteria showed, however, that this dipolar ﬂow gets
quickly overwhelmed by noise a few cell lengths away,
and thus acts only when the cells are close to the sur-
face, leading to long residence times (Drescher et al.,
2011). For cells which swim toward a surface and get
trapped there, what determines the long-time equilib-
rium distance between swimming cells and surfaces, and
their orientation?
Although simple models all predict
bacteria eventually touching walls and therefore require
short-range repulsion (Dunstan et al., 2012; Spagnolie
& Lauga, 2012), boundary element computations with a
model polar bacterium demonstrated that hydrodynam-
ics alone was able to select a stable orbit with swimming
at a ﬁnite distance (Fig. 7c) (Giacch´e et al., 2010).
A second remarkable feature of bacteria swimming
near surface is a qualitative change in their trajecto-
ries.
Between reorientation events, ﬂagellated bacteria
far from walls swim along straight or wiggly paths. Near
rigid surfaces, their trajectories are observed to become
circular, typically CW when viewed from above the sur-
face in the ﬂuid (Berg & Turner, 1990; Frymier et al.,
1995). This is illustrated in Fig. 7d for an individually-
tracked E coli cell swimming near a glass surface (Vigeant


## Page 10


10
FIG. 7
(a) Attraction of smooth-swimming E. coli cells by two rigid surfaces located at y = 0 and y = 100 µm (symbols) and
ﬁt by a point-dipole model (lines) (Berke et al., 2008); (b) Hydrodynamic images for a pusher force dipole above a ﬂat no-slip
surface (purple arrows) leading to attraction by the surface (black arrow); (c) Computations showing stable swimming at a
ﬁnite distance from a rigid surface for a polar bacterium (distance to wall nondimensionalized by cell size as a function of time
nondimensionalized by ﬂagellar rotational frequency) (Giacch´e et al., 2010); (d) Tracking data for a smooth-swimming E. coli
cell near a glass surface (Vigeant & Ford, 1997); (e) Physical interpretation of wall-induced moment on bacterium with helical
ﬂagellar ﬁlament leading to circular swimming: the rotating ﬂagellum is subject to a surface-induced force to its left (when
viewed from above) and the counter-rotating body by a force in the opposite direction, leading to a moment and therefore
rotation of the cell; (f) Rectiﬁcation of ﬂuorescent swimming E. coli in channels with asymmetric geometrical features (Galajda
et al., 2007). All ﬁgures reproduced with permission.
& Ford, 1997). Early computations for model polar bac-
teria also predicted circular trajectories (Ramia et al.,
1993) while recent experiments showed that the physic-
ochemical nature of the interface plays a critical role se-
lecting the rotation direction (Lemelle et al., 2013; Morse
et al., 2013).
The switch from forward to circular swimming is a
ﬂuid dynamics eﬀect owing to new forces and moments
induced near surfaces (Lauga et al., 2006). This is illus-
trated in Fig. 7e for locomotion of model polar bacterium
above of a rigid wall. A helix rotating parallel to a no-slip
surface is subject to a net force whose direction depends
on the chirality of the helix and its direction of rotation
(to the left in Fig. 7d for a CCW rotation of a left-handed
helix). Similarly, as the cell body is counter-rotating, it
is subject to a hydrodynamic force in the direction of its
rolling motion on the surface (to the right in Fig. 7d)
(Kim & Karrila, 1991).
These two forces are exactly
zero far from the surface and their magnitudes depend
strongly on the distance to the wall (Li et al., 2008).
The net eﬀect of these forces is a wall-induced moment
acting on the cell. Since the cell is torque-free, it needs
to rotate (here, CW when viewed from above), leading
to circular trajectories. Notably, the sign of the surface-
induced forces are reversed if the rigid wall is replaced by
a free surface, leading to circular swimming in the oppo-


## Page 11


11
FIG. 8
(a) Jeﬀery’s orbits for non-ﬂagellated E. coli cells in a microchannel (Kaya & Koser, 2009); (b) Non-motile Bacillus
subtilis cells show a uniform concentration under non-uniform shear (Rusconi et al., 2014); (c) Motile cells initially uniformly
distributed (black line) accumulate under non-uniform shear in the high-shear regions (red line); (d) Motile E. coli cells
swimming in circles near rigid surfaces in the absence of ﬂow (Kaya & Koser, 2012); (e) Upstream swimming of the same cells
under moderate shear; (f) Under strong shear, all cells are advected downstream. All ﬁgures reproduced with permission.
site direction (Di Leonardo et al., 2011), and a possible
co-existence between CW and CCW for cell populations
near complex interfaces (Lemelle et al., 2013; Lopez &
Lauga, 2014; Morse et al., 2013).
The interactions of bacteria with complex geometries
have also lead to fascinating results. Swimming E. coli
cells in rectangular microchannels with three polymeric
walls and one agar surface showed a strong preference to
swim near the agar side of the channels (DiLuzio et al.,
2005), a phenomenon still unexplained. The same bacte-
ria are rectiﬁed by channels with asymmetric geometrical
features (Galajda et al., 2007), which can then be ex-
ploited to passively increase cell concentrations (Fig. 7f).
Similarly, bacteria can be harnessed to perform mechan-
ical work and, for example, rotate asymmetric micro-
gears (Di Leonardo et al., 2010; Sokolov et al., 2010).
In strong conﬁnement, helical ﬂagella continue to induce
propulsion, but the swimming speed decreases for motion
driven at constant torque (Liu et al., 2014a). Related ex-
periments show that the limit of ﬂagella-driven motility
is reached when the cell body has clearance of about less
than 30% of its size, although cells can continue to move
in smaller channels through cell division (M¨annik et al.,
2009).
VIII. BACTERIA IN FLOWS
Similarly to colloidal particles, swimming bacteria re-
spond to external ﬂows by being passively advected and
rotated. In many relevant situations where the cells are
much smaller than any of the ﬂow length scales (e.g. in
marine environments), the ﬂow can be assumed to be
locally linear, and thus a superposition of uniform trans-
lation, pure extension, and pure rotation. In that case,
the dynamics of the (elongated) bacteria is described by
Jeﬀery’s equation which is exact for prolate spheroids in
linear ﬂows (Pedley & Kessler, 1992).
Physically, the
cells move with the mean ﬂow velocity and their rotation
rate is the sum of the vorticity component (which alone
would predict rotation at a constant rate) and the (poten-
tial) extensional component (which alone would predict
steady alignment with the principal axis of extension).
The resulting tumbling trajectories, called Jeﬀery’s or-
bits, are illustrated in Fig. 8a for non ﬂagellated E. coli
cells under shear in a microﬂuidic device (Kaya & Koser,
2009).
In addition to the classical Jeﬀery’s orbits, bacteria are
subject to an additional mechanism which results from
their chiral shapes. The hydrodynamics of a helical ﬂag-
ellum in a simple shear ﬂow leads to a viscous torque be-


## Page 12


12
ing produced on the helix, which reorients it away from
the plane of shear. Combined with motility, this is an
example of rheotaxis where cells responds to shear (here,
purely physically) (Marcos et al., 2012). Beyond the as-
sumption of linear ﬂow, swimming bacteria respond to
non-uniform shears by developing non-uniform orienta-
tion distributions, which, when coupled to motility, lead
to cells accumulating in the high shear regions (Rusconi
et al., 2014). This is illustrated in Fig. 8b-c for Bacil-
lus subtilis in Poiseuille ﬂow. Non-swimming cells have a
uniform distribution (Fig. 8b) whereas motile cells start-
ing uniformly distributed (black line in Fig. 8c) develop
non-uniform distributions and gather in the high-shear
regions (red line Fig. 8c).
One compelling aspect of the response of bacteria to
external ﬂows is the feedback of swimming cells on the
surrounding ﬂuid through the stresses they exert. Due
to their dipolar ﬂows, swimming bacteria exert bulk
stresses on the ﬂuid – hence the term “stresslet” origi-
nally coined by Batchelor in the context of passive sus-
pensions (Batchelor, 1970). A group of swimming bac-
teria subject to an external deformation will thus gener-
ically respond by a state of stress with a rich dynamics.
The most fundamental question relating stresses to de-
formation in the ﬂuid is: what is the eﬀective viscosity of
a suspension of swimming bacteria? Experiments have
been ﬁrst carried out with the peritrichous Bacillus sub-
tilis by estimating the viscosity in two diﬀerent ways,
ﬁrst by looking at the unsteady decay of vortex and then
by measuring directly the torque on a rotating probe in
the cell suspension (Sokolov & Aranson, 2009). The re-
sults showed a strong reduction in the eﬀective viscosity
(up to a factor of seven), while an increase was possi-
ble at larger cell concentrations. A diﬀerent setup was
proposed for E. coli where a suspension was ﬂown in a
microchannel and the eﬀective viscosity estimated using
predictions for the unidirectional ﬂow proﬁle from multi-
phase Newtonian ﬂuid dynamics (Gachelin et al., 2013).
In that case, the eﬀective viscosity showed an initial de-
crease, followed by shear-thickening up to relative vis-
cosities above 1, followed by shear-thinning at high shear
rates. In parallel, theoretical and computational work on
model cells in both shear and extensional ﬂows predicted
the viscosity decrease for pusher cells, together with the
possibility of negative viscosities and normal stress coeﬃ-
cients of sign opposite to the ones for passive suspensions
(Haines et al., 2009; Saintillan, 2010a,b).
Finally, bacteria swimming near boundaries in external
ﬂows also have a propensity to swim upstream and hence
against the ﬂow (Cisneros et al., 2007; Hill et al., 2007).
This is illustrated in Fig. 8d-f where motile E. coli cells
which swim in circles in the absence of ﬂow (Fig. 8d) are
seen to move upstream under moderate shear (Fig. 8e)
and are passively advected downstream at high shear
(Fig. 8f) (Kaya & Koser, 2012).
The physical origin
of this transition to upstream swimming has been pro-
posed to be hydrodynamic, whereby a shear ﬂow of mod-
erate strength produces a torque on a downward-facing
cell which reorients it so that its stable equilibrium is
to point upstream and thus swim against the ﬂow (Hill
et al., 2007; Kaya & Koser, 2012).
IX. LOCOMOTION IN COMPLEX FLUIDS
Bacteria who inhabit soils and higher organisms rou-
tinely have to progress through complex environments
with microstructures whose characteristic length scales
might be similar to that of the cell.
Some bacte-
ria also have to endure chemically- and mechanically-
heterogeneous environments. For example, Helicobacter
pylori, which survives in the acidic environment of the
stomach, creates an enzyme which locally increases pH
and can induce rheological changes to the mucus pro-
tecting the epithelium surface of the stomach, changing
it from a gel to a viscous ﬂuid in which it is able to swim
(Bansil et al., 2013). In many instances, the surround-
ing ﬂuids might not be totally ﬂowing but instead pos-
sess their own relaxation dynamics, which might occur
on time scales comparable to the intrinsic time scales of
the locomotion. For example, during bioﬁlm formation,
bacteria produce an extracellular polymeric matrix for
which they control the mechanical properties through wa-
ter content (Costerton et al., 1995; Wilking et al., 2011)
(Fig. 9a). A number of studies have attempted to quan-
tify the impact of such complex ﬂuids on the swimming
kinematics and energetics of bacteria.
Early studies were concerned with perhaps the simplest
question possible: How is bacterial locomotion modiﬁed
by a change in the viscosity of the surrounding (New-
tonian) ﬂuid? Flagellated bacteria display a systematic
two-phase response, where an increase in viscosity is seen
to ﬁrst lead to a small increase in the swimming speed
followed by a sharp decrease at large viscosities (Green-
berg & Canale-Parola, 1977; Schneider & Doetsch, 1974;
Shoesmith, 1960).
The decrease has been rationalized
by assuming that the rotary motor is working at con-
stant power output (Keller, 1974), an assumption we
now know is erroneous since it is the motor torque which
is constant (see §II). In stark contrast with ﬂagellated
bacteria, spirochetes show a systematic enhancement of
their swimming speed with an increase of the viscosity of
the ﬂuid (Kaiser & Doetsch, 1975). In a related study,
the viscosity required to immobilize bacteria was mea-
sured to be larger, by orders of magnitude, for spirochetes
compared to ﬂagellated bacteria (Greenberg & Canale-
Parola, 1977).
How can the diﬀerence between ﬂagellated bacteria
and spirochetes be rationalized? One argument brought
forward focused on the details of the microstructure of
the ﬂuid, arguing that all increases in viscosity are not
created equal (Berg & Turner, 1979). Increases in viscos-
ity are induced by dissolving polymers, but the nature of
the polymer chains structure may be critical.
Experi-
ments showing large increases in swimming speeds used
solution of long unbranched chain polymers (e.g., methyl-


## Page 13


13
FIG. 9
(a) Bioﬁlm on the stainless steel surface of a bioreactor (Centers for Disease Control and Prevention); (b) Waves in the
director ﬁeld created by rotating ﬂagella of the peritrichous B. subtilis in a liquid crystal (Zhou et al., 2014); (c-d) Magnitude of
the polymer stresses in the cross section of a ﬂagellum rotating in a Oldroyd-B ﬂuid (nondimensionalized by the viscosity times
the ﬁlament rotation rate) from computations (the white dashed line indicates the path followed by the ﬂagellum centerline)
(Spagnolie et al., 2013). Top: De = 0.3; bottom: De = 1.5. All ﬁgures reproduced with permission.
cellulose) which are expected to form a network against
which the cells are eﬀectively able to push. In contrast,
solutions of branched polymers are more homogeneous,
and should lead to a decrease of the swimming speed
since, for a constant-torque motor rotating in a viscous
ﬂuid, the product of the viscosity by the rotational fre-
quency needs to remain constant. The idea that the pres-
ence of the microstructure itself in the solvent is crit-
ical in explaining the change in swimming speeds was
further modeled mathematically, with a similar physical
picture (Leshansky, 2009; Magariyama & Kudo, 2002).
Recent experiments further shed light on the interplay
between the viscosity of the ﬂuid and the torque applied
by the rotary motor (Martinez et al., 2014). If the ﬂuid is
anisotropic (for example a liquid crystal), a strong cou-
pling can develop between the director ﬁeld and the bac-
teria, enabling constrained locomotion and fascinating
novel ﬂow features with truly long-ranged interactions
(Fig. 9b) (Zhou et al., 2014).
Recent work has focused on viscoelastic ﬂuids with
the primary motivation to understand the locomotion of
bacteria, and higher organisms, in mucus (Lauga, 2014).
Such ﬂuids have the added complexity of having ﬁnite re-
laxation times, λ, and for ﬂagella rotating with frequency
ω a dimensionless Deborah number, De = λω, needs to be
considered. Small-amplitude theory on ﬂagellar propul-
sion predicted that the relaxation in the ﬂuid would al-
ways leads to slower swimming (Fu et al., 2007; Lauga,
2007). Experiments with macroscopic helices driven in
rotation and undergoing force-free translation conﬁrmed
the small-amplitude theoretical results but showed that
helices with larger amplitudes could experience a mod-
erate increase in translational speed for order one Deb-
orah numbers (Liu et al., 2011). Detailed numerics on
the same setup argued that the increase was due to the
rotating ﬂagellum revisiting its viscoelastic wake, as il-
lustrated in Fig. 9c-d for De = 0.3 (top) and De = 1.5
(bottom) (Spagnolie et al., 2013).
X. SUMMARY POINTS
1. Low-Reynolds-number hydrodynamics is at the
heart of the fundamental physics of bacteria swim-
ming, ﬁrst and foremost by the generation of
propulsive forces. It might have also played a role
in the evolution of the bacterial ﬂagellum result-
ing in optimal polymorphic shapes used for forward
motion.
2. At the level of a single-cell, ﬂuid dynamic forces
are exploited by peritrichous bacteria to induce fast
bundling and unbundling of their multiple ﬂagella,
resulting in eﬃcient reorientation mechanisms.
3. The ﬂows created by swimming bacteria aﬀect
the interactions with their environment and with
other cells leading to enhanced nutrient transport


## Page 14


14
and collective locomotion. Similarly, complex mi-
crostructures or external ﬂows can have signiﬁcant
inﬂuence on the trajectories, concentrations, and
orientations of swimming bacteria.
4. Although surrounding ﬂuids play important roles
in the life of bacteria, hydrodynamic forces on ﬂag-
ellar ﬁlaments and cell bodies often have to be bal-
anced with bending and twisting elasticity, short-
range electrostatic interactions, and are subject to
both biochemical and thermal noise. Fluid dynam-
ics is therefore only one of the complex physical
processes at play.
XI. FUTURE ISSUES
1. Why is the value of the experimentally-measured
torque applied by the rotary motor so diﬀerent
from that from hydrodynamic predictions (Darn-
ton et al., 2007)? What are the other mechanical
forces at play?
2. Why does the ﬂagellar hook of peritrichous bac-
teria not buckle, as it does for polar bacteria un-
der seemingly similar propulsive conditions (Son
et al., 2013)? Why is the ﬂagellar hook so precisely
tuned in size and rigidity that ﬂagellar bundling is
no longer possible if small changes are made to it
(Brown et al., 2012)?
3. How exactly can a tight bundle of multiple ﬂag-
ella open up and close repeatedly without jamming
under the uncoordinated action of a few motors
(Macnab, 1977)? How much of this process is truly
driven by hydrodynamic interactions vs. other pas-
sive mechanisms?
4. Can we derive predictive whole-cell models able
to reproduce the full run-and-tumble statistics of
swimming bacteria based solely on our understand-
ing on the behavior of rotary motors (Turner et al.,
2000)?
Acknowledgements
I thank Tom Montenegro-Johnson for his help with the
ﬁgures. Discussions with Howard Berg and Ray Gold-
stein are gratefully acknowledged. This work was funded
in part by the European Union (through a Marie-Curie
CIG Grant) and by the Isaac Newton Trust (Cambridge).
References
Allen RD, Baumann P. 1971.
Structure and arrangement
of ﬂagella in species of the genus Beneckea and Photobac-
terium ﬁscheri. J. Bacteriol. 107:295–302
Bansil R, Celli JP, Hardcastle JM, Turner BS. 2013. The inﬂu-
ence of mucus microstructure and rheology in Helicobacter
pylori infection. Front. Immun. 4:310
Batchelor GK. 1970.
The stress system in a suspension of
force-free particles. J. Fluid Mech. 41:545–570
Berg HC. 1993.
Random Walks in Biology.
New Jersey:
Princeton University Press
Berg HC. 2003. The rotary motor of bacterial ﬂagella. Annu.
Rev. Biochem. 72:19–54
Berg HC. 2004. E. coli in Motion. New York, NY: Springer-
Verlag
Berg HC, Anderson RA. 1973.
Bacteria swim by rotating
their ﬂagellar ﬁlaments. Nature 245:380–382
Berg HC, Turner L. 1979. Movement of microorganisms in
viscous environments. Nature 278:349–351
Berg HC, Turner L. 1990. Chemotaxis of bacteria in glass
capillary arrays – Escherichia coli, motility, microchannel
plate, and light scattering. Biophys. J. 58:919–930
Berke AP, Turner L, Berg HC, Lauga E. 2008. Hydrodynamic
attraction of swimming microorganisms by surfaces. Phys.
Rev. Lett. 101:038102
Berry RM, Berg HC. 1997. Absence of a barrier to backwards
rotation of the bacterial ﬂagellar motor demonstrated with
optical tweezers. Proc. Natl. Acad. Soc., USA 94:14433–
14437
Blair DF. 1995. How bacteria sense and swim. Annu. Rev.
Microbiol. 49:489–520
Blake JR. 1971. A note on the image system for a stokeslet
in a no-slip boundary. Proc. Camb. Phil. Soc. 70:303–310
Bray D. 2000.
Cell Movements.
New York, NY: Garland
Publishing
Brennen C, Winet H. 1977. Fluid mechanics of propulsion by
cilia and ﬂagella. Annu. Rev. Fluid Mech. 9:339–398
Brown MT, Steel BC, Silvestrin C, Wilkinson DA, Delalez
NJ, et al. 2012. Flagellar hook ﬂexibility is essential for
bundle formation in swimming Escherichia coli cells.
J.
Bacter. 194:3495–3501
Calladine CR. 1978. Change of waveform in bacterial ﬂagella
: the role of mechanics at the molecular level. J. Mol. Biol.
118:457–479
Chattopadhyay S, Moldovan R, Yeung C, Wu XL. 2006.
Swimming eﬃciency of bacterium Escherichia coli. Proc.
Natl. Acad. Sci. USA 103:13712–13717
Chattopadhyay S, Wu X. 2009. The eﬀect of long-range hy-
drodynamic interaction on the swimming of a single bac-
terium. Biophys. J. 96:2023–2028
Chen X, Berg HC. 2000. Torque-speed relationship of the ﬂag-
ellar rotary motor of Escherichia coli. Biophys. J. 78:1036–
1041
Chwang AT, Wu TY. 1971. Helical movement of microorgan-
isms. Proc. Roy. Soc. Lond. B 178:327–346
Chwang AT, Wu TY. 1975. Hydromechanics of low-Reynolds-
number ﬂow. Part 2. Singularity method for Stokes ﬂows.
J. Fluid Mech. 67:787–815
Chwang AT, Wu TY, Winet H. 1972. Locomotion of spirilla.
Biophys. J. 12:1549
Cisneros LH, Cortez R, Dombrowski C, Goldstein RE, Kessler
JO. 2007. Fluid dynamics of self-propelled microorganisms,
from individuals to concentrated populations. Exp. Fluids
43:737–753
Coombs D, Huber G, Kessler JO, Goldstein RE. 2002. Pe-
riodic chirality transformations propagating on bacterial
ﬂagella. Phys. Rev. Lett. 89:118102–1–118102–4
Copeland MF, Weibel DB. 2009. Bacterial swarming: a model


## Page 15


15
system for studying dynamic self-assembly.
Soft Matt.
5:1174–1187
Costerton JW, Lewandowski Z, Caldwell DE, Korber DR,
Lappinscott HM. 1995.
Microbial bioﬁlms.
Annu. Rev.
Microbiol. 49:711–745
Cox RG. 1970. The motion of long slender bodies in a viscous
ﬂuid. Part 1. General theory. J. Fluid Mech. 44:791–810
Darnton NC, Berg HC. 2007. Force-extension measurements
on bacterial ﬂagella: Triggering polymorphic transforma-
tions. Biophys. J. 92:2230–2236
Darnton NC, Turner L, Rojevsky S, Berg HC. 2007. On torque
and tumbling in swimming Escherichia coli. J. Bacteriol.
189:1756–1764
Darnton NC, Turner L, Rojevsky S, Berg HC. 2010. Dynamics
of bacterial swarming. Biophys. J. 98:2082–2090
Di Leonardo R, Angelani L, DellArciprete D, Ruocco G, Iebba
V, et al. 2010. Bacterial ratchet motors. Proc. Natl. Acad.
Sci. U.S.A. 107:9541–9545
Di Leonardo R, Dell’Arciprete D, Angelani L, Iebba V. 2011.
Swimming with an image. Phys. Rev. Lett. 106:038101
DiLuzio WR, Turner L, Mayer M, Garstecki P, Weibel DB,
et al. 2005. Escherichia coli swim on the right-hand side.
Nature 435:1271–1274
Doi M, Edwards SF. 1988. The Theory of Polymer Dynamics.
Oxford, U.K.: Oxford University Press
Drescher K, Dunkel J, Cisneros LH, Ganguly S, Goldstein
RE. 2011. Fluid dynamics and noise in bacterial cell-cell
and cell-surface scattering. Proc. Natl. Acad. Sci. U.S.A.
108:10940–10945
Dunstan J, Mi˜no G, Clement E, Soto R. 2012. A two-sphere
model for bacteria swimming near solid surfaces.
Phys.
Fluids 24:011901
Ehlers K, Oster G. 2012. On the mysterious propulsion of
Synechococcus. PLOS One 7:e36081
Falke JJ, Bass RB, Butler SL, Chervitz SA, Danielson MA.
1997. The two-component signaling pathway of bacterial
chemotaxis: A molecular view of signal transduction by
receptors, kinases, and adaptation enzymes. Annu. Rev.
Cell Dev. Biol. 13:457
Fauci LJ, Dillon R. 2006. Bioﬂuidmechanics of reproduction.
Annu. Rev. Fluid Mech. 38:371–394
Flores H, Lobaton E, Mendez-Diez S, Tlupova S, Cortez R.
2005. A study of bacterial ﬂagellar bundling. Bull. Math.
Biol. 67:137–168
Frymier PD, Ford RM, Berg HC, Cummings PT. 1995. Three-
dimensional tracking of motile bacteria near a solid planar
surface. Proc. Natl. Acad. Sci. USA 92:6195–6199
Fu HC, Powers TR, Wolgemuth HC. 2007. Theory of swim-
ming ﬁlaments in viscoelastic media.
Phys. Rev. Lett.
99:258101–258105
Fujii M, Shibata S, Aizawa SI. 2008. Polar, peritrichous, and
lateral ﬂagella belong to three distinguishable ﬂagellar fam-
ilies. J. Mol. Biol. 379:273–283
Gachelin J, Mi˜no G, Berthet H, Lindner A, Rousselet A,
Cl´ement E. 2013.
Non-newtonian viscosity of echerichia
coli suspensions. Phys. Rev. Lett. 110:268103
Gaﬀney EA, Gadelha H, Smith DJ, Blake JR, Kirkman-
Brown JC. 2011. Mammalian sperm motility: Observation
and theory. Annu. Rev. Fluid Mech. 43:501–528
Galajda P, Keymer JE, Chaikin P, Austin RH. 2007. A wall
of funnels concentrates swimming bacteria. J. Bacteriol.
189:8704–8707
Ghosh A, Fischer P. 2009. Controlled propulsion of artiﬁcial
magnetic nanostructured propellers.
Nano Lett. 9:2243–
2245
Giacch´e D, Ishikawa T, Yamaguchi T. 2010. Hydrodynamic
entrapment of bacteria swimming near a solid surface.
Phys. Rev. E 82:056309
Goldstein RE. 2015. Green algae as model organisms for bi-
ological ﬂuid dynamics. Annu. Rev. Fluid Mech. 47:34375
Goldstein SF, Buttle KF, Charon NW. 1996. Structural anal-
ysis of the Leptospiraceae and Borrelia burgdorferi by high-
voltage electron microscopy. J. Bacteriol. 178:6539–6545
Gray J, Hancock GJ. 1955.
The propulsion of Sea-urchin
spermatozoa. J. Exp. Biol. 32:802–814
Greenberg EP, Canale-Parola E. 1977. Motility of ﬂagellated
bacteria in viscous environments. J. Bacteriol. 132:356–358
Guasto JS, Rusconi R, Stocker R. 2012.
Fluid mechanics
of planktonic microorganisms.
Annu. Rev. Fluid Mech.
44:373400
Haines BM, Sokolov A, Aranson IS, Berlyand L, Karpeev DA.
2009. Three-dimensional model for the eﬀective viscosity
of bacterial suspensions. Phys. Rev. E 80:041922
Hancock GJ. 1953. The self-propulsion of microscopic organ-
isms through liquids. Proc. Roy. Soc. Lond. A 217:96–121
Harshey RM. 2003. Bacterial motility on a surface: Many
ways to a common goal. Annu. Rev. Microbiol. 57:249–273
Hasegawa K, Yamashita I, Namba K. 1998.
Quasi- and
nonequivalence in the structure of bacterial ﬂagellar ﬁla-
ment. Biophys. J. 74:569–575
Hernandez-Ortiz JP, Stoltz CG, Graham MD. 2005. Trans-
port and collective dynamics in suspensions of conﬁned
swimming particles. Phys. Rev. Lett. 95:204501
Higdon JJL. 1979. Hydrodynamics of ﬂagellar propulsion –
Helical waves. J. Fluid Mech. 94:331–351
Hill J, Kalkanci O, McMurry JL, Koser H. 2007. Hydrody-
namic surface interactions enable Escherichia coli to seek
eﬃcient routes to swim upstream. Phys. Rev. Lett. 98:1–4
Hotani H. 1980. Micro-video study of moving bacterial ﬂagel-
lar ﬁlaments. II. Polymorphic transition in alcohol. Biosyst.
12:325–330
Hotani H. 1982. Micro-video study of moving bacterial ﬂag-
ellar ﬁlaments III. Cyclic transformation induced by me-
chanical force. J. Mol. Biol. 156:791
Hyon Y, Marcos, Powers TR, Stocker R, Fu HC. 2012. The
wiggling trajectories of bacteria. J. Fluid Mech. 705:58–76
ImhoﬀJF, Tr¨uper HG. 1977.
Ectothiorhodospira halochlo-
ris sp. nov., a new extremely halophilic phototrophic bac-
terium containing bacteriochlorophyll b∗. Arch. Microbiol.
114:115–121
Ishikawa T, Sekiya G, Imai Y, Yamaguchi T. 2007. Hydro-
dynamic interaction between two swimming bacteria. Bio-
phys. J. 93:2217–2225
Janssen PJA, Graham MD. 2011. Coexistence of tight and
loose bundled states in a model of bacterial ﬂagellar dy-
namics. Phys. Rev. E 84
Jarrell KF, McBride MJ. 2008. The surprisingly diverse ways
that prokaryotes move. Nature Rev. Microbiol. 6:466–476
Johnson RE. 1980.
An improved slender body theory for
Stokes ﬂow. J. Fluid Mech. 99:411–431
Johnson RE, Brokaw CJ. 1979.
Flagellar hydrodynamics.
a comparison between resistive-force theory and slender-
body theory. Biophys. J. 25:113
Kaiser GE, Doetsch RN. 1975. Enhanced translational motion
of Leptospira in viscous environments. Nature 255:656–657
Kanehl P, Ishikawa T. 2014. Fluid mechanics of swimming
bacteria with multiple ﬂagella. Phys. Rev. E 89:042704
Kasyap TV, Koch DL, Wu M. 2014. Hydrodynamic tracer


## Page 16


16
diﬀusion in suspensions of swimming bacteria. Phys. Fluids
26:081901
Kaya T, Koser H. 2009. Characterization of hydrodynamic
surface interactions of Escherichia coli cell bodies in shear
ﬂow. Phys. Rev. Lett. 103:138103
Kaya T, Koser H. 2012.
Direct upstream motility in Es-
cherichia coli. Biophys. J. 102:1514–1523
Kearns DB. 2010. A ﬁeld guide to bacterial swarming motility.
Nature Rev. Microbiol. 8:634–644
Keller JB. 1974. Eﬀect of viscosity on swimming velocity of
bacteria. Proc. Natl. Acad. Sci. USA 71:3253–3254
Keller JB, Rubinow SI. 1976. Swimming of ﬂagellated mi-
croorganisms. Biophys. J. 16:151–170
Kim M, Bird JC, Parys AJV, Breuer KS, Powers TR. 2003.
A macroscopic scale model of bacterial ﬂagellar bundling.
Proc. Natl. Acad. Sci. USA 100:15481–15485
Kim M, Powers TR. 2004.
Hydrodynamic interactions be-
tween rotating helices. Phys. Rev. E 69:061910
Kim MJ, Breuer KS. 2004. Enhanced diﬀusion due to motile
bacteria. Phys. Fluids 16:L78–L81
Kim MJ, Powers TR. 2005.
Deformation of a helical ﬁla-
ment by ﬂow and electric or magnetic ﬁelds. Phys. Rev. E
71:021914–1–10
Kim S, Karrila JS. 1991.
Microhydrodynamics: Principles
and Selected Applications.
Boston, MA: Butterworth-
Heinemann
Koch DL, Subramanian G. 2011. Collective hydrodynamics
of swimming microorganisms: Living ﬂuids. Annu. Rev.
Fluid Mech. 43:637 – 659
Lauga E. 2007. Propulsion in a viscoelastic ﬂuid. Phys. Fluids
19:083104
Lauga E. 2014. Locomotion in complex ﬂuids: Integral theo-
rems. Phys. Fluids 26:081902
Lauga E, DiLuzio WR, Whitesides GM, Stone HA. 2006.
Swimming in circles: Motion of bacteria near solid bound-
aries. Biophys. J. 90:400–412
Lauga E, Powers TR. 2009. The hydrodynamics of swimming
microorganisms. Rep. Prog. Phys. 72:096601
Leifson E. 1960. Atlas of Bacterial Flagellation. New York
and London: Academic Press
Lemelle L, Palierne JF, Chatre E, Vaillant C, Place C. 2013.
Curvature reversal of the circular motion of swimming bac-
teria probes for slip at solid/liquid interfaces. Soft Matter
9:9759–9762
Leshansky
AM.
2009.
Enhanced
low-Reynolds-number
propulsion in heterogeneous viscous environments. Phys.
Rev. E 80:051911
Li G, Tam LK, Tang JX. 2008. Ampliﬁed eﬀect of brown-
ian motion in bacterial near-surface swimming. Proc. Natl.
Acad. Sci. USA 105:18355–18359
Liao Q, Subramanian G, DeLisa MP, Koch DL, Wu MM.
2007.
Pair velocity correlations among swimming Es-
cherichia coli bacteria are determined by force-quadrupole
hydrodynamic interactions. Phys. Fluids 19:061701
Lighthill J. 1975. Mathematical Bioﬂuiddynamics. Philadel-
phia: SIAM
Lighthill J. 1976. Flagellar hydrodynamics—The John von
Neumann lecture, 1975. SIAM Rev. 18:161–230
Lim S, Peskin CS. 2012. Fluid-mechanical interaction of ﬂex-
ible bacterial ﬂagella by the immersed boundary method.
Phys. Rev. E 85:036307
Lin Z, Thiﬀeault JL, Childress S. 2011. Stirring by squirmers.
J. Fluid Mech. 669:167–177
Liu B, Breuer KS, Powers TR. 2013. Helical swimming in
stokes ﬂow using a novel boundary-element method. Phys.
Fluids 25:061902
Liu B, Breuer KS, Powers TR. 2014a. Propulsion by a helical
ﬂagellum in a capillary tube. Phys. Fluids 26:011701
Liu B, Gulino M, Morse M, Tang JX, Powers TR, Breuer KS.
2014b. Helical motion of the cell body enhances caulobac-
ter crescentus motility.
Proc. Natl. Acad. Sci. U.S.A.
111:11252–11256
Liu B, Powers TR, Breuer KS. 2011. Force-free swimming of
a model helical ﬂagellum in viscoelastic ﬂuids. Proc. Natl.
Acad. Sci. USA 108:19516–19520
Lopez D, Lauga E. 2014. Dynamics of swimming bacteria at
complex interfaces. Phys. Fluids 26:071902
Lytle DA, Johnson CH, Rice EW. 2002. A systematic compar-
ison of the electrokinetic properties of environmentally im-
portant microorganisms in water. Colloid. Surf. B 24:91–
101
Macnab RM. 1977.
Bacterial ﬂagella rotating in bundles:
A study in helical geometry. Proc. Natl. Acad. Sci. USA
74:221
Madigan MT, Martinko JM, Stahl D, Clark DP. 2010. Brock
Biology of Microorganisms (13th Edition). San Francisco,
CA: Benjamin Cummings
Magariyama Y, Ichiba M, Nakata K, Baba K, Ohtani T, et al.
2005. Diﬀerence in bacterial motion between forward and
backward swimming caused by the wall eﬀect. Biophys. J.
88:3648–3658
Magariyama Y, Kudo S. 2002. A mathematical explanation
of an increase in bacterial swimming speed with viscosity
in linear-polymer solutions. Biophys. J. 83:733–739
Magariyama Y, Sugiyama S, Kudo S. 2001. Bacterial swim-
ming speed and rotation rate of bundled ﬂagella.
Fems
Microbiol. Lett. 199:125–129
Magariyama Y, Sugiyama S, Muramoto K, Kawagishi I, Imae
Y, Kudo S. 1995. Simultaneous measurement of bacterial
ﬂagellar rotation rate and swimming speed.
Biophys. J.
69:2154–2162
M¨annik J, Driessen R, Galajda P, Keymer JE, Dekker C.
2009.
Bacterial growth and motility in sub-micron con-
strictions. Proc. Natl. Acad. Sci. USA 106:14861–14866
Marcos, Fu HC, Powers TR, Stocker R. 2012. Bacterial rheo-
taxis. Proc. Natl. Acad. Sci. U.S.A. 109:4780–4785
Martinez VA, Schwarz-Linek J, Reufer M, Wilson LG, Mo-
rozov AN, Poon WCK. 2014. Flagellated bacterial motil-
ity in polymer solutions.
Proc. Natl. Acad. Sci. U.S.A.
111:17771–17776
Mi˜no GL, Dunstan J, Rousselet A, Cl´ement E, Soto R. 2013.
Induced diﬀusion of tracers in a bacterial suspension: The-
ory and experiments. J. Fluid Mech. 729:423–444
Mitchell JG. 2002. The energetics and scaling of search strate-
gies in bacteria. Am. Natur. 160:727–740
Morse M, Huang A, Li G, Maxey MR, Tang JX. 2013. Molec-
ular adsorption steers bacterial swimming at the air/water
interface. Biophys. J. 105:21 – 28
Namba K, Vonderviszt F. 1997.
Molecular architecture of
bacterial ﬂagellum. Q. Rev. Biophys. 30:1–65
Olson SD, Lim S, Cortez R. 2013. Modeling the dynamics
of an elastic rod with intrinsic curvature and twist using a
regularized Stokes formulation. J. Comp. Phys. 238:169–
187
Ottemann KM, Miller JF. 1997.
Roles for motility in
bacterial-host interactions. Mol. Microbiol. 24:1109–1117
Pedley TJ, Kessler JO. 1992.
Hydrodynamic phenomena
in suspensions of swimming microorganisms. Annu. Rev.


## Page 17


17
Fluid Mech. 24:313–358
Phan-Thien N, Tran-Cong T, Ramia M. 1987. A boundary-
element analysis of ﬂagellar propulsion.
J. Fluid Mech.
184:533–549
Purcell EM. 1977. Life at low Reynolds number. Am. J. Phys.
45:3–11
Purcell EM. 1997. The eﬃciency of propulsion by a rotating
ﬂagellum. Proc. Natl. Acad. Soc., USA 94:1130711311
Pushkin DO, Shum H, Yeomans JM. 2013. Fluid transport
by individual microswimmers. J. Fluid Mech. 726:5–25
Qian B, Jiang H, Gagnon DA, Breuer KS, Powers TR. 2009.
Minimal model for synchronization induced by hydrody-
namic interactions. Phys. Rev. E 80:061919
Ramia M, Tullock DL, Phan-Thien N. 1993. The role of hy-
drodynamic interaction in the locomotion of microorgan-
isms. Biophys. J. 65:755–778
Reichert M, Stark H. 2005. Synchronization of rotating helices
by hydrodynamic interactions. Eur. Phys. J. E 17:493–500
Reid SW, Leake MC, Chandler JH, Lo CJ, Armitage JP,
Berry RM. 2006.
The maximum number of torque-
generating units in the ﬂagellar motor of Escherichia coli
is at least 11. Proc. Natl. Acad. Sci. USA 103:8066–8071
Reigh SY, Winkler RG, Gompper G. 2012. Synchronization
and bundling of anchored bacterial ﬂagella.
Soft Matt.
8:4363–4372
Rusconi R, Guasto JS, Stocker R. 2014. Bacterial transport
suppressed by ﬂuid shear. Nature Phys. 10:212–217
Saintillan D. 2010a. Extensional rheology of active suspen-
sions. Phys. Rev. E 81:056307
Saintillan D. 2010b. The dilute rheology of swimming suspen-
sions: A simple kinetic model. J. Exp. Mech. 50:1275
Schneider W, Doetsch RN. 1974. Eﬀect of viscosity on bac-
terial motility. J. Bacteriol. 117:696–701
Schnitzer MJ. 1993. Theory of continuum random walks and
application to chemotaxis. Phys. Rev. E 48:2553
Shaevitz JW, Lee JY, Fletcher DA. 2005. Spiroplasma swim
by a processive change in body helicity. Cell 122:941
Shoesmith JG. 1960. The measurement of bacterial motility.
J. Gen. Microbiol. 22:528–535
Silverman M, Simon M. 1974.
Flagellar rotation and the
mechanism of bacterial motility. Nature 249:73–74
Sokolov A, Apodaca MM, Grzybowski BA, Aranson IS. 2010.
Swimming bacteria power microscopic gears. Proc. Natl.
Acad. Sci. USA 107:969–974
Sokolov A, Aranson IS. 2009. Reduction of viscosity in sus-
pension of swimming bacteria. Phys. Rev. Lett. 103:148101
Son K, Guasto JS, Stocker R. 2013. Bacteria can exploit a
ﬂagellar buckling instability to change direction.
Nature
Phys. 9:494–498
Spagnolie SE, ed. 2015. Complex Fluids in Biological Systems.
Biological and Medical Physics, Biomedical Engineering.
Springer, New York
Spagnolie SE, Lauga E. 2011. Comparative hydrodynamics
of bacterial polymorphism. Phys. Rev. Lett. 106:058103
Spagnolie SE, Lauga E. 2012.
Hydrodynamics of self-
propulsion near a boundary: predictions and accuracy of
far-ﬁeld approximations. J. Fluid Mech. 700:105–147
Spagnolie SE, Liu B, Powers TR. 2013. Locomotion of helical
bodies in viscoelastic ﬂuids: Enhanced swimming at large
helical amplitudes. Phys. Rev. Lett. 111:068101
Srigiriraju SV, Powers TR. 2006. Model for polymorphic tran-
sitions in bacterial ﬂagella. Phys. Rev. E 73:011902
Stocker R, Seymour JR. 2012. Ecology and physics of bac-
terial chemotaxis in the ocean. Microbiol. Mol. Biol. Rev.
76:792–812
Taylor GI. 1967.
Low Reynolds number ﬂows.
US Natl.
Comm. Fluid Mech. Films video
Turner L, Ryu WS, Berg HC. 2000.
Real-time imaging of
ﬂuorescent ﬂagellar ﬁlaments. J. Bacteriol. 182:2793–2801
Vanloosdrecht MCM, Lyklema J, Norde W, Zehnder AJB.
1990. Inﬂuence of interfaces on microbial activity. Micro-
biol. Rev. 54:75–87
Vig DK, Wolgemuth CW. 2012. Swimming dynamics of the
lyme disease spirochete. Phys. Rev. Lett. 109:218104
Vigeant MAS, Ford RM. 1997. Interactions between motile
Escherichia coli and glass in media with various ionic
strengths, as observed with a three-dimensional tracking
microscope. Appl. Environ. Microbiol. 63:3474–3479
Vogel R, Stark H. 2010. Force-extension curves of bacterial
ﬂagella. Eur. Phys. J. E 33:259–271
Vogel R, Stark H. 2012. Motor-driven bacterial ﬂagella and
buckling instabilities. Eur. Phys. J. E 35:1–15
Vogel R, Stark H. 2013. Rotation-induced polymorphic tran-
sitions in bacterial ﬂagella. Phys. Rev. Lett. 110:158104
Vogel S. 1996. Life in Moving Fluids. Princeton, NJ: Prince-
ton University Press
Wada H, Netz RR. 2007. Model for self-propulsive helical ﬁl-
aments: Kink-pair propagation. Phys. Rev. Lett. 99:108102
Wada H, Netz RR. 2008. Discrete elastic model for stretching-
induced ﬂagellar polymorphs. EPL 82
Watari N, Larson RG. 2010. The hydrodynamics of a run-and-
tumble bacterium propelled by polymorphic helical ﬂagella.
Biophys. J. 98:12–17
Weibull C. 1950.
Electrophoretic and titrimetric measure-
ments on bacterial ﬂagella. Acta. Chim. Scandinav. 4:260–
267
Wilking JN, Angelini TE, Seminara A, Brenner MP, Weitz
DA. 2011. Bioﬁlms as complex ﬂuids. MRS Bull. 36:385–
391
Wolfe AJ, Conley MP, Berg HC. 1988. Acetyladenylate plays
a role in controlling the direction of ﬂagellar rotation. Proc.
Natl. Acad. Sci. U.S.A. 85:6711–6715
Wu XL, Libchaber A. 2000. Particle diﬀusion in a quasi-two-
dimensional bacterial bath. Phys. Rev. Lett. 84:3017–3020
Xie L, Altindal T, Chattopadhyay S, Wu XL. 2011. Bacte-
rial ﬂagellum as a propeller and as a rudder for eﬃcient
chemotaxis. Proc. Natl. Acad. Sci. USA 108:2246–2251
Yuan J, Fahrner KA, Turner L, Berg HC. 2010. Asymmetry in
the clockwise and counterclockwise rotation of the bacterial
ﬂagellar motor. Proc. Natl. Acad. Sci. U.S.A. 107:12846–
12849
Zhang L, Peyer KE, Nelson BJ. 2010. Artiﬁcial bacterial ﬂag-
ella for micromanipulation. Lab Chip 10:2203–2215
Zhou S, Sokolov S, Lavrentovich OD, Aranson IS. 2014. Living
liquid crystals.
Proc. Natl. Acad. Sci. U.S.A. 111:1265–
1270

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1509_02184v1_bacterial_hydrodynamics
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2015/1509_02184V1_BACTERIAL_HYDRODYNAMICS.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

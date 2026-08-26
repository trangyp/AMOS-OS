---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1805.06531v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1805.06531v2_Continuum_models_of_collective_cell_migration

> Source: 1805.06531v2_Continuum_models_of_collective_cell_migration.pdf

> Pages: 26

---


## Page 1


Continuum models of collective cell migration
Shiladitya Banerjee and M. Cristina Marchetti
Abstract Collective cell migration plays a central role in tissue development, mor-
phogenesis, wound repair and cancer progression. With the growing realization that
physical forces mediate cell motility in development and physiology, a key biologi-
cal question is how cells integrate molecular activities for force generation on multi-
cellular scales. In this review we discuss recent advances in modeling collective cell
migration using quantitative tools and approaches rooted in soft matter physics. We
focus on theoretical models of cell aggregates as continuous active media, where the
feedback between mechanical forces and regulatory biochemistry gives rise to rich
collective dynamical behavior. This class of models provides a powerful predictive
framework for the physiological dynamics that underlies many developmental pro-
cesses, where cells need to collectively migrate like a viscous ﬂuid to reach a target
region, and then stiffen to support mechanical stresses and maintain tissue cohesion.
Keywords: Continuum modelling, cell migration, cell mechanics, tissue mechanics,
active matter
1 Introduction
In many physiological and developmental contexts, groups of cells coordinate their
behavior to organize in coherent structures or migrate collectively [1]. Many ex-
perimental studies have established that these multicellular processes are regulated
by the cross-talk between cell-cell adhesions, cell interaction with the extracellular
matrix, and myosin-based contractility of the cell cortex [2]. Importantly, faithful
Shiladitya Banerjee
University College London, London, UK, e-mail: shiladitya.banerjee@ucl.ac.uk
M. Cristina Marchetti
University of California Santa Barbara, Santa Barbara, CA, USA, e-mail: cmarchetti@ucsb.
edu
1
arXiv:1805.06531v2  [physics.bio-ph]  5 Dec 2018


## Page 2


2
Shiladitya Banerjee and M. Cristina Marchetti
execution of multicellular processes requires both biochemical signaling and me-
chanical force transmission.
A well-studied multicellular process is wound healing, where epithelial cells
march in unison to ﬁll in a gap in the tissue [3, 4]. Although the cells at the front of
the advancing monolayer often show large, spread-out lamellipodia and an almost
mesenchymal phenotype, long-range collective migration is not simply achieved
via the pulling action of such leader cells on a sheet of inert followers [5]. In fact,
traction forces transmitted to the extracellular matrix are found to remain signiﬁcant
well behind the leading edge of the tissue, indicating that cells in the bulk participate
in force generation and transmission. This observation, together with the presence
of spread-out cells with large cryptic lamellipodia throughout the monolayer [6],
indicates that, although leader cells at the sheet edge provide guidance for migra-
tion, they do not play a unique role in force generation. Instead, a new paradigm
has emerged where collective migration is associated with long-range forces ex-
tending throughout the tissue, with waves of propagating mechanical stress that are
sustained by biochemical signaling at the molecular scale [5, 7]. These waves of
stress and cellular deformation provide a mechanism for information transmission,
much like sound in air. Such mechanical waves have been shown to drive periodic
cycles of effective stiffening and ﬂuidiﬁcation in expanding cell monolayers [7] and
coherent vortical or standing motions in conﬁned ones [8, 9].
Multicellularity and collective migration is intimately related to the materials
properties of tissues - viscoelastic materials with both ﬂuid and solid-like behavior.
In morphogenesis, for instance, cells must sort and ﬂow like a liquid to reach the
right location, but then stiffen and support mechanical stresses once the tissue has
achieved the desired structure [10]. Recent experiments have suggested that dense
tissues may be in a glassy or jammed state, where local cell rearrangements are rare
and energetically costly. A relatively small change in tissue mechanical parameters
may trigger a change from an elastic response to viscous ﬂuid-like behavior, where
individual cells are highly motile and rearrange continuously [11, 12]. Indeed living
tissues appear to have well-deﬁned mechanical properties, some familiar from con-
ventional matter, such as elastic moduli [13] and surface tension [14], others unique
to living systems, such as homeostatic pressure, proposed theoretically as a factor
controlling tumor growth [15].
Just like intermolecular forces yield the emergence of materials properties in
nonliving matter, cell-cell interactions, mediated by cadherins, play a crucial role
in controlling the macroscopic properties of groups of cells and tissues [16, 17].
The collective mechanics of living matter, however, is more complex than that of
inert materials as individual cell activity competes with cell-cell interactions in con-
trolling the large scale behavior of cell assemblies. In addition, physical models
of collective cell behavior must also incorporate interactions of cells with the ex-
tracellular matrix. In other words, the coupling of of cells to their surroundings is
affected by intracellular contractility and cell-cell interactions, which in turn can be
actively regulated by the environment, in a complex feedback loop unique to living
matter. Finally, unlike inert materials where phase changes are controlled by ex-
ternally tuning parameters such as temperature and density, living matter can tune


## Page 3


Continuum models of collective cell migration
3
itself between states with different macroscopic properties through the regulation
of molecular scale and genetic processes that drive motility, division, death and
phenotypical changes. A quantitative understanding of the relative importance of
mechanical and biochemical mechanisms in controlling the collective tissue proper-
ties is beginning to emerge through developments in molecular biology, microscopy,
super-resolution imaging and force measurement techniques [18]. These advances
provide an ideal platform for constructing quantitative physical models that account
for the role of active cellular processes in controlling collective mechanics of motile
and deformable multicellular structures.
Theoretical modeling of multicellular processes can be divided broadly into two
classes. The ﬁrst encompasses discrete mesoscale models that incorporate some
minimal features of individual cells, such as contractility and motility, and then
examine how cell-cell interactions and coupling to the environment determine ma-
terials properties at the tissue scale. This class includes models of cells as active
particles endowed with persistent motility [19, 20], as well as models that have been
used extensively in developmental biology, such as Vertex [21, 22], Voronoi [23, 24]
and Cellular Potts models [25] that are designed to capture the behavior of conﬂu-
ent tissues, where there are no gaps nor overlaps between cells. Vertex and Voronoi
models describe cells as irregular polygons tiling the plane and are deﬁned by an
energy functional that tends to adjust the area and perimeter of each cell to target
values [26]. Recent modiﬁcations have also endowed these mesoscopic models with
cell motility [24, 27, 28] and active contractility [29]. Vertex models have been em-
ployed successfully to quantify how intercellular forces control shape at both the
cell and tissue scale under the assumption of force balance at every vertex of the
cellular network [26]. An active version of the Voronoi model was recently shown
to exhibit a liquid-solid transition of conﬂuent epithelia tuned by motility and cell
shape, which in turns encodes information about the interplay between cortex con-
tractility and cell-cell adhesion [24]. An intriguing prediction of this work is that
individual cell shape, that can be inferred directly from cell imaging segmentation,
provides a measure of tissue rigidity [30].
The second class of theoretical work encompasses continuum models, such as
phase ﬁeld [31] and active gel models [32], where a cell sheet is described as a
ﬂuid or an elastic continuum, with couplings to internal degrees of freedom that
account for active processes, such as contractiity and cellular polarization. Con-
tinuum models have been shown to account for the heterogeneous spatial distri-
bution of cellular stresses inferred from Traction Force Microscopy [33] in both
expanding [5, 7, 34, 35] and conﬁned monolayers [36], and even at the level of
individual cells [37]. They also capture the mechanical waves observed in these
systems [7, 38]. This review does not aim to be comprehensive, and will focus on
models of tissue as active continuous media, with an emphasis on models that de-
scribe tissue as active elastic continua. This class of mechanochemical models has
had a number of successes in capturing the tissue scale behavior in adherent [39],
conﬁned [36] and expanding epithelia [38].
Both the mesoscale and continuum approaches do not attempt to faithfully in-
corporate intracellular processes, but rather aim at characterizing quantitatively the


## Page 4


4
Shiladitya Banerjee and M. Cristina Marchetti
modes of organization and the materials properties of cell collectives in terms of
a few macroscopic parameters, such as cell density and shape, cell-cell adhesive-
ness, contractility, polarization and division/death rates. Each of these quantities
may describe the combined effect of a number of molecular processes and signaling
pathways. This approach, inspired from condensed matter physics [40], aims at pro-
viding experimentalists with testable predictions that may allow to correlate classes
of signaling pathways to tissue scale organization.
The review is organized as follows. In Sect. 2 we describe a dynamical model
of cell collectives as active viscoelastic media, coupled to the dynamics of active
intracellular processes such as actomyosin contractility and cell polarization. An
important aspect of the model is a dynamic feedback between mechanical stresses
and regulatory biochemistry which gives rise to rich collective behavior. In Sect. 3
we discuss applications of this class of continuum models to describing force trans-
mission in epithelial monolayers, waves in expanding cell sheets, collective cell
migration in conﬁnement and during epithelial gap closure. We then compare the
quantitative predictions of viscoelastic solid models with ﬂuid models of tissues in
Sect. 4, describing their equivalence as well as highlighting the key differences. We
conclude with a critical discussion of the continuum model limitations and highlight
open theoretical questions in understanding the collective behavior of multicellular
assemblies (Sect. 5).
2 Cells as active continuous media
We begin by considering the mechanics of a monolayer of epithelial cells, migrating
on a soft elastic matrix (Fig. 1a-b), with an average height h much thinner than
in-plane cell dimensions [34, 41, 42]. In mechanical equilibrium, the condition of
local force-balance translates to ∂βΣαβ = 0, where Σ is the three-dimensional stress
tensor of the monolayer, with greek indices taking values x,y and z. In-plane force
balance is given by
∂jΣij +∂zΣiz = 0 ,
(1)
with i, j denoting in-plane coordinates. For a thin cell monolayer we average the
cellular force-balance equation over the cell thickness h. We assume that the top
surface of the cell is stress free, Σiz(r⊥,z = h) = 0, whereas at the cell-substrate
interface, z = 0, the cells experience lateral traction stresses given by Σiz(r⊥,z =
0) = Ti(r⊥). A representative traction stress map for a monolayer expanding in free
space is reproduced in Fig. 1b, which shows appreciable traction stress penentration
throughout bulk of the tissue. The thickness-averaged force balance equation then
reads,
h∂jσij = Ti ,
(2)
where σi j(r⊥) =
R h
0 (dz/h)Σi j(r⊥,z) is the in-plane monolayer stress. The force-
balance diagram is illustrated in Fig. 1c. It is worthwhile to mention that the as-
sumption of in-plane traction forces is a good approximation for fully spread cells


## Page 5


Continuum models of collective cell migration
5
Fig. 1 Forces driving collective cell motion. (a-b) Radial component of traction stress (a) and
phase contrast images of an expanding MDCK cell monolayer, reproduced from Ref. [5] (scale
bar=200 µm). (b) Schematic of the physical forces acting on the cell monolayer [36]. Tractions
exerted by the monolayer on the substrate (ECM) point inward (red arrows) at the monolayer edge
and balance the forces due to viscous friction, ζv (black arrows), and polarized motility, fp (green
arrows). The tractions are locally balanced by the divergence of the monolayer stress, T = h∇.σ .
making almost zero contact angle with the substrate. During the early stages of
spreading and migration, cells can exert appreciable out-of-plane traction forces via
rotation of focal adhesions [43]. The quantity Ti is a stress in three dimensions, i.e., a
force per unit area. It describes the in-plane traction force per unit area that the cell
exerts on the substrate. The force-balance equation is supplemented by the mass
balance equation, such that cell density, ρ(r⊥,t), obeys the following conservation
equation,
∂tρ +∇.(ρv) = χρ ,
(3)
where v is the velocity ﬁeld, and χ is the rate of variation in cell density due to cell
division or death [44]. In the following, we assume χ = 0. See refs [45, 46, 47] for
continuum models for tissues with explicit consideration of cell division and death.
2.1 Constitutive model for intercellular stress
The in-plane cellular stress, σ , can be decomposed as the sum of intercellular stress,
σ c, and active stress, σ a, originating from active intracellular processes (Fig. 2). The
form of the constitutive relation for the intercellular stress has been highly debated,
given the complex rheology of cellular aggregates [48]. On the timescale of seconds
to minutes, living tissues behave elastically, recovering their original shape after


## Page 6


6
Shiladitya Banerjee and M. Cristina Marchetti
Fig. 2 Constitutive elements
of the continuum model
for collective migration.
The viscoelastic and active
elements exert stresses in par-
allel. A local gradient in stress
is balanced by the traction
exerted by the cell on the
substrate, which is modelled
by a viscous element.
K
⌘
σa
T
cell monolayer
substrate
a transient application of force [49, 50]. On longer timescales (tens of minutes to
hours), cellular aggregates exhibit ﬂuid-like behavior that can arise from cell-cell
adhesion turnover, cellular rearrangements, cell division or death [46, 51, 52]. It is
therefore commonly assumed that intercellular stresses obey Maxwell visco-elastic
constitutive law [53], described by solid-like response at short time scales and ﬂuid-
like behavior at longer time scales.
Experimental and computational studies by many groups have shown, however,
that stresses imposed on tissues cannot be completely dissipated, and cells sup-
port some part of applied tension [54, 55, 56]. In fact rheological experiments have
demonstrated that stress relaxation in epithelial monolayers can be described by a
spring connected in parallel to a viscous dashpot [55, 57]. Others have shown that
mechanical stress buildup in monolayers occurs in unison with strain accumula-
tion [7], which can be described by an elastic constitutive law [58, 39]. Therefore,
to describe the dynamic mechanical behavior of cohesive cellular aggregates we
assume linear Kelvin-Voigt rheology (Fig. 2) [45]
σ c = (1+τ∂t)

K∇.u 1+ µ
 ∇u+(∇u)T −∇.u 1

,
(4)
where 1 is the identity matrix, u is the cellular displacement ﬁeld, K is the com-
pressional elastic modulus, µ is the shear modulus, and τ is the viscoelastic re-
laxation timescale. The assumption of isotropic elasticity is consistent with stress
measurement in cell monolayers using monolayer stress microscopy [36, 58]. For
simplicity, we have ignored nonlinear contributions to the constitutive relation in
Eq. (20), which may be essential for stabilizing the dynamical response of living
tissues to large mechanical strain [59, 60, 61]. In Sect. 4, we discuss the quantita-
tive comparisons between elastic and ﬂuid models of tissue rheology. We note that
recent experimental studies show evidence for more complex rheological proper-
ties, including combinations of active elastic and dissipative response at moderate
stretching [57], as well as superelastic behavior at extreme stretching [62].


## Page 7


Continuum models of collective cell migration
7
Fig. 3 Coordination of cell
motion and polarization.
Cells align their motion along
the polarity vector, p, and
move with a velocity v.
Neighboring cells tend to
align their polarities, and
poalrity differences generate
a net torque on neighboring
cells. Cells also exert a dipole-
like contractile stress on the
substrate due to actomyosin
activity. Figure adapted from
Ref. [53].
~p
~p
~p
2.2 Active intracellular stress
The active intracellular stress stems from contractile forces generated in the acto-
myosin cytoskeleton in the cell cortex [63], and from actin treadmiling driven by
the assembly and diassembly actin ﬁlaments. Active contractile stresses depend on
the concentration of actomyosin units, c(t), with the form
σ a = σ0(c)1+σan(c)pp ,
(5)
where we have introduced the cell polarization or polarity vector, p, which is an
internal state variable that controls the local direction of cell motion (Fig. 3). σ0(c)
and σan(c) are the isotropic and anisotropic components of the active stress due to
actomyosin contractility. Note that additional active stress terms of the form ∝∇p
are allowed by symmetry in this phenomenological model, leading to renormaliza-
tion of the elastic modulus to leading order [34]. Several models for the dependence
of σ0 on c have been proposed, including linear [64], logarithmic [38] and saturating
behaviour [65]. Recent in vitro measurements show that contractile strains accumu-
late cooperatively as a function of myosin density [66], indicating that σ0 could take
the general Hill functional form:
σ0(c) = σ0
cn
cn∗+cn ,
(6)
where the constant n > 1 indicates cooperative behavior beyond a critical concen-
tration c∗, and σ0 > 0 is the magnitude of the contractile stress.
Finally, the force balance equation, Eq. 2, requires a constitutive equation for
the net traction stress transmitted to the substrate. For a layer of motile cells this is
chosen of the form (Fig. 1c) [38]
T = ζv−fp ,
(7)


## Page 8


8
Shiladitya Banerjee and M. Cristina Marchetti
where v = ∂tu, f is the magnitude of the propulsion force, and ζ is an effective fric-
tion coefﬁcient that depends on the rate of focal adhesion turnover [67]. This form
for traction in Eq. (7) results in local misalignment of traction stress and cell veloc-
ity, consistent with experimental ﬁndings [36, 68]. The propulsion force, fp, drives
cell crawling, and depends on the concentration of branched actin in the lamellipo-
dia of migrating cells. For simplicity, we assume that there is a steady concentration
of polymerized actin that pushes the cell forward. Dynamic models for the competi-
tion between branched and contractile actin have been proposed [69, 70]. A detailed
description of such molecular processes lies beyond the scope of this review, but can
be easily incorporated within this framework. The resultant force balance equation
is then given by (Fig. 1c,2),
h∇.(σ c +σ a) = ζv−fp+fext ,
(8)
where fext is the external force (density) applied to the system. In the absence of
external forces or stresses applied at the boundary, the net traction force, when in-
tegrated over the entire cell-substrate interface must vanish. This implies a funda-
mental constraint on the relatioship between cell polarity and velocity:
Z
v.dA = f
ζ
Z
p.dA .
(9)
In the following, we will additionally need to prescribe the dynamics of cell polar-
ization and actomyosin concentration, which regulate active cell motility and the
production of contractile stresses.
2.3 Mechanochemical coupling of cell motion and contractility
The dynamics of cell polarization is commonly modeled following the physics of
active liquid crystals [40], a phenomenological approach that requires further justi-
ﬁcation and scrutiny. The cell polarization vector evolves in time according to,
∂tp+β(p.∇)p+v.∇v−1
2(∇×v)×v = a(1−|p|2)p+κ∇2p+w∇c ,
(10)
where the advective coupling β arises from ATP driven processes such as tread-
miling [71], the velocity dependent advective terms are borrowed from the nematic
liquid crystal literature [72], and the Franck elastic constants are both assumed to
be equal to κ. Here, a controls the rate of relaxation to a homogeneously polarized
cell monolayer, and κ controls the strength of nearest-neighbor alignment of the
polarization ﬁeld (Fig. 3), akin to velocity alignment in the Viscek model of collec-
tive motion [73]. The active mechanochemical coupling w > 0 represents the rate of
alignment of cell polarization with gradients in the actomyosin concentration ﬁeld.
As a result, local cell motion is guided toward regions of high contractility.


## Page 9


Continuum models of collective cell migration
9
Fig. 4 Mechanochemical
feedback mechanisms. Feed-
back between cell stretch,
actomyosin contractility and
polarized cell motility in
the mechanochemical model
for collective motion. Local
stretch upregulates assembly
of actomyosin, which gen-
erates contractile forces that
exert compressive stress. Po-
larized motility, in turn, pulls
and stretches the cells.
Contractility
σa
Mechanical 
stretch
Motility
~p
r.u > 0
The concentration of contractile actomyosin is described by a reaction-advection-
diffusion equation,
∂tc+∇.(cv) = D∇2c−1
τc
(c−c0)+αc0
∇.u
1+|∇.u|/s0
,
(11)
where D is a diffusion constant, τc is the timescale of relaxation to steady-state,
and α > 0 is the rate of accumulation of contractile actomyosin due to local tis-
sue stretching [38]. The positive constant s0 sets the upper limit of strain magnitude
above which the production rate of c saturates [60]. This mechanochemical feedback
(Fig. 4) is consistent with experimental data for single cells [74] and cell monolay-
ers [7, 75], where a local extensile strain reinforces contractility via assembly of
actomyosin [76]. Turnover of contractile elements at a rate τ−1
c
ﬂuidizes the mono-
layer, inducing an effective viscosity of magnitude ηeff = (K −σ0 +Dζ/h)τc [38].
Aside from the negative feedback between mechanical strain and actomyosin as-
sembly, positive feedback occurs between mechanical strain and advective ﬂuxes
into regions of high contractility. Advective transport can compete with diffusion to
generate steady state patterns of contractility [77].
It is instructive to note that for small changes in c around c0, Eq. (11) describes a
dynamics of active contractile stress that is similar to a Maxwell constitutive model
for intercellular stress proposed by Lee and Wolgemuth [53]. Here, in addition,
we consider an elastic contribution to the active stress, described by the term α.
The feedback between mechanical strain and contractility yields an effective elastic
modulus Keff ≈K+ατc(σ0+ fw/2ah) [38], larger than the modulus K of the mono-
layer in the absence of contractility. This prediction is consistent with experimental
measurements that cell monolayers treated with blebbistatin (myosin-II inhibitor)
have a much reduced elastic modulus [36].


## Page 10


10
Shiladitya Banerjee and M. Cristina Marchetti
3 Forces and motion driving collective cell behavior
The coupled system of Eqs. (8)-(11) describes the spatiotemporal dynamics of cell
monolayers, subject to appropriate boundary and initial conditions for cellular dis-
placement (u), cell polarity ﬁeld (p) and actomyosin concentration (c). We now
discuss the quantitative predictions of this model for collective mechanics and mi-
gration in various biological contexts. In particular we will focus on four scenar-
ios where continuum model predictions have been tested and validated against ex-
perimental data: Force transmission in epithelial monolayers (Sect. 3.1), Collec-
tive motility in expanding monolayers (Sect. 3.2), Cell migration under conﬁnement
(Sect. 3.3), and Epithelial movement during gap closure (Sect. 3.4).
3.1 Force transmission in epithelial monolayers
Epithelial cell monolayers adherent to soft elastic substrates provide a model system
for mechanical force generation during tissue growth, migration and wound heal-
ing [78, 2]. In the experimental assays of interest [79, 5], the substrates are usually
coated with extracellular matrix proteins (e.g. ﬁbronectin, collagen) that allow cells
to spread fully to a thin ﬁlm and thereby establish contractile tension. To describe
the experimentally observed traction force localization in fully spread adherent cell
sheets [79, 5, 39], we consider the steady-state limit of Eq. (8)-(11), which was
originally studied in refs [80, 34, 41, 39]. In this limit, v ≡0, and concentration of
active contractile units is slaved to material strain, c ≈c0(1+ατc∇.u). This results
in renormalization of the compressional modulus to linear order. Similarly from
Eq. (10) it follows that p ≈−
  wατcc0
κ

u.
To linear order, the force balance equation for the contracting cell layer, with
internal stress σ = σ c +σ01, is given by,
h∇.σ = Yu ,
(12)
where, Y = k + fwατcc0
κ
is the effective substrate rigidity, resulting from the sum
of substrate stiffness k, and the contribution from cell polarization. The intercellular
stress, σ c, follows a constitutive relation identical to that of a linear elastic solid with
a renormalized compressional modulus Keff. Equation (12) can be exactly solved for
circularly shaped monolayers [80, 39], subject to the stress-free boundary condition:
σ .ˆn = 0, where ˆn is the unit normal to the boundary of the monolayer. This boundary
condition needs to be appropriately modiﬁed if the colony edge is under tension due
to peripheral actin structures [81].
The resulting solution to Eq. (12) describes cell traction forces and displace-
ments localized to the edge of the monolayer over a a length scale ℓp =
p
Keffh/Y,
deﬁned as the stress penetration depth. Furthermore, internal stresses in the mono-
layer, σ , accumulate at the center of the monolayer, in agreement with experimental
data (Fig. 5a-b) [5, 58]. The model can be solved numerically for monolayers of


## Page 11


Continuum models of collective cell migration
11
any geometry, and it predicts that traction stresses localize to regions of high cur-
vature [82]. This was later conﬁrmed experimentally by micropatterning adhesion
geometries of non-uniform curvatures [37]. The model has been used to recapitulate
a number of experimental observations [34, 41, 82, 39], including substrate rigidity
dependence of traction stresses [83] and cell spread area [84], traction stress depen-
dence on cell geometry [37], correlation between cell shape and mechanical stress
anisotropy [85], as well as the optimal substrate rigidity for maximal cell polariza-
tion [86].
A particularly interesting application of this model is in understanding the rela-
tionship between traction force magnitude and the geometric size of cohesive cell
colonies adherent to soft matrices [39]. One can deﬁne the magnitude of the to-
tal traction force transmitted to substrate as F =
R |T.dA|, where the integral is
taken over the entire spread area of the colony, A. The model predicts that for large
cell colonies of linear size R ≫ℓp, F = 2πhσ0R. This linear scaling of force with
colony size (Fig. 6) implies that actomyosin contractility, σ0, induces an effective
surface tension in solid tissues, which appear to wet the substrate underneath akin to
ﬂuid droplets. The effective surface tension was estimated from experiments on ker-
atinocyte colonies to be 8×10−4 N/m [39], which is of the same order of magnitude
as the apparent surface tension estimated in adherent endothelial cells [87], Dic-
tyostelium cells [88], mm-scale migrating epithelial sheets [5], and cellularised ag-
gregates [50]. Recent work has shown that for highly motile and ﬂuid cell colonies,
traction forces localize to the colony interior rather than at the edge [89].
Fig. 5 Stress transmission in epithelial monolayers. (a) Internal stress, σxx, in an expanding
MDCK monolayer obtained by integrating cellular traction force. Adapted from Ref. [5]. Buildup
of σxx signiﬁes that tension in the actin cytoskeleton and cell-cell junctions increases towards the
centre of the monolayer. (b) Time evolution of the internal stress σ(x,t) in the monolayer predicted
by the continuum model of epithelium [38].


## Page 12


12
Shiladitya Banerjee and M. Cristina Marchetti
  20
40
60
80
100
200
20
40
60
80
100
200
400
600
800
1,000
2,000
1 cell
2 cells
3 cells
4 cells
5 cells
6 cells
> 6 cells
surface tension
contractility model
a
b
Fig. 6 Active surface tension in cohesive epithelial colonies. (a) Total force transmitted to the
substrate by keratinocyte colonies, F, as a function of the equivalent radius, R, of the colonies [39].
The dashed line represents the linear scaling expected for surface tension, F ∝R. The solid line
shows a ﬁt of the data to the continuum model in Eq. (12). (b) Distribution of strain energy, w, for
a representative single cell, pair of cells, and colony of 12 cells. Scale bar=50 µm.
3.2 Collective motility in expanding monolayers
Migratory behaviors of epithelial cells are commonly studied experimentally using
the wound healing assay. In the classical scratch-assay [90], a strip of cells is re-
moved from the monolayer to observe collective migration of cells marching to ﬁll
the tissue gap. This experimental model system, however, is unsuited for controlled
study of migration due to ill-deﬁned borders and debris created by the physical
wound. The last decade has seen signiﬁcant improvement in the wound healing as-
say, where cells are grown to conﬂuence within a removable barrier, which is then
lifted to allow cell migration into free space [91, 5]. These studies, in combination
with Traction Force Microscopy have shed light into the forces and motion driving
collective cell migration. In particular, it has been observed that cell velocity ﬁelds at
the leading edge of the epithelium exhibit complex swirling patterns [92] and often
form multicellular migration ﬁngers [91]. Measurement of mechanical stresses at
cell-cell and cell-substrate interfaces have given rise to models of tug-of-war [5], a
consequence of mechanical force-balance, where local traction stresses in the mono-
layers are integrated into long-ranged gradients of intercellular tensions (Fig. 5a-b).
Stress inference at cell-cell junctions have led to the suggestion of plithotaxis [58],
where cell migration is guided towards the direction of maximum normal stress and
minimum shear stress.
A particularly interesting case is that of collective migration waves, observed in
mm-sized monolayers expanding into free space [7] (Fig. 7a). These mechanical
waves, crucially dependent on myosin contractility and cell-cell adhesions, propa-


## Page 13


Continuum models of collective cell migration
13
Fig. 7 Mechanical waves during epithelial expansion. (a) Traction stress map of an expand-
ing MDCK monolayer, adapted from Ref. [7]. (b) Kymograph of strain rate in expanding MDCK
monolayers [7], showing generation and propagation of X-shaped mechanical waves. (c) Propagat-
ing stress waves predicted by the continuum model, Eq. (8)-(11) [38]. (d) Schematic illustrating the
mechanics of migration waves, adapted from refs. [93, 7]. Cells at the colony center (purple) are ini-
tially stretched by pulling forces generated by leader cells. Stretched cells recover their equilibrium
shape via cytoskeletal ﬂuidization (blue star), which is then reinforced to trigger shape elongation
again. These shape oscillations mediate periodic stiffening and ﬂuidization of cells (green curve).
gate at a slow speed (on the order of µm/hr) from the colony edge to the center
and back (Fig. 7b). The waves are mediated by shape changes at the scale of single
cells. Pulling forces from crawling cells at the leading edge of the colony stretch
interior cells, which periodically recover their shape via a proposed model of cy-
toskeletal ﬂuidization (Fig. 7d) [93]. Interestingly, this wave-like progression of cell
movement naturally arises in the active elastic media models, Eq. (8)-(11), due to a
feedback between contractility and mechanical strain [38].
To understand the origin of wave propagation and estimate the wave frequency,
it is useful to examine the mechanics of an expanding one-dimensional monolayer
with a polarization ﬁeld pointing outward from the colony center. We consider the
linear ﬂuctuations in the strain ﬁeld δε and the concentration ﬁeld δc, about the qui-
escent homogeneous state u = 0, c = c0. Using Eqs. (8) and (11), one can eliminate
δc to obtain the linearized dynamics of strain ﬂuctuations:
τcζ∂2
t δε +ζ∂tδε = h(Keff +ηeff∂t −τcKD∂2
x )∂2
x δε .
(13)
The above equation shows that the coupling of strain to concentration ﬁeld yields an
effective mass density (inertia), τcζ, and viscoelasticity characterized by an effective
elastic modulus, Keff, and an effective viscosity ηeff, which leads to oscillations with


## Page 14


14
Shiladitya Banerjee and M. Cristina Marchetti
a characteristic frequency ω = q
p
h(Keff +τcq2KD)/(τcζ), with q the wavevector.
Full solutions of the nonlinear equations [38] yields X-shaped propagating stress
waves akin to experimental data (Fig. 7c) [7]. These contraction waves are chrar-
acterized by sustained oscillations in tissue rigidity - a slow period of stiffening
followed by rapid ﬂuidization (Fig. 7d). When the coupling of polarization to strain
and contractility is turned on, complex spatiotemporal patterns emerge including
traveling stress pulses and chaotic polarization waves [60, 38].
3.3 Cell migration under conﬁnement
In many biological contexts, including morphogenesis, tissue polarity establish-
ment, and acini formation, cells often migrate collectively in conﬁned environments.
Experiments have shown the emergence of coherent angular motion of cells in vivo
(Fig. 8a), including cells in yolk syncytial layer of zebraﬁsh embryos [94], and
breast epithelial cells in 3D collagen gels [95]. These self-generated persistent mo-
tions are crucially dependent on cell-cell adhesions and myosin contractility, loss
of which can drive malignant behavior. In recent years, collective motion in geo-
metric conﬁnement have been studied in a more controlled manner using adhesive
micropatterns [96], which allow conﬁnement of cell cultures in geometric domains
of any shape and size.
When plated in circular micropatterns, small sized epithelial monolayers often
exhibit large scale correlated movements and spontaneous swirling motions, as
shown in Fig. 8b [8, 9, 97, 36]. These collective rotations emerge once the cells
have reached a critical density (2000 cells/mm2) and occur in micropatterns of radii
smaller than the cellular velocity correlation length (∼200 µm) in unconﬁned situ-
ations [8]. Furthermore these rotations require cell-cell adhesions for efﬁcient trans-
mission of motility cues by contact guidance [8], and radial velocity oscillations are
observed with a time period linearly proportional to the micropattern radius [9].
Aside from collective rotational motion, emergence of active nematic states has
also been observed in conﬁned monolayers of elongated ﬁbroblasts and MDCK
cells [98, 99, 100]. In these cases, cells actively transfer alignment cues from the
boundary to the bulk of the monolayer, resulting in domains of alignment and topo-
logical defect patterns.
Different cell-based computational models have been implemented to recapitu-
late collective rotational motion, including the the cellular Potts model [101, 8, 102],
active particle models [9], and voronoi-type models [23], where persistent rotations
emerge due to velocity alignment mechanisms of motile cells. In recent work [36],
we described collective rotations using a continuum model similar to Eq. (8)-(11)
(Fig. 8c-d). This model quantitatively captures a key aspect of the experimental
data, namely, that the cell velocity ﬁeld alternated between inward and outward
radial motion with a time period equal to that of the oscillations in the intercellu-
lar stress [36]. This wave-like motion is predicted by the model to arise through
the chemomechanical feedback between the mechanical strain, ∇u, and actomyosin


## Page 15


Continuum models of collective cell migration
15
Fig. 8 Coherent cell motion in conﬁned environment. (a) Coherent angular motion of cells
during acinus morphogenesis, adapted from Ref. [95]. Graph shows angular rotation of the parent
and daughter cells obtained by nuclei tracking. Inset: Cross section of acinus with F-actin staining
in green (Scale bar=30 µm). (b) Collective rotation of MDCK cells seeded on circular ﬁbronectin
patterns, reproduced from Ref. [8]. The magnitude and the direction of local velocity ﬁelds are
indicated by red arrows (Scale bar = 50 µm). (c) Kymograph of radial velocity ﬁelds of conﬂuent
cells in a micropattern [36], showing periodic oscillations. (d) Radial velocity kymograph, obtained
by simulating Eqs. (8)-(11), reproducing collective cell oscillations.
contractility, c [38]. In the limiting case where cell deformations, u, is only coupled
to polarity p, no oscillatory behavior is observed. This prediction was conﬁrmed by
experiments, where inhibition of contractility by blebbistatin eliminated the multi-
cellular oscillations. Furthermore, the polarization ﬁeld, p, is crucial to capture the
misalignment between traction and velocity, observed experimentally. Overall, the
coupling of cell motion to polarization and actomyosin contractility is required to
to capture the experimentally observed distribution of traction forces [36], which
points inward at the periphery of the micropattern and oscillates between outward
and inward within the bulk of the monolayer.
3.4 Epithelial movement during gap closure
Collective cell movement during epithelial gap closure is essential for maintaining
the tissue mechanical integrity and to protect the internal environment from the
outside by regenerating a physical barrier. Gaps can occur autonomously during


## Page 16


16
Shiladitya Banerjee and M. Cristina Marchetti
Fig. 9 Collective migration during epithelial gap closure. (a) Closure of in vitro wound in ep-
ithelial monolayers is mediated by a combination of purse-string based contraction of actomyosin
cable (arrows) and lamellipodia based cell crawling (arrowheads). Figure adapted from Ref. [105].
(b) Lamellipodial protrusions generate traction forces away from the wound (red arrows), whereas
traction generated by purse-string based contraction point towards the wound (green arrows). Trac-
tion stress map reproduced from Ref. [68]. (c) Schematic of a continuum model for gap closure,
showing the dependence of purse-string and crawling forces on the local gap geometry. (d) Mi-
gration velocity increases with increasing magnitude of local gap curvature. Reproduced from
Ref. [109].
development [103], or can be generated by cell apoptosis [104] or tissue injury. It is
widely accepted that epithelial gap closure is driven by two distinct mechanisms for
collective cell movement (Fig. 9a) [105, 4]. First, cells both proximal and distal to
the gap can crawl by lamellipodial protrusions [106, 107, 3]. Secondly, cells around
the gap can assemble a multicellular actomyosin purse-string, which closes gaps via
contractile forces (Fig. 9b) [106, 108]. The continuum framework described in this
review can be appropriately adapted to study the relative contributions of crawling
and contractile forces on epithelial gap closure.
Continuum models of tissue gap closure have considered both visco-elastic
solid [110] and ﬂuid [111, 109] models of tissues. In either scenarios, force bal-
ance between cell-cell and cell-substrate interactions can be expressed as,
h∇.σ = ζv−fp ,
(14)


## Page 17


Continuum models of collective cell migration
17
where f is the magnitude of the propulsion force acting on the cells due to lamel-
lipodial protrusions, both proximal and distal to the gap, such that p points into free
space. While previous continuum models have neglected the polarity term in the
force balance, this is necessary for the misalignment of traction force and velocity
observed for instance in closed contour wound healing assays [68]. To model the ac-
tive pulling forces on the gap boundary, Eq. (14) is solved subject to the following
boundary condition for the stress tensor on the moving gap boundary (Fig. 9c):
σ .ˆn = (fL −λκ)ˆn ,
(15)
where ˆn is the local normal vector on the gap boundary, directed away from the
tissue, fL is the force density due to lamellipodial protrusions, κ is the local gap
boundary curvature (negative for circular gaps), and λ is the line tension due to acto-
myosin purse-string. The model has been used to capture the sensitivity of collective
motion on the local gap geometry [109] (Fig. 9d). For instance, crawling mediated
migration (λ = 0) occurs at a speed independent of gap curvature, whereas purely
purse-string driven motility (fL = 0) increases with decreasing radius of curvature.
This may explain why purse-string is not assembled for large wounds, as its driving
force is inversely proportional to the gap diameter. A model of cable reinforcement,
where tension λ ∝κ, has also been proposed to account for the experimentally
observed increase in closure velocity and traction stress with time [110]. A more
comprehensive model of gap closure dynamics with spatiotemporal variations in
lamellipodia and purse-string forces (Fig. 9b) has recently been implemented using
the vertex model [28].
4 Comparisons between active elastic and ﬂuid models of
collective cell migration
Previous work has employed both elastic [60, 38] and ﬂuid [112, 53, 113, 35, 114,
115] models of epithelial cell sheet to describe the dynamics of epithelial expansion,
as probed for instance in wound healing assays (Fig. 7a). Both models can account
for traveling waves, as observed in experiments, provided the sheet rheology is cou-
pled to internal dynamical degrees of freedom, such as contractile activity (elastic
model [38]) or cell division or polarization (ﬂuid model [113, 114]). On the other
hand, tissues can undergo ﬂuidization/stiffening cycles, respond elastically or vis-
cously on different times scales, and there is still no continuum model capable of
capturing their rheology across all time scales.
In this section we compare the viscous and elastic continuum approaches for
modeling cell monolayers, focusing on a one-dimensional (1d) model that allows
for an analytical solution. The 1d calculation can also be directly compared to ex-
periments such as those shown in Fig. 5a, where the monolayer properties are gen-
erally averaged over the direction transverse to that of mean motion. Denoting by x
the direction of monolayer expansion, the in-plane force balance equation is simply


## Page 18


18
Shiladitya Banerjee and M. Cristina Marchetti
given by
ζvx = f px +h∂xσ ,
(16)
where σ = σxx = σc + σa. In the absence of cell division and tissue growth, the
volume of the monolayer remains approximately constant during expansion. This
requires the product L(t)h(t) to remain constant, where L(t) and h(t) are the mono-
layer width in the direction of expansion and the monolayer thickness at time t,
respectively. For simplicity in the following we neglect the variation of h.
To illustrate the difference between the ﬂuid and elastic models we examine be-
low the accumulation of contractile stresses in an isotropic expanding monolayer,
with vanishing net polarization, that was discussed for the ﬂuid case in Ref. [35].
In contrast to Ref. [35] we assume σa = constant, to incorporate contractile cell
activity. We neglect both nonlinear active stresses and spatiotemporal variations of
the concentration c of contractile actomyosin. We additionally use a quasi-static ap-
proximation for the cell polarization that is assumed to relax on time scales much
faster than those associated with cellular deformations and rearrangements. Finally,
for simplicity we will neglect the spatial and temporal variation of the thickness h of
the monolayer. We retain only linear terms so that the polarization ﬁeld, px, satisﬁes
the equation [35]
L2
p∂2
x px = px ,
(17)
where we have introduced the length scale Lp =
p
κ/a that describes spatial varia-
tion in polarization within the monolayer.
The viscous or elastic nature of the cell sheet will be speciﬁed by the chosen
form of the constitutive equation for the intercellular stresses, σc. One important
distinction, not apparent in the linear form of the equations considered here, is that
the ﬂuid motion is treated in an Eulerian frame, while the elastic medium model is
implemented in a Lagrangian frame of reference. This difference will be important
below when imposing boundary conditions.
The case of a ﬂuid layer of growing width 2L(t) was discussed in Ref. [35]
(Fig. 10a). In this case intercellular stresses are purely viscous, with σc = η∂xvx and
η the shear viscosity. Assuming that cells at the boundaries are outwardly polarized
to drive expansion, i.e., px(−L(t)) = −1 and px(+L(t)) = 1, the static polarization
proﬁle is given by
px(x) =
sinh(x/Lp)
sinh(L(t)/Lp) .
(18)
The force balance equation, Eq. (16), can then be recast as an equation for the total
stress in the ﬂuid monolayer σv(x) = σ(x),
1
L2v
(σv −σa) = f0
Lp
∂xpx +∂2
x σv
(19)
where Lv =
p
hη/ζ is a viscous length scale, and f0 = fLp/h is a characteristic
stress scale. We solve Eq. (19) with stress-free boundary conditions at the monolayer
edge, σv(x = ±L(t)) = 0, where L = L(t) is the growing monolayer length. The
resultant stress is,


## Page 19


Continuum models of collective cell migration
19
σv(x) = σa

1−cosh(x/Lv)
cosh(L/Lv)

+
f0L2
v
L2p −L2v
cosh(x/Lp)
sinh(L/Lp) −cosh(L/Lp)cosh(x/Lv)
sinh(L/Lp)cosh(L/Lv)

.
(20)
As shown in Ref. [35] and in Fig. 10b-c, the shape of the stress proﬁle depends on
the length L(t) as well as on the ratio Lp/Lv > 0. With increasing L (for ﬁxed Lp/Lv)
or Lp/Lv (for ﬁxed L), the initial stress maxima at the center of the layer disappears,
and two stress peaks accumulate near the edge of the colony.
The length L(t) of the expanding layer can be determined by equating the rate of
change of L(t) to the velocity at the leading edge, ˙L = vx(L). For L(t) ≫Lp,Lv we
ﬁnd vx(L) ≃f0L2
v/η(Lp +Lv)−σaLv/η, resulting in a linear growth in time of the
length of the monolayer,
L(t) = L0 +
LpL2
v
hη(Lp +Lv)(f −f v
c )t ,
(21)
provided the pulling force f exceeds a threshold value required to overcome the
contractile force, f v
c = hσa(L−1
p +L−1
v ), and drive layer expansion. Note, however,
that the assumption of indeﬁnite growth in time in the absence of cell division is not
realistic. Such a growth will be arrested by the requirement of volume conservation.
If the cell monolayer is modeled as an elastic continuum, then σc = B∂xux where
B is a compressional modulus and ux the displacement ﬁeld. The velocity must be
identiﬁed with the rate of change of the displacement, vx = ∂tux. In this case the
-
-








/()
σ()/σ
Lp/Lv=0.01
Lp/Lv=0.1
Lp/Lv=0.25
-
-








/()
σ()/σ
t=0
t=2
t=5
a
b
c
x
h
2L(t)
Lp
Fig. 10 Viscous ﬂuid model of expanding monolayers. (a) Schematic of an expanding epithelial
monolayer of height h and length 2L, studied in Ref. [35]. The purple shaded curve represents the
spatial proﬁle of the polarization ﬁeld, whose penetration depth is characterized by the length scale
Lp. (b) Representative stress proﬁles of an expanding cell monolayer, predicted by the ﬂuid model
in Eq. (20), at different values of time with ﬁxed Lp/Lv = 0.25. (c) Stress proﬁles for different
values of Lp/Lv at ﬁxed length L = 4L(0). Other parameters: Lp/L(0) = 0.5, f0/σa = 2.


## Page 20


20
Shiladitya Banerjee and M. Cristina Marchetti
layer has a reference length 2L0 and an expanded length 2L(t) = 2L0 + u(L0,t) −
u(−L0,t). The polarization proﬁle has the same functional form given in Eq. (18),
but with L(t) replaced by L0. It is then evident that, in the absence of cell division
and growth, the only steady state solution will have vx = 0 corresponding to the fact
that the elastic layer can be stretched by outward pulling cells, but not indeﬁnitely
expanded. The stress balance equation can again be written as a closed equation for
the stress (σel(x) = σ(x)), h∂xσel = −f px(x), with the solution (Fig. 5b)
σel(x) = f0
cosh(L0/Lp)−cosh(x/Lp)
sinh(L0/Lp)
.
(22)
The stress proﬁle of the elastically stretched tissue is controlled by the single length
scale Lp and always shows a maximum at the midpoint of the layer. From this so-
lution, one can immediately obtain the steady state displacement ﬁeld, ux, at the
sample boundary, up to an undetermined constant. We eliminate this constant by as-
suming a symmetric deformation proﬁle such that ux(0) = 0. In the limit L0 ≫Lp we
get ux(L0) = −ux(−L0) = L0
B (f0Lp/L0 −σa). Of course in this case the monolayer
stretches only provided the pulling forces due to polarization exceed the contractile
forces. There is a critical pulling force, given by f e
c = hσaL0/L2
p. Retaining again
only leading terms in Lp/L0, the total length of the expanded monolayer is then
given by
L∞= L0
"
1+ L2
p
L0h(f −f e
c )
#
.
(23)
Unlike the ﬂuid, a purely elastic layer cannot sustain a state of steady growth.
To obtain steady expansion in the case where the layer is modeled as an elastic
medium it is necessary to include cell division. This can be accomplished in several
ways: by allowing the reference layer length L0 to grow with time; by describing cell
division in terms of an extensile contribution to the active stress, such as σa,g = −Rt,
where R > 0 describes the rate of growth; or by allowing the elastic constant B to
vary in time. Each of these prescriptions will in general give different expansion
rates for the monolayer. A full discussion of these cases is beyond the scope of
the present review. In general, both viscous and elastic models have successfully
reproduced the stress, velocity and deformation proﬁles measured in experiments.
This suggests that these large scale quantities may not be terribly sensitive to the
speciﬁc rheology of the monolayer. More work, however, remains to be done to fully
understand the mechanisms that allow living tissues to maintain their cohesiveness,
while exhibiting the ﬂuidity necessary for motion and morphological changes, and
to formulate a rheological model capable of capturing these unique properties.


## Page 21


Continuum models of collective cell migration
21
5 Conclusion
Continuum models of multicellular mechanics have been widely successful in de-
scribing the physical forces, ﬂow and deformation patterns that mediate collective
cell migration during wound healing, tissue morphogenesis and development. These
models are largely based on phenomenological approaches rooted in soft condensed
matter physics, ﬂuid dynamics and statistical mechanics [40]. One of the key ad-
vantages of a continuum framework is that it is formulated in terms of a few coarse-
grained collective variables such as density, velocity, strain and stress ﬁelds which
are directly measurable in experiments. The resultant theory contains only a small
number of macroscopic parameters, representing the effective mechanochemical
couplings that arise from the combined effect of a number of signaling pathways
at subcellular and cellular scales.
On the other hand, continuum models are generally written down phenomeno-
logically, leaving open the key challenge of relating the continuum scale mechanical
parameters to speciﬁc processes that control the active behavior of cells at µm and
nm scales. In the absence of such a connection between subcellular and cellular or
tissue scale, there are no constraints on the range of values spanned by the param-
eters of the continuum model. Many of the molecular pathways that mediate force
generation and movement in cells are, however, intimately coupled and also sensi-
tive to external perturbations and to the physical properties the cell’s environment.
It is then likely that molecular scale feedback processes may constrain the range of
parameter values that are accessible at the cellular and tissue scales. As a result, all
the complex dynamical phases predicted by generic continuum models may not be
realizable in biological systems, as particular cells and tissues may likely operate in
a narrow region of parameter space.
Another key limitation of the continuum modeling approach lies in the assump-
tion of ﬁxed materials properties of tissues, which is encoded in the choice of a par-
ticular constitutive law. As discussed elsewhere [48], tissue rheology is highly com-
plex, and the presence of multiple relaxation times demands a rheological model ca-
pable of capturing both active solid-like and ﬂuid-like behavior in different regimes
of stress response. In this review, we focus on active elastic models of tissue mechan-
ics [41, 39, 80, 60, 38, 36] which have been successful in capturing many experimen-
tally observed cell behaviors during collective migration. These include mechanical
waves [7], collective cell rotations [8, 9, 36], traction force localization [5, 39], and
mechanosensitivity to extracellular matrix properties [42]. We also compare elastic-
ity models against viscous ﬂuid models of cell migration [35], showing that macro-
scopic quantities and observables may not sensitive to the speciﬁc choice of tissue
rheology. On the other hand, a number of mesoscopic models, such as the Vertex,
Voronoi, Potts and particle-based models, have been shown to capture various as-
pects of tissue-scale mechanics, providing an alternate bottom-up approach that may
allow us to connect molecular scale to tissue-scale properties. A systematic study of
such models with an eye on developing the multi-scale mechanics of multicellular
assemblies is currently lacking, and remains an open theoretical challenge at the
interface of physics and biology.


## Page 22


22
Shiladitya Banerjee and M. Cristina Marchetti
Living cells are active entities, capable for instance of autonomous motion, spon-
taneous mechanical deformations, division and phenotypical changes. This behavior
can often be modeled at the mesoscale through internal state variables unique to liv-
ing systems. In this review we have introduced two such internal state variables:
the concentration of intracellular molecular active force generators and the cell po-
larity vector that describes the direction in which individual cells tend to move.
For simplicity we have only considered the concentration of contractile units in the
actomyosin cytoskeleton, that may represent, for instance, phosporylated myosins.
More generally, several dynamically coupled chemical components may be needed
to capture the complexity of molecular processes in the cell cytoskeleton. Multiple
ﬁlaments, motors, and binding proteins compete to regulate cell homeostasis, polar-
ization, and active force generation [70]. As more fascinating regulatory properties
of the cytoskeletal machinery are being discovered, future models must attempt to
incorporate such self-regulatory mechanisms controlling active cell mechanics.
An open question is the molecular interpretation of the cell polarization. Dif-
ferent interpretations have been put forward in the literature, including identifying
cell polarization with the direction of lamellipodial/ﬁlopodial protrusions or with
the orientation of the cell long axis associated with the alignment of actin stress
ﬁbers, although the latter provides a nematic (head-tail symmetric) degree of free-
dom, rather than a polar one. Regardless of its subcellular origin, cell polarity serves
to dictate the direction of local motion, and is distinct from the actual direction of
cell motion in a tissue that is also controlled by the forces from neighboring cells. In
other words, the dynamics of the polarity vector encodes the decision-making rules
for cell motility that come from the sum of mechanical and biochemical cues that an
individual cell experiences from its internal as well as external environments. Given
the multitude of polarity cues gathered by a cell, it remains contentious whether a
single polarity state variable can fruitfully describe multiple mechanisms of active
cell motility.
Essential ingredients of the models described in this review are the feedbacks
between cellular mechanics, polarized motility, and the regulatory biochemistry of
actomyosin contractility. Mechanochemical coupling of cell motion, adhesion and
contractility have been argued as the physical basis for tissue morphogenesis and
development [116]. These couplings also play an essential role in the transmission
of spatial information in large cell monolayers, mediated by waves, pulses, and a
tug of war between cell-cell and cell-substrate forces. Both negative and positive
feedback loops are exploited by cells for robust movement and force generation.
Positive feedback commonly occurs between mechanical strain and advective trans-
port of cytoskeletal ﬁlaments and motors into regions of high contractility. These
active forces compete with diffusion and elasticity to establish the spatial gradients
of contractility responsible for spontaneous cell motion. On the other hand, nega-
tive feedback between mechanical strain and contractility can yield periodic cycles
of tissue stiffening and ﬂuidization, which can result in long-range propagation of
mechanical waves in tissues. At present, however, these feedback mechanisms re-
main purely phenomenological constructs, with only qualitative support from ex-
periments. Their direct quantiﬁcation is an outstanding experimental challenge.


## Page 23


Continuum models of collective cell migration
23
In the future, theorists and experimentalists will need to work together to identify
and probe all the key mechanical and biochemical parameters in a single model
system. Such collaborative efforts will lead the way to more quantitatively accurate
models of collective cell behavior in physiology and development.
Acknowledgements SB acknowledges support from a Strategic Fellowship at the Institute for
the Physics of Living Systems at UCL, Royal Society Tata University Research Fellowship
(URF\R1\180187), and Human Frontiers Science Program (HFSP RGY0073/2018). MCM was
supported by the National Science Foundation at Syracuse University through awards DMR-
1609208, DGE-1068780 and at KITP under Grant PHY-1748958, and by the Simons Foundation
through a Targeted Grant Award No. 342354. MCM thanks the Syracuse Soft and Living Matter
Program for support and the KITP for hospitality during completion of some of this work.
References
1. P. Friedl, D. Gilmour, Nature Reviews Molecular Cell Biology 10(7), 445 (2009)
2. B. Ladoux, R.M. M`ege, Nature Reviews Molecular Cell Biology 18(12), 743 (2017)
3. G. Fenteany, P.A. Janmey, T.P. Stossel, Current Biology 10(14), 831 (2000)
4. S. Begnaud, T. Chen, D. Delacour, R.M. M`ege, B. Ladoux, Current Opinion in Cell Biology
42, 52 (2016)
5. X. Trepat, M.R. Wasserman, T.E. Angelini, E. Millet, D.A. Weitz, J.P. Butler, J.J. Fredberg,
Nature Physics 5(6), 426 (2009)
6. R. Farooqui, G. Fenteany, Journal of Cell Science 118(1), 51 (2005)
7. X. Serra-Picamal, V. Conte, R. Vincent, E. Anon, D.T. Tambe, E. Bazellieres, J.P. Butler, J.J.
Fredberg, X. Trepat, Nature Physics 8(8), 628 (2012)
8. K. Doxzen, S.R.K. Vedula, M.C. Leong, H. Hirata, N.S. Gov, A.J. Kabla, B. Ladoux, C.T.
Lim, Integrative Biology 5(8), 1026 (2013)
9. M. Deforet, V. Hakim, H.G. Yevick, G. Duclos, P. Silberzan, Nature Communications 5,
3747 (2014)
10. T. Lecuit, P.F. Lenne, E. Munro, Annual Review of Cell and Developmental Biology 27, 157
(2011)
11. T.E. Angelini, E. Hannezo, X. Trepat, J.J. Fredberg, D.A. Weitz, Physical Review Letters
104(16), 168104 (2010)
12. T.E. Angelini, E. Hannezo, X. Trepat, M. Marquez, J.J. Fredberg, D.A. Weitz, Proceedings
of the National Academy of Sciences 108(12), 4714 (2011)
13. D.E. Discher, P. Janmey, Y.l. Wang, Science 310(5751), 1139 (2005)
14. R.A. Foty, G. Forgacs, C.M. Pﬂeger, M.S. Steinberg, Physical Review Letters 72(14), 2298
(1994)
15. M. Basan, T. Risler, J.F. Joanny, X. Sastre-Garau, J. Prost, HFSP Journal 3(4), 265 (2009)
16. A.F. Mertz, Y. Che, S. Banerjee, J.M. Goldstein, K.A. Rosowski, S.F. Revilla, C.M. Niessen,
M.C. Marchetti, E.R. Dufresne, V. Horsley, Proceedings of the National Academy of Sci-
ences 110(3), 842 (2013)
17. V. Maruthamuthu, B. Sabass, U.S. Schwarz, M.L. Gardel, Proceedings of the National
Academy of Sciences 108(12), 4708 (2011)
18. P. Roca-Cusachs, V. Conte, X. Trepat, Nature Cell Biology 19(7), 742 (2017)
19. M. Basan, J. Elgeti, E. Hannezo, W.J. Rappel, H. Levine, Proceedings of the National
Academy of Sciences 110(7), 2452 (2013)
20. B.A. Camley, W.J. Rappel, Journal of Physics D: Applied Physics 50(11), 113002 (2017)
21. H. Honda, G. Eguchi, Journal of Theoretical Biology 84(3), 575 (1980)
22. A.G. Fletcher, M. Osterﬁeld, R.E. Baker, S.Y. Shvartsman, Biophysical Journal 106(11),
2291 (2014)


## Page 24


24
Shiladitya Banerjee and M. Cristina Marchetti
23. B. Li, S.X. Sun, Biophysical Journal 107(7), 1532 (2014)
24. D. Bi, X. Yang, M.C. Marchetti, M.L. Manning, Physical Review X 6(2), 021011 (2016)
25. F. Graner, J.A. Glazier, Physical review letters 69(13), 2013 (1992)
26. R. Farhadifar, J.C. R¨oper, B. Aigouy, S. Eaton, F. J¨ulicher, Current Biology 17(24), 2095
(2007)
27. D.L. Barton, S. Henkes, C.J. Weijer, R. Sknepnek, PLoS Computational Biology 13(6),
e1005569 (2017)
28. M.F. Staddon, D. Bi, A.P. Tabatabai, V. Ajeti, M.P. Murrell, S. Banerjee, PLoS Computational
Biology 14(10), e1006502 (2018)
29. N. Noll, M. Mani, I. Heemskerk, S.J. Streichan, B.I. Shraiman, Nature Physics 13(12), 1221
(2017)
30. D. Bi, J. Lopez, J. Schwarz, M.L. Manning, Nature Physics 11(12), 1074 (2015)
31. F. Ziebert, S. Swaminathan, I.S. Aranson, Journal of The Royal Society Interface p.
rsif20110433 (2011)
32. J. Prost, F. J¨ulicher, J.F. Joanny, Nature Physics 11(2), 111 (2015)
33. R.W. Style, R. Boltyanskiy, G.K. German, C. Hyland, C.W. MacMinn, A.F. Mertz, L.A.
Wilen, Y. Xu, E.R. Dufresne, Soft Matter 10(23), 4047 (2014)
34. S. Banerjee, M.C. Marchetti, Europhysics Letters 96(2), 28003 (2011)
35. C. Blanch-Mercader, R. Vincent, E. Bazelli`eres, X. Serra-Picamal, X. Trepat, J. Casademunt,
Soft Matter 13(6), 1235 (2017)
36. J. Notbohm, S. Banerjee, K.J. Utuje, B. Gweon, H. Jang, Y. Park, J. Shin, J.P. Butler, J.J.
Fredberg, M.C. Marchetti, Biophysical Journal 110(12), 2729 (2016)
37. P.W. Oakes, S. Banerjee, M.C. Marchetti, M.L. Gardel, Biophysical Journal 107(4), 825
(2014)
38. S. Banerjee, K.J. Utuje, M.C. Marchetti, Physical Review Letters 114(22), 228101 (2015)
39. A.F. Mertz, S. Banerjee, Y. Che, G.K. German, Y. Xu, C. Hyland, M.C. Marchetti, V. Horsley,
E.R. Dufresne, Physical Review Letters 108(19), 198101 (2012)
40. M.C. Marchetti, J.F. Joanny, S. Ramaswamy, T.B. Liverpool, J. Prost, M. Rao, R.A. Simha,
Reviews of Modern Physics 85(3), 1143 (2013)
41. S. Banerjee, M.C. Marchetti, Physical Review Letters 109(10), 108101 (2012)
42. U.S. Schwarz, S.A. Safran, Reviews of Modern Physics 85(3), 1327 (2013)
43. W.R. Legant, C.K. Choi, J.S. Miller, L. Shao, L. Gao, E. Betzig, C.S. Chen, Proceedings of
the National Academy of Sciences 110(3), 881 (2013)
44. A. Bove, D. Gradeci, Y. Fujita, S. Banerjee, G. Charras, A.R. Lowe, Molecular Biology of
the Cell 28(23), 3215 (2017)
45. J. Murray, G. Oster, Journal of Mathematical Biology 19(3), 265 (1984)
46. J. Ranft, M. Basan, J. Elgeti, J.F. Joanny, J. Prost, F. J¨ulicher, Proceedings of the National
Academy of Sciences 107(49), 20863 (2010)
47. S. Yabunaka, P. Marcq, Physical Review E 96(2), 022406 (2017)
48. N. Khalilgharibi, J. Fouchard, P. Recho, G. Charras, A. Kabla, Current Opinion in Cell Biol-
ogy 42, 113 (2016)
49. H. Phillips, M. Steinberg, Journal of Cell Science 30(1), 1 (1978)
50. K. Guevorkian, M.J. Colbert, M. Durth, S. Dufour, F. Brochard-Wyart, Physical Review Let-
ters 104(21), 218101 (2010)
51. C. Guillot, T. Lecuit, Science 340(6137), 1185 (2013)
52. C.P. Heisenberg, Y. Bella¨ıche, Cell 153(5), 948 (2013)
53. P. Lee, C.W. Wolgemuth, PLoS Computational Biology 7(3), e1002007 (2011)
54. G. Wayne Brodland, C.J. Wiebe, Computer methods in biomechanics and biomedical engi-
neering 7(2), 91 (2004)
55. A.R. Harris, L. Peter, J. Bellis, B. Baum, A.J. Kabla, G.T. Charras, Proceedings of the Na-
tional Academy of Sciences 109(41), 16449 (2012)
56. D. Gonzalez-Rodriguez, L. Bonnemay, J. Elgeti, S. Dufour, D. Cuvelier, F. Brochard-Wyart,
Soft Matter 9(7), 2282 (2013)
57. N. Khalilgharibi, J. Fouchard, N. Asadipour, A. Yonis, A. Harris, P. Mosaffa, Y. Fujita,
A. Kabla, B. Baum, J.J. Munoz, et al., bioRxiv p. 302158 (2018)


## Page 25


Continuum models of collective cell migration
25
58. D.T. Tambe, C.C. Hardin, T.E. Angelini, K. Rajendran, C.Y. Park, X. Serra-Picamal, E.H.
Zhou, M.H. Zaman, J.P. Butler, D.A. Weitz, et al., Nature Materials 10(6), 469 (2011)
59. S. Banerjee, T.B. Liverpool, M.C. Marchetti, Europhysics Letters 96(5), 58004 (2011)
60. M.H. K¨opf, L.M. Pismen, Soft Matter 9(14), 3727 (2013)
61. D.S. Banerjee, A. Munjal, T. Lecuit, M. Rao, Nature Communications 8(1), 1121 (2017)
62. E. Latorre, S. Kale, L. Casares, M. G´omez-Gonz´alez, M. Uroz, L. Valon, R.V. Nair, E. Gar-
reta, N. Montserrat, A. del Campo, B. Ladoux, M. Arroyo, X. Trepat, Nature 563(7730), 203
(2018)
63. M. Murrell, P.W. Oakes, M. Lenz, M.L. Gardel, Nature Reviews Molecular Cell Biology
16(8), 486 (2015)
64. S. Banerjee, M.C. Marchetti, Soft Matter 7(2), 463 (2011)
65. J.S. Bois, F. J¨ulicher, S.W. Grill, Physical Review Letters 106(2), 028103 (2011)
66. I. Linsmeier, S. Banerjee, P.W. Oakes, W. Jung, T. Kim, M.P. Murrell, Nature Communica-
tions 7, 12615 (2016)
67. S. Walcott, S.X. Sun, Proceedings of the National Academy of Sciences 107(17), 7757
(2010)
68. A. Brugu´es, E. Anon, V. Conte, J.H. Veldhuis, M. Gupta, J. Colombelli, J.J. Mu˜noz, G.W.
Brodland, B. Ladoux, X. Trepat, Nature Physics 10(9), 683 (2014)
69. A.J. Lomakin, K.C. Lee, S.J. Han, D.A. Bui, M. Davidson, A. Mogilner, G. Danuser, Nature
Cell Biology 17(11), 1435 (2015)
70. C. Suarez, D.R. Kovar, Nature Reviews Molecular Cell Biology 17(12), 799 (2016)
71. A. Ahmadi, M.C. Marchetti, T.B. Liverpool, Physical Review E 74(6), 061913 (2006)
72. J. Prost, The physics of liquid crystals, vol. 83 (Oxford university press, 1995)
73. T. Vicsek, A. Czir´ok, E. Ben-Jacob, I. Cohen, O. Shochet, Physical Review Letters 75(6),
1226 (1995)
74. F.B. Robin, J.B. Michaux, W.M. McFadden, E.M. Munro, bioRxiv p. 076356 (2016)
75. R. Vincent, E. Bazelli`eres, C. P´erez-Gonz´alez, M. Uroz, X. Serra-Picamal, X. Trepat, Physi-
cal Review Letters 115(24), 248103 (2015)
76. R. Levayer, T. Lecuit, Trends in Cell Biology 22(2), 61 (2012)
77. P. Gross, K.V. Kumar, S.W. Grill, Annual Review of Biophysics 46, 337 (2017)
78. M.A. Wozniak, C.S. Chen, Nature Reviews Molecular cell biology 10(1), 34 (2009)
79. O. Du Roure, A. Saez, A. Buguin, R.H. Austin, P. Chavrier, P. Siberzan, B. Ladoux, Proceed-
ings of the National Academy of Sciences 102(7), 2390 (2005)
80. C.M. Edwards, U.S. Schwarz, Physical Review Letters 107(12), 128101 (2011)
81. A. Ravasio, A.P. Le, T.B. Saw, V. Tarle, H.T. Ong, C. Bertocchi, R.M. M`ege, C.T. Lim, N.S.
Gov, B. Ladoux, Integrative Biology 7(10), 1228 (2015)
82. S. Banerjee, M.C. Marchetti, New Journal of Physics 15(3), 035015 (2013)
83. M. Ghibaudo, A. Saez, L. Trichet, A. Xayaphoummine, J. Browaeys, P. Silberzan, A. Buguin,
B. Ladoux, Soft Matter 4(9), 1836 (2008)
84. A. Chopra, E. Tabdanov, H. Patel, P.A. Janmey, J.Y. Kresh, American Journal of Physiology-
Heart and Circulatory Physiology 300(4), H1252 (2011)
85. P. Roca-Cusachs, J. Alcaraz, R. Sunyer, J. Samitier, R. Farr´e, D. Navajas, Biophysical Journal
94(12), 4984 (2008)
86. A. Zemel, F. Rehfeldt, A. Brown, D. Discher, S. Safran, Nature Physics 6(6), 468 (2010)
87. I.B. Bischofs, S.S. Schmidt, U.S. Schwarz, Physical Review Letters 103(4), 048101 (2009)
88. H. Delano¨e-Ayari, J. Rieu, M. Sano, Physical Review Letters 105(24), 248103 (2010)
89. E.N. Schaumann, M.F. Staddon, M.L. Gardel, S. Banerjee, Molecular Biology of the Cell
29(23), 2835 (2018)
90. J.C. Yarrow, Z.E. Perlman, N.J. Westwood, T.J. Mitchison, BMC Biotechnology 4(1), 21
(2004)
91. M. Poujade, E. Grasland-Mongrain, A. Hertzog, J. Jouanneau, P. Chavrier, B. Ladoux,
A. Buguin, P. Silberzan, Proceedings of the National Academy of Sciences 104(41), 15988
(2007)
92. L. Petitjean, M. Reffay, E. Grasland-Mongrain, M. Poujade, B. Ladoux, A. Buguin, P. Sil-
berzan, Biophysical Journal 98(9), 1790 (2010)


## Page 26


26
Shiladitya Banerjee and M. Cristina Marchetti
93. M. Th´ery, Nature Physics 8(8), 583 (2012)
94. L.A. D’Amico, M.S. Cooper, Developmental Dynamics 222(4), 611 (2001)
95. K. Tanner, H. Mori, R. Mroue, A. Bruni-Cardoso, M.J. Bissell, Proceedings of the National
Academy of Sciences 109(6), 1973 (2012)
96. M. Th´ery, M. Piel, Cold Spring Harbor Protocols 2009(7), pdb (2009)
97. F.J. Segerer, F. Th¨uroff, A.P. Alberola, E. Frey, J.O. R¨adler, Physical Review Letters 114(22),
228102 (2015)
98. G. Duclos, S. Garcia, H. Yevick, P. Silberzan, Soft Matter 10(14), 2346 (2014)
99. G. Duclos, C. Erlenk¨amper, J.F. Joanny, P. Silberzan, Nature Physics 13(1), 58 (2017)
100. T.B. Saw, A. Doostmohammadi, V. Nier, L. Kocgozlu, S. Thampi, Y. Toyama, P. Marcq, C.T.
Lim, J.M. Yeomans, B. Ladoux, Nature 544(7649), 212 (2017)
101. A.J. Kabla, Journal of The Royal Society Interface p. rsif20120448 (2012)
102. P.J. Albert, U.S. Schwarz, PLoS Computational Biology 12(4), e1004863 (2016)
103. W. Wood, A. Jacinto, R. Grose, S. Woolner, J. Gale, C. Wilson, P. Martin, Nature Cell Biol-
ogy 4(11), 907 (2002)
104. J. Rosenblatt, M.C. Raff, L.P. Cramer, Current Biology 11(23), 1847 (2001)
105. A. Jacinto, A. Martinez-Arias, P. Martin, Nature Cell Biology 3(5), E117 (2001)
106. P. Martin, J. Lewis, Nature 360(6400), 179 (1992)
107. E. Anon, X. Serra-Picamal, P. Hersen, N.C. Gauthier, M.P. Sheetz, X. Trepat, B. Ladoux,
Proceedings of the National Academy of Sciences 109(27), 10891 (2012)
108. W.M. Bement, P. Forscher, M.S. Mooseker, The Journal of Cell Biology 121(3), 565 (1993)
109. A. Ravasio, I. Cheddadi, T. Chen, T. Pereira, H.T. Ong, C. Bertocchi, A. Brugues, A. Jacinto,
A.J. Kabla, Y. Toyama, et al., Nature Communications 6, 7683 (2015)
110. S.R.K. Vedula, G. Peyret, I. Cheddadi, T. Chen, A. Brugu´es, H. Hirata, H. Lopez-Menendez,
Y. Toyama, L.N. De Almeida, X. Trepat, et al., Nature Communications 6, 6111 (2015)
111. O. Cochet-Escartin, J. Ranft, P. Silberzan, P. Marcq, Biophysical Journal 106(1), 65 (2014)
112. J. Arciero, Q. Mi, M.F. Branca, D.J. Hackam, D. Swigon, Biophysical Journal 100, 535
(2011)
113. P. Recho, J. Ranft, P. Marcq, Soft Matter 12, 2381 (2016)
114. C. Blanch-Mercader, J. Casademunt, Soft Matter 13(38), 6913 (2017)
115. C. P´erez-Gonz´alez, R. Alert, C. Blanch-Mercader, M. G´omez-Gonz´alez, T. Kolodziej,
E. Bazellieres, J. Casademunt, X. Trepat, Nature Physics (2018)
116. J. Howard, S.W. Grill, J.S. Bois, Nature Reviews Molecular Cell Biology 12(6), 392 (2011)

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
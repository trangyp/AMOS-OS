---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1609.01764v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1609.01764v1_Crawling_and_turning_in_a_minimal_reaction-diffusion_cell_motility_model__coupli

> Source: 1609.01764v1_Crawling_and_turning_in_a_minimal_reaction-diffusion_cell_motility_model__coupli.pdf

> Pages: 12

---


## Page 1


Crawling and turning in a minimal reaction-diffusion cell motility model: coupling cell shape and
biochemistry
Brian A. Camley,1, 2, ∗Yanxiang Zhao,3, ∗Bo Li,4 Herbert Levine,5 and Wouter-Jan Rappel1, 2
1Department of Physics, University of California, San Diego, La Jolla CA 92093
2Center for Theoretical Biological Physics, University of California, San Diego
3Department of Mathematics, The George Washington University, Washington, D.C.
4Department of Mathematics and Graduate Program in Quantitative Biology, University of California, San Diego, La Jolla CA 92093
5Department of Bioengineering, Center for Theoretical Biological Physics, Rice University, Houston, TX 77005
We study a minimal model of a crawling eukaryotic cell with a chemical polarity controlled by a reaction-
diffusion mechanism describing Rho GTPase dynamics. The size, shape, and speed of the cell emerge from
the combination of the chemical polarity, which controls the locations where actin polymerization occurs, and
the physical properties of the cell, including its membrane tension. We ﬁnd in our model both highly persistent
trajectories, in which the cell crawls in a straight line, and turning trajectories, where the cell transitions from
crawling in a line to crawling in a circle. We discuss the controlling variables for this turning instability, and
argue that turning arises from a coupling between the reaction-diffusion mechanism and the shape of the cell.
This emphasizes the surprising features that can arise from simple links between cell mechanics and biochem-
istry. Our results suggest that similar instabilities may be present in a broad class of biochemical descriptions of
cell polarity.
I.
INTRODUCTION
Cell motility is a fundamental aspect of biology, crucial in pro-
cesses ranging from morphogenesis to wound healing to cancer
metastasis [1]. Many aspects of cell motility have been exten-
sively modeled, ranging from the biochemistry and physics of
actin-polymerization-based protrusion [2, 3], to the importance of
cytoskeleton mechanics [4–6] to a wide variety of internal mech-
anisms for determining a cell’s orientation [7–9]. Many of these
aspects of the modeling of eukaryotic cell shape and motility have
been reviewed in two recent papers [10, 11].
In this paper, we will take a minimalistic approach, focusing on
two main aspects of cell motility: the cell shape, as determined
by a force balance at the surface of the cell, and the cell’s internal,
chemical regulation of its direction, modeled by reaction-diffusion
equations within the cell. This model can be characterized by a
small number of unitless parameters – six physical and biochem-
ical parameters, and a few others related to the numerical evalua-
tion of the model. The relative simplicity of this model allows us
to capture essential cell behaviors, but avoids the full parameter
space of more detailed schemes.
Even with such a simple model, it is possible to create rea-
sonable cell shapes, which can be regulated by both physical and
chemical features. In addition, we show that both linear and cir-
cular crawling trajectories can be observed. We argue that the cir-
cular trajectories arise from a coupling between cell shape and the
internal chemical polarity of the cell, and suggest that these effects
should be visible in a broad variety of models for cell polarity. Our
results may provide some insight into recent experiments linking
cell turning events and cell speed [12].
II.
MODEL
We model the cell’s boundary as an interface with a tension ap-
plied to it, driven by actin polymerization at the front of the cell
and myosin-based contraction at the cell rear. For simplicity, we
∗B.A. Camley and Y. Zhao contributed equally to this work.
neglect the membrane’s bending modulus; including it is straight-
forward [13], but we have found it does not qualitatively chage
our results. The cell front and rear are characterized by the distri-
bution of a membrane-bound Rho GTPase ˜ρ (a polarity protein),
whose dynamics are given by a variant of the simple wave-pinning
reaction-diffusion model established by Mori et al. [14]. We as-
sume that the motion of the cell membrane is overdamped, i.e.
obeying a force balance Factomyosin + Fmembrane + Ffriction = 0. We
assume that the actomyosin force is normally directed and propor-
tional to ˜ρ,
Factomyosin = (α˜ρ −β) ˆn
(1)
where α, β > 0 and ˆn is the outward-pointing normal to the cell.
Similar assumptions are used in [7, 13, 15]. This corresponds to a
cell pushing out at the front, where α˜ρ > β and contracting at the
back, where α˜ρ < β; α is thus a measure of protrusiveness and
β a measure of contractility. We assume that the membrane has a
tension γ (a line tension, since we are working in two dimensions),
and thus exerts a force per unit length of
Fmembrane = −cγˆn
(2)
where c is the local curvature of the membrane. We assume a
ﬂuid-like friction, proportional to the velocity v of the cell bound-
ary,
Ffriction = −τv.
(3)
We will solve the combined force balance equation at the inter-
face, τv = (α˜ρ −β) ˆn −cγˆn, by casting it into a phase ﬁeld
form [16–18]. This approach has been used to extensively model
both single and collective cell dynamics over the past few years
[4, 13, 15, 19–24]; our model follows our earlier work, particu-
larly [13, 15]. We will describe the cell boundary by a ﬁeld φ(˜r),
where φ smoothly varies from zero outside of the cell to unity
inside the cell; this variation has a characteristic length scale ˜ϵ.
φ = 1/2 implicitly sets the location of the boundary. As shown in
[13, 15], the phase ﬁeld version of this equation is
τ∂˜tφ = (α˜ρ −β) | ˜∇φ| + γ

˜∇2φ −G′(φ)
˜ϵ2

(4)
where G(φ) = 18φ2(1 −φ)2. In the limit ˜ϵ →0, we expect the
motion of the interface at φ = 1/2 to follow the force-balance law
arXiv:1609.01764v1  [physics.bio-ph]  6 Sep 2016


## Page 2


2
described above. We have used tildes f
· · · to indicate a unitful vari-
able; we will later rescale them to unitless variables and drop the
tildes to reduce the number of characteristic parameters involved.
To determine the direction the cell travels, we model the dy-
namics of a Rho GTPase, which will be a polarity marker indi-
cating the front of the cell. This Rho GTPase could be, e.g. Rac,
which is often localized to the cell front and leads to protrusion
[25]. We apply a modiﬁcation of the reaction-diffusion model of
Mori et al. [14]. In this model, a Rho GTPase protein switches be-
tween a membrane-bound, active state, with a concentration ˜ρ(˜r),
and a cytosolic form ˜ρcyt. As the diffusion coefﬁcients of cytosolic
Rho GTPases are typically 100 times those of membrane-bound
ones [26], we assume that the cytosolic density ˜ρcyt can be ap-
proximated as uniform over the cell. The membrane-bound form
diffuses with a diffusion coefﬁcient Dρ. In order to solve this
equation on the moving, deforming cell, we apply a phase ﬁeld
method [27, 28] in which we augment the reaction-diffusion equa-
tions with the phase ﬁeld φ. This equation is:
∂˜t (φ˜ρ) = ˜∇·

φDρ ˜∇˜ρ

+ φf(˜ρ, ˜ρcyt)
(5)
where the reaction term is
f(˜ρ, ˜ρcyt) = −k˜ρ (˜ρ −h) (˜ρ −m˜ρcyt)
(6)
This cubic reaction term is chosen for simplicity, as an example
of a reaction that can create polarity by wave-pinning [14], ro-
bustly leading to a region of the cell with a high concentration
of ˜ρ and a region of the cell with low ˜ρ.
In a homogeneous
system (constant ˜ρ), ˜ρ has two stable steady states, whose val-
ues are set by m and the total amount of ˜ρ in the system.
k
controls the overall timescale of the reaction, and h will set the
value of ˜ρ at the cell front.
˜ρcyt can be found by the conser-
vation of ˜ρ between its membrane-bound and cytosolic forms,
R
d2˜x (˜ρ(˜x) + ˜ρcyt) φ(˜x) = Ntot, or, assuming the cytosolic actin
promoter is well-mixed (uniform),
˜ρcyt = Ntot −
R
d2˜x˜ρ(˜x)φ(˜x)
R
d2˜xφ(˜x)
.
(7)
Eq. 5 will, in the sharp-interface limit ˜ϵ →0, reproduce the re-
sults of the reaction-diffusion equation ∂˜t˜ρ = Dρ ˜∇2˜ρ+f(˜ρ, ˜ρcyt)
solved with no-ﬂux boundaries on the cell interface [28]. How-
ever, we note that there is no advection in the reaction-diffusion
equation Eq. 5 - this corresponds to an assumption that the mem-
brane (except for its boundaries) is at rest relative to the substrate
the cell is crawling on. This assumption may be challenged, but
we note that similar turning phenomena are observed in models
with intracellular ﬂuid ﬂow [29].
We will rescale our variables into unitless form, choosing x ≡
˜x/R, t ≡˜tv0/R, ρ ≡˜ρ/2h, ρcyt ≡˜ρcyt/2h, where R is the
typical radius of the cell and v0 = 2hα/τ is the velocity scale.
We have chosen to rescale ˜ρ by its typical value at the front of the
cell, which is 2h [14]; hence ρ ≈1 at the front of the cell. In these
units, we ﬁnd
∂tφ = (ρ −ρ∗) |∇φ| + χ

∇2φ −G′(φ)
ϵ2

(8)
∂t (φρ) = Pe−1∇· (φ∇ρ) −Kφρ (ρ −1/2) (ρ −mρcyt)
(9)
ρcyt = C −
R
d2xρ(x)φ(x)
R
d2xφ(x)
.
(10)
where the only remaining parameters are the seven unitless pa-
rameters ρ∗, χ, Pe, K, C, m, and ϵ, as deﬁned in Table I.
Pe = v0R
Dρ
. . . . . . . . . . . Peclet number: speed of cell relative to
speed of diffusive transport; Pe ≈1 −
−10
K = kR(2h)2
v0
. . . . . . . . Relative speed of reaction compared to
motility; K = O(100)
χ =
γ
2hαR . . . . . . . . . . . Relative strength of tension vs acto-
myosin; χ ≈0.2
ρ∗=
β
2hα . . . . . . . . . . . Rescaled contractility; ρ∗is the value
of ρ such that actomyosin force is zero,
0 ≤ρ∗≤1
C =
Ntot
2hR2 . . . . . . . . . . . Rescaled total amount of ρ
m
. . . . . . . . . . . . . . . . . Reaction parameter
ϵ = ˜ϵ/R . . . . . . . . . . . . . Rescaled interface size
TABLE I. Table of unitless parameters
III.
PARAMETER ESTIMATION
Many of our parameters can be estimated well, or at least con-
strained, by using experimental data; other parameters may only
be varied over a narrow range in order for our cell to effectively
crawl.
We are interested in modeling the crawling of keratocytes and
other fast-moving cells [30–32], where cell speeds are in the range
of 0.1 −0.2 µm/s. We will thus take v0 ≈0.1µm/s. Keratocytes
typically cover areas of around 30µm × 15µm [33], so we will
assume an initial size scale of R ≈10µm. In the model of cell
polarity we use, we describe a Rho GTPase diffusing in the cell
membrane with diffusion coefﬁcient Dρ; typical membrane pro-
tein diffusion coefﬁcients of these Rho GTPases are of the order
of 0.1µm2/s [26], though of course there may be some variation
in this. With these estimates, we expect Pe = v0R/Dρ to take on
values ranging from 1 to 10, depending on the precise speed and
diffusion coefﬁcients involved. We will often report parameters in
terms of the inverse Peclet number, Pe−1, which enters Eq. 9 as
an effective diffusion coefﬁcient in our units.
The kinetic timescale of the Rho GTPases is expected to be on
the order of seconds [14, 34]; we will therefore set the rate k(2h)2
to be of the order of 1/s; this allows us to estimate K = O(100).
It is slightly more difﬁcult to estimate χ =
γ
2hαR =
γ
v0τR,
as we need to determine the effective friction coefﬁcient τ relat-
ing the force per unit length on the cell boundary to its velocity.
This friction is not simple, as it arises from a combination of hy-
drodynamic effects between the cell membrane and the substrate
and friction from breaking adhesions with the surface; we do not
know a convincing ﬁrst-principles estimate of this value. In [13],
a value of τ = 2.62 pNs/µm2 was found to create a reasonable
cell shape. The tension on the membrane is estimated to be of the
order γ ≈1pN [13], setting χ ≈0.2.
ρ∗is a rescaled contractility of the cell, measuring the ratio of
forces driving contraction (β) to those driving protrusion (2hα),
and does not have a natural scale. However, for the front of the
cell, where ρ ≈1, to protrude, we must have ρ∗< 1; we must
also have ρ∗> 0 for the back of the cell, where ρ ≈0, to contract,
see Eq. 8.
The values of C and m are constrained by the requirement that
the cell be able to polarize. These requirements include that [14,
35]:
|Ω|
m ≤C ≤m + 1
m
|Ω|
(11)


## Page 3


3
FIG. 1. Two characteristic trajectories of a crawling cell. Left: a crawling
cell with a higher unitless tension (χ = 0.3) maintains a persistent trajec-
tory. Right: a crawling cell undergoes a turning instability and transitions
to a circular trajectory when unitless tension is smaller (χ = 0.2). The
snapshots are taken at t = 0.2, 5.2, 10.2, · · · , 25.2. In each snapshot,
the blue line indicates the cell boundary, i.e. φ = 1/2, and the red line
indicates the cell front - the half-maximum contour of the Rho GTPase ρ.
ρ∗= 0.4, Pe−1 = 0.30, K = 500, C = 6, m = 0.5, ϵ = 0.1 in these
simulations.
where |Ω| is the area of the cell. Clearly as m →0, the cell
will not be able to polarize unless C is very carefully tuned. We
choose m = 1/2 and C = 6 throughout this paper, which we have
found allows cells to polarize within a reasonable range of cell
sizes. We note that the asymptotic results in [14, 35] from which
Eq. 11 is derived are only completely valid for a stationary cell.
However, we have found similar transitions between polarized and
unpolarized states in moving cells [29].
IV.
CELL BEHAVIOR
We numerically evaluate Eqs. 8-10 by a semi-implicit Fourier
spectral method; see Appendix A for numerical details. We ﬁnd
that this simple model supports both straight and circular trajec-
tories (Fig. 1). Initially the cell shape is taken to be circular, and
we choose the ρ-distribution to be polarized, ρ = 0.8 in the front
half and zero in the rear, though with a random noise added on
top (Appendix A). Due to this ρ-polarization, the front half of the
cell is pushed out while the rear half is contracted, deforming the
cell. After nearly t = 5, the crawling cell with χ = 0.3 reaches an
equilibrium shape and undergoes a straight trajectory, while the
one with χ = 0.2 undergoes a turning instability and transitions
to a circular trajectory at t ≈15. The straight trajectories resem-
ble the highly persistent, half-moon shape of crawling keratocytes
[30–32]. The turning behavior is equally likely to occur in either
direction, and depends on the noise in the initial conditions; larger
noise can accelerate turning, while states with zero initial noise
can proceed for a very long time without turning.
While we show only cells that effectively crawl in Fig. 1, we
also note that even initially polarized cells may become depolar-
ized, with ρ becoming uniform over the cell. This occurs at larger
tensions than we plot here, in which the cell cannot effectively
push the membrane out, and becomes too small to develop polar-
ization. This corresponds to violations of the constraints in Eq. 11
in which wave-pinning fails [14, 35], and only homogeneous so-
lutions to the reaction-diffusion equations are possible.
V.
TRANSITION TO CIRCULAR TRAJECTORIES
Unitless line tension χ
Inverse Peclet number Pe−1
Cells in straight trajectory
Cells in circular trajectory
0.15
0.2
0.25
0.3
0.1
0.15
0.2
0.25
0.3
0.35
FIG. 2. (Color online) Cells turn at low χ and high Pe−1. Blue crosses
show simulations where cells develop a circular trajectory. Points are
sampled from χ ∈[0.12, 0.3] and Pe−1 ∈[0.1, 0.36] with sample grid
0.02. Other parameters are ﬁxed as ρ∗= 0.4, K = 500, C = 6, m =
0.5, ϵ = 0.1. The background phase diagram is a sharp-interface predic-
tion, where the darker gray corresponds to turning cells. The theory is
detailed in Section VI C. Simulations are run until t = 40; if a cell has
not turned by this point, we treat it as a stable one with straight trajectory.
What parameters control the transition from straight trajectories
to circular ones? We show a χ-Pe−1 phase diagram in Fig. 2; in
this phase diagram, blue crosses indicate the parameters at which
we have observed cells turning and following circular trajectories.
In general, the straight trajectory is stabilized by increasing the
unitless tension χ on the cell and decreasing the unitless diffusion
coefﬁcient Pe−1 of the diffusing molecule ρ.
Additionally, for a crawling cell in circular trajectory, the cur-
vature κ of the trajectory is affected by χ and Pe−1. We show
a bifurcation diagram of κ as a function of χ for three values of
Pe−1 in Fig. 3. Curvature κ = 0 indicates the straight trajectory
of the crawling cell. We see the existence of a supercritical pitch-
fork bifurcation point for χ below which the crawling cell tends
to undergo circular motion (the up-down symmetry in the bifurca-
tion diagram is due to the fact that the cell can turn to clockwise
circular motion or counterclockwise circular motion with equal
probability), and after which the cell becomes stable in a straight
trajectory. The dashed line indicates that for small value of χ, the
straightly crawling cell is unstable in the sense that it will turn to
a circular motion under small perturbation in the system. As Pe−1
increases, the bifurcation value of χ becomes smaller, which is
also observed in the phase digram Fig. 2.
We plot a phase diagram for cell turning as a function of tension
χ and rescaled contractility ρ∗in Fig. 4; again, blue crosses indi-


## Page 4


4
FIG. 3. (Color online) Curvature κ of the circular-trajectory solutions of
Eqs. 8-10 as a function of tension χ. We plot these bifurcation diagrams
for three values of the inverse Peclet number, Pe−1 = 0.26, 0.28, 0.30
from bottom to top. Dashed lines indicate that the straight crawling cell
trajectory is unstable under small perturbation.
Unitless line tension χ
Rescaled contractility ρ*
Cells in straight trajectory
Cells in circular trajectory
0.2
0.25
0.3
0.25
0.3
0.35
0.4
0.45
0.5
0.55
FIG. 4. (Color online) Phase diagram for cell turning as a function of
tension χ and rescaled contractility ρ∗. Blue crosses show simulations
where cells develop a circular trajectory. Points are sampled from χ ∈
[0.18, 0.4] and ρ∗∈[0.28, 0.58] with sample grid size of 0.02. Other pa-
rameters are ﬁxed as Pe−1 = 0.3, K = 500, C = 6, m = 0.5, ϵ = 0.1.
Increasing the line tension χ tends to stabilize the cell; while increas-
ing ρ∗ﬁrst destabilizes the straight trajectory and then restabilizes it.
The background phase diagram is a sharp-interface prediction, where the
darker gray corresponds to turning cells. The theory is detailed in Sec-
tion VI C. Simulations are run until t = 40; if a cell has not turned by this
point, we treat it as a stable one with straight trajectory.
cate where the cell turns to a circular trajectory. Surprisingly, as
we vary ρ∗we observe reentry, as increasing ρ∗ﬁrst destabilizes
the straight trajectory and then subsequently restabilizes it.
The phase diagrams in both Fig. 4 and Fig. 2 show both simu-
lation results (blue crosses) and a theoretical approximation of the
phase diagram (dark/light gray coloring). We will now introduce
this theoretical analysis, which will provide some intuition about
the inﬂuence of χ, Pe−1, and ρ∗.
VI.
ORIGIN OF TURNING INSTABILITY: ANALYTICAL
ESTIMATE OF PHASE DIAGRAM
FIG. 5. (Color online) Proposed schematic diagram for turning instability.
Cell polarization leads to cell deformation (seen in Fig. 1); this leads to
polarity reorientation to minimize the length of the interior ρ interface,
as L2 < L1; this new ρ polarization will alter the cell shape. This is a
potential biomechanical mechanism for the generic instability proposed
in [36].
Why does turning occur? We argue that the turning instabil-
ity and circular trajectory arise from the coupling between the
reaction-diffusion mechanism and the cell shape in Eq. 9, in a
scheme illustrated in Fig. 5. The reaction-diffusion mechanism
tends to minimize the length of the interface between regions of
high ρ and low ρ. For this reason, the high ρ regions are attracted
to high curvature [35, 37]. As the cell is deformed, widening in the
direction perpendicular to cell motion, the cell front becomes a lo-
cal curvature minimum (Fig. 1), and the reaction-diffusion mech-
anism will, if the cell shape is ﬁxed, re-orient the cell polarization
to the high curvature region. The rate of this destabilizing process
is controlled by the effective diffusion coefﬁcient Pe−1.
Given this instability, why can the cell maintain a straight tra-
jectory if Pe−1 is low enough or χ high enough? Even if the
polarity is linearly unstable, the straight trajectory may be rescued
by the cell’s ability to adapt its shape. If the cell shape immedi-
ately reorients to any change in polarity, the cell cannot turn, and
the straight trajectory is stabilized. This explain the importance of
χ, as the dynamics of the cell shape strongly depend on χ. We
would then naturally expect increasing χ to stabilize the cell, and
increasing Pe−1 to destabilize it, as seen in Fig. 2. However, this
intuition does not immediately explain the effect of ρ∗in Fig. 4,
which we will ﬁnd to occur because of the inﬂuence of ρ∗on cell
shape.
We have been able to qualitatively, but not quantitatively repro-
duce the phase diagrams sketched in Fig. 2 and Fig. 4, including
the reentry, with a calculation based on this argument. In Sec.
VI A, we show that the ρ dynamics respond to the cell shape, and
show that this instability is slower as Pe increases, but also de-
pends on the cell shape. In Sec. VI B, we study the dynamics of
how the cell shape is controlled by the distribution of ρ, and show
that the speed at which a cell relaxes to its new shape is propor-
tional to χ. In Sec. VI C, we combine these results to predict the
phase diagram of cells as a function of the effective cell tension χ,
the Peclet number, and the rescaled contractility ρ∗.
A.
Dynamics of Rho GTPase within a ﬁxed geometry
Simulating the reaction-diffusion dynamics of Eq. 9 in a ﬁxed,
non-moving cell shows that the reaction-diffusion mechanism is
sensitive to cell shape (Fig. 6). In particular, we ﬁnd that the


## Page 5


5
cell “front” (region of high ρ) rotates to point toward the higher-
curvature region of the cell. This is consistent with the idea that
the reaction-diffusion dynamics of Eq. 9 serve to minimize the in-
terface between high ρ and low ρ. This behavior has been noted
before [35, 37]; see also a brief discussion of this point in [7].
FIG. 6. (Color online) Simulation of ρ dynamics in a ﬁxed geometry
shows that the high-ρ cell front region is attracted to regions of higher
curvature, as noted in [35, 37]. As a result, in a static near-elliptical
geometry, the polarity will tend to move toward the narrow end. (Cells
are rotated to show their elongated dimension along x.)
We characterize the kinetics of the instability of large ρ mov-
ing to higher curvature, and how it depends on the cell shape and
Peclet number. We will look at the dynamics of ρ in a cell with a
ﬁxed shape,
R(θ) = R0 −δ cos 2θ
where θ is, as usual, the angle counter-clockwise from the x axis.
To compute the evolution in ρ in a ﬁxed cell shape, we solve only
Eq. 9 with a ﬁxed φ(r) = 1
2 [1 + tanh (3rs/ϵ)], where rs is the
(signed) distance from the curve R(θ).
The instability in Fig. 6 is a linear instability. We ﬁnd that if
the distribution of ρ(θ) is initially centered near θ = 0, we ﬁnd an
exponential increase of the center of mass of ρ(θ) with time, θρ =
θρ(0)eσt. (Here, we deﬁne θρ to be the angle to the center of mass
of the distribution ρ(r), rρ =
R
d2rrρ(r)φ(r)/
R
d2rρ(r)φ(r).)
If this instability is driven by the mean curvature ﬂow identiﬁed
by Ref. 35, we would expect that σ ∼Pe−1. We have conﬁrmed
this numerically for the parameters we have studied (Fig. 7).
0.1
0.15
0.2
0.25
0.3
0.35
0.4
0.2
0.4
0.6
0.8
Pe−1
0.05
0.08
0.11
0.14
0.17
0.2
0.1
0.2
0.3
Cell shape enlongation  δ
Growth rate σ
FIG. 7. The growth rate σ of the reorientational ρ instability in a ﬁxed
cell geometry depends linearly on both the cell deformation δ and Pe−1.
The parameter δ = 0.3 is ﬁxed in the top subﬁgure, while in the bot-
tom subﬁgure, Pe−1 = 0.1 is ﬁxed. Other parameters take their default
values.
We also expect that as δ →0, the instability should vanish as a
perfect circle has no shape asymmetry. We ﬁnd, consistently with
this intuition, that σ ∼δ at small |δ| (Fig. 7). Based on these
results, we hypothesize that σ = bδPe−1 with b a constant, i.e.
d
dtθρ = bδPe−1θρ
(12)
Though this is reasonable at small δ, we would not expect it to nec-
essarily generalize to larger aspect ratios. In addition, in a more
complex shape, σ may depend on higher Fourier modes in the cell
shape.
B.
Dynamics of cell shape response to ρ
1.
Sharp interface theory
In the absence of any driving forces, or ρ = ρ∗, the phase
ﬁeld Eq. 8 is simply an Allen-Cahn equation. In the sharp in-
terface limit of ϵ →0, the interface evolves with a normal ve-
locity vn = −χκ with κ the interface curvature [38] (we note
this is distinct from the curvature of the trajectory, which we also
have labeled κ above, but is not addressed in this section). The
added forcing terms correspond to the interface being advected
with velocity v = (ρ −ρ∗)ˆn where ˆn = −∇φ/|∇φ| is the
outward-pointing normal. Since this term varies smoothly across
the boundary, we can get the normal interface velocity by adding
ρ −ρ∗directly to the curvature-driven relaxation velocity −χκ
[39]. Then the normal velocity of the cell boundary in arc-length
s should be:
vn(s) = (ρ −ρ∗) −χκ(s)
(13)
When the cell takes on a steady shape, the normal velocity must
satisfy:
Z
dsvn(s) = 0.
(14)
where the integral is over the entire cell boundary.
2.
Steady cell shape in quasi-circular Fourier modes
Let us describe a cell with boundary given by the function
R(θ, t), where the angle θ is with respect to the x axis . We can
expand R in Fourier modes:
R(θ, t) = R0 + g
X
cn(t)einθ.
(15)
Here we assume that the cell shape is close to circular, cn/R0 ≪
1, and we use f
P to denote P
̸=0,±1.
The n = ±1 mode is
excluded because it corresponds to the cell translational motion,
which we include by assuming that the cell is initially traveling
with a constant speed of v. We have also excluded the n = 0
size expansion mode; we ﬁnd, in a numerically exact solution of
Eq. 13, that there are many distinct solutions corresponding to
different cell perimeters. Selecting R0 or equivalently c0 chooses
which of these steady state solutions we observe, and will be done
later by setting the cell perimeter L ≈2πR0.
The normal velocity at an angle θ is [40]
vn(θ) = v · ˆn +
R
√
R2 + R′2
dR
dt
(16)


## Page 6


6
Up to the ﬁrst order of the deviations, we have
κ(θ, t) = 1
R0
+ 1
R2
0
g
X
(n2 −1)cn(t)einθ
(17)
vn(θ, t) = v · ˆn + g
X d
dtcn(t)einθ
(18)
Expanding Eq. 13 into Fourier modes, we ﬁnd (assuming the cell
has velocity v = vˆx),
d
dtcn(t) = ρn −χ
R2
0
(n2 −1)cn
(19)
+
v
2R0

(n + 1)cn+1 −(n −1)cn−1

,
n ̸= 0, ±1
We will treat c0 and c±1 as zero when they arise from the term
proportional to v here, and
ρn = 1
2π
Z π
−π
dθ [ρ(θ) −ρ∗] e−inθ
(20)
is the Fourier transform of the protrusion strength – how far the
Rho GTPase protein ρ exceeds the critical value ρ∗.
The equations of motion for the Fourier modes cn(t) (Eq. 19)
depend on the velocity of the cell, v. This velocity can be found,
following [40], as
v = 1
A
Z
dsR(s)vn(s)
(21)
≈ˆx
A
Z 2π
0
dθ
 
R2
0 + 2R0
X
n
cneinθ
!
×
[ρ(θ) −ρ∗−χK(θ)]
= ˆx
"
ρ1 + ρ−1 + 2
R0
X
n
cn (ρ−n+1 + ρ−n−1)
#
(22)
where R(s) is the vector pointing from the cell’s center of mass
to the element at arclength s, A ≈πR2
0 is the cell area, and the
approximation is true for small deformations.
We have seen from our simulations and the analysis of [14, 41]
that ρ has a sharp interface between values ρ+ = mρcyt = 1 and
ρ−= 0, which are controlled by the details of the reaction term
Eq. 9. We thus assume a simple form for ρ(θ):
ρ(θ) =
(
ρ+,
|θ| ≤θ+/2
0,
otherwise
(23)
with θ+ indicating the angle of the cell over which ρ is equal to
ρ+, with 0 < θ+ < 2π. With this form,
ρn = ρ+
nπ sin
nθ+
2

.
(24)
Importantly, we can ﬁnd θ+ without explicitly solving the
reaction-diffusion equations.
Integrating Eq. 13 over the arc-
length and using Eq. 14, we ﬁnd a relationship between ρ, the cell
shape, and χ that is required for there to be a steady state shape,
2πχ =
Z L
0
ds(ρ −ρ∗),
(25)
where L ≈2πR0 + O(cn) is the cell perimeter. The integral over
the arc length s can be cast into one over the angle θ:
ds =
p
R(θ)2 + R′(θ)2dθ
(26)
=

R0 + g
X
cneinθ + O(c2
n)

dθ,
(27)
then the Eq. 25 becomes, up to linear order in cn,
2πχ =
Z π
−π
dθ(ρ −ρ∗)R0 + g
X
cnρ−n
= R0ρ+θ+ −2πR0ρ∗+ 2ρ+g
Xcn
n sin
nθ+
2

.
(28)
This equation is a link between cell shape and θ+ at steady state.
Expanding θ+ in cn as θ+ = θ+
0 + θ+
1 + · · · , where we assume
θ+
1 is O(cn), we ﬁnd
θ+
0 = 2π(χ + R0ρ∗)
R0ρ+
.
(29)
and
θ+
1 = −2
R0
g
Xcn
n sin
nθ+
0
2

.
(30)
Then the Fourier modes of ρ in Eq. 24 becomes, to linear order
again,
ρn = ρ+
nπ sin
nθ+
0
2

+ ρ+
2π cos
nθ+
0
2

θ+
1 .
If we look for the steady state of cn, which we will write cs.s.
n ,
we ﬁnd that, using Eq. 19,
χ
R2
0
(n2 −1)cs.s.
n −
v
2R0

(n + 1)cs.s.
n+1 −(n −1)cs.s.
n−1

(31)
= ρn(cs.s.
n )
which can be re-written as a simple matrix multiplication,
X
m̸=0±1
Anmcs.s.
m = gn
(32)
where
Anm = χ
R2
0
(n2 −1)δnm −mv
2R0
[δn+1,m −δn−1,m] + Bnm
Bn,m =
ρ+
mπR0
cos
nθ+
0
2

sin
mθ+
0
2

gn = ρ+
nπ sin
nθ+
0
2

where δmn is the Kronecker delta. Because v multiplies terms of
order cn, we can approximate it by
v ≈ρ1 + ρ−1
(33)
≈(2ρ+/π) sin
 θ+
0 /2

(34)
to zeroth order in cn (Eq. 22).
Eq. 32 may be solved to reconstruct cs.s.
n , and therefore R(θ),
by truncating to ﬁnite number Nmax of Fourier modes, n ∈


## Page 7


7
(−Nmax, · · · , −3, −2, 2, 3, · · · , Nmax). If we only take the n =
±2 modes, the answer is relatively simple,
cs.s.
±2 = ρ+
2π sin θ+
0
 3χ
R2
0
+ ρ+ sin 2θ+
0
2πR0
−1
(35)
This model, with the assumptions we have made, is straight-
forward to solve. However, it is not numerically exact because of
the assumption of quasi-circularity, cn/R0 ≪1. We compare the
Fourier series shapes with a sharp-interface determination of the
cell shape that does not require assuming cn/R0 ≪1 in Appendix
B 1.
3.
Dynamics of Perturbation from Steady-state Shape
In calculating the steady-state shape above, we have assumed
that the cell travels at a steady velocity in the ˆx direction. Our sim-
ulations show that turning begins from a near-steady-state shape.
To study this linear instability, we will calculate how the cell shape
relaxes if we slightly change the distribution of ρ(θ). If the orien-
tation of ρ(θ) changes by a small angle q, this is exactly the same
as if we slightly rotate our cell shape away from the x-axis, and
see how it relaxes. We assume that this process is dominated by
the dynamics of the lowest mode, n = ±2; we will thus look at
the dynamics of c2 when it takes on the form c2 = cs.s.
2 eiq(t) with
q(t) small, and neglect all other modes |n| > 2. We will also as-
sume that θ+ and v do not depend on q. With these assumptions,
we ﬁnd from Eq. 19 that, to linear order in q,
d
dtq = −3χ
R2
0
q.
(36)
We note that because we have limited ourselves to the n = ±2
modes, the relaxation dynamics of this rotation do not depend on
the cell’s velocity v.
C.
Predicted Phase Diagram
We can now predict when the cell should be stable or unstable.
Small perturbations of cell shape away from the direction of po-
larity relax with a rate 3χ/R2
0, as shown in Eq. 36. We also found
numerically that, in a ﬁxed cell shape with a distortion size of δ,
the front of the cell will move toward the narrow end of the cell
with a rate σ = bδPe−1 (Fig. 7 and Eq. 12). Combining these
results will show when the linear cell motion remains stable.
In our earlier results, computing the shape relaxation, we as-
sumed that the initial direction of polarity was θρ = 0, but this
is not necessary. Similarly in computing the instability of ρ in a
static cell shape, we assumed a stationary shape that is narrowed
along the x-axis, but we can rotate to consider the shape relative to
an arbitrary axis to get equivalent results. We can then generalize
our above results to
d
dtq = −3χ
R2
0
(q −θρ) ,
(37)
d
dtθρ = σ(θρ −q) .
(38)
Combining these equations, we ﬁnd that the linear stability of θρ−
q, i.e. the difference between the direction of chemical polarity ρ,
and the direction of shape polarity, q, is controlled by
d
dt(θρ −q) =

σ −3χ
R2
0

(θρ −q),
(39)
from which we can see that when σ < 3χ/R2
0, we expect our
straight-crawling cell to be stable to linear perturbations, and for
σ > 3χ/R2
0 we expect it to turn.
We established that σ = bδPe−1 = −2bcs.s.
2 Pe−1. Using our
simulations (Fig. 7), we estimate b ≈9.3724. The only other
crucial feature is the steady-state shape of the crawling cell cs.s.
2 ,
which we know by Eq. 35 – assuming once again that the cell
shape is dominated by the lowest n = ±2 mode. We then have
the bifurcation relation for marginal stability:
−bρ+
π
sin θ+
0
 3χ
R2
0
+ ρ+ sin 2θ+
0
2πR0
−1
Pe−1 = 3χ
R2
0
(40)
where ρ+ = 1, R0 = 1 and θ+
0 is set by Eq. 29.
We show slices of this phase diagram in Fig. 2 and Fig. 4.
The phase diagrams we compute are only roughly accurate, as
would be expected with the number of approximations that we
have made. However, we predict correctly both the order of mag-
nitude of the transitions, and that there should be a reentry as ρ∗
decreases, where for both small ρ∗and large ρ∗there is stability
(Fig. 4). However the theory also predicts a reentry for small χ;
this has not been observed in the simulations. This may be be-
cause as the tension χ becomes smaller, the cell shape becomes
less and less quasi-circular, and our assumptions fail.
VII.
DISCUSSION
We argue that the existence of turning and circular motion may
be quite generic in cell motility of the sort we have studied here,
with biochemical polarity mechanisms that create a single front.
Many other reaction-diffusion dynamics or other potential bio-
chemical models of the cell’s polarity [9] may display the at-
traction to high curvature which drives the instability we discuss
here. For instance, polarity driven by phase separation of two
non-miscible species [42] would also tend to minimize the inter-
face between these species. Related mechanisms, including phase
separation, and the constrained Allen-Cahn equation, are known
to display instabilities similar to that of Fig. 6 within ﬁxed geome-
tries [43–46]. Turing patterns may also be reoriented by curvature,
though in some reaction-diffusion systems, coupling to curvature
can be overwhelmed by initial conditions [47, 48]. We also note
that the coupling between shape and protein dynamics has been
emphasized recently in a Rho GTPase model wave pinning model
applied to dendritic spines [49], and cell shape-biochemistry inter-
actions have been observed in a broad range of models and exper-
iments [29, 50, 51]. In general, we would expect any mechanism
for ρ that displays an effective line tension at the region between
high and low ρ to be able to generate turning instabilities of the
type studied in our paper.
In addition, Ohta and Ohkuma [36] have argued from a sim-
ple model proposed on symmetry grounds that the transition to
circular motion is a generic property of active deformable parti-
cles, as long as there is a coupling between particle shape and
particle polarity. Our model provides a possible example of this
coupling in the context of cellular motility. However, the details
of our mechanical model shows that generic models of this sort
(e.g. [52–56]) can conceal surprises like reentry – it is not at all


## Page 8


8
straightforward to map physical properties of cells into the effec-
tive parameters. In particular, because the destabilizing effect of
the reaction-diffusion mechanism depends on the steady-state cell
shape, any parameter that controls cell shape can alter the stability
diagram, and cell shape may not be a simple monotonic function
of changing physical parameters.
Cell turning has been studied in other models [57, 58], though
primarily in a response to an altered stimulus – e.g. the rotation of
a chemoattractant gradient or an actin asymmetry. This is in con-
trast to our example, where turning occurs spontaneously. How-
ever, we do note that Ref. 57, observes a drifting behavior which
could be a transition into a very large-radius circular turn.
We have also observed turning and circular motion in the full
model of [4, 29], which includes ﬂuid ﬂow, separate dynamics for
myosin, and individual adhesions with stochastic transitions: see
Fig. S1 in the Supplementary Material of [29]. We have found that
decreasing Dρ (Da in [29]) also tends to stabilize the cell in the
more complex model. However, mechanical parameters do not
have as straightforward an effect as studied in the simple model
Eq. 8-10; in particular, we were unable to stabilize turning cells
by straightforwardly increasing tension.
How do our results on turning and circular motion compare
with experiments on cell motility? Recent work has shown that
multi-lobed keratocytes undergo circular motion [59], but with a
very different shape than the cells we simulate. In addition, Gore-
lik and Gautreau have recently suggested that arpin [60] may in-
duce cells to turn by slowing them [12]; this is consistent with
our result that slowing the cell (or decreasing the Peclet number)
can cause turning. However, we emphasize that in other cell types
turning is associated with different morphology and may not be
controlled by the simple mechanism studied here [61].
We predict, based on our analysis, that when our mechanism
applies, cell slowing will correspond with increased turning, but
by a different mechanism than the speed-persistence relationship
identiﬁed by [62]. Turning could potentially be prevented by re-
ducing the membrane diffusion coefﬁcient of polarity proteins on
the surface of the cell, e.g. by increasing their binding to the cor-
tex. We also argue that cell shape is a crucial mediator of turning:
wider cells would, in this mechanism, tend to be less stable. Any
interventions that alter cell tension, contractility at the cell rear, or
strength of protrusiveness, and thereby alter cell shape may dis-
rupt or induce turning.
VIII.
CONCLUSIONS
In this paper, we have presented a simpliﬁed variant of a phase
ﬁeld cell motility model, extending our earlier work [13, 15]. We
demonstrated that our model can support both straight and circu-
lar trajectories, with the circular trajectories occurring through a
turning instability. We have argued that this instability occurs be-
cause of the instability of the protein dynamics model we have
adapted [14] that tends to orient proteins within the cell toward
the cell’s narrower ends. When combination of the protein dy-
namics and cell shape dynamics leads to the cell widening, this
may lead to destabilization of the straight trajectory. Both our
model and our simple theory suggest that the phase diagram of
turning can be highly complex, with changing parameters having
non-monotonic effects on the stability: we observe that increas-
ing contractility ﬁrst destabilizes and then restabilizes the cell’s
straight trajectory.
Appendix A: Numerical Method
For the numerical method of the phase ﬁeld model (Eqs. 8-10),
we adopt the semi-implicit Fourier spectral method.
Let us consider a rectangular domain in R2:
Ω= {−Lx < x < Lx, −Ly < y < Ly}
and a periodic boundary condition is imposed for the problem. Let
us discretize the spatial domain Ωby a rectangular mesh which is
uniform in each direction as follows:
(xi, yj) = (−Lx + ihx, −Ly + jhy)
for 0 ≤i ≤Nx and 0 ≤j ≤Ny, hx = 2Lx/Nx and
hy = 2Ly/Ny. Let φij = φij(t) ≈φ(xi, yj, t), ρij = ρij(t) ≈
ρ(xi, yj, t) denote the approximate solutions. Then the set of un-
knowns are
Φ = (φij)0:Nx−1,0:Ny−1, U = (ρij)0:Nx−1,0:Ny−1.
The Laplacian operator in the spectral space corresponds to the
following spectrum
λij = −λ2
x(i) −λ2
y(j)
with
λx(i) =
(
π
Lx i,
0 ≤i ≤Nx/2,
π
Lx (Nx −i),
Nx/2 < i ≤Nx −1,
λy(j) =
( π
Ly j,
0 ≤j ≤Ny/2,
π
Ly (Ny −j),
Ny/2 < j ≤Ny −1.
For the Eq. 8, we can write it into the semi-implicit form:
φ(x, t + ∆t) −χ∆t∇2φ(x, t + ∆t) =
φ(x, t) + ∆t(ρ −ρ∗)|∇φ(x, t)| −χ∆t
ϵ2 G′(φ(x, t)).
By taking the fast Fourier transform of both sides of the above
equation, we get
(1 + χ∆tΛ) ⊙ˆΦ(t + ∆t) = FFT(R.H.S.)
where Λ = (λij)0:Nx−1,0:Ny−1 and ⊙stands for element-wise
multiplication between matrices. The approximate solution of φ
at t + ∆t can be obtained by taking inverse Fourier transform:
Φ(t + ∆t) = iFFT(ˆΦ(t + ∆t)).
Similarly for the Eq. 9, we can write it into the semi-implicit form
in terms of φρ,
(φρ)(x, t + ∆t) −Pe−1∆t∇2(φρ)(x, t + ∆t) =
(φρ)(x, t) −Pe−1∆t

∇· (ρ∇φ)

(x, t) + (φf)(x, t)
and then apply the FFT and iFFT to ﬁnd the approximate solution
of φρ at t + ∆t. The approximate solution U = (ρij) at t + ∆t is
obtained by:
ρij =
(
(φρ)ij/φij,
if φij ≥10−4,
(φρ)ij,
if φij < 10−4.
In our numerical simulations, we take Lx = Ly = 2.5, Nx =
Ny = 256 and ∆t = 5 × 10−4.


## Page 9


9
1.
Initial Conditions
Initially the cell shape is taken to be circular with radius R0 =
1, φ =
1
2 + 1
2 tanh [3(R0 −r)/ϵ] with ϵ = 0.1, and the ρ-
distribution equal to 0.8 in the front half and 0 in the rear half,
with an added normally-distributed noise with standard deviation
of 0.2.
Appendix B: Sharp interface models without the quasi-circularity
assumption
1.
Exact Calculation of Steady-state Shapes of Straight Cells
α ^n
v
α = −π
α = 0
α = π
x
y
s1
s2
FIG. 8. Schematic for the steady state of a straight crawling cell in the
sharp interface model. The curved arrow inside indicates the increasing
of arc-length s. The ratio of the width and height of the circumscribed
rectangle deﬁnes the aspect ratio of the cell.
We can ﬁnd a numerically exact solution to the steady-state
shape of the cell by integrating the sharp-interface equation
Eq. 13; related approaches, including graded radial extension
models, have been applied before [31, 63]. If we assume that the
cell is crawling along a straight trajectory with constant velocity
v = vˆy, where ˆy stands for the unit y-axis direction, then the rela-
tion between the cell velocity and cell shape can be obtained from
Eq. 13:
v cos α = (ρ −ρ∗) −χ ˙α
(B1)
where α is the angle counterclockwise from ˆn to v, see Fig. 8,
and the overhead dot represents the derivative with respect to the
arc-length s. We take the boundary conditions
α(0) = −π, α(L) = π
(B2)
which are appropriate if the cell perimeter is a simple closed
curve, and there is no cusp at s = 0 (Fig. 8). Given a solution
α(s), we can ﬁnd the cell shape by integrating the tangent vector
along the arclength,
˙x = cos α,
˙y = −sin α.
(B3)
Because the cell is a simple closed curve, we will ﬁnd that x(0) =
x(L) and y(0) = y(L).
The only unknown parameter in Eq. B1 is the cell’s velocity v,
if we specify the cell perimeter. The two boundary conditions of
Eq. B2 on the ﬁrst-order equation of Eq. B1 shows that, for a ﬁxed
value L, there will be only a particular value of v for which Eq. B1
can be solved.
We know from our simulations and the analysis of [14, 41] that
ρ has a sharp interface between values ρ+ and ρ−:
ρ(s) =
(
ρ+,
s1 < s < s2
ρ−,
s ≤s1 or s ≥s2
(B4)
where s1 = (L −L+)/2, s2 = (L + L+)/2 and L+ is the length
of the ρ+ region, see Fig. 8 in which the red part stands for the ρ+
region. How large is L+? Integrating Eq. B1 along the arc-length
and using Eq. 14, we ﬁnd that
2πχ =
Z L
0
ds(ρ −ρ∗) = L+ρ+ + (L −L+)ρ−−Lρ∗,
and then
L+ = 2πχ −L(ρ−−ρ∗)
ρ+ −ρ−
.
(B5)
In practice, ρ+ = 1 and ρ−= 0 are appropriate for our reaction-
diffusion equations.
Eq. B1 coupled with the boundary conditions of B2 is numer-
ically solved by using a shooting method to determine the value
of v for which the equations can be solved. As an example, we
choose L = 2π. We compare this result with our quasicircular
approximation in Fig. 9, seeing generally good agreement on cell
shape and size. Even using the model with only N = 2 Fourier
modes, we capture the appropriate trends of cell shape. We choose
R0 = 1 in the quasicircular approximation (Eq. 15); this is set so
that the cell’s contour length L in the quasicircular approxima-
tion L ≈2πR0 matches that for the numerically exact method.
(We note that the agreement between contour lengths is only ap-
proximate, and the contour length of some cells shown in Fig. 9
can deviate from 2π.) Velocities predicted by the Fourier model
are also in good agreement with those predicted by the numeri-
cally exact model, with errors of less than 25% for the parameters
shown in Fig. 9, even only including N = 2 modes.
The sharp interface solutions also have good agreement with the
phase ﬁeld solutions (Fig. 10). However, this agreement depends
on the validity of our assumptions, e.g. that the value of ρ at the
cell front is unity. This is controlled by K. Mathematically, K
resembles a penalty constant to maintain ρ−= 0, ρ+ = 1 (Eq. 9).
As K becomes greater, ρ+ becomes closer to 1 and the phase ﬁeld
cell shrinks to the sharp interface one.
2.
Exact Calculation of Steady-state Shape of Cells with Circular
Trajectories
While we only used the sharp-interface results in the main paper
to determine the steady-state shape of cells on straight trajectories,
our techniques can also be used to determine the shape of cells
undergoing circular motion. Schematically, we show a circularly
moving cell in steady state in Fig. 11. The origin O is the center of
rotation, Q is a representative point on the cell boundary, τ is the
angle made by OQ from horizontal, β is the angle of inclination
from horizontal, ˆn is the normal to the cell boundary, and v is
the moving direction of Q which is normal to OQ. The blue curve
represents the ρ−region and the red part is ρ+ region. The point P
is the middle point of the blue ρ−region with respect to arc-length
and is taken as the starting point for arc-length parameterization,
namely, s = 0 at P. Note that the cell shape is independent of
angle ψ1, so in the sharp-interface model, we take ψ1 = π/2 to


## Page 10


10
FIG. 9. Comparison between numerically exact calculation of sharp-interface cell shapes and the quasicircular approximations. Solid lines are the
numerically exact calculation, blue crosses are the quasicircular model with N = 2, and green dots are the quasicircular model with N = 100. In this
ﬁgure, cells are shown with their velocity along the positive y direction. The values of χ are χ = 0.2, 0.3, 0.4 and ρ∗= 0.2, 0.35, 0.5. L = 2π is the
perimeter for the numerically exact results, and R0 = 1 for the quasicircular calculations. Details of numerical calculation are in Section B 1.
FIG. 10. Comparison between sharp interface solution and phase ﬁeld solutions. The parameter K = 500, 2000, 4000 from left to right. The other
parameter values are χ = 0.26, Pe−1 = 0.30, ρ∗= 0.40, C = 6, m = 0.5 and ϵ = 0.1. Color plots indicate the phase ﬁeld, dashed line the
sharp-interface results. Lengths for each value of K (listed above the image) are taken from the corresponding phase ﬁeld simulations.
O
P
Q
 1
v
τ
β
β −τ
x
y
β0
^n
FIG. 11. Schematic for the steady state of a circularly crawling cell in the
sharp interface model.
keep P on the y-axis. The angle between ˆn and v is β −τ and the
normal velocity
vn = ω0
p
x2 + y2 cos(β −τ),
(B6)
where ω0 is the constant angular velocity for the cell in circular
steady state. Then in the circular steady state, we have
ω0
p
x2 + y2 cos(β −τ) = (ρ −ρ∗) −χ ˙β
⇒ω0
p
x2 + y2 (cos τ cos β + sin τ sin β) = ρ −ρ∗−χ ˙β
⇒ω0 (x cos β + y sin β) = ρ −ρ∗−χ ˙β.
(B7)
Notice that
x cos β + y sin β = 1
2(x2 + y2)·,
Integrating Eq. B7 along the arclength, we ﬁnd that
2πχ =
Z L
0
(ρ −ρ∗) ds,
exactly as what we obtain from the equation for the straightly
moving cell.


## Page 11


11
0
0.5
1
0
0.5
1
1.5
2 χ = 0.12
0
0.5
1
0
0.5
1
1.5
2 χ = 0.18
FIG. 12.
(Color online) Exactly calculated sharp-interface cell shape
in circular steady state. The tension χ = 0.12 (left) and 0.18 (right).
The values of angular velocity ω0 and the radius of the circular orbit are
obtained from phase ﬁeld simulations (8-10): ω0 = 0.5775 (left) and
0.3832 (right), R0 = 1.0530 (left) and 1.3563 (right). Other parameters
are ρ∗= 0.4.
Finally we obtain the system for steady state of circular cells:
ω0 (x cos β + y sin β) = ρ −ρ∗−χ ˙β,
(B8)
˙x = cos β,
˙y = sin β,
with the following boundary conditions
β(0) = β0,
x(0) = 0,
y(0) = R0.
(B9)
β(L) = β0 + 2π,
x(L) = x(0),
y(L) = y(0).
(B10)
Note that for the boundary conditions (B10) at s = L, x(L) =
x(0) and y(L) = y(0) automatically implies β(L) = β0 + 2π by
considering (13), (14) and (B8), so β(L) is a redundant boundary
condition. Besides, the cell perimeter L and the initial inclina-
tion angle β0 are two unknown parameters, so the number of un-
knowns matches with the number of boundary conditions in (B8-
B10). The length L+ of the ρ+ region is determined by Eq. B5,
which is treated known once L is determined.
Numerically, we solve the Eq. B8 coupled with boundary con-
ditions (B9-B10) by a shooting method. The parameter values are
ρ∗= 0.4, χ = 0.12 (0.18, respectively), R0 = 1.0530 (1.3563,
respectively) and ω0 = 0.5775 (0.3832, respectively) where the
cell’s angular velocity ω0 and circular radius R0 are taken from
the phase ﬁeld simulations (8-10). As in the earlier sharp inter-
face limit calculations, we take ρ+ = 1, ρ−= 0. The numerical
results are presented in Fig. 12 which have good agreement with
the phase ﬁeld simulations.
[1] Dennis Bray. Cell movements: from molecules to motility. Garland
Science, 2001.
[2] Alex Mogilner and George Oster. Force generation by actin poly-
merization ii: the elastic ratchet and tethered ﬁlaments. Biophysical
Journal, 84(3):1591, 2003.
[3] Longhua Hu and Garegin A Papoian. Mechano-chemical feedbacks
regulate actin mesh growth in lamellipodial protrusions. Biophysical
Journal, 98(8):1375, 2010.
[4] D. Shao, H. Levine, and W.-J. Rappel. Coupling actin ﬂow, adhe-
sion, and morphology in a computational cell motility model. Pro-
ceedings of the National Academy of Sciences, 109(18):6851, 2012.
[5] B. Rubinstein, M.F. Fournier, K. Jacobson, A.B. Verkhovsky, and
A. Mogilner.
Actin-myosin viscoelastic ﬂow in the keratocyte
lamellipod. Biophysical Journal, 97(7):1853, 2009.
[6] Marc Herant and Micah Dembo. Form and function in cell motility:
from ﬁbroblasts to keratocytes. Biophysical Journal, 98(8):1408,
2010.
[7] Charles W Wolgemuth, Jelena Stajic, and Alex Mogilner. Redun-
dant mechanisms for stable cell locomotion revealed by minimal
models. Biophysical Journal, 101(3):545–553, 2011.
[8] Athanasius FM Mar´ee, Verˆonica A Grieneisen, and Leah Edelstein-
Keshet. How cells integrate complex stimuli: the effect of feed-
back from phosphoinositides and cell shape on cell polarization and
motility. PLoS Computational Biology, 8(3):e1002402, 2012.
[9] Alexandra Jilkine and Leah Edelstein-Keshet.
A comparison of
mathematical models for polarization of single eukaryotic cells
in response to guided cues.
PLoS Computational Biology, 7(4):
e1001121, 2011.
[10] William R Holmes and Leah Edelstein-Keshet. A comparison of
computational models for eukaryotic cell shape and motility. PLoS
Computational Biology, 8(12):e1002793, 2012.
[11] Falko Ziebert and Igor S Aranson.
Computational approaches
to substrate-based cell motility. npj Computational Materials, 2:
16019, 2016.
[12] Roman Gorelik and Alexis Gautreau. The arp2/3 inhibitory protein
arpin induces cell turning by pausing cell migration. Cytoskeleton,
72(7):362, 2015.
[13] Danying Shao, Wouter-Jan Rappel, and Herbert Levine. Compu-
tational model for cell morphodynamics. Physical Review Letters,
105(10):108104, 2010.
[14] Y. Mori, A. Jilkine, and L. Edelstein-Keshet.
Wave-pinning and
cell polarity from a bistable reaction-diffusion system. Biophysical
Journal, 94(9):3684, 2008.
[15] Brian A Camley, Yunsong Zhang, Yanxiang Zhao, Bo Li, Eshel
Ben-Jacob, Herbert Levine, and Wouter-Jan Rappel. Polarity mech-
anisms such as contact inhibition of locomotion regulate persistent
rotational motion of mammalian cells on micropatterns. Proceed-
ings of the National Academy of Sciences, page 201414498, 2014.
[16] WJ Boettinger, JA Warren, C Beckermann, and A Karma. Phase-
ﬁeld simulation of solidiﬁcation 1. Annual Review of Materials Re-
search, 32(1):163–194, 2002.
[17] Joseph B Collins and Herbert Levine. Diffuse interface model of
diffusion-limited crystal growth. Physical Review B, 31(9):6119,
1985.
[18] Thierry Biben, Klaus Kassner, and Chaouqi Misbah. Phase-ﬁeld
approach to three-dimensional vesicle dynamics. Physical Review
E, 72(4):041921, 2005.
[19] Falko Ziebert, Sumanth Swaminathan, and Igor S Aranson. Model
for self-polarization and motility of keratocyte fragments. J. Roy.
Soc. Interface, 9(70):1084–1092, 2012.
[20] Jakob L¨ober, Falko Ziebert, and Igor S Aranson. Modeling crawling
cell movement on soft engineered substrates. Soft matter, 10(9):
1365–1373, 2014.
[21] Jakob L¨ober, Falko Ziebert, and Igor S Aranson. Collisions of de-
formable cells lead to collective migration. Scientiﬁc Reports, 5,
2015.
[22] Benoit Palmieri, Yony Bresler, Denis Wirtz, and Martin Grant. Mul-
tiple scale model for cell migration in monolayers: Elastic mismatch
between cells enhances motility. Scientiﬁc Reports, 5, 2015.
[23] Elsen Tjhung, Davide Marenduzzo, and Michael E Cates. Sponta-


## Page 12


12
neous symmetry breaking in active droplets provides a generic route
to motility. Proceedings of the National Academy of Sciences, 109
(31):12381, 2012.
[24] E Tjhung, A Tiribocchi, D Marenduzzo, and ME Cates. A mini-
mal physical model captures the shapes of crawling cells. Nature
Communications, 6, 2015.
[25] Yi I Wu, Daniel Frey, Oana I Lungu, Angelika Jaehrig, Ilme
Schlichting, Brian Kuhlman, and Klaus M Hahn.
A genetically
encoded photoactivatable Rac controls the motility of living cells.
Nature, 461(7260):104, 2009.
[26] Marten Postma, Leonard Bosgraaf, Harri¨et M Loovers, and Pe-
ter JM Van Haastert. Chemotaxis: signalling modules join hands
at front and tail. EMBO Reports, 5(1):35, 2004.
[27] Julien Kockelkoren, Herbert Levine, and Wouter-Jan Rappel. Com-
putational approach for modeling intra-and extracellular dynamics.
Physical Review E, 68(3):037702, 2003.
[28] X Li, J Lowengrub, A R¨atz, and A Voigt. Solving PDEs in com-
plex geometries: a diffuse domain approach. Communications in
Mathematical Sciences, 7(1):81, 2009.
[29] Brian A Camley, Yanxiang Zhao, Bo Li, Herbert Levine, and
Wouter-Jan Rappel. Periodic migration in a physical model of cells
on micropatterns. Physical Review Letters, 111(15):158102, 2013.
[30] Alexander B Verkhovsky, Tatyana M Svitkina, and Gary G Borisy.
Self-polarization and directional motility of cytoplasm. Current Bi-
ology, 9(1):11, 1999.
[31] Kinneret Keren, Zachary Pincus, Greg M Allen, Erin L Barnhart,
Gerard Marriott, Alex Mogilner, and Julie A Theriot. Mechanism
of shape determination in motile cells. Nature, 453(7194):475–480,
2008.
[32] Erin L Barnhart, Kun-Chun Lee, Kinneret Keren, Alex Mogilner,
and Julie A Theriot. An adhesion-dependent switch between mech-
anisms that determine motile cell shape.
PLoS Biology, 9(5):
e1001059, 2011.
[33] Kinneret Keren and Julie A Theriot. Biophysical aspects of actin-
based cell motility in ﬁsh epithelial keratocytes. In Cell Motility,
page 31. Springer, 2008.
[34] Yasushi Sako,
Kayo Hibino,
Takayuki Miyauchi,
Yoshikazu
Miyamoto, Masahiro Ueda, and Toshio Yanagida. Single-molecule
imaging of signaling molecules in living cells. Single Molecules, 1
(2):159, 2000.
[35] Alexandra Jilkine. A wave-pinning mechanism for eukaryotic cell
polarization based on Rho GTPase dynamics. PhD thesis, Univer-
sity of British Columbia (Vancouver), 2009.
[36] Takao Ohta and Takahiro Ohkuma. Deformable self-propelled par-
ticles. Physical Review Letters, 102(15):154101, 2009.
[37] Ben Vanderlei, James J Feng, and Leah Edelstein-Keshet. A compu-
tational model of cell polarization and motility coupling mechanics
and biochemistry. Multiscale Modeling and Simulation, 4(9):1420–
1443, 2011.
[38] KR Elder, Martin Grant, Nikolas Provatas, and JM Kosterlitz. Sharp
interface limits of phase-ﬁeld models. Physical Review E, 64(2):
021604, 2001.
[39] Tao Han and Mikko Haataja. Comprehensive analysis of compo-
sitional interface ﬂuctuations in planar lipid bilayer membranes.
Physical Review E, 84(5):051903, 2011.
[40] Takao Ohta, Takahiro Ohkuma, and Kyohei Shitara. Deformation
of a self-propelled domain in an excitable reaction-diffusion system.
Physical Review E, 80(5):056203, 2009.
[41] Y. Mori, A. Jilkine, and L. Edelstein-Keshet. Asymptotic and bi-
furcation analysis of wave-pinning in a reaction-diffusion model for
cell polarization.
SIAM Journal on Applied Mathematics, 71(4):
1401, 2011.
[42] Marco Zamparo, F Chianale, Claudio Tebaldi, M Cosentino-
Lagomarsino, M Nicodemi, and A Gamba.
Dynamic membrane
patterning, signal localization and polarity in living cells. Soft Mat-
ter, 11(5):838, 2015.
[43] Nicholas D Alikakos, Xinfu Chen, and Giorgio Fusco. Motion of a
droplet by surface tension along the boundary. Calculus of Varia-
tions and Partial Differential Equations, 11(3):233–305, 2000.
[44] Doug Stafford, Michael J Ward, and Brian Wetton. The dynamics of
drops and attached interfaces for the constrained Allen–Cahn equa-
tion. European Journal of Applied Mathematics, 12(01):1, 2001.
[45] Nicholas D Alikakos, Peter W Bates, Xinfu Chen, and Giorgio
Fusco. Mullins-Sekerka motion of small droplets on a ﬁxed bound-
ary. Journal of Geometric Analysis, 10(4):575, 2000.
[46] Davide Marenduzzo and Enzo Orlandini. Phase separation dynam-
ics on curved surfaces. Soft Matter, 9(4):1178, 2013.
[47] E Orlandini, D Marenduzzo, and AB Goryachev. Domain formation
on curved membranes: phase separation or Turing patterns?
Soft
Matter, 9(39):9311, 2013.
[48] Giulio Vandin, Davide Marenduzzo, Andrew B Goryachev, and
Enzo Orlandini.
Curvature-driven positioning of Turing patterns
in phase-separating curved membranes. Soft Matter, 12(17):3888,
2016.
[49] Samuel A Ramirez, Sridhar Raghavachari, and Daniel J Lew. Den-
dritic spine geometry can localize GTPase signaling in neurons.
Molecular Biology of the Cell, 26(22):4171, 2015.
[50] William R Holmes, Benjamin Lin, Andre Levchenko, and Leah
Edelstein-Keshet. Modelling cell polarization driven by synthetic
spatially graded rac activation. PLoS Computational Biology, 8(6):
e1002366, 2012.
[51] Jason Meyers, Jennifer Craig, and David J Odde. Potential for con-
trol of signaling pathways via cell size and shape. Current Biology,
16(17):1685–1693, 2006.
[52] Takao Ohta, Mitsusuke Tarama, and Masaki Sano. Simple model of
cell crawling. Physica D: Nonlinear Phenomena, 318:3, 2016.
[53] Mitsusuke Tarama and Takao Ohta. Oscillatory motions of an active
deformable particle. Physical Review E, 87(6):062912, 2013.
[54] Mitsusuke Tarama and Takao Ohta.
Spinning motion of a de-
formable self-propelled particle in two dimensions.
Journal of
Physics: Condensed Matter, 24(46):464129, 2012.
[55] Andreas M Menzel and Takao Ohta. Soft deformable self-propelled
particles. EPL (Europhysics Letters), 99(5):58001, 2012.
[56] T Hiraiwa, MY Matsuo, T Ohkuma, T Ohta, and M Sano. Dynamics
of a deformable self-propelled domain. EPL (Europhysics Letters),
91(2):20001, 2010.
[57] Athanasius FM Mar´ee,
Alexandra Jilkine,
Adriana Dawes,
Verˆonica A Grieneisen, and Leah Edelstein-Keshet.
Polarization
and movement of keratocytes: a multiscale modelling approach.
Bulletin of Mathematical Biology, 68(5):1169, 2006.
[58] A Mogilner and B Rubinstein. Actin disassembly’clock’and mem-
brane tension determine cell shape and turning: a mathematical
model.
Journal of Physics: Condensed Matter, 22(19):194118,
2010.
[59] Franck Raynaud,
Mark E Amb¨uhl,
Chiara Gabella,
Alicia
Bornert, Ivo F Sbalzarini, Jean-Jacques Meister, and Alexander B
Verkhovsky. Minimal model for spontaneous cell polarization and
edge activity in oscillating, rotating and migrating cells.
Nature
Physics, 12(4):367, 2016.
[60] Irene Dang, Roman Gorelik, Carla Sousa-Blin, Emmanuel Derivery,
Christophe Gu´erin, Joern Linkner, Maria Nemethova, Julien G Du-
mortier, Florence A Giger, Tamara A Chipysheva, et al. Inhibitory
signalling to the Arp2/3 complex steers cell migration. Nature, 503
(7475):281, 2013.
[61] Xiaji Liu, Erik S Welf, and Jason M Haugh. Linking morphodynam-
ics and directional persistence of T lymphocyte migration. Journal
of The Royal Society Interface, 12(106):20141412, 2015.
[62] Paolo Maiuri, Jean-Franc¸ois Rupprecht, Stefan Wieser, Verena
Ruprecht, Olivier B´enichou, Nicolas Carpi, Mathieu Coppey, Simon
De Beco, Nir Gov, Carl-Philipp Heisenberg, et al. Actin ﬂows me-
diate a universal coupling between cell speed and cell persistence.
Cell, 161(2):374, 2015.
[63] Yair Adler and SeﬁGivli. Closing the loop: Lamellipodia dynamics
from the perspective of front propagation. Physical Review E, 88
(4):042708, 2013.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1608.07218v2
source: arxiv
tags: [arxiv, knowledge, math, quantum, reference]
---
# 1608.07218v2_Pattern_formation_in_polymerising_actin_flocks__spirals__spots_and_waves_without

> Source: 1608.07218v2_Pattern_formation_in_polymerising_actin_flocks__spirals__spots_and_waves_without.pdf

> Pages: 7

---


## Page 1


Pattern formation in polymerising actin ﬂocks: spirals, spots and waves without
nonlinear chemistry
T. Le Goﬀ∗, B. Liebchen†, D. Marenduzzo‡
SUPA, School of Physics and Astronomy, University of Edinburgh,
Peter Guthrie Tait Road, Edinburgh, EH9 3FD, UK
We propose a model solely based on actin treadmilling and polymerisation which describes many
characteristic states of actin wave formation: spots, spirals and travelling waves. In our model, as
in experiments on cell recovering motility following actin depolymerisation, we choose an isotropic
low density initial condition; polymerisation of actin ﬁlaments then raises the density towards the
Onsager threshold where they align. We show that this alignment, in turn, destabilizes the isotropic
phase and generically induces transient actin spots or spirals as part of the dynamical pathway
towards a polarized phase which can either be uniform or consist of a series of actin-wave trains
(ﬂocks).
Our results uncover a universal route to actin wave formation in the absence of any
system speciﬁc nonlinear biochemistry, and it may help understand the mechanism underlying the
observation of actin spots and waves in vivo. They also suggest a minimal setup to design similar
patterns in vitro.
PACS numbers:
Actin networks are highly dynamic subcellular struc-
tures which constitute a key component of the cytoskele-
ton of eukaryotic cells [1]. These cells can be viewed as
crosslinked gels made up from actin ﬁlaments, i.e. semi-
ﬂexible protein polymers with persistence and contour
lengths both typically in the 1 −10 µm range.
Actin
ﬁlaments are active polymers which function far from
thermodynamic equilibrium, as they constantly turn over
their components, actin monomers, through polymerisa-
tion and depolymerisation [1, 2].
Under physiological
conditions, the actin cytoskeleton forms a cortex just be-
low the cell membrane, and it exploits polymerisation to
power cellular motility [3], e.g. when a cell crawls on a
substrate.
Actin ﬁlaments and networks self-organize into a vari-
ety of mesmerising patterns [4–6]. In vitro, experiments
have reported the formation of lanes, waves and spirals in
systems where actin ﬁbers of constant length walk on a
carpet of immobilised molecular motors [4]. In vivo, the
actin network of a cell is normally localized within a µm-
wide cortex trailing just behind the advancing membrane
of a moving cell. However, under particular conditions,
actin ﬁbers reorganize within the cell, and create diﬀerent
patterns, such as travelling or scroll waves [5–9].
In some cases, the mechanism through which actin
waves arise is relatively well understood, and is given
by a network of biochemical regulatory reactions involv-
ing actin-associated proteins [10], which can be eﬀec-
tively modeled as an activator-inhibitor dynamical sys-
tem. Such models, based on nonlinear biochemistry, suc-
cessfully explain cases where actin waves are associated
∗thomas.le-goﬀ@ed.ac.uk
†bliebche@staﬀmail.ed.ac.uk
‡dmarendu@ph.ed.ac.uk
with the activation of the SCAR-WAVE complex [11],
and they are linked to chemotaxis [12]. However, there
are other examples where waves depend on only a small
number of components. Most relevant to our work are
the waves observed in Dictyostelium cells recovering from
treatment with latrunculin, which causes mass depoly-
merisation of actin ﬁbers [5, 6].
When latrunculin is
taken away, actin ﬁbers repolymerise from monomers in
the cytosol, and after this cells recover motility: they do
so by undergoing a surprisingly complex pattern forma-
tion cascade. First, actin assembles into transient spots,
which then evolve into waves; spiral patterns are also
observed in some cases. A set of experiments knocking
out several actin-associated proteins clariﬁed that the dy-
namics leading to waves is not dependent, among others,
on the SCAR-WAVE complex, or on contractile myosin
motors [6].
The waves observed in Ref. [5] have to date been ad-
dressed by a number of models in the literature [13–
17]. All these works lead to wave formation, and all in-
clude some nonlinear dynamics, such as the Fitz-Nagumo
model [13], or other activator-inhibitor models [14]. This
choice is often motivated by the observation that some
actin-associated proteins are found in waves – most no-
tably, coronin, which localizes at the rear of a wave, and
myosin I, which lies at the front [6]. While these are all
perfectly plausible models, they either rely on the exis-
tence of a delay, or on (cubic) nonlinear reaction terms
which are generally quite system speciﬁc.
Here we suggest an alternative model for wave forma-
tion, which does not require any nonlinear biochemistry,
and solely depends on three simple and generic ingre-
dients:
actin polymerisation, steric repulsion between
actin ﬁbres, and treadmilling (i.e., the eﬀective motion
of actin ﬁbres which grow at one end and shrink at the
other one [1, 2]). Since all three ingredients occur in a
arXiv:1608.07218v2  [cond-mat.soft]  26 Aug 2016


## Page 2


2
wide class of systems featuring actin waves, our ﬁndings
suggest that spots and waves could hinge on a universal
mechanism and do not, as the current literature suggests,
require system speciﬁc nonlinear chemistry.
This key
ﬁnding should be of particular relevance for the current
understanding of waves in Dictyostelium in vivo; they
also suggest how to set up experiments in vitro to gener-
ate similar patterns.
In our model actin ﬁlaments “ﬂock” [18]: they align
when dense enough, due to excluded volume interactions
(like rigid rods in the Onsager theory for nematic liquid
crystals [19]), and they move due to treadmilling, leading
to actin waves. At the low initial ﬁber densities typical
of the early stages of experiments in Dictyostelium, how-
ever, alignment interactions are ineﬀective. As a prelimi-
nary step to wave formation, polymerisation increases the
ﬁbre density. Here, we unveil that spot formation, which
is frequently observed in experiments prior to waves [5],
does not require complex reaction-based instabilities but
occurs generically as part of the dynamical pathway from
the isotropic to the ﬂocking phase. Here polymerisation
shapes the morphology of the emerging waves, and allows
controlling their lengthscale.
To specify our qualitative arguments, we now propose
a dynamical model to study pattern formation in a sys-
tem of polymerising actin ﬁbers, where we follow both
the density of F-actin ﬁlaments, ρ, and their average po-
larisation (i.e., the sum of orientation unit vectors per
unit volume), P. The equations of motion deﬁning our
model read as follows:
∂tρ = −v0∇.(ρP) + Dρ∇2ρ + αρ

1 −ρ
ρ0

(1)
∂tP = γ
 ρ
ρc
−1

P + K∇2P −γ2P 2P.
(2)
Here Dρ is the diﬀusion coeﬃcient for F-actin, K is an ef-
fective elastic constant, while v0 and α denote the tread-
milling speed and the polymerisation rate respectively.
Further, γ measures how fast F-actin ﬁlaments change
their direction, the term in γ2 ensures saturation of the
polarisation, whereas ρc and ρ0 indicate respectively the
critical density above which nematic order sets in, and
the target polymerisation density (i.e., the density of F-
actin which would be reached due to polymerisation in a
well-stirred system in the absence of spatial eﬀects). For
α = 0, Eqs. (1,2) are related to the models of Refs. [20–
23], although even in that limit our emphasis here is on
the dynamical pathway the system follows, rather than
on steady state behaviour.
It is also useful to recast Eqs. (1,2) in terms of dimen-
sionless variables, as follows,
∂tρ = −∇.(ρP) + ∇2ρ + ρ (1 −ρ)
(3)
∂tP = Γ (rρ −1) P + D∇2P −Γ2P 2P,
(4)
where we have deﬁned Γ = γ/α, r = ρ0/ρc, D = K/Dρ,
Γ2 = γ2Dρ/v2
0, and we have further redeﬁned t →αt,
t = 16.2
t = 243
t = 486
1
1.6
1.4
1.2
(a)
t = 100
t = 1000
t = 1500
(b)
1
2
3
4
t = 76.5
t = 117
1
2
3
(c)
t = 81
FIG. 1: Representative snapshots for actin pattern formation,
time increasing from left to right. (a) Γ = 1: an actin spot
forms and then disappears. (b) Γ = 4.3: spiralling spots form
early on; they then decay and are replaced by a regular wave
train. (c) Γ = 10: spots are polarised, and the ﬁnal actin
waves are irregular. Other parameters: r = 1.1, D = 5 and
Γ2 = 0.075. The scale bar is 50.
x →(α/Dρ)1/2x, ρ →ρ/ρ0 and P →(v0/
p
Dρα)P, so
as to have dimensionless time, space, density and polar-
isation. Eqs. (3,4) also clarify that the dynamics of our
model depends on four dimensionless parameters – while
we have varied all of these, we have found that Γ, which
is the ratio between alignment and polymerisation rate,
is our key control parameter (provided that r > 1). To
provide an overview over the possible patterns in this
system, we vary this parameter in the following while
keeping other parameters at values given in the caption
of Fig. 1. It is useful to estimate the orders of magnitude
of parameter values which are relevant to experiments.
In vivo or in the lab, actin may polymerise at a rate
α ∼1 −100 s−1 [2, 24], while γ may be estimated as
the rotational diﬀusion of an intracellular F-actin ﬁla-
ment of typical geometry ∼1µm × ∼5 nm, which is
∼10 s−1 [24]. For this geometry, the Onsager threshold
of actin ﬁbers can be estimated as 0.5% in volume frac-
tion – the inverse of their aspect ratio – whereas the ﬁber
density in a cell is up to ∼10 g/l [25], or ∼1% in volume
fraction. As a result, an experimentally relevant range of
parameters is Γ ∼0.1 −10, and r > 1.
We have solved Eqs. (3,4) for diﬀerent values of Γ on
a square lattice of size Lx × Ly using ﬁnite diﬀerence
methods, periodic boundary conditions and a uniform
initial state {ρ, p} = (0, 0) plus some small ﬂuctuations.
For identical polymerisation and alignment rate (Γ = 1),
we initially observe a uniform density growth followed,


## Page 3


3
t = 85
Lx = 250
Ly = 250
t = 87.5
t = 95
FIG. 2: Snapshots of the evolution of the P-ﬁeld during the
formation of spots for Γ = 4.3, r = 1.1, D = 5 and Γ2 = 0.075,
shown in Fig. 1b.
Γ
R(λ)
1
0
−1
−2
−3
0
0.4
0.8
1.2
q
0
0.4
0.8
1.2
q
Γ
I(λ)
0
−5
−10
−15
−20
FIG. 3: Real and imaginary parts of dispersion relation of
small ﬂuctuations around the uniform phase, for Γ from 0 to
10 with r = 1.1, D = 5 and Γ2 = 0.075.
after a certain lag time, by the formation of one or sev-
eral spots growing out of the uniform phase (Fig. 1a and
video 1 in SM). These spots have a spiral-like orientation
of the actin ﬁbres (Fig. 1a, inset). Remarkably, they are
not stable, but decay after a lifetime of about 200 poly-
merisation cycles back to the uniform state. If ﬁbres align
faster than new ones are polymerised (Γ = 4.3), we again
observe transient spot formation. Intriguingly, however,
here we do not end up with a uniform phase but observe
the emergence of travelling actin waves. These waves self-
arrange into a pattern with a well-deﬁned length scale
(Fig.
1b and video 2 in SM). Further enhancing the
alignment rate (Γ = 10) again leads to the formation of
spots. Here, however, the spots are less pronounced and
start to spiral and move while growing [24]; they continu-
ously transforms into travelling waves (Fig. 1c and video
3 in SM). Further enhancing Γ directly leads to waves
without a preceding spot stage.
Therefore, strikingly,
our simple and generic model accounts for the sequence
of actin patterns, from spots to waves, observed experi-
mentally [5, 6]. We now want to understand why spots
and then waves emerge.
To this end, we now perform a linear stability anal-
ysis of our equations of motion (providing results here
in physical units).
We note that the present system
has three uniform solutions.
These are:
(i) (ρ, p) =
(0, 0) (which we chose as our initial state, following in-
vivo experiments), (ii) (ρ, p) = (ρ0, 0), (iii) (ρ, p) =
(ρ0,
p
(γ/γ2)(ρ0/ρc −1)e), where e represents a unit vec-
tor pointing in a spontaneously chosen direction set by
the initial conditions. All solutions correspond to uni-
form phases: the ﬁrst two are unpolarized, the third is
polarized, hence travelling (ﬂocking). First, we explore
the stability of our initial low density state. The dom-
inant branch of the dispersion relation of ﬂuctuations
around this phase reads λ = α −Dρq2: therefore our
initial state is generally unstable against polymerisation,
simply leading to a density growth in the whole system
if α > 0 (with no eﬀect on the polarization ﬁeld, as the
eigenmode of the unstable mode is orthogonal to p). This
density growth proceeds until we have ρ = ρc; i.e. poly-
merisation generally transfers the system from phase (i)
to phase (ii).
Conversely to phase (i), for ρ0 > ρc, alignment inter-
actions become eﬀective in phase (ii), i.e.
they domi-
nate over rotational diﬀusion – see Eq. 2. This can be
seen from the dominant branch of the dispersion relation,
λ = γ(ρ0/ρc −1) −Kq2 (see SM), of ﬂuctuations in this
phase, which yields a stationary long wavelength insta-
bility. Notably, alignment interactions are strong enough
here to generate an instability of the uniform unpolar-
ized phase but too weak to generate waves (which would
require an oscillatory instability). Following this instabil-
ity, the dynamical pathway of our system is subtle and
can be described as follows.
Actin ﬁbres align locally,
leading to polarized domains, with the polarization ﬁeld
of each domain pointing in a spontaneously chosen direc-
tion. Due to treadmilling each of these domains moves,
but soon ’collides’ with other domains of aligned ﬁbres,
resulting in a defect in the p ﬁeld with ingoing ﬁbre-
density ﬂux from all directions (see Fig.
2), which in
turn generates a spot in the density ﬁeld (Fig. 1a,b).
This scenario is a natural and generic consequence of
the instability of phase (ii) and therefore part of the dy-
namic pathway followed by our system, when initialised
in phase (i).
We determined the length scale of the
spots, l, by a combination of linear stability analysis (see
SM) and systematic parameter sweeps, and found that
l ∼
p
K/(γ(ρ0/ρc −1))(γ2Dρ/v2
0)1/4. Hence, the typi-
cal spot size increases with diﬀusion but decreases with
self-propulsion velocity. This scaling is intuitive, since ﬁ-
bres treadmill from all directions towards the spot center
thereby competing with diﬀusion (a similar scaling, albeit
leading to a distinct functional form for l, determined
the size of aster size in [21]). Remarkably, we found that
for γ2Dρ/v2
0 > 1 the spot size converges to a healing
length l ∼
p
K/(γ(ρ0/ρc −1)) representing the distance
needed for the polarization ﬁeld to recover from a local
orientational perturbation (defect). We note that, in the
absence of polymerisation (α = 0), our asters satisfy the
steady state condition of Eq. 1 ( ˙ρ = 0) yielding a solution
p ∝∇ρ/ρ where ﬁbre treadmill up the density gradient
thereby permanently balancing diﬀusive ﬁbre losses. Im-
portantly, however, the local density in the spot exceeds
ρ0, leading for α > 0 to depolymerisation. This in turn
initiates Fisher waves travelling from the spot in all direc-
tions. We expect these Fisher wave fronts to move with a
characteristic velocity of v =
p
2Dρα; these waves com-


## Page 4


4
bine with the alignment interactions to decrease spot size
and take the system back towards a uniform phase. This
scenario describes the transition from a uniform phase to
spot and back to uniformity as observed in Fig. 1a. But
why does the described scenario not repeat to initiate
new spots? The answer is, that the new uniform phase
is now polarized and given by (iii) rather than by (ii).
Hence, the spots in Fig. 1a (video 1 in SM) are a generic
transient pattern formed as actin ﬁbers polymerise start-
ing from a low density phase.
Having followed this pathway from phase (i) to phase
(iii), we now want to know how waves emerge. Let us
therefore explore the stability of phase (iii) by calculating
the dispersion relation of ﬂuctuations around this phase
(Fig. 3, see also SM). Remarkably, R(λ) is always nega-
tive at small q but becomes positive at ﬁnite q if Γ is suﬃ-
ciently large (Fig. 3). Since also the imaginary part of the
dispersion relation is ﬁnite, we have an oscillatory short
wavelength instability and may therefore expect travel-
ling waves for suﬃciently strong alignment interactions
(Γ): this explains our previous observation of travelling
waves in Figs. 1b and Fig. 1c. We ﬁnd that the velocity
of our waves is given by v ∼v0
p
(γ/γ2)(ρ0/ρc −1) =
v0P0 – this is true if r = (ρ0/ρc −1) > 1, otherwise
v ∼v0
p
γ/γ2. Therefore the wave speed is proportional
to the treadmilling velocity of individual ﬁbres, weighted
by an alignment factor measuring the average fraction of
aligned ﬁlaments. The distance between adjacent wave
peaks can be estimated by numerical evaluation of the
dispersion relation of our linear stability analysis reveal-
ing a fastest growing mode at length scale l ∝l3/2
1
l−1/2
2
with l1 ∼
p
K/γ and l2 ∼
p
KDρ/(v2
0P 2
0 ) if K > Dρ,
or l2 ∼
p
K3/(Dρv2
0P 2
0 ) if K < Dρ (see SM, note we
have dropped for simplicity an extra non-dimensional de-
pendence on r). Our simulations conﬁrm that the wave
length is typically close to this value, at least deep into
the wave forming regime. The width of our wave peaks
follows, approximately, a variant of our healing length
l ∼
p
K/γ for K > Dρ and l ∼
p
Dρ/γ if Dρ > K
(see SM for more details) – in this context this is the
length scale over which diﬀusion neutralizes polar order-
ing within a wave peak.
The possible scenarios can be summarised in a phase
diagram (Fig. 4). For small Γ and r −1, i.e. when align-
ment interactions are weak and the saturation ﬁbre den-
sity is close to the Onsager threshold, the evolution fea-
tures a uniform increase of our low density initial state,
i.e. a transition from phase (i) via (ii); this phase then
morphs into a set of asters and spirals, which leave way
eventually to a phase (iii) which is asymptotically stable.
Instead, when we cross the transition line, along the black
arrow in Fig. 4, we always ﬁnd travelling actin waves at
long timescales. Deep in the wave phase (large Γ), we
ﬁnd waves emerging directly within the uniform phase:
these waves are also irregular and peaks are far from each
∝(r −1)−1/3
∝(r −1)−1
106
103
1
10−3
10−6
10−3
1
103
Γ2
r −1
Γ
Γ →boundary
Γ →∞
FIG. 4: Phase diagram in the (Γ, r −1) plane. Curves corre-
spond to D = 5 and selected values of Γ2. From top to bot-
tom, these are: 0.00075, 0.075, 0.1775, 0.3704, 3/8, 0.3754,
0.4688.
other. Closer to the transition line we typically ﬁnd spots
appear before waves emerge; waves are also more regular
and the separation between peaks can be decreased, for
instance, by increasing polymerisation (hence decreasing
Γ). The diﬀerent dynamics occur since close to the tran-
sition line, waves emerge slowly and do not impede spot
formation on the pathway from phase (ii) to phase (iii).
The length scale selection may be linked to the fact that
the longest wavelength in the instability band (where the
real part of the dispersion relation is positive) depends
on α. For Γ2 > 3/8 (orange curve) there is an additional
transition line in our phase diagram (dashed lines for
grey and brown line), representing a parameter domain
of large actin ﬁber density where waves are impossible
even for very strong alignment interactions. Physically,
this means that wave formation is only possible in our
system if self-propulsion is fast enough; the critical speed
is given by a combination of ﬁber diﬀusion and alignment
saturation.
Finally, we would like to highlight here the role of poly-
merisation in our model.
Besides guiding the system
through successive instabilities as the overall density in-
creases, actin polymerisation plays other major roles in
the system. First, when its rate α is large enough, it can
suppress pattern formation altogether. Second, close to
the instability threshold, the polymerisation rate controls
the width of and separation between wave peaks. Finally,
at least within the range which we have explored, poly-
merisation is required to create transient spots.
To conclude, we have shown that an ensemble of poly-
merising and treadmilling actin ﬁlaments forms a cas-
cade of patterns encompassing spots, spirals and waves,
which resemble the typical phenomenology found in ex-
periments. Speciﬁcally, when Dictyostelium cells recover
from actin depolymerisation, they reassemble their actin


## Page 5


5
cytoskeleton by creating spots which later on transition
to waves [6, 13]. Remarkably, and at variance with pre-
vious work, our model can recreate this sequence of pat-
terns without the need to assume any underlying non-
linear biochemistry leading to delay, or oscillatory or
activator-inhibitor behaviour. Instead, starting from a
low density initial phase, we suggest that polymerisa-
tion increases the overall density of actin until locally
oriented domains of moving actin ﬂocks appear. These
domains travel along randomly selected directions, and
collide with each other to form spirals or larger spots
where the ﬁlament directions are arranged in an aster
shape. Hence, our work demonstrates that spots occur
automatically en route from the typical low density initial
phase towards the ﬂocking state featuring waves, thereby
challenging previous and more complicated mechanisms
describing the phenomenology of typical in vivo actin
wave experiments. Besides this, our results might also be
useful for designing and understanding minimal in vitro
systems mimicking the actin dynamics observed in vivo.
We thank EPSRC (grant EP/K007404/1) for sup-
port.
BL gratefully acknowledges funding by a Marie
Sk lodowska Curie Intra European Fellowship (G.A. no
654908) within Horizon 2020.
[1] B. Alberts, A. Johnson, J. Lewis, M. Raﬀ, K. K. Roberts
and P. Walter, Molecular biology of the cell (Garland Sci-
ence, New York, 2002).
[2] D. Bray, Cell movements (Garland Science, New York,
2000).
[3] A. Gholami, M. Falcke and E. Frey, New J. Phys. 10,
033022 (2008).
[4] V. Schaller, C. Weber, C. Semmrich, E. Frey and A. R.
Bausch, Nature 467, 73 (2010); J. F. Joanny and S. Ra-
maswamy, Nature 467, 33 (2010).
[5] G. Gerisch, T. Bretschneider, A. M¨uller-Taubenberger,
E. Simmeth, M. Ecke, S. Diez and K. Anderson, Biophys.
J. 87, 3493 (2004).
[6] T.
Bretschneider,
K.
Anderson,
M.
Ecke,
A.
M.
M¨uller- Taubenberger, B. Schroth-Diez, H. C. Ishikawa-
Ankerhold and G. Gerisch, Biophys. J. 96, 2888 (2009).
[7] J. Allard and A. Mogilner, Curr. Opin. Cell Biol. 25, 107
(2013).
[8] M. G. Vicker, Biophys. Chem. 84, 87 (2000).
[9] M. G. Vicker, Exp. Cell Res. 275, 54 (2002).
[10] V. Kamviwath, J. Hu and H. G. Othmer, PLoS ONE 8,
e64272 (2013).
[11] A. Y. Pollitt and R. H. Insall, J. Cell Sci. 122, 2575
(2009).
[12] O. D. Weiner, W. A. Marganski, L. F. Wu, S. J.
Altschuler and M. W. Kirschner, PLoS Biol. 5, e221
(2007).
[13] S. Whitelam, T. Bretschneider and N. J. Burroughs,
Phys. Rev. Lett. 102, 198103 (2009).
[14] V. Wasnik and R. Mukhopadhyay, Phys. Rev. E 90,
052707 (2014).
[15] A. E. Carlsson, Phys. Rev. Lett. 104, 228102 (2010).
[16] K. Doubrovinski and K. Kruse, Europhys. Lett. 83, 18003
(2008).
[17] C. Beta, PMC Biophys. 3, 12 (2010).
[18] J. Toner, Phys. Rev. Lett. 108, 088102 (2012).
[19] L. Onsager, Ann. N. Y. Acad. Sci. 51, 62 (1949).
[20] S. Mishra, A. Baskaran and M. C. Marchetti, Phys. Rev.
E 81, 061916 (2010).
[21] A. Chaudhuri, B. Bhattacharya, K. Gowrishankar, S.
Mayor and M. Rao, Proc. Natl. Acad. Sci. U.S.A. 108,
14825 (2011); K. Gowrishankar and M. Rao, Soft Matter
12, 2040 (2016).
[22] J. Toner, Y.-h. Tu, and S. Ramaswamy, Ann. Phys. 318,
170 (2005).
[23] J.-B. Caussin, A. Solon, A. Peshkov, H. Chat´e, T. Daux-
ois, J. Tailleur, V. Vitelli and D. Bartolo, Phys. Rev. Lett.
112, 148102 (2014).
[24] X. Yang, D. Marenduzzo and M. C. Marchetti, Phys.
Rev. E 89, 012711 (2014).
[25] M. Bailly et al., J. Cell. Biol. 145, 331 (1999).


## Page 6


6
SUPPLEMENTARY MATERIAL
Here, we perform a detailed linear stability analysis
of our model to derive the expressions for the stability
criteria and length scale which we used in the discussion
of spot and wave formation in the main text. To keep our
calculations comprehensive, we consider the equations of
motion in dimensionless form (see main text):
 ∂tP = Γ (rρ −1) P + D∇2P −Γ2P 2P,
∂tρ = −∇· (ρP) + ∇2ρ + ρ (1 −ρ) ,
(5)
where Γ = γ/α, r = ρ0/ρc, D = K/Dρ and Γ2 =
γ2Dρ/v2
0.
These equations allow us to identify three diﬀerent sta-
tionary uniform solutions for the density and polarization
ﬁeld:
(i) P = 0 and ρ = 0,
(ii) P = 0 and ρ = 1,
(iii) P = P0 = [(Γ/Γ2)(r −1)]1/2e and ρ = 1,
Solutions (i) and (ii) represent uniform isotropic phases
with zero and ﬁnite density, respectively.
In contrast,
(iii) is a uniform polarized phase with spontaneously
chosen polarization direction e. This phase only exists
if r ≥1, i.e.
if the target polymerization density is
larger than the critical density at which alignment in-
teractions dominate over rotational diﬀusion of the actin
ﬁlaments.
We will now test the stability of each of
the phases (i)–(iii) against small ﬂuctuations.
There-
fore we linearize Eqs. (5) around solutions (i)–(iii) re-
spectively, and solve the resulting equations in Fourier
space (or alternatively by plugging a plane wave ansatz
(P, ρ) = (Ps, ρs)+(AP, Aρ) exp(λt+iq.r) with small AP
and Aρ into the linearized equations).
Uniform growth
Following typical experiments, in our simulations we
initialized our system in phase (i) with some additional
ﬂuctuations in the particle density ﬁeld (see main text).
To follow the dynamics of our system, we investigate the
stability of phase (i) ﬁrst. Solving the linearized version
of Eqs. (5) around phase (i) in Fourier space, quickly
leads to the following condition for the existence of plane
wave solutions:

λ + Dq2 + Γ
0
0
0
λ + Dq2 + Γ
0
0
0
λ + q2 −1

= 0.
From this condition we quickly determine the dispersion
relation λ(q) for plane wave ﬂuctuations, whose largest
branch is:
λ = −q2 + 1
(6)
Translation this result back to physical units leads to
λ = −Dρq2 + α, which shows that polymerization cre-
ates a long wavelength instability of phase (i). Notably,
the eigenmode corresponding to this unstable growth is
orthogonal to P leading to a simple growth of the actin
ﬁlament concentration without aligning ﬁlaments, tran-
ferring our system from phase (i) to (ii).
Spots formation
Now analysing the linear stability of phase (ii) we ﬁnd
the condition

λ + Dq2 −Γ (r −1)
0
0
0
λ + Dq2 −Γ (r −1)
0
iqx
iqy
λ + q2 + 1

= 0.
yielding for the largest branch of the dispersion relation
λ = −Dq2 + Γ (r −1)
(7)
Translating this expression back to physical variables, we
ﬁnd λ = −Kq2+γ

ρ0
ρc −1

featuring another long wave-
length instability if ρ0 > ρc. Remarkably, this instability
is now parallel to P meaning that once the system has
reached phase (ii) alignment interactions become eﬀec-
tive but do not aﬀect the density ﬁeld in the linear regime.
We can observe a corresponding alignment of actin ﬁla-
ments in Fig.2 of the main text generically leading to the
formation of defects in p which results in formation of
spots in ρ which is a purely nonlinear eﬀect and part of
the dynamical pathway of our system from phase (ii) to
(iii) (rather than a distinct ’spot’ phase).
Generation of waves
To analyse the linear stabilty of phase (iii) we choose
a coordinate system where the direction of polarization
e is parallel to the x-axis, i.e.
where P0 = P0ex =
[(Γ/Γ2)(r −1)]1/2ex. Here, linear stability analysis leads
to the condition

λ + Dq2 + 2Γ (r −1)
0
−ΓrP0
0
λ + Dq2
0
iqx
iqy
λ + q2 + 1 + iP0qx

= 0
yielding the following implicit equation for the dispersion
relation of plane wave ﬂuctuations

λ + Dq2 + 2Γ (r −1)
  λ + q2 + 1 + iP0qx

+ irqxΓP0
	
×

λ + Dq2	
= 0.
(8)
Ignoring the last term which generates only a negative
solution for λ in which we are not interested, Eq. (8) can


## Page 7


7
be rewritten as
λ2 +

(D + 1) q2 + iP0qx + 2Γ (r −1) + 1

λ + Dq4
+ iDP0qxq2 + [D + 2Γ (r −1)] q2 + iΓ (3r −2) P0qx
+ 2Γ (r −1) = 0.
(9)
This equation leads to the following dispersion relation:
λ± = −1
2

(D + 1) q2 + iP0qx + 2Γ (r −1) + 1

±f (10)
Here f is a complex number. Since the product of roots
of a polynomial function of the form Pol(x) = PN
i=0 aixi
is equal to (−1)Na0
aN
, here leading to λ+λ−= a0, we can
write
f 2 =1
4

(D + 1) q2 + iP0qx + 2Γ (r −1) + 1
2 −Dq4
−iDP0qxq2 −[D + 2Γ (r −1)] q2 −iΓ (3r −2) P0qx
−2Γ (r −1) .
(11)
Real and imaginary parts of f 2 are then easily calculated
F = R(f 2) =
(D −1)
2
q2 + Γ (r −1) −1
2
2
−
P0
2 qx
2
,
G = I(f 2) = −P0qx
(D −1)
2
q2 + Γ (2r −1) −1
2

.
We ﬁnally obtain
f =
F
2 + 1
2
 F 2 + G21/21/2
(12)
+ i
G
2
h
F
2 + 1
2 (F 2 + G2)1/2i1/2 .
Note there are two solutions for f but both solutions lead
to the same growth rates which read
λ+ = −(D + 1)
2
q2 −1
2 −Γ (r −1) −iP0qx
2
+ f,
(13)
λ−= −(D + 1)
2
q2 −1
2 −Γ (r −1) −iP0qx
2
−f, (14)
In physical variables these dispersion relations read:
λ+ = −(K + Dρ)
2
q2 −α
2 −γ
ρ0
ρc
−1

(15)
−iv0P0qx
2
+ f,
λ−= −(K + Dρ)
2
q2 −α
2 −γ
ρ0
ρc
−1

(16)
−iv0P0qx
2
−f.
We note, that the imaginary part of λ is diﬀerent from
zero. Hence, phase (iii) is subject to an oscillatory in-
stability allowing for moving patterns. In contrast to the
instabilities of phases (i) and (ii) which generically occur
for α > 0 and large densities r > 1 phase (iii) can be
stable even at large densities and for all values of α > 0.
If Γ is suﬃciently small the real part of our dispersion
relation is negative; then we only observe spot formation
and our system ends up in phase (iii) without featuring
waves.
The fastest growing mode for the dispersion relation
corresponding to the generation of waves can be found
as the value of q for which the real part of λ is maximal.
From a numerical analysis, we ﬁnd that the correspond-
ing wavelength l obeys the scaling:
l ∼l3/2
1
l−1/2
2
(17)
where the two lengthscales l1 and l2 depend on parame-
ters as follows,
l1 ∼[K/(γ(ρ0/ρc −1))]1/2
if ρ0/ρc −1 > 1, (18)
l1 ∼[K/(γ(ρ0/ρc −1)5/9)]1/2 if ρ0/ρc −1 < 1,
l2 ∼[KDρ/(v2
0P 2
0 )]1/2
if K > Dρ,
(19)
l2 ∼[K3/(Dρv2
0P 2
0 )]1/2
if K < Dρ.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
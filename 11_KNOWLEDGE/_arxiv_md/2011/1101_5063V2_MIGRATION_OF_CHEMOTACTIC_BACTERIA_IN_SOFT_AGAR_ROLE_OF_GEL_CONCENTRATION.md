---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1101.5063v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1101.5063v2_Migration_of_chemotactic_bacteria_in_soft_agar__role_of_gel_concentration

> Source: 1101.5063v2_Migration_of_chemotactic_bacteria_in_soft_agar__role_of_gel_concentration.pdf

> Pages: 28

---


## Page 1


arXiv:1101.5063v2  [cond-mat.soft]  6 Aug 2011
Migration of chemotactic bacteria in soft agar: role
of gel concentration
Ottavio A. Croze1
School of Mathematics and Statistics
University of Glasgow
Glasgow G12 8QW, UK.
Gail P. Ferguson
School of Medicine and Dentistry
Division of Applied Medicine
Institute of Medical Sciences
University of Aberdeen
Foresterhill, Aberdeen AB25 2ZD, UK.
Michael E. Cates
SUPA, School of Physics and Astronomy
University of Edinburgh
Mayﬁeld Road, Edinburgh EH9 3JZ, UK.
Wilson C. K. Poon
SUPA, School of Physics and Astronomy
University of Edinburgh
Mayﬁeld Road, Edinburgh EH9 3JZ, UK.
1Corresponding author. Email: o.croze@physics.org


## Page 2


Abstract
We study the migration of chemotactic wild type Escherichia coli popu-
lations in semi-solid (‘soft’) agar in the concentration range C = 0.15 −
0.5%(w/v). For C ≲0.35%, expanding bacterial colonies display character-
istic chemotactic ‘rings’. At C = 0.35%, however, bacteria migrate as broad
circular bands rather than sharp rings. These are growth/diﬀusion waves
arising because of suppression of chemotaxis by the agar and have not been
previously reported experimentally. For C = 0.4 −0.5% expanding colonies
do not span the depth of the agar and develop pronounced front instabili-
ties. The migration front speed is weakly dependent of agar concentration
below C = 0.25%, but decreases sharply above this value. We discuss these
observations in terms of an extended Keller-Segel model for which we de-
rived novel transport parameter expressions accounting for perturbations of
the chemotactic response by collisions with the agar. The model allows to
ﬁt the observed front speed decay in the range C = 0.15 −0.35%, and its
solutions qualitatively reproduce the observed transition from chemotactic
to growth/diﬀusion bands. We discuss the implications of our results for the
study of bacteria in porous media and for the design of improved bacterio-
logical chemotaxis assays.
Key words: Escherichia coli; motility; semi-solid agar; porous media;
chemotaxis; population dynamics


## Page 3


E. coli in soft agar
2
Introduction
Much is understood about the motility of ﬂagellated bacteria in open liq-
uid media (1) and on solid surfaces (2). In contrast, bacterial locomotion
within semi-solid media is much less well studied, even though bacteria of-
ten colonise three dimensional semi-solid environments, e.g. host tissues or
foodstuﬀs.
‘Soft’ agar with concentration 0.2% ≲C ≲0.35% (through-
out, % = %w/v), a gel network whose main component is the semi-ﬂexible
polysaccharide agarose (3), is a plausible model for many of these kinds
of solid environments. It has been used in studies aimed at understanding
motile microbial pathogens growing inside the semi-solid matrix of a vari-
ety of foods and of infected hosts, and therefore for predicting spoilage and
infection (4–6).
Soft agar was ﬁrst introduced into microbiology for assaying chemotaxis
(7).
Chemotactic wild-type Escherichia coli inoculated at one end of a
capillary ﬁlled with nutrient buﬀer spread out in ‘bands’ as they succes-
sively deplete the medium of oxygen and various nutrients. In a Petri dish
ﬁlled with nutrient agar, the observation of successive sharp circular bands
(‘rings’) progressing outwards from the colony inoculated into the centre
of the soft agar is taken to conﬁrm the chemotaxis genotype, since non-
chemotactic mutants spread out uniformly (8).
Interestingly, the agar concentration in this widely-used chemotaxis as-
say is not standardized, varying from investigator to investigator, or even
within the same study, in the range of 0.2% ≲C ≲0.4%. The tacit as-
sumption seems to be that, as long as concentrations are in the ‘soft range’,
agar conveniently suppresses thermal and biological convection in the liquid
medium which hosts bacteria, but otherwise has no interesting eﬀect. Wolfe
and Berg’s investigation (8) of a number chemotactic mutants in soft agar
(C = 0.2% −0.35%) appears to conﬁrm this assumption. They report no
qualitative diﬀerence except a slowing down of the spreading front.
However, the run-and-tumble motion of E. coli (1) and similar bacteria
suggests a priori that soft agar should aﬀect chemotaxis.
The pore size
of soft agar is ∼1µm (10), the same order as typical bacterial run lengths.
Since cells perform chemotaxis by altering their tumble frequency and there-
fore run length, the structure of agar may therefore interfere with the ability
to chemotactically ‘bias’ random walks. The expectation is that this inter-
ference will be more pronounced in agar than in other porous media, such
as sand and soil, where most pore sizes (≈10µm to 1 mm) are very much
larger than typical run lengths. Indeed, a study of Pseudomonas putida in
sand columns with grain sizes in the range 80 −800µm found no eﬀect on


## Page 4


E. coli in soft agar
3
chemotaxis (9).
In this work, we show by experiment and theory that the chemotaxis
of E. coli in soft agar is indeed strongly aﬀected as the concentration is in-
creased in the range C = 0.15 −0.5%. We observe that, as C is increased,
the colony growth pattern changes qualitatively. Also, the speed of the mi-
grating front is weakly dependent on C at C ≲0.25%, but decreases sharply
with agar concentration above this value. To understand our observations,
we formulate a modiﬁed Keller-Segel type model (11, 12) with transport
parameters that are functions of agar concentration. These functions are
derived by extending a recent description of bacterial chemotactic response
(13), and account for the diminished ability of bacteria to detect chemical
gradients in dense gels. Our model is able to ﬁt quantitatively the observed
dependence of front speed on agar concentration.
Methods
We used the E. coli K-12 derivative AB1157, a chemotactic wild-type (14).
Plate cultures from frozen stocks were refrigerated at 4◦C for up to 3 weeks
prior to use. Luria Broth (LB) agar was prepared by adding 1.5-5 g/l of
Difco Bacto-agar to LB Broth (10 g/l Difco Bacto-Tryptone, 5 g/l Difco
Yeast extract, 10 g/l NaCl) (15). The mixture was autoclaved at 121◦C
under 1.02 atm for 30 min, and left to cool for an hour. Agar plates were
then prepared by pouring hot (45-50◦C) nutrient agar into standard sized
(100 mm diameter, 12 mm deep) plastic Petri dishes (Sterilin) on a level
surface; 58 ml were poured in each plate (ﬁnal agar thickness: 10.0±0.1 mm).
Poured plates were left to set for about a day at ambient temperature (22-
27◦C). The ﬁnal pH of the agar was 7.3 ± 0.1.
Late exponential phase cultures (OD600 = 0.8 −1.3) were prepared by
inoculating single colonies in LB-ﬁlled ﬂasks incubated at 30.0◦C and shaken
at 200 rpm.
Cultures were then diluted to OD600 = 0.1 (≈108 viable
cells/ml) and agar plates were inoculated by delivering a droplet of ≲1µl
via a 2µl pipette. Inocula were left to sit on the agar for about an hour;
then a thin layer (thickness ≈1.5 mm, corresponding to ≈9 ml) of sterile
ﬁltered mineral oil (Sigma) was poured on the plates. Except at the highest
agar concentrations studied (C ≳0.4%), the inoculum had been (to the
naked eye) completely assimilated by the time the oil was poured, with no
visible evidence of the pouring spreading organisms to other parts of the agar
surface. At the highest C, the inoculum was not signiﬁcantly incorporated
into the agar after an hour, so that careful pouring was needed to minimise


## Page 5


E. coli in soft agar
4
spreading. When signiﬁcant spreading did occur, the plates were discarded.
The thin oil layer kept evaporative losses to < 1% (weight) during our
observations, but did not generate anaerobic conditions (16).
The Petri dishes were incubated at 30.0±0.5◦C on a dark background, il-
luminated from the sides, and imaged at 30 minute intervals using computer-
controlled CCD cameras. Images were analysed using ImageJ (NIH) and
IDL (RSI, Boulder, CO): a, static noise (by subtracting the ﬁrst frame in
each sequence) was removed; b, slightly non-uniform illumination was cor-
rected for (subtracting the image background ﬁtted using a sliding paraboloid
with 20 pixels rolling ball radius); c, histograms were matched histograms
using gray-scale mapping (17). Then we obtained azimuthally-averaged ra-
dial intensity proﬁles from those images without signiﬁcant blebs (see below
for observations and further discussion on blebs). The images presented in
Fig. 1a and Fig. 2 were processed using only steps b and c.
At high C, image thresholding enabled us to determine the colony area,
A, from which we calculated the radius r =
p
A/π. At lower C we ﬁtted a
circle to the intensity maximum in each image and determined the area of
the ﬁtted circle, from which r was then calculated.
Model of chemotactic E. coli populations in agar
The fundamental processes in agar plates inoculated with bacteria are growth
due to nutrient uptake and dispersion due to chemotactic motility, which can
be modelled by generalized Keller-Segel models (11, 18). Migrating popu-
lations of bacteria in agar have been described for bacteria chemotactically
sensing nutrients (19, 20) or attractants secreted by the cells themselves
(21). However, these models ignore, or inconsistently account for, the eﬀect
of agar on bacterial chemotaxis. Since agar is a porous gel, one might think
that existing descriptions of other porous media (22, 23) should be appli-
cable to agar.
We will show below that these descriptions are incorrect.
The model presented here is an adaptation of that originally formulated by
Lauﬀenburger, Kennedy and Aris (LKA) for a chemotactic population with
growth in one dimension (12). Our model diﬀers from the LKA model in
three ways. First, we model growth as logistic, while LKA used a linear
term. Secondly, we work in two dimensions, since LKA’s 1D analysis is not
adequate for modelling Petri dishes for early times. Finally and most cru-
cially, bacterial transport coeﬃcients in our model are not constants, but
functions of agar concentration derived from a recent model of chemotactic
response (13).


## Page 6


E. coli in soft agar
5
Model equations
The starting point equations of our model are:
∂b
∂t = −∇· [−µ(s, C)∇b + vχ(s, C)b] + kgb

g(s) −b
kb

(1)
∂s
∂t = D∇2s −1
Y kgg(s)b.
(2)
Equation 1 expresses the conservation of bacteria, with population density
b(r, t).
This population evolves in response to the combined eﬀect of its
diﬀusive and chemotactic ﬂuxes, with diﬀusivity µ(s, C) and drift velocity
vχ(s, C); these are in general functions of both substrate and agar concen-
trations, s(r, t) and C respectively. The bacterial population also evolves by
growth, with birth rate kgg(s), where kg is the maximum growth rate and
g(s) is a function of substrate uptake, and a death rate −kgb/kb, where kb
is the carrying capacity of the population. Equation (2) models the conser-
vation of the ﬁrst, most readily metabolised substrate, with concentration
s(r, t), diﬀusing with diﬀusivity D and being consumed by bacteria at a
rate −kgg(s). In tryptone broth or LB this substrate is L-serine (7, 20).
In the consumption term of (2), Y is the bacterial yield upon consump-
tion (b = Y s). We now assume the following relations: µ(s, C) = µ(C);
vχ(s, C) = χ(C) ∇fχ(s), where fχ(s) =
s
s+kχ ; and g(s) =
s
s+ks. That is, we
assume the diﬀusivity to be isotropic and independent of substrate concen-
tration; µ depends only on the spatially uniform agar concentration C (see
below). The chemotactic velocity, vχ, is assumed linear in the gradient of a
‘receptor-adsorption’ function fχ(s); kχ is the characteristic saturation con-
centration of the chemotactic response (24). The proportionality constant
is the chemotactic coeﬃcient χ which, like µ, is assumed to depend only on
agar concentration. The relations involving vχ and µ are approximate forms
valid in the limit of shallow concentration gradients (25). Bacterial growth
depends on substrate concentration through a Monod-type growth function
g(s) (26); ks is the characteristic saturation concentration for growth.
We have derived the dependence of the diﬀusivity, µ, and chemotactic
parameter, χ, on agar concentration by modifying de Gennes’ integral model
of bacterial chemotactic response (13), as detailed in Appendix A.
The
model quantiﬁes the intuition that in a dense matrix of obstacles bacteria
are reoriented by collisions with the matrix as well as by tumbles, making
chemotaxis ineﬃcient. Such collisions increase the eﬀective bacterial tumble
rate from the in liquido value α0 to α(C) = α0(1+f(C), where the function
f(C) quantiﬁes the collision-induced concentration-dependent increase of


## Page 7


E. coli in soft agar
6
the tumble rate (see below). From our model it can be shown (see Appendix
A) that the chemotactic transport parameters in agar are given by:
µ(C) = µ0 [1 + f(C)]−1 ;
χ(C) = χ0 [1 + f(C)]−2 Iχ [f(C)]
(3)
where µ0 and χ0 are the bacterial diﬀusivity and chemotactic coeﬃcient in
the absence of agar. The agar concentration-dependent integral Iχ is given
by equation (A16) and its value depends on the form of the chemotactic
response function, K(t), see equation (A17). The function f(C) gauges the
increase with agar concentration of the tumble rate in agar, αA(C), with
respect to its in liquido value α0. That is, we assume αA(C) = α0f(C). Since
collisions are more frequent for a higher density of obstacles, we expect f(C)
to monotonically increase with C. We adopt the ansatz f(C) = exp[C−C1
C0 ],
where C0 is a characteristic concentration.
The concentration ‘shift’ C1
accounts for the possibility that the tumble rate in agar can recover its in
liquido value for small, but nonzero agar concentrations: αA(C ≤C1) →0
so α(C ≤C1) →α0, C1 > 0.
To further understand the experimentally observed migration transition
and to compare our results to those derived for bacteria in porous media
(22, 23), we have also derived asymptotic limits to the expression (3) for
χ(C). As shown in Appendix A, these asymptotic limits are:
χ(C) ≃
(
χ0 [1 + f(C)]−2 [1 −κf(C)]
if ˜α(C) ≈1
β χ0 [1 + f(C)]−3
if ˜α(C) ≫1.
(4)
where κ and β are constants (see Appendix A) and ˜α(C) = 1 + αA/α0 =
1 + f(C) is the dimensionless eﬀective tumble rate in agar (see (A6)). The
limits (4) reﬂect the eﬀect of conﬁnement in agar on chemotaxis. At low
concentrations, agar does not signiﬁcantly impede chemotaxis, and bacte-
ria can tumble relatively freely:
˜α(C) ≈1 (‘eﬃcient’ limit).
At higher
concentrations, frequent collisions with the agar ˜α(C) ≫1 confuse the
chemotactic response (the ‘confused limit’).
Neither expressions (3), nor
the limits (4) coincide with those derived in previous models of bacteria in
porous media. These models treat bacteria in porous media like molecu-
lar gases, and so derive transport parameters obeying the balance relation:
µ(C)
µ0
= χ(C)
χ0
= [1 + αA(C)
α0
]−1 (22, 23). However, in our model this rela-
tion does not hold (even for very low C) because of the eﬀect of collisions
on chemotaxis.
It is only recovered in the absence of agar.
We assume
changes in the swimming speed, D or kg with agar concentration are negli-
gible (27, 28).


## Page 8


E. coli in soft agar
7
Geometry, scaling and model parameters
We will consider only the two-dimensional, axisymmetric limit of our equa-
tions. Our assumption is that, modulo a time shift, fully developed bacte-
rial front dynamics are insensitive to particular initial conditions (provided
the initial colony is azimuthally symmetric). The characteristic length and
time scales for our experiments are millimeters and hours, so we rescale our
equations by τg ∼k−1
g , where kg is the growth rate, and lg ∼
p
µ0/kg,
the average length a cell diﬀuses during a doubling time (in the absence of
agar). The population density is rescaled by its carrying capacity, kb, and
all concentrations by the initial substrate concentration, s0. We rescale all
diﬀusivities by that of the bacterial population (in the absence of agar), µ0.
We also rescale the yield Y by the maximum possible yield kb/s0. Thus:
r = r
p
kg/µ0; T = kgt; B = b/kb; S = s/s0; N = D/µ0; δ0 = χ0/µ0; Kχ =
kχ/s0; Ks = ks/s0; H = kb/(Y s0); M(C) = µ(C)/µ0; X(C) = χ(C)/χ0.
The model equations (1) and (2) in dimensionless form then read
∂B
∂T = M(C)∇2B −δ0X(C)∇·

B dFχ
dS ∇S

+ B [G(S) −B] ,
(5)
∂S
∂T = N∇2S −H G(S) B,
(6)
where Fχ(S) =
S
S+Kχ, G(S) =
S
S+Ks and where the dependence on agar
concentration is through the functions:
M(C) = [1 + f(C)]−1 ;
X(C) = [1 + f(C)]−2 Iχ [f(C)] ,
(7)
where we recall f(C) = exp[C−C1
C0 ], where C0 and C1 are the characteristic
concentrations introduced earlier. The parameter δ0 is signiﬁcant: it mea-
sures the relative magnitude of chemotactic advection to random diﬀusion
in the absence of agar (a chemotactic P´eclet number). It is how this ratio
is modiﬁed by agar which leads to surprising results, as we will see. We
have also deﬁned the dimensionless parameters N, the ratio of nutrient and
bacterial diﬀusivities, and H, the ratio of carrying capacitance of the bac-
terial population to the maximum population obtainable from the nutrient
available. Equations (5) and (6) are subject to no-ﬂux boundary conditions
and to the initial conditions:
B(R, 0) = e−R2
σ2 ;
S(R, 0) = 1 −e−R2
σ2 ,
(8)
where σ is the width of an initial Gaussian packet of bacteria.
The fol-
lowing parameter values were used to solve our equations: growth rate,
kg = 0.7h−1 (from in liquido growth curve); initial cell concentration, b0(=


## Page 9


E. coli in soft agar
8
kb) = 3.5 × 108 cells/ml (from viable counts); initial substrate concentration
(of L-serine in LB), s0 = 1 mM (5-8 mM (29)); cell diﬀusivity (no agar),
µ0 = 5.7 mm2/h (1.2 mm2/h (30)); chemotactic parameter (no agar), χ0 =
600 mm2/h (450 mm2/h to α-methylaspartate (30)); substrate diﬀusivity,
D = 3 mm2/h; chemotactic threshold concentration, kχ = 0.5 mM (0.2 mM
for α-methylaspartate (30)); growth threshold concentration, ks = 1 mM;
yield, Y = 1011 cells/ml/M. The growth rate and initial cell concentration
were determined by our own independent experiments indicated in brackets.
All other parameters are based on experimental literature values for E. coli,
many of which have been used in other models of E. coli migration (31, 32).
Reference literature values close to parameters we changed are reported in
brackets above. In addition to these macroscopic parameters, we use the
in liquido tumble rate α0 = 1 s and the constant A0 = 0.5 to calculate the
integral Iχ in (7) using (A16) and (A17) (33). The concentrations C0 and
C1 are free parameters, ﬁxed by ﬁtting the predicted front speeds with those
we observed experimentally (see Results and Discussion). Prior to perform-
ing the ﬁt, the values of the parameters kg, µ0, χ0 and kχ were adjusted
slightly to match the values of experimental and predicted band speed for
C = 0.15% (assuming this is the same as in liquido).
With these parameters, the dimensionless constants of the model have
the values: δ0 = 105; Kχ = 0.53; Ks = 1; N = 0.5; H = 3.5. The above
parameters will not be changed in our investigation and the initial packet
width σ is ﬁxed at 2. Equations (5) and (6) in 1D axisymmetric form were
solved numerically for C = 0.15−0.35% on a linear domain (L = 100) using
Matlab subject to initial conditions (8) and no-ﬂux boundary conditions.
Migration front speeds were obtained by subtracting the position of the
leading edge inﬂexion points of solution proﬁles calculated at neighbouring
time points and dividing by the time interval. Like in experiment, these
speeds were calculated in the linear growth regime (long times) where speed
does not change with radius.
Results
Observations on migration morphology and radial dynamics
We ﬁrst report qualitative features of colony morphology and dynamics.
For all concentrations studied (C = 0.15 −0.5%) it takes 5-7 hours for the
bacterial inoculum on the agar surface to become visible. The inoculum
then grows in optical density and, after an additional time lag of 1-50 hours
(likely caused by the oil overlay, but with no inﬂuence on the reproducibility


## Page 10


E. coli in soft agar
9
of subsequent front dynamics), the initial bacterial colony migrates across
the plates. Stills from early and advanced stages of colony migration for
concentrations in the range 0.15% ≤C ≤0.35%, are shown in Fig.
1a.
Two striking eﬀects of increasing concentration are immediately apparent:
the change from a morphology displaying sharp rings to one which is more
diﬀuse and featureless, and the loss of circular symmetry in the advanced
stage of migration at high concentrations (C ≈0.35%).
At the lowest concentrations sampled, C = 0.15−0.2%, bacteria migrate
as sharp circular bands inside the agar. We observed two bands in succession.
The ﬁrst band sharpens as it migrates across the plate, Fig.
1b,c.
The
second band is slower than the ﬁrst and also appears to sharpen as it travels.
Interestingly, the ﬁrst band at C = 0.15% initially displays internal structure
(a double band, see ﬁrst frame of Fig. 1b) and is reﬂected from the plate
walls (not shown) before the second band catches up with it.
Bacteria also migrate as circular bands for C = 0.25 −0.3%.
Again
two bands were observed, but now they travelled together Fig. 1d,e. At
C = 0.35%, sharp bands are no longer visible (Fig. 1f). The colony grows
from the inoculum as a circular disk with a slightly nebulous front (Fig. 1).
The intensity across the disk is initially approximately uniform, falling oﬀ
at the edges, deﬁning the band front Fig. 1f. At later times, however, it
displays a broad band structure. We did not follow the radial development
of these bands to the edge of the plate because the colony front develops
instabilities (blebs) that disrupt circular symmetry.
Visual inspection conﬁrmed that bacteria had spread from the surface
inoculum into the agar to a signiﬁcant depth. For concentrations supporting
bands these are initially hard to resolve for radii smaller than the agar depth:
the colony appears like a uniform expanding circle from above (Fig. 1a, top
row). For larger radii the ﬁrst band is visible and clearly spans the depth of
the agar, as observed by Adler (7). For colonies with two distinct bands, it
is not clear at what depths the second bands occur; from our images they
seem to be further inside the agar. Microscopy (not shown) reveals that for
C < 0.4% bacteria penetrate signiﬁcantly beyond 1mm in depth, but for
this and larger concentrations it seems that agar limits penetration to a few
mm from the surface.
At C = 0.4 −0.5%, shown in Fig. 2, the expanding colony appeared
as homogeneous, solid circles initially.
However, the front invariably de-
veloped extensive blebs. The blebbing instability set in earlier for higher
concentrations (e.g. at C = 0.4% blebs appeared when the colony radius
was beyond a third of the plate radius, while at C = 0.45% it appeared at
around one sixth). The blebs developed into wedge shaped sectors, giving


## Page 11


E. coli in soft agar
10
the colony an overall ﬂower shape (Fig. 2). At these concentrations, the
colony also appeared to spread on the surface of the agar (though not by
classical ‘swarming’), but we did not investigate such surface migration.
Eﬀect of concentration on radial migration
In Fig. 3 we plot the radius of the outermost migrating front (band), r,
against the time, t = ti −∆tl, elapsed since inception of visible colony
growth, where ti is the time since inoculation and ∆tl is the latency time
before a colony grows out. We estimated ∆tl from the intersection of a linear
ﬁt to the raw radial data with the time axis (Fig. 3, inset). A substantial
portion of the radial growth is linear in time for 0.15% < C < 0.4%. Linear
portions can also be identiﬁed for 0.45 and 0.5% (not shown), though the
extent of these data is severely limited by the formation of blebs. Slopes from
the ﬁts to the radial growth curves in the range 0.15 −0.35% (0.15 −0.5%)
are plotted as a function of agar concentration in Fig. 4 (and inset). At
C ≤0.25% the migration speed is at best weakly aﬀected by concentration,
but beyond this value it decreases dramatically. Our model can account for
this behaviour (see below).
Theoretical front speed decay and band proﬁles
A ﬁt to the experimental front speed data from solutions of our full model
using relations (3) is shown in Fig. 4; also shown are the ‘eﬃcient’ and ‘con-
fused’ limits of the model for the same parameters. As expected, the eﬃcient
(confused) limit is a good description at low (high) concentration. The evo-
lution of the theoretical band proﬁles corresponding to the full model best ﬁt
is shown in Fig. 5 (left). Also shown in Fig. 5 (right) is the prediction using
transport parameters from gas kinetic models derived for bacteria in porous
media: µ(C)
µ0
= χ(C)
χ0
= [1 + αA(C)
α0
]−1 (22, 23). As concentration is increased
in the experimental range C = 0.15 −0.35%, the full model band proﬁles
displays a gradual transition from sharp, chemotaxis-dominated bands to
broader, growth/diﬀusion-dominated bands. In the gas kinetic model, be-
cause the chemotaxis parameter, χ, and diﬀusivity, µ, have the same func-
tional dependence on C, proﬁles remain sharp for all concentrations. The
rounded proﬁles predicted by our model arise from suppression (‘confusion’)
of the chemotactic response caused by bacterial collisions with the agar.
When the chemotactic ﬂux in equation (1) becomes negligible with respect
to the ﬂuxes due to logistic growth and diﬀusion, the travelling band solu-
tions to (1) and (2) change from sharp, fast chemotaxis-dominated bands to


## Page 12


E. coli in soft agar
11
slower, broader bands driven by growth/diﬀusion processes. This is what we
observe experimentally. The breakdown of the model in the range C = 0.4-
0.5%, evident from the inset to Fig. 4, is explained in the discussion below.
Discussion
We have experimentally studied the migration of chemotactic E. coli popula-
tions in soft agar of concentration in the range C = 0.15−0.5%. Consistently
with other investigators we ﬁnd that increasing agar concentration decreases
the speed of propagation of the bacterial front (5, 8, 34) and severely ham-
pers penetration for C ≳0.5% (5, 34). However, our work also reveals a
hitherto unobserved transition in the dynamics of the population as agar
concentration increases. The gradual transition is from a dynamics display-
ing characteristic sharp chemotactic bands (rings) to one where the bacteria
travel as broader bands. By increasing the chemotaxis to diﬀusion ratio
δ0 = χ0/µ0 Lauﬀenburger et al.
(LKA) theoretically studied the transi-
tion from sharp chemotactic to broader growth/diﬀusion bands, but failed
to ﬁnd evidence for the latter in studies of chemotaxis in capillaries (12).
Interestingly, we have discovered that suﬃciently concentrated agar pro-
vides an environment where chemotaxis is suppressed and growth/diﬀusion
processes can be observed to dominate the band dynamics.
To understand our experimental results we also built a model of bacte-
rial migration in agar. We extended the LKA model and coupled it to the
ﬁrst full expressions for the concentration dependence of bacterial diﬀusiv-
ity µ(C) and chemotactic parameter χ(C) in agar. We derived these (see
Appendix A) from an adaptation to agar of de Gennes’ model of bacterial
chemotactic response (13). Collisions with the matrix of concentrated agar
(eﬀective tumble rate α(C) = α0(1 + f(C)), where f(C) = exp[C−C1
C0 ]) con-
fuse this response causing µ(C) and χ(C) to have diﬀerent functional forms.
Our model can thus predict the band transition we observe experimentally.
We obtained a best ﬁt of the theoretical front speeds to the experimentally
observed values (Fig. 4) in the concentration range 0.15-0.35%, ﬁnding the
characteristic concentrations C0 = 0.035% and C1 = 0.28%. In comparing
model proﬁles, Fig. 5, with experimental ones, Fig. 1b-f, we note that the
vertical axes in the latter probably do not map linearly to cell density due to
multiple scattering eﬀects. In addition, ‘dead’ or non-motile bacteria con-
tribute to the signal but do not contribute in theoretical plots. With these
caveats, we see that for C = 0.15-0.35% our model qualitatively reproduces
the experimentally observed transition in the colony (band) proﬁle at long


## Page 13


E. coli in soft agar
12
times rather nicely (Fig.
5, left): bands change from sharp to broad as
concentration in increased.
The model breaks down for C = 0.4-0.5%. At these concentrations bac-
terial diﬀusivity becomes very small (e.g. M(0.4%) = 0.03) and equations
(1) and (2) predict a front speed independent of C. However, the measured
(early, bleb-less) front speed continues to fall sharply with C, see inset to
Fig. 4. One reason the model fails is that small diﬀusivity aﬀects growth at
high C. During a doubling time bacteria in 0.4% agar are able to diﬀuse ≈6
times less far than for C = 0.15% (in liquido), which increases competition
for nutrients with neighbours. Further, at high C small bacterial diﬀusivity
means growth is limited by that of nutrients: µ(0.4%)/D = 0.06. Diﬀusion
limited growth is known to produce branching instabilities like those we
observe (35).To fully explain high concentration colony morphologies (Fig.
2) changes in gene expression in response to low nutrient levels will also
need to be considered. An interesting possibility is that in high C agar cell
densities could reach large enough values to elicit quorum sensing responses
(36). Experimentally, the situation for C ≥0.4% is also complicated by
the observation of coexisting subpopulations (see results and also (34)), one
growing on the surface and one in the bulk, which does not penetrate very
deeply (the dynamics is no longer 2D as assumed). Modelling these very
diﬀerent conditions is left to a future study.
We have so far been implicitly discussing the ﬁrst (front) band.
Ex-
perimentally a second band is also observed for C < 0.35% which, as agar
concentration is increased, travels closer and closer to the ﬁrst (see Fig.
1b-f).
As mentioned bacteria in LB preferentially metabolise one nutri-
ent at a time: the ﬁrst band aerobically consumes L-serine and the second
L-aspartate, with a roughly constant metabolic delay Tm between bands
(7, 8, 20). Thus the maximum spacing between bands Lb ∼vF (C)Tm will
decay with C like vF(C), the speed of the ﬁrst band. In this paper the em-
phasis has been on explaining the experimentally observed shape transition
of the ﬁrst band. In the future, it will be interesting to extend our model
and experiments to quantify chemotaxis and its suppression for all nutri-
ents consumed. Accounting for multiple bands, as well as using improved
receptor-adsorption functions for growth and chemotaxis, will allow more
realistic predictions for the trailing edge of the bands.
The suppression of chemotaxis we have studied is relevant to the migra-
tion of bacteria in porous materials other than agar, important in bioreme-
diation (22) and food spoilage (5). As discussed above, previous gas kinetic
models of bacterial migration in porous media (22, 23) do not account for
the possibility of the chemotactic response becoming confused by collisions


## Page 14


E. coli in soft agar
13
with agar. This neglect, which is an implicit consequence of assuming bac-
terial populations behave like molecular gases, invalidates the predictions of
these models in porous media with a ﬁnite concentration of obstacles, even
if dilute. Gas kinetic models can provide good ﬁts to our experimental front
speed data (with diﬀerent values for the characteristic concentrations C0
and C1), but cannot also reproduce the experimentally observed transition
in front shapes. On the other hand, provided pores are larger than a cell, our
model accurately describes the transport of chemotactic bacteria in general
porous media.
Our results also have potentially important implications for microbio-
logical practice. Microbiologists studying motility often make chemotactic
mutants which are screened for using chemotaxis assays. One of these assays,
the ‘motility assay’, involves inoculating soft agar and imaging the resulting
bacterial colony, like we have done in this study. The agar concentration
for such assays is not standard (values in the range 0.1-0.4% can be found
in the literature (37, 38)), and seems to be a matter of convenience (e.g.
larger concentration allows to study more than one colony in the same plate
(39)). When chemotactic mutants are screened for, the chemotactic band
phenotype is sought for as a marker of chemotaxis, its absence denoting a
successful chemotactic mutant (8) or a failed restoration of the chemotaxis
phenotype (37). Our experiments suggest, however, that chemotactic run-
and-tumble bacteria above a certain (still soft) concentration of agar will
fail to show the band phenotype. Thus, if agar plates are used to assay
for chemotaxis it will be important take into account the possibility that
suppression of the band phenotype by the physical environment may oc-
cur. Performing assays at a number of agar concentrations spanning the
soft range (0.1-0.4%) should therefore be part of standard protocol when
screening for chemotaxis.
Acknowledgements
We acknowledge work by Jessica Cameron in the embryonic stages of this
research, assistance by Sarah Spragg, and discussions with Rosalind Allen,
Julien Tailleur, Davide Marenduzzo and with Gary Dorken.
OAC and
WCKP were funded by the EPSRC EP/E030173 and EP/D071070. GPF
was funded by an MRC New Investigator grant G0501107. MEC was funded
by the Royal Society.


## Page 15


E. coli in soft agar
14
A
Modelling run-and-tumble chemotaxis in agar
Using a microscopic model of run-and-tumble dynamics in one dimension
(see (40) and references therein) it can be shown that the bacterial diﬀusivity,
µ, and the chemotactic parameter, χ, are given by:
µ =
2v2
α+ + α−;
vχ = vα−−α+
α+ + α−
(A1)
where α± are the mean tumble probabilities for bacteria moving up (+)
and down (−) the substrate gradient, and v is the average run speed. Note
that for symmetric bias, α+ = α−= α, µ = v2/αd ≡µ0 in d dimensions.
Extension to the asymmetric case for d > 1 is cumbersome and here we
formally work only in d = 1. (By writing the ﬁnal results in terms of µ0 the
correct d-dependence is, however, recovered in the symmetric limit).
We connect the above expressions to the chemotactic response by mod-
ifying previous work (13? ) to account for the eﬀect of agar. A bacterial
run is an inhomogeneous Poisson process with rate
αt(t) = α0

1 −
Z t
−∞
dt′K(t −t′)fχ(x(t′))

≡α0[1 −∆(t)]
(A2)
where the subscript t indicates tumbles and, as in the main text, α0 is the
tumble rate in the absence of bias and fχ is a function related to substrate
concentration at position x via fχ = s(x)/(s(x) + kχ). The function K(t)
is the bilobed chemotactic response function which has been measured for
E. coli (42), and obeys
R ∞
0
K(t)dt = 0. The linear expression above is valid
for shallow substrate gradients, i.e. the bias |∆(t)| ≪1. Considering a run
starting at t = 0, in the absence of agar the probability density for a tumble
occurring in the interval [t, t + dt] is given by αt(t) exp

−
R t
0 dt′αt(t′)

. We
argue that since bacterial collisions with the agar can also be considered a
Poisson process, the same probability density describes the occurrence of
tumbles in agar if the tumble rate αt is replaced by an eﬀective rate:
αe(t; C) = αt + αA
(A3)
which comprises (independent) contributions from αt = αt(t; C), the tumble
rate due to the intrinsic bacterial dynamics (modulated by any chemotac-
tic response) and αA = αA(C) an additional collision rate with the agar
(which also randomises swimming direction). Then the mean run duration
for bacteria in agar (or other porous media) is given by
T(C) =
Z ∞
0
dt t αe(t; C) exp

−
Z t
0
dt′αe(t′; C)

paths
(A4)


## Page 16


E. coli in soft agar
15
where ⟨. . .⟩paths denotes an average over all possible bacterial swimming
paths (the suﬃx will hereafter be assumed), since the nonlocal contribution
αt to αe is path dependent. Then, changing variables in the memory integral
(A2) by deﬁning u = t−t′, substituting (A3) into (A4) and recalling |∆(t)| ≪
1, we have:
T(C) ≈
1
α(C) + α0
Z ∞
0
dte−α(C)t
Z t
0
dt′
Z ∞
0
duK(u)fχ(x(t′ −u))

(A5)
where we have deﬁned the unbiased tumble rate in agar
α(C) = α0 + αA(C).
(A6)
The concentration function fχ is related to imposed gradients by a Taylor
expansion:
fχ(x(t −u)) ≈x(t −u)∇fχ + const.
(A7)
Recalling that that K(u) integrates to zero, the constant term does not
contribute to integral (A5). Thus, following a trick introduced by De-Gennes
(13), we consider a ‘single delay’ response function of the form K(u) =
Aδ(u −θ), so (A5) becomes
T(C) ≈
1
α(C) + A∇fχα0
Z ∞
0
dte−α(C)t
Z t
0
dt′x(t′ −θ)

.
(A8)
Next, again following (13) (ignoring persistence and rotational diﬀusion, see
(41)) we notice that for times t−θ < 0 before the start of a run, the position
x(t −θ) is on average not correlated to the bacterial velocity along the run.
On the other hand for t −θ > 0, we can write x(t −θ) = ±v(t −θ), where
±v is the run speed up or down a gradient. (A8) then becomes
T ±(C) ≈
1
α(C) ± v |∇fχ| α0A
Z ∞
θ
dte−α(C)t 1
2(t −θ)2
(A9)
and, after integrating by parts
T ±(C) ≈
1
α(C) ± v |∇fχ|
α0
α(C)3 Ae−α(C)θ
(A10)
. So ﬁnally, for a general a distribution of delay times K(θ) we have
T ±(C) ≈
1
α(C) ± v |∇fχ|
α0
α(C)3
Z ∞
0
dθK(θ)e−α(C)θ.
(A11)


## Page 17


E. coli in soft agar
16
Now we identify α± = 1/T ±, so that we can use (A11) and (A1) to ﬁnd, to
leading order in |∇fχ|,
µ(C) =
v2
α(C);
vχ(C) = v2
α0
α(C)2 |∇fχ|
Z ∞
0
dθK(θ)e−α(C)θ.
(A12)
Or, since the chemotactic sensitivity parameter χ is deﬁned by vχ = χ(C)∇fχ
µ(C) = v2
α0

1 + αA(C)
α0
−1
;
χ(C) = v2
α0

1 + αA(C)
α0
−2 Z ∞
0
dθK(θ)e−α(C)θ.
(A13)
where we have expanded the agar tumble rate deﬁned in (A6). Equations
(A13) are the bacterial transport parameters in agar accounting for a chemo-
tactic response nonlocal in time. In the absence of agar (C →0), the ex-
perimentally measured values of the bacterial transport parameters are µ0
and χ0, the in liquido diﬀusivity and chemotactic parameter. In this limit
(A13) become the expressions derived by de Gennes (13)
µ(C →0) = v2
α0
≡µ0;
χ(C →0) = v2
α0
Z ∞
0
dθK(θ)e−α0θ ≡χ0.
(A14)
Using (A14), we can rewrite (A13) as
µ(C) = µ0

1 + αA(C)
α0
−1
;
χ(C) = χ0

1 + αA(C)
α0
−2
Iχ
αA(C)
α0

,
(A15)
where
Iχ
αA(C)
α0

=
R ∞
0
dθK(θ)e−α0
h
1+ αA(C)
α0
i
θ
R ∞
0
dθK(θ)e−α0θ
.
(A16)
To solve the model presented in the main text, we require an explicit expres-
sion of K(t) to evaluate (A16), and thus (A15). We use a recently proposed
ﬁt to the experimentally measured impulse response of E. coli (33), and
write:
K(t) = N0e−α0t

1 −A0

α0t + 1
2α2
0t2

,
(A17)
where α0 is the base tumble rate, A0 is a dimensionless constant and N0 > 0
is a normalisation constant whose value is unimportant, as it cancels out in
the expression for Iχ.
To facilitate the discussion of our results, we also evaluate two limiting
expressions for the concentration dependence of the chemotactic parameter


## Page 18


E. coli in soft agar
17
in (A15). For very low concentrations bacterial collisions with the agar are
rare, αA(C) ≪1 (α(C) ≈α0), so, expanding to ﬁrst order, (A16) becomes
Iχ ≈1 −κ αA/α0, where κ ≡
R ∞
0
dθK(θ)e−α0θα0θ/
R ∞
0
dθK(θ)e−α0θ. For
large agar concentrations, on the other hand, collisions with the agar are
frequent and confuse the chemotactic response. The eﬀective tumble rate
is so large compared to the natural one, α(C) ≫α0, that K(θ) can be
approximated by K(0) in the numerator of (A16), where the integrand falls
rapidly to zero for θ ≥1/α(C).
In this case Iχ(αA/α0 ≫1) ≈β[1 +
αA(C)/α0]−1, where β = K(0)/(α0
R ∞
0 dθK(θ)e−α0θ). We can then write
asymptotic expressions for the chemotactic parameter:
χ(C) ≃



χ0
h
1 + αA(C)
α0
i−2 h
1 −καA(C)
α0
i
if α(C) ≈α0
β χ0
h
1 + αA(C)
α0
i−3
if α(C) ≫α0 .
(A18)
If, as in the main text, the values A0 = 0.5 and α0 = 1 are used in (A17),
then κ = 1/10 and β = 16/5.
References
1. Berg, H. C., 2004. E. coli in motion. Springer.
2. Harshey, R. M., 2003. Bacterial motility on a surface: many ways to a
common goal. Ann. Rev. Microbiol. 57:249–273.
3. Guenet, J. M., and C. Rochas, 2006. Agarose sols and gels revisited.
Macromol. Symp. 242:65–70.
4. Wimpenny, J. W. T., L. Leistner, L. V. Thomas, A. J. Mitchell, K. Kat-
saras, and P. Peetz, 1995. Submerged bacterial colonies within food and
model systems: Their growth, distribution and interactions. Int. J. Food
Microbiol. 28:299–315.
5. Mitchell, A. J., and J. W. T. Wimpenny, 1997.
The eﬀects of agar
concentration on the growth and morphology of submerged colonies of
motile and non-motile bacteria. J. Appl. Microbiol. 83:76–84.
6. Richardson, K., 1991.
Role of motility and ﬂagellar structure in the
pathogenicity of Vibrio cholerae: Analysis of motility mutants in three
animal models. Infect. Immun. 59:2727–2736.
7. Adler, J., 1966. Chemotaxis in bacteria. Science 153:708–716.


## Page 19


E. coli in soft agar
18
8. Wolfe, A. J., and H. C. Berg, 1989. Migration of bacteria in semisolid
agar. Proc. Natl. Acad. Sci. USA 86:6973–6977.
9. Barton, J. W., and R. M. Ford, 1995. Determination of Eﬀective Trans-
port Coeﬃcients for Bacterial Migration in Sand Columns. Appl. Env.
Microbiol. 61:3329–3335.
10. Righetti, P. G., B. C. W. Brost, and R. S. Snyder, 1981. On the limiting
pore size of hydrophilic gels for electrophoresis and isoelectric focusion.
J. Biochem. Biophys. Methods 4:347–363.
11. Keller, E. F., and L. A. Segel, 1972. Travelling bands of chemotactic
bacteria - theoretical analysis. J. Theor. Biol. 30:235–248.
12. Lauﬀenburger, D., C. Kennedy, and R. Aris, 1984. Role of chemotaxis in
the transport of bacteria through saturated porous media. Bull. Math.
Biol. 46:19–40.
13. de Gennes, P.-G., 2004. Chemotaxis: the role of internal delays. Eur.
Biophys. J. 33:691–693.
14. DeWitt, S. K., and E. A. Adelberg 1962. The occurrence of a genetic
transposition in a strain of Escherichia coli. Genetics 47:577–685.
15. Sambrook, J., E. F. Fritsch, and T. Maniatis, 1989. Molecular cloning:
a laboratory manual. Cold Spring Harbour Press, N.Y., 2nd edition.
16. Rahn, O., and G. L. Richardson, 1941. Oxygen demand and oxygen
supply. J. Bacteriology 41:225–249.
17. Benke, K. K., and D. F. Hedger, 1996. Normalisation of brightness and
contrast in video displays. Eur. J. Phys. 17:268–274.
18. Tindall, M. J., P. K. Maini, S. L. Porter, and J. P. Armitage, 2008.
Overview of Mathematical Approaches Used to Model Bacterial Chemo-
taxis II: Bacterial Populations. Bull. Math. Biol. 70:1570–1607.
19. Nossal, R., 1972. Boundary movement of chemotactic bacterial popula-
tions. Math. biosci. 397–406.
20. Agladze, K., E. Budrene, G. Ivanitsky, V. Krinsky, V. Shakhbazyan, and
M. Tsyganov, 1993. Wave mechanisms of pattern formation in microbial
populations. Proc. R. Soc. Lond. B 253:131–135.


## Page 20


E. coli in soft agar
19
21. Woodward, D. E., R. Tyson, M. R. Myerscough, J. D. Murray, E. O.
Budrene, and H. C. Berg, 1995. Spatio-temporal patterns generated by
Salmonella typhimurium. Biophys. J. 68:2181–2189.
22. Ford, R. M., and R. W. Harvey, 2007. Role of chemotaxis in the trans-
port of bacteria through saturated porous media. Adv. Water Resour.
30:1608–1617.
23. Barton, J. W., and R. M. Ford, 1996. Mathematical model for charac-
terization of bacterial migration through sand cores. Biotechnol. Bioeng.
53:487–496.
24. Lapidus, I. R., and R. Schiller, 1976. Model for the chemotactic response
of a bacterial population. Biophys. J. 16:779–789.
25. Chen, K. C., R. M. Ford, and P. T. Cummings, 1998.
Perturba-
tion expansion of Alt’s cell balance equations reduces to Segel’s one-
dimensional equations for shallow chemoattractant gradients. SIAM J.
Appl. Math. 59:35–57.
26. Monod, J., 1949. The growth of bacterial cultures. Ann. Rev. Microbiol.
3:371–394.
27. Schantz, E. J., and M. A. Lauﬀer, 1962. Diﬀusion measurements in agar
gel. Biochemistry 1:658663.
28. Sharma, P. K., M. J. McInerney, and R. M. Knapp, 1993.
In situ
growth and activity and modes of penetration of Escherichia coli in
unconsolidated porous materials.
Appl. Environ. Microbiol. 59:3686–
3694.
29. Senozov, G., D. Joseleau-Petit, and R. D’ari, 2007.
Escherichia coli
physiology in Luria-Bertani Broth. J. Bacteriol. 189:8746–8749.
30. Ahmed, T., and R. Stocker, 2008. Experimental Verication of the Behav-
ioral Foundation of Bacterial Transport Parameters Using Microuidics.
Biophys. J. 95:4481–4493.
31. Murray, J. D., 2003.
Mathematical Biology. II. Spatial Models and
Biomedical Applications. Springer, New York, 3rd edition.
32. Lapidus, I. R., and R. Schiller, 1978. A model for traveling bands of
chemotactic bacteria. Biophys. J. 22:1–13.


## Page 21


E. coli in soft agar
20
33. Clark, D. A., and L. C. Grant, 2005.
The bacterial chemotactic re-
sponse reﬂects a compromise between transient and steady-state be-
haviour. Proc. Natl. Acad. Sci. USA 102:9150–9155.
34. Eiha, N., A. Komoto, S. Maenosono, J. Y. Wakano, J. Yamamoto, and
Y. Yamaguchi, 2002. The mode transition of the bacterial colony. Phys-
ica A 313:609–624.
35. Ben-Jacob, E., I. Cohen, and H. Levine, 2000. Cooperative self organi-
zation of microorganisms. Adv. Phys. 49:395–554.
36. Surette, M. G., M. B. Miller, and B. L. Bassler, 1999. Quorum sensing
in Escherichia coli, Salmonella typhimurium, and Vibrio harveyi: A
new family of genes responsible for autoinducer production. Proc. Natl.
Acad. Sci. USA 96:1639–1644.
37. Barak, R., and M. Eisenbach, 1999. Chemotactic-like response of Es-
cherichia coli cells lacking the known chemotaxis machinery but con-
taining overexpressed CheY. Mol. Microbiol. 31:1125–1137.
38. Liaw, S.-J., H.-C. Lai, S.-W. Ho, K.-T. Luh, and W.-B. Wang, 2000.
Inibition of virulence factor and swarming diﬀerentiation in Proteus
mirabilis by p-nitrophenylglycerol. J. Med. Microbiol. 49:725–731.
39. Lam, K. H., T. K. W. Ling, and S. W. N. Au, 2010. Crystal structure of
activated CheY1 from Helicobacter pylori. J. Bacteriol. 192:2324–2334.
40. Tailleur, J., and M. E. Cates, 2008. Statistical Mechanics of Interacting
Run-and-Tumble Bacteria. Phys. Rev. Lett. 100:218103.
41. Locsei, J. T., 2007. Persistence of direction increases the drift velocity
of run and tumble chemotaxis. J. Math. Biol. 55:41–60.
42. Segall, J. E., S. M. Block, and H. C. Berg, 1986. Temporal comparisons
in bacterial chemotaxis. Proc. Natl. Acad. Sci. USA 83:8987–8991.


## Page 22


E. coli in soft agar
21
Figure Legends
Figure 1.
(a) Early (top row) and advanced (bottom) stages of the migration of E.
coli AB1157 populations through LB agar of concentration C = 0.15-0.35%,
as labelled.
Shown are circular views (65 mm diameter) from minimally
processed images (see methods) of 100 mm diameter petris ﬁlled with 10
mm thick agar. (b-e) Azimuthally averaged radial intensity proﬁles from
the images (see text).
The time since inoculation in hours is indicated
throughout.
Figure 2.
Bacterial populations for C = 0.4-0.5%. Colonies (65 mm views) are initially
circular (top row), but quickly develop blebbing instabilities (bottom row).
Images were minimally processed as for Fig. 1a (see methods).
Figure 3.
Colony radius, r, against the time, t, since growth inception (see text) for
C = 0.15-0.4%, as shown. The inset shows a linear ﬁt to the raw radial data
for C = 0.3% against time since inoculation, ti. Similar ﬁts for all other
concentrations deﬁne the migration speed (slope) and the latency time ∆tl
(intersection with the time axis). Error bars are at most the size of a data
point.
Figure 4.
Experimental migration front speed as a function of concentration in the
range 0.15-0.35% together with a best ﬁt to the data using our model. Also
shown for best ﬁt parameters are the model ‘eﬃcient’ and ‘confused’ limits,
and the prediction from gas kinetic models (23). The inset shows the same
data but including points for C = 0.4-0.5%, labelled diﬀerently to indicate a
diﬀerent mode of migration at these concentrations. The model breakdown
in this region is evident.
Figure 5.
Theoretical predictions for the band proﬁles for the full model (left) and gas
kinetic models (23) (right) in the same range probed in experiments: C =
0.15-0.35%, as indicated. In the full model, as concentration is increased


## Page 23


E. coli in soft agar
22
the dynamics changes from chemotactic (sharp bands) to growth/diﬀusion
dominated (broad bands). This gradual transition is qualitatively the same
as observed in experiment (see Fig.
1), and is not predicted by the gas
kinetic model.


## Page 24


E. coli in soft agar
23
 0
 10
 20
 30
 40
 50
 60
 0
 5
 10
 15
 20
 25
 30
 35
< I >
r (mm)
17.7 h
 0
 10
 20
 30
 40
 50
 60
< I >
16.7 h
 0
 10
 20
 30
 40
 50
 60
< I >
15.7 h
 0
 10
 20
 30
 40
 50
 60
< I >
C=0.15%, (b)
14.7 h
 0
 10
 20
 30
 40
 50
 60
 0
 5
 10
 15
 20
 25
 30
 35
< I >
r (mm)
18.8 h
 0
 10
 20
 30
 40
 50
 60
< I >
17.8 h
 0
 10
 20
 30
 40
 50
 60
< I >
16.8 h
 0
 10
 20
 30
 40
 50
 60
< I >
15.8 h
C=0.2%, (c)
 0
 10
 20
 30
 40
 50
 60
 0
 5
 10
 15
 20
 25
 30
 35
< I >
r (mm)
19.3 h
 0
 10
 20
 30
 40
 50
 60
< I >
17.3 h
 0
 10
 20
 30
 40
 50
 60
< I >
15.3 h
 0
 10
 20
 30
 40
 50
 60
< I >
13.3 h
C=0.25%, (d)
 0
 10
 20
 30
 40
 50
 60
 0
 5
 10
 15
 20
 25
 30
 35
< I >
r (mm)
30.2 h
 0
 10
 20
 30
 40
 50
 60
< I >
27.7 h
 0
 10
 20
 30
 40
 50
 60
< I >
25.2 h
 0
 10
 20
 30
 40
 50
 60
< I >
22.7 h
C=0.3%, (e)
 0
 10
 20
 30
 40
 50
 60
 0
 5
 10
 15
 20
 25
 30
 35
< I >
r (mm)
47.7 h
 0
 10
 20
 30
 40
 50
 60
< I >
43.7 h
 0
 10
 20
 30
 40
 50
 60
< I >
39.7 h
 0
 10
 20
 30
 40
 50
 60
< I >
35.7 h
C=0.35%, (f)
Figure 1:


## Page 25


E. coli in soft agar
24
0.4%
0.45%
0.5%
63.8 h
95.3 h
73.1 h
165.6 h
100.0 h
261.2 h
Figure 2:


## Page 26


E. coli in soft agar
25
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
 0
 6
 12
 18
 24
 30
 36
r (mm)
t (h)
0.15%
0.2%
0.25%
0.3%
0.35%
0.4%
 0
 10
 20
 30
 40
 15  20  25  30  35
ti (h)
Figure 3:


## Page 27


E. coli in soft agar
26
 1
 10
 0.1
 0.15
 0.2
 0.25
 0.3
 0.35
 0.4
vF (mm/h)
C (%)
experiment
full model
efficient limit
confused limit
gas kinetic model
 0.01
 0.1
 1
 10
 0.1  0.2  0.3  0.4  0.5
Figure 4:


## Page 28


E. coli in soft agar
27
 50
 55
 60
 65
 70
 75
 80
R
C=0.35%, T=130
C=0.3%, T=60
C=0.25%, T=30
C=0.2%, T=25
C=0.15%, T=23
FULL MODEL
 50
 55
 60
 65
 70
 75
 80
R
C=0.35%, T=56
C=0.3%, T=34
C=0.25%, T=26
C=0.2%, T=24
C=0.15%, T=24
GAS KINETIC
Figure 5:

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1101_5063v2_migration_of_chemotactic_bacteria_in_soft_agar_role_of_gel_concentration
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2011/1101_5063V2_MIGRATION_OF_CHEMOTACTIC_BACTERIA_IN_SOFT_AGAR_ROLE_OF_GEL_CONCENTRATION.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

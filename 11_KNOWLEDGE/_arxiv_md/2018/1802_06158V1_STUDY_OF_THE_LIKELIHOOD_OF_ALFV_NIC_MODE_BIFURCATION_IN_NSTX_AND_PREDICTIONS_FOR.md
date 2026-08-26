---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1802.06158v1
source: arxiv
tags: [arxiv, knowledge, quantum, reference]
---
# 1802.06158v1_Study_of_the_likelihood_of_Alfvénic_mode_bifurcation_in_NSTX_and_predictions_for

> Source: 1802.06158v1_Study_of_the_likelihood_of_Alfvénic_mode_bifurcation_in_NSTX_and_predictions_for.pdf

> Pages: 13

---


## Page 1


Study of the likelihood of Alfvénic mode bifurcation in NSTX and predictions
for ITER baseline scenarios
V. N. Duarte∗
Princeton Plasma Physics Laboratory, Princeton University, Princeton, NJ, 08543, USA and
Institute of Physics, University of São Paulo, São Paulo, SP, 05508-090, Brazil
N. N. Gorelenkov, M. Schneller, E. D. Fredrickson, and M. Podestà
Princeton Plasma Physics Laboratory, Princeton University, Princeton, NJ, 08543, USA
H. L. Berk
Institute for Fusion Studies, University of Texas, Austin, TX, 78712, USA
(Dated: June 15, 2022)
Rare Alfvénic wave transitions between ﬁxed-frequency and chirping phases are identiﬁed in
NSTX, where Alfvénic waves are normally observed to exhibit either chirping or avalanching re-
sponses. For those transitions, we apply a criterion [Duarte et al, Nucl. Fusion 57, 054001 (2017)]
to predict the nature of fast ion redistribution in tokamaks to be in the convective or diﬀusive non-
linear regimes. For NSTX discharges in which the transition is not accompanied by changes in the
beam deposited power or modiﬁcations in the injected radiofrequency power, it has been found that
the anomalous fast ion transport is a likely mediator of the bifurcation between the ﬁxed-frequency
mode behavior and rapid chirping. For a quantitative assessment, global gyrokinetic simulations
of the eﬀects of electrostatic ion temperature gradient turbulence and trapped electron mode tur-
bulence on chirping were pursued using the GTS code. The investigation is extended by means of
predictive studies of the probable spectral behavior of Alfvénic eigenmodes for baseline ITER cases
consisting of elmy, advanced and hybrid scenarios. It has been observed that most modes are found
to be borderline between the steady and the chirping phases.
INTRODUCTION
Energetic-particle-driven
Alfvénic
instabilities
can seriously degrade the performance of present-
day and next-generation fusion devices [1–5]. The
control of these instabilities is, therefore, consid-
ered essential for the ITER performance [3, 6]. To
avoid and mitigate instabilities due to fast ions, it
is important to understand what is the nature of
the induced transport (e.g., coherent prompt losses
[7], convective losses due to phase-space structures
[8] and diﬀusive losses due to phase-space stochasti-
zation [9]) and the associated spectral character of
the instability [10]. For this purpose, in this paper
we investigate what conditions delineate the transi-
tion of Alfvénic modes between ﬁxed-frequency and
chirping phases in NSTX. In addition to that, typ-
ical ITER cases are analyzed and predictions are
∗vduarte@pppl.gov
made regarding the likelihood of modes to chirp or
to oscillate steadily at a nearly constant frequency.
From the theory perspective, the onset of chirp-
ing has been linked with the relative importance
between stochastic and coherent processes aﬀecting
the resonant population [11–14].
Experimentally,
several elements have been identiﬁed as altering the
Alfvén wave spectral behavior, such as radiofre-
quency (RF) waves [15–17], background plasma
beta [18], beam beta [8], 3D ﬁelds [19] and rota-
tional transform [20, 21]. Recently, the rare emer-
gence of chirping in DIII-D has been shown to be
related to a marked decrease of the inferred fast ion
micro-turbulence levels [10].
In Refs. [10, 22], theoretical predictions for real-
istically computed tokamak modes were compared
with experiments.
It was observed, both in the
theory and in the experiment, that fast ion micro-
turbulence is a mediator between mode nature tran-
sition for several typical tokamak scenarios, while
exhibiting little macroscopic anomalous transport
arXiv:1802.06158v1  [physics.plasm-ph]  16 Feb 2018


## Page 2


2
[23]. The fact that ion anomalous diﬀusity is typi-
cally much smaller in spherical tokamaks (STs) than
in conventional tokamaks has been proposed [10]
as the explanation for the longstanding observation
that chirping is more common in STs relative to con-
ventional tokamaks. A criterion proposed to distin-
guish between the two typical scenarios (chirping
vs ﬁxed-frequency), which was shown to be sensi-
tive to the relative strength of scattering (from col-
lisions and micro-turbulence) and drag processes,
ultimately translates into a condition for the appli-
cability of reduced quasilinear modeling for realistic
tokamak eigenmodes.
Recently, DIII-D had ded-
icated experiments [24] to stress-test the chirping
prediction [10]. The experiments employed negative
plasma triangularity as a means to decrease turbu-
lence levels. In those shots, chirping was much more
prevalent than in the usual and more turbulent oval
or positive triangularity cases. In addition, chirping
was also observed for modes located around inter-
nal transport barriers, even in positive triangular-
ity. From the numerical side, turbulence stochas-
ticity has been recently included in a bump-on-tail
simulation [25], which showed its eﬀect on chirping
suppression.
The purpose of this paper is twofold. First, we in-
vestigate whether the conclusion of chirping based
on turbulence holds for NSTX, where ion micro-
turbulence is already observed to be low (as com-
pared to ion neoclassical transport [26]), or whether
there are other elements that determine the mode
nonlinear evolution. This is addressed by means of
global gyrokinetic simulations. Chirping is a ma-
jor issue in connection with fast ion losses in toka-
maks and there is currently no understanding of
how to systematically avoid them in NSTX-U. The
second goal of this work is an attempt to antic-
ipate what will be the probable spectral nature of
toroidicity-induced and reversed shear Alfvén eigen-
modes (TAEs and RSAEs) in ITER. The proﬁles
employed in this study are ﬁducially constructed
using a transport code.
This article is organized as follows. In Sec. II, we
present gyrokinetic analysis of Alfvénic mode bifur-
cation in NSTX and its comparison with theoretical
predictions. Sec. III is devoted to a study of the
possibility of occurrence of mode chirping in ITER
baseline scenarios (reversed shear, hybrid and elmy
H mode) and Sec. IV presents discussions and con-
clusions.
ANALYSES OF RARE TRANSITIONS
BETWEEN CONSTANT FREQUENCY AND
CHIRPING IN NSTX
A distinctive feature of Alfvénic wave behavior in
STs [27] as compared to conventional tokamaks is
that chirping and avalanches are customary in the
former and infrequent in the latter.
The ubiqui-
tous Alfvénic chirping in NSTX is observed to be
a precursor of the phase locking of high-intensity
modes of several toroidal mode numbers, known as
avalanche [28, 29]. During the avalanche, the es-
cape of a substantial fraction of fast ions occurs,
which can typically reach up to 40%. Wave chirp-
ing has been identiﬁed to transition to avalanches
in NSTX only when the fast particle energy was
greater than about 30% of the total plasma energy
[30], with higher chances of avalanches to appear
correlating with lower values of maximum energetic
ion speed divided by the Alfvén speed [27]. The con-
ditions determining the likelihood of the chirping-
to-avalanche transition are therefore, to a certain
extent, experimentally identiﬁed. We therefore turn
our attention to the likelihood of transition from a
steady frequency to chirping instead.
Typically in NSTX, Afvénic modes are already
chirping when they ﬁrst appear in a spectrogram,
although mode intensity can vary considerably. The
constant frequency phase is normally not observed.
Eventually chirping modes undergo conversion to
the avalanche phase as more beam power is injected.
It is often challenging to identify cases in which
they appear in their ﬁxed-frequency phase. From
an extensive NSTX database, we have selected rare
steady-to-chirping transitions, with no inﬂuence of
RF or 3D ﬁelds, in order to test the proposed in-
terpretation that fast ion micro-turbulence can be a
determining factor behind the transition. Although
rare, these transitions oﬀer a unique testbed to de-
cipher the parameters that need to be varied to in-
duce change in the nonlinear character of modes.
For some cases, we have observed that chirping
and steady phases appear to co-exist for diﬀerent
Alfvénic modes, which possibly indicate that each


## Page 3


3
mode has its own threshold to undergo transition
between the two phases. From the initial set of tran-
sitions, we observe that in most cases the modes
switch over to chirping because of an increase in
the applied beam power, with the spectral change
happening within the characteristic fast ion slow-
ing down time. This increases the strength of the
drive and likely allows the modes to access a harder
nonlinear phase. This observation is in agreement
with Ref. [8], that reported a correlation between
chirping and high fast ion pressure. The chances of
chirping increasing at higher drive may be related to
a convective ampliﬁcation mechanism [31] and also
be related to mode structure deformation due to the
presence of EPs, both of which are beyond the scope
of this work. Therefore, to obtain a comparable set
of steady-to-chirping transitions, we further analyze
only a sub-set of cases with roughly constant beam
beta throughout the transition.
Only three dis-
charges satisﬁed this constraint, among which only
two allowed for a successful equilibrium reconstruc-
tion: NSTX shots #128453 and #135388.
NSTX #135388
0.20
0.25
0.30
0.35
t [s]
0
2
4
6
8
10
χi [m2/s]
rho=0.30
rho=0.40
rho=0.50
NSTX #128453
0.260
0.273
0.287
0.300
t [s]
0
1
2
3
4
5
6
χi [m2/s]
rho=0.20
rho=0.25
rho=0.30
frequency (kHz)
150
100
50
0
time (s)
0.26
0.27
0.29
0.30
0.28
NSTX 128453
frequency (kHz)
150
100
50
0
time (s)
0.26
0.27
0.29
0.30
0.28
200
0.31
0.32
NSTX 135388
Figure 1. Correlation between the onset of Alfvénic chirping (lower plots) and an improvement of thermal ion
conﬁnement, as inferred from TRANSP (upper plots), for NSTX pulses #128453 and #135388.
Previous chirping analysis [10, 22] relied on trans-
port coeﬃcients calculated by TRANSP for ther-
mal ions. The fast ion coeﬃcients were then scaled
from the thermal ones using the relations reported
in Ref.
[32–34].
These are based on an analytic
approach and numerical examination of a simula-
tion database. One can appreciate in Fig. 1 the
correlation between the emergence of chirping and
the decrease of thermal ion turbulent levels, which
can be used as a proxy for the fast ion anomalous
diﬀusivity [35]. The values of χi in Fig. 1 are un-
usually high before the start of the chirps. In the
present work, however, we analyze new cases more
quantitatively consistent by performing individual
gyrokinetic simulations at given time slices of the
mode evolution, taking into consideration the ex-


## Page 4


4
perimental plasma parameters for each individual
discharge. This allows us to understand what type
of turbulence is dominant and oﬀers insights on its
key characteristics, such as the origin of its drive.
The global turbulence simulations reported in
this study are carried out using the Gyrokinetic
Tokamak Simulation (GTS) code [36, 37]. The
GTS code performs nonlinear gradient-driven elec-
trostatic turbulence simulations based on a gen-
eralized gyrokinetic simulation model using a δf
particle-in-cell approach. The presented GTS simu-
lations of NSTX discharges #128453 and #135388
take into account a comprehensive inﬂuence of a
number of relevant physical eﬀects, including fully
kinetic electrons, realistic geometry constructed us-
ing experimental data as well as plasma proﬁles
which are read from TRANSP [38]. The global sim-
ulations cover a wide region of normalized minor
radii, from rtor = 0.2 to 0.8 (rtor represents the
square root of the toroidal ﬂux normalized with its
value at the separatrix).
Convergence in marker
numbers was found for 80 particles per cell per
species. The spatial grid size in the perpendicular
direction is approximately equal to or less than the
local ion gyroradius ρi. The wavenumber range that
is simulated is k⊥ρi ≲2, which covers the typical
low-k turbulence due to ion temperature gradient
(ITG) mode and trapped electron mode (TEM).
frequency (kHz)
150
100
50
0
time (s)
0.26
0.27
0.29
0.30
0.28
200
0.31
0.32
NSTX 135388
frequency (kHz)
150
100
50
0
time (s)
0.26
0.27
0.29
0.30
0.28
NSTX 128453
0.2
0.3
0.4
0.5
0.6
0.7
0.8
radius
0
0.005
0.01
0.015
0.02
<  
2 >
NSTX#128453
t=[2.30e-04,2.70e-04], at t=265ms
t=[2.30e-04,2.70e-04], at t=290ms
0.2
0.3
0.4
0.5
0.6
0.7
0.8
radius
0
0.05
0.1
0.15
0.2
0.25
0.3
0.35
<  
2 >
NSTX#135388
t=[2.30e-04,2.70e-04], at t=265ms
t=[2.30e-04,2.70e-04], at t=300ms
Before chirping, 265ms
During chirping, 290ms
Electrostatic turbulence fluctuation
Electrostatic turbulence fluctuation
Before chirping, 265ms
During chirping, 300ms
Figure 2. Correlation between low anomalous transport and Alfvénic chirping, as calculated by GTS global gyroki-
netic simulations, for NSTX pulses #128453 and #135388.
The spatiotemporal evolution of turbulence in-
tensity, deﬁned as

δΦ2
≡⟨(eδφ/Ti)2⟩, with δφ be-
ing the electrostatic potential ﬂuctuation, Ti the ion
temperature at the reference radius rtor = 0.5 and
e the elementary charge, is displayed in Figs. 2, 3
and 4. For #128453, the fully developed ITG/TEM
turbulence spreads mainly around rtor = 0.36 and
rtor = 0.52. For #135388, ITG turbulence evolves
between rtor = 0.25 and 0.6 with a peak around
rtor = 0.32. The location of the peaks is consis-
tent with the radial position with strongest tem-
perature proﬁle gradients.
Interestingly, for both


## Page 5


5
cases, the level of turbulence is remarkably reduced
as the mode undergoes transition to chirping, in
agreement with the theory prediction and the ob-
servation on DIII-D [10]. The evolution and satu-
ration of the potential perturbation are illustrated
in logarithmic scale in Fig. 5, using the equilibrium
proﬁles before and during the chirping.
Interestingly, the turbulent levels in NSTX dis-
charges #128453 and #135388 are found to be re-
duced due to diﬀerent eﬀects. For #128453, it is ob-
served (Fig. 6(a))that the ion temperature gets in-
creasingly ﬂattened in the core between t = 265ms
and t = 300ms, thus depleting the drive of the
ITG modes.
For #135388, the q proﬁle, which
was monotonic at t = 265ms, becomes reversed at
t = 290ms (Fig. 6(b)). The simulation result is in
agreement with the prediction that a reversed q pro-
ﬁle should have an eﬀect on the micro-turbulence
supression [39].
The extraordinarily high electrostatic turbu-
lence potential for case #135388 (as compared to
#128453) can be partially understood when looking
at one of the main driving sources, η = ∇Ti/∇ni.
In both time slices of the discharge NSTX #135388,
this value is up to a factor of 5 to 6 higher than
in the scenarios of NSTX #128453. Especially at
lower radii (where the stabilizing shear is lower),
this high η value is considered responsible for the
high turbulence levels.
In order to evaluate the criterion for chirping like-
lihood proposed in [10], we ﬁrst need to categorize
the modes that are measured. For this purpose, we
employ the reﬂectometer data to provide informa-
tion regarding the mode structure, which can be
compared with the eigenmodes calculated by the
NOVA code [40, 41].
Due to lower density, for
shot #135388 only two channels of the reﬂectome-
ter could be used, which did not allow for proper
mode identiﬁcation. The measured mode structure
compared to its best match from NOVA results is
shown in Fig. 7 for shot #128453 before and during
the chirping phase.
In order to calculate the relative importance be-
tween fast ion stochasticity arising from turbulent
processes and collisional processes, we use the ap-
proach introduced by Lang and Fu [42], which in
the notation deﬁned in [22], is approximately given
(a)
(b)
Figure 3. Averaged squared electrostatic potential ﬂuc-
tuation normalized with the square of the ion temper-
ature at mid-radius (indicated by the color code), as a
function of time, expressed in units of 10−4s and the
minor radius, expressed in terms of the square root of
the toroidal ﬂux divided by the toroidal ﬂux at the edge.
The results were obtained by the GTS code for the time
slices (a) before chirping starts, at t = 265ms and (b)
during the chirping, at t = 290ms, for NSTX discharge
#128453.
The color code scale is the same for both
plots, which indicates a substantial reduction of the tur-
bulent activity from (a) to (b).


## Page 6


6
(a)
(b)
Figure 4. Averaged squared electrostatic potential ﬂuc-
tuation normalized with the square of the ion temper-
ature at mid-radius (indicated by the color code), as a
function of time, expressed in units of 10−4s and the
minor radius, expressed in terms of the square root of
the toroidal ﬂux divided by the toroidal ﬂux at the edge.
The results were obtained by the GTS code for the time
slices (a) before chirping starts, at t = 265ms and (b)
during the chirping, at t = 300ms, for NSTX discharge
#135388.
The color code scale is the same for both
plots, which indicates a substantial reduction of the tur-
bulent activity from (a) to (b).
(a)
(b)
Figure 5. GTS computation of the time evolution of the
averaged squared electrostatic potential ﬂuctuation nor-
malized with the square of the ion temperature at mid-
radius, as a function of time for NSTX discharges (a)
#128453 and (b) #135388, before (continuous curves)
and during (dashed curves) the chirping.
The colors
indicate several radial positions.
by
νturb
νscatt
⋍


DEP

qEP
mEP
∂ψ
∂r
2
2ν⊥R2µB


1/3
(1)
where νturb and νscatt are the eﬀective turbulent and
collisional scattering frequencies, DEP , qEP and
mEP are the energetic particle diﬀusivity, charge
and mass, respectively. ψ is the poloidal magnetic
ﬂux divided by 2π, r is the minor radius, ν⊥is the
90o pitch angle scattering rate, R is the major ra-
dius, µ is the magnetic moment and B is the mag-
netic ﬁeld intensity.
DEP is calculated using the
scalings of [32]. We note, however, that the GTS


## Page 7


7
code is currently being extended to include a pas-
sive energetic ion population. It should allow for
more accurate estimates of DEP in the future.
The weakly nonlinear mode dynamics can be de-
scribed by an integro-diﬀerential, time-delayed cu-
bic equation for the mode amplitude [11, 43]. The
evolution to chirping has been identiﬁed to be asso-
ciated with the explosion of the solution of the cu-
bic equation in a ﬁnite time [44]. It has been shown
that, for realistic tokamak modes, a criterion for
chirping likelihood Crt [10] should involve a phase-
space integration over the multiple resonance sur-
faces of a given mode. Crt is sensitive to the ratio
between the eﬀective frequencies due to stochastic
(νstoch) and coherent (νcoher) processes. We take
νstoch = νscatt + νturb and νcoher = νdrag, where
νdrag is the eﬀective frequency associated with col-
lisional drag (slowing down). For the chirping cri-
terion Crt evaluation purpose, we use the kinetic
postprocessor NOVA-K [45, 46]. We ﬁnd that at
265ms, Crt = +0.0027 and at 290ms, Crt = −0.34,
which is consistent with the experiment (Crt < 0
implies more probability of chirping while Crt > 0
predicts that the wave will likely oscillate at a con-
stant frequency [10]).
PREDICTIVE STUDIES FOR ITER
BASELINE SCENARIOS
ITER will employ two negative-ion-based neutral
beam injection (NBI) sources, which will account
for 33MW of injected power [47, 48].
Both the
3.5MeV fusion-born alpha particles and the tan-
gentially injected 1MeV NBI ions will have supra-
Alfvénic velocities, allowing them to interact with
TAEs via their main resonance. An upper limit of
5% of fast ion loss has been established for ITER
to sustain a burning plasma [6]. Therefore, to un-
derstand the relevant mode evolution and fast ion
transport due to Alfvénic instabilities in ITER, it
is instructive to anticipate whether the modes will
be more prone to have their frequencies locked to
the background equilibrium or be subject to rapid
chirps [49].
In recent years, a number of publi-
cations have addressed various aspects of fast ion
conﬁnement in ITER, both linearly and nonlinearly
[50–62]. Most of these previous studies quantita-
0.2
0.4
0.6
0.8
radius
0
0.2
0.4
0.6
0.8
Ti /keV
(a)
1
2
3
4
5
#128453, at t=265 ms
#128453, at t=290 ms
1
2
3
4
5
q
0.2
0.4
0.6
0.8
radius
0
0.5
1
1.5
2
Ti /keV
(b)
0
1
2
3
4
5
6
7
#135388, at t=265 ms
#135388, at t=300 ms
0
1
2
3
4
5
6
7
q
Figure 6. Ion temperature proﬁle (red) and safety fac-
tor proﬁle (black), before (continuous curves) and after
(dot-dashed curves) the transition to chirping. Simu-
lations show that for shot 128453 (part (a)), the tur-
bulence drive is depleted via a ﬂattening of Ti at mid-
radius while for shot 135388 (part (b)), it is found that
the reversal of q has a stabilizing eﬀect on the turbu-
lence.
tively addressed stability and transport features.
In this work we analyze another relevant aspect of
the problem, which is the prediction of the prob-
able character that Alfvénic waves will assume in
ITER. This can be helpful in anticipating the theo-
retical and numerical tools that may need to be de-
veloped and employed. For example, for situations
in which chirping is not expected to take place, re-


## Page 8


8
t=265.0ms, n=2
1.1
1.2
1.3
1.4
1.5
R  [m]
-0.4
-0.2
0.0
0.2
0.4
0.6
0.8
δn/n [%]
measurements
NOVA
fmeas=74.6+/-2.4kHz
fNOVA=50.064kHz
Rshift=0.7cm
(a)
t=290.0ms, n=2
1.1
1.2
1.3
1.4
1.5
R  [m]
-0.4
-0.2
0.0
0.2
0.4
0.6
0.8
δn/n [%]
measurements
NOVA
fmeas=61.8+/-0.6kHz
fNOVA=60.426kHz
Rshift=-3.3cm
(b)
Figure 7. Identiﬁcation of mode structures for an n = 2
mode NSTX shot 128453 calculated by NOVA (in red)
compared with reﬂectometer measurements (in black)
for (a) t = 265ms and (b) t = 290ms. δn is the per-
turbed density while n is the background density. The
reﬂectometer measurement positions are shown by the
cyan diamonds.
duced quasilinear modeling [63–65] can be enough
for a quantitative assessment of fast ion redistribu-
tion due to Alfvénic modes.
ITER plasma performance can change consid-
erably depending on the relative external heating
power between NBI, ion cyclotron resonant heat-
ing (ICRH) and electron cyclotron resonant heat-
ing (ECRH). Heating mixes with high NBI power
increase the toroidal rotation and the fusion yield
but have the disadvantage of triggering Alfvénic in-
stabilities [66].
Therefore it is necessary to con-
sider Alfvénic spectral behavior for the main three
scenarios [67] and make use of diﬀerent plasma pro-
ﬁles that the TRANSP code predicts for them. The
ﬁrst scenario is a reversed shear, advanced (steady
state) scenario in which most of the plasma current
is driven non-inductively (bootstrap current), with
the current density peak displaced from the center
and a non-monotonic safety factor q proﬁle. The
second scenario is an elmy H mode, in which q is
minimum (with a value just below 1) at the cen-
ter. Finally, the third scenario is a hybrid one, that
has weak or low magnetic shear and the current,
although modiﬁed externally, does not completely
rely on non-inductive mechanisms.
We utilize plasma parameters from a previous
TRANSP/TSC analysis [57], requiring Q ≥10
(where Q is the ratio between the power gener-
ated by fusion reactions and the power input to the
plasma). We employ the mode structures and reso-
nances previously reported in [57], which had their
linear stability already assessed. For each ITER sce-
nario, we take the most linearly unstable modes and
limit ourselves to toroidal mode numbers n from 7
to 11.
In order to be able to account for distinctive tur-
bulence levels for each of the three baseline scenar-
ios, we use the results of Ref. [32] to scale the fast
ion diﬀusivity with the thermal ion one, which is
obtained with TRANSP. We note that Albergante
et al [68–70] used the GENE code [71] to study
the diﬀusivity of fast ions due to ITG turbulence
speciﬁcally for ITER-relevant scenarios [6, 67]. An
alternative for our study would be to use the com-
puted fast ion diﬀusivity in terms of the parallel and
perpendicular components of the velocity, shown in
Fig. 6 of Ref. [68]. We note that the ﬁgure was pro-
duced for the speciﬁc case of E = 30Te. However,


## Page 9


9
0
0.25
0.5
0.75
1
0
1
2
3
4
5
6
7
ψθ /ψθ,1
Ω2
ΩA
2
modes radial localization
n=7
n=8
n=9
n=10
n=11
n=7
n=8
n=9
n=10
n=11
n=7
n=8
n=9
n=10
n=11
reversed shear
hybrid
elmy
Figure 8. Radial localization and frequency of the TAEs
and RSAEs used in the chirping prediction simulations
of Fig. 9. Dotted (red), dashed (blue) and dot-dashed
(green) curves indicate the envelope of the continuum
for reversed-shear, hybrid and H mode elmy cases. For
the purpose of obtaining the envelope, a high toroidal
mode number n = 30 was used. Ψθ is the poloidal mag-
netic ﬂux and Ψθ,1 is its value at the plasma separa-
trix. The modes angular frequency Ωis nomalized with
ΩA = vA,axis/(q1R0), where vA,axis is the Alfvén speed
at the magnetic axis, q1 is the safety factor at the edge
and R0 is the major radius at the geometric center.
to make an estimate less approximate, one can use
the result in Fig. 5b of Ref. [68] that shows the de-
pendence of the diﬀusivity on the temperature, for
the situation when the velocity-space is integrated
over, where it can be inferred that DEP ∝T −1
i
.
The latter expression can be used as a correction
factor to the diﬀusivity resolved in velocity for the
case E = 30Te, in order to have a better estimate for
the speciﬁc fast ion energy and background temper-
ature for each speciﬁc ITER case. Interestingly, we
ﬁnd that the scalings found in Ref. [32] provide val-
ues for DEP reasonably compatible with the ones
extracted from Albergante’s work, for most cases
examined here.
◆
◆
◆
◆
◆
●
●
●
●
●
0
10
20
30
40
50
60
-0.75
-0.5
-0.25
0
0.25
0.5
ITER reversed shear (advanced) scenario
n=7
n=8
n=9
n=10
n=11
(a)
chirping likely
fixed frequency
likely
◆
◆
◆
◆
◆
●●
●
●
●
0
5 10 15 20 25 30 35 40
-1.25
-1
-0.75
-0.5
-0.25
0
0.25
0.5
ITER hybrid scenario
n=7
n=8
n=9
n=11
n=10
(b)
chirping likely
fixed frequency
likely
◆
◆
◆
◆
◆
●
●●
●
●
0
5 10 15 20 25 30 35 40
-1
-0.75
-0.5
-0.25
0
0.25
0.5
ITER elmy H mode scenario
n=7
n=8
n=9
n=10
n=11
(c)
chirping likely
fixed frequency
likely
Figure 9.
Evaluation of the chirping criterion Crt
[10, 22] for the baseline scenarios (a) reversed shear,
(b) hybrid and (c) elmy h mode. It is shown the predic-
tion for individual modes with (arrowhead diamonds)
and without (arrow tail disks) the inclusion of micro-
turbulence stochasticity in the model. The arrows do
not describe any meaningful path but simply connect
two points corresponding to the same mode.


## Page 10


10
The frequency and radial localization of the 15
modes used in the analysis are shown in Fig.
8,
overlaid with the envelopes of the continua. These
envelopes were calculated by interpolating the tips
of each continuum curve, using high values of n in
order to be able to produce more reliable curves,
representative of all modes of a given scenario.
The fact that the TAEs and the RSAEs in ITER
can be driven by both alphas and beam ions is taken
into account in the analysis via a weighted average
of the individual contributions entering Eq. 1. The
predictions for the three baseline scenarios for ITER
are shown in Fig. 9. They indicate that most of
the unstable TAEs and RSAEs are located close to
the boundary between the chirping and steady fre-
quency regions. We note that without the addition
of micro-turbulent stochasticity in the model, all
modes are predicted to lie in the region that allows
for chirping. However, upon the addition of νturb to
νscatt (represented by the arrows in Fig. 9), most
modes get very close to the borderline Crt = 0.
Since there could be a considerable error in the es-
timate of DEP , we show error bars in Fig. 9, which
indicate by how much the prediction for Crt would
change if DEP is multiplied by two (upper bars)
and divided by two (lower bars).
It is worth comparing the predictions for ITER
with previous analyses of DIII-D discharges [10].
Because of the inverse dependence of DEP on the
EP energy, we see that for ITER, DEP is about an
order of magnitude smaller with respect to typical
values inferred for DIII-D. On the other hand, the
Alfvén speed vA is about 2.5 times larger in ITER
because of higher ﬁeld, which means that the 90o
degree pitch angle scattering rate ν⊥(see deﬁnition
in Eq. 3 of Ref. [22]) at vA is also an order of mag-
nitude smaller than in DIII-D. The combination of
the other parameters involved in the ratio 1 do not
change appreciably in the comparison between the
two tokamaks, therefore, the ratio 1 appears to be
of the same order in DIII-D and in ITER.
Each ITER mode in Fig.
9 appears to have
its own threshold for steady/chirping transition.
Therefore it is challenging to draw general conclu-
sions regarding their spectral nature. It is however
notorious that most modes appear to be close to the
borderline. This means that any additional stochas-
tic mechanism, such as RF heating, interaction with
neoclassical tearing modes (NTMs), ﬁeld ripples,
energy diﬀusion, mode overlap, would contribute to
make the modes cross towards the positive Crt re-
gion. ITER will be able to operate on a range of
ICRH power, which can deliver up to 20MW [66].
It remains to be understood how strong the eﬀect of
ICRH can be on the fast ions that are in resonance
with Alfvén waves.
SUMMARY AND CONCLUSIONS
We reported a study of rare transitions be-
tween mode constant frequency and mode chirp-
ing in NSTX using global gyrokinetic simulation
and chirping criterion analysis. The results indicate
that fast ion anomalous diﬀusion likely mediates the
transition, for cases when RF-induced diﬀusion and
changes in beam beta are not present. The chirping
phase is observed to be achieved following a marked
decrease in the turbulent ﬁeld amplitude, which is
consistent with the interpretation proposed in Ref.
[10].
We have studied the likelihood of TAEs to ex-
hibit chirping for typical ITER scenarios (reversed
shear, elmy and hybrid). A few modes were found to
be distinctly on either oscillation regime. However,
most modes were found to be borderline between
the two phases. If additional mechanisms for de-
tuning fast ion from a resonance (e.g., induced by
3D ﬁelds, ICRH, NTMs, energy diﬀusion) will be
important in ITER, then most modes can be ex-
pected to oscillate at a constant frequency. Each
of these additional mechanisms, however, deserve a
study on their own, which is beyond the scope of
this work. We also note that the constraint Q > 10
imposed by the analysis means that the thermal dif-
fusion could be too optimistic, which would increase
the likelihood for chirping. Besides, this constraint
may mean that we are overestimating the drive of
the modes.
The analysis we presented in both parts of this
work assumed that the modes remain isolated
throughtout their evolution.
We note, however,
that because the toroidal mode numbers of Alfvénic
waves in ITER will be higher compared to present-
day tokamaks, also higher poloidal mode numbers
will be important. This can lead to an enhanced


## Page 11


11
phase-space density of resonances (as an illustra-
tion, see Fig. 9 of [53]), which can make resonance
overlap more likely to occur. In the region of over-
lap, resonant particles should move stochastically,
which contributes to destroy phase-space structures
that sustain coherent phenomena, such as chirping.
In this case, our predictions with respect to the non-
linear character of Alfvénic modes, which assumed
isolated resonances, are no longer valid. In the fu-
ture, the description of the chirping structures using
more sophisticated numerical tools, such as guiding
center codes or initial value codes, could provide a
more detailed picture of the mode dynamics in re-
alistic toroidal geometry. They could be used as a
comparison with the predictions from the present
reduced modeling eﬀort.
ACKNOWLEDGMENTS
This work was supported by the US Depart-
ment of Energy (DOE) under contract DE-AC02-
09CH11466 and by the São Paulo Research Foun-
dation (FAPESP) under grants 2012/22830-2 and
2014/03289-4. The authors acknowledge Z. X. Lu
for pointing out the stabilizing eﬀect of a reversed
shear proﬁle, S. M. Kaye for preparing a TRANSP
run for NSTX shot 128453 and S. Ethier for prepar-
ing the TRANSP proﬁles and equilibrium input
ﬁles for GTS. The GTS simulations for this work
were run on the supercomputer HYDRA, provided
by the Max Planck Computing and Data Facility
(MPCDF) in Garching, Germany. Computational
resources as well as support are gratefully acknowl-
edged.
[1] W. W. Heidbrink and G. J. Sadler, Nuclear Fusion
34, 535 (1994).
[2] P. Lauber, Physics Reports 533, 33 (2013).
[3] N. Gorelenkov, S. Pinches, and K. Toi, Nucl. Fu-
sion 54, 125001 (2014).
[4] L. Chen and F. Zonca, Rev. Mod. Phys. 88, 015008
(2016).
[5] W. W. Heidbrink, Phys. Plasmas 15, 055501
(2008), http://dx.doi.org/10.1063/1.2838239.
[6] ITER Physics Expert Group on Energetic Parti-
cles, Heating and Current Drive and ITER Physics
Basis Editors, Nuclear Fusion 39, 2471 (1999).
[7] X. Chen, M. E. Austin, R. K. Fisher, W. W. Hei-
dbrink, G. J. Kramer, R. Nazikian, D. C. Pace,
C. C. Petty,
and M. A. Van Zeeland, Phys. Rev.
Lett. 110, 065004 (2013).
[8] W. W. Heidbrink, Plasma Phys. Control. Fusion
37, 937 (1995).
[9] M.
García-Muñoz,
N.
Hicks,
R.
van
Voorn-
veld, I. G. J. Classen, R. Bilato, V. Bobkov,
M.
Bruedgam,
H.-U.
Fahrbach,
V.
Igochine,
S. Jaemsae, M. Maraschek,
and K. Sassenberg
(ASDEX Upgrade Team), Phys. Rev. Lett. 104,
185002 (2010).
[10] V. N. Duarte, H. L. Berk, N. N. Gorelenkov, W. W.
Heidbrink, G. J. Kramer, R. Nazikian, D. C. Pace,
M. Podestà , B. J. Tobias, and M. A. V. Zeeland,
Nuclear Fusion 57, 054001 (2017).
[11] H. L. Berk, B. N. Breizman, and M. Pekker, Phys.
Rev. Lett. 76, 1256 (1996).
[12] H. Berk, B. Breizman, and N. Petviashvili, Phys.
Lett. A 234, 213 (1997).
[13] M. K. Lilley, B. N. Breizman,
and S. E. Shara-
pov, Phys. Rev. Lett. 102 (2009), 10.1103/phys-
revlett.102.195003.
[14] M.
K.
Lilley,
B.
N.
Breizman,
and
S.
E.
Sharapov,
Phys.
Plasmas
17,
092305
(2010),
http://dx.doi.org/10.1063/1.3486535.
[15] D. Maslovsky, B. Levitt, and M. E. Mauel, Phys.
Rev. Lett. 90, 185001 (2003).
[16] D.
Maslovsky,
B.
Levitt,
and
M.
E.
Mauel,
Physics
of
Plasmas
10,
1549
(2003),
http://dx.doi.org/10.1063/1.1557072.
[17] E. Fredrickson, G. Taylor, N. Bertelli, D. Darrow,
N. Gorelenkov, G. Kramer, D. Liu, N. Crocker,
S. Kubota,
and R. White, Nuclear Fusion 55,
013012 (2015).
[18] M. P. Gryaznevich and S. E. Sharapov, Plasma


## Page 12


12
Physics and Controlled Fusion 46, S15 (2004).
[19] A. Bortolon, W. W. Heidbrink, G. J. Kramer,
J.-K. Park, E. D. Fredrickson, J. D. Lore,
and
M. Podestà, Phys. Rev. Lett. 110, 265008 (2013).
[20] A. Melnikov, L. Eliseev, F. Castejón, C. Hidalgo,
P. Khabanov, A. Kozachek, L. Krupnik, M. Liniers,
S. Lysenko, J. de Pablos, S. Sharapov, M. Uﬁmt-
sev, V. Zenin, and HIBP Group and TJ-II Team,
Nuclear Fusion 56, 112019 (2016).
[21] A. Melnikov, L. Eliseev, E. Ascasíbar, A. Cappa,
F. Castejón,
C. Hidalgo,
T. Ido,
J. Jiménez,
A. Kozachek, L. Krupnik, M. Liniers, S. Lysenko,
K. Nagaoka, J. de Pablos, A. Shimizu, S. Sharapov,
M. Uﬁmtsev, S. Yamamoto, and HIBP group and
TJ-II team, Nuclear Fusion 56, 076001 (2016).
[22] V. N. Duarte, H. L. Berk, N. N. Gorelenkov,
W. W. Heidbrink, G. J. Kramer, R. Nazikian,
D. C. Pace, M. Podestà,
and M. A. V. Zee-
land,
Physics
of
Plasmas
24,
122508
(2017),
https://doi.org/10.1063/1.5007811.
[23] D. C. Pace, M. E. Austin, E. M. Bass, R. V. Budny,
W. W. Heidbrink, J. C. Hillesheim, C. T. Holcomb,
M. Gorelenkova, B. A. Grierson, D. C. McCune,
G. R. McKee, C. M. Muscatello, J. M. Park, C. C.
Petty, T. L. Rhodes, G. M. Staebler, T. Suzuki,
M. A. Van Zeeland, R. E. Waltz, G. Wang, A. E.
White, Z. Yan, X. Yuan,
and Y. B. Zhu, Phys.
Plasmas 20, 056108 (2013).
[24] M. A. Van Zeeland et al (15th IAEA Technical
Meeting on the Energetic Particles in Magnetic
Conﬁnement Systems, invited talk, 2017).
[25] B. J. Q. Woods, V. N. Duarte, A. J. De-Gol, N. N.
Gorelenkov,
and R. G. L. Vann, Nuclear Fusion
(2018), 10.1088/1741-4326/aaa9fd.
[26] S. Kaye,
F. Levinton,
D. Stutman,
K. Tritz,
H. Yuh, M. Bell, R. Bell, C. Domier, D. Gates,
W. Horton, J. Kim, B. LeBlanc, N. Luhmann,
R. Maingi, E. Mazzucato, J. Menard, D. Mikkelsen,
D. Mueller, H. Park, G. Rewoldt, S. Sabbagh,
D. Smith,
and W. Wang, Nucl. Fusion 47, 499
(2007).
[27] K. G. McClements and E. D. Fredrickson, Plasma
Physics and Controlled Fusion 59, 053001 (2017).
[28] M. Podestà, R. Bell, A. Bortolon, N. Crocker,
D. Darrow, A. Diallo, E. Fredrickson, G.-Y. Fu,
N. Gorelenkov, W. Heidbrink, G. Kramer, S. Kub-
ota, B. LeBlanc, S. Medley,
and H. Yuh, Nucl.
Fusion 52, 094001 (2012).
[29] E. D. Fredrickson, N. A. Crocker, R. E. Bell,
D. S. Darrow, N. N. Gorelenkov, G. J. Kramer,
S. Kubota, F. M. Levinton, D. Liu, S. S. Med-
ley, M. Podestà, K. Tritz, R. B. White,
and
H. Yuh, Physics of Plasmas 16, 122505 (2009),
https://doi.org/10.1063/1.3265965.
[30] E. Fredrickson, N. Gorelenkov, M. Podesta, A. Bor-
tolon,
S. Gerhardt,
R. Bell,
A. Diallo,
and
B. LeBlanc, Nuclear Fusion 54, 093007 (2014).
[31] F. Zonca, S. Briguglio, L. Chen, G. Fogaccia, and
G. Vlad, Nuclear Fusion 45, 477 (2005).
[32] W. Zhang, Z. Lin, and L. Chen, Phys. Rev. Lett.
101 (2008), 10.1103/physrevlett.101.095001.
[33] T. Hauﬀ,
M. J. Pueschel,
T. Dannert,
and
F. Jenko, Phys. Rev. Lett. 102, 075004 (2009).
[34] M. Pueschel, F. Jenko, M. Schneller, T. Hauﬀ,
S. Guenter,
and G. Tardini, Nuclear Fusion 52,
103018 (2012).
[35] W. W. Heidbrink, J. M. Park, M. Murakami,
C. C. Petty, C. Holcomb,
and M. A. V. Zee-
land, Phys. Rev. Lett. 103 (2009), 10.1103/phys-
revlett.103.175001.
[36] W. X. Wang,
Z. Lin,
W. M. Tang,
W. W.
Lee,
S.
Ethier,
J.
L.
V.
Lewandowski,
G.
Rewoldt,
T.
S.
Hahm,
and
J.
Man-
ickam, Physics of Plasmas 13, 092505 (2006),
http://dx.doi.org/10.1063/1.2338775.
[37] W. X. Wang,
P. H. Diamond,
T. S. Hahm,
S.
Ethier,
G.
Rewoldt,
and
W.
M.
Tang,
Physics
of
Plasmas
17,
072511
(2010),
http://dx.doi.org/10.1063/1.3459096.
[38] R. J. Hawryluk, in Physics of Plasmas Close
to Thermonuclear Conditions, Vol. 1, edited by
B. Coppi, G. G. Leotta, D. Pﬁrsch, R. Pozzoli, and
E. Sindoni (CEC, Brussels, 1980) pp. 19–46.
[39] Y. Kishimoto, J.-Y. Kim, W. Horton, T. Tajima,
M. J. LeBrun, and H. Shirai, Plasma Physics and
Controlled Fusion 41, A663 (1999).
[40] C. Cheng, L. Chen,
and M. Chance, Annals of
Physics 161, 21 (1985).
[41] N. N. Gorelenkov, C. Z. Cheng,
and G. Y. Fu,
Phys. Plasmas 6, 2802 (1999).
[42] J. Lang and G.-Y. Fu, Phys. Plasmas 18, 055902
(2011).
[43] H. L. Berk, B. N. Breizman,
and M. Pekker,
Plasma Phys. Rep. 23, 778 (1997).
[44] H. L. Berk, B. N. Breizman, J. Candy, M. Pekker,
and N. V. Petviashvili, Phys. Plasmas 6, 3102
(1999).
[45] C. Cheng, Phys. Rep. 211, 1 (1992).
[46] N. N. Gorelenkov, Y. Chen, R. B. White, and H. L.
Berk, Phys. Plasmas 6, 629 (1999).
[47] R.
Hemsworth,
H.
Decamps,
J.
Graceﬀa,
B. Schunke, M. Tanaka, M. Dremel, A. Tanga,
H. D. Esch, F. Geli, J. Milnes, T. Inoue, D. Mar-
cuzzi, P. Sonato, and P. Zaccaria, Nuclear Fusion
49, 045006 (2009).
[48] M. J. Singh, D. Boilson, A. R. Polevoi, T. Oikawa,


## Page 13


13
and R. Mitteau, New Journal of Physics 19, 055004
(2017).
[49] S.
Sharapov,
B.
Alper,
H.
Berk,
D.
Borba,
B. Breizman, C. Challis, I. Classen, E. Edlund,
J. Eriksson, A. Fasoli, E. Fredrickson, G. Fu,
M.
Garcia-Munoz,
T.
Gassner,
K.
Ghantous,
V. Goloborodko, N. Gorelenkov, M. Gryaznevich,
S. Hacquin, W. Heidbrink, C. Hellesen, V. Kip-
tily, G. Kramer, P. Lauber, M. Lilley, M. Lisak,
F. Nabais, R. Nazikian, R. Nyqvist, M. Osakabe,
C. P. von Thun, S. Pinches, M. Podesta, M. Porko-
lab, K. Shinohara, K. Schoepf, Y. Todo, K. Toi,
M. V. Zeeland, I. Voitsekhovich, R. White, V. Ya-
vorskij,
and ITPA EP TG and JET-EFDA Con-
tributors, Nuclear Fusion 53, 104022 (2013).
[50] P. Lauber, Plasma Physics and Controlled Fusion
57, 054011 (2015).
[51] S. D. Pinches, I. T. Chapman, P. W. Lauber,
H. J. C. Oliver, S. E. Sharapov, K. Shinohara,
and K. Tani, Physics of Plasmas 22, 021807 (2015),
https://doi.org/10.1063/1.4908551.
[52] P. Rodrigues, A. Figueiredo, J. Ferreira, R. Coelho,
F. Nabais, D. Borba, N. Loureiro, H. Oliver, and
S. Sharapov, Nuclear Fusion 55, 083003 (2015).
[53] M. Schneller, P. Lauber, and S. Briguglio, Plasma
Physics and Controlled Fusion 58, 014019 (2016).
[54] M. Fitzgerald, S. Sharapov, P. Rodrigues,
and
D. Borba, Nuclear Fusion 56, 112010 (2016).
[55] A. Figueiredo, P. Rodrigues, D. Borba, R. Coelho,
L. Fazendeiro, J. Ferreira, N. Loureiro, F. Nabais,
S. Pinches, A. Polevoi, and S. Sharapov, Nuclear
Fusion 56, 076007 (2016).
[56] P. Rodrigues, A. Figueiredo, D. Borba, R. Coelho,
L. Fazendeiro, J. Ferreira, N. Loureiro, F. Nabais,
S. Pinches, A. Polevoi, and S. Sharapov, Nuclear
Fusion 56, 112006 (2016).
[57] N. N. Gorelenkov, H. L. Berk, R. V. Budny, C. E.
Kessel, G. J. Kramer, D. McCune, J. Manickam,
R. Nazikian,
and A. Polevoi, The linear stability
properties of medium- to high-n TAEs in ITER,
Tech. Rep. (Princeton Plasma Physics Labora-
tory, DOE OFES Theory Joule Milestone FY2007,
Preprint 4287, 2008).
[58] N. Gorelenkov, H. Berk,
and R. Budny, Nuclear
Fusion 45, 226 (2005).
[59] M. V. Zeeland, N. Gorelenkov, W. Heidbrink,
G. Kramer, D. Spong, M. Austin, R. Fisher, M. G.
Muñoz, M. Gorelenkova, N. Luhmann, M. Mu-
rakami, R. Nazikian, D. Pace, J. Park, B. Tobias,
and R. White, Nuclear Fusion 52, 094023 (2012).
[60] G. Vlad, S. Briguglio, G. Fogaccia, F. Zonca, and
M. Schneider, Nuclear Fusion 46, 1 (2006).
[61] M. Y. Isaev, S. Y. Medvedev, and W. A. Cooper,
Plasma Physics Reports 43, 109 (2017).
[62] Y. Todo and A. Bierwage, Plasma and Fusion Re-
search 9, 3403068 (2014).
[63] H.
Berk,
B.
Breizman,
J.
Fitzpatrick,
and
H. Wong, Nucl. Fusion 35, 1661 (1995).
[64] N. N. Gorelenkov, V. N. Duarte, M. Podesta, and
H. L. Berk, Nuclear Fusion (submitted) (2018).
[65] G. Meng, N. N. Gorelenkov, V. N. Duarte, H. L.
Berk, R. B. White, and X. Wang, Nuclear Fusion
(2018), 10.1088/1741-4326/aaa918.
[66] R. Budny, Nuclear Fusion 49, 085008 (2009).
[67] A. C. C. Sips, for the Steady State Operation, and
the Transport Physics topical groups of the Inter-
national Tokamak Physics Activity, Plasma Physics
and Controlled Fusion 47, A19 (2005).
[68] M. Albergante, J. P. Graves, A. Fasoli, F. Jenko,
and T. Dannert, Physics of Plasmas 16, 112301
(2009).
[69] M. Albergante, J. Graves, A. Fasoli, and X. Lapil-
lonne, Nuclear Fusion 50, 084013 (2010).
[70] M. Albergante, J. P. Graves, A. Fasoli, M. Jucker,
X. Lapillonne, and W. A. Cooper, Plasma Physics
and Controlled Fusion 53, 054002 (2011).
[71] F. Jenko, W. Dorland, M. Kotschenreuther,
and
B. N. Rogers, Physics of Plasmas 7, 1904 (2000),
https://doi.org/10.1063/1.874014.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
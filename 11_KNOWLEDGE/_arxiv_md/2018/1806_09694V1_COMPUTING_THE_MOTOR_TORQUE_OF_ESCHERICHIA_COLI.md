---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1806.09694v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1806.09694v1_Computing_the_motor_torque_of_Escherichia_coli

> Source: 1806.09694v1_Computing_the_motor_torque_of_Escherichia_coli.pdf

> Pages: 14

---


## Page 1


Computing the motor torque of Escherichia coli
Debasish Das and Eric Lauga∗
Department of Applied Mathematics and Theoretical Physics, Centre for Mathematical Sciences,
University of Cambridge, Wilberforce Road, Cambridge CB3 0WA, UK.
(Dated: June 16, 2018)
The rotary motor of bacteria is a natural nano-technological marvel that enables cell locomotion by
powering the rotation of semi-rigid helical ﬂagellar ﬁlaments in ﬂuid environments. It is well known
that the motor operates essentially at constant torque in counter-clockwise direction but past work
have reported a large range of values of this torque. Focusing on Escherichia coli cells that are
swimming and cells that are stuck on a glass surface for which all geometrical and environmental
parameters are known (N. C. Darnton et al., J. Bacteriology, 2007, 189, 1756–1764), we use two
validated numerical methods to compute the value of the motor torque consistent with experiments.
Speciﬁcally, we use (and compare) a numerical method based on the boundary integral representation
of Stokes ﬂow and also develop a hybrid method combining boundary element and slender body
theory to model the cell body and ﬂagellar ﬁlament, respectively. Using measured rotation speed
of the motor, our computations predict a value of the motor torque in the range 440 pN nm to 829
pN nm, depending critically on the distance between the ﬂagellar ﬁlaments and the nearby surface.
1.
INTRODUCTION
The study of bacteria is not only important in order to
understand many pathogenic diseases, it also serves as a
model system for microorganisms locomotion [1–3] and
their response to environmental cues [4, 5]. Bacteria are
present in great abundance on Earth in all kinds of envi-
ronments ranging from living creatures such as plants and
animals to non-living bodies like soil[6], rock[7], oceans[8]
and sea ice [9].
Bacteria have devised diﬀerent techniques to perform
locomotion contingent on their surrounding.
As many
as six diﬀerent types of translocation have been reported
in literature [10, 11], namely (i) swarming, requiring ex-
cessive development of ﬂagella; (ii) swimming, depend-
ing crucially on interactions between ﬂagella and ﬂuid;
(iii) gliding, dependent on an intrinsic motive force; (iv)
twitching, using an intrinsic motive force on type IV pili
(slender appendages that attach to substrates and pull
on the cell body); (v) sliding, requiring growth and re-
duced friction; and (vi) darting, dependent on growth of
capsulated aggregates.
In this article, we consider the swimming mode of bac-
teria locomotion and focus on the model organism Es-
cherichia coli (E. coli). A lot is known about this bac-
terium from the point of view of genetics and biochem-
istry, which enables researchers to induce behavioural
changes and elucidate its motility mechanisms [1].
The locomotion of E. coli is powered by rotary motors
rotating helical ﬂagellar ﬁlaments, see Fig. 1. Each motor
is embedded in a 3-layered cell wall. Structures outside
the cell wall include a rigid helical ﬂagellum attached to
the motor via a short elastic hook, while those inside
include a basal body and a short rod. The rod acts as a
drive shaft and rotates the elastic hook which plays the
role of a universal joint, so that it can rotate the semi-
∗E-mail: e.lauga@damtp.cam.ac.uk
rigid ﬂagellar ﬁlament even in situations when the rod
and ﬁlament are not aligned coaxially. [1, 12].
Directional reversibility of the rotary motor is the main
mechanism behind the “run and tumble” motion of bac-
teria searching for favourable environments[13]. On an
average, an E. coli cell has four such motors located
randomly on its surface[14].
During a run event, left-
handed ﬂagella arising from these motors form a heli-
cal bundle behind the cell and rotate counter-clockwise
(CCW), when viewed from behind the cell, thereby push-
ing it forward. To initiate a tumble event, at least one
of the motors starts to rotate clockwise (CW), the ﬂagel-
lum attached to this motor comes out of the bundle and
transforms from a left-handed to a right-handed helical
shape, still pushing the cell forward. This enables the cell
rigid
ﬁlament
hook 
ﬁlament 
junction
elastic
hook
MS-ring
C-ring
outer
membrane
cell wall
inner
membrane
MotB
MotA
Stator
Rotor
FIG. 1. Schematic diagram of the bacterial ﬂagellar motor
(adapted from Berg [12]). The primary components include
a rigid ﬁlament attached to an elastic hook rotated by torque
generating protein units MotA and MotB that act as stator
while the MS-ring and C-ring form the rotor.
arXiv:1806.09694v1  [physics.bio-ph]  25 Jun 2018


## Page 2


2
to change its course of motion. After a short period, the
reversed motor switches back to CCW rotation and the
ﬂagellum returns to its normal left-handed conﬁguration,
rejoining the bundle[14].
Torque in the motor is generated by interactions be-
tween the rotor (MS-ring and C-ring) and the stator
(MotA and MotB proteins) units, the latter functioning
as proton channels, see illustration in Fig. 1.
Experi-
ments have reported at least 11 torque generating units,
each consisting of a stator [15].
Proton ﬂux through
the proton channels due to an electrochemical gradient
causes the rotor to rotate. The work done per unit charge
that a proton does in crossing the cell membrane is called
the protonmotive force (pmf). Though the motor’s speed
is known to be proportional to pmf, the exact mechanism
of torque generation is still an active area of research
[1, 16]. Central to the work in our paper is the exact
value of the torque generated by the motor. A variety
of experimental methods have been used to measure the
torque-speed relationship for a number of bacteria species
[17]. For E. coli, the torque is approximately constant up
to a speed of a few 100 Hz, before rapidly decreasing to
zero at a critical zero-torque speed.
A wide range of values have been reported in the lit-
erature for the constant torque at frequencies below the
constant speed. Early work indirectly measured the mo-
tor torque using (i) electrorotation [18] where the cells
are made to rotate using electric ﬁelds; (ii) tethered cell
experiments [19] where the ﬂagella is tethered to a glass
surface and the cell body rotates about a ﬁxed point; and
(iii) tethered bead experiments [15] where the ﬂagellar ﬁl-
ament is sheared oﬀand a spherical bead is attached to
the remaining ﬂagellar stub. The relatively slower rota-
tion speeds and simpler spherical geometry make it easier
to track the rotation speed of these beads, allowing to ob-
tain an estimation of the value of the motor torque. More
recent experiments [20] used spherical magnetic beads to
replace the ﬁlament and an external applied magnetic
ﬁeld to stop them from rotating, allowing measurement
of the stall motor torque.
Alternatively, the value of the motor torque could be
inferred directly by combining modelling with a measure
of the rotation speed of ﬂagellar ﬁlaments of a swimming
E. coli. Swimming bacteria typically actuate indepen-
dently between four and seven ﬁlaments which are gath-
ered behind the cell in a thick helical bundle [14], a ge-
ometrical setup which presents modelling challenges due
to ﬁlament-ﬁlament interactions [21]. A clever alterna-
tive was reported by Darnton et al. [22] who, in addition
to focusing on swimming cells, considered bacteria stuck
on a glass surface which only rotate a single ﬂagellar ﬁl-
ament. This simpliﬁed situation makes it an ideal case
to analyse from a modelling and numerical simulation
viewpoint.
In this paper, we combine the boundary element
method and slender body theory in order to develop a
mathematical model of the ﬂagellated bacterium E. coli
and numerically simulate the experiments of Darnton et
al. [22]. We ﬁrst address the case where the cell is freely
swimming, despite some experimental unknowns, in or-
der to compare the experimental observables with those
obtained in the numerics. We then consider the situation
where the cell body is stuck on the wall, a conﬁguration
where all characteristics of the experiments are precisely
known. Boundary element methods have long been used
to study problems in bacteria locomotion including ﬂag-
ellar propulsion [23], interaction between two swimming
bacteria [24], bacterial behaviour and entrapment close
to surfaces [25, 26], and locomotion using multiple ﬂag-
ella [27]. Similarly, slender-body theory has been used to
address problems in bacterial swimming such as bacte-
rial polymorphism and optimal propulsion [28] and mi-
croscale pumping by bacteria near walls [29]. In addition
to our two numerical studies, we compare our results with
two recent attempts to simulate the experiments of Darn-
ton et al. [22] using mesoscale hydrodynamic simulations
[30] and bead-spring model [31].
Our paper is organised as follows. We describe the ge-
ometry and parameters of the problem in §2.1 and the
basics of rigid body boundary element method in §2.2.
We next introduce the two computational approaches
used in this study, based solely on boundary element
method in §2.3 and a hybrid method based on boundary
element and slender body theory in §2.4. We validate
the two models with existing semi-analytical results in
§2.5. The results of our numerical simulations are pre-
sented in §3, ﬁrst for free-swimming cells, and then for
cells stuck on surfaces, followed by a comparison with
previous work in §4 and discussion in §5. The results of
various tests performed to validate the numerical method
against tractable analytical solutions and details of mesh
generation are provided in appendices.
2.
MODEL: GEOMETRY AND
COMPUTATIONS
2.1.
Geometry and parameters
We use the geometrical dimensions of bacteria reported
in the experiments of Darnton et al. [22]. The cell body
is 2.5 µm long and 0.88 µm wide (see Fig. 2). The length
of the helical ﬂagellar ﬁlament measured along its centre-
line is ∼7 µm and the radius of the helix is 0.2 µm. The
viscosity of the aqueous medium where they reside ranges
from µ = 0.931 cP to 3.07 cP. In the case of free-moving
cells, the swimming speed of bacteria and rotational ve-
locity of the ﬂagellar ﬁlaments are measured to be 29
µm/s and 2π × 131 Hz respectively. Taking the density
of water to be 1000 kg/m3, the corresponding Reynolds
numbers for translation and rotation are ∼7 × 10−5 and
∼3 × 10−5, respectively, small enough that ﬂuid inertia
can be neglected. This allows us to describe ﬂuid mo-
tion around the bacteria using the incompressible Stokes
equation,
−∇p + µ∇2u = 0,
∇· u = 0,
(1)
where p and u are the pressure and velocity of the ﬂuid.


## Page 3


3
2.2.
Boundary element method (BEM)
We use boundary element method to solve the ﬂow
problem around rigid bodies with prescribed motion[32,
33]. Consider a rigid body experiencing a hydrodynamic
stress that resists its motion. The disturbance velocity
ﬁeld in a ﬂuid domain V , free of any additional localised
forcing, is represented by a surface distribution of ﬂow
singularities called stokeslets whose strength is the mod-
iﬁed boundary traction, fh, i.e. we have
u(x0) = u∞(x0)−
1
8πµ
ZZ
S
fh(x)·G(x, x0) dS(x). (2)
In Eq. (2), the integration points x are on S, the bound-
ary of the ﬂuid domain (i.e. the surface of the body) and
the evaluation point x0 is any point in V , the bulk ﬂuid,
and u∞is an arbitrary external ﬂow set to zero here.
The mathsfbi G(x, x0) is the free space Green’s func-
tion for Stokes equation, Eq. (1), also called the Oseen-
Burgers mathsfbi, representing ﬂuid ﬂow produced by a
point force,
G(x, x0) =
I
|x −x0| + (x −x0)(x −x0)
|x −x0|3
,
(3)
where I is the 3 × 3 identity mathsfbi.
The integral
equation relating the interfacial velocity and the surface
traction via distribution of stokeslet is referred to as sin-
gle layer potential (SLP) integral. When the evaluation
point lies on the surface, x0 ∈S, the no slip condition
prescribes the ﬂuid motion to be the same as the surface
of the rigid body. The surface velocity of a body translat-
ing with velocity U, measured at some arbitrary origin
inside the body, and rotating with velocity Ω, measured
about a point xm, is
u(x0) = U + Ω× (x0 −xm),
x0 ∈S.
(4)
The surface of the rigid body is discretised into 6-nodes
curved elements and each element is assumed to have
a constant velocity and force. Though 3-nodes ﬂat el-
ements are applicable for this problem as well, curved
elements are used for better accuracy. When the eval-
uation point lies on the surface, x0 ∈S, the kernel in
equation (2) can become singular and the singularity is
removed by transforming the variables from Cartesian to
polar coordinates[33]. For a prescribed velocity, u, the
unknown hydrodynamic surface tractions on the surface
fh can be computed by solving equation (2) numerically.
The net hydrodynamic force, F , and torque, T measured
about point xm, acting on the body are then computed
as
F =
ZZ
S
fh(x) dS(x),
T =
ZZ
S
(x −xm) × fh(x) dS(x),
x ∈S.
(5)
FIG. 2. Schematic diagram of a bacterium with a cell body
modelled as a prolate spheroid of length 2a, width 2b and
a rigid tapered helical ﬂagellum of pitch λ, radius R, axial
length Lλ, ﬁlament cross-sectional radius ρ, placed at a dis-
tance d parallel to a rigid wall and tilted at an angle θ with
respect to the bottom surface.
The linear system arising from the SLP formulation is
known for being ill-conditioned making it unsuitable for
iterative solvers like GMRES [34] used in this work. How-
ever, in practice this is only a problem for very ﬁne dis-
cretisation giving rise to large linear systems and the SLP
formulation has been used with success in many previous
studies involving swimming micro-organisms [23–27, 35].
The ﬂuid dynamics of a swimming bacterium involves
solving the ﬂow interaction between the cell body and the
ﬂagella. Since the ﬂagella are slender, we have the option
of discretising their entire surface and tackling it also us-
ing BEM, as carried out in §2.3, or taking advantage of
slender body theories [36] (SBT), thereby reducing the
surface integrals on the ﬁlaments to contour integrals, as
we do in §2.4.
2.3.
Computational model I: BEM-BEM
In this ﬁrst computational model (termed CM-I), both
the cell body and ﬂagellum surfaces, denoted as Sb and
Sf respectively, are discretised as illustrated in Fig. 3.
The details of the surface discretisation method are pro-
vided in appendix A. The cell body is modelled as a pro-
late spheroid with x-direction being the symmetry axis,
of equation
x2
a2 + y2 + z2
b2
= 1,
(6)
where a and b are the major and minor semi-axes length
respectively (a > b). The ﬂagellum is modelled as a rigid
left-handed helix with tapered ends [37, 38],
x = [s, E(s)R sin(ks + ψ), E(s)R cos(ks + ψ)],
s ∈[0, Lλ],
(7)
where the tapering function is E(s) = 1 −e−k2
Es2 and
where kE is a constant that determines how quickly the
helix grows to its maximum amplitude R and k is the
wavenumber. We use kE = k in this work. Notably, while
many previous studies have used a right-handed helix and
rotated the helix in a CW direction[23–27, 38], in reality
the bacterial ﬂagellum is a left-handed helix that rotates


## Page 4


4
FIG. 3. Computational model I: Posterior view of the bound-
ary element mesh of an E. coli bacterium with the cell body
and ﬂagellar ﬁlament modelled as a surface distribution of
stokeslets on a prolate spheroid and a rigid left-handed helix,
respectively.
CCW when viewed from behind (though one situation is
just the mirror-image symmetric of the other).
The axial length of the helix is Lλ while its contour
length is L = Lλ/ cos(φ), and the angle φ = arctan (Rk)
is the helix pitch angle. Changing the phase angle ψ sim-
ply rotates the helix around its axis in the x-direction.
The linear (or axial) wavelength and wave speed are
λ = 2π/k and V = ω/k respectively. The curvilinear
(or contour) wavelength Λ = λ/ cos φ and wave speed
c = V/ cos φ are not constant in the ‘end region’ but
vary negligibly outside of it. The cross-sectional radius
of the helix is ρ and the aspect ratio is deﬁned as ε = ρ/L.
The velocity on the surfaces of cell body and ﬂagellum
surfaces satisﬁes
u(x0) = −1
8πµ
ZZ
Sb
G(x, x0) · fh(x) dS(x)
−1
8πµ
ZZ
Sf
G(x, x0) · fh(x) dS(x),
x0 ∈Sb,f.
(8)
If the bacterium is swimming or held in place by an
optical trap in an inﬁnite ﬂuid medium, the free-space
Green’s function G given by equation (3) is used. How-
ever, if the bacterium is swimming close to a glass sur-
face or stuck on it, the Oseen-Burgers mathsfbi G is re-
placed with appropriate wall-modiﬁed Green’s function
Gw satisfying the no-slip velocity condition on the semi-
inﬁnite wall [39]. The expression for Gw is provided in
appendix B.
For a free-moving bacterium, the total hydrodynamic
force and torque acting on it should be zero, i.e.
Fb + Ff = 0,
Tb + Tf = 0.
(9)
The torques are calculated about the point where the
ﬂagellum is attached to the cell body.
The kinematic
conditions stipulate that the ﬂagellum remains attached
FIG. 4.
Computational model II: Side view of the bound-
ary element mesh of an E. coli bacterium with the cell body
modelled as a surface distribution of stokeslets on a prolate
spheroid and the ﬂagellar ﬁlament modelled as a line distribu-
tion of stokeslet on the centreline of a rigid left-handed helix.
to the body and thus
u(x0) = U + Ωb × x0,
x0 ∈Sb,
(10)
u(x0) = U + (Ωb + Ωm) × x0,
x0 ∈Sf,
(11)
where U and Ωb are the translational and angular veloc-
ities of the cell body while Ωm is the angular velocity of
the motor (equal to the relative rotational velocity of the
ﬂagellum with respect to the cell body). The lab frame
angular velocity of the ﬂagellum is Ωf = Ωb + Ωm. The
angular velocities and torque acting on the cell body and
ﬂagellum are measured at the point where the motor is
located, xm, which is taken to be the origin in our sim-
ulations.
The cell body and ﬂagellum are discretised into Nb and
Nf elements respectively. The total number of unknowns
to be solved for is 3Nb + 3Nf + 6, namely the 3Nb + 3Nf
components of surface tractions on the cell body and the
ﬂagellum and 6 components of the translational and ro-
tational velocity of the cell body. The relative rotational
velocity of the ﬂagellum Ωm serves as the forcing for the
system. Equations (8) provide us with 3Nb + 3Nf equa-
tions while equations (9) provide us additional 6 equa-
tions.
In the situation where the body of the bacterium is
stuck to the wall, we now have U = 0 and Ωb = 0.
Therefore, the kinematic conditions simplify to
u(x0) = 0,
x0 ∈Sb,
(12)
u(x0) = Ωm × x0,
x0 ∈Sf.
(13)
There is a net force and torque required to hold the bac-
teria stationary. The hydrodynamic traction acting on
the cell body and ﬂagellum is unknown. Hence, we need
to solve 3Nb +3Nf unknowns using 3Nb +3Nf equations
provided by the boundary integral equation (8).
2.4.
Computational Model II: BEM-SBT
In our second computational model (termed CM-II),
the cell surface is discretised in the same way as in §2.3
but the ﬂagellar hydrodynamics are described using slen-
der body theory [36], as illustrated in Fig. 4. Since the
bacterial ﬂagellar ﬁlament is a very slender helix of aspect
ratio ε ∼0.002, we can take advantage of past classical
work on the dynamics of slender ﬁlaments in viscous ﬂu-
ids. Using the formulation of Johnson [36], the velocity u
of the centreline Cf of a slender body is linearly related
to the hydrodynamic force per unit length, fh, acting on


## Page 5


5
it through the integral relationship,
u(x0) = −1
8πµΛ[fh](x0) −
1
8πµK[fh](x0),
x0 ∈Cf,
(14)
where 0 ≤s ≤L is the arclength along the centreline of
the ﬁlament. In Eq. (14), the local, Λ, and non-local, K,
operators are given by [36]
Λ[fh](x0) = [−c(I + ˆsˆs) + 2(I −ˆsˆs)] · fh(x0),
(15)
K[fh](x0) =
L
Z
0
(fh(x) · G(x, x0)
−I + ˆsˆs
|s −s′| · fh(x0)

ds′(x),
(16)
where c = log (ε2e).
Note that in this formulation,
the cross-sectional radius of the body varies slowly as
r(s) = 2ε
p
s(L −s) where ε = r(L/2)/L, ensuring
algebraically-accurate results. The cross-sectional radius
at the midpoint s = L/2 is taken to be equal to the ra-
dius of the ﬂagellum, i.e. r(L/2) = ρ . Equation (16)
becomes formally singular when s = s′ and this singular-
ity is removed by regularising the integral [40].
The hydrodynamics of the bacterium is then described
with a surface and a line distribution of stokeslet, repre-
senting the cell body and the ﬂagellum respectively,
u(x0) = −1
8πµ
ZZ
Sb
G(x, x0) · fh(x) dS(x)
−1
8πµ
Z
Cf
G(x, x0) · fh(x) ds(x),
x0 ∈Sb,
(17)
and
u(x0) = −1
8πµ
ZZ
Sb
G(x, x0) · fh(x) dS(x)
−1
8πµΛ[fh](x0) −
1
8πµK[fh](x0),
x0 ∈Cf.
(18)
For a free-swimming cell, the force and torque balance
equations are the same as in Eq. (9), except that the
force and torque on the ﬂagellum are now computed by
integrating fh along the centreline,
Ff =
Z
Cf
fh(x) ds(x),
Tf =
Z
Cf
x × fh(x) ds(x),
x ∈Cf.
(19)
0.0
0.02
0.04
0.06
0.08
0.1
0.12
U
V
0
1
2
3
4
5
6
Nλ
Hig. L = 5
Hig. L = 10
Hig. L = 20
CM-I L = 5
CM-I L = 10
CM-I L = 20
CM-II L = 5
CM-II L = 10
CM-II L = 20
FIG. 5. Validation of the computational models, CM-I and
CM-II, with the semi-analytical results of Higdon [38]. Aver-
age swimming speed plotted as a function of number of waves
with ρ/a = 0.02, αk = 1 and k/kE = 1 for three diﬀerent
ﬂagella lengths L = 5 (solid red lines), 10 (dotted blue line)
and 20 (dashed black line).
The velocity of the cell body is same as before,
i.e. Eq. (10), while the velocity of the ﬂagellum centreline
is now given by,
u(x0) = U + (Ωb + Ωm) × x0,
x0 ∈Cf.
(20)
The cell body surface and ﬂagellum centreline are discre-
tised into Nb and ˜Nf elements that requires us to solve
for 3Nb + 3 ˜Nf + 6 unknowns.
In the situation where the cell is stuck to the wall, we
now have U = 0 and Ωb = 0. The kinematic conditions
for the body is same as equation (12) and that for the
ﬂagellum simpliﬁes to,
u(x0) = Ωm × x0,
x0 ∈Cf.
(21)
We need to solve 3Nb + 3 ˜Nf unknowns tractions on the
cell body and ﬂagellum using 3Nb + 3 ˜Nf equations pro-
vided by the boundary integral equations (17) and (18).
2.5.
Validation of the computational models
We ﬁrst validate computational model I by perform-
ing simulations relevant for the hydrodynamics of (i) a
pair of spheres approaching each other, as detailed in
appendix C and (ii) a slender cylinder rotating in an in-
ﬁnite ﬂuid and translating next to a wall, as shown in
appendix D. In both case we compare our numerical re-
sults with exact solutions with excellent agreement.
We next validate both computational models using
past semi-analytical results for ﬂagellar swimming.
In
a landmark paper, Higdon [38] used slender body theory
to model a microorganism swimming by propagating he-
lical waves. Instead of discretising the surface of the cell
body, he used modiﬁed Green’s functions satisfying the
no-slip boundary condition on the cell body modelled as
a sphere. The swimming speed, U/V , normalised by the
linear wave speed, is plotted as a function of the num-
ber of waves, Nλ, for three diﬀerent ﬂagellar lengths with


## Page 6


6
Data Body Length Body Width Axial Length Motor Speed
set
(2a)
(2b)
(Lλ)
(Ωm)
A
2.5 µm
0.88 µm
8.3 µm
2π × 154s−1
B
2.0 µm
0.86 µm
10.0 µm
2π × 87s−1
C
2.5 µm
0.88 µm
6.2 µm
2π × 111s−1
TABLE I. Geometrical and kinematic characteristics of the
three data sets from Darnton et al. [22]. Data sets A and B
are measurements of swimming E. coli cells in two diﬀerent
ﬂuids using a bundle of ﬂagellar ﬁlaments, while C is that of a
stuck E. coli bacterium with a single rotating ﬂagellum. The
length and angular velocity scales for the problem are a and
Ωm, respectively
the parameters αk and k/kE kept ﬁxed in Fig. 5. Our
computational results are in excellent agreement with the
results of Higdon [38].
However, it is important to note a few diﬀerences be-
tween our two models. First, and unsurprisingly, solving
the integral equation on a line (CM-II) instead on a sur-
face (CM-I) results in faster computations. Second, the
surface mesh of a helical ﬂagellum used in computational
model I has a circular cross-section of constant radius
ρ, see appendix A, while the slender body theory used
in computational model II a circular cross-section of ra-
dius ρ at the centre that slowly tapers towards the ends.
Third, in situations where the ﬂagellum is very close to
another body, for example a semi-inﬁnite plane wall as
in §3.2, we expect near-ﬁeld hydrodynamic interactions
with the wall to play an important role. In these situa-
tions, slender body theory will fail to resolve the hydro-
dynamics, necessitating full surface discretisation. This
makes computational model I a more accurate but also a
costlier approach. For example, simulations of swimming
bacteria, presented in §3.1 using CM-I, were performed
with Nb = 80 and Nf = 4620 leading to a system size of
14106, requiring ∼74s to be solved. On the other hand,
simulations using CM-II were performed with Nb = 80
and ˜Nf = 300 leading to a system size of 1146, requiring
∼1s to be solved. These simulations were performed on
a computer with 3401 MHz CPU clock speed and 16GB
RAM.
3.
RESULTS
We use our computational models to address three sets
of data for E. coli from the experiments of Darnton et
al. [22]. Data sets A and B are concerned with E. coli
bacteria swimming using a bundle of helical ﬂagellar ﬁl-
aments in two diﬀerent ﬂuids and our numerical results
in this case are given in §3.1.
In contrast, the bacte-
ria in data set C are stuck on a glass surface with only
one rotating ﬂagellum, with our results provided in §3.2.
While the main goal of our paper is to use the experi-
ments on stuck bacteria to infer the value of the motor
torque, we also model the case of swimming cells to com-
pare our simulations with observable physical quantities
in the experiments, namely the cell swimming speed and
body rotation frequency.
In all cases, the helical ﬂagellar ﬁlaments have identi-
cal pitch, λ = 2.22 µm, helical radius, R = 0.2 µm and
cross-sectional radius, ρ = 0.012 µm. The other relevant
parameters including geometrical dimensions and motor
rotation speed vary from one data set to the next and are
listed in Table 3. The number of ﬁlaments in the bundle
for data sets A and B is unknown and we focus here on
the case of a single ﬁlament (see discussion below on the
role played by the ﬁlament radius). In order to model a
bacterium, one needs to transform the sphere in §2.5 into
a prolate spheroid of appropriate dimensions. The motor
rotation speed, Ωm, and the major semi-axes length, a,
are used as the angular velocity and length scale, respec-
tively (see Table 3). The major axes of the cell body and
the ﬂagella are aligned with each other along the x-axis.
We maintain a small gap between the cell body and the
helix ∼0.0125 µm, thereby avoiding a singularity in the
boundary integral equation (results are unaﬀected by al-
terations in this distance). Each calculation presented
below has been averaged over the phase angle ψ.
Numerically, all results in the following sections are
computed with Nb = 80, Nf = 4620 and ˜Nf = 300.
We have performed convergence tests and veriﬁed that
ﬁner grid resolution than these values produce negligible
changes in our results.
3.1.
Swimming bacteria
Using computational models I and II and ﬁrst assum-
ing that the cell is propelled by a single helical ﬁlament,
we prescribe the dimensionless motor rotation velocity
along the major axis of the cell body, Ωm = ˆi that acts
as the forcing on the system (see Table 3 for the dimen-
sional values). The observable physical quantities are the
swimming speed, U, and the angular velocity of the cell
body, Ωb, occuring in the negative x−direction since the
body counter-rotates compared to the ﬂagella. Data set
A takes place in the ﬂuid medium termed motility buﬀer
(MB+) for which the viscosity is 0.93 cP. The swimming
speed U computed using the two computational models
I and II, 20.6 µm/s is lower than that measured in exper-
iments, 29 µm/s. The angular velocity of the body Ωb
using models I and II are 27 Hz and 25 Hz respectively,
slightly higher than that measured in experiments, 23
Hz. The hydrodynamic torque experienced by the ﬂag-
ella, equal to the motor torque, were found to be 728 and
682 pN nm with models I and II, respectively.
Data set B takes place in the MB+ ﬂuid with added
methylcellulose (MC) for which the viscosity is 3.07
cP. The cell body length and motor rotation speed are
smaller while the ﬂagella is longer in this case when com-
pared to data set A. The swimming speed U computed
using the two computational models I and II, is found
to be 12.6 µm/s, signiﬁcantly lower than that measured
in experiments, 31 µm/s.
The angular velocity of the
body Ωb using models I and II are 21.3 Hz and 20.1 Hz
respectively and agree very well with that measured in


## Page 7


7
Data set A
Expt
CM-I
CM-II
Body rotation speed (Hz)
23
27
25
Filament rotation speed (Hz)
131
127
129
Cell speed (µm/s)
29
20.6
20.6
Motor torque (pN nm)
-
728
682
Data set B
Expt
CM-I
CM-II
Body rotation speed (Hz)
21
21.3
20.1
Filament rotation speed (Hz)
66
65.7
66.9
Cell speed (µm/s)
31
12.6
12.6
Motor torque (pN nm)
-
1504
1418
TABLE II. Comparison between measurements and computa-
tions for data sets A and B relevant for swimming bacterium
in ﬂuids MB+ and MB+ with MC, respectively, from Darnton
et al. (2007) [22]. Data set A has dimensionless body length
2a = 2, width 2b = 0.7, ﬁlament axial length Lλ = 8.3 and
viscosity = 0.93 cP. Data set B has dimensionless body length
2a = 2, width 2b = 0.86, ﬁlament axial length Lλ = 10.0 and
viscosity = 3.07 cP. The motor rotation speed is prescribed
in the simulations
experiments equal to 21 Hz. The hydrodynamic torque
experienced by the ﬂagella in this case were found to be
1504 and 1418 pN nm with models I and II, respectively.
These results are summarised in Table 3.1.
It is not speciﬁed in the experiments for data sets A
and B whether the bacteria are swimming close to a sur-
face. In order to investigate how the presence of a wall
may eﬀect the swimming kinematics, we vary the dis-
tance of the bacterium from the wall while keeping the
rotation rate of the motor ﬁxed as in the inﬁnite ﬂuid
medium case. The free-space Green’s function G used
in the models is replaced with Gw to account for the no-
slip condition on the wall. The variation of the swimming
speed, rotational speed and motor torque with the mini-
mum distance between the cell body and wall d −b (see
notation in Fig. 2), are shown in Fig. 6 for data set A (the
same trends are seen for data set B, the corresponding
plots of which are not presented here for brevity).
As expected, we ﬁnd that the swimming and rotational
speed of the cell body decrease monotonically while the
motor torque increases as the cell is moved closer to the
wall. As the distance between the bacterium and the wall
increases, the computed velocities and torque asymptot-
ically reach their inﬁnite ﬂuid medium values.
In the freely swimming cells experiments of Darnton et
al. [22], it is observed that some ﬂagella can wrap around
the cell body.
While the distance between a wrapped
ﬂagellum and the cell body is unknown, we may esti-
mate its eﬀect on the torque generation by assuming a
worst-case scenario where this distance is 0.1 nm. The
viscous torque arising from lubrication forces due to ro-
tation of the ﬂagellum near a cell body can be estimated
using Jeﬀrey’s analytical result for the torque per unit
length, Th, experienced by a cylinder of radius ρ rotating
with angular velocity Ωat a distance d from a plane wall,
namely Th = −4πµΩρ2d/
p
d2 −ρ2[41]. Assuming that
the length of the ﬂagellum rotating next to the cell body
is approximately half the cell body length, a, and substi-
tuting in this formula the relevant values from Tables 3
15
16
17
18
19
20
21
U (µm s−1)
0.0
0.1
0.2
0.3
0.4
0.5
0.6
d −b (µm)
Inﬁnite: CM-I
Inﬁnite: CM-II
Wall+Cell: CM-I
Wall+Cell: CM-II
14
16
18
20
22
24
26
28
Ωb
2π (Hz)
0.0
0.1
0.2
0.3
0.4
0.5
0.6
d −b (µm)
650
700
750
800
850
900
T (pN-nm)
0.0
0.1
0.2
0.3
0.4
0.5
0.6
d −b (µm)
FIG. 6. Top: Variation of the bacterium swimming speed,
U (µm/s), with the minimum distance between the cell body
and the wall, d −b (µm), for data set A. Circles (wall ef-
fect) and solid red line, 20.6 µm/s (inﬁnite medium) corre-
spond to model I while squares (wall eﬀect) and dotted blue
line, 20.6 µm/s (inﬁnite medium) correspond to model II. The
swimming speed in the experiments of Darnton et al. [22] was
found to be 29 µm/s (not shown). Middle: Dependence of the
rotational speed of the cell body, Ωb/2π (Hz), with the dis-
tance to the wall. Circles (wall eﬀect) and solid red line, 27 Hz
(inﬁnite medium) correspond to model I while squares (wall
eﬀect) and dotted blue line, 25 Hz (inﬁnite medium) corre-
spond to model II. Black dashed line corresponds to rotational
speed of 23 Hz measured in experiments of Darnton et al. [22].
Bottom: Variation of the motor torque, T (pN nm), with the
minimum distance between the cell body and the wall. Circles
(wall eﬀect) and solid red line, 728 pN nm (inﬁnite medium)
correspond to model I while squares (wall eﬀect) and dotted
blue line, 682 pN nm (inﬁnite medium) correspond to model
II.


## Page 8


8
Data set A
Expt
2ρ
3ρ
4ρ
Body rotation speed (Hz)
23
32.5
37.4
42.2
Filament rotation speed (Hz)
131
121.5
116.6
111.8
Cell speed (µm/s)
29
20.6
19.4
18.1
Total torque (pN nm)
-
877
1012
1144
Data set B
Expt
2ρ
3ρ
4ρ
Body rotation speed (Hz)
21
25.3
28.7
31.9
Filament rotation speed (Hz)
66
61.7
58.3
55.1
Cell speed (µm/s)
31
12.0
10.9
10.4
Total torque (pN nm)
-
1784
2026
2256
TABLE III. Comparison between measurements and compu-
tations using CM-I for data sets A and B relevant for swim-
ming bacterium in ﬂuids MB+ and MB+ with MC, respec-
tively, from Darnton et al. (2007) [22] with varying cross-
sectional radius of the eﬀective helical ﬁlament (from twice
the radius of a single ﬁlament to four times); all other param-
eters as in Table 3.1
and 3.1, we obtain additional torques for data set A and
B of 16 pN nm and 7 pN nm respectively. These values
do not add signiﬁcantly to the torque values obtained
from the simulations.
Quite remarkably, and except for the value of the
swimming speed in data set B, the agreement between
our simulations with a single ﬂagellar ﬁlament and the
experiments is excellent. Since the number of ﬁlaments in
the helical bundle is unknown in the experiments, we then
use an alternate method to account for the eﬀect of mul-
tiple ﬁlaments. In a controlled experimental study[42], it
was shown that the ﬂow ﬁeld generated by a bundle of
two ﬁlaments is well approximated by the ﬂow generated
by a single rigid helix with twice the ﬁlament radius. For
data sets A and B, we thus used computational model
I to carry out additional simulations varying the cross-
sectional radius of the helical ﬁlament, taking values of
either 2ρ, 3ρ or 4ρ, where ρ = 0.012 µm is the radius of
an isolated ﬁlament. The results of these simulations are
summarised in Table 3.1. We ﬁnd that, as the thickness
of the ﬁlament increases, the mismatch between our nu-
merical results and the experiments increases, indicating
that the hydrodynamics of a bundle is closer to that of
an isolated ﬁlament.
The discrepancy between the experimental and our
computational results with a single ﬁlament may be at-
tributed to the ﬁne details of the ﬁlament interactions.
Firstly, the eﬀect of hydrodynamic interactions between
the ﬁlaments is absent in the simulations.
Secondly,
steric interactions between ﬁlaments could also play a
signiﬁcant role [30].
However, it was noted previously
that including ﬁlament interactions does not lead to a
linear increase in swimming speeds or rotational speeds,
both seen in experiments [22] and numerical simulations
[30]. The viscosity for data set B is three times that of
data set A but it is believed that the motor torque is
independent of the medium viscosity. Hence, it is quite
surprising that the motor torque for data set B is almost
twice as high as that for data set A. It might be that
the ﬂuid medium surrounding the rotating ﬂagellum is
not perfectly Newtonian and the presence of polymers
could induce additional stresses in the ﬂow, despite the
fact that the 24 nm diameter ﬂagellar ﬁlament might be
comparable in size to both the radius of gyration of the
polymer molecules and to the distance between them.
3.2.
Bacteria stuck on a surface
The most important result of our study is the situation
where the bacterium is stuck on a (glass) surface with an
immobile cell body rotating a single ﬂagellar ﬁlament,
termed data set C in Table 3. All other geometric and
kinematic parameters are known in this case, apart from
the distance to the surface, making it an ideal situation to
model in order to predict the value of the torque exerted
by a single rotary motor. The forcing for this system is
Ωf = Ωm but unlike the swimming bacterium case there
are no direct observables in the experiments to compare
with as the cell body is not moving, i.e. U = 0 and
Ωb = 0. Note that the bacterium is not force and torque
free in this case.
We ﬁrst consider a ﬂagellum rotating in an inﬁnite ﬂuid
medium in the absence of the cell body.
Using com-
putational models I and II, we get motor torque values
equal to 474 pN nm and 438 pN nm, respectively which
are signiﬁcantly higher than that obtained by resistive
force theory calculations, 370 pN nm [22] (and repro-
duced in Table 4). We then place an immobile cell body
that simply acts as a hydrodynamic obstacle to the ro-
tating ﬂagellum and ﬁnd the torques increase negligibly
to 475 pN nm and 440 pN nm for models I and II re-
spectively. The increase in the force experienced by the
ﬂagella, ∼6% is also small but higher than the increase
in the torque, ∼0.2%. These results prove that an immo-
bile cell body does not produce signiﬁcant hydrodynamic
resistance to the rotating ﬂagellum.
We next consider the eﬀect of the wall on the torque ex-
perienced by a ﬂagellum with and without the cell body
while keeping the ﬂagellum parallel to the wall and the
rotation speed of the motor ﬁxed at the experimentally-
measured value of 2π ×111 Hz. As shown in Fig. 7 (top),
the value of the motor torque increases as we get closer
to the wall. We may also place a cell body next to the
rotating ﬂagellum, exactly reproducing the experimen-
tal conditions of a bacterium stuck on a glass surface.
The results of computational model I in Fig. 7 (top) are
plotted using triangles when there is no cell body and
circles if we add the cell body; similarly, for computa-
tional model II we use diamond (cell body absent) and
squares (cell body present). For both models, we see the
two sets of symbols overlap with each other, indicating
that the torque values is essentially unaﬀected by the
presence of the cell body, consistent with our results in
the inﬁnite ﬂuid medium case. The maximum values of
motor torque obtained for computational models I and
II are 829 pN nm and 739 pN nm when the ﬂagellum is
placed very close to the wall at a distance d = 0.22 µm,
slightly above the mathematically minimum gap between
the ﬂagellum and the wall of 0.02 µm.


## Page 9


9
400
450
500
550
600
650
700
750
800
850
T (pN-nm)
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1.0
d (µm)
Inﬁnite: CM-I
Inﬁnite: CM-II
Wall: CM-I
Wall: CM-II
Wall+Cell: CM-I
Wall+Cell: CM-II
d = R
d = b
400
450
500
550
600
650
T (pN-nm)
0
0.1π
0.2π
0.3π
0.4π
0.5π
θ
Inﬁnite: CM-I
Inﬁnite: CM-II
Tilted: CM-I
Tilted: CM-II
FIG. 7.
Top: Variation of motor torque T (pN nm) as a
function of the distance d (µm) of the ﬂagellum’s centreline
from the wall. Triangles and diamonds correspond to motor
torque values in the presence of wall but without a cell body,
circles and squares correspond to those in the presence of both
wall and cell body while the red and blue lines correspond to
torque values in an inﬁnite ﬂuid medium without wall or cell
body. The vertical black dashed line is d = R = 0.2 µm while
the vertical dash-dotted brown line is at d = b = 0.44 µm.
Bottom: Variation of motor torque, T (pN nm), as a function
of the tilt angle, θ, of the ﬂagellar axis relative to the wall.
The distance between the major axis of the cell body and the
wall is kept constant at d = 0.46 µm.
To give an indication of the magnitude of the torque for
a more realistic value of the distance to the wall, we may
pick the value d = 0.46 µm, so that the gap between the
cell body and the wall is 0.02 µm. In this case, the value of
the motor torque with and without the cell are 540 pN nm
and 539 pN nm for model I and 498 pN nm in both cases
for model II. Note that in either case we can not have
zero distance between the wall and the ﬂagellum or the
cell body as the integral equations become singular. The
full dependence of T on the value of d is shown in Fig. 7
(top).
Just as for freely swimming cells, it is likely that in
some cases a portion of the ﬂagellum is wrapped around
the cell body. We can carry out an analysis similar to
the one in §3.1 using the same assumptions to ﬁnd that
the lubrication torque due to a ﬂagellum rotating close
to a cell body is now on the order of 11 pN nm (a smaller
Geometrical parameter (µm) CM-I (pN nm) CM-II (pN nm)
a = 2.5 + 10%
540 + 0.0%
498 + 0.0%
a = 2.5 −10%
540 + 0.0%
498 + 0.0%
b = 0.88 + 10%
540 - 2.0%
498 - 2.0%
b = 0.88 −10%
540 + 2.6%
498 + 2.6%
ρ = 0.012 + 10%
540 + 3.1%
498 + 2.6%
ρ = 0.012 −10%
540 - 3.2%
498 - 2.7%
λ = 2.22 + 10%
540 + 0.8%
498 + 0.9%
λ = 2.22 −10%
540 - 1.1%
498 - 1.2%
R = 0.2 + 10%
540 + 18.5%
498 + 18.8%
R = 0.2 −10%
540 - 17.2%
498 - 17.5%
Lλ = 6.2 + 10%
540 + 10.5%
498 + 10.5%
Lλ = 6.2 −10%
540 - 10.5%
498 - 10.5%
TABLE IV. Variation in the value of the motor torque with
changes in the geometrical parameters of the stuck bacterium
with a rotating ﬂagellum next to a wall for both models. The
minimum distance between the cell body and the wall is kept
ﬁxed at 0.02 µm
value than above due to a smaller rotation frequency).
Here again, this contribution to the torque is small and
can be neglected.
3.2.1.
Tilted ﬂagellum
The exact orientations of the ﬂagellar ﬁlaments relative
to the surface have not been reported in the experiments
but they are likely to play an important role. Keeping the
cell body’s major axis ﬁxed at a distance of d = 0.46 µm
from the wall, we vary in our simulations the value of the
tilt angle, θ, between the axis of the ﬂagellar ﬁlament
and the direction of the surface. The results are shown
in Fig. 7 (bottom). Note that the minimum value of tilt
towards the wall is dictated by the minimum separation
distance of the ﬂagellum from the wall; speciﬁcally in
the simulations, we limit ourselves to θmin = −0.012π
corresponding to a minimum distance of 0.0165 µm of the
ﬂagellum from the wall. Unsurprisingly, we ﬁnd that the
axial torque required to rotate the ﬂagellum at a constant
angular velocity (111 Hz) systematically increases with
an increase of tilt angle towards the wall as parts of the
ﬂagellum move closer towards it. The maximum values
of the torque at the minimum tilt angle are equal to 611
pN nm and 556 pN nm for models I and II respectively,
almost 30% larger than the values when the ﬁlaments
are tilted away and far from the surface. These results
demonstrate the importance of the ﬂagellum orientation
on the motor torque values.
3.2.2.
Geometrical parameters uncertainties
In addition to intrinsic biological variability, there are
unavoidable uncertainties in the measurements of geo-
metrical parameters of the bacteria. In order to estimate
the impact of these uncertainties on our results, we look
at the variability of the motor torque, T, induced by a


## Page 10


10
Motor Torque Experiments
Reference
(pN nm)
vs. Numerics
vs. Theory
Berry and Berg (1997) [19]
∼4,500
exp
Fahrner et al. (2003) [43]
1,370 ± 50
exp
Chattopadhyay et al. (2006) [44] 500
exp
Reid et al. (2006) [15]
1,260 ± 190
exp
Darnton et al. (2007) [22]
370 ± 100
exp + th
Shimogonya et al. (2015) [45]
∼700
exp + num
Hu et al. (2015) [30]
∼1,200
num
Kong et al. (2015) [31]
∼1,600
num
Van Oene et al. (2017) [20]
874 ± 206
exp
Present work
440–829
num
TABLE V. List in chronological order of past experiments
(exp) and numerical simulations (num) or theory (th) inves-
tigating the value of the bacterial motor torque with range of
reported values
±10% variability in the geometrical parameters, namely
a, b, ρ, λ, R and Lλ. All the simulations are performed
with the minimum gap between the cell body and the
wall kept ﬁxed at 0.02 µm and the results are summarised
in Table 3.2. We ﬁnd that variations in the length and
width of the cell body and the cross-sectional radius and
pitch of the ﬂagellum have negligible eﬀect on the mo-
tor torque value. In contrast, the torque varies linearly
with the axial length of the ﬂagellum (consistent with the
asymptotic resistive force theory [2]) and varies the most
with changes in radius of the helical ﬁlament.
4.
MOTOR TORQUE: COMPARISON WITH
PAST EXPERIMENTS AND SIMULATIONS
Our simulations in the case of bacteria stuck on a sur-
face exactly reproduce the experiments of Darnton et
al. [22] and allow us therfore to provide a computational
prediction for the value of the motor torque. Our results,
shown in Fig. 7, were seen to range between 440 pN nm
(minimum value, in bulk ﬂuid) to 829 pN nm (maximum
value in the extreme case where the ﬂagellum all but
touches the surface). In order to compare with past ex-
periments and simulations, we summarise in Table 4 a
list of the previous studies that have attempted to ﬁnd
the value of the motor torque of E. coli.
4.1.
Comparison with past experiments
The early experimental investigation of bacterial motor
torque were done with electrorotation method [18], how-
ever, absolute values of torque were not reported. Since
it is diﬃcult to measure the high rotation rates of in-
dividual ﬂagella, Berry and Berg [19] tethered a single
ﬂagellum to a glass surface and measured the slowly ro-
tating cell body of E. coli cells. The rotation of the cell
body was stopped by using optical tweezers thereby pro-
viding an estimate of the motor torque ∼4,500 pN nm.
This high value appears to be an outlier in the literature.
The preferred method used in experiments since then
involves shearing most of the ﬂagellar ﬁlament and teth-
ering a small spherical bead to the remaining ﬂagellar
stub. The rotation rate of the sphere is then measured
and the viscous torque acting on it directly relates to
the motor torque.
Chen and Berg [46] pioneered this
tethered bead experimental method, however, they did
not give the absolute torque values but only relative
value of the torques at diﬀerent frequencies. While Chen
and Berg [46] used spherical beads of diameter 0.45 µm
and changed the load by changing the viscosity of the
medium, Fahrner et al. [43] used the same method but
used beads of diﬀerent sizes in order to change the load.
Unfortunately, neither the value of torque nor the vis-
cosity of the ﬂuid medium are mentioned in the article.
In the low-speed, high-torque limit with spheres whose
diameters ranged from 1.0–2.1 µm, they obtained rota-
tion rates ranging from 78 to 8.6 Hz. A mean torque of
∼1, 370 pN nm is however mentioned by the same group
in Darnton et al. [22]. Finally, using spherical beads of
diameter 1 µm for the tethered bead method, Reid et
al. [15] found the motor torque to be ∼1, 260 pN nm
corresponding to a motor speed of 63 ± 7 Hz.
A diﬀerent method was proposed Chattopadhyay et
al. [44] who used optical traps to prevent E. coli bacteria
from swimming. The optical trap force compares directly
with the thrust force that propels the bacteria and can
be used to ﬁnd the torque and swimming speed in an
indirect manner (though the dimensions of the ﬂagellum
are inferred and not directly measured in these experi-
ments). The rotation rate of the cell body and ﬂagellum
were measured to be 19.6 Hz and 115 Hz respectively and
the thrust force was found to be 0.57 pN. In the absence
of the trap, swimming speeds of 22 µm/s were measured
using direct video microscopy. Using these values, Chat-
topadhyay et al. [44] estimated the motor torque value to
be 500 pN nm. These values are close to that found in our
simulations of an immobile bacterium close to the glass
surface, 475 pN nm (CM-I) and 440 pN nm (CM-II). In
recent experiments, Drescher et al. [47] used ﬂow ﬁeld
measurements to estimate the force dipole generated for
a bacterium swimming at 22 ± 5 µm/s, and obtained a
dipole consistent with a thrust force of 0.42 pN, close to
the 0.57 pN found by Chattopadhyay et al.[44]. Our nu-
merical simulations (CM-I) for data sets A and B predict
a thrust value of 0.28 pN and 0.49 pN for cells swimming
at speeds 20.6 µm/s and 12.6 µm/s with their ﬂagellum
rotating at 127 Hz and 65.7 Hz respectively, in broad
agreement.
Shimogonya et al.[45] performed tethered bead exper-
iments using gold particles of diameter 0.25 µm. They
measured the precession of these particles and predicted
a motor torque of the order of 700 pN nm using boundary
element method.
Finally, the latest experiments using tethered beads
method on 1 µm diameter spheres performed by Van
Oene et al. [20] suggest the motor torque to be 874 ±
206 pN nm corresponding to a motor speed of 30.5 ± 6.9
Hz. These experimental measurements match our sim-


## Page 11


11
ulations in the case of a ﬂagellar ﬁlament rotating very
close to a wall. In the same experimenters, Van Oene
et al. [20] were able to stop the rotation of the spherical
magnetic beads by applying an external magnetic torque
and found the stall motor torque be 444 ± 366 pN nm,
surprisingly much smaller than the prediction for the mo-
tor torque in the case of rotating tethered beads.
4.2.
Comparison with past simulations and theory
Using an analytical model based on resistive force the-
ory, Darnton et al. [22] estimated the motor torque of
E. coli to be 370 ± 100 pN nm, the lowest value among
all studies.
Mesoscale hydrodynamic simulations [30] have been
performed for a bacterium with cell body length 2a =
2.5 µm, width 2b =0.9 µm, and a single ﬂagellar ﬁla-
ment with pitch λ = 2.2 µm, pitch angle ψ = 30◦, cross-
sectional radius ρ = 0.012 µm and 3 turns corresponding
to an axial length of λ = 6.6 µm (instead of 8.3 µm or
10 µm in the experiments). These simulations predict a
swimming speed of 14.5 µm/s and ﬂagellum rotation fre-
quency of 131 Hz resulting from applying a motor torque
equal to ∼1, 200 pN nm. We note that the authors did
not perform simulations of a stationary bacterium. How-
ever, by invoking linearity of Stokes ﬂows, we can infer
that the ﬂagellum rotation frequency would be 111 Hz
if a motor torque value of ∼1, 000 pN nm was applied,
allowing comparison with the data of Darnton et al. [22].
Simulations based on bead spring model [31] with three
ﬂagella also attempted to reproduce the experiments
of Darnton et al. [22] with ﬂagellum dimensions which
are not exactly the same but are close to the experi-
ments. Speciﬁcally, the relevant dimensions used in these
simulations are: cell body length 2a = 2.5 µm, width
2b =0.88 µm, pitch λ = 2.5 µm (instead of 2.22 µm in
the experiments), helical radius R = 0.5 µm (instead of
0.4 µm in the experiments), cross-sectional radius ρ =
0.012 µm and axial length λ = 8.3 µm. The motor torque
applied in these simulations is also 1,200 pN nm. The
cell, bundle rotation rate and swimming speed were found
to be 26 Hz, 62 Hz and 24 µm/s, respectively. On scal-
ing the bundle rotation rate to the experimental value of
Darnton et al. [22], 111 Hz, we obtain the motor torque
value to be ∼2, 150 pN nm.
5.
DISCUSSION
In this paper, we have used two computational ap-
proaches based on the well established boundary integral
equations and slender body theory valid for Stokes ﬂow
in order to compute the value of torque generated by
the rotary motor of an E. coli. We performed a number
of tests to comprehensively validate the numerical sim-
ulations with analytical results presented in the appen-
dices. The models are also validated with existing semi-
analytical solutions of Higdon [38] relevant for micro-
organisms swimming due to helical waves. We note that
the model for the rotary motor used in the article is, in
eﬀect, a lumped model that represents the whole motor
by a single rotation and associated torque. The hydro-
dynamics of the hook is ignored owing to its small size
compared to the ﬂagellar ﬁlament. Since, in steady state,
the elastic hook simply rotates with the rigid ﬂagellum
it does not change the amount of torque transmitted to
the ﬂagellum. Equipped with our model, we ﬁrst sim-
ulated the dynamics of E. coli in the case where it is
swimming due to a single rotating ﬂagellar ﬁlament. In
the former case, the agreement between our simulations
the experiments of Darnton et al. [22] is quite remarkable
even though the swimming cells in the experiments are
propelled by multiple interacting ﬂagellar ﬁlaments.
We next considered the situation where the cell has
a stationary cell body, an idealised situation to make a
prediction for the value of the motor torque given that
all parameters from the experiment of Darnton et al. [22]
have been measured. Values reported in the literature for
the motor torque span a wide range, mostly 500–1,200
pN nm, and our computations are on the smaller end of
that spectrum. It is not clear at all what causes these
numbers to diﬀer so much from each other, even though
many of the experiments employ the same techniques.
As we have demonstrated here, the distance between a
rotating ﬂagellar ﬁlament and a nearby surface is crucial
to obtaining the correct values, as hydrodynamic friction
depends critically on it, and suggests that perhaps hy-
drodynamic interactions with surface might have played
an important role in some of the experimental investiga-
tions.
Appendix A: Discretisation method
In order to create a spherical mesh, we use the sub-
routine BEMLIB [33] starting from an icosahedron and
successively subdividing the triangles. The transforma-
tion of the sphere to a prolate spheroid is done by simply
rescaling the coordinates, y = (b/a)y and z = (b/a)z.
To create a helical surface, we ﬁrst specify the number
of points Ncl along the centreline of the helix. Around
each point, we then create a circle of radius ρ having 12
points. These points either form a vertex or mid-points
of the 6-nodes triangles. Each consecutive circle is shifted
by π/24 so that we have approximately uniform isosceles
triangles rather than right-angled triangles. A section of
a discretised helix is shown in Fig. 8. We attach 2 hemi-
spheres of radius ρ on both ends of the discretised helix
to remove sharp corners.
Appendix B: Green’s function for a stokeslet near a
wall
Let us consider a stokeslet placed above a wall at z = 0
at a distance h such that its location is (y1, y2, h). The
image singularities are then accordingly located below


## Page 12


12
FIG. 8. Surface discretisation of a rigid helical object using
6-nodes curved elements. Evenly spaced circles are created
along the centreline of the helix that are discretised into 12
points that either form a vertex or midpoints of the individual
elements.
the wall at (y1, y2, −h). The Green’s function [39] due to
the stokeslet at an evaluation point (x1, x2, x3) is,
Gw
ij =δij + ˆriˆrj
r
−δij + ˆRi ˆRj
R
+ 2h∆jk
∂
∂Rk
 
h ˆRi
R2 −δi3 + ˆRi ˆR3
R
!
,
(B1)
where the vector pointing from the stokeslet location to
the evaluation point is ri = (x1 −y1, x2 −y2, x3 −h), the
vector pointing from the image location to the evaluation
point is Ri = (x1 −y1, x2 −y2, x3 + h). The matrix ∆jk
takes the value of 1 when j = k = 1, 2, -1 when j = k = 3
and 0 for every other combination.
Appendix C: Interaction between two spheres
In order to validate our numerical algorithm for two
solid interacting bodies in Stokes ﬂow, we analyse the hy-
drodynamic force acting on 2 spheres approaching each
other, separated by a distance d. Fig. 9 shows two dis-
cretised spheres, each made with 5120 elements.
The
line joining their centres is along the x axis. We essen-
tially solve equations (8) to ﬁnd the tractions on the 2
spheres moving with a prescribed velocity of U = ±0.5ˆi,
so that the relative speed of approach is 1.
We com-
pare the force computed by our numerical method for 3
diﬀerent discretisation levels, Nb = 320, 1280 and 5120
with that obtained using lubrication theory [48] valid
for small distances, far-ﬁeld asymptotic solution valid for
large distances and exact solutions based on bispherical
coordinates, see Fig. 10. Our numerical method based on
FIG. 9. Boundary element mesh (Nb = 5120) of two spheres
separated by a distance d approaching each other with veloc-
ities, U, along the line connecting the centres.
10−2
10−1
1
10
F/6πµ
10−2
10−1
1
10
d
Lubrication
Far-ﬁeld
Bi-spherical
BEM Nb = 320
BEM Nb = 1280
BEM Nb = 5120
FIG. 10.
Comparison of hydrodynamic force acting on 2
spheres approaching each other at a relative velocity of 1 along
the line joining their centres obtained by boundary element
method and theoretical calculations.
boundary element method ﬁnds excellent agreement with
the theoretical predictions. Note that as the distance be-
tween the spheres d decreases, ﬁner discretisation of the
spheres near the closest point becomes necessary to re-
solve the ﬂow ﬁeld accurately. In order to validate the
force-free and torque-free bacterium model, we can think
of sphere 2 as a rotating ﬂagella and implement computa-
tional model I. On imposing a relative velocity of Ωm = ˆi,
we found the body rotation rate to be Ωb = −0.5ˆi, as ex-
pected theoretically. The swimming velocity U is found
to be exactly zero as neither of the bodies are chiral. This
serves as another validation for computational model I.
Appendix D: Rotating and translating slender
cylinder
As there are no exact solutions to problems of helices
in viscous ﬂows, we test our numerical method for slender
cylinders rotating in an inﬁnite ﬂuid medium and trans-
lating next to a plane wall. The length of the cylinder
is L = 7 while the cross-sectional radius is ρ = 0.01, so
that the aspect ratio is ε = 0.0014, comparable to that of
a bacterial ﬂagella. An inﬁnitely long cylinder rotating
in a viscous ﬂuid experiences a viscous torque per unit
length [48] Th = −4πµρ2Ωwith the angular velocity Ω
pointing along the axis of the cylinder. Using boundary
element method, we obtain the hydrodynamic torque per
unit length acting on the discretised rotating cylinder.
Fig. 11 shows the relative error between the numerical
simulations and analytical results for 4 diﬀerent levels of
discretisation, Nf = 1020, 2028, 4044 and 8076.
In order to validate our results that include wall ef-
fects, we consider a slender cylinder translating perpen-
dicular to its long axis close to a wall such that the cylin-
der centreline is at a distance d = 0.02 from the wall.
The dimensions of the cylinder are the same as consider


## Page 13


13
0.0
0.02
0.04
0.06
0.08
0.1
0.12
0.14
0.16
relative error
1020 2028
4044
8076
Nf
Rotation
Translation
FIG. 11. Relative error in the hydrodynamic torque and force
per unit length acting on a slender cylinder rotating in an
inﬁnite ﬂuid medium and translating perpendicular to its axis
next to a plane wall, respectively, computed using boundary
element methods for 4 levels of discretisation Nf = 1020,
2028, 4044 and 8076.
before. The translating cylinder experiences a hydrody-
namic force per unit length [41] Fh = −4πµU/α, where
α = log [(d/ρ) +
p
(d/ρ)2 −1]. Fig. 11 shows the relative
error between the numerical simulations and analytical
results for 4 diﬀerent levels of discretisation, Nf = 1020,
2028, 4044 and 8076. In both these tests, we ﬁnd ex-
cellent agreement between numerics and theory and the
accuracy increases as we increase the grid resolution.
ACKNOWLEDGEMENTS
We thank Howard Berg, Richard Berry, Maciej Lisicki,
John Lister and Thomas Powers for helpful discussions
and Sebastien Michelin for providing the MATLAB code
for the exact solution of the force acting on two spheres
presented in the appendix C. This project has received
funding from the European Research Council (ERC) un-
der the European Union’s Horizon 2020 research and in-
novation programme (grant agreement 682754 to EL).
[1] H. C. Berg. E. coli in Motion. Springer Science & Busi-
ness Media, 2008.
[2] E. Lauga and T. R. Powers. The hydrodynamics of swim-
ming microorganisms. Rep. Prog. Phys., 72(9):096601,
2009.
[3] E. Lauga. Bacterial hydrodynamics. Annu. Rev. Fluid
Mech., 48:105–130, 2016.
[4] H. C. Berg. Chemotaxis in bacteria. Annu. Rev. Biophys.
Bioeng., 4(1):119–136, 1975.
[5] K. M. Ottemann and J. F. Miller. Roles for motility in
bacterial–host interactions. Mol. Microbiol., 24(6):1109–
1117, 1997.
[6] J. Gans, M. Wolinsky, and J. Dunbar. Computational
improvements reveal great bacterial diversity and high
metal toxicity in soil.
Science, 309(5739):1387–1390,
2005.
[7] A. A. Gorbushina and W. J. Broughton. Microbiology
of the atmosphere-rock interface: how biological inter-
actions and physical stresses modulate a sophisticated
microbial ecosystem. Annu. Rev. Microbiol., 63:431–450,
2009.
[8] F. Azam, T. Fenchel, J. G. Field, J. S. Gray, L. A. Meyer-
Reil, and F. Thingstad.
The ecological role of water-
column microbes in the sea. Mar. Ecol. Prog. Ser., pages
257–263, 1983.
[9] J. T. Staley and J. J. Gosink. Poles apart: biodiversity
and biogeography of sea ice bacteria. Annu. Rev. Micro-
biol., 53(1):189–215, 1999.
[10] J. Henrichsen. Bacterial surface translocation: a survey
and a classiﬁcation. Bacteriol. Rev., 36(4):478, 1972.
[11] R. M. Harshey. Bacterial motility on a surface: many
ways to a common goal.
Annu. Rev. Microbiol.,
57(1):249–273, 2003.
[12] H. C. Berg. The rotary motor of bacterial ﬂagella. Annu.
Rev. Biochem., 72:19–54, 2003.
[13] H. C. Berg. Random walks in biology. Princeton Univer-
sity Press, 1993.
[14] L. Turner, W. S. Ryu, and H. C. Berg. Real-time imaging
of ﬂuorescent ﬂagellar ﬁlaments. J. Bacteriol., 182:2793–
2801, 2000.
[15] S. W. Reid, M. C. Leake, J. H. Chandler, C.-J. Lo,
J. P. Armitage, and R. M. Berry. The maximum num-
ber of torque-generating units in the ﬂagellar motor of
Escherichia coli is at least 11.
Proc. Natl. Acad. Sci.,
103(21):8066–8071, 2006.
[16] C. V. Gabel and H. C. Berg. The speed of the ﬂagel-
lar rotary motor of Escherichia coli varies linearly with
protonmotive force. Proc. Natl. Acad. Sci., 100(15):8748–
8751, 2003.
[17] Y. Sowa and R. M. Berry.
Bacterial ﬂagellar motor.
Quart. Rev. Biophys., 41(2):103–132, 2008.
[18] H. C. Berg and L. Turner. Torque generated by the ﬂag-
ellar motor of Escherichia coli. Biophys. J., 65(5):2201–
2216, 1993.
[19] R. M. Berry and H. C. Berg. Absence of a barrier to back-
wards rotation of the bacterial ﬂagellar motor demon-
strated with optical tweezers.
Proc. Natl. Acad. Sci.,
94(26):14433–14437, 1997.
[20] Maarten M Van Oene, Laura E Dickinson, Bronwen
Cross, Francesco Pedaci, J. Lipfert, and N. H. Dekker.
Applying torque to the Escherichia coli ﬂagellar motor
using magnetic tweezers. Sci. Rep., 7:43285, 2017.
[21] H. Flores, E. Lobaton, S. M´endez-Diez, S. Tlupova, and
R. Cortez. A study of bacterial ﬂagellar bundling. Bull.
Math. Biol., 67:137–168, 2005.
[22] N. C. Darnton, L. Turner, S. Rojevsky, and H. C. Berg.
On torque and tumbling in swimming Escherichia coli.
J. bacteriology, 189(5):1756–1764, 2007.
[23] N. Phan-Thien, T. Tran-Cong, and M. Ramia.
A
boundary-element analysis of ﬂagellar propulsion.
J.
Fluid Mech., 184:533–549, 1987.


## Page 14


14
[24] T. Ishikawa, G. Sekiya, Y. Imai, and T. Yamaguchi. Hy-
drodynamic interactions between two swimming bacte-
ria. Biophys. J., 93(6):2217–2225, 2007.
[25] H. Shum, E. A. Gaﬀney, and D. J. Smith.
Modelling
bacterial behaviour close to a no-slip plane boundary:
the inﬂuence of bacterial geometry. Proc. R. Soc. Lond.
A, 466(2118):1725–1748, 2010.
[26] D. Giacch´e, T. Ishikawa, and T.i Yamaguchi.
Hydro-
dynamic entrapment of bacteria swimming near a solid
surface. Phys. Rev. E, 82(5):056309, 2010.
[27] P. Kanehl and T. Ishikawa. Fluid mechanics of swim-
ming bacteria with multiple ﬂagella.
Phys. Rev. E,
89(4):042704, 2014.
[28] S. E. Spagnolie and E. Lauga.
Comparative hydrody-
namics of bacterial polymorphism.
Phys. Rev. Lett.,
106(5):058103, 2011.
[29] J. Dauparas, D. Das, and E. Lauga. Helical micropumps
near surfaces. Biomicroﬂuidics, 12(1):014108, 2018.
[30] J. Hu, M. Yang, G. Gompper, and R. G. Winkler. Mod-
elling the mechanics and hydrodynamics of swimming E.
coli. Soft matter, 11(40):7867–7876, 2015.
[31] M. Kong, Y. Wu, G. Li, and R. G. Larson. A bead-spring
model for running and tumbling of ﬂagellated swimmers:
detailed predictions compared to experimental data for
E. coli. Soft Matter, 11(8):1572–1581, 2015.
[32] C. Pozrikidis. Boundary Integral and Singularity Meth-
ods for Linearized Viscous Flow. Cambridge University
Press, 1992.
[33] C. Pozrikidis. A Practical Guide to Boundary Element
Methods with the Software Library BEMLIB. CRC Press,
2002.
[34] Y. Saad and M. H. Schultz. GMRES: A generalized min-
imal residual algorithm for solving nonsymmetric linear
systems. SIAM J. Sci. Stat. Comput., 7:856–869, 1986.
[35] D. J. Smith, E. A. Gaﬀney, J. R. Blake, and J. C.
Kirkman-Brown. Human sperm accumulation near sur-
faces: a simulation study. J. Fluid Mech., 621:289–320,
2009.
[36] R. E. Johnson.
An improved slender-body theory for
stokes ﬂow. J. Fluid Mech., 99(2):411–431, 1980.
[37] J. J. L Higdon.
A hydrodynamic analysis of ﬂagellar
propulsion. J. Fluid Mech., 90(4):685–711, 1979.
[38] J. J. L Higdon. The hydrodynamics of ﬂagellar propul-
sion: helical waves. J. Fluid Mech., 94(2):331–351, 1979.
[39] J. R. Blake and A. T. Chwang. Fundamental singularities
of viscous ﬂow. J. Eng. Math., 8:23–29, 1974.
[40] A.-K. Tornberg and M. J. Shelley. Simulating the dy-
namics and interactions of ﬂexible ﬁbers in stokes ﬂows.
J. Comp. Phys., 196(1):8–40, 2004.
[41] D. J. Jeﬀrey and Y. Onishi. The slow motion of a cylin-
der next to a plane wall. Quart. J. Mech. Appl. Math.,
34(2):129–137, 1981.
[42] M. J.n Kim, M. J. Kim, J. C. Bird, J. Park, T. R. Powers,
and K. S. Breuer. Particle image velocimetry experiments
on a macro-scale model for bacterial ﬂagellar bundling.
Exp. Fluids, 37(6):782–788, 2004.
[43] K. A. Fahrner, W. S. Ryu, and H. C. Berg.
Biome-
chanics: bacterial ﬂagellar switching under load. Nature,
423(6943):938–938, 2003.
[44] S. Chattopadhyay, R. Moldovan, C. Yeung, and X. L.
Wu. Swimming eﬃciency of bacterium Escherichia coli.
Proc. Natl. Acad. Sci., 103(37):13712–13717, 2006.
[45] Y. Shimogonya, Y. Sawano, H. Wakebe, Y. Inoue,
A. Ishijima, and T. Ishikawa. Torque-induced precession
of bacterial ﬂagella. Sci. Rep., 5:18488, 2015.
[46] X. Chen and H. C. Berg. Torque-speed relationship of
the ﬂagellar rotary motor of Escherichia coli. Biophys.
J., 78(2):1036–1041, 2000.
[47] K. Drescher, J. Dunkel, L. H. Cisneros, S. Ganguly, and
R. E. Goldstein. Fluid dynamics and noise in bacterial
cell–cell and cell–surface scattering.
Proc. Natl. Acad.
Sci., 108(27):10940–10945, 2011.
[48] S. Kim and S. J. Karrila. Microhydrodynamics: principles
and selected applications. Courier Corporation, 2013.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1806_09694v1_computing_the_motor_torque_of_escherichia_coli
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2018/1806_09694V1_COMPUTING_THE_MOTOR_TORQUE_OF_ESCHERICHIA_COLI.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

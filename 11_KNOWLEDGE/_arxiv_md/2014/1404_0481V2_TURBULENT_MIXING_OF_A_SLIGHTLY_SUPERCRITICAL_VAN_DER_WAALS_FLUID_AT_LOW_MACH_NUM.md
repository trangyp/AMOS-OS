---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1404.0481v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1404.0481v2_Turbulent_mixing_of_a_slightly_supercritical_Van_der_Waals_fluid_at_Low-Mach_num

> Source: 1404.0481v2_Turbulent_mixing_of_a_slightly_supercritical_Van_der_Waals_fluid_at_Low-Mach_num.pdf

> Pages: 36

---


## Page 1


Mixing in Low-Mach number supercritical jets
Turbulent mixing of a slightly supercritical Van der Waals ﬂuid at Low-Mach number
F. Battista,1 F. Picano,2 and C.M. Casciola1
1)Department of Mechanical and Aerospatial Engineering, Sapienza University,
via Eudossiana 18, 00184 Rome, Italy
2)Department of Industrial Engineering, University of Padova, via Venezia 1,
35131, Padova, Italy
(Dated: June 25, 2018)
Supercritical ﬂuids near the critical point are characterized by liquid-like densities
and gas-like transport properties. These features are purposely exploited in diﬀerent
contexts ranging from natural products extraction/fractionation to aerospace propul-
sion. Large part of studies concerns this last context, focusing on the dynamics of
supercritical ﬂuids at high Mach number where compressibility and thermodynamics
strictly interact. Despite the widespread use also at low Mach number, the turbu-
lent mixing properties of slightly supercritical ﬂuids have still not investigated in
detail in this regime. This topic is addressed here by dealing with Direct Numerical
Simulations (DNS) of a coaxial jet of a slightly supercritical Van der Waals ﬂuid.
Since acoustic eﬀects are irrelevant in the Low Mach number conditions found in
many industrial applications, the numerical model is based on a suitable low-Mach
number expansion of the governing equation. According to experimental observa-
tions, the weakly supercritical regime is characterized by the formation of ﬁnger-like
structures– the so-called ligaments –in the shear layers separating the two streams.
The mechanism of ligament formation at vanishing Mach number is extracted from
the simulations and a detailed statistical characterization is provided. Ligaments al-
ways form whenever a high density contrast occurs, independently of real or perfect
gas behaviors. The diﬀerence between real and perfect gas conditions is found in the
ligament small-scale structure. More intense density gradients and thinner interfaces
characterize the near critical ﬂuid in comparison with the smoother behavior of the
perfect gas. A phenomenological interpretation is here provided on the basis of the
real gas thermodynamics properties.
PACS numbers: 47.27.wg,47.27.ek,47.51.+a
Keywords: Van der Waals ﬂuids, Low-Mach number expansion; Supercritical ﬂuids;
Turbulent jets
1
arXiv:1404.0481v2  [physics.flu-dyn]  20 May 2014


## Page 2


Mixing in Low-Mach number supercritical jets
I.
INTRODUCTION
A supercritical ﬂuid is a phase of matter with no sharp transition between high, liquid-
like density states and low, gas-like density states that exists at pressures and temperatures
higher than those of the critical point. It consists of a unique hybrid state intermediate be-
tween liquid and gas where no surface tension acts at density interfaces. In certain regions
of the phase diagram, supercritical ﬂuids exhibit liquid-like density and gas-like transport
properties that diverge approaching the critical point. These peculiar features make su-
percritical ﬂuids attractive in several industrial and technological applications from space
propulsions to chemical extraction processes1–4.
The frequent use of supercritical ﬂuids in aerospace propulsion devices, as in liquid rocket
engines, motivated a substantial part of the studies in the literature. Indeed, numerous
experimental investigations on supercritical ﬂuids10–14 have been addressing turbulent mixing
properties, like Nitrogen/Heptane systems in experiments devoted to the basic understanding
of mixing or Hydrogen/Oxygen systems for applications to combustion. Interesting reviews
on these issues are Refs 15 and 16 which provide the state-of-the-art up to 2000. In recent
years numerical simulations also addressed supercritical mixing by investigating temporal
mixing layers17–19 and turbulent jet ﬂows20. Aiming at aerospace propulsion applications,
all these studies considered supercritical ﬂows with moderately high Mach numbers where
acoustic eﬀects and pressure ﬂuctuations are crucial17.
On the other hand many technological applications often employ ﬂuids at low speed.
In industrial applications, supercritical ﬂuids are frequently used in place of CFC for cool-
ing5, to sterilize biological materials6, for textiles cleaning, and for electronics components
degreasing7. Supercritical ﬂuids are also widely adopted for chemical extraction, e.g. to ex-
tract substances from foods8,9 in processes like decaﬀeination by CO221. For these cases at
vanishing Mach number, where acoustic eﬀects are negligible, much less attention has been
paid to turbulent mixing between a faster and a slower stream of even a single-component
supercritical ﬂuid. It turns out that, when dealing with supercritical ﬂows, the computa-
tional diﬃculties known to arise in strongly subsonic ﬂows, notably the increasingly stiﬀ
behavior of the compressible Navier-Stokes equations at increasing sound speed22,23, still
need to be addressed in detail. A major aim of the present work is to develop a consistent
treatment of a supercritical ﬂuid at small Mach number capable of being implemented in
eﬃcient numerical simulations of turbulent mixing.
In this context, the Low-Mach expansion, developed by Majda & Sethian22 for perfect-gas
reacting ﬂows, is certainly a fundamental starting point. However their formulation needs
to be substantially rearranged to allow the extension to real gas conditions. The original
part of the relevant asymptotic expansion is presented here by focusing on the special case
of Van der Waals ﬂuids. It is then a straightforward exercise adapting it to other cases of
practical interest, like to the widespread Peng-Robinson equation of state24.
Beside introducing the low Mach number expansion, the primary intent of the paper
is investigating the peculiar features of the turbulent mixing of a single-component Van
der Waals ﬂuid at vanishing Mach number and slightly supercritical pressure. The issue
is addressed by focusing on a co-axial jet with two streams at diﬀerent temperatures and
2


## Page 3


Mixing in Low-Mach number supercritical jets
velocities. Data from Direct Numerical Simulations (DNS) of real and perfect gas are com-
pared to highlight the eﬀect induced by the real gas thermodynamics. Similarly to the high
Mach number case12,13, the weakly supercritical regime is characterized by the formation of
ﬁnger-like structures (ligaments) in the shear layers separating the two streams. We show
that ligaments always form whenever a high density contrast occurs, independently of real
or perfect gas conditions. The ligament small scale structure is found to distinguish the
real from the perfect gas behavior with more intense density gradients and thinner inter-
faces characterizing the near-critical ﬂuid in comparison with the smoother behavior of the
perfect gas.
The paper is organized as follows. Section § II is dedicated to the generalized Low Mach
number expansion for real-gas ﬂows. Section § III deals with the speciﬁc aspects of the Van
der Waals model. In section § IV the variable-density turbulent coaxial jet simulations are
presented, discussing the relevant aspects of the solution algorithm. The detailed physics of
the near-critical jet dynamics is illustrated in § V that provides the main physical results
of the paper.
Final comments and conclusions are eventually reported in § VI. A few
Appendices are included at the end, to allow the illustration of certain technical aspects
without interrupting the main stream of the discussion.
II.
THE LOW-MACH NUMBER FORMULATION FOR A GENERIC
EQUATION OF STATE
In the original derivation of the low-Mach number approximation of the fully compressible,
reacting Navier-Stokes equations, Majda & Sethian22 employed the perfect gas equation of
state to describe the thermodynamic behavior of the ﬂuid. The original procedure described
in that seminal paper heavily relies on the particularly simple and speciﬁc form of the
equation of state. However, when dealing with near-critical conditions, the equation of state
should be generalized to treat more general cases and allow the use of the Van der Waals
model or other appropriate real gas descriptions.
Since deriving the approximation under these more general conditions requires a diﬀerent
manipulation of the equations, the basic procedure is here brieﬂy outlined.
3


## Page 4


Mixing in Low-Mach number supercritical jets
The fully compressible, single component Navier-Stokes equations read as
∂ρ∗
∂t∗+ ∇∗· (ρ∗u∗) = 0 ,
(1)
∂(ρ∗u∗)
∂t∗
+ ∇∗· (ρ∗u∗⊗u∗) = ∇∗· Σ∗−∇∗p∗+ f ∗,
(2)
ρ∗
∂U∗
∂t∗+ u∗· ∇∗U∗

= −p∗∇∗· u∗+ Σ∗: ∇∗⊗u∗−∇∗· q∗,
(3)
∂(ρ∗Y ∗)
∂t∗
+ ∇·(ρ∗u∗Y ∗) = ∇∗· (D∗∇∗Y ∗) ,
(4)
p∗= p∗(θ∗, ρ∗) ,
(5)
U∗= U∗(θ∗, ρ∗) ,
(6)
where the asterisk denotes dimensional variables. In the equations, t∗, ρ∗, p∗, θ∗, u∗are
time, density, pressure, temperature and velocity, respectively with ∇∗the spatial gradient
and ⊗the tensor product. Σ∗= µ∗[(∇∗⊗u∗+ (∇∗⊗u∗)T) −(µ∗
B/µ∗−2/3) (∇∗· u∗) I]
is the viscous stress tensor, µ∗(θ∗) and µ∗
B(θ∗) are the temperature dependent dynamic and
bulk viscosity, respectively, and f ∗= −ρ∗g∗ez is the gravitational force (with ez the vertical
unit vector). For simplicity, in eq. (3) the heat ﬂux q∗is assumed to follow the Fourier law,
q∗= −k∗(θ∗) ∇∗θ∗as appropriate for single component ﬂuids. U∗is the internal energy
per unit mass, obeying an equation of state in terms of temperature and density, eq. (6).
Equation (4) is the convection-diﬀusion equation for a generic passive scalar, like a tracer
that is mixed by the ﬂow. Finally, eq. (5) is a generic equation of state expressing the
pressure in terms of density ρ∗and temperature θ∗. The system can be easily extended to
deal with multi-component reactive mixtures by including additional convection-diﬀusion-
reaction equations for each species and by considering a more complete transport model for
heat and mass ﬂuxes, see e.g. Ref 25. The extension of the Low Mach number expansion to
be introduced below to the more general multi-component, reactive case is straightforward
and will not be discussed further in the following.
The Low Mach number expansion is better performed starting from the dimensionless
system. After selecting a characteristic length ℓ∗
R, a speed |u∗
R|, a pressure p∗
R and a density
ρ∗
R, the other reference quantities follows as
t∗
R =
l∗
R
|u∗
R|,
U∗
R = p∗
R
ρ∗
R
,
θ∗
R = θ∗
R (p∗
R, ρ∗
R)
(7)
where the characteristic temperature θ∗
R is expressed as a function of reference pressure and
density through the pressure equation of state (5), see also § III. The dimensionless system
4


## Page 5


Mixing in Low-Mach number supercritical jets
reads
∂ρ
∂t + ∇·(ρu) = 0
(8)
∂(ρu)
∂t
+ ∇·(ρu ⊗u) = 1
Re ∇·Σ −
1
γRd
Ma
2∇p −
1
Fr2ρez
(9)
ρ
∂U
∂t + u · ∇U

= −p∇·u + γRd
Ma
2
Re
Σ : ∇⊗u +
c∗
pR
ZR∗
m
1
Re Pr ∇· (k∇θ)
(10)
∂(ρY )
∂t
+ ∇·(ρuY ) =
1
ReSc∇·(D∇Y )
(11)
p = p(θ, ρ)
(12)
U = U(θ, ρ) ,
(13)
where the relevant dimensionless parameters are
d
Ma =
|u∗
R|
p
γRp∗
R/ρ∗
R
,
Re = |u∗
R| ℓ∗
R ρ∗
R
µ∗
R
,
Pr = cp∗
Rµ∗
R
k∗
R
,
(14)
Fr =
|u∗
R|
p
ℓ∗
Rg∗,
Sc =
µR
DRρ∗
R
,
with c∗
pR = c∗
p(θ∗
R, ρ∗
R) being c∗
p = ∂[U∗+ p∗/ρ∗] /∂θ∗
|p∗the constant-pressure speciﬁc heat
coeﬃcient, R∗
m is the gas constant, Z = p∗
R/(R∗
mθ∗
Rρ∗
R) is the compressibility factor, and k∗
R
and µ∗
R the thermal diﬀusion coeﬃcient and the dynamic viscosity, respectively, evaluated at
the reference temperature θ∗
R. d
Ma takes the role of the Mach number, even if the quantity in
the denominator does not directly coincide with the sound speed at reference thermodynamic
conditions, since in general, for a real gas, c2
R = ∂p∗/∂ρ∗
|S∗(θ∗
R, ρ∗
R) ̸= γRp∗
R/ρ∗
R with γR the
ratio of constant pressure to constant volume speciﬁc heat and cR the actual sound speed in
the reference conditions.
The Low Mach number formulation, Ref 22, amounts to introducing the asymptotic
expansion
f(x, t) = f0(x, t) + f2(x, t)d
Ma
2 + O(d
Ma
4) .
(15)
for the generic variable into system (8)-(13). After grouping together terms with the same
power in the Mach number and requiring that the resulting equations should be identically
satisﬁed for any, suﬃciently small Mach number, the system of equations governing the
diﬀerent terms in expansion (15) is readily obtained.
5


## Page 6


Mixing in Low-Mach number supercritical jets
The zero-th order contribution to the mass conservation equation is
∂ρ0
∂t + ∇·(ρ0u0) = 0 .
(16)
The same procedure applied to the momentum conservation provides a ﬁrst contribution
formally diverging like 1/d
Ma
2.
Removing this low Mach number divergence yields the
equation
∇p0 = 0 ⇒p0 = p0(t) ,
(17)
that implies a spatially constant zero-th order (thermodynamic) pressure. A second contri-
bution arises at zero-th order in the Mach number and is given by
∂(ρ0u0)
∂t
+ ∇·(ρ0u0 ⊗u0) = 1
Re ∇·Σ0 −∇p2 + ρ0
Fr2ez ,
(18)
where p2 is the second order (hydrodynamic) pressure22. Analogously, the zero-th order
equation for the transported scalar follows as
∂(ρ0Y0)
∂t
+ ∇·(ρ0u0Y0) =
1
ReSc∇·(D∇Y0) .
(19)
In order to complete the asymptotic expansion for real gases it is worth recasting the
energy equation (10) in terms of temperature exploiting the equation of state (13) (more
details are given in Appendix C),
ρ c∗
v
R∗
m
Dθ
Dt = −Zθ ∂p
∂θ

ρ
∇·u + Z γRd
Ma
2
Re
Σ : ∇u + c∗
p
R∗
m
1
Re Pr ∇· (k∇θ) ,
(20)
where c∗
v = ∂U∗/∂θ∗|v∗is the constant-volume speciﬁc heat coeﬃcient. Exploiting the Low-
Mach number expansion of the temperature equation, the zero-order contribution follows
as
ρ0
c∗
v0
R∗
m
Dθ0
Dt = −Zθ0
∂p0
∂θ0

ρ0
∇·u0 + c∗
p0
R∗
m
1
Re Pr ∇· (k0∇θ0)
(21)
where c∗
v0 = c∗
v (θ∗
Rθ0, ρ∗
Rρ0) and c∗
p0 = c∗
p (θ∗
Rθ0, ρ∗
Rρ0). The equation is further manipulated
by expressing the temperature derivative on the left-hand side though the mass-conservation
equation, where the density is expressed as ρ∗= ρ∗(θ∗, p∗), eq. (5),
1
ρ0
Dρ
Dt

0
=
θ∗
R
ρ∗
∂ρ∗
∂θ∗|p∗

p∗=p∗
Rp0
θ∗=θ∗
Rθ0
Dθ
Dt

0
+
 
p∗
R
ρ∗
∂ρ∗
∂p∗|θ∗
!
θ∗=θ∗
Rθ0
p∗=p∗
Rp0
Dp
Dt

0
= −α0
Dθ
Dt

0
+ β0
Dp
Dt

0
= −∇·u0 ,
(22)
where the dimensionless thermal expansion and isothermal compressibility coeﬃcients,
α0(θ0, p0) and β0(θ0, p0), respectively, are implicitly deﬁned by comparing the second and
6


## Page 7


Mixing in Low-Mach number supercritical jets
the third member of the equation. Substituting the material derivative of temperature from
equation (22) into (21) yields
ρ0
c∗
v0
R∗
m
β0
α0
Dp0
Dt + c∗
v0
R∗
m
ρ0
α0
∇·u = −Zθ0
∂p0
∂θ0

v0
∇·u0 + c∗
p0
R∗
m
1
Re Pr ∇· (k0∇θ0) ,
(23)
where the zero-th order contribution to the pressure term depends only on time, Dp0/Dt =
dp0/dt, as shown in eq. (17). The velocity divergence then reads
∇·u0 =
−ρ0
c∗
v0
R∗
m
β0
α0
dp0
dt + c∗
p0
R∗
m
1
Re Pr ∇· (k0∇θ0)
c∗
v0
R∗
m
ρ0
α0
+ Zθ0
∂p0
∂θ0

ρ0
.
(24)
Summarizing, the complete system in the zero-th order approximation is
∂ρ0
∂t + ∇·(ρu)0 = 0
(25)
∂(ρu)0
∂t
+ ∇·[(ρu)0 ⊗u0] = 1
Re ∇·Σ0 −∇p2 +
1
Fr2ρ0ez
(26)
∇·u0 =
−ρ0
c∗
v0
R∗
m
β0
α0
dp0
dt + c∗
p0
R∗
m
1
Re Pr ∇· (k0∇θ0)
c∗
v0
R∗
m
ρ0
α0
+ Zθ0
∂p0
∂θ0

ρ0
(27)
∂(ρ0Y0)
∂t
+ ∇·(ρ0u0Y0) =
1
ReSc∇·(D∇Y0)
(28)
p0(t) = p [θ0(x, t), ρ0(x, t)] .
(29)
The crucial features of the system of equations we arrived at are worth begin emphasized:
i) Zero-th order density ρ0(x, t) and temperature θ0(x, t) are not independent ﬁelds since
they are locally coupled through the equation of state (29).
Indeed the time evolution
of the thermodynamic pressure p0(t) follows by integrating (27) over the, generally time
dependent, ﬂow domain D(t) and accounting for the boundary conditions on the normal
velocity component and on the temperature,
dp0
dt
Z
D(t)
ρ0
c∗
v0
R∗
m
β0
α0
dV =
Z
∂D(t)
c∗
p0
R∗
m
1
Re Pr k0
∂θ0
∂n dS −
Z
D(t)
1
Re Pr k0∇θ0 · ∇
 c∗
p0
R∗
m

dV
(30)
−
Z
D(t)
 
c∗
v0
R∗
m
ρ0
α0
+ Zθ0
∂p0
∂θ0

ρ0
!
dV
Z
∂D(t)
u0 · ndS .
7


## Page 8


Mixing in Low-Mach number supercritical jets
Stepwise integration allows to determine p0(t) and to eliminate either density or temperature
in favour of the other ﬁeld through (29). In particular, the pressure is constant for the present
problem in an unbound domain, i.e. p0(t) = p0 = const. ii) Acoustic waves are implicitly
ﬁltered out of the system, since the equation of state for pressure only enters at the lowest
order, where pressure is spatially constant. The thermodynamic pressure is decoupled in this
way from turbulence- and thermal-induced spatial variations of density, preventing acoustic
waves from propagating in the medium. These eﬀects can possibly be consistently recovered
at next orders in the approximation. iii) The ﬂuid density is allowed to change both in
space and time to comply with thermal expansion eﬀects– heat release due to combustion
and heat transfer are perfectly consistent within the assumed approximation limits. iv) No
assumption is made as concerning the thermodynamic model of the ﬂuid. This is essential
in view of our present aim of modelling turbulent mixing of slightly supercritical ﬂuids. For
the sake of deﬁniteness, it should be stressed that resonance eﬀects associated with thermo-
acoustic coupling cannot be consistently dealt with within the range of validity of the present
approximation, since, by non-linear coupling, they bring acoustics in foreground calling for
a complete modelling of wave propagation.
III.
THERMODYNAMIC ASSUMPTIONS
As anticipated in the § I, the perfect gas equation of state is not suitable to describe
the thermodynamic behavior close to the critical point. Indeed the Van der Waals equation
of state is presumably the simplest extension of the perfect gas model able to consistently
deal with the thermodynamics of a diatomic gas at a slightly super-critical pressure. It will
be hereafter assumed for its simplicity in the present application of the Low-Mach number
expansion which, however, can be easily adapted to more general cases, like e.g. the Peng-
Robinson equation of state24, see Appendix A 2.
The Van der Walls theory is directly derived from statistical mechanics, see e.g. Ref 26,
and allows a complete and straightforward thermodynamic characterization of the gas start-
ing from the Helmholtz free energy f ∗= −Nkbθ ln (Z∗) of the system expressed in terms of
the canonical partition function Z∗(N, V, θ) of the corresponding atomistic model. Here N is
the number of gas molecules, V the volume and kB the Boltzmann constant, see Appendix A
for a brief review of the subject. The pressure equation of state follows as
p∗= −∂f ∗
∂V ∗

θ∗,N
= R∗
mθ∗ρ∗
1 −b′∗ρ∗−a′∗ρ∗2 ,
(31)
where a′∗and b′∗are the Van der Waals coeﬃcients that account for intermolecular forces
and excluded volume, respectively. Thermal expansion and isothermal compressibility coef-
ﬁcients, α∗and β∗respectively,
α∗= −
R∗
m
2a′∗ρ∗−3a′∗b′∗ρ∗2 −p∗b′∗−R∗
mθ∗
β∗=
(1 −b′∗ρ∗) /ρ∗
2a′∗ρ∗−3a′∗b′∗ρ∗2 −p∗b′∗−R∗
mθ∗
8


## Page 9


Mixing in Low-Mach number supercritical jets
follow directly from the pressure equation of state. All these thermodynamic relationships
can be expressed in dimensionless form. Assuming p = p0 + O

d
Ma
2
, with similar ex-
pressions for θ and ρ, leads to the leading order contributions in the Low Mach number
expansion for pressure, thermal expansion and isothermal compressibility,
p0 =
θ0ρ0
Z(1 −b′ρ0) −a′ρ2
0 ,
(32)
α0 = −
1
Z (2a′ρ0 −3a′b′ρ2
0 −p0b′) −θ0
(33)
β0 =
(1 −b′ρ0) /ρ0
2a′ρ0 −3a′b′ρ2
0 −p0b′ −θ0/Z
(34)
where a′ = a′∗ρ∗2
R /p∗
R and b′ = b′∗ρ∗
R.
Applying the analysis presented in section § II to the Van der Waals equation of state,
most of the equations in system (25)-(29) remain unchanged, while velocity divergence and
pressure equation of state become
∇·u0 =
1
Z p0
 c∗
p0
R∗
m
1
RePr ∇·(k∇θ)0



1
1 + (γ −2) aρ2
0
p0γ
+ 2a′b′ρ3
0
p0γ


(35)
θ0 = Z p0
ρ0

1 + a′ρ2
0
p0

(1 −b′ρ0) .
(36)
In eq. (35) γ = c∗
p0/c∗
v0 and the spatially constant pressure has been assumed constant
also in time, p0(t) = const, as appropriate for a free jet conﬁguration where the discharge
pressure is a known parameter. Overall, the system is formed by seven equations in the
seven unknowns ρ0, u0, p2, Y0 and θ0. Peculiar feature is the presence of the hydrodynamic
pressure p2 in the momentum equation22. Under this respect, the system is similar to the
incompressible Navier-Stokes equations where the pressure takes the mathematical role of a
Lagrange multiplier that allows to enforce the constraint (35) on the velocity.
As a ﬁnal comment on the mathematical model, we like stress once more that the same
machinery would work in the same way also for diﬀerent gas models.
IV.
NUMERICS AND PHYSICAL PARAMETERS
The DNS of a coaxial jet of a Van der Waals gas –hereafter referred to as real-gas–
is performed employing cylindrical coordinates (r, ϕ, z), with z the axial coordinate, r the
radial coordinate in the transverse plane and ϕ the angle, in the cylindrical domain with
dimensions [ϕmax×Rmax×Zmax] = [2π×18R×20R] with [Nϕ×NR×NZ] = [128×281×600]
collocation points. The geometry of the system – ﬁgure 1 – consists of a coaxial jet with inner
nozzle radius R and with inner and outer radii of the outer jet R1 = 1.2R and R2 = 1.5R,
respectively. The jet discharges in a cylindrical domain with radius Rmax = 18R, large
9


## Page 10


Mixing in Low-Mach number supercritical jets
R2
R1
LN2
Zmax
Rmax
GN2
outer
GN2
inner
R
outer
Figure 1.
Schematic diagram of the coaxial jet used in the present simulations.
Liquid-like
density Nitrogen N2 is injected through the “Inner” nozzle while the “Outer” nozzle discharges
gaseous Nitrogen N2 in the high pressure environment. In dimensionless variables the inner radius
is R = 1.
enough to allow the use of traction free conditions on the side boundary. The axial extent
of the computational domain is Zmax = 20R with convective27 boundary condition used at
the exit section. The numerics models an apparatus with suﬃciently long inlet manifold
to have fully developed turbulence at the core inlet. On the contrary, the outer stream is
considered to be fed by a short annular manifold, such that the inﬂow velocity is constant
through the section. The core inlet turbulence is taken from a companion turbulent pipe
ﬂow at matching conditions, see e.g.
Refs 28 and 29 for more details.
In the diﬀerent
simulations addressed below the mean inlet velocity and density typically change, and the
diﬀerent cases are compared at the same turbulent intensity q/|u∗
R|, with q =
p
⟨u′
iu′
i⟩and
u′
i the instantaneous velocity ﬂuctuation.
In the radial direction grid stretching is applied to resolve the shear layer occurring
at the boundary between the internal and the external jet and between the external jet
and the surrounding environment.
Given the Kolmogorov scale at the inlet of the core
jet (η ≃0.01 R) the grid size, ∆r = 0.0125 R in the shear layers, is able to accurately
capture the ﬁnest scales of turbulence. The present discretization also enables capturing the
strong density gradients which take place across the inner shear layer separating the outer
stream from the core jet, see also Refs 30 and 31 for similar considerations in the context
of combustion. The basic simulation to be discussed deals with a real gas coaxial Nitrogen
jet in transcritical conditions, to be addressed as simulation A to distinguish it from several
others we performed to highlight real gas eﬀects on turbulent jet dynamics.
Geometry
and thermodynamic parameters are chosen to be similar to the coaxial jet experiments
presented by Mayer et al.. Clearly the Reynolds number amenable to DNS is signiﬁcantly
smaller than the experimental one, ReD = 6000 compared to the experimental value of
order of O(104 −105)14,32. This Reynolds number value can be achieved, e.g., by considering
an inner nozzle of diameter D∗= 1.8 mm with typical injection velocity |u∗
core| = 0.2 m/s,
density ρ∗
core = 320 kg/m3 and dynamic viscosity µ∗= 1.9 × 10−5 Pa/s, corresponding to
10


## Page 11


Mixing in Low-Mach number supercritical jets
10−2
10−1
100
101
102
100
101
102
103
104
p/pc
ρc/ρ
10−4
10−3
10−2
10−1
100
101
100
101
102
ρ/ρc
θ/θc
0
0.4
0.8
1.2
15
30
0
0.4
0.8
1.2
15
30
0
0.4
0.8
1.2
15
30
0
0.4
0.8
1.2
15
30
0
0.4
0.8
1.2
15
30
0
0.4
0.8
1.2
15
30
0
0.4
0.8
1.2
15
30
0
0.4
0.8
1.2
15
30
0
0.4
0.8
1.2
15
30
10−2
10−1
100
101
102
100
101
p/pc
ρc
10−4
10−3
10−2
10−1
100
101
100
ρ/ρc
θ/
0.4
0.8
1.2
0.4
0.8
1.2
0.4
0.8
1.2
0.4
0.8
1.2
0.4
0.8
1.2
0.4
0.8
1.2
0.4
0.8
1.2
0.4
0.8
1.2
0.4
0.8
1.2
(a)
(b)
Figure 2.
Panel (a): pressure-density diagram (log-log coordinates) for the Van der Waals
equation of state. Solid lines: isotherms at diﬀerent temperatures for the Van der Waals equation
of state. Dash-dotted lines: isotherms for the perfect fas equation of state. Dotted line (purple in
the electronic version): critical isotherm. Symbols: thermodynamics injection conditions of each
simulation, namely Sim A and C (asterisks), Sim B (squares), and Sim D (circles). Panel (b): ˆρ−ˆθ
phase diagram and injection conditions of each simulation, same symbols as in panel (a). Inset:
same quantities in linear scale.
slightly supercritical Nitrogen. The sound speed at core inlet is c∗= 179 m/s, leading to
a Mach number Ma = 1 × 10−3 consistently with the adoption of the low Mach number
expansion described in the previous sections.
The Nitrogen coaxial jet is assumed to discharge in a gaseous N2 environment at p∗
env =
4.0 MPa, slightly above the Nitrogen critical pressure (p∗
c ≃3.4MPa, p∗
env/p∗
c = 1.168).
The core jet is injected at a density slightly exceeding the critical density ρ∗
core ≃1.04ρ∗
c,
while the external stream has density ten times lower, ρ∗
core/ρ∗
ext = 10, matching that of
the surrounding environment ρ∗
core > ρ∗
c > ρ∗
ext = ρ∗
env. The injection temperature of the
core is θ∗
core = 131.46 K (with θ∗
c = 126.2 K), while external jet and environment are at
θ∗
env = 529.79 K, with a temperature ratio θ∗
env/θ∗
core ≃4.
Panel (a) of ﬁgure 2 provides the pressure-density diagram (log-log coordinates) for the
Van der Waals equation of state in reduced variables ˆθ = 3/8 (ˆp + 3ˆρ2) (1/ˆρ −1/3) and
ˆp = p/pc, 1/ˆρ = ρc/ρ, ˆθ = θ/θc.
The dotted line is the critical isotherm ˆθ = 1.
The
other solid lines are isotherms at increasing temperature.
The dash-dotted lines sketch
the corresponding isotherms for the perfect gas equation of state, ˆθ = 3ˆp/ (8ˆρ). The limit
behavior of the perfect gas is achieved when two conditions are met, namely i) ˆp ≫3ˆρ2, with
the curve ˆp = 3ˆρ2 shown as the dash-double-dotted line of slope −2, and ii) ˆρ ≪3, which is
the vertical axis delimiting the plot on the left. Increasing the temperature the perfect gas
limit is recovered, uppermost solid line of slope −1. Moving along an isotherm the perfect
gas limit is reached as well at suﬃciently low pressure.
The symbols reported in panel (a) of ﬁgure 2 provide the thermodynamic conditions for
the simulations considered in the paper. The two asterisks are the working points for core
jet and environment (leftmost and rightmost symbol, respectively) for the real gas cases,
11


## Page 12


Mixing in Low-Mach number supercritical jets
simulations A and C of Table I. The two open squares (one of which superimposed to an
asterisk) give the corresponding points for the perfect gas simulation, simulation B in the
same Table. Both asterisks and open squares are on the same isobar, at slightly supercritical
pressure ˆp = 1.17. The density ratio for simulations A, C (asterisks) and B (open squares) is
the same, ρcore/ρext ≃10. On the two isotherms concerning the real gas conditions (asterisks)
two additional working points at a substantially lower pressure, ˆp = 0.02941 corresponding
to atmospheric pressure for Nitrogen, are denoted by open circles and provide the injection
conditions for simulation D. Here the gas behavior can be approximated with the perfect
gas law. The temperature ratio for simulation D is the same as that for simulations A and
C. Clearly the density ratio is instead much lower, ρcore/ρext ≃4. The ˆρ −ˆθ phase diagram
of the conditions of each simulation is represented in panel (b) of ﬁgure 2.
The two constants of the Van der Waals model, a∗= 3p∗
c/ρ∗2
c
and b∗= 1/ (3ρ∗
c), are
determined from the critical pressure and density of Nitrogen. Assuming the value of the
universal gas constant, the critical temperature is estimated as θ∗
c = 8p∗
c/ (3R∗
mρ∗
c) = 97.22 K
in comparison with 126.2 pertaining to actual Nitrogen. For our purposes, the Van der Waals
model reproduces acceptably well the behavior of Nitrogen with the advantage of having a
clear and reasonably simple theoretical derivation. In case better accuracy were needed,
alternatives are available, e.g. the Peng-Robinson model.
For the reader’s convenience, it may be worth mentioning what the rationale behind
the parameters selection for simulation B is. Simulation B, squares in ﬁgure 2, has same
pressure and density ratio ρ∗
core/ρ∗
env = 10 of simulation A. The diﬀerence is the larger
injection temperatures such that Nitrogen behaves as a perfect gas, θ∗
core = 529.79 K and
temperature ratio θ∗
env/θ∗
core = ρ∗
core/ρ∗
env = 10.
At constant pressure, the dynamics of
a strongly subsonic perfect gas is substantially controlled by density ratio, Prandtl and
Reynolds number. Instead, the parameters entering the description of real gas dynamics also
include the distance of the injection conditions from the critical point. Indeed simulation B
is designed to achieve the same density ratio and injection pressure of simulation A, using the
perfect gas equation of state in the region of the parameter space where Nitrogen recovers
the perfect gas behavior.
Indeed, a part from the real vs perfect gas issue, an additional diﬀerence exists between
simulations A and B, namely the diﬀerent range of temperatures which aﬀects the transport
coeﬃcients. In order to discriminate between the eﬀect of thermodynamic behavior and
temperature range, a third simulation, C, has been conceived with same thermodynamic
conditions and gas model of simulation A (real gas), now artiﬁcially enforcing the Prandtl
number of simulation B (perfect gas).
It is important to recall that in all the three cases just considered the density ratio between
inner core and external jet plus environment is a large one, ρ∗
core/ρ∗
env = 10. It is worthwhile
comparing the results with a fourth simulation, D, where the density ratio is substantially
lower due to a lower environment pressure, as for Nitrogen at atmospheric pressure and same
injection temperatures of the basic simulation A (real gas), θ∗
core = 131.46 K, θ∗
env/θ∗
core ≃4,
which results in ρ∗
core/ρ∗
env = 4.
This simulation is performed with the Van der Waals
equation of state and the actual transport coeﬃcients of Nitrogen in the parameter region
where Nitrogen behaves almost like a perfect gas (i.e. the real system could have been
12


## Page 13


Mixing in Low-Mach number supercritical jets
sim A-C
inner jet
outer jet
surrounding environment
p∗
p∗
R
p∗
R
p∗
R
ρ∗
ρ∗
R
0.1 ρ∗
R
0.1 ρ∗
R
θ∗
θ∗
R
4 θ∗
R
4 θ∗
R
(ρ∗U∗A∗)inj
ρ∗
R|u∗
R|πR∗2
0.234 ρ∗
R|u∗
R|πR∗2
–
(ρ∗U∗2A∗)inj ρ∗
R|u∗
R|2πR∗2 1.296 ρ∗
R|u∗
R|2πR∗2
–
sim B
inner jet
outer jet
surrounding environment
p∗
p∗
R
p∗
R
p∗
R
ρ∗
ρ∗
R
0.1 ρ∗
R
0.1 ρ∗
R
θ∗
θ∗
R
10 θ∗
R
10 θ∗
R
(ρ∗U∗A∗)inj
ρ∗
R|u∗
R|πR∗2
0.234 ρ∗
R|u∗
R|πR∗2
–
(ρ∗U∗2A∗)inj ρ∗
R|u∗
R|2πR∗2 1.296 ρ∗
R|u∗
R|2πR∗2
–
sim D
inner jet
outer jet
surrounding environment
p∗
p∗
R
p∗
R
p∗
R
ρ∗
ρ∗
R
0.25 ρ∗
R
0.25 ρ∗
R
θ∗
θ∗
R
4 θ∗
R
4 θ∗
R
(ρ∗U∗A∗)inj
ρ∗
R|u∗
R|πR∗2
0.234 ρ∗
R|u∗
R|πR∗2
–
(ρ∗U∗2A∗)inj ρ∗
R|u∗
R|2πR∗2 1.296 ρ∗
R|u∗
R|2πR∗2
–
Table I. Thermodynamic and physical conditions at injection and surrounding environment nor-
malized with the reference quantities. Top table: real gas (simulations A-C) where the reference
quantities are: p∗
R = 1.178p∗
c, ρ∗
R = 1.0424ρ∗
c and θ∗
R = 1.0417θ∗
c. Middle table: perfect gas (simula-
tion B) with reference quantities: p∗
R = 1.178p∗
c, ρ∗
R = 0.10424ρ∗
c and θ∗
R = 4.198θ∗
c. Bottom table:
real gas (simulation D) where the reference quantities are p∗
R = 0.0294117p∗
c, ρ∗
R = 0.010672ρ∗
c and
θ∗
R = 1.04θ∗
c; due to low pressure and density the limit of perfect gas behavior is almost reached.
accurately approximated with the perfect gas equation of state).
Concerning momentum, in all the four cases the momentum ratio is kept constant at
ρ∗
ext|u∗
ext|/ (ρ∗
core|u∗
core|) = 0.4. For the purpose of making equations dimensionless reference
conditions are selected as the corresponding core jet features ρ∗
R = ρ∗
core, p∗
R = p∗
core =
p∗
env, |u∗
R| = |u∗
core|.
Table I provides detailed information for the diﬀerent simulations.
We stress once more that in cases A and B density and momentum ratios between core
and outer stream are the same, ρ∗
core/ρ∗
ext = 10 and (ρ∗
ext|u∗
ext|) / (ρ∗
core|u∗
core|) = 0.4. The
comparison is aimed at addressing the eﬀects of supercritical injection on jet dynamics
and mixing process, at low-Mach number, hence with neglecting acoustic eﬀects. The two
simulations mainly diﬀer for the temperatures of core and outer jet. While in the perfect
gas case, for given pressure, the density ratio ρ∗
core/ρ∗
ext = 10 results in the temperature ratio
θ∗
core/θ∗
ext = 0.1, in the real gas case the temperature ratio is θ∗
core/θ∗
ext ≃0.25. The bottom
panel of Table I provides the physical and thermodynamic conditions of simulation D. Here
since the temperature ratio θ∗
ext/θ∗
core matches that of simulation A, the density ratio is much
13


## Page 14


Mixing in Low-Mach number supercritical jets
101
102
103
104
0
50
100
150
200
250
300
350
µ(θ,p) (µPa s)
θ (K)
p=1.0 pc
p=1.17pc
p=1.5 pc
p=2.0 pc
p=3.0 pc
p=4.0 pc
p=5.0 pc
102
103
0
50
100
150
200
250
300
350
k(θ,p) (µPa s)
θ (K)
p=1.0 pc
p=1.17pc
p=1.5 pc
p=2.0 pc
p=3.0 pc
p=4.0 pc
p=5.0 pc
(a)
(b)
Figure 3.
Dependence of Nitrogen viscosity µ(θ, p), panel (a), and thermal conductivity k(θ, p),
panel (b), on temperature and pressure. The complete analytical relations are provided in Ap-
pendix B.
smaller than all the other cases, ρ∗
core/ρ∗
ext = θ∗
ext/θ∗
core ≃4.
The model is completed with the expressions for dynamic viscosity and thermal diﬀusivity
as a function of pressure and temperature. We use here the relations provided in Ref 33,
µ∗= µ∗0(θ∗) + µ∗r(τ, δ)
k∗= k∗0(θ∗) + k∗r(τ, δ) + k∗c(τ, δ)
(37)
where τ = θ∗
c/θ∗and δ∗= ρ∗/ρ∗
c, with µ∗0 and k∗0 the perfect gas viscosity and thermal
conductivity, respectively, µ∗r and k∗r the so-called residual ﬂuid contributions, and k∗c the
critical enhancement of thermal conductivity33. Since the eﬀect of the critical condition
on viscosity is negligible no critical enhancement is considered. The expressions entering
eqs. (37) are explicitly reported in Appendix B with the model constant chosen to reproduce
Nitrogen. Figure 3 shows the resulting behavior of viscosity and thermal conductivity as a
function of temperature and pressure.
Using the core jet parameters as reference conditions, eqs. (7), the Prandtl number,
eq. (14), is Pr = 0.35 for simulation A (real gas), Pr = 0.6 for simulation B (high pressure
perfect gas case) and C (real gas with transport coeﬃcient matching the high pressure
perfect gas case B) and Pr = 0.75 for simulation D (low pressure case, real gas behaving
like a perfect gas).
These values are determined through the transport coeﬃcients (37)
and the speciﬁc heat coeﬃcient (A6) evaluated at the respective reference thermodynamic
conditions. It is worth stressing that the diﬀerence in the Prandtl number between cases A
and B/C is substantial.
In all cases buoyancy is neglected since it would have introduced an explicit dependence
on the density ratio, thus hampering a fair comparison between the diﬀerent gas models.
14


## Page 15


Mixing in Low-Mach number supercritical jets
A
B
C
D
Figure 4.
Normalized mean density ﬁelds ρ∗/ρ∗
jet. From left to right: real gas jet (sim. A), perfect
gas jet (sim. B), real gas jet with perfect gas transport properties (sim. C) and real gas jet at low
pressure (sim. D), respectively.
V.
RESULTS
A.
Mean ﬁelds
As anticipated four simulations are considered. For each of them average ﬁelds are ex-
tracted by ensemble averaging of about 200 independent instantaneous conﬁgurations sep-
arated in time by 0.25R/Ur. Each sample was acquired after the ﬂow reached statistically
steady conditions. The typical correlation time τc = 0.083R/Ur is estimated from the au-
tocorrelation of the axial velocity ﬂuctuation u′
z(φ, r, z, t) = uz −⟨uz⟩on the jet axis one
diameter downstream of the inlet section (r = 0, z = D),
τc =
Z 50R/Ur
0
Z 50R/Ur
0
u′
z(φ, 0, D, t)u′
z(φ, 0, D, t + τ)dtdτ
Z 50R/Ur
0
u′
z
2(φ, 0, D, t)dτ
.
Here and in the following, the subscript 0 is dropped from the variables, since no confusion
may arise and the hydrodynamic pressure p2 is never mentioned explicitly.
The dimensionless average density ρ∗/ρ∗
core is illustrated in ﬁgure 4 where it ranges from 1
in the jet core to 0.1 in the outer stream for the three density matched simulations including
both the two real gas simulations (case A and C) and the perfect gas simulation (case B).
The density ranges instead from 1 (core jet) to 0.25 in the outer stream for simulation D
15


## Page 16


Mixing in Low-Mach number supercritical jets
Figure 5.
Normalized mean temperature ﬁelds θ∗/θ∗
ext. From left to right: real gas jet (sim. A),
perfect gas jet (sim. B), real gas jet with perfect gas transport properties (sim. C) and real gas jet
at low pressure (sim. D), respectively.
(low pressure, real gas case) which is temperature matched with the high pressure, real gas
simulations A and C. The mixing eﬃciency may be quantiﬁed by the extension of the core
region measured, e.g., by the intercept on the jet axis of a selected high-density isoline,
ρ∗= 0.95ρ∗
core in the present case. The ﬁgure shows that the low pressure case (D) exhibits
the longest core length.
Concerning the dimensionless temperature θ∗/θ∗
ext, ﬁgure 5, its normalized mean ﬁeld
ranges from 4 in the jet core to 1 in the outer stream for the real gas cases (A and C). For
the perfect gas case B the temperature ranges instead from 10 in the jet core to 1 in the
outer part. In other words, at ﬁxed density ratio, a higher temperature ratio characterizes
the perfect gas case as a consequence of the diﬀerent equation of state that become crucial
in near critical conditions.
B.
Instantaneous ﬁelds
The four panels in Figure 6 compare planar cuts of instantaneous axial momentum ﬁelds,
ρuz, shaded contours. The solid lines denote two density isolevels, namely ρ = 0.9 and
ρ = 0.2, respectively. In the near ﬁeld, close to the inlet, typical structures are apparent at
the shear layers formed between inner and outer streams where high density contrast occurs
between inner and outer jet (cases A, B, and C). They correspond to the ﬁnger-like objects
16


## Page 17


Mixing in Low-Mach number supercritical jets
Figure 6. Axial momentum ﬁeld (ρuz, gray scale contours) with two density isolevels (ρ = 0.9, 0.2,
respectively) shown by solid lines. From left to right: case A (real gas, high pressure), case B
(perfect gas, high pressure), case C (real gas, with modiﬁed transport coeﬃcients) and case D (real
gas, low pressure). In the last case the 0.2 density isoline does not exist.
observed in the experimental snapshot10,34 and known to characterize supercritical jets also
at moderate Mach numbers. Such structures are much less apparent in the low density ratio
case D (atmospheric pressure case). Interestingly they also exist in the high pressure perfect
gas jet (B), conﬁrming that they are associated with the high density contrast between
inner and outer stream. The structures are similar to the ligaments occurring in the break-
up of a liquid jet35.
They are formed through a similar kinematic mechanism but are
associated with diﬀerent thermodynamic phenomenologies10,11. The liquid (subcritical) jet
is characterized by two immiscible phases, liquid and gaseous, with no mutual diﬀusion. In
this case the joint eﬀect of shear and capillary instability promoted by the surface tension
acting at the liquid-gas interface induces droplet formation.
The external high velocity
gas stream stretches the liquid core, forming ﬁnger-like structures that elongate until they
break-up into droplets due to capillarity35,36. For the cases at high core density (A, B, and
C), the density continuously varies from a liquid-like large value in the core to a gas-like
low value in the external stream. No truly sharp interface exists however, and consequently
no corresponding surface tension. In this context the ﬁnger-like structures observed in the
corresponding panels of ﬁgure 6 are still due to the stretching of the inner core by the faster
external stream. However their persistence cannot be ascribed to phase separation, like in
the liquid-gas system. Rather they are due to a relatively poor diﬀusivity of the high density
features in the background low density environment. Indeed the essential phenomenology is
associated with thermal diﬀusivity which, at ﬁxed injection pressure, tends to smear out the
temperature diﬀerence existing between low temperature ﬂuid structures originated in the
core and the high temperature surroundings. If the process occurs too slowly with respect
to the typical axial velocity, the density structures tend to persist for a signiﬁcant length
beyond the inlet section. This jet dynamics at supercritical conditions is known in literature
as jet disintegration11,12.
17


## Page 18


Mixing in Low-Mach number supercritical jets
The concept is better illustrated by manipulating the continuity equation (25) by inserting
the expression for the velocity divergence provided by the energy equation (27),
∂ρ
∂t + u · ∇ρ = −ρ
Zp
1
RePr∇·(k∇θ)


1
1 + (γ −2) aρ2
pγ
+ 2abρ3
pγ

.
(38)
On the basis of this equation, the density adapts along a ﬂuid trajectory due to thermal
diﬀusion that forces the ﬂuid expansion toward thermodynamic equilibrium with the external
conditions. As a matter of fact, as the core jet thermodynamic state approaches the critical
point, the temperature diﬀerence between inner and outer streams keeps on reducing for
given density ratio, see the asterisks in comparison with open squares in the right panel of
ﬁgure 2. Given the injection pressure, the material derivative of the density on the left hand
side of the equation can be expressed as Dρ/Dt = (∂ρ/∂θ)p Dθ/Dt, so that the eﬀective
P´eclet number for the temperature equation, Dθ/Dt = (1/Pe) ∇· (k∇θ), is given by
1
Pe = −
∂θ
∂ρ

p
ρ
Zp
1
RePr


1
1 + (γ −2) aρ2
pγ
+ 2abρ3
pγ

> 0 .
The dependence of both P´eclet number and dimensionless thermal conductivity k on the
local temperature is non-linear and does not easily allow to predict the eﬀective diﬀusion of
the jet in presence of turbulence. It is then worthwhile extracting from the simulation an
eﬀective turbulent diﬀusivity D∗
eff. It is constructed with a transverse diﬀusion length-scale
– in the present case the radius of the inner injection nozzle R∗(we recall that the asterisk
denote dimensional quantities) – and the convective characteristic time-scale T ∗= z∗
D/|u∗
core|
corresponding to the time needed by a particle travelling on the axis of the jet to reach the
position where mixing between internal and external streams is completed. In practice the
mixing length z∗
D is quantiﬁed by the distance from the jet nozzle where the average local
density on the axis decreases by a prescribed amount with respect to the injection condition,
see the isoline highlighted in ﬁgure 4. The turbulent diﬀusivity follows as
D∗
eff = R∗2|u∗
core|
z∗
D
providing the expression for the turbulent P´eclet number, PeT = R∗|u∗
core|/D∗
eff = z∗
D/R∗=
zD/R, in terms of the dimensionless mixing length.
The ratio of the molecular, Pe =
ρ∗|u∗
core|R∗/(k∗/c∗
p), to the turbulent P´eclet number Pe/PeT = ρ∗D∗
eff/(k∗/c∗
p) measures
the enhanced diﬀusion due to turbulence.
As anticipated, in the present case, the dimensionless mixing length z∗
D/R∗is evaluated
from the average density ﬁeld as the position of the intercept of the selected ρ-isoline (ρ∗=
.95ρ∗
core) with the jet axis. For the four cases we ﬁnd z∗
D(A) ≃7.4R∗, z∗
D(B) ≃7.9R∗,
z∗
D(C) ≃8.8R∗, z∗
D(D) ≃9.8R∗. Dimensional analysis provides a list of parameters upon
18


## Page 19


Mixing in Low-Mach number supercritical jets
Figure 7.
Real gas (Sim A) Instantaneous conﬁgurations of the near ﬁeld of axial momentum.
From left to right, consecutive instants of time with a time gap equal to 0.25 R∗/|u∗
R|. The arrows
highlight the evolution of a speciﬁc “ligament”.
which z∗
D/R∗may depend, namely
z∗
D
R∗= f
R∗
1
R∗, R∗
2
R∗
1
, ρ∗
core
ρ∗
c
, ρ∗
core
ρ∗
ext
, p∗
env
p∗
c
, ρ∗
core|u∗
core|
ρ∗
ext|u∗
ext| , Re, Pr

,
where the dependence on the turbulent intensity of the incoming inner stream is accounted
for through the Reynolds number.
In the cases we address, geometry, momentum ratio
ρ∗
core|u∗
core|/(ρ∗
ext|u∗
ext|), and Reynolds number are held ﬁxed. From the numerical results we
ﬁnd a weak dependence on the pressure ratio p∗
env/p∗
c, on the Prandtl number Pr, and on
injection density ρ∗
core/ρ∗
c that result in an almost constant z∗
D/R∗≃7 −8 for the three high
pressure cases and a little larger for the lowest pressure z∗
D/R∗≃9.8.
Let us now assume that one intends to simplify the system by modelling the high-pressure,
real gas injection with the perfect gas model for ﬁxed mass ﬂow rate, i.e. given ρ∗
core|u∗
core|,
and for the same injector geometry. Two alternative procedures can be reasonably conceived,
namely keeping the same injection density (ρ∗R
core = ρ∗P
core, with the superscript R and P de-
noting the real and the perfect gas case respectively) or, alternatively, the same temperature
(θ∗R
core = θ∗P
core). Since z∗
D/R∗is more or less constant, in the ﬁrst case (same density), where
|u∗
core|R = |u∗
core|P, the persistence time of the structures T ∗= z∗
D/|u∗
core| will be the same
for the real gas and for its perfect gas model. In the other case (same temperature), the
diﬀerent injection density ρ∗R
core > ρ∗P
core entails a diﬀerent injection speed resulting in a longer
persistence time for the real gas. We observe that, commonly, the injection temperatures
are the experimental control parameters, leading to an increased persistence of the real gas
coherent structures of density with respect to the perfect gas analogue.
The dynamics of ligaments formation is addressed in ﬁgure 7 by showing ﬁve successive
conﬁgurations of the jet near ﬁeld. Ligament formation, growth and evolution are clearly
visualized by the axial momentum isocontours (see the arrow used to highlight the same
structure in the successive stages of development). The wake of the ﬁnite thickness trailing
edge separating the inner from the outer stream, see the sketch in ﬁgure 1, gives rise to the
system of Kelvin-Helmholtz vortices apparent in ﬁgure 8. They force the internal, slow, and
dense gas towards the external, fast, and light stream. The extruded structures are conse-
quently elongated by the high velocity stream to form the ligaments. Panel (a) of ﬁgure 8
19


## Page 20


Mixing in Low-Mach number supercritical jets
(a)
(b)
Figure 8.
Magniﬁcation of the region characterized by the formation of ligaments in the last
instantaneous ﬁeld shown in the rightmost panel of ﬁgure 7. Panel (a): instantaneous density
ﬁeld with in-plane velocity vectors. Solid white lines denote three levels of passive scalar injected
through the external stream. Panel (b): passive scalar contour with the in-plane velocity vectors.
provides the instantaneous density ﬁeld on an axial plane, together with the in-plane velocity
vectors and three isolevels of a passive scalar injected in the external stream. The contour
plot of the passive scalar ﬁeld is superimposed to the in-plane velocity vectors in the panel
(b). The ligament formation is apparently correlated with the Kelvin-Helmholtz vortices,
highlighted by the velocity vectors and by the passive scalar isolines. The dense structures
protruding from the inner core contribute to slow down the external stream thereby blocking
the ﬂow and inducing additional radial motion. It is worthwhile stressing that the dynam-
ics of ligament formation is generic as long as a strong density and velocity contrast exists
between the two streams. Indeed, although ﬁgure 8 concerns the real gas simulation A,
a substantially identical phenomenology is found in all the other two cases with large in-
ner/outer density ratio (B, C). In the fourth case, D, persistent ligaments are not observed
and density structures are much less neatly deﬁned due to the small density contrast between
the streams.
The most signiﬁcant diﬀerence among the three high density ratio cases is found in the
small scale features of the jet, that turn out to be deeply inﬂuenced by the thermodynamic
behavior of the ﬂuid.
Figure 9 addresses the magnitude of the instantaneous temperature
gradients,
√
∇θ · ∇θ. A peculiar aspect is that the temperature gradients have substantially
the same order of magnitude for the two real gas cases (top and bottom panel in the left
column) and for the perfect gas case (top right panel), despite the temperature diﬀerence
between inner and outer jet is smaller for the former two cases than it is for the perfect gas
case. It follows that the scales at which the temperature gradients occur tend to be smaller in
supercritical conditions. In order to make the argument clear, let us consider a dimensional
estimate for the temperature gradients,
√
∇θ · ∇θ ∼∆Θ/ℓθ, where ∆Θ is the temperature
jump across the interface and ℓθ is the eﬀective thickness of the instantaneous thermal
interface between the high and low temperature regions. Our data show that ∆ΘA/ℓA
θ ≃
∆ΘB/ℓB
θ . Since ∆ΘA < ∆ΘB, it follows ℓA
θ < ℓB
θ , i.e. the thermal thickness for the real gas,
supercritical jet is smaller than for the perfect gas case. The statistical characterization of
this behavior will be provided in the following section.
20


## Page 21


Mixing in Low-Mach number supercritical jets
A
B
C
D
5
25
45
65
85
105
125
r/R
0.8
0.9
1
1.1
1.2
1.3
1.4
5
25
45
65
85
105
125
r/R
0.8
0.9
1
1.1
1.2
1.3
1.4
5
25
45
65
85
105
125
r/R
0.8
0.9
1
1.1
1.2
1.3
1.4
5
25
45
65
85
105
125
r/R
0.8
0.9
1
1.1
1.2
1.3
1.4
Figure 9.
Temperature gradient magnitude
√
∇θ · ∇θ ﬁeld. From left to right and from top to
bottom: real gas jet (Sim A), perfect gas jet (Sim B), real gas jet with the transport properties
of the perfect gas case (Sim C), perfect gas jet matching the temperature ratio of the real gas
case (Sim D). The bottom part of each panel report the radial proﬁles of the temperature gradient
magnitude at z=R (solid lines) and z=2R (dashed lines), in the ﬁeld contour the two axial stations
are highlighted with the red segments.
21


## Page 22


Mixing in Low-Mach number supercritical jets
According to eq. (29) where p(t) = const, the density gradients are associated with the
corresponding temperature gradients, ∇ρ = (∂ρ(θ, p)/∂θ) ∇θ. Here the real gas thermody-
namics makes the diﬀerence and the singularity near the critical point plays a role, since
∂ρ(θ, pc)/∂θ →∞for θ →θc, where we recall that pc and θc are the critical pressure and
temperature, respectively. This leads to a further intensiﬁcation of the density gradients
for the real gas near the critical point, with respect to the perfect gas case. Indeed, the
dimensional estimate for the density thickness of the interface, ℓρ ∼∆P/√∇ρ · ∇ρ, where
∆P is the density jump across the interface, is ℓρ ∼ℓθ(∆P/∆Θ)/ (∂ρ/∂θ) (here the symbol
P reads capital ρ). This expression shows that the density thickness becomes much thinner
than the thermal thickness where the gas gets close to the critical conditions. This behavior
of the density gradients can be appreciated in ﬁgure 10 that provides the isolevels of the
gradient intensity for two instantaneous conﬁgurations, corresponding to the real gas and
the perfect gas simulation, left and right panel, respectively. Close to the injection section,
the density interface is apparently much sharper for the conﬁguration reported on the left.
Increasing the distance from the exit, the persistent ﬁlamentary structures observed for this
case become less evident and weaker in the perfect gas case. Meanwhile, the mixing region
becomes increasingly convoluted by small scale, sharply contrasted details which are missing
instead at corresponding positions in the right panel. This behavior corresponds to increased
turbulent mixing with respect to the perfect gas case.
C.
Statistical analysis
The previous subsection dealt with the instantaneous conﬁgurations of the jets.
The
conclusions we reached are now better substantiated by quantitatively addressing the related
statistics. The statistical analysis is based on the same collection of about two hundred
instantaneous ﬁelds, separated in time by 0.25 R∗/|u∗
R|, used for the mean ﬁelds.
The panels in the left column of Figure 11 show the probability density function of
the radial component of the normalized density ﬂuctuation gradient, (∂ρ′/∂r)/∆P, with
ρ′ = ρ −⟨ρ⟩and ⟨ρ⟩the local mean density. As a matter of fact the density gradient is,
on average, almost aligned with the radial direction suggesting that the statistics of ∂ρ′/∂r
conveys most of the information on the structure of the instantaneous ﬁeld. The statistics
concerns the region extending two diameters downstream the inlet section (0 ≤z ≤4R)
and is conditioned to diﬀerent density ranges, namely 0.05 < Cρ < 0.95 (top panel), 0.75 <
Cρ < 0.95 (middle panel), 0.05 < Cρ < 0.75 (bottom panel), with Cρ = (ρ −ρext) /∆P the
density normalized such that Cρ = 0 in the external stream and Cρ = 1 in the core. The
panels in the right column of Figure 11 refer to the radial component of the temperature
ﬂuctuation gradient, ∂θ′/∂r/∆Θ, with θ′ = θ −⟨θ⟩the temperature ﬂuctuation with respect
to the mean one ⟨θ⟩and ∆Θ = θcore −θext. Conditioning to density is indeed instrumental
to focus the analysis on the instantaneous interface between high density inner core and low
density outer stream. This is the region of the phase space where well deﬁned ligaments
tend to be formed, see Figure 10. In the three cases (A, real gas; B, perfect gas; C, real gas
with artiﬁcial transport properties) the pdf f(∂ρ′/∂r/∆P|0.05 ≤Cρ ≤0.95, 0 ≤z ≤4R) is
signiﬁcantly skewed towards the negative tail, see top panel on the left and the related inset
22


## Page 23


Mixing in Low-Mach number supercritical jets
1
3
5
7
9
11
r/R
0.7
0.8
0.9
1
1.1
1.2
A
B
1
3
5
7
9
11
13
15
17
19
21
23
r/R
0.7
0.8
0.9
1
1.1
1.2
Figure 10.
Instantaneous density gradient ﬁelds of real gas jet (Sim A) (left top panel) and perfect
gas jet (Sim B) (right top panel). The ﬁeld of simulation C is similar to the simulation A while the
density gradients of simulation D are negligible respect to the showed one, since they are omitted.
In the bottom panels the radial proﬁles of the density gradient magnitude at z=R (solid lines) and
z=2R (dashed lines) are reported, In the top panels the two axial stations are highlighted with the
red segments.
showing the pdf in logarithmic and linear scale, respectively. The real gas cases show longer
tails indicating large intensity events comparatively more frequent than in the perfect gas
case. This behavior is quantiﬁed by the normalized even moments of the pdf, the so-called
23


## Page 24


Mixing in Low-Mach number supercritical jets
10−3
10−2
10−1
−20
−15
−10
−5
0
5
10
15
pdf( (∂ρ/∂r)/∆ Ρ|0.05 <Cρ< 0.95)
(∂ρ/∂r)/∆ Ρ
0
0.1
0.2
−20 −10
0
10
0
0.1
0.2
−20 −10
0
10
0
0.1
0.2
−20 −10
0
10
10−3
10−2
10−1
100
−10
−5
0
5
10
15
pdf( (∂θ/∂r)/∆Θ |0.05 <Cρ< 0.95)
(∂θ/∂r)/∆Θ
0
0.1
0.2
0.3
0.4
−10
0
10
0
0.1
0.2
0.3
0.4
−10
0
10
0
0.1
0.2
0.3
0.4
−10
0
10
10−3
10−2
10−1
−20
−15
−10
−5
0
5
10
15
pdf( (∂ρ/∂r)/∆ Ρ|0.75 <Cρ< 0.95)
(∂ρ/∂r)/∆ Ρ
Perfect
Real Pr=0.6
Real Pr=0.35
10−3
10−2
10−1
100
−10
−5
0
5
10
15
pdf( (∂θ/∂r)/∆Θ |0.75 <Cρ< 0.95)
(∂θ/∂r)/∆Θ
10−3
10−2
10−1
−20
−15
−10
−5
0
5
10
15
pdf( (∂ρ/∂r)/∆ Ρ|0.05 <Cρ< 0.75)
(∂ρ/∂r)/∆ Ρ
Perfect
Real Pr=0.6
Real Pr=0.35
10−3
10−2
10−1
100
−10
−5
0
5
10
15
pdf( (∂θ/∂r)/∆Θ |0.05 <Cρ< 0.75)
(∂θ/∂r)/∆Θ
(a)
(b)
(c)
(d)
(e)
(f)
Figure 11.
Probability density function of the radial component of the density gradient ﬂuctuation
∂ρ′/∂r/∆P (left column, panels a,c,e), and of the temperature gradient ﬂuctuation ∂θ′/∂r/∆Θ
(right column, panels b,d,f). ∆P = ρcore −ρext and ∆Θ = θcore −θext are respectively the density
and temperature diﬀerence between jet core and external environment. The statistics concerns
the region extending two diameters downstream the inlet section 0 < z < 4R and is conditioned
to diﬀerent ranges of the density, namely 0.05 < Cρ < 0.95 (top; panels a,b), 0.75 < Cρ < 0.95
(middle; panels c,d) and 0.05 < Cρ < 0.75 (bottom; panels e,f), where Cρ = (ρ −ρext) /∆P is the
normalized density ranging from Cρ = 0 in the external environment to Cρ = 1 in the jet core.
hyper-ﬂatness factors of order n
F2n[∂ρ′/∂r] = ⟨(∂ρ′/∂r)2n⟩
⟨(∂ρ′/∂r)2⟩n
F2n[∂θ′/∂r] = ⟨(∂θ′/∂r)2n⟩
⟨(∂θ′/∂r)2⟩n ,
(39)
see the data reported in Table II. Values of the hyper-ﬂatness exceeding the reference values
for a Gaussian distribution, F G
2n = 3, 15, 105 for n = 2, 3, 4, signal the existence of an
24


## Page 25


Mixing in Low-Mach number supercritical jets
n=2 n=3
n=4
sim. A
7.2 110. 2327.
sim. B
6.4
91. 1930.
sim. C
5.1
49.
624.
Gauss
3.0
15.
105.
n=2 n=3
n=4
sim. A
9.0 172. 4464.
sim. B
8.1 134. 2990.
sim. C
6.0
72. 1151.
Gauss
3.0
15.
105.
Table II. Hyper-ﬂatness, F2n [∂·′ /∂r], of the probability distribution reported in the top panels
of ﬁgure 11.
Left table: radial component of density gradient ﬂuctuations; right table: radial
component of temperature gradient ﬂuctuations.
intermittent behavior, where phases of relatively weak gradients are alternated with the
presence of relatively rare but intense events. In our system the origin of the intermittency
is related to the ligaments that invade regions of relatively smooth density variation.
Given the relationship between temperature and density gradients, ∂θ′/∂r = (∂θ/∂ρ) ∂ρ′/∂r,
the overall shape of the temperature pdf is grossly speaking specular with respect to that of
density since ∂θ/∂ρ < 0. Interestingly, the three temperature gradient pdfs for the two real
gas and the perfect gas case are substantially identical, conﬁrming the impression gained
from inspecting the instantaneous ﬁeld, see Figure 9.
We stress that conditioning with
respect to density is used in the two top panels at the only purpose of removing from the
analysis the events of vanishing gradients occurring in the external region and in the inner
jet core that would otherwise outnumber the comparatively less numerous events belonging
to the physically signiﬁcant interface between inner and outer stream.
In order to focus on the large density features, the middle panels of Figure 11 show the
ﬂuctuation gradient pdf conditioned to the high density range 0.75 < Cρ < 0.95. It is ap-
parent that the origin of the intermittent behavior of the density gradients (left panel) is
mostly related to features associated with large density. The pdf shows exponential tails
which are deﬁnitely longer in the two real gas cases. Conversely, the temperature gradients
conditioned to the same density range (right panel) are characterized by a comparatively
narrower distribution, indicating that the structures which support the density gradients
have almost deterministic temperature gradients, ∂θ/∂r ≃∂⟨θ⟩/∂r, as follows from observ-
ing that ∂θ′/∂r ≃0. Considered that ∂⟨θ⟩/∂r = ⟨∂θ/∂ρ ∂ρ/∂r⟩, since ∂ρ/∂θ is large for the
near critical gas, it follows that the high density features supporting the density gradients
are almost isothermal in the real gas cases.
The bottom panels of Figure 11 concern the complementary density range 0.05 < Cρ <
0.75. Apparently the most signiﬁcant ﬂuctuations of the temperature gradient (left panel)
occur in this region of the phase space. The intermittency of the temperature gradient is
signiﬁcant, implying that, locally, a large temperature diﬀerence occurs, with relatively low
temperature regions getting close to high temperature ones. Clearly, this induces strong
density gradients, giving reason of the non-negligible density-gradient intermittency found
also in this complementary density range.
The density gradient is strictly related to the thickness of the interface between the high-
density core and the low-density external stream. Indeed the high density gradients that
characterize the real gas jets suggest that the interface is thinner for the real gas than for the
25


## Page 26


Mixing in Low-Mach number supercritical jets
(a)
(b)
(c)
Figure 12.
Joint probability density function, f(δρ, Cρ), of density interface thickness δρ =
∆P/ |∇ρ| and normalized density Cρ, in the region one diameter downstream the jet inlet. From
left to right: real gas jet (panel a), perfect gas jet (panel b) and real gas jet with perfect gas
transport features (panel c).
perfect gas. The interface thickness can be estimated as the inverse of the normalized density
gradient module δρ = ∆P/ |∇ρ|. Figure 12 provides the joint probability density function,
f(δρ, Cρ), of interface thickness δρ and normalized density Cρ, where the real gas case A is
reported on the panel (a), the perfect gas case B in the panel (b), and the real gas case
with perfect gas transport coeﬃcients C in the panel (c). The statistics concern the same
region of the ﬂow domain already considered in the pdfs of ﬁgure 11 and are conditioned to
a density interval ranging from Cρ = 0.9 to Cρ = 0.1.
In order to understand the diﬀerent roles played by the equation of state and by the
transport coeﬃcients it is worth ﬁrst comparing real and perfect gas cases with identical
transport coeﬃcients, cases B and C reported in the middle and right-most panel of the ﬁg-
ure, respectively. Apparently as the density increases (Cρ), the interface thickness decreases
for both cases. In comparison with the perfect gas case, at given normalized density, the
pdf of the interface thickness is much more peaked at small values for the reals gas case. A
further feature to be noted is that, at large density, the peak of the pdf moves toward slightly
larger scales for the perfect gas case, implying an increased diﬀusion of high density features.
On the contrary the pdf peak remains centered on the smallest scales for the real gas. This
behavior is explained by looking at the isobars in the density-temperature diagram provided
in ﬁgure 2. The injection states for cases B and C are denoted with the squares and the
asterisks, respectively, reported on the same isobar (green curve). Apparently, huge density
diﬀerence take place at almost constant temperature for case C (real gas), see also the inset
with the isobars plotted in linear scale. On the contrary for case B density changes are
almost uniformly distributed along the temperature range. Since diﬀusion eﬀects are deter-
mined by the temperature ﬁeld, eq. (38), it follows that density structures are more diﬀusive
for case B, where they are always associated with signiﬁcant temperature diﬀerences. The
comparatively smaller diﬀusion taking place in the real gas explains the statistically smaller
interface thickness observed in the scatter plots shown in the panel (c) of ﬁgure 12 in com-
parison with that shown in the panel (b). The eﬀect is observed at all values of density a
part from the smallest range farther from the critical condition, where the isobar gets closer
to the behavior of the perfect gas.
26


## Page 27


Mixing in Low-Mach number supercritical jets
When recovering the actual transport coeﬃcients of the real gas (case A), panel (a) of
ﬁgure 12, the typical scales of the density gradients increase signiﬁcantly with respect to the
artiﬁcial case C (real gas with perfect gas transport coeﬃcients). The eﬀect is qualitatively
explained by comparing the behavior of the thermal diﬀusivity λ for the real gas shown in
the right panel of ﬁgure 3, see Appendix B, with the Sutherland law shown as a dashed
line in the same ﬁgure. Clearly the diﬀusivity is enhanced, hence the increased scale for the
density gradients.
In conclusion, the coherent structures of high density observed as a consequence of the
high density and momentum contrast between inner and outer stream are characterized by
a sharp interface of separation with the background low density environment. The instan-
taneous interface is extremely sharp for the real gas (Van der Waals equation of state),
although it is partially smeared by the increased thermal diﬀusivity occurring near the criti-
cal point. Such features of coherent density and their sharp interface are responsible for the
highly intermittent statistical behavior observed for the density gradients.
VI.
FINAL REMARKS
The low Mach number asymptotic expansion of the Navier-Stokes equations, originally
derived by Majda & Sethian for perfect gas ﬂows in reactive conditions, was here extended to
a generic real gas equation of state to deal with ﬂuids in near critical conditions. The resulting
formulation allowed the detailed analysis of the turbulent mixing of slightly supercritical
ﬂuids at vanishing Mach number through accurate and eﬃcient Direct Numerical Simulations
of a coaxial jet of a single component Van der Waals ﬂuid.
When slightly supercritical
streams are mixed at large Reynolds number, turbulence and real-gas eﬀects combine and
have been shown to produce peculiar eﬀects.
Elongated ﬁnger-like structures, the so-called “ligaments”, similar to those classically ob-
served in the break-up of liquid jets, are found in the simulations. These structures have
been well documented also in supercritical injection experiments and numerical simulation
at moderately high Mach number and diﬀer from those characterizing liquid jets which even-
tually break up in droplets. The supercritical ligaments, once formed, diﬀuse to eventually
disappear altogether.
The ligaments are originated by the joint eﬀect of a high density
contrast between inner and outer stream in combination with the strong shear layer gen-
erated at the interface between the slower inner jet and the outer faster stream. The high
velocity ratio of the shear layer promotes the formation of the classical Kelvin-Helmholtz
instability with rolling vortices. Finger-shaped high density protrusions are extruded by
these vortices in the low density high speed stream where they are elongated well inside the
external environment thereby generating the ligaments. It is worth emphasizing that this
mechanism operates in all the cases where a high density contrast exists, irrespective of the
thermodynamic model. The main diﬀerence between Van der Waals and perfect gas jets
mostly resides in the small-scale features of the ligaments. In comparison with the perfect
gas model, the dense gas case shows much steeper density gradients and a thinner interface
between the high- and low-density streams. Instead temperature gradients behave much
more similarly in the two cases, despite the fact that the bulk temperature diﬀerences are
27


## Page 28


Mixing in Low-Mach number supercritical jets
smaller in the dense gas case, for given density contrast. In other words, turbulent mixing
in dense gases is associated with smaller scales than in perfect gases in order to balance the
smaller temperature jump occurring at near critical conditions for given density contrast
between the mixing streams. The steep density gradients near the critical point are indeed
associated with the critical point singularity that controls the spatial scales of the density
variations.
The statistical signature of this phenomenology is found in the intermittency of the den-
sity ﬁeld, as evaluated by the hyper-ﬂatness of the density gradient pdf. Indeed the increased
intermittency in real gas mixing is related to the occurrence of the mentioned ligamentary
structures characterized by an extremely sharp interface separating high and low density
streams. The picture is reinforced after looking at the large density gradient ﬂuctuations
that take place in correlation with high density regions, thermodynamically closer to the
critical state. Typically, the ligaments are almost isothermal structures with small temper-
ature diﬀerences with the local environment. This behavior is understood after considering
that ﬂuid particles at near critical conditions may assume signiﬁcantly diﬀerent densities
with almost identical temperatures as a consequence of the aforementioned critical point
singularity. Overall, the much smaller local interface thickness for the near critical gas may
have signiﬁcant consequences for the numerical simulation of this kind of ﬂows.
As a ﬁnal remark, we like to stress that the features that have been observed in connection
with the Wan der Waals model for the gas are expected to hold also for other thermodynamic
model of dense gases (e.g. the Peng-Robinson model), that in certain cases may provide a
better description of a real gas.
The intermittent behavior promoted by the ligaments in combination with the sharp
interface separating high and low density regions is a crucial feature to be modeled in view
of increasing the predictive performances of coarse-grained descriptions like Large-Eddy-
Simulation.
The formulation here introduced could indeed represent a solid framework
to develop appropriate sub-grid models to deal with turbulent diﬀusion processes in high-
Reynolds-number technological applications involving supercritical ﬂuids.
ACKNOWLEDGEMENTS
The authors acknowledge the CASPUR High Performance Computing Centre for the
computational resources provided via std10-284 grant.
Appendix A: Van der Waals and Peng-Robinson equation of state
Thermal properties of polyatomic gases are aﬀected by quantum eﬀects that emerge
already at ordinary thermodynamic conditions. In addition, when the density is suﬃciently
high, molecule-molecule interaction become signiﬁcant giving rise to the so-called real-gas
eﬀects. All this information is gathered in the expression for the Helmholtz free-energy as a
function of temperature, volume and molecule number.
28


## Page 29


Mixing in Low-Mach number supercritical jets
1.
The Van der Waals model
The simplest model endowed with all these features is a diatomic Van der Waals
gas, whose Helmholtz free energy f can be derived from quantum statistical mechanics
considerations26,
f = Rnθ ln
"
 1 −e−τ
θ 
C(n) (V −b) θ5/2
#
−a
V + Rnτ
2
(A1)
where C(n) = 8π2nιR5/2√
2πm/

ℏ5N 3/2
A

with ι and m the moment of inertia and the mass
of the molecule, R the universal gas constant, ℏ= h/(2π) with h the Planck’s constant, NA
the Avogadro’s number, n = N/NA the number of moles, N the number of gas molecules, τ =
ℏζNA/R where ζ is the fundamental vibrational frequency of the molecule. In the expression
for the free-energy two additional constant appear, a and b related to the intermolecular
forces and to the excluded volume, respectively.
The pressure equation of state follows as
p = −∂f
∂V

θ,N
= Rmθρ
1 −b′ρ −a′ρ2 ,
(A2)
where a′ = a/(nW)2 and b′ = b/(nW) with W the molar mass respectively, and Rm = R/W.
The entropy is
S = −∂f
∂θ

V,N
= 5
2Rn (ln θ + 1) + Rn ln
"
C(n) (V −b)
 1 −e−τ
θ 
#
+
Rnτ
(eτ/θ −1) θ ,
(A3)
which yields the internal energy
U = F + θS = 5
2Rnθ −a
V + Rnτ
1
2 −
1
eτ/θ −1

.
(A4)
Hence the heat capacity at constant pressure and volume can be calculated from the entropy
by means the known thermodynamic relations,
cv = θ ∂S
∂θ

V,N
= 5
2Rn + Rn
τ 2
(eτ/θ −1)2 θ2
(A5)
cp = cv + θ ∂p
∂θ

V,N
∂V
∂θ

p,N
= cv + θ
R2n2
(V −b) (p −a/V 2 + 2ba/V 3) .
(A6)
The ideal gas is recovered by setting a = b = 0, with τ = 0 recovering constant, temperature-
independent thermal properties. Relations (A2), (A5) and (A6) can be re-expressed as
p = Rmθρ
1 −b′ρ −a′ρ2 ,
(A7)
c′
v = cv
nW = 5
2Rm + Rm
τ 2
(eτ/θ −1)2 θ2 ,
(A8)
c′
p = cp
nW = c′
v + Rm
Rmρθ
(1 −b′ρ) (p −a′ρ2 + 2b′a′ρ3) ,
(A9)
where c′
v = cv/(nW) and c′
p = cp/(nW) are the heat capacity coeﬃcients per mass unit.
29


## Page 30


Mixing in Low-Mach number supercritical jets
2.
The Peng-Robison model
In many circumstances the Van der Waals model is not suﬀuciently accurate, and should
be substituted by alternative thermodynamic models. As an example, the pressure equation
for the Peng-Robinson model,24, reads
p = kBNθ
V −b −
aα(θ)
V + 2 b V −b2 ,
(A10)
where V is the volume and a, b and α(θ) can be expressed as a function of the critical
thermodynamic variables and of what is called the acentric factor ω,
a = 0.457235N 2k2
Bθ2
c
pc
b = 0.077796NkBθc
pc
α =

1 + κ
 1 −θ0.5
R
2 ,
with θR = θ/θc and κ = 0.37464 + 1.54226 ω −0.26992 ω2. Considering the relation p =
−(∂f/∂V )θ,N, the Helmholtz free-energy f associated with the equation of state (A10) is
obtained by straightforward integration,
f = −kBθ ln Z = −kBθN
Z
1
V −bdV + a α(θ)
Z
1
V + 2 b V −b2dV + A(θ, N) ,
(A11)
where A(θ, N) is the integration constant which depends only on temperature and particle
number. The result is
f = −kBθN ln |V −b| + aα(θ)
2
√
2 b ln

V −
 √
2 −1

b
V +
 √
2 + 1

b
 + A(θ, N) .
(A12)
The integration constant A(θ, N) may be evaluated considering that in the limit V →∞
for ﬁxed temperature and particle number both the Peng-Robinson and the Van der Waals
models should approach the same limit. In other words, in the limit, equations (A1) and
(A12) must eventually coincide, providing by comparison the expression for A
A(θ, N) = −5
2kBθN ln θ + kBN τ
2 + kBθN ln
 1 −e−τ
θ 
−kBθN ln
 8
ℏ5π2Nιk5/2
B
√
2πm

.
Once A is found, all the relevant thermodynamic quantities are accessible from the Helmholtz
free-energy that reads
f =Rnθ ln |V −b| −aα(θ)
2
√
2 b ln

V −
 √
2 −1

b
V +
 √
2 + 1

b

+5
2Rnθ ln θ −Rnτ
2 −Rnθ ln
 1 −e−τ
θ 
+ Rnθ ln
 8
ℏ5π2Nιk5/2
B
√
2πm

.
(A13)
30


## Page 31


Mixing in Low-Mach number supercritical jets
i
bi
0
0.431
1 −0.4623
2 0.08406
3 0.005341
4 −0.00331
Table III. Fitting coeﬃcients of the Collision integral for the dilute gas viscosity provided in33.
i
Ni
ti
di li γi
1
10.72
0.1
2 0 0
2 0.03989 0.25 10 1 1
3 0.001208 3.2 12 1 1
4 −7.402
0.9
2 2 1
5
4.620
0.3
1 3 1
Table IV. Coeﬃcients and exponent of the residual viscosity equation.
Appendix B: Transport coeﬃcients.
The dynamic viscosity and thermal conductivity are evaluated, see Ref 33, considering the
dilute gas contribution, µ0 and k0, the residual ﬂuid contribution, µr and kr, and the critical
state contribution, kc. The critical state enhancement can be neglected for the dynamic
viscosity.
For the viscosity the dilute gas contribution is given by
µ0(θ) = 0.0266958
√
Wθ
σ2Ω(¯θ)
,
(B1)
where σ is the Lennard-Jones size parameter equal to σ = 0.3656 nm for the Nitrogen. Ωis
the collisional integral
Ω(¯θ) = exp
 
4
X
i=0
bi

ln(¯θ)
i
!
,
(B2)
where ¯θ = θ/(ε/k) and ε/k is the Lennard-Jones energy parameter equal to ε/k = 98.94K
for the Nitrogen. bi are ﬁtting coeﬃcient provided in Ref 33, and are reported in table III.
The residual contribution to the dynamic viscosity yields
µr(τ, δ) =
n
X
i=1
Niτ tiδdi exp
 −γiδli
,
(B3)
where τ and δ are the ratios τ = θc/θ and δ = ρ/ρc, respectively, while the coeﬃcients Ni,
ti, di, li and γi are reported in table IV. The dynamic viscosity is obtained by the sum of the
two contribution obtaning the viscosity in µPa · s. The model for the thermal conductivity,
31


## Page 32


Mixing in Low-Mach number supercritical jets
espressed in mW/(m · K), is composed of three contribution. The ﬁrst one is the dilute gas
contribution,
k0 = N1
 µ0(θ)
1µPa · s

+ N2τ t2 + N3τ t3 .
(B4)
The second contribution to the thermal conductivity equation is the residual one,
kr =
n
X
i=4
Niτ tiδdiexp
 −γiδli
.
(B5)
The third contribution dealing with the critical state correction reads
kc = ρcp
kBR0θ
6πξµ(θ, ρ)

˜Ω−˜Ω0

(B6)
where
˜Ω= 2
π
cp −cv
cp

tan−1
 ξ
qD

+
cv
cp
  ξ
qD

(B7)
˜Ω0 = 2
π

1 −exp

−1
(ξ/qD)−1 + (ξ/qD)2/3(ρc/ρ)2

(B8)
ξ = ξ0
 ˜χ(θ, ρ) −˜χ(θref, ρ)θref/θ
Γ
ν/γ
(B9)
˜χ(θ, ρ) = pcρ
ρ2
c
∂ρ
∂p

θ
.
(B10)
The coeﬃcient and exponents of these equations are summarized in table V, while the other
relevant parameters are the Boltzmann’s constant kB = 1.380658 · 10−23J/K, the constants
R0 = 1.01, ν = 0.63 and γ = 1.2415. Finally a few other constants depend on the speciﬁc
gas and data ﬁtting on Nitrogen yields qD = 0.4nm, ξ0 = 0.17nm and Γ = 0.055. The
reference temperature θref is twice the critical temperature, and, in addition, kc should be
set to zero when the term in the bracket of equation (B9) is negative.
Appendix C: Thermal form of energy equation for a general EOS
For the reader’s convenience, the calculations needed to obtain the temperature equation
for a generic equation of state, eq. (20), are here explicitly reported. The diﬀerential of the
internal energy as a function of temperature θ∗and density ρ∗, u∗= u(θ∗, ρ∗), is,
du∗= ∂u∗
∂θ∗

ρ∗
dθ∗+ ∂u∗
∂ρ∗

θ∗
dρ∗= c∗
vdθ∗+ ∂u∗
∂ρ∗

θ∗
dρ∗,
(C1)
32


## Page 33


Mixing in Low-Mach number supercritical jets
i
Ni
ti
di li γi
1
1.511
2
2.117
−1.0
3 −3.332 −0.7
4
8.862
0.0
1 0 0
5
31.11
0.03 2 0 0
6 −73.13
0.2
3 1 1
7
20.03
0.8
4 2 1
8 −0.7096 0.6
8 2 1
9 0.2672
1.9 10 2 1
Table V. Coeﬃcients and exponents of the residual thermal conductivity equation.
with c∗
v = ∂u∗/∂θ∗|v∗= ∂u∗/∂θ∗|ρ∗and v∗= 1/ρ∗the speciﬁc volume. Since dρ∗= ρ∗2dv∗,
it follows
∂u∗
∂ρ∗

θ∗
dρ∗= −1
ρ∗2
∂u∗
∂v∗

θ∗
dρ∗.
(C2)
Combining equations (C2) and (C1), the material derivative of the internal energy follows
as
Du∗
Dt∗= c∗
v
Dθ∗
Dt∗−1
ρ∗2
∂u∗
∂v∗

θ∗
Dρ∗
Dt∗,
(C3)
which, using the continuity equation, 1/ρ∗Dρ∗/Dt = −∇∗· u∗, becomes
Du∗
Dt∗= c∗
v
Dθ∗
Dt∗+ 1
ρ∗
∂u∗
∂v∗

θ∗
∇∗· u∗= c∗
v
Dθ∗
Dt∗+ v∗∂u∗
∂v∗

θ∗
∇∗· u∗.
(C4)
Inserting eq. (C4) in the internal energy equation (3) leads to
ρ∗c∗
v
Dθ∗
Dt∗= −

p∗+ ∂u∗
∂v∗

θ∗

∇∗· u∗+ Σ∗: ∇∗u∗+ ∇∗· (k∗∇∗θ∗) .
(C5)
The ﬁrst term on the right hand side of this equation can be rearranged starting from the
fundamental thermodynamic relation du∗= θ∗ds∗−p∗dv∗, where the speciﬁc entropy can
be expressed as a function of temperature and speciﬁc volume s∗= s(θ∗, v∗),
du∗= θ∗
 ∂s∗
∂θ∗

v∗
dθ∗+ ∂s∗
∂v∗

θ∗
dv∗

−p∗dv∗
(C6)
=

−p∗+ θ∗∂s∗
∂v∗

θ∗

dv∗+ θ∗∂s∗
∂θ∗

v∗
dθ∗.
(C7)
Since the speciﬁc entropy −s∗is the ﬁrst derivative of the Helmholtz speciﬁc free energy f ∗
with respect to the temperature, one of the Maxwell’s relations yieds
∂s∗
∂v∗

θ∗
= −
∂2f ∗
∂θ∗|v∗∂v∗|θ∗= ∂p∗
∂θ∗

v∗
(C8)
33


## Page 34


Mixing in Low-Mach number supercritical jets
where p∗= −∂f ∗/∂v∗|θ∗. Merging equations (C7) and (C8), brings to the general identity
∂u∗
∂v∗

θ∗
= −p∗+ θ∗∂s∗
∂v∗

θ∗
= −p∗+ θ∗∂p∗
∂θ∗

v∗
.
(C9)
Inserting the above expression in the speciﬁc energy equation (C5), yields the required
equation for the temperature ﬁeld,
ρ∗c∗
v
Dθ∗
Dt∗= −θ∗∂p∗
∂θ∗

v∗
∇∗· u∗+ Σ∗: ∇∗u∗+ ∇∗· (k∗∇∗θ∗)
(C10)
which is indeed the dimensional counterpart of the dimensionless equation reported in the
main text as eq. (10).
REFERENCES
1M.V. Palmer and S.S.T. Ting, “Applications for supercritical ﬂuid technology in food
processing,” Food chemistry 52, 345–352 (1995).
2M. Perrut,“Supercritical ﬂuid applications: Industrial developments and economic issues,”
Industrial & engineering chemistry research 39, 4531–4535 (2000).
3J. Fages, H. Lochard, J.J. Letourneau, M. Sauceau, and E. Rodier, “Particle generation
for pharmaceutical applications using supercritical ﬂuid technology,” Powder Technology
141, 219–226 (2004).
4G. Brunner, “Applications of supercritical ﬂuids,” Annual Review of Chemical and
Biomolecular Engineering 1, 321–342 (2010).
5L. Cheng, G. Ribatski, and J.R. Thome, “Analysis of supercritical CO2 cooling in macro-
and micro-channels,” International Journal of Refrigeration 31, 1301–1316 (Dec. 2008),
ISSN 01407007.
6A. Checinska, I.A. Fruth, T.L. Green, R.L. Crawford, and A.J. Paszczynski, “Steriliza-
tion of biological pathogens using supercritical ﬂuid carbon dioxide containing water and
hydrogen peroxide,” Journal of microbiological methods 87, 70–75 (2011).
7G.L. Weibel and C.K. Ober,“An overview of supercritical co< sub> 2</sub> applications
in microelectronics processing,” Microelectronic Engineering 65, 145–152 (2003).
8J.W. King and G.R. List, Supercritical ﬂuid technology in oil and lipid chemistry (The
American Oil Chemists Society, 1996).
9J.A. Mendiola, M. Herrero, M. Castro-Puyana, and E. Ib´a˜nez, “Supercritical ﬂuid extrac-
tion,” Natural Product Extraction: Principles and Applications 21, 196 (2013).
10B. Chehroudi, D. Talley, and E. Coy, “Visual characteristics and initial growth rates of
round cryogenic jets at subcritical and supercritical pressures,” Physics of Fluids 14, 850
(2002).
11C. Segal and S. a. Polikhov, “Subcritical to supercritical mixing,” Physics of Fluids 20,
052101 (2008), ISSN 10706631.
12A. Roy, C. Joly, and C. Segal, “Disintegrating supercritical jets in a subcritical environ-
ment,” Journal of Fluid Mechanics 717, 193–202 (Feb. 2013), ISSN 0022-1120.
34


## Page 35


Mixing in Low-Mach number supercritical jets
13W. Mayer, J. Telaar, R. Braham, G. Schneider, and J. Hussong, “Raman measurements of
cryogenic injection at supercritical pressure,” Heat and Mass Transfer 39, 709 (2003).
14W. Mayer, A. Schik, C. Schweitzer, and M. Schaﬄer, “Injection and mixing pro-
cesses in high pressure lox/gh2 rocket combustors, aiaa paper no. 96-2620,” in 32nd
AIAA/ASME/SAE/ASEE Joint Propulsion Conference & Exhibit, Lake Buena Vista,
Florida (–, 1996).
15J. Bellan, “Supercritical (and subcritical) ﬂuid behavior and modeling: drops, streams,
shear and mixing layers, jets and sprays,” Progress in energy and combustion science 26,
329–366 (2000).
16N. Zong and V. Yang, “Cryogenic ﬂuid jets and mixing layers in transcritical and su-
percritical environments,” Combustion science and technology 178, 193–228 (2006), ISSN
0010-2202.
17R.S. Miller, K.G. Harstad, and J. Bellan, “Direct numerical simulations of supercritical
ﬂuid mixing layers applied to heptane-nitrogen,” Journal of Fluid Mechanics 436, 1–39
(2001).
18N. A. Okong’o and J. Bellan, “Direct numerical simulation of a transitional supercritical
binary mixing layer: heptane and nitrogen,” Journal of Fluid Mechanics 464, 1–34 (2002).
19N. Okong’o and J. Bellan, “Real-gas eﬀects on mean ﬂow and temporal stability of binary-
species mixing layers,” AIAA journal 41, 2429–2443 (2003).
20J.C. Oefelein, “LES of supercritical LOX-H 2 injection and combustion in a shear-coaxial
uni-element rocket,” in 41 st AIAA Aerospace Sciences Meeting & Exhibit, (Reno, NV),
0479 (2003).
21A. Capuzzo, M.E. Maﬀei, and A. Occhipinti,“Supercritical ﬂuid extraction of plant ﬂavors
and fragrances,” Molecules 18, 7194–7238 (2013).
22A. Majda and J. Sethian, “The derivation and numerical solution of the equations for zero
mach number combustion,” Combustion science and technology 42, 185–205 (1985).
23G. Volpe, “Performance of compressible ﬂow codes at low mach numbers,” AIAA journal
31, 49–56 (1993).
24D.Y. Peng and D.B. Robinson, “A new two-constant equation of state,” Industrial & En-
gineering Chemistry Fundamentals 15, 59–64 (1976).
25C.K. Law, Combustion physics (Cambridge Univ Pr, 2006).
26Y. Zhu, Large-scale inhomogeneous thermodynamics: and application for atmospheric en-
ergetics (Cambridge International Science Publishi, 2003).
27I. Orlanski, “A simple boundary condition for unbounded hyperbolic ﬂows,” Journal of
computational physics 21, 251–269 (1976).
28F. Picano and CM Casciola, “Small-scale isotropy and universality of axisymmetric jets,”
Physics of Fluids 19, 118106 (2007).
29F. Picano, G. Sardina, P. Gualtieri, and CM Casciola, “Anomalous memory eﬀects on
transport of inertial particles in turbulent jets,” Physics of Fluids 22, 051705 (2010).
30F. Picano, F. Battista, G. Troiani, and CM Casciola, “Dynamics of piv seeding particles
in turbulent premixed ﬂames,” Experiments in Fluids 50, 75–88 (2011).
31F. Battista, F. Picano, G. Troiani, and C.M. Casciola, “Intermittent features of inertial
particle distributions in turbulent premixed ﬂames,” Physics of Fluids 23, 123304 (2011).
35


## Page 36


Mixing in Low-Mach number supercritical jets
32T. Schmitt, J. Rodriguez, IA Leyva, and S. Candel,“Experiments and numerical simulation
of mixing under supercritical conditions,” Physics of Fluids 24, 055104–055104 (2012).
33E.W. Lemmon and R.T. Jacobsen, “Viscosity and thermal conductivity equations for ni-
trogen, oxygen, argon, and air,” International journal of thermophysics 25, 21–69 (2004).
34B. Chehroudi, D. Talley, W. Mayer, R. Branam, JJ Smith, A. Schik, and M. Oschwald,
“Injection of ﬂuids into supercritical environments, invited review paper, special volume
dedicated to supercritical ﬂuids,”Combustion Science and Technology 178, 49–100 (2006).
35J. Eggers and E. Villermaux, “Physics of liquid jets,” Reports on progress in physics 71,
036601 (2008).
36R.S. Miller and J. Bellan,“Direct numerical simulation of a conﬁned three-dimensional gas
mixing layer with one evaporating hydrocarbon-droplet-laden stream,” Journal of Fluid
Mechanics 384, 293–338 (1999).
37R.W. Shaw and E.U. Franck, “Supercritical water: A medium for chemistry,” Chem. Eng.
News 69, 26–39 (1991).
38R.L. Mendes, B.P. Nobre, M.T. Cardoso, A.P. Pereira, and A.F. Palavra, “Supercritical
carbon dioxide extraction of compounds with pharmaceutical importance from microalgae,”
Inorganica Chimica Acta 356, 328–334 (2003).
36

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1404_0481v2_turbulent_mixing_of_a_slightly_supercritical_van_der_waals_fluid_at_low_mach_num
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2014/1404_0481V2_TURBULENT_MIXING_OF_A_SLIGHTLY_SUPERCRITICAL_VAN_DER_WAALS_FLUID_AT_LOW_MACH_NUM.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

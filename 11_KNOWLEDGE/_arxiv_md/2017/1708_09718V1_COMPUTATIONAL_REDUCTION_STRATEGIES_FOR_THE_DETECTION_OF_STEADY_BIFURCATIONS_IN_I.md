---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1708.09718v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1708.09718v1_Computational_reduction_strategies_for_the_detection_of_steady_bifurcations_in_i

> Source: 1708.09718v1_Computational_reduction_strategies_for_the_detection_of_steady_bifurcations_in_i.pdf

> Pages: 31

---


## Page 1


Computational reduction strategies for the detection of
steady bifurcations in incompressible ﬂuid-dynamics:
applications to Coanda eﬀect in cardiology
Giuseppe Pitton1, Annalisa Quaini2, and Gianluigi Rozza1
1SISSA, International School for Advanced Studies, Mathematics Area, mathLab,
Via Bonomea 265, 34136 Trieste, Italy. , Email: giuseppe.pitton@sissa.it,
gianluigi.rozza@sissa.it
2University of Houston, Department of Mathematics, Houston, TX, USA. Email:
quaini@math.uh.edu
Abstract
We focus on reducing the computational costs associated with the hydrodynamic stabil-
ity of solutions of the incompressible Navier-Stokes equations for a Newtonian and viscous
ﬂuid in contraction-expansion channels. In particular, we are interested in studying steady
bifurcations, occurring when non-unique stable solutions appear as physical and/or geometric
control parameters are varied. The formulation of the stability problem requires solving an
eigenvalue problem for a partial diﬀerential operator. An alternative to this approach is the
direct simulation of the ﬂow to characterize the asymptotic behavior of the solution. Both
approaches can be extremely expensive in terms of computational time. We propose to apply
Reduced Order Modeling (ROM) techniques to reduce the demanding computational costs
associated with the detection of a type of steady bifurcations in ﬂuid dynamics. The appli-
cation that motivated the present study is the onset of asymmetries (i.e., symmetry breaking
bifurcation) in blood ﬂow through a regurgitant mitral valve, depending on the Reynolds
number and the regurgitant mitral valve oriﬁce shape.
Keywords: Reduced basis method, parametrized Navier-Stokes equations, stability of
ﬂows, symmetry breaking bifurcation
1
Introduction
We focus on the hydrodynamic stability of solutions of the incompressible Navier-Stokes equations
for a Newtonian and viscous ﬂuid in contraction-expansion channels, with a particular concern
on steady bifurcations.
Steady bifurcations occur when new, non-unique solution branches of
the Navier-Stokes equations appear as physical and/or geometric control parameters are varied.
When the ﬂuid domain is characterized by two or three dimensions with non-periodic boundary
conditions, the formulation of the stability problem requires solving an eigenvalue problem for
a partial diﬀerential operator. See [23] for a review on numerical methods for stability analysis
based on linearized eigenvalue problems. An alternative to the eigenvalue problem approach is
the direct simulation of the ﬂow to characterize the asymptotic behavior of the solution; see, e.g.,
[33, 3, 54]. Both approaches can be extremely expensive in terms of computational time. In this
paper, we propose to apply Reduced Order Modeling (ROM) techniques to reduce the demanding
computational costs associated with ﬂow stability analysis.
Practical applications of contraction-expansion channel ﬂows include equipments such as heat
exchangers, combustion chambers, and mixing vessel. An application that motivated the present
study is the onset of asymmetries (i.e., symmetry breaking bifurcation) in blood ﬂow through
c⃝2017. This manuscript version is made available under the CC-BY-NC-ND 4.0 license
http://creativecommons.org/licenses/by-nc-nd/4.0/
1
arXiv:1708.09718v1  [math.NA]  31 Aug 2017


## Page 2


(a) Location of Mitral Valve
(b) Central color Doppler jet
(c) Eccentric color Doppler jet
Figure 1: (a) Anatomy of the heart showing the mitral valve. (b) Echocardiographic image of central
regurgitant jet ﬂowing from the left ventricle (LV) to the left atrium (LA). Colors denote diﬀerent ﬂuid
velocities. (c) Echocardiographic image of eccentric regurgitant jet, hugging the walls of the left atrium
(LA) known as the Coanda eﬀect.
a regurgitant mitral valve, depending on the Reynolds number and the regurgitant mitral valve
oriﬁce shape. Mitral regurgitation is a valvular disease characterized by abnormal leaking of blood
through the mitral valve from the left ventricle into the left atrium of the heart. See Figure 1.
In certain cases the regurgitant jet “hugs” the wall of the heart’s atrium as shown in Figure 1(c).
These eccentric, wall-hugging, non-symmetric regurgitant jets have been observed at low Reynolds
numbers [67, 1] and are said to undergo the Coanda eﬀect [65, 70].
This eﬀect, described as
the tendency of a ﬂuid jet to be attracted to a nearby surface, owes its name to Romanian
aerodynamics pioneer Henri Coanda. The primary tool to assess the severity of mitral regurgitation
is echocardiography [73]. One of the biggest challenges in echocardiographic assessment of mitral
regurgitation is the Coanda eﬀect: the wall-hugging jets appear smaller in the color Doppler image
of regurgitant ﬂow, leading to a gross under-estimation of regurgitant volume by inexperienced
observers [31, 16]. As a result, patients requiring treatment may not be recognized.
Despite the large cardiovascular and bioengineering literature reporting on the Coanda eﬀect in
echocardiographic assessment of mitral regurgitation, there is very little connection with the ﬂuid
dynamics literature that could help identify and understand the main features of the corresponding
ﬂow conditions. In this paper, our goal is to understand what triggers the Coanda eﬀect in a
simpliﬁed setting. A contraction-expansion channel is a simpliﬁed setting which has the same
geometric features of mitral regurgitation. In fact, a mitral regurgitant jet ﬂows from the left
ventricle through the contraction between the mitral leaﬂet, called regurgitant oriﬁce, into the left
atrium. First, we focus on planar contraction-expansion channels (see Fig. 2) and investigate the
inﬂuence of the Reynolds number and the contraction width wc (i.e., the oriﬁce height) on the
ﬂow. Then, we consider the 3D geometry reported in Fig. 3 to understand the role played by the
channel depth h (i.e., the oriﬁce length). Eccentric regurgitant jets typically occur in prolapsed
mitral valves, i.e. when two valve ﬂaps of the mitral valve do not close evenly. Thus, another
parameter of interest, although not considered in this work, could be the oriﬁce depth. Moreover,
for a more realistic setting one would have to account for the pulsatility of the ﬂow and include
the Strouhal number among the parameters.
We remark that the focus of this paper is to investigate the cause of the Coanda eﬀect in
simpliﬁed settings. Nonetheless, it is thanks to the results reported here that our medical collab-
orators at the Houston Methodist DeBakey Heart & Vascular Center were able to reproduce the
Coanda eﬀect in a mock heart chamber (see Sec. 4.4). A comparison between the experiments in
vitro and corresponding 3D simulations is presented in [69].
The incompressible ﬂuid dynamics in a planar contraction-expansion channel has been widely
studied from both theoretical and practical perspectives; see, e.g., [49, 24, 63, 26, 36, 48] and
2


## Page 3


references therein. In the two-dimensional geometry reported in Fig. 2, the wall-hugging eﬀect
happens only above a critical Reynolds number (12), which depends on the expansion ratio λ
deﬁned in (11). Compare Fig. 5(e) and Fig. 5(b), which correspond to a Reynolds number above
and below the critical value, respectively. The asymmetric, wall-hugging solution remains stable
for a certain range of Reynolds number and asymmetries become stronger with the increasing
Reynolds number, as shown in [48]. The formation of stable asymmetric vortices in 2D planar
expansion is attributed to an increase in velocity near one wall that leads to a decrease in pressure
near that wall [70]. Once a pressure diﬀerence is established across the channel, it will maintain
the asymmetry of the ﬂow. The critical value of the Reynolds number has been identiﬁed for
diﬀerent expansion ratios λ. In particular, it was found that such critical value decreases with
increasing value of λ (see [24, 57]).
In the three-dimensional geometry reported in Fig. 3, the critical Reynolds number for the
symmetry-breaking (i.e., the wall-hugging) varies with the expansion ratio and the aspect ratio
deﬁned in (13), as shown in [17, 18, 52]. When the expansion ratio is ﬁxed and the aspect ratio
decreases, the endwall inﬂuence becomes more important: the critical Reynolds number increases
[18, 52]. For moderate aspect ratios, the ﬂow is steady in time but highly three-dimensional, and
complex spiraling structures are observed, which are not closed recirculating cells as in the case of
2D ﬂows. See Fig. 15. The numerical studies in [66] found that the ﬂow only resembles a 2D ﬂow
for very large aspect ratios. The theoretical study of Lauga et al. [41] shows that for low aspect
ratios the ﬂow is highly three-dimensional. The numerical and experimental studies in [52] show
that the strong three-dimensional eﬀects appearing for low aspect ratios inhibit the wall-hugging
eﬀect observed in geometries with high aspect ratios at the same Reynolds number. This suggests
that the eccentric regurgitant jets, such as the one in Figure 1(c), occur when the regurgitant
oriﬁce is long (large aspect ratio) and narrow (large expansion ratio).
Given the relatively fast decay of energy spectrum for ﬂows at suﬃciently low Reynolds num-
bers, a ROM technique is expected to be an eﬃcient tool to reduce the prohibitive computational
costs associated to identifying the ﬂow conditions and geometries that trigger asymmetries. Recent
developments of ROM techniques have focused on the reduction of computational time for a wide
range of diﬀerential problems [19, 55], while maintaining a prescribed tolerance on error bounds
[59, 38, 56]. Terragni and Vega [64] showed that a Proper Orthogonal Decomposition (POD)
approach allows for considerable computational time savings for the analysis of bifurcations in
some nonlinear dissipative systems. Herrero, Maday and Pla [37] have used a Reduced Basis (RB)
method to speed up the computations of diﬀerent solution branches of a two-dimensional natural
convection problem (Rayleigh-B´enard), achieving a good accuracy but without investigating the
approximation of bifurcation points. For each ﬁxed aspect ratio, multiple steady solutions for
the Rayleigh-B´enard problem can be found for diﬀerent Rayleigh numbers and stable solutions
coexist at the same values of external physical parameters. In [37], it is shown that stable and
unstable solutions are correctly identiﬁed by the RB method. Yano and Patera [72] introduced a
RB method for the stability of ﬂows under perturbations in the forcing term or in the boundary
conditions, which is based on a space-time framework that allows for particularly sharp error esti-
mates. Furthermore, in [72] it is shown how a space-time inf-sup constant approaches zero as the
computed solutions get close to a bifurcating value.
In a previous work [53] we have investigated steady and Hopf bifurcations in a natural convec-
tion problem dealing with a geometrical parameter (the cavity length), and a physical parameter
(the Grashof number). This work is an extension of that study and provides a proof of concept
of the applicability of reduced order methods to investigate stability and bifurcations in complex
ﬂuid dynamic problems at a reasonable computational cost. The proposed framework allows the
use of a black-box input-output toolbox to be managed also by non-expert scientists in compu-
tational sciences. The oﬄine-online splitting of the computational procedure is crucial in view
of the use of a High Performance Computing (HPC) infrastructure for the oﬄine computational
step (expensive and time consuming) and a light modern device, such as tablet or smart phone,
for online calculations. The idea is to use diﬀerent platforms (and methodologies) for a strategic
computational collaboration between high order and reduced order methods, with competitive
computational costs for complex simulations. This could still be considered a research frontier in
3


## Page 4


computational ﬂuid dynamics, especially in view of real life applications.
The outline of the paper is as follows. The general problem setting is described in Section 2,
while the numerical methods are treated in Section 3. Numerical results in 2D and 3D contraction-
expansion channels under diﬀerent parametrizations are reported in Section 4. Conclusions and
perspectives follow in Section 5.
2
Problem setting
Let Ω⊂Rd, d = 2, 3, be the computational domain. The motion of an incompressible, viscous
ﬂuid in a spatial domain Ωover a time interval of interest (0, T) is governed by the incompressible
Navier-Stokes equations
∂u
∂t + (u · ∇)u −∇· ß = 0
in Ω× (0, T),
(1)
∇· u = 0
in Ω× (0, T),
(2)
where u is the velocity and ß is the Cauchy stress tensor. In large arteries and inside the heart,
it is widely accepted to model blood as a Newtonian ﬂuid. See, e.g., [29] and references therein.
For such ﬂuids, σ(u, p) = −pI + 2νϵ(u), where p is the pressure, ν is the ﬂuid kinematic viscosity,
and ϵ(u) = (∇u + (∇u)T )/2 is the strain rate tensor. Eq. (1) represents the conservation of the
linear momentum, while eq. (2) represents the conservation of the mass. Eq. (1)-(2) need to be
endowed with boundary and initial conditions, e.g.:
u = d
on ΓD × (0, T),
(3)
ß · n = g
on ΓN × (0, T),
(4)
u = u0
in Ω× {0},
where Γ D ∪Γ N = ∂Ωand ΓD ∩ΓN = ∅. Here, d, g, and u0 are given. We assume that there is
no external body force acting on the ﬂuid (see eq. (1)) and the motion is driven by the boundary
conditions (3)-(4).
When the ﬂuid acceleration is negligible (i.e., the system has evolved towards a steady state),
eq. (1)-(2) can be replaced by:
(u · ∇)u −∇· ß = 0
in Ω,
(5)
∇· u = 0
in Ω,
(6)
To characterize the ﬂow regime under consideration, we deﬁne the Reynolds number as
Re = UL
ν ,
(7)
where U and L are characteristic macroscopic velocity and length respectively. We will characterize
U and L for the speciﬁc cases under consideration in Sec. 2.1 and 2.2.
For the variational formulation of the ﬂuid problem (1)-(2), we indicate with L2(Ω) the space
of square integrable functions in Ωand with H1(Ω) the space of functions in L2(Ω) with ﬁrst
derivatives in L2(Ω). We use (·, ·)Ωand ⟨·, ·⟩Ωto denote the L2 product and the duality pairing
between H1/2(Ω) and H−1/2(Ω), respectively. Moreover, let us deﬁne:
VD = H1
D(Ω) := {v ∈H1(Ω) s.t. v = d on ΓD},
V = H1
0(Ω) := {v ∈H1(Ω) s.t. v = 0 on ΓD},
Q
= L2(Ω).
The variational formulation of problem (1)-(2) with boundary conditions (3)-(4) reads: ﬁnd
(u, p) ∈VD × Q such that
∂u
∂t , v

Ω
+ (v, (u · ∇)u)Ω+ ν(ϵ(v), ϵ(u))Ω−(∇· v, p)Ω= ⟨g, v⟩ΓN
∀v ∈V ,
(8)
(q, div u)Ω= 0
∀q ∈Q.
(9)
4


## Page 5


x
y
Lc
wc
Figure 2: Scheme of the planar contraction-expansion channel considered in this work.
The
notation is the same used in [52].
If eq. (5)-(6) are used to model the ﬂuid dynamics, then the ﬁrst term in eq. (8) is disregarded.
The nonlinearity in problem (1)-(2) can produce a loss of uniqueness for the solution, with
multiple solutions branching from a known solution at a bifurcation point. As will be explained
in Sec. 2.1, the Coanda eﬀect is associated with a steady bifurcation point. To detect numerically
the presence of a steady bifurcation point, we will rely on the spectrum analysis of a linearized
operator.
See, e.g., [2] for a theoretical introduction to bifurcation theory, and [20] and [23]
for applications to numerical analysis.
Following [20, par. 7.3], we introduce the linearization
L : VD × V →V of the convection operator in eq. (5), obtained by Fr´echet diﬀerentiation about
a base point u∗of the term u · ∇u:
L(u∗)[v] = u∗· ∇v + v · ∇u∗.
(10)
At a symmetry breaking bifurcation point, a simple eigenvalue of L changes sign.
We remark that for the kind of bifurcations we are interested in (namely supercritical pitchfork
bifurcations) it is suﬃcient to study the spectrum of the antisymmetric part of the linearized
operator [20]. Other techniques would have to be used for diﬀerent kind of singular points (e.g.,
Hopf bifurcations, fold points) occurring at higher Reynolds numbers or in diﬀerent settings.
2.1
2D case
The domain under consideration for the two dimensional case is shown in ﬁgure 2. The following
boundary conditions are imposed in this case: homogeneous Dirichlet (no-slip) boundary condition
on the sides drawn with a continuous line, non-homogeneous Dirichlet boundary condition (time-
independent parabolic velocity proﬁle) on the red dashed line which corresponds to the inlet, and
homogeneous Neumann (stress-free) boundary condition on the blue dashed line which corresponds
to the outlet. For space limitation, the channel depicted in Fig. 2 is shorter than the actual one.
The actual domain length past the expansion is 6 times the channel height Lc. The length of the
contraction channel is equal to (Lc −wc)/2, and the distance between the inﬂow section and the
contraction is equal to Lc.
For the characterization of the ﬂow in the 2D case, we introduce the following quantities:
- expansion ratio:
λ = Lc
wc
;
(11)
- average horizontal velocity: ⟨vx⟩= Q
wc
, where Q is the ﬂow rate;
- Reynolds number:
Re2D = 2⟨vx⟩wc
ν
.
(12)
Notice that the above deﬁnition of Re2D does not coincide with taking L = wc and U = ⟨vx⟩
in (7). The reason for the extra factor 2 will be explained in the next subsection. In the numerical
simulations, we vary Re2D by changing the value of the viscosity ν.
5


## Page 6


x
y
z
h
Figure 3: Scheme for the 3D geometry.
In the geometry considered by [52] the expansion ratio λ is equal to 15.4. In order to reproduce
the results in [52] for validation purposes, in Sec. 4.1 we set λ = 15.4 and we focus on the interval
Re ∈[0.01, 90].
In this interval, the ﬂow conﬁguration evolves as follows when the Reynolds
numbers increases:
- Creeping ﬂow: for very low Reynolds numbers the velocity ﬁeld presents a double symme-
try, with respect to both the horizontal and vertical symmetry axes of the domain geometry.
See Fig. 5(a).
- Symmetric jet: for slightly larger Reynolds numbers there is a breaking of the vertical
symmetry.
The ﬂow is still symmetric with respect to the horizontal axis, but the two
vortices downstream of the expansion are larger than the vortices upstream. See Fig. 5(b).
At a further increase of the Reynolds number, the vertical asymmetry of the ﬂow becomes
increasingly evident, yet the horizontal symmetry is maintained.
- Asymmetric jets: when the Reynolds number is suﬃciently large, the conﬁguration with
a symmetric jet is still possible, but unstable [63]. In fact, small perturbations 1 expand one
recirculation zone and shrink the other, causing a drastic variation in the ﬂow. See Fig. 5(c)
and (d). This horizontally asymmetric solution remains stable for a certain range of Re2D
and asymmetries become stronger with the increasing Reynolds number, as shown in [48].
See also Fig. 5(e): the upper recirculation has enlarged and pushed the high velocity jet to
the upper wall. Notice that the ﬂow could have evolved to its mirrored image conﬁguration
with respect to the domain symmetry axis.
At the minimum value of the Reynolds number for which the asymmetric jet conﬁguration
exists there is a symmetry breaking bifurcation point or steady-state bifurcation point. In Sec. 4.3
we will show how the critical value of the Reynolds number for the symmetry breaking bifurcation
changes as λ varies.
2.2
3D case
A 3D channel is obtained by extruding the 2D geometry considered in the previous section in
the direction orthogonal to the ﬂow plane. The goal of this test case is to study the inﬂuence of
the channel depth on the ﬂow pattern, and in particular on the symmetry breaking bifurcation
point. Once λ is ﬁxed, the 3D problem depends on two parameters: the Reynolds number and
the channel depth h. See Figure 3. Note that also in this case the geometry reported in the ﬁgure
has been cropped due to space limitation. In reality, we considered a channel length past the
expansion equal to 6 times the channel height Lc.
The boundary conditions are the same as in the 2D case: we impose a parabolic velocity proﬁle
at the inlet, a stress-free condition at the outlet, and a no-slip condition everywhere else.
We introduce the following quantities, which are useful in the characterization of the numerical
simulation [52]:
- aspect ratio:
AR = h
wc
;
(13)
1That can be realized in several ways, e.g. with a slight variation of the boundary conditions, forcing terms, or
superimposing a small random ﬁeld to an established ﬂow ﬁeld and using this as a new initial condition.
6


## Page 7


- normalized channel depth: H =
h
h + wc
=
AR
AR + 1;
- average horizontal velocity: ⟨vx⟩=
Q
wch, with Q ﬂow rate;
- Reynolds number: Re3D = ⟨vx⟩
ν
2wch
h + wc
= ⟨vx⟩wc
ν
2AR
AR + 1.
Note that H = 1 is the limit case of inﬁnite channel depth, which corresponds to the 2D
conﬁguration. The deﬁnition of Re3D has been obtained by setting U = ⟨vx⟩and L equal to the
hydraulic diameter of the contraction channel in (7). We remark that the 2D case can be seen as
a limit of the 3D case for AR →∞. This justiﬁes the factor 2 in the deﬁnition of Re2D in (12).
Another reason to deﬁne Re2D in (12) is to compare our results with [52] (see Sec. 4.1).
For our 3D tests in Sec. 4.4, we set λ = 15.4 and let the normalized channel depth H span
interval [0.2, 0.95]. This corresponds to a wide range of aspect ratios: AR ∈[0.2635, 19.71]. As
for the Reynolds number, we consider the same interval of interest used for the 2D case, namely
[0.01, 90].
3
Numerical method
We are interested in adopting a Reduced Order Model (ROM) for the numerical solution of the
problems presented in the previous section.
Reduced Order Models have been introduced for
parametrized problems requiring real-time capabilities due to a many-query setting. The goal
is to compute reliable results at a fraction of the cost of a conventional (full order) method. A
practical way to realize this is to organize the computation in two steps:
- An oﬄine phase: full order approximation solutions corresponding to selected representa-
tive parameters values/system conﬁgurations are computed and stored, together with other
information concerning the parametrized problem. This is a computationally expensive step
usually performed on high performance computing facilities.
- An online phase: the information obtained during the oﬄine phase is used to compute the
solution for a newly speciﬁed value of the parameters in a short amount of time (ideally in
real time), even on a relatively low power device such as a laptop or a smartphone.
These split computational procedures are built in such a way that new parameter dependent
quantities are easily and quickly computed online, while representative basis functions for selected
parameter values and more demanding quantities are pre-computed oﬄine. We refer to [40] for a
review of ROM in Fluid Mechanics.
The problem under consideration might depend on several parameters, with each parameter
varying in a certain range. We introduce a parameter vector µ that contains all parameters. If
the problem depends on two parameters, we have µ = (µ1, µ2) ∈D1 × D2 = D; for example
µ = (Re, H) ∈D = [0.01, 90] × [0.2, 0.95]. We consider both physical parameters (e.g., Re) and
geometric parameters (e.g., λ and H). To stress the solution dependence on the parameter(s),
we will use the notation u = u(µ) and p = p(µ), without implying that there is a one-to-one
correspondence between µ and u or p. The maps µ 7→u(µ) and µ 7→p(µ) are one-to-one only
on the region of D where there exists a unique solution of problem (1)-(2).
The treatment of the geometric parametrization deserves further explanation. Let ξ ∈D be
a geometric parameter the problem depends on. We select a reference domain bΩthat is mapped
to the parametrized domain Ω(ξ) through a one-to-one, orientation preserving transformation
T : D × bΩ→Ω(ξ). Using this map, we can cast eq. (8)-(9) into the reference domain. For
instance, eq. (9) becomes:
(q, div u)Ω(ξ) =
Z
Ω(ξ)
q div u dx =
Z
bΩ
q F−T |J(ξ)| div u dbx,
(14)
7


## Page 8


where F(ξ) is the Jacobian matrix of transformation T (ξ) and J(ξ) its determinant.
Among many Reduced Order Models available in the literature, we choose a Reduced Basis
(RB) method. We will brieﬂy recall the main features of RB methods in the following sections.
For a general review on the RB method we refer to, e.g., [59, 38, 56].
3.1
Full order approximation
As full order approximation scheme for eq. (8)-(9) to be used in the oﬄine phase, we choose
the Spectral Element Method (SEM). See, e.g., [22, 14, 13] for a general review of SEM and
application to ﬂuid mechanics.
We adopt the SEM implementation available in open source
software Nek5000 [27], where the basis functions for each element are the Lagrange interpolants
on a Gauss-Lobatto-Legendre tensor product grid. We refer to [22] for an introduction to eﬃcient
SEM implementation.
Let V N , QN , and V N
0
be the Spectral Element spaces, which are ﬁnite dimensional approxima-
tions of the inﬁnite dimensional spaces VD, Q, and V , respectively. The full order approximation
problem reads: for a given µ ∈D, ﬁnd (uN (µ), pN (µ)) ∈V N × QN such that
∂uN
∂t , v

Ω
+ (v, (uN · ∇)uN )Ω+ ν(ϵ(v), ϵ(uN ))Ω−(div v, pN )Ω= 0,
∀v ∈V N
0 ,
(15)
(q, div uN )Ω= 0,
∀q ∈QN .
(16)
Notice that in eq. (15)-(16) we have already accounted for the fact that g = 0 in (4) for both the
2D and 3D case.
For the computations in Sec. 4, we choose the stable P11 −P9 couple for velocity and pressure
approximation. In the Nek5000 solver, the aliasing errors associated with the choice of high order
polynomials for approximating the nonlinearity are dealt with the 3/2 rule (also called zero-padding
rule, see [10]). This rule consists in evaluating the integrals of the nonlinear term (to be liearized)
using a quadrature formula with 3/2 times the quadrature points of the other terms, so that the
aliasing errors contribute only for those wavelengths that are ﬁltered out by the grid size. For
the time discretization of eq. (15)-(16) we adopt a Backward Diﬀerentiation Formula of order 3
(BDF3; see, e.g., [22]). The convective term is treated explicitly, with a third order extrapolation
formula as explained in Nek5000 documentation [50]. Such a treatment of the convective term
does not guarantee the unconditional stability in time of the linearized numerical scheme. A CFL
condition has to be veriﬁed at every collocation point.
Given an initial solution, we consider the system to be close enough to the steady state when
the following stopping condition is satisﬁed:
∥uN
n −uN
n−1∥L2(Ω)
∥uN
n ∥L2(Ω)
< tol,
(17)
with tolerance tol = 10−8. When the stopping criterion (17) is met, the simulation is interrupted.
3.2
Sampling
The sampling process consist in selecting N parameters {µi}, with i = 1, . . . , N, in the parameter
space D, whose corresponding solutions {uN (µi)} ⊂V N and {pN (µi)} ⊂QN will be used to
construct the Reduced Basis spaces for velocity and pressure, respectively. Solutions uN (µi) and
pN (µi), with i = 1, . . . , N, are called snapshots. In order to simplify the notation, we will denote
uN (µi) by u(µi) and pN (µi) by p(µi). In this section, we are going to explain how to select the
velocity snapshots. The same procedure can be applied to obtain the pressure snapshots.
Let µk be the k-th component of parameter vector µ and let Dk be the interval of interest for
such component. The sampling procedure described below will select Nk values of µk in Dk and
the total number of sample parameter vectors is N = Q
k Nk:
{µi}N
i=1 = ⊗k{µj
k}Nk
j=1.
(18)
8


## Page 9


For each component µk of the parameter vector µ we choose as µj
k the Chebyshev points:
µj
k = µk,min + µk,max −µk,min
2
cos((j −1)π/(Nk −1)),
j = 1, . . . , Nk,
(19)
where
µk,min = min
µk∈Dk µk
µk,max = max
µk∈Dk µk.
(20)
This procedure to sample sample points in D is called Gauss-Lobatto-Chebyshev (GLC) tensor
product collocation strategy [71]. For example, Fig. 4 shows the sample parameters considered
for the 3D case where µ = (Re, H) ∈= [0.01, 90] × [0.025, 1]. The corresponding values of the
Reynolds number and H are reported in tables 1 and 2, respectively. Note that the tensor product
collocation allows to choose a diﬀerent number of sampling points Nk for each component of the
parameter space.
0
10
20
30
40
50
60
70
80
90
Re
0.0
0.2
0.4
0.6
0.8
1.0
H
Figure 4: Sample parameters for the 3D case with µ = (Re, H) ∈= [0.01, 90] × [0.025, 1]
The GLC collocation points are a practical choice, since in this case many sampling points share
the same geometric parameter, requiring to start the continuation method very few times [71].
Other sampling methods such as Greedy [59] or CVT [53] would require to start the continuation
method for each new sampling point. A disadvantage of the GLC collocation strategy is that the
approximation spaces are not hierarchical, meaning that the RB spaces for a certain value of N
are not in general subspaces of the RB spaces obtained for a higher value of N. This could increase
the oﬄine computational cost in case we need to enrich the RB spaces.
Our conjecture is that for bifurcation problems it may be useful to cluster the sampling points
close to the bifurcation points. However, to the best of our knowledge, there are no error esti-
mates for diﬀerent sampling methods for steady state Navier-Stokes equations involving bifurcation
points. In any case we are enriching our investigation with an eigenvalue analysis to detect the
bifurcation point at the reduced level as well, as we will introduce in Sec. 3.5.
Table 1: 2D and 3D case: values of the Reynolds number used for the Chebyshev collocation
sampling.
1
2
3
4
5
6
7
8
9
Re
0.010
4.466
13.19
27.79
45.01
62.22
76.82
86.58
90.00
3.3
Construction of the RB spaces
For every selected sample µi, we solve the full order approximation problem (15)-(16) until stop-
ping criterion (17) is satisﬁed to get u(µi) and p(µi). After the sampling is complete, we have two
9


## Page 10


Table 2: 3D case: geometric parameters used for the Chebyshev collocation sampling. Notice that
sample 8 corresponds to the 2D case.
1
2
3
4
5
6
7
8
H
0.025
0.0733
0.2085
0.4040
0.6210
0.8165
0.9517
1
AR
0.026
0.0791
0.2634
0.6779
1.6389
4.4550
19.704
∞
sets of snapshots {u(µi)}N
i=1 and {p(µi)}N
i=1 which generate the ﬁnite dimensional subspaces V N
and QN, called Reduced Basis spaces. The key feature of a correct ROM is that the dimension of
the reduced order space is much lower that the dimension of the full order space:
N = dim V N ≪N = dim V N .
(21)
In this way, all the computations required by the online phase (see Sec. 3.4) will be much less
expensive that the computations required during the oﬄine phase.
In this section, we are going to focus on how to construct the Reduced Basis {φi}N
i=1 for V N.
The same procedure can be applied to obtain the Reduced Basis {σi}N
i=1 for QN. To actually build
the space V N, it is usually preferred not to evaluate directly the inner products in eq. (15)-(16)
for all the snapshots {u(µi)}, for two reasons:
- the snapshots may contain some redundant information, due to the sampling procedure, thus
leading to linear dependence and ill-conditioning during the matrix assembling.
- in general the snapshots will not be orthogonal to each other, and consequently they will
generate a full mass matrix, increasing the storage requirement and operations count.
Thus, it is preferred to compute an orthonormal generating set {φi}N
i=1 for V N so that the
resulting linearized problem is well conditioned. Two of the most popular techniques to compute
othogonal basis functions are the Proper Orthogonal decomposition (POD) [68] and the Gram-
Schmidt orthogonalization (GS) with its variants [60].
One of the ways to build a POD is to compute the correlation matrix for the set of snapshots,
deﬁned as as
Cij = (uN (µi), uN (µj)).
(22)
The eigenvalues λi and eigenvectors ψi of C are computed, and each POD basis vector is deﬁned
as
φi =
N
X
k=1
ψi,kuN (µk)
(23)
where ψi,k denotes the k-th component of the i-th eigenvector. The eigenvalue λi associated to
each POD mode is related to the fraction of energy stored in the corresponding mode. The POD
modes are automatically orthogonal in the L2 inner product, but not normal in general.
It can be shown [68, 35] that the space generated by the POD, denoted by V N
POD, minimizes
the projection error in the L2 norm:
V N
POD = arg minV N⊂V ,dim V N=N
N
X
i=1


u(µi) −ΠV N u(µi)


 .
(24)
where ΠV N : V →V N is the projection operator on the space V N generated by the POD modes.
For the results reported in Sec. 4, we have used POD to compute the basis functions. However,
we would like to remark that POD has one major drawback when the number of snapshots is
large: the number of operations required to compute the correlation matrix (22) and its eigenpairs
becomes prohibitive. If this is the case, a Gram-Schmidt orthogonalization is usually preferred
10


## Page 11


over computing the basis functions by means of a POD [60]:
φi = uN (µi) −
i
X
j=1
φj(uN (µi), φj)
φi ←
φi
∥φi∥,
(25)
where the normalization step is not always adopted, since it may lead to an ill-conditioned linear
system.
As mentioned above, the same orthonomalization method can be applied to obtain the pressure
basis {σi}N
i=1. The reduced basis spaces V N and QN are deﬁned as:
V N = span{φi}N
i=1
and
QN = span{σk}N
k=1.
(26)
3.4
Online phase computation
After the construction of the Reduced Basis spaces, an online approximation of the solution can
be computed by applying the Galerkin projection to the spaces V N and QN. Namely, given a
target parameter µ ∈D we search for (uN(µ), pN(µ)) ∈V N × QN such that
∂uN(µ)
∂t
, v

Ω
+
 v, (uN(µ) · ∇)uN(µ)

Ω+ ν
 ϵ(v), ϵ(uN(µ))

Ω−
 ∇· v, pN(µ)

Ω= 0
∀v ∈V N,
(27)
 q, div uN(µ)

Ω= 0
∀q ∈QN.
(28)
For convenience, for the rest of this section we are going to assume that the ﬁrst term in eq. (27)
is negligible, as if the ﬂow was modeled by eq. (5)-(6).
The convective term is linearized with a ﬁxed point scheme. Suppose that an initial tentative
solution uN
0 (µ) is known. Given uN
k−1(µ), at the k-th iteration of the ﬁxed point method we solve
problem:
 v, (uN
k−1(µ) · ∇)uN
k (µ)

Ω+ ν
 ϵ(v), ϵ(uN
k (µ))

Ω−
 ∇· v, pN
k (µ)

Ω= 0
∀v ∈V N,
(29)
 q, div uN
k (µ)

Ω= 0
∀q ∈QN.
(30)
The iterative scheme can be stopped for instance when an increment-based residual:
resk = ∥uN
k (µ) −uN
k−1(µ)∥
∥uN
k (µ)∥
(31)
is below a given tolerance.
The solution scheme described so far requires the V N −QN pair to satisfy a stability condition
called inf-sup condition or Ladyzhenskaya-Brezzi-Babuˇska (LBB) condition:
inf
q∈QN sup
v∈V N
(q, div v)
∥q∥Q∥v∥V
= βN > 0.
(32)
See, e.g., [39, 4, 11, 9, 25]. Spaces V N and QN in (26) computed using the POD or GS modes
as explained in Sec. 3.3 are not guaranteed to fulﬁll condition (32). There are two options for
circumventing this issue: casting the problem into a divergence-free space (see, e.g., [53]) and
enforcing approximation stability properties for the V N −QN pair (see, e.g., [60, 58, 6]). Here,
we choose the former approach. This means that we require V N to be a subset of H1
div(Ω):
H1
div(Ω) := {v ∈H1(Ω) s.t. (q, div v) = 0 ∀q ∈L2(Ω)},
(33)
11


## Page 12


which is a subspace of H1(Ω). If the basis functions for V N are divergence-free, eq. (30) is no
longer needed. Thus, the pressure disappears from the variational formulation and we do not need
to build the space QN. See, e.g., [28].
With a divergence-free basis set for V N, at every ﬁxed-point iteration we have to solve the
following linear system:
Ak(µ)uk = bk
(34)
where uk is the vector containing the projection coeﬃcients of uN
k−1 onto the space V N, bk ∈RN
depends from the speciﬁed boundary conditions, and Ak(µ) ∈RN×N is given by:
Ak
lj(µ) =
 φl, uN
k−1(µ) · ∇φj

Ω+ ν (∇φl, ∇φj)Ω.
(35)
Once the velocity uN(µ) ∈H1
div(Ω) has been computed, the pressure can be recovered, for exam-
ple, by solving a Poisson problem online:
∆pN(µ) = −div
 uN(µ) · ∇uN(µ)

.
We refer to,e.g., [12] for an analysis of velocity-pressure reduced order models.
In equation (35), we wrote explicitly the dependence of matrix A on the parameter vector µ.
Such dependence is more or less evident for the diﬀerent type of parameters. For instance, if the
Reynolds number is the only parameter, i.e. µ = µ1 = Re, from (7) we have ν = UL/Re and
matrix A can be written as:
Ak
lj(Re) =
 φl, uN
k−1(Re) · ∇φj

Ω+ LU
Re (∇φl, ∇φj)Ω,
with a linear dependence on Re−1. On the other hand, if H is the only parameter, i.e. µ = µ1 = H,
the dependence of A on it is hidden in the inner products and diﬀerential operators. This holds
true in general for geometric parameters. Let ξ ∈D be a geometric parameter. If the geometric
transformation T : D × bΩ→Ωis aﬃne, it is possible to express the inner products as a linear
combination of the inner products on the reference domain:
A(ξ) =
dim D
X
i=1
Θi(ξ)Ai.
(36)
Only functions Θi depend on ξ and need to be evaluated online.
Matrices Ai are assembled
oﬄine since they do not depend on ξ. Thus, the aﬃne decomposition (36) allows for important
computational time savings. In this work, we will consider only aﬃne decompositions. If A depends
nonlinearly on ξ, it has to be computed from scratch for each value of ξ. The eﬃcient assembling
of A when the geometric transformation is non-aﬃne is still an active research area, one of the
most popular techniques being the Empirical Interpolation Method [7].
The construction of a divergence-free basis set for V N when geometric parameters are con-
sidered is less trivial than in the case of physical parameters only.
Thus, it requires further
explanation. The Piola transformation P can be seen as the composition of the map T in eq. (14)
with any function f deﬁned on the image (or preimage) of T . For example, if f : bΩ→R, a
new function g : Ω→R can be obtained by considering g(x) = f(T −1x) for x ∈Ω. The Piola
transformation P acts as a map between ﬁnite dimensional Hilbert spaces D×V N(bΩ) and V N(Ω):
P : D × V N(bΩ) →V N(Ω).
Its use in an oﬄine-online setting is as follows:
1. The snapshots {uN (µi)}N
i=1 are divergence-free on the original domain Ω. By pulling back
the divergence operator to the reference domain bΩthrough the Piola map, we obtain a set
of snapshots that are divergence free on the reference domain.
12


## Page 13


2. Perform the POD or GS orthogonalization for the divergence-free snapshots on the reference
domain to obtain a basis for V N(bΩ). These basis functions are divergence free on bΩ, but
not on Ωunless mapped with the Piola transformation.
3. Compute the matrices Ai in (36) on the reference domain and with the orthogonal divergence-
free basis set.
4. During the online phase, apply the Piola transformation to the matrices Ai computed at step
3 so that their entries coincides with the Piola-transformed divergence-free basis functions
computed on Ω.
We refer to [9] for details on the Piola transformation, and to [46] for an application to RB
methods in incompressible ﬂuid mechanics in laminar regime. For the application of RB methods
to moderately turbulent ﬂows we refer for example to [45], and references therein.
Regarding the boundary conditions, the global support of the RB modes does not allow to
impose pointwise values for the non-homogeneous Dirichlet condition. An equivalent way to impose
the desired ﬂow conditions is to impose the mass ﬂow rate, instead of the inﬂow velocity proﬁle.
The physically correct deﬁnition of mass ﬂow rate is:
˙vx =
R
Ωux dx
R
Ωdx ,
(37)
where ux is the x-component of the velocity. Notice that due to incompressibility and the pre-
scribed boundary conditions, (37) is equivalent to:
˙vx =
R
Γinlet ux dx
R
Γinlet dx .
From the implementation point of view, it is more convenient to impose the integrated mass
ﬂow rate ˙wx, that for a given inlet velocity proﬁle is deﬁned as:
˙wx =
Z
Ω
ux dx.
(38)
We impose the average mass ﬂow condition for the RB simulation through a Lagrange multiplier
approach as follows. We compute the integrated mass ﬂow rate for each of the RB functions:
˙ci =
Z
Ω
φi,x dx,
(39)
and collect all the ˙ci in a vector C ∈RN. Let αk ∈R be the Lagrange multiplier associated with
the mass ﬂow rate constraint at the k-th iteration of the ﬁxed point method described above.
Notice that this is a new unknown in the problem. Then, instead of solving system (34), at each
ﬁxed-point iteration we solve the following linear system:

Ak(µ)
CT
C
0
 
uk
αk

=

bk
˙wx

.
(40)
We remark that imposing a constrainted condition by a Lagrange multiplier is fairly common in
the Reduced Basis context, see, e.g.,[51].
3.5
Bifurcation detection
In the conﬁguration described in Section 2, the ﬁrst pitchfork bifurcation point is determined by
a classical modal stability analysis, that can be set up as follows. Let us consider the 3D case, for
which the parameters are Re3D and H. Suppose that an initial RB solution uN(µi) of the steady
state problem is known for a given value of the parameter µi = (Re3D,i, Hi), characterized by a
suﬃciently small Reynolds number Re3D,i so that the solution is surely unique. We proceed as
follows: set s = 1 and Res = Re3D,i, then:
13


## Page 14


1. Keeping ﬁxed the value of the geometric parameter Hi, increase the value of the Reynolds
number by a suﬃciently small increment ∆Re (i.e., small enough so that the corrector step
will converge to a solution in the desired branch) and set µs+1 = (Res + ∆Re, Hi).
2. Compute the RB solution uN(µs+1) of the steady state problem for the new parameter value
µs+1.
3. Compute the Galerkin projection of operator L deﬁned in (10) on the RB space V N to form
the matrix L(µs+1):
Lkl(µs+1) = (φk, L(uN(µs+1))[φl]).
(41)
4. Compute the eigenvalues of L(µs+1) and check if there is one eigenvalue that has changed
sign with respect to the previous iteration. If not, set s = s + 1 and go back to step 1.
We remark that the above algorithm may be unstable in the sense that in a neighborhood of
the bifurcation point it may abruptly switch the approximated solution branch, or fail to converge.
To make sure that the approximation is always laying on the correct branch a continuation method
may be used.
Continuation methods rely on a predictor-corrector iteration to compute solutions lying on the
same branch. Suppose that the u(µs) is a solution of equations (8)-(9), and is known to lie on a
certain branch of interest. The predictor step consists in the computation of an initial guess for
the velocity increment ∆u due to an increase of a single parameter, denoted by ∆µ, by solving the
linearized Navier-Stokes equations. Then, starting from the prediction ˜u = u(µs)+∆u, a Newton
iteration is set up to impose that the new solution u(µs +∆µ) solves the original problem (8)-(9),
under the constraint that the solution be orthogonal to the tangent plane at the point (µs, u(µs))
in the parameter-solution space. We refer to e.g. [23] for an introduction to continuation methods
in ﬂuid mechanics.
The continuation method is computationally quite expensive. Thanks to the fact the the GLC
collocation strategy keeps the number of sample values small, the number of times the continuation
method has to be restarted is reduced, allowing for important computational time savings.
Note that the matrix L is dense but has rank equal to N, with N of the order of a few tenths
at most. Hence all the eigenvalues can be computed inexpensively with QR iterations [32], for
instance. If the spectrum analysis had to be carried out on the full-order model, only a few of the
eigenvalues closer to zero could be computed. Moreover, the computations would be much more
expensive, requiring Krylov subspace methods [61] and most likely a supercomputer.
For the 2D case, we use an analogous algorithm, the only diﬀerence being that the parameters
are Re2D and λ.
Lately, increasing attention has been devoted to eigenvalue calculation (as bifurcation detector
tool) at the reduced order level [47, 34]. We refer to [30] for a theoretical analysis of bifurcation
detection techniques in Navier-Stokes equations and to [21] for a bifurcation detection method in
a similar geometry.
4
Results
In this section the method described in section 3 will be validated against benchmark problems
reported in [52, 24]. We start with the test cases in two dimensions and then consider problems
in three dimensions. We show that our RB method successfully captures the bifurcation points
reported in [52, 24]. We compare our results with full order solutions and provide an estimate of
the computational savings. Moreover, we carry out an extensive set of simulations that will allow
us to conﬁrm that the eccentric mitral regurgitant jets occur when the regurgitant oriﬁce is long
(large aspect ratio) and narrow (large expansion ratio).
14


## Page 15


4.1
2D case: one parameter study
We start with the validation of the bifurcation detection method presented in section 3.5 for the
2D test case with the Reynolds number as the only varying parameter. For the moment, the
geometry is kept ﬁxed. We set the expansion ratio λ to 15.4 in order to compare our results with
those reported in reference [52]. In this case we choose a mesh with 308 spectral elements of order
11, with careful reﬁnement near the re-entrant corners of the domain, where we can expect a loss
of regularity for the solution.
As shown in table 1, we sample nine values for the Reynolds number in the interval Re2D ∈
[0.01, 90]. For the ﬁrst four values of Re2D in table 1 the oﬄine solver returned only the symmetric
solution, as expected. For the remaining ﬁve values, the solver returned two snapshots: one for the
symmetric solution (unstable [63]) and one for the asymmetric solution (stable). As mentioned in
Sec. 2.1, at a Reynolds number higher than the critical value for the symmetry breaking two stable
solutions co-exist, which are one the mirrored image of the other with respect to the horizontal
axis (see, e.g., [8]). Bifurcation theory allows to clarify the nature of the multiplicity of possible
ﬂows, whereas a (numerical or laboratory) experiment will give one or the other of the stable
symmetric solutions. Thus, for the multi-parameter case we will disregard the symmetric unstable
solution and retain only the stable solutions.
The online phase for the 2D problem is performed with a RB space of dimension N = 9. In
Fig. 5 we report representative snapshots for the 2D case, corresponding to Reynolds numbers
Re2D = 0.01, 13.2, 27.7, 62.2.
For very low Reynolds number the solution is characterized by
symmetry about the horizontal axis and a vertical axis, with a couples of vortices both upstream
and downstream of the contraction called Moﬀatt eddies [49].
See Fig. 5(a).
As the inertial
eﬀects of ﬂuid become more important (i.e., as Re2D increases), the Moﬀatt eddies upstream
of the contraction gradually diminish in size and two recirculation regions of equal size develop
downstream of the expansion. See Fig. 5(b). Symmetry about the vertical axis is lost, but the
solution is still symmetric about the horizontal axis. Past the bifurcation point we can see two
solutions: a symmetric one (unstable) and a slightly asymmetric one (stable). See Fig. 5(c) and
(d). The formation of stable asymmetric vortices in 2D planar expansion is attributed to the
Coanda eﬀect (see [70]): an increase in velocity near one wall will lead to a decrease in pressure
near that wall and once a pressure diﬀerence is established across the channel it will maintain the
asymmetry of the ﬂow. This asymmetric solution remains stable for a certain range of Re2D and
asymmetries become stronger with the increasing Reynolds number. See Fig. 5(e).
(a) Re2D = 0.01
(b) Re2D = 13.19
(c) Re2D = 27.7, unstable solution
(d) Re2D = 27.7, stable solution
(e) Re2D = 62.22
Figure 5: Representative snapshots for the 2D case for λ = 15.4: velocity magnitude and stream-
lines for (a) Re2D = 0.01, (b) Re2D = 13.2, (c) Re2D = 27.7 unstable solution, (d) Re2D = 27.7
stable solution, and (e) Re2D = 62.2.
To test the bifurcation detection method described in section 3.5, we run the online solver
parametrized using the 2D basis set with N = 9 snapshots. In Fig. 6, we plot the real part of
15


## Page 16


the eigenvalue of matrix L in (41) responsible for the symmetry breaking. We see that the curve
crosses the horizontal axis at a Reynolds number of about Re2D,sb = 26. This is in good agreement
with the critical values for the symmetry breaking reported by [52, 54] (Re2D,sb = 28) and [48]
(Re2D,sb = 27).
Figure 6: 2D case for λ = 15.4: real part of the eigenvalue of matrix L in (41) responsible for
the symmetry breaking as a function of the Reynolds number in a neighborhood of a bifurcation
point.
Fig. 7(a) shows the path of the eigenvalues of matrix L in (41) in the complex plane for
Re2D ∈[20, 55]. The arrows indicate the direction of the increasing Reynolds numbers. Fig. 7(b)
is a zoomed-in view of Fig. 7(a), and Fig. 7(c) is in turn a zoomed-in view of Fig. 7(b). In Fig. 7(c)
we see the eigenvalue responsible for the bifurcation: it is the simple eigenvalue colored in blue
that changes sign as the Reynolds number increases.
For this 2D case, the computational savings are signiﬁcant. The detection of the bifurcation
point using the continuation method required about 80 runs, with a total computational time of
around 5 minutes (0.08h) on a common desktop computer, which means 3.75s per online single
run. The same computations using the full order model described in sec. 3.1 would have required
about 10 CPU-hours per run. Hence, adding to the online cost the time required for the RB spaces
generation (i.e., the 2 CPU hours required by the POD computations), we can estimate that the
computational cost for the reduced model is around 11.5% of the computational cost for the full
order model, considering all the operations needed for the bifurcation detection and computation
(N = 9).
Time to build the RB spaces + Online time to detect the bifurcation point
Time of the equivalent full order computation
= 9 · 10h + 2h + 0.08h
80 · 10h
≃11.5%.
More generally, if only the online runtimes are considered, the computational savings become much
more relevant compared with the oﬄine runtimes per single query:
RB online query time
Equivalent full order single computation = 3.75s
10h ≃0.01%.
An important quantity to be used as indication if a reduced computational model is competitive
is the break-even, comparing all the oﬄine computational times needed to prepare the reduced
basis problem (N = 9) and an online query with full order model:
All full order computations for RB prep.
Full order one query comp. time
= 9 · 10h + 2h
10h
≃9.2.
suggesting that the use of Reduced Order Methods becomes more and more competitive as the
number of queries increases (with 10 or more queries this approach brings already important
computational advantages). Also, this conﬁrms that for the one-parameter scenario, this method
16


## Page 17


(a) eigenvalues of matrix L
(b) zoomed-in view of (a)
(c) zoomed-in view of (b)
Figure 7: 2D case for λ = 15.4: (a) path of the eigenvalues of matrix L in (41) in the complex
plane for Re2D ∈[20, 55]. Subﬁgure (b) is a zoomed-in views of subﬁgure (a) and subﬁgure (c) is
a zoomed-in views of subﬁgure (b). The arrows indicate the direction of the increasing Reynolds
numbers. The eigenvalue responsible for the bifurcation is the one colored in blue in (c).
could be eﬃciently adapted to a real-time query tool to be used, e.g., on smartphones or other
mobile devices with appropriate apps.
We conclude this section by showing that there is no visible qualitative diﬀerence between the
solutions obtained with the full order method and with the RB method for values of the Reynolds
number not associated with the snapshots. See the comparison in Fig. 8
(a) Re2D = 20, full order
(b) Re2D = 20, reduced order
(c) Re2D = 55, full order
(d) Re2D = 55, reduced order
Figure 8: 2D case for λ = 15.4: solutions obtained with the full order (left) and reduced order
(right) method for (a) and (b) Re2D = 20, (c) and (d) Re2D = 55.
17


## Page 18


4.2
Unstable solution branch
As already mentioned, for a given expansion ratio λ and given Re2D the symmetric ﬂow conﬁg-
uration exists regardless of whether Re2D is smaller or grater than the critical value Re2D,sb for
the bifurcation. Indeed, the symmetric branch is the only solution branch existing for Reynolds
numbers below Re2D,sb, but for Reynolds numbers above Re2D,sb it becomes unstable. See, for
example, the unstable symmetric ﬂow conﬁguration for Re2D = 27.7 in Fig. 5(c) and the corre-
sponding stable asymmetric conﬁguration in Fig. 5(d).
The numerical tests have shown that the RB approximation of the unstable branch can be
achieved, but some care is required with the choice of the trial and test RB spaces. One way to
reconstruct the unstable branch is to use only the basis functions coming from the sampling of
the unstable branch itself for both trial and test spaces. If this strategy is adopted, all the ﬂow
conﬁgurations of the unstable branch will be correctly approximated, but the bifurcation point will
not be detected. On the other hand, if basis functions coming from both the symmetric and the
asymmetric branch are employed, the bifurcation point can be successfully detected but the ﬁxed
point scheme fails to converge after the bifurcation point, oscillating without damping between
the two solution branches. In this case, convergence to the symmetric or asymmetric branch after
the bifurcation point can be achieved through e.g. a predictor-corrector or a pseudo-arclength
continuation method (see [23]) during the online phase, with a further programming eﬀort.
On the other hand, if one is interested only in the approximation of the stable solution branches,
there is no need for basis functions coming from the unstable branch and no need for a continuation
method in the online phase. The reduced basis for the velocity is constructed only with basis
functions arising from stable branches. This will allow to detect the bifurcation point and compute
the stable solution for every parameter value.
4.3
2D case: two-parameter study
In this section, we still consider a slightly modiﬁed 2D channel: the part of the channel upstream
of the sudden expansion in Fig. 2 is removed, since we focus now on the ﬂow downstream of the
contraction. The new geometry is thus a rectangle. We let vary both the Reynolds number and
the contraction width, so the parameter vector has now two components: µ = (Re2D, λ).
In this very simple case, the geometry can be parametrized in two diﬀerent ways:
- Geometric parametrization: the contraction width is treated as explained in section 3
and the incompressibility constraint can be imposed through the Piola transformation as
explained in section 3.4;
- Boundary condition parametrization: the diﬀerent aspect ratio of the contraction is
imposed by parametrizing the boundary conditions. Indeed, a channel with a contraction of
width λ will produce in our model a parabolic inner velocity proﬁle dependent on λ:
vx =



−(y −λLc)(y + λLc)
λ2L2c
if −λLc ≤y ≤λLc
0
otherwise,
(42)
where the y coordinate has origin on the symmetry axis of the contraction.
One advantage of the second strategy is that the RB functions are automatically divergence-free
and the relatively complex procedure of the Piola transformation does not need to be performed.
Thus, we choose the boundary condition parametrization. However, we need to be careful in im-
posing the inlet velocity proﬁle because the mass ﬂow rate constraint as expressed in equations (39)
and (40) is not suﬃcient to ensure uniqueness of the RB solution. One possible workaround for
this issue is to split the boundary integral (38) used for the mass ﬂow rate constraint in two parts:
Z
Γin
vx dx =
Z
Γ0
vx dx +
Z
Γλ
vx dx,
(43)
18


## Page 19


where Γin is the part of ∂Ωwhere the inlet velocity proﬁle is imposed, Γ0 the part of Γin where
vx = 0 and Γλ the part of Γin where vx ̸= 0. Notice that Γ0 ∪Γλ = Γin and Γ0 ∩Γλ = ∅. We
introduce two Lagrange multipliers α0 for Γ0 and αλ for Γλ, in order to enforce (42) in integral
form as:
α0
Z
Γ0
vx dy = 0
αλ
Z
Γλ
vx dy = ˙wx
(44)
Finally, the two Lagrange multipliers α0 and αλ are treated as additional unknowns, and a linear
system analogous to that in equation (40) is solved.
The GLC collocation sampling has been carried out on the kinematic viscosity set ν ∈[1.5, 5] ·
10−3 and on the contraction width set wc ∈[1/10, 1/2]. We obtained 6 values for the kinematic
viscosity ν = 1.5·10−3, 1.73446·10−3, 2.375·10−3, 4.125·10−3, 4.76554·10−3, 5·10−3 and 7 values
for the expansion ratio λ = 2, 3, 4, 5, 6, 8, 10, so N = 42. Note that the sampling has not been
performed directly on the Reynolds number due to its dependence on the contraction width. In
table 3, we report the critical Reynolds numbers for the symmetry breaking computed with the
RB method for diﬀerent values of the contraction width.
Table 3: Symmetry breaking Reynolds numbers as a function of the channel contraction width for
the 2D case with variable geometry.
λ
2
3
4
5
6
8
10
Re2D,sb
222.5
73.5
59.125
42.75
34.5
28.5
27.0
The same values in table 3 are plotted in ﬁgure 9. We clearly see that as the aspect ratio λ
decreases, the critical Reynolds number for the symmetry breaking increases, as observed also in
[24]. We see that Re2D,sb decreases fast for small values of λ, while it decreases mildly for λ ≥6
(also recall that for λ = 15.4 we found Re2D,sb ≈26). We remark that also in this case the results
match closely the ones in [24].
2
3
4
5
6
7
8
9
10
λ
0
50
100
150
200
250
Re
Figure 9: 2D case: value of the Reynolds number at the bifurcation point as a function of the
expansion ratio λ.
Let us analyze the computational time savings allowed by our RB method. Since we have
N = 42 with a 10h cputime needed per single run, the computational time analysis is given by:
Time to build the RB spaces + Online time to detect the bifurcation point
Time of the equivalent full order computation
= 42 · 10h + 2h + 7 · 0.08h
7 · 10h · 80
≃7.5%.
The ratio between a single online reduced order run and a single full order one are the same as
the one considered in the single parameter case (order 10−4). The break-even, comparing all the
19


## Page 20


oﬄine computational times needed to prepare the reduced basis problem (N = 42) and an online
query with full order model is:
All full order computations for RB prep.
Full order one query comp. time
= 42 · 10h + 2h
10h
≃42.2.
After 43 queries a reduced order computational model brings savings.
For λ = 6, which is one value among those listed in table 3, we plot in ﬁgure 10 the vertical
component of the velocity is taken on the horizontal axis, at distance 1 from the inlet, versus the
Reynolds number. This bifurcation diagram with both the stable and unstable solution branches
compares very well with the one in [24], but it has been obtained at a fraction of the computational
time as explained above.
Figure 10: Bifurcation diagram obtained with the Reduced Order Model for λ = 6: vertical
component of the velocity uy taken on the horizontal axis, at distance 1 from the inlet, versus the
Reynolds number.
Keeping λ = 6, we check how the ﬂow evolves as Re2D is pushed to a higher value, well beyond
the parameter range considered in this work. Fig. 11 reports the streamlines of both the unstable
and stable solution at Re2D = 600. The stable solution in Fig. 11(b) shows that the ﬂow structure
becomes more complex, with existing recirculations changing shape and growing in size. This is
consistent with the results presented in [24, 54].
(a) Unstable solution
(b) Stable solution
Figure 11: 2D case for λ = 6: streamlines for the (a) stable asymmetric and (b) unstable symmetric
solutions at Re2D = 600.
4.4
3D case
The three-dimensional channel in Fig. 3 has been obtained by extruding the two-dimensional
geometry in Fig. 2 along the z-axis. Thus, for the 3D case, we would have three parameters: the
Reynold number Re3D, the contraction width, and the channel depth. However, since we have
already investigated in Sec. 4.3 the inﬂuence of the expansion ratio (i.e., the contraction width)
on the critical Reynolds number for the symmetry breaking, we ﬁx the contraction width and
consider the Reynolds number and the channel depth as the only parameters.
20


## Page 21


We set the expansion ratio λ to 15.4, due to the richness of ﬂow patterns described in Sec. 4.1
and reference [52]. Of course, we expect the vortex structure to be much more complex than in
the 2D case. We are interested in understanding how varying the Reynolds number and the aspect
ratio AR (and thus H) aﬀects the ﬂow in the expansion channel. The goal of this section is to
evaluate the eﬀect of the walls on the bifurcating phenomenon. Intuitively, when the walls are
very far apart (large values of H), their inﬂuence on the central region of the channel will be quite
small, and the ﬂow pattern can be expected to be close to the 2D case. On the other hand, when
the walls are very close with respect to the channel height (small values of H), a relatively large
fraction of the sectional area will be occupied by low velocity ﬂuid. As a result, we can expect
that the bifurcation will take place at higher Reynolds numbers. As reported in tables 1 and 2,
we sample sample nine values for the Reynolds number in the interval Re2D ∈[0.01, 90] and eight
value of H. Notice that the eighth “value” of H in table 2 corresponds to the 2D case.
In order to show the sequence of events as the Reynolds number is increased when the aspect
ratio is ﬁxed, we set it to 1.6398 which corresponds to H = 0.6210. In Fig. 12, we display the
streamlines on the xy-plane for diﬀerent values of the Reynolds number Re3D. At Re3D = 0.01,
the 3D ﬂow looks similar to the 2D ﬂow: (compare Fig. 12(a) with Fig. 5(a)) but it features smaller
Moﬀatt eddies. As the Reynolds number increases, “lip vortices” form, as shown in Fig. 12(b).
This is in agreement with the observations in [52] and references therein.
The size of the lip
vortices increases as Re3D increases and once they reach the corner, the vortices continue to grow
in the downstream direction, i.e. along the x-axis. See Fig. 12(c), (d), and (e). By convention,
once they expand in the downstream direction they are called “corner vortices”. Notice that the
ﬂow downstream of the expansion is symmetric about the xz-plane up to Re3D = 76.821, while
asymmetries in 2D (i.e., for H = 1) arise around Re2D = 26.
Let us consider the geometry with H = 0.9517, which corresponds to the largest aspect ratio
among those in Table 2 for which we have an actual 3D geometry. We proceed with the computa-
tion of the symmetry breaking bifurcation point using the bifurcation detection method described
in section 3.5. Since H is ﬁxed, we consider a total of 9 basis functions for the online computation,
corresponding to the diﬀerent values of Reynolds number reported in table 2. In Fig. 13, we plot
the real part of the eigenvalue of matrix L in (41) responsible for the symmetry breaking. We see
that the curve crosses the horizontal axis at a Reynolds number of about 35. This coincides with
the critical value for the symmetry breaking reported by [52]. For the sake of completeness, in
ﬁgure 14 we report the path of all the eigenvalues in the complex plane.
For λ = 15.4, the critical Reynolds number for the symmetry breaking in the 2D geometry
(i.e., H = 1) found in Sec. 4.1 is Re2D,sb = 26. See Fig. 6. When H is decreased to 0.9517,
the critical Reynolds number for the symmetry breaking increases to Re3D,sb = 35, as shown in
Fig. 13. If H is further decreased to 0.6210, we saw in Fig. 12 that the ﬂow remains symmetric
up to Re3D = 76.821. As expected, at low values of H the proximity of vertical walls make the
ﬂow fully three-dimensional (instead of quasi-2D) inhibiting the symmetry breaking. Thus, as H
decreases Re3D,sb becomes larger and larger.
Next, we let both the geometric parameter H and the Reynolds number vary. We display in
ﬁgure 15 the streamlines on the xy-plane (left) and yz-plane for representative values of the two
parameters. For low values of H and Re3D, the ﬂow develops without forming vortices, with the
streamlines deviating only slightly out of plane. See Fig. 15(a) and (b), which have been obtained
for Re3D = 27.79 and H = 0.8165. As the channel increases in width, the streamlines gradually
become fully three-dimensional, especially in the vortex region. See Fig. 15(c) through (f). Notice
how Fig. 15(c) and (d), obtained for H = 0.9517 and Re3D = 27.79, diﬀer from Fig. 15(a) and (b),
obtained for the same Reynolds number but a smaller H. The corner vortices in Fig. 15(e) looks
similar to the recirculations observed in 2D (see, e.g., Fig. 5(b)). However, in a 3D geometry the
presence of a top and bottom bounding wall leads to complex 3D spiraling recirculation structures
[18, 66], as shown in Fig. 15(f). See also Fig. 15(g) and (h).
Fig. 16 shows that streamlines on the xy-plane and yz-plane of both the unstable (symmetric)
and the stable (asymmetric) solution for a value of the Reynolds number (Re3D = 76.82) past
the bifurcation point, the usual expansion ratio λ = 15.4, and H = 0.9517. The vortex pattern
becomes even more intricate after the bifurcation point, with the vortices promoting the mixing
21


## Page 22


(a) Re3D = 0.01
(b) Re3D = 27.786
(c) Re3D = 45.005
(d) Re3D = 62.224
(e) Re3D = 76.821
Figure 12: 3D case for λ = 15.4 and H = 0.6210: streamlines on the xy-plane (see ﬁgure 3) for (a)
Re3D = 0.01, (b) Re3D = 27.786, (c) Re3D = 45.005, (d) Re3D = 62.224, and (e) Re3D = 76.821.
Figure 13: 3D case for λ = 15.4 and H = 0.9517: real part of the eigenvalue of matrix L in (41)
responsible for the symmetry breaking as a function of the Reynolds number in a neighborhood
of a bifurcation point.
between distant regions of the channel. Due to the symmetry of the geometry and the boundary
conditions, there is no ﬂow crossing the midline xy plane.
22


## Page 23


(a) eigenvalues of matrix L
(b) zoomed-in view of (a)
(c) zoomed-in view of (b)
Figure 14: 3D case for λ = 15.4 and H = 0.9517: (a) path of the eigenvalues of matrix L in (41)
in the complex plane for Re3D ∈[0.01, 90]. Subﬁgure (b) is a zoomed-in views of subﬁgure (a)
and subﬁgure (c) is a zoomed-in views of subﬁgure (b). The arrows indicate the direction of the
increasing Reynolds numbers. The eigenvalue in red on the real axis in (c) is responsible for the
bifurcation point.
Each 3D full order computation requires about 240h of CPU time, and the preprocessing time
is about 40h. The computational time savings estimate for the two parameter (Re and H) case is
given by:
time to build the RB spaces + online time to detect the bifurcation point
time of the equivalent full order computation
= 56 · 240h + 40h + 0.05h
7 · 7 · 10 · 240h
≃11.4%.
where, based on the experience acquired with the 2D case, we suppose that 7 runs per each param-
eter are required to have a reasonable tracking of the bifurcation points in the parameter space.
With 2 parameters this amounts to 49 runs, each run requiring on average 10 full simulations.
Thus, in the 3D case the break-even is given by:
All full order computations for RB prep.
Full order one query comp. time
= 56 · 240h + 40h
240h
≃56.2.
The interpretation of this result is that a reduced order model can be expected to bring savings if
more than 56 runs are planned.
To test our method, we select a geometric aspect ratio not considered in the sampling phase,
and we try to recover some characterizing ﬂow features as a function of the Reynolds number. We
23


## Page 24


(a) Re3D = 27.79, H = 0.8165, xy-plane
(b) Re3D = 27.79, H = 0.8165, yz-plane
(c) Re3D = 27.79, H = 0.9517, xy-plane
(d) Re3D = 27.79, H = 0.9517, yz-plane
(e) Re3D = 45.01, H = 0.9517, xy-plane
(f) Re3D = 45.01, H = 0.9517, yz-plane
(g) Re3D = 62.22, H = 0.8165, xy-plane
(h) Re3D = 62.22, H = 0.8165, yz-plane
Figure 15: 3D case for λ = 15.4: streamlines on the xy-plane (left) and yz-plane (right) and
(a) and (b) H = 0.8165, Re3D = 27.79, (c) and (d) H = 0.9517, Re3D = 27.79, (e) and (f)
H = 0.9517, Re3D = 45.01, (g) and (h) H = 0.8165, Re3D = 62.22.
The projection on the
yz-plane for symmetry reasons shows only half of the geometry.
consider AR = 2.12 (corresponding to H = 0.679) and we reconstruct the proﬁle of the normalized
axial velocity:
vx
⟨vx⟩c
= vx
R
Ω∩Πc vx dx
|Ω∩Πc|
,
(45)
where Πc is any plane crossing the contraction section and orthogonal to the channel axis and
|Ω∩Πc| is the measure of the intersection between the plane Πc and the domain Ω. We also
24


## Page 25


(a) xy-plane, unstable solution
(b) yz-plane, unstable solution
(c) xy-plane, stable solution
(d) yz-plane, stable solution
Figure 16: 3D case for λ = 15.4, H = 0.9517, and Re3D = 76.82: streamlines on the xy-plane (left)
and yz-plane (right) for (a) and (b) unstable solution, (c) and (d) stable solution. The projection
on the yz-plane for symmetry reasons shows only half of the geometry.
consider the normalized axial velocity gradient:
∂xvx
⟨vx⟩c
wc.
(46)
We plot the normalized axial velocity (45) and normalized axial gradient (46) along the center
line for diﬀerent values of the Reynolds number in ﬁgure 17(a) and (b), respectively. The results
are in good qualitative agreement with those reported in [52]. Concerning the normalized axial
velocity, for small Reynolds numbers the curve is almost a symmetric step function, since the
viscosity is suﬃciently high to avoid large velocity gradients both inside the cross-section and
along the channel length. As the Reynolds number is increased, the curve becomes more and
more asymmetric, and the averaging eﬀect of the viscosity takes longer to smooth out the velocity
gradients. This is visible from the long tail of the curves with higher Reynolds number. The
viscosity has also a clear eﬀect on the normalized axial gradient in Fig. 17(b): the two spikes
show that the velocity gradients in proximity of the variations in channel width increase as the
Reynolds number increases. We remark that the graphs in ﬁgure 17 can be easily drawn by saving
the normalized axial velocity and normalized axial gradient for the RB functions and using these
as to interpolate the desired output in real time. This feature is particularly interesting in the
real-time query case, since it does not need to search a large database during the postprocessing
phase.
We conclude the section with the streamlines for the ﬂow associated to H = 0.2085 (in Fig. 18),
H = 0.6210 (in Fig. 19), and H = 0.9517 (in Fig. 20) for a small value, a medium value, and a
large of Re3D ∈[0.01, 90]. In particular, compare the solutions for Re3D = 90 (leftmost panel in
Fig. 18, 19, and 20). They clearly show that at low values of H the symmetry breaking bifurcation
is pushed to higher values of Re3D due the vertical walls.
Based on the results presented in Sec. 4.3 and 4.4, we conclude that eccentric mitral regur-
gitant jets are produced by long (large H) and narrow (large λ) oriﬁces. In fact, such slender
oriﬁces associated with eccentric jets, seem to resemble the coaptation geometry of the mitral
valve. Coaptation is the region where the two leaﬂets of the mitral valve meet Our hypothesis is
25


## Page 26


Figure 17: 3D case for λ = 15.4 and H = 0.9517: normalized axial velocity (45) and normalized
axial gradient (46) as a function of the normalized distance from the contraction inlet. The curves
in the two ﬁgures are computed for values of the Reynolds number between 0.01 and 90. The
diﬀerent curves refer to the values of Reynolds number reported in the legend.
Figure 18: 3D case for λ = 15.4 and H = 0.2085 streamlines for Re3D = 0.01 (left), Re3D = 23
(center), and Re3D = 90 (right).
Figure 19: 3D case for λ = 15.4 and H = 0.6210: streamlines for Re3D = 0.01 (left), (b) Re3D = 13
(center), and Re3D = 90 (right).
Figure 20: 3D case for λ = 15.4 and H = 0.9517: streamlines for Re3D = 4.466 (left), Re3D = 27
(center), and Re3D = 90 (right).
that Coanda eﬀect occurs in mitral valves in which the leakage, i.e., regurgitation, occurs along a
26


## Page 27


large section of the coaptation zone, rather than at an isolated point, leading to a possibly signif-
icant regurgitant volume. This is corroborated by clinical observations indicating that eccentric
regurgitant jets are, indeed, prevalent in patients with severe MR [43, 15, 62].
Before the study presented in this manuscript, our collaborators at the Houston Methodist
DeBakey Heart & Vascular Center had never succeeded in reproducing the Coanda eﬀect in vitro.
Following our results, they designed a long and narrow oriﬁce in a divider plate that mimics a
closed leaky mitral valve. A close-up view of the oriﬁce is in Fig. 21(a). The divider plate was
mounted on an anatomically correct mock (left) heart chamber developed to study the use of
2D and 3D color Doppler techniques in imaging the clinically relevant intra-cardiac ﬂow events
associated with regurgitant jets [44, 42]. See Figure 21(b). The chamber is connected to a pulsatile
ﬂow loop. The ﬂuid in the mock heart chamber is water with 30% glycerin added to mimic blood
viscosity. Notice that this is consistent with modeling blood as a Newtonian ﬂuid in Sec. 2. From
the 2D Doppler echocardiographic image in Fig. 21(c) we see that indeed the slender oriﬁce in
Fig. 21(a) generates a regurgitant jet that hugs the wall. See also [69]. We expect also that these
studies could enhance in the near future in vivo studies and applications.
(a) 3D printed plate with ori-
ﬁce
(b) Mock heart chamber
(c) Mock heart chamber
Figure 21:
(a) Close-up view of the 3D printed divider plate with a long and narrow oriﬁce to
mimic a closed leaky mitral valve, (b) geometry of the mock heart chamber with the divider plate
between mock left ventricle and mock left atrium (LA), and (c) 2D Doppler echocardiographic
image of the regurgitant jet in the mock heart chamber. Conic distortion in (c) occurs due to the
use of convex array transducer.
5
Conclusions and perspectives
The symmetry breaking bifurcation (Coanda eﬀect) has been studied in parametric ﬂows, rep-
resenting a simpliﬁed test case for regurgitant mitral valve ﬂows. Our preliminary work shows
that standard reduced order methods (e.g., Reduced Basis and /or Proper Orthogonal Decompo-
sition) allow to capture complex physical and mathematical phenomena, such as bifurcations in
the parametrized Navier-Stokes equations, at a fraction of the computational cost required by full
order order methods. In order to detect the bifurcation points, the reduced parametric Navier-
Stokes equations have been supplemented with a generalized eigenvalue problem, also cast into
the reduced order setting. This work is also an example of computational collaboration between
high performance computing and reduced order methods: thanks to the computational gains with
the same resources we can treat more complex problems. This computational collaboration has
demonstrated the ability to provide reliable and accurate results with signiﬁcant reduction of com-
putational times. Results have been validated both with the full-order model and by comparison
with parametric studies available in literature for both 2D and 3D cases.
Research perspectives in this ﬁeld include the development of proper error bounds for the
detection of the bifurcation points and the veriﬁcation of the accuracy. At the state of the art this
aspect is carried out by supplementing the state equation with a generalized eigenvalue problem,
solved with the same reduced order method proposed for the state equation. Moreover, we plan
on taking into account the interaction of the ﬂuid with elastic walls (i.e., elastic valve leaﬂet) [5].
27


## Page 28


This would lead to important improvements in the study of this complex multiphysics nonlinear
problem and a better understanding of how the Coanda eﬀect is inﬂuenced by the valve elasticity.
6
Acknowledgements
The authors want to thank Prof.
S. Canic, Prof.
R. Glowinski (University of Houston) and
S. Little MD (The Methodist Hospital, Houston) for the fruitful discussions.
The research in
this work has been partially supported by the National Science Foundation under grants DMS-
1620384, DMS-1263572 and DMS-1109189 (Quaini), INDAM-GNCS 2015 project “Computational
Reduction Strategies for CFD and Fluid-Structure Interaction Problems”, by the INDAM-GNCS
2016 projects “Tecniche di riduzione della complessit`a computazionale per le scienze applicate”,
by PRIN project “Mathematical and numerical modeling of the cardiovascular system, and their
clinical applications”, and by European Union Funding for Research and Innovation – Horizon
2020 Program – in the framework of European Research Council Executive Agency: H2020 ERC
CoG 2015 AROMA-CFD project 681447 “Advanced Reduced Order Methods with Applications
in Computational Fluid Dynamics”. Computations have been performed on the SISSA cluster
Ulysses and on the CINECA clusters (COGESTRA project 2015).
References
[1]
J. Albers et al. “Regurgitant Jet Evaluation Using Three-Dimensional Echocardiography
and Magnetic Resonance”. In: Ann Thorac Surg 78 (2004), pp. 96–102.
[2]
A. Ambrosetti and G. Prodi. A Primer of Nonlinear Analysis. Cambridge: Cambridge Uni-
versity Press, 1993.
[3]
F. Auteri, N. Parolini, and L. Quartapelle. “Numerical investigation on the stability of
singular driven cavity ﬂow”. In: Journal of Computational Physics 183 (2002), pp. 1–25.
[4]
I. Babuska. “The ﬁnite element method with Lagrangian multipliers”. In: Numerische Math-
ematik 20 (1973), pp. 179–192.
[5]
F. Ballarin and G. Rozza. “POD-Galerkin monolithic reduced order models for parametrized
ﬂuid-structure interaction problems”. In: International Journal for Numerical Methods in
Fluids 82.12 (2016), pp. 1010–1034.
[6]
Francesco Ballarin et al. “Supremizer stabilization of POD–Galerkin approximation of parametrized
steady incompressible Navier–Stokes equations”. In: International Journal for Numerical
Methods in Engineering 102.5 (2015), pp. 1136–1161.
[7]
M. Barrault et al. “An “empirical interpolation method”: application to eﬃcient reduced-
basis discretization of partial diﬀerential equations”. In: C. R. Acad. Sci. Paris, Ser. I 339
(2004), pp. 667–672.
[8]
F. Battaglia et al. “Bifurcation of low Reynolds number ﬂows in symmetric channels”. In:
AIAA J. 35 (1997), pp. 99–105.
[9]
D. Boﬃ, F. Brezzi, and M. Fortin. Mixed Finite Element Methods and Applications. Vol. 44.
Springer Series in Computational Mathematics. Heidelberg: Springer, 2013.
[10]
J.P. Boyd. Chebyshev and Fourier Spectral Methods. Dover Publications, 2001.
[11]
F. Brezzi. “On the existence, uniqueness and approximation of saddle point problems arising
from Lagrange multipliers”. In: RAIRO Anal. Numer. 8 (1974), pp. 129–151.
[12]
A. Caiazzo et al. “A numerical investigation of velocity–pressure reduced order models for
incompressible ﬂows”. In: Journal of Computational Physics 259 (2014), pp. 598–616.
[13]
C. Canuto et al. Spectral Methods Evolution to Complex Geometries and Applications to
Fluid Dynamics. Scientiﬁc Computation. Springer, 2007.
28


## Page 29


[14]
C. Canuto et al. Spectral Methods Fundamentals in Single Domains. Scientiﬁc Computation.
Springer, 2006.
[15]
Sonal Chandra et al. “A three-dimensional insight into the complexity of ﬂow convergence in
mitral regurgitation: adjunctive beneﬁt of anatomic regurgitant oriﬁce area”. In: American
Journal of Physiology-Heart and Circulatory Physiology 301.3 (2011), H1015–H1024.
[16]
K. Chao et al. “Inﬂuence of the Coanda eﬀect on color Doppler jet area and color encoding”.
In: Circulation 85 (1992), pp. 333–341.
[17]
W. Cherdron, F. Durst, and J.H. Whitelaw. “Asymmetric ﬂows and instabilities in symmetric
ducts with sudden expansions”. In: J. Fluid Mech. 84 (1978), pp. 13–31.
[18]
T.P. Chiang, Tony W.H. Sheu, and S.K. Wang. “Side wall eﬀects on the structure of laminar
ﬂow over a plane-symmetric sudden expansion”. In: Computers & Fluids 29.5 (2000), pp. 467
–492.
[19]
Francisco Chinesta et al. “Model Order Reduction”. Encyclopedia of Computational Me-
chanics 2016, in press, Elsevier.
[20]
K.A. Cliﬀe, A. Spence, and S.J. Tavener. “The numerical analysis of bifurcation problems
with application to ﬂuid mechanics”. In: Acta Numerica 9 (2000), pp. 39–131.
[21]
K.A. Cliﬀe et al. “Adaptivity and a Posteriori Error Control for Bifurcation Problems III:
Incompressible Fluid Flow in Open Systems with O(2) Symmetry”. In: Journal of Scientiﬁc
Computing 52.1 (2012), pp. 153–179.
[22]
M.O. Deville, P.F. Fischer, and E.H. Mund. High-Order Methods for Incompressible Fluid
Flow. Cambridge Monographs on Applied and Computational Mathematics. Cambridge:
Cambridge University Press, 2002.
[23]
H.A. Dijkstra et al. “Numerical Bifurcation Methods and their Application to Fluid Dy-
namics: Analysis beyond Simulation”. In: Communications in Computational Physics 15.1
(2014), pp. 1–45.
[24]
D. Drikakis. “Bifurcation phenomena in incompressible sudden expansion ﬂows”. In: Physics
of Fluids 9 (1 1997), pp. 76–87.
[25]
A. Ern and J.-L. Guermond. Theory and Practice of Finite Elements. New York: Springer-
Verlag, 2004.
[26]
R.M. Fearn, T. Mullin, and K.A. Cliﬀe. “Nonlinear ﬂow phenomena in a symmetric sudden
expansion”. In: J. Fluid Mech. 211 (1990), pp. 595–608.
[27]
P.F. Fischer, J.W. Lottes, and S.G. Kerkemeier. Nek5000 Web page. http://nek5000.mcs.anl.gov.
2008.
[28]
C. Foias et al. Navier—Stokes Equations and Turbulence. Vol. 83. Encyclopedia of Mathe-
matics and its Applications. Cambridge: Cambridge University Press, 2001.
[29]
L. Formaggia, A. Quarteroni, and A. Veneziani. Cardiovascular Mathematics. Vol. 1. Mod-
eling, Simulation and Applications. Springer, 2009.
[30]
G.P. Galdi. “Navier-Stokes Equations: a Mathematical Analysis”. In: Mathematics of Com-
plexity and Dynamical Systems. Ed. by R.A. Meyers. Springer, 2011, pp. 1009–1042.
[31]
C. Ginghina. “The Coanda eﬀect in cardiology”. In: J. Cardiovasc. Med. 8 (2007), pp. 411–
413.
[32]
G.H. Golub and C.F. Van Loan. Matrix Computations. Johns Hopkins University Press,
2012.
[33]
J.W. Goodrich, K. Gustafson, and K. Halasi. “Hopf bifurcation in the driven cavity”. In:
Journal of Computational Physics 90 (1990), pp. 219–261.
[34]
Nils Gr¨abner et al. “Numerical methods for parametric model reduction in the simulation of
disk brake squeal”. In: ZAMM - Journal of Applied Mathematics and Mechanics / Zeitschrift
fr Angewandte Mathematik und Mechanik (2016). doi: 10.1002/zamm.201500217.
29


## Page 30


[35]
Max D. Gunzburger. Perspectives in Flow Control and Optimization. SIAM, 2003.
[36]
T. Hawa and Z. Rusak. “The dynamics of a laminar ﬂow in a symmetric channel with a
sudden expansion”. In: J. Fluid Mech. 436 (2001), pp. 283–320.
[37]
H. Herrero, Y. Maday, and F. Pla. “RB (Reduced Basis) for RB (Rayleigh-B´enard)”. In:
Computer Methods in Applied Mechanics and Engineering 261-262 (2013), pp. 132–141.
[38]
Jan S Hesthaven, Gianluigi Rozza, and Benjamin Stamm. Certiﬁed Reduced Basis Methods
for Parametrized Partial Diﬀerential Equations. Springer Briefs in Mathematics, 2015.
[39]
O. Ladyzhenskaya. The Mathematical Theory of Viscous Incompressible Flow. Gordon and
Breach, New York, 1969.
[40]
T. Lassila et al. “Model order reduction in ﬂuid dynamics: challenges and perspectives”. In:
Reduced Order Methods for modeling and computational reduction. Ed. by A. Quarteroni and
G. Rozza. Vol. 9. Modeling, Simulation and Applications. Milano: Springer, 2014. Chap. 9,
pp. 235–273.
[41]
Eric Lauga, Abraham D. Stroock, and Howard A. Stone. “Three-dimensional ﬂows in slowly
varying planar geometries”. In: Physics of Fluids 16.8 (2004), pp. 3051–3062.
[42]
S. H. Little et al. “In vitro validation of real-time three-dimensional color Doppler echocardio-
graphy for direct measurment of Proximal Isovelocity Surface Area in mitral rigurgitation”.
In: Am. J. Cardiol. 99.10 (2007), pp. 1440–1447.
[43]
S. H. Little et al. “Three-Dimensional Color Doppler Echocardiography for Direct Mea-
surement of Vena Contracta Area in Mitral Regurgitation: In Vitro Validation and Clinical
Experience”. In: JACC: Cardiovascular Imaging 1.6 (2008), pp. 695–704.
[44]
S. H. Little et al. “Three-dimensional ultrasound imaging model of mitral valve regurgitation:
design and evaluation”. In: Ultrasound in Med. & Biol. 34.4 (2008), pp. 647–654.
[45]
S. Lorenzi et al. “POD-Galerkin method for ﬁnite volume approximation of Navier-Stokes
and RANS equations”. In: Computer Methods in Applied Mechanics and Engineering 311
(2016), 151–179.
[46]
A.M. Lovgren, Y. Maday, and E.M. Ronquist. “A reduced basis element method for the
steady Stokes problem”. In: ESAIM: Mathematical Modelling and Numerical Analysis 40.3
(2006), pp. 529–552.
[47]
Volker Mehrmann and Christian Schroder. “Eigenvalue analysis and model reduction in the
treatment of disc brake squeal”. In: SIAM News 49.1 (2016), pp. 1–3.
[48]
S. Mishra and K. Jayaraman. “Asymmetric ﬂows in planar symmetric channels with large
expansion ratios”. In: Int. J. Num. Meth. Fluids 38 (2002), pp. 945–962.
[49]
H.K. Moﬀatt. “Viscous and resistive eddies near a sharp corner”. In: J. Fluid Mech. 18
(1964), pp. 1–18.
[50]
Nek5000 documentation. https://nek5000.mcs.anl.gov/ﬁles/2015/09/NEK doc.pdf. 2015.
[51]
N. C. Nguyen, K. Veroy, and A. T. Patera. “Certiﬁed Real-Time Solution of Parametrized
Partial Diﬀerential Equations”. In: Handbook of Materials Modeling. Ed. by S. Yip. Springer,
2005, pp. 1523–1558.
[52]
M.S.N. Oliveira et al. “Simulations of extensional ﬂow in microrheometric devices”. In:
Microﬂuid Nanoﬂuid 5 (2008), pp. 809–826.
[53]
Giuseppe Pitton and Gianluigi Rozza. “A reduced basis method for bifurcation problems in
incompressible ﬂuid dynamics”. In: Submitted. SISSA preprint 55/2015/MATE (2015).
[54]
A. Quaini, R. Glowinski, and S. Canic. “Symmetry breaking and preliminary results about a
Hopf bifurcation for incompressible viscous ﬂow in an expansion channel”. In: International
Journal of Computational Fluid Dynamics 30.1 (2016), pp. 7–19.
[55]
A. Quarteroni and G. Rozza. Reduced Order Methods for Modeling and Computational Re-
duction. Vol. 9. Springer Milano, MS&A Series, 2014.
30


## Page 31


[56]
Alﬁo Quarteroni, Andrea Manzoni, and Federico Negri. Reduced Basis Methods for Partial
Diﬀerential Equations. Vol. 92. UNITEXT. Springer, 2016.
[57]
A. Revuelta. “On the two-dimensional ﬂow in a sudden expansion with large expansion
ratios”. In: Phys. Fluids 17.1 (2005), pp. 1–4.
[58]
G. Rozza, D.B.P. Huynh, and A. Manzoni. “Reduced basis approximation and a posteriori
error estimation for Stokes ﬂows in parametrized geometries: roles of the inf-sup stability
constants”. In: Numer. Math. 125.1 (2013), pp. 115–152.
[59]
G. Rozza, D.B.P. Huynh, and A.T. Patera. “Reduced Basis Approximation and a Posteriori
Error Estimation for Aﬃnely Parametrized Elliptic Coercive Partial Diﬀerential Equations”.
In: Archives of Computational Methods in Engineering 15.3 (2008), pp. 229–275.
[60]
G. Rozza and K. Veroy. “On the stability of the reduced basis method for Stokes equations
on parametrized domains”. In: Computer methods in applied mechanics and engineering 196
(2007), pp. 1244–1260.
[61]
Y. Saad. Numerical Methods for Large Eigenvalue Problems, Revised Edition. Vol. 66. Clas-
sics in Applied Mathematics. SIAM, 2011.
[62]
Miriam Shanks et al. “Quantitative assessment of mitral regurgitation comparison between
three-dimensional transesophageal echocardiography and magnetic resonance imaging”. In:
Circulation: Cardiovascular Imaging 3.6 (2010), pp. 694–700.
[63]
I.J. Sobey and P.G. Drazin. “Bifurcations of two-dimensional channel ﬂows”. In: J. Fluid
Mech. 171 (1986), pp. 263–287.
[64]
F. Terragni and J.M. Vega. “On the use of POD-based ROMs to analyze bifurcations in some
dissipative systems”. In: Physica D: Nonlinear Phenomena 241.17 (2012), pp. 1393–1405.
[65]
D.J. Tritton. Physical Fluid Dynamics, Section 22.7: The Coanda Eﬀect. Van Nostrand
Reinhold, 1977 (reprinted 1980).
[66]
Chien-Hsiung Tsai et al. “Capabilities and limitations of 2-dimensional and 3-dimensional
numerical methods in modeling the ﬂuid ﬂow in sudden expansion microchannels”. In: Mi-
croﬂuidics and Nanoﬂuidics 3.1 (2007), pp. 13–18. issn: 1613-4982.
[67]
M. Vermeulen et al. “In Vitro Flow Modelling for Mitral Valve Leakage Quantiﬁcation”. In:
Proc. 8th Int. Symp. Particle Image Velocimetry. Melbourne Australia, 2009, p. 4.
[68]
S. Volkwein. “Proper Orthogonal Decomposition: Theory and Reduced-Order Modelling”.
In: Lecture Notes. University of Konstanz, Department of Mathematics and Statistics, 2013.
[69]
Y. Wang et al. “3D experimental and computational analysis of eccentric mitral regurgitant
jets in a mock imaging heart chamber”. In: Submitted. NA & SC Preprint series n. 55,
Department of Mathematics, University of Houston (2016).
[70]
R. Wille and H. Fernholz. “Report on the ﬁrst European mechanics colloquium on Coanda
eﬀect”. In: J. Fluid Mech. 23 (1965), pp. 801–819.
[71]
D. Xiu and J.S. Hesthaven. “High-Order Collocation Methods for Diﬀerential Equations with
Random Inputs”. In: SIAM Journal on Scientiﬁc Computing 27 (3 2005), pp. 1118–1139.
[72]
M. Yano and A.T. Patera. “A space-time variational approach to hydrodynamic stability
theory”. In: Proceedings of the Royal Society A 496.2155 (2013).
[73]
W.A. Zoghbi et al. “American Society of Echocardiography: Recommendations for eval-
uation of the severity of native valvular regurgitation with two-dimensional and Doppler
echocardiography.” In: Eur. J. Echocardiogr. 4 (2003), pp. 237–261.
31

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
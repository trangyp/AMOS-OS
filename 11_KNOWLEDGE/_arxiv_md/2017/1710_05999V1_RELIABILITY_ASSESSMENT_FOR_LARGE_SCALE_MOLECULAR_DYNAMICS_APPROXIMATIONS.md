---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1710.05999v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1710.05999v1_Reliability_Assessment_for_Large-Scale_Molecular_Dynamics_Approximations

> Source: 1710.05999v1_Reliability_Assessment_for_Large-Scale_Molecular_Dynamics_Approximations.pdf

> Pages: 16

---


## Page 1


arXiv:1710.05999v1  [math.NA]  16 Oct 2017
Reliability Assessment for Large-Scale Molecular Dynamics Approximations
Francesca Grogan,1, a) Michael Holst,1, 2, b) Lee Lindblom,1, 2, c) and Rommie Amaro3, d)
1)Center for Computational Mathematics, Department of Mathematics, University of California at San Diego,
La Jolla, CA 92093, USA
2)Center for Astrophysics and Space Sciences, University of California at San Diego, La Jolla, CA 92093,
USA
3)Department of Chemistry and Biochemistry, University of California at San Diego, La Jolla, CA 92093,
USA
(Dated: 11 July 2018)
Molecular dynamics (MD) simulations are used in biochemistry, physics, and other ﬁelds to study the mo-
tions, thermodynamic properties, and the interactions between molecules. Computational limitations and the
complexity of these problems, however, create the need for approximations to the standard MD methods and
for uncertainty quantiﬁcation and reliability assessment of those approximations. In this paper, we exploit the
intrinsic two-scale nature of MD to construct a class of large-scale dynamics approximations. The reliability
of these methods are evaluated here by measuring the diﬀerences between full, classical MD simulations and
those based on these large-scale approximations. Molecular dynamics evolutions are non-linear and chaotic,
so the complete details of molecular evolutions cannot be accurately predicted even using full, classical MD
simulations. This paper provides numerical results that demonstrate the existence of computationally eﬃcient
large-scale MD approximations which accurately model certain large-scale properties of the molecules: the
energy, the linear and angular momenta, and other macroscopic features of molecular motions.
PACS numbers: 83.10.Mj, 83.10.Rs, 87.10.Tf, 87.15.ap
Keywords: molecular dynamics, uncertainty quantiﬁcation, numerical methods, normal modes
I.
INTRODUCTION
Traditional molecular dynamics (MD) simulations use
Newton’s classical equations of motion, with an eﬀective
potential that models the interactions between atoms,
to describe the evolution of molecules.1–3 This standard
MD method has been applied to a variety of problems
in biochemistry and condensed matter physics in recent
years.4–11
The results obtained from these MD simulations can
be characterized, qualitatively, as the evolution of the
overall position and orientation of each molecule, plus vi-
brations of the individual atoms about their average po-
sitions within each molecule. The timescales associated
with the macroscopic bulk motions of the molecules are
typically much longer than the timescales associated with
the internal atomic vibrations. However, these very short
timescale vibrations determine the maximum timesteps
allowed for accurate solutions of the classical MD evolu-
tion equations using standard numerical methods. This
fundamental fact, together with the need to simulate ex-
tremely large complex molecules in modern biochemical
research, means the computational cost of performing
MD simulations can be prohibitively large.
Computa-
tional cost is therefore one of the factors that drives the
need to develop approximation methods capable of ob-
a)Electronic mail: fgrogan@ucsd.edu
b)Electronic mail: mholst@ucsd.edu
c)Electronic mail: llindblom@ucsd.edu
d)Electronic mail: ramaro@ucsd.edu
taining reliable simulations of those aspects of the molec-
ular systems of primary interest to researchers.
Another factor that motivates the development of ap-
proximation methods for MD simulations is the well-
known fact that typical n-body systems exhibit chaotic
behavior in which exponentially divergent evolutions re-
sult from small perturbations of initial conditions.12 It
is simply impossible, and therefore pointless to attempt,
to simulate all the details in the evolutions of complex
molecular systems. Many large-scale properties of such
systems, including statistical time averages of various
properties, are nevertheless well deﬁned2,13,14 and these
properties are therefore in principle observable and sim-
ulatable. These macroscopic characteristics include the
positions, average velocities, and other time averages of
thermodynamic quantities.
Given these two motivating factors—the need for
greater computational eﬃciency and the fundamental in-
ability to simulate chaotic dynamics in complete micro-
scopic detail—we have developed a new class of large
scale MD approximations. We construct these approx-
imations by starting with a new representation of the
exact traditional MD equations of motion. The standard
MD equations generally use the Cartesian coordinates
of the location of each atom as the primary dynamical
variables. We transform these Cartesian variables into a
new representation that separates the macroscopic loca-
tion and orientation of each molecule, from the internal
degrees of freedom that represent the molecular vibra-
tions. This transformation is (loosely) motivated by Wil-
son’s representation of the internal degrees of freedom of
a molecule by normal modes.15 Our approach diﬀers from
Wilson’s, however, by providing an exact representation


## Page 2


2
of the molecular motions even when the mode amplitudes
are not small. We test this new mode-basis description
of MD by comparing the results of numerical simulations
using it with those based on the standard classical MD
equations. The results of these numerical tests, described
in more detail in Sec. III B, conﬁrm that our new mode-
basis representation of MD is exact.
In our mode-basis representation of MD, the large-
scale degrees of freedom are cleanly separated from the
collection of mode amplitudes that describe the inter-
nal vibration degrees of freedom of the molecule. It is
straightforward to replace the exact equations that deter-
mine the evolution of these mode amplitudes, with vari-
ous approximate expressions. For example the mode am-
plitudes could be chosen to satisfy the analytic sinusoidal-
in-time expressions derived from the small-amplitude
normal-mode equations.
Another possibility would be
to use the normal-mode sinusoidal-in-time expressions
for some number of the highest frequency modes, while
evolving the remaining lower frequency mode amplitudes
numerically using the exact evolution equations. This ap-
proach would be qualitatively similar to that used in the
constraint algorithms like SHAKE and RATTLE.16,17
Another possibility would simply be to ignore the inter-
nal degrees of freedom of the atoms completely by setting
the mode amplitudes equal to zero, i.e. to their expected
long timescale averages. We present numerical tests that
compare diﬀerent approximations of this type with the
results of the exact MD evolutions. The results of these
numerical tests are described in more detail in Sec. III C.
We assess the reliability of our new large-scale approx-
imation methods by applying the techniques of uncer-
tainty quantiﬁcation (UQ).18–22 Here we focus attention
on measuring the accuracy of our new large-scale approxi-
mation methods by comparing them to standard classical
MD, setting aside other important issues such as time-
stepper integration errors, errors in the molecular inter-
action potential model, errors that arise from the use of
classical rather than a fully quantum description of MD,
etc. The MD evolution equations are highly non-linear,
as are the equations for our large-scale approximations.
It is possible to derive rigorous analytic mathematical
bounds on the errors in our large-scale approximation
methods.23 However the bounds we have obtained in this
way are quite weak, and do not provide a good estimate
of the size of the actual large-scale approximation errors
in practical simulations. Therefore we focus the discus-
sion of our UQ analysis in this paper on making detailed
numerical comparisons between full classical MD simula-
tions and those obtained for identical molecular systems
using our new large-scale approximations.
Since MD simulations are typically performed to es-
timate the values of various macroscopic observables of
the molecules, we have focused our uncertainty quantiﬁ-
cation analysis on assessing the errors in the large-scale
approximation values of those quantities. In particular
we evaluate the errors in the energy, the linear and angu-
lar momenta, and the errors in the positions and orienta-
tions of each molecule. Our numerical results show that
all the large-scale approximations tested here are linear
momentum conserving, and consequently the positions
and velocities of the molecular centers of mass are also
determined exactly. Some of our large-scale approxima-
tions tested here also conserve energy and angular mo-
mentum exactly. Angular momentum conservation does
not, however, guarantee that the orientations or angular
velocities of the molecules are determined accurately. We
show that these orientation features evolve chaotically in
MD systems, and are therefore unpredictable even in full
classical MD simulations.
The remainder of this paper is organized as follows.
In Sec. II, we derive a new mode-basis representation
of the molecular dynamics evolution equations, and then
use them to derive several large-scale molecular dynamics
approximations. We have implemented these equations
in a numerical MD evolution code and have used this
code to evolve simple models of several of the smaller
fullerene molecules: C20, C26, C60 and C70. In Sec. III
we discuss the results of our numerical simulations of
these molecules using both standard classical MD and
several large-scale approximations, highlighting the un-
certainty quantiﬁcation of the macroscopic properties of
these molecules. We conclude by summarizing and dis-
cussing our results brieﬂy in Sec. IV.
II.
CLASSICAL MOLECULAR DYNAMICS
Classical molecular dynamics (MD) uses Newton’s
equations to describe the motions of the atoms (repre-
sented as point particles) that make up the molecules
being studied.
We use the notation ⃗xA(t) to denote
the Cartesian coordinates of the location of atom A as
a function of time. The classical MD equations of mo-
tion for the atoms that make up a molecule (or collection
of molecules) are therefore given by
mA
d 2⃗xA
dt2
= −∂U(⃗xB)
∂⃗xA
,
(1)
where mA is the mass of atom A and U(⃗xB) is the ef-
fective potential energy function that describes the in-
teractions between the atoms. This potential energy will
in general be a non-linear function of the locations of
all of the atoms. Consequently the MD evolution equa-
tions, Eq. (1), are non-linear and strongly coupled. The
solutions to these equations therefore display the typi-
cal characteristics of chaotic n-body systems,2,13,14 i.e.
while most details of the evolution of a particular initial
molecular state cannot be predicted, certain “statistical”
features of the evolution can.
In this section we develop a new class of large-scale
approximations to the classical MD equations of mo-
tion, Eq. (1). These new approximations are designed
to provide a more eﬃcient way to evaluate some of the
observable “statistical” or “thermodynamic” features of


## Page 3


3
MD systems. We construct these approximations in two
steps. In the ﬁrst step, in Sec. II A, we transform the
exact classical MD equations into a representation that
cleanly separates some of the observable macroscopic de-
grees of freedom of a molecule from the internal de-
grees of freedom that determine its microscopic state.
We refer to this new representation of the MD equa-
tions as a mode-basis representation, because the choice
of variables used to describe the microscopic state of a
molecule is based (loosely) on the normal-mode descrip-
tion of molecular vibrations.15,24 The transformation we
use to construct this mode-basis representation is exact,
however, so it is simply a change of variables for the clas-
sical MD system given in Eq. (1). We present the exact
MD equations of motion for the mode-basis representa-
tion in Sec. II B. The second step in the development of
the new class of MD approximations is to replace the
exact mode-amplitude evolution equations with various
approximations. We present several examples in Sec. II C
that use simple analytic expressions to approximate the
evolutions of some or all of the mode amplitudes which
describe the internal molecular degrees of freedom.
A.
Mode-basis Representation of MD
The mode-basis representation of MD is obtained by
transforming the Cartesian coordinate variables, ⃗xA,
used in the standard representation into new variables
that separate into i) a set that describes the macroscopic
location and orientation of the molecule, and ii) another
set that describes the molecules’ microscopic vibrational
dynamics. The macroscopic location of a molecule is rep-
resented by its center of mass, ⃗xCM(t), deﬁned by
⃗xCM(t) = 1
M
X
A
mA⃗xA(t),
(2)
where M = P
A mA is the total mass of the molecule.
1
The macroscopic orientation of a molecule is repre-
sented by a time-dependent rotation matrix R(t). This
matrix provides the transformation between a reference
frame ﬁxed to and co-moving with the molecule, and
the global inertial frame used to describe the atoms in
the standard representation of MD. We use the notation
⃗x0A + δ⃗xA(t) to denote the location of atom A in the
molecule’s co-moving reference frame, where ⃗x0A rep-
resents the time independent equilibrium position, and
1 We note that for MD simulations of collections of molecules, the
single index A that identiﬁes the atoms should be replaced by a
pair of indices mA, with m identifying the particular molecule and
A the atom within that molecule. All the macroscopic properties
of these molecules should also acquire an additional m index to
identify which molecule the attribute belongs to, e.g. M should
become Mm, ⃗xCM (t) should become ⃗xCMm(t), etc. For simplic-
ity of notation we will suppress these molecule-identifying indices
in the discussion in this paper.
δ⃗xA(t) the displacement from equilibrium (which is not
assumed to be small) of this atom. The global Carte-
sian coordinate location of atom A is determined by these
macroscopic variables—the center of mass, ⃗xCM(t) and
the orientation matrix, R(t)—along with the internal dy-
namical variables δ⃗xA:
⃗xA(t) = ⃗xCM(t) + R(t) ·

⃗x0A + δ⃗xA(t)

.
(3)
In the mode-basis representation of MD, the internal
microscopic degrees of freedom of a molecule are de-
scribed by the variables δ⃗xA. Unfortunately these vari-
ables are not independent, so special care must be taken
to isolate the truly independent degrees of freedom they
represent.
To see this more clearly, note that in the
standard MD representation there are 3N variables, ⃗xA,
needed to represent the conﬁguration state of a molecule
having N atoms. The macroscopic variables introduced
above, {⃗xCM, R}, represent 6 of these degrees of free-
dom (since there is a three-dimensional space of rotation
matrices R).
Consequently there can only be 3N −6
truly independent internal microscopic degrees of free-
dom among the 3N variables δ⃗xA. To isolate these in-
dependent degrees of freedom we introduce a collection
of “mode-basis” vectors ⃗e µ
A, where the index µ labels the
3N −6 vectors representing those independent degrees
of freedom. Without loss of generality we can normalize
these basis vectors:
δµν =
X
A
mA
M ⃗e µ
A · ⃗e ν
A,
(4)
where δµν is the Kronecker delta.
To ensure that
the ⃗e µ
A are independent from the macroscopic variables,
{⃗xCM, R}, we choose them to be orthogonal to any over-
all translation or rotation of the molecule:
0 =
X
A
mA
M ⃗e µ
A,
(5)
0 =
X
A
mA
M ⃗e µ
A × ⃗x0A.
(6)
Appendix A explains in detail why Eqs. (5) and (6) are
the conditions needed to enforce the translation and rota-
tion invariance of the eigenvectors ⃗e µ
A. Given any collec-
tion of mode-basis vectors satisfying Eqs. (4)–( 6), it is
straightforward to write down a general expression for
δ⃗xA in terms of 3N −6 independent mode-amplitude
functions Aµ(t):
δ⃗xA =
X
µ
Aµ(t)⃗e µ
A.
(7)
Using this expression and Eq. (3), it is now possible to
write down the transformation between the mode-basis
representation variables, {⃗xCM, R, Aµ}, and the Carte-
sian coordinates, ⃗xA used in the standard representation
of MD:
⃗xA(t) = ⃗xCM(t) + R(t) ·
"
⃗x0A +
X
µ
Aµ(t)⃗e µ
A
#
. (8)


## Page 4


4
There are an inﬁnite number of ways to choose the
mode-basis vectors, ⃗e µ
A. One natural choice is to let the
⃗e µ
A be the eigenvectors of the Hessian of the potential
energy function:
0 = −mAω2
µ ⃗e µ
A +
X
B
∂2U
∂⃗xB∂⃗xA
· ⃗e µ
B.
(9)
The Hessian matrix, ∂2U/∂⃗xB∂⃗xA, in this equation is
to be evaluated at the equilibrium state of the molecule
where ⃗xA = ⃗x0A. Since the Hessian is a symmetric real
matrix, the eigenvalues ω2
µ and eigenvectors ⃗e µ
A are also
real. Equation (9) is equivalent to Newton’s equation of
motion, Eq. (1), for the case of very small amplitude oscil-
lations about its equilibrium state. This choice of eigen-
vectors is therefore particularly useful for isolating the
individual microscopic degrees of freedom of a molecule.
The connection of these eigenvectors to the classical
normal-mode analysis of molecular vibrations15,24 mo-
tivated our choice of the name “mode-basis” representa-
tion. The eigenvalues ω2
µ in Eq. (9) are non-negative for
any stable molecule, and except for the six zero-frequency
modes that correspond to rigid rotations and translations
of the molecule, these eigenvalues are strictly positive
(generically). Since the Hessian matrix is symmetric, the
eigenvectors ⃗e µ
A form a complete basis for the δ⃗xA that
satisfy (or in the case of degenerate eigenvalues, can be
chosen to satisfy) the orthogonality conditions, Eq. (4).
Appendix A shows that they also satisfy the constraints,
Eqs. (5) and (6).
The standard MD equations of motion, Eq. (1), are
second-order ordinary diﬀerential equations. Therefore
both the position ⃗xA and the velocity ⃗vA = d⃗xA/dt of
each atom are needed to determine the full dynamical
state of a molecule. The analog of these velocity degrees
of freedom for the macroscopic variables are the center
of mass velocity ⃗vCM = d⃗xCM/dt, and the time deriva-
tive of the orientation matrix dR/dt.
It is convenient
and customary to express the time derivative of the ori-
entation matrix as an angular velocity vector, ⃗Ω, in the
following way. The matrix ∗Ωdeﬁned by,
∗Ω= −dR
dt · R−1,
(10)
is anti-symmetric for any rotation matrix R. Therefore
∗Ωis dual to a vector ⃗Ω:
∗Ωij =
X
k
ǫijkΩk,
(11)
where ǫijk is the totally anti-symmetric tensor with
ǫxyz = 1 in Cartesian coordinates. The time derivative
dR/dt is therefore given by,
dR
dt = −∗Ω· R,
(12)
or in component notation,
dRij
dt
= −
X
kℓ
ǫikℓΩℓRkj.
(13)
Using these results we can now write down the com-
plete set of transformation equations between the Carte-
sian coordinate variables, {⃗xA,⃗vA}, used in the stan-
dard representations of classical MD, and the variables,
{⃗xCM,⃗vCM, R, ⃗Ω, Aµ, dAµ/dt} used in our new mode-
basis representation:
⃗xA(t) = ⃗xCM(t) + ∆⃗xA(t),
(14)
⃗vA(t) = ⃗vCM(t) + ⃗Ω(t) × ∆⃗xA(t)
+
X
µ
dAµ(t)
dt
R(t) · ⃗e µ
A,
(15)
where ∆⃗xA is given by
∆⃗xA(t) = R(t) ·
"
⃗x0A +
X
µ
Aµ(t)⃗e µ
A
#
.
(16)
B.
Evolution Equations for Mode-Basis MD
The evolution equations for the mode-basis dynamical
variables, {⃗xCM, R, ⃗Ω, Aµ}, are determined from Eq. (1)
using the transformation given in Eq. (8). The resulting
equations can be written in the form:
d 2⃗xCM
dt2
= −
X
A
1
M
∂U
∂⃗xA
,
(17)
d R
dt = −∗Ω· R,
(18)
d ⃗Ω
dt = ˜U−1 · ⃗V,
(19)
d 2Aµ
dt2
=
X
ν
Sµν dAν
dt
+
X
ν
T µνAν + Fµ.
(20)
The tensor ˜U and vector ⃗V that appear in Eq. (19) are
functions of {⃗xCM, R, ⃗Ω, Aµ, dAµ/dt} given by
˜U =
X
A
mA
M
 h
R−1  ⃗x0A + δ⃗xA

· ⃗x0A
−
 ⃗x0A + δ⃗xA

⊗
 R · ⃗x0A
i
,
(21)
⃗V =
X
A
mA
M
 
2

⃗x0A · R−1 · ⃗Ω
dδ⃗xA
dt
−2

⃗x0A · dδ⃗xA
dt
 
R−1 · ⃗Ω

−

⃗Ω· ∆⃗XA

⃗x0A ×

R−1 · ⃗Ω

−1
mA
⃗x0A ×

R−1 · ∂U
∂⃗xA

,
(22)
where δ⃗xA is given in Eq. (7). Similarly the quantities
Sµν, T µν, and Fµν that appear in Eq. (20) are functions


## Page 5


5
of {⃗xCM, R, ⃗Ω, Aµ, dAµ/dt} given by
Sµν = 2
X
A
mA
M (R · ⃗e µ
A) ·
h
(R · ⃗e ν
A) × ⃗Ω
i
,
(23)
T µν = ⃗Ω· ⃗Ωδµν +
X
A
mA
M (R · ⃗e µ
A) ·
"
(R · ⃗e ν
A) × d⃗Ω
dt
#
−
X
A
mA
M
h
(R · ⃗e µ
A) · ⃗Ω
i h
(R · ⃗e ν
A) · ⃗Ω
i
,
(24)
F µ = −
X
A
1
M (R · ⃗e µ
A) · ∂U(⃗xC)
∂⃗xA
+
X
A
mA
M (R · ⃗e µ
A) ·
"
(R · ⃗x0A) × d⃗Ω
dt
#
−
X
A
mA
M
nh
(R · ⃗e µ
A) · ⃗Ω
i h
(R · ⃗x0A) · ⃗Ω
i
−(⃗e µ
A · ⃗x0A)

⃗Ω· ⃗Ω
o
. (25)
The d ⃗Ω/dt that appear in Eqs. (24) and (25) are to
be replaced by the expression on the right side of
Eq. (19).
With those replacements, the expressions
on the right sides of Eq. (17)–(20) depend only on
{⃗xCM, d⃗xCM/dt, R, ⃗Ω, Aµ, dAµ/dt}.
While the derivations leading to Eqs. (17)–(20) are
straightforward, they are lengthy and have not been re-
produced here in detail. Those derivations can be sum-
marized however as follows. Equation (17) is obtained
by inserting Eq. (1) into the second time derivative of
Eq. (2). Equation (18) follows trivially from Eqs. (10)
and (11). The derivation of Eq. (19) is more complicated.
It is obtained by projecting Eq. (1) onto the three inde-
pendent generators of rigid rotations of the molecule, i.e.
the vectors ⃗θ × ⃗x0A where ⃗θ is a unit vector whose direc-
tion determines the axis of rotation. Similarly Eq. (20)
is obtained by projecting Eq. (1) onto each of the mode-
basis vectors ⃗e µ
A.
Finally, we note that while Eq. (18) determines the
evolution of the rotation matrix R(t), solving this equa-
tion numerically directly in this form is problematic. In-
stead it is better to adopt some parameterization for
the rotation matrices, e.g. using Euler angles, and then
to solve numerically the diﬀerential equations implied
by Eq. (18) for those parameters.
In our numerical
work we have adopted the “quaternion” parameteriza-
tion of rotation matrices, in which each rotation ma-
trix is represented by four parameters {q0, q1, q2, q3} with
q2
0 + q2
1 + q2
2 + q2
3 = 1. Appendix B describes this quater-
nion representation, and explicitly gives the representa-
tion of Eq. (18) in terms of these parameters. We point
out that the version of the quaternion evolution equa-
tions used here introduces a new (so far as we know) con-
straint damping mechanism that ensures the constraint,
q2
0 + q2
1 + q2
2 + q2
3 = 1, remains satisﬁed by the numerical
solution.
C.
Large-Scale MD Approximations
Equations (17)–(20) are a well-posed system of ordi-
nary diﬀerential equations that give an exact representa-
tion of classical MD in terms of the mode-basis dynam-
ical variables {⃗xCM, R, ⃗Ω, Aµ}. The idea of our large-
scale MD approximations is to use some subset of the
exact equations to determine the macroscopic degrees of
freedom, {⃗xCM, R, ⃗Ω}, while using simpler approximate
equations to determine the evolution of the internal vi-
brational degrees of freedom Aµ.
The most straightforward way to construct a large-
scale approximation uses Eqs. (17)–(19) to determine
{⃗xCM, R, ⃗Ω}, while replacing Eq. (20) with some approx-
imate equation for Aµ.
Perhaps the most natural ap-
proximation for Aµ, which we refer to as the sinusoidal
mode amplitude (SMA) approximation, would be to set
the mode amplitudes Aµ(t) to their small-amplitude per-
turbation solution values:
Aµ(t) = A0
µ sin(ωµt + ϕµ),
(26)
where ωµ is the mode frequency determined from Eq. (9),
while A0
µ and ϕµ are constants that specify the amplitude
of phase of each mode. In this approximation, Eq. (26)
replaces Eq. (20) and is used to evaluate the right sides
of Eqs. (17)–(19). Those equations for the macroscopic
degrees of freedom {⃗xCM, R, ⃗Ω} are then solved numeri-
cally. The system of equations being solved numerically
is therefore reduced from 6N ﬁrst-order equations for the
exact MD system, to just twelve for this large-scale ap-
proximation. The use of this approximation eliminates
the need to evaluate the complicated quantities Sµν, T µν
and Fµ that appear on the right side of Eq. (20) numer-
ically. This reduction in the number of equations to be
solved numerically, as well as the reduction in the need to
evaluate the complicated expressions that occur on the
right side of Eq. (20) considerably reduces the computa-
tional cost of implementing the SMA approximation.
Another plausible approximation, which we refer to as
the zero mode amplitude (ZMA) approximation, simply
sets all the mode amplitudes to zero:
Aµ(t) = 0.
(27)
We expect the long time averages of the positions of the
atoms to be their equilibrium positions ⃗x0A. Thus we ex-
pect the time averages of the mode amplitudes Aµ(t) to
be zero, as they are for example in the SMA approxima-
tion given in Eq. (26). This should reduce the computa-
tional cost of evaluating the right sides of Eqs. (17)–(19)
in the ZMA approximation even below those costs in the
SMA approximation. In addition the ZMA approxima-
tion eliminates all the short timescale eﬀects associated
with the molecular vibrations, so it should be possible to
use much larger timesteps to determine the macroscopic
variables {⃗xCM, R, ⃗Ω} in this approximation, and thus to
reduce the computational cost even below those for the
SMA approximation.


## Page 6


6
We note that hybrid approximations can easily be con-
structed as well. In these hybrid approximations some of
the mode amplitudes are set to the SMA or the ZMA
approximations given in Eqs. (26) or (27), while the re-
maining amplitudes are determined numerically by solv-
ing Eq. (20).
This approach might be appropriate for
systems having a few modes with oscillation timescales
comparable to the timescales associated with the macro-
scopic properties of the molecule.
In such cases those
low frequency modes could be treated exactly while the
approximations could still be used for the majority of
modes having much shorter oscillation timescales.
Somewhat more sophisticated large-scale approxima-
tions can also be obtained by choosing the equations of
motion for the macroscopic variables, {⃗xCM, R, ⃗Ω}, from
the particular combination of the exact equations that
determine the evolution of the macroscopic linear and
angular momentum, ⃗P and ⃗J, of each molecule. These
quantities are deﬁned by
⃗P =
X
A
mA
d⃗xA
dt ,
(28)
⃗J =
X
A
mA∆⃗xA × d∆⃗xA
dt
,
(29)
where ∆⃗xA, deﬁned in Eq. (14), is the position of each
atom relative to the center of mass of the molecule.
2
The time derivatives of these quantities can be written
in terms of the macroscopic variables as
d⃗P
dt = M d 2⃗xCM
dt2
,
(30)
d ⃗J
dt = ˜
JΩ· d⃗Ω
dt + ⃗J ,
(31)
where ˜
JΩand ⃗J are given by
˜
JΩ=
X
A
mA

∆⃗xA · ∆⃗xA I −∆⃗xA ⊗∆⃗xA

,
(32)
⃗J =
X
A
mA∆⃗xA × ⃗BA,
(33)
and where ⃗BA is given by
⃗BA =
X
µ
d 2Aµ
dt2
+ 2dAµ
dt
⃗Ω×

R · ⃗e µ
A
+

⃗Ω⊗⃗Ω−⃗Ω· ⃗ΩI

· ∆⃗xA.
(34)
If we assume the mode amplitudes Aµ(t) are prede-
termined by some approximate expressions, like those in
Eqs. (26) or (27) for example, then ˜
JΩand ⃗J depend
only on the large scale variables d⃗xCM/dt, R, ⃗Ω, but not
2 The angular momentum ⃗J deﬁned in this way is the angular
momentum relative to the center of mass of the molecule.
on their time derivatives. Equations (30) and (31) can
therefore be used to construct an alternate set of approxi-
mate evolution equations for the large scale variables. In
particular an evolution equation for the center-of-mass
motion of each molecule can be obtained by setting the
rate of change of the total momentum equal to the total
external force acting on the molecule:
d⃗P
dt = −
X
A
∂U
∂⃗xA
= M d 2⃗xCM
dt2
.
(35)
Similarly an equation for d⃗Ω/dt can be obtained by set-
ting d ⃗J/dt equal to the total external torque acting on
the molecule:
d ⃗J
dt = −
X
A
∆⃗xA × ∂U
∂⃗xA
= ˜
JΩ· d ⃗Ω
dt + ⃗J .
(36)
The resulting evolution equations for ⃗xCM and ⃗Ωare
given by
d 2⃗xCM
dt2
= −1
M
X
A
∂U
∂⃗xA
,
(37)
d ⃗Ω
dt = −

˜
JΩ
−1
·
"
⃗J +
X
A
∆⃗xA × ∂U
∂⃗xA
#
.
(38)
Equations (37) and (38) represent somewhat diﬀerent
projections of the exact MD equations, Eq. (1), than
those given in Eqs. (17) and (19). Therefore Eqs. (37) and
(38) together with Eq. (18), provide an alternate some-
what diﬀerent set of evolution equations for the macro-
scopic variables {⃗xCM, R, ⃗Ω}.
We refer to these alter-
nate equations as the momentum conserving (MC) large-
scale approximation. These equations can be solved us-
ing any predetermined approximate form for the mode
amplitudes Aµ(t). In this paper we explore the two pos-
sibilities discussed above: We refer to the momentum
conserving approximation using sinusoidal mode ampli-
tudes, Eq. (26), as the MCSMA approximation, and the
momentum conserving approximation using zero mode
amplitudes, Eq. (27), as the MCZMA approximation.
III.
RELIABILITY TESTING
In this section we assess the reliability of the large-scale
MD approximations introduced in Sec. II C. We do this
by comparing the values of the macroscopic variables,
{⃗xCM,⃗vCM, R, ⃗Ω}, computed numerically using the ex-
act MD equations, with those computed using several
examples of large-scale MD approximations.
We also
compare how well these various methods conserve the
total energy E, the total momentum ⃗P, and the total
angular momentum ⃗J of each molecule. The remainder
of this section is organized as follows. Section III A de-
scribes in detail the model problem, and the numerical
methods used to solve the MD equations for these tests.


## Page 7


7
Section III B presents the results of numerical tests that
conﬁrm the mode-basis representation of the exact MD
equations, introduced in Sec. II B, gives the same results
as the standard Cartesian representation for this model
problem. Section III C gives the results of our numeri-
cal tests for the large-scale approximations SMA, ZMA,
MCSMA and MCZMA introduced in Sec. II C. Finally
in Sec. III D we compare the computational eﬃciency of
these various methods when applied to our model prob-
lem.
A.
Model Problem
We use a collection of simple molecules, the fullerenes
C20, C26, C60, and C70, to study the reliability of the
large-scale MD approximations introduced in Sec. II C.
These molecules consist entirely of trivalent carbon atoms
located at the vertices of convex polyhedra. Figure 1 il-
lustrates the topological bond connections between the
atoms (but not the actual geometrical shapes) of the
molecules used in our tests.
FIG. 1. Figures show the topological bond connections for the
C20, C26, C60, and C70 molecules used in our test MD simu-
lations. Each atom is labeled with a number that represents
the value of the index A for that atom.
We use a simpliﬁed version of the CHARMM27 model
for the potential energy function U(⃗xA) that determines
the interactions between the atoms. This interaction po-
tential is given by
U = 1
2κb
X
bonds (CD)
(rCD −Lb)2 + 1
2κθ
X
angles (CDE)
(θCDE −θb)2,
(39)
where Lb and θb are the lengths and angles of equilibrium
molecular bonds in this simple model, and where rCD and
θCDE represent respectively the distance between atoms
C and D and the angle formed by the bonds between atom
D with atoms C and E,
r2
CD = (⃗xC −⃗xD) · (⃗xC −⃗xD),
(40)
cos θCDE = (⃗xC −⃗xD) · (⃗xE −⃗xD)
rCD rDE
.
(41)
The sums in Eq. (39) are taken respectively over the
collection of bonds (CD) between the pairs of atoms C
and D, and over the collection of angles (CDE) formed
by the bond between atoms C and D and the bond be-
tween atoms D and E. We use the following values for
the carbon-carbon bond parameters:
κb = 305 kcal/
˚A2/mol, Lb = 1.375 ˚A, and θb = 120 degrees taken from
the CHARMM27 force ﬁeld parameters for these carbon-
carbon bonds.25 For simplicity in coding up our tests, we
left out the standard torsion-angle bond interactions from
the potential energy. Without those torsion-angle forces,
the fullerene molecules are unstable with our simpliﬁed
interaction potential when the CHARMM27 value is used
for the bond angle force constant, κθ = 40 kcal/rad2/mol.
Therefore we have increased the value of κθ used in our
tests to κθ = 305 kcal/rad2/mol to achieve stability. Our
purpose here is to test the robustness of our large-scale
approximations. These approximations should succeed
or fail independent of the details of the interaction po-
tential model being used, so we do not think it matters
that our simpliﬁed potential model is not state of the art.
The ﬁrst step in our analysis of these molecules is to
determine their equilibrium conﬁgurations, ⃗x0A, for the
interaction potential U(⃗xA) given in Eq. (39).
We do
this by ﬁnding the energy minimum where ∂U/∂⃗xA = 0.
We use the Fletcher-Reeves-Polak-Ribiere version of the
conjugate gradient method with line minimizations to
ﬁnd these equilibrium states, ⃗x0A, numerically.26 Given
an equilibrium state, we next evaluate the Hessian ma-
trix ∂2U/∂⃗xA∂⃗xB numerically for that state, and solve
Eq. (9) to determine the eigenvalues ωµ and eigenvec-
tors ⃗e µ
A.
We use Householder reduction to transform
∂2U/∂⃗xA∂⃗xB to tridiagonal form, followed by a tradi-
tional QL algorithm with implicit shifts to determine the
eigenvalues and eigenvectors numerically.26 These eigen-
vectors are then projected and normalized so they satisfy
Eqs. (4)–(6) to double precision accuracy numerically.
We
construct
initial
data
for
our
test
evolu-
tions by choosing values for the mode-basis variables
{⃗xCM,⃗vCM, R, ⃗Ω, Aµ, dAµ/dt} that are appropriate for
a thermodynamic equilibrium state at temperature T .
Following the equipartition theorem, we ﬁx the values
for each of the mode-basis variables so that each de-
gree of freedom of the molecule has energy 1
2kT , where
k = 1.9872×10−3 kcal/(mol K) is Boltzmann’s constant.
All the tests reported here use a temperature T = 300K.
By choosing the origin and the orientation of the Carte-
sian coordinate system, we can set ⃗xCM = 0 and R = I
at t = 0 without loss of generality. We choose ⃗vCM and
⃗Ωat t = 0 to be vectors whose orientations are set with
a random number generator, and whose magnitudes are
set by requiring the translational and rotational kinetic


## Page 8


8
energies to satisfy,
1
2kT = 1
2M ⃗vCM · ⃗vCM,
(42)
1
2kT = 1
2
X
A
mA
h
⃗x0A · ⃗x0A ⃗Ω· ⃗Ω−
 ⃗x0A · ⃗Ω
2i
. (43)
The mode amplitudes Aµ and their time derivatives
dAµ/dt are chosen at t = 0 to ensure that each normal
mode of the molecule has energy kT :
Aµ = 1
ωµ
r
2kT
M sin ϕµ,
(44)
dAµ
dt
=
r
2kT
M cos ϕµ,
(45)
where ϕµ are randomly selected phases. These initial val-
ues for {⃗xCM,⃗vCM, R, ⃗Ω, Aµ, dAµ/dt} are used to start
the evolutions of the exact mode-basis representation of
the MD equations. We convert them to the equivalent
Cartesian representation variables using Eqs. (14) and
(15), and use those initial data to start our exact Carte-
sian MD evolutions. We also use the same initial values
of {⃗xCM,⃗vCM, R, ⃗Ω, Aµ, dAµ/dt} to set the initial data
for the SMA and MCSMA approximation tests.
And
ﬁnally we use these same values for {⃗xCM,⃗vCM, R, ⃗Ω}
with Aµ = dAµ/dt = 0 to set the initial data for the
ZMA and MCZMA approximation tests.
All the MD simulation methods considered here con-
sist of systems of ordinary diﬀerential equations of the
form d ⃗Y /dt = ⃗F(⃗Y , t), where ⃗Y is the n-dimensional
vector consisting of the dynamical ﬁelds in a particu-
lar method and ⃗F(⃗Y , t) is the right side of the evolution
equations for those ﬁelds. We solve these systems nu-
merically with the initial data ⃗Y = ⃗Y (0) described above
using an 8th order integrator by Dormand and Prince
with dynamic timestep size control (see Hairer et al.27
for details).
This algorithm controls the error in ⃗Y (t)
by adjusting the timestep size to keep an estimate of the
local time-truncation error below ǫτ
 |⃗Y | + 1

(see Hairer
et al.27 for details about this timestep control). We run
each simulation with several values of the timestep ac-
curacy parameter ǫτ in the range 10−13 ≤ǫτ ≤10−6 to
verify that timestep errors are not the dominant cause
of any diﬀerences we may see between the various MD
evolution methods.
B.
Testing the Exact Mode-Basis Representation
Our ﬁrst numerical tests of the model problem de-
scribed in Sec. III A are designed to examine the diﬀer-
ences between MD simulations performed with the stan-
dard Cartesian-basis representation of the MD equations,
Eq. (1), and the exact mode-basis representation given in
Eqs. (17)–(20). To perform these tests we use the exact
Cartesian-basis solution computed with timestep accu-
racy parameter ǫτ = 10−13 as the reference solution with
0
100
200
300
400
t (ps)
10
-12
10
-10
10
-8
10
-6
10
-4
10
-2
10
0
Ex
Cartesian-basis      ετ=10
−6
Cartesian-basis      ετ=10
−8
Cartesian-basis      ετ=10
−10
Cartesian-basis      ετ=10
−12
Mode-basis            ετ=10
−6
Mode-basis            ετ=10
−8
Mode-basis            ετ=10
−10
Mode-basis            ετ=10
−12
FIG. 2.
Solid curves show Ex computed with the exact
Cartesian-basis MD code for diﬀerent values of the timestep
accuracy parameter ǫτ. Dashed curves show Ex for evolutions
of the exact mode-basis MD code for diﬀerent ǫτ. The expo-
nential growth in these Ex is caused by the chaotic nature of
MD evolutions.
which to compare everything else. We refer to this refer-
ence solution as ⃗x Ref
A
(t).
We ﬁrst measure how sensitively the exact Cartesian-
basis MD evolutions depend on the timestep accuracy pa-
rameter ǫτ. To do this we evaluate the quantity Ex that
measures the diﬀerences between solutions computed us-
ing diﬀerent timestep accuracy parameters, ǫτ, and the
reference solution:
Ex(ǫτ) =
s
1
N
X
A
⃗xA(ǫτ) −⃗x Ref
A
2.
(46)
The solid curves in Fig. 2 show Ex(ǫτ) for exact
Cartesian-basis MD simulations of the C20 fullerene
molecule computed with four diﬀerent values of ǫτ =
{10−6, 10−8, 10−10, 10−12}. Data points for these curves
are obtained by evaluating Ex at 10 ps time intervals dur-
ing the evolutions. Each of these curves begins at early
times with Ex ≈ǫτ and then grows exponentially un-
til Ex ≈1 where it remains relatively constant for the
duration of the simulation. These curves conﬁrm the ex-
pectation that MD simulations are chaotic. Although the
initial data at t = 0 for these various runs are identical,
after one time step the solutions diﬀer from the one spec-
iﬁed by the initial data, by amounts that depend on the
timestep accuracy parameter ǫτ. By deﬁnition, chaotic
dynamical systems have the property that nearby solu-
tions diverge exponentially. Figure 2 conﬁrms that this
is what is going on by showing that each of these evolu-
tions of the fullerene C20 molecule diverges from the ref-


## Page 9


9
erence solution at the same exponential rate. The anal-
ogous graphs for the other fullerene molecules, C26, C60
and C70, included in our study are very similar, except
for the timescale on which the chaotic instability occurs.
In the C26 case, the instability grows at about half the
rate of the C20 case, while the instabilities in the C60
and the C70 cases grow at two or three times the C20
rate. The presence of chaotic behavior in these MD sim-
ulations demonstrates why it is impossible to compute
molecular evolutions in complete detail.
Only certain
macroscopic features of the evolutions, like dynamically
conserved quantities such as the energy, momentum and
angular momentum are reproducible and simulatable.
The dashed curves in Fig. 2 show Ex for simulations
based on the exact mode-basis MD representation. We
use the same Cartesian-basis reference solution ⃗x Ref
A
when computing Ex for these mode-basis simulations, and
we see that the exponential divergence from the reference
solution has exactly the same structure it has for the
Cartesian-basis evolutions. The only diﬀerence is that
the values of Ex are somewhat larger, Ex ≈3ǫτ, at very
early times in the mode-basis case. These diﬀerences ap-
pear to be caused by the fact that the mode-basis equa-
tions are much more complicated than their Cartesian-
basis counterparts, so the truncation errors are somewhat
higher in this case for ﬁxed ǫτ. The rate of the exponen-
tial divergence from the reference solution is the same
as the Cartesian-basis case, so Fig. 2 conﬁrms that the
mode-basis equations produce the same evolutions as the
standard Cartesian-basis representation of MD. More im-
portantly perhaps, these tests also conﬁrm that our codes
to evolve both versions of the MD equations contain no
serious errors.
We have also monitored how well the energy E deﬁned
by,
E = 1
2
X
A
d⃗xA
dt · d⃗xA
dt + U(⃗xB),
(47)
the total momentum ⃗P deﬁned in Eq. (28) and the total
angular momentum (about the center of mass) ⃗J deﬁned
in Eq. (29) are conserved in these exact MD evolutions.
In the absence of external forces (like van der Waals in-
teractions with other molecules) these quantities should
all be conserved by the exact MD evolution equations.
To monitor these conserved quantities we deﬁne EE, EP
and EJ that measure the deviations of these quantities
from their initial values:
EE(t) =
E(t) −E(0)

E(0)
,
(48)
EP (t) =
⃗P(t) −⃗P(0)

⃗P(0)

,
(49)
EJ(t) =
 ⃗J(t) −⃗J(0)

 ⃗J(0)

.
(50)
The solid curves in Fig. 3 show the evolution of these
energy and momentum conservation errors for the simu-
0
100
200
300
400
t (ps)
10
-16
10
-14
10
-12
10
-10
EE     Cartesian-basis
EE     Mode-basis 
EP     Cartesian-basis
EP     Mode-basis
EJ     Cartesian-basis
EJ     Mode-basis
FIG. 3.
Solid curves show EE, EP and EJ for evolutions
using the exact Cartesian MD code with timestep accuracy
ǫτ = 10−13. Dashed curves show these same quantities for
evolutions using the exact mode-basis MD code.
lations of the Cartesian-basis representation of the MD
equations. The results in this ﬁgure represent those of
the highest resolution simulations, i.e. those computed
with timestep error parameter ǫτ = 10−13. We see from
these ﬁgures that each of the conservation error quan-
tities begins at small times with EE ≈EP ≈EJ ≈ǫτ,
which then grow slowly, roughly as a power law in time:
E ∝t k, with k ≲2. (The growth of truncation level er-
rors in this way is typical of explicit numerical ordinary
diﬀerential equation integrators such as the Dormand-
Prince algorithm used in our tests.) The dashed curves
in Fig. 3 show the errors in these conserved quantities for
evolutions of the same initial data using the mode-basis
representation of MD. The mode-basis results shown in
Fig. 3 were also computed using timestep error parame-
ter ǫτ = 10−13. These results conﬁrm that both versions
of the exact MD equations conserve the energy, the linear
momentum, and the angular momentum of molecules at
the level of the numerical truncation error used.
C.
Testing the Large-Scale Approximations
In this section we present the results of numerical
tests of the large-scale MD approximations developed in
Sec. II C. These approximations include the SMA and
ZMA approximations that use a sinusoidal-in-time ap-
proximation (SMA) or the zero approximation (ZMA) re-
spectively for the mode amplitudes Aµ(t). These approx-
imations solve the exact mode-basis evolution Eqs. (17)–
(19) for {⃗xCM,⃗vCM, R, ⃗Ω}, and simply ignore the exact


## Page 10


10
0
100
200
300
400
t (ps)
10
-16
10
-14
10
-12
10
-10
10
-8
10
-6
10
-4
EE
SMA
ZMA
MCSMA
MCZMA
FIG. 4.
Solid curves show energy conservation violations
EE for the large-scale approximations SMA and ZMA, while
dashed curves show these violations for the MCSMA and
MCZMA approximations.
evolution Eq. (20) for Aµ(t). We also test approxima-
tions that use angular momentum conservation instead
of Eq. (19) to determine the evolution of ⃗Ω(t). The equa-
tions for these momentum conserving approximations,
MCSMA and MCZMA, are given in Eqs. (37) and (38).
All the numerical results shown here use the highest time
resolution, ǫτ = 10−13, in evolutions of the C20 fullerene
molecule.
First we test how well these large-scale approximations
conserve the energy E, linear momentum ⃗P, and angular
momentum ⃗J during the evolutions of our model prob-
lem.
We use the quantities EE, EP and EJ deﬁned in
Eqs. (48)–(50) to monitor conservation violations. The
solid curves in Fig. 4 show the energy conservation vio-
lations EE for the SMA and ZMA approximations, while
the dashed curves show these violations for the MCSMA
and MCZMA approximations.
We see that the zero
mode approximations ZMA and MCZMA conserve en-
ergy much better than the sinusoidal mode approxima-
tions SMA and MCSMA. However, even these sinusoidal
mode approximations give energy conservation violations
below the 0.1% level for these test problems.
The solid curves in Fig. 5 show the linear momentum
conservation violations EP for the SMA and ZMA ap-
proximations, while the dashed curves show these viola-
tions for the MCSMA and MCZMA approximations. We
see that linear momentum violation EP are much smaller
for MCSMA than the SMA approximation, while its val-
ues are about the same for the MCZMA and ZMA ap-
proximations. Figure 5 shows, however, that linear mo-
mentum conservation is excellent for all of these large-
scale approximations.
0
100
200
300
400
t (ps)
10
-22
10
-20
10
-18
10
-16
10
-14
10
-12
10
-10
10
-8
EP
SMA
ZMA
MCSMA
MCZMA
FIG. 5. Solid curves show linear momentum conservation vio-
lations EP for the large-scale approximations SMA and ZMA,
while dashed curves show these violations for the MCSMA
and MCZMA approximations.
0
100
200
300
400
t (ps)
10
-20
10
-18
10
-16
10
-14
10
-12
10
-10
10
-8
10
-6
10
-4
10
-2
EJ
SMA
ZMA
MCSMA
MCZMA
FIG. 6. Solid curves show angular momentum conservation
violations EJ for the large-scale approximations SMA and
ZMA, while dashed curves show these violations for the MC-
SMA and MCZMA approximations.
The solid curves in Fig. 6 show the angular momen-
tum conservation violations EJ for the SMA and ZMA
approximations, while the dashed curves show these vi-
olations for the MCSMA and MCZMA approximations.


## Page 11


11
We see that angular momentum conservation EJ is much
better for MCSMA than the SMA approximation, while
these violations are about the same for the MCZMA
and ZMA approximations.
Not surprisingly, the mo-
mentum conserving approximation MCSMA has much
better linear and angular momentum conservation prop-
erties that SMA, and somewhat better momentum con-
servation than the zero mode amplitude approximations
MCZMA and ZMA.
Finally,
we
test
how
well
the
large-scale
ap-
proximations
reproduce
the
macroscopic
variables
{⃗xCM,⃗vCM, R, ⃗Ω} for our model problem. We use the
exact mode-basis representation with ǫτ = 10−13 as our
reference solution in this case to test the various the
large-scale approximations. We evaluate the diﬀerences
between the approximate and the exact solutions using
the quantities ExCM , EvCM , EΩand Eq, deﬁned by
ExCM =
⃗xCM −⃗x Ref
CM
,
(51)
EvCM =
⃗vCM −⃗v Ref
CM
,
(52)
EΩ=
⃗Ω−⃗ΩRef
⃗ΩRef 
,
(53)
Eq = 1
2
sX
i
 qi −q Ref
i
2.
(54)
The solid curves in Fig. 7 show errors in the center of
mass position, ExCM , for the SMA and ZMA approxima-
tions, and the dashed curves show these errors for the
MCSMA and MCZMA approximations. For comparison
the dotted curve in Fig. 7 shows the error in the some-
what lower resolution, ǫτ = 10−12, evolution of the exact
mode-basis representation compared to the reference so-
lution. All of these errors are very small, and are only
growing slowly with time, approximately like ExCM ∝t2.
These graphs conﬁrm that all the large-scale approxima-
tions are able to determine ⃗xCM with excellent precision.
The solid curves in Fig. 8 show the errors in the veloc-
ity of the center of mass, EvCM , for the SMA and ZMA
approximations, and the dashed curves show these errors
for the MCSMA and MCZMA approximations. For com-
parison the dotted curve in Fig. 8 shows the error in the
somewhat lower resolution, ǫτ = 10−12, evolution of the
exact mode-basis representation compared to the refer-
ence solution. All of these errors are very small, and ap-
pear almost constant in time at late times. These graphs
conﬁrm that all the large-scale approximations are able
to determine ⃗vCM with excellent precision.
The solid curves in Fig. 9 show the errors in the ori-
entation matrix R, as measured by Eq, for the SMA and
ZMA approximations, and the dashed curve shows these
errors for the MCSMA approximation.
The Eq curve
for the MCZMA approximation is indistinguishable from
the ZMA curve.
For comparison the dotted curve in
Fig. 9 shows the error in the somewhat lower resolution,
ǫτ = 10−12, evolution of the exact mode-basis representa-
tion compared to the reference solution. The exact dot-
0
100
200
300
400
t (ps)
10
-13
10
-12
10
-11
10
-10
10
-9
ExCM
SMA
ZMA
MCSMA
MCZMA
Exact Mode-Basis
FIG. 7. Solid curves show errors in the center of mass posi-
tion ExCM for the large-scale approximations SMA and ZMA,
while dashed curves show these errors for the MCSMA and
MCZMA approximations. Dotted curve shows ExCM for an
exact mode-basis evolution with ǫτ = 10−12.
0
100
200
300
400
t (ps)
10
-14
10
-13
10
-12
10
-11
EvCM
SMA
ZMA
MCSMA
MCZMA
Exact Mode-Basis
FIG. 8. Solid curves show errors in the center of mass veloc-
ity EvCM for the large-scale approximations SMA and ZMA,
while dashed curves show these errors for the MCSMA and
MCZMA approximations. Dotted curve shows EvCM for an
exact mode-basis evolution with ǫτ = 10−12.
ted curve in Fig. 9 shows the exponential growth at early
times which signals the presence of chaotic dynamics in
this variable.
The large scale approximations all have
errors Eq that are comparable to the late time behavior


## Page 12


12
0
100
200
300
400
t (ps)
10
-12
10
-10
10
-8
10
-6
10
-4
10
-2
10
0
Eq
SMA
ZMA, MCZMA
MCSMA
Exact Mode-Basis
FIG. 9. Solid curves show errors in the orientation param-
eters Eq for the large-scale approximations SMA and ZMA,
while dashed curve shows these errors for the MCSMA ap-
proximation. The MCZMA errors are indistinguishable from
the ZMA errors in this graph. Dotted curve shows Eq for an
exact mode-basis evolution with ǫτ = 10−12.
of the exact MD simulation. While it may be surprising
that the orientation of the molecule cannot be predicted
accurately from initial conditions of the molecule using
an exact MD simulation, it is not surprising in this case
that the large-scale approximations all give rather poor
results for R as well.
The solid curves in Fig. 10 show errors in ⃗Ω, as mea-
sured by EΩ, for the SMA and ZMA approximations, and
the dashed curves show these errors for the MCSMA ap-
proximation. The MCZMA curve for EΩis indistinguish-
able from the ZMA curve. For comparison the dotted
curve in Fig. 10 shows the error in the somewhat lower
resolution, ǫτ = 10−12, evolution of the exact mode-
basis representation compared to the reference solution.
The exact dotted curve in Fig. 10 shows the exponential
growth signaling the presence of chaotic dynamics in this
variable. Given the chaos seen in the evolution of the ori-
entation matrix R seen in Fig. 9, it is not at all surprising
that similar chaotic behavior is seen in the evolution of
⃗Ω. Thus it is not surprising that the large scale approx-
imations all have errors EΩthat are comparable to the
late time behavior of the exact MD simulations.
In summary: All the large scale approximations do an
excellent job of conserving linear momentum.
All the
large scale approximations except SMA do an excellent
job of conserving angular momentum.
The ZMA and
MCZMA approximations do an excellent job of energy
conservation, while the SMA and MCSMA approxima-
tions do not do so well. All of the large-scale approx-
imations do excellent jobs of modeling ⃗xCM and ⃗vCM.
0
100
200
300
400
t (ps)
10
-12
10
-10
10
-8
10
-6
10
-4
10
-2
10
0
EΩ
SMA
ZMA, MCZMA
MCSMA
Exact Mode-Basis
FIG. 10.
Solid curves show errors in the angular velocity
EΩfor the large-scale approximations SMA and ZMA, while
dashed curve shows these errors for the MCSMA approxi-
mation. The MCZMA errors are indistinguishable from the
ZMA errors in this graph. Dotted curve shows EΩfor an exact
mode-basis evolution with ǫτ = 10−12.
None of the large scale approximations do a good job
of modeling the macroscopic orientation variables R and
⃗Ω. Overall then, our results show that the ZMA and the
MCZMA approximations are more reliable approxima-
tions of the exact MD equations than the SMA and the
MCSMA approximations.
D.
Computational Eﬃciency
This section brieﬂy discusses the computational costs
of the various MD evolutions used in our tests.
Fig-
ure 11 shows the total run times (in seconds) for the
exact Cartesian-basis simulation tests performed for
each of the fullerene molecules C20, C26, C60, and
C70.
For each molecule we ran ﬁve evolutions with
ǫτ = {10−6, 10−8, 10−10, 10−12, 10−13}, with each evolu-
tion simulating 400 ps of the molecular motion. Figure 11
shows that the run times for these tests increases expo-
nentially as the number of atoms in the simulation in-
creases. A reasonably good approximation of these total
run times is given by trun ≈1500 × 10 N/33. The code
we wrote to implement these methods was not highly op-
timized, so we expect that the computational eﬃciency
could almost certainly be improved.
In Fig. 12 we illustrate the relative computational costs
of performing evolutions using the various versions of the
MD evolution equations discussed here. The solid curves
connect the data points that represent the ratios of the
total run times for the SMA and ZMA large-scale approx-


## Page 13


13
20
30
40
50
60
70
N
10
3
10
4
10
5
trun (s)
Exact Cartesian-basis
FIG. 11. Total run times in seconds for the 400 ps simula-
tions of the fullerene molecules CN using the Cartesian-basis
version of the MD evolution code. Total run time includes
the runs using ﬁve diﬀerent values of the timestep error pa-
rameters ǫτ = {10−6, 10−8, 10−10, 10−12, 10−13}.
imations to the total run time for the exact Cartesian-
basis evolution. The dashed curves connect the analo-
gous data points for the MCSMA and the MCZMA ap-
proximations. Finally, the dotted curve connects the data
points that represent the ratios of the total run times for
the exact mode-basis MD representation to the total run
time for exact Cartesian-basis representation. These re-
sults show that computations using the SMA and MC-
SMA approximations are about twice as fast as those us-
ing the exact Cartesian-based representation, while the
ZMA and MCZMA approximations are more than 25
times faster. The dotted curve in Fig. 12 shows that com-
putations using the exact mode-basis representation of
MD is two or three times slower than the exact Cartesian-
basis representation. On the basis of computational eﬃ-
ciency, the MCZMA large-scale approximation is by far
the best of the various MD simulation methods tested
here.
IV.
DISCUSSION
We have developed a new mode-based representation
of the classical MD equations of motion that separate
the macroscopic position and orientation degrees of free-
dom of a molecule from the internal vibrational degrees
of freedom. We have conﬁrmed through our numerical
tests that most details of a molecular dynamical state
evolve chaotically, including the large scale orientation
and angular velocity of the molecule. Consequently those
features cannot be predicted accurately even with exact
20
30
40
50
60
70
N
10
-2
10
-1
10
0
tSMA / tCartesian-basis
tZMA / tCartesian-basis
tMCSMA / tCartesian-basis
tMCZMA / tCartesian-basis
tMode-basis / tCartesian-basis
FIG. 12. Relative run times for the various large-scale MD
approximations as functions of N the number of atoms in the
simulation. Solid curves represent the ratios of the run times
of the SMA and ZMA approximations with the run time for
the exact Cartesian-basis representation. Dashed curves give
the analogous ratios for the MCSMA and the MCZMA ap-
proximations. Dotted curve gives the ratio of the run times for
the exact mode-basis representation to the exact Cartesian-
basis representation.
MD simulations. We have derived a number of new large-
scale approximations (based our new mode-based rep-
resentation) speciﬁcally designed to simulate accurately
those features of MD evolutions that are not chaotic. We
have shown through a series of careful numerical tests
that some of these large-scale approximations give reli-
able, accurate predictions for the macroscopic properties
of molecular motions, including the energies, linear and
angular momentum, and the positions and velocities of
their centers of mass.
We ﬁnd that one of these new
approximations (MCZMA, the best of these new large-
scale approximations studied here) is more than 25 times
faster than our exact Cartesian-basis MD code, while
giving comparable accuracy for the large-scale molecu-
lar properties. We also note that the MCZMA approx-
imation does not depend on the mode basis vectors ⃗e,µ
A
at all, which makes it very easy to implement numeri-
cally. Thus we conclude there are many reasons to use
reliable well-tested approximations for MD simulations
rather than performing simulations using the full exact
MD equations.
The tests done for this study focused on simulations of
the dynamics of single molecules. The formalism created
here has been designed, however, to accommodate sim-
ulations of collections of molecules in a straightforward
way. The only change that needs to be made, as we noted
earlier, is to change the single index A used to identify


## Page 14


14
individual atoms to a pair of indices mA, where the ﬁrst
index m determines which molecule the particular atom
belongs. Macroscopic properties of the molecule like the
energy, E, linear and angular momenta, ⃗P and ⃗J, the po-
sition and velocity of the center of mass, ⃗xCM and ⃗vCM
should also acquire indices to identify which molecule
they belong: {Em, ⃗Pm, ⃗Jm, ⃗xCMm,⃗vCMm}. Then, by in-
cluding van der Waals and/or Coulomb forces in the in-
teraction potential U(⃗xmA), it would be possible to study
interactions between molecules using any of the large-
scale approximations introduced here. The interactions
modeled in this way should be essentially identical to
those interactions in an exact MD simulation.
ACKNOWLEDGMENTS
We thank Andrew McCammon and Lane Votapka for
numerous helpful discussions on molecular dynamics.
Funding and support for this work came from the Na-
tional Biomedical Computation Resource through NIH
grant P41 GM103426.
The fullerene topology graphs
used in Fig. 1 were adapted from ﬁgures produced by
R.A. Nonenmacher and published in Wikipedia under
the Creative Commons Attribution-Share Alike 3.0 Un-
ported license.
Appendix A: Normal Mode Basis
One natural choice for the mode-basis vectors ⃗e µ
A are
the eigenvectors of the Hessian of the potential energy
function:
0 = −mAω2
µ ⃗e µ
A +
X
B
∂2U
∂⃗xB∂⃗xA
· ⃗e µ
B,
(A1)
where ∂2U/∂⃗xB∂⃗xA in this equation is to be evaluated
at the equilibrium state of the molecule where ⃗xA = ⃗x0A.
Since the Hessian is a symmetric 3N × 3N dimensional
real matrix, the eigenvalues ω2
µ and eigenvectors ⃗e µ
A are
also real, and the collection of eigenvectors form a com-
plete basis for the 3N dimensional space of vectors.
Equation (A1) is equivalent to Newton’s equation of mo-
tion, Eq. (1), for the case of very small amplitude os-
cillations about its equilibrium state, so we call these ⃗e µ
A
the normal-mode basis. For stable molecules the normal-
mode frequencies are real, so all the eigenvalues of such
systems are non-negative: ω2
µ ≥0.
The zero-frequency modes of a molecule are repre-
sented by the eigenvectors of the Hessian matrix of the
equilibrium potential energy function having zero eigen-
values,
0 =
X
B
∂2U(⃗x0C)
∂⃗xA∂⃗xB
· ⃗e µ
B.
(A2)
We will now show that the eigenvectors corresponding to
overall rigid translations and rotations of the molecule
are zero frequency modes.
We assume that the equilibrium state of the molecule
is invariant under rigid spatial translations and rotations.
This assumption makes sense to ensure that the equilib-
rium state of interest to us is one where the molecule is
isolated and does not interact with its large scale envi-
ronment. If the molecule is invariant under translations,
then the forces acting on the individual atoms must also
be invariant. In its equilibrium state, the total force act-
ing on each atom must vanish, therefore the gradient of
the potential energy function must vanish:
0 = ∂U(⃗x0C)
∂⃗xA
= ∂U(⃗x0C + λ⃗τ)
∂⃗xA
,
(A3)
where ⃗τ is an arbitrary vector that describes the same
translation for all the atoms in the molecule, and where λ
is an arbitrary parameter that determines the magnitude
of the translation. We can express the forces acting on
each atom of a molecule that has been translated by an
inﬁnitesimal amount using a Taylor series expansion:
0 = ∂U(⃗x0C + λ⃗τ)
∂⃗xA
= ∂U(⃗x0C)
∂⃗xA
+ λ
X
B
∂2U(⃗x0C)
∂⃗xA∂⃗xB
· ⃗τ + O(λ2). (A4)
The ﬁrst term on the right side of Eq. (A4) vanishes be-
cause of the equilibrium condition, Eq. (A3). Therefore,
the second term on the right side of Eq. (A4) must also
vanish for all values of λ. It follows that any vector ⃗τ
that is the same for all the atoms in a molecule is a zero-
frequency eigenvector:
0 =
X
B
∂2U(⃗x0C)
∂⃗xA∂⃗xB
· ⃗τ.
(A5)
The argument for the rotational invariance of the equi-
librium state of the molecule is similar. Let R(λ) de-
note a one parameter family of rotation matrices. We
assume that λ = 0 corresponds to the identity rotation:
R(0) = I. The rotational invariance of the equilibrium
state of the molecule implies that
0 = ∂U[⃗x0C]
∂⃗xA
= ∂U[R(λ) · ⃗x0C]
∂⃗xA
.
(A6)
As before, we perform a Taylor expansion of the expres-
sion for the forces acting on an equilibrium molecule that
has been rotated an inﬁnitesimal amount:
0 = ∂U[R(λ) · ⃗x0C]
∂⃗xA
(A7)
= ∂U[⃗x0C]
∂⃗xA
+ λ
X
B
∂2U[⃗x0C]
∂⃗xA∂⃗xB
· dR
dλ

λ=0
· ⃗x0B
+O(λ2).(A8)
The derivative of any rotation matrix is an antisymmetric
matrix. In this case this matrix can be written as
dRij
dλ

λ=0
= −
X
k
ǫijkθk,
(A9)


## Page 15


15
where the vector ⃗θ determines the direction and magni-
tude of the inﬁnitesimal rotation. It follows that Eq. (A8)
can be re-written as
0 = ∂U[⃗x0C]
∂⃗xA
+ λ
X
B
∂2U[⃗x0C]
∂⃗xA∂⃗xB
·

⃗θ × ⃗x0B

+ O(λ2).
(A10)
The ﬁrst term on the right side of Eq. (A10) vanishes
because of the equilibrium condition, Eq. (A6). There-
fore, the second term on the right side of Eq. (A10) must
vanish for all values of λ. It follows that any vector of
the form ⃗θ × ⃗x0A, where ⃗θ is the same for all the atoms
in a molecule, is a zero-frequency eigenvector:
0 =
X
B
∂2U[⃗x0C]
∂⃗xA∂⃗xB
·

⃗θ × ⃗x0B

.
(A11)
The eigenvectors of the zero frequency modes (for
generic molecules) therefore consist of rigid translations
⃗e t
A(⃗τ) = ⃗τ,
(A12)
where ⃗τ is a constant vector that determines the magni-
tude and direction of the translation, and rigid rotations,
⃗e r
A(⃗θ) = ⃗θ × ⃗x0A,
(A13)
where ⃗θ is a constant vector that determines the axis and
magnitude of the rotation.
It is easy to show from Eq. (A1) that two eigenvectors,
⃗e µ
A and ⃗e ν
A, having diﬀerent eigenvalues, ω2
µ ̸= ω2
ν, are
orthogonal in the sense that,
0 =
X
A
mA
M ⃗e µ
A · ⃗e ν
A.
(A14)
It follows that the translations ⃗e t
A(⃗τ) = ⃗τ and rotations
⃗e r
A(⃗θ) = ⃗θ × ⃗x0A will be orthogonal to all of the non-
zero frequency mode eigenvectors ⃗e µ
A. These orthogonal-
ity conditions are given by:
0 =
X
A
mA
M ⃗e µ
A · ⃗e t
A(⃗τ) =
X
A
mA
M ⃗e µ
A · ⃗τ,
(A15)
0 =
X
A
mA
M ⃗e µ
A · ⃗e r
A(⃗θ)
= −
X
A
mA
M (⃗e µ
A × ⃗x0A) · ⃗θ.
(A16)
These orthogonality conditions will hold for arbitrary val-
ues of the vectors ⃗τ and ⃗θ. Therefore these conditions can
also be written in the form
0 =
X
A
mA
M ⃗e µ
A =
X
A
mA
M ⃗e µ
A × ⃗x0A.
(A17)
These conditions must hold for each non-zero frequency
mode µ, and therefore demonstrate that the constraints
on the mode-basis eigenvectors given in Eqs. (5) and (6)
are satisﬁed by the normal-mode basis vectors.
Appendix B: Quaternion Representation of R(t)
The diﬀerential equation that determines the rotation
matrix R(t),
dRij
dt
= −
X
kℓ
ǫikℓΩℓRkj,
(B1)
can be integrated numerically directly. Unfortunately the
accumulation of truncation and roundoﬀerrors in this di-
rect approach inevitably produces a solution that is no
longer a rotation matrix, and there is no reliable way to
project out these errors to retrieve the correct R(t). A
better approach is to adopt some parametric representa-
tion of the three-dimensional space of rotation matrices,
then to convert Eq. (B1) into a system of equations for
the evolution of those parameters, and ﬁnally to integrate
that parametric representation numerically. For exam-
ple, one common representation of the rotation matrices
uses the Euler angles as parameters.
Since the Euler
angle representation is not one to one (at a few singu-
lar points), a better representation uses unit quaternions
which do provide a one to one representation. We use the
quaternion representation for our numerical solutions of
R(t). Let q0 represent the real part, and q1, q2, and q3
the three independent imaginary parts of a quaternion
with
q2
0(t) + q2
1(t) + q2
2(t) + q2
3(t) = 1.
(B2)
This equation deﬁnes a unit three-sphere in this param-
eter space, so the space of possible parameter values is
three-dimensional. A general rotation matrix R can be
written in terms of these quaternion parameters in the
following way,
R = 2


q2
0 + q2
1 −1
2
q1q2 −q0q3
q1q3 + q0q2
q1q2 + q0q3
q2
0 + q2
2 −1
2
q2q3 −q0q1
q1q3 −q0q2
q2q3 + q0q1
q2
0 + q2
3 −1
2

. (B3)
It is then straightforward to transform the rotation ma-
trix evolution Eq. (B1) into an equation for the evolution
of the quaternion parameters. The result is
dq0(t)
dt
= −1
2(Ωxq1 + Ωyq2 + Ωzq3),
(B4)
dq1(t)
dt
= 1
2(Ωxq0 + Ωyq3 −Ωzq2),
(B5)
dq2(t)
dt
= 1
2(−Ωxq3 + Ωyq0 + Ωzq1),
(B6)
dq3(t)
dt
= 1
2(Ωxq2 −Ωyq1 + Ωzq0).
(B7)
Given a solution to these equations for q0(t), q1(t), q2(t)
and q3(t), it is easy to reconstruct the rotation matrix
R(t) using Eq. (B3).
The constraint,
C ≡q2
0 + q2
1 + q2
2 + q2
3 −1,
(B8)


## Page 16


16
which measures how well the quaternion parameters re-
main on the unit three-sphere, is preserved by the evo-
lution deﬁned by Eqs. (B4)–(B7).
In particular these
evolution equations imply
dC
dt = 0.
(B9)
Solving Eqs. (B4)–(B7) numerically will nevertheless re-
sult in truncation level violations of this constraint, so it
is necessary to re-scale the solution periodically to ensure
that C = 0. Without this re-scaling the R(t) constructed
using Eq. (B3) will not be a rotation matrix.
The numerical solution of Eqs. (B4)–(B7) can be
improved by adding constraint damping terms to the
system.
These extra terms vanish whenever the con-
straints are satisﬁed, thus leaving the desired solutions
unchanged. But these constraint damping terms are cho-
sen to drive the solution back toward the constraint sat-
isfying surface whenever small numerical constraint vio-
lations inevitably occur. The resulting quaternion evolu-
tion equation with constraint damping is given by,
dq0(t)
dt
= −1
2(Ωxq1 + Ωyq2 + Ωzq3) −1
8 η q0 C,
(B10)
dq1(t)
dt
= 1
2(Ωxq0 + Ωyq3 −Ωzq2) −1
8 η q1 C,
(B11)
dq2(t)
dt
= 1
2(−Ωxq3 + Ωyq0 + Ωzq1) −1
8 η q2 C,
(B12)
dq3(t)
dt
= 1
2(Ωxq2 −Ωyq1 + Ωzq0) −1
8 η q3 C.
(B13)
These equations imply the following evolution equation
for the constraint,
dC
dt = −η(C + 1)C,
(B14)
which drives constraint violations C toward zero exponen-
tially on a timescale set by the constant η when η > 0.
This is the form of the rotation matrix evolution equa-
tions used in all of our numerical solutions of the various
representations of the MD equations.
REFERENCES
1J.
A.
McCammon
and
S.
C.
Harvey,
Dynamics of proteins and nucleic acids
(Cambridge
Univer-
sity Press, 1987).
2M. Allen and D. Tildesley, Computer Simulation of Liquids (Ox-
ford Science Publications, 1987).
3D. Frenkel and B. Smit, Understanding Molecular Simulation,
2nd ed. (Academic Press, 2002).
4M. Karplus and J. A. McCammon, Nature Structural Biology 9,
646 (2002).
5R.
A.
Laskowski,
F.
Gerick,
and
J.
M.
Thornton,
FEBS Letters 583, 1692 (2009), Prague Special Issue:
Func-
tional Genomics and Proteomics.
6J. D. Durrant and J. A. McCammon, BMC biology 9, 1 (2011).
7X. Li, Appl. Mol. Dynam. in Atmospheric and Solution Chem.
(KTH Royal Institute of Technology, Stockholm, 2011).
8J. Wang and T. Hou, Journal of Chemical Theory and Computation 7, 2151 (2
9M. O. Steinhauser, “Molecular dynamics - studies of synthetic
and biological macromolecules,” (InTech, 2012) Chap. Introduc-
tion to Molecular Dynamics Simulations: Applications in Hard
and Soft Condensed Matter Physics, pp. 3–28.
10J. R. Perilla, B. C. Goh, C. K. Cassidy, B. Liu, R. C. Bernardi,
T. Rudack, H. Yu, Z. Wu, and K. Schulten, Current Opinion in
Structural Biology 31, 64 (2015).
11G.
Vettoretti,
E.
Moroni,
S.
Sattin,
J.
Tao,
D.
Agard,
A. Bernardi, and G. Colombo, Scientiﬁc Reports 6 (2016).
12H. Poincar´e, Acta Mathematica 13, 1270 (1890).
13S. D. Bond and B. J. Leimkuhler, Acta Numerica 16, 1 (2007).
14B. Leimkuhler and S. Reich, Simulating Hamiltonian Dynamics
(Cambridge University Press, 2004).
15E. B. Wilson Jr., The Journal of Chemical Physics 9, 76 (1941).
16J.-P. Ryckaert, G. Ciccotti,
and H. J. Berendsen, The Journal
of Computational Physics 23, 327 (1977).
17H. C. Andersen, The Journal of Computational Physics 52, 24
(1983).
18R. C. Smith, Uncertainty Quantiﬁcation (SIAM, 2014).
19P. N. Patrone, A. Dienstfrey, A. R. Browning, S. Tucker,
and
S. Christensen, Polymer 87, 246 (2016).
20S.
T.
Reeve
and
A.
Strachan,
Journal of Computational Physics 334, 207 (2017).
21F.
Rizzi,
H.
N.
Najm,
B.
J.
Debusschere,
K.
Sargsyan,
M.
Salloum,
H.
Adalsteinsson,
and
O.
M.
Knio,
Multiscale Modeling & Simulation 10, 1428 (2012).
22F.
Rizzi,
H.
N.
Najm,
B.
J.
Debusschere,
K.
Sargsyan,
M.
Salloum,
H.
Adalsteinsson,
and
O.
M.
Knio,
Multiscale Modeling & Simulation 10, 1460 (2012).
23F. C. Grogan, Comp. Tech. in M. D. and Det. Shock Dynam.,
Ph.D. thesis, University of California at San Diego (2017).
24M. Levitt, C. Sander,
and P. S. Stern, Journal of Molecular
Biology 181, 423 (1985).
25A. D. MacKerell, D. Bashford, M. Bellott, R. L. Dunbrack,
J. D. Evanseck, M. J. Field, S. Fischer, J. Gao, H. Guo, S. Ha,
D. Joseph-McCarthy, L. Kuchnir, K. Kuczera, F. T. K. Lau,
C. Mattos, S. Michnick, T. Ngo, D. T. Nguyen, B. Prodhom,
W. E. Reiher, B. Roux, M. Schlenkrich, J. C. Smith, R. Stote,
J. Straub, M. Watanabe, J. Wi´orkiewicz-Kuczera, D. Yin, and
M. Karplus, The Journal of Physical Chemistry B 102, 3586
(1998).
26W. H. Press, S. A. Teukolsky, W. T. Vetterling,
and B. P.
Flannery, Numerical Recipes in FORTRAN, 2nd ed. (Cambridge
University Press, Cambridge, England, 1992).
27E.
Hairer,
S.
P.
Nørsett,
and
G.
Wanner,
Solving Ordinary Diﬀerential Equations I (Springer, 2008).

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
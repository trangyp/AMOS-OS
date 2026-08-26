---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1303.3162v2
source: arxiv
tags: [arxiv, knowledge, math, quantum, reference]
---
# 1303.3162v2_Nonlinear_Inversion_from_Partial_EIT_Data__Computational_Experiments

> Source: 1303.3162v2_Nonlinear_Inversion_from_Partial_EIT_Data__Computational_Experiments.pdf

> Pages: 24

---


## Page 1


arXiv:1303.3162v2  [math.NA]  5 Feb 2014
NONLINEAR INVERSION FROM PARTIAL EIT DATA:
COMPUTATIONAL EXPERIMENTS
S. J. HAMILTON AND S. SILTANEN
Abstract. Electrical impedance tomography (EIT) is a non-invasive
imaging method in which an unknown physical body is probed with
electric currents applied on the boundary, and the internal conductivity
distribution is recovered from the measured boundary voltage data. The
reconstruction task is a nonlinear and ill-posed inverse problem, whose
solution calls for special regularized algorithms, such as D-bar methods
which are based on complex geometrical optics solutions (CGOs). In
many applications of EIT, such as monitoring the heart and lungs of
unconscious intensive care patients or locating the focus of an epileptic
seizure, data acquisition on the entire boundary of the body is impracti-
cal, restricting the boundary area available for EIT measurements. An
extension of the D-bar method to the case when data is collected only
on a subset of the boundary is studied by computational simulation.
The approach is based on solving a boundary integral equation for the
traces of the CGOs using localized basis functions (Haar wavelets). The
numerical evidence suggests that the D-bar method can be applied to
partial-boundary data in dimension two and that the traces of the partial
data CGOs approximate the full data CGO solutions on the available
portion of the boundary, for the necessary small k frequencies.
1. Introduction
1.1. EIT and the inverse conductivity problem. Electrical impedance
tomography (EIT) is a non-invasive imaging method where an unknown
physical body is probed with electric currents, and the internal conductiv-
ity distribution is recovered from the measurement data. The reconstruction
task is a nonlinear and ill-posed inverse problem, whose solution calls for spe-
cial regularized algorithms, such as the D-bar method [KLMS09]. Applica-
tions of EIT include monitoring the heart and lungs of unconscious intensive
care patients, industrial process monitoring and underground prospecting.
Practical considerations typically restrict the boundary area available for
EIT measurements: for example, it is not sensible to cover a patient com-
pletely with electrodes when imaging the heart. In this paper we study a
possible extension of the D-bar method to the case when data is collected
only on a subset of the boundary. See Figure 1. The mathematical model
2010 Mathematics Subject Classiﬁcation. Primary 65N21, 35R30; Secondary 45Q05.
Key words and phrases. Inverse problem, Numerical solver, Conductivity equation,
Inverse conductivity problem, Complex geometrical optics solution, Nonlinear Fourier
transform, Electrical impedance tomography.
SalWe Research Program for Mind and Body (Tekes - the Finnish Funding Agency for
Technology and Innovation grant 1104/10).
Academy of Finland (Finnish Centre of Excellence in Inverse Problems Research 2012–
2017, decision number 250215).
1


## Page 2


2
S. J. HAMILTON AND S. SILTANEN
Γ
Figure 1. Left: original conductivity. Middle: reconstruc-
tion from full-boundary data using the D-bar method. Right:
reconstruction from partial-boundary data using the pro-
posed method. The subset Γ ⊂∂Ωwhere the measurements
are available is denoted by a black line, which corresponds to
25% of the entire boundary
of EIT is the inverse conductivity problem introduced by Calder´on [Cal80].
Let Ω⊂Rn be a bounded and simply connected set with a smooth boundary
∂Ω. Let σ : Ω→R be an essentially bounded measurable function satisfying
σ(x) ≥c > 0 for almost every x ∈Ω. Let u ∈H1(Ω) be the unique solution
to
∇· σ∇u
=
0 in Ω,
(1.1)
u

∂Ω
=
φ ∈H1/2(∂Ω).
(1.2)
The inverse conductivity problem is to recover the conductivity σ from the
Dirichlet-to-Neumann (D-N) map deﬁned by
Λσ : φ 7→σ∂u
∂ν

∂Ω.
Here ν = (ν1, ν2) = ν1 + iν2 is the unit outward facing normal vector to the
boundary. Here φ is a voltage distribution applied on the boundary, and
Λσφ is the resulting current ﬂux through the boundary. Therefore, Λσ can
be seen as an ideal inﬁnite-precision model of practical voltage-to-current
measurements.
Calder´on asked two main questions in his seminal article [Cal80]:
(i) Is σ uniquely determined by Λσ?
(ii) If the answer to (i) is yes, how can one calculate σ from Λσ?
In practical EIT imaging only a ﬁnite-range and noisy approximate operator
Λδ
σ is available. In general, Λδ
σ is not the D-N map of any conductivity. We
usually only know that ∥Λδ
σ −Λσ∥Y ≤δ. Here Y is an appropriate data
space and δ > 0 can be determined from the properties of the measurement
device. This leads us to a third question:
(iii) Given Λδ
σ and δ, how can one design a continuous map from Y to
L∞(Ω) whose output is a useful approximation to σ?
As the inverse conductivity problem is ill-posed, the forward map A : σ 7→
Λσ does not have a continuous inverse. Therefore, question (iii) needs to
be answered by constructing a regularization strategy [EHN96]. More pre-
cisely, a family of continuous mappings Rα : Y →L∞(Ω) must be deﬁned,


## Page 3


NONLINEAR INVERSION FROM PARTIAL EIT DATA
3
Model space
Data space
L∞(Ω)
Y
σ
A
δ
Rα
Λσ
A(D(A))
D(A)
Λδ
σ
Rα(Λδ
σ)
Figure 2. Schematic illustration of nonlinear regulariza-
tion of the eit problem. Here the forward map is deﬁned
as A(σ) = Λσ with the domain of deﬁnition denoted by
D(A) ⊂L∞(Ω).
The conductivity σ is approximately re-
covered as Rα(Λδ
σ).
parameterized by 0 < α < ∞, such that
(1.3)
lim
α→0 ∥Rα(Λσ) −σ∥L∞(Ω) = 0,
for each ﬁxed σ. Note that (1.3) is closely related to question (ii) above.
Furthermore, one needs to specify a choice α = α(δ) for the regularization
parameter as a function of the noise level so that α(δ) →0 as δ →0. Finally,
the reconstruction error ∥Rα(δ)(Λδ
σ)−σ∥L∞(Ω) must vanish in the zero noise
limit: for any ﬁxed σ we must have
(1.4)
sup
Λδσ∈Y
n
∥Rα(δ)(Λδ
σ) −σ∥L∞(Ω) : ∥Λδ
σ −Λσ∥Y ≤δ
o
→0 as δ →0.
For more details, see Figure 2 and [KLMS09, MS12].
1.2. D-bar methods for full-boundary data. From the practical view-
point, the solution of the inverse conductivity problem is a computational
algorithm that implements a regularization strategy Rα satisfying (1.3) and
(1.4). Achieving such a goal is typically a large project involving several
milestones, often corresponding to one of the following two types:
(a) A theoretical breakthrough that outlines a computational approach
(b) Successful computational experiments that inspire further theoreti-
cal study
Let us review the history of a speciﬁc two-dimensional D-bar method for
EIT in light of (a) and (b).
1996(a):
Nachman showed uniqueness (i) and introduced a inﬁnite-
precision reconstruction method (ii) for twice diﬀerentiable conductivities
in [Nac96]. The proof used a nonlinear Fourier transform based on so-called
complex geometrical optics (CGO) solutions, ﬁrst deﬁned by Faddeev in
1966 [Fad66] and later rediscovered in 1987 by Sylvester and Uhlmann in
the context of 3D EIT [SU87]. Thus, [Nac96] represents a breakthrough
in the form of (a) since it is the basis of the ﬁrst numerical D-bar method
[SMI00, SMI01, MS03].


## Page 4


4
S. J. HAMILTON AND S. SILTANEN
2004(b): Isaacson et al. demonstrated in [IMNS04, IMNS06] that the
D-bar method performs well on practical data measured from laboratory
phantoms and from human subjects. The mandatory regularization step
was provided by low-pass ﬁltering in the nonlinear frequency domain. The
need for such ﬁltering is evident from the structure of the experimental
nonlinear Fourier transforms: they blow up outside a disc centered at the
origin.
2009(a): The numerical evidence from practical imaging experiments
[IMNS04, IMNS06] inspired a rigorous regularization proof of convergence
in the form of (1.4), see [KLMS09]. This gave an answer to (iii) and outlined
a method for choosing the regularization parameter as the inverse of the
nonlinear cutoﬀfrequency. We outline the reconstruction method in Section
2 below.
There is an analogous history for other uniqueness proofs and related algo-
rithms in two-dimensions. We review them brieﬂy below without specifying
explicitly the progress steps of types (a) and (b).
Brown and Uhlmann were able to prove uniqueness for real-valued con-
ductivities assuming only one derivative in [BU97]. This result was com-
plemented by constructive steps and numerical implementation by Knudsen
and Tamasan [KT04, Knu02, Knu03]; see also [KMS04]. Francini [Fra00]
extended the uniqueness proof to complex conductivities whose real and
imaginary parts are twice diﬀerentiable, and her approach was subsequently
implemented in [HHMV12, Ham12, HM13, Her12]. We outline this recon-
struction method in Section 3 below. Both methods involve transforming
(1.1) to a ﬁrst order system of ∂z and ∂z equations.
Astala and P¨aiv¨arinta answered Calder´on’s questions (i) and (ii) in their
original smoothness category σ ∈L∞(Ω), see [AP06b, AP06a]. This ap-
proach has been implemented numerically as well [AMPS10, AMP+11].
Despite the above developments, some questions still remain open:
• Is it possible to give a regularization analysis (iii) for less smooth con-
ductivities than twice diﬀerentiable? There is numerical evidence
of type (b) available since all of the above EIT methods produce
noise-robust images when applied to data arising from discontin-
uous conductivities and regularized by nonlinear low-pass ﬁltering
[KLMS08, KLMS07, HHMV12, AMP+11].
• Can the D-bar methodology be used in the case of partial-boundary
data? We discuss this in Section 1.3 below in the two-dimensional
case.
1.3. Extension to partial-boundary data. It is of high practical im-
portance to be able to compute EIT reconstructions from data measured
only on a part of the boundary. One possibility for designing such algo-
rithms would be to take one of the recent theoretical breakthroughs, such as
[Knu06, KSU07, NS10, IUY10], and implement it in the spirit of (a) above.
However, we do not discuss such approaches in this paper. We proceed along
(b) and produce novel numerical evidence suggesting that it may be possible
to use the classical D-bar approach for partial data reconstructions. It is our
hope that these computational results inspire further theoretical advances.


## Page 5


NONLINEAR INVERSION FROM PARTIAL EIT DATA
5
Our starting point is the assumption that only a proper subset Γ ⊂∂Ωis
available for measurements. We consider voltage-to-current data represented
ideally by the restricted D-N map eΛσ, deﬁned as follows. Let eφ ∈H1/2(∂Ω)
satisfy supp(eφ) ⊂Γ and let u ∈H1(Ω) be the unique solution of the con-
ductivity equation
∇· σ∇u
=
0 in Ω,
(1.5)
u

∂Ω
=
eφ.
(1.6)
Our partial D-N map is then deﬁned by
(1.7)
eΛσ : eφ 7→σ∂u
∂ν

Γ.
The practical data is a ﬁnite-range and noisy approximate operator eΛδ
σ sat-
isfying ∥eΛδ
σ −eΛσ∥Y ≤δ.
Let us brieﬂy explain our approach in the context of the regularized D-
bar method [KLMS09] based on Nachman’s uniqueness proof [Nac96]. In the
full-boundary data case, it begins by solving this Fredholm integral equation
of the second kind for the (approximate) traces of the CGO solutions on ∂Ω:
(1.8)
ψ(z, k) = eikz −
Z
∂Ω
Gk(z −ζ)(Λδ
σ −Λ1)ψ(ζ, k) dS(ζ),
z ∈∂Ω,
where Gk is the Faddeev Green’s function [Fad66], here deﬁned in the sense
of tempered distributions,
(1.9)
Gk(z) := eikzgk(z),
gk(z) :=
1
(2π)2
Z
R2
eiz·ξ
|ξ|2 + 2k(ξ1 + iξ2)dξ.
In the case of partial-boundary data, we solve the following equation for
the unknown functions ω( · , k) : Γ →C:
(1.10) ω(z, k) = eikz −
Z
Γ
Gk(z −ζ)(eΛδ
σ −eΛ1)ω(ζ, k) dS(ζ),
z ∈Γ ⊂∂Ω.
Now the hypothesis is that
(1.11)
ψ(z, k)|Γ ≈ω(z, k),
z ∈Γ ⊂∂Ω,
for some k ∈C.
If (1.11) holds, it opens up a variety of extensions of D-bar methods to
partial-boundary data applications.
1.4. Focus of this paper. How does one solve (1.10) numerically? Com-
putational solution methods for boundary integral equations (BIEs) of type
(1.8), corresponding to the continuum model, have most often been based on
representing the unknown CGO solutions in terms of (generalized) trigono-
metric bases, where the basis functions are essentially supported on the
entire boundary [KLMS09, AMP+11, MS12]. This approach is not directly
applicable to partial data problems. In this work we present new numerical
experiments on the unit disc (without loss of generality) involving the solu-
tion of the above-mentioned BIEs using localized basis functions supported
only on a subset of the boundary, in this case the Haar wavelets which
are naturally applicable to the partial (as well as full) boundary continuum
model. See Figure 3.


## Page 6


6
S. J. HAMILTON AND S. SILTANEN
Trigonometric basis functions and
corresponding electrode inputs:
for full-boundary data
Haar wavelet functions and
corresponding electrode inputs:
for both full and partial data
Figure 3. Illustration of various basis functions used for
solving boundary integral equations. Also shown are voltage
patterns applied using 32 electrodes, approximating the basis
functions.
The right-hand side functions and patterns are
localized and therefore may be more suitable for working with
partial-boundary data.
Let us stress that at present there is no proof available for the solvability
of equation (1.10). However, we did not encounter any problems when nu-
merically solving (1.10), suggesting that it may be possible to prove unique
solvability under appropriate assumptions.
We demonstrate that it is possible to recover the traces of the CGO solu-
tions approximately on the part of the boundary available for measurements.
In other words, the approximation in (1.11) is quite good in the C2 and dis-
continuous conductivity examples we consider. In addition, we show below
that these partial traces lead to interesting and useful reconstructions of
practically relevant discontinuous conductivities.
Our new results may be useful in extending three-dimensional D-bar re-
constructions, such as [CKS06, BIK+08, BKM11, DHK0], to partial-boundary
data.
We mention that numerical reconstructions using restricted information
about the conductivity have been published in cases of partial-boundary
data, see [MIN99, IIN+07, IINS10, UW08]. The present work diﬀers from
those in that we aim to recover the full unknown conductivity function
instead of inclusions in a known background.
Also, there is an alterna-
tive methodology for partial-data EIT based on resistor networks [Mam10,
BDMGV10, BDM10]; our work again represents a very diﬀerent approach.
Finally, we mention that there is a large body of work on iterative solution
methods for EIT in cases of partial data; those studies are fundamentally
diﬀerent from our direct (non-iterative) approach.


## Page 7


NONLINEAR INVERSION FROM PARTIAL EIT DATA
7
2. Method 1: The method based on the Schr¨odinger equation
As mentioned above, the proof by [Nac96] transforms the conductivity
equation (1.5) to the Schr¨odinger equation
(−∆+ q(z)) ψ(z, k) = 0,
z ∈Ωand k ∈C,
via the change of variables ψ(z, k) = √σu(z, k), where
q(z) = ∆
p
σ(z)
p
σ(z)
,
denotes the Schr¨odinger potential and R2 is associated with C via z =
(x, y) = x + iy. Without loss of generality, the conductivity σ is assumed to
be 1 near ∂Ωand then extended to 1 in all of C. Existence and uniqueness are
then studied for the well known Schr¨odinger equation with CGO solutions
ψ that are asymptotic to eikz and kz = (k1 + ik2)(x + iy).
The alternative Lippmann-Schwinger formulation
(2.1)
µ(z, k) = 1 −gk ∗(qµ) ,
z, k ∈C,
of the Schr¨odinger equation uses the related CGO solutions µ(z, k) = e−ikzψ(z, k)
where gk is related to the Faddeev Green’s function and deﬁned in (1.9).
The reconstruction method of Nachman [Nac96] from inﬁnite-precision
data consists of the following two steps:
Λσ
1
−→t(k)
2
−→σ.
Step 1: From boundary measurements Λσ to the scattering trans-
form t.
For each ﬁxed k ∈C, solve in H1/2(∂Ω) the integral equation
(2.2)
ψ(z, k) = eikz −
Z
∂Ω
Gk(z −ζ)(Λσ −Λ1)ψ(ζ, k) dS(ζ),
z ∈∂Ω,
for the CGO solutions ψ where the D-N map of the homogeneous
conductivity 1 is denoted by Λ1. Then, substitute ψ into the formula
for the nonlinear scattering transform t : C →C:
t(k) =
Z
∂Ω
ei¯k¯z(Λσ −Λ1)ψ(z, k) dS(z),
(2.3)
where dS denotes arclength measure on ∂Ω.
Step 2: From the scattering transform t to the conductivity σ.
Denote e(z, k) := exp(i(kz + kz)). For each ﬁxed z ∈Ω, solve the
integral equation
µ(z, k) = 1 +
1
(2π)2
Z
R2
t(k′)
(k −k′)¯k′ e(−z, k′)µ(z, k′)dk′
1dk′
2,
(2.4)
then the conductivity is recovered by σ(z) = µ(z, 0)2.
The integral equation (2.4) was obtained from a corresponding partial dif-
ferential equation, a so-called D-bar equation, which involves the derivative
with respect to the complex variable k. This is where the D-bar method
gets its name.


## Page 8


8
S. J. HAMILTON AND S. SILTANEN
3. Method 2: The method based on a ∂z and ∂z system
As the existence/uniqueness result by Francini [Fra00] holds for complex
admittivities γ = σ+iωǫ, where ω is the frequency of the applied current and
ǫ denotes the electrical permittivity, and is an extension of that by Brown
and Uhlmann [BU97] we will formulate the problem in the complex case.
Let u1(z, k) and u2(z, k) be two CGO solutions to (1.5) with asymptotic
behavior eikz
ik
and eik¯z
−ik , respectively.
Introduce a matrix Ψ(z, k) of CGO
solutions related to u1 and u2 by

Ψ11
Ψ21

= γ1/2
 ∂z u1
∂z u1

,

Ψ12
Ψ22

= γ1/2
 ∂z u2
∂z u2

,
for z ∈Ωand k ∈C. The transformed system is then
(3.1)
DΨ = QΨ,
where D is a matrix of ∂z and ∂z partial derivatives and Q represents a
matrix potential
Q(z) =

0
−1
2∂z log γ(z)
−1
2 ¯∂z log γ(z)
0

,
D =

∂z
0
0
∂z

.
(3.2)
The admittivity γ is assumed to be 1 near ∂Ωand is extended to 1 in all
of C. Existence and uniqueness of solutions are then studied for (3.1) for
z ∈C instead of (1.5). As it is more practical to work with CGOs with
ﬁnite asymptotic behavior, we often make use of the related matrix of CGO
solutions M(z, k) ∼

1
0
0
1

deﬁned by
(3.3) M(z, k) = Ψ(z, k)

e−izk
0
0
ei¯zk

=

e−izkΨ11(z, k)
ei¯zkΨ12(z, k)
e−izkΨ21(z, k)
ei¯zkΨ22(z, k)

.
Similarly to Method 1, the full data direct reconstruction algorithm [HHMV12]
also involves solving Fredholm integral equations of the second kind for CGO
solutions using D-N data, evaluating a nonlinear scattering transform S(k),
solving a ∂k equation, and using the recovered CGO solutions at k = 0 to
reconstruct the conductivity and permittivity. The method can be summa-
rized in the following steps:
Λγ
1
−→S(k)
2
−→M(z, 0)
3
−→γ.
Step 1: From boundary measurements Λγ to the scattering trans-
form S.
For ﬁxed k ∈C \0, solve Fredholm integral equations of the second
kind on ∂Ωfor the traces of the CGO solutions u1(z, k) and u2(z, k):
u1(z, k)
=
eikz
ik −
Z
∂Ω
Gk(z −ζ)(Λγ −Λ1)u1(ζ, k)dS(ζ),
z ∈∂Ω
(3.4)
u2(z, k)
=
e−ik¯z
−ik −
Z
∂Ω
Gk(−¯z + ζ)(Λγ −Λ1)u2(ζ, k)dS(ζ),
z ∈∂Ω.
(3.5)


## Page 9


NONLINEAR INVERSION FROM PARTIAL EIT DATA
9
Use the traces of u1 and u2 to compute the oﬀdiagonal entries of
the CGO solutions Ψ(z, k) for z ∈∂Ωfrom the BIEs
Ψ12(z, k)
=
Z
∂Ω
ei¯k(z−ζ)
4π(z −ζ) [Λγ −Λ1] u2(ζ, k) dS(ζ),
z ∈∂Ω
(3.6)
Ψ21(z, k)
=
Z
∂Ω
 eik(z−ζ)
4π(z −ζ)

[Λγ −Λ1] u1(ζ, k) dS(ζ),
z ∈∂Ω,
(3.7)
and compute the oﬀ-diagonal entries of the scattering matrix S(k)
S12(k)
=
i
2π
Z
∂Ω
e−i¯kzΨ12(z, k)(ν1 + iν2)dS(z),
k ∈C
(3.8)
S21(k)
=
−i
2π
Z
∂Ω
ei¯k¯zΨ21(z, k)(ν1 −iν2)dS(z),
k ∈C .
(3.9)
Interpolate the scattering data S(k) to include k = 0.
Step 2: From the scattering transform S(k) to CGO solutions M(z, 0).
Solve the ∂k equation (3.10) for the matrix M(z, k)
(3.10)
∂kM(z, k) = M(z, ¯k)

e(z, ¯k)
0
0
e(z, −k)

S(k).
Step 3: From CGO solutions M(z, 0) to the Admittivity γ = σ + iωǫ.
Reconstruct the matrix potential Q from
(3.11)
Q12(z) = ∂z M+(z, 0)
M−(z, 0) ,
Q21(z) = ∂z M−(z, 0)
M+(z, 0) ,
where
M+(z, k)
=
M11(z, k) + e−i(kz+¯k¯z)M12(z, k)
(3.12)
M−(z, k)
=
M22(z, k) + ei(kz+¯k¯z)M21(z, k),
(3.13)
and use either Q12 or Q21 to recover γ
(3.14) γ(z) = exp

−2
π
Z
Ω
Q12(ζ)
¯z −¯ζ dµ(ζ)

= exp

−2
π
Z
Ω
Q21(ζ)
z −ζ dµ(ζ)

,
where the integration takes place over Ωrather than all of C due to
the compact support of the matrix potential Q.
4. Computation of Partial Boundary Data CGO Solutions
In this work we use localized basis functions in place of global basis func-
tions. As mentioned above, the most commonly used global basis functions
for the continuum model are the exponential trigonometric basis functions
einθ. When electrode models (such as the gap, shunt, or complete electrode
model) are used, a trigonometric basis of sines and cosines is often used
instead [DM10, IMNS04]. As mentioned above, the common thread of these
global basis functions is that their support is essentially the entire boundary
of the domain. By contrast, localized basis functions are supported on a
subset of the boundary. Examples of localized basis patterns include the
skip patterns and adjacent patterns (see e.g., [Ham12, Mur07, HM13]) as


## Page 10


10
S. J. HAMILTON AND S. SILTANEN
well as the Haar wavelets. In this work we use the Haar wavelets as they are
localized basis functions that can be naturally used in both the continuum
and electrode model cases.
As the boundary integral equations in Methods 1 and 2 are very similar,
we will describe, without loss of generality, the computation in detail for
Method 1. In order to solve the boundary integral equation (2.2)
ψ(z, k) = eikz −
Z
∂Ω
Gk (z −ζ) (Λσ −Λ1) ψ(ζ, k) dS(ζ),
z ∈∂Ω,
for the traces of the CGO solutions ψ(z, k), we will need the Dirichlet-to-
Neumann (D-N) map, and thus we must ﬁrst discuss the applied voltage
patterns, in this case, the Haar wavelets.
4.1. Description of Haar Wavelets. Let Γ denote a subset of the bound-
ary ∂Ωand let |Γ| = L denote the length of the subset Γ. The ﬁrst wavelet
is the scaling function which we will denote φ1, and is deﬁned as:
(4.1)
φ1(z)
=
h1
z ∈Γ ⊆∂Ω
h1
=
q
1
L.
If z ∈∂Ω\Γ, the scaling function φ1(z) is set to zero, as will be the case for
the subsequent Haar wavelets.
For ease of notation, let d(z) be the distance, along the subset Γ of the
boundary, a point z is from the beginning point z0 on Γ (corresponding to
the smallest θ value in the traditional counter-clockwise orientation) and zL
the ending point (corresponding to the largest θ value). Thus, d = 0 at z0
and d = L at zL.
The second wavelet is the so-called mother wavelet which we will denote
φ2 and is deﬁned as:
(4.2)
φ2(z) =
(
h1,

z ∈Γ
0 ≤d(z) < L
2
	
−h1,

z ∈Γ
L
2 ≤d(z) ≤L
	
.
As the basis functions need to be orthonormal, we require ⟨φm, φn⟩= δm,n,
which the above wavelets satisfy by construction.
The third and fourth Haar wavelets φ3 and φ4 are copies of the mother
wavelet φ2, squished into 1/2 the length of the support of φ2 as follows:
(4.3)
φ3(z) =
(
h2,

z ∈Γ
0 ≤d(z) < L
4
	
−h2,

z ∈Γ
L
4 ≤d(z) ≤L
2
	
,
φ4(z) =
(
h2,

z ∈Γ
 L
2 ≤d(z) < 3L
4
	
−h2,

z ∈Γ
 3L
4 ≤d(z) ≤L
	
,
h2 =
q
2
L.
Notice that these new wavelets satisfy ⟨φm, φn⟩= δm,n for m, n = 1, . . . , 4.
An exact formula for the j-th height function hj is
hj =
r
2j−1
L ,
j ≥1,


## Page 11


NONLINEAR INVERSION FROM PARTIAL EIT DATA
11
corresponding to Haar wavelets with support width wj
wj =
L
2j−1 ,
j ≥2.
4.2. Formation of the D-N map Using Haar Wavelets. As the main
goal is to use only partial boundary data, thus applying and measuring
data only on subset of the domain, it is more natural to apply voltages
(rather than currents) and form the Dirichlet-to-Neumann (D-N) map di-
rectly. Although in practice currents are frequently applied, and thus the
Neumann-to-Dirichlet (N-D) map is formed ﬁrst (which is done to dampen
noise), that approach requires the inversion of the N-D map, which for par-
tial data poses new questions. As a preliminary approach, we proceed with
Dirichlet data.
The conductivity equation (1.5) can be solved using the Finite Element
Method. For each Haar wavelet, the Dirichlet boundary value problem is
solved and the resulting solution u in Ωis used to determine the current
ﬂux (Neumann data) at the boundary. This allows the determination of the
Neumann data corresponding to the prescribed Dirichlet data and formation
the D-N map:
Λσf = σ ∂u
∂ν

∂Ω
.
Note that for the cases in this document, the conductivity on and near the
boundary is 1.
The discrete matrix approximation to the D-N map is formed using the
following formula for the (m, n)-th entry
(4.4)
ΛM
σ (m, n) := ⟨Λσφm, φn⟩= ⟨σ∇φm · ν, φn⟩= ⟨∇φm · ν, φn⟩,
where φj are the Haar wavelets described in Section 4.1 that now serve as
the Dirichlet data and ⟨·, ·⟩denotes the L2 inner product. As ν denotes the
outward facing unit normal and Ωis the unit disc, at the boundary point
z = eiθ = cos(θ) + i sin(θ), we have ν = (cos(θ), sin(θ)).
4.3. Solution of the Full Data BIE. After forming the D-N map us-
ing the Haar wavelets, localized basis functions, we proceed to solving the
boundary integral equation for the traces of CGO solutions ψ(z, k). This
involves the solution of a Fredholm integral equation of the second kind. Fol-
lowing the approach of [DM10, HHMV12, HM13, Ham12], we expand the
exponential eikz and CGOs ψ(z, k) in the Haar wavelet patterns {Φj}J
j=1.
Let zℓbe an evaluation point on ∂Ωand J denote the number of linearly
independent Haar wavelet functions used. Then the values of the CGO so-
lution ψ and complex exponential eikz, for a given complex number k, at
position zℓon ∂Ωare given by
(4.5)
ψ(zℓ, k) ≈
J
X
j=1
bj(k)Φj
ℓ,
and
(4.6)
eikzℓ≈
J
X
j=1
cj(k)Φj
ℓ,


## Page 12


12
S. J. HAMILTON AND S. SILTANEN
where Φ denotes the normalized Haar wavelets such that their ℓ2 norm is 1,
i.e. they are related via
Φj =
r
L
Lφj.
Let b(k) denote the column vector b(k) = [b1(k), . . . , bJ(k)]T , and deﬁne
c(k) analogously where T denotes the standard matrix non-conjugate trans-
pose.
Let Eℓ′ denote the ℓ′-th subdivision of the boundary ∂Ω(ℓ′ = 1, . . . , L)
centered at the center of the ℓ′-th boundary element zℓ′ with length 2π/L.
Splitting the integral over ∂Ωinto a sum of integrals over the subsections
Eℓ′
ψ(zℓ, k)
≈
eikzℓ−
L
X
ℓ′=1
Z
Eℓ′
Gk (zℓ−ζ) δΛσψ(ζℓ′, k) dS(ζ)
=
eikzℓ−
L
X
ℓ′=1
Z
Eℓ′
Gk (zℓ−ζ) dS(ζ) [δΛσψ(ζℓ′, k)] ,
where for ease of notation
δΛσ = Λσ −Λ1.
Using the expansions for ψ(zℓ, k) and eikzℓ, (4.5) and (4.6) respectively, we
have
J
X
j=1
bj(k)Φj
ℓ
≈
J
X
j=1
cj(k)Φj
ℓ−
L
X
ℓ′=1
Z
Eℓ′
Gk (zℓ−ζ) dS(ζ)

δΛσ
J
X
j=1
bj(k)Φj
ℓ′


=
J
X
j=1
cj(k)Φj
ℓ−
L
X
ℓ′=1
Z
Eℓ′
Gk (zℓ−ζ) dS(ζ)
J
X
j=1
bj(k)fj (ζℓ′) ,
where fj (ζℓ′) denotes the action of the discretized δΛM
σ matrix on the j-th
normalized Haar wavelet basis function evaluated at ζℓ′. Deﬁne the matrix
approximation to the Faddeev Green’s function as
(4.7)
Gk(ℓ, ℓ′) =
(
Gk (zℓ, ζℓ′)
ℓ̸= ℓ′
0
ℓ= ℓ′,
removing the singularity at Gk(0). Then
(4.8)
J
X
j=1
bj(k)Φj
ℓ≈
J
X
j=1
cj(k)Φj
ℓ−2π
L
J
X
j=1
bj(k)
L
X
ℓ′=1
Gk(ℓ, ℓ′)fj (ζℓ′) .
Following [DM10]
(4.9)
fp(ζℓ′) ≈
 ΦδΛM
σ

(ℓ′, j),
i.e., the (ℓ′, j) entry in the matrix resulting from multiplication of the matrix
of normalized basis functions Φ and the discretized diﬀerence in D-N maps


## Page 13


NONLINEAR INVERSION FROM PARTIAL EIT DATA
13
δΛM
σ . Using the properties of matrix multiplication, equation (4.8) can be
rewritten as
J
X
j=1
bj(k)Φj
ℓ=
J
X
j=1
cj(k)Φj
ℓ−2π
L
J
X
j=1
bj(k)
 GkΦδΛM
σ

(ℓ, j),
or equivalently,
Φb = Φc −2π
L GkΦδΛM
σ b,
a matrix equation for the unknown coeﬃcients b which are needed in the
normalized Haar wavelet basis expansion of ψ(z, k).
Using the orthonormality of the normalized Haar wavelet basis functions
in the matrix Φ, we multiply both sides of the equation by ΦT, and then
solve
(4.10)
(I + A)b = c,
where
(4.11)
A = 2π
L ΦT GkΦδΛM
σ .
To reiterate, for each desired value of k ∈C, expand eikz for z ∈∂Ωin
the normalized Haar wavelets Φ to deﬁne the vector of coeﬃcients c, and
solve the system (4.10) using GMRES for the unknown coeﬃcients b. These
coeﬃcients are then used to reconstruct ψ(z, k) for the speciﬁed value of k
via (4.5).
4.4. Solution of the Partial Data BIE. We now proceed to the problem
of interest, namely, the solution of the boundary integral equation (2.2) when
only part of the boundary is accessible for data acquisition. The solution
method is nearly identical to the full data Haar wavelet case presented above.
Now Γ is a proper subset of the boundary ∂Ωand the Haar wavelets and
D-N map are formed as above. The D-N map now corresponds to data taken
only on the proper subset Γ since the applied voltage is 0 oﬀΓ.
Let ˜z denote the boundary values z restricted to Γ and ˜ψ the correspond-
ing partial data CGO solutions. We then expand eik˜z and ˜ψ as before and
solve the resulting system for each desired value of k ∈C:
(I + ˜A)˜b = ˜c,
where
(4.12)
˜A = L
L
˜ΦT ˜Gk ˜Φδ˜ΛM
σ ,
and L = |Γ|.
5. Numerical Reconstruction of Conductivities from Partial
Data Using Method 2
As stated above, the boundary integral equations (3.4) and (3.5) are
nearly identical to the BIE (2.2) described above for Method 1. Thus, their
traces on the subset Γ of the boundary can be recovered by solving analogous
formulas. The coeﬃcients ˜b1 for u1 are determined by solving
(I + ˜A)˜b1 = ˜c1,


## Page 14


14
S. J. HAMILTON AND S. SILTANEN
where ˜c1 are the coeﬃcients in the Haar expansion of eik˜z
ik . Similarly, the
coeﬃcients ˜b2 for u2 are determined by solving
(I + ˜
A2)˜b2 = ˜c2,
where ˜c2 are the coeﬃcients in the Haar expansion of e−ik˜z
−ik
and ˜A2 now
contains the matrix approximation of Gk(−¯z + ¯ζ) instead of Gk(z −ζ).
A natural question is whether these CGO solutions, which match very
well on Γ with their full data counterparts (see Section 6.1), can be used to
produce informative reconstructions of the conductivity (and/or permittiv-
ity) near the region of the accessible boundary. Our aim was to understand
the extent of the impact of the partial data CGO solutions on the remainder
of a D-bar algorithm. Therefore, as an initial test, we left the remainder of
the algorithm for Method 2 intact which means computing the intermediate
CGO solutions Ψ12 and Ψ21 using the partial D-N map and the partial data
CGO solutions u1 and u2, computing the scattering transforms S12 and S21
over Γ, and proceeding with Steps 2-3 as before. The steps of the proposed
partial data algorithm are included here for the reader’s convenience.
˜Λγ
1
−→˜S(k)
2
−→˜
M(z, 0)
3
−→˜γ.
Step 1: From partial boundary measurements ˜Λγ to the approx.
scattering transform ˜S(k).
For ﬁxed k ∈C \0 such that |k| < R a ﬁxed radius depending on the
measured D-N map, solve Fredholm integral equations of the second
kind on Γ ⊂∂Ωfor the approximate traces of the CGO solutions
˜u1(z, k) and ˜u2(z, k) on Γ ⊂∂Ω
˜u1(z, k)
=
eikz
ik

Γ
−
Z
Γ
Gk(z −ζ)(˜Λγ −˜Λ1)˜u1(ζ, k)dS(ζ),
z ∈Γ
(5.1)
˜u2(z, k)
=
e−ik¯z
−ik

Γ
−
Z
Γ
Gk(−¯z + ζ)(˜Λγ −˜Λ1)˜u2(ζ, k)dS(ζ),
z ∈Γ.
(5.2)
Use the approximate traces of u1 and u2 (namely, ˜u1 and ˜u2) to
compute the approximate oﬀdiagonal entries of the CGO solutions
eΨ(z, k) for z ∈Γ ⊂∂Ωfrom the BIEs
eΨ12(z, k)
=
Z
Γ
ei¯k(z−ζ)
4π(z −ζ)
h
˜Λγ −˜Λ1
i
˜u2(ζ, k) dS(ζ),
z ∈Γ
(5.3)
eΨ21(z, k)
=
Z
Γ
 eik(z−ζ)
4π(z −ζ)
 h
˜Λγ −˜Λ1
i
˜u1(ζ, k) dS(ζ),
z ∈Γ,
(5.4)
and compute the oﬀ-diagonal entries of the scattering matrix ˜S(k)
integrating over Γ ⊂∂Ω
˜S12(k)
=
i
2π
Z
Γ
e−i¯kz eΨ12(z, k)(ν1 + iν2)dS(z)
(5.5)
˜S21(k)
=
−i
2π
Z
Γ
ei¯k¯z eΨ21(z, k)(ν1 −iν2)dS(z).
(5.6)
Interpolate the approximate scattering data ˜S(k) to include k = 0.


## Page 15


NONLINEAR INVERSION FROM PARTIAL EIT DATA
15
Step 2: From the approx.
scattering transform ˜S(k) to approx.
CGO solutions f
M(z, 0).
Solve the ∂k equation (3.10) for the matrix of approx. CGO solutions
f
M(z, k)
(5.7)
∂k f
M(z, k) = f
M(z, ¯k)

e(z, ¯k)
0
0
e(z, −k)

˜S(k).
Step 3: From the approximate CGO solutions f
M(z, 0) to approx.
admittivity ˜γ = ˜σ + iω˜ǫ.
Reconstruct the approximate matrix potential ˜Q from
(5.8)
˜Q12(z) = ∂z f
M+(z, 0)
f
M−(z, 0)
,
˜Q21(z) = ∂z f
M−(z, 0)
f
M+(z, 0)
,
where
f
M+(z, k)
=
f
M11(z, k) + e−i(kz+¯k¯z) f
M12(z, k)
(5.9)
f
M−(z, k)
=
f
M22(z, k) + ei(kz+¯k¯z) f
M21(z, k),
(5.10)
and use either ˜Q12 or ˜Q21 to recover the approximation ˜γ
(5.11)
˜γ(z) = exp
(
−2
π
Z
Ω
˜Q12(ζ)
¯z −¯ζ dµ(ζ)
)
= exp
(
−2
π
Z
Ω
˜Q21(ζ)
z −ζ dµ(ζ)
)
,
where the integration takes place over Ωrather than all of C due to
the compact support of the matrix potential ˜Q.
For the numerical details regarding how to implement Steps 2-3 see [HHMV12,
Ham12, HM13].
6. Computational Experiments
We considered two test problems. Test 1 aims to determine how a partial
data D-N map aﬀects the values of the traces of the CGO solutions on the
accessible portion of the boundary. Test 2 aims to determine the eﬀect of
the partial data CGO solutions on a D-bar algorithm.
6.1. Test 1: Partial Data Traces of CGO Solutions. For the ﬁrst test
problem we considered the C2 smooth conductivity given in Figure 4. The
conductivity equation was ﬁrst solved using the Finite Element method with
256 Haar wavelets with essential support on the entire boundary, serving as
256 diﬀerent Dirichlet boundary conditions. We considered the 3/4, 1/2,
and 1/4 data problems with 192, 128, and 64 Haar wavelets respectively.
Each of the partial data cases is centered around z = 1, i.e. θ = 0.
Using Method 1, we solved the full data matrix formulation (4.10) of
the boundary integral equation for the traces of the CGO solutions ψ.
The partial data traces of the CGO solutions were recovered by solving
(4.12). In order to evaluate how well the reconstructed traces compare to
the true traces we also solved the Lippmann-Schwinger equation (2.1) using
the twice-diﬀerentiable conductivity in Figure 4.


## Page 16


16
S. J. HAMILTON AND S. SILTANEN
Figures 5 and 6 show the recovered traces of the CGO solutions ψ(z, k) for
k = 0.5 and −4i respectively, plotted against the true traces produced via
the Lippmann-Schwinger computation. Preliminary results suggest that for
small magnitude k, the partial data CGO solutions agree with the full data
(and true) solutions on the accessible part of the domain. As the magnitude
of the frequency parameter k increases, the partial data CGO solutions begin
to drift slightly from the full data solutions. However, in the nonlinear CGO
approaches typically used in EIT imaging, only low frequency CGO solutions
are used and therefore these results are very promising.
σ = 2
σ = 0.5
σ = 1
Figure 4. The C2 conductivity used in Test 1.
6.2. Test 2: D-Bar Reconstructions of Conductivities using Partial
Data CGO Solutions. In Test 1, we saw that the traces of the CGO so-
lutions computed using the partial D-N data corresponding to an accessible
subset Γ of the boundary ∂Ωmatch the true, as well as full data, traces
very well on Γ for low frequencies k and C2 smooth conductivities. Real
life situations often involve cases where the conductivities are not smooth
but instead only bounded. In order to determine if the traces of the partial
data CGO solutions still provide useful information when the smoothness is
relaxed, we consider the discontinuous test conductivity shown in Figure 7.
This test phantom could represent a saline ﬁlled tank containing an object
of higher conductivity.
As the smoothness condition for Method 2 is violated (as well as that for
Method 1), we cannot compare the full or partial data traces of the CGO
solutions to their “true” traces. Precisely, we cannot compute the potential
Q (or q) and the associated ∂z −∂z system (or Lippmann-Schwinger equa-
tion) for the “true” traces of the CGO solutions. Instead, we compare the
partial D-N data traces of the CGO solutions to the corresponding full D-N
data traces. Figures 8 and 9 shows the reconstructed traces of the CGO
solutions ˜u1 and ˜u2, respectively, for k = 3 + 3i resulting from the conduc-
tivity distribution in Figure 7 plotted for full, 3/4, 1/2, and 1/4 D-N data
with 256, 192, 128, and 64 Haar wavelets respectively. Clearly the partial


## Page 17


NONLINEAR INVERSION FROM PARTIAL EIT DATA
17
Real parts of ψ
Imaginary parts of ψ
True
Full data
3
4 data
1
2 data
1
4 data
All
−π
−π/2
0
π/2
π
−π
−π/2
0
π/2
π
Figure 5. Traces of the CGO solutions ψ corresponding to
the C2 conductivity in Figure 4. Here k = 0.5.
D-N data traces of the CGO solutions appear to approximate the full D-N
data traces of the CGO solutions in the accessible region Γ of the boundary.
Next we used the partial D-N data traces of the CGO solutions ˜u1 and
˜u2 in the modiﬁed D-bar algorithm for Method 2, described above in Sec-
tion 5, to determine their eﬀect on the algorithm and thus the reconstructed
conductivity distribution. Figures 10 and 11 show the reconstructed conduc-
tivity from full, 3/4, 1/2, and 1/4 D-N data using scattering data satisfying
|k| ≤3 and |k| ≤4, respectively. The range of the reconstructed values
decreases with the size of the accessible region of the boundary Γ, however
an object of higher conductivity is clearly visible in all cases. As the mag-
nitude of k increases the reconstructed values of the conductivity improve.
However, as in the full data D-N case, increasing the scattering radius too
much can introduce artifacts into the reconstruction.


## Page 18


18
S. J. HAMILTON AND S. SILTANEN
Real parts of ψ
Imaginary parts of ψ
True
Full data
3
4 data
1
2 data
1
4 data
All
−π
−π/2
0
π/2
π
−π
−π/2
0
π/2
π
Figure 6. Traces of the CGO solutions ψ corresponding to
the C2 conductivity in Figure 4. Here k = −4i.
Note that the reconstructions of the conductivity shown in Figures 10
and 11 are all plotted on their own scales. In both ﬁgures we are clearly
able to determine whether the inclusion is more or less conductive than the
background, as well as its approximate location, even from as little as 25%
D-N data.
Figure 12 shows the real and imaginary parts of the scattering transform
S21(k) for Full, 3/4, 1/2, and 1/4 data with |k| ≤4. Note that the scattering
data is clearly aﬀected by the loss of information in the D-N map, yet the
reconstructions of the conductivity (seen in Figures 10 and 11) continue to
contain valuable information. If one were to continue in this direction (using
the partial data D-bar algorithm described in Section 5) a more in-depth
study to determine which values of k are admissible in the scattering data
is recommended.


## Page 19


NONLINEAR INVERSION FROM PARTIAL EIT DATA
19
σ = 4
σ = 1
Figure 7. The discontinuous conductivity used in Test 2.
Real parts of u1
Imaginary parts u1
Full data
3
4 data
1
2 data
1
4 data
All
−π
−π/2
0
π/2
π
−π
−π/2
0
π/2
π
Figure 8. Traces of the CGO solutions u1 corresponding to
the discontinuous conductivity in Figure 7. Here k = 3 + 3i.


## Page 20


20
S. J. HAMILTON AND S. SILTANEN
Real parts of u2
Imaginary parts u2
Full data
3
4 data
1
2 data
1
4 data
All
−π
−π/2
0
π/2
π
−π
−π/2
0
π/2
π
Figure 9. Traces of the CGO solutions u2 corresponding to
the discontinuous conductivity in Figure 7. Here k = 3 + 3i.
Full Data
max = 1.19
min = 0.97
3
4 Data
max = 1.14
min = 0.93
1
2 Data
max = 1.10
min = 0.96
1
4 Data
max = 1.06
min = 0.97
|k| ≤3
Figure 10. Reconstructions of the discontinuous conduc-
tivity in Figure 7 produced using scattering data for |k| ≤3
using the method described in Section 5. From left to right,
the reconstructions are for Full, 3/4, 1/2, and 1/4 Dirichlet-
to-Neumann data.


## Page 21


NONLINEAR INVERSION FROM PARTIAL EIT DATA
21
Full Data
max = 1.38
min = 0.96
3
4 Data
max = 1.30
min = 0.82
1
2 Data
max = 1.24
min = 0.88
1
4 Data
max = 1.13
min = 0.96
|k| ≤4
Figure 11. Reconstructions of the discontinuous conduc-
tivity in Figure 7 produced using scattering data for |k| ≤4
using the method described in Section 5. From left to right,
the reconstructions are for Full, 3/4, 1/2, and 1/4 Dirichlet-
to-Neumann data.
Full Data
 
 
−0.035
0.035
 
 
−0.035
0.035
3
4 Data
 
 
−0.094
0.094
 
 
−0.124
0.126
1
2 Data
 
 
−0.036
0.036
 
 
−0.094
0.015
1
4 Data
 
 
−0.077
0.076
 
 
−0.085
0.059
Re S21
Im S21
Figure 12. Scattering transforms S21 for the discontinuous
conductivity in Figure 7 for |k| ≤4 using the method de-
scribed in Section 5.
From left to right, the plots are for
Full, 3/4, 1/2, and 1/4 Dirichlet-to-Neumann data.


## Page 22


22
S. J. HAMILTON AND S. SILTANEN
7. Conclusions
The ﬁrst step in nonlinear EIT imaging uses the voltage and current
boundary data to determine the traces of the CGO solutions at the bound-
ary. This is done by solving a boundary integral equation which is a Fred-
holm equation of the second kind, e.g., (2.2).
In this work, we used simulated partial boundary data and a wavelet-
based integral equation solver to demonstrate that CGO solutions can be
approximately recovered from partial data, on the part of the boundary
where the data was acquired. This result is clearly seen in Figures 5 and 6
for a C2 conductivity, and in Figures 8 and 9 for a discontinuous conductiv-
ity. In addition, we have demonstrated that such partial data CGO solutions
can be used in existing full data D-bar methods to provide useful and infor-
mative reconstructions, even in the case of discontinuous conductivities, see
Figures 10 and 11.
Acknowledgments
The study was supported by the SalWe Research Program for Mind and
Body (Tekes - the Finnish Funding Agency for Technology and Innovation
grant 1104/10) and by the Academy of Finland (Finnish Centre of Excellence
in Inverse Problems Research 2012–2017, decision number 250215).
References
[AMP+11]
K. Astala, J.L. Mueller, L. P¨aiv¨arinta, A. Per¨am¨aki, and S. Siltanen, Di-
rect electrical impedance tomography for nonsmooth conductivities, Inverse
Problems and Imaging 5 (2011), no. 3, 531–549.
[AMPS10]
K. Astala, J.L. Mueller, L. P¨aiv¨arinta, and S. Siltanen, Numerical compu-
tation of complex geometrical optics solutions to the conductivity equation,
Applied and Computational Harmonic Analysis 29 (2010), no. 1, 391–403.
[AP06a]
K. Astala and L. P¨aiv¨arinta, A boundary integral equation for Calder´on’s
inverse conductivity problem, Proc. 7th Internat. Conference on Harmonic
Analysis, Collectanea Mathematica, 2006.
[AP06b]
K. Astala and L. P¨aiv¨arinta, Calder´on’s inverse conductivity problem in the
plane, Annals of Mathematics 163 (2006), no. 1, 265–299.
MR 2195135
(2007b:30019)
[BDM10]
L. Borcea, V. Druskin, and A. V. Mamonov, Circular resistor networks
for electrical impedance tomography with partial boundary measurements,
Inverse Problems 26 (2010), no. 4, 045010, 30. MR 2608623 (2011f:65239)
[BDMGV10] L. Borcea, V. Druskin, A. V. Mamonov, and F. Guevara Vasquez, Pyramidal
resistor networks for electrical impedance tomography with partial boundary
measurements, Inverse Problems 26 (2010), no. 10, 105009, 36. MR 2719770
(2011f:65238)
[BIK+08]
G. Boverman, D. Isaacson, T.-J. Kao, Saulnier, G. J., and J. C. Newell,
Methods for direct image reconstruction for eit
in two and three dimen-
sions, Proceedings of the 2008 Electrical Impedance Tomography Confer-
ence (Dartmouth College, in Hanover, New Hampshire, USA), June 16 to
18 2008.
[BKM11]
J. Bikowski, K. Knudsen, and J. L. Mueller, Direct numerical reconstruction
of conductivities in three dimensions using scattering transforms, Inverse
Problems 27 (2011).
[BU97]
R. M. Brown and G. Uhlmann, Uniqueness in the inverse conductivity prob-
lem for nonsmooth conductivities in two dimensions, Communications in
Partial Diﬀerential Equations 22 (1997), no. 5, 1009–1027.


## Page 23


NONLINEAR INVERSION FROM PARTIAL EIT DATA
23
[Cal80]
A.-P. Calder´on, On an inverse boundary value problem, Seminar on Numer-
ical Analysis and its Applications to Continuum Physics (Rio de Janeiro,
1980), Soc. Brasil. Mat., Rio de Janeiro, 1980, pp. 65–73.
MR 590275
(81k:35160)
[CKS06]
H. Cornean, K. Knudsen, and S. Siltanen, Towards a d-bar reconstruction
method for three-dimensional eit , Journal of Inverse and Ill-Posed Problems
14 (2006), no. 2, 111–134. MR MR2242300 (2007f:65046)
[DHK0]
Fabrice Delbary, Per Christian Hansen, and Kim Knudsen, Electrical
impedance tomography: 3D reconstructions using scattering transforms, Ap-
plicable Analysis 0 (0), no. 0, 1–19.
[DM10]
M. DeAngelo and J. L. Mueller, 2D D-bar reconstructions of human chest
and tank data using an improved approximation to the scattering transform,
Physiological Measurement 31 (2010), 221–232.
[EHN96]
H.W. Engl, M. Hanke, and A. Neubauer, Regularization of inverse problems,
Kluwer Academic Publishers, 1996.
[Fad66]
L. D. Faddeev, Increasing solutions of the Schr¨odinger equation, Soviet
Physics Doklady 10 (1966), 1033–1035.
[Fra00]
E. Francini, Recovering a complex coeﬃcient in a planar domain from
Dirichlet-to-Neumann map, Inverse Problems 16 (2000), 107–119.
[Ham12]
S. J. Hamilton, A Direct D-bar reconstruction algorithm for complex admit-
tivies in W 2,∞(Ω) for the 2-D EIT problem, Ph.D. Thesis, Colorado State
University, Fort Collins, CO, Summer 2012.
[Her12]
C. N. L. Herrera, Um metodo D-bar para estimar admitividade em 2-D
atraves de tomograﬁa por impedancia electrica, Ph.D. Thesis, University of
S˜ao Paulo, S˜ao Paulo, Brazil, Fall 2012.
[HHMV12]
S. J. Hamilton, C. N. L. Herrera, J. L. Mueller, and A. VonHerrmann, A
direct D-bar reconstruction algorithm for recovering a complex conductivity
in 2-D, Inverse Problems 28 (2012), 095005.
[HM13]
S. J. Hamilton and J. L. Mueller, Direct EIT reconstructions of complex ad-
mittivities on a chest-shaped domain in 2-D, IEEE Transactions on Medical
Imaging 32 (2013), no. 4, 757–769.
[IIN+07]
T. Ide, H. Isozaki, S. Nakata, S. Siltanen, and G. Uhlmann, Probing for
electrical inclusions with complex spherical waves, Communications on pure
and applied mathematics 60 (2007), no. 10, 1415–1442.
[IINS10]
T. Ide, H. Isozaki, S. Nakata, and S. Siltanen, Local detection of three-
dimensional inclusions in electrical impedance tomography, Inverse problems
26 (2010), 035001.
[IMNS04]
D. Isaacson, J. L. Mueller, J. C. Newell, and S. Siltanen, Reconstructions
of chest phantoms by the D-bar method for electrical impedance tomography,
IEEE Transactions on Medical Imaging 23 (2004), 821–828.
[IMNS06]
D. Isaacson, J.L. Mueller, J.C. Newell, and S. Siltanen, Imaging cardiac ac-
tivity by the D-bar method for electrical impedance tomography, Physiological
Measurement 27 (2006), S43–S50.
[IUY10]
O.Y. Imanuvilov, G. Uhlmann, and M. Yamamoto, The Calder´on problem
with partial data in two dimensions, American Mathematical Society 23
(2010), no. 3, 655–691.
[KLMS07]
K. Knudsen, M. Lassas, J.L. Mueller, and S. Siltanen, D-bar method for elec-
trical impedance tomography with discontinuous conductivities, SIAM Jour-
nal on Applied Mathematics 67 (2007), no. 3, 893.
[KLMS08]
K. Knudsen, M. Lassas, J.L. Mueller, and S. Siltanen, Regularized D-bar
method for the inverse conductivity problem, Proceedings of the 4th AIP In-
ternational Conference and the 1st Congress of the IPIA, Journal of Physics:
Conference Series, 124, 2008.
[KLMS09]
, Regularized D-bar method for the inverse conductivity problem, In-
verse Problems and Imaging 3 (2009), no. 4, 599–624.


## Page 24


24
S. J. HAMILTON AND S. SILTANEN
[KMS04]
K. Knudsen, J.L. Mueller, and S. Siltanen, Numerical solution method for the
dbar-equation in the plane, Journal of Computational Physics 198 (2004),
500–517.
[Knu02]
K. Knudsen, On the inverse conductivity problem, Ph.D. thesis, Department
of Mathematical Sciences, Aalborg University, Denmark, 2002.
[Knu03]
, A new direct method for reconstructing isotropic conductivities in
the plane, Physiological Measurement 24 (2003), no. 2, 391–403.
[Knu06]
K. Knudsen, The Calder´on problem with partial data for less smooth conduc-
tivities, Communications in Partial Diﬀerential Equations 31 (2006), 57–71.
[KSU07]
Carlos E. Kenig, Johannes Sj¨ostrand, and Gunther A. Uhlmann, The
Calder´on problem with partial data, Annals of Mathematics 165 (2007),
no. 2, 567–591.
[KT04]
K. Knudsen and A. Tamasan, Reconstruction of less regular conductivities
in the plane, Communications in Partial Diﬀerential Equations 29 (2004),
361–381.
[Mam10]
Alexander Vasilyevich Mamonov, Resistor networks and optimal grids for the
numerical solution of electrical impedance tomography with partial boundary
measurements, ProQuest LLC, Ann Arbor, MI, 2010, Thesis (Ph.D.)–Rice
University. MR 2792941
[MIN99]
J.L. Mueller, D. Isaacson, and J. C. Newell, A reconstruction algorithm
for electrical impedance tomography data collected on rectangular electrode
arrays, IEEE Transactions on Biomedical Engineering 49 (1999), 1379–1386.
[MS03]
J.L. Mueller and S. Siltanen, Direct reconstructions of conductivities from
boundary measurements, SIAM Journal on Scientiﬁc Computing 24 (2003),
no. 4, 1232–1266.
[MS12]
, Linear and nonlinear inverse problems with practical applications,
SIAM, 2012.
[Mur07]
E. K. Murphy, 2-D D-Bar conductivity reconstructions on non-circular do-
mains, Ph.D. Thesis, Colorado State University, Fort Collins, CO, Fall 2007.
[Nac96]
A. I. Nachman, Global uniqueness for a two-dimensional inverse boundary
value problem, Annals of Mathematics 143 (1996), 71–96.
[NS10]
A. Nachman and B. Street, Reconstruction in the Calder´on problem with
partial data, Communications in Partial Diﬀerential Equations 35 (2010),
no. 2, 375–390.
[SMI00]
S. Siltanen, J. Mueller, and D. Isaacson, An implementation of the recon-
struction algorithm of A. Nachman for the 2-D inverse conductivity problem,
Inverse Problems 16 (2000), 681–699.
[SMI01]
, Reconstruction of high contrast 2-D conductivites by the algorithm
of A. Nachman, Proceedings of the 2000 conference on Radon transforms
and tomography (et. al. ed. Quinto, ed.), vol. 278, 2001, pp. 241–254.
[SU87]
J. Sylvester and G. Uhlmann, A global uniqueness theorem for an inverse
boundary value problem, Annals of Mathematics 125 (1987), 153–169.
[UW08]
Gunther Uhlmann and Jenn-Nan Wang, Reconstructing discontinuities using
complex geometrical optics solutions, SIAM J. Appl. Math. 68 (2008), no. 4,
1026–1044. MR 2390978 (2009d:35347)
University of Helsinki, Department of Mathematics and Statistics, P.O.
Box 68, FI-00014 Helsinki, Finland
E-mail address: sarah.hamilton@helsinki.fi
University of Helsinki, Department of Mathematics and Statistics, P.O.
Box 68, FI-00014 Helsinki, Finland
E-mail address: samuli.siltanen@helsinki.fi

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
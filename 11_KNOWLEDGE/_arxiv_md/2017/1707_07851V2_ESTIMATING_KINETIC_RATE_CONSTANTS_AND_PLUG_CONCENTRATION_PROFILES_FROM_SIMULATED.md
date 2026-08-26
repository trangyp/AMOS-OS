---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1707.07851v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1707.07851v2_Estimating_Kinetic_Rate_Constants_and_Plug_Concentration_Profiles_from_Simulated

> Source: 1707.07851v2_Estimating_Kinetic_Rate_Constants_and_Plug_Concentration_Profiles_from_Simulated.pdf

> Pages: 14

---


## Page 1


Estimating Kinetic Rate Constants
and Plug Concentration Proﬁles from
Simulated KCE Electropherogram Signals
J´ozsef Vass, Sergey N. Krylov∗
jvass@yorku.ca, skrylov@yorku.ca
Centre for Research on Biomolecular Interactions
Department of Chemistry, York University
Toronto, ON, M3J 1P3, Canada
April 27, 2017
Abstract
Kinetic rate constants fundamentally characterize the dynamics of the chemical inter-
action of macromolecules, and thus their study sets a major direction in experimental
biochemistry. The estimation of such constants is often challenging, partly due to the
noisiness of data, and partly due to the theoretical framework. We present novel and
qualitatively reasonable methods for the estimation of the rate constants of complex
formation and dissociation in Kinetic Capillary Electrophoresis (KCE). This also serves
our broader eﬀort to resolve the inverse problem of KCE, where these estimates pose as
initial starting points in the non-linear optimization space, along with the asymmetric
Gaussian parameters describing the injected plug concentration proﬁles, which we also
hereby estimate. We also compare our rate constant estimation method to an earlier
one, also devised by our research team.
MSC class: 92C45 (primary); 62H12, 92C40 (secondary).
Keywords: Parameter estimation, kinetic rate constants, plug concentration proﬁles,
biochemical interactions, convection–diﬀusion equations.
∗Corresponding author.
1
arXiv:1707.07851v2  [q-bio.QM]  2 Aug 2017


## Page 2


Contents
1
Introduction
3
2
Preliminaries
4
2.1
The Physical Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4
2.2
Estimation with the Area Method . . . . . . . . . . . . . . . . . . . . . . . .
6
2.3
The Deconvolution Operator . . . . . . . . . . . . . . . . . . . . . . . . . . .
7
3
Estimation Methods
8
3.1
Estimation of koﬀ. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8
3.2
Estimation of γ and kon
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9
4
Computational Results
10
4.1
Error Comparison between the Area and Our Method . . . . . . . . . . . . .
10
4.2
Error Analysis of the Initial Concentration Proﬁles
. . . . . . . . . . . . . .
10
5
Concluding Remarks
12
References
14
2


## Page 3


1
Introduction
The physical model of Kinetic Capillary Electrophoresis (KCE) was introduced by our lab
in articles [3, 16] and surveyed in [10]. The main purpose of the model is to enable the ex-
perimenter the reliable determination of the kinetic rate constants of complex formation and
dissociation, denoted kon and koﬀ. Under speciﬁc ﬁxed initial conditions, these two constants
induce parametrized signals, arising from the solution of a constant–convection–diﬀusion–
reaction equation (CCDR) [19]. The measured experimental signal poses a signiﬁcant re-
duction in information, as it is merely the superposition of two concentration components,
while the CCDR equation has actually three such components – i.e. one component is lost
entirely in the signal acquisition, while the other two are summed, as explained in the next
section.
Despite the complexity of this estimation task, hinted above, our team has introduced an
integration-based method, which has gone through several stages of improvement, and we
review the latest version in Section 2.2, along with the series of papers that led up to it. The
crux of the method is determining the three disjoint subintervals of the experimental time
interval, in which the signal acquisition occurs at the detector location. Two of these three
intervals correspond to a left- and right-peak of the superposed concentration functions,
mentioned earlier, while the third is the dissociation bridge. The area under the signal over
these three intervals imply the area-based estimates for kon and koﬀ.
Our new estimation method introduced in Section 3 also requires the above three intervals,
but the requirement of accurate integrability is replaced with a more robust linear least
squares regression, executed either directly on the signal data sample, or data derived via
deconvolution. The former is the case for our estimation of koﬀ, while the latter for that
of the asymmetric Gaussian plug parameters, which imply our estimate of kon. The exact
solutions of KCE for a simpliﬁed case, derived in [19], are utilized towards this estimate. The
accuracy of our rate constant estimates is compared to the area-based method in Section
4.1, while the plug parameter estimates are analyzed in Section 4.2.
To give a brief survey of the relevant literature, ﬁrstly we observe that various experimental
approaches have been taken to approximating the rate constants of complex formation and
dissociation, kon and koﬀ.
Methods by others are [20, 6, 2, 12, 1, 17], while the KCE-
based methods by our lab are surveyed in Section 2.2. Each method has its advantages and
limitations, while their applications also vary. For instance, Hornblower et al. [6] present
a nanopore amperometric approach, which requires the microscopic observation of a few
molecules, similarly to another approach via ﬂuorescence correlation spectroscopy [2, 12].
Other approaches, such as one via surface-immobilized binding sensors [1, 17], or our own via
KCE, are macroscopic since they require measuring changes in concentrations. KCE methods
[10] have their advantage in measuring rate and equilibrium constants with only a relatively
small amount of the required substances, which are often expensive, on the condition that
one of the reactants can be labeled ﬂuorescently, without aﬀecting the interaction.
3


## Page 4


2
Preliminaries
2.1
The Physical Model
Our previous article [19] describes how the KCE equations [10, 3, 16] originate in the Nernst–
Planck Equations, which model the combined eﬀects of convection, diﬀusion, and chemical
reaction between ions in some electric ﬁeld.
The concentration vector of three reactants c = (L, T, C) : R2
+ →R3
+ denoting the ligand,
target, and complex, is deﬁned over spacetime points (t, x) ∈[0, tmax] × [0, xdet], where the
measurement occurs at the detector xdet. The concentrations satisfy the equation
∂tc + v · ∂xc = D · ∂2
xc + R(c)
where v = (vL, vT, vC) ∈R3
+ and D = (DL, DT, DC) ∈R3
+ are the constant velocity and dif-
fusion vectors, and · denotes the Hadamard product. The reaction term takes the form
R(c) = (−konLT + koﬀC, −konLT + koﬀC, konLT −koﬀC) : R2
+ →R3
where k = (kon, koﬀ) ∈R2
+ are the rate constants of complex formation and dissociation
respectively. The equilibrium dissociation constant is deﬁned as Kd := koﬀ/kon.
This system of partial diﬀerential equations must be accompanied by appropriate initial and
boundary conditions to ensure the existence and uniqueness of solutions. This article deals
with only the NECEEM case, but the estimation methods to be introduced also work for
other KCE cases where there are two prominent peaks in the signal, such as ppKCE [19] or
MASKE [13].
The NECEEM initial conditions IC(x) = c(0, x) = ¯c · ϱ(x/l) represent the concentration
proﬁles of the injected plugs, where ¯c = (¯L, ¯T, ¯C) ∈R3
+ denotes the initial equilibrium
concentrations (note that Kd = ¯L ¯T/ ¯C), furthermore ϱ : R+ →R3 is a vector of asymmetric
Gaussian density functions, and l is the theoretical “length” of the injected plugs. The left
boundary condition vanishes c(t, 0) = 0, while the right one is also a vanishing Neumann
boundary condition ∂xc(t, xdet) = 0, for computational purposes. See our previous article for
further details [19].
The signal is measured at the detector as the superposition of the ligand and complex
concentrations
S(t) = S[k](t) = S[k, γ](t) := (L + C)(t, xdet)
where the signals may be considered to be parametrized by the rate constants k and the
asymmetric Gaussian plug parameters
γ = (µL, σ1
L, σ2
L, hL, µT, σ1
T, σ2
T, hT, µC, σ1
C, σ2
C, hC)
which denote the center, the left and right standard deviations, and the height of the injected
plugs (dependent on the initial equilibrium concentrations).
4


## Page 5


A particular simpliﬁcation of NECEEM is when R(c) = (koﬀC, koﬀC, −koﬀC) [14], for which
explicit solutions have been derived when the densities are symmetric Gaussians [19], but the
formulas shall prove to be useful nevertheless in deriving our estimates for the parameters k
and γ from a given signal. Denoting
F[k](t, x) := ϑ(t) e−kt ϱG[vt, 2Dt](x)
ϱG(x) := ϱG[µ, σ2](x) :=
1
σ
√
2π exp

−(x −µ)2
2σ2

,
ϑ(t) :=
(
1 if t ≥0
0 otherwise
and observing that for some µ0, σ0 > 0 and µ := µ0l, σ := σ0l, we have
IC(x) = ¯c ϱG[µ0, σ2
0](x/l) = ¯cl ϱG[µ, σ2](x)
then via the convolution property of Gaussians we get
C(t, x) = (ICC ∗FC[koﬀ](t, ·))(x) = l ¯C ϑ(t) e−koﬀt ϱG[µ + vCt, σ2 + 2DCt](x).
The L and C concentrations over spacetime are the superpositions of an equilibrium and
dissipation term
L(t, x) = (ICL ∗FL[0](t, ·))(x) + koﬀ(C ∗FL[0])(t, x) = l¯L ϱG[µ + vLt, σ2 + 2DLt](x) +
+ koﬀl ¯C
Z t
0
e−koﬀτϱG[µ + vLt + (vC −vL)τ, σ2 + 2DLt + 2(DC −DL)τ](x) dτ.
The formula for T is analogous.
5


## Page 6


2.2
Estimation with the Area Method
Figure 1: The areas deﬁned under the signal,
the three main ones being the C-peak, the dis-
sociation bridge D, and the L-peak.
The estimation of kinetic rate constants via
integration of the signal began in our lab
with the work of Berezovski and Krylov
[3, 11], which gave an estimate for the equi-
librium binding and dissociation constants
in NECEEM (Kb and Kd), deﬁned in terms
of the areas over certain subintervals of the
signal domain.
Okhonin et al.
[14] built
upon this work to derive an estimate for koﬀ,
through the simpliﬁcation of NECEEM, dis-
cussed in the previous section, but for rect-
angular plugs. This work was expanded to
ppKCE with an estimate for kon as well [15].
Cherney et al. gave estimates for both kon
and koﬀthrough a similar area method for
NECEEM [4] and the simpliﬁed KCE case
of MASKE [5]. See also [7, 8, 9].
Figure 1 is a self-explanatory depiction of the area quantities used in the formulas for calcu-
lating kon and koﬀ. The only question that remains is how to calculate ∆tL and ∆tC. If the
signal is quite noisy, the deﬁnitions may vary, but typically they run to 1% of the right end
of the L and the left end of the C peaks, respectively. Denoting the area operator as A, the
magenta and red areas – under the ends of the dissipation tails L∗, C∗– have been shown
to be approximately [4]
A(L∗) ≈2
3hL∆tL, A(C∗) ≈2
3hC∆tC.
Deﬁning the auxiliary constants
R1 :=
A(L) −A(L∗)
A(C) + A(D) + A(L∗),
R2 := A(C) + A(D) + A(L∗)
A(C) −A(C∗)
the dissociation constant can be approximated as
Kd ≈1000(Tini(1 + R1) −Lini)
1 +
1
R1
where Lini, Tini are the initial pre-equilibrium concentrations. The kinetic rate constants can
then be approximated as
koﬀ≈1
tC
ln(R2),
kon = koﬀ
Kd
.
6


## Page 7


2.3
The Deconvolution Operator
As we have seen earlier, the solutions of the simpliﬁed NECEEM system are expressed
in terms of the function convolution operator, so in order to approximate the Gaussian
parameters describing the initial concentration proﬁles, one may already suspect that some
sort of deconvolution must be performed. For the sake of clarity and eﬃciency of presentation,
we hereby introduce an operator for the linear least squares method performed on discrete
matrices sampled from theoretically exact functions.
We consider a bivariate F : R2 →R and two univariate functions g, h : R →R, the ﬁrst of
which is unknown, related by (F(t, ·)∗g)(x) = h(t, x). Denote the deconvolution operator as
g := Γ(F, h), if such a g indeed exists and it is unique. To resolve this in the discrete sense,
we sample these functions on a spacetime grid deﬁned by t0, . . . , tI and x0, . . . , xJ, in the
intervals It := [t0, tI], Ix := [x0, xJ]. Speciﬁcally, we are interested in deconvolution at xJ
(which typically corresponds to the detector location xdet). Thus at some ti, we have
h(ti, xJ) = ((F(ti), ·) ∗g)(xJ) =
Z xJ
0
F(ti, xJ −x)g(x) dx ≈
J
X
j=1
F(ti, xJ −xj)g(xj)∆x
where ∆x = xJ/J, implying a potentially over/under-determined system of linear equations,
which can be written in matrix form as


F(t0, xJ −x1)
. . .
F(t0, xJ −xJ)
...
...
...
F(tI, xJ −x1)
. . .
F(tI, xJ −xJ)

·


g(x1)
...
g(xJ)

= J
xJ
·


h(t0, xJ)
...
h(tI, xJ)

.
Clearly, exact equality may not be attainable, meaning no such vector of values (g(x1), . . . , g(xJ))
is likely to exist, though a least squares approximation does.
Denoting the matrices as
bF, bg, bh, the vector v ∈RJ that minimizes the error ∥bFv −bh∥2 in the Euclidean norm, is
given by
bΓ(F, h) = bΓIt,Ix(F, h) = bΓI,J(F, h) := ( bF T bF)−1 bF Tbh ≈bg.
Clearly, this explicitly-deﬁned discrete deconvolution operator approaches the continuous
one in the limit (in some appropriate operator metric), as the spacetime grid becomes
denser.
7


## Page 8


3
Estimation Methods
3.1
Estimation of koﬀ
As described earlier in Section 2.1, the signal S[k, γ] in the simpliﬁed NECEEM case is given
by the formula
S[k, γ](t) = L(t, xdet) + C(t, xdet) = Leq(t, xdet) + Ldis(t, xdet) + C(t, xdet) =
= l¯L ϱG[µ + vLt, σ2 + 2DLt](x) +
+ koﬀl ¯C
Z t
0
e−koﬀτϱG[µ + vLt + (vC −vL)τ, σ2 + 2DLt + 2(DC −DL)τ](x) dτ +
+ l ¯C ϑ(t) e−koﬀt ϱG[µ + vCt, σ2 + 2DCt](x).
The third term in the sum is C(t, xdet), which is dominated by the Gaussian factor only near
the C-peak, while along the dissociation bridge the exponential factor e−koﬀt dominates.
Therefore heuristically C(t, xdet) ≈λe−koﬀt, with some λ > 0 along the dissociation bridge.
The second term Ldis(t, xdet) can actually be expressed similarly, since
d
dtLdis(t, xdet) = koﬀC(t, x) ≈koﬀλe−koﬀt
implying on the dissociation bridge that Ldis(t, xdet) ≈−λe−koﬀt. Lastly, the ﬁrst term in the
above superposition is the L-peak, which is roughly constant along the bridge. Thus we can
conclude that the signal along the bridge decays approximately exponentially, with a rate of
koﬀ.
This implies the following method for approximating koﬀ. Take a subinterval of the bridge
which does follow an exponential (such as by taking the natural logarithm of the signal, and
ﬁnding an interval where its second derivative is near-zero). Then take the logarithm of the
signal on that subinterval, and perform a linear least squares approximation. The resulting
slope is our approximation of koﬀ.
8


## Page 9


3.2
Estimation of γ and kon
Assuming that the initial concentration proﬁles of the injected plugs are asymmetric Gaussian
density functions, with the vector of parameters
γ = (µL, σ1
L, σ2
L, hL, µT, σ1
T, σ2
T, hT, µC, σ1
C, σ2
C, hC)
from Section 2.1, the three proﬁles are entirely determined by these twelve parameters. In
order to approximate them, however, a deconvolution must be performed on ideal portions
of the signal.
Our ﬁrst aim is to identify subintervals of the signal support, where the deconvolutions may
be ideally performed. One may observe heuristically, that the bottom one third of the left-
half of the C-peak values arise solely from the values of C, unaﬀected by L. Denote this
interval IC. Similarly, the bottom one third of the right half of the L-peak values arise solely
from the equilibrium values of L, unaﬀected by C or the dissipation values of L. Denote this
interval IL. Also denote Ix := [0, xdet]. The following hold over these intervals
L(t, xdet) ≈(FL[0](t, ·) ∗ICL)(xdet),
C(t, xdet) = (FC[koﬀ](t, ·) ∗ICC)(xdet)
deﬁned earlier as
FL[0](t, x) = ϱG[vLt, 2DLt](x),
FC[koﬀ](t, x) = e−koﬀtϱG[vCt, 2DCt](x).
In order to perform the deconvolutions according to Section 2.3, we ﬁrst discretize the space-
time intervals IL × Ix, IC × Ix. Then approximations to the initial concentration proﬁles are
given by the discrete deconvolutions
c
ICL = bΓIL,Ix(FL[0], L(·, xdet)),
c
ICC = bΓIC,Ix(FL[koﬀ], C(·, xdet)).
The corresponding parameters in γ can be deduced from these two proﬁles, as follows. The
centers and standard deviations, are the peak locations and the inﬂection points of the asym-
metric Gaussian initial condition proﬁles c
ICL and c
ICC. Furthermore, the initial equilibrium
concentrations can be calculated from the initial condition heights as follows
¯L = hL
√
2π σ1
L + σ2
L
2
,
¯C = hC
√
2π σ1
C + σ2
C
2
,
¯T = 10002Tinil −¯C.
The center and standard deviations of the T initial condition (injected plug concentration
proﬁle) are approximated as
cT ≈cL + cC
2
,
σ1
T ≈σ1
L + σ1
C
2
,
σ2
T ≈σ2
L + σ2
C
2
.
Lastly, according to Section 2.1, the kinetic rate constant of complex formation can be
estimated via the exact relationship kon = koﬀ¯C/(¯L ¯T). Thus the error in estimating the
concentration components of ¯c accumulates in this kon estimate, as analyzed in the next
section.
9


## Page 10


4
Computational Results
4.1
Error Comparison between the Area and Our Method
We performed a computational comparison on Figure 2 between the area method (Section
2.2) and our method (Section 3), over a set of kinetic rate constants with constant Kd and
varying kon, in a neighborhood of three orders of magnitude, with 1000 uniformly distributed
random sample points, centered at
kon = 500 m3/mol, koﬀ= 0.001, v = (0.22, 3.33, 0.48)×10−3 m2/Vs, D = (7, 7, 7)×10−11 m2/s
¯c = (2.1, 18.1, 1.9) × 10−7 mol/m3, l = 0.01 m, tmax = 1200 s, xdet = 0.2 m.
Figure 2 is plotted on a logarithmic scale in the independent variable kon, with the center
of the sample interval being log10(500) = 2.6990. Kd is kept constant at a value of 2 ×
10−6 mol/m3. The relative error is calculated as the ratio of the absolute distance between
the original and the estimated value, and the original value. See our software [18].
Upon plotting the relative errors, it is perhaps most important to observe that all four
estimation methods are near-exact for particular kon values – meaning, the relative error
nearly vanishes – which conﬁrms the reliability of the methods in this sense. The ﬁrst local
minimum in the log-scale sample, for our kon estimation method, occurs at 2.7656 with a
relative error of 0.03%, for our koﬀmethod at 5.0034 with 0.20%, for the area kon method at
3.3975 with 0.08%, and for the area koﬀmethod at 4.0210 with 0.23%. Interestingly, beyond
these critical values, the errors for all four methods become unpredictable, making them all
unreliable for higher kon values.
Thus based on Figure 2, we conjecture that both our kon and koﬀestimates are reliable up
to certain kon values, the estimation of which we leave as an open problem.
4.2
Error Analysis of the Initial Concentration Proﬁles
To get an idea of the relative errors incurred by the estimation of the γ parameter vector,
characterizing the asymmetric Gaussian plug concentration proﬁles, we perform the estima-
tion of this vector using exact (non-estimated) kon and koﬀvalues, on the same logarithmic
interval as before, while keeping the original γ coordinates constant at the above values.
The resulting Figure 3 shows the remarkable constancy of the relative errors between the
original and the estimated γ values up to certain critical values (interestingly, hL is not
quite constant). These critical values occur in our sample for the L- and T-plug parameters
µL, σ1
L, σ2
L, hL, µT, σ1
T, σ2
T, hT at the log10(kon) value of 2.8618, while the C-plug errors for µC
and σ2
C remain constant a bit longer, and those for σ1
C and hC are oﬀthe chart or erratic.
This behavior is partly due to the nature of the estimation method presented in Section 3.2,
and partly to our MATLAB implementation [18]. Note that the error that accumulates in γ
towards estimating kon remains reasonable, according to the previous section.
10


## Page 11


Figure 2: Kinetic parameter estimation errors with the area and our method.
Figure 3: Plug concentration parameter estimation errors.
11


## Page 12


5
Concluding Remarks
We have introduced some estimation methods, based on linear regression, for kinetic con-
stants of macromolecules, as well as for the parameters of the initial concentration proﬁles
of the injected plugs, within the experimental framework of Kinetic Capillary Electrophore-
sis. As demonstrated through computational testing, our rate constant estimation proved to
be more reliable, up to some conjectured upper bound, than our former integration-based
method. Our initial concentration proﬁle parameter estimation method may curiously like-
wise be conjectured to be reliable up to some upper bound.
The proof of these conjectures could be a matter of future eﬀort, however, it may not be
particularly worthwhile, considering that the utility of the rate constant and concentration
parameter estimates is merely in their role as an initial starting point for our computational
resolution of the KCE inverse problem [18], to be detailed in our upcoming papers. While
a reliable starting point is preferable for the inversion – i.e. one “typically close enough” to
the sought solution – it is not imperative. Nevertheless, an estimation method that is known
to be “robust” according to suﬃcient testing, can serve as a check on whether the inversion
diverges – i.e. the optimization algorithm performing the minimization of the error function,
deﬁned between the target and the simulated signals.
12


## Page 13


References
[1] Y. Abdiche, D. Malashock, A. Pinkerton, and J. Pons. Determining kinetics and aﬃni-
ties of protein interactions using a parallel real-time label-free biosensor, the octet.
Analytical biochemistry, 377(2):209–217, 2008.
[2] W. Al-Souﬁ, B. Reija, M. Novo, S. Felekyan, R. K¨uhnemuth, and C. A. Seidel. Fluores-
cence correlation spectroscopy, a tool to investigate supramolecular dynamics: inclusion
complexes of pyronines with cyclodextrin. Journal of the American Chemical Society,
127(24):8775–8784, 2005.
[3] M. Berezovski and S. N. Krylov. Nonequilibrium capillary electrophoresis of equilibrium
mixtures – a single experiment reveals equilibrium and kinetic parameters of protein-
DNA interactions. Journal of the American Chemical Society, 124(46):13674–13675,
2002.
[4] L. T. Cherney, M. Kanoatov, and S. N. Krylov. Method for determination of peak
areas in nonequilibrium capillary electrophoresis of equilibrium mixtures. Analytical
chemistry, 83(22):8617–8622, 2011.
[5] L. T. Cherney and S. N. Krylov.
Slow-equilibration approximation in macroscopic
approach to studying kinetics at equilibrium. Analytical chemistry, 83(4):1381–1387,
2011.
[6] B. Hornblower, A. Coombs, R. D. Whitaker, A. Kolomeisky, S. J. Picone, A. Meller,
and M. Akeson. Single-molecule analysis of DNA-protein complexes using nanopores.
Nature Methods, 4(4):315–317, 2007.
[7] M. Kanoatov, L. T. Cherney, and S. N. Krylov. Extracting kinetics from aﬃnity cap-
illary electrophoresis (ACE) data: A new blade for the old tool. Analytical chemistry,
86(2):1298–1305, 2014.
[8] M. Kanoatov, V. A. Galievsky, S. M. Krylova, L. T. Cherney, H. K. Jankowski, and
S. N. Krylov. Using nonequilibrium capillary electrophoresis of equilibrium mixtures
(NECEEM) for simultaneous determination of concentration and equilibrium constant.
Analytical chemistry, 87(5):3099–3106, 2015.
[9] M. Kanoatov, S. Mehrabanfar, and S. N. Krylov. Systematic approach to optimization
of experimental conditions in nonequilibrium capillary electrophoresis of equilibrium
mixtures. Analytical Chemistry, 88(18):9300–9308, 2016.
[10] S. N. Krylov. Kinetic CE: Foundation for homogeneous kinetic aﬃnity methods. Elec-
trophoresis, 28(1-2):69–88, 2007.
[11] S. N. Krylov and M. Berezovski. Non-equilibrium capillary electrophoresis of equilibrium
mixtures – appreciation of kinetics in capillary electrophoresis. Analyst, 128(6):571–575,
2003.
13


## Page 14


[12] Y. Li, G. J. Augustine, and K. Weninger. Kinetics of complexin binding to the SNARE
complex: correcting single molecule FRET measurements for hidden events. Biophysical
journal, 93(6):2178–2187, 2007.
[13] V. Okhonin, M. V. Berezovski, and S. N. Krylov.
MASKE: Macroscopic approach
to studying kinetics at equilibrium.
Journal of the American Chemical Society,
132(20):7062–7068, 2010.
[14] V. Okhonin, S. M. Krylova, and S. N. Krylov. Nonequilibrium capillary electrophoresis
of equilibrium mixtures, mathematical model. Analytical Chemistry, 76(5):1507–1512,
2004.
[15] V. Okhonin, A. P. Petrov, M. Berezovski, and S. N. Krylov. Plug–plug kinetic capillary
electrophoresis: Method for direct determination of rate constants of complex formation
and dissociation. Analytical chemistry, 78(14):4803–4810, 2006.
[16] A. Petrov, V. Okhonin, M. Berezovski, and S. N. Krylov. Kinetic capillary electrophore-
sis (KCE): a conceptual platform for kinetic homogeneous aﬃnity methods. Journal of
the American Chemical Society, 127(48):17104–17110, 2005.
[17] R. L. Rich and D. G. Myszka. Higher-throughput, label-free, real-time molecular inter-
action analysis. Analytical biochemistry, 361(1):1–6, 2007.
[18] J. Vass. KCE Solvers Package – Direct and Inverse Solver. GitHub/jzsfvss/KCESolvers,
2017.
[19] J. Vass and S. N. Krylov.
A fast stable discretization of the constant–convection–
diﬀusion–reaction equations of kinetic capillary electrophoresis (KCE).
Submitted,
arXiv/1611.05795, 2016.
[20] W. D. Wilson.
Analyzing biomolecular interactions.
Science, 295(5562):2103–2105,
2002.
14

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1707_07851v2_estimating_kinetic_rate_constants_and_plug_concentration_profiles_from_simulated
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2017/1707_07851V2_ESTIMATING_KINETIC_RATE_CONSTANTS_AND_PLUG_CONCENTRATION_PROFILES_FROM_SIMULATED.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

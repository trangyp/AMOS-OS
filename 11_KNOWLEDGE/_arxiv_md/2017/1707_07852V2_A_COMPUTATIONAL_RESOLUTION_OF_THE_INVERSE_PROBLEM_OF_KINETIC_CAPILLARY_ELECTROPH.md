---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1707.07852v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1707.07852v2_A_Computational_Resolution_of_the_Inverse_Problem_of_Kinetic_Capillary_Electroph

> Source: 1707.07852v2_A_Computational_Resolution_of_the_Inverse_Problem_of_Kinetic_Capillary_Electroph.pdf

> Pages: 10

---


## Page 1


A Computational Resolution of the Inverse
Problem of Kinetic Capillary Electrophoresis
(KCE)
J´ozsef Vass and Sergey N. Krylov
Abstract Determining kinetic rate constants is a highly relevant problem in bio-
chemistry, so various methods have been designed to extract them from experimen-
tal data. Such methods have two main components: the experimental apparatus and
the subsequent analysis, the latter often dependent on mathematical theory. Thus the
theoretical approach taken inﬂuences the effectiveness of constant determination. A
computational inverse problem approach is hereby presented, which does not merely
give a single rough approximation of the sought constants, but is inherently capable
of determining them from exact signals to arbitrary accuracy. This approach is thus
not merely novel, but opens a whole new category of solution approaches in the
ﬁeld, enabled primarily by an efﬁcient direct solver.
1 Introduction
1.1 Aims and Overview
The direct problem of efﬁciently generating accurate numerical solutions to the set
of partial differential equations of Kinetic Capillary Electrophoresis (KCE) [6], has
been resolved earlier via a multimesh algorithm [12], which fully overcomes the
typical instability arising from the interaction of the diffusion and convection terms.
J´ozsef Vass
Centre for Research on Biomolecular Interactions, Department of Chemistry, York University,
Toronto, ON, M3J 1P3, Canada, e-mail: jvass@yorku.ca
Sergey N. Krylov
Centre for Research on Biomolecular Interactions, Department of Chemistry, York University,
Toronto, ON, M3J 1P3, Canada, e-mail: skrylov@yorku.ca
1
arXiv:1707.07852v2  [q-bio.QM]  2 Aug 2017


## Page 2


2
J. Vass and S.N. Krylov
This potent solution to the direct problem allows the effective resolution of the in-
verse problem on a reasonable timescale, as we shall hereby discuss and demon-
strate. The inversion essentially entails the optimization of a non-linear error ob-
jective function, computed between the experimental target signal and the signals
generated numerically at each iteration. Estimating the starting point for the opti-
mization, posed a challenge in itself [13]. Furthermore, control of the error in the
sought parameters is demonstrated, enabling the resolution of this inverse problem
to arbitrary accuracy for exact target signals. This work has also been implemented
as a software package [11].
The KCE system of equations includes kinetic rate constants in the reaction term,
which can be viewed as parameters that the solution functions of this system of
partial differential equations depend on. The aim of the inverse problem is to ﬁnd
or approximate certain parameters – the rate constants of complex formation and
dissociation – that induce an a priori given exact solution. If such a method can
arbitrarily approximate an exact solution, then it can be applied to experimental
data reliably. Therefore, the goal becomes to minimize an error function between
the given solution and the approximating solutions, which must be generated for
each set of test parameters as the optimization progresses. The generation of such
parametric solutions is essentially akin to a function evaluation in an optimization
iteration step, which must clearly be both efﬁcient and accurate.
Various experimental approaches have been taken in the literature to approximating
rate constants, though not to arbitrary accuracy, which differentiates our method in
its novelty. Existing methods include [16, 5, 2, 7, 1, 10], while KCE-based methods
are surveyed in the previous article [13].
1.2 The Physical Model
We adopt the physical model and the notations covered in earlier articles [12, 13],
originally introduced in [6, 3, 9].
The concentration vector of reactants c = (L, T, C) : R2
+ →R3
+ is a mapping deﬁned
over spacetime points (t, x) ∈[0, tmax]×[0, xdet]. It satisﬁes the equation
∂tc+v·∂xc = D·∂2
x c+R(c)
where v = (vL, vT, vC) ∈R3
+ and D = (DL, DT, DC) ∈R3
+, and · denotes the
Hadamard product. The reaction term takes the form
R(c) = (−konLT +koffC, −konLT +koffC, konLT −koffC) : R2
+ →R3
where k = (kon, koff) ∈R2
+. Lastly, deﬁne Kd := koff/kon.


## Page 3


A Computational Resolution of the Inverse Problem of KCE
3
Since as it will become apparent in Section 2, the scope of this paper is con-
strained by the parameter estimation methods introduced earlier [13], we only con-
sider the NECEEM initial and boundary conditions for the above partial differential
equations. The initial conditions are given by IC(x) = c(0, x) = ¯c · ρ(x/l), where
¯c = (¯L, ¯T, ¯C) ∈R3
+ (note: Kd = ¯L ¯T/ ¯C) and ρ : R+ →R3
+ is a vector of asymmetric
Gaussian density functions, and l > 0. The left boundary condition is c(t, 0) = 0,
while the right one is ∂xc(t, xdet) = 0, for computational purposes.
The signal is deﬁned as the function
S[k, γ](t) := (L+C)(t, xdet), t ∈[0, tmax]
parametrized by the above k and the asymmetric Gaussian plug parameters
γ = (µL, σ1
L, σ2
L, hL, µT, σ1
T, σ2
T, hT, µC, σ1
C, σ2
C, hC)
which denote the center, the left and right standard deviations, and the height of the
Gaussian initial conditions (dependent on ¯c).
See our previous articles for further details [13, 12, 6], such as the physical meaning
of the above constants.
2 The Inverse Problem of KCE
2.1 Problem Statement
The direct problem of generating a solution to the KCE equations, introduced above,
can be inverted to inquire what parameters (k∗, γ∗) ∈R14
+ induced a given signal
S∗: [0, tmax] →R+, meaning S∗= S[k∗, γ∗] by the earlier notations, which we refer
to as the “target signal”. Since as we shall see in the next section, the values of k∗and
γ∗are not independent, we will only need to invert over some of these parameters,
denoted by ω ∈R10
+ , while updating the deﬁnition of the signal mapping S[ω] to
eliminate the redundant parameters.
Deﬁne the error function as E(ω) := D(S∗, S[ω]) (ω ∈R10
+ ) where D is any met-
ric, typically the Euclidean. This E is the target function to be minimized during
inversion, below some required threshold ε > 0. The problem is thus the follow-
ing.
Problem 2.1 (KCE Inverse Problem) Given a threshold ε > 0 and an S∗: [0, tmax] →
R+ function, induced by unknown KCE parameters ω∗and deﬁned as S∗:= S[ω∗],
ﬁnd an ω parameter vector such that E(ω) < ε.


## Page 4


4
J. Vass and S.N. Krylov
This inverse problem may appear at ﬁrst to be ill-posed, meaning its solution is not
necessarily unique, and E(ω) = 0 doesn’t trivially imply that ω = ω∗. The signal
mapping S is not only a superposition, but also a slice of a surface, resulting in
a signiﬁcant loss of information relative to the full solution vector c = (L, T, C).
However, our computational experiments strongly suggest well-posedness, making
it a worthwhile conjecture, equivalent to asserting that the error function possesses
a unique minimum.
2.2 The Optimization Space
In this section, we clarify how the optimization space over ω ∈R10
+ reduces from
the seemingly straightforward variables (k, γ) ∈R14
+ . As mentioned, this reduction
is partly necessitated by the interdependencies between the coordinates of the latter
vector, which originate in the physicochemical model of KCE [6].
Another reason for the reduction, is that the variation in the T-plug parameters in
γ does not really affect the simulated signal. The standard deviations are not par-
ticularly relevant for the effectiveness of the computational inversion. The quantity
of the T substance in this chemical reaction can be controlled solely via the height
of the T-plug, while the plug center may be allowed to vary within 1 −2 orders
of magnitude. Though the height is in fact dependent on some other parameters, as
stated below.
Furthermore, it must be noted that kon typically has little bearing on the NECEEM
signal, as reasoned in earlier papers [13, 8], so the optimization process may place
a greater emphasis on optimizing in koff.
The full vector of parameters
(k, γ) = (kon, koff, µL, σ1
L, σ2
L, hL, µT, σ1
T, σ2
T, hT, µC, σ1
C, σ2
C, hC)
is reduced to the vector of optimization parameters
ω = (koff, µL, σ1
L, σ2
L, hL, µT, µC, σ1
C, σ2
C, hC).
To make up for the missing coordinates kon, σ1
T, σ2
T, hT, which are still necessary to
generate signals S[ω] for the calculation of the error E, some relationships between
the coordinates must be observed. Firstly
¯L =
√
2π hL
l
σ1
L +σ2
L
2
and similarly for ¯C, while ¯T = 1000Tini −¯C where Tini is the initial pre-equilibrium
concentration of the T-plug. Its height can then be calculated as


## Page 5


A Computational Resolution of the Inverse Problem of KCE
5
hT =
l ¯T
√
2π
 ˆσ1
T + ˆσ2
T
2
where ˆσ1,2
T
are the standard deviation estimates for the asymmetric Gaussian T-
plug [13]. Using mere estimates does not signiﬁcantly affect the effectiveness of
inversion, as reasoned heuristically above, i.e. the minimization of the error function
E below a given threshold. Lastly, kon = koff ¯C/(¯L ¯T) which is simply the relationship
mentioned in Section 1.2.
Lastly, we remark that the inversion using any optimization algorithm we tested,
proved to be signiﬁcantly more efﬁcient when carried out in logarithmic space, in
all independent variables.
2.3 Error Control
As stated in the KCE Inverse Problem 2.1, the inversion is formulated as the min-
imization of the error function ω →E(ω) below some threshold ε > 0, where the
signal error is calculated as E(ω) = D(S∗, S[ω]), typically with the Euclidean met-
ric D and some target signal S∗= S[ω∗].
It remains unclear, how this minimization can be made practical. For the purpose
of scientiﬁc applications, our inevitable aim must be to ensure that the error in the
k = (kon, koff) parameter is minimized below a threshold δ > 0, prescribed a priori.
Therefore, the task becomes to determine – or estimate – what ε threshold above is
necessary to ensure this δ.
The matter can be resolved under the rather weak hypothesis that there is a local
Lipschitz constant L satisfying
d(k∗, k) ≤d(ω∗, ω) ≤L·D(S[ω∗], S[ω]) = L·E(ω)
in a neighborhood of the point ω∗in the optimization space. Since this point is
unknown, computationally we ensure a large enough neighborhood in logarithmic
space around our estimate – derived earlier [13] – likely to contain the sought ω∗.
Typically, the neighborhood is taken within two orders of magnitude, which proved
to be sufﬁcient according to our computational experiments.
The Lipschitz constant L can then be estimated within this neighborhood, by tak-
ing random pairs of points ω1, ω2 in it, and taking the maximum of the ratios
d(ω1, ω2)/D(S[ω1], S[ω2]).
Using this estimated L, the threshold in the signal error E(ω) must be taken to be
δ := ε/L, in order to ensure that the error in k falls below the prescribed signal
threshold ε > 0.


## Page 6


6
J. Vass and S.N. Krylov
2.4 Implementation
The inverse solver [11] is essentially a non-linear optimization process, which min-
imizes the error function introduced in Section 2.1. At each evaluation of this func-
tion, the direct solver must be called to generate a signal S[ω] for the current it-
eration of parameters ω. Thus the runtime of the inverse solver is fundamentally
implied by that of the direct solver. The stability and efﬁciency of the direct solver
was established in our earlier article [12].
Finding a well-functioning – or perhaps even “ideal” – optimization algorithm, was
in itself a challenge, and we have tested several. The fmincon MATLAB function
with the interior-point algorithm proved to be the most robust and efﬁcient. The
bfgs Hessian approximation option (a dense quasi-Newton approximation [14]) is
typically sufﬁcient, but occasionally the lbfgs option (a limited-memory, large-scale
quasi-Newton approximation [15]) must also be run, in case the bfgs option fails to
converge below the required signal error threshold within the allocated time. Other
tested algorithms include Cuckoo Search [18], Flower Pollination [17], and Har-
mony Search [4], each of which proved to be less robust than fmincon, but are
nevertheless available in our package [11].
Each inverter – i.e. error minimization subroutine, with a particular optimization
algorithm – was tested for simulated signals induced by known parameters, and
then compared to the output parameters in terms of relative error (see Figures 1 and
3). In practice, the inverters are executed on experimental signals (from unknown
parameters), in which case, the accuracy of the result can be gauged via the error
control method described in Section 2.3, and demonstrated in Section 3.
3 Performance Analysis
Figure 1 depicts the performance analysis of the primary inverter, running the BFGS
and L-BFGS [14, 15] interior point optimization algorithms of MATLAB (fmincon
with the interior-point algorithm, and Hessian approximation methods bfgs and
lbfgs). The target threshold of 0.0001% in the signal error tends to ensure two correct
decimal places in k in scientiﬁc notation. This threshold is reached by the inverter up
to log10(kon) ≈3.45 on the horizontal axis, but it fails to converge above that value.
The ca. 4200 evaluations is the default upper iteration bound that each optimization
algorithm is allowed to run, at this t-mesh size. The ca. 5000 evaluations at ca. 2.75
results from running the inverter twice, trying both settings (bfgs and lbfgs).
Figure 2 accompanies Figure 1, for reference. Apparently for log10(kon) > 3.45 the
C-peak vanishes, visually elucidating the divergence of the inverter. The necessity of
a prominent C-peak thus becomes a practical rule of thumb for the reliable inversion
of experimental signals.


## Page 7


A Computational Resolution of the Inverse Problem of KCE
7
Figure 3 is a log-log graph (with decreasing horizontal axis), which demonstrates
a deﬁnite power law relationship on average, with an exponent of ca. 0.7 between
the optimization threshold in the signal relative error and the relative error between
the original kon value and the one determined by the inverter. The error in koff tends
to be close to the same value, or less, so it is not plotted. For lower kon values, the
relative error in k apparently stagnates for higher threshold errors in the signal, but
does begin to decrease later. The demonstrated power law may be different for other
experimental parameter sets.
Interestingly, the fmincon optimization subroutine also exhibits a power law rela-
tionship between its runtime and the error threshold in the signal, with a negligible
exponent of ca. −0.07, not considering the outlier. In the outlier log10(kon) ≈2.95
case, the parameters appear to conspire so that only the lbfgs option is able to tackle
the inversion (the plotted runtimes include the failed attempts with the bfgs option).
Nevertheless, the overall linear relationship ensures that the runtime remains pre-
dictable for various thresholds.
Based on Figure 4, we can conclude that for all the log10(kon) ≤2.7 test cases,
and for all tested mesh sizes, the interior point inverter was successful. The case
runtimes, however, did not follow a clear relationship with the increasing mesh size.
Taking the average among all cases (in black), however, does exhibit a somewhat
clear trend.
Fig. 1 Variation of the relative error in k with respect to increasing log10(kon) values, at constant
Kd = 2×10−6 mol/m3. The t-mesh size is 300, and the error threshold is ε = 0.0001%.


## Page 8


8
J. Vass and S.N. Krylov
Fig. 2 Simulated electropherogram signals for increasing log10(kon), at a t-mesh size of 300.
Fig. 3 Illustration of the correlation between the decrease in the optimization threshold in the
signal relative error and the decrease in the kon relative error, for various log10(kon) cases (labeled
in the legend). The corresponding runtimes are also plotted. Only the log10(kon) ≤3.45 cases are
plotted, where convergence of the inverter was ensured (see Figure 1).


## Page 9


A Computational Resolution of the Inverse Problem of KCE
9
Fig. 4 Illustration of the variation of runtime with increasing temporal mesh size (to which the
spatial is proportional). Only the log10(kon) ≤2.7 cases are plotted, where convergence of the
inverter was ensured within a reasonable timeframe for a temporal mesh size of 300 (see Figure 1).
4 Concluding Remarks
This article aimed to resolve the inverse problem of Kinetic Capillary Electrophore-
sis, involving a set of partial differential equations, parameterized in the initial and
boundary conditions, as well as the equations themselves. The problem was refor-
mulated as the non-linear minimization of a certain error function, each evaluation
of which required the generation of a solution with the direct solver.
The main challenge thus became to identify an optimization algorithm capable of
carrying out this minimization to arbitrary accuracy, robustly and efﬁciently, which
was accomplished. Furthermore, a local Lipschitz condition was utilized to relate
the error in the signal to the error in the sought parameters, in order to control
the accuracy in the latter. This is a deﬁnite novelty relative to earlier work on this
topic.
While this article focused on the design of a computational method and its practical
robust implementation, the implied theoretical questions nevertheless project av-
enues for future research. The most relevant problems being: (1) uniqueness of the
global minimizer of the error function; (2) continuous differentiability of the error


## Page 10


10
J. Vass and S.N. Krylov
function. There is strong consistent computational evidence of a unique minimizer,
according to our experiments. The second property would imply local Lipschitz
continuity (hypothesized in Section 2.3), and validate the use of gradient-based op-
timization algorithms.
This work was supported by the Natural Sciences and Engineering Research Council
of Canada (grant: CRDPJ 485321-15).
References
1. Y. Abdiche, D. Malashock, A. Pinkerton, and J. Pons. Determining kinetics and afﬁnities
of protein interactions using a parallel real-time label-free biosensor, the octet. Analytical
biochemistry, 377(2):209–217, 2008.
2. W. Al-Souﬁ, B. Reija, M. Novo, S. Felekyan, R. K¨uhnemuth, and C. A. Seidel. Fluorescence
correlation spectroscopy, a tool to investigate supramolecular dynamics: inclusion complexes
of pyronines with cyclodextrin. Journal of the American Chemical Society, 127(24):8775–
8784, 2005.
3. M. Berezovski and S. N. Krylov. Nonequilibrium capillary electrophoresis of equilibrium
mixtures – a single experiment reveals equilibrium and kinetic parameters of protein-DNA
interactions. Journal of the American Chemical Society, 124(46):13674–13675, 2002.
4. Z. W. Geem, J. H. Kim, and G. Loganathan. A new heuristic optimization algorithm: harmony
search. simulation, 76(2):60–68, 2001.
5. B. Hornblower, A. Coombs, R. D. Whitaker, A. Kolomeisky, S. J. Picone, A. Meller, and
M. Akeson. Single-molecule analysis of DNA-protein complexes using nanopores. Nature
Methods, 4(4):315–317, 2007.
6. S. N. Krylov.
Kinetic CE: Foundation for homogeneous kinetic afﬁnity methods.
Elec-
trophoresis, 28(1-2):69–88, 2007.
7. Y. Li, G. J. Augustine, and K. Weninger. Kinetics of complexin binding to the SNARE com-
plex: correcting single molecule FRET measurements for hidden events. Biophysical journal,
93(6):2178–2187, 2007.
8. V. Okhonin, S. M. Krylova, and S. N. Krylov. Nonequilibrium capillary electrophoresis of
equilibrium mixtures, mathematical model. Analytical Chemistry, 76(5):1507–1512, 2004.
9. A. Petrov, V. Okhonin, M. Berezovski, and S. N. Krylov.
Kinetic capillary electrophore-
sis (KCE): a conceptual platform for kinetic homogeneous afﬁnity methods. Journal of the
American Chemical Society, 127(48):17104–17110, 2005.
10. R. L. Rich and D. G. Myszka. Higher-throughput, label-free, real-time molecular interaction
analysis. Analytical biochemistry, 361(1):1–6, 2007.
11. J. Vass. KCE Solvers Package – Direct and Inverse Solver. GitHub/jzsfvss/KCESolvers, 2017.
12. J. Vass and S. N. Krylov. A fast stable discretization of the constant–convection–diffusion–
reaction equations of kinetic capillary electrophoresis (KCE). Submitted, arXiv/1611.05795,
2016.
13. J. Vass and S. N. Krylov. Estimating kinetic rate constants and plug concentration proﬁles
from simulated KCE electropherogram signals. To be submitted, arXiv/1707.07851, 2017.
14. Wikipedia. Broyden–Fletcher–Goldfarb–Shanno algorithm. Link, accessed 06-27-2017.
15. Wikipedia. Limited-memory BFGS. Link, accessed 06-27-2017.
16. W. D. Wilson. Analyzing biomolecular interactions. Science, 295(5562):2103–2105, 2002.
17. X.-S. Yang. Flower pollination algorithm for global optimization. In International Conference
on Unconventional Computing and Natural Computation, pages 240–249. Springer, 2012.
18. X.-S. Yang and S. Deb. Cuckoo search via L´evy ﬂights. In 2009 World Congress on Nature
& Biologically Inspired Computing (NaBIC), pages 210–214. IEEE, 2009.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1304.1357v1
source: arxiv
tags: [arxiv, knowledge, math, quantum, reference]
---
# 1304.1357v1_Trap-free_manipulation_in_the_Landau-Zener_system

> Source: 1304.1357v1_Trap-free_manipulation_in_the_Landau-Zener_system.pdf

> Pages: 6

---


## Page 1


Trap-free manipulation in the Landau-Zener system
Alexander Pechen1, 2, ∗and Nikolay Il’in2
1Department of Chemical Physics, Weizmann Institute of Science, Rehovot 76100, Israel
2Steklov Mathematical Institute of Russian Academy of Sciences, Gubkina 8, Moscow 119991, Russia
(Dated: November 12, 2018)
The analysis of traps, i.e., locally but not globally optimal controls, for quantum control systems
has attracted a great interest in recent years. The central problem that has been remained open is to
demonstrate for a given system either existence or absence of traps. We prove the absence of traps
and hence completely solve this problem for the important tasks of unconstrained manipulation of
the transition probability and unitary gate generation in the Landau-Zener system—a system with
a wide range of applications across physics, chemistry and biochemistry. This ﬁnding provides the
ﬁrst example of a controlled quantum system which is completely free of traps. We also discuss the
impact of laboratory constraints due to decoherence, noise in the control pulse, and restrictions on
the available controls which when being suﬃciently severe can produce traps.
PACS numbers: 02.30.Yy, 32.80.Qk
Keywords: Quantum control landscapes, Landau-Zener system
I.
INTRODUCTION
Manipulation by atomic and molecular systems is an
important branch of modern science with applications
ranging from optimal laser driven population transfer in
atomic systems out to laser assisted control of chemical
reactions [1]. High interest is directed towards control
of the Landau-Zener (LZ) system—a two-state quantum
system whose unitary evolution under the action of the
control ε(t) (e.g., shaped laser ﬁeld) is governed by the
equation
˙U ε
t = −i(∆σx + ε(t)σz)U ε
t ,
U ε
t=0 = I
(1)
where ∆> 0, σx and σz are the Pauli matrices. The
case ε(t) = εt with constant ε was studied by Landau,
Zener, St¨uckelberg, and Majorana [2]. This system has
been widely applied in physics, chemistry, and biochem-
istry, e.g., for describing transfer of charge along with its
energy [3], photosynthesis [4], atomic and molecular colli-
sions, processes in plasma physics [5], Bose-Einstein con-
densate [7], experimental realizations of qubits, etc. [6, 8–
13].
Controlled manipulation by a quantum system can be
formulated as ﬁnding global maxima of a suitable objec-
tive J(ε) associated to the system. For example, maxi-
mizing the probability of transition from the initial state
|i⟩to a target ﬁnal state |f⟩at a ﬁnal time T can be
described by maximizing J(ε) = Pi→f = |⟨f|U ε
T |i⟩|2. A
control which attains a local maximum of J can be found
either numerically using the model of the system or ex-
perimentally. In both circumstances, the ﬁrst step of a
common procedure is to apply a trial pulse ε0 and obtain
the outcome J(ε0), either numerically or measuring it in
the laboratory. The second step is to make various small
∗Electronic address:
apechen@gmail.com;
URL: http://www.
mathnet.ru/eng/person17991
modiﬁcations of ε0 and ﬁnd ε1 which produces maximum
increase in J. Then ε1 is used as a new trial pulse and
the procedure is repeated until no signiﬁcant increase is
produced or a maximum number of iterations is reached.
Of crucial practical importance is to know whether
J(ε) has traps, i.e. local maxima with the values less than
the global maximum, as necessary to properly choose be-
tween local (e.g., gradient) and global optimization meth-
ods [14–19]. Traps can strongly inﬂuence on both theo-
retical and experimental quantum control studies—they
determine the level of diﬃculty of controlling the system
and can signiﬁcantly slow down or even completely pre-
vent ﬁnding globally optimal controls. Whereas the anal-
ysis of traps in manipulation by quantum systems has at-
tracted high attention [20–28], no examples of trap-free
quantum systems have been known. Only partial the-
oretical results have been obtained stating the absence
of traps at special regular controls.
This ﬁnding does
not at all exclude the absence of traps that makes the
problem open since even a single trap may produce sig-
niﬁcant diﬃculties for the optimization if it has a large
attracting domain [29]. In this work we show that the LZ
system is trap-free and hence, for example, the only ex-
trema of J(ε) = Pi→f for this system are global maxima
and minima. This ﬁnding provides the ﬁrst example of
a trap-free quantum control system where unconstrained
local manipulations are always suﬃcient to ﬁnd best con-
trol pulses. Suﬃciently strong constraints on the controls
may destroy this property and in the end we discuss pos-
sible limitations for the analysis due to decoherence, noise
in the control pulses and limited tunability of the control
strength and time scales in laboratory experiments.
II.
TRAPS AND CONTROL LANDSCAPES
Formally, a control ﬁeld ε(t) is a trap for the objec-
tive J(ε) if it is a local maximum, i.e., a maximum with
the value less than the global maximum, J(ε) < Jmax =
arXiv:1304.1357v1  [quant-ph]  4 Apr 2013


## Page 2


2
max
ε
J(ε) (in this work we consider as control goal maxi-
mizing the objective; if the goal is to minimize the objec-
tive then traps are local minima). Answering the ques-
tion whether traps exist for a given control problem is
crucial for determining proper algorithms and our abili-
ties for ﬁnding optimal control ﬁelds. In the absence of
traps, local search algorithms should generally be able
to ﬁnd globally optimal controls (exceptions may occur
if the initial control is chosen exactly at a saddle point,
where the gradient of the objective is zero). If the ob-
jective has traps (perhaps even a single trap with large
attracting domain) then local search procedures may con-
verge to local maxima instead of attaining a desired glob-
ally optimal control and more sophisticated global search
methods should be exploited for a successful optimiza-
tion.
Traps are critical points, i.e., the gradient ∇Jε = 0 at
any trap. Critical points for control objectives J(ε) =
Pi→f were studied in seminal works [20], where the ab-
sence of traps was suggested. The suggestion was drawn
from the proof that any function of the form f(U) =
Tr[Uρ0U †O] (ρ0 is a positive matrix and O is Hermitian)
deﬁned on the unitary group U(n), where n is the system
dimension, has as extrema only global maxima, global
minima, and saddles and has no traps. (Extrema of trace
functions over unitary and orthogonal groups were stud-
ied in other contexts by J. von Neumann [30], R. Brock-
ett [31], S. Glaser et al [32], etc.) Then, under the con-
trollability condition which assumes that any U ∈U(n)
can be generated by some control, this result was used to
conclude the absence of traps for the underlying objective
functional J(ε). Later it was shown that the conclusion
of the absence of traps requires an additional assumption
that the map χ : ε →U ε
T is non-degenerate [21], meaning
that arbitrary inﬁnitesimal variations of ε produce vari-
ations of U ε
T in all directions on U(n) [33, 34]. While the
controllability condition is relatively easy to verify [35],
checking the non-degeneracy assumption turned out to
be a hard problem. Moreover, critical controls violating
this assumption were found [24, 25], and even second-
order traps—critical controls which are not global max-
ima and where the Hessian H = δ2J/(δε)2 is negative
semideﬁnite were shown to exist under rather general as-
sumptions [26]. (Second-order traps are not necessarily
local maxima but eﬀectively they are traps for local algo-
rithms exploiting at most second order local information
about the objective; see Chapter 20 of [36] for a gen-
eral discussion of the non-degeneracy and second order
optimality conditions.) These ﬁndings led to reconsid-
eration of the conclusion of absence of traps. Some nu-
merical simulations suggested that the condition of non-
degeneracy might be generally satisﬁed or at least its vi-
olation does not produce multiple traps [27], while other
indicated possible trapping behavior [25, 29]. However,
numerical search is limited and the extent to which these
runs span the full space of quantum control possibilities
is questionable [29]. Hence the problem of proving either
existence or absence of traps has been remained open.
III.
ABSENCE OF TRAPS FOR THE
LANDAU-ZENER SYSTEM
Our main result is that the only critical points of any
objective of the form J(ε) = f(U ε
T ), where U ε
T satis-
ﬁes (1) and f(U) is any function on the special unitary
group SU(2) which has no local extrema, are global max-
ima, global minima, and the zero control ﬁeld ε(t) = 0.
Important examples of such objectives include
• Transition probability
Ji→f(ε) = |⟨f|U ε
T |i⟩|2
This objective is maximized by a control which
completely transfers the initial state |i⟩into the de-
sired ﬁnal state |f⟩.
• Expectation of a system observable O
JO(ε) = Tr[U ε
T ρ0U ε†
T O]
Here O is a Hermitian matrix representing the ob-
servable and ρ0 is the initial system density matrix.
The objective is maximized by a control which max-
imizes quantum-mechanical average of O at time T.
• Generation of a unitary process W
JW (ε) = 1
4|Tr(W †U ε
T )|2
Here W is the unitary matrix representing a desired
system evolution or a desired quantum gate, for
example Hadamard gate. Maximum of this objec-
tive is achieved by a control such that UT = eiφW,
where φ is arbitrary (generally unphysical) phase.
Factor 1/4 is chosen to have max
ε
JW (ε) = 1.
Proof of the main result.
We will consider ﬁrst
J(ε) = Ji→f(ε).
For brevity, we will sometimes omit
the superscript ε in U ε
t and U ε
T , and without loss of gen-
erality set ∆= 1. Gradient of J(ε) = |⟨f|U ε
T |i⟩|2 for the
LZ system has the form [26]
∇Jε(t) = 2ℑ

⟨i|U †
T |f⟩⟨f|UT U †
t σzUt|i⟩

(2)
It can be written as ∇Jε(t) = L(U †
t σzUt) = l(t), where
L : su(2) →R is the linear map on the Lie algebra of
traceless Hermitian 2 × 2 matrices deﬁned by L(A) =
2ℑ[⟨i|U †
T |f⟩⟨f|UT A|i⟩], and l(t) is a real-valued function.
If ε is a critical control ﬁeld, then l(t) ≡0 and therefore,
in particular, l′(t) = l′′(t) = 0. These derivatives can be
computed to be
l′(t) = L(−iU †
t [σx + ε(t)σz, σz]Ut) = −2L(U †
t σyUt)
l′′(t) = −2L(−iU †
t [σx + ε(t)σz, σy]Ut)
= −4L(U †
t σzUt) + 4ε(t)L(U †
t σxUt)


## Page 3


3
Thus the condition l′′ = l′ = l = 0 for any t such that
ε(t) ̸= 0 takes the form
L(U †
t σxUt) = L(U †
t σyUt) = L(U †
t σzUt) = 0
(3)
The matrices U †
t σxUt, U †
t σyUt, U †
t σzUt are linearly inde-
pendent traceless Hermitian 2 × 2 matrices. They form
a basis of su(2) and hence (3) implies L(A) = 0 for any
A ∈su(2).
Let |i⊥⟩be the state which is orthogonal to |i⟩. Taking
A = |i⟩⟨i⊥| + |i⊥⟩⟨i| and A′ = i(|i⟩⟨i⊥| −|i⊥⟩⟨i|) gives
L(A)
= 0 ⇒ℑ

⟨i|U †
T |f⟩⟨f|UT |i⊥⟩

= 0
L(A′) = 0 ⇒ℜ

⟨i|U †
T |f⟩⟨f|UT |i⊥⟩

= 0
Thus ⟨i|U †
T |f⟩⟨f|UT |i⊥⟩= 0, i.e. either ⟨i|U †
T |f⟩= 0 or
⟨f|UT |i⊥⟩= 0. The former case corresponds to the global
minimum of the objective (J = 0) and the latter to its
global maximum (J = 1). These are the only allowed
critical controls except of ε(t) ≡0.
This ﬁnishes the
proof of the main result for Ji→f(ε).
The analysis above immediately implies that if a lin-
ear map L : su(2) →R satisﬁes L(U †
t σzUt) = 0 then
L ≡0. Now we will show that it means that the map
χ : ε →U ε
T is non-degenerate everywhere outside of
ε(t) ≡0. Since we consider objectives produced by func-
tions on SU(2) which therefore invariant with respect to
the overall phase of U ε
T , we can identify U ε
T with the cor-
responding element of SU(2). Small variations around
U ε
T can be represented as ˜U ε
T = U ε
T eδw ≈U ε
T (1 + δw),
where δw = −i
R T
0 U †
t σzUtδε(t)dt.
For the map χ to
be non-degenerate, ˜U ε
T should span a neighborhood of
U ε
T that in turn requires δw to span su(2). If δw does
not span su(2), then there exists A ∈su(2), A ̸= 0
such that (A, δw) ≡Tr(A†δw) = 0 for all δε and hence
LA(U †
t σzUt) := Tr(A†U †
t σzUt) = 0. This is possible only
if A = 0 and hence the map can not be degenerate.
Therefore our result immediately implies the absence of
traps at any ε ̸= 0 for any objective functional J(U ε
T )
which has no traps if considered as a function on SU(2).
This includes important objectives JO = Tr[U ε
T ρ0U ε†
T O]
for maximizing expectation of a system observable O
and JW
= (1/4)|Tr(W †U ε
T )|2 for optimal generation
of a unitary process W (e.g., for unitary gate genera-
tion).
These objectives appear to be trap-free for the
LZ system since functions fO(U) = Tr[Uρ0U †O] and
fW (U) = (1/4)|Tr(W †U)|2 have no local maxima on
SU(2) [20].
The control ε(t) ≡0 requires a separate consideration
since the condition l′′(t) = 0 for ε ≡0 can not be used to
conclude L(U †
t σxUt) = 0. This control is however not a
trap for example for Ji→f as shown by direct computation
in the Appendix.
FIG. 1:
(Color online) The control landscape of J0→1(a1, a2)
for the LZ system controlled by piecewise constant controls
(N = 2, T = 10, ∆= 1). The landscape possesses multiple
traps (local maxima).
IV.
DISCUSSION
Now we discuss important limitations for the present
analysis. No real-world system will perfectly evolve ac-
cording to Eq. (1) and three general kinds of deviations
from the ideal situation include decoherence eﬀects, de-
viations of the actual control from the intended one due
to noise or imperfections of the laboratory setup, and
limited tunability of the control strength and time scales
in laboratory experiments. While we consider the sys-
tem as evolving according to the Schr¨odinger equation
with unitary evolution, in real circumstances it can ex-
perience additional inﬂuence of the environment which
causes the dynamics to be non-unitary. We also assume
that any shape of the control ε(t) is available, whereas
typical pulses are either piecewise constant or ﬁnite sums
of cosines and sines at certain ﬁxed frequencies. These
assumptions are common for the ﬁrst step of control land-
scape analysis which deals with the ideal situation of
noiseless unconstrained controls. The next step upon es-
tablishment of the ideal landscape properties is to study
the eﬀects of possible deviations, which we discuss below
for the LZ system.
The requirements on the available control ﬁelds (e.g.
on their strength and time scale) necessary for the con-
clusion of the absence of traps for attaining maximal ob-
jective value are such that the available controls are suﬃ-
cient to guarantee controllability of the system. Minimal
control time for the LZ system can be estimated using the
fundamental theory of optimal control at the quantum
speed limit as TQSL ≈∆E−1
0
arccos(|⟨i, f⟩|), where ∆E0
is the energy variance of the free Hamiltonian H0 = ∆·σx
calculated on the initial state [10]. Hence our analysis
applies to any ﬁnal time T ≳π∆E−1
0 .
If for a given
physical system decoherence eﬀects occur on a time scale
slower than ∆E−1
0 , they can be neglected when the con-
trol is implemented in the time optimal fashion.
This
shows that while ﬁnite-time [37] and decoherence [38–40]
eﬀects can be important for the LZ system, they do not
modify the trap-free landscape property as soon as ﬁnal
time T is suﬃciently smaller that the relaxation time and
at the same time is not too small to violate controllability


## Page 4


4
FIG. 2:
(Color online) Probability of trapping as a func-
tion of N for piecewise constant controls (T = 10, ∆= 1).
For every point, 103 runs of MATLAB realization of the
Broyden-Fletcher-Goldfarb-Shanno (BFGS) optimization al-
gorithm where performed each starting at a random initial
control a = (a1, . . . , aN) [41]. Initial control amplitudes are
uniformly distributed in the range ai ∈[A, A] but are allowed
to escape this range during the search. The search is deﬁned
as trapped if the attained objective is less than 0.99. Trap-
ping may occur due to the presence of local maxima and/or
principal impossibility of attaining the objective value greater
that 0.99 with available controls. Probability of trapping is
estimated as a fraction of trapped runs among all 103 runs.
of the systems.
An extensive numerical analysis of control landscapes
for multi-level model systems with realistic laboratory
control ﬁelds is provided in [27]. To analyze the role of
limitations on the available control ﬁelds for the LZ sys-
tem, we numerically estimate the probability of trapping
when available controls are piecewise constant controls of
the form ε(t) = PN
i=1 aiχ[ti,ti+1](t), where χ[ti,ti+1](t) = 1
if t ∈[ti, ti+1] and zero otherwise and ai are the control
parameters. Typically, N ≈100 and control amplitudes
are constrained within certain ranges, say ai ∈[−A, A].
Exact solution for piecewise constant controls can be ob-
tained for example in the simplest case N = 1.
The
objective for maximizing the probability of spin ﬂip
J0→1 = |⟨0|U ε
T |1⟩|2 by a constant control ε(t) = a can
be computed to be J0→1(a) = sin2(T
√
1 + a2)/(1 + a2).
Its traps (local maxima) are given by solutions of the
equation tan(T
√
1 + a2) = T
√
1 + a2; the correspond-
ing objective values are J0→1(a) = T 2/(1 + T 2 + T 2a).
Control landscapes for a two-dimensional control space
(N = 2) are more complex. Fig. 1 shows as an exam-
ple the control landscape of J0→1(a1, a2). The landscape
has multiple local maxima showing that signiﬁcant re-
strictions on the control space in an originally trap-free
system may produce traps. Fig. 2 provides the numeri-
cally estimated probability of trapping for piecewise con-
stant controls as a function of N.
The probability of
trapping becomes negligible already for N = 10–15 that
means that limitations on the number of components N
of available laboratory control ﬁelds have minor eﬀect
already for N ≳10 and hence should be negligible for
realistic case N ≈100.
In the laboratory, actual controls may deviate from the
designed numerically optimal pulse due to noise and im-
perfections of experimental setup [42]. These noise eﬀects
can inﬂuence on the landscape structure by decreasing
the maximal objective value. We adopt the general the-
ory of [43] to analyze this inﬂuence for the LZ system.
Let ε0(t) be an optimal control in the ideal situation of
absence of noise. In the presence of a random noise ξ(t),
the actual control will ﬂuctuate as ε(t) = ε0(t)+ϱ(t)ξ(t),
where ϱ(t) = 1 for additive noise and ϱ(t) = ε0(t) for
multiplicative noise. A weak noise modiﬁes the averaged
objective as
E[J(ε0)] ≈J(ε0)+1
2
T
Z
0
T
Z
0
H0(t, t′)ϱ(t)ϱ(t′)E[ξ(t)ξ(t′)]dtdt′
where H0(t, t′) =
δ2J
δε0(t)δε0(t′) is the Hessian of the ob-
jective computed at the optimal control ﬁeld ε0 and
E[ξ(t)ξ(t′)] is the autocorrelation function of the noise.
Since Hessian is negative semideﬁnite at the maximum,
the noise generally decreases the average ﬁdelity.
The
objective for additive (AWN) and multiplicative (MWN)
white noise with autocorrelation function E[ξ(t)ξ(t′)] =
σδ(t−t′), where σ2 is the variance of the noise amplitude
distribution, takes the forms
EAWN[J(ε0)] ≈J(ε0) + σ2
2
T
Z
0
H0(t, t)dt
EMWN[J(ε0)] ≈J(ε0) + σ2
2
T
Z
0
H0(t, t)|ε0(t)|2dt
The last term in these equations is the noise-induced de-
crease −D(ε0, σ, T) of the objective (such that E(J) ≈
J(ε0) −D with D ≥0).
The diagonal of the Hes-
sian for J
= Ji→f can be shown to be H0(t, t) =
−2|⟨i|U †
t σzUt|i⊥⟩|2 so that |H0(t, t)| ≤2.
Therefore
D(ε0, σ, T) for J = Ji→f is majorized by
DAWN(ε0, σ, T) ≤σ2T
DMWN(ε0, σ, T) ≤σ2E
where E =
R T
0 |ε0(t)|2dt is the total energy of the pulse.
The diagonal of the Hessian for the objective JW is
H0(t, t) = −2 and therefore for this objective DAWN =
σ2T and DMWN = σ2E. It then follows that in both cases
the inﬂuence of a weak AWN can be minimized by us-
ing time optimal controls, while minimizing weak MWN
can be done by selecting less energetic pulses among all
optimal pulses.
If the ideal landscape has multiple global optima with
diﬀerent H0(t, t), then the noise induced decrease of ob-
jective can be diﬀerent at diﬀerent optima that can pro-
duce traps in the non-ideal landscape. Weak decoherence


## Page 5


5
operates similarly to weak noise and can also produce
traps in the ideally trap-free landscape [20]. These de-
viations from the ideal situation should be avoided to
reveal the trap-free landscape property by either oper-
ating in the time optimal regime or using weak optimal
controls to combat MWN. Strong noise and strong deco-
herence that can signiﬁcantly modify the landscape are
out of scope of this discussion.
Conclusions.—This work shows that unconstrained
manipulation in the Landau-Zener system is free of traps
and hence unconstrained local search for optimal con-
trols is always able to ﬁnd best optima. The impact on
this result of laboratory limitations due to decoherence,
noise in the actual control pulses, and restrictions on the
available control ﬁelds is discussed.
Acknowledgments
A. Pechen acknowledges support of the Marie Curie In-
ternational Incoming Fellowship within the 7th European
Community Framework Programme. N. Il’in is partially
supported by the Russian Foundation for Basic Research.
This research is made possible in part by the historic
generosity of the Harold Perlman family and by the Min-
istry of Education and Science of the Russian Federation,
project 8215.
Appendix
Here we prove that the control ε(t) ≡0 is not a trap for
state-to-state transfer described by the objective J(ε) =
Ji→f(ε). The evolution operator produced by ε(t) = 0
has the form Ut = e−itσx. Therefore Vt := U †
t σzUt =
cos(2t)σz + sin(2t)σy and the gradient of the objective is
∇Jε=0(t) = cos 2t · L(σz) + sin 2t · L(σy)
If ε(t) = 0 is a critical point, then ∇Jε=0(t) = 0 for any
t ∈[0, T], and hence L(σz) = L(σy) = 0. If α := L(σx) =
0, then L ≡0 on su(2) and similarly to the proof of the
main result we conclude that ε = 0 is not a trap.
Now consider the case α ̸= 0. In this case |i⟩and |f⟩
are such that ε = 0 is neither a global maximum nor
global minimum. The evolution operator produced by a
small variation of the control δε can be represented as
U δε
T = e−iT σxWT , where WT satisﬁes
˙Wt = −iδε(t)VtWt,
W0 = I
The operator WT can be computed up to the second order
in δε as
WT = I + A1 + A2 + o(∥δε∥2)
A1 = −i
Z T
0
dtδε(t)Vt,
A2 = −
Z T
0
dt1
Z t1
0
dt2δε(t1)δε(t2)Vt1Vt2
This gives the perturbation expansion for the objective
(here |f′⟩= eiT σz|f⟩)
J(δε) = |⟨f′|I + A1 + A2 + . . . |i⟩|2
= |⟨f′|i⟩|2 + δJ1(δε) + δJ2(δε) + o(∥δε∥2)
where
δJ1(δε) = 2ℜ(⟨f′|i⟩⟨f′|A1|i⟩)
δJ2(δε) = |⟨f′|A1|i⟩|2 + 2ℜ(⟨f′|i⟩⟨f′|A2|i⟩)
Hence the variation of the objective satisﬁes (note that
|⟨f′|i⟩|2 = J(0))
δJ = J(δε) −J(0) = δJ1(δε) + δJ2(δε) + o(∥δε∥2)
If ε = 0 is a critical control, then δJ1(δε) = 0 for any
δε. We will show the existence of controls δε1 and δε2
such that δJ2(δε1) and δJ2(δε2) have opposite signs. It
is suﬃcient to choose δε1 and δε2 to satisfy ⟨f′|A1|i⟩= 0,
e.g.
Z T
0
dtδεi(t) cos 2t =
Z T
0
dtδεi(t) sin 2t = 0,
i = 1, 2.
Since Vt1Vt2 = cos 2(t1 −t2) + iσx sin 2(t1 −t2), we have
δJ2(δε) = 2
Z T
0
dt1
Z t1
0
dt2δε(t1)δε(t2)

J(0) cos 2(t1 −t2)
+α sin 2(t1 −t2)

= 2α
Z T
0
dt1
Z t1
0
dt2δε(t1)δε(t2) sin 2(t1 −t2)
Assuming for simplicity that T ≥π, we take δε1(t) =
χ[0,π](t) and δε2(t) = cos(4t)χ[0,π](t), where χ[0,π](t) is
the characteristic function of the interval [0, π].
Then
δJ2(δε1) = −πα and δJ2(δε2) = πα/6.
Therefore for
α ̸= 0 there exist control variations around ε(t) = 0
increasing the objective and control variations decreasing
it. This implies that ε(t) = 0 is neither a local maximum
nor minimum.
[1] D. J. Tannor and S. A. Rice, J. Chem. Phys. 83, 5013
(1985); S. A. Rice and M. Zhao, Optical Control of Molec-
ular Dynamics (Wiley, New York, 2000); P. W. Brumer
and M. Shapiro, Principles of the Quantum Control of


## Page 6


6
Molecular Processes (Wiley-Interscience, 2003); Control
of Molecular and Quantum Systems (in Russian), Eds.
A. L. Fradkov and O. A. Yakubovskii (Institute for Com-
puter Studies, Moscow-Izhevsk, 2003); D. J. Tannor, In-
troduction to Quantum Mechanics: A Time Dependent
Perspective (University Science Press, Sausalito, 2007);
V. S. Letokhov, Laser Control of Atoms and Molecules
(Oxford University Press, USA, 2007); D. D’Alessandro,
Introduction to Quantum Control and Dynamics (Chap-
man & Hall, Boca Raton, 2007); D. V. Zhdanov and
V. N. Zadkov, Phys. Rev. A 77, 011401 (2008); M. G.
Reuter, M. A. Ratner, and T. Seideman, Phys. Rev. A
86, 013426 (2012); Brif, R. Chakrabarti, and H. Rabitz,
in Advances in Chemical Physics, edited by S. A. Rice
and A. R. Dinner (Wiley, New York, 2012), vol. 148, p.
1.
[2] L. Landau, Phys. Z. Sowjetunion 2, 46 (1932); C. Zener,
Proc. R. Soc. London A 137, 696 (1932); E. C. G.
St¨uckelberg, Helv. Phys. Acta 5, 369 (1932); E. Majo-
rana, Nuovo Cimento 9, 43 (1932).
[3] A. M. Kuznetsov, Charge Transfer in Physics, Chem-
istry, and Biology (Gordon & Breach, Reading, 1995).
[4] A. Warshel, Proc. Natl. Acad. Sci. USA 77, 3105 (1980).
[5] B. M. Smirnov, Physics of Atoms and Ions (Springer,
New York, 2003).
[6] V. L. Pokrovskii, Physics-Uspekhi 52, 1169 (2009).
[7] M. G. Bason, M. Viteau, N. Malossi, P. Huillery, E. Ari-
mondo, D. Ciampini, R. Fazio, V. Giovannetti, R. Man-
nella, and O. Morsch, Nature Physics 8, 147 (2012).
[8] B. W. Shore, K. Bergmann, and J. Oreg, Z. Phys. D.:
Atoms, Molecules and Clusters, 23, 33 (1992).
[9] M. Jona-Lasinio, O. Morsch, M. Cristiani, N. Malossi, J.
H. M¨uller, E. Courtade, M. Anderlini, and E. Arimondo,
Phys. Rev. Lett. 91, 230406 (2003).
[10] T. Caneva, M. Murphy, T. Calarco, R. Fazio, S. Mon-
tangero, V. Giovannetti, and G. E. Santoro, Phys. Rev.
Lett. 103, 240501 (2009).
[11] A. Brataas and E. I. Rashba, Phys. Rev. B 84, 045301
(2011).
[12] O. V. Baturina and O. V. Morzhin, Programmable Sys-
tems: Theory and Applications 2(1), 51 (2011); Autom.
Remote Control, 72(6), 1213 (2011).
[13] J. E. Avron, M. Fraas, G. M. Graf, and P. Grech, Comm.
Math. Phys. 305, 633 (2011).
[14] D. J. Tannor, V. Kazakov, V. Orlov, in Time-Dependent
Quantum Mechanics, edited by J. Broeckhove and L.
Lathouwers (Plenum Press, New York, 1992), P. 347.
[15] V. F. Krotov and I. N. Feldman, Eng. Cybern. 17, 123
(1983); V. F. Krotov, Autom. Remote Control 70(3), 357
(2009).
[16] N. Khaneja, T. Reiss, C. Kehlet, T. Schulte-Herbr¨uggen,
and S. Glaser, J. Magn. Reson. 172, 296 (2005).
[17] M. S. Anan’evskii and A. L. Fradkov, Autom. Remote
Control 66(5), 734 (2005).
[18] R. Eitan, M. Mundt, and D. J. Tannor, Phys. Rev. A 83,
053426 (2011).
[19] S. Machnes et al, Phys. Rev. A 84, 022305 (2011).
[20] H. Rabitz, M. Hsieh, and C. Rosenthal, Science 303, 1998
(2004); Phys. Rev. A 72, 052337 (2005).
[21] T.S. Ho and H. Rabitz, J. Photochemistry A, 180, 226
(2006).
[22] M. Hsieh, R. Wu, H. Rabitz, and D. Lidar, Phys. Rev. A
81, 062352 (2010).
[23] S. Ruetzel, C. Stolzenberger, S. Fechner, F. Dimler, T.
Brixner, and D. J. Tannor, J. Chem. Phys. 133, 164510
(2010).
[24] R. Wu, R. Long, J. Dominy, T.-S. Ho, and H. Rabitz,
Phys. Rev. A 86, 013405 (2012).
[25] P. de Fouquieres and S. G. Schirmer, arXiv:1004.3492.
[26] A. N. Pechen and D. J. Tannor, Phys. Rev. Lett. 106,
120402 (2011).
[27] K. W. Moore and H. Rabitz, Phys. Rev. A 84, 012109
(2011).
[28] A. N. Pechen and D. J. Tannor, Isr. J. Chem. 52, 467
(2012).
[29] A. N. Pechen and D. J. Tannor, Phys. Rev. Lett. 108,
198902 (2012).
[30] J. von Neumann, Tomsk Univ. Rev. 1, 286 (1937); see
also J. von Neumann, Collected Works, A. H. Taub, Ed.
(Pergamon, New York, 1962), vol. IV, pp. 205–218.
[31] R. Brockett, Lin. Alg. Appl. 122/123/124, 761 (1989).
[32] S. J. Glaser, T. Schulte-Herbr¨uggen, M. Sieveking, O.
Schedletzky, N. C. Nielsen, O. W. Sørensen, and C.
Griesinger, Science 280, 421 (1998).
[33] R. Chakrabarti and H. Rabitz, Intl. Rev. Phys. Chem.
26, 671 (2007).
[34] R. Wu, A. Pechen, H. Rabitz, M. Hsieh, and B. Tsou, J.
Math. Phys. 49, 022108 (2008).
[35] G. Huang, T. Tarn, and J. Clark, J. Math. Phys. 24,
2608 (1983); C. Altaﬁni, ibid. 43, 2051 (2002).
[36] A. A. Agrachev and Yu. L. Sachkov, Control Theory from
the Geometric Viewpoint (Springer, 2004).
[37] N. V. Vitanov and B. M. Garraway, Phys. Rev. A 53,
4288 (1996).
[38] P. Ao and J. Rammer, Phys. Rev. Lett. 62, 3004 (1989).
[39] V. M. Akulin and W. P. Schleich, Phys. Rev. A 46, 4110
(1992).
[40] M. Scala, B. Militello, A. Messina, and N. V. Vitanov,
Phys. Rev. A 84, 023416 (2011).
[41] We use BFGS Hessian update for choosing the search di-
rection in the quasi-Newton algorithm built in the MAT-
LAB routine fminunc for unconstrained nonlinear opti-
mization. Exact gradient of the objective is provided. De-
fault MATLAB stopping criteria are modiﬁed as follows:
maximum number of objective evaluations is 103N, ter-
mination tolerance on the objective value and on ai is
10−8.
[42] A. F. Bartelt, M. Roth, M. Mehendale, and H. Rabitz,
Phys. Rev. A 71, 063806 (2005).
[43] K. W. Moore, C. Brif, M. D. Grace, A. Donovan,
D. L. Hocker, T. S. Ho, R. Wu, and H. Rabitz ,
arXiv:1112.0333.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
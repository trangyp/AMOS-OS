---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1508.04600v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1508.04600v1_Discrimination_of_time-dependent_inflow_properties_with_a_cooperative_dynamical_

> Source: 1508.04600v1_Discrimination_of_time-dependent_inflow_properties_with_a_cooperative_dynamical_.pdf

> Pages: 25

---


## Page 1


arXiv:1508.04600v1  [nlin.AO]  19 Aug 2015
Discrimination of time-dependent inﬂow
properties with a cooperative dynamical
system
Hiroshi Uenoa, Tatsuaki Tsuruyamab, Bogdan Nowakowskic,
Jerzy G´oreckic,∗and Kenichi Yoshikawaa,∗
a Faculty of Life and Medical Sciences,
Doshisha University, Kyoto 610-0394, Japan
bDepartment of Diagnostic Pathology, Graduate School of Medicine,
Kyoto University, Japan
cInstitute of Physical Chemistry, Polish Academy of Sciences,
Kasprzaka 44/52, 01-224 Warsaw, Poland.
∗jgorecki@ichf.edu.pl
∗keyoshik@mail.doshisha.ac.jp
September 4, 2018
Abstract
Many physical, chemical and biological systems exhibit a cooperative
or sigmoidal response with respect to the input. In biochemistry, such
1


## Page 2


behavior is called an allosteric eﬀect.
Here we demonstrate that a
system with such properties can be used to discriminate the amplitude
or frequency of an external periodic perturbation or input. Numerical
simulations performed for a model sigmoidal kinetics illustrate that
there exists a narrow range of frequencies and amplitudes within which
the system evolves toward signiﬁcantly diﬀerent states.
Therefore,
observation of system evolution should provide information about the
characteristics of the perturbation. The discrimination properties for
periodic perturbation are generic. They can be observed in various
dynamical systems and for diﬀerent types of periodic perturbation.
1
Introduction
Bistability and hysteresis are commonly observed in physics, chemistry and
biology [1–5]. Let us assume that a system has two stable states S1 and S2
and that an increase in the value of control parameter λ above the threshold
λ1 triggers the transition from S1 to S2, whereas the reverse transition from
S2 to S1 occurs if the value of the control parameter drops below λ2. Such
a system can obviously be used as a discriminator of the control parameter
value. For example, if the initial state is S1 and after some time we observe
the system in S2, then at some point the value of the control parameter
necessarily exceeded λ1.
However, if only time-monotonic changes in the
value of the control parameter are considered, then the system discrimination
ability is reduced to just two values ; λ1 and λ2.
In this paper we demonstrate the suitability of a dynamical system charac-
terized by sigmoidal kinetics for discrimination-oriented applications, under
2


## Page 3


a new strategy of imposing a periodic perturbation or input on a cooper-
ative system.
It has been reported [6–8] that periodic perturbations can
signiﬁcantly change the time evolution of a nonlinear system. As a discrim-
inator prototype, we consider a two-variable system in which the inﬂow of
one of the variables is a control parameter. Numerical simulations reveal a
non-trivial property of such a system: a marginal change in the inﬂow pa-
rameters (amplitude or frequency) can switch the response of a cooperative
system between diﬀerent branches in the stage diagram. The frequency at
which such switching occurs is a monotonic function of the inﬂow ampli-
tude. Therefore, at a ﬁxed amplitude of periodic inﬂow, the observation of a
transition between diﬀerent types of oscillatory evolution of the system pro-
vides information which allows us to discriminate the inﬂow frequency. The
above discussion does not necessarily limit the range of frequencies that can
be discriminated by the observation of transitions between diﬀerent types
of oscillations Similarly, for a ﬁxed frequency of periodic inﬂow, transitions
between diﬀerent types of system oscillations occur within a narrow range of
amplitudes. The transition can be used to discriminate the inﬂow amplitude,
but for the model considered here, the useful range of such discrimination is
rather limited.
In numerical simulations, we consider simple system dynamics deﬁned by
a single sigmoidal term expressed by a rational function, which is typical for
enzymatic reactions [9–13]. In such reactions the appearance of sigmoidal
kinetic behavior is usually interpreted to be the result of the interaction of
substrates with enzymes through positive cooperative binding. Modeling of
3


## Page 4


cooperative binding leads to the Hill equation [9]:
θ =
[L]n
Kd + [L]n
(1)
where θ is the fraction of ligand binding sites ﬁlled, [L] is the ligand con-
centration, Kd is the apparent dissociation constant derived from the mass
action law, and n is the Hill coeﬃcient which represents the degree of coop-
erativity. If n = 1, there is no cooperativity; for n > 1, the cooperativity
is positive. Kinetics with sigmoidal behavior are not limited to enzymatic
reactions. This also describes the response of various biological systems to
external stimuli, including the eﬀect of drug delivery, which is an interesting
topic in pharmacology. Among the many experimental studies that have re-
ported sigmoidal behavior, the Hill coeﬃcient n usually has a value between 2
and 4 [9–19]. Here we selected n = 3 for the numerical simulations presented
below.
The paper is organized as follows. In the next section, we consider a
bistable model and study its time evolution as a function of the amplitude and
frequency of periodic inﬂow. We demonstrate how the system can be used
as a discriminator and discuss the sources of discrimination errors. In the
ﬁnal section we argue that the observed phenomenon is generic and discuss
its potential applications.
4


## Page 5


2
The response of a model dynamical system
to periodic perturbations
Let us consider a dynamical system of two variables (x(t), y(t)) deﬁned by a
set of diﬀerential equations:
dx
dt = g(x, y, t) = −αx + y + A · (sin(2πft + φ0) + 1) · Θ(t)
(2)
dy
dt = h(x, y) = 1
ε · (
x3
1 + x3 −y)
(3)
In Eq.(2), the last term I(t) = A · (sin(2πft + φ0) + 1) · Θ(t) describes a
periodic inﬂow of x with frequency f and initial (for t = 0) phase φ0. Θ(t)
is the Heaviside step function. We assume that the there is no inﬂow for
t < 0, and it is switched on at t = 0.
If φ0 = 3 · π/2, then I(t) is a
continuous function. In this case, I(t = 0) = 0. It then increases and ﬁnally
oscillates. For any other phase, the inﬂow term is not continuous at t = 0;
for example, if φ0 = π/2 and then I(t = 0) = 2 · A. I(t) then decreases and
ﬁnally oscillates. The inﬂow term is always non-negative. For t > 0 the time
average of I(t) equals A and is independent of the frequency and the initial
phase. If the inﬂow amplitude A = 0, then (x = 0, y = 0) is the only steady
state of Eqs.(2,3) and is stable. In the following analysis, we assume that the
stable state of the system without ﬂow is the initial state for the simulated
evolution.
Initially, let us consider the time evolution of the system for a constant
inﬂow I(t) = A > 0 for t ≥0 (thus, f = 0 and φ0 = 0). The characteristics
of the time evolution depend on the amplitude of the inﬂow term and on the
initial state. In this case, the nullcline g(x, y, t) = 0 is the time-independent
line with a deﬁnite slope determined by the value of α and a shift which
5


## Page 6


depends on the inﬂow amplitude A. Figure 1 shows the location of nullclines,
calculated for ε = 1, α = 0.55 and a few diﬀerent values of the inﬂow. Let
us assume that A1 and A2 are the amplitudes for which the BN g(x, y) = 0
nullcline is tangential to the sigmoidal-shaped nullcline h(x, y) = 0. The
stable stationary states of the system can be located on two branches on
the h(x, y) = 0 nullcline. One contains all of the points of the h(x, y) = 0
nullcline located between point (0, 0) and the tangency point (x1, y1). We will
call it the lower stable branch (LSB). The other is the upper stable branch
(USB), and is formed by all of the points of the h(x, y) = 0 nullcline located
above (x2, y2). The stationary states located on the nullcline between (x1, y1)
and (x2, y2) are unstable. In the case when A < A2, the only stationary state
is located on the lower stable branch, so the system converges to the stable
state y∞= limt→∞y(t) such that y∞≤y1 regardless of the initial state.
Similarly, for A > A1, the single BN stationary state is located on the upper
stable branch, and for all initial states the system converges to the stable
state y∞≥y2. For A2 ≤A ≤A1, the stationary state that is approached
for t →∞depends on the initial state and on the partition of the phase
space determined by the separatrices of the saddle point which is located
on the middle branch of the h nullcline.
This analysis also applies when
the frequency of inﬂow oscillations is very high. In such a case, the ﬂow
oscillations are much faster than both the system dynamics and the system
responses to the time-averaged value of the inﬂow A.
For suﬃciently slow oscillations of the inﬂow ( 0 < f ≪1), the system
can follow the slowly relocating stable state, the position of which varies
according to the instantaneous value of the inﬂow.
If the initial state of
6


## Page 7


the system is (x(0) = 0, y(0) = 0) and 2 · A ≤A1, then y(t) ≤y1 for all
t. Therefore, the system state oscillates along the lower stable branch of
the h(x, y) = 0 nullcline with the period deﬁned by the frequency of inﬂow
oscillations.
If 2 · A > A1, then there are intervals of time within which
the system has a single stationary state located on the upper stable branch.
During a single oscillation cycle, there are moments of time t1 and t2 at which
y(t1) ≤y1 and y(t2) ≥y2, and thus oscillations that extend over both stable
branches are expected.
For moderate values of f, the system dynamics are too slow to closely
follow the changes in the inﬂow value. In such a case, oscillations around a
stable state located in the lower stable branch that extend to the unstable
branch, as well as oscillations around a stable state located in the upper
stable branch that extend to the unstable branch, should be observed. This
is conﬁrmed by numerical simulations.
The complexity of oscillations observed for a constant inﬂow amplitude
A = 0.12 (thus A > A1/2 but A < A1 ) as a function of ﬂow frequency is
illustrated in Fig. 2. As discussed above, for the selected amplitude and a
low frequency of inﬂow oscillations, the system dynamics follow the time-
dependent stationary state and oscillations of y(t) extend over both stable
branches of the h(x, y) = 0 nullcline. For intermediate frequencies, oscilla-
tions accumulate on the upper stable branch of the nullcline and the min-
imum value of y(t) increases with frequency. Then, at a certain frequency
fc ( for the selected amplitude of oscillations, fc ≈0.0312 ), the oscillations
switch from the upper to the lower stable branch of the h(x, y) = 0 nullcline.
The transition between oscillations located on diﬀerent stable branches is
7


## Page 8


quite pronounced and should be easily detected in experiments with a sys-
tem exhibiting hysteresis. Therefore, it becomes apparent that a cooperative
system can discriminate the frequency of a perturbation if its amplitude
remains ﬁxed. Numerical simulations have also demonstrated that the fre-
quency of the transition between oscillations on the USB and LSB depends
on the phase φ0. The right upper corner of Fig. 2 shows two types of oscil-
lations that are observed for f = 0.031. If φ0 = 0, the system oscillates at
the upper stable branch, but if φ0 = 3π
2 , oscillations around the lower stable
branch are seen. Fortunately for the application of this approach to discrim-
ination, the interval of frequencies within which phase-dependent evolution
is observed is very narrow. For A = 0.12, it is [0.0306, 0.0312]. The width of
this interval (∆f ∼0.0006) deﬁnes the precision in frequency discrimination.
The dynamical system considered here can also be used to discriminate
the amplitude of an applied perturbation. Figure 3 shows the time evolu-
tion of y(t) for a few values of perturbation amplitude A and a ﬁxed inﬂow
frequency (f = 0.05). As expected, for small amplitudes (A ≤0.1122) the
oscillations of y(t) are limited to the LSB. For larger amplitudes (0.1122 <
A < 0.1361), the range of observed values of y(t) increases, but the oscilla-
tions are still anchored on the LSB. Finally, if 0.13617 ≤A, the oscillations
move onto the USB. The transition between the diﬀerent types of oscillation
is quite pronounced and can be used to discriminate the value of amplitude.
Here, similar to the cases illustrated in Fig. 2, we observe a narrow interval
of amplitudes ( ∆A ∼0.0001) within which the type of oscillation depends
on the initial phase.
8


## Page 9


0
 0.4
 0.8
 0
 0.5
 1
 1.5
 2
x1
y1
x2
y2
-A2
-A1
y
x
α = 0.55, ε = 1
Figure 1:
Positions of nullclines for the dynamical system deﬁned by
Eqs.(2,3).
The model parameters are:
ε = 1, α = 0.55, f = 0 and
φ0 = 0.
The nullcline h(x, y) = 0 is plotted with a solid line.
The
nullcline g(x, y, t) = 0 is shown for a few cases: A = 0 ( dotted line),
A = A2 = 0.02603 ( short-dashed line), A = A1 = 0.16445 ( long-dashed
line). For the selected parameters of the model, the variables at tangential
points are (x1, y1) = (0.47368, 0.09607) and (x2, y2) = (1.23531, 0.65339)
9


## Page 10


( II ) - ( I ) transition 
dependent on     
 0
 0.2
 0.4
 0.6
 0.8
 1
 0
 300
 600
t
f = 0.007
y
 0
 250
 500
t
f = 0.010
 0
 150
 300
t
f = 0.020
 0
 100
 200
t
f = 0.032
 0
 100
 200
t
f = 0.031
φ0 = 3 π/2
 0
 100
 200
t
0
f = 0.031
φ = 0
 0
 50
 100
t
f = 0.061
f
φ
0
( III )
Full Amp.
( II )-2
( II )-1
USB
( I )-1
LSB
( I )-2
0.0071
0.0120
0.0306
0.0312
0.0602
Figure 2: Time evolution of the dynamical system described by Eqs.(2,3) as a
function of the inﬂow frequency f for a ﬁxed amplitude A = 0.12. The model
parameters are: ε = 1, α = 0.55. Tics and numbers on the frequency scale
mark transitions between diﬀerent types of oscillation.
The initial phase
is φ0 = 3π/2 for all cases except the central one, for which φ0 = 0. The
horizontal green lines mark the values of y1 and y2.
10


## Page 11


Figure 3: Time evolution of the dynamical system described by Eqs.(2,3) as
a function of the inﬂow amplitude A for a ﬁxed frequency f = 0.05. Tics
and numbers on the frequency scale mark transitions between diﬀerent types
of oscillation. The initial phase is φ0 = 3π/2 for all cases except at the top
in the right column, for which φ0 = 0. The horizontal dashed lines mark the
values of y1 and y2.
11


## Page 12


To give a more precise description of system evolution, let us introduce a
classiﬁcation of oscillations based on the minimum and maximum values of
y(t) observed over a long time interval for which the evolution has reached a
stationary state. We deﬁne:
ymin = mint∈[tmin,tmax] y(t)
(4)
and
ymax = maxt∈[tmin,tmax] y(t)
(5)
Initially, we used tmin = 1000, where tmax = tmin + 1000. Next we repeated
the calculations for tmin = 2000. If there is a signiﬁcant discrepancy in ymin,
ymax obtained for these time intervals, then the procedure is repeated with
tmin increased by an additional 1000 time units until agreement is attained.
The type of oscillation is classiﬁed through the comparison of ymin and
ymax with the values of y1 and y2, as illustrated in Fig. 4. The classiﬁcation
of oscillations is summarized in Table I.
Table I
oscillation class
condition
(I)-1 LSB
ymin ≤ymax < y1 (oscillations limited to LSB)
(I)-2
ymin < y1, y1 ≤ymax < y2
(III)
ymin < y1, ymax ≥y2
(II)-2
y1 ≤ymin < y2, ymax ≥y2
(II)-1 USB
ymax ≥ymin > y2 (oscillations limited to USB)
(IV)
y1 ≤ymin < y2, y1 ≤ymax < y2
12


## Page 13


As shown in Fig.
4, the transitions between oscillation types (I) −
1LSB ↔(I)−2 and (I)−2 ↔(III) are continuous because they result from
an increase or decrease in the ymax value. Similarly, the transitions between
oscillation types (III) ↔(II) −2 and (II) −2 ↔(II) −1USB are conti-
nous because they are related to an increase or decrease in the ymin value.
In actual experiments, these transitions are diﬃcult to detect because they
require highly accurate data acquisition. On the other hand, the transition
(I) −2 ↔(II) −1USB, on which the discrimination is based, can be easily
detected because it is related to a discontinuous jump between ymax < y2
and ymin > y2.
13


## Page 14


( I )-1
LSB
( I )-2
( III )
( II )-2
( II )-1
USB
( IV )
y1
y1
y2
y2
ymax
ymin
Figure 4: Geometrical illustration of types of oscillation in the classiﬁcation
based on ymin and ymax.
The dotted lines mark y1 = 0.09607 and y2 =
0.65338.
14


## Page 15


Figure 5 illustrates the regions of parameters (f, A) for which a given os-
cillation pattern is observed in a model characterized by α = 0.55 and ε = 1.
The thick line separates the region of the phase space (f, A) in which class
(I)-2 oscillations are observed, from the region where class (II)-1 USB oscilla-
tions appear. Let us denote points on this line as (fc, Ac). The amplitude Ac,
when treated as a function of fc, is a continuous, monotonically increasing
function Ac = G(fc). Therefore, the inverse function fc = G−1(Ac) exists.
Our discrimination method is based on the determination of conditions in
which a small change in fc or Ac qualitatively changes the character of the
time evolution to force a transition between (I) −2 and (II) −1USB type
oscillations. Let us assume that we want to measure the unknown inﬂow
frequency and that we can regulate the inﬂow amplitude.
The following
procedure can be applied. Initially, we set a low amplitude so the system
oscillates on the LSB (type (II) −1 oscillations). Next, the amplitude is
increased up to the moment Az when oscillations of type (II) −1USB are
detected. The frequency of inﬂow fz can be estimated as fz = G−1(Az). This
method works for all frequencies greater than f0, which corresponds to the
tip of the (II) −1USB region ((f0, A0)). The accuracy of the estimation
depends on the frequency and is high where the amplitude Ac is a rapidly
increasing function of fc, here for 0.02 ≤fc ≤0.1. This system can also be
used to determine the amplitude of inﬂow when we can control the frequency.
Now we set a low frequency and the system exhibits type (III) oscillations.
Next, the frequency is increased up to the moment fy when oscillations of
type (I) −2 are detected. The amplitude of the inﬂow Ay is Ay = G(fy).
Unlike for frequency, the range of discriminated amplitudes does not extend
15


## Page 16


outside the interval [A0, A1].
The phase diagrams, similar to that in Fig. 5 but for ε = 1/5 and ε = 5,
are shown in Fig. 6 and Fig. 7 respectively. The results are qualitatively
identical to those in Fig. 5, suggesting that the described changes in the
system oscillations are generic and should also apply to other systems with
hysteresis inﬂuenced by a periodic perturbation.
16


## Page 17


A
f
 0.07
 0.08
 0.09
 0.1
 0.11
 0.12
 0.13
 0.14
 0.15
 0.16
 0.17
 0.18
 0
 0.05
 0.1
 0.15
 0.2
( III ) ( II )-2
( II )-1
USB
( I )-1
LSB
( I )-2
 A1
 A1/2
Figure 5: Phase diagram showing the type of oscillation as a function of
inﬂow parameters (f, A). The horizontal lines indicate A1 = 0.16445 and
A1/2. The model parameters are ε = 1 and α = 0.55
. The thick solid line marks the boundary between oscillation classes (I) −
2 and (II) −1USB. The transition between these oscillations is used to
determine the parameters of inﬂow.
17


## Page 18


0.07
 0.08
 0.09
 0.1
 0.11
 0.12
 0.13
 0.14
 0.15
 0.16
 0.17
 0.18
 0
 0.05
 0.1
 0.15
 0.2
A
f
Classification
class 3,3-4
class 1,1-2
( III ) ( II )-2
( II )-1
USB
( I )-1
LSB
( I )-2
 A1
 A1/2
Figure 6: Phase diagram showing the type of oscillation as a function of
inﬂow parameters (f, A). The horizontal lines indicate A1 = 0.16445 and
A1/2 . The model parameters are ε = 1/5 and α = 0.55
.
18


## Page 19


Figure 7: Phase diagram showing the type of oscillation as a function of
inﬂow parameters (f, A). The horizontal lines indicate A1 = 0.16445 and
A1/2 . The model parameters are ε = 5 and α = 0.55
.
19


## Page 20


3
Conclusions
We have described how the time evolution of a cooperative system is de-
pendent on the frequency and amplitude of a periodic stimulus. There is a
narrow range of these parameters within which the characteristics of this evo-
lution change in a qualitative manner: oscillations around one stable branch
change into oscillations on another branch. This phenomenon can be used to
determine the amplitude or frequency of an applied perturbation. As for the
numerical framework, we evaluated the eﬀect of the rhythmicity of substrate
input in a model biochemical system with sigmoidal kinetics, i.e. n = 3 in
the Hill equation. Using numerical simulations, we separated the phase space
of inﬂow parameters (amplitude and frequency) into regions where speciﬁc
types of oscillation are observed. The boundary line separating oscillations
with signiﬁcantly diﬀerent behaviors (type (I) −2 and type (II) −1USB
oscillations) was identiﬁed. The frequency that causes a transition appears
in a monotonic function of the inﬂow amplitude. The system can be used
to determine the inﬂow frequency if we can control the inﬂow amplitude. It
can also be used to determine the inﬂow amplitude when we can control the
frequency. In other words, sigmoidal kinetics with the Hill equation can act
as an inﬂow discriminator.
This paper describes a system in which the nonlinear term in the kinetic
equation for the y(t) variable is described by
x3
1+x3 term (cf. Eq.(3)) and the
periodic inﬂow is described by a trigonometric function. We believe that
these results are general, and qualitatively similar behavior can be expected
in other systems with cooperative characteristics. We performed numerical
simulations for a model based on Eqs.( 2,3) but with the inﬂow term in the
20


## Page 21


form J(t) = A · (tanh (γ · sin(2πft + φ0)) + 1) · Θ(t) for diﬀerent values of
γ. Such periodic inﬂow becomes a square-like wave for large γ. The phase
diagrams that illustrate the type of oscillation as a function of f and A
are qualitatively the same, as presented in Figs. (5-7). We also considered
other nonlinear terms in the kinetic equation for y(t), like tanh (x −x0) or
1/(1 + exp (−δ · (x −x0)), and obtained similar results. Therefore, we be-
lieve that real systems of chemical reactions with hysteresis can be used as
discriminators in the manner described above.
The present results can be regarded as a solution to the problem of the
optimum stabilization of a system in an unstable state. Let us assume that
Eqs.( 2,3) describe the time-dependent progress of a medical treatment where
the variable y(t) represents the condition of a patient.
The variable x(t)
describes the time-dependent concentration of the curing drug. The states on
the LSB and USB correspond to an ill and healthy patient, respectively. This
simple model seems to realistically describe the basic features of drug therapy.
It predicts that if the inﬂow of the drug is small, then the patient remains
ill. Only a dose higher than a critical dose allows for successful treatment.
However, some drugs are toxic ( such as those used in chemotherapy) and the
total dose should be as small as possible. An analysis of the dynamical system
presented in Fig. 5 can provide a solution: if we consider the periodic inﬂow
of a drug in the form of Eq.(1), then the minimum amount of drug required
to stabilize the patient in a healthy state corresponds to the bottom corner
of the type (II) −1USB oscillation region - here A0 ∼= 0.1 and f0 ∼= 0.015.
21


## Page 22


4
Acknowledgement
This work was supported by KAKENHI Grants-in-Aid for Scientiﬁc Research
(15H02121, 25103012).
22


## Page 23


References
[1] J.D. Murray, Mathematical Biology. I. An Introduction , 3rd ed,
(Springer-Verlag, Berlin Heidelberg, 2002).
[2] M.A. Krasnoselsky, A.W. Pokrowsky, Sistemy s gisteresisom (Systems
with Hysteresis, in Russian), (Nauka, Moscov, 1983).
[3] K. Yoshikawa and N. Yoshinaga, Novel scenario of the folding transition
of a single chain. J. Phys. Cond. Matt., 17, S2817 (2005).
[4] M. I. Stefan and N. Le Nov`ere, S. Wodak, ed. Cooperative Binding. PLoS
Comput. Biol. 9, e1003106. (2013).
[5] K. Tsumoto, F. Luckel, and K. Yoshikawa, Giant DNA molecules ex-
hibit on/oﬀswitching of transcriptional activity through conformational
transition. Biophys. Chem. (2003).
[6] A.L. Kawczy´nski, Nonlinear resonances, quasiperiodicity and chaos in
a periodically perturbed oscillatory chemical system with inﬁnite number
of bifurcations, Pol. J. Chem. 69, 296-307 (1995).
[7] A.L. Kawczy´nski and K. Bar-Eli, Periodic perturbations and 3-branch
return maps of an oscillatory chemical system, J. Phys. Chem. 99, 16636-
16640 (1995).
[8] A.L. Kawczy´nski, Periodic perturbations of chaotic dynamics induce or-
der, Pol.J.Chem., 70, 643-655 (1996).
23


## Page 24


[9] Hill, A. V. The possible eﬀects of the aggregation of the molecules of
haemoglobin on its dissociation curves. J. Physiol. (Lond.), 40, iv-vii.
(1910).
[10] S. Goutelle, M. Maurin, F. Rougier, X. Barbaut, L. Bourguignon, M.
Ducher, and P. Maire, The Hill equation: a review of its capabilities in
pharmacological modelling. Fundam. Clin. Pharmacol. 22, 633 (2008).
[11] J. Keener and J. Sneyd, Mathematical Physiology II: Systems Physiology
p. 974 (Springer, 2009).
[12] J.J. Tyson, Biochemical oscillations. In: C.P. Fall, E.S Marland, J. M.
Wagner, J.J. Tyson, eds., Comput. Cell. Biol. 230-60. ( Springer-Verlag,
2001).
[13] R. Heinrich, S.M. Rapoport, and T.A. Rapoport, Prog. Biophys. Molec.
Biol. 32, 1-82 (Pergamon Press, 1978).
[14] J. Vera, O. Rath, E. Balsa-Canto, J.R. Banga, W. Kolch, and O. Wolken-
hauer, Investigating dynamics of inhibitory and feedback loops in ERK
signalling using power-law models. Mol. BioSyst. 6, 2174 (2010).
[15] R. Blossey, J.-F. Bodart, A. Devys, T. Goudon, and P. Laﬁtte, Signal
propagation of the MAPK cascade in Xenopus oocytes: role of bistability
and ultrasensitivity for a mixed problem. J. Math. Biol. 64, 1-39 (2011).
[16] L. Qiao, R.B. Nachbar, I.G. Kevrekidis, and S.Y. Shvartsman, Bistability
and oscillations in the Huang-Ferrell model of MAPK signaling. PLoS
Comput. Biol. 3, 1819 (2007).
24


## Page 25


[17] M. Zumsande and T. Gross, Bifurcations and chaos in the MAPK sig-
naling cascade. J. Theor. Biol. 265, 481-491 (2010).
[18] T. Tsuruyama, T. Nakamura, G. Jin, M. Ozeki, Y. Yamada, and H.
Hiai,Constitutive activation of Stat5a by retrovirus integration in early
pre-B lymphomas of SL/Kh strain mice. Proc. Natl. Acad. Sci. 99, 8253-
8258 (2002).
[19] T. Tsuruyama, A model of cell biological signaling predicts a phase tran-
sition of signaling and provides mathematical formulae. PLoS One 9,
e102911 (2014).
25

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1912.10468v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1912.10468v1_A_biology-inspired_approach_to_the_positive_integral_control_of_positive_systems

> Source: 1912.10468v1_A_biology-inspired_approach_to_the_positive_integral_control_of_positive_systems.pdf

> Pages: 52

---


## Page 1


A biology-inspired approach to the positive integral
control of positive systems - the antithetic, exponential,
and logistic integral controllers
Corentin Briat∗
Abstract
The integral control of positive systems using nonnegative control input is an im-
portant problem arising, among others, in biochemistry, epidemiology and ecology. An
immediate solution is to use an ON-OFF nonlinearity between the controller and the
system. However, this solution is only available when controllers are implemented in
computer systems. When this is not the case, like in biology, alternative approaches
need to be explored. Based on recent research in the control of biological systems [7,14],
we propose to develop a theory for the integral control of positive systems using non-
negative controls based on the so-called antithetic integral controller and two positively
regularized integral controllers, the so-called exponential integral controller and logistic
integral controller. For all these controllers, we establish several qualitative results,
which we connect to standard results on integral control. We also obtain additional
results which are speciﬁc to the type of controllers. For instance, we show an inter-
esting result stipulating that if the gain of the antithetic integral controller is suitably
chosen, then the local stability of the equilibrium point of the closed-loop system does
not depend on the choice for the coupling parameter, an additional parameter speciﬁc
to this controller. Conversely, we also show that if the coupling parameter is suitably
chosen, then the equilibrium point of the closed-loop system is locally stable regardless
the value of the gain. For the exponential integral controller, we can show that the
local stability of the equilibrium point of the closed-loop system is independent of the
gain of the controller and the gain of the system. The stability only depends on the
exponential rate of the controller, again a parameter that is speciﬁc to this type of
controllers. Several examples are given for illustration.
Keywords. Positive systems; positive control; antithetic integral controller; regularized
integral control; control of biological systems; Cybergenetics
∗NCIS, Switzerland (corentin@briat.info, www.briat.info).
1
arXiv:1912.10468v1  [math.OC]  22 Dec 2019


## Page 2


1
Introduction
Integral control is undoubtedly a cornerstone of control theory as it allows for the tracking
of constant reference signals while being able to reject constant disturbances, an impressive
feat despite to its very simple structure. It is, therefore, not surprising to ﬁnd this structure
in many control algorithms for industrial processes in the so-called Proportional-Integral-
Derivative (PID) controllers [1]. Interestingly, integral control is not only of engineering
interest but has also been shown to arise in living organisms such as in bacteria [7, 57] or
mammals [24]. Synthetic genetic regulation circuits have also recently attracted a lot of
interest in the nascent ﬁeld of Cybergenetics, the ﬁeld pertaining on the modeling, analysis
and control of biological processes using in-silico and in vivo controllers; see e.g. [7,9–11,14,
16,19–21,41,58].
We propose to consider in this paper the integral control of positive systems with the
constraint that the control input be nonnegative. Positive systems [25] are an important
class of dynamical systems whose state is conﬁned in the nonnegative orthant. Such systems
have been considered for the modeling of a wide variety of real world processes such as the
modeling of populations [38], physiological systems [33], biochemical systems [7,9,10,14,30],
communication networks [13, 52], etc. The control/controllability/reachability of systems
with positive inputs have been well studied; see e.g. [18, 23, 32, 37, 49] and the references
therein. The nonnegative proportional-integral control of linear positive systems have been
studied in [9, 10, 12] in the context of the control of the moments equation in biochemical
reaction networks. The idea is to place between the controller and the system an ON/OFF
static nonlinearity [27] which zeroes the control input when it is negative.
This makes
the global stability/stabilization problem addressable in the linear system setting using, for
instance, the Popov criterion [9,10,12,29,46] or surface Lyapunov functions [27]. However,
the cases of nonlinear systems or stochastic systems are way more involved and there seems
to be no clear way on how to address this problem in a fairly general setting.
To palliate this, we propose to use two alternative approaches. The ﬁrst one is based on
the use of the antithetic integral controller recently introduced in [7] in the context of the
in vivo control of single-cells and cell populations; see also [2] for an experimental validation
of the approach. This controller has the beneﬁt to implement an integral action and to
naturally produce a nonnegative control input without the use of any additional static non-
linearity. The price to pay, however, is its nonlinear behavior (yet polynomial of order two)
and its higher dimensionality (dimension two). However, its polynomial structure makes it
interesting for then controlling polynomial/rational nonlinear systems since it makes it pos-
sible to use numerical methods such as the use of polynomial Lyapunov functions combined
with optimization tools such as sum of squares programming [44,45]. This particular integral
control structure works in both the deterministic and the stochastic settings. In fact, the
antithetic integral controller is the simplest integral controller that is able to properly work
in a stochastic setting. The performance analysis of the antithetic integral controller and its
generalizations have also been theoretically studied in [17,42,43,47] in a deterministic and
stochastic settings. In those papers, the stability and robustness properties of the antithetic
integral controller is studied in various parametric regimes for both the controller and sys-
2


## Page 3


tem parameters, notably in the presence of degrading controller species. In particular, [17]
focuses on the extension of those ideas to PID control.
We show, in the linear systems case, that provided the system matrix is Hurwitz stable
, we can always ﬁnd an antithetic integral controller that makes the desired equilibrium
point locally exponentially stable. Compared to the standard integral controller for which
only the gain k needs to be tuned so that the closed-loop system is (locally) asymptoti-
cally/exponentially stable, the antithetic integral controller has an extra degree of freedom
η, which we refer here to as the coupling parameter. We show, again in the case of linear sys-
tems, that when the gain k of the integral controller lies within some interval whose bounds
can be exactly characterized and accurately computed, then the closed-loop system is (lo-
cally) asymptotically/exponentially stable regardless the choice for the coupling parameter
η. This result complements existing ones [8,42,43,47] where the strong coupling, or strong
binding, assumption (i.e. inﬁnite coupling parameter) was used as a simplifying procedure to
obtain simpler stability conditions, explicit expressions for the variance in stochastic systems
or as a mean to recover disturbance rejection properties when the controller state is subject
to exponential decay. However, even if in biological systems binding constants can be large,
they remain ﬁnite and it is unclear whether we can extrapolate those results to the ﬁnite
coupling parameter case with no proper mathematical ground. We show here that, in fact,
we can extrapolate those results as long as stability is concerned since the strong binding
regime is the most restrictive one in the sense that if the equilibrium system is stable when
the coupling parameter is inﬁnite then it is necessarily stable when the coupling parameter
remains ﬁnite. Still in the case of linear systems, a dual result establishing an interval of
values for η for which the closed-loop system is (locally) asymptotically/exponentially stable
regardless the choice for the gain k. All those results naturally extend to certain classes of
nonlinear systems having a unique locally exponentially stable hyperbolic equilibrium point
corresponding to possible output values. Note that in this case the linearized system may
not be positive which is not a problem since the Metzler structure of the system matrix is
not used in any of the proof. In this regard, the obtained results therefore readily apply
to the broader class of externally positive systems. Examples considering nonlinear systems
coming from biochemistry and epidemiology are provided for illustration.
The second approach is based on the use of regularizing functions, a novel ﬂexible con-
cept, allowing to impose certain properties to a controller such as the nonnegativity or the
saturation of the control input. Regularizing functions are deﬁned as diﬀerentiable invertible
strictly increasing functions from R to some connected interval of R. When the image set
is a connected interval of the nonnegative orthant, the regularizing function is said to be a
positively regularizing function. When placed between the controller and the system, a posi-
tively regularizing function will make the control input nonnegative as the ON-OFF function
would also do. However, the invertibility and diﬀerentiability of regularizing functions makes
it possible to obtain a dynamical model for the controller and the regularizing function all to-
gether. Interestingly, when the regularizing function is chosen to be the exponential function
or the logistic function, then the corresponding dynamical model is of polynomial form. This
is a clear advantage over the use of an ON-OFF nonlinearity for the same reasons as for the
3


## Page 4


antithetic integral control as it makes possible to consider those controllers in the nonlinear
setting. It is worth mentioning that the exponential integral controller is not new and has
been studied in the past, for instance, in [14,22,26,34,53]. In particular, [53] studied its role
in fold-change detection whereas [26] focused on the controller ability to reject non-constant
disturbances. In the present paper, we observe for the ﬁrst time that this controller can be
obtained using positively regularizing functions and we mainly focus on its stability prop-
erties and on the characterization of the diﬀerent classes of systems that can be controlled
using such a controller motif. On the other hand, the logistic controller does not seem to have
been studied in the past. These two controllers are expected to fail in the stochastic setting
because of the presence of an absorbing state located at zero. In the deterministic case,
however, the equilibrium point is shown to be structurally unstable. Analogous results to
the antithetic integral controller are then obtained and illustrated through several examples.
In particular, the exponential controller is shown to possess an intrinsic robustness property
with respect to the gain at zero frequency of the system. The logistic integral controller does
not enjoy such a property because of the presence of the saturation.
Outline.
The paper is structured as follows.
Positive integration and positive integral
control are introduced in Section 2. The control of positive linear systems using antithetic
integral control is addressed in Section 3 whereas the case of nonlinear positive systems
is considered in Section 4. The theory pertaining on the exponential and logistic integral
controllers is developed in Section 5 and Section 6, respectively. A concluding discussion is
given in Section 7.
2
Positive integration
We introduce in this section the concept of positive integration as well several positive
integration structures.
2.1
Antithetic integration
The antithetic integrator [7,41] is deﬁned as
˙z1(t)
=
w1(t) −ηz1(t)z2(t)
˙z2(t)
=
w2(t) −ηz1(t)z2(t)
z(0)
=
z0
(1)
where z := (z1, z2) ∈R2
≥0 is the state of the integrator, w1, w2 : R≥0 →R≥0 are the inputs,
z0 ∈R2
≥0 is the initial condition and η > 0 is the coupling parameter. It is immediate to
see that the state remains nonnegative whenever the initial condition and the inputs are
nonnegative as well. Note also that this integrator has two states and two inputs, which is
a clear diﬀerence with the standard integrator. However, it is possible to reconcile them by
virtue of the following result:
4


## Page 5


Proposition 1 The signal ˜z := z1 −z2 has dynamics
˙˜z(t) = ˜w(t), ˜z(0) = z1(0) −z2(0).
(2)
and, hence, the system (1) is an implementation of the integration operator acting on the
input ˜w := w1 −w2.
This results demonstrates that even though the two inputs are nonnegative, the integrator
integrates their diﬀerence, which can be negative. An interpretation of the antithetic integra-
tor is that z1 and z2 contain the positive and the negative part of ˜z, respectively. However,
this is not purely the positive and negative parts since they are usually both nonzero.
2.2
Regularized integration
Before deﬁning what is regularized integration, it is necessary to deﬁne the concept of regu-
larizing function:
Deﬁnition 2 We say that ϕ : R →R is a regularizing function if it is
• continuously diﬀerentiable a.e., and
• monotonically increasing, i.e. ϕ′ > 0 a.e.
If, moreover, it is nonnegative, then it is called a positively regularizing function.
The idea behind the use of regularizing functions to be combined with a standard integrator
to change its properties. The deﬁnition above imposes some strong properties which are
useful in the current paper and when we have applications in biology in mind. However,
it is possible to drop the diﬀerentiability or the strict monotonicity assumptions so that
ON-OFF nonlinearities of the form max{0, ·} or saturation functions can be considered. In
the current paper, we rely on the invertibility property of regularizing functions in order to
obtain a dynamical model for the combination of the regularized integration operator. This
leads to the following result:
Proposition 3 The dynamics of the regularized integrator ˙I = w, v := ϕ(I), for some
regularizing function ϕ and input signal w, is given by
˙v(t) = ϕ′(ϕ−1(v(t)))w(t), v(0) = v0
(3)
Proof :
The proof follows from the standard diﬀerentiation rules and the fact that the
inverse of ϕ exists according to the deﬁnition of regularizing functions.
♦
Deriving the model for entire regularized integral controller is interesting for various reasons.
First of all, it removes the regularizing function from the loop by embedding it in the model
of the integrator. Another interesting fact is that this new expression for the regularized in-
tegrator emphasizes connections with existing models in biochemistry, notably in the glucose
regulation system [34] for a certain choice for the regularizing function. Such integrators are
5


## Page 6


notably also called constrained integrators in [56] but their correspondence with regularizing
functions has never been pointed so far.
In Table 1, several correspondences between (positively) regularizing functions and the
dynamical model for v are provided. Interestingly, we can see that exponential-based reg-
ularizing functions lead to polynomial dynamical models for v, an essential property when
such controllers need to be implemented in living organisms. The hyperbolic, arctangent
and algebraic regularizing functions, even if not considered any further in this paper, may
ﬁnd applications in the control of nonlinear systems subject to input saturations. Indeed,
substituting the static saturation function by a regularizing function could allow for a more
systematic analysis of the closed-loop dynamics. Note also, that these regularizing functions
can be made positively regularizing by simply adding a constant term to their expression.
Table 1: Some (positively) regularizing functions and the associated regularized integration
models
ϕ(x), α, β, θ > 0
˙v for v = ϕ(I)
Exponential
eαx
αvw
Logistic
β
e−αx + 1
α
β v(β −v)w
Generalized Logistic
β
(e−αx + 1)θ
αθ
β1/θ v(β1/θ −v)w
Hyperbolic
β tanh(αx)
α

1 −v2
β2

w
Arctangent
β arctan(αx)
αβ
1 + tan (v/β)2w
Algebraic
βαx
(1 + α2x2)1/2
α
β2(β2 −v2)3/2w
3
Antithetic integral control of linear internally posi-
tive systems
The objective of this section is to provide a thorough analysis of the antithetic integral
controller and its application to the integral control of linear positive systems. First, linear
positive systems are brieﬂy recalled in Section 3.1 with some of their properties. The control
problem and its solution based on the use of an antithetic integral controller are deﬁned
in Section 3.2. Local stability results are obtained in Section 3.3, Section 3.4 and Section
3.5. The perfect adaptation properties of the controller are discussed in Section 3.6 and the
section concludes on an example inspired from biochemistry in Section 3.7.
6


## Page 7


3.1
Linear positive systems
Let us consider the linear system
˙x(t)
=
Ax(t) + Bu(t), x(0) = x0
y(t)
=
Cx(t)
(4)
where x ∈Rn is the state of the system, u ∈R is the control input and y ∈R is the measured
output that has to be controlled. The matrices A ∈Rn×n, B ∈Rn×1 and C ∈R1×n are the
state matrix, the input matrix and the output matrix, respectively. Since we are interested
in the control of linear internally positive systems, we need a way to identify this type of
systems. The following result gives a complete characterization of linear internally positive
systems [25]:
Proposition 4 The following statements are equivalent:
(a) The system (4) is internally positive; i.e. for any x0, w(t) ≥0 for all t ≥0, we have
that x(t), y(t) ≥0 for all t ≥0.
(b) The matrix A is Metzler (i.e. all the oﬀ-diagonal entries are nonnegative), the ma-
trices B and C are nonnegative (i.e. all the entries are nonnegative).
A consequence of this result is that the impulse response of an internally positive system is
nonnegative. However, there may exist systems which are not internally positive having a
nonnegative impulse response. Those systems are called externally positive systems and only
require the output to be nonnegative for any nonnegative input and zero initial conditions
[25].
We also make the following assumption:
Assumption 5 The matrix A is Hurwitz stable and CA−1B ̸= 0.
The assumption of asymptotic stability is motivated by the fact that the integral action
usually has a destabilizing eﬀect on the dynamics of the system. It is still possible to control
systems for which this assumption is not met under additional conditions on the poles and
zeros of the transfer function associated with the system. This will be treated in a diﬀerent
article. The second assumption simply states that the DC-gain of the system is nonzero.
One implication of this assumption is that of the output controllability of (4):
Proposition 6 Assume that the system (4) is internally positive and that Assumption 5
holds. Then, the system (4) is output-controllable1 and we have that CA−1B < 0.
Proof : For the system (4) to be output controllable, it suﬃces that the impulse response be
non-identically 0. This is equivalent to saying that its transfer function G be non-identically
zero as well. Since the system is internally positive and A is Hurwitz stable, then we have
that ||G||H∞= supw∈R |G(jω)| = |G(0)| = |CA−1B| ̸= 0, by assumption. The fact that
1The system (4) is output-controllable if rank

CB
CAB
. . .
CAn−1B

= 1; see e.g. [40].
7


## Page 8


the frequency response has maximum modulus at the zero frequency comes from the fact
that the system is internally positive and stable; see e.g. [6]. Hence, the system is output-
controllable. Finally, since the matrix A is Metzler and Hurwitz stable then its inverse is
nonpositive [4]. Hence, CA−1B < 0, since CA−1B ̸= 0. The proof is completed.
♦
3.2
The control problem and the antithetic integral controller
We consider in this section the following control problem:
Problem 7 Let the reference µ > 0 be given and assume that the system (4) is internally
positive and satisﬁes the assumptions in Assumption 5. Find an integral controller such that
(a) the control input u is nonnegative at all times;
(b) the equilibrium point of interest of the closed-loop system consisting of the system (4)
and the controller is (locally) asymptotically stable;
(c) the output y asymptotically tracks the reference µ > 0; i.e. y(t) →µ as t →∞;
(d) the closed-loop system locally rejects constant disturbances acting on the input and on
the state of the system.
This problem and its variations have been addressed in the past using various approaches. A
thoroughly considered approach relies on the use of an ON-OFF nonlinearity placed between
the controller and the system; [9,10,12,29]. The main issue is that an ON-OFF integrator
cannot be readily implemented in terms of chemical reactions and, hence, cannot be im-
plemented inside biological organisms. Another drawback of ON-OFF nonlinearities is the
diﬃculty of considering them for the control of nonlinear systems. On the other hand, the
antithetic integral controller deﬁned as
˙z1(t)
=
µ −kηz1(t)z2(t)
˙z2(t)
=
y(t) −kηz1(t)z2(t)
u(t)
=
kz1(t)
z(0)
=
z0 ≥0,
(5)
where k > 0 is the gain of the controller and η > 0 is the coupling parameter, can be
theoretically implemented in terms of chemical reactions. This controller was ﬁrst proposed
in [7] for the integral control of biological networks using in vivo controllers. Using the
implementation ideas proposed in [7], this controller has been implemented in vivo and con-
vincing experimental results were obtained and reported in [2]. Even though we are not
considering such implementation constraints here, the above controller has the beneﬁt of
being polynomial. In this regard, this controller may be interesting to consider when con-
trolling polynomial or rational systems as it would allow for the use of modern optimization
methods such as sum of squares programming [45]. Note that the ON-OFF nonlinearity can
8


## Page 9


be considered in the linear setting using Popov’s criterion but the nonlinear setting is way
more involved and there is no clear way on how to do so. A last remark is that the model
is slightly diﬀerent than the one [7] where the term η is considered instead of kη for the
polynomial term in the model. The underlying reason is purely technical and allows one
to simplify the derivation of the results. The simple change of variables η ←kη allows to
retrieve the controller considered in [7] and to adapt the results of this paper to the controller
in [7].
The following result shows that the closed-loop system has only one equilibrium imposed
by the antithetic integral controller:
Proposition 8 Let k, η, µ be given. Then, the equilibrium point of the closed-loop system
(4)-(5) is unique and is given by
x∗= µ A−1B
CA−1B , z∗
1 =
−µ
CA−1Bk and z∗
2 = −CA−1B
η
.
(6)
The equilibrium point of the closed-loop system for some given µ, η, k > 0 is denoted by
X ∗
µ,η,k := {(x∗, z∗) deﬁned in (6)} .
(7)
3.3
Controller existence - a non-constructive result
The following result proves the existence of an antithetic integral controller that solves the
Problem 7:
Theorem 9 (Local stabilization) Assume that the system (4) is internally positive and
that it satisﬁes Assumption 5. Then, the following statements hold for the closed-loop system
(4)-(5):
(a) for any given µ, η > 0, there exists a ¯k = ¯k(µ, η) > 0 such that for any k ∈(0, ¯k), the
equilibrium point X ∗
µ,η,k is locally asymptotically stable;
(b) there exists a ¯k > 0 such that, for any k ∈(0, ¯k), all the equilibrium points in X ∗
µ,η,k
for all η, µ > 0 are locally asymptotically stable.
Proof :
Proof of statement (a).
Let µ, η > 0 be given.
The proof is based on a
perturbation argument on the closed-loop system. The Jacobian linearization of the system
about the equilibrium point (6) is given by


˙˜x(t)
˙˜z1(t)
˙˜z2(t)

=


A
Bk
0
0
CA−1Bk
ηµ
CA−1B
C
CA−1Bk
ηµ
CA−1B


|
{z
}
˜A(k)


˜x(t)
˜z1(t)
˜z2(t)


(8)
9


## Page 10


where ˜x = x −x∗, ˜z1 = z1 −z∗
1 and ˜z2 = z2 −z∗
2. The above matrix ˜A(k) can be decomposed
as ˜A0 + ˜A1k where
˜A0 =


A
0
0
0
0
ηµ
CA−1B
C
0
ηµ
CA−1B


and
˜A1 =


0
B
0
0
CA−1B
0
0
CA−1B
0

.
(9)
The aﬃne dependency on k is a consequence of the choice for the coeﬃcient of the second-
order term in (5). Indeed, if η would have been considered instead of kη, we would have
obtained a dependence on k and 1/k, which would have complicated the analysis when k is
close to zero. It is immediate to see that the spectrum of ˜A0, σ( ˜A0), is simply given by
σ( ˜A0) = σ(A) ∪
n
0,
ηµ
CA−1B
o
.
(10)
Since CA−1B < 0, then ˜A0 is marginally stable with a simple eigenvalue located at 0. The
key idea is to show, via a perturbation argument, that the matrix ˜A0 + ε ˜A1 can be made
Hurwitz for some suﬃciently small ε > 0. In other words, the 0-eigenvalue of A0 must shift
to the open left half-plane whenever ˜A0 is slightly perturbed in the direction ˜A1. Note that
the perturbation result is only an analysis tool here. Indeed, the matrix ˜A0 is not the matrix
of the system when k = 0 since the equilibrium point (6) is not deﬁned for k = 0. Below,
we only consider the sum ˜A0 + k ˜A1 to be a matrix to analyze, and our main tool for doing
so is perturbation theory.
Let us then study the bifurcation of the simple eigenvalue λ0 = 0 of ˜A0 under the pertur-
bation ˜A0 + ε ˜A1. It is known that when an eigenvalue is simple, it is locally diﬀerentiable
and admits the Taylor expansion [50]
λ(ε) = λ0 + ε λ1 + o(ε)
(11)
where λ1 = vℓ˜A1vr where vℓand vr are the left and right normalized eigenvectors (i.e.
vℓvr = 1) associated with the eigenvalue λ0 = 0 of the matrix ˜A0. They are given by
vℓ=

CA−1
1
−1

and vr =

0
1
0
T .
(12)
Using the above vectors, we get that λ1 = CA−1B, which is negative by Proposition 6.
Therefore, a small positive ε will shift the eigenvalue λ0 = 0 to the open left-half plane. As
a result, using the continuity property of eigenvalues, there will exist a (suﬃciently small)
¯k = ¯k(µ, η) such that for all k ∈(0, ¯k), the equilibrium point X ∗
µ,η,k is locally exponentially
stable. This proves statement (a).
Proof of statement (b). Using the fact that the perturbation direction λ1 = CA−1B < 0
is independent of η and µ, this means that it is possible to ﬁnd a ¯k independent of η and
µ such that for all k ∈(0, ¯k), all the equilibrium points X ∗
µ,η,k for all η, µ > 0 are locally
exponentially stable. This proves statement (b).
♦
10


## Page 11


Example 10 Let us illustrate this result through a simple example. We consider here the
system (4) with the matrices
A =
−1
0
1
1

, B =
1
0

, C =
0
1
T
.
(13)
The matrix ˜A(k) of the linearized system around the equilibrium point (µ, µ, −µ/k, 1/η) is
given by
˜A(k) =


−1
0
k
0
1
−1
0
0
0
0
−k
−ηµ
0
1
−k
−ηµ

.
(14)
The characteristic polynomial χ(λ) associated with this matrix is given by
χ(λ) := λ4 + (2 + k + ηµ)λ3 + (2k + 1 + 2ηµ)λ2 + (k + ηµ)λ + kηµ.
(15)
The Routh-Hurwitz stability criterion gives the following conditions for the stability of the
matrix ˜A(k)
2 + k + ηµ > 0, kηµ > 0, 2(k + ηµ + 1)2
2 + k + ηµ
> 0 and kηµ(2 + k + ηµ) −2(k + ηµ)(k + ηµ + 1)2
2 + k + ηµ
.
(16)
The ﬁrst three conditions are trivially satisﬁed. Expanding the last one gives the following
condition
C(k, ηµ) := η3µ3(k −2) + 2η2µ2(k2 −k −2) + ηµ(k3 −2k2 −6k −2) −2k(1 + k)2 < 0. (17)
Noting that C(0, ηµ) = −2η3µ3 −η2µ2 −2ηµ < 0 (but the matrix is not Hurwitz stable
because kηµ = 0) and using the fact that C(k, ηµ) is continuous in k, we immediately get the
existence of a ¯k(µ, η) > 0, such that C(k, ηµ) and all the other conditions are negative for all
k ∈(0, ¯k(µ, η)). For instance, if we pick η = 1 and µ = 10, we get that
C(k, 10) = 8k3 + 176k2 + 738k −2420 < 0.
(18)
Interpreting now the above expression as a polynomial in k, we can see that there is one sign
change in the coeﬃcients. By virtue of the Descartes’ rule of signs, one can conclude that
there is one and only one positive root to this polynomial, which we denote by ¯k(10, 1). Since,
the left-hand side of the condition is negative for k = 0, then we get that the inequality holds
for all k ∈(0, ¯k(10, 1)). Numerical calculations show that ¯k(10, 1) is approximately 2.11.
This illustrates the ﬁrst statement of Theorem 9.
We now illustrate the second statement of Theorem 9.
We then view the condition
C(k, ηµ) < 0 as a polynomial in ηµ. Obviously, if k > 0 is chosen such that all the co-
eﬃcients of the polynomial are negative then we have that C(k, ηµ) < 0 for all ηµ > 0. In
11


## Page 12


fact, by virtue of Descartes’ rule of signs, this condition is a necessary and suﬃcient condi-
tion for the negativity of the polynomial for all ηµ > 0. We obtain the following conditions
on k:
k < 2, k2 −k −2 < 0 and k3 −2k2 −6k −2 < 0.
(19)
For k = 0, the above conditions are satisﬁed. From Descartes’ rule of sign, we also know
that each polynomial has one and only one positive solution. Interestingly, k = 2 is the
positive root of the second polynomial whereas the third polynomial evaluated at k = 2 gives
-16. Hence, its positive root is larger than 2. As a conclusion, if we pick k ∈(0, 2), then
C(k, ηµ) < 0 holds for all ηµ > 0. This illustrates the second statement.
3.4
A constructive result
Theorem 9 is non-constructive in nature. The calculations in the example show that one
can compute important parameters for the closed-loop system. The downside is that the
calculations will not scale very well as the dimension of the system increases. In this regard,
it would be interesting to derive constructive results. The ﬁrst step towards this goal is to
show that for any µ, k > 0, we can ﬁnd a small enough η > 0 such that the equilibrium point
of the closed-loop system is locally exponentially stable. This is formally stated below:
Lemma 11 Assume that the system (4) is internally positive and that it satisﬁes Assump-
tion 5. Assume further that k, µ > 0 are given. Then, there exists ¯η = ¯η(µ) > 0 such that
for any η ∈(0, ¯η), the equilibrium point X ∗
µ,η,k is locally asymptotically stable.
Proof : Similarly to as in the proof of Theorem 9, we ﬁrst rewrite the linear system matrix
as


A
Bk
0
0
CA−1Bk
0
C
CA−1Bk
0

+ η


0
0
0
0
0
µ
CA−1B
0
0
µ
CA−1B

.
(20)
The spectrum of the matrix to the left is given by λ(A) ∪{0, CA−1Bk}, which corresponds
to the spectrum of a marginally stable matrix. We use, once again, a perturbation argument
on the 0-eigenvalue. The corresponding normalized left- and right-eigenvectors are given by
uℓ=

−CA−1
0
1

and ur =

0
0
1
T .
(21)
The eigenvalue bifurcates according to λ(η) = λ0 + ηλ1 + o(η) where λ1 =
µ
CA−1B . There-
fore, we can conclude on the existence of a ¯η such that for any η ∈(0, ¯η), the equilibrium
points X ∗
µ,η,k are locally asymptotically stable. Note, moreover, that this result does not
depend on the choice for k.
♦
Whereas the above result states that, for any k, µ > 0, we can ﬁnd a small enough η > 0,
that makes the unique equilibrium point of the closed-loop system locally exponentially
stable, the next one provides a condition on the gain k under which the unique equilibrium
12


## Page 13


point of the closed-loop system locally exponentially stable provided that η > 0 is large
enough.
Lemma 12 Assume that the system (4) is internally positive and that it satisﬁes Assump-
tion 5. Assume further that k is chosen such that the matrix
M(k) :=
 A
Bk
−C
0

(22)
is Hurwitz stable. Then, there exists ¯η = ¯η(k) > 0 such that for any η > ¯η the equilibrium
point X ∗
µ,η,k is locally exponentially stable.
Proof : Let ε = 1/η, and rewrite the matrix of the linearized system as


0
0
0
0
0
µ
CA−1B
0
0
µ
CA−1B

+


A
Bk
0
0
CA−1Bk
0
C
CA−1Bk
0

ε .
(23)
The case when ε = 0 corresponds to the case η = ∞. So, in this case, we actually perturb
from inﬁnity. The matrix to the left has spectrum
n
µ
CA−1B , 0
o
where the 0-eigenvalue has
multiplicity n + 1. The left- and right-eigenvectors are given by
vℓ=
In
0
0
0
1
−1

and vr =
In
0
0
0
1
0
T
.
(24)
Since the rank of the eigenvectors is n + 1, hence the 0-eigenvalue is semisimple2. Therefore
it smoothly bifurcates under the action of the perturbation parameter ε > 0 according to
the expression
λi(ε) = 0 + ε λi
1 + o(ε)
(25)
where the λi
1’s are the eigenvalues of the matrix
vℓ


A
Bk
0
0
CA−1Bk
0
C
CA−1Bk
0

vr =
 A
Bk
−C
0

= M(k).
(26)
Therefore, if k > 0 is chosen such that the above matrix is Hurwitz stable, then the 0-
eigenvalues of the left-matrix of (23) bifurcate in n + 1 (distinct or not) eigenvalues that are
located in the open left-half plane. The proof is complete.
♦
The above result shows that if k is chosen such that the matrix M(k) is Hurwitz sta-
ble, then the equilibrium point is locally asymptotically stable for any suﬃciently large η’s.
2An eigenvalue is semisimple when the algebraic multiplicity equals the geometric multiplicity.
13


## Page 14


However, this matrix is nothing else but the closed-loop system matrix of the system (4) con-
trolled with a standard integral controller. This demonstrates a natural connection between
antithetic integral control and standard integral control. The limiting case η →∞, called
”strong binding regime” in [42,43], was used there as a simplifying assumption in order to get
simpler stability condition. This assumption was supported by the fact that strong binding
aﬃnity occurs naturally in living organisms. The diﬀerences between those results and the
ones proposed in this paper lies at the level of generality, the considered mathematical tools,
and, as we shall see below, much stronger results on the robustness of the stability of the
equilibrium point with respect to η or k can be obtained. Other similar results have been
obtained in [47,48] using singular perturbation theory to account for a very large coupling
parameter value. The approach is quite general and addresses diﬀerent problems such as the
approximation of a system into a reduced-order one and bounding trajectories between the
two systems in order to conclude on perfect adaptation property for leaky antithetic integral
controllers. In this paper, stability of the system is simply assumed.
We are now in position to state the main result that complements those in [42,43,47,48]
Theorem 13 Assume that the system (4) is internally positive and that it satisﬁes Assump-
tion 5. Deﬁne ¯k∞as
¯k∞:= sup

κ ≥0 s.t. M(κ) :=
 A
Bκ
−C
0

Hurwitz

.
(27)
When the matrix is Hurwitz for all κ > 0, then we set ¯k∞= ∞.
Then, for all k ∈(0, ¯k∞), the equilibrium point X ∗
µ,η,k is locally asymptotically stable for
all η, µ > 0.
Proof :
We have also proved in Lemma 11, that there exist small enough values for η for
which the equilibrium points are locally asymptotically stable. Similarly, we have proved
in Lemma 12 that there exist large enough values for η for which the equilibrium points
are locally asymptotically stable. The idea is to prove that if k is chosen accordingly, the
equilibrium points are locally asymptotically stable for all η ∈(0, ∞).
We have the following necessary condition that k must be chosen such that M(k) be
Hurwitz stable. We prove that here it that is also suﬃcient. To this aim, let θ = −
µη
CA−1B >
0 and, in this case, the Jacobian matrix rewrites
Ψ(θ) :=


A
Bk
0
0
CA−1Bk
−θ
C
CA−1Bk
−θ

.
(28)
The characteristic polynomial of the above matrix can be shown to be equal to
det(sI −Ψ(θ)) = det(sI −A)

s(s −CA−1Bk) + θ(H(s)k + s)

(29)
where H(s) := C(sI −A)−1B and where we have used the Schur determinant formula. Since
A is Hurwitz, we just have to study the distribution of the zeros of the second factor. Since
14


## Page 15


the poles and the zeros are located at 0 and the open left half-plane, then their sum
F(s, θ) := s(s −CA−1Bk) + θ(H(s)k + s)
(30)
and decompose H(s) = N(s)/D(s) where N(s), D(s) are polynomials. Therefore the zeros
of F(s, θ) are also the zeros of
˜F(s, θ) := s(s −CA−1Bk)D(s) + θ(N(s)k + sD(s)).
(31)
From the above expression, if we view the roots of the ˜F(s, θ) as a function of θ, those roots
start at those of s(s −CA−1Bk)D(s) when θ = 0 and end at those of N(s)k + sD(s) when
θ = ∞. Note that N(s)k + sD(s) coincides with the denominator of the transfer function
describing the closed-loop system consisting of the system H(s) controlled by the integral
controller k/s. We know that N(s)k + sD(s) is stable polynomial since M(k) is Hurwitz
stable. We also know that for a small enough θ, ˜F(s, θ) is also a stable polynomial. It
remains to characterize the behavior of those roots as θ increases from 0 to inﬁnity. The
diﬃculty here lies in the fact that some of the roots will escape to inﬁnity following some
asymptotes due to the fact that the polynomials s(s −CA−1Bk)D(s) and N(s)k + sD(s)
have diﬀerent degrees. To do so, we will use a root locus argument [31] and, to this aim, we
deﬁne the transfer function
G(s)
:=
H(s)k + s
s(s −CA−1Bk)
=
N(s)k + D(s)s
s(s −CA−1Bk)D(s).
(32)
The root locus analysis states that if nz and np are the number of zeros and poles of the
above transfer function, then one has np −nz asymptotes that intersect the real axis at the
point
χ :=
Pnp
i=1 pi −Pnz
i=1 zi
np −nz
where pi and zi are the poles and zeros, counting multiplicity and leaves this point with angle
ϕi = π + 2(i −1)π
np −nz
, i = 1, . . . , np −nz.
(33)
The polynomial s(s −CA−1Bk)D(s) has n + 2 roots where n denotes the order of the
polynomial D(s), so we have that np = n+2. Similarly, N(s)k +sD(s) has n+1 roots since
the degree of N(s) is at most that of D(s) and, hence, nz = n + 1. Therefore, there is only
one asymptote leaving the point χ with angle ϕ1 = π. Since there is no direct-feedthrough
in the system (the input does not directly inﬂuence the output) then we have that the order
of the polynomial N(s) is strictly less than n. From Vieta’s formulas, we have that the
sum of the roots of kN(s) + sD(s) = 0 is equal to −dn−1 where dn−1 is the coeﬃcient of
the polynomial D(s) associated with the n −1-th power. Similarly, the sum of the zeros of
s(s −CA−1Bk)D(s) is equal to CA−1Bk −dn−1. Therefore,
χ = CA−1Bk −dn−1 + dn−1 = CA−1Bk < 0.
15


## Page 16


As a result, the only escaping root to inﬁnity escapes to −∞along the horizontal axis and,
therefore, the roots of the polynomial ˜F(s, θ) are located in the open left half-plane for all
θ ∈(0, ∞). This proves the result.
♦
This result is important for multiple reasons.
First of all, it is a result that shows
that η can be freely chosen as long as k ∈(0, ¯k∞). This parameter can be used to ensure
additional properties for the closed-loop system such as the settling time. However, what
this result states is that the strong-binding regime (i.e. η = ∞) is the worst case regime in
terms of stability. Ensuring stability in this regime is suﬃcient to ensure stability for any
other binding regime. This is particulary important since it means that the results obtained
in [42,43] remain valid even when the coupling parameter is ﬁnite, which is likely to be the
case in practice. Perhaps surprisingly, a dual result can be found in which the gain k can be
made free by suitably choosing η. This result is stated below:
Theorem 14 Assume that the system (4) is internally positive and that it satisﬁes Assump-
tion 5. Deﬁne ¯η∞as
¯η∞:= g2
¯µ sup

κ ≥0 s.t. M(κ) :=
 A
Bκ
−C
0

Hurwitz

(34)
where 0 < µ ≤¯µ. When the matrix is Hurwitz for all κ > 0, then we set ¯η∞= ∞.
Then, for all η ∈(0, ¯η∞), the equilibrium point X ∗
µ,η,k is locally asymptotically stable for
all k > 0 and all µ ∈(0, ¯µ).
Proof :
The proof follows from the same lines as the proof of Theorem 13 and is therefore
only sketched. The starting point is again the characteristic polynomial ˜F(s, θ) which we
rewrite as
˜F(s, θ) = (s + θ)sD(s) + k(gsD(s) + θN(s))
where g = −CA−1B is the gain of the system. Interestingly, we can see that when k = 0,
the roots of that polynomial are those of (s + θ)sD(s) whereas when k →∞the roots
tend to those of gsD(s) + θN(s). We know that for small enough k’s, the polynomial is
stable regardless the values for µ, η > 0. The roots of gsD(s) + θN(s) are in the open left
half-plane for all µ ∈(0, ¯µ) if and only if η ∈(0, ¯η∞). To show that the system remains
stable for all values for η, we again rely on a root locus argument and note that the degrees
of the numerator and the denominator are again equal to n + 1 and n + 2, so the only
asymptote coincides with the real axis and point towards −∞. The sums of zeros and poles
are given by −gdn−1 and −µη/g −dn−1, respectively. In this regard, the asymptote starts
at χ = −µη/g −dn−1 + gdn−1 and points towards −∞along the real axis. Therefore, the
roots of the polynomial ˜F(s, θ) lie in the open left half-plane for all k ∈(0, ∞) provided that
η ∈(0, ¯η∞).
♦
Example 15 Let us consider again the system of Example 10. After tedious calculations,
it was shown that if k < ¯k∞= 2, then the closed-loop system is locally asymptotically stable
16


## Page 17


for all η, µ > 0. We now prove the same result using Theorem 13. We ﬁrst form the matrix
 A
Bk
−C
0

=


−1
0
k
1
−1
0
0
−1
0

.
(35)
The corresponding characteristic polynomial is given by
λ3 + 2λ2 + λ + k.
(36)
The Routh-Hurwitz stability criterion yields the conditions k > 0 and k −2 < 0. Hence,
¯k∞= 2. Similarly, we have that ¯η∞= 2g2/µ.
3.5
Computing k∞and η∞
We propose in this section some ways to establish the value for ¯k. The ﬁrst approach allows
one to determine whether this value is ﬁnite using the concept of strictly positive real transfer
functions and strictly passive systems. The second approach is based on stability crossing
where we study the existence of purely imaginary eigenvalues which essentially reduces to
the analysis of some polynomials.
The case ¯k∞= ∞and ¯η∞= ∞. Interestingly, there are cases where the equilibrium
point of the closed-loop system (4)-(5) is locally exponentially stable for any µ, η, k > 0.
This is formalized in the result below:
Theorem 16 Assume that the system (4) is internally positive and that it satisﬁes Assump-
tion 5. Deﬁne further its transfer function as G(s) := C(sI −A)−1B. Then, the following
statements are equivalent:
(a) The system (4) is strictly passive.
(b) The transfer function G is strictly positive real, that is, ℜ[G(jω)] > 0 for all ω ∈R≥0
and
lim
ω→∞ω2ℜ[G(jω)] > 0.
(c) There exist symmetric positive deﬁnite matrices P, Q such that ATP +PA = −Q and
PB = CT.
(d) The equilibrium point of the closed-loop system (4)-(5) is locally exponentially stable
for any µ, η, k > 0.
Proof :
The proof of the equivalence between two ﬁrst statements can be found in [36].
A proof for the statement (b) can be also found in [54]. The equivalence with the third
statement comes from the Kalman-Yakubovich-Popov Lemma; see e.g [35]. In this regard,
we simply need to prove the equivalence with the last statement. The proof follows from
17


## Page 18


an application of the Nyquist stability criterion. First note that, since −CA−1B > 0, then
ℜ[G(jω)] > 0 for all ω ∈R≥0 is equivalent to saying that arg[G(jω)] ∈(−π/2, π/2) for
all ω ∈R≥0. The loop-transfer associated with the system described by M(k) is given by
L(s) = kG(s)/s and we have that
arg(L(jω))
=
arg(kG(jω)) −arg(jω)
=
arg(G(jω)) −π/2.
(37)
and
|L(jω)| = k|G(jω)|
ω
.
(38)
Since the system G(s) is stable then, from the Nyquist stability criterion, the closed-loop
system is unstable if and only if there is an ωc > 0 such that arg(L(jωc)) = −π and k ≥kc
where kc = ωc/|G(jωc)|; i.e. the Nyquist plot encircles at least once the critical point −1. For
such an ωc to exist, we need that arg(G(jωc)) = −π/2. Therefore, a necessary and suﬃcient
condition for this ωc to not exist is that ℜ[G(jω)] > 0 for all ω ∈R≥0. This concludes the
proof.
♦
We give below an example of a controlled reaction network satisfying such a condition.
Example 17 Let us consider a reaction network represented by the following linear system
which is inspired from an example in [42]
˙x(t)
=
−γ
k1
k2
−γ

x(t) +
0
1

y(t)
=

0
1

(39)
where γ2 −k1k2 > 0. This system is internally positive with a Hurwitz stable system matrix
and we have that −CA−1B = γ/(γ2 −k1k2). The associated transfer function is given by
H(s) =
s + γ
s2 + 2γs + γ2 −k1k2
.
(40)
Clearly the relative degree is equal to one and we have that
ℜ[H(jω)] =
γω2 + γ2 −k1k2
(−ω2 + γ2 −k1k2)2 + 4γ2ω2.
(41)
Since γ2 −k1k2 > 0, the numerator is always positive and we have that
lim
ω→∞ω2ℜ[G(jω)] = γ > 0.
Hence, the transfer function is strictly positive real and the equilibrium point of the closed-
loop system will be locally exponentially stable for all positive controller parameters µ, k and
θ.
18


## Page 19


Alternatively, we can check the condition of statement (c) in Theorem 16. Let us deﬁne
P =
p1
p2
p2
p3

.
(42)
Then, the condition that PB −CT = 0 yields p2 = 0 and p3 = 1. Moreover, we have that
ATP + PA =
 −2p1γ
p1k1 + k2
p1k1 + k2
−2γ

.
(43)
This matrix is negative deﬁnite if and only if the trace is negative and the determinant is
positive. As the trace is negative for all p1 > 0, we need to ﬁnd a suitable value for p1 > 0
such that the determinant is positive. This yields the condition
k2
1p2
1 + 2p1(k1k2 −2γ2) + k2
2 < 0.
(44)
This condition is minimum for p1 = 2γ2 −k1k2
k2
1
which yields
ATP + PA = 2γ
k2
1
−(2γ2 −k1k2)
k1γ
k1γ
−k2
1.

(45)
The determinant of the matrix without the factor is then equal to k2
1(γ2−k1k2) and is positive.
This proves that the system is strictly passive.
The case ¯k∞< ∞and ¯η∞< ∞. When the test previously presented fails, then ¯k is
necessarily ﬁnite and its value can be computed using a stability crossing test, a popular
method in the time-delay systems community [28,39]. This is stated in the result below:
Proposition 18 Assume that the system (4) is internally positive and that it satisﬁes As-
sumption 5. Let P(s, k) be the characteristic polynomial of the matrix M(k) in (22) and
deﬁne further the real polynomials P 0
R(ω), P 1
R(ω), P 0
I (ω) and P 1
I (ω) as
P 0
R(ω) + kP 1
R(ω) := ℜ[P(k, jω)] and P 0
I (ω) + kP 1
I (ω) := ℑ[P(k, jω)].
(46)
If the set
Ω:=

ω > 0 : P 1
R(ω)P 0
I (ω) −P 0
R(ω)P 1
I (ω) = 0
	
(47)
is nonempty, then the value for ¯k∞and ¯η∞are given by
¯k∞= inf
¯ω∈Ω







−P 0
R(¯ω)
P 1
R(¯ω)
if
P 1
R(¯ω) ̸= 0
−P 0
I (¯ω)
P 1
I (¯ω)
if
P 1
I (¯ω) ̸= 0.
(48)
¯η∞= g2
µ inf
¯ω∈Ω







−P 0
R(¯ω)
P 1
R(¯ω)
if
P 1
R(¯ω) ̸= 0
−P 0
I (¯ω)
P 1
I (¯ω)
if
P 1
I (¯ω) ̸= 0.
(49)
where g = −CA−1B. When the set Ωis empty, then ¯k∞= ∞and ¯η∞= ∞.
19


## Page 20


Proof : The matrix M(k) is Hurwitz stable if and only if the roots of its characteristic
polynomial P(s, k) are all located in the open left-half plane. We then look for pairs (¯ω, ¯k) ∈
R2
>0 such that P(j¯ω, ¯k) = 0. By doing so, we look for critical values of ¯k for which we
necessarily have a pair of eigenvalues on the imaginary axis. This expression can be rewritten
as

P 0
R(¯ω) + ¯kP 1
R(¯ω)

+ j

P 0
I (¯ω) + ¯kP 1
I (¯ω)

= 0
(50)
where P 0
R(ω) + kP 1
R(ω) := ℜ[P(jω, k)], P 0
I (ω) + kP 1
I (ω) := ℑ[P(jω, k)]. If such a pair (¯k, ¯ω)
exists then we have that P 0
R(¯ω) + ¯kP 1
R(¯ω) = P 0
I (¯ω) + ¯kP 1
I (¯ω) = 0. This can be rewritten as
P 0
R(¯ω)
P 1
R(¯ω)
P 0
I (¯ω)
P 1
I (¯ω)
 1
¯k

= 0.
(51)
This is equivalent to say that the vector lies in the kernel of the matrix and a necessary
and suﬃcient condition for that is that the matrix be singular, or, equivalently, that its
determinant be equal to zero. This leads to the condition (47). We can then solve for ¯ω
and either use P 0
R(¯ω) + ¯kP 1
R(¯ω) = 0 or P 0
I (¯ω) + ¯kP 1
I (¯ω) = 0 to ﬁnd ¯k. Since, we may have
multiple solutions for the crossing frequencies, we need to choose the smallest ¯k to ensure
the stability. The result follows.
♦
3.6
Disturbance rejection/Perfect adaptation
Let us analyze the disturbance rejection properties of the antithetic integral controller. It
is expected that this controller rejects constant disturbances on the control input and on
the states of the system by virtue of the internal model principle which stipulates that
“any good regulator must create a model of the dynamic structure of the environment in
the closed-loop system” [3]. This follows from the fact that the integrator models constant
disturbances. Disturbance rejection of the antithetic motif was notably addressed in [7] in
the stochastic setting with respect to constant disturbance rejection. A more general analysis
in the deterministic setting is described in [42] using the sensitivity function. We show this
using a diﬀerent approach. To this aim, let us consider the following disturbed system
˙x(t)
=
Ax(t) + Bu(t) + Ed, x(0) = x0
y(t)
=
Cx(t)
(52)
where the disturbance vector d ∈R≥0 has been added and where E ∈Rn
≥0.
Assuming that the system is internally positive and that it satisﬁes the conditions of
Assumption 5, then for any constant u ≥0 and d ≥0, we have that y = −CA−1(Bu + Ed)
at equilibrium. Since CA−1 ≤0 and B, E ≥0, then we have that y ≥−CA−1Ed. Therefore,
if d ≥0 is such that −CA−1Ed = µ+ϵ, ϵ > 0, then output tracking is not achievable. Indeed,
for the reference to be reached by the output, we would need the control input to be equal
to
u = µ + CA−1B
−CA−1E
=
−ϵ
−CA−1E < 0
(53)
20


## Page 21


which would violate the nonnegativity of the control input.
This leads us to deﬁne the
following set of admissible disturbance values
Dµ :=

d ∈R≥0 : µ + CA−1Ed > 0
	
.
(54)
In particular when −CA−1E = 0, then the disturbance can be arbitrarily large.
Proposition 19 Let µ > 0 be given and assume that d ∈Dµ, then the controlled disturbed
system (52)-(5) has the following equilibrium point (x∗, z∗
1, z∗
2):

A−1
B(µ + CA−1Ed)
CA−1B
−Ed

, −µ + CA−1Ed
CA−1Bk
,
µ
ηkz∗
1

.
(55)
Proposition 20 Let µ > 0 be given. For any E of appropriate dimensions, the controlled
disturbed system (52)-(5) rejects constant disturbances provided that d ∈Dµ and the corre-
sponding equilibrium point is locally exponentially stable.
Proof : The controlled disturbed system (52)-(5) locally rejects constant disturbances if and
only if the matrix


A
Bk
0
E
0
−kηz∗
1
−kηz∗
2
0
C
−kηz∗
1
−kηz∗
2
0
C
0
0
0


(56)
is singular. This is equivalent to saying that the DC-gain of the transfer d 7→y is zero
or that the (local) transfer function of the closed-loop system has a transmission zero at
the zero frequency. It is immediate to see that this is the case since the last row is a linear
combination of the two previous ones. Note that this would not be the case if the disturbance
were acting on the dynamics of the controller or on the output.
♦
3.7
Example: gene expression
We exemplify here the results of the section on the following gene expression model
˙x1(t)
=
−γ1x1(t) + u(t)
˙x2(t)
=
k2x1(t) −γ2x2(t)
(57)
where x1, x2 and u are the average populations of mRNA, protein and the transcription rate
(control input). As in [7,14,42,43], the idea is to control the system using a positive integral
controller. The control input being driven positively to the state x1, the control input can
be chosen to be the positive component of the controller and we have
˙z1(t)
=
µ −ηkz1(t)z2(t)
˙z2(t)
=
x2(t) −ηkz1(t)z2(t)
u(t)
=
kz1(t)
(58)
21


## Page 22


where it can be seen that the goal is to have the average number of proteins to track the
reference value µ > 0. We have the following matrices
A =
−γ1
0
k2
−γ2

, B =
1
0

and C =

0
1

.
(59)
Using Theorem 13, we ﬁnd that
¯k∞= γ1γ2(γ1 + γ2)
k2
which means that the unique equilibrium point is locally exponentially stable for all k ∈
(0, ¯k∞), µ, η > 0. We now use Theorem 14 to ﬁnd that
¯η∞= k2(γ1 + γ2)
¯µγ1γ2
(60)
which means that the unique equilibrium point is locally exponentially stable for all µ ∈
(0, ¯µ), η ∈(0, ¯η∞), k > 0.
For completeness, it seems interesting to obtain the same result using Proposition 18.
We have that
P(s, k) = sD(s) + kN(s)
(61)
where D(s) = (s + γ1)(s + γ2) and N(s) = k2. Substituting (s, k) by (j¯ω, ¯k) yields
P(j¯ω, ¯k) = −¯ω2(γ1 + γ2) + kk2 + jω(γ1γ2 −ω2) = 0,
(62)
and, hence,
P 0
R(¯ω) = −¯ω2(γ1 + γ2), P 1
R(¯ω) = k2, P 0
I (¯ω) = ω(γ1γ2 −ω2) and P 1
I (¯ω) = 0.
(63)
We then obtain that
P 1
R(¯ω)P 0
I (¯ω) −P 0
R(¯ω)P 1
I (¯ω) = k2¯ω(γ1γ2 −¯ω2).
(64)
The only positive root to this equation is given by ¯ω = (γ1γ2)1/2 and we get that the
corresponding value for ¯k is given by
¯k = −P 0
R(¯ω)
P 1
R(¯ω) = −−¯ω2(γ1 + γ2)
k2
= γ1γ2(γ1 + γ2)
k2
.
(65)
For numerical purposes, let us consider the parameters γ1 = 1 h−1, γ2 = 1 h−1, k2 = 1
h−1. In such a case, we must choose k < ¯k∞= 2. Picking then k = 1/3 h−1, kη = 10
nM−1 h−1 and µ = 1 nM h−1, we obtain the simulation results depicted in Figure 1 and
Figure 2. We can observe the convergence of the output to the reference and that a larger
kη improves the transient performance. In fact, it seems that when kη is large enough,
the output trajectories converge to the trajectory that would be obtained using a standard
22


## Page 23


0
5
10
15
20
Time [sec]
0
0.5
1
1.5
2
2.5
3
3.5
mRNA (x1)
Protein (x2)
Control input (z1)
z2
Figure 1: Controlled gene expression network with k = 1/3, kη = 10 and µ = 1.
integral control law; see Figure 3. The bifurcation curve in the (k, η)-plane is depicted in
Figure 4 where the stable region is located below the curve. The vertical line corresponds to
the value ¯k∞and we can clearly observe that it is an vertical asymptote for the bifurcation
curve illustrating that for k ∈(0, ¯k∞) the closed-loop system is locally exponentially stable
regardless the value of η > 0. Conversely, the horizontal asymptote indicates the value for
¯η∞which is equal to 2 here. we can see that when η is smaller than this value, the closed-loop
system is stable for all gains k > 0. Figure 5 depicts the bifurcation surface in the (k, ηk)-
plane with corresponds to the bifurcation curve for the slightly diﬀerently parameterized
controller in [7]. This demonstrates the validity of the results for this controller. Figure 3.7
depicts the root locus in the case where k = 1 as η sweeps from 0 to ∞. We can clearly see
that the system remains stable as the root locus remains conﬁned in the open left half-plane.
This is a consequence of the fact that M(1) is Hurwitz stable. Note also the presence of the
asymptote point towards −∞for the root escaping to inﬁnity. On the other hand, Figure
3.7 depicts the case where k = 2.5 showing that the system becomes unstable if η is too
large because the matrix M(2.5) is not Hurwitz stable.
4
Antithetic integral control of nonlinear internally pos-
itive systems
This section aims at demonstrating that the theory developed in the previous section for
linear positive systems also applies to some classes of nonlinear positive systems. Nonlinear
positive systems are brieﬂy recalled in Section 4.1. The main stability results are presented
in Section 4.2 and are illustrated in Section 4.3 through several examples taken from bio-
23


## Page 24


0
5
10
15
20
Time [sec]
0
0.2
0.4
0.6
0.8
1
1.2
1.4
1.6
2k =0.1
2k =1
2k =10
2k =100
2k =1000
Figure 2: Evolution of the protein concentration with k = 1/3, µ = 1 and diﬀerent values
for ηk.
0
5
10
15
20
Time [sec]
0
0.2
0.4
0.6
0.8
1
1.2
Figure 3: Comparison of the output trajectory for the system controlled with an antithetic
integral control with kη = 1000 (blue) and a standard integral control (red). The trajectories
are so close that we cannot distinguish them.
24


## Page 25


k
0
5
10
15
20
2
0
20
40
60
80
100
Figure 4: Bifurcation curve in the (k, η) plane for the gene expression network with γm = 1,
γp = 1, kp = 1 and µ = 1. The vertical line corresponds to the value ¯k∞whereas the
horizontal one corresponds to ¯η∞.
k
0
5
10
15
20
2k
0
20
40
60
80
100
Figure 5: Bifurcation curve in the (k, kη) plane for the gene expression network with γm = 1,
γp = 1, kp = 1 and µ = 1. The vertical line corresponds to the value ¯k whereas the horizontal
one corresponds to the maximum value for ηk for which the system is stable for all k > 0.
The value is approximately equal to 9.4815 in the current scenario.
25


## Page 26


<[6]
-5
-4
-3
-2
-1
0
1
=[6]
-0.8
-0.6
-0.4
-0.2
0
0.2
0.4
0.6
0.8
Figure 6: Root locus of the closed-loop network as η increases when k = 1. The root locus
starts from the zeros denoted by crosses and end up at the poles indicated by circles which
coincide with the eigenvalues of the matrix M(1). We can clearly see the asymptote going
to −∞and that the root locus stays in the open left half-plane.
chemistry and epidemiology.
4.1
Nonlinear positive systems
Let us consider here the following nonlinear system
˙x(t)
=
f(x(t), u(t)), x(0) = x0
y(t)
=
h(x(t))
(66)
where x, x0 ∈Rn, u ∈R and y ∈R are the state of the process, the initial condition, the
control input and the measured output, respectively.
Proposition 21 The following statements are equivalent:
(a) The system (66) is internally positive; i.e. for any x0 ≥0 and u(t) ≥0, for all t ≥0,
we have that x(t) ≥0 and y(t) ≥0, for all t ≥0.
(b) The following conditions hold:
• fi(x, u) ≥0 whenever xi = 0 and xj, u ≥0, j = 1, . . . , N, j ̸= i and for all
i = 1, . . . , n;
• h(x) ≥0 for all x ≥0.
26


## Page 27


<[6]
-5
-4
-3
-2
-1
0
1
=[6]
-1.5
-1
-0.5
0
0.5
1
1.5
Figure 7: Root locus of the closed-loop network as η increases when k = 2.5. The root locus
starts from the zeros denoted by crosses and end up at the poles indicated by circles which
coincide with the eigenvalues of the matrix M(2.5). We can clearly see the asymptote going
to −∞but the root locus does not stay conﬁned in the open left half-plane because the
matrix M(2.5) is not Hurwitz stable.
27


## Page 28


Note that those conditions naturally reduce to those in Proposition 4 in the linear case.
Deﬁne now the following sets
Y := {h(x) : f(x, u) = 0, u ∈R≥0} ,
(67)
U (y) := {u : f(x, u) = 0, y = h(x)} ,
(68)
X (y) := {x : f(x, u) = 0, y = h(x)} ,
(69)
which characterize the set of equilibrium output values for any given input value, the set
of all constant inputs associated with a given equilibrium output value and the set of the
equilibrium state values given an equilibrium value for the output. We assume for simplicity
that
Assumption 22 For all y ∈Y , the sets U (y) and X (y) are singletons which are denoted
by u∗(y) and x∗(y) their only element, respectively, and the map F(u) := {h(x) : f(x, u) = 0}
is continuous and strictly monotonic.
Assumption 23 For all y ∈Y , the matrix
∂f
∂x

(x,u)∈U (y)×X (y)
(70)
is invertible.
We are now in position to properly deﬁned the linearized system associated with (66)
about an equilibrium point uniquely deﬁned by the value of the output at stead-state:
Proposition 24 Let us consider the system (66) that is assumed to be internally positive
and to satisfy Assumption 22 and Assumption 23. Then, the equilibrium point associated
with the steady-state output y∗= µ ∈Y of the nonlinear system (66) is given by
u∗(µ) = F −1(µ), x∗(µ) = g(F −1(µ))
(71)
where F −1 is the inverse function of the nonlinear gain F deﬁned as F(u) = h(g(u)) and g :
R 7→Rn is such that f(g(u), u) = 0. Moreover, the linearized system about that equilibrium
is given by
˙˜x(t)
=
˜A˜x(t) + ˜B˜u(t)
˜y(t)
=
˜C˜x(t)
(72)
where
 ˜A(µ)
˜B(µ)
˜C(µ)
0

:=


∂f
∂x

(x∗(µ),u∗(µ))
∂f
∂u

(x∗(µ),u∗(µ))
∂h
∂x

(x∗(µ),u∗(µ))
0

.
(73)
28


## Page 29


Proof :
Assumption 22 imposes the existence of a unique steady-state for every possible
steady-state output value whereas Assumption 23 implies that, by virtue of the implicit
function theorem, that the function g : R 7→Rn mapping steady-state input values to
steady-state state values is locally well-deﬁned. Since the function F is monotonic, it is
invertible. The result then follows.
♦
Assumption 25 The matrix ˜A is Hurwitz stable and ˜C(µ) ˜A(µ)−1 ˜B(µ) ̸= 0.
As for linear systems, the condition ˜C(µ) ˜A(µ)−1 ˜B(µ) ̸= 0 states that the linearized
system is locally output controllable. However, the DC-gain may not be positive, the matrix
˜A(µ) may not be Metzler and the matrices ˜B(µ), ˜C(µ) may not be nonnegative. This is,
fortunately, not an issue as what really matters is the sign of the DC-gain. Indeed, if the
DC-gain is positive then we shall choose u = kz1. Otherwise, we shall choose u = kz2. This
will be clariﬁed in the next section.
4.2
Main results
We consider the following version of Problem 7
Problem 26 Let the reference µ > 0 be given and assume that the system (66) is internally
positive and that it satisﬁes Assumption 22, Assumption 23 and Assumption 25. Find an
integral controller such that
(a) the control input u is nonnegative at all times;
(b) the equilibrium point of interest of the closed-loop system consisting of the system(66)
and the controller is (locally) asymptotically stable;
(c) the output y asymptotically tracks the reference µ > 0; i.e. y(t) →µ as t →∞;
(d) the closed-loop system locally rejects constant disturbances acting on the input and on
the state of the system.
Again, the antithetic integral controller
˙z1(t)
=
µ −ηkz1(t)z2(t)
˙z2(t)
=
h(x(t)) −ηkz1(t)z2(t)
z(0)
=
z0
(74)
will be shown to provide a suitable solution to the Problem 26. The main diﬀerence with
the linear case is that the local gain of internally linear systems is always positive. We have
the following preliminary result:
29


## Page 30


Proposition 27 Assume that Assumption 22, Assumption 23 and Assumption 25 are sat-
isﬁed for the system (66) and assume that this system is internally positive.
Then, the
equilibrium point of the closed-loop system consisting of the internally positive system (66)
and the antithetic integral controller (74) with u = kz1 is given by X ∗,+
µ,η,k := (x∗, z∗) where
x∗(µ) = g(F −1(µ)), z∗
1(µ) = F −1(µ)
k
and z∗
2(µ) =
µ
ηF −1(µ).
(75)
When u = kz2, the equilibrium point is denoted by X ∗,−
µ,η,k := (x∗, z∗) where
x∗(µ) = g(F −1(µ)), z∗
1(µ) =
µ
ηF −1(µ) and z∗
2(µ) = F −1(µ)
k
.
(76)
It is interesting to
We then have the following result in the case where u = kz1:
Theorem 28 Let the conditions in Assumption 22, Assumption 23 and Assumption 25 be
veriﬁed for the system (66) and assume that this system is internally positive. Let µ ∈Y be
given. Assume further that F(u) is monotonically increasing or, equivalently, that the local
gain is positive for all µ ∈Y . Then, for any k ∈(0, ¯k+
∞(µ)), the equilibrium point X ∗,+
µ,η,k is
locally asymptotically stable for all η > 0 where
¯k+
∞(µ) := sup

κ ≥0 s.t.
 ˜A(µ)
˜B(µ)κ
−˜C(µ)
0

is Hurwitz stable

.
(77)
Proof : Let the conditions in Assumption 22, Assumption 23 and Assumption 25 be veriﬁed.
Then, the linearized system about the unique equilibrium point induced by y∗(µ) = µ is given
by


˙˜x(t)
˙˜z1(t)
˙˜z2(t)

=


˜A(µ)
˜B(µ)k
0
0
−
kµ
F −1(µ)
−ηF −1(µ)
˜C(µ)
−
kµ
F −1(µ)
−ηF −1(µ)




˜x(t)
˜z1(t)
˜z2(t)


(78)
where ˜x = x −x∗(µ), ˜z1 = z1 −z∗
1(µ) and ˜z2 = z2 −z∗
2(µ). The rest of the proof follows from
exactly the same steps as in the linear case since the matrix is of similar structure. The only
diﬀerence is that the results may now depend on the set-point µ.
♦
We can see that the result reduces to that of Theorem 13 when F(u) = −CA−1Bu and,
hence, F −1(µ) = −µ/CA−1B. Indeed, substituting this expression in the matrix in (78)
exactly yields the matrix in (8). The value for ¯k+
∞(µ) can be computed using the approaches
described in Section 3.5. In particular, if the transfer function ˜C(µ)(sI −˜A(µ))−1 ˜B(µ) is
strictly positive real, then ¯k+
∞(µ) = ∞.
Let us address now the case where u = kz2:
30


## Page 31


Theorem 29 Let the conditions in Assumption 22, Assumption 23 and Assumption 25 be
veriﬁed for the system (66) and assume that this system is internally positive. Let µ ∈Y be
given. Assume further that F(u) is monotonically decreasing or, equivalently, that the local
gain is negative for all µ ∈Y .
Then, for any k ∈(0, ¯k−
∞(µ)), the equilibrium point X ∗,+
µ,η,k is locally asymptotically stable
for all η > 0 where
¯k−
∞(µ) := sup

κ ≥0 s.t.
 ˜A(µ)
˜B(µ)κ
˜C(µ)
0

is Hurwitz stable

.
(79)
Proof : Let the conditions in Assumption 22, Assumption 23 and Assumption 25 be veriﬁed.
Then, the linearized system about the unique equilibrium point induced by y∗(µ) = µ is given
by


˙˜x(t)
˙˜z1(t)
˙˜z2(t)

=


˜A(µ)
0
˜B(µ)k
0
−ηF −1(µ)
−
kµ
F −1(µ)
˜C(µ)
−ηF −1(µ)
−
kµ
F −1(µ)




˜x(t)
˜z1(t)
˜z2(t)


(80)
where ˜x = x −x∗(µ), ˜z1 = z1 −z∗
1(µ) and ˜z2 = z2 −z∗
2(µ). The rest of the proof follows from
the same arguments as in the linear case with the diﬀerence that the matrix has a diﬀerent
structure. The proof is only sketched for brevity. We ﬁrst show that a small enough k > 0
makes the above matrix Hurwitz stable. Indeed, the zero-eigenvalue of the matrix when
k = 0 moves in the direction −˜C(µ) ˜A(µ)−1 ˜B(µ) for some suﬃciently small k > 0. Since,
the local gain is negative, then the zero eigenvalue moves in the open left half-plane, making
the matrix Hurwitz stable for some suﬃciently small k > 0. Similarly, we show that for any
suﬃciently small η > 0 makes the matrix Hurwitz stable. The zero-eigenvalue of the matrix
when η = 0 moves in the direction −˜C(µ) ˜A(µ)−1 ˜B(µ)F −1(µ) < 0 for some suﬃciently small
η > 0. Hence the zero eigenvalue moves in the open left half-plane, making the matrix
Hurwitz stable for some suﬃciently small k > 0. Analogously, we can show that the matrix
Hurwitz stable for any suﬃciently large η > 0 provided that the matrix (79) is Hurwitz
stable. To prove that the Hurwitz stability of the matrix in (79) is a necessary and suﬃcient
condition for the local stability of the equilibrium point X ∗,−
µ,η,k, we can invoke a root locus
argument which develops exactly as in the linear case. The details are omitted.
♦
The value for ¯k−
∞(µ) can be computed using the approaches described in Section 3.5. In
particular, if the transfer function −˜C(µ)(sI −˜A(µ))−1 ˜B(µ) (not the minus sign) is strictly
positive real, then ¯k−
∞(µ) = ∞.
4.3
Examples
SIS model. Let us consider the following deterministic SIS model
˙x1(t)
=
−βx1(t)x2(t) + αx2(t)
˙x2(t)
=
βx1(t)x2(t) −αx2(t)
(81)
31


## Page 32


where x1(t) and x2(t) represent the susceptible and infectious people, respectively. Since
the system veriﬁes the conservation law x1(t) + x1(t) = N for all t ≥0, it can therefore be
reduced to the system one-dimensional system:
˙x1(t) = −βx1(t)(N −x1(t)) + α(N −x1(t)).
(82)
Assume now that we would like to control the number of susceptible people to a certain
value µ < N, and that it is possible to control the recovery rate α, thus we set α(t) = u(t).
Hence,
Y = [0, µ], X (µ) = {µ} and U (µ) = F −1(µ) = {µβ}
(83)
and F(u) = u/β. Hence, the system satisﬁes Assumption 22. Since, the nonlinear gain is an
monotonically increasing function of u, then the local DC-gain is positive and, therefore, we
choose the controller
˙z1(t)
=
µ −ηkz1(t)z2(t)
˙z2(t)
=
x1(t) −ηkz1(t)z2(t)
u(t)
=
kz1(t)
(84)
where k, η > 0 are the controller parameters.
We then have the following result:
Theorem 30 The unique equilibrium point
x∗
1
=
µ,
z∗
1
=
βµ
k ,
z∗
2
=
1
βη
(85)
of the closed-loop system (82)-(84) is locally exponentially stable for all N, k, η, β > 0 and
all µ ∈(0, N).
Proof :
We need ﬁrst to show that the system satisﬁes the assumptions. We have already
shown that Assumption 22 holds. The linearized system around the equilibrium point (85)
is given by
˙X(t) =


β(µ −N)
k(N −µ)
0
0
−k/β
−ηβµ
1
−k/β
−ηβµ

X(t).
(86)
The matrix ˜A(µ) = β(µ−N) is negative since µ < N and we have that −C(µ)A(µ)−1B(µ) =
1/β. Therefore, the assumptions are satisﬁed. The result then follows from the fact that the
local transfer function of the system given by
H(s) =
N −µ
s + β(N −µ)
(87)
is strictly positive real for all β, N and 0 < µ < N.
♦
For simulation purposes, let us consider the controlled SIS-model (82)-(84) with the
parameters β = 1, ηk = 13, k = 2, N = 100 and µ = 99; i.e. we aim at maintaining 99% of
32


## Page 33


the population healthy. The initial condition is set to x1(0) = 90 and z1(0) = z2(0) = 0. We
obtain the simulation results depicted in Figure 8.
Time [sec]
0
5
10
15
20
0
20
40
60
80
100
x1(t)
z1(t)
z2(t)
Figure 8: Controlled SIS system (82)-(84) with the parameters β = 1, ηk = 13, k = 2,
N = 100 and µ = 99.
Gene expression with controlled translation. Let us consider the following gene ex-
pression model with repressed translation:
˙x1
=
−γ1x1 + k1
˙x2
=
k2x1
1 + u −γ2x2
(88)
where x1 and x2 denote the concentration of the mRNA and its associated protein, respec-
tively. Choosing y = x2, we have that
F(u) =
k1k2
γ1γ2(1 + u) and, hence, F −1(µ) = k1k2
γ1γ2µ −1.
(89)
Hence,
Y =

0, k1k2
γ1γ2

, X (µ) =





k1
γ1
µ




and U (µ) =
 k1k2
γ1γ2µ −1

.
(90)
As a result, the system satisﬁes Assumption 22. Moreover, since the function F(u) is a
monotonically decreasing function of u, then the local gain is negative and, therefore, we
need to consider the controller
˙z1(t)
=
µ −ηkz1(t)z2(t)
˙z2(t)
=
x2(t) −ηkz1(t)z2(t)
u(t)
=
kz2(t).
(91)
33


## Page 34


This yields the following result:
Proposition 31 The unique equilibrium point
(x∗
1, x∗
2, z∗
1, z∗
2) =
k1
γ1
, µ,
γ1γ2µ2
η(k1k2 −γ1γ2µ), 1
k
 k1k2
γ1γ2µ −1

(92)
of the closed-loop system (88)-(91) is locally exponentially stable for all γ1, γ2, k1, η, k > 0
and all µ ∈

0, k1k2
γ1γ2

.
Proof : The linearized closed-loop system is given by
˜A(µ) =
" −γ1
0
γ1γ2µ
k1
−γ2
#
, ˜B(µ) =


0
−γ1γ2
2
k1k2

, ˜C(µ) =

0
1

.
(93)
We can see that the matrix ˜A(µ) is Hurwitz stable (hence invertible) for all µ ∈Y and that
−˜C(µ) ˜A(µ)−1 ˜B(µ) = −γ1γ2µ2
k1k2
< 0.
Hence, the linearized system satisﬁes Assumption 25 and Assumption 23 for all µ ∈Y .
Therefore, we can apply Theorem 29 and consider the transfer function
Hµ(s) := −˜C(µ)(sI −˜A(µ))−1 ˜B(µ) =
γ1γ2
2
k1k2(s + γ2).
(94)
This transfer function as a positive DC-gain and is of ﬁrst-order type, which implies that it
is strictly positive real. This proves the result.
♦
5
Exponential integral control of linear positive sys-
tems
We consider in this section the exponential integral controller. First the model of the ex-
ponential integral controller is given. The local stability of the diﬀerent equilibrium points
is then analyzed. Finally, a way to compute the maximum value of the exponential rate
is provided. It is notably shown that the gain of the controller does not alter the stability
properties of the closed-loop system.
5.1
The model
The exponential integral controller is based on the consideration of
ϕ(x) = eαx, α > 0
(95)
as regularizing function. This leads to the following result:
34


## Page 35


Proposition 32 The exponential integral controller is given by
˙v(t)
=
αv(t)(µ −y(t)), v(0) = v0
u(t)
=
kv(t)
(96)
where k > 0 is the gain of the controller and α > 0 is the exponential rate of the controller
of the controller. The closed-form solution of the above system is given by
v(t) = v0 exp

α
Z t
0
[µ −y(s)]ds

.
The name comes from the fact that the integral action is exponentiated. Interestingly, this
controller has a form that is reminiscent of the logistic model; see e.g. [5,55]. It also shares
some connection with biochemical models exhibiting the property of Absolute Concentration
Robustness (ACR) [51]. Those networks have species whose stationary values that do not
depend on initial conditions. The connection between Absolute Concentration Robustness
and integral control has been recently clariﬁed in [15].
Remark 33 The controller (96) is only valid when the local DC-gain of the open-loop system
is positive, which is always the case for linear internally positive systems. In the case of
nonlinear internally positive systems, the local DC-gain can be negative and, in such a case,
one should use the controller
˙v(t) = αv(t)(y(t) −µ)
where we have swapped the error terms.
5.2
Main results
We now address the question of the existence of equilibrium points for the closed-loop system
(4)-(96).
Proposition 34 The closed-loop system consisting of the system (4) and the controller (96)
admits two equilibrium points:
(a) the ﬁrst one is the trivial equilibrium point
(x∗, v∗) = (0, 0)
(97)
whereas
(b) the second one is the positive equilibrium point
(x∗, z∗) =
 A−1Bµ
CA−1B ,
−µ
CA−1Bk

(98)
which exists provided that µ > 0.
35


## Page 36


Clearly, the ﬁrst equilibrium is undesirable since it does solve the control problem stated in
Problem 7. Indeed, the output does not track the desired set-point µ unlike in the second
case. The results below show that the ﬁrst equilibrium point is structurally unstable whereas
the second one can be made locally exponentially stable through a suitable choice for the
controller parameters. Let us start ﬁrst with the trivial equilibrium point:
Proposition 35 Let us consider the closed-loop system consisting of the system (4) and the
controller (96). Then, the zero-equilibrium point (97) is unstable for all α, k, µ > 0.
Proof : The linearized system about that equilibrium point is given by
 ˙˜x(t)
˙˜v(t)

=
A
Bk
0
αµ
 ˜x(t)
˜v(t)

(99)
and is obviously unstable since αµ > 0.
♦
While the zero equilibrium point is unstable in the deterministic setting, it actually becomes
an absorbing state in the stochastic setting and, therefore, cannot be used in that setting
unlike the antithetic integral controller.
We address now the stability of the positive equilibrium point:
Proposition 36 Let us consider the closed-loop system consisting of the system (4) and the
controller (96) and let µ > 0 be given. Then, there exists an ¯α > 0 such that the positive
equilibrium point (98) is locally exponentially stable for all k > 0 and all α ∈(0, ¯α) where
¯α := sup
(
ν > 0 :
"
A
B
νµC
CA−1B
0
#
Hurwitz
)
.
(100)
Proof : The linearized system about that equilibrium point is given by
 ˙˜x(t)
˙˜v(t)

=
"
A
Bk
αCµ
CA−1Bk
0
# ˜x(t)
˜v(t)

.
(101)
It is immediate to see that the eigenvalues of the above matrix do not depend on k. Therefore,
we only need to characterize the dependence of the eigenvalues on α, µ > 0. We prove now
using a perturbation argument that the matrix is Hurwitz for some suﬃciently small α > 0.
When α = 0, the resulting matrix has n stable eigenvalues (those of A) and one eigenvalue
at 0. The eigenvalue at 0 has normalized left- and right-eigenvectors given by
uℓ=

01×n
1

, ur =
−A−1B
1

(102)
respectively. The theory of perturbation of eigenvalues says that the zero-eigenvalue locally
changes under the eﬀect of the perturbation of α around α = 0 according to the relation
λ(α) = λ(0) + uℓMurα + o(α) where λ(0) = 0 and
M =
"
0
0
Cµ
CA−1B
0
#
.
36


## Page 37


We therefore obtain that λ(α) = −µα+o(α). This means that by slightly perturbing α from
0 to positive values, we can shift the marginally stable eigenvalue into the open left-half
plane. This means that there exists ¯α > 0 such that for all α < ¯α, the Jacobian matrix is
Hurwitz.
♦
We prove below a robustness result which seems to be speciﬁc to the integral controller
Theorem 37 Assume that the system (4) is internally positive and that it satisﬁes Assump-
tion 5. Assumer further that the system (4) depends on some parameters p = (p1, . . . , pK)
and let ¯p1 = (p1, . . . , pℓ) and ¯p2 = (pℓ+1, . . . , pK) for some 0 < ℓ≤K. Assume further that
the transfer function of the system writes
C(p)(sI −A(p))−1B(p) = G(¯p1) ˜H(s, ¯p2)
(103)
for some function G : Rℓ
≥0 7→R and some transfer function ˜H(s, ¯p2).
Then, the stability of the equilibrium point does not depend on the parameters in ¯p1.
Proof :
The matrix in (101) is Hurwitz stable if and only if the roots of its characteristic
polynomial
P(s, α) := det


sI −A(p)
−B(p)
−
αµC(p)
C(p)A(p)−1B(p)
s

= 0
(104)
are located in the open left half-plane. By virtue of the determinant formula, we have
P(s, α) = det(sI −A(p)) det (s + αµHn(s, ¯p2))
(105)
where Hn(s) is deﬁned as
Hn(s, ¯p2) := −C(p)(sI −A(p))−1B(p)
C(p)A(p)−1B(p)
= G(¯p1) ˜H(s, ¯p2)
G(¯p1) ˜H(0, ¯p2)
=
˜H(s, ¯p2)
˜H(0, ¯p2)
(106)
and is independent ¯p1. Therefore, the stability is independent of those parameters.
♦
The above result generalizes the fact that the stability of the positive equilibrium point
does not depend on the gain of the controller. In this regard, this controller allows arbitrarily
large gain for the system and may be useful for controlling highly sensitive systems. This
will be illustrated in the examples.
5.3
Computing α
The following result proposes a numerical method for computing ¯α:
Proposition 38 Let us consider the closed-loop system consisting of the internally positive
system (4) and the controller (96). Assume further that the system (4) satisﬁes Assumption
5 and deﬁne the real polynomials NR(ω), DR(ω), NI(ω) and DI(ω) as
Hn(jω) := −C(sI −A)−1B
CA−1B
=: NR(ω) + jNI(ω)
DR(ω) + jDI(ω)
(107)
37


## Page 38


and let
Ω:= {ω > 0 : Q(ω) := NI(ω)DI(ω) + NR(ω)DR(ω) = 0} .
(108)
Then, the equilibrium point (98) is locally exponentially stable for all k > 0 and all α ∈
(0, ¯α∞) where
¯α∞:= inf
ω∈Ω
1
µ







DI(ω)ω
NR(ω)
if
NR(ω) ̸= 0
−DR(ω)ω
NI(ω)
if
NI(ω) ̸= 0.
(109)
When the set Ωis empty, then ¯α∞= ∞.
Proof :
The matrix in (101) is Hurwitz stable if and only if the roots of its characteristic
polynomial
P(s, α) := det
" sI −A
−B
−αµC
CA−1B
s
#
= 0
(110)
are located in the open left half-plane. By virtue of the determinant formula, we have
P(s, α) = det(sI −A) det (s + αµHn(s)) = sD(s) + αµNn(s) = 0
(111)
where Hn(s) =: Nn(s)/D(s) is deﬁned in Proposition 38. Therefore, the above polynomial
is Hurwitz stable if and only if P(s, α) does not have zeros in the closed right-half plane. We
use the same approach as for proving Proposition 18 and we view (111) as a multivariate
polynomial. We then look for pairs (ω, α) ∈R2
>0 such that P(jω, α) = 0. Such a pair
exists if and only if ℜ[P(jω, α)] = 0 and ℑ[P(jω, α)] = 0. Expanding those expressions and
combining them in matrix form yields
−ωDI(ω)
NR(ω)
ωDR(ω)
NI(ω)
  1
αµ

= 0.
(112)
Such a vector exists if and only if the matrix is singular and, therefore, if and only if
ωQ(ω) = 0. Since, we do not consider the zero frequency which corresponds to the case
¯α = 0, we are just left with the condition that Q(ω) = 0. The result then follows.
♦
Unlike the antithetic integral controller, the stability conditions depend on the desired set-
point and one cannot make the equilibrium stable for any arbitrarily large set-point for a
given α. However, the stability of the equilibrium will not depend on the gain k as well as all
the parameters exclusively appearing in the DC-gain of the system. This is a consequence
of the fact that the stability condition depends on the normalized transfer function. This
will be illustrated in the examples.
5.4
Disturbance rejection/Perfect adaptation
We characterize here the disturbance rejection properties of the exponential controller. Let
us start with the analysis of the zero equilibrium point:
38


## Page 39


Proposition 39 Assume that d ∈Dµ, then the equilibrium point
(x∗, v∗) =
 −A−1Ed, 0

(113)
is unstable for all α, k, µ > 0.
Proof : The proof is identical to the one of Proposition 35.
♦
The following result states stability conditions for the positive equilibrium point:
Proposition 40 Let µ > 0 be given and assume that d ∈Dµ, then the equilibrium point
(x∗, v∗) =

A−1
B(µ + CA−1Ed)
CA−1B
−Ed

, −µ + CA−1Ed
CA−1Bk

(114)
is locally exponentially stable for all k > 0 and any α ∈(0, ¯αd) where
¯αd
∞=
µ
µ + CA−1Ed ¯α∞≥¯α∞
(115)
where ¯α∞is deﬁned in Proposition 38. Moreover, if α < ¯α∞, then the equilibrium point is
locally exponentially stable for all d ∈Dµ and all k > 0.
Proof : As we have seen before, the equilibrium value of the state does not change the local
linear system. Only the equilibrium value of the state of the integrator matters. Noting that
v∗(d) = v∗(0) + ∆vd where
v∗(0)
=
−µ
CA−1Bk > 0
∆v
=
−CA−1E
CA−1Bk ≤0
(116)
allows us to conclude that v∗(d) ≤v∗(0) for all d ∈Dµ. In this case, the state matrix of the
linearized system becomes

A
Bk
−αv∗(d)C
0

(117)
where we can observe that αv∗(d)C is a decreasing function of d and, therefore, the presence
of the disturbance tends to decrease the loop gain. From the disturbance-free stability result,
we can see that it is enough to rescale the value for ¯α∞to get the new bound, This completes
the proof.
♦
5.5
Examples
Gene expression. We consider again the gene expression system from Section 3.7. In this
case, we have that
Hn(s) =
γ1γ2
(s + γ1)(s + γ2).
(118)
39


## Page 40


Since the system has a relative degree equal to two, then ¯α∞is ﬁnite. The polynomial Q(ω)
is given for this system by
Q(ω) = γ1γ2(ω2 −γ1γ2)
(119)
and, therefore, the only positive root is √γ1γ2. We can verify that
Hn(j√γ1γ2) = −j√γ1γ2
γ1 + γ2
(120)
and is located on the imaginary axis. We then get that
¯α∞= γ1 + γ2
µ
.
(121)
We can see that the stability condition does not depend on k2 as expected from Theorem 37.
As a result, the equilibrium point will be stable for all k2 > 0, this a clear diﬀerence with
the antithetic integral controller which requires that k < ¯k∞= γ1γ2(γ1 +γ2)/k2 is the strong
binding regime. Clearly, if k2 is much larger than γ1γ2(γ1 + γ2), the stability of the system
will not be robust with respect to the controller gain. The exponential controller allows one
to overcome this situation. Minor drawback of the integral controller is that the exponential
rate α needs to be tuned with an a priori maximum value for the reference and its nonlinear
behavior.
For numerical purposes, let us consider the parameters γ1 = 1 h−1, γ2 = 1 h−1, k2 = 1
h−1 as well as k = 1. We obtain the results depicted in Figure 9 and Figure 10 where we
can see the inﬂuence of α on the dynamics of the closed-loop system. The robustness with
respect to the gain of the system is illustrated for various values for k2 is illustrated in Figure
11.
0
10
20
30
40
50
0
0.5
1
1.5
2
2.5
Figure 9: Output of the controlled gene expression system consisting of the system (57) and
the exponential controller (96) for various values for α.
40


## Page 41


0
10
20
30
40
50
0
0.1
0.2
0.3
0.4
Figure 10: State of the exponential controller (96) in closed loop with the gene expression
system consisting of the system (57) for various values for α.
0
10
20
30
40
50
0
1
2
3
4
5
6
Figure 11: Output of the controlled gene expression system consisting of the system (57)
and the exponential controller (96) for various values for k2 and for k = 1, α = 0.5.
Gene expression with protein maturation. Let us consider the gene expression
41


## Page 42


system with protein maturation
˙x1(t)
=
k1 −γ1x1(t)
˙x2(t)
=
k2x1(t) −(γ2 + k3)x2(t)
˙x3(t)
=
k3x2(t) −γ3x3(t).
(122)
where x1, x2 and x3 denote the concentration of mRNA, protein and maturated protein
molecules, respectively. We choose the transcription rate as the control input and the con-
trolled output is the concentration of maturated proteins. This makes the system linear,
stable and positive. Its normalized transfer function Hn(s) is given by
Hn(s) =
γ1γ3(γ2 + k3)
(s + γ1)(s + γ2 + k3)(s + γ3)
(123)
which is readily seen to be independent of k2. Since the above transfer function has relative
degree 3, then ¯α∞is ﬁnite. The associated polynomial Q(ω) is given by
Q(ω) = γ1γ3(γ2 + k3) −ω2(γ1 + γ2 + γ3 + k3)
(124)
from which we can conclude that Q(¯ω) = 0 with ¯ω =
s
γ1γ3(γ2 + k3)
γ1 + γ2 + γ3 + k3
. This ﬁnally yields
the bound
¯α∞= (γ1 + γ3)(γ1 + γ2 + k3)(γ2 + γ3 + k3)
µ(γ1 + γ2 + γ3 + γ3)2
.
(125)
6
Logistic integral control of linear positive systems
We consider here a saturated version of the exponential integral controller, namely the logistic
integral controller. First the model of the logistic integral controller is given. The local
stability of the diﬀerent equilibrium points is then analyzed. Finally, a way to compute the
maximum value of the exponential rate is provided.
6.1
The model
The model of the logistic integral controller is based on the use of the logistic function
ϕ(x) =
β
1 + e−αx, α, β > 0
(126)
as regularizing function. This leads to the following result:
Proposition 41 The logistic integral controller is given by
˙v(t)
=
α
β v(t)(β −v(t))(µ −y(t))
u(t)
=
kv(t)
(127)
42


## Page 43


where k > 0 is the gain of the controller, α > 0 is the exponential rate of the controller
and β > 0 is the saturation bound of the controller. The closed-form solution of the above
system is given by
v(t) =
β
1 + v0 exp

α
Z t
0
[µ −y(s)]ds
.
This model can be viewed as an extension of the exponential model and allows to capture
for the saturation at the value β. This is the reason why we get the additional term β −v(t)
in the controller dynamical expression. . It is important to note here that this controller is
only valid when the local DC-gain of the open-loop system is positive. When it is negative,
the exponential integral controller then takes the form
α
β v(t)(β −v(t))(y(t) −µ).
6.2
Local stability analysis
The use of a logistic integral controller yields a closed-loop system with three equilibrium
points:
Proposition 42 The closed-loop system consisting of the system (4) and the controller (127)
admits three equilibrium points:
(a) the ﬁrst one is the zero equilibrium point
(x∗, v∗) = (0, 0)
(128)
(b) the second one is the saturating equilibrium point
(x∗, z∗) =
 −A−1Bkβ, β

(129)
(c) the third one is the positive equilibrium point
(x∗, z∗) =
 A−1Bµ
CA−1B ,
−µ
CA−1Bk

(130)
which exists provided that 0 < µ ≤−CA−1Bkβ.
Similarly to as in the previous section, the zero and saturating equilibrium points are
undesirable equilibrium points as they do not achieve tracking for the constant set-point for
the controlled output. We prove below that the zero equilibrium point is unstable:
Proposition 43 Let us consider the closed-loop system consisting of the internally positive
system (4) and the controller (127). Assume further that the system (4) satisﬁes Assumption
5 and that µ ∈(0, −CA−1Bkβ). Then the zero-equilibrium point (128) is unstable for all
α, β, k > 0.
43


## Page 44


Proof : The linearized system about that equilibrium point is given by
 ˙˜x(t)
˙˜v(t)

=
A
Bk
0
αµ
 ˜x(t)
˜z(t)

.
(131)
Since αµ > 0, then the equilibrium point is unstable for any α, β, µ, k > 0.
♦
We prove below that the saturating equilibrium point is unstable:
Proposition 44 Let us consider the closed-loop system consisting of the internally positive
system (4) and the controller (127). Assume further that the system (4) satisﬁes Assumption
5 and that µ ∈(0, −CA−1Bkβ). Then, the zero-equilibrium point (129) is unstable for all
α, β, k > 0.
Proof : The linearized system about that equilibrium point is given by
 ˙˜x(t)
˙˜v(t)

=
A
Bk
0
−α(µ + CA−1Bkβ)
 ˜x(t)
˜z(t)

.
(132)
Since µ > −CA−1Bkβ by assumption, then the term −α(µ + CA−1Bkβ) is positive and the
equilibrium point is unstable.
♦
We prove below that the positive equilibrium point is locally exponentially stable provided
that a condition is met:
Proposition 45 Let us consider the closed-loop system consisting of the internally positive
system (4) and the controller (127). Assume further that the system (4) satisﬁes Assumption
5 and that µ ∈(0, −CA−1Bkβ). Then, the equilibrium point (130) is locally exponentially
stable provided that kα ∈(0, ¯ξ) where
¯ξ∞:= sup
(
ν > 0 :
"
A
B
−νβ
4 C
0
#
Hurwitz
)
.
(133)
When the matrix is Hurwitz stable for all ν > 0, then ¯ξ∞= ∞. Moreover, we have that
¯ξ∞= 4¯α∞(µ)µ
gβ
.
(134)
Proof : The linearized system about that equilibrium point is given by
 ˙˜x(t)
˙˜v(t)

=
"
A
Bk
−α
β v∗(β −v∗)C
0
# ˜x(t)
˜z(t)

(135)
where v∗= −µ/CA−1Bk. Since 0 < µ < −CA−1Bkβ, then β −v∗> 0 and therefore
−α
β v∗(β −v∗) < 0. The lower-left term lies in the interval [−αβ/4, 0), therefore if k and α
are chosen such that the matrix
"
A
Bk
−αβ
4 C
0
#
(136)
44


## Page 45


is Hurwitz stable, then we know that for any 0 < µ < −CA−1Bkβ, the equilibrium will be
locally asymptotically stable. A coordinate change yields the result.
♦
6.3
Examples
Gene expression. We consider back the gene expression system (57) and we can compute
¯ξ∞using the formula in Proposition 45 to get that
¯ξ∞= 4γ1γ2(γ1 + γ2)
βk2
.
(137)
0
10
20
30
40
50
0
0.5
1
1.5
2
Figure 12: Output of the controlled gene expression system with protein maturation (122)
with the logistic integral controller (127) for k = 1 and several values for α.
45


## Page 46


0
10
20
30
40
50
0
0.5
1
1.5
2
Figure 13: State of the integrator of the controlled gene expression system with protein
maturation (122) and the logistic integral controller (127) for k = 1 and several values for α.
0
10
20
30
40
50
0
0.5
1
1.5
Figure 14: Output of the controlled gene expression system with protein maturation (122)
with the logistic integral controller (127) for α = 1 and several values for k.
Gene expression with protein maturation. Let us consider back the gene expression
network with protein maturation (122). We can apply the same method as for the exponential
46


## Page 47


integral controller to compute the value of ¯ξ∞. We notably obtain
¯ξ∞= 4
β
γ1γ3(γ1 + γ3)(γ2 + k3)(γ1 + γ2 + k3)(γ2 + γ3 + k3)
k2k3(γ1 + γ2 + γ3 + k3)2
.
(138)
7
Discussion
Two approaches have been presented for the derivation of positive integral controllers. The
ﬁrst one is based on the consideration of an antithetic integral controller previously intro-
duced in [7] in the context of the integral control of biochemical networks. The second one
is based on the use of regularizing functions placed between the output of the controller and
the input of system. Several local stability conditions as well as other qualitative results
have been obtained.
In the present paper, internally positive systems have been extensively considered. How-
ever, the main underlying requirement was that the input and output signals be nonnegative
at all times, which is a weaker property than internal positivity. This property is referred
to as external positivity in the literature and is more diﬃcult to characterize than internal
positivity; see e.g. [?]. In this respect, it might be possible that some of the obtained results
extend to that class of systems. A less straightforward extension of those results would be the
consideration of linear systems having a system matrix having a multiple or not eigenvalue
at zero or, in the nonlinear setting, Jacobian matrix having eigenvalues on the imaginary
axis.
Other interesting extensions of this work include elucidating the question of whether the
equilibrium point of the closed-loop system is also globally asymptotically stable under the
same conditions. An obvious, yet tedious, approach would be the construction of a Lyapunov
function. So, alternative, more generic, approaches may be interesting to consider instead.
The application of the logistic regularizing function to the control of nonlinear polynomial
or rational systems subject to input saturation would also be of interest as this would allow
for the use of eﬃcient algorithms relying, for instance, on sum of squares programming. All
these problems are left for future research.
References
[1] K. J. ˚Astr¨om and T. H¨agglund. PID Controllers: Theory, Design, and Tuning. Instru-
ment Society of America, Research Triangle Park, North Carolina, USA, 1995.
[2] S. Aoki, G. Lillacci, A. Gupta, A. Baumschlager, D. Schweingruber, and M. Khammash.
A universal biomolecular integral feedback controller for robust perfect adaptation. Na-
ture, 570:533–537, 2019.
[3] G. Bengtson. Output regulation and internal models – a frequency domain approach.
Automatica, 13(4):333–345, 1977.
47


## Page 48


[4] A. Berman and R. J. Plemmons. Nonnegative matrices in the mathematical sciences.
SIAM, Philadelphia, USA, 1994.
[5] F. Brauer and C. Castillo-Chavez. Mathematical models in population biology and epi-
demiology. Springer-Verlag New York, 2012.
[6] C. Briat. Robust stability and stabilization of uncertain linear positive systems via
integral linear constraints - L1- and L∞-gains characterizations. International Journal
of Robust and Nonlinear Control, 23(17):1932–1954, 2013.
[7] C. Briat, A. Gupta, and M. Khammash. Antithetic integral feedback ensures robust
perfect adaptation in noisy biomolecular networks. Cell Systems, 2:17–28, 2016.
[8] C. Briat, A. Gupta, and M. Khammash.
Variance reduction for antithetic inte-
gral control of stochastic reaction networks. Journal of the Royal Society: Interface,
15(143):20180079, 2018.
[9] C. Briat and M. Khammash. Computer control of gene expression: Robust setpoint
tracking of protein mean and variance using integral feedback. In 51st IEEE Conference
on Decision and Control, pages 3582–3588, Maui, Hawaii, USA, 2012.
[10] C. Briat and M. Khammash. Integral population control of a quadratic dimerization
process. In 52nd IEEE Conference on Decision and Control, pages 3367–3372, Florence,
Italy, 2013.
[11] C. Briat and M. Khammash. Perfect adaptation and optimal equilibrium productivity
in a simple microbial biofuel metabolic pathway using dynamic integral control. ACS
Synthetic Biology, 7(2):419–431, 2018.
[12] C. Briat and M. Khammash. In-silico proportional-integral moment control stochastic
reaction networks with applications expression (with dimerization). submitted, 2019.
[13] C. Briat, E. A. Yavuz, H. Hjalmarsson, K.-H. Johansson, U. T. J¨onsson, G. Karlsson,
and H. Sandberg. The conservation of information, towards an axiomatized modular
modeling approach to congestion control. IEEE Transactions on Networking, 23(3),
2015.
[14] C. Briat, C. Zechner, and M. Khammash. Design of a synthetic integral feedback circuit:
dynamic analysis and DNA implementation. ACS Synthetic Biology, 5(10):1108–1116,
2016.
[15] D. Cappelletti, A. Gupta, and M. Khammash.
A hidden integral structure endows
absolute concentration robust systems with resilience to dynamical concentration dis-
turbances. arXiv, page 1910.05531, 2019.
48


## Page 49


[16] Y.-J. Chen, N. Dalchau, N. Srinivas, A. Phillips, L. Cardelli, D. Soloveichik, and
G. Seelig. Programmable chemical controllers made from DNA. Nature nanotechnology,
8:755–762, 2013.
[17] M. Chevalier, M. G´omez-Schiavon, A. H. Ng, and H. El-Samad. Design and analysis
of a proportional-integral-derivative controller with biological molecules. Cell Systems,
9:1–16, 2019.
[18] P. G. Coxson and H. Shapiro. Positive input reachability and controllability of positive
systems. Linear Algebra and its Applications, 94:35–53, 1987.
[19] C. Cuba Samaniego and E. Franco. An ultrasensitive biomolecular network for robust
feedback control. In 20th IFAC World Congress, pages 11437–11443, 2017.
[20] D. Del Vecchio, H. Abdallah, Y. Qian, and J. J. Collins. A blueprint for a synthetic
genetic feedback controller to reprogram cell fate. International Journal of Control,
4:1–12, 2017.
[21] D. Del Vecchio, A. J. Dy, and Y. Qian. Control theory meets synthetic biology. Journal
of The Royal Society Interface, 13(120), 2016.
[22] T. Drengstig, X. Y. Ni, K. Thorsen, L. W. Jolma, and P. Ruoﬀ. Robust adaptation and
homeostasis by autocatalysis. The Journal of Physical Chemistry, 116:5355–5363, 2012.
[23] J. Eden, Y. Tan, D. Lau, and D. Oetomo. On the positive output controllability of
linear time invariant systems. Automatica, 71:202–209, 2016.
[24] H. El-Samad, J. P. Goﬀ, and M. Khammash.
Calcium homeostasis and parturient
hypocalcemia: An integral feedback perspective. Journal of Theoretical Biology, 214:17–
29, 2002.
[25] L. Farina and S. Rinaldi. Positive Linear Systems: Theory and Applications. John
Wiley & Sons, 2000.
[26] G. Fjeld, K. Thorsen, T. Drengstig, and P. Ruoﬀ. Performance of homeostatic controller
motifs dealing with perturbations of rapid growth and depletion. The Journal of Physical
Chemistry, 121:6097–6107, 2017.
[27] J. M. Gon¸calves, A. Megretski, and M. D. Dahleh. Global analysis of piecewise linear
systems using impact maps and surface Lyapunov functions. IEEE Transactions on
Automatic Control, 48(12):2089–2106, 2007.
[28] K. Gu, V. L. Kharitonov, and J. Chen. Stability of Time-Delay Systems. Birkh¨auser,
Boston, 2003.
[29] C. Guiver, H. Logemann, R. Rebarber, A. Bill, B. Tenhumberg, D. Hodgson, and
S. Townley.
Integral control for population management.
Journal of Mathematical
Biology, 70:1015–1063, 2015.
49


## Page 50


[30] A. Gupta, C. Briat, and M. Khammash. A scalable computational framework for es-
tablishing long-term behavior of stochastic reaction networks. PLOS Computational
Biology, 10(6):e1003669, 2014.
[31] M. A. Haidekker. Linear Feedback Controls. The Essentials. Elsevier, 2013.
[32] W. P. M. H. Heemels, S. J. L. Van Eijndhoven, and A. A. Stoorvogel. Linear quadratic
regulator problem with positive controls. International Journal of Control, 70(4):551–
578, 1998.
[33] R. Hovorka, V. Canonico, L. Chassin, U. Haueter, M. Massi-Benedetti, M. Orsini Fed-
erici, T. Pieber, H. C Schaller, L. Schaupp, T. Vering, and M. E Wilinska. Nonlinear
model predictive control of glucose concentration in subjects with type 1 diabetes. Phys-
iological Measurement, 25(4):905–920, 2004.
[34] O. Karin, A. Swisa, B. Glaser, Y. Dor, and U. Alon.
Dynamical compensation in
physiological circuits. Molecular Systems Biology, 12:1–7, 2016.
[35] H. K. Khalil. Nonlinear Systems. Prentice-Hall, Upper Saddle River, New Jersey, USA,
2002.
[36] N. Kottenstette, M. J. McCourt, M. Xia, V. Gupta, and P. J. Antsaklis. On relationships
among passivity, positive realness, and dissipativity in linear systems.
Automatica,
50(4):1003–1016, 2014.
[37] H. Leyva and J. Sol´ıs-Daun. Global clf stabilization of systems with respect to a hyper-
box, allowing the null-control input in its boundary (positive controls). In 53rd IEEE
Conference on Decision and Control, pages 3107–3112, Los Angeles, California, USA,
2014.
[38] J. D. Murray. Mathematical Biology Part I. An Introduction. 3rd Edition. Springer-
Verlag Berlin Heidelberg, 2002.
[39] S. I. Niculescu.
Delay eﬀects on stability. A robust control approach, volume 269.
Springer-Verlag: Heidelbeg, 2001.
[40] K. Ogata. Modern control engineering. Prentice Hall, Upper Saddle River, 1970.
[41] K. Oishi and E. Klavins. Biomolecular implementation of linear I/O systems. IET
Systems Biology, 5(4):252–260, 2010.
[42] N. Olsman, A.-A. Baetica, F. Xiao, Y. P. Leong, and R. M. Murray. Hard limits and
performance tradeoﬀs in a class of antithetic integral feedback networks. Cell Systems,
9:1–15, 2019.
[43] N. Olsman, F. Xiao, and J. C. Doyle. Architectural principles for characterizing the
performance of antithetic integral feedback networks. iScience, 14:277–291, 2019.
50


## Page 51


[44] A. Papachristodoulou, J. Anderson, G. Valmorbida, S. Prajna, P. Seiler, and P. A.
Parrilo. SOSTOOLS: Sum of squares optimization toolbox for MATLAB v3.00, 2013.
[45] P. Parrilo. Structured Semideﬁnite Programs and Semialgebraic Geometry Methods in
Robustness and Optimization. PhD thesis, California Institute of Technology, Pasadena,
California, 2000.
[46] V. M. Popov. Absolute stability of nonlinear systems of automatic control. Automa-
tion and Remote Control (Translated from Automatica i Telemekhanika), 22(8):857–875,
1961.
[47] Y. Qian and D. Del Vecchio. Realizing “integral control” in living cells: How to overcome
leaky integration due to dilution? Journal of the Royal Society: Interface, 15:20170902,
2018.
[48] Y. Qian and D. Del Vecchio. A singular singular perturbation problem arising from a
class of biomolecular feedback controllers. IEEE Control Systems Letters, 3(2):236–241,
2019.
[49] S. H. Saperstone. Global controllability of linear systems with positive controls. SIAM
Journal of Control, 11(3):417–423, 1973.
[50] A. P. Seyranian and A. A. Mailybaev. Multiparameter stability theory with mechanical
applications. World Scientiﬁc, Singapore, 2003.
[51] G. Shinar and M. Feinberg. Structural sources of robustness in biochemical reaction
networks. Science, 327:1389–1391, 2010.
[52] R. Shorten, F. Wirth, and D. Leith. A positive systems model of TCP-like congestion
control: asymptotic results. IEEE Transactions on Networking, 14(3):616–629, 2006.
[53] O. Shoval, L. Goentoro, Y. Hart, A. Mayo, E. Sontag, and U. Alon.
Fold-change
detection and scalar symmetry of sensory input ﬁelds. PNAS, 107(36):15995–160000,
2010.
[54] G. Tao and P. A. Ioannou. Necessary and suﬃcient conditions for strictly positive real
matrices. IEE Proceedings, 137(5):360–366, 1990.
[55] P. F. Verhulst. Notice sur la loi que la population suit dans son accroissement (french).
Correspondance math´ematique et physique, 10:113–121, 1938.
[56] F. Xiao and J. C. Doyle. Robust perfect adaptation in biomolecular reaction networks.
BioRxiv, page 299057, 2018.
[57] T.-M. Yi, Y. Huang, M. I. Simon, and J. Doyle. Robust perfect adaptation in bacterial
chemotaxis through integral feedback control. Proceedings of the National Academy of
Sciences, 97(9):4649–4653, 2000.
51


## Page 52


[58] B. Yordanov, J. Kim, R. L. Petersen, A. Shudy, V. V. Kulkarni, and A. Phillips. Com-
putational design of nucleic acid feedback control circuits. ACS Synthetic Biology, 3
(8):600–616, 2014.
52

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
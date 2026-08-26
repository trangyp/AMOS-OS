---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1612.05188v1
source: arxiv
tags: [arxiv, fractal, knowledge, quantum, reference]
---
# 1612.05188v1_Investigation_of_a_Structured_Fisher_s_Equation_with_Applications_in_Biochemistr

> Source: 1612.05188v1_Investigation_of_a_Structured_Fisher_s_Equation_with_Applications_in_Biochemistr.pdf

> Pages: 28

---


## Page 1


Investigation of a Structured Fisher’s Equation
with Applications in Biochemistry
John T. Nardini∗, D.M. Bortz∗
July 8, 2021
Abstract
Recent biological research has sought to understand how biochemical
signaling pathways, such as the mitogen-activated protein kinase (MAPK)
family, inﬂuence the migration of a population of cells during wound heal-
ing. Fisher’s Equation has been used extensively to model experimental
wound healing assays due to its simple nature and known traveling wave
solutions. This partial diﬀerential equation with independent variables
of time and space cannot account for the eﬀects of biochemical activity
on wound healing, however. To this end, we derive a structured Fisher’s
Equation with independent variables of time, space, and biochemical path-
way activity level and prove the existence of a self-similar traveling wave
solution to this equation. We also consider a more complicated model
with diﬀerent phenotypes based on MAPK activation and numerically in-
vestigate how various temporal patterns of biochemical activity can lead
to increased and decreased rates of population migration.
keywords: Stage-structure, Traveling Wave Solutions, Wound Healing, Bio-
chemical Signaling Pathways
1
Introduction
Traveling wave solutions to partial diﬀerential equations (PDEs) are often used
to study the collective migration of a population of cells during wound heal-
ing [5, 11, 26, 27, 29], tumorigenesis [25], and angiogenesis [40, 43]. R.A. Fisher
introduced what is now referred to as Fisher’s Equation in 1937 to model the ad-
vance of an advantageous gene in a population [14]. Since then, it has been used
extensively in math biology literature to model the migration of a monolayer of
cells during experimental wound healing assays [5, 20, 29].
Fisher’s Equation is written as
ut = Duxx + λu(K −u)
(1)
∗Department of Applied Mathematics, University of Colorado, Boulder 80309-0526, United
States (john.nardini@colorado.edu, dmbortz@colorado.edu)
1
arXiv:1612.05188v1  [math.AP]  15 Dec 2016


## Page 2


with subscripts denoting diﬀerentiation with respect to that variable and u =
u(t, x) representing a population of cells over time t at spatial location x. The
ﬁrst term on the right hand side of (1) represents diﬀusion in space with rate of
diﬀusion, D, and the second term represents logistic growth of the population
with proliferation rate, λ, and carrying capacity, K. As shown in [35, § 11.2],
(1) admits traveling wave solutions of the form
u(t, x) = U(z), z = x −ct
where c denotes the speed of the traveling wave solution and U(z) denotes
the traveling wave proﬁle.
Traveling wave solutions to (1) thus maintain a
constant proﬁle, U(z), over time that moves leftward if c < 0 or rightward if
c > 0 with speed |c|. It is also shown that (1) has a positive and monotonic
proﬁle for |c| ≥2
√
Dλ, which is biologically relevant when u(t, x) denotes a
population of cells. Kolmogoroﬀproved in 1937 that any solution to (1) with a
compactly-supported initial condition will converge to a traveling wave solution
with minimum wavespeed c = 2
√
Dλ [24]. See [34, § 5.4] for a proof of this.
There is also a wide literature on studies into extensions of Fisher’s Equation,
such as Fisher’s Equation coupled with chemotaxis [2, 26], time-dependent rates
of proliferation and diﬀusion [18], and space-dependent rates of diﬀusion [9].
Structured population models, or PDE models with independent variables
to distinguish individuals by some continuously-varying properties, were ﬁrst
investigated via age-structured models in the early 20th century [32, 42]. The
1970s saw a revival in structured population modeling after the introduction
of methods to investigate nonlinear structured population models [17], which
led to our current understanding of semigroup theory for linear and nonlinear
operators on Banach spaces [50]. Several recent biological studies have demon-
strated the existence of traveling wave solutions to structured population models
[12, 13, 15, 45], and another study used an independent variable representing
subcellular β-catenin concentration to investigate how signaling mutations can
cause intestinal crypts to invade healthy neighboring crypts [36].
Recent biological research has focused on the inﬂuence of biochemical sig-
naling pathways on the migration of a population of cells during wound healing.
Particular emphasis has been placed on the mitogen-activated protein kinase
(MAPK) signaling cascade, which elicits interesting patterns of activation and
migration in response to diﬀerent types of cytokines and growth factors in var-
ious cell lines [7, 31]. For example, experimental wounding assays of madine
darby canine kidney cells (MDCKs) in [31] yielded a transient pulse of ERK
1/2 (a speciﬁc MAPK protein) activity in the cell sheet that only lasted for
a few minutes. This pulse of activity was followed by a slow wave of activity
that propagated from the wound margin to submarginal cells over the course
of several hours. The second wave was determined to be crucial for regulating
MDCK sheet migration. The authors of [31] proposed that these fast and slow
waves of ERK 1/2 activity could be caused by the production of reactive oxygen
species (ROS) and epidermal growth factor (EGF), respectively. Similar exper-
iments with ﬁbroblasts also demonstrated this ﬁrst transient wave of ERK 1/2
2


## Page 3


activity, but not the following slow wave. The authors of [7] found that human
keratinocyte (HaCaT) cells exhibit ERK 1/2 activity primarily at the wound
margin during similar experimental wound healing assays with a high density
in response to treatment with transforming growth factor-β (TGF-β).
In this study, we detail an approach to investigate a structured version of
Fisher’s Equation that is motivated by the above experimental observations.
Previous structured population models have been restricted to traits that pri-
marily increase over time, such as age or size, but our analysis allows for both
activation and deactivation along the biochemical activity dimension.
In Section 2, we develop our structured population model and devote Section
3 to a review of relevant material from size-structured population models. We
demonstrate the existence of self-similar traveling wave solutions to the model
in Section 4. We then study a more complicated version of our model where
migration and proliferation of the population depend on MAPK activity levels in
Section 5 before making ﬁnal conclusions and discussing future work in Section
6.
2
Model Development
We model a cell population during migration into a wound, denoted by
u(t, x, m), for
u : [0, ∞) × R × [m0, m1] →R
where t denotes time, x denotes spatial location, and m denotes activation along
a biochemical signaling pathway with minimum and maximum levels m0 and
m1, respectively. As a ﬁrst pass, we assume that any cells of the same MAPK
activity level will activate identically over time in the same environment. This
assumption allows us to model the activation distribution of the population over
time deterministically by considering how cells of all possible MAPK activity
levels activate and deactivate over time. We note that biochemical signaling
is an inherently heterogeneous process, so our approach would beneﬁt from a
further investigation with stochastic diﬀerential equations.
As discussed in [10], crucial aspects of a structured population model include
the individual state, the environmental state, external forcing factors, and feed-
back functions. The individual state is a dimension used to distinguish between
individuals of a population and is typically based on physiological properties
such as age or size. As activation of biochemical signaling pathways inﬂuences
cell migration through diﬀusive and proliferative properties of cells, we incor-
porate the biochemical activity dimension, m, as an individual state for our
model.
The environmental state of a population is the external factors that inﬂuence
individual behavior. Recall that external cytokines and growth factors, such as
ROS, TGF-β, and EGF, inﬂuence activation of the MAPK signaling cascade
and promote migration during wound healing.
The cell population will not
directly aﬀect the level of external growth factor in this work, so an external
forcing factor will be used to represent treatment with these chemicals here.
3


## Page 4


The external chemical concentration at time t will be denoted by s(t), and the
activation response of cells to this chemical will be given by the function f(s).
A feedback function included in our work will be the inhibition of individual
cell proliferation in response to a conﬂuent density. As proliferation is hindered
by contact inhibition, we introduce a new variable,
w(t, x) :=
ˆ m1
m0
u(t, x, m)dm
(2)
to represent the population of cells at time t and spatial location x. Proliferation
of the population will accordingly vanish as w(t, x) approaches the carrying
capacity, K.
Our model, which we term as a structured Fisher’s Equation, is given by the
PDE:
ut + (f(s(t))g(m)u)m
|
{z
}
activation
=
D(m)uxx
|
{z
}
diffusion
+ λ(m)u (K −w(t, x))
|
{z
}
population growth
(3)
w(t, x)
=
ˆ m1
m0
u(t, x, m)dm
u(t = 0, x, m)
=
φ(x, m)
u(t, x, m = m1)
=
0
w(t, −∞) = K
w(t, x = +∞) = 0
The function g(m) ∈C1 ([m0, m1]) denotes the rate of biochemical activation
in the population, s(t) ∈L∞(R+) denotes the external chemical concentration
in the population, f(s) ∈L1
loc(0, ∞) denotes the activation response of cells
to the level of signaling factor present, D(m) and λ(m) denote biochemically-
dependent rates of cell diﬀusion and proliferation, and φ(x, m) denotes the initial
condition of u. The spatial boundary conditions specify that the cell density
has a conﬂuent density at x = −∞and an empty wound space at x = +∞.
We use a no ﬂux boundary condition at m = m1 so that cells cannot pass
this boundary. In the remainder of this study, we will write f(s(t)) as f(t) for
simplicity, though we note that this function will diﬀer between cell lines that
respond diﬀerently to the same chemical during wound healing1.
The solution space of (3), D, is deﬁned with inspiration from [50] and [49, §
1.1]. If we let Z denote the space of bounded and twice continuously diﬀeren-
tiable functions on R, then we deﬁne
D :=

u(t, x, m)

ˆ m1
m0
u(t, x, m)dm ∈Z

,
i.e., u(t, x, m) ∈D if w(t, x) ∈Z for all t > 0. We note that
´ m1
m0 φ(x, m)dm need
only be bounded and piecewise continuous with a ﬁnite number of discontinuities
1Note that an extension for modeling the dynamics governing s(t) will be considered in a
future study.
4


## Page 5


[49]. If φ(x, m) is not suﬃciently smooth in m, we obtain generalized solutions
of (3) [50].
In Section 4, we will investigate (3) with constant rates of diﬀusion and
proliferation (i.e., D(m) = D, λ(m) = λ) and f(t) = 1. By substituting
u∗= u/K,
t∗= λKt,
x∗= x
p
λK/D,
m∗= (m −m0)/(m1 −m0),
g∗(m∗) =
g(m∗(m1 −m0) + m0)/(λKm1),
and dropping asterisks for simplicity, (3) can be non-dimensionalized to
ut + (f(t)g(m)u)m
|
{z
}
activation
=
uxx
|{z}
diffusion
+ u

1 −
ˆ 1
0
u(t, x, m)dm

|
{z
}
population growth
(4)
w(t, x)
=
ˆ 1
0
u(t, x, m)dm
u(t = 0, x, m)
=
φ(x, m)
u(t, x, m = 1)
=
0
w(t, x = −∞) = 1
w(t, x = +∞) = 0.
In Section 5, we will consider the full model (3) when the rates of cellular dif-
fusion and proliferation are piece-wise constant functions of m and numerically
investigate how diﬀerent functions for f(t) lead to increased and decreased levels
of population migration.
3
Background Material from Size-Structured
Population Modeling
Before investigating the existence of traveling-wave solutions to (4), it is useful
to review some key topics used to solve size-structured population models, as
discussed in [50]. These topics will be useful in analyzing (3) in later sections. A
reader familiar with using the method of characteristics to solve size-structured
population models may brieﬂy skim over this section to pick up on the notation
used throughout our study.
As an example, we consider the size-structured model given by
ut + (g(y)u)y
=
Au
(5)
u(t = 0, y)
=
φ(y)
where u = u(t, y) : [0, ∞) × [y0, y1] →R denotes the size distribution over y of a
population at time t, y0 and y1 denote the minimum and maximum population
sizes respectively, and g(y) ∈C1(([y, y1]) denotes the physical growth rate2
2Note that in this section, g(y) denotes a growth rate with respect to size, y, whereas
throughout the rest of our study, g(m) denotes an activation rate with respect to biochemical
activity, m.
5


## Page 6


of individuals of size y.
In this section, we will work in the Banach space
X = L1((y0, y1) →R), and assume A ∈B(X), the space of bounded, linear
operators on X. The method of characteristics will facilitate solving (5).
For a ﬁxed size y ∈[y0, y1], the function
σ(y; y) :=
ˆ y
y
1
g(y′)dy′
(6)
provides the time it takes for an individual to grow from the ﬁxed size y to
arbitrary size y. If g(y) is positive and uniformly continuous on [y0, y1], then
σ(y; y) is invertible. We denote the inverse function, σ−1(t; y), as the growth
curve, and it computes the size of an individual over time that starts at size
y at time t = 0. For instance, if an individual has size y at t = 0, then that
individual will have size σ−1(t1; y) at time t = t1. Some helpful properties of
the growth curve are that σ−1(0; y) = y and
d
dtσ−1(t; y) = g(σ−1(t; y)).
(7)
See Section A in the appendix for the derivation of (7).
In order to solve (5) with the method of characteristics, we set y = σ−1(t; y)
to deﬁne the variable v(t; y):
v(t; y) := u(t, y = σ−1(t; y)).
(8)
As shown in Section B of the appendix, substitution of (8) into (5) yields the
characteristic equation
vt = −g′(σ−1(t; y))v + Av,
(9)
where primes denote diﬀerentiation with respect to y. This characteristic equa-
tion has size y at time t = 0 and can be solved explicitly as3
v(t; y) =
g(y)
g(σ−1(t; y))eAtφ(y).
(10)
As (10) provides the solution to (5) along the arbitrary characteristic curve
with initial size y, we use it to solve the whole equation with the substitution
y = σ−1(t, y), in which we ﬁnd
u(t, y) =
(
g(σ−1(−t,y))
g(y)
eAtφ(σ−1(−t, y))
σ−1(t; y0) ≤y ≤y1
0
y0 ≤y < σ−1(t; y0).
(11)
If φ(y) /∈C1(y0, y1), then (11) is viewed as a generalized solution. Note that a
piecewise form is needed for (11) because we do not have any individuals below
3To derive this,
use separation of variables and with the help of
(7) note that
´ t
0 g′(σ−1(τ; y))dτ = ln[g(σ−1(t; y))/g(y)].
6


## Page 7


the minimum size, y0, and thus the minimum possible size at time t is given
by σ−1(t; y0). If the population is assumed to give birth to individuals of size
y0 over time, then the appropriate renewal equation representing population
birth would replace the zero term in the piecewise function (see [3, § 9.5] for an
example in size-structured populations and [15] for an example in age-structured
populations).
4
Existence of Traveling Wave Solutions to the
Structured Fisher’s Equation
4.1
Existence of traveling wave solutions to (4)
We now incorporate topics from the previous section to show the existence of
traveling wave solutions to (4). After taking the time derivative of w(t, x), which
was deﬁned in (2), we can rewrite (4) as a system of two coupled PDEs4:
ut + (g(m)u)m
=
uxx + u(1 −w)
wt
=
wxx + w(1 −w).
(12)
Note that in this section, g(m) is a function of biochemical activity level and
σ−1(t; m) computes the activity level of an individual over time that starts at
level m at time t = 0. We will thus now refer to σ−1(t; m) as the activation
curve. We next set up the characteristic equation for u by setting m = σ−1(t; m)
for a ﬁxed value of m:
v(t, x; m) := u(t, x, m = σ−1(t; m)).
(13)
Substituting (13) into (12) simpliﬁes to our characteristic equation
vt
=
vxx + v[1 −w −g′(σ−1(t; m))]
wt
=
wxx + w(1 −w),
(14)
a nonautonomous system of two coupled PDEs in time and space. Note that
the bottom equation for (14) is Fisher’s Equation, which has positive monotonic
traveling wave solutions for any speed c ≥2 (see [35, § 11.2]).
We next aim to derive traveling wave solutions to (14), however, we are not
aware of any traveling wave solutions to nonautonomous systems such as this
one. From our knowledge of size-structured population models from Section 3,
we instead intuit the ansatz of a self-similar traveling wave solution, which we
write as
v(t, x; m)
=
g(m)
g(σ−1(t; m))V (z), z = x −ct
(15)
w(t, x)
=
W(z).
4Note that either g(m0) = 0 or u(t, m = m0, x) = 0 for t > 0, so that the activation term
drops out when integrating over m for w.
7


## Page 8


In this ansatz, V (z) will deﬁne a traveling wave proﬁle for v and
g(m)
g(σ−1(t;m)) will
provide the height of the function over time. With the aid of the chain rule, we
observe that:
vt(t, x; m)
=
g′(σ−1(t; m))g(σ−1(t; m))
g(m)
V −cg(σ−1(t; m))
g(m)
Vz
vxx(t, x; m)
=
g(σ−1(t; m))
g(m)
Vzz,
where subscripts denote diﬀerentiation with respect to t, x, or z and primes
denote diﬀerentiation with respect to m. Substituting (15) into (14) reduces to
the autonomous system
−cVz
=
Vzz + V (1 −W)
−cWz
=
Wzz + W(1 −W).
(16)
It is now useful to rewrite (16) as the ﬁrst order system
d
dz V =




Vz
−cVz −V (1 −W)
Wz
−cWz −W(1 −W)




(17)
for V(z) = [V (z), Vz(z), W(z), Wz(z)]T . Recall that proﬁles to traveling wave
solutions can be constructed with heteroclinic orbits between equilibria for a
given dynamical system (or homoclinic orbits for a traveling pulse) [22, § 6.2].
We observe two types of equilibria for (16), given by V∗
1 = (1, 0, V, 0)T and
V∗
2 = ⃗0, where the former represents a conﬂuent cell density and the latter
represents an empty wound space. We accordingly search for heteroclinic orbits
from V∗
1 to V∗
2 for some c > 0. We choose to focus on the characteristic equations
v(t, x, m = σ−1(t; m)) for values of m in which φ(m, x = −∞) > 0 to represent
the population of cells migrating into the empty wound space. We thus denote
V∗
1 = (1, 0, ν, 0)T for ν > 0.
Note that V∗
1 is an equilibrium for any value of V, as W = 1 will guarantee
the existence of an equilibrium.
Such a “continuum” of equilibria was also
observed in [39]. This structure of V∗
1 yields a zero eigenvalue after linearizing
(17) about V∗
1, so we cannot use linear theory to study the local behavior of (17)
near V∗
1. While we could construct the unstable manifold of (17) using a power
series representation to study its local behavior around V∗
1 (see [33, Section
5.6]), we ﬁnd it more insightful to deﬁne a trapping region in the (V, Vz)-plane
as has been done in previous traveling wave studies [2, 25]. We will then use
asymptotically autonomous phase-plane theory to describe the ω-limit set of
our ﬂow, which will show the existence of a heteroclinic orbit from V∗
1 to V∗
2.
Trapping regions are positively invariant regions with respect to the ﬂow of a
dynamical system, and the ω-limit set of a ﬂow is the collection all limit point
of that ﬂow [33, § 4.9-10].
8


## Page 9


We study the trajectory of V in the (V, Vz)-plane by deﬁning the triangular
region bound by the lines {V = ν, Vz = 0, Vz = −c
2V } and denoting this region
as ∆. The following lemma will demonstrate that ∆is a trapping region for the
ﬂow of (17) in the (V, Vz)-plane.
Lemma: Let ν > 0 and c ≥2. Then the region ∆is positively invariant
with respect to (17) so long as 0 < W(z) < 1 for all z ∈R.
Proof:
We prove this lemma by investigating the vector ﬁeld along each of the lines
specifying the boundary of our region and showing that they point into the
interior of the space.
i.) Along the line Vz = 0,
d
dzVz = −V (1 −W), which is nonpositive because
W(z) < 1 for all z ∈R and our region is deﬁned for V (z) ≥0. If V = 0,then we
are at the equilibrium point (V, Vz) = (0, 0).
ii.) Along V = ν,
d
dzV = Vz, which is negative in our deﬁned region. The
only point to worry about here is at (V, Vz) = (ν, 0), as then
d
dzV = 0. However,
we see from part i.) that
d
dzVz < 0 here, so that a ﬂow starting at (ν, 0) will
initially move perpendicular to the V -axis in the negative Vz direction, and then
d
dzV < 0, so the ﬂow enters ∆.
iii.) Note that the inner normal vector to the line Vz = −c
2V is ˆn =
  c
2, 1

.
Then
ˆn · d
dz (V, Vz)
=
 c
2, 1

· (Vz, −cVz −V + V W)
=
 c
2, 1

· (−c
2V, c2
2 V −V + V W)
=
−c2
4 V + c2
2 V −V + V W
=
V
c2
4 −1

+ V W,
which is positive, as c ≥2.□
This proof is visually demonstrated in the top row of Figure 1. As W(z)
has a heteroclinic orbit with W(−∞) = 1 and W(∞) = 0 for any c ≥2 [35, §
11.2], we conclude that ∆is a positively invariant set for the ﬂow of (17) in the
(V, Vz). The following corollary describes the ω-limit set of (17).
Corollary: The ω-limit set of (17) starting at V∗
2 , ω(V∗
2), is V∗
1.
Proof:
As W(z) →0 as z →+∞, then the vector ﬁeld for (17) in the (V, Vz)-plane
is asymptotically autonomous to the vector ﬁeld
d
dz

V
Vz

=

Vz
−cVz −V

,
(18)
a linear system whose only equilibrium is the origin. As c ≥2, the origin is a
stable equilibrium and the ﬂow of the limiting system remains in ∆, and hence
the fourth quadrant, for all time.
9


## Page 10


0
/2
-c /2
-c /4
0
(a)
0
/2
-c /2
-c /4
0
(b)
0
0.2
0.4
0.6
0.8
1
-0.2
-0.1
0
0.1
(c)
0
/2
-c /2
-c /4
0
(d)
Trapping region
V orbit
Figure 1: Construction of the heteroclinic orbit between V∗
1 and V∗
2 for (17).
In (a) and (b), we depict the trapping region in the (V, Vz)-plane, ∆, and the
vector ﬁeld along its boundary for α = 0.5, c = 2.3, Wz = 0 and W near 0
and 1, respectively. In (c) and (d), we depict numerical simulations of (17)
in the (W, Wz)-plane and in the (V, Vz)-plane, respectively. Arrows denote the
direction of the ﬂow and the black dots mark equilibria of (17).
As d/dzV = Vz < 0 in ∆, no periodic or homoclinic orbits can exist for the lim-
iting system. We thus conclude from the asymptotically autonomous Poincare-
Bendixson Theorem presented in [30]5 that our ﬂow in the (V, Vz) plane starting
at (ν, 0) will limit to the origin. We conclude that ω(V∗
2) = V∗
1.□
4.2
Summary of results
We have demonstrated the existence of self-similar traveling wave solutions to
(4) in this section of the form
u(t, x, m)
=
g(m)
g(σ−1(t; m))V (z; m), z = x −ct
for c ≥2 and values of m where the initial condition φ(x = −∞, m) > 0 and
V (z; m) = u(x −ct, m = σ−1(t; m)). Setting m = σ−1(t, m), then this can be
5The relevant theorem statement is given in Appendix C. We note that while the results
of [30] are suﬃcient for our study, asymptotically autonomous systems have been more exten-
sively studied in [4, 6, 47, 48] and a more comprehensive result in describing the ω-limit set
of the asymptotically autonomous ﬂow is given in [48].
10


## Page 11


written more explicitly as
u(t, x, m) =
(
g(σ−1(−t,m))
g(m)
V (z; σ−1(−t; m)),
σ−1(t; 0) ≤m < 1
0
otherwise
and
ˆ 1
0
u(t, x, m)dm = w(t, x) = W(z)
where [V (z; m), W(z)]T satisﬁes (16). An example height function g(σ−1(−t,m))
g(m)
for trajectories along the activation curves m = σ−1(t; m) will be demonstrated
later in Figure 3.
5
Structured Fisher’s Equation with MAPK-
dependent Phenotype
We now study a version of Fisher’s Equation where cellular migration and pro-
liferation depend on biochemical activity, m. Various cell lines have reduced
rates of proliferation and increased migration in response to MAPK activation
[7, 8, 31], so we let m denote activity along the MAPK signaling cascade in
this section. We consider a model with two subpopulations: one with a high
rate of diﬀusion in response to MAPK activation and the other with a high rate
of proliferation when MAPK levels are low. MAPK activation will depend on
an external forcing factor to represent the presence of an extracellular signaling
chemical, such as ROS, TGF-β, or EGF. While the method of characteristics is
not applicable to spatial activation patterning here due to the parabolic nature
of (3) in space, we can investigate temporal patterns of activation and deactiva-
tion. We will exhibit simple scenarios that give rise to three ubiquitous patterns
of biochemical activity: 1.) a sustained wave of activation, 2.) a single pulse of
activitation, and 3.) periodic pulses of activation.
Before describing these examples, we ﬁrst introduce some tools to facilitate
our study of (3). We will detail some assumptions that simplify our analysis in
Section 5.1, solve and compute the population activation proﬁle over time and
use it to deﬁne some activation criteria in Section 5.2, and discuss numerical
issues and the derivation of a nonautonomous averaged Fisher’s Equation in
Section 5.3 before illustrating the diﬀerent activation patterns and their eﬀects
on migration in Section 5.4.
5.1
Model Description
Recall that the full structured Fisher’s Equation is given by
11


## Page 12


ut + (f(t)g(m)u)m
=
D(m)uxx + λ(m)u (1 −w)
(19)
w
=
ˆ m1
m0
u(t, x, m)dm
u(t = 0, x, m)
=
φ1(m)φ2(x)
u(t, x, m = m1)
=
0
w(t, x = +∞) = 0
w(t, x = −∞) = 1.
We have chosen the separable initial condition u(t = 0, x, m) = φ1(m)φ2(x)
for simplicity. Given some mcrit ∈(m0, m1), we deﬁne two subsets of [m0, m1]
as Minact := [m0, mcrit], Mact := (mcrit, m1], and the rates of diﬀusion and
proliferation by
D(m) :=
 D1
m ∈Minact
D2
m ∈Mact
, λ(m) :=
 λ1
m ∈Minact
λ2
m ∈Mact
(20)
for D1 < D2 and λ2 < λ1. Hence for m ∈Minact, the population is termed
as inactive and primarily proliferates whereas for m ∈Mact, the population is
termed as active and primarily diﬀuses.
We let supp(φ1(m)) = [mmin, mmax] for mmax < mcrit and assume that
´ m1
m0 φ1(m)dm = 1 so φ1(m) represents a probability density function for the
initial distribution of cells in m. We accordingly denote
Φ1(m) :=



0
m ≤m0
´ m
m0 φ1(m′)dm′
m0 < m ≤m1
1
m1 < m
as the cumulative distribution function for φ1(m).
5.2
Activation Proﬁle and Activation Criteria
An interesting question is how the distribution of (19) along m changes over
time. To answer this question, we consider (19) in terms of t and m, which we
will write as p(t, m) and call the activation proﬁle:
pt + (f(t)g(m)p)m
=
0
(21)
p(0, m)
=
φ1(m).
Following the analysis from Section 3, we can solve (21) analytically. We inte-
grate (21) along the activation curves, h(t; m), which now are given by
m = h(t; m) := σ−1 (F(t); m) ,
(22)
where F(t) :=
´ t
0 f(τ)dτ denotes a cumulative activation function. We ﬁnd the
activation proﬁle to be:
p(t, m) =
(
g(σ−1(−F (t),m))
g(m)
φ1(σ−1(−F(t), m))
h(t; m0) ≤m ≤m1
0
m0 ≤m < h(t; m0).
(23)
12


## Page 13


Now we can derive a condition for a cell population starting in the inactive
population to enter the active population. We see from (23) that the population
will enter the active population if
h(t; mmax) > mcrit ⇐⇒F(t) > σ(mcrit; mmax)
(24)
for some values of t. By standard calculus arguments, (24) will occur if
F(tmax) > σ(mcrit; mmax)
(25)
where a local maximum for F(t) occurs at t = tmax.
Hence, f(tmax) = 0,
f(t−
max) > 0, and f(t+
max) < 0. We denote (25) as the activation criterion for
(19). By the same argument, for the entire population to activate at some point,
then we can derive the entire activation criterion as
F(tmax) > σ(mcrit; mmin).
(26)
5.3
Numerical Simulation Issues and Derivation of an Av-
eraged Nonautonomous Fisher’s Equation
We depict the u = 1 isocline for a numerical simulation of (19) in Figure 2 with
g(m) = αm(1 −m), f(t) = β sin(γt), α = 1/2, β = 1, and γ = 1.615. These
terms will be detailed more in Example 3 below. For numerical implementation,
we use a standard central diﬀerence scheme for numerical integration along the
x-dimension, an upwind scheme with ﬂux limiters (similar to those described
in [46]) to integrate along the m dimension, and a Crank-Nicholson scheme to
integrate along time. From (25), we see that this simulation should not enter
the active population with an initial condition of φ1(m) = 10/3I[.05,0.35](m),
where IM(m) denotes an indicator function with support for m ∈M. In Figure
2, however, we observe that the numerical simulation does enter the active
population, which causes a signiﬁcant portion of the population to incorrectly
diﬀuse into the wound at a high rate.
Numerical simulations of advection-driven processes have been described as
an “embarrassingly diﬃcult” task, and one such problem is the presence of
numerical diﬀusion [28, 46]. Numerical diﬀusion along the m-dimension is hard
to avoid and here causes a portion of the cell population to enter the active
population in situations where the it should approach the m = mcrit plane but
not pass it. Numerical diﬀusion can be reduced with a ﬁner grid, but this can
lead to excessively long computation times. With the aid of the activation curves
given by (22), however, we can track progression of cells in the m-dimension
analytically and avoid the problems caused by numerical diﬀusion completely.
To avoid the problems caused by numerical diﬀusion, we derive a nonau-
tonomous Fisher’s Equation for w(t, x) that represents the average behavior
along m with time-dependent diﬀusion and proliferation terms. To investigate
the averaged cell population behavior along m over time, we integrate (19) over
m to ﬁnd
wt(t, x)
=
(D1wxx + λ1w(1 −w)) I[Minact](m)
+ (D2wxx + λ2w(1 −w)) I[Mact](m).
(27)
13


## Page 14


(a)
(b)
Figure 2: Two views of the isocline for u = 1 from a numerical simulation
of (19) with g(m) = αm(1 −m) and f(t) = β sin(γt) for α = 0.5, β = 1,
γ = 1.615, D1 = 0.01, D2 = 1, λ1 = 0.25, and λ2 = 0.0025 and an initial
condition of φ1(m) = 10/3I[.05,0.35](m) and φ2(x) = I[x≤5](x). The numerical
scheme is discussed in Section 5.3 and the step sizes used are ∆m = 1/80, ∆x =
1/5, ∆t = 10−3. From (25), the simulation should not cross the m = mcrit plane,
which is given by the red plane. We see in frame (a) that the simulation does
cross the m = mcrit plane due to numerical diﬀusion, which causes the high
rate of diﬀusion along x seen in frame (b).
An explicit form for (27) thus requires determining how much of the population
is in the active and inactive populations over time. This is determined with the
activation curves by calculating
h(t; m) < mcrit
⇐⇒
F(t) < σ(mcrit; m)
⇐⇒
m < σ−1 (−F(t); mcrit) =: ψ(t).
(28)
Thus, m = σ−1(−F(t); m) maps the distribution along m at time t back to the
initial distribution, φ1(m), and ψ(t) denotes the threshold value in m between
the active and inactive populations over time. Φ1(ψ(t)) thus denotes the portion
of the population in the inactive population, and 1−Φ1(ψ(t)) denotes the portion
in the active population over time.
We thus derive a nonautonomous PDE for w, which we will term the averaged
nonautonomous Fisher’s Equation, as:
wt
=
D(t)wxx + λ(t)w(1 −w),
(29)
w(t = 0, x)
=
φ2(x)
w(t, x = −∞) = 1
w(t, x = ∞) = 0
where
D(t)
=
D2 + (D1 −D2)Φ1(ψ(t))
λ(t)
=
λ2 + (λ1 −λ2)Φ1(ψ(t)).
14


## Page 15


5.4
Three biologically-motivated examples
We next consider three examples of (19) that pertain to common patterns of
biochemical activity during wound healing. We will use numerical simulations
of (29) to investigate how diﬀerent patterns of activation and deactivation over
time aﬀect the averaged cell population proﬁle. We will also investigate how
the proﬁle changes when crossing the activation and entire activation thresholds
derived in (25) and (26). In each example, we ﬁx mcrit = 0.5, D1 = 0.01, D2 =
1, λ1 = .25, λ2 = 0.0025, φ1(m) = 10/3I[.05,0.25](m), φ2(x) = I(−∞,5](x) and
g(m) = αm(1−m), and use a diﬀerent terms for f(t) to mimic diﬀerent biological
situations.
The choice for g(m) ensures that the distribution along m stays
between m = 0 and m = 1. A standard central diﬀerence scheme is used for
numerical simulations of (29).
Example 1: Single Sustained MAPK activation wave: f(t) = 1
In this example, we consider a case where we observe the entire cell population
approach a level of m = 1 over time. Such a scenario may represent the sustained
wave of ERK 1/2 activity observed in MDCK cells from [31]. The authors of
[41] proposed that the autocrine production of EGF caused this activation in
the population. We use f(t) = 1 to observe this behavior.
Using (6) and (28), we ﬁnd
σ(m; m)
=
1
α log

m
1 −m
1 −m
m

; m, m ∈(0, 1)
h(t; m)
=
σ−1(t; m) = m
 (1 −m)e−αt + m
−1
ψ(t)
=
(1 + eαt)−1
These functions demonstrate that the distribution along m is always activating
along m but never reaches the m = 1 line, as σ(m; m) →∞as m →1−for
any m ∈(0, 1). The entire population (excluding m = 0) approaches m = 1
asymptotically, however, as limt→∞σ−1(t; m) = 1. In Figure 3, we use (23) to
depict the activation proﬁle, p(t, m), over time to show the activation behavior
of the population. As expected, we observe the entire population converging
to m = 1. We include some speciﬁc plots of the activation curves, h(t; m), for
this example. Note that the density changes along these curves by the height
function g(σ−1(−F (t),m))
g(m)
, which is equivalent to the height function of the self-
similar traveling wave ansatz made in (15).
In Figure 4(a), we depict a numerical simulation of w(t, x) over time using
(29). The slices denoted as “P” and “D” denote when the population is pri-
marily proliferating (Φ1(ψ(t)) > 1/2) or diﬀusing (Φ1(ψ(t)) ≤1/2) over time.
The proﬁle maintains a high cell density but limited migration into the wound
during the proliferative phase and then migrates into the wound quickly during
the diﬀusive phase but can not maintain a high cell density throughout the pop-
ulation. In Figure 4(b), we investigate how the proﬁle of w(t = 40, x) changes
as α varies from α = 0 to α = 0.2. In the slice denoted “No activation”, the
15


## Page 16


Figure 3: The analytical solution for the activation proﬁle, p(t, m), for Example
1 for α = 0.5, and φ1(m) = I(0.05,0.35)(m). The solid black curves denote h(t; m)
for m = 0.05, 0.15, and 0.35 and the dashed line denotes m = mcrit. Note that
a log scale is used along p for visual ease.
entire population is still in the inactive population at t = 40 and thus does
not progress far into the wound or change with α. In the slice denoted “Ac-
tivation,” the population is split between the active and inactive populations
at t = 40. The proﬁles here are sensitive to increasing values of α, as they mi-
grate further into the wound while maintaining a high density near x = 0. The
slice denoted as “Entire Activation” denotes simulations that are entirely in the
active population by t = 40. As α increases, these simulations do not migrate
much further into the wound but do have decreasing densities at x = 0. These
results suggest that a combination of proliferation and diﬀusion must be used to
maximize population migration while maintaining a high cellular density behind
the population front. The optimal combination appears to occur at the entire
activation threshold.
Example 2: Single pulse of MAPK activation: f(t) = βeγt −1
We now detail an example that exhibits a pulse of activation in the m dimension,
which may represent the transient wave of ERK 1/2 activation observed in
MDCK cells in [31]. The authors of [41] proposed that this wave may be caused
by the rapid production of ROS in response to the wound, followed by the quick
decay of ROS or its consumption by cells. We now let f(t) = βeγt −1. This
forcing function arises if ROS is present but decaying exponentially over time
and modeled by s(t) = βeγt, β > 0, γ < 0 and cells activate linearly in response
to the presence of ROS but have a baseline level of deactivation, which may be
given by f(s) = s −1.
We see that σ(m; m) and σ−1(t; m) are the same as in Example 1 and now
16


## Page 17


Figure 4: Numerical simulations of the averaged nonautonomous Fisher’s equa-
tion for Example 1.
In (a), we depict a simulation of w(t, x) over time for
α = 0.05. The letters “P” and “D” denote when the population is primarily
proliferating or diﬀusing, respectively.
In (b), we depict how the proﬁle for
w(t = 40, x) changes for various values of α. The descriptions “No Activation”,
“Activation”, and “Entire Activation” denote values of α for which the popula-
tion is entirely in the inactive population, split between the active and inactive
populations, or entirely in the active population at t = 40, respectively.
compute
h(t; m)
=
m

m + (1 −m) exp

αt −αβ
γ (exp(γt) −1)
−1
ψ(t)
=

1 + exp

−αt + αβ
γ (exp(γt) −1)
−1
.
In Figure 5, we use (23) to depict the activation proﬁle, p(t, m), over time to
show the activation behavior of the population. We also include some speciﬁc
plots of the activation curves, h(t; m), which show a pulse of MAPK activity in
the population that starts decreasing around t = 5. Note that h(t; 0.35) crosses
the m = mcrit line but h(t; 0.05) does not, so (25) is satisﬁed for this parameter
set (the population becomes activated) but (26) is not (the entire population
does not become activated).
Using (25), we determine our activation criterion for this example as
1 −β + log β
γ
> 1
α log

mcrit
1 −mcrit
1 −mmax
mmax

.
If we ﬁx γ = −1, α = 1, mcrit = 0.5, mmax = 0.35, and mmin = 0.05, we ﬁnd
that the above inequality is satisﬁed for β approximately greater than 2.55.
This may represent a scenario in which we know the decay rate of the ROS
through γ, the activation rate of the MAPK signaling cascade through α, the
MAPK activation distribution before ROS release with mmin and mmax, and
the activation threshold with mcrit. The values of β denote the concentration of
released ROS, which should be at least 2.55 to see the population activate. We
similarly ﬁnd that the entire population will activate at some time for β > 5.68.
17


## Page 18


Figure 5: The analytical solution for the activation proﬁle, p(t, m), for Example
2 for α = 0.5, β = 3, γ = −1/4 and φ1(m) = I(0.05,0.35)(m). The solid black
curves denote h(t; m) for m = 0.05, 0.15, and 0.35 and the dashed line denotes
m = mcrit. Note that a log scale is used along p for visual ease.
In Figure 6(a), we depict a numerical simulation of (29) for this example.
The population quickly transitions to a diﬀusing stage due to the pulse of MAPK
activation and shows the smaller densities (u approximately less than 0.2) mi-
grating into the wound rapidly while the density behind the population front
drops. As the pulse of MAPK activation ends and the population transitions
back to a proliferating phenotype, the populations restores a high density be-
hind the cell front and begins to develop a traveling wave proﬁle, as suggested
by the parallel contour lines. In Figure 6(b), we investigate how the proﬁle
for w(t = 30, x) changes as β varies from β = 2 to β = 9 while keeping all
other parameters ﬁxed. We observe that the proﬁle is the same for all values of
β < 2.55, as (25) is not satisﬁed. As β increases past the activation threshold,
the proﬁle shows increased rates of migration into the wound. After passing the
entire activation threshold (26), the proﬁle continues to migrate further as β
increases, but appears less sensitive to β. This increased migration is likely due
to the population spending more time in the active population for larger values
of β. Note that for all simulations shown, the pulse of MAPK activation has
ﬁnished by t = 30.
Example 3: Periodic pulses of MAPK activation: f(t) = β sin(γt)
As a last example, we exhibit a scenario with periodic waves of activity. Such
behavior was observed in some of the experiments performed in [51], in which
cell cultures of the HaCaT cell line were periodically treated with TGF-β to
investigate how periodic treatment with TGF-β aﬀects activation of the SMAD
pathway (the canonical pathway for TGF-β, which also inﬂuences cell prolif-
eration and migration). We let f(t) = β sin(γt), β, γ > 0, which occurs if the
concentration of TGF-β over time is given by s(t) = 1 + sin(γt), and cells acti-
vate linearly in response to s and have a baseline rate of deactivation, given by
f(s) = β(s −1).
We now calculate
18


## Page 19


Figure 6: Numerical simulations of the averaged nonautonomous Fisher’s equa-
tion for Example 2.
In (a), we depict a simulation of w(t, x) over time for
α = 1, β = 8, γ = −1. Slices denoted with a “P” or “D” denote when the popu-
lation is primarily proliferating or diﬀusing, respectively. In (b), we depict how
the proﬁle for w(t = 30, x) changes for various values of β. The descriptions
“No activation”, “Activation”, and “Entire Activation” denote values of β for
which the population is entirely in the inactive population, split between the
active and inactive populations, or entirely in the active population at t = tmax.
h(t; m) = m

m + (1 −m) exp
αβ
γ (cos(γt) −1)
−1
ψ(t) =

1 + exp
αβ
γ (1 −cos(γt))
−1
.
In Figure 7, we use (23) to depict the activation proﬁle, p(t, m), over time to show
the activation behavior of the population. We also include some speciﬁc plots
of the activation curves h(t; m), which demonstrate periodic waves of activation
along m. Note that h(t; 0.05) crosses the m = mcrit line, so (26) is satisﬁed, and
the entire population becomes activated at some points during the simulation.
The activation criterion (25) can be solved as
2β
γ > 1
α log

mcrit
1 −mcrit
1 −mmax
mmax

.
We thus calculate that if we ﬁx β = 1, α = 1/2, mmax = 0.35, mmin = 0.05,
and mcrit = 0.5, then the activation criterion (25) is satisﬁed for γ < 1.615
and the entire activation criterion (26) is satisﬁed for γ < 0.34. These estimates
would tell us how frequently signaling factor treatment is needed to see diﬀerent
patterns of activation in the population.
In Figure 8(a), we depict a numerical simulation of (29) for this example.
The population phenotype has a period of 4π, and we see that the lower densities
migrate into the wound most during the diﬀusive stages, whereas all densities
appear to migrate into the wound at similar speeds during the proliferative
19


## Page 20


Figure 7: The analytical solution for the activation proﬁle, p(t, m), for Example
3 for α = 1/2, β = 4, γ = 1 and φ1(m) = I(0.05,0.35)(m). The solid black curves
denote h(t; m) for m = 0.05, 0.15, and 0.35 and the dashed line denotes m =
mcrit. Note that a log scale is used along p for visual ease.
stages. In Figure 8(b), we investigate how the proﬁle for w(t = 40, x) changes
as γ varies between γ = 0 and γ = 1.9 while keeping all other parameters
ﬁxed. All proﬁles appear the same for γ > 1.615 as (25) is not satisﬁed. As γ
decreases below this threshold, more of the population becomes activated during
the simulation, culminating in a maximum propagation of the population at the
entire activation threshold, γ ≈0.34. As γ falls below γ=0.34, the population
tends to migrate less, although the population does migrate far for γ near 0.2.
For γ < 0.2, the population appears to spend too much time in the active
population and diﬀuses excessively with limited proliferation. These simulations
lead to shallow proﬁles that do not migrate far into the wound. As γ approaches
zero, the simulations would become entirely activated, but do not before t =
40. These simulations stay in the inactive population for the duration of the
simulation and do not migrate far into the wound.
6
Discussion and Future work
We have investigated a structured Fisher’s Equation that incorporates an added
dimension for biochemical activity that inﬂuences population migration and
proliferation. The method of characteristics proved to be a useful way to track
the progression along the population activity dimension over time. With the aid
of a phase plane analysis and an asymptotically autonomous Poincare-Bendixson
Theorem, we were able to prove the existence of a self-similar traveling wave
solution to the equation when diﬀusion and proliferation do not depend on
MAPK activity. The height function of the self-similar traveling wave ansatz
along characteristic curves is demonstrated in Figures 3, 5, and 7. We believe our
analysis could be extended to investigate structured versions of other nonlinear
PDEs.
Activation of the MAPK signaling cascade is known to inﬂuence collective
migration during woung healing through cellular migration and proliferation
20


## Page 21


Figure 8: Numerical simulations of the averaged nonautonomous Fisher’s equa-
tion for Example 3.
In (a), we depict a simulation of w(t, x) over time for
α = 0.5, β = 1, and
γ = 1/2.
Slices denoted with a “P” or “D” denote when the population is
primarily proliferating or diﬀusing, respectively. In (b), we depict w(t = 40, x)
for various values of γ. The descriptions “No activation”, “Activation”, and
“Entire Activation” denote values of γ for which the population is entirely in
the inactive population, split between the active and inactive populations, or
entirely in the active population at t = tmax.
properties.
For this reason, we also considered a structured PDE model in
which the rates of cellular diﬀusion and proliferation depend on the levels of
MAPK activation in the population. We also extended the model to allow for
the presence of an external cytokine or growth factor that regulates activation
and deactivation along the MAPK signaling cascade. We derived two activation
criteria for the model to establish conditions under which the population will be-
come activated during simulations. As numerical simulations of the structured
equation are prone to error via numerical diﬀusion, we derived a nonautonomous
equation in time and space to represent the average population behavior along
the biochemical activity dimension. Using this nonautonomous equation, we ex-
hibited three simple examples that demonstrate biologically relevant activation
levels and their eﬀects on population migration: a sustained wave of activity, a
pulse of activity, and periodic pulses of activity. We found that the population
tends to migrate farthest while maintaining a high cell density at the entire
activation threshold value, (26), for the sustained wave and periodic pulse pat-
terns of activation. The single pulse case continued migrating further into the
wound after passing the entire activation threshold but appeared less sensitive
after doing so.
A natural next step for this analysis is to use a structured population model
of this sort in combination with biological data to thoroughly investigate the
eﬀects of MAPK activation and deactivation on cell migration and proliferation
during wound healing. Previous mathematical models have focused on either
collective migration during wound healing assays in response to EGF treatment
(while neglecting the MAPK signaling cascade) [21, 37] or MAPK propagation
21


## Page 22


during wound healing assays (while neglecting cell migration) [41]. To the best
of our knowledge, no mathematical models have been able to reliably couple
signal propagation and its eﬀect on cell migration during wound healing. The
examples detailed in this work intentionally used the simplest terms possible
as a means to focus on the underlying mathematical aspects. With a separate
in-depth study into the biochemistry underlying the MAPK signaling cascade
and its relation with various cytokines or growth factors, more complicated
and biologically relevant terms for g(m), f(s), and s(t) can be determined to
help elucidate the eﬀects of MAPK activation on cell migration during wound
healing.
The analytical techniques used in this study cannot be used to investigate
spatial patterns of biochemical activity due to the parabolic nature of (3) in
space.
Cell populations also migrate via chemotaxis during wound healing,
in which cells migrate up a concentration gradient of some chemical stimulus
[2, 23, 26, 38].
Chemotactic equations are hyperbolic in space, which may
facilitate spatial patterns of MAPK activation during wound healing, such as
those described experimentally in [7]. As various pathways become activated
and cross-talk during wound healing to inﬂuence migration [16], future studies
could also investigate a population structured along multiple signaling pathways,
u(t, x, ⃗m) for the vector ⃗m = (m1, m2, . . . , mn)T . Because the cell population
also produces cytokines and growth factors for paracrine and autocrine signaling
during wound healing, these models would also beneﬁt from unknown variables
representing ROS, TGF-β, EGF, etc.
While the main motivation for this study is epidermal wound healing, there
are potential applications in other areas of biology. Fisher’s equation has also
been used to study population dynamics in ecology and epidemiology [1, 19, 44].
Our framework could be extended to a case where an environmental eﬀect, such
as seasonal forcing, impacts species migration or susceptibility of individuals to
disease. The results presented here may thus aid in a plethora of mathematical
biology studies.
References
[1] S. Ai and W. Huang, Travelling waves for a reaction-diﬀusion system in
population dynamics and epidemiology, Proceedings of the Royal Society of
Edinburgh Section A: Mathematics, 135 (2005), pp. 663–675.
[2] S. Ai, W. Huant, and Z.-a. Wang, Reaction, Diﬀusion and chemotaxis
in wave propagation, Discrete and Continuous Dynamical System - B, 20
(2015), pp. 1–21.
[3] H. T. Banks and H. T. Tran, Mathematical and Experimental Modeling
of Physical and Biological Processes, CRC Press, Boca Raton, FL, 2009.
22


## Page 23


[4] S. P. Blythe, K. Cooke, and C. Castillo-Chavez, Autonomous Risk-
behavior change, and non-linear incidence rate, in models of sexually trans-
mitted diseases, (1991).
[5] A. Q. Cai, K. A. Landman, and B. D. Hughes, Multi-scale modeling of
a wound-healing cell migration assay, Journal of Theoretical Biology, 245
(2007), pp. 576–594.
[6] C. Castillo-Chavez and H. R. Thieme, Asymptotically Autonomous
Epidemic Models, (1994).
[7] D. A. Chapnick and X. Liu, Leader cell positioning drives wound-
directed collective migration in TGF beta-stimulated epithelial sheets, Mol.
Biol. Cell, 25 (2014), pp. 1586–1593.
[8] R. A. F. Clark and P. Henson, The Molecular and Cellular Biology of
Wound Repair, Plenum Press, New York, second ed., 1995.
[9] C. W. Curtis and D. M. Bortz, Propagation of fronts in the Fisher-
Kolmogorov equation with spatially varying diﬀusion, Physical Review E,
86 (2012).
[10] A. M. de Roos, A gentle introduction to physiologically structured popu-
lation models, in Structured-Population Models in Marine, Terrestrial, and
Freshwater Systems, Population and Community Biology Series, 1996.
[11] P. K. Denman, D. L. S. McElwain, and J. Norbury, Analysis of
Travelling Waves Associated with the Modelling of Aerosolised Skin Grafts,
Bull. Math. Biol., 69 (2006), pp. 495–523.
[12] A. Ducrot, Travelling waves for a size and space structured model in
population dynamics: Point to sustained oscillating solution connections,
Journal of Diﬀerential Equations, 250 (2011), pp. 410–449.
[13] A. Ducrot, P. Magal, and S. Ruan, Travelling Wave Solutions in
Multigroup Age-Structured Epidemic Models, Arch Rational Mech Anal,
195 (2009), pp. 311–331.
[14] R. A. Fisher, The wave of advance of advantageous genes, Annals of
Eugenics, 7 (1937), pp. 353–369.
[15] S. Gourley, R. Liu, and J. Wu, Some Vector Borne Diseases with
Structured Host Populations: Extinction and Spatial Spread, SIAM J. Appl.
Math., 67 (2007), pp. 408–433.
[16] X. Guo and X.-F. Wang, Signaling cross-talk between TGF-beta/BMP
and other pathways, Cell Res, 19 (2009), pp. 71–88.
[17] M. E. Gurtin and R. C. Maccamy, Non-linear age-dependent popula-
tion dynamics, Arch. Rational Mech. Anal., 54 (1974), pp. 281–300.
23


## Page 24


[18] J. F. Hammond and D. M. Bortz, Analytical solutions to Fisher’s equa-
tion with time-variable coeﬃcients, Applied Mathematics and Computa-
tion, 218 (2011), pp. 2497–2508.
[19] A. Hastings, K. Cuddington, K. F. Davies, C. J. Dugaw, S. El-
mendorf, A. Freestone, S. Harrison, M. Holland, J. Lambri-
nos, U. Malvadkar, B. A. Melbourne, K. Moore, C. Taylor, and
D. Thomson, The spatial spread of invasions: new developments in theory
and evidence, Ecology Letters, 8 (2005), pp. 91–101.
[20] W. Jin, E. T. Shah, C. J. Penington, S. W. McCue, L. K. Chopin,
and M. J. Simpson, Reproducibility of scratch assays is aﬀected by the
initial degree of conﬂuence: Experiments, modelling and model selection,
Journal of Theoretical Biology, 390 (2016), pp. 136–145.
[21] S. T. Johnston, E. T. Shah, L. K. Chopin, D. L. Sean McElwain,
and M. J. Simpson, Estimating cell diﬀusivity and cell proliferation rate
by interpreting IncuCyte ZOOM assay data using the Fisher-Kolmogorov
model, BMC Systems Biology, 9 (2015).
[22] J. P. Keener and J. Sneyd, Mathematical Physiology: I Cellular Phys-
iology, vol. 8/I of Interdisciplinary Applied Mathematics, Springer, sec-
ond ed., 2009.
[23] E. F. Keller and L. A. Segel, Traveling bands of chemotactic bacteria:
a theoretical analysis, Journal of Theoretical Biology, 30 (1971), pp. 235–
248.
[24] A. Kolmogoroff, I. Petrovsky, and N. Piscounoff, Etude de
l’equation de la diﬀusion avec croissance de la quantite de matiere et son
application a un probleme biologique, Moscow Univ. Bull. Math, 1 (1937),
pp. 1–25.
[25] Y. Kuang, E. M. Rutter, and T. L. Stepien, A data-motivated
density-dependent diﬀusion model of in vitro glioblastoma growth, Math-
ematical Biosciences and Engineering, 12 (2015), pp. 1157–1172.
[26] K. Landman, M. Simpson, J. Slater, and D. Newgreen, Diﬀusive
and Chemotactic Cellular Migration: Smooth and Discontinuous Traveling
Wave Solutions, SIAM J. Appl. Math., 65 (2005), pp. 1420–1442.
[27] K. A. Landman, A. Q. Cai, and B. D. Hughes, Travelling Waves of
Attached and Detached Cells in a Wound-Healing Cell Migration Assay,
Bull. Math. Biol., 69 (2007), pp. 2119–2138.
[28] B. P. Leonard, The ULTIMATE conservative diﬀerence scheme applied
to unsteady one-dimensional advection, Computer Methods in Applied Me-
chanics and Engineering, 88 (1991), pp. 17–74.
24


## Page 25


[29] P. K. Maini, D. S. McElwain, and D. I. Leavesley, Traveling wave
model to interpret a wound-healing cell migration assay for human peri-
toneal mesothelial cells, Tissue engineering, 10 (2004), pp. 475–482.
[30] L. Markus, Asymptotically autonomous diﬀerential systems, in Contribu-
tions to the theory of nonlinear oscillations, vol. III of Annals of Mathe-
matics Studies, Princeton University Press, 1956.
[31] Y. Matsubayashi, M. Ebisuya, S. Honjoh, and E. Nishida, ERK Ac-
tivation Propagates in Epithelial Cell Sheets and Regulates Their Migration
during Wound Healing, Current Biology, 14 (2004), pp. 731–735.
[32] A. G. McKendrick, Applications of mathematics to medical problems,
1927.
[33] J. D. Meiss, Diﬀerential Dynamical Systems, SIAM, 2007.
[34] J. D. Murray, Lectures on nonlinear-diﬀerential equation models in biol-
ogy, Oxford University Press, 1977.
[35] J. D. Murray, Mathematical Biology I. An Introduction, vol. 17 of In-
terdisciplinary Applied Mathematics, Springer New York, New York, NY,
3rd ed., 2002.
[36] P. J. Murray, J.-W. Kang, G. R. Mirams, S.-Y. Shin, H. M.
Byrne, P. K. Maini, and K.-H. Cho, Modelling Spatially Regulated beta-
Catenin Dynamics and Invasion in intestinal Crypts, Biophysical Journal,
99 (2010), pp. 716–725.
[37] J. T. Nardini, D. A. Chapnick, X. Liu, and D. M. Bortz, Modeling
keratinocyte wound healing: cell-cell adhesions promote sustained migra-
tion, Journal of Theoretical Biology, 400 (2016), pp. 103–117.
[38] D. Newgreen, G. Pettet, and K. Landman, Chemotactic Cellular
Migration: Smooth and Discontinuous Travelling Wave Solutions, SIAM J.
Appl. Math., 63 (2003), pp. 1666–1681.
[39] A. Perumpanani, B. Marchant, and J. Norbury, Traveling Shock
Waves Arising in a Model of Malignant Invasion, SIAM J. Appl. Math.,
60 (2000), pp. 463–476.
[40] G. J. Pettet, H. M. Byrne, D. L. S. Mcelwain, and J. Norbury,
A model of wound-healing angiogenesis in soft tissue, Mathematical Bio-
sciences, 136 (1996), pp. 35–63.
[41] F. Posta and T. Chou, A mathematical model of intercellular signaling
during epithelial wound healing, Journal of Theoretical Biology, 266 (2010),
pp. 70–78.
[42] F. R. Sharpe and A. J. Lotka, A problem in Age-Distribution,
Philosphical Magazine, 21 (1911), pp. 435–438.
25


## Page 26


[43] J. A. Sherratt and M. A. J. Chaplain, A new mathematical model
for avascular tumour growth, J Math Biol, 43 (2001), pp. 291–312.
[44] N. Shigesada and K. Kawasaki, Biological Invasions: Theory and Prac-
tice, Oxford Series in Ecology and Evolution, Oxford University Press, 1997.
[45] J. W.-H. So, J. Wu, and X. Zou, A reaction-diﬀusion model for a single
species with age structure. I Travelling wavefronts on unbounded domains,
Proceedings of the Royal Society of London A: Mathematical, Physical and
Engineering Sciences, 457 (2001), pp. 1841–1853.
[46] J. A. Thackham, D. L. S. McElwain, and I. W. Turner, Computa-
tional Approaches to Solving Equations Arising from Wound Healing, Bull.
Math. Biol., 71 (2008), pp. 211–246.
[47] H. R. Thieme, Convergence results and a Poincare-Bendixson trichotomy
for asymptotically autonomous diﬀerential equations, J. Math. Biol., 30
(1992), pp. 755–763.
[48] H. R. Thieme, Asymptotically Autonomous Diﬀerential Equations in the
Plane, Rocky Mountain J. Math., 24 (1993), pp. 351–380.
[49] A. Volpert, V. Volpert, and V. Volpert, Traveling Wave Solutions
of Parabolic Systems, vol. 140 of Translations of Mathematical Monographs,
American Mathematical Society, 1994.
[50] G. F. Webb, Population models structured by age, size, and spatial po-
sition, in Structured Population Models in Biology and Epidemiology,
Springer, 2008, pp. 1–49.
[51] Z. Zi, Z. Feng, D. A. Chapnick, M. Dahl, D. Deng, E. Klipp,
A. Moustakas, and X. Liu, Quantitative analysis of transient and sus-
tained transforming growth factor-beta signaling dynamics, Molecular Sys-
tems Biology, 7 (2011), p. 492.
A
Properties of σ−1(t; y)
If we assume that g is positive and uniformly continuous, then σ−1(t; y) exists
and satisﬁes the following:
d
dtσ−1(t; y) = g(σ−1(t; y)), σ−1(0; y) = y.
(30)
26


## Page 27


To derive (30), see that
y(t)
=
σ−1(t; y)
⇒σ(y(t); y)
=
t
⇒d
dt
 σ(y(t); y)

= d
dy σ(y(t); s)dy
dt
=
1
⇒
1
g(y(t))
dy
dt
=
1
⇒dy
dt
=
g(y(t))
⇒d
dtσ−1(t; y)
=
g(σ−1(t; y)).
and for the initial condition,
σ(y, y)
=
0
⇒σ−1(0, y)
=
y.
B
Derivation of (9)
In (8), we deﬁned
v(t; y) := u(t, y = σ−1(t; y)).
Taking the derivative of v(t; y) with respect to time, we ﬁnd with the aid of the
chain rule:
d
dtv(t; y)
=
∂
∂tu(t, y = σ−1(t; y)) + ∂
∂y u(t, y = σ−1(t; y)) · d
dtσ−1(t; y)
=
−∂
∂y

g
 σ−1(t; y)

u
 t, y = σ−1(t; y)

+ Au
 t, y = σ−1(t; y)

+ g
 σ−1(t; y)
 ∂
∂y u
 t, y = σ−1(t; y)

=
−g′(σ−1(t; y))v(t; y) + Av(t; y).
C
Relevant Material on Asymptotically Au-
tonomous Diﬀerential Systems
The theorem statements in this section have been slightly modiﬁed to match
notation from our study. Consider the two vector ﬁelds,
˙x
=
f(t, x)
(31)
˙y
=
g(y),
(32)
for x, y ∈Rn and t > 0. Assume f(t, x) and g(x) are continuous in t and x
and locally Lipschitz in x for x ∈Ωand t > 0, where Ωis an open subset of
27


## Page 28


Rn. We say that (31) is asymptotically autonomous with limit equation (32) if
f(t, x) →g(x) pointwise as t →∞on any compact subset of Ω.
We will denote the ω-limit sets for all points starting in the set Θ ⊂Ωat
t = 0 for the system (31) as ωf(Θ). This asymptotically autonomous Poincare-
Bendixson Theorem was introduced in [30] and states
Asymptotically Autonomous Poincare-Bendixson Theorem:
Let n = 2 and (31) be asymptotically autonomous with limit equation (32)
in Ω⊂R2. Let a solution, x(t), of (31) lie in a compact set Θ ⊂Ωfor large t
and suppose ωf(Θ) contains no equilibria of (32). Then ωf(Θ) is the union of
periodic orbits of (32).
The proof of this Theorem is a result of the standard Poincare-Bendixson
Theorem (see [33, Section 6.6]) and the following theorem, which is also proved
in [30].
Theorem: Let (31) be asymptotically autonomous with limit equation (32)
in Ω∈Rn. Let P be a stable equilibrium point of (32). Then there is a neigh-
borhood, N, of P and a time T such that ωf(N) ={P} for all solutions of (31)
starting at time T or later.
28

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
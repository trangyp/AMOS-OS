---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1901.07620v3
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1901.07620v3_A_Kinetic_Theory_Approach_to_Model_Pedestrian_Dynamics_in_Bounded_Domains_with_O

> Source: 1901.07620v3_A_Kinetic_Theory_Approach_to_Model_Pedestrian_Dynamics_in_Bounded_Domains_with_O.pdf

> Pages: 30

---


## Page 1


A kinetic theory approach to model pedestrian dynamics in
bounded domains with obstacles
Daewa Kim∗and Annalisa Quaini∗
∗Department of Mathematics, University of Houston, 3551 Cullen Blvd, Houston TX 77204
daewakim@math.uh.edu; quaini@math.uh.edu
June 17, 2019
Abstract We consider a kinetic theory approach to model the evacuation of a crowd from bounded
domains. The interactions of a person with other pedestrians and the environment, which includes
walls, exits, and obstacles, are modeled by using tools of game theory and are transferred to the
crowd dynamics. The model allows to weight between two competing behaviors: the search for less
congested areas and the tendency to follow the stream unconsciously in a panic situation. For the
numerical approximation of the solution to our model, we apply an operator splitting scheme which
breaks the problem into two pure advection problems and a problem involving the interactions. We
compare our numerical results against the data reported in a recent empirical study on evacuation
from a room with two exits. For medium and medium-to-large groups of people we achieve good
agreement between the computed average people density and ﬂow rate and the respective measured
quantities. Through a series of numerical tests we also show that our approach is capable of handling
evacuation from a room with one or more exits with variable size, with and without obstacles, and
can reproduce lane formation in bidirectional ﬂow in a corridor.
1
Introduction
The complex dynamical behavior of pedestrian crowds has fascinated researchers from various
scientiﬁc ﬁelds since the early 1950’s. Academic studies started with empirical observations and
continued with the development of models in the ﬁeld of applied physics and mathematics. The
simulation of pedestrian ﬂow has attracted increasing research attention in recent years since a
reliable simulation model for pedestrian ﬂow may greatly beneﬁt engineers in mass transportation
management, and designers in urban planning and architecture.
A very large variety of models have been developed over the years. The diﬀerent mathematical
models can be divided into three main categories depending on the scale of observation [8]. A ﬁrst
approach corresponds to the macroscopic description: evolution equations are derived for mass
1
arXiv:1901.07620v3  [math.NA]  14 Jun 2019


## Page 2


density and linear momentum, which are regarded as macroscopic observables of pedestrian ﬂow.
See, e.g., [28, 37]. Such an approach is suitable for high density, large-scale systems, which are not
the focus of our work.
A second approach looks at the problem at the microscopic level. Microscopic models can be
further divided into models which are grid-based or grid-free. Cellular Automata [14, 15, 16, 21, 31]
models belong to the ﬁrst category.
They describe pedestrian ﬂow in space-time by assigning
discrete states to a grid of space-cells. These cells can be occupied by a pedestrian or be empty.
Thus, the movement of pedestrians in space is done by passing them from cell to cell (discrete space)
in discrete time. Grid-free methods can be based on second order models (forces-based), ﬁrst order
models (vision-based or speed-based) or zeroth order models (rule-based or decision-based). Force-
based models use Newtonian mechanics to interpret pedestrian movement as the physical interaction
between the people and the environment, i.e. the action of other people and the environment on
a given pedestrian is modeled with forces. These models are one of the most popular modeling
paradigms of continuous models because they describe the movement of pedestrians qualitatively
well.
See, e.g., [18, 24, 26, 27, 32, 33, 39, 43] and references therein.
Collective phenomena,
like unidirectional or bidirectional ﬂow in a corridor, lane formation, oscillations at bottlenecks,
the faster-is-slower eﬀect, and emergency evacuation from buildings, are well reproduced. Agent-
based models allow for ﬂexibility, extensibility, and capability to realize heterogeneity in crowd
dynamics. For examples of vision-based, speed-based, rule-based, and decision-based models we
refer to [2, 3, 4, 17, 19, 20] and references therein.
Both force-based and agent-based models
may introduce artifacts due to the force representation of human behavior, leading to unrealistic
backward movement or oscillating trajectories. These artifacts can be reduced by incorporating
extra rules and/or elaborate calibrations, at the price of an increased computational cost.
The scale of observation for the third approach is between the previous two. Introduced in [5]
and further developed in [1, 6, 7, 9, 10, 11, 12], this approach derives a Boltzmann-type evolution
equation for the statistical distribution function of the position and velocity of the pedestrians,
in a framework close to that of the kinetic theory of gases. See also [13] for a literature review
on this approach. The model proposed in [5, 6, 12] is valid in unbounded domains and with a
homogeneous distribution of walking ability for the pedestrians, while the extension to bounded
domains is presented in [1] and further explored in [9, 10, 11]. In [9], more general features of
behavioral-social dynamics are taken into account. In [10], Monte Carlo simulations are introduced
to study pedestrians behavior in complex scenarios.
The methodology in [10] is validated by
comparing the computed fundamental density-velocity diagrams with empirically observed ones
and by checking that well known emerging properties are reproduced. A kinetic theory approach
for modeling pedestrian dynamics in presence of social phenomena, such as the propagation of stress
conditions, is presented in [11]. Finally, we refer to [7] for a thorough description of how kinetic
theory and evolutionary game theory can be used to understand the dynamics of living systems.
The scale of observation for the third approach is between the previous two. In a framework close
to that of the kinetic theory of gases, this approach derives a Boltzmann-type evolution equation
for the statistical distribution function of the position and velocity of the pedestrians. The kinetic


## Page 3


theory approach was introduced in [5] and further developed in [12]. The model in [5, 12] is valid
in unbounded domains. The extension to bounded domains is presented in [1]. Further literature
review on this approach can in found in [13].
In this work, we consider the model proposed in [1]. We ﬁrst validate it against experimental
data and then extend it to bounded domains with obstacles. It is worth noticing that most of the
models and methods in the references cited so far have been shown to reproduce phenomena of
pedestrian movement qualitatively through analysis and/or numerical simulations. However, before
using a model to predict quantitative results like, e.g., the total evacuation time, the mathematical
models have to be validated and the numerical methods have to be veriﬁed [22]. In the context of
pedestrian dynamics, this is still diﬃcult due to a lack of reliable experimental data. In addition,
the few available datasets show large diﬀerences [34, 36, 42].
In this paper, we compare our
numerical results against the data reported in a recent empirical study [40]. We have selected this
study because it deals with egressing from a facility and thus it is the most directly related to our
focus. With the model under consideration, for medium and medium-to-large groups of people we
manage to achieve good agreement between the computed average people density and ﬂow rate and
the respective measured quantities. Finally, we mention that in order to make the models more
reliable, evolutionary adjustment of the parameters and data assimilations have also been proposed
in [29, 41], respectively.
The strategy we propose to handle obstacles within the computational domain makes use of
an eﬀective obstacle area, which is an enlarged area that encloses the real obstacle, and a model
parameter used to describe the quality of the environment. Thanks to those two ingredients, we can
successfully exclude from the walkable area square and rectangular obstacles. We test our strategy
in a square room that contains one or two obstacles and has one exit. In addition, through a series
of numerical tests we show that our approach is capable of handling evacuation from a room with
one or more exits with variable size, with and without obstacles, and can reproduce lane formation
in bidirectional ﬂow in a corridor.
The paper is organized as follows. Section 2 introduces the representation of the system and
the modeling of interactions with pedestrians and with the envornment. In Section 3, we apply
the Lie splitting algorithm to the model described in Section 2. Numerical results are presented in
Section 4 and conclusions are drawn in Sectioin 5.
2
Mathematical model
The model we consider is based on the model proposed in [1]. Let Ω⊂R2 denote a bounded
domain. We assume that the boundary ∂Ωincludes an exit E which could be the ﬁnite union
of disjoint sets, and walls W. Here, E ∪W = ∂Ωand E ∩W = ∅. Let x = (x, y) ∈Ωdenote
position and v = v(cos θ, sin θ) ∈Ωv denote velocity, where v is the velocity modulus, θ is the
velocity direction, and Ωv ⊂R2 is the velocity domain. For a system composed by a large number


## Page 4


of pedestrians distributed inside Ω, the distribution function is given by
f = f(t, x, v)
for all t ≥0, x ∈Ω, v ∈Ωv.
Under suitable integrability conditions, f(t, x, v)dxdv represents the number of individuals who,
at time t, are located in the inﬁnitesimal rectangle [x, x + dx] × [y, y + dy] and have a velocity
belonging to [v, v + dv] × [θ, θ + dθ]. Since we use polar coordinates for the velocity, we can write
the distribution function as f = f(t, x, v, θ).
Following [1], we assume that variable θ is discrete.
This assumption is motivated by the
granularity of pedestrian dynamics when the crowd size is not enough to justify the continuity of
the distribution function over the variable θ. For simplicity, we assume θ can take values in the set:
Iθ =

θi = i −1
Nd
2π : i = 1, . . . , Nd

,
where Nd is the maxim number of possible directions. As for the velocity magnitude v, we model
it as a continuous deterministic variable which evolves in time and space according to macroscopic
eﬀects determined by the overall dynamics. In fact, experimental studies show that in practical
situations the speed of pedestrians depends mainly on the level of congestion around them.
Due to the deterministic nature of the variable v, the kinetic type representation is given by
the reduced distribution function
f(t, x, θ) =
Nd
X
i=1
fi(t, x)δ(θ −θi),
(1)
where fi(t, x) = f(t, x, θi) represents the active particles that, at time t and position x, move with
direction θi. In equation (1), δ denotes the Dirac delta function.
Let us introduce some reference quantities that will be use to make the variable dimensionless.
We deﬁne:
- D: the largest distance a pedestrian can cover in domain Ω;
- VM: the highest velocity modulus a pedestrian can reach in low density and optimal environ-
mental conditions;
- T: a reference time given by D/VM;
- ρM: the maximal admissible number of pedestrians per unit area.
The dimensionless variables are then: position ˆx = x/D, time ˆt = t/T, velocity modulus ˆv = v/VM
and distribution function ˆf = f/ρM. From now on, all the variables will be dimensionless and hats
will be omitted to simplify notation.
Due to the normalization of f, and of each fi, the dimensionless local density is obtained by
summing the distribution functions over the set of directions:
ρ(t, x) =
Nd
X
i=1
fi(t, x).
(2)


## Page 5


As mentioned above, we assume that pedestrians adjust their speed depending on the level of
congestion around them. This means that the velocity modulus depends formally on the local
density, i.e. v = v[ρ](t, x), where square brackets are used to denote that v depends on ρ in a
functional way. For instance, v can depend on ρ and on its gradient.
A parameter α ∈[0, 1] is introduced to represent the quality of the domain where pedestrians
move: α = 0 corresponds to the worst quality which forces pedestrians to slow down or stop, while
α = 1 corresponds to the best quality, which allows pedestrians to walk at the desired speed. We
assume that the maximum dimensionless speed vM a pedestrian can reach depends linearly on the
quality of the environment. For simplicity, we take vM = α. Let ρc be a critical density value
such that for ρ < ρc we have free ﬂow regime (i.e., low density condition), while for ρ > ρc we
have a slowdown zone (i.e., high density condition). We set ρc = α/5. Note that this choice is
compatible with the experimentally measured values of ρc reported in [35]. Next, we set the velocity
magnitude v equal to vM in the free ﬂow regime and equal to a heuristic third-order polynomial in
the slowdown zone:
v = v(ρ) =
(
α
for
ρ ≤ρc(α) = α/5
a3ρ3 + a2ρ2 + a1ρ + a0
for
ρ > ρc(α) = α/5,
(3)
where ai is constant for i = 0, 1, 2, 3. To set the value of these constants, we impose the following
conditions: v(ρc) = vM, ∂ρv(ρc) = 0, v(1) = 0 and ∂ρv(1) = 0. This leads to:











a0
= (1/(α3 −15α2 + 75α −125))(75α2 −125α)
a1
= (1/(α3 −15α2 + 75α −125))(−150α2)
a2
= (1/(α3 −15α2 + 75α −125))(75α2 + 375α)
a3
= (1/(α3 −15α2 + 75α −125))(−250α).
(4)
Figure 1 (A) reports v as a function of ρ for α = 0.4, 0.7, 1.
2.1
Modeling interactions
Each pedestrian is modeled as a particle. Interactions involve three types of particles:
- test particles with state (x, θi): they are representative of the whole system;
- candidate particles with state (x, θh): they can reach in probability the state of the test
particles after individual-based interactions with the environment or with ﬁeld particles;
- ﬁeld particles with state (x, θk): their presence triggers the interactions of the candidate
particles.
The process through which a pedestrian decides the direction to take is the results of several factors.
We take into account four factors:
(F1) The goal to reach the exit.
Given a candidate particle at the point x, we deﬁne its distance to the exit as
dE(x) = min
xE∈E ||x −xE||,


## Page 6


0
0.2
0.4
0.6
0.8
1
density 
0
0.2
0.4
0.6
0.8
1
velocity modulus v
 = 1
 = 0.7
 = 0.4
(a) v as a function of ρ
xW
(b) Notation in a sample computational domain
Figure 1: (A) Dependence of the dimensionless velocity modulus v on the dimensionless density ρ
for diﬀerent values of the parameter α, which represents the quality of the environment. (B) Sketch
of computational domain Ωwith exit E and a pedestrian located at x, moving with direction θh.
The pedestrian should choose direction uE to reach the exit, while direction uW is to avoid collision
with the wall. The distances form the exit and from the wall are dE and dW , respectively.
and we consider the unit vector uE(x), pointing from x to the exit. See Figure 1 (B).
(F2) The desire to avoid the collision with walls.
Given a candidate particle at the point x moving with direction θh, we deﬁne the distance
dW (x, θh) from the particle to a wall at a point xW (x, θh) where the particle is expected to
collide with the wall. The unit tangent vector uW (x, θh) to ∂Ωat xW points to the direction
of the the exit. Vector uW is used to avoid a collision with the walls. See Figure 1 (B).
(F3) The tendency to look for less congested area.
A candidate particle (x, θh) may decide to change direction in order to avoid congested areas.
This is achieved with the direction that gives the minimal directional derivative of the density
at the point x. We denote such direction by unit vector uC(θh, ρ).
(F4) The tendency to follow the stream.
A candidate particle modiﬁes its state, in probability, into that of the test particle due to
interactions with ﬁeld particles, while the test particle loses its state as a result of these
interactions. A candidate particle h interacting with a ﬁeld particle k may decide to follow it
and thus adopt its direction, denoted with unit vector uF = (cos θk, sin θk).
Factors (F1) and (F2) are related to geometric aspects of the domain, while factors (F3) and
(F4) consider that people’s behavior is strongly aﬀected by surrounding crowd. Note that the eﬀects
related to factors (F3) and (F4) compete with each other: (F4) is dominant in a panic situation,


## Page 7


while (F3) characterizes rational behavior.
As a weight between (F3) and (F4), we introduce
parameter ε ∈[0, 1]: ε = 0 corresponds to the situation in which only the research of less congested
areas is considered (rational behavior), while ε = 1 corresponds to the situation in which only the
tendency to follow the stream is taken into account (panic behavior).
2.1.1
Interaction with the bounding walls
The interaction with the bounding walls is modeled with two terms:
- µ[ρ]: the interaction rate models the frequency of interactions between candidate particles and
the boundary of the domain. If the local density is getting lower, it is easier for pedestrians
to see the walls and doors. Thus, we set µ[ρ] = 1 −ρ.
- Ah(i): the transition probability gives the probability that a candidate particle h, i.e. with
direction θh, adjusts its direction into that of the test particle θi due to the presence of the
walls and/or an exit. The following constraint for Ah(i) has to be satisﬁed:
Nd
X
i=1
Ah(i) = 1
for all h ∈{1, . . . , Nd}.
We assume that particles change direction, in probability, only to an adjacent clockwise or
counterclockwise direction in the discrete set Iθ. This means a candidate particle h may end up
into the states h −1, h + 1 or remain in the state h. In the case h = 1, we set θh−1 = θNd and, in
the case h = Nd, we set θh+1 = θ1. The set of all transition probabilities A = {Ah(i)}h,i=1,...,Nd
forms the so-called table of games that models the game played by active particles interacting with
the bounding walls.
To take into account factors (F1) and (F2), we deﬁne the vector
uG(x, θh) =
(1 −dE(x))uE(x) + (1 −dW (x, θh))uW (x, θh)
||(1 −dE(x))uE(x) + (1 −dW (x, θh))uW (x, θh)||
= (cos θG, sin θG).
(5)
Here θG is the geometrical preferred direction, which is the ideal direction that a pedestrian
should take in order to reach the exit and avoid the walls in an optimal way. Notice that the closer
a pedestrian is to an exit (resp., a wall), the more direction uE (resp., uW ) weights.
A candidate particle h will update its direction by choosing the angle closest to θG among the
three allowed angles θh−1, θh and θh+1. The transition probability is given by:
Ah(i) = βh(α)δs,i + (1 −βh(α))δh,i,
i = h −1, h, h + 1,
(6)
where
s =
arg min
j∈{h−1,h+1}
{d(θG, θj)},


## Page 8


with
d(θp, θq) =
(
|θp −θq|
if |θp −θq| ≤π,
2π −|θp −θq|
if |θp −θq| > π.
(7)
In (6), δ denotes the Kronecker delta function. Coeﬃcient βh, proportional to parameter α, is
deﬁned by:
βh(α) =



α
if d(θh, θG) ≥∆θ,
αd(θh, θG)
∆θ
if d(θh, θG) < ∆θ,
where ∆θ = 2π/Nd. The role of βh is to allow for a transition to θh−1 or θh+1 even in the case
that the geometrical preferred direction θG is closer to θh. Such a transition is more likely to occur
the more distant θh and θG are. Notice that if θG = θh, then βh = 0 and Ah(h) = 1, meaning
that a pedestrian keeps the same direction (in the absence of interactions other than with the
environment) with probability 1.
2.1.2
Interaction with obstacles
The strategy reported in the previous section to avoid collisions with the walls works well when
the pedestrian is suﬃciently far from the walls. If pedestrians get too close to the bounding walls,
and in particular if they are close to an exit, the deﬁnition of uG in (5) does not prevent collisions
with the walls. Thus, obstacles within the domain Ωcannot be avoided just by adjusting uW . In
this section, we report an eﬀective strategy to handle obstacles.
Four ingredients are needed to exclude the real obstacle area from the walkable domain:
1. An eﬀective area: an enlarged area that encloses the real obstacle.
2. A deﬁnition of uW to account for the eﬀective area.
3. A setting of the parameter α in the eﬀective area depending on the shape of the obstacle.
4. A dynamic setting of uE.
The eﬃcacy of this approach is demonstrated numerically in Sec. 4.3. Given the complexity of
the pedestrian dynamics model under consideration, a formal demonstration that this approach
guarantees exclusion of the obstacle from the walkable area is less straightforward and we shall
address it elsewhere. We note that all the ingredients are already available within the model.
The eﬀective area is necessary especially if the obstacle is close to an exit: it allows to deﬁne
uW with respect to a larger area than the one occupied by the obstacle to achieve the goal of having
no pedestrian walking on the real obstacle area. See Fig. 2. In the numerical results reported in
Section 4.3, we used an eﬀective area that is four times bigger than the real obstacle area. The size
and shape of the eﬀective area has been determined heuristically.
Since some pedestrians will walk on part of the eﬀective area, one needs to set parameter α. By
setting α = 1 (i.e., best quality of the environment) in the eﬀective area, pedestrians can move with
the maximal velocity modulus as they approach the obstacle and thus they quickly adapt to the
eﬀective area through uW . However, some pedestrians will walk close to the top, bottom, and rear


## Page 9


Ω
E
Figure 2: Deﬁnition of uW and uE with respect to the eﬀective area.
(with respect to the pedestrian motion) boundary of the eﬀective area. Thus, the real obstacle is
located at the front of the eﬀective area. From the numerical results reported in Section 4.3, we also
see that the shape of the obstacle is square. By setting α = 0 (i.e., worst quality of the environment)
in the eﬀective area, pedestrians are forced to slow down at the front part of the eﬀective area. The
slow down leads to higher densities in the front part of the eﬀective area, therefore direction uW
competes with direction uC. As a result some pedestrians walk on the front part of the eﬀective
area. However, as the congestion decreases pedestrians avoid the rear part of the eﬀective area.
From the numerical results shown in Section 4.3, we see that the shape of the obstacle for α = 0 in
the eﬀective area is slender.
Finally, the dynamic setting of uE is needed for certain pedestrians, depending on their position
with respect to the obstacle. As a pedestrian approaches the eﬀective area of an obstacle, uE
connects his/her position to the closest corner of the eﬀective area in the direction of the ﬁnal
target (i.e., the exit). See Fig. 2. Notice that uE can be regarded as the direction a pedestrian
needs to take to reach his/her target. Thus, it is reasonable that a pedestrian adjusts the direction
when in proximity of an obstacle.
2.1.3
Interactions between pedestrians
The interaction with other pedestrians is modeled with two terms:
- η[ρ]: the interaction rate deﬁnes the number of binary encounters per unit time. If the local
density increases, then the interaction rate also increases. For simplicity, we take η[ρ] = ρ.
Notice that unlike the case of classical gas dynamics, this rate is not related to the relative
particle velocity.
- Bhk(i)[ρ]: the transition probability gives the probability that a candidate particle h modiﬁes
its direction θh into that of the test particle i, i.e. θi, due to the research of less congested
areas and the interaction with a ﬁeld particle k that moves with direction θk. The following


## Page 10


constrain for Bhk(i) has to be satisﬁed:
Nd
X
i=1
Bhk(i)[ρ] = 1
for all h, k ∈{1, . . . , Nd},
where again the square brackets denote the dependence on the density ρ.
The game consists in choosing the less congested direction among the three admissible ones.
This direction can be computed for a candidate pedestrian h situated at x, by taking
C =
arg min
j∈{h−1,h,h+1}
{∂jρ(t, x)},
where ∂jρ denotes the directional derivative of ρ in the direction given by angle θj.
We have
uC(θh, ρ) = (cos θC, sin θC). As for the tendency to follow the crowd, we set uF = (cos θk, sin θk).
This means that a candidate particle follows the direction of a ﬁeld particle.
To take into account (F3) and (F4), we deﬁne the vector
uP (θh, θk, ρ) =
εuF + (1 −ε)uC(θh, ρ)
||εuF + (1 −ε)uC(θh, ρ)|| = (cos θP , sin θP ),
where the subscript P stands for pedestrians. Direction θP is the interaction-based perferred di-
rection, obtained as a weighted combination between the trendency to follow the stream and the
tendency to avoid crowded zones.
The transition probability is given by:
Bhk(i)[ρ] = βhk(α)ρδr,i + (1 −βhk(α)ρ)δh,i,
i = h −1, h, h + 1,
where r and βhk are deﬁned by:
r =
arg min
j∈{h−1,h+1}
{d(θP , θj)},
βhk(α) =



α
if d(θh, θP ) ≥∆θ
αd(θh, θP )
∆θ
if d(θh, θP ) < ∆θ.
We recall that d(·, ·) is deﬁned in (7).
2.2
Equation of balance
The derivation of the mathematical model can be obtained by a suitable balance of particles in an
elementary volume of the space of microscopic states, considering the net ﬂow into such volume


## Page 11


due to transport and interactions [1]. Taking into account factors (F1)-(F4), we obtain:
∂fi
∂t + ∇·
 vi[ρ](t, x)fi(t, x)

= J i[f](t, x)
= J i
G[f](t, x) + J i
P [f](t, x)
= µ[ρ]
 n
X
h=1
Ah(i)fh(t, x) −fi(t, x)
!
+ η[ρ]


n
X
h,k=1
Bhk(i)[ρ]fh(t, x)fk(t, x) −fi(t, x)ρ(t, x)


(8)
for i = 1, 2, . . . , Nd.
Functional J i[f] represents the net balance of particles that move with
direction θi due to interactions. As explained in the previous subsection, we consider both the
interaction with the environment and with the surrounding people.
Thus, we can write J i as
J i = J i
G + J i
P , where J i
G is an interaction between candidate particles and the environment and
J i
P is an interaction between candidate and ﬁeld particles.
Equation (8) is completed with equation (2) for the density and equation (3),(4) for the velocity.
In the next section, we will discuss a numerical method for the solution of problem (2),(3),(4),(8).
3
Numerical method
The approach we consider is based on a splitting method that decouples the treatment the transport
term and the interaction term in equation (8). As usual with splitting methods, the idea is to split
the model into a set of subproblems that are easier to solve and for which practical algorithms are
readily available. The numerical method is then completed by picking an appropriate numerical
scheme for each subproblem. Among the available operator-splitting methods, we chose the Lie
splitting scheme because it provides a good compromise between accuracy and robustness, as shown
in [23].
3.1
The Lie operator-splitting scheme
Although the Lie splitting scheme is quite well-known, it may be useful to present brieﬂy this
scheme before applying it to the solution of problem (2),(3),(4),(8).
Let us consider a ﬁrst-order system in time:
∂φ
∂t + A(φ)
=
0,
in (0, T),
φ(0)
=
φ0,


## Page 12


where A is an operator from a Hilbert space into itself. Operator A is then split, in a non-trivial
decomposition, as
A =
I
X
i=1
Ai.
The Lie scheme consists of the following. Let ∆t > 0 be a time discretization step for the time
interval [0, T]. Denote tk = k∆t, with k = 0, . . . , Nt and let φk be an approximation of φ(tk). Set
φ0 = φ0. For n ≥0, compute φk+1 by solving
∂φi
∂t + Ai(φi)
=
0
in (tk, tk+1),
(9)
φi(tk)
=
φk+(i−1)/I,
(10)
and then set φk+i/I = φi(tk+1), for i = 1, . . . .I.
This method is ﬁrst-order accurate in time.
More precisely, if (9) is deﬁned on a ﬁnite-
dimensional space, and if the operators Ai are smooth enough, then ∥φ(tk) −φk∥= O(∆t) [23].
In the next section, we will apply Lie splitting to problem (8). The whole problem will be split
into three subproblems:
1. A pure advection problem in the x direction.
2. A pure advection problem in the y direction.
3. A problem involving the interaction with the environment and other pedestrians.
3.2
Lie scheme applied to problem (8)
Let us apply the Lie operator-splitting scheme described in the previous section to problem (8).
Given an initial condition fi,0 = fi(0, x), for i = 1, . . . , Nd, the algorithm reads:
For k =
0, 1, 2, . . . , Nt −1, perform the following steps:
- Step 1: Find fi, for i = 1, . . . , Nd, such that



∂fi
∂t + ∂
∂x
 (v[ρ] cos θi)fi(t, x)

= 0 on (tk, tk+1),
fi(tk, x) = fi,k.
(11)
Set fi,k+ 1
3 = fi(tk+1, x).
- Step 2: Find fi, for i = 1, . . . , Nd, such that



∂fi
∂t + ∂
∂y
 (v[ρ] sin θi)fi(t, x)

= 0 on (tk, tk+1),
fi(tk, x) = fi,k+ 1
3 .
(12)
Set fi,k+ 2
3 = fi(tk+1, x).


## Page 13


- Step 3: Find fi, for i = 1, . . . , Nd, such that



∂fi
∂t = J i[f](t, x) on (tk, tk+1),
fi(tk, x) = fi,k+ 2
3 .
(13)
Set fi,k+1 = fi(tk+1, x).
Notice that once fi,k+1 is computed for i = 1, . . . , Nd, we use equation (2) to get the density
ρk+1 and equation (3),(4) to get the velocity magnitude at time tk+1.
3.3
Space and time discretization
Let us assume for simplicity that the computational domain under consideration is a rectangle
[0, L] × [0, H], for given L and H. We mesh the computational domain by choosing ∆x and ∆y to
partition interval [0, L] and [0, H], respectively. Let Nx = L/∆x and Ny = H/∆y. We deﬁne the
discrete mesh points xpq = (xp, yq) by
xp = p∆x,
p = 0, 1, . . . , Nx,
yq = q∆y,
q = 0, 1, . . . , Ny.
It will also be useful to deﬁne
xp+1/2 = xp + ∆x/2 =

p + 1
2

∆x,
yq+1/2 = yq + ∆y/2 =

q + 1
2

∆y.
In order to simplify notation, let us set φ = fi, θ = θi, t0 = tk, tf = tk+1. Let M be a positive
integer (≥3, in practice). We associate with M a time discretization step τ = (tf −t0)/M and
set tm = t0 + mτ. Next, we proceed with the space and time discretization of each subproblem in
Section 3.2.
Step 1
Let φ0 = fi,k. Problem (11) can be rewritten as



∂φ
∂t + ∂
∂x ((v[ρ] cos θ)φ(t, x)) = 0 on (t0, tf),
φ(t0, x) = φ0.
(14)
The ﬁnite diﬀerence method we use produces an approximation Φm
p,q ∈R of the cell average
Φm
p,q ≈
1
∆x ∆y
Z yq+1/2
yq−1/2
Z xp+1/2
xp−1/2
φ(tm, x, y)dx dy,


## Page 14


where m = 1, . . . , M, 1 ≤p ≤Nx −1 and 1 ≤q ≤Ny −1. Given an initial condition φ0, function
φm will be approximated by Φm with
Φm

[xp−1/2, xp+1/2]×[yq−1/2, yq+1/2]
= Φm
p,q
The Lax-Friedrichs method for problem (14) can be written in conservative form as follows:
Φm+1
p,q
= Φm
p,q −τ
∆x

F(Φm
p,q, Φm
p+1,q) −F(Φm
p−1,q, Φm
p,q)

where
F(Φm
p,q, Φm
p+1,q) = ∆x
2τ (Φm
p,q −Φm
p+1,q) + 1
2

(v[ρm
p,q] cos θ)Φm
p,q + (v[ρm
p+1,q] cos θ)Φm
p+1,q

.
Step 2
Let φ0 = fi,k+ 1
3 . Problem (12) can be rewritten as



∂φ
∂t + ∂
∂y ((v[ρ] sin θ)φ(t, x)) = 0 on (t0, tf),
φ(t0, x) = φ0
Similarly to step 1, we use the conservative Lax-Friedrichs scheme:
Φm+1
p,q
= Φm
p,q −τ
∆y

F(Φm
p,q, Φm
p,q+1) −F(Φm
p,q−1Φm
p,q)

where
F(Φm
p,q, Φm
p,q+1) = ∆y
2τ (Φm
p,q −Φm
p,q+1) + 1
2

(v[ρm
p,q] sin θ)Φm
p,q + (v[ρm
p,q+1] sin θ)Φm
p,q+1

.
Step 3
Let J = J i and φ0 = fi,k+ 2
3 . Problem (13) can be rewritten as



∂φ
∂t = J [f](t, x) on (t0, tf),
φ(t0, x) = φ0.
For the approximation of the above problem, we use the Forward Euler scheme:
Φm+1
p,q
= Φm
p,q + τ

J m[F m]

,


## Page 15


where F m is the approximation of the reduced distribution function (1) at time tm.
For stability, the subtime step τ is chosen to satisfy the Courant-Friedrichs-Lewy (CFL) condi-
tion (see, e.g., [30]):
max
(
τ
∆x,
τ
∆y
)
≤1.
4
Numerical results
We present a series of numerical results to showcase the features of our model. We start from
the simulation of evacuation from a room with one exit in Section 4.1. We use this ﬁrst test to
validate our implementation of the model presented in Section 2 against the results in [1].
In
order to further validate our software, in Section 4.2 we compare our numerical results with the
experimental data reported in [40], where the authors study the evacuation from a room with two
exits. Our successfully validated code is then used to study evacuation from a room with obstacles
in Section 4.3 and lane formation in a corridor in Section 4.4.
For all the simulations, we consider eight diﬀerent velocity directions Nd = 8 in the discrete set:
Iθ =

θi = i −1
8
2π : i = 1, . . . , 8

.
4.1
Evacuation from a room with one exit
This ﬁrst test case is taken from [1].
The computational domain encloses a square room with
side 10 m with an exit door located in the middle of the right side. The exit size is 2.6 m. The
computational domain is larger than the room itself to follow the motion of the pedestrian also
once they have left the room. We aim at simulating the evacuation of 46 people located inside the
room and initially distributed into two equal-area circular clusters. See Figure 3, top left panel.
The two groups are initially moving against the each other with opposite initial directions θ3 and
θ7. Following [1], simulations are performed with ε = 0.4.
In order to work with dimensionless quantities as described in Section 2, we deﬁne the following
reference quantities: D = 10
√
2 m, VM = 2 m/s, T = D/VM = 5
√
2 s, and ρM = 7 people/m2.
However, once the results are computed we convert them back to dimensional quantities.
In order to understand what level of reﬁnement is needed for the mesh, we consider three
diﬀerent meshes:
- coarse mesh with ∆x = ∆y = 0.5 m;
- medium mesh with ∆x = ∆y = 0.25 m;
- ﬁne mesh with ∆x = ∆y = 0.125 m.
Similarly, we consider three diﬀerent time steps: a large time step ∆tlarge = 1.5 s, a medium time
step ∆tmedium = 0.75 s, and a small time step ∆tsmall = 0.375 s. The value of M for the Lie


## Page 16


splitting scheme is set to 3. Figure 3 shows the density computed with medium mesh and ∆tmedium
at times t = 0, 1.5, 3, 6, 10.5, 13.5 s.
time = 0
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
?
6
time = 1.5000
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
time = 3.0000
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
time = 6.0000
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
time = 10.5000
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
time = 13.5000
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
Figure 3: Evacuation process of 46 pedestrians grouped into two clusters with opposite initial
directions θ3 and θ7 using the medium mesh and ∆tmedium for time t = 0, 1.5, 3, 6, 10.5, 13.5 s. The
color refers to density.
Figure 4 (A) reports the number of pedestrians left in the room computed with the following
combinations of mesh and time step: coarse mesh and ∆large, coarse mesh and ∆medium, coarse
mesh and ∆small, medium mesh and ∆medium, medium mesh and ∆small, and ﬁne mesh and ∆small.
In all the cases the total evacuation time is around 18 s, which agrees well with the results reported
in [1]. However, we see that the evacuation dynamics varies when the mesh and time step change.
In fact, from Figure 4 (A) one can observe that as the time step gets smaller with a given mesh
people walk slightly faster, while as the mesh gets ﬁner with a given time step pedestrians walk
slightly slower. When using operator splitting methods, it is advised to reduce the time step as the
mesh is reﬁned (see, e.g. [23]). So, for ease of comparison in Figure 4 (B) we report only the results
computed with coarse mesh and ∆tlarge, medium mesh and ∆tmedium, ﬁne mesh and ∆tsmall. We
can see very good agreement for those three curves.
Next, we consider the same room as in the previous test but we vary the exit size. We locate
the exit symmetrically with respect to the room centerline and let the exit size vary from 1.5 m to
4 m. We consider the medium meshes and ∆tmedium mentioned before since Figure 4 show that is
an appropriate choice for the problem under consideration. All the other model and discretization
parameters are set like in the previous test. Figure 5 shows the total evacuation time as a function


## Page 17


0
5
10
15
20
25
30
time (s)
0
10
20
30
40
50
Number of pedestrians
  coarse mesh, 
 tlarge
  coarse mesh, 
 tmedium
  coarse mesh, 
 tsmall
medium mesh, 
 tmedium
medium mesh, 
 tsmall
       fine mesh, 
 tsmall
(a) Number of pedestrians vs time
0
5
10
15
20
25
30
time (s)
0
10
20
30
40
50
Number of pedestrians
  coarse mesh, 
 tlarge
medium mesh, 
 tmedium
       fine mesh, 
 tsmall
(b) Selected curves from (A)
Figure 4: (A) Number of pedestrians inside the room over time computed with six diﬀerent combi-
nations of mesh and time step. For ease of comparison, (B) shows only the curves in (A) obtained
with simultaneous reﬁnements of mesh and time step.
of the exit size.
First, we notice that our results are in very good agreement with the results
reported in [1]. As expected, the total evacuation time decreases with the exit size, but that once
the exit is large enough for the crowd contained in the room the evacuation time does not change
signiﬁcantly if the exit is further enlarged.
1
1.5
2
2.5
3
3.5
4
4.5
Exit size (m)
17
18
19
20
21
22
Evacuation time (s)
medium mesh, 
 tmedium
(a) Our results
1
1.5
2
2.5
3
3.5
4
4.5
Exit size (m)
17
18
19
20
21
22
Evacuation time (s)
(b) Results from [1]
Figure 5: Computed evacuation time from the room with one exit versus the exit size: (A) our
results and (B) results from [1].


## Page 18


As last test for the room with one exit, we computed the total evacuation time from a room
with variable exit size for diﬀerent values of ε. The results did not show any visible diﬀerence
from the ones displayed in Figure 5 (A), which corresponds to ε = 0.4, and thus are not reported
here. This test case is probably too simple to see any diﬀerence in the crowd dynamics when (F3),
i.e. the tendency avoid the crowd, is dominant over (F4), i.e. the tendency to follow the crowd, and
viceversa.
4.2
Evacuation from a room with two exits
After validating our software against the numerical results in [1], we proceed with the validation
against the experimental data reported in [40].
The computational domain corresponds to the
setting studied in [40]: a room of side 10 m with diﬀerent sized exits placed on on the right side:
exit 1 with size 0.7 m and exit 2 with size 1.1 m. The distance between the two exits is 3 m. See
Figure 6.
time = 0
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
-
-
2
1
Figure 6: Computational domain corresponding to the experimental set-up in [40] and initial density
and direction (i.e., θ1) for the experiment with 138 pedestrians.
The data in [40] refer to ten trials: 2 trials with 18 pedestrians, 6 trials with 40 pedestrians,
and 2 trials with 138 pedestrians. In the experiments with 18 and 40 pedestrians (and so in the
simulation as well), the group is initially positioned in a square located symmetrically with respect
to the horizontal axis of the room and towards the back of the room with linearly increasing people
density from the front to the back. In the experiments with 138 pedestrians, pedestrians are initially
distributed as follows: a ﬁrst group of 90 people is positioned in a rectangle in the middle of the
room, while the remaining 48 people are positioned in a square behind the ﬁrst group. Thus, we
adopt the same conﬁguration in the simulations. We impose constant density in the rectangle and
prescribe a linearly increasing density from the front to the back of the square. See Figure 6. In all
the cases, the pedestrians are given initial direction θ1. For all the simulations, we use the medium
mesh and ∆tsmall considered in Section 4.1.


## Page 19


To compute the mean density DV and mean ﬂow rate FV we use the Voronoi method [38]:
DV (t) =
P
x∈ω ρ(t, x)
| ω |
,
FV (t) = DV VV E,
(15)
where VV is the mean velocity modulus over the area ω and E is the exit width. We choose two
4 m2 areas in front of the exits as ω. The mean density and mean ﬂow rate computed from our
simulations are shown in Figure 7 (A) and (B). Figure 7 (C) and (D) report the measured mean
density and mean ﬂow rate form the experiments in [40]. We see very good agreement between
computed and measured quantities for the 40 and 138 people cases, while there is no good agreement
for the 18 people case. This is to be expected since the kinetic approach is not meant to simulate
the dynamics of a small number of pedestrians. With this test we concludes the validation of our
software.
0
0.5
1
1.5
2
2.5
0
0.5
1
1.5
2
2.5
138 people
  40 people
  18 people
Exit 1
Exit 2
(a) Computed DV
0.5
1
1.5
2
2.5
3
3.5
0.5
1
1.5
2
2.5
3
3.5
138 people
  40 people
  18 people
Exit 1
Exit 2
(b) Computed FV
0
0.5
1
1.5
2
2.5
0
0.5
1
1.5
2
2.5
138 people
  40 people
  18 people
Exit 1
Exit 2
(c) Measured DV
0.5
1
1.5
2
2.5
3
3.5
0.5
1
1.5
2
2.5
3
3.5
138 people
  40people
  18 people
Exit 1
Exit 2
(d) Measured FV
Figure 7: Computed (A) mean density DV and (B) mean ﬂow rate FV as deﬁned in (15), and
measured (C) mean density and (D) mean ﬂow rate from [40].
So far, we have only considered velocity modulus v as deﬁned (3), which uses a cubic polynomial


## Page 20


outside the free ﬂow regime. For the two exit test, we take into consideration other possible choices:
vpurple(ρ) = (1 + cos((ρ −0.2)
2
3 π/0.8
2
3 ))/2,
vorange(ρ) = (1 + cos((ρ −0.2)
1
2 π/0.8
1
2 ))/2,
vblue(ρ) = (1 + cos((ρ −0.2)
1
3 π/0.8
1
3 ))/2.
(16)
See Figure 8 (A). We repeat the test with 138 pedestrians for all the above velocity moduli. The
corresponding number of pedestrians in the room versus times is shown in Figure 8 (B). For a
given density ρ in the slowdown zone, we have v(ρ) > vpurple(ρ) > vorange(ρ) > vblue(ρ). Thus, it
is not surprising the the total evacuation time increases as we pass from the original deﬁnition of
velocity modulus in (3) to vblue through vpurple and vorange. To further illustrate the diﬀerence in
the evacuation process when the above velocity moduli are used, in Figure 9 we display the density
and velocity modulus (with selected velocity vectors) at time t = 15 when using the three velocity
moduli.
0
0.2
0.4
0.6
0.8
1
Density 
0
0.2
0.4
0.6
0.8
1
Velocity modulus v
    Free flowzone
 Original velocity
   Purple velocity
 Orange velocity
      Blue velocity
(a) Diﬀerent velocity moduli
0
5
10
15
20
25
30
35
time (s)
0
20
40
60
80
100
120
140
Number of pedestrians
 Original velocity
   Purple velocity
 Orange velocity
      Blue velocity
(b) Number of pedestrians
Figure 8: (A) Diﬀerent velocity moduli under consideration and (B) corresponding number of
pedestrians in the room versus time for the 138 pedestrian case.
Next, we investigate the relationship between evacuation time and the width ratio of the two
exits. We ﬁx the size and position of exit 1, and the position of the center of exit 2, while the size
of exit 2 varies. See Figure 10 (A) for the widths of exit 2 under consideration and corresponding
width ratios. We consider two scenarios: the group of 40 people with velocity modulus (3) and
the group of 138 people with the blue velocity modulus (16). In both cases, all other model and
discretization parameters are set like for the results reported in Figure 7. Figure 10 (B) shows the
total evacuation time versus the exit width ratio for both scenarios. As expected, when the ratio
of exit 2 width/exit 1 width increases the total evacuation time decreases.


## Page 21


time = 15.0000
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
time = 15.0000
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
time = 15.0000
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
Figure 9: Density (top) and velocity magnitude with selected velocity vectors (bottom) for the
evacuation process of 138 pedestrians with the purple (left), orange (middle), and blue (right)
velocity moduli at time t = 15 s.
4.3
Evacuation from a room with obstacles
In the model introduced in Section 2.1, parameter α represents the quality of the environment,
which inﬂuences also the maximal dimensionless velocity modulus (3) a pedestrian can reach. In
theory, parameter α = 0 forces pedestrians to stop, while the value α = 1 contributes to keep the
maximal velocity modulus. However, in practice this parameter alone is not suﬃcient to model
obstacles within the domain. To eﬀectively model the obstacles, we use the strategy reported in
Section 2.1.2.
We consider a square room of side 10 m with a 2.6 m wide exit located on the right wall as in
Section 4.1, with the following obstacle conﬁguration:
1. One obstacle close to the exit, i.e. in the middle of the right wall, with eﬀective area depicted
in Figure 11 (A).
2. Two obstacles close to the right wall, place symmetrically with respect to the exit.
See
Figure 11 (B) for the eﬀective area of both obstacles.
Pedestrians are initially distributed in a rectangular region with constant density ρ = 0.80, as
shown in Figure 11. The total number of of pedestrians is 44. The initial direction is θ1.
Figure 12 and 13 show the evacuation process for conﬁguration 1 when α = 1 and α = 0 in the
eﬀective area, respectively. As explained in Section 2.1.2, when α = 1 (resp., α = 0) pedestrians


## Page 22


2
2
1
(a) Exit 2 width and width ratios
1
2
3
4
The ratio of Exit     / Exit
16
18
20
22
24
26
28
30
32
Evacuation time (s)
  40 pedestrians, Original velocity
138 pedestrians, Blue velocity
2
1
(b) Evacuation time vs width ratio
Figure 10: (A) Widths of exit 2 under consideration and corresponding width ratios and (B)
evacuation time versus width ratios for two diﬀerent scenarios.
time = 0
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
-
(a) Conﬁguration 1
time = 0
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
-
(b) Conﬁguration 2
Figure 11: Computational domain with eﬀective area for (A) an obstacle placed in the middle of
the room, towards the exit, and (B) two obstacles placed symmetrically with respect to the exit.
avoid the front (resp., back) part of the eﬀective area. Moreover, the shape of the real obstacle
is diﬀerent: it is square for α = 1, while for α = 0 it is slender. These ﬁndings are conﬁrmed by
Figure 14 and 15, which show the evacuation process for conﬁguration 2 when α = 1 and α = 0 in
the eﬀective area, respectively.
Finally, Figure 16 compares the evacuation times for the room with no obstacles (α = 1 every-
where in the domain), and for conﬁgurations 1 and 2 for α = 1 and α = 0 in the eﬀective area.


## Page 23


time = 0
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
-
time = 3.0000
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
time = 6.0000
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
time = 7.5000
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
time = 9.0000
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
time = 13.5000
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
Figure 12: Conﬁguration 1 with α = 1 in the eﬀective area: computed density for t = 0, 3, 6, 7.5,
9, 13.5 s. The small square within the eﬀective area represents the real obstacle.
Obviously, the shortest evacuation time is for the room with no obstacles and overall good quality
of the environment. The evacuation time is slightly larger when there is one or two obstacles and
α is equal to 1 in the eﬀective area. When we compare Figure 12 and 13 at t = 13.5 s, it seems
that roughly the same number of people is left in the room. However, the small group of people in
the eﬀective area in Figure 13 has velocity modulus close 0 since α is equal to 0 there and thus the
overall evacuation process takes longer. The same happens in Figure 15.
4.4
Lane formation
In this section, we assess the ability of our model to reproduce an empirically observed phenomenon:
formation of lanes in a corridor when two or more groups of pedestrians have opposite walking
directions [25]. We consider a computational domain of length L = 20 m and width H = 5 m and
we impose periodic boundary conditions on the short edges. The reference quantities we use for
this test are: D = 5
√
17 m, VM = 2 m/s, and ρM = 7 per/m2. See Section 2. The reference time
is thus TM = 5
√
17/2 s.
We generate a mesh with ∆x = ∆y = 0.2 m and set ∆t = 0.3 s. We run two tests: in one
98 people are present in the computational domain, while in the other we increase the number
of people to 188.
Pedestrians are initially distributed into four equal-area rectangular clusters
with a parabolic density distribution with maximum density ρ = 1 in the center and minimum


## Page 24


time = 0
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
-
time = 3.0000
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
time = 6.0000
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
time = 7.5000
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
time = 9.0000
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
time = 13.5000
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
Figure 13: Conﬁguration 1 with α = 0 in the eﬀective area: computed density for t = 0, 3, 6, 7.5,
9, 13.5 s. The small rectangle within the eﬀective area represents the real obstacle.
density ρ = 0.6. The groups at the opposite ends of the corridor initially move with opposite initial
directions θ1 and θ5. See the top left panel in Figure 17 and 18. The rest of Figure 17 and 18 shows
the evolution of the pedestrian dynamics. From both pictures, we see that pedestrians try to avoid
contact by changing the direction, which leads to sorting, separation, and lane formation.
5
Conclusion
We considered a kinetic theory approach to model pedestrian dynamics in bounded domain and
adapted it to handle obstacles. For the numerical approximation of the solution to our model, we
applied the Lie splitting scheme which breaks the problem into two pure advection problems and
a problem involving the interaction with the environment and other pedestrians.
Several test cases have been considered in order to show the ability of the model to reproduce
qualitatively:
- evacuation from a room with one exit, without and with obstacles;
- evacuation from a room with two exits and no obstacles;
- lane formation.
In the case of the room with two exits and no obstacles, we also presented a quantitative comparison
with experimental data. Numerical results and experimental data are in very good agreement for
medium and medium-to-large groups of people. With the conﬁdence in the model given by the


## Page 25


time = 0
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
-
time = 3.0000
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
time = 6.0000
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
time = 7.5000
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
time = 10.5000
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
time = 13.5000
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
Figure 14: Conﬁguration 2 with α = 1 in the eﬀective area: computed density for t = 0, 3, 6, 7.5,
10.5, 13.5 s. The small square within the eﬀective area represents the real obstacle.
experimental validation, we performed numerical tests to study evacuation for diﬀerent scenarios
in terms of exit sizes, obstacle shapes, and velocity moduli.
Acknowledgements
This work has been partially supported by NSF through grant DMS-1620384.
References
[1] J. P. Agnelli, F. Colasuonno and D. Knopoﬀ, A kinetic theory approach to the dynamics
of crowd evacuation from bounded domains, Mathematical Models and Methods in Applied
Sciences, 25 (2015), 109–129.
[2] G. Antonini, M. Bierlaire and M. Weber, Discrete choice models of pedestrian walking behav-
ior, Transportation Research Part B: Methodological, 40 (2006), 667–687.
[3]
M. Asano, T. Iryo and M. Kuwahara, Microscopic pedestrian simulation model combined
with a tactical model for route choice behaviour, Transportation Research Part C: Emerging
Technologies, 18 (2010), 842–855.


## Page 26


time = 0
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
-
time = 3.0000
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
time = 6.0000
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
time = 7.5000
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
time = 10.5000
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
time = 13.5000
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
Figure 15: Conﬁguration 2 with α = 0 in the eﬀective area: computed density for t = 0, 3, 6, 7.5,
10.5, 13.5 s s. The small rectangle within the eﬀective area represents the real obstacle.
No
One
Two
Position
15
20
25
30
35
40
45
Evacuation time (s)
 = 1
 = 0
Figure 16: Evacuation times for the room with no obstacles (α = 1 everywhere in the domain), for
room with one and two obstacles with α = 1 and α = 0 in the eﬀective area.
[4] S. Bandini, S. Manzoni and G. Vizzari, Agent based modeling and simulation: An informatics
perspective, Journal of Artiﬁcial Societies and Social Simulation, 12 (2009).
[5] N. Bellomo and A. Bellouquid, On the modeling of crowd dynamics: Looking at the beautiful
shapes of swarms, Networks and Heterogeneous Media, 6 (2011), 383–399.
[6] N. Bellomo, A. Bellouquid and D. Knopoﬀ, From the microscale to collective crowd dynamics,


## Page 27


Figure 17: The movement process of 98 pedestrians grouped into four clusters with opposite initial
direction θ1 and θ5 in the periodic corridor for t = 0, 4.2, 12.3, 19.8, 33.9, 50.7, 72.3 s, respectively.
Figure 18: The movement process of 188 pedestrians grouped into four clusters with initial opposite
direction θ1 and θ5 in the periodic corridor for t = 0, 4.5, 12.6, 19.8, 33.9, 50.7, 89.7 s, respectively.
Society for Industrial and Applied Mathematics Multiscale Modeling and Simulation, 11 (2013),


## Page 28


943–963.
[7]
N. Bellomo, A. Bellouquid, L. Gibelli and N. Outada,
A Quest Towards a Mathematical
Theory of Living Systems, Modeling and Simulation in Science, Engineering and Technology,
Birkhauser, 2017.
[8]
N. Bellomo and C. Dogbe,
On the modeling of traﬃc and crowds: A survey of models,
speculations, and perspectives, Society for Industrial and Applied Mathematics Review, 53
(2011), 409–463.
[9]
N. Bellomo and L. Gibelli,
Toward a mathematical theory of behavioral-social dynamics
for pedestrian crowds,
Mathematical Models and Methods in Applied Sciences, 25 (2015),
2417–2437.
[10] N. Bellomo and L. Gibelli, Behavioral crowds: Modeling and Monte Carlo simulations toward
validation, Computers and Fluids, 141 (2016), 13–21.
[11] N. Bellomo, L. Gibelli and N. Outada, On the interplay between behavioral dynamics and
social interactions in human crowds, Kinetic and Related Models, 12 (2019), 397–409.
[12] N. Bellomo, D. Knopoﬀand J. Soler, On the diﬃcult interplay between life, “Complexity”,
and mathematical sciences, Mathematical Models and Methods in Applied Sciences, 23 (2013),
1861–1913.
[13]
N. Bellomo, B. Piccoli and A. Tosin,
Modeling crowd dynamics from a complex system
viewpoint, Mathematical Models and Methods in Applied Sciences, 22 (2012).
[14] V. J. Blue and J. L. Adler, Cellular automata microsimulation of bidirectional pedestrian
ﬂows, Journal of Transportation Research Record, 1678 (1999), 135–141.
[15] V. J. Blue and J. L. Adler, Cellular automata microsimulation for modeling bi-directional
pedestrian walkways, Transportation Research Part B: Methodological, 35 (2000), 293–312.
[16] C. Burstedde, K. Klauck, A. Schadschneider, J. Zittartz, Simulation of pedestrian dynamics
using a two-dimensional cellular automaton, Physica A: Statistical Mechanics and its Appli-
cations, 295 (2001), 507–525.
[17] N. Chooramun, P. J. Lawrence and E. R. Galea, An agent based evacuation model utilising
hybrid space discretisation, Safety Science, 50 (2012), 1685–1694.
[18] M. Chraibi, U. Kemloh, A. Schadschneider and A. Seyfried, Force-based models of pedestrian
dynamics, Networks and Heterogeneous Media, 6 (2011), 1556–1801.


## Page 29


[19]
M. Chraibi, A. Tordeux, A. Schadschneider and A. Seyfried, Modelling of Pedestrian and
Evacuation Dynamics, Encyclopedia of Complexity and Systems Science Series, 2019, 649–
669.
[20] J. Dai, X. Li and L. Liu, Simulation of pedestrian counter ﬂow through bottlenecks by using
an agent-based model,
Physica A: Statistical Mechanics and its Applications, 392 (2013),
2202–2211.
[21]
J. Dijkstra, J. Jessurun and H. Timmermans,
A multi-agent cellular automata model of
pedestrian movement, Pedestrian and Evacuation Dynamics, (2001), 173–181.
[22] B. Einarsson, Accuracy and Reliability in Scientiﬁc Computing, Society for Industrial and
Applied Mathematics, 2005.
[23] R. Glowinski, Finite Element Methods for Incompressible Viscous Flow, Handbook of numer-
ical analysis, 9. North-Holland, Amsterdam, 2003.
[24] D. Helbing, A mathematical model for the behavior of pedestrians, Behavioral Science, 36
(1991), 298–310.
[25] D. Helbing, I. J. Farkas, P. Molnar, and T. Vicsek, Simulation of pedestrian crowds in normal
and evacuation situations, Pedestrian and Evacuation Dynamics, 21 (2002), 21–58.
[26] D. Helbing and P. Molnar, Social force model for pedestrian dynamics, Physical Review E,
51 (1998), 4282–4286.
[27] D. Helbing and T. Vicsek, Optimal self-organization, New Journal of Physics, 1 (1999).
[28] R. L. Hughes, A continuum theory for the ﬂow of pedestrians, Transportation Research Part
B: Methodological, 36 (2002), 507–535.
[29] A. Johansson, D. Helbing and P. K. Shukla, Speciﬁcation of the social force pedestrian model
by evolutionary adjustment to video tracking data, Advances in Complex Systems, 10 (2007),
271–288.
[30] R. J. LeVeque, Numerical Methods for Conservation Laws, 2nd edition, Springer Science &
Business Media, 1992.
[31] X. Li, X. Yan, X. Li and J. Wang, Using cellular automata to investigate pedestrian conﬂicts
with vehicles in crosswalk at signalized intersection, Discrete Dynamics in Nature and Society,
(2012).
[32]
S. Liu, S. Lo, J. Ma and W. Wang,
An agent-based microscopic pedestrian ﬂow simula-
tion model for pedestrian traﬃc problems, IEEE Transactions on Intelligent Transportation
Systems, 15 (2014), 992–1001.


## Page 30


[33] J. Moussa¨ıd, D. Helbing, S. Garnier, A. Johansson, M. Combe and G. Theraulaz, Experi-
mental study of the behavioural mechanisms underlying self-organization in human crowds,
Proceedings of the Royal Society B: Biological Sciences, 276 (2009), 2755–2762.
[34]
A. Schadschneider, W. Klingsch, H. Kluepfel, T. Kretz, C. Rogsch, A. Seyfried,
Evacua-
tion dynamics: Empirical results, modeling and applications, Extreme Environmental Events:
Complexity in Forecasting and Early Warning, (2011), 517–550.
[35]
A. Schadschneider and A. Seyfried,
Empirical results for pedestrian dynamics and their
implications for modeling, Networks and Heterogeneous Media, 6 (2011), 545–560.
[36] A. Seyfried, O. Passon, B. Steﬀen, M. Boltes, T. Rupprecht and W. Klingsch, New insights
into pedestrian ﬂow through bottlenecks, Transportation Science, 43 (2009), 395–406.
[37] A. Shende, M. P. Singh and P. Kachroo, Optimization-Based feedback control for pedestrian
evacuation from an exit corridor, IEEE Transactions on Intelligent Transportation Systems,
12 (2011), 1167–1176.
[38] B. Steﬀen and A.Seyfried, Methods for measuring pedestrian density, ﬂow, speed and direction
with minimal scatter, Physica A: Statistical Mechanics and its Applications, 389 (2009), 1902–
1910.
[39] A. Turner and A. Penn, Encoding Natural Movement as an Agent-Based System: An In-
vestigation into Human Pedestrian Behaviour in the Built Environment, Environment and
Planning B: Planning and Design, 29 (2002), 473–490.
[40] A. U. K. Wagoum, A. Tordeux and W. Liao, Understanding human queuing behaviour at
exits: an empirical study, Royal Society Open Science, 4 (2017).
[41] J. A. Ward, A. J. Evans and N. S. Malleson, Dynamic calibration of agent-based models using
data assimilation, Royal Society Open Science, 3 (2016).
[42] J. Zhang, W. Klingsch, A. Schadschneider and A. Seyfried, Transitions in pedestrian fun-
damental diagrams of straight corridors and T-junctions, Journal of Statistical Mechanics:
Theory and Experiment, 6 (2011).
[43]
B. Zhou, X. Wang and X. Tang,
Understanding collective crowd behaviors: Learning a
Mixture model of Dynamic pedestrian-Agents, 2012 IEEE Conference on Computer Vision
and Pattern Recognition, (2012), 2871–2878.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1901_07620v3_a_kinetic_theory_approach_to_model_pedestrian_dynamics_in_bounded_domains_with_o
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1901_07620V3_A_KINETIC_THEORY_APPROACH_TO_MODEL_PEDESTRIAN_DYNAMICS_IN_BOUNDED_DOMAINS_WITH_O.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

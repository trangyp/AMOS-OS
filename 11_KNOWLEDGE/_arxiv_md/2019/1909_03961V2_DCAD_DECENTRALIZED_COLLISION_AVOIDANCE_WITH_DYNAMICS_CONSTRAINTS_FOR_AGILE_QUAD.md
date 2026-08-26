---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1909.03961v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1909.03961v2_DCAD__Decentralized_Collision_Avoidance_with_Dynamics_Constraints_for_Agile_Quad

> Source: 1909.03961v2_DCAD__Decentralized_Collision_Avoidance_with_Dynamics_Constraints_for_Agile_Quad.pdf

> Pages: 10

---


## Page 1


DCAD: Decentralized Collision Avoidance with Dynamics Constraints
for Agile Quadrotor Swarms
Senthil Hariharan Arul1 and Dinesh Manocha2
Abstract— We present a novel, decentralized collision avoid-
ance algorithm for navigating a swarm of quadrotors in dense
environments populated with static and dynamic obstacles. Our
algorithm relies on the concept of Optimal Reciprocal Collision
Avoidance (ORCA) and utilizes a ﬂatness-based Model Predic-
tive Control (MPC) to generate local collision-free trajectories
for each quadrotor. We feedforward linearize the non-linear
dynamics of the quadrotor and subsequently use this linearized
model in our MPC framework. Our method approach tends to
compute safe trajectories that avoid quadrotors from entering
each other’s downwash regions during close proximity maneu-
vers. In addition, we account for the uncertainty in the position
and velocity sensor data using Kalman ﬁlter. We evaluate the
performance of our algorithm with other state-of-the-art de-
centralized methods and demonstrate its superior performance
in terms of smoothness of generated trajectories and lower
probability of collision during high velocity maneuvers.
I. INTRODUCTION
Due to their agility, ease of deployment, decreasing costs,
and small size, quadrotors are extensively used in robotics
and related areas. Their 3-D navigation capabilities are fa-
vorable for tasks such as surveillance, target tracking, search
& rescue, etc. Many applications use a coordinating swarm
of quadrotors for efﬁciency, where large 3D regions can
be simultaneously covered by different quadrotors. Agile,
high-velocity quadrotor navigation is especially important
in applications involving disaster response, where time is
critical for effective rescue operations [1]. Further, for safe
implementation, it is important to avoid collisions with the
obstacles in the scene as well as other quadrotor agents dur-
ing the high-velocity maneuvers. Such applications require
navigation algorithms that can rapidly adapt to the changes
in the environment, account for sensor uncertainty, and scale
to a large number of swarm agents.
Many centralized [2], [3], [4], [5] and decentralized [6], [7]
planning approaches have been proposed for collision-free
navigation of quadrotors in a swarm. Centralized methods
scale poorly and are generally not adaptable to dynamic en-
vironments but can provide guarantees on trajectory smooth-
ness, optimality, etc. In contrast, decentralized methods are
scalable and are adaptable to changes in the environment, but
cannot provide such guarantees on the generated trajectories.
Quadrotor dynamics is non-linear due to the sinusoidal
relationships required to describe its orientation [8]. Collision
1Senthil
Hariharan
Arul
is
with
Department
of
Electrical
and
Computer Engineering, University of Maryland, College Park, USA
sarul1@umd.edu
2Dinesh Manocha is with the Department of Computer Science, Electrical
and Computer Engineering, University of Maryland, College Park, USA
dm@cs.umd.edu
avoidance methods that account for such non-linearities
either do not run in real-time [3], [4] or use a compu-
tationally expensive controller such as N-MPC [9], thus
limiting the available on-board computational power for
other applications like perception and communication. In
addition, an N-MPC solution is susceptible to converging
to local minima [10]. In contrast, other methods
[6], [7]
reduce the complexity by linearizing the quadrotor dynamics
about an equilibrium point (usually about the quadrotor’s
hover conﬁguration). This linearized model is valid near
the equilibrium point, but its performance decreases during
aggressive (high-velocity) maneuvers, where large pitch and
roll is required [11]. Further, to account for downwash in the
collision avoidance algorithm, the quadrotors are modeled as
axis-aligned ellipsoids, disregarding the quadrotor orientation
[5], [7], though the downwash region would vary in relation
to the quadrotor orientation [12].
Main Results: We present a novel decentralized realtime
approach (DCAD) for navigation of large quadrotor swarms
in dynamic environments. Our approach is general and makes
no assumptions about the obstacles or the environment. To
handle the non-linear dynamics constraints and enable fast
maneuvers, we present two novel algorithms:
1) An on-line collision avoidance algorithm for nav-
igation in dynamic environments that accounts for
quadrotor dynamics using ﬂatness-based feedforward
linearization and MPC. In contrast to linearizing about
the hover point, we can still incorporate the non-
linearities in the system using an inverse map.
2) An algorithm to incorporate downwash into the con-
struction of collision avoidance constraints based on
ORCA. In contrast to using axis-aligned ellipsoids
to consider downwash, our algorithm incorporates
quadrotor attitude by modeling neighboring pair of
quadrotors as a combination of a sphere and an ori-
ented ellipsoid.
We combine these algorithms with ORCA constraints for col-
lision avoidance [13] to compute the local trajectory for each
quadrotor in a decentralized manner. In addition, our method
incorporates sensing uncertainty using Kalman ﬁltering and
provides scalability with respect to the number of agents.
In practice, our algorithm takes about 5 ms on average
to calculate a new collision-avoiding control input for an
agent in the presence of 8 obstacles. Moreover, our DCAD
results in better behaviour in terms of smoother trajectories
and collision avoidance during high-velocity maneuvers, as
compared to prior decentralized methods based on ORCA
arXiv:1909.03961v2  [cs.RO]  2 Dec 2019


## Page 2


[14], AVO [15], LQR-obstacles [7], and LSwarm [16].
The rest of the paper is organized as follows. In Section II,
we summarize state-of-the-art methods in collision avoidance
and quadrotor control. In Section III, we introduce our
quadrotor model and the notion of feedforward lineariza-
tion. In Section IV, we present our decentralized collision
avoidance algorithm that considers dynamics constraints. In
Section V, we describe its implementation and highlight the
beneﬁts over prior methods. compared to other state-of-the-
art methods.
II. PREVIOUS WORK
In this section, we give a brief overview of prior work in
quadrotor control and collision avoidance.
A. Quadrotor Control
In prior literature [6], [7], [17], [18], quadrotor dynamics
is handled by linearizing the system dynamics about the
hover point to facilitate the use of a linear controller such
as an LQR [19] or a linear Model Predictive Control (MPC)
[20]. These methods facilitate reduced computational over-
head compared to non-linear controllers, thereby allowing
more on-board processing power for other applications like
perception or communication. However, aggressive (high-
velocity, high-acceleration) maneuvers require large attitude
deviations from the hover point, and the performance is
reduced when hover-point linearization is used [21]. Kamel
et al. [22] and Zhu et al. [9] present a non-linear Model
Predictive Control-based (NMPC-based) collision avoidance
method, that models the full non-linear quadrotor dynamics.
The NMPC-based algorithm [9] takes about 16ms to compute
a collision avoiding control input for a quadrotor with 6
neighboring obstacles. Flatness-based feedforward controller
for trajectory tracking is proposed in [23], [10]. Unlike
the methods that linearize about the hover point, these
feedforward methods do not make small angle assumptions
about the roll and pitch of the quadrotors. Controllers based
on feedforward linearization and ﬂatness have shown bet-
ter performance in terms of computation time and, unlike
NMPC, they are not sensitive to the choice of the initial
trajectory or susceptible to local minima convergence issues
[10]. Because of these advantages, we use ﬂatness-based
feedforward linearization to model the quadrotor dynamics
in our algorithm.
B. Collision Avoidance
Prior research can be grouped into two broad areas,
centralized trajectory generation and reactive collision avoid-
ance.
1) Centralized Trajectory Generation: Augugliaro et al.
[3] and Chen et al. [4] propose a centralized algorithm that
relies on solving a sequential convex program to generate
collision-free trajectories for a swarm. Kushleyev et al. [2]
present a method that generates collision-free trajectories
for a swarm of quadrotors by solving a Mixed Integer
Quadratic Program (MIQP). Due to the high computational
overhead and centralized nature of MIQP, the algorithm
scales exponentially with the number of agents. Preiss et
al. [5] reduce the computation cost by decomposing the
collision-free trajectory generation problem into a discrete
collision-free path planner and a trajectory optimizer. Hamer
et al. [24] present a parallel formulation for fast generation of
collision-free trajectories in multi-agent scenarios. Central-
ized trajectory generation can guarantee optimality in terms
of minimum path length, time to reach the goal, or fuel
cost. However, these methods can be limited in terms of
real-world urban scenarios due to the dynamic nature of the
environment, a sudden change in mission, or covering very
large areas.
2) Reactive Collision Avoidance: Velocity Obstacle (VO)
[25]-based methods such as RVO [13] provide decentralized
collision avoidance by locally altering the trajectories for
agents with single-integrator dynamics. Constraints in RVO
[13] were linearly approximated in ORCA [14] and extended
to double integrator dynamics in AVO [15]. Ruﬂi et al. [26]
extend RVO to generate nth order continuous trajectories.
Berg et al. [6] and Bareiss et al. [7] extend VO to control
obstacles for agents with linear dynamics. Moreover, they
demonstrate the algorithm for a large swarm of quadrotors
by linearizing the quadrotor dynamics about the hover con-
ﬁguration. This type of linearized model is valid only for
small roll and pitch angles about the hover conﬁguration
[11] and not for large angular deviation as during high-
velocity ﬂights. Further, control obstacles may also result in
non-convex solution space and the new velocity is generally
computed from a convex subset of this solution space. Cheng
et al. [27] avoid this convex approximation by using an MPC-
based method for linear systems. Morgan et al. [28] present a
decentralized algorithm based on sequential convex program-
ming (SCP). Due to its higher computational complexity,
SCP is not favorable for fast online computation. Baca et
al. [29] present a control and collision avoidance algorithm,
where collisions are resolved by priority based altitude
variations. In many ways, this approach is complimentary to
our method. However, collision avoidance through altitude
variations may be unsuitable when large number of agents
operate in indoor scenarios due to limits on ceiling height.
Reactive methods are suitable for dynamic environments
because they only use the local position and velocity data for
the neighboring agents and obstacles (i.e. state information).
However, these reactive methods cannot provide any global
guarantees.
C. Downwash
In dense scenarios, multiple quadrotors may have to ma-
neuver in close proximity to each other. Downwash causes a
region of instability below the rotors of a quadrotor and any
other quadrotor entering this region may lose control or result
in unstable behavior [5]. In prior literature, the downwash
effect is considered in collision avoidance by modeling the
agents as axis-aligned ellipsoids [7], [5] or cylinders [30],
[12], which encourages a larger separation along the Z-
axis. Quadrotor roll and pitch affect the downwash region,
and the ellipsoid or cylinder must be rotated with respect


## Page 3


TABLE I: Notation and symbols.
Notation
Deﬁnition
W
World Frame deﬁned by unit vectors xW, yW, and zW
along the standard X, Y and Z axes
B
Body Frame attached to the center of mass, deﬁned by
the axes xB, yB, and zB
r
3-D position of the center of mass of the quadrotor
given by [x,y,z]
v
Velocity of the quadrotor given by [˙x, ˙y, ˙z]
a,j
Acceleration and jerk of the quadrotor given by second
and third derivative of position respectively
φ,θ,ψ
Roll, pitch and yaw of the quadrotor.
R
Rotation matrix of quadrotor body frame (B) w.r.t
world frame (W )
T
Net thrust in body ﬁxed coordinate frame
m
Mass of quadrotor
ω
Angular velocity in body ﬁxed coordinate frame given
by [p,q,r]
x
Quadrotor State space
u
Control input to the quadrotor
uc
Input to the inner loop controller
VOτ
A|B
Velocity Obstacle for agent A induced by agent B over
a time horizon τ
ORCAτ
A|B
Collision avoiding velocity set for agent A induced by
agent B over a time horizon τ
Vmax
Maximum value of velocity allowed by the quadrotor
dynamics
Amax
Maximum value of acceleration allowed by the
quadrotor dyamics
to the quadrotor orientation for accurate modeling [12].
For simplicity, the quadrotors are modeled as axis-aligned
ellipsoids and the radius of the ellipsoid/cylinder is increased
by a safety threshold to account for roll and pitch [12] [30].
III. PRELIMINARIES
In this section, we introduce our assumptions, notation,
and provide an overview of the concepts of differential ﬂat-
ness and feedforward linearization. We describe the quadro-
tor model and the non-linear transformation used in our
collision avoidance algorithm (Section IV).
A. Symbols and Notation
The symbols and notations used in this paper are deﬁned
in Table I.
B. Differential Flatness
A nonlinear system given by ˙x = f(x,u) is differentially
ﬂat if there exists a set ζ (ﬂat output) whose elements,
expressed
as
ζ
= [ζ1,ζ2,...,ζm],
are
differentially
independent; ζ
and their derivatives can be used to
construct the system state space and control inputs [31]
[32]. The quadrotor model we consider is described below
and, from [33], we know that the quadrotor dynamics
is differentially ﬂat for the ﬂat output set given by
ζ = [ζ1,ζ2,ζ3,ζ4] = [x,y,z,ψ].
Quadrotor Model: The state space and the control input for
the quadrotor are given by
x = [x,y,z, ˙x, ˙y, ˙z,φ,θ,ψ, p,q,r],
(1)
u = [T, ˙φ, ˙θ, ˙ψ].
(2)
The quadrotor dynamics can be represented by the following
set of equations:
˙r = v,
(3)
m¯a = −mgzW +TzB,
(4)
˙R = R×ωT,
(5)
˙ω = J−1[−ω ×Jω +τ].
(6)
C. Feedforward Linearization
Hagenmeyer et al. [32] introduce the notion of exact feed-
forward linearization based on differential ﬂatness. Given
a non-linear, differentially ﬂat system ˙x = f(x,u) and a
sufﬁciently smooth trajectory in the ﬂat output ζref , the
system can be represented as a linear ﬂat model given as
˙ξ = Aξ +Bν,
(7)
ν = ψ(ξ,u, ˙u,...,uσ),
(8)
when a nominal input (9) is applied to the non-linear system,
provided the initial condition (10) is satisﬁed.
u∗= ψ−1(ξ desired,νdesired),
(9)
ξ(0) = ξ desired(0).
(10)
Here, ξ is the linear multi-variable Brunovsky form, repre-
sented as
ξ = [ζ1, ˙ζ1,...,ζ ρ1−1
1
,ζ2,...,ζm−1,
˙
ζm−1,...,ζ ρm−1
m−1 ],
(11)
and ν represents the new control input in the ﬂat space. The
desired ﬂat state (ξ desired) and ﬂat input (νdesired) can be
computed from ζref . In Equation (8), σ is the maximum
order of differentiation of u required to describe ν.
Equation (9) represents the non-linear transformation re-
quired to obtain u from the ﬂat input. We observe from Etal
et al. [34] that we require the third derivative of position (r)
and the ﬁrst derivative of yaw (ψ) to express the state and
the control input. Hence, we choose the ﬂat state space z and
the ﬂat input ν as
z = [r,v,a,ψ],
ν = [j, ˙ψ].
In our method, ﬂatness-based feedforward linearization pro-
vides the beneﬁt of reducing the computation overload by
linearizing the quadrotor dynamics to linear ﬂat model while
still allowing us to handle the non-linearities using a non-
linear map. We use a ﬂatness-based MPC that is similar
to the one used in [10] to generate a feasible collision-free
trajectory. The non-linear map (Eqn. 13) is described below:
Non-linear Map:
The control input u can be represented
in terms of ζ and its derivative using the following relation,
u1 = T = mg+ ¨ζ3
R33
,
(12)


u2
u3
u4

=


˙φ
˙θ
˙ψ

= 1
T


−Y T
B
−XT
B /cosφ
0

j + ˙ψref


sinθ
−cosθtanφ
1

.
(13)


## Page 4


Eqn. 13 gives the non-linear map that transforms the ﬂat
inputs to the quadrotor inputs [34].
We assume the presence of an inner-loop attitude con-
troller that can track the attitude values and takes as input
uc = [T,φcmd,θcmd, ˙ψ]. The inner loop control dynamics is
given by
˙φ = 1
τφ
(Kφφcmd −φ),
(14)
˙θ = 1
τθ
(Kθθcmd −θ),
(15)
˙ψ = ψre f .
(16)
From Eqn. (12) - (16) we can compute uc in terms of ζ and
its derivative, which is then applied as input to the inner loop
controller.
D. Assumptions on Swarm Agents
We assume that each agent has access to a reference
trajectory in ﬂat output space ζre f = [x,y,z,ψ] that considers
static obstacles in the environment. The reference trajectory
is assumed to be sufﬁciently smooth and can be generated
prior to ﬂight using any trajectory generation method, such
as [35]. In our case, we assume the yaw orientation of the
quadrotor is not important and we take ψ = 0 in the reference
trajectory. Though the reference trajectory considers static
obstacles, collision avoidance can deviate the agent from
its reference trajectory causing them to collide with static
obstacle. Such issues are managed by constructing VO with
the closest point obstacle, as shown in [16]. We assume
the availability of position, velocity, and orientation of each
neighboring quadrotor/obstacle to each swarm agent at any
given time for generating ORCA constraints. Our collision
avoidance scheme is based on ORCA [14] and [27], and we
assume that neighboring agents and dynamic obstacle travel
at a constant velocity during the prediction horizon of the
MPC.
IV. COLLISION AVOIDANCE AND TRAJECTORY
COMPUTATION
In this section, we present our decentralized collision
avoidance algorithm for the quadrotor swarm. In our algo-
rithm, the quadrotor dynamics are handled in the ﬂat-MPC,
while ORCA planes are used as state constraints to generate
local, collision-free, downwash-aware trajectories. The high-
level overview of our algorithm is given in Fig. 1 and the
details are given below.
A. MPC
Model Predictive Control (MPC) is a receding horizon
planner that computes a control input based on the system
dynamics, input and state constraint, by minimizing an
objective function over a prediction horizon. Here, prediction
horizon (N) is a ﬁnite time horizon in the future [t, t+N].
In our method, we linearize the quadrotor model using
feedforward linearization, as mentioned in Section III, to
facilitate the use of a linear MPC. The linearized ﬂat state
space z and the ﬂat input ν are given by
z = [r,v,a,ψ],
ν = [j, ˙ψ].
At each time step, the MPC uses the linear ﬂat model (z)
to plan the state trajectories in the ﬂat space and to compute
a control input in the ﬂat input space ν. The optimization
problem minimizes the tracking error and ﬂat input (ν) while
satisfying the velocity constraints by ORCA and constraints
on jerk. The optimization problem is given by
minimize
N
∑
t=0
 ζref,t −ζt

Q
 ζref,t −ζt

+νtRνt
subject to
ξ0 = ξt
ξk+1 = Aξk +Bνk
|vx,k| ≤Vmax,x,|vy,k| ≤Vmax,y,|vz,k| ≤Vmax,z
|ax,k| ≤Amax,x,|ay,k| ≤Amax,y,|az,k| ≤Amax,z
ORCA
 Cξk+1,Cξneighbour,k+1

≤0
J (ξk,φmin,φmax,θmin,θmax) ≤0
∀k = 0,1,...,N −1.
(17)
Here ‘N’ is the number of prediction steps, ζref is the
reference trajectory, and the matrices Q and R are weights
that prioritize between minimizing the trajectory tracking
error and the control input. ξk represents the ﬂat state of
the agents and matrix C is such that Cξk gives the position,
velocity and orientation of the agent at time step k. ξneighbour,k
is the ﬂat state of the neighboring agent/obstacle at time step
k. During collision avoidance, the quadrotor may have to
deviate from its reference trajectory to avoid collision. In this
case, the initial state of the quadrotor agent may deviate from
the reference trajectory, the state feedback is used to satisfy
the initial condition requirement given by (10). Equation
ξ0 = ξt represents the state feedback. The ORCA velocity
constraints between the agent and its neighbors are repre-
sented by ORCA(Cξk+1,Cξneighbour,k+1) ≤0. The constraints
on the jerk are represented by J(ξk,φmin,φmax,θmin,θmax) ≤0,
and are computed as follows.
Constraints on Jerk: Assume the quadrotor can reach
a maximum and minimum roll and pitch angle given by
(φmax,φmin), and (θmax,θmin). Since the MPC computes a
control input in ﬂat input ν, the constraint on roll and
pitch need to be transformed to the ﬂat space to prevent
quadrotors from ﬂipping over during collision avoidance. At
any timestep, the maximum jerk that can be applied to the
system is dependent on the current state of the quadrotor,
including maximum and minimum limits on roll and pitch.
A maximum and minimum value for the roll rate
( ˙φmax, ˙φmin) and pitch rate ( ˙θmax, ˙θmin) can be computed using
φmax,φmin,θmax,θmin,ξ, Eqn. (14) and (15). To compute the
limits on jerk (jmin, jmax) at a given timestep, we re-write
Eqn. (13) as follows. The minimum jerk can be computed


## Page 5


Fig. 1: Collision avoidance framework for each agent: The
Flat-MPC incorporates the ORCA velocity constraints as
state constraints in the the optimization problem and com-
putes a feasible trajectory for the agents. The position,
velocity, and orientation of an agent and neighbours are used
in the ORCA block to compute a collision avoidance velocity
constraint that accounts for downwash.
as
jmin = min
˙φ, ˙θ
T

−Y T
B
−XT
B /cosφ
−1  ˙φ
˙θ

−˙ψre f

sinθ
−cosθtanφ

.
Similarly, we can compute jmax by maximizing the above
expression. The computed jmax and jmin values are used as
maximum and minimum jerk constraints, respectively, over
the entire prediction horizon.
MPC Output: As a result of the optimization, the MPC
generates the predicted state trajectory and computed control
input for each time step in the time horizon. The values for
the state and the control input (ν) are passed to the non-
linear map to compute the control input for the inner loop
attitude controller (uc) using the non-linear map (13).
B. Collision Avoidance
ORCA generates linear collision avoidance constraints,
which result in a convex set of feasible velocity [14]. In
our method, we incorporate ORCA velocity constraints as
state constraints in our MPC formulation.
1) State Constraints: At a time t = 0, ORCA constraints
can be computed for an agent considering the current posi-
tion and current velocity of all its neighboring agents and
obstacles. For subsequent timesteps {t +i | i = 1,2...N −1},
we compute ORCA planes by predicting the future position
and velocity of the agents and neighbours using their current
state information. Assume that we are to compute the ORCA
constraints for an agent A. The position and velocity of agent
A is obtained from the state trajectory predicted by the MPC.
This is given by
{ξpredicted,k | k = 1,2,...N}.
In contrast, for neighboring agents we propagate their current
position using a simple motion model given by
rt+1 = rt +vtt.
We assume velocity for the neighboring agents and obstacles
to remain constant over the prediction horizon. State con-
straints by ORCA now pertain to a particular time step in the
prediction horizon. The ORCA planes consider downwash
and uncertainty in the sensor reading. The modiﬁcations to
ORCA for downwash is presented below.
2) Downwash: In dense scenarios, multiple quadrotors
may have to maneuver in close proximity to each other.
Downwash causes a region of instability below the rotors
of a quadrotor and any other quadrotor entering this region
may lose control and face instability. To ensure safe ﬂights
in close proximity, we must account for downwash in our
collision avoidance method.
Since we do not make small angle assumptions regarding
the attitude angle, assuming a ﬁxed orientation in the form
of axis-aligned ellipsoids is not ideal. Hence, we rotate
the ellipsoidal bounding region of the agent according to
the quadrotor attitude when computing the VO. Two issues
require proper consideration in this approach.
1) When two quadrotors are in proximity, only the
quadrotor (and its orientation) at the higher altitude
inﬂuences the downwash region. The quadrotor at the
lower altitude, in spite of its orientation, may face
instability when it enters the downwash region of the
quadrotor above it.
2) ORCA requires Minkowski sum construction and clos-
est point computation for constructing the ORCA half-
planes. Modelling the quadrotors as oriented ellipsoids
increases the complexity of both the computation.
Since we are required to recompute the ORCA plane
over the prediction horizon as discussed in Section IV-
B.1, we need a fast method to perform this computa-
tion.
We solve the issue by modelling only one of the two
quadrotors as ellipsoids while constructing the VO for the
pair of agents. To maintain the symmetry of VOτ
A|B and
VOτ
B|A about the origin, the decision regarding which quadro-
tor is modelled as an ellipsoid must be common for any pair
of quadrotors.
When an agent constructs the VO based on its neighbors,
we choose to model the quadrotor at the higher altitude
(at the current timestep) as an ellipsoid, while the other is
modelled as a sphere. Also, the orientation of the agent at
the higher altitude is used to rotate the bounding ellipsoid for
the construction of the Minkowski sum. This results in the
Minkowski sum being computed between a oriented ellipsoid
and a sphere. Given two agent ’i’ and ’j’, assume agent
’j’ is at a higher altitude at the current timestep. Then the
Minkowski sum is given by
Oij = Oi,sphere ⊕Oj,ellipsoid,φ,θ.
In addition, since the choice of agent at a higher altitude
is unique for any pair of agents, this ensures that VOτ
A|B and
VOτ
B|A are symmetric about the origin.
C. Modeling Uncertainty
ORCA assumes perfect knowledge of the sizes, positions
and velocities of all the obstacles around them. This as-
sumption is idealistic and makes implementing ORCA on


## Page 6


Fig. 2: Top view of two quadrotors A and B ﬂying close to
each other is shown. From left to right, the uncertainty in
the position and velocity of B as sensed by A increases. To
account for the uncertainty, A increases its perceived bound-
ing ellipsoid of agent B and computes its new, dynamically
feasible velocities based on B’s increased size. Our method
makes A take a conservative trajectory (red) away from B,
rather than its preferred trajectory (green).
real quadrotors impractical. To account for a quadrotor’s
imperfect sensing, we use a Kalman ﬁlter to compute the
mean and covariance of the position and velocity of all
obstacles around it.
The agent’s process and observation model is assumed to be
as follows,
xk+1 = Axk +Buk +wk
yk = Cxk +vk
Here xk is the state and uk is the control input at time
step k. wk and vk are the process and measurement noise
respectively and are assumed to be Gaussian, zero-mean
white-noise. The state transition matrix A, matrix B and C
are same as in the linear ﬂat model we compute for the
quadrotor. The mean and the co-variance for the states are
computed through kalman predict and update cycle.
Eigenvalues of the covariance matrix represent the spread
of the data, or the level of uncertainty in the direction of the
eigenvectors. Therefore, we use the maximum eigenvalue of
an entity’s position covariance matrix to enlarge its bounding
volume from the perspective of the quadrotor that senses
it. If the sensed entity is another agent, we increase the
length of the axes of its bounding ellipsoid and, if the
entity is a dynamic obstacle, we increase the radius of its
bounding sphere. This is similar to the method used in [36].
The VO is constructed using this bounding sphere and is
later augmented by the velocity covariance matrix. Although
this formulation makes the collision avoidance conservative,
we observe that it works well even with tens of dynamic
obstacles. Fig. 2 shows a scenario with two agents and
the increase in the size of an agent’s bounding ellipsoid as
perceived by another agent. This is a simple approach to
account for uncertainty, which could be extended to more
sophisticated methods, as shown in [37] or [22].
V. RESULTS
In this section we highlight our implementation and the
experimental results and describe the beneﬁts of our method
over prior methods.
A. Experimental Setup
Our algorithm is implemented on an Intel Xeon w-2123
octacore processor (3.6 GHz) with 32 GB memory and
GeForce GTX 1080 GPU. We utilize the PX4 Software In
The Loop framework, ROS Kinetic, and Gazebo 7.14.0 for
our simulations. The RVO-3D library is utilized to compute
the ORCA collision avoidance constraints. The Optimal
Control Problem (OCP) is solved using IPOPT Library with a
prediction horizon of 10 steps and a timestep of 0.1 seconds.
We consider a sensing region of 6m and a time horizon
of 5 seconds for ORCA (including the one used in our
formulation), AVO, and LQR-obstacle. The δ parameter for
AVO is set as 2vmax/amax as suggested in [15].
B. Performance Evaluation
We compare the performance of our algorithm with
ORCA, AVO and LQR-Obstacles in terms of smoothness of
trajectories, variation in velocity during collision avoidance,
and proportion of collisions while maneuvering trajectories
with high-velocity. In addition, we show the separation
between agents to demonstrate the downwash performance.
1) Generated Trajectory: We compare the smoothness of
the trajectories followed by 6 agents while using our method,
ORCA, and AVO. The agents are initially in a circular for-
mation, exchanging their positions with diagonally opposite
agents. The maximum velocity for the agents in the above
scenario was limited to 4 m/s. Figure 3a, 3b, and 3c illustrate
the trajectories followed by the 6 agents using our method,
ORCA and AVO. We observe that our method produces
smoother trajectories than ORCA.
2) Variation in Velocity: To show our method results
in smoother trajectories than AVO, we plot the velocity
components (along X, Y, and Z axes) of an agent while
performing collision avoidance in the scenarios discussed
in the previous subsection. Figure 4 graphs the variation in
velocity of one agent while using our method, ORCA, and
AVO. It can be observed that the variation velocity is much
smoother for the agent using our method compared to ORCA
or AVO.
3) Performance
During
Agile
Maneuvers:
Table
II
summarizes the performance of the various algorithms while
following high velocity time-parameterized trajectories. The
trajectories provided are straight lines, but the quadrotors
accelerate to reach their highest velocity in the midpoint of
the line before decelerating. We deﬁne an episode as when
all 8 quadrotors exchange their positions with the agents
diagonally opposite them. We report the number of episodes
(out of 250 episodes) that resulted in one or more of the
agents colliding. We observe that our method performs
better when following such trajectories.


## Page 7


(a) Proposed Method
(b) ORCA
(c) AVO
Fig. 3: The trajectories generated using a) our proposed method b) ORCA and c) AVO, when 8 agents exchange their position
with diagonally adjacent agents. The colored circles represent the starting position of the agents. Each colored trajectory
represents a different agent. The quadrotors travel at a max velocity of 5m/s
(a) Proposed Method
(b) ORCA
(c) AVO
Fig. 4: Variation in velocity when agents exchange their positions to antipodal positions in circular scenarios when collision
avoidance is performed using a) proposed method, b) ORCA, and c) AVO. Our scenarios consist of 6 quadrotors with a
maximum velocity of 5m/s.
Collisions while tracking a reference trajectory
Average
Velocity
Episodes with Observed Collisions (out of 250 Episodes)
ORCA
AVO
DCAD (Our Method)
1 m/s
0
0
0
2 m/s
0
0
0
4 m/s
17
31
0
7 m/s
151
128
21
TABLE II: 7m Number of episodes in which one or more
quadrotor collided when the agents used ORCA, AVO,
LQR or our method for collision avoidance. The scenarios
consisted of 8 quadrotor in a circle exchanging their positions
with the antipodal agents. It can be observed that in high-
velocity trajectories, our method shows good performance.
In previous literature, ORCA and AVO are generally tested
in scenarios where only the goal position is provide, this is
in contrast to using a time parameterized trajectory as in
our previous result. Hence, we also tabulate the results when
only a goal position is provided in Table III. The scenarios
is same as earlier, the agents exchange positions with the
diagonally opposite neighbour.
Comparing with both cases, we can observe that our
method performs better in high velocity ﬂight in scenarios
with small sensing distance (6m in our case).
In addition, we observe that our collision avoidance per-
forms well in aggressive trajectories such as a lamniscate
(shown in ﬁgure 5).
(a) Top View
(b) Bird’s Eye View
Fig. 5: Two quadrotors (represented by red and blue) tracking
the same lamniscate trajectory in opposing directions (red
moving clockwise and blue moving anti-clockwise) at an
average speed of 4.2 m/s. We observe that quadrotors alter
their trajectories to avoid the collisions even while perform-
ing such aggressive maneuvers.


## Page 8


Collisions while moving to a goal position
Average
Velocity
Episodes with Observed Collisions (out of 250 Episodes)
ORCA
AVO
DCAD (Our Method)
1 m/s
0
0
0
2 m/s
0
0
0
4 m/s
0
21
0
7 m/s
67
106
21
TABLE III: Number of episodes in which one or more
quadrotor collided when the agents used ORCA, AVO,
LQR or our method for collision avoidance. The scenarios
consisted of 8 quadrotor in a circle exchanging their positions
with the antipodal agents. It can be observed that in high
velocity our method shows good performance.
Number of Agents
Trajectory Length (m)
Time to Goal (s)
ORCA
AVO
DCAD
ORCA
AVO
DCAD
2
40.62
40.75
41.08
15.71
15.71
15.71
4
40.77
40.96
41.42
15.71
15.71
15.70
6
40.84
41.74
41.53
15.72
15.71
15.71
8
41.55
41.94
42.34
15.70
15.72
15.71
10
41.96
42.17
42.97
15.70
15.71
15.70
TABLE IV: Comparison of mean path length and mean
time taken to reach goal when the agents use ORCA, AVO,
and DCAD. A circular scenario is considered when agents
exchange positions with their diagoannly opposite agents.
The circle is of diameter 40m and therefore the optimal path
length in an obstacle-free case would be 40m.
4) Optimality: In order to compare the optimality of
the generated trajectories we consider two metrics, namely,
length of trajectory generated and time to reach goal. We
consider a circular scenario as before and the tabulate the
average trajectory length and the mean time taken to reach
the goal. The agents move to their anti-podal positions which
are 40m away. Hence, in the absence of any obstacle the
optimal path would be a straight line path with a distance
of 40m to the goal. From table IV we can observe that the
trajectory length while performing collision avoidance using
DCAD is close to 40m as in the ideal obstacle-free case.
Similarly the path lengths are comparable to other methods
such as AVO, ORCA. Further, it can be noted that the time
to reach the goal is approximately the same.
5) Scalability Comparison: The Figure 6 illustrates the
computation time of our algorithm for one agent considering
1 to 50 obstacles in the environment. We observe that
considering only the closest 10 obstacles provides good
performance in most cases, an on an average this take less
than 6ms.
Figure 7 illustrates the average time taken by our algorithm
for computing control input for all agents in the scenario
presented in Fig. 3. The number of agents in the scenario is
varied from 5 to 50 agents. Each agent considers only the
nearest 10 agents as obstacles.
Table V below tabulates the average time taken by DCAD
and ORCA for computing control input. The number of
agents in the scenario is varied from 5 to 50 agents. Each
agent considers the nearest 10 agents as obstacles.
Fig. 6: The time (ms) required to compute a collision-free
trajectory for a single agent per timestep considering 1 to 50
nearest neighbors.
Fig. 7: The time (ms) required to compute a collision-free
trajectory for a single agent per timestep considering 1 to 50
nearest neighbors.
C. Computational Complexity
DCAD is a decentralized collision avoidance method,
hence each agent makes independent decisions to avoid col-
lision. Assuming that there are ‘N’ agents in the environment
and each agent considers ‘p’ agents in its sensing region as
its neighbors. The overall running time would be linear in the
number of total agents (i.e. N). This is because the maximum
number of linear constraints (ORCA velocity computation
constraints) for an agent is ﬁxed since we consider only ‘p’
agents in its sensing region as its neighbors.
The complexity is based on Eqn. 17 in the paper, which
describes the optimization problem. The number of linear
constraints due to agents dynamics, box constraints on veloc-
ity, acceleration, and jerk are ﬁxed for an agent. The number
of ORCA linear constraints for the agent depend on the
number of neighboring agents considered. Since we consider
only ‘p’ in the local environment as neighbors, the maximum
number of linear constraints for the optimization problem is
ﬁxed. Considering the worst case computation time to solve
this optimization problem to be ‘k’ milliseconds. The total
worst case computation time for all agents in the environment
would be Nk (in milliseconds) on a single core. That is a
linear function of ‘N’.


## Page 9


Number of Agents
Computation Time (ms)
ORCA
DCAD
1
0.009
5.1
5
0.023
29.8
10
0.097
66.6
15
0.141
113.3
20
0.213
175.1
25
0.325
242.5
30
0.392
269.9
35
0.445
341.9
40
0.511
427.9
TABLE V: Computation time
Since the agent perform the computation independently,
we can parallelize the computation on ‘m’ cores the worst
case total computation time would be kN/m.
D. Beneﬁts Over Prior Methods
In comparison with the centralized methods shown in [5]
and [24], our method proves to be superior in handling
dynamic scene changes and provides scalability to large
numbers of agent due to its decentralized and reactive nature.
In addition, our method is also computationally inexpensive
compared to NMPC methods such as [9], enabling more
computation power to be available to other applications like
perception and/or communication.
VI. CONCLUSION, LIMITATIONS, AND FUTURE WORK
In this paper, we present a decentralized collision avoid-
ance method for a quadrotor swarm. Our method uses
differential ﬂatness and feed-forward linearization to simplify
the quadrotor dynamics and uses a linear MPC to generate
smooth, collision-free, downwash-conscious local trajecto-
ries.
We observe that our method results in smoother trajecto-
ries and smoother velocity variations. Further, our method
performs considerably better than OCRA or AVO when
following high-velocity trajectories. We observe that our
method requires 5 ms for each agent to compute a control
input in the presence of 8 nearest obstacles.
In this paper, we include a conservative method that
accounts for sensor uncertainty by augmenting the bounding
volume of agents and VO based on the eigenvalue of the
state uncertainty. Our next step is to provide tighter bounds
on the sensor uncertainty to improve the performance with
noisy sensing. Further, we currently assume the position
and velocity data in the case of dynamic obstacles (e.g.,
birds) are available through some form of sensing. It would
be interesting and useful to develop robust methods with
integrated sensing, tracking and planning capabilities. In
addition, we plan on physically implementing our algorithm
in a quadrotor system to measure its performance.
REFERENCES
[1] P. Foehn, D. Falanga, N. Kuppuswamy, R. Tedrake, and D. Scara-
muzza, “Fast trajectory optimization for agile quadrotor maneuvers
with a cable-suspended payload.” in Robotics: Science and Systems,
2017, pp. 1–10.
[2] A. Kushleyev, D. Mellinger, C. Powers, and V. Kumar, “Towards a
swarm of agile micro quadrotors,” Autonomous Robots, vol. 35, no. 4,
pp. 287–300, 2013.
[3] F. Augugliaro, A. P. Schoellig, and R. D’Andrea, “Generation of
collision-free trajectories for a quadrocopter ﬂeet: A sequential convex
programming approach,” in 2012 IEEE/RSJ international conference
on Intelligent Robots and Systems.
IEEE, 2012, pp. 1917–1922.
[4] Y. Chen, M. Cutler, and J. P. How, “Decoupled multiagent path
planning via incremental sequential convex programming,” in 2015
IEEE International Conference on Robotics and Automation (ICRA).
IEEE, 2015, pp. 5954–5961.
[5] J. A. Preiss, W. H¨onig, N. Ayanian, and G. S. Sukhatme, “Downwash-
aware trajectory planning for large quadrotor teams,” in 2017
IEEE/RSJ International Conference on Intelligent Robots and Systems
(IROS).
IEEE, 2017, pp. 250–257.
[6] J. Van Den Berg, D. Wilkie, S. J. Guy, M. Niethammer, and
D. Manocha, “Lqg-obstacles: Feedback control with collision avoid-
ance for mobile robots with motion and sensing uncertainty,” in 2012
IEEE International Conference on Robotics and Automation.
IEEE,
2012, pp. 346–353.
[7] D. Bareiss and J. Van den Berg, “Reciprocal collision avoidance
for robots with linear dynamics using lqr-obstacles,” in 2013 IEEE
International Conference on Robotics and Automation.
IEEE, 2013,
pp. 3847–3853.
[8] H. Voos, “Nonlinear control of a quadrotor micro-uav using feedback-
linearization,” in 2009 IEEE International Conference on Mechatron-
ics.
IEEE, 2009, pp. 1–6.
[9] H. Zhu and J. Alonso-Mora, “Chance-constrained collision avoidance
for mavs in dynamic environments,” IEEE Robotics and Automation
Letters, vol. 4, no. 2, pp. 776–783, 2019.
[10] M. Greeff and A. P. Schoellig, “Flatness-based model predictive con-
trol for quadrotor trajectory tracking,” in 2018 IEEE/RSJ International
Conference on Intelligent Robots and Systems (IROS).
IEEE, 2018,
pp. 6740–6745.
[11] T. Engelhardt, T. Konrad, B. Sch¨afer, and D. Abel, “Flatness-based
control for a quadrotor camera helicopter using model predictive
control trajectory generation,” in 2016 24th Mediterranean Conference
on Control and Automation (MED).
IEEE, 2016, pp. 852–859.
[12] E. Ferrera, A. Alc´antara, J. Capit´an, A. Casta˜no, P. Marr´on, and
A. Ollero, “Decentralized 3d collision avoidance for multiple uavs
in outdoor environments,” Sensors, vol. 18, no. 12, p. 4101, 2018.
[13] J. Van den Berg, M. Lin, and D. Manocha, “Reciprocal velocity obsta-
cles for real-time multi-agent navigation,” in 2008 IEEE International
Conference on Robotics and Automation. IEEE, 2008, pp. 1928–1935.
[14] J. Van Den Berg, S. J. Guy, M. Lin, and D. Manocha, “Reciprocal
n-body collision avoidance,” in Robotics research.
Springer, 2011,
pp. 3–19.
[15] J. Van Den Berg, J. Snape, S. J. Guy, and D. Manocha, “Reciprocal
collision avoidance with acceleration-velocity obstacles,” in 2011
IEEE International Conference on Robotics and Automation.
IEEE,
2011, pp. 3475–3482.
[16] S. H. Arul, A. J. Sathyamoorthy, S. Patel, M. Otte, H. Xu, M. C.
Lin, and D. Manocha, “Lswarm: Efﬁcient collision avoidance for large
swarms with coverage constraints in complex urban scenes,” IEEE
Robotics and Automation Letters, vol. 4, no. 4, pp. 3940–3947, Oct
2019.
[17] D. Mellinger, N. Michael, and V. Kumar, “Trajectory generation
and control for precise aggressive maneuvers with quadrotors,” The
International Journal of Robotics Research, vol. 31, no. 5, pp. 664–
674, 2012.
[18] G. Hoffmann, S. Waslander, and C. Tomlin, “Quadrotor helicopter
trajectory tracking control,” in AIAA guidance, navigation and control
conference and exhibit, 2008, p. 7410.
[19] E.
Reyes-Valeria,
R.
Enriquez-Caldera,
S.
Camacho-Lara,
and
J. Guichard, “Lqr control for a quadrotor using unit quaternions: Mod-
eling and simulation,” in CONIELECOMP 2013, 23rd International
Conference on Electronics, Communications and Computing.
IEEE,
2013, pp. 172–178.
[20] M. Bangura and R. Mahony, “Real-time model predictive control for
quadrotors,” IFAC Proceedings Volumes, vol. 47, no. 3, pp. 11 773–
11 780, 2014.
[21] M. Kamel, M. Burri, and R. Siegwart, “Linear vs nonlinear mpc for
trajectory tracking applied to rotary wing micro aerial vehicles,” IFAC-
PapersOnLine, vol. 50, no. 1, pp. 3463–3469, 2017.


## Page 10


[22] M. Kamel, J. Alonso-Mora, R. Siegwart, and J. Nieto, “Robust
collision avoidance for multiple micro aerial vehicles using nonlinear
model predictive control,” in 2017 IEEE/RSJ International Conference
on Intelligent Robots and Systems (IROS).
IEEE, 2017, pp. 236–243.
[23] J. Ferrin, R. Leishman, R. Beard, and T. McLain, “Differential ﬂatness
based control of a rotorcraft for aggressive maneuvers,” in 2011
IEEE/RSJ International Conference on Intelligent Robots and Systems.
Ieee, 2011, pp. 2688–2693.
[24] M. Hamer, L. Widmer, and R. Dandrea, “Fast generation of collision-
free trajectories for robot swarms using gpu acceleration,” IEEE
Access, vol. 7, pp. 6679–6690, 2018.
[25] P. Fiorini and Z. Shiller, “Motion planning in dynamic environments
using velocity obstacles,” The International Journal of Robotics Re-
search, vol. 17, no. 7, pp. 760–772, 1998.
[26] M. Ruﬂi, J. Alonso-Mora, and R. Siegwart, “Reciprocal collision
avoidance with motion continuity constraints,” IEEE Transactions on
Robotics, vol. 29, no. 4, pp. 899–912, 2013.
[27] H. Cheng, Q. Zhu, Z. Liu, T. Xu, and L. Lin, “Decentralized navigation
of multiple agents based on orca and model predictive control,” in 2017
IEEE/RSJ International Conference on Intelligent Robots and Systems
(IROS).
IEEE, 2017, pp. 3446–3451.
[28] D. Morgan, S.-J. Chung, and F. Y. Hadaegh, “Decentralized model
predictive control of swarms of spacecraft using sequential convex
programming,” Advances in the Astronautical Sciences, no. 148, pp.
1–20, 2013.
[29] T. Baca, D. Hert, G. Loianno, M. Saska, and V. Kumar, “Model
predictive trajectory tracking and collision avoidance for reliable
outdoor deployment of unmanned aerial vehicles,” in 2018 IEEE/RSJ
International Conference on Intelligent Robots and Systems (IROS),
Oct 2018, pp. 6753–6760.
[30] Y. Xu, S. Lai, J. Li, D. Luo, and Y. You, “Concurrent optimal
trajectory planning for indoor quadrotor formation switching,” Journal
of Intelligent & Robotic Systems, vol. 94, no. 2, pp. 503–520, 2019.
[31] M. Fliess, J. L´evine, P. Martin, and P. Rouchon, “Flatness and defect of
non-linear systems: introductory theory and examples,” International
journal of control, vol. 61, no. 6, pp. 1327–1361, 1995.
[32] V. Hagenmeyer and E. Delaleau, “Exact feedforward linearization
based on differential ﬂatness,” International Journal of Control,
vol. 76, no. 6, pp. 537–556, 2003.
[33] D. Mellinger and V. Kumar, “Minimum snap trajectory generation
and control for quadrotors,” in 2011 IEEE International Conference
on Robotics and Automation.
IEEE, 2011, pp. 2520–2525.
[34] E. Tal and S. Karaman, “Accurate tracking of aggressive quadrotor
trajectories using incremental nonlinear dynamic inversion and differ-
ential ﬂatness,” in 2018 IEEE Conference on Decision and Control
(CDC).
IEEE, 2018, pp. 4282–4288.
[35] S. Liu, N. Atanasov, K. Mohta, and V. Kumar, “Search-based motion
planning for quadrotors using linear quadratic minimum time control,”
in 2017 IEEE/RSJ International Conference on Intelligent Robots and
Systems (IROS), Sep. 2017, pp. 2872–2879.
[36] J. Snape, J. Van Den Berg, S. J. Guy, and D. Manocha, “The hybrid
reciprocal velocity obstacle,” IEEE Transactions on Robotics, vol. 27,
no. 4, pp. 696–706, 2011.
[37] B. Gopalakrishnan, A. K. Singh, M. Kaushik, K. M. Krishna, and
D. Manocha, “Prvo: Probabilistic reciprocal velocity obstacle for multi
robot navigation under uncertainty,” in 2017 IEEE/RSJ International
Conference on Intelligent Robots and Systems (IROS).
IEEE, 2017,
pp. 1089–1096.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
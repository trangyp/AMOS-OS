---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1909.04655v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1909.04655v1_Energy_Conscious_Over-actuated_Multi-Agent_Payload_Transport_Robot__Simulations_

> Source: 1909.04655v1_Energy_Conscious_Over-actuated_Multi-Agent_Payload_Transport_Robot__Simulations_.pdf

> Pages: 7

---


## Page 1


Energy Conscious Over-actuated Multi-Agent Payload Transport Robot:
Simulations and Preliminary Physical Validation
Rahul Tallamraju1,2, Pulkit Verma1, Venkatesh Sripada3, Shrey Agrawal1 and Kamalakar Karlapalem1
Abstract— In this work, we consider a multi-wheeled payload
transport system. Each of the wheels can be selectively actuated.
When they are not actuated, wheels are free moving and do
not consume battery power. The payload transport system is
modeled as an actuated multi-agent system, with each wheel-
motor pair as an agent. Kinematic and dynamic models are
developed to ensure that the payload transport system moves
as desired. We design optimization formulations to decide on
the number of wheels to be active and which of the wheels
to be active so that the battery is conserved and the wear
on the motors is reduced. Our multi-level control framework
over the agents ensures that near-optimal number of agents is
active for the payload transport system to function. Through
simulation studies we show that our solution ensures energy
efﬁcient operation and increases the distance traveled by the
payload transport system, for the same battery power. We
have built the payload transport system and provide results
for preliminary experimental validation.
I. INTRODUCTION
The advent of electric vehicles and related emerging
technologies [1] are the result of understanding an urgent
need for clean and safe energy for human or cargo trans-
portation. Over-actuated systems have advantages over three
or four-wheeled mobile robot systems in applications like
traversing uneven terrain or transporting heavy loads
[2]–
[4]. However energy efﬁcient, wear conscious and failure
resilience properties of such multi-wheel systems have not
been extensively studied in literature. Our work aims to en-
hance efﬁciency and motivate the use of multi-agent control
for transportation systems. In this paper, we introduce an
over-actuated multi-agent payload transport robot (MAPTR)
which uses multiple low-power motors (refer Table I) to
achieve near energy efﬁcient motor operation. The presented
methodology actuates only a subset of all motors at near
constant velocities based on the motor energy efﬁciency
criterion. Our results provide evidence for such an energy
conscious operation. The primary challenges in achieving
energy conscious operation for an over-actuated robot can be
categorized into (1) system kinematic and dynamic modeling,
(2) controller design for energy efﬁcient actuator control, and
(3) real-time computation of control allocation.
We address these challenges as follows.
1. Modelling the robot kinematics and dynamics. Each
wheel of the robot rotates about its associated motor shaft
axis, which is its only degree of freedom. We therefore use
rahul.tallamraju@tuebingen.mpg.de,sripadav@oregonstate.edu,
pulkit.verma,shrey.agarwal@research.iiit.ac.in,kamal@iiit.ac.in
1Agents and Applied Robotics Group, IIIT Hyderabad, India.
2Max Planck Institute for Intelligent Systems, T¨ubingen, Germany.
3Oregon State University, Corvallis, United States.
skid-steer kinematic and dynamic models (Sec. III, Sec.IV)
to manoeuvre the system along any trajectory.
2. Energy and wear conscious operation. As the system
moves from rest and achieves near constant velocity,
the torque required to maintain a reference velocity can
be distributed among a subset of motors. Therefore, we
explore effects of deactivating motors while the robot is
in motion. Each wheel in the robot is associated with a
low-power, low-torque gearless motors (refer Table I) to
enable activation (actuation) and deactivation. By using
fewer motors at nearly constant velocity, the system ensures
that each motor (or agent) can function about its energy
efﬁcient operating point (Sec. IV-B), thus making the system
conscious of its energy usage. Additionally, since only a
subset of agents is active, we can distribute the effort of
transporting the load among different active-inactive agent
sets, thereby making the system wear-conscious (Sec. IV-C).
3. Multi-level decision-making controller. The system is
modeled as a multi-agent system where each wheel-motor
pair is considered as an agent. The agent has control over its
wheel velocity. A group of agents are controlled by a group
controller which allocates activation and deactivation signals
based on energy efﬁciency. Multiple group controllers
communicate
to
an on-board
central
controller
which
provides high-level trajectory information for the robot.
We validate the proposed robot model and its energy
conscious operation in simulation experiments. Further, we
verify the feasibility of using multiple low-power gearless
motors to transport payloads with a real over-actuated robot.
II. RELATED WORK
Advantages of distributed electric control with redundant
actuators for future aerial systems are discussed in
[5]–
[7].
To the best of our knowledge not much of work has
been carried out in identifying energy conscious and wear
minimizing control allocation for over-actuated autonomous
ground vehicles. Therefore, we review literature related to
different aspects of our work.
Energy efﬁcient control
allocation for electric vehicles was studied to track longi-
tudinal trajectories in [8], [9]. In that work, actuation and
re-generative breaking controls are allocated to the motors
to achieve energy efﬁcient operation using a piecewise linear
motor efﬁciency model. In [10] energy optimal acceleration-
deceleration proﬁles are identiﬁed for unmanned ground
vehicles through a novel actuator calibration and modelling
procedure. These proﬁles are generated ofﬂine for a given
arXiv:1909.04655v1  [cs.RO]  10 Sep 2019


## Page 2


System 
Dynamics
Wheel 
Encoders
Multi Agent System
Agent Task 
Allocation
Σ
Reference 
Velocities
-
+
errorL
Pseudo 
Velocities
errorR
Left Half
Right Half
Voltage Control
Number of  
Active Agents 
Multi-Level Control
Level-1
Level-2
Level-3
Agent Number
Time(s)
Agent Schedule
MIMO
Central 
Controller
Group 
Controllers
PID 
Loop
Nonlinear 
Optimization
Fig. 1: The three level control architecture with a snapshot
of the real multi-wheel system.
battery lifetime and trajectory of a four wheeled robot.
Fault tolerant control allocation for over-actuated systems
was explored in [11]. Control signals are dynamically al-
located to actuators through a control effectiveness matrix
and a numerical optimization formulation. The allocation
was however only applied to LTI systems. Wheel-motor
pairs are modeled as independent agents [12] to control a
wheeled robot along a circular trajectory using multi-agent
reinforcement learning. However not more than four driving
modules are used and also motor wear reduction is not
explored. In contrast to the aforementioned literature, our
work ensures that a collaborative effort by a large group
of motors achieves energy conscious operation. This makes
it conducive to model our system as a networked multi-
agent system [13]–[16]. Moreover, agents in the system are
selectively actuated in real-time based on system energy
efﬁciency, system trajectory and work done criteria. The two
key steps which enable such an agent actuation scheme are,
(1) system dynamics constrained, energy efﬁcient actuator
control-allocation, (2) control-allocation constrained, wear
minimizing actuation and deactivation agent schedules.
III. ROBOT SYSTEM MODEL
The MAPTR is modeled as a multi-agent system. Each
wheel-motor pair is modeled as an agent and a set of agents
forms a group. Agents in a group are associated with a
controller, limited battery power, wired connection to the
group controller and local sensing in the form of wheel
encoders. In this paper, agents are assigned to control groups,
left half group (L) and right half group (R)1, based on their
spatial positions with respect to the central controller. The
group controllers are further connected to a system level
central controller. It should be noted that in the MAPTR
the wheels move freely when the motor is powered off. The
free movement is hindered only by wheel-ground contact
1These control groups can be further divided into sub-groups in the case
of a cascaded multi-robot system, where each robot controls its own motors
friction and low viscous friction in the gearless motor shaft.
The full control architecture of the MAPTR is as shown
in Fig. 1. Control at various levels is summarized below.
Level-1 (agent decision) helps in maintaining a desired
wheel velocity (Sec. IV-A). Level-2 (group and system
decision) determines the required number of active agents for
near energy efﬁcient actuator operation (Sec. IV-B). Level-3
(group decision) identiﬁes an agent activation-deactivation
schedule to ensure uniform usage of all the agents. The
controller takes decisions based on the following inputs (a)
active agent velocity (level-1), (b) active agent efﬁciency
(level-2) and (c) number of active agents (level-3). For
concept demonstration, we consider (a) identical agents, (b)
agents belonging to the same group are coupled along their
motor shaft axis (thereby forming a multi-motor drive), (c)
ﬂat terrain, (d) no longitudinal wheel slip. Ideally, with small
in-hub motors, columns of actuated wheels can be stacked
on either side of the system. A sixteen wheel compact
conﬁguration with two columns of closely spaced wheels on
either side of the system center of mass (COM) is chosen
for concept demonstration. We derived kinematic, dynamic
and electrical models below.
A. Kinematic Model
The MAPTR uses skid-steering to manoeuvre, therefore,
lateral velocity of the wheels is non-zero. Figure 2a shows
spacing between agents for 16 wheel model. The system
has a linear velocity, v = [vx,vy,0]Tand angular velocity ω =
[0,0,ω]T. In Fig. 2a subscripts [L,R] represent the left and
right control groups and [A,B] represent the front and back
wheel sets, the wheel velocities are related as follows.
A design constraint δa << a
2is considered then vL = vL1 =
vL2 and vR = vR1 = vR2. {vL = vjx | j ∈1−8}, {vR = vjx | j ∈
9−16}, {vA1 = vjy | j ∈4,8,12,16}, {vA2 = vjy | j ∈3,7,11,15},
{vB1 = vjy | j ∈2,6,10,14}, {vB2 = vjy | j ∈1,5,9,13}.

vL
vR
vA1
vA2
vB1
vB2
T = Λ6×2

vx
ω
T
(1)
where,Λ6×2 =
 1
1
0
0
0
0
−a
2
a
2
3b
2
b
2
−b
2
−3b
2
T
System pose in generalized coordinates is q = [X,Y,θ,φL,φR]T,
where, [X,Y,θ] is the position and the orientation of the of
the system in the world frame and [φL,φR] are the angular
wheel orientations about their rotation axis. From equation
(1), the pseudo velocities ν =
vx
ωT = rΛ2×2
 ˙φL
˙φR
T,
where r is the wheel radius. The generalized and pseudo
velocities (˙q,ν) are related through the kinematic constraint
matrix S(q), as given in eqn. (2), which spans the null space
of the non-holonomic constraint matrix (vy = 0 or −˙Xsinθ +
˙Ycosθ = 0).
˙q
=
S(q)ν,
(2)
S(q)
=

cos(θ)
sin(θ)
0
1
1
0
0
1
−a
2
a
2
T
B. Dynamic Model
Referring to Fig. 2b, and solving the Lagrange-Euler
equation and, further eliminating Lagrange multipliers for


## Page 3


vL
Xw
Yw
Ow
vR
ICR
a
𝛅a
b
b
b
COM
v
Xr
⍵
v1
v2
v3
v4
v13
v14
v15
v16
vR2 = Agents {13,14,15,16} 
vL1 = Agents {1,2,3,4} 
v5
v6
v7
v8
vR1 = Agents {9,10,11,12} 
𝛅a
(a) Kinematic parameters
Xw
Yw
Ow
Mr
M
F1
Fl1
Fs1
F4
Fl4
Fs4
F16
Fl16
Fs16
Fl13
Fs13
Fry
Frx
A1
A2
B1
B2
F13
(b) Forces acting on system
Fig. 2: Kinematic and Dynamic Parameters of an illustration of the system
non-holonomic constraints, the system dynamic model is
given by,
ST (q)M(q)¨q+ST (q)R(˙q)
=
ST (q)B(q)τ
(3)
, where, M(q)= diag(m, m, Izz, NLIw, NRIw). Here, m is the mass
of the system, Izz,Iw are mass moment of inertia of the chassis
about the z-axis and the wheel about its rotation axis, ¨q is the
acceleration in generalized coordinates, R(˙q) = [Frx,Fry,Mr] is
a generalized frictional force vector [17] along longitudinal,
lateral and yaw axes. Fl j = µlmg 2
π tan−1(ksvyj)is the lateral
friction on wheel, Fsj = µsmg 2
π tan−1(ksvx j)is the longitudinal
friction on wheel. The viscous friction is modeled as part of
DC motor dynamics (Sec. III-C). µs,µl are the coefﬁcients
of rolling friction and lateral sliding friction for the wheels
with ground, g is the gravitational acceleration and ks >> 1
is a constant. B(q) is the input transformation matrix and
the total system torque applied by the motors given by,
τ =

∑i∈L τi,∑i∈R τi
T = [τL,τR]T. Final state-space dynamics
update equation is derived by differentiating equation (2)
(¨q = ˙S(q)ν +S(q)˙ν) and substituting it in equation (3).
˙ν =

˙vx
˙ω

=


τL+τR−r(Frx(˙q)cos(θ)+Fry(˙q)sin(θ))
r(m+16Iw)
−aτL+aτR−2rMr(˙q)
2r(I+ 8Iwa2
2
)


(4)
C. Integrating Motor and Battery Models
The MAPTR has a motor associated with each wheel and
a battery associated with each group controller, it is therefore
pivotal to model their characteristics.
1) Motor Model: Using the ﬁrst order DC motor model,
actuator torques in the system are given by,
τi
=
Na,i(KTIa,i −KTI0 −bdamp ˙φi), Ia,i = Vi −Ke ˙φi
Ω
i
∈
[L,R], τtotal = τL +τR, Na = Na,L +Na,R
(5)
where, VL,VR are left and right group motor supply voltages,
Ωis the armature resistance, Ke is the back emf constant, ˙φi
is the motor shaft angular velocity, KT is the motor torque
constant, I0 is the no-load current and bdamp is the viscous
friction coefﬁcient, NL,NR are total number of motors in the
left and right groups, and Na,L,Na,R are the total number
of active motors in the left and right groups. The motor
integrated dynamic model is obtained by substituting eqn.
(5) in (4) as shown below.
˙ν = [˙vx ˙ω] =
(6)


τtotal−(N−Na)bdamp−r(Frx(˙q)cos(θ)+Fry(˙q)sin(θ))
r(m+16Iw)
a(−τL+τR+bdamp((NL−N(a,L))−(NR−N(a,R))))−2rMr(˙q)
2r(I+ 8Iwa2
2
)


where, N = NL + NR and the additional damping terms
(Ni −Na,i)bdamp are added because of the viscous rotational
friction that exists due to the inactive motors in the system.
2) Battery Model: The multi-wheel system will be op-
erationally limited by its battery life. The battery voltage
deterioration with discharge is experimentally determined.
We ﬁnd the statistically best ﬁt to the data as a two term
exponential model VB = hewdB + yezdB, where, VB is the
supplied battery voltage, dB is the battery discharge and
h,w,y,z are coefﬁcients determined from the ﬁt. The results
(Sec. V) showcase the effects of reducing battery voltage
with and without efﬁciency optimization (Sec. IV-B).


## Page 4


IV. MULTI-LEVEL CONTROL SYSTEM
The multi-level control system is as shown in Fig.1.
The MAPTR ensures that its agents operate efﬁciently. It
does so by regulating the number of active agents, thereby
ensuring to get greater work done with fewer active agents.
Consequently, some agents in the system get a break from
activity. The duration of the break is based on (i) motor
models, (ii) battery consumption and (iii) system trajectory.
A. Level-1: Agent Velocity Control
Control at an agent level is achieved using proportional-
integral-derivative (PID) control [18]. The central controller
speciﬁes reference wheel velocities for the agents in the left
˙φref,L and right groups ˙φre f,R. At each discrete time instant
k, an agent 2 applies a control voltage Vi[k].
Vi[k] = KPei[k]+KIEi[k]+KD∆ei[k], i ∈[L,R] ,
(7)
where, ei[k] = ˙φi[k] −˙φre f,i, Ei[k] = Ei[k −1] + ei[k] and
∆ei[k] = ei[k]−ei[k −1]. KP,KI,KD are gains corresponding
to proportional, integral and derivative components of the
PID, Ei[k] is the cumulative error and ∆ei[k] is the change
in error. By tuning control gains, the PID achieves desired
performance irrespective of the underlying MAPTR model.
20
Voltage (V)
Motor Efficiency Variation 
10
0
20
Load Torque(N-mm)
100
40
Efficiency (%)
50
60
0
0
80
0
50
Motor Speed Variation
Load Torque
0
2000
100
Speed (rpm)
Voltage (V)
20
4000
6000
10
0
0
0.2
0.4
0.6
0.8
1
Fig. 3: Efﬁciency v/s Torque and Speed v/s Torque
B. Level-2: Energy Conscious Operation
Surface plots in Fig. 3 are characteristic curves of a typi-
cal permanant magnet DC motor (PMDC). The curves are
plotted using equation (5) for, a single 24 V, 15 W motor
with a stall torque of 130 Nmm and a no-load speed of
5930 rpm. Efﬁciency (η) of a motor in the nth agent is
calculated as
τn ˙φn
VnIa,n , where τn is the torque of nth agent,
˙φn is the wheel velocity, Vn is the applied voltage and Ia,n
is the current drawn. From Fig. 3, we note that maximum
motor efﬁciency lies around 10 −20% of stall torques at
different voltages. Furthermore, we observe a steep drop in
efﬁciency proﬁle from maximum efﬁciency point to near
zero efﬁciency at low load torques, due to relatively high
dissipative losses. Efﬁciency of each motor in the MAPTR
varies as a function of system load, number of active agents
and dissipative losses.
Voltage control (Sec. IV-A) applies a voltage Vi corre-
sponding to the error with respect to reference velocity. To
maximize active agent efﬁciency by regulating the number of
2 ˙φi[k], i ∈[L,R] velocities of an agent in a group are equal due to identical
agent assumption
active agents, we formulate a non-linear optimization prob-
lem. Each group controller independently executes the opti-
mization. The objective of the optimization is to maximize
motor efﬁciency. It is constrained by the number of agents the
group controller can actuate and the system dynamics. Since
the dynamics depends on the torque supplied by both the
agent groups, information on the number of active agents in
neighboring group is communicated by the central controller.
The optimization is deﬁned as follows.
Maximize
H
∑
h=0
τi[k +h] ˙φ[k +h]
Vi[k +h]Ia[k +h]
s.t. 0 ≤Na,i[k] ≤Ni,i ∈[L,R]
˙φi[k] = f(τa,L[k −1],τR[k −1],Na,L[k],Na,R[k]),
Ia,i[k] = Vi[k]−Ke ˙φi[k]
Ωi
,
τi[k] = KT(Ia,i[k]−I0)−bdamp ˙φi[k].
(8)
Here, Na,i is the number of active agents in the left or right
groups, f represents zero-order hold discretized dynamics of
the system (6). The objective of optimization is to maximize
agent efﬁciency (with identical agent assumption), by regu-
lating number of active agents Na,i. The cost is accumulated
for a horizon H because of instantaneous rise in current with
agent deactivation, causing instantaneous decrease in agent
efﬁciency. The advantage of agent deactivation can only be
observed after a few future time steps. Energy conscious
system operation ensures that the number of active agents
required for efﬁcient operation, converges to a constant value,
for a smooth trajectory. Since, the number of active agents
(Na,i) is less than the total number of agents in a group (Ni),
number of allowed agent failures for a given payload weight
is (Ni −Na,i),i ∈[L,R] agents. Therefore the system remains
operational despite some agent failures. The optimization
is feasible if the torque supplied by the total number of
agents is greater than the system load torque. Furthermore,
since the optimization is constrained by non-linear system
dynamics, the problem being solved is non-convex. We
resolve this by numerically evaluating the optimization using
sequential quadratic programming [19], where the given
problem is locally approximated as a quadratic program. The
approximation is reﬁned over multiple iterations to achieve
sub-optimal solutions. Therefore, for real-time control, the
solution to (8) is locally optimal albeit fast to compute.
C. Level-3: Online Task Allocation
The MAPTR can switch to different conﬁgurations of
active agents to uniformly share the work load. Agent task
allocation decisions are taken independently by the group
controllers. A conﬁguration of active agents is enforced to
be operational for a predeﬁned period of time TON (based on
motor thermal model). The distance traveled by agents might
vary for a non-smooth trajectory due to changes in number
of active agents. Therefore, we present a constrained linear
integer program to ensure that the distance traveled by each
agent is approximately equal. Optimization is evaluated every
TON(≈100) seconds or whenever the number of active agents


## Page 5


TABLE I: Mechanical and Electrical Parameters of the Multi-Agent System
Parameter
Value
Units
Number of Motors (N)
4-128
-
Chassis Weight
0.2
kg
Wheel Weight(mw)
0.05
kg
Payload Weight (m)
10-60
kg
a
0.2
m
b
0.08
m
Wheel radius(r)
0.035
m
Rolling Friction (µs)
0.01
-
Sliding Friction (µl)
0.1
-
Parameter of Motor
Type-I
Type-II
Units
Rated Voltage (V)
24
6
V
No-load Current (I0)
50
250
mA
No-Load Speed (φ0)
5930
5500
rpm
Stall Torque (τs)
130
17.6
mN m
Armature Resistance (R)
7.03
2.4
Ω
Viscous Friction Coeff. (b)
6×10−7
2.2×10−7
Nms
Torque Constant (KT )
38.2×10−3
7×10−3
Nm/A
Back-emf Constant (K e)
38.4×10−3
7×10−3
Vs/rad
Motor Weight
0.21
0.11
kg
0
50
100
time(s)
0
20
40
60
80
Efficiency
Efficiency of Agent
0
50
100
time(s)
0
1
2
3
4
Current (A)
Current in each Agent
0
50
100
time(s)
0
5
10
15
20
Number of Active Agents 
Active Agents with Time
0
50
100
time(s)
0
5
10
15
20
Velocity (m/s)
Velocity with Time
13.2 kg
23.2 kg
33.2 kg
43.2 kg
(a) Level-2 : Different gross weights
0
50
100
time(s)
0
20
40
60
80
Efficiency
Efficiency of Agent
0
50
100
time(s)
0
1
2
3
4
Current (A)
Current in each Agent
0
50
100
time(s)
0
5
10
15
20
Active Motors
Active Agents with Time
12 V
16 V
20 V
24 V
0
50
100
time(s)
0
5
10
15
20
Velocity (m/s)
Velocity with Time
(b) Level-2: Different input voltages
Fig. 4: The above plots showcase the results of energy conscious operation for a 16-agent system. (a) Notice that numerically
optimizing (8), for different payload weights, ensures that each agent (or motor) operates near its maximum efﬁciency
(η ≊80% from Fig. 3). (b) Notice that the agent achieves near maximum efﬁciency for different input voltages. The
resulting efﬁciencies approximately match the characteristic curve in Fig. 3.
(Na,i) changes. As conﬁguration changes are not rapid, the
level-1 and level-2 operations remain unaffected.
Minimize (D[k]−Dre f )Txi[k]
s.t.
Ni
∑
j=0
xi[k](j) = Na,i[k]
0 ≤xi[k](j) ≤1, xi[k](j) ∈Z, ∀j ∈[1,Ni]
where i ∈[L,R],
(9)
In the above equation D is the vector of distances traveled
by the agents. The values of D are normalized to lie in [0,1].
Dref is a vector whose elements have a value 1
Ni . The objec-
tive of the optimization evaluates the fairness of agent usage
based on the distance travelled by each agent. This cost is
evaluated as a weighted addition over a binary valued vector
xi[k], which represents activity (1) or inactivity (0) of agents
at instant k. The ﬁrst constraint imposes an equality over the
number of active motors (Na,i[k]), which was determined by
the level-3 controller. The second constraint imposes binary
values for the vector xi[k]
V. RESULTS
We showcase results obtained by (a) optimizing the straight
line system efﬁciency for both constant and varied voltages
TABLE II: Straight-Line power saving for a 16 agent system
(distance of 36km (approx.)). (EC-Energy Conscious Operation,
NO-No optimization)
Gross
Weight (kg)
Energy (kJ)
Power
Saving(%)
Active
Agents
Mileage (m/J)
NO
EC
NO
EC
13.2
92.33
63.17
31.58
3
0.4098
0.5347
18.2
111.69
87.46
21.70
5
0.3359
0.3970
23.2
131.05
108.94
16.87
6
0.2838
0.3171
28.2
150.41
132.81
11.7
8
0.2452
0.2633
33.2
169.77
156.58
7.77
10
0.2153
0.2249
38.2
189.13
180.35
4.64
12
0.1916
0.1962
for different payloads (Sec. IV-B), (b) computing optimal
online task allocation (Sec. IV-C), and, (c) testing the
feasibility of using a collection of low-power motors
in a real system. The various mechanical and electrical
parameters (Motors Types-’I’, ’II’) considered for the
multi-wheel system are as shown in Table I.
Energy Conscious Operation: To solve the numerical
optimization of equations (8) in real-time, we employ the se-
quential quadratic program (SQP) [20], with relaxed integer
constraints. Since SQP solutions in non-linear optimization
are sensitive to an initial solution guess, as a pre-processing
step, we simulate and approximate the required number of
active agents that achieve efﬁcient operation at different


## Page 6


0
50
100
150
200
250
300
350
Payload(kg)
0
10
20
30
40
50
60
Energy Advantage %
Percentage Energy Advantage
9 Agents
16 Agents
25 Agents
36 Agents
64 Agents
128 Agents
Fig. 5: Energy Advantage v/s Number of agents
loads. A horizon of 10 time steps results in a stable number
of active agents, with optimization running at 1Hz. The
optimization results for using Type-I motors with different
gross system weights (payload + chassis weight) is presented
in Fig. 4a. Through active agent regulation, the efﬁciency of
each agent converges to nearly the same maximum value, de-
spite increase in payload weight. Also, the number of active
agents required, increases with increase in payload weight.
Conversely, with increase in payload weight, the number of
agents available in case of operational failures, decreases.
If there are more than Ni −Na,i,i ∈[L,R] failed agents, the
system can no longer operate. The optimal number of active
agents can also vary with a change in applied voltage to
the motors. Effect of changing input voltage, for a 10 kg
payload is as shown in Fig. 4b. Table II summarizes results
of optimization for different gross system weights with the
sixteen wheel system, moving along a straight trajectory for
a duration of 30 min (36 km). A signiﬁcant power advantage
is observed at lower payloads weights, which reduces as the
payload weight nears the system rated weight.
Up-Scaling Number of Agents: Increasing the number of
agents increases the load carrying capacity of the system.
Moreover, we observed that by using our energy conscious
algorithm (8) the percentage of power saving improves, when
total number of agents in the system is increased, as shown in
Fig. 5. We also observe that the energy advantage curve has
reduced slope with agent scale up, which indicates that the
advantage is preserved for a larger range of payload weights.
Effect of Battery Discharge: Fig. 6 compares straight-line
energy conscious and non-energy conscious operation for
type-I motors with the effect of battery discharge. Coefﬁ-
cients for the two-term exponential model ﬁt (Sec. III-C) are
h = −1.851 × 10−14,w = 0.005345,y = 23.4,z = −1.018 ×
10−5. Battery discharge reduces the available supply. This
affects the number of active agents chosen by the energy con-
scious operation. In Fig. 6 the ﬁrst row of subplots compares
efﬁciency of agent v/s time. Notice that the efﬁciency of an
energy conscious agent is on average higher than a regular
agent. In the second row, observe that the number of active
agents are optimized in accordance with the payload weight.
Fig. 6: Comparison of battery discharge behaviors for non-
energy conscious and energy conscious operations. Notice
that the system operates for a longer duration with energy
conscious operation.
0
5
10
15
20
Time Steps
0
2
4
6
8
Agent Number
3-Agent Schedule
0
5
10
15
20
Time Steps
0
2
4
6
8
Agent Number
4-Agent Schedule
0
5
10
15
20
Time Steps
0
2
4
6
8
Agent Number
5-Agent Schedule
0
5
10
15
20
Time Steps
0
2
4
6
8
Agent Number
6-Agent Schedule
12.64
12.64
12.64
12.64
12.03
12.03
12.03
12.03
10
10
10.7
10.7
10.7
10
11.6
11.6
Distance (km)
Distance (km)
Fig. 7: Online: Conﬁguration transitions (1 step=100 s)
Towards the end of operation the number of active agents
increase for energy conscious operation. This is due to the
decrease in supply voltage with battery discharge. Finally,
in row three we observe that, in general, the system lasts
longer with energy conscious operation. For example, notice
the highlighted data points in Fig. 6. For a battery capacity
of 6395 mAh and a payload weight of 30 kg the system lasts
for (≈800s) longer.
Results of Task Allocation: From basic thermal analysis
we observe that the Type-I,II motors should not approxi-
mately exceed 600s of continuous operation at 1 Ampere
to avoid overheating. Each time step is TON = 100s. Fig. 7
showcases the results of performing online task allocation,
with energy conscious operation, for different number of
active agents. Additionally, simulating the three-level control
architecture with online task allocation for 30 minutes, we
plot the average idle time steps per agent as the number
of agents is scaled up for a known payload weight. Fig. 8
shows that the average idle time (steps) per agent increases
with agent scale up for a constant payload weight. This is
an advantage as the agents ensure efﬁcient system operation
by staying idle for longer periods of time, resulting in lesser
overall motor wear.
Validation of Physical System: We validate (a) the


## Page 7


0
20
40
60
80
100
120
140
Number of Agents
0
2
4
6
8
10
12
14
16
18
20
Average Idle Time Steps
Idle Time Variation with Agent Scale Up
4 kg
12 kg
20 kg
28 kg
Fig. 8: Average agent idle time v/s total number of agents,
determined using the proposed multi-level controller.
feasibility of using a collection of low-torque motors to
transport payloads and (b) de-activating some motors after
a few seconds of operation and ensure system motion. Fig.
9 showcases a constructed physical model in motion. The
physical model consists of 12 low torque and free moving
Type-III motors (Table I). We use an Arduino Mega Central
Controller in conjunction with a Raspberry Pi 3 micro-
computer running ROS [21]. The system costs under 400$,
weighs 3kg and can carry a payload weight of upto 10 kg
(Type-III motors).
Fig. 9: Experimental Platform in Motion
VI. CONCLUSION
In this work, we present a novel energy conscious over-
actuated robot which selectively actuates only a subset of all
its available wheels. Decisions on how many and which of
the wheels to activate are made in real-time using a hierarchi-
cal decision making architecture. Energy conscious operation
(Sec. IV-B) is achieved by leveraging non-linear optimiza-
tion. Furthermore, the system ensures that all its agents
are utilized uniformly to minimize agent wear (Sec. IV-
C). Our system can energy consciously track any trajectory,
using the developed kinematic, dynamic and electric models
(Sec. III).
Further work would involve introduction of
holonomic, energy conscious steering for our over-actuated
system. This would aid further development of modular and
decentralized multi-agent controllers. Our system and the
developed control methodologies could enable development
of future human transport systems.
REFERENCES
[1] J. Todd, J. Chen, and F. Clogston, “Creating the clean energy economy.
analysis of the electric vehicle industry,” International Economic
Development Council, Washington, DC, 2013.
[2] B. H. Wilcox, T. Litwin, J. Biesiadecki, J. Matthews, M. Heverly,
J. Morrison, J. Townsend, N. Ahmad, A. Sirota, and B. Cooper,
“Athlete: A cargo handling and manipulation robot for the moon,”
Journal of Field Robotics, vol. 24, no. 5, pp. 421–434, 2007.
[3] K. Iagnemma and S. Dubowsky, “Mobile robot rough-terrain control
(rtc) for planetary exploration,” in DETC, vol. 2000, 2000.
[4] S. H. Turlapati, M. Shah, S. P. Teja, A. Siravuru, S. V. Shah et al.,
“Stair climbing using a compliant modular robot,” in Intelligent Robots
and Systems (IROS).
IEEE, 2015, pp. 3332–3339.
[5] J. Holden and N. Goel, “Fast-forwarding to a future of on-demand
urban air transportation,” San Francisco, CA, 2016.
[6] M. D. Moore, “Personal air vehicles: a rural/regional and intra-urban
on-demand transportation system,” Journal of the American Institute
of Aeronautics and Astronautics (AIAA), vol. 2646, 2003.
[7] F. Gigante, “Volocopter e-volo takes ﬂight,” World Airnews, 2017.
[8] Y. Chen and J. Wang, “Fast and global optimal energy-efﬁcient control
allocation with applications to over-actuated electric ground vehicles,”
IEEE Transactions on Control Systems Technology, vol. 20, no. 5, pp.
1202–1211, 2012.
[9] J. Chen, Y Wang, “Design and experimental evaluations on energy
efﬁcient control allocation methods for over-actuated electric vehicles:
Longitudinal motion case,” IEEE/ASME Transactions on Mechatron-
ics, vol. 19, no. 2, pp. 538–548, 2014.
[10] P. Tokekar, N. Karnad, and V. Isler, “Energy-optimal velocity proﬁles
for car-like robots,” in ICRA.
IEEE, 2011, pp. 1457–1462.
[11] A. Khelassi, P. Weber, and D. Theilliol, “Reconﬁgurable control design
for over-actuated systems based on reliability indicators,” in 2010
Conference on Control and Fault-Tolerant Systems (SysTol).
IEEE,
2010, pp. 365–370.
[12] U. Dziomin, A. Kabysh, V. Golovko, and R. Stetter, “A multi-agent
reinforcement learning approach for the efﬁcient control of mobile
robot,” in IDAACS, vol. 2.
IEEE, 2013, pp. 867–873.
[13] J. Ota, “Multi-agent robot systems as distributed autonomous systems,”
Advanced engineering informatics, vol. 20, no. 1, pp. 59–70, 2006.
[14] L. E. Parker, “Multiple mobile robot systems,” in Springer Handbook
of Robotics.
Springer, 2008, pp. 921–941.
[15] Y. Chevaleyre, P. E. Dunne, U. Endriss, J. Lang, N. Maudet, and J. A.
Rodr´IGuez-Aguilar, “Multiagent resource allocation,” The Knowledge
Engineering Review, vol. 20, no. 2, pp. 143–149, 2005.
[16] E. H. Durfee and J. S. Rosenschein, “Distributed problem solving
and multi-agent systems: Comparisons and examples,” Ann Arbor, vol.
1001, no. 48109, p. 29, 1994.
[17] K. Kozłowski and D. Pazderski, “Modeling and control of a 4-
wheel skid-steering mobile robot,” International Journal of Applied
Mathematics and Computer Science, vol. 14, pp. 477–496, 2004.
[18] K. J. ˚Astr¨om and T. H¨agglund, PID controllers: theory, design, and
tuning.
Isa Research Triangle Park, NC, 1995, vol. 2.
[19] P. T. Boggs and J. W. Tolle, “Sequential quadratic programming,” Acta
numerica, vol. 4, pp. 1–51, 1995.
[20] J. Nocedal and S. J. Wright, Sequential quadratic programming.
Springer, 2006.
[21] M. Quigley, K. Conley, B. Gerkey, J. Faust, T. Foote, J. Leibs,
R. Wheeler, and A. Y. Ng, “Ros: an open-source robot operating
system,” in ICRA workshop on open source software, vol. 3, no. 3.2.
Kobe, 2009, p. 5.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1909_04655v1_energy_conscious_over_actuated_multi_agent_payload_transport_robot_simulations
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1909_04655V1_ENERGY_CONSCIOUS_OVER_ACTUATED_MULTI_AGENT_PAYLOAD_TRANSPORT_ROBOT_SIMULATIONS.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

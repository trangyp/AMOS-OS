---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1611.05443v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1611.05443v1_Bridging_the_Gap_between_Individuality_and_Joint_Improvisation_in_the_Mirror_Gam

> Source: 1611.05443v1_Bridging_the_Gap_between_Individuality_and_Joint_Improvisation_in_the_Mirror_Gam.pdf

> Pages: 25

---


## Page 1


arXiv:1611.05443v1  [q-bio.NC]  16 Nov 2016
Bridging the Gap between Individuality and Joint Improvisation
in the Mirror Game
Chao Zhai, Michael Z. Q. Chen, Francesco Alderisio, Alexei Yu. Uteshev and Mario di Bernardo ∗
Abstract
Extensive experiments in Human Movement Science suggest that solo motions are char-
acterized by unique features that deﬁne the individuality or motor signature of people. While
interacting with others, humans tend to spontaneously coordinate their movement and un-
consciously give rise to joint improvisation. However, it has yet to be shed light on the
relationship between individuality and joint improvisation. By means of an ad-hoc virtual
agent, in this work we uncover the internal mechanisms of the transition from solo to joint
improvised motion in the mirror game, a simple yet eﬀective paradigm for studying inter-
personal human coordination. According to the analysis of experimental data, normalized
segments of velocity in solo motion are regarded as individual motor signature, and the ex-
istence of velocity segments possessing a prescribed signature is theoretically guaranteed. In
this work, we ﬁrst develop a systematic approach based on velocity segments to generate
in-silico trajectories of a given human participant playing solo. Then we present an online
algorithm for the virtual player to produce joint improvised motion with another agent while
exhibiting some desired kinematic characteristics, and to account for movement coordination
and mutual adaptation during joint action tasks. Finally, we demonstrate that the proposed
approach succeeds in revealing the kinematic features transition from solo to joint improvised
motions, thus revealing the existence of a tight relationship between individuality and joint
improvisation.
∗Corresponding author: Michael Z. Q. Chen (mzqchen@outlook.com). Chao Zhai and Michael Z. Q. Chen
are with the Department of Mechanical Engineering, University of Hong Kong, Haking Wong Building, Pok Fu
Lam Road, Hong Kong. Alexei Yu. Uteshev is with the Faculty of Applied Mathematics, St. Petersburg State
University, Universitetskij pr.35, Petrodvorets, 198504, St. Petersburg, Russia. Francesco Alderisio and Mario
di Bernardo are with the Department of Engineering Mathematics, University of Bristol, Merchant Venturers’
Building, Woodland Road, Bristol, BS8 1UB, United Kingdom. Mario di Bernardo is also with the Department
of Electrical Engineering and Information Technology, University of Naples Federico II, 80125 Naples, Italy.
1


## Page 2


1
Introduction
People suﬀering from social deﬁciencies (i.e., schizophrenia or autism) ﬁnd it hard to engage
in social activities and interact with others, which inevitably brings sorrow to themselves and
their relatives [1, 2]. The theory of similarity in Social Psychology suggests that individuals
prefer to cooperate with others sharing similar morphological and behavioral features, and that
they tend to unconsciously coordinate their movements [3, 4, 5]. It has been shown that motor
processes caused by interpersonal coordination are closely related to mental connectedness, and
that motor coordination between two people contributes to social attachment [6, 7].
The mirror game provides a simple paradigm to study social interactions and the onset of
motor coordination among human beings, as it happens in improvisation theater, group dance
and parade marching [8, 9]. In order to enhance social interaction through motor coordination,
it would be desirable to create a virtual player (VP) or computer avatar capable of playing the
mirror game with a human subject (typically the patient) either by mimicking similar kinematic
characteristics or producing dissimilar ones [10]. Indeed, this allows to modulate the kinematic
similarity of the VP while maintaining a certain level of coordination with the human player
(HP) so that the s/he is unconsciously guided towards the direction of some desired movement
features.
Motor coordination between two or more eﬀectors in biological systems emerges as a result
of the integration of several body parts and functions. Such coordination occurs through two
types of control actions: feedback and feed-forward [11]. The motor system is able to correct the
deviation from the desired movement by means of feedback control, whilst feed-forward control
allows it to reconcile the interdependency of the involved eﬀectors and preplan the response to
the incoming sensory information, without taking into account how the system reacts to the
command signal [12]. Inspired by the above motor process of the human body, a computational
approach based on optimal control has been proposed in the literature for the VP to interact
with other participants and reconcile movement coordination with its own prescribed kinematic
features [13, 14].
The main challenge is to develop a mathematical model capable of driving the VP to joint-
improvise with a HP in the mirror game, while guaranteeing an assigned motor signature as
deﬁned in [15]. The ﬁrst step towards this goal is to design a computational architecture able to
generate in-silico trajectories reproducing the motor signature exhibited by a certain HP playing
solo. In so doing, we propose an approach based on velocity segments [16]. The second step
2


## Page 3


is to provide such architecture with an online algorithm allowing the virtual player to produce
joint improvised motions and interact with a HP or another VP. Much research eﬀort has been
spent on the design of control architectures for the virtual agent or robot [8, 13, 17, 18, 19,
20, 21, 22], but only pre-recorded time series of human players in solo trials have been used to
generate the joint motion of a customized VP [23], which limits its movement diversity due to the
ﬁnite number of available pre-recorded trajectories. The approach we propose here overcomes
this drawback by allowing the VP to autonomously exhibit any motor signature with speciﬁed
kinematic features (characterizing the solo motion of a given HP) during the interaction with
another agent.
The outline of this paper is given as follows. In Section 2 we introduce the experimental
paradigm of the mirror game, a quantitative marker of motor signatures, and their construction
method. In Section 3 we focus on the design of a computational architecture for the VP. Specif-
ically, we develop an algorithm capable of generating solo motions with prescribed kinematic
features, followed by an online algorithm allowing the VP to produce joint improvised motion
with another agent. Experimental validations is carried out in Section 4 to test the proposed
approach. Finally, in Section 5 we draw conclusions and discuss future directions.
2
Preliminaries
2.1
Mirror game
The mirror game is a simple yet eﬀective paradigm to investigate the onset of social motor
coordination between two players and describe their movement imitation at high temporal and
spatial resolution [8, 16, 24].
Figure 1 shows the experimental set-up at the University of
Montpellier, France.
The mirror game can be played in three diﬀerent experimental conditions [15]:
1. Solo Condition: This is an individual trial. Participants perform the game on their own
and try to create interesting motions.
2. Leader-Follower Condition: This is a collaborative round, whose purpose is for the partic-
ipants to create synchronized motions. One player leads the game, while the other tries to
follow the leader’s movement.
3. Joint-Improvisation Condition: Two players are required to imitate each other, create
synchronized and interesting motions and enjoy playing together, without any designation
3


## Page 4


Figure 1: Mirror game set-up at the University of Montpellier [14]. Two horizontal strings are
mounted perpendicularly at eye level and centrally between the two human participants. Two
small balls are mounted on the parallel strings, respectively. Human participants are instructed
to hold the handle beneath each ball and move it along the string back and forth. Cameras
are installed around the participants to collect experimental data and record their movement
trajectories. In solo trials, only one human participant is instructed to perform the motion. In
joint trials, two human participants are seated opposite each other and interact while moving
their respective ball.
of leader and follower roles.
Human movements in solo condition reﬂect their intrinsic dynamics, i.e., their individual mo-
tor signature [15]. On the other hand, participants reconcile their respective intrinsic dynamics
with the communal goal (movement synchronization) in leader-follower or joint-improvisation
condition. Here, we focus on the mathematical modeling of human coordination in solo and
joint improvisation (JI) condition, and shed light on their interconnection.
2.2
Motor signature
Data analysis of experimental recordings reveals the self-similarity characteristics of human
hand movements in solo trials, thus allowing to identify and distinguish human participants by
comparing the kinematic features of their solo motions [16, 25]. Indeed, motor signatures refer
to the unique, time-persistent kinematic characteristics of human movements in solo condition
[15, 25].
It has been shown that a possible candidate of motor signature is the probability
distribution function (PDF) of velocity time series in solo trials [25].
As a consequence, a
control architecture based on pre-recorded HP velocity proﬁles was developed for the VP to
4


## Page 5


0
time
velocity
0
skewness
kurtosis
Figure 2:
Motor signature of a human participant based on velocity segments in the mirror
game [16]. The blue curve denotes the velocity time series of a human participant in a solo trial.
The velocity segments in the red dashed boxes are normalized and then mapped as two blue
points in the skewness-kurtosis (S-K) plane. Solo motions of a human participant in the S-K
plane correspond then to a green ellipse, whose center is individuated by a black circle, which
contains all the mapped segments.
achieve real-time interaction in leader-follower and joint-improvisation conditions [13, 14, 21].
Notably, skewness and kurtosis of normalized velocity segments provide also a suitable com-
plement as marker of motor signature [16]. Speciﬁcally, segments represent periods and portions
of motion between two consecutive events of zero velocity, while normalized (or base) segments
are obtained by normalizing the original ones over the time interval [0, 1] and the corresponding
velocity integral. Figure 2 gives a graphical representation of velocity-segments-based individual
motor signatures, represented by the following ellipse:
(zs −µs)2
σ2s
+ (zk −µk)2
σ2
k
= 1
(1)
where zs and zk represent the horizontal and vertical coordinates in the skewness-kurtosis (S-K)
plane, with µs and µk (σs and σk) referring to mean values (standard deviations) of skewness
and kurtosis of the normalized velocity segments, respectively.
Our goal is to develop a computational architecture for the VP to produce human-like solo
movements and joint improvised trajectories with any desired values for skewness and kurtosis of
normalized velocity segments, such that the kinematic features of a certain HP can be reproduced
without making use of limited pre-recorded trajectories.
5


## Page 6


2.3
Base segment of velocity
It has been demonstrated that smooth point-to-point movements can be generated by minimizing
the time integral of the jerk magnitude squared [26]. This can be formulated as the following
minimization problem:
min
x J(x)
(2)
where
J(x) = 1
2
Z 1
0
d3x
dt3
2
dt
with x(t), t ∈[0, 1] denoting a desired position trajectory. In order to solve the optimization
problem (2), we ﬁrst compute
J(x + cδx) = 1
2
Z 1
0
d3x
dt3 + cd3δx
dt3
2
dt
(3)
where c is a constant and δx(t), t ∈[0, 1] is a smooth curve with the constraints
δx(0) = d2δx(0)
dt2
= d3δx(0)
dt3
= 0
(4)
and
δx(1) = d2δx(1)
dt2
= d3δx(1)
dt3
= 0
(5)
We then obtain the increment of J(x)
J(x + cδx) −J(x) = c
2
Z 1
0
d3δx
dt3

2d3x
dt3 + cd3δx
dt3

dt
(6)
that leads to
lim
c→0
J(x + cδx) −J(x)
c
=
Z 1
0
d3δx
dt3 · d3x
dt3 dt
(7)
From Equations (4) and (5) it follows that
Z 1
0
d3δx
dt3 · d3x
dt3 dt = −
Z 1
0
δx · d6x
dt6 dt
(8)
The optimal trajectory should then satisfy
lim
c→0
J(x + cδx) −J(x)
c
= −
Z 1
0
δx · d6x
dt6 dt = 0
(9)
Since δx can be an arbitrary function with initial condition (4) and terminal condition (5),
Equation (9) leads to a sixth-order diﬀerential equation
d6x
dt6 = 0
(10)
6


## Page 7


Thus, an ideal solution to Equation (10) is given by a ﬁfth-order polynomial in t
x(t) =
5
X
i=0
aiti,
t ∈[0, 1]
(11)
where ai, i ∈{0, 1, 2, 3, 4, 5} represent unknown coeﬃcients.
Therefore, the desired velocity
segments correspond to a fourth-order polynomial in t.
In order to create a base segment of velocity that combines smooth motion with the de-
sired kinematic features described by some individual motor signature, we deﬁne a probability
distribution function
f(t) :=
4
X
i=0
biti,
t ∈[0, 1]
(12)
where bi, i ∈{0, 1, 2, 3, 4} represent unknown coeﬃcients, and with the following boundary
conditions
f(0) = f(1) = 0
(13)
Mean value µ and variance σ2 of f(t) are deﬁned as follows:
µ :=
Z 1
0
τf(τ)dτ,
σ2 :=
Z 1
0
(τ −µ)2f(τ)dτ
(14)
Since the integral of f(t) over the time interval [0, 1] (i.e., the area of the base segment) must
be unitary, that is
Z 1
0
f(τ)dτ = 1
(15)
Equations (13), (14) and (15) yield b0 = 0 and the following matrix equation







1
1
1
1
1
2
1
3
1
4
1
5
1
3
1
4
1
5
1
6
1
4
1
5
1
6
1
7







b =







0
1
µ
µ2 + σ2







(16)
where b = (b1, b2, b3, b4)T . Likewise, the deﬁnitions of skewness s and kurtosis k
s := 1
σ3
Z 1
0
(τ −µ)3f(τ)dτ,
k := 1
σ4
Z 1
0
(τ −µ)4f(τ)dτ
(17)
are respectively equivalent to
bT







1
5 −3µ
4 + 2µ2
3
1
6 −3µ
5 + µ2
2
1
7 −µ
2 + 2µ2
5
1
8 −3µ
7 + µ2
3







= sσ3
(18)
7


## Page 8


and
bT







1
6 −4µ
5 + 3µ2
2 −µ3
1
7 −2µ
3 + 6µ2
5 −3µ3
4
1
8 −4µ
7 + µ2 −3µ3
5
1
9 −µ
2 + 6µ2
7 −µ3
2







= kσ4
(19)
By substituting b in Equations (18) and (19) with the solution to Equation (16), we obtain
a fourth-order polynomial system with two variables (µ and σ) and two parameters (s and k)
as follows



F(µ, σ, s) = 0
G(µ, σ, k) = 0
(20)
where F(µ, σ, s) = 0 and G(µ, σ, k) = 0 correspond to (18) and (19), respectively. The following
result holds for the solution to Equation (20).
Proposition 2.1. There exist real solutions µ and σ to the polynomial system (20) for any
given positive parameters s and k characterizing the motor signature of a human player.
Proof. See Appendix.
Remark 2.1. Proposition 2.1 guarantees the existence of velocity segments satisfying smooth
point-to-point movements with speciﬁed skewness and kurtosis. It is possible to prove Proposition
2.1 with the aid of discriminant [27] and resultant [28].
Analytical solutions to the polynomial system (20) are not always available, hence numerical
methods (i.e., polynomial continuation) have to be used to ﬁnd approximate solutions of mean
value µ and standard deviation σ for given skewness s and kurtosis k. By means of approximated
values of mean µ and standard deviation σ, it is possible to obtain the coeﬃcient vector b =
(b1, b2, b3, b4)T and the base segment of velocity f(t) = P4
i=0 biti via Equation (16).
For the sake of computational simplicity, in this work we assign all the four parameters µ,
σ, s and k characterizing the desired PDF P of a given HP, and then select three distinct time
instants (t1, t2, t3) for the ﬁtted segment of velocity h(t) := P4
i=0 citi to match such velocity
proﬁle
h(ti) = P(ti, µ, σ, s, k),
ti ∈(0, 1)
i ∈{1, 2, 3}
(21)
with
h(0) = h(1) = 0
(22)
8


## Page 9


0
0.5
1
0
1
2
3
4
5
S=0.5,K=1.5
0
0.5
1
0
1
2
3
4
5
S= 0.5,K=2
0
0.5
1
0
1
2
3
4
5
S=0.5,K=2.5
0
0.5
1
0
1
2
3
4
5
S=0.5,K=3
0
0.5
1
0
1
2
3
4
5
S=0,K=1.5
0
0.5
1
0
1
2
3
4
5
S=0,K=2
0
0.5
1
0
1
2
3
4
5
S=0,K=2.5
0
0.5
1
0
1
2
3
4
5
S=0,K=3
0
0.5
1
0
1
2
3
4
5
S=0.5,K=1.5
0
0.5
1
0
1
2
3
4
5
S=0.5,K=2
0
0.5
1
0
1
2
3
4
5
S=0.5,K=2.5
0
0.5
1
0
1
2
3
4
5
S=0.5,K=3
 
PDF
Segment
time[s]
time[s]
time[s]
time[s]
Figure 3: Construction of ﬁtted base segments of velocity by matching a desired velocity proﬁle.
The blue curve refers to the desired PDF P with speciﬁed skewness and kurtosis (mean value
µ = 0.5 and standard deviation σ = 0.25 are the same in all the sub-ﬁgures), while the red one
represents the ﬁtted base segment g. S and K stand for skewness and kurtosis, respectively. The
values of skewness for human participants generally range between −0.5 and 0.5, in comparison
with those of kurtosis varying from 1.5 to 3, respectively [16].
By combining Equations (21) and (22), we obtain the matrix equation







1
1
1
1
t1
t2
1
t3
1
t4
1
t2
t2
2
t3
2
t4
2
t3
t2
3
t3
3
t4
3







c =







0
P(t1, µ, σ, s, k)
P(t2, µ, σ, s, k)
P(t3, µ, σ, s, k)







(23)
with c = (c1, c2, c3, c4)T . The solution to Equation (23) gives the ﬁtted segment of velocity
h(t) = c1t + c2t2 + c3t3 + c4t4,
t ∈[0, 1]
(24)
which can ﬁnally be normalized to yield the ﬁtted base segment of velocity
g(t) =
h(t)
R 1
0 h(τ)dτ
(25)
Figure 3 presents twelve ﬁtted base segments of velocity obtained for diﬀerent values of
skewness and kurtosis.
9


## Page 10


Figure 4: Computational architecture of the VP in the mirror game. Variables p and ˙p represent
position and velocity of the human player, while x and ˙x those of the virtual player; g represents
the ﬁtted base segment and v the actual velocity segment of the VP, respectively.
3
Computational Architecture
The in-silico generation of velocity trajectories in solo motion with prescribed kinematic fea-
tures allows to develop a customized VP able to interact with a HP in JI condition, with the
former exhibiting the desired motor signature of a given human participant. In this section we
present the computational architecture of the VP to shed light on the relationship between the
mechanism underlying the generation of solo and joint improvised motions. Compared with
previous approaches [13, 14, 21], the one we propose here allows the virtual player to spon-
taneously reproduce the motor signature of a given HP, without making use of pre-recorded
time series of her/his motion in solo condition. This overcomes the drawback given by the need
for a large database of human solo trajectories, and endows the VP with a wider repertoire of
motor signatures, thus opening the possibility of exploring the eﬀects of continuously changing
its kinematic features during the interaction with another partner.
The proposed computational architecture (shown in Figure 4) consists of six function blocks
described in details as follows.
1. Velocity Estimation: The position trajectory of a HP detected by a camera is sent to
this block, where her/his corresponding velocity time series is estimated and split into a
series of velocity segments [16]. Then position and velocity errors between HP and VP are
computed.
10


## Page 11


2. Motor Planning: This block determines the direction, duration and displacement of the
velocity segments for the VP.
3. Motor Signature: This block reﬂects the kinematic features of a human player as it gen-
erates the ﬁtted base segment g. It allows to change the motor signature of the VP by
resetting the desired values of µ, σ, s and k.
4. Motor Coordination: This block allows for mutual adaptation, imitation and synchroniza-
tion between the virtual player and its partner in joint improvisation condition.
5. Movement Integration: The actual velocity segments v of the VP are generated by integrat-
ing the movement constraints on motor planning, motor signature and motor coordination.
6. Trajectory Generation: The movement trajectory of the VP is generated by chronologically
assembling the integrated velocity segments.
3.1
Generation of solo motions
While playing the mirror game in solo condition, the VP produces a prescribed motion without
taking into consideration that of any other participant. Thus, the generation of solo motions can
be regarded as a special case of joint motion where there is no motor coordination. Speciﬁcally,
the actual segments of velocity v are derived from the the ﬁtted base segments g after integrating
the displacement with the duration of time, and after assigning a motion direction.
Let ∆t denote the duration of the time interval for each velocity segment, which is a ran-
dom variable with probability distribution function λ(τ) that can be obtained by statistically
analyzing the solo recordings of a human participant. The probability of ∆t belonging to the
interval [t, ¯t] can be calculated as
P (t ≤∆t ≤¯t) =
Z ¯t
t
λ(τ)dτ
(26)
According to experimental data, the average time interval for velocity segments is equal to 0.8s,
with a standard deviation of 0.7s [16]. In addition, let ∆l represent the segment displacement
(i.e., position mismatch between the starting point and terminal point of each segment), which
is a random variable with probability distribution function ξ(s). Likewise, the probability of ∆l
belonging to the interval [l, ¯l] is given by
P
 l ≤∆l ≤¯l

=
Z ¯l
l
ξ(s)ds
(27)
11


## Page 12


0
1
2
0
2
4
6
∆t=0.5 ∆l=0.5
0
1
2
0
2
4
6
∆t=0.5 ∆l=1
0
1
2
0
2
4
6
∆t=0.5 ∆l=2
0
1
2
0
2
4
6
∆t=1 ∆l=0.5
0
1
2
0
2
4
6
∆t=1 ∆l=1
0
1
2
0
2
4
6
∆t=1 ∆l=2
0
1
2
0
2
4
6
∆t=2 ∆l=0.5
0
1
2
0
2
4
6
∆t=2 ∆l=1
0
1
2
0
2
4
6
∆t=2 ∆l=2
time[s]
time[s]
time[s]
Figure 5:
Variants of a ﬁtted base segment of velocity with respect to time duration ∆t and
displacement ∆l. The red curve represents g, while the blue ones represent its variants obtnained
for diﬀerent values of ∆t and ∆l as described in Equation (28).
Regardless of the motion direction, the variant of a ﬁtted base segment can be calculated as
∆l
∆t · g
 t
∆t

(28)
where g is deﬁned in Equation (25). Figure 5 shows a ﬁtted base segment of velocity and possible
eight variants for it with respect to time duration ∆t and displacement ∆l.
Since HPs tend to move around the middle part of the string in solo trials [15], the movement
direction of the VP is determined by
⃗D =







sign(x −pb),
|x −pa| > |x −pb|;
sign(x −pa),
|x −pa| < |x −pb|;
either,
|x −pa| = |x −pb|,
(29)
where x denotes the position of the VP, and pa < pb represent position bounds. An actual
velocity segment v is then constructed as follows
v(t) = ⃗D · ∆l
∆t · g
 t
∆t

= ⃗D ·
∆l · h( t
∆t)
∆t ·
R 1
0 h(τ)dτ
t ∈[0, ∆t]
(30)
12


## Page 13


Table 1: Solo Motion Algorithm (SMA).
1: Set skewness s, kurtosis k and running time Ts
2: Generate a ﬁtted base segment g(t) with (21), (22), (23), (24) and (25)
3: while (time < Ts)
4:
Determine the segment duration ∆t with (26)
5:
Determine the segment displacement ∆l with (27)
6:
Choose the movement direction ⃗D with (29)
7:
Generate an actual velocity segment v(t) with (30)
8:
Output the position trajectory x(t) with (31)
9: end while
Solo motions are generated by consecutively joining the actual velocity segments together.
Finally, the position trajectory of the VP is produced as follows
x(t) = x0 +
Z t
0
v(τ)dτ
t ∈[0, ∆t]
(31)
where x0 denotes the initial position of the generated segment. Table 1 summarizes the solo
motion algorithm (SMA) employed for the VP to produce human-like solo movements with
prescribed kinematic features.
3.2
Generation of joint improvised motions
While playing the mirror game in JI condition, the VP interacts with its partner while exhibit-
ing some prescribed kinematic features (motor signature). Based on the position and velocity
mismatch between the two players, the proposed computational architecture allows the virtual
player to imitate, adapt to and synchronize with the movement of its partner, thereby achieving
joint improvisation [14].
Similarly to SMA, the segment duration and displacement are determined by Equations (26)
and (27), respectively. As the two participants attempt to achieve movement synchronization,
the movement direction of the VP is given by
⃗D = sign(p −x)
(32)
where x denotes the position of the virtual player and p refers to that of the other agent. When
p = x, the VP is provided with a random direction.
13


## Page 14


The motor coordination block enables the VP to imitate and adapt to the movement of its
partner in order to synchronize their joint movements, while the two participants consciously
adjust their way of moving (i.e., the proﬁle of their velocity segments during the game). It has
been suggested that an optimal feedback control driving the VP is equivalent to a PD control
when the optimization interval is small enough, and that the nonlinear HKB equation originally
introduced in [29] is not signiﬁcantly better than a double integrator as end eﬀector model of
the VP in the mirror game [30].
For the sake of simplicity, in this work we employ a double integrator with PD control to
describe the motion of the VP and design the online algorithm as follows
¨x = cs(v −˙x) + cv( ˙p −˙x) + cp(p −x) + κ(x, ǫ)
(33)
where v is the actual velocity segment generated by Equation (30), x and ˙x represent position
and velocity of the VP, p and ˙p those of its partner, with cs, cv, cp and k being tunable positive
parameters. The ﬁrst three terms on the right-hand side of Equation (33) account for preferred
movement, mutual imitation and movement synchronization, respectively [14], whereas κ(x, ǫ)
is used to constrain the movement of the VP within the admissible range of motion:
κ(x, ǫ) =







cr|x −pb|,
x −pa ≤ǫ
−cr|x −pa|,
pb −x ≤ǫ
0,
otherwise
with cr and ǫ being tunable positive parameters. When the distance between the VP and its
closer bound is lower than ǫ, the term κ(x, ǫ) drives the VP with strength cr towards the middle
point of the position range.
By solving equation (33), the position trajectory of the VP is given by
x(t) = x0 +
Z t
0
Z τ
0
¨x(s)ds dτ,
t ≥0
(34)
where x0 refers to the initial position of the VP. Table 2 summarizes the joint improvisation
algorithm (JIA) employed for the VP to perform JI with another agent in the mirror game.
4
Experimental Validation
In order to test and validate the proposed computational architecture, in this section we compare
solo and joint improvised motions of human players with those generated by their respective
customized virtual agents. The numerical algorithms are implemented in Matlab R2010a.
14


## Page 15


Table 2: Joint Improvisation Algorithm (JIA).
1: Set skewness s, kurtosis k and running time Ts
2: Generate a ﬁtted base segment g(t) with (21), (22), (23), (24) and (25)
3: while (time < Ts)
4:
Determine the segment duration ∆t with (26)
5:
Determine the segment displacement ∆l with (27)
6:
Choose the movement direction ⃗D with (32)
7:
Generate an actual velocity segment v(t) with (30)
8:
Evaluate the acceleration ¨x(t) with (33)
9:
Output the position trajectory x(t) with (34)
10: end while
4.1
Solo motions
Figures 6(a) and 6(b) show position and velocity time series of a HP performing a 60s solo trial.
The HP moves the ball along the string within the normalized range [−1, 1].
The sampling
frequency of the camera is 100 Hz. According to data analysis of the velocity segments shown
in Fig. 6(b), the averaged mean value ¯µ, standard deviation ¯σ, skewness ¯s and kurtosis ¯k are
0.50, 0.23, −0.08 and 2.11, respectively. We then choose three time points t1 = ¯µ −¯σ, t2 = ¯µ
and t3 = ¯µ + ¯σ to construct the base segment of velocity. In particular, the Matlab function
“pearspdf” is employed to compute the values of the desired PDF P(t, ¯µ, ¯σ, ¯s, ¯k) at the selected
time points.
The probability distributions of ∆l and ∆t of the velocity segments in Fig. 6(b) are described
by cumulative distribution functions (CDF) shown in Figs. 6(e) and 6(f), respectively.
Figures 6(c) and 6(d) show position and velocity time series of a VP fed with the same
motor signature as that in Fig. 6(b) and driven by the SMA described in Table 1. The velocity
segments generated by the SMA resemble those of the HP in terms of proﬁle, yet are slightly
smoother. A visible diﬀerence is that the HP sometimes stays still during the game, whilst the
VP always keeps moving.
Figure 6(g) shows skewness and kurtosis of normalized velocity segments for both the HP
and her/his customized VP in the S-K plane. It is possible to appreciate that most velocity
segments of the VP are mapped into the ellipse representing the kinematic features of the HP,
15


## Page 16


0
0.5
1
1.5
2
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
∆l
0
0.5
1
1.5
2
CDF
1
0.5
0
0.5
1
Time
0
10
20
30
40
50
60
4
2
0
2
4
1
	0.5
0
0.5
1
Time
Position
0
10
20
30
40
50
60

2
1
0
1
2
Velocity
a
b
e
f
c
d
position
velocity
time [s]
time [s]
∆t
CDF
1

0.8
0.6
0.4
0.2
0
0.2
0.4
0.6
0.8
1
1
1.2
1.4
1.6
1.8
2
2.2
2.4
2.6
2.8
3
HP
VP
skewness
kurtosis
g
Figure 6:
Experimental validation – solo motions. Position (a) and velocity (b) time series of
the HP. Position (c) and velocity (d) time series of the VP. CDFs of ∆l (e) and ∆t (f) for the
HP. (g) Visualization of solo motion for the HP and her/his customized VP in the S-K plane:
blue dots correspond to velocity segments of the HP, whereas red ones refer to those of the VP.
The two corresponding ellipses are evaluated by means of Equation (1).
thus conﬁrming hat the VP succeeds in reproducing the motor signature of the speciﬁed HP.
Moreover, the VP segments are clustered together, whereas those of the HP are scattered in the
S-K plane, thus implying that solo motions of human players are more ﬂexible and diverse than
those of their customized computer avatar.
16


## Page 17


4.2
Joint improvised motions
Next, we present numerical validation of the JIA described in Table 2 for both HP-VP and
VP-VP dyads in a joint improvisation condition.
4.2.1
HP-VP dyad
The experimental set-up allowing a HP to perform joint improvisation with a VP is shown in
Fig.7. The parameter setting for the VP is given as follows: ¯µ = 0.51, ¯σ = 0.23, ¯s = −0.09,
¯k = 2.14, cs = 2, cv = 5, cp = 3, cr = 5 and ǫ = 0.1.
HP
mouse
laptop
Figure 7: Experimental set-up of HP-VP interaction in the mirror game. The HP is required
to sit in front of a laptop, which implements the JIA in Matlab. The blue circle represents the
position of the HP, which is controlled by means of a mouse, while the red circle represents that
of the VP, which is generated by the JIA.
Figures 8(a) and 8(b) show position and velocity time series of HP and VP, respectively.
Some synchronized segments can be observed in the position trajectories, which implies the
occurrence of joint improvisation between HP and VP.
The two ellipses featuring the movement patterns of the two interacting agents are shown
in Fig. 8(c). It is possible to appreciate that they are largely overlapping in the S-K plane,
implying that the two players exhibit similar kinematic features while interacting in the mirror
game.
4.2.2
VP-VP dyad
In order to validate the capability of the proposed computational architecture to reproduce the
kinematic characteristics observed when two human players (HP1 and HP2) perform the mirror
game in a joint improvisation condition, we numerically simulate a VP-VP trial. The evaluation
method is the same as that proposed in [14]. Speciﬁcally, two virtual players (VP1 and VP2)
17


## Page 18


a
b
c
position
velocity
time [s]
skewness
kurtosis
−2
−1.5
−1
−0.5
0
0.5
1
1.5
2
1
1.2
1.4
1.6
1.8
2
2.2
2.4
2.6
2.8
VP
HP
−1
−0.5
0
0.5
1
VP
HP
0
10
20
30
40
50
60
−2
−1
0
1
2
Figure 8: Experimental validation – JI trial between HP (blue) and VP (red). Position (a) and
velocity (b) time series of HP and VP. (c) Visualization of the JI motion between HP and VP
in the S-K plane.
are enabled to play the mirror game in a JI condition, with VP1 (VP2) being fed with the motor
signatures of HP1 (HP2), respectively (Fig. 9).
Figure 9: Schematic diagram of VP-VP interaction in the mirror game.
The two virtual players are driven by the JIA with the following parameters setting: ¯µ1 =
0.51, ¯σ1 = 0.22, ¯s1 = −0.18 and ¯k1 = 2.13 for VP1, ¯µ2 = 0.53, ¯σ2 = 0.25, ¯s2 = −0.18 and
¯k2 = 1.87 for VP2, and cs = 1.5, cv = 3.6, cp = 4.9, cr = 5 and ǫ = 0.1 for both VPs.
Figures 10(a) and 10(b) show position and velocity time series of the two human players, while
Figures 10(c) and 10(d) those of the two customized virtual agents, respectively. VP1 and VP2
succeed in reproducing the joint improvised movement (synchronized segments) as occurred in
the HP1-HP2 interaction.
Figure 10(e) describes the transition of motor signatures from solo to JI motion. The kine-
18


## Page 19


a
b
c
d
position
velocity
time [s]
time [s]
0
10
20
30
40
50
60
1
0.5
0
0.5
1
VP1
VP2
0
10
20
30
40
50
60
1
0.5
0
0.5
1
0
10
20
30
40
50
60
1
0.5
0
0.5
1
HP1
HP2
0
10
20
30
40
50
60
1
0.5
0
0.5
1
e
skewness
kurtosis
2
1.5
1
0.5
0
0.5
1
1.5
2
1.5
2
2.5
3
VP2
HP2
VP1
HP1
S1
S2
Figure 10: Experimental validation – JI trial in a human (HP1 and HP2) and in a virtual (VP1
and VP2) dyad. Position (a) and velocity (b) time series of the human dyad (HP1 in red and
HP2 in blue). Position (c) and velocity (d) time series of the virtual dyad (VP1 in red and VP2
in blue). (e) Visualization of solo and JI motions for the human pair and the customized virtual
pair in the skewness-kurtosis plane. VP segments are mapped into dashed-line ellipses (VP1
in red and VP2 in blue), HP segments into solid-line ellipses (HP1 in red and HP2 in blue),
and their corresponding kinematic signatures in solo motion (S1 and S2) into green solid-line
ellipses.
matic features of the human players in solo condition are separate, while those in JI condition
converge towards each other and are more variable. Notably, similar remarks can be made for
the kinematic features exhibited by the virtual players, thus indicating the desirable matching
performance of the VPs driven by the proposed computational architecture.
19


## Page 20


5
Conclusions
We developed a systematic approach to account for the generation of human solo motions, joint
improvised motions and the transition of their kinematic characteristics in the mirror game.
In so doing, a computational architecture was designed to describe the mechanisms underlying
solo and joint improvised movements, which provides a new insight into the shift of kinematic
patterns from individuality to joint improvisation.
We observed how, despite being characterized by diﬀerent motor signatures in solo motion,
players tend to imitate their respective kinematic features when interacting together, and ex-
hibit a wider repertoire of movements. Such results were successfully captured by the proposed
computational architecture, thus opening the possibility of testing in-silico interactions between
diﬀerent individuals in a number of diﬀerent conﬁgurations. Theoretical analysis was also pre-
sented to guarantee the existence of base segments of velocity characterizing any individual
motor signature.
Future work may include the consideration of motor learning in joint actions and the gener-
alization of this approach to other experimental paradigms for investigating socio-motor coor-
dination, both in dyads [31] and in larger ensembles [32, 33, 34, 35].
Acknowledgments
The authors wish to thank Prof. Krasimira Tsaneva-Atanasova and Dr. Piotr S lowi´nski at the
University of Exeter, UK for the insightful discussions and thank Prof. Benoit Bardy, Prof.
Ludovic Marin and Dr. Robin Salesse at the University of Montpellier, France for collecting
the experimental data that is used to validate the approach presented in this paper. This work
is supported by National Nature Science Foundation of China under Grant 61374053, by the
Innovation and Technology Commission under Grant No. UIM/268, and by the Research Grants
Council, Hong Kong, through the General Research Fund under Grant No. 17205414.
Appendix
In what follows we present the details on the proof of Proposition 2.1.
Proof. F(µ, σ, s) and G(µ, σ, k) in Equation (20) can be simpliﬁed as follows:
F(µ, σ, s) = −µ3 −3µσ2 −sσ3 + 3
2µ2 + 3
2σ2 −9
14µ + 1
14
(35)
20


## Page 21


and
G(µ, σ, k) = 3µ4 + 6µ2σ2 −kσ4 −6µ3 −6µσ2 + 89
21µ2 + 5
3σ2 −26
21µ + 5
42
(36)
which can be rewritten as
F1(µ, σ, s) := F(µ, σ, s)
σ3
= −s +

3
28σ2 −3
 µ −1/2
σ
−
µ −1/2
σ
3
(37)
and
G1(µ, σ, s) := G(µ, σ, k)
σ4
= −k+ 1
6σ2 −
1
336σ4 +

6 −
11
42σ2
 µ −1/2
σ
2
+3
µ −1/2
σ
4
. (38)
From these representations, it is evident that if the system has a solution (µ, σ) ∈C2 then
it also has a solution (1 −µ, −σ). Furthermore, with the aid of substitution
M = µ −1/2
σ
, η = 1
σ2
(39)
the expressions for F1(µ, σ, s) and G1(µ, σ, k) can be further simpliﬁed as
F1(M, η, s) = −s +
 3
28η −3

M −M3 ,
(40)
and
G1(M, η, k) = −k + 1
6η −
1
336η2 +

6 −11
42η

M2 + 3 M4,
(41)
respectively. By solving equation F1(M, η, s) = 0 with respect to η, we obtain
η = 28
3

M2 + 3 + s
M

(42)
Substitution of Equation (42) into G1(M, η, k) = 0 yields
G2(M, s, k) = 0
(43)
with
G2(M, s, k) = 8 M6 −36 M4 −80 sM3 + (63 −27 k)M2 −7 s2 .
(44)
According to data analysis of human movements in the mirror game, skewness s and kurtosis
k belong to the intervals (−0.5, 0.5) and (1.5, 3), respectively [16]. For any selection of values
s ∈(0, 0.5) and k ∈(1.5, 3), Equation (43) has a positive zero M = M0 in the interval (0, 2
√
3)
due to the conditions
G2(0, s, k) < 0,
(45)
and
G2(2
√
3, s, k) = 9396 −1920
√
3s −324 k −7 s2
21


## Page 22


= (9065 −1920
√
3s) + 324(1 −k) + 7(1 −s2) > 0 .
(46)
Therefore, from Equation (42) it is clear that also η is positive, hence the second equation
from (39) can be resolved in real numbers with respect to σ. The corresponding value for µ can
be then found in the ﬁrst equation from (39), which implies that F(µ, σ, s) = 0 and G(µ, σ, k) = 0
have real roots µ and σ.
References
[1] Z. Boraston, S. J. Blakemore, R. Chilvers, D. Skuse, Impaired sadness recognition is linked
to social interaction deﬁcit in autism, Neuropsychologia, 45(7), 1501-1510, 2007.
[2] S. M. Couture, D. L. Penn, D. L. Roberts, The functional signiﬁcance of social cognition
in schizophrenia: a review. Schizophrenia bulletin, 32(1), S44-S63, 2006.
[3] V. S. Folkes, Forming relationships and the matching hypothesis, Personality and Social
Psychology Bulletin, 8(4), 631-636, 1982.
[4] R. C. Schmidt, P. A. Fitzpatrick, Understanding the motor dynamics of interpersonal
interactions. Proceedings of IEEE International Conference on Systems, Man, and Cyber-
netics (SMC), pp. 760-764, 2014.
[5] A. E. Walton, M. J. Richardson, P. Langland-Hassan, A. Chemero, Improvisation and the
self-organization of multiple musical bodies, Frontiers in psychology, 6(313), 2015.
[6] S. S. Wiltermuth, C. Heath, Synchrony and cooperation, Psychological Science, 20(1), 1-5,
2009.
[7] S. Raﬀard, R. N. Salesse, L. Marin, J. Del-Monte, R. C. Schmidt, M. Varlet, et al, So-
cial priming enhances interpersonal synchronization and feeling of connectedness towards
schizophrenia patients. Scientiﬁc reports, 5, 2015
[8] L. Noy, E. Dekel, U. Alon, The mirror game as a paradigm for studying the dynamics of
two people improvising motion together, Proceedings of the National Academy of Sciences,
108(52), 20947-20952, 2011.
[9] L. Noy, N. Levit-Binun, Y. Golland, Being in the zone: physiological markers of together-
ness in joint improvisation, Frontiers in human neuroscience, 9, 187-187, 2014.
22


## Page 23


[10] C. Zhai, F. Alderisio, K. Tsaneva-Atanasova, M. di Bernardo, A novel cognitive architec-
ture for a human-like virtual player in the mirror game, Proceedings of the 2014 IEEE
International Conference on Systems, Man, and Cybernetics, pp. 754-759, 2014.
[11] M. I. Jordan, D. M. Wolpert, Computational Motor Control, 1999.
[12] M. Desmurget, S. Grafton, Forward modeling allows feedback control for fast reaching
movements, Trends in Cognitive Sciences, 4(11), 423-431, 2000.
[13] C. Zhai, F. Alderisio, K. Tsaneva-Atanasova, M. di Bernardo, A model predictive approach
to control the motion of a virtual player in the mirror game, Proceedings of the 54th IEEE
Conference on Decision and Control, pp. 3175-3180, 2015.
[14] C. Zhai, F. Alderisio, P. S lowi´nski, K. Tsaneva-Atanasova, M. di Bernardo, Design of a
virtual player for joint improvisation with humans in the mirror game, PLoS ONE, 11(4),
e0154361, 2016.
[15] P. S lowi´nski, C. Zhai, F. Alderisio, R. Salesse, M. Gueugnon, L. Marin, B. G. Bardy, M. di
Bernardo, K. Tsaneva-Atanasova, Dynamic similarity promotes interpersonal coordination
in joint action, Journal of The Royal Society Interface, 13(116): 20151093, 2016.
[16] Y. Hart, L. Noy, R. Feniger-Schaal, A. E. Mayo, U. Alon, Individuality and togetherness
in joint improvised motion, PLoS ONE, 9(2), e87213, 2014.
[17] X. Li, G. Chi, S. Vidas, C. C. Cheah, Human-guided robotic comanipulation: two illus-
trative scenarios, IEEE Transactions on Control Systems Technology (24)5, 1751-1763,
2016.
[18] S. F. Atashzar, M. Shahbazi, M. Tavakoli, R. V. Patel, A passivity-based approach for sta-
ble patient-robot interaction in haptics-enabled rehabilitation systems: modulated time-
domain passivity control, IEEE Transactions on Control Systems Technology,(PP)99, 1-16,
2016.
[19] A. M¨ortl, T. Lorenz, S. Hirche, Rhythm patterns interaction-synchronization behavior for
human-robot joint action, PLoS ONE, 9(4), e95195, 2014.
[20] G. Dumas, G. C. de Guzman, E. Tognoli, J. S. Kelso, The human dynamic clamp as a
paradigm for social interaction, Proceedings of the National Academy of Sciences, 111(35),
e3726-e3734, 2014.
23


## Page 24


[21] C. Zhai, F. Alderisio, K. Tsaneva-Atanasova, M. di Bernardo, Adaptive tracking control of
a virtual player in the mirror game, Proceedings of the 53rd IEEE Conference on Decision
and Control, pp. 7005-7010, 2014.
[22] J. S. Kelso, G. C. de Guzman, C. Reveley, E. Tognoli, E, Virtual partner interaction (VPI):
exploring novel behaviors via coordination dynamics, PLoS ONE, 4(6): e5749, 2009.
[23] C. Zhai, F. Alderisio, P. S lowi´nski, K. Tsaneva-Atanasova, M. di Bernardo, Design and
validation of a virtual player for studying interpersonal coordination in the mirror game,
arXiv preprint arXiv:1509.05881, 2015.
[24] A. Dahan, L. Noy, Y. Hart, A. Mayo, U. Alon, Exit from Synchrony in Joint Improvised
Movement, PLoS ONE 11(10):e0160747, 2016.
[25] P. S lowi´nski, E. Rooke, M. di Bernardo, K. Tanaseva-Atanasova, Kinematic characteristics
of motion in the mirror game, Proceedings of the 2014 IEEE International Conference on
Systems, Man and Cybernetics, pp. 748-753, 2014.
[26] T. Flash, N. Hogan, The coordination of arm movements: an experimentally conﬁrmed
mathematical model, The Journal of Neuroscience, 5(7), 1688-1703, 1985.
[27] E. A. Kalinina, A. Yu. Uteshev, Elimination Theory (in Russian) SPb, Nii khimii, 2002.
[28] M. Bˆocher, Introduction to Higher Algebra. NY. Macmillan, 1907.
[29] H. Haken, J. S. Kelso, and H. Bunz, A theoretical model of phase transitions in human
hand movements. Biological cybernetics, 51(5), 347-356, 1985.
[30] F. Alderisio, D. Antonacci, C. Zhai, M. di Bernardo, Comparing diﬀerent control ap-
proaches to implement a human-like virtual player in the mirror game, Proceedings of the
15th European Control Conference (ECC), pp. 216-221, 2016.
[31] F. Alderisio, M. Lombardi, G. Fiore, M. di Bernardo, Study of movement coordination
in human ensembles via a novel computer-based set-up, arXiv preprint arXiv:1608.04652,
2016.
[32] M. Z. Q. Chen, L. Y. Zhang, H. S. Su, G. R. Chen, Stabilizing solution and parameter de-
pendence of modiﬁed algebraic Riccati equation with application to discrete-time network
synchronization, IEEE Transactions on Automatic Control, 61(1), 228-233, 2016.
24


## Page 25


[33] M. Z. Q. Chen, L. Y. Zhang, H. S. Su, C. Y. Li, Event-based synchronisation of linear
discrete-time dynamical networks, IET Control Theory and Application, 9(5), 755-765,
2015.
[34] F. Alderisio, G. Fiore, R. N. Salesse, B. G. Bardy, M. di Bernardo, Interaction pat-
terns and individual dynamics shape the way we move in synchrony, arXiv preprint
arXiv:1607.02175, 2016.
[35] F. Alderisio, B. G. Bardy, M. di Bernardo, Entrainment and synchronization in networks
of Rayleigh–van der Pol oscillators with diﬀusive and Haken–Kelso–Bunz couplings, Bio-
logical cybernetics, 110(2),151-169, 2016.
25

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
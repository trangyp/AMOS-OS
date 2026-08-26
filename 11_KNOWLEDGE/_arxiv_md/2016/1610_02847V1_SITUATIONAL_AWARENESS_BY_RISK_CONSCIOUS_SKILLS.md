---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1610.02847v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1610.02847v1_Situational_Awareness_by_Risk-Conscious_Skills

> Source: 1610.02847v1_Situational_Awareness_by_Risk-Conscious_Skills.pdf

> Pages: 15

---


## Page 1


Situational Awareness by Risk-Conscious Skills
Daniel J. Mankowitz
Electrical Engineering Department,
The Technion - Israel Institute of Technology,
Haifa 32000, Israel
danielm@tx.technion.ac.il
Aviv Tamar
Electrical Engineering and
Computer Sciences Department,
UC Berkeley
CA, USA
avivt@berkeley.edu
Shie Mannor
Electrical Engineering Department,
The Technion - Israel Institute of Technology,
Haifa 32000, Israel
shie@ee.technion.ac.il
Abstract
Hierarchical Reinforcement Learning has been previously shown to speed up the
convergence rate of RL planning algorithms as well as mitigate feature-based
model misspeciﬁcation Mankowitz et al. (2016a,b); Bacon & Precup (2015). To do
so, it utilizes hierarchical abstractions, also known as skills – a type of temporally
extended action Sutton et al. (1999) to plan at a higher level, abstracting away from
the lower-level details. We incorporate risk sensitivity, also referred to as Situational
Awareness (SA) , into hierarchical RL for the ﬁrst time by deﬁning and learning risk
aware skills in a Probabilistic Goal Semi-Markov Decision Process (PG-SMDP).
This is achieved using our novel Situational Awareness by Risk-Conscious Skills
(SARiCoS) algorithm which comes with a theoretical convergence guarantee. We
show in a RoboCup soccer domain that the learned risk aware skills exhibit complex
human behaviors such as ‘time-wasting’ in a soccer game. In addition, the learned
risk aware skills are able to mitigate reward-based model misspeciﬁcation.
1
Introduction
Hierarchical-Reinforcement Learning (H-RL) is an RL paradigm that utilizes hierarchical abstractions
to solve tasks. This enables an agent to abstract away from the lower-level details and focus more
on solving the task at hand. Hierarchical abstractions have been utilized to naturally model many
real-world problems in machine learning and, more speciﬁcally, in RL. This includes high-level
controllers in robotics Peters & Schaal (2008); Hagras et al. (2004); da Silva et al. (2012), strategies
(such as attack and defend) in soccer Bai et al. (2015) and video games Mann (2015), as well as high-
level sub-tasks in search and rescue missions Liu & Nejat (2015). In RL, hierarchical abstractions are
typically referred to as skills, (da Silva et al. (2012)), Temporally Extended Actions (TEAs), options
(Sutton et al. (1999)) or macro-actions, (Hauskrecht (1998)). We will use the term skill to refer to
hierarchical abstractions from here on in.
H-RL is important as it utilizes skills to both speed up the convergence rate in RL planning algorithms
Mann & Mannor (2013); Precup & Sutton (1997); Mankowitz et al. (2014) as well as mitigating
model misspeciﬁcation. Model misspeciﬁcation in RL can be sub-divided into (1) feature-based
model misspeciﬁcation - where a limited, sub-optimal feature set is provided (e.g., due to limited
memory resources or sub-optimal feature selection) leading to sub-optimal performance; and (2)
reward-based model misspeciﬁcation whereby the reward shaping function is incorrectly designed
arXiv:1610.02847v1  [cs.AI]  10 Oct 2016


## Page 2


Goal
Keep possession when winning
(a)
(b)
Shoot
Goal
Attack when losing
B
B
P
P
P
P
P
P
Figure 1: Time-based SA - Blue players are
on the same team: (a) Playing attacking soc-
cer when losing a game and time is running
out; (b) Keeping possession and time-wasting
when winning the game and time is running
out.
Dry
Wet Puddles
Wide 
Narrow
(a)
(b)
Figure 2: Spatial SA: (a) Wide/Narrow lanes;
(b) Dry/Wet roads
(e.g., due to an incorrect understanding of the target problem). Previous work has focused on utilizing
skills to mitigate feature-based model misspeciﬁcation Mankowitz et al. (2014, 2016a,b), but have
not attempted to mitigate reward-based model misspeciﬁcation. Risk sensitivity can be utilized to
mitigate this form of misspeciﬁcation.
An important factor missing in H-RL is risk sensitivity. A risk-sensitive H-RL framework would
enable us to generate skills with different Risk Attitudes, also known as Situational Awareness (SA)
Endsley (1995); Smith & Hancock (1995), which, as we will show in our paper, allows us to mitigate
reward-based model misspeciﬁcation. As seen in Table 1, previous work in H-RL has focused on
skill learning Mankowitz et al. (2014, 2016a,b), but has not incorporated risk-sensitivity into the
H-RL objective, nor learned risk aware skills to mitigate reward-based model misspeciﬁcation. From
here on in, the terms risk sensitivity, risk attitude and SA will be used interchangeably.
Situational Awareness (SA): SA can be dependent on both time and space, although the focus of
this paper is on time-based SA. We provide both deﬁnitions below.
Time-based SA: Consider a soccer game composed of complicated strategies (skills), such as attack
and defend, based on the status of the game. Consider a team losing by one goal to zero with ten
minutes remaining. Here, the team needs to play attacking, risky soccer such as making long, risky
passes as well as shooting from distance to try and score goals and win the game (Figure 1a). On the
other hand, if the team is winning by one goal to zero with ten minutes remaining, the team needs
to ‘waste time’ by maintaining possession and playing risk-averse, defensive football to prevent the
opponent from gaining the ball and scoring goals (Figure 1b). In both scenarios the team has the
same objective which is to score more goals than their opponent once time runs out (I.e. win the
game). Time-based SA enables an agent to act in a risk-aware manner based on the amount of time
remaining in the task.
Spatial SA: As mentioned previously, SA can also be deﬁned in terms of space. Consider an
autonomous vehicle (the agent) driving in a narrow/wide lane or on dry/wet roads as shown in Figure
2. The proximity of the agent to the other vehicles in the lane example (Figure 2a), or the distance of
the agent to other vehicles as well as puddles in the dry/wet road example (Figure 2b) determines the
SA and therefore the risk attitude of the agent.
Our main idea in this paper, is that a simple way to add risk-sensitivity to H-RL is by maximizing a
risk-sensitive objective rather than the regular expected return formulation. One example that we
focus on in this work is that of a Probabilistic Goal Markov Decision Process (PG-MDP) Xu &
Mannor (2011). Previous works that incorporate risk into RL have mainly been focused on learning a
single risk aware policy in a non-hierarchical setting Avila-Godoy & Fernández-Gaucherand (1998);
Tamar et al. (2015a,b) by maximizing the Conditional Value-at-Risk or the Value-at-Risk objectives.
We provide a framework that enables an agent, for the ﬁrst time to solve a task by maximizing a risk-
sensitive objective in hierarchical RL. We deﬁne a Probabilistic Goal Semi-Markov Decision Process
(PG-SMDP) which naturally models this setting. By solving the PG-SMDP using our novel SARiCoS
algorithm, the agent learns Risk-Aware Skills (RASs) that have a particular Risk Attitude/SA. We
show that the learned risk-aware skills exhibit complex human behaviours such as time-wasting in a
soccer game. We then show in our experiments that these skills can be used to overcome reward-based
model misspeciﬁcation, in contrast to the regular expected return formulation.
2


## Page 3


Table 1: Comparison of Approaches to SARiCoS
Maxmizes a
Learns
Learns
Uses skills to
hierarchical risk-aware
RL skills
risk-aware RL skills
mitigate reward-based
RL objective
(E.g. time wasting in soccer)
model misspeciﬁcation
SARiCoS (this paper)
✓
✓
✓
✓
Mankowitz et al. (2016b)
×
✓
×
×
Mankowitz et al. (2016a)
×
✓
×
×
Bacon & Precup (2015)
×
✓
×
×
Masson & Konidaris (2015)
×
×
×
×
Main Contributions: (1) Extending hierarchical RL to incorporate SA by deﬁning a Probabilistic
Goal Semi-Markov Decision Process (PG-SMDP) (2) The development of the Situational Awareness
by Risk-Conscious Skills (SARiCoS) algorithm which optimizes a hierarchical risk-aware RL
objective and learns Risk-Aware Skills (RASs) that incorporate SA. (3) Theorem 1 which derives
a policy gradient update rule for learning Risk Aware Skills and inter-skill policy parameters in a
Probabilistic Goal Semi-Markov Decision Process (PG-SMDP). (4) Theorem 2 which proves that
SARiCoS converges to a locally optimal solution. (5) Experiments in the RoboCup domain that
exhibit an agent’s ability to learn skills possessing SA (e.g., time wasting in a soccer game). In
addition, we show the agent utilizing these skills to overcome reward-based model misspeciﬁcation.
2
Background
Semi-Markov Decision Process (SMDP) Sutton et al. (1999) A Semi-Markov Decision Process
can be deﬁned by the 5-tuple ⟨X, Σ, P, R, γ⟩, where X is a set of states, Σ is a set of skills, P is a
transition probability function and R is a bounded reward function. We assume that the rewards we
receive at each timestep are bounded between [0, Rmax]. Therefore R forms a mapping from X × Σ
to [0, Rmax
1−γ ] and represents the expected discounted sum of rewards that are received from executing
skill σ ∈Σ from state x ∈X. The discount factor is deﬁned as γ ∈[0, 1]. The inter-skill policy
µ : X →∆Σ maps states to a probability distribution over skills. The goal in an SMDP is to ﬁnd
the optimal inter-skill policy µ∗that maximizes the value function V µ(x) = E
P∞
t=0 γtRt|x, µ

.
This represents the expected return of following the inter-skill policy µ from state x. The optimal
policy µ∗determines the best action to take for a given state and generates the optimal value function
V µ∗(s).
Skill, Option and Macro-Action Sutton et al. (1999); da Silva et al. (2012): An RL skill, option or
macro action σ is deﬁned as the 3-tuple σ = ⟨I, πθ, p(x)⟩where I is a set of initiation states from
which a skill can be initialized or executed; πθ is the intra-skill policy which selects the lower-level
(or primitive) actions to perform whilst the skill is executing and is parameterized by θ ∈Rn; The
termination probability p(x) which determines the probability of the skill terminating when in state
x.
Probabilistic Goal MDP (PG-MDP) Xu & Mannor (2011): While the standard MDP objective
presented above considered the expected reward, in some situations different objectives may be more
appropriate. In particular, risk-sensitive criteria that maximize the probabilty of success, and not just
the expected outcome, are natural objectives in domains such as ﬁnance and operations research, but
also in game-playing, such as soccer. The PG-MDP is an extension of the MDP that accounts for
such an objective. In a PG-MDP, the goal is to learn a policy π that maximizes the probability that
some performance threshold will be attained. That is, it aims to maximize:
P(Wπ ≥β) ,
(1)
where Wπ is a random variable representing the total reward of the MDP under the policy π. The
parameter β ∈R is a performance threshold. The PG-MDP formulation is key for our risk shaping
method, and will be further discussed when deﬁning the PG-SMDP.
Policy Gradient Peters & Schaal (2006): In continuous as well as high-dimensional MDPs, it is
computationally inefﬁcient to learn a policy that determines an action to perform for any given state.
Policies therefore need to be generalizable, where the policy will choose the same or similar action
to perform when in nearby states. In order to achieve this generalization, a policy is parameterized
using techniques such as Linear Function Approximation (LFA) (which we use in this work) Sutton
3


## Page 4


& Barto (1998). A popular technique to learning the parameters for these parameterized policies is
the policy gradient method. Let Jπ(θ) denote the expected return of the policy parametrized by θ as
Jπ(θ) =
R
τ P(τ)R(τ)dτ where τ is a trajectory of T timesteps ⟨x1, a1, r1, x2 · · · , xT ⟩; P(τ) is the
probability of a trajectory and R(τ) is deﬁned as the total reward of the trajectory. Policy gradient
uses sampling to estimate the gradient ∇θJπ(θ) and then updates the parameters using a gradient
ascent update rule θt+1 = θt + ϵ∇θJπ(θ) where ϵ denotes a positive step size.
3
Probabilistic Goal SMDP (PG-SMDP)
In this work we focus on solving problems in which the agent must maximize its probability of
success for solving a given task in a limited amount of time. A natural model for such problems is
the the PG-MDP framework described above. However, we are interested in complex problems that
require some hierarchical reasoning, and therefore propose to extend PG-MDPs to incorporate skills,
leading to a PG Semi-MDP (PG-SMDP) model. We now derive an equivalent PG-SMDP with an
augmented state space and skill set Σ that can easily be utilized with policy gradient algorithms.
We assume that we are given a set of skills Σ = {σi|i = 1, 2, · · · n, σj = ⟨Ij, πj, pj(x)⟩} and
inter-skill policy µ(σ|x) →∆Σ which chooses a skill to execute given the current state x ∈X. We
wish to maximize the probability that the total accumulated reward, PT
t=0 rt, attained during the
execution of the inter-skill policy µ, passes the pre-deﬁned performance objective threshold β ∈R
within T timesteps. This takes the form of a Probabilistic Goal SMDP (PG-SMDP) (since we are
incorporating skills) deﬁned in Equation 2.
max
µ
P(
T
X
t=0
rt ≥β|µ) .
(2)
In order to solve this PG-SMDP using traditional RL techniques, we augment the state space with the
total accumulated reward Xu & Mannor (2011) to create an equivalent augmented PG-SMDP. We
will show the important developments of this formulation for reader clarity. This will enable us to
utilize traditional RL techniques in order to maximize the probability of surpassing the performance
threshold β, given a set of skills Σ, within T timesteps. First note that maximizing the probability
can be formulated as an expectation as shown in Equation 3.
maxµ P
PT
t=0 r(xt, σt) ≥β
 µ

=
maxµ Eµ h
I
PT
t=0 r(xt, σt) ≥β
i
(3)
This expectation still contains a constraint. We now formulate an equivalent augmented PG-SMDP
that removes the β constraint and incorporates the constraint into the reward function. Deﬁne an
augmented state z = {x, w} where x ∈X is the original state space and w = PT
t=0 r(xt, σt) is the
accumulated reward up until time T. We can then deﬁne the transition probabilities in terms of the
augmented state z according to Equation 4.
P(z′|z, σ) = {{x′, w + r(x, σ)}w.p P(x′|x, σ)} .
(4)
The reward function for this augmented state is then deﬁned according to Equation 5.
˜rt(z, σ) =



0,
t < T
0,
t = T, w < β
1,
t = T, w ≥β
(5)
Together, the transition probabilities and the reward function forms an equivalent PG-SMDP with an
augmented state space z ∈Z as shown in Equation 6. This formulation learns an inter-skill policy
4


## Page 5


µ that maximizes the probability that the total accumulated reward will surpass the performance
threshold β within T timesteps.
max
µ
E
" T
X
t=0
˜r(zt, σt)
#
(6)
In the next Section, we show that risk can be incorporated into the PG-SMDP by incorporating a Risk
Awareness Parameter (RAP) into the typical deﬁnition of a skill to form a Risk Aware Skill (RAS).
We derive a policy gradient algorithm to learn both the inter-skill policy and the RAPs such that the
agent is able to successfully solve the PG-SMDP.
4
Risk-Aware Skill
We modify the typical deﬁnition of a skill to include a parameter, called the Risk-Awareness Parameter
(RAP) yw ∈R. This is the parameter that controls the risk-attitude of the Risk-Aware Skill (RAS).
Deﬁnition 1. A Risk Aware Skill (RAS) σ is a temporally extended action that consists of the 4-tuple
σ = ⟨I, πθ, p(z), yw⟩, where I are the set of states from where the RAS can be initialized; πθ is the
parameterized intra skill policy; p(z) is the probability of terminating in state z ∈Z; and yw ∈R is
the Risk-Awareness Parameter (RAP) governed by the Risk-Aware Distribution (RAD) yw ∼Pw(·)
with parameters w ∈Rm.
In practice, the RAP can parameterize the intra-skill policy, or act as a meta-parameter for the RAS
(E.g. Dribble power in the RoboCup experiment (See Experiments Section)).
5
SARiCoS Algorithm
The Situational Awareness by Risk-Conscious Skills (SARiCoS) algorithm learns the parameters of a
two-tiered skill selection policy deﬁned as:
µα,Ωi(σ, y|z) = µα(σ|z)µσi
Ωi(y|z) ,
(7)
where µα : Z →∆Σ is the inter-skill policy, parameterized by α ∈Rd, that selects which RAS σ
needs to be executed from a set Σ of N RASs, given the current state z ∈Z.; µσi
Ωi(·|z) is the RAD
for RAS σi with RAD parameters Ωi = wi ∈Rm. The RAD parameters for all RASs are stored in a
vector Ω= [ω1, ω2, · · · , ωN] ∈R|N||m|×1 for algorithmic purposes.
The two-tiered skill selection policy is executed by ﬁrst sampling a Risk-Aware Skill σi to execute
from µα(σ|z). The risk attitude of the skill is then determined by sampling the RAP from the RAD
µσi
Ωi(y|z). SARiCoS learns (1) the inter-skill policy parameters α ∈Rd and (2) the RAD parameters
Ωto produce Situationally Aware RASs. In order to derive gradient update rules for these parameters
in a policy gradient setting, we deﬁne the notion of a risk-aware trajectory.
Risk-Aware Trajectory: In the standard policy gradient framework, we deﬁne a typical trajectory as
τ = (zt, σt, rt, zt+1)T
t=0 where T is the length of the trajectory. To incorporate the two-tiered policy
into this trajectory, we deﬁne a risk-aware trajectory τr = (zt, σt, ywσtrt, zt+1)T
t=0 where at each
timestep, we draw a RAP corresponding to the RAS σt that was selected. We can therefore deﬁne the
probability of a trajectory as Pα,Ω(τr) = P(z0) QT −1
t=0 P(zt+1|zt, σt)µα,Ω(σt, yt|zt), where P(z0) is
the initial state distribution; P(zt+1|zt, σt) is the transition probability of moving from state zt to
state zt+1 given that a RAS σt was executed; and µα,Ω(σt, yt|zt) is the two-tiered selection policy.
Using this notion, it is now possible to derive the gradient update rules for each set of parameters as
shown in Theorem 1.
5.1
Inter-skill policy and RAP Update Rules
We deﬁne the expected reward for following a policy µα,Ω:
J(µα,Ω) =
Z
τ
P(τ|α, Ω)R(τ)dτ .
(8)
5


## Page 6


Let us group the parameters for the inter-skill policy and the continuous RAD Parameters into a
single vector χ = [α, Ω] ∈Rd+m·N. Taking the derivative of this objective and using the well-known
likelihood trick Peters & Schaal (2008) yields:
∇χJ(µχ) =
Z
τ
P(τ|χ)∇α log P(τ|χ)R(τ)dτ ,
(9)
where P(τ|χ) = P(z0) QT
k=1 P(zk+1|zk, σk)P(σk|zk, χ); zk ∈Z is the state at timestep k; σk
is the RAS selected at timestep k and T is the length of the trajectory. Since only P(σk|zk, χ) is
parameterized, the gradient ∇χJ(µχ) can be simpliﬁed to:
∇χJ(µχ) =
Z
τ
P(τ|χ)∇χ log P(σk|zk, χ)R(τ)dτ ,
(10)
where P(σk|zk, χ) = µα(σt|zt)µσt
Ω(yt|zt). Therefore, substituting the two-tiered policy into Equa-
tion 20 and deriving with respect to α leads to the gradient update rule:
∇αJ(µχ)
=
Z
τ
P(τ|χ)∇α log µα(σt|zt)R(τ)dτ .
If we represent µα(σt|zt) as a Gibb’s distribution which is a common policy choice in many MDPs
Sutton & Barto (1998), then we can easily derive the gradient and estimate it by samples using the
following gradient update rule:
∇αJ(µχ) =
* H
X
h=0
∇α log µα(σh|zh)
H
X
j=0
γjrj
+
(11)
If we substitute the two-tiered policy into Equation 20 and deriving with respect to Ωfor the RAD
Parameters, then we get the following gradient update rule:
∇ΩJ(µχ)
=
Z
τ
P(τ|χ)∇Ωlog µσt
Ω(yt|zt)R(τ)dτ .
If we represent µσt
Ω(yt|zt) as any distribution from the natural exponential family, then we can easily
derive the gradient and estimate it by samples using the following gradient update rule:
∇ΩJ(µχ) =
* H
X
h=0
∇Ωlog µσt
Ω(yt|zt)
H
X
j=0
γjrj
+
(12)
These derivations are summarized in Theorem 1. A full proof can be found in the supplementary
material.
Theorem 1 (Gradient Update Derivation). Suppose that we are maximizing the Policy Gradient
(PG) objective J(µα,Ω) =
R
τ Pα,Ω(τ)R(τ)dτ using risk-aware trajectories, generated by the two-
tiered skill selection policy µα(σt|xt)µσt
Ω(yt|zt), then the expectation of the gradient update rules
for the inter-skill policy parameters α ∈Rd and the RAD parameters Ω∈R|N||m| are the true
gradients and are deﬁned as (1) ∇αJ(µα,Ω) =
DPH
h=0 ∇α log µα(σh|zh) PH
j=0 γjrj
E
and (2)
∇ΩJ(µα,Ω) =
DPH
h=0 ∇Ωlog µσt
Ω(yt|zt) PH
j=0 γjrj
E
respectively. H is the trajectory length and
< · > is an average over trajectories as in standard PG.
Given the gradient update rules, we can derive an algorithm for learning both the inter-skill parameters
α ∈Rd and the continuous RAD parameters Ω= [ω1, ω2, · · · , ωN] ∈R|N||m|×1 for the N RAS.
SARiCoS learns these parameters by two timescale stochastic approximation, as shown in Algorithm
1, and converges to a locally optimal solution as is proven in Theorem 2. The convergence proof is
based on standard two-timescale stochastic approximation convergence arguments Borkar (1997) and
is found in the supplementary material.
6


## Page 7


Theorem 2 (SARiCoS Convergence). Suppose we are optimizing the expected return J(µΩ,α) =
R
R(τ)P(τ)dτ for any arbitrary SARiCoS policy µΩ,α where Ω∈R|N||m| and α ∈Rd are the
inter-skill and Risk Aware Distribution parameters respectively. Then, for step sizes sequences
{ak}∞
k=0, {bk}∞
k=0 that satisfy P
k ak = ∞, P
k bk = ∞, P
k a2
k < ∞, P
k b2
k < ∞and bk > ak,
the SARiCoS iterates converge a.s αk →α∗, Ωk →¯λ(α∗) as k →∞to the countable set of locally
optimal points of J(µΩ,α).
Algorithm 1 SARiCoS Algorithm
Require: α ∈Rd. {Inter-skill policy parameterization}, Ω∈R|N||m|×1 {Set of RAD parameters
for each skill}
1: repeat:
2: αk+1 →αk + ak∇αJα,Ω
3: Ωk+1 →Ωk + bk∇ΩJα,Ω{stepsize bk > ak}
4: until convergence
6
Experiments
The experiments were performed in the RoboCup 2D soccer simulation domain Akiyama &
Nakashima (2014); a well-known benchmark for many AI challenges. In the experiments, we
demonstrate the ability of the agent to learn risk-aware skills (such as ‘time-wasting’ in a soccer
game), and therefore exhibit SA, by maximizing the PG-SMDP objective. In the RoboCup domain,
we also show the agent’s ability to exit local optima due to reward shaping and therefore overcome
reward-based model misspeciﬁcation.
RoboCup Offense (RO) Domain: This domain 1 consists of two teams on a soccer ﬁeld where the
striker (the yellow agent) needs to score against a goalkeeper (purple circle) as shown in Figure 3a.
The striker has T = 150 timesteps (length of the episode) to try and score a goal. State space - The
state space in RO consists of the continuous ⟨x, y⟩ﬁeld locations of the striker, ball, goalposts and
goalkeeper as well as the cumulative sum of rewards w. Skills - The Risk-Aware Skill (RAS) set Σ
in each of the experiments consists of three RAS: (1) Move to the ball (M), (2) Move to the ball and
shoot towards the goal (S) and (3) Move to the ball and dribble in the direction of the goal (D). Each
RAS i is parameterized with a Risk Aware Parameter ywi. We focus on learning the dribbling power
RAP yw,D that controls how hard the agent kicks the ball when performing the skill Dribble. Data:
SARiCoS is trained over 3 independent trials with 20, 000 episodes per trial. Learning Algorithm
and features - The learning algorithm for both the inter-skill policy parameters α and the RAPs for
the RASs is Actor Critic Policy Gradient (AC-PG) 2. The inter-skill policy µ that chooses which
RAS to execute is represented by a Gibb’s distribution with Fourier Features. The Risk Aware
Distribution (RAD) is represented as a normal distribution y ∼N(φ(s)T ω, V ) with a ﬁxed variance
V . Here, φ(s) are state dependent features [1, xagent, yagent, w, distGoal] representing the agent’s
x, y location, the cumulative reward and the distance of the agent to the goal. Rewards - Engineering
of the reward in RL is common practice for the RoboCup domain Hausknecht & Stone (2015); Bai
et al. (2015). The rewards for both of the RoboCup scenarios have been engineered based on logical
soccer strategies. The striker gets small positive rewards for dribbling outside the box rD,far and
shooting when inside or near the box rS,near. Negative rewards come about when the striker dribbles
inside the box, rD,near, or shoots from far, rS,far, as the striker has a smaller probability of scoring
Yiannakos & Armatas (2006). The striker also gets a small positive reward for moving towards the
ball rmove. There is also a game score reward rscore, which is positive if winning and negative if
losing or drawing. In the PG-SMDP setting, the rewards ˜r = 1 if w >= β at the end of each episode,
otherwise the reward is 0 at each timestep. In the Expected Return setting (see Reward-Based Model
Misspeciﬁcation), the regular rewards are utilized at each timestep.
6.1
Situational Awareness by Risk-Conscious Skills
In this section we show that learning the inter-skill policy and RAD parameters using SARiCoS so as
to maximize a PG-SMDP can bring about risk-aware skills that exhibit time-based SA. We provide
1https://github.com/mhauskn/HFO
2AC-PG has lower variance compared to regular PG and the convergence guarantees are trivial extensions of
the current proof.
7


## Page 8


Figure 3: (a) The RO domain (b) SA for a winning scenario (i) and a losing scenario (ii) (c) The RAP
values (dribble power) for the D skill superimposed onto the soccer ﬁeld. Red indicates a fast dribble
(hard kicks) and blue indicates a slow dribble (short kicks). (d) Reward-based model misspeciﬁcation:
the trajectories for the trained Expected Return (ER) and SARiCoS policies.
the agent with two different soccer situations: (1) The agent is losing the game 0 −1; (2) The agent
is winning the game 1 −0. Similar results are obtained for different scores (e.g., 2 −0 and 0 −2
etc. and have therefore been omitted). For all of the scenarios, the performance threshold β for the
PG-SMDP is set to a constant value (β = 1.0) a-priori.
SA in a Losing Scenario: In a scenario where a team is losing and time is running out, the team
needs to play risky, attacking soccer to try and score goals. The agent is placed in a losing scenario
where the score is 0 −1 to the opposition with 150 timesteps remaining. Using SARiCoS, the agent
learns to perform a fast Dribble by kicking the ball with signiﬁcant power to make quick progress
along the pitch and get in a position to shoot for goal as seen in Figure 3b(i). The average RAP
value for the Dribble RAS is approximately 100 (max value 150, min value 0) prompting the agent to
kick the ball with signiﬁcant power and quickly advance up the pitch. The RAP is state dependent,
enabling the agent to learn to initially kick the ball with a large amount of power when near the
half-way line and then decrease the dribble power when approaching the goal so as to prevent losing
possession to the goalkeeper. This is seen from the dribble power color gradient superimposed onto
the RO domain in Figure 3c. The color gradient varies from powerful kicks (in red) to soft kicks (in
blue). Once the agent is near the goal, it executes the skill Shoot as seen in the ﬁgure 3b(i). The
average episode length is 70.0 ± 1.0 (mean±std) as seen in Table 2 and the average number of goals
scored over 100 evaluation episodes is 74.3 ± 6.5. In addition, the keeper captures the ball on average
21 ± 5.29 times indicating that the striker is playing risky football with aggressive dribbling and, as a
result, scores a high number of goals. In addition, the average reward is consistently higher than the
β threshold.
SA in a Winning Scenario: When winning a game with little time remaining, a natural strategy is to
hold onto the ball and run out the clock 3 (‘time-wasting’) so as to prevent the opposing team from
gaining possession and possibly scoring a goal. SARiCoS learns ‘time-wasting’ since when the agent
is winning the game 1 −0, the agent slowly dribbles his way up the pitch, collecting the dribble from
far rewards rD,far in the process as seen in Figure 3b(ii). Once the agent crosses the performance
threshold, it stands on the ball, and wastes time by executing the M skill, whilst continuing to collect
the positive score rewards rscore and the small positive rmove rewards. This strategy causes the agent
to take the largest amount of time on average (142.3 ± 1.5 steps) to complete each episode (time
wasting) and as a result only scores 1.3 ± 0.6 goals. However, the ball is almost never captured by
the opponent 7.3 ± 0.6 times on average per 100 evaluation episodes. See a Video4 of the agent’s
behavior in each of these scenarios.
6.2
Mitigating Reward-based Model Misspeciﬁed
The learned risk-aware skills can be utilized to overcome reward-based model misspeciﬁcation. We
focus on the losing scenario in RoboCup soccer. We compared SARiCoS to the regular Expected
Return (ER) formulation, i.e., an implementation of Actor-Critic Policy Gradient that utilizes regular
rewards at each timestep to learn a game-winning policy.
As seen in Figure 3d, the ER striker (light blue circle) does not learn to score goals as the algorithm
settles quickly on collecting positive dribble from far rewards rD,far and moving to the ball rewards
rmove. The ER agent therefore gets stuck in a local optima causing the agent to execute D until it
3http://www.collinsdictionary.com/dictionary/american/run-out-the-clock
4https://youtu.be/xA-8rWJ4a7I
8


## Page 9


Table 2: Performance of the trained SARiCoS and Expected Return (ER) policies in the win-
ning/losing scenarios averaged over 100 evaluation episodes.
SARiCoS
SARiCoS
ER
Winning
Losing
Losing
Goals
1.3 ± 0.6
74.3±6.5
1.7±1.2
Out of Time
90.3±1.5
1.0 ± 1.7
47.0 ± 3.6
Avg Reward
3.9 ± 1.1
6.3±0.2
-0.3±0.1
Episode Length
142.3 ± 1.5
70.0 ± 1.0
107.3 ± 3.8
settles on the M skill and stands on the ball, receiving small positive rewards. As seen in Table 2, the
ER agent only manages to score 1.7 ± 1.2 goals on average and has a low average reward −0.3 ± 0.1,
well below the β threshold.
These rewards are therefore not enough to enable the SARiCoS agent (yellow circle in Figure 3d) to
pass its performance threshold β, especially since, in the losing scenario, the agents are also receiving
a negative game score reward rscore at each timestep. This forces the SARiCoS agent to search for
additional rewards such as a goal-scoring reward. As seen in Table 2, the SARiCoS agent learns to
score goals (74 ± 6.5), and achieves average reward well above the β performance threshold. As a
result it mitigates the reward shaping-based model misspeciﬁcation.
7
Discussion
We have deﬁned a PG-SMDP which provides a natural risk-sensitive objective for learning SA in
hierarchical RL. We ﬁnd it interesting that an agent can learn a complex human behavior by simply
maximizing a risk-sensitive objective. To do so, we have introduced Risk-Aware Skills (RASs) — a
type of parameterized option Sutton et al. (1999) with an additional Risk-Aware Parameter (RAP).
We have developed the Situational Awareness by Risk-Conscious Skills (SARiCoS) algorithm which
learns both the inter-skill policy that chooses RASs to execute, as well as learning the RAPs for each
RAS. We have shown that this algorithm converges to a locally optimal solution. We also show that
SARiCoS can induce situational awareness (E.g. ‘time-wasting’) in Risk-Aware Skills in a time
dependent RoboCup soccer scenario. In principle, any other risk criteria can be incorporated into this
work such as exponential risk, CVaR and VaR Avila-Godoy & Fernández-Gaucherand (1998); Tamar
et al. (2015a,b). Extensions of this work include optimizing a PG-MDP performance threshold β for
each RAS as well as utilizing SA in lifelong learning problems Thrun & Mitchell (1995); Pickett &
Barto (2002); Brunskill & Li (2014). The SARiCoS policy could also be implemented as a Deep
Network Mnih et al. (2015), leading to more complex policies on higher dimensional problems.
Acknowledgements
The research leading to these results has received funding from the European Research Council
under the European Union’s Seventh Framework Program (FP/2007-2013) / ERC Grant Agreement n.
306638.
References
Akiyama, Hidehisa and Nakashima, Tomoharu. Helios base: An open source package for the robocup
soccer 2d simulation. In RoboCup 2013: Robot World Cup XVII, pp. 528–535. Springer, 2014.
Avila-Godoy, Guadalupe and Fernández-Gaucherand, Emmanuel. Controlled markov chains with
exponential risk-sensitive criteria: modularity, structured policies and applications. In Decision
and Control, 1998. Proceedings of the 37th IEEE Conference on, volume 1, pp. 778–783. IEEE,
1998.
Bacon, Pierre-Luc and Precup, Doina. The option-critic architecture. In NIPS Deep Reinforcement
Learning Workshop, 2015.
Bai, Aijun, Wu, Feng, and Chen, Xiaoping. Online planning for large markov decision processes
with hierarchical decomposition. ACM Transactions on Intelligent Systems and Technology (TIST),
6(4):45, 2015.
9


## Page 10


Borkar, Vivek S. Stochastic approximation with two time scales. Systems & Control Letters, 29(5):
291–294, 1997.
Brunskill, Emma and Li, Lihong. Pac-inspired option discovery in lifelong reinforcement learning. In
Proceedings of the 31st International Conference on Machine Learning (ICML-14), pp. 316–324,
2014.
da Silva, B.C., Konidaris, G.D., and Barto, A.G. Learning parameterized skills. In Proceedings of
the Twenty Ninth International Conference on Machine Learning, June 2012.
Endsley, Mica R. Toward a theory of situation awareness in dynamic systems. Human Factors: The
Journal of the Human Factors and Ergonomics Society, 37(1):32–64, 1995.
Hagras, Hani et al. A hierarchical type-2 fuzzy logic control architecture for autonomous mobile
robots. Fuzzy Systems, IEEE Transactions on, 12(4):524–539, 2004.
Hausknecht, Matthew and Stone, Peter. Deep reinforcement learning in parameterized action space.
arXiv preprint arXiv:1511.04143, 2015.
Hauskrecht, Milos.
Planning with macro-actions: Effect of initial value function estimate on
convergence rate of value iteration. Technical report, Brown University, 1998.
Liu, Yugang and Nejat, Goldie. Multirobot cooperative learning for semiautonomous control in urban
search and rescue applications. Journal of Field Robotics, 2015.
Mankowitz, Daniel J, Mann, Timothy A, and Mannor, Shie. Time regularized interrupting options.
Internation Conference on Machine Learning, 2014.
Mankowitz, Daniel J., Mann, Timothy A., and Mannor, Shie. Iterative Hierarchical Optimization
for Misspeciﬁed Problems (IHOMP). arXiv preprint arXiv:1602.03348, 2016a. URL http:
//arxiv.org/abs/1602.03348.
Mankowitz, Daniel J., Mann, Timothy A., and Mannor, Shie. Adaptive Skills, Adaptive Partitions
(ASAP). Neural Information Processing Systems (NIPS), 2016b.
Mann, Timothy .A, Mankowitz Daniel J. Mannor Shie. Learning when to switch between skills in a
high dimensional domain. AAAI-2015 Workshop on Learning for General Competency in Video
Games, 2015.
Mann, Timothy A. and Mannor, Shie. The advantage of planning with options. In Proceedings of the
First Annual Conference on Reinforcement Learning and Decision Making (RLDM), 2013.
Masson, Warwick and Konidaris, George. Reinforcement learning with parameterized actions. arXiv
preprint arXiv:1509.01644, 2015.
Mnih, Volodymyr, Kavukcuoglu, Koray, Silver, David, Rusu, Andrei A, Veness, Joel, Bellemare,
Marc G, Graves, Alex, Riedmiller, Martin, Fidjeland, Andreas K, Ostrovski, Georg, et al. Human-
level control through deep reinforcement learning. Nature, 518(7540):529–533, 2015.
Peters, Jan and Schaal, Stefan. Policy gradient methods for robotics. In Intelligent Robots and
Systems, 2006 IEEE/RSJ International Conference on, pp. 2219–2225. IEEE, 2006.
Peters, Jan and Schaal, Stefan. Reinforcement learning of motor skills with policy gradients. Neural
networks, 21(4):682–697, 2008.
Pickett, Marc and Barto, Andrew G. Policyblocks: An algorithm for creating useful macro-actions in
reinforcement learning. In ICML, volume 2, pp. 506–513, 2002.
Precup, Doina and Sutton, Richard S. Multi-time models for temporally abstract planning. In
Advances in Neural Information Processing Systems 10 (Proceedings of NIPS’97), 1997.
Smith, Kip and Hancock, Peter A. Situation awareness is adaptive, externally directed consciousness.
Human Factors: The Journal of the Human Factors and Ergonomics Society, 37(1):137–148, 1995.
Sutton, Richard and Barto, Andrew. Reinforcement Learning: An Introduction. MIT Press, 1998.
10


## Page 11


Sutton, Richard S, Precup, Doina, and Singh, Satinder. Between MDPs and semi-MDPs: A framework
for temporal abstraction in reinforcement learning. Artiﬁcial Intelligence, 112(1):181–211, August
1999.
Tamar, Aviv, Chow, Yinlam, Ghavamzadeh, Mohammad, and Mannor, Shie. Policy gradient for
coherent risk measures. arXiv preprint arXiv:1502.03919, 2015a.
Tamar, Aviv, Glassner, Yonatan, and Mannor, Shie. Optimizing the cvar via sampling. Conference on
Artiﬁcial Intelligence (AAAI), 2015b.
Thrun, Sebastian and Mitchell, Tom M. Lifelong robot learning. Springer, 1995.
Xu, Huan and Mannor, Shie. Probabilistic goal markov decision processes. In Proceedings of the
Twenty-Second international joint conference on Artiﬁcial Intelligence-Volume Volume Three, pp.
2046–2052. AAAI Press, 2011.
Yiannakos, A and Armatas, V. Evaluation of the goal scoring patterns in european championship in
portugal 2004. International Journal of Performance Analysis in Sport, 6(1):178–188, 2006.
11


## Page 12


A
SARiCoS Supplementary Material
A.1
Full Derivation of Theorem 1
We deﬁne the expected reward for following a policy µα,Ωas:
J(µα,Ω) =
Z
τ
P(τ|α, Ω)R(τ)dτ .
(13)
Let us group the parameters for the inter-RAS policy and the continuous RADPs into a single vector
χ = [α, Ω] ∈Rd+m·N. Taking the derivative of this objective and using the well-known likelihood
trick Peters & Schaal (2008) yields:
∇χJ(µχ)
=
∇χ
Z
τ
P(τ|χ)R(τ)dτ
(14)
=
Z
τ
∇χP(τ|χ)R(τ)dτ
(15)
=
Z
τ
P(τ|χ)∇α log P(τ|χ)R(τ)dτ ,
(16)
where P(τ|χ) = P(z0) QT
k=1 P(zk+1|zk, σk)P(σk|zk, χ) where zk ∈Z is the state at timestep k;
σk is the RAS selected at timestep k and T is the length of the trajectory. Since only P(σk|zk, χ) is
parameterized, the gradient ∇χJ(µχ) can be simpliﬁed as follows:
∇χJ(µχ)
=
Z
τ
P(τ|χ)∇χ log P(τ|χ)R(τ)dτ
(17)
=
Z
τ
P(τ|χ)∇χ log

P(z0)
T
Y
k=1
P(zk+1|zk, σk)P(σk|zk, χ)

R(τ)dτ
(18)
=
Z
τ
P(τ|χ)∇χ

log P(z0) + ΣT
k=1 log P(zk+1|zk, σk) + log P(σk|zk, χ)

R(τ)dτ
(19)
=
Z
τ
P(τ|χ)∇χ log P(σk|zk, χ)R(τ)dτ
(20)
where P(σk|zk, χ) = µα(σt|zt)µσt
Ω(yt|zt). Therefore, substituting the two-tiered policy into Equa-
tion 20 and deriving with respect to α leads to the gradient update rule:
∇αJ(µχ)
=
Z
τ
P(τ|χ)∇α log µα(σt|zt)R(τ)dτ .
If we represent µα(σt|zt) as a Gibb’s distribution which is a common policy choice in many MDPs
Sutton & Barto (1998), then we can easily estimate the gradient by sampling:
∇αJ(µχ) =
* H
X
h=0
∇α log µα(σh|zh)
H
X
j=0
γjrj
+
,
(21)
where H is the length of a trajectory; and

·

represents an average over trajectories. If we derive
Equation 20 with respect to Ωfor the RADPs, then we get the following gradient update rule:
∇ΩJ(µχ)
=
Z
τ
P(τ|χ)∇Ωlog µσt
Ω(yt|zt)R(τ)dτ .
12


## Page 13


If we represent µσt
Ω(yt|zt) as any distribution from the natural exponential family, then we can easily
estimate the gradient by samples using the following gradient update rule:
∇ΩJ(µχ) =
* H
X
h=0
∇Ωlog µσt
Ω(yt|zt)
H
X
j=0
γjrj
+
.
(22)
These derivations are summarized in Theorem 1.
Theorem 1 (Gradient Update Derivation). Suppose that we are maximizing the Policy Gradient
(PG) objective J(µα,Ω) =
R
τ Pα,Ω(τ)R(τ)dτ using risk-aware trajectories, generated by the two-
tiered skill selection policy µα(σt|xt)µσt
Ω(yt|zt), then the expectation of the gradient update rules
for the inter-skill policy parameters α ∈Rd and the RAD parameters Ω∈R|N||m| are the true
gradients and are deﬁned as (1) ∇αJ(µα,Ω) =
DPH
h=0 ∇α log µα(σh|zh) PH
j=0 γjrj
E
and (2)
∇ΩJ(µα,Ω) =
DPH
h=0 ∇Ωlog µσt
Ω(yt|zt) PH
j=0 γjrj
E
respectively. H is the trajectory length and
< · > is an average over trajectories as in standard PG.
A.2
Proof of Theorem 2: SARiCoS Convergence
Theorem 2 (SARiCoS Convergence). Suppose we are optimizing the expected return J(µΩ,α) =
R
R(τ)P(τ)dτ for any arbitrary SARiCoS policy µΩ,α where Ω∈R|N||m| and α ∈Rd are the
inter-skill and Risk Aware Distribution parameters respectively. Then, for step sizes sequences
{ak}∞
k=0, {bk}∞
k=0 that satisfy P
k ak = ∞, P
k bk = ∞, P
k a2
k < ∞, P
k b2
k < ∞and bk > ak,
the SARiCoS iterates converge a.s αk →α∗, Ωk →¯λ(α∗) as k →∞to the countable set of locally
optimal points of J(µΩ,α).
The true gradient of the two-tiered policy µΩ,α is:
∇Ω,αJ(µΩ,α) = E[Rτ∇log P(τ)]
where Rτ = Ph−1
t=0 γtrt is the discounted cumulative reward for a trajectory τ of length h; the
term P(τ) = P(x0)Πh−1
i=0 P(xi+1|xi, σi)µΩ,α(σi, yi|xi) is the probability of a trajectory for a given
policy µΩ,α(σi, yi|xi).
The estimated gradient is:
ˆ∇J(x)
=
Rτ∇log µΩ,α(σt, yt|xt)
=
Rτ∇log(µα(σt|xt)µσt
Ω(yt|xt))
We need to prove that the parameters α ∈Rd of the inter-skill policy and the risk-aware parameters
Ω∈R|N||m| converge to a locally optimal solution. Here, N is the number of skills and m is the
number of risk-aware distribution parameters for each skill. In order to do so, we ﬁrst derive the
gradient with respect to α to yield the following recursive update equations:
αk+1
=
Γα(αk + ak ˆ∇αJ(x))
=
Γα(αk + ak(Rτ∇α log µα(σt|xt)))
(1)
=
Γα(αk + ak(Rτzα
k ))
=
Γα(αk + ak(Rτzα
k −E[Rτzα
k ] + E[Rτzα
k ]))
=
Γα(αk + ak(f(α(k), Ω) + Nk+1))
(23)
where (1) zα
k = ∇α log µα(σt|xt) and Nk+1 = Rτzα
k −E[Rτzα
k ] is a zero-mean martingale
difference sequence; f(α(k), Ω) = E[Rτzα
k ] and Γα : Rd →Rd is a projection operator that projects
any αk to a compact region C = {α|gi(α) ≤0, i = 1, · · · l} ∈Rn where gi(·), i = 1, · · · l represent
13


## Page 14


the continuously differentiable constraints that project the iterates to a compact region deﬁned by
a ball with a smooth boundary. This operator ensures that the iterates remain bounded. It can be
seen by inspection that this recursion represents a noisy discretization of the Ordinary Differential
Equation (ODE) Borkar (1997):
˙α = Γα(E[Rτzα
k ])
We also derive the recursive update for the risk-aware parameters Ωas follows:
Ωk+1
=
ΓΩ(Ωk + bk ˆ∇ΩJ(x))
=
ΓΩ(Ωk + bk(Rτ∇log µσt
Ω(yt|xt))
=
ΓΩ(Ωk + bk(RτzΩ
k ))
=
ΓΩ(Ωk + bk(RτzΩ
k −E[RτzΩ
k ] + E[RτzΩ
k ]))
=
ΓΩ(Ωk + bk(g(Ω(k), α) + Mk+1)),
(24)
where Mk+1 = RτzΩ
k −E[RτzΩ
k ] is a zero mean martingale difference sequence with respect to
the σ−ﬁelds Ft = σ(Ωn, αn, Nn, Mn, n ≤t; t ≥0); g(Ω(k), α) = E[RτzΩ
k ] and ΓΩ: R|N||m| →
R|N||m| is the corresponding projection operator for Ωwhich ensures that these iterates are projected
to a compact region W as in the previous iterate update equation. We can thus represent the Ωupdate
with the following ODE:
˙Ω= ΓΩ(E[RτzΩ
k ])
Deﬁne the continuous time projection operators ˆΓΩ(v) = limδ→∞
ΓΩ(Ω+δv)−Ω
δ
and ˆΓα(p) =
limδ→∞
Γα(α+δv)−α
δ
that, given directions v and p to modify the paramaters Ωand α respectively
ensures that the iterates are projected into their compact sets C and W respectively. We can thus
deﬁne the ODEs using this continuous operator as:
˙Ω= ˆΓΩ(E[RτzΩ
k ]) .= ¯g(Ω(k), α)
˙α = ˆΓα(E[Rτzα
k ]) .= ¯f(α(k), Ω)
Assumption (A1): For each α ∈Rd, the ODE:
˙Ω(t) = ¯g(Ω(k), α)
has a globally asymptotically stable equilibrium ¯λ(α) such that ¯λ : Rd →R|N||m| is Lipschitz.
Assumption (A2): The ODE:
˙α = ¯f(α(k), ¯λ(α(k)))
has a unique global asymptotically stable equilibrium α∗.
In order to prove that these ODEs collectively converge, we need to make the following assumptions.
Assumption (A3): The functions f, g are Lipschitz continuous functions
Assumption (A4): supk ∥Ωk∥, supk ∥αk∥< ∞
Assumption (A5): P
n a(n) = P
n b(n) = ∞, P
n a(n)2 = P
n b(n)2 < ∞
Assumption (A6): For increasing σ-algebras, the martingale sequences P akNk, P bkMk < ∞a.s
Assumption (A7) For all α, Ω, the objective function J(µα,Ω) has bounded second derivatives and
the set Z of local optima of J(µα,Ω) are countable.
Given the above assumptions, the parameter Ωk →¯λ(α∗) and αk →α∗as k →∞a.s by standard
two-timescale stochastic approximation arguments Borkar (1997). That is, the iterates converge to
{¯λ(α∗), α∗|α∗∈Z} .
14


## Page 15


A.3
SARiCoS Video
A video is attached with the supplementary material showing an agent (the striker) applying the
learned risk-aware skills in a one-on-one scenario with a goalkeeper. The videos exhibit the Situational
Awareness (SA) of the agent in both a losing scenario and a winning scenario.
15

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
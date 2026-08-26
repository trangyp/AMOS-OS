---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1812.05551v3
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1812.05551v3_Exploration_Conscious_Reinforcement_Learning_Revisited

> Source: 1812.05551v3_Exploration_Conscious_Reinforcement_Learning_Revisited.pdf

> Pages: 27

---


## Page 1


Exploration Conscious Reinforcement Learning Revisited
Lior Shani * 1 Yonathan Efroni * 1 Shie Mannor 1
Abstract
The Exploration-Exploitation tradeoff arises in
Reinforcement Learning when one cannot tell if a
policy is optimal. Then, there is a constant need to
explore new actions instead of exploiting past ex-
perience. In practice, it is common to resolve the
tradeoff by using a ﬁxed exploration mechanism,
such as ϵ-greedy exploration or by adding Gaus-
sian noise, while still trying to learn an optimal
policy. In this work, we take a different approach
and study exploration-conscious criteria, that re-
sult in optimal policies with respect to the explo-
ration mechanism. Solving these criteria, as we
establish, amounts to solving a surrogate Markov
Decision Process. We continue and analyze prop-
erties of exploration-conscious optimal policies
and characterize two general approaches to solve
such criteria. Building on the approaches, we ap-
ply simple changes in existing tabular and deep
Reinforcement Learning algorithms and empiri-
cally demonstrate superior performance relatively
to their non-exploration-conscious counterparts,
both for discrete and continuous action spaces.
1. Introduction
The main goal of Reinforcement Learning (RL) (Sutton
et al., 1998) is to ﬁnd an optimal policy for a given decision
problem. A major difﬁculty arises due to the Exploration-
Exploitation tradeoff, which characterizes the omnipresent
tension between exploring new actions and exploiting the
so-far acquired knowledge. Considerable line of work has
been devoted for dealing with this tradeoff. Algorithms
that explicitly balance between exploration and exploitation
were developed for tabular RL (Kearns & Singh, 2002; Braf-
man & Tennenholtz, 2002; Jaksch et al., 2010; Osband et al.,
2013). However, generalizing these results to approximate
*Equal
contribution
1Department
of
Electrical
Engi-
neering,
Technion,
Haifa,
Israel.
Correspondence
to:
Lior
Shani
<shanlior@gmail.com>,
Yonathan
Efroni
<jonathan.efroni@gmail.com>.
Proceedings of the 36 th International Conference on Machine
Learning, Long Beach, California, PMLR 97, 2019. Copyright
2019 by the author(s).
RL, i.e, when using function approximation, remains an
open problem. On the practical side, recent works com-
bined more advanced exploration schemes in approximate
RL (e.g, Bellemare et al. (2016); Fortunato et al. (2017)),
inspired by the theory of tabular RL. Nonetheless, even in
the presence of more advanced mechanisms, ϵ-greedy explo-
ration is still applied (Bellemare et al., 2017; Dabney et al.,
2018; Osband et al., 2016). More generally, the traditional
and simpler ϵ-greedy scheme (Sutton et al., 1998; Asadi &
Littman, 2016) in discrete RL, and Gaussian action noise in
continuous RL, are still very useful and popular in practice
(Mnih et al., 2015; 2016; Silver et al., 2014; Schulman et al.,
2017; Horgan et al., 2018), especially due to their simplicity.
These types of exploration schemes share common proper-
ties. First, they all ﬁx some exploration parameter before-
hand, e.g, ϵ, the ‘inverse temperature’ β, or the action vari-
ance σ for the ϵ-greedy, soft-max and Gaussian exploration
schemes, respectively. By doing so, the balance between
exploration and exploitation is set. Second, they all explore
using a random policy, and exploit using current estimate
of the optimal policy. In this work, we follow a different
approach, when using these ﬁxed exploration schemes: ex-
ploiting by using an estimate of the optimal policy w.r.t. the
exploration mechanism.
Exploration-Consciousness is the main reason for the im-
proved performance of on-policy methods like Sarsa and
Expected-Sarsa (Van Seijen et al., 2009) over Q-learning
during training (Sutton et al., 1998)[Example 6.6: Cliff
Walking]. Imagine a simple Cliff-Walking problem: The
goal of the agent is to reach the end without falling of the
cliff, where the optimal policy is to go alongside the cliff.
While using a ﬁxed-exploration scheme, playing a near op-
timal policy which goes alongside the cliff will lead to a
signiﬁcant sub-optimal performance. This, in turn, will hurt
the acquisition of new experience needed to learn the op-
timal policy. However, learning to act optimally w.r.t. the
exploration scheme can mitigate this difﬁcultly; the agent
learns to reach the goal while keeping a safe enough distance
from the cliff.
In the past, tabular q-learning-like exploration-conscious
algorithms were suggested (John, 1994; Littman et al., 1997;
Van Seijen et al., 2009). Here we take a different approach,
and focus on exploration conscious policies. The main
arXiv:1812.05551v3  [cs.LG]  13 May 2019


## Page 2


Exploration Conscious Reinforcement Learning Revisited
contributions of this work are as follows:
• We deﬁne exploration-consciousness optimization cri-
teria, for discrete and continuous actions spaces. The
criteria are interpreted as ﬁnding an optimal policy
within a restricted set of policies. Both, we show, can
be reduced to solving a surrogate MDP. The surrogate
MDP approach, to the best of our knowledge, is a new
one, and serves us repeatedly in this work.
• We formalize a bias-error sensitivity tradeoff. The
solutions are biased w.r.t. the optimal policy, yet, are
less sensitive to approximation errors.
• We establish two fundamental approaches to practically
solve Exploration-Conscious optimization problems.
Based on these, we formulate algorithms in discrete
and continuous action spaces, and empirically test the
algorithms on the Atari and MuJoCo domains.
2. Preliminaries
Our framework is the inﬁnite-horizon discounted Markov
Decision Process (MDP). An MDP is deﬁned as the 5-tuple
(S, A, P, R, γ) (Puterman, 1994), where S is a ﬁnite state
space, A is a compact space, P ≡P(s′|s, a) is a transition
kernel, R ≡r(s, a) ∈[0, Rmax] is a bounded reward func-
tion, and γ ∈[0, 1). Let π : S →P(A) be a stationary pol-
icy, where P(A) is a probability distribution on A, and de-
note Π as the set of deterministic policies, π ∈Π : S →A.
Let vπ ∈R|S| be the value of a policy π, deﬁned in state s
as vπ(s) ≡Eπ
|s[P∞
t=0 γtr(st, at)], where at ∼π(st), and
Eπ
|s denotes expectation w.r.t. the distribution induced by
π and conditioned on the event {s0 = s}. It is known
that vπ = P∞
t=0 γt(P π)trπ = (I −γP π)−1rπ, with the
component-wise values [P π]s,s′ ≜Ea∼π[P(s′ | s, a)] and
[rπ]s ≜Ea∼π[r(s, a)]. Furthermore, the q-function of π
is given by qπ(s, a) = r(s, a) + γ P
s′ P(s′ | s, a)vπ(s′),
and represents the value of taking an action a from state s
and then using the policy π.
Usually, the goal is to ﬁnd π∗yielding the optimal value,
π∗∈arg maxπ∈Π Eπ[P∞
t=0 γtr(st, at)], and the optimal
value is v∗= vπ∗. It is known that optimal deterministic
policy always exists (Puterman, 1994). To achieve this goal
the following classical operators are deﬁned (with equalities
holding component-wise). ∀v, π :
T πv =rπ + γP πv, Tv = max
π
T πv,
(1)
G(v) = {π : T πv = Tv},
(2)
where T π is a linear operator, T is the optimal Bellman op-
erator and both T π and T are γ-contraction mappings w.r.t.
the max norm. It is known that the unique ﬁxed points of
T π and T are vπ and v∗, respectively. G(v) is the standard
set of 1-step greedy policies w.r.t. v. Furthermore, given
v∗, the set G(v∗) coincides with that of stationary optimal
policies. It is also useful to deﬁne the q-optimal Bellman
operator, which is a γ-contraction, with ﬁxed point q∗.
T qq(s, a)=r(s, a)+γ
X
s′
P(s′ | s, a) max
a′ q(s′, a′), (3)
In this work, the use of mixture policies is abundant. We
denote the α ∈[0, 1]-convex mixture of policies π1, π2 by
πα(π1, π2) ≜(1 −α)π1 + απ2. Importantly, πα(π1, π2)
can be interpreted as a stochastic policy s.t with w.p (1 −α)
the agent acts with π1 and w.p α acts with π2.
3. The α-optimal criterion
In this section, we deﬁne the notion of α-optimal policy w.r.t.
a policy, π0. We then claim that ﬁnding an α-optimal policy
can be done by solving a surrogate MDP. We continue
by deﬁning the surrogate MDP, and analyze some basic
properties of the α-optimal policy.
Let α ∈[0, 1]. We deﬁne π∗
α,π0 to be the α-optimal policy
w.r.t. π0, and is contained in the following set,
π∗
α,π0 ∈arg max
π′∈Π Eπα(π′,π0)
"X
t=0
γtr(st, at))
#
,
(4)
or, π∗
α,π0 ∈arg maxπ′ vπα(π′,π0), where at ∼πα(π′, π0)
and πα(π′, π0) is the α-convex mixture of π′ and π0, and
thus a probability distribution. For brevity, we omit the sub-
script π0, and denote the α-optimal policy by π∗
α throughout
the rest of the paper. The α-optimal value (w.r.t. π0) is
vπα(π∗
α,π0), the value of the policy πα(π∗
α, π0). In the fol-
lowing, we will see the problem is equivalent to solving a
surrogate MDP, for which an optimal deterministic policy is
known to exist. Thus, there is no loss optimizing over the
set of deterministic policies Π.
Optimization problem (4) can be viewed as optimizing over
a restricted set of policies: all policies that are a convex
combination of π0 with a ﬁxed α. Naturally, we can consider
in (4) a state-dependent α(s) as well, and some of the results
in this work will consider this scenario. In other words, π∗
α
is the best policy an agent can act with, if it plays w.p (1−α)
according to π∗
α, and w.p α according to π0, where π0 can
be any policy. The relation to the ϵ-greedy exploration setup
becomes clear when π0 is a uniform distribution on the
actions, and set α = ϵ instead of α. Then, π∗
α is optimal
w.r.t. the ϵ-greedy exploration scheme; the policy would
have the largest accumulated reward, relatively to all other
policies, when acting in an ϵ-greedy fashion w.r.t. it.
We choose to name the policy as the α- and not ϵ-optimal
to prevent confusion with other frameworks. The ϵ-optimal
policy is a notation used in the context of PAC-MDP type


## Page 3


Exploration Conscious Reinforcement Learning Revisited
of analysis (Strehl et al., 2009), and has a different meaning
than the objective in this work (4).
3.1. The α-optimal Bellman operator, α-optimal policy
and policy improvement
In the previous section, we deﬁned the α-optimal policy
and the α-optimal value, π∗
α and vπα(π∗
α,π0), respectively.
We start this section by observing that problem (4) can be
viewed as solving a surrogate MDP, denoted by Mα. We
deﬁne the Bellman operators of the surrogate MDP, and use
them to prove an important improvement property.
Deﬁne the surrogate MDP as Mα =(S, A, Pα, Rα, γ).
∀a ∈A, rα(s, a)=(1 −α)r(s, a) + αrπ0(s),
P π
α (s′ | s, a)=(1 −α)P(s′ | s, a) + αP π0(s′ | s), (5)
are its reward and dynamics, and rest of its ingredients are
similar to M. We denote the value of a policy π on Mα
by vπ
α, and the optimal value on Mα by v∗
α. The following
simple lemma relates the value of a policy π, measured on
M and Mα (see proof in Appendix D).
Lemma 1. For any policy π, vπ
α = vπα(π,π0). Thus, an
optimal policy on Mα is the α-optimal policy π∗
α (4).
The ﬁxed-policy and optimal Bellman operators of Mα are
denoted by T π
α and Tα, respectively. Again, for brevity we
omit π0 from the deﬁnitions. Notice that T π
α and Tα are γ-
contractions as being Bellman operators of a γ-discounted
MDP. The following Lemma relates T π
α and Tα to the Bell-
man operators of the original MDP, M. Furthermore, it
stresses a non-trivial relation between the α-optimal policy
π∗
α and the α-optimal value, vπα(π∗
α,π0).
Proposition 2. The following claims hold for any policy π:
1. T π
α=(1−α)T π+αT π0, with ﬁxed point vπ
α=vπα(π,π0).
2. Tα =(1−α)T+αT π0, with ﬁxed point v∗
α =vπα(π∗
α,π0).
3. An α-optimal policy is an optimal policy of Mα and is
greedy w.r.t. v∗
α, π∗
α ∈G(v∗
α) = {π′ : T π′v∗
α = Tv∗
α}.
In previous works, e.g. (Asadi & Littman, 2016), the opera-
tor (1−ϵ)T +ϵT π0 was referred to as the ϵ-greedy operator.
Lemma 2 shows this operator is Tα (with α = ϵ), the opti-
mal Bellman operator of the deﬁned surrogate MDP Mα.
This lemma leads to the following important property.
Proposition 3. Let α ∈[0, 1), β ∈[0, α], π0 be a
policy, and π∗
α be the α-optimal policy w.r.t π0.
Then,
vπ0 ≤vπα(π∗
α,π0) ≤vπβ(π∗
α,π0), with equality iff vπ0 = v∗.
The ﬁrst relation vπ0 ≤vπα(π∗
α,π0), πα(π∗
α, π0) is better
than π0, is trivial and holds by deﬁnition (4). The non-
trivial statement is the second one. It asserts that given
π∗
α, it is worthwhile to use the mixture policy πβ(π∗
α, π0)
with β < α; use π0 with smaller probability. Speciﬁcally,
better performance, compared to πα(π∗
α, π0), is assured
when using the deterministic policy π∗
α, by setting β = 0.
In section 6, we demonstrate the empirical consequences
of the improvement lemma, which, to our knowledge, has
not yet been stated. Furthermore, the improvement lemma
is unique to the deﬁned optimization criterion (4). We will
show that alternative deﬁnitions of exploration conscious
criteria does not necessarily have this property. Moreover,
one can use Proposition 3 to generalize the notion of the
1-step greedy policy (2), as was done in Efroni et al. (2018)
with multiple-step greedy improvement. We leave studying
this generalization and its Policy Iteration scheme for future
work, and focus on solving (4) a single time.
3.2. Performance bounds in the presence of
approximations
We now consider an approximate setting and quantify a bias
- error sensitivity tradeoff in πα(ˆπ∗
α, π0), where ˆπ∗
α is an
approximated α-optimal policy. We formalize an intuitive
argument; as α increases the bias relatively to the optimal
policy increases. Yet, the sensitivity to errors decreases,
since the agent uses π0 w.p. α regardless of errors.
Deﬁnition 1. Let v∗be the optimal value of an MDP, M.
We deﬁne L(s) ≜v∗(s)−T π0v∗(s) ≥0, to be the Lipschitz
constant w.r.t. π0 of the MDP at state s. We further deﬁne
the upper bound on the Lipschitz constant L ≜maxs L(s).
Deﬁnition 1 deﬁnes the ‘Lipschitz’ property of the optimal
value, v∗. Intuitively, L(s) quantiﬁes a degree of ‘smooth-
ness’ of the optimal value. A small value of L(s) indicates
that if one acts according to π0 once and then continue play-
ing the optimal policy from state s, a great loss will not
occur. Large values of L(s) indicate that using π0 from
state s leads to an irreparable outcome (e.g, falling off a
cliff). The following theorem formalizes a bias-error sensi-
tivity tradeoff. As α increases, the bias increases, while the
sensitivity to errors decreases (see proof in Appendix H).
Theorem 4. Let α ∈[0, 1]. Assume ˆv∗
α is an approximate
α-optimal value s.t ∥v∗
α −ˆv∗
α∥= δ for some δ ≥0. Let
ˆπ∗
α be the greedy policy w.r.t. ˆv∗
α, ˆπ∗
α ∈G(ˆv∗
α). Then, the
performance relatively to the optimal policy is bounded by,



v∗−vπα(ˆπ∗
α,π0)


 ≤
αL
1 −γ
| {z }
Bias
+ 2(1 −α)γδ
1 −γ
|
{z
}
Sensitivity
.
When the bias of the α-optimal value relatively to the opti-
mal one is small, solving (4) does not lead to a great loss
relatively to the optimal performance. The bias can be
bounded by the ‘Lipschitz’ property L of the MDP. For a


## Page 4


Exploration Conscious Reinforcement Learning Revisited
state dependent α(s), the bias bound changes to be depen-
dent on maxs α(s)L(s). This highlights the importance of
prior knowledge when using (4). Choosing π0 (possibly
state-wise) s.t. maxs α(s)L(s) is small, allows to use a
bigger α, while the bias is small. The sensitivity term up-
per bounds the performance of πα(ˆπ∗
α, π0) relatively to the
α-optimal value, and is less sensitive to errors as α increase.
The bias term is derived by using the structure of Mα,
and is not a direct application of the Simulation Lemma
(Kearns & Singh, 2002; Strehl et al., 2009); applying it
would lead to a bias of αRmax
(1−γ)2 . For the sensitivity term, we
generalize (Bertsekas & Tsitsiklis, 1995)[Proposition 6.1]
(see Appendix G). There, a (1 −α) factor does not exists.
4. Exploration-Conscious Continuous Control
The α-greedy approach from Section 3 relies on an explo-
ration mechanism which is ﬁxed beforehand: π0 and α
are ﬁxed, and an optimal policy w.r.t. them is being calcu-
lated (4). However, in continuous control RL algorithms,
such as DDPG and PPO (Lillicrap et al., 2015; Schulman
et al., 2017), different approach is used. Usually, a policy
is being learned, and the exploration noise is injected by
perturbing the policy, e.g., by adding to it a Gaussian noise.
We start this section by deﬁning an exploration-conscious
optimality criterion that captures such perturbation for the
simple case of Gaussian noise. Then, results from Section 3
are adapted to the newly deﬁned criterion, while highlight-
ing commonalities and differences relatively to (4). As in
Section 3, we deﬁne an appropriate surrogate MDP and we
show it can be solved by the usual machinery of Bellman
operators. Unlike Section 3, we show that improvement
when decreasing the stochasticity does not generally hold.
Finally, we prove a similar bias-error sensitivity result: As σ
grows, the bias increases, but the sensitivity term decreases.
Instead of restricting the set of policies to the one deﬁned
in (4), we restrict our set of policies to be the set of Gaussian
policies with a ﬁxed σ2 variance. Formally, we wish to ﬁnd
the optimal deterministic policy µ∗
σ : S →A in this set,
µ∗
σ ∈arg max
µ∈Π Eπµ,σ
" ∞
X
t=0
γtr(st, at)
#
,
(6)
where πµ,σ(· | s) = N(µ(s), σ2), is a Gaussian policy with
mean µ(s) and a ﬁxed variance σ2. We name µ∗
σ and π∗
σ
as the mean and σ-optimal policy, respectively. As in (4),
we show in the following that solving (6) is equivalent for
solving a surrogate MDP. Thus, optimal policy can always
be found in the deterministic class of policies Π; mixture of
Gaussians would not lead to a better performance in (6).
Similarly to (5), we deﬁne a surrogate MDP Mσ w.r.t. to
the Gaussian noise and relate it to values of Gaussian poli-
cies on the original MDP M. Then, we characterize its
Bellman operators and thus establish it can be solved us-
ing Dynamic Programming. Deﬁne the surrogate MDP as
Mσ =(S, A, Pσ, Rσ, γ). For every a ∈A,
rσ(s, a)=
Z
A
N(a′; a, σ)r(s, a′)da′,
Pσ(s′ | s, a)=
Z
A
N(a′; a, σ)P(s′ | s, a′)da′,
(7)
are its reward and dynamics, and denote a value of a policy
on Mσ by vµ
σ. The following results correspond to Lemma
1 and Proposition 2 for the class of Gaussian policies.
Lemma 5. For any policy π, vπ
µ,σ = vµ
σ. Thus, an optimal
policy on Mσ is the mean optimal policy µ∗
σ (6).
Proposition 6. Let π be a mixture of Gaussian policies.
Then, the following holds:
1. T µ
σ = Eπ∼πµ,σ T π, with ﬁxed point vµ
σ =vπµ,σ.
2. Tσ =max
µ∈˜
A
Eπ∼πµ,σ T π, with ﬁxed point v∗
σ =vπµ∗σ,σ.
3. The mean σ-optimal policy µ∗
σ is an optimal policy of
Mσ and, µ∗
σ ∈{µ : T πµ,σv∗
σ = maxµ T πµ,σv∗
σ}.
Surprisingly, given a σ-optimal policy mean µ∗
σ, an im-
provement is not assured when lowering the stochasticity by
decreasing σ in πµ∗σ,σ. This comes in contrast to Proposition
3 and highlights its uniqueness (proof in Appendix J).
Proposition 7. Let 0 ≤σ′ < σ and let µ∗
σ be the mean σ-
optimal policy. There exists an MDP s.t vπµ∗,σ ≰vπµ∗,σ′.
Deﬁnition 2. Let M be a continuous action space
MDP. Assume that exists Lr, Lp
≥
0, s.t.
∀s
∈
S, ∀a1, a2 ∈A, |r(s, a1) −r(s, a2)| ≤Lr ∥a1 −a2∥1
and ∥p(·|s, a1) −p(·|s, a2)∥T V
≤Lp ∥a1 −a2∥1.
The
Lipschitz constant of M is L ≜(1 −γ)Lr + γLpRmax.
The following theorem quantiﬁes a bias-error sensitivity
tradeoff in σ, similarly to Theorem 4 (see Appendix K).
Theorem 8. Let M be an MDP with Lipschitz constant L
and let σ ∈R|A|
+ . Let v∗
σ be the σ-optimal value of Mσ. Let
ˆv∗
σ be an approximation of v∗
σ s.t. ∥v∗
σ −ˆv∗
σ∥= δ for δ ≥0.
Let µ∗
σ, ˆµ∗
σ ∈RA be the greedy mean policy w.r.t. v∗
σ and
ˆv∗
σ respectively. Let ∥·∥σ−2 is the σ−2-weighted euclidean
norm. Then,



v∗−vˆπ∗
σ



≤
L ∥σ∥1
2 (1 −γ)2
|
{z
}
Bias
+ γδ min{ 1
2 ∥µ∗
σ −ˆµ∗
σ∥σ−2 , 2}
1 −γ
|
{z
}
Sensitivity
.
5. Algorithms
In this section, we offer two fundamental approaches to
solve exploration conscious criteria using sample-based al-
gorithms: the Expected and Surrogate approaches. For both,


## Page 5


Exploration Conscious Reinforcement Learning Revisited
we formulate converging, q-learning-like, algorithms. Next,
by adapting DDPG, we show the two approaches can be
used in exploration-conscious continuous control as well.
Consider any ﬁxed exploration scheme. Generally, these
schemes operate in two stages: (i) Choose a greedy action,
achosen. (ii) Based on achosen and some randomness genera-
tor, choose an action to be applied on the environment, aenv.
E.g., for ϵ-greedy exploration, w.p. 1−α the agent acts with
achosen, otherwise, with a random uniform policy. While in
RL the common update rules use aenv, the saved experience
is (s, aenv, r, s′), in the following we motivate the use of
achosen, and view the data as (s, achosen, aenv, r, s′).
The two approaches characterized in the following are based
on two, inequivalent, ways to deﬁne the q-function. For
the Expected approach the q-function is deﬁned as usual:
qπ(s, a) represents the value obtained when taking an ac-
tion a = aenv and then acting with π, meaning a is the
action chosen in step (ii). Alternatively, for the Surrogate
approach, the q-function is deﬁned on the ‘Surrogate’ MDP,
i.e., the exploration is viewed as stochasticity of the envi-
ronment. Then, qπ
α(s, a) is the value obtained when a is the
action of step (i), i.e., choosing action a = achosen.
5.1. Exploration Conscious Q-Learning
We focus on solving the α-optimal policy (4), and formulate
q-learning-like algorithms using the two aforementioned
approaches. The Expected α-optimal q-function is,
qπα(π∗
α,π0)(s, a)≜r(s, a)+γ
X
s′
P(s′ | s, a)v∗
α(s′)
(8)
Indeed, qπα(π∗
α,π0) is the usually deﬁned q-function of the
policy πα(π∗
α, π0) on an MDP M.
Here, the action a
represents the actual performed action, aenv. By relating
qπα(π∗
α,π0) to v∗
α it can be easily veriﬁed that qπα(π∗
α,π0)
satisﬁes the ﬁxed point equation (see Appendix L),
qπα(π∗
α,π0)(s, a) =
r(s, a)+γ(1−α)
X
s′
P(s′ |s, a) max
a′ qπα(π∗
α,π0)(s′, a′)
+γα
X
s′,a′
P(s′ |s, a)π0(a′ |s′)qπα(π∗
α,π0)(s′, a′).
(9)
Alternatively, consider the optimal q-function of the surro-
gate MDP Mα (5). It satisﬁes the ﬁxed-point equation
q∗
α(s, a)≜rα(s, a)+γ
X
s′
Pα(s′ | s, a) max
a′ q∗
α(s′, a′).
The following lemma formalizes the relation between the
two q-functions, and shows they are related by a function of
the state, and not of the action.
Lemma 9. q∗
α(s, a) = (1 −α)qπα(π∗
α,π0)(s, a) + f(s).
The α-optimal policy π∗
α is also an optimal policy of Mα
(Lemma 1). Thus, it is greedy w.r.t. q∗
α, the optimal q of Mα.
By Proposition 2.3 it is also greedy w.r.t. qπα(π∗
α,π0), i.e.,
π∗
α(s) ∈arg max
a′ q∗
α(s, a′) = arg max
a′ qπα(π∗
α,π0)(s, a′).
Lemma 9 describes this fact by different means; the two q-
functions are related by a function of the state and, thus, the
greedy action w.r.t. each is equal. Furthermore, it stresses
the fact that the two q-function are not equal.
Before describing the algorithms, we deﬁne the following
notation for any q(s, a),
v(s) = max
a′ q(s, a′), vπ(s) =
X
a′
π(a′ | s)q(s, a′).
We now describe the Expected α-Q-learning algorithm (see
Algorithm 1), also given in (John, 1994; Littman et al.,
1997), and re-interpret it in light of the previous discussion.
The ﬁxed point equation (9), leads us to deﬁne the operator
T Eq
α
for which qπα(π∗
α,π0) = T Eq
α qπα(π∗
α,π0). Expected α-
Q-learning (Alg. 1) is a Stochastic Approximation (SA) alg.
based on the operator T Eq
α . Given a sample of the form
(s, achosen, aenv, r, s′), it updates q(s, aenv) by
(1−η)q(s, aenv)+η (rt+γ((1−α)v(st+1)+αvπ0(st+1)))
(10)
Algorithm 1 Expected α-Q-Learning
Initialize: α ∈[0, 1], π0, q, learning rate ηt.
for t = 0, 1, ... do
achosen ←arg maxa qt(st, a)
Xt ∼Bernoulli(1 −α)
aenv =
(
achosen, if Xt = 1
a ∼π0(· | s), if Xt = 0
rt, st+1 ←ACT(aenv)
yt ←rt + γ(1 −α)vt(st+1) + γαvπ0
t (st+1)
q(st, aenv) ←(1 −ηt) q(st, aenv) + ηtyt
end for
return: π ∈arg maxa q(·, a)
Its convergence proof is standard and follows by showing
T Eq
α
is a γ-contraction and using (Bertsekas & Tsitsiklis,
1995)[Proposition 4.4] (see proof in Appendix L.1).
We now turn to describe an alternative algorithm, which
operates on the surrogate MDP, Mα, and converges to q∗
α.
Naively, given a sample (s, achosen, r, s′), regular q-learning
on Mα can be used by updating q(s, achosen) as,
(1−ηt)q(s, achosen)+ηt(rt+γv(st+1)),
(11)
Yet, this approach does not utilize a meaningful knowledge;
when the exploration policy π0 is played, i.e., when Xt = 0,
the sample (rt, st+1) can be used to update all the action


## Page 6


Exploration Conscious Reinforcement Learning Revisited
entries from the current state. These entries are also affected
by the policy π0. In fact, we cannot prove the convergence of
the naive update based on current techniques; if the greedy
action is repeatedly chosen, ‘inﬁnitely often’ visit in all
(s, a) pairs cannot be guaranteed.
Algorithm 2 Surrogate α-Q-Learning
Initialize: α ∈[0, 1], π0, qα, q, learning rate ηt.
for t = 0, 1, ... do
achosen ←arg maxa q(st, a)
Xt ∼Bernoulli(1 −α)
aenv =
(
achosen, if Xt = 1
a ∼π0(· | s), if Xt = 0
rt, st+1 ←ACT(aenv)
for ¯a ∈A do
y¯a
t =
(
rt + γvα(st+1), ¯a = achosen
Xtq(st, ¯a)+(1−Xt) (rt+γvα(st+1)), o.w
qα(st, ¯a) ←(1 −η) qα(st, ¯a) + ηy¯a
t
end for
yt ←rt + γ(1 −α)v(st+1) + γαvπ0(st+1)
q(st, aenv) ←(1 −ηt)q(st, aenv) + ηtyt
end for
return π ∈arg maxa qα(·, a)
This reasoning leads us to formulate Surrogate α-Q-learning
(see Algorithm 2). The Surrogate α-Q-learning updates two
q-functions, q and qα. The ﬁrst, q, has the same update
as in Expected α-Q-learning, and thus converges (w.p 1)
to qπα(π∗
α,π0). The second, qα, updates the chosen greedy
action using equation (11), when the exploration policy is
not played (Xt = 1). By bootstrapping on q, the algorithm
updates all other actions when the exploration policy π0 is
played (Xt = 0). Using (Singh et al., 2000)[Lemma 1], the
convergence of Surrogate α-Q-learning to (qπα(π∗
α,π0), q∗
α)
is established (see proof in Appendix L.2). Interestingly,
and unlike other q-learning algorithms (e.g, Expected α-Q-
learning, Q-learning, etc.), Surrogate α-Q-learning updates
the entire action set given a single sample. For completness,
we state the convergence result for both algorithms.
Theorem 10. Consider the processes described in Alg. 1, 2.
Assume {ηt}∞
t=0 satisﬁes ∀s ∈S, ∀a ∈A, P∞
t=0 ηt = ∞,
and P∞
t=0 η2
t < ∞, where ηt ≡ηt(st = s, aenv,t = a).
Then, for both 1, 2 the sequence {qn}∞
n=0 converges w.p. 1
to qπα(π∗
α,π0), and for 2, {qα,n}∞
n=0 converges w.p. 1 to q∗
α.
5.2. Continuous Control
Building on the two approaches for solving Exploration
Conscious criteria, we suggest two techniques to ﬁnd an
optimal Gaussian policy (6) using gradient based Deep RL
(DRL) algorithms, and speciﬁcally, DDPG (Lillicrap et al.,
2015). Nonetheless, the techniques are generalizable to
other actor-critic, DRL algorithms (Schulman et al., 2017).
Assume we wish to ﬁnd an optimal Gaussian policy by
parameterizing its mean µ(φ). Nachum et al. (2018)[Eq.
13] showed the gradient of the value w.r.t. φ is similar to
Silver et al. (2014),
∇φvπµ,σ =
Z
S
∂aq
ππµ,σ
σ
(s, a)∇φµθ(s)dρπµ,σ(s),
(12)
where qµ
σ(s, a) = rσ(s, a)+γ
R
S pσ(s′ | s, a)vπµ,σ(s′)ds′,
is the q-function of the surrogate MDP. In light of previ-
ous section, we interpret qµ
σ as the q-function of the surro-
gate MDP’s Mσ (7). Furthermore, we have the following
relation between the surrogate and expected q-functions,
qµ
σ(s, a) =
R
a′∈A N(a′ | a, σ)qπµ,σ(s, a′)da′, from which
it is easy to verify that (see Appendix L.3),
∇uqπµ,σ
σ
(s, b)=
Z
A
N(b | a, σ)∇bqπµ,σ(s, b)db.
(13)
Thus, we can update the actor in two inequivalent ways, by
using gradients on the surrogate MDP’s q-function (12), or
by using gradients of the expected q-function (13).
The updates of the critic, qµ
σ or qπµ,σ, can be done using the
same notion that led to the two forms of updates in (11)-(10).
When using Gaussian noise, one performs the two stages
deﬁned in Section 5, where achosen is the output of the
actor µ(s), and aenv ∼N(achosen, σ). Then, the sample
(s, achosen, aenv, r, s′) is obtained by interacting with the
environment. Based on the the ﬁxed policy TD-error deﬁned
in (11), we deﬁne the following loss function, for learning
qµ
σ, q-function of the ﬁxed policy µ over Mσ,
 qθ
σ(s, achosen) −r −γqθ−
σ (s′, µφ−(s′))
2 .
On the other hand, we can deﬁne a loss function derived
from the ﬁxed-policy TD-error deﬁned in (10), for learning
qπµ,σ, the q-function of the Gaussian policy with mean and
variance µ, σ2 over M,
 qθ(s, aenv)−r −γ
Z
A
N(b | µφ−(s′), s′)qθ−(s′, b)db
2.
6. Experiments
In this section, we test the theory and algorithms 1 suggested
in this work. In all experiments we used γ = 0.99. The
tested DRL algorithms in this section (See Appendix B)
are simple variations of DDQN (Van Hasselt et al., 2016)
and DDPG (Lillicrap et al., 2015), without any parame-
ter tuning, and based on Section 5. For example, for the
surrogate approach in both DDQN and DDPG we merely
save (s, achosen, r, s′) instead of (s, aenv, r, s′) in the replay
buffer (see Section 5 for deﬁnitions of aenv, achosen).
1Implementation of the proposed algorithms can be found in
https://github.com/shanlior/ExplorationConsciousRL.


## Page 7


Exploration Conscious Reinforcement Learning Revisited
2
4
Iteration
1e5
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4
Es
U[v * (s)
v
t(s)]
Q
E- Q, Mixture
B- Q, Mixture
E- Q, Greedy
B- Q, Greedy
S
S
2
4
Iteration
1e5
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4
Es
U[v * (s)
v
t(s)]
Q
E- Q, Mixture
B- Q, Mixture
E- Q, Greedy
B- Q, Greedy
S
S
Figure 1. T-Cliff-Walking for the expected (E) and surrogate (S)
approaches. (Left) α=0.3. (Right) α(s) from prior knowledge.
We observe a signiﬁcant improved empirical performance,
both in training and evaluation for both the surrogate
and expected approaches relatively to the baseline perfor-
mance. The improved training performance is predictable;
the learned policy is optimal w.r.t. the noise which is be-
ing played. In large portion of the results, the exploration-
conscious criteria leads to better performance in evaluation.
6.1. Exploration Consciousness with Prior Knowledge
We use an adaptation of the Cliff-Walking maze (Sutton
et al., 1998) we term T-Cliff-Walking (see Appendix C).
The agent starts at the bottom-left side of a maze, and needs
to get to the bottom-right side goal state with value +1.
If the agent falls off the cliff, the episode terminates with
reward −1. When the agent visits any of the ﬁrst three steps
on top of the cliff, it gets a reward of 0.01 · (1 −γ).
We tested Expected α-Q-learning, Surrogate α-Q-learning,
and compared their performance to Q-learning in the pres-
ence of ϵ-greedy exploration. Figure 1 stresses the typical
behaviour of the α-optimality criterion. It is easier to approx-
imate πα(π∗
α, π0) than the optimal policy. Further, by being
exploration-consciousness, the value of the approximated
policy improves faster using the α-optimal algorithms; it
learns faster which regions to avoid. As Proposition 4 sug-
gests, the value of the learned policy is biased w.r.t v∗. Next,
as suggested by Proposition 3, acting greedily w.r.t. the
approximated value attains better performance. Such im-
provement is not guaranteed while the value had not yet
converged to v∗
α. However, the empirical results suggest
that if the agent performs well over the mixture policy, it is
worth using the greedy policy.
We show that it is possible to incorporate prior knowledge
to decrease the bias caused by being Exploration-Conscious.
The T-Cliff-Walking example demands high exploration,
α = ϵ = 0.3, because of the bottleneck state between the
two sides of the maze. The α-optimal policy in such case
is to stay at the left part of the maze. We used the prior
knowledge that L(s) close to the barrier is high. The knowl-
edge was injected through the choice of α, i.e., we chose a
Table 1. Train and Test rewards for the Atari 2600 environment,
with 90% conﬁdence interval
Game
DDQN
Expected
α-DDQN
Surrogate
α-DDQN
Train
Breakout
350±4
356±6
357±4
FishingDer
-45±9
-35±27
-8±8
Frostbite
1191±171
794±158
1908±162
Qbert
13221±565
13431±178
14240±225
Riverraid
8602±205
8811±645
11476±79
Test
Breakout
402±14
390±5
392±5
FishingDer
-37±15
-19±34
-3±19
Frostbite
1720±191
1638±292
2686±278
Qbert
15627±497
15780±206
16082±338
Riverraid
9049±443
9491±802
12846±241
state-wise exploration scheme with α(s) = ϵ(s) = 0.1 in
the passage and the two states around it, and α(s) = 0.3
elsewhere, for all three algorithms. The results in Figure 1
suggests that using prior knowledge to set α(s), can increase
the performance by reducing the bias. In contrast, such prior
knowledge does not help the baseline q-learning.
6.2. Exploration Consciousness in Atari
We tested the α-optimal criterion in the more complex func-
tion approximation setting (see Appendix Alg. 3, 4). We
used ﬁve Atari 2600 games (5) from the ALE (Bellemare
et al., 2013). We chose games that resemble the Cliff Walk-
ing scenario, where the wrong choice of action can lead to a
sudden termination of the episode. Thus, being unaware of
the exploration strategy can lead to poor training results. We
used the same deep neural network as in DQN (Mnih et al.,
2015), using the openAI Baselines implementation (Dhari-
wal et al., 2017), without any parameter tuning, except for
the update equations. We chose to use the Double-DQN
variant of DQN (Van Hasselt et al., 2016) for simplicity and
generality. Nonetheless, changing the optimality criterion is
orthogonal to any of the suggested add-ons to DQN (Hessel
et al., 2017). We used α = ϵ = 0.01 in the train phase, and
ϵ = 0.001 in the evaluation phase. For the surrogate version,
we used a naive implementation based on equation (11).
Table 1 shows that our method improves upon using the op-
timal criterion. That is, while bias exists, the algorithm still
converges to a better policy. This result holds both on the ex-
ploratory training regime and the evaluation regime. Again,
acting greedy w.r.t. the approximation of the α-optimal
policy proved beneﬁcial: The evaluation phase results sur-
passes the train phase results as shown in the table, and the
training ﬁgures in Appendix (2). The evaluation is usually
done with an ϵ = 0.001 > 0. Proposition 3 put formal
grounds for using smaller ϵ in the evaluation phase than in
the training phase; improvement is assured. Being accurate


## Page 8


Exploration Conscious Reinforcement Learning Revisited
Table 2. Train and Test rewards for the MuJoCo environment.
Game
DDPG
Expected
σ-DDPG
Surrogate
σ-DDPG
Train
Ant
809±47
1013±49
993±110
HalfCheetah
2255±804
2634±828
3848±248
Hopper
1864±139
1866±132
2566±155
Humanoid
1281±142
1416±155
1703±272
InPendulum
694±109
882±33
998±3
Walker
1722±170
2144±145
2587±214
Test
Ant
1611±120
1924±126
1754±184
HalfCheetah
2729±936
3147±986
4579±298
Hopper
3099±113
3071±50
3037±78
Humanoid
1688±223
1994±389
2154±408
InPendulum
999±2
1000±0
1000±0
Walker
3031±298
3315±147
3501±240
is extremely important in most Atari games, so Exploration-
Consciousness can also hurt the performance. Still, one can
use prior knowledge to overcome this obstacle.
6.3. Exploration Consciousness in MuJoCo
We tested the Expected σ-DDPG (5) and Surrogate σ-
DDPG (6) on continuous control tasks from the MuJoCo
environment (Todorov et al., 2012). We used the OpenAI
implementation of DDPG as the baseline, where we only
changed the update equations to match our proposed algo-
rithms. We used the default hyper-parameters, and inde-
pendent Gaussian noise with σ = 0.2, for all tasks and
algorithms. The results in Table 2 were averaged over 10
different seeds. The performance of the σ-optimal variants
superseded the baseline DDPG, for most of the training and
test results. Interestingly, although improvement is not guar-
anteed (Proposition 7), the σ-optimal policy improved when
using µφ deterministically, i.e., in the test phase. This sug-
gests that improvement can be expected on certain scenarios,
although that generally it is not guaranteed. We also found
that the training process was faster using the σ-optimal algo-
rithms, as can be seen in the learning curves in Appendix 3.
Interestingly, again, the surrogate approach proved superior.
7. Relation to existing work
Lately, several works have tackled the exploration problem
for deep RL. In some, like Bootstrapped-DQN (see appendix
[D.1] in (Osband et al., 2016)), the authors still employ an
ϵ-greedy mechanism on top of their methods. Moreover,
methods like Distributional-DQN (Bellemare et al., 2017;
Dabney et al., 2018) and the state-of-the-art Ape-X DQN
(Horgan et al., 2018), still uses ϵ-greedy and Gaussian noise,
for discrete and continuous actions, respectively. Hence, all
the above works are applicable for the α-optimal criterion
by using the simple techniques described in Section 5.
Existing on-policy methods produce variants of Exploration-
Consciousness. In TRPO and A3C (Schulman et al., 2015;
Mnih et al., 2016), the exploration is implicitly injected
into the agent policy through entropy regularization, and
the agent improves upon the value of the explorative policy.
Simple derivation shows the α-greedy and the Gaussian
approaches are both equivalent to regularizing the entropy to
be higher than a certain value by setting α or σ appropriately.
Expected α-Q-learning highlights a relation to algorithms
analysed in (John, 1994; Littman et al., 1997) and to
Expected-Sarsa (ES) (Van Seijen et al., 2009). The focus of
(John, 1994; Littman et al., 1997) is exploration-conscious
q-based methods. In ES, when setting the ‘estimation policy’
(Van Seijen et al., 2009) to be π = (1 −αt)πG + αtπ0, we
get similar updating equations as in lines 1-1, and similarly
to (John, 1994; Littman et al., 1997). However, in ES αt
decays to zero, and the optimal policy is obtained in the inﬁ-
nite time limit. In (Nachum et al., 2018), the authors offer a
gradient based mechanism for updating the mean and vari-
ance of the actor. Here, we offer and analyze the approach
of setting αt and σt to a constant value. This would be of
interest especially when a ‘good’ mechanism for decaying
αt and σt lacks; the decay mechanism is usually chosen by
trial-and-error, and is not clear how it should be set.
Lastly, (4) and (6) can be understood as deﬁning a ‘surro-
gate problem’, rather than ﬁnding an optimal policy. In this
sense, it offers an alternative approach to biasing the prob-
lem by lowering the discount-factor, i.e., solve a surrogate
MDP with ¯γ < γ (Petrik & Scherrer, 2009; Jiang et al.,
2015). Interestingly, the introduced bias when solving (4) is
proportional to a local property of v∗, L(s), that can be esti-
mated using prior-knowledge on the MDP, where solving an
MDP with ¯γ introduces a bias proportional to a non-local
term, which is harder to estimate. More importantly, the per-
formance of an α-optimal policy π∗
α is assured to improve
when tested on the original MDP M (Proposition 3), while
the performance of an optimal policy in an MDP with ¯γ
might decline when tested on M with γ-discounting.
8. Summary
In this paper, we revisited the notion of an agent being
conscious to an exploration process. To our view, this notion
did not receive the proper attention, though it is implicitly
and repeatedly used.
We started by formally deﬁning optimal policy w.r.t. an
exploration mechanism (4), (6). This expanded the view
on exploration-conscious q-learning (John, 1994; Littman
et al., 1997) to a more general one, and lead us to derive new
algorithms, as well as re-interpreting existing ones (Van Sei-
jen et al., 2009). We formulated the surrogate MDP notion,


## Page 9


Exploration Conscious Reinforcement Learning Revisited
which helped us to establish that exploration-conscious cri-
teria can be solved by Dynamic Programming, or, more
generally, by an MDP solver. From the practical side, based
on the theory, we tested DRL algorithms – by simply modi-
fying existing ones, with no further hyper-parameter tuning
– and empirically showed their superiority.
Although a bias - error sensitivity tradeoff was formulated,
we did not prove (4), (6) are easier to solve than an MDP.
We believe proving whether the claim is true is of interest.
Furthermore, analyzing more exploration-conscious criteria,
e.g., exploration-conscious w.r.t. Ornstein-Uhlenbeck noise,
is of interest, as well as deﬁning a uniﬁed framework for
exploration-conscious criteria.
Acknowledgments
We would like to thank Chen Tessler, Nadav Merlis and
Tom Zahavy for helpful discussions.
References
Asadi, K. and Littman, M. L.
An alternative softmax
operator for reinforcement learning.
arXiv preprint
arXiv:1612.05628, 2016.
Bellemare, M., Srinivasan, S., Ostrovski, G., Schaul, T.,
Saxton, D., and Munos, R. Unifying count-based explo-
ration and intrinsic motivation. In Advances in Neural
Information Processing Systems, pp. 1471–1479, 2016.
Bellemare, M. G., Naddaf, Y., Veness, J., and Bowling, M.
The arcade learning environment: An evaluation plat-
form for general agents. Journal of Artiﬁcial Intelligence
Research, 47:253–279, 2013.
Bellemare, M. G., Dabney, W., and Munos, R. A distri-
butional perspective on reinforcement learning. arXiv
preprint arXiv:1707.06887, 2017.
Bertsekas, D. P. and Tsitsiklis, J. N. Neuro-dynamic pro-
gramming: an overview. In Decision and Control, 1995.,
Proceedings of the 34th IEEE Conference on, volume 1,
pp. 560–564. IEEE, 1995.
Brafman, R. I. and Tennenholtz, M. R-max-a general poly-
nomial time algorithm for near-optimal reinforcement
learning. Journal of Machine Learning Research, 3(Oct):
213–231, 2002.
Dabney, W., Rowland, M., Bellemare, M. G., and Munos,
R. Distributional reinforcement learning with quantile re-
gression. In Thirty-Second AAAI Conference on Artiﬁcial
Intelligence, 2018.
Dhariwal, P., Hesse, C., Klimov, O., Nichol, A., Plap-
pert, M., Radford, A., Schulman, J., Sidor, S., and
Wu, Y. Openai baselines. https://github.com/
openai/baselines, 2017.
Efroni, Y., Dalal, G., Scherrer, B., and Mannor, S. Beyond
the one-step greedy approach in reinforcement learning.
In Proceedings of the 35th International Conference on
Machine Learning, pp. 1386–1395, 2018.
Fortunato, M., Azar, M. G., Piot, B., Menick, J., Osband, I.,
Graves, A., Mnih, V., Munos, R., Hassabis, D., Pietquin,
O., et al. Noisy networks for exploration. arXiv preprint
arXiv:1706.10295, 2017.
Hessel, M., Modayil, J., Van Hasselt, H., Schaul, T., Ostro-
vski, G., Dabney, W., Horgan, D., Piot, B., Azar, M., and
Silver, D. Rainbow: Combining improvements in deep
reinforcement learning. arXiv preprint arXiv:1710.02298,
2017.
Horgan, D., Quan, J., Budden, D., Barth-Maron, G., Hessel,
M., Van Hasselt, H., and Silver, D. Distributed priori-
tized experience replay. arXiv preprint arXiv:1803.00933,
2018.
Jaksch, T., Ortner, R., and Auer, P. Near-optimal regret
bounds for reinforcement learning. Journal of Machine
Learning Research, 11(Apr):1563–1600, 2010.
Jiang, N., Kulesza, A., Singh, S., and Lewis, R. The depen-
dence of effective planning horizon on model accuracy.
In Proceedings of the 2015 International Conference on
Autonomous Agents and Multiagent Systems, pp. 1181–
1189. International Foundation for Autonomous Agents
and Multiagent Systems, 2015.
John, G. H. When the best move isn’t optimal: Q-learning
with exploration. Citeseer, 1994.
Kearns, M. and Singh, S. Near-optimal reinforcement learn-
ing in polynomial time. Machine learning, 49(2-3):209–
232, 2002.
Lillicrap, T. P., Hunt, J. J., Pritzel, A., Heess, N., Erez,
T., Tassa, Y., Silver, D., and Wierstra, D. Continuous
control with deep reinforcement learning. arXiv preprint
arXiv:1509.02971, 2015.
Littman, M. L. et al. Generalized markov decision processes:
Dynamic-programming and reinforcement-learning algo-
rithms. 1997.
Mnih, V., Kavukcuoglu, K., Silver, D., Rusu, A. A., Veness,
J., Bellemare, M. G., Graves, A., Riedmiller, M., Fidje-
land, A. K., Ostrovski, G., et al. Human-level control
through deep reinforcement learning. Nature, 518(7540):
529, 2015.


## Page 10


Exploration Conscious Reinforcement Learning Revisited
Mnih, V., Badia, A. P., Mirza, M., Graves, A., Lillicrap,
T., Harley, T., Silver, D., and Kavukcuoglu, K. Asyn-
chronous methods for deep reinforcement learning. In
International Conference on Machine Learning, pp. 1928–
1937, 2016.
Nachum, O., Norouzi, M., Tucker, G., and Schuurmans, D.
Smoothed action value functions for learning gaussian
policies. arXiv preprint arXiv:1803.02348, 2018.
Osband, I., Russo, D., and Van Roy, B. (more) efﬁcient
reinforcement learning via posterior sampling. In Ad-
vances in Neural Information Processing Systems, pp.
3003–3011, 2013.
Osband, I., Blundell, C., Pritzel, A., and Van Roy, B. Deep
exploration via bootstrapped dqn. In Advances in neural
information processing systems, pp. 4026–4034, 2016.
Petrik, M. and Scherrer, B. Biasing approximate dynamic
programming with a lower discount factor. In Advances
in neural information processing systems, pp. 1265–1272,
2009.
Puterman, M. L. Markov decision processes. j. Wiley and
Sons, 1994.
Schulman, J., Levine, S., Abbeel, P., Jordan, M., and Moritz,
P. Trust region policy optimization. In International
Conference on Machine Learning, pp. 1889–1897, 2015.
Schulman, J., Wolski, F., Dhariwal, P., Radford, A., and
Klimov, O. Proximal policy optimization algorithms.
arXiv preprint arXiv:1707.06347, 2017.
Silver, D., Lever, G., Heess, N., Degris, T., Wierstra, D., and
Riedmiller, M. Deterministic policy gradient algorithms.
In ICML, 2014.
Singh, S., Jaakkola, T., Littman, M. L., and Szepesv´ari,
C.
Convergence results for single-step on-policy
reinforcement-learning algorithms. Machine learning,
38(3):287–308, 2000.
Strehl, A. L., Li, L., and Littman, M. L. Reinforcement
learning in ﬁnite mdps: Pac analysis. Journal of Machine
Learning Research, 10(Nov):2413–2444, 2009.
Sutton, R. S., Barto, A. G., et al. Reinforcement learning:
An introduction. MIT press, 1998.
Todorov, E., Erez, T., and Tassa, Y. Mujoco: A physics
engine for model-based control. In Intelligent Robots
and Systems (IROS), 2012 IEEE/RSJ International Con-
ference on, pp. 5026–5033. IEEE, 2012.
Van Hasselt, H., Guez, A., and Silver, D. Deep reinforce-
ment learning with double q-learning. In AAAI, volume 2,
pp. 5. Phoenix, AZ, 2016.
Van Seijen, H., Van Hasselt, H., Whiteson, S., and Wiering,
M. A theoretical and empirical analysis of expected sarsa.
In Adaptive Dynamic Programming and Reinforcement
Learning, 2009. ADPRL’09. IEEE Symposium on, pp.
177–184. IEEE, 2009.


## Page 11


Exploration Conscious Reinforcement Learning Revisited
A. Training graphs for the Atari and MuJoCo experiments
0
100
200
#Frames
0
100
200
300
400
Reward
0
1
2
#Frames
1e8
0
100
200
300
400
Reward
0
100
200
#Frames
100
80
60
40
20
0
Reward
0
1
2
#Frames
1e8
100
80
60
40
20
0
Reward
0
100
200
#Frames
0
500
1000
1500
2000
Reward
0
1
2
#Frames
1e8
0
500
1000
1500
2000
2500
Reward
0
100
200
#Frames
0
2500
5000
7500
10000
12500
Reward
0
1
2
#Frames
1e8
0
5000
10000
15000
Reward
0
100
200
#Frames
2000
4000
6000
8000
10000
Reward
0
1
2
#Frames
1e8
2000
4000
6000
8000
10000
12000
Reward
DDQN
Expected -DDQN
Surrogate -DDQN
Figure 2. Simulation results for the Atari 2600 environment: From up to bottom: Breakout, Fishing Derby, Frostbite, Qbert and Riverraid.
(Left) Training. (Right) Test.


## Page 12


Exploration Conscious Reinforcement Learning Revisited
0
1
2
#Steps
1e6
0
200
400
600
800
Reward
0
1
2
#Steps
1e6
0
500
1000
1500
Reward
0
1
2
#Steps
1e6
0
1000
2000
3000
4000
Reward
0
1
2
#Steps
1e6
0
1000
2000
3000
4000
Reward
0
1
2
#Steps
1e6
0
500
1000
1500
2000
Reward
0
1
2
#Steps
1e6
0
500
1000
1500
2000
2500
Reward
0
1
2
#Steps
1e6
250
500
750
1000
1250
1500
Reward
0
1
2
#Steps
1e6
500
1000
1500
2000
Reward
0
1
2
#Steps
1e6
0
200
400
600
800
1000
Reward
0
1
2
#Steps
1e6
0
200
400
600
800
1000
Reward
0
1
2
#Steps
1e6
0
500
1000
1500
2000
2500
Reward
0
1
2
#Steps
1e6
0
1000
2000
3000
Reward
DDPG 
Expected -DDPG 
Surrogate -DDPG 
Figure 3. Simulation results for the MuJoCo environment: From up to bottom: Ant, HalfCheetah, Hopper, Humanoid, InvertedPendulum
and Walker2d. (Left) Training. (Right) Test.


## Page 13


Exploration Conscious Reinforcement Learning Revisited
B. Deep RL Exploration Conscious algorithms
The algorithms in this section are the adjusted DDQN (Van Hasselt et al., 2016) and DDPG (Lillicrap et al., 2015) to solve
the α-optimal and σ-optimal policies, respectively. For the surrogate approach the change is merely the gathered data;
the action achosen is saved and not aenv. For the expected approach, the expectation is calculated by an explicit averaging
Algorithm 3 or by simple sampling technique Algorithm 5.
Algorithm 3 Expected α-DDQN
Initialize: Network parameters θ, θ−←θ
Replay buffer R, Target network update time N −
for episode= 1, M do
for t = 1, T do do
achosen ←arg maxa q(st, a|θ)
Xt ∼Bernoulli(1 −α)
aenv =
(
achosen, if Xt = 1
a ∼π0(· | s), if Xt = 0
rt, st+1 ←ACT(aenv)
Store (st, aenv, rt, st+1) in R
Sample N tuples (si, ai
env, ri, s′
i) from R
ai ←arg maxa q(s′
i, a|θ)
vi ←(1 −α)q(s′
i, ai|θ−) + αvπ0(s′
i|θ−)
yi ←ri + γvi
Minimize L = 1
N
P
i
 yi −q(si, ai
env|θ
2
Update θ−←θ every N −steps
end for
end for
return π ∈arg maxa q(·, a)
Algorithm 4 Surrogate α-DDQN
Initialize: Network parameters θ, θ−←θ
Replay buffer R, Target network update time N −
for episode= 1, M do
for t = 1, T do do
achosen ←arg maxa qα(st, a|θ)
Xt ∼Bernoulli(1 −α)
aenv =
(
achosen, if Xt = 1
a ∼π0(· | s), if Xt = 0
rt, st+1 ←ACT(aenv)
Store (st, achosen, rt, st+1) in R
Sample N tuples (si, ai
chosen, ri, s′
i) from R
ai ←arg maxa qα(s′
i, a|θ)
yi ←ri + γqα(s′
i, ai|θ−)
Minimize L = 1
N
P
i
 yi −qα(si, ai
chosen|θ
2
Update θ−←θ every N −steps
end for
end for
return π ∈arg maxa qα(·, a)
Algorithm 5 Expected σ-DDPG
Initialize: Critic and Actor networks q(s, a|θ), µ(s|φ)
Target networks weights: θ−←θ and φ−←φ
Replay buffer R, Target network update time N −
for episode= 1, M do
Initialize random markovian exploration process N
Receive initial observation state s1
for t = 1, T do do
aenv ←µ(st|φ) + Nt
rt, st+1 ←ACT(at)
Store (st, aenv, rt, st+1, Nt) in R
Sample N transitions (si, ai, ri, s′
i, Ni) from R
Sample D1 noise terms nj given Ni
yi ←ri + γ 1
D1
P
j q(s′
i, µ(s′
i) + nj|φ−)|θ−)
Critic Loss: L = 1
N
P
i (yi −q(si, ai|θ)2
Sample D2 noise terms nj given Ni
Approximate gradient policy gradient:
∇πqπ(si) ≈
1
D2
P
j ∇aq(si, a|θ)

a=µ(si)+nj
Update actor using policy gradient:
∇φV ≈1
N
P
i ∇πqπ(si)∇φµ(si|φ)
Update target networks every N −steps
end for
end for
return µ(·|φ)
Algorithm 6 Surrogate σ-DDPG
Initialize: Critic and Actor networks qσ(s, a|θ), µ(s|φ)
Target networks weights: θ−←θ and φ−←φ
Replay buffer R, Target network update time N −
for episode= 1, M do
Initialize random markovian exploration process N
Receive initial observation state s1
for t = 1, T do do
achosen ←µ(st|φ)
aenv ←achosen + Nt
rt, st+1 ←ACT(aenv)
Store (st, achosen, rt, st+1) in R
Sample N transitions (si, ai, ri, s′
i) from R
yi ←ri + γqσ(s′
i, µ(s′
i|φ−))|θ−)
Critic Loss: L = 1
N
P
i (yi −qσ(si, ai|θ)2
Update actor using policy gradient:
∇φV = 1
N
P
i ∇aqσ(si, a|θ)

a=µ(si)∇φµ(si|φ)
Update target networks every N −steps
end for
end for
return µ(·|φ)


## Page 14


Exploration Conscious Reinforcement Learning Revisited
Figure 4. T-Cliff-Walking: The bright gray area is an impenetrable barrier. The cliff is colored in dark gray. The green states are with a
small reward of 0.01 · (1 −γ).
Figure 5. Atari games. From left to right: Breakout, Fishing Derby, Frostbite, Qbert, Riverraid.
C. Experimental details
In this section we will discuss some technicalities that are related to the experiments done in this paper.
C.1. Cliff Walking
We used the T-Cliff-Walking scenario in Figure 4: The size of the cliff is (h, w) = (4, 12). We added small reward of
0.01rmax (green states) in order to create some small bias between the optimal and the α-optimal policy. The maximal
reward in this example is rmax = 1 −γ. We ﬁrst checked to see that that alpha = ϵ = 0.1 performed bad. Then, we raised
the ϵ value. The bottleneck passage between to sides of the maze, creates a scenario where high exploration is needed. We
performed 2,000 runs for each of the algorithms. Finally, the test error was evaluated with high precision using the ﬁxed
value iteration procedure.
D. Proof of Lemma 1
For any policy π the following equalities hold.
vπ
α = (I −γP π
α )−1rπ
α
= (I −γ((1 −α)P π + αP π0))−1((1 −α)rπ + αrπ0)
= (I −γP πα(π,π0))−1rπα(π,π0) = vπα(π,π0).
E. Proof of Proposition 2
Proof. Let v ∈R|S| and consider the surrogate MDP, Mα. Its ﬁxed policy Bellman operator (see (1)) is given by:
T π
α v = rπ
α + γP π
α v
= (1 −α)(rπ + γP πv) + α(rπ0 + γP π0v)
= (1 −α)T πv + αT π0v.
(14)
The second relation is by plugging P π
α , rπ
α from (5), and rearranging. The ﬁxed point of T π
α is vπ
α, the value of π measured
in Mα. Due to Lemma 1, vπ
α = vπα(π,π0).


## Page 15


Exploration Conscious Reinforcement Learning Revisited
The optimal Bellman operator of Mα is (see (1)):
Tαv = max
π
T π
α v
= max
π (1 −α)T πv + αT π0v
= (1 −α) max
π
T πv + αT π0v = (1 −α)T + αT π0,
(15)
where the second relation holds by (14). The ﬁxed point of Tα is, by construction, v∗
α, the optimal value on Mα. Moreover,
v∗
α is the optimal value of a policy on Mα. By Lemma 1, the policy that achieves the optimal value on Mα achieves the
α-optimal value, maxπ′ vπα(π′,π0) = vπα(π∗
α,π0). Thus, this policy is the α-optimal policy, π∗
α, and v∗
α = vπ∗
α = vπα(π∗
α,π0).
Since Mα is an MDP, its optimal policy is in the greedy set w.r.t. v∗
α (see (2)). Thus,
π∗
α ∈{π : T π
α v∗
α = Tαv∗
α}
= {π : (1 −α)T πv∗
α + αT π0v∗
α = (1 −α)Tv∗
α + αT π0v∗
α}
= {π : T πv∗
α = Tv∗
α} = G(v∗
α).
F. Proof of Theorem 3
For completness we give two useful lemmas that are in use. The ﬁrst one has several instances in the literature.
Lemma 11. Let vπ and vπ′ be the correspondsing values of the policies π and π′. Then,
vπ′ −vπ = (I −γP π′)−1(T π′vπ −vπ)
(16)
Proof.
vπ′ −vπ = (I −γP π′)−1rπ′ −vπ
= (I −γP π′)−1(rπ′ + γP π′vπ −vπ)
= (I −γP π′)−1(T π′vπ −vπ).
The following Lemma has several instrances in previous literature:
Lemma 12. Let π be any policy and π1−step ∈G(vπ). Then,
vπ ≤vπα(π1−step,π),
where the inequality is strict at least in one-component if π ̸= π∗, if π is not the optimal policy.
Proof.
vπα(π1−step,π) −vπ = (I −γP πα(π1−step,π))−1(T πα(π1−step,π)vπ −vπ),
where the ﬁrst relation holds due to Lemma 11. See that,
T πα(π1−step,π)vπ −vπ = (1 −α)T π1−stepvπ + αT πvπ −vπ
= (1 −α)T π1−stepvπ + αvπ −vπ
= (1 −α) (T π1−stepvπ −vπ) = (1 −α) (Tvπ −vπ)
Plugging it into (F) yields,
vπα(π1−step,π) −vπ = (1 −α)(I −γP πα(π1−step,π))−1(Tvπ −vπ).
We have that P πα(π1−step,π))−1 ≥0 since it is a γ-discounted weighted sum of stochastic matrices. Furthermore,
vπ = T πvπ ≤Tvπ,
where the last inequality is strict at least in one component if vπ ̸= v∗, i.e, if π ̸= π∗.


## Page 16


Exploration Conscious Reinforcement Learning Revisited
s0
s1
s2
a1, 0
a2, 0
a1, 0.8
a2, 0
a1, 1
Figure 6. Counter exmple for an MDP with no monotonous improvement for the α-optimal criterion 3.
We now prove the result. The ﬁrst relation holds almost by construction. We have that,
vπα(π∗
α,π0) = max
π′ vπα(π′,π0) ≥vπα(π0,π0) = vπ0
(17)
where the ﬁrst relation is due to the deﬁnition of the α-optimal value (4), the second relation holds by deﬁnition and the
third relation holds since
πα(π0, π0) = (1 −ϵ)π0 + ϵπ0 = π0.
As long as π0 ̸= π∗, the policy π1−step ∈G(vπ0) acheives strict improvement in (17). Meaning,
vπα(π1−step,π0) ≥vπ0.
This means that the improvement in (17) is strict as long as π0 ̸= π∗.If π0 is not optimal we have that
vπ0 ≤vπα(π1−step,π0) ≤vπα(π∗
α,π0).
The ﬁrst relation is strict due to Lemma 12, and the second relation holds by the deﬁnition of the α-optimal policy.
We now prove the second relation of the lemma. Let β ∈[0, α]. Then,
vπβ(π∗
α,π0) −v∗
α = (I −γP πβ(π∗
α,π0))−1(T πβ(π∗
α,π0)v∗
α −v∗
α).
We have that,
T πβ(π∗
α,π0)v∗
α −v∗
α = T πβ(π∗
α,π0)v∗
α −Tαv∗
α
= (1 −β)T π∗
αv∗
α + βT π0v∗
α −(1 −α)Tv∗
α −αT π0v∗
α
= (α −β) (Tv∗
α −T π0v∗
α) ,
where in the last relation we used T π∗
αv∗
α = Tv∗
α (see Proposition 2). Plugging into (F) yields,
vπβ(π∗
α,π0) −v∗
α = (α −β)(I −γP πβ(π∗
α,π0))−1 (Tv∗
α −T π0v∗
α) .
We have that (I −γP πβ(π∗
α,π0))−1 ≥0 since it is a γ-discounted sum of stochastic matrices, and Tv∗
α ≥T π0v∗
α with
equality if and only if π0 is optimal; if and only if π0 is optimal v∗
α = v∗due to the ﬁrst part of this proof.
F.1. Counter example for monotonous improvement for the α-optimal criterion
In this section, we give a counter example that proves that the improvement in Proposition 3 is not monotonous w.r.t
β. Let the MDP given in Figure 6 be a γ-discounted MDP for some γ ∈(0, 1). Let π0 be a deterministic policy which
always chooses action a2. For α = 0.25, It is easy to verify that v∗
α(s1) = 0.8 and v∗
α(s2) = (1 −α) = 0.75. Now,
q∗
α(s0, a1) = γ(1 −α)v∗
α(s1) + αv∗
α(s2) = 0.7875γ, and q∗
α(s0, a2) = 0.75γ. Thus, the α-optimal policy on s0 is to
choose a1, and v∗
α(s0) = 0.7875γ.
Now, we consider acting according to the mixture policy πβ(π∗
α, π0) for some β < α. For the greedy policy, i.e. β = 0,
we get that vπ0(π∗
α,π0) = vπ∗
α = 0.8γ. For β = 0.1, we get that vπ0.1(π∗
α,π0) = γ(0.9 · 0.8 + 0.1 · (0.9 · 1)) = 0.81γ.
To conclude, as the lemma 3 suggests, we get improvement for both inspected β, i.e. v∗
α < vπ∗
α and v∗
α < vπ0.1(π∗
α,π0).
However, the improvement does not increase monotonically as we decrease β, as vπ∗
α = 0.8γ < 0.81γ = vπ0.1(π∗
α,π0).


## Page 17


Exploration Conscious Reinforcement Learning Revisited
G. Generalization of (Bertsekas & Tsitsiklis, 1995)[Proposition 6.1] for any policy class
In this section, we prove a generalization of (Bertsekas & Tsitsiklis, 1995)[Proposition 6.1] for any class of policies.
Proposition 13. Let σ a set of ﬁxed parameters of some distribution class. Assume ˆv∗
σ is an approximate σ-optimal value
s.t. ∥v∗
σ −ˆv∗
σ∥= δ for some δ > 0. Then,



v∗
σ −vˆπ∗
σ



 ≤γδ∥π∗
σ −ˆπ∗
σ∥T V
1 −γ
.
Proof.
v∗
σ −vˆπ∗
σ
σ
= Tσv∗
σ −T ˆπ∗
σvˆπ∗
σ = Tσv∗
σ −Tσˆv∗
σ + Tσˆv∗
σ −T ˆπ∗
σvˆπ∗
σ
= Tσv∗
σ −Tσˆv∗
σ + T ˆπ∗
σv∗
σ −T ˆπ∗
σv∗
σ + T ˆπ∗
σ ˆv∗
σ −T ˆπ∗
σ ˆv∗
σ + Tσˆv∗
σ −T ˆπ∗
σvˆπ∗
σ
= (Tσv∗
σ −Tσˆv∗
σ) +

T ˆπ∗
σ ˆv∗
σ −T ˆπ∗
σv∗
σ

+

T ˆπ∗
σv∗
σ −T ˆπ∗
σ ˆv∗
σ + Tσˆv∗
σ −T ˆπ∗
σvˆπ∗
σ

(a)
≤

T π∗
σv∗
σ −T π∗
σ ˆv∗
σ

+

T ˆπ∗
σ ˆv∗
σ −T ˆπ∗
σv∗
σ

+

T ˆπ∗
σv∗
σ −T ˆπ∗
σ ˆv∗
σ + Tσˆv∗
σ −T ˆπ∗
σvˆπ∗
σ

(b)
= γP π∗
σ (v∗
σ −ˆv∗
σ) −γP ˆπ∗
σ (v∗
σ −ˆv∗
σ) +

T ˆπ∗
σv∗
σ −Tσˆv∗
σ + Tσˆv∗
σ −T ˆπ∗
σvˆπ∗
σ

= γ

P π∗
σ −P ˆπ∗
σ

(v∗
σ −ˆv∗
σ) +

T ˆπ∗
σv∗
σ −T ˆπ∗
σvˆπ∗
σ

Where (a) is due to the fact that for any v and π, T π
σ ≤Tσv, and (b) is due to the deﬁnition of the σ-greedy operator.
Taking the max-norm,
v∗
σ (s) −vˆπ∗
σ (s)
 ≤γ


P π∗
σ −P ˆπ∗
σ

(v∗
σ −ˆv∗
σ)

(s)
 +


T ˆπ∗
σv∗
σ −T ˆπ∗
σvˆπ∗
σ

(s)

≤γ

X
s′,a
p (s|s′, a) (π∗
σ (a|s′) −ˆπ∗
σ (a|s′)) (v∗
σ (s′) −ˆv∗
σ (s′))

+ γ



v∗
σ −vˆπ∗
σ



 =
≤γmaxs′

X
a
(π∗
σ (a|s′) −ˆπ∗
σ (a|s′)) (v∗
σ (s′) −ˆv∗
σ (s′))
 + γ



v∗
σ −vˆπ∗
σ



≤γ ∥v∗
σ −ˆv∗
σ∥∥π∗
σ −ˆπ∗
σ∥T V + γ



v∗
σ −vˆπ∗
σ



Where the ∥·∥T V accounts for the maximal total-variation distance over all states. Finally,



v∗
σ −vˆπ∗
σ



 ≤γδ∥π∗
σ −ˆπ∗
σ∥T V
1 −γ
.
Finally, this bound is a generalization of (Bertsekas & Tsitsiklis, 1995)[Proposition 6.1], for any class of distributions.
Notice that the total variation distance is not bigger than 2, which is the case of two different deterministic policies. This
leads back to the familiar bound.
H. Proof of Theorem 4: Bias-Error Sensitivity in the α-greedy case
In order to prove the theorem, we ﬁrst prove the following two propositions 14,15. Then, we plug the results in the following
triangle inequality:



v∗−vπα(ˆπ∗
α,π0)


 ≤∥v∗−v∗
α∥+



v∗
α −vπα(ˆπ∗
α,π0)


Proposition 14. Let ∀s ∈S, α(s) ∈[0, 1], be a state-dependent function. Let π∗
α be the α-optimal policy, and L(s) the
MDP Lipschitz constant, both relatively to π0. Deﬁne B(α) ≜maxs α(s)L(s). The following bounds hold,



v∗−vπ∗
α



 ≤



v∗−vπα(πg,π0)


 ≤B(α)
1 −γ ,
If ∀s ∈S, α(s) = α ∈[0, 1] then B(α) = αL (see Deﬁnition 1). Furthermore, this bound is tight.


## Page 18


Exploration Conscious Reinforcement Learning Revisited
Proof. We have that for any s ∈S,
v∗−v∗
α(s) = (Tv∗−Tαv∗)(s) + (Tαv∗−Tαv∗
α)(s)
≤∥Tv∗−Tαv∗∥+ ∥Tαv∗−Tαv∗
α∥
≤∥Tv∗−Tαv∗∥+ γ ∥v∗−v∗
α∥,
in the last relation we used the fact that Tα is a γ contraction in the max-norm. Moreover, we have that for any s ∈S,
Tv∗(s) −Tαv∗(s) = Tv∗−(1 −α(s))Tv∗(s) −α(s)T π0v∗(s)
= α(s) (Tv∗(s) −T π0v∗(s))
(18)
= α(s) (v∗(s) −T π0v∗(s)) = α(s)L(s).
In the third relation we used the fact that Tv∗= v∗component-wise, since v∗is the ﬁxed-point of T. Thus, we see that,
∥Tv∗−Tαv∗∥= max
s
α(s)L(s) = B(α),
and that L(s) ≥0 since v∗(s) −T π0v∗(s) ≥0. By taking the max-norm on (14), which is possible since it is positive, and
simple algebraic manipulation we conclude the result.
We can continue and bound the above to get the bound in (14), which is less tight. We have that,
|Tv∗−T π0v∗|(s) = |T π∗v∗−Tαv∗|(s)
(19)
≤
X
a
|π∗(a | s) −π0(a | s)| ×
r(s, a) + γ
X
s′
P(s′ | s, a)v∗(s′)
 ,
where the ﬁrst relation is by using the triangle inequality, and then use |a · b| ≤|a| · |b|. We further have that,
r(s, a) + γ
X
s′
P(s′ | s, a)v∗(s′)
 ≤Rmax
1 −γ .
Thus, continuing from (14), we can further bound (19),
|Tv∗−T π0v∗|(s) ≤Rmax
1 −γ
X
a
|π∗(a | s) −π0(a | s)|.
Thus,
α(s)(Tv∗−T π0v∗)(s) ≤max α(s) ∥π∗−π0∥T V (s)Rmax
1 −γ
where ∥π∗−π0∥T V (s) = P
a |π∗(a | s) −π0(a | s)|, is the total variation of π∗and π0 in state s.
Finally, the bound is proved tight by an example which attains it as described below:
For the MDP described in ﬁgure 7, it is easy to see that for the uniform π0:
v∗−vπ∗
α =
1
1 −γ −1 −α/2
1 −γ
= α/2
1 −γ
Next:
α
1 −γ





v∗(s) −
X
a
π0(a|s)q∗(s, a)





 =
α
1 −γ




1
1 −γ −1/2
1 −γ −γ/2
1 −γ




 = α/2
1 −γ
Proposition 15. Let α ∈[0, 1]. Assume ˆv∗
α is an approximate α-optimal value s.t ∥v∗
α −ˆv∗
α∥= δ for some δ ≥0. Let πg
be the greedy policy w.r.t. v, ˆπ∗
α ∈G(ˆv∗
α). Then



v∗
α −vπα(ˆπ∗
α,π0)


 ≤2(1 −α)γδ
1 −γ
Furthermore, there exists some δ0 > 0 such that if δ < δ0, then ˆπ∗
α = π∗
α, and this bound is tight.


## Page 19


Exploration Conscious Reinforcement Learning Revisited
s0
a0
0
a1
1
Figure 7. One State MDP that attains the bound in Proposition 14
s0
s1
a0
−γδ
a1 γδ
a1
γδ
a0
−γδ
Figure 8. Two State MDP that attains the bound in Proposition 15 over a uniform π0.
Proof. First, notice that for any two α-greedy policies, πα(π1, π0), πα(π2, π0),
∥πα(π1, π0) −πα(π2, π0)∥T V = ∥(1 −α)π1 + απ0 −(1 −α)π2 −απ0∥T V
= (1 −α) ∥π1 −π2∥T V
≤2(1 −α)
Where the last transition is due to the fact that for the total- variation between distributions is always smaller than 2, which
is the case of two different deterministic policies. Plugging in the result in Proposition 13, we get the required bound.
Finally, we prove that this bound is tight (see that different MDP then in (Bertsekas & Tsitsiklis, 1995) is used). Observe at
the MDP described in Figure 8. The policy π∗
α is to always choose action a1. Hence,
v∗
α =
∞
X
n=0
γn h
γδ(1 −α
2 ) −γδ α
2
i
= γδ(1 −α)
1 −γ
Now, given value estimation ˆv∗
α, such that ˆv∗
α(s0) = δ, ˆv∗
α(s1) = −δ, taking always a1 is an α-greedy policy with respect to
ˆv∗
α:
(1 −α
2 )(γδ + γˆv∗
α(s1)) + α
2 (−γδ + γˆv∗
α(s0)) = 0 = (1 −α
2 )(−γδ + γˆv∗
α(s0)) + α
2 (γδ + γˆv∗
α(s1))
Hence,
vπα(ˆπ∗
α,π0) =
∞
X
n=0
γn h
−γδ(1 −α
2 ) + γδ α
2
i
= γδ(α −1)
1 −γ
Simple arithmetic show that this MDP attains the upper bound.
I. Proof of Proposition 6
In this section, we will prove Proposition 6. First, we deﬁne the sufﬁcient conditions for an MDP on which Proposition 6 is
true:
Deﬁnition 3. An MDP M = (S, A, P, R, γ) is a bounded continuous MDP if the following holds:
1. A is a metric space, s.t. A = R|A|
2. ∀s ∈S and a ∈A, the state-wise reward function is positive, continuous, and bounded r(s, a)


## Page 20


Exploration Conscious Reinforcement Learning Revisited
3. ∀s ∈S, the state-wise reward function r(s, a) is continuous in a ∈A
4. ∀s, s′ ∈S, the transition probability density function p(s′|s, a) is continuous in a ∈A.
Furthermore, we assume S is ﬁnite. Yet, we believe it is possible to extend our result to continuous space as well. This we
leave for future work.
Next, we state again the deﬁnition the optimal policy with respect to the Gaussian noise:
µ∗
σ ∈arg max
µ∈˜
A
Eπµ,σ
" ∞
X
t=0
γtr(st, at)
#
,
(20)
Where the optimization is restricted to ˜
A, a compact subset of A.
We are now state again our main theorem regarding the σ-optimal optimization criterion:
Lemma 16. Let M = (S, A, P, R, γ) be a bounded continuous MDP (see (3)). Let N(µ, σ) be the Gaussian measure with
mean µ ∈Rn and σ ≥0 and let ˜
A ⊂A be a compact metric space. Then, the following claims hold:
1. T µ
σ = Eπ∼πµ,σ T π, with ﬁxed point vµ
σ=vπµ,σ.
2. Tσ =maxµ∈˜
AEπ∼πµ,σ T π, with ﬁxed point v∗
σ=vπµ∗σ,σ.
3. A σ-optimal policy is an optimal policy of Mσ and is Gaussian w.r.t. v∗
α, µ∗
σ ∈Nσ(v∗
σ) = {µ : T πµ,σv∗
σ =
maxµ T πµ,σv∗
σ}.
Proof. We deﬁne the surrogate MDP Mσ to have the following reward and dynamics,
rσ(s, a) =
Z
N(a′ | a, σ)r(s, a′)da′,
pσ(s′ | s, a) =
Z
N(a′ | a, σ)p(s′ | s, a′)da′.
Notice that
X
s′
pσ(s′ | s, a) =
Z
N(a′ | a, σ)
X
s′
p(s′ | s, a′)da′
=
Z
N(a′ | a, σ)da′ = 1.
First, we show that the surrogate MDP Mσ is equivalent to a Gaussian policy on M. More speciﬁcally, we show that the
ﬁxed policy bellman operator for a deterministic policy on Mσ is equivalent to the bellman operator of a Gaussian policy on
M. Then, we show similar relation for the bellman optimality operator.
Lemma 17. The following claims hold:
1. The ﬁxed-policy bellman operator on Mσ, T µ
σ and T πµ,σ are equivalent.
2. The bellman operator on Mσ, Tσ and maxµ T πµ,σ are equivalent.
Proof.
T µ
σ v = rµ
σ + γpµ
σv
= Eπ∼πµ,σrπ + Eπ∼πµ,σpπv
= Eπ∼πµ,σrπ + γpπv
= Eπ∼πµ,σT π
The second relation holds directly from taking the maximum over both sides.


## Page 21


Exploration Conscious Reinforcement Learning Revisited
By Lemma 17, the connection between operators is stated for both (1) and (2). By the deﬁnition of Mσ, for any Gaussian
policy with mean µ, πµ,σ, it holds that vµ
σ = vµ,σ.
Next, we prove the second relation. Again, we start by proving the following Lemma:
Lemma 18. There exists a σ-optimal Gaussian policy
Proof. The functions rσ(s, a) and pσ(s′|s, a) are deﬁned as the expectation of r(s, ·) and p(s′|s, ·) on the Gaussian
measure with mean a respectively. For every s, s′ ∈S, deﬁne the integrand g(a, µ) = φ(a|µ, σ)f(s′, s, a), where
f(s′, s, a) represents r(s, a) or p(s′|s, a). The derivative of φµ(a|µ, σ) exists ∀µ ∈R|A|. Thus, (a) gµ(a, µ) exists
∀µ ∈R|A|. Next, For all s, s′ ∈S, r(s, a) and p(s′|s, a) are continuous and bounded in a. ∀µ, the Gaussian function
is lebesgue-integrable function of a. Thus, (b) ∀µ, g(a, µ) is a Lebesgue-integrable function of a. Now, there exist
c > 0, such that, |φµ| ≤c|a −µ|φ(a|µ, σ). Furthermore, f(s′, s, a) is bounded. Hence, there exists C > 0, such
that, |gµ(a, µ)| ≤C|a −µ|φ(a|µ, σ) ≜h(a, µ). Then, ∀µ, we can take an open ball of radius r, Br(µ). Deﬁne,
t(a) = maxx∈Br(µ) h(a, x). t is integrable for every a ∈A by construction. In other words, (c) there is an integrable
function t : A →R such that |gµ(a, µ)| ≤t(a) for all µ ∈Br(µ).
Finally, From (a),(b) and (c), by the Dominated convergence theorem, Leibniz integral rule applies, which means that
rσ(s, a) and pσ(s′|s, a) are differentiable in a ∈A, and thus continuous in a ∈A, for every s, s′ ∈S.
Now, (1) let Mσ be the surrogate MDP, and assume the state space is discrete. (2) For all s, s′ ∈S, rσ(s, a) and pσ(s′|s, a)
are continuous in a. (3) By the deﬁnition of the optimality criterion, we consider only actions a ∈A. Hence, the action
space of Mσ is compact.
Then, by theorem [6.2.10] in (Puterman, 1994), there exist an optimal deterministic policy for the surrogate MDP, Mσ.
By the deﬁnition of the Mσ and Lemma 17, a deterministic policy µ in Mσ is equivalent to a Gaussian policy πµ,σ on
M. Denote the optimal deterministic policy on the surrogate MDP as µ∗
σ. Thus, the policy πµ∗σ,σ is an σ-optimal Gaussian
policy on M.
Finally, we show that solving the surrogate MDP is equivalent to solving (20) Tσ is the greedy bellman operator on the
surrogate MDP. Therefore, it is a γ-contraction. Thus, (a) by the Banach ﬁxed point theorem and Theorem [6.2.2] in
(Puterman, 1994), v∗
σ is the unique solution to the optimality equation, Tσv∗
σ = v∗
σ. (b) By Lemma 18, there exists a
deterministic optimal policy. Combining (a) and (b), we get that the greedy policy w.r.t. v∗
σ, µ∗
σ, is an optimal policy in the
surrogate MDP. By transforming back to the original MDP we get that π∗
σ = πµ∗σ,σ:
µ∗
σ ∈{µ : T µ
σ v∗
σ = Tσv∗
σ}
= {µ : Eπ∼πµ,σT πv∗
σ = max
µ
Eπ∼πµ,σT πv∗
σ}
= Nσ(v∗
σ).
I.1. MDP with bounded action space
In this section we explain how to apply the σ-optimal criterion to an MDP with bounded action space. Let M be a bounded
continuous MDP with a compact action-space A. Proposition 6 demands the action space to be deﬁned on the support of the
Gaussian measure. Thus, we need to formalize how the Gaussian noise which is deﬁned over R|A| operates on the bounded
action set A. Intuitively, we choose to project any action chosen outside the action set a /∈A onto the action set boundary.
Formally, the noise operates on the extended MDP, Mext, as deﬁned here.
Deﬁnition 4. For a bounded continuous MDP M = (S, A, P, R, γ), we deﬁne the extended MDP, Mext, with action space
Aext = R|A|, such that:
1. Rext(s, a) = R(s, PA(a)), for all s ∈S.
2. Pext(s, a) = P(s, PA(a)), for all s, s′ ∈S


## Page 22


Exploration Conscious Reinforcement Learning Revisited
Figure 9. Illustration of a typical case where there is no improvement: (Blue) The state-action value function as a function of the action
taken. (Orange) The σ-optimal policy is with µ∗
σ = 0 due to the smoothing effect of the Gaussian policy. (Black) A deterministic policy
around the µ∗
σ. It can be easily seen that decreasing the noise degrades the performance of the agent.
Where, PA(a) is the orthogonal projection of the action a onto the set A
The MDP Mext is a bounded continuous MDP, with action space R|A|. Therefore, by 6, it is possible to ﬁnd the optimal
policy w.r.t. the σ-optimal criterion, over any bounded action space. Finally, most naturally, one can apply the criterion to
the original action space A.
J. No Improvement in Continuous Control
We give here the proof, the improvement is not always guaranteed in the continuous case.
Proposition 19. Let 0 ≤σ′ < σ and let µ∗be the σ-optimal policy. There exists an MDP such that vπµ∗,σ > vπµ∗,σ′.
Decreasing the stochasticity can hurt the performance of the agent, and improvement is not guaranteed.
Proof. Let M be a one-state MDP, with the following reward: r(u) = 1
2
1
√πe−(u−1)2 + 1
2
1
√πe−(u+1)2. The expected
reward under a Gaussian policy with µ and σ = 1 is: rπ = 1
2
1
√
3πe−(µ−1)2/3 + 1
2
1
√
3πe−(µ+1)2/3. It is easy to calculate that
the maximum of rπ is attained when µ = 0 and its value lower bounded by 0.23. Hence, the σ-optimal policy with σ = 1 is
π(u|s) = N(0, 1). However, acting greedily w.r.t the mean of the σ-optimal, i.e., acting always with u = 0 can be upper
bounded by 0.21. Thus, rπ∗
σ > rπµσ ,0
An illustration of such a case is given in ﬁgure J.
While in the general case there is no improvement, it is easy to verify that a sufﬁcient condition for improvement is that the
state-wise variance of the qπ∗
σ w.r.t. every smaller noise level, ˜σ < σ, is less than the noise level itself:
Ea∼πµ∗σ,˜σ(·|s)
h
(a −µ∗
σ (s))2qπ∗
σ (s, a)
i
Ea∼πµ∗σ,˜σ(·|s)qπ∗σ (s, a)
≤˜σ2.
K. Proof of Theorem 8: Bias-Error Sensitivity in the Gaussian case
In this section we prove a bias-error sensitivity result for the Gaussian noise case, similarly to 4. Theorem 8 exhibits a
Bias-Sensitivity trade-off w.r.t. the noise parameter σ. When σ grows, the bias increases in ∥σ∥1, but the sensitivity term
decreases. In the limit where σ goes to inﬁnity, the approximation error tend to zero. In the other limit, where the noise
reduces to zero, we return to the case of a greedy optimal policy. Indeed, as the bound shows, we get an unbiased solution,
and the sensitivity term reduces to the classical bound of Bertsekas & Tsitsiklis (1995). Unsurprisingly, we get a better
sensitivity bound only when there is a sufﬁcient overlap between the two policies.
In order to prove the theorem, we will ﬁrst prove two propositions: A bias proposition 20 and a sensitivity proposition 21.
Then, we plug the results in the following triangle inequality:


v∗−vˆµ,σ

 ≤∥v∗−v∗
σ∥+


v∗
σ −vˆµ,σ

First, we derive the bias proposition,


## Page 23


Exploration Conscious Reinforcement Learning Revisited
Proposition 20. Let σ ≥0 and let π∗
σ be the σ-optimal policy. Assume an MDP M is Lipschitz, i.e., there exists Lr ≥0 and
Lp ≥0, such that, ∀s, s′ ∈S and ∀a1, a2 ∈A, |r(s, a1) −r(s, a1)| < Lr ∥a1 −a2∥1 and |p(s′|s, a1) −p(s′|s, a1)| <
Lp ∥a1 −a2∥1. Then, the following holds,
∥v∗−v∗
σ∥≤
r
2
π
(1 −γ) Lr + γLpRmax
(1 −γ)2
σ
Proof.
∥v∗−v∗
σ∥= ∥v∗−Tσv∗
σ∥
≤∥v∗−Tσv∗∥+ ∥Tσv∗−Tσv∗
σ∥
≤∥v∗−Tσv∗∥+ γ ∥v∗−v∗
σ∥
Where the inequality is due to the fact that Tσ is a γ-contraction. Simple algebra gives ∥v∗−v∗
σ∥≤∥v∗−Tσv∗∥
1−γ
Next, we bound the nominator:
v∗(s) −(Tσv∗)(s) = (T ∗v∗)(s) −(Tσv∗)(s)
= max
a
r(s, a) + γ
X
s′∈S
p(s′|s, a)v∗(s′) −max
µ
Z
N(a|µ, σ)
"
r(s, a) + γ
X
s′∈S
p(s′|s, a)v∗(s′)
#
da
≤r(s, a∗) + γ
X
s′∈S
p(s′|s, a∗)v∗(s′) −
Z
N(a|a∗, σ)
"
r(s, a) + γ
X
s′∈S
p(s′|s, a)v∗(s′)
#
da
=
Z
N(a|a∗, σ)
"
(r(s, a∗) −r(s, a)) + γ
X
s′∈S
(p(s′|s, a∗) −p(s′|s, a)) v∗(s′)
#
da
≤
Z
N(a|a∗, σ)
"
(r(s, a∗) −r(s, a)) + γ
X
s′∈S
|p(s′|s, a∗) −p(s′|s, a)| v∗(s′)
#
da
≤
Z
N(a|a∗, σ)
"
(r(s, a∗) −r(s, a)) + γRmax
1 −γ
X
s′∈S
|p(s′|s, a∗) −p(s′|s, a)|
#
da
≤
Z
N(a|a∗, σ)

Lr ∥a∗−a∥1 + γ ∥p(· | s, a∗) −p(· | s, a)∥T V
Rmax
1 −γ

da
≤
Z
N(a|a∗, σ)

Lr ∥a∗−a∥1 + γLp ∥a∗−a∥1
Rmax
1 −γ

da
=

Lr + γLp
Rmax
1 −γ
 Z
N(a|a∗, σ) ∥a∗−a∥1 da
=

Lr + γLp
Rmax
1 −γ
 r
2
π ∥σ∥1
Where the ﬁrst transition is due to a∗∈arg max r(s, a) + γ P
s′∈S p(s′|s, a)v∗(s′), and the last is due to the absolute ﬁrst
moment of the Gaussian distribution.
We get,
∥v∗−Tσv∗∥≤
r
2
π

Lr + γLp
Rmax
1 −γ

∥σ∥1
Finally, combining the two results gives:
∥v∗−v∗
σ∥≤
r
2
π
(1 −γ)Lr + γLpRmax
(1 −γ)2
∥σ∥1


## Page 24


Exploration Conscious Reinforcement Learning Revisited
Finally, we prove the following sensitivity proposition using:
Proposition 21. Let σ ∈R|A|
+ . Assume ˆv∗
σ is an approximate σ-optimal value s.t. ∥v∗
σ −ˆv∗
σ∥= δ for some δ > 0. Let
µ∗
σ, ˆµ∗
σ ∈RA be the greedy mean policy w.r.t. v∗
σ and ˆv∗
σ respectively. Then,
∥v∗
σ −vπˆ
µ∗σ,σ∥≤1
2
γδ min{∥µ∗
σ −ˆµ∗
σ∥σ−2 , 4}
1 −γ
,
where ∥·∥σ−2 is the σ−2-weighted euclidean norm.
Proof. First, notice that the total variation distance is not bigger than 2, which is the case of two different deterministic
policies, as seen in (Bertsekas & Tsitsiklis, 1995)[Proposition 6.1]. Next, the Kullback-Leibler divergence between
two Gaussian distributions with the same variance σ is 1
2 ∥µ∗
σ −ˆµ∗
σ∥2
σ−2, where ∥·∥σ−2 is the σ−2-weighted euclidean
norm. Finally, by using Pinsker’s inequality to bound the total variation distance, and plugging in the closed form of the
Kullback-Leibler divergence, one gets the required result.
L. Supplementary material for Section 5
In this section we give the proofs for the algorithms proposed in Section 5.1.
The proof of Lemma 9 is given as follows:
Proof. By using the deﬁnition of T Eq
α , and due to v∗
α = maxa q∗
α(·, a), we have that,
q∗
α(s, a) = T Eq
α q∗
α(s, a)
= rα(s, a) + γ
X
s′
Pα(s′ | s, a) max
a′ q∗
α(s′, a′)
= (1 −α)
 
r(s, a) + γ
X
s′
P(s′ | s, a)v∗
α(s′)
!
+ α
X
a
π(a′ | s)
 
r(s, a′) + γ
X
s′
P(s′ | s, a′)v∗
α(s′)
!
= (1 −α)qπα(π∗
α,π0)(s, a) + α
X
a
π0(a′ | s)qπα(π∗
α,π0)(s, a′),
where in the last relation we used (8).
We now prove the following lemma:
Lemma 22. The operator T Eq
α
is a γ-contraction, and its ﬁxed point is qπα(π∗
α,π0)
Proof. It is easy to verify this operator is a γ-contraction using standard arguments (Bertsekas & Tsitsiklis, 1995). We prove
that the ﬁxed point of T Eq
α
is qπα(π∗
α,π0). First, by using the max operator w.r.t. the action on the result in Lemma 9, we get
v∗
α = (1 −α) max
a
qπα(π∗
α,π0)(·, a) + αΠ0qπα(π∗
α,π0).
(21)
Consider the deﬁnition of qπα(π∗
α,π0) (8). We have that,
qπα(π∗
α,π0)(s, a) = r(s, a) + γ
X
s′
P(s′ | s, a)v∗
α(s′)
= r(s, a) + γ(1 −α)
X
s′
P(s′ | s, a) max
a′ qπα(π∗
α,π0)(s′, a′)
+ γα
X
s′,a′
P(s′ | s, a)π0(a′ | s′)qπα(π∗
α,π0)(s′, a′)
= T Eq
α qπα(π∗
α,π0)(s, a),
where the ﬁrst relation holds by plugging (21) and the third relation holds by identifying the operator T Eq
α .


## Page 25


Exploration Conscious Reinforcement Learning Revisited
L.1. Convergence of Expected α-Q-Learning
Now, we move on to prove the convergence of Expected α-Q-Learning:
Theorem 23. Consider the process described in Algorithm 1. Assume the sequence {ηt}∞
t=0 satisﬁes ∀s ∈S, ∀a ∈A,
P∞
t=0 ηt(st = s, aenv,t = a) = ∞, and P∞
t=0 η2
t (st = s, aenv,t = a) < ∞. Then, the sequence {qn}∞
n=0 converges w.p 1
to qπα(π∗
α,π0).
Proof. The updating equations of Algorithm 1 can be written as
qn+1(s, aenv) =(1 −ηt)qn(s, aenv) + ηt(T Eq
α qn(s, aenv) −wt),
where
wt = rt + γ(1 −α)v(st+1) + γαvπ0(st+1) −T Eq
α qt(s, aenv),
and
v(st+1) = max
a′ q(st+1, a′),
vπ0(st+1) =
X
a′
π0(a′ | st+1)q(st+1, a′).
We let Ft = {Ht−1, st, aenv, Xt, achosen, rt}, where Ht−1 is the entire history until and including time t −1. i.e, the
ﬁltration includes both the chosen action, before deciding whether to act with it or according to π0, and the acted action.
We have that,
E
h
rt + γ(1 −α) max
a
q(st+1, aenv)(st+1) | Ft
i
=
= r(st, aenv) + γ(1 −α)
X
s′
P(s′ | s, aenv) max
a′ q(s′, a′) + γα
X
s′,a′
P(s′ | st, aenv)π0(a′ | s′)q(s′, a′),
and E [wt | Ft] = 0. It is also easy to see that E

w2
t | Ft

≤A + B||Q||2
∞.
Thus, according to (Bertsekas & Tsitsiklis, 1995)[Proposition 4.4] the process converges to the ﬁxed point contraction
operator T Eq
α , qπα(π∗
α,π0) (see Lemma 22).
L.2. Convergence of Surrogate α-Q-Learning
In this section, we prove the convergence of Surrogate α-Q-Learning:
Theorem 24. Consider the process described in Algorithm 2. Assume the sequence {ηt}∞
t=0 satisﬁes ∀s ∈S, ∀a ∈A,
P∞
t=0 ηt(st = s, aenv,t = a) = ∞, and P∞
t=0 η2
t (st = s, aenv,t = a) < ∞. Then, the sequences {qn}∞
n=0 and {qα,n}∞
n=0
converges w.p 1 to qπα(π∗
α,π0) and q∗
α, respectively.
We will use the following result (Singh et al., 2000)[Lemma 1].
Lemma 25. Consider a stochastic process (αt, ∆t, ∆t, ft), t ≥0, where αt, ∆t, ft : X →R satisfy the equations
∆t+1(x) = (1 −αt(x))∆t(x) + αt(x)ft(x),
x ∈X, t = 0, 1, 2, ..
(22)
Let Ft be a sequence of increasing σ-ﬁelds such that α0 and ∆0 are F0-measurable, t = 1, 2, .... Assume that the following
hold:
1. The set X is ﬁnite.
2. 0 ≤αt(x) ≤1, P
t αt(x) = ∞, P
t α2
t(x) < ∞w.p 1.
3. ||E [ft(·) | Ft] || ≤κ||∆t|| + ct, where κ ∈[0, 1) and ct converges to zero w.p 1.
4. V ar [Ft(·) | Ft] ≤K(1 + ||∆t||)2, where K is some constant.
Then, ∆t converges to zero with probability 1.


## Page 26


Exploration Conscious Reinforcement Learning Revisited
Observe that qt has updating rule as in Expected α-Q-Learning (see Algorithm 1), and is independent of qα. Due to the
assumptions that ∀s ∈S, ∀a ∈A
∞
X
t=0
ηt(st = s, aenv,t = a) = ∞,
∞
X
t=0
ηt(st = s, aenv,t = a) ≤∞,
we get that the sequence {qt}∞
t=0 converges to qπα(π∗
α,π0) w.p 1.
We now manipulate the updating of q in Algorithm 2 to have the form of (22). Deﬁne the following difference
∆t(s, a) = qt(s, a) −q∗
α(s, a),
and consider the ﬁltration Ft = {Ht−1, st, achosen}.
By decreasing q∗
α(s, a) from both sides of the updating equations of q in Algorithm 2, we obtain for any a ∈A,
∆t+1(st, a) = (1 −ηt)∆t(st, a)ft(st, a).
If ¯a = achosen then,
ft(st, ¯a) = rt + γvα,t(st+1) −q∗
α(s, a),
whereas for ¯a ̸= achosen,
ft(st, ¯a) =Xtqπα(π∗
α,π0)(st, ¯a) + (1 −Xt)(rt + γvα,t(st+1))
+ Xt(qt(st, ¯a) −qπα(π∗
α,π0)(st, ¯a)) −q∗
α(st, ¯a).
We now show that for all action entries ¯a ∈A, E [ft(st, ¯a) | Ft] || ≤κ||∆t(st, ¯a)|| + ct, and ct converges to zero w.p. 1.
If ¯a = achosen then,
E [ft(st, ¯a) | Ft] = (1 −α)(r(st, ¯a) + γ
X
s′
P(s′ | st, ¯a) max
a′ qα,t(s′, a′))
+α(rπ0(st)+γ
X
s′
P π0(s′ | st) max
a′ qα,t(s′, a′))−q∗
α(s, a)
= Tαqα,t(st+1, a′)) −q∗
α(s, a).
Thus, for this case,
||E [ft(st, ¯a) | Ft] || = ||Tαqα,t(st+1, a′)) −q∗
α(s, a)||
= ||Tαqα,t(st+1, a′)) −q∗
α(s, a)||
≤γ||qα,t(st+1, a′)) −q∗
α(s, a)||,
meaning, ct = 0 for this entry. We now turn to the case ¯a ̸= achosen.
E [ft(st, ¯a) | Ft] = (1 −α)qπα(π∗
α,π0)(st, ¯a) −q∗
α(s, ¯a)
+ α(rπ0 + γ
X
s′
P π0(s′ | s) max
a′ qα,t(s′, a′))
+ (1 −α)(qt(st, ¯a) −qπα(π∗
α,π0)(st, ¯a)).
Deﬁne
ct ≜(1 −α)(qt(st, ¯a) −qπα(π∗
α,π0)(st, ¯a)).
See that ct converges to zero w.p. 1, since qt converges to qπα(π∗
α,π0). Furthermore, using Lemma 9, we have that
(1 −α)qπα(π∗
α,π0)(st, ¯a) −q∗
α(s, ¯a) = −α(rπ0 + γ
X
s′
P π0(s′ | s) max
a′ q∗
α(s′, a′)).


## Page 27


Exploration Conscious Reinforcement Learning Revisited
Thus,
E [ft(st, ¯a) | Ft] = −α(rπ0 + γ
X
s′
P π0(s′ | s) max
a′ q∗
α(s′, a′)) + α(rπ0 + γ
X
s′
P π0(s′ | s) max
a′ qα,t(s′, a′)) + ct
= αγ
X
s′
P π0(s′ | s)(max
a′ qα,t(s′, a′) −max
a′ q∗
α(s′, a′)) + ct
= αγ
X
s′
P π0(s′ | s)|(max
a′ qα,t(s′, a′) −max
a′ q∗
α(s′, a′))| + ct
= αγ
X
s′
P π0(s′ | s) max
a′ |(qα,t(s′, a′) −q∗
α(s′, a′))| + ct
= αγ max
s′,a′ ||qα,t −q∗
α|| + ct
Where in the ﬁrst relation we applied Lemma 9. By showing similar result for −E [ft(st, ¯a) | Ft], we conclude that,
E [ft(st, ¯a) | Ft] ≤αγ max
s′,a′ ||qα,t −q∗
α|| + ct,
where ct converges to zero w.p.1. The Var(ft(·, ·)) can be bounded by K(1 + ||∆t||)2, since the reward is bounded and
P∞
t=0 η2
t (st = s, aenv,t = a) < ∞.
We conclude that all conditions of Lemma 25 are satisﬁed for each ¯a ∈A and, thus, Lemma 25 establishes the convergence
of the procedure.
L.3. Proof of the gradients’ equivalence in section 5.2
Proof.
∇uqπ
σ (s, u) = ∇u
Z
A
N (u′|u, σ) qπ (s, u′) du′
=
Z
A
qπ (s, u′) ∇uN (u′|u, σ) du′
= −
Z
A
qπ (s, u′) ∇u′N (u′|u, σ) du′
= −qπ (s, u′) N (u′|u, σ)|∞
−∞+
Z
A
N (u′|u, σ) ∇u′qπ (s, u′) du′
=
Z
A
N (u′|u, σ) ∇u′qπ (s, u′) du′
Where we used integration by parts.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1811.01741v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1811.01741v1_Learning_Shared_Dynamics_with_Meta-World_Models

> Source: 1811.01741v1_Learning_Shared_Dynamics_with_Meta-World_Models.pdf

> Pages: 10

---


## Page 1


Learning Shared Dynamics with Meta-World Models
Lisheng Wu ∗, Minne Li ∗, Jun Wang
University College London
{lisheng.wu.17,minne.li.17,jun.l.wang}@ucl.ac.uk
Abstract
Humans have consciousness as the ability to perceive events
and objects: a mental model of the world developed from
the most impoverished of visual stimuli, enabling humans to
make rapid decisions and take actions. Although spatial and
temporal aspects of different scenes are generally diverse, the
underlying physics among environments still work the same
way, thus learning an abstract description of shared physical
dynamics helps human to understand the world. In this paper,
we explore building this mental world with neural network
models through multi-task learning, namely the meta-world
model. We show through extensive experiments that our pro-
posed meta-world models successfully capture the common
dynamics over the compact representations of visually dif-
ferent environments from Atari Games. We also demonstrate
that agents equipped with our meta-world model possess the
ability of visual self-recognition, i.e., recognize themselves
from the reﬂected mirrored environment derived from the
classic mirror self-recognition test (MSR).
Introduction
Building machines to mimic human brain’s abilities has
drawn considerate attention from the recent progress in ar-
tiﬁcial intelligence (AI) (Lake 2014; Lake, Salakhutdinov,
and Tenenbaum 2015; Graves et al. 2016; Baker et al. 2017).
Founders of the modern computational science consider
the possibility that machines would ultimately possess con-
sciousness (Turing 1950), which is the ability to perceive
events and objects as humans have (Van Gulick 2018). How-
ever, many of the current advances lie on the statistical pat-
tern recognition paradigm, which treats learning as making
good predictions by discovering patterns correlated to high
value rewards (or low errors) directly from the environments
(Lake et al. 2017). These approaches do not draw inspira-
tion from human cognition aspects, i.e., learning and think-
ing like a person (Dehaene, Lau, and Kouider 2017), and are
considered as model-free. At the early stage of learning in
high-dimensional environments with sparse rewards, model-
free methods cannot ﬁnd an optimal learning direction due
to the lack of reward signals, thus requiring large amounts
of data to explore and learn a good policy.
In contrast, humans can achieve comparable perfor-
mances on a range of tasks with much less experiences. For
∗Equal contribution.
example, a human player needs only two hours of practice
before achieving reasonable performance on one Atari game
and can quickly adapt to different games, while DQN needs
several days’ of training using large amounts of computa-
tional resources (Mnih et al. 2015).
Humans develop a mental model of the world from the
most impoverished of visual stimuli (Heider and Simmel
1944), and use this world to make rapid decisions and take
actions (Forrester 1971). To build truly human-like AI ma-
chines, we consider an engineering approach in the ﬁrst step,
and focus on developing the world model to support expla-
nation and understanding. One of the key ingredients for
building this model is the cognitive capability of understand-
ing the underlying physics and dynamics of the environment
(Wellman and Gelman 1992). For example, in the Atari Pong
game, the ball and paddles follow principles of persistence,
continuity, cohesion and solidity (Bellemare et al. 2015).
Through mental models of the world, humans can recon-
struct a perceptual scene following these principles to sup-
port mental simulations that can predict the future movement
of the objects (Spelke 1990). Equipped with a world model
understanding these intuitive theories of physics, agents can
simulate the real experiences and learn the structured prop-
erties of the environment. By exploiting the underlying dy-
namics learned by the model, we can reduce the dimension
of the input and generalize features across states and ac-
tions in high-dimensional environments (Watter et al. 2015;
Wahlstr¨om, Sch¨on, and Deisenroth 2015; Levine and Abbeel
2014). With one transition model, agents can attend to the
dynamics of the states by modeling how the environment
evolves with speciﬁc action. These approaches, regarded
as model-based learning, have been investigated by sev-
eral previous works (Sutton 1990; Levine and Abbeel 2014;
Watter et al. 2015; Wahlstr¨om, Sch¨on, and Deisenroth 2015;
Schmidhuber 2015; Gu et al. 2016; Leibfried, Kushman, and
Hofmann 2016; Ha and Schmidhuber 2018). However, the
learned underlying dynamics are often restricted to be effec-
tive in a single world environment.
Although spatial and temporal aspects of different scenes
are generally diverse, the underlying physics among envi-
ronments still work the same way. As such, humans can
easily adapt to different environments with the help of their
understanding of the underlying physics. For example, hu-
mans can still play Pong game when the observation is
arXiv:1811.01741v1  [cs.AI]  5 Nov 2018


## Page 2


mirrored or transposed (rotated by ninety degrees and mir-
rored). On the other hand, recent computational achieve-
ments cannot solve such scene understanding problems, e.g.,
not rotation-invariant. Human-like world models should un-
derstand these shared physical dynamics and use them to
rapidly generalize knowledge to new tasks and environ-
ments. This common knowledge serves as a prior for learn-
ing new task, helping agents to efﬁciently adapt to new en-
vironments. For example, the knowledge gained from Atari
Pong can be beneﬁcial for learning to play Breakout and
Video Pinball, which share the common concept of the
ball and paddles (Parisotto, Ba, and Salakhutdinov 2015).
Multi-task learning (or meta-learning) (Duan et al. 2016;
Finn, Abbeel, and Levine 2017; Parisotto, Ba, and Salakhut-
dinov 2015) has been used to learn the common knowledge
among different tasks. However, most meta-learning algo-
rithms generally have troubles in searching common param-
eters or feature spaces directly from high-dimensional envi-
ronments.
In this paper, we explore building meta mental world
models to establish the common physical dynamics over
the compact representations from visually different envi-
ronments. Without the guidance of explicit rewards, our
meta-world models learn about the relationships among dif-
ferent worlds through multi-task learning. The key con-
cept is to maintain a recurrent neural network (RNN) using
self-supervised learning to capture the underlying dynam-
ics of each environment and ﬁnd a common latent struc-
ture across different environments. As a result, we obtain
a low-dimensional common latent structure among multiple
environments which share the underlying dynamics learned
by the RNN. We demonstrate the performance of our meta-
world using ﬁve variants of the Atari Pong game, which are
completely different from the original Pong in the transition
function and even the state space.
As the only premise we have is that all training environ-
ments share the same physical dynamics, two challenges are
induced to build meta-world models. Firstly, the transforma-
tion pattern and corresponding states between environments
are unknown, so we cannot simply obtain the common rep-
resentations by direct transformation or supervised learning.
Secondly, it’s not guaranteed to learn shared dynamics as
the capacity of neural networks can be large enough to re-
gard all training environments’ dynamics as different even
with a single model. Through extensive experiments, we
ﬁnd that it’s possible to unify two visually different envi-
ronment using the shared dynamics. We also demonstrate
that agents equipped with our meta-world model possess the
ability of visual self-recognition, i.e., pass the classic mirror
self-recognition test (MSR) (Gallup 1970). To the best of
our knowledge, this is the ﬁrst work to build a meta-world
model to learn shared dynamics.
Related Work
Model-based deep reinforcement learning algorithms have
been shown to be more effective than model-free alterna-
tives in certain tasks (Watter et al. 2015; Wahlstr¨om, Sch¨on,
and Deisenroth 2015; Levine and Abbeel 2014). One of the
classical model-based algorithms is Dyna-Q (Sutton 1990)
which learns the policy from both the model and the en-
vironment by supplementing real world on-policy experi-
ences with simulated trajectories. However, using trajecto-
ries from a non-optimal or biased model can lead to learn-
ing a poor policy (Gu et al. 2016). To model the world
environment of Atari Games, autoencoder has been used
to predict the next observation and environment rewards
(Leibfried, Kushman, and Hofmann 2016). Some previ-
ous works (Schmidhuber 2015; Ha and Schmidhuber 2018;
Leibfried, Kushman, and Hofmann 2016) maintain a re-
current architecture to model the world using unsupervised
learning and proved its efﬁciency in helping RL agents to
outperform previous methods in complex environments. The
work from (Ha and Schmidhuber 2018) also demonstrates
their model’s capability of helping the agent to act in real
world by learning from the ”dream world”, i.e., the men-
tal model of the world. However, these models can only be
applied to a single environment and need to be built from
scratch for new environments. Although using a similar re-
current architecture, our work differs from above works by
learning the common underlying dynamics over multiple en-
vironments.
To achieve multi-task learning, recurrent architecture
(Duan et al. 2016; Wang et al. 2016) has also been used to
learn to reinforcement learn by adapting to different MDPs
automatically, which is shown to be comparable to the
UCB1 algorithm (Auer, Cesa-Bianchi, and Fischer 2002) on
bandit problems. Meta-learning shared hierarchies (MLSH)
(Frans et al. 2017) shares sub-policies among different tasks
to achieve the goal in the training process, where high hier-
archy actions are obtained and reused in other tasks. Model-
agnostic meta-learning algorithm (MAML) (Finn, Abbeel,
and Levine 2017) minimizes the total error across multi-
ple tasks by locally conducting few-shot learning to ﬁnd
the optimal parameters for both supervised learning and RL.
Actor-mimic (Parisotto, Ba, and Salakhutdinov 2015) dis-
tills multiple pre-trained DQNs on different tasks into one
single network to accelerate the learning process by ini-
tializing the learning model with learned parameters of the
distilled network. To achieve promising results, these pre-
trained DQNs have to be expert policies. Distral (Teh et al.
2017) learns multiple tasks jointly and trains a shared policy
as the ”centroid” by distillation. Most of the meta-learning
approaches consider the problems within the model-free
RL paradigm and focus on ﬁnding the common structure
in the policy space. However, learning in high-dimensional
environments with model-free approaches suffers from the
sparse and high-variance reward signals, thus requiring large
amounts of data to explore. In contrast, we explicitly main-
tain a meta-world model to capture the latent structures and
dynamics of the environment, thus having more stable cor-
relation signals.
In terms of the meta-learning for model-based algorithms,
(Al-Shedivat et al. 2017; Clavera et al. 2018) focused on
model adaptation when the model is incomplete or the un-
derlying MDPs are evolving. By taking the unlearned model
as a new task and continuously learning new structures, the
agent can keep its model up to date. Different from above ap-
proaches, we focus on how to establish the common physi-


## Page 3


cal dynamics over the compact representations from visually
different environments.
Preliminaries
In this section, we will introduce the notation and formalize
the meta-world learning.
Environment Setting
We ﬁrst deﬁne the environment as a
Markov Decision Process (MDP) represented by tuple Γ =
⟨S, P, A, R⟩, where S, P, A, R are the state space, the tran-
sition probability function, the action space, and the reward
function respectively. At each time step t, a state st ∈S is
provided by the environment Γ. The agent in this environ-
ment receives this state information and chooses an action
at ∈A according to its own strategy. The environment then
receives this action and moves to a new state st+1 following
the transition function P(st+1|st, at) : S ×A →S. The ini-
tial state of the environment is determined by a distribution
p1(s1) : S →[0, 1]. In the following sections, we also use
the apostrophe to indicate quantities at next time step when
t is neglected for simplicity, e.g., s′ instead of st+1.
To help agents learn compact representations of the envi-
ronment, (Ha and Schmidhuber 2018) introduced the world
model. Inspired by the human cognitive system, the world
model (fφ, gθ) consists of two components: a Vision Model
(V) and a Memory Model (M), denoted as fφ and gθ, pa-
rameterized by φ and θ respectively. At each time step t, the
vision model receives the real-time high-dimensional obser-
vation (e.g., a image frame) from the environment and com-
presses the input into a compact but informative represen-
tation zt. The memory model serves as the history encoder
and future predictor by: (1) compressing the abstract presen-
tation from V and producing a history information ht over
time; (2) combining the history information ht−1 with the
current abstract observation zt to predict the future zt+1.
Because the agent affects the environment state with its own
action, agent action at is also fed into the memory model to
better predict the future. With the ability of reconstructing
low-dimensional representations to the form of environment
observations, a variational autoencoder (VAE) (Kingma and
Welling 2013) is normally used as the vision model, where
the encoder and the decoder are denoted as f e and f d, pa-
rameterized by φe and φd respectively. Agents can then use
the information from zt and ht to make a decision at, where
zt = f e
φ(st),
(1)
ˆst = f d
φ(zt) = fφ(st),
(2)
˜zt+1, ht+1 = gθ(zt, ht, at),
(3)
˜st+1 = f d
φ(˜zt+1).
(4)
Meta-World Model
To train a world model that can
seize the common underlying dynamics of multiple envi-
ronments Γi ∈{Γ1, ..., ΓN}, we propose the meta-world
model and formalize the problem of meta-world learning.
The goal of meta-world learning is to build one mem-
ory model M for sharing across multiple environments.
During the training stage, a set of trajectories Di
=
{(s1, a1, ..., sT −1, aT −1, sT )} are sampled from the envi-
ronment Γi. We deﬁne the meta-world model as (f∗, gθ) and
si
t
ˆsi
t
zi
t
fi
e
fi
d
(a) Reconstruction
zi
t
!zi
t+1
!si
t+1
ai
t
si
t
fi
e
fi
d
gθ
(b) Prediction
Figure 1: Meta-learning for meta-world models.
the world model for environment Γi as (fφi, gθ), abbreviated
as (fi, gθ). For each environment Γi, the V model with pa-
rameter φi encodes input states si to latent vectors zi, which
represents the dynamics learned by the meta-world model.
Our expectation is to learn similar zi, i.e., shared underlying
dynamics across multiple environments.
Methods
In this section, we ﬁrst provide the meta-learning algorithm
for meta-world models. Then we present the method to vali-
date the performance of meta-world models. To ﬁnd the un-
derlying dynamics of different environments, we describe
some further constraints applied to the intermediate output
distribution of the V model.
Meta-Learning for Meta-World Models
To train a meta-world model, we adopt the variational au-
toencoder (VAE) as the vision model V and the LSTM
(Hochreiter and Schmidhuber 1997) model with variant out-
put as the memory model M.
As illustrate in Fig. 1, the training process consists of two
stages: the reconstruction of V models and the prediction
of M models. The reconstruction stage is for V model to
compress the input state st to the latent vector zt, and un-
compress zt to the output state ˆst that closely matches the
original st. In the prediction stage, the M model takes both
the action at and the latent vector zt as inputs to predict
˜zt+1. Then, the predicted state ˜st+1 is obtained by decoding
˜zt+1 using the decoder of the V model to approximate the
true next state st+1, which is the result of applying at to the
environment under the current state st. The reconstruction
loss Lr is the distance between the state approximation ˆst
and the true environment state st, and the prediction loss Lp
comes from the distance between the predicted state ˜st+1
and the actual state of the next time step st+1:
Lr(Γi, φi) =
X
Di
X
t
d(ˆst, st),
(5)
Lp(Γi, θ, φi) =
X
Di
X
t
d(˜st+1, st+1),
(6)
where d is a distance measurement function. During the
training process, the updating rules for both models are de-
ﬁned as
θ ←θ −α
X
Γi∼p(Γ)
∇θLp(Γi, θ, φi),
(7)
φi ←φi −βr∇φiLr(Γi, φi) −βp∇φiLp(Γi, θ, φi),
(8)


## Page 4


where βr and βp are the ratio of Lr and Lp at one training
step respectively. The V model is updated with gradients of
both Lr and Lp, and the M model is updated with gradients
of Lp only.
In the meta-learning for meta-world models, we alternate
the training process for V models between minimizing Lr
and Lp by adjusting βr and βp accordingly. For the train-
ing of V models, minimizing Lp helps to adjust V models
of different environments with respect to the shared under-
lying dynamics learned by the memory model M. However,
the adjustment of V models to satisfy the learning of shared
dynamics will in turn affect the reconstruction ability of V
models. The optimization of Lr and Lp are inﬂuenced by
each other similar to a general-sum game, where a equilib-
rium is hard to reach when two optimization process run si-
multaneously. Thus, we use the alternate training scheme as
minimizing Lr and Lp for V models respectively throughout
the training process to avoid trapping into local minimum.
To capture the shared underlying dynamics across multiple
environments, following constraints are considered in our
model:
1. The Memory model M should make use of the abstract
representation of the current state and its own memory to
predict the next state with speciﬁc action.
2. The Vision model V should be able to reconstruct the
original state from its abstract representation.
Validating the Model Performance
People may doubt that the meta-world might not learn the
common dynamics because a neural network with high ca-
pacity could represent multiple dynamics simultaneously.
Despite the strict constraints listed above, it’s still possible
for our meta-world model to learn multiple dynamics simul-
taneously or be trapped into local minimum. In this section,
we present the method to validate that meta-world models
actually learn the common dynamics of multiple environ-
ments.
Suppose we have environment Γi and environment Γj
sharing the same underlying physical dynamics but differ-
ent visual observations. For the sake of simplicity, we as-
sume the visual observation of Γi is the transpose of that
of Γj, i.e., clockwise rotated by 90◦and horizontal ﬂipped.
For most of the advanced neural networks without rotation-
invariance, these two environments are totally different. Al-
though they might be seen as different to humans at the ﬁrst
glance, humans will come to realize Γi and Γj are almost
identical because they consist of the same components and
share the same underlying physical dynamics, even though
the dynamics are presented in different directions. Thus, hu-
mans have the ability to unify different observations sharing
the same underlying dynamics.
To demonstrate that our meta-world model is also capa-
ble of capturing the common dynamics of such two environ-
ments instead of treating them as different dynamics and ab-
sorbing them simultaneously into the neuron model, Γi and
Γj should have very similar abstract representations zi and
zj of corresponding observations si and sj. However, it’s not
applicable to directly measure the distance of the abstract
representations in the vector space, due to the high-variance
of V models. Instead, we validate our model by encoding the
observation si from Γi to the corresponding abstract repre-
sentation zi, which is decoded with the decoder of the V
model of environment Γj. Then, we compare the decoded
result ˆsj with the corresponding observation sj. If sj and ˆsj
are almost identical, we can conﬁrm that meta-world models
actually capture the underlying physical dynamics of differ-
ent environments and unify their abstract representations as
the shared dynamics, rather than simply memorizing and ab-
sorbing them into the neuron models.
Adding Constraints on Abstract Representations
As described in the above section, we want to unify the
abstract representations of different environments sharing
the same underlying physical dynamics. However, the ab-
stract representation generated by each vision model Vi ∈
V1, ..., VN might not be the same without further constraints
on the learning period. Concretely, because we adopt the
VAE as the V model, the element-wise similarity of the
abstract representation zi is determined by the distribution
(both the mean and the variance) of the intermediate output
of VAE. Thus, it is difﬁcult for randomly initialized V mod-
els to ﬁnd the common dynamics through the coordination
of abstract representations.
To add further constraints on the distribution of the ab-
stract representations zi, we introduced the Maximum Mean
Discrepancy (Gretton et al. 2007) to regularize the channels
of zi by adding constraints on the distance among all the
mean and variance of the intermediate output of V models.
Concretely, we force all meta-world models to have similar
distributions to the abstract representation of Γ1 by adding
the total training loss with a regularizer
LMMD =
X
−Γ1
ηµ||¯µi −¯µ1||2 + ησ||log(σi) −log(σ1)||2,
(9)
where µi and σi are the mean and variance of the VAE of
Γi, and ηµ and ησ are the ratio of the error of mean and log
variance respectively. Then the total training loss of the V
model can be written as,
L = βpLp + βrLr + ηLMMD.
(10)
During the training process, we add MMD loss to the re-
construction stage, while keeping training with prediction
loss in the prediction stage. In this way, the distributions of
abstract representations can also be inﬂuenced by other en-
vironments through the participation of memory model M.
That is, the V models of other environments V2, ..., VN can
affect M to change its parameters by the joint training in
the prediction stage, thus inﬂuencing the distributions of ab-
stract representations of V1 indirectly.
Experiments
This section starts with the introduction of our experiment
environment (the Atari Pong game), problem setup, and
evaluation criteria. We then present the experiment results
and analysis of different training strategies, i.e., using cor-
responding states from different environments as training


## Page 5


(a) Γo →Γt
(b) Γo →Γh
(c) Γo →Γc
(d) Γo →Γm
(e) Γo →Γv
Figure 2: Meta-world environments.
data or not. We also demonstrate that agents equipped with
our meta-world model possess the ability of visual self-
recognition as being self-aware.
The Pong World
Atari Pong game is a environment with two paddles that can
only move up or down to hit the ball. The dynamics of Pong
game involves an opponent which the player’s action cannot
control, and an agent that the player can control To verify
the ability of our models capturing shared physical dynamics
among different visual observations, we generate ﬁve vari-
ants of the Atari Pong game while keeping the physical dy-
namics of the environment. As shown in Fig.2, each variant
corresponds to one transformation from Γo: (a) the trans-
posed Γt, which is transformed from the state observation
of Γo by clockwise rotating 90◦and horizontal ﬂipping; (b)
the horizontal-swapped Γh, which is generated by vertically
splitting the observation frame of Γo from the center and
swapping the left part with the right part; (c) the inverse Γc,
which is created by exchanging the background color with
the paddles/ball color of Γo; (d) the mirror-symmetric Γm,
which reﬂects Γo like a mirror by horizontally swapping the
observation; and (e) the vertical-swapped Γv, which is ob-
tained by horizontally splitting the observation of Γo from
the center and swapping the upper part with the lower part.
We should note that the split line in the transformation from
Γo to Γv may cut the paddles into two halves, e.g., a part
of the paddle could disappear from the top of the frame and
reappear at the bottom when the paddle is moving across the
center. We consider this situation as the paddle teleportation.
These variants can be divided into two groups by the dif-
ference of state space compared to Γo. The ﬁrst group, in-
cluding Γt, Γh, and Γc, has totally different state space from
Γo by either putting the paddles in different positions or ex-
pressing the corresponding states with different pixel values.
Obviously, actions in this group of environments appear dif-
ferently because of the new state space. The second group,
consisting of Γm and Γv, has either the same or at least some
overlaps with the state space of Γo. However, the actions still
appear differently because of the transformation.
Different from the original Atari Pong observations, we
(1) transform each image frame to a binary matrix; (2) re-
move the scoreboard to focus on the dynamics of the pad-
dles; and (3) resize each frame to 64 ∗64 to serve as the
state observations of the original Pong world environment
Γo. The action space is formed by all six available discrete
actions of the original Atari game environment.
Problem Setup
Although the presented environment variants transit with
actions in different ways from the aspect of observations,
they share the same underlying physical dynamics as ac-
tions impose transition on the paddle in corresponding ways.
By observing the shared dynamics from environment vari-
ants, humans could recall the dynamics seen in the origi-
nal environment Γo and try to ﬁnd the similarities, then ﬁ-
nally consider them as highly related environments. How-
ever, artiﬁcial neural networks (ANNs) are not able to gen-
eralize across such transformation with ease. For example,
ANNs are not rotation-invariant, thus regarding the trans-
posed environment Γt as a totally different world as Γo. Our
target is to unify the latent representations between envi-
ronment variants and the original environment by utilizing
their shared dynamics. For simplicity, we build meta-world
models on the original Pong environment Γo and one of the
ﬁve environment variants separately. We explore training the
shared dynamics on two environments with corresponding
inputs and non-corresponding inputs, i.e., using correspond-
ing states from different environments as training data or
not, to verify the performance of meta-world models.
To collect the training data covering most dynamics of
the Pong environment, we use an agent with random policy
to play the game for 10,000 episodes and limit the episode
length to 1000 steps. The vision model V adopts the same ar-
chitectures as the World Model (Ha and Schmidhuber 2018)
with the latent vector z of size 32. The memory model M is a
LSTM with 32 hidden units to predict the parameters of a di-
agonal Gaussian distribution. The predicted latent represen-
tation of the next state ˜z is then sampled from the Gaussian
distribution. The latent vector encoded by VAE is sampled
from the same Gaussian distribution , making it enough for
an LSTM with one Gaussian prediction to deal with the ex-
periments. We set the batch size for each task as 16 and the
sequence length of LSTM as 25. As described before, we
alternate the training process for V models between mini-
mizing Lr and Lp by setting each training iteration with 20
prediction iterations and 10 reconstruction iterations.
Evaluation Criteria
Each experiment involves two environments (denoted by Γi
and Γj) as we want to validate whether the latent represen-
tations of the corresponding states are identical, or, at least
close enough. Because of the variance introduced by the
VAE, we can indirectly decode the latent representation zi
of the state si from Γi by the decoder f d
j of Γj to ˆsj. The
performance is evaluated by the transformation loss
Lt(Γi, Γj) = ||sj −ˆsj||2,
(11)


## Page 6


(a) Γo and Γt
(b) Γo and Γh
(c) Γo and Γc
(d) Γo and Γm
(e) Γo and Γv
Figure 3: Training meta-world models with corresponding inputs. Legend: p: prediction loss Lp; r: reconstruction loss Lr; t:
transformation loss Lt; pt: predicted transformation loss Lpt.
which is the distance between ˆsj and the real corresponding
states sj.
We also investigate whether the RNN prediction of the
latent representation for each environment shares the same
vector space. We decode the predicted latent representation
˜z′
i of environment Γi using the decoder f d
j of Γj to get
˜s′
j. Similarly, the performance is evaluated by the predicted
transformation loss
Lpt(Γi, Γj) = ||s′
j −˜s′
j||2,
(12)
which is the distance between s′
j and ˜s′
j.
Meta-World Experiments
Corresponding Inputs
In the ﬁrst experiment, we train
two environments with corresponding states as input. How-
ever, we don’t provide meta-world models with any infor-
mation about the type of the transformation between envi-
ronments, thus preventing from simply obtaining the com-
mon representations by direct transformation or supervised
learning. For simplicity, we focus on pair-wise training, i.e.,
ﬁx the original environment Γo and choose one of the ﬁve
variants Γi ∈{Γt, Γh, Γc, Γm, Γv} for each training pro-
cess. At each time step, we randomly sample 16 trajectories
of length 25 from the dataset as the training data for Γo, and
transform these samples to corresponding states as the train-
ing data for Γi, thus making the training input for different
environments already have the same type of dynamics.
We present training results with respect to Lp, Lr, Lt, and
Lpt for each of the ﬁve environment variant to illustrate the
performance of meta-world models. As shown in Fig. 3, the
transformation loss Lt of all experiments could converge to
a relatively low value, which is nearly the same as the recon-
struction loss Lr of the corresponding environment variant;
same results stand for the predicted transformation loss Lpt
and prediction loss Lp as well. At each training step of the
prediction stage, the corresponding inputs setting provides
meta-world models with same types of dynamics from dif-
ferent environments, which are easier to learn by the mem-
ory model. Meanwhile, vision models could learn to adapt to
these shared dynamics simultaneously, thus leading to eas-
ier convergence of meta-world models. With the help of the
memory model predicting corresponding states, vision mod-
els of different environments could understand correspond-
ing states in the same way, i.e., meta-world models could
unify the latent representations of different vision models,
thus possessing the ability to capture the underlying shared
dynamics of different environments.
Non-corresponding Inputs
In the second experiment, we
explore a more humanlike but difﬁcult learning strategy:
learning shared dynamics without knowing the correspond-
ing states, i.e., randomly choosing training data instead of
providing the model with trajectories with same types of dy-
namics as input. Concretely, we split the training set into
two parts and conduct the corresponding transformation on
one part to prepare the training data for Γi. At each time
step, we randomly sample 16 trajectories from each part and
feed them as input to meta-world models. These trajectories
normally present different types of dynamics, which prevent
the memory model from learning corresponding parts of dy-
namics simultaneously from both environments, thus requir-
ing models to ﬁgure out the exact corresponding states and
then learn the shared dynamics.
Similar to experiments with corresponding inputs, we also
present training results with respect to Lp, Lr, Lt, and Lpt
for the original environment and each of the ﬁve variant.
As illustrated in Fig. 4, the convergence results on experi-
ments of Γo and Γi ∈{Γt, Γh, Γc, Γm} prove the effective-
ness of meta-world models in unifying the latent represen-
tations of different environments when training with non-
corresponding inputs, although being slightly worse than
that of using corresponding inputs. This is mainly because
vision models also try to adapt to the memory model with
previous learned dynamics when the memory model is up-
dated during the prediction stage. During the reconstruction
stage, the memory model is in turn prevented from overﬁt-
ting because it needs to predict proper latent representation
˜z′
i to get interpreted by the decoder f d
i of environment Γi.
Thus, meta-world models are able to capture the underly-
ing shared dynamics even though the training process is un-
stable, i.e., both the memory model and vision models are
optimized through ﬂuctuated directions.
Meanwhile, the meta-world model built on Γo and Γv
ﬁnds it hard to capture the shared dynamics when training
with non-corresponding inputs. We consider it may be at-
tributed to the paddle teleportation; in Γv, a paddle can be
divided into two parts where one part could disappear at one
side of the frame and reappear at the other side, resulting in
new properties of split and teleported paddles not existing in
other environments. Fig. 4e illustrates the learning curve of
a successful try to learn the meta-world model on Γo and Γv.


## Page 7


(a) Γo and Γt
(b) Γo and Γh
(c) Γo and Γc
(d) Γo and Γm
(e) Γo and Γv
Figure 4: Training meta-world models without corresponding inputs. Legend: p: prediction loss Lp; r: reconstruction loss Lr;
t: transformation loss Lt; pt: predicted transformation loss Lpt.
(a) log standard deviations
(b) mean L1 distance
Figure 5: Difference between latent vectors zo and zm of
corresponding states from vision models of Γo and Γm.
Analyzing the Shared Dynamics
To explicitly demonstrate the ability of meta-world models
to unify the representation space of different environments,
we provide the visualized results on evaluation set in Ap-
pendix. A. To further investigate the shared dynamics among
different environments, we analyze the difference between
latent representations zo and zm from two environments Γo
and Γm as shown in Fig. 5.
Fig. 5a illustrates the log standard deviations of the vision
models of Γo and Γm respectively, where a small group of
elements (indexed as 7, 13, 19, 20 and 21) has relatively low
variance in both environments, thus keeping relatively stable
value across different observations. Fig. 5b shows the mean
L1 distance of each element from latent representations of
corresponding states between Γo and Γm, where the ele-
ments in the same group are close to each other in the repre-
sentation space between different environments. Being sta-
ble through different observations, these elements also share
high similarity between both environments and can be inter-
preted mutually by both visual models. We consider these
elements as the critical part in representing the shared dy-
namics and deﬁne them as key elements.
To validate the importance of key elements in extracting
the underlying dynamics, we show the weights of the de-
coder neural network f d
o connected to the latent representa-
tions zo in Fig. 6a. As the sum of absolute weights connected
to key elements are much larger than others, the change of
key elements will apply higher inﬂuence to the decoder out-
put ˆso, thus illustrating their signiﬁcance in latent represen-
tations. Also, the value of each element of the decoder output
ˆso ranges from 0 to 1, where pixels of paddles correspond to
high values. We then compute the gradients of the output
ˆso with respect to the latent vector to observe which part of
(a) sum of absolute weights con-
nected to zo in f d
o
(b) mean absolute gradients of
output to zo in f d
o
Figure 6: Validating the importance of key elements.
the latent vector contributes to the paddle more. As shown
in Fig. 6b, the mean absolute gradients of key elements are
signiﬁcantly larger than others. Indeed, other elements have
nearly zero gradients, meaning almost no contributions to
the decoder output ˆso. Consequently, the learned uniﬁed rep-
resentations mainly concentrate on key elements.
Self-Awareness
One of the simple deﬁnitions of self-awareness is the abil-
ity to recognize oneself as an individual separated from the
environment. The mirror self-recognition test (MSR) is the
classical method for attempting to measure self-awareness
(Gallup 1970), where an animal is exposed to mirrors for
the ﬁrst time to test if it can recognize the reﬂected image as
itself, rather than of another animal. Humans are known to
have self-consciousness as they can learn to recognize their
own images after prolonged confrontation with mirrors and
stop responding socially to the reﬂection. Although the rea-
son why animals can achieve this without seeing themselves
before is still under debate, we propose a possible direction;
we think animals with self-consciousness should have the
ability to correlate their own actions to that in the mirror and
perceive the reﬂection as themselves. The inﬂuence of their
actions will have the same impact in both the mirrored en-
vironment and the real world even with different visual ob-
servations, which means two environments share the same
underlying dynamics.
In our experiments, we deﬁne the self-awareness of agents
as the ability to unify the concepts of the agent itself in two
different environments, e.g., Γo and Γm. Our ﬁrst experi-
ment with corresponding inputs can be seen as the Atari
Pong version of the mirror test. When taking an action in Γo,
an agent with meta-world models can predict how will the


## Page 8


mirrored world Γm change with the inﬂuence of this action.
Being able to predict the next observation in a mirrored Pong
game, an agent possesses the ability to distinguish between
the controlled paddle and the opponent paddle by observ-
ing their actions and dynamics, thus recognizing themselves
from the reﬂected mirrored environment.
Meanwhile, the experiment with non-corresponding in-
puts takes a step further, where agents try to ﬁgure out the
correspondence between two environments without know-
ing the exact transformations. This can be seen as the pro-
cess of reasoning about the differences between observa-
tions and searching the common rules among them. Humans
normally understand the world in this way, where the pro-
cess of integrating knowledge involves ﬁnding the shared as-
pects of different observations that progress independently.
Once the common points are found, the conception about
these observations can get uniﬁed in a certain way, thus help-
ing human to enhance their knowledge to better understand
the world.
Conclusions
In this paper, we propose the meta-world models for learning
shared underlying dynamics among visually different envi-
ronments. To propose an engineering approach to mimic the
activity of human brains, which keeps a mental model of
the world developed from the most impoverished of visual
stimuli, we explore building a meta-world model with ba-
sic form of consciousness. We show through extensive ex-
periments that our meta-world model can successfully learn
an abstract description of shared physical dynamics among
different variants of the Atari Pong game, which can be to-
tally different in both state space and transition functions.
We also demonstrate that agents equipped with our meta-
world model possess the ability of visual self-recognition,
i.e., pass the classic mirror self-recognition test (MSR). For
future directions, we would like to explore the ability of our
meta-world model understanding the world by applying it to
more diverse environments. We would also like to combine
the meta-world model with ”model-free” methods to learn
through experience and make inferences and planning more
computationally efﬁcient.
References
[Al-Shedivat et al. 2017] Al-Shedivat, M.; Bansal, T.; Burda, Y.;
Sutskever, I.; Mordatch, I.; and Abbeel, P. 2017. Continuous adap-
tation via meta-learning in nonstationary and competitive environ-
ments. arXiv preprint arXiv:1710.03641.
[Auer, Cesa-Bianchi, and Fischer 2002] Auer, P.; Cesa-Bianchi, N.;
and Fischer, P. 2002. Finite-time analysis of the multiarmed bandit
problem. Machine Learning 47(2):235–256.
[Baker et al. 2017] Baker, C. L.; Jara-Ettinger, J.; Saxe, R.; and
Tenenbaum, J. B. 2017. Rational quantitative attribution of be-
liefs, desires and percepts in human mentalizing. Nature Human
Behaviour 1:0064 EP –.
[Bellemare et al. 2015] Bellemare, M. G.; Naddaf, Y.; Veness, J.;
and Bowling, M. 2015. The arcade learning environment: An eval-
uation platform for general agents. IJCAI’15, 4148–4152. AAAI
Press.
[Clavera et al. 2018] Clavera, I.; Nagabandi, A.; Fearing, R. S.;
Abbeel, P.; Levine, S.; and Finn, C.
2018.
Learning to
adapt: Meta-learning for model-based control.
arXiv preprint
arXiv:1803.11347.
[Dehaene, Lau, and Kouider 2017] Dehaene,
S.;
Lau,
H.;
and
Kouider, S. 2017. What is consciousness, and could machines
have it? Science 358(6362):486–492.
[Duan et al. 2016] Duan, Y.; Schulman, J.; Chen, X.; Bartlett, P. L.;
Sutskever, I.; and Abbeel, P.
2016.
Rl 2: Fast reinforce-
ment learning via slow reinforcement learning.
arXiv preprint
arXiv:1611.02779.
[Finn, Abbeel, and Levine 2017] Finn, C.; Abbeel, P.; and Levine,
S. 2017. Model-agnostic meta-learning for fast adaptation of deep
networks. arXiv preprint arXiv:1703.03400.
[Forrester 1971] Forrester, J. W. 1971. Counterintuitive behavior of
social systems. Theory and Decision 2(2):109–140.
[Frans et al. 2017] Frans, K.; Ho, J.; Chen, X.; Abbeel, P.; and
Schulman, J.
2017.
Meta learning shared hierarchies.
arXiv
preprint arXiv:1710.09767.
[Gallup 1970] Gallup, G. G. 1970. Chimpanzees: Self-recognition.
Science 167(3914):86–87.
[Graves et al. 2016] Graves, A.; Wayne, G.; Reynolds, M.; Harley,
T.; Danihelka, I.; Grabska-Barwi´nska, A.; Colmenarejo, S. G.;
Grefenstette, E.; Ramalho, T.; Agapiou, J.; Badia, A.; Hermann,
K. M.; Zwols, Y.; Ostrovski, G.; Cain, A.; King, H.; Summerﬁeld,
C.; Blunsom, P.; Kavukcuoglu, K.; and Hassabis, D. 2016. Hybrid
computing using a neural network with dynamic external memory.
Nature 538:471 EP –.
[Gretton et al. 2007] Gretton, A.; Borgwardt, K. M.; Rasch, M.;
Sch¨olkopf, B.; and Smola, A. J. 2007. A kernel method for the
two-sample-problem. In Advances in NIPS, 513–520.
[Gu et al. 2016] Gu, S.; Lillicrap, T.; Sutskever, I.; and Levine, S.
2016. Continuous deep q-learning with model-based acceleration.
In ICML, 2829–2838.
[Ha and Schmidhuber 2018] Ha, D., and Schmidhuber, J.
2018.
World models. arXiv preprint arXiv:1803.10122.
[Heider and Simmel 1944] Heider, F., and Simmel, M. 1944. An
experimental study of apparent behavior. The American Journal of
Psychology 57(2):243–259.
[Hochreiter and Schmidhuber 1997] Hochreiter, S., and Schmidhu-
ber, J. 1997. Long short-term memory. Neural Comput. 9(8):1735–
1780.
[Kingma and Welling 2013] Kingma, D. P., and Welling, M. 2013.
Auto-encoding variational bayes. arXiv preprint arXiv:1312.6114.
[Lake et al. 2017] Lake, B. M.; Ullman, T. D.; Tenenbaum, J. B.;
and Gershman, S. J. 2017. Building machines that learn and think
like people. Behavioral and Brain Sciences 40:e253.
[Lake, Salakhutdinov, and Tenenbaum 2015] Lake,
B.
M.;
Salakhutdinov, R.; and Tenenbaum, J. B.
2015.
Human-
level concept learning through probabilistic program induction.
Science 350(6266):1332–1338.
[Lake 2014] Lake, B. M. 2014. Towards more human-like concept
learning in machines: Compositionality, causality, and learning-
to-learn. Ph.D. Dissertation, Massachusetts Institute of Technol-
ogy.
[Leibfried, Kushman, and Hofmann 2016] Leibfried, F.; Kushman,
N.; and Hofmann, K. 2016. A deep learning approach for joint
video frame and reward prediction in atari games. arXiv preprint
arXiv:1611.07078.


## Page 9


[Levine and Abbeel 2014] Levine, S., and Abbeel, P. 2014. Learn-
ing neural network policies with guided policy search under un-
known dynamics. In Advances in Neural Information Processing
Systems, 1071–1079.
[Mnih et al. 2015] Mnih, V.; Kavukcuoglu, K.; Silver, D.; Rusu,
A. A.; Veness, J.; Bellemare, M. G.; Graves, A.; Riedmiller, M.;
Fidjeland, A. K.; Ostrovski, G.; et al. 2015. Human-level control
through deep reinforcement learning. Nature 518(7540):529.
[Parisotto, Ba, and Salakhutdinov 2015] Parisotto, E.; Ba, J. L.; and
Salakhutdinov, R. 2015. Actor-mimic: Deep multitask and transfer
reinforcement learning. arXiv preprint arXiv:1511.06342.
[Schmidhuber 2015] Schmidhuber, J. 2015. On learning to think:
Algorithmic information theory for novel combinations of rein-
forcement learning controllers and recurrent neural world models.
arXiv preprint arXiv:1511.09249.
[Spelke 1990] Spelke, E. S. 1990. Principles of object perception.
Cognitive Science 14(1):29 – 56.
[Sutton 1990] Sutton, R. S. 1990. Integrated architectures for learn-
ing, planning, and reacting based on approximating dynamic pro-
gramming. In Machine Learning Proceedings 1990. Elsevier. 216–
224.
[Teh et al. 2017] Teh, Y.; Bapst, V.; Czarnecki, W. M.; Quan, J.;
Kirkpatrick, J.; Hadsell, R.; Heess, N.; and Pascanu, R.
2017.
Distral: Robust multitask reinforcement learning. In Advances in
NIPS, 4496–4506.
[Turing 1950] Turing, A. M. 1950. Computing machinery and in-
telligence. Mind LIX(236):433–460.
[Van Gulick 2018] Van Gulick, R. 2018. Consciousness. In Zalta,
E. N., ed., The Stanford Encyclopedia of Philosophy. Metaphysics
Research Lab, Stanford University, spring 2018 edition.
[Wahlstr¨om, Sch¨on, and Deisenroth 2015] Wahlstr¨om, N.; Sch¨on,
T. B.; and Deisenroth, M. P.
2015.
From pixels to torques:
Policy learning with deep dynamical models.
arXiv preprint
arXiv:1502.02251.
[Wang et al. 2016] Wang, J. X.; Kurth-Nelson, Z.; Tirumala, D.;
Soyer, H.; Leibo, J. Z.; Munos, R.; Blundell, C.; Kumaran, D.;
and Botvinick, M. 2016. Learning to reinforcement learn. arXiv
preprint arXiv:1611.05763.
[Watter et al. 2015] Watter, M.; Springenberg, J.; Boedecker, J.; and
Riedmiller, M. 2015. Embed to control: A locally linear latent
dynamics model for control from raw images. In Advances in NIPS,
2746–2754.
[Wellman and Gelman 1992] Wellman, H. M., and Gelman, S. A.
1992. Cognitive development: Foundational theories of core do-
mains.
Annual Review of Psychology 43(1):337–375.
PMID:
1539946.


## Page 10


A. Unifying the representation space of different environments
t = 0
t = 1
t = 2
t = 3
t = 4
t = 5
t = 6
t = 7
(a) Γo
(b) Γh
(c) Γt
(d) Γc
(e) Γm
(f) Γv
Figure 7: The visualized results on evaluation set. The ﬁrst column is the observation of environment Γo, which is encoded to
zo by V model Vo. The rest columns correspond to the decoding results of zo from vision models of Γh, Γt, Γc, Γm, Γv.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1804.00062v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1804.00062v1_Visual_Robot_Task_Planning

> Source: 1804.00062v1_Visual_Robot_Task_Planning.pdf

> Pages: 8

---


## Page 1


Visual Robot Task Planning
Chris Paxton1, Yotam Barnoy1, Kapil Katyal1, Raman Arora1, Gregory D. Hager1
Abstract— Prospection, the act of predicting the consequences
of many possible futures, is intrinsic to human planning and ac-
tion, and may even be at the root of consciousness. Surprisingly,
this idea has been explored comparatively little in robotics.
In this work, we propose a neural network architecture and
associated planning algorithm that (1) learns a representation
of the world useful for generating prospective futures after the
application of high-level actions, (2) uses this generative model
to simulate the result of sequences of high-level actions in a
variety of environments, and (3) uses this same representation
to evaluate these actions and perform tree search to ﬁnd a
sequence of high-level actions in a new environment. Models are
trained via imitation learning on a variety of domains, including
navigation, pick-and-place, and a surgical robotics task. Our
approach allows us to visualize intermediate motion goals and
learn to plan complex activity from visual information.
I. INTRODUCTION
Humans are masters at solving problems they have never
encountered before. When attempting to solve a difﬁcult
problem, we are able to build a good abstract models and
to picture what effects our actions will have. Some say
this act — the act of prospection — is the essence of true
intelligence [1]. If we want robots that can plan and act in
general purpose situations just as humans do, this ability
would appear crucial.
As an example, consider the task of stacking a series
of colored blocks in a particular pattern, as explored in
prior work [2]. A traditional planner would view this as a
sequence of high-level actions, such as pickup(block),
place(block,on block), and so on. The planner will
then decide which object gets picked up and in which order.
Such tasks are often described using a formal language such
as the Planning Domain Description Language (PDDL) [3].
To execute such a task on a robot, speciﬁc goal conditions
and cost functions must be deﬁned, and the preconditions
and effects of each action must be speciﬁed. This is a time
consuming manual undertaking [4]. Humans, on the other
hand, do not require that all of this information to be given
to them beforehand. We can learn models of task structure
purely from observation or demonstration. We work directly
with high dimensional data gathered by our senses, such as
images and haptic feedback, and can reason over complex
paths without being given an explicit model or structure.
Ideally, we would learn representations that could be used
for all aspects of the planning problem, that also happen to be
human-interpretable. For example, deep generative models
such as conditional generative adverserial networks (cGANs)
1Department
of
Computer
Science,
The
Johns
Hopkins
Univer-
sity, Baltimore, MD, USA {cpaxton, ybarnoy1, kkatyal2,
rarora8, ghager1}@jhu.edu
𝒙𝟎
𝒉𝟎
𝒙𝒊
𝒉𝒊
𝒉𝒊+𝟏
𝒙𝒊+𝟏
𝒉𝒊+𝟐
𝒙𝒊+𝟐
𝒉𝒊+𝟑
𝒙𝒊+𝟑
Fig. 1: Example of our algorithm using learned policies to predict
a good sequence of actions. Left: initial observation x0 and current
observation xi, plus corresponding encodings h0 and hi. Right:
predicted results of three sequential high level actions.
Input
Predicted Goals
Observed Goals
Fig. 2: Predicting the next step during a suturing task based on
labeled surgical data. Predictions clearly show the next position of
the arms.
allow us to generate realistic, interpretable future scenes [5].
In addition, a recent line of work in robotics focuses on
making structured predictions to inform planning [6], [7]: So
far, however, these approaches focus on making relatively
short-term predictions, and do not take into account high-
level variation in how a task can be performed. Recent work
on one-shot deep imitation learning can produce general-
purpose models for various tasks, but relies on a task solution
from a human expert, and does not generate prospective
future plans that can be evaluated for reliable performance
in new environments [2]. These approaches are very data
intensive: Xu et al. [2] used 100,000 demonstrations for their
block-stacking task.
We propose a supervised model that learns high-level
task structure from imperfect demonstrations. Our approach
then generates interpretable task plans by predicting and
evaluating a sequence of high-level actions, as shown in
Fig. 1. Our approach learns a pair of functions fenc and fdec
that map into and out of a lower-dimensional hidden space
arXiv:1804.00062v1  [cs.RO]  30 Mar 2018


## Page 2


H, and then learns a set of other functions that operate on
values in this space. Models are learned from labeled training
data containing both successes and failures, are not reliant
on a large number of good expert examples, and work in
a number of domains including navigation, pick-and-place,
and robotic suturing (Fig. 2). We also describe a planning
algorithm that uses these results to simulate a set of possible
futures and choose the best sequence of high-level actions to
execute, resulting in realistic explorations of possible futures.
To summarize, our contributions are:
• A network architecture and training methodology for
learning a deep representation of a planning task.
• An algorithm to employ this planning task to generate
and evaluate sequences of high-level actions.
• Experiments demonstrating the model architecture and
algorithm on multiple datasets.
Datasets and source code will be made available upon
publication.
II. RELATED WORK
Motion Planning: In robotics, effective TAMP approaches
have been developed for solving complex problems involving
spatial reasoning [8]. A subset of planners focused on Par-
tially Observed Markov Decision Process extend this capabil-
ity into uncertain worlds; examples include DeSPOT, which
allows manipulation of objects in cluttered and challenging
scenes [9]. These methods rely on a large amount of built-
in knowledge about the world, however, including object
dynamics and grasp locations.
A growing number of works have explored the integration
of planning and deep neural networks. For example, QMDP-
nets embed learning into a planner using a combination
of a ﬁlter network and a value function approximator net-
work [10]. Similarly, value iteration networks embed a differ-
entiable version of a planning algorithm (value iteration) into
a neural network, which can then learn navigation tasks [11].
Vezhnevets proposed to generate plans as sequences of
actions [12]. Other prior work employed Monte Carlo Tree
Search (MCTS) together with a set of learned action and
control policies for task and motion planning [13], but did
not incorporate predictions.
Prediction is intrinsic to planning in a complex world.
While most robotic motion planners assume a simple causal
model of the world, recent work has examined learning
predictive models. Lotter et al. [14] propose PredNet as a
way of predicting sequences of images from sensor data,
with the goal of predicting the future, and Finn et al. [7]
use unsupervised learning of predictive visual models to
push objects around in a plane. However, to the best of our
knowledge, ours is the ﬁrst work to use prospection for task
planning.
Learning Generative Models.: GANs are widely consid-
ered the state of the art in learned image generation [15],
[16], though they are far from the only option. The Wasser-
stein GAN is of particular note as an improvement over other
GAN architectures [16]. Isola et al. proposed the PatchGAN,
which uses an average adversarial loss over “patches” of the
image, together with an L1 loss on the images as a way
of training conditional GANs to produce one image from
another [5].
Prior work has examined several ways of generating
multiple realistic predictions [15], [17], [18]. The authors
in [19] demonstrated the advantage of applying adversarial
methods to imitation learning. More recently, [18] proposed
to learn a deep predictive network that uses a stochastic
policy over goals for manipulation tasks, but without the
goal of additionally predicting the future world state.
Learning Representations for Planning: Sung et al. [20]
learn a deep multimodal embedding for a variety of tasks.
This representation allows them to adapt to appliances with
different interfaces while reasoning over trajectories, nat-
ural language descriptions, and point clouds for a given
task. Finn et al. [6] learn a deep autoencoder as a set of
convolutional blocks followed by a spatial softmax; they
found that this representation was useful for reinforcement
learning. Recently, Higgins et al. [21] proposed DARLA, the
DisentAngled Representation Learning Agent, which learns
useful representations for tasks that enable generalization to
new environments. Interpretability and predicting far into the
future were not goals of these approaches.
III. APPROACH
We deﬁne a planning problem with continuous states x ∈
X, where x contains observed information about the world
such as a camera image. We augment this state with high-
level actions a ∈A that describe the task structure. We also
assume that the hidden world state h ∈H should encode both
task information (such as goals) and the underlying ground
truth input from the various sensors. For example, in the
block-stacking task in Fig. 1, h encodes the positions of the
four blocks, the obstacle and the conﬁguration of the arm.
Our objective is to learn a set of models representing the
necessary components of this planning problem, but acting in
this latent space H. In other words, given a particular action
a and an observed state x, we want to be able to predict both
an end state x′ and the optimal sequence of actions a ∈A∗
necessary to take us there. We speciﬁcally propose that there
are three components of this prediction function:
1. fenc(x) →h ∈H, a learned encoder function maps
observations and descriptions to the hidden state.
2. fdec(h) →(x), a decoder function that maps from the
hidden state of the world to the observation space.
3. T(h, a) →h′ ∈H, the i-th learned world state trans-
formation function, which maps to different positions
in the space of possible hidden world states.
Speciﬁcally, we will ﬁrst learn an action subgoal predic-
tion function, which is a mapping fdec(T(fenc(x), a)) →
(x′). In practice, we include the hidden state of the ﬁrst
world observation as well in our transform function, in order
to capture any information about the world that may be
occluded. This gives the transform function the form:
T(h0, h, a) →h′ ∈H


## Page 3


Fig. 3: Overview of the prediction network for visual task planning. We learn fenc(x), fdec(x), and T(h, a) to be able to predict and
visualize results of high-level actions.
We assume that the hidden state h contains all the neces-
sary information about the world to make high level decisions
as long as this h0 is available to capture change over time. As
such, we learn additional functions representing the value of
a given hidden state, the predicted value of actions moving
forward from each hidden state, and connectivity between
hidden states. Given these components, we can appropriately
represent the task as a tree search problem.
A. Model Architecture
Fig. 3 shows the architecture for visual task planning.
Inputs are two images x0 and xi: the initial frame when
the planning problem was ﬁrst posed, and the current frame.
We include x0 and h0 to capture occluded objects and
changes over time from the beginning of the task. In Fig. 3,
hidden states h0, hi, hj, hk are represented by averaging
across channels.
Encoder and Decoder. The ﬁrst training step ﬁnd the
transformations into and out of the learned hidden space
H. Speciﬁcally, we train fenc and fdec using the encoder-
decoder architecture shown in Fig. 4. Convolutional blocks
are indicated with Ck, where k is the number of ﬁlters.
Most of our layers are 5 × 5 convolutions, although we used
a 7 × 7 convolution on the ﬁrst layer and we use 1 × 1
convolutions to project into and out of the hidden space.
Each convolution is followed by an instance normalization
and a ReLU activation. Stride 2 convolutions and transpose
convolutions are then used to increase or decrease image size
after each block. The ﬁnal projection into the hidden state
has a sigmoid activation in place of ReLU and is not paired
with a normalization layer. In most of our examples, this
hidden space is scaled down to an 8 × 8 × 8 space.
Both dropout and normalization played an important role
in learning fast, accurate models for encoding the hidden
state, but we use the instance norm instead of the more
common batch normalization in order to avoid issues with
dropout. After every block, we add a dropout layer D, with
dropout initially set to 10%. Instance normalization has been
found useful for image generation in the past [22]. We do
not apply dropout at test time except with GANs.
Transform function. T(h0, h, a) computes the most likely
next hidden state. This function was designed to combine
information about the action and two observed states, and to
compute global information over the entire hidden space. We
use the spatial soft argmax previously employed by Finn and
Levine. [6], [23] and Ghadirzadeh et al. [18] to compute a set
of keypoints, which we then concatenate with a high-level
action label and use to predict a new image. This is sufﬁcient
to capture the next action with a good deal of ﬁdelity (see
Sec. V-B), but to capture background details we add a skip
connection across this spatial soft argmax bottleneck.
Fig. 5 shows the complete transform block as used in the
block stacking and navigation case studies described below.
For the suturing case study, with a larger input and hidden
space, we add an extra set of size 64 convolutions to each
side of the architecture and a corresponding skip connection,
but it is otherwise the same.
Each dense layer is followed by a ReLU nonlinearity. The
ﬁnal projection into the hidden state also has a sigmoid
activation and no instance normalization layer, as in the
encoder.
Value functions. V (h) computes the value of a particular
hidden state h as the probability the task will be successful
from that point onwards, and Q(h0, h, a, a′) predicts the
probability that taking action a′ from the tree search node
(h0, h, a) will be successful. These are trained based on
{0, 1} labels indicating observed task success and observed
failures. We also train the function f(h0, h, a) which predicts
whether or not an action a successfully ﬁnished.
Structure prior. Value functions do not necessarily indi-
cate what happens if there are no feasible actions from a
particular state. To handle this, we learn the permissability
function p(a′|h0, h, a), which states that it is possible for a′
to follow a, but does not state whether or not a′ will succeed.
These last four models are trained on supervised data, but
without the instance normalization in femc, fdec, and T, as


## Page 4


Fig. 4: Encoder-decoder architecture used for learning a transform into and out of the hidden space h.
Fig. 5: Architecture of the transform function T(h0, h, a) for computing transformations to an action subgoal in the learned hidden space.
we saw this hurt performance. Q, p, and f were trained with
two 1 × 1 convolutions on h and h0, then a concatenated,
followed by C64 −C64 −FC256 −FC128, where FCk is
a fully connected layer with k neurons. The value function
V (h) was a convolutional neural net of the form C32 −
C64 −C128 −FC128.
B. Learning
We train our predictor directly on supervised pairs contain-
ing the state x′ = fdec(T(fenc(x), a)) resulting from action
a. First, we considered a simple L1 loss on the output images.
However, this might not capture all details of complex
scenes, so we also train with an augmented loss which
encourages correct classiﬁcation of the resulting image. This
approach is in some ways similar to that used by [15], in
which the authors predict images while minimizing distance
in a feature space trained on a classiﬁcation problem. Here,
we use a combination of an L1 term and a term maximizing
the cross-entropy loss on classiﬁcation of the given image,
which we refer to as the L1+λC loss in the following, where
λ is some weight. Finally, we explored using two different
GAN losses: the Wasserstein GAN [16] and the pix2pix
GAN from Isola et al. [5].
First we train the goal classiﬁer C(x) on labeled training
data for use in testing and in training our augmented loss.
Next we train the encoder and decoder structure fenc(x) and
fdec(x), which provide our mapping in and out of the hidden
world state. Finally we train the transform function T(h, a)
and the evaluation functions used in our planning algorithm.
Transform Training. To encourage the model to make
predictions that remain consistent over time, we link two
consecutive transforms with shared weights, and train on the
sum of the L1 loss from both images, with the optional
classiﬁer loss term applied to the second image. The full
training loss given ground truth predictions ˆx1, ˆx2 is then:
L(x1, x2) = ∥ˆx1 −x1∥1 + ∥ˆx2 −x2∥1 + λC(x2)
Implementation. All models were implemented in Keras
and trained using the Adam optimizer, except for the Wasser-
stein GAN, which we trained with RMSProp as per prior
work [16]. We performed multiple experiments to set the
learning and dropout rates in our models, and selected a
relatively low learning rate of 1e −4 and dropout rate of
0.1, which strikes a balance between regularization and crisp
per-pixel predictions when learning the hidden state.
C. Visual Planning with Learned Representations
We use these models together with Monte Carlo Tree
Search (MCTS) in order to ﬁnd a sequence of actions that
we believe will be successful in the new environment. The
general idea is that we run a loop where we repeatedly
sample a possible action a′ according to the learned function
Q(h0, h, a, a′) and use this action to simulate the effects
of that high-level action T(h0, h, a′). We can then execute
the sequence of learned or provided black box policies to
complete the motion on the robot.
We propose a variant of MCTS as a general way of
exploring the tree over possible actions [13]. We represent
each node in the tree by a unique instance of a high-level
action (∅for the root). The full algorithm is described in
Alg. 1.
The EVALUATE function sets vi = V (h), but also checks
the validity of the chosen action and determines which
actions can be sampled. We also compute f(h0, h, a) to
determine if the robot would succesfuuly complete the action
with some conﬁdence cdone. If not this is considered a failure
(vi = 0). If v′ < vfailed, we will halt exploration.


## Page 5


Algorithm 1 Algorithm for visual task planning with a
learned state representation.
Given: max depth d, initial state x0, current state x, number of
samples Nsamples
h = fenc(x), h0 = h
for i ∈Nsamples do
EXPLORE(h0,h,∅,0,d)
end for
function EXPLORE(h0,h,a,i,d)
vi = EVALUATE(h0, h, a)
if i ≥d or vi < vfailed then return vi end if
a′ = SAMPLE(h0, h, a)
h′ = T(h0, h, a′)
v′ = EXPLORE(h0,h′,a′,i + 1,d)
UPDATE(a, a′, v′)
return vi · v′
end function
The SAMPLE function greedily chooses the next action a′
to pursue according to a score v(a, a′):
v(a, a′) = cQ(h0, h, a, a′)
N(a, a′)
+ v∗(a, a′)
where Q is the learned action-value function, N(a, a′) is
the number of times a′ was visited from a, and v∗(a, a′)
is the best observed result from taking a′. We set c = 10
to encourage exploration to actions that are expected to be
good. The UPDATE function is responsible for incrementing
N(a, a′). Sampled actions a′ are rejected if we predict a′ is
not reachable from its parent.
IV. EXPERIMENTAL SETUP
We applied the proposed method to both a simple navi-
gation task using a simulated Husky robot, and to a UR5
block-stacking task. 1
In all examples, we follow a simple process for collecting
data. First, we generate a random world conﬁguration, de-
termining where objects will be placed in a given scene.
The robot is initialized in a random pose as well. We
automatically build a task model that deﬁnes a set of control
laws and termination conditions, which are used to generate
the robot motions in the set of training data. Legal paths
through this task model include any which meet the high-
level task speciﬁcation, but may still violate constraints (due
to collisions or errors caused by stochastic execution).
We include both positive and negative examples in our
training data. Training was performed with Keras [24] and
Tensorﬂow 1.5 for 45,000 iterations on an NVidia Titan Xp
GPU, with a batch size of 64. Training took roughly 200 ms
per batch.
A. Robot Navigation
In the navigation task, we modeled a Husky robot moving
through a construction site environment to investigate one
of four objects: a barrel, a barricade, a construction pylon
or a block, as shown in Fig. 6(left). The goal was to ﬁnd
a path between different objects, so that it takes less then
1Source code for all examples will be made available after publication.
Fig. 6: Simulation experiments. Left: Husky navigation task. The
robot is highlighted. Right: UR5 block-stacking task with obstacle
avoidance.
ten seconds to move between any two objects. Here, x was
a 64x64 RGB image that provides an aerial view of the
environment. Data was collected using a Gazebo simulation
of the robot navigating to a randomly-chosen sequence of
objects. We collected 208 trials, of which 128 were failures.
B. Simulated Block Stacking
To analyze our ability to predict goals for task planning,
we learn in a more elaborate environment. In the block
stacking task, the robot needed to pick up a colored block
and place it on top of any other colored block. The robot
succeeds if it manages to stack any two blocks on top of
one another and failed immediately if either it touches this
obstacle or if at the end of 30 seconds the task has not
been achieved. Training was performed on a relatively small
number of examples: we used 6020 trials, of which 2991
were successful and 3029 were failures. The state x is a
64×64 RGB image of the scene from a ﬁxed external camera.
We provided a set of non-optimal expert policies and
randomly sampled a set of actions. This task was fairly com-
plicated, with a total of 36 possible actions divided between
two sub-tasks. Separate high-level actions were provided
for aligning the gripper with an object, moving towards
a grasp, closing the gripper, lifting an object, aligning a
block with another block below it, stacking the currently
held block on another, opening the gripper, and returning
to the home position. These were provided for each of four
colored blocks the robot could manipulate: the actions were
either parameterized by the block to pick up (the ﬁrst four
steps) or the block to stack on top of (the last four steps).
Each performance was labeled a failure if either (a) it
took more than 30 seconds, (b) there was a collision with the
obstacle, or (c) the robot moved out of the workspace for any
reason. The simulation was implemented in PyBullet, and
was designed to be stochastic and unpredictable. At times
the robot would drop the currently-held block, or it would
fail to accurately place the block held in its hands. There
was also some noise in the simulated images.
C. Surgical Robot Image Prediction
Next, we explored our ability to predict the goal of the next
motion on a real-world surgical robot problem. Minimally
invasive surgery is a highly skilled task that requires a great
deal of training; our image prediction approach could allow
novice users some insight into what an expert might do


## Page 6


Fig. 7: Learned hidden state representations for the simulated
stacking task (left) and navigation task (right).
in their situation. There is a growing amount of surgical
robot video available, and a growing body of work seeks
to capitalize on this to improve video prediction [25]. We
used a subset of the JIGSAWS dataset to train a variant of
our Visual Task Planning models on a labeled suturing task
in order to predict the results of certain motions.
The JIGSAWS dateset consists of stereo video frames,
with each pair labeled as belonging to one of 15 possible
gestures. For our task, We used only the left frames of the
video stream. The dataset contains the 3 tasks of suturing,
know tying, and needle passing, with each task consisting
of a subset of gestures. We reduced the image dimensions
from 640 × 480 to a more reasonable 96 × 128. For this
application, we used a slightly larger 12 × 16 × 8 hidden
representation. Fig. 12 shows examples of the pretrained fenc
and fdec functions.
V. RESULTS
Our models are able to generate realistic predictions of
possible futures for several different tasks, and can use these
predictions to make intelligent decisions about how they
should move to solve planning problems. See Fig. 1 above
for an example: we give the model input images x0 and xi,
and see realistic results as it peforms three actions: lifting
closing the gripper, picking up the green block, and placing
it on top of the blue block. In the real data set, this action
failed because the robot attempted to place the green block
on the red block (next to an obstacle), but here it makes a
different choice and succeeds. We visualize the 8 × 8 × 8
hidden layer by averaging cross the channels.
A. Learned Hidden State
The state learned by our encoder-decoder contains in-
formation representing possible objects and positions. We
compared use of the hidden state representation learned on
our data set with models trained for speciﬁc tasks on different
models. Fig. 7 shows the lower-dimensional hidden state
representation used by the predictive model. In the stacking
task, we can see how different features change dramatically
as objects are moved about in the scene. In the simpler
navigation task, only the Husky robot changes position. In
this case, many of the features are likely redundant.
To
visualize
the
effects
of
the
transform
function
T(h0, h, a) on the learned hidden state, we randomly sam-
pled a number of hidden states and repeatedly applied
T(h0, h, a) with random actions. After 200 steps, we see
results similar to those in Fig. 8, with objects and the arm
positioned randomly in the scene. From left to right, these
Fig. 8: Randomly sampled hidden states projected onto the manifold
of the transform function T(h0, h, a).
No Skip Connections
No Classifier Loss
With Classifier Loss
Fig. 9: Selected results different possible architectures for the
Transform block.
show (1) the randomly sampled hidden state, (2) a decoding
of this hidden state, (3) a hidden state after 200 random
transform operations, and (4) the decoded version of this
hidden state.
B. Model Architecture
We performed a set of experiments to verify our model
architecture, particularly in comparing different versions of
the transform block T. We compare three different options:
the block as shown in Fig. 5, the same block with the skip
connection removed, and the same block with the spatial
softmax and dense block replaced by a stride 2 and a stride
1 convolution to make a more traditional U-net similar to
that used in prior work [5].
To compare model architectures and training strategies,
we propose a simple metric: given a single frame, can we
determine which action just occurred? This is computed
given the same pretrained discriminator discussed in Sec. III-
B. We compare versions of the loss function with and without
the classiﬁer loss term, and with this term given one of
two possible weights. Both the classiﬁer loss term and the
conditional GAN discriminator term were applied to the
second of two transforms, to encourage the model to generate
predictions that remained consistent over time.
Tables I and II show the results of this comparison.
There were 37453 example frames from successful examples
and 54077 total examples in the data set. In general, the
pretrained encoder-decoder structure allowed us to reproduce
high-quality images in all of our tasks. The “Naive” model
indicates L1 loss with only one prediction; it performs


## Page 7


Model
x1 label
x1 error
x2 label
x2 error
Naive
87.2%
0.0161
74.3%
0.0261
L1
88.1%
0.016
84.5%
0.018
L1+0.01C
87.9%
0.0177
94.3%
0.0214
L1+0.001C
88.2%
0.016
85.4%
0.0184
No Skips
87.5%
0.0224
85.4%
0.0247
cGAN [5]
84.5%
0.0196
77.5%
0.0235
TABLE I: Comparison of test losses as assessed by image prediction
error (MAE) and image confusion on successful examples only.
Model
x1 label
x1 error
x2 label
x2 error
Naive
89.3%
0.0182
77.3%
0.0276
L1
90.4%
0.0181
86.4%
0.0209
L1+0.01C
90.6%
0.0198
95.6%
0.0239
L1+0.001C
90.9%
0.0181
88.6%
0.0208
No Skips
90.1%
0.0243
89.3%
0.0271
cGAN [5]
86.5%
0.0216
79.9%
0.0260
TABLE II: Comparison of test losses as assessed by image predic-
tion error (MAE) and image confusion.
notably worse than other models due to errors accumulating
over subsequent applications of T(h0, h, a).
The classiﬁer loss term improved the quality of predictions
on the second example, and improved crispness of results,
at the slight cost of some pixel-wise error on the output
images. Here, we see that adding the classiﬁer loss terms
(L1+0.01C and L1+0.001C) slightly improved recognition
performance looking forward in time. This corresponds with
increasing image clarity corresponding to the ﬁngers of the
robot’s gripper in particular. Pose and texture differences
largely explain the differences in per-pixel error.
The “No Skips” model was trained the same as the
L1+0.001C model, but without the skip connections in
Fig. 5. These connections allow us to ﬁll in background
detail correctly (see Fig. 9), but were not necessary for the
key aspects of any particular action.
The cGAN was able to capture feasible texture, but
often missed or made mistakes on spatial structure. It often
misplaced blocks, for example, or did not hallucinate them
at all after a placement action. This may be because of the
noisy data and the large number of failures.
C. Plan Evaluation
Our approach is able to generate feasible action plans in
unseen environments and to visualize them; see Fig. 10 for an
example. The ﬁrst two plans are recognized as failures, and
then the algorithm correctly ﬁnds that it can pick up the red
block and place it on the blue without any issues. The value
function V (h) correctly identiﬁed frames as coming from
successful or failed trials 83.9% of the time after applying
two transforms – good, considering that it is impossible to
differentiate between success and failure from many frames.
It correctly classiﬁed possible next actions 96.0% of the time.
At each node in our tree search, we examine multiple
possible futures. This is important both for planning and
for usability: it allows our system to justify future results.
Fig. 11 shows examples of these predictions in different
environments. We see how the system will predict a set
of serious failures in the middle row, when attempting to
grasp the red or blue blocks, and one possible failure when
grasping the yellow block.
We tested our method on 10 new test environments in the
stacking task. On each of these environments, we performed
a search with 10 samples. Our approach found 8 solutions to
planning tasks executing the demonstrated high-level actions,
and in 2 tasks it predicted that all of its actions would result
in failures, due to proximity to the obstacle. This highlights
an advantage of the visual task planning approach: in the
event of a failure, the robot provides a clear explanation for
why (see the second sample in Fig. 10 for an example).
D. Surgical Image Prediction
We trained our network on 36 examples in the JIGSAWS
dataset, leaving out 3 for validation. We were able to generate
predictions that clearly showed the location of the arms after
the next gesture, as shown in Fig. 2. The learned space H
is very expressive, but loses some ﬁne details such as the
thread at times; see Fig. 12. The result of fdec(fenc(x)) still
has almost all the same detail as the goal image (right).
Image prediction created recognizable gestures, such as
pulling the thread after a suture. While our results are
visually impressive, error was higher than in the robotic
manipulation task: we saw mean absolute error of 0.039 and
0.062 for generated images x1 and x2, respectively. This is
likely because the surgical images contain a lot more subtle
but functionally irrelevant data that is not fully reconstructed
by our transform. It therefore looks “good enough” for
human perception, but does not compare as well at a pixel-
by-pixel level. In addition, there is high variability on the
performance of each action and a relatively small amount of
avaiable data.
Again, the cGAN did not have a measurable impact: MAE
of 0.039 and 0.067 across the three test examples. As such,
the longer training time of the cGAN does not seem justiﬁed.
In general, it appears to us that conditional GANs are good
at modifying texture, but not necessarily at hallucinating
completely new image structure.
VI. CONCLUSIONS
We described an architecture for visual task planning,
which learns an expressive representation that can be used
to make meaningful predictions forward in time. This can
be used as part of a planning algorithm that explores multi-
ple prospective futures in order to select the best possible
sequence of future actions to execute. In the future we
will apply our method to real robotic examples and expand
experiments on surgical data.
ACKNOWLEDGMENTS
This research project was conducted using computational
resources at the Maryland Advanced Research Computing
Center (MARCC). It was funded by NSF grant no. 1637949.
The Titan Xp used in this work was donated by the NVIDIA
Corporation.


## Page 8


𝒙𝟎
𝒙𝟏
𝒙𝟐
𝒙𝟑
Fig. 10: First three results from a call of the planning algorithm on a random environment.
Input
Predicted Goals
Fig. 11: Analyzing parallel possible futures for the stacking and
navigation tasks. Top row shows multiple good options for grasping
separate objects; the second shows how attempts to grab two objects
are clear failures and only one is a clear success.
Fig. 12: Results of the pretraining step show that our encoder/de-
coder architecture can accurately capture all the relevant detail even
in noisy, complex scenes.
REFERENCES
[1] M.
E.
P.
Seligman,
P.
Railton,
R.
F.
Baumeister,
and
C.
Sripada,
“Navigating
into
the
future
or
driven
by
the
past,”
Perspectives
on
Psychological
Science,
vol.
8,
no.
2,
pp.
119–141,
2013,
pMID:
26172493.
[Online].
Available:
https://doi.org/10.1177/1745691612474317
[2] D. Xu, S. Nair, Y. Zhu, J. Gao, A. Garg, L. Fei-Fei, and S. Savarese,
“Neural task programming: Learning to generalize across hierarchical
tasks,” arXiv preprint arXiv:1710.01813, 2017.
[3] M. Ghallab, C. Knoblock, D. Wilkins, A. Barrett, D. Christian-
son, M. Friedman, C. Kwok, K. Golden, S. Penberthy, D. E.
Smith et al., “PDDL-the planning domain deﬁnition language,”
http://www.citeulike.org/group/13785/article/4097279, 1998.
[4] M. Beetz, D. Jain, L. Mosenlechner, M. Tenorth, L. Kunze, N. Blodow,
and D. Pangercic, “Cognition-enabled autonomous robot control for
the realization of home chore task intelligence,” Proceedings of the
IEEE, vol. 100, no. 8, pp. 2454–2471, 2012.
[5] P. Isola, J. Zhu, T. Zhou, and A. A. Efros, “Image-to-image translation
with conditional adversarial networks,” CoRR, vol. abs/1611.07004,
2016. [Online]. Available: http://arxiv.org/abs/1611.07004
[6] C. Finn, X. Y. Tan, Y. Duan, T. Darrell, S. Levine, and P. Abbeel,
“Deep spatial autoencoders for visuomotor learning,” in ICRA. IEEE,
2016, pp. 512–519.
[7] C. Finn, I. Goodfellow, and S. Levine, “Unsupervised learning for
physical interaction through video prediction,” in Advances in Neural
Information Processing Systems, 2016, pp. 64–72.
[8] M. Toussaint, “Logic-geometric programming: An optimization-based
approach to combined task and motion planning,” in IJCAI, 2015.
[9] J. K. Li, D. Hsu, and W. S. Lee, “Act to see and see to act: POMDP
planning for objects search in clutter,” in IROS.
IEEE, 2016, pp.
5701–5707.
[10] P. Karkus, D. Hsu, and W. S. Lee, “Qmdp-net: Deep learning for plan-
ning under partial observability,” arXiv preprint arXiv:1703.06692,
2017.
[11] A. Tamar, Y. Wu, G. Thomas, S. Levine, and P. Abbeel, “Value
iteration networks,” in Advances in Neural Information Processing
Systems, 2016, pp. 2154–2162.
[12] A. Vezhnevets, V. Mnih, S. Osindero, A. Graves, O. Vinyals, J. Aga-
piou et al., “Strategic attentive writer for learning macro-actions,” in
Advances in Neural Information Processing Systems, 2016, pp. 3486–
3494.
[13] C. Paxton, V. Raman, G. D. Hager, and M. Kobilarov, “Combining
neural networks and tree search for task and motion planning in
challenging environments,” 2017.
[14] W. Lotter, G. Kreiman, and D. Cox, “Deep predictive coding net-
works for video prediction and unsupervised learning,” arXiv preprint
arXiv:1605.08104, 2016.
[15] Q. Chen and V. Koltun, “Photographic image synthesis with cascaded
reﬁnement networks,” arXiv preprint arXiv:1707.09405, 2017.
[16] M. Arjovsky, S. Chintala, and L. Bottou, “Wasserstein GAN,” stat,
vol. 1050, p. 9, 2017.
[17] C. Rupprecht, I. Laina, R. DiPietro, M. Baust, F. Tombari, N. Navab,
and G. D. Hager, “Learning in an uncertain world: Representing
ambiguity through multiple hypotheses,” ICCV, 2017.
[18] A. Ghadirzadeh, A. Maki, D. Kragic, and M. Bj¨orkman, “Deep
predictive policy training using reinforcement learning,” 2017.
[19] J. Ho and S. Ermon, “Generative adversarial imitation learning,” in
Advances in Neural Information Processing Systems, 2016, pp. 4565–
4573.
[20] J. Sung, S. H. Jin, I. Lenz, and A. Saxena, “Robobarista: Learning
to manipulate novel objects via deep multimodal embedding,” arXiv
preprint arXiv:1601.02705, 2016.
[21] I. Higgins, A. Pal, A. A. Rusu, L. Matthey, C. P. Burgess, A. Pritzel,
M. Botvinick, C. Blundell, and A. Lerchner, “DARLA: Improv-
ing zero-shot transfer in reinforcement learning,” arXiv preprint
arXiv:1707.08475, 2017.
[22] D. Ulyanov, A. Vedaldi, and V. Lempitsky, “Improved texture net-
works: Maximizing quality and diversity in feed-forward stylization
and texture synthesis,” in Proc. CVPR, 2017.
[23] S. Levine, C. Finn, T. Darrell, and P. Abbeel, “End-to-end training
of deep visuomotor policies,” Journal of Machine Learning Research,
vol. 17, no. 39, pp. 1–40, 2016.
[24] F. Chollet, “Keras,” https://github.com/fchollet/keras, 2015.
[25] S. S. Vedula, A. O. Malpani, L. Tao, G. Chen, Y. Gao, P. Poddar,
N. Ahmidi, C. Paxton, R. Vidal, S. Khudanpur et al., “Analysis of the
structure of surgical activity for a suturing and knot-tying task,” PloS
one, vol. 11, no. 3, p. e0149174, 2016.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
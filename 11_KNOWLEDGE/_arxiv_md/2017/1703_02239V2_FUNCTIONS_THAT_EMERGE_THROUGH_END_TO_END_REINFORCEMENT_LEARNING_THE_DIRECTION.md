---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1703.02239v2
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1703.02239v2_Functions_that_Emerge_through_End-to-End_Reinforcement_Learning_-_The_Direction_

> Source: 1703.02239v2_Functions_that_Emerge_through_End-to-End_Reinforcement_Learning_-_The_Direction_.pdf

> Pages: 5

---


## Page 1


arXiv:1703.02239v2  [cs.AI]  16 May 2017
Functions that Emerge through End-to-End Reinforcement Learning
— The Direction for Artiﬁcial General Intelligence —
Katsunari Shibata∗
Department of Innovative Engineering
Oita University
700 Dannoharu, Oita 870-1192, JAPAN
katsunarishibata@gmail.com
Abstract
Recently, triggered by the impressive results in TV-games or game of Go by Google DeepMind, end-to-end reinforcement
learning (RL) is collecting attentions. Although little is known, the author’s group has propounded this framework for
around 20 years and already has shown a variety of functions that emerge in a neural network (NN) through RL. In this
paper, they are introduced again at this timing.
“Function Modularization” approach is deeply penetrated subconsciously. The inputs and outputs for a learning system
can be raw sensor signals and motor commands. “State space” or “action space” generally used in RL show the existence
of functional modules. That has limited reinforcement learning to learning only for the action-planning module. In order
to extend reinforcement learning to learning of the entire function on a huge degree of freedom of a massively parallel
learning system and to explain or develop human-like intelligence, the author has believed that end-to-end RL from
sensors to motors using a recurrent NN (RNN) becomes an essential key. Especially in the higher functions, since their
inputs or outputs are difﬁcult to decide, this approach is very effective by being free from the need to decide them.
The functions that emerge, we have conﬁrmed, through RL using a NN cover a broad range from real robot learning with
raw camera pixel inputs to acquisition of dynamic functions in a RNN. Those are (1)image recognition, (2)color constancy
(optical illusion), (3)sensor motion (active recognition), (4)hand-eye coordination and hand reaching movement, (5)ex-
planation of brain activities, (6)communication, (7)knowledge transfer, (8)memory, (9)selective attention, (10)prediction,
(11)exploration. The end-to-end RL enables the emergence of very ﬂexible comprehensive functions that consider many
things in parallel although it is difﬁcult to give the boundary of each function clearly.
Keywords: function emergence, end-to-end reinforcement learning (RL), recurrent neural network (RNN),
higher functions, artiﬁcial general intelligence (AGI)
Acknowledgements
This research has been supported by JSPS KAKENHI Grant Numbers JP07780305, JP08233204, JP13780295, JP15300064,
JP19300070 and many our group members
∗http://shws.cc.oita-u.ac.jp/˜shibata/home.html


## Page 2


1
Introduction
Recently, triggered by the impressive results in TV-games[1, 2] or game of Go[3] by Google DeepMind, the ability of
reinforcement learning (RL) using a neural network (NN) and the importance of end-to-end RL is collecting attentions.
One remarkable point especially in the results in TV-games is the gap such that even though the inputs of a deep NN
are raw image pixels without any pre-processing and the NN is just learned through RL, the ability acquired through
learning extends to the excellent strategies for several games. The learning do not need special knowledge about learned
tasks and necessary functions emerge through learning, and so it is strongly expected to open the way to the Artiﬁcial
General Intelligence (AGI) or Strong AI.
It has been general that a NN is considered as just a non-linear function approximator for RL, and a recurrent neural
network (RNN) is used to avoid POMDP (Partially Observable Markov Decision Problem). Under such circumstances,
the origin of the end-to-end RL can be found in the Tesauro’s work called TD-gammon[4]. The author’s group is the
only one who has propounded this framework consistently for around 20 years using sometimes the symbolic name of
“Direct-Vision-based Reinforcement Learning”[7, 8] and has shown already a variety of functions that emerge in a NN
or RNN through RL[9] although little is known about them unfortunately.
In this paper, the author’s unwavering direction that end-to-end RL becomes an important key for explaining human
intelligence or developing human-like intelligence especially for the higher functions is introduced at ﬁrst. It is also
shown that a variety of functions emerge through end-to-end (oriented) RL; from real robot learning with raw camera
pixel inputs to acquisition of dynamic functions in an RNN. All of the works here have been published already, but the
author believes that it is worthwhile to know what functions emerge and what functions hardly emerge at this timing
when the end-to-end RL begins to be focused on.
2
The Direction for Human-like General Intelligence
There is probably little doubt that human intelligence is realized thanks to the massively parallel and cohesively ﬂexible
processing on a huge degree of freedom in our brain. On the other hand, unlike in the case of unconsciousness, our
consciousness looks linguistic and so it is not parallel but sequential. Therefore, it is impossible to completely understand
the brain functions through our consciousness. Nevertheless, the researchers have tried to understand the brain or
develop human-like intelligence by hands. We are likely to divide a difﬁcult problem into sub-problems expecting each
divided one is easier to solve. Then “Function Modularization” approach has been deeply penetrated subconsciously.
However, for each module, we have to decide what are the inputs and outputs at ﬁrst. It is easily known that to decide
the information that comes and goes between divided modules, it is necessary to understand the entire function. Then to
decide the information, some simple frame is set in advance and that causes the “Frame Problem”. It can be also thought
that the division into “symbolic (logical) processing” and “pattern processing” causes the “Symbol Grounding Problem”.
In our brain, they may be processed in different areas, but they must be closely related in the same brain as one NN.
“State space” or “action space”, which is generally used in RL, can be another aspect of the function modularization.
Researchers have limited the learning only to the actions that make the mapping from state space to action space, and
have tried to develop the way of construction of state space from sensor signals and given the way of generating motor
commands from each action separately from RL. It has also been taken for granted that in recognition problems, clas-
siﬁcation categories are given and in control problems, reference trajectories are given in advance usually. However,
we can recognize complicated situations from a picture, but it is clear that all of them cannot be given as classiﬁcation
targets in advance. There is no evidence that reference trajectory is explicitly generated in our brain. From the viewpoint
of understanding and developing human-like general intelligence, they are by-products of the function modularization.
They give unnecessary constraints on a huge degree of freedom, and disturb the ﬂexible and comprehensive learning
despite the intension of the researchers.
Based on the above, the author has thought that the interruption of human designers should be cut off and the devel-
opment of functions should be committed to learning of high-dimensional parallel systems as much as possible. The
inputs for a learning system can be raw sensor signals, the outputs can be raw actuator signals, and the entire process
from sensors to actuators (motors) should be learned without dividing into functional modules. A NN has an ability
to optimize the parallel process according to some value or cost function through learning. If training signals are given
by humans, they can be constraints for learning. However, RL has an ability to learn autonomously without receiving
training signals directly based on trials and errors using a motion-perception feedback loop with the environment.
For the higher functions, which are different from the recognition or control, it is difﬁcult to decide either inputs or
outputs, and that has disturbed the progress of the research on them. The author is expecting that higher functions
also emerge through comprehensive end-to-end RL from sensors to motors using a recurrent NN. In image recognition,
the use of deep learning makes the performance better than the conventional approaches that need to design a feature
space[5]. In speech recognition, to leave the learning to an RNN makes the performance better than the combination
with conventional methods like HMM[6]. They seem to support the importance of end-to-end learning approach.
1


## Page 3


The author has thought that what emerges should be called “functions” rather than “representation” because it is not
just a choice of representation, but the result of the processing to get there. Furthermore to be more accurate, the function
that emerges cannot be localized clearly in the NN, but it is just a label for us to understand through our consciousness.
3
Functions that Emerge through Reinforcement Learning (RL)
Here, functions that have been observed to emerge in a NN through RL in our works are introduced. The NN is trained
using the training signals produced automatically by RL; Q-learning, actor-critic or Actor-Q (for learning of both con-
tinuous motion and discrete action) based on TD learning. By using actor outputs in actor-critic or actor-Q directly as
motion commands, not probability called policy but continuous motions have been learned directly. The structure like
convolutional NN is not used except for the work in [22]. The details of each work can be found in each reference.
3.1
Static Functions that Emerge in a Layered Neural Network (NN)
target
64x24(pixels)+4(IR)
critic actor
robot
for two wheels
continuous
motion commands
right
wheel
left
wheel
Figure 1: Learning of Box Pushing: End-to-end
reinforcement learning (RL) using a real robot
(Khepera). A reward was given only when the
robot pushed the box, and continuous motions
for the two wheels were learned. (2003)[10]
A layered neural network (NN) is used and trained according to error
back-propagation (BP), and static functions emerge as follows.
§ Image Recognition
Same as [1, 2], images (pixels) were put into a neural network di-
rectly as inputs, and appropriate behaviors to get a reward were
acquired[7, 8].
That was conﬁrmed also in real robot tasks; Box
Pushing (continuous motion)[10] and Kissing AIBO (real-world-like
environment)[11, 12] as shown in Fig. 1 and Fig. 2.
§ Color Constancy (Optical Illusion)
Motion control of a colored object to the goal location decided by the
object color was learned. The top view image covered by a randomly-
appearing colored ﬁlter was the input. From the internal representa-
tion, we tried to explain the optical illusion of color constancy[13].
§ Sensor Motion (Active Recognition)
A pattern image was the input, and from the reward that indicates
whether the recognition result is correct or not, both recognition and
camera motion for better recognition were acquired through RL[14].
§ Hand-Eye Coordination and Hand Reaching Movement
A NN whose inputs were joint angles of an arm and also image on which its hand can be seen, and whose outputs were
the joint torques learned to reach the hand to the randomly-located target that could be also seen on the image. No
explicit reference trajectory was given. Furthermore, adaptation of force ﬁeld and its after effect were observed[15].
§ Explanation of the Brain Activations during Tool Use
From the internal representation after learning of a reaching task with variable link length, we tried to explain the emer-
gence of the activities observed in the monkey brain when the monkey used a tool to get a food[16].
§ Knowledge Transfer between Different Sensors
An agent has two kinds of sensors and two kinds of motors. There are four sensor-and-motor combinations. There is
a task that could be achieved using either of the combinations. After the agent learned the task using 3 combinations,
learning for the remainder sensor-and-motor combination was drastically accelerated[17].
§ Game Strategy (Not our works, but wonderful results can be seen in [4, 1, 2, 3])
Camera Image
Red Pixels
Green Pixels
Blue Pixels
Q-value
Turn
Right
Go
Straight
Turn
Left
Turn Right
Turn Left
Go
Straight
52x40x3=6240
Figure 2: Learning of approaching to kiss the other AIBO (not moving): a real robot (AIBO) learned using a DQN (Deep-Q
Network) (convolutional structure was not used) in a real-world-like environment. (2008)[11]
2


## Page 4


3.2
Dynamic Functions that Emerge in a Recurrent Neural Network (RNN)
Here, the emergence of dynamic functions is introduced in which expansion along the time axis is required. In this case,
an RNN is used to deal with dynamics, and is trained by BPTT(Back Propagation Through Time) with the training signals
generated automatically based on RL. For both acquisition of memory and error propagation, the feedback connection
weights are set so that the transition matrix is the identity matrix or close to it when being linearly approximated.
§ Memory
There are some works in which necessary information was extracted, memorized and reﬂected to behaviors after learn-
ing almost only from a reward at each goal and punishment. In [18], a very interesting behavior in which if unexpected
results occurred, an agent went back to check the state in the previous stage without any direction could be observed. In
[19] and [20], a real camera image was used as input, and both camera motion and pattern meaning[19] or both camera
motion and word recognition[20] were learned. Purposive associative memory could be also observed[19].
§ Selective Attention
It was learned that in a task in which the attended area of the next presented pattern is changed according to the
previously-presented image, the area of the image was correctly classiﬁed without any special structure for attention[21].
Here, TD-based RL was not used, but learning was done by the reinforcement signal representing only whether the ﬁnal
recognition result was correct or not. Purposive associative memory could be also observed.
§ Prediction (shown in the next subsection[22])
§ Explanation of the Emergence of Reward Expectancy Neurons
From a simulation result of RL using an RNN, we tried to explain the emergence of reward expectancy neurons, which
responded only in the non-reward trials in a multi-trial task observed in the monkey brain[23].
§ Exploration
Effective and deterministic exploration behavior for ambiguous or invisible goal considering past experience was learned
and temporal abstraction was discussed[24, 25].
§ Communication (introduced in another paper[26])
Although each function has been examined in a very simple task, it is known that a variety of functions emerge based
on extraction and memory of necessary information using an RNN. However, the emergence of “thinking” or “symbol
processing” that needs multi-step state transition has not been observed yet.
3.3
Frame-free Function Emergence for Artiﬁcial General Intelligence
As mentioned before, through end-to-end RL from sensors to motors, entire process is learned and comprehensive
function is acquired.
For example, in the work in [22], an agent who has a visual sensor and an RNN as shown
in Fig.
3 learned both motion and capture timing of a moving object that often becomes invisible randomly.
0.5
8.0
8.0
0.0
0.0
6.0
0.0
3.0
field (object)
field (agent)
41x16
17x7
0.2
11x16
5x7
input layer
(sensor cell layer)
discrete decision(action)
(Q)
“capture” “move”
continuous motion
(Actor)
vagent,x vagent,y
feedback
connections
lower hidden layer
upper
hidden layer
output layer
17
7
41
16
7
5
11
16
actual field
Bounce at wall
vx,after =     0.9vx,before vy,after = -0.8vy,before
Invisibility area
40%: not appear
40%: normal
60%: appear
(new object location and moving direction is random)
20%: unexpected object motion when it appears again
(width and location is random)
(width and location is random but ended before x
 = 4.5)
8.0
3.0
0.0
successful capture area
6.0
x
3.0
y
object
start
2.5
0.5
θ0
agent
start
(-45 ~ 45 )
vx,0 (0.4 ~ 0.8)
1.0
agent movable
area
object is invisible
     in the area
object
py,0
vx =   0.4
the reward is larger
as the object is closer to the center
Figure 3: Invisible moving object capture problem (prediction task). Invisibility area, object start location, initial object
moving direction and velocity are decided randomly at each episode. The input of the RNN is 832 visual signals (656 for
the object and 176 for the agent itself). By using Actor-Q, the agent can choose ‘capture’ or ‘move’, and when ‘move’ is
chosen, the continuous motion is determined by the two actor outputs.(2013)[22]
3


## Page 5


6.0
8.0
0.0
3.0
x
y
case 1
case 2
case 1
case 2
object
start
   0.5
agent
start
vx=0.8
vx=0.4
θ=45
θ=22.5
6.0
8.0
3.0
0.0
3.0
x
y
case 3
4.5
object
start
agent
start
vx =0.4
θ =-45
2.5
case 4
gray: object invisible area
         (randomly appears)
movable range for agent
6.0     x     8.0
Figure 4: Sample agent behaviors after learning of a
prediction task. (2013)[22]
In a general approach, the object motion is estimated from some
frames of image using some given model, the future object location
is predicted, the capture point and time are decided by some opti-
mization method, a reference trajectory is derived from the capture
point, and the motions are controlled to follow the trajectory.
Fig. 4 shows four examples after RL based on the reward given for
object capture. The agent did not know in advance the way to pre-
dict the motion or even the fact that prediction is necessary to catch
it. Nevertheless, it moved to the very front of its range of motion,
waited the object, and when the object came to close, the agent
moved backward with it and caught it. Though the object became
invisible or visible again suddenly, the agent could behave appro-
priately. Since the moving direction of the object changed some-
times when it was invisible during learning, the agent learned to
wait close to the center (y = 1.5) where it can react the unexpected
object motion. As shown in case 4, when the object changed its
direction unexpectedly, the agent could catch it though the timing
is a bit later than the case of expected motion (case 3).
References
[1] Minh, V., Kavukcuoglu, K., et al. (2013) Playing Atari with Deep Reinforcement Learning, NIPS Deep Learning Workshop 2013.
[2] Minh, V., Kavukcuoglu, K., Silver, D., et al. (2015) Human-level control through deep reinforcement learning Nature, 518, 529–533.
[3] Silver, D., Huang, A., et al. (2016) Mastering the game of Go with deep neural networks and tree search, Nature, 529, 484–489.
[4] Tesauro, G. (1992) Practical Issues in Temporal Difference Learning, Machine Learning, 8, 257–277.
[5] Krizhevsky, A., Sutskever, I., et al. (2012) ImageNet Classiﬁcation with Deep Convolutional Neural Networks NIPS, 25, 1097–1105.
[6] Amodei, D., Anubhai, R., et al. (2015) DeepSpeech2: End-to-end Speech Recognition in English and Mandarin arXiv:1512.02595.
[7] Shibata, K. & Okabe, Y. (1997) Reinforcement Learning When Visual Sensory Signals are Directly Given as Inputs, Proc. of ICNN(Int’l
Conf. on Neural Networks)97, 3, 1716–1720.
[8] Shibata, K., Okabe, Y. & Ito, K. (1998) Direct-Vision-Based Reinforcement Learning in ”Going to an Target” Task with an Obstacle and
with a Variety of Target Sizes, Proc. of NEURAP(Neural Networks and their Applications)’98, 95-102.
[9] Shibata, K. (2011) Emergence of Intelligence through Reinforcement Learning with a Neural Network, Advances in Reinforcement
Learning, Intech, 99–120.
[10] Shibata, K. & Iida, M. (2003) Acquisition of Box Pushing by Direct-Vision-Based Reinforcement Learning, Proc. of SICE Annual Conf.
2003, 1378–1383.
[11] Shibata, K. & Kawano, T. (2008) Learning of Action Generation from Raw Camera Images in a Real-World-like Environment by
Simple Coupling of Reinforcement Learning and a Neural Network, Adv. in Neuro-Information Processing, LNCS, 5506, 755–762.
[12] Shibata, K. & Kawano, T. (2009) Acquisition of Flexible Image Recognition by Coupling of Reinforcement Learning and a Neural
Network, SICE J. of Control, Measurement, and System Integration, 2(2), 122–129.
[13] Shibata, K. & Kurizaki, S. (2012) Emergence of Color Constancy Illusion through Reinforcement Learning with a Neural Network,
Proc. of ICDL-EpiRob(Int’l Conf. on Developmental Learning & Epigenetic Robotics)2012, PID2562951.
[14] Shibata, K., Nishino, T. & Okabe, Y. (1995) Active Perception Based on Reinforcement Learning, Proc. of WCNN’95, II, 170–173.
[15] Shibata, K. & Ito, K. (2002) Effect of Force Load in Hand Reaching Movement Acquired by Reinforcement Learning, Proc. of
ICONIP(Int’l Conf. on Neural Information Processing)2002, 1444–1448.
[16] Shibata, K. & Ito, K. (2003) Hidden Representation after Reinforcement Learning of Hand Reaching Movement with Variable Link
Length, Proc. of IJCNN (Int’l Joint Conf. on Neural Networks) 2003, 2619–2624.
[17] Shibata, K. (2006) Spatial Abstraction and Knowledge Transfer in Reinforcement Learning Using a Multi-Layer Neural Network,
Proc. of ICDL (5th Int’l Conf. on Development and Learning) 2006, 36 (CD-ROM).
[18] Utsunomiya, H. & Shibata, K. (2008) Contextual Behavior and Internal Representations Acquired by Reinforcement Learning with a
Recurrent Neural Network ..., Adv. in Neuro-Information Processing, Lecture Notes in Comp. Sci., Proc. of ICONIP ’08,5507, 970–978
[19] Shibata, K. & Utsunomiya, H. (2011) Discovery of Pattern Meaning from Delayed Rewards by Reinforcement Learning with a
Recurrent Neural Network, Proc. of IJCNN (Int’l Joint Conf. on Neural Networks) 2011, 1445–1452.
[20] Faudzi, A. A. M. & Shibata, K. (2014) Acquisition of Context-Based Active Word Recognition by Q-Learning Using a Recurrent
Neural Network, Robot Intelligent Technology and Applications, 2, 191–200.
[21] Shibata, K. & Sugisaka, M. (2004) Dynamics of a Recurrent Neural Network Acquired through Learning of a Context-based Attention
Task, Artiﬁcial Life and Robotics, 7 (4), 145–150.
[22] Shibata, K. & Goto, K. (2013) Emergence of Flexible Prediction-Based Discrete Decision Making and Continuous Motion Generation
through Actor-Q-Learning, Proc. of ICDL-Epirob (Int’l Conf. on Developmental Learning & Epigenetic Robotics) 2013, ID 15.
[23] Ishii S., Shidara, M. & Shibata, K. (2006) A model to explain the emergence of reward expectancy neurons using reinforcement
learning and neural network, Neurocomputing, 69, 1327–1331.
[24] Shibata, K. (2006) Learning of Deterministic Exploration and Temporal Abstraction in Rein..., Proc. of SICE-ICCAS 2006, 4569–4574.
[25] Goto, K. & Shibata, K. (2010) Acquisition of Deterministic Exploration and Purposive Memory through Reinforcement Learning
with a Recurrent Neural Network, Proc. of SICE Annual Conf. 2010, FB03-1.pdf
[26] Shibata, K.(2017) Communications that Emerge through Reinforcement Learning Using a (Recurrent) Neural Network, RLDM2017
4

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
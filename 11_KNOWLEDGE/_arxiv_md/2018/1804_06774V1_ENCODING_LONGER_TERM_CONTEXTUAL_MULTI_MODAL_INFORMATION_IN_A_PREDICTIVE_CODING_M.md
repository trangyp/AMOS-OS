---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1804.06774v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1804.06774v1_Encoding_Longer-term_Contextual_Multi-modal_Information_in_a_Predictive_Coding_M

> Source: 1804.06774v1_Encoding_Longer-term_Contextual_Multi-modal_Information_in_a_Predictive_Coding_M.pdf

> Pages: 6

---


## Page 1


arXiv:1804.06774v1  [cs.AI]  17 Apr 2018
Encoding Longer-term Contextual Multi-modal
Information in a Predictive Coding Model
Junpei Zhong∗†, Tetsuya Ogata∗‡, Angelo Cangelosi†
∗National Institute of Advanced Industrial Science and Technology (AIST), Aomi 2-3-26, Tokyo, Japan
Email: joni.zhong@aist.go.jp
†Centre for Robotics and Neural Systems, Plymouth University, Plymouth, UK
‡ Lab for Intelligent Dynamics and Representation, Waseda University, Tokyo, Japan
Abstract—Studies suggest that within the hierarchical architec-
ture, the topological higher level possibly represents a conscious
category of the current sensory events with a slower changing
activities. They attempt to predict the activities on the lower
level by relaying the predicted information. On the other hand,
the incoming sensory information corrects such prediction of the
events on the higher level by the novel or surprising signal. We
propose a predictive hierarchical artiﬁcial neural network model
that examines this hypothesis on neurorobotic platforms, based
on the AFA-PredNet model. In this neural network model, there
are different temporal scales of predictions exist on different
levels of the hierarchical predictive coding, which are deﬁned
in the temporal parameters in the neurons. Also, both the fast-
and the slow-changing neural activities are modulated by the
active motor activities. A neurorobotic experiment based on the
architecture was also conducted based on the data collected from
the VRep simulator.
I. INTRODUCTION
Predictive coding (PC) [1, 2, 3, 4] asserts that our sensori-
motor loop works as a predictive machine. In this predictive
machine, it attempts to minimize the difference between the
posterior estimation and the truth from its perception, by
changing its internal learning model (“perceptual inference”
(see also [5] and [6]) or by the action execution (“active
inference”, see also [7] and [8]). Additionally, because of the
integrative property of both perception and action, perceiving
the world (perceptual inference) and acting on it (active
inference) can be regarded as two aspects with the same aim:
to minimize the prediction error.
The integrative process of model adjustment follows a bi-
directional learning mechanism on each level of our hier-
archical brain. It is suggested that within the hierarchical
architecture, the topological higher level in the brain areas
infer the prediction on the lower areas with a slower changing
activities [9, 10]. This is done by its subsets of such prediction
representations are transmitted to the lower levels to predict
the upcoming faster neural activities on the lower level. For
instance, areas on the higher-level of our brain learn multiple
world models and act as prior to explain the best descriptions
of the upcoming percept. This continual process acts as an
“explain away” function (e.g. [11, 12]): the explaination on
the higher-level offers the best parameters to predict the most
likely causes of the sensory data on the lower levels, which
explain away the other models. Such hierarchical function can
be realised by the interaction of neural oscillations in different
time-scales, which encode different temporal parameters of the
world models.
Therefore, the higher level representation in a hierarchical
model may physically represent the contextual information
based on the understanding of the upcoming world model for
prediction, As such, the internal world model on the higher
level has to be shaped by the statistical structure of the error.
Based on this hypothesis, we suggest that the concept of time-
scales should also be implemented in the internal models of
the PC framework as well.
II. RELATED WORKS
The difference of the temporal scales of prediction results
in different cognitive functions in embodied internal models.
Some of the previous research focused on the short-term
predictive function of the internal model. In most cases, such
short-term prediction can act a compensation function of the
sensorimotor integration (e.g. [13, 14, 15, 16]). Based on the
PC framework, the PredNet model [17] is considered to be the
ﬁrst deep learning model that can be utilised in solving a real
application. Speciﬁcally, the model uses the error between the
predicted image and the real image as an input in the bottom-
up stream, which strictly follows the concept of PC. In its
experiment, the next video frame of the autonomous driving
stream could be predicted. To solve this problem, a recent work
[18] proposed a model called AFA-PredNet which integrates
both motor action and perception in the PC framework. In
this network, the motor action is used as attention model for
the prediction from a couple of recurrent networks. However,
the long-term prediction based on the understanding of the
world model is still missing in both the PredNet and the AFA-
PredNet models.
Indeed, when we think about the predictive functions in
biological brains, there are no explicit boundaries between the
short- and mid-term prediction and the long-term predictive:
the short-term prediction is based on a long-term understand-
ing and prediction of the world. For instance, [19] and [20]
studied how to apply internal model to control the actual motor
actions, mostly focusing on the predictive control of a motor
action. [21] extended these models to imitation learning of the
sensorimotor behaviours. The long-term planning behaviours
can also emerge from internal simulation where the prediction
occurs constantly (e.g. [22, 23]).


## Page 2


Speciﬁcally, while we consider the pre-symbolic repre-
sentation as a understanding of the context in the long-
term prediction, it can be acted as a modality of long-term
prediction too, which is learnt in a unsupervised way. From
this perspective, [24] reported an embodied experiment in
which an association between the semantic meaning and the
sensorimotor behaviours emerges by a recurrent architecture
called Recurrent Neural Network with Parametric Bias Units
(RNNPB). Based on the extension of this network,
[25]
discovered that the semantic representation about the object
movements and object features also emerge in a recurrent
neural network. Speciﬁcally, the network is able to predict
the next probable position of the object movement, while to
pre-symbolic representation is given.
If we regard the uniﬁcation of different time-scales in a
single predictive model with artiﬁcial recurrent connections,
experiments based on the Multiple Timescale Neural Network
(MTRNN) [26] offers an explanation from the view of the
non-linear dynamical system for such phenomena. It can
be regarded as another extended version of the RNNPB.
The neurons on the higher-level of the MTRNN are with
slower-changing neural activities, which modulates the neural
activities on the lower-levels by the similar roles of the bias
inputs. Thus, the whole network is able to work as a number of
non-linear dynamic functions as a similar role of bifurcation.
While the model is used to learn the temporal sequences such
as the sensorimotor information of the robots, the model is
able to represent different spatio-temporal embodiment scales
of sensorimotor information, such as the language learning
[27, 25] and object features/movements [28]. Similar concept
of multiple time-scales has also be applied in Gated Recurrent
Units for automatically context extraction [29, 30].
The multiple time-scales concept can also be extended in
different modalities. For instance, the multiple spatio-temporal
scales RNN (MSTRNN) [31] integrates the MTRNN and
convolutional neural networks [32, 33], where both the spatial
and temporal information are connected and asscocated on
the higher level, where slower changing neurons represent the
sensorimotor behaviours. The slower changing units on the
higher level also makes the dynamics of the model easier
to be interpreted, examined and changed. But unfortunately,
neither MTRNN nor MSTRNN cannot be considered as a PC
model, as that they do not have an explicit input from the error
(i.e.difference) between the prediction and the original values.
On the other hand, compared with MSTRNN, the PredNet
[17] follows the deﬁnition of PC while using the difference
as inputs on each layer. And it also uses the convolutional
network to capture the local features of the visual streams.
But the PredNet builds the temporal prediction in the top-
down perception part, which makes the model more biological
plausible.
Building the PC embodied model with the concept of
multiple time-scales would be beneﬁcial for both engineering
and cognitive studies. Firstly, it follows the results from the
brain and cognitive studies that different response times while
the neurons react to conscious/unconscious prediction. Second,
the slower changing neurons in such a model would be easier
for us to control and examine the dynamical behaviours of the
model or the embodied systems. This is the main motivation
why we are proposing for a novel action modulated PC model
with multiple time scales.
III. THE MODEL
The proposed MTA-PredNet (Multiple Time-scale Action
modulated PredNet) is shown in Fig. 1. In general, the MTA-
PredNet is functionally organized as an integration with two
networks: the left part is equivalent to a generative recurrent
network, while the right part is a standard convolutional
network.
In terms of architecture, it is similar as AFA-PredNet [18].
1) There are a number of recurrent neural networks. (e.g.
Convolutional LSTM) on each level of the model, which
learn different possibilities of the prediction (a genera-
tive unit, GU, green))
2) The input of the motor action is used as an additional
signal for the modulation of the prediction (the motor
modulation unit, MM, grey). Speciﬁcally, it acts as an
attention mechanism for the prediction from the upper
level (top-down prediction);
3) The convolutional network in the bottom-up part capture
the feature of the error on each level, (the discriminative
unit, DU, blue);
4) The difference of the updating rate on different levels of
the architecture determine different representation of the
sptio-temporal properties of the sensorimotor behaviours
(the error unit, ER, red).
The generative unit, GU, is usually a recurrent network
that generates a prediction of the next time-step from the
current input. Here, the convolutional LSTM [34, 35] is
employed to generate the local feature prediction in the image.
We employ a number of independent recurrent units on one
layer of the GU unit so that the different possibilities of the
prediction given the motor action input can be memorized
and predicted. Such memories are also determined by the
time-scales we mention later, which produces the prediction
given the contexts of different time-scales. During training
with various action-perception pairing, each of these units
implicitly memorizes different possibilities of the prediction
(e.g. the moving direction) with respect to the motor action in
a unsupervised way.
The neural functions on each neural unit can be found in
Eq. III. Although the main architecture of the MTA-PredNet
is the same as AFA-PredNet, the most important feature is
that in the neural function of the generative unit (Eq. 4), the
generated output is determined not only by the current neural
status, but also its previous status. The fraction of the output
is determined by the temporal parameter τ.


## Page 3


Fig. 1: A 2-layer AFA-PredNet
Xl(t) =
(
i(t),
if l = 0,
MAXPOOL(f(Conv(El−1(t)))),
if l > 0
(1)
ˆXl(t) = f(Conv(Rl(t)))
(2)
El(t) = [f(Xl(t) −ˆXl(t)); f( ˆ
Xl(t) −Xl(t))]
(3)
Rd
l (t) = (1 −1
τ )Rd
l (t) + 1
τ ConvLST M(El(t −1), Rl(t −1), DevConv(Rl+1(t)))
(4)
Rl(t) = MLP(a(t)) × Rd
l (t)
(5)
where f(·) is an activation function of the neurons, which
we apply the ReLu function to ensure a faster learning in
back-propagation, X(·)t
l is the neural representation of the
level l at time t. The representation on the EL layer l is
E(·)l. The MAXPOOL, Conv, ConvLST M and MLP are
the corresponding neural algorithms. Speciﬁcally, to realize
the time scale concept, Eq. 4 indicates that the predicted
information in the GU unit should consider the previous state
of the ConvLSTM outputs as well as the current output. This
is determined by the time parameter τ.
The overall algorithm for learning a whole sequence is
showed in Algorithm 1.
Fig. 2: Data Collected from VRep Simulation
IV. CASE ANALYSIS
In this section, the performance of the network as well
as the analysis of the neural activities will be conducted in


## Page 4


Data: i(t)&a(t) ∈data
while error > threshold or
iteration > maximum iteration do
for t ←0 to T do
for l ←0 to L do
if l == L then
Rd
l (t) = (1 −1/τ)Rd
l (t −1) + 1/τ ·
ConvLST M(El(t −1), Rl(t −1);
else
Rd
l (t) = (1 −1/τ)Rd
l (t −1) + 1/τ ·
ConvLST M(El(t −1), Rl(t −
1), DevConv(Rl+1(t)));
end
Rl(t) = MLP(a(t)) × Rd
l (t);
end
/* Generative (top-down) Process
*/
for l ←L to 0 do
ˆXl(t) = f(Conv(Rl(t))); El(t) =
[f(Xl(t) −ˆXl(t)); f( ˆXl(t) −Xl(t));
/* Discriminative
(bottom-up) Process
*/
end
end
end
Algorithm 1: MTA-PredNet Computation
a mobile robot experiment. We recorded a data-set from a
robot simulation about the line tracer robot car from the VRep
simulator [36]. In this simulation (Fig. 2), the robot equips
three vision sensors as well as three Line Finder sensors. With
these sensors, the robot was able to adjust the velocities of its
wheels to follow the line on the ground. Using VRep, we were
also able to record the wheel velocity data and the camera data
to train the network. To gather the data, we captured the grey-
scale images with size of 8×12 pixels from the middle vision
sensor every 0.02s.
A three-layer MTA-PredNet was used for training the se-
quence of both motor action vectors (i.e. the velocities of the
wheels) and images, with the Adam optimizer [37]. Three
different values of τ were applied in three different layers.
With a larger tau on the upper levels, it indicates slower
neural activities would be expected. Compared with the τ
values selected in MTRNN works (e.g. [26, 28]), a much
smaller τ values are chosen, because the LSTM networks
performs longer term memories by themselves. The parameters
are shown in the table:
Parameters
Value
τ0
1.0
τ1
1.3
τ2
2.0
Kernel
3 × 3
Padding
1
Pooling
2 × 2
TABLE I: parameters
Fig. 3 and Fig. 4 show the comparison between the samples
of the original and the predicted images.
We further visualise the neural activities on different layers
to examine how time parameters τ affects the representation.
Corresponding to the prediction samples, the internal repre-
sentations of the prediction on the 1st GU of each layer are
shown (Figs. 5, 6 and 7), from which we can observe the
predicted image on the higher-level (Fig. 7) remains steady
during almost the whole movement of the robot compared with
other two layers. A demo of the experiment can be found in1.
V. CONCLUSION
The top-down prediction in the PC framework may occurs
based on the longer term understanding representing the con-
textual multi-modal information. As a few neuroscience stud-
ies have suggested the temporal difference in neural activities
can be found in the hierarchical brain areas, the multiple time-
scales concepts have been applied in an embodied PC model,
the PredNet model. Speciﬁcally, the higher-level encodes the
slowly changing information of both perception and action,
indicating the understanding of the full sensorimotor event.
At the next stage, we will examine the network performance
in details and with more robot experiments. Also, it would be
interesting to explore the interaction between the short- and
long-term prediction in the sense of the neural representation.
And how such interaction emerges from the embodied inter-
action.
ACKNOWLEDGEMENT
The research was partially supported by New Energy and
Industrial Technology Development Organization (NEDO). A
Pytorch implementation of MTA-PredNet can be found on
Github2
REFERENCES
[1]
A. Clark. “Whatever next? Predictive brains, situated
agents, and the future of cognitive science”. In: Behav-
ioral Brain Sciences (2012), pp. 1–86.
[2]
R. P. Rao and D. H. Ballard. “Predictive coding in
the visual cortex: a functional interpretation of some
extra-classical receptive-ﬁeld effects”. In: Nature neu-
roscience 2.1 (1999), pp. 79–87.
[3]
K. Friston. “Learning and inference in the brain”. In:
Neural Networks 16.9 (2003), pp. 1325–1352.
[4]
K. Friston. “A theory of cortical responses”. In: Philo-
sophical Transactions of the Royal Society B: Biological
Sciences 360.1456 (2005), pp. 815–836.
[5]
E. M. Segal and T. G. Halwes. “The inﬂuence of
frequency of exposure on the learning of a phrase struc-
tural grammar”. In: Psychonomic Science 4.1 (1966),
pp. 157–158.
[6]
K. Friston and S. Kiebel. “Cortical circuits for per-
ceptual inference”. In: Neural Networks 22.8 (2009),
pp. 1093–1104.
1https://youtu.be/4w7RqeU42XY
2https://github.com/jonizhong/mta prednet.git


## Page 5


(a) Frame 1
(b) Frame 10
(c) Frame 50
(d) Frame 100
(e) Frame 130
Fig. 3: Image Samples from the Middle Vision Sensor
(a) Frame 1
(b) Frame 10
(c) Frame 50
(d) Frame 100
(e) Frame 130
Fig. 4: Predicted Images after Training
(a) Frame 1
(b) Frame 10
(c) Frame 50
(d) Frame 100
(e) Frame 130
Fig. 5: Image generated from the 1st GU output (Layer 0), τ = 1.0
(a) Frame 1
(b) Frame 10
(c) Frame 50
(d) Frame 100
(e) Frame 130
Fig. 6: Image generated from the 1st GU output (Layer 1), τ = 1.3
[7]
K. Friston, J. Mattout, and J. Kilner. “Action under-
standing and active inference”. In: Biological cybernet-
ics 104.1 (2011), pp. 137–160.
[8]
G. Pezzulo, F. Rigoli, and K. Friston. “Active Infer-
ence, homeostatic regulation and adaptive behavioural
control”. In: Progress in Neurobiology 134 (2015),
pp. 17–35.
[9]
B. Han and R. VanRullen. “The rhythms of predictive
coding? Pre-stimulus phase modulates the inﬂuence of
shape perception on luminance judgments”. In: Scien-
tiﬁc reports 7 (2017), p. 43573.
[10]
R. VanRullen. “Perceptual cycles”. In: Trends in Cog-
nitive Sciences 20.10 (2016), pp. 723–735.
[11]
D. Kersten, P. Mamassian, and A. Yuille. “Object per-
ception as Bayesian inference”. In: Annual review of
psychology 55 (2004).
[12]
J. Hohwy, A. Roepstorff, and K. Friston. “Predictive
coding explains binocular rivalry: An epistemological
review”. In: Cognition 108.3 (2008), pp. 687–701.
[13]
E. von Holst and H. Mittelstaedt. “The reafference prin-
ciple: Interaction between the central nervous system
and the peripheral organs. Selected Papers of Erich
von Holst: The Behavioural Physiology of Animals and
Man”. In: (1950).
[14]
R. C. Miall and D. M. Wolpert. “Forward models for
physiological motor control”. In: Neural networks 9.8
(1996), pp. 1265–1279.


## Page 6


(a) Frame 1
(b) Frame 10
(c) Frame 50
(d) Frame 100
(e) Frame 130
Fig. 7: Image generated from the 1st GU output (Layer 1), τ = 2.0
[15]
N. L. Cerminara, R. Apps, and D. E. Marple-Horvat.
“An internal model of a moving visual target in the
lateral cerebellum”. In: The Journal of physiology 587.2
(2009), pp. 429–442.
[16]
J. Zhong, C. Weber, and S. Wermter. “A Predictive
Network Architecture for a Robust and Smooth Robot
Docking Behavior”. In: Paladyn. Journal of Behavioral
Robotics 3.4 (2012), pp. 172 –180.
[17]
W. Lotter, G. Kreiman, and D. Cox. “Deep predictive
coding networks for video prediction and unsupervised
learning”. In: arXiv preprint arXiv:1605.08104 (2016).
[18]
J. Zhong et al. “AFA-PredNet: The action modulation
within predictive coding”. In: International Joint Con-
ference on Neural Networks (IJCNN) (2018).
[19]
D. M. Wolpert, Z. Ghahramani, and M. I. Jordan. “An
internal model for sensorimotor integration”. In: Science
(1995), pp. 1880–1880.
[20]
D. M. Wolpert and M. Kawato. “Multiple paired for-
ward and inverse models for motor control”. In: Neural
Networks 11.7-8 (1998), pp. 1317–1329.
[21]
Y. Demiris and B. Khadhouri. “Hierarchical atten-
tive multiple models for execution and recognition of
actions”. In: Robotics and autonomous systems 54.5
(2006), pp. 361–369.
[22]
H. Hoffmann. “Perception through visuomotor antici-
pation in a mobile robot”. In: Neural Networks 20.1
(2007), pp. 22–33.
[23]
R. M¨oller and W. Schenck. “Bootstrapping cognition
from behaviora computerized thought experiment”. In:
Cognitive Science 32.3 (2008), pp. 504–542.
[24]
Y. Sugita and J. Tani. “Learning semantic combinato-
riality from the interaction between linguistic and be-
havioral processes”. In: Adaptive Behavior 13.1 (2005),
p. 33. ISSN: 1059-7123.
[25]
J. Zhong, A. Cangelosi, and S. Wermter. “Towards a
self-organizing pre-symbolic neural model representing
sensorimotor primitives”. In: Frontiers in Behavioral
Neuroscience 8 (2014), p. 22.
[26]
Y. Yamashita and J. Tani. “Emergence of functional
hierarchy in a multiple timescale neural network model:
a humanoid robot experiment”. In: PLoS Computational
Biology 4.11 (2008), e1000220.
[27]
T. Ogata and H. G. Okuno. “Integration of behaviors
and languages with a hierarchal structure self-organized
in a neuro-dynamical model”. In: Robotic Intelligence
In Informationally Structured Space (RiiSS), 2013 IEEE
Workshop on. IEEE. 2013, pp. 89–95.
[28]
J. Zhong et al. “Sensorimotor Input as a Language
Generalisation Tool: A Neurorobotics Model for Gen-
eration and Generalisation of Noun-Verb Combina-
tions with Sensorimotor Inputs”. In: arXiv preprint
arXiv:1605.03261 (2016).
[29]
M. Kim, M. D. Singh, and M. Lee. “Towards Ab-
straction from Extraction: Multiple Timescale Gated
Recurrent Unit for Summarization”. In: arXiv preprint
arXiv:1607.00718 (2016).
[30]
J. Zhong, A. Cangelosi, and T. Ogata. “Toward Ab-
straction from Multi-modal Data: Empirical Studies on
Multiple Time-scale Recurrent Models”. In: 2017 Inter-
national Joint Conference on Neural Networks (IJCNN)
(2017).
[31]
H. Lee, M. Jung, and J. Tani. “Recognition of visually
perceived compositional human actions by multiple
spatio-temporal scales recurrent neural networks”. In:
arXiv preprint arXiv:1602.01921 (2016).
[32]
Y. LeCun et al. “Gradient-based learning applied to
document recognition”. In: Proceedings of the IEEE
86.11 (1998), pp. 2278–2324.
[33]
J. Donahue et al. “Long-term recurrent convolutional
networks for visual recognition and description”. In:
Proceedings of the IEEE conference on computer vision
and pattern recognition. 2015, pp. 2625–2634.
[34]
S. Hochreiter and J. Schmidhuber. “Long short-term
memory”. In: Neural computation 9.8 (1997), pp. 1735–
1780.
[35]
X. Shi et al. “Convolutional LSTM network: A machine
learning approach for precipitation nowcasting”. In:
Advances in neural information processing systems.
2015, pp. 802–810.
[36]
E. Rohmer, S. P. Singh, and M. Freese. “V-REP: A
versatile and scalable robot simulation framework”. In:
Intelligent Robots and Systems (IROS), 2013 IEEE/RSJ
International Conference on. IEEE. 2013, pp. 1321–
1326.
[37]
D. P. Kingma and J. Ba. “Adam: A method for stochas-
tic optimization”. In: arXiv preprint arXiv:1412.6980
(2014).

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1804_06774v1_encoding_longer_term_contextual_multi_modal_information_in_a_predictive_coding_m
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2018/1804_06774V1_ENCODING_LONGER_TERM_CONTEXTUAL_MULTI_MODAL_INFORMATION_IN_A_PREDICTIVE_CODING_M.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

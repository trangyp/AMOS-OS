---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1811.01701v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1811.01701v1_Role_of_Awareness_and_Universal_Context_in_a_Spiking_Conscious_Neural_Network__S

> Source: 1811.01701v1_Role_of_Awareness_and_Universal_Context_in_a_Spiking_Conscious_Neural_Network__S.pdf

> Pages: 14

---


## Page 1


Role of Awareness and Universal Context in a Spiking Conscious
Neural Network (SCNN): A New Perspective and Future Directions
Ahsan Adeel
Computing Science and Mathematics, University of Stirling, FK9 4LA, UK
deepCI.org, 20/1 Parkside Terrace, Edinburgh, EH16 5XW, UK
Abstract
Awareness plays a major role in human cognition and adaptive behaviour, though mechanisms involved remain un-
known. Awareness is not an objectively established fact, therefore, despite extensive research, scientists have not been
able to fully interpret its contribution in multisensory integration and precise neural ﬁring, hence, questions remain:
(1) How the biological neuron integrates the incoming multisensory signals with respect to different situations? (2)
How are the roles of incoming multisensory signals deﬁned (selective ampliﬁcation or attenuation) that help neuron(s)
to originate a precise neural ﬁring complying with the anticipated behavioural-constraint of the environment? (3) How
are the external environment and anticipated behaviour integrated? Recently, scientists have exploited deep learning
architectures to integrate multimodal cues and capture context-dependent meanings. Yet, these methods suffer from
imprecise behavioural representation and a limited understanding of neural circuitry or underlying information pro-
cessing mechanisms with respect to the outside world. In this research, we introduce a new theory on the role of
awareness and universal context that can help answering the aforementioned crucial neuroscience questions. Specif-
ically, we propose a class of spiking conscious neuron in which the output depends on three functionally distinctive
integrated input variables: receptive ﬁeld (RF), local contextual ﬁeld (LCF), and universal contextual ﬁeld (UCF) -
a newly proposed dimension. The RF deﬁnes the incoming ambiguous sensory signal, LCF deﬁnes the modulatory
sensory signal coming from other parts of the brain, and UCF deﬁnes the awareness. It is believed that the conscious
neuron inherently contains enough knowledge about the situation in which the problem is to be solved based on past
learning and reasoning and it deﬁnes the precise role of incoming multisensory signals (ampliﬁcation or attenuation) to
originate a precise neural ﬁring (exhibiting switch-like behaviour). It is shown, when implemented within an SCNN,
the conscious neuron helps modelling a more precise human behaviour e.g., when exploited to model human audio-
visual speech processing, the SCNN performed comparably to deep long-short-term memory (LSTM) network. We
believe that the proposed theory could be applied to address a range of real-world problems including elusive neural
disruptions, explainable artiﬁcial intelligence, human-like computing, low-power neuromorphic chips etc.
Keywords: Multisensory Integration, Conscious Neuron, Behavioural Modelling
1. Introduction
What is awareness or consciousness? Think of a well-trained and experienced car driver who automatically iden-
tiﬁes and follows the trafﬁc protocols in different surrounding environments (e.g. street, highway, and city centre) by
interpreting the visual scenes directly (such as buildings, school etc.). Similarly, imagine a car with defective parking
sensors which sometimes miscalculate the nearby object distance. It means that the audio input is ambiguous and
driver can’t fully rely on parking sensors for precise maneuvering decisions e.g. while reversing the car. In this situ-
ation, we observe that the driver automatically starts utilizing visual cues to leverage the complementary strengths of
both ambiguous sound (defective reversing beeps) and visuals. This is one example of consciousness or awareness,
*ahsan.adeel@deepci.org c⃝Ahsan Adeel 2018. All rights reserved.
arXiv:1811.01701v1  [cs.AI]  5 Nov 2018


## Page 2


Figure 1: Ambiguous decision-making and local contextual modulation
where the surrounding environment or situation (UCF) helps establishing the anticipated behaviour to comply with,
deﬁning the optimal roles of incoming multisensory information, and eventually controlling human actions.
Similarly, in contextual audio-visual (AV) speech processing, we observe that in a very noisy environment, our
brain naturally utilizes other modalities (such as lips, body language, facial expressions) to perceive speech or the con-
veyed message (i.e. speech perception in noise) [1][2][3][4]. However, it raises crucial questions: How does it happen
in the brain? How the incoming sensory signals (such as vision and sound) integrate with respect to the situation? How
are the roles of incoming signals (selective ampliﬁcation/suppression) deﬁned? How does the neuron(s) originate a
precise control command that controls human actions based on incoming multisensory information and their precise
integration, complying with the anticipated behavioural-constraint of the environment? Certainly, deﬁning the context
and its relevant features knowing when a change in context has taken place are challenging problems in modelling
human behaviour [5]. It is also claimed in the literature that context could be of inﬁnite dimensions but humans have
a unique capability of correlating the signiﬁcant context and set its boundaries intuitively with respect to the situation.
However, once the context is identiﬁed, it is relatively easy to utilize and set its bounds to more precisely deﬁne the
search space for the selection of best possible decision [5].
A simple example of contextual modulation is shown in Figure 1 [6]. It illustrates the role of localized contextual
information (i.e. LCF) that comes from the nearby location in space. It can be seen that the ambitious RF input (in
the top row) is interpreted as B or 13 depending on the local contextual information coming from the nearby location
in space. Identically, consider the perception of any ambiguous letter or speech sound. At times, if available, the
surrounding environment and its understanding signiﬁcantly help to disambiguate the ambiguous input. The contextual
modulation can in principle be from anywhere in space/time that modulates the transmission of information about other
driving signals [6]. However, the selective ampliﬁcation and attenuation of incoming multisensory information with
respect to the outside world at the neural level is still very little understood. In addition, to the best of our knowledge,
not much progress has been made to fully interpret the role of consciousness and objectively deﬁne its contribution in
multisensory integration. The complexity of the problem is widely appreciated by scientists with a consensus that it is
not easy to use awareness and contextual modulation to show enhanced processing, learning, and reasoning.
In this research article, we propose a novel conscious neural structure and objectively deﬁne awareness in terms of
newly proposed UCF. The proposed spiking conscious neuron exhibits a switch-like behavior that deﬁnes the role of
incoming multisensory signals with respect to the outside environment and anticipated behaviour. It is believed that
the conscious neuron inherently contains enough knowledge about the situation in which the problem is to be solved
based on past learning and reasoning and it helps deﬁning the precise role of incoming multimodal signals to originate a
precise control command. The conscious neuron exploits four types of contexts: modulatory (LCF), temporal, spatial,
and awareness (UCF). The preliminary behavioural modelling analysis and simulation results demonstrate enhanced
learning and reasoning capability of the proposed SCNN as compared to the state-of-the-art unimodal and multimodal
models.
The rest of the paper is organized as follows: Section 2 discusses the conceptual foundation and motivation which
leads to the development of conscious neural structure and SCNN. Section 3 presents the conscious neural structure
and SCNN. In section 4, the conscious neural structure and SCNN are utilized for behavioural modelling including
AV speech processing and driving behaviour. Finally, section 5 discusses the research impact, applications, and future
research directions.
2. Motivation and Contribution
The simpliﬁed state-of-the-art integrate-and-ﬁre neural structure is doing wonders today, think of the potential of
neuron representing a closer form of biophysical reality. There exists ample evidence that divisive and multiplicative
2


## Page 3


gain modulations are widely spread in mammalian neocortex with an indication of ampliﬁcation or attenuation via
contextual modulation [6]. Evidence gathered in the literature suggests that multisensory interactions emerge at the
primary cortical level [7][8]. Scientists have presented several theories and empirical results on the role of contextual
modulation to disambiguate the ambiguous input or improve feature detection with weak or noisy inputs [9]. Recently,
the authors in [6] used modern developments in the foundation of information theory to study the properties of local
processors (neuron or microcircuit) embedded within the neural system that uses the contextual input to amplify or
attenuate transmission of information about their driving inputs. Speciﬁcally, the authors used advances in information
decomposition to show that the information transmitted by the local processor with two distinct inputs (driving and
contextual information) can be decomposed into components unique to each other having three-way mutual/shared
information. In [9], the authors used an edge detection problem as a benchmark to demonstrate the effectiveness of
contextual modulation in recognizing speciﬁc patterns with noisy RF input. It was shown how surrounding regions
in different parallel streams helped detecting the edge within any particular region and played a signiﬁcant role in
combating noisy input.
Recently, researchers have also proposed several deep recurrent neural network architectures to exploit contextual
modulation by leveraging the complementary strengths of multimodal cues. For example, researchers in [10] presented
a joint AV model for isolating a single speech signal from a mixture of sounds. The authors used a complementary
strength of both audio and visual cues using deep learning to focus the audio on the desired speaker in a scene.
Similarly, the authors in [11] and [12] developed an AV switching component for speech enhancement and mask
estimation to effectively account for different noisy conditions contextually. The contextual AV switching components
were developed by integrating a convolutional neural network (CNN) and long-short-term memory (LSTM) network.
However, these end-to-end multimodal learning models operate at the network level and can’t be used for deep analysis
and information decomposition to understand neural circuitry and underlying information processing mechanisms at
the neural level, with respect to the outside world and anticipated behaviour. In addition, these methods only exploit the
localized context without considering the overall knowledge of the problem (awareness). Thus, the limited contextual
exploitation leads to imprecise behavioural representation. This work proposes a new conscious neural structure and
SCNN that objectively deﬁne awareness at the neural level. Contrary to the work presented in [9], the proposed SCNN
is evaluated with a noisy speech ﬁltering problem. Speciﬁcally, we used two distinctive multimodal multistreams (lip
movements as LCF and noisy speech as RF) and studied how the LCF helped to improve the noisy speech ﬁltering
in different noisy conditions (ranging from a very noisy to an almost zero noise environment). Later, going beyond
the theory of local contextual modulation, we added UCF as another input variable (as a fourth virtual dimension) to
deﬁne descriptive and control context (environment and anticipated behaviour) in SCNN.
3. Spiking Conscious Neural Network
The proposed conscious neural structure is presented in Figure 2. The output of the neuron depends on three
functionally distinctive integrated input variables: driving (RF), modulatory (LCF), and awareness (virtual UCF). The
RF is deﬁning the ambiguous sensory signal, LCF is deﬁning the modulatory sensory signal coming from other parts
of the brain, and UCF is deﬁning the outside world and anticiapted behaviour. The interaction among RF, LCF, and
UCF in an SCNN is shown in Figure 3. The output is denoted by the random variable Y, whereas X, Z, and U represent
RF, LCF, and UCF respectively. It is believed that the proposed neural structure when implemented within a multi-
layered multiunit network of similar neurons produce a widely distributed activity pattern with respect to the current
circumstances (i.e. a combination of RF, LCF, and UCF at the neuronal level). This activity helps neural network
to explore and exploit the associative relations between the features extracted within different streams [9][6]. In the
implementation, the neuron in one stream is connected to all other neurons in the neighbouring stream of the same
layer. This is achieved through shared connections among the neurons that guide learning and processing with respect
to local and universal contexts.
3.1. Mathematical Modelling
The conscious neuron (y) in the proposed SCNN interacts by exchanging the excitatory and inhibitory spikes
probabilistically (in the form of bipolar signal trains) as shown in Figure 3 and Figure 4. In steady state, the stochastic
spiking behaviour of the network has a product form property (product of ﬁring rates and transition probabilities)
which deﬁnes state probability distribution with easily solvable non-linear network equations. The ﬁring from neuron
y to succeeding neuron w in the network is according to the Poisson process, represented by the synaptic weights
w+
yw = ry[P +
yx + P +
yz + P +
yu] and w−
yw = ry[P −
yx + P −
yz + P −
yu], where P +
yx, P +
yz, P +
yu and P −
yx, P −
yz, P −
yu represent the
3


## Page 4


Figure 2: Proposed conscious neural structure with a switch-like behaviour: The output depends on three functionally distinctive integrated input
variables: driving (RF), modulatory (LCF), and awareness (virtual UCF). The RF is deﬁning the ambiguous sensory signal, LCF is deﬁning the
modulatory sensory signal coming from other parts of the brain, and UCF is deﬁning the outside world and anticiapted behaviour. The conscious
neuron, with respect to the outside environment (UCF), decides whether the role of LCF is modulatory or null.
probabilities of excitatory and inhibitory RF, LCF, and UCF signals, respectively. The term ry represents the ﬁring
rate of the conscious neuron. The terms w+
yx, w+
yz, w+
yu and w−
yx, w−
yz, w−
yu represent the RF, LCF, and UCF synaptic
weights (i.e. the rates of positive and negative signal transmission) that network learns through the process of learning
or training. In the network, the conscious neuron y can receive exogenous signals positive/negative from the inside
(within the network) or outside world according to Poisson arrival streams of rates Λx, λx, respectively. The potential
(Y) of the conscious neuron represents its state that increases/decreases with respect to an incoming signal coming
from the inside or outside world. The proposed neural structure is implemented using G-networks which possess
product-form asymptotic solution [13]. The neuron y in ﬁring state transmits an impulse to neuron w with a Poisson
rate (ry) and probability P +(y, w) or P −(y, w) depending on the incoming signal as excitatory or inhibitory. The
transmitted signal can also leave the network and go outside the world with probability d(y) such that:
d(y) +
N
X
x=1
[P +(y, x) + P −(y, x)] +
N
X
z=1
[P +(y, z) + P −(y, z)] +
N
X
u=1
[P +(y, u) + P −(y, u)]
=
1
(1)
Where,
w+(y, w) = ry[P +(y, x) + P +(y, z) + P +(y, u)] ≥0, w−(y, w) = ry[P −(y, x) + P −(y, z) + P −(y, u)] ≥0
(2)
The ﬁring rate of the conscious neuron can be written as:
r(y) = (1 −d(y))−1(
N
X
x=1
[w+(y, x) + w−(y, x)] +
N
X
z=1
[w+(y, z) + w−(y, z)] +
N
X
u=1
[w+(y, u) + w−(y, u)])
(3)
If Y (t) is the potential of the conscious neuron y then in n number of neurons, vector Y (t) = (Y1(t), Y2(t), ..., Yn(t))
can be modelled as a continuous-time Markov process. The stationary joint probability of the network is given as:
lim
n→∞P(Y (t)) = y1(t), y2(t), ..., yn(t) =
n
Y
y=1
(1 −qy)qny
y , qy =
Q+
Y
ry + Q−
Y
(4)
4


## Page 5


Figure 3: The interaction among RF, LCF, and UCF in an SCNN. Please note that the switch-like behaviour or ﬁltering rules are enforced by the
positive and negative synaptic weights associated with each input ﬁeld.
Where Q+
Y and Q−
Y are the average rate of +ive and -ive signals at neuron y, given as:
Q+
Y =
N
X
x=1
qxw+(y, x) +
N
X
z=1
qzw+(y, z) +
N
X
u=1
quw+(y, u)
(5)
Q−
Y =
N
X
x=1
qxw−(y, x) +
N
X
z=1
qzw−(y, z) +
N
X
u=1
quw−(y, u)
(6)
The probability that the conscious neuron (Y) is excited can be written as:
qy =
PN
x=1 qxw+(y, x) + PN
z=1 qzw+(y, z) + PN
u=1 quw+(y, u)
[W +
W + W −
W ] + PN
w=1 qxw−(y, x) + PN
z=1 qzw−(y, z) + PN
u=1 quw−(y, u)
(7)
where w+(y, x), w−(y, x), w+(y, z), w−(y, z) w+(y, u), w+(y, u) are the positive and negative RF, LCF, and
UCF weights. W +
W and W −
W are the positive and negative weights between the conscious neuron y and succeeded
neuron w. For training and weights update, state-of-the-art gradient descent algorithm is used. The RF input (qx) is
given as:
qx =
Q+
x
[w(x, y)+ + w(x, y)−] + Q−
x
(8)
Q+
x = Λx +
N
X
v=1
qvw+(x, v)
(9)
Q+
x = λx +
N
X
v=1
qvw−(x, v)
(10)
Where qv is the potential of the preceding neuron v coming from the outside world, and qu and qz in (7) are the
potentials of incoming LCF and UCF. It is to be noted that w(x, y)+ and w(y, x)+ are different.
5


## Page 6


Figure 4: Proposed SCNN: Multi-layered multiunit network of many similar conscious neurons, where the unit in one stream is connected to all
other units in the neighbouring streams of the same layer.
3.2. Information Decomposition
A Venn diagram of the information theoretic measures for distinctive integrated input variables is depicted in
Figure 5, where RF, LCF, and UCF are represented by the green, orange, and grayish pink ellipses respectively. The
output (Y) is represent by the blue ellipse. In information processing equations, the output is denoted by the random
variable Y, whereas RF, LCF, and UCF are represented by X, Z, and U respectively.
The mutual information shared between random variables X (RF) and Y (output) can be written as [14]:
I(X; Y ) = H(X) −H(X|Y )
(11)
Where, H(X) is the Shannon entropy associated with the distribution of X and H(X|Y ) is the Shannon entropy
associated with the conditional distribution of X given Y. It is deﬁned as the information contained in X but not in
Y [14]. It is assumed that the mutual information is always non-negative when random variables are stochastically
independent [14]. Since we are dealing with four random variables, the conditional mutual information can be written
as:
I(X; Y |Z, U) = H(Y |Z, U) −H(Y |X, Z, U)
(12)
6


## Page 7


Figure 5: Venn diagram of information theoretic measures for distinctive integrated input variables RF, LCF, and UCF represented by the green
ellipse, orange ellipse, and grayish pink ellipse respectively. The output (Y) is represent by the blue ellipse. The UCF (U) and associated
H(U|X, Y, Z) is interpreted as the information contained in U but not in X, Y, and Z. The output (Y) and associated H(Y |X, Z, U) is inter-
preted as the information contained in Y but not in X, Z, and U. The LCF (Z) and associated H(Z|X, Y, U) is interpreted as the information
contained in Z but not in X, Y, and U. The RF (X) and associated H(X|Y, Z, U) is interpreted as the information contained in X but not in Y, Z,
and U.
This is the conditional mutual information shared between X and Y, having observed Z and U. It is deﬁned as the
information shared between X and Y but not shared with Z and U.
The four-way mutual information shared among four random variables X, Y, Z, and U can be deﬁned as:
I(X; Y ; Z; U) = I(X; Y ) −I(X; Y |Z, U) = I(X; Z) −I(X; Z|Y, U) =
I(X; U) −I(X; U|Y, Z) = I(Y ; Z) −I(Y ; Z|X, U) = I(Y ; U) −I(Y ; U|X, Z)
(13)
If the four-way mutual information is positive, Shannon entropy associated with the distribution of Y can be deﬁned
as [14]:
H(Y )
=
I(Y ; X; Z; U) + I(Y ; X|Z, U) + I(Y ; Z|X, U) + I(Y ; U|X, Z) + H(Y ; X|Z, U)
(14)
In case the random variables are discrete, the integrals are replaced by summations, and the probability mass
function can be written as [14]:
H(Y ) = −
Z
p(y)logp(y)dy
(15)
H(Y |X) = −
Z Z
p(y|x)logp(y|x)p(x)dydx
(16)
H(Y |X, Z) = −
Z Z Z
p(y|x, z)logp(y|x, z)p(x, z)dydxdz
(17)
H(Y |X, Z, U) = −
Z Z Z Z
p(y|x, z, u)logp(y|x, z, u)p(x, z, u)dydxdzdu
(18)
The objective function to be maximized can be deﬁned as:
F
= φ0I(Y ; X; Z; U) + φ1I(Y ; X|Z, U) + φ2I(Y ; Z|X, U) + φ3I(Y ; U|X, Z) + φ4H(Y ; X|Z, U)
(19)
I(Y ; X|Z, U) is the information that the output shares with the RF (X) and is not contained in the LCF and UCF
units. I(Y ; Z|X, U) is the information that the output shares with the LCF and not contained in the RF and UCF units.
I(Y ; U|X, Z) is the information that the output shares with the UCF and not contained in the RF and LCF units.
7


## Page 8


Figure 6: General human behavioural modelling in any environment N using the conscious neural structure.
Figure 7: Human AV speech processing model in three different environments using the conscious neural structure. Please note that in the ﬁrst two
environments, LCF (visual information from lip movements) has a modulatory role, but in the third environment it has a Null role.
The values of φ′s are tunable within the range [-1, 1]. Different φ values allow investigating speciﬁc mutual/shared
information, such that:
f(x) =









F = I(Y ; X),
if φ1 = 1, φ2 = φ3 = φ4 = 0
F = I(Y ; Z),
if φ2 = 1, φ1 = φ3 = φ4 = 0
F = I(Y ; U),
if φ3 = 1, φ1 = φ2 = φ4 = 0
I(Y ; X; Z; U),
otherwise
4. Human behavioural modelling
Contextual identiﬁcation and transition are two difﬁcult problems. Given any desired human behaviour to be
modelled, a set of appropriate contexts could be identiﬁed and grouped together to develop a computationally efﬁ-
cient model (given a broader understanding of the task in hand). According to the proposed theory in this paper, a
combination of RF, LCF, and UCF can help modelling different human behaviours more precisely. A general human
behavioural model is depicted in Figure 6. The two distinctive input variables RF and LCF are deﬁning the incoming
sensory inputs (e.g., vision and sound), whereas the UCF input is deﬁning the speciﬁc situation (outside world) and
associated anticipated behaviour. In the proposed neural structure, the role of RF and LCF changes with respect to the
outside environment (UCF). To further illustrate the proposed theory, following are the two case studies.
4.1. Case Study 1: Human AV speech processing
Human performance for speech recognition in a noisy environment is known to be dependent upon both aural
and visual cues, which are combined by sophisticated multi-level integration strategies to improve intelligibility [15].
The multimodal nature of the speech is well established in the literature, and it is well understood how speech is
produced by the vibration of vocal folds and conﬁguration of the articulatory organs. The correlation between the
8


## Page 9


visible properties of the articulatory organs (e.g., lips, teeth, tongue) and speech reception has been previously shown in
numerous behavioural studies [1][3][2][4]. Therefore, a clear visibility of some articulatory organs could be effectively
utilized to extract a clean speech signal out of a noisy audio background. Figure 7 depicts the audio-visual speech
processing in three different surrounding environments: Restaurant, Cafe, and Home. In any of the environments,
multisensory information (audio and visual cues) is available all the time but their optimal utilization depends on the
outside environment. For example, in a busy cafe and restaurant environments (multi-talker speech perception), if
there is a high background noise, our brain automatically utilizes other modalities (such as lips, body language, and
facial expressions) to perceive speech or the conveyed message. Therefore, based on the information provided by the
UCF (i.e. outside environment), the roles of LCF and RF are deﬁned. For example, both RF and LCF are active in
the ﬁrst two scenarios (i.e. LCF modulates RF), whereas in the Home scenario (with little or zero noise), lip-reading
is less effective for speech enhancement and indeed of no importance (Null role). This phenomenon is shown in our
previous work at the network level [11], where we showed that lip-reading driven speech enhancement signiﬁcantly
outperforms benchmark audio-only (A-only) speech enhancement approaches (such as spectral subtraction and log-
minimum mean square error) at low signal-to-noise ratios (SNRs). However, at low levels of background noise, visual
cues become less effective.
Figure 8: Audio-visual speech processing: Shallow SCNN - Three streams-three layered multisensory multiunit network of several similar conscious
neurons (where the unit in one stream is connected to all other units in the neighbouring streams). Different surrounding environments deﬁning the
respective anticipated behaviour and establishing the roles of incoming multisensory signals.
To test our proposed theory and SCNN, three distinctive multimodal streams (lip movements as LCF, noisy speech
as RF, and the outside environment as UCF) are used. We studied how LCF and UCF are helping to improve the noisy
speech ﬁltering in different noisy conditions (ranging from a noisy (-12dB SNR) to a little noisy environment (12dB
SNR)). The implemented three streams-three layered SCNN is shown in Figure 8. To train the shallow SCNN, the
deep problem was transformed into a shallow problem. Speciﬁcally, in our previous AV deep learning implementation
[15], the output layer of the LSTM network had 23 log ﬁlter-bank (FB) coefﬁcients (i.e. frame by frame prediction).
In contrast, the evaluated shallow SCNN model predicted one coefﬁcient at a time (i.e. coefﬁcient by coefﬁcient
prediction). In the experiments, neurons interact by exchanging the excitatory and inhibitory spiking signals proba-
bilistically and ﬁre when excited as explained in Section 3. For training, the benchmark AV ChiME3 corpus is used
which is developed by mixing the clean Grid videos [16] with the ChiME3 noises [17] for SNRs ranging from -12dB
to 12dB [11]. The preprocessing includes sentence alignment and incorporation of prior audio and visual frames. Prior
multiple visual frames are used to incorporate temporal information. The audio and visual features were extracted us-
ing log-FB and 2-dimensional discrete cosine transform (2D-DCT) methods. More corpus related and preprocessing
details are comprehensively presented in [11][15]. Figure 9 depicts the prediction of clean logFB coefﬁcients, where it
can be seen that multimodal RF+LCF+UCF model outperformed multimodal RF+LCF (audio-visuals) and unimodal
9


## Page 10


Figure 9: Neural level shallow SCNN performance: Results for A-only (RF), AV (RF+LCF), and AV with UCF, considering 3 prior AV coefﬁcients.
It is to be noted that RF+LCF+UCF model outperforms both RF-only and RF+LCF-only models. The data samples include 2D-logFB (speech) and
2D-DCT (lip movements) coefﬁcients for 1000 utterances from Grid and ChiME3 Corporas (Speaker 1 of the Grid). The number of clean logFB
audio features are 22×205,712. The combined noisy logFB audio features for -12dB, -9dB, -6dB, -3dB, 0dB, 3dB, 6dB, 9dB, and 12dB SNRs are
22×205,712. Similarly, the DCT visual features are 25×205,712 in total. For UCF modelling, ﬁve dynamic real-world commercially-motivated
scenarios are considered: cafe, restaurant, public transport, pedestrian area, and home. Please note that a particular SNR range deﬁnes a particular
environment (UCF), represented by a unique pattern using one-hot-encoding.
Figure 10: Network level lip-reading driven deep learning performance: Stacked LSTM validation results for different prior visual frames. The
ﬁgure on left presents an overall behaviour of an LSTM model when different number of previous visual frames are added. The ﬁgure on right
presents estimated clean logFB audio features using 14 prior visual frames (i.e. actual normalized energy in each of the 23 frequency bands (target,
estimated)). The LSTM network had total 550 LSTM cells in the hidden layer with 23 output neurons [15].
RF (audio-only) models, achieving MSE of 0.051, 0.064, and 0.072 respectively. The performance of a network level
lip-reading driven deep learning approach for speech enhancement is presented in Figure 10 [15]. It is to be noted that
the shallow SCNN with only 29 spiking conscious neurons performed comparably to deep LSTM network which had
550 hidden cell. The ongoing work includes exploiting optimized deep learning driven AV features from [15][11] to
train SCNN.
It is believed that the enhanced learning in an SCNN is due to the shared connections and shared local and universal
contextual information. The SCNN discovered and exploited the associative relations between the features extracted
within each of the RF, LCF, and UCF streams. We believe that the UCF helped establishing the outside environment
and anticipated behaviour and deﬁned the roles of incoming multisensory information with respect to different situ-
ations as shown in Figure 7 (e.g. the use of audio-visual cues and audio-only cues in extreme noisy conditions and
relatively clean conditions respectively). However, to further strengthen our proposed theory, we intend to study the
properties of the conscious neuron(s) using advances in information decomposition methods. Speciﬁcally, we intend
to quantify the suppression and attenuation using partial information decomposition methods and explore the proper-
ties of conscious neuron and its functioning in terms of four basic arithmetic operators and their various forms [6].
Furthermore, we aim to critically analyze how the information is decomposed into components unique to each other
having multiway mutual/shared information in recurrent SCNN.
10


## Page 11


Figure 11: Driver behavioural model in two different environments using conscious neural structure. Please note that the audio cues (defective
audible reversing warning beeps) are represented by ambiguous RF, coming from a defective parking sensors (partially working) which sometimes
miscalculate the nearby object distance. Different surrounding environments (UCF) deﬁning the respective anticipated behaviours and establishing
the roles of incoming multisensory signals. For example, in a car reverse situation with no blind spot, the driver can’t rely only on parking sensors
for precise maneuvering decisions, as the audio input is ambiguous due to defective parking sensors. Therefore, in this situation, the conscious
neuron deﬁnes the role of visual cues (LCF) as modulatory. In contrast, when there is a blind spot, the driver may have to rely on other modulatory
signals to make an optimal decision along with the ambiguous RF.
Figure 12: Driver behavioural modelling with a Shallow SCNN.
4.2. Case Study 2: Driver behavioral model
The gap between humans and machine is shrinking and scientists are trying to develop more human-like comput-
ing devices. It is becoming increasingly important to develop computer systems that incorporate or enhance situation
awareness. However, methods to reduce margins of uncertainty and minimize miscommunication need further explo-
ration. The proposed conscious neural structure and its property of originating a controlled neural command based on
a precise mutisensory signals integration with respect to the external environment can help addressing these modelling
challenges. For example, the proposed SCNN can help modelling a more precise driving behaviour. Figure 11 and
Figure 12 depict the driving behavioural model at a neural and network level in two different surrounding environ-
ments: car reverse with no blind spot and care reverse with blind spot. It is assumed that the parking sensors are not
fully functional and at times they miscalculate the nearby object distance. Therefore, the audio input is ambiguous
and the driver can’t rely only on parking sensors for precise maneuvering decisions. In the ﬁrst situation, where there
is no blind spot, the driver leverages the complementary strengths of both AV cues. The visual cues are modulating
the ambiguous audio signal (RF). In contrast, when there is a blind spot, the driver may have to rely on other mod-
ulatory signals to make an optimal decision along with the ambiguous RF. In a nutshell, in any of the surrounding
11


## Page 12


environments (UCF), multisensory information is available, but depending on the situation, the roles of incoming mul-
tisensory signals are deﬁned to originate a precise control command (driver’s maneuvering decision) complying with
the anticipated behaviour.
5. Discussion, Research Impact, and Future Directions
In this research, we introduced a novel theory on the role of awareness and universal context in an SCNN. The
proposed theory throws light on selective ampliﬁcation and attenuation of incoming multisensory information in the
brain with respect to the external environment and anticipated behaviour. Speciﬁcally, it deﬁnes a guidance frame-
work to study and model human behaviours and their underlying neural functioning in different conditions. The
proposed SCNN is used to model human AV speech processing and driving behaviour. For AV speech modelling, the
SCNN outperformed state-of-the-art multimodal (RF+LCF) and unimodal (RF-only) processing models. Similarly, in
driver behavioural modelling, it is shown that the conscious neuron allows modelling a more precise human driving be-
haviour. We hypothesize that the integration of RF, LCF, and UCF helped SCNN to discover and exploit the associative
relations between the features extracted within each of the RF, LCF, and UCF streams. This integration and the shared
local and universal contextual information enabled enhanced learning. We believe that the inherent SCNN properties
ideally place it as a powerful tool for precise behavioural modelling. However, an in-depth analysis is required to
further study the properties of conscious neuron(s). In the future, we intend to use the advances in information decom-
position to quantify the suppression and attenuation using partial information decomposition methods. Ongoing work
also includes the development of hierarchical deep SCNN (HD-SCNN) by integrating multiple SCNNs responsible
for a speciﬁc human behaviour such as audio processing, visual processing etc. For the training of HD-SCNN, we are
using a theory of hypnosis for the selective training of a subnetwork (single SCNN) without affecting other already
well-trained models. The testing of the proposed theory using biomedical and clinical experimental methods is also a
part of our ongoing work. In subsequent sections, we present the application of SCNN in developing more human-like
computing devices, low-power neuromorphic chips, and modelling sentiment and ﬁnancial behaviours.
5.1. Research Impact
5.1.1. Understanding Neurodegenerative Processes using Biomedical and Clinical Methods
Sensory impairments have an enormous impact on our lives and are closely linked to cognitive functioning. Neu-
rodegenerative processes in Alzheimer’s disease (AD) and Parkinson’s disease (PD) affect the structure and function-
ing of neurons, resulting in altered neuronal activity [18]. However, the cellular and neuronal circuit mechanisms
underlying this disruption are elusive. The patients with AD suffer from sensory impairment and they lack the ability
to channelise awareness. Therefore, it is important to understand how multisensory integration process changes in AD
and why AD patients fail to guide their actions.
Our ongoing work includes designing an appropriate subjective testing protocol using biomedical and clinical
methods to observe the role of RF, LCF, and UCF in processing and learning. For example, study AD and normal mice
to observe differences in their multisensory integration processes with respect to different environmental conditions
(e.g. circadian rhythms). The circadian context could be used as a UCF e.g., to deﬁne day and night along with the
associated expected behaviours. The incoming multisensory information such as information from retinal ganglion
cells (RGCs) could be used as RF/LCF in the proposed computational model. We believe that an integration of
the proposed computational model with biomedical and clinical experiments can help understanding the underlying
disrupted neural processing in different medical conditions. Speciﬁcally, it can help understanding the precise and
imprecise neural ﬁring in normal and neurodegenerative disorder patients respectively, and how different medical
conditions affect the functioning of neurons. The experimental observations in the light of the proposed theory can be
quantiﬁed to develop improved normal/AD/PD models.
5.2. Low-power Neuromorphic Chips and Internet of Things (IoT) Sensors
The controlled ﬁring property of the proposed conscious neural structure can help developing highly energy-
efﬁcient (low-power) neuromorphic chips and IoT sensors. The proposed SCNN inherently leverages the complemen-
tary strengths of incoming multisensory signals with respect to the outside environment and anticipated behaviour. For
example, as explained in case study 1 that in a high background noise, the conscious neuron leverages the comple-
mentary strengths of both visual and audio cues to perceive ambiguous speech. In contrast, in a low background noise,
the audio cues are good enough to solve the problem. Consequently, the synaptic weights associated with the input
12


## Page 13


audio cues in case of a low background noise possess high synaptic strength that leads to ﬁring of relevant neurons
and dysfunctioning of neurons associated with visual cues. This precise neural ﬁring behaviour stops the unnecessary
successive neural processing and power consumption which could be very useful in developing low-power wireless
sensors. Ongoing work also includes the development of low-power neuromorphic chips and IoT sensors based on our
proposed theory.
5.3. Other Real-World Applications
The proposed theory can also be applied to address problems such as developing accurate ﬁnancial market mod-
els, sentiment analysis models etc. The authors in [19] proposed a decision support from ﬁnancial disclosures using
deep neural networks and transfer learning. Speciﬁcally, the authors used deep recurrent neural network (LSTM) to
automatically extract features from ordered sequences of words in order to capture highly non-linear relationships
and context-dependent meanings. The authors demonstrated a higher directional accuracy as compared to traditional
machine learning methods when predicting stock price movements in response to ﬁnancial disclosures. Similar net-
work level multimodal integration has widely been used for applications such as sentiment analysis, emotion recog-
nition, and deception detection [20] [21][22]. For example, the authors in [20] addressed the problem of ambiguous
and context-aware tweets utilizing connected adjacent information with world-level and tweet level context attention.
However, such implementations exploit the temporal contextual information or LCF at the network level with no in-
tegration of the overall knowledge of the problem (awareness) at the neural level, restricting accurate modelling or
precise behavioral representation.
Acknowledgment
This work was supported by the UK Engineering and Physical Sciences Research Council (EPSRC) Grant No.
EP/M026981/1 and deepCI.org. The author would like to greatly acknowledge Prof. Amir Hussain and Mandar Gogate
from the University of Stirling for their contributions in implementing lip-reading driven deep learning approach and
contextual AV switching for speech enhancement, which are published previously and cited here for reference. The
author would also like to acknowledge Prof. Bruce Graham, Prof. Leslie Smith, Prof. Peter Hancock, and Prof.
Bill Phillips from the University of Stirling, Areej Riaz from the London Business School, and Dr Mino Belle and
Prof. Andrew Randall from the University of Exeter for their help and support in several different ways including
appreciation, motivation, and encouragement.
References
[1] W. H. Sumby and I. Pollack, “Visual contribution to speech intelligibility in noise,” The journal of the acoustical
society of america, vol. 26, no. 2, pp. 212–215, 1954.
[2] H. McGurk and J. MacDonald, “Hearing lips and seeing voices,” 1976.
[3] Q. Summerﬁeld, “Use of visual information for phonetic perception,” Phonetica, vol. 36, no. 4-5, pp. 314–331,
1979.
[4] M. L. Patterson and J. F. Werker, “Two-month-old infants match phonetic information in lips and voice,” Devel-
opmental Science, vol. 6, no. 2, pp. 191–196, 2003.
[5] A. J. Gonzalez, B. S. Stensrud, and G. Barrett, “Formalizing context-based reasoning: A modeling paradigm for
representing tactical human behavior,” International Journal of Intelligent Systems, vol. 23, no. 7, pp. 822–847,
2008.
[6] J. W. Kay and W. A. Phillips, “Contrasting information theoretic decompositions of modulatory and arithmetic
interactions in neural information processing systems,” arXiv preprint arXiv:1803.05897, 2018.
[7] B. E. Stein and T. R. Stanford, “Multisensory integration: current issues from the perspective of the single
neuron,” Nature Reviews Neuroscience, vol. 9, no. 4, p. 255, 2008.
[8] B. E. Stein, T. R. Stanford, and B. A. Rowland, “The neural basis of multisensory integration in the midbrain: its
organization and maturation,” Hearing research, vol. 258, no. 1-2, pp. 4–15, 2009.
13


## Page 14


[9] J. Kay, D. Floreano, and W. A. Phillips, “Contextually guided unsupervised learning using local multivariate
binary processors,” Neural Networks, vol. 11, no. 1, pp. 117–140, 1998.
[10] A. Ephrat, I. Mosseri, O. Lang, T. Dekel, K. Wilson, A. Hassidim, W. T. Freeman, and M. Rubinstein, “Looking
to listen at the cocktail party: A speaker-independent audio-visual model for speech separation,” arXiv preprint
arXiv:1804.03619, 2018.
[11] A. Adeel, M. Gogate, and A. Hussain, “Contextual audio-visual switching for speech enhancement in real-world
environments,” arXiv preprint arXiv:1808.09825, 2018.
[12] M. Gogate, A. Adeel, R. Marxer, J. Barker, and A. Hussain, “Dnn driven speaker independent audio-visual mask
estimation for speech separation,” INTERSPEECH, 2018.
[13] E. Gelenbe, “G-networks by triggered customer movement,” Journal of applied probability, vol. 30, no. 3, pp.
742–748, 1993.
[14] J. W. Kay and W. Phillips, “Coherent infomax as a computational goal for neural systems,” Bulletin of mathe-
matical biology, vol. 73, no. 2, pp. 344–372, 2011.
[15] A. Adeel, M. Gogate, A. Hussain, and W. M. Whitmer, “Lip-reading driven deep learning approach for speech
enhancement,” arXiv preprint arXiv:1703.10893, 2018.
[16] M. Cooke, J. Barker, S. Cunningham, and X. Shao, “An audio-visual corpus for speech perception and automatic
speech recognition,” The Journal of the Acoustical Society of America, vol. 120, no. 5, pp. 2421–2424, 2006.
[17] J. Barker, R. Marxer, E. Vincent, and S. Watanabe, “The third chimespeech separation and recognition challenge:
Dataset, task and baselines,” in Automatic Speech Recognition and Understanding (ASRU), 2015 IEEE Workshop
on.
IEEE, 2015, pp. 504–511.
[18] S. Liebscher, G. B. Keller, P. M. Goltstein, T. Bonhoeffer, and M. H¨ubener, “Selective persistence of sensorimotor
mismatch signals in visual cortex of behaving alzheimers disease mice,” Current Biology, vol. 26, no. 7, pp. 956–
964, 2016.
[19] M. Kraus and S. Feuerriegel, “Decision support from ﬁnancial disclosures with deep neural networks and transfer
learning,” Decision Support Systems, vol. 104, pp. 38–48, 2017.
[20] X. Zou, J. Yang, and J. Zhang, “Microblog sentiment analysis using social and topic context,” PloS one, vol. 13,
no. 2, p. e0191163, 2018.
[21] M. Gogate, A. Adeel, and A. Hussain, “A novel brain-inspired compression-based optimised multimodal fusion
for emotion recognition,” in Computational Intelligence (SSCI), 2017 IEEE Symposium Series on.
IEEE, 2017,
pp. 1–7.
[22] Gogate, A. Adeel, and A. Hussain, “Deep learning driven multimodal fusion for automated deception detection,”
in Computational Intelligence (SSCI), 2017 IEEE Symposium Series on.
IEEE, 2017, pp. 1–6.
14

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
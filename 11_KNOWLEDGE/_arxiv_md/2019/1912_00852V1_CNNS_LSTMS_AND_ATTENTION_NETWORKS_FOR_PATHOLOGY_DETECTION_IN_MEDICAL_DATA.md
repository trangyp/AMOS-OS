---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1912.00852v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1912.00852v1_CNNs__LSTMs__and_Attention_Networks_for_Pathology_Detection_in_Medical_Data

> Source: 1912.00852v1_CNNs__LSTMs__and_Attention_Networks_for_Pathology_Detection_in_Medical_Data.pdf

> Pages: 53

---


## Page 1


Aus dem Institut f¨ur Medizinische Informatik der Universit¨at zu L¨ubeck
Direktor: Prof. Dr. rer. nat. habil. Heinz Handels
CNNs, LSTMs, and Attention Networks
for Pathology Detection in Medical Data
CNNs, LSTMs und Attention Netzwerke f¨ur die Detektion von
Pathologien in medizinischen Daten
Masterarbeit
im Rahmen des Studienganges Medizinische Informatik
der Universit¨at zu L¨ubeck
vorgelegt von
Nora Vogt
ausgegeben und betreut von
Prof. Dr. Mattias P. Heinrich
mit Unterst¨utzung von
Dr. Julien Oster1
1 IADI U1254, Charg´e de Recherche (Senior Research Fellow) INSERM
L¨ubeck, den 24. Juli 2018
arXiv:1912.00852v1  [cs.LG]  2 Dec 2019


## Page 2


Abstract
For the weakly supervised task of electrocardiogram (ECG) rhythm classiﬁcation, con-
volutional neural networks (CNNs) and long short-term memory (LSTM) networks
are two increasingly popular classiﬁcation models. This work investigates whether a
combination of both architectures to so-called convolutional long short-term memory
(ConvLSTM) networks can improve classiﬁcation performances by explicitly capturing
morphological as well as temporal features of raw ECG records. In addition, various
attention mechanisms are studied to localize and visualize record sections of abnormal
morphology and irregular rhythm. The resulting saliency maps are supposed to not
only allow for a better network understanding but to also improve clinicians’ accep-
tance of automatic diagnosis in order to avoid the technique being labeled as a black
box. In further experiments, attention mechanisms are actively incorporated into the
training process by learning a few additional attention gating parameters in a CNN
model. An 8-fold cross validation is ﬁnally carried out on the PhysioNet Computing
in Cardiology (CinC) challenge 2017 to compare the performances of standard CNN
models, ConvLSTMs, and attention gated CNNs.


## Page 3


Contents
1
Introduction
1
1.1
Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1
1.2
Related Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2
1.2.1
ECG Rhythm Classiﬁcation . . . . . . . . . . . . . . . . . . . .
2
1.2.2
Attention Mechanisms . . . . . . . . . . . . . . . . . . . . . . .
3
2
Basic Concepts
5
2.1
Electrocardiogram Basics . . . . . . . . . . . . . . . . . . . . . . . . . .
5
2.1.1
Atrial Fibrillation . . . . . . . . . . . . . . . . . . . . . . . . . .
5
2.2
Neural Network Basics . . . . . . . . . . . . . . . . . . . . . . . . . . .
6
2.2.1
Convolutional Neural Networks . . . . . . . . . . . . . . . . . .
7
2.2.2
Recurrent Neural Networks, Long Short-Term Memory Networks,
and Gated Recurrent Unit Networks
. . . . . . . . . . . . . . .
9
3
Methods
14
3.1
Convolutional Long Short-Term Memory Networks
. . . . . . . . . . .
14
3.2
Attention Mechanisms
. . . . . . . . . . . . . . . . . . . . . . . . . . .
15
3.2.1
Class Activation Maps . . . . . . . . . . . . . . . . . . . . . . .
15
3.2.2
Attention Gates . . . . . . . . . . . . . . . . . . . . . . . . . . .
17
3.2.3
Perturbation Masks . . . . . . . . . . . . . . . . . . . . . . . . .
18
4
Material and Experiments
21
4.1
Datasets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
21
4.1.1
The PhysioNet CinC Challenge 2017 . . . . . . . . . . . . . . .
21
4.1.2
The MIT-BIH Arrhythmia Database
. . . . . . . . . . . . . . .
21
4.2
Evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
22
4.3
Network Architectures and Parameterisations
. . . . . . . . . . . . . .
22
4.3.1
Basic Convolutional Neural Network Modules
. . . . . . . . . .
22
4.3.2
Global Pooling Setup . . . . . . . . . . . . . . . . . . . . . . . .
24
4.3.3
Gated Attention Setup . . . . . . . . . . . . . . . . . . . . . . .
24
4.3.4
Convolutional Long Short-Term Memory Network Setup
. . . .
25
4.4
Implementation and Computation Times . . . . . . . . . . . . . . . . .
26
5
Results
28
5.1
Global Pooling Performances . . . . . . . . . . . . . . . . . . . . . . . .
28
5.1.1
Class Activation Map Visualizations
. . . . . . . . . . . . . . .
29
5.2
Gated Attention Network Performances . . . . . . . . . . . . . . . . . .
32
5.3
Convolutional Long Short-Term Memory Network Performances . . . .
32
5.3.1
Sensitivity to Hyperparameters
. . . . . . . . . . . . . . . . . .
32


## Page 4


Contents
iv
5.3.2
Plotting Class Decisions Over Time . . . . . . . . . . . . . . . .
34
5.3.3
Shift Perturbation Mask Visualizations . . . . . . . . . . . . . .
36
5.3.4
Hidden State and Gate Visualizations . . . . . . . . . . . . . . .
37
5.4
Performance Comparisons . . . . . . . . . . . . . . . . . . . . . . . . .
39
6
Discussion
41
6.1
Are ConvLSTMs the Winners of the CinC Challenge? . . . . . . . . . .
41
6.2
Can Attention Visualizations Support AF Diagnosis? . . . . . . . . . .
43
6.3
Are Attention Mechanisms Beneﬁcial for the Training Process? . . . . .
44
7
Conclusion
45
Bibliography
46


## Page 5


Chapter 1
Introduction
As the detection of atrial ﬁbrillation (AF) consists in the examination of long-term
electrocardiograms (ECGs), the diagnosis of cardiac arrhythmias can be very time-
consuming. Especially in cases of paroxysmal AF, episodes of AF might occur infre-
quently and therefore require heart activity records over several days. The aim of this
work is the development of an automatic system for the detection of cardiac arrhythmias
that can yield a fast and accurate diagnosis. Diﬀerent visualization approaches are
proposed to improve the interpretability and to experimentally validate classiﬁcation
outputs. It is suggested that the highlighting of salient ECG sections has the potential
to not only lead to a better acceptance of several compared deep learning models but
to also facilitate the subsequent inspection of clinicians in cases of high prediction
uncertainty.
The next section will give a brief overview of existing state-of-the-art ECG rhythm
classiﬁers, which in many cases rely on (well designed) handcrafted features. Following
the trend of deep learning, we try to evade the engineering part by automatically
extracting a discriminative data representation with neural network architectures. Two
popular architectures for the given task are convolutional neural networks (CNNs) [27]
and recurrent neural networks (RNNs) [14]/ long short-term memory networks (LSTMs)
[21]. While CNNs have proven to be particularly successful in image classiﬁcation tasks
(by learning translation invariant ﬁlters for pattern recognition), RNNs recently yielded
promising achievements for the processing of temporal data (by learning short and
long-range dependencies at diﬀerent scales [17]).
In this work, CNNs and LSTMs will be combined with the goal to ﬁrst learn dis-
criminative patterns and then discover temporal dependencies in a feature sequence.
Besides studying a number of attention visualization approaches, an attention net-
work is presented that is actively incorporating saliency information into the learning
process.
1.1 Motivation
Atrial ﬁbrillation is the most common cardiac arrhythmia with a population prevalence
of 1-2 % [28] and is known to be associated with a number of cardiovascular diseases
(causing heart failure, ischemia, stroke, and even cardiac death [33]). The treatment of
AF (drugs or ablation procedure) should be started as early as possible which implies


## Page 6


Chapter 1 Introduction
2
that accurate diagnostic tools are strongly needed. To encourage the development of
automatic diagnosis systems, the PhysioNet community [18] provides access to a large
collection of physiological (and particularly cardiac) databases. For the PhysioNet
Computing in Cardiology (CinC) challenge 2017 [11] 8528 short single lead ECG
recordings were made available for the purpose of AF classiﬁcation. Even though the
challenge is over by now, the hidden test set is kept private for further submissions.
The CinC dataset (each record being annotated with one global rhythm label) will
be used to evaluate the performance of our models. For a better validation of our
attention visualization approaches, we furthermore considered the MIT-BIH database
[32] (provided by the MIT and Boston’s Beth Israel Hospital) which oﬀers a beat-
wise annotation and therefore allows for an easier interpretation of obtained attention
outputs.
1.2 Related Work
This brief overview of related AF classiﬁcation systems focuses on recent attempts
to combine both CNNs and LSTMs for the application of ECG processing.
The
discussion of convolutional long short-term memory networks (ConvLSTMs) for other
applications would go beyond the scope of this introduction. Still, it is worth mentioning
that ConvLSTMs already were successfully applied in many other tasks such as sleep
stage scoring on EEG data [46], weather forecasting [43], and gesture recognition
(outperforming both plain CNNs and plain LSTMs) [49]. Finally, work in the area of
recent attention mechanism and attention network variants and applications will be
reviewed.
1.2.1 ECG Rhythm Classiﬁcation
Following the analysis of a literature study by Jangra et al. [22], established ECG
classiﬁers typically include a preprocessing (e.g. removing noise and artifacts), a feature
extraction, a feature space dimensionality reduction (e.g. performing independent
component analysis), and a classiﬁer module. The feature extraction part aims at
describing the signal by morphological, temporal, and statistical features and is often
based on cardiologists’ expert knowledge. Typical features are, for instance, capturing
information about the extrema of waveforms, RR intervals, QRS complex durations,
and wavelet transforms [22]. In their overview of state-of-the-art algorithms, Jangra et
al. name, among others, feed forward networks [31], probabilistic networks [31], support
vector machines [31], fuzzy neural networks [44], radial basis function neural networks
[53], and random forest algorithms [15].
CinC 2017 challenge participants
Some of the before mentioned algorithms did
also participate in the CinC challenge 2017 (see [11] for all 75 participating teams).
Amongst the submissions are support vector machines [4], random forest classiﬁers
[55], CNNs [39], RNNs [48], and also some ConvLSTMs [1], [51]. One of the winning


## Page 7


Chapter 1 Introduction
3
teams that reached an average F1 score of 0.83 were Teijeiro et al. [48]. They combined
an LSTM network with a tree gradient boosting (XGBoost) classiﬁer and utilized the
Construe algorithm in order to ﬁnd “same features as used by cardiologists” regarding
morphology, rhythm and signal quality.
A slightly worse F1 score of 0.82 (while using a less complex architecture, but processing
the ECG records as logarithmic spectrograms) was achieved by Zihlmann et al. [60].
They combined a deep CNN with a multi-layer bidirectional LSTM for the temporal
aggregation of features. The authors also compared the performances of LSTMs and
temporal average pooling operations and showed that the LSTM slightly outperformed
the pooling variant in case data augmentation was employed. Reviewing their exper-
iments, Zihlmann et al. did not observe great performance diﬀerences between the
two variants. Still, they formulated the hypothesis that the aggregated feature vector
provided by an LSTM could potentially better preserve episodic phenomena than a
simple pooling layer. Another team processed raw ECG data using a ConvLSTM with
only one CNN layer and thereby obtained an F1 score of 0.80 without requiring any
pre-processing of the data [51].
Despite the comparably large amount of submitted RNN approaches, there were also
teams applying pure CNNs or pure LSTMs only. The densely connected CNN of
Rubin et al. [39], for instance, processed time-frequency representations of the data
and achieved an F1 score of 0.80. The team additionally incorporated information
about the signal quality to immediately classify some records as noisy and furthermore
used an Ada-Boost classiﬁer in a post-processing step. Another pure CNN architecture
was the one-layer CNN architecture of Chandra et al. [6], which processed heartbeat
windows centered at detected R-peaks but only achieved an F1 score of 0.71. A pure
LSTM, on the contrary, was submitted by Maknicka et al. [29], who used pre-computed
QRS features as input to a multi-layer LSTM and thereby achieved an F1 score of
0.78.
Observing that many approaches of the challenge used complex pre- or post-processing
steps, this work aims at setting up a simpler architecture which only relies on CNN and
LSTM modules and allows for the processing of raw ECG data. Since CNNs proved
to be promising feature extractors for the given task, the focus of our work is the
comparison of diﬀerent temporal feature aggregation strategies (comparing particularly
simple pooling layers with more complex LSTM modules).
1.2.2 Attention Mechanisms
First neural network attention mechanisms were proposed for CNNs, being either
applied in a post-processing step (after a networks training had ﬁnished) [45], [58] or
integrated into the learning process (requiring the optimization of additional attention
parameters) [3], [41].
In some of the ﬁrst works, Zeiler et al. [57] used deconvolutional networks to trace high
neuron activations back to the image space. By visualizing resulting attention maps, the
authors managed to identify input objects and patterns that were of highest relevance


## Page 8


Chapter 1 Introduction
4
for the prediction of the network. In this work, we will study the attention visualization
approach that was proposed by Zhou et al. [59] in 2016 and has subsequently been
successfully applied by Wang et al. [50] for the weakly supervised localization of thorax
diseases in chest X-ray images. It was found that the proposed class activation map
(CAM) concept provides a convenient way to highlight salient input regions as it only
requires a few modiﬁcations of the standard CNN classiﬁer part.
In another work, Fong et al. [16] introduced model independent attention maps that
are based on the computation of occlusion masks. By masking out most informative
input pixels (with e.g. a constant value or noise), evidences that led to the original
class decision are removed and networks consequently are fooled. Westhuizen et al. [52]
recently applied a ‘zero perturbation’ occlusion mask for heartbeat windows of the MIT-
BIH database. It is assumed that for the rhythm classiﬁcation task the expressiveness of
resulting attention maps can be further improved by a more realistic perturbation variant.
For this reason, the estimation of a deformation grid that applies a temporally varying
shift to the ECG data will be introduced and explored in Sec. 3.2.
Beside the idea of visualizing attention, there has been some further research on how
to beneﬁt from attention to improve the performance of networks. So-called attention
networks are motivated by the human visual attention system and have before, for
instance, successfully improved ﬁne-grained object classiﬁcations [58]. Some further
networks were proposed that learned to apply suppression masks [26], to “look and
think twice” [5], or to “pay more attention to attention” [56]. This work studies
attention gated CNNs that aim at incorporating the most contextually ‘useful’ features
of multiple network layers to more explicitly provide features at diﬀerent resolutions.
Those networks were introduced by Jetley et al. [23], were extended by Oktay et
al. [34] for the task of organ localization in abdominal CTs and also showed to improve
ultrasound scan plane detections [41].


## Page 9


Chapter 2
Basic Concepts
After a short introduction to electrocardiograms and the diagnosis of atrial ﬁbrillation,
this section presents the basic concepts of ﬁrst, CNNs and second, RNN architec-
tures.
2.1 Electrocardiogram Basics
Since the recording of electrical heart activity conveniently visualizes depolarization
and repolarization disorders of cardiac ﬁbers, the detection of cardiac arrhythmias is
commonly based on the examination of ECGs (where disorders are indicated by changes
of the P, Q, R, S, and T wave amplitudes and intervals).
Figure 2.1a shows a diagram of a typical healthy heartbeat that represents a normal
cardiac contraction cycle.
Its shape originates from the electrical activity of the
following processes: the depolarization of the atrial muscle ﬁbers and pass through
the atrioventricular (AV) node (P wave), the activation of the muscle ﬁbers in the
ventricles (QRS complex), the plateau of the ventricular action potential (ST), and the
repolarization of the ventricles (T wave) [42].
Regarding the classiﬁcation task of the CinC challenge 2017, normal sinus rhythms (N),
atrial ﬁbrillation (AF), other rhythms (O), and signals that are too noisy to be classiﬁed
(∼) are to be distinguished (see Fig. 2.1b for example signals). Cardiac rhythm changes
(that can be of permanent or episodic nature) typically arise if the cardiac cycle of the
sinus rhythm is disturbed by, for instance, abnormal electrical activations originating
from the atria, the AV node, or the ventricles.
2.1.1 Atrial Fibrillation
Atrial ﬁbrillation is caused by chaotic electrical activations in the atria and results in
irregular heart contractions that disturb the mechanical functions of the heart and also
aﬀect the whole cardiac-vascular system (potentially leading to heart failure, stroke,
coronary artery disease and the risk of death [18]). The development of reliable AF detec-
tors is therefore important but at the same time challenging due to episodic occurrences
of AF, noisy clinical data, and the diﬀerentiation between AF and other arrhythmias
which show similar ECG features (like irregular RR intervals).


## Page 10


Chapter 2 Basic Concepts
6
P
Q
R
S
T
QRS complex
ST segment
PR segment
PR interval
QT interval
(a)
−1
0
1
Amplitude (mV)
Normal rhythm
Recording−−A00001
−1
0
1
2
Amplitude (mV)
AF rhythm
Recording−−A00004
−2
0
2
Amplitude (mV)
Other rhythm
Recording−−A00077
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
−5
0
5
Amplitude (mV)
Time (s)
Noisy recording
Recording−−A01246
(b)
Figure 2.1: (a) Schema of an ECG curve and (b) example records of the CinC database. Source: [11].
AF related ECG appearances
In cases of AF, irregular RR intervals result from
the ﬁbrillation of the atria which excites the AV node at a very high rate. This in turn,
causes the AV node to ﬁre in a chaotic and highly irregular pattern and consequently
leads to an irregular polarization of the ventricles. It furthermore aﬀects the morphology
of the sinus waveform in such a way that the ‘traditional’ P wave is replaced with the
appearance of low amplitude f waves. That is why common AF classiﬁcation systems
need to capture both abnormal morphologies and rhythm changes.
Class Other related ECG appearances
As the class Other comprises various
cardiac pathologies, possible appearances are more diﬃcult to summarize than those of
the AF class. Figure 2.2 shows a few examples of popular rhythm disorders that were
presented in [38]. It is to be noted, that those examples were not extracted from the
CinC database. Still, the selection of records conveniently shows the variety of other
rhythm types and illustrates the challenge of representing all those abnormalities with
a training set of less than ten thousand patients. Further challenges are introduced
by the presence of noise and varying heart rates (with a rate of more than 100 beats
per minute (bpm) being referred to as tachycardia and one of less than 60 bpm being
referred to as bradycardia). As it can be seen in Fig. 2.2, class Other records show
similar RR interval changes as AF records but often also exhibit morphology changes
of e.g. the QRS complex.
2.2 Neural Network Basics
In the following section, four commonly applied network architectures will be introduced
for the task of ECG classiﬁcation: convolutional neural networks (CNNs) [27], vanilla


## Page 11


Chapter 2 Basic Concepts
7
Ventricular
Bigeminy
CompleteHeart
Block
Ectopic
Atrial
Rhythm
Idioventricular
Rhythm
Junctional
Rhythm
Supraventricular
Tachycardia
Ventricular
Trigeminy
Ventricular
Tachycardia
Wenckebach
(Mobitz I)
Description
Example
Atrial Fibrilla-
tion
Atrial Flutter
Second degree
AV Block Type
2(Mobitz II)
Description
Example
Description
Example
Figure 2.2: ECG record examples showing the variety of common cardiac arrhythmias. Source: [38].
recurrent neural networks (RNNs) [14], long short-term memory networks (LSTMs)
[21], and gated recurrent unit networks (GRUs) [9].
Throughout this work, a weakly supervised classiﬁcation setup will be considered where
each ECG record X = x0, x2, ..., xN−1 of length N is assigned with one target rhythm
label c ∈1, 2, ..., C. For this purpose, all network architectures will apply a ﬁnal
fully connected classiﬁer layer with softmax activation to yield a pseudo-probability
ˆyc ∈[0, 1] for each possible output class c. In the following, the network speciﬁc
ways of extracting and processing class discriminative features of the input will be
studied.
2.2.1 Convolutional Neural Networks
Beside many successes in image processing tasks, CNNs were recently also applied to ac-
curately classify temporal data. Two key aspects that make CNNs such powerful are loca-
tion invariance and the composing of increasingly complex features.
The concept of feature maps
Location invariance is achieved by convolving input
images (or signals) with shared ﬁlters which allows for the detection of same patterns
at diﬀerent locations of the input. It has been shown that ﬁrst layers extract simple
features like edges and subsequent layers gradually build up more complex features
by combining the patterns of the preceding layer (building shapes from edges, object
parts from shapes and ﬁnally entire objects from object parts). The number of patterns
which can be detected by a layer depends on its number of channels since each channel
learns one ﬁlter for the convolution. The channel-wise ﬁlter responses (feature detected


## Page 12


Chapter 2 Basic Concepts
8
Figure 2.3: Convolutional neural network architecture using global pooling for the channel-wise
aggregation of features to obtain a ﬁxed sized vector that can be passed to the classiﬁcation
layer.
or not) result from the convolution of a channel ﬁlter with the input of the layer and
are stored in so-called feature maps.
More formally, the output activations of the jth channel for a given layer l are the results
of the convolution of an input activation ain with a shared ﬁlter w:
al
out,j = f(
Cl
in−1
X
k=0
wl
j ∗al
in,k + bl
j).
(2.1)
If the input ain consists of several channels, the convolution (denoted as ∗) is performed
and summed up over all Cin input channels. Commonly, a non-linearity f is afterward
applied to the output to yield the output activations aout,j. One example of such a non-
linear function is the rectiﬁed linear unit (ReLU) which computes:
ReLU(zl
j) = max(0, zl
j).
(2.2)
Global pooling for weakly supervised classiﬁcation
For global classiﬁcation
tasks, the output feature map of the last convolution layer needs to be reduced to a
ﬁxed size vector before being passed to a ﬁnal classiﬁcation layer (see Fig. 2.3). For
this task, a global pooling operation is applied (e.g. global maximum pooling (GMP)
or global average pooling (GAP)). Let aL
out(n) be the output activations of the last
convolutional layer L at temporal (or spatial) location n. To channel-wise aggregate
features to one scalar, the global average pooling for each channel j is deﬁned as:
gapL
j = 1
N
N−1
X
n=0
aL
out,j(n).
(2.3)


## Page 13


Chapter 2 Basic Concepts
9
The resulting feature vector is subsequently connected to all C neurons of the classiﬁca-
tion layer (with each connection holding one weight wj,c). The linear classiﬁcation layer
is then computing output scores sc for each neuron c:
sc =
CL
out−1
X
k=0
wk,cgapL
k + bc,
(2.4)
with CL
out −1 again being the number of channels in the last convolutional layer. Finally,
a softmax function can be applied to squash the output scores into the range [0, 1],
summing up to 1 over all C classes:
softmax(sc) =
exp(sc)
PC
c=1 exp(sc)
.
(2.5)
Both shared weights and intermediate pooling layers have a positive eﬀect on the
generalization abilities of a network. Since pooling layers discard information about
location of patterns, they introduce both translation as well as some scaling invari-
ance.
2.2.2 Recurrent Neural Networks, Long Short-Term Memory
Networks, and Gated Recurrent Unit Networks
Recurrent neural networks have been introduced for the analysis of data that is changing
over time.
Popular applications are, for instance, speech recognition [40], image
captioning [8], or character prediction for the impressive generation of (almost compiling)
source code [25]). An idea that comes along with the processing of time series is that
the output of a neuron should not only depend on a given time step input but rather
on information of the (entire) past. To allow the network to memorize and to access
input histories, so-called recurrent connections are inserted. Figure 2.4a illustrates such
a residual connection which is basically a simple feedback loops from a cell to itself.
This section will ﬁrst study the realization of internal memories for standard (vanilla)
RNNs and will afterward present the two most popular RNN variants that are LSTMs
and gated recurrent unit networks (GRUs).
Vanilla recurrent neural networks
The loop that is introduced by a recurrent
connection is often visualized in a ‘time-unrolled’ way. Figure 2.4a depicts the resulting
sequential graph as a chain of repeated cell modules (where the number of repetitions
corresponds to the number of inputs in the input sequence). Regarding vanilla RNNs,
those modules are simply repeated tanh layers, where a module output at time t is
deﬁned as [35]:
ht = tanh(Whhht−1 + Wxhxt),
(2.6)
using the tanh function:
tanh(x) = ex −e−x
ex + e−x.
(2.7)


## Page 14


Chapter 2 Basic Concepts
10
hz
h
t-1
t
t+1
t+1
t
t-1
ht-1
ht
ht+1
Wxh
Whh
Whz
Whz
Whz
Whh
Wxh
Wxh
xh
Whh
Whh
z
z
z
z
x
x
x
x
W
W
(a)
1-layer RNN
3-layer RNN
(b)
Figure 2.4: (a) RNN with a recurrent connection visualized as recursive graph (left) and as unrolled
sequential time graph (right). Source: [8]. (b) Many-to-many RNN performing a sequence-
to-sequence prediction (left). Multi-layer variant where each RNN layer receives the
hidden state sequence of the previous layer as input (right). Source: [19].
Thus, the cell holds a weight for both, outputs of the last time step hidden state ht−1
(Whh) and new input xt (Wxh). By updating the parameters of the weight matrices,
the cell learns to memorize information of the past and to decide which information to
keep or to overwrite by new inputs.
Depending on the application, RNNs can, among others, be applied for sequence-to-
sequence predictions (many-to-many RNNs) or, as in case of ECG rhythm classiﬁcation,
for the predictions of global class labels after the processing of all input samples has
ﬁnished (many-to-one RNNs). For both variants, the hidden states serve as hidden
representation of the inputs and are passed to the classiﬁcation layer for the class
prediction. Softmax scores at time step t are computed as:
zt = softmax(Whzht + bz),
(2.8)
with Whz, bz, as usual, being the weights and the bias of the output layer.
As it is the case for multi-layer CNNs, it is possible to stack multiple layers of RNNs
in order to built up temporal features hierarchically. For multi-layer RNNs, each
RNN layer receives the hidden state sequence of the previous layer as input (see
Fig. 2.4b). Hermans et al. [19] argue that for the application of speech recognition such
a hierarchy corresponds to a processing of time series at several time scales (building
up features of words, phrases, sentences, and ﬁnally, full conversations at the highest
level).
Looking at the unrolled RNN visualization of Fig. 2.4a, it becomes apparent that
the weights Wxh, Whh, and Whz are shared across all time steps. Given the global
classiﬁcation approach, the class prediction is performed after the processing of the
entire sequence (that is after the last time step T). As for CNNs, the loss (here the
cross-entropy loss) is ﬁrst computed in a forward pass. In a subsequent backward
pass, the partial error derivatives w.r.t. the network parameters (weights and biases)
are then computed for the Stochastic Gradient Descent (SGD) update. Given that
the RNN output zT depends on all previous time steps, backpropagation for RNNs
is backpropagation through time (BPTT) and associated with a recursive application
of the chain rule. A detailed derivation of the BPTT formulas can be found in a
publication of Chen et al. [8]. Here, only one formula is given in order to hint the


## Page 15


Chapter 2 Basic Concepts
11
gt
ct
i t
ot
f t
W
Wxi
Whi
W
Who
Wxf
Whf
h t
x t
h t-1
h t-1
x t
h t-1
x t
Candidate gate
Input gate
Output gate
Forget gate
Cell state
Wxg
hg
xo
Figure 2.5: LSTM cell structure showing the relations between the hidden state ht, the cell state ct
and the four cell gates which determine the accessing of the cell memory. Source: [8].
problem that arises for the processing of very long sequences. Following Chen et al.,
the derivative for the weight Whh (when considering a cross-entropy loss) is given by
[8]:
∂L
∂Whh
=
X
t
t+1
X
k=1
∂L(t + 1)
∂zt+1
∂zt+1
∂ht+1
∂ht+1
∂hk
∂hk
∂Whh
.
(2.9)
It can be deducted from this formula that gradients are aggregated over the whole time
sequence length T. As this aggregation can include the multiplication of a large number
of small factors, gradients are at risk to get increasingly small.
Long short-term memory networks
Given the fact that this popular ‘vanishing
gradient’ problem can impede the learning process severely, LSTMs were proposed to
better control the gradient ﬂow. The LSTM cell formulation is for this reason extended
by the deﬁnition of gate units and a memory state [8]. Figure 2.5 illustrates the structure
of such an LSTM unit including the input, output, candidate, and forget gates that are
known to enable the memory storage for long sequences (by e.g. keeping the cell from
being overwhelmed by irrelevant inputs). For each sample xt of the input sequence an
LSTM unit computes the following functions at time step t [37]:
Input gate:
it = σ(Wxixt + bxi + Whiht−1 + bhi)
(2.10)
Forget gate:
ft = σ(Wxfxt + bxf + Whfht−1 + bhf)
(2.11)
Output gate:
ot = σ(Wxoxt + bxo + Whoht−1 + bho)
(2.12)
Candidate gate:
gt = tanh(Wxgxt + bxg + Whght−1 + bhg)
(2.13)


## Page 16


Chapter 2 Basic Concepts
12
LSTM
LSTM
LSTM
LSTM
LSTM
LSTM
x N-1
x 0
x 1
...
...
Backward
Forward
Figure 2.6: Bidirectional LSTM concatenating the last hidden states of the forward and the backward
pass as input to the classiﬁcation layer.
Hidden state:
ht = ot tanh(ct)
(2.14)
Cell state:
ct = ftct−1 + itgt
(2.15)
where ht−1 and ct−1 are the hidden state and the cell state of the previous time step
(or the initial states at time step t = 0). The gates apply the sigmoid function σ:
σ(x) =
1
1 + exp(−x)
(2.16)
to compute scalars in the range [0, 1] (to either let all information pass by opening the
gates which is corresponding to a value of 1 or to not let any information pass with a
value of 0).
While the cell state ct is considered to be a long-term memory, the hidden state ht
rather represents the working memory which focuses on immediately useful information
of the long-term memory [8]. The hidden state is therefore claimed to be a sharped
version of the cell state (since it results from a multiplication of the cell state with the
output gate, which limits the information that is passed on) [7]. During the training
process, the LSTM adapts the weights W that are associated with all gates to learn
which information to remember, to update, and to pay attention to. Short, it learns a
good feature representation ht of the data, which ﬁnally can be used as input for the
classiﬁcation layer.
Bidirectional long short-term memory networks
Bidirectional LSTMs can be
beneﬁcial in setups where an output at a given time step not only depends on the past
but also on the future information. The idea is to basically train two independent LSTM
units, one ‘forward’ LSTM that processes the input sequence with regular (0, .., N −1)
time order and a second ‘backward’ LSTM with reversed time order (N −1, .., 0)
processing. To combine information of both directions, the forward and the backward
hidden states are concatenated at each time step. For many-to-one LSTMs, commonly,
the hidden states hN−1 and h0 are concatenated for the forward and the backward
LSTM, respectively (see Fig. 2.6).


## Page 17


Chapter 2 Basic Concepts
13
Gated recurrent unit neural networks
GRUs are a simpliﬁed LSTM variant using
a merged formulation of the cell and the hidden state as well as a merged formulation
of the forget and the input gate into a single update gate (resulting in a total number
of three gates). For each element in the input sequence, a GRU unit computes the
following functions [37]:
Reset gate:
rt = σ(Wirxt + bir + Whrht−1 + bhr)
(2.17)
Update gate:
zt = σ(Wizxt + biz + Whzht−1 + bhz)
(2.18)
New gate:
nt = tanh(Winxt + bin + rt(Whnht−1 + bhn))
(2.19)
Hidden state:
ht = (1 −zt)nt + ztht−1.
(2.20)


## Page 18


Chapter 3
Methods
As already discussed in Sec. 1.2, many researchers are interested in combining the
beneﬁts of CNN and LSTM architectures. They suggest that using CNN modules
for the hierarchical feature extraction task and a subsequent application of LSTM
layers can help to capture temporal long-range dependencies in the feature sequence.
Following the ConvLSTM motivation of Sainath et al. [40], “CNNs are good at reducing
frequency variations, LSTMs are good at temporal modeling, and deep neural networks
are appropriate for mapping features to a more separable space”. After explaining the
general ConvLSTM setup used in this work, two attention mechanisms that can be
applied for CNN architectures will be introduced. In addition, a network independent
variant will be presented, that yields attention maps by computing perturbation masks
for network inputs.
3.1 Convolutional Long Short-Term Memory
Networks
Figure 3.1 shows the general setup of the ConvLSTM architecture used throughout this
work. Feature vectors were extracted for each temporal location of the last CNN layer
to deﬁne the input sequence for the LSTM module. The number of feature channels
thereby deﬁned the size of the feature vectors. In this work, we aimed at a simple data
presentation and therefore proposed to present raw ECG data to the CNN module.
However, it is also possible to previously transform the data into other representations
(like logarithmic spectrograms [60]).
The task of the CNN is to extract a sequence of high-level features that can be easier
processed by the LSTM than the raw ECG data representation. The deeper the CNN
network (and the more pooling layers are applied), the smaller the feature map of the
last layer becomes. If an LSTM would be applied on the raw ECG data instead, the
parameter updates would require the backpropagation through all time steps (that
are up to 18300 samples for the CinC challenge records). That is why a processing
of raw data is often unfeasible for long sequences and the preceding feature sequence
extraction of the CNN can help to reduce the number of time steps for the error
propagation.


## Page 19


Chapter 3 Methods
15
Figure 3.1: ConvLSTM example setup using many-to-one inference. CNN feature vectors are ex-
tracted for each temporal sample (where the dimension of the feature vector corresponds
to the amount of channels in the feature map) and are processed as a sequence by the
LSTM. The LSTM is returning one hidden state at each time step and passes the last
hidden state to the classiﬁcation layer.
Given the global classiﬁcation task, in this work, a many-to-one LSTM is proposed.
The many-to-one LSTM computes one hidden state for each input time step but only
passes the last hidden state to the classiﬁcation layer (see Fig. 3.1). It is assumed
that the last hidden state incorporates memory information about the whole input
sequence and implicitly represents those input features that were detected earlier in the
sequence. Some recent works attempted to improve the incorporation of intermediate
time step outputs by computing attention weighted combinations of hidden states (see
for instance [3]).
3.2 Attention Mechanisms
So far, there has been a range of attempts to visualize the internal processes of neural
network models. In this section, we will ﬁrst study the simple concept of class activation
maps (CAMs) [59] which provide heat maps that localize most important samples for
the class decision. The related approach of attention gated CNNs [41] furthermore uses
internal attention parameters to actively highlight or suppress information during the
training process. This section afterward concludes with a presentation of perturbation
masks, which are not restricted to the application of CNNs and derive attention maps
by manipulating input data.
3.2.1 Class Activation Maps
Figure 3.2 illustrates the basic architecture of Zhou’s et al. [59] saliency visualization
module, which requires the insertion of a global pooling layer and a fully connected
output layer after the last convolutional layer of a given CNN network. As discussed
in Sec. 2.2.1, each channel of a feature map within the network shows the presence or
absence of one particular pattern (with patterns getting more and more complex with


## Page 20


Chapter 3 Methods
16
Australian
terrier
...
C
O
N
V
C
O
N
V
C
O
N
V
C
O
N
V
C
O
N
V
GAP
...
w1
w2
wn
w1 *
+ w2 *
+ … + wn *
Class
Activation
Map
(Australian terrier)
=
C
O
N
V
Class Activation Mapping
Figure 3.2: Class activation map computation for the task of weakly supervised object localization.
CAMs are computed as weighted linear sum of upsampled feature maps and weights that
connect the globally pooled feature vector to the classiﬁcation layer. Resulting attention
maps can be interpreted as conﬁdence maps that highlight most informative regions for
the given class prediction. Source: [59].
increasing network depth). After the CNN layers have completed the feature extraction
part, the fully connected classiﬁcation layer is supposed to learn which of the detected
patterns are discriminative for each of the possible output classes.
Fig. 3.2 demonstrates this concept for a simple example input. If, for instance, the
pattern ‘dog nose’ was detected in a given image (the associated feature map is colored in
green), the output neuron that represents the class ‘Australien terrier’ will get assigned
a high weight wn during the training process. The feature ‘human face’ (represented by
the blue colored feature map), in contrast, will probably get assigned a weight w1 close
to zero. The global pooling layer is ﬁnally needed to reduce the spatial dimensions
of each feature map channel to a scalar value that can afterward be passed to the
classiﬁcation layer (as it has been earlier discussed in Sec. 2.2.1). The most commonly
applied pooling variants are global average pooling, global max pooling, and log-sum-exp
(LSE) pooling [50].
Even though the discarding of location information of detected patterns is supposed to
not signiﬁcantly damage the global classiﬁcation performance, location information is
often desired for weakly supervised localization tasks. That is why Zhou et al. proposed
to recover location information by the computation of class activation maps. They
are doing so by ﬁrstly upsampling the last layer feature maps, secondly extracting the
weights that are connecting each pooled scalar to a given output neuron and thirdly
computing the weighted linear combination of weights and upsampled maps. More
formally, the class activation map for output neuron c can be computed as weighted
linear sum:
CAMc =
CL
out−1
X
k=0
wk,cAL
out,k,
(3.1)


## Page 21


Chapter 3 Methods
17
Figure 3.3: Attention gate network introduced for the application of ultrasound scan plane detection.
While the upper path shows the before described CNN setup with a global pooling layer,
the network also comprises two attention paths. In those paths, intermediate feature
maps are weighted according to attention weights that are deﬁned by similarity scores to
the last layer feature map. Again, the gated attention maps of both paths are globally
pooled in order to provide feature vectors that are then, together with the upper layers
feature vector, passed to the classiﬁcation layer. Source: [41].
where AL
out,k is the upsampled last layer feature map of channel k and wk,c the weight
connecting the pooled output of the given channel with the output neuron c. The result
of this computation is a likelihood conﬁdence map that allows to localize discriminative
input regions for a given class prediction. Due to the required upsampling step, CAMs
often provide rather rough localization of salient patterns (where the resolution of the
map again depends on the parameterisation of the CNN).
3.2.2 Attention Gates
Schlemper et al. [41] argue that the application of global pooling layers forces CNN
networks to extract the most salient features only on a very global level and that
more local information should be preserved. By inserting attention gates at multiple
CNN layers, they aim at incorporating salient information of diﬀerent scales into the
classiﬁcation.
Figure 3.3 shows an example setup of their attention gated CNN architecture. While the
upper network path represents a standard CNN applying a global pooling after the last
convolutional layer, the network holds two additional attention paths. For each attention
path, Schlemper et al. ﬁrst extract an intermediate feature map, then weight the map
according to a gating grid (that assigns one attention weight for each pixel location)
and subsequently perform a global pooling to reduce the resulting gated attention map
to a vector. The obtained vectors of all paths are afterward passed to the classiﬁcation


## Page 22


Chapter 3 Methods
18
layer (e.g. using a concatenation strategy, where all vectors are concatenated before
being passed to the last layer). To obtain the attention weights for each spatial location
of a given intermediate feature map, Schlemper et al. compute compatibility scores to
a global context grid. In their work, this global context grid is simply the feature map
of the last layer (before the global pooling is applied). Attention coeﬃcients are then
deﬁned by the following additive attention formula [41]:
αl
i = σ2(ψT(σ1(W T
x xl
i + W T
c ci + bc)) + bφ),
(3.2)
with Wx, Wc, ψ, bc, and bφ being learnable parameters (implemented as 1 × 1 convo-
lutions), σ2 the sigmoid function and ci a global context (gating) vector of the grid
extracted at pixel location i. The motivation behind this complex similarity measure
is the learning of a nonlinear, expressive relation between the intermediate and the
last layer feature maps [41]. The actual ‘gating’ is then a simple element-wise multi-
plication of feature maps and attention coeﬃcients. For each layer l it is deﬁned as:
ˆxl
i,k = xl
i,k · αl
i,
(3.3)
where αl
i is a scalar value for each pixel vector xl
i,k (which is shared over all feature
map channels k). Finally, the weighted feature map of a given layer l is pooled to
a single output vector by simply summing all feature vectors over all pixel locations:
gl =
n
X
i=1
ˆxi.
(3.4)
Beside concatenating all attention gated vectors gl, it is also possible to train fully
connected layers for each of the paths independently. The output scores of all clas-
siﬁcation layers can then be combined utilizing e.g. an average or a maximum vot-
ing.
3.2.3 Perturbation Masks
So far, only network architecture dependent attention visualization techniques were
discussed that require the extraction of some internal parameters or even introduce
additional parameters. Fong et al. [16], on the contrary, recently introduced a more
general solution that can be applied to any model after training has ﬁnished. Their
attention approach is inspired by the idea of a ‘deletion game’ that progressively takes
evidence from the input by perturbing salient regions (using diﬀerent perturbation types
like blur, constant occlusion values, or noise) in order to drop the conﬁdence scores
of an initial class prediction. Resulting ‘occlusion masks’ identify those input pixels
that had the highest impact on a model prediction and can therefore be considered as
(inverse) attention maps.
In order to ﬁnd an occlusion mask m that leads to a maximal drop of the initial
prediction score, Fong et al. formulate an stochastic gradient descent optimization task.


## Page 23


Chapter 3 Methods
19
Normal
LBBB
Vﬁb
Paced
0
1
Figure 3.4: Occlusion mask examples that have been reported for the task of MIT-BIH heartbeat
classiﬁcation (showing from left to right a normal beat, a left bundle branch block beat
(LBBB), a paced beat and a ventricular ﬁbrillation beat (Vﬁb)). In this setup, zero
perturbation was applied to drop the sample amplitudes and resulted in masks that
highlight class relevant patterns (the authors name e.g. a wider QRS complex for the
LBBB beat and a lack of Q through for Vﬁb). Source: [52].
The objective function searches for a sparse and smooth mask (with mi ∈[0, 1]) and is
deﬁned as [16]:
arg minmλ1||1 −m||1 + λ2
X
||∇m||β
β + sc(φ(x; M)).
(3.5)
In this formula, the ﬁrst term minimizes the region masked, the second term the
total variation and the third term the softmax score of the predicted class c given the
perturbed input. The parameters λ1 and λ2 are weights that deﬁne the inﬂuence of the
L1 norm and total variation terms. To avoid over-ﬁtting and the attraction to artifacts,
a mask of low resolution is learned that is afterward upsampled to match the input
image size (where the upsampled mask is denoted by M). The perturbation of the
image x with a constant value k is computed as:
φ(x; M) = M ⊙x + k(1 −m).
(3.6)
While a mask value of 1 is not applying any perturbing, values close to zero replace the
original input by the occlusion value completely (details about alternative perturbation
types can be found in [16]). Given that low mask values correspond to high importances
of a particular input region, attention heat maps can ﬁnally be computed as the
normalized inverse of the occlusion masks.
Westhuizen et al. [52] recently studied the computation of occlusion masks for the
heartbeat classiﬁcation of MIT-BIH data and showed that perturbations with constant
zero could yield meaningful attention maps (see Fig. 3.4). For the application of ECG
rhythm classiﬁcation, however, dropping sample amplitudes appear less useful. In order
to obtain alternative, more realistic distortions we therefore propose the optimization
of a shift deformation grid. Deriving attention maps from shift computations mainly
focuses on the identiﬁcation of abnormal, temporal features with, for instance, irregular
RR interval. As discussed earlier, those rhythm irregularities can be primarily found
in records belonging to the CinC classes AF or Other (when showing e.g. premature
beats). Since the network is expected to potentially switch to class prediction Normal
in case RR intervals are becoming increasingly regular (by shifting samples of sections
where irregular intervals are observed), regions of large shifts are likely localizing those
beats of strongest rhythm irregularity. For the experiments of this work, the objective
function of Fong et al. will be only slightly adopted by deﬁning m as a perturbation
grid instead of an occlusion mask. Again, both the L1 norm and the total variation


## Page 24


Chapter 3 Methods
20
will be applied to regulate the extent of the deformations and the smoothness of the
grid. As for the occlusion mask formulation, a downsampled version of the deformation
grid will be considered for the optimization (since it is assumed that the optimization
of fewer parameters can potentially lead to more robust results).


## Page 25


Chapter 4
Material and Experiments
4.1 Datasets
Two diﬀerent databases were considered for the evaluation of the proposed network archi-
tectures and visualization approaches. Classiﬁcation performances were ﬁrst assessed by
performing an 8-fold cross validation for the weakly annotated data of the Computing in
Cardiology (CinC) challenge 2017 [11]. Moreover, the MIT-BIH Arrhythmia Database
[32] was used to facilitate a visual evaluation of the attention approaches’ localization
abilities since it not only provides rhythm but also beat wise annotations and therefore
more easily allowed to reason about attention outputs.
4.1.1 The PhysioNet CinC Challenge 2017
The dataset of the PhysioNet Computing in Cardiology challenge 2017 [11] consists of
12186 short ECG sequences that were recorded by AliveCor single-channel ECG devices.
So far, a training set of 8528 records have been made available while the test set of
3658 records still remains private. In order to obtain scores for the hidden test set,
classiﬁcation models need to be submitted to the Physionet challenge community. The
records of the CinC dataset have an average length of about 30 seconds (ranging from
9 - 61 seconds) and are sampled at 300 Hz. Experts manually classiﬁed each complete
sequence into Normal rhythm (N), AF rhythm (AF), Other rhythm (O) and Noisy
entries (∼) and did reﬁne their annotation several times during the oﬃcial phase of
the challenge. Since only global annotations are available for the network training, this
work studies a weakly supervised learning task.
4.1.2 The MIT-BIH Arrhythmia Database
The MIT-BIH arrhythmia database [32] was provided by the Boston’s Beth Israel
Hospital and contains 48 two-channel records of 30 minutes duration. The records were
obtained from 47 patients and are sampled at 360 Hz. The annotation was performed
by at least two experts, which were assigning one from 15 diﬀerent heartbeat types
for each beat and furthermore provided annotations of signal quality changes, rhythm
changes and the corresponding rhythm class.


## Page 26


Chapter 4 Material and Experiments
22
4.2 Evaluation
Since we had no access to the hidden test set, an 8-fold cross validation was performed
on the training set to evaluate and compare the performances of studied models. Each
validation fold consisted of 1066 records, resulting in a remaining training set of 7462
records for each of the eight evaluation runs. The class distribution of each fold was
approximately 60% Normal, 8% AF, 29% Other, and 3% Noisy records. The performance
was evaluated utilizing the overall F1 score, where the class F1 scores were computed
for the classes c ∈{AF, N, O, ∼} using the following formula:
F1c = 2 × TPc
Pc + pc
.
(4.1)
Here, TPc denotes the count of true positives, Pc the count of positives, and pc the
count of predicted positive records for the given class c. In accordance to the challenge
guidelines, class F1 scores were then averaged over all classes except for class Noisy
(which was severely underrepresented in the overall database):
F1 = F1AF + F1N + F1O
3
.
(4.2)
Finally, the global F1 score was deﬁned as the average F1 score over all folds.
4.3 Network Architectures and Parameterisations
This section gives an overview of studied CNN and ConvLSTM architectures. Notations
in bold letters will thereby introduce the abbreviation of architectures that will be
referred to in the next section. To handle varying record lengths in the CinC database
and to facilitate the implementation of batch-processing, all input records were zero-
padded to a length of 61 seconds.
During training, the networks minimized the
cross-entropy loss using stochastic gradient descent with Adam optimizer and batch
sizes of 16. If not stated diﬀerently, the training was performed over 50 epochs using
an initial learning rate of 0.001 that was decreased with a factor of 0.95 in each
epoch.
4.3.1 Basic Convolutional Neural Network Modules
To ensure a fair performance comparison between global pooling and LSTM feature aggre-
gation strategies, the following basic CNN networks were considered:


## Page 27


Chapter 4 Material and Experiments
23
BN
Conv16
BN
ReLU
Conv32
BN
ReLU
Dropout
AvgPool
AvgPool
Conv32
BN
ReLU
Dropout
AvgPool
Conv64
BN
ReLU
Dropout
AvgPool
Conv64
BN
ReLU
Dropout
Conv128
BN
ReLU
Dropout
Conv128
BN
ReLU
Dropout
AvgPool
Figure 4.1: Basic CNN network consisting of seven convolutional layers using batch normalization
(BN) and intermediate average pooling layers (AvgPool).
4 layer CNN module
Throughout the experiments of this work, the application
of shallow CNN architectures led to inferior results than the application of deeper
networks. Nevertheless, a four layer CNN network (with 16, 32, 64, and 128 channels,
each applying a kernel of size 21) was examined in order to investigate the inﬂuence of
too weakly abstracted features on the performance of LSTM aggregation modules. Given
a comparably large output size of 4535 × 128, the inference of global rhythm predictions
appeared especially diﬃcult for global pooling setups. The module in total contained
227366 trainable parameters. As in all other basic modules, each convolutional layer
was followed by a batch normalization and a ReLU activation.
7 layer CNN module
The second studied CNN architecture is illustrated in Fig. 4.1.
It consisted of seven convolutional layers (with 16, 32, 32, 64, 64, 128, and 128 channels
again using kernel sizes of 21) and overall 679622 trainable parameters. In order to
speed up computations and to improve the generalization abilities of the network,
average pooling (kernel size 2 and stride 2) was applied between all layers (except for
the ﬁrst and the last one). The dropout factor was increased layer after layer, giving
the following dropout series (0, 0.2, 0.3, 0.4, 0.5, 0.5, 0). Considering padded records
of size 18300 as input (corresponding to 61 seconds sampled at 300 Hz) the last layer
feature map was of size 531 × 128 and thus assigned a 128 dimensional feature vector
to each temporal output sample.
15 layer CNN module
The third basic CNN network was, with 15 convolutional
layers in total, eight layers deeper than the previous module. Using kernel sizes of 21 and
channel sizes of 16, 32, 32, 32, 32, 64, 64, 64, 64, 128, 128, 128, 128, 256, and 256, the
module consisted of 3650566 trainable parameters. Applying average pooling after every
second convolutional layer led to a network output size of 206×256.
15 layer CNN module with residual connections
Inspired by a recent work of
Rajpurkar et al. [38], another 15 layer CNN was studied using residual connections be-
tween blocks of CNN layers. In this module, the input of each CNN block was added to its
output to facilitate a better gradient ﬂow through the network. Since the convolutional
layers were used without applying any padding, the feature maps that bypassed these
convolutions had to be cropped to match the given output size.


## Page 28


Chapter 4 Material and Experiments
24
17 layer CNN module
Given that the attention gated CNN approach required
an even deeper architecture to successfully extract high level features at intermediate
layers, a further 17 layer CNN was proposed using channel sizes of 16, 32, 32, 64, 64,
64, 64, 128, 128, 128, 128, 256, 256, 256, 256, 512, and 512. Again, batch normalization,
ReLU activations and increasing dropout series were applied and average pooling was
inserted after every second CNN layer. The last layer output ﬁnally consisted of 63
samples for the padded sequences and only 9 samples for the shortest 9 second records
(when padded zero samples were removed after the convolution).
4.3.2 Global Pooling Setup
As introduced in Sec. 2.2.1, global pooling layers can be stacked after the last CNN layer
in order to temporally aggregate feature vectors for a subsequent classiﬁcation layer (see
Fig. 2.3). In this work, two diﬀerent pooling variants were compared, namely global aver-
age pooling (CNN+GAP) and global max pooling (CNN+GMP).
Class activation maps
The class activation maps that will be depicted in the next
chapter, were computed as the weighted linear sum of the last CNN layer’s upsampled
feature maps and the weights that connect the maps to the neuron with the highest
output activation (see Eq. 3.1). Still, especially for cases of high prediction uncertainty,
it can be helpful to also visualize CAMs for the remaining output neurons (resulting in
attention maps showing evidences for the other classes).
The resolution of the class activation maps is mainly determined by the depth of the
CNN network. That means feature maps of deep architectures are becoming increasingly
coarse. Nevertheless to enable a visualization of ‘high resolution’ attention maps, it was
also experimented with incorporating additional global pooling layers for earlier feature
maps (which show activations for lower-level features but are of higher resolution than
the last layer feature map). For this purpose, the classiﬁcation was trained on both the
GMP vector of the last and the one of an additional intermediate layer of our choice
(15 layer CNN+GMP, mean vote).
4.3.3 Gated Attention Setup
As mentioned before, attention gated CNNs aim at extracting high level features at one
or more intermediate feature scales. For this reason, a 17 layer deep CNN was studied
that applied an attention gating at the 13th convolutional layer. The 13th layer was
chosen speciﬁcally, since it provided outputs of size 492 × 256, which were of similar
resolution than the output features of the 7 layer CNN module. As introduced by
Schlemper et al. [41], attention weights were computed as similarity scores between the
feature vectors of the intermediate and the last CNN layer (see Sec. 3.2.2). Obtaining
one score for each location, the feature maps were ﬁrst multiplied (gated) in a channel-
wise fashion with the attention weights matrix and ﬁnally temporally pooled to a vector
of size 1 × 256. In order to aggregate the resulting vector with the one of the global


## Page 29


Chapter 4 Material and Experiments
25
pooling path (whose output was of size 1 × 512), two independent classiﬁcation layers
were trained. Subsequently, a mean vote strategy was applied to combine the scores of
both paths.
4.3.4 Convolutional Long Short-Term Memory Network Setup
We experimented with three diﬀerent ways of presenting the input data to the networks.
First, extracting non-overlapping subwindows of 0.25 or 1 seconds. Second, using
(overlapping) heart beat windows centered at detected R-peaks. And third, to present
the ECG record at full length which was found to result in best performances (see
Fig. 3.1 for an illustration of the overall setup).
Stacking CNN and LSTM modules
As discussed in Sec. 3.1, each temporal
CNN output sample t is associated with one feature vector xt (whose dimensionality
corresponds to the number of feature channels). An LSTM module that is stacked on
a CNN module subsequently processes the feature sequence in order to ﬁnd a hidden
state representation that can be used for the classiﬁcation.
The ‘onedirectional’ LSTMs of our experiments, performed many-to-one predictions
by only passing the last time step hidden state to the classiﬁcation layer. In further
experiments, standard LSTMs were compared with bidirectional LSTMs and GRUs.
Contrary to onedirectional LSTMs, bidirectional LSTMs concatenated the ‘last’
hidden states of both directions (the backward module processed the input in reversed
order) before passing the combined vector to the classiﬁcation layer (see Fig. 2.6).
An attempt to alternatively extract the hidden states of both directions at the cen-
tral time step (to potentially solve memory problems for long sequences) is denoted
as CNN+bidirectional LSTM, center.
In a last setup (CNN+bidirectional
LSTM+pooling), an additional connection between the CNN module and the classi-
ﬁcation layer was inserted by concatenating the last hidden state with a global pooling
vector of the last CNN layer. Throughout the experiments it was found that a pretrain-
ing of CNN parameters using GMP and a classiﬁcation layer potentially had a positive
eﬀect on the ConvLSTM performances (denoted as pretrained in the setup names).
In those experiments, pretraining was performed over 50 epochs and the initial learning
rate of the CNN parameters was reduced to 1e−4 during the combined training with the
LSTM parameters (which used an initial learning rate of 1e −3).
Plotting class decisions over time
The many-to-one ConvLSTMs of this work
performed one global class prediction after the whole record had been processed. Still,
it can be helpful to examine the decision making process over time by also passing
intermediate hidden states ht to the classiﬁcation layer. By doing so, each time step
t ∈1, ..., T was assigned with softmax scores that could be plotted as the intermediate
(attention-like) class conﬁdences for a given input window (since the CNN output was
of lower resolution that the original input). The ‘class decision over time’ plots ﬁnally


## Page 30


Chapter 4 Material and Experiments
26
show the intermediate class decision corresponding to the maximum softmax score for
each time step.
Computation of shift perturbation masks
By minimizing the objective function
of Eq. 3.5, we aimed at ﬁnding input perturbations that were switching the network
decision from class AF or Other to Normal. Beats of most salient rhythm irregularities
could then be identiﬁed as samples showing the highest shift values in the perturbation
mask.
In order to ease the optimization problem, a downsampled version of the
deformation grid was optimized that was computing shifts for only 1% of the actual input
samples (corresponding to a downsampling factor of 100). The downsampled grid was
initialized with random shift values sampled from a normal distribution with zero mean
and a standard deviation of 0.001. Generally, the grid held values in the range [−1, 1]
with sample locations being normalized by the lengths of the input (-1 corresponding
to the very left input sample and 1 the very right one). Linear interpolation was used
to sample the input pixels and to derive a gradient for optimization. Optimization
again was performed with stochastic gradient descent and Adam optimizer and aimed
at the computation of an optimal perturbation mask that ﬂipped the class decision of
the network. This time, a smaller learning rate of 0.0001 and an optimizing over 500
epochs were considered. The hyperparameters λ1 (L1 coeﬃcient) and λ1 (TV coeﬃcient)
inﬂuenced the extent of the shifts and the smoothness of the ﬁnal perturbation grid result.
Without any regularization the perturbations did not produce helpful visualizations
and ﬂipped the label to the class Noisy in most cases.
Visualization of hidden states and gates
Karpathy [25] and Chen [7] recently
managed to gain some insights into the LSTM cell behavior by analyzing its states and
input, forget, and output gates. However, Karpathy [25] found that for the prediction
of next characters in creating programming code only 5% of the neurons performed
meaningful operations (like tracking the position in line, turning on in quotes, activating
inside if statements, etc.) and that many neuron states remained hard to interpret. For
this reason, the internal gate and state values for a very simple 2 hidden unit LSTM will
be analyzed. Values for each time step gate and state values were thereby computed
according to the equations (2.10) to (2.14).
4.4 Implementation and Computation Times
All models were implemented in Python using the Pytorch library [37] and each
experiment was run on a single GPU (NVIDIA GeForce GTX 1080 Ti, 11GB RAM).
Computation times depend on the network setups and particularly the length of the
feature sequence that was processed by the LSTM module (and that the error needed
to be backpropagated through). While most of the models (both CNNs with global
pooling and ConvLSTMs) took between 1 to 3 hours to train, much longer training
times of about 4 to 5 hours were observed for the ConvLSTM that extracted features
using a shallow 4 layer CNN setup and therefore processed longer feature sequences.


## Page 31


Chapter 4 Material and Experiments
27
Certainly, training times were also inﬂuenced by the model complexities. The number
of trainable parameters were 679622 for the 7 layer CNN, 3650566 for the deeper 15
layer CNN, 3732230 for the ConvLSTM with 15 CNN layers and 64 hidden units, and
ﬁnally 3765510 for the ConvLSTM consisting of 15 CNN layers and 2 LSTM layers
with 64 hidden units.


## Page 32


Chapter 5
Results
This section reports the cross validation performances of the previously introduced
network architectures and illustrates various attention maps for a selection of models.
The presented tables give an overview of class speciﬁc and total F1 scores that have
been averaged over all folds of the cross validation. As introduced in the last chapter,
the overall F1 score does not include the class Noisy.
5.1 Global Pooling Performances
In ﬁrst experiments, global rhythm classiﬁcations were performed by global pooling
CNNs. Table 5.1 gives an overview of F1 scores that were obtained for CNN modules
of varying depths. Despite a prior assumption that GMP would outperform GAP due
to a superior capturing of episodic abnormalities, both pooling variants obtained an
equal average F1 score of 0.82 when studying a 7 layer CNN module. Performances
were further improved to a score of 0.84 when using a deeper network setup with 15
layers and 256 output channels (15 layer CNN+GMP). The insertion of residual
connections (15 layer, residual CNN+GMP), however, even slightly dropped the
F1 score to 0.83. Furthermore, it can be observed that the performances with F1 = 0.68
were signiﬁcantly inferior for the 4 layer CNN setup (4 layer CNN+GMP) where
the temporal aggregation of features had to be performed over long sequences of 4535
output samples.
Table 5.1: 8-fold cross validation of global pooling setups
Architecture
F1AF
F1N
F1O
F1∼
F1total
4 layer CNN+GMP
0.61 (± 0.06)
0.86 (± 0.03)
0.59 (± 0.03)
0.50 (± 0.09)
0.68 (± 0.04)
7 layer CNN+GAP
0.79 (± 0.05)
0.91 (± 0.01)
0.75 (± 0.03)
0.60 (± 0.07)
0.82 (± 0.02)
7 layer CNN+GMP
0.78 (± 0.03)
0.92 (± 0.01)
0.76 (± 0.02)
0.56 (± 0.08)
0.82 (± 0.01)
15 layer CNN+GMP
0.82 (± 0.02)
0.92 (± 0.01)
0.79 (± 0.02)
0.63 (± 0.07)
0.84 (± 0.01)
15 layer, residual CNN+GMP
0.80 (± 0.03)
0.91 (± 0.01)
0.77 (± 0.02)
0.63 (± 0.05)
0.83 (± 0.02)
15 layer CNN+GMP, mean vote
0.81 (± 0.02)
0.91 (± 0.01)
0.78 (± 0.02)
0.54 (± 0.11)
0.83 (± 0.02)
17 layer CNN+GMP
0.81 (± 0.04)
0.92 (± 0.01)
0.78 (± 0.02)
0.65 (± 0.04)
0.83 (± 0.02)


## Page 33


Chapter 5 Results
29
5900
6100
6300
6500
6700
6900
7100
7300
0
1
0.0
1.0
Figure 5.1: CNN+GAP CAM for the correctly classiﬁed Other rhythm record A06020. Full record
visualization (top) and 5 second excerpt (bottom) of an attention map that successfully
highlights an abnormal beat. As indicated by the color bar, activations are color coded
from high to low as red to blue.
7400
7600
7800
8000
8200
8400
8600
8800
0
1
Figure 5.2: CNN+GMP CAM for the correctly classiﬁed Other rhythm record A05831. The attention
map particularly focuses on one premature beat while assigning the lowest activations to
a noisy section at the center of the record (visible in the full record visualization at the
top).
5.1.1 Class Activation Map Visualizations
The inﬂuence of the pooling variant choice can be further examined by studying the
class activation maps that were computed for a network with 7 convolutional layers (see
Fig. 5.3 to Fig. 5.6). Each depicted attention map represents the CAM for the output
neuron with the highest softmax score and therefore highlights input patterns that were
considered to be meaningful evidences for the predicted class.
The ﬁrst record example of Fig. 5.1 shows a class activation map that resulted from an
GAP architecture. The visualization suggests that the network was conﬁdent about the
class prediction Other and that one particular abnormal beat was highlighted in the
rhythm. Despite the episodic character of the pathological event, the corresponding
section of high CAM activations (indicated by the red color coding) dominated all
remaining temporal samples in the averaging process and provoked the correct class
prediction Other on the global level.
While Other rhythm examples often exhibited strong activations for single prominent
record sections, interpretations were generally less intuitive for examples of classes AF
and Normal. In those cases, where class speciﬁc patterns occurred repeatedly, CAMs
either assigned high activations for many subsequent beats (like in Fig. 5.4) or only
focused on single pattern occurrences. The ﬁgure 5.3, for instance, shows a CAM, where
an irregular RR interval feature was highlighted at the central part but not at the
beginning of the record. This observation indicates that ﬁnal rhythm predictions can
base solely on the detection of single key features of strong evidence and are rarely taking
all episodes of pathologies into account. An additional, more encouraging observation


## Page 34


Chapter 5 Results
30
was the assignment of very low activation for class irrelevant patterns (colored in dark
blue), as it can be seen in the noisy section of Fig. 5.3.
2900
3100
3300
3500
3700
3900
4100
4300
0.0
0.5
++
Figure 5.3: CNN+GAP CAM for the correctly classiﬁed AF rhythm record A00225. The attention
map highlights some (but not all) beats with irregular RR interval.
0
200
400
600
800
1000
1200
1400
0.2
0.0
0.2
Figure 5.4: CNN+GAP CAM for the correctly classiﬁed Normal rhythm record A00464. Apparently,
the network focused on several beats of similar appearance equally.
7400
7600
7800
8000
8200
8400
8600
8800
0
1
Figure 5.5: CNN+GMP CAM for the AF rhythm record A01718 that was incorrectly predicted as
Other rhythm.
0
200
400
600
800
1000
1200
1400
0.0
0.2
0.4
Figure 5.6: CNN+GMP CAM for the misclassiﬁed Noisy rhythm record A08043. Even though large
parts of the record were of noisy appearance, the clear detection of AF speciﬁc rhythm
irregularities caused an AF class prediction. This case illustrates a weakness of the global
max pooling operation, which is not able to capture information about the duration of
feature occurrences.


## Page 35


Chapter 5 Results
31
0
2000
4000
6000
8000
1
0
0
2000
4000
6000
8000
1
0
Figure 5.8: 15 layer CNN+GMP CAMs (obtained by a mean vote strategy) for the correctly classiﬁed
Other record A03516. Again, the visualizations show the CAMs that were computed for
the intermediate (top) and the last layer (bottom).
0
1000
2000
3000
4000
5000
6000
7000
0.5
0.0
0.5
0
1000
2000
3000
4000
5000
6000
7000
0.5
0.0
0.5
Figure 5.7: 15 layer CNN+GMP CAMs (obtained by a concatenation strategy) for the correctly
classiﬁed AF record A01718. The visualizations show the CAMs that were computed for
the intermediate (top) and the last layer (bottom).
In cases of misclassiﬁcations, class activation maps can also help to closer examine
record patterns that caused wrong predictions. Figure 5.6, for instance, shows a class
activation map of a misclassiﬁed record of ground truth class Noisy that clearly suggests
that the classiﬁcation as AF was triggered by the detection of missing P waves and
irregular rhythms. Deciding at which extent and amount of noise a record was to be
classiﬁed as Noisy appeared to be a non trivial and potentially ambiguous task and
was discussed exhaustingly during the challenge (leading to several reﬁnements of the
expert annotations).
As discussed in the experimental setup description, another attempt to improve the
classiﬁcation performance was to explicitly consider global as well as more local in-
formation when performing the classiﬁcation (15 layer CNN+GMP, mean vote).
Nevertheless, neither a concatenation of both vectors nor the ﬁtting of two indepen-
dent classiﬁcation layers (whose outputs were combined by averaging) showed any
performance improvements and even dropped the F1 score to 0.83. One remaining
beneﬁt of such intermediate CAM computations was the ability to visualize informative
attention maps for deep networks. Two examples of intermediate layer CAMs are
depicted in Fig. 5.7 and Fig. 5.8 (showing correctly classiﬁed records of classes AF and
Other, respectively). While the CAM of the intermediate layer apparently highlights
single, suspicious beats, the coarse CAM (computed for the last layer) hardly gives any
interpretable insights regarding the class decision of the network.


## Page 36


Chapter 5 Results
32
Table 5.2: 8-fold cross validation of gated attention CNN setups
Architecture
F1AF
F1N
F1O
F1∼
F1total
17 layer CNN+GMP
0.81 (± 0.04)
0.92 (± 0.01)
0.78 (± 0.02)
0.65 (± 0.04)
0.83 (± 0.02)
17 layer CNN+AttentionGates, concat
0.81 (± 0.05)
0.92 (± 0.01)
0.78 (± 0.02)
0.66 (± 0.05)
0.83 (± 0.02)
17 layer CNN+AttentionGates, mean vote
0.81 (± 0.04)
0.92 (± 0.01)
0.78 (± 0.02)
0.63 (± 0.09)
0.84 (± 0.02)
5.2 Gated Attention Network Performances
The results in Table 5.2 indicate that the extension of a global pooling CNN with an
additional attention path could slightly improve the performance from 0.83 to 0.84
when using two independent classiﬁcation layers for both paths. First attempts to
train a single classiﬁcation layer for a concatenated output of both paths resulted in
‘empty’ attention maps for the intermediate layer and consequently a skipping of the
attention gating path. Figure 5.9 shows some examples of resulting intermediate gated
attention maps and last layer CAMs that were computed using GMP and mean voting
over two classiﬁers. While the attention map of the 13th layer highlights single beats,
the CAM of the last layer was of much coarser appearance. As for the concatenation
strategy setup, class Other record attention maps strikingly often did not show any high
activations (indicating that local features were not considered for the classiﬁcation). In
fact, outputs of attention gated CNNs generally appeared less interpretable than the
standard CAMs presented in the previous section.
5.3 Convolutional Long Short-Term Memory
Network Performances
This section studies the inﬂuence of CNN and LSTM parameter choices when combining
both modules to ConvLSTMs. An overview of all considered parameterizations (where
4 layer CNN, 7 layer CNN, 15 layer CNN, and 15 layer, residual CNN again
denote the basic CNN networks) is given in Table 5.3.
5.3.1 Sensitivity to Hyperparameters
Recapitulating all experiments, the network depth of the CNN module appeared to have
a larger eﬀect on the performance than the number of layers or hidden units concerning
the LSTM module. While the shallowest setup with four convolutional layers and 64
hidden units reached an F1 score of 0.75, the ConvLSTM consisting of 7 CNN layers
and only 4 LSTM units already yielded a score of 0.82. Increasing the dimension of
the hidden state to 16 slightly improved the performance to 0.83 and using multiple
layers in combination with a pretraining of CNN parameters ﬁnally yielded a score
of 0.84. Apparently, neither the bidirectional LSTM variant nor the application of a
simpliﬁed GRU module brought any beneﬁts compared to the 1 layer LSTM setup. The
attempt to pass pooled CNN features as well as LSTM outputs to the classiﬁcation


## Page 37


Chapter 5 Results
33
0
500
1000
1500
2000
2500
3000
1
0
1
0
500
1000
1500
2000
2500
3000
1
0
1
(a)
0
2000
4000
6000
8000
1
0
2
0
2000
4000
6000
8000
1
0
2
(b)
0
2000
4000
6000
8000
0.5
0.0
0.5
0
2000
4000
6000
8000
0.5
0.0
0.5
(c)
Figure 5.9: Gated attention maps (top) and CAMs (bottom) for examples of classes AF (a), Normal
(b), and Other (c) that were all correctly classiﬁed by the attention network. While the
gated attention maps were extracted at the 13th layer, the CAMs were computed for
the output neuron that corresponded to the highest softmax score. The network was
trained with a mean vote aggregation strategy to combine the scores of two independently
trained classiﬁcation layers. While the attention gated feature maps for both AF and
Normal example focus on one to two particular beats, the feature map for the class Other
example does not show any high activations throughout the entire record.


## Page 38


Chapter 5 Results
34
Table 5.3: 8-fold cross validation of ConvLSTM setups
Architecture
F1AF
F1N
F1O
F1∼
F1total
4 layer CNN+1 layer LSTM, 16 hidden
0.63 (± 0.04)
0.86 (± 0.01)
0.59 (± 0.04)
0.44 (± 0.12)
0.69 (± 0.03)
4 layer CNN+1 layer LSTM, 64 hidden
0.69 (± 0.04)
0.88 (± 0.01)
0.68 (± 0.03)
0.56 (± 0.10)
0.75 (± 0.02)
7 layer CNN+1 layer LSTM, 4 hidden
0.77 (± 0.04)
0.91 (± 0.01)
0.77 (± 0.02)
0.56 (± 0.12)
0.82 (± 0.02)
7 layer CNN+1 layer LSTM, 16 hidden
0.80 (± 0.03)
0.92 (± 0.01)
0.78 (± 0.02)
0.65 (± 0.06)
0.83 (± 0.02)
7 layer CNN+1 layer LSTM, 64 hidden
0.80 (± 0.03)
0.92 (± 0.01)
0.78 (± 0.02)
0.64 (± 0.08)
0.83 (± 0.02)
pretrained 7 layer CNN+2 layer LSTM, 16 hidden
0.81 (± 0.02)
0.92 (± 0.01)
0.78 (± 0.02)
0.65 (± 0.06)
0.84 (± 0.02)
pretrained 7 layer CNN+3 layer LSTM, 32 hidden
0.82 (± 0.02)
0.92 (± 0.01)
0.78 (± 0.02)
0.65 (± 0.10)
0.84 (± 0.01)
7 layer CNN+bidirectional LSTM, 16 hidden
0.81 (± 0.02)
0.92 (± 0.01)
0.78 (± 0.03)
0.65 (± 0.08)
0.83 (± 0.02)
7 layer CNN+bidirectional LSTM, 16 hidden, center
0.80 (± 0.04)
0.92 (± 0.01)
0.78 (± 0.02)
0.65 (± 0.07)
0.83 (± 0.02)
7 layer CNN+bidirectional GRU, 16 hidden
0.81 (± 0.02)
0.91 (± 0.01)
0.77 (± 0.02)
0.64 (± 0.06)
0.83 (± 0.01)
7 layer CNN+bidirectional LSTM, 64 hidden+pooling
0.80 (± 0.02)
0.91 (± 0.01)
0.76 (± 0.02)
0.59 (± 0.07)
0.82 (± 0.01)
pretrained 15 layer CNN+1 layer LSTM, 2 hidden
0.79 (± 0.04)
0.91 (± 0.01)
0.78 (± 0.02)
0.52 (± 0.21)
0.83 (± 0.02)
pretrained 15 layer CNN+1 layer LSTM, 4 hidden
0.82 (± 0.03)
0.92 (± 0.01)
0.78 (± 0.02)
0.62 (± 0.06)
0.84 (± 0.02)
pretrained 15 layer CNN+1 layer LSTM, 64 hidden
0.83 (± 0.03)
0.92 (± 0.01)
0.79 (± 0.02)
0.64 (± 0.06)
0.85 (± 0.02)
pretrained 15 layer CNN+2 layer LSTM, 64 hidden
0.82 (± 0.03)
0.92 (± 0.01)
0.79 (± 0.02)
0.64 (± 0.09)
0.84 (± 0.02)
pretrained 15 layer residual CNN+2 layer LSTM, 64 hidden
0.80 (± 0.02)
0.91 (± 0.01)
0.78 (± 0.02)
0.60 (± 0.06)
0.83 (± 0.01)
layer (see setup 7 layer CNN+bidirectional LSTM+pooling) even resulted in a
slight performance drop which implies that the additional path of information had a
negative impact on the training.
The best ConvLSTM performance of 0.85 was ﬁnally obtained with the setup pre-
trained 15 layer CNN+1 layer LSTM, 64 hidden. However, the application of a
t-test conﬁrmed that performances were not signiﬁcantly better than other setups that
reached a score of 0.84 for the same basic CNN module. In conclusion, the positive
eﬀect of LSTMs on the classiﬁcation accuracy is more pronounced for networks with
fewer layers and the inﬂuence of the LSTM parameter choices decreased with growing
depth.
5.3.2 Plotting Class Decisions Over Time
The following visualizations depict four ‘class decision over time’ plots that were obtained
for a ConvLSTM with 7 CNN layers and 16 hidden units. Since the output of the
CNN was approximately 34 times smaller than the original input record, each time step
represented a window of about 34 samples in the plot. The ﬁrst example of Fig. 5.10a
shows a record excerpt that was correctly classiﬁed as Normal throughout the whole
sequence. It can be observed that the prediction conﬁdence slightly decreased with
the beginning of a noisy event but that no class prediction switch was caused. The
AF record of Fig. 5.10b, on the contrary, was initially classiﬁed as class Other until a
beat with missing P wave was encountered and the prediction switched to class AF.
Generally, the plot of class Other rhythm examples allowed for the easiest interpretation.
The 5 second excerpt of Fig. 5.11a, for instance, clearly visualizes a strong enhancing of
the class Other softmax score after the detection of an abnormal beat in the sequence.
The last example of Fig. 5.11b ﬁnally illustrates a failure case where a record with
the class Other was confused as AF rhythm. Concerning this record, the network
apparently permanently switched between the two class decisions Other and AF which
likely originated from the fact that irregular RR intervals are a common feature for
both classes.


## Page 39


Chapter 5 Results
35
0
2
Softmax scores 
0
2
0
2
0
2
1400
1800
2200
2600
0
2
Class predictions
0
1
AF
N
O
~
(a)
0 . 0
0 . 5
Softmax scores
0 . 0
0 . 5
0 . 0
0 . 5
0 . 0
0 . 5
0
400
800
1200
0 .0
0 .5
Class predictions
0
1
AF
N
O
~
(b)
Figure 5.10: 5 second excerpt plot of intermediate class decisions for an example of class Normal (a)
and class AF (b). While the plots 1-4 (from top to bottom) show the softmax scores
changing over time for classes AF, N, O, and Noisy, plot 5 depicts the resulting class
decisions (with classes being color coded according to the legend at the right).
Softmax scores
5900
6300
6700
7100
Class predictions
0
1
AF
N
O
~
0
1
0
1
0
1
0
1
0
1
(a)
Softmax scores
7400
7800
8200
8600
Class predictions
0
1
AF
N
O
~
0 . 0
0 . 5
0 . 0
0 . 5
0 . 0
0 . 5
0 . 0
0 . 5
0 . 0
0 . 5
(b)
Figure 5.11: 5 second excerpt plot of intermediate class decisions for two examples of class Other
being (a) correctly classiﬁed and (b) mistaken as class AF.
Softmax scores
0
400
800
1200
Class predictions
0
1
0
1
0
1
0
1
0
1
0
1
AF
N
O
~
(a)
Softmax scores
1670
17100
17500
17900
Class predictions
0
1
0
1
0
1
0
1
0
1
0
1
AF
N
O
~
(b)
Figure 5.12: Class decision plot for a shallower CNN module with only 4 layers showing the ﬁrst 5
seconds (a) and the last 5 seconds (b) of an Other rhythm record that was incorrectly
classiﬁed as Normal. It is likely that the misclassiﬁcation was caused by limited memory
capacities of the LSTM. Apparently, the class decision switched back to class normal
at the end of the record, indicating that the cell ‘forgot’ the detection of class Other
patterns earlier in the sequence.


## Page 40


Chapter 5 Results
36
0
500
1000
1500
2000
2500
3000
3500
0
1
N
N
N
N
N
N
N
N
N
N
N
N
N
N
N
0
500
1000
1500
2000
2500
3000
0
1
0
500
1000
1500
2000
2500
3000
0.000
0.005
Figure 5.13: MIT-BIH ﬁle 210 with meaningful perturbation for an AF example. Subﬁgures show
the beat target annotation (top), the original signal in blue and the shifted signal in
magenta (middle row), and ﬁnally the corresponding shift values of the upsampled
pertubation grid (bottom). The perturbation yielded softmax scores of 0.00, 0.83, 0.17,
and 0.00 for the classes AF, N, O, and Noisy using L1 and TV coeﬃcients of 0.2 and
0.1.
When studying an even shallower ConvLSTM consisting of only 4 CNN and 2 LSTM
layers with 128 hidden units, each time step represented a much smaller window
of only 4 samples. Given that the LSTM processed a sequence of up to 4535 time
steps, it is possible that the network had diﬃculties to remember salient patterns
over long periods of time (e.g. if abnormal beats were encountered at the ﬁrst part
of the record). The example of Fig. 5.12 depicts a class Other record where such a
long-range memory issue likely have caused a misclassiﬁcation as class Normal. Even
though the class decision was performed correctly after the occurrence of abnormal
morphologies, the decision switched back to class Normal at some point at the end of
the sequence.
5.3.3 Shift Perturbation Mask Visualizations
As visible in Fig. 5.13 and Fig. 5.14, the application of perturbation masks succeeded
to identify irregular located beats for both AF and Other rhythms. The concept of
‘attention’ in this context was expressed as the amount of shift that minimized the
objective function of Eq. 3.5. In other words, irregular beats of the input were supposed
to be shifted in such an extent, that the network prediction switched from AF (or
Other) to Normal (resulting from a maximal drop of the softmax score of e.g. AF when
shifting the input samples with the given perturbation mask). The records of Fig. 5.13
and Fig. 5.14 were ﬁnally successfully predicted as rhythm class Normal after the most
prominent rhythm irregularities were removed by the perturbation mask. Especially
the mask of the second example, however, also exhibits some higher shift values for
beats of regular rhythm. Less interpretable is the perturbation of Fig. 5.15 which was
conﬁdently predicted as class Normal even though the resulting perturbed signal has
an unrealistic appearance.


## Page 41


Chapter 5 Results
37
0
500
1000
1500
2000
2500
3000
3500
1
0
1
N
N
N
N
N
A
N
N
N
N
N
N
N
N
N
N
0
500
1000
1500
2000
2500
3000
0
1
-1
0
500
1000
1500
2000
2500
3000
0.010
0.005
0.000
Figure 5.14: MIT-BIH ﬁle 209 with successful perturbation for a premature beat example of an class
Other record. Resulting softmax scores were 0.01, 0.92, 0.03, and 0.04 for the classes
AF, N, O, and Noisy using L1 and TV coeﬃcients of 0.4 and 0.1.
0
500
1000
1500
2000
2500
3000
3500
0
1
N
N
N
N
V
N
A
N
N
N
N
N
N
N
N
-1
0
500
1000
1500
2000
2500
3000
0
1
-1
0
500
1000
1500
2000
2500
3000
0.005
0.000
Figure 5.15: MIT-BIH ﬁle 205 with uninterpretable perturbation of an class Other record that
surprisingly led to a class Normal prediction with softmax scores of 0.00, 0.98, 0.01, and
0.00 for the classes AF, N, O, and Noisy. The L1 and TV coeﬃcients were set to 0.2
and 0.1.
5.3.4 Hidden State and Gate Visualizations
Since both the inﬂuence of LSTM parameters and the internal computations of LSTM
cells remained hard to interpret, this sections aims at getting a better understanding
of gate and state evolutions for a simple LSTM setup. The studied ConvLSTM (that
yielded an F1 score of 0.83) consisted of 15 convolutional layers and used only two
LSTM units for the temporal aggregation. Given the many-to-one LSTM formulation,
the classiﬁcation layer of this setup received only two input activations which were the
two entries of the last hidden state vector. Requiring the encoding of four classes by
two values, the LSTM module apparently learned the following class speciﬁc hidden
state representations: while the class AF prediction was associated with a very low
activation for both neurons (color coded as dark blue), the class Normal showed high
activations for both units (red), the class Other a high activation for the ﬁrst and a
low one for the second neuron, and lastly the class Noisy prediction was triggered by a
combination of low and very low activations (dark and light blue).


## Page 42


Chapter 5 Results
38
5
0
Hidden states
5
0
(a)
0
1
Hidden states
0
1
(b)
0
1
Hidden states
0
1
(c)
5
0
Hidden states
5
0
5000
10000
15000
0
(d)
1
0
Hidden states
1
0
1
0
Input gates
1
0
1
0
Candidate gates
1
0
1
0
Output gates
1
0
1
0
Forget gates
15700
15900
16100
16300
1
0
Figure 5.16: Left: Visualization of LSTM hidden states with two hidden units for examples of classes
AF (a), Normal (b), Other (c), and Noisy (d). Hidden state activations are color coded
from high to low as dark red to dark blue. Examining the last hidden state for several
examples, class speciﬁc encodings could be observed (showing e.g. two low activations
for class normal records and a combination of high and low activations for class Other
records). Right: Visualization of LSTM hidden states and gates with two hidden units
for a 5 second excerpt of the preceding Other example. In this plot, a drop of candidate
gate values can be observed after encountering a noisy record section.


## Page 43


Chapter 5 Results
39
Table 5.4: 8-fold cross validation performance comparison.
Architecture
F1AF
F1N
F1O
F1∼
F1total
7 layer CNN+GAP
0.79 (± 0.05)
0.91 (± 0.01)
0.75 (± 0.03)
0.60 (± 0.07)
0.82 (± 0.02)
7 layer CNN+GMP
0.78 (± 0.03)
0.92 (± 0.01)
0.76 (± 0.02)
0.56 (± 0.08)
0.82 (± 0.01)
7 layer CNN+1 layer LSTM, 16 hidden
0.80 (± 0.03)
0.92 (± 0.01)
0.78 (± 0.02)
0.65 (± 0.06)
0.83 (± 0.02)
pretrained 7 layer CNN+2 layer LSTM, 16 hidden
0.81 (± 0.02)
0.92 (± 0.01)
0.78 (± 0.02)
0.65 (± 0.06)
0.84 (± 0.02)
15 layer CNN+GMP
0.82 (± 0.02)
0.92 (± 0.01)
0.79 (± 0.02)
0.63 (± 0.07)
0.84 (± 0.01)
pretrained 15 layer CNN+1 layer LSTM, 4 hidden
0.82 (± 0.03)
0.92 (± 0.01)
0.78 (± 0.02)
0.62 (± 0.06)
0.84 (± 0.02)
pretrained 15 layer CNN+1 layer LSTM, 64 hidden
0.83 (± 0.03)
0.92 (± 0.01)
0.79 (± 0.02)
0.64 (± 0.06)
0.85 (± 0.02)
pretrained 15 layer CNN+2 layer LSTM, 64 hidden
0.82 (± 0.03)
0.92 (± 0.01)
0.79 (± 0.02)
0.64 (± 0.09)
0.84 (± 0.02)
17 layer CNN+GMP
0.81 (± 0.04)
0.92 (± 0.01)
0.78 (± 0.02)
0.65 (± 0.04)
0.83 (± 0.02)
17 layer CNN+AttentionGates, mean vote
0.81 (± 0.04)
0.92 (± 0.01)
0.78 (± 0.02)
0.63 (± 0.09)
0.84 (± 0.02)
Fig. 5.16 illustrates this encoding for four example cases. It can be observed that the
‘hidden state evolution over time plots’ (see for instance Fig. 5.16a and Fig. 5.16d) are of
similar appearance as the ‘class decision over time plots’ studied earlier in this section.
When sticking to the two unit class encoding hypothesis, the predictions for the record
of class AF (depicted in Fig. 5.16a) appear to have switched from initially AF, to Noisy,
to Other, and ﬁnally back to the correct class prediction AF.
Figure 5.16 furthermore shows a zoomed 5 second excerpt of the depicted class Other
record, which is displayed together with the corresponding input, candidate, output
and forget gate values. In this example, the values of the forget gate and the output
gate were consistently high, whereas the input and the candidate gates showed some
changes over time. While the drop of the candidate gate values with the beginning
of a noisy record section appears reasonable, the remaining gate behaviors were more
diﬃcult to interpret. When recalling the hidden state and cell state deﬁnitions (which
were ct = ftct−1 + itgt and ht = ot tanh(ct), respectively), the high values for both forget
and output gates apparently kept the cell state entries from being overwritten by new
inputs. In conclusion, even this simple LSTM module remained a black box concerning
the internal gate and state modiﬁcations over time and no clear ‘responsibilities’ of
single neurons could be identiﬁed when analyzing the behavior of the cell for several
examples.
5.4 Performance Comparisons
Table 5.4 summarizes the presented 8-fold cross validation scores for a selection of
experiments. The best average F1 score of 0.85 was obtained by a single layer LSTM
consisting of 64 hidden units that was stacked on top of a pretrained CNN with 15
layers. Especially for deep CNN setups, a pretraining of CNN parameters showed to be
beneﬁcial. While the hidden state capacity appeared to have a large inﬂuence on the
performance for the 4 layer CNN setup (obtaining a score of 0.69 when using 16 hidden
units and 0.75 when increasing the number of hidden units to 64), a smaller inﬂuence
was observed for ConvLSTMs with deeper CNN modules. Moreover, it was found that
simple global pooling CNN architectures performed surprisingly well. For both 7 layer
and 15 layer CNN modules the performances were only slightly worse than those of
ConvLSTM networks using the same amount of CNN layers. Finally, the application of


## Page 44


Chapter 5 Results
40
Table 5.5: Confusion matrices for 7 layer CNN+GMP (left) and pretrained 7 layer CNN+2
layer LSTM, 16 hidden (right).
Ground truth
AF
N
O
∼
Total
Prediction
AF
688
70
236
21
1015
N
13
4707
423
57
5200
O
48
225
1663
21
1957
∼
9
74
93
180
356
Total
758
5076
2415
279
8528
Ground truth
AF
N
O
∼
Total
Prediction
AF
637
28
134
14
813
N
20
4795
487
50
5156
O
83
204
1740
22
2287
∼
18
49
54
193
272
Total
758
5076
2415
279
8528
Table 5.6: Confusion matrices for 15 layer CNN+GMP (left) and pretrained 15 layer CNN+1
layer LSTM, 64 hidden (right).
Ground truth
AF
N
O
∼
Total
Prediction
AF
641
37
124
11
813
N
14
4703
379
60
5352
O
90
301
1864
32
2049
∼
13
35
48
176
314
Total
758
5076
2415
279
8528
Ground truth
AF
N
O
∼
Total
Prediction
AF
633
21
99
13
766
N
18
4706
403
59
5186
O
96
318
1869
35
2318
∼
11
31
44
172
258
Total
758
5076
2415
279
8528
attention gates in a 17 layer deep CNN network did only insigniﬁcantly improve the
baseline CNN performances from 0.83 to 0.84.
The confusion matrices of Table 5.5 and Table 5.6 (which are the summed confusion
matrices over all 8 folds) compare the class prediction distributions of global max pooling
and LSTM setups for a 7 layer and a 15 layer CNN module, respectively. The depicted
distribution suggests that the 7 layer CNN+GAP setup was the most sensitive to
AF cases and at the same time the least sensitive for class Other rhythms. An opposing
behavior was observed for the 15 layer CNN+LSTM setup which detected the fewest
AF and the most Other rhythm records. Moreover, it becomes apparent that for both
global pooling and LSTM variants the number of correctly classiﬁed Other records
increased signiﬁcantly with growing network depth.
An examination of the overall F1 scores for the class AF (which were 0.79 for 7 layer
CNN+GAP, 0.81 for 7 layer CNN+LSTM, 0.82 for 15 layer CNN+GMP, and
0.83 for 15 layer CNN+LSTM), shows that the high sensitivity of the shallow global
pooling setup came along with a comparably high number of false positive predic-
tions. Consequently, LSTMs yielded superior scores concerning the F1 performance
metric. A study of the overall F1 scores for the class Other (which were 0.75 for 7
layer CNN+GAP, 0.78 for 7 layer CNN+LSTM, 0.79 for 15 layer CNN+GAP,
and 0.79 for 15 layer CNN+LSTM) again suggested that the accuracy was more
impacted by the network depth than by the choice of temporal aggregation strat-
egy.


## Page 45


Chapter 6
Discussion
6.1 Are ConvLSTMs the Winners of the CinC
Challenge?
It does not directly follow that the excellent performance of our ConvLSTM network of
F1 = 0.85 on the CinC training set would be the best ranking performance on the oﬃcial
test set (for which a best score of F1 = 0.83 was reported). A drop of performance
was, for instance, noted by Warrick et al. [51] who achieved a score of F1 = 0.83 for a
10-fold cross validation and a score of only 0.80 on the test set. Consequently, a fair
comparison to other state-of-the-art approaches, so far, is only limited possible and a
submission of our best performing model intended.
Assuming a similar performance drop of about 0.03, the proposed ConvNet would,
however, yield a satisfying performance while keeping the classiﬁcation pipeline much
simpler than most of the participating teams (see Sec. 1.2). As intended, the proposed
setup not only avoided additional post-processing steps but also the requirement of
complex feature engineering pipelines. Furthermore, it is to be assumed that both an
ensemble of multiple, independently trained ConvLSTMs and the application of data
augmentation could further improve the performances.
Are pure CNNs better classiﬁers than ConvLSTMs?
The experiments of this
work suggest that the complex temporal aggregation of LSTMs (which adds many
learnable parameters) did not signiﬁcantly outperform global pooling strategies (which,
on the contrary, basically discard information). Even if this observation is surprising,
it is in line with the results reported by Zihlmann et al. [60] who discovered that for
a 24 layer CNN setup, LSTMs outperformed GAP only in case data augmentation
was employed. Still, a more obvious superiority of LSTMs was observed for the 4
and 7 layer CNN modules, where LSTMs apparently provided a ‘smarter’ temporal
aggregation of local beat features than the competing global pooling layers. However,
with a growing receptive ﬁeld (that comes along with deeper networks), CNNs seemed
to successfully take over the task of capturing temporal long-range dependencies (like
rhythm change informations). This interpretation was emphasized by class activation
map visualizations which showed that CNN networks successfully managed to detect
irregular rhythm sections. The choice of the aggregation strategy certainly also depends
on the deﬁnition of the ground truth annotations. If, for instance, records where


## Page 46


Chapter 6 Discussion
42
classiﬁed as AF as soon as some f oscillations or irregular RR interval changes were
included (features that could be well detected by CNN layers) or whether additional
knowledge of e.g. rhythm change durations needed to be captured (which potentially
could be better performed by LSTM layers).
Furthermore, the stacking of multiple LSTM layers is supposed to yield higher level
temporal features at diﬀerent time scales [30],[25]. For the application of character-level
language modeling, Karpathy [24] published some rules of thumbs telling that usually 2
to 3 layers perform well and the number of hidden units should be chosen according to
the amount of available data. Still, throughout the experiments of this work, neither
the number of LSTM layers nor the amount of hidden units had a large impact on the
rhythm classiﬁcation performance.
Another study was recently published by Yin et al. [54], who compared CNN and
RNN performances for the application of natural language processing. They concluded
that no answer can be found to the question which setup generally performs best and
advised to use CNNs for classiﬁcation tasks (like sentiment analysis, where a class is
usually determined by some key features) and RNNs for sequence modeling applications
(like language modeling). Nevertheless, Yin et al. also referenced related works where
RNNs performed well for document-level sentiment classiﬁcation [47] or gated CNNs
outperformed LSTMs on language modeling tasks [13].
Beneﬁts of bidirectional LSTMs and GRUs?
It was assumed that bidirectional
LSTMs could improve the classiﬁcation accuracy particularly for records where patholog-
ical ﬁndings were observed in the ﬁrst part of the time sequence. Given that backward
LSTMs in such cases need to remember detected events over less time steps, the incor-
poration of the backward hidden state was expected to provide beneﬁcial supplementary
information. The experiments of this work, however, did not conﬁrm this hypothesis
(neither the concatenation of hidden states for both directions nor the extraction of
hidden states at the central time step).
Arkhipenko et al. [2] recently evaluated GRUs for the task of sentiment analysis and
found GRUs to outperform both LSTMs and pure CNNs. As introduced in Sec. 2.2.2,
the GRU cell uses a merged formulation of the hidden state and the cell state and also
reduces the number of gates from four to three. However, since performances in ﬁrst
experiments did not seem to improve and as other empirical studies also came to the
conclusion that LSTMs and GRUs often perform comparably well (see e.g. Chung et al.
[10]), we did not follow up on further GRU investigations.
Rise and fall of LSTMs?
Some researchers even state “drop your RNN and LSTM,
they are no good” [12], claiming that companies like Google and Facebook would start
to replace RNN architectures with attention based models. Culurciello [12] argues that
the use of LSTMs should be generally avoided since recurrent architectures are not only
limited in memory capacities but also computationally expensive. Hierarchical attention
models, on the contrary, could integrate more time steps and would require shorter
paths in the backpropagation pass (where the length in tree hierarchies is proportional


## Page 47


Chapter 6 Discussion
43
to the logarithm of the tree depth while standard RNNs propagate the error through
all time steps of the sequence) [12].
6.2 Can Attention Visualizations Support AF
Diagnosis?
In this work, we aimed at developing visualization tools to better understand the internal
processes of neural network models and to support clinicians focusing on meaningful
ECG sections during AF diagnosis. In the following, it will be discussed which attention
maps were the most promising and which challenges might remain.
Class activation maps
The idea of class activation maps proved to be promising
and stunningly simple. The attention maps of the previous section gave visual proof
that global pooling CNNs can facilitate a precise and at the same time interpretable
detection of pathological events in long term ECGs. Still, those CAMs only provide a
rough approximation to the regions of the highest importance for the CNN classiﬁcation.
As it has been shown, when several pathological episodes occur in a single window, one
or more of these episodes could be missed with the CNN focusing on another particular
episode.
Approaches to improve localization abilities of class activation maps were extensively
discussed for weakly supervised object localization applications. An example work that
managed to better capture the full extent of detected objects was 2017 published by
Dahun et al. [26]. In their work, the authors proposed to suppress relevant CNN neurons
of highest activations in a second training phase in order to encourage a network to
look for further class evidences. They found that this ‘two phase learning’ resulted in
more accurate heat maps of localized objects. Concerning the ECG classiﬁcation task
of this thesis, such a two phase learning could potentially allow for the detection of
more pathological episodes.
LSTM class decision plots
The plot of intermediate class decisions provided
attention-like maps for recurrent neural networks. Beside highlighting salient record
sections, it allowed for a better understanding of the sequential input processing and
also helped to identify long-range memory diﬃculties (which were often indicated by
alternating class decisions at the end of the record plot).
Shift perturbations
The ‘attention maps’ that resulted from the computation of
perturbation masks allowed for the examination of saliency without requiring any
modiﬁcations (not to mention any internal parameter extractions) of the underlying
model. By replacing the original ‘occlusion mask’ formulation (where samples were
occluded by constant values, noise, or blur) by shift perturbations, we presented a novel
approach for the detection of pathological episodes in AF and class Other records. The


## Page 48


Chapter 6 Discussion
44
concept of perturbation masks proved to be an interesting tool for the manipulation of
network decisions and might be beneﬁcial for realistic data augmentation. Nevertheless,
it is unlikely that perturbation mask attention visualizations can actually support
clinical diagnosis since the optimization process appeared unstable and the applicability
was limited to a selection of rhythm types.
6.3 Are Attention Mechanisms Beneﬁcial for the
Training Process?
Inspired by the human visual attention system, attention networks learn to focus
on important input details and to fade-out irrelevant background information. The
attention gated CNN architecture studied in this work was therefore expected to ﬁrst
identify important rhythm features on a global scale and to afterward focus on local
morphology information of salient beats (to e.g. more successfully discriminate between
AF and Other rhythm beats which might both show sections of irregular RR intervals
at the coarsest scale).
Attention gating in CNN models
In fact, such a focusing on particular beats
could be observed for the gated attention map examples of Fig. 5.9 (at least for the cases
of AF and Normal rhythm). Contrary to the attention maps reported by Schlemper et
al. [41], highlighted beats were, however, not located in the same rhythm section that
had been before detected by the global classiﬁcation paths.
The reason for this observation can be probably found in the additive attention weight
deﬁnition of Eq. 3.2, where compatibility scores are computed between the intermediate
and the last layer’s feature map. Since ECG records show repetitive patterns throughout
the whole record, it is possible that feature vectors of high compatibility scores less
likely corresponded to beats included in the detected region of the global feature map
(whereas Schlemper et al. [41] processed images where objects could be more easily
discriminated from background regions). Moreover, attention maps that were extracted
for class Other records hardly showed any high activations, which implies that ﬁne-scale
features for those cases did not contribute to the prediction.
Summarizing, it was found that the incorporation of attention gates could slightly
improve the F1 score of the baseline CNN from 0.83 to 0.84 but that resulting attention
maps where less intuitive than simple class activation maps of shallower networks (with
similar performances).


## Page 49


Chapter 7
Conclusion
In this work, convolutional long short-term memory were proposed for the detection
of AF rhythms in single-lead ECG recordings. Combining the beneﬁts of both CNN
and LSTM architectures, the network successfully captured features of morphology and
rhythm changes from raw ECG records while not requiring any pre- or post-processing.
Yielding an F1 score of 0.85 for an 8-fold cross validation on the CinC 2017 challenge
training data, the network performed similarly to the top ranked challenge approaches
with a score of 0.83 on the unavailable test set. To allow for a performance assessment
and a fair comparison with other state-of-the-art approaches, a submission of our best
model to the PhysioNet community is intended. Comparing the temporal feature
aggregation abilities of LSTMs and global pooling layers, a slight superiority of LSTMs
was observed for shallow CNN setups. However, when increasing the depth of CNN
architectures for the feature extraction, no signiﬁcant performance diﬀerences could be
reported.
In addition, various attention visualization techniques were presented for CNN as
well as LSTM architectures.
By successfully highlighting pathological episodes of
morphology or rhythm irregularities, attention maps proved to have a great potential to
support clinicians for cardiac diagnosis in long-term ECGs. It is assumed that attention
mechanisms can help to speed up diagnosis, to yield better classiﬁcation transparency
and to reassess cases of low prediction certainty. The extension of a standard CNN
network with additional trainable attention parameters only insigniﬁcantly improved
the performance from F1 = 0.83 to F1 = 0.84. Resulting attention maps were more
diﬃcult to interpret than simple class activation maps and therefore appeared less
helpful for the task of clinical diagnosis support.
In future research, we plan to adopt our model for the processing of ECG data that was
acquired during magnetic resonance imaging (MRI). Given that the presence of a static
magnetic ﬁeld distorts the recordings of heart activity [36], a special handling of noise
and artifacts will be required to still enable arrhythmia detection. For this purpose,
denoising strategies will be exploited using, for instance, autoencoder networks [20] for
an unsupervised pretraining. Moreover, it is suggested that a pretraining on the large
PhysioNet database with subsequent transfer learning can improve the generalization
abilities of models for the comparably small database.


## Page 50


Bibliography
[1] Al Rahhal, Mohamad M, Yakoub Bazi, Mansour Al Zuair, Esam Othman and Bilel
BenJdira: Convolutional Neural Networks for Electrocardiogram Classiﬁcation. Journal of
Medical and Biological Engineering, pages 1–12, 2018.
[2] Arkhipenko, K, I Kozlov, J Trofimovich, K Skorniakov, A Gomzin and D Turdakov:
Comparison of neural network architectures for sentiment analysis of russian tweets. In Computa-
tional Linguistics and Intellectual Technologies Proceedings of the Annual International Conference
Dialogue, Moscow, RGGU, pages 50–58, 2016.
[3] Bahdanau, Dzmitry, Kyunghyun Cho and Yoshua Bengio: Neural machine translation by
jointly learning to align and translate. arXiv preprint arXiv:1409.0473, 2014.
[4] Behar, Joachim A, Aviv A Rosenberg, Yael Yaniv and Julien Oster: Rhythm and
Quality Classiﬁcation from Short ECGs Recorded Using a Mobile Device. Computing, 44:1, 2017.
[5] Cao, Chunshui, Xianming Liu, Yi Yang, Yinan Yu, Jiang Wang, Zilei Wang, Yongzhen
Huang, Liang Wang, Chang Huang, Wei Xu et al.: Look and think twice: Capturing top-
down visual attention with feedback convolutional neural networks. In Proceedings of the IEEE
International Conference on Computer Vision, pages 2956–2964, 2015.
[6] Chandra, BS, CS Sastry, Soumya Jana and S Patidar: Atrial Fibrillation Detection Using
Convolutional Neural Networks. Computing, 44:1, 2017.
[7] Chen, Edwin: Exploring LSTMs. http://blog.echen.me/2017/05/30/exploring-lstms/.
Accessed: 2018-05-28.
[8] Chen, Gang: A Gentle Tutorial of Recurrent Neural Network with Error Backpropagation. arXiv
preprint arXiv:1610.02583, 2016.
[9] Cho, Kyunghyun, Bart Van Merri¨enboer, Dzmitry Bahdanau and Yoshua Bengio:
On the properties of neural machine translation: Encoder-decoder approaches. arXiv preprint
arXiv:1409.1259, 2014.
[10] Chung, Junyoung, Caglar Gulcehre, KyungHyun Cho and Yoshua Bengio: Empirical
evaluation of gated recurrent neural networks on sequence modeling. arXiv preprint arXiv:1412.3555,
2014.
[11] Clifford, Gari D, Chengyu Liu, Benjamin Moody, Li-wei H Lehman, Ikaro Silva,
Qiao Li, AE Johnson and Roger G Mark: AF classiﬁcation from a short single lead ECG
recording: The Physionet Computing in Cardiology Challenge 2017. Proceedings of Computing in
Cardiology, 44:1, 2017.
[12] Culurciello, Eugenio: The fall of RNN / LSTM.
https://towardsdatascience.com/
the-fall-of-rnn-lstm-2d1594c74ce0/. Accessed: 2018-07-06.
[13] Dauphin, Yann N, Angela Fan, Michael Auli and David Grangier: Language modeling
with gated convolutional networks. arXiv preprint arXiv:1612.08083, 2016.
[14] Elman, Jeffrey L: Finding structure in time. Cognitive science, 14(2):179–211, 1990.


## Page 51


Bibliography
47
[15] Emanet, Nahit: ECG beat classiﬁcation by using discrete wavelet transform and Random
Forest algorithm. In Soft Computing, Computing with Words and Perceptions in System Analysis,
Decision and Control, 2009. ICSCCW 2009. Fifth International Conference on, pages 1–4. IEEE,
2009.
[16] Fong, Ruth C and Andrea Vedaldi: Interpretable explanations of black boxes by meaningful
perturbation. arXiv preprint arXiv:1704.03296, 2017.
[17] Geras, Krzysztof J, Abdel-rahman Mohamed, Rich Caruana, Gregor Urban,
Shengjie Wang, Ozlem Aslan, Matthai Philipose, Matthew Richardson and Charles
Sutton: Blending lstms into cnns. arXiv preprint arXiv:1511.06433, 2015.
[18] Goldberger, Ary L, Luis AN Amaral, Leon Glass, Jeffrey M Hausdorff, Plamen Ch
Ivanov, Roger G Mark, Joseph E Mietus, George B Moody, Chung-Kang Peng and
H Eugene Stanley: Physiobank, physiotoolkit, and physionet. Circulation, 101(23):e215–e220,
2000.
[19] Hermans, Michiel and Benjamin Schrauwen: Training and analysing deep recurrent neural
networks. In Advances in neural information processing systems, pages 190–198, 2013.
[20] Hinton, Geoffrey E and Ruslan R Salakhutdinov: Reducing the dimensionality of data
with neural networks. science, 313(5786):504–507, 2006.
[21] Hochreiter, Sepp and J¨urgen Schmidhuber: Long short-term memory. Neural computation,
9(8):1735–1780, 1997.
[22] Jangra, Manisha, Sanjeev Kumar Dhull and Krishna Kant Singh: Recent trends in
arrhythmia beat detection: A review. In Communication and Computing Systems: Proceedings of
the International Conference on Communication and Computing Systems (ICCCS 2016), Gurgaon,
India, 9-11 September, 2016, page 177. CRC Press, 2017.
[23] Jetley, Saumya, Nicholas A Lord, Namhoon Lee and Philip HS Torr: Learn to pay
attention. arXiv preprint arXiv:1804.02391, 2018.
[24] Karpathy, Andrej: Multi-layer Recurrent Neural Networks (LSTM, GRU, RNN) for character-
level language models in Torch. https://github.com/karpathy/char-rnn/. Accessed: 2018-07-
08.
[25] Karpathy, Andrej: The Unreasonable Eﬀectiveness of Recurrent Neural Networks. http:
//karpathy.github.io/2015/05/21/rnn-effectiveness/. Accessed: 2018-05-29.
[26] Kim, Dahun, Donggeun Yoo, In So Kweon et al.: Two-phase learning for weakly supervised
object localization. arXiv preprint arXiv:1708.02108, 2017.
[27] LeCun, Yann, L´eon Bottou, Yoshua Bengio and Patrick Haffner: Gradient-based
learning applied to document recognition. Proceedings of the IEEE, 86(11):2278–2324, 1998.
[28] Lip, Gregory Y. H., Laurent Fauchier, Saul B. Freedman, Isabelle Van Gelder,
Andrea Natale, Carola Gianni, Stanley Nattel, Tatjana Potpara, Michiel Rienstra,
Hung-Fat Tse and Deirdre A. Lane: Atrial ﬁbrillation. Nature Reviews Disease Primers, 2,
2016.
[29] Maknickas, Vykintas, Algirdas Maknickas and LLC Tesonet: Atrial Fibrillation Classi-
ﬁcation Using QRS Complex Features and LSTM. Computing, 44:1, 2017.
[30] Malhotra, Pankaj, Lovekesh Vig, Gautam Shroff and Puneet Agarwal: Long short
term memory networks for anomaly detection in time series. In Proceedings, page 89. Presses
universitaires de Louvain, 2015.


## Page 52


Bibliography
48
[31] Martis, Roshan Joy, U Rajendra Acharya, KM Mandana, Ajoy Kumar Ray and
Chandan Chakraborty: Application of principal component analysis to ECG signals for
automated diagnosis of cardiac health. Expert Systems with Applications, 39(14):11792–11800,
2012.
[32] Moody, George B and Roger G Mark: The impact of the MIT-BIH arrhythmia database.
IEEE Engineering in Medicine and Biology Magazine, 20(3):45–50, 2001.
[33] Odutayo, Ayodele, Christopher X Wong, Allan J Hsiao, Sally Hopewell, Douglas G
Altman and Connor A Emdin: Atrial ﬁbrillation and risks of cardiovascular disease, renal
disease, and death: systematic review and meta-analysis. Bmj, 354:i4482, 2016.
[34] Oktay, Ozan, Jo Schlemper, Loic Le Folgoc, Matthew Lee, Mattias Heinrich,
Kazunari Misawa, Kensaku Mori, Steven McDonagh, Nils Y Hammerla, Bernhard
Kainz et al.: Attention U-Net: Learning Where to Look for the Pancreas.
arXiv preprint
arXiv:1804.03999, 2018.
[35] Olah, Christopher: Understanding LSTM Networks.
http://colah.github.io/posts/
2015-08-Understanding-LSTMs/. Accessed: 2018-05-29.
[36] Oster, Julien, Raul Llinares, Stephen Payne, Zion Tsz Ho Tse, Ehud Jeruham
Schmidt and Gari D. Clifford: Comparison of three artiﬁcial models of the magnetohydro-
dynamic eﬀect on the electrocardiogram. Computer Methods in Biomechanics and Biomedical
Engineering, 18(13):1400–1417, 2015. PMID: 24761753.
[37] Paszke, Adam, Sam Gross, Soumith Chintala, Gregory Chanan, Edward Yang,
Zachary DeVito, Zeming Lin, Alban Desmaison, Luca Antiga and Adam Lerer:
Automatic diﬀerentiation in PyTorch. In NIPS-W, 2017.
[38] Rajpurkar, Pranav, Awni Y. Hannun, Masoumeh Haghpanahi, Codie Bourn and
Andrew Y. Ng: Cardiologist-Level Arrhythmia Detection with Convolutional Neural Networks.
CoRR, abs/1707.01836, 2017.
[39] Rubin,
Jonathan, Saman Parvaneh, Asif Rahman, Bryan Conroy and Saeed
Babaeizadeh: Densely Connected Convolutional Networks and Signal Quality Analysis to Detect
Atrial Fibrillation Using Short Single-Lead ECG Recordings. arXiv preprint arXiv:1710.05817,
2017.
[40] Sainath, Tara N, Oriol Vinyals, Andrew Senior and Has¸im Sak: Convolutional, long
short-term memory, fully connected deep neural networks.
In Acoustics, Speech and Signal
Processing (ICASSP), 2015 IEEE International Conference on, pages 4580–4584. IEEE, 2015.
[41] Schlemper, Jo, Ozan Oktay, Liang Chen, Jacqueline Matthew, Caroline Knight,
Bernhard Kainz, Ben Glocker and Daniel Rueckert: Attention-Gated Networks for
Improving Ultrasound Scan Plane Detection. arXiv preprint arXiv:1804.05338, 2018.
[42] Selzer, Arthur: THE CIBA COLLECTION OF MEDICAL ILLUSTRATIONS: Volume
5—Heart— A Compilation of Paintings on the Normal and Pathologic Anatomy and Physiology,
Embryology, and Diseases.
[43] Shi, Xingjian, Zhourong Chen, Hao Wang, Dit-Yan Yeung, Wai-Kin Wong and Wang-
chun Woo: Convolutional LSTM Network: A Machine Learning Approach for Precipitation
Nowcasting. CoRR, abs/1506.04214, 2015.
[44] Shyu, Liang-Yu, Ying-Hsuan Wu and Weichih Hu: Using wavelet transform and fuzzy neural
network for VPC detection from the Holter ECG. IEEE Transactions on Biomedical Engineering,
51(7):1269–1273, 2004.
[45] Simonyan, Karen, Andrea Vedaldi and Andrew Zisserman: Deep inside convolutional net-
works: Visualising image classiﬁcation models and saliency maps. arXiv preprint arXiv:1312.6034,
2013.


## Page 53


Bibliography
49
[46] Supratak, Akara, Hao Dong, Chao Wu and Yike Guo: DeepSleepNet: A model for
automatic sleep stage scoring based on raw single-channel EEG. IEEE Transactions on Neural
Systems and Rehabilitation Engineering, 25(11):1998–2008, 2017.
[47] Tang, Duyu, Bing Qin and Ting Liu: Document modeling with gated recurrent neural network
for sentiment classiﬁcation. In Proceedings of the 2015 conference on empirical methods in natural
language processing, pages 1422–1432, 2015.
[48] Teijeiro, Tom´as, Constantino A. Garc´ıa, Daniel Castro and Paulo F´elix: Arrhythmia
Classiﬁcation from the Abductive Interpretation of Short Single-Lead ECG Records.
CoRR,
abs/1711.03892, 2017.
[49] Tsironi, Eleni, Pablo Barros and Stefan Wermter: Gesture recognition with a convolu-
tional long short-term memory recurrent neural network. Bruges, Belgium, 2, 2016.
[50] Wang, Xiaosong, Yifan Peng, Le Lu, Zhiyong Lu, Mohammadhadi Bagheri and
Ronald M Summers: Chestx-ray8: Hospital-scale chest x-ray database and benchmarks on
weakly-supervised classiﬁcation and localization of common thorax diseases. In 2017 IEEE Confer-
ence on Computer Vision and Pattern Recognition (CVPR), pages 3462–3471. IEEE, 2017.
[51] Warrick, Philip and Masun Nabhan Homsi: Cardiac Arrhythmia Detection from ECG
Combining Convolutional and Long Short-Term Memory Networks. Computing, 44:1, 2017.
[52] Westhuizen, JVD and J Lasenby: What does an LSTM look for in classifying heartbeats?
2017.
[53] Yang, Guangying and Yue Chen: The Study of Electrocardiograph Based on Radial Basis
Function Neural Network. In Intelligent Information Technology and Security Informatics (IITSI),
2010 Third International Symposium on, pages 143–145. IEEE, 2010.
[54] Yin, Wenpeng, Katharina Kann, Mo Yu and Hinrich Sch¨utze: Comparative study of cnn
and rnn for natural language processing. arXiv preprint arXiv:1702.01923, 2017.
[55] Zabihi, Morteza, Ali Bahrami Rad, Aggelos K Katsaggelos, Serkan Kiranyaz,
Susanna Narkilahti and Moncef Gabbouj: Detection of Atrial Fibrillation in ECG Hand-
held Devices Using a Random Forest Classiﬁer. Computing, 44:1, 2017.
[56] Zagoruyko, Sergey and Nikos Komodakis: Paying more attention to attention: Improv-
ing the performance of convolutional neural networks via attention transfer. arXiv preprint
arXiv:1612.03928, 2016.
[57] Zeiler, Matthew D and Rob Fergus: Visualizing and understanding convolutional networks.
In European conference on computer vision, pages 818–833. Springer, 2014.
[58] Zhao, Bo, Jiashi Feng, Xiao Wu and Shuicheng Yan: A survey on deep learning-based
ﬁne-grained object classiﬁcation and semantic segmentation. International Journal of Automation
and Computing, 14(2):119–135, Apr 2017.
[59] Zhou, Bolei, Aditya Khosla, Agata Lapedriza, Aude Oliva and Antonio Torralba:
Learning Deep Features for Discriminative Localization. In The IEEE Conference on Computer
Vision and Pattern Recognition (CVPR), June 2016.
[60] Zihlmann, Martin, Dmytro Perekrestenko and Michael Tschannen: Convolutional
recurrent neural networks for electrocardiogram classiﬁcation. Computing, 44:1, 2017.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
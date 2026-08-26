---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1909.11791v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1909.11791v1_Single-modal_and_Multi-modal_False_Arrhythmia_Alarm_Reduction_using_Attention-ba

> Source: 1909.11791v1_Single-modal_and_Multi-modal_False_Arrhythmia_Alarm_Reduction_using_Attention-ba.pdf

> Pages: 9

---


## Page 1


1
Single-modal and Multi-modal False Arrhythmia
Alarm Reduction using Attention-based
Convolutional and Recurrent Neural Networks
Sajad Mousavi, Atiyeh Fotoohinasab and Fatemeh Afghah
School of Informatics, Computing and Cyber Systems, Northern Arizona University, Flagstaff, USA
{SajadMousavi, af2329, Fatemeh.Afghah}@nau.edu
Abstract—This study proposes a deep learning model that
effectively suppresses the false alarms in the intensive care units
(ICUs) without ignoring the true alarms using single- and multi-
modal biosignals. Most of the current work in the literature
are either rule-based methods, requiring prior knowledge of
arrhythmia analysis to build rules, or classical machine learning
approaches, depending on hand-engineered features. In this
work, we apply convolutional neural networks to automatically
extract time-invariant features, an attention mechanism to put
more emphasis on the important regions of the input segmented
signal(s) that are more likely to contribute to an alarm, and
long short-term memory units to capture the temporal informa-
tion presented in the signal segments. We trained our method
efﬁciently using a two-step training algorithm (i.e., pre-training
and ﬁne-tuning the proposed network) on the dataset provided
by the PhysioNet computing in cardiology challenge 2015. The
evaluation results demonstrate that the proposed method obtains
better results compared to other existing algorithms for the false
alarm reduction task in ICUs. The proposed method achieves a
sensitivity of 93.88% and a speciﬁcity of 92.05% for the alarm
classiﬁcation, considering three different signals. In addition, our
experiments for 5 separate alarm types leads signiﬁcant results,
where we just consider a single-lead ECG (e.g., a sensitivity of
90.71%, a speciﬁcity of 88.30%, an AUC of 89.51 for alarm type
of Ventricular Tachycardia arrhythmia) 1.
Index Terms—False alarm reduction, arrhythmia, convolu-
tional neural networks, recurrent neural networks, attention
mechanism, biomedical signals.
I. INTRODUCTION
T
HE electrocardiogram (ECG) is a biomedical signal that
includes information about the electrical activity of heart
function and heart conditions over a period of time. Monitoring
and interpretation of ECG signals serve the most useful tool
for medical staff in ICUs to check the patients heart condition
such as arrhythmia, ventricular hypertrophy, and myocardial
infarction, etc. Cardiac arrhythmias can cause serious and even
potentially fatal symptoms if they are not inspected promptly.
Although patient-monitoring alarms play an indispensable role
in saving patients’ lives, the high rate of false alarms not
only can be annoying for patients but also may delay the
response of medical staff due to making them less sensitive to
warnings. Moreover, it can delay patients’ recovery by causing
1This material is based upon work supported by the National Science
Foundation under Grant Number 1657260. Research reported in this pub-
lication was supported by the National Institute On Minority Health And
Health Disparities of the National Institutes of Health under Award Number
U54MD012388.
sleep deprivation and depressed immune systems. Therefore,
suppressing the rate of false alarms in ICUs will improve the
quality of patient care and reduce the number of missed true
fatal alarms by medical staff. As reported by Aboukhalil et
al. [1] and Drew et al. [2], the rate of false alarms in ICUs
reaches as high as almost 90%. In regard to this concern, the
PhysioNet directed the challenge 2015 to reduce the incidence
of false arrhythmia alarms in ICUs while the true alarms are
not suppressed [3].
In order to reduce the rate of false alarms in ICUs, various
methods have been proposed. Typically, they can be classiﬁed
into two general categories: 1) methods based on cardiac
rules and 2) machine learning based methods. In the ﬁrst
category, some cardiac rules are deﬁned by experts to detect
alarm types. All of the approaches in this category depend
primarily on the QRS-complex detection in order to estimate
heart rate (HR) and evaluate the signal quality. Ansari et
al. [4] adopted several peak detection algorithms to create a
robust peak detection algorithm and exploited the information
from all three ECG, ABP and PPG signals. Fallet et al. [5]
used an adaptive frequency tracking algorithm to estimate HR
from PPG and ABP signals and an adaptive mathematical
morphology approach to estimate HR from the ECG. Also,
they exploited the Spectral Purity Index (SPI) to quantify
the morphological changes of QRS complexes related to the
Ventricular Arrhythmia. Then, they employed a set of rules
based on the HR and the SPI to inspect false alarms. Plesinger
et al. [6] and Couto et al. [7] applied a set of rules on each
alarm types to distinguish between false and true alarms using
ECG, ABP and PLETH signals. He et al.[8] classiﬁed alarms
using ECG and ABP signals by following a set of rules related
to Signal Quality Index (SQI) and Heart Rate Variability
(HRV). However, one challenge with the false alarm detection
based on cardiac rules is the need for an expert to determine
the rules and the required thresholds. To tackle this, recent
studies have exploited machine-learning approaches to detect
false alarms.
Machine learning ﬁeld has many different applications
ranging from computer vision, wireless and IoT networks,
Unmanned aerial vehicle (UAV) navigation to clinical pre-
diction models [9], [10], [11], [12], [13], [14], [15], [16],
[17], [18]. In machine learning based methods, a false alarm
detection model is trained using some extracted features from
the dataset’s samples. In [19], features of interest are extracted
arXiv:1909.11791v1  [q-bio.QM]  25 Sep 2019


## Page 2


2
from the two-dimensional beat-to-beat correlograms using Fast
Fourier Transform (FFT) and principle component analysis
(PCA) as well as basic statistical and self-similarity analy-
sis. Then, several machine learning algorithms are evaluated
using the extracted features to detect false alarms. In [20],
a random forest technique is applied to reduce false alarms
using different methods of probability and class assignments.
Lehman et al. [21] adopted a supervised denoising autoencoder
(SDAE) to identify false alarms in Ventricular Tachycardia
using features of interest extracted by FFT. Kalidas and Tamil
[22] used a combination of logical and SVM algorithm to
classify arrhythmias using ECG and PPG signals. In their
work, the features of interest are a set of both time and
frequency-domain information. [23] and [24] proposed game
theoretical approaches in order to extract more discriminative
features to reduce the rate of false alarms.
The performance of the classiﬁcation methods highly de-
pends on the quality of class discriminating features in terms
of on what extent they can capture the main characteristics of
the input. Most of the machine learning methods are trained
based on hand-crafted features. However, one challenge facing
the hand-crafted features is that it depends on a speciﬁc
dataset, thereby new features may be needed if the dataset
changes in terms of size and variety of patients. Although deep
learning algorithms have been utilized in medical applications
[25], [26], [27], only a few numbers of studies in the false
alarm reduction literature applied deep learning methods and
automatic feature extraction [21], [28]. In this paper, we
propose a deep learning-based approach to reduce the rate
of false alarms in ICUs for ﬁve life-threatening arrhythmias:
Asystole (ASY), Extreme Bradycardia (EBR), Extreme Tachy-
cardia (ETC), Ventricular Tachycardia (VTA), and Ventricular
Flutter/Fibrillation (VFB). The performance of the proposed
model is evaluated using the publicly available alarm dataset
for ICUs provided by ”PhysioNet computing in cardiology
challenge 2015”. The experimental results show the proposed
method can signiﬁcantly suppress the rate of false alarms in
ICU equipment with respect to ﬁve mentioned life-threatening
arrhythmias without suppressing true alarms. In the following,
the main contributions of this work are summarized:
• We present a multi-modal model that integrates three
main signals of arterial blood pressure (ABP), photo-
plethysmograph (PPG) and ECG in order to enhance
the accuracy of arrhythmia detection and reduce the
false alarm rate in ICUs. A multi-modal approach that
analyzes a set of independent sources/signals for alarm
detection can signiﬁcantly improve the alarm detection
performance. The reason behind this idea is that each
independent channel or source of data is inclined to
distinct noise and/or artifacts, thereby a hidden pattern
in a certain channel caused by noise and/or artifacts can
be disclosed by other clean channels.
• We develop a network architecture for automatic feature
extraction that utilizes a convolutional neural network
(CNN) with two consecutive one-dimensional convolu-
tional layers composed of different ﬁlter sizes, atten-
tion and long short-term memory (LSTM) units, and a
classiﬁcation layer. The CNN part extracts a vector of
features from each segment of a single channel, while the
attention and LSTM units are trained to identify the most
effective parts of the segment in the detection and capture
long-range of dependencies between segments of an input
signal, respectively. Typically, some indicators appear in
the signals as early as few hours before cardiac events
[29], [30], [31]. Since considering the entire length of the
signals is not necessarily feasible, an attention mechanism
along with a memory-based approach can divide the
signals into different partitions by putting a higher weight
on the most important ones to save space/computation as
well as enhance the accuracy.
• We apply two loss functions of Mean False Error (MFE)
and Mean Squared False Error (MSFE) instead of using
the common loss function in deep learning algorithms;
Mean Squared Error (MSE), to reduce the effect of class
unbalanced dataset on degrading the performance. This
proposed loss function propagates the training error for a
misclassiﬁed sample without considering its membership
to the major or minor class.
• We introduce a two-step training algorithm to train the
proposed model effectively so that the effect of the
unbalanced class problem is alleviated. In the ﬁrst step, a
model is trained for each of the three signals separately
to extract the most distinctive features in regard to each
signal. In the second step, the model is trained to generate
a label given the three signals.
In the next section, we describe the proposed false arrhyth-
mia alarm reduction method. Section III provides a description
of the dataset used in this study. In Section IV, we present
the experimental results and compare the performance of
the proposed algorithm to other state-of-the-art algorithms,
followed by the conclusion in Section V.
II. METHODOLOGY
We develop a deep learning model to classify the ar-
rhythmias from the segments of three common physiological
signals of ECG, ABP, and PPG signals based on a two-
stage approach to further reduce the false alarm rate. In the
ﬁrst part, we develop three pre-trained networks to extract
features of interest for the three biosignals separately, followed
by a shallow neural network in the second part that uses
the extracted features from the pre-trained nets to perform
a classiﬁcation task. At each time step, pre-trained networks
extract features of their corresponding input signals, and then,
the extracted features are averaged and fed to the fully-connect
layer with the size of 256 neurons followed by a dropout block.
Finally, a softmax layer is used to determine the probability of
the input signal belonging to each class of interest (true or false
alarm). Figure 1 shows an overall view of the proposed model
for reducing false arrhythmia alarms in ICUs. It should be
noted that the dropout block is frozen during the testing phase
and is just used in the training phase. In the following sections,
we describe the details of different parts of the proposed
model.


## Page 3


3
PPG NET
ECG NET
ABP NET
ECG
ABP
PPG
AVG
256
Dense
Dropout 0.5
512
Soft 
max
T alarm
F alarm
Pretrained Nets 
FC
Figure 1: An overview of the network architecture for multi-model false alarm reduction method. AVG: average, FC: fully
connected layer.
A. Pre-processing
Prior to feature extraction and classiﬁcation parts, the ECG,
ABP, and PPG signals were subjected to normalization and
segmentation steps. For the normalization step, the signals are
normalized to a range of 0 to 1. The segmentation part is
perfomed using a sliding 200-sample window with an overlap
of 25% for all three signals separately. These segments are
fed to their corresponding networks (i.e., ECG, ABP, and PPG
NETs as shown in Figure 1) as the input sequences. It is worth
mentioning that the pre-processing process does not include
any noise removing and/or ﬁltering steps to remove muscle
artifacts and baseline wander.
B. The model architecture
The following subsections describe the main parts of the
automatic feature extraction network. We train a feature ex-
traction network for each of the three input signals separately.
Figure 2 illustrates the proposed network architecture for
automatic feature extraction.
1) Convolutional neural network (CNN): We employ two
consecutive 1D convolutional layers with different sizes of
ﬁlters and a max-pooling layer following the ﬁrst convolutional
layer. The ﬁrst convolutional layer is composed of 32 ﬁlters
with a kernel size of 2×1 and a stride 1, and a Rectiﬁed Linear
Unit (ReLU) layer. The second convolutional layer with larger
sizes of ﬁlters has 64 ﬁlters with a kernel size of 2 × 1 and
a stride 1, and a ReLU layer. The max-pooling layer has a
pooling region of size 2 × 1 with a stride size of 2 × 1. At
each time step, a sequence of a segmented signal (e.g., ECG,
ABP or PPG) with the size of n is fed to the CNN to extract
features of interest. The second CNN layer generates D feature
maps of size L×1 for each sample of the input signal, which
is converted to L vectors of D-dimension as follows:
Ct = [Ct,1, Ct,2, . . . , Ct,L],
Ct,i ∈RD.
Here, we have 64 feature maps with the sizes of 5 × 1 (see
Figure 2).
2) Attention and Long Short-Term Memory (LSTM) units:
We use an attention unit to learn the most effective parts
of the input signal that are responsible to trigger a speciﬁc
alarm. This unit assigns a probability value to each part of the
signal to specify its importance in the prediction process (e.g.,
predicting true or false alarm). For instance, as depicted in
Figure 2, the attention unit assigns a probability value to each
vector extracted from the input segment by the CNN. Finally,
an expected value of the most effective regions of the input
segments is generated using the probability values provided
by the attention units (represented by the feature vector, Ct).
Figure 3 illustrates a systematic diagram of the attention unit
utilized in our proposed model. The attention unit is fed by
two inputs: (1) L feature vectors, Ct,1, Ct,2, . . . , Ct,L, where
each Ct,i represents a different part of the input segment, and
(2) A hidden state ht−1, which is the internal state of the RNN
at the previous time step, t−1. Then, it calculates a vector, ct
which is a weighted sum over feature slices, Ct,i. With respect
to the aforementioned assumptions, the attention mechanism
can be formulated as:
αt,i = f(tanh(Whht−1 + WCCt,i))
i ∈1, 2, . . . , L,
(1)
ct =
L
X
i=1
αt,iCt,i,
(2)
In the above equations, αt,i is the importance of part i of
the input segment. f(.) is a softmax function that processes a
vector of L real numbers as input, and normalizes them into
probability values. At ﬁrst, a vector consisted of a weighted
sum over Ct,i and ht−1 values is created and passed to the
tanh function. Then, the softmax function normalizes the L
values of the input vector and creates αt,i. In other words,
each αt,i is considered as the amount of importance of the
corresponding vector Ct,i among L vectors in the input seg-
ment. Finally, the attention unit calculates ct, a weighted sum
of all vectors Ct,i with respect to αt,is. Following the above
process, the model attempts to learn to put more emphasis
on the important regions of the input segment with higher


## Page 4


4
ht­1
Attention 
Model 
Attention 
Model 
Attention 
Model 
Fully connected Layer
SoftMax Function
ct
ct+1
ct+n
ht
ht+n­1
LSTM
LSTM
LSTM
T Alarm
F Alarm
Conv1d 
 
stride (1,1) 
2 × 1, 32
MaxPool 
 
stride (2,1) 
2 × 1
Conv1d 
 
stride (1,1) 
2 × 1, 64
 
Reshape 
 
 
n × 10 × 20
 
Cn
5 × 64
 
Ci
5 × 64
 
C1
5 × 64
ECG/ABP/PPG
Figure 2: The network architecture of the proposed model for
feature extraction.
probabilities that make to trigger an alarm (e.g., a false or
true alarm) in ICUs.
In order to extract temporal information and capture long-
range of dependencies between segments of the input signal,
we employ a stack of two long short-term memory (LSTM)
units with sizes of 256. The LSTM units are following the
attention units and take ct+i values produced by the attention
units and the previous hidden states of the LSTM units as
inputs to generate the next hidden states. In other words, the
LSTM unit takes ct , the output of attention unit at time t, and
ht−1, previous hidden state, to return the next hidden state ht.
The new hidden states are fed to the attention units to produce
the value of ht at the next step and also the fully-connected
layer with a size of 256 (see Figure 2).
3) Classiﬁcation layer: This layer speciﬁes the label of the
input signal (i.e., true or false alarm) and consists of a fully-
connected layer followed by a softmax layer. The softmax
Ct,1
ht­1
ct
SoftMax
⋅
∑
i=0
L
Ct,i
αt,i
αt,1
αt,2
αt,L
Tanh
wc1
Ct,2
wc2
Ct,L
wcL
wh1
wh2
whL
×
×
×
+
Figure 3: A systematic diagram of the attention unit. The
attention unit takes as input vertical feature slices, Ct,i i ∈
1, 2, . . . , L, and the RNN previous hidden state, ht−1. Then,
it computes a linear weighted vector, ct that is a multiplication
of each feature slice and its corresponding importance, αt,i.
layer assigns probabilities that the given input belongs to each
of the class labels (i.e., true or false alarm classes). Note that
this layer is removed while the model depicted in Figure 2 is
used as a feature extractor in the network illustrated in Figure
1.
C. Loss calculation
An important caveat in the false alarm reduction research is
the class imbalance problem, meaning that the number of true
alarms is much less than the false alarms. This problem causes
to drop the performance of the applied method for the minor
class. To tackle this problem, we utilize a combination of two
loss functions of mean false error (MFE) and mean squared
false error (MSFE) [32], [33] instead of the commonly used
Mean Squared Error (MSE) in deep learning algorithms. These
loss functions calculate the training error without considering
the membership of the misclassiﬁed sample to the major or
minor class. In other words, the MFE and MSFE methods
capture the training error of the classes equally as opposed
to the MSE method that is biased to the major class in
a imbalanced dataset. The loss functions can be deﬁned as
follows:
l(gi) = 1
Gi
Gi
X
i=j
(yj −ˆyj)2,
(3)
lMF E =
N
X
i=1
l(gi),
(4)
lMSF E =
N
X
i=1
l(gi)2,
(5)
In the above equations, gi is the class label (e.g., true or
false alarm), Gi is the number of samples in the class gi, N
is the number of available classes (in this study, we have two
classes), and l(gi) is the error calculated over the class gi.
D. Training algorithm
In order to effectively train the proposed model via back-
propagation algorithm, we present a two-step training algo-
rithm as illustrated in 1. Step 1 (lines 1-9) involves extracting


## Page 5


5
the features of interest for a speciﬁc input signal (i.e., for each
of ECG, ABP, and PPG signals, separately). Then, pre-trained
networks are used as feature extractors for their corresponding
models including ECG, ABP, and PPG. In this step, in order
to apply the pre-trained networks as feature extractors, only
the output of the fully-connected layer in the classiﬁcation
layer is utilized to represent the given signal and the softmax
layer is discarded (i.e., line 8). In step 2 (lines 10-16), the
classiﬁcation task is accomplished using the three signals as
shown in Figure 1. It must be pointed out that the three pre-
trained networks are frozen during training process and the
second part of the model is trained to generate a label. Also,
training the models in both steps are performed with the same
hyper-parameters.
Algorithm 1 Two-step training algorithm for the proposed
model
Input: hyper-parameters, data
Output: f model
Step 1:
1: for each modal in [ECG, ABP, PPG] do
2:
Initialize NET[modal] with random weights
3:
for i = 1 to n epochs do
4:
for each batch in batch data(data, modal) do
5:
NET[modal] ←train network
(NET[modal], batch),
as shown in Figure 2
6:
end for
7:
end for
8:
NET[modal] ←r softmax layer(NET[modal])
9: end for
Step 2:
10: Initialize f model with random weights
11: for i = 1 to n epochs do
12:
for each batch in batch data(data) do
13:
f model ←train model(f model, NET[ECG],
NET[ABP], NET[PPG], batch),
as shown in Figure 1
▷Learning for NET[.] is frozen.
14:
end for
15: end for
16: return f model
III. DATASET
We applied the publicly available alarm database for ICUs
provided by PhysioNet computing in cardiology challenge
2015 [3], [34]. It includes ﬁve types of life-threatening arrhyth-
mia alarms: Asystole (ASY), Extreme Bradycardia (EBR),
Extreme Tachycardia (ETC), Ventricular Tachycardia (VTA),
and Ventricular Flutter/Fibrillation (VFB). The deﬁnition and
visualization of each alarm are presented in Table I and in
Figure 5, respectively. The training set includes 750 recordings
and the test set includes 500 recordings. The test set has
not been publicly available yet, therefore we use the training
set for both test and training purposes. Each is recording
composed of two ECG leads and one or more pulsatile
waveforms (i.e., the photoplethysmogram (PPG) and/or arterial
blood pressure (ABP) waveform). Figure 4 shows a sample of
each type of the ECG, ABP and PPG signals. The signals were
re-sampled to a resolution of 12 bit and frequency of 250 Hz
and ﬁltered by a ﬁnite impulse response (FIR) bandpass [0.05
to 40 Hz] and mains notch ﬁlters for denoising. The alarms
were labeled with a team of expert to either ’true’ or ’false’.
Table II shows the statistics of the numbers of true and false
alarms of each arrhythmia type in the training set.
ECG
ABP
PPG
Figure 4: Illustration of an electrocardiogram (ECG), an arte-
rial blood pressure (ABP) and a photoplethysmogram (PPG)
signal.
ASY
EBR
ETC
VTA
VFB
Figure 5: Five common critical alarm types in the intensive
care units as used in the PhysioNet/Computing in Cardiology
Challenge 2015 [3].


## Page 6


6
Table I: Alarms deﬁnition
Alarm Type
Deﬁnition
Asystole(ASY)
There might not be heartbeats for more than 4s in the signal
Extreme Bradycardia (EBR)
The heart rate is less than 40 beats per minute (bpm)
Extreme Tachycardia (ETC)
The heart rate would be greater than 140 bpm for 17 consecutive beats
Ventricular Tachycardia (VTA)
A sequence of ﬁve or more ventricular beats with the heart rate greater than 100 bpm in the signal
Ventricular Flutter/Fibrillation (VFB)
A rapid Fibrillatory, ﬂutter, or oscillatory waveform for at least 4 seconds in the signal
HR: Heart rate
Table II: The statistics of the numbers of true and false alarms of each arrhythmia type.
Alarm
# of patients
# of false alarms
# of true alarms
Asystole (ASY)
122
100
22
Extreme Bradycardia (EBR)
89
43
46
Extreme Tachycardia (ETC)
140
9
131
Ventricular Tachycardia (VTA)
341
252
89
Ventricular Flutter/Fibrillation (VFB)
58
52
6
Total
750
456
294
IV. EXPERIMENTAL RESULTS
A. Experimental Design
The performance of the proposed model was evaluated us-
ing the PhysioNet challenge-2015 dataset. Since multi-modal
prediction is based on the three signals of ECG, ABP and
PPG, only 220 samples out of 750 recordings that include
all these signals are used and for the single-modal method
all samples are utilized. The PhysioNet challenge 2015 [34]
have considered two main events: (i) real-time setting in which
the information before the alarm onset can be used, and
(ii) retrospective setting in which up to 30 seconds of data
after the alarm can be used. In this study, we focus on the
real-time setting where only information prior to occurring
the alarm is used. As mentioned above, using all signals
in the learning process makes the model take beneﬁt of
all available information and extract the correlation between
different models. We used k-fold cross-validation approach to
train and test the proposed model with a k size of 10 unless
explicitly stated otherwise. Indeed, we divided the dataset into
k= 10 folds. Then, for each fold of the 10 folds, one fold is
used for evaluating the model and the remaining 9 folds are
used to train the model. In the end, all evaluation results were
concatenated.
Both whole model and the three networks (ECG, ABP and
PPG Nets) were trained with a maximum of 100 epochs and
a mini-batch size of 10. The RMSProp optimizer was applied
to minimize the lMF E loss with a learning rate parameter
of α = 0.001. Two different regularization techniques were
used to prevent the overﬁtting problem. First, the dropout
layer with the probability of dropping of 0.5 (as shown in
Figure 1). At every learning iteration, the dropout function
chooses the some nodes randomly and deletes them along with
their connections. Second, an additional L2 regularization term
with β = 0.001 was added to the loss function. This kind of
regularization tries to punish the model parameters with large
values. As a result, it prevents an unstable learning (i.e., the
exploding gradient problem). Python programming language
along with Google Tensorﬂow deep learning library were used
to implement our model. Furthermore, a machine with 8 CPUs
(Intel(R) Xeon(R) CPU @ 3.60 GHz), 32 GB memory and
Ubuntu 16.04 was utilized to run the k-fold cross validation.
The training time for each epoch was 98 seconds on average
and the testing time for each batch of 20 EEG epochs was
approximately 0.102 seconds.
Different metrics were considered to assess the performance
of the proposed model. These metrics include accuracy (ACC),
sensitivity (SEN), speciﬁcity (SPE), precision (PRE), F1-score,
and area under the ROC curve (AUC). We also report the
PhysioNet Challenge 2015 score for our proposed method. It
is deﬁned as score = (TP +TN)/(TP +TN+FP +5×FN),
where TP is true positives, FP is false positives, FN is false
negatives, and TN is true negatives. All results are reported as
an average over k-folds, where k can set to 5 and 10).
B. Results and Discussion
The results in Table III represent the alarm classiﬁcation
success for our proposed method against other methods in
the literature while three signals (i.e., ECG II, ABP and
PPG) are considered. It can been seen from the table that
our model signiﬁcantly outperforms other methods. We also
experimented our single-modal (using just one single lead)
approach to bold how outcome might be different. Table III
demonstrates using the multi-modal approach absolutely leads
in better performance results compared to the single-modal
one.
The results provided in Table III are for 220 samples of
dataset with three available signals, aggregating all alarm
types. We also evaluated our model with samples with just
Ventricular Tachycardia alarm type. There were two main
reasons that we selected this alarm type, (1) the number
of samples for other life-threatening arrhythmia alarm types
were too small, Asystole (34: 4 true and 30 false alarms),
Extreme Bradycardia (30: 21 false and 9 true alarms), Extreme
Tachycardia (15: 14 false and 1 true alarms), Ventricular-
Flutter/Fibrillation (17: 12 false and 5 true alarms), and Ven-
tricular Tachycardia (124: 106 false and 18 true alarms), (2) the
Ventricular Tachycardia alarms are more difﬁcult than other
alarm types to detect [34]. Table IV shows the performance


## Page 7


7
of our proposed model for Ventricular Tachycardia alarm
type using a single-lead signal and multi-lead signals. Our
method achieves remarkable results for both the multi-modal
and the single-modal (ECG II) approaches, a sensitivity and
a speciﬁcity of 93.75% and 93.92% for the single-modal
technique, and a sensitivity and a speciﬁcity of 93.75% and
95.49% for the multi-modal technique. As shown in the table,
our method outweighs the other method signiﬁcantly. It also
can be see that using all available signals performs better
compared to the single-lead signal.
We also investigated how our model behaves for all alarm
types using single-lead ECG waveforms. Table V compares
the performance (in terms of true positive rate (TPR or also
called the sensitivity) true negative rate (TNR or also called
speciﬁcity) and AUC) of various algorithms using different
signals. As can be seen in Table V, the proposed method
performs better than the methods proposed by Lehman et al.
[21] and Li et al. [35] on Ventricular Tachycardia (VTA) alarm.
Furthermore, our method using single-lead ECG (ECG II) de-
tects Extreme Bradycardia (EBR), Extreme Tachycardia (ETC)
and Ventricular-Flutter/Fibrillation (VFB) alarms signiﬁcaly
better than other methods using two-lead ECG (Lehman et
al. [21]) and all available signals, including ECG II, ECG
V, ABP and PPG (Ansari et al. [36] and Gajowniczek et al.
[20]). Moreover, as shown in Table V, our proposed single-
modal method leads to comparable results (in some cases, even
better outcomes) for detecting Asystole (ASY) and Ventric-
ular Tachycardia (VTA) arrhythmical alarm types compared
to other listed algorithms that have utilized more than one
signal. In addition, we note that here our remarkable results
were obtained using a single-lead ECG (ECG II), however
having more than one modal would leads to a improvement
in performance results.
Furthermore, Table VI reports the evaluation results of our
single-modal proposed method with various metrics, including
the challenge score provided by the PhysioNet Challenge
2015, using just the ECG II signal. This table can be used
as a reference to compare future work.
V. CONCLUSION
False arrhythmia alarm reduction in ICUs is a challenging
classiﬁcation problem because of the presence of different
sources of noise and artifacts in the data (i.e., the collected
signals) as well as a large number of false alarms that results
in the class imbalance problem. In this study, we proposed
a deep learning-based network composed of the CNN layers,
attention mechanism, and LSTM units to reduce false alarm
arrhythmia in ICUs. We also utilized a new loss function
to alleviate the effect of the class imbalance problem while
training the model. Our proposed approach utilized a two-
step training algorithm that trains the model for each modal
(i.e., ECG, ABP, and PPG) to efﬁciently extract features, and
then uses the combined features of each modal to classify
the three-input signal to a true or false alarm (i.e., in a multi-
modal way). Our proposed multi- and single-modal approaches
demonstrated high performance for the suppression of false
alarms without disregarding the true alarms compared to the
existing algorithms in the literature.
REFERENCES
[1] A. Aboukhalil, L. Nielsen, M. Saeed, R. G. Mark, and G. D. Clifford,
“Reducing false alarm rates for critical arrhythmias using the arterial
blood pressure waveform,” Journal of biomedical informatics, vol. 41,
no. 3, pp. 442–451, 2008.
[2] B. J. Drew, P. Harris, J. K. Z`egre-Hemsey, T. Mammone, D. Schindler,
R. Salas-Boni, Y. Bai, A. Tinoco, Q. Ding, and X. Hu, “Insights
into the problem of alarm fatigue with physiologic monitor devices:
a comprehensive observational study of consecutive intensive care unit
patients,” PloS one, vol. 9, no. 10, p. e110274, 2014.
[3] PhysioNet, Reducing False Arrhythmia Alarms in the ICU, 2015,
accessed July 28, 2016. [Online]. Available: http://www.physionet.org/
challenge/2015/
[4] S. Ansari, A. Belle, and K. Najarian, “Multi-modal integrated approach
towards reducing false arrhythmia alarms during continuous patient
monitoring: the physionet challenge 2015,” in 2015 Computing in
Cardiology Conference (CinC).
IEEE, 2015, pp. 1181–1184.
[5] S. Fallet, S. Yazdani, and J.-M. Vesin, “A multimodal approach to reduce
false arrhythmia alarms in the intensive care unit,” in 2015 Computing
in Cardiology Conference (CinC).
IEEE, 2015, pp. 277–280.
[6] F. Plesinger, P. Klimes, J. Halamek, and P. Jurak, “False alarms in
intensive care unit monitors: detection of life-threatening arrhythmias
using elementary algebra, descriptive statistics and fuzzy logic,” in
Computing in Cardiology Conference (CinC), 2015.
IEEE, 2015, pp.
281–284.
[7] P. Couto, R. Ramalho, and R. Rodrigues, “Suppression of false ar-
rhythmia alarms using ecg and pulsatile waveforms,” in Computing in
Cardiology Conference (CinC), 2015.
IEEE, 2015, pp. 749–752.
[8] R. He, H. Zhang, K. Wang, Y. Yuan, Q. Li, J. Pan, Z. Sheng, and
N. Zhao, “Reducing false arrhythmia alarms in the icu using novel signal
quality indices assessment method,” in 2015 Computing in Cardiology
Conference (CinC).
IEEE, 2015, pp. 1189–1192.
[9] S. S. Mousavi, M. Schukat, and E. Howley, “Trafﬁc light control using
deep policy-gradient and value-function-based reinforcement learning,”
IET Intelligent Transport Systems, vol. 11, no. 7, pp. 417–423, 2017.
[10] F. Afghah, A. Shamsoshoara, L. Njilla, and C. Kamhoua, “A reputation-
based stackelberg game model to enhance secrecy rate in spectrum leas-
ing to selﬁsh iot devices,” in IEEE INFOCOM 2018-IEEE Conference on
Computer Communications Workshops (INFOCOM WKSHPS).
IEEE,
2018, pp. 312–317.
[11] S. S. Mousavi, M. Schukat, and E. Howley, “Deep reinforcement learn-
ing: an overview,” in Proceedings of SAI Intelligent Systems Conference.
Springer, 2016, pp. 426–440.
[12] A. Shamsoshoara, M. Khaledi, F. Afghah, A. Razi, and J. Ashdown,
“Distributed cooperative spectrum sharing in uav networks using multi-
agent reinforcement learning,” in 2019 16th IEEE Annual Consumer
Communications & Networking Conference (CCNC).
IEEE, 2019, pp.
1–6.
[13] A. Shamsoshoara, M. Khaledi, F. Afghah, A. Razi, J. Ashdown, and
K. Turck, “A solution for dynamic spectrum management in mission-
critical uav networks,” arXiv preprint arXiv:1904.07380, 2019.
[14] S. Mousavi, M. Schukat, E. Howley, A. Borji, and N. Mozayani,
“Learning to predict where to look in interactive environments using
deep recurrent q-learning,” arXiv preprint arXiv:1612.05753, 2016.
[15] S. S. Mousavi, M. Schukat, E. Howley, and P. Mannion, “Applying
q (λ)-learning in deep reinforcement learning to play atari games,” in
AAMAS Adaptive Learning Agents (ALA) Workshop, 2017.
[16] A. Shamsoshoara and Y. Darmani, “Enhanced multi-route ad hoc on-
demand distance vector routing,” in 2015 23rd Iranian Conference on
Electrical Engineering.
IEEE, 2015, pp. 578–583.
[17] A. Shamsoshoara, A. Korenda, F. Afghah, and S. Zeadally, “A survey
on hardware-based security mechanisms for internet of things,” arXiv
preprint arXiv:1907.12525, 2019.
[18] A. Fotoohinasab, E. Fatemizadeh, H. Pezeshk, and M. Sadeghi, “De-
noising of genetic switches based on parrondos paradox,” Physica A:
Statistical Mechanics and its Applications, vol. 493, pp. 410–420, 2018.
[19] C. H. Antink, S. Leonhardt, and M. Walter, “Reducing false alarms
in the icu by quantifying self-similarity of multimodal biosignals,”
Physiological measurement, vol. 37, no. 8, p. 1233, 2016.
[20] K. Gajowniczek, I. Grzegorczyk, and T. Zabkowski, “Reducing false
arrhythmia alarms using different methods of probability and class
assignment in random forest learning methods,” Sensors, vol. 19, no. 7,
p. 1588, 2019.
[21] E. P. Lehman, R. G. Krishnan, X. Zhao, R. G. Mark, and H. L. Li-wei,
“Representation learning approaches to detect false arrhythmia alarms


## Page 8


8
Table III: Comparison of performance of the proposed model against other algorithms on the PhysioNet challenge-2015 dataset.
Best Performance (%)
Method
Signal
# of samples
CV
SEN
SPE
PRE
F1 −score
AUC
ACC
Multi-modal method
All
220
10-fold CV
93.88
92.05
79.31
85.98
92.99
92.50
Zaeri-Amirani et al. [24]
All
220
10-fold CV
73
75
-
-
81
77
Afghah et al. [37]
All
220
10-fold CV
80
71
-
-
74.32
77.6
Single-modal method
ECG II
220
10-fold CV
73.33
87.74
63.46
68.04
80.53
84.50
Single-modal method
ABP
220
10-fold CV
78.72
65.35
41.11
54
72.04
68.50
Single-modal method
PPG
220
10-fold CV
87.50
63.15
42.96
57.53
75.32
69
All: ECG II, ABP, PPG; CV: Cross Validation
Table IV: Comparison of performance of the proposed model against other algorithms for alarm type of Ventricular Tachycardia
arrhythmia on the PhysioNet challenge-2015 dataset.
Best Performance (%)
Method
Signal
# of samples
CV
SEN
SPE
PRE
F1 −score
AUC
ACC
Multi-modal method
All
124/220
10-fold CV
93.75
95.49
85.41
86.67
94.61
95
Afghah et al. [37]
All
124/220
10-fold CV
86
-
73
-
-
85.48
Single-modal method
ECG II
124/220
10-fold CV
93.75
93.92
79.16
84.58
93.84
93.75
Single-modal method
ABP
124/220
10-fold CV
81.25
75.68
41.95
69.76
78.46
76.67
Single-modal method
PPG
124/220
10-fold CV
100
50
33.33
50
75
60
All: ECG II, ABP, PPG; CV: Cross Validation
Table V: Comparison of performance of the proposed model against other algorithms for all alarm types on the PhysioNet
challenge-2015 dataset.
ASY
EBR
ETC
VTA
VFB
Method
Signal
CV
TPR
TNR
AUC
TPR
TNR
AUC
TPR
TNR
AUC
TPR
TNR
AUC
TPR
TNR
AUC
Single-modal method
ECG II
5-fold
96.67
82.16
89.41
97.78
94.85
96.31
100
100
100
90.71
88.30
89.51
100
97.22
98.61
Lehman et al. [21]
ECG II*
10-fold
-
-
-
-
-
-
-
-
-
-
-
87
-
-
-
Li et al. [35]
ECG II
0.67/0.33
-
-
-
-
-
-
-
-
-
76.70
59.80
-
-
-
-
Lehman et al. [21]
ECG II/V*
10-fold
-
-
-
-
-
-
-
-
-
89
86
91
-
-
-
Ansari et al. [36]
All
5-fold
84.97
89.21
-
90.49
90.05
-
96.55
97.80
-
96.63
95.47
-
92.40
61.64
-
Gajowniczek et al. [20]
All
10-fold
85
90
95
84.5
91
93.3
99.2
77.8
99
67.8
88.9
87
83.3
94.2
95
All: ECG II, ECG V, ABP, and PPG; CV: Cross Validation; *: 1250 records (750 train, 500 hidden test of Physionet), in which 562 records contains VTA alarms
Table VI: Performance of the proposed model for all alarm
types on the PhysioNet challenge-2015 dataset, considering
just a single lead (ECG II).
Best Performance (%)
Alarm
SEN
SPE
PRE
F1-score
AUC
ACC
Score
ASY
96.67
82.17
57.33
69.21
89.41
84.20
81.20
EBR
97.78
94.85
93.76
95.56
96.31
96
92.35
ETC
100
100
100
100
100
100
100
VTA
90.71
88.30
74.88
81.41
89.51
88.89
81.55
VFB
100
97.22
87.50
91.67
98.61
97.50
97.50
Score: PhysioNet/CinC Challenge 2015 Score
from ecg dynamics,” in Machine Learning for Healthcare Conference,
2018, pp. 571–586.
[22] V. Kalidas and L. S. Tamil, “Enhancing accuracy of arrhythmia clas-
siﬁcation by combining logical and machine learning techniques,” in
Computing in Cardiology Conference (CinC), 2015.
IEEE, 2015, pp.
733–736.
[23] F. Afghah, A. Razi, and K. Najarian, “A shapley value solution to game
theoretic-based feature reduction in false alarm detection,” arXiv preprint
arXiv:1512.01680, 2015.
[24] M. Zaeri-Amirani, F. Afghah, and S. Mousavi, “A feature selection
method based on shapley value to false alarm reduction in icus a genetic-
algorithm approach,” in 2018 40th Annual International Conference of
the IEEE Engineering in Medicine and Biology Society (EMBC), July
2018, pp. 319–323.
[25] U. R. Acharya, S. L. Fernandes, J. E. WeiKoh, E. J. Ciaccio, M. K. M.
Fabell, U. J. Tanik, V. Rajinikanth, and C. H. Yeong, “Automated
detection of alzheimers disease using brain mri images–a study with
various feature extraction techniques,” Journal of Medical Systems,
vol. 43, no. 9, p. 302, 2019.
[26] S. Mousavi and F. Afghah, “Inter-and intra-patient ecg heartbeat classi-
ﬁcation for arrhythmia detection: a sequence to sequence deep learning
approach,” in ICASSP 2019-2019 IEEE International Conference on
Acoustics, Speech and Signal Processing (ICASSP).
IEEE, 2019, pp.
1308–1312.
[27] S. Mousavi and F. Afghah, “ECGNET: Learning where to attend for
detection of atrial ﬁbrillation with deep visual attention,” arXiv preprint
arXiv:1812.07422, 2018.
[28] O. M. Hooman, M. M. Al-Rifaie, and M. A. Nicolaou, “Deep neu-
roevolution: Training deep neural networks for false alarm detection
in intensive care units,” in 2018 26th European Signal Processing
Conference (EUSIPCO).
IEEE, 2018, pp. 1157–1161.
[29] I. Mozos and A. Caraba, “Electrocardiographic predictors of cardiovas-
cular mortality,” Disease markers, vol. 2015, 2015.
[30] S. A. Abdelghani, T. M. Rosenthal, and D. P. Morin, “Surface electrocar-
diogram predictors of sudden cardiac arrest,” Ochsner Journal, vol. 16,
no. 3, pp. 280–289, 2016.
[31] D. Lai, Y. Zhang, X. Zhang, Y. Su, and M. B. B. Heyat, “An automated
strategy for early risk identiﬁcation of sudden cardiac death by using
machine learning approach on measurable arrhythmic risk markers,”
IEEE Access, vol. 7, pp. 94 701–94 716, 2019.
[32] S.
Mousavi,
F.
Afghah,
and
U.
R.
Acharya,
“SleepEEGNet:
Automated
sleep
stage
scoring
with
sequence
to
sequence


## Page 9


9
deep
learning
approach,”
PLoS
ONE
14(5):
e0216456.
https://doi.org/10.1371/journal.pone.0216456, 2019.
[33] S. Wang, W. Liu, J. Wu, L. Cao, Q. Meng, and P. J. Kennedy, “Training
deep neural networks on imbalanced data sets,” in Neural Networks
(IJCNN), 2016 International Joint Conference on.
IEEE, 2016, pp.
4368–4374.
[34] G. D. Clifford, I. Silva, B. Moody, Q. Li, D. Kella, A. Shahin,
T. Kooistra, D. Perry, and R. G. Mark, “The physionet/computing in
cardiology challenge 2015: reducing false arrhythmia alarms in the icu,”
in 2015 Computing in Cardiology Conference (CinC).
IEEE, 2015, pp.
273–276.
[35] A. S. Li, A. E. Johnson, and R. G. Mark, “False arrhythmia alarm
reduction in the intensive care unit,” arXiv preprint arXiv:1709.03562,
2017.
[36] S. Ansari, A. Belle, H. Ghanbari, M. Salamango, and K. Najarian,
“Suppression of false arrhythmia alarms in the icu: a machine learning
approach,” Physiological measurement, vol. 37, no. 8, p. 1186, 2016.
[37] F. Afghah, A. Razi, R. Soroushmehr, H. Ghanbari, and K. Najarian,
“Game theoretic approach for systematic feature selection; application
in false alarm detection in intensive care units,” Entropy, vol. 20, no. 3,
p. 190, 2018.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
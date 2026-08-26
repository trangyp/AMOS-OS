---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1809.08443v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1809.08443v1_Automated_Classification_of_Sleep_Stages_and_EEG_Artifacts_in_Mice_with_Deep_Lea

> Source: 1809.08443v1_Automated_Classification_of_Sleep_Stages_and_EEG_Artifacts_in_Mice_with_Deep_Lea.pdf

> Pages: 7

---


## Page 1


1
Automated Classiﬁcation of Sleep Stages and EEG
Artifacts in Mice with Deep Learning
Justus T. C. Schwabedal, Daniel Sippel, Moritz D. Brandt, Stephan Bialonski
Abstract—Sleep scoring is a necessary and time-consuming
task in sleep studies. In animal models (such as mice) or in
humans, automating this tedious process promises to facilitate
long-term studies and to promote sleep biology as a data-driven
ﬁeld. We introduce a deep neural network model that is able
to predict different states of consciousness (Wake, Non-REM,
REM) in mice from EEG and EMG recordings with excellent
scoring results for out-of-sample data. Predictions are made on
epochs of 4 seconds length, and epochs are classiﬁed as artifact-
free or not. The model architecture draws on recent advances in
deep learning and in convolutional neural networks research.
In contrast to previous approaches towards automated sleep
scoring, our model does not rely on manually deﬁned features of
the data but learns predictive features automatically. We expect
deep learning models like ours to become widely applied in
different ﬁelds, automating many repetitive cognitive tasks that
were previously difﬁcult to tackle.
Index Terms—deep learning, sleep scoring
I. INTRODUCTION
Humans and other animals spend much of their time in
sleep. Despite its importance, many aspects of sleep are not
yet fully understood. In order to uncover mechanisms and
functions of sleep, scientists study humans and animal models.
Rodents (mice and rats) are often studied as these are well
established mammal models which show sleep characteristics
that are comparable to human sleep (i.e., NREM and REM
sleep). An important step in many studies is the identiﬁcation
of different states of consciousness from different recording
modalities such as electroencephalography (EEG) and elec-
tromyography (EMG). For many years, sleep scoring has been
a manual and time consuming process. The time required
for manual sleep scoring depends on various factors (i.e.,
data quality, artifacts, sleep fragmentation). While experienced
personnel needs up to 3 hours to thoroughly score 24 hours
of EEG/EMG recordings, untrained staff may spend up to 6
hours to score the same amount of data. This tedious process
poses not only a challenge to human scorers who often face
the problem of decreasing scoring accurracies as concentration
fades during such monotonous tasks. It also poses a challenge
for studies to achieve a suitable statistics (with a reasonable
number of mice scored) and to establish long-term studies in
Justus T. C. Schwabedal, Department of Biomedical Informatics, Emory
University, GA, USA — Daniel Sippel, Department of Psychiatry and
Psychotherapy, University Hospital T¨ubingen, T¨ubingen, Germany; Institute
of Medical Psychology and Behavioral Neurobiology, University of T¨ubingen,
T¨ubingen, Germany — Moritz D. Brandt, Department of Neurology, Technis-
che Universit¨at Dresden, Dresden, Germany; German Center for Neurodegen-
erative Diseases (DZNE) Dresden, Dresden, Germany — Stephan Bialonski,
FH Aachen University of Applied Sciences, Aachen, Germany.
Manuscript received XXX, revised XXX
which potentially several days and weeks of sleep recordings
need to be scored.
Early approaches towards automating the sleep scoring
process date back to the late 1960s [1]. Since then, the
ﬁeld has made rapid progress over the years (see [2] for a
historic overview), yielding methods that aim at interactively
supporting human scorers or even fully automating the scoring
process. Most methods rely on hand-crafted features (feature
engineering), many of which are derived from power spectra
of the EEG (see, e.g., Refs. [3]–[5]) where researchers focused
on classical frequency bands in rodents (delta, theta, and
sigma bands). Other approaches include features derived from
bispectra [6], or wavelet coefﬁcients (see, e.g., Ref. [7]). While
feature engineering is often the only feasible way to create
predictive models in cases in which data is not abundant, this
process relies on expert knowledge and may not yield features
that are optimal for the sleep scoring task at hand. However,
if data is abundant, feature engineering can in many cases
be replaced by automated feature learning, which can lead to
better prediction results as has been shown in the context of
deep learning in various disciplines in recent years [8].
We introduce a deep neural network model that is trained
end-to-end to predict different states of consciousness in mice
from EEG and EMG recordings (see Fig. 1). Instead of
engineering features, features are learnt automatically by the
model. The model architecture (see Fig. 2) and the training of
the model draws on recent advances in convolutional neural
network research which has demonstrated the usefulness of
learnt features for time sequenced data in a number of ap-
plications (e.g., generative modeling of audio data [9], ma-
chine translation [10]). Our model achieves excellent scoring
results for out-of-sample data and in artifact-free conditions.
Furthermore, we demonstrate that increasing the number of
recording channels can partially counteract the decrease of
scoring performance for artifact-contaminated data.
II. METHODS
A. Data
The data was recorded from 22 mice (age 10-11 weeks,
male, C57BL/6 strain). All mice were kept at the animal
facility of the Center for Regenerative Therapies of the Tech-
nische Universit¨at Dresden, Germany. All applicable local
and federal regulations of animal welfare in research were
followed. The experiments were approved by the responsible
authority, Landesdirektion Sachsen, Germany. The mice were
chronically implanted with a synchronous recording system
of 1 EMG and 2 EEG electrodes (8201, Pinnacle Technology
arXiv:1809.08443v1  [q-bio.QM]  22 Sep 2018


## Page 2


2
50
0
50
EEG1 ( V)
100
0
100
EEG2 ( V)
100
0
100
EMG ( V)
REM
REM
REM
Wake
Wake
Wake
nREM
nREM
nREM
0
1
2
3
4
5
6
7
8
Epoch Number
10
5
10
1
100
Probability
Wake
REM
nREM
artif
Fig. 1.
Automated sleep scoring. The model predicts from up to three input channels (EEG, top two panels; EMG, third panel) the probabilities of an
epoch to belong to different sleep classes (third panel) and the probability of the input data to contain artifacts. The sleep class associated with the maximum
probability is outputted as the prediction of the model. Each epoch has a duration of 4 s; ground truth labels as determined by DS are shown in green letters
in the third panel.
Inc., Lawrence, KS) 10-14 days before the ﬁrst recording.
Four stainless steel screws sitting on top of the cortex at
the following coordinates (relative to bregma) were used
as EEG electrodes: anterior-posterior (AP): +2 mm, medial-
lateral (ML): +1.5 mm (EEG2) / ML: -1.5 mm (ground) and
AP: -4 mm, ML: +1.5 mm (EEG1) / ML: -1.5 mm (reference).
With this setup, we sampled the electrical activity of the frontal
(EEG2) and the parieto-occipital lobes (EEG1), respectively.
Two ﬂexible stainless steel wires were inserted into the neck
muscles to measure the EMG signal. All electroencephalo-
graphic (EEG) and electromyographic (EMG) time series were
sampled at 400 Hz. 82 recordings, each lasting 24 hours and
containing all three channels, were available for the creation
of training, validation and test sets.
All recordings were divided into non-overlapping consec-
utive epochs of 4 seconds. One of the authors (DS) scored
each epoch manually as sleep stage “Non REM”, “REM”
or “Wake”. In addition, each epoch was scored according to
whether recording artifacts were present (artifact-contaminated
epoch) or not (artifact-free epoch). Manual scoring was per-
formed using our own customized software edfView [11] that
was conﬁgured to show 5 consecutive epochs of all three
channels, and to allow our scoring specialist to assign one of
the labels to the middle epoch: The Wake state is characterized
by high EMG activity (active locomotion, higher muscle tone
even when resting) and a mixed frequency EEG signal (with-
out a clear peak at a certain frequency in the power spectrum).
Non REM sleep shows lower EMG activity compared to the
Wake state as well as a power spectrum peak in the delta band
(0.5–4 Hz). REM sleep is usually characterized by very low
EMG activity (with only seldom muscle twiches and a clear
power spectrum peak in the theta band (at 7–8 Hz)).
Time series were low-pass ﬁltered with a 4th-order But-
terworth ﬁlter (cutoff frequency: 25.6 Hz) using a forward-
backward scheme to ensure zero-phase ﬁltering [12]. The
ﬁltered time series were downsampled from 400 Hz to 64 Hz
by linearly interpolating between neighboring sampling points.
Each of the 82 recordings was divided into different parts, and
TABLE I
CHARACTERISTICS OF THE DATA SET.
training set
test set
validation set
all data
recording days
65
4
13
82
number of epochs
1,407,706
84,694
275,599
1,767,999
percentage
79.6 %
4.8 %
15.6 %
100 %
segments (epochs) of these parts were assigned to the training,
test, and validation set, respectively (cf. Tab. I). We made sure
that data of the test set came from different mice.
Table II summarizes the number of labeled epochs for
the whole dataset. The most frequent class was “Wake”
(57%), followed by “Non REM” (33%) and “REM” (5.9%)
sleep. Artifacts were most pronounced during Wake (3.6%)
while they were barely present during REM sleep (0.04%).
Such large class imbalances are known to negatively affect
training results. The large variability in the frequencies of
class members can adversely affect the model ﬁtting process.
We accounted for the class imbalance by resampling with
replacement and used the resulting rebalanced training set for
training our models. Indeed, we observed better ﬁtting results
with this rebalanced training set, and the sampling probabilities
(class percentages) used to produce the rebalanced training set
are reported in table II.
B. Machine-Learning Model architecture
To closely imitate the scoring procedure (cf. section II-A),
our learning model uses information of 5 consecutive time
series epochs in order to classify the middle epoch to belong to
one of three distinct sleep state classes and to decide whether
the middle epoch contains artifacts or not. More formally,
our learning model is a function F that maps 5 consecutive
epochs of multivariate time series ⃗xi, i ∈{1, . . . , 5}, to the
vector ⃗pstate and to a scalar partifact. Values of partifact larger
than a threshold value of 0.5 indicate the middle epoch ⃗x3
to contain artifacts. The entries of ⃗pstate are interpreted as
probabilities of the middle epoch ⃗x3 to reﬂect wakefulness


## Page 3


3
TABLE II
STATISTICS OF LABELED EPOCHS OF THE WHOLE DATASET (“all data”),
OF THE TRAINING SET AND THE REBALANCED TRAINING SET (SEE TEXT).
NR: “NON REM SLEEP”, R: “REM SLEEP”, W: “WAKEFULNESS”. (A):
ARTIFACT-CONTAMINATED. PERC: PERCENTAGE, (REB.) TRAIN. SET:
(REBALANCED) TRAINING SET, # EPOCHS: NUMBER OF EPOCHS.
label
NR
NR (A)
R
R (A)
W
W (A)
all data
# epochs
586,832
1,973 103,546
672 1,010,412
64,564
perc.
33.19 %
0.11 %
5.86 %
0.04 %
57.15 %
3.65 %
train. set
# epochs
465,134
1,290
82,646
429
807,419
50,788
perc.
33.04 %
0.09 %
5.87 %
0.03 %
57.36 %
3.61 %
reb. train. set
# epochs
305,061 165,145 188,307 164,293
406,125 178,775
perc.
21.67 % 11.73 % 13.38 % 11.67 %
28.85 % 12.70 %
(Wake), REM, or non-REM sleep. The model identiﬁes the
maximum component of ⃗pstate and outputs its associated class,
thereby producing a label of the most probable sleep state.
The model architecture (cf. ﬁg. 2) is inspired by recent
advances in deep learning [9], [13] and consists of two
parts: (1) A feature extractor successively downsamples and
nonlinearly transforms multivariate time series to create a set
of features that are used by (2) the classiﬁer to classify the
time series. The feature extractor consists of 8 convolutional
layers without padding where each layer has 64 kernels of
size 5. Kernels (also called ﬁlters) are shifted with a stride of
1 in layers 1, 3, 5, and 7. The other convolutional layers use a
stride of 2 and thus successively downsample the nonlinearly
transformed data. We used Rectiﬁed Linear Units (ReLUs) as
nonlinearities after each convolutional layer since ReLUs were
observed to show superior training behavior in previous studies
[14], [15]. To stabilize training, we reduced internal covariate
shift by applying Batch Normalization (BN) [16] after the
nonlinearities of each convolutional layer1. In addition, we
also applied Batch Normalization to the input data (i.e.,
before the ﬁrst convolutional layer). The batch normalized 64
feature maps after the last convolutional layer are ﬂattened
and concatenated to form a single feature vector which is the
output of the feature extractor.
The classiﬁer consists of two fully connected (fc) layers,
fc1 and fc2. fc1 is composed of 80 neurons with ReLU
nonlinearities and processes the feature vector produced by
the feature extractor. fc2 consists of 4 neurons which process
the output activities of fc1. Instead of ReLU nonlinearities,
we apply a softmax on the output of the ﬁrst three neurons,
yielding the probabilities pj, j ∈{1, . . . , 3} of the input epoch
to belong to the three classes. The output of the fourth neuron
is transformed into a value pa by a sigmoid function, which
maps values into the interval [0, 1]. We interpret the ﬁrst three
components of the resulting output vector as class probabilities
while the last component shall indicate whether the input
epoch contains artifacts (1) or not (0). Since fully connected
layers contain many free parameters that make overﬁtting
more likely, we employed dropout regularization (dropout
1We note that in Ref.
[16] Batch Normalization (BN) was carried out
before the nonlinearities of a layer. However, we observed our model to ﬁt
our data well when applying BN after the nonlinearities.
probability: 0.2) [17] on the weights connecting the feature
vector to the neurons of fc1 and on the weights connecting
the output of fc1 to the neurons of fc2.
We implement the training objective by a loss function L =
L1 + L2 that becomes small (L1) if the classiﬁer assigns a
large probability to the correct class and becomes small (L2)
if the classiﬁer correctly indicates whether the input contains
artifacts or not. The loss is computed over a minibatch of the
input. Let ck ∈{1, 2, 3} denote the correct class index for
the middle input epoch ⃗xk and let pk,ck be the predicted class
probability of ⃗xk for the correct class ck. We deﬁne L1 as a
negative log-likelihood,
L1 = −1
Nb
Nb
X
k=1
log(pk,ck)
(1)
where Nb is the minibatch size. The second term L2 is deﬁned
as the binary cross entropy between the predicted value pk,a
for an input ⃗xk and the true label tk,a ∈{0, 1} indicating
whether an artifact is present (1) or not (0),
L2 = 1
Nb
Nb
X
k=1
(−tk,a log pk,a + (1 −tk,a) log (1 −pk,a)) .
(2)
The model is differentiable and can be trained via gradient
descent.
C. Training
The model was trained by RMSprop (Root Mean Square
Propagation), a variant of stochastic gradient descent where
the learning rate is adapted separately for each free parameter
(weight) of the model [18]. Let w(t) denote a weight and
let ∆(t) = ∂L
∂w denote the gradient of the loss function with
respect to the weight obtained for the minibatch at step t of
the training. We update the weight by
w(t + 1) = w(t) −
η
p
R(t)
∆(t)
(3)
where η is the learning rate. R is a running mean of the
squared magnitudes of recent gradients for that weight,
R(t + 1) = αR(t) + (1 −α)∆(t)2,
(4)
where we set the smoothing factor α to α = 0.99. After the
gradients for all weights are determined, we checked whether
a gradient exceeded the value 0.1. In such a case, we rescaled
all gradients such that the largest value was 0.1 (maximum-
norm normalization of gradients).
We adjusted the learning rate according to the following
learning protocol: during model exploration (section III-A),
the learning rate η was linearly increased from 0 to η∗=
0.00128Nb (warm-up period) in the ﬁrst 5 training cycles,
where Nb denotes the size of the minibatches. This linear
scaling of the learning rate with minibatch size combined with
a warm-up period was observed to lead to better generaliza-
tion properties of models when trained with large minibatch
sizes [19]. A single training cycle was completed when all
minibatches of the training set were used once for a stochastic
gradient descent step. During the following 5 training cycles,


## Page 4


4
n
5
64 kernels
size 5 x n, stride 1
n batch normalized (BN) 
input time series
64
64 kernels
size 5 x 64, stride 2
Layer 1
Layer 2
Layer 3-8
ReLu + BN
Flatten
80
4
Layer 9
Layer 10
fully-connected
fully-connected
output
input
feature extractor
classifier
Fig. 2. Deep neuronal network model that predicts from time series input the corresponding sleep stage class. The feature extractor consists of a hierarchy
of 8 convolutional layers and produces a feature vector. The classiﬁer is composed of 2 fully connected layers and transforms the feature vector to class
probabilities as well as a probability that artifacts are present in the input time series. Features are learnt automatically during training.
the learning rate was linearly decreased again to 0 (cool-down
period). For the training of the ﬁnal models (section III-B), we
linearly increased the learning rate from 0 to η∗in the ﬁrst 5
training cycles. During the subsequent 10 training cycles, the
learning rate was η∗, while during the next 5 training cycles
we linearly decreased η again from η∗to 0. All trainings were
carried out with a minibatch size of Nb = 256, and we did not
observe moderate changes in minibatch sizes to affect training
outcomes.
D. Evaluation.
To evaluate the prediction performance of our model, we
employed classical techniques to characterize the quality of
classiﬁcations in binary as well as in multiclass classiﬁcation
settings.
a) Artifact classiﬁcation: We used the F1 score (also
known as F measure, [20]) to quantify the prediction perfor-
mance of our model to distinguish between artifact-free and
artifact-contaminated epochs (binary classiﬁcation) in a given
sleep stage. The F1 score is a summary statistics which takes
on values between 0 and 1, where larger values indicate better
predictive performance. It is deﬁned as the harmonic mean of
precision (pprecision) and recall (precall),
F1 =

1
pprecision
+
1
precall
−1
,
(5)
where precision is also known as positive predictive value.
In a binary classiﬁcation setting, the precision is the number
of epochs for which a class was correctly predicted by the
model (number of true positives) divided by the total number
of epochs that were predicted by the model to belong to that
class,
pprecision =
number of true positives
number of true and false positives .
(6)
TABLE III
MODEL EXPLORATION. ¯F1 (TOP TWO ROWS) AND F1 (LAST THREE
ROWS) SCORES OBTAINED ON TRAINING AND VALIDATION SETS. L:
LAYERS, K: KERNELS. LIGHT GREY: BEST ¯F1 SCORES OBTAINED ON THE
VALIDATION SET; DARK GRAY: SLIGHT CASES OF OVERFITTING.
prediction
target
96 k
4 l
condition
set
4 l
8 l
10 l
32 k
64 k
96 k
sleep
stages
no artifact
training
0.95
0.98
0.98
0.92
0.94
0.95
validation
0.93
0.95
0.95
0.91
0.93
0.93
artifact
training
0.98
1.00
1.00
0.93
0.97
0.98
validation
0.88
0.85
0.82
0.85
0.88
0.88
artifact
yes/no
Non-REM
training
0.94
0.94
0.96
0.70
0.88
0.94
validation
0.60
0.80
0.81
0.48
0.56
0.81
REM
training
1.00
1.00
1.00
0.84
0.97
0.99
validation
0.60
0.76
0.76
0.53
0.63
0.58
Wake
training
0.89
0.95
0.96
0.82
0.87
0.89
validation
0.85
0.86
0.87
0.81
0.83
0.84
The recall, also known as sensitivity, is the number of epochs
for which a class was correctly predicted by the model divided
by the total number of epochs of that class,
precall =
number of true positives
number of true positives and false negatives.
(7)
Both, precision and recall, take on values between 0 and 1.
b) Sleep-stage classiﬁcation: We quantiﬁed the predic-
tion performance of our model to distinguish between different
sleep stages (multiclass classiﬁcation) by calculating averages
of F1 scores. More precisely, we converted the multiclass
classiﬁcation problem into multiple binary classiﬁcations: We
determined the F1 score for each class c (sleep stage) sepa-
rately (F c
1) where precision and recall were calculated with
respect to the distinction between class c and everything else
(¬c). The resulting F1 scores were then averaged to arrive at
a ﬁnal score,
¯F1 = 1
Nc
Nc
X
c=1
F c
1,
(8)


## Page 5


5
where Nc denotes the number of classes (Nc = 3 sleep stages).
The ¯F1 score varies between 0 and 1 where large values
indicate better predictive performance. Next to the ¯F1 score,
we also determined confusion matrices in order to investigate
whether our models systematically confused one class with
another.
III. RESULTS
We investigated our learning model with respect to its
ability (i) to accurately predict sleep stages and (ii) to detect
artifacts. In a ﬁrst series of experiments, we investigated to
what extent changes of our basic model architecture (as shown
in ﬁgure 2) affected prediction performance. In this model
exploration step, we evaluated the performance of different
model architectures on the validation set (see section III-A).
Based on these results, we chose a ﬁnal model architecture.
In a second series of experiments (see section III-B), we
addressed the question whether the predictive performance
changes when varying the number of input channels presented
to the model. Here we evaluated the performance of our model
on the test set.
A. Model exploration
We varied our model architecture (cf. ﬁgure 2) and investi-
gated which of the resulting architectures yielded the best pre-
diction performance. We varied (i) the number of convolutional
layers and (ii) the number of kernels per convolutional layer.
The input for all models consisted of three input time series
(EEG1, EEG2, EMG) that were simultaneously recorded, and
each model was trained as described in section II-C.
When increasing the number of layers or the number of
kernels, we increase the complexity of the model and thus its
ability to ﬁt the training data. Indeed, we observed F1 scores
obtained on the training set (see table III) to increase with
an increasing number of layers and number of kernels per
layer. Best ¯F1 scores were obtained for the architecture with
largest model complexity (10 convolutional layers with 96
kernels each) which reach 0.98 and 1.00 for sleep stage clas-
siﬁcation from artifact-free and artifact-contaminated epochs,
respectively. For the same model architecture in the artifact-
free condition, our model generalized well to unseen epochs
as indicated by an ¯F1 score of 0.95 for the validation set. Due
to this high value, we expect our model to very reliably predict
sleep stages on unseen and artifact-free epochs.
Our models were able to ﬁt artifact-contaminated time series
in the training set, reaching ¯F1 scores larger than 0.92 for all
model architectures (cf. table III). However, as compared to
the artifact-free case, our models were not able to generalize
as well, which was indicated by lower ¯F1 scores between
0.82 and 0.88 on the validation set. This phenomenon may
be related to class imbalances of the training set, where
artifact-free epochs were much more frequent than artifact-
contaminated epochs (cf. table II). We observed the same
phenomenon, namely less generalization performance, for the
prediction of artifacts under the condition of non-REM, REM,
and Wake stages (cf. table III, last three rows).
TABLE IV
MODEL PERFORMANCE. ¯F1 (TOP TWO ROWS) AND F1 (LAST THREE
ROWS); IC: INPUT CHANNELS; GREY CELLS: LARGEST ¯F1 SCORES FOR
PREDICTING SLEEP STAGES IN ARTIFACT-FREE AND
ARTIFACT-CONTAMINATED EPOCHS IN THE TEST SET.1
prediction
target
96 kernels, 8 layers
condition
set
1 ic
2 ic
3 ic
sleep
stages
no artifact
training
0.95
0.97
0.98
testing
0.93
0.95
0.96
validation
0.92
0.94
0.95
artifact
training
1.00
1.00
1.00
testing
0.82
0.92
0.93
validation
0.77
0.85
0.84
artifact
yes/no
Non-REM
training
0.87
0.91
0.95
testing
0.12
0.15
0.17
validation
0.68
0.68
0.81
REM
training
0.99
1.00
1.00
testing
0.40
0.36
0.56
validation
0.68
0.65
0.73
Wake
training
0.92
0.94
0.96
testing
0.74
0.75
0.83
validation
0.79
0.80
0.87
1 Small differences between values reported in table III and in table IV
are due to a retraining of the models and the stochastic nature of the
optimization algorithm (stochastic gradient descent).
We noticed tendencies of slight overﬁtting (decreasing
¯F1 scores for increasing model complexity for the validation
set) when predicting sleep stages from artifact-contaminated
epochs and increasing the number of layers (see dark gray cells
in table III). This tendency was also observed for the prediction
of artifacts from epochs recorded during REM sleep and
increasing the number of kernels. While we do not consider
these cases of overﬁtting to be severe, we chose our ﬁnal
model architecture, 8 layers and 96 kernels, as a compromise
between high ¯F1 scores for sleep stage prediction (see light
gray cells in table III) and reduced overﬁtting.
B. Model performance
We studied the predictive performance of the ﬁnal model
and whether and how it changed when predictions were
based on a different number of simultaneously recorded time
series (input channels). This question becomes important when
experimental restrictions and setups do not allow for all three
channels to be recorded. A reliable prediction of sleep stages
and artifacts based on few channels is highly desirable in such
cases.
We varied the number of input channels from one channel
(“EEG2”), to two (“EEG2, EMG”), and three (“EEG1, EEG2,
EMG”) and trained one ﬁnal model for each of the three cases
using the ﬁnal architecture (i.e., 8 convolutional layers with 96
kernels each) as determined in the previous section. ¯F1 scores
for sleep stage prediction and F1 scores for artifact prediction
obtained for all datasets are shown in table IV. We observed
¯F1 scores and F1 scores obtained on the training set to increase
with increasing the number of input channels, indicating our
models to better predict sleep stages or artifacts the more input
channels were available. This tendency was also observed for
the test set and, as such, for epochs not used for training.
We obtained best ¯F1 scores for sleep stage prediction of 0.96
and 0.93 (grey cells in table IV) for the three channels con-
dition and for artifact-free and artifact-contaminated epochs,


## Page 6


6
Wake
REM
Non REM
Wake
REM
Non REM
True label
97.1%
0.5%
2.4%
1.8%
95.4%
2.8%
2.6%
0.9%
96.5%
Wake
REM
Non REM
Wake
REM
Non REM
True label
99.8%
0.0%
0.2%
5.8%
85.5%
8.7%
3.4%
1.7%
94.9%
Wake
REM
Non REM
Wake
REM
Non REM
96.6%
0.7%
2.8%
1.4%
96.2%
2.4%
2.1%
1.1%
96.8%
Wake
REM
Non REM
Predicted label
Wake
REM
Non REM
99.6%
0.1%
0.3%
1.4%
94.2%
4.3%
5.1%
6.8%
88.1%
Wake
REM
Non REM
Wake
REM
Non REM
94.6%
1.0%
4.4%
6.7%
91.6%
1.7%
4.4%
0.9%
94.7%
Wake
REM
Non REM
Wake
REM
Non REM
99.2%
0.2%
0.6%
27.5%
71.0%
1.4%
18.6%
6.8%
74.6%
(a)
(d)
(b)
(e)
(c)
(f)
Fig. 3. Confusion matrices for predicting sleep stages with the ﬁnal model (8 layers, 96 convolutional kernels) from artifact-free epochs (a–c) and artifact-
contaminated epochs (d–f) obtained on the test set. The ﬁnal model predicted sleep stages from three input time series (a, d), two input time series (b, e),
and one input time series (c, f). Matrices show the percentages of epochs that were correctly or incorrectly assigned to a sleep stage by our model.
respectively. More importantly, ¯F1 scores obtained on the test
set only slightly decreased when decreasing the number of
input channels. This indicates that our model is able to reliably
predict sleep stages even in experimental setups in which only
one channel is recorded.
F1 scores for predicting artifacts obtained low values on
the test set, e.g. 0.12 for one input channel and artifact
prediction in Non-REM epochs. We hypothesized that these
low values are related to the small size of the test set that
only encompasses 4.8 % of the labeled total data (cf. table I).
Since the test set is small, it has only few artifact-contaminated
epochs that are, moreover, assigned to different sleep stages.
Due to this difﬁcult statistical situation, we also reported
F1 scores (cf. table IV) obtained on the validation set (which
was larger than the test). Indeed, for the validation set and the
prediction of artifacts, we observed F1 scores which are close
to those reported in the previous section.
To offer insight into the prediction of individual labels,
we provide confusion matrices (ﬁgure 3) grouped for artifact-
contaminated and artifact-free epochs. For three input channels
and for artifact-free epochs, our ﬁnal model correctly classiﬁed
95.4 % of all “REM” epochs, 96.5 % of all “Non REM”
epochs, and 97.1 % of all “Wake” epochs. These numbers
only slightly decrease when reducing the number of input
channels, where we obtained 91.6 % as the lowest fraction of
correct predictions for artifact-free REM epochs (cf. ﬁgure 3).
As expected, prediction performance worsened for artifact-
contaminated epochs, where our model showed tendencies to
confuse “Non REM” or “REM” sleep stages with “Wake”.
This confusion was most pronounced when using a single
input channel (27.5 % of “REM” epochs were misclassiﬁed as
“Wake”). Increasing the number of input channels, however,
led to more robust predictions in artifact-contaminated epochs,
i.e. to a larger fraction of correctly predicted sleep stages.
IV. DISCUSSION
We introduced a deep neural network model that predicts
different states of consciousness in mice from EEG and EMG
recordings. Unlike many previous approaches towards auto-
mated sleep scoring, our model does not rely on manually de-
ﬁned features (such as power in frequency bands). Instead, our
model was trained end-to-end, thereby automatically learning
features of the data that were successfully used by the classiﬁer
of the model to distinguish between different sleep stages.
While many previous approaches predicted sleep stages on
epochs of 10 seconds length, our model allows for higher time
resolution and was able to make reliable predictions for epochs
of 4 seconds length. Such time resolutions are important to
capture short arousals and frequent changes in sleep states that
are typical in mice. High time resolutions particularly call for
approaches towards automatizing potentially time-consuming
manual scoring procedures.
We observed our model to achieve high speciﬁcity and sen-
sitivity (as indicated by large F1 scores) on artifact-free out-
of-sample (test) data. Decreasing the number of input channels
that were available for our model to infer sleep stages led only
to a slight decrease of prediction performance for artifact-free
data. This indicates that our model will yield good prediction
performance even for experiments in which constraints prohib-
ited to simultaneously capture multiple recording modalities.


## Page 7


7
For artifact-contaminated data, F1 scores became better when
the model based its predictions on more input channels. This
observation agreed with our expectation that recordings will
likely contain partially redundant information which renders
inferring sleep classes from artifact-contaminating epochs eas-
ier if other recording channels are available. Nevertheless, pre-
diction performance of our model was decreased for artifact-
contaminated data when compared to artifact-free data. We
speculate that the deteriorating effect of artifacts may also be
related to our training set that contained much more artifact-
free than artifact-contaminated epochs. We addressed these
class imbalances by sampling with replacement but expect
larger training sets to allow future models to even further
increase their prediction performance on artifact-contaminated
data.
In our study, we assessed prediction performance on test
data which was created from 22, male, 10-11 week old,
genetically identical C57BL/6 mice with a ﬁxed electrode
placement scheme. This restriction was due to experimental
constraints when creating the data set and limits our ability
to draw conclusions on prediction performance for other mice
strains and electrode placements. However, we are conﬁdent
that our deep learning model can be successfully employed to
predict sleep stages in other mice strains, models and/or other
implantation schemes after retraining. Such a retraining could
substantially proﬁt from transfer learning techniques [21]
which have the potential to signiﬁcally reduce the amount of
training data required. Next to the aforementioned restriction,
we also did not assess inter-rater and intrarater variability, i.e.
the scoring variability between different persons scoring our
data and the same person scoring the same data multiple times,
respectively. Such assessments become increasingly challeng-
ing as the amount of data to score increases. We speculate,
however, that intrarater variability sets an upper limit to the
maximum achievable sensitivity and speciﬁcity of our model.
Also, previous studies observed inter-rater reliability to be
never 100 % but rather in the range of 83–96 % [22]. Future
studies on model architectures like the one introduced here that
assess rater variability will be able to relate scoring accuracies
achieved by models to those achieved by human scorers.
We expect models like ours (a TensorFlow.js implemen-
tation is available online [23]) to facilitate or even enable
long-term studies in sleep research. Automating the time-
consuming process of sleep scoring will contribute to support
sleep research as a data-driven ﬁeld and will help researchers
and lab personnel to become more productive. This is in line
with what we expect to happen in the early 21st century: The
automation of cognitive repetitive tasks. In this context, deep
learning models and automated feature learning will play an
important role.
REFERENCES
[1] D. B. Drane, W. B. Martin, and S. S. Viglione, “Pattern recognition
applied to sleep state classiﬁcation,” Electroen. Clin. Neuro.., vol. 26, p.
238, 1969.
[2] G. A. Sunagawa, H. S´ei, S. Shimba, Y. Urade, and H. R. Ueda,
“FASTER: An unsupervised fully automated sleep staging method for
mice,” Genes to Cells, vol. 18, no. 6, pp. 502–518, 2013.
[3] J. H. Benington, S. K. Kodali, and H. C. Heller, “Scoring transitions to
REM sleep in rats based on the EEG phenomena of pre-REM sleep: an
improved analysis of sleep structure.” Sleep, pp. 28–36, 1994.
[4] S. Kohtoh, Y. Taguchi, N. Matsumoto, M. Wada, Z.-L. Huang,
and Y. Urade, “Algorithm for sleep scoring in experimental animals
based on fast fourier transform power spectrum analysis of the
electroencephalogram,” Sleep Biol. Rhythms, vol. 6, no. 3, pp. 163–171,
Jul 2008. [Online]. Available: https://doi.org/10.1111/j.1479-8425.2008.
00355.x
[5] J. Brankaˇck, V. I. Kukushka, A. L. Vyssotski, and A. Draguhn, “EEG
gamma frequency and sleep-wake scoring in mice: comparing two types
of supervised classiﬁers,” Brain Res., vol. 1322, pp. 59–71, 2010.
[6] V. Swarnkar and U. Abeyratne, “Objective measure of sleepiness and
sleep latency via bispectrum analysis of eeg,” Med. Biol. Eng. Comput.,
vol. 48, pp. 1203–1213, 2010.
[7] F. Ebrahimi, M. Mikaeili, E. Estrada, and H. Nazeran, “Automatic sleep
stage classiﬁcation based on EEG signals by using neural networks and
wavelet packet coefﬁcient,” Conf. Proc. IEEE Eng. Med. Biol. Soc., pp.
1151–1154, 2008.
[8] I. J. Goodfellow, Y. Bengio, and A. C. Courville, Deep Learning,
ser. Adaptive computation and machine learning.
MIT Press, 2016.
[Online]. Available: http://www.deeplearningbook.org/
[9] A. van den Oord, S. Dieleman, H. Zen, K. Simonyan, O. Vinyals,
A. Graves, N. Kalchbrenner, A. Senior, and K. Kavukcuoglu, “Wavenet:
A generative model for raw audio,” arXiv, p. 1609.03499, 2016.
[10] J. Gehring, M. Auli, D. Grangier, D. Yarats, and Y. N. Dauphin,
“Convolutional sequence to sequence learning,” in Proceedings of the
34th International Conference on Machine Learning, ICML 2017,
Sydney, NSW, Australia, 6-11 August 2017, 2017, pp. 1243–1252.
[Online]. Available: http://proceedings.mlr.press/v70/gehring17a.html
[11] J. Schwabedal, “edfView: A free, opensource, multiplatform, universal
viewer and toolbox,” https://github.com/jusjusjus/edfView, 2017.
[12] S. Smith, Digital Signal Processing. A Practical Guide for Engineers
and Scientists.
Oxford: Elsevier, 2002.
[13] Y. LeCun, Y. Bengio, and G. Hinton, “Deep learning,” Nature,
vol.
521,
pp.
436–444,
may
2015.
[Online].
Available:
https:
//doi.org/10.1038/nature14539
[14] V. Nair and G. E. Hinton, “Rectiﬁed linear units improve restricted
boltzmann
machines,”
in
Proceedings
of
the
27th
International
Conference on Machine Learning (ICML-10), 2010, Haifa, Israel,
2010, pp. 807–814. [Online]. Available: http://www.icml2010.org/
papers/432.pdf
[15] A.
Krizhevsky,
I.
Sutskever,
and
G.
E.
Hinton,
“Imagenet
classiﬁcation
with
deep
convolutional
neural
networks,”
in
Advances
in
Neural
Information
Processing
Systems
25,
2012,
pp.
1106–1114.
[Online].
Available:
http://papers.nips.cc/paper/
4824-imagenet-classiﬁcation-with-deep-convolutional-neural-networks
[16] S. Ioffe and C. Szegedy, “Batch normalization: Accelerating deep
network training by reducing internal covariate shift,” in Proceedings of
the 32nd International Conference on Machine Learning, ICML 2015,
Lille, France, 6-11 July 2015, 2015, pp. 448–456. [Online]. Available:
http://jmlr.org/proceedings/papers/v37/ioffe15.html
[17] N. Srivastava, G. E. Hinton, A. Krizhevsky, I. Sutskever,
and
R. Salakhutdinov, “Dropout: a simple way to prevent neural networks
from overﬁtting,” J. Mach. Learn. Res., vol. 15, no. 1, pp. 1929–1958,
2014. [Online]. Available: http://dl.acm.org/citation.cfm?id=2670313
[18] T. Tieleman and G. Hinton, “Lecture 6.5 - rmsprop: Divide the gradient
by a running average of its recent magnitude,” COURSERA: Neural
Networks for Machine Learning, 2012.
[19] P. Goyal, P. Doll´ar, R. B. Girshick, P. Noordhuis, L. Wesolowski,
A. Kyrola, A. Tulloch, Y. Jia, and K. He, “Accurate, large minibatch
SGD: Training ImageNet in 1 hour,” CoRR, vol. abs/1706.02677, 2017.
[Online]. Available: http://arxiv.org/abs/1706.02677
[20] C. D. Manning, P. Raghavan, and H. Sch¨utze, Introduction to informa-
tion retrieval.
New York: Cambridge University Press, 2008.
[21] S. J. Pan and Q. Yang, “A survey on transfer learning,” IEEE Trans.
Knowl. Data Eng., vol. 22, no. 10, pp. 1345–1359, 2010. [Online].
Available: https://doi.org/10.1109/TKDE.2009.191
[22] M. Kreuzer, S. Polta, J. Gapp, C. Schuler, E. F. Kochs, and T. Fenzl,
“Sleep scoring made easy—Semi-automated sleep analysis software and
manual rescoring tools for basic sleep research in mice,” MethodsX,
vol. 2, pp. 232–240, 2015.
[23] J. T. C. Schwabedal, “Tensorﬂow.js implementation of the deep learning
model for classifying sleep stages in mice,” https://jusjusjus.github.io/
html/edfmicestaging.html, 2018.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
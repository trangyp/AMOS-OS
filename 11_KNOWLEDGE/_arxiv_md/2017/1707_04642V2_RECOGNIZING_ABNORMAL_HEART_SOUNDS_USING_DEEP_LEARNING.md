---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1707.04642v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1707.04642v2_Recognizing_Abnormal_Heart_Sounds_Using_Deep_Learning

> Source: 1707.04642v2_Recognizing_Abnormal_Heart_Sounds_Using_Deep_Learning.pdf

> Pages: 7

---


## Page 1


Recognizing Abnormal Heart Sounds Using Deep Learning
Jonathan Rubin1, Rui Abreu2, Anurag Ganguli2, Saigopal Nelaturi2, Ion Matei2, Kumar Sricharan2
1 Philips Research North America, 2 PARC, A Xerox Company
jonathan.rubin@philips.com, rui@computer.org,
{anurag.ganguli, saigopal.nelaturi, ion.matei, sricharan.kumar}@parc.com
Abstract
The work presented here applies deep learning to
the task of automated cardiac auscultation, i.e. rec-
ognizing abnormalities in heart sounds.
We de-
scribe an automated heart sound classiﬁcation al-
gorithm that combines the use of time-frequency
heat map representations with a deep convolutional
neural network (CNN). Given the cost-sensitive
nature of misclassiﬁcation, our CNN architecture
is trained using a modiﬁed loss function that di-
rectly optimizes the trade-off between sensitivity
and speciﬁcity. We evaluated our algorithm at the
2016 PhysioNet Computing in Cardiology chal-
lenge where the objective was to accurately clas-
sify normal and abnormal heart sounds from sin-
gle, short, potentially noisy recordings. Our en-
try to the challenge achieved a ﬁnal speciﬁcity of
0.95, sensitivity of 0.73 and overall score of 0.84.
We achieved the greatest speciﬁcity score out of
all challenge entries and, using just a single CNN,
our algorithm differed in overall score by only 0.02
compared to the top place ﬁnisher, which used an
ensemble approach.
1
Introduction
Advances in deep learning [LeCun et al., 2015] are be-
ing made at a rapid pace, in part due to challenges such
as ILSVRC – the ImageNet Large-Scale Visual Recognition
Challenge [Russakovsky et al., 2015]. Successive improve-
ments in deep neural network architectures have resulted in
computer vision systems that are better able to recognize and
classify objects in images [Lin et al., 2013; Szegedy et al.,
2015] and winning ILSVRC entries [Szegedy et al., 2014;
He et al., 2015]. While a large focus of deep learning has
been on automated analysis of image and text data, advances
are also increasingly being seen in areas that require process-
ing other input modalities. One such area is the medical do-
main where inputs into a deep learning system could be phys-
iologic time series data. An increasing number of large scale
challenges in the medical domain, such as [Kaggle, 2014] and
[Kaggle, 2015] have also resulted in improvements to deep
learning architectures [Liang and Hu, 2015].
PhysioNet [Goldberger et al., 2000] has held a Comput-
ing in Cardiology Challenge since 2000 that requires partic-
ipants to automatically analyze physiologic time series data.
The 2016 challenge [Clifford et al., 2016] asked participants
to perform automated analysis of phonocardiogram (PCG)
waveforms, i.e.
heart sound data collected using digital
stethoscopes. The objective of the challenge was to accu-
rately classify normal and abnormal heart sounds. Record-
ings were collected from both healthy individuals, as well as
those with heart disease, including heart valve disease and
coronary artery disease. A PCG plot showing the recording
of the (normal) sounds made by the heart is given in Figure 1.
Figure 1: A phonocardiogram showing the recording of nor-
mal heart sounds, together with corresponding electrocardio-
gram tracing. S1 is the ﬁrst heart sound and marks the begin-
ning of systole. Source [Springer et al., 2016].
Heart disease remains the leading cause of death globally,
resulting in more people dying every year due to cardiovas-
cular disease compared to any other cause of death [World
Health Organization, 2017]. Successful automated PCG anal-
ysis can serve as a useful diagnostic tool to help determine
whether an individual should be referred on for expert di-
agnosis, particularly in areas where access to clinicians and
medical care is limited.
In this work, we present an algorithm that accepts PCG
waveforms as input and uses a deep convolutional neural net-
work architecture to classify inputs as either normal or abnor-
arXiv:1707.04642v2  [cs.SD]  19 Oct 2017


## Page 2


mal using the following steps:
1. Segmentation of time series A logistic regression hidden
semi-Markov model is used to segment incoming heart
sound instances into shorter segments beginning at the
start of each heartbeat, i.e. the S1 heart sound.
2. Transformation of segments into heat maps Using
Mel-frequency cepstral coefﬁcients, one dimensional
time series input segments are converted into two-
dimensional spectrograms (heat maps) that capture the
time-frequency distribution of signal energy.
3. Classiﬁcation of heat maps using a deep neural network
A convolutional neural network is trained to perform
automatic feature extraction and distinguish between
normal and abnormal heat maps.
The contributions of this work are as follows:
1. We introduce a deep convolutional neural network ar-
chitecture designed to automatically analyze physiologic
time series data for the purposes of identifying abnor-
malities in heart sounds.
2. Given the cost-sensitive nature of misclassiﬁcation, we
describe a novel loss function used to train the above
network that directly optimizes the sensitivity and speci-
ﬁcity trade-off.
3. We present results from the 2016 PhysioNet Computing
in Cardiology Challenge where we evaluated our algo-
rithm and achieved a Top 10 place ﬁnish out of 48 teams
who submitted a total of 348 entries.
The remainder of this paper is organized as follows. In
Section 2, we discuss related works, including historical ap-
proaches to automated heart sound analysis and deep learning
approaches that process physiologic time series input data.
Section 3 introduces our approach and details each step of
the algorithm. Section 4 further describes the modiﬁed cost-
sensitive loss function used to trade-off the sensitivity and
speciﬁcity of the network’s predictions, followed by Section
5, which details the network training decisions and param-
eters. Section 6 presents results from the 2016 PhysioNet
Computing in Cardiology Challenge and in Section 7 we pro-
vide a ﬁnal discussion and end with conclusions in Section
8.
2
Related Work
Before the 2016 PhysioNet Computing in Cardiology Chal-
lenge there were no existing approaches (to the authors’
knowledge) that applied the tools and techniques of “deep
learning” to the automated analysis of heart sounds [Liu et
al., 2016]. Previous approaches relied upon a combination of
feature extraction routines input into classic supervised ma-
chine learning classiﬁers. Features extracted from heart cy-
cles in the time and frequency domains, as well as wavelet
features, time-frequency and complexity-based features were
input into artiﬁcial neural networks [De Vos and Blancken-
berg, 2007; U˘guz, 2012a; U˘guz, 2012b; Sepehri et al., 2008;
Bhatikar et al., 2005] and support vector machines [Maglo-
giannis et al., 2009; Ari et al., 2010; Zheng et al., 2015]
for classiﬁcation. Previous works have also employed Hid-
den Markov Models for both segmenting PCG signals into
the fundamental heart sounds [Springer et al., 2014; Springer
et al., 2016], as well as classifying normal and abnormal in-
stances [Wang et al., 2007; Sarac¸oglu, 2012].
While there have been many previous efforts applied to au-
tomated heart sound analysis, gauging the success of histor-
ical approaches has been somewhat difﬁcult, due to differ-
ences in dataset quality, number of recordings available for
training and testing algorithms, recorded signal lengths and
the environment in which data was collected (e.g. clinical vs.
non-clinical settings). Moreover, some existing works have
not performed appropriate train-test data splits and have re-
ported results on training or validation data, which is highly
likely to produce optimistic results due to overﬁtting [Liu et
al., 2016]. In this work, we report results from the 2016 Phy-
sioNet Computing in Cardiology Challenge, which evaluated
entries on a large hidden test-set that was not made publicly
available. To reduce overﬁtting, no recordings from the same
subject were included in both the training and the test set and
a variety of both clean and noisy PCG recordings, which ex-
hibited very poor signal quality, were included to encourage
the development of accurate and robust algorithms.
The work presented in this paper, is one of the ﬁrst at-
tempts at applying deep learning to the task of heart sound
data analysis. However, there have been recent efforts to ap-
ply deep learning approaches to other types of physiological
time series analysis tasks. An early work that applied deep
learning to the domain of psychophysiology is described in
[Mart´ınez et al., 2013]. They advocate the use of preference
deep learning for recognizing affect from physiological in-
puts such as skin conductance and blood volume pulse within
a game-based user study. The authors argue against the use
of manual ad-hoc feature extraction and selection in affective
modeling, as this limits the creativity of attribute design to the
researcher. One difference between the work of [Mart´ınez et
al., 2013] and ours is that they perform an initial unsuper-
vised pre-training step using stacked convolutional denoising
auto-encoders, whereas our network does not require this step
and is instead trained in a supervised fashion end-to-end.
Similar deep learning efforts that process physiologic time
series have also been applied to the problems of epileptic
seizure prediction [Mirowski et al., 2008] and human activity
recognition [Hammerla et al., 2016].
3
Approach
Recall from Section 1 that our approach consists of three gen-
eral steps: segmentation, transformation and classiﬁcation.
Each is described in detail below.
3.1
Segmentation of time series
The main goal of segmentation is to ensure that incoming
time series inputs are appropriately aligned before attempting
to perform classiﬁcation. We ﬁrst segment the incoming heart
sound instances into shorter segments and locate the begin-
ning of each heartbeat, i.e. the S1 heart sound. A logistic re-
gression hidden semi-Markov model [Springer et al., 2016] is
used to predict the most likely sequence of heart sound states


## Page 3


Figure 2: MFCC heat map visualization of a 3-second segment of heart sound data. Sliding windows, i, are represented on
the horizontal axis and ﬁlterbank frequencies, j, are stacked along the inverted y-axis. MFCC energy information, ci,j is
represented by pixel color in the spectrograms. Also shown are the original one-dimensional PCG waveforms that produced
each heat map.
(S1 →Systole →S2 →Diastole) by incorporating informa-
tion about expected state durations.
Once the S1 heart sound has been identiﬁed, a time seg-
ment of length, T, is extracted. Segment extraction can either
be overlapping or non-overlapping. Our ﬁnal model used a
segment length of, T = 3 seconds, and we chose to use over-
lapping segments as this led to performance improvements
during initial training and validation.
3.2
Transformation of segments into heat maps
Each segment is transformed from a one-dimensional time
series signal into a two-dimensional heat map that captures
the time-frequency distribution of signal energy. We chose
to use Mel Frequency Cepstral Coefﬁcents [Davis and Mer-
melstein, 1980] to perform this transformation, as MFCCs
capture features from audio data that more closely resembles
how human beings perceive loudness and pitch. MFCCs are
commonly used as a feature type in automatic speech recog-
nition [Godino-Llorente and Gomez-Vilda, 2004].
We apply the following steps to achieve the transformation:
1. Given an input segment of length, T, and sampling rate,
ν, select a window length, ℓ, and step size, ∆, and extract
overlapping sliding windows, si(n), from the input time
series segment, where i ∈[1,
 T
∆

] is the window index
and n ∈[1, ℓν] is the sample index. We chose a window
length of 0.025 seconds and a step size of 0.01 seconds.
2. Compute the Discrete Fourier transform for each win-
dow.
Si(k) =
ℓν
X
n=1
si(n)h(n)ei2πn k
ℓν
(1)
where k ∈[1, K], K is the length of the DFT and h(n)
is a hamming window of length N. The power spectral
estimate for window, i, is then given by (2).
Pi(k) = 1
N |Si(k)|2
(2)
3. Apply a ﬁlterbank of, j ∈[1, J], triangular band-pass
ﬁlters, dj,1...K, to the power spectral estimates, Pi(k),
and sum the energies in each ﬁlter together. Include a
log transformation as sound volume is not perceived on
a linear scale.
c∗
i,j = log(
K
X
k=1
dj,kPi(k))
(3)
We used a ﬁlterbank consisting of J
= 26 ﬁlters,
where frequency ranges were derived using the Mel
scale that maps actual measured frequencies, f, to values
that better match how humans perceive pitch, M(f) =
1125 ln(1 +
f
700).
4. Finally, apply a Discrete Cosine Transform to decorre-
late the log ﬁlterbank energies, which are correlated due
to overlapping windows in the Mel ﬁlterbank.
ci,j =
J
X
j=1
c∗
i,j cos
hk(2i −1)π
2J
i
, k = 1 . . . J
(4)
The result is a collection of cepstral coefﬁcients, ci,j for
window, i. For i = 1 . . .
 T
∆

, ci,j can be stacked to-
gether to give a time-frequency heat map that captures
changes in signal energy over heart sound segments.
Figure 2 illustrates two example heat maps (one derived
from a normal heart sound input and the other from an
abnormal input), where ci,j is the MFCC value (repre-
sented by color) at location, i, on the horizontal axis and,
j, on the (inverted) vertical axis.
3.3
Classiﬁcation of heat maps using a deep neural
network
The result of transforming the original one-dimensional time-
series into a two-dimensional time-frequency representation
is that now each heart sound segment can be processed as an
image, where energy values over time can be visualized as a
heat map (see Figure 2). Convolutional neural networks are a
natural choice for training image classiﬁers, given their abil-
ity to automatically learn appropriate convolutional ﬁlters.
Therefore, we chose to train a convolutional neural network
architecture using heat maps as inputs.
Decisions about the number of ﬁlters to apply and their
sizes, as well as how many layers and their types to include
in the network were made by a combination of initial manual


## Page 4


Figure 3: Convolutional neural network architecture for predicting normal versus abnormal heart sounds using MFCC heat
maps as input
exploration by the authors, followed by employing a random
search over a limited range of network architecture parame-
ters. Figure 3 depicts the network architecture of a convolu-
tional neural network that accepts as input a single channel
6x300 MFCC heat map and outputs a binary classiﬁcation,
predicting whether the input segment represents a normal or
abnormal heart sound.
The ﬁrst convolutional layer learns 64 2x20 kernels, using
same-padding. This is followed by applying a 1x20 max-
pooling ﬁlter, using a horizontal stride of 5, which has the
effect of reducing each of the 64 feature maps to a dimension
of 6x60. A second convolutional layer applies 64 2x10 ker-
nels over the previous layer, once again using same padding.
This is again followed by a max-pooling operation using a ﬁl-
ter size of 1x4 and a stride of 2, further reducing each feature
map to a dimension of 6x30. At this stage in the architec-
ture a ﬂattening operation is applied that unrolls each of the
64 6x30 feature maps into a single dimensional vector of size
11,520. This feature vector is fed into a ﬁrst fully connected
layer consisting of 1024 hidden units, followed by a second
layer of 512 hidden units and ﬁnally a binary classiﬁcation
output.
4
Sensitivity-Speciﬁcity Loss Trade-off
The loss function of the network was altered from a standard
softmax cross entropy loss function to instead directly trade-
off between sensitivity and speciﬁcity.
Given unnormalized log-probabilities, y = Wx + b, from
a classiﬁer consisting of weight matrix, W, and bias b. The
softmax function:
s(yi) =
eyi
P
j
eyj
(5)
gives probability predictions P(yi|x; W, b) for the class at in-
dex, i, for input x.
Consider,
Y =


s(y(1))
s(y(2))
...
s(y(n))

, Y ∗=


y∗(1)
y∗(2)
...
y∗(n)


where s(y(j)
i ), refers to the ith entry of row j and Y ∗is the
corresponding one hot encoded matrix of actual class labels.
For the binary class labels of normal (y∗
0) and abnormal
(y∗
1), we deﬁne the mask matrices, YNn and YAa, where en-
tries within each matrix are softmax prediction values ex-
tracted ∀s(y(j))∈Y , as follows:
YNn =









s(y(j)
0 ),
where y∗(j)
0
= 1 and
arg max {s(y(j))} = arg max{y∗(j)}
0,
otherwise
YAa =









s(y(j)
1 ),
where y∗(j)
1
= 1 and
arg max {s(y(j))} = arg max{y∗(j)}
0,
otherwise
We then deﬁne softmax sensitivity, Se, and speciﬁcity, Sp,
as follows:
Se =
X
j
Y (j)
Aa
Y ∗(j)
Aa
,
Sp =
X
j
Y (j)
Nn
Y ∗(j)
Nn
(6)
The ﬁnal loss function we wish to minimize is given in (7).
LSeSp = −(Se + Sp) + λR(W)
(7)
where λR(W) is a regularization parameter and routine, re-
spectively.


## Page 5


Hyper-parameters
Value
Learning rate
0.00015822
Beta
0.000076253698849
Dropout
0.85565561
Network parameters
Value
Regularization Type
L2
Batch Size
256
Weight Update
Adam Optimization
Table 1: Listing of hyper-parameters and selected network
parameters. Hyper-parameters were learned over the network
architecture described in Section 3.3, using random search
over a restricted parameter space.
5
Network Training
L2 regularization was computed for each of the fully con-
nected layers’ weight and bias matrices and applied to the loss
function. Dropout was applied within both fully connected
layers. Table 1 shows the values of hyper-parameters cho-
sen by performing a random search through parameter space,
as well as a list of other network training choices, including
weight updates and use of regularization. Adam optimization
[Kingma and Ba, 2014] was used to perform weight updates.
Models were trained on a single NVIDIA GPU with between
4 – 6 GB of memory. A mini-batch size of 256 was selected
to satisfy the memory constraints of the GPU.
5.1
Training/Validation/Test Datasets
The overall dataset used within the PhysioNet Computing in
Cardiology Challenge was provided by the challenge orga-
nizers and consisted of eight heart sound databases collected
from seven countries over a period of more than a decade
[Clifford et al., 2016]. In total 4,430 recordings were taken
from 1,072 subjects, resulting in 30 hours of heart sound
recordings. From this total dataset, 1,277 heart sound record-
ings from 308 subjects were removed to be used as held-
out test data for evaluating challenge submissions. The test
dataset was not made publicly available and challengers were
only allowed to make 15 submissions, in total, to the chal-
lenge server to evaluate their models on a small 20% subset
of the hidden dataset, before ﬁnal results were computed. The
number of allowed submissions was limited to avoid the is-
sue of participants implicitly overﬁtting their models on the
hidden test dataset.
From the 3153 publicly available PCG waveforms supplied
by the challenge organizers, the authors set aside a further
301 instances to be used as a local held-out test-set to gauge
model performance before making a submission to the chal-
lenge server. The remaining instances were used to train ini-
tial models. Models were trained on the overlapping 3-second
MFCC segments extracted from the remaining 2852 PCG
waveforms. This resulted in approximately 90,000 MFCC
heat maps, which were split into a training (∼75, 000 in-
stances) and validation set (∼15, 000 instances). This train-
ing and validation set was unbalanced, consisting of approx-
imately 80% normal segments and 20% abnormal segments.
Training was performed on the unbalanced dataset and no at-
tempt was made to compensate for this class imbalance.
Given that each model was trained on 3-second MFCC heat
map segments, it was necessary to stitch together a collection
of predictions to classify a single full instance. The simple
strategy of averaging each class’s prediction probability was
employed and the class with the greatest probability was se-
lected as the ﬁnal prediction.
6
Results
Equations (8) and (9) show the modiﬁed sensitivity and speci-
ﬁcity scoring metrics that were used to assess the submit-
ted entries to the 2016 PhysioNet Computing in Cardiology
Challenge [Clifford et al., 2016]. Uppercase symbols reﬂect
the true class label, which could either be (A)bnormal, or
(N)ormal. Lowercase symbols refer to a classiﬁer’s predicted
output where, once again, a is abnormal, n is normal and q
is a prediction of unsure. A subscript of 1 (e.g. Aa1, Na1)
refers to heart sound instances that were considered good sig-
nal quality by the challenge organizers and a subscript of 2
(e.g. An2, Nn2) refers to heart sound instances that were
considered poor signal quality by challenge organizers. Fi-
nally, the weights used to calculate sensitivity, wa1 and wa2,
capture the percentages of good signal quality and poor signal
quality recordings in all abnormal recordings. Correspond-
ingly for speciﬁcity, the weights wn1 and wn2 are the propor-
tion of good signal quality and poor signal quality recordings
in all normal recordings. Overall, scores are given by Se+Sp
2
.
Se =
wa1 · Aa1
Aa1 + Aq1 + An1
+ wa2 · (Aa2 + Aq2)
Aa2 + Aq2 + An2
,
(8)
Sp =
wn1 · Nn1
Na1 + Nq1 + Nn1
+ wn2 · (Nn2 + Nq2)
Na2 + Nq2 + Nn2
(9)
Table 2 shows a selected subset of the results for the 2016
PhysioNet Computing in Cardiology Challenge.
For each
selected entry, sensitivity, speciﬁcity and overall scores are
shown, as well as the entry’s ﬁnal ranking and a brief descrip-
tion of its approach. In total, 348 entries were submitted by
48 teams. Our entry, as described by the algorithm presented
in this paper, was ranked 8th with a sensitivity of 0.7278 and
speciﬁcity of 0.9521, giving an overall score of 0.8399. The
top entry to the competition achieved sensitivity of 0.9424,
speciﬁcity of 0.7781 for an overall score of 0.8602. Also
included in Table 2 is the result of a benchmark entry that
was supplied by the challenge organizers, which ranked 43rd
overall, with a sensitivity of 0.6545 and speciﬁcity of 0.7569,
for an overall score of 0.7057.
7
Discussion
Table 2 shows that the overall scores for the top entries to
the PhysioNet Computing in Cardiology challenge were very
close. In particular, our entry, which achieved an 8th place
ranking, had a difference in score of only 0.02, compared
to the top place ﬁnisher.
For our entry, the overall score
of 0.8399 was achieved using a single convolutional neural
network, whereas other top place ﬁnishers achieved strong
classiﬁcation accuracies using an ensemble of classiﬁers. Im-
provements in performance have often been witnessed using


## Page 6


Rank
Sensitivity
Speciﬁcity
Overall
Description
1
0.9424
0.7781
0.8602
AdaBoost & CNN
2
0.8691
0.849
0.859
Ensemble of SVMs
3
0.8743
0.8297
0.852
Regularized Neural Networks
4
0.8639
0.8269
0.8454
MFCCs, Wavelets, Tensors & kNN
5
0.8848
0.8048
0.8448
Random Forest + LogitBoost
6
0.8063
0.8766
0.8415
Unofﬁcial entry
7
0.7696
0.9125
0.8411
Probability-distribution based
8
0.7278
0.9521
0.8399
Our Approach (see Section 3)
9
0.8691
0.7873
0.8282
Approach Unknown
10
0.7696
0.8831
0.8263
Approach Unknown
43
0.6545
0.7569
0.7057
Provided Benchmark Entry
48
0.8063
0.2643
0.5353
Approach Unknown
Table 2: Selected results from the 2016 PhysioNet Computing in Cardiology Challenge
an ensemble of networks or separate classiﬁers and we leave
this for future work/improvement. For practical purposes, a
diagnostic tool that relies on only a single network, as op-
posed to a large ensemble, has the advantage of limiting the
amount of computational resources required for classiﬁca-
tion. Deployment of such a diagnostic tool on platforms that
impose restricted computational budgets, e.g mobile-based,
could perhaps beneﬁt from such a trade-off between accuracy
and computational cost.
Another point of interest is that our entry to the PhysioNet
Computing in Cardiology challenge achieved the greatest
speciﬁcity score (0.9521) out of all challenge entries. How-
ever, the network architecture produced a lower sensitivity
score (0.7278). Once again, considering the practical result
of deploying a diagnostic tool that relied upon our algorithm,
this would likely result in a system with few false positives,
but at the expense of misclassifying some abnormal instances.
Final decisions about the trade-off between sensitivity and
speciﬁcity would require further consideration of the exact
conditions and context of the deployment environment.
A ﬁnal point of discussion and area of future improvement
is that the approach presented was limited to binary decision
outputs, i.e. either normal or abnormal heart sounds. An
architecture that also considered signal quality as an output
would likely result in performance improvement.
8
Conclusion
The work presented here is one of the ﬁrst to apply deep
convolutional neural networks to the task of automated heart
sound classiﬁcation for recognizing normal and abnormal
heart sounds. We have presented a novel algorithm that com-
bines a CNN architecture with MFCC heat maps that capture
the time-frequency distribution of signal energy. The network
was trained to automatically distinguish between normal and
abnormal heat map inputs and it was designed to optimize
a loss function that directly considers the trade-off between
sensitivity and speciﬁcity.
We evaluated the approach by
submitting our algorithm as an entry to the 2016 PhysioNet
Computing in Cardiology Challenge. The challenge required
the creation of accurate and robust algorithms that could deal
with heart sounds that exhibit very poor signal quality. Over-
all, our entry to the challenge achieved a Top-10 place ﬁnish
out of 48 teams who submitted 348 entries. Moreover, us-
ing just a single CNN, our algorithm differed by a score of at
most 0.02 compared to other top place ﬁnishers, all of which
used an ensemble approach of some kind.
References
[Ari et al., 2010] Samit
Ari,
Koushik
Hembram,
and
Goutam Saha. Detection of cardiac abnormality from pcg
signal using lms based least square svm classiﬁer. Expert
Systems with Applications, 37(12):8019–8026, 2010.
[Bhatikar et al., 2005] Sanjay R Bhatikar, Curt DeGroff, and
Roop L Mahajan. A classiﬁer based on the artiﬁcial neu-
ral network approach for cardiologic auscultation in pedi-
atrics. Artiﬁcial intelligence in medicine, 33(3):251–260,
2005.
[Clifford et al., 2016] Gari D Clifford, CY Liu, Benjamin
Moody, David Springer, Ikaro Silva, Qiao Li, and Roger G
Mark.
Classiﬁcation of normal/abnormal heart sound
recordings: the physionet/computing in cardiology chal-
lenge 2016.
Computing in Cardiology, pages 609–12,
2016.
[Davis and Mermelstein, 1980] Steven Davis and Paul Mer-
melstein.
Comparison of parametric representations for
monosyllabic word recognition in continuously spoken
sentences. IEEE transactions on acoustics, speech, and
signal processing, 28(4):357–366, 1980.
[De Vos and Blanckenberg, 2007] Jacques P De Vos and
Mike M Blanckenberg. Automated pediatric cardiac aus-
cultation. IEEE Transactions on Biomedical Engineering,
54(2):244–252, 2007.
[Godino-Llorente and Gomez-Vilda, 2004] Juan
Ignacio
Godino-Llorente and P Gomez-Vilda. Automatic detec-
tion of voice impairments by means of short-term cepstral
parameters and neural network based detectors.
IEEE
Transactions on Biomedical Engineering, 51(2):380–384,
2004.
[Goldberger et al., 2000] A. L. Goldberger, L. A. N. Ama-
ral, L. Glass, J. M. Hausdorff, P. Ch. Ivanov, R. G. Mark,
J. E. Mietus, G. B. Moody, C.-K. Peng, and H. E. Stanley.
PhysioBank, PhysioToolkit, and PhysioNet: Components


## Page 7


of a new research resource for complex physiologic sig-
nals. Circulation, 101(23):e215–e220, 2000.
[Hammerla et al., 2016] Nils Y. Hammerla, Shane Halloran,
and Thomas Pl¨otz.
Deep, convolutional, and recurrent
models for human activity recognition using wearables.
In Subbarao Kambhampati, editor, Proceedings of the
Twenty-Fifth International Joint Conference on Artiﬁcial
Intelligence, IJCAI 2016, New York, NY, USA, 9-15 July
2016, pages 1533–1540. IJCAI/AAAI Press, 2016.
[He et al., 2015] Kaiming He, Xiangyu Zhang, Shaoqing
Ren, and Jian Sun. Deep residual learning for image recog-
nition. CoRR, abs/1512.03385, 2015.
[Kaggle, 2014] Kaggle. American epilepsy society seizure
prediction challenge.
https://www.kaggle.com/
c/seizure-prediction, 2014.
[Online; accessed
22-December-2016].
[Kaggle, 2015] Kaggle.
Grasp-and-Lift
EEG
De-
tection.
https://www.kaggle.com/c/
grasp-and-lift-eeg-detection, 2015.
[On-
line; accessed 22-December-2016].
[Kingma and Ba, 2014] Diederik P. Kingma and Jimmy Ba.
Adam: A method for stochastic optimization.
CoRR,
abs/1412.6980, 2014.
[LeCun et al., 2015] Yann LeCun, Yoshua Bengio, and Ge-
offrey Hinton. Deep learning. Nature, 521(7553):436–
444, 2015.
[Liang and Hu, 2015] Ming Liang and Xiaolin Hu.
Re-
current convolutional neural network for object recogni-
tion. In IEEE Conference on Computer Vision and Pattern
Recognition, CVPR 2015, Boston, MA, USA, June 7-12,
2015, pages 3367–3375. IEEE Computer Society, 2015.
[Lin et al., 2013] Min Lin, Qiang Chen, and Shuicheng Yan.
Network in network. CoRR, abs/1312.4400, 2013.
[Liu et al., 2016] Chengyu Liu, David Springer, Qiao Li,
Benjamin Moody, Ricardo Abad Juan, Francisco J Chorro,
Francisco Castells, Jos´e Millet Roig, Ikaro Silva, Alis-
tair EW Johnson, et al. An open access database for the
evaluation of heart sound algorithms. Physiological Mea-
surement, 37(12):2181, 2016.
[Maglogiannis et al., 2009] Ilias
Maglogiannis,
Euripidis
Loukis, Elias Zaﬁropoulos, and Antonis Stasis. Support
vectors machine-based identiﬁcation of heart valve dis-
eases using heart sounds.
Computer methods and pro-
grams in biomedicine, 95(1):47–61, 2009.
[Mart´ınez et al., 2013] H´ector Perez Mart´ınez, Yoshua Ben-
gio, and Georgios N. Yannakakis. Learning deep physio-
logical models of affect. IEEE Comp. Int. Mag., 8(2):20–
33, 2013.
[Mirowski et al., 2008] Piotr W Mirowski, Yann LeCun,
Deepak Madhavan, and Ruben Kuzniecky.
Comparing
svm and convolutional networks for epileptic seizure pre-
diction from intracranial eeg. In 2008 IEEE Workshop on
Machine Learning for Signal Processing, pages 244–249.
IEEE, 2008.
[Russakovsky et al., 2015] Olga Russakovsky,
Jia Deng,
Hao Su, Jonathan Krause, Sanjeev Satheesh, Sean Ma,
Zhiheng Huang, Andrej Karpathy, Aditya Khosla, Michael
Bernstein, Alexander C. Berg, and Li Fei-Fei.
Ima-
geNet Large Scale Visual Recognition Challenge. Inter-
national Journal of Computer Vision (IJCV), 115(3):211–
252, 2015.
[Sarac¸oglu, 2012] Ridvan Sarac¸oglu. Hidden markov model-
based classiﬁcation of heart valve disease with PCA for
dimension reduction. Eng. Appl. of AI, 25(7):1523–1528,
2012.
[Sepehri et al., 2008] Amir A Sepehri, Joel Hancq, Thierry
Dutoit,
Arash Gharehbaghi,
Armen Kocharian,
and
A Kiani.
Computerized screening of children congeni-
tal heart diseases.
Computer methods and programs in
biomedicine, 92(2):186–192, 2008.
[Springer et al., 2014] David B Springer, Lionel Tarassenko,
and Gari D Clifford. Support vector machine hidden semi-
markov model-based heart sound segmentation. In Com-
puting in Cardiology 2014, pages 625–628. IEEE, 2014.
[Springer et al., 2016] David B Springer, Lionel Tarassenko,
and Gari D Clifford.
Logistic regression-hsmm-based
heart sound segmentation. IEEE Transactions on Biomed-
ical Engineering, 63(4):822–832, 2016.
[Szegedy et al., 2014] Christian Szegedy, Wei Liu, Yangqing
Jia, Pierre Sermanet, Scott E. Reed, Dragomir Anguelov,
Dumitru Erhan, Vincent Vanhoucke, and Andrew Ra-
binovich.
Going deeper with convolutions.
CoRR,
abs/1409.4842, 2014.
[Szegedy et al., 2015] Christian
Szegedy,
Vincent
Van-
houcke, Sergey Ioffe, Jonathon Shlens, and Zbigniew
Wojna. Rethinking the inception architecture for computer
vision. CoRR, abs/1512.00567, 2015.
[U˘guz, 2012a] Harun U˘guz.
Adaptive neuro-fuzzy infer-
ence system for diagnosis of the heart valve diseases using
wavelet transform with entropy. Neural Computing and
applications, 21(7):1617–1628, 2012.
[U˘guz, 2012b] Harun U˘guz. A biomedical system based on
artiﬁcial neural network and principal component analysis
for diagnosis of the heart valve diseases. Journal of medi-
cal systems, 36(1):61–72, 2012.
[Wang et al., 2007] Ping Wang,
Chu Sing Lim,
Sunita
Chauhan, Jong Yong A Foo, and Venkataraman Anan-
tharaman. Phonocardiographic signal analysis method us-
ing a modiﬁed hidden markov model. Annals of Biomedi-
cal Engineering, 35(3):367–374, 2007.
[World Health Organization, 2017] World
Health
Organi-
zation. Cardiovascular diseases (cvds). http://who.
int/mediacentre/factsheets/fs317/en/,
2017. [Online; accessed 01-Febuary-2017].
[Zheng et al., 2015] Yineng Zheng, Xingming Guo, and Xi-
aorong Ding. A novel hybrid energy fraction and entropy-
based approach for systolic heart murmurs identiﬁca-
tion. Expert Systems with Applications, 42(5):2710–2721,
2015.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1707_04642v2_recognizing_abnormal_heart_sounds_using_deep_learning
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2017/1707_04642V2_RECOGNIZING_ABNORMAL_HEART_SOUNDS_USING_DEEP_LEARNING.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

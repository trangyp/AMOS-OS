---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1908.08419v3
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1908.08419v3_NE-LP__Normalized_Entropy_and_Loss_Prediction_based_Sampling_for_Active_Learning

> Source: 1908.08419v3_NE-LP__Normalized_Entropy_and_Loss_Prediction_based_Sampling_for_Active_Learning.pdf

> Pages: 12

---


## Page 1


arXiv:1908.08419v3  [cs.CL]  17 Jul 2020
Neural Computing and Applications manuscript No.
(will be inserted by the editor)
NE-LP: Normalized Entropy and Loss Prediction based
Sampling for Active Learning in Chinese Word Segmentation
on EHRs
Tingting Cai · Zhiyuan Ma · Hong Zheng · Yangming Zhou
Received: date / Accepted: date
Abstract Electronic Health Records (EHRs) in hos-
pital information systems contain patients’ diagnosis
and treatments, so EHRs are essential to clinical data
mining. Of all the tasks in the mining process, Chinese
Word Segmentation (CWS) is a fundamental and im-
portant one, and most state-of-the-art methods greatly
rely on large-scale of manually-annotated data. Since
annotation is time-consuming and expensive, eﬀorts have
been devoted to techniques, such as active learning,
to locate the most informative samples for modeling.
In this paper, we follow the trend and present an ac-
tive learning method for CWS in EHRs. Speciﬁcally,
a new sampling strategy combining Normalized En-
Corresponding author : Yangming Zhou
E-mail: ymzhou@ecust.edu.cn
Tingting Cai
School of Information Science and Engineering, East China
University of Science and Technology, Shanghai 200237,
China
E-mail: y30190775@mail.ecust.edu.cn
Zhiyuan Ma
Institute of Machine Intelligence, University of Shanghai for
Science and Technology, Shanghai 200093, China
E-mail: yuliar3514@usst.edu.cn
Hong Zheng
School of Information Science and Engineering, East China
University of Science and Technology, Shanghai 200237,
China
E-mail: zhenghong@ecust.edu.cn
Yangming Zhou
School of Information Science and Engineering, East China
University of Science and Technology, Shanghai 200237,
China
The Key Laboratory of Advanced Control and Optimization
for Chemical Processes, Ministry of Education, East China
University of Science and Technology, 130 Meilong Road,
200237 Shanghai, China
E-mail: ymzhou@ecust.edu.cn
tropy with Loss Prediction (NE-LP) is proposed to se-
lect the most representative data. Meanwhile, to min-
imize the computational cost of learning, we propose
a joint model including a word segmenter and a loss
prediction model. Furthermore, to capture interactions
between adjacent characters, bigram features are also
applied in the joint model. To illustrate the eﬀective-
ness of NE-LP, we conducted experiments on EHRs col-
lected from the Shuguang Hospital Aﬃliated to Shang-
hai University of Traditional Chinese Medicine. The re-
sults demonstrate that NE-LP consistently outperforms
conventional uncertainty-based sampling strategies for
active learning in CWS.
Keywords Active learning · Chinese word segmenta-
tion · Deep learning · Electronic health records
1 Introduction
Electronic Health Records (EHRs) systematically col-
lect patients’ clinical information, such as health pro-
ﬁles, histories of present illness, past medical histories,
examination results and treatment plans [8]. By ana-
lyzing EHRs, many useful information, closely related
to patients, can be discovered [37]. Since Chinese EHRs
are recorded without explicit word delimiters (e.g., “糖
尿病酮症酸中毒” (diabetic ketoacidosis)), Chinese Word
Segmentation (CWS) is a prerequisite for processing
EHRs. Currently, state-of-the-art CWS methods usu-
ally require large amounts of manually-labeled data to
reach their full potential. However, compared to gen-
eral domain, CWS in medical domain is more diﬃcult.
On one hand, EHRs involve many medical terminolo-
gies, such as “高血压性心脏病” (Hypertensive Heart
Disease) and “罗氏芬” (Rocephin), so only annotators
with medical backgrounds are qualiﬁed to label EHRs.


## Page 2


2
Tingting Cai et al.
On the other hand, EHRs may involve personal priva-
cies of patients. Therefore, they cannot be released on
large scales for labeling. The above two reasons lead to
the high annotation cost and insuﬃcient training cor-
pus for CWS in medical texts.
CWS was usually formulated as a sequence labeling
task [19], which can be solved by supervised learning
approaches, such as Hidden Markov Model (HMM) [6]
and Conditional Random Field (CRF) [16]. However,
these methods rely heavily on handcrafted features. To
relieve the eﬀorts of feature engineering, neural net-
work based methods are beginning to thrive [3, 5, 20].
However, due to insuﬃcient annotated training data,
conventional models for CWS trained on open corpora
often suﬀer from signiﬁcant performance degradation
when transferred to speciﬁc domains, let alone the re-
searches are rarely dabbled in medical domain.
One solution for this obstacle is to use active learn-
ing, where only a small scale of samples are selected and
labeled in an active manner. Active learning methods
are favored by the researchers in many Natural Lan-
guage Processing (NLP) tasks, such as text classiﬁca-
tion [30] and Named Entity Recognition (NER) [13].
However, only a handful of works are conducted on
CWS [19], and few focuses on medical domain.
Given the aforementioned challenges and current
researches, we propose a word segmentation method
based on active learning. To select the most informative
data, we incorporate a sampling strategy called NE-
LP, which consists of Normalized Entropy (NE) and
Loss Prediction (LP). Speciﬁcally, we leverage the nor-
malized entropy of class posterior possibilities from Bi-
directional Long-Short Term Memory and Conditional
Random Field (BiLSTM-CRF) based word segmenter
to deﬁne uncertainty. Then, we attach a “loss predic-
tion model” based on self-attention [31] to the word
segmenter and it aims to predict the loss of input data.
The ﬁnal decision on the selection of labeling samples
is made by calculating the sum of normalized token en-
tropy and losses according to a certain weight. Besides,
to capture coherence over characters, we additionally
add n-gram features to the input of the joint model
and experimental results show that for speciﬁc texts,
such as our medical texts, bigram performs best.
To sum up, the main contributions of our work are
summarized as follows:
– We propose a novel word segmentation method in-
corporating active learning and hybrid features. The
former lightens the burden of labeling large amounts
of data, and the latter combines bigram features
with character embeddngs to achieve better repre-
sentations of the coherence between adjacent char-
acters.
– To improve the performance of active learning, we
propose a simple, yet eﬀective sampling strategy
called NE-LP, which is based on a joint model in-
cluding a word segmenter and a loss prediction model.
Instead of solely relying on the uncertainty of clas-
sifying boundary to choose the most representative
samples for labeling, our proposed method utilizes
normalized token entropy to estimate the uncer-
tainty from outputs of the word segmenter at statis-
tical level, moreover, we also employ self-attention
as a loss prediction model to simulate human un-
derstanding of words from the deep learning level.
– Instead of evaluating the performance in simulated
data, we use cardiovascular diseases data collected
from the Shuguang Hospital Aﬃliated to Shanghai
University of Traditional Chinese Medicine to illus-
trate the improvements of the proposed method. Ex-
perimental results show that NE-LP is superior to
mainstream uncertainty-based sampling strategies
in F1-score.
The rest of this paper is organized as follows. Sec-
tion 2 brieﬂy reviews the related work on CWS and ac-
tive learning. Section 3 details the proposed method for
CWS, followed by experimental evaluations as Section
4. In the end, the conclusions and potential research
directions are summarized as Section 5.
2 Related Work
2.1 Chinese Word Segmentation
Due to the practical signiﬁcance [20], CWS has at-
tracted considerable research eﬀorts, and a great num-
ber of solution methods have been proposed in the lit-
erature in past decades [25, 35, 40]. Generally, all the
existing approaches fall into two categories: statistical
machine learning and deep learning [19].
Statistical Machine Learning Methods. Initially,
statistical machine learning methods were widely-used
in CWS. Xue and Shen [35] employed a maximum en-
tropy tagger to automatically assign Chinese charac-
ters. Zhao et al. [39] used CRF for tag decoding and
considered both feature template selection and tag set
selection. However, these methods greatly rely on man-
ual feature engineering [24], while handcrafted features
are diﬃcult to design, and the sizes of these features
are too large for practical use [3]. In such a case, deep
learning methods have been increasingly employed for
the ability to minimize the eﬀorts in feature engineer-
ing.
Deep Learning Methods. Recently, researchers
tended to apply various neural networks for CWS and


## Page 3


Title Suppressed Due to Excessive Length
3
achieved remarkable performance. To name a few, Zheng
et al. [40] used deep layers of neural networks to learn
feature representations of characters. Chen et al. [3]
adopted LSTM to capture the previous important in-
formation. Wang and Xu [32] proposed a Convolutional
Neural Network (CNN) to capture rich n-gram features
without any feature engineering. Gan and Zhang [7]
investigated self-attention for CWS and observed that
self-attention gives highly competitive results. Jiang and
Tang [14] proposed a sequence-to-sequence transformer
model to avoid overﬁtting and capture character infor-
mation at the distant site of a sentence. La Su and
Liu [15] presented a hybrid word segmentation algo-
rithm based on Bi-directional Gated Recurrent Unit
(BiGRU) and CRF to learn the semantic features of the
corpus. Ma et al. [22] found that BiLSTM can achieve
better results on many of the popular CWS datasets as
compared to models based on more complex neural net-
work architectures. Therefore, in this paper, we adopt
BiLSTM-CRF as our base word segmenter due to its
simple architecture, yet remarkable performance.
Open-source CWS Tools. In recent years, more
and more open-source CWS tools are emerging, such
as Jieba and PyHanLP. These tools are widely-used
due to convenience and great performance for CWS in
general ﬁelds. However, terminologies and uncommon
words in medical ﬁelds would lead to the unsatisfac-
tory performance of segmentation results. We experi-
mentally compare seven well-known open-source CWS
tools on EHRs. As shown in Table 4, we ﬁnd that since
these open-source tools are trained from general domain
corpora, the results are not ideal enough to cater to the
needs of subsequent NLP tasks when applied to medical
ﬁelds.
Domain-Speciﬁc CWS Methods. Currently, a
handful of domain-speciﬁc CWS approaches have been
studied, but they focused on decentralized domains.
In the metallurgical ﬁeld, Shao et al. [25] proposed a
domain-speciﬁc CWS method based on BiLSTM model.
In the medical ﬁeld, Xing et al. [34] proposed an adap-
tive multi-task transfer learning framework to fully lever-
age domain-invariant knowledge from high resource do-
main to medical domain. Meanwhile, transfer learning
still greatly focuses on the corpora in general domain.
When it comes to the speciﬁc ﬁeld, large amounts of
manually-annotated data are necessary. Active learn-
ing can solve this problem to a certain extent, where a
model asks human to annotate data that it is uncertain
of [38]. However, due to the challenges faced by per-
forming active learning on CWS, only a few studies have
been conducted. On judgements, Yan et al. [36] adopted
the local annotation strategy, which selects substrings
around the informative characters in active learning.
However, their method still stays at the statistical level.
Therefore, compared to the above method, we intend to
utilize a new active learning approach for CWS in med-
ical text, which combines normalized entropy with loss
prediction to eﬀectively reduce annotation cost.
2.2 Active Learning
Active learning [1] mainly aims to ease data collec-
tion process by automatically deciding which instances
should be labeled by annotators, thus saving the cost of
annotation [12]. In active learning, the sampling strat-
egy plays a key role. Over the past few years, the rapid
development of active learning has resulted in various
sampling strategies, such as uncertainty sampling [18],
query-by-committee [9] and information gain [11].
Currently, in sequence labeling tasks, uncertainty-
based method has attracted considerable attention since
it performs well and saves much time in most cases [21].
Traditional uncertainty-based sampling strategies mainly
include least conﬁdence, maximum token entropy and
minimum token margin.
Least Conﬁdence (LC). The LC strategy selects
the samples whose most likely sequence tags that the
model is least conﬁdent of. Despite its simplicity, this
approach has been proven eﬀective in various tasks [38].
SLC(x) = 1 −p (y∗|x)
(1)
where x is the instance to be predicted and y∗repre-
sents the most likely tag sequence of x.
Maximum Token Entropy (MTE). The MTE
strategy evaluates the uncertainty of a token by en-
tropy. The closer the distribution of marginal probabil-
ity to uniform, the larger the entropy:
SMT E(x) = −
N
X
i=1
p (y∗|x) · log p (y∗|x)
(2)
where N represents the number of classes.
Minimum Token Margin (MTM). To measure
the informativeness, MTM considers the ﬁrst and sec-
ond most likely assignments and subtracts the highest
probability by the lowest one [23]:
SMT M(x) = max p (y∗|x) −max ′p (y∗|x)
(3)
where max′ means the second maximum probability.
However, in some complicated tasks, such as CWS
and NER, only considering the uncertainty of data is
obviously not enough. Therefore, we further take loss
values into account and pick up samples from two per-
spectives including both uncertainty and loss.


## Page 4


4
Tingting Cai et al.
Base Model
Loss Prediction Model
Input Data
Segmentation Prediction
Loss Prediction
Fig. 1 The overall architecture of the joint model, where the
loss prediction model is attached to the base model.
3 Joint Model Incorporated Active Learning
framework for Chinese Word Segmentation
3.1 Overview
Active learning algorithm is generally composed of two
parts: a learning engine and a selection engine. The
learning engine is essentially a segmenter, which is mainly
utilized for training in sequence labeling problems. The
selection engine picks up unlabeled samples based on
preset sampling strategy and submits these samples for
human annotation. Then, we incorporate them into the
training set after experts complete the annotation, thus
continuously improving the F1-score of the segmenter
with the increasing of the training set size [26]. In this
paper, we propose a joint model as a selection engine.
Fig. 1 shows the overall architecture of the joint model,
where the loss prediction model predicts the loss value
from input data. Moreover, the loss prediction model is
(i) attached to the base model, and (ii) jointly learned
with the base model. Here, the base model is employed
as a learning engine.
Algorithm 1 demonstrates the procedure of CWS
based on active learning with the sampling strategy of
NE-LP. First, with training set, we train a joint model
including a segmenter and a loss prediction model. Later,
the joint model selects n-highest ranking samples based
on NE-LP strategy, which are expected to improve the
performance of the segmenter to the largest extent.
Afterwards, medical experts annotate these instances
manually. Finally, these annotated instances are incor-
porated into the training set, and we use the new train-
ing set to train the joint model. The above steps iterate
until the desired F1-score is achieved or the number of
iterations has reached a predeﬁned threshold.
Fig. 2 demonstrates the detailed architecture of the
joint model. First, we pre-process EHRs at the character-
level, separating each character of raw EHRs. For in-
stance, given a sentence L = [C0C1C2 . . . Cn−1Cn], where
Ci represents the i-th character, the separated form
is Ls = [C0, C1, C2, . . . , Cn−1, Cn], and we obtain the
character embeddings by converting character indexes
into ﬁxed dimensional dense vectors. Afterwards, to
capture interactions between adjacent characters, bi-
gram embeddings are utilized to feature the coherence
Algorithm 1: NE-LP based Active Learning for
Chinese Word Segmentation
Input: labeled data L, unlabeled data U, the number
of iterations M, the number of samples
selected per iteration n, partitioning function
Split, size τ
Output: a word segmentation model f ∗with the
smallest testing set loss lmin
1 begin
2
Initialize: Trainingτ, Testingτ ←Split(L, τ)
3
train a joint model with a word
segmenter fτ and a loss prediction model tτ
4
estimate the testing set loss lτ on fτ
5
label U by fτ
6
for i = 1 to M do
7
for Sample ∈U do
8
compute UncertaintySample from the
output of f and predict LossSample by t
9
calculate the sum of UncertaintySample
and LossSample according to a certain
weight
10
end
11
select n-highest ranking samples R
12
relabel R by annotators
13
form a new labeled dataset
TrainingR ←Trainingτ
S{R}
14
form a new unlabeled dataset UR ←Uτ\{R}
15
train a joint model with fR and tR
16
estimate the new testing loss lR on fR
17
compute the loss reduction δR ←lR −lτ
18
if δR < 0 then
19
lmin ←lR
20
end
21
else
22
lmin ←lτ
23
end
24
end
25
f ∗←f with the smallest testing set loss lmin
26 end
27 return f ∗
over characters. We construct the bigram feature for
each character by concatenating it with the previous
character, i.e., B = [x0x1, x1x2, . . . , xt−1xt]. We employ
Word2Vec [10] to train bigram features to get bigram
embedding vectors. Then, we concatenate the charac-
ter embeddings and bigram embeddings as the input
of BiLSTM layer. Finally, CRF layer makes positional
tagging decisions over individual characters, and self-
attention layer learns to simulate the loss deﬁned in
the base model.
3.2 BiLSTM-CRF based Word Segmenter
CWS can be formalized as a sequence labeling problem
with character position tags, which are (‘B’, ‘M’, ‘E’,
‘S’), so we convert the labeled data into the ‘BMES’
format, in which each character in the sequence is as-
signed with a label as follows: B=beginning of a word,


## Page 5


Title Suppressed Due to Excessive Length
5
Bigram 
Embeddings
Word2Vec
x x!
⏻ᐤ
x!x"
ᐤ㔃
x"x#
㔃ᵚ
x#x$
ᵚ㿱
x$x%
㿱᰾
x%x&
᰾ᱮ
x%x&
ᱮ㛯
x&x'
㛯བྷ
Concatenated 
Embeddings
Embedding Layer
x 
⏻
x!
ᐤ
x"
㔃
x#
ᵚ
x$
㿱
x%
᰾
x&
ᱮ
x'
㛯
x(
བྷ
Character 
Embeddings
……
……
……
……
CRF Layer
B
M
E
B
E
E
E
B
B
Self-Attention Layer
a predicted loss
BiLSTM
Layer
Segmentation
Prediction
Loss
Prediction
Fig. 2 The detailed architecture of the joint model, where BiLSTM-CRF is employed as a word segmenter and BiLSTM-Self-
Attention is a loss prediction model. The loss prediction model shares BiLSTM layer parameters with word segmenter to learn
feature representations better for loss prediction.
M=middle of a word, E=end of a word and S=single
word. For example, a Chinese segmented sentence “病
人/长期/于/我院/心血管科/住院/治疗/。/” (The pa-
tient was hospitalized for a long time in the cardio-
vascular department of our hospital.) can be labeled
as ‘BEBESBEBMMEBEBES’. In this paper, we use
BiLSTM-CRF as the base model for CWS, which is
widely-used in sequence labeling.
3.2.1 BiLSTM Layer
LSTM is mainly an optimization for traditional Recur-
rent Neural Network (RNN). RNN is widely used to
deal with time-series prediction problems. The result of
its current hidden layer is determined by the input of
the current layer and the output of the previous hidden
layer [17]. Therefore, RNN can remember historical re-
sults. However, traditional RNN has vanishing gradient
and exploding gradient problems when training long se-
quences [2], and LSTM can eﬀectively solve these prob-
lems by adding a gated mechanism to RNN. Formally,
the LSTM unit performs the following operations at
time step t:
ft = σg (Wfxt + Ufht−1 + bf)
(4)
it = σg (Wixt + Uiht−1 + bi)
(5)
ot = σg (Woxt + Uoht−1 + bo)
(6)
ct = ct−1 ⊙ft + it ⊙σc (Wcxt + Ucht−1 + bc)
(7)
ht = σh (ct) ⊙ot
(8)
where xt, ct−1, h(t−1) are the inputs of LSTM, all W∗
and U∗are a set of parameter matrices, and b∗is a
set of bias parameter matrices. ⊙and σ operation rep-
resent matrix element-wise multiplication and sigmoid
function, respectively. In the LSTM unit, there are two
hidden layers (ht, ct), where ct is the internal memory
cell for dealing with vanishing gradient, while ht is the
main output of the LSTM unit for complex operations
in subsequent layers.
Obviously, the hidden state ht of the current LSTM
unit only relies on the previous hidden state ht−1, while
ignoring the next hidden state ht+1. However, future
information from the backward direction is also useful
to CWS [29]. BiLSTM, which consists of two LSTMs,
i.e., forward LSTM and backward LSTM, can capture
and merge features both from the forward and back-
ward direction of a sequence. Therefore, BiLSTM can
understand the syntactic and semantic context from a
deeper perspective than LSTM. Assume that the out-
put sequence of hidden states of the forward and back-
ward LSTM are −→
ht and ←−
ht, respectively, the context
vector can be denoted by concatenating the two hidden
vectors as ht=[−→
ht ; ←−
ht].


## Page 6


6
Tingting Cai et al.
3.2.2 CRF Layer
For CWS, it is necessary to consider the dependencies
of adjacent tags. For example, a B (Begin) tag should
be followed by an M (Middle) tag or an E (End) tag,
and cannot be followed by an S (Single) tag. Given the
observed sequence, CRF has a single exponential model
for the joint probability of the entire sequence of labels,
so it can solve the label bias problem eﬀectively, which
motivates us to use CRF to model the tag sequence
jointly, not independently [33].
A is an important parameter in CRF called a trans-
fer matrix, which can be set manually or learned by
model. Ayi,yi+1 denotes the transition probability from
label yi to yi+1. y∗represents the most likely tag se-
quence of x and it can be formalized as:
y∗= arg max
y
p(y|x; A)
(9)
3.3 Self-Attention based Loss Prediction Model
To select the most appropriate sentences in a large
number of unlabeled corpora, we attach a self-attention
based loss prediction model to the base word segmenter,
which is inspired by [38]. The word segmenter is learned
by minimizing the losses. If we can predict the losses of
input data, it is intuitive to choose samples with high
losses, which tend to be more beneﬁcial to current seg-
menter improvement.
3.3.1 Self-Attention Layer
The attention mechanism was ﬁrst proposed in the ﬁeld
of computer vision, and it is widely used in NLP tasks
in recent years, which imitates human beings to address
problems focusing on important information from big
data [28]. Attention mainly aims to map a query to a se-
ries of key-value pairs [4]. Formally, attention performs
the following three operations:
1. Calculate the similarity between query and each key
to get the weight coeﬃcient of the value correspond-
ing to each key, and then scale the dot products by
1
√dk :
f (Q, Ki) = QT Ki
√dk
(10)
where dk denotes the dimension of key and value.
Word Segmenter
Loss Prediction 
Model
Input Data
Segmentation 
Prediction
Loss Prediction
Segmentation 
ŶŶŽƚĂƚŝŽŶ
Segmentation 
Loss
Loss-Prediction-Model Loss
Fig. 3 The method for training loss prediction model. Given
an input, the word segmenter and loss prediction model out-
put a segmentation prediction and a predicted loss, respec-
tively. Next, a segmentation loss can be computed by the seg-
mentation prediction and annotation. Then, the segmentation
loss is regarded as a ground-truth loss for the loss prediction
model, and is used to compute the loss-prediction-model loss.
2. Normalize the weight coeﬃcient by softmax func-
tion:
ai = softmax (f (Q, Ki)) =
exp (f (Q, Ki))
PLen
j=1 exp (f (Q, Kj))
(11)
3. The ﬁnal attention is a weighted sum of weight co-
eﬃcients and values:
Attention(Q, K, V ) =
Len
X
i=1
ai ∗Vi
(12)
where Len is the length of the input sequence.
Self-attention mechanism is a special form of atten-
tion, where Q, K and V have the same value, i.e., each
token in the sequence will be calculated attention with
other remaining tokens. Self-attention can learn the in-
ternal structure of the sequence and it is more sensitive
to the diﬀerence between input and output, so we use
self-attention to learn the loss of word segmenter and we
deﬁne that a sequence with higher self-attention score
has higher loss.
3.3.2 Loss Learning
Fig. 3 shows a detailed description of how to train the
loss prediction model. Given the input data x, the seg-
mentation prediction can be obtained through the word
segmenter: spre = Seg(x). Similarly, we can get the loss
prediction through the loss prediction model: losspre =
Loss(x). Next, the segmentation loss can be computed
as: lossSeg = LSeg(spre, strue), where strue represents
the true annotation of x. Then, lossSeg is regarded as a
ground-truth target for loss prediction model, so we can
compute the loss of loss prediction model as lossLoss =


## Page 7


Title Suppressed Due to Excessive Length
7
LLoss(losspre, lossSeg). The ﬁnal loss function of the
joint model is deﬁned as:
Ljoint = LSeg(spre, strue) + λLLoss(losspre, lossSeg)
(13)
where λ represents the weight coeﬃcient. In the follow-
ing part, we empirically set λ to 1.
When training the loss prediction model, we seek to
minimize the segmentation loss and the predicted loss:
LLoss = 1
n
n
X
i=1
[losspre −lossSeg]2
(14)
where n means the number of samples.
3.4 NE-LP Sampling Strategy
To judge whether the samples are eﬀective to improve
the model performance, we combine the normalized en-
tropy of segmentation prediction with loss prediction.
The former measures the uncertainty, which can be
computed as Equation (15), while the latter takes seg-
mentation loss into consideration.
Uncertainty(x) =
PN
i=1 pSeg(x) log pSeg(x)
log 1
N
√
Len
(15)
where pSeg represents the output probability of word
segmenter, and N denotes the number of labeled classes.
To ensure that the normalized entropy and loss are in
the same order of magnitude, we scale the normalized
entropy by
1
√
Len, where Len is the length of the input
sequence.
For CWS, we hypothesize that if a sample has both
high uncertainty and high loss, it is probably infor-
mative to the current word segmenter, and we verify
this assumption in our experiments. Therefore, the ﬁ-
nal sampling strategy NE-LP can be formalized as:
SNE−LP (x) = α
PN
i=1 pSeg(x) log pSeg(x)
log 1
N
√
Len
+ βLoss(x)
(16)
where α and β are the weight coeﬃcients of normalized
entropy and loss prediction, respectively.
Table 1 Detailed Information of EHRs.
Types
Counts
Contents
Hospital records
957
Admission date,
history of present illness.
Medical records
992
Chief complaints,
physical examination.
Ward round records
952
General, heart rate,
laboratory ﬁndings.
Discharged records
967
Treatment plans,
date of discharge.
Table 2 Statistics of Datasets.
Datasets
Sentences
Words
Characters
Training set
16465
400878
706362
Initial labeled set
4950
120699
212598
Unlabeled set
11525
280179
493764
Testing set
5489
131624
233759
Validation set
5489
135406
238954
4 Experiments & Analysis
4.1 Datasets
We collect 204 EHRs with cardiovascular diseases from
the Shuguang Hospital Aﬃliated to Shanghai Univer-
sity of Traditional Chinese Medicine and each contains
27 types of records. We choose 4 diﬀerent types with
a total of 3868 records from them, which are hospital
records, medical records, ward round records and dis-
charge records. The detailed information of EHRs are
listed in Table 1.
We divide 3868 records including 27442 sentences
into training set, testing set and validation set with the
ratio of 6:2:2. Then, we randomly select 4950 sentences
from training set as initial labeled set, and the remain-
ing 11525 sentences as unlabeled set, i.e., we obtain the
initial labeled set and unlabeled set by splitting the
training set according to the ratio of 3:7. Statistics of
datasets are listed in Table 2.
4.2 Parameter Settings
Hyper-parameter conﬁguration may have a great im-
pact on the performance of neural network. The hyper-
parameter conﬁgurations of our method are listed in
Table 3.
We initialize bigram embeddings via Word2Vec on
the whole datasets. The dimension of character embed-
dings is set as same as the bigram embeddings. Then,
we concatenate two embeddings with the dimsension of
256 as the input of BiLSTM layer. BiLSTM hidden unit
number is twice the dimension of concatenated embed-


## Page 8


8
Tingting Cai et al.
Table 3 Hyper-parameter Setting.
Hyper-parameters
Setting
Maximum sequence length
len = 200
Character embedding dimension
dcha = 128
Bigram embedding dimension
dbig = 128
Concatenated embedding dimension
dcon = 256
BiLSTM hidden unit number
nhid = 512
Dropout rate
rate = 0.2
Table
4 Experimental Results of Diﬀerent Open-source
CWS Tools.
CWS tools
Precision
Recall
F1-score
SnowNLP
59.4
56.68
58.04
PyHanLP
65.01
70.89
67.82
Jieba
70.36
71.48
70.91
THULAC
68.67
77.36
72.76
PyNLPIR
69.14
76.89
72.81
FoolNLTK
72.85
76.98
74.86
pkuseg
78.93
75.86
77.37
dings. Dropout [27] is applied to the outputs of BiLSTM
layer in order to prevent our model from overﬁtting.
In active learning, we ﬁx the number of iterations
at 10 since each sampling strategy does not improve
obviously after 10 iterations. At each iteration, we select
1000 sentences from unlabeled data for joint model to
learn.
4.3 Experimental Results
4.3.1 Comparisons between Diﬀerent Open-source
CWS Tools
We select seven widely-used and mainstream open-source
CWS tools from the Internet, which are SnowNLP1, Py-
HanLP2, Jieba3, THULAC4, PyNLPIR5, FoolNLTK6
and pkuseg7. We evaluate them on our datasets with a
total of 27443 sentences.
As shown in Table 4, we ﬁnd that pkuseg performs
the best with the F1-score of 77.37% while SnowNLP
shows the lowest of 58.04%, and THULAC has the high-
est recall of 77.36%. However, since these open-source
tools are trained by general domain corpora, when ap-
plied to speciﬁc ﬁelds, such as medical domain, the re-
sults are still not satisfactory. Therefore, we need to
train a new segmenter on medical texts.
1 https://github.com/isnowfy/snownlp
2 https://github.com/hankcs/pyhanlp
3 https://github.com/fxsjy/jieba
4 https://github.com/thunlp/THULAC-Python
5 https://github.com/tsroten/pynlpir
6 https://github.com/rockyzhengwu/FoolNLTK
7 https://github.com/lancopku/pkuseg-python
4.3.2 Comparisons between Diﬀerent Models for CWS
To select a base word segmenter that is most suitable
for medical texts, we compare diﬀerent types of mod-
els including both statistical machine learning and deep
learning. These models are trained on the whole train-
ing set with 20 epoches. The results are listed in TA-
BLE 5.
All deep neural networks obtain higher F1-score than
statistical machine learning model CRF by the margins
between 2.35% and 11.84% since neural networks can
eﬀectively model feature representations.
We further observe that self-attention-CRF shows
relatively low F1-score of 86.48% since only a single
self-attention layer cannot extract useful feature repre-
sentations. Thus, to capture more features, we employ
Transformer-CRF, i.e., we use the encoder part of the
model proposed by [31] as the feature extractor, which
is composed of a multi-head attention sub-layer and
a position-wise fully connected feed-forward network.
Results show that Transformer-CRF has an F1-score
of 91.25%, which is a 4.77% improvement compared to
self-attention-CRF.
Among bi-directional RNNs, BiLSTM-CRF shows
a highest F1-score of 95.89%, while BiRNN-CRF and
BiGRU-CRF achieve 95.30% and 95.71%, respectively.
BiLSTM and BiGRU are optimizations for BiRNN since
they introduce gated mechanism to solve the problem
of long-distance dependencies, where BiLSTM contains
three gates, which are forget, input and output gates,
while BiGRU has two gates, which are reset and update
gates.
Furthermore, we notice that BiLSTM-CRF outper-
forms LSTM-CRF by the margins of 2.78%, which shows
that BiLSTM can understand the syntactic and seman-
tic contexts better than LSTM. Compared to CNN-
CRF, the F1-score of BiLSTM-CRF improves by 1.74%.
However, CNN is able to extract more local features,
while BiLSTM may ignore some key local contexts im-
portant for CWS when modeling the whole sentence.
Therefore, when combining BiLSTM and CNN as fea-
ture extractor, the F1-score reaches the peak of 95.97%,
which outperforms BiLSTM-CRF by a small margin of
0.08%.
Given the above experimental results, considering
the computational cost, complextity of model architec-
ture and ﬁnal results, we adopt BiLSTM-CRF as our
base segmenter since the performance does not improve
greatly when incorporating CNN, but it costs more time
due to a more complex architecture.


## Page 9


Title Suppressed Due to Excessive Length
9
Table 5 Experimental Results of Diﬀerent Models for CWS.
Model
Precision
Recall
F1-score
CRF
83.39
84.88
84.13
Self-Attention-CRF
85.74
87.23
86.48
Transformer-CRF
90.72
91.78
91.25
LSTM-CRF
92.76
93.46
93.11
CNN-CRF
93.73
94.58
94.15
BiRNN-CRF
94.90
95.71
95.30
BiGRU-CRF
95.36
96.06
95.71
BiLSTM-CRF
95.81
95.97
95.89
CNN-BiLSTM-CRF
95.77
96.18
95.97
Table 6 Experimental Results with Diﬀerent N-gram Fea-
tures in BiLSTM-CRF.
Model + feature
Precision
Recall
F1-score
BiLSTM-CRF
95.81
95.97
95.89
BiLSTM-CRF + Four-gram
96.72
96.70
96.71
BiLSTM-CRF + Trigram
97.19
97.44
97.32
BiLSTM-CRF + Bigram
97.59
97.80
97.70
4.3.3 Eﬀectiveness of N-gram Features in
BiLSTM-CRF based Word Segmenter
To investigate the eﬀectiveness of n-gram features in
BiLSTM-CRF based word segmenter, we also compare
diﬀerent n-gram features on EHRs. The results are shown
in Table 6.
By using additional n-gram features in BiLSTM-
CRF based word segmenter, there is an obvious im-
provement of F1-score, where bigram features achieve
97.70% while trigram and four-gram reach 97.32% and
96.71%, respectively. Speciﬁcally, bigram, trigram and
four-gram features outperform character-only features
by margins of 1.81%, 1.43% and 0.82%, which indicates
that n-gram features can eﬀectively capture the seman-
tic coherence between characters.
Furthermore, we explore the reason why bigram fea-
tures perform better than trigram and four-gram. We
analyze the number of words consisting of 2, 3 and 4
characters in our datasets. As shown in Table 7, we
ﬁnd the reason that yields such a phenomenon is that 2-
character words appear most often in datasets, with the
appearance of 147143, 48717 and 49413 times in train-
ing, testing and validation set, respectively. Therefore,
in our texts, bigram features can eﬀectively capture the
likelihood of 2 characters being a legal word, and they
are most beneﬁcial to model performance improvement.
Given the experimental results, we use bigram as
additional feature for BiLSTM-CRF based word seg-
menter.
Table 7 Statistics of words whose characters are of diﬀerent
lengths.
N-character words
Training set
Testing set
Val set
N = 2
147143
48717
49413
N = 3
30379
10043
10385
N = 4
8187
2707
2857
Fig. 4 Comparisons between diﬀerent weight coeﬃcients of
normalized entropy and loss prediction.
4.3.4 Comparisons between Diﬀerent Weight
Coeﬃcients of Normalized Entropy and Loss
Prediction
To study which part has more inﬂuence on the ﬁnal per-
formance, we conduct an experiment on diﬀerent weight
coeﬃcients of normalized entropy and loss prediction
with bigram features. We compare ﬁve diﬀerent groups
of parameters in Equation (16).
From the learning curves of Fig. 4, it is clear that
when the weight coeﬃcients α and β are all set to 1,
the results are better than others in early iterations,
and then tend to be uniform, except for the coeﬃcients
of 1 and 100.
Furthermore, we ﬁnd that, when α and β are 100
and 1, i.e., we enlarge the eﬀect of loss prediction, the
F1-scores are higher than the results when α and β are
1 and 100. We believe the reason is that loss predic-
tion is task-agnostic as the model is learned from losses
regardless of target tasks while normalized entropy is
more eﬀective to the task like classiﬁcation, which is
learned to minimize cross-entropy between predictions
and labels.
When the weight coeﬃcients α and β are all set
to 1, respectively, the performance is the best, which
shows that combining two parts together can make full
use of respective advantages to achieve better results,


## Page 10


10
Tingting Cai et al.
thus we choose this group of parameters for subsequent
experiments.
4.3.5 Comparisons between Diﬀerent Sampling
Strategies
In this experiment, we compare the conventional sam-
pling strategies introduced in Section 2 with our pro-
posed method NE-LP, as well as the uniformly ran-
dom baseline (RAND). We evaluate the performance
of strategy by its F1-score on the testing set. To prove
the eﬀectiveness of our proposed method, we conduct
our experiments in two conﬁgurations: adding addi-
tional bigram features and using character-only fea-
tures. For each iteration, we train 30 epoches with bi-
gram features, which is a good trade-oﬀbetween speed
and performance, while 50 epoches without bigram fea-
tures to ensure model convergence.
As illustrated in Fig. 5, all sampling strategies per-
form better than RAND baseline. From the left of
Fig. 5, we ﬁnd that LC and MTE greatly outperform
MTM in early rounds while from the right of Fig. 5,
we notice that MTE works very eﬀectively with the bi-
gram features, but LC suﬀers from performance drop.
The reason may be that, on the inﬂuence of bigram fea-
tures, LC is not accurate enough to localize the best
token to label.
Furthermore, we observe that the F1-scores improve
greatly when adding bigram features, which again indi-
cates the eﬀectiveness of bigram features.
Regardless of whether to add bigram features, our
approach NE-LP shows the best performance for all
active learning cycles. The performance gaps between
our method NE-LP and entropy-based MTE are ob-
vious since NE-LP not only captures the uncertainty
of sequences, but also takes segmentation losses into
consideration.
4.3.6 Comparisons between Diﬀerent Sampling
Strategies with Diﬀerent Sizes of Initial labeled Set
Furthermore, we also investigate the eﬀects of diﬀerent
initial labeled set sizes on the ﬁnal performance. Instead
of using the ratio of 3:7, we now divide the training set
with the ratio of 1:9 to get the initial labeled set and
unlabeled set.
As depicted in Fig. 6, we ﬁnd that our proposed
method NE-LP still outperforms other uncertainty-
based sampling strategies at all iterations, which shows
that our method can always select informative samples
beneﬁcial to current model improvement regardless of
the size of initial labeled set.
The performance trends of these sampling strategies
are similar to those in Fig. 5. NE-LP shows the best
performance, MTE achieves better F1-scores than LC
and MTM while RAND obtains the lowest results.
However, the performance gaps between NE-LP
and MTE are less obvious than Fig. 5 since when the
ratio is 1:9, losses tend to be smaller than those with
the ratio of 3:7. Therefore, in NE-LP, compared to loss
prediction, normalized entropy has a greater impact on
performance, leading to the phenomenon that the F1-
score curve of NE-LP is close to MTE. However, de-
spite the small gaps, NE-LP outperforms MTE any-
way. Therefore, we still can’t ignore the importance of
loss prediction since it also plays a role to improve the
performance.
5 Conclusion and Future Work
To relieve the eﬀorts of EHRs annotation, we propose
an eﬀective word segmentation method based on active
learning with a novel sampling strategy called NE-LP.
NE-LP eﬀectively utilizes the output of a joint model
and combines normalized entropy with self-attention
based loss prediction. Compared to the widely-used and
mainstream uncertainty-based sampling methods, our
sampling strategy selects samples from statistical per-
spective and deep learning level. In addition, to cap-
ture coherence between characters, we further add bi-
gram features to the joint model. Based on EHRs col-
lected from the Shuguang Hospital Aﬃliated to Shang-
hai University of Traditional Chinese Medicine, we eval-
uate our method on CWS. Compared to conventional
uncertainty-based sampling strategies, NE-LP achieves
best performance, which proves the eﬀectiveness of our
method to a certain extent.
As possible research directions, we plan to employ
other highly performant pre-trained neural networks,
such as Bert and GPT for EHRs segmentation. Then,
considering the characteristics of CWS task and model,
we believe that our method can also be applied to other
tasks, such as NER and relation extraction.
Acknowledgements We kindly thank Ju Gao from Shuguang
Hospital Aﬃliated to Shanghai University of Traditional Chi-
nese Medicine for providing us clinical datasets, and Ping He
from Shanghai Hospital Development Center for her help.
This work was supported by the National Natural Science
Foundation of China (No. 61903144) and the National Key
R&D Program of China for “Precision medical research” (No.
2018YFC0910550).


## Page 11


Title Suppressed Due to Excessive Length
11
Fig. 5 Comparisons between diﬀerent sampling strategies when the ratio of initial labeled set and unlabeled set is 3:7.
Fig. 6 Comparisons between diﬀerent sampling strategies when the ratio of initial labeled set and unlabeled set is 1:9.
Compliance with ethical standards
Conﬂict of interest No conﬂict of interest exits in the
submission of this manuscript.
References
1. Angluin, D.: Queries and concept learning.
Machine
Learning 2(4), 319–342 (1988)
2. Bengio, Y., Simard, P., Frasconi, P., et al.: Learning
long-term dependencies with gradient descent is diﬃcult.
IEEE Transactions on Neural Networks 5(2), 157–166
(1994)
3. Chen, X., Qiu, X., Zhu, C., Liu, P., Huang, X.: Long
short-term memory neural networks for Chinese word
segmentation.
In: Proceedings of the 2015 Conference
on Empirical Methods in Natural Language Processing,
pp. 1197–1206 (2015)
4. Cheng, K., Yue, Y., Song, Z.: Sentiment classiﬁcation
based on part-of-speech and self-attention mechanism.
IEEE Access 8, 16387–16396 (2020)
5. Collobert,
R., Weston, J., Bottou,
L., Karlen, M.,
Kavukcuoglu, K., Kuksa, P.: Natural language process-
ing (almost) from scratch. Journal of Machine Learning
Research 12(Aug), 2493–2537 (2011)
6. Eddy, S.R.: Proﬁle hidden markov models. Bioinformat-
ics (Oxford, England) 14(9), 755–763 (1998)
7. Gan, L., Zhang, Y.: Investigating self-attention net-
work for Chinese word segmentation.
arXiv preprint
arXiv:1907.11512 (2019)
8. Gesulga, J.M., Berjame, A., Moquiala, K.S., Galido, A.:
Barriers to electronic health record system implementa-
tion and information systems resources: A structured re-
view. Procedia Computer Science 124, 544–551 (2017)


## Page 12


12
Tingting Cai et al.
9. Gilad-Bachrach, R., Navot, A., Tishby, N.: Query by
committee made real. In: Advances in neural informa-
tion processing systems, pp. 443–450 (2006)
10. Goldberg, Y., Levy, O.: Word2Vec explained: deriv-
ing mikolov et al.’s negative-sampling word-embedding
method. arXiv preprint arXiv:1402.3722 (2014)
11. Houlsby, N., Husz´ar, F., Ghahramani, Z., Lengyel, M.:
Bayesian active learning for classiﬁcation and preference
learning. arXiv preprint arXiv:1112.5745 (2011)
12. Hu, P., Lipton, Z.C., Anandkumar, A., Ramanan, D.:
Active learning with partial feedback. In: International
Conference on Learning Representations (2018)
13. Huang, H., Wang, H., Jin, D.: A low-cost named entity
recognition research based on active learning. Scientiﬁc
Programming 2018, 1–10 (2018)
14. Jiang, W., Tang, Y.: A seq-to-seq transformer premised
temporal convolutional network for Chinese word seg-
mentation. arXiv preprint arXiv:1905.08454 (2019)
15. La Su, Y., Liu, W.: Research on the lstm mongolian and
chinese machine translation based on morpheme encod-
ing. Neural Computing and Applications 32(1), 41–49
(2020)
16. Laﬀerty, J.D., McCallum, A., Pereira, F.C.: Conditional
random ﬁelds: Probabilistic models for segmenting and
labeling sequence data. In: Proceedings of the Eighteenth
International Conference on Machine Learning, pp. 282–
289 (2001)
17. Lei, L., Zhou, Y., Zhai, J., Zhang, L., Fang, Z., He,
P., Gao, J.: An eﬀective patient representation learn-
ing for time-series prediction tasks based on ehrs.
In:
IEEE International Conference on Bioinformatics and
Biomedicine, pp. 885–892. IEEE (2018)
18. Lewis, D.D., Gale, W.A.: A sequential algorithm for
training text classiﬁers. In: Proceedings of the 17th An-
nual International Conference on Research and Develop-
ment in Information Retrieval, pp. 3–12. Springer (1994)
19. Li, S., Zhou, G., Huang, C.R.: Active learning for Chi-
nese word segmentation. In: Proceedings of International
Conference on Computational Linguistics 2012: Posters,
pp. 683–692 (2012)
20. Liu, J., Wu, F., Wu, C., Huang, Y., Xie, X.: Neural chi-
nese word segmentation with dictionary. Neurocomput-
ing 338, 46–54 (2019)
21. Liu, M., Tu, Z., Wang, Z., Xu, X.: LTP: A new ac-
tive learning strategy for Bert-CRF based named entity
recognition. arXiv preprint arXiv:2001.02524 (2020)
22. Ma, J., Ganchev, K., Weiss, D.: State-of-the-art Chinese
word segmentation with bi-lstms. In: Proceedings of the
2018 Conference on Empirical Methods in Natural Lan-
guage Processing, pp. 4902–4908 (2018)
23. Marcheggiani, D., Artieres, T.: An experimental com-
parison of active learning strategies for partially labeled
sequences.
In: Proceedings of the 2014 Conference on
Empirical Methods in Natural Language Processing, pp.
898–906 (2014)
24. Peng, F., Feng, F., McCallum, A.: Chinese segmentation
and new word detection using conditional random ﬁelds.
In: Proceedings of the 20th international conference on
Computational Linguistics, pp. 562–568. Association for
Computational Linguistics (2004)
25. Shao, D., Zheng, N., Yang, Z., Chen, Z., Xiang, Y., Xian,
Y., Yu, Z.: Domain-speciﬁc Chinese word segmentation
based on bi-directional long-short term memory model.
IEEE Access 7, 12993–13002 (2019)
26. Song, H., Yao, T., Kit, C., Cai, D.: Active learning based
corpus annotation. In: CIPS-SIGHAN Joint Conference
on Chinese Language Processing (2010)
27. Srivastava, N., Hinton, G., Krizhevsky, A., Sutskever, I.,
Salakhutdinov, R.: Dropout: a simple way to prevent neu-
ral networks from overﬁtting. Journal of Machine Learn-
ing Research 15(1), 1929–1958 (2014)
28. Sun, D., Yaqot, A., Qiu, J., Rauchhaupt, L., Jumar, U.,
Wu, H.: Attention-based deep convolutional neural net-
work for spectral eﬃciency optimization in mimo sys-
tems. Neural Computing and Applications (2020)
29. Tang, P., Yang, P., Shi, Y., Zhou, Y., Lin, F., Wang,
Y.: Recognizing Chinese judicial named entity using
BiLSTM-CRF. arXiv preprint arXiv:2006.00464 (2020)
30. Tang, X., Du, B., Huang, J., Wang, Z., Zhang, L.: On
combining active and transfer learning for medical data
classiﬁcation. Institution of Engineering and Technology
Computer Vision 13(2), 194–205 (2018)
31. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J.,
Jones, L., Gomez, A.N., Kaiser,  L., Polosukhin, I.: Atten-
tion is all you need. In: Advances in Neural Information
Processing Systems, pp. 5998–6008 (2017)
32. Wang, C., Xu, B.: Convolutional neural network with
word embeddings for Chinese word segmentation. arXiv
preprint arXiv:1711.04411 (2017)
33. Wang, Q., Zhou, Y., Ruan, T., Gao, D., Xia, Y., He, P.:
Incorporating dictionaries into deep neural networks for
the Chinese clinical named entity recognition. Journal of
biomedical informatics 92, 103–133 (2019)
34. Xing, J., Zhu, K., Zhang, S.: Adaptive multi-task transfer
learning for Chinese word segmentation in medical text.
In: Proceedings of the 27th International Conference on
Computational Linguistics, pp. 3619–3630 (2018)
35. Xue, N., Shen, L.: Chinese word segmentation as lmr tag-
ging. In: Proceedings of the second SIGHAN workshop
on Chinese language processing-Volume 17, pp. 176–179.
Association for Computational Linguistics (2003)
36. Yan, Q., Wang, L., Li, S., Liu, H., Zhou, G.: Active
learning for Chinese word segmentation on judgements.
In: National CCF Conference on Natural Language Pro-
cessing and Chinese Computing, pp. 839–848. Springer
(2017)
37. Yang, J., Yu, Q., Guan, Y., Jiang, Z.: An overview of
research on electronic medical record oriented named en-
tity recognition and entity relation extraction. Acta Au-
tomatica Sinica 40(8), 1537–1562 (2014)
38. Yoo, D., Kweon, I.S.: Learning loss for active learning. In:
Proceedings of the IEEE Conference on Computer Vision
and Pattern Recognition, pp. 93–102 (2019)
39. Zhao, H., Huang, C.N., Li, M., Lu, B.L.: Eﬀective tag
set selection in Chinese word segmentation via condi-
tional random ﬁeld modeling. In: Proceedings of the 20th
Paciﬁc Asia Conference on Language, Information and
Computation, pp. 87–94 (2006)
40. Zheng, X., Chen, H., Xu, T.: Deep learning for Chinese
word segmentation and pos tagging. In: Proceedings of
the 2013 Conference on Empirical Methods in Natural
Language Processing, pp. 647–657 (2013)

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
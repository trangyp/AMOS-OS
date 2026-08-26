---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1912.01109
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1912.01109_On_the_Vietnamese_Name_Entity_Recognition__A_Deep_Learning_Method_Approach

> Source: 1912.01109_On_the_Vietnamese_Name_Entity_Recognition__A_Deep_Learning_Method_Approach.pdf

> Pages: 5

---


## Page 1


On the Vietnamese Name Entity Recognition: A
Deep Learning Method Approach
Ngoc C. Lˆe
School of Applied Mathematics and Informatics
Hanoi University of Science and Technology
Institution of Mathematics
Vietnam Academy of Science and Technology
lechingoc@yahoo.com
Ngoc-Yen Nguyen
School of Applied Mathematics and Informatics
Hanoi Univ of Science and Technology
yen.nn154447@sis.hust.edu.vn
Anh-Duong Trinh
iCOMM Media & Tech, Jsc
duong.trinh@icomm.vn
Abstract—Named entity recognition (NER) plays an important
role in text-based information retrieval. In this paper, we combine
Bidirectional Long Short-Term Memory (Bi-LSTM) [7], [27] with
Conditional Random Field (CRF) [9] to create a novel deep
learning model for the NER problem. Each word as input of
the deep learning model is represented by a Word2vec-trained
vector. A word embedding set trained from about one million
articles in 2018 collected through a Vietnamese news portal
(baomoi.com). In addition, we concatenate a Word2Vec [18]-
trained vector with semantic feature vector (Part-Of-Speech
(POS) tagging, chunk-tag) and hidden syntactic feature vector
(extracted by Bi-LSTM nerwork) to achieve the (so far best)
result in Vietnamese NER system. The result was conducted
on the data set VLSP2016 (Vietnamese Language and Speech
Processing 2016 [29]) competition.
Index Terms—Vietnamese, Named Entity Recognition, Long
Short-Term Memory, Conditional Random Field, Word Embed-
ding
I. INTRODUCTION
Named-entity recognition (NER) (also known as entity iden-
tiﬁcation, entity chunking and entity extraction) is a subtask
of information extraction that seeks to locate and classify
named entity mentions in unstructured text into pre-deﬁned
categories such as the person names, organizations, locations,
medical codes, time expressions, quantities, monetary values,
percentages, etc . It is a fundamental NLP research problem
that has been studied for years. It is also considered as one
of the most basic and important tasks in some big problems
such as information extraction, question answering, entity
linking, or machine translation. Recently, there are many
novel ideal in NER task such as Cross-View Training (CVT)
[4], a semi-supervised learning algorithm that improves the
representations of a Bi-LSTM sentence encoder using a mix
of labeled and unlabeled data, or deep contextualized word
representation [24] and contextual string embeddings, a recent
type of contextualized word embedding that were shown to
yield state-of-the-art results [1], [2]. These studies have shown
new state-of-the-art methods with F1 scores on NER task.
In Vietnamese language, NER systems in VLSP 2016 adopted
either conventional feature-based sequence labeling models
such as Recurrent neural network (RNN), Bidirectional Long
Short Term Memory (Bi-LSTM) [25], Maximum-Entropy-
Markov Models (MEMMs) [14], [21], Conditional Random
Fields (CRFs) [11], [22]. For the VLSP 2016 data set, the ﬁrst
Vietnamese NER system has applied MEMMs with speciﬁc
features [25]. However, they have not achieved accuracy that
far beyond those of classical machine learning methods. Most
of the above models depends heavily on speciﬁc resources
and hand-crafted features, which makes it difﬁcult for those
models to apply to new domains and other tasks.
In [19], [20], the author used the information of word, word
shapes, part-of-speech tags, chunking tags as hand-crafted fea-
tures for CRF to label entity tags [23]. Over the past few years,
many deep learning models have been proposed to overcome
these limitations. Some NER models have used LSTM and
CRF to predict NER [8], [12]. In addition, beneﬁts from both
the expression of words and characters when combining CNN
and CRF are presented in [17], [28].
In this study, we introduce a deep neural network for Viet-
namese NER using extraction of morphological features au-
tomatically through a Bi-LSTM (character feature) network
combined with POS features - tagging and chunk tag. The
model includes two bidirectional-lstm hidden layer and an
output layer CRF. For Vietnamese language, we use the data
set from the 2016 VLSP contest. The results show that our
model outperforms the best previous systems for Vietnamese
NER [23] with F1 is 95.61% on test set.
The remainder of this paper is structured as follows. Section
II refers related work on named entity recognition. Section
III describes the implementation method. Section IV gives
experimental results and discussions. Finally, the conclusion
will be given in Section V.
II. RELATED WORK
The approaches for NER task can be divided into two rou-
tines: (1) statistical learning approaches and (2) deep learning
methods.
In the ﬁrst type, the authors used traditional labeling models
such as crf, hidden markov model, support vector machine,
maximum entropy that are heavily dependent on hand-crafted
features. Sentences are expressed in the form of a set of
features such as word, pos, chunk, etc Then they are put into
a linear model for labeling. Some examples following this
routine are [6], [13], [15], [16]. These models were proven to
arXiv:1912.01109v1  [cs.CL]  18 Nov 2019


## Page 2


work quite well for low existing resources languages such as
Vietnamese. However, these kinds of NER systems are relied
heavily on the used feature set, and on hand-crafted features
that are expensive to construct and are difﬁcultly reusable [23].
For the second routine, with the appearance of deep learning
models with superior computational performance seems to
improve the accuracy of the NER task. The performance of
deep learning models also have been shown much better than
the statistical based methods. In particular, the convolutional
neural network (CNN) [30], recurrent neural network (RNN),
LSTM networks are popular use, we can exploit the syntax
feature through character embedding in combination with
word embedding [26], [28]. Other information such as pos-
tag and chunk-tag is also used to provide more information
about semantic [3], [20], [25]. The word vectors are combined
in different ways, then feed into the Bi-LSTM network with
CRF in output. For Vietnamese, there are many NER systems
using LSTM network. In [25], the authors introduced a model
that uses two Bi-LSTM layers with softmax layers at the
output, with input from vectors using syntax speciﬁc, F1 score
is 92.05%. A model using single Bi-LSTM layer combining
crf at the output to achieve F1-score of 83.25% was given in
[22]. A number of high-precision models are introduced in the
[3] with Bi-LSTM-CRF model with the input is the extracted
vector with characteristic of word character, F1 is 94.88%. And
most recently, a combination of Bi-LSTM - attention layer -
CRF model with F1 score of 95.33% was given in [23].
III. METHODOLOGY
A. Feature engineering
Word embedding To build up a word embedding set, we
use the skip-gram neural network model, which is trained
from one million articles in 2018 through a Vietnamese
news portal (baomoi.com). Skip-gram is used to predict the
context word for a given target word. We choose sliding
window of Size 2, therefore, normally there are four context
words corresponding to a target word. For words that are not
trained, a vector called unknown (UNK) embedding is used
instead. The UNK embedding is created by random vectors
sampled uniformly from the range [−
q
3
dim, +
q
3
dim], where
the dimension (dim) is the dimension of word embeddings [3].
To improve the performance of our system, we use semantic
features to vectorize words into models (part of speech tagging
and chunk-tag). The pos-tagging vectors and chunk-tag vectors
were represented as one-hot vectors.
1) Character Embedding: Recently, automatically extract-
ing hidden features using neural networks (LSTM, CNN) used
in many articles, proved effective in the NER task [10]. In
this research, we use the Bi-LSTM network to extract hidden
patterns that characterize the syntax of words, as shown in
Fig. III-A1.
B. LSTM
LSTM networks are a type of Recurrent Neural Networks
(RNN) that uses special units in addition to standard units.
Fig. 1. Character-level Embedding
LSTM units contain a memory cell that can maintain in-
formation in memory for controlled periods of time. A cell
in the LSTM network consists of three control gates: forget
gate (determining which information is ignored and which is
retained), update gate (deciding how much of the memorized
information is added to the current state) and the output gate
(making the decision about which part of the current cell
makes it to the output). At time t, cell updates are given as
follows:
ft = σ (Wfht−1 + Ufxt + bf)
(1)
it = σ(Wiht−1 + Uixt + bi)
(2)
ot = σ(W0ht−1 + U0xt + b0)
(3)
∼c
t = tanh(Wcht−1 + Ucxt + bc)
(4)
ct = ft ⊙ct−1 + it ⊙
∼c
t
(5)
ht = ot ⊙tanh(ct),
(6)
where σ is the sigmoid function and ⊙is an pointwise
operator, which can be multiplication or addition or tanh
function, xt is the input vector at time t, ht is the hidden
state vector that holds information from the beginning to the
present time. The gates f, i, o, c are the forget gate, input gate,
output gate and cell vector respectively. The matrices Uf, Ui,
Uo, Uc are weight matrices that connect input and gates. The
matrices Wf, Wi, Wo, Wc are weight matrices that connect
gates and hidden state.
C. Bi-LSTM
In sequence labeling task, the context of a word is rep-
resented more effectively by the context, i.e. the companion
words, the left and right words in a sentence. To archive
these information, a candidate model is Bidirectional-LSTM
network as shown in Fig. III-C. Then, the output of the Bi-
LSTM network is observed by concatenating its left and right
context representations.


## Page 3


Fig. 2. Bidirectional - LSTM
D. Conditional Random Fields (CRFs)
For many sequence labeling tasks, a simple but effective
approach is consider the correlation between the labels close
together and the best sequence decoding with simple rules. The
conditional random ﬁeld is essentially a probability model,
which can predict labels with predeﬁned structures. Instead
of decoding independent labels, CRFs learn the sequence of
labels from train data to decode output labels at the same time.
In CRF, when given a word sequence x = (x1, x2, ..., xm), the
conditional probability of a tag sequence y = (y1, y2, ..., ym),
is deﬁned as in [19]:
P(y|x) =
exp(w.F(y, x))
P
y′∈Y exp(w.F(y′, x)),
(7)
where w is the parameter vector estimated from training data.
The feature function F(y, x) ∈IRd is deﬁned globally on an
entire input sequence and an entire tag sequence. Space Y is
the space of all possible tag sequences. The feature function
F(y, x) is calculated by summing local feature functions:
Fj(y, x) =
n
X
i=1
fj(yi−1, yi, x, i)
(8)
E. Our Deep Learning Model
For the NER labeling task for Vietnamese, we use multiple
Bi-LSTM layers with the CRF layer at the top to detect
entities named in the sequence [3], as shown in Fig. III-E.
The architecture operates as in the following sequence:
• The input of our neural network is sequence of word
representations
• Each word representation encoded through two Bi-LSTM
layers
• The CRF layer at the top to decode hidden feature vectors
from previous layer (Bi-LSTM layer)
IV. EXPERIMENTS
A. Datasets
To evaluate the model, we use dataset from VLSP-2016
NER task [29], with four types of entities including person
(PER), location (LOC), organization (ORG), miscellaneous
(MISC). In addition, VLSP-2016 dataset provides the infor-
mation about word segmentation, part-of-speech, and chunking
Fig. 3. Our Deep Learning model
tags. The number of sentences in train-set, validation-set and
test-set is shown in the T Table IV.
TABLE I
NUMBER OF SENTENCES
Dataset
Number of sentences
Train
14861
Validation
2000
Test
2831
The number of entities included in the train set and test set
is shown in the following table:
TABLE II
NUMBER OF LABELS IN DATASET
Type
Train
Test
Location
6245
1379
Organization
1213
274
Person
7480
1294
Miscellaneous names
282
49
Total
15220
2996
B. Hyper-parameters
Table IV-B summarizes the hyper-parameters that we have
chosen for our NER model. In order to have more efﬁcient
training process, the parameters are optimized using Nesterov-
accelerated Adaptive Moment Estimation (Nadam) optimizer
[5] with batch size 64. Word representation concatenated by
a 300 dimensional word2vec-vector (pre-trained from bao-
moi.com) and two one-hot vectors represent pos tags and
chunks, respectively and a 60 dimensional character vector
(generated from a bi-lstm network with dropout rate equal 0.3,
as shown in Figure 1). To prevent overﬁtting, we ﬁx dropout
rate to 0.5 for both Bi-LSTM layers (as shown in Figure 3).
The NER model is trained in 40 epoch. First 20 epochs, the
initial learning rate is set at 0.004. In the remaining epochs,
it is ﬁxed to 0.0004. The best model obtained when the value
of the loss function on validation-set is minimal.


## Page 4


TABLE III
THE MODEL HYPE-PARAMETERS
Hyper-parameter
Value
Character dimension
60
Word dimension
300
Hidden size char
30
Hidden size word
64
Update function
Nadam
Learning rate ﬁrst 20 0epoch
0.004
Learning rate last 20 epoch
0.0004
Dropout character embedding
0.3
Dropout two Bi-LSTM layers
0.5
Batch size
64
C. Experimental Results
The experiment is conducted by combining all input features
include pos-tag feature, chunk feature and character feature.
The results are shown in Table IV-C.
TABLE IV
RESULTS ON VLSP 2016 TEST-SET
Precision
Recall
F1-Score
LOC
95.43
96.95
96.18
PER
95.53
97.53
96.52
ORG
87.32
90.51
88.89
MISC
100.0
87.76
93.48
Avg/total
95.32
95.93
95.61
With VLSP 2016 dataset, the experiment achieved state-of-
the-art performances on Vietnamese NER task with 95.61%
F1-score. Table IV-C shows the performance of our deep
learning model and several published systems on NER task.
TABLE V
PERFORMANCES ON VLSP 2016 DATASET
Model
F1-Score
VNER[12]
95.33
Feature-based CRF [10]
93.93
NNVLP [9]
92.91
Nguyen et al. 2018 [21]
94.88
Our NER model
95.61
The general difference with other systems in Table 5 is that
we trained a new word embedding set by word2vec model,
described in Subsection III-A. Moreover, we use two Bi-LSTM
layers in order to encode word representations.
V. CONCLUSIONS
In this paper, we presented a neural network model for
Vietnamese named entity recognition task, which obtains state-
of-the-art performance. Experiments on recognize Vietnamese
entity in sequence labeling task showed the effectiveness
of training a new word embedding set and using two Bi-
LSTM layers in order to extract hidden features from word
representations. Our results is outperform the best previous
systems for Vietnamese Named entity recognition.
ACKNOWLEDGMENT
The ﬁrst author also has receive the support from Institute of
Mathematics, Vietnam Academy of Science and Technology,
Year 2019. This work is also supported by iCOMM Media &
Tech, Jsc. We would like to thank the iCOMM RnD team for
supported resources and text data that we used during training
and experiments our model.
REFERENCES
[1] A. Akbik, D. Blythe, and R. Vollgraf, Contextual String Embeddings
for Sequence Labeling, COLING 2018, 27th International Conference
on Computational Linguistics, pp. 1638–1649, 2018.
[2] A. Akbik, T. Bergmann, and R. Vollgraf, Pooled Contextualized Em-
beddings for Named Entity Recognition, Proceedings of the 2019
Conference of the North American Chapter of the Association for
Computational Linguistics: Human Language Technologies, Volume 1,
pp. 724–728, June 2019.
[3] D. N. Anh, H. N. Kiem, and V. N. Van, Neural sequence labeling
for Vietnamese POS Tagging and NER, 2019 IEEE-RIVF International
Conference on Computing and Communication Technologies (RIVF),
March 2019.
[4] K. Clark, M-T. Luong, C. D. Manning, and Q. V. Le, Semi-Supervised
Sequence Modeling with Cross-View Training, ICLR 2018, Feb. 16th
2018.
[5] T. Dozat, Incorporating Nesterov Momentum into Adam, International
Conference on Learning Representations 2016 (ICLR 2016).
[6] R. Florian, A. Ittycheriah, H. Jing, and T. Zhang, Named entity recog-
nition through classiﬁer combination, In Proceedings of the Seventh
Conference on Natural Language Learning at HLT-NAACL 2003 -
Volume 4, pp. 168–171, 2019.
[7] S. Hochreiter and Jrgen Schmidhuber, ”Long short-term memory”,
Neural Computation Vol. 9:8, pp. 1735-1780, 1997.
[8] Z. Huang, W. Xu, and K. Yu, Bidirectional LSTM-CRF Models for
Sequence Tagging, arXiv:1508.01991, Aug. 2015.
[9] J. Lafferty, A. McCallum, and F. Pereira, ”Conditional random ﬁelds:
Probabilistic models for segmenting and labeling sequence data”, In
Proceeding 18th International Conference on Machine Learning pp.
282-289, 2001.
[10] G. Lample, M. Ballesteros, S. Subramanian, K. Kawakami, and C. Dyer,
Neural Architectures for Named Entity Recognition, In Proceedings of
the 2016 Conference of the North American Chapter of the Association
for Computational Linguistics: Human Language Technologies, pp.260–
270, June 2016.
[11] T. H. Le, T. T. T. Nguyen, T. H. Do, and X. T. Nguyen, Named Entity
Recognition in Vietnamese Text, The Fourth International Workshop on
Vietnamese Language and Speech Processing (VLSP 2016), 2016.
[12] T.A. Le, M.Y. Arkhipov, and M.S. Burtsev, ”Application of a Hybrid Bi-
LSTM-CRF Model to the Task of Russian Named Entity Recognition”,
In: Artiﬁcial Intelligence and Natural Language, AINL 2017, Commu-
nications in Computer and Information Science, vol. 789, pp. 91–103,
2017.
[13] P. Le-Hong, A. Roussanaly, T. M. H. Nguyen, and M. Rossignol, An em-
pirical study of maximum entropy approach for part-of-speech tagging
of Vietnamese texts, Traitement Automatique des Langues Naturelles -
TALN 2010, ATALA (Association pour le Traitement Automatique des
Langues), Jul 2010, Montral, Canada, pp. 12–23, Oct 2010.
[14] P. Le-Hong, Vietnamese Named Entity Recognition using Token Regular
Expressions and Bidirectional Inference, In The Fourth International
Workshop on Vietnamese Language and Speech Processing (VLSP
2016), 2016.
[15] D. Lin and X. Wu, Phrase clustering for discriminative learning, ACL ’09
Proceedings of the Joint Conference of the 47th Annual Meeting of the
ACL and the 4th International Joint Conference on Natural Language
Processing of the AFNLP: Volume 2, pp. 1030–1038, 2009.
[16] G. Luo, X. Huang, C-Y. Lin, and Z. Nie, Joint Named Entity Recognition
and Disambiguation, Proceedings of the 2015 Conference on Empirical
Methods in Natural Language Processing, pp. 879–888, September
2015.
[17] X. Ma, and E. Hovy, End-to-end Sequence Labeling via Bi-directional
LSTM-CNNs-CRF, Proceedings of the 54th Annual Meeting of the
Association for Computational Linguistics, pp. 1064–1074, March 2016.


## Page 5


[18] T. Mikolov, K. Chen, G. Corrado, and J. D. Tomas, ”Efﬁcient Estimation
of Word Representations in Vector Space”, arXiv:1301.3781, 2013.
[19] P. Q. N. Minh, A Feature-Rich Vietnamese Named-Entity Recognition
Model, arXiv:1803.04375, 12 Mar 2018.
[20] P. Q. N. Minh, A Feature-Based Model for Nested Named Entity
Recognition at VLSP-2018 NER Evaluation Campaign, In Proceedings
of Vietnamese Speech and Language Processing (VLSP), 2018.
[21] T. C. V. Nguyen, T. S. Pham, T. H. Vuong, N. V. Nguyen, and M. V.
Tran, Dsktlab-ner: Nested named entity recognition in vietnamese text,
In The Fourth International Workshop on Vietnamese Language and
Speech Processing (VLSP 2016), 2016.
[22] T. S. Nguyen, L. M. Nguyen, and X. C. Tran, Vietnamese named entity
recognition at vlsp 2016 evaluation campaign, In Proceedings of The
Fourth International Workshop on Vietnamese Language and Speech
Processing, 2016.
[23] K. A. Nguyen, N. Dong, and C-T. Nguyen, Attentive Neural Network
for Named Entity Recognition in Vietnamese, 2019 IEEE-RIVF Inter-
national Conference on Computing and Communication Technologies
(RIVF), March 2019.
[24] M. Peters, M. Neumann, M. Iyyer, M. Gardner, C. Clark, K. Lee,
and Luke Zettlemoyer, Deep contextualized word representations, Pro-
ceedings of the 2018 Conference of the North American Chapter
of the Association for Computational Linguistics: Human Language
Technologies, Volume 1, June 2018.
[25] T-H. Pham and P. Le-Hong, The Importance of Automatic Syntactic
Features in Vietnamese Named Entity Recognition, The 31st Paciﬁc
Asia Conference on Language, Information and Computation, November
2017.
[26] T-H. Pham, X-K. Pham, T-A. Nguyen, and P. Le-Hong, NNVLP: A
Neural Network-Based Vietnamese Language Processing Toolkit, In
The Companion Volume of the IJCNLP 2017 Proceedings: System
Demonstrations, pp. 37-40, 2017.
[27] M. Schuster and K. K. Paliwal. ”Bidirectional recurrent neural net-
works”, Signal Processing, IEEE Transactions, Vol. 45.11, pp. 2673–
2681, 1997.
[28] F. Wu, J. Liu, C. Wu, Y. Huang, and X. Xie, Neural Chinese Named
Entity Recognition via CNN-LSTM-CRF and Joint Training with Word
Segmentation, The World Wide Web Conference, pp. 3342–3348, Apr.
2019.
[29] http://vlsp.org.vn/resources-vlsp2016
[30] W. Zhang. ”Shift-invariant pattern recognition neural network and its
optical architecture”, Proceedings of Annual Conference of the Japan
Society of Applied Physics, pp. 734, Sept. 1988.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1912_01109_on_the_vietnamese_name_entity_recognition_a_deep_learning_method_approach
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1912_01109_ON_THE_VIETNAMESE_NAME_ENTITY_RECOGNITION_A_DEEP_LEARNING_METHOD_APPROACH.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

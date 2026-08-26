---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1811.03754
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1811.03754_Neural_sequence_labeling_for_Vietnamese_POS_Tagging_and_NER

> Source: 1811.03754_Neural_sequence_labeling_for_Vietnamese_POS_Tagging_and_NER.pdf

> Pages: 5

---


## Page 1


Neural sequence labeling for Vietnamese
POS Tagging and NER
Anh-Duong Nguyen
Hanoi Univ of Science and Technology
Hanoi, Vietnam
20160840@student.hust.edu.vn
Kiem-Hieu Nguyen
Hanoi Univ of Science and Technology
Hanoi, Vietnam
hieunk@soict.hust.edu.vn
Van-Vi Ngo
VCCorp
Hanoi, Vietnam
vingovan@admicro.vn
Abstract—This paper presents a neural architecture for Viet-
namese sequence labeling tasks including part-of-speech (POS)
tagging and named entity recognition (NER). We applied the
model described in [8] that is a combination of bidirectional
Long-Short Term Memory and Conditional Random Fields,
which rely on two sources of information about words: character-
based word representations learned from the supervised corpus
and pre-trained word embeddings learned from other unanno-
tated corpora. Experiments on benchmark datasets show that
this work achieves state-of-the-art performances on both tasks -
93.52% accuracy for POS tagging and 94.88% F1 for NER. Our
sourcecode is available at here.
Index Terms—sequence labeling , part-of-speech tagging,
named-entity recognition, character-level knowledge, syntactic
information
I. INTRODUCTION
Linguistic sequence tagging is a well studied yet challenging
problem in natural language processing. Most traditional high
performance sequence tagging systems apply supervised learn-
ing techniques such as Hidden Markov Models, Maximum en-
tropy Markov models, and Conditional Random Fields (CRFs)
[23] [19] [12], which require large amounts of hand-crafted
features and domain-speciﬁc knowledge. For example, se-
quence taggers beneﬁt from carefully constructed word-shape
features; external language-speciﬁc knowledge resources such
as gazetteers are also widely used for solving NER task.
However, such task-speciﬁc knowledge are inherently limited
and can be costly to develop, making these models difﬁcult to
adapt to new languages or new domains.
Recently, deep learning has been extensively applied to
sequence tagging in many languages, and the focus has shifted
from feature engineering to designing and implementing effec-
tive neural network architectures [8] [13] [5].
There are several work applying deep learning to sequence
tagging in Vietnamese [22] [16] [20]. However, they have not
achieved accuracy that far beyond that of classical machine
learning methods. In this paper, we demonstrate the success
of applying a neural architecture for sequence labeling to
Vietnamese. The model requires no task-speciﬁc resources,
hand-engineered, or data pre-processing beyond pre-trained
word embeddings on unannotated corpora [8]. The model ﬁrst
uses bidirectional Long-Short Term Memory units (Bidirec-
tional LSTM) to learn character embeddings. Next, charac-
ter representation is concatenated with the pre-trained word
embeddings and then applying dropout [26] to encourage the
model to learn to trust both sources of evidence, then feed them
into a bidirectional LSTM to capture context information of
each word. On top of bidirectional LSTM, sequential CRFs
are used to jointly decode labels for the whole sentence.
Experiments on benchmark datasets show that we obtain state-
of-the-art results on both tasks - 93.52% accuracy for POS
tagging and 94.88% F1 for NER.
The main contributions of this paper are three-fold:
• We demonstrate the effectiveness of leveraging character-
level knowledge for language representations.
• We apply a neural sequence labeling system for Viet-
namese that outperforms traditionally machine learning
methods and other deep learning models.
• We release all code to the research community.
II. RELATED WORK
As mentioned earlier, we can basically categorize main
approaches to sequence tagging into feature-based machine
learning models and deep learning models.
The ﬁrst approach includes traditional models that rely
heavily on hand-crafted features and domain-speciﬁc knowl-
edge. For Vietnamese, previously published sequence labeling
systems used traditional machine learning methods such as
CRFs [14] and MEMM [11], [14]. Recently, several partici-
pants at the VLSP 2016 workshop for NER task use MEMM
[10] and CRFs [9] to solve this problem.
In deep learning approach, our work is closely related to
NNVLP [22]. Being motivated by CNN-LSTM-CRF architec-
ture that achieves state-of-the-art performance in many lan-
guages [13], NNVLP applied this architecture to Vietnamese.
In our work, instead of CNNs, we use LSTM to represent
character embeddings as in [8].
III. BACKGROUNDS ON LSTM AND CRFS
A. Recurrent Neural Networks
Recurrent Neural Networks (RNNs) are a family of artiﬁcial
neural network for processing sequential data [24]. They take
a sequence of vectors x as input and return another sequence
h representing some information about the sequence at every
step in the input. An RNN introduces the connection the
previous hidden state and current hidden state. At time step t,
arXiv:1811.03754v2  [cs.CL]  12 Nov 2018


## Page 2


the value in the hidden layers and output layers o are computed
as follows:
ht = f(Uxt + W h(t−1))
(1)
ot = g(V st),
(2)
where U, W and V are the parameters computed in training
time. f usually is a nonlinear function such as tanh or ReLU,
and g is a softmax function.
RNNs maintain a memory based on history information
which enables the model can, in theory, predict the current
output conditioned on long distance features. In practice they
fail to do, and tend to be biased towards their most recent
inputs, due to the gradient vanishing/exploding problems [1]
[18].
B. LSTMs
LSTMs [4] are variants of RNNs which have been designed
to deal with these gradient vanishing problems by replacing the
RNN’s hidden layers by purpose-built memory cells, and have
been shown to effectively capture long-range dependencies.
An LSTM unit is composed of several gates which control
the proportions of information to forget and to pass on to the
next time. Thus they can be better at ﬁnding and exploiting
long range dependencies in the data. Formally, the memory
cell is updated at time t as follow:
f t = σ(W fht−1 + U fxt + bf)
(3)
it = σ(W iht−1 + U ixt + bi)
(4)
˜ct = tanh(W cht−1 + U cxt + bc)
(5)
ct = f t ⊙ct−1 + it ⊙˜ct
(6)
ot = σ(W oht−1 + U oxt + bo)
(7)
ht = ot ⊙tanh(ct),
(8)
where σ is the logistic sigmoid function and ⊙is the element-
wise product. xt is the input vector at time t, and ht is
the hidden state vector capturing the useful information at
current time (and all the previous time steps). f, i, o and
c are the forget gate, input gate, output gate and cell vectors
respectively, with U f, U i, U o, U c are weight matrices of
these gates for input xt and W f, W i, W o, W c are the weight
matrices for hidden state ht.
C. Bidirectional LSTM
An LSTM takes information in a sequence only from
past. However, in many sequence tagging tasks, retrieving
information from both past (left) and future (right) contexts
is beneﬁcial. A straightforward way to do this is using a
bidirectional LSTM network (ﬁgure 1) as proposed in [2].
generates a representation of the right context that can be
achieved by using a second LSTM reading the same sequence
in reverse. Then the ﬁnal output is obtained by concatenating
its left and right context representations.
Input
Input
Input
LSTM
LSTM
LSTM
LSTM
LSTM
LSTM
Output
Output
Output
Forward Layer
Backward Layer
Figure 1. Bidirectional LSTM
D. Bidirectional LSTM-CRFs
For many sequence labeling tasks, a very simple but surpris-
ingly effective method is to consider the correlations between
labels in neighborhoods and jointly decode the best chain of
labels for a given input sequence. For example, in NER task
with BIO2 annotation [25], B-LOC is certainly followed by I-
LOC, and I-PER cannot follow B-ORG. Therefore, instead of
decoding each label independently, we decode them jointly
using a linear-chain ﬁrst order CRF [7]. CRFs is a fam-
ily of discriminative probabilistic framework, which directly
model conditional probabilities of a tag sequence given a
word sequence. Formally, the score of the input sentence
X = (x1, x2, . . . , xn), where xi is the vector of the ith word,
associated with the sequence of tag y = (y1, y2, . . . , yn) is
deﬁned to be
s(X, y) =
n
X
i=0
Ayi,yi+1 +
n
X
i=1
Pyi,i,
where Ai,j denotes the score of a transition from the tag i to
the tag j, y0 and yn+1 are the start and end tags of a sentence.
Py,i represents the score of the tag y of the ith word in a
sentence outputted by the bidirectional LSTM network.
Then, the probability of the tag sequence is given with the
following form
p(y|X) =
exp (s(X, y))
P
y′∈YX exp(s(X, y′))
where Y X is the set of all possible tag sequences for a
sentence X. For CRF training, the parameters can be estimated
by maximizing the log-probability of the correct tag sequence
log(p(y|X)), and the output sequence y∗is obtained by
maximizing the score
y∗= argmax
y′∈YX
s(X, y′)
The decoding stage in CRFs (i.e. linear ﬁrst-order CRFs in
our work) can be efﬁciently solved by Viterbi algorithm.


## Page 3


hb 
hb 
hb 
hb 
hf
hf 
hf 
hf 
H
à
_
N
ộ
hf 
hb 
i
hf 
hb 
Forward 
Representation 
Backward  
Representation 
Character-level 
Representation 
Figure 2. The character embeddings of the word “Hà_Nội” are given to a
bidirectional LSTMs for extracting character-level word features. Character-
level representation of one word is the concatenation of its forward and
backward representations
IV. BIDIRECTIONAL LSTM-CRFS WITH CHARACTER
EMBEDDINGS FOR SEQUENCE LABELING
A. Bidirectional LSTM-CRFs with character embeddings for
POS Tagging
Character-based model of word. Recently, character-level
knowledge has been leveraged and empirically veriﬁed to be
helpful in sequence labeling tasks. [8] has shown that LSTM
is an effective approach to extract morphological information
(instead of hand-engineering preﬁx and sufﬁx information
about words) from characters of words. Firstly, we randomly
initialize an embedding for every character. The character
embeddings corresponding to characters in a word are given
to a forward and a backward LSTM. For each word, the
character-level word embedding is the concatenation of two
last hidden states from forward and backward layers of the
Bidirectional LSTM as described in Figure 2. Then, this
character-based word representation is concatenated with the
pre-trained word embedding to obtain the word representation.
Pre-trained word embeddings. In this work, we use avail-
able word embedding set provided by [22], that trained from
7.3GB of 2 million articles collected through a Vietnamese
news portal by word2vec toolkit. For words that do not have
an embedding, a vector called unknown (UNK) embedding
is used instead. The UNK embedding is created by random
vectors sampled uniformly from the range [−
q
3
dim, +
q
3
dim]
where dim is the dimension of word embeddings [3]. Here the
number of dimensions for word embedding is 300. Dropout
layers are applied on both the input and output vectors of
Bidirectional LSTM to prevent the models from depending
on one representation or the other too strongly. Experimental
results have shown the signiﬁcant effectiveness of the use of
dropout in training. Finally, the output vectors of Bidirectional
LSTM are fed to a CRF layer to jointly decode the best label
CRF  
Layer
N
Np
V
Np
LSTM
LSTM 
LSTM
LSTM
LSTM
LSTM
LSTM
LSTM
w1
w2
w3
w4
Backward 
LSTM 
Forward 
LSTM 
Word  
Representation 
Char-level 
Representation 
Word 
Embedding 
Tổng_thống 
Obama 
thăm 
Hà_Nội 
Figure 3. Bidirectional LSTM-CRFs architecture for POS tagging.
sequence. Figure 3 presents the architecture of this approach.
B. Bidirectional LSTM-CRFs with character embeddings for
NER.
For NER task, we apply the same system as in the POS
tagging task. Furthermore, we utilizes other information such
as POS tags or chunk tags that are available in the dataset
to provide additional syntactic information. To do this, we
encode every POS (and chunk) tag as a one-hot vector whose
length is equal to the number of POS tags (and chunk tags).
For example:
• N: 1000...000
• V: 0100...000
• R: 0000...010
Then, the concatenation of these one-hot vectors and word
representation are fed into Bidirectional LSTM as described
in Figure 4.
V. EXPERIMENTS
A. Datasets
We use the following benchmark datasets in our experi-
ments: VietTreebank (VTB) [17] for POS tagging, and VLSP
shared task 2016 corpus for NER task. While the NER dataset
has been originally released for evaluation, the POS tagging
data set are not previously divided. Therefore, we use cross-
validation to evaluate POS tagging. Table I provides some
statistics about these corpus. The dataset provided by VLSP
2016 organizers consist of four columns of word, POS, chunk
and NER tag respectively.


## Page 4


Decoder 
 Layer
O
B-PER
O
B-LOC
LSTM
LSTM 
LSTM
LSTM
LSTM
LSTM
LSTM
LSTM
w1
w2
w3
w4
Word  
Representation 
Word 
Embedding 
Char-level 
Representation 
POS 
Embedding 
Chunk 
embedding 
Tổng_thống
Obama
thăm
Hà_Nội
Encoder 
 Layer
Figure 4. Bidirectional LSTM-CRFs architecture for NER
Table I
DATASET STATISTICS
Dataset
Task
#sent
#word
VTB
POS tagging
10,383
221,464
VLSP 2016 - train
NER
14,861
325,686
VLSP 2016 - dev
NER
2,000
43,706
VLSP 2016 - test
NER
2,831
66,097
B. Hyper-parameters
Table II summarizes the chosen hyper-parameters for all ex-
periments. Hyper-parameters were tuned on the development
set of NER. On the hand, we used hyper-parameters tuned for
NER to learn POS tagging.
We set the character embedding dimension at 100, the word
embedding dimension at 300, the dimension of hidden states
of the char-level LSTMs at 100 and the dimension of hidden
states of the word-level LSTMs at 150. We optimize parame-
ters using Adaptive Moment Estimation (Adam) optimizer [6]
with mini-batch size 8. We choose an initial learning rate of
η0 = 0.003, and the learning rate is updated on each epoch of
training as ηt = η0/(1+αt), with decay rate α = 0.05 and t is
the number of epoch completed [13]. Inputs for POS tagging
task are gold word segmentation, and for NER task are gold
word segmentation, POS tags, and chunks. As mention before,
dropout method is applied on both the input and output vectors
of the second Bidirectional LSTM to prevent overﬁtting. We
Table II
THE MODEL HYPER-PARAMETERS
Hyper-parameter
Value
character dimension
100
word dimension
300
hidden size char
100
hidden size word
150
update function
Adam
learning rate
0.0035
learning decay rate
0.005
dropout rate
0.35
batch size
8
Table III
POS TAGGING PERFORMANCE ON VTB
Method
Accuracy
Evaluation Method
NNVLP [22]
91.92
RDRPOStagger [16]
92.59
5-fold cross-validation
BiLSTM-CRFs w.o char
91.74
BiLSTM-CRFs
92.98
VNTagger [11]
93.40
BiLSTM-CRFs w.o char
92.22
10-fold cross-validation
BiLSTM-CRFs
93.52
ﬁx the dropout rate to 0.35. We use early stopping based on
performance on development sets in which the convergence is
reached after around 25 epochs.
C. Experimental Results
For POS tagging, we compare our work with the following
supervised taggers:
• NNVLP [22] is a deep learning method based on Bidi-
rectional LSTM-CRFs architecture with character embed-
dings from CNNs.
• RDRPOSTagger [16] learns tagging rules from annotation
using Ripple-Down Rules framework.
• VNTagger [11] learns a Maximum Entropy model using
handcraft features.
For NER, we compare our work with the following super-
vised methods:
• Feature-rich CRFs [15]: As the name mentions, this
system learn CRFs model with a rich set of features
including surrounding n-grams and word shape features.
• NNVLP [22]: This model is identical to the model for
POS tagging except the inclusion of POS tags and chunk
embeddings.
We conduct experiments and compare the performance of
our system and several published systems on POS tagging
and NER task. In experiments, we use micro-averaged F1
score, the ofﬁcial evaluation metric in CoNLL 2003 [27] as
the evaluation measure for NER task. The results on these task
are plotted in Table III and Table IV respectively. These tables
compares the Vietnamese POS tagging and NER results of
our system with results reported in prior work, using the same
experimental setup. In particular, our system achieves an accu-
racy of 93.52% for POS tagging task and a F1 score of 94.88%
for NER task, which signiﬁcantly outperform previous state-
of-the-art work on Vietnamese. Experimental results showed
signiﬁcant improvement on both tasks, especially for NER,
gained by leveraging character-level knowledge of words. We
also observed that NER task beneﬁts from syntactic features
including POS and chunk information, which aligns with the
results in [21].
As our model signiﬁcantly outperforms NNVLP which ap-
plies the same Bidirectional LSTM-CRFs framework and the
same pre-trained word embedding set, we take a closer look
at their model. Firstly, their neural networks have different
hyper-parameter values. Secondly, their CNNs use only one
window size of three subsequent characters. Therefore, it could


## Page 5


Table IV
NER PERFORMANCE ON VLSP 2016 DATASET
Method
P
R
F1
F1
(w.o char)
Feature-rich CRFs [15]
93.87
93.99
93.93
-
NNVLP [22]
92.76
93.07
92.91
-
BiLSTM-CRFs
90.97
87.52
89.21
76.43
BiLSTM-CRFs + POS
90.90
90.39
90.64
86.06
BiLSTM-CRFs + Chunk
95.24
92.16
93.67
87.13
BiLSTM-CRFs + POS + Chunk
95.44
94.33
94.88
91.36
possibly be that our hyper-parameters were better tuned on
development set; or their CNNs-based character embeddings
should be further improved, for instance by combining several
window sizes; or LSTMs, which capture long-range dependen-
cies and cross-syllable dependencies, are better for character
embeddings of Vietnamese words. In the future, we are going
to investigate more on this.
VI. CONCLUSIONS
In this work, we have applied a deep neural network model
for Vietnamese sequence tagging, which obtains state-of-the-
art performance. Experiments on benchmark data sets for
Vietnamese sequence labeling tasks showed the effectiveness
of training character-based model of word by bidirectional
LSTM in language representation serving sequence labeling
tasks, that outperform models using CNN despite requiring
less cost for building. We have also shown that inserting
syntactic features into the representation of a word improves
accuracy signiﬁcantly, especially information about chunk.
ACKNOWLEDGMENT
This work is supported by VCCorp. We would like to thank
the NNVLP [22] team for publishing the pre-trained word
embedding set that we used during training and evaluating
stage of our model.
REFERENCES
[1] Y. Bengio, P. Simard, and P. Frasconi, “Learning long-term dependencies
with gradient descent is difﬁcult,” IEEE transactions on neural networks,
vol. 5, no. 2, pp. 157–166, 1994.
[2] A. Graves and J. Schmidhuber, “Framewise phoneme classiﬁcation
with bidirectional lstm and other neural network architectures,” Neural
Networks, vol. 18, no. 5-6, pp. 602–610, 2005.
[3] K. He, X. Zhang, S. Ren, and J. Sun, “Delving deep into rectiﬁers:
Surpassing human-level performance on imagenet classiﬁcation,” in
Proceedings of the IEEE international conference on computer vision,
2015, pp. 1026–1034.
[4] S. Hochreiter and J. Schmidhuber, “Long short-term memory,” Neural
computation, vol. 9, no. 8, pp. 1735–1780, 1997.
[5] Z. Huang, W. Xu, and K. Yu, “Bidirectional lstm-crf models for
sequence tagging,” arXiv preprint arXiv:1508.01991, 2015.
[6] D. P. Kingma and J. Ba, “Adam: A method for stochastic optimization,”
arXiv preprint arXiv:1412.6980, 2014.
[7] J. Lafferty, A. McCallum, and F. C. Pereira, “Conditional random ﬁelds:
Probabilistic models for segmenting and labeling sequence data,” 2001.
[8] G. Lample, M. Ballesteros, S. Subramanian, K. Kawakami, and
C. Dyer, “Neural architectures for named entity recognition,” in
Proceedings
of
the
2016
Conference
of
the
North
American
Chapter of the Association for Computational Linguistics: Human
Language Technologies.
San Diego, California: Association for
Computational Linguistics, June 2016, pp. 260–270. [Online]. Available:
http://www.aclweb.org/anthology/N16-1030
[9] T. H. Le, T. T. T. Nguyen, T. H. Do, and X. T. Nguyen, “Named entity
recognition in vietnamese text,” Proceedings of VLSP, 2016.
[10] P.
Le-Hong,
“Vietnamese
named
entity
recognition
using
token
regular
expressions
and
bidirectional
inference,”
arXiv
preprint
arXiv:1610.05652, 2016.
[11] P. Le-Hong, A. Roussanaly, T. M. H. Nguyen, and M. Rossignol,
“An empirical study of maximum entropy approach for part-of-speech
tagging of vietnamese texts,” in Traitement Automatique des Langues
Naturelles-TALN 2010, 2010, p. 12.
[12] G. Luo, X. Huang, C.-Y. Lin, and Z. Nie, “Joint entity recognition and
disambiguation,” in Proceedings of the 2015 Conference on Empirical
Methods in Natural Language Processing, 2015, pp. 879–888.
[13] X.
Ma
and
E.
Hovy,
“End-to-end
sequence
labeling
via
bi-
directional
lstm-cnns-crf,”
in
Proceedings
of
the
54th
Annual
Meeting of the Association for Computational Linguistics (Volume
1: Long Papers).
Berlin, Germany: Association for Computational
Linguistics,
August
2016,
pp.
1064–1074.
[Online].
Available:
http://www.aclweb.org/anthology/P16-1101
[14] D.-T. L. Mai-Vu Tran, “vtools: Chunker and part-of-speech tools,” RIVF-
VLSP 2013 Workshop, 2013.
[15] P. Q. N. Minh, “A feature-rich vietnamese named-entity recognition
model,” arXiv preprint arXiv:1803.04375, 2018.
[16] D. Q. Nguyen, D. Q. Nguyen, D. D. Pham, and S. B. Pham, “Rdrpostag-
ger: A ripple down rules-based part-of-speech tagger,” in Proceedings
of the Demonstrations at the 14th Conference of the European Chapter
of the Association for Computational Linguistics, 2014, pp. 17–20.
[17] P.-T. Nguyen, X.-L. Vu, T.-M.-H. Nguyen, V.-H. Nguyen, and H.-P.
Le, “Building a large syntactically-annotated corpus of vietnamese,” in
Proceedings of the Third Linguistic Annotation Workshop.
Association
for Computational Linguistics, 2009, pp. 182–185.
[18] R. Pascanu, T. Mikolov, and Y. Bengio, “On the difﬁculty of training
recurrent neural networks,” in International Conference on Machine
Learning, 2013, pp. 1310–1318.
[19] A. Passos, V. Kumar, and A. McCallum, “Lexicon infused phrase em-
beddings for named entity resolution,” arXiv preprint arXiv:1404.5367,
2014.
[20] T.-H. Pham and P. Le-Hong, “End-to-end recurrent neural network mod-
els for vietnamese named entity recognition: Word-level vs. character-
level,” in Proceedings of The 15th International Conference of the Paciﬁc
Association for Computational Linguistics, 2017.
[21] ——, “The importance of automatic syntactic features in vietnamese
named entity recognition,” arXiv preprint arXiv:1705.10610, 2017.
[22] T.-H. Pham, X.-K. Pham, T.-A. Nguyen, and P. Le-Hong, “Nnvlp:
A neural network-based vietnamese language processing toolkit,” in
Proceedings of The 8th International Joint Conference on Natural
Language Processing, 2017.
[23] L. Ratinov and D. Roth, “Design challenges and misconceptions in
named entity recognition,” in Proceedings of the Thirteenth Conference
on Computational Natural Language Learning.
Association for Com-
putational Linguistics, 2009, pp. 147–155.
[24] D. E. Rumelhart, G. E. Hinton, and R. J. Williams, “Learning internal
representations by error propagation,” California Univ San Diego La
Jolla Inst for Cognitive Science, Tech. Rep., 1985.
[25] E. F. Sang and J. Veenstra, “Representing text chunks,” in Proceedings
of the ninth conference on European chapter of the Association for
Computational Linguistics.
Association for Computational Linguistics,
1999, pp. 173–179.
[26] N. Srivastava, G. Hinton, A. Krizhevsky, I. Sutskever, and R. Salakhut-
dinov, “Dropout: a simple way to prevent neural networks from over-
ﬁtting,” The Journal of Machine Learning Research, vol. 15, no. 1, pp.
1929–1958, 2014.
[27] E. F. Tjong Kim Sang and F. De Meulder, “Introduction to the conll-
2003 shared task: Language-independent named entity recognition,” in
Proceedings of the seventh conference on Natural language learning at
HLT-NAACL 2003-Volume 4.
Association for Computational Linguis-
tics, 2003, pp. 142–147.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
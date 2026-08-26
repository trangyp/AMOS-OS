---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1705.04044
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1705.04044_End-to-end_Recurrent_Neural_Network_Models_for_Vietnamese_Named_Entity_Recogniti

> Source: 1705.04044_End-to-end_Recurrent_Neural_Network_Models_for_Vietnamese_Named_Entity_Recogniti.pdf

> Pages: 14

---


## Page 1


arXiv:1705.04044v3  [cs.CL]  21 Jul 2017
End-to-end Recurrent Neural Network Models
for Vietnamese Named Entity Recognition:
Word-level vs. Character-level
Thai-Hoang Pham1 and Phuong Le-Hong2
1 R&D Department, Alt Inc, Hanoi, Vietnam
phamthaihoang.hn@gmail.com,
2 College of Science
Vietname National University in Hanoi, Vietnam
phuonglh@vnu.edu.vn
Abstract. This paper demonstrates end-to-end neural network archi-
tectures for Vietnamese named entity recognition. Our best model is a
combination of bidirectional Long Short-Term Memory (Bi-LSTM), Con-
volutional Neural Network (CNN), Conditional Random Field (CRF),
using pre-trained word embeddings as input, which achieves an F1 score
of 88.59% on a standard test set. Our system is able to achieve a compara-
ble performance to the first-rank system of the VLSP campaign without
using any syntactic or hand-crafted features. We also give an extensive
empirical study on using common deep learning models for Vietnamese
NER, at both word and character level.
Keywords: Vietnamese, named entity recognition, end-to-end, Long
Short-Term Memory, Conditional Random Field, Convolutional Neural
Network
1
Introduction
Named entity recognition (NER) is a fundamental task in natural language pro-
cessing and information extraction. It involves identifying noun phrases and
classifying each of them into a predefined class. In 1995, the 6th Message Under-
standing Conference (MUC)3 started evaluating NER systems for English, and
in subsequent shared tasks of CoNLL 20024 and CoNLL 20035 conferences, lan-
guage independent NER systems were evaluated. In these evaluation tasks, four
named entity types were considered, including names of persons, organizations,
locations, and names of miscellaneous entities that do not belong to these three
types.
More recently, the Vietnamese Language and Speech Processing (VLSP)6
community has organized an evaluation campaign to systematically compare
3 http://cs.nyu.edu/faculty/grishman/muc6.html
4 http://www.cnts.ua.ac.be/conll2002/ner/
5 http://www.cnts.ua.ac.be/conll2003/ner/
6 http://vlsp.org.vn/


## Page 2


NER systems for the Vietnamese language. Similar to the CoNLL 2003 share
task, four named entity types are evaluated: persons (PER), organizations (ORG),
locations (LOC), and miscellaneous entities (MISC). The data are collected from
electronic newspapers published on the web.
In this paper, we present a state-of-the-art NER system for the Vietnamese
language without using any hand-crafted features. Our system is competitive
with the first-rank system of the VLSP campaign that used many syntactic and
hand-crafted features. In summary, the overall F1 score of our system is 88.59%
on the standard test set provided by the organizing committee of the evaluation
campaign7. The contributions of this work include:
– We propose a truly end-to-end deep learning model which gives the state-of-
the-art performance on a standard NER data set for Vietnamese. Our best
model is a combination of Bi-LSTM, CNN, and CRF models, which achieves
an F1 score of 88.59%.
– We give an extensive empirical study on using common deep learning models
for Vietnamese NER, at both word and character level. These models are also
comparable to conventional sequence labeling models, including Maximum
Entropy Markov Models (MEMMs) and CRFs.
– We make our NER system open source for research purpose, which is believed
to be a good contribution to the future development of Vietnamese NER in
particular and Vietnamese language processing research in general.
The remainder of this paper is structured as follows. Section 2 summarizes
related work on NER. Section 3 describes end-to-end models used in our system.
Section 4 gives experimental results and discussions. Finally, Section 5 concludes
the paper.
2
Related Work
Within the large body of research on NER which have been published in the
last two decades, we identify two main approaches. The first approach is char-
acterized by the use of well-established sequence labeling models such as con-
ditional random field (CRF), hidden markov model, support vector machine,
maximum entropy and so on. The performance of these models is heavily de-
pendent on hand-crafted features. In particular, most of the participants at
CoNLL-2003 shared task attempted to use information other than the avail-
able training data such as gazetteers and unannotated data. The best system
at CoNLL-2003 shared task is the work of [5] which achieved an F1 score of
88.76%. After that, [17] surpassed them by using phrase features extracted from
an external database. Moreover, training NER models jointly with related tasks
helps improve their performance. For instance, [4] trained a CRF model for joint-
learning three tasks, including coreference resolution, entity linking, and NER,
7 The first-rank system of the VLSP 2016 NER evaluation campaign has F1 =88.78%
on the test set.


## Page 3


and achieved the state-of-the-art result on OntoNotes dataset. With a similar
approach, [18] gained the best performance on CoNLL-2003 shared task dataset.
With a recent resurgence of the deep learning approach, several neural ar-
chitectures have been proposed for NER task. These methods have a long story,
but they have been focused only recently by the advance of computational power
and high-quality word embeddings. The first neural network model is the work
of [23] that used a feed-forward neural network with one hidden layer. This model
achieved the state-of-the-art result on the MUC6 dataset. After that, [8] used
a long short-term memory network for this problem. Recently, [3] used a con-
volution neural network over a sequence of word embeddings with a conditional
random field on the top. This model achieved near state-of-the-art results on
some sequence labeling tasks such as POS tagging, chunking, and NER. From
2015 until now, the long short-term memory model has been the best approach
for many sequence labeling tasks. [10] used bidirectional LSTM with CRF layer
for joint decoding. Instead of using hand-crafted feature as [10], [2] proposed
a hybrid model that combined bidirectional LSTM with convolutional neural
networks (CNN) to learn both character-level and word-level representations.
Unlike [2], [13] used bidirectional LSTM to model both character and word-
level information. The work of [19] proposed a truly end-to-end model that used
only word embeddings for detecting entities. This model is the combination
of CNN, bidirectional LSTM, and CRF models. Approaching this problem at
the character-level sequence, the LSTM-CRF model of [11] achieved the nearly
state-of-the-art results in seven languages.
3
Methodology
3.1
Long Short-Term Memory Networks
Recurrent Neural Network The recurrent neural network (RNN) is a class
of artificial neural network designed for sequence labeling task. It takes input as
a sequence of vector and returns another sequence. The simple architecture of
RNN has an input layer x, hidden layer h and output layer y. At each time step
t, the values of each layer are computed as follows:
ht = f(Uxt + Wht−1)
yt = g(Vht)
where U, W, and V are the connection weight matrices in RNN, and f(z)
and g(z) are sigmoid and softmax activation functions.
Long Short-Term Memory Long short-term memory (LSTM) [9] is a variant
of RNN which is designed to deal with these gradient vanishing and exploding
problems [1,22] when learning with long-range sequences. LSTM networks are
the same as RNN, except that the hidden layer updates are replaced by memory
cells. Basically, a memory cell unit is composed of three multiplicative gates that


## Page 4


control the proportions of information to forget and to pass on to the next time
step. As a result, it is better for exploiting long-range dependency data. The
memory cell is computed as follows:
it = σ(Wiht−1 + Uixt + bi)
ft = σ(Wfht−1 + Ufxt + bf)
ct = ft ⊙ct−1 + it ⊙tanh(Wcht−1 + Ucxt + bc)
ot = σ(Woht−1 + Uoxt + bo)
ht = ot ⊙tanh(ct)
where σ is the element-wise sigmoid function and ⊙is the element-wise product,
i, f, o and c are the input gate, forget gate, output gate and cell vector respec-
tively. Ui, Uf, Uc, Uo are connection weight matrices between input x and gates,
and Ui, Uf, Uc, Uo are connection weight matrices between gates and hidden
state h. bi, bf, bc, bo are the bias vectors.
Bidirectional Long Short-Term Memory The original LSTM uses only
previous contexts for prediction. For many sequence labeling tasks, it is advisable
when taking the contexts from two directions. Thus, we utilize the bidirectional
LSTM (Bi-LSTM) [7,6] for both word and character-level systems.
3.2
Conditional Random Field
Conditional Random Field (CRF) [12] is a type of graphical model designed for
labeling sequence of data. Although the LSTM is likely to handle the sequence
of the input data by learning the dependencies between the input at each time
step but it predicts the outputs independently. The CRF, therefore, is beneficial
to explore the correlations between outputs and jointly decode the best sequence
of labels. In NER task, we implement the CRF on the top of Bi-LSTM instead
of the softmax layer and take outputs of Bi-LSTM as the inputs of this model.
The parameter of the CRF is the transition matrix A where Ai,j represents the
transition score from tag i to tag j. The score of the input sentence x along with
the sequence of tags y is computed as follow:
S(x, y, θ ∪Ai,j) =
T
X
t=1
(Ayt−1,yt + fθ(yt,t))
where θ is the parameters of Bi-LSTM, fθ is the score outputed by Bi-LSTM,
and T is the number of time steps. Then the tag-sequence likelihood is computed
by the softmax equation:
p(y|x, A) =
exp(S(x, y, θ ∪Ai,j))
P
y′ ∈Y exp(S(x, y
′, θ ∪Ai,j))


## Page 5


where Y is the set of all possible output sequences. In the training stage, we
maximize the log-likelihood function:
L =
N
X
i=1
log p(yi|xi; A)
where N is the number of training samples. In the inference stage, the Viterbi
algorithm is used to find the output sequence y∗that maximize the conditional
probability:
y∗= arg max
y∈Y
p(y|x, A)
3.3
Learning Word Embedings
It has been shown that distributed representations of words (words embeddings)
help improve the accuracy of a various natural language models. In this work, we
investigate three methods to create word embeddings using a skip-gram model,
a CNN model and a Bi-LSTM model.
Pre-Trained Word Vectors Learnt by Skip-gram Model To create word
embeddings for Vietnamese, we train a skip-gram model using the word2vec8
tool on a dataset consisting of 7.3GB of text from 2 million articles collected
through a Vietnamese news portal.9 The text is first normalized to lower case
and all special characters are removed. The common symbols such as the comma,
the semicolon, the colon, the full stop and the percentage sign are replaced with
the special token punct, and all numeral sequences are replaced with the special
token number. Each word in the Vietnamese language may consist of more than
one syllables with spaces in between, which could be regarded as multiple words
by the unsupervised models. Hence it is necessary to replace the spaces within
each word with underscores to create full word tokens. The tokenization process
follows the method described in [16]. For words that appear in VLSP corpus
but not appear in word embeddings set, we create random vectors for these
words by uniformly sampling from the range [−
q
3
dim, +
q
3
dim] where dim is
the dimension of embeddings.
Character-Level Word Vectors Learnt by Convolutional Neural Net-
work Convolutional neural network (CNN) is a type of feed-forward neural net-
works that that uses many identical copies of the same neuron. This characteris-
tic of CNN permits this network to have lots of neurons and, therefore, express
computationally large models while keeping the number of actual parameters
relativity small. For NLP tasks, previous works have shown that CNN is likely
to extract morphological features such as prefix and suffix effectively [24,2,19].
8 https://code.google.com/archive/p/word2vec/
9 http://www.baomoi.com


## Page 6


Fig. 1. The CNN for extracting character-level word features of word Học_sinh (Stu-
dent).
For this reason, we incorporate the CNN to the word-level model to get richer
information from character-level word vectors. These vectors are learnt during
training together with the parameters of the word models. The CNN we use in
this paper is described in Figure 1.
Character-Level Word Vectors Learnt by Long Short-Term Memory
The second way for generating character-level word vectors is using Bi-LSTM. In
particular, we incorporate this model to the word-level model to learn character-
level word vectors. Character-level word vectors are concatenations of two last
hidden states from forward and backward layers of Bi-LSTM. These vectors are
also learnt during training together with the parameters of the word models.
The Bi-LSTM model we use for this task is described in Figure 2.
3.4
Our Proposed Models
We propose two different types of models based on the level of input, either using
word sequence or character sequence. Concretely, in the first type, each input
sentence is fed to the model as a sequence of words, while in the second type, it
is fed as a sequence of characters. Both of the two model types share the same
pipeline in that it takes as input a sequence of distributed representations of the
underlying processing unit (word or character), that sequence is then passed to
a Bi-LSTM, and then a CRF layer takes as input the output of the Bi-LSTM to
predict the best named entity output sequence.
Word-Levels Models In the first type, we investigate four different word em-
beddings, including (Word-0) random vectors, (Word-1) skip-gram vectors,


## Page 7


Fig. 2. The Bi-LSTM for extracting character-level word features of word Học_sinh
(Student).
(Word-2) skip-gram vectors concatenated with CNN-generated word features,
and (Word-3) skip-gram vectors concatenated with LSTM-generated word fea-
tures. Figure 3 describes the architecture of the word-level models.
Character-Level Model In the second type, we investigate one model in that
its input is a sequence of vectors corresponding to characters of the input sen-
tence. We call this model (Char-0). Because the size of Vietnamese character
set is relatively small, our data set is sufficient to learn distributed representa-
tions for Vietnamese characters. We therefore initialize random vectors for these
characters by uniformly sampling from the range [−
q
3
dim, +
q
3
dim] where dim
is the dimension of embeddings. These character vectors are then learnt during
training together with the parameters of the models.
The training data for NER is in CoNLL-2003 format, where both input and
output sequence are annotated at word-level. For this reason, it is necessary
to convert the dataset from word-level sequences to character-level sequences.
We use a simple method in which all characters of a word are labeled with the
same tag. For example, the label of all characters of a person named entity is
P. Similarly, all characters of location, organization, and miscellaneous tokens
are labelled with letters L, G, and M respectively. The characters of other words
and spaces are labelled by O. Figure 4 shows the transformation from word-level
to character-level of an example sentence Anh rời EU hôm qua (UK left EU
yesterday) and Figure 5 describes the architecture of the character-level models.
4
Results and Discussions
4.1
VLSP Corpus
We evaluate our system on the VLSP NER shared task 2016 corpus. This corpus
consists of electronic newspapers published on the web. There are four named
entity types in this corpus, names of person, location, organization and other


## Page 8


Fig. 3. Word-level model type for input sentence Anh rời EU hôm qua. (UK left EU
yesterday.) Word-0 and Word-1 models uses only word embeddings as input, while
Word-2 and Word-3 models uses both word embeddings and word features generated
either by CNN or Bi-LSTM.
Anh
rời
EU
hôm_qua
B-ORG O B-ORG
O
A n h
r ời
E U
h ô m _ q u a
G G G O O O O O G G O O O O O O O O
Fig. 4. Word and character-level sequence labeling of the sentence Anh rời EU
hôm_qua. (UK left EU yesterday.)
named entities. Four types of NEs are compatible with their descriptions in the
CoNLL shared task 2003. The examples of each entity type are described in
Table 1
Data have been preprocessed with word segmentation and POS tagging. Be-
cause POS tags and chunking tags are determined automatically by public tools,
they may contain mistakes. The format of this corpus follows that of the CoNLL
2003 shared task. It consists of five columns. The order of these columns are
word, POS tag, chunking tag, named entity label, and nested named entity la-
bel. Our system focuses on only named entity without nesting, so we do not use
the fifth column. Named entity labels are annotated using the IOB notation as
in the CoNLL shared tasks. There are 9 labels: B-PER and I-PER are used for
persons, B-ORG and I-ORG are used for organizations, B-LOC and I-LOC are
used for locations, B-MISC and I-MISC are used for other named entities and O


## Page 9


Fig. 5. Character-level model type for input sentence Anh. (UK.)
Table 1. Examples of Vietnamese Entity Types
Entity Types
Examples
Person
thành phốHồChí Minh (Ho Chi Minh
city), núi Bà Đen (Ba Den mountain),
sông Bạch Đằng (Bach Dang river)
Location
công ty Formosa (Formosa company),
nhà máy thủy điện Hòa Bình (Hoa
Binh hydroelectric factory)
Organization
ông Lân (Mr. Lan), bà Hà (Mrs. Ha)
Miscellaneous names tiếng Indonesia (Indonesian), người
Canada (Canadian)
is used for other elements. Table 2 shows the quantity of named entity annotated
in the training set and the test set.
Because our systems are end-to-end architecture, we focus only on the word
and named entity label columns. To alleviate the data sparseness, we perform
the following preprocessing for our system:
– All tokens containing digit number are replaced by a special token number.
– All punctuations are replaced by a special token punct.
Moreover, we take one part of training data for validation. The detail of each
data set is described in Table 3.
4.2
Evaluation Method
The performance is measured with F1 score, where F1 = 2∗P ∗R
P +R . Precision (P) is
the percentage of named entities found by the learning system that are correct.
Recall (R) is the percentage of named entities present in the corpus that are


## Page 10


Table 2. Statistics of named entities in VLSP corpus
Entity Types
Training Set Testing Set
Location
6,247
1,379
Organization
1,213
274
Person
7,480
1,294
Miscellaneous names
282
49
All
15,222
2,996
Table 3. Size of each data set in VLSP corpus
Data sets Number of sentences
Train
14,861
Dev
2,000
Test
2,831
found by the system. A named entity is correct only if it is an exact match
of the corresponding entity in the data file. For character-level model, after
predicting label for each character, we convert these outputs back to the word-
level sequence to evaluate. The performance of our system is evaluated by the
automatic evaluation script of the CoNLL 2003 shared task.10.
4.3
Results
Word-Level Model vs. Character-Level Model In the first experiment, we
compare the effectiveness of word and character-level approaches without using
any external corpus. For this reason, in this experiment, we do not use any pre-
trained word embeddings by comparing two models: Word-0 and Char-0. Both
of the two models take embeddings as inputs of Bi-LSTM and predict outputs
by the CRF top layer. Table 4 presents the performance of these systems.
Table 4. Performances of word and character-level models
Entity
Word-0
Char-0
P
R
F1
P
R
F1
LOC
88.37 74.69 80.95 80.03 84.84 82.37
MISC 90.48 77.55 83.52 84.21 65.31 73.56
ORG
60.57 38.83 47.32 50.00 33.58 40.17
PER
89.49 66.51 76.31 84.20 86.09 85.14
ALL
86.78 67.90 76.19 80.08 80.37 80.23
We see that the character-level model outperforms the word-level model by
about 4%. It is because the size of the character set is much smaller than that of
word set. The VLSP corpus, therefore, is enough for learning effectively character
10 http://www.cnts.ua.ac.be/conll2003/ner/


## Page 11


embeddings. For word embeddings, we need a bigger corpus to learn useful word
vectors.
Effect of Word Embeddings It is beneficial to use the external corpus to
learn the word embeddings. In the second experiment, we use skip-gram word
embeddings and compare Word-1 and Word-0 models. The improvement by
using pre-trained word embeddings for the word-level model is shown in Table 5.
Table 5. Performances of random and word2vec embeddings for word-level model
Entity
Word-0
Word-1
P
R
F1
P
R
F1
LOC
88.37 74.69 80.95 87.88 84.08 85.94
MISC 90.48 77.55 83.52 90.00 73.47 80.90
ORG
60.57 38.83 47.32 72.77 50.92 59.91
PER
89.49 66.51 76.31 88.92 71.38 79.19
ALL
86.78 67.90 76.19 87.21 75.35 80.85
By using pre-trained word embeddings, the performance of word-level model
increases by about 4%, to 80.85%. This accuracy is comparable to that of the
character-level model. It proves the effectiveness of using good embeddings for
both words and characters in the Bi-LSTM-CRF model.
Effect of Character-Level Word Features In the third experiment, we eval-
uate the performance of Word-2 and Word-3 models. Recall that these two
models make use of both pre-trained skip-gram word embeddings and character-
level word features generated either by CNN or Bi-LSTM. The obtained perfor-
mances are described in Table 6.
Table 6. Performances of word-level models
Entity
Word-3
Word-2
Word-1
P
R
F1
P
R
F1
P
R
F1
LOC
90.72 88.26 89.48 91.60 88.85 90.20 87.88 84.08 85.94
MISC 94.29 67.35 78.57 97.30 73.47 83.72 90.00 73.47 80.90
ORG
69.23 52.75 59.88 72.77 62.64 67.32 72.77 50.92 59.91
PER
90.12 72.62 80.43 93.60 88.24 90.84 88.92 71.38 79.19
ALL
88.82 77.87 82.98 90.97 85.93 88.38 87.21 75.35 80.85
We observe a significant improvement of performance when character-level
word features learnt by CNN are integrated with pre-trained word embeddings.


## Page 12


This model achieves an overall F1 score of 88.38%. The character-level word
features learnt by Bi-LSTM are not as good as those learnt by CNN, achieves
only an overall F1 score of 82.98%, but they also help improve the performance
of the model in comparison to the Word-1 model.
Comparison with Previous Systems In VLSP 2016 workshop, several dif-
ferent systems have been proposed for Vietnamese NER. In this campaign, they
have evaluated over three entities types LOC, ORG, PER. In all fairness, we
also evaluate our performances over these tags on the same training and test
set. The accuracy of our best model over three entity types is 88.59%, which is
competitive with the best participating system [15] in that shared task. That
system, however, used many hand-crafted features to improve the performance
of maximum entropy classifier (ME) while our system is truly end-to-end model
that takes only word sequences as inputs. Most approaches in VLSP 2016 used
the CRF and ME models, whose performance is heavily dependent on feature
engineering. Table 7 shows those models and their performance.
Table 7. Comparison to participating NER systems at VLSP 2016
Team
Model
Performance
[15]
ME
88.78
Word-2
Bi-LSTM-CNN-CRF
88.59
[Anonymous]11
CRF
86.62
[20]
ME
84.08
[21]
Bi-LSTM-CRF
83.80
[14]
CRF
78.40
There is one work [21] that applied deep learning approach for this task. They
used the implementation provided by [13]. There are two types of LSTM models
in this open source software: Bi-LSTM-CRF and Stack-LSTM. The model that
is most similar to ours is Bi-LSTM-CRF. The accuracy of this system is 83.25%.
Our system outperforms this model due to some possible reasons. First, they
used random vectors as word embeddings and update them during the training
stage. The VLSP corpus size is relatively small so it is not good enough for
learning word representations. Our word embeddings are trained on a collection
of Vietnamese newspapers that is much larger and more abundant than the
VLSP corpus. Second, they used LSTM to model character-level features, while
we used CNN in our model. Previous works have shown that CNN is very useful
to extract these features [24,2,19].
11 This team provided a system without the technical report.


## Page 13


5
Conclusion
In this work, we have investigated a variety of end-to-end recurrent neural net-
work architectures at both word and character-level for Vietnamese named en-
tity recognition. Our best end-to-end system is the combination of Bi-LSTM,
CNN, and CRF models, and uses pre-trained word embeddings as input, which
achieves an F1 score of 88.59% on the standard test corpus published recently
by the Vietnamese Language and Speech community. Our system is competitive
with the first-rank system of the related NER shared task without using any
hand-crafted features.
Acknowledgement
The second author is partly funded by the Vietnam National University, Hanoi
(VNU) under project number QG.15.04. Any opinions, findings and conclusion
expressed in this paper are those of the authors and do not necessarily reflect
the view of VNU.
References
1. Bengio, Y., Simard, P., Frasconi, P.: Learning long-term dependencies with gradient
descent is difficult. IEEE transactions on neural networks 5(2), 157–166 (1994)
2. Chiu, J.P., Nichols, E.: Named entity recognition with bidirectional lstm-cnns.
Transactions of the Association for Computational Linguistics 4, 357–370 (2016)
3. Collobert, R., Weston, J., Bottou, L., Karlen, M., Kavukcuoglu, K., Kuksa, P.:
Natural language processing (almost) from scratch. Journal of Machine Learning
Research 12, 2493–2537 (2011)
4. Durrett, G., Klein, D.: A joint model for entity analysis: Coreference, typing, and
linking. Transactions of the Association for Computational Linguistics 2, 477–490
(2014)
5. Florian, R., Ittycheriah, A., Jing, H., Zhang, T.: Named entity recognition through
classifier combination. In: Daelemans, W., Osborne, M. (eds.) Proceedings of
CoNLL-2003. pp. 168–171. Edmonton, Canada (2003)
6. Graves, A., rahmand Mohamed, A., Hinton, G.: Speech recognition with deep
recurrent neural networks. In: Proceedings of 2013 IEEE international conference
on acoustics, speech and signal processing. pp. 6645–6649. IEEE, Vancouver, BC,
Canada (2013)
7. Graves, A., Schmidhuber, J.: Framewise phoneme classification with bidirectional
lstm networks. In: Proceedings of 2005 IEEE International Joint Conference on
Neural Networks. vol. 4, pp. 2047–2052. IEEE, Montreal, QC, Canada (2005)
8. Hammerton, J.: Named entity recognition with long short-term memory. In: Pro-
ceedings of the seventh conference on Natural language learning at HLT-NAACL.
vol. 4, pp. 172–175. Association for Computational Linguistics (2003)
9. Hochreiter, S., Schmidhuber, J.: Long short-term memory. Neural computation
9(8), 1735–1780 (1997)
10. Huang, Z., Xu, W., Yu, K.: Bidirectional lstm-crf models for sequence tagging.
arXiv preprint arXiv:1508.01991 (2015)


## Page 14


11. Kuru, O., Can, O.A., Yuret, D.: Charner: Character-level named entity recog-
nition. In: Proceedings of The 26th International Conference on Computational
Linguistics. pp. 911–921 (2016)
12. Lafferty, J., McCallum, A., Pereira, F.: Conditional random fields: Probabilistic
models for segmenting and labeling sequence data. In: Proceedings of The Eigh-
teenth International Conference on Machine Learning. vol. 1, pp. 282–289 (2001)
13. Lample, G., Ballesteros, M., Subramanian, S., Kawakami, K., Dyer, C.: Neural
architectures for named entity recognition. arXiv preprint arXiv:1603.01360 (2016)
14. Le, T.H., Nguyen, T.T.T., Do, T.H., Nguyen, X.T.: Named entity recognition in
vietnamese text. In: Proceedings of The Fourth International Workshop on Viet-
namese Language and Speech Processing. Hanoi, Vietnam (2016)
15. Le-Hong, P.: Vietnamese named entity recognition using token regular expressions
and bidirectional inference. In: Proceedings of The Fourth International Workshop
on Vietnamese Language and Speech Processing. Hanoi, Vietnam (2016)
16. Le-Hong, P., Nguyen, T.M.H., Roussanaly, A., Ho, T.V.: A hybrid approach to
word segmentation of Vietnamese texts. In: Language and Automata Theory and
Applications, Lecture Notes in Computer Science, vol. 5196, pp. 240–249. Springer
Berlin Heidelberg (2008)
17. Lin, D., Wu, X.: Phrase clustering for discriminative learning. In: Proceedings
of the Joint Conference of the 47th Annual Meeting of the ACL and the 4th
International Joint Conference on Natural Language Processing of the AFNLP.
vol. 2, pp. 1030–1038. Association for Computational Linguistics (2009)
18. Luo, G., Xiaojiang Huang, Chin-Yew Lin, Z.N.: Joint entity recognition and dis-
ambiguation. In: Proceedings of the 2015 Conference on Empirical Methods on
Natural Language Processing. pp. 879–888. Association for Computational Lin-
guistics (2015)
19. Ma, X., Hovy, E.: End-to-end sequence labeling via bi-directional lstm-cnns-crf.
arXiv preprint arXiv:1603.01354 (2016)
20. Nguyen, T.C.V., Pham, T.S., Vuong, T.H., Nguyen, N.V., Tran, M.V.: Dsktlab-
ner: Nested named entity recognition in vietnamese text. In: Proceedings of The
Fourth International Workshop on Vietnamese Language and Speech Processing.
Hanoi, Vietnam (2016)
21. Nguyen, T.S., Nguyen, L.M., Tran, X.C.: Vietnamese named entity recognition
at vlsp 2016 evaluation campaign. In: Proceedings of The Fourth International
Workshop on Vietnamese Language and Speech Processing. Hanoi, Vietnam (2016)
22. Pascanu, R., Mikolov, T., Bengio, Y.: On the difficulty of training recurrent neural
networks. In: The 30th International Conference on Machine Learning. vol. 28, pp.
1310–1318. Atlanta, USA (2013)
23. Petasis, G., Petridis, S., Paliouras, G., Karkaletsis, V., Perantonis, S., Spyropoulos,
C.: Symbolic and neural learning for named-entity recognition. In: Symposium on
Computational Intelligence and Learning. pp. 58–66. Citeseer, Chios, Greece (2000)
24. dos Santos, C., Guimaraes, V., RJ Niterói, a.R.d.J.: Boosting named entity recog-
nition with neural character embeddings. In: Proceedings of NEWS 2015 The Fifth
Named Entities Workshop. pp. 25–33 (2015)

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1705_04044_end_to_end_recurrent_neural_network_models_for_vietnamese_named_entity_recogniti
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2017/1705_04044_END_TO_END_RECURRENT_NEURAL_NETWORK_MODELS_FOR_VIETNAMESE_NAMED_ENTITY_RECOGNITI.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

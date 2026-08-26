---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1911.03648
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1911.03648_Hate_Speech_Detection_on_Vietnamese_Social_Media_Text_using_the_Bidirectional-LS

> Source: 1911.03648_Hate_Speech_Detection_on_Vietnamese_Social_Media_Text_using_the_Bidirectional-LS.pdf

> Pages: 4

---


## Page 1


Hate Speech Detection on Vietnamese Social Media
Text using the Bidirectional-LSTM Model
Hang Thi-Thuy Do, Huy Duc Huynh, Kiet Van Nguyen, Ngan Luu-Thuy Nguyen and Anh Gia-Tuan Nguyen
University of Information Technology, VNU-HCM
{16520339, 16520508}@gm.uit.edu.vn, {kietnv, ngannlt, anhngt}@uit.edu.vn
Abstract—In this paper, we describe our system which par-
ticipates in the shared task of Hate Speech Detection on Social
Networks of VLSP 2019 evaluation campaign. We are provided
with the pre-labeled dataset and an unlabeled dataset for social
media comments or posts. Our mission is to pre-process and
build machine learning models to classify comments/posts. In
this report, we use Bidirectional Long Short-Term Memory to
build the model that can predict labels for social media text
according to Clean, Offensive, Hate. With this system, we achieve
comparative results with 71.43% on the public standard test set
of VLSP 2019.
Index Terms—Bi-LSTM, Hate Speech Detection, Vietnamese,
Social Media Text
I. INTRODUCTION
In recent years, social networking has grown and become
prevalent with every people, it makes easy for people to
interact and share with each other. However, every problem
has two sides. It also has some negative issues, hate speech is
a hot topic in the domain of social media. With the freedom of
speech on social networks and anonymity on the internet, some
people are free to comment on hate and insults. Hate speech
can have an adverse effect on human behavior as well as
directly affect society. We don’t manually delete each of those
comments, which is time-consuming and boring. This spurs
research to build an automated system that detects hate speech
and eliminates them. With that system, we can detect and
eliminate hate speech and thus reduce their spread on social
media. With Vietnamese, we can use methods to apply spe-
ciﬁc extraction techniques manually and in combination with
string labeling algorithms such as Conditional Random Field
(CRF)[1], Model Hidden Markov (HMM)[2] or Entropy[3].
However, we have to choose the features manually to bring the
model with high accuracy. Deep Neural Network architectures
can handle the weaknesses of the above methods. In this report
we apply Bidirectional Long Short-Term Memory (Bi-LSTM)
to build the model. Also combined with the word embedding
matrix to increase the accuracy of the model.
The rest of the paper is organized as follows. In section
2, we presented the related work. In section 3, we described
our Bi-LSTM system. In sections 4 and 5, we presented
the experimental process and results. Finally, section 6 gives
conclusions about the work.
II. RELATED WORK
Gao and Huang (2017)[4] used BiLSTMs with attention
mechanism 372 to detect hate speech. They illustrated that
the Bi-directional LSTM model with attention mechanism
achieves the high performance. They hypothesize that this
is because hate indicator phrases are often concentrated in
a small region of a comment, which is especially the case
for long comments. Davidson et al. (2017)[5] train a model
to differentiate among three classes: containing hate speech,
only offensive language, or neither.Jing Qian, Mai ElSherief,
Elizabeth Belding, William Yang Wang (2018) [6] worked on
classifying a tweet as racist, sexist or neither by multiple deep
learning architectures. ABARUAH at SemEval-2019 [7] pre-
sented the results obtained using bi-directional long short-term
memory (BiLSTM) with and without attention and Logistic
Regression (LR) models for multilingual detection of hate
speech against immigrants and women in Twitter. Animesh
Koratana and Kevin Hu [8] use many machine learning models
to detect toxic words, in which the Bi-Lstm model got the
highest performance. Malmasi and Zampieri (2017)[9] made a
similar study to compare the performance of different features
in detecting hate speech.
III. BI-LSTM MODEL FOR VIETNAMESE HATE SPEECH
DETECTION
As mentioned previously, we propose a framework based
on the ensemble of Bi-LSTM models to perform hate speech
detection with the provided dataset. Besides, we also imple-
mented some more models to compare and ﬁnd the optimal
model for the task.
A. Long Short-Term Memory
LSTM takes words from an input sentence in a distributed
word representation format. LSTM’s network architecture
includes memory cells and ports that allow the storage or
retrieval of information. These gates help the LSTM memory
cell to perform a write, read and reset operation. They enable
the LSTM memory cell to store and access information over
a period of time.
B. Bidirectional Long Short-Term Memory
One drawback of LSTM architecture[10] is that they are
only considering the previous context. However, the identiﬁ-
cation of a word depends not only on the previous context
arXiv:1911.03648v1  [cs.CL]  9 Nov 2019


## Page 2


but also on the subsequent context. Bidirectional LSTM (Bi-
LSTM)[11] was created to overcome this weakness. A Bi-
LSTM architecture usually contains two single LSTM net-
works used simultaneously and independently to model input
chains in two directions: forward LSTM and backward LSTM.
Fig. 1. Bi-LSTM architecture [12]
IV. PRE-PROCESSING
The pre-processing performed on the text includes the
following:
• The comments were converted to lowercase.
• The URLs, mentions (@) and non-alphabetic characters
are removed (number, excess whitespace).
• Several stopwords were removed from the comments.
We don’t remove all stopword because having a few
stopwords affect the results.
• A few characters that don’t affect the results are replaced
by an empty string.
• Using Tokenizer to convert each comment into a sequence
of integers.
V. EXPERIMENTS
A. Dataset and Word Embeddings
VLSP Shared Task 2019: Hate Speech Detection on Social
Networks: This dataset includes 25431 items in csv format,
the dataset was divided into two ﬁle, training dataset with
20345 items and test dataset with 5086 items. Each data
line of training dataset is assigned 1 of 3 labels CLEAN,
OFFENSIVE or HATE. The test dataset is not assign label.
The statistic summarization of the given training dataset is
described in Table I.
• Hate speech (HATE) contains the abusive language,
which often bears the purpose of insulting individuals
or groups, and can include hate speech, derogatory and
offensive language. An item is identiﬁed as hate speech
if it (1) targets individuals or groups on the basis of their
characteristics; (2) demonstrates a clear intention to incite
harm, or to promote hatred; (3) may or may not use
offensive or profane words.
• Offensive but not hate speech (OFFENSIVE) is an
item (posts/comments) may contain offensive words but
it does not target individuals or groups on the basis of
their characteristics.
• Neither offensive nor hate speech (CLEAN) is a normal
item. It’s conversations, expressing emotions normally. It
does not contain offensive language or hate speech.
In this paper, we use two different word embeddings to com-
pare and ﬁnd out the best word embedding such as Word2Vec
[17] and FastText [16]. We used pre-trained vector with large
dimensions to increase the accuracy of the model. Through
experiments we found FastText achieved better results.
TABLE I
THE STATISTIC OF VLSP 2019 HSDOSN TRAINING DATASET
CLEAN
OFFENSIVE
HATE
TOTAL
Frequency
18614
1022
709
20345
Percentage
91.49%
5.02%
3.49%
100%
For this public dataset, we ﬁnd that the dataset is an
unbalanced dataset. The CLEAN label has the highest rate
with 91.49% and the HATE label is lowest with 3.49%.
Therefore, it is difﬁcult and challenging to ﬁnd a good model
for this task.
B. Evaluation on each Model
For problems of this type, there are many models suitable
to handle such as: SVM, Bi-LTSM, LR, GRU, CNN and etc.
To solve this problem, we implement four different models
(SVM, LR, Bi-LSTM, and GRU) to compare and ﬁnd the
most suitable one. To evaluate the four models on this task,
we divide the training dataset into two parts training, testing
rate of 80%, 20% respectively.
The details of our models are provided below.
1. Support Vector Machine (SVM)
Support Vector Machines (SVMs) are a popular machine
learning method for classiﬁcation, regression, and other learn-
ing tasks [13]. It is often used for two-class classiﬁcation
problems. For this problem, it has three labels, so we use
the SVM to classify twice, two label at a time.Firstly, we
classify two label 0 and 1, we achieved accuracy, precision,
recall, and F1-score rates of 96.00%, 93.37%, 98.96%, and
96.08% respectively, on training dataset. Second time, we
classify two label 1 and 2, we achieved accuracy, precision,
recall, and F1-score rates of 84.34%, 87.38%, 78.86%, and
82.90% respectively. We ﬁnd that this model doesn’t classify
well for two labels 1 and 2. Moreover, when we check this
model with the public-test, it brings the result as not good as
we expected with 63.87%.
2. Logistic Regression (LR)
Logistic regression is basically a supervised classiﬁcation
algorithm. In a classiﬁcation problem, the target variable(or
output), can take only discrete values for a given set of
features(or inputs) [14]. We have applied it to this problem
as follows: Firstly, we use the TﬁdfVectorizer tool to convert
text into feature vectors that are used as input for the model.


## Page 3


Then, we used the Logistic Regression model to predict the
classiﬁcation results. When checking it on training datasets,
we achieved accuracy, precision, recall, and F1-score rates of
94.17%, 88.87%, 55.54%, and 64.15% respectively. We also
try submitting this model’s result on the system, the result is
worse we thought with 51.15%
3. Gated Recurrent Units (GRU)
The Recurrent Neural Network (RNN) handles the variable-
length sequence by having a recurrent hidden state whose
activation at each time is dependent on that of the previous
time [15]. The GRU is a variant of RNN and it only has
two inputs. We have used it into this problem as follows: We
have used it with word embeddings Fasttext [16]. First, we use
Tokenizer() for sequences because GRU is good at processing
long sequences. Then, we have applied this model to the
problem. We achieved accuracy, precision, recall, and F1-score
rates of 94.61%, 67.12%, 59.66%, and 64.15% respectively,
on the training dataset. When we check this model with the
public dataset, it brings the result quite good with 65.01%
4. Bidirectional Long Short-Term Memory (Bi-LSTM)
The LSTM is a famous variant of RNN. The Bidirectional
Long Short Term Memory can be trained using all available
input information in the past and future of a speciﬁc time
frame. We have applied it with word embeddings Fasttext [16]
and baomoi.vn.model.txt [17]. As follows:
As well as the GRU, we also used GloVe Embedding for
sequences and applied this model for the problem. When us-
ing word embeddings baomoi.vn.model.txt [17], we achieved
accuracy, precision, recall, and F1-score rates of 93.26%,
90.74%, 50.30%, and 53.62% respectively, on the training
dataset. The same with word embeddings Fasttext [16], we
achieved accuracy, precision, recall, and F1-score rates of
95.67%, 85.61%, 67.36%, and 73.84% respectively, on the
training dataset. We ﬁnd that when combining the Bi-LSTM
with fasttext will bring the result better. When we check it
with the public dataset, it brings the result good with 71.43%
C. Experimental Results
After conducting experiments on many models, we obtained
the following results on public-test, shown in Table II.
TABLE II
THE RESULTS TABLE OF MODELS.
Model
F1-Score
SVM
63.87
LR
51.15
GRU
65.01
Bi-LSTM
71.43
We achieved the best result with Bi-LSTM, ranking the 2nd
of the scoreboard on the public-test set shown in Table III.
However, our result ranks the 6th of the scoreboard on the
private-test set.
VI. CONCLUSION AND FUTURE WORK
In this paper, we have presented our approach to address
Vietnamese hate speech detection task proposed at the VLSP
TABLE III
THE RESULTS TABLE OF THE TOP 5 ON PUBLIC-TEST SET
Rank
Team
F1-score
1
Try hard
73.01
2
HH UIT
71.43
3
titanic
70.74
4
ABCD
70.58
5
TIN HUYNH
70.57
Shared Task 2019. We develop the system using Bidirectional
Long Short Memory for classifying three different labels in
this task. We participate in this and evaluate the performance
of our system on this dataset. As a result, our result is
71.43% of F1-score, ranking the 2nd of the scoreboard on
the public-test set.
In the future work, we plan to address this problem in
different ways to enhance the performance of this task. We will
investigate experiments both in traditional machine learning
and types of deep learning for this problem. In addition, we
also analyze experimental results on this task to choose the
efﬁcient approach such as the hybrid approach which combines
machine learning and rule-based approaches to boost the result
of detecting hate speech on Vietnamese social media text.
ACKNOWLEDGMENT
We would like to thank the VLSP Shared Task 2019
organizers for their really hard work and providing the dataset
of Vietnamese Hate Speech Detection on social networks for
our experiments.
REFERENCES
[1] An Introduction to Conditional Random Fields for Relational Learning.
[2] P. Blunsom, Hidden markov models, Lect. notes, August, vol. 15, no.
1819, p. 48, 2004.
[3] K. Nigam, J. Lafferty, and A. McCallum, Using maximum entropy
for text classiﬁcation, in IJCAI-99 workshop on machine learning for
information ﬁltering, 1999, vol. 1, no. 1, pp. 6167.
[4] Lei Gao and Ruihong Huang. 2017. Detecting online hate speech using
context aware models. In Proceedings of the International Conference
Recent Advances in Natural Language Processing, RANLP 2017, pages
260266, Varna, Bulgaria. INCOMA Ltd.
[5] Thomas Davidson, Dana Warmsley, Michael Macy, and Ingmar Weber.
2017. Automated Hate Speech Detection and the Problem of Offensive
Language. In Proceedings of the Eleventh International AAAI Confer-
ence on Web and Social Media (ICWSM 2017), pages 512515, Montreal.
[6] J. Qian, M. ElSherief, E. M. Belding, and W. Y. Wang, Leveraging intra-
user and inter-user representation learning for automated hate speech
detection, arXiv Prepr. arXiv1804.03124, 2018.
[7] A. Baruah, F. Barbhuiya, and K. Dey, ABARUAH at SemEval-2019
Task 5: Bi-directional LSTM for Hate Speech Detection, in Proceedings
of the 13th International Workshop on Semantic Evaluation, 2019, pp.
371376.
[8] Kevin
Hu,
Animesh
Koratana,
CS
224n
Winter
2019:
Toxic
Speech
Detection,
2019.
[Online].
Available:
http://web.stanford.edu/class/cs224n/posters/15744362.pdf.
[9] S. Malmasi and M. Zampieri, Detecting hate speech in social media,
arXiv Prepr. arXiv1712.06427, 2017.
[10] Sepp Hochreiter and Jurgen Schmidhuber. Long short-term mem-
ory.Neural computation, 9(8):17351780, 1997.
[11] Guillaume Lample, Miguel Ballesteros, Sandeep Subramanian, Kazuya
Kawakami, and Chris Dyer. Neural architectures for named entity
recognition. arXiv preprint arXiv:1603.01360, 2016.


## Page 4


[12] Kunal Bhashkar, ”Spelling Correction Using Deep Learning: How Bi-
Directional LSTM with Attention Flow works in Spelling Correction,”,
URL:
https://medium.com/@BhashkarKunal/spelling-correction-using-
deep-learning-how-bi-directional-lstm-with-attention-ﬂow-works-in-
366fabcc7a2f.
[13] Chih-Chung
Chang
and
Chih-Jen
Lin.
LIBSVM:
a
library
for
support
vector
machines,
2001.
Paper
available
at
https://www.csie.ntu.edu.tw/ cjlin/papers/libsvm.pdf.
[14] https://www.geeksforgeeks.org/understanding-logistic-regression/
[15] NGUYEN
Hong
Thinh,
RNN
on
Machine
Reading
Com-
prehension
-
Bi-Directional
Attention
Flow
model,
URL:
https://pdfs.semanticscholar.org/8b9d/677ec3845b2a9b7cb200cdc73dfc.
[16] E. Grave, P. Bojanowski, P. Gupta, A. Joulin, and T. Mikolov, Learning
word vectors for 157 languages, arXiv Prepr. arXiv1802.06893, 2018.
[17] Xuan-Son Vu, ”Pre-trained Word2Vec models for Vietnamese,”, 2016,
url: https://github.com/sonvx/word2vecVN

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
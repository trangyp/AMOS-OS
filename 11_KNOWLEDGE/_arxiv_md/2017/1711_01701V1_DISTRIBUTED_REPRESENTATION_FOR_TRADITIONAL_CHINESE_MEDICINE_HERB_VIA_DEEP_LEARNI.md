---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1711.01701v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1711.01701v1_Distributed_Representation_for_Traditional_Chinese_Medicine_Herb_via_Deep_Learni

> Source: 1711.01701v1_Distributed_Representation_for_Traditional_Chinese_Medicine_Herb_via_Deep_Learni.pdf

> Pages: 8

---


## Page 1


arXiv:1711.01701v1  [cs.CL]  6 Nov 2017
Distributed Representation for Traditional Chinese Medicine Herb via
Deep Learning Models
Wei Li
MOE Key Laboratory of
Computational Linguistics
Department of Computer Science
Peking University
liweitj47@pku.edu.cn
Zheng Yang
School of Chinese Medicine
Beijing University of Chinese Medicine
yangzheng@bucm.edu.cn
Abstract
Traditional Chinese Medicine (TCM) has ac-
cumulated a big amount of precious resource
in the long history of development. TCM pre-
scriptions that consist of TCM herbs are an
important form of TCM treatment, which are
similar to natural language documents, but in
a weakly ordered fashion. Directly adapting
language modeling style methods to learn the
embeddings of the herbs can be problematic
as the herbs are not strictly in order, the herbs
in the front of the prescription can be con-
nected to the very last ones.
In this paper,
we propose to represent TCM herbs with dis-
tributed representations via Prescription Level
Language Modeling (PLLM). In one of our
experiments, the correlation between our cal-
culated similarity between medicines and the
judgment of professionals achieves a Spear-
man score of 55.35 indicating a strong correla-
tion, which surpasses human beginners (TCM
related ﬁeld bachelor student) by a big margin
(over 10%).
1
Introduction
Traditional Chinese Medicine (TCM) has accumu-
lated a large amount of data during the long term
of development, a big part of which embodies as
TCM prescriptions. TCM herbs, also known as
materia medica, is one of the most important ways
of TCM treatment, whose form is the prescriptions
that doctor gives based on his/her observation and
judgment on the patients’ condition.
The prescriptions consist of various kinds and
doses of herbs. We show an example of a famous
TCM prescription called Xiao Chai Hu Tang (小
柴胡汤) in Table 1.
Doctors would adjust the
doses of the herbs according to the speciﬁc con-
dition of the patient. The herbs have their own
natures, for instance, ”warm (温)” , ”cool (凉)” ,
”cold (寒)” and ”hot (热)” . Apart from this, the
compatibility of medicines also plays a very im-
portant role, for example, some certain patterns of
combination are strictly prohibited in TCM guid-
ance called ”eighteen pairs of strictly prohibited
medicine combination (十八反) ”. This indicates
that modeling the matching patterns behind the
herbs in the prescription is necessary if we want
to bring Artiﬁcial Intelligence into TCM treatment
procedure.
As the development of data driven kind of ma-
chine learning algorithms like deep learning, it
has achieved signiﬁcant improvement in the natu-
ral language processing (NLP) ﬁeld. For instance,
neural machine translation (Bahdanau et al., 2014;
Sutskever et al., 2014; Sun et al., 2017),
text
summarization
(Ma and Sun,
2017;
Ma et al.,
2017) question answering (Rajpurkar et al., 2016;
Wang and Jiang, 2016), automatic dialogue gener-
ation (Li et al., 2016) and so on. How to apply
deep learning to TCM ﬁeld, which seems relevant
to NLP, then becomes an interesting question.
Table 1: An example of TCM prescription
Name
Xiao Chai Hu Tang (小柴胡汤)
Composition
radix
bupleuri,
Pinellia
ter-
nata,
ginseng,
licorice
root,
Scutellaria baicalensis, ginger,
Chinese-date
Translation
柴胡、半夏、人参、甘草、
黄芩、生姜、大枣。
Previous works have attempted to use prob-
abilistic topic models such as Latent Dirichlet
Allocation (LDA) and Latent Semantic Analy-
sis (LSA) to describe the properties of the herbs
(Zhang, 2011; Zhipeng et al., 2017).
In NLP
ﬁeld, the neural network based word embedding
models (Mikolov et al., 2013b; Pennington et al.,


## Page 2


2014) have achieved great success, and laid a good
foundation for the development and application of
deep learning models (Collobert et al., 2011). In
this paper, we propose to learn the distributed rep-
resentation of TCM herbs by a way analogous to
the word embeddings in NLP, which can be hope-
fully helpful to the further development of TCM
research.
However, TCM prescriptions are not exactly
like natural language sentences. TCM prescrip-
tions have their own way of organizing the herbs,
which are often put in a weakly ordered way. The
herbs in the front of the prescription may be con-
nected with the very last herb instead of the sur-
rounding ones. In our learning process, We see
each prescription as a sequence of tokens.
The
herbs form the context to each other.
By pre-
dicting the central herb with the corresponding
context, we can learn the representation of each
herb, which contains the information of the pat-
terns of combination, indicating some of the prop-
erties of the herbs. In our experiments we see that
ﬁrst modeling the prescription as a whole provides
much better results than traditional language mod-
eling style methods.
Although there has been thousands of TCM pre-
scriptions in the history, because of the lack of dig-
italization, there has not been much structured dig-
ital resources. In this paper, we collect large scale
digital resources from the Internet.
After some
steps of formalization and cleaning of the data,
we get over 80,000 TCM prescriptions. By pre-
dicting the randomly chosen central herb based on
the corresponding context, we can learn the rep-
resentation of each herb, which contains the in-
formation of the patterns of combination. In this
paper we propose a Prescription Level Language
Modeling (PLLM) that predicts the central herb by
ﬁrst modeling the whole prescription. In our ex-
periments we observe that our PLLM method per-
forms much better than traditional language mod-
eling style methods. Apart from these, we also
propose one possible way of applying deep learn-
ing to assist doctors in TCM treatment in the real
life.
Our contributions mainly lie in the following as-
pects:
• We clean and formalize a large scale of TCM
data from the Internet and provide a dataset
for training and testing the quality of herb
embeddings.
• We propose to represent TCM herbs with
distributed embeddings, and propose a Pre-
scription Level Language Modeling (PLLM)
method to learn the distributed representa-
tions of the TCM herbs. In the experiments
we see that modeling the prescription as a
whole is better than directly applying lan-
guage modeling method.
• We propose a possible way to assist TCM
doctors to compose prescriptions with deep
learning methods.
2
Related Work
2.1
Computational TCM Methods
Zhou et al. (2010) attempted to build TCM clinical
data warehouse to make use of TCM knowledge.
This is a typical way of collecting big data, since
the number of prescriptions given by the doctors
in the clinics is very large. However, in reality,
besides the problem of quality, most of the TCM
doctors don’t use these digital systems. Therefore,
we choose prescriptions in the traditional classics
of TCM. Although this may suffer from the loss
of data magnitude, it guarantees the quality of the
prescriptions.
Wang et al. (2004) attempted to construct a self-
learning expert system with several simple clas-
siﬁers to facilitate the TCM diagnosis procedure,
Wang (2013) proposed to use deep learning and
CRF based multi-labeling learning methods to
model TCM inquiry process, but their systems
are too simple to be actually effective in the real
life TCM diagnosis. Lukman et al. (2007) made a
survey on some computational methods on TCM,
while these methods utilize traditional data mining
methods.
2.2
Distributed Word Embedding
Bengio et al. (2003) ﬁrst proposed to learn the dis-
tributed representation of words while predicting
the next word in a sequence to ﬁght the curse of di-
mensionality. Mikolov et al. (2010) followed this
thread by expanding the simple feed forward neu-
ral networks to recurrent neural networks, hoping
to capture longer distance dependency. These two
models still largely resembles the framework of
probabilistic language modeling.
Mikolov et al. (2013b,a) proposed two very
simple yet effective models called continuous bag
of words (CBOW) and skip gram. CBOW pre-
dicts the central word in a context window based


## Page 3


on the words in the window with a simple logis-
tic regression classiﬁer. Skip gram uses the same
architecture but predicts the context words based
on the central word.
Although these two mod-
els achieved very good results in many kinds of
tasks, they suffer from the loss of not being able
to utilize global information. To tackle this prob-
lem, Pennington et al. (2014) proposed a Global
Vector model (GloVe), which aims to combine
the advantage of both LSA model and the CBOW
model. We develop our methods to learn the dis-
tributed representations of herbs inspired by the
above ideas while modeling the prescription as a
whole rather than using limited context window.
3
Data Construction
When constructing our TCM prescription dataset,
we ﬁrst considered the TCM medical records (中
医医案) in the history, which contain a lot of very
good resource. The medical records are widely
referenced by the doctors in the treatment, how-
ever, they have not been well digitalized, which
makes it hard to extract the prescriptions out of the
descriptive natural language from the records. An-
other way to get large scale prescriptions is from
TCM clinics, the problem is that most of this kind
of valuable data is not publicly available. There-
fore, we turn to Internet resources, which contain
large scale digitalized prescription resources.
We crawl the data from TCM Prescription
Knowledge Base (中医方剂知识库) 1. This
knowledge base includes quite comprehensive
TCM documentations in the history, which also
provides a search engine for prescriptions.
The
database includes 710 TCM historical books or
documentations as well as some modern ones,
consisting of 85,166 prescriptions in total. Each
item in the database provides the name, origin,
compositions, effect, prescription, contraindica-
tions and preparation methods. We clean and for-
malize the database and get 85,161 usable pre-
scriptions2.
In the process of normalization, we temporar-
ily omit the dose information and the prepara-
tion method description, which we may use in
the future.
Word segmentation is typically the
ﬁrst step to Chinese text processing (Xu and Sun,
2016; Zhao et al., 2010; Sun et al., 2014, 2012,
2009). Word segmentation is used to pre-process
1http://www.hhjfsl.com/fang/
2The data and processing code are all available on-line
the text into word based sequences. In addition
to the traditional word segmentation techniques,
we use more heuristics to assist the segmentation
process because this domain has speciﬁc features.
We also write some simple rules to project some
rarely seen herbs to their similar form that is nor-
mally referred to. For example, if the herb appears
less than 5 times and all the characters of the herb
name is a substring of another more popular herb,
then the herb would be mapped to the other one.
This simple projection procedure can partly solve
the data sparsity problem.
3.1
HerbSim80
Similar to the way of building wordsim353
(Finkelstein et al., 2001) , we manually build a
dataset consisting of 80 pairs of herbs, which we
ask three TCM professionals to make a judgment
on how likely the two herbs in the pair would ap-
pear in the same prescription. We then evaluate
the embeddings by calculating the correlation be-
tween the similarity scores given by the cosine dis-
tance of embeddings and the scores given by the
professionals. In Table 2 we show some examples.
Table 2: Examples of HerbSim80. The Chinese char-
acters in Herb 1 and Herb 2 two columns are all herb
names. The scores in S 1, S 2 and S 3 are scores given
by the three professionals. Ave S is the average of three
scores.4
Herb 1
Herb 2
S 1
S 2
S 3
Ave S
乌头
栀子
1
1
1
1.00
麦门冬
山茱萸
3
3
3
3.00
赤芍
藿香
2
2
1
1.67
苍术
乌梅肉
2
1
1
1.33
The detailed procedure is as follows:
1. We randomly generate 120 pairs of TCM
herbs.
2. We invite three TCM professionals, who have
been practicing TCM diagnosis and treatment
for over ﬁve years, to give a score of the herb
pair between 1 and 5. 1 indicates that the two
herbs are very unlikely to appear together in
one prescription. On the contrary, 5 indicates
that the two herbs often appear as a pair in the
same prescription.
3. We rank the pairs by the standard deviation
between the three scores given by the profes-


## Page 4


sionals, and get the top 80 pairs with better
agreement. The ﬁnal score is set to be the
average of the three scores.
4. We invite a junior student who majors in
TCM (student who has just ﬁnished the
course of Principles of TCM Prescriptions) to
do the task, which will be compared with the
result given by the embeddings.
4
Distributed Representations of TCM
Herb
Similar to the one-hot representation in NLP, herbs
can also be represented as one-hot vectors, where
the length of the vector is the size of the whole
herb vocabulary and in each vector, only one slot is
ﬁlled with “1” while others are all “0”. The prob-
lem of this way of representation is that it can not
show the innate relation between herbs, which is
even more important than it is in NLP. For exam-
ple, cinnamon(肉桂) and cinnamon twig (桂枝)
are two different parts of the same plant cinna-
mon tree. The natures of these two herbs are very
similar, but in the one-hot style representation, the
distance between these two herbs are no different
from any other pairs.
Another possible way of representing herbs is
to model the herbs with some features that how
TCM experts view the herbs. For each aspect of
the herb, we can use one-hot vectors to represent
them. This way of representation accords to the
theory of TCM research in the history. For exam-
ple, assume we model each herb from cold and hot
(寒热)、the ﬁve ﬂavors (五味: sweet, sour, bitter,
pungent and salty) two aspects, we can represent a
herb with a 7-length vector. However, to make this
work, it costs very expensive human expert effort,
which makes it impracticable.
Inspired by the way of representing words with
distributed vectors in NLP ﬁeld, we propose to
represent the TCM herbs with distributed repre-
sentations. We model the TCM prescriptions as
documents in NLP, while herbs as words. We can
automatically learn the herb embeddings by tun-
ing the distributed representation of herbs while
predicting the central herb with context herbs in
the prescription. This way the information of the
herb is implicitly embodied in the vectors, and we
can learn the representations automatically from
the dataset we build without much human effort.
Although TCM prescriptions are very similar
to natural language texts, there is one major dif-
ference that in natural language, the order of the
words is very important which is strictly restricted
by syntax and grammar, while in prescriptions,
the order of the herbs usually plays less important
roles. On the other hand, the herbs in the front of a
prescription may be connected to the very last one
instead of its surrounding ones. Based on this ob-
servation, we propose to ﬁrst model the prescrip-
tion as a whole, and then predict the central herb.
4.1
Proposed Baselines
In this subsection, we propose several baseline
models that are directly adapted from NLP ﬁeld.
• Latent Semantic Analysis (LSA) : LSA is
used to analyze the relationship between a
set of documents and the terms they contain
by producing a set of concepts related to the
documents and terms. We model the herbs
as words and prescriptions as documents. We
use a matrix containing herb counts in pre-
scriptions to represent the coexistence rela-
tion between herbs and prescriptions. With
singular value decomposition, we can get a
vector for each herb, which is then used as
the distributed representation of the herbs.
• Continuous
bag
of
words
(CBOW)(Mikolov et al.,
2013b)
:
This
model uses a log-linear regression model
with negative sampling to predict a central
word with the context words within a local
context window.
• Global
vectors
for
word
representation
(GloVe)(Pennington et al.,
2014)
:
This
model uses a global log-bilinear regression
model that combines the advantages of the
global matrix factorization (similar to LSA)
and local context window (similar to CBOW)
methods.
• Recurrent Neural Networks Language Mod-
eling (RNNLM) : This model is similar to
CBOW model in the setting of objective, that
is to predict a herb based on their context
herbs. However, this model aims to model a
longer dependency between herbs by using a
bidirectional gated recurrent neural networks
(BiGRNN) to predict the central herb. This
model predicts the central herb by consider-
ing the herbs both before and after it.


## Page 5


4.2
Prescription Level Language Modeling
In this subsection, We show the details of our
proposed methods, Prescription Level Language
Modeling(PLLM).
softmax
herb 
embeddings
hidden 
states
Central Herb 
to be 
predicted
Prescription 
Level Vector 
by last 
pooling
Figure 1: An illustration of Prescription Level Lan-
guage Modeling with BiGRNN
In this subsection, We show the details of our
proposed Prescription Level Language Modeling.
As is shown in Figure 1, we ﬁrst encode the whole
prescription (except the central herb) into a pre-
scription level vector (vector that encodes the in-
formation of the whole prescription) hc, and then
predict the central herb based on this prescription
level vector hc.
1. We take the one-hot herbs in the prescrip-
tion w1, ..., wt−1, wt+1, ...wn as input, and
project them into the corresponding embed-
dings e1, ...et−1, et+1, ..., en.
2. Then we go over the whole prescription ex-
cept the central word to be predicted wt with
BiGRNN, which gives us the hidden states
h1, ..., ht−1, ht+1, ..., hn.
3. After that, We apply last pooling with the
hidden states, and get the context vector hc,
which is expected to embody the information
of the whole prescription.
4. Finally, we use a softmax regression layer
to predict the central herb.
We encode the whole prescription into a ﬁxed
length vector hc in order to capture the depen-
dency beyond the local windows of the herbs. In
this way, even the last herb can be an auxiliary
to the ﬁrst herb in the prescription. We believe
this is very important compared with the baseline
RNNLM model, as it separates the herbs before
and after the central one. Further more, the vector
of the whole prescription can also be a good repre-
sentation of the disease that the prescription wants
to tackle, which we would like to explore in the
future.
5
Application on TCM Treatment
In the TCM diagnosis and treatment procedure,
different from modern medicine science, doctors
usually have more freedom when writing a pre-
scription based on his own observation instead of a
standard process. Still, they often refer to the clas-
sical prescriptions recorded in the TCM classics,
for instance, Treatise on Febrile Diseases (《伤
寒论》).
In these classics, there are not only
the principles for giving the prescriptions but also
some widely used, carefully constructed prescrip-
tions. In this section, based on this observation, we
propose a language modeling style method based
on the model we learn from the classical prescrip-
tions, which can hopefully give hints to doctors on
writing prescriptions for patients. On thing that
should be noted is that our proposed method is
more of a prototype rather than a complete tool.
Doctors start to write prescriptions after they
have made a judgment on the patients’ situations.
Each time a herb is given, our model would pro-
cess the unﬁnished prescription, and then suggest
a candidate herb that the doctor may want to use.
The CBOW, RNNLM, PLLM models are the same
as described in Section 4. We also apply N-gram
model as our baseline model. N-gram model is
similar to how it is used in NLP, which predicts
the next herb by selecting the herb with the largest
likelihood.
The likelihood is given by the lin-
ear combination of unigram, bigram and trigram
transition probabilities. The parameters of these
models are all trained on the dataset we build,
which consists of classical prescriptions.
After
our model predicts the most probable herb, doc-
tors can choose whether to take the advice or not.
6
Experiments
In all of the following experiments, we use our dis-
tributed herb representations in an unsupervised
way. The distance between two herbs are all given
by the cosine distance between the two vectors.
6.1
Correlation
In this section, we show the correlation results be-
tween the professionals and various models. We


## Page 6


Algorithm 1 TCM prescription auxiliary compo-
sition
Require: The unﬁnished prescription,
trained
model
1: Read in the herbs in the unﬁnished prescrip-
tion
2: Choose a model out of n-gram, RNNLM,
CBOW, PLLM to process the herbs.
3: Predict a herb that ﬁts the current unﬁnished
prescription.
use the HerbSim80 dataset described in Section
3.1.
For LSA, the vector size is set to be 20,
while for other models, the vector size is set to
be 100. The gensim toolkit 5 is used to train the
LSA model. For GloVe6 and CBOW7 we use their
ofﬁcial program respectfully. The similarity score
of two herbs is given by the cosine distance be-
tween the vectors of the herbs.
We use Spear-
man’s rank score as the criteria to evaluate the
correlation between our model and the profession-
als. Our RNNLM, PLLM models are built using
Tensorﬂow toolkit(Abadi et al., 2015). We choose
Adam(Kingma and Ba, 2014) as the optimization
method. An early stopping strategy is adopted to
avoid over-ﬁtting in the training process. We stop
the training process when the accuracy of herb pre-
diction in the development set fails to increase in
the last three training epochs.
In the bottom row of Table 3, we show the cor-
relation result of a human junior student who ma-
jors in TCM. From the table we can see that PLLM
model gives the best result, which surpasses the re-
sult of the student by over 10%. This phenomenon
shows that our PLLM model can learn some useful
knowledge out of the prescriptions in the dataset
with unsupervised learning. An overall descrip-
tion of the prescription can indeed help predicting
the herb. The simple model CBOW also gives a
rather good result of 49.33%. The traditional LSA
model doesn’t perform well in this experiment,
maybe because it omits the local information of
the herbs, which plays a more important role in
TCM prescriptions. GloVe suffers the same prob-
lem that the objective of global part inﬂuences the
representation of the local context.
5http://radimrehurek.com/gensim/
6https://nlp.stanford.edu/projects/glove/
7https://code.google.com/p/word2vec/
Table 3:
Correlation with Professionals’ judgment.
Student means the correlation score with the Junior
student.
Model
Spearman’s R
Student
0.4506
LSA
0.3861
GloVe
0.3952
CBOW
0.4933
RNNLM
0.5158
PLLM
0.5535
6.2
Prediction
In the Section 5, we propose to use our model to
assist doctors to write prescriptions.
We manu-
ally build a test set consisting of 206 prescriptions.
For each prescription, we temporarily blank one
of the herbs, which is randomly chosen, and test
whether our models could predict what the origi-
nal herb is. The original prescriptions all have at
least four herbs. Some examples are shown in Ta-
ble 4, where the herb in the Answer column is the
blank in the Question column.
Table 4: Examples from the test set for herb predic-
tion. The characters in the Question column are TCM
herb names. The characters in the Answer column is
the herb name that should be put into the blank in the
Question
Question
Answer
麻黄
杏仁炙甘草
桂枝
生地黄当归牡丹皮
升麻
黄连
In this experiment, we use bigram and trigram
from both directions for n-gram prediction. For
the prediction score, we simply add up the proba-
bilities with the same weights.
score(i) = p(i|i −1) + p(i|i −2, i −1)
+p(i|i + 1) + p(i|i + 1, i + 2)
(1)
From Table 5 we can see that the baseline model
N-gram is very strong. The accuracy of N-gram
model is even higher than RNNLM model, which
shows that directly transfer the language model-
ing method from NLP may not be a good idea
when predicting the next herb. CBOW model is
slightly different from the original one, we average
all the herb embeddings of the prescription, based
on which we predict the blanked one. We assume
the reason that it gives a rather good result is that
it makes use of a wider range of context. In this


## Page 7


experiment, our PLLM gets the best result, which
is much higher than other models. We assume that
it is necessary to consider the whole prescription
when predicting the next herb.
Again we clarify that this application is a proto-
type. It doesn’t mean that we don’t need to con-
sider other factors like the patients’ situation when
composing a prescription. What we want to show
is that the combination of herbs play an important
role when composing a prescription and our model
can capture this kind of pattern on some level.
Table 5: Accuracy on herb prediction
Model
Accuracy
N-gram
17.96
CBOW
20.39
RNNLM
16.50
PLLM
32.04
6.3
Further Observation
In the experiments, we observe that the distributed
vectors of herbs have linear algebraic relation-
ships. For example, v[熟地黄(prepared rehman-
nia root)] −v[生地黄(dried rehamnnia root)]
≈v [煨姜(roasted ginger)] −v [生姜(ginger)].
This phenomenon is similar to the observa-
tion described in (Mikolov et al., 2013a), where
v[bigger] −v[big] ≈v[smaller] −v[small]. In
the future, we hope to further look into this and
see whether this is a general phenomenon in TCM
herbs.
7
Conclusion and Future Work
In this paper, we propose to represent TCM herbs
with distributed representation via Prescription
Level Language modeling. In the experiments we
testify that simply adopting the methods from NLP
ﬁeld is problematic because of the difference that
lies between natural language and TCM prescrip-
tions. Furthermore, we propose a possible appli-
cation for our models in TCM treatment, which we
hope can facilitate doctors composing prescrip-
tions.
References
Mart´ın Abadi, Ashish Agarwal, Paul Barham, Eu-
gene Brevdo, Zhifeng Chen, Craig Citro, Greg S.
Corrado, Andy Davis,
Jeffrey Dean, Matthieu
Devin, Sanjay Ghemawat, Ian Goodfellow, Andrew
Harp, Geoffrey Irving, Michael Isard, Yangqing
Jia, Rafal Jozefowicz, Lukasz Kaiser, Manjunath
Kudlur, Josh Levenberg, Dan Man´e, Rajat Monga,
Sherry Moore, Derek Murray, Chris Olah, Mike
Schuster, Jonathon Shlens, Benoit Steiner, Ilya
Sutskever, Kunal Talwar, Paul Tucker, Vincent Van-
houcke, Vijay Vasudevan, Fernanda Vi´egas, Oriol
Vinyals, Pete Warden, Martin Wattenberg, Mar-
tin Wicke, Yuan Yu, and Xiaoqiang Zheng. 2015.
TensorFlow: Large-scale machine learning on heterogeneous systems
Software
available
from
tensorﬂow.org.
http://tensorflow.org/.
Dzmitry Bahdanau, Kyunghyun Cho, and Yoshua Ben-
gio. 2014.
Neural machine translation by jointly
learning to align and translate.
arXiv preprint
arXiv:1409.0473 .
Yoshua Bengio, R´ejean Ducharme, Pascal Vincent, and
Christian Jauvin. 2003. A neural probabilistic lan-
guage model. Journal of machine learning research
3(Feb):1137–1155.
Ronan Collobert, Jason Weston, L´eon Bottou, Michael
Karlen, Koray Kavukcuoglu, and Pavel Kuksa.
2011. Natural language processing (almost) from
scratch.
Journal of Machine Learning Research
12(Aug):2493–2537.
Lev Finkelstein, Evgeniy Gabrilovich, Yossi Matias,
Ehud Rivlin, Zach Solan, Gadi Wolfman, and Eytan
Ruppin. 2001. Placing search in context: The con-
cept revisited. In Proceedings of the 10th interna-
tional conference on World Wide Web. ACM, pages
406–414.
Diederik Kingma and Jimmy Ba. 2014.
Adam: A
method for stochastic optimization. arXiv preprint
arXiv:1412.6980 .
Jiwei Li, Will Monroe, Alan Ritter, Michel Galley,
Jianfeng Gao, and Dan Jurafsky. 2016. Deep rein-
forcement learning for dialogue generation. arXiv
preprint arXiv:1606.01541 .
Suryani Lukman, Yulan He, and Siu-Cheung Hui.
2007. Computational methods for traditional chi-
nese medicine: a survey. Computer methods and
programs in biomedicine 88(3):283–294.
Shuming
Ma
and
Xu
Sun.
2017.
A semantic relevance based neural network for text summarization an
CoRR
abs/1710.02318.
http://arxiv.org/abs/1710.02318.
Shuming
Ma,
Xu
Sun,
Jingjing
Xu,
Houfeng
Wang,
Wenjie
Li,
and
Qi
Su.
2017.
Improving semantic relevance for sequence-to-sequence learning of c
In Proceedings of the 55th Annual Meeting of
the Association for Computational Linguistics,
ACL 2017, Vancouver, Canada, July 30 - Au-
gust 4, Volume 2: Short Papers. pages 635–640.
https://doi.org/10.18653/v1/P17-2100.
Tomas Mikolov, Kai Chen, Greg Corrado, and Jef-
frey Dean. 2013a.
Efﬁcient estimation of word
representations in vector space.
arXiv preprint
arXiv:1301.3781 .


## Page 8


Tomas Mikolov, Martin Karaﬁ´at, Lukas Burget, Jan
Cernock`y, and Sanjeev Khudanpur. 2010.
Recur-
rent neural network based language model. In Inter-
speech. volume 2, page 3.
Tomas Mikolov, Ilya Sutskever, Kai Chen, Greg S Cor-
rado, and Jeff Dean. 2013b. Distributed representa-
tions of words and phrases and their compositional-
ity. In Advances in neural information processing
systems. pages 3111–3119.
Jeffrey Pennington, Richard Socher, and Christopher D
Manning. 2014.
Glove: Global vectors for word
representation. In EMNLP. volume 14, pages 1532–
1543.
Pranav Rajpurkar, Jian Zhang, Konstantin Lopyrev, and
Percy Liang. 2016.
Squad: 100,000+ questions
for machine comprehension of text. arXiv preprint
arXiv:1606.05250 .
Xu Sun, Wenjie Li, Houfeng Wang, and Qin Lu. 2014.
Feature-frequency-adaptive on-line training for fast
and accurate natural language processing. Compu-
tational Linguistics 40(3):563–586.
Xu Sun,
Houfeng Wang,
and Wenjie Li. 2012.
Fast online training with frequency-adaptive learning rates for chinese word segmentation and new word detection.
In The 50th Annual Meeting of the Association
for Computational Linguistics,
Proceedings of
the Conference, July 8-14, 2012, Jeju Island,
Korea - Volume 1: Long Papers. pages 253–262.
http://www.aclweb.org/anthology/P12-1027.
Xu
Sun,
Bingzhen
Wei,
Xuancheng
Ren,
and
Shuming
Ma.
2017.
Label embedding network: Learning label representation for soft training of deep networks.
CoRR
abs/1710.10393.
http://arxiv.org/abs/1710.10393.
Xu
Sun,
Yao-zhong Zhang,
Takuya Matsuzaki,
Yoshimasa Tsuruoka, and Jun’ichi Tsujii. 2009.
A discriminative latent variable chinese segmenter with hybrid word/character information.
In Human Language Technologies: Conference of
the North American Chapter of the Association of
Computational Linguistics, Proceedings, May 31 -
June 5, 2009, Boulder, Colorado, USA. pages 56–64.
http://www.aclweb.org/anthology/N09-1007.
Ilya Sutskever, Oriol Vinyals, and Quoc V Le. 2014.
Sequence to sequence learning with neural net-
works. In Advances in neural information process-
ing systems. pages 3104–3112.
Liwen Wang. 2013. TCM inquiry modelling research
based on Deep Learning and Conditional Random
Field multi-lable learning methods.
Ph.D. thesis,
East China University of Science and Technology.
Shuohang Wang and Jing Jiang. 2016. Machine com-
prehension using match-lstm and answer pointer.
arXiv preprint arXiv:1608.07905 .
Xuewei Wang, Haibin Qu, Ping Liu, and Yiyu Cheng.
2004. A self-learning expert system for diagnosis
in traditional chinese medicine. Expert systems with
applications 26(4):557–566.
Jingjing
Xu
and
Xu
Sun.
2016.
Dependency-based gated recursive neural network for chinese word se
In
Proceedings
of
the
54th
Annual
Meet-
ing
of
the
Association
for
Computational
Linguistics,
ACL
2016,
August
7-12,
2016,
Berlin,
Germany,
Volume
2:
Short
Papers.
http://aclweb.org/anthology/P/P16/P16-2092.pdf.
Xiaoping Zhang. 2011. Topic Modelling and its ap-
plication in TCM clinical diagonosis and treatment.
Ph.D. thesis, Beijing Transportation University.
Hai
Zhao,
Changning
Huang,
Mu
Li,
and
Bao-Liang
Lu.
2010.
A uniﬁed character-based tagging framework for chinese word segme
ACM
Trans.
Asian
Lang.
Inf.
Process.
9(2).
http://dblp.uni-trier.de/db/journals/talip/tal
Zhu Zhipeng, Du Jianqiang, Liu Yingfeng, Yu Fang,
and Jigen Luo. 2017. Tcm prescription similartiy
computation based on lda topic modelling. Applica-
tion Research Of Computers pages 1668–1670.
Xuezhong Zhou, Shibo Chen, Baoyan Liu, Runsun
Zhang, Yinghui Wang, Ping Li, Yufeng Guo, Hua
Zhang, Zhuye Gao, and Xiufeng Yan. 2010. Devel-
opment of traditional chinese medicine clinical data
warehouse for medical knowledge discovery and de-
cision support.
Artiﬁcial Intelligence in medicine
48(2):139–152.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
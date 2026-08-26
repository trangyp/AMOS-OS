---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1906.07662
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1906.07662_State-of-the-Art_Vietnamese_Word_Segmentation

> Source: 1906.07662_State-of-the-Art_Vietnamese_Word_Segmentation.pdf

> Pages: 6

---


## Page 1


State-of-the-Art Vietnamese Word Segmentation
Song Nguyen Duc Cong
Computer Science Department
Assumption University
Bangkok, Thailand
st5429822@au.edu
Quoc Hung Ngo
University of Information Technology
Ho Chi Minh City, Vietnam
hungnq@uit.edu.vn
Rachsuda Jiamthapthaksin
Computer Science Department
Assumption University
Bangkok, Thailand
rachsuda@scitech.au.edu
Abstract—Word segmentation is the ﬁrst step of any tasks
in Vietnamese language processing. This paper reviews state-
of-the-art approaches and systems for word segmentation in
Vietnamese. To have an overview of all stages from building
corpora to developing toolkits, we discuss building the corpus
stage, approaches applied to solve the word segmentation and
existing toolkits to segment words in Vietnamese sentences. In
addition, this study shows clearly the motivations on building cor-
pus and implementing machine learning techniques to improve
the accuracy for Vietnamese word segmentation. According to
our observation, this study also reports a few of achivements and
limitations in existing Vietnamese word segmentation systems.
Index Terms—Vietnamese word segmentation; text modelling;
Vietnamese corpus
I. INTRODUCTION
Lexical analysis, syntactic analysis, semantic analysis, dis-
closure analysis and pragmatic analysis are ﬁve main steps in
natural language processing [1], [2]. While morphology is a
basic task in lexical analysis of English, word segmentation
is considered a basic task in lexical analysis of Vietnamese
and other East Asian languages processing. This task is to
determine borders between words in a sentence. In other
words, it is segmenting a list of tokens into a list of words
such that words are meaningful.
Word segmentation is the primary step in prior to other
natural language processing tasks i. e., term extraction and
linguistic analysis (as shown in Figure 1). It identiﬁes the
basic meaningful units in input texts which will be processed
in the next steps of several applications. For named entity
recognization [3], word segmentation chunks sentences in
input documents into sequences of words before they are
further classiﬁed in to named entity classes. For Vietnamese
language, words and candidate terms can be extracted from
Vietnamese copora (such as books, novels, news, and so
on) by using a word segmentation tool. Conformed features
and context of these words and terms are used to identify
named entity tags, topic of documents, or function words. For
linguistic analysis, several linguistic features from dictionaries
can be used either to annotating POS tags or to identifying the
answer sentences. Moreover, language models can be trained
by using machine learning approaches and be used in tagging
systems, like the named entity recognization system of Tran
et al. [3].
Many studies forcus on word segmentation for Asian lan-
guages, such as: Chinese, Japanese, Burmese (Myanmar) and
Thai [4], [5], [6], [7]. Approaches for word segmentation
task are variety, from lexicon-based to machine learning-based
methods. Recently, machine learning-based methods are used
widely to solve this issue, such as: Support Vector Machine or
Conditional Random Fields [8], [9]. In general, Chinese is a
language which has the most studies on the word segmentation
issue. However, there is a lack of survey of word segmentation
studies on Asian languages and Vietnamese as well. This paper
aims reviewing state-of-the-art word segmentation approaches
and systems applying for Vietnamese. This study will be a
foundation for studies on Vietnamese word segmentation and
other following Vietnamese tasks as well, such as part-of-
speech tagger, chunker, or parser systems.
Figure 1. Word segmentation tasks (blue) in the Vietnamese natural lanuage
processing system.
There are several studies about the Vietnamese word seg-
mentation task over the last decade. Dinh et al. started this task
with Weighted Finite State Transducer (WFST) approach and
Neural Network approach [10]. In addition, machine learning
approaches are studied and widely applied to natural language
processing and word segmentation as well. In fact, several
studies used support vector machines (SVM) and conditional
random ﬁelds (CRF) for the word segmentation task [8], [9].
Based on annotated corpora and token-based features, studies
used machine learning approaches to build word segmentation
systems with accuracy about 94%-97%.
According to our observation, we found that is lacks of
complete review approaches, datasets and toolkits which we
recently used in Vietnamese word segmentation. A all sided
arXiv:1906.07662v1  [cs.CL]  18 Jun 2019


## Page 2


review of word segmentation will help next studies on Viet-
namese natural language processing tasks have an up-to-date
guideline and choose the most suitable solution for the task.
The remaining part of the paper is organized as follows.
Section II discusses building corpus in Vietnamese, containing
linguistic issues and the building progress. Section III brieﬂy
mentions methods to model sentences and text in machine
learning systems. Next, learning models and approaches for
labeling and segmenting sequence data will be presented in
Section IV. Section V mainly addresses two existing toolkits,
vnTokenizer and JVnSegmenter, for Vietnamese word segmen-
tation. Several experiments based on mentioned approaches
and toolkits are described in Section VI. Finally, conclusions
and future works are given in Section VII.
II. CORPUS
A. Language Deﬁnition
Vietnamese, like many languages in continental East Asia, is
an isolating language and one branch of Mon-Khmer language
group. The most basic linguistic unit in Vietnamese is mor-
pheme, similar with syllable or token in English and “hình vị”
(phoneme) or “tiếng” (syllable) in Vietnamese. According to
the structured rule of its, Vietnamese can have about 20,000
different syllables (tokens). However, there are about 8,000
syllables used the Vietnamese dictionaries. There are three
methods to identify morphemes in Vietnamese text [11].
• Morpheme is the smallest meaningful unit of Vietnamese.
• Morpheme is the basic unit of Vietnamese.
• Morpheme is the smallest meaningful unit and is not used
independently in the syntax factor.
In computational linguistics, morpheme is the basic unit of
languages as Leonard Bloomﬁeld mentioned for English [12].
In our research for Vietnamese, we consider the morpheme as
syllable, called “tiếng” in Vietnamese (as Nguyen’s deﬁnition
[13]).
The next concept in linguistics is word which has fully
grammar and meaning function in sentences. For Vietnamese,
word is a single morpheme or a group of morphemes, which
are ﬁxed and have full meaning [13]. According to Nguyen,
Vietnamese words are able classiﬁed into two types, (1) 1-
syllable words with fully meaning and (2) n-syllables words
whereas these group of tokens are ﬁxed. Vietnamese syllable
is not fully meaningful. However, it is also explained in the
meaning and structure characteristics. For example, the token
“kỳ” in “quốc kỳ” whereas “quốc” means national, “kỳ” means
ﬂag. Therefore, “quốc kỳ” means national ﬂag.
Consider dictionary used for evaluating the corpus, extract-
ing features for models, and evaluating the systems, there
are many Vietnamese dictionaries, however we recommend
the Vietnamese dictionary of Hoang Phe, so called Hoang
Phe Dictionary. This dictionary has been built by a group of
linguistical scientists at the Linguistic Institute, Vietnam. It
was ﬁrstly published in 1988, reprinted and extended in 2000,
2005 and 2010. The dictionary currently has 45,757 word
items with 15,901 Sino-Vietnamese word items (accounting
for 34.75%) [14].
B. Name Entity Issue
In Vietnamese, not all of meaningful proper names are in
the dictionary. Identifying proper names in input text are also
important issue in word segmentation. This issue is sometimes
included into unknown word issue to be solved. In addition,
named entity recognition has to classify it into several types
such as person, location, organization, time, money, number,
and so on.
Proper name identiﬁcation can be solved by characteristics.
For example, systems use beginning characters of proper
names which are uppercase characters. Moreover, a list of
proper names is also used to identify names in the text.
In particular, a list of 2000 personal names extracted from
VietnamGiaPha, and a list of 707 names of locations in
Vietnam extracted from vi.wikipedia.org are used in the study
of Nguyen et al. for Vietnamese word segmentation [8].
C. Building Corpus
In general, building corpus is carried out through four
stages: (1) choose target of corpus and source of raw data;
(2) building a guideline based on linguistics knowledge for
annotation; (3) annotating or tagging corpus based on rule
set in the guideline; and (4) reviewing corpus to check the
consistency issue.
Encoding word segmentation corpus using B-I-O tagset can
be applied, where B, I, and O denoted begin of word, inside
of word, and others, respectively. For example, the sentence
“Megabit trên giây là đơn vịđo tốc đọtruyền dẫn dữliệu
." (”Megabit per second is a unit to measure the network
trafﬁc.” in English) with the word boundary result “Megabit
trên giây là đơn_vịđo tốc_độtruyền_dẫn dữ_liệu .” is encoded
as “Megabit/B trên/B giây/B là/B đơn/B vị/I đo/B tốc/B độ/I
truyền/B dẫn/I dữ/B liệu/I ./O" .
Annotation guidelines can be applied to ensure that anno-
tated corpus has less errors because the manual annotation is
applied. Even though there are guidelines for annotating, the
available output corpora are still inconsistent. For example,
for the Vietnamese Treebank corpus of the VLSP1 project,
Nguyen et al. listed out several Vietnamese word segmentation
inconsistencies in the corpus based on POS information and
n-gram sequences [15] .
Currently, there are at least three available word segmenta-
tion corpus used in Vietnamese word segmentation studies and
systems. Firstly, Dinh et al. built the CADASA corpus from
CADASA’s books [16]. Secondly, Nguyen et al. built vnQTAG
corpus from general news articles [8]. More recently, Ngo
1http://vlsp.vietlp.org:8080/demo/
Table I
VIETNAMESE WORD CORPUS
Corpus
Domain
No. of Articles No. of Sentences No. of Words
CADASA
General book
5
24,240
229,357
vnQTAG
Short novels
7
74755
EVBNews
General news
1,000
45,531
832,441
(EVBCorpus)


## Page 3


et al. introduced the EVBCorpus corpus, which is collected
from four sources, news articles, books, law documents, and
novels. As a part of EVBCorpus, EVBNews, was annotated
common tags in NLP, such as word segmentation, chunker,
and named entity [17]. All of these corpora are collected from
news articles or book stories, and they are manually annotated
the word boundary tags (as shown in Table I).
III. TEXT MODELLING AND FEATURES
To understand natural language and analyze documents
and text, computers need to represent natural languages as
linguistics models. These models can be generated by using
machine learning methods (as show in Figure 2).
Figure 2. Word segmentation data process
There are two common modeling methods for basic NLP
tasks, including n-gram model and bag-of-words model. The
n-gram model is widely used in natural language processing
while the bag-of-words model is a simpliﬁed representation
used in natural language processing and information retrieval
[18], [19]. According to the bag-of-words model, the represen-
tative vector of sentences in the document does not preserve
the order of the words in the original sentences. It represents
the word using term frequency collected from the document
rather than the order of words or the structure of sentences
in the document. The bag-of-words model is commonly used
in methods of document classiﬁcation, where the frequency
of occurrence of each word is used as an attribute feature
for training a classiﬁer. In contrast, an n-gram is a contiguous
sequence of n items from a given sequence of text. An n-gram
model is a type of probabilistic language model for predicting
the next item in a given sequence in form of a Markov model.
To address word segmentation issue, the n-gram model is
usually used for approaches because it considers the order of
tokens in the original sentences. The sequence is also kept the
original order as input and output sentences.
IV. BUILDING MODEL METHODS
There are several studies for Vietnamese Word Segmenta-
tion during last decade. For instance, Dinh et al. started the
word segmentation task for Vietnamese with Neural Network
and Weighted Finite State Transducer (WFST) [10]. Nguyen et
al. continued with machine learning approaches, Conditional
Random Fields and Support Vector Machine [8]. Most of
statistical approaches are based on the architecture as shown
in Figure 2. According to the architecture, recent studies and
systems focus on either improving or modifying difference
learning models to get the highest accuracy. Features used in
word segmentation systems are syllable, dictionary, and entity
name. The detail of all widely used techniques applied are
collected and described in following subsections.
A. Maximum Matching
Maximum matching (MM) is one of the most popular
fundamental and structural segmentation algorithms for word
segmentation [20]. This method is also considered as the
Longest Matching (LM) in several research [10], [4]. It is
used for identifying word boundary in languages like Chinese,
Vietnamese and Thai. This method is a greedy algorithm,
which simply chooses longest words based on the dictionary.
Segmentation may start from either end of the line without any
difference in segmentation results. If the dictionary is sufﬁcient
[20], the expected segmentation accuracy is over 90%, so it is a
major advantage of maximum matching . However, it does not
solve the problem of ambiguous words and unknown words
that do not exist in the dictionary.
There are two types of the maximum matching approach:
forward MM (FMM) and backward MM (BMM). FMM
starts from the beginning token of the sentence while BMM
starts from the end. If the sentence has word boundary ambigu-
ities, the output of FMM and BMM will be different. When
applying FMM and BMM, there are two types of common
errors due to two ambiguities: overlapping ambiguities and
combination ambiguity. Overlapping ambiguities occur when
the text AB has both word A, B and AB, which are in the
dictionary while the text ABC has word AB and BC, which are
in the dictionary. For example, "cụgià đi nhanh quá" (there two
meanings: ”the old man goes very fast” or ”the old man died
suddenly”) is a case of the overlapping ambiguity while "tốc
độtruyền thông tin" is a case of the combination ambiguity.
As shown in Figure 2, the method simpliﬁcation ambigui-
ties, maximum matching is the ﬁrst step to get features for the
modelling stage in machine learning systems, like Conditional
Random Fields or Support Vector Machines.
B. Hidden Markov Model (HMM)
In Markov chain model is represented as a chain of tokens
which are observations, and word taggers are represented as
predicted labels. Many researchers applied Hidden Markov
model to solve Vietnamese word segmentation such as in [9],
[21] and so on.
N-gram language modeling applied to estimate probabilities
for each word segmentation solution [22]. The result of this
method depends on copora and is based maximal matching
strategy. So, they do not solve missing word issue. Let P(s)


## Page 4


is a product of probabilities of words created from sentence s
(1) with length m :
s = w1...w2
(1)
Each conditional probability of word is based on the last n-1
words (n-gram) in the sentence s. It is estimated by Markov
chain model for word w from position i-n+1 to i-1 with
probability (2)
P(wi | wi−1
i−n+1)
(2)
We have equation (3)
P(s) =
m
Y
i=1
P(wi | wi−1
i
) ≈
m
Y
i=1
P(wi | wi−1
i−n+1)
(3)
C. Maximum Entropy (ME)
Maximum Entropy theory is applied to solve Vietnamese
word segmentation [16], [23], [24]. Some researchers do not
want the limit in Markov chain model. So, they use the context
around of the word needed to be segmented. Let h is a context,
w is a list of words and t is a list of taggers, Le [16], [23]
used
P(t1...tn | w1...wn) ≈
n
Y
i=1
P(ti | hi)
(4)
P(s) is also a product of probabilities of words created from
sentence s (1). Each conditional probability of word is based
on context h of the last n word in the sentence s.
D. Conditional Random Fields
To tokenize a Vietnamese word, in HMM or ME, authors
only rely on features around a word segment position. Some
other features are also affected by adding more special at-
tributes, such as, in case ’?’ question mark at end of sentence,
Part of Speech (POS), and so on. Conditional Random Fields
is one of methods that uses additional features to improve the
selection strategy [8].
There are several CRF libraries, such as CRF++2, CRF-
suite3. These machine learning toolkits can be used to solve the
task by providing an annotated corpus with extracted features.
The toolkit will be used to train a model based on the corpus
and extract a tagging model. The tagging model will then be
used to tag on input text without annotated corpus. In the
training and tagging stages, extracting features from the corpus
and the input text is necessary for both stages.
E. Support Vector Machines
Support Vector Machines (SVM) is a supervised machine
learning method which considers dataset as a set of vectors
and tries to classify them into speciﬁc classes. Basically, SVM
is a binary classiﬁer. however, most classiﬁcation tasks are
multi-class classiﬁers. When applying SVMs, the method has
been extended to classify three or more classes. Particular NLP
tasks, like word segmentation and Part-of-speech task, each
token/word in documents will be used as a feature vector. For
2https://taku910.github.io/crfpp/
3http://www.chokkan.org/software/crfsuite/
the word segmentation task, each token and its features are
considered as a vector for the whole document, and the SVM
model will classify this vector into one of the three tags (B-
IO).
This technique is applied for Vietnamese word segmentation
in several studies [8], [25]. Nguyen et al. applied on a seg-
mented corpus of 8,000 sentences and got the result at 94.05%
while Ngo et al. used it with 45,531 segmented sentences and
get the result at 97.2%. It is worth to mention that general
SVM libraries (such as LIBSVM4, LIBLINEAR5, SVMlight6,
Node-SVM7, and TreeSVM8 ), YamCha9 is an opened source
SVM library that serves several NLP tasks: POS tagging,
Named Entity Recognition, base NP chunking, Text Chunking,
Text Classiﬁcation and event Word Segmentation.
V. TOOLKITS
vnTokenizer and JVnSegmenter are two famous segmen-
tation toolkits for Vietnamese word segmentation. Both two
word segmentation toolkits are implemented the word seg-
mentation data process in Figure 2. This section gives more
details of these Vietnamese word toolkits.
A. Programming Languages
In general, Java and C++ are the most common language
in developing toolkits and systems for natural language pro-
cessing tasks. For example, GATE10, OpenNLP11, Stanford
CoreNLP12 and LingPipe13 platforms are developed by JAVA
while foundation tasks and machine learning toolkits are devel-
oped by C++. CRF++14, SVMLight15 and YAMCHA16 . Re-
cently, Python becomes popular among the NLP community.
In fact, many toolkits and platforms have been developed by
this language, such as NLTK17, PyNLPl18 library for Natural
Language Processing.
B. JVnSegmenter
JVnSegmenter19 is a Java-based Vietnamese Word Segmen-
tation Tool developed by Nguyen and Phan. The segmentation
model in this tool was trained on about 8,000 tagged Viet-
namese text sentences based on CRF model and the model
extracted over 151,000 words from the training corpus. In
addition, this is used in building the EnglishVietnamese Trans-
lation System [26], [27], [28]. Vietnamese text classiﬁcation
[29] and building Vietnamese corpus [30], [31].
4https://www.csie.ntu.edu.tw/ cjlin/libsvm/
5https://www.csie.ntu.edu.tw/ cjlin/liblinear/
6http://svmlight.joachims.org/
7https://github.com/nicolaspanel/node-svm
8https://github.com/sitfoxﬂy/tree-svm
9http://chasen.org/ taku/software/yamcha/
10https://gate.ac.uk/
11https://opennlp.apache.org/
12http://stanfordnlp.github.io/CoreNLP/
13http://alias-i.com/lingpipe/
14https://taku910.github.io/crfpp/
15http://svmlight.joachims.org/
16http://chasen.org/ taku/software/yamcha/
17http://www.nltk.org/
18https://github.com/proycon/pynlpl
19http://jvnsegmenter.sourceforge.net/


## Page 5


C. vnTokenizer
vnTokenizer20 is implemented in Java and bundled as
Eclipse plug-in, and it has already been integrated into vn-
Toolkit, an Eclipse Rich Client application, which is intended
to be a general framework integrating tools for processing of
Vietnamese text. vnTokenizer plug-in, vnToolkit and related
resources, including the lexicon and test corpus are freely
available for download. According to our observation, many
research cited vnTokenizer21 to use word segmentation results
for applications as building a large Vietnamese corpus [32],
building an English-Vietnamese Bilingual Corpus for Machine
Translation [33], Vietnamese text classiﬁcation [34], [35], etc.
VI. EVALUATION AND RESULTS
This research gathers the results of Vietnamese word seg-
mentation of several methods into one table as show in Table
II. It is noted that they are not evaluated on a same corpus. The
purpose of the result illustration is to provide an overview of
the results of current Vietnamese word segmentation systems
based on their individual features. All studies mentioned in the
table have accuracy around 94-97% based on their provided
corpus.
This study also evaluates the Vietnamese word segmentation
based on existing toolkits using the same annotated Viet-
namese word segmentation corpus. There are two available
toolkits to evaluate and to segment. To be neutral to both
toolkits, we use the EVBNews Vietnamese corpus, a part of
EVBCorpus, to evaluate Vietnamese word segmentation. The
EVBNews corpus contains over 45,000 segmented Vietnamese
sentences extracted from 1,000 general news articles (as shown
in Table III) [17]. We used the same training set which has
1000 ﬁles and 45,531 sentences. vnTokenizer outputs 831,455
Vietnamese words and 1,206,475 tokens. JVnSegmenter out-
puts 840,387 words and 1,201,683. We correct tags (BIO), and
compare to previous outputs, we have rate from vnTokenizer
is 95.6% and from JVnsegmenter is 93.4%. The result of
both vnTokenizer and JVnSegmenter testing on the EVBNews
Vietnamese Corpus are provided in Table IV.
VII. CONCLUSIONS AND FUTURE WORKS
This study reviewed state-of-the-art approaches and systems
of Vietnamese word segmentation. The review pointed out
common features and methods used in Vietnamese word
segmentation studies. This study also had an evaluation of
the existing Vietnamese word segmentation toolkits based on
a same corpus to show advantages and disadvantages as to
shed some lights on system enhancement.
There are several challenges on supervised learning ap-
proaches in future work. The ﬁrst challenge is to acquire
very large Vietnamese corpus and to use them in building a
classiﬁer, which could further improve accuracy. In addition,
applying linguistics knowledge on word context to extract
useful features also enhances prediction performance. The
20http://mim.hus.vnu.edu.vn/phuonglh/softwares/vnTokenizer
21https://scholar.google.com/
second challenge is design and development of big data
warehouse and analytic framework for Vietnamese documents,
which corresponds to the rapid and continuous growth of
gigantic volume of articles and/or documents from Web 2.0
applications, such as, Facebook, Twitter, and so on. It should
be addressed that there are many kinds of Vietnamese doc-
uments, for example, Han - Nom documents and old and
modern Vietnamese documents that are essential and still
needs further analysis. According to our study, there is no a
powerful Vietnamese language processing used for processing
Vietnamese big data as well as understanding such language.
The ﬁnal challenge relates to building a system, which is able
to incrementally learn new corpora and interactively process
feedback. In particular, it is feasible to build an advance NLP
system for Vietnamese based on Hadoop platform to improve
system performance and to address existing limitations.
REFERENCES
[1] Manning, Christopher D., and Hinrich Schutze. ¨ Foundations of sta-
tistical natural language processing, Vol. 999. Cambridge: MIT press,
1999.
[2] Jurafsky, Dan. Speech & language processing, Pearson Education India,
2000.
[3] Quoc Tri Tran, Thi Xuan Thao Pham, Quoc Hung Ngo, Dien Dinh
and Nigel Collier, Named entity recognition in Vietnamese documents,
Progress in Informatics, No.4, March 2007, pp. 5-13.
[4] Surapant Meknaviny, Paisarn Charoenpornsawatz and Boonserm Ki-
jsirikulz , Feature-based Thai word segmentation, In Proceeding of
natural language processing Paciﬁcrim Symposium (NLPRS), pp 41-
46, 1997.
[5] Huang, Changning and Zhao, Hai, Chinese word segmentation: A decade
review, In Journal of Chinese Information Processing, vol. 21, no. 3, pp.
8-20, 2007
[6] Ding, Chenchen and Thu, Ye Kyaw and Utiyama, Masao and Sumita,
Eiichiro, Word Segmentation for Burmese (Myanmar), In ACM Trans-
actions on Asian and Low-Resource Language Information Processing,
vol. 15, no. 4, pp. 22, 2016.
[7] Zhu, Ke, Analysis of Chinese Word Segmentation Technology, In
Applied Mechanics and Materials, vol. 687, pp. 1540–1543, 2014.
[8] Cam-Tu Nguyen, Trung-Kien Nguyen, Xuan-Hieu Phan, Le-Minh
Nguyen, and Quang-Thuy Ha. Vietnamese word segmentation with
CRFs and SVMs: An investigation, In Proceedings of the 20th Paciﬁc
Asia Conference on Language, Information and Computation (PACLIC)
2006.
[9] Thi Minh Huyen Nguyen, Azim Roussanaly, and Tuong Vinh Ho, A
hybrid approach to word segmentation of Vietnamese texts, Language
and Automata Theory and Applications. Springer Berlin Heidelberg, pp
240-249. 2008.
[10] Dien Dinh, Kiem Hoang and Van Toan Nguyen, Vietnamese Word
Segmentation, In Proceedings of 6th Natural Language Processing
Paciﬁc Rim Symposium (NLPRS); pp 749–756, 2001.
[11] Thien Giap Nguyen, Three Methods of Identifying Words and Mor-
phemes in Vietnam, Journal of Science, Vietnam National University,
Hanoi, vol. 29, no. 4, pp 1–7, 2013
[12] Leonard Bloomﬁeld, 1926, A set of postulates for the science of
language, Language, JSTOR; vol. 2, no. 3, pp 153-164.
[13] Tai Can Nguyen, Vietnamese Grammar, Publishing House of Vietnam
National University - Ha Noi, Vietnam; 1996.
[14] Phe Hoang, Vietnamese Dictionary, Encyclopedia Publishing House,
Vietnam; 2010.
[15] Thi Quy Nguyen and Ngan LT Nguyen and Miyao Yusuke, Comparing
Different Criteria for Vietnamese Word Segmentation, In Proceedings
of the 3rd Workshop on South and Southeast Asian Natural Language
Processing (SANLP); pp 53–68, 2012.
[16] Dien Dinh and Thuy Vu, A maximum entropy approach for Vietnamese
word segmentation, In Proceedings of the International Conference on
Research, Innovation and Vision for the Future (RIVF), IEEE, pp 248–
253, 2006.


## Page 6


Table II
EVBNEWS VIETNAMESE CORPUS
Method
Features
Corpus
Result
Result
NN with WFST
Dictionary, proper name
305 newspaper articles,
98.36%
Dinh et al. [10]
Morphological analyzer
7,800 sentences
ME
Syllable, dictionary, proper name,
CADASA
94.44%
Dien Dinh and Thuy Vu [16]
misc, Vietnamese Syllable
24,240 sentences
ME
Syllable, dictionary, proper name,
4,800 sentences,
93.70%
Le et al. [23]
misc, Vietnamese Syllable
113, 000 syllables 22
SVMs
Syllable, BMM, FMM, proper
1000 newspaper articles,
97.2%
Ngo et al. [36]
name, misc, foreign
45,531 sentences
768,031 Vietnamese words
SVMs
Syllable, dictionary, proper name,
305 newspaper articles,
94.05%
Nguyen et al. [8]
misc, Vietnamese Syllable
150 novel sentences
8,000 sentences 23
CRFs
Syllable, dictionary, proper name,
305 newspaper articles,
95%
Nguyen et al. [8]
misc, Vietnamese Syllable
150 novel articles
8,000 sentences
Table III
EVBNEWS VIETNAMESE CORPUS
Statistics
Number of Files
1,000
Number of Sentences
45,531
Number of Words
832,441
Number of Tokens
832,441
Table IV
VIETNAMESE WORD SEGMENTATION RESULT OF
VNTOKENIZER AND JVNSEGMENTER
vnTokenizer
JVnSegmenter
Number of Files
1,000
1,000
Number of Sentences
45,531
45,531
Number of Words
831,455
840,387
Number of Tokens
1,206,475
1,201,683
Correct Tags
1,153,198
1,122,752
Rate
95.6%
93.4%
to sentence boundary detection of Vietnamese texts, In Proceedings of
[17] Quoc Hung Ngo, Werner Winiwarter, and Bartholomaus Wloka, EVB-
Corpus - A Multi-Layer English-Vietnamese Bilingual Corpus for
Studying Tasks in Comparative Linguistics, In Proceedings of the
11th Workshop on Asian Language Resources (11th ALR within the
IJCNLP2013), Asian Federation of Natural Language Processing, pp
1–9. 2013.
[18] Wallach, Hanna M. Topic modeling: beyond bag-of-words, Proceedings
of the 23rd international conference on Machine learning. ACM, 2006.
[19] Dang Duc Pham and Giang Binh Tran and Son Bao Pham, A hybrid
approach to vietnamese word segmentation using part of speech tags, In
Proceedings of the International Conference on Knowledge and Systems
Engineering. KSE’09, 2009.
[20] Ynan Liu, Qiang Tan, and Kun Xu Shen. The Word Segmentation Rules
and Automatic Word Segmentation, Methods for Chinese Information
Processing (in Chinese), pp 36, 1994.
[21] Thuc Viet Ha, Van Quang Anh Nguyen, Hoang Tru Cao, Jonathan
Lawry, A fuzzy synset-based hidden Markov model for automatic text
segmentation, In Soft Methods for integrated Uncertainty Modelling ,
Springer Berlin Heidelberg. pp 365-372, 2006
[22] Gabriel, K. R., and J. Neumann. A Markov chain model for daily rainfall
occurrence at Tel Aviv. Quarterly Journal of the Royal Meteorological
Society 88.375 (1962): 90-95.
[23] Hong Phuong Le and Vinh Tuong Ho, A maximum entropy approach
the International Conference on Research, Innovation and Vision for the
Future (RIVF), IEEE; 2008.
[24] Oanh Thi Tran, Cuong Anh Le, and Thuy Quang Ha. Improving
vietnamese word segmentation and pos tagging using mem with various
kinds of resource, Journal of Natural Language Processing 17.3: 41-60,
2010.
[25] Quang Thang Dinh, Hong Phuong Le, Thi Minh Huyen Nguyen
and Cam Tu Nguyen, Rossignol Mathias and Xuan Luong Vu, Word
segmentation of Vietnamese texts: a comparison of approaches, In
Proceedings of the 6th international conference on Language Resources
and Evaluation (LREC), 2008.
[26] Tu Bao Ho , Pham Ngoc Khanh, Ha Thanh Le, and Nguyen Thi Phuong
Thao Issues and First Development Phase of the English-Vietnamese
Translation System EVSMT1. 0
[27] Chi Mai Luong and Satoshi Nakamura. Toward Asian Speech Trans-
lation: The Development of Speech and Text Corpora for Vietnamese
language
[28] Axelrod, Amittai, Ahmed Elgohary, Marianna Martindale, Khanh
Nguyen, Xing Niu, Yogarshi Vyas, and Marine Carpuat. The UMD
Machine Translation Systems at IWSLT 2015
[29] Cam Tu Nguyen, Hidden topic discovery toward classiﬁcation and
clustering in Vietnamese web documents Diss. Master Thesis, 2008.
[30] Doan Nguyen. Using search engine to construct a scalable corpus for
Vietnamese lexical development for word segmentation, Proceedings
of the 7th Workshop on Asian Language Resources. Association for
Computational Linguistics, 2009.
[31] Liling Tan and Francis Bond. Building and Annotating the Linguistically
Diverse NTU-MC (NTU-Multilingual Corpus), Int. J. of Asian Lang.
Proc. 22.4, 161-174, 2012
[32] Phuong-Thai Nguyen et al. Building a large syntactically-annotated
corpus of Vietnamese, Proceedings of the Third Linguistic Annotation
Workshop. Association for Computational Linguistics, 2009.
[33] Quoc Hung Ngo and Werner Winiwarter. Building an EnglishVietnamese
Bilingual Corpus for Machine Translation, Asian Language Processing
(IALP), 2012 International Conference on. IEEE, 2012.
[34] Minh Trung Nguyen, Duc Tam Nguyen and Hong Phuong Nguyen.
Using main content extraction to improve performance of Vietnamese
web page classiﬁcation, Proceedings of the Second Symposium on
Information and Communication Technology. ACM, 2011.
[35] Giang-Son Nguyen, Xiaoying Gao and Peter Andreae. Phoneme based
representation for vietnamese web page classiﬁcation, Proceedings of the
2011 IEEE/WIC/ACM International Conferences on Web Intelligence
and Intelligent Agent Technology-Volume 01. IEEE Computer Society,
2011.
[36] Quoc Hung Ngo, Dien Dinh, Winiwarter Winiwarter, A hybrid method
for word segmentation with English-Vietnamese bilingual text. In Pro-
ceedings of the 2013 International Conference on Control, Automation
and Information Sciences (ICCAIS), IEEE. pp 48–52, 2013.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
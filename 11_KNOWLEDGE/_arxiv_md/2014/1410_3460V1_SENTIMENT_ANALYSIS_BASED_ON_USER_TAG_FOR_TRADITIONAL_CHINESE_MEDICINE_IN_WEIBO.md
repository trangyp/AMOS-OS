---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1410.3460v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1410.3460v1_Sentiment_Analysis_based_on_User_Tag_for_Traditional_Chinese_Medicine_in_Weibo

> Source: 1410.3460v1_Sentiment_Analysis_based_on_User_Tag_for_Traditional_Chinese_Medicine_in_Weibo.pdf

> Pages: 7

---


## Page 1


Sentiment Analysis based on User Tag for
Traditional Chinese Medicine in Weibo
Junhui Shen
Information Center
Beijing Univercity of Chinese Medicine
Beijing, China
Email: shen-junhui@163.com
Peiyan Zhu, Rui Fan
State Key Lab of Software Development Environment
Beihang University
Beijing, China
Abstract—With the acceptance of Western culture and science,
Traditional Chinese Medicine (TCM) has become a controversial
issue in China. So, it’s important to study the public’s sentiment
and opinion on TCM. The rapid development of online social
network, such as twitter, make it convenient and efﬁcient to
sample hundreds of millions of people for the aforementioned
sentiment study. To the best of our knowledge, the present work
is the ﬁrst attempt that applies sentiment analysis to the domain
of TCM on Sina Weibo (a twitter-like microblogging service in
China). In our work, ﬁrstly we collect tweets topic about TCM
from Sina Weibo, and label the tweets as supporting TCM and
opposing TCM automatically based on user tag. Then, a support
vector machine classiﬁer has been built to predict the sentiment
of TCM tweets without labels. Finally, we present a method
to adjust the classiﬁer result. The performance of F-measure
attained with our method is 97%.
I. INTRODUCTION
With the rapid acceptance of Western culture and science
from the beginning of the 20th century, Traditional Chinese
Medicine (TCM) was seriously thrown into doubts in terms
of its scientiﬁc foundation. When such kind of debate was
reviewed in respective of debaters sentiment towards TCM,
it can be seen that two types of sentiment are dominating:
one school thinks that TCM are not proved by scientiﬁc
experiment, so it is pseudo-science and should be abolished,
while the other school believes TCM is effective in treating
many diseases and therefore TCM is essentially a kind of
science.
Microblogging today has become a very popular com-
munication
tool
among
internet
users.
In
China,
Sina
Weibo(http://www.weibo.com), a Twitter-like microblogging
service launched in 2009, has accumulated more than 500
million users in less than four years, leading to it’s most
important role in the social media marketing platform. Every
second, approximately more than 1000 Chinese tweets are
posted in Weibo. It is imaginable that the debate surrounding
TCM spread into cyber-space in unbelievable speed.
So far, although many researches have been conducted on
sentiment classiﬁcation, there is very little such work done on
Traditional Chinese Medicine. To the best of our knowledge,
the present work is the ﬁrst attempt that applies sentiment
analysis to the domain of TCM on Sina Weibo. In our work,
main contents are: collecting corpus and dictionary resources,
labeling data automatically based on user tag, building an
SVM classiﬁer to predict the sentiment of TCM tweets and
presenting a method to adjust the classiﬁer result. The perfor-
mance of F-measure attained with our method is 0.97%.
The rest of the paper is organized as follows: In section
II presents previous works on sentiment analysis and their
application for microblogging. In Section III data collecting
and labeling are discussed. Feature selection and learning
method are described in Section IV. In Section V experimental
results are presented. Finally, conclusion and future directions
of research are discussed in section VI.
II. RELATED WORK
Sentiment classiﬁcation has been investigated in different
domains such as movie reviews, product reviews and customer
feedback reviews. The main researches have fallen into two
categories. The ﬁrst is machine learning techniques, which
attempts to train a sentiment classiﬁer based on occurrence
frequencies of the various words in the documents. The other
approach is semantic oriented, which classiﬁes words into
two classes, such as ”positive” or ”negative”, and then counts
an overall positive/negative score for the text. A very broad
overview of the existing work was presented in [1, 2]. In
their survey, the authors describe existing techniques and
approaches for sentiment analysis.
With the popularization of microblog and online social
networks, such as Twitter and Weibo, sentiment analysis
become a ﬁeld of interest to many researches. Some of the
early and recent results on sentiment of Twitter data have been
presented in [3–5]. Go et al.[3] used distant learning to acquire
sentiment data. They used tweets ending in positive emoticons
like ”:)”, ”:-)” as positive and negative emoticons like ”:(”, ”:-
(” as negative. They built models using Nave Bayes, MaxEnt
and Support Vector Machines (SVM), and they reported that
SVM outperforms other classiﬁers. In terms of feature space,
they tried unigram, bigram model in conjunction with parts-
of-speech (POS) features. They noted that the unigram model
outperforms all other models. Speciﬁcally, bigrams and POS
features do not help. So, in this paper, we use the SVM
classiﬁer with a unigram model. In China, some of the
research on sentiment of Weibo data are conducted by Zhao
et al. [6] and He[7] etc. Zhao et al. [6] built a system for
arXiv:1410.3460v1  [cs.CL]  13 Oct 2014


## Page 2


sentiment analysis of Chinese tweets in Weibo. It employed
the emoticons for the generation of sentiment labels for tweets,
and built an incremental learning Nave Bayes classiﬁer for the
categorization of four types of sentiments: angry, disgusting,
joyful and sad.
About the subject of TCM in Weibo, however, there is very
little investigation conducted on sentiment classiﬁcation.
III. DATA COLLECTING AND LABELING
In this section, we discuss the collecting and preprocessing
of tweet topic on TCM. For each tweet in our corpus, we
convert it into a sequence of words.
A. Corpus Collection based on User Tag
In China, Sina Weibo is one of China’s most important
social networking channels, and is the Chinese counterpart
to Twitter. As with Twitter, Weibo users are allowed to post
real-time messages, called tweets. Tweets are short messages,
restricted to 140 characters in length.
There are some prominent differences between Twitter and
Weibo. For example, user can freely tag himself/herself to
indicate his/her interests and characteristics in Weibo. Of
course, Tagging is not mandatory in Weibo where users can
tag up to 10 keywords.
In January 2014, we searched Weibo users interested in
TCM by user tag. If someone has more than one user tag
included in our search keywords list, he/she would be dupli-
cated in our dataset. After ﬁltering the duplicated users, we
constructed a dataset including 48861 Weibo users, denoted
as C. The user tags and the corresponding numbers of Weibo
users are listed in Table 1. Among all tags, ”Traditional
Chinese Medicine” is used by 42608 users and occupies the
dominating share of 87%, ”Medicine Material”, ”Acupuncture
and Moxibustion” and ”Massage” follow but none of them
takes the share more than 8%. It is not surprising ”Traditional
Chinese Medicine” is the main tag used because it is a
wide concept, which often refers to not only TCM therapy
but also including ”Medicine Material”, ”Acupuncture and
Moxibustion” and ”Massage”.
TABLE I
USER TAG AND THE NUMBER OF WEIBO USER CORRESPONDINGLY
User Tag
User Tag
the Counts
(Original Text)
(English Translation)
of Weibo Users
Traditional Chinese Medicine
42608
Medicine Material
3827
Acupuncture and Moxibustion
3236
Massage
2198
Moxa-moxibustion
763
Chinese Herb Medicine
417
Acupuncture
73
Acupuncture and Massage
67
Chinese Patent Drug
50
Using the Application Programming Interfaces(APIs) pro-
vided by Weibo, we collected the tweets which were posted by
the users in C. Due to the limit of API, only the most recent
2000 tweets of each user posted can be obtained, we gathered
21,242,370 tweets totally.
The sentiment of a retweet is not always consistent with
the tweet, especially when debating. For this reason, we split
every tweet which has retweet and insert every retweet into our
corpus. Sometimes, one post has more than one re-posting, so
we have much more tweets after splitting. Totally, we collected
43,012,068 tweets in our corpus, more than twice of original
tweets count.
B. Two Dictionary Resources
In this paper, we introduce two new resources for the
preprocessing of Weibo data topic on TCM: custom dictionary
and TCM terminology dictionary. We collect western medicine
terminology, TCM terminology and popular vocabulary on the
internet, totally 5307 words in the custom dictionary. It can be
used as a helpful complement of build-in dictionary of general
tool for Chinese Word Segmentation. The TCM terminology
dictionary collect 2715 TCM terminology words including
Traditional Chinese Medicine, Chinese Patent Medicine, Chi-
nese Herb Medicine and acupuncture point etc. It can be used
to ﬁlter the Weibo which topic is about TCM.
C. Preprocessing of Data
We pre-process all the tweets as follows: 1) Translating
the tweet to Chinese Simpliﬁed if it is written by Chinese
Traditional; 2) Filtering URL links (e.g. http://example.com ),
Weibo user names (e.g. @shen with symbol @ indicating a
user name), Weibo special words ( e.g. reply ), and emoticons
from tweets; 3)Segmenting Chinese Word (with the ICTCLAS
tool [8] and the custom dictionary as introduced in subsection
B ) to generate a sequence of words; 4) Removing stop
words ( such as ”oh” ) from the bag of words; 5) Filtering
advertisements by key words (such as ”sale”).
D. Filtering Chinese Medicine Tweets
However, the topics of tweets posted by the users interested
in TCM are diverse and not only concerning to TCM. There-
fore, in our study, we should screen out the tweets in which
the real topic is not about TCM.
In our approach, we ﬁlter the tweets topic on TCM with
the TCM terminology dictionary (introduced in subsection B).
Usually, a tweet topic on TCM contains more than one key
word, so we ﬁlter the tweets including at least two different
key words of TCM strictly. After ﬁltering, there remain in our
corpus 1,650,497 tweets in which the real topic is about TCM.
E. Labeling the Data
When we label the sentiment of tweet, our approach is based
on the basic principle: the user is prone to have consistent
opinions for a certain topic due to the principle of consistency
[9]. It means that if the user’s opinion is for TCM, the
sentiment of all the tweets he/she posted is for TCM. In
contrast, if the user’s opinion is against TCM, the sentiment
of all the tweets he/she posted is against TCM.


## Page 3


TABLE II
USER TAG OF DIFFERENT SENTIMENT AND CORRESPONDING WEIBO USER
COUNTS
Sentiment
User Tag
User Tag
User
(Original Text)
(English Translation)
Counts
Supporting TCM
Love TCM
972
Love TCM
239
Doctor of TCM
230
Love TCM
85
TCM Follower
55
TCM Follower
52
Pharmacist of TCM
51
Acupuncturist
42
Regimen of TCM
29
Masseur
28
TCM Master
12
Opposing TCM
Oppose TCM
191
Abominate TCM
55
Oppose TCM
28
In our approach, we acquire user’s opinion about TCM by
the user tag. The keyword which is used as user tag is deﬁned
by the user. Consequently, the user tags could be different
even if the sentiment to TCM is same. The user tags which
are used to label the sentiment are listed in Table 2. Only
the user tags which have been quoted by more than 10 users
are included in the table. As a result, 1866 Weibo users are
labeled as supporting TCM, while 290 Weibo users are labeled
as opposing TCM. The rest are not labeled because we can’t
obtain obvious sentiment orientation from his/her user tags.
Based on our basic principle, we label the sentiment of tweet
according to the user’s opinion on TCM. Finally, 40888 tweets
are labeled as supporting TCM, and 6975 tweets are labeled
as opposing TCM. Obviously, there is an imbalance but it is
consistent with the real world. The tweets labeled will be used
as the training dataset in the next step of our research.
IV. METHODOLOGY
This section presents the methodology of sentiment classi-
ﬁcation system we use. First, feature selection method is used
to pick out discriminating terms for training and classiﬁcation.
Then we use the machine learning method to build a sentiment
classiﬁer. Finally, we adjust the classiﬁcation result based on
the basic principle that a user keeps consistent opinions for a
certain topic.
A. Feature Selection
A number of feature selection metrics have been explored
in text categorization, i.e. chi-square (CHI), information gain
(IG), correlation coefﬁcient (CC) and odds ratios (OR). All
these methods compute a score for each individual feature and
then pick out a predeﬁned size of feature set. In our approach,
we use the chi-square feature selection method, one of the
most effective methods in text categorization [10].
Chi-square measures the lack of independence between a
term t and a category ci and can be compared to the chi-square
distribution with one degree of freedom to judge extremeness.
It is deﬁned as:
χ2(t, ci) = N[P(t, ci)P(¯t, ci) −P(t, ci)P(¯t, ci)]2
P(t)P(¯t)P(ci)P(ci)
where N is the total number of documents.
B. Machine Learning Method
So far, most of the research on sentiment classiﬁcation
focused on training machine learning algorithms to classify
reviews. Support vector machine (SVM) have been shown to
be highly effective for traditional text categorization [11].
Based on the structural risk minimization principle from the
computational learning theory, SVM seeks a decision surface
to separate the training data points into two classes and makes
decisions based on the support vectors that are selected as the
only effective elements in the training set.
Here we limit our discussion to linear SVM due to its
popularity and high performance in text categorization [12].
The optimization of SVMs (dual form) is to minimize:
⃗α∗= arg min{−
n
X
i=1
αi +
n
X
i=1
n
X
j=1
αiαjyiyj < ⃗xi, ⃗xj >}
Subject to :
n
X
i=1
αiyi = 0;
0 ≤αi ≤C
For a tutorial on SVM and details of their formulation we
refer the reader to Burges [13] and Cristiani [14]. A detailed
treatment of these models application to text classiﬁcation can
be found in Joachims [15].
C. Adjusting Sentiment Classiﬁcation Result
Based on the basic principle that the same user should have
consistent opinions for a certain topic, we adjust the sentiment
classiﬁcation result: assign majority sentiment label to all the
tweets the same user posted.
Based on the sentiment classiﬁcation result, the number of
tweets which are judged as supporting TCM posted by one
user can be obtained as Cs, and the number of tweets posted
by the same user which are judged as opposing TCM can be
obtained as Co. Then we deﬁne γ as
γ = max{Cs, Co}
Cs + Co
where 0.5 ≤γ ≤1. If γ = 1, it means the sentiment of the
user is consistent absolutely. If γ = 0.5, it means Co is equal to
Cs, then we don’t need to adjust the sentiment classiﬁcation
result. When 0.5 < γ < 1, we can adjust the classiﬁcation
result.
V. EXPERIMENTS AND RESULTS
In our dataset, there are 1,650,497 tweets in which the
topic focuses on TCM, including 40,888 tweets labeled as
supporting TCM, and 6,975 tweets labeled as opposing TCM
( introduced in Section 4 ). Since it’s imbalanced, we focused
on not only the global performance, but also the performance


## Page 4


TABLE III
Top 10 Key Words of Each Class
Supporting TCM
Supporting TCM
Opposing TCM
Opposing TCM
(Original Text)
(English Translation)
(Original Text)
(English Translation)
Medicine Material
Chinese Patent Medicine
Health Preservation
Aristolochic acid
State
injection
Science
injection
TCM
Zhouzi Fang
China
Cinnabar
Body
Events
Doctor
Oppose
Health
Aristolochic
Cure
Longdan Xiegan Wan
of each class. Therefore, we choose the F1 to evaluate the
classiﬁcation system.
After applying CHI feature selection to tweets, for all our
experiments we use Support Vector Machine and report 5-fold
cross-validation test results.
Pang [11] argued that feature presence binary value is
more useful than feature frequency for the SVM classier.
Therefore, we use binary value for each feature instead of
feature frequency.
A. The performance measure
To evaluate the imbalanced classiﬁcation system, we use
the F1 measure. This measure combines recall and precision
in the following way:
Precision = number of correct positive predictions
number of positive predictions
Recall = number of correct positive predictions
number of positive examples
F1 = 2 ∗Precision ∗Recall
Recall + Precision
B. Feature Selection Results
The top 10 key-words of each class selected by the CHI
method are listed in table 3. Among the proponents of
TCM, it is not surprise that ”Medicine Material”, ”Health
Preservation”, ”Tradational Chinese Medicine” and ”Body”
are often used. The frequncy of ”State” and ”China” could
be due to that Chinese government employed clear policy to
support TCM. Among the opponents of TCM, ”Aristolochic
acid”, ”Cinnabar”, ”Longdan Xiegan Wan” and ”injection” are
popular words. This could be due to that all these terms are
related to untoward effects so the opponents want to shake the
scientiﬁc foundation of TCM.
Figure 1 shows the classiﬁcation performance curves us-
ing the CHI feature selection method vs. feature number.
The performance of classiﬁer is above 90% stably and the
performance increases as number of features increases. It is
found that the performance of TCM proponent classiﬁer is
slightly higher than the performance of the total classiﬁer. It
is notable that the performance of TCM opponent classiﬁer
increase signiﬁcantly when number of features increases. The
performance of each class is relatively stable when the number
of features exceeds 3000. So, we ﬁxed the number of features
at 3000 in the following experiments.
G
G
G
G
G
G
G
0.5
0.6
0.7
0.8
0.9
1.0
Number of selected features
F1
0
500
1000
2000
3000
4000
G
Whole
Supporting TCM
Opposing TCM
Fig. 1.
The Performance Curves of Each Class vs. Feature Number.
0.90
0.91
0.92
0.93
0.94
0.95
parameter wi
the performance of classifier
0
0.1
0.3
0.5
0.7
0.9
1
G
G
G
G
G
G
G
G
G
G
G
F1
Precission
Recall
Fig. 2.
The Performance Curves vs. Parameter wi


## Page 5


G
G
G
G
G
G
G
G
G
G
0.5
0.6
0.7
0.8
0.9
1.0
parameter wi
Precision
0
0.2
0.4
0.6
0.8
1
G
Supporting TCM
Opposing TCM
(a) PRECISION
G
G
G
G
G
G
G
G
G
G
0.5
0.6
0.7
0.8
0.9
1.0
parameter wi
Recall
0
0.2
0.4
0.6
0.8
1
G
Supporting TCM
Opposing TCM
(b) RECALL
Fig. 3.
The Precision and Recall of Each Class vs. Parameter wi
G
G
G
G
G
G
G
G
G
G
0.90
0.94
0.98
parameter wi
the performance of supporting TCM
0
0.2
0.4
0.6
0.8
1
G
F1
Precision
Recall
(a) SUPPORTING TCM
G
G
G
G
G
G
G
G
G
G
0.5
0.6
0.7
0.8
0.9
1.0
parameter wi
the performance of opposing TCM
0
0.2
0.4
0.6
0.8
1
G
F1
Precision
Recall
(b) OPPOSING TCM
Fig. 4.
the Performance of Supporting TCM and Opposing TCM Separately.
C. Classiﬁcation Results
Because the dataset is unbalanced, we tune the wi parameter
for SVM, where 0 ≤wi ≤1.
Figure 2 shows the performance of F1, precision and recall
by varying the parameter wi from 0.1 to 1.0. when wi increases
from 0 to 1, precision, recall and F1 all increase signiﬁcantly
and reach plateau.
Figure 3 shows precision and recall separately with each
class by varying the parameter wi. It is interesting that
precision shows a reverse trend of that of recall. When wi
increases from 0 to 1, the precision of supporting TCM
gradually decreases while the precision of opposing TCM
rapidly increase. During the same process, recall of supporting
TCM increases while recall of opposing TCM signiﬁcantly
decreases.
Figure 4 shows the performance of each class separately.
From these ﬁgures we can see that it is better to set wi to 0.9.
It summarizes the performance of the classiﬁer of supporting
TCM and the classiﬁer of opposing TCM. When wi gradually
increases, for TCM proponents, Precision decreases from 98%
to 96%, Recall increases from 91% to 98%, and F1 increases
gradually to a plateau phase. For TCM opponents, Precision
increases 62% to 86%, Recall decreases from 89% to 75%,
and F1 increases gradually to a plateau phase.
Either viewing the whole or the individual class, when wi
increases from 0.1 to 1, F1 value increases gradually to a
plateau phase. F1 value reaches the optimal when wi equals
to 0.9.
G
G
G
G
G
G
0.90
0.92
0.94
0.96
0.98
1.00
parameter gamma
F1
0.5
0.6
0.7
0.8
0.9
1
Fig. 5.
The Performance Curves vs. Parameter γ.
D. Adjusted Classiﬁcation Results
As introduced in Section 4.3, we can adjust the classiﬁcation
results based on the principle that the same user should have
consistent opinions for a certain topic. Figure 5 shows the
performance by varying the parameter γ from 0.5 to 1(and
ﬁxing wi=0.9). There is a noticeable decline of F1. when γ
is set to 0.5, our model achieves the best performance of F1,
which is 97%.
E. Prediction
Besides the labeled tweets, there are 1,602,634 unlabeled
tweets which the topic is about TCM. We can predict their
sentiment with our trained classiﬁer. Figure 6 shows the curves
for the number of tweets which, respectively, support TCM(a)
and oppose TCM(b). The number of tweets supporting TCM
far exceeds the number of tweets opposing TCM. For the
simple comparison, the tweets number of both opposing and
supporting TCM are converted to their log forms, as shown in
(c). This result coincides with the real world. In china, most
people support TCM, especially the regimen of TCM. There
are only a small number of people opposing TCM. In addition,
the tweet count before 2010 is very small, which is due to the
limit of Weibo where only the most recent 2000 tweets of each
user can be obtained.
After the sentiment classiﬁcation of tweets concerning
TCM, we can monitor the sentiment ﬂuctuation of TCM in
Weibo. As shown in Figure 6, the number of tweets supporting
TCM decreases signiﬁcantly during January of 2012, 2013
and 2014. Because the three periods coincide Chinese New
Year, the decrease could be due to that people did not log on
Weibo during these holiday seasons. On the contrary, number
of tweets opposing TCM showed no clear trend. The erupt of
the tweets opposing TCM could be caused by incidents related
to TCM, which could be an interesting research topic in the
future.
It is also found from Figure 6 thatthe tweet counts of both
class reached the peak in Nov. 2013. We show the details of
the curve in that month in Figure 7. In November 2013, the
number of tweets supporting TCM is relatively stable while the
number of tweets opposing TCM ﬂuctuates drastically. This
is in line with overall trend of the number of each class.


## Page 6


G G G G G G G G G G G G G G G G G
G
G G
G
G G
G
G
G
G G
G
G
G
G
G G G G G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
0
10000
30000
50000
70000
Month
the number of supporting TCM tweets
Jan.2010
Jan.2011
Jan.2012
Jan.2013
Jan.2014
(a) SUPPORTING TCM
G G G G G G G G G G G
G
G
G G G G
G
G
G
G
G
G
G G
G
G
G
G
G
G
G
G
G
G G
G
G
G
G
G
G
G
G
G
G
G
G G
G
G
G
G
0
500
1000
1500
2000
Month
the number of opposing TCM tweets
Jan.2010
Jan.2011
Jan.2012
Jan.2013
Jan.2014
(b) OPPOSING TCM
G
G
G
G
G
G
G G
G
G
G G
G
G
G
G
G
G
G G G G G
G G G G G
G
G G G G G G G G G
G G G
G
G G G G G G G G G G
G
0
1
2
3
4
5
Month
the log of tweets number
Jan.2010
Jan.2011
Jan.2012
Jan.2013
Jan.2014
G
Support TCM
Oppose TCM
(c) SUPPORTING
TCM
vs.
OPPOSING
TCM
Fig. 6.
the Tweets Number of Supporting TCM vs. Opposing TCM.
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
0
5
10
15
20
25
30
0
1
2
3
4
5
Day of Nov.2013
the log of tweets number
G
Supporting TCM
Opposing TCM
Fig. 7.
the Prediction Result of Nov.2013.
Moreover, Our methodology is able to generate keywords
of TCM in favor tweets and TCM against tweets. The top 50
keywords of each class in Nov. 2013 is shown separately in
Figure 8. ”Traditional Chinese Medicine”, ”Health Preserva-
tion”, ”Food” etc. often appears in tweets supporting TCM,
while ”Chinese Patent Medicine”, ”injection”, ”toxicity” etc.
frequently appears in tweets opposing TCM. This is conformed
with Table 3. It is worth mentioning that words such as ”toxic”
or ”harmful” appears in tweets supporting TCM too. This is
not unexpected because TCM theory admits that a few TCM
medicine is toxic so the dosage of these toxic TCM medicines
should be controlled with caution.
VI. CONCLUSION
Traditional Chinese Medicine is an ancient but thriving and
somewhat controversial discipline, meanwhile, it is important
to study the public’s sentiments and opinions on TCM. To the
best of our knowledge, the present work is the ﬁrst attempt
to study sentiment analysis for TCM based on user tag in
Weibo. We classify the opinions on TCM into two categories:
supporting TCM and opposing TCM. The F1 measure value
of our method is 0.97.
Moreover, we collect 48861 Weibo users who are interested
in TCM and 1,650,497 tweets concerning TCM. And we
construct two dictionary resources for processing Chinese
tweets topic on TCM. Based on the aforementioned corpora
and resources, we build an effective classiﬁer with SVM to
analyze the sentiment opinions on TCM using Weibo tweets
automatically.
In future work, we will explore more linguistic techniques
to study sentiment analysis for TCM, such as parsing, semantic
analysis and topic modeling.
Data sharing statement: The unpublished data from this
study are available by contacting Junhui Shen (email:shen-
junhui@163.com ; telephone: 86-10-64287566). Data can be
sent by email.
REFERENCES
[1] B. Pang and L. Lee, “Opinion mining and sentiment anal-
ysis,” Foundations and trends in information retrieval,
vol. 2, no. 1-2, pp. 1–135, 2008.
[2] B. Liu, “Sentiment analysis and opinion mining,” Synthe-
sis Lectures on Human Language Technologies, vol. 5,
no. 1, pp. 1–167, 2012.
[3] A. Go, R. Bhayani, and L. Huang, “Twitter sentiment
classiﬁcation using distant supervision,” CS224N Project
Report, Stanford, pp. 1–12, 2009.
[4] A. Agarwal, B. Xie, I. Vovsha, O. Rambow, and R. Pas-
sonneau, “Sentiment analysis of twitter data,” in Pro-
ceedings of the Workshop on Languages in Social Media.
Association for Computational Linguistics, 2011, pp. 30–
38.
[5] A. Bermingham and A. F. Smeaton, “Classifying senti-
ment in microblogs: is brevity an advantage?” in Pro-
ceedings of the 19th ACM international conference on
Information and knowledge management.
ACM, 2010,
pp. 1833–1836.
[6] J. Zhao, L. Dong, J. Wu, and K. Xu, “Moodlens: an
emoticon-based sentiment analysis system for chinese
tweets,” in Proceedings of the 18th ACM SIGKDD in-
ternational conference on Knowledge discovery and data
mining.
ACM, 2012, pp. 1528–1531.


## Page 7


养生
食物
中医
中医药
医生
子宫
中国
成分
人群
医药
科学
市场
伤害
产品
大师
中药
有毒
存在
记者
同仁堂
全面
甘肃
普通
化学
广东
国内
报道
指南
退烧
最终
依然
新闻
死亡
思考
诊疗
胶囊
离开
乳头
肝炎
销售
规范
怀疑
监测
基层
乌头
口服
媒体
感冒药
保健品
纯天然
(a) SUPPORTING TCM
中成药
注射
说明书
毒性
药品
品种
注射液
首乌
拒绝
目录
入选
修订事件
通报
总局
清开灵
中药注射剂
草药
监管
朱砂
人中白
转基因
劣迹
骗子
致敏
咸阳
注册
斑斑
云南白药
祸害
修改
灾难
试验
证据
孔卡
获准
管理局
排名
失明
封杀
愚昧
保密
评选
阻挡
乌头碱
制品
号称
增补
少女
专利
(b) OPPOSING
Fig. 8.
The Top 50 Key Words of Each Class in Nov.2013.
[7] H. He, “Sentiment analysis of sina weibo based on se-
mantic sentiment space model,” in Management Science
and Engineering (ICMSE), 2013 International Confer-
ence on.
IEEE, 2013, pp. 206–211.
[8] H.-P. Zhang, H.-K. Yu, D.-Y. Xiong, and Q. Liu, “Hhmm-
based chinese lexical analyzer ictclas,” in Proceedings
of the second SIGHAN workshop on Chinese language
processing-Volume 17.
Association for Computational
Linguistics, 2003, pp. 184–187.
[9] H. Deng, J. Han, H. Li, H. Ji, H. Wang, and Y. Lu,
“Exploring and inferring user–user pseudo-friendship for
sentiment analysis with heterogeneous networks,” Statis-
tical Analysis and Data Mining: The ASA Data Science
Journal, 2014.
[10] Y. Yang and J. O. Pedersen, “A comparative study on
feature selection in text categorization,” in ICML, vol. 97,
1997, pp. 412–420.
[11] B. Pang, L. Lee, and S. Vaithyanathan, “Thumbs up?:
sentiment classiﬁcation using machine learning tech-
niques,” in Proceedings of the ACL-02 conference on Em-
pirical methods in natural language processing-Volume
10.
Association for Computational Linguistics, 2002,
pp. 79–86.
[12] R.-E. Fan, K.-W. Chang, C.-J. Hsieh, X.-R. Wang, and
C.-J. Lin, “Liblinear: A library for large linear classiﬁca-
tion,” The Journal of Machine Learning Research, vol. 9,
pp. 1871–1874, 2008.
[13] C. J. Burges, “A tutorial on support vector machines
for pattern recognition,” Data mining and knowledge
discovery, vol. 2, no. 2, pp. 121–167, 1998.
[14] N. Cristianini and J. Shawe-Taylor, An introduction to
support vector machines and other kernel-based learning
methods.
Cambridge university press, 2000.
[15] T. Joachims, Learning to classify text using support vec-
tor machines: Methods, theory and algorithms.
Kluwer
Academic Publishers, 2002.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
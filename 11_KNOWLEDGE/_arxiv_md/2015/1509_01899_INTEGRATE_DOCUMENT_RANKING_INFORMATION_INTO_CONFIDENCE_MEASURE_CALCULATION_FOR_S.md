---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1509.01899
source: arxiv
tags: [arxiv, knowledge, math, quantum, reference]
---
# 1509.01899_Integrate_Document_Ranking_Information_into_Confidence_Measure_Calculation_for_S

> Source: 1509.01899_Integrate_Document_Ranking_Information_into_Confidence_Measure_Calculation_for_S.pdf

> Pages: 5

---


## Page 1


Integrate Document Ranking Information into Conﬁdence
Measure Calculation for Spoken Term Detection
Quan Liu, Wu Guo, Zhen-Hua Ling
University of Science and Technology of China, Hefei, China
quanliu@mail.ustc.edu.cn, guowu@ustc.edu.cn, zhling@ustc.edu.cn
ABSTRACT
This paper proposes an algorithm to improve the calcula-
tion of conﬁdence measure for spoken term detection (STD).
Given an input query term, the algorithm ﬁrst calculates a
measurement named document ranking weight for each
document in the speech database to reﬂect its relevance
with the query term by summing all the conﬁdence mea-
sures of the hypothesized term occurrences in this docu-
ment. The conﬁdence measure of each term occurrence is
then re-estimated through linear interpolation with the cal-
culated document ranking weight to improve its reliability
by integrating document-level information. Experiments are
conducted on three standard STD tasks for Tamil, Viet-
namese and English respectively. The experimental results
all demonstrate that the proposed algorithm achieves consis-
tent improvements over the state-of-the-art method for con-
ﬁdence measure calculation. Furthermore, this algorithm is
still eﬀective even if a high accuracy speech recognizer is not
available, which makes it applicable for the languages with
limited speech resources.
Categories and Subject Descriptors
H.3.3 [Information Storage and Retrieval]: Information
search and retrieval—search process, selection process; I.2.7
[Artiﬁcial Intelligence]: Natural Language Processing
General Terms
Algorithms, Management, Veriﬁcation
Keywords
Spoken Term Detection, Speech Retrieval, Conﬁdence Mea-
sure, Document Ranking, Speech Recognizer.
1.
INTRODUCTION
Spoken term detection (STD) is a task designed for eﬃ-
cient keyword search (given text query) in a speech databases,
Permission to make digital or hard copies of all or part of this work for
personal or classroom use is granted without fee provided that copies are
not made or distributed for proﬁt or commercial advantage and that copies
bear this notice and the full citation on the ﬁrst page. To copy otherwise, to
republish, to post on servers or to redistribute to lists, requires prior speciﬁc
permission and/or a fee.
Copyright 20XX ACM X-XXXXX-XX-X/XX/XX ...$15.00.
and plays a central role in information management and
speech retrieval [12, 4, 6, 13].
State-of-the-art STD ap-
proaches include two subsystems. The ﬁrst one is an auto-
matic speech recognizer (ASR), which is used to transcribe
the spoken utterances into text. The text transcriptions con-
tain all the possibly recognized words with corresponding
posterior probabilities [5, 12, 13]. The posterior probability
as been one typical conﬁdence measure plays a central
role in keyword searching. The second subsystem is a key-
word searcher which returns the results of term detection
for each query term according to the decoded transcriptions.
Formally, in STD applications, a conﬁdence measure (CM)
is deﬁned to represent the reliability of each detected term
occurrence, which is usually estimated by the recognizer [5,
12]. Relying on the conﬁdence measure, the ﬁnal term de-
tection results could be obtained by threshold-based recall.
However, when only limited training resources are available
for building the ASR system, the accuracy of the recognizer
and the reliability of the conﬁdence measure are relatively
low, which makes it diﬃcult to ﬁnd correct query results in
the speech database.
This paper focuses on the calculation of conﬁdence mea-
sure for STD when the speech recognizer has been built.
In this situation, a one-pass retrieval candidate set can be
obtained for each query. Each candidate contains the term
occurrence location information and the corresponding con-
ﬁdence measure. The baseline system of this paper could
then be evaluated on it directly by conducting standard
score normalization and ﬁnal decision [11, 13].
To im-
prove the reliability of term occurrences, some recent
eﬀorts have attempted to do this work and have achieved
some improvements on STD task. In [10, 9], the conﬁdence
measure of query occurrence is re-estimated based on the
context consistency information. [19] proposed a two-stage
cascaded machine learning approach for rescoring keyword
search outputs for low resource languages. [20] proposed a
modiﬁed logistic regression strategy for term detection op-
timization. Discriminative score normalization method was
introduced to normalize conﬁdence measures through dis-
criminative modeling [14]. Moreover, another method was
proposed in [8] to employ extra acoustic features for getting
a better conﬁdence measure.
However, all these methods fail to utilize long-term con-
texts at document or topic level, which has been proved to
be useful for some other information retrieval (IR) tasks [15,
23]. Clustering and latent topic models have also gained im-
provements over traditional vector space models for IR [21,
2]. Besides, the well known PageRank algorithm considers
arXiv:1509.01899v2  [cs.CL]  10 Sep 2015


## Page 2


the hyperlink between every two pages and computes a con-
verged importance score for each page [1]. Inspired by these
work, this paper proposes to integrate document ranking
information into the calculation of conﬁdence measures of
term occurrences for spoken term detection. The document
ranking information is deﬁned to be the topic relevance
between the document and query term.
For each query
term, there are some documents tend to be more related
to it because they are of a similar topic. When examining
the accuracy of STD results, those topic-related documents
tend to contain more correct hits. In detail, this informa-
tion is quantized as a ranking weight for each document in
this paper. Based on the one-pass retrieval candidates for
a speciﬁc query term, we ﬁrst sum up the conﬁdence mea-
sures of all term occurrences in each document. The doc-
ument ranking weights are then estimated by normalizing
these sums and are further integrated into the original con-
ﬁdence measures through linear interpolation. Experiments
on three standard STD tasks demonstrate the eﬀectiveness
of our proposed method.
For the rest of this paper, we will describe the related
works of this paper in Section 2. The proposed algorithm for
conﬁdence measure calculation will be presented in Section
3. Section 4 and 5 are the experimental setup and results
on three standard STD tasks. Finally, we will conclude our
work in Section 6.
2.
RELATED WORK
There are some other work attempted to utilize long-term
contexts for STD. In [3], they improved term detection per-
formance based on the word burstiness in spoken conversa-
tional corpora.
More recently, [22, 17] took advantage of
word repetition to improve spoken term detection, having
observed the phenomenon of word repetition within single
documents. They leveraged the burstiness of keywords by
taking the most conﬁdent keyword hypothesis in each doc-
ument and interpolating with lower scoring hits. Although
they had designed an eﬀective method to determine the in-
ter coeﬃcients in their experiments, they focussed on intra-
document term repetition, without paying attention to the
inter-document contexts, e.g. the document ranking infor-
mation used in this paper.
The work in [7] is very simi-
lar to us since they also gave a high priority to the candi-
date segments that are included in highly ranked documents.
However, they proposed to calculate the position dependent
document weights recursively. This paper calculates docu-
ment ranking weights in a more easier way and considers
the inter document ranking information. In this paper, we
will rank all documents in the speech database according to
their relevance with a speciﬁc query term and incorporate
such document ranking information into the calculation of
conﬁdence measures.
3.
PROPOSED METHOD
For an input query term, a set of one-pass retrieval can-
didates in the speech database is ﬁrstly generated follow-
ing the conventional STD approach. Each term detection
occurrence commonly contains location information and a
conﬁdence measure, while the location information usually
includes the located document name (or ID), start time and
duration time. For example, for term t, we use Oi to repre-
sent the location information of the i-th detection occurrence
Algorithm 1 Calculate Document Ranking Weights Given a
Query Term
Input: The set of one-pass retrieval candidates given query
term t.
Output: The document ranking weights for all documents
in the database.
Main procedure:
1. Document Clustering
Cluster the documents in all the hypothesized oc-
currences of term t by summing all the conﬁdence
measures in each document d:
Sd(t) =
X
Oi∈d
CMbase(t|Oi, d),
(1)
where Sd(t) can be viewed as the occurrence possibility
of term t in document d. The maximum score Smax(t)
for term t can also be obtained if we traverse all the
documents.
Smax(t) =
max
d∈all documents Sd(t).
(2)
2. Document Ranking
The ranking weight Wd(t) for each document is
calculated using the “relative-to-max” method, which
is obtained by dividing Sd(t) by Smax(t):
Wd(t) = Sd(t)/Smax(t).
(3)
End
of term t.
If the location information indicates that this
occurrence candidate belong to document d, then the conﬁ-
dence measure of the i-th term detection occurrence conﬁ-
dence measure can be denoted as CMbase(t|Oi, d). We use
subscript “base” to emphasis that this measure is obtained
from the one-pass retrieval candidate set. The conﬁdence
measure is designed to describe the reliability of a detected
term occurrence, i.e., a correct query hit is expected to have
a high conﬁdence measure. However, when the ASR subsys-
tem performs poorly, there may be many false alarms with
high conﬁdence measure as well as correct candidates with
low conﬁdence measure.
Based on the idea we have described in the introduction
section, we propose to use document ranking information to
improve the calculation of conﬁdence measures. The algo-
rithm to estimate the document ranking weight Wd(t) for a
input term t is described in Algorithm 1. After the calcula-
tion of document ranking weights, we re-estimate the conﬁ-
dence measure of each occurrence by combining the original
one with the ranking weight of the document it belongs to.
In this work, a linear interpolation is adopted as
CMnew(t|Oi, d) = αWd(t) + (1 −α)CMbase(t|Oi, d),
(4)
where the interpolation coeﬃcient α for interpolation is con-
sistent for all query terms, and it can be tuned using a
development set. In short, the algorithm of conﬁdence re-
estimation can be divided into three steps, i.e., document
clustering, document ranking and conﬁdence re-estimation.
4.
EXPERIMENTAL SETUP
4.1
Data Set and Evaluation Condition
The experiments were conducted using three standard
spoken term detection tasks, the STD 2006 English conver-


## Page 3


sational telephone speech (CTS) evaluation set, the OpenKWS
2013 Vietnamese and the OpenKWS 2014 Tamil develop-
ment sets1. The English CTS evaluation set included about
3 hours of speech, and the keyword set consisted of 411 key-
words. The development sets of Vietnamese and Tamil in-
cluded about 10 hours of speech respectively. The evaluation
keyword set for Vietnamese consisted of 4065 keywords, with
901 of those keywords appearing in the development set and
being used in our experiments. For the Tamil task, we used
the kwlist3 keyword set supplied by IBM, which consisted
of 2375 keywords. The intention of using three tasks was to
evaluate the proposed algorithm using three very diﬀerent
languages, with diﬀerent ASR accuracy, diﬀerent amounts
of training data and with variations in the sizes of keyword
sets. The evaluation criterion used in the experiments was
the Actual Term Weighted Value (ATWV) deﬁned by NIST,
using a cost function of the false alarm probability P(FA)
and P(Miss), averaged over a set of queries2.
4.2
Automatic Speech Recognizer
Our ASR engines were built using the DNN-HMM based
acoustic modeling, which is the state-of-the-art approach for
speech recognition [18].
For the English task, 309 hours of Switchboard speech
were used to train the acoustic model, and the transcriptions
of these speech ﬁles were used to train a 3-gram language
model. The cross entropy criterion was used to train the
DNN models. The word accuracy (ACC) of the ASR system
on the evaluation set was 77.67%.
For the Vietnamese recognizer, two approaches were adopted
to prevent the over-ﬁtting problem in DNN training since
the training corpus contains only about 70 hours of speech.
The ﬁrst approach was cross-lingual training, where we used
a DNN model acquired from 1000 hours of Chinese CTS
data to initialize the Vietnamese DNN parameters.
Fur-
thermore, the rectiﬁed linear unit (ReLU) activation func-
tion was used to replace the sigmoid function in the DNN
model. The transcripts of the Vietnamese training ﬁles were
then used to train a 2-gram language model. A word ACC
of 45.76% was achieved on the development set. The strat-
egy employed for the Tamil ASR engine was similar to that
used for Vietnamese. The only diﬀerence was that the se-
quence training algorithm was applied in the DNN training
for Tamil. A word ACC of 31.03% was achieved on the
development set.
4.3
STD Indexer and Keyword Searcher
We designed a toolkit named iSTD to build our keyword
search subsystem for STD. We followed the work in [12,
13] to construct the inverted index based on confusion net-
works. The term occurrence candidates were then found by
keyword searching on the inverted index.
The conﬁdence
re-estimation algorithm proposed in this paper was also in-
tegrated into this toolkit.
5.
EXPERIMENTAL RESULTS
5.1
Effectiveness of Document Ranking
1http://www.nist.gov/itl/iad/mig/openkws.cfm
2http://www.itl.nist.gov/iad/mig/tests/std/2006/docs/std06-
evalplan-v10.pdf
0
10
20
30
40
50
0.0
0.2
0.4
Document Ranking Position
Recall Rate
0
10
20
30
40
50
0.0
0.2
0.4
Document Ranking Position
Precision Rate
Figure 1: Correlation Curve based on Document Ranking.
In order to validate the rationality of applying the docu-
ment ranking information to STD tasks, we examined the
relationship between the performance of term detection and
the document ranking positions. Here, the document rank-
ing positions were derived by sorting all documents in de-
scending order of the weights calculated following Algorithm
1. Figure 1 shows the correlation curve for the aforemen-
tioned Vietnamese STD task. The results were obtained by
averaging over 901 query keywords. The correlation curves
reveal that the documents with high document ranking weights
usually have high precision and recall of term detection.
In addition, we calculated the Spearman rank correla-
tion coeﬃcient between the two performance measurement
of term detection and the document ranking weights on the
three STD tasks. The results are given in Table 1 and shows
the existence of high correlations. All these results indicate
that the document ranking information is strongly corre-
lated with the STD performance and it is reasonable to in-
tegrate it into the calculation of conﬁdence measures for the
term detection.
Table 1: Spearman correlation for three STD Tasks.
STD Task
Spearman Correlation
Language
ACC
Precision-Rank
Recall-Rank
English
78%
0.93
0.74
Vietnamese
46%
0.74
0.73
Tamil
31%
0.70
0.68
5.2
Results of Tuning Interpolation Coefﬁcients
The interpolation coeﬃcient α in (4) controls the balance
between the document weights and the baseline conﬁdence
measures for a speciﬁc query term. To explore its practical
eﬀcets, the ATWVs on the development set of the Viet-
namese STD task versus diﬀerent interpolation coeﬃcients
were depicted in Fig. 2. We can see that a reasonable choice
for α is within the range 0.05 to 0.4. In the next section, ex-
perimental results will be presented for diﬀerent tasks, where
α was tuned on the development and set to be 0.05, 0.1 and
0.15 for Tamil, Vietnamese and English respectively.
5.3
Results of STD Tasks
We compared the proposed conﬁdence measure re-estimation
algorithm with the baseline system for the three STD tasks.
The baseline system directly adopted the ASR posterior
score as the conﬁdence measure for each query term. Keyword-
speciﬁc threshold was applied for all systems as the ﬁnal
decision recall method [16]. Experimental results are listed
in Table 2.
We can see that the proposed conﬁdence re-
estimation approach achieves consistent improvements for
all the three typical speech retrieval tasks. Considering the
amount of training data available in these three tasks, the re-


## Page 4


0.0
0.2
0.4
0.6
0.8
0.364
0.370
0.376
interpolation coefficient
ATWV
Figure 2: Eﬀect of diﬀerent interpolation coeﬃcient.
Table 2:
Term Detection Results for Three Tasks (ASR
recognition accuracy:
English=78%,
Vietnamese=46%,
Tamil=31%).
Language
Conﬁdence
ATWV
P(Miss)
English
Baseline
0.8064
0.142
Proposed
0.8182 (+1.5%)
0.119
Vietnamese
Baseline
0.3661
0.583
Proposed
0.3779 (+3.2%)
0.565
Tamil
Baseline
0.2785
0.661
Proposed
0.2934 (+5.4%)
0.626
sults in Table 2 also indicate that the proposed conﬁdence re-
estimation method is neither language-dependent, nor sen-
sitive to the amounts of training resources.
6.
CONCLUSIONS
This paper has presented an algorithm to improve the cal-
culation of conﬁdence measures for spoken term detection.
Inspired by the PageRank algorithm and the application of
language models in the text information retrieval area, we
propose to integrate the document ranking information into
the calculation of conﬁdence measures for term occurrences.
The document ranking information indicates the topic rel-
evance between each document and the query term, while
topic-related documents are expected to contain more cor-
rect hits. Experiments on three standard STD tasks demon-
strate the eﬀectiveness of this algorithm by introducing doc-
ument ranking information.
7.
REFERENCES
[1] S. Brin and L. Page. The anatomy of a large-scale
hypertextual web search engine. Computer networks
and ISDN systems, 30(1):107–117, 1998.
[2] B. Chen. Latent topic modelling of word co-occurence
information for spoken document retrieval. In Proc.
ICASSP, pages 3961–3964. IEEE, 2009.
[3] J. Chiu and A. I. Rudnicky. Using conversational word
bursts in spoken term detection. In Proc.
INTERSPEECH, pages 2247–2251, 2013.
[4] J. G. Fiscus, J. Ajot, J. S. Garofolo, and
G. Doddingtion. Results of the 2006 spoken term
detection evaluation. In Proc. SIGIR, volume 7, pages
51–57, 2007.
[5] H. Jiang. Conﬁdence measures for speech recognition:
A survey. Speech communication, 45(4):455–470, 2005.
[6] J. Kohler, M. Larson, F. de Jong, W. Kraaij, and
R. Ordelman. Spoken content retrieval: Searching
spontaneous conversational speech. In ACM SIGIR
Forum, volume 42, pages 66–75. ACM, 2008.
[7] K. Konno, Y. Itoh, K. Kojima, M. Ishigame,
K. Tanaka, and S.-w. Lee. High priority in highly
ranked documents in spoken term detection. In Signal
and Information Processing Association Annual
Summit and Conference (APSIPA), 2013 Asia-Paciﬁc,
pages 1–4. IEEE, 2013.
[8] H.-y. Lee, P.-w. Chou, and L.-s. Lee. Improved
open-vocabulary spoken content retrieval with word
and subword lattices using acoustic feature similarity.
Computer Speech & Language, 2014.
[9] H.-y. Lee, T.-w. Tu, C.-P. Chen, C.-y. Huang, and
L.-s. Lee. Improved spoken term detection using
support vector machines based on lattice context
consistency. In Proc. ICASSP, pages 5648–5651, 2011.
[10] H. Li, J. Han, T. Zheng, and G. Zheng. A novel
conﬁdence measure based on context consistency for
spoken term detection. In Proc. INTERSPEECH,
2012.
[11] J. Mamou, J. Cui, X. Cui, M. J. F. Gales,
B. Kingsbury, K. Knill, L. Mangu, D. Nolden,
M. Picheny, B. Ramabhadran, R. Schl¨uter, A. Sethy,
and P. C. Woodl. System combination and score
normalization for spoken term detection. In Proc.
ICASSP, pages 8272–8276, 2013.
[12] J. Mamou, B. Ramabhadran, and O. Siohan.
Vocabulary independent spoken term detection. In
Proc. SIGIR, pages 615–622. ACM, 2007.
[13] L. Mangu, B. Kingsbury, H. Soltau, H.-K. Kuo, and
M. Picheny. Eﬃcient spoken term detection using
confusion networks. In Proc. ICASSP, pages
7844–7848, 2014.
[14] V. T. Pham, H. Xu, N. F. Chen, S. Sivadas, B. P.
Lim, E. S. Chng, and H. Li. Discriminative score
normalization for keyword search decision. In Proc.
ICASSP, pages 7078–7082, 2014.
[15] J. M. Ponte and W. B. Croft. A language modeling
approach to information retrieval. In Proc. SIGIR,
pages 275–281. ACM, 1998.
[16] Y. Proc. Wang and F. Metze. An in-depth comparison
of keyword speciﬁc thresholding and sum-to-one score
normalization. In INTERSPEECH, 2014.
[17] J. Richards, M. Ma, and A. Rosenberg. Using word
burst analysis to rescore keyword search candidates on
low-resource languages. In Proc. ICASSP, pages
7824–7828, 2014.
[18] F. Seide, G. Li, and D. Yu. Conversational speech
transcription using context-dependent deep neural
networks. In INTERSPEECH, pages 437–440, 2011.
[19] V. Soto, L. Mangu, A. Rosenberg, and J. Hirschberg.
A comparison of multiple methods for rescoring
keyword search lists for low resource languages. In
Proc. INTERSPEECH, 2014.
[20] J. van Hout, L. Ferrer, D. Vergyri, N. Scheﬀer, Y. Lei,
V. Mitra, and S. Wegmann. Calibration and multiple
system fusion for spoken term detection using linear
logistic regression. In Proc. ICASSP, pages 7188–7192,


## Page 5


2014.
[21] X. Wei and W. B. Croft. Lda-based document models
for ad-hoc retrieval. In Proc. SIGIR, pages 178–185.
ACM, 2006.
[22] J. Wintrode and S. Khudanpur. Can you repeat that?
using word repetition to improve spoken term
detection. In Proc. ACL, pages 1316–1325. Association
for Computational Linguistics, 2014.
[23] C. Zhai and J. Laﬀerty. A study of smoothing
methods for language models applied to information
retrieval. ACM Transactions on Information Systems
(TOIS), 22(2):179–214, 2004.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
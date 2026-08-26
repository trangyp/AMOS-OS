---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1911.03726
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1911.03726_Vietnamese_transition-based_dependency_parsing_with_supertag_features

> Source: 1911.03726_Vietnamese_transition-based_dependency_parsing_with_supertag_features.pdf

> Pages: 6

---


## Page 1


Vietnamese Transition-based Dependency Parsing
with Supertag Features
Kiet V. Nguyen
Department of Information Science and Engineering
University of Information Technology
Vietnam National University - Ho Chi Minh City, Vietnam
Email: kietnv@uit.edu.vn
Ngan Luu-Thuy Nguyen
Faculty of Computer Science
University of Information Technology
Vietnam National University - Ho Chi Minh City, Vietnam
Email: ngannlt@uit.edu.vn
Abstract—In recent years, dependency parsing is a fascinating
research topic and has a lot of applications in natural language
processing. In this paper, we present an effective approach to
improve dependency parsing by utilizing supertag features. We
performed experiments with the transition-based dependency
parsing approach because it can take advantage of rich fea-
tures. Empirical evaluation on Vietnamese Dependency Treebank
showed that, we achieved an improvement of 18.92% in labeled
attachment score with gold supertags and an improvement of
3.57% with automatic supertags.
Index Terms—Dependency parsing, transition-based parsing
system, supertags.
I. INTRODUCTION
Dependency parsing is one of the basic and important
natural language processing problems. Outputs of dependency
parsing are dependency structures which are relations of
two words. In recent years, dependency parsing has a lot
of real world applications such as Question Answering [1],
Machine Translation [2], Information Extraction [3], Opinion
Mining [4] and so on. There are a lot of research related to
dependency parsing. Large and prestigious conferences in
the ﬁeld of computational linguistics, including ACL, EACL,
and COLING, have constantly provided many tutorials on
dependency parsing [13], [20]–[23]. Especially, the 2006
and 2007 CoNLL Shared Tasks [8], [15] attracted a lot of
research works in study on data-driven dependency parsing
on many languages.
The problem of dependency parsing is described as: Given
an input sentence with the length of n words S = w0, w1, w2,
..., wn, where w0 = ROOT, the goal of dependency parsing is
to analyze this sentence into a labeled dependency graph as
described in Figure 1. A triple (h, d, l) represents a labeled arc,
where node h is the head (or parent) of the modifier (or child,
dependent) d, and their syntactic dependency relation is l. For
instance, the label SUB describes a subject dependency relation
between the head word mô tả/describes and the modifier kịch
bản/scripts. It is important to note that each word must have
exactly one incoming arc and the zero node indicates the root
of the sentence.
Figure 1. A dependency graph example for a Vietnamese sentence which is
borrowed from [12].
A wide range of research works on dependency parsing
has demonstrated the effectiveness of utilizing rich feature
representations, for examples, ﬁned-grained POS features
[5], rich non-local features [6], supertag features [7]. But
state-of-the-art parsing systems for the Vietnamese language
generally use only two basic kinds of features: word form
and part-of-speech (POS) tag. In this paper, we can take
advantage
of
supertag
features
to
improve
Vietnamese
dependency parsing. Supertags are complex features that
capture ﬁned-grained syntactic phenomenon and long-distance
dependencies [7].
The contributions of this paper to the development of
dependency parsing for Vietnamese are summarized as
follows.
• First, we demonstrate the effectiveness of supertags as
a new kind of feature for Vietnamese dependency parsing;
• Second, we propose three types of design for supertags
which
are
suitable
for
Vietnamese
transition-based
dependency parsing;
• Third, we has built a Vietnamese dependency parsing tool
which is trained on Vietnamese Dependency Treebank
(VnDT) [10]. This system achieves the highest accuracy
and becomes a state-of-the-art dependency parser.
The rest of this paper is oganized as follows. Section 2
discusses the related works on transition-based dependency
parsing, Vietnamese dependency parsing, and parsing features.
arXiv:1911.03726v1  [cs.CL]  9 Nov 2019


## Page 2


Section 3 describes three designs of supertags for improving
Vietnamese dependency parsing. Section 4 shows the ex-
perimental parsing results reported using the cross-validation
scheme. Finally, we draw a conclusion and future directions
for dependency parsing for Vietnamese language in Section 5.
II. RELATED WORKS
A. Transition-based Dependency Parsing
Dependency parsing has two main approaches: grammar-
driven and data-driven. Research works on dependency
parsing mainly concentrate on data-driven models for its
historical development. An architecture of data-driven model
for dependency parsing is shown in Figure 2. There are
three important modules including the learning algorithm, the
parsing model, and the parsing algorithm. Depending on the
parsing algorithm, data-driven dependency parsing is divided
two types including graph-based and transition-based. In this
paper, we used transition-based dependency parsing to build
the Vietnamese dependency parsing system with new features
for the learning module.
Figure 2. An architecture of data-driven dependency parsing system.
Transition-based dependency parsing systems [14], [16],
[17], [25], are among state-of-the-art parsing systems because
of high accuracy and speed in many natural languages.
One of the well-known data-driven dependency parsings is
MaltParser, an open-source system [14] that has a lot of
parameters for customization. It has nine transition-based
parsing algorithms which are divided into three parsing
algorithm groups: Nirve’s algorithm, Convington’s algorithms
and Stack algorithms [18] with a wide range of complex
feature models. Maltparser used two libraries for machine
learning: LIBSVM [28] and LIBLINEAR [29]. MaltParser
can be trained to parse any language as long as we have
a treebank in CoNLL format [8], [15]. In this paper, we
employ new features - supertags to improve the parsing for
the Vietnamese language.
MaltOptimizer
[18]
is
a
automatic
tool
developed
to
optimize
components
of
parsers
developed
using
MaltParser.
MaltOptimizer
can
ﬁnd
optimal
parameters
of each component, it includes an analysis of the dependency
treebank
and
three
optimal
phases.
When
performing
MaltParser
for
a
new
language
or
domain,
there
are
essentially three components of the optimal system that need
to be found: parsing algorithm, feature model, and learning
algorithm. In our experiment, we used MaltOptimizer to ﬁnd
suitable aspects for Vietnamese dependency parsing.
B. Vietnamese Dependency Parsing
On
Vietnamese,
there
are
few
research
works
on
dependency parsing. Some research works [9], [10] developed
Vietnamese
dependency
treebank
from
phrase-structure
treebank VietTreebank. Thi et al. [9] achieved 73.03% and
66.35% in the unlabeled and labeled attachment scores given
by MaltParser using the gold standard POS tags. Nguyen et
al. [10] achieved an unlabeled attachment score of 79.08%
and a labeled attachment score of 71.66%. All accuracies of
these parsers are under 80% in unlabeled attachment score.
There are still many challenges for building Vietnamese
dependency parsers with higher performance.
According to the error analysis results for Vietnamese
dependency parsing in [12], dependency parsing tends to
have lower accuracies on long dependencies. We can see that
a lot of dependency relations (noun modiﬁer, verb modiﬁer,
subject, direct object, root, adjective modiﬁer, coordination,
conjunction, indirect object) have lower accuracies than
others, as shown in Table I (the ﬁgures in this table are from
the paper [12]). Therefore, we focus on ﬁnding new features
to solve above problems related to these dependency relations.
Table I
PRECISION/RECALL FOR DEPENDENCY RELATIONS. DR =
DEPENDENCY RELATION; DLA = DEPENDENCY LENGTH
AVERAGE.
DR
DLA
Precision
Recall
NMOD
1.83
79.04
75.09
VMOD
2.58
60.70
58.22
SUB
3.57
65.70
67.29
DOB
1.63
68.76
64.00
ROOT
5.62
79.92
79.84
AMOD
1.50
72.01
69.12
COORD
5.64
50.94
50.74
CONJ
2.43
70.32
69.85
IOB
2.80
27.45
37.95
Most research works on Vietnamese dependency parsing
have
yet
taken
advantage
of
linguistic
knowledge
for
the design of dependency parsing features. In this paper,
we proposed and designed new features to improve our
dependency parsing for Vietnamese in section 3.
C. Corpus: Vietnamese Dependency Treebank
As shown in Figure 2, in order to build a data-driven
parsing system, we must have a large set of dependency
trees - treebank. Vietnamese Dependency Treebank (VnDT)


## Page 3


is a treebank containing dependency structures converted
from Vietnamese Treebank [19] following the approach of
Nguyen et al. [10]. There are 33 dependency relations in the
VnDT treebank. The percentage of non-projective structures
in VnDT is 4.49%. The percentage of sentences with length
less than 30 words is 80%. The proportion of sentences with
length over 20 words accounts for 45.61%. In this paper, we
conducted experiments on this treebank.
D. Transition-based Dependency Parsing with Supertag Fea-
tures
A wide range of research works [24]–[27] have shown
that transition-based dependency parsing utilizes rich feature
representations. Most experiments on dependency parsers
employed two types of basic features: word forms and
part-of-speech tags. We should ﬁnd a different feature type
which can improve the accuracy of dependency parsing
systems on a new language or domain.
Supertags are lexical templates imposed complex constraints
in a local context. Supertags are extracted from dependency
structure treebank and encode rich syntactic information.
There are many parsing systems improved with supertags, for
instance, the English dependency parsing [7], the German de-
pendency parser with Weighted Constraint Dependency Gram-
mar (WCDG) [30], Hindi transition-based dependency parsing
with supertags based on CCG lexicon [31]. For English, Ouchi
et al. [7] proposed two supertag models for transition-based
dependency parsing with an improvement of 1.3% in unlabeled
attachment score. In our experiments, we used supertags to
improve our dependency parsing. We present in detail our
supertag designs in the next section.
III. SUPERTAG DESIGNS FOR VIETNAMESE
In this paper, we proposed utilizing linguistic features to im-
proving Vietnamese dependency parsing. Supertags are labels
for tokens much like part-of-speech tags but they also encode
ﬁne-grained information of syntax. The major difﬁculty of
the supertag designs is to ﬁnd a tagset that balance between
granularity and predictability. We would like to increase the
number of supertags considerably and make it more difﬁcult
to predict automatically. We designed supertags based on the
two models proposed by Ouchi et al. [7] and error analysis
for Vietnamese dependency parsing by Nguyen et al. [12].
To suit Vietnamese dependency parsing, we design supertags
related to dependency relations such as NMOD, VMOD, SUB,
DOB, ROOT, AMOD, COORD, CONJ, and IOB. Because
these dependency relations have low accuracies as analyzed
in the paper [12]. We describe how to create three supertag
models in the following.
A. Model 0
In Model 0, we designed a supertag which represents
syntactic information as follows: Dependency Label/X, where
X indicates the relative position (direction) of the head of a
Table II
DESIGN OF THREE MODELS OF THE SUPERTAG FOR THE SENTENCE
Word
Model 0
Model 1
Model 2
(Hai)
(Two)
DET
DET
DET
(kịch bản)
(scripts}
SUB/R
SUB/R+L R
SUB/R+L R
(mới)
(new)
NMOD/L
NMOD/L
NMOD/L
(mô tả)
(describe)
ROOT
ROOT+L R
ROOT + SUB/L DOB/R
(cuộc sống)
(life)
DOB/L
DOB/L+R
DOB/L+R
(hiện đại)
(modern)
NMOD/L
NMOD/L
NMOD/L
.
PUNCT
PUNCT
PUNCT
word, which can be left (L) or right (R). With dependency
relations, for examples, NMOD, VMOD, SUB, DOB, ROOT,
AMOD, COORD, CONJ, and IOB, the supertags combine
with the dependency relation label and the left(L) or right(R)
information, else, the supertag is the dependency relation. For
example, kịch bản/script’s in the example in Figure 1 has its
head in the right direction with a label SUB, so its supertag
can be represented as SUB/R. The number of supertags of
Model 0 is 40 tags.
B. Model 1
Model 1 is inherited from Model 0. We also add information
about whether a word has any left or right dependents for
the dependency labels NMOD, VMOD, SUB, DOB, ROOT,
AMOD, COORD, CONJ, and IOB. For instance, the word
cuộc sống/life has a right dependent hiện đại/modern, so we
encode it as DOB/L+R, where the part before + speciﬁes
the head information (DOB/L) and the part afterwards (L)
speciﬁes the position of the dependent (L for left, R for
right). When a word has its dependents in both left and right
directions, such as the word mô tả/descibe in Figure 1, we
combine them using an underline, as in: ROOT+L R. On
Vietnamese Dependency Treebank, Model 1 has 47 supertags.
C. Model 2
Model 2 is inherited from Model 1. For verbs, we add
obligatory dependents of the main verb to dependency
relation labels. The obligatory dependents have the following
dependency relation labels, SUB, DOB, PRD and IOB. For
example, mô tả/describe in the example sentence has an
obligatory dependent with a label SUB in the left direction
and DOB in the right direction, so its supertag is represented
as ROOT + SUB/L DOB/R. The number of supertags of
Model 2 is 63 tags.
In this supertag, we focus on the obligatory dependents of
the verbs with dependency relations such as subjects, objects
(direct and indirect objects), and predicates, as seen in Figure
3. Because it is important to construct dependency graphs


## Page 4


and decrease the number of supertags in this model.
Figure 3.
Obligatory dependents of the verbs with subjects, objects and
predicates
IV. EXPERIMENTS
We used Vietnamese Dependency Treebank [10] to train
and test the dependency parsing (MaltParser, version 1.9.0).
We conducted evaluations of the parser using the 5-fold
cross validation scheme with the average fold size of 2400
sentences. In these experiments, we used automatic supertags,
POS tags, and main-verb-attachment POS tags. We used
LibSVM for the learning phase. For all experiments, the
parameters were set as the followings: c = 0.1 (cost), e = 0.1
(termination criterion), B = 0 (bias).
A. Supertagging Experiments
In this experiment, we used the training and test data
extracted from Vietnamese Dependency Treebank according to
our proposed supertag templates. We used the training dataset
to train the RDRPOSTagger (version 1.2.2) [32] to achieve a
supertagging model. RDRPOSTagger is a rule-based POS tag-
ging toolkit that automatically constructs transformation rules
for POS tagging. It is the current state-of-the-art POSTagger
for Vietnamese.
The test dataset was used to calculate the accuracies of the
resulted Vietnamese suppertagger. The experimental results of
supertagging are shown in Table III. It can be seen in this
table that the supertagging accuracies are around 79-81% for
all three models.
Table III
AVERAGE ACCURACIES OF THREE SUPERTAGS MODELS
Fold
Model 0
(%)
Model 1
(%)
Model 2
(%)
1
81.57
80.52
80.13
2
80.79
80.45
79.25
3
81.20
79.85
79.17
4
80.88
80.76
79.57
5
80.39
80.22
78.95
Average
80.97
80.36
79.41
B. Dependency Parsing Experiments
In this section, we present the experiments on transition-
based dependency parsing for Vietnamese. We conducted
four dependency parsing experiments including the baseline
experiments with basic features (word forms and part-of-
speech tags) and the other experiments with the improved
parsing models corresponding to three supertag models. All
experiments were carried out through 3 steps, including:
• Step 1: We used the MaltOptimizer tool [18] to ﬁnd the
best parameters:
+ Choosing the parsing algorithm.
+ Creating automatically the feature model from ba-
sic feature types (word forms, POS tags, and supertags).
+ Choosing the parameters of the learning algorithm.
• Step
2:
We
used
the
transition-based
dependency
parsing system - MaltParser [18] to conduct experiments
on 5-fold cross validation scheme with settings from
MaltOptimizer results in Step 1.
• Step 3: We used the evaluation tool for dependency
parsing - MaltEval [34] to evaluate the Vietnamese
dependency parsing on both gold and automatic tags
(POS tags and supertags). The experimental results were
reported in accuracy measured with two settings: with
and without consideration of dependency labels, i.e.,
UAS (Unlabeled Attachment Score) and LAS (Labeled
Attachment Score). UAS is the percentage of tokens that
search correctly the heads. LAS is the percentage of
tokens for which the parser has predicted correctly both
the heads and the dependency labels.
Table IV
ACCURACY OF VIETNAMESE DEPENDENCY PARSING (%)
Model
Gold Supertag
Automatic Supertag
UAS
LAS
UAS
LAS
Baseline
76.1
69.9
73.5
65.2
0
88.0
87.9
78.3
68.3
1
89.9
88.8
78.5
68.8
2
88.6
88.5
77.4
68.6
Table IV shows the results of Vietnamese transition-based
dependency parsing with three supertag features. We begin
with baseline features, and add three supertag features (Model
0, Model 1, Model 2). We can see that adding Model 0
features improves the baseline LAS sharply by 18.02% in
the gold supertags while using automatic supertags gives a
smaller improvement of 3.07%. For Model 1, gold supertag
features make the bigger contribution to the improvements
by 18.92% than automatic ones 3.57%. For Model 2, gold
supertag features make a bigger improvement (18.6%) in
comparison with the automatic supertag features (3.37%).
We can see increasing results in Table V. With these results,
we can see that the three supertag models outperform the
baseline in all metrics. In other, the three kinds of supertag
features are effective for the Vietnamese transition-based
dependency parsing.
From the calculations in Table V, we can see that
differences between parsing results on gold supertags and
automatic supertags are quite large. We can see that the


## Page 5


Table V
DIFFERENCE BETWEEN SUPERTAG AND BASELINE PARSING SYSTEMS
Model
Gold Supertag
Automatic Supertag
UAS
LAS
UAS
LAS
0
+11.92
+18.02
+4.78
+3.07
1
+13.08
+18.92
+4.98
+3.57
2
+12.52
+18.62
+3.88
+3.37
parsing accuracy of automatic supertag data may asymptotic
the results on gold supertag data. Therefore, the increase in
the performance of the supertagger is one of the research
work needed to increase the accuracy of the dependency
parsing system. On gold supertag data sets, the LAS accuracy
is growing faster than UAS and the differences are not
signiﬁcant.
In three supertag designs, we can see the supertags of
Model 2 encode rich information of syntax. However, Model
1 is more effective than the two other supertag models (Model
0 and 2). Because the number of supertags in Model 2 is
larger than others and Model 1 is the model which has a good
balance between granularity and predictability. This may be
the reason that makes Model 1 the most effective supertag
model for Vietnamese dependency parsing.
V. CONCLUSION AND FUTURE DIRECTIONS
We present an effective approach to improve transition-
based
dependency
parsing
using
supertag
features.
We
have shown the effectiveness of supertags for Vietnamese
transition-based dependency parsing. Our experimental results
show that Model 1 is the most effective supertag model for
Vietnamese dependency parsing. Futhermore, the supertags
have signiﬁcantly improved the accuracy of Vietnamese
dependency parsing with an increase of 18.92% for gold
supertags and 3.57% for automatic supertags in the LAS
score. To our knowledge, this is the state-of-the-art parsing
result for the Vietnamese language so far. For gold standard
POS tags, we achieved the UAS score of 89.9% and the LAS
score of 88.8%. On automatically-assigned POS tags and
supertags, the scores are 78.5% and 68.8% for the UAS and
the LAS, respectively.
In future research works, we suggest several possible
research
directions
for
improvement
of
the
data-driven
dependency for Vietnamese:
1) We would like to improve the supertagger with the CRF
algorithm [33]. With increasing supertagging accuracy,
the transition-based dependency parsing will also be
improved. We plan to expand the implementation of
the supertags by splitting each supertag into subparts.
For
example,
the
supertag
ROOT+SUB/L DOB/R
is splitted into ROOT, SUB/L and PRD/R which
encode the information of the supertag head, the left
dependents, and the right dependents correspondingly.
2) We
can
also
implement
ﬁne-grained
features
on
POS tags as proposed by Zhou et al [5] to improve
Vietnamese dependency parsing. We can create ﬁne-
grained features by splitting different POS tags to
different levels using hypernym-hyponymy hierarchical
semantic knowledge.
REFERENCES
[1] Hang Cui, Renxu Sun, Keya Li, Min-Yen Kan, and Tat-Seng Chua.
”Question Answering Passage Retrieval Using Dependency Relations”.
In Proceedings of ACM SIGIR, pages 400–407, Salvador, Brazil, 2005.
[2] M. R. Costa-Juss`a and M. Farr´us. ”Statistical machine translation en-
hancements through linguistic levels: A survey”. ACM Computing Surveys
(CSUR), 46(3):42, 2014.
[3] Attardi, Giuseppe and Simi, and Maria. ”Dependency Parsing Techniques
for Information Extraction”. In Proceedings of the First Italian Con-
ference on Computational Linguistics CLiC-it 2014 and of the Fourth
International Workshop EVALITA 2014, Pisa, 2014.
[4] Yuanbin Wu, Qi Zhang, Xuanjing Huang, and Lide Wu. ”Phrase De-
pendency Parsing for Opinion Mining”. Proceedings of the 2009 Con-
ference on Empirical Methods in Natural Language Processing, pages
1533–1541, Singapore, 6-7 August 2009.
[5] Guangyou Zhou, Li Cai, Kang Liu, and Jun Zhao. ”Improving Depen-
dency Parsing with Fined-Grained Features”. In Proceedings of the 5th
International Joint Conference on Natural Language Processing, pages
228–236, Chiang Mai, Thailand, November 8 – 13, 2011.
[6] Yue Zhang, and Joakim Nivre. ”Transition-based Dependency Parsing
with Rich Non-local Features”. In Proceedings of the 49th Annual
Meeting of the Association for Computational Linguistics:shortpapers,
pages 188–193, Portland, Oregon, June 19-24, 2011.
[7] Hiroki Ouchi, Kevin Duh, and Yuji Matsumoto. ”Improving Dependency
Parsers with Supertags”. In Proceedings of the 14th Conference of the
European Chapter of the Association for Computational Linguistics,
pages 154–158, Gothenburg, Sweden, April 26-30 2014.
[8] Buchholz, Sabine, and Erwin Marsi. ”CoNLL-X shared task on multi-
lingual language processing”. In Proceedings of the 10th Conference on
Computational Natural Language Learning (CoNLL), pp. 149-164, New
York, 2006.
[9] Luong Nguyen Thi, Linh Ha My, Hung Nguyen Viet, Huyen Nguyen
Thi Minh, and Phuong Le Hong. ”Building a treebank for Vietnamese
dependency parsing”. In Proceedings of the 10th IEEE RIVF International
Conference on Computing and Communication Technologies, Research,
Innovation, and Vision for the Future, pp.147-151, Vietnam, 2013.
[10] Dat Nguyen, Dai Nguyen, Son Pham, Phuong-Thai Nguyen, and Minh
Le Nguyen. ”From treebank conversion to automatic dependency parsing
for Vietnamese”, In Proceedings of 19th International Conference on
Application of Natural Language to Information Systems, NLDB’14,
pp.196-207, France, 2014.
[11] Cam Vu-Manh, Anh Tuan Luong, Phuong Le-Hong. ”Improving Viet-
namese Dependency Parsing Using Distributed Word Representations”,
Proceedings of the Sixth International Symposium on Information and
Communication Technology, SoICT2015, pp.54-60, UAS, 2015.
[12] Kiet Van Nguyen, Ngan Luu-Thuy Nguyen. ”Error Analysis for Viet-
namese Dependency Parsing”, 2015 Seventh International Conference
on Knowledge and Systems Engineering (KSE), KSE2015, pp.79-84,
Vietnam, 2015.
[13] Joakim Nirve and Sandra Kubler. ”Tutorial: Dependency Parsing”. In
Proceedings of COLING/ACL 2006, Sydney, Australia, 2006.
[14] Joakim Nivre. ”Constraints on non-projective dependency parsing”, In
Proceedings of the 11th Conference of the European Chapter of the
Association for Computational Linguistics, pp. 73-80, Italy, 2006.
[15] Joakim Nivre, Johan Hall, Sandra Kubler, Ryan McDonald, Jens Nilsson,
Sebastian Riedel, and Deniz Yure. ”The CoNLL 2007 Shared Task on
Dependency Parsing”. In Proceedings of the CoNLL Shared Task Session
of EMNLP-CoNLL 2007, pp. 915–932, Prague, 2007.


## Page 6


[16] Joakim Nivre and Ryan McDonald. ”Integrating Graph-Based and
Transition-Based Dependency Parsers”. In Proceedings of the 46th An-
nual Meeting of the Association for Computational Linguistics: Human
Language Technologies (ACL-08: HLT), pp. 950–958, Ohio, 2008.
[17] Joakim Nivre, Johan Hall, Jens Nilsson, Gulsen and Svetoslav, Mari-
nov. ”Labeled pseudoprojective dependency parsing with support vector
machines”. In Proceedings of CoNLL, pp. 221-225, New York, USA.
[18] Miguel Ballesteros and Joakim Nivre. ”MaltOptimizer: An Optimization
Tool for MaltParser”. In Proceedings of the System Demonstration Session
of the Thirteenth Conference of the European Chapter of the Association
for Computational Linguistics (EACL), France, 2012.
[19] Nguyen Phuong-Thai, Vu Xuan-Luong, Nguyen Thi-Minh-Huyen,
Nguyen Van-Hiep and Le Hong-Phuong. ”Building a Large Syntactically-
Annotated Corpus of Vietnamese”. In Proceedings of the Third Linguistic
Annotation Workshop, pp. 182–185, Singapore, 2009.
[20] Qin Iris Wang and Yue Zhang. ”Tutorial: Recent Advances in Depen-
dency Parsing”. In Proceedings of the 11th Annual Conference of the
North American Chapter of the Association for Computational Linguistics
(NAACL), Los Angeles, 2010.
[21] Ryan McDonald and Joakim Nivre. ”Tutorial: Recent Advances in
Dependency Parsing”. In Proceedings of the 14th Conference of the
European Chapter of the Association for Computational Linguistics
(EACL), Sweden, 2014.
[22] Wenliang Chen, Zhenghua Li, and Min Zhang. ”Tutorial: Dependency
Parsing: Past, Present, and Future”. In Proceedings of the 25th Inter-
national Conference on Computational Linguistics (COLING), Dublin,
2014.
[23] Zhenghua Li, Wenliang Chen, and Min Zhang. ”Tutorial: Dependency
Parsing: Past, Present, and Future”. In Proceedings of the 6th Inter-
national Joint Conference on Natural Language Processing (IJCNLP),
Japan, 2013.
[24] H Yamada and Y Matsumoto. ”Statistical dependency analysis using
support vector machines”. In Proceedings of IWPT, France, 2003.
[25] Joakim Nivre, Johan Hall, Jens Nilsson, Atanas Chanev, Gulsen Eryigit,
Sandra Kubler, Svetoslav, Marinov, and Erwin Marsi. ”Maltparser: A
language-independent system for data-driven dependency parsing”. Nat-
ural Language Engineering, pp. 95-135, France, 2007.
[26] Liang Huang and Kenji Sagae. ” Dynamic programming for linear-time
incremental parsing”. In Proceedings of ACL, pp. 1077-1086, Uppsala,
Sweden, 2010.
[27] Yoav Goldberg and Michael Elhadad. ” An Efﬁcient Algorithm for
Easy-First Non-Directional Dependency Parsing”. In Proceedings of
HLT/NAACL, pp. 742-750, Los Angeles, USA, 2010.
[28] Chih-Chung
Chang
and
Chih
Jen
Lin,
2001.
LIBSVM:
A
Library
for
Support
Vector
Machines.
Software
available
at
http://www.csie.ntu.edu.tw/cjlin/libsvm.
[29] Rong En Fan, Kai Wei Chang, Cho Jui Hsieh, and Xiang Rui Wang, and
Chih Jen Lin. 2008. LIBLINEAR: A library for large linear classiﬁcation.
Journal of Machine Learning Research, 9:1871–1874.
[30] Kilian Foth, Tomas By, and Wolfgang Menzel. ”Guiding a Constraint
Dependency Parser with Supertags”. In Proceedings of COLING/ACL
2006, pages 289-296, Sydney, Australia, 2006.
[31] Bharat R Ambati, Tejaswini Deoskar and Mark Steedman. 2013. Using
CCG categories to improve Hindi dependency parsing. In Proceedings of
ACL, pages 604-609, Soﬁa, Bulgaria, August.
[32] Dat Quoc Nguyen, Dai Quoc Nguyen, Dang Duc Pham and Son Bao
Pham. RDRPOSTagger: A Ripple Down Rules-based Part-Of-Speech
Tagger. In Proceedings of the Demonstrations at the 14th Conference of
the European Chapter of the Association for Computational Linguistics
(EACL), pp. 17-20, 2014.
[33] N Okazaki. 2007. CRFsuite: a fast implementation of Conditional
Random Fields (CRFs). http://www.chokkan.org/software/crfsuite/.
[34] Jens Nilsson, Joakim Nivre. MaltEval: An Evaluation and Visualization
Tool for Dependency Parsing. In In Proceedings of the Sixth International
Language Resources and Evaluation, LREC, 2008.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
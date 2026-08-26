---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1610.05652
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1610.05652_Vietnamese_Named_Entity_Recognition_using_Token_Regular_Expressions_and_Bidirect

> Source: 1610.05652_Vietnamese_Named_Entity_Recognition_using_Token_Regular_Expressions_and_Bidirect.pdf

> Pages: 5

---


## Page 1


arXiv:1610.05652v2  [cs.CL]  19 Oct 2016
Vietnamese Named Entity Recognition using Token
Regular Expressions and Bidirectional Inference
Phuong Le-Hong
College of Science
Vietnam National University, Hanoi, Vietnam
Email: phuonglh@vnu.edu.vn
Abstract—This paper describes an efficient approach to im-
prove the accuracy of a named entity recognition system for
Vietnamese. The approach combines regular expressions over
tokens and a bidirectional inference method in a sequence
labelling model. The proposed method achieves an overall F1
score of 89.66% on a test set of an evaluation campaign,
organized in late 2016 by the Vietnamese Language and Speech
Processing (VLSP) community.
I. INTRODUCTION
Named entity recognition (NER) is a fundamental task
in natural language processing and information extraction. It
involves identifying noun phrases and classifying each of them
into a predefined class. In 1995, the 6th Message Under-
standing Conference (MUC) started evaluating NER systems
for English, and in subsequent shared tasks of CoNLL 2002
and CoNLL 2003 conferences, language independent NER
systems were evaluated. In these evaluation tasks, four named
entity types were considered, including names of persons,
organizations, locations, and names of miscellaneous entities
that do not belong to these three types.
More recently, the Vietnamese Language and Speech Pro-
cessing (VLSP) community has organized an evaluation cam-
paign to systematically compare NER systems for the Viet-
namese language. Similar to the CoNLL 2003 share task, four
named entity types are evaluated: persons (PER), organizations
(ORG), locations (LOC), and miscellaneous entities (MISC).
The data are collected from electronic newspapers published
on the web.
This paper presents the approach and experimental results
of our participating system on this evaluation campaign. In
summary, the overall F1 score of our system is 89.66% on a
development set extracted from the training dataset provided
by the organizing committee of the evaluation campaign. Three
important properties of our approach include (1) use of token
regular expressions to encode regularities of organization and
location names, (2) an algorithm to annotate every token in an
input sentence with their token regular expression types, and
(3) a bidirectional decoding approach to boost the accuracy of
the system.
The remainder of this paper is structured as follows. Sec-
tion II gives a brief introduction of multinomial logistic
regression, the main machine learning model which is used in
our system. Section III describes in detail the features used in
our model, including common features used in NER and those
derived from our newly proposed token regular expressions.
This section also presents an algorithm we develop to annotate
every token of an input sentence with its regular expression
type. Section IV introduces a bidirectional decoding scheme
and a method to combine forward and backward models to
get a better model. Section V gives experimental results and
discussions. Finally, Section VI concludes the paper.
II. MULTINOMIAL LOGISTIC REGRESSION
Multinomial logistic regression (a.k.a maximum entropy
model) is a general purpose discriminative learning method
for classification and prediction which has been successfully
applied to many problems of natural language processing, such
as part-of-speech tagging, syntactic parsing and named entity
recognition. In contrast to generative classifiers, discriminative
classifiers model the posterior P(y| x) directly. One of the
main advantages of discriminative models is that we can
integrate many heterogeneous features for prediction, which
are not necessarily independent. Each feature corresponds to
a constraint on the model. In this model, the conditional
probability of a label y given an observation x is defined as
P(y| x) =
exp(θ · φ(x, y))
P
y∈Y exp(θ · φ(x, y)),
where φ(x, y) ∈RD is a real-valued feature vector, Y is the set
of labels and θ ∈RD is the parameter vector to be estimated
from training data. This form of distribution corresponds to
the maximum entropy probability distribution satisfying the
constraint that the empirical expectation of each feature is
equal to its true expectation in the model:
bE(φj(h, t)) = E(φj(h, t)),
∀j = 1, 2, . . ., D.
The parameter θ ∈RD can be estimated using iterative
scaling algorithms or some more efficient gradient-based op-
timization algorithms like conjugate gradient or quasi-Newton
methods [1]. In this paper, we use the L-BFGS optimization
algorithm [2] and L2-regularization technique to estimate the
parameters of the model. This classification model is applied
to build a classifier for the dependency parser where each
observation x is a parsing configuration and each label y is a
transition type.


## Page 2


III. FEATURE REPRESENTATIONS
In discriminative statistical classification models in general
and the maximum entropy model in particular, features play an
important role because they provide the discriminative ability
to efficiently disambiguate classes.
In order to facilitate the extraction of various feature types,
each lexical token is associated with a surface word and an
annotation map containing different information of the text
in the form of key and value pairs. The current annotation
map includes values for part-of-speech, chunk, token regular
expression type and named entity label.
In the context of named entity recognition, the information
about surface word, part-of-speech and chunk tag are given;
and in a training phrase, named entity tags are also provided. In
the next subsection, we describe the regular expression types
which are associated with each token to add some helpful
semantic information for named entity disambiguation.
A. Regular Expressions over Tokens
We use regular expressions at both character level and token
level to infer useful features for disambiguating named entities.
While character-level regular expressions are used to detect
word shape information, which was shown very important in
NER, token-level regular expressions are very helpful to detect
word sequence information in many long named entities [3].
Common word shape features that our system uses include:
• is lower word, e.g., “tỉnh”
• is capitalized word, e.g., “Tổng_cục”
• contains all capitalized letters (allcaps), e.g., “UBND”
• is mixed case letters, e.g., “iPhone”
• is capitalized letter with period, e.g., “H.”, “Th.”, “U.S.”
• ends in digit, e.g., “A9”, “B52”
• contains hyphen, e.g., “H-P”
• is number, e.g., “100”
• is date, e.g., “20-10-1980”, “10/10”
• is code, e.g, “21B”
• is name, where consecutive syllables are capitalized, e.g.,
“Hà_Nội”, “Buôn_Mê_Thuột”
Using the word shape features presented above, we then
introduce regular expressions over a sequence of words to
capture its regularity. Suppose that fPress(w) is a boolean
function which returns true if w is in a set of predefined words
related to press and newspaper domain, for example {“báo”,
“tờ”, “tạp_chí”, “đài”, “thông_tấn_xã”}, and returns false
otherwise. And suppose that fName(w) is a boolean function
which returns true if w is a name or an allcaps, and returns
false otherwise. Then, we can define the following token
regular expressions to capture the name of a news agency:
[fPress, fName]
This sequence pattern matches many different, probably un-
seen news agency names, such as “báo Tuổi_Trẻ, thông_tấn_xã
Việt_Nam”, or “tờBatam”.
In a similar way, suppose that we have a function fProvince
which matches common names of administrative structure
at various levels such as “{tỉnh, thành_phố, quận, huyện,
xã,...}”, we can build a sequence pattern
[fAllcaps, fProvince, fName]
which
matches many
corresponding organization names
such as “UBND thành_phốĐà_Nẵng”, “HĐND huyện
Mù_Căng_Chải”, etc.
Note that an elementary token pattern can be reused in mul-
tiple sequence patterns. For example, the following sequence
pattern
[fProvince, fName]
can
match
provincial
names,
which
are
usually
of
type location, such as “tỉnh Quảng_Ninh”, “thành_phố
Hồ_Chí_Minh”.
By examining the training data, we have manually built a
dozen of regular expresions to match common organization
names, and six regular expressions to match common location
names. These regular expressions over tokens are shown
to provide helpful features for classifying candidate named
entities, as shown in the experiments.
B. Regular Expression Type Annotation
Once regular expressions over tokens have been defined,
we add a regular expression type for each word of an input
sentence by annotating its corresponding annotation map key.
Together with word identity, word shape, part-of-speech and
chunk tag information, regular expression types provide help-
ful information for better classifying named entities, as shown
in the latter experiments.
We use a greedy algorithm to annotate regular expres-
sion type for every word if it has. Basically, the algorithm
works as follows. Given a sequence of T tokens (or words)
[w1, w2, . . . , wT ] and a map of regular expressions over tokens,
each key name defines a pattern sequence: (patternName,
patternRegExp), we first search for all positions of the sentence
which begins a pattern match, and select the longest match,
say, pattern patternName which ranges from token wi to token
wj, for 1 ≤i < j ≤T . Then, all the tokens wi, wi+1, . . . , wj
are annotated with the same regular expression type pat-
ternName. And finally, the algorithm recursively annotates
types for tokens in the remaining two halves of the sequence
[w1, w2, . . . , wi−1] and [wj+1, wj+2, . . . , wT ].
Note that this is a greedy method in that we always choose
the longest pattern in each run. This is a plausible approach
since if there are multiple matches, longer patterns tend to be
more correct than shorter ones. For example, there are two
matches on the token sequence “UBND tỉnh Đồng_Nai”, one
is an organization name over the entire sequence, and another
is a location name over the last two tokens; the longer one is
the correct match.
C. Feature Set
In this subsection, we describe the full feature set that is
used in our system to classify a token at a position of a
sentence.


## Page 3


• Basic features: current word w0, current part-of-speech
p0, current chunk tag c0, previous named entity tags t−1
and t−2 (or a special padding token “BOS” – begin of
sentence);
• Word shape features, as described in the previous sub-
section;
• Basic joint features: previous word w−1 (or “BOS”), joint
of current and previous word w0 + w−1, next word w+1
(or “EOS” – end of sentence), joint of current and next
word w0 + w+1, previous part-of-speech p−1, joint of
current and previous part-of-speech p0 + p−1, next part-
of-speech p+1, joint of current and next part-of-speech
p0+p+1, joint of previous and next part-of-speech p−1 +
p+1, joint of current word and previous named entity tag
w0 + t−1;
• Regular expression types: current regular expression (reg-
exp) type r0 (or “NA” – not available), previous regexp
type r−1 (or “NA”/“BOS”), joint feature r0 + r−1, next
regexp type r+1 (or “NA”/“EOS”), joint feature r0 +r+1,
joint features between current word and regexp types
w0 + r0, w0 + r−1, w0 + r+1, and lastly, joint features
between current part-of-speech and regexp types p0 + r0,
p0 + r−1, and p0 + r+1.
IV. BIDIRECTIONAL DECODING
The standard decoding algorithm for sequence labelling
is the Viterbi algorithm, which is a dynamic programming
algorithm for finding the most likely sequence of tags given
a sequence of observations. In this work, we also use the
Viterbi algorithm to find the best tag sequence for a given
word sequence. However, we found a significant improvement
of tagging accuracy when combining two decoding directions,
both forward decoding and backward decoding. In this section,
we describe our bidirectional decoding approach.
Given a sequence of T words [w1, w2, . . . , wT ], for each
word wj, a pre-trained multinomial logistic regression model
computes a conditional probability distribution over possible
tags yj ∈Y:
P(yj|cj) =
exp(θ · φ(cj, yj))
P
yj∈Y exp(θ · φ(cj, yj)),
∀j = 1, 2, . . ., T,
where φ(cj, yj) is the feature function which extract features
from context cj containing known information up to position j.
As described in the previous section, cj encodes useful features
for predicting yj, including those extracted from a local word
window wj−2, . . . , wj+2, two previous tags yj−1, yj−2, and
joint features between them.
The probability of a tag sequence given a word sequence
is approximated by using the Markov property. In a log scale,
we have
log P(y1, . . . , yT |w1, . . . , wT ) ≈
T
X
j=1
log P(yj|cj).
The Viterbi algorithm is then used to find the best tag
sequence by1, by2, . . . , byT corresponding to the max-probability
path on a lattice of size K × T where K = |Y| is the size of
the tag set.
Note that in the second-order Markov model as above, each
context cj uses the two tags yj−2 and yj−1 which have been
infered in the previous steps. That said, this is a left-to-right
inference scheme. In the experiments, we use a greedy update
at each position j where the tag yj is chosen as the best tag of
each local probabilty distribution computed by the maximum
entropy model.
A reversed inference scheme does the same decoding proce-
dure but in a right-to-left fashion, where two tags yj+2, yj+1
are infered before decoding yj. In essence, when performing
backward decoding, we can use the same Viterbi decoding
procedure as in the forward counterpart, but now using a
backward maximum entropy model to compute the probability
of a tag given its following tags. It turns out that both the
training and decoding procedure for this model can be reused
simply by reversing the word and tag sequences at both training
and test stages.
An important finding in our experiments is that the back-
ward model is much better than the forward model in recog-
nizing location names while it is much worse in recognizing
person names. We therefore propose a method to combine the
strength of the two models to boost the accuracy of the final
model. The combination method will be presented in detail in
the experiments.
V. EXPERIMENTS
A. Datasets
We evaluate our system on the training dataset provided
by the VLSP NER campaign.1 This dataset contains 16, 858
tagged sentences, totaling 386, 520 words. The dataset contains
four different types of named entities: person (PER), loca-
tion (LOC), organization (ORG), and miscellaneous (MISC).
Since the real test set has not been released, we divide this
training set into two parts, one for training and another for
development. The training dataset has 306, 512 tokens (79.3%
of the corpus), and the development dataset has 80, 007 tokens
(20.7% of the corpus).
B. Parameter Settings
The multinomial logistic regression models used in our
system are trained by the L-BFGS optimization algorithm
using the L2-regularization method with regularization param-
eter fixed at 10−6.2 The convergence tolerance of objective
function is also fixed at 10−6. The maximum number of
iterations of the optimization algorithm is fixed at 300. That
is, the training terminates either when the function value
converges or when the number of iterations is over 300. We
use the feature hashing technique as a fast and space-efficient
method of vectorizing features. The number of features for our
models are fixed at 262, 144 (that is, 218).
These parameters values are chosen according to a series of
experiments, for example, using a smaller number of features
1http://vlsp.org.vn/evaluation_campaign_NER
2Using a larger regularization parameter underfits the model.


## Page 4


(say, 217) reduces slightly the performance of the models,
while using a larger number does not result in an improvement
of accuracy but increase the training time.
C. Main Results
We train our proposed models on the training set and test
them on the development set as described in the previous
subsection. The performance of our system is evaluated on the
development set by running the automatic evaluation script of
the CoNLL 2003 shared task3. The main results are shown in
Table I.
Table I: Performance of our system
Type
Precision
Recall
F1
All
89.56%
89.75%
89.66
LOC
84.97%
94.13%
89.32
MISC
93.02%
81.63%
86.96
ORG
79.75%
52.72%
63.48
PER
94.82%
92.75%
93.77
Our system achieves an F1 score of 89.66% overall. Organi-
zation names are the most difficult entity type for the system,
whose F1 is the lowest of 63.48%. Person names are the easiest
type for the system whose both precision and recall ratios are
high and the F1 score of this type is 93.77%.
D. Effect of Bidirectional Inference
In this subsection we report and discuss the results using
unidirectional inference, either forward and backward. The
performance of the forward model is shown in Table II and
that of the backward model is shown in Table III.
Table II: Performance of the forward model
Type
Precision
Recall
F1
All
88.08%
87.10%
87.59
LOC
81.61%
86.54%
84.00
MISC
97.67%
85.71%
91.30
ORG
79.75%
52.72%
63.48
PER
94.38%
93.45%
93.91
Table III: Performance of the backward model
Type
Precision
Recall
F1
All
88.03%
87.94%
87.98
LOC
85.60%
91.80%
88.59
MISC
100.00%
83.67%
91.11
ORG
66.45%
43.10%
52.28
PER
92.15%
92.54%
92.34
We see that the backward model is better than the forward
model by 4.6 point of F1 score in recognizing location
names. This is surprising since the only difference between
the two models is a reverse of input sentences. One possible
explanation of this effect is that when recognizing location
names of a token sequence w1, w2, . . . , wn, if we already know
about the type of wn it is easier to predict its previous token
3http://www.cnts.ua.ac.be/conll2003/ner/
wn−1 and so on. We conjecture that this is due to the natural
structure of Vietnamese location names.
However, the backward model underperforms the forward
model in recognizing the organization names by a large
margin. Its F1 score of this type is only 52.28%, while
that of the forward model is 63.48%. This is understandable
because our token regular expressions are designed to capture
regularities in many organization names, as described in the
subsection III-A, but these expressions do not work anymore
if an input token sequence is reversed.
Either of the two unidirectional models achieves an overall
F1 score of 88.00% but when they are combined, our system
achieves an overal score of 89.66%, as presented in the
previous subsection. The combined model has both the strong
ability of recognizing location names of the backward model
and is good at recognizing organization names of the forward
model.
E. Effect of Token Regular Expressions
In this subsection, we report the effectiveness of token
regular expressions to our model. We observe that using token
regular expressions significantly improves the performance of
the system.
If the token regular expressions for ORG type are not used,
its F1 score of the forward model is 62.94%. Adding token
regular experessions for this type help boost this score to
65.01%. Similarly, when token regular expressions for LOC
are not used, its score of the forward model is 82.19%. Adding
six token regular expressions for this type improves its score
to 83.07%. However, we observe that when all the regular
expressions for this two named entity types are used together,
they interact with each other and make their scores slightly
different, as shown in the Table II.
F. Software
The named entity recognition system developed in this work
has been integrated into the Vitk toolkit, which includes some
fundamental tools for processing Vietnamese texts. The toolkit
is developed in Java and Scala programming languages, which
is open source and freely downloadable for research purpose.4
An interesting property of this toolkit is that it is an Apache
Spark application, which is a fast and general engine for large
scale data processing. As a result, Vitk is a very fast and
scalable toolkit for processing big text data.
VI. CONCLUSION
We have introduced our approach and its experimental result
in named entity recognition for Vietnamese text. We have
shown the effectiveness of using token regular expressions, of
bidirectional decoding method in a conditional Markov model
for sequence labelling, and of combining the backward and
forward models. Our system achieves the overall F1 score of
89.66% on a test corpus.
4https://github.com/phuonglh/vn.vitk


## Page 5


ACKNOWLEDGEMENTS
This research is partly financially supported by Alt Inc.5,
and in particular we thank Dr. Nguyen Tuan Duc, the head
of Alt Hanoi office. We thank the developers of the Apache
Spark software.
REFERENCES
[1] G. Andrew and J. Gao, “Scalable training of l1-regularized log-linear
models,” in Proceedings of ICML, Oregon State University, Corvallis,
USA, 2007, pp. 33–40.
[2] J. Nocedal and S. J. Wright, Numerical Optimization, 2nd ed. New York:
Springer, 2006.
[3] E. F. Tjong Kim Sang and F. De Meulder, “Introduction to the conll-
2003 shared task: Language-independent named entity recognition,” in
Proceedings of CoNLL-2003, W. Daelemans and M. Osborne, Eds.
Edmonton, Canada, 2003, pp. 142–147.
5http://alt.ai/corporate

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
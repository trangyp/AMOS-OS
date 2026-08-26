---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1910.13732
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1910.13732_LSTM_Easy-first_Dependency_Parsing_with_Pre-trained_Word_Embeddings_and_Characte

> Source: 1910.13732_LSTM_Easy-first_Dependency_Parsing_with_Pre-trained_Word_Embeddings_and_Characte.pdf

> Pages: 6

---


## Page 1


LSTM Easy-ﬁrst Dependency Parsing with Pre-trained Word
Embeddings and Character-level Word Embeddings in Vietnamese
Binh Duc Nguyen∗, Kiet Van Nguyen† and Ngan Luu-Thuy Nguyen‡
University of Information Technology
Vietnam National University – Ho Chi Minh City, Vietnam
Email: ∗14520071@gm.uit.edu.vn, †kietnv@uit.edu.vn, ‡ngannlt@uit.edu.vn
Abstract—In Vietnamese dependency parsing, several methods
have been proposed. Dependency parser which uses deep neural
network model has been reported that achieved state-of-the-
art results. In this paper, we proposed a new method which
applies LSTM easy-ﬁrst dependency parsing with pre-trained
word embeddings and character-level word embeddings. Our
method achieves an accuracy of 80.91% of unlabeled attachment
score and 72.98% of labeled attachment score on the Vietnamese
Dependency Treebank (VnDT).
I. INTRODUCTION
Over the last decade, there has been considerable interest
in dependency parsing which generates grammatical relations
between two words in the sentence. For instance, in the
CoNLL 2007 shared task [1], each participating team tested
their system in thirteen different languages. In 2014, the
SPMRL shared task [2] was held to evaluate dependency
parsing on nine morphologically rich languages.
Since CoNLL-X [3], there are two dominant dependency
parsing models which are transition-based parsing and graph-
based parsing. These names are ﬁrst mentioned in [4]. Both
two models are data-driven parsers which are learned from
an annotated corpus and have shorter development time than
rule-based system [4].
The last few years has witnessed a rapid development of
neural-network methods. Many works showed that neural-
network methods can achieve state-of-the-art results on dif-
ferent tasks of Natural Language Processing such as Named
Entity Recognition (NER) [5], Machine Translation [6], [8].
In dependency parsing, there are studies using deep neural-
networks to encode features without hand-crafted deﬁnition
[9], [10], [11] and [12].
In Vietnamese, there are several researchers working on
dependency parsing. Nguyen et al. [14] and Nguyen et al. [15]
automatically convert a constituent treebank to a dependency
treebank. Nguyen and Nguyen [16] used supertags features and
Vu-Manh et al. [17] used word embeddings on the transition-
based parser. Nguyen et al [18] used BiLSTM encoder to
generate word representation vectors and obtained a state-of-
the-art result on Vietnamese Dependency Treebank (VnDT)
[15].
We found that [18] did not incorporate pre-trained word
embeddings in the vector representation of words. Although
this feature can improve the accuracy of dependency parsing
because of its rich context information [11] [12] and [17].
Beside the pre-trained word embeddings, character-level
word embeddings has been found useful for NER [5] or
dependency parsing [13]. It represents words by combining
their character embeddings so it does not depend on the
word-based lookup dictionary. However, no previous study has
investigated the impact of character-level word embeddings on
dependency parsing for Vietnamese.
The parser we used is a variant of transition-based parser
called tree LSTM easy-ﬁrst [11] which is fast speed and
similar to human annotation [19]. The tree LSTM easy-ﬁrst
is reported as the state-of-the-art parser for Chinese [11]. Be-
cause Chinese syntax structures is very similar to Vietnamese,
we believe that this parser can give a good accuracy for
Vietnamese dependency parsing.
In this paper, we focused on applying two word represen-
tation features on Vietnamese dependency parsing, which are
pre-trained word embeddings and character-level word embed-
dings. Although Vu-Manh et al. [17] have already used pre-
trained word embeddings for Vietnamese dependency parsing.
Their paper used MaltParser [7] which is incomparison with
other neural network parsers like Tree LSTM easy-ﬁrst parser.
Our paper is the ﬁrst study which applied character-level word
embedding to dependency parsing on VnDT as well as the
ﬁrst time easy-ﬁrst parser was utilized with character-level
word embeddings in either Vietnamese or English. Our method
makes an improvement in parsing accuracy (0.79% UAS and
1.51% LAS) and achieves state-of-the-art performance on
Vietnamese dependency parsing (80.91% UAS and 72.98%
LAS).
The remainder of the paper is organized as follows: Section
2 describes easy-ﬁrst parsing algorithm used in this paper.
Word representation features are represented in Section 3. We
evaluate the results of the methods in Section 4 and draw the
conclusion and future work in Section 5.
II. EASY-FIRST PARSING
Easy-ﬁrst parsing is a type of syntactic parsing algorithm
which is a variant of transition-based parsing. This method is
ﬁrst proposed by Goldberg and Elhadad [19]. Several studies
were proposed for improving the accuracy of this method such
as Ma et al [20] using beam search strategy to effectively ex-
plore the search space of parsing process. Another method was
proposed by Kiperwasser & Goldberg [11] which uses deep
neural network to learn model’s parameters, entire dependency
arXiv:1910.13732v1  [cs.CL]  30 Oct 2019


## Page 2


tree was encoded by LSTMs and was applied as deep features
for effective learning.
A. The parsing process
In the parsing process, there are a list of partial structures
called pending which is the main data-structure of the parser,
the parser will stop if the pending have only one element in it. A
partial structure can be a token or a dependency structure which
is built from the previous parse steps. At each step of the parsing
process, the algorithm generates all possible actions. These
actions are ranked by a scoring function. The highest scoring
action is chosen to applied to the pending. There are two types
of actions which are LEFT and RIGHT. Let p1, p2, p3..., pn
be the elements of pending. The action LEFT(i,r) adds the
dependency edge (pi+1, pi) with the relation r and remove
pi from the pending, while the action RIGHT(i,r) adds the
dependency edge (pi, pi+1) with the relation r and remove
pi+1 from the pending. Figure 1 demonstrates how to parse the
sentence "Tôi có một con mèo" using easy-first algorithm. Let
Arcs be the list of dependency edges in parsing process. At step
1, action LEFT(4, nmod) is chosen, edge (mèo, con, nmod) is
added to Arcs. At step 2, action LEFT(3,det) is ranked highest
so the edge (mèo, một, det) is added to Arcs. At the third step,
the chosen action is RIGHT(2, dobj) and the edge (có, mèo,
dobj) is added to Arcs. At the final step, action LEFT(1,nsubj)
was chosen and produce the output dependency structure.
Tôi
có
một
con
mèo
Tôi
có
một
mèo
con
nmod 
Tôi
có
mèo
con
nmod 
một
det
Tôi
có
mèo
con
nmod 
một
det
dobj
Tôi
có
mèo
con
nmod 
một
det
dobj
subj
1
2
3
4
5
1
2
3
4
1
2
3
1
2
LEFT(4, nmod)
LEFT(3, det)
RIGHT(2, dobj)
LEFT(1, subj)
Figure 1.
The sentence "Tôi có một con mèo"is parsed using easy-first
algorithm.
At one step of the parsing process, for a pending with n
elements, there are n −1 attachment points where actions can
be applied to. For each attachment point, there will be 2 ∗R
actions where R is the number of total dependency relations.
Therefore, there are 2R(n −1) actions can be chosen at each
step so there are more than one valid action sequences leads
to the dependency structure of the sentence. That gives more
examples to the learning algorithm.
B. The LSTMs Easy-ﬁrst algorithm
In this paper, we used an extended version of the easy-ﬁrst
algorithm [11], which employs LSTMs to represent a depen-
dency structure as a vector and used multilayer perceptron
(MLP) to score the parse actions. The dependency structure
can be described as follows [11]:
t
t. l3
t. l2
t. l1
t. r1
t. r2
t. r3
• The depenency structure is a tree with root node t and t
is associated with the head word wt.
• For every child of t, if the head word of this child is on
the left of wt according to their positions in the sentence,
this child will be the left child, otherwise, this child will
be the right child. The nearest child of the head node is
indexed as 1 while the left most or right most child has
the largest index.
• Let enc(t) be the vector representing dependency struc-
ture t. All of left children t.l1...t.lkl are fed to an LSTM
called LSTML, all of right children t.r1...t.rkr are fed
to an LSTM called LSTMR. The ﬁrst input of LSTM
is the vector representation of the head word vi(t), the
last input is the vector representation of left-most child
or right-most child. The output of LSTML and LSTMR
are concatenated el(t) ◦er(t). The dimension of the con-
catenated vector is reduced using linear transformation,
followed by a non-linear activate function. The result
vector represents dependency structure.
enc(t) = g(W e.(el(t) ◦er(t) ◦l(t)) + be)
(1)
el(t) = LSTML(vi(t), enc(t.l1)...enc(t.lkl))
(2)
er(t) = LSTMR(vi(t), enc(t.r1)...enc(t.rkr))
(3)
• The process runs recursively and stop at leaf nodes
where vi(leaf) is the vector representation of word i
in sentence. Which will be described in the Section 3.
Figure 2 shows the network of dependency structure of
the sentence "Tôi có một con mèo".
enc(leaf) = g(W e.(el(leaf) ◦er(leaf)) + be)
(4)
el(leaf) = LSTML(vi(leaf))
(5)
er(leaf) = LSTMR(vi(leaf))
(6)
Pseudocode for Tree LSTM Easy-ﬁrst parsing is described
in Algorithm 1 [11]. The parsing algorithm is similar to the
original [19] but with some differences:


## Page 3


Tôi
subj
dobj
có
một
con
det
nmod
mèo
LSTML
LSTMR
mèo
mèo
mèo
con
một
LSTML
LSTMR
có
có
Tôi
có
det
nmod
dobj
subj
Figure 2. Networks of dependency structure of sentence "Tôi có một con mèo".
The solid circle is is a representation of the hidden state of LSTM networks, the
dotted circle is a representation of the function of concatenating two LSTM
networks. The inputs of LSTM hidden state include previously hidden state,
vector representation of the child node and a vector represented for dependency
relation between child node and head node.
• When the action was applied to pending, the vector of
modiﬁer will be appended to the LSTMs of the head
(LSTML or LSTMR).
• There are two scoring functions which are modeled as
multi-layer perceptrons (MLP) - ScoreU and ScoreR.
ScoreU scores an action based on its head and modiﬁer
while ScoreR scores an action based on head, modiﬁer
and the relation of this action. Scoring functions are using
information of partial structure at the attachment point
as well as its neighbors. The score of an action a with
relation r in ScoreU or ScoreR is an element of the
output layer of MLP. Size of the output layer of MLPU
is 2 while MLPR is 2R where R is the total number of
dependency relations:
ScoreU(i, a) = MLPU(xi)[a]
(7)
ScoreL(i, a, r) = MLPL(xi)[r, a]
(8)
xi = pi−2 ◦... ◦pi+3
(9)
• The score of an action is the sum of ScoreU result and
ScoreR result:
Score(i, a, r) = ScoreU(i, a) + ScoreL(i, a, r)
(10)
Algorithm 1: LSTM Easy-ﬁrst dependency parsing algo-
rithm
Input : a sentence= w1...wn, parameter w
Output: sentence’s dependency arcs
1 Arcs ←{} ;
2 for i in {0..len(sentence)-1} do
3
pending[i].w = wi;
4
pending[i].LSTML.init().append(wi);
5
pending[i].LSTMR.init().append(wi);
6 end
7 while len(pending) > 1 do
8
actions ←{};
9
for i in 0...len(pending) −1 do
10
for r in Rels do
11
for a in [LEFT, RIGHT] do
12
actions.append(i, a, r);
13
end
14
end
15
end
16
(i, a, r) = argmaxact∈actions Score(act, w);
17
if a == LEFT then
18
Arcs.append(pi+1, pi, r);
19
pending[i + 1].LSTML.append(pi, r);
20
pending.remove(pi) ;
21
else if a == RIGHT then
22
Arcs.append(pi, pi+1, r);
23
pending[i].LSTMR.append(pi+1, r);
24
pending.remove(pi+1) ;
25 end
26 return Arcs
C. The training process
For parameters update, a hinge loss function with margin 1
is used [11]:
max{0, 1 −maxi,a,r∈GScore(i, a, r)+
maxi,a,r∈A\GScore(i, a, r)}
(11)
Pseudocode of training phrase is described in Algorithm
2 [11]. Where A is set of valid actions and G is set of all
possible actions at the current step. For validation checking,
the parser uses Oracle which is a set of deﬁned rules based
on gold dependency structure of a sentence. The Oracle used
in Tree LSTM Easy-ﬁrst is dynamic oracle [22]. If an invalid
action was chosen, in the next step, the parser will treat an
action which leads to best acceptable dependency structure as
the valid action. The rules used in Tree LSTM Easy-ﬁrst parser
are deﬁned as follows:
• Head, modiﬁer and relation of action must be in the gold
dependency structure of the sentence.
• Modifer of the action must be complete which means
that all children of the modiﬁer have been explored at
the previous step.


## Page 4


• If the gold head of modiﬁer is removed from pending, the
action then is valid if the dependency relation of modiﬁer
is the same with the relation in the gold dependency
structure despite that the head is different.
Algorithm 2: LSTM Easy-ﬁrst training algorithm for
dependency parsing
Input : a sentence= w1...wn, parameter w
Output: sentence’s dependency arcs
1 for i in 1...n do
2
errors ←[] ;
3
for sentence in corpus do
4
for i in 0..len(sentence)-1 do
5
pending[i].w = wi;
6
pending[i].LSTML.init().append(wi);
7
pending[i].LSTMR.init().append(wi);
8
end
9
while len(pending) > 1 do
10
actions ←{};
11
for i in {0...len(pending) −1} do
12
for r in Rels do
13
for a in [LEFT, RIGHT] do
14
if is valid(i, a, r) then
15
G.append(i, a, r);
16
else
17
A.append(i, a, r);
18
end
19
end
20
end
21
i, a, r, s = argmaxact∈A Score(act, w);
22
i′, a′, r′, s′ = argmaxact∈G Score(act, w);
23
if s > 1 + s′ then
24
ibest, abest, rbest = i, a, r;
25
else
26
ibest, abest, rbest = i′, a′, r′;
27
errors.append(1 −s + s′);
28
apply action(ibest, abest, rbest);
29
if len(errors) > 50 then
30
update;
31
errors ←[];
32
end
33
end
34
end
35
if len(errors) > 0 then
36
update;
37
end
38 end
When the loss of parse step is greater than zero, this step is
count as one error. If the total errors are greater than 50, all
parameters are updated using Adam Optimizer.
III. WORDS REPRESENTATION
A. Representing words using word form and POS tag
The baseline approach of representing words as vectors
is used information of word form and POS tag which are
embeddings and jointly trained with the networks. Word-form
and POS-tag vectors are concatenated and transformed to v′
i
via a linear transformation followed by a non-linear activation
function. Kiperwasser and Goldberg [11] used Bidirectional
LSTMs to incorporate the context information of words in
a sentence. For the word ith in sentence, network LSTMF
runs from the begining of the sentence to word ith while
LSTMB runs in reverse order. Outputs of two networks are
concatenated to produce vector vi representing word i. The
ﬁgure 3 illustrates how a word is represented using BiLSTMs.
v′
i = g(W v.(wi ◦pi) + bv)
(12)
fi = LSTMF (v′
1, v′
2, ...v′
i)
(13)
bi = LSTMB(v′
n, v′
n−1, ..., v′
i)
(14)
vi = (fi ◦bi)
(15)
Tôi
có
một
con
mèo
LSTMB
LSTMF
Word 
embedding 
POS 
embedding 
Figure 3. Words’s vector representation using BiLSTMs
B. Pretrained word embeddings
A common way to incorporate context information of
words is using word representations learned from unanno-
tated corpora. In pre-trained word embeddings, each word
in vocabulary is associated with a high dimensional real-
valued vector which is learned from neural network model.
Vocabulary can be considered as points in vector space and
words which are similar in meaning are closer in vector
space. The representation can capture syntactic and semantic


## Page 5


relationships between words. To investigate the effect of pre-
trained word embedding, we used two existing pre-trained
word embedding models on Vietnamese (skip-gram [23] and
subwords [24]) and used them as additional information along
with word form embedding and POS tag embedding:
v′
i = g(W v.(wi ◦pi ◦extni) + bv)
(16)
C. Character-level word embedding
The main contribution of this study is using character-
level word embeddings as additional information of word
representation in the easy-ﬁrst algorithm and applied it on
VnDT. Unlike pre-trained word embeddings, character-level
word embeddings can deal with out-of-vocabulary (OOV)
problem because unknown words can be generated using their
component characters. As characters are shared across words,
character embedding combination still presents semantic in-
formation of words like pre-trained words embeddings.
We used the same network structure as in [13]. Character
embeddings of words is fed to the bidirectional LSTMs which
include two LSTMs called Forward and Backward. The input
of the forward network is the character embeddings of the
characters from the beginning to the end of the word while
inputs of the backward network is characters of the word in the
reverse order. The output of the two networks is concatenated
to one vector which represents information of words. Character
embeddings are learned jointly with the training process. The
ﬁgure 4 shows an example of using character embeddings for
representing a word.
t
h
ư
v
i
ệ
n
t
h
ư
v
i
ệ
n
Forward
Backward
∘
f ⃗  b⃗ 
b⃗ 
f ⃗ 
Figure 4.
The word "thư viện"is represented by character embedding with
BiLSTM
The hyper-parameters of the networks used for training
character embeddings are detailed in Table I.
Table I
HYPER-PARAMETERS USED FOR CHARACTER EMBEDDING NETWORKS
Char embedding dimension
100
BI-LSTM Layers
2
BI-LSTM Dimensions
100 + 100
IV. RESULTS AND DISCUSSION
In our experiments, we use the VnDT [15] which has 10,200
dependency structures. For comparison purposes, we split the
data in the same way as [18], last 1020 sentences for testing
(POS and automatic POS tagging) and the rest for training.
The POS tagging tool we used is VnTagger 1, its accuracy
is 94.4% on our test set. The performance is measured with
unlabeled attachment score (UAS) and labeled attachment
score (LAS).
We used two pre-trained word embeddings datasets which
were trained with two different models on Vietnamese: skip-
gram2 and subwords3. Information on these two datasets is
described in table II. Coverage column shows the percentage
of words in the VnDT treebank which appears in pre-trained
word embeddings.
Because of the difference between word tokenization meth-
ods, many words in VnDT do not exist in pre-trained word
embeddings, this is the reason for the low percentage of vocab-
ulary coverage of both datasets. If a word cannot be found in
pre-trained word embeddings, this word will be treated as an
unknown word and represented by the unknown vector. This
unknown vector do not carry much useful context information
of words that leads to poor performance in parsing.
Table II
INFORMATION OF TWO PRE-TRAINED WORD EMBEDDINGS
Model
Dim
Vocabulary
Coverage
Subword
300
200,000
20%
Skip-gram
300
100,000
67%
For fully exploration of pre-trained word embeddings and
character-level word embeddings, we design our experiments
as follows:
• Word embeddings + POS tag embeddings.
• Word embeddings + POS tag embeddings + Character
embeddings.
• Word embeddings + POS tag embeddings + Pre-trained
word embeddings.
• Word embeddings + POS tag embeddings + Character
embeddings + Pre-trained word embeddings.
We also compare the result of the easy-ﬁrst algorithm with
the current state-of-the-art parsers proposed by Kiperwasser
and Goldberg [12] which uses BiLSTM encoder to represent
words in the sentence, the word vector is used as features
in transition-based parser (BistT) and graph-based parser
(BistG) [11] 4. The implementation of Tree LSTM easy-ﬁrst is
provided at https://github.com/elikip/htparser. The results are
demonstrated in Table III. In the table, the results of BistT
and BistG are taken from [19] because this is reported as the
state-of-the-art parser on VnDT.
1https://github.com/scorpion1206/VnTagger
2https://github.com/pth1993/NNVLP
3https://github.com/facebookresearch/fastText
4https://github.com/elikip/bist-parser


## Page 6


Table III
VIETNAMESE DEPENDENCY PARSING RESULTS ON DIFFERENT PARSERS
Model
Gold POS Tag
Auto POS Tag
UAS%
LAS%
UAS%
LAS%
BistT
79.33
72.53
76.56
68.22
BistG
79.39
73.17
76.28
68.40
Easy-ﬁrst (Word + POS)
79.29
71.44
77.51
68.27
+ Char
80.58
72.95
78.01
68.82
+ Skip-gram
79.69
72.23
76.91
67.77
+ Char
80.91
72.98
78.26
69.04
+ Sub-word
79.50
71.94
77.16
67.96
+ Char
80.56
72.37
78.13
68.56
Using character-level word embeddings as additional in-
formation improve the accuracy of easy-ﬁrst parser (0.79%
UAS and 1.51% LAS). Replacing word embedding with
character-level word embedding shows slight increase in the
performance of the parser (0.39% UAS and 0.09% LAS).
These results show that using character-level word embeddings
can improve the accuracy of parsing.
Using both skip-gram and subword pre-trained word em-
beddings increase the accuracy of the parser. Despite that
the difference of vocabulary coverage between skip-gram and
subword is high (40%), the accuracy of the parser using skip-
gram is only higher than subword 0.16%. We found that in our
test data, the different of token coverage (percentage of token
in test data which appears in pre-trained word embeddings)
between two datasets is only 5% (75.39% for skip-gram and
70.95 % for subword).
Among all features we applied to Tree LSTM easy-ﬁrst
parser, the combination of word embedding + POS-tag embed-
ding + character-level word embedding + pre-trained word
embedding gives the best parse result (80.91% UAS and
72.98% LAS). Our model has outperformed the BistG parser
and obtained state-of-the-art performance on the VnDT.
V. CONCLUSION
We have demonstrated the effectiveness of pre-train word
embedding and character-level word embedding as features for
Vietnamese easy-ﬁrst dependency parsing.
In future work, we would like to train character-level word
embedding on larger corpora and use it as pre-trained features
like pre-trained word embeddings.
VI. ACKNOWLEDGEMENT
This research is funded by University of Information Tech-
nology - Vietnam National University Ho Chi Minh City under
grant number D1-2017-13.
REFERENCES
[1] Nivre, Joakim, et al. ”The CoNLL 2007 shared task on dependency pars-
ing.” Proceedings of the 2007 Joint Conference on Empirical Methods
in Natural Language Processing and Computational Natural Language
Learning (EMNLP-CoNLL). 2007.
[2] Seddah, Djam´e, Sandra K¨ubler, and Reut Tsarfaty. ”Introducing the
spmrl 2014 shared task on parsing morphologically-rich languages.”
Proceedings of the First Joint Workshop on Statistical Parsing of Mor-
phologically Rich Languages and Syntactic Analysis of Non-Canonical
Languages. 2014.
[3] Buchholz, Sabine, and Erwin Marsi. ”CoNLL-X shared task on multi-
lingual dependency parsing.” Proceedings of the Tenth Conference on
Computational Natural Language Learning. Association for Computa-
tional Linguistics, 2006.
[4] McDonald, Ryan, and Joakim Nivre. ”Characterizing the errors of data-
driven dependency parsing models.” Proceedings of the 2007 Joint
Conference on Empirical Methods in Natural Language Processing and
Computational Natural Language Learning (EMNLP-CoNLL). 2007.
[5] Chiu, Jason PC, and Eric Nichols. ”Named entity recognition with
bidirectional LSTM-CNNs.” arXiv preprint arXiv:1511.08308 (2015).
[6] Bahdanau, Dzmitry, Kyunghyun Cho, and Yoshua Bengio. ”Neural
machine translation by jointly learning to align and translate.” arXiv
preprint arXiv:1409.0473 (2014).
[7] Nivre, Joakim, Johan Hall, and Jens Nilsson. ”Maltparser: A data-driven
parser-generator for dependency parsing.” Proceedings of LREC. Vol. 6.
2006.
[8] Sutskever, Ilya, Oriol Vinyals, and Quoc V. Le. ”Sequence to sequence
learning with neural networks.” Advances in neural information process-
ing systems. 2014.
[9] Dyer, C., Ballesteros, M., Ling, W., Matthews, A., & Smith, N. A.
(2015). Transition-based dependency parsing with stack long short-term
memory. arXiv preprint arXiv:1505.08075.
[10] Ballesteros, M., Dyer, C., Goldberg, Y., & Smith, N. A. (2017). Greedy
transition-based dependency parsing with stack lstms. Computational
Linguistics, 43(2), 311-347.
[11] Kiperwasser, Eliyahu, and Yoav Goldberg. ”Easy-ﬁrst dependency pars-
ing with hierarchical tree LSTMs.” arXiv preprint arXiv:1603.00375
(2016).
[12] Kiperwasser, Eliyahu, and Yoav Goldberg. ”Simple and accurate depen-
dency parsing using bidirectional LSTM feature representations.” arXiv
preprint arXiv:1603.04351 (2016).
[13] Ballesteros, Miguel, Chris Dyer, and Noah A. Smith. ”Improved
transition-based parsing by modeling characters instead of words with
lstms.” arXiv preprint arXiv:1508.00657 (2015).
[14] Thi, Luong Nguyen, et al. ”Building a treebank for Vietnamese depen-
dency parsing.” Computing and Communication Technologies, Research,
Innovation, and Vision for the Future (RIVF), 2013 IEEE RIVF Inter-
national Conference on. IEEE, 2013.
[15] Nguyen, D. Q., Nguyen, D. Q., Pham, S. B., Nguyen, P. T., & Le
Nguyen, M. (2014, June). From treebank conversion to automatic
dependency parsing for Vietnamese. In International Conference on
Applications of Natural Language to Data Bases/Information Systems
(pp. 196-207). Springer, Cham.
[16] Nguyen, Kiet V., and Ngan Luu-Thuy Nguyen. ”Vietnamese transition-
based dependency parsing with supertag features.” Knowledge and
Systems Engineering (KSE), 2016 Eighth International Conference on.
IEEE, 2016. 175-180). IEEE.
[17] Vu-Manh, C., Luong, A. T., & Le-Hong, P. (2015, December). Im-
proving Vietnamese dependency parsing using distributed word rep-
resentations. In Proceedings of the Sixth International Symposium on
Information and Communication Technology (pp. 54-60). ACM.
[18] Nguyen, D. Q., Dras, M., & Johnson, M. (2016). An empirical study
for Vietnamese dependency parsing. Proceedings of the Australasian
Language Technology Association Workshop 2016, 143–149. Retrieved
from http://www.aclweb.org/anthology/U16-1017
[19] Goldberg, Yoav, and Michael Elhadad. ”An efﬁcient algorithm for easy-
ﬁrst non-directional dependency parsing.” Human Language Technolo-
gies: The 2010 Annual Conference of the North American Chapter of
the Association for Computational Linguistics. Association for Compu-
tational Linguistics, 2010.
[20] Ma, Ji, et al. ”Easy-ﬁrst pos tagging and dependency parsing with beam
search.” Proceedings of the 51st Annual Meeting of the Association for
Computational Linguistics (Volume 2: Short Papers). Vol. 2. 2013.
[21] Ballesteros, M., Dyer, C., & Smith, N. A. (2015). Improved transition-
based parsing by modeling characters instead of words with lstms. arXiv
preprint arXiv:1508.00657.
[22] Goldberg, Y., & Nivre, J. (2012). A dynamic oracle for arc-eager
dependency parsing. Proceedings of COLING 2012, 959-976.
[23] Mikolov, Tomas, et al. ”Distributed representations of words and phrases
and their compositionality.” Advances in neural information processing
systems. 2013.
[24] Bojanowski, Piotr, et al. ”Enriching word vectors with subword infor-
mation.” arXiv preprint arXiv:1607.04606 (2016).

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1910_13732_lstm_easy_first_dependency_parsing_with_pre_trained_word_embeddings_and_characte
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1910_13732_LSTM_EASY_FIRST_DEPENDENCY_PARSING_WITH_PRE_TRAINED_WORD_EMBEDDINGS_AND_CHARACTE.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

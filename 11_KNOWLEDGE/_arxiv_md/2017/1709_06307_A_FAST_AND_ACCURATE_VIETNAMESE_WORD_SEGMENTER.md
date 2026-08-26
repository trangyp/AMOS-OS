---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1709.06307
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1709.06307_A_Fast_and_Accurate_Vietnamese_Word_Segmenter

> Source: 1709.06307_A_Fast_and_Accurate_Vietnamese_Word_Segmenter.pdf

> Pages: 6

---


## Page 1


A Fast and Accurate Vietnamese Word Segmenter
Dat Quoc Nguyen1, Dai Quoc Nguyen2, Thanh Vu3, Mark Dras4, Mark Johnson4
1The University of Melbourne, Australia
dqnguyen@unimelb.edu.au
2Deakin University, Australia
dai.nguyen@deakin.edu.au
3Newcastle University, United Kingdom
thanh.vu@newcastle.ac.uk
4Macquarie University, Australia
{mark.dras, mark.johnson}@mq.edu.au
Abstract
We propose a novel approach to Vietnamese word segmentation. Our approach is based on the Single Classification
Ripple Down Rules methodology (Compton and Jansen, 1990), where rules are stored in an exception structure and
new rules are only added to correct segmentation errors given by existing rules. Experimental results on the benchmark
Vietnamese treebank show that our approach outperforms previous state-of-the-art approaches JVnSegmenter, vnTokenizer,
DongDu and UETsegmenter in terms of both accuracy and performance speed. Our code is open-source and available at:
https://github.com/datquocnguyen/RDRsegmenter.
Keywords: Vietnamese, Word segmentation, Single classification ripple down rules
1.
Introduction
Word segmentation is referred to as an important first
step for Vietnamese NLP tasks (Dien et al., 2001; Ha,
2003; Duc Cong et al., 2016). Unlike English, white
space is a weak indicator of word boundaries in Viet-
namese because when written, it is also used to sep-
arate syllables that constitute words. For example, a
written text “thuếthu nhập cá nhân” (individualcá_nhân
incomethu_nhập taxthuế) consisting of 5 syllables forms
a two-word phrase “thuế_thu_nhập cá_nhân.”1 More
specifically, about 85% of Vietnamese word types are
composed of at least two syllables and 80%+ of syl-
lable types are words by themselves (Thang et al.,
2008; Le et al., 2008), thus creating challenges in Viet-
namese word segmentation (Nguyen et al., 2012).
Many approaches are proposed for the Vietnamese
word segmentation task. Le et al. (2008), Pham et
al. (2009) and Tran et al. (2012) applied the maxi-
mum matching strategy (NanYuan and YanBin, 1991)
to generate all possible segmentations for each input
sentence; then to select the best segmentation, Le et
al. (2008) and Tran et al. (2012) used n-gram language
models while Pham et al. (2009) employed part-of-
speech (POS) information from an external POS tag-
ger. In addition, Nguyen et al. (2006), Dinh and Vu
1In the traditional underscore-based representation in
the Vietnamese word segmentation task (Nguyen et al.,
2009), white space is only used to separate words while un-
derscore is used to separate syllables inside a word.
(2006) and Tran et al. (2010) considered this segmen-
tation task as a sequence labeling task, using either a
linear-chain CRF, SVM or MaxEnt model to assign
each syllable a segmentation tag such as B (Begin
of a word) or I (Inside of a word). Another promis-
ing approach is joint word segmentation and POS
tagging (Takahashi and Yamamoto, 2016; Nguyen et
al., 2017b), which assigns a combined segmentation
and POS tag to each syllable. Furthermore, Luu and
Kazuhide (2012), Liu and Lin (2014) and Nguyen and
Le (2016) proposed methods based on pointwise pre-
diction (Neubig and Mori, 2010), where a binary clas-
sifier is trained to identify whether or not there is a
word boundary between two syllables.
In this paper, we propose a novel method to Viet-
namese word segmentation. Our method automatically
constructs a Single Classification Ripple Down Rules
(SCRDR) tree (Compton and Jansen, 1990) to correct
wrong segmentations given by a longest matching-
based word segmenter. On the benchmark Vietnamese
treebank (Nguyen et al., 2009), experimental results
show that our method obtains better accuracy and
performance speed than the previous state-of-the-art
methods JVnSegmenter (Nguyen et al., 2006), vnTok-
enizer (Le et al., 2008), DongDu (Luu and Kazuhide,
2012) and UETsegmenter (Nguyen and Le, 2016).
2.
SCRDR methodology
This section gives a brief introduction of the SCRDR
methodology (Compton and Jansen, 1988; Compton
arXiv:1709.06307v2  [cs.CL]  23 Dec 2017


## Page 2


Figure 1: An illustration of a SCRDR tree for POS tagging. This figure is adapted from Nguyen et al. (2016).
and Jansen, 1990; Richards, 2009). A SCRDR tree is
a binary tree with only two unique types of edges “ex-
cept” and “if-not”, where every node is associated with
a rule in a form of “if condition then conclusion.” To
ensure that the tree always produces a conclusion, the
rule at its root (default) node has a trivial condition
which is always satisfied.
Each case to be evaluated starts at the root node and
ripples down as follows: (i) If the case satisfies the
condition of a current node’s rule, the case is then
passed on to the current node’s “except” child if this
“except” child exists. (ii) Otherwise, if the case does
not satisfy the condition, it is then passed on to the cur-
rent node’s “if-not” child. So, the conclusion returned
by the tree is the conclusion of the last satisfied rule in
the evaluation path to a leaf node.
For example, Figure 1 illustrates a SCRDR tree
for POS tagging. Let us consider a concrete case
“as/IN
investors/NNS
anticipate/VB
a/DT
recov-
ery/NN” where “anticipate” and “VB” is the current
considered pair of word and its initial POS tag. Be-
cause this case satisfies the conditions of the rules at
nodes (0), (1) and (3), it is passed on to node (6) using
the “except” edge. The case does not satisfy the con-
dition of the rule at node (6), thus it is passed on to
node (7) using the “if-not” edge. Finally, the case does
not satisfy the condition of the rule at the leaf node
(7). So, the rule at node (3)—the last satisfied rule in
the the evaluation path (0)-(1)-(3)-(6)-(7)—concludes
“VBP” should be the POS tag of the word “anticipate”
instead of the initial POS tag “VB.”
To correct a wrong conclusion returned for a given
case, a new node containing a new exception rule may
be attached to the last node in the evaluation path. If
the last node’s rule is the last satisfied rule given the
case, the new node is added as its child with the “ex-
cept” edge; otherwise, the new node is attached with
the “if-not” edge.
SCRDR has been successfully applied in NLP tasks
for temporal relation extraction (Pham and Hoffmann,
2006), word lemmatization (Plisson et al., 2008), POS
Figure 2: Diagram of our approach.
tagging (Xu and Hoffmann, 2010; Nguyen et al.,
2011b; Nguyen et al., 2014; Nguyen et al., 2016),
named entity recognition (Nguyen and Pham, 2012)
and question answering (Nguyen et al., 2011a; Nguyen
et al., 2013; Nguyen et al., 2017a). The works by Plis-
son et al. (2008), Nguyen et al. (2011b), Nguyen et al.
(2014) and Nguyen et al. (2016) build the tree auto-
matically, while others manually construct the tree.
3.
Our approach
This section describes our new error-driven approach
to automatically construct a SCRDR tree to correct
wrong segmentations produced by an initial word seg-
menter.
Following Nguyen et al. (2006) and Tran et al. (2010),
we also formalize the word segmentation problem as
a sequence labeling task. In particular, each syllable is
labeled by either segmentation tag B (Begin of a word)
or I (Inside of a word). As a result, our approach can
be viewed as an extension to word segmentation of the
automatic SCRDR approach for POS tagging (Nguyen
et al., 2014; Nguyen et al., 2016). Our learning dia-
gram is described in Figure 2.


## Page 3


Tuple as key
Value
(“”, “”, “”, “”, thuế, B, thu, B, nhập, I)
B
√
(“”, “”, thuế, B, thu, B, nhập, I, cá, B)
I
X
(thuế, B, thu, B, nhập, I, cá, B, nhân, I)
I
√
(thu, B, nhập, I, cá, B, nhân, I, “”, “”)
B
√
(nhập, I, cá, B, nhân, I, “”, “”, “”, “”)
I
√
Table 1: Examples of key-value pairs in the 5-
syllable context dictionary D when comparing the BI-
formed gold standard corpus “thuế/B thu/I nhập/I cá/B
nhân/I” and the BI-formed initialized corpus “thuế/B
thu/B nhập/I cá/B nhân/I.” Here, “” denotes an empty
element in tuples. √and X represent the correct and
incorrect initial segmentations, respectively.
We
start
with
an
underscore-based
gold
stan-
dard training corpus consisting of manually word-
segmented sentences, e.g. “thuế_thu_nhập cá_nhân”
(individualcá_nhân incomethu_nhập taxthuế) and trans-
form this corpus into a BI-formed representation (e.g.
“thuế/B thu/I nhập/I cá/B nhân/I”). We then extract
syllables to construct the raw corpus (which does not
have B and I segmentation tags, and would look like
“thuếthu nhập cá nhân”).
We apply an initial segmenter on the input raw cor-
pus to get the output BI-formed initialized corpus.
For example, given the input raw text “thuếthu nhập
cá nhân”, the initial segmenter returns the output
BI-formed initialized text “thuế/B thu/B nhập/I cá/B
nhân/I.” The initial segmenter in our approach is based
on the longest matching strategy (Poowarawan, 1986),
using a Vietnamese lexicon from Le et al. (2008).
We then compare the BI-formed gold standard cor-
pus and the BI-formed initialized corpus to gener-
ate a 5-syllable context dictionary D where each
key-value pair consists of a 5-syllable window tu-
ple as key and a gold standard tag as value. Here,
each tuple captures a 5-syllable window context of
a current syllable and its initial segmentation tag
B/I in a format of (Previous-2nd-syllable, Previous-
2nd-tag, Previous-1st-syllable, Previous-1st-tag, syl-
lable, tag, Next-1st-syllable, Next-1st-tag, Next-2nd-
syllable, Next-2nd-tag) from the initialized corpus,2
while the gold standard tag is the corresponding seg-
mentation tag of the current syllable in the gold stan-
dard corpus. So, a wrong segmentation is when the
initial segmentation tag is different from the gold stan-
dard tag, as shown in the second row in Table 1.
Based on the 5-syllable context dictionary D, the rule
selector selects the most suitable rules to construct the
2Syllables in each tuple are all converted into a lower-
case form.
syllable
s-2, s-1, s0, s+1, s+2
(s-2, s0), (s-1, s0), (s-1, s+1), (s0, s+1)
(s0, s+2)
(s-2, s-1, s0), (s-1, s0, s+1), (s0, s+1, s+2)
tag
t-2, t-1, t0, t+1, t+2
(t-2, t-1), (t-1, t+1), (t+1, t+2)
syllable & tag
(t-1, s0), (s0, t+1), (t-1, s0, t+1), (t-2, t-1, s0)
(s0, t+1, t+2)
Table 2: Short descriptions of our rule templates.
“s” refers to syllable and “t” refers to B/I segmen-
tation label while subscripts -2, -1, 0, 1, 2 denote
indices. For example, (s-1, s+1) represents the rule
template “IF Previous-1st-syllable == tuple.Previous-
1st-syllable && Next-1st-syllable == tuple.Next-1st-
syllable THEN tag = gold-standard-tag”, where el-
ements in bold are replaced by concrete values from
tuple and gold tag pairs in the 5-syllable context dic-
tionary D. Given (s-1, s+1) and the second row in Table
1, we have a concrete rule “IF Previous-1st-syllable ==
thuế&& Next-1st-syllable == nhập THEN tag = I.”
Figure 3: SCRDR tree initialization.
SCRDR tree. Concrete rules are generated based on
rule templates. Table 2 presents short descriptions of
the rule templates. The SCRDR tree is initialized with
a default rule—the rule at the root node—and its two
exception rules, as shown in Figure 3. Our learning
process to automatically add new exception rules to
the SCRDR tree is as follows:
• Let us consider a node N in the tree. We define
a subset TN of the context dictionary D such that
the rule at N is the last satisfied rule in the eval-
uation path for every tuple in TN but N returns
a wrong segmentation tag. For example, given
node (2) in Figure 3 and D in Table 1, T(2) would
contain a pair of the tuple (“”, “”, thuế, B, thu, B,
nhập, I cá, B) and gold segmentation tag I from
the second row in Table 1. A new node containing
a new exception rule must be added to the current
tree to correct the errors given by N.3
• The new exception rule is selected from all con-
3See the second last paragraph in Section 2. for how to
attach a new node to an existing SCRDR tree.


## Page 4


crete rules, in which these concrete rules are gen-
erated by applying the rule templates to all tuples
in TN. The selected rule must satisfy following
constraints: (1) If N is not one of the first three
nodes in Figure 3, then the selected rule’s condi-
tion must not be satisfied by every tuple for which
N already returns a correct segmentation tag. (2)
The selected rule is associated with the highest
value of the subtraction a −b. Here a is the num-
ber of tuples in TN in which each tuple not only
satisfies the rule’s condition but also gets a cor-
rect segmentation tag given by the rule’s conclu-
sion, while b is the number of tuples in TN in
which each tuple also satisfies the rule’s condi-
tion but gets a wrong segmentation tag given by
the rule’s conclusion. (3) The value a−b must be
not smaller than a given threshold.
• This process is repeated until at any node it can-
not select a new exception rule satisfying con-
straints above.
With the learned SCRDR tree, we perform word seg-
mentation on unsegmented text as follows: The initial
segmenter takes the input unsegmented text to gener-
ate a BI-formed initialized text. Next, by sliding a 5-
syllable window from left to right, a tuple is generated
for each syllable in the initialized text; then the learned
SCRDR tree takes the input tuple to return a final seg-
mentation tag to the corresponding syllable. Finally,
the output of this labeling process is converted to the
traditional underscore-based representation.
4.
Experiments
4.1.
Experimental setup
Following Nguyen and Le (2016), we conduct ex-
periments and compare the performance of our
approach—which we call RDRsegmenter—with pub-
lished results of other state-of-the-art approaches on
the benchmark Vietnamese treebank (Nguyen et al.,
2009). The training set consists of 75k manually
word-segmented sentences (about 23 words per sen-
tence in average).4 The test set consists of 2120 sen-
tences (about 31 words per sentence) in 10 files from
800001.seg to 800010.seg.5 We use F1 score as the
main evaluation metric to measure the performance of
word segmentation.
Note that to determine the threshold in our RDRseg-
menter, we sampled a development set of 5k sentences
4The data, officially released in 2013, is provided for re-
search or educational purpose by the national project VLSP
on Vietnamese language and speech processing.
5The test set was originally released for evaluation in the
POS tagging shared task at the VLSP 2013 workshop.
Approach
Precision
Recall
F1
vnTokenizer
96.98
97.69
97.33
JVnSegmenter-Maxent
96.60
97.40
97.00
JVnSegmenter-CRFs
96.63
97.49
97.06
DongDu
96.35
97.46
96.90
UETsegmenter
97.51
98.23
97.87
Our RDRsegmenter
97.46
98.35
97.90
Table 3: Vietnamese word segmentation results (in
%). The results of vnTokenizer, JVnSegmenter and
DongDu are reported in Nguyen and Le (2016).
97.4
97.6
97.8
9.5k
19k
37.5k
75k
training size
F1
Approach
RDRsegmenter
UETsegmenter
Figure 4: F1 scores (in %) when varying the training
size at 9.5k, 19k, 37.5k and full 75k sentences.
from the full training set and used the remaining 70k
sentences for training. We found an optimal threshold
value at 2 producing the highest F1 score on the devel-
opment set. Then we learned a SCRDR tree from the
full training set with the optimal threshold, resulting
in 1447 rules in total.
4.2.
Main results
Table 3 compares the Vietnamese word segmentation
results of our RDRsegmenter with results reported in
prior work, using the same experimental setup.
Table 3 shows that RDRsegmenter obtains the high-
est F1 score. In particular, RDRSegmenter obtains
0.5+% higher F1 than vnTokenizer (Le et al., 2008)
though both approaches use the same lexicon for ini-
tial segmentation. In terms of a sequence labeling task,
RDRSegmenter outperforms JVnSegmenter (Nguyen
et al., 2006) with 0.8+% improvement. Compared with
the pointwise prediction approaches DongDu (Luu
and Kazuhide, 2012) and UETsegmenter (Nguyen
and Le, 2016), RDRsegmenter does significantly bet-


## Page 5


ter than DongDu and somewhat better than UETseg-
menter. In Figure 4, we show F1 scores of RDRseg-
menter and UETsegmenter at different training sizes,
showing that RDRsegmenter clearly improves perfor-
mance in a smaller dataset scenario.
It is worth noting that on a personal computer of In-
tel Core i7 2.2 GHz, our RDRsegmenter processes
at a speed of 62k words per second in a single
threaded implementation, which is 1.3 times faster
than UETsegmenter.6 In addition, Nguyen and Le
(2016) showed that UETsegmenter is faster than vn-
Tokenizer, JVnSegmenter and DongDu.7 So RDRseg-
menter is also faster than vnTokenizer, JVnSegmenter
and DongDu.
5.
Conclusion
In this paper, we have proposed a new error-driven
method to automatically construct a Single Classifi-
cation Ripple Down Rules tree for Vietnamese word
segmentation. Experiments on the benchmark Viet-
namese treebank show that our method obtains bet-
ter accuracy and speed than previous approaches.
Our code is available at: https://github.com/
datquocnguyen/RDRsegmenter.
Note that excluding the language-specific initial seg-
menter, our method generally can be viewed as a lan-
guage independent approach. Here, a Vietnamese syl-
lable is analogous to a character in other languages
such as Chinese and Japanese. So we will adapt our
method to those languages in future work.
Acknowledgments
This research was partially supported by the Aus-
tralian Government through the Australian Research
Council’s Discovery Projects funding scheme (project
DP160102156). This research was also partially sup-
ported by NICTA, funded by the Australian Govern-
ment through the Department of Communications and
the Australian Research Council through the ICT Cen-
tre of Excellence Program. This research was done
while the first author was at Macquarie University.
6We repeated the segmentation process on the test set
100 times, and then computed the averaged speed. Note that
model loading time was not taken into account, in which
RDRsegmenter took 50 miniseconds while UETsegmenter
took 10 seconds.
7Evaluated on a computer of Intel Core i5-3337U
1.80GHz, Nguyen and Le (2016) showed that JVnSeg-
menter, vnTokenizer, DongDu and UETsegmenter obtained
performance speeds at 1k, 5k, 17k and 33k words per sec-
ond, respectively. All of them are implemented in Java ex-
cept DongDu which is in C++. Our RDRsegmenter is also
implemented in Java.
References
Compton, P. and Jansen, B. (1988). Knowledge in
Context: A Strategy for Expert System Mainte-
nance. In Proceedings of the 2nd Australian Joint
Artificial Intelligence Conference, pages 292–306.
Compton, P. and Jansen, R. (1990). A Philosophical
Basis for Knowledge Acquisition. Knowledge Aqui-
sition, 2(3):241–257.
Dien, D., Kiem, H., and Toan, N. V. (2001). Viet-
namese Word Segmentation.
In Proceedings of
the Sixth Natural Language Processing Pacific Rim
Symposium, pages 749–756.
Dinh, D. and Vu, T. (2006). A Maximum Entropy
Approach for Vietnamese Word Segmentation. In
Proceedings of the 2006 International Conference
on Research, Innovation and Vision for the Future,
pages 248–253.
Duc Cong, S. N., Hung Ngo, Q., and Jiamthapthaksin,
R. (2016). State-of-the-art Vietnamese word seg-
mentation. In Proceedings of the 2nd International
Conference on Science in Information Technology,
pages 119–124.
Ha, L. A. (2003). A method for word segmentation in
Vietnamese. In Proceedings of Corpus Linguistics.
Le, H. P., Nguyen, T. M. H., Roussanaly, A., and Ho,
T. V. (2008). A hybrid approach to word segmen-
tation of Vietnamese texts. In Proceedings of the
2nd International Conference on Language and Au-
tomata Theory and Applications, pages 240–249.
Liu, W. and Lin, L. (2014). Probabilistic Ensemble
Learning for Vietnamese Word Segmentation. In
Proceedings of the 37th International ACM SIGIR
Conference on Research & Development in Infor-
mation Retrieval, pages 931–934.
Luu, T. A. and Kazuhide, Y. (2012).
Ứng dụng
phương pháp Pointwise vào bài toán tách từcho
tiếng Việt. https://github.com/rockkhuya/DongDu.
NanYuan, L. and YanBin, Z. (1991). A Chinese word
segmentation model and a Chinese word segmen-
tation system PC-CWSS. Journal of Chinese Lan-
guage and Computing, 1(1).
Neubig, G. and Mori, S. (2010). Word-based Par-
tial Annotation for Efficient Corpus Construction.
In Proceedings of the Seventh International Confer-
ence on Language Resources and Evaluation, pages
2723–2727.
Nguyen, T.-P. and Le, A.-C. (2016). A Hybrid Ap-
proach to Vietnamese Word Segmentation. In Pro-
ceedings of the 2016 IEEE RIVF International Con-
ference on Computing and Communication Tech-
nologies: Research, Innovation, and Vision for the
Future, pages 114–119.


## Page 6


Nguyen, D. B. and Pham, S. B.
(2012).
Ripple
Down Rules for Vietnamese Named Entity Recog-
nition. In Proceedings of the 4th international con-
ference on Computational Collective Intelligence:
Technologies and Applications - Volume Part I,
pages 354–363.
Nguyen, C.-T., Nguyen, T.-K., Phan, X.-H., Nguyen,
L.-M., and Ha, Q.-T. (2006). Vietnamese Word
Segmentation with CRFs and SVMs: An Investiga-
tion. In Proceedings of the 20th Pacific Asia Con-
ference on Language, Information and Computa-
tion, pages 215–222.
Nguyen, P. T., Vu, X. L., Nguyen, T. M. H., Nguyen,
V. H., and Le, H. P. (2009). Building a Large
Syntactically-Annotated Corpus of Vietnamese. In
Proceedings of the Third Linguistic Annotation
Workshop, pages 182–185.
Nguyen, D. Q., Nguyen, D. Q., and Pham, S. B.
(2011a).
Systematic Knowledge Acquisition for
Question Analysis. In Proceedings of the 8th Inter-
national Conference on Recent Advances in Natural
Language Processing, pages 406–412.
Nguyen, D. Q., Nguyen, D. Q., Pham, S. B., and Pham,
D. D. (2011b). Ripple Down Rules for Part-of-
Speech Tagging. In Proceedings of the 12th In-
ternational Conference on Intelligent Text Process-
ing and Computational Linguistics - Volume Part I,
pages 190–201.
Nguyen, Q. T., Nguyen, N. L., and Miyao, Y. (2012).
Comparing Different Criteria for Vietnamese Word
Segmentation. In Proceedings of the 3rd Workshop
on South and Southeast Asian Natural Language
Processing, pages 53–68.
Nguyen, D. Q., Nguyen, D. Q., and Pham, S. B.
(2013). KbQAS: A Knowledge-based QA System.
In Proceedings of the 12th International Semantic
Web Conference (Posters & Demonstrations Track),
pages 109–112.
Nguyen, D. Q., Nguyen, D. Q., Pham, D. D., and
Pham, S. B. (2014). RDRPOSTagger: A Ripple
Down Rules-based Part-Of-Speech Tagger. In Pro-
ceedings of the Demonstrations at the 14th Confer-
ence of the European Chapter of the Association for
Computational Linguistics, pages 17–20.
Nguyen, D. Q., Nguyen, D. Q., Pham, D. D., and
Pham, S. B. (2016). A Robust Transformation-
Based Learning Approach Using Ripple Down
Rules for Part-of-Speech Tagging. AI Communica-
tions, 29(3):409–422.
Nguyen, D. Q., Nguyen, D. Q., and Pham, S. B.
(2017a). Ripple Down Rules for Question Answer-
ing. Semantic Web, 8(4):511–532.
Nguyen, D. Q., Vu, T., Nguyen, D. Q., Dras, M., and
Johnson, M. (2017b). From Word Segmentation
to POS Tagging for Vietnamese. In Proceedings of
the Australasian Language Technology Association
Workshop 2017, pages 108–113.
Pham, S. B. and Hoffmann, A. (2006). Efficient
Knowledge Acquisition for Extracting Temporal Re-
lations. In Proceedings of the 17th European Con-
ference on Artificial Intelligence, pages 521–525.
Pham, D. D., Tran, G. B., and Pham, S. B. (2009). A
Hybrid Approach to Vietnamese Word Segmenta-
tion using Part of Speech tags. In Proceedings of the
2009 International Conference on Knowledge and
Systems Engineering, pages 154–161.
Plisson, J., Lavraˇc, N., Mladeni´c, D., and Erjavec,
T. (2008). Ripple Down Rule Learning for Auto-
mated Word Lemmatisation. AI Communications,
21(1):15–26.
Poowarawan, Y. (1986). Dictionary-based Thai Syl-
lable Separation. In Proceedings of the Ninth Elec-
tronics Engineering Conference, pages 409–418.
Richards, D. (2009). Two Decades of Ripple Down
Rules Research. Knowledge Engineering Review,
24(2):159–184.
Takahashi, K. and Yamamoto, K. (2016). Fundamen-
tal tools and resource are available for Vietnamese
analysis. In Proceedings of the 2016 International
Conference on Asian Language Processing, pages
246–249.
Thang, D. Q., Phuong, L. H., Huyen, N. T. M., Tu,
N. C., Rossignol, M., and Luong, V. X. (2008).
Word segmentation of Vietnamese texts : a compar-
ison of approaches. In Proceedings of the 6th In-
ternational Conference on Language Resources and
Evaluation, pages 1933–1936.
Tran, T. O., Le, A. C., and Ha, Q. T. (2010). Improv-
ing Vietnamese Word Segmentation and POS Tag-
ging using MEM with Various Kinds of Resources.
Journal of Natural Language Processing, 17(3):41–
60.
Tran, N. A., Dao, T. T., and Nguyen, P. T. (2012).
An effective context-based method for Vietnamese-
word segmentation. In Proceedings of the 1st In-
ternational Workshop on Vietnamese Language and
Speech Processing, pages 34–40.
Xu, H. and Hoffmann, A. (2010). RDRCE: Com-
bining Machine Learning and Knowledge Acquisi-
tion. In Proceedings of the 11th International Work-
shop on Knowledge Management and Acquisition
for Smart Systems and Services, pages 165–179.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1801.09030v2
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1801.09030v2_Exploration_on_Generating_Traditional_Chinese_Medicine_Prescription_from_Symptom

> Source: 1801.09030v2_Exploration_on_Generating_Traditional_Chinese_Medicine_Prescription_from_Symptom.pdf

> Pages: 9

---


## Page 1


arXiv:1801.09030v2  [cs.CL]  21 May 2018
Exploration on Generating Traditional Chinese Medicine Prescriptions
from Symptoms with an End-to-End Approach
Wei Li, Xu Sun
MOE Key Laboratory of Computational Linguistics,
School of Electronics Engineering and Computer
Science, Peking University
liweitj47,xusun@pku.edu.cn
Zheng Yang
Beijing University
of Chinese Medicine
yangzheng@bucm.edu.cn
Abstract
Traditional Chinese Medicine (TCM) is an
inﬂuential form of medical treatment in
China and surrounding areas.
In this pa-
per, we propose a TCM prescription gener-
ation task that aims to automatically gener-
ate a herbal medicine prescription based on
textual symptom descriptions.
Sequence-to-
sequence (seq2seq) model has been success-
ful in dealing with sequence generation tasks.
We explore a potential end-to-end solution to
the TCM prescription generation task using
seq2seq models. However, experiments show
that directly applying seq2seq model leads to
unfruitful results due to the repetition problem.
To solve the problem, we propose a novel de-
coder with coverage mechanism and a novel
soft loss function. The experimental results
demonstrate the effectiveness of the proposed
approach. Judged by professors who excel in
TCM, the generated prescriptions are rated 7.3
out of 10. It shows that the model can indeed
help with the prescribing procedure in real life.
1
Introduction
Traditional Chinese Medicine (TCM) is one of
the most important forms of medical treatment in
China and the surrounding areas. TCM has ac-
cumulated large quantities of documentation and
therapy records in the long history of develop-
ment. Prescriptions consisting of herbal medica-
tion are the most important form of TCM treat-
ment. TCM practitioners prescribe according to
a patient’s symptoms that are observed and an-
alyzed by the practitioners themselves instead of
using medical equipment, e.g., the CT. The patient
takes the decoction made out of the herbal medi-
cation in the prescription. A complete prescription
includes the composition of herbs, the proportion
of herbs, the preparation method and the doses of
the decoction. In this work, we focus on the com-
position part of the prescription, which is the most
essential part of the prescription.
During the long history of TCM, there has been
a number of therapy records or treatment guide-
lines in the TCM classics composed by outstand-
ing TCM researchers and practitioners.
In real
life, TCM practitioners often take these classical
records for reference when prescribing for the pa-
tient, which inspires us to design a model that can
automatically generate prescriptions by learning
from these classics. It also needs to be noted that
due to the issues in actual practice, the objective of
this work is to generate candidate prescriptions to
facilitate the prescribing procedure instead of sub-
stituting the human practitioners completely.
An example of TCM prescription is shown in
Table 1. The herbs in the prescription are orga-
nized in a weak order. By “weak order”, we mean
that the effect of the herbs are not inﬂuenced by the
order. However, the order of the herbs reﬂects the
way of thinking when constructing the prescrip-
tion. Therefore, the herbs are connected to each
other, and the most important ones are usually
listed ﬁrst. Due to the lack of digitalization and
Name
麻黄汤(Mahuang decoction)
Symptoms
外感风寒表实证。恶寒发热，头身
疼痛，无汗自喘，舌苔薄白，脉浮
紧。
Translation
Affection
of
exogenous
wind-cold;
aversion to cold, fever; headache and
body pain; adiapneustia and pant; thin
and white tongue coating, ﬂoating and
tense pulse
Prescription
麻黄、桂枝、杏仁、甘草
Translation
Mahuang
(ephedra),
Guizhi
(cassia
twig), Xingren (almond), Gancao (gly-
cyrrhiza)
Table 1: An example of a TCM symptom-prescription
pair. As we are mainly concerned with the composition
of the prescription, we only provide the herbs in the
prescription.


## Page 2


formalization, TCM has not attracted sufﬁcient at-
tention in the artiﬁcial intelligence community. To
facilitate the studies on automatic TCM prescrip-
tion generation, we collect and clean a large num-
ber of prescriptions as well as their corresponding
symptom descriptions from the Internet.
Inspired by the great success of natural lan-
guage generation tasks like neural machine trans-
lation (NMT) (Bahdanau et al., 2014; Cho et al.,
2014; Sutskever et al., 2014), abstractive summa-
rization (See et al., 2017), generative question an-
swering (Yin et al., 2015), and neural dialogue re-
sponse generation (Li et al., 2017, 2016), we pro-
pose to adopt the end-to-end paradigm, mainly the
sequence to sequence model, to tackle the task
of generating TCM prescriptions based on textual
symptom descriptions.
The sequence to sequence model (seq2seq) con-
sists of an encoder that encodes the input sequence
and a decoder that generates the output sequence.
The success in the language generation tasks indi-
cates that the seq2seq model can learn the seman-
tic relation between the output sequence and the
input sequence quite well. It is also a desirable
characteristic for generating prescriptions accord-
ing to the textual symptom description.
The prescription generation task is similar to the
generative question answering (QA). In such task
settings, the encoder part of the model takes in the
question, and encodes the sequence of tokens into
a set of hidden states, which embody the informa-
tion of the question. The decoder part then iter-
atively generates tokens based on the information
encoded in the hidden states of the encoder. The
model would learn how to generate response af-
ter training on the corresponding question-answer
pairs.
In the TCM prescription generation task, the
textual symptom descriptions can be seen as the
question and the aim of the task is to produce a set
of TCM herbs that form a prescription as the an-
swer to the question. However, the set of herbs
is different from the textual answers to a ques-
tion in the QA task.
A difference that is most
evident is that there will not be any duplication
of herbs in the prescription. However, the basic
seq2seq model sometimes produces the same herb
tokens repeatedly when applied to the TCM pre-
scription generation task. This phenomenon can
hurt the performance of recall rate even after ap-
plying a post-process to eliminate repetitions. Be-
cause in a limited length of the prescription , the
model would produce the same token over and
over again, rather than real and novel ones. Fur-
thermore, the basic seq2seq assumes a strict or-
der between generated tokens, but in reality, we
should not severely punish the model when it pre-
dicts the correct tokens in the wrong order.
In this paper, we explore to automatically gen-
erate TCM prescriptions based on textual symp-
toms. We propose a soft seq2seq model with cov-
erage mechanism and a novel soft loss function.
The coverage mechanism is designed to make the
model aware of the herbs that have already been
generated while the soft loss function is to relieve
the side effect of strict order assumption. In the ex-
periment results, our proposed model beats all the
baselines in professional evaluations, and we ob-
serve a large increase in both the recall rate and the
F1 score compared with the basic seq2seq model.
The main contributions of this paper lie in the
following three folds:
• We propose a TCM prescription generation
task and collect a large quantity of TCM
prescription data including symptom descrip-
tions. It is the ﬁrst time that this task has been
considered to our knowledge.
• We propose to apply an end-to-end method
to deal with the TCM prescription generation
problem. In the experiments, we observe that
directly applying seq2seq model would result
in low recall rate because of the repetition
problem.
• We propose to enhance the basic seq2seq
model with cover mechanism and soft loss
function to guide the model to generate more
fruitful results. In our experiments, the pro-
fessional human evaluation score reaches 7.3
(out of 10), which shows that our model can
indeed help the TCM practitioners to pre-
scribe in real life. Our ﬁnal model also in-
creases the F1 score and the recall rate in
automatic evaluation by a substantial margin
compared with the basic seq2seq model.
2
Related Work
There has not been much work concerning com-
putational TCM. Zhou et al. (2010) attempted to
build a TCM clinical data warehouse so that the
TCM knowledge can be analyzed and used. This


## Page 3


is a typical way of collecting data, since the num-
ber of prescriptions given by the practitioners in
the clinics is very large. However, in reality, most
of the TCM doctors do not refer to the constructed
digital systems, because the quality of the input
data tends to be poor. Therefore, we choose pre-
scriptions in the classics (books or documentation)
of TCM. Although the available data can be fewer
than the clinical data, it guarantees the quality of
the prescriptions.
Wang et al. (2004) attempted to construct a self-
learning expert system with several simple clas-
siﬁers to facilitate the TCM diagnosis proce-
dure, Wang (2013) proposed to use shallow neu-
ral networks and CRF based multi-labeling learn-
ing methods to model TCM inquiry process, but
they only considered the disease of chronic gastri-
tis and its taxonomy is very simple. These meth-
ods either utilize traditional data mining methods
or are highly involved with expert crafted systems.
Zhang (2011); Zhipeng et al. (2017) proposed to
use LDA to model the herbs. Li and Yang (2017)
proposed to learn the distributed embedding for
TCM herbs with recurrent neural networks.
3
Methodology
Neural sequence to sequence model has proven to
be very effective in a wide range of natural lan-
guage generation tasks, including neural machine
translation and abstractive text summarization. In
this section, we ﬁrst describe the deﬁnition of the
TCM prescription generation task. Then, we in-
troduce how to apply seq2seq model in the pre-
scription composition task. Next, we show how
to guide the model to generate more fruitful herbs
in the setting of this task by introducing coverage
mechanism. Finally, we introduce our novel soft
loss function that relieves the strict assumption of
order between tokens. An overview of the our ﬁnal
model is shown in Figure 1.
3.1
Task Deﬁnition
Given a TCM herbal treatment dataset that con-
sists of N data samples, the i-th data sample
(x(i), p(i)) contains one piece of source text x(i)
that describes the symptoms, and Mi TCM herbs
(pi
1, pi
2, ..., pi
Mi) that make up the herb prescription
p(i).
We view the symptoms as a sequence of charac-
ters x(i) = (x(i)
1 , x(i)
2 , ..., x(i)
T ). We do not segment
the characters into words because they are mostly
in traditional Chinese that uses characters as basic
semantic units. The herbs pi
1, pi
2, ..., pi
Mi are all
different from each other.
3.2
Basic Encoder-Decoder Model
Sequence-to-sequence model was ﬁrst proposed to
solve the machine translation problem. The model
consists of two parts, an encoder and a decoder.
The encoder is bound to take in the source se-
quence and compress the sequence into a series
of hidden states. The decoder is used to generate
a sequence of target tokens based on the informa-
tion embodied in the hidden states given by the
encoder. Typically, both the encoder and the de-
coder are implemented with recurrent neural net-
works (RNN).
In our TCM prescription generation task, the
encoder RNN converts the variable-length symp-
toms in character sequence x = (x1, x2, ..., xT )
into a set of hidden representations
h
=
(h1, h2, ..., hT ), by iterating the following equa-
tions along time t:
ht = f(xt, ht−1)
(1)
where f is a RNN family function. In our imple-
mentation, we choose gated recurrent unit (GRU
(Cho et al., 2014)) as f, as the gating mechanism
is expected to model long distance dependency
better. Furthermore, we choose the bidirectional
version of recurrent neural networks as the en-
coder to solve the problem that the later words get
more emphasis in the unidirectional version. We
concatenate both the ht in the forward and back-
ward pass and get bht as the ﬁnal representation of
the hidden state at time step t.
We get the context vector c representing the
whole source x at the t-th time through a non-
linear function q, normally known as the attention
mechanism:
ct =
T
X
j=1
αtjhj
(2)
αtj =
exp (a (st−1, hj))
PT
k=1 exp (a (st−1, hk))
(3)
The context vector ct is calculated as a weighted
sum of hidden representation produced by the en-
coder h = (h1, ..., hT ).
a(st−1, hj) is a soft
alignment function that measures the relevance be-
tween st−1 and hj. It computes how much hj is
needed for the t-th output word based on the pre-
vious hidden state of the decoder st−1.
The decoder is another RNN. It generates a


## Page 4


context 
vector
Encoder
hidden 
states
character 
embeddings
Decoder
coverage 
vector
tokens to 
be 
predicted
hidden 
states
Figure 1: An illustration of our model. The model is built on the basis of seq2seq model with attention mechanism.
We use a coverage mechanism to reduce repetition problem. The coverage mechanism is realized by adding a
coverage vector to the decoder.
variable-length sequence y = (y1, y2, ..., yT ′) to-
ken by token (herb), through a conditional lan-
guage model:
st = f(st−1, ct, Eyt−1)
(4)
p(yt|y1,...,t, x) = g(st)
(5)
where st is the hidden state of the decoder RNN at
time step t. f is also a gated recurrent unit. The
non-linear function g is a softmax layer, which
outputs the probabilities of all the herbs in the herb
vocabulary. E ∈(V × d) is the embedding ma-
trix of the target tokens, V is the number of herb
vocabulary, d is the embedding dimension. yt−1 is
the last predicted token.
In the decoder, the context vector ct is calcu-
lated based on the hidden state st−1 of the decoder
at time step t −1 and all the hidden states in the
encoder. The procedure is known as the attention
mechanism. The attention mechanism is expected
to supplement the information from the source se-
quence that is more connected to the current hid-
den state of the decoder instead of only depending
on a ﬁxed vector produced by the encoder.
The encoder and decoder networks are trained
jointly to maximize the conditional probability of
the target sequence. A soft version of cross en-
tropy loss is applied to maximize the conditional
probability, which we will describe in detail.
3.3
Coverage Mechanism
Different from natural language generation tasks,
there is no duplicate herb in the TCM prescription
generation task. When directly applying seq2seq
model in this task, the decoder tends to gener-
ate some frequently observed herbs over and over
again. Although we can prune the repeated herbs
through post processing by eliminating the re-
peated ones, it still hurts the recall performance
as the maximum length of a prescription is lim-
ited.
This situation is still true when we use a
< EOS > label to indicate where the generation
should stop.
To encourage the decoder to generate more di-
verse and reasonable herb tokens, we propose to
apply coverage mechanism to make the model
aware of the already generated herbs. Coverage
mechanism (Tu et al., 2016b,a; Mi et al., 2016)
was ﬁrst proposed to help the decoder focus on
the part that has not been paid much attention by
feeding a fertility vector to the attention calcula-
tion, indicating how much information of the input
is used.
In our model, we do not use the fertility vec-
tor to tune the attention weights. The reason is
that the symptoms are related to others and alto-
gether describe the whole disease, which is ex-
plained in Section 1. Still, inspired by its moti-
vation, we adapt the coverage mechanism to the
decoder where a coverage vector is fed to the GRU
cell together with the context vector. Equation 4 is
then replaced by the following ones.
at = tanh(WDt + b)
(6)
st = f(st−1, ct, Eyt−1, at)
(7)
where at is the coverage vector at the t-th time
step in decoding. Dt is the one-hot representa-
tion of the generated tokens until the t-th time
step. W ∈RV ×H is a learnable parameter ma-
trix, where V is the size of the herb vocabulary and
H is the size of the hidden state. By feeding the
coverage vector, which is also a sketch of the gen-
erated herbs, to the GRU as part of the input, our
model can softly switch more probability to the
herbs that have not been predicted. This way, the


## Page 5


model is encouraged to produce novel herbs rather
than repeatedly predicting the frequently observed
ones, thus increasing the recall rate.
3.4
Soft Loss Function
We argue that even though the order of the
herbs matters when generating the prescription
(Vinyals et al., 2015; Nam et al., 2017), we should
not strictly restrict the order. However, the tradi-
tional cross entropy loss function applied to the ba-
sic seq2seq model puts a strict assumption on the
order of the labels. To deal with the task of pre-
dicting weakly ordered labels (or even unordered
labels), we propose a soft loss function instead of
the original hard cross entropy loss function:
loss = −
X
t
q′
t log(pt)
(8)
Instead of using the original hard one-hot target
probability qt, we use a soft target probability dis-
tribution q′
t, which is calculated according to qt
and the target sequence q of this sample. Let qv
denote the bag of words representation of q, where
only slots of the target herbs in q are ﬁlled with 1s.
We use a function ξ to project the original target
label probability qt into a new probability distri-
bution q′
t.
q′
t = ξ(qt, qv)
(9)
This function ξ is designed so as to decrease the
harsh punishment when the model predicts the la-
bels in the wrong order.
In this paper, we ap-
ply a simple yet effective projection function as
Equation 10. This is an example implementation,
and one can design more sophisticated projection
functions if needed.
ξ(yt, s) = ((qv/M) + yt)/2
(10)
where M is the length of q. This function means
that at the t-th time of decoding, for each target
herb token pi, we ﬁrst split a probability density of
1.0 equally across all the l herbs into 1/M. Then,
we take the average of this probability distribution
and the original probability qt to be the ﬁnal prob-
ability distribution at time t.
4
Experiment
4.1
Dataset Construction
We crawl the data from TCM Prescription Knowl-
edge Base (中医方剂知识库) 1. This knowledge
base includes comprehensive TCM documentation
in the history. The database includes 710 TCM
1http://www.hhjfsl.com/fang/
historic books or documents as well as some mod-
ern ones, consisting of 85,166 prescriptions in to-
tal. Each item in the database provides the name,
the origin, the composition, the effect, the con-
traindications, and the preparation method.
We
clean and formalize the database and get 82,044
usable symptom-prescription pairs
In the process of formalization, we temporar-
ily omit the dose information and the preparation
method description, as we are mainly concerned
with the composition. Because the names of the
herbs have evolved a lot, we conclude heuristic
rules as well as speciﬁc projection rules to project
some rarely seen herbs to their similar forms that
are normally referred to. There are also prescrip-
tions that refer to the name of other prescriptions.
We simply substitute these names with their con-
stituents.
To make the experiment result more robust,
we conduct our experiments on two separate test
datasets. The ﬁrst one is a subset of the data de-
scribed above. We randomly split the whole data
into three parts, the training data (90%), the de-
velopment data (5%) and the test data (5%). The
second one is a set of symptom-prescription pairs
we manually extracted from the modern text book
of the course Formulaology of TCM (中医方剂
学) that is popularly adopted by many TCM col-
leges in China.
There are more cases in the ﬁrst sampled test
dataset (4,102 examples), but it suffers from lower
quality, as this dataset was parsed with simple
rules, which may not cover all exceptions. The
second test dataset has been proofread and all of
the prescriptions are the most classical and inﬂu-
ential ones in the history. So the quality is much
better than the ﬁrst one.
However, the number
of the cases is limited. There are 141 symptom-
prescription pairs in the second dataset. Thus we
use two test sets to do evaluation to take the ad-
vantages of both data magnitude and quality.
4.2
Experiment Settings
In our experiments, we implement our models
with the PyTorch toolkit 2. We set the embedding
size of both Chinese characters in the symptoms
and the herb tokens to 100.
We set the hidden
state size to 300, and the batch size to 20. We set
the maximum length of the herb sequence to 20
because the length of nearly all the prescriptions
2www.pytorch.org


## Page 6


Data
Average
Max
Under 20
Crawled Data
7.2
108
97.99%
Textbook Data
6.7
16
100%
Table 2: The statistic of the length of prescriptions.
Crawled data means the overall data crawled from the
Internet, including the training set data, the develop-
ment set data and test set 1. Textbook data is the same
to test set 2. Under 20 means the percentage of data
that are shorter or equal than length 20.
are within this range (see Table 2 for the statistics
of the length of prescriptions). Unless speciﬁcally
stated, we use bidirectional gated recurrent neu-
ral networks (BiGRNN) to encode the symptoms.
Adam (Kingma and Ba, 2015), and use the model
parameters that generate the best F1 score on the
development set in testing
4.3
Proposed Baseline
In this sub-section, we present the Multi-label
baseline we apply. In this model, we use a Bi-
GRNN as the encoder, which encodes symptoms
in the same way as it is described in Section 3.
Because the position of the herbs does not mat-
ter in the results, for the generation part, we im-
plement a multi-label classiﬁcation method to pre-
dict the herbs. We use the multi-label max-margin
loss (MultiLabelMarginLoss in pytorch) as the op-
timization objective, because this loss function is
more insensitive to the threshold, thus making the
model more robust.
We set the threshold to be
0.5, that is, if the probability given by the model
is above 0.5 and within the top k range (we set k
to 20 in our experiment, same to seq2seq model),
we take the tokens as answers. The way to calcu-
late probability is shown below.
p(i) = σ(WohT )
(11)
where
σ
indicates
the
non-linear
function
sigmoid, Wo ∈RH×V , H is the size of the
hidden state produced by the encoder and V is the
size of the herb vocabulary. hT is the last hidden
state produced by the encoder.
During evaluation, we choose the herbs satisfy-
ing two conditions:
1. The predicted probability of the herb is
within top k among all the herbs, where k is a
hyper-parameter. We set k to be the same as
the maximum length of seq2seq based mod-
els (20).
2. The predicted probability is above a threshold
Model
E 1
E 2
Average
Multi-Label
4.5
4.1
4.3
Basic seq2seq
6.8
6.6
6.7
Proposal
7.4
7.1
7.3
Table 3: Professional evaluation on the test set 2. The
score range is 0∼10. The Pearson’s correlation coefﬁ-
cient between the two evaluators is 0.72 and the Spear-
man’s correlation coefﬁcient is 0.72. Both p-values are
less than 0.01, indicating strong agreement.
0.5 (related to the max-margin).
4.4
Human Evaluation
Since medical treatment is a very complex task,
we invite two professors from Beijing University
of Chinese Medicine, which is one of the best
Traditional Chinese Medicine academies in China.
Both of the professors enjoy over ﬁve years of
practicing traditional Chinese medical treatment.
The evaluators are asked to evaluate the prescrip-
tions with scores between 0 and 10.
Both the
textual symptoms and the standard reference are
given, which is similar to the form of evaluation
in a normal TCM examination. Different from the
automatic evaluation method, the human evalua-
tors focus on the potential curative effect of the
candidate answers, rather than merely the literal
similarity. We believe this way of evaluation is
much more reasonable and close to reality.
Because the evaluation procedure is very time
consuming (each item requires more than 1
minute), we only ask the evaluators to judge the
results from test set 2.
As shown in Table 3, both of the basic seq2seq
model and our proposed modiﬁcation are much
better than the multi-label baseline. Our proposed
model gets a high score of 7.3, which can be of
real help to TCM practitioners when prescribing
in the real life treatment.
4.5
Automatic Evaluation Results
We use micro Precision, Recall, and F1 score as
the automatic metrics to evaluate the results, be-
cause the internal order between the herbs does
not matter when we do not consider the prescrib-
ing process.
In Table 4, we show the results of our proposed
models as well as the baseline models. One thing
that should be noted is that since the data in Test
set 2 (extracted from text book) have much better
quality than Test set 1, the performance on Test set


## Page 7


Model
Test set 1
Test set 2
P
R
F
P
R
F
Multi-label
10.83
29.72
15.87
13.51
40.49
20.26
Basic seq2seq
26.03
13.52
17.80
30.97
23.70
26.85
Proposal
29.57
17.30
21.83
38.22
30.18
33.73
Table 4: Automatic evaluation results of different models on the two test datasets. Multi-label is introduced in
Section 4.3. Test set 1 is the subset of the large dataset collected from the Internet, which is homogeneous to the
training set. Test set 2 is the test set extracted from the prescription text book.
Model
Test set 1
Test set 2
P
R
F
P
R
F
Basic seq2seq
26.03
13.52
17.80
30.97
23.70
26.85
+ coverage
26.69
12.88
17.37
37.09
24.12
29.23
+ soft loss
29.3
17.26
21.72
37.90
27.63
31.96
+ coverage & soft loss
29.57
17.30
21.83
38.22
30.18
33.73
Table 5: Ablation results of applying coverage mechanism and soft loss function. Test set 1 and test set 2 are the
same as Table 4
2 is much higher than it is on Test set 1, which is
consistent with our instinct.
From the experiment results we can see that the
baseline model multi-label has higher micro recall
rate 29.72, 40.49 but much lower micro precision
10.83, 13.51. This is because unlike the seq2seq
model that dynamically determines the length of
the generated sequence, the output length is rigid
and can only be determined by thresholds. We take
the tokens within the top 20 as the answer for the
multi-label model.
As to the basic seq2seq model, although it beats
the multi-label model overall, the recall rate drops
substantially.
This problem is partly caused by
the repetition problem, the basic seq2seq model
sometimes predicts high frequent tokens instead of
more meaningful ones. Apart from this, although
the seq2seq based model is better able to model
the correlation between target labels, it makes a
strong assumption on the order of the target se-
quence. In the prescription generation task, the or-
der between herb tokens are helpful for generating
the sequence. However, since the order between
the herbs does not affect the effect of the prescrip-
tion, we do not consider the order when evaluating
the generated sequence. We call the phenomenon
that the herbs are under the “weak order”. The
much too strong assumption on order can hurt the
performance of the model when the correct tokens
are placed in the wrong order.
In Table 5 we show the effect of applying cov-
erage mechanism and soft loss function.
Coverage mechanism gives a sketch on the pre-
scription.
The mechanism not only encourages
the model to generate novel herbs but also enables
the model to generate tokens based on the already
predicted ones.
This can be proved by the im-
provement on Test set 2, where both the precision
and the recall are improved over the basic seq2seq
model.
The most signiﬁcant improvement comes from
applying the soft loss function. The soft loss func-
tion can relieve the strong assumption of order
made by seq2seq model. Because predicting a cor-
rect token in the wrong position is not as harmful
as predicting a completely wrong token. This sim-
ple modiﬁcation gives a big improvement on both
test sets for all the three evaluation metrics.
4.6
Case Study
In this subsection, we show an example generated
by various models in Table 6 in test set 2 because
the quality of test set 2 is much more satisfactory.
The multi-label model produces too many herbs
that lower the precision, we do not go deep into its
results, already we report its results in the table.
For the basic seq2seq model, the result is bet-
ter than multi-label baseline in this case. “柴胡”
(radix bupleuri)、“葛根” (the root of kudzu vine)
can be roughly matched with “恶风发热，汗出头
疼” (Aversion to wind, fever, sweating, headache),
“甘草” (Glycyrrhiza)、“陈皮” (dried tangerine
or orange peel)、“桔梗” (Platycodon grandiﬂo-
rum) can be roughly matched with “鼻鸣咽干，
苔白不渴” (nasal obstruction, dry throat, white


## Page 8


Symptoms
外感风寒表虚证。恶风发热，汗出
头疼，鼻鸣咽干，苔白不渴，脉浮
缓或浮弱。
Translation
Exogenous
wind-cold exterior deﬁ-
ciency syndrome.
Aversion to wind,
fever, sweating, headache, nasal ob-
struction, dry throat, white tongue coat-
ing, not thirsty, ﬂoating slow pulse or
ﬂoating weak pulse.
Reference
桂枝芍药甘草生姜大枣
Multi-label
防风知母当归川芎黄芪橘红甘草
茯苓白术葛根荆芥柴胡麦冬泽泻
车前子石斛木通赤茯苓升麻白芍
药
Basic seq2seq
柴胡干葛川芎桔梗甘草陈皮半夏
Proposal
桂枝麻黄甘草生姜大枣
Table 6: Actual predictions made by various models in
test set 2. Multi-label model generates too many herb
tokens, so we do not list all of them here. Reference
is the standard answer prescription given by the text
book.4
tongue coating, not thirsty), “川芎” (Ligusticum
wallichii) can be used to treat the symptom of “头
疼” (headache). In this case, most of the herbs
can be matched with certain symptoms in the tex-
tual description. However, the problem is that un-
like the reference, the composition of herbs lacks
the overall design. The symptoms should not be
treated independently, as they are connected to
other symptoms. For example, the appearance of
symptom “头疼” (headache) must be treated to-
gether with “汗出” (sweat). When there is simply
headache without sweat, “川芎” (Ligusticum wal-
lichii) may be suitable. However, since there is
already sweat, this herb is not suitable in this sit-
uation. This drawback results from the fact that
this model heavily relies on the attention mecha-
nism that tries to match the current hidden state in
the decoder to a part of the context in the encoder
every time it predicts a token.
For our proposed model, the results are much
more satisfactory. “外感风寒” (Exogenous wind-
cold exterior deﬁciency syndrome) is the reason
of the disease, the symptoms “恶风发热，汗出
头疼，鼻鸣咽干，苔白不渴，脉浮缓或浮
弱” (Aversion to wind, fever, sweating, headache,
4Translation: 桂枝- cassia twig, 芍药- Chinese herba-
ceous peony 大黄- Rhubarb, 厚朴- Magnolia ofﬁcinalis, 枳
实- Fructus Aurantii Immaturus, 芒硝- Mirabilite, 栀子-
Cape Jasmine Fruit, 枳壳- Fructus Aurantii, 当归- Angel-
ica Sinensis, 甘草- Glycyrrhiza, 黄芩- Scutellaria, 生姜-
ginger, 大枣- Chinese date, 柴胡- radix bupleuri, 葛根- the
root of kudzu vine, 陈皮- dried tangerine or orange peel, 桔
梗- Platycodon grandiﬂorum, 川芎- Ligusticum wallichii,
麻黄- Chinese ephedra
nasal obstruction, dry throat, white tongue coat-
ing, not thirsty, ﬂoating slow pulse or ﬂoating
weak pulse) are the corresponding results.
The
prescription generated by our proposed model can
also be used to cure “外感风寒” (Exogenous
wind-cold exterior deﬁciency syndrome), in fact
“麻黄” (Chinese ephedra) and “桂枝” (cassia
twig) together is a common combination to cure
cold. However, “麻黄” (Chinese ephedra) is not
suitable here because there is already sweat. One
of the most common effect of “麻黄” (Chinese
ephedra) is to make the patient sweat. Since there
is already sweat, it should not be used. Compared
with the basic seq2seq model, our proposed model
have a sense of overall disease, rather than merely
discretely focusing on individual symptoms.
From the above analysis, we can see that com-
pared with the basic seq2seq model, our proposed
soft seq2seq model is aware more of the connec-
tions between symptoms, and has a better overall
view on the disease. This advantage is correspon-
dent to the principle of prescribing in TCM that
the prescription should be focusing on the “辩证”
(the reason behind the symptoms) rather than the
superﬁcial “症” (symptoms).
5
Conclusion
In this paper, we propose a TCM prescription gen-
eration task that automatically predicts the herbs
in a prescription based on the textual symptom
descriptions. To our knowledge, this is the ﬁrst
time that this critical and practicable task has
been considered. To advance the research in this
task, we construct a dataset of 82,044 symptom-
prescription pairs based on the TCM Prescription
Knowledge Base.
Besides the automatic evaluation, we also invite
professionals to evaluate the prescriptions given
by various models, the results of which show that
our model reaches the score of 7.3 out of 10,
demonstrating the effectiveness.
In the experi-
ments, we observe that directly applying seq2seq
model would lead to the repetition problem that
lowers the recall rate and the strong assumption of
the order between herb tokens can hurt the perfor-
mance. We propose to apply the coverage mecha-
nism and the soft loss function to solve this prob-
lem. From the experimental results, we can see
that this approach alleviates the repetition problem
and results in an improved recall rate.


## Page 9


References
Dzmitry Bahdanau, Kyunghyun Cho, and Yoshua Ben-
gio. 2014.
Neural machine translation by jointly
learning to align and translate.
arXiv preprint
arXiv:1409.0473.
Kyunghyun Cho, Bart van Merrienboer, Caglar Gul-
cehre, Dzmitry Bahdanau, Fethi Bougares, Holger
Schwenk, and Yoshua Bengio. 2014.
Learning
phrase representations using rnn encoder–decoder
for statistical machine translation. In Proceedings of
the 2014 Conference on Empirical Methods in Nat-
ural Language Processing (EMNLP), pages 1724–
1734. Association for Computational Linguistics.
Diederik P. Kingma and Jimmy Lei Ba. 2015. Adam:
a Method for Stochastic Optimization.
Inter-
national Conference on Learning Representations
2015, pages 1–15.
Jiwei Li, Will Monroe, Alan Ritter, Michel Galley,
Jianfeng Gao, and Dan Jurafsky. 2016. Deep rein-
forcement learning for dialogue generation. arXiv
preprint arXiv:1606.01541.
Jiwei Li, Will Monroe, Tianlin Shi, Alan Ritter,
and Dan Jurafsky. 2017.
Adversarial learning
for neural dialogue generation.
arXiv preprint
arXiv:1701.06547.
Wei Li and Zheng Yang. 2017. Distributed represen-
tation for traditional chinese medicine herb via deep
learning models. arXiv preprint arXiv:1711.01701.
Haitao Mi, Baskaran Sankaran, Zhiguo Wang, and Abe
Ittycheriah. 2016.
Coverage Embedding Models
for Neural Machine Translation.
Proceedings of
the 2016 Conference on Empirical Methods in Nat-
ural Language Processing (EMNLP-16), (Section
5):955–960.
Jinseok Nam, Eneldo Loza Menc´ıa, Hyunwoo J Kim,
and Johannes F¨urnkranz. 2017. Maximizing subset
accuracy with recurrent neural networks in multi-
label classiﬁcation. In Advances in Neural Informa-
tion Processing Systems, pages 5419–5429.
Abigail See, Peter J Liu, and Christopher D Man-
ning. 2017.
Get to the point:
Summarization
with pointer-generator networks.
arXiv preprint
arXiv:1704.04368.
Ilya Sutskever, Oriol Vinyals, and Quoc V Le. 2014.
Sequence to sequence learning with neural net-
works. In Advances in neural information process-
ing systems, pages 3104–3112.
Zhaopeng Tu, Zhengdong Lu, Yang Liu, Xiaohua Liu,
and Hang Li. 2016a. Coverage-based Neural Ma-
chine Translation. Arxiv, pages 1–19.
Zhaopeng Tu, Zhengdong Lu, Yang Liu, Xiaohua
Liu, and Hang Li. 2016b.
Modeling coverage
for neural machine translation.
arXiv preprint
arXiv:1601.04811.
Oriol Vinyals, Samy Bengio, and Manjunath Kudlur.
2015. Order matters: Sequence to sequence for sets.
arXiv preprint arXiv:1511.06391.
Liwen Wang. 2013. TCM inquiry modelling research
based on Deep Learning and Conditional Random
Field multi-lable learning methods.
Ph.D. thesis,
East China University of Science and Technology.
Xuewei Wang, Haibin Qu, Ping Liu, and Yiyu Cheng.
2004. A self-learning expert system for diagnosis
in traditional chinese medicine. Expert systems with
applications, 26(4):557–566.
Jun Yin, Xin Jiang, Zhengdong Lu, Lifeng Shang,
Hang Li,
and Xiaoming Li. 2015.
Neural
generative question answering.
arXiv preprint
arXiv:1512.01337.
Xiaoping Zhang. 2011. Topic Modelling and its ap-
plication in TCM clinical diagonosis and treatment.
Ph.D. thesis, Beijing Transportation University.
Zhu Zhipeng, Du Jianqiang, Liu Yingfeng, Yu Fang,
and Jigen Luo. 2017. Tcm prescription similartiy
computation based on lda topic modelling. Applica-
tion Research Of Computers, pages 1668–1670.
Xuezhong Zhou, Shibo Chen, Baoyan Liu, Runsun
Zhang, Yinghui Wang, Ping Li, Yufeng Guo, Hua
Zhang, Zhuye Gao, and Xiufeng Yan. 2010. Devel-
opment of traditional chinese medicine clinical data
warehouse for medical knowledge discovery and de-
cision support. Artiﬁcial Intelligence in medicine,
48(2):139–152.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
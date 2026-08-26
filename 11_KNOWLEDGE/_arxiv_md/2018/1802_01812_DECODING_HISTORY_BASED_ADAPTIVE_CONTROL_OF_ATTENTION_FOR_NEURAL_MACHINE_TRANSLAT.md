---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1802.01812
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1802.01812_Decoding-History-Based_Adaptive_Control_of_Attention_for_Neural_Machine_Translat

> Source: 1802.01812_Decoding-History-Based_Adaptive_Control_of_Attention_for_Neural_Machine_Translat.pdf

> Pages: 8

---


## Page 1


arXiv:1802.01812v1  [cs.CL]  6 Feb 2018
Decoding-History-Based Adaptive Control of Attention
for Neural Machine Translation
Junyang Lin, Shuming Ma, Qi Su, Xu Sun
MOE Key Laboratory of Computational Linguistics, Peking University
School of Electronics Engineering and Computer Science, Peking University
School of Foreign Languages, Peking University
{linjunyang, shumingma, sukia, xusun}@pku.edu.cn
Abstract
Attention-based sequence-to-sequence model has
proved successful in Neural Machine Translation
(NMT). However, the attention without consider-
ation of decoding history, which includes the past
information in the decoder and the attention mecha-
nism, often causes much repetition. To address this
problem, we propose the decoding-history-based
Adaptive Control of Attention (ACA) for the NMT
model.
ACA learns to control the attention by
keeping track of the decoding history and the cur-
rent information with a memory vector, so that the
model can take the translated contents and the cur-
rent information into consideration. Experiments
on Chinese-English translation and the English-
Vietnamese translation have demonstrated that our
model signiﬁcantly outperforms the strong base-
lines.
The analysis shows that our model is ca-
pable of generating translation with less repetition
and higher accuracy. The code will be available at
https://github.com/lancopku
1
Introduction
With the development of Deep Learning, Neural Machine
Translation (NMT) has demonstrated outstanding effects, and
the sequence-to-sequence model (Seq2Seq) [Sutskever et al.,
2014] is the most commonly-used model in NMT. The atten-
tion mechanism [Bahdanau et al., 2014; Luong et al., 2015]
is often used in the Seq2Seq model, and in many cases it can
signiﬁcantly improve the performance of the model. In trans-
lating, the decoder builds a language model on the target lan-
guage for semantic coherence, the attention mechanism ob-
tains the source-side information for the word generation at
each time step.
However, the current source-side information that the at-
tention mechanism acquires is often controversial to the trans-
lated contents because the attention has no knowledge of the
translated contents.
We present a typical example of the
over-translation of the attention-based Seq2Seq model on the
Chinese-English translation in Table 1. From the example, it
can be found that the attention-based Seq2Seq generates the
same phrase “the Russian capital of Moscow” for multiple
times, causing much repetition.
Seq2Seq+Attention: In the Russian capital of Moscow , the
Russian capital of Moscow of the Russian capital of Moscow
was killed this year because of the cold war, most of them were
homeless and the elderly, including many people.
Gold: The temperatures in Moscow, capital of Russia, dropped
to such low levels last night that even locals felt freezing cold.
Six people died as a result, bringing up the death toll due to
coldness this year to 239. Most of the dead were the homeless
and the elderly, including many drunk.
Table 1: An example of the translation of the conventional attention-
based Seq2Seq model on the NIST 2003 Chinese-English translation
task. The text highlighted indicates repetition.
With the motivation to tackle this problem, we propose our
decoding-history-basedAdaptive Control of Attention (ACA)
for the attention-based Seq2Seq model. The mechanism con-
trols the output of the attention based on the decoding his-
tory, including the past information in the decoder and the
past alignment information in the attention mechanism. The
computation of the attention requires the information of the
memory vector, which is updated based on the decoding his-
tory, by manipulating the decoder output and the attention
vector. With the help of the memory, the attention can be
more adaptive to the translated contents so that the repetition
in translation can be reduced.
Our main contributions include:
• We propose a decoding-history-based Adaptive Control
of Attention for the NMT model, which tackles the con-
ﬂict between the current attention and the decoding his-
tory so that the generation can be more adaptive to the
translated contents;
• Experiments on the Chinese-English translation and the
English-Vietnamese translation show that our model
outperforms the strong baselines, with the advantages of
3.61 BLEU score and 1.17 BLEU score over the best
attention-based Seq2Seq model;
• Compared with the strong baselines, the translation of
our model is with less repetition and higher accuracy.
2
Attention-based Seq2Seq
In Figure 1(a), we present a common type of attention-based
Seq2Seq with RNN as its main component, and as we use


## Page 2


-1

+1
ℎ-1
ℎ
ℎ+1
-1

+1

-1

+1
-1

+1
	
	
	

-2

-1


a. Attention-Based Seq2Seq
b. Attention-Based Seq2Seq + ACA
-1

+1
ℎ-1
ℎ
ℎ+1
-1

+1

+1
-1

+1
-1

Figure 1: Structure of the attention-based Seq2Seq and our Seq2Seq with ACA. The left is the structure of the attention-based Seq2Seq
model, and the right is the structure of our model, the attention-based Seq2Seq with the ACA.
LSTM in our model, we introduce the structure of LSTM in
the following.
2.1
Encoder
As words are discrete units, the words in the source sequence
should be sent through an embedding layer to become word
embeddings as the input. On top of the embedding layer,
the encoder turns the embeddings x = {x1, ..., xn} into a se-
quence of encoder outputs h = {h1, ..., hn} and sends out the
ﬁnal hidden state hn to the decoder.
The encoder in our model is a bidirectional LSTM, which
is deﬁned below:
fi = σ(Wf [xi, hi−1] + bf)
(1)
ii = σ(Wi[xi, hi−1] + bi)
(2)
oi = σ(Wo[xi, hi−1] + bo)
(3)
˜Ci = tanh(WC[xi, hi−1] + bC)
(4)
Ci = fi ⊙Ci−1 + ii ⊙˜Ci
(5)
hi = oi ⊙tanh(Ci)
(6)
where xi is the input word embedding at each time step from
a minibatch of input sequences. LSTM consists of four gates,
which collectively control the information ﬂow from the last
time step and the current time step.
Bidirectional LSTM
contains the same structure of LSTM, but it reads the in-
put in two directions to generate two sequences of hidden
states −→h ={−→
h1, −→
h2, −→
h3, ..., −→
hn} and ←−h ={←−
h1, ←−
h2, ←−
h3, ..., ←−
hn},
where:
−→
hi = LST M(xi, −−→
hi−1, Ci−1)
(7)
←−
hi = LST M(xi, ←−−
hi−1, Ci−1)
(8)
The encoder outputs corresponding to each time step are con-
catenated as mentioned below:
hi =[−→
hi; ←−
hi]
(9)
2.2
Decoder
The decoder is responsible for decoding the ﬁnal state of the
encoder hn to a new sequence y = {y1, ..., ym}. With the
ﬁnal encoder state as the initial state, the decoder is initial-
ized to decode step by step, with a word embedding at each
time step, until it generates the token representing the end-of-
sentence mark.
For the decoder, we implement a unidirectional LSTM.
The output of each time step is sent into a feed-forward
neural network to be projected into the space of vocabulary
Y ∈R|Y |×dim. At each time step, the decoder generates a
word yt by sampling from a distribution of the target vocabu-
lary Pvocab, where:
Pvocab = softmax(Wovt)
(10)
vt = g(Wv[ct; st])
(11)
st = LST M(yt−1, st−1, Ct−1)
(12)
where g(·) refers to non-linear activation function.
The global attention mechanism [Luong et al., 2015] is
applied to the LSTM output st and the encoders outputs
h = {h1, ..., hn} in order to obtain the global attention αt,i
and the context vector ct, which is described in the follow-
ing:
ct =
n
X
i=1
αt,ihi
(13)
αt,i =
exp(et,i)
Pn
j=1exp(et,j)
(14)
et,i = s⊤
t−1Wahi
(15)
2.3
Training
The training for the Seq2Seq model is usually based on max-
imum likelihood estimation.
Given the parameters θ and


## Page 3



R
-1

F


Figure 2: Structure of the Recurrent Memory in the ACA. “R”
and “F” refer to the Remove and Feed operations, and “g” refers to
the MLP.
source text x, the model generates a sequence ˜y. The learning
process is to minimize the negative log-likelihood between
the generated text ˜y and reference y, which in our context is
the sequence in target language for machine translation and
summary for abstractive summarization:
L = −1
N
N
X
i=1
T
X
t=1
p(y(i)
t |˜y(i)
<t, x(i), θ)
(16)
where the loss function is equivalent to maximizing the con-
ditional probability of sequence y given parameters θ and
source sequence x.
3
Adaptive Control of Attention
As it is mentioned above, it is easy for the conventional
attention-based Seq2Seq NMT models to suffer from gener-
ating incoherent texts due to the conﬂict between the attention
mechanism and the decoding history. Based on the hypothe-
sis, we propose our decoding-history-based Adaptive Control
of Attention (ACA) mechanism to tackle the problem. In-
stead of sending the context vector ct directly to the output
layer at each time step, we propose to update the attention
with a recurrent memory that stores the information from the
previous decoding time steps, so that the information from
the attention mechanism can be controlled to be most bene-
ﬁcial to the whole generation. The memory updates itself at
each time step with the information from the current decoder
output and the current context vector, so that it can learn to
remove unnecessary information and store important infor-
mation at each time step. Moreover, it is responsible for re-
stricting the information ﬂow of the context vector in order to
mitigate the conﬂict between attention and neural language
model.
3.1
Recurrent Memory
As our objective in this study is to build connection for the
attention at the current time step with the decoding history,
we implement the Recurrent Memory in the decoder for up-
dating the context vector. The recurrent memory in the model
is responsible for controlling the information ﬂow of the at-
tention mechanism, so that the effects of the attention mech-
anism can be connected with the previous decoding outputs
from the RNN as well as the attention mechanism. Moreover,
the memory should be updated at every decoding time step,
so that it can reﬂect the development of the decoding history.


U


Figure 3: Structure of Gated Control. “U” refers to the Update
Gate.
The memory mt is a representation vector at the decoding
time step t, whose initialization m0 is the last hidden state
of the encoder, which is also the initial state for the RNN of
the decoder. At each decoding time step t, the memory mt
is updated with a Remove-Feed operation. The operation is
based on the decision of the decoder output st from the RNN
and the context vector ct from the attention mechanism, so
that the memory can observe the situation at the current time
step and update itself with the guide of the current informa-
tion. The structure of the Recurrent Memory is presented in
Figure 2.
At the beginning, the previous memory mt−1 experiences
a Remove-Feed operation. The decoder output st and the
context vector ct generate a Remove Gate rt to decide how
to update the memory to be adaptive to the current decoding
and a Feed Gate ft to decide how to update the memory with
new information from the decoder and the attention:
rt = σ(gr([st; ct]))
(17)
ft = σ(gf([st; ct]))
(18)
where g(·) refers to non-linear activation function to generate
a vector of the hidden size.
Next, the previous memory mt−1 passes through the gates
and updates itself to be mt by removing information from
the previous memory and adding new information from the
decoder output and the context vector:
mt = (rt ⊙mt−1) ⊕(ft ⊙gi([st; ct]))
(19)
The Remove operation based on st and ct can update the
information stored in the memory based on the decoding and
the attention at the current time step, so that the memory
can be adaptive to the current decoding. The Feed opera-
tion based on the two same elements can provide the mem-
ory with the new information from the current time step so
that the memory can store the repetition of the translated con-
tents. Next, we introduce how the model makes use of the
time-sensitive memory to improve the decoding.
3.2
Gated Control
After the update, before entering the next time step, the mem-
ory mt collaborates with the decoder output st to generate
a gate for the context vector ct. Therefore, the information
from the attention mechanism is controlled by the informa-
tion from the decoding history and the current state with the
help of the updated memory. The detail operations are illus-
trated below.


## Page 4


Before entering the next time step, the current memory mt
and the decoder output st generate an Update Gate ut for the
context vector ct:
ut = σ(gu([mt; st]))
(20)
ˆct = ut ⊙ct
(21)
where ˆct is the ﬁnal context vector to be concatenated with
the decoder output st to generate the ﬁnal output ˆvt, which is
given by:
ˆvt = go([st; ˆct])
(22)
In the ﬁnal step of decoding, instead of sending vt to the
output layer for the word prediction as mentioned in Equa-
tion 10, the model sends ˆvt, outputted from the ACA, for the
prediction at each time step.
With the Gated Control, the context vector ct can be rec-
tiﬁed based on the decoding history and the current informa-
tion. The memory storing useful information of the partial
translation can encourage to model to translate contents that
are less repeated compared with the translated contents.Even
if the source-side information in the context vector is in con-
ﬂict with the decoding history, the conﬂict can be mitigated
by the gate controlled by the memory.
4
Experiment
This section introduces the details of our experiments, includ-
ing datasets, setups, baseline models as well as results.
4.1
Datasets
We evaluated our proposed model on the NIST translation
task for Chinese-English translation and provided the analy-
sis on the same task. Moreover, in order to evaluate the per-
formance of our model on the low-resource translation, we
also evaluated our model on the IWLST 2015 [Cettolo et al.,
2015] for the English-Vietnamese translation task.
Chinese-English Translation For the NIST translation
task, we trained our model on 1.25M sentence pairs extracted
from LDC2002E18, LDC2003E07, LDC2003E14, Hansards
portion of LDC2004T07, LDC2004T08 and LDC2005T06,
with 27.9M Chinese words and 34.5M English words. Fol-
lowing Su et al. [2016], we validated our model on the dataset
for the NIST 2005 translation task and tested our model on
that for the NIST 2002, 2003, 2004, 2006, 2008 transla-
tion tasks.
We used the most frequent 50,000 words for
both the Chinese vocabulary and the English vocabulary.
The evaluation metric is BLEU [Papineni et al., 2002], and
we calculated the case-insensitive NIST BLEU score with
multi-bleu.perl provided by Moses1 .
English-Vietnamese Translation The data is from the
translated TED talks, containing 133K training sentence
pairs provided by the IWSLT 2015 Evaluation Campaign
[Cettolo et al., 2015]. We followed the studies of Huang et al.
[2017], and used the same preprocessing as well as the valida-
tion set and the test set. The validation set is the TED tst2012
with 1553 sentences and the test set is the TED tst2013 with
1268 sentences. The English vocabulary is 17.7K words and
the Vietnamese vocabulary is 7K words. The evaluation met-
ric is also BLEU as mentioned above.
1http://www.statmt.org/moses/.
4.2
Setting
We implement the models using PyTorch, and the experi-
ments are conducted on an NVIDIA 1080Ti GPU. Both the
size of word embedding and hidden size are 512, and the
batch size is 64. We use Adam optimizer [Kingma and Ba,
2014] to train the model with the default setting β1 = 0.9,
β2 = 0.999 and ǫ = 1 × 10−8, and we initialize the learning
rate to 0.001.
Based on the performance on the development sets, we use
a 3-layer LSTM as the encoder and a 2-layer LSTM as the
decoder. Gradient clipping is applied so that the norm of the
gradients cannot be larger than a constant, which is 10 in our
experiments. Dropout is used with the dropout rate set to 0.2.
Following Xiong et al. [2017], we use beam search with a
beam width of 10 to generate translation for the evaluation
and test, and we normalize the log-likelihood scores by sen-
tence length.
4.3
Baselines
In the following, we introduce our baseline models for
the Chinese-English translation and the English-Vietnamese
translation respectively.
Chinese-English Translation
Following Su et al. [2016] and Zhang et al. [2017], we com-
pare our model with the state-of-the-art NMT systems based
on our implementation and the results directly reported in
their articles, and we report the results of the baselines, Moses
and RNNSearch from the study of Su et al. [2016].
• Moses An open source phrase-based translation sys-
tem with default conﬁgurations and a 4-gram language
model trained on the training data for the target lan-
guage;
• RNNSearch An attention-based Seq2Seq with ﬁne-
tuned hyperparameters;
• Lattice The Seq2Seq model with a Lattice-based RNN
Encoder [Su et al., 2016];
• Bi-Tree-LSTM A tree-coverage Seq2Seq model which
lets the model depend on the source-side syntax
[Chen et al., 2017];
• Mixed RNN Extending RNNSearch with a mixed RNN
as the encoder [Li et al., 2017];
• CPR Extending RNNSearch with a coverage penalty
[Wu et al., 2016];
• POSTREG
Extending
RNNSearch
with
poste-
rior regularization with a constrained posterior set
[Ganchev et al., 2010];
• PKI Extending RNNSearch with posterior regulariza-
tion to integrate prior knowledge [Zhang et al., 2017].
English-Vietnamese Translation
Following Luong and Manning [2015], Raffel et al. [2017]
and Huang et al. [2017], we compare our model with the
state-of-the-art NMT models, and we present the results of
the baseline directly reported in their studies.
• RNNSearch-1 The attention-based Seq2Seq model by
Luong and Manning [2015];


## Page 5


Model
MT-02
MT-03
MT-04
MT-05
MT-06
MT-08
Ave.
Moses [Su et al., 2016]
33.19
32.43
34.14
31.47
30.81
23.85
31.04
RNNSearch [Su et al., 2016]
34.68
33.08
35.32
31.42
31.61
23.58
31.76
Lattice [Su et al., 2016]
35.94
34.32
36.50
32.40
32.77
24.84
32.95
Coverage [Tu et al., 2016]
-
-
-
32.73
32.47
25.23
-
Bi-Tree-LSTM [Chen et al., 2017]
36.57
35.64
36.63
34.35
30.57
-
-
Mixed RNN [Li et al., 2017]
37.70
34.90
38.60
35.50
35.60
-
-
CPR [Zhang et al., 2017]
33.84
31.18
33.26
30.67
29.63
22.38
29.72
POSTREG [Zhang et al., 2017]
34.37
31.42
34.18
30.99
29.90
22.87
30.20
PKI [Zhang et al., 2017]
36.10
33.64
36.48
33.08
32.90
24.63
32.51
Seq2Seq+Attention
35.79
35.22
36.86
33.14
33.05
24.56
33.10
+ACA
40.25
38.31
40.20
36.82
36.53
28.14
36.71
Table 2: Results of our model and the baselines (directly reported in the referred articles) on the Chinese-English translation, tested on the
NIST Machine Translation tasks in 2003, 2004, 2005, 2006 with BLEU score. “-” means that the studies did not test the models on the
corresponding datasets.
Model
BLEU
RNNSearch-1 [Luong and Manning, 2015]
23.30
RNNSearch-2 [Huang et al., 2017]
26.10
LabelEmb [Sun et al., 2017b]
26.80
NPMT [Huang et al., 2017]
27.69
NPMT+LM [Huang et al., 2017]
28.67
Seq2Seq+Attention
26.93
+ACA
29.10
Table 3: Results of our model and the baselines (directly reported in
the referred articles) on the English-Vietnamese translation, tested
on the TED tst2013 with the BLEU score.
• RNNSearch-2 The implementation of the attention-
based Seq2Seq by Huang et al. [2017];
• LabelEmb Extending RNNSearch with soft target rep-
resentation [Sun et al., 2017b];
• NPMT The Neural Phrased-based Machine Translation
model by Huang et al. [2017];
• NPMT-LM On the basis of the NPMT, a trained 4th-
order language model is added.
4.4
Results
Table 2 shows the overall results of the systems on the
Chinese-English translation task.
We compare our model
with the strong baselines with their results directly reported
in their articles. To facilitate fair comparison, we compare
with the baselines that are trained on the same training set
or slightly larger training set as reported in their articles.
Many of the models are from the studies of the recent two
years, which prove to be very strong baselines. The results
have shown that for the six translation tasks, our ACA model
has clear advantage over them, with 4.95 BLEU score over
RNNSearch and 3.76 BLEU score over PKI, which proves
that our model is effective.
Table 3 shows the overall results of the systems on the
English Vietnamese translation. It can be found that on the
low-resource translation, the ACA can also bring signiﬁcant
improvement for the attention-based Seq2Seq model, with
1-gram
2-gram
3-gram
4-gram
0
5
10
15
20
% of the duplicates
w/o ACA
ACA
Figure 4: Percentage of the duplicates at sentence level. Tested on
the NIST 2003 dataset. The red bar is the performance of our ACA,
and the blue bar is the attention-based SeqSeq without ACA.
the advantage of over 2.17 BLEU score over the strongest
attention-based Seq2Seq and 1.41 BLEU score over the
SOTA model NPMT. Moreover, compared with NPMT with
a pretrained language model, our model is still better.
4.5
Analysis
In order to test whether our model can mitigate the problem of
repetition in translation, we tested the repetition on the NIST
2003 dataset, following See et al. [2017]. We evaluated the
proportion of the duplicates of 1-gram, 2-gram, 3-gram and
4-gram in each sentence and calculated the mean value. It
can be found that at all levels, the translation of our model
has less repetition. Moreover, the advantage of ours becomes
clearer with the increase of the number of gram. Especially
for the 4-gram, the proportion of duplicates of our model is
almost only a half of that of the model without ACA. It is nor-
mal that there are repeating words in a sentence, but repeating
4-gram in most cases is unreasonable. Compared with the
model without ACA, ACA can help the Seq2Seq model re-
duce unreasonable repetition and therefore mitigate the prob-
lem of over-translation by taking the decoding history into
account.


## Page 6


0
10
20
30
40
50
60
22
24
26
28
30
32
34
36
38
Sentence length (no shorter than)
BLEU (%)
w/o ACA
ACA
Figure 5: Performance on different sentence lengths. Tested on
the NIST 2003 dataset. The red line is the performance of our ACA,
and the blue line is the attention-based SeqSeq without ACA.
Moreover, we choose the NIST 2003 Chinese-English
translation dataset to test the performance of our model and
the conventional attention-based Seq2Seq model without our
ACA. We test the BLEU scores on sentences of length no
shorter than 10, 20, 30, 40, 50, and 60. With the increase
of length, the performance of both models decrease but our
model ACA always has a clear advantage over the attention-
based Seq2Seq. In our hypothesis, the model can adapt to the
decoding history by improving the attention mechanism, so it
is possible that it can perform better on the long-length sen-
tence translation. Our analysis proves that the model can be
more robust to translating sentences of diverse lengths.
4.6
Translation Examples
Table 4 shows two translation examples of our model on
the NIST 2003 dataset, compared with the translation of the
attention-based Seq2Seq model without ACA and the refer-
ence. It is obvious that both two translation examples of our
example are similar to the references, outperforming those
of the model without ACA, which has problems of repetition
and meaning inconsistency. For the ﬁrst sentence, the model
without ACA generates repetition of “cell phone users” and
misses the semantic unit “top”. On the contrary, our transla-
tion is closer to literal translation, which is more faithful to
the expression in the source. For the second example, it re-
quires the model to reorder the translation since the name is
followed by an adverbial phrase in the source. The complex
and different structure in Chinese confused the model without
ACA, which can only generate repetition of “we are entering
a new era”. With ACA, our model successfully reorders the
translation by putting the name after the adverbial.
5
Related Work
The
studies
of
encoder-decoder
framework
[Kalchbrenner and Blunsom,
2013;
Cho et al.,
2014;
Sutskever et al., 2014] for this task launched the Neural
Machine Translation (NMT). To improve the focus on the
information in the encoder, Bahdanau et al. [2014] proposed
the attention mechanism, which greatly improved the perfor-
Source: 在此之前一年, 单单手机用户已跃居全球之冠。
Reference: The year before that, the number of mobile phone
users alone already topped the world.
Seq2Seq+Attention: A year ago, cell phone users of cell phone
users are already in the world.
+ACA: In the past year, cell phone users have leapt to the high-
est level in the world.
Source: 佛莱文在谈及推行再生性能源策略已获致成功时
表示: “我们正进入一个新时代。”
Reference: Speaking about the success of promoting the strat-
egy of renewable energies, Flavin said: “we’re entering a new
era.”
Seq2Seq+Attention: “We are entering a new era.” “We are
ente-ring a new era.”
+ACA: Speaking on the success of the renewable energy strat-
egy, Fortuyn said: “we are entering a new era.”
Table 4: Two translation examples of our model, compared with the
translation of the attention-based Seq2Seq model and the reference.
mance of the Seq2Seq model on NMT. Still, the attention
mechanism suffers from prediction failure, and therefore,
a number of studies were proposed to improve the mech-
anism, which also enhanced the performance of the NMT
model [Luong et al., 2015; Mi et al., 2016b; Jean et al.,
2015; Feng et al., 2016; Tu et al., 2016; Mi et al., 2016a;
Meng et al., 2016; dou; Xiong et al., 2017]. Some of them
[Tu et al., 2016; Meng et al., 2016] incorporated the previous
attention into the current attention for better alignment, but
none of them are based on the decoding history.
Besides improving attention mechanism for NMT, there
are also some more effective neural networks. Gehring et al.
[2017] turned the RNN-based model into CNN-based
model, which greatly improves the computation speed.
Vaswani et al. [2017] removed the CNN and RNN and only
used attention mechanism to build the model and showed out-
standing performance. Also, some researches incorporated
external knowledge in their systems and also achieved obvi-
ous improvement [Li et al., 2017; Chen et al., 2017].
6
Conclusion
In conclusion, this paper proposes the decoding-history-
based Adaptive Control of Attention (ACA) for the NMT
model, which can transmit the signiﬁcant information in the
decoding history to control the output of the attention mech-
anism adaptively. Thus, the output of the attention mecha-
nism is based on the the decoding history, including the past
information in the RNN decoder as well as the alignment in-
formation in the attention mechanism. With this method, the
conﬂict between the source-side information from the atten-
tion and the translated contents can be mitigated. Compared
with the attention-based Seq2Seq model, our model captures
more correct source information with the help of the decod-
ing history and its translation behaves more adaptive to the
past translation. Experiments on the Chinese-English transla-
tion and the English-Vietnamese translation all show that our
model outperforms the strong baselines, which demonstrate
the effectiveness of our model.


## Page 7


References
Dzmitry Bahdanau, Kyunghyun Cho, and Yoshua Bengio.
Neural machine translation by jointly learning to align and
translate. CoRR, abs/1409.0473, 2014.
Mauro Cettolo, Jan Niehues, Sebastian St¨uker, Luisa Ben-
tivogli, Roldano Cattoni, and Marcello Federico. The iwslt
2015 evaluation campaign. Proc. of IWSLT, Da Nang, Viet-
nam, 2015.
Huadong Chen, Shujian Huang, David Chiang, and Jiajun
Chen. Improved neural machine translation with a syntax-
aware encoder and decoder. In ACL 2017, pages 1936–
1945, 2017.
Kyunghyun Cho, Bart van Merrienboer, C¸ aglar G¨ulc¸ehre,
Dzmitry Bahdanau, Fethi Bougares, Holger Schwenk, and
Yoshua Bengio.
Learning phrase representations using
RNN encoder-decoder for statistical machine translation.
In EMNLP 2014, pages 1724–1734, 2014.
Shi Feng, Shujie Liu, Nan Yang, Mu Li, Ming Zhou, and
Kenny Q. Zhu. Improving attention modeling with implicit
distortion and fertility for machine translation. In COLING
2016, pages 3082–3092, 2016.
Kuzman Ganchev, Jennifer Gillenwater, Ben Taskar, et al.
Posterior regularization for structured latent variable mod-
els. Journal of Machine Learning Research, 11(Jul):2001–
2049, 2010.
Jonas Gehring, Michael Auli, David Grangier, Denis Yarats,
and Yann N. Dauphin. Convolutional sequence to sequence
learning. In ICML 2017, pages 1243–1252, 2017.
Po-Sen
Huang,
Chong
Wang,
Dengyong
Zhou,
and
Li Deng. Neural phrase-based machine translation. CoRR,
abs/1706.05565, 2017.
S´ebastien Jean, KyungHyun Cho, Roland Memisevic, and
Yoshua Bengio.
On using very large target vocabulary
for neural machine translation. In ACL 2015, pages 1–10,
2015.
Nal Kalchbrenner and Phil Blunsom. Recurrent continuous
translation models. In EMNLP 2013, pages 1700–1709,
2013.
Diederik P. Kingma and Jimmy Ba. Adam: A method for
stochastic optimization. CoRR, abs/1412.6980, 2014.
Junhui Li, Deyi Xiong, Zhaopeng Tu, Muhua Zhu, Min
Zhang, and Guodong Zhou. Modeling source syntax for
neural machine translation. In ACL 2017, pages 688–697,
2017.
Minh-Thang Luong and Christopher D Manning. Stanford
neural machine translation systems for spoken language
domains. In Proceedings of the International Workshop
on Spoken Language Translation, 2015.
Thang Luong, Hieu Pham, and Christopher D. Manning. Ef-
fective approaches to attention-based neural machine trans-
lation. In EMNLP 2015, pages 1412–1421, 2015.
Shuming Ma and Xu Sun. A semantic relevance based neu-
ral network for text summarization and text simpliﬁcation.
CoRR, abs/1710.02318, 2017.
Shuming Ma, Xu Sun, Jingjing Xu, Houfeng Wang, Wenjie
Li, and Qi Su. Improving semantic relevance for sequence-
to-sequence learning of chinese social media text summa-
rization.
In Proceedings of the 55th Annual Meeting of
the Association for Computational Linguistics, ACL 2017,
Vancouver, Canada, July 30 - August 4, Volume 2: Short
Papers, pages 635–640, 2017.
Fandong Meng, Zhengdong Lu, Hang Li, and Qun Liu. Inter-
active attention for neural machine translation. In COLING
2016, pages 2174–2185, 2016.
Haitao Mi, Baskaran Sankaran, Zhiguo Wang, and Abe Itty-
cheriah. Coverage embedding models for neural machine
translation. In EMNLP 2016, pages 955–960, 2016.
Haitao Mi, Zhiguo Wang, and Abe Ittycheriah. Supervised
attentions for neural machine translation. In EMNLP 2016,
pages 2283–2288, 2016.
Kishore Papineni, Salim Roukos, Todd Ward, and Wei-Jing
Zhu. Bleu: a method for automatic evaluation of machine
translation. In ACL, 2002, pages 311–318, 2002.
Colin Raffel, Minh-Thang Luong, Peter J. Liu, Ron J. Weiss,
and Douglas Eck.
Online and linear-time attention by
enforcing monotonic alignments.
In ICML 2017, pages
2837–2846, 2017.
Abigail See, Peter J. Liu, and Christopher D. Manning. Get to
the point: Summarization with pointer-generator networks.
In ACL 2017, pages 1073–1083, 2017.
Jinsong Su, Zhixing Tan, Deyi Xiong, and Yang Liu. Lattice-
based recurrent neural network encoders for neural ma-
chine translation. CoRR, abs/1609.07730, 2016.
Xu Sun, Xuancheng Ren, Shuming Ma, and Houfeng Wang.
meprop: Sparsiﬁed back propagation for accelerated deep
learning with reduced overﬁtting.
In Proceedings of
the 34th International Conference on Machine Learning,
ICML 2017, Sydney, NSW, Australia, 6-11 August 2017,
pages 3299–3308, 2017.
Xu Sun, Bingzhen Wei, Xuancheng Ren, and Shuming Ma.
Label embedding network: Learning label representation
for soft training of deep networks. CoRR, abs/1710.10393,
2017.
Ilya Sutskever, Oriol Vinyals, and Quoc V. Le. Sequence to
sequence learning with neural networks. In NIPS, 2014,
pages 3104–3112, 2014.
Zhaopeng Tu, Zhengdong Lu, Yang Liu, Xiaohua Liu, and
Hang Li. Modeling coverage for neural machine transla-
tion. In ACL 2016, 2016.
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszko-
reit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, and
Illia Polosukhin.
Attention is all you need.
CoRR,
abs/1706.03762, 2017.
Bingzhen Wei, Xu Sun, Xuancheng Ren, and Jingjing Xu.
Minimal effort back propagation for convolutional neural
networks. CoRR, abs/1709.05804, 2017.


## Page 8


Yonghui Wu, Mike Schuster, Zhifeng Chen, Quoc V. Le, Mo-
hammad Norouzi, Wolfgang Macherey, Maxim Krikun,
Yuan Cao, Qin Gao, Klaus Macherey, Jeff Klingner,
Apurva Shah, Melvin Johnson, Xiaobing Liu, Lukasz
Kaiser, Stephan Gouws, Yoshikiyo Kato, Taku Kudo,
Hideto Kazawa, Keith Stevens, George Kurian, Nishant
Patil, Wei Wang, Cliff Young, Jason Smith, Jason Riesa,
Alex Rudnick, Oriol Vinyals, Greg Corrado, Macduff
Hughes, and Jeffrey Dean. Google’s neural machine trans-
lation system: Bridging the gap between human and ma-
chine translation. CoRR, abs/1609.08144, 2016.
Hao Xiong, Zhongjun He, Xiaoguang Hu, and Hua Wu.
Multi-channel encoder for neural machine translation.
CoRR, abs/1712.02109, 2017.
Jingjing Xu, Xu Sun, Xuancheng Ren, Junyang Lin, Binzhen
Wei, and Wei Li. Dp-gan: Diversity-promoting generative
adversarial network for generating informative and diver-
siﬁed text. CoRR, abs/1802.01345, 2018.
Jiacheng Zhang, Yang Liu, Huanbo Luan, Jingfang Xu, and
Maosong Sun. Prior knowledge integration for neural ma-
chine translation using posterior regularization.
In ACL
2017, pages 1514–1523, 2017.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
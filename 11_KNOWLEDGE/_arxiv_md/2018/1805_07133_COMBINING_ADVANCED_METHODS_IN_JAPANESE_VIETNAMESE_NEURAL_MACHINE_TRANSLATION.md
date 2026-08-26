---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1805.07133
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1805.07133_Combining_Advanced_Methods_in_Japanese-Vietnamese_Neural_Machine_Translation

> Source: 1805.07133_Combining_Advanced_Methods_in_Japanese-Vietnamese_Neural_Machine_Translation.pdf

> Pages: 7

---


## Page 1


arXiv:1805.07133v1  [cs.CL]  18 May 2018
1
Combining Advanced Methods in
Japanese-Vietnamese Neural Machine Translation
Thi-Vinh Ngo
University of Information and Communication Technology
TNU, Vietnam
ntvinh@ictu.edu.vn
Phuong-Thai Nguyen
University of Engineering and Technology
VNU, Vietnam
npthai@vnu.edu
Thanh-Le Ha
Institute of Anthropomatics and Robotics
KIT, Germany
thanh-le.ha@kit.edu
Le-Minh Nguyen
School of Information Science
JAIST, Japan
nguyenml@jaist.ac.jp
Abstract—Neural machine translation (NMT) systems have
recently obtained state-of-the art in many machine translation
systems between popular language pairs because of the avail-
ability of data. For low-resourced language pairs, there are
few researches in this ﬁeld due to the lack of bilingual data.
In this paper, we attempt to build the ﬁrst NMT systems for
a low-resourced language pairs:Japanese-Vietnamese. We have
also shown signiﬁcant improvements when combining advanced
methods to reduce the adverse impacts of data sparsity and
improve the quality of NMT systems. In addition, we proposed
a variant of Byte-Pair Encoding algorithm to perform effective
word segmentation for Vietnamese texts and alleviate the rare-
word problem that persists in NMT systems.
Index Terms—Neural Machine Translation, Japanese - Viet-
namese Translation, Low-resourced Neural Machine Translation,
Byte-Pair Encoding, Back Translation, Mix-Source
I. INTRODUCTION
Neural machine translation (NMT) [1], [2] is widely ap-
plied for machine translation (MT) in recent years and fo-
cuses on popular language pairs such as English↔French,
English↔German, English↔Chinese or English↔Japanese.
NMT has obtained state-of-the-art performance on those lan-
guage pairs compared to the traditional statistical machine
translation (SMT) when given enough data [3], [4]. Further-
more, due to the ability of feature learning, NMT systems
can be trained end-to-end with pure parallel texts and mini-
mal linguistic knowledge of the languages involved. Thus it
makes training NMT for a new language pair much easier,
more scalable and robust. Nevertheless, NMT has not been
employed in many low-resourced language pairs since in those
scenarios, data scarcity often limits the learning ability of neu-
ral methods. In contrast, combinating complicated linguistic-
driven features in a typical log-linear framework still keeps
SMT the best approach in many translation directions but also
hard to apply to new domains or to other language pairs.
In this paper we attempt to build NMT systems for such
a low-resourced language pair: Japanese↔Vietnamese. Our
aim is to set the ﬁrst and reasonable NMT systems that
can be reproducible in order to serve as the baseline for
further researches in the direction1. Furthermore, we conduct
experiments using some advanced methods to improve the
quality of the systems. An important criteria for those methods
is that they must be scalable and language-independent as
much as possible. The criteria ensures the basic principle of
NMT as well as the reproducibility of the systems. On the
other hand, the methods are chosen in the direction that they
would help alleviate the data sparsity problem of NMT when
being applied in this low-resourced setting.
Speciﬁcally, to deal with rare-word translation problems, we
experiment with translation units in different levels: subword,
word and beyond. In morphological-rich languages such as
English or German, using subword as the translation units
is often suitable since neural methods are able to induce
meaning or linguistic function of sub-components constituting
a word. Byte-Pair Encoding (BPE) [5] is a simple unsupervised
technique to do subword segmentation and it has great effects
when applied to NMT training. Japanese and Vietnamese (and
some other Asian languages), however, have different word
segmentation issues. Hence, it would be difﬁcult to apply
BPE directly to the texts in those languages and build NMT
systems for subword translation without any modiﬁcation. In
this paper, we experiment different segmentation methods for
both languages and also propose a variant of BPE algorithm
to learn translation units for Vietnamese in an unsupervised
way.
We also attempt to increase the amount of training data by
using back-translated texts or mix-source data just from our
small available corpus. Those data augmentation approaches
have shown their effectiveness on various NMT systems,
especially in under-resourced scenarios. While back translation
technique is used to generate synthetic data from monolingual
corpora, mix-source technique utilizes human-quality corpora
in a multilingual setting, leveraging the transfer learning ability
across languages. Both are simple but elegantly model the
relevant noise needed in training neural architectures in such
low-resourced situations.
1All the corpora and codes used in the experiments will be published later.


## Page 2


2
The main contributions of this paper are:
• We
created
the
ﬁrst
NMT
systems
for
Japanese↔Vietnamese
and
released
the
dataset
as
well as the codes to reproduce the experiments.
• We conducted several ways of segmentation and proposed
a variant of BPE algorithm for Vietnamese, which does
not need any labeled data or linguistic resource.
• We applied elegant data augmentation methods in order
to reduce the severeness of data sparsity problem in
training NMT systems using a small dataset of Japanese-
Vietnamese.
II. NEURAL MACHINE TRANSLATION
In this section, we will describe the general architecture of
NMT as a kind of sequence-to-sequence modeling framework.
In this kind of sequence-to-sequence modeling framework,
often there is an encoder trying to encode context information
from the input sequence and a decoder to generate one item
of the output sequence at a time based on the context of both
input and output sequences. Besides, an additional component,
named attention, exists in between, deciding which parts of the
input sequence the decoder should pay attention in order to
choose which to output next. In other words, this attention
component calculates the context relevant to the decision of
the decoder at the considering time. Those components as a
whole constitute a large trainable neural architecture called
the famous attention-based encoder-decoder framework. This
framework becomes popular in many sequence-to-sequence
tasks.
In the ﬁeld of machine translation, using the attention-based
encoder-decoder framework is referred to as Neural Machine
Translation approach. First presented in [1], the encoder and
decoder in NMT are recurrent-based, which each hidden unit
in those components is a recurrent unit like Long Short-
term Memory (LSTM) [6] or Gated Recurrent Unit(GRU) [7].
Later, the encoder or decoder can also be a convolutional
architecture, as in [8]. Recently, [9] introduces transformer
architecture, in which both the encoder and decoder are a
special variant of attention mechanism, called self attention.
In this paper, we will brieﬂy explain the Recurrent NMT as
we utilize it in our experiments.
The Recurrent NMT model follows the attention-based ar-
chitecture proposed by [1]. The bidirectional recurrent encoder
reads every words xi of a source sentence x = {x1, ..., xn}
and encodes a representation s of the sentence into a ﬁxed-
length vector hi concatenated from those of the forward and
backward directions:
hi = [−→
h i, ←−
h i]
−→
h i = f(−→
h i−1, s)
←−
h i = f(←−
h i+1, s)
s = Es
• xi
Here xi is the one-hot vector of the word xi and Es
is the word embedding matrix which is shared across the
source words. f is the recurrent unit computing the current
hidden state of the encoder based on the previous hidden state.
hi is then called an annotation vector, which represent the
information of the source sentence up to the time i from both
forward and backward directions.
Those annotation vectors of the source sentences are com-
bined in the attention layers in a way that the resulted vector
encodes the source context relevant to the considering target
word the decoder should produce. Intuitively, a relevance
between the previous target word zj−1 and the annotation
vectors hi corresponding to the source words xi can be used
to form some attention scenario:
rel(zj−1, hi) = va
• tanh(Wa • zj−1 + Ua
• hi)
αij =
exp(rel(zj−1, hi))
P
i′ exp(rel(zj−1, hi′))
and cj =
X
i
αijhi
This speciﬁc attention mechanism, originally called align-
ment model in [1], has been employed as a simple feedforward
network with the ﬁrst layer is a learnable layer via adaptation
factors va,Wa and Ua. The relevance scores rel are then
normalized into attention weights αij and the context vector
cj is calculated as the weighted sum of all annotation vectors
hi. Depending on how much attention the target word at time
j put on the source states hi, a soft alignment is learned and a
source context cj at time j is calculated prior to the prediction
of the decoder.
Similar to the encoder, the recurrent decoder recursively
generates one target word yj to form a translated target
sentence y = {y1, ..., ym} in the end. At time j, it takes
the previous hidden state of the decoder zj−1, the previous
embedded word representation tj−1 and the time-speciﬁc
context vector cj as inputs to calculate the current hidden
state zj:
zj = g(zj−1, tj−1, cj)
tj−1 = Et • yj−1
Again, g is the recurrent activation function of the decoder
and Et is the shared word embedding matrix of the target
sentences.
Given the parallel corpus consisting of N training examples
{(x(n), y(n))}N
n=1, the objective is to maximize the condi-
tional log-probability of the correct translation given a source
sentence with respect to the parameters θ of the whole model:
L(θ) = arg max
θ
1
N
N
X
n=1
log p(y(n)|x(n), θ)
III. SUBWORD TRANSLATION
One of the most severe problems of NMT is dealing with the
rare words, which are not in the short lists of the vocabularies,
i.e. out-of-vocabulary (OOV) words, or do not appear in the
training set at all. On one hand, we would like to have fewer
OOV words by increasing the size of the short lists. On the
other hand, we need our neural network to learn fast and has
a good generalization capability on the unseen words as well.
As explained shortly in the introduction, for many lan-
guages, using subword instead of word as a translation unit
(TU) has been shown that it is not only effective on reducing
vocabulary sizes, thus alleviating the computing burden on


## Page 3


3
the large soft-max layer as well as reducing a substantial
number of parameters to be learnt, but also has the ability
to generate unseen words. In those languages, a word can
be a compound word or comprised by sub-components, each
has its own raw meaning or contains morphological infor-
mation. Segmenting words into sub-components allows NMT
to learn to translate them with considerably fewer data. For
example, it is deﬁnitely less chance to see this popular Ger-
man word “Wohnungsreinigung" (English equivalence: “house
cleaning”) than its sub-components “Wohnung” (i.e. “house”
or “ﬂat”) and “reinigung” (i.e. “cleaning”) in a middle-sized
German-English parallel corpus. Instead, NMT can observe
and translate those sub-components (“Wohnung” and “reini-
gung”) and combine their translations to generate the unseen
words (“house cleaning”). This is achieved by segmenting
words into subword units using segmentation techniques in
the preprocessing phase prior to translation. There are several
segmentation methods; Some are the complicate ones which
require linguistic resources or human-crafted rules. Thus, they
are not language-independent and expensive to obtain for low-
resourced languages.
Byte-Pair Encoding, otherwise, is a simple but robust tech-
nique to do subword segmentation. Since it is an unsuper-
vised and fast technique, it has great effects when applied
to build NMT systems for morphologically rich languages.
BPE is originally proposed in [10] as a data compression
technique by iteratively replaces the most frequent pair of
bytes in a sequence with a single, unused byte. [5] realized
Gage’s algorithm for word segmentation by merging frequent
characters inside a word instead of merging frequent pairs of
bytes in a whole ﬁle (sequence of bytes). Being applied in
translation from and to morphological rich languages, it can
automatically induce sub-components of a word (i.e. sequence
of characters) which bear some meaning or morphological
function without knowing much about linguistic characteristics
of those languages. Hence, the TU of the NMT used in those
languages is at a smaller level of word, i.e. subword.
On the other hand, Japanese and Vietnamese are different
to those languages in the way of how we consider a word.
In Vietnamese, the TU, normally considered as a word, which
often separated to each others by white spaces, is not a word in
linguistic term since it does not really have its own meaning.
Therefore, applying BPE to segment those TUs into smaller
units without any modiﬁcation is not suitable for Vietnamese.
In case of Japanese, there are no space to separate written texts
into TUs. Thus, for Vietnamese and Japanese as well as for
the languages having similar problem, before applying BPE,
it is necessary to have some preprocessing step to tokenize the
texts into words.
A. Vietnamese Tokenization
From the linguistic point of view, each sequence of char-
acters between two white spaces in Vietnamese texts cannot
be considered as a word since it does not always have a full
meaning to stand alone. For example, in the sentence “hôm
nay là sinh nhật của tôi” (English equivalence: “Today is my
birthday”), “hôm” and “nay” are not two words, they together
form a word, which means “today”. Nevertheless, “hôm” and
“nay” somehow still bear some meaning: “hôm”-“day”, “nay”-
“now”. Similarly, “sinh”-“birth” and “nhật”-“date” also form
the word “sinh nhật”-“birthday” but they are not two distinct
words. We could also call them subwords.
In many Vietnamese processing tasks such as Part-of-
Speech Tagging, Syntax Parsing or Chunking, there requires
a step to concatenate those subwords to make a word since
in those tasks, word is necessarily considered as the smallest
unit to be processed. This step is normally referred to as word
segmentation. There are various word segmentation methods;
The best ones are using machine learning approaches to learn
from a labeled corpus. It makes the tasks hard and expensive
to be applied in other domains. Furthermore, the translation
unit in Machine Translation does not need to be a word but
can be a subword or sequence of subwords if it have its own
meaning.
With this observation in mind, if we consider a subword,
i.e. the sequence of characters between two white spaces, as
a byte and a sentence as a sequence of bytes, we can apply
the BPE algorithm straight-forward: We iteratively ﬁnd and
concatenate the most frequent pair of subwords (w1,w2) and
replace it by an unseen subwords w1_w2. We do not merge
w1 with w1 if one of them are digits or punctuations or other
special symbols. The BPE learning algorithm has an arguments
which is the minimum value of frequency. In practice, we set
the minimum frequency is 2. Listing 1 presents this variant of
BPE, which we call VNBPE.
def
get_m os t_fre q_ p ai r ( text , min_freq ) :
d i c t = {}
dumpWord = { s et_of_s epa ra t e _s ym b ol s }
f o r
l i n e
in
t e x t :
w1 = t h e _ f i r s t _ w o r d _ i n _ t h e _ l i n e
f o r w2 = each_w ord_in_the_line :
i f w1 , w2 not
in dumpWord
and w1 i s
not a number :
d i c t [w1, w2] += 1
g e t _ n e x t _ p a i r _ i n _ t h e _ l i n e ( )
w1 = w2
r e t u r n
( a l l
p a i r s
has
freq
> min_freq )
def
u p d a t e _ p a i r s ( pair , text , c o d e s _ f i l e ) :
original_w ord
= p a i r [ 0 ] + " " + p a i r [ 1 ]
replaced_word = p a i r [ 0 ] + "_" + p a i r [ 1 ]
i n p u t _ f i l e . r e p l a c e ( rew , orw )
w r i t e _ r e p l a c e d _ w o r d _ t o _ c o d e s _ f i l e ( )
r e t u r n
i n p u t _ f i l e
### MAIN PART ###
min_freq =2
open ( i n p u t _ f i l e )
to
read
open ( c o d e s _ f i l e )
and
( o u t p u t _ f i l e )
to
w rite
p a i r s = get_m os t_fre q _p a i r ( i n p u t _ f i l e , min_freq )
a r r a n g e _ p a i r s _ f o r _ d e c r e a s i n g _ o f _ f r e q u e n c y ( )
f o r
each
( freq , p a i r )
in
p a i r s :
u p d a t e _ p a i r s ( pair , i n p u t _ f i l e , c o d e s _ f i l e )
o u t p u t _ f i l e = i n p u t _ f i l e
c l o s e _ a l l _ f i l e s ( )
The proposed variant of BPE for Vietnamese.
Compared to other word segmentation methods which require
training on labeled data, our VNBPE is a simple unsupervised
method, alike to its original BPE algorithm. Table I shows
the outputs of one decent word segmentation method and our


## Page 4


4
No.
Vietnamese phrases
Segmentation using pyvi’s algorithm
Segmentation using VN_BPE algorithm
1
sẽkết thúc
sẽkết_thúc
sẽ_kết_thúc
2
sựtập trung
sựtập_trung
sự_tập_trung
3
một đống
một đống
một_đống
4
vào lĩnh vực
vào lĩnh_vực
vào_lĩnh_vực
5
bằng máy bay
bằng máy_bay
bằng_máy_bay
Table I: Comparing a decent segmentation algorithm and VN_BPE.
VNBPE.
B. Japanese Tokenization
In a Japanese written text, there could be a mixture of three
different types of scripts: Chinese characters (kanji) and the
other two syllabic scripts: hiragana and katakana. Each of
kanji characters can be loosely considered as a subword that
we mentioned in the previous section. In the meanwhile, each
of hiragana or katakana characters can be considered as a latin
character in English or Vietnamese. In addition, there is no
space in the Japanese written texts to separate the characters,
either kanji, ,hiragana or katakana. So we cannot learn good
subwords from a small corpus by directly applying BPE or
the variant VNBPE on Japanese written texts. In order to learn
good subwords and with a little knowledge about Japanese, we
decided to use KyTea [11] to do Japanese word segmentation
and then apply Sennrich’s BPE on those word-segmented texts.
Some examples of the Japanese words going through the word
segmentation and BPE are shown in Table II.
Before BPE
After BPE
Vietnamese equi.
English equi.
受け入れる
受け入れる
Chấp nhận
Accept
崩れ落ちる
崩れ落ちる
Thu gọn
Collapse
姉ちゃん
姉ちゃん
Chịgái
Older sister
哀れん
哀れん
Đáng tiếc
Pity
取りかかる
取りかかる
Đểbắt đầu
To start
Table II: Examples of Japanese words after BPE.
IV. DATA AUGMENTATION
In this section, we describe the data augmentation methods
we use to increase the amount of training data in order to
make our NMT systems suffer less from the low-resourced
situation in Japanese ↔Vietnamese translation. Although
NMT systems can predict and generate the translation of
unseen words on their vocabularies, but they only perform
this well if the parallel corpus for training are sufﬁciently
large. For many under-resourced languages, unfortunately, it
hardly presents. In reality, although the monolingual data of
Vietnamese and Japanese are immensely available due to the
popularity of their speakers, the bilingual Japanese-Vietnamese
corpora are very limited and often in low quality or in narrowly
technical domains. Therefore, data augmentation methods to
exploit monolingual data for NMT systems are necessary to
obtain more bilingual data, thus upgrading the translating
quality.
A. Back Translation
One of the approaches to leverage the monolingual data is
to use a machine translation system to translate those data
in order to create a synthetic parallel data. Normally, the
monolingual data in the target language is translated, thus the
name of the method: Back Translation [12].
More speciﬁc, to generate the data for an X→Y NMT
system, we use the best Y→X translation system we have to
translate every sentence {yi} ∈Y in the monolingual data of
language Y into sentences {xi} ∈X in the source language
X. Then we pair {xi, yi} to get the synthetic data. Finally,
original bilingual data and synthetic data are mixed to train
our NMT from the start.
Back Translation can improve the estimate conditional
probability of the target word on the previous context words
through adding a bilingual data with approximate translations
to the source languages. Furthermore, the synthetic data might
contain some translation noise from the Back Translation
system, and if this noise is relevant, our NMT can be more
robust in learning how to translate noisy inputs. One the other
hand, if the quality of the Back Translation system is not
adequate, using the synthesis data might bring adverse effects
to our NMT.
In this paper, we subsample an amount of Vietnamese
monolingual data so that we can create a synthetic corpus
having the same size with the Japanese-Vietnamese parallel
corpus. In the end, the data we have is double in size compared
to the original one.
B. Mix-Source Approach
Another data augmentation method considered useful in
this low-resourced setting is the mix-source method [13].
In this method, we can utilize the monolingual data of the
target language in a multilingual NMT system by mixing the
original source sentences with those target monolingual data.
The multilingual framework then uses the share information
across source and target languages to improve the decision of
the target words to be chosen.
Speciﬁcally, there are a small parallel corpus XY of the lan-
guage pair X-Y which has n sentence pairs {xi, yi} (i = 1, n)
and a big monolingual corpus Y of the language Y which
has m sentences {aj} (j = 1, m, m ≫n). Now from the
monolingual corpus Y we can generate a parallel corpus Y Y
where we try to model the identical translation Y-Y: {aj, aj}
(j = 1, m). Then we mix XY and Y Y to get a parallel
corpus of the size m + n. Similar to the Back Translation,
we subsample n Vietnamese sentence pairs from the corpus
Y Y then the size of the parallel data we have is also doubled.


## Page 5


5
To let the NMT knows which language a certain source
sentence is in and then can model the language information,
we follows the conventions from [13]. We append language
tags to every word in both source and target sentences of
the mixed XY + Y Y corpus to indicate the language of
the words. This technique shows the effectiveness in low-
resourced scenarios [14], [15] and our Japanese↔Vietnamese
is such a scenario.
V. EXPERIMENTS
A. Data Preparation
We collected Japanese-Vietnamese parallel data from TED
talks extracted from WIT3’s corpus [16]. After removing blank
and duplicate lines we obtained 106758 pairs of sentences. The
validation set used in all experiments is dev2010 and the test
set is tst2010.
The data augmentation methods has been applied only for
the Japanese↔Vietnamese direction. For Back Translation, we
use Vietnamese monolingual data from VNESEcorpus of
DongDu2 which includes 349578 sentences. We shufﬂe the
lines of VNESEcorpus corpus and take out the ﬁrst 106758
sentences (the same as the number of sentence pairs in the
original parallel corpus). For Mix-Source, instead of using a
subsampled monolingual corpus, we use the Vietnamese part
of the Japanese-Vietnamese parallel corpus in order to learn
the multilingual information in the same domain. Our datasets
are listed in Table III.
Dataset
Description
Num. of sentences
Training
TED
106758
Back Translation data
Subsampled DongDu
106758
Mix-Source data
Vietnamese part of TED
106758
Validation
TED dev2010
568
Test
TED tst2010
1220
Table III: Statistics of the dataset used in our experiments
B. Preprocessing
After using KyTea to tokenize the Japanese texts, we learn
and apply Sennrich’s BPE from the tokenized texts. For
Vietnamese texts, ﬁrst we use Moses scripts3 to normalize
the texts from digits, punctuations and special symbols. We
use pyvi4 for Vietnamese word segmentation since it is one
of the best tools for this task in term of speed, robustness
and performance. On the other hand, we useVNBPE as
an alternative way of doing word segmentation. Those two
approaches are compared in an extrinsic evaluation of the
NMT systems employing them.
C. System Architecture and Training
We implement the translation systems using OpenNMT-py
framework5 [17]. Our system architecture includes two bi-
directional LSTM layers for the encoder and two LSTM layers
2http://viet.jnlp.org/download-du-lieu-tu-vung-corpus
3https://github.com/moses-smt/mosesdecoder/tree/master/scripts
4https://github.com/trungtv/pyvi
5https://github.com/OpenNMT/OpenNMT-py
for the decoder, each layer has the size of 512 hidden units.
The size of source and target embedding layers is also 512. We
use Adam optimizer [18] and learning rate annealing scheme
with the initial learning rate at 0.001. We train each systems
for 15 epochs with the batch size of 64. The best model in term
of the unigram accuracy on the validation set is usually used
to translate the test set with beam size of 16. Other settings
are the default settings of OpenNMT-py, otherwise already
noted.
D. Results
We evaluate the quality of translation of systems based
on different approaches mentioned in previous sections. The
multi-BLEU from Moses scripts is used. The results have
shown in the Table IV.
Baseline. For the baseline systems, the training data in-
cludes KyTea-segmented Japanese texts and pyvi-segmented
Vietnamese texts. For comparison purpose, we build two
baseline systems for each direction: one is use the traditional
phrase-based statistical machine translation (SMT), the other
one is the NMT system. Although our training set is small
but we ﬁnd that the NMT systems (2) are still more effective
than the phrase-based SMT models (1) in both translation
directions.
Subword
NMT.
We
applied
VNBPE
and
JPBPE
to
the
baseline’s
data
and
trained
NMT
systems.
On
Vietnamese↔Japanese, we observed an improvement of 0.6
BLEU points when we used our VNBPE (3) instead of the
pyvi’s word segmentation (2). Furthermore, when we trained
our NMT models using both BPE methods (4), we obtained a
bigger gain of 1.15 BLEU points. The similar improvements
can be found in the Japanese↔Vietnamese as well: 0.29
BLEU points between (3) and (2) and 0.57 BLEU points
between (4) and (3). This draws two conclusions: (i), despite
using an unsupervised Vietnamese word segmentation which
is fast, robust and does not require linguistic resources, our
NMT systems performed better than those systems employing
a complicate word segmentation method, (ii) BPE works
signiﬁcantly well for Japanese texts after we tokenized the
texts.
Data
Augmentation.
We
use
the
best
system
for
Vietnamese↔Japanese, which is the NMT systems trained
on BPE-processed texts, to generate the synthetic data
for Japanese↔Vietnamese translation. Although we achieved
some gain (from 9.04 to 9.39 BLEU points), the effective-
ness of Back Translation is not on par with its application
on the translation systems of other language pairs. Looking
into the Vietnamese↔Japanese translation of DongDu corpus
and its BLEU score, we speculate that it is because the
Vietnamese↔Japanese system is not good enough to produce
reasonable synthetic data. In the meanwhile, combining Back
Translation and Mix-Source brings a considerable improve-
ments of 0.6 BLEU points compared to not using them.
VI. RELATED WORKS
Japanese-Vietnamese MT is ﬁrstly mentioned in 2005 [19].
The authors focused on the difference from embedding struc-
tures between Japanese and Vietnamese, and then proposed


## Page 6


6
Vietnamese→Japanese
System
dev2010
tst2010
(1)
SMT Baseline
-
8.73
(2)
NMT Baseline
8.68
9.39
(3)
+ VNBPE
9.12
9.89
(4)
+ JPBPE
9.74
11.13
Japanese→Vietnamese
System
dev2010
tst2010
(1)
SMT Baseline
-
7.73
(2)
NMT Baseline
6.85
8.18
(3)
+ VNBPE
7.36
8.47
(4)
+ JPBPE
7.77
9.04
(5)
+ Back Translation
8.25
9.39
(6)
+ Mix-Source
8.56
9.64
Table IV: Evaluation of Japanese↔Vietnamese NMT systems.
rules for MT system and experiment on very small dataset
(714 Japanese embedding sentences). This approach is suitable
for small system applied in a speciﬁc domain or language, but
it is not easily extendable to other domains or languages due
to the expensiveness of building such rules.
The other previous work for Japanese→Vietnamese uses
SMT [20]. They also conducted the experiments on parallel
corpora collected from TED talks. They used phrase-based and
tree-to-string models and have shown that the SMT system
trained on French→Vietnamese obtains better results than the
system of Japanese→Vietnamese because French and Viet-
namese have more similarities in the structures of sentences
than between Japanese and Vietnamese. We also built phrase-
based systems on the TED data and achieved better BLEU
scores when using NMT.
Recently, some works use monolingual data to improve
the accuracy of NMT systems. [12] have shown signiﬁcant
improvements by using monolingual data on target-side to
generate synthetic data and then add them to original training
data. [21] have shown signiﬁcant improvements by "self-
learning" method to generate the target sentences based on
monolingual data on the source-side and then combined them
with original bilingual data to train. [13] convert monolingual
corpus on the target-side into a bitexts by copying target
sentences to the source sentence and then combined original
bilingual data together on training. Our systems employ those
approaches to exploit monolingual data and show the improved
performance for Japanese↔Vietnamese translations.
VII. CONCLUSION
We has built the ﬁrst Japanese↔Vietnamese NMT systems
and released the dataset as well as the associated training
scripts. We have also shown that the proposed VNBPE al-
gorithm can be used for Vietnamese word segmentation in
order to conduct neural machine translation. Furthermore, by
adapting Back Translation and Mix-Source, our NMT systems
achieved the best improvement on the dataset. In the future,
we will exploit more domain and multilingual information to
improve the quality of the systems.
VIII. ACKNOWLEDGMENTS
We would like to thank the center of High-performance
computing (HPC), University of Engineering and Technology,
VNU, Vietnam for allowing us to use their GPUs to perform
the experiments mentioned in the paper. We also thank the
anonymous reviewers for their careful reading of our paper
and insightful comments.
REFERENCES
[1] D. Bahdanau, K. Cho, and Y. Bengio, “Neural Machine Translation by
Jointly Learning to Align and Translate,” CoRR, vol. abs/1409.0473,
2014. [Online]. Available: http://arxiv.org/abs/1409.0473
[2] I. Sutskever, O. Vinyals, and Q. V. Le, “Sequence to sequence learning
with neural networks,” in Technical Report arXiv:1409.3215 [cs.CL],
Google. NIPS’2014, 2014.
[3] Y. Wu, M. Schuster, Z. Chen, Q. V. Le, M. Norouzi, W. Macherey,
M. Krikun, Y. Cao, Q. Gao, K. Macherey et al., “Google’s neural
machine translation system: Bridging the gap between human and ma-
chine translation,” in Transactions of the Association for Computational
Linguistics, vol. 5, pp. 339–351 2017.
[4] M. Cettolo, J. Niehues, S. Stüker, L. Bentivogli, R. Cattoni, and
M. Federico, “The IWSLT 2016 Evaluation Campaign,” in Proceedings
of the 13th International Workshop on Spoken Language Translation
(IWSLT 2016), Seattle, WA, USA, 2016.
[5] R. Sennrich, B. Haddow, and A. Birch, “Neural Machine Translation
of Rare Words with Subword Units,” in Association for Computational
Linguistics (ACL 2016), Berlin, Germany, August 2016.
[6] S. Hochreiter and J. Schmidhuber, “Long short-term memory,” Neural
Comput., vol. 9, no. 8, pp. 1735–1780, Nov. 1997. [Online]. Available:
http://dx.doi.org/10.1162/neco.1997.9.8.1735
[7] K. Cho, B. van Merrienboer, Ç. Gülçehre, F. Bougares, H. Schwenk,
and Y. Bengio, “Learning Phrase Representations using RNN Encoder-
Decoder for Statistical Machine Translation,” in Proceedings of Eighth
Workshop on Syntax, Semantics and Structure in Statistical Translation
(SSST-8.
Baltimore, ML, USA: Association for Computational Lin-
guistics, Jule 2014.
[8] J. Gehring, M. Auli, D. Grangier, and Y. Dauphin, “A convolutional
encoder model for neural machine translation,” in Proceedings of the
55th Annual Meeting of the Association for Computational Linguistics
(Volume 1: Long Papers), vol. 1, 2017, pp. 123–135.
[9] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez,
Ł. Kaiser, and I. Polosukhin, “Attention is all you need,” in Advances
in Neural Information Processing Systems, 2017, pp. 6000–6010.
[10] P. Gage, “A new algorithm for data compression,” in C Users J.,
12(2):23–38, February, 1994.
[11] G. Neubig, Y. Nakata, and S. Mori, “Pointwise prediction for robust,
adaptable japanese morphological analysis,” in Proceedings of the 49th
Annual Meeting of the Association for Computational Linguistics:
Human Language Technologies: short papers-Volume 2.
Association
for Computational Linguistics, 2011, pp. 529–533.
[12] R. Sennrich, B. Haddow, and A. Birch, “Improving Neural Machine
Translation Models with Monolingual Data,” in Association for Compu-
tational Linguistics (ACL 2016), Berlin, Germany, August 2016.
[13] T.-L.
Ha,
J.
Niehues,
and
A.
Waibel,
“Toward
multilingual
neural machine translation
with universal
encoder and decoder,”
Proceedings
of
the
13th
International
Workshop
on
Spoken
Language
Translation
(IWSLT
2016),
2016.
[Online].
Available:
http://arxiv.org/abs/1611.04798
[14] E. Cho, J. Niehues, T.-L. Ha, M. Sperber, M. Mediani, and A. Waibel,
“Adaptation and Combination of NMT Systems: The KIT Translation
Systems for IWSLT 2016,” in Proceedings of the 13th International
Workshop on Spoken Language Translation (IWSLT 2016), Seattle, WA,
USA, 2016.
[15] T.-L. Ha, J. Niehues, and A. Waibel, “Effective Strategies in Zero-Shot
Neural Machine Translation,” Proceedings of the 14th International
Workshop on Spoken Language Translation (IWSLT 2017), 2017.
[Online]. Available: http://arxiv.org/abs/1711.07893
[16] M. Cettolo, C. Girardi, and M. Federico, “Wit3: Web inventory of
transcribed and translated talks,” in Proceedings of the 16th Conference
of the European Association for Machine Translation (EAMT), Trento,
Italy, May 2012, pp. 261–268.
[17] G. Klein, Y. Kim, Y. Deng, J. Senellart, and A. M. Rush, “Opennmt:
Open-source toolkit for neural machine translation,” in Proc. ACL,
2017. [Online]. Available: https://doi.org/10.18653/v1/P17-4012
[18] D. Kingma and J. Ba, “Adam: A method for stochastic optimization,”
arXiv preprint arXiv:1412.6980, 2014.
[19] M. C. Nguyen and T. Ikeda, “Translating japanese-vietnamese machine
qualiﬁcation structure in machine translation,” Natural Language Pro-
cessing, vol. 12, no. 3, pp. 145–182, 2005.


## Page 7


7
[20] D. Do, M. Utiyama, and E. Sumita, “Machine translation from japanese
and french to vietnamese, the difference among language families,”
October 2015.
[21] Z. Zhang, S. Liu, M. Li, M. Zhou, and E. Chen, “Joint training for neural
machine translation models with monolingual data,” in Association
for the Advancement of Artiﬁcial Copyright Intelligence (AAAI 2018),
Louisiana, USA, February 2018.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
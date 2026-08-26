---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1910.05603
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1910.05603_VAIS_ASR__Building_a_conversational_speech_recognition_system_using_language_mod

> Source: 1910.05603_VAIS_ASR__Building_a_conversational_speech_recognition_system_using_language_mod.pdf

> Pages: 3

---


## Page 1


VAIS ASR: Building a conversational speech
recognition system using language model
combination
1st Quang Minh Nguyen
Vietnam Artiﬁcial Intelligence System
Hanoi, Vietnam
minhnq@vais.vn
2nd Thai Binh Nguyen
Vietnam Artiﬁcial Intelligence System
Hanoi University of Science and Technology
Hanoi, Vietnam
binhnguyen@vais.vn
3rd Ngoc Phuong Pham
Vietnam Artiﬁcial Intelligence System
Thai Nguyen University
Thai Nguyen, Vietnam
phuongpn@tnu.edu.vn
4th The Loc Nguyen
Vietnam Artiﬁcial Intelligence System
Hanoi University of Mining and Geology
Hanoi, Vietnam
locnguyen@vais.vn
Abstract—Automatic Speech Recognition (ASR) systems have
been evolving quickly and reaching human parity in certain cases.
The systems usually perform pretty well on reading style and
clean speech, however, most of the available systems suffer from
situation where the speaking style is conversation and in noisy
environments. It is not straight-forward to tackle such problems
due to difﬁculties in data collection for both speech and text. In
this paper, we attempt to mitigate the problems using language
models combination techniques that allows us to utilize both large
amount of writing style text and small number of conversation
text data. Evaluation on the VLSP 2019 ASR challenges showed
that our system achieved 4.85% WER on the VLSP 2018 and
15.09% WER on the VLSP 2019 data sets.
Index Terms—conversational speech, language model, combine,
asr, speech recognition
I. INTRODUCTION
Informal speech is different from formal speech, especially
in Vietnamese due to many conjunctive words in this language.
Building an ASR model to handle such kind of speech is
particularly difﬁcult due to the lack of training data and also
cost for data collection. There are two components of an
ASR system that contribute the most to the accuracy of it, an
acoustic model and a language model. While collecting data
for acoustic model is time-consuming and costly, language
model data is much easier to collect.
The language model training for the Automatic Speech
Recognition (ASR) system usually based on corpus crawled
on formal text, so that some conjunctive words which often
used in conversation will be missed out, leading to the system
is getting biased to writing-style speech.
In this paper, we present our attempt to mitigate the
problems using a large scale data set and a language model
combination technique that only require a small amount of
conversation data but can still handle very well conversation
speech.
II. SYSTEM DESCRIPTION
In this section, we describe our ASR system, which consists
of 2 main components, an acoustic model which models
the correlation between phonemes and speech signal; and a
language model which guides the search algorithm throughout
inference process.
A. Acoustic Model
We adopt a DNN-based acoustic model [1] with 11 hidden
layers and the alignment used to train the model is derived
from a HMM-GMM model trained with SAT criterion. In
a conventional Gaussian Mixture Model - Hidden Markov
Model (GMM-HMM) acoustic model, the state emission log-
likelihood of the observation feature vector ot for certain tied
state sj of HMMs at time t is computed as
log p(ot|sj) = log
M
X
m=1
πjmN(ot|sj)
(1)
where M is the number of Gaussian mixtures in the GMM
for state j and πjm is the mixing weight. As the outputs
from DNNs represent the state posteriors p(sj|ot), a DNN-
HMM hybrid system uses pseudo log-likelihood as the state
emissions that is computed as
log p(ot|sj) = log p(sj|ot) −log p(sj),
(2)
where the state priors log p(sj) can be estimated using the
state alignments on the training speech data.
arXiv:1910.05603v1  [cs.CL]  12 Oct 2019


## Page 2


B. Language Model
Our language model training pipeline is described in Fig-
ure 1. First, we collect and clean large amount of text data from
various sources including news, manual labeled conversation
video. Then, the collected data is categorized into domains.
This is an important step as the ASR performance is highly
depends on the speech domain. After that, the text is fed into
a data cleaning pipeline to clean bad tone marks, normalizing
numbers and dates.
For each domain text data, we train an n-gram language
model [2] that is optimized for that domain. As the results, we
have more than 10 language models. These language models
are combined based on perplexity calculated on a small text
of a domain that we want to optimize for.
In our system, the language model is used in 2 pass-
decoding. In the ﬁrst pass, the language model is combined
with acoustic and lexicon model to form a full decoding graph.
In this stage, the language model is typically small in size by
utilizing pruning method. In the second stage, we use a un-
pruned language model to rescore decoded lattices.
III. CORPUS DESCRIPTION
A. Speech data
Our speech corpus consists of approximately 3000 hours of
speech data including various domains and speaking styles.
The data is augmented with noise and room impulse respond
to increase the quantity and prevent over-ﬁtting.
B. Text data
To train n-gram language models that are robust to various
domains and, we collect corpus from many resources, mainly
is come from newspaper site (like dantri, vnexpress,..), law
document and some crawled repository1. In total, more than
50GB of text split to separate subjects was used to train n-gram
language models. Table I shows the statistic of the collected
data.
TABLE I
LANGUAGE MODEL DATASET
Domain
Vocab size
Cong nghe
269k
Doi song
285k
Giai tri
305k
Giao duc
135k
Khoa hoc
167k
Kinh te
291k
Phap luat
446k
Tin tuc
1.247k
Nha dat
24.97
The gioi
126k
The thao
216k
Van hoa
300k
Xa hoi
203k
Xe co
92k
1The text corpus is made available here https://github.com/binhvq/news-
corpus
IV. EXPERIMENTS
There are two different testing sets from VLSP 2018 and
VLSP 2019. In general, the data of this year is more complex
than the last year one, so there is a big gap in results between
two of them. The experiments are conducted using the Kaldi
speech recognition toolkit [3].
A. Evaluation data
• Testing data VLSP 2018: This dataset contains relatively
5 hours of short audio voices with 796 samples.
• Testing data VLSP 2019: The testing set in 2019 is quite
harder compare with the set in 2018. There are more
than 17 hours with 16,214 short audio samples. The set
is difﬁcult because audio contains more noise and having
more informal speaking style.
B. Single system evaluation
Table II shows the results on the VLSP 2019 test set with
two language models. Various language model weights were
also used to ﬁnd the optimal value for the test set. As we
can see, the conversation language model with the weight of
8 yielded the best single system of 15.47% WER.
TABLE II
EVALUATION OF THE SYSTEM WITH DIFFERENT LANGUAGE MODELS
LMWT
General LM
Conversation LM
7
18.85
15.67
8
20.05
15.47
9
22.11
15.78
10
24.97
16.72
C. System combination
To further improve the performance, we adopt system com-
bination on the decoding lattice level. By combining systems,
we can take advantage of the strength of each model that is
optimized for different domains. The results for 2 test sets is
showed on Table III and IV.
As we can see, for both test sets, system combination
signiﬁcantly reduce the WER. The best result for vlsp2018 of
4.85% WER is obtained by the combination weights 0.6:0.4
where 0.6 is given to the general language model and 0.4 is
given to the conversation one. On the vlsp2019 set, the ratio is
change slightly by 0.7:0.3 to deliver the best result of 15.09%.
V. CONCLUSION
In this paper, we presented our ASR system participated
in VLSP 2019 challenge that incorporates a language model
combination technique to handle conversation speech with
small amount of text data required. The method demonstrated
that it can help to reduce WER by 3% on the VLSP 2019
challenge.


## Page 3


Raw text domain 1
ngram_d1
ngram_tuning
ngram_final
Raw text domain 2
Raw text domain …
Raw text domain n
Spoken text
ngram_d2
ngram_d…
ngram_dn
ngram_spoken
Making
n-gram
model
Language model 
interpolation
Language model 
combine (50:50)
Fig. 1. Language model training pipeline
TABLE III
EVALUATION IN WORD ERROR RATE (WER) WITH VLSP 2018 SET
LMWT
General LM ratio
Conversation LM ratio
WER
7
0.3
0.7
5.08%
7
0.4
0.6
5.02%
7
0.5
0.5
4.94%
7
0.6
0.4
4.86%
7
0.7
0.3
4.90%
8
0.3
0.7
5.12%
8
0.4
0.6
5.02%
8
0.5
0.5
4.90%
8
0.6
0.4
4.85%
8
0.7
0.3
4.93%
9
0.3
0.7
5.26%
9
0.4
0.6
5.17%
9
0.5
0.5
5.04%
9
0.6
0.4
5.07%
9
0.7
0.3
5.09%
10
0.3
0.7
5.64%
10
0.4
0.6
5.52%
10
0.5
0.5
5.37%
10
0.6
0.4
5.37%
10
0.7
0.3
5.37%
REFERENCES
[1] V. Peddinti, D. Povey, and S. Khudanpur, “A time delay neural network
architecture for efﬁcient modeling of long temporal contexts,” in Sixteenth
Annual Conference of the International Speech Communication Associa-
tion, 2015.
[2] P. F. Brown, P. V. Desouza, R. L. Mercer, V. J. D. Pietra, and J. C.
Lai, “Class-based n-gram models of natural language,” Computational
linguistics, vol. 18, no. 4, pp. 467–479, 1992.
[3] D. Povey, A. Ghoshal, G. Boulianne, L. Burget, O. Glembek, N. Goel,
M. Hannemann, P. Motlicek, Y. Qian, P. Schwarz et al., “The kaldi
speech recognition toolkit,” in IEEE 2011 workshop on automatic speech
recognition and understanding, no. CONF.
IEEE Signal Processing
Society, 2011.
TABLE IV
EVALUATION IN WER WITH VLSP 2019 SET
LMWT
General LM ratio
Conversation LM ratio
WER
7
0.5
0.5
15.55%
7
0.6
0.4
15.18%
7
0.7
0.3
15.15%
7
0.8
0.2
15.26%
8
0.5
0.5
15.88%
8
0.6
0.4
15.27%
8
0.7
0.3
15.09%
8
0.8
0.2
15.10%
9
0.5
0.5
16.83%
9
0.6
0.4
16.06%
9
0.7
0.3
15.67%
9
0.8
0.2
15.55%
10
0.5
0.5
18.47%
10
0.6
0.4
17.40%
10
0.7
0.3
16.85%
10
0.8
0.2
16.60%

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
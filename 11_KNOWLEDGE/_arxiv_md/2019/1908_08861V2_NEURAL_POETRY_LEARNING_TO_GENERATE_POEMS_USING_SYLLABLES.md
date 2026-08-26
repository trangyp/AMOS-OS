---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1908.08861v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1908.08861v2_Neural_Poetry__Learning_to_Generate_Poems_using_Syllables

> Source: 1908.08861v2_Neural_Poetry__Learning_to_Generate_Poems_using_Syllables.pdf

> Pages: 13

---


## Page 1


Neural Poetry: Learning to
Generate Poems using Syllables⋆
Andrea Zugarini1,2, Stefano Melacci2, and Marco Maggini2
1 DINFO, University of Florence, Italy
2 DIISM, University of Siena, Italy
andrea.zugarini@unifi.it, {mela,maggini}@diism.unisi.it
Abstract. Motivated by the recent progresses on machine learning-
based models that learn artistic styles, in this paper we focus on the
problem of poem generation. This is a challenging task in which the ma-
chine has to capture the linguistic features that strongly characterize a
certain poet, as well as the semantics of the poet’s production, that are
inﬂuenced by his personal experiences and by his literary background.
Since poetry is constructed using syllables, that regulate the form and
structure of poems, we propose a syllable-based neural language model,
and we describe a poem generation mechanism that is designed around
the poet style, automatically selecting the most representative gener-
ations. The poetic work of a target author is usually not enough to
successfully train modern deep neural networks, so we propose a multi-
stage procedure that exploits non-poetic works of the same author, and
also other publicly available huge corpora to learn syntax and grammar
of the target language. We focus on the Italian poet Dante Alighieri,
widely famous for his Divine Comedy. A quantitative and qualitative
experimental analysis of the generated tercets is reported, where we in-
cluded expert judges with strong background in humanistic studies. The
generated tercets are frequently considered to be real by a generic pop-
ulation of judges, with relative diﬀerence of 56.25% with respect to the
ones really authored by Dante, and expert judges perceived Dante’s style
and rhymes in the generated text.
Keywords: Poem Generation · Transfer Learning · Language Models ·
Recurrent Neural Networks · Natural Language Generation.
1
Introduction
Natural Language Generation (NLG) is a challenging problem that has drawn a
lot of attention in the Natural Language Processing (NLP) community [15,17].
NLG is crucial for multiple NLP applications and problems, such as dialogue
systems [20], text summarization [4], and text paraphrasing [7]. Poem generation
⋆This
is
a
post-peer-review,
pre-copyedit
version
of
an
article
published
in
LNCS, volume 11730. The ﬁnal authenticated version is available online at:
https://doi.org/10.1007/978-3-030-30490-4 26
arXiv:1908.08861v2  [cs.CL]  24 Sep 2019


## Page 2


2
A. Zugarini, S. Melacci, M. Maggini
is an instance of NLG that is particularly fascinating for its peculiar features.
Verses have precise structures, rhyme and meter that convey an aesthetic and
rhythmic sound to the poetry. This expressive art of language is ancient and
spread across all cultures in the world.
Automatically creating poems requires a strong attention to both the content
and the form. The machine has to capture the linguistic features that strongly
characterize a certain poet, as well as the semantics of the poet’s production, that
are inﬂuenced by their personal experiences and by their literary background. In
the last few years, the machine learning community focussed on the problem of
poem generation, proposing approaches that generate either English quatrains
[5,8,10] or Chinese verses [24,23,21,22]. Most of them are based on neural ar-
chitectures that combine several modules, post-processing the ﬁnal results to
generate well-formed verses (we postpone to Section 2 an in-depth description
of related work). In order to cope with the lack of large scale data, these works
usually do not try to mimic the style of a target poet, and they frequently con-
sider the poetic production of several authors. Moreover, despite Italian poetry
is one of the most signiﬁcant and well known poetries, to the best of our knowl-
edge it has not been the subject of studies in which neural approaches have been
evaluated.
In this paper, we propose a simple and eﬀective neural network-based model
to generate verses. We focus on the Italian language and, in particular, on Dante
Alighieri, the Italian poet that authored the Divine Comedy [2], the most impor-
tant poem of the Middle Ages, widely considered as the greatest literary work in
the Italian literature. Our model learns to generate tercets with Dante Alighieri’s
style by “reading” the Divide Comedy. The learning problem is tacked follow-
ing Language Modeling tasks but, diﬀerently from what is commonly done by
several authors, we consider syllables as input tokens (instead of words, generic
n-grams, or characters, for example). This choice is motivated by the fact that
poetry is constructed using syllables that regulate the form and structure of
poems. For example, syllables play a crucial role in the context of meter and
rhyme. Moreover, the use of sub-word information is even more useful in Italian
that is a language with a rich morphology. Our model consists of a Recurrent
Neural Network (LSTM [18]) that outputs one syllable at each time instant,
conditioned to the previously generated text. The model is trained on Dante’s
tercets, that are composed of triples of hendecasyllables, with a precise structure
of the rhymes. Due to its syllable-based nature, the proposed model can capture
several properties of the input language, and it has a large ﬂexibility in terms
of what it can generate. The latter feature requires attention when using the
language model to generate new text. We take into account the key properties
of the Divine Comedy, automatically selecting the generations that are closer to
Dante’s style.
Training neural models on poems from a single target author can lead to
low generalization quality, due to the small size of the training data. Moreover,
the language used by poets from the middle ages can be signiﬁcantly diﬀerent
from modern language, such as in the case of the Italian used by Dante Alighieri


## Page 3


Neural Poetry: Learning to Generate Poems using Syllables
3
and nowadays Italian. We exploit the basic consideration that even if the form of
some words have changed over time, there are a number of inherent regularities at
the syllable level that have not changed that much. We propose to pre-train the
system with a large modern Italian corpus (PAISA’ [11]), and to perform transfer
learning towards the poetry domain. The transfer of information is performed
in multiple steps, exploiting Dante’s prose and other Dante’s poems (i.e. all the
poet’s production), and ﬁnally training the model with the Divine Comedy.
Our experimentation shows that exploiting Italian corpora and the poet’s
production improves the perplexity of the poetry-related language model, al-
lowing the system to better capture the language and contents of the Divine
Comedy. We performed a qualitative analysis of the generated tercets, based on
human evaluation, where we also asked the collaboration of expert judges with
strong background in humanistic studies. The generated tercets are frequently
considered to be real by a generic population of judges, and expert judges per-
ceived Dante’s style and rhymes in the generated text. As expected, evaluators
emphasized how the semantics behind the generated verses are sometimes hard
to appreciate since they do not convey enough emotion, suggesting that more
structured models that integrate additional information about the author could
be an interesting topic for future work.
The paper is organized as follows. In Section 2 we describe related state-of-
the-art approaches. Then, we introduce the proposed model and the generation
mechanism in Section 3. Section 4 includes experiments and a discussion on the
obtained results, while, ﬁnally, we draw our conclusions in Section 5.
2
Related Work
The scientiﬁc literature includes several works on machines that are either pro-
grammed to generate poems or that approach the problem of poem generation
using machine learning algorithms. Early methods [5] rely on rule-based solu-
tions, while more recent approaches focus on learnable language models. Lan-
guage Modeling is the problem of predicting which word comes next, given a
sequence of previous words. In the last few years, neural language models are
the dominant class of algorithms applied to NLG. While Language Modeling was
successfully addressed using feed-forward neural networks on a ﬁxed window of
words [3], in [13] a recurrent neural network approach proved to be preferable.
As a matter of fact, several nowadays NLG approaches are based on recurrent
nets [20,4,7].
Word-based language models usually require large vocabularies to store all
the (most frequent) words in huge textual corpora, and, of course, they cannot
generalize to never-seen-before words. Some other approaches tried to overcome
this issue, exploiting sub-word information. A character-level solution was pro-
posed in [9], while other authors [14] combine word embeddings with character-
level representations. It has been shown [12,1] that character-based models can
be adapted to produce powerful word and even context representations that cap-


## Page 4


4
A. Zugarini, S. Melacci, M. Maggini
ture both morphology and semantics. Sub-word information is very important
in poetry, since it represents a crucial element to capture the “form” of a poem.
The ﬁrst approach that proposes a deep learning-based solution to poem
generation is described in [24], where the authors combined convolutional and
recurrent networks to generate Chinese quatrains. Then, a number of approaches
focussing on Chinese poetry were proposed. In particular, a sequence-to-sequence
model with attention mechanisms was proposed in [21] and [19]. In [23] the au-
thors extend Generative Adversarial Networks (GANs) [6] to the generation of
sequences of symbols, exploiting Reinforcement Learning (RL). They consider
the GAN discriminator to be the reward signal of a RL-based generator, and,
among a variety of tasks, Chinese quatrains generation is also addressed. Another
RL-based approach is proposed in [22], where two networks learn simultaneously
from each other with a mutual RL scheme, to improve the quality of the gener-
ated poems.
In the context of English poem generation, transducers were exploited to
generate poetic text [8]. Meter and rhyme are learned from characters by cas-
cading a module that focusses on the content and a weighted state transducer
that explicitly models the form of the generation. Diﬀerently, the more recent
Deep-speare [10] combines three neural modules, sharing the same character-
based representation, to generate English quatrains. These models consist in a
word-level language model fed with both word and character representations, a
network that learns the meter, and another net that identiﬁes rhyming pairs.
At the end, generations are selected after a post-processing step that picks the
best quatrains combining the output of the three modules. We notice that the
authors of [10] exploited a collection of poems from several authors in order to
train the model.
Following the intuition of working with syllables, our solution is simpler and
in the case of Italian poetry, as we will show in Section 4, it generates tercets not
only with the proper form, but also resembling the style of the selected target
author.
3
Model
The main module of the proposed model consists of a syllable-based Language
Model, also referred to as sy-LM, that processes a sequence of syllables. In order
to handle the input data, we have to convert the available text into a sequence
of syllables, i.e., we have to segment the input text into words, and then to split
words into syllables. Since we focus on the Italian language, we implemented
a module that follows the most common Italian hyphenation rules that, apart
from rare exceptions, correctly divides words into syllables (the same procedure
could have been followed for other languages, English included).
We focus on data from Dante Alighieri’s Divine Comedy, that is composed
of a set of tercets (i.e., three verses). Each tercet is converted into a sequence
of tokens (syllables) x1, · · · , xT belonging to the syllable dictionary Vsy. We


## Page 5


Neural Poetry: Learning to Generate Poems using Syllables
5
removed the punctuation and introduced some special tokens: word-separator
<sep>, begin-of-tercet <go>, end-of-verse <eov>, end-of-tercet <eot>.
For each time instant t, sy-LM outputs the probability
ˆyt = p(xt|x1, · · · , xt−1)
for all xt ∈Vsy. If we indicate with ˆyt the vector with the probabilities associated
to all the vocabulary elements, the model yields the syllable associated with the
highest probability.
We follow the classic setting of neural network-based language models: each
element of the vocabulary is encoded into a 1-hot representation of size |Vsy|, and
the system associates it to a latent dense representation that is learned jointly
with the other model parameters. Such dense representations, also referred to as
“syllable embeddings”, are collected row-wise in matrix Wsy ∈R|Vsy |×d. Each
token xt of the input tercet is then mapped into its syllable embedding et ∈Rd,
that is the row of Wsy associated to xt. In detail, we have,
et = Wsy · 1(xt) ,
where 1(·) is a function returning the 1-hot column vector that has 1 in the
position associated to the vocabulary index of its argument. It is important
to notice that since Vsy is the set of all syllables (and a few special tokens),
its cardinality is smaller than traditional word-based vocabularies, therefore the
embedding matrix Wsy has a signiﬁcantly smaller number of elements than what
usually happens in the case of word-level representations.
The sequence of syllable embeddings of the input tercet is provided as input
to a recurrent neural network, one element at each time step. The internal state
of the recurrent network at time t is indicated with ht, and it is computed by
updating the previous state using the current syllable embedding,
ht = r(et, ht−1) ,
(1)
where r(·, ·) is the state-update function of the network. We selected LSTMs as
recurrent neural model, due to their good results in language modeling [18].
A projection layer (weights W, bias b, activation σ – that we set to the hyper-
bolic tangent) transforms ht into a d-sized vector zt, and a dense layer followed
by the softmax activation function computes the probability distribution ˆyt,
zt = σ(Wht + b)
(2)
ot = W ′
syzt
(3)
ˆyt = softmax(ot) .
(4)
Notice that the dense layer of Eq. (3) shares its parameters with the syllable
embedding matrix Wsy (being ′ the transpose operator), ulteriorly reducing the
number of learnable parameters of the model.
We train the sy-LM by minimizing the cross-entropy between each ˆyt and
the ground truth from the Divine Comedy, thus pushing toward 1 the element


## Page 6


6
A. Zugarini, S. Melacci, M. Maggini
of ˆyt associated to the t-th syllable of the current tercet in the Divine Comedy.
We measure the model performance in terms of perplexity (PPL), as commonly
done in language modeling approaches [13]. An illustration of the entire model
is presented in Fig. 1.
LSTM
LSTM
LSTM
...
nel
hyphenation 
module 
Nel mezzo del cammin di nostra vita 
mi ritrovai per una selva oscura 
ché la diritta via era smarrita. 
<sep>
ri
ta
mez
zo
LSTM
LSTM
LSTM
...
...
<sep>
mez
zo
<sep>
ta
<eot>
<go>
LSTM
nel
Fig. 1. Sketch of the Syllable LM. Input tercets are ﬁrst pre-processed by a module
that splits words into syllables and introduces some special tokens: word-separator
<sep>, begin-of-tercet <go>, end-of-verse <eov>, end-of-tercet <eot>. Orange blocks
are syllable embeddings, each blue block depicts the network of Eq. (2-4). The system
predicts the next syllable, i.e. the one associated to the largest probability in ˆyt.
3.1
Multi-Stage Transfer Learning
Learning from the Divine Comedy (or, more generally, from a single poem or
from all the poems of a given target author) might not be enough to provide
strong generalization skills to neural language models (≈4, 000 tercets). For
this reason, we follow a multi-stage training procedure that consists in sequen-
tially pre-training our model with related data, before training it on the Divine
Comedy. We want the model to deeply grasp most of the syntax and grammar
of the Italian language, independently from the considered author, so that we
pre-train the network using publicly available large Italian corpora (see Section
4). Dante Alighieri lived in the middle ages, and he wrote the Divine Comedy
in Tuscan/Florentine Italian dialect of that time, giving a strong contribute in
creating the currently standard language for Italy. His language is slightly diﬀer-
ent from modern Italian, including some old-fashioned words and forms not used
anymore. Word-level models are likely to fail due to the unavoidable changes in
the vocabulary when moving from modern Italian to Dante’s Italian. Diﬀerently,
our syllable-based vocabulary is ﬂexible enough to be transferred to related data.
The transition toward the Divine Comedy can be made smoother by performing
a further pre-training step using all Dante’s production (poems and prose), thus
allowing the network to get more information on the main linguistic features of
the author. Finally, we train the model on the Divine Comedy.


## Page 7


Neural Poetry: Learning to Generate Poems using Syllables
7
3.2
Poem Generation Procedure
Once sy-LM has been trained, it is directly exploited to generate new samples,
i.e., new tercets. We start with h0 set to zeros, and we feed the system with the
<go> input symbol, iteratively sampling the next token to generate. We follow
a Monte Carlo sampling procedure as done in [23]. We keep sampling and gener-
ating tokens until the end-of-tercet symbol (<eot>) is generated or the number
of syllables reaches a ﬁxed maximum limit (75 in our experiments). Thanks to
the randomness in the multinomial sampling, the system can generate multiple
diﬀerent sequences sampled from the distribution learned from the training data.
We generate a batch of tercets (2,000 in our experiments), and we assign
a score R(x) ∈R to each tercet x of the batch. Those tercets with highest
scores are selected among all the generated ones (only the top-scored generation,
if the goal is to generate a single tercet). R(x) is the average of 4 diﬀerent
scores, R1(x), . . . , R4(x) ∈R that are based on known properties of the author
of the Divine Comedy, in terms of form and language. In particular, tercets are
composed of three hendecasyllables, with chained rhyming scheme (“ABA” – the
ﬁrst tercet is paired with the last one), and the words produced by the syllable-
based generation must belong to the vocabulary used in the Divine Comedy.
The ﬁrst score penalizes non-tercet-like generations,
R1(x) = −abs(|x| −3) + 1 ,
(5)
where |x| indicates the number of verses in the tercets and abs is the absolute
value function. Diﬀerently, R2(x) promotes sequences with verses in x that follow
an hendecasyllabic meter. Since our model is based on syllables, it is easy to count
the number of syllables in a generated verse v, and we deﬁne R2 as follows,
R2(x) = −
X
v∈x
(abs(|v| −11)) + 1 .
(6)
The chained rhyming scheme is measured by R3(x),
R3(x) =
(
1,
if (v1, v3), v1, v3 ∈x are in rhyme
−1,
otherwise
,
(7)
where a positive score is given when a tercet has ﬁrst verse v1 in rhyme with
the third one v3. Since the generated x is actually a sequence of syllables, words
are identiﬁed by merging syllables until the word-separator token <sep> is pre-
dicted. In order to avoid the generation of words that are far from the poet’s
style – that is pretty unlikely in our experience –, we assign a small positive
contribute a to words in x that belong to the vocabulary of the Divine Comedy.
Formally,
R4(x) =
X
w∈x
fw(x), fw(xi) =
(
a,
if w ∈V
−b,
otherwise
(8)
where w indicates a word in tercet x. In the experiments a was set to 0.05 and
b to 1 to strongly discourage not valid words.


## Page 8


8
A. Zugarini, S. Melacci, M. Maggini
4
Experiments
We performed several experiments to assess the quality of the sy-LM, reporting
both quantitative and qualitative results. We considered multiple data sources
(i., ii., iii. below), following the multi-stage learning procedure of Section 3.1.
The core of this work is the Divine Comedy, the most important Dante Alighieri’s
contribution.
(i.) The Divine Comedy (DC). It is a poem composed of 100 “cantos” organized
into three cantiche. Each canto is a poem with a variable number of tercets also
known as “Dante’s tercet”. sy-LM was trained on 3768 tercets and evaluated on
a test set of 472. We also kept a validation set of 471 to set the network hyper-
parameters. Overall, there are about 180k syllables in the Divine Comedy.
(ii.) Modern Italian Dataset (PAISA’). We exploited PAISA’,1 a large corpus
of Italian web texts. We considered a portion of 200k documents, consisting of
about 836k sentences with more than 67M syllables.
(iii.) Dante’s Production (DP). We collected most of Dante’s known non-latin
prose and poetry manuscripts. In particular, we gathered all the text from Con-
vivio, Le rime and La vita nuova, collecting overall 1752 sentences (∼157k
syllables) for prose and 2727 verses (∼48k syllables).
In order to select the hyper-parameters of the neural architecture we mea-
sured the perplexity (PPL) of several conﬁgurations on the validation set taken
from the DC corpus. We found that the best performing size d for the syllable
embeddings was 300, whereas the best size of the state of the LSTM was 1024.
State neurons were dropped out [16] with probability 0.3. The size of Vsy was set
to 1884, including all the syllables in the Divine Comedy and the special tokens.
When pre-training on PAISA’ and then reﬁning on DP (Section 3.1), we kept
a small validation set to decide when to early stop the learning procedure, and
diﬀerent batch sizes and learning rates have been validated. Best results occurred
with batch size 32 and learning rate of 0.001.
4.1
Results
We experimented the transfer learning procedure of Section 3.1, evaluating the
impact of the diﬀerent data sources. In Table 1 we report our results (PPL) on
both validation and test set data. As expected, the model beneﬁts from pre-
training on additional data. In particular, the most signiﬁcant improvement is
given when pre-training on PAISA’, showing that there is a positive transfer
of information from modern Italian to Dante’s language. Moreover, despite the
quantity of data in DP is still rather small, we can see further improvements
when other Dante’s productions are used to pre-train the model.
The quality of the generated tercets has been assessed by human judges
in two diﬀerent evaluations. In the ﬁrst test, we involved 13 graduate and not
graduated students, mostly from humanistic degrees. We refer to them as “non-
expert” judges, since they were not specialized in Dante’s production, but very
1 http://www.corpusitaliano.it/en/contents/paisa.html


## Page 9


Neural Poetry: Learning to Generate Poems using Syllables
9
Table 1. Perplexity on validation and test set data from the Divine Comedy, pre-
training (or not) the model using multiple data. A →B means that we train on data
A ﬁrst, and then we train on data B.
Datasets
Val PPL Test PPL
DC
12.45
12.39
PAISA’ →DC
10.83
10.82
DP →DC
11.95
11.74
PAISA’→DP →DC
10.63
10.55
well aware of the author and of the Divine Comedy. They were asked to judge if a
given tercet was authored by Dante Alighieri or not (i.e., generated by sy-LM).
Each judge evaluated 10 tercets, 5 of which were from Dante and 5 generated
by our model. In Table 2 we report the number of times (percentages) that
tercets from a certain population were judged to be authored by Dante. It is
clear that, given the humanistic background of the evaluators, judgements are
rather thoughtful, however our generated tercets are considered as real almost
half of the times of ones from Dante, with a relative diﬀerence of 56.25%.
Table 2. The number of times (percentages) that tercets from either sy-LM or Dante
Alighieri (Poet) are judged to be authored by Dante (i.e., they were marked as “real”).
Our model is considered to be realistic almost half of the times of real Dante’s produc-
tion.
Generator Real-Mark
sy-LM
28%
Poet
64%
We can further analyze this result by distinguishing between those judges
that were less capable of identifying real Dante’s tercets (marking them to be
real less than 50% of the times) and the other ones. In Figure 2 we can observe
that the “less-capable judges” were even more attracted by sy-LM than by
real Dante’s tercets. Since these judges better represent the average population
of users, this result suggests that sy-LM is very positively perceived. On the
other hand, more capable evaluators are less frequently fooled by sy-LM with a
relative diﬀerence of ≈67% from Dante.
In another experiment, we involved 4 expert judges with academic experi-
ences on Dante Alighieri’s production. Each expert evaluated 20 tercets, scoring
(from 0 to 5) diﬀerent properties of each of them: emotion, meter, rhyme, read-
ability and adherence to the author’s style. In particular, 10 tercets were gen-
erated by sy-LM and 10 were extracted from the Divine Comedy. Judges were
not aware of how tercets were distributed. We report the test results in Table 3.
Dante’s tercets are better scored, of course, however, we observe a good evalua-
tion of the quality of the rhymes produced by sy-LM. Considering that judges
know very well Dante Alighieri, it is interesting to see that they are experienc-


## Page 10


10
A. Zugarini, S. Melacci, M. Maggini
less-capable-judges
more-capable-judges
0
20
40
60
Real-Mark
sy-LM
Poet
Fig. 2. Results of Table 2 further divided into two groups: judges that are less capable
of recognizing real Dante’s tercets and the other ones.
ing some of the author’s style in the generated tercets. Evaluators emphasized
how the semantics behind the generated verses are sometimes hard to appreci-
ate since they do not convey enough emotion, that is the motivation behind the
lower scores on the ﬁrst two columns of Table 3. Finally, judges applied very
strict criteria in evaluating the meter, giving low scores whenever a small inco-
herence with Dante’s meter was apparently detected, even if they reported that
it was not far from the ideal case.
Table 3. Experts evaluations restricted to tercets generated by sy-LM. Votes vary
from 0 to 5. The average rate is also reported. For comparisons, in the last line we also
report the average rate in the case of Dante’s real tercets (Poet).
Readability Emotion Meter Rhyme Style
Judge 1
1.57
1.21
1.57
3.36
2.29
Judge 2
1.64
1.45
1.73
3.00
2.27
Judge 3
2.83
2.33
2.00
4.17
2.92
Judge 4
2.17
2.00
2.33
2.92
2.50
Average
2.04
1.73
1.90
3.37
2.49
Poet (Average)
4.34
3.87
4.45
4.50
4.34
Finally, we report some examples of generated tercets in Table 4. The ﬁrst
three tercets were well rated by non-expert and also expert judges, while the
last one was badly scored.
5
Conclusions
We presented a syllable-based language model for poem generation, that was
applied to generate tercets. The proposed model is general, and we studied it
in the context of Italian language and, in particular, in Dante Alighieri’s Di-
vine Comedy. Despite its simplicity and the lack of large-scale collections of
data from the target author, our model produces tercets that are considered real


## Page 11


Neural Poetry: Learning to Generate Poems using Syllables
11
Table 4. Examples of generated tercets. The last one (bottom right) never fooled the
judges, whereas the ﬁrst three tercets were marked as real Dante’s tercets by 88.00%,
55.56% and 45.45% of the evaluators, respectively.
e tenendo con li occhi e nel mondo
che sotto regal facevan mi novo
che ’l s’apparve un dell’altro fondo
in questo imaginar lo ’ntelletto
vive sotto ’l mondo che sia fatto moto
e per accorger palude dritto stretto
per lo mondo che se ben mi trovi
con mia vista con acute parole
e s’altri dicer fori come novi
non pur rimosso pome dal sospetto
che ’l litigamento mia come si lece
che per ammirazion di dio subietto
by evaluators with humanistic background roughly half of the times of Dante’s
verses. This is due to a scored generation mechanism that helps to keep Divine
Comedy’s meter and rhyme, and also due to a multi-stage training procedure
that improves the quality of the content, exploiting all the poet’s production
and text in modern Italian. However, the outcome of the evaluation from expert
judges clearly showed that, while the rhyme and style are positively captured
by the model, the generations are still weak on meter and on conveying enough
emotion. In future work we plan to exploit the scoring criteria that we used in
generating text to setup a Reinforcement Learning strategy. We are also inter-
ested in exploring more structured models that include additional information
about the author, to improve the emotional quality of the generations.
Acknowledgments
We thank Emmanuela Carb´e and Elisabetta Bartoli for providing us Dante’s
data and for inviting several evaluators of our model. We would also like to
thank Monica Marchi, Irene Tani, Maria Rita Traina and Simonetta Teucci,
that helped us in evaluating the model. This research was partially supported
by QuestIT s.r.l. in the framework of the joint laboratory SAINLab.
References
1. Akbik, A., Blythe, D., Vollgraf, R.: Contextual string embeddings for sequence
labeling. In: Proceedings of the 27th International Conference on Computational
Linguistics. pp. 1638–1649 (2018)
2. Alighieri, D., Sisson, C., Sisson, C., Higgins, D.: The Divine Comedy. Oxford Uni-
versity Press, Oxford University Press (1998)
3. Bengio, Y., Ducharme, R., Vincent, P., Jauvin, C.: A neural probabilistic language
model. Journal of machine learning research 3(Feb), 1137–1155 (2003)
4. Chopra, S., Auli, M., Rush, A.M.: Abstractive sentence summarization with at-
tentive recurrent neural networks. In: Proceedings of the 2016 Conference of the
NAACL: Human Language Technologies. pp. 93–98 (2016)
5. Colton, S., Goodwin, J., Veale, T.: Full-face poetry generation. In: ICCC. pp. 95–
102 (2012)


## Page 12


12
A. Zugarini, S. Melacci, M. Maggini
6. Goodfellow, I., Pouget-Abadie, J., Mirza, M., Xu, B., Warde-Farley, D., Ozair,
S., Courville, A., Bengio, Y.: Generative adversarial nets. In: Advances in neural
information processing systems. pp. 2672–2680 (2014)
7. Hasan, S.A., Lee, K., Datla, V., Qadir, A., Liu, J., Farri, O., et al.: Neural para-
phrase generation with stacked residual lstm networks. In: International Conference
on Computational Linguistics: Technical Papers. pp. 2923–2934 (2016)
8. Hopkins, J., Kiela, D.: Automatically generating rhythmic verse with neural net-
works. In: Proceedings of the 55th Annual Meeting of the Association for Compu-
tational Linguistics (Volume 1: Long Papers). vol. 1, pp. 168–178 (2017)
9. Hwang, K., Sung, W.: Character-level language modeling with hierarchical recur-
rent neural networks. In: Acoustics, Speech and Signal Processing (ICASSP), 2017
IEEE International Conference on. pp. 5720–5724. IEEE (2017)
10. Lau, J.H., Cohn, T., Baldwin, T., Brooke, J., Hammond, A.: Deep-speare: A joint
neural model of poetic language, meter and rhyme (2018)
11. Lyding, V., Stemle, E., Borghetti, C., Brunello, M., Castagnoli, S., Dell’Orletta,
F., Dittmann, H., Lenci, A., Pirrelli, V.: The paisa’ corpus of italian web texts. In:
9th Web as Corpus Workshop (WaC-9)@ EACL 2014. pp. 36–43. EACL (2014)
12. Marra, G., Zugarini, A., Melacci, S., Maggini, M.: An unsupervised character-aware
neural approach to word and context representation learning. In: International
Conference on Artiﬁcial Neural Networks. pp. 126–136. Springer (2018)
13. Mikolov, T., Karaﬁ´at, M., Burget, L., ˇCernock`y, J., Khudanpur, S.: Recurrent
neural network based language model. In: Eleventh annual conference of the inter-
national speech communication association (2010)
14. Miyamoto, Y., Cho, K.: Gated word-character recurrent language model. In: Pro-
ceedings of the 2016 Conference on Empirical Methods in Natural Language Pro-
cessing. pp. 1992–1997 (2016)
15. Reiter, E., Dale, R.: Building natural language generation systems. Cambridge
university press (2000)
16. Srivastava, N., Hinton, G., Krizhevsky, A., Sutskever, I., Salakhutdinov, R.:
Dropout: a simple way to prevent neural networks from overﬁtting. The Journal
of Machine Learning Research 15(1), 1929–1958 (2014)
17. Subramanian, S., Rajeswar, S., Dutil, F., Pal, C., Courville, A.: Adversarial gener-
ation of natural language. In: Proceedings of the 2nd Workshop on Representation
Learning for NLP. pp. 241–251 (2017)
18. Sundermeyer, M., Schl¨uter, R., Ney, H.: Lstm neural networks for language mod-
eling. In: Thirteenth annual conference of the international speech communication
association (2012)
19. Wang, Q., Luo, T., Wang, D., Xing, C.: Chinese song iambics generation with
neural attention-based model. In: Proceedings of the Twenty-Fifth International
Joint Conference on Artiﬁcial Intelligence. pp. 2943–2949. AAAI Press (2016)
20. Wen, T.H., Gasic, M., Mrkˇsi´c, N., Su, P.H., Vandyke, D., Young, S.: Semantically
conditioned lstm-based natural language generation for spoken dialogue systems.
In: Proceedings of the 2015 Conference on Empirical Methods in Natural Language
Processing. pp. 1711–1721 (2015)
21. Yi, X., Li, R., Sun, M.: Generating chinese classical poems with rnn encoder-
decoder. In: Chinese Computational Linguistics and Natural Language Processing
Based on Naturally Annotated Big Data, pp. 211–223. Springer (2017)
22. Yi, X., Sun, M., Li, R., Li, W.: Automatic poetry generation with mutual rein-
forcement learning. In: Proceedings of the 2018 Conference on Empirical Methods
in Natural Language Processing. pp. 3143–3153 (2018)


## Page 13


Neural Poetry: Learning to Generate Poems using Syllables
13
23. Yu, L., Zhang, W., Wang, J., Yu, Y.: Seqgan: Sequence generative adversarial nets
with policy gradient. In: Thirty-First AAAI Conference on Artiﬁcial Intelligence
(2017)
24. Zhang, X., Lapata, M.: Chinese poetry generation with recurrent neural networks.
In: Proceedings of the 2014 Conference on Empirical Methods in Natural Language
Processing (EMNLP). pp. 670–680 (2014)

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1908_08861v2_neural_poetry_learning_to_generate_poems_using_syllables
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1908_08861V2_NEURAL_POETRY_LEARNING_TO_GENERATE_POEMS_USING_SYLLABLES.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

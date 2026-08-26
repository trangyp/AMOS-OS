---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1904.12213v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1904.12213v1_Towards_Recognizing_Phrase_Translation_Processes__Experiments_on_English-French

> Source: 1904.12213v1_Towards_Recognizing_Phrase_Translation_Processes__Experiments_on_English-French.pdf

> Pages: 12

---


## Page 1


arXiv:1904.12213v1  [cs.CL]  27 Apr 2019
Towards Recognizing Phrase Translation Processes:
Experiments on English-French
Yuming Zhai⋆, Pooyan Safari⋆, Gabriel Illouz, Alexandre Allauzen, and Anne Vilnat
LIMSI-CNRS, Univ. Paris-Sud, Univ. Paris-Saclay, France
{firstname.lastname}@limsi.fr
Abstract. When translating phrases (words or group of words), human transla-
tors, consciously or not, resort to different translation processes apart from the
literal translation, such as Idiom Equivalence, Generalization, Particularization,
Semantic Modulation, etc. Translators and linguists (such as Vinay and Darbel-
net, Newmark, etc.) have proposed several typologies to characterize the different
translation processes. However, to the best of our knowledge, there has not been
effort to automatically classify these ﬁne-grained translation processes. Recently,
an English-French parallel corpus of TED Talks has been manually annotated
with translation process categories, along with established annotation guidelines.
Based on these annotated examples, we propose an automatic classiﬁcation of
translation processes at subsentential level. Experimental results show that we
can distinguish non-literal translation from literal translation with an accuracy of
87.09%, and 55.20% for classifying among ﬁve non-literal translation processes.
This work demonstrates that it is possible to automatically classify translation
processes. Even with a small amount of annotated examples, our experiments
show the directions that we can follow in future work. One of our long term
objectives is leveraging this automatic classiﬁcation to better control paraphrase
extraction from bilingual parallel corpora.
Keywords: Translation processes · Non-literal translation · Automatic classiﬁ-
cation
1
Introduction
Since 1958, translators and linguists have published work on translation processes [35,23,8,22].
They distinguish literal translations from other translation processes at subsentential
level. Consider these two human non-literal translation examples: the ﬁrst translation
preserves exactly the meaning, where the ﬁxed expression à la hauteur de ‘to the height
of’ has a ﬁgurative sense which means capable of solving; while the second one is more
complicated, there exists a textual inference between the source text and the translation.
(1.EN) a solution that’s big enough to solve our problems
(1.FR) une solution à la hauteur de nos problèmes
(2.EN) and that scar has stayed with him for his entire life
(2.FR) et que, toute sa vie, il a souffert de ce traumatisme
(‘he has suffered from this traumatism’)
Non-literal translations can bring difﬁculties for automatic word alignment [11,10],
or cause meaning changes in certain cases. However, to the best of our knowledge, there
⋆Both authors contributed equally to this article.


## Page 2


has not been effort to automatically classify these ﬁne-grained translation processes to
beneﬁt downstream natural language processing tasks. For example, Machine Trans-
lation (MT) techniques have been leveraged for paraphrase extraction from bilingual
parallel corpora [1,20]. The assumption is that two monolingual segments are potential
paraphrases if they share common translations in another language. Currently the largest
paraphrase resource, PPDB (ParaPhrase DataBase) [12], has been built following this
method. Nonetheless, Pavlick et al. [26] revealed that there exist other relations (i.e.
Entailment (in two directions), Exclusion, Other related and Independent)1 than strict
equivalence (paraphrase) in PPDB. Non-literal pivot translations inside the parallel cor-
pora could break the strict equivalence between the candidate paraphrases extracted,
whereas they have not received enough attention during this corpora exploitation.
From a linguistic point of view, apart from the word-for-word literal translation,
different versions of human translations reﬂect the richness of human language expres-
sions, where various translation processes could be employed. Furthermore, because
of the existing differences between languages and cultures, non-literal translation pro-
cesses are sometimes inevitable to produce correct and natural translations. The ﬁne-
grained phrase-level translation processes could help foreign language learners to better
compare the language being learned with another language already mastered.
Based on the theories developed in translation studies and through manually anno-
tating and analyzing an English-French parallel corpus, Zhai et al. [37] have proposed a
typology of translation processes adapted to their corpus. In this work our main contri-
bution is proposing an automatic classiﬁcation of translation processes at subsentential
level, based on these annotated examples. From the aspect of granularity and our goal
of better controlling paraphrasing process or helping foreign language learners, it is
different from the task of ﬁltering semantically divergent parallel sentence pairs to im-
prove the performance of MT systems [6,36,29]. Experimental results show that we can
distinguish non-literal translation processes from literal translation with an accuracy of
87.09%, and 55.20% for classifying among non-literal multi-classes.
In the present paper, after reviewing related work, we describe the manual annota-
tion and the data set. Exploited features and different neural network architectures will
be presented, followed by experimental results and error analysis. Finally we conclude
and present the perspectives of this work.
2
Related Work
Translators and linguists have proposed several typologies to characterize different
translation processes. Vinay and Darbelnet [35] identiﬁed direct and oblique transla-
tion processes, the latter being employed when a literal translation is unacceptable, or
when structural or conceptual asymmetries arising between the source language and the
target language are non-negligible. Following studies include, among others, the work
of Newmark [23,24], Chuquet and Paillard [8]. More recently, Molina and Hurtado Al-
bir [22] proposed their own categorization based on studying the translation of cultural
elements in the novel A Hundred Years of Solitude from Spanish to Arabic.
1 Exclusion: X is the contrary of Y; X is mutually exclusive with Y. Other related: X is related
in some other way to Y. (e.g. country / patriotic). Independent: X is not related to Y.
2 / 12


## Page 3


Non-literal translations or cross-language divergences have been studied to improve
MT related techniques. In order to enable more accurate word-level alignment, Dorr et
al. [11] proposed to transform English sentence structure to more closely resemble an-
other language. A translation literalness measure was proposed to select appropriate
sentences or phrases for automatically constructing MT knowledge [15]. Using a hi-
erarchically aligned parallel treebank, Deng and Xue [10] semi-automatically identify,
categorize and quantify seven types of translation divergences between Chinese and En-
glish.2 Based on the syntactic and semantic similarity between bilingual sentences, Carl
and Schaeffer [5] developed a metric of translation literality. We have drawn inspiration
from these preceding work for our feature engineering.
Recently, different models have been proposed to automatically detect translation
divergence in parallel corpora, with the goal of automatically ﬁltering out divergent
sentence pairs to improve MT systems’ performance. An SVM-based cross-lingual di-
vergence detector was introduced [6], using word alignments and sentence length fea-
tures. Their following work [36] proposed a Deep Neural Network-based approach.
This system could be trained for any parallel corpus without any manual annotation.
They conﬁrmed that these divergences are a source of performance degradation in neu-
ral machine translation. Pham et al. [29] built cross-lingual sentence embeddings ac-
cording to the word similarity with a neural architecture in an unsupervised way. They
measure the semantic equivalence of a sentence pair to decide whether to ﬁlter it out.
Another task studying human translations concerns automatic post-editing [7]. The
aim is evaluating systems for automatically correcting translation errors of an unknown
“black box” MT engine, by learning from human revisions of translations produced by
the same engine. Evaluation metrics include TER [31], BLEU [25] and manual evalua-
tion. The task that we propose here is different from these attempts, which either ﬁlter
semantically divergent sentence pairs to improve the performance of MT systems; or
automatically correct machine translation errors to improve the translation quality. Our
task of classifying translation processes (in two classes or in multi-classes) at subsen-
tential level is a stand-alone task. One of our long term objectives is leveraging this
automatic classiﬁcation to better control phrase-level paraphrase extraction from bilin-
gual parallel corpora.
3
Manual Annotation and Data Description
In order to model translation choices made by human translators at subsentential level,
Zhai et al. [37] have annotated a trilingual parallel (English-French, English-Chinese)
corpus of TED Talks3 with translation processes. The corpus is composed of transcrip-
tions and human translations of oral presentations. The inter-annotator agreement (Co-
hen’s Kappa) [9] for annotating the English-French and English-Chinese control corpus
is 0.67 and 0.61, both around the substantial agreement threshold. This indicates that
the task of manual annotation is already complicated. Readers can ﬁnd more details of
corpus construction in the article [37].
2 Lexical encoding; difference in transitivity; absence of language-speciﬁc function words; dif-
ference in phrase types; difference in word order; dropped elements; structural paraphrases.
3 https://www.ted.com/
3 / 12


## Page 4


The automatic classiﬁcation is conducted on the English-French pair in this work.
We present in the table 1 a brief deﬁnition, a typical example and the number of in-
stances for each category to be automatically classiﬁed.4 We combine Transposition
and Mod+Trans in a category Contain_Transposition, where Modulation is considered
as a neutral part. We will work on the classiﬁcation of the pair English-Chinese once
the annotation phase is ﬁnished. In this work, we conduct experiments in a simpliﬁed
scenario, where we already know the boundaries of bilingual pairs, and we only predict
the translation process. For example, given the pair deceptive →une illusion in a pair
of bilingual sentences, the goal is to predict its label Contain_Transposition.
Table 1: Deﬁnition, typical example and number of instances for each translation
process to be automatically classiﬁed. The instances were manually annotated in
an English-French parallel corpus of TED Talks. We combine Transposition and
Mod+Trans in a category Contain_Transposition for the automatic classiﬁcation.
Translation Process Deﬁnition and typical example
Literal
Word-for-word translation, also concerns lexical units in multiword form.
(3771)
certain kinds of →certains types de
Equivalence
Non-literal translation of proverbs or ﬁxed expressions; a word-for-word
translation makes sense but the translator expresses differently, without
changing the meaning and the grammatical classes.
(289)
back then →à l’époque (‘at that time’)
Generalization
Several source words or expressions could be translated into a more
general target word or expression, the translator uses the latter to translate.
(86)
as we sit here in ... →alors que nous sommes à ... (‘as we are at ...’)
Particularization
The source word or expression could be translated into several target
words or expressions with a more speciﬁc meaning, and the translator
chooses one of them according to the context.
(215)
the idea I want to put out is ... →l’idée que je veux diffuser c’est ... (‘the
idea I want to spread is ...’)
Modulation
Metonymical and grammatical modulation [8]; change the point of view;
the meaning could be changed.
(195)
that scar has stayed with him →il a souffert de ce traumatisme (‘he has
suffered from this traumatism’)
Transposition
Change grammatical classes without changing the meaning.
(289)
unless something changes →à moins qu’un changement ait lieu (‘unless
a change occurs’)
Mod+Trans
Combine the transformations of Modulation and of Transposition, which
could make the alignment difﬁcult.
(53)
this is a completely unsustainable pattern →il est absolument impossible
de continuer sur cette tendance (‘it is completely impossible to continue
on this trend’)
4 Note that there are other detailed annotation rules in the annotation guidelines.
4 / 12


## Page 5


4
Automatic Classiﬁcation
We have tried two approaches for the automatic classiﬁcation. Since the size of the
cross validation data set is quite small, we ﬁrst compare different statistical machine
learning techniques with feature engineering. We also build different neural network
architectures which we explain below.
4.1
Feature Engineering with Statistical Machine Learning Techniques
We describe below the features exploited in this work. The tag sets of English and
French for part-of-speech (PoS) tagging, constituency parsing and dependency parsing
have been converted into three compact and uniﬁed tag sets [28].
1) The PoS tagging is done by Stanford CoreNLP [21] for the two languages. On
source and target side, for each PoS tag, the number of its occurrence is counted in a
vector. We also calculate the cosine similarity between these two vectors (on all words
and only on content words).5
2) We verify the pattern of PoS tag sequence changing according to a manual list,
for example the pair methodologically →de façon méthodologique ‘methodologically’
corresponds to the pattern ADV →ADP NOUN ADJ.
3) The number of tokens in the two segments (le, lf), the ratio of these numbers
(le/lf, lf/le), the distance Levenshtein [18] between the segments.
4) The constituency parsing is done by Bonsai [4] for French, by Stanford CoreNLP
for English. We compare the PoS tags for a pair of words, the non-terminal node tags
for a pair of segments, the tag category (e.g. verb →verb phrase) for a word translated
by a segment or vice versa.
5) The dependency parsing is done by Stanford CoreNLP for the two languages.
Inside the segments, the number of occurrence of each dependency relation is counted.
Outside the segments, among the words linked at source and target side, we ﬁlter those
which are aligned in the sentence context. Then the number of occurrence of each de-
pendency relation between the words in segments and these context words is counted.
6) The cosine similarity is calculated between the embeddings from ConceptNet
Numberbatch [32]. This resource is multilingual and the system based on ConceptNet
took the ﬁrst place in the task “Multilingual and Cross-lingual Semantic Word Sim-
ilarity” of SemEval2017 [3,33]. Certain multi-word expressions have their own em-
beddings in this resource. Otherwise, we calculate the average of embeddings only on
content words. The same features are calculated for lemmatized segments.6
7) The resource ConceptNet [32] also provides assertions in triplet: a pair of words
or expressions linked by a relation. In this multilingual resource, we verify if an English-
French pair is directly linked; indirectly linked by another French segment or simply not
linked.7 Three forms are tested: original form, lemmatized form and lemmatized ﬁltered
form.8
5 The tags of content words include: ADJ, ADV, NOUN, PROPN, VERB. If a segment does not
contain any content word, the original segment is used.
6 The lemmatization is done by Stanford CoreNLP and Tree Tagger [30] for English and French.
7 The EN-FR and FR-FR assertions are used in this work.
8 We ﬁlter the words in a manual list, for example the light verbs, determinants, pronouns, etc.
5 / 12


## Page 6


8) On the lemmatized ﬁltered form, we calculate the percentage of tokens which
are linked with a relation of derivation, based on the resource ConceptNet. For example
deceptive and illusion ‘illusion’ are not directly linked in the resource, but they are both
linked to illusoire ‘illusory’. Hence we consider that there exists a link of derivation
between them.
For the three following features, we have exploited the lexical translation probabil-
ity table generated by the statistical word alignment tool Berkeley Word Aligner [19],
trained on an English-French parallel corpus composed of TED Talks and a part of
Paracrawl corpus (in total 1.8M parallel sentence pairs and 41M English tokens).9
9) The entropy of the distributions of lexical translation probabilities [13,5], calcu-
lated according to this equation: H(X) = P
i P(xi)I(xi) = −P
i P(xi)logeP(xi).
We calculate the average entropy on content words. A bigger entropy indicates that
the words have more general meanings or they are polysemous. The same feature is
calculated on the lemmatized content words.
10) The bidirectional lexical weighting on content words, by supposing a n-m align-
ment a between the segments (¯e and ¯f). In the scheme proposed by Koehn et al. [16]
(equation 1), to calculate the direct lexical weighting, each of the English words ei is
generated by aligned foreign words fj with the word translation probability w(ei|fj).
And similarly for the reverse lexical weighting lex( ¯f|¯e, a). The same feature is calcu-
lated for lemmatized content words. This feature could reﬂect the alignment conﬁdence
between a pair of segments.
lex(¯e| ¯f, a) =
length(¯e)
Y
i=1
1
|{j|(i, j) ∈a}|
X
∀(i,j)∈a
w(ei|fj)
(1)
11) The sum of lexical translation probability differences between the human trans-
lation and the most probable translation according to the probability table. For each
source word, we take the target word in human translation with the biggest probability.
According to this method, we also count the unaligned words to calculate a ratio on the
total number of tokens on each side. These features are calculated in the two directions
of translation.
We use the toolkit Scikit-Learn [27] to train different statistical machine learning
classiﬁers.10
4.2
End-to-end Neural Network Architectures
The source and target phrases are encoded using a bidirectional encoder with Gated
Recurrent Unit (GRU) (size 10). The outputs of forward and backward recurrent net-
works are concatenated to form the source and target phrase representations (size 20).
After the encoder layer we have tried two different architectures. The ﬁrst one is to
build an alignment matrix for the source-target phrases, using the dot product of the
two representations, inspired by these two work [17,29]. Then a Convolutional Neural
9 https://wit3.fbk.eu/, https://paracrawl.eu/index.html
10 The code and data set is publicly available at https://github.com/YumingZHAI/ctp.
6 / 12


## Page 7


Network (CNN) classiﬁer is applied to this alignment matrix, which is composed of one
convolution layer followed by pooling. Since the shape of the alignment matrix varies
from one source-target pair to another, an adaptive pooling is used [14]. The output of
the pooling layer is fed into a fully-connected layer followed by a linear layer as the
output. In the second architecture, the source and target outputs of the encoder layer
are averaged over time steps to produce two ﬁxed-dimensional vectors, which are fur-
ther concatenated (size 40) and fed into a Multi-layer Perceptron (MLP) classiﬁer. The
hidden layer of MLP includes 10 hidden units with tanh non-linearity.
The length of our phrases is usually short, especially for word-for-word Literal
instances. In order to build a more robust alignment matrix and to avoid the out-of-
vocabulary problem, we ﬁnally choose to use character embeddings. As shown in ta-
ble 2, for the embedding layer, we have tried respectively randomly initialized character
embeddings (size 10), and training our own word embeddings using skipgram model of
FastText [2] on a TED Talks corpus (around 3M tokens for both English and French),
with a word-embedding size of 100, minimum n-gram of 3, and maximum n-gram of 6.
All the models have been trained in 200 epochs, with a learning rate of 0.0001 using
Adam optimizer and the minibatch size of 20. Dropout has been applied to all layers
except the output and embedding layers.
5
Experimental Results and Analysis
The table 2 and 3 show the results of our classiﬁers using end-to-end neural network
architectures, for binary classiﬁcation (balanced distribution) and multi-class classiﬁ-
cation. For the binary classiﬁcation, Non_literal (NL) class has in total 1127 instances,
and 1127 Literal (L) instances are randomly chosen. Besides the preprocessing steps
of lowercasing and correcting minor spelling errors, for the neural classiﬁers, we also
normalized the clitic forms to complete words (e.g. ’re →are), and normalized digits
to letter form (e.g. 42 →four two). The architecture using word embeddings and MLP
obtain better results and is faster than the other two architectures. However, the current
data set is too small for neural architectures to produce satisfactory results.
Table 2: Binary classiﬁcation
(balanced distribution)
Architecture Accuracy F1 (L)
F1 (NL)
Randomly initialized character embedding
CNN
59.99%
0.60
0.60
MLP
71.16%
0.71
0.71
Pre-trained fasttext word embedding
MLP
71.25%
0.71
0.71
Table 3: Multi-class classiﬁcation
(ﬁve non-literal classes)
Architecture Accuracy Micro-F1 Macro-F1
Randomly initialized character embedding
CNN
34.08%
0.34
0.20
MLP
40.74%
0.41
0.34
Pre-trained fasttext word embedding
MLP
43.22%
0.43
0.34
The number of all non-literal instances (1127) is only one third of Literal instances
(3771). Considering this important difference, for the statistical machine learning clas-
siﬁers, we ﬁrst evaluated them under these conﬁgurations:
- six classes (Literal, Equivalence, Generalization, Particularization, Modulation,
Contain_Transposition). We ﬁrst put all Literal instances. Then to have an approxi-
mately balanced class distribution, we randomly take 200 instances for Literal.
7 / 12


## Page 8


- two classes (Literal and Non_literal), with three distributions (3:1, 2:1, 1:1). The
distribution 3:1 is the natural distribution in the data set. The instances of Literal have
been extracted randomly for the last two distributions.
- ﬁve classes (only non-literal categories).
For each conﬁguration, we have tuned the hyperparameters of different classiﬁers.
We evaluate them by ﬁve-fold cross-validation,11 using the metrics such as the average
accuracy of ﬁve folds, the micro average and macro average F1-score [34]. The Dum-
myClassiﬁer is used as a baseline, which generates random predictions by respecting
the distribution of training classes.
First, we attempted a direct classiﬁcation into six classes (see table 4). The best
results by RandomForest reﬂect the difﬁculty of the task in multi-classes. On the other
hand, we observe the potential of our features on classifying the category Literal when
the number of instances increases. As a result, we decide to divide the problem: conduct
ﬁrst a binary classiﬁcation, and secondly a multi-class classiﬁcation among the non-
literal categories.
Table 4: Classiﬁcation results under different conﬁgurations, using all features
Distribution of classes
Classiﬁer
Accuracy Micro-F1 Macro-F1
Six classes
six classes, with 3771 Literal
Dummy
60.76%
0.61
0.15
RandomForest 83.10%
0.83
0.44
six classes, with 200 Literal
Dummy
18.92%
0.19
0.16
RandomForest 57.04%
0.57
0.52
Two classes
Literal (3) : Non_literal (1)
Dummy
65.84%
0.66
0.52
RandomForest 90.16%
0.90
0.86
Literal (2) : Non_literal (1)
Dummy
56.43%
0.56
0.51
RandomForest 88.85%
0.89
0.88
Literal (1) : Non_literal (1)
Dummy
53.19%
0.53
0.53
RandomForest 87.09%
0.87
0.87
Five classes
Five non-literal classes
Dummy
20.32%
0.20
0.18
RandomForest 55.10%
0.55
0.47
For the binary classiﬁcation, the two best classiﬁers are RandomForest and MLP.
Furthermore, RandomForest has better performance than the two combined by the
method hard voting or soft voting. The table 4 presents the results under three different
class distributions. From the natural distribution (3:1) to our artiﬁcial balanced distribu-
tion by randomly choosing Literal instances (thus both class have 1127 instances), the
average F1-score for the class Non_literal increases from 0.78 to 0.88. We will continue
to test this tendency when a larger data set is available. Table 4 also shows the results
for the classiﬁcation into ﬁve non-literal classes using all features, and the average F1-
score for each non-literal category are shown in table 5. The category Generalization
11 StratiﬁedKFold is used for cross-validation, where the folds are made by preserving the per-
centage of samples for each class.
8 / 12


## Page 9


has many fewer instances than the other categories, which need to be augmented; there
exist many confusions between Modulation and the other categories, which suggests
rather a review of annotation guidelines.
Table 5: Average F1-score for each non-literal class, using all features
Category
Equivalence Generalization Particularization Modulation Contain_Transposition
Nb. instances
289
86
215
195
342
Average F1
0.51
0.25
0.56
0.36
0.68
The table 6 recapitulates the best performance on binary classiﬁcation (balanced
distribution) and on the classiﬁcation of ﬁve non-literal classes, using the most helpful
set of features. With the best performing classiﬁer RandomForest, we have investigated
the performance of features one by one and also grouped them: PoS_tagging (feature 1,
2), surface (feature 3), syntactic_analysis (feature 4, 5), external_resource (feature 6,
7, 8) and word_alignment (feature 9, 10, 11). For binary classiﬁcation, feature 10 (bidi-
rectional lexical weighting) is most helpful, which generates average F1-score of 0.78
for Literal and 0.80 for Non_literal by itself. The group of features word_alignment
contributes the most for the binary classiﬁcation. The combination of all features gen-
erates the best results, which remain the same if we remove the feature 4 (constituency
parsing), 7 (how the pair is linked in the resource ConceptNet) and the features on PoS
tagging apart from the vector counting the occurrence of each tag. The features in ﬂoat
form generally perform better than those in discrete form (e.g. 0, 1, etc.). Concerning
the classiﬁcation into ﬁve non-literal classes, the combination of all features except the
group external_resource leads to the best results, where the group PoS_tagging and
syntactic_analysis contribute more than the group word_alignment and surface. The
accuracy changes from 55.10% to 55.20% after feature ablation (see table 4).
Our error analysis shows that in binary classiﬁcation, it is difﬁcult to distinguish
Literal and Equivalence; in multi-class classiﬁcation, the biggest confusion is between
Equivalence and Contain_Transposition. Consequently, we conducted another three bi-
nary classiﬁcation experiments (see table 7), where in all conﬁgurations each class has
549 instances to make the results comparable: i) Literal vs Non_literal ii) Literal com-
bined with Equivalence (E), vs the other classes iii) Literal combined with Equivalence
and Transposition (T), vs the other classes. The third conﬁguration is more interesting,
because the group of translation processes LET do not bring meaning changes, while
the processes non-LET could. The results show that by including Transposition (change
grammatical classes without changing the meaning), the performance gets better than
only grouping Literal and Equivalence, since we avoid the confusion between Equiv-
alence and Transposition. The better results of binary classiﬁcation (L vs NL, LET vs
non-LET) indicate that in future work we can develop cascading classiﬁers, namely
ﬁrst separating word-for-word literal translations, or those which do not cause meaning
changes, then conducting a ﬁner-grained classiﬁcation among the other categories.
6
Conclusion and Perspectives
We have proposed a new Natural Language Processing task of automatically classify-
ing translation processes at subsentential level, based on manually annotated examples
9 / 12


## Page 10


Table 6: Classiﬁcation results after feature ablation study
average accuracy
average F1-scores
binary classiﬁcation
(balanced distribution)
87.09%
0.87 (Literal)
0.88 (Non_literal)
ﬁve non-literal classes
55.20%
0.55 (micro average) 0.48 (macro average)
Table 7: Classiﬁcation results after grouping classes, every class has 549 instances
Conﬁguration
average accuracy average F1 (class1) average F1 (class2)
Dummy
48.63%
0.49
0.49
L vs NL
85.24%
0.84
0.86
LE vs non-LE
75.32%
0.74
0.77
LET vs non-LET
79.42%
0.78
0.81
from a parallel English-French TED Talks corpus. To the best of our knowledge, these
translation processes have not been explicitly exploited during paraphrase extraction
from bilingual parallel corpora. With the best performing classiﬁer RandomForest and
feature engineering, our empirical results show a best accuracy of 87.09% for binary
classiﬁcation (Literal vs Non_literal) and 55.20% for multi-class classiﬁcation (Equiv-
alence, Generalization, Particularization, Modulation, Contain_Transposition), which
are much better than the baseline random classiﬁer.
This task is complicated, and our exploratory work is restrained by the limited
amount of annotated examples. However, our work demonstrates that automatically
classifying translation processes seem possible, and the experiments show the direc-
tions that we can follow in future work. There is much room to constitute an augmented
and balanced data set, on which we will evaluate our classiﬁer to observe the perfor-
mance. The ﬁner error analysis of the classiﬁcation results is useful to help the research
on corpus annotation and linguistic analysis. We will continue to improve the classiﬁer
on English-French, by implementing other features for multi-class classiﬁcation, and
explore more neural architectures. We will also extend our work to English-Chinese
translation pairs. One of our long term objectives is leveraging this automatic classiﬁ-
cation to better control paraphrase extraction from bilingual parallel corpora.
References
1. Bannard, C., Callison-Burch, C.: Paraphrasing with bilingual parallel corpora. In: Proceed-
ings of the 43rd Annual Meeting on Association for Computational Linguistics. pp. 597–604.
Association for Computational Linguistics (2005)
2. Bojanowski, P., Grave, E., Joulin, A., Mikolov, T.: Enriching word vectors with subword in-
formation. Transactions of the Association for Computational Linguistics 5, 135–146 (2017)
3. Camacho-Collados, J., Pilehvar, M.T., Collier, N., Navigli, R.: Semeval-2017 task 2: Multi-
lingual and cross-lingual semantic word similarity. In: Proceedings of the 11th International
Workshop on Semantic Evaluation (SemEval-2017). pp. 15–26. Association for Computa-
tional Linguistics (2017). https://doi.org/10.18653/v1/S17-2002
4. Candito, M., Nivre, J., Denis, P., Anguiano, E.H.: Benchmarking of statistical dependency
parsers for french. In: Proceedings of the 23rd International Conference on Computational
10 / 12


## Page 11


Linguistics: Posters. pp. 108–116. Association for Computational Linguistics, Chinese In-
formation Processing Society of China (2010)
5. Carl, M., Schaeffer, M.J.: Why translation is difﬁcult: A corpus-based study of non-literality
in post-editing and from-scratch translation. HERMES-Journal of Language and Communi-
cation in Business (56), 43–57 (2017)
6. Carpuat, M., Vyas, Y., Niu, X.: Detecting cross-lingual semantic divergence for neural ma-
chine translation. In: Proceedings of the First Workshop on Neural Machine Translation. pp.
69–79. Association for Computational Linguistics (2017)
7. Chatterjee, R., Negri, M., Rubino, R., Turchi, M.: Findings of the WMT 2018 Shared Task on
Automatic Post-Editing. In: Proceedings of the Third Conference on Machine Translation.
Association for Computational Linguistics, Belgium, Brussels (October 2018)
8. Chuquet, H., Paillard, M.: Approche linguistique des problèmes de traduction anglais-
français. Ophrys (1989)
9. Cohen, J.: A coefﬁcient of agreement for nominal scales. Educational and Psychological
Measurement 20, 37–46 (1960)
10. Deng, D., Xue, N.: Translation divergences in chinese–english machine translation: An em-
pirical investigation. Computational Linguistics 43(3), 521–565 (2017)
11. Dorr, B.J., Pearl, L., Hwa, R., Habash, N.: Duster: A method for unraveling cross-language
divergences for statistical word-level alignment. In: Conference of the Association for Ma-
chine Translation in the Americas. pp. 31–43. Springer (2002)
12. Ganitkevitch, J., Van Durme, B., Callison-Burch, C.: PPDB: The paraphrase database. In:
Proceedings of the 2013 Conference of the North American Chapter of the Association for
Computational Linguistics: Human Language Technologies. pp. 758–764 (2013)
13. Gray, R.M.: Entropy and Information Theory. Springer-Verlag, Berlin, Heidelberg (1990)
14. He, K., Zhang, X., Ren, S., Sun, J.: Spatial pyramid pooling in deep convolutional networks
for visual recognition. IEEE Transactions on Pattern Analysis and Machine Intelligence
37(9), 1904–1916 (Sept 2015). https://doi.org/10.1109/TPAMI.2015.2389824
15. Imamura, K., Sumita, E., Matsumoto, Y.: Automatic construction of machine translation
knowledge using translation literalness. In: Proceedings of the tenth conference on European
chapter of the Association for Computational Linguistics-Volume 1. pp. 155–162. Associa-
tion for Computational Linguistics (2003)
16. Koehn, P., Och, F.J., Marcu, D.: Statistical phrase-based translation. In: Proceedings of the
2003 Conference of the North American Chapter of the Association for Computational Lin-
guistics on Human Language Technology-Volume 1. pp. 48–54. Association for Computa-
tional Linguistics (2003)
17. Legrand, J., Auli, M., Collobert, R.: Neural Network-based Word Alignment through Score
Aggregation. In: Proceedings of the First Conference on Machine Translation, WMT 2016,
colocated with ACL 2016, August 11-12, Berlin, Germany. pp. 66–73. The Association for
Computer Linguistics (2016)
18. Levenshtein, V.I.: Binary codes capable of correcting deletions, insertions, and reversals.
Soviet physics doklady 10(8), 707–710 (1966)
19. Liang, P., Taskar, B., Klein, D.: Alignment by agreement. In: Proceedings of the main con-
ference on Human Language Technology Conference of the North American Chapter of the
Association of Computational Linguistics. pp. 104–111. Association for Computational Lin-
guistics (2006)
20. Mallinson, J., Sennrich, R., Lapata, M.: Paraphrasing revisited with neural machine transla-
tion. In: Proceedings of the 15th Conference of the European Chapter of the Association for
Computational Linguistics: Volume 1, Long Papers. vol. 1, pp. 881–893 (2017)
21. Manning, C.D., Surdeanu, M., Bauer, J., Finkel, J., Bethard, S.J., McClosky, D.: The Stanford
CoreNLP natural language processing toolkit. In: Association for Computational Linguistics
(ACL) System Demonstrations. pp. 55–60 (2014)
11 / 12


## Page 12


22. Molina, L., Hurtado Albir, A.: Translation Techniques Revisited: A Dynamic and Function-
alist Approach. Meta 47(4), 498–512 (2002). https://doi.org/10.7202/008033ar
23. Newmark, P.: Approaches to Translation (Language Teaching Methodology Senes). Oxford:
Pergamon Press (1981)
24. Newmark, P.: A textbook of translation, vol. 66. Prentice Hall New York (1988)
25. Papineni, K., Roukos, S., Ward, T., Zhu, W.J.: Bleu: a method for automatic evaluation of
machine translation. In: Proceedings of the 40th annual meeting on association for computa-
tional linguistics. pp. 311–318. Association for Computational Linguistics (2002)
26. Pavlick, E., Bos, J., Nissim, M., Beller, C., Van Durme, B., Callison-Burch, C.: Adding
semantics to data-driven paraphrasing. In: Proceedings of the 53rd Annual Meeting of the
Association for Computational Linguistics and the 7th International Joint Conference on
Natural Language Processing (Volume 1: Long Papers). vol. 1, pp. 1512–1522 (2015)
27. Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., Blondel, M.,
Prettenhofer, P., Weiss, R., Dubourg, V., Vanderplas, J., Passos, A., Cournapeau, D., Brucher,
M., Perrot, M., Duchesnay, E.: Scikit-learn: Machine learning in Python. Journal of Machine
Learning Research 12, 2825–2830 (2011)
28. Petrov, S., Das, D., McDonald, R.T.: A universal part-of-speech tagset. In: Calzolari, N.,
Choukri, K., Declerck, T., Dogan, M.U., Maegaard, B., Mariani, J., Odijk, J., Piperidis, S.
(eds.) Proceedings of the Eighth International Conference on Language Resources and Eval-
uation, LREC 2012, Istanbul, Turkey, May 23-25, 2012. pp. 2089–2096. European Language
Resources Association (ELRA) (2012)
29. Pham, M.Q., Crego, J., Senellart, J., Yvon, F.: Fixing translation divergences in parallel cor-
pora for neural mt. In: Proceedings of the 2018 Conference on Empirical Methods in Natural
Language Processing. pp. 2967–2973 (2018)
30. Schmid, H.: Improvements In Part-of-Speech Tagging With an Application To German. In:
Proceedings of the ACL SIGDAT-Workshop. pp. 47–50 (1995)
31. Snover, M., Dorr, B., Schwartz, R., Micciulla, L., Makhoul, J.: A study of translation edit
rate with targeted human annotation. In: Proceedings of association for machine translation
in the Americas. vol. 200 (2006)
32. Speer, R., Chin, J., Havasi, C.: Conceptnet 5.5: An open multilingual graph of general knowl-
edge. In: Thirty-First AAAI Conference on Artiﬁcial Intelligence. pp. 4444–4451 (2017)
33. Speer, R., Lowry-Duda, J.: Conceptnet at semeval-2017 task 2: Extending word embeddings
with multilingual relational knowledge. In: Bethard, S., Carpuat, M., Apidianaki, M., Mo-
hammad, S.M., Cer, D.M., Jurgens, D. (eds.) Proceedings of the 11th International Workshop
on Semantic Evaluation, SemEval@ACL 2017, Vancouver, Canada, August 3-4, 2017. pp.
85–89. Association for Computational Linguistics (2017)
34. Tsoumakas, G., Katakis, I., Vlahavas, I.: Random k-labelsets for multilabel classiﬁcation.
IEEE Transactions on Knowledge and Data Engineering 23(7), 1079–1089 (2011)
35. Vinay, J.P., Darbelnet, J.: Stylistique comparée du français et de l’anglais: méthode de tra-
duction. Bibliothèque de stylistique comparée, Didier (1958)
36. Vyas, Y., Niu, X., Carpuat, M.: Identifying Semantic Divergences in Parallel Text without
Annotations. In: Walker, M.A., Ji, H., Stent, A. (eds.) Proceedings of the 2018 Conference
of the North American Chapter of the Association for Computational Linguistics: Human
Language Technologies, NAACL-HLT 2018, New Orleans, Louisiana, USA, June 1-6, 2018,
Volume 1 (Long Papers). pp. 1503–1515. Association for Computational Linguistics (2018)
37. Zhai, Y., Max, A., Vilnat, A.: Construction of a multilingual corpus annotated with transla-
tion relations. In: First Workshop on Linguistic Resources for Natural Language Processing.
pp. 102–111 (2018)
12 / 12

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1912.10847v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1912.10847v1_What_do_Asian_Religions_Have_in_Common__An_Unsupervised_Text_Analytics_Explorati

> Source: 1912.10847v1_What_do_Asian_Religions_Have_in_Common__An_Unsupervised_Text_Analytics_Explorati.pdf

> Pages: 18

---


## Page 1


WHAT DO ASIAN RELIGIONS HAVE IN COMMON?
AN UNSUPERVISED TEXT ANALYTICS EXPLORATION
PREETI SAH and ERNEST FOKOU´E
Abstract. The main source of various religious teachings is their sacred texts which varies from religion
to religion based on diﬀerent factors like the geographical region or time of birth of particular religion.
Despites these diﬀerences there could be similarities between the sacred texts based on what lessons it
teaches to it’s followers. This paper attempts to ﬁnd the similarity using text mining techniques. The
corpus consisting of Asian (Tao Te Ching, Buddhism, Yogasutra, Upanishad) and non Asian (four Bible
texts) is used to explore ﬁndings of similarity measures like Euclidean, Manhattan, Jaccard and Cosine
on raw Document Term Frequency [DTM], normalized DTM which reveals similarity based on word
usage. The performance of Supervised learning algorithms like K-Nearest Neighbor [KNN], Support
Vector Machine [SVM] and Random Forest is measured based on it’s accuracy to predict correct scared
text for any given chapter in the corpus. The K-means clustering visualizations on Euclidean distances
of raw DTM reveals that there exists a pattern of similarity among these sacred texts with Upanishads
and Tao Te Ching being the most similar text in the corpus.
1. Introduction
The purpose of religion is to facilitate love, compassion, patience, tolerance, humility and forgive-
ness. The sacred texts are cornerstone of religion and medium to instill the religious teachings in the
people. Every part of the world follow diﬀerent sacred texts to learn and preach about their religion.
The following scripts were collected for diﬀerent religions which is followed in diﬀerent countries:
• Hinduism (India): Yogasutras, Upanishads
• Buddhism (Tibet): Four Noble Truth of Buddhism
• Taoism (China): Tao Te Ching
• Christianity (Central Asia/America): Book of Proverb, Book of Ecclesiastes, Book of Ec-
clesiasticus, Book of Wisdom
All the data collected was English translations of the original language in which it was written.This
was done to make sure that we have uniformity of texts collected from diﬀerent sources.
The sources of the data were:
• Yogasutras: Project Gutenberg’s The Yoga Sutras of Patanjali, by Charles Johnston
• Upanishads: The Project Gutenberg EBook of The Upanishads, by Swami Paramananda
• Four Noble Truth of Buddhism: https://www.accesstoinsight.org/lib/study/truths.html
• Tao Te Ching: Tao Te Ching - Translated by J. Legge
• Book of Proverb: Project Gutenberg EBook The Bible, Douay-Rheims, Book 22: Proverbs
• Book of Ecclesiastes: Project Gutenberg EBook The Bible, Douay-Rheims, Book 23: Ec-
clesiastes
• Book of Ecclesiasticus: Project Gutenberg EBook The Bible, Douay-Rheims, Book 26:
Ecclesiasticus
1
arXiv:1912.10847v1  [cs.CL]  20 Dec 2019


## Page 2


2
SAH and FOKOU´E
• Book of Wisdom: Project Gutenberg EBook The Bible, Douay-Rheims, Book 25: Wisdom
Buddhism teaches about four noble truth. Each of these truths entails a duty: stress is to be
comprehended, the origination of stress abandoned, the cessation of stress realized, and the path
to the cessation of stress developed. When all of these duties have been fully performed, the mind
gains total release [1]. Tao Te Ching teaches that Tao is The Way, Not Your Wayabout. The
chapters talk about staying detached, letting go and keeping things simple [2]. Yogasutra contains
essence of wisdom. We think of ourselves as living a purely physical life, in these material bodies
of ours. In reality, we have gone far indeed from pure physical life; for ages, our life has been
psychical, we have been centred and immersed in the psychic nature [3]. The Upanishads represent
the loftiest heights of ancient Indo-Aryan thought and culture. They form the wisdom portion or
Gnana-Kanda of the Vedas, as contrasted with the Karma-Kanda or sacriﬁcial portion. In each of
the four great Vedas–known as Rik, Yajur, Sama and Atharva–there is a large portion which deals
predominantly with rituals and ceremonials, and which has for its aim to show man how by the
path of right action he may prepare himself for higher attainment [4].
Book of Proverbs consists of wise and weighty sentences: regulating the morals of men: and direct-
ing them to wisdom and virtue [5]. Book of Ecclesiastes or The Preacher, (in Hebrew, Coheleth,)
because in it, Solomon, as an excellent preacher, setteth forth the vanity of the things of this world:
to withdraw the hearts and aﬀections of men from such empty toys [6]. Book of Ecclesiasticus gives
admirable lessons of all virtues [7]. Book of Wisdom abounds with instructions and exhortations
to kings and all magistrates to minister justice in the commonwealth, teaching all kinds of virtues
under the general names of justice and wisdom [8].
Buddhism :And what are fabrications? There are these six classes of intention: intention aimed
at sights, sounds, aromas, tastes, tactile sensations, ideas. These are called fabrications. Tao Te
Ching: Heaven and earth do not act from (the impulse of) any wish to be benevolent; they deal
with all things as the dogs of grass are dealt with. The sages do not act from (any wish to be)
benevolent; they deal with the people as the dogs of grass are dealt with. May not the space between
heaven and earth be compared to a bellows? ’Tis emptied, yet it loses not its power; ’Tis moved
again, and sends forth air the more. Much speech to swift exhaustion lead we see; Your inner being
guard, and keep it free [1].
Tao Te Ching: Heaven and earth do not act from (the impulse of) any wish to be benevolent; they
deal with all things as the dogs of grass are dealt with. The sages do not act from (any wish to be)
benevolent; they deal with the people as the dogs of grass are dealt with. May not the space between
heaven and earth be compared to a bellows? ’Tis emptied, yet it loses not its power; ’Tis moved
again, and sends forth air the more. Much speech to swift exhaustion lead we see; Your inner being
guard, and keep it free [2].
Upanishad : The Brahman once won a victory for the Devas. Through that victory of the Brahman,
the Devas became elated. They thought, ”This victory is ours. This glory is ours.” Brahman here
does not mean a personal Deity. There is a Brahma, the ﬁrst person of the Hindu Trinity; but
Brahman is the Absolute, the One without a second, the essence of all. There are diﬀerent names
and forms which represent certain personal aspects of Divinity, such as Brahma the Creator, Vishnu
the Preserver and Siva the Transformer; but no one of these can fully represent the Whole. Brahman
is the vast ocean of being, on which rise numberless ripples and waves of manifestation. From the
smallest atomic form to a Deva or an angel, all spring from that limitless ocean of Brahman, the
inexhaustible Source of life. No manifested form of life can be independent of its source, just as no
wave, however mighty, can be independent of the ocean. Nothing moves without that Power. He is
the only Doer. But the Devas thought: ”This victory is ours, this glory is ours.” [4]


## Page 3


WHAT DO ASIAN RELIGIONS HAVE IN COMMON?AN UNSUPERVISED TEXT ANALYTICS EXPLORATION3
Yogasutra : perception of the true nature of things. When the object is not truly perceived, when
the observation is inaccurate and faulty, thought or reasoning based on that mistaken perception is
of necessity false and unsound [3].
Book of Proverb : Doth not wisdom cry aloud, and prudence put forth her voice? 8:2. Standing
in the top of the highest places by the way, in the midst of the paths, 8:3. Beside the gates of the
city, in the very doors she speaketh, saying: 8:4. O ye men, to you I call, and my voice is to the
sons of men. 8:5. O little ones understand subtlety, and ye unwise, take notice. 8:6. Hear, for I
will speak of great things: and my lips shall be opened to preach right things. 8:7. My mouth shall
meditate truth, and my lips shall hate wickedness [5].
Book of Ecclesiastes : Speak not any thing rashly, and let not thy heart be hasty to utter a word
before God. For God is in heaven, and thou upon earth: therefore let thy words be few. 5:2. Dreams
follow many cares: and in many words shall be found folly. 5:3. If thou hast vowed any thing to
God, defer not to pay it: for an unfaithful and foolish promise displeaseth him: but whatsoever thou
hast vowed, pay it. 5:4. And it is much better not to vow, than after a vow not to perform the
things promised. 5:5. Give not thy mouth to cause thy ﬂesh to sin: and say not before the angel:
There is no providence: lest God be angry at thy words, and destroy all the works of thy hands.
5:6. Where there are many dreams, there are many vanities, and words without number: but do
thou fear God [6].
Book of Ecclesiasticus : Then Nathan the prophet arose in the days of David. 47:2. And as the fat
taken away from the ﬂesh, so was David chosen from among the children of Israel. 47:3. He played
with lions as with lambs: and with bears he did in like manner as with the lambs of the ﬂock, in his
youth. 47:4. Did not he kill the giant, and take away reproach from his people? 47:5. In lifting up
his hand, with the stone in the sling he beat down the boasting of Goliath: 47:6. For he called upon
the Lord the Almighty, and he gave strength in his right hand, to take away the mighty warrior, and
to set up the horn of his nation. 47:7. So in ten thousand did he glorify him, and praised him in
the blessings of the Lord, in oﬀering to him a crown of glory: 47:8. For he destroyed the enemies
on every side, and extirpated the Philistines the adversaries unto this day: he broke their horn for
ever. 47:9. In all his works he gave thanks to the holy one, and to the most High, with words of
glory. 47:10. With his whole heart he praised the Lord, and loved God that made him: and he gave
him power against his enemies: 47:11. And he set singers before the altar, and by their voices he
made sweet melody [7].
Book of Wisdom : Love justice, you that are the judges of the earth. Think of the Lord in goodness,
and seek him in simplicity of heart: 1:2. For he is found by them that tempt him not: and he
sheweth himself to them that have faith in him. 1:3. For perverse thoughts separate from God: and
his power, when it is tried, reproveth the unwise: 1:4. For wisdom will not enter into a malicious
soul, nor dwell in a body subject to sins. 1:5. For the Holy Spirit of discipline will ﬂee from the
deceitful, and will withdraw himself from thoughts that are without understanding, and he shall not
abide when iniquity cometh in. 1:6. For the spirit of wisdom is benevolent, and will not acquit the
evil speaker from his lips: for God is witness of his reins, and he is a true searcher of his heart,
and a hearer of his tongue [8].
These texts from sacred scripts originated in diﬀerent geographical locations and at diﬀerent historic
time-line. The question arises is there are any similarity between them in terms what these texts
want to teach and how they are teaching various religious lessons.
Text Mining using machine learning and feature extraction is helpful in ﬁnding patterns of words
in document collections [9]. Using text mining the aim of this research is to ﬁnd if various sacred
texts are strongly connected. The similarity measures such as Euclidean, Manhattan, Jaccard and
Cosine is ﬁrstly applied to word frequency matrix of the raw corpus to ﬁnd similarities based on
word usage. The distance matrices on Document Term Matrix formed by LDA was calculated
to ﬁnd the similarities between texts based on probabilistic models [12] [13] by selecting k topics


## Page 4


4
SAH and FOKOU´E
[11][14]. The unsupervised learning algorithm such as K mean clustering on raw frequency DTM
reveals the strong similarity between sacred texts [10]. Also supervised learning techniques like K-
Nearest Neighbor, Support Vector Machine and Random Forest on labeled corpus was implemented
to ﬁnd if these algorithms can predict accurately if any chapter belongs to which sacred text.
2. Methodology
2.1. Overview
The Figure 1 shows overview of the steps and algorithms used to ﬁnd similarity between religious
scripts.
Figure 1. Various steps involved in ﬁnding similarity between scriptures
Bag of Words assumes that each document is the fragment of text from a sacred book.
The
distinction between sacred books is supervised via the creation of corresponding label. The closeness
of sacred books is found in terms of document distances calculated using various similarity measures.
2.2. Similarity Measures
Throughout the rest of this paper, we will use the p-dimensional vector xl = (xl1, xl2, · · · , xlp)⊤to
denote the entries of the lth row of the term document matrix X. Given two rows xl and xm of
X, we use the generic notation d(xl, xm) to denote the distance between the two rows, which is
essentially the distance between two chosen chapters of the whole corpus regardless of which sacred
book each belongs to. The chapter here is our basic document.


## Page 5


WHAT DO ASIAN RELIGIONS HAVE IN COMMON?AN UNSUPERVISED TEXT ANALYTICS EXPLORATION5
In this section we introduce diﬀerent mathematical distances grouped mathematically and we em-
pirically evaluate their performance. Each distance family has speciﬁc mathematical properties
that diﬀerentiates one another from each other. The eﬀectiveness of applying the similarity mea-
sure is believed to be related to the mathematical properties of each family.
The various similarity measures helps us to understand the similarity of various chapters within
the same book and also similarity between diﬀerent book in the corpus.
The diﬀerent measures used for the corpus:
• The very commonly known Euclidean distance belongs to Minkowski Family. The Euclidean
distance between two chapters in the corpus is calculated as:
dE(xl, xm) =


p
X
j=1
(xlj −xmj)2


1
2
(1)
• Manhattan distance belongs to Minkowski Family and distance between two chapters of the
corpus is deﬁned as:
dM(xl, xm) =
p
X
j=1
|xlj −xmj|
(2)
• Cosine Similarity measure is the normalized inner product between two documents on the
vector space that measures the cosine of the angle between them. The formula to ﬁnd cosine
similarity between two chapters can be written as:
dC(xl, xm) =
x⊤
l xm
(x⊤
l xl)
1
2 (x⊤
mxm)
1
2
(3)
• The Jaccard similarity measures the intersection between two chapters. Jaccard coeﬃcient
is calculated using the formula:
sim(xl, xm) =
p
X
j=1
min{xlj, xmj}
p
X
k=1
max{xlk, xmk}
The Jaccard distance between two chapters is deﬁned as:
dJ(xl, xm) = 1 −sim(xl, xm)
Using the above deﬁned similarity measures on given books Xa and Xb we are trying to:
• study Xa or Xb separately
d(X(a)
l
, X(a)
m ) ≡distance between two chapters of same book X(a)
This helps to discover the relationship of various chapters within the same book
• study relationship between Xa or Xb


## Page 6


6
SAH and FOKOU´E
d(X(a), X(b)) =
min
xl∈X(a)
xm∈X(b)

d(xl, xm)
	
(4)
We are calculating the mean, median, minimum and maximum distances between chapters
of diﬀerent books to discover the relationship between the books.
d(Xa, Xb) =

















min
iϵ(1,..,na),jϵ(1,..,nb) d(Xai, Xbj)
max
iϵ(1,..,na),jϵ(1,..,nb) d(Xai, Xbj)
average
iϵ(1,..,na),jϵ(1,..,nb)
d(Xai, Xbj)
median
iϵ(1,..,na),jϵ(1,..,nb) d(Xai, Xbj)
Within the book distance matrix helps to cluster the chapter in the same book and is
represented as:
DX =


d11
d12
d13
. . .
d1n
d21
d22
d23
. . .
d2n
...
...
...
...
...
dn1
dn2
dn3
. . .
dnn


Distance between n chapters of script X
Distance matrix between eight books helps to cluster books across the corpus and is
represented as:
∆=


X11
X12
X13
. . .
X18
X21
X22
X23
. . .
X28
...
...
...
...
...
X81
X82
X83
. . .
X88


2.3. Supervised Learning Algorithms
Predictive aspects helps in prediction of the origin of fragments of spiritual literature. How well
can we predict which sacred text a fragment of spiritual literature comes from? Three supervised
algorithms: K-Nearest Neighbor, Support Vector Machine and Random Forest was applied on
the labeled corpus. The supervised machines were trained on 70% of the corpus and tested on
remaining 30%. The algorithm providing the maximum accuracy will be best in predicting the
sacred text for a given chapter.
2.4. Data Analysis
Our goals with the data are
• Create a corpus where document is smallest unit of data
• Create Bag of Words DTM after data cleaning
• Attempt to conﬁrm or discover some of the closeness among scared texts using similarity
measures
• Measure the performance of supervised learning in identifying the book label for any docu-
ment


## Page 7


WHAT DO ASIAN RELIGIONS HAVE IN COMMON?AN UNSUPERVISED TEXT ANALYTICS EXPLORATION7
There are several challenges with the data: non uniform structure data in each sacred book, initial
preprocessing reveals large amount of stop words data which can mislead the similarity measures.
Through this paper, document analysis assumes that (a) document is the smallest unit of data
being used for ﬁnding similarity (b) within the bag of words (BOW) assumption/approach, each
document is represented by the words. Using the BOW assumption, our basic data structure after
pre-processing, is the term document matrix (tdm) also known as the document term matrix (dtm),
which can be written in the following n × p matrix
X =


X11
X12
· · ·
· · ·
· · ·
· · ·
X1j
· · ·
X1p
...
...
...
...
· · ·
· · ·
· · ·
· · ·
...
Xi1
Xi2
· · ·
· · ·
· · ·
· · ·
Xij
· · ·
Xip
...
...
...
...
· · ·
· · ·
· · ·
· · ·
...
Xn1
Xn2
· · ·
· · ·
· · ·
· · ·
Xnj
· · ·
Xnp


(5)
Each column Xj of X represents a atomic word like truth, diligent, sense, power, right. In most
document analysis tasks, the term document matrix X is typically very sparse, with 90% of zeroes
not unusual. Besides, except in rare cases, X tends to be ultra-high dimensional, meaning that
p ≫n as depicted in the matrix, since the number of words tends be much much higher than the
number of documents to be text-analyzed. Depending on the analysis, the entries Xij of X can be
of one of the following types:
• Xij ≡Frequency of word j in document i.
• Xij ≡logarithmized relative frequency of word j in document i.
As indicated earlier, one of the most interesting questions one may seek to answer in the presence of
a collection of documents dealing with the diﬀerent sacred texts: are there any similarity between
the various sacred texts ? If so, can we measure that? As we shall see later we will tackle this
question using methods like K-means clustering. Speciﬁcally, if we anticipate k groups of sacred
texts, and denote by Pk = C1 ∪· · · ∪Ck, the partitioning of the data into k groups/clusters, then
we seek the optimum clustering.
P ∗
k = argmin
Pk



k
X
j=1
n
X
i=1
zijd(xi, x∗
j)


,
(6)
where zij = L(xi ∈Cj) and d(·) could be any distance like the Euclidean d(xi, x∗
j) = ∥xi −x∗
j∥2
or the Manhattan distance d(xi, x∗
j) = ∥xi −x∗
j∥1, or any other suitable distance. Section 3 of this
paper is dedicated to the exploration of the clustering of the documents in our corpus. The other
question that naturally arises from such a corpus of documents is: For any given document can we
predict which sacred text it belongs to?
• Data Processing
The unstructured nature of text data adds an extra layer of complexity in the feature
extraction task, and the inherently sparse nature of the corresponding data matrices makes
text mining a distinctly diﬃcult task. To deal with this problem it was required to process
that data. There was a need to clean the noise using Natural Language processing (NLP).
• Data Cleaning
The data cleaning involved removing of stop words using NLTK library. Apart from stop
words present in library it was observed that the data required further cleaning. This was
done by removing unnecessary punctuation marks, special characters and ancient English
words
which
were
not
recognized
as
stop
words
by
NLTK
library.


## Page 8


8
SAH and FOKOU´E
• Data Sampling
The organization of the text was:
– Books: Collection of entire script data
– Paragraphs: Division of script based on the topic being explained
– Chapters: Division of paragraph based on subtopic within each topic
Unit of Sampling: Chapter was taken as smallest unit of sampling. Each religious scripts
was fragmented to chapters and stored for further process of ﬁnding the similarities.These
units existed in the text such as Tao Te Ching while in other books it was approximated
from texts headings.
Corpus ≡Various sacred texts
Chapter ≡Collection of V words from corpus
Chapterd ≡xd ≡(xd1, xd2, ..., xdv)
≡Input Vector
≡1 chapter in a book
• Document Term Matrix (DTM) on Raw Text
The ﬁrst input of similarity measures done using the raw corpus. The raw corpus in this
case refers to corpora after applying data cleaning and processing. We are interested to han-
dle the big corpus without any possible modiﬁcation to test distance measures performance.
Hence, the term document matrix of the raw texts was used as:
The rows of our term document matrix refer to a fragment of text from one of the sacred
books, which is a chapter in the sense adopted in this paper. The sacred book to which a
document belongs is traced in a supervised manner with a variable Y from the set of labels
of all the books considered here namely Y = {g1, g2, · · · , g8} where
g1 is Book 1 containing chapters on the teachings of the Buddha
g2 is Book 2 referring to the Tao Te Ching
g3 is Book 3 referring to the Upanishads
g4 is Book 4 referring to YogaSutra
g5 is Book 5 referring to the Book of Proverb
g6 is Book 6 referring to Book of Ecclesiastes
g7 is Book 7 referring to Book of Ecclesiasticus
g8 is Book 8 referring to Book of Wisdom
3. Results
The minimum, maximum and average distances might contain outliers i.e chapters which are very
similar to each other or quite dissimilar. To deal with this problem median of all distances of
each chapter with every other chapter was used. The median distances was able to capture the
similarities which do not take outliers into consideration.
The Euclidean distance was able to separate the distances amongst diﬀerent scripts while Cosine,
Manhattan and Jaccard were unable to distinguish that.
Figure 2 shows the Euclidean median distance of chapters within the same scripts and across the
script. Between the scripts, distance is minimum between Upanishads and Tao Te Ching. Within
the same script the distance of chapters within Upanishads is minimum (considering the diagonal).


## Page 9


WHAT DO ASIAN RELIGIONS HAVE IN COMMON?AN UNSUPERVISED TEXT ANALYTICS EXPLORATION9
Figure 2. Euclidean median distance between diﬀerent scripts


## Page 10


10
SAH and FOKOU´E
Figure 3a, 3b, 3c and 3d the Euclidean distance of chapters within the Asian scriptures which helps
to ﬁnd most similar chapters within the same script.
(a) Buddhism
(b) Tao Te Ching
(c) Upanishads
(d) Yogasutra
Figure 3. Euclidean distance between diﬀerent chapters of Asian Religious scriptures


## Page 11


WHAT DO ASIAN RELIGIONS HAVE IN COMMON?AN UNSUPERVISED TEXT ANALYTICS EXPLORATION11
Figure 4a, 4b, 4c and 4d shows the euclidean distance of chapters within the Bible texts which
helps to ﬁnd most similar chapters within the same book.
(a) Book of Proverb
(b) Book of Ecclesiastes
(c) Book of Ecclesiasticus
(d) Book of Wisdom
Figure 4. Euclidean distance between diﬀerent chapters of Bible texts
Amongst all scripts, chapters within Upanishads were most similar to themselves which is shown
in ﬁgure 3c. The diagonals represent the distance of a chapter to itself thus resulting in minimum
distance of 0.
The strength of similarity between diﬀerent scripts can be found by visualizing k-means clustering
results calculated from Euclidean distances in ﬁgure 5, 6 7, 8, 9 and 10. Each node is the network
graph represents a script and strength between two scripts is proportional to the width and bright-
ness of edge. The cluster number(k) varies from two to seven and each ﬁgure represents groups of
similarity for diﬀerent k. [Nodes : Bdd = Buddhism / Tao = TaoTeChing/ Upd = Upanishad/
Yoga = YogaSutra/ Prv = Proverb/ Ecc = Ecclesiastes/ Ecs = Ecclesiasticus/ Wsd = Wisdom]


## Page 12


12
SAH and FOKOU´E
(a) Graph network representation
(b) Tree Structure
Figure 5. Clustering with k = 2
(a) Graph network representation
(b) Tree Structure
Figure 6. Clustering with k = 3


## Page 13


WHAT DO ASIAN RELIGIONS HAVE IN COMMON?AN UNSUPERVISED TEXT ANALYTICS EXPLORATION13
(a) Graph network representation
(b) Tree Structure
Figure 7. Clustering with k = 4
(a) Graph network representation
(b) Tree Structure
Figure 8. Clustering with k = 5


## Page 14


14
SAH and FOKOU´E
(a) Graph network representation
(b) Tree Structure
Figure 9. Clustering with k = 6
(a) Graph network representation
(b) Tree Structure
Figure 10. Clustering with k = 7


## Page 15


WHAT DO ASIAN RELIGIONS HAVE IN COMMON?AN UNSUPERVISED TEXT ANALYTICS EXPLORATION15
The ﬁgure 6 represents that Asian texts are more similar to themselves as compared to the Biblical
texts. As we increase the number of cluster from 2 to 7 we can visualize the similarities amongst
Asian scripts. While moving from k=3 to 5 all biblical texts belong to diﬀerent clusters which
means even 4 biblical texts are quite diﬀerent from each other. At the end Upanishads and Tao
Te Ching are the most similar scripts as they belong to same cluster when k=7.
The performance of diﬀerent supervised algorithms in predicting sacred text for any chapter in the
scripture is shown in Table 1, 2 and 3.
Buddhism
Ecclesiastes
Ecclesiasticus
Proverb
Tao
Upanishad
Wisdom
Yoga
Buddhism
4
0
0
0
0
0
0
0
Ecclesiastes
0
0
0
0
0
0
0
0
Ecclesiasticus
0
0
0
0
0
0
1
0
Proverb
0
0
4
4
0
0
0
0
Tao
0
0
0
0
0
0
0
0
Upanishad
10
3
7
3
23
43
3
61
Wisdom
0
0
1
0
0
0
1
0
Yoga
1
0
0
0
0
0
0
5
Table 1.
Confusion matrix generated by KNN having accuracy = 0.339
Buddhism
Ecclesiastes
Ecclesiasticus
Proverb
Tao
Upanishad
Wisdom
Yoga
Buddhism
1
0
0
0
0
0
0
0
Ecclesiastes
0
0
0
0
0
0
0
0
Ecclesiasticus
0
1
10
6
0
0
2
0
Proverb
0
0
0
0
0
0
0
0
Tao
0
0
0
0
0
0
0
0
Upanishad
0
0
1
1
0
0
0
0
Wisdom
0
0
0
0
0
0
0
0
Yoga
14
2
4
0
23
43
3
66
Table 2.
Confusion matrix generated by SVM having accuracy = 0.435
Buddhism
Ecclesiastes
Ecclesiasticus
Proverb
Tao
Upanishad
Wisdom
Yoga
Buddhism
8
0
0
0
0
0
0
0
Ecclesiastes
0
0
0
0
0
0
0
0
Ecclesiasticus
0
1
14
0
0
0
5
0
Proverb
0
0
1
7
0
0
0
0
Tao
0
0
0
0
14
0
0
0
Upanishad
7
0
0
0
8
43
0
8
Wisdom
0
0
0
0
0
0
0
0
Yoga
0
2
0
0
1
0
0
58
Table 3.
Confusion matrix generated by Random Forest having accuracy = 0.8136
Amongst all three supervised algorithms Random Forest has highest accuracy of predicting which
sacred text a fragment of spiritual literature comes from, as shown in Table 3. The Upnaishads and
Yogasutra have the largest number of chapters in the corpus and random forest is accurately able
to predict most of the chapters for these two sacred texts which SVM and KNN fail to identify.


## Page 16


16
SAH and FOKOU´E
4. Conclusions
After projecting Euclidean distances on various DTM (raw data DTM and normalized log DTM)
we can conclude that the pattern of strong closeness exists among the diﬀerent religious scripts.
The similarity is driven by geography of origin of the religions. Bag of words is powerful to ﬁnd
the pattern of strong closeness between the four Asian religious scripts: Buddhism, Tao Te Ching,
Upanishad and Yogasutra whose place of origin are geographical close. The two most similar scripts
Tao Te Ching and Upanishad depicts the inﬂuence of two neighbouring countries China and India
on their common religious teachings.
An interesting potential work in this direction would be extracting main sematics features of the
texts. Also, k-medoids using PAM can be implemented to observe the similarity between scripts.
Using k-medoids ensures that the centers of clusters are actual points in the DTM and can give
better results. This work also initiates the conversation about interesting results that be obtained
from Markov models.
References
[1] Accesstoinsight.org.
The
Four
Noble
Truths:
A
Study
Guide.
[online]
Available
at:
https://www.accesstoinsight.org/lib/study/truths.html [Accessed 25 Mar. 2018]. 2010. Data.
[2] Teo, S. (n.d.) Three Things to Learn from Tao Te Ching - ’The’ Way, Not ’Your’ Way. [online] Tao Te Ching.
Available at: http://tao-in-you.com/three-things-about-tao-te-ching/ [Accessed 25 Mar. 2018]. Data.
[3] Gutenberg.org.
The
Yoga
Sutras
of
Patanjali.
[online]
Available
at:
http://www.gutenberg.org/ﬁles/2526/2526.txt [Accessed 25 Mar. 2018]. 2010. Data.
[4] Gutenberg.org. The Upanishads. [online] Available at: http://www.gutenberg.org/cache/epub/3283/pg3283.txt
[Accessed 25 Mar. 2018]. 2014. Data.
[5] Gutenberg.org. The Bible, Douay-Rheims, Book 22: Proverbs The Challoner Revision. [online] Available at:
http://www.gutenberg.org/cache/epub/8322/pg8322.txt [Accessed 25 Mar. 2018]. 2014. Data.
[6] Gutenberg.org. The Bible, Douay-Rheims, Book 23: Ecclesiastes The Challoner Revision. [online] Available
at: http://www.gutenberg.org/cache/epub/8323/pg8323.txt [Accessed 25 Mar. 2018]. 2005. Data.
[7] Gutenberg.org. The Bible, Douay-Rheims, Book 26: Ecclesiasticus The Challoner Revision. [online] Available
at: http://www.gutenberg.org/cache/epub/8326/pg8326.txt [Accessed 25 Mar. 2018]. 2005. Data.
[8] Gutenberg.org. The Bible, Douay-Rheims, Book 25: Wisdom The Challoner Revision. [online] Available at:
http://www.gutenberg.org/cache/epub/8325/pg8325.txt [Accessed 25 Mar. 2018]. 2005. Data.
[9] Qahl, Salha Hassan Muhammed An Automatic Similarity Detection Engine Between Sacred Texts Using
Text Mining and Similarity Measures” (2014). Thesis. Rochester Institute of Technology.
[10] Bjornar Larsen and Chinatsu Aone. 1999 Fast and eﬀective text mining using linear-time document clus-
tering. In Proceedings of the ﬁfth ACM SIGKDD international conference on Knowledge discovery and data
mining (KDD ’99). ACM, New York, NY, USA, 16-22.
[11] Rajkumar Arun, V. Suresh, C. E. Veni Madhavan, and M. N. Narasimha Murthy. On ﬁnding the natural
number of topics with latent dirichlet allocation: Some observations. In Advances in knowledge discovery and
data mining, Mohammed J. Zaki, Jeﬀrey Xu Yu, Balaraman Ravindran and Vikram Pudi (eds.). Springer Berlin
Heidelberg, 391402. 2010.
[12] Cao Juan, Xia Tian, Li Jintao, Zhang Yongdong, and Tang Sheng. A density-based method for adaptive
lDA model selection. Neurocomputing 16th European Symposium on Artiﬁcial Neural Networks 2008 72, 79:
17751781. 2009.
[13] Romain Deveaud, ric SanJuan, and Patrice Bellot.
Accurate and eﬀective latent concept modeling for
ad hoc information retrieval. Document numrique 17, 1: 6184. 2014.
[14] Thomas L. Griffiths and Mark Steyvers. Finding scientiﬁc topics. Proceedings of the National Academy
of Sciences 101, suppl 1: 52285235. 2004.


## Page 17


WHAT DO ASIAN RELIGIONS HAVE IN COMMON?AN UNSUPERVISED TEXT ANALYTICS EXPLORATION17
Preeti Sah, College of Computing and Information Sciences, Rochester Institute of Technology, 85 Lomb Memorial
Drive, Rochester, New York 14623,
e-mail: ks3911@rit.edu
Ernest Fokou´e, , School of Mathematical Sciences, Rochester Institute of Technology, 85 Lomb Memorial Drive,
Rochester, New York 14623,
e-mail: epfeqa@rit.edu


## Page 18


18

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
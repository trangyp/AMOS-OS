---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1608.03587v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1608.03587v2_The_statistical_trade-off_between_word_order_and_word_structure_-_large-scale_ev

> Source: 1608.03587v2_The_statistical_trade-off_between_word_order_and_word_structure_-_large-scale_ev.pdf

> Pages: 24

---


## Page 1


The statistical trade-off between word order and 
word structure – large-scale evidence for the 
principle of least effort 
Alexander Koplenig1, Peter Meyer1, Sascha Wolfer1, Carolin Müller-Spitzer1 
1 Institute for the German Language (IDS), Mannheim, Germany.
Abstract 
Languages employ different strategies to transmit structural and grammatical information. 
While, for example, grammatical dependency relationships in sentences are mainly 
conveyed by the ordering of the words for languages like Mandarin Chinese, or 
Vietnamese, the word ordering is much less restricted for languages such as Inupiatun or 
Quechua, as those languages (also) use the internal structure of words (e.g. inflectional 
morphology) to mark grammatical relationships in a sentence. Based on a quantitative 
analysis of more than 1,500 unique translations of different books of the Bible in almost 
1,200 different languages that are spoken as a native language by approximately 6 billion 
people (more than 80% of the world population), we present large-scale evidence for a 
statistical trade-off between the amount of  information conveyed by the ordering of words 
and the amount of information conveyed by internal word structure: languages that rely 
more strongly on word order information tend to rely less on word structure information 
and vice versa. In addition, we find that – despite differences in the way information is


## Page 2


expressed – there is also evidence for a trade-off between different books of the biblical 
canon that recurs with little variation across languages: the more informative the word 
order of the book, the less informative its word structure and vice versa. We argue that this 
might suggest that, on the one hand, languages encode information in very different (but 
efficient) ways. On the other hand, content-related and stylistic features are statistically 
encoded in very similar ways. 
Introduction 
Natural languages employ different strategies to transmit information that is necessary to 
recover specific aspects of the corresponding message (e.g. grammatical relations, thematic 
roles, agreement phenomena, and more generally, the encoding of grammatical categories). 
While, for example, grammatical information ("who did what to whom") in a sentence is 
mainly conveyed by the ordering of the words in languages like Mandarin Chinese or 
Vietnamese, the word ordering is much less restricted for languages like Inupiatun or 
Quechua, as those languages (also) use the internal structure of words (e.g. the modification 
of word roots by inflection or the compounding of roots) as cues to inform about 
grammatical relationships in a sentence. This has led linguists to speculate, mostly 
qualitative in nature [1–5], about a potential trade-off between the amount of regularity of 
the ordering of words and the amount of regularity of the internal word structure: languages 
that rely more on word order to encode information rely less on morphological information 
and vice versa. In this paper, we explicitly address this question quantitatively. 
Theoretically, the trade-off hypothesis can be justified as an instantiation of Zipf's principle 
of least effort [6], or the more general framework of synergetic linguistics [7]: If, for


## Page 3


example, grammatical relationships in a sentence are fully determined by the ordering of 
words, it would constitute unnecessary cognitive effort to additionally encode this 
information by intra-lexical regularities. If, however, word ordering gives rise to some 
extent of grammatical ambiguity, we should expect this ambiguity to be cleared up with the 
help of word structure regularities in order to avoid unsuccessful transmission. If we define 
Dstructure as the amount to which parts of a word token can be predicted given the observed 
overall regularities in intra-word structure and Dorder  as the amount of information that is 
expressed in the ordering of words [8], then the simplest conceivable mathematical form of 
this relationship would be: 
𝐷𝑠𝑡𝑟𝑢𝑐𝑡𝑢𝑟𝑒∗ 𝐷𝑜𝑟𝑑𝑒𝑟 = 𝑐   
 
 
[1] 
where c is some constant. Put differently, we set out to test the hypothesis that Dorder varies 
inversely as Dstructure. Or, if we relax the rather strong assumption of a proportional 
relationship, we can model Dorder as a function of the reciprocal of Dstructure, where the 
conditional expectation can be written as: 
𝐸(𝐷𝑠𝑡𝑟𝑢𝑐𝑡𝑢𝑟𝑒|𝐷𝑜𝑟𝑑𝑒𝑟) = 𝛽0 + 𝛽1 ∗(𝐷𝑜𝑟𝑑𝑒𝑟)−1 
 
[2] 
where the parameters 𝛽0 and 𝛽1 are estimated empirically. If we do not want to make any 
assumptions regarding the functional form of the relationship, we can compute Spearman's 
rank correlation coefficient rs between Dorder and Dstructure. A trade-off between both 
variables would imply that: 
𝑟𝑠≪0  
 
 
[3] 
Material and Methods


## Page 4


We neither pursue liturgical or theological goals, nor do we want to propagate Christian 
missionary work. As linguists, our interest in the Bible stems solely from the fact that it is 
the book with the most available translations into different languages [9].  
Interactive visualizations, raw data and code to reproduce all results presented in this paper, 
are available online at http://www.owid.de/plus/eebib2016/project.html. On a side note, our 
data also conform to a typical areal pattern of linguistic features, viz. "a strong tendency to 
geographical homogeneity" [2]. The online presentation of our results makes such patterns 
accessible through interactive maps. 
As our data basis, we used the Parallel Bible Corpus made available by [9]. It contains 
1,559 unique translations of the Bible in 1,196 different languages in a fine-grained parallel 
structure (regarding book, chapter and verse). Each translation is tokenized and Unicode 
normalized. Spaces were inserted between words and both punctuation marks and non-
alphabetic symbols. In addition, all texts were manually checked and corrected by [9] 
where necessary. In texts without spaces or marks between words, a dictionary lookup 
method was used to detect word boundaries (e.g. for Khmer, Burmese, or Mandarin 
Chinese). Detected word tokens are space-separated. All uppercase characters were lowered 
in a language-specific way based on the closest ISO 639-3 code provided by [9]. We then 
split each bible translation into different books of the biblical canon, effectively treating 
each book as a different text sample of the corresponding Bible translation. Here, we 
focused on the following six books of the New Testament: the four Gospels (Matthew, 
Mark, Luke, John), the Book of Acts and the Book of Revelation, because (i) we have 
enough available translations in different languages for those books and (ii) those books are 
reasonably long which makes the estimation of our two key quantities more reliable and


## Page 5


robust. Interactive visualizations for all other books of the biblical canon are available 
online.  
In October 2015, the Wycliffe Global Alliance estimated that almost 6 billion people have 
access to at least portions of the Bible in their native language [10]. To check the reliability 
of this figure, we extracted native speaker estimates for the languages available to us from 
the English Wikipedia [https://en.wikipedia.org, all accessed on 07/11/2016]. Our estimate 
corresponds well with the figure quoted above. It is important to emphasize that such a 
figure has to be treated with caution, because (i) census methods and dates of surveying 
vary significantly, (ii) defining a language, a language variety, or a dialect can be difficult, 
and (iii) there are people with more than one native language.  
Let 
us 
represent 
each 
book 
as 
a 
symbolic 
sequence 
of 
N 
characters 
i.e. 𝑏= {𝑐1, 𝑐2, … , 𝑐𝑁−1, 𝑐𝑁} where 𝑐𝑖 represents any character (including white spaces and 
punctuation marks) in the book at position i. The set of all distinct characters (or letters) 
that appear in b is defined as the alphabet Ab, while the set of all distinct space-separated 
sequences (or word types) that appear in b is defined as the book’s lexicon Wb. While this 
technical definition of word types is the de-facto standard in quantitative linguistics, this 
definition can be called into question from a theoretical point of view as mentioned above 
[11,12]. 
Since we are interested in measuring the amount of information that is conveyed by the 
word structure and the ordering of words, we use information theory as our mathematical 
framework [13]. To this end, we use one of the key ideas of the Minimum Description 
Length Principle: "any regularity in the data can be used to compress the data, i.e. to 
describe it using fewer symbols than needed to describe the data literally.  The more


## Page 6


regularities there are, the more the data can be compressed." [14]. We measure the entropy 
per symbol or entropy rate Hb for each book b which can be defined [13] as the average 
amount of information that is needed in order to describe b. Or put differently, Hb measures 
the redundancy of b [15]. We use the non-parametric estimation method of [15,16] that is 
based on the Lempel-Ziv compression algorithm [17]. This method does not require any 
prior training, produces robust estimates without the need for very long strings as input and 
is able to take into account very long range correlations typical of literary texts [18,19] that 
are not captured by direct parametric Markovian or "plug-in" estimators [15]. For each 
book b, we estimate the per-symbol description length as [15]: 
𝐻̂𝑏=  [
1
𝑁∑
𝑙𝑖
log (𝑖+1)
𝑁
𝑖=1
]
−1
 
 
 
[4] 
To measure the minimum number in bits per character [bpc], logarithms throughout this 
paper are taken to base two. Here, the key quantity of interest is the match-length 𝑙𝑖. It 
measures the length of the shortest substring starting at position i of b that is not also a 
substring of the part of the book before this position. For example, given the string 
"montana bananas" at position i = 10, l10 is equal to 4 ("anan"). Roughly speaking, at 
position i, the past {𝑐1, … , 𝑐𝑖−1} characters of the sequence are taken as a database (or 
lexicon) to assess how much of the sequence starting at i is contained somewhere in our 
"database". The intuitive idea of this approach is that longer match-lengths are indicative of 
more redundancy in the source texts and, therefore, a lower mean uncertainty per letter. 
There are no restrictions regarding the size of the "database", illustrating (i) why the 
estimator can be used in the presence of very long range correlations, as we do not impose 
any restrictions on how far "into the past we can look for a long match" [15] and (ii) that 
the estimator seems like a reasonable model of linguistic patterns of experience, as it


## Page 7


captures structure on various levels of linguistic organization (co-occurring words, regular 
relations between grammatical word forms, constructions) that can be linked to theories of 
language learning and language processing [20]. Details of our Java implementation and an 
open source version can be found online. 
It is important to note that the estimation of entropy rate is defined as the average 
description length for a process that is both stationary and ergodic. It is not clear a priori if 
textual data can be seen as such a process [13], or if both concepts are even meaningful for 
natural languages [21]. To induce (at least some) stationarity, and thereby improve 
convergence, we simply randomized the order of the verses in each book, effectively 
discarding all supra-verse information [22]. 
Based on the ideas of [8,23,24], we approximate the amount of information that is 
conveyed by ordering of words and the structure of words, by estimating 𝐻̂𝑏 for three 
versions of each book: (i) 𝐻̂𝑜𝑟𝑖𝑔𝑖𝑛𝑎𝑙
𝑏
is estimated on the basis of the original version of the 
book. (ii) 𝐻̂𝑜𝑟𝑑𝑒𝑟
𝑏
 is estimated  the basis of a version of the book where word ordering has 
been deliberately destroyed. (iii) 𝐻̂𝑠𝑡𝑟𝑢𝑐𝑡𝑢𝑟𝑒
𝑏
 is estimated on the basis of a version of the 
book in which intra-lexical regularities have been masked. Now, if we use the book version 
with absent word order to construct a code instead, we will need 𝐻̂𝑜𝑟𝑖𝑔𝑖𝑛𝑎𝑙
𝑏
 + 𝐷̂𝑜𝑟𝑑𝑒𝑟
𝑏
 bpc on 
average in order to describe b where 𝐷̂𝑜𝑟𝑑𝑒𝑟
𝑏
is the relative entropy [13,24]. Analogously, 
𝐷̂𝑠𝑡𝑟𝑢𝑐𝑡𝑢𝑟𝑒
𝑏
= 𝐻̂𝑠𝑡𝑟𝑢𝑐𝑡𝑢𝑟𝑒
𝑏
−𝐻̂𝑜𝑟𝑖𝑔𝑖𝑛𝑎𝑙
𝑏
. 
Thus, 
the 
incurring 
penalty 
of 
𝐷̂𝑜𝑟𝑑𝑒𝑟
𝑏
 
or 
𝐷̂𝑠𝑡𝑟𝑢𝑐𝑡𝑢𝑟𝑒
𝑏
measures the amount of information in bpc that gets lost on average if the 
ordering of words or the intra-lexical structure is not considered when an efficient code is 
constructed in order to compress b. Hence, higher value of 𝐷̂𝑜𝑟𝑑𝑒𝑟
𝑏
 or 𝐷̂𝑠𝑡𝑟𝑢𝑐𝑡𝑢𝑟𝑒
𝑏
 are


## Page 8


indicative of a greater amount of regularity or information of the word order or the word 
structure. 
Table 1 illustrates our approach of (i) destroying the word order and (ii) masking the word 
structure. For the version of the book with absent word order, we simply randomized the 
order of words within each verse. This means that when estimating the entropy rate of this 
book, redundancy that stems from the word order cannot be used to compress the corpus, 
but the statistics on the word level remain constant. In languages where the relative 
ordering of words is free, this manipulation should not have a major influence. Hence, a 
small 𝐷̂𝑜𝑟𝑑𝑒𝑟
𝑏
 indicates that the relative ordering of words is less informative in the 
respective language. For the version of the book with masked word structure information, 
all tokens for each word type 𝑤𝑗∈𝑊𝑏 with a length of at least 2 characters are replaced by 
a unique equal-length sequence of characters randomly constructed from the alphabet Ab, 
effectively destroying the structure on the word level, but keeping both the syntactical and 
the collocational structure constant. For example, Table 1 shows that the intra-lexical 
regularity of forming the simple past tense via the suffix "ed" is masked as well as the 
regularity of forming nouns from stems of Latin via the suffix "tion". If the intra-lexical structure 
carries less information in a particular language, meaning that most words have little or no 
internal structure, this manipulation should not have a major influence on the entropy rate 
and thus lead to a small 𝐷̂𝑠𝑡𝑟𝑢𝑐𝑡𝑢𝑟𝑒
𝑏
.  
 
Original 
i said i just dropped in to see what condition my condition was in 
Masked word structure i nypa i wpid imjnwct nc ye wuj jaoh hywjopoic ue hywjopoic wea nc 
Destroyed word order 
condition said was i in what dropped i my see to in condition just


## Page 9


Table 1: Toy example illustrating our approach. First line: original text (one line taken 
from Kenny Rogers' song "Just Dropped In"). Second line: masked word structure. [NB.: 
"i" is not masked since it is only one character long. Thus it does not contain any intra-
lexical structure.] Third line: destroyed word order. Word types printed in boldface appear 
two times. 
It is worth pointing out that in both manipulated versions, basic quantitative structural 
properties of the original text remain unaffected (e.g. book length, word length, the type-
token word frequency distribution), which rules out the (likely) possibility that changes to 
those characteristics influence the entropy rate estimation [25]. For the inter-book 
comparisons (cf. Figure 4 & Figure 5), we keep N constant by first identifying the book 
with the smallest size in characters and then truncating the other five books at this position. 
In 1,450 of all 1,476 translations with available information for the six books, the shortest 
book is Revelation. Since we randomized the order of words within each verse for the book 
version with absent word order, differences of (average) verse lengths (in words) between 
the six books could potentially influence our results. To rule out this possibility, we 
generated an additional data set, where N is kept constant, but the word order is randomized 
per book instead of verse. The results based on this data set are qualitatively 
indistinguishable from the results we report here. The data set is avaiblable online. 
To understand the functional form of the relationship between 𝐷̂𝑠𝑡𝑟𝑢𝑐𝑡𝑢𝑟𝑒
𝑏
 and 𝐷̂𝑜𝑟𝑑𝑒𝑟
𝑏
  (cf. 
Eq. 2 & Figure 1), we fitted the following non-linear regression function by least squares 
for each book b: 
𝐷̂𝑠𝑡𝑟𝑢𝑐𝑡𝑢𝑟𝑒
𝑏,𝑡
= 𝛽0 + 𝛽1 ∗(𝐷̂𝑜𝑟𝑑𝑒𝑟
𝑏,𝑡
)−1 + 𝜖𝑏,𝑡 
[5]


## Page 10


where t = 1, 2, …, T are our available translations for b; 𝜖𝑏,𝑡 is the error term. For 
languages with more than one available translation 𝐷̂𝑠𝑡𝑟𝑢𝑐𝑡𝑢𝑟𝑒
𝑏
 and 𝐷̂𝑜𝑟𝑑𝑒𝑟
𝑏
 were averaged 
across languages, except when stated otherwise in the text or in Figure 5 where we used all 
translations with available information for all six books.  
p-values for the correlation of the rankings of the six books for the selected languages are 
based on exact permutation tests for all 6! = 720 permutations. 
Results 
Figure 1 summarizes the primary result of our analysis. There is clear evidence for a 
statistical trade-off between the amount of word structure information and the amount of 
word order information. For all investigated books, there is a negative Spearman 
correlation of at least 𝑟𝑠= −.71.  
While our results do not permit the conclusion that Dorder is inversely proportional to 
Dstructure in a strictly mathematical sense (cf. Eq.1), the black dashed lines in Figure 1 show 
that a lot of the structure can be captured by a simple statistical model that suggests the 
presence of a reciprocal relationship (cf. Eq. 2): variation in Dorder explains at least 54% of 
the variation in Dstructure for all six investigated books. Interactive visualizations for all other 
books of the biblical canon are available online.


## Page 11


Figure 1. 
The statistical relationship between word structure information and word order 
information (in bpc) for six investigated books of the biblical canon. Orange labels show the ISO 
codes for twelve selected languages. 𝑟𝑠-values are Spearman correlation coefficients. Black dashed 
lines in each plot indicate that a lot of structure can be captured in a simple model that suggests the 
presence of a reciprocal relationship (cf. Eq.2). Abbreviations: chr – Cherokee: cmn – Mandarin 
Chinese; deu – Standard German; eng – English; esk – Northwest Alaska Inupiatun; grc – Koine 
Greek; mya – Burmese; tam – Tamil; qvw - Huaylla Wanca Quechua; vie – Vietnamese; xuo – 
Kuo; zul – Zulu.


## Page 12


This relationship between word order information and word structure information 
corresponds well with typological expectations. Highly synthetic languages like Inupiatun 
(ISO code: esk) or Quechua (qvw) have a higher level of word structure information and a 
lower level of word order information, while very analytic languages like Mandarin 
Chinese (cmn), Vietnamese (vie) or Kuo (xuo; an Mbum language of southern Chad) 
primarily convey grammatical information by the ordering of words (among them 
grammatical particles that correspond to inflectional morphology in more synthetic 
languages). On the other side, very analytical languages show a high(er) level of word order 
information and a low(er) level of word structure information. Languages like Koine Greek 
(the original language of the New Testament, grc), German (deu), or English (eng) mix 
both methods of conveying information; accordingly those languages tend to occupy 
intermediate spots on this spectrum.  
To rule out the possibility of overfitting the data and to demonstrate the robustness of our 
results, Figure 2 shows that the resulting word order and word structure information 
rankings are strongly positively intra-correlated and strongly negatively inter-correlated. In 
terms of variance explained, if we know the word structure information ranking of 
Matthew, we can explain roughly 𝑟2 =. 982 = 96% of the variation in the word structure 
ranking in Acts and roughly 𝑟2 = −.742 = 54% of the variation in its word order ranking.


## Page 13


Figure 2. 
Spearman rank correlation matrix for all combinations of the six investigated books 
demonstrates that the word order and word structure information rankings have a strong positive 
intra-correlation and a strong negative inter-correlation. 
 
Figure 3 shows that our results can also be interpreted from an evolutionary point of view. 
Here, we focus on Mark, since this is the only book for which we have available textual 
data in Old English. Old English, typologically classified as a synthetic language, relies on 
morphological structure to convey grammatical information. Modern English uses analytic 
constructions to mark grammatical relations. This corresponds well with the visible trend in


## Page 14


Figure 3, showing a substantial shift from Old English, with a high amount of word 
structure information to both Middle and Modern English, reducing the system of 
inflectional endings in favour of a stricter word order as indicated by a higher amount of 
word order information: "The Middle English evolution consists primarily in a shift 
towards more analytic structure, eventually approaching that of today’s language which 
[…] is close to isolating" [26].  
Figure 3. 
Scatterplot depicting the relationship between word structure information and word 
order information for translations of the Gospel of Mark in English and English based Creole.


## Page 15


For example, with the loss of inflections in the period of Late Old English / Early Middle 
English, it became difficult to identify a genitive case when an article or a possessive 
adjective was followed by a noun phrase. This ambiguity problem was solved by replacing 
genitives with of-constructions in the period of Middle English [27] and thus creating a 
higher amount of word order information. Or put differently, if less information is carried 
within the word, more information has to be spread among words in order to communicate 
successfully. For the evolution of languages, this indicates that a change in one 
grammatical area can trigger a temporally subsequent change in another grammatical area. 
This is exactly what [28] shows for Icelandic, where changes within its words lead to 
changes in its syntax.  
The classification of the English based Creole languages, which can be seen as "creative 
adaptions of natural languages" [2], also makes sense, as it indicates another substantial 
shift towards more analycity with very little reliance on inflectional morphemes 
compensated by a very strict word order to mark grammatical categories. It is worth 
pointing out that Figure 3 could also be used as a validation of the two key quantities 
estimated in this paper: the amount of word order information and the amount of word 
structure information measure how a given language encodes information, in this case, 
regarding grammatical functions.


## Page 16


Figure 4. 
Inter-book trade-off for the six investigated books for twelve selected languages. 
Abbreviations: Ac – Acts; Jn – John; Lk – Luke; Mr – Mark; Mt – Matthew; Re – Revelation.


## Page 17


Remarkably, while Figure 2 clearly reveals that the inter-language word structure and word 
order rankings are strongly correlated, Figure 4 indicates that there also seems to be an 
inter-book trade-off in addition to the inter-language trade-off: the more informative the 
word order, the less informative the word structure and vice versa. If we calculate the 
Spearman correlation for the 6 investigated books, the median correlation for the 12 
selected languages is 𝑟𝑠= −.94 (for all N = 1,476 translations, the median correlation is 
also 𝑟𝑠= −.94). If we compare the emerging pattern across languages, we find that the 
intra-language relationship is surprisingly similar: regardless of whether the languages are 
historically/geographically related or not, Revelation and John tend to have a higher word 
order information and a lower word structure information in relation to the other 
investigated books, and conversely for both Acts and Luke. Mark and Matthew tend to 
occupy intermediate positions. More precisely, if we calculate the correlations between all 
inter-book rankings for the selected languages, the median correlation is 𝑟𝑠= .94 in both 
cases. For the word structure ranking, the lowest correlation is between Mandarin Chinese 
and Kuo with 𝑟𝑠= .71 (p = .068). For the word order ranking, the smallest correlation is 
between Cherokee and Quechua with 𝑟𝑠= .77  (p = .051). In sum, these results suggest 
that while different languages occupy very different positions in the two-dimensional word 
order/word structure space indicating differences in the way grammatical information is 
encoded, content-related and stylistic features of the source material (here: the Koine Greek 
version) are encoded in very similar ways when they are translated into different languages.  
To further explore this pattern in Figure 5, we used N = 1,476 translations for which we had 
available information for all six books. Here, we ranked the books, with a rank of 1 
indicating that the corresponding book has the highest word order or word structure 
information of all six books of this translation. For each book, separate histograms


## Page 18


visualizing the distribution of word order information ranks and word structure information 
ranks are depicted in the first two columns. The height of each bin represents the relative 
frequency of occurrence of the corresponding rank (in %). The matrix-plots (3rd columns) 
present bi-variate histograms, in which the colors of the cells represent the relative 
frequency of occurrence, with darker shades of gray representing a higher relative 
frequency (in %). In addition, numbers printed in each cell report relative frequencies 
rounded to the nearest integer. The emerging inter-book pattern in Figure 5 is remarkably 
stable across translations: Revelation and John tend to have a higher word order 
information and a lower word structure information in relation to the other investigated 
books, while the opposite applies to both Acts and Luke. Mark and Matthew tend to occupy 
intermediate positions across translations. While most contemporary scholars do not 
believe that the Revelation of John and the Gospel of John were written by the same 
person, there is a widespread consensus that the Book of Acts and the Gospel of Luke were 
written by one author [29]. In general, metaphors, symbolism and the repetition of key 
phrases are characteristic for the Book of Revelation [30], while some scholars describe the 
author of Luke-Acts as a reliable historian accurately recording historic events and 
geographic places [31]. Regarding the four Gospels, there is also agreement about the fact 
that Mark, Matthew and Luke are distinct from John, both in content and in style, with John 
containing more metaphors or allegories [32].


## Page 19


Figure 5. 
Word order information and word structure information rankings for the six 
investigated books. A rank of 1 indicates that the corresponding book has the highest word order or 
word structure information of all six books of the corresponding translation. Histograms visualizing 
the distribution of word order information ranks and word structure information ranks are depicted 
in the first two columns. The height of each bin represents the relative frequency of occurrence of 
the corresponding rank (in %). The matrix-plots (3rd columns) present bi-variate histograms, in 
which the colors of the cells represent the relative frequency of occurrence, with darker shades of 
gray representing a higher relative frequency (in %). In addition, numbers printed in each cell report 
relative frequencies rounded to the nearest integer.


## Page 20


Since our analysis has no liturgical goals, we conclude from a linguistic point of view that 
one interpretation of this result is that stylistic and content-related properties of the source 
material seem to be preserved when translated into different languages. Or put differently, 
if a book of the biblical canon shows more word order regularity and less word structure 
regularity than another book in one language, then this relationship between the books is 
likely to reappear in other languages. More work is needed to understand the linguistic 
correlates of style and/or content that lead to the emergence of this pattern.  
Discussion 
In this paper we used a simple quantitative information-theoretic approach that is not 
restricted to a particular language or a particular writing system. Moreover, the approach is 
not motivated by a specific linguistic theory and is less subjective than other more 
traditional ad-hoc measures [8]. However, it is important to point out that such a numerical 
approach also has drawbacks: (i) It is completely based on the entropy estimation of 
symbolic sequences, the approach does not permit conclusions about specific word 
sequences (or alternative sequences) that can be used to encode a specific message. (ii) It 
does not reveal the precise underlying structures that are affected by the destruction of 
intra- and inter-word regularities [33]. (iii) Finding a definition of a word type that is valid 
across languages is harder than it might look [11]. For example, since we destroy the intra-
lexical structure of distinct space-separated sequences, word types that span two strings 
separated by a blank are excluded from this procedure. This can be problematic, since the 
orthographical representation of compounding varies across languages, (e.g. English "data


## Page 21


set" vs. German "Datensatz"). Addressing these problems and developing additional 
validation methods are clearly required in order to assess the accuracy of our approach. 
With that in mind, we hope that we were able demonstrate that our results can be 
interpreted in an intuitively plausible and meaningful linguistic way [34]. We presented 
evidence that supports Zipf's principle of least effort in relation to the way natural 
languages encode grammatical information. In addition, we found that – despite differences 
in the way information is encoded – the inter-book trade-off regarding different texts of the 
biblical canon regarding the amount of both word order information and word structure 
information remains highly similar across translations into different languages. This result 
is both methodologically and theoretically remarkable. On the methodological side, it arose 
as a by-product of our study, something we did not expect when we conducted this study, 
which indicates the great potential of quantitative studies both for gaining empirical 
evidence for long-standing claims and for finding out new aspects about language and its 
statistical structure. On the theoretical side, the result suggests that basic stylistic and 
content-related properties of individual texts are preserved when they are translated into 
different languages.  
Conversely, the stability of the relationship across books that differ with regard to style and 
content strengthens the evidence for the statistical trade-off between word order and word 
structure. Overall, this is our major scientific finding: there is an inverse relation between 
the amount of information contributed by the ordering of words and the amount of 
information contributed by the internal word structure: languages that rely more on word 
order to transmit grammatical information, rely less on intra-lexical regularities and vice 
versa.


## Page 22


Acknowledgments 
First and foremost, we would like to thank Michael Cysouw and the Parallel Bible Corpus 
team for compiling the Bible data and for making it available to us. Michael Cysouw also 
discussed the results with us and provided very insightful suggestions and comments. We 
thank Frank Michaelis for preparing the online interface. We also would like to thank 
Christian Bentz, Stefan Engelberg, Peter Fankhauser, and Marc Kupietz for their input and 
feedback. We are grateful to Katharina Ehret for making the Old English Bible data 
available to us. We thank Sarah Signer for proofreading. All remaining errors are ours.  
References 
1.  
Zipf GK. The psycho-biology of language ; an introduction to dynamic philology. Boston: 
Houghton Mifflin company; 1935.  
2.  
Crystal D. The Cambridge encyclopedia of language. 3rd ed. Cambridge ; New York: Cambridge 
University Press; 2010.  
3.  
O’Grady W, Dobrovolsky M, Aronoff M, editors. Contemporary linguistics: an introduction. 2nd, 
U.S.  / prepared by Mark Aronoff ed. New York, NY: St. Martin’s Press; 1993.  
4.  
Edwards J. Multilingualism. London: Penguin Books; 1995.  
5.  
Bickerton D. Language and human behavior. 2. print. Seattle: Univ. of Washington Press; 1996.  
6.  
Zipf GK. Human behavior and the principle of least effort: an introduction to human ecology. 
Mansfield Centre, CT: Martino Pub.; 2012.  
7.  
Köhler R. SYSTEM THEORETICAL LINGUISTICS. Theor Linguist. 2009;14: 241. 
doi:10.1515/thli.1987.14.2-3.241 
8.  
Juola P. Assessing linguistic complexity. In: Miestamo M, Sinnemäki K, Karlsson F, editors. 
Language complexity: typology, contact, change. Amsterdam ; Philadelphia: John Benjamins Pub. 
Co; 2008.  
9.  
Mayer T, Cysouw M. Creating a Massively Parallel Bible Corpus. In: Chair) NC (Conference, 
Choukri K, Declerck T, Loftsson H, Maegaard B, Mariani J, et al., editors. Proceedings of the 
Ninth International Conference on Language Resources and Evaluation (LREC’14). Reykjavik, 
Iceland: European Language Resources Association (ELRA); 26-31.


## Page 23


10.  Wycliffe Global Alliance. 2015 Bible Translation Statistics FAQ [Internet]. 2015. Available: 
http://resources.wycliffe.net/statistics/WycliffeGA_stats_2015_FAQs_EN.pdf 
11.  Haspelmath M. The indeterminacy of word segmentation and the nature of morphology and syntax. 
Folia Linguist. 2011;45. doi:10.1515/flin.2011.002 
12.  Jacobs J. Grammatik ohne Wörter? In: Engelberg S, Holler A, Proost K, editors. Sprachliches 
Wissen zwischen Lexikon und Grammatik. Berlin, Boston: DE GRUYTER; 2011. Available: 
http://www.degruyter.com/view/books/9783110262339/9783110262339.345/9783110262339.345.
xml 
13.  Cover TM, Thomas JA. Elements of information theory. 2nd ed. Hoboken, N.J: Wiley-
Interscience; 2006.  
14.  Grünwald PD. A tutorial introduction to the minimum description length principle [Internet]. 2004. 
Available: arXiv:math/0406077 
15.  Kontoyiannis I. The Complexity and Entropy of Literary Styles [Internet]. Stanford University, 
Department of Statistics; 1996. Available: http://pages.cs.aueb.gr/~yiannisk/PAPERS/english.pdf 
16.  Kontoyiannis I, Algoet PH, Suhov YM, Wyner AJ. Nonparametric entropy estimation for 
stationary processes and random fields, with applications to English text. IEEE Trans Inf Theory. 
1998;44: 1319–1327. doi:10.1109/18.669425 
17.  Wyner AD, Ziv J. Some Asymptotic Properties of the Entropy of a Stationary Ergodic Data Source 
with Applications to Data Compression. IEEE Trans Inf Theor. 1989;35: 1250–1258. 
doi:10.1109/18.45281 
18.  Ebeling W, Neiman A. Long-range correlations between letters and sentences in texts. Phys Stat 
Mech Its Appl. 1995;215: 233–241. doi:10.1016/0378-4371(95)00025-3 
19.  Montemurro MA, Pury PA. Long-range fractal correlations in literary corpora. Fractals. 2002;10: 
451–461.  
20.  Ellis NC. Implicit AND explicit language learning: Their dynamic interface and complexity. In: 
Rebuschat P, editor. Studies in Bilingualism. Amsterdam: John Benjamins Publishing Company; 
2015. pp. 1–24. Available: https://benjamins.com/catalog/sibil.48.01ell 
21.  Schürmann T, Grassberger P. Entropy estimation of symbol sequences. Chaos Interdiscip J 
Nonlinear Sci. 1996;6: 414. doi:10.1063/1.166191 
22.  Moscoso del Prado Martín, F. The mirage of morphological complexity. Proceedings of 
Quantitative Measures in Morphology and Morphological Development. Center for Human 
Development, UC San Diego; 2011. Available: 
http://csjarchive.cogsci.rpi.edu/proceedings/2011/papers/0836/paper0836.pdf 
23.  Juola P. Measuring linguistic complexity: The morphological tier. J Quant Linguist. 1998;5: 206–
213. doi:10.1080/09296179808590128


## Page 24


24.  Montemurro MA, Zanette DH. Universal Entropy of Word Ordering Across Linguistic Families. 
Breakspear M, editor. PLoS ONE. 2011;6: e19875. doi:10.1371/journal.pone.0019875 
25.  Tweedie FJ, Baayen RH. How Variable May a Constant be? Measures of Lexical Richness in 
Perspective. Comput Humanit. 1998;32: 323–352.  
26.  Lass R. Phonology and Morphology. In: Lass R, editor. The Cambridge History of the English 
Language. Cambridge: Cambridge University Press; 2000. pp. 56–186. Available: 
http://universitypublishingonline.org/ref/id/histories/CBO9781139053747A006 
27.  Fischer O. SYNTAX. In: Blake N, editor. The Cambridge History of the English Language. 
Cambridge: Cambridge University Press; 1992. pp. 207–408. Available: 
http://universitypublishingonline.org/ref/id/histories/CBO9781139055536A007 
28.  Moscoso del Prado Martín, F. Grammatical Change Begins within the Word: Causal Modeling of 
the Co-evolution of Icelandic Morphology and Syntax. CogSci 2014 Proceedings. Quebec, Canada; 
2014. Available: https://mindmodeling.org/cogsci2014/papers/460/paper460.pdf 
29.  Burkett DR. An introduction to the New Testament and the origins of Christianity. Cambridge, 
UK ; New York: Cambridge University Press; 2002.  
30.  Tenny MC. Interpreting Revelation. Wm. B. Eerdmans Publishing Company; 1988.  
31.  Ramsay WM. The Bearing of Recent Discovery on the Trustworthiness of the New Testament. 
Hodder and Stoughton; 1915.  
32.  Evans CA. The Routledge encyclopedia of the historical Jesus. New York; London: Routledge; 
2010.  
33.  Ehret K, Szmrecsanyi B. An information-theoretic approach to assess linguistic complexity. In: 
Baechler R, Seiler G, editors. Complexity and Isolation. Berlin: De Gruyter; to appear. Available: 
http://www.benszm.net/omnibuslit/EhretSzmrecsanyi_web.pdf 
34.  Fedzechkina M, Newport EL, Jaeger TF. Balancing Effort and Information Transmission During 
Language Acquisition: Evidence From Word Order and Case Marking. Cogn Sci. 2016; n/a-n/a. 
doi:10.1111/cogs.12346

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1608_03587v2_the_statistical_trade_off_between_word_order_and_word_structure_large_scale_ev
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2016/1608_03587V2_THE_STATISTICAL_TRADE_OFF_BETWEEN_WORD_ORDER_AND_WORD_STRUCTURE_LARGE_SCALE_EV.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1810.03184
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1810.03184_Phonology-Augmented_Statistical_Framework_for_Machine_Transliteration_using_Limi

> Source: 1810.03184_Phonology-Augmented_Statistical_Framework_for_Machine_Transliteration_using_Limi.pdf

> Pages: 13

---


## Page 1


IEEE TRANSACTIONS ON AUDIO, SPEECH, AND LANGUAGE PROCESSING
1
Phonology-Augmented Statistical Framework
for Machine Transliteration using Limited
Linguistic Resources
Gia H. Ngo, Minh Nguyen, Nancy F. Chen
Abstract—Transliteration converts words in a source language
(e.g., English) into words in a target language (e.g., Vietnamese).
This conversion considers the phonological structure of the target
language, as the transliterated output needs to be pronounceable
in the target language. For example, a word in Vietnamese that
begins with a consonant cluster is phonologically invalid and thus
would be an incorrect output of a transliteration system. Most
statistical transliteration approaches, albeit being widely adopted,
do not explicitly model the target language’s phonology, which
often results in invalid outputs. The problem is compounded by
the limited linguistic resources available when converting foreign
words to transliterated words in the target language. In this
work, we present a phonology-augmented statistical framework
suitable for transliteration, especially when only limited linguistic
resources are available. We propose the concept of pseudo-
syllables as structures representing how segments of a foreign
word are organized according to the syllables of the target
language’s phonology. We performed transliteration experiments
on Vietnamese and Cantonese. We show that the proposed
framework outperforms the statistical baseline by up to 44.68%
relative, when there are limited training examples (587 entries).
Index
Terms—transliteration,
machine
translation,
cross-
lingual information retrieval, named entity recognition
I. INTRODUCTION
I
N every language, new words are constantly being invented
or borrowed from foreign languages (e.g. names of people,
locations, organizations, and products). For example, the city’s
name “Manchester” has become well known by people of lan-
guages other than English. These new words are often named
entities that are important in cross-lingual information retrieval
[1][2][3][4][5], information extraction [6], machine translation
[7][8][9][10][11], and often present out-of-vocabulary chal-
lenges to spoken language technologies such as automatic
speech recognition [12], spoken keyword search [13][14][15],
and text-to-speech [16][17]. Transliteration is a mechanism
for converting a word in a source (foreign) language to a
target language, and often adopts approaches from machine
translation. In machine translation, the objective is to preserve
the semantic meaning of the utterance as much as possible
while following the syntactic structure in the target language.
Gia H. Ngo is currently with Cornell University, but part of this work
was done at the Institute for Infocomm Research, A*STAR. Minh Nguyen is
currently with National University of Singapore. Nancy F. Chen is currently
with the Institute for Infocomm Research, A*STAR.
c⃝2018 IEEE. Personal use of this material is permitted. Permission from
IEEE must be obtained for all other uses, in any current or future media,
including reprinting/republishing this material for advertising or promotional
purposes, creating new collective works, for resale or redistribution to servers
or lists, or reuse of any copyrighted component of this work in other works.
In transliteration, the objective is to preserve the original
pronunciation of the source word as much as possible while
following the phonological structures of the target language.
The amount of training data available for transliteration is
often much less than that of machine translation. The amount
of training data for machine translation is not limited to
the adoption of new vocabulary or concepts from a foreign
language while this is true for transliteration. It is therefore
challenging for a statistical model to generalize well to im-
plicitly learn the phonological rules of the target language for
transliteration tasks. The lack of training data often results in
non-interpretable outputs by statistical transliteration models
[18]; these outputs are invalid because speakers of the target
language are unable to pronounce these transliterated outputs.
Given the limited training data for transliteration, performance
of statistical transliteration approaches has often been sub-
optimal [7][19]. On the other hand, symbolic transliteration
approaches have been shown to produce phonologically-valid
outputs with minimal training resources [20]. However, sym-
bolic approaches are often limited by the complexity of the
predeﬁned rules, and therefore, under-perform with larger
datasets, as compared to statistical methods [20].
We propose a transliteration framework in which n-gram
language modeling is augmented with phonological knowl-
edge. We propose the concept of pseudo-syllables in sta-
tistical models to impose phonological constraints of syl-
lable structure in the target language, yet retain acoustic
authenticity of the source language as closely as possible.
Our proposed framework integrates advantages of symbolic
approaches on top of statistical transliteration models. The pro-
posed approach ensures phonologically-valid outputs, while
maintaining strengths of statistical models (e.g., language-
independence, performance scaling up with training data size).
This work extends and expands our prior work [20] to
include detailed formulations, experiments, analyses, and dis-
cussions left out in the conference version. In particular,
empirical validation has been generalized on two language
pairs: English-to-Vietnamese and English-to-Cantonese, using
the Vietnamese corpora from the IARPA BABEL program1
that was released for the NIST OpenKWS13 Evaluation [21]
and for the shared tasks at the Named Entity Workshop
(NEWS) at ACL 20182. The implementation of the proposed
1https://catalog.ldc.upenn.edu/LDC2017S01
2The English-to-Vietnamese transliteration data in [20] was released at
NEWS 2018 (http://workshop.colips.org/news2018/shared.html)
arXiv:1810.03184v1  [cs.CL]  7 Oct 2018


## Page 2


IEEE TRANSACTIONS ON AUDIO, SPEECH, AND LANGUAGE PROCESSING
2
model, the symbolic systems and the customized tools for
evaluating transliteration error rates are publicly available3.
II. BACKGROUND
A. Phonology
We introduce three phonological concepts relevant to our
discussion.
1) Syllable: A syllable is considered the smallest phonolog-
ical unit of a word [22] with the following structure [23][24]:
[O] N [Cd] + [T]
(1)
where the “[ ]” speciﬁes an optional unit. O denotes the
Onset, which is a consonant or a cluster of consonants at
the beginning of a syllable. N denotes the Nucleus, which
contains at least a vowel. Cd denotes the Coda, which mostly
contains consonants. T denotes lexical tone, a feature existing
in many languages to distinguish different words [25][26][27].
The syllabic structure above is shared across most languages
in the world [24][28][29].
However, how consonants (C ) and vowels (V ) constitute
Onset, Nucleus, Coda differs across languages. For instance,
in English, an Onset can be a consonant cluster, such as “sn”,
while no consonant cluster can be the Onset of a syllable in
Vietnamese or Cantonese [30][31][32][33].
2) Lexical Tones: In tonal languages, pitch is used to
distinguish the meaning of words which are phonetically
identical [26][34]. This distinctive pitch level or contour is
referred to as lexical tones [35]. For instance, there are 6
distinct lexical tones in Vietnamese [36] and 6 distinct lexical
tones in Cantonese [37]. Around 70% of languages are tonal
[35], concentrating in Africa, East and Southeast Asia [38].
Each lexical tone is commonly encoded in phonetic repre-
sentation with a number. For example, consider two different
Vietnamese words: b_< O 3 (cow) and b_< O 6 (bug). The
two words are represented in phonetic units using X-SAMPA
notation [39], and have the same Onset (b_<) and Nucleus
(O), but are distinguished by the two different lexical tones
(tone 3 and tone 6).
3) Transliteration: In transliteration, a word in a source
language is converted to a target language while preserving the
acoustic phonetic properties of the source language as much as
possible. However, the syllabic structures of the transliterated
output might differ from the syllabic structures of the original
word [7][40][41].
New phonetic units can be inserted into the transliteration
output to imitate the pronunciation of the original word. When
performing transliteration on words from a non-tonal language
(e.g. English) to tonal languages, lexical tones need to be
assigned to each syllable of the transliterated output. So far,
only limited preliminary work has explored lexical tones in
transliteration [36][42].
Another example of insertion in transliteration is the addi-
tion of new phonemes to the output. For example, converting
a consonant cluster from English to many languages involves
3https://github.com/ngohgia/transliteration
the insertion of an additional nucleus after the ﬁrst conso-
nant of a consonant cluster. This phenomenon is deﬁned as
epenthesis with the inserted nucleus usually being a “schwa”
and observed in languages such as Vietnamese [36], Japanese
[43][44], Cantonese [45][46], and many more [47][48][49].
Furthermore, certain phonemes of the source word might be
deleted in the target language due to phonological constraints.
For example, fricatives occurring at the syllable-ﬁnal position
of an English word tends to be omitted (deleted) in their
corresponding counter-part in Vietnamese [36] and Cantonese
[50].
B. Machine Transliteration
1) Input and Aim: Suppose we are given a training dataset
consisting of pairs of words from a source language (e.g.
English) and their corresponding transliteration versions in a
target language (e.g. Vietnamese). Each word of the source
language, which we name as source word in short, is rep-
resented in orthographic form as a sequence of letters f =
[f1, f2, ..., fm]. For each corresponding word in the target
language, we can generate a sequence of phonemes e =
[e1, e2, ..., en], which is also organized into syllables according
to the phonological rules of the target language.
For example, given the English word Manchester, its cor-
responding transliteration in Vietnamese is “man chét sờtơ”,
written in Vietnamese text. Syllables of a Vietnamese word
are separated by a whitespace. Vietnamese lexical tones are
denoted by diacritics above the nuclei of the syllables, except
tone 1 is not represented in text form by any diacritic mark.
2) Approaches: Symbolic systems for machine translitera-
tion encapsulates expert-deﬁned rules for mapping graphemes
of the source word to the target language, as well as handling
the mismatches between the pronunciation of the source and
target languages (such as the epenthesis of nuclei and deletion
of sound). In [51], an English-Chinese name transliteration
algorithm was devised using predeﬁned rules. An English
word was ﬁrst divided into syllables, each syllable is further
divided into sub-syllabic units. The sub-syllabic units were
mapped to Pinyin characters. The syllables in Pinyin were then
mapped to Chinese characters. The syllabiﬁcation rules were
deterministic and the phonetic mapping used a lookup table.
In [2], predeﬁned “phonetically similar” English-Japanese
(katakana) letters were used to derive English-Japanese symbol
pronunciation similarity matrices. To transliterate a new En-
glish word to Japanese, the decoder looked for the path that
maximizes the total similarity across all letters. An English-
Punjabi transliteration system of name entities was devised in
[52]. Rules were deﬁned to syllabify a source English word,
with each syllable subsequently being mapped to a Punjabi
syllable.
Standard statistical transliteration models are alignment-
based. During training, the model learns (1) the distribution of
how the source letters f are aligned to the target phonemes e
and (2) the distribution of how the aligned source letters f are
mapped to the target phonemes e. During decoding, the model
produces the sequence of target phonemes with the highest
likelihood.


## Page 3


IEEE TRANSACTIONS ON AUDIO, SPEECH, AND LANGUAGE PROCESSING
3
The early machine transliteration system requires an addi-
tional step to convert the source letters to source phonemes,
essentially convert the problem into a phoneme-to-phoneme
conversion [3][4][7][53]. In [7], transliteration was posed
as generative process and the English phonemes - Japanese
phonemes alignment was estimated with expectation maxi-
mization [54]. The same approach was applied to transliterate
English word to Arabic text [53]. An adaptation was made by
attaching the position of the vowel in a word (initial, medial,
ﬁnal) to each English vowel. The introduction of such contex-
tual information helps the model learn the mapping of English
letters to the less deterministically phonetic Arabic letters. In
[3], English-Chinese transliteration was also performed using
phonemic representation in an intermediate step. Instead of
aligning English phonemes to Chinese phonemes directly, the
English phonemes were aligned to sub-syllabic units (initial-
ﬁnal) of the Chinese word.
The second group of standard alignment-based machine
transliteration systems transform source graphemes to target
phonemes without an intermediate source graphemes to source
phonemes step. The English-Arabic transliteration system in
[4] performed two runs of alignment. In the ﬁrst run, English
letters were aligned to the Arabic characters and the most
often aligned n-grams of English letters were extracted for
the second run. In the second run, the selected English n-
grams were realigned to the Arabic characters. In [1], an
English-Chinese transliteration comprised of two steps, the
ﬁrst step used expert rules to append syllable nuclei to the
sequence of English phonemes and the second step modeled
the probabilities of mapping between English and Chinese
phonemes.
The third group of standard statistical transliteration models
uses a combination of methods. For example, the translitera-
tion system for Arabic in [19] combined both phonetic-based
and letter-based transliteration. The phonetic-based approach
made use of the positional information of the vowel as in
[53]. In [5], English-to-Korean transliteration was performed
by combining the output from an ensemble of grapheme-based
transliteration model, phoneme-based transliteration model,
and grapheme- and phoneme-based transliteration model. The
ﬁnal output was produced by ranking with web data and
relevance scores given by each transliteration model.
The joint source-channel model introduced in [55] (with
a similar approach implemented in [56]) approaches statisti-
cal transliteration differently. Under the joint source-channel
model, both the alignment and source-channel symbol map-
ping were handled intrinsically at the same time using inter-
mediate tokens (grapheme-phoneme cosegments) comprising
of both the source letters and the target phonemes. The
joint source-channel model has been shown to improve the
transliteration performance in various tasks (e.g. [57][58]) and
is used as the baseline for statistical transliteration in this work.
Recently, neural approaches have gained popularity in ma-
chine translation and other natural language processing tasks.
End-to-end deep learning models are different from statistical
transliteration models as they do not require explicit alignment
between the source graphemes and the target graphemes.
However, among the few work [59], [60] to date that applied
Source word
Pronunciation 
in Vietnamese
d_<
i
1
.
s
@:
3
.
n
i
1
.
l
E
n
1
Grapheme
|
Phoneme
Cosegment
D
I
S
N
E
Y
L
A
N
D
d_<
i
1
.
s
@:
3
.
n
i
D
I
S
N
E
Y
L
A
N
D
1
.
l
E
n
1
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
Vietnamese
text
đ
i
s
Ờ
n
i
l
e
n
Figure 1: Transliteration by the standard statistical transliter-
ation model (no explicit phonological knowledge)
Source word
Pronunciation 
in Vietnamese
d_<
i
1
.
s
n
i
1
.
l
E
n
?
Grapheme
|
Phoneme
Cosegment
D
I
S
N
E
Y
L
A
N
D
d_<
i
1
.
s
n
i
1
D
I
S
N
E
Y
L
A
N
D
.
l
E
n
1
2
3
4
5
6
7
8
9
10
11
12
13
Invalid consonant
cluster
Missing lexical
tone
đ
i
?
?
Vietnamese
text
Figure 2: Phonologically invalid transliteration output by the
standard statistical transliteration model.
neural approaches to machine transliteration, none have shown
that they outperform standard statistical approaches.
3) Limitations of statistical approach:
Figure 1 illus-
trates how transliteration is performed via the alignment of
grapheme-phoneme cosegments under the joint source-channel
model.
In this example, the English word DISNEYLAND is
transliterated to Vietnamese. The Vietnamese pronunciation is
represented by X-SAMPA symbols.
Each dotted box represents a cosegment of source word’s
graphemes and target pronunciation’s phonemes. The arrows
show the correspondence between the sequences of the English
graphemes and sequences of the Vietnamese phonetic tokens
via their cosegments. The grapheme-phoneme cosegments in
Figure 1 are the most likely sequence of cosegments given the
input graphemes, with the cosegments and their probability
distribution learned from a training dataset. The transliteration
output is the sequence of phonetic tokens extracted from the
most likely sequence of grapheme-phoneme cosegments. The
numbers of tokens 3, 7, 11 and 16 denote Vietnamese lexical
tones. The dot “.” of tokens 4, 8 and 12 are delimiters between
syllables. The Vietnamese pronunciation can be mapped to
Vietnamese text if the syllables conform to Vietnamese sylla-
bles’ structure4.
In the standard statistical model for transliteration, phones,
4The grapheme to phoneme mapping in Vietnamese is virtually one-to-
one, and lexical tones are embedded in diacritics in vowels. To more explicitly
explain the motivation and design philosophy of the transliteration framework,
we choose to use the X-SAMPA phonetic symbols to represent the Vietnamese
graphemes. The lexical tones are represented as diacritics that are above the
graphemes, but in X-SAMPA format lexical tones are represented numerically,
making it easier to explain the model.


## Page 4


IEEE TRANSACTIONS ON AUDIO, SPEECH, AND LANGUAGE PROCESSING
4
tones and syllabic delimiters of the target phonetic output
are treated equally. Since there is no phonological constraint
placed on the organization of the components of the target
pronunciation, transliteration is not guaranteed to produce
outputs with structures considered valid by the phonological
rules of the target language. Figure 2 illustrates a scenario of
which the standard transliteration model produces an output
that is invalid according Vietnamese phonology:
• In the second syllable, there is a consonant cluster sn
formed by phones at position 5 and 6. However, there is
no consonant cluster in Vietnamese phonology[31].
• In the third syllable, there is no lexical tone, while under
Vietnamese phonology, each syllable is assigned with one
tone[36].
Empirically, at least 21% of transliteration outputs lacked
lexical tones when we ran Sequitur [61] (an implementation of
the joint source-channel model) on 100 English - Vietnamese
word-pronunciation pairs extracted from NIST OpenKWS13
corpus [21].
III. PHONOLOGY-AUGMENTED STATISTICAL MODEL FOR
TRANSLITERATION
To overcome the limitations of the traditional statistical
transliteration model, we attempt to augment statistical translit-
eration with phonological knowledge. While many symbolic
systems have been devised to capture the phonological rules
involved in transliteration [2][20][51][52], predeﬁned rules
are likely to make mistakes with words not observed in the
training data. Symbolic approaches are thus outperformed
by statistical models in larger data sets [20]. On the other
hand, while statistical transliteration approaches like the joint
source-channel model [55][56] can capture the phonological
intricacies in converting a source word to a phonetically
equivalent in another language, such approaches require a
relatively large amount of training data to be effective [20].
To overcome the limitations of the traditional statistical
transliteration as well as the symbolic systems, we propose
a phonology-augmented statistical model for transliteration by
integrating phonological knowledge of the target language ex-
plicitly with a statistical model. Phonological constraints have
often been introduced to transliteration. To adapt statistical
machine translation tools into transliteration, many systems
ﬁrst converted the source written words into phonemes before
performing alignment with the target phonemes [3][4][7][53].
The initial grapheme to phoneme conversion implicitly pro-
jected the source graphemes into phonetic units, which could
be organized into sub-units of syllables [3]. Some systems
explicitly augmented the source word to improve the statistical
model. For example, in the English-to-Chinese transliteration
system described in [1], syllable nuclei were appended to
the sequence of English phonemes to improve the accuracy
of their conversion to Chinese. In [19][53], attaching the
position in a syllable (initial, medial, ﬁnal) to each English
vowel helped improve the mapping of English graphemes
to Arabic graphemes. In our proposed model, the positional
information of a unit in a syllable (onset, nucleus, coda) are
also used. Unlike [19][53], such contextual information is
Source word
1. Pseudo-syllables
formulation
N
EY
O
N
2. Pseudo-syllable-to-
phoneme mapping
n
i
3. Tone assignment
@: ‘schwa’
D
I
O
N
S
@:
O
N
d_<
i
s
@:
n
i
1
l
E
n
1
d_<
i
1
s
@:
3
D
I
S
N
E
Y
L
A
N
D
L
A
N
O
N
Cd
l
E
n
Tone
Nucleus
Onset
Coda
Figure 3: Phonology-augmented statistical model for translit-
eration
used to inform the cross-language mapping of not just the
nucleus, but also the onset and coda. Imposing conditions
on the structure of the output syllables helps to improve
the phonological validity of the transliteration output, and
yet remains generalizable across languages. The same syl-
labic structure is shared across most languages [28][29] and
thus, utilizing this universal phonological property keeps the
proposed framework relatively language-independent. On the
other hand, when the transliteration output conforms to valid
syllabic structures, the search space for the output is also
bounded, which might make ﬁnding the correct output easier.
For example, the consonant “l” in English can be mapped
to different Vietnamese phonemes. However, conditioned on
the corresponding sub-syllabic unit that “l” is mapped to
in the output syllable, the number of possibilities would be
smaller: “l” is more likely to correspond to an /n/ phoneme
in Vietnamese if it is at the Coda position, and more likely to
correspond to an /l/ phoneme if it is at the Onset position.
Furthermore, transliteration is performed directly from the
source graphemes to the target phonemes. By avoiding using
the intermediate source phonemes, the proposed model does
not assume the speciﬁc language of the source word.
The proposed model performs translieration in three steps,
as summarized in Figure 3.
1) Pseudo-syllable formulation: graphemes of the source
word
are
organized
into
pseudo-syllables.
Source
graphemes are assigned explicitly to the sub-syllabic
units of each pseudo-syllable such that the units form
valid syllabic structures deﬁned by the target language’s
phonology.
2) Pseudo-syllable-to-phoneme mapping: a language model
is used to map the graphemes of each pseudo-syllable,
given their assigned unit in a syllable, to the most likely
phonemes.
3) Tone assignment: one tone is assigned to each syllable,
based on the target language’s phonemes in each sylla-
ble.
A. Pseudo-Syllable Formulation
1) Scheme: Pseudo-syllable is a representation of how
segments of a foreign word are arranged according to the
syllable structure speciﬁed by the target language’s phonology.
The concept is inspired by how native speakers process a
foreign loanword by imposing native phonological constraints


## Page 5


IEEE TRANSACTIONS ON AUDIO, SPEECH, AND LANGUAGE PROCESSING
5
Source word
(1) Graphemic
labels assignment
n
Cd4
(2) Sub-syllabic
components 
formation
Vietnamese 
pronunciation
(with syllabic 
structures’ 
labeling)
d_<
O1
n
O3
S
O2
l
E
n
n
i
d_<
i
s
@:
i
N1
@:
N2
l
O4
E
N4
i
N3
O
N
Cd
O
N
O
N
O
N
s1
s2
s4
s3
D
I
S
N
E
Y
L
A
N
D
O
N
ON
O
N
N
O
N
Cd
X
1
2
3
4
5
6
7
8
9
10
Figure 4: Pseudo-syllable formulation
on the foreign word’s form [7][45]. A pseudo-syllable’s
structure is deﬁned as: si = {[sO
i ], sN
i , [sCd
i
]}, where sO
i ,
sN
i , sCd
i
are the Onset, Nucleus and Coda of the i-th
pseudo-syllable respectively. Onset, Nucleus and Coda are
sub-syllabic units constituting a syllable.
i. Graphemic labels assignment
To form pseudo-syllables from a source word, a segmenta-
tion function groups the source word’s graphemes into sub-
syllabic units. Pseudo-syllables are formulated by grouping
graphemes of the source word according to the labels that
they are assigned to. The labels suggest which sub-syllabic
unit the grapheme would be assigned to, and the grapheme’s
relation with neighboring graphemes. For illustration, we will
use ﬁve labels O, N, Cd, ON, X in our discussion:
• O: Onset
• N: Nucleus
• Cd: Coda
• ON: Onset, with a special token representing a new
Nucleus inserted to the pseudo-syllable containing this
Onset. This label addresses the insertion phenomenon
explained in Section II-A3.
• X: eXcluded. Graphemes labelled by X are not assigned
to any pseudo-syllable. This label addresses the deletion
phenomenon explained in Section II-A3.
The sequence of labels assigned to all graphemes of a source
word is the output of the pseudo-syllabic formulation step.
ii. Sub-syllabic units formation
2) Ground-truth: To train a model for pseudo-syllabic
formulation, a ground-truth of graphemic labels need to be
determined from the original training pairs of original source
words and target pronunciation. For a given training pair,
a search is performed among all possible combinations of
graphemic labels in order to ﬁnd the candidate combination
that produces a sequence of pseudo-syllables of the same
structures as the target pronunciation’s. To reduce the com-
putational complexity of the search, any partial sequence of
graphemic labels that produces invalid pseudo-syllables (for
example, pseudo-syllables that start with a coda) would be
rejected without iterating through the remaining graphemes.
Step 1 of Figure 4 shows an example of a combination of
graphemic labels. Given the sequence of graphemic labels in
the ﬁgure, the corresponding pseudo-syllables are formed as
follows:
• Labels at position 1, 4 and 7 are O. Therefore, the
corresponding graphemes ‘D’, ‘N’ and ‘L’ are assigned to
the Onsets of pseudo-syllables s1, s3, and s4 respectively.
• Labels at position 2, 5, 6 and 8 are N. Therefore, the
corresponding graphemes are assigned to the Nuclei of
the pseudo-syllables. Note that since the graphemes ‘E’
and ‘Y’ at position 5 and 6 are adjacent and both given
label N, they are joined to form the Nucleus of pseudo-
syllable s3.
• Label at position 3 is ON. Therefore, the corresponding
grapheme ‘S’ is assigned to the Onset of pseudo-syllable
s1. A special token (@ :) is also inserted to the Nucleus
position of pseudo-syllables s1, representing an epenthe-
sized nucleus.
• Label at position 10 is X. Therefore, the corresponding
grapheme ‘D‘ is ignored.
The resulting pseudo-syllables of the word DISNEYLAND are
shown in Figure 4 as dotted boxes, with:
• s1={D, I}, where sO
1 ={D}, sN
1 ={I}
• s2={S, @:}, where sO
2 ={S}, sN
2 ={@:}
• s3={N, EY} where sO
3 ={N}, sN
3 ={EY}
• s4={L, A, N} with sO
4 ={L}, sN
4 ={A}, and sCd
4 ={N}
The graphemic labels in Figure 4 shows a valid pseudo-
syllable formulation since the pseudo-syllables have the same
syllabic structures O N . O N . O N .O N Cd as the
syllables of the target pronunciation.
3) Training: Given a training example consisting of a pair
of foreign word f = [f1, f2, ..., fM] and its corresponding
phonetic output e = [e1, e2, ..., eN], the corresponding training
example for graphemic labels can be deduced as follows:
Let l = [l1, l2, ..., lM] be the sequence of graphemic labels
assigned to the graphemes sequence f. For 1 ≤m ≤M,
lm ∈L where L is the set of all possible graphemic labels,
L = {O, N, Cd, ON, X}.
Let Γ(f, l) be the function to form sub-syllabic units from
the sequence of graphemes f and sequence of graphemic labels
l as described in Section III-A-ii. Function Γ is deﬁned as:
Γ(f, l) = s = [s1, s2, ..., sK]
(2)
= [(sO
1 , sN
1 , sCd
1 ), ..., (sO
K, sN
K, sCd
K )]
(3)
where s = [s1, s2, ..., sK] is a sequence of pseudo-syllables,
with (sO
k , sN
k , sCd
k ) being the groups of graphemes assigned to
the Onset, Nucleus and Coda unit of the k-th pseudo-syllable
respectively.
A sequence of graphemic labels is found for f and e if
the syllabic structures rs of the pseudo-syllables s match
the syllabic structures re of the target pronunciation e. For
example, in Figure 4, the syllabic structures rs and re are both
[O, N], [O, N], [O, N], [O, N, Cd]. The syllabic structures
re of the target pronunciation e can be trivially determined
using a pronunciation-subsyllabic unit dictionary of the target
language. For example, in the case of target transliteration
output for Vietnamese, the language speciﬁc document of the
OpenKWS13 is used as the pronunciation-subsyllabic unit


## Page 6


IEEE TRANSACTIONS ON AUDIO, SPEECH, AND LANGUAGE PROCESSING
6
dictionary [21]. The syllabic structures rs can be directly
determined from the pseudo-syllables s.
4) Decoding: We want to ﬁnd the most likely graphemic
roles l for all letters of the new example f:
l∗
= arg maxl p (l | f, D)
(4)
where D is the training data of graphemic labels produced in
the previous section.
We model l as a Markov chain of n-gram, with n being an
even number:
l∗
= arg maxl
QM
i=1 p
 li |
 fi−n/2, ..., fi+n/2

(5)
5) Smoothing: To deal with data sparsity, li in Eq. (5) is
estimated from a weighted score of probability of smoothed
n-grams:
q (li)
= Pn/2
k=0
Pn/2
t=0 ωk,tp

li |

f ′
i−n/2, ..., f ′
i+n/2

(6)
where (f ′
i−n/2, ..., f ′
i+n/2) is a smoothed n-gram such that
given 0 ≤k, t ≤n/2 (n is an even number):
f ′
j =









fj if i −n/2 + t ≤j ≤i + n/2 −k
otherwise





C
if fj is a consonant
V
if fj is a vowel
if fj is C or V
where the empty token
represents the back-off case of
which the smoothed n-gram is the shortened version of
the original n-gram. For example, given the tri-gram of
letters (B, E, S), its smoothed n-grams are {(B, E, S), (C ,
E, S), (B, E, C ), (C , E, C ), ..., (V )}. ωk,t is the weight
corresponding to the smoothed n-gram, with ωk,t > ωk′,t′ for
k +t < k′ +t′; for example: ω1,0 (corresponding to (C , E, S))
> ω1,1 (corresponding to (C , E, C )).
B. Pseudosyllable-to-Phoneme Mapping
Transliteration takes into account (1) graphemes of the
source word, (2) how the word is pronounced in the source
language, and (3) phonological rules of the target language
[36][45]. A formal equation of such relation can be given by:
e∗= arg max
e
p (e | f, v, Le)
(7)
where e is the phonemes of the target language’s pronuncia-
tion, f and v are the graphemes and phonemes of the original
word from the source language, and Le is the phonological
rules of the target language.
In the proposed model, the relationship in Eq. (7) is sim-
pliﬁed to:
e∗
= QK
k=1
Q
u∈U arg maxeu
k p (eu
k | su
k, vu
k)
(8)
with eu
k, su
k, vu
k being the target language’s phoneme, source
language’s graphemes and source language’s phoneme of the
sub-syllabic unit u ∈U = {O, N, Cd}, of the k-th syllable
in the target pronunciation or the k-th pseudo-syllable of the
source word.
The source phonemes are produced with CMU text-to-
phoneme tool for American English [62]. Note that we do
Source graphemes
N
N
D
D
N
N
S
Z
i
i
I
IY
@:
_
L
L
A
AE
EY
EY
Syllable’s index
1
2
3
4
d_<
s
@:
l
E
n
n
N
O
N
O
N
O
N
O
Cd
Source phonemes
Target phonemes
Sub-syllabic role
Figure 5: Pseudo-syllable-to-Phoneme mapping with phono-
logical constraint
not assume that the source words are in English, the source
phonemes are only used as back-off to complement the source
graphemes in performing the pseudo-syllables to phonemes
mapping.
The mapping from pseudo-syllables to phonetic tokens
in the proposed model is illustrated in Figure 5. As seen
from Figure 5, pseudo-syllables formulated in Section III-A
provide a streamlined model of the phonological constraints
Le by modeling (1) valid syllabic structures in the target
pronunciation, and (2) valid phonemes for each sub-syllable
unit r. The distribution p (eu
k | su
k, vu
k) of Eq. 8 can be learned
from the training data prepared in Section III-A.
C. Lexical Tone Assignment
In most transliteration models, lexical tones are treated the
same as other phonetic tokens of the transliterated output.
Lexical tone assignment usually depends on large amounts
of training data to be correct [3][55]. Previous translitera-
tion studies using tone assignment to complement output of
statistical models have shown improvement in transliteration
performance [42][63].
Phonology studies show that in many tonal languages, the
assignment of a lexical tone to a syllable is inﬂuenced by the
syllable’s phonemes [36][64], and the lexical tones of adjacent
syllables (tone sandhi) [65][66]. Similarly, we used tonal and
phonetic context to model tone assignment to a syllable.
Let t be the lexical tones assigned to all syllables of a
transliteration output, with tk being the lexical tone assigned
to the k-th syllable of the output.
t = arg max
t
Y
k
p
 tk | tk−1, (eO
k , eN
k , eCd
k ), tk+1

(9)
where (eO
k , eN
k , eCd
k ) are phonemes of the Onset, Nucleus, and
Coda sub-syllabic unit in the k-th syllable of the output.
IV. EXPERIMENTS
A. Transliteration for different language pairs
1) Experimental set-up: We performed transliteration on
corpora of two language pairs: English-to-Vietnamese and
English-to-Cantonese5.
a) English-to-Vietnamese Corpus from NIST OpenKWS13
Evaluation: The Vietnamese corpus is released from the
IARPA Babel program [21] for the NIST OpenKWS13 Eval-
uation (denoted as NIST OpenKWS13 dataset). From the
5It might be more linguistically precise to say Western-to-Vietnamese
and Western-to-Cantonese, given some of the English words are not of
Anglophone origin.


## Page 7


IEEE TRANSACTIONS ON AUDIO, SPEECH, AND LANGUAGE PROCESSING
7
scripted telephone speech of the OpenKWS13 lexicon, for-
eign words in the developmental data (evalpart1, which was
publicly released) were designated as the test set (140 words)
and shared among all experiments. Training-development data
sub-corpora of size 100, 200, 300, 400, 500, 587 were also
extracted. Each sub-corpus is split by the proportion of 75%
to 25% into training and development sets. Each sub-corpus
is repartitioned 4 times to create 4 different, non-overlapping
training-development data sets. Each phonetic output of the
foreign words is a sequence of Vietnamese phonemes in X-
SAMPA [39] and one lexical tone (represented by a number
from 1 to 6), separated by syllabic delimiters. The setup is
described in details in [20].
b) English-to-Cantonese Corpus from Hong Kong Poly-
technic University: This corpus comprises of 473 pairs of
foreign words and their corresponding Cantonese pronuncia-
tions, extracted from a database of English loanwords in Hong
Kong Cantonese, developed at the Hong Kong Polytechnic
University [67] (denoted as Hong Kong Polytechnic Cantonese
dataset).
Each pronunciation is a sequence of syllables of Cantonese
in Jyutping [68] and one lexical tone (represented by a number
from 1 to 6), separated by syllabic delimiters6. Sub-corpora of
size 100, 200, 300, 400 and 473 were randomly sampled for
the experiments. Each sub-corpus of the Cantonese data set
was split randomly into three sets, 60% for training the models,
20% for development, and 20% testing. Each sub-corpus is
repartitioned 5 times to create 5 different, non-overlapping test
sets (cross-validation).
2) Implementation Details: In each experiment, transliter-
ation was performed using three different approaches:
a) Standard statistical approach (no phonological con-
straint): joint source-channel model implemented with Se-
quitur [61].
b) Symbolic approach: two symbolic systems for Viet-
namese and Cantonese were implemented for the respective
transliteration experiments of the two languages. The sym-
bolic transliteration system used in these experiments was
ﬁrst proposed for Vietnamese language in [20] and further
extended to Cantonese (Appendix A). The symbolic systems
was optimized to the best of our capabilities to minimize the
string error rate of the outputs. The error rates by the symbolic
systems served as reference to compare the performance by
the statistical models.
c) Proposed phonology-augmented statistical model for
transliteration.
3) Evaluation Metrics: The error rates computed in our
experiments were evaluated using SCLITE [69]:
a) Token error rate (TER): Tokens include both phonemes
and syllable delimiters.
b) String error rate (SER): Any error within a string results
in string error.
6For Cantonese, we chose to use Jyuping (phoneme-baed graphemes)
instead of logographic graphemes due to the following reasons: (1) Jyuping
explicitly represents lexical tones, while logographic graphemes usually do not
embed lexical tone information; (2) Logographic graphemes lack a standard
system in Cantonese, especially for words speciﬁc to Cantonese and have no
equivalent counterpart in Mandarin. We have a separate piece of work on
pronunciation modeling for Han logographic languages under review.
B. Results
In all experiments on Vietnamese and Cantonese cor-
pora, the phonology-augmented statistical framework im-
proved upon the transliteration performance of the standard
joint-source channel model under limited-resource scenarios.
As training data sizes increased, the transliteration perfor-
mance by statistical models improved and caught up with
the symbolic system’s performance. Transliteration error rates
by the symbolic system for Vietnamese in Figures 6a - 6b
(and also in Figure 8a - 8e) are ﬂat across all sizes of
the training data because the same test set was used. On
the other hand, transliteration error rates by the symbolic
system for Cantonese in Figures 7a - 7b (and also in Figure
9a - 9e) vary across different corpus sizes because some
words that overlap across different folds of the cross-validation
contributed multiple times to the error rates, even though the
symbolic system would produce the same outputs for these
input words.
1) English-to-Vietnamese: From Figures 6a - 6b, we see
that the proposed model consistently outperforms the statis-
tical baseline across all the training set sizes for English-to-
Vietnamese.
The proposed model outperforms the baselines at the small-
est training data size (100 word pairs): it improves the joint
source-channel model by 23.71% relative in TER and by
15.85% relative in SER. The proposed model outperforms the
baselines at the largest training data size (587 word pairs): it
improves the joint source-channel model by 29.74% relative
in TER and by 16.89% relative in SER. The proposed model
also improves the symbolic system by 15.98% relative in TER.
2) English-to-Cantonese: From Figures 7a - 7b, we observe
that the proposed model outperforms the statistical baseline
across all the training set sizes for English-to-Cantonese.
The proposed model outperforms the baselines at the small-
est corpus size (100 word pairs): it improves the joint source-
channel model by 12.77% relative in TER and by 2.27%
relative in SER.
The proposed system outperforms the statistical baseline at
the largest corpus size (473 word pairs) by 7.83% relative in
TER and by 4.23% relative in SER. The proposed model also
improves the the symbolic system by 3.51% relative in TER.
C. Further Analysis on Syllabic and Sub-Syllabic Structure
Since the phonological knowledge of syllabic structures are
used to better guarantee well-formed syllables in the translit-
eration output, we want to have a more detailed analysis of
improvement by the proposed model over traditional statistical
model at individual sub-syllabic positions.
a) Syllabic error rate: A syllable is the combination of to-
kens (for both phonemes and tones) within a pair of syllable’s
delimiters. Each syllable is treated as a token and the error
rate was computed as token error rate using SCLITE.
b) Onset, Nucleus, Coda, and Tone error rate: To compute
the syllable error rate, the hypothesis and reference syllables
are aligned to minimize the error distance between the two
sequences. From these aligned sequences, output and reference
syllables with the same number of sub-syllabic units are


## Page 8


IEEE TRANSACTIONS ON AUDIO, SPEECH, AND LANGUAGE PROCESSING
8
(a) Token error rate
15
20
25
30
35
40
100
200
300
400
500
Token error rate
Training data size
Rule-based
Joint source-channel
Proposed
(b) String error rate
45
55
65
75
85
100
200
300
400
500
String error rate
Training data size
Rule-based
Joint source-channel
Proposed
Figure 6: Performance of different transliteration models
as a function of corpus size (Vietnamese dataset - NIST
OpenKWS13 dataset).
extracted. A sub-syllabic unit is counted as incorrect if it is
different from the corresponding reference unit. Note that since
the error rates of sub-syllabic units are only computed for the
subset of output and reference syllables with the same number
of units, we only approximate the actual error rates of the sub-
syllabic units.
1) Vietnamese: As shown in Figures 8a - 8e, the proposed
model consistently outperforms the statistical baseline for
all sub-syllabic units across all the training set sizes for
Vietnamese. At the smallest training data size (100 entries),
the proposed model improves the joint source-channel model
by 16.62% relative for syllable error rate, 27.97% relative for
onset, 33.29% relative for nucleus, 15.25% relative for coda,
and 33.51% relative for tone error rate.
At the largest training data size (587 entries), the proposed
model improves the joint source-channel model by 22.33%
relative for syllable error rate, 39.06% relative for onset,
27.52% relative for nucleus, 29.90% relative for coda, and
44.68% relative for tone error rate. The proposed model also
improves the symbolic system by 1.42% relative for syllable
error rate, 28.57% relative for coda error rate, and 32.32%
relative for tone error rate.
2) Cantonese: As shown in Figures 9a - 9e, the proposed
model consistently outperforms the statistical baseline for all
sub-syllabic units across all the training sets for Vietnamese.
At the smallest training data size (100 entries), the proposed
(a) Token error rate
40
45
50
55
60
65
100
200
300
400
Token error rate
Corpus size
Symbolic
Joint source-channel
Proposed
(b) String error rate
85
90
95
100
100
200
300
400
String error rate
Corpus size
Symbolic
Joint source-channel
Proposed
Figure 7: Performance of different transliteration models as
a function of corpus size (Hong Kong Polytechnic Cantonese
dataset).
model improves the joint source-channel model by 3.92%
relative for syllable error rate, 22.37% relative for onset,
10.27% relative for nucleus, 6.84% relative for coda, and
12.34% relative for tone error rate.
At the largest training data size (473 entries), the proposed
model improves the joint source-channel model by 3.33%
relative for syllable error rate, 9.38% relative for onset, 2.06%
relative for nucleus, 17.45% relative for coda, and 8.69%
relative for tone error rate.
V. DISCUSSION
A. Statistical modeling with phonological knowledge
The proposed framework can be interpreted as a statistically
grounded framework that adopts symbolic transliteration con-
cepts. The proposed framework uses pseudo-syllables to deﬁne
the general constraints on the structure of the transliteration
output: how graphemes of the source word should conform
to the phonology of the target language’s syllables. From the
training data, the framework learns speciﬁc distributions of
the combinations of graphemes that constitute the pseudo-
syllables, the mapping of individual units of the pseudo-
syllable to the target language’s phonemes, and the assignment
of tones to each of the syllables. As a result, the transliteration
performance of the proposed framework improves as the data
sizes increase while the performance of the symbolic model
is constant across all data sizes, as shown in Figure 6 - 9.


## Page 9


IEEE TRANSACTIONS ON AUDIO, SPEECH, AND LANGUAGE PROCESSING
9
In [70], we offered a more detailed analysis on the trade-off
between data size and performance for the different models.
Using a larger corpus (HCMUS corpus [57]), we compared
the transliteration performance using TER and SER for the
proposed framework, the standard joint-source channel model
and the symbolic model. The proposed framework performs
better than the symbolic system in TER for all corpus sizes
larger than 350 words, and better than the symbolic system in
all three metrics for all corpus sizes larger than 1,000 words.
While symbolic frameworks for transliteration are still
highly valuable when little training data is available, they
are also non-trivial to derive. We constructed two symbolic
frameworks for Vietnamese and Cantonese with the idea of
sharing as much general basic principles between them as
possible. Nonetheless, while we tried our best to optimize
their performance in terms of the string error rate (Figure
6b and Figure 7b), there are obviously many cases that our
rules failed to capture, as evident by the high token error
rate (Figure 6a and Figure 7a) and sub-syllabic unit error
rates (Figure 8a - Figure 8e and Figure 9a - Figure 9e) as
compared to the statistical models. Such difﬁculties would
deﬁnitely render it highly challenging to extend a symbolic
transliteration framework to other languages, or even different
dialects of the same language.
The proposed approach ensures the transliteration output is
valid, as speciﬁed by the target language’s phonology. Figure
8a and 9a show that the proposed framework consistently
improves the syllables’ error rate of the baseline statistical
model across all languages and all data sizes. This evidence
veriﬁes the strength of the proposed approach. By augment-
ing a statistical model for transliteration with phonological
knowledge, the proposed model better captures the syllabic
structures and syllabic boundaries in scenarios with limited
linguistic resources.
B. Future Extensions
In our analysis of data size vs. performance trade-off be-
tween different transliteration models for Vietnamese language
in [70], the phonology-augmented statistical framework per-
forms consistently better than the joint source-channel model
for corpora of size up to 1,500 word pairs. The joint source-
channel model caught up with the proposed framework for
corpora of size 1,500 word pairs and more. In our analysis
for other languages with readily available large datasets for
transliteration such as Mandarin and Japanese, we observe a
similar trend. We suspect that such performance differences
could be due to different model assumptions. Below we
elaborate on some future extensions to potentially improve
the proposed framework.
1) Modeling inter-syllable context: In the proposed frame-
work, pseudosyllable-to-phoneme mapping and tone assign-
ment is contained within each syllable’s boundary. From our
preliminary analysis, it is possible that inter-syllable context
of phonemes may play some role in determining grapheme
to phoneme mapping, as well as how a tone can be assigned
to a syllable. Without considering syllable’s boundaries, the
traditional transliteration model can capture such inter-syllabic
context more easily and produces better performance given
sufﬁcient training data.
2) Beyond monosyllabic tonal languages: In this work, we
focus on monosyllabic tonal languages that share a similar
phonological structure and lexical tones. The proposed model
can be applied to languages such as Korean which, while
not tonal, share similar syllable structures as Vietnamese and
Cantonese.
3) End-to-end modeling: Each of the three steps of the
proposed model is optimized separately, which means an error
in one step is propagated to the next with no mechanism to
correct the mistake in a later step. The statistical baseline
models syllabic segmentation, grapheme to phoneme and tone
assignment together using the joint source-channel sequences,
and thus, performs optimization for all the steps together.
Approaches that we are currently exploring include genera-
tive models such as Bayesian graphical models, variational
autoencoders, and generative adversarial networks (GANs).
VI. CONCLUSION
We proposed a phonology-augmented statistical framework
for transliteration. Using phonological knowledge to augment
the statistical n-gram language modeling, our proposed frame-
work ensures the transliteration outputs are valid, resulting
in lower error rates compared with baseline approaches in
limited-resources scenarios. On the other hand, using the
concept of pseudo-syllables as an additional phonological con-
straint, while being largely generic and language-independent,
offers an approach to automate the learning of syllable for-
mulation instead of relying on exhaustive effort to build
predeﬁned symbolic systems.
ACKNOWLEDGMENT
The authors would like to thank Mr. Risheng Gao’s expertise
in Cantonese and Mandarin in helping us preprocess the data.
The authors would also like to thank Dan Jurafsky and Mark
Hasegawa-Johnson, Haizhou Li, and Bin Ma for the insightful
discussions that helped improve the manuscript.


## Page 10


IEEE TRANSACTIONS ON AUDIO, SPEECH, AND LANGUAGE PROCESSING
10
(a) Syllable error rate
30
35
40
45
50
55
60
100
200
300
400
500
Syllable error rate
Training data size
Rule-based
Joint source-channel
Proposed
(b) Onset error rate
10
15
20
25
30
35
40
100
200
300
400
500
Onset error rate
Training data size
Rule-based
Joint source-channel
Proposed
(c) Nucleus error rate
15
20
25
30
35
40
45
100
200
300
400
500
Nucleus error rate
Training data size
Rule-based
Joint source-channel
Proposed
(d) Coda error rate
15
20
25
30
35
40
45
100
200
300
400
500
Coda error rate
Training data size
Rule-based
Joint source-channel
Proposed
(e) Tone error rate
10
15
20
25
30
35
40
100
200
300
400
500
Tone error rate
Training data size
Rule-based
Joint source-channel
Proposed
Figure 8: Performance of different transliteration models
as a function of corpus size (Vietnamese dataset - NIST
OpenKWS13 dataset).
(a) Syllable error rate
70
75
80
85
90
95
100
200
300
400
Syllable error rate
Corpus size
Symbolic
Joint source-channel
Proposed
(b) Onset error rate
25
30
35
40
45
50
55
100
200
300
400
Onset error rate
Corpus size
Symbolic
Joint source-channel
Proposed
(c) Nucleus error rate
50
55
60
65
70
75
100
200
300
400
Nucleus error rate
Corpus size
Symbolic
Joint source-channel
Proposed
(d) Coda error rate
35
40
45
50
55
60
65
70
100
200
300
400
Coda error rate
Corpus size
Symbolic
Joint source-channel
Proposed
(e) Tone error rate
45
50
55
60
65
70
100
200
300
400
Tone error rate
Corpus size
Symbolic
Joint source-channel
Proposed
Figure 9: Performance of different transliteration models as
a function of corpus size (Hong Kong Polytechnic Cantonese
dataset).


## Page 11


IEEE TRANSACTIONS ON AUDIO, SPEECH, AND LANGUAGE PROCESSING
11
APPENDIX A
SYMBOLIC FRAMEWORK
Our symbolic cross-lingual framework was ﬁrst proposed
for Vietnamese language in [20]. The proposed framework was
mainly a phoneme-to-phoneme system with the source words’
phones produced by a text-to-phoneme tool for American En-
glish [62], before being mapped to Vietnamese phonemes. We
have since extended the symbolic framework to Cantonese by
directly using the source words’ graphemes for the conversion.
Using the source words’ graphemes, we can make use of
the richer context of the graphemes without making strong
assumptions on the source words’ origin. On the other hand,
the algorithm of the symbolic framework remains the same.
A. Outline of the Symbolic Framework for Cantonese
Input: graphemes of a source word.
Output: a sequence of phonetic tokens of the target language
that includes phonemes, syllabic delimiters and lexical tones.
Cantonese phonemes are represented in Jyutping [68].
1) Syllable-splitting: Similar to Vietnamese, Cantonese is
also a monosyllabic tonal language [71]. Hence, the
strategy used for forming syllables in Cantonese is also
similar to that for Vietnamese [20].
a) Segmentation:
Graphemes of the source word
are segmented into vowel clusters and consonant
clusters.
b) Role assignment:
* From the sequence of segments in the previous
step, vowel clusters are assigned to Nucleus units.
* Consonant clusters are assigned to Onset and
Coda units as followed:
- If the cluster has one consonant, it is assigned to
the Onset role because <Consonant-Vowel> struc-
ture is more common than <Vowel-Consonant> or
<Vowel> structure [72].
- If the cluster has two consonants or more, the
cluster is split into two parts: (1) the ﬁrst part is
assigned to the Coda of the preceding syllable, (2)
the second part is assigned to the Onset of the
following syllable
c) Post-processing:
* Some Vowel clusters are split up to form the
Nucleus of two adjacent syllables of the structures
<Onset-Nucleus>, <Nucleus-Coda>.
2) Grapheme-to-phoneme mapping: Each of the source
word’s sub-syllabic units are mapped to a target pronun-
ciation’s phoneme [45][46][51][73][74][75]. There are
also more speciﬁc mapping rules that use the context of
preceding and following sub-syllabic units of the source
word’s graphemes to perform the mapping.
3) Lexical tone assignment: A lexical tone is assigned to
each of the target pronunciation’s syllables based on its
phones.
Figure 10 shows how the world ALBANIA is transliterated
to Cantonese under the symbolic framework.
Source word
A
Role assignment
A
L
B
A
L
B
A
N
I
A
N
IA
Segmentation
A
L
N
IA
B
A
A
N
I
B
A
L
A
Post-processing
Cantonese(Jyutping)
Phone mapping
aa
n
ei
b
aa
aa
j
i
Lexical tone 
assignment
aa
3
n
ei
4
b
aa
1
aa
3
j
i
5
Figure 10: Example of the symbolic transliteration framework
for Cantonese
B. Compensation Strategies
When converting words from one language to pronunciation
in another, there are compensations need to be made such
that the output pronunciation does not only best retain the
acoustic authenticity of the source word, but also conforms to
the target language’s phonology. We present in the following
sections some of the compensation strategies used for Can-
tonese transliteration, with respect to each sub-syllabic unit.
1) Onset:
Since Cantonese does not have consonant
clusters, these clusters are split, with the epenthesis vowels
added to form new syllables[46][73].
English
greenland
Cantonese (Jyutping)
g aa k 3 . l i ng 4 . l . aa . n 4
2) Coda:
For consonant clusters in Coda role, both
epenthesis and deletion are valid compensation strategies for
Cantonese language [73][76]. For example, given the source
word BOLT, vowel insertion occurs for both l and t.
English
bolt
Cantonese (Jyutping)
b o 1 . j i 5 . d a k 6
However, given the source word FORD, vowel insertion
only applies to d while r is deleted.
English
ford
Cantonese (Jyutping)
f u k 1 . d a k 6
For consonant clusters where the ﬁrst letter is a liquid,
for example r in the consonant cluster rt, the liquid is usually
deleted. This is because liquid is not salient compared to
its neighboring phones and therefore is not perceived by
Cantonese speakers [45][46][74]. Thus, the liquid is likely
to be deleted in the output pronunciation. Furthermore, in
Cantonese, Codas are either stop or nasal [45].
C. Lexical tones
There are some patterns for lexical tones observed among
the Cantonese loanwords in our experimental data.
• Syllables with “p”, “t” or “k” as Coda only accept tone
1, 3 or 6.
• 95% of syllables with “p” as Coda have either tone 3 or
tone 6.
• 90% of syllables with “m” as Coda have either tone 1 or
tone 4.


## Page 12


IEEE TRANSACTIONS ON AUDIO, SPEECH, AND LANGUAGE PROCESSING
12
REFERENCES
[1] H. M. Meng, W.-K. Lo, B. Chen, and K. Tang, “Generating phonetic
cognates to handle named entities in english-chinese cross-language
spoken document retrieval,” in Automatic Speech Recognition and Un-
derstanding, 2001. ASRU’01.
IEEE, 2001, pp. 311–314.
[2] A. Fujii and T. Ishikawa, “Japanese/english cross-language information
retrieval: Exploration of query translation and transliteration,” Comput-
ers and the Humanities, vol. 35, no. 4, pp. 389–420, 2001.
[3] P. Virga and S. Khudanpur, “Transliteration of proper names in cross-
language applications,” in Proceedings of the 26th Annual International
ACM SIGIR Conference on Research and Development in Informaion
Retrieval, ser. SIGIR ’03.
New York, NY, USA: ACM, 2003, pp. 365–
366. [Online]. Available: http://doi.acm.org/10.1145/860435.860503
[4] N. AbdulJaleel and L. S. Larkey, “Statistical transliteration for english-
arabic cross language information retrieval,” in Proceedings of the
twelfth international conference on Information and knowledge man-
agement.
ACM, 2003, pp. 139–146.
[5] J. H. Oh and K. S. Choi, “An ensemble of transliteration models for
information retrieval,” Information processing & management, vol. 42,
no. 4, pp. 980–1002, 2006.
[6] Y. Marton and I. Zitouni, “Transliteration normalization for information
extraction and machine translation,” Journal of King Saud University-
Computer and Information Sciences, vol. 26, no. 4, pp. 379–387, 2014.
[7] K. Knight and J. Graehl, “Machine Transliteration,” Computational
Linguistics, vol. 24, no. 4, pp. 599–612, Dec. 1998. [Online]. Available:
http://dl.acm.org/citation.cfm?id=972764.972767
[8] Y. Al-Onaizan and K. Knight, “Translating named entities using mono-
lingual and bilingual resources,” in Proceedings of the 40th Annual
Meeting on Association for Computational Linguistics.
Association
for Computational Linguistics, 2002, pp. 400–408.
[9] U. Hermjakob, K. Knight, and H. Daum´e III, “Name translation in sta-
tistical machine translation-learning when to transliterate,” Proceedings
of ACL-08: HLT, pp. 389–397, 2008.
[10] N. Durrani and P. Koehn, “Improving machine translation via trian-
gulation and transliteration,” in Proceedings of the 17th Annual Con-
ference of the European Association for Machine Translation (EAMT),
Dubrovnik, Croatia, 2014.
[11] N. Durrani, H. Sajjad, H. Hoang, and P. Koehn, “Integrating an un-
supervised transliteration model into statistical machine translation,” in
Proceedings of the 14th Conference of the European Chapter of the
Association for Computational Linguistics, volume 2: Short Papers,
2014, pp. 148–153.
[12] A.
Mansikkaniemi
and
M.
Kurimo,
“Unsupervised
Vocabulary
Adaptation for Morph-based Language Models,” in Proceedings of
the NAACL-HLT 2012 Workshop: Will We Ever Really Replace
the N-gram Model? On the Future of Language Modeling for
HLT,
ser.
WLM
’12.
Stroudsburg,
PA,
USA:
Association
for
Computational Linguistics, 2012, pp. 37–40. [Online]. Available:
http://dl.acm.org/citation.cfm?id=2390940.2390945
[13] P. Schone, “Low-resource autodiacritization of abjads for speech key-
word search,” in Ninth International Conference on Spoken Language
Processing, 2006.
[14] S. Zhang, Z. Shuang, and Y. Qin, “Automatic pronunciation transliter-
ation for chinese-english mixed language keyword spotting,” in Pattern
Recognition (ICPR), 2010 20th International Conference on.
IEEE,
2010, pp. 1610–1613.
[15] N. F. Chen, S. Sivadas, B. P. Lim, H. G. Ngo, H. Xu, V. T. Pham, B. Ma,
and H. Li, “Strategies for Vietnamese Keyword Search,” in ICASSP,
2014.
[16] R. Eklund and A. Lindstrom, “How To Handle ”Foreign Sounds” in
Swedish Text-to-Speech Conversion: Approaching the ‘Xenophone’,” in
Problem. Proc. of the International Conference on Spoken Language
Processing, 1998.
[17] S. Y. Jung, S. Hong, and E. Paek, “An english to korean translitera-
tion model of extended markov window,” in Proceedings of the 18th
conference on Computational linguistics-Volume 1.
Association for
Computational Linguistics, 2000, pp. 383–389.
[18] K. Yoon and C. Brew, “A linguistically motivated approach to
grapheme-to-phoneme conversion for Korean,” Computer Speech &
Language, vol. 20, no. 4, pp. 357 – 381, 2006. [Online]. Available:
http://www.sciencedirect.com/science/article/pii/S0885230805000239
[19] Y. Al-Onaizan and K. Knight, “Machine transliteration of names in
arabic text,” in Proceedings of the ACL-02 workshop on Computational
approaches to semitic languages.
Association for Computational
Linguistics, 2002, pp. 1–13.
[20] H. G. Ngo, N. F. Chen, S. Sivadas, B. Ma, and H. Li, “A Minimal-
Resource Transliteration Framework for Vietnamese,” in Annual Con-
ference of the International Speech Communication Association, 2014.
[21] NIST. (2013) Open Keyword Search 2013 (OpenKWS13) Evaluation:
http://www.nist.gov/itl/iad/mig/openkws13.cfm.
[22] P. Ladefoged and K. Johnson, A course in phonetics. Cengage learning,
2014.
[23] J. A. Goldsmith, J. Riggle, and C. Alan, The handbook of phonological
theory.
John Wiley & Sons, 2011, vol. 75.
[24] B. Kessler and R. Treiman, “Syllable structure and the distribution of
phonemes in English syllables,” Journal of Memory and Language,
vol. 37, no. 3, pp. 295–311, 1997.
[25] D. Klein, R. J. Zatorre, B. Milner, and V. Zhao, “A cross-linguistic PET
study of tone perception in Mandarin Chinese and English speakers,”
Neuroimage, vol. 13, no. 4, pp. 646–653, 2001.
[26] Y. J. Lee, The role of lexical tone in spoken word recognition of Chinese.
ProQuest, 2008.
[27] R. J. Anyanwu, “Fundamentals of phonetics, phonology and tonol-
ogy,” Noch nicht ver¨offentlichtes Buchmanuskript. Wird elektronisch zur
Verf¨ugung gestellt, 2008.
[28] I. Maddieson, “Syllable structure,” in The World Atlas of Language
Structures Online, M. S. Dryer and M. Haspelmath, Eds.
Leipzig:
Max Planck Institute for Evolutionary Anthropology, 2013. [Online].
Available: http://wals.info/chapter/12
[29] J. Blevins, “Syllable typology,” in Encyclopedia of Language and
Linguistics: Vol. 12 [Spe-Top].
Elsevier, 2006, pp. 333–337.
[30] A. C. Gimson, An Introduction to the Pronunciation of English.
New
York: St. Martin’s Press, 1970.
[31] D. H. Nguyen, “Vietnamese,” in The World’s Major Languages, B. Com-
rie, Ed.
Oxford: Oxford University Press, 1990, pp. 777–796.
[32] D. I. Slobin, The crosslinguistic study of language acquisition: Theoret-
ical issues.
Psychology Press, 1986.
[33] S. McLeod, The international guide to speech acquisition.
Thomson
Delmar Learning Clifton Park, NY, 2007.
[34] M. Mojalefa and P. Groenewald, Rabadia Ratˇshatˇsha: Studies in African
Language Literature, Linguistics, Translation and Lexicography.
Sun
Press, 2007. [Online]. Available: https://books.google.com.sg/books?id=
oVoyAwAAQBAJ
[35] Yip, Moira, Tone, ser. Cambridge Textbooks in Linguistics. Cambridge
University Press, 2002. [Online]. Available: http://books.google.com.sg/
books?id=KFv2lojXjpwC
[36] T. Q. H. Hoang, “A phonological contrastive study of Vietnamese and
English,” 1965, mA Thesis, Texas Technology College.
[37] S. H. N. Cheung, “A Grammar of Cantonese Spoken in Hong Kong,” A
Grammar of Cantonese Spoken in Hong Kong, Revised Edition, 2007.
[38] I. Maddieson, Tone.
Leipzig: Max Planck Institute for Evolutionary
Anthropology, 2013. [Online]. Available: http://wals.info/chapter/13
[39] J. C. Wells. (2001) Computer-coding the IPA: a proposed extension of
SAMPA: http://www.phon.ucl.ac.uk/home/sampa/x-sampa.htm.
[40] E. Haugen, “The analysis of linguistic borrowing,” Language, pp. 210–
231, 1950.
[41] W.
Frawley,
International
Encyclopedia
of
Linguistics.
Oxford
University Press, 2003, no. v. 4. [Online]. Available: https://books.
google.com.sg/books?id=sl dDVctycgC
[42] O. Y. Kwong, “Homophones and tonal patterns in English-Chinese
transliteration,” in Proceedings of the ACL-IJCNLP 2009 Conference
Short Papers, ser. ACLShort ’09.
Stroudsburg, PA, USA: Association
for Computational Linguistics, 2009, pp. 21–24. [Online]. Available:
http://dl.acm.org/citation.cfm?id=1667583.1667592
[43] H. Masuda and T. Arai, “Processing of consonant clusters by japanese
native speakers: Inﬂuence of english learning backgrounds,” Acoustical
Science and Technology, vol. 31, no. 5, pp. 320–327, 2010.
[44] A. Kashiwagi and M. Snyder, “American and japanese listener assess-
ment of japanese eﬂspeech: Pronunciation features affecting intelligi-
bility,” The Journal of AsiaTEFL, vol. 5, no. 4, pp. 27–47, 2008.
[45] D. Silverman, “Multiple scansions in loanword phonology: evidence
from Cantonese,” Phonology, vol. 9, 1992.
[46] M. Yip, “Cantonese loanword phonology and Optimality Theory,” Jour-
nal of East Asian Linguistics, vol. 2, no. 3, pp. 261–291, 1993.
[47] Y. Rose and K. Demuth, “Vowel epenthesis in loanword adaptation:
Representational and phonetic considerations,” Lingua, vol. 116, no. 7,
pp. 1112–1139, 2006.
[48] C.
Uffmann,
Vowel
Epenthesis
in
Loanword
Adaptation,
ser.
Linguistische
Arbeiten.
De
Gruyter,
2007.
[Online].
Available:
https://books.google.com.sg/books?id=hdYlj7vQWPoC
[49] S. Yun, “Perceptual similarity and epenthesis positioning in loan adap-
tation,” in Chicago Linguistic Society, vol. 48, 2012.


## Page 13


IEEE TRANSACTIONS ON AUDIO, SPEECH, AND LANGUAGE PROCESSING
13
[50] A. Y. Chan and D. C. Li, “English and Cantonese phonology in contrast:
Explaining Cantonese ESL learners’ English pronunciation problems,”
Language Culture and Curriculum, vol. 13, no. 1, pp. 67–85, 2000.
[51] S. Wan and C. M. Verspoor, “Automatic english-chinese name translit-
eration for development of multilingual resources,” in Proceedings of
the 17th international conference on Computational linguistics-Volume
2.
Association for Computational Linguistics, 1998, pp. 1352–1356.
[52] D. Bhalla, N. Joshi, and I. Mathur, “Rule based transliteration scheme
for english to punjabi,” arXiv preprint arXiv:1307.4300, 2013.
[53] B. G. Stalls and K. Knight, “Translating names and technical terms
in arabic text,” in Proceedings of the Workshop on Computational
Approaches to Semitic Languages.
Association for Computational
Linguistics, 1998, pp. 34–41.
[54] A. P. Dempster, N. M. Laird, and D. B. Rubin, “Maximum likelihood
from incomplete data via the EM algorithm,” Journal of the royal
statistical society. Series B (methodological), pp. 1–38, 1977.
[55] H. Li, M. Zhang, and J. Su, “A Joint Source-channel Model
for Machine Transliteration,” in Proceedings of the 42Nd Annual
Meeting on Association for Computational Linguistics, ser. ACL ’04.
Stroudsburg, PA, USA: Association for Computational Linguistics,
2004. [Online]. Available: http://dx.doi.org/10.3115/1218955.1218976
[56] M. Bisani and H. Ney, “Joint-sequence models for grapheme-to-
phoneme conversion,” Speech Communication, vol. 50, no. 5, pp. 434
– 451, 2008. [Online]. Available: http://www.sciencedirect.com/science/
article/pii/S0167639308000046
[57] N. X. Cao, N. M. Pham, and Q. H. Vu, “Comparative analysis
of transliteration techniques based on statistical machine translation
and joint-sequence model,” in Proceedings of the 2010 Symposium
on Information and Communication Technology, ser. SoICT ’10.
New York, NY, USA: ACM, 2010, pp. 59–63. [Online]. Available:
http://doi.acm.org/10.1145/1852611.1852624
[58] B. M. Nguyen, H. G. Ngo, and N. F. Chen, “Regulating orthography-
phonology relationship for english to thai transliteration,” in Proceedings
of the Sixth Named Entity Workshop, 2016, pp. 83–87.
[59] M. Rosca and T. Breuel, “Sequence-to-sequence neural network models
for transliteration,” arXiv preprint arXiv:1610.09565, 2016.
[60] A. Finch, L. Liu, X. Wang, and E. Sumita, “Target-bidirectional neural
models for machine transliteration,” in Proceedings of the Sixth Named
Entity Workshop, 2016.
[61] M.
Bisani.
(2011)
Sequitur
G2P:
A
trainable
Grapheme-
to-Phoneme
converter:
http://www-i6.informatik.rwth-
aachen.de/web/Software/g2p.html.
[62] K.
Lenzo.
(1998,
December
28)
t2p:
Text-to-Phoneme
Converter
Builder.
Retrieved
from
Carnegie
Mellon
University:
http://www.cs.cmu.edu/afs/cs.cmu.edu/user/lenzo/html/areas/t2p.
[63] Y. Song, C. Kit, and H. Zhao, “Reranking with multiple features
for better transliteration,” in Proceedings of the 2010 Named Entities
Workshop, ser. NEWS ’10.
Stroudsburg, PA, USA: Association
for Computational Linguistics, 2010, pp. 62–65. [Online]. Available:
http://dl.acm.org/citation.cfm?id=1870457.1870466
[64] J. Setter, C. Wong, and B. Chan, Hong Kong English, ser. Dialects of
English.
Edinburgh University Press, 2010.
[65] K. A. Lee, “Chinese tone sandhi and prosody,” Ph.D. dissertation,
University of Illinois at Urbana-Champaign, 1997.
[66] T. Takenobu, D. Kaplan, C.-R. Huang, S.-K. Hsieh, N. Calzolari,
M. Monachini, C. Soria, K. Shirai, V. Sornlertlamvanich, T. Charoenporn
et al., “Adapting international standard for Asian language technologies,”
Proceedings of the Sixth International Language Resources and Evalu-
ation (LREC08), Marrakech, Morocco, 2008.
[67] C. S. P. Wong, R. S. Bauer, and W. Lam, “The integration of english
loanwords in hong kong cantonese,” Journal of the Southeast Asian
Linguistics Society, 2009.
[68] The Linguistic Society of Hong Kong. Cantonese Romanization Scheme
- Jyutping: http://www.lshk.org/node/31.
[69] NIST. (2007) Evaluation Tools: http://www.itl.nist.gov/iad/mig//tools/.
[70] H. G. Ngo, N. F. Chen, B. M. Nguyen, B. Ma, and H. Li, “Phonology-
augmented statistical transliteration for low-resource languages,” in Six-
teenth Annual Conference of the International Speech Communication
Association, 2015.
[71] S. Gao, T. Lee, B. Xu, P. Ching, T. Huang et al., “Acoustic modeling
for Chinese speech recognition: A comparative study of Mandarin
and Cantonese,” in Acoustics, Speech, and Signal Processing, 2000.
ICASSP’00. Proceedings. 2000, vol. 3.
IEEE, 2000, pp. 1261–1264.
[72] R. S. Carlisle, “Syllable structure universals and second language
acquisition,” IJES, International Journal of English Studies, vol. 1, no. 1,
pp. 1–19, 2001.
[73] H. L. Guo, “Mandarin loanword phonology and optimality theory:
Evidence from transliterated American state names and typhoon names,”
in The 13th Paciﬁc Asia Conference on Language, Information and
Computation, 1999, pp. 191–202.
[74] Yip, Moira, “Perceptual inﬂuences in Cantonese loanword phonology,”
Journal of the Phonetic Society of Japan, vol. 6, no. 1, pp. 4–21, 2002.
[75] Yip, Moira, “The symbiosis between perception and grammar in loan-
word phonology,” Lingua, vol. 116, no. 7, pp. 950–975, 2006.
[76] L. H. Wee, “Syllabiﬁcation Paradox-Hong Kong Transliteration of
English Words,” 2006.
Gia H. Ngo received his B.Eng from the National
University of Singapore (NUS) in 2015 and currently
pursuing his PhD at Cornell University. Gia has
worked at Human Language Technology department
at the Institute of Infocomm Research, A*STAR
(2013), the Computational Brain Imaging Group at
National University of Singapore (2016 - 2017), and
GIVE.asia (2014 - 2018). Gia’s research interests
lie in machine learning, Bayesian statistics and their
application in natural language processing and com-
putational neuroscience. In particular, Gia’s research
interests in natural language processing include transliteration in limited
resource scenarios and Bayesian graphical model in language modeling. His
research interests in computational neuroscience include parametric mixture
models and non-parametric hierarchical Bayesian models to estimate reference
atlases of brain networks from large datasets of neuroimages.
Minh Nguyen received his B.Eng from the Na-
tional University of Singapore (NUS) in 2016. He
is currently a research assistant at the Institute for
Infocomm Research (I2R), Singapore and Clinical
Imaging Research Center (CIRC), Singapore.
Minh’s research interests include the application
of machine learning to problems in natural lan-
guage processing, computational neuroscience and
robotics. For natural language processing, Minh is
interested in using machine learning, including deep
learning techniques, to model the phonology of
loanwords in different languages. Minh’s research interests in computational
neuroscience include applying time series modeling to predict diseases pro-
gression in human neural system and to denoise neuroimaging data.
Nancy F. Chen (S’03-M’12-SM’15) received her
Ph.D. from MIT and Harvard in 2011. She worked
at MIT Lincoln Laboratory on her Ph.D. research
in multilingual speech processing. She is currently
leading initiatives in deep learning, conversational
AI, human language technology, and Cognitive
Human-Like Empathetic and Explainable Machine
Learning (CHEEM) at I2R, A*STAR and A*AI,
Singapore. She is an adjunct faculty member at
Singapore University of Technology and Design. Dr.
Chen led a cross-continent team for low-resource
spoken language processing, which was one of the top performers in the
NIST Open Keyword Search Evaluations (2013-2016), funded by the IARPA
Babel program. Dr. Chen is an elected member of IEEE Speech and Language
Technical Committee (2016-2018) and was the guest editor for the special
issue of “End-to-End Speech and Language Processing” in the IEEE Journal
of Selected Topics in Signal Processing (2017). Dr. Chen has received multiple
awards, including Best Paper at APSIPA ASC (2016), the Singapore MOE
Outstanding Mentor Award (2012), the Microsoft-sponsored IEEE Spoken
Language Processing Grant (2011), and the NIH Ruth L. Kirschstein National
Research Award (2004-2008).

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
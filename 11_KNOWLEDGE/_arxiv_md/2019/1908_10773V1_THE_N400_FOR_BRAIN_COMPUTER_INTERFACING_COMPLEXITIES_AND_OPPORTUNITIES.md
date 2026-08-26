---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1908.10773v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1908.10773v1_The_N400_for_Brain_Computer_Interfacing__complexities_and_opportunities

> Source: 1908.10773v1_The_N400_for_Brain_Computer_Interfacing__complexities_and_opportunities.pdf

> Pages: 28

---


## Page 1


The N400 for Brain Computer Interfacing:
complexities and opportunities
K V Dijkstra, J D R Farquhar and P W M Desain
Radboud University, Donders Institute for Brain, Cognition and Behaviour
Abstract.
The N400 is an Event Related Potential that is evoked in response to conceptually
meaningful stimuli. It is for instance more negative in response to incongruent than
congruent words in a sentence, and more negative for unrelated than related words
following a prime word. This sensitivity to semantic content of a stimulus in relation
to the mental context of an individual makes it a signal of interest for Brain Computer
Interfaces. Given this potential it is notable that the BCI literature exploiting the N400
is limited. We identify three existing application areas: (1) exploiting the semantic
processing of faces to enhance matrix speller performance, (2) detecting language
processing in patients with Disorders of Consciousness, and (3) using semantic stimuli
to probe what is on a user’s mind. Drawing on studies from these application areas,
we illustrate that the N400 can successfully be exploited for BCI purposes, but that
the signal-to-noise ratio is a limiting factor, with signal strength also varying strongly
across subjects. Furthermore, we put ﬁndings in context of the general N400 literature,
noting open questions and identifying opportunities for further research.
arXiv:1908.10773v1  [q-bio.NC]  28 Aug 2019


## Page 2


The N400 for Brain Computer Interfacing
2
1. Introduction
A Brain Computer Interface measures brain activity to infer something about the
user and take appropriate action based on that inference.
This can be the passive
recognition of the user’s mental state, or the detection of an intention that the user is
actively trying to transmit. In an ideal world, the user’s intention would be extracted
directly from their brain activity: for instance, if they wish to convey a message, the
user simply thinks of the words and the system decodes the brain signature(s) that
accompany them. In practice this is generally not possible, as the representation of such
thoughts is currently unknown and the limited temporal or spatial resolution of current
neuroimaging systems likely precludes them from real-time detection. Advancements
have been made in decoding or reconstructing speech from invasive electrophysiological
recordings (intracranial or intracortical), with the aim to extend these to imagined
speech (see Martin et al. [1] for a recent overview), but this ﬁeld is still young and the
invasive nature limits wide applicability.
In absence of the ability to measure a desired action directly from someone’s brain
activity, it can be useful to look at brain signatures or signals that we know can be
measured reliably from brain activity, and center the design of a Brain Computer
Interface around those.
For instance, using electroencephalography (EEG), Event
Related Potentials (ERPs) can be measured that reﬂect the brain activity in response
to stimuli. The P300 is an ERP that is elicited for stimuli that are relevant to the task
a user is performing in a stream of non-target stimuli [2]. By designing a stimulus set
such that the subject has the option to determine which stimuli are task-relevant (by
directing their attention to the stimuli associated with the selection of interest), a P300
BCI can enable a user to make multiple-choice selections. A well known example is
the P300 speller. When ﬂashing the columns and rows of the letter matrix, the user’s
attention to a single letter elicits P300s only for ﬂashes on that letter’s row/column
coordinates. This subsequently enables the system to infer (the position of) the attended
letter based on the extracted ERP responses. Other examples of such an approach are
using neurofeedback of the mismatch negativity for sound discrimination learning [3], or
using the power changes in the posterior alpha associated with (covert) spatial attention
for indicating a direction [4, 5].
The N400 is another well established ERP in neuroscience literature. It was ﬁrst
discovered when in sentential contexts, incongruent sentence endings exhibited a more
negative ERP than congruent sentence endings, peaking at around 400 ms [6]. In the
decades since, it has been investigated extensively (see Kutas & Federmeier [7] for an
overview). The N400 is not limited to sentence contexts, and can also be elicited through
semantic priming: presenting a prime word followed by a related or unrelated stimulus,
with the unrelated stimuli eliciting a more negative N400 [8]. This extends to cases
where the prime is not presented, but merely actively recollected [9]. Broadly speaking,
it is sensitive to the relation of the presented stimulus to the mental context of the user.
This is interesting from a BCI perspective, because it suggests that the N400 could


## Page 3


The N400 for Brain Computer Interfacing
3
be used to infer information about the user’s mental context, without the user having
to make this explicit. That is, given that BCIs are (currently) unable to read what
someone is thinking directly from their brain activity, the N400 could potentially be used
to infer information about the user’s active mental context by presenting stimuli with
speciﬁc content, and observing the size of the elicited N400 to these stimuli. However, in
addition to these contextual eﬀects, numerous (inherent) stimulus characteristics have
been shown to also aﬀect the N400: for instance, simply the frequency that a word
occurs in a language can aﬀect the N400 amplitude. These may need to be controlled
or accounted for when using the N400 for a BCI application.
Given the prominence of the N400 in the neuroscience literature, attention for the
N400 in the BCI ﬁeld has been comparatively limited. This may reﬂect a disinterest in
the kind of BCI paradigms that could be designed around a N400 eﬀect, or, a (perceived)
diﬃculty to make such paradigms work. To obtain more insight, we searched for the
keywords "Brain Computer Interface" and "N400" and identiﬁed three research lines
that do make use of an N400 eﬀect: (1) the use of the N400 in response to familiar face
stimuli for boosting performance of the matrix speller [10–12], (2) to detect the absence
or presence of language processing in patients with impaired levels of consciousness
(Disorders of Consciousness) [13–15], and (3) to probe for information about the active
mental state of the user, e.g., a category or word on the user’s mind, by presenting
stimuli that elicit responses of relatedness with regard to this mental context [16–18].
In the following sections we discuss these research lines to provide an overview of the
current ways the N400 is exploited for BCI purposes, to determine limitations, and to
identify opportunities for improving existing paradigms or developing new paradigms.
To provide context, we start with a more detailed description of the N400 and the
conditions in which it is elicited.
The Neuroscience literature on this N400 eﬀect
is extensive, and a good overview article already exists [7], so the focus here is not
to be comprehensive, but to summarise the most important aspects and to take the
opportunity to discuss its properties with a BCI context in mind.
With this N400
overview and an analysis of the limitations and potential opportunities in existing N400
BCI research, we hope to provide a starting point for researchers with an interest in using
the N400 for a BCI paradigm, in deciding whether or not their intended application may
be feasible.
2. Overview of the N400
The N400 is characterised as a negative going wave that reaches its maximum (negative)
amplitude around 400ms after stimulus presentation over centro-parietal electrodes
[7]. It is most known for its sensitivity to semantic context, being more negative to
incongruent than congruent words in a sentence [6], or more negative for unrelated than
related words following a prime word [8]. Figure 1 depicts the N400 in response to
related and unrelated stimulus words in relation to a remembered target word, showing
the characteristic negativity, latency and topography [18]. One experiment comparing


## Page 4


The N400 for Brain Computer Interfacing
4
-2
0
2
4
-2
0
2
4
0
0.4
0.8
time (s)
-2
0
2
4
amplitude (μV)
Fz
Cz
Pz
amplitude (μV)
-2
0
2
300-700ms
related
unrelated
(a)
(b)
Figure 1. Brain responses to related and unrelated stimuli-words in relation to a
memorised target-word (data from [18]). (A) Grand average ERPs for channels Fz, Cz
and Pz, for 20 subjects. Shaded areas represent a bootstrapped 95% conﬁdence interval
of the mean (B) grand average topography for the 300-700 ms period, (unrelated -
related)
the word pair priming and sentence congruency eﬀects found a N400 diﬀerence of 3.4
µV (Cz) and 5.2 µV (Pz) for sentences, and a diﬀerence of 1.8 µV (Cz) and 1.9 µV
(Pz), for word pair stimuli, suggesting that the sentence congruency eﬀect is stronger
than the word-priming eﬀect.
Repetition of a stimulus within an experimental session can also aﬀect the N400 to
that stimulus, with subsequent presentations having a reduced N400 amplitude [19, 20].
This reduction is larger the sooner the repetition occurs, but persists even when e.g., 19
intervening words are presented before the item is repeated, in a list [19], or when up
to several hundred words are read before encountering the repetition in a text [21]. A
15 min break, on the other hand, can be suﬃcient to make the repetition eﬀect nearly
undetectable [20].
In addition to these contextual manipulations, the N400 amplitude has been shown
to be sensitive to certain inherent stimulus properties, that can be measured even in
isolated stimulus presentations. Instances of properties that aﬀect the N400 amplitude


## Page 5


The N400 for Brain Computer Interfacing
5
for word stimuli are: the (written) frequency with which a word occurs in a language
(larger N400 for low frequency words) [20, 22], the concreteness of a word (larger N400
for concrete than abstract words) [23, 24], and the orthographic neighbourhood size (i.e.,
how many words are similar in spelling; a larger N400 for words with a larger/denser
neighbourhood) [25, 26]. The latter is only one of several neighbourhood eﬀects, where
a neighbourhood can be deﬁned both orthographically and associatively (which words
are related to this word). In both deﬁnitions a larger neighbourhood size, and even a
higher word frequency of the neighbours can increase the N400 amplitude [25].
Experiments where both contextual and lexical eﬀects have been manipulated,
show that these eﬀects can interact: for instance, both stimulus repetition and higher
word frequency lead to a smaller N400 amplitude in isolation, however, when both
low and high frequency words were presented twice, the eﬀect of the repetition on
the high frequency word’s ERP was small to none, while the repetition of the low
frequency words reduced the size of the N400 [20].
Kounios et al.
ﬁnd a similar
interaction between concreteness and repetition [24]. A study by Dambacher et al. shows
another interaction, that of sentence context (measured as word predictability), and
word frequency, with the eﬀect of word frequency decreasing as predictability increases
[27].
Another BCI relevant interaction eﬀect is that of age, where for certain experimental
manipulations the N400 amplitude decreases with age (reminiscent of the changes in
the P300 with age [28]), but does not decrease for others. For instance, while sentential
context eﬀects have been shown to elicit smaller N400 diﬀerences in older subjects
[29, 30], Payne et al. [30] found that this did not extend to the lexical eﬀects they
tested (i.e., word frequency and orthographical neighbourhood). Federmeier et al. [29]
found a reduction of the N400 for sentence ﬁnal-word (in)congruency, for their older
subjects, but no reduced N400 diﬀerence for lexical association (i.e., priming) eﬀects,
within those sentences.
Returning to the semantic context eﬀects, research indicates that it is not only
the ‘local’ (e.g., sentence level) semantic context in which a stimulus occurs that is
relevant for the N400 amplitude.
Discourse (i.e., context on a larger scale), built
up over a few preceding sentences, can increase the N400 amplitude when violating
expectations from previous context [31], or decrease the N400 amplitude when prior
context causes a normally incongruent sentence ending to be interpretable as congruent
[32]. Furthermore, beyond active mental context, even passive world-knowledge can
elicit a larger negativity when it is incongruent with a presented stimulus: world-
knowledge violations, e.g., a sentence asserting that that dutch trains are white, elicited
a negativity similar to the N400 from semantic violations, e.g., a sentences asserting
dutch trains are sour [33, 34]. This example, however, does not distinguish between
the kind of world knowledge that stems from a learned association between concepts
(e.g., ‘train’ and ‘yellow’), and world knowledge that allows truth-values to be assigned
to statements (propositional knowledge). In the latter case the relation with the N400
may not always be straightforward (see e.g., the eﬀect of negation on the N400 [35, 36]).


## Page 6


The N400 for Brain Computer Interfacing
6
Table 1.
Summary of the main variables aﬀecting the N400 amplitude, with a short
description. The direction of the eﬀect is noted, with ’>’ indicating which will obtain
a larger N400 amplitude (i.e., have a more negative ERP in the N400 timerange).
Level
Variable
Description
Direction
lexical
eﬀects
word frequency
How often a word occurs in (written)
language.
House is a frequent word,
parsimonious is not.
low freq. > high freq.
word neighbourhood
Orthographic neighbourhood:
words
that are similar in spelling to the word
in question (visual presentation) Mine
has neighbours such as mane, line.
Phonological
neighbourhood:
words
that are similar in sound (auditory
presentation)
The neighbourhood size (or density)
refers to the number of words that are
within close distance of a given word.
large > small neighbourhood
dense > sparse neighb.
word concreteness
Concreteness (as opposed to abstract-
ness) describes the degree with which
a word can be experienced with the
senses[37]). House is a concrete word,
justice is abstract.
concrete > abstract
contextual
eﬀects
stimulus repetition
Whether it concerns the ﬁrst presenta-
tion of a stimulus or a second or nth
presentation. The interval (time before
repetition) is also relevant.
ﬁrst presentation > repetition
long interval > short interval
lexical relatedness or
association
Semantic priming occurs when a word
was preceded by a semantically similar
word (cup - bowl) or associated word
(tea - cup) compared to an unrelated
or unassociated word.
unrelated > related
unassociated > associated
sentence context
How well does a word ﬁt in the existing
sentence semantic context. Does it ﬁt
with the sentence so far (:=congruent)
or is it anomalous (:=incongruent).
How
often
would
people
end
the
sentence word the word in question (:=
cloze probability).
incongruent > congruent
low cloze-prob. > high prob.
discourse context or
world-knowledge
How well does a word ﬁt in the context
of a larger preceding text, or with
existing world-knowledge
incongruent > congruent
non
linguistic
con-
text
Other types of meaningful stimuli in
the form of e.g.,
drawings,
photos,
videos, sounds and smells representing
concepts such as objects, actions, faces
and even mathematics [7] can elicit
N400 eﬀects
incongruent > congruent
un-primed > primed


## Page 7


The N400 for Brain Computer Interfacing
7
An overview of the mentioned eﬀects can be found in table 1. Here the diﬀerent
variables that have an eﬀect on the N400 are listed, with a short description and the
direction of the eﬀect.
It is important to note that whilst most N400 studies have focused on visually
presented word stimuli, the diﬀerential eﬀect with respect to the active mental context
has also been demonstrated with other presentation modalities. Spoken words elicit
N400 eﬀects analogous to the visual presented stimuli [38, 39] (with phonological
neighbourhood as the auditory analogue of orthographic neighbourhood). Furthermore,
they are not limited to words: pictures of faces, for instance, have been found to
elicit N400 (priming) eﬀects [40–42].
More broadly, actions or objects, represented
with pictures (drawings or photo’s), videos, sounds and even smells have successfully
been used to elicit N400 eﬀects (see Kutas et al. (2011) [7]). This does not mean that
the N400 eﬀects are identical across modalities. For instance, in a priming experiment
Holcomb & Neville found a larger N400 amplitude and an earlier N400 onset for auditory
stimuli than for the same stimuli presented visually [38].
From a BCI standpoint it is also relevant to know whether subjects need an explicit
task to elicit the signal. For the N400 it is generally suﬃcient for subjects to attend the
stimuli to elicit the eﬀects, as processing stimuli for meaning happens automatically.
This is, unless the task explicitly does not require people to process the stimuli as a
stimulus containing meaning at all (e.g., just the size of the stimulus on the screen), in
such a case the N400 may be absent [43, 44]. Additional experimental manipulations
have shown that the processing of the stimuli does not need to reach conscious awareness
for a detectable N400, with both attentional blink and masked priming studies ﬁnding
eﬀects of priming on the N400 (see Kutas & Federmeier [7] and Deacon & Shelley-
Tremblay [45] for overviews). However, the degree of attention does play a role in the
strength of the elicited N400 eﬀect. Cruse et al. [46], for instance, link the degree of
active semantic task involvement of the subjects to the number of subjects for which a
N400 can be detected, ﬁnding progressively smaller N400s for a covert (mental decision
only) and passive task (no task), compared to an overt task (requiring a behavioural
response).
The functional explanation of the N400 is still a matter of debate. To summarise
the main views, the N400 has been suggested to reﬂect brain activity from the activation
of (the representation of) the stimulus in long term memory, to reﬂect activity of the
integration of the stimulus in the active mental context, or, to reﬂect a combination of
such processes [7, 34, 47–49]. In the ﬁrst view the amplitude of the N400 is reduced when
the stimulus’ representation was (partially) pre-activated by prior stimuli, facilitating
semantic access. In the integration account the N400 amplitude reﬂects the diﬃculty
with which the stimulus can be incorporated into the previously accrued context. There
have also been attempts at building a computational model of the N400: a recent paper
models the N400 as reﬂecting the degree of change in probabilities in an update of the
mental model in response to the presentation of a given stimulus. This computational
model subsequently exhibits a considerable number of the N400 eﬀects outlined above


## Page 8


The N400 for Brain Computer Interfacing
8
[50].
In addition to the N400, language manipulations sometimes elicit a later positive
ERP: the late positive component or complex (LPC), or P600 [51–54]. It can co-occur
with the N400 [51], or be elicited independently, e.g., in response to syntactic violations
[52]. In sentence congruence paradigms, it does not occur as consistently as the N400,
with various studies not ﬁnding a positivity in this late range (600-900 ms) [51]. Some
studies attempt to interpret this late response as a late P300 (P3b) [55].
In fact,
it is unclear whether these late eﬀects represent a single brain response, or multiple
functionally dissociable responses [53]. Furthermore, in a study by Kos et al. [54] only
about half the participants (n = 72) exhibited a LPC, while others showed an extended
negativity of the N400. This may cause the eﬀect to be averaged out in grand average
ERPs, while there may yet be a signal present for individual subjects.
In summary, the N400 is a complex response that has been shown sensitive to many
parameters of the user or user’s mental context, ranging from general-world-knowledge
and subject age, to stimulus properties (such as word frequency, orthographic or
phonological neighbourhood size and concreteness), from long range document-context
eﬀects, to short range sentence congruency eﬀects and direct prime-probe relations or
repetition eﬀects. These multiple levels of interaction make the N400 response both
potentially attractive for many possible BCI applications, and particularly challenging
for these possible applications to control for all the other possible interactions. A similar
complexity (though much less extreme) is seen in p300 spellers where choices with regard
to the matrix size aﬀect the size of the elicited P300 [56], which may be attributable
to the fact that the P300 is not only sensitive to the task relevance of a stimulus (i.e.,
is it a ’target’ for the current selection), but also the inherent stimulus frequency or
probability, with lower probability stimuli eliciting larger P300s.
3. Current approaches using N400 for BCI purposes
We have identiﬁed three categories of existing research that use the N400 for BCI
purposes: (1) approaches that exploit the N400 to enhance existing BCI applications,
(2) approaches that aim to detect language processing in patients with Disorders of
Consciousness (DoC), (3) and approaches that use stimuli to probe the users mental
context. We discuss these here, identifying limitations, open questions and opportunities
for further research.
3.1. Enhancing existing BCI applications
We mentioned brieﬂy in the previous section that the N400 can also be elicited in
response to (pictures of) faces. This is both in the priming sense [40], eﬀects of repetition
[42], and by presenting faces outside of context, where, similar to the lexical eﬀects in
language, diﬀerences have been identiﬁed in response to familiar and unknown faces [41].
Speciﬁcally, familiar faces elicit a larger N400 than the unknown faces, which appears


## Page 9


The N400 for Brain Computer Interfacing
9
at odds with the frequency eﬀects in words, where pseudo-words elicit larger N400s
than real words. A suggested reason for this is that the unknown faces do not initiate
semantic processing and show no N400 negativity at all [57]. This used to be similarly
suggested for illegal character strings, which (without context) generally do elicit more
positive ERPs than legal words, but Laszlo and Federmeier have showed that illegal
nonwords can in fact elicit N400 eﬀects, and attribute the reduced N400 to factors such
as lower (orthographic) neighbourhood competition [25, 58].
In addition to the N400 elicited by these familiar faces, the presentation of faces
in comparison to other non-face stimuli (e.g., objects) elicits a negativity at 170ms (the
N170) [41].
In their famous-faces speller, Kaufmann et al.
[10, 11] demonstrate how these
responses to (familiar) faces can be exploited by replacing the ﬂashing of a letter in the
matrix speller, by the superposition of a face over the letter (for each letter in a given
row or column). This is shown to improve speller performance, with accuracy for 5
sequences of highlights at ˜95% for the classic speller and ˜100% for the famous faces in
Kaufmann et al. (2011) [10]. In Kaufmann et al. (2013) [11], both patients and healthy
subjects were tested. There, again for 5 sequences, healthy subjects achieved ˜90% and
˜99% for the classic and faces speller respectively. The improvement for the patients
was even more pronounced, improving from ˜77% to ˜100%, from the classic to the faces
condition. In this followup-study they tested two additional face conditions: personal
familiar faces and unfamiliar faces. The N400(f) eﬀect for all three conditions were
indistinguishable, while all signiﬁcantly more negative than in the classic speller. The
authors speculate that the presence of an N400 for the unfamiliar faces may have been
due to an induced familiarity from the repeated presentations, however if unfamiliar
faces are indeed analogous to (illegal) nonwords, it is not surprising that they elicit
N400 activity [58].
In these studies a single face is used for all highlights across a session. Given the
attenuating eﬀect of repetition on the N400 amplitude (also applicable to faces [41, 42]),
this may not be ideal. While the increased performance of the face speller compared to
the classic version shows that even a potentially attenuated eﬀect is suﬃcient to increase
the signal(s)-to-noise ratio of the speller, a collection of faces rather than a single face
may improve performance further. Jin et al. [12] investigate this possibility, comparing a
single face versus a multi-face paradigm. They ﬁnd an increase in classiﬁcation accuracy
for the multi-face paradigm, (also speciﬁcally in the N400 window: 450-600ms).
It
is relevant to note that in their ERP grand averages, the single face condition had a
consistently more negative amplitude than the multi-face condition in this time-window,
which we would not expect if the N400 had attenuated due to a larger repetition eﬀect in
the single-face condition. Furthermore, their multi-face condition consisted of 5 faces;
given that N400 repetition eﬀects (for word stimuli) were still distinguishable at an
interval of 20 intervening words before the repetition in previous literature [19], a set of
5 may not be suﬃcient to measure the eﬀect of this on the N400 (20-100 may be more
appropriate).


## Page 10


The N400 for Brain Computer Interfacing
10
Overall, the faces speller paradigm oﬀers a nice illustration of how the signal-to-
noise ratio of an existing application can be boosted by adding an additional signal, and
how automatic processing of meaning, as indexed by the N400, can be exploited for this
purpose.
3.2. Language processing detection for Disorders of Consciousness
Another ﬁeld where the N400 has been used is the detection of language processing in
patients with Disorders of Consciousness (DoC). Such disorders range from coma, to
unresponsive wakefulness syndrome (UWS; formerly referred to as vegetative state), in
which patients appear awake but are completely unresponsive, to minimally conscious
state (MCS), in which there is some evidence of behavioural responses to commands,
but no communication is achieved [59, 60].
In these cases the lack of behavioural
communication is attributed to impaired consciousness, as opposed to a disability arising
from paralysis (e.g. complete locked-in state, CLIS). However, patients in the latter
category may also have impaired levels of consciousness [61, 62], so in practice the
dichotomy may not be clear cut.
Detection of language processing in patients with DoC can give insight into what
level of cognitive processing is intact in a given individual. This is not a BCI application
in the traditional sense of oﬀering control to the user, but a BCI as a (oﬄine) diagnostics
or prognostics tool. Possibilities for providing communication BCIs for these patients
have also been explored, with a number of studies showing that for certain patients,
command following (i.e., performing a mental task when prompted) can be detected
(e.g., in fMRI [63, 64] or EEG [65, 66]).
Generally, studies that use EEG to determine cognitive processing in DoC patients,
use a range of ERP tasks. These are most commonly oddball tasks, to elicit signals such
as the MMN or the P300, and semantic tasks to elicit a N400 and/or a late positive
component. Stimuli are presented auditorily, as hearing is assumed to be intact. In
Kotchoubey et al. [13], for instance, a large group of patients (n = 78) with DoC are
investigated, with three oddball and three semantic tasks. The percentage of patients
for whom a signiﬁcant ERP could be detected ranged from 8% to 95%, depending on the
group (UWS or MSC) and the brain signal under consideration (N1/P2, MMN, P300,
P600 or N400). In particular, ˜14% (UWS) to ˜23% (MCS) of patients a N400 could be
detected for a given semantic task. These were similar to the percentages for a group
of severely brain damaged but conscious control group.
Such studies generally check whether the patients improve, and/or regain some
degree of communication at a later date, to assess whether detection of these ERPs is
predictive of patient outcome. In Kotchoubey et al. (2005) [13], patients that exhibited
a MMN improved signiﬁcantly more often than those that did not. For the N400, this
eﬀect was not signiﬁcant (p=0.079), but in a more recent study by Steppacher et al.
[14], a signiﬁcant correlation was found for the N400 and recovery. In that study, the
P300, did not have a signiﬁcant relationship with recovery, even though overall it was


## Page 11


The N400 for Brain Computer Interfacing
11
detected more frequently in patients,
Whether someone exhibits a given ERP can be decided in multiple ways:
by
performing one of various statistical tests to single trial data, or employing human
raters to judge average ERPs. In all approaches there is some balance between the
possibility of a false positive or false negative: judging someone to exhibit an ERP
when in fact they do not, or vice versa [67]. This is still separate from the issue of
whether or not someone who does not (appear to) exhibit an identiﬁable N400, is in
fact processing the stimuli. The latter cannot be excluded as a possibility, as even in
the healthy population, the N400 can not always be detected in single subjects, even
with behavioural conﬁrmation that they are processing the stimulus’s content.
The degree to which this is a relevant factor depends on the rate in which the
N400 can be detected in healthy subjects. While the N400 literature is large, this is
not a question that is usually addressed in general neuroscience. In table 2 we have
compiled a number of studies who do report individual detection rates, for both the
general population and data from DoC studies. Studies who had a control group of
healthy students are listed twice in the table, in split by their respective categories.
Two studies employed a control group of patients with brain damage, but without a
disorder of consciousness, as a closer control. These have been included with the label
CTRL. We specify a number of variables that may aﬀect the identiﬁcation rate: the
task and stimuli used, the number of stimuli collected per class, and the test used to
determine signiﬁcance. Both the sample of studies and the sample sizes within studies
are small, limiting our ability to draw conclusions.
In some sense the detection of a signiﬁcant N400 eﬀect in a single subject is an
easier problem than making single trial predictions for BCI control.
Table 2 shows
that even this detection is/can be non trivial for the N400, even for healthy subjects.
Furthermore, the data from the DoC studies suggest that in this application often
relatively few stimuli per class are used to make these decisions. This may be due to
time-constraints, as the N400 is often a single task in a task battery (i.e., combined
with other tasks such as oddball paradigms), but likely hampers detectability.
For
instance, if we limit the number of trials per class to 50, in the Dijkstra et al. study
[18] (listed in the table), then only about 6/19 individuals would have been identiﬁed
as exhibiting an N400, rather than the 15/19 from using 400 brain responses per class.
We determined this by running a cluster-based permutation test on the data from each
individual subject, drawing a sample of trials per class (with replacement; 50 samples)
from the full data of the respective individual, for a number of subset sizes ([30, 50, 75,
100, 150, 200, 300, 400]). The results of this analysis can be found in ﬁgure 2.
At 100 stimuli per class only about 50% of participants are identiﬁed to exhibit an
N400, compared to when 400 stimuli per class are considered. The task employed in
this study may not be ideal for detecting a N400: an implicit priming task was used in
which the subject was given a target word to remember, followed by 1-10 probe words
that they needed to assess the relatedness status to the target to. Yet, this analysis
clearly illustrates that if the goal is to determine whether a given subject exhibits an


## Page 12


The N400 for Brain Computer Interfacing
12
30 50 75 100
150
200
300
400
#stimuli per class
0%
20%
40%
60%
80%
100%
subjects with identifiable N400
1
4
7
10 13 16 19
subject
0%
50%
100%
1
4
7
10 13 16 19
0%
50%
100%
% identified across bootstrap samples
(a)
(c)
(b)
Figure 2. (a) percentage of individuals (n=19) for whom a signiﬁcant N400 can be
detected for an increasing number of stimuli per class (data from Dijkstra et al. [18]).
The plot represents the mean and standard deviations across 50 bootstrapped samples
of each participant’s data. (b) and (c), per participant, the percentage of bootstrap
samples in which an N400 eﬀect could be identiﬁed using (b) 400 or (c) 100 (c) stimuli
per class, sorted based on the 100-per-class detection percentage.
N400, using 50-100 stimuli may produce a considerable amount of false negatives.
The fact that increasing the number of stimuli per class has such a eﬀect on
detection rates suggests that this is a signal-to-noise problem.
Sculthorpe-Petley et
al.
[68], approach this problem, by accruing information across participants, rather
than increasing the number of presented stimuli. They train a Supoort Vector Machine
on the averaged ERPs of each single subject, one for related and one for unrelated
stimuli, and obtain a 92% accuracy in a leave-one-subject-out training approach. We
note however, that this appears to be the accuracy for predictions of both the related
and unrelated ERPs for each subject, while the decision of whether a subject exhibits
an N400 when only one of the two was classiﬁed correctly is non-straightforward. An
open question is furthermore, whether this approach can be extended to the detection
of the N400 in DoC patients, as they do not always exhibit a typical ERP [13].
If more time were available for these diagnostic tasks, there may be additional
opportunities for assessing language processing. For instance, a subject that is listening
to a story, may exhibit N400 eﬀects based on the lexical properties of each given item,
but not be tracking sentence level or discourse level content. Currently the paradigms
outlined in table
2, only asses the mid level semantic content (primed words or
[in]congruent sentences). The low level stimulus properties may help determine whether
for a given individual an N400 can be detected, and if so, if this person also exhibit
higher level language processing. This does assume that such lexical eﬀects are easier
(or as easy) to identify, which ought to be determined empirically in healthy subjects
ﬁrst. Similarly, manipulating discourse level semantics may allow to determine whether
a patient accrues semantic context on longer timescales, though such manipulations may
require longer sessions in order to collect suﬃcient data.


## Page 13


The N400 for Brain Computer Interfacing
13
Table 2.
Studies reporting detection rates of the N400 in individuals, from the
general population or in patients with Disorders of Consciousness.
paper
n
task
instruction
#stim
/class
detection
rate (%)
statistic
general population
Bostanov et al [69]
36
WP
passive
200
67
94
t-CWT randomiziation testc
t-CWT Hotellingc
Daltrozzo et al [15]
20
WP
SC
passive
60
50
45
60
t-CWT Hotellingc
Cruse et al [46]
12
12
12
WPa
overt
covert
passive
100
75
58
0
cluster permutation testd
12
WPb
passive
100
50
12
SC
passive
100
17
Sculthorpe-Petley
et al [68]
100
SC
passive
30
26
92
cluster permutation testd
cross-subject SVMe
Rohaut et al [70]
19
WP
passive
68
42
t-test criterionf
Geuze et al [17]
12
WP
covert
200
100
binomial conﬁdence intervalg
Dijkstra et al [18]
19
WP
covert
∼500
63
79
binomial conﬁdence intervalg
cluster permutation testd
Disorders of Consciousness
Schoenle et al [71]
43 uws
23 nevs
54 ctrl
SC
passive
100
39
77
90
human raters (experts)h
Kotchoubey
et
al
[13]
38 uws
WP
SC
passive
50
14
23
38 mcs
WP
SC
20
18
10 ctrl
WP
SC
22
14
one-tailed ANOVAi
Daltrozzo et al [15]
42 coma
WP
SC
passive
60
50
17
7
t-CWT Hotellingc
Steppacher
et
al
[14]
53 uws
SC
covert
100
32
15
39 mcs
SC
covert
100
44
23
t-CWTc
human raters (experts)h
t-CWTc
human raters (experts)h
Rohaut et al [70]
15 uws
14 mcs
WP
passive
68
7
36
t-test criterionf
WP: word priming task | SC: sentence congruence task | UWS: unresponsive wakefulness state | MCS: minimally conscious state
| NEVS: near vegetative state (approx. between uws and mcs) | CTRL: control group of brain injured, but conscious patients
a relatedness based on shared semantic features [72]
b relatedness based on association norms [73]
c Student’s t-statistics applied to a Continuous Wavelet
Transform [69]
d non-parametric cluster-based permutation test [74]
e Support Vector Machine trained on the average ERPs of
n-1 subjects and tested on the nth subject
f unpaired t-test criterion:
p ≤0.05 on a minimum of 5
samples and 10 electrodes
g
a
binomial
conﬁdence
interval
used
to
distinguish
prediction accuracies from chance
h averaged ERPs evaluated by neurophysiologists.
i one-tailed ANOVA of factor condition (related vs unrelated)
on (windowed) ERP amplitude


## Page 14


The N400 for Brain Computer Interfacing
14
3.3. Inferring information about the user’s active mental context
The fact that the active mental context of a subject modulates the N400 to a given
stimulus can be exploited for BCI purposes by presenting stimuli of which the semantic
content is known and, through presentation of stimuli with varying semantic content
and decoding the (absence) of relationships, inferring this mental context.
One line of research in this direction is that of relevance detection: ﬁguring out
what a user is searching for based on their brain response to speciﬁc words or images.
For instance, Wenzel et al. 2014 [16] attempt to decode a category of interest based on
brain responses to stimuli words out of various categories. To make the setting more
natural, multiple words were presented simultaneously, distributed spatially across the
screen.
The time-lock of the brain response to the stimulus was achieved with an
eyetracker, based on the moments of eye ﬁxation. In the (online) test phase of the
experiment, subjects picked a single category out of 5 as a target and attended stimuli
of all 5 categories. Attended stimuli disappeared (based on gaze detection), and were
replaced with new stimuli. Incoming data was then analysed to update ranking of the
expected target category, online. After a 100 stimuli a trial ended and new categories
were selected.
Given the semantic nature of this task, this should elicit a N400 response, and
the reported results indeed show a N400-like negativity in Cz for stimuli that were not
members of the target category. It is important to note that the relevant-irrelevant
diﬀerence was markedly reduced in the online phase. The authors suggest this may be
due to a change in task (during training subjects were asked to count, during testing only
to search for relevant terms). However, since the experiment used a total of 17 categories
with 20 stimuli each, subjects would have seen most stimuli at least once during training,
and while during a given trial in the testing phase subjects saw each stimuli only once,
categories would return in other trials, leading to repetitions of stimuli. It is therefore
possible this attenuation can be attributed to a N400 repetition eﬀect. In addition to
the N400, they found a positive component in left posterior electrodes (e.g., P9), from
200-600 ms. This positive component was more pronounced in the online phase, and
persisted past 800 ms. Furthermore, in this online phase, this positive component was
more widespread, showing a left lateralised eﬀect, that showed up as a late positive
component (following the attenuated N400), in electrode Cz. Performance for this BCI
was measured based on the ranking of the correct category out of all ﬁve categories,
with a mean rank of 1.68 (chance level is 3) across all subjects (range 1.12-2.47).
In Golenia et al. [75] a similar paradigm is used to detect which concept is relevant
to a users search, but here the aim is to disambiguate between multiple meanings of
a term using images. Fixation-related potentials were collected in response to pictures
each depicting one of two interpretations of a search term (e.g., bass the ﬁsh, or bass
the instrument). While this task can be interpreted as presenting related and unrelated
stimuli in context of a target (the intended meaning), this task did not appear to elicit a
N400 eﬀect. Instead, there was a late eﬀect (>500ms), more negative for images with the


## Page 15


The N400 for Brain Computer Interfacing
15
intended meaning (i.e., related), compared to the images with the alternative meaning,
that could successfully be exploited for classiﬁcation. Picture stimuli have been shown
to elicit N400 eﬀects in priming studies [76], so an N400 could have reasonably been
expected and we have no clear hypothesis for why this paradigm would not elicit one.
In our own research group we have pursued a similar application, presenting stimuli
to deduce information about the active mental context, but aimed for word selection,
rather than category selection or word/concept disambiguation. Our studies thus far
have been oﬄine experiments, that aim to determine the suitability of the N400 for
the intended task. Speciﬁcally, a ﬁrst study determined whether or the N400 could
be decoded in single trials by determining whether a given stimulus (i.e., the probe)
was related to the active mental context (the immediately preceding prime) [17]. These
stimuli were presented in word-pairs where half of the primes were related and half
unrelated.
Across 12 subjects, classiﬁcation accuracies ranged from 54% to 67%,
(average ˜60).
In a follow-up study we aimed to determine whether or not the N400 can reliably
be detected when the prime word is not presented, but actively recalled by the subject,
while multiple consecutive probe words are presented. An earlier study by Van Vliet et
al. had already established that it is not necessary to actually present a prime word, it is
suﬃcient for the subject to actively recall it [9]. In this consecutive probing experiment
a trial started by supplying the subject with a target word to remember, after which
one to ten probe words were presented, with probe words either strongly related or
unrelated to the target. No attenuation between the ﬁrst and 9th or 10th probe was
detected, suggesting that multiple consecutive probes can be used to elicit information
about a target concept on the users mind. At the same time, classiﬁcation rates were
again low: accuracies for single probes ranged from 50% (indistinguishable from chance
level) to 72% (mean 58%), and for approximately 1/3 of subject the accuracy was
not distinguishable from the (bonferroni-corrected 95%) conﬁdence interval of chance
performance. While it is not an unknown problem for a subset of users unable to use a
BCI [77], this can be a concern for BCI development.
Low single trial classiﬁcation rates can be overcome by accumulating data over
multiple brain responses. Given the sensitivity of the N400 to repetition of stimuli, this
does not have to be limited to aggregation of information over a single repeated probe,
but can consist of accumulating information across diﬀerent probes. The Wenzel et
al. relevance detection study is an clear example where category detection is possible,
when the set of categories is small, and inference is performed on the aggregating
over a large number of stimuli presentations (˜100 stimuli).
Their ﬁxation-related-
potentials approach allows users to decide their own pace, and the short ﬁxation times
(˜200 to ˜300ms), show that requiring many stimuli is not necessarily a problem, when
single responses can be obtained quickly. However, it remains a question how well this
approach can be expanded to allow selections from a larger number of categories or
concepts. In the Dijkstra et al. study, no online phase was included, but simulations
were used to estimate how well the correct target could be inferred from the others (˜120


## Page 16


The N400 for Brain Computer Interfacing
16
possible targets). The results from these simulations indicated that only for about 5
subjects, 100 stimuli would be suﬃcient to have the correct target in the top 3 guesses
(on average; see Dijkstra et al. for more details [18]). Such simulations make various
(implicit) assumptions and have limited interpretability compared to results from an
online test, but this illustrates that extending this approach to larger concept dictionaries
(e.g., 1000), would likely require an impractical number of consecutive probes, with this
approach.
The limiting factor here is likely the signal-to-noise ratio of the N400 that, for the
average subject, appears to be lower than that of e.g., the P300, given the diﬃculty of
even ﬁnding a signiﬁcant eﬀect in a given individual (see ﬁgure 2). A possible solution
may be to increase the signal-to-noise by evoking an additional signal, e.g., by coupling
the probing approach with a task to elicit a P300, similar to the use of faces in the
famous faces speller. This approach was used in Geuze et al. (2014) [78], in which
subjects were instructed to press a button for all related stimuli in a stream, intended
to elicit both a P300 and an event-related desynchronisation (ERD) over the motor
cortex. The authors found a positive ERP for related stimuli from 300ms to 1 second,
and obtain classiﬁcation rates ranging from 59% to 77% using time and time-frequency
features. These classiﬁcation rates may depend on the P300, the ERD, and/or the N400,
and it is unclear to which degree each contribute. Regardless, they are higher than the
50%-72% for cross-validated, oﬄine classiﬁcation of the N400 in a similar task [18]. The
Wenzel study, notably, also established an ERP in addition to the N400, a left-lateralized
late positivity for unrelated stimuli. This matches the LPC or P600 responses that are
sometimes reported to co-occur with N400 tasks, and that have been interpreted as
late P300’s by some [53]. However, this response is in the opposite direction as ERP
in the Geuze et al.
(2014) study, where the unrelated stimuli were more negative.
Furthermore, in the Wenzel study, the relative strength of the N400 and this P600
diﬀered between the training and test phases (where subjects received an explicit task,
or no task, respectively). Further research would be required to understand the diﬀerent
factors at play here. While adding deliberate responses such as an ERD or a P300 to
this approach may certainly be successful, it does detract from one of the main draws of
the N400, its more automatic nature: an intuitive task ("process these stimuli") is likely
less cognitively taxing than an deliberate task ("do X when this stimulus appears").
These probing paradigms can also be improved by determining the right stimuli to
present at a given time, similar to the optimisation of ﬂashing patterns in P300 spellers.
By updating after each new stimulus, the information accumulated thus far can then
be exploited to select which stimulus would be particularly informative or to determine
whether suﬃcient conﬁdence has been reached to make a prediction. Which stimulus to
present next, in this scenario, is analogous to asking for which instance (i.e., stimulus)
the system would prefer to receive a label (i.e., the relatedness status) next. This is
a question explored in the ﬁeld of active learning, and techniques from this ﬁeld may
be easy to adopt (see Settles, 2012, for an overview [79]). A simple strategy is, for
instance, to present the stimulus for which the distribution across predicted/expected


## Page 17


The N400 for Brain Computer Interfacing
17
response(s) currently has the highest variance (known as ‘uncertainty sampling’). More
sophisticated strategies avoid potential pitfalls of uncertainty sampling, but can become
computationally expensive [79].
4. Discussion
We have outlined how the N400 can be elicited in various ways (visually or auditorily,
with linguistic or other meaningful stimuli) and how its amplitude is sensitive to a
range of experimental manipulations and parameters (active or passive mental context,
stimulus properties). Analyses of BCI studies across three application areas suggests
that the N400 can successfully be exploited for BCI purposes, but that the signal-to-
noise ratio is a limiting factor, with signal strength also varying strongly across subjects.
We have shown how this oﬀers a range of opportunities for exploitation, evidenced by
the applications discussed, as well as how it poses diﬃculty in designing BCI paradigms,
due to both an apparent low signal-to-noise ratio and a high potential of confounding
variables.
One unaddressed aspect is how to obtain labelled stimuli for eliciting these eﬀects.
For linguistic stimuli there many resources. For instance, for determining the relatedness
of two words there are association norms databases (e.g., [80, 81]). Alternative measures
of relatedness (e.g., similarity) can be extracted from WordNet [82] (see e.g., [83]). Word
embeddings from Computational Linguistic represent the meaning of a word as a (high
dimensional) vector, that can be used to compute relatedness (e.g., word2vec [84, 85]
or LSA [86, 87]). Lexical properties (e.g, word frequency and neighbourhood measures)
can be found in lexical databases (e.g., [88, 89]).
Databases also exist for sentence
stimuli (e.g., [90]), and word-embeddings can be extended to represent larger contexts
by averaging over terms (see e.g., [91]). For non-linguistic stimuli it is less trivial to
obtain labelled stimuli. For pictures Golenia et al. used the Flickr API that allows
images to be retrieved based on tags [75].
For face images in particular, there is a
Microsoft database for celebrity faces [92], though it may be non-trival to make these
suitable for insertion into e.g., a matrix speller.
We have discussed three lines of current research that use a N400 for BCI purposes:
(1) enhancing the matrix speller by using the (N170 and) N400 response to familiar faces,
(2) the detection of language processing in patients with Disorders of Consciousness
(DoC), and (3) the use of probe stimuli to infer information about a user’s mental
context.
The success of the use of famous faces in matrix spelling applications in
boosting spelling performance shows that the N400 can successfully be exploited for
BCI purposes. It would be of interest to see whether this performance boost extends to
covert speller paradigms, where the diﬀerences between face presentations for attended
and unattended letters derive only from the users interpretation of the relevance of the
stimulus, not the location of its presentation (foveal or peripheral) [93]. Furthermore,
the fact that repetitions of (face) stimuli have been established to attenuate the N400
amplitude provides an opportunity to explore whether presenting larger sets of faces


## Page 18


The N400 for Brain Computer Interfacing
18
may boost performance further.
The diagnosis of language processing in patients with DoC on the basis of the
N400, was shown to have prognostic value: patients that can be shown to exhibit an
N400 are more likely to improve in their condition or recover. At the same time it is
clear from comparative paradigms in healthy controls that the detection of the N400
even in the general population is non-trivial. An analysis in which we increased the
number of stimuli per class that are considered when making the decision for a given
subject, illustrated that detection rates continue to rise well beyond the number of
stimuli typically considered when judging the presence or absence of an N400. Low
detection rates of the N400, when considering small numbers of trials, can thus easily
be attributed to low signal-to-noise ratios as opposed to an indication of a lack of
linguistic processing. Next to increasing the number of stimuli presented to the subject
in order to make a judgement, this low signal-to-noise ratio can also be overcome by
accruing data across individuals, as demonstrated by Sculthorpe-Petley et al.
[68].
However whether ERPs from DoC patients are similar enough for this to work remains
an open question. To summarise, it is clear that when the N400 is used as a proxy
for determining language processing in an individual, the potential of a false negative
(deciding a patient does not process language when in fact they do), is substantial,
regardless of the statistical method, evidenced by the non-perfect detection rates in
healthy subjects. The probability of a false positive, conversely, will depend mostly on
the approach. Statistical approaches, if properly applied, are typically designed to have
a 5% probability of a type I error (i.e., a false positive). Using human raters gives a less
clear control of the false positive rate, though the results from Steppacher et al. [14]
show that it is not necessarily the case that human raters are more likely to produce
positive judgements, than a statistical method (see table 2).
Patients with a disorder of consciousness, whom have been determined to exhibit
an N400, could also be a target population for BCI paradigms that attempt to infer
information about the active mental context of the user, using the probing approaches.
Whether this has a potential for success depends on whether BCI control beyond
command following is even theoretically possible for DoC patients, and may depend
on the speciﬁc diagnosis (e.g., UWS or MCS).
This application of inferring information about the active mental context of the user
was the third application we discussed. On one hand there is evidence that this approach
can be used successfully to determine which of a small number of categories a subject
aims to select (’has on mind’) [16]. By using ﬁxation-related potentials, stimuli can be
presented to a user at a fast speed, as the inter-stimulus interval is determined by the
subject, through their gaze. On the other hand, approaches where this is attempted to
infer concepts from a larger space, the low signal-to-noise ratio becomes a problem, and
subject variability is ampliﬁed. Here limits to the exploitation of the N400 become clear:
Single trial classiﬁcation rates are low (˜50-75%), and there is high variability across
subjects in the strength of the N400 (see also ﬁgure 2), if it can be identiﬁed at all.
There are possibilities for improving these paradigms: e.g., by inducing an additional


## Page 19


The N400 for Brain Computer Interfacing
19
signal such as the P300 or by using techniques to do informed probe selection, however,
it is unclear whether this could ever lead to an application where subjects can select
from a large concept space (e.g, >1000).
The BCI applications explored so far focus on sentence level and priming eﬀects.
However, as higher level discourse or context also aﬀect the N400, it may be possible
to design BCI paradigms that exploit such eﬀects.
For this it is useful to have
representations of meaning coherence at a higher level.
As alluded to earlier, word
embedding vectors can used for this purpose.
For instance, Broderick et al.
[91],
demonstrate how a regression to a word-embedding measure of relatedness can be used to
measure comprehension of an audiobook. The authors ﬁt Temporal Response Functions
(TRFs) of EEG responses to word (dis)similarity values extracted from word2vec, using
averaged word vectors to represent sentence level context. These TRFs subsequently
exhibited a stronger negativity in the N400 time-range when ﬁtted to an attended story,
compared to a, simultaneously presented, unattended story. While in that study the
authors use the embeddings to calculate sentence level congruence, this measure could
also be extended to asses higher level semantic content, by averaging word vectors over
larger units of text (e.g., paragraphs and sections).
Combining measures of comprehension at diﬀerent levels, could allow indexation
of the level of understanding of a given text.
Such an approach could be used to
detect text comprehension, which may be of interest for a DoC language processing
application, but also for detecting whether someone is able to understand a given text
in a non-patient population.
It may be non-trivial to develop an application that
detects the level of expertise in a academic ﬁeld (do word-embeddings then need to
be trained on this academic literature?), but a more straightforward application may
be to determine appropriate reading levels in children.
A study by Holcomb et al.
(1992) [94] investigated the N400 in ages between 5 and 26 and found N400 amplitudes
to be larger for younger subjects, with amplitudes stabilising around age 15-16.
A
comprehension detection application may thus prove especially sensitive when aimed at
children. Such an approach could also be applied to adult second language learners.
These learners have, for instance, been shown to have distinguishable N400 responses
to foreign language words and pseudo-words after only 14 hours of instruction in the
respective language [95]. On a more speculative note, N400-like waves have even been
identiﬁed during sleep [96], which may allow for evaluation paradigms for which subjects
need not be awake.
These applications do not only exploit the active contextual eﬀects ("are you
processing the meaning of this text"), but also whether the passive requisite knowledge
is present for understanding.
It is good to point out that this can also be used to
elicit more personally identifying information about an individual. A strong illustration
of this is a recent study in which congruency eﬀects were elicited using Harry Potter
related stimuli, and the authors found a correlation between the N400 strength to these
stimuli and the self-reported familiarity with the Harry Potter fandom [97]. Such an
approach could be extended to predict an individual’s familiarity with the books, raising


## Page 20


REFERENCES
20
ethical considerations: an application based on active mental context, can be subverted
more easily than an application that probes your passive (world-) knowledge. While
(un)familiarity with Harry Potter may not constitute sensitive personal information
for most, these methods could perhaps be used to elicit other personal details, such
as political or religious beliefs. If BCI applications become more widely adopted, it
may become possible for malicious parties to covertly extract such information, by
strategically inserting certain linguistic stimuli within another application.
Whether these suggested applications are viable as BCI paradigms remains an open
question. It would be useful to have a better idea of the relative size of the diﬀerent
manipulations and a predictive model that can take the eﬀect size or signal-to-noise
ratio for a given manipulation and determine whether the N400 eﬀect is suﬃciently
strong that it is suitable for an intended BCI task. However, it appears size of the
N400 amplitude diﬀerence is highly dependent on the manipulation, task and subject
characteristics, making such an estimation non-trivial.
Overall, the N400 oﬀers access to someone’s active mental context or their passive
knowledge and associations, which makes it highly interesting for BCI applications,
yet its relatively low signal-to-noise ratio makes it diﬃcult to exploit. This makes the
N400 most suitable for applications where longer integration times (i.e., more stimulus
information that is averaged/accumulated over) are acceptable, such as the suggested
use of determining language processing through presentation of texts or audiobooks.
Acknowledgments
We thank Mante Nieuwland and Ceci Verbaarschot for helpful comments.
References
[1] Stephanie Martin, José del R. Millán, Robert T. Knight, and Brian N. Pasley.
The use of intracranial recordings to decode human language: Challenges and
opportunities. Brain and Language, July 2016.
[2] Walter S. Pritchard. Psychophysiology of P300. Psychological bulletin, 89(3):506,
1981.
[3] Ming Chang, Hiroyuki Iizuka, Yasushi Naruse, Hideyuki Ando, and Taro Maeda.
Unconscious learning of auditory discrimination using mismatch negativity (MMN)
neurofeedback. Scientiﬁc Reports, 4:6729, October 2014.
[4] Marcel van Gerven and Ole Jensen.
Attention modulations of posterior alpha
as a control signal for two-dimensional brain–computer interfaces.
Journal of
Neuroscience Methods, 179(1):78–84, April 2009.
[5] Matthias S. Treder, Ali Bahramisharif, Nico M. Schmidt, Marcel AJ van Gerven,
and Benjamin Blankertz. Brain-computer interfacing using modulations of alpha
activity induced by covert shifts of attention. Journal of NeuroEngineering and
Rehabilitation, 8(1):24, May 2011.


## Page 21


REFERENCES
21
[6] M. Kutas and S. A. Hillyard. Reading senseless sentences: brain potentials reﬂect
semantic incongruity. Science, 207(4427):203–205, January 1980.
[7] Marta Kutas and Kara D. Federmeier.
Thirty Years and Counting:
Finding
Meaning in the N400 Component of the Event-Related Brain Potential (ERP).
Annual Review of Psychology, 62(1):621–647, 2011.
[8] Shlomo Bentin, Gregory McCarthy, and Charles C. Wood. Event-related potentials,
lexical decision and semantic priming.
Electroencephalography and Clinical
Neurophysiology, 60(4):343–355, April 1985.
[9] Marijn van Vliet, Christian Mühl, Boris Reuderink, and Mannes Poel. Guessing
What’s on Your Mind: Using the N400 in Brain Computer Interfaces. In Yiyu Yao,
Ron Sun, Tomaso Poggio, Jiming Liu, Ning Zhong, and Jimmy Huang, editors,
Brain Informatics, Lecture Notes in Computer Science, pages 180–191. Springer
Berlin Heidelberg, 2010.
[10] T. Kaufmann, S. M. Schulz, C. Grünzinger, and A. Kübler. Flashing characters with
famous faces improves ERP-based brain–computer interface performance. Journal
of Neural Engineering, 8(5):056016, 2011.
[11] Tobias Kaufmann, Stefan M. Schulz, Anja Köblitz, Gregor Renner, Carsten Wessig,
and Andrea Kübler.
Face stimuli eﬀectively prevent brain–computer interface
ineﬃciency in patients with neurodegenerative disease. Clinical Neurophysiology,
124(5):893–900, May 2013.
[12] Jing Jin, Brendan Z. Allison, Yu Zhang, Xingyu Wang, and Andrzej Cichocki. An
ERP-based BCI using an oddball paradigm with diﬀerent faces and reduced errors
in critical functions. International journal of neural systems, 24(08):1450027, 2014.
[13] B. Kotchoubey, S. Lang, G. Mezger, D. Schmalohr, M. Schneck, A. Semmler,
V. Bostanov, and N. Birbaumer.
Information processing in severe disorders
of consciousness:
Vegetative state and minimally conscious state.
Clinical
Neurophysiology, 116(10):2441–2453, October 2005.
[14] Inga Steppacher, Simon Eickhoﬀ, Todor Jordanov, Michael Kaps, Wolfgang Witzke,
and Johanna Kissler.
N400 predicts recovery from disorders of consciousness.
Annals of Neurology, 73(5):594–602, 2013.
[15] Jerôme Daltrozzo,
Norma Wioland,
Veronique Mutschler,
Philippe Lutun,
Bartholomeus Calon, Alain Meyer, Thierry Pottecher, Simone Lang, Albert Jaeger,
and Boris Kotchoubey. Cortical Information Processing in Coma. Cognitive and
Behavioral Neurology, 22(1):53, March 2009.
[16] Markus Andreas Wenzel, Mihail Bogojeski, and Benjamin Blankertz. Real-time
inference of word relevance from electroencephalogram and eye gaze. Journal of
Neural Engineering, 2017.
[17] Jeroen Geuze, Marcel A. J. van Gerven, Jason Farquhar, and Peter Desain.
Detecting Semantic Priming at the Single-Trial Level. PLoS ONE, 8(4):e60377,
April 2013.


## Page 22


REFERENCES
22
[18] Karen Dijkstra, Jason Farquhar, and Peter Desain. Semantic Probing: Feasibility
of using sequential probes to decode what is on a user’s mind. bioRxiv, page 496844,
December 2018.
[19] Michael D. Rugg and Margaret E. Nagy. Event-related potentials and recognition
memory for words. Electroencephalography and Clinical Neurophysiology, 72(5):395–
406, May 1989.
[20] Michael D. Rugg.
Event-related brain potentials dissociate repetition eﬀects of
high-and low-frequency words. Memory & Cognition, 18(4):367–379, July 1990.
[21] Cyma Van Petten and Marta Kutas. Interactions between sentence context and
word frequencyinevent-related brainpotentials. Memory & Cognition, 18(4):380–
393, July 1990.
[22] Cyma Van Petten.
A comparison of lexical and sentence-level context eﬀects
in event-related potentials.
Language and Cognitive Processes, 8(4):485–531,
November 1993.
[23] Horacio A. Barber, Leun J. Otten, Stavroula-Thaleia Kousta, and Gabriella
Vigliocco. Concreteness in word processing: ERP and behavioral eﬀects in a lexical
decision task. Brain and Language, 125(1):47–53, April 2013.
[24] J. Kounios and P. J. Holcomb. Concreteness eﬀects in semantic processing: ERP
evidence supporting dual-coding theory.
Journal of Experimental Psychology.
Learning, Memory, and Cognition, 20(4):804–823, July 1994.
[25] Sarah Laszlo and Kara D. Federmeier.
The N400 as a snapshot of interactive
processing: Evidence from regression analyses of orthographic neighbor and lexical
associate eﬀects. Psychophysiology, 48(2):176–186, 2011.
[26] Phillip J. Holcomb, Jonathan Grainger, and Tim O’Rourke. An Electrophysio-
logical Study of the Eﬀects of Orthographic Neighborhood Size on Printed Word
Perception. Journal of Cognitive Neuroscience, 14(6):938–950, August 2002.
[27] Michael Dambacher, Reinhold Kliegl, Markus Hofmann, and Arthur M. Jacobs.
Frequency and predictability eﬀects on event-related potentials during reading.
Brain Research, 1084(1):89–103, April 2006.
[28] Rik van Dinteren, Martijn Arns, Marijtje L. A. Jongsma, and Roy P. C. Kessels.
P300 Development across the Lifespan: A Systematic Review and Meta-Analysis.
PLoS ONE, 9(2), February 2014.
[29] Kara D. Federmeier, Cyma Van Petten, Tanya J. Schwartz, and Marta Kutas.
Sounds, Words, Sentences:
Age-Related Changes Across Levels of Language
Processing. Psychology and Aging, 18(4):858–872, 2003.
[30] Brennan R. Payne and Kara D. Federmeier.
Contextual constraints on lexico-
semantic processing in aging:
Evidence from single-word event-related brain
potentials. Brain Research, 1687:117–128, May 2018.
[31] Jos J. A. Van Berkum, Colin M. Brown, Pienie Zwitserlood, Valesca Kooijman, and
Peter Hagoort. Anticipating Upcoming Words in Discourse: Evidence From ERPs


## Page 23


REFERENCES
23
and Reading Times. Journal of Experimental Psychology: Learning, Memory, and
Cognition, 31(3):443–467, 2005.
[32] Mante S. Nieuwland and Jos J. A. Van Berkum.
When Peanuts Fall in Love:
N400 Evidence for the Power of Discourse.
Journal of Cognitive Neuroscience,
18(7):1098–1111, July 2006.
[33] Peter Hagoort, Lea Hald, Marcel Bastiaansen, and Karl Magnus Petersson.
Integration of Word Meaning and World Knowledge in Language Comprehension.
Science, 304(5669):438–441, April 2004.
[34] Peter Hagoort, Giosuè Baggio, and Roel M. Willems. Semantic uniﬁcation. In
Michael S. Gazzaniga, editor, The cognitive neurosciences, 4th ed., pages 819–836.
MIT Press, Cambridge, MA, 2009.
[35] Ira Fischler,
Paul A. Bloom,
Donald G. Childers,
Salim E. Roucos,
and
Nathan W. Perry.
Brain Potentials Related to Stages of Sentence Veriﬁcation.
Psychophysiology, 20(4):400–409, 1983.
[36] Mante S. Nieuwland and Gina R. Kuperberg.
When the truth isn’t too hard
to handle:
An event-related potential study on the pragmatics of negation.
Psychological science, 19(12):1213–1218, December 2008.
[37] Marc Brysbaert, Amy Beth Warriner, and Victor Kuperman. Concreteness ratings
for 40 thousand generally known English word lemmas. Behavior Research Methods,
46(3):904–911, September 2014.
[38] Phillip J. Holcomb and Helen J. Neville. Auditory and Visual Semantic Priming in
Lexical Decision: A Comparison Using Event-related Brain Potentials. Language
and Cognitive Processes, 5(4):281–312, October 1990.
[39] Kurt Winsler, Katherine J. Midgley, Jonathan Grainger, and Phillip J. Holcomb.
An electrophysiological megastudy of spoken word recognition.
Language,
Cognition and Neuroscience, 33(8):1063–1082, September 2018.
[40] S. E. Barrett and M. D. Rugg. Event-related potentials and the semantic matching
of faces. Neuropsychologia, 27(7):913–922, January 1989.
[41] Martin Eimer. Event-related brain potentials distinguish processing stages involved
in face perception and recognition. Clinical Neurophysiology, 111(4):694–705, April
2000.
[42] Shlomo Bentin and Gregory McCarthy. The eﬀects of immediate stimulus repetition
on reaction time and event-related potentials in tasks of diﬀerent complexity.
Journal of Experimental Psychology: Learning, Memory, and Cognition, 20(1):130,
1994.
[43] Dorothee J. Chwilla, Colin M. Brown, and Peter Hagoort. The N400 as a function
of the level of processing. Psychophysiology, 32(3):274–285, May 1995.
[44] Diana Deacon, Françloise Breton, Walter Ritter, and Herbert G. Vaughan. The
Relationship Between N2 and N400: Scalp Distribution, Stimulus Probability, and
Task Relevance. Psychophysiology, 28(2):185–200, March 1991.


## Page 24


REFERENCES
24
[45] Diana Deacon and John Shelley-Tremblay. How automatically is meaning accessed:
a review of the eﬀects of attention on semantic processing. Frontiers in Bioscience,
5(Part E):82–94, 2000.
[46] Damian Cruse, Steve Beukema, Srivas Chennu, Jeﬀrey G. Malins, Adrian M. Owen,
and Ken McRae. The reliability of the N400 in single subjects: Implications for
patients with disorders of consciousness. NeuroImage: Clinical, 4:788–799, January
2014.
[47] Ellen F. Lau, Colin Phillips, and David Poeppel. A cortical network for semantics:
(de)constructing the N400. Nature Reviews Neuroscience, 9(12):920–933, December
2008.
[48] Giosuè Baggio and Peter Hagoort. The balance between memory and uniﬁcation
in semantics: A dynamic account of the N400. Language and Cognitive Processes,
26(9):1338–1367, November 2011.
[49] Mante S. Nieuwland, Dale J. Barr, Federica Bartolozzi, Simon Busch-Moreno,
Emily Darley, David I. Donaldson, Heather J. Ferguson, Xiao Fu, Evelien Heyselaar,
Falk Huettig, E. Matthew Husband, Aine Ito, Nina Kazanina, Vita Kogan, Zdenko
Kohút, Eugenia Kulakova, Diane Mézière, Stephen Politzer-Ahles, Guillaume
Rousselet, Shirley-Ann Rueschemeyer, Katrien Segaert, Jyrki Tuomainen, and
Sarah Von Grebmer Zu Wolfsthurn. Dissociable eﬀects of prediction and integration
during language comprehension: Evidence from a large-scale study using brain
potentials. bioRxiv, page 267815, January 2019.
[50] Milena Rabovsky, Steven S. Hansen, and James L. McClelland.
Modelling the
N400 brain potential as change in a probabilistic representation of meaning. Nature
Human Behaviour, 2(9):693–705, September 2018.
[51] Cyma Van Petten and Barbara J. Luka. Prediction during language comprehension:
Beneﬁts, costs, and ERP components. International Journal of Psychophysiology,
83(2):176–190, February 2012.
[52] Lee Osterhout and Phillip J Holcomb. Event-related brain potentials elicited by
syntactic anomaly. Journal of Memory and Language, 31(6):785–806, December
1992.
[53] Michelle Leckey and Kara D. Federmeier.
The P3b and P600(s):
Positive
contributions to language comprehension. Psychophysiology, 0(0):e13351, 2019.
[54] Miriam Kos, Danielle Van den Brink, and Peter Hagoort.
Individual Variation
in the Late Positive Complex to Semantic Anomalies. Frontiers in Psychology, 3,
2012.
[55] Jona Sassenhagen, Matthias Schlesewsky, and Ina Bornkessel-Schlesewsky.
The
P600-as-P3 hypothesis revisited: Single-trial analyses reveal that the late EEG
positivity following linguistically deviant material is reaction time aligned. Brain
and Language, 137:29–39, October 2014.


## Page 25


REFERENCES
25
[56] B. Z. Allison and J. A. Pineda. ERPs evoked by diﬀerent matrix sizes: implications
for a brain computer interface (BCI) system. IEEE Transactions on Neural Systems
and Rehabilitation Engineering, 11(2):110–113, June 2003.
[57] Shlomo Bentin and Leon Y. Deouell. Structural Encoding and Identiﬁcation in Face
Processing: Erp Evidence for Separate Mechanisms. Cognitive Neuropsychology,
17(1-3):35–55, February 2000.
[58] Sarah Laszlo, Mallory Stites, and Kara D. Federmeier. Won’t get fooled again:
An event-related potential study of task and repetition eﬀects on the semantic
processing of items without semantics. Language and cognitive processes, 27(2):257–
274, 2012.
[59] Steven Laureys, Gastone G. Celesia, Francois Cohadon, Jan Lavrijsen, José León-
Carrión, Walter G. Sannita, Leon Sazbon, Erich Schmutzhard, Klaus R. von Wild,
Adam Zeman, Giuliano Dolce, and the European Task Force on Disorders of
Consciousness. Unresponsive wakefulness syndrome: a new name for the vegetative
state or apallic syndrome. BMC Medicine, 8(1):68, November 2010.
[60] J. T. Giacino, S. Ashwal, N. Childs, R. Cranford, B. Jennett, D. I. Katz, J. P.
Kelly, J. H. Rosenberg, J. Whyte, R. D. Zafonte, and N. D. Zasler. The minimally
conscious state:
Deﬁnition and diagnostic criteria.
Neurology, 58(3):349–353,
February 2002.
[61] Andrea Kübler and Boris Kotchoubey. Brain–computer interfaces in the continuum
of consciousness. Current Opinion in Neurology, 20(6):643–649, 2007.
[62] A. Kübler and N. Birbaumer. Brain–computer interfaces and communication in
paralysis: Extinction of goal directed thinking in completely paralysed patients?
Clinical Neurophysiology, 119(11):2658–2666, November 2008.
[63] Adrian M. Owen, Martin R. Coleman, Melanie Boly, Matthew H. Davis, Steven
Laureys, and John D. Pickard.
Detecting Awareness in the Vegetative State.
Science, 313(5792):1402–1402, September 2006.
[64] Martin M. Monti, Audrey Vanhaudenhuyse, Martin R. Coleman, Melanie Boly,
John D. Pickard, Luaba Tshibanda, Adrian M. Owen, and Steven Laureys. Willful
modulation of brain activity in disorders of consciousness. New England Journal
of Medicine, 362(7):579–589, 2010.
[65] Damian Cruse, Srivas Chennu, Camille Chatelle, Tristan A Bekinschtein, Davinia
Fernández-Espejo, John D Pickard, Steven Laureys, and Adrian M Owen. Bedside
detection of awareness in the vegetative state:
a cohort study.
The Lancet,
378(9809):2088–2094, December 2011.
[66] Fei Wang, Yanbin He, Jun Qu, Qiuyou Xie, Qing Lin, Xiaoxiao Ni, Yan Chen,
Jiahui Pan, Steven Laureys, Ronghao Yu, and Yuanqing Li. Enhancing clinical
communication assessments using an audiovisual BCI for patients with disorders of
consciousness. Journal of Neural Engineering, 14(4):046024, June 2017.


## Page 26


REFERENCES
26
[67] B. Kotchoubey, S. Veser, R. Real, C. Herbert, S. Lang, and A. Kübler. Towards a
more precise neurophysiological assessment of cognitive functions in patients with
disorders of consciousness. Restorative Neurology and Neuroscience, 31(4):473–485,
January 2013.
[68] Lauren Sculthorpe-Petley, Careesa Liu, Sujoy Ghosh Hajra, Hossein Parvar, Jason
Satel, Thomas P. Trappenberg, Rober Boshra, and Ryan C. N. D’Arcy. A rapid
event-related potential (ERP) method for point-of-care evaluation of brain function:
Development of the Halifax Consciousness Scanner.
Journal of Neuroscience
Methods, 245:64–72, April 2015.
[69] Vladimir Bostanov and Boris Kotchoubey. The t-CWT: A new ERP detection and
quantiﬁcation method based on the continuous wavelet transform and Student’s
t-statistics. Clinical Neurophysiology, 117(12):2627–2644, December 2006.
[70] Benjamin Rohaut, Frédéric Faugeras, Nicolas Chausson, Jean-Rémi King, Imen El
Karoui, Laurent Cohen, and Lionel Naccache. Probing ERP correlates of verbal
semantic processing in patients with impaired consciousness.
Neuropsychologia,
66:279–292, January 2015.
[71] Paul W. Schoenle and Wolfgang Witzke. How vegetative is the vegetative state?
Preserved semantic processing in VS patients–evidence from N 400 event-related
potentials. NeuroRehabilitation, 19(4):329–334, 2004.
[72] Ken McRae, George S. Cree, Mark S. Seidenberg, and Chris Mcnorgan. Semantic
feature production norms for a large set of living and nonliving things. Behavior
Research Methods, 37(4):547–559, November 2005.
[73] Douglas L. Nelson, Cathy L. McEvoy, and Thomas A. Schreiber. The University
of South Florida free association, rhyme, and word fragment norms.
Behavior
Research Methods, Instruments, & Computers, 36(3):402–407, August 2004.
[74] Eric Maris and Robert Oostenveld. Nonparametric statistical testing of EEG- and
MEG-data. Journal of Neuroscience Methods, 164(1):177–190, August 2007.
[75] Jan-Eike Golenia, Markus A. Wenzel, Mihail Bogojeski, and Benjamin Blankertz.
Implicit relevance feedback from electroencephalography and eye tracking in image
search. Journal of Neural Engineering, 15(2):026002, 2018.
[76] Sarah E Barrett and Michael D Rugg. Event-related potentials and the semantic
matching of pictures. Brain and Cognition, 14(2):201–212, November 1990.
[77] Brendan Z. Allison and Christa Neuper. Could Anyone Use a BCI? In Brain-
Computer Interfaces, Human-Computer Interaction Series, pages 35–54. Springer,
London, 2010.
[78] Jeroen Geuze, Jason Farquhar, and Peter Desain.
Towards a Communication
Brain Computer Interface Based on Semantic Relations. PLoS ONE, 9(2):e87511,
February 2014.
[79] Burr Settles. Active Learning. Synthesis Lectures on Artiﬁcial Intelligence and
Machine Learning, 6(1):1–114, June 2012.


## Page 27


REFERENCES
27
[80] G.R. Kiss, C. Armstrong, R. Milroy, and J. Piper. An associative thesaurus of
English and its comupter analysis. In A.J. Aitken, R.W. Bailey, and N. Hamilton-
Smith, editors, The Computer and Literary Studies. Edinburgh: University Press,
1973.
[81] Simon De Deyne and Gert Storms. Word associations: Norms for 1,424 Dutch
words in a continuous task. Behavior Research Methods, 40(1):198–205, February
2008.
[82] Christiane Fellbaum.
WordNet.
In The Encyclopedia of Applied Linguistics.
Blackwell Publishing Ltd, 2012.
[83] Alexander Budanitsky and Graeme Hirst. Evaluating WordNet-based Measures of
Lexical Semantic Relatedness. Comput. Linguist., 32(1):13–47, March 2006.
[84] Tomas Mikolov, Ilya Sutskever, Kai Chen, Greg S Corrado, and JeﬀDean.
Distributed Representations of Words and Phrases and their Compositionality. In
C. J. C. Burges, L. Bottou, M. Welling, Z. Ghahramani, and K. Q. Weinberger,
editors, Advances in Neural Information Processing Systems 26, pages 3111–3119.
Curran Associates, Inc., 2013.
[85] word2vec
-
Tool
for
computing
continuous
distributed
representations
of
words., 2013.
Available at https://code.google.com/archive/p/word2vec/
#Pre-trained_word_and_phrase_vectors.
[86] Thomas K. Landauer, Peter W. Foltz, and Darrell Laham. An introduction to
latent semantic analysis. Discourse Processes, 25(2-3):259–284, January 1998.
[87] LSA @ CU Boulder. Available at http://lsa.colorado.edu/.
[88] David A. Balota, Melvin J. Yap, Keith A. Hutchison, Michael J. Cortese, Brett
Kessler, Bjorn Loftis, James H. Neely, Douglas L. Nelson, Greg B. Simpson, and
Rebecca Treiman.
The English Lexicon Project.
Behavior Research Methods,
39(3):445–459, August 2007.
[89] R Harald Baayen, Richard Piepenbrock, and Leon Gulikers.
The celex lexical
database (release 2). Distributed by the Linguistic Data Consortium, University of
Pennsylvania, 1995.
[90] Cady K. Block and Carryl L. Baldwin. Cloze probability and completion norms
for 498 sentences: Behavioral and neural validation using event-related potentials.
Behavior Research Methods, 42(3):665–670, August 2010.
[91] Michael P. Broderick, Andrew J. Anderson, Giovanni M. Di Liberto, Michael J.
Crosse, and Edmund C. Lalor.
Electrophysiological Correlates of Semantic
Dissimilarity Reﬂect the Comprehension of Natural, Narrative Speech. Current
Biology, 28(5):803–809.e3, March 2018.
[92] MSRA-CFW - Data Set of Celebrity Faces on the Web.
Available at https:
//msropendata.com/datasets/d80afccb-991d-4ec2-9f67-9ce188a2b7fc.
[93] Matthias S. Treder and Benjamin Blankertz. (C)overt attention and visual speller


## Page 28


REFERENCES
28
design in an ERP-based brain-computer interface. Behavioral and Brain Functions,
6:28, May 2010.
[94] Phillip J. Holcomb, Sharon A. Coﬀey, and Helen J. Neville. Visual and auditory
sentence processing: A developmental analysis using event-related brain potentials.
Developmental Neuropsychology, 8(2-3):203–241, January 1992.
[95] Judith McLaughlin, Lee Osterhout, and Albert Kim. Neural correlates of second-
language word learning:
minimal instruction produces rapid change.
Nature
Neuroscience, 7(7):703, July 2004.
[96] Agustín M. Ibáñez, René San Martín, Esteban Hurtado, and Vladimir López. ERPs
studies of cognitive processing during sleep. International Journal of Psychology,
44(4):290–304, 2009.
[97] Melissa Troyer and Marta Kutas. Harry Potter and the Chamber of What?: the
impact of what individuals know on word processing during reading. Language,
Cognition and Neuroscience, 0(0):1–17, August 2018.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1908_10773v1_the_n400_for_brain_computer_interfacing_complexities_and_opportunities
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1908_10773V1_THE_N400_FOR_BRAIN_COMPUTER_INTERFACING_COMPLEXITIES_AND_OPPORTUNITIES.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

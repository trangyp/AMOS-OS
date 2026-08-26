---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1903.08459v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1903.08459v1_Smart_Edition_of_MIDI_Files

> Source: 1903.08459v1_Smart_Edition_of_MIDI_Files.pdf

> Pages: 20

---


## Page 1


Smart Edition of Midi Files
Pierre Roy and Franc¸ois Pachet
Spotify
Abstract
We address the issue of editing musical performance data, in particular Midi ﬁles representing hu-
man musical performances. Editing such sequences raises speciﬁc issues due to the ambiguous nature
of musical objects. Te ﬁrst source of ambiguity is that musicians naturally produce many deviations
from the metrical frame. Tese deviations may be intentional or subconscious, but they play an im-
portant role in conveying the groove or feeling of a performance. Relations between musical elements
are also usually implicit, creating even more ambiguity. A note is in relation with the surrounding
notes in many possible ways: it can be part of a melodic pattern, it can also play a harmonic role
with the simultaneous notes, or be a pedal-tone. All these aspects play an essential role that should
be preserved, as much as possible, when editing musical sequences.
In this paper, we contribute speciﬁcally to the problem of editing non-quantized, metrical musical
sequences represented as Midi ﬁles. We ﬁrst list of number of problems caused by the use of naive
edition operations applied to performance data, using a motivating example. We then introduce a
model, called Dancing Midi, based on 1) two desirable, well-deﬁned properties for edit operations
and 2) two well-deﬁned operations, split and concat, with an implementation. We show that our
model formally satisﬁes the two properties, and that it prevents most of the problems that occur
with naive edit operations on our motivating example, as well as on a real-world example using an
automatic harmonizer.
1
Introduction
Te term music performance denotes all musical artefacts produced by one or more human musicians
playing music, such as a pianist performing a score or accompanying a singer, a violin section playing an
orchestration of a piece or a jazz musician improvizing a solo on a given lead sheet. Music performance
can be represented in various ways, depending on the context of use: printed notation, such as scores
or lead sheets, audio signals, or performance acquisition data, such as piano-rolls or Midi ﬁles. Each of
these representations captures partial information about the music that is useful in certain contexts, with
its own limitations [4]. Printed notation oﬀers information about the musical meaning of a piece, with
explicit note names and chord labels (in, e.g., lead sheets), and precise metrical and structural information,
but it tells little about the sound. Audio recordings render timbre and expression accurately, but provide
no information about the score. Symbolic representations of musical performance, such as Midi, provide
precise timings are are therefore well adapted to edit operations, either by humans or by sofware.
Te need for editing musical performance data arises from two situations. First, musicians ofen need
to edit performance data when producing a new piece of music. For instance, a jazz pianist may play an
improvized version of a song, but this improvization should be edited to accommodate for a posteriori
changes in the structure of the song. Te second need comes from the rise of AI-based automatic music
generation tools. Tese tools usually work by analyzing existing human performance data to produce new
ones (see, e.g. [3] for a survey). Whatever the algorithm used for learning and generating music, these tools
1
arXiv:1903.08459v1  [cs.SD]  20 Mar 2019


## Page 2


call for editing means that preserve as far as possible the expressiveness of original sources. We address the
issue of editing musical performance data represented as Midi ﬁles, while preserving as much as possible
its semantics, in a sense deﬁned below.
However, editing music performance data raises speciﬁc issues related to the ambiguous nature of
musical objects. Te ﬁrst source of ambiguity is that musicians produce many temporal deviations from
the metrical frame. Tese deviations may be intentional or subconscious, but they play an important part
in conveying the groove or feeling of a performance. Relations between musical elements are also usually
implicit, creating even more ambiguity. A note is in relation with the surrounding notes in many possible
ways: it can be part of a melodic pattern, it can also play a harmonic role with the simultaneous notes, or
be a pedal-tone. All these aspects, although not explicitly represented in a Midi ﬁle, play an essential role
that should be preserved, as much as possible, when editing such musical sequences.
Te Midi format is widespread in the instrument industry and Midi editors are commonplace, for in-
stance in Digital Audio Workstations. Paradoxically, the problem of editing Midi with semantic-preserving
operations was not addressed yet, to our knowledge. Attempts to provide semantically-preserving edit
operations have been made on the audio domain (e.g. [13]) but these are not transferrable to music per-
formance data, as we explain below.
In human-computer interaction, cut, copy and paste [11] are the Holy Trinity of data manipulation.
Tese three commands proved to be so useful that they are now incorporated in virtually every sofware,
such as word processing, programming environments, graphics creation, photography, audio signal, or
movie editing tools. Recently, they have been extended to run across devices, enabling moving text or
media from, for instance, a smartphone to a computer. Tese operations are simple and have a clear,
unambiguous semantics: cut, for instance, consists in selecting some data, say a word in a text, removing
it from the text, and saving it to a clipboard for later use.
Each type of data to be edited raises its own editing issues that led to the development of speciﬁc
editing techniques. For instance, edits of audio signals usually require cross fades to prevent clicks. Simi-
larly, in movie editing, fade-in and fade-out are used to prevent harsh transitions in the image ﬂow. Edge
detection algorithms were developed to simplify object selection in image editing. Te case of Midi data
is no exception. Every note in a musical work is related to the preceding, succeeding, and simultaneous
notes in the piece. Moreover, every note is related to the metrical structure of the music. In Section 2, we
list a number of issues occurring when applying na¨ıve edition commands to a musical stream.
In this paper, we restrict ourself to a speciﬁc type of musical performance data: non-quantized, metri-
cal music data, i.e. performances which are recorded with free expression but with a ﬁxed, known tempo.
Tis includes most of MIDI ﬁles available on the web (for instance [9] ). Tis excludes MIDI ﬁles consisting
of free improvization, or music performance with no ﬁxed tempo. Note that these could also be included
in the scope of our system, using automatic downbeat estimation methods, but we do not consider this
case in this paper.
It is not possible, to our knowledge, to deﬁne a precise semantics to musical performance in general. In
this paper we contribute to the problem of editing non-quantized, metrical musical sequences represented
as Midi ﬁles in the following way:
1. We list of number of problems caused by the use of naive edition operations applied to performance
data, using a motivating example;
2. We then introduce a model, called Dancing Midi, based on 1) two desirable, well-deﬁned properties
for edit operations and 2) two well-deﬁned operations, split and concat, with an implementation.
Tese primitives can be used to create higher-level operations, such as cut, copy, or paste;
2


## Page 3


3. We show that our model formally satisﬁes the two properties;
4. We show additionally that our model does not create most of the problems that occur with naive
edit operations on our motivating example, as well as on a real-world example using an automatic
harmonizer.
2
Motivating Example
Figure 1: A piano roll with ﬁve measures extracted from a piece by Brahms. Colors indicate note velocities
(blue is sof, green is medium, and brown is loud). A typical edit operation: the goal is to cut the ﬁrst two
beats of Measure 3 and insert them at the beginning of Measure 6.
Figure 1 shows a piano roll representing ﬁve measures extracted from a Midi stream consisting of a
performance capture of Johannes Brahms’s Intermezzo in B♭minor. Consider the problem of cutting the
ﬁrst two beats of Measure 3 and inserting these two beats at the beginning of Measure 6. Figure 2 shows the
piano roll produced when these operations are performed in a straightforward way, i.e., when considering
notes as mere time intervals. Notes that are played across the split temporal positions are segmented,
leading to several musical inconsistencies. First, long notes, such as the highest notes, are split into several
contiguous short notes. Tis alters the listening experience, as several attacks are heard, instead of a single
one. Additionaly, the note velocities (a Midi equivalent of loudness) are possibly changing at each new
attack, which is unmusical. Another issue is that splitting notes with no consideration of the musical
context leads to creating excessively short note fragments, which we call residuals, e.g., at the bottom right
in Figure 2. Residuals are disturbing, especially if their velocity is high, and are somehow analogous to
clicks in audio signals. Finally, a side-eﬀect of this approach is that some notes are quantized (last two
beats of Measure 5). As a result, slight temporal deviations present in the original Midi stream are lost in
the process. Such temporal deviations are important parts of the performance, as they convey the groove,
or feeling of the piece, as interpreted by the musician.
Here is a list of musical issues occurring when raw editing a Midi stream:
1. Creation of residuals, i.e., excessively brief notes;
2. Splitting long notes, creating superﬂuous attacks;
3. Creating surprising, inconsistent changes in note velocities;
4. Losing small temporal deviations with respect to the metrical structure, leading to unnecessary,
undesirable quantization.
3


## Page 4


Figure 2: Raw editing the piano roll in Figure 1 produces a poor musical result: long notes are split,
residuals are created, some notes are quantized, and note velocities are inconsistent. Tis piano roll was
obtained using Apple Logic Pro X Midi editor, using the “split” option, see Section 3.
Figure 3: Solving the Midi edition problem stated in Figure 1 using the model we present here. Tere are
no short note residuals, long notes are held and there are no harsh changes in velocities. Small temporal
deviations are preserved (no quantization). Tis is to be compared to Figure 2.
Figure 3 shows another solution to the problem, obtained using the model presented in this article.
Comparing Measure 5 in Figures 2 and 3 shows obvious diﬀerences in the two approaches: none of the
issues produced with raw edits, shown in Figures 2, are present in the piano roll shown in Figures 3.
3
State of the Art
LogicPro X, the Digital Audio Workstation commercialized by Apple, features a full-featured Midi editor.
As shown in Figure 4, when editing a Midi stream, the decisions regarding notes that overlap with the
selected regions are lef to the user who has to decide whether to split, shorten (to ﬁt the region boundaries)
or keep the notes. Figure 2 shows the piano roll produced using the ﬁrst option, split. In the latter case,
keep, when pasting somewhere else, the notes will be put back with their original duration, even if it
exceeds the region boundaries. Tis forces the user to decide explicitly what to do, and the decision
applies to all notes, regardless of the musical context. Besides, this strategy leads to creating overlapping
notes, which create ambiguous situations as the Midi format does not have a way to handle overlapping
notes with the same pitch.
Te piano roll panel in Avid Pro Tools, another major Digital Audio Workstation, oﬀers less control
on Midi edits than Logic Pro X. Figure 5 shows the piano roll obtained with Pro Tools, when using the
basic copy and paste functions on the motivating example. Tis piano roll is essentially the same as that
in Figure 2, except note velocities are not displayed.
4


## Page 5


Figure 4: Te menu that pops up when splitting a Midi stream with Apple Logic Pro X Digital Audio
Workstation. Here, we split at both ends of a region covering the ﬁrst two beats of Measure 3 (yellow
zone). Te system lets the user decide what they want explicitly regarding notes that cross the split region
boundaries.
Figure 5: Te piano roll produced when editing the motivating example using the piano roll module in
Avid Pro Tools.
5


## Page 6


4
Te Model
In this section, we present a model of temporal sequences that allows us to implement two primitives:
split and concat. Te split primitive is used to break a Midi stream (or Midi ﬁle) at a speciﬁed temporal
position, yielding two Midi streams: the ﬁrst one contains the music played before the split position and
the second one contains the music played afer. Te concat operation takes two Midi streams as inputs
and returns a single stream by appending the second stream to the ﬁrst one. Te model is called Dancing
Midi since the underlying technique (see Section 4.2) bears some similarity with the idea of Dancing Links
that Donald Knuth developed in [6]
High-level edit operations, such as copy, cut, paste, or insert, may be performed by applying split and
concat to the right streams. For example, to cut a Midi stream S between temporal positions t1 and t2,
we execute the sequence of primitive operations
1. (S′, Sr) ←split(S, t2), i.e., we split S at t2;
2. (Sl, Sm) ←split(S′, t1), i.e., we split S′ at t1.
3. Return concat(Sl, Sr);
Te stream Sm is removed from S and it could be stored in a Midi clipboard for later use. Similarly, to
insert a Midi stream T in a stream S at temporal position t, one can perform:
1. (S1, S2) ←split(S, t), i.e., split S at t;
2. Return concat (concat (S1, T) , S2).
In our model, a continuous subdivision of time coexists with a discrete, regular subdivision of time, in, e.g.,
beats or measures, which is equivalent to the metrical frame of a musical sequence. Te constant distance
between discrete temporal positions is denoted by δ. Musical events, e.g., notes, rests, chords, may occur
at any continuous temporal position. On the contrary, split and concat are applicable only on discrete
temporal positions, i.e., multiples of δ. In short, musical events may be placed at any position, and take
arbitrary durations, within a regularly decomposed time frame.
We made the practical choices to represent time by integers and to consider only sequences start-
ing at time 0 and whose duration is a multiple of the segmentation subdivision, which is denoted by δ.
Tese choices aim at simplifying the implementation and clarifying the presentation without limiting the
generality of the model1.
A (time) event e is deﬁned by its start and end times, denoted by e−and e+, two nonnegative integers,
with e−≤e+. We consider sequences of non-overlapping time events. A sequence S with a duration d(S)
is an ordered list of time events E(S) = (e1, . . . , en), such that:
• d(S) ≡0 (mod δ), i.e., the duration of S is a multiple of δ,
• e+
n ≤d(S), i.e., all events are within the sequence, and
• e+
i ≤e−
i+1, ∀i = 1, . . . , n −1, i.e., there are no overlapping events.
Te set of all such sequences is denoted by Sδ.
Te model handles sequences of non-overlapping time intervals (elements of Sδ), and therefore can-
not directly deal with Midi streams, which contain overlapping intervals (e.g., chords consist of three or
1In Midi ﬁles, time is represented by integer numbers, based on a predeﬁned resolution, typically 960 ticks per beats.
6


## Page 7


more overlapping intervals). Terefore, we decompose a Midi stream into individual sequences of non-
overlapping events, one for each unique pitch and unique Midi channel. We show, in Section 4.5, how this
approach applies to real Midi streams.
4.1
Problem Statement
We address the problem of implementing split and concat in an eﬃcient and sensible (from a musical
viewpoint) way. Te split primitive breaks a sequence at a speciﬁc temporal position and the concat
primitive returns a sequence formed by concatenating two sequences:
split: Sδ × {0, δ, 2δ, . . . , d(S)} →Sδ × Sδ
(S, t) 7→(Sl, Sr),
where t is the segmentation position, Sl is the lef part of S, from 0 to t, hence d(Sl) = t, and Sr is the
right part of S, afer position t, with d(Sr) = d(S) −t and
concat: Sδ × Sδ →Sδ
(S1, S2) 7→S = S1 ⊕S2.
where S is a sequence of duration d(S) = d(S1) + d(S2) constructed by appending S2 to S1.
Te types above specify that split and concat create sequences of Sδ, i.e., , sequences with no over-
lapping events and with all events falling within the sequence’s bounds.
We call residual an event whose duration is shorter than a predeﬁned threshold ε. We deﬁne two
properties for split and concat:
(P1) split and concat are the inverse of one another, i.e.,
a. ∀S ∈Sδ, ∀t ∈{0, δ, 2δ, . . . , d(S)}, concat(split(S, t)) = S
b. ∀S, T ∈Sδ, split(concat(S, T), d(S)) = (S, T)
(P2) split and concat never create residuals, i.e.,
a. let S ∈Sδ, ∀t ∈{0, δ, 2δ, . . . , d(S)} and (S1, S2) = split(S, t), then ∀e ∈S1 ∪S2,
d(e) < ε ⇒e ∈S,
b. ∀S, T ∈Sδ, ∀e ∈S ⊕T, d(e) < ε ⇒e ∈S ∪T.2
Property (P1) states that splitting a sequence and merging back the resulting sequences produces the
original sequence and, conversely, concatenating two sequences and splitting them again at the same po-
sition, returns the two original sequences. Tis is to ensure that no information is lost upon splitting and
concatenating sequences. Additionally, as we show in Section 4.3, this property oﬀers the beneﬁts of a
powerful, generalized undo mechanism.
Property (P2) ensures that no residual is created: the only residuals appearing in a sequence obtained
using split or concat were already in the original sequence(s). Note that the second part, i.e., (P2)(b.), is
a bit simpliﬁed, as we explain in Section 4.2.3.
It is easy to design split and concat primitives that satisfy either (P1) or (P2). However, as we will
illustrate now, it is diﬃcult to enforce (P1) and (P2). It is the combination of these two properties that
ensures that no information is lost and that no residual is created.
2Tis is a simpliﬁcation, as we explain in Section 4.2.3
7


## Page 8


Figure 6 shows a simple sequence S of duration d(S) = 20, with a regular temporal subdivision
δ = 10 time units, and containing event e, with e−= 8 and e+ = 12. We consider the problem of
splitting S in its middle (t = 10) and concatenating back the two extracted sequences.
Figure 6: A simple sequence with a single event (gray box) and a regular subdivision of 10 time units.
Assuming the threshold for brief events is set to ε = 3 time units, split and concat should not create
events shorter than 3. Figure 7 shows the result of splitting S into S1 and S2 and concatenating S1 and S2,
performed in a straightforward way by raw event segmentation, i.e., cut exactly at the speciﬁed position,
and with no additional processing. Te concatenation S1 ⊕S2 is identical to the original sequence S,
satisfying Property (P1). However, this approach creates two events of duration 2 in the split sequences
S1 and S2, which violates the residual Property (P2) for ε = 3.
On Figure 8, on the contrary, short fragments are omitted, by adding a simple ﬁlter, fulﬁlling Prop-
erty (P2) as no residuals show up on split sequences S1 and S2. However, S1 ⊕S2 is empty, which violates
the reversibility Property (P1).
Figure 7: Straightforward approach: sequence S (top) is split at t = 10, yielding sequences S1 and S2
(middle), with two residuals (events of duration 2), then S1 and S2 are concatenated resulting in S1 ⊕S2,
which is identical to S, as expected.
Figure 8: Applying the straightforward approach with a ﬁlter for residuals results in creating no residuals
(S1 and S2 are empty, as expected), but violates the reversibility as S1 ⊕S2 ̸= S.
8


## Page 9


Tis example sugests that some memory is needed to implement the split and concat operations
so they satisfy (P1) and (P2). We show in the next section how to deﬁne this operations with a minimal
amount of memory.
4.2
Model Implementation
Te implementation of the model is based on memory cells that store information about the events oc-
curring at each segmentation position in a sequence.
4.2.1
Computing the Memory Cells
For a given segmentation position t, for each event e containing t, i.e., e−≤t ≤e+, we compute the
length of e that lies before t and the length of e afer t. Tese two quantities are stored in two memory
cells, a lef and a right memory cell, as shown in Figure 9. Te lef cell stores only information related to
events starting strictly before t and, conversely, the right cell stores information related to events ending
strictly afer t. Tere are ﬁve possible conﬁgurations, which are shown in Figure 9. When the sequence is
split at position t, the memory cells of S at position t are distributed to the resulting sequences: the lef
cell is associated to the lef sequence, at position t and the right cell is associated to the right sequence at
position 0. Tese values will be used to concatenate these subsequences with other sequences, using the
concat operation. Algorithm 1 computes the two memory cells for a sequence and a speciﬁc segmentation
position.
Figure 9: Te lef and right memory cells at segmentation position t. Case 1: no interval, the memory is
“empty”; case 2: a lef-touching interval of length 12, stored in the lef memory cell; case 3: same as 2 except
on the right and length is 5; case 4: two touching intervals, each stored in the corresponding cell; case 5: a
crossing interval, the lef and right memories store the interval’s length before and afer t.
4.2.2
Implementation of split
Te split primitive, described by Algorithm 2, consists in distributing the intervals to the lef and right
sequences, Sl and Sr, as follows: intervals occurring before the segmentation position t are allocated to
Sl and intervals occurring afer t are allocated to Sr. Te memory of the original sequence is copied to
the resulting sequences in a similar way: memory cells stored before t are copied to the lef sequence at
9


## Page 10


Algorithm 1 Compute (ll, lr), (rl, rr), the lef and right memory cells of S at t.
1: procedure ComputeMemory(S, t)
2:
if t = 0 then
▷t is the start time of S
3:
if ∃e ∈S such that e−= 0 then return (0, 0), (0, d(e))
4:
else return (0, 0), (0, 0)
5:
else if t = d(S) then
▷t is the end time of S
6:
if ∃e ∈S such that e+ = d(S) then return (d(e), 0), (0, 0)
7:
else return (0, 0), (0, 0)
8:
else
▷t is within the sequence
9:
if ∃e ∈S with e−< t < e+ then return (t −e−, e+ −t), (t −e−, e+ −t)
10:
else if ∃e1, e2 ∈S with e+
1 = e−
2 = t then return (d(e1), 0), (0, d(e2))
11:
else if ∃e ∈S with e−= t then return (0, 0), (0, d(e))
12:
else if ∃e ∈S with e+ = t then return (d(e), 0), (0, 0)
13:
else return (0, 0), (0, 0)
the same position; memory cells of S stored afer t are copied to the right sequence, with oﬀset −t as all
sequences start at position 0 (see Section 4).
A speciﬁc treatment is required at position t, to avoid creating residuals that could appear when
splitting short intervals containing position t, in order to satisfy Property (P2)(a.). If an event e contains
t, i.e., e−< t < e+, we consider the memory cells ll, lr, rl, and rr stored in M(S, t) to decide whether
an event of length ll should be added at the very end of the lef sequence. Te event is added if it is not
a residual, i.e., ll > ε or if it is a residual that already existed in S, i.e., lr = 0 and ll > 0. A similar
treatment is applied to decide if an event of length rr is inserted at the very beginning of Sr. Note that,
doing this, we ignore the actual events, and only consider the memory. Tis is reﬂected in lines 16 and 18
in Algorithm 2.
Sequence Sl is such that the space between t −ll and t is either empty of event or it contains a single
event [t −ll, t], possibly lef-trimmed so it does not start before 0:
e+ ≤t −M(Sl, t).ll, ∀e ∈Sl or [max{0, t −M(Sl, t).ll}, t] ∈Sl
(1)
and Sr is such that the space between 0 and rr is either empty of event or it contains a single event [0, rr],
possibly right-trimmed so it does not exceed the sequence’s end time:
e−≥M(Sr, 0).rr, ∀e ∈Sr or [0, min{M(Sr, 0).rr, d(Sr)}] ∈Sr
(2)
Note that the way the memory is computed, see Algorithm 1, ensures that (1) and (2) are satisﬁed by any
sequence before it is split.
4.2.3
Implementation of concat
Concatenating two sequences S1 and S2 creates a new sequence S, whose duration d(S) = d −1 + d2,
with d1 = d(S1) and d2 = d(S2). All events of S1 that end strictly before d1 are added to S, as well as
all events of S2 that start strictly afer 0. Te only delicate operation is to decide what to do at position
d1 in S.
In Section 4.2.2, we have seen that all sequences satisfy (1) and (2). Terefore, to concatenate S1 and
S2, we need to consider four cases:
10


## Page 11


Algorithm 2 Split S at t.
1: procedure ComputeMemory(S, t)
▷δ is the regular subdivision of time; d(S) = nδ; t = mδ with 0 < m < n.
2:
Sl ←empty sequence with d(Sl) = t
3:
Sr ←empty sequence with d(Sr) = d(S) −t
▷copies the memory cells from S
4:
for i = 0, . . . , m do
5:
M(Sl, iδ) ←M(S, iδ)
6:
for i = m, . . . , n do
▷translate by −t, as Sr starts at 0
7:
M(Sr, iδ −t) ←M(S, iδ)
8:
for e ∈S do
9:
if e+ ≤t then
10:
add e to Sl
11:
else if e−≥t then
12:
add event [e−−t, e+ −t] to Sr
13:
else
▷e satisﬁes e−< t < e+
14:
(ll, lr), (rl, rr) ←M(S, t)
▷shortcut notations
15:
if ll ≥ε or (lr = 0 and ll > 0) then
16:
add event [max(0, t −ll), t] to Sl
17:
if rr ≥ε or (rl = 0 and rr > 0) then
18:
add event [(0, min(d(S), rr)] to Sr
19:
return Sl, Sr
▷d(Sl) = t = mδ and d(Sr) = d(S) −t
1. e+ ≤t−M(S1, d1).ll, ∀e ∈Sl and e−≥M(S2, 0).rr, ∀e ∈S2, i.e., S1 has no event overlapping
with the temporal segment deﬁned by M(S1, d1).ll, its lef-memory at d1 and, similarly, S2 has
no event overlapping with the temporal segment deﬁned by M(S2, 0).rr, its right-memory at 0;
2. e+ ≤t −M(S1, d1).ll, ∀e ∈Sl and [0, min{M(S2, 0).rr, d(S2)}] ∈S2, i.e., S1 has no event
overlapping with the temporal segment deﬁned by M(S1, d1).ll, its lef-memory at d1 and S2 has
an event occupying the temporal segment deﬁned by M(S2, 0).rr, its right-memory at 0;
3. [max{0, t −M(S1, d1).ll}, t] ∈Sl and e−≥M(S2, 0).rr, ∀e ∈S2 has an event occupying the
temporal segment deﬁned by M(S1, d1).ll, its lef-memory at d1 and S2 has no event overlapping
with the temporal segment deﬁned by M(S2, 0).rr, its right-memory at 0;
4. [max{0, t −M(S1, d1).ll}, t] ∈Sl and [0, min{M(S2, 0).rr, d(S2)}] ∈S2, i.e., S1 has an event
occupying the temporal segment deﬁned by M(S1, d1).ll, its lef-memory at d1 and, similarly, S2
has an event occupying the temporal segment deﬁned by M(S2, 0).rr, its right-memory at 0;
Tese four cases correspond to the four if statements in Algorithm 3 at lines 18, 31, 33, and 35 respectively.
Case 1.
Te space delimited by the memories of S1 and S2 does not contain any event. Te question is
to decide whether an event should be created, based on the values of the memories of S1 and S2.
If the memories of S1 and S2 are identical, i.e., ll = rl and lr = rr, then we add the event
e = [max{0, d1 −ll}, min{d1 + d2, d1 + rr}].
11


## Page 12


We add this event, regardless of its duration, even if it is very small, i.e., ll +rr < ε, because such an short
event was present at some point, before S1 and S2 were obtained by splitting a longer sequence. We must
add this event to ensure that Property (P1) is not violated. See Figure 10.
On the contrary, if the memories of S1 and S2 diﬀer, the choice will depend on the values stored in
the memories of S1 and S2. Tere are several cases to consider:
If ll = 0 or rr = 0, we do nothing, as no events are recorded around the concatenation position.
Otherwise, that is when ll > 0 and rr > 0, we know that S1 (resp. S2) had originally an event containing
position d(S1) (resp. 0), which disappeared afer a split operation. We will create an additional event
e = [max{0, d1 −ll}, min{d1 + s2, d1 + rr}],
if d(e) = min{d1 + d2, d1 + rr} −max{0, d1 −ll} ≥ε, to avoid creating a residual.
Case 2.
Te space delimited by the memories of S1 and S2 contains an event e starting at the onset of
S2. Te question is whether e should start earlier, i.e., “in S1”, depending on the memories of S1 and S2.
In this case, we start e at
e−= max{0, d1 −ll},
another option is to set
e−= max{0, d1 −ll, d1 −rl}.
In the second option, the algorithm will try to create an attack for the corresponding note based on
the memory of S2. Both options are equally valid, the intuition is that favoring the memory of the lef
sequence tends to preserve temporal deviations in attacks as they appear in the lef sequence. Conversely,
favoring the memory of the right sequence tends to replicate deviations of attacks as they appear in the
right sequence.
Case 3.
Te space delimited by the memories of S1 and S2 contains an event e ending at the end of S1.
Te question is whether e should end later, “in S2”, depending on the memories of S1 and S2.
One possible implementation is to systematically end e at
e+ = min{d1 + d2, d1 + rr}.
Another option is to start the event at
e+ = min{d1 + d2, d1 + rr, d1 + lr}.
Here again, both options are equally valid. Te intuition is that favoring the memory of the lef (resp.
right) sequence tends to preserve temporal deviations in note durations as they appear in the lef (resp.
right) sequence.
Case 4.
Te space delimited by the memories of S1 and S2 contains an event ending at the end of S1
and another event starting at the onset of S2. In this case, if lr > 0 and rl > 0, we merge the two events
in a single one, otherwise, we do nothing.
12


## Page 13


Algorithm 3 Concatenates S1 and S2.
1: procedure Concat(S, t)
▷m is the integer such that d(S) = mδ
2:
d1 ←d(S1) and d2 ←d(S2)
3:
S ←empty sequence with d(S) = d1 + d2
4:
for i = 0, . . . , m do
▷Copies memory from S1 and S2, except at d1
5:
if iδ < d1 then M(S, iδ) ←M(S1, iδ)
6:
if iδ > d1 then M(S, iδ) ←M(S2, iδ −d1)
7:
M(S, d1).ll ←M(S1, d1).ll
▷ll at the end of S1
8:
M(S, d1).lr ←M(S1, d1).lr
▷lr at the end of S1
9:
M(S, d1).rl ←M(S2, 0).rl
▷rl at the start of S2
10:
M(S, d1).rr ←M(S2, 0).rr)
▷rr at the start of S2
11:
for e ∈S1 s.t. e+ < d1 do
▷events ending before d1 are added
12:
add e to S
13:
for e ∈S2 s.t. e−> 0 do
▷events starting afer d1 are added
14:
add event (e−+ d1, e+ + d1) to S
15:
(ll, lr), (rl, rr) ←M(S, d1)
▷shortcut notations
16:
P1 ←S1 is empty or S1[−1]+ ≤d1 −ll
▷S1[−1] denotes the last event in S1
17:
P2 ←S2 is empty or S2[0]+ ≥rr
▷S2[0] denotes the ﬁrst event in S1
18:
if P1 and P2 then
19:
if ll = rl and lr = rr and ll > 0 then
▷same as initial situation for S1 and S2
20:
add [max{0, d1 −ll}, min{d1 + d2, d1 + rr}] to S
▷restore memory, regardless of ε
21:
else
22:
if ll = 0 and rr = 0 then
23:
do nothing
▷no memory to consider
24:
else if ll = 0 and rr > 0 and rl = 0 then
25:
add e = [d1, min{d1 + d2, d1 + rr}] to S
▷e ∈S2 was not created by splitting
26:
else if rr = 0 and ll > 0 and lr = 0 then
27:
add e = [max{0, d1 −ll}, d1] to S
▷e ∈S1 was not create by splitting
28:
else
▷ambiguous case
29:
if min{d1 + d2, d1 + rr} −max{0, d1 −ll} ≥ε then
30:
add e = [max{0, d1 −ll}, min{d1 + d2, d1 + rr}] to S ▷add e if not residual
31:
else if P1 and not P2 then
32:
add [max{0, d1 −ll}, d1 + S2[0]+] to S
▷extend S2[0] in the past (starts before d1)
33:
else if not P1 and P2 then
34:
add [S1[0]−, min{d1 + d2, d1 + rr}] to S
▷extend S1[−1] in the future (ends afer d1)
35:
else
36:
if lr > 0 and rl > 0 then
37:
add [S1[−1]−, d1 + S2[0]+] to S
▷merge S1[−1] and S2[0]
38:
else
39:
add S1[−1] to S
▷add both S1[−1] and S2[0]
40:
add [d1 + S2[0]−, d1 + S2[0]+] to S
return S
13


## Page 14


Figure 10: Splitting a sequence S as t = 10 with a residual at t. Te resulting sequences S1 and S2 are
empty, but memorize the residual (lightgray hatched boxes). When concatenating them, Algorithm 3 will
recreate the residual.
4.3
Te Model Satisﬁes Properties (P1) and (P2)
Properties (P1) and (P2) respectively ensure that the model enables temporal sequence editing without
creating undesired residuals and with the guaranty that editing is non-destructive. Terefore the model
naturally provides an undo mechanism: if two sequences that originally formed a single sequence are
concatenated together in their original position, this will result in the original sequence. But this undo
mechanism is more general as even if the two sequences were used for other intermediate edit operations,
it will always be possible to recreate the initial sequence. Tis, combined with the possibility to copy
sequences, gives rise to powerful sequence edition tools. Tis is illustrated on Midi streams in Section4.5.
Te model relies on a memory structure computed at each segmentation position. Tis memory con-
sists of two memory cells, representing the lef-hand and right-hand sides of the sequence at the speciﬁed
position. Te essential invariant in the implementation of the split and concat primitives is that
• the lef-hand side memory of a sequence at its end position is never modiﬁed and
• the right-hand side memory of a sequence at position 0 is never modiﬁed.
Terefore, arbitrary editing the sequence never leads to any information loss, as the model always remem-
bers information about the initial state of a sequence at its starting and end positions. Tis is what makes
it possible to satisfy Properties (P1) and (P2).
We will not fully demonstrate that the model satisﬁes Properties (P1) and (P2). From the description
of Algorithms 2 and 3, it is clear that Property (P2) on residuals is satisﬁed, with the subtle case discussed
in the ﬁfh case of Algorithm 3 (see Section 4.2.3). Te Property (P1) on reversibility is easily checked
in most cases. Te only tricky case is when residuals are present in the edited sequences. A full proof
requires reviewing all possible conﬁgurations, which would be too long. However, the discussion in Sec-
tion 4.2.3 covers the most diﬃcult case of split residuals which need to be recreated when concatenating
two sequences that were originally forming a single sequence.
4.4
Extending the Model
Te model may be extended easily to handle additional musical information. A ﬁrst extension is to asso-
ciate each event in a sequence to some metadata. In the case of Midi ﬁles, it is natural to store the velocity
and the channel of a note-on event with the corresponding event. Tis is straightforward to implement by
14


## Page 15


storing the metadata in the memory cells computed by Algorithms 1, and by associating the best metadata
to newly created events in Algorithms 2 and 3.
Technically, each event e is associated to a value v(e), which may represent any metadata. A time
event e is therefore a 3-tuple [e−, e+, v(e)]. Te only modiﬁcations to the algorithms are:
1. in Algorithm 1, each memory cell is a 3-tuple, e.g., the lef memory cell for event e is [ll, lr, v];
2. in Algorithm 2, in line 12, we add event [e−−t, e+ −t, v(e)] instead of simply [e−−t, e+ −t],
similarly in line 16, we add [e−, t, v(e)] and in line 18, we add [0, e+ −t, v(e)];
3. in Algorithm 3, events receive the value stored in the corresponding memory; when we merge two
events, we systematically chose to keep the metadata associated to the lef event. Tis decision is
arbitrary and we could decide otherwise, e.g., use the memory of the right sequence, compute an
“average” value.
In our model, residuals are deﬁned by an absolute threshold duration ε. It is also natural to use a
relative deﬁnition for residuals. For instance, when splitting a sequence at position t, if an event e is
such that e−= t −a and e+ = t + b with b ≫a > ε, depending on the musical context, one may
want to dismiss the part of e occurring before t (or length a), although it is not a residual in the absolute
sense as a > ε. A typical case is a measure containing a long, whole note starting slightly before the bar
line. When splitting at the bar line, the head of the note should be removed, as it obviously belongs to
the measure starting at t, not to the measure ending at t. It is quite easy to extend the model to handle
relative residuals, although it makes Algorithms 2 and 3 a bit longer, which is why it is not reported here.
Technically, the head (or tail) of a split event is considered a residual if its duration is shorter than ε
or if it is shorter than a certain ratio of the length the whole event. Typical values for the ratio range from
1/10 (a fragment shorter than a third of the original event is considered too small to exist on its own) to
1/3. Tis modiﬁcation leads to a slight increase in the complexity of Algorithms 2 and 3 to ensure that the
model still satisﬁes Properties (P1) and (P2).
4.5
Using the Model on Actual Music Performance
As we said in Section 4, the model handles sequences of non-overlapping events, and as such is not directly
applicable to Midi ﬁles. However, in a Midi ﬁle, for a given Midi pitch and a given Midi channel, the
successive note-on and note-oﬀevents form a sequence of non-overlapping time intervals. Terefore,
the model is applicable to Midi ﬁles if we treat each note (ﬁxed pitch and channel) individually. Te
targeted use of the model is to edit a Midi ﬁle capturing a musical performance, and therefore with non-
quantized note events, but recorded with a speciﬁed tempo. Te tempo may change during the piece, but
we will consider it ﬁxed here for the sake of clarity. Te model is well-adapted to edit such Midi ﬁles
with segmentation points set as a fraction of the meter, e.g., one beat, one bar, half-a-beat. Te split and
concat primitives were implemented with this application in mind. Te way we use the memory when
concatenating sequences is to ensure that temporal deviations from the metrical structure of the music are
preserved as much as possible, without creating disturbing residuals, and with the ﬂexibility of a powerful
undo mechanism.
We describe here applications of our model to two real world examples.
4.5.1
Transforming a 4/4 into a 3/4 Music Piece
Consider the piano roll in Figure 11, which shows eight measures of a Midi capture of a piano performance
by French pianist Lionel Gaget, in the style of American pianist Chick Corea. Te time signature of this
15


## Page 16


Figure 11: A piano roll showing ﬁrst eight measures of a Midi capture of a piano performance, in the style
of American jazz pianist Chick Corea.
Figure 12: A raw edit of the Midi shown in Figure 11 obtained by removing the fourth beat of every measure,
resulting in a version with a 3/4 time signature with many musical issues (in red boxes): some long notes
are split, residuals are present, note velocities are inconsistent, and many notes are quantized.
piece is 4/4. We aim at producing a 3/4 version of this piece by removing the last beat of every measure.
We created two versions: Figure 12 shows a piano roll of the resulting Midi stream when performing raw
edits and Figure 13 shows the resulting music when performing edits with our model.
Te version in Figure 12 exhibits many musical issues that make it necessary to manually edit the
resulting piano roll to preserve the groove of the original music. Here is a list of some of these issues:
• Split long notes, such as the B2 between measures 2 and 3;
• Residuals: A2 beginning of m. 4, B2 beginning of m. 5, loud E3 at end of m. 5, etc.
• Quantized notes: heads of B1 and F♯3 beginning of m. 2, tails of E1 and B1 at end of m. 6, etc.
• Inconsistent velocities: the velocity of the split B2 changes between m. 2 and m. 3.
Te piano roll in Figure 13, on the other hand, does not have any of the issues of the raw edit version,
and, as a result, sounds more natural and preserves the style of original music more convincingly.
4.5.2
Harmonization
Recent progress in Artiﬁcial Intelligence have led to powerful music generation systems, especially in the
symbolic domain [2]. Computers have become extremely eﬃcient at creating brief musical fragments in
many styles [12, 5], but no algorithm has yet captured the art of spontaneously arranging musical material
into longer convincing structures, such as songs. For instance, in the composition process using Flow-
Machines [8], human musicians are in charge of selecting and organizing musical material sugested by
16


## Page 17


Figure 13: A Dancing Midi edit of the Midi shown in Figure 11 obtained by removing the fourth beat of
every measure, resulting in a version with a 3/4 time signature with none of the musical issues mentioned
(compare white boxes here with red boxes in Figure 12). Many notes are held across segmentation points,
creating a smoother musical output.
Figure 14: Te harmonization of “Autumn Leaves” as written in the lead sheet from measure 20 to measure
33. Te list of chords visible on the ﬁgure is Gm (measures 20-21), Cm7, F7, B♭maj7 (mm. 24-25), Am7/♭5,
D7/9, Gm7, F♯7, Fm7, E7, E♭maj7, D7/♭9, and Gm (mm. 32-33) using a jazz notation for chord symbols, in
a default voicing.
the computer to create large-scale structures conveying a sense of direction. Tese new ways of making
music highlight the need for powerful tools to edit musical material.
One of the main strength of the Midi format is that it enables musical transformations, such as pitch-
shifing (or transposition) and time-stretching, with no loss of quality. Te model is naturally compatible
with transpositions because the memory cells do not depend on the actual pitch of a note. Tis can be il-
lustrated by integrating our model within any generative algorithm. As an illustration, we have developed
a system that produces harmonizations for a given target Midi ﬁle in the style of a source Midi ﬁle. Te
harmonizer outputs a new Midi ﬁle with the same duration as the target ﬁle, created by editing the source
ﬁle, using split and concat combined with chromatic transpositions, in such a way that the output ﬁle’s
harmony matches that of the target Midi ﬁle. Te harmonizer uses Dynamic Programming [1] or similar
techniques, such as Belief Propagation [7], to produce a ﬁle that optimizes the harmonic similarity with
the target ﬁle and, at the same time, minimizes the edits in the source ﬁle, to preserve the style of the
source as much as possible. We do not fully describe the harmonizer in this article [10].
Figures 15-16 show piano rolls obtained by harmonizing 14 measures of “Autumn Leaves” (see Figure 14)
using a Midi capture of a piano performance of an intermezzo by Johannes Brahms. Te raw edit in
Figures 15 exhibits the same type of artifacts as Figure 12. Long notes are split at each segmentation
17


## Page 18


Figure 15: Harmonization of the 14 measures of “Autumn Leaves” shown in Figure 14 in the style of a piano
performance of an intermeeezo by Johannes Brahms and using raw Midi edits. Te actual harmony is
visible in the background (light green notes). Musical inconsistencies are indicated by red boxes.
Figure 16: Te same harmonization as in Figure 15 except all edits are performed with the model. Tis
piano-roll has none of the musical issues of the piano roll in Figure 15.
point (here, every beat), which creates dissonant chords at measures 24-25. More generally, the style of
the resulting Midi ﬁle is substantially diﬀerent from that of the original source. Te source contains
numerous long-held notes and most chords are arpegiated. In the Midi ﬁle on Figures 15 long-held notes
are broken at every beat, making most chords non-arpegiated (notes are played all together). Many
residuals are introduced, and some of them make up chords (red boxes in measure 23 and 31) that sound
wrong. On the contrary, Figure 16 shows a much cleaner result, with none of these musical issues.
5
Conclusion
We have presented a model for editing non-quantized, metrical musical sequences represented as Midi
ﬁles. We ﬁrst listed a number of problems caused by the use of naive edition operations applied to per-
formance data, using a motivating example. We then introduced a model, called Dancing Midi based
on 1) two desirable, well-deﬁned properties for edit operations and 2) two well-deﬁned operations, split
and concat, with an implementation. We showed that our model formally satisﬁes the two properties,
and that our model does not create most of the problems that occur with naive edit operations on our
motivating example, as well as on a real-world example using an automatic harmonizer. Our approach has
limitations. First, the model requires two parameters (ε and the relative ratio), which have to be set by
18


## Page 19


the user. Assigning these parameters to 0.15 beats and 20% respectively turned out to work well for most
music we had to deal with. However, there are cases where these parameters should be tuned, especially
for non typical music (e.g. extreme tempos or very dense). More generally, the model is monophonic by
nature, so it does not make any inference on groups of notes (e.g. chords). Tis may produce, in rare cases,
strange behavior (like treating one note of a chord diﬀerently than others).
However the reversibility of the operations (no undo mechanism is required by construction) and the
light weight nature of the model (complexity is linear in the number of segmentation points) makes it
worth using in many cases as it clearly improves on naive editing.
acknowledgement
We thank Jonathan Donier for fruitful remarks and comments.
References
[1] Bellman, R. Dynamic Programming, 1 ed. Princeton University Press, Princeton, NJ, USA, 1957.
[2] Briot, J.-P., Hadjeres, G., and Pachet, F. Deep learning techniques for music generation-a survey.
arXiv preprint arXiv:1709.01620 (2017).
[3] Briot, J.-P., and Pachet, F. Deep learning for music generation: challenges and directions. Neural
Computing and Applications (2018), 1–13.
[4] Dannenberg, R. B. Music Representation Issues, Techniques, and Systems. Computer Music Journal
17, 3 (1993), 20–30.
[5] Hadjeres, G., Pachet, F., and Nielsen, F. DeepBach: a Steerable Model for Bach Chorales Gener-
ation. In International Conference on Machine Learning (2017), pp. 1362–1371.
[6] Knuth, D. E. Dancing links. eprint arXiv:cs/0011047 (Nov. 2000).
[7] Papadopoulos, A., Pachet, F., Roy, P., and Sakellariou, J. Exact sampling for regular and
markov constraints with belief propagation.
In Principles and Practice of Constraint Programming
(Cham, 2015), G. Pesant, Ed., Springer International Publishing, pp. 341–350.
[8] Papadopoulos, A., Roy, P., and Pachet, F. Assisted Lead Sheet Composition Using FlowCom-
poser. In Principles and Practice of Constraint Programming (Cham, 2016), M. Rueher, Ed., Springer
International Publishing, pp. 769–785.
[9] Raffel, C. Te lakh midi dataset v0.1, 2016.
[10] Roy, P., Pachet, F., and Carr´e, B. Te MIDI Harmonizer. eprint arXiv:to-appear (Nov. 2018).
[11] Tesler, L. A Personal History of Modeless Text Editing and Cut/Copy-Paste. interactions 19, 4 (July
2012), 70–75.
[12] Van Den Oord, A., Dieleman, S., Zen, H., Simonyan, K., Vinyals, O., Graves, A., Kalchbren-
ner, N., Senior, A., and Kavukcuoglu, K. WaveNet: A Generative Model for Raw Audio. arXiv
preprint arXiv:1609.03499 (2016).
19


## Page 20


[13] Whittaker, S., and Amento, B. Semantic speech editing. In Proceedings of the SIGCHI conference on
Human factors in computing systems (2004), ACM, pp. 527–534.
20

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1903_08459v1_smart_edition_of_midi_files
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1903_08459V1_SMART_EDITION_OF_MIDI_FILES.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

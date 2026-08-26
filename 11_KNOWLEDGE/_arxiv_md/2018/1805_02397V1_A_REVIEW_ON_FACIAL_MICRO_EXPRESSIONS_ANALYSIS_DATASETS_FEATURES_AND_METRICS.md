---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1805.02397v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1805.02397v1_A_Review_on_Facial_Micro-Expressions_Analysis__Datasets__Features_and_Metrics

> Source: 1805.02397v1_A_Review_on_Facial_Micro-Expressions_Analysis__Datasets__Features_and_Metrics.pdf

> Pages: 19

---


## Page 1


PREPRINT SUBMITTED TO IEEE JOURNAL.
1
A Review on Facial Micro-Expressions Analysis:
Datasets, Features and Metrics
Walied Merghani, Adrian K. Davison, Member, IEEE, Moi Hoon Yap, Member, IEEE
(This work has been submitted to the IEEE for possible publication. Copyright may be transferred without
notice, after which this version may no longer be accessible).
Abstract—Facial micro-expressions are very brief, spontaneous facial expressions that appear on the face of humans when they either
deliberately or unconsciously conceal an emotion. Micro-expression has shorter duration than macro-expression, which makes it more
challenging for human and machine. Over the past ten years, automatic micro-expressions recognition has attracted increasing
attention from researchers in psychology, computer science, security, neuroscience and other related disciplines. The aim of this paper
is to provide the insights of automatic micro-expressions analysis and recommendations for future research. There has been a lot of
datasets released over the last decade that facilitated the rapid growth in this ﬁeld. However, comparison across different datasets is
difﬁcult due to the inconsistency in experiment protocol, features used and evaluation methods. To address these issues, we review the
datasets, features and the performance metrics deployed in the literature. Relevant challenges such as the spatial temporal settings
during data collection, emotional classes versus objective classes in data labelling, face regions in data analysis, standardisation of
metrics and the requirements for real-world implementation are discussed. We conclude by proposing some promising future directions
to advancing micro-expressions research.
Index Terms—Facial micro-expressions, micro-expressions recognition, micro-movements detection, feature extraction, deep learning.
!
1
INTRODUCTION
F
ACIAL expression research has a long history and accel-
erated through the 1970s. The modern theory on basic
emotions by Ekman et al [1], [2], [3] has generated more re-
search than any other in the psychology of emotion [4]. They
outline 7 universal facial expressions: happy, sad, anger,
fear, surprise, disgust and contempt, as the universality of
emotion. When an emotional episode is triggered, there is an
impulse which may induce one or more of these expressions
of emotion.
Facial micro-expression (henceforth, micro-expression)
analysis has become an active research area in recent years.
Micro-expressions occur when a person attempts to conceal
their true emotion [2], [5]. When they consciously realise
that a facial expression is occurring, the person may try to
suppress the facial expression because showing the emotion
may not be appropriate or could be due to a cultural display
rule [6]. Once the suppression has occurred, the person may
mask over the original facial expression and cause a micro-
expression. In a high-stakes environment, these expressions
tend to become more likely as there is more risk to showing
the emotion.
Micro-expressions contain a signiﬁcant and effective
amount of information about the true emotions which may
be useful in practical applications such as security and inter-
rogations [7], [8], [9]. It is not easy to extract this information
•
W. Merghani is with Sudan University of Science and Technology
•
A. K. Davison was with Manchester Metropolitan University during this
study and is now with the University of Manchester.
•
M. H. Yap is with the School of Computing, Mathematics and Digital
Technology, Manchester Metropolitan University, Manchester, United
Kingdom. E-mail: m.yap@mmu.ac.uk
due to the brief movements in micro-expressions, where
there is a need for the features to be more descriptive. The
difﬁculty also comes from one of the main characteristics
of micro-expressions which is the short duration, with the
general standard being a duration of no more than 500
ms [10]. Other deﬁnitions of speed that have been studied
show micro-expressions to last less than 250 ms [11], less
than 330 ms [3] and less than half a second [8]. Following
Ekman and Friesen as ﬁrst to deﬁne a micro-expression [12],
a usual duration considered is less than 200 ms. Duration
is the main feature that distinguishing micro-expressions
from macro-facial expressions
[13], which make it more
challenging than micro-expressions in the following aspects:
•
Difﬁculties for human to spot micro-expressions: Hu-
mans ﬁnd it difﬁcult to spot micro-expressions con-
sistently [8]. This is due to macro-expressions tend to
be large and distinct, whereas micro-expressions are
very quick and subtle muscle movements.
•
Datasets Creation: It is difﬁcult to induce micro-
expressions if compared to macro-expressions. Cur-
rent available micro-expression datasets were in-
duced
in
a
laboratory
controlled
environment.
Macro-expressions can be recorded by normal cam-
era. However, the speed and subtlety of micro-
expressions require high-speed camera, where this
digital capture device produces more noisy data than
the normal camera.
•
The
history
of
algorithm
development:
Auto-
mated micro-expression recognition is relatively new
(found work in 2009 [14]), when compared with
facial expression recognition (found in 1990s [15],
arXiv:1805.02397v1  [cs.CV]  7 May 2018


## Page 2


PREPRINT SUBMITTED TO IEEE JOURNAL.
2
[16]).
Although both micro and macro-expressions loosely re-
lated due to the facial expression aspect, these two topics
should be looked upon as different research problems. Our
focus is to provide comprehensive review and new insights
for micro-expressions. For review in macro-expressions,
please refer to [17], [18].
This paper introduces and surveys recent research ad-
vances of micro-expressions. We present a comprehensive
review and comparison on the datasets, the state-of-the-
art features for micro-expression recognition and the per-
formance metrics. We demonstrate the potential and chal-
lenges of micro-expression analysis. This rest of the paper
is organised as follows: Section 2 provides a review on
publicly available datasets. Section 3 presents the feature
representation. Detailed performance metrics used in this
ﬁeld are shown in Section 4 and Section 5 outlines chal-
lenges and Section 6 concludes this paper by providing
future recommendations.
2
FACIAL MICRO-EXPRESSION DATASETS
This section will compare and contrast the relevant publicly
available datasets for facial micro-expressions analysis.
2.1
Non-spontaneous datasets
The
earlier
research
dependent
on
non-spontaneous
datasets. Here we present a review on the three earliest non-
spontaneous datasets.
2.1.1
Polikovsky Dataset
One of the ﬁrst micro-expression datasets was created by Po-
likovsky et al. [14]. The participants were 10 university stu-
dents in a laboratory setting and their faces were recorded at
200fps with a resolution of 640×480. The demographic was
reasonably spread but limited in number with 5 Asians, 4
Caucasians and 1 Indian student participants.
The laboratory setting was set up to maximise the focus
on the face, and followed the recommendations of mugshot
best practices by McCabe [19]. To reduce shadowing, lights
were placed above, to the left and right of the participant.
The background consisted of a uniform colour of approxi-
mately 18% grey. The camera was also rotated 90 degrees to
increase the pixels available for face acquisition.
The micro-expressions in this dataset were posed by par-
ticipants whom were asked to perform the 7 basic emotions
with low muscle intensity and moving back to neutral as
fast as possible. Posed facial expressions have been found to
have signiﬁcant differences to spontaneous expressions [20],
therefore the micro-expressions in this dataset are not rep-
resentative of natural human behaviour and highlights the
requirement for expressions induced naturally. Further, this
dataset is not publicly available for further study.
2.1.2
USF-HD
Similar to the previous dataset, USF-HD [21] includes 100
posed micro-expressions recorded at 29.7 fps. The partic-
ipants were shown various micro-expressions and told to
replicate them in any order of preferencethey ed. As with the
Polikovly described dataset, posed not re-create a real-world
scenario and replicating other people’s micro-expressions
does not represent how these movements would be pre-
sented by the participants themselves.
Recording at almost 30 fps can risk losing important
information about the movements. In addition, this dataset
deﬁned micro-expressions as no higher than 660 ms, which
is longer than the previously accepted deﬁnitions. Moreover,
the categories for micro-expressions are smile, surprise,
anger and sad, which is reduced from the 7 universal
expressions by missing out disgust, fear and contempt. This
dataset has also not been made available for public research
use.
2.1.3
YorkDDT
As part of a psychological study named the York Deception
Detection Test (YorkDDT), Warren et al.
[22] recorded 20
video clips, at 320×240 resolution and 25 fps, where par-
ticipants truthfully or deceptively described two ﬁlm clips
that were either classed as emotional, or non-emotional.
The emotional clip, intended to be stressful, was of an
unpleasant surgical operation. The non-emotional clip was
meant to be neutral, showing a pleasant landscape scene.
The participants viewing the emotional clip were asked
to describe the non-emotional video, and vice versa for
the participants watching the non-emotional clip. Warren
et al. [22] reported that some micro-expressions occurred
during both scenarios, however these movements were not
reported to be available for public use.
During their study into micro-expression recognition,
Pﬁster et al. [23] managed to obtain the original scenario
videos where 9 participants (3 male and 6 female) displayed
micro-expressions. They extracted 18 micro-expressions for
analysis, 7 from the emotional scenario and 11 from the non-
emotional version.
Other than the very low amount of micro-expressions
in this dataset, it is created through a second source that do
not go into a large amount of detail about AU, or participant
demographic. With the data unable to be publicly accessed,
it is not possible to study these micro-expressions. It is also
an issue with the frame rate being so low, the largest amount
of frames for analysis would be around 12-13 frames. The
lowest reported micro-expression length was 7 frames.
2.2
Spontaneous datasets
Developing micro-expression spontaneous datasets is one
of the biggest challenges faced in this research area. It is
difﬁcult to elicit micro-expressions because they are difﬁcult
to fake, so we need to get the true emotion while the person
try to hide it. Some spontaneous datasets to date include:
SMIC [24], CASME [25], CASME II [26], SAMM [27] and
CAS(ME)2 [28]. SAMM was designed for micro-movements
with less emphasis on the emotional side for increased
objectiveness. Available datasets will be described in this
section.
2.2.1
Chinese Academy of Sciences Micro-Expressions
(CASME)
Yan et al. [25] created a spontaneous micro-expression
dataset called CASME. The dataset contains 195 samples
of micro-expressions with a frame rate of 60 fps. These 195


## Page 3


PREPRINT SUBMITTED TO IEEE JOURNAL.
3
Fig. 1. Sample of HS SMIC dataset with negative expression.
Fig. 2. Sample of CASME II dataset with happiness expression, the participant has been FACS coded with AU1+AU12 (Inner brow raiser+lip corner
puller).
Fig. 3. Sample of SAMM dataset with anger expression, the participant has been FACS coded with AU4+AU7 (Brow lowerer+lid tightener).
samples were selected from more than 1500 facial move-
ments, where 35 participants (13 females, 22 males) took
part. The clips were divided into two classes depending on
the environmental setting and cameras used.
2.2.1.1
Class A: Samples in this class recorded by
BenQ M31 camera at 60 fps, and the resolution is set to
1280×720 pixels. Natural light was used for recording.
2.2.1.2
Class B: A GRAS-03K2C camera recording
at 60 fps was used to record samples in this class with
resolution set to 640×480 pixels. For class B two LED lights
have been used.
Table 1 shows each emotion class and the frequencies at
which they occur in the CASME(A and B) dataset.
TABLE 1
The frequency occurance of each emotion category in the CASME
dataset
Emotion
Frequency
Amusement
5
Sadness
6
Disgust
88
Surprise
20
Contempt
3
Fear
2
Repression
40
Tense
28
2.2.2
Spontaneous Micro-expression Corpus (SMIC)
Li et al. [24] built the SMIC dataset, which was recorded in
an indoor environment with four lights from the four upper
corners of the room. To induce strong emotions 16 movie
clips were selected and shown to participants on a computer
monitor. Facial expressions have been gathered using a cam-
era ﬁxed on the top of monitor while participants watched
movie clips.
The dataset is spontaneous, 20 participants (6 females
and 14 males) participated in the experiment. A high speed
(HS) camera set to 100 fps and resolution of 640×480 was
used to gather the expressions from the ﬁrst ten participants.


## Page 4


PREPRINT SUBMITTED TO IEEE JOURNAL.
4
TABLE 2
Type of Emotions Frequency in SMIC [24]
Dataset
positive
negative
surprise
total
HS
51
70
43
164
VIS
28
23
20
71
NIR
28
23
20
71
A sample from this HS dataset is shown in Fig. 1. A normal
visual camera (VIS) and near-infrared (NIR), both with 25
fps and resolution of 640×480, were used for all 20 partici-
pants. The lower frame rates of the latter two cameras can
help to check whether the current method can be effective
at this speed.
The accepted duration of micro-expression for SMIC
is 1/2 second. Since not every participant showed micro-
expressions when recording SMIC the ﬁnal dataset includes
164 micro-expression clips from 16 participants recorded in
HS dataset. While VIS and NIR datasets include 71 clips
from 8 participants. Emotions in SMIC were classiﬁed into
3 classes (positive, negative and surprise). Table 2 show the
number of emotions in any class according to the type of
dataset.
2.2.3
Chinese Academy of Sciences Micro-Expression II
(CASME II)
CASME II has been developed by Yan et al. [26], which
succeeds the CASME dataset [25] with major improvements.
All samples in CASME II are spontaneous and dynamic
micro-expressions with high frame rate (200 fps). There is
always a few frames kept before and after each micro-
expressions, to make it suitable for detection experiments,
however the amount of these frames can vary across clips.
The resolution of samples is 640×480 pixels for recording,
which were saved as MJPEG with a resolution of around
280×340 pixels for the cropped facial area. Fig. 2 shows
a sample from the CASME II with a happiness-class ex-
pression. The micro-expressions were elicited in a well-
controlled laboratory environment. The dataset contains 247
micro-expressions (gathered from 35 participants) that were
selected from nearly 3000 facial movements and have been
labeled with action units (AUs) based on the Facial Action
Coding System (FACS) [29]. Lighting ﬂickers were avoided
in the recordings and highlights to the regions of the face
have been reduced.
TABLE 3
The frequency of each micro-expression class in the CASME II dataset.
Emotion
Frequency
Happiness
33
Disgust
60
Surprise
25
Repression
27
Others
102
2.2.4
Spontaneous Actions and Micro-Movements (SAMM)
The Spontaneous Actions and Micro-Movements (SAMM)
[27] dataset is the ﬁrst high-resolution dataset of 159 micro-
movements induced spontaneously with the largest vari-
ability in demographics. The inducement procedure was
based on the 7 basic emotions [2] and recorded at 200 fps.
An example from the SAMM dataset can be seen in Fig.
3. As part of the experimental design, each video stimuli
was tailored to each participant, rather than getting self-
reports after the experiment. This allowed for particular
videos to be chosen and shown to participants for optimal
inducement potential. The experiment comprised of 7 stim-
uli used to induce emotion in the participants who were told
to suppress their emotions so that micro-movements might
occur. To increase the chance of this happening, a prize of 50
was offered to the participant that could hide their emotion
the best, therefore introducing a high-stakes situation [2],
[5]. Each participant completed a questionnaire prior to the
experiment so that the stimuli could be tailored to each in-
dividual to increase the chances of emotional arousal. There
is a total of 159 FACS-coded micro-movements reported in
this dataset.
2.2.5
A Dataset of Spontaneous Macro-Expressions and
Micro-Expressions (CAS(ME)2)
Qu et al. [28] presented a new facial database with macro-
and micro-expressions, which included 250 and 53 sam-
ples respectively selected from more than 600 facial move-
ments. This database has been collected from 22 partici-
pants (6 males and 16 females) with mean age of 22.59
years (standard deviation: 2.2). A Logitech Pro C920 camera
was used to record samples at frame rate equal to 30 fps
and resolution set to 640×480 pixels. CAS(ME)2 has been
labelled using combinations of AUs, self-reports and the
emotion category decided for the emotion-evoking videos.
This database contains four emotion categories: positive,
negative, surprise and other which is shown in Table 4 with
their frequency occurrence.
TABLE 4
Type of emotion and their frequencies in the CAS(ME)2 dataset.
Emotion
Macro-expression
Micro-expression
Positive
87
6
Negative
95
19
Surprise
13
9
Other
55
19
2.3
Dataset comparison
Table 5 shows summary of a comparison of the datasets.
Due to the non-spontaneous datasets were not made avail-
able, it is not been possible to provide a critical review
on those datasets. Overall, CASME II has a high number
of micro-expression samples collected from high number
of participants (35 participants), similar to CASME but
with 195 samples. There is no distribution in ethnicities in
CASME and CASME II, where all participants are Chinese.
SMIC have participants from 3 different ethnicities, but this
limitation was overcome in SAMM which has participants
from 13 different ethnicities. SAMM also has advantage
over the other in age distribution with mean age of 33.24
years (SD: ±11.32). CASME II and SAMM have high frame
rate (200 fps). SAMM is the ﬁrst high-resolution dataset
which set to 2040×1088 pixel and a facial area of 400×400.


## Page 5


PREPRINT SUBMITTED TO IEEE JOURNAL.
5
TABLE 5
A Summary of non-spontaneous and spontaneous datasets.
Dataset
Participants
Resolution
FPS
Samples
Emotion Classes
FACS Coded
Ethnicities
Polikovsky [14]
11
640×480
200
13
7
Yes
3
USF-HD [21]
N/A
720×1280
29.7
100
4
No
N/A
YorkDDT [22]
9
320×240
25
18
N/A
No
N/A
CASME [25]
35
640×480, 1280×720
60
195
7
Yes
1
SMIC [24]
20
640×480
100 and 25
164
3
No
3
CASME II [26]
35
640×480
200
247
5
Yes
1
SAMM [27]
32
2040×1088
200
159
7
Yes
13
CAS(ME)2 [28]
22
640×480
30
250 macro, 53 micro
4
No
1
The CAS(ME)2 has a limited number of micro-expression
samples with just 53 collected. In terms of emotion stimuli
for the participants, CASME and SAMM have 7 classes,
CASME II has 5 classes and SMIC only with 3 classes.
CASME, CASME II and SAMM have been coded using
FACS. Although SAMM was stimulated by 7 emotional
classes, the ﬁnal label in their ﬁrst release for the micro-
movements only consists of FACS codes - but not emotion
classes.
CASME II and SAMM become the focus of the re-
searchers as they equipped with all the criteria needed for
micro-expressions recognition: emotion classes, high frame
rate, a rich number of micro-expressions and varies in term
of the intensity for facial movements.
3
FEATURES
The features used in micro-expression recognition will be
discussed in this section. Figure 4 shows the total number
of publications and its feature types based on our review.
This is a strong evidence to support the growth of micro-
expressions research. It is noted that 3DHOG was used in
earlier work but not as popular as HOOF in recent years.
LBP-TOP gained popularity in 2014 and maintained its
number till today. On the other hand, deep learning is still
in its infancy but we expect this number will grow rapidly
in the future.
The full summary of the feature types, classifers and
metrics used in the past decade is presented on Table 6
for Part I (2009-2015) and Table 7 for Part II (2016-2018).
The detailed algorithms review are categorised into: 3D His-
tograms of Oriented Gradients, Local Binary Pattern-Three
Orthogonal Planes, Histogram of Oriented Optical Flow,
Deep Learning Approaches and Other Feature Extraction
Methods.
3.1
3D Histograms of Oriented Gradients (3DHOG)
Polikovsky et al. [14] presented an approach for facial micro-
expression recognition. They divided face into 12 regions
selected through manual annotation of points on the face
and then a rectangle was centred on these points. 3D-
histograms of oriented gradients (3DHOG) was used to
recognise motion in each region. This approach was eval-
uated on a posed dataset of micro-expressions captured
using a high speed camera (200 fps). 13 different micro-
expressions were recognised in this experiment. Their main
contribution was to measure the duration of three phases
of micro-expressions; constrict of the muscles (Constrict),
muscle construction (In-Action) and release of the muscles
(Release).
Polikovsky and Kameda [30] used 3DHOG again this
time with k-mean classiﬁer and voting procedure. They
proposed a method for detecting and measuring timing
characteristic of micro-expressions. Frame-by-frame classiﬁ-
cation was done to detect AUs in 8 video cube regions. The
Onset frame and Offset have higher accuracy than the Apex
frame, which indicates that their proposed descriptor is
suitable for recognition rather than classiﬁcation for a static
frame. To measure AU timing characteristics, the change of
bin values in the 3D gradient orientation histogram have
been used to reﬂect the changes and motion accelerations
of facial movement. They claimed that this time proﬁle
could be used to identify the distinction between posed and
spontaneous micro-expression.
Different facial regions having different contributions to
micro-expressions as Chen et al. claimed [31] and this being
largely ignored by previous studies. They proposed to used
3DHOG features with weighted method and used fuzzy
classiﬁcation for micro-expression recognition. They eval-
uated their method on 36 samples from CASME II, which
contains 4 emotions at a rate of 9 samples per emotion. They
compared the result with 3DHOG and weighted 3DHOG
and perform better than both achieving average accuracy of
86.67%.
3.2
Local
Binary
Pattern-Three
Orthogonal
Planes
(LBP-TOP) and Variations
Pﬁster et al. [23] proposed a framework for recognising
spontaneous facial micro-expressions. LBP-TOP [49] as a
spatio-temporal local texture descriptor has been used to
extract dynamic features. In classiﬁcation phase, Support
Vector Machine (SVM), Multiple Kernel Learning (MKL)
and Random First (RF) have been used. This framework
was evaluated on earlier version of SMIC where the data
collected from only six participants with 77 sample of micro-
expressions. Temporal Interpolation Model (TIM) has been
used to increase the number of frames to achieve more
statistically stable histograms. The result of SMIC were
compared to York Deception Detection Test (YorkDDT) [22]
which were recorded in 25 fps and resolution 320×240.
Using leave-one-subject-out (LOSO), the method was eval-
uated on two corpora and down-sampled SMIC to 25 fps.
They have two sets to classify between them emotional vs
non-emotional and lie vs truthful. The best result achieved


## Page 6


PREPRINT SUBMITTED TO IEEE JOURNAL.
6
Fig. 4. Illustration of the number of publications in micro-expressions recognition based on feature types over the past 10 years. The total publications
show the growth of research in this area particularly in 2014 with more researchers focused on LBP-TOP. In recent years, more research focused
on HOOF than 3DHOG. Deep learning technique is still in its infancy, but it is expected that the number of publications using deep learning will have
a rapid growth in the future.
on YorkDDT to classify between ﬁrst set is an accuracy of
76.2% using MKL and 10 frames. For the second set, the
best result is 71.5% using MKL 10 frames and same result
using SVM. For SMIC they classify between negative and
positive, the best result is 71.4% using MKL 10 frames and
64.9% using MKL and 15 frames for down-sampled SMIC.
Pﬁster et al. [32] then proposed a method to differentiate
between spontaneous and posed facial expressions (Sponta-
neous Vs Posed (SVP)). They extended Complete Local Bi-
nary Patterns (CLBP) which was proposed by Guo et al. [50]
to work with dynamic texture descriptor and called it CLBP
from Three Orthogonal Planes (CLBP-TOP). They evaluated
their proposed method by leave-one-subject-out on a corpus
developed by them Spontaneous vs POSed (SPOS). This
SPOS provides spontaneous and posed expression for the
same subject in the session. It contains 7 subjects with
84 posed and 147 spontaneous expressions. Two cameras
have been used to record the corpus, one recorded data
from visual (VIS) and the other from near-infrared channel
(NIR). Both of cameras used 640×480 resolution and 25 fps.
SVM, LINEAR classiﬁer (LIN), Multiple Kernel Learning
(MKL) and fusion of SVM, LIN and Random Forest through
majority voting (FUS) have been used as classiﬁers. They
showed that CLBP-TOP overcome LBP-TOP with an accu-
racy of 78.2%, 72% and 80% on NIR, VIS and combination,
respectively.
Li et al. [24] run two experiments on SMIC database
for analysing micro-expressions. The ﬁrst experiment was
to detect micro-expressions occurring and the other was to
then recognise the type of micro-expression. The detection
stage was employed to distinguish a micro-expression and
a normal facial expression. On the other hand, recognition
discriminated three classes of micro-expression (positive,
negative and surprise). A normalisation was done to all
faces, followed by a registration to a face model using 68
feature points from an Active Shape Model [51]. Then the
faces were cropped according to the eye positions that has
been detected using Haar eye detector [52]. LBP-TOP was
used for feature extraction from cropped face sequences.
In the VIS and NIR dataset which has a limited number
of frames, some problems may arise when applying LBP-
TOP. To avoid these problems, TIM was used to allow up-
sampling and down-sampling of the number of frames.
SVM was used as a classiﬁer and leave-one-subject-out cross
validation [53] was used to compute the performance of the
two experiments, which were run on three datasets (HS,
VIS and NIR). The best accuracy for detection of micro-
expressions was 65.55% when evaluating the method on the
HS dataset and the X, Y and T parameters were equal to
5, 5 and 1 respectively for LBP-TOP. For micro-expressions
recognition, the best accuracy is equal to 52.11% on VIS
dataset with X, Y and T having the same value as previous.
Avoiding the problem that may arise because the limitation
regarding the number of frames by using TIM is considered
a strength for this algorithm. However, there is a limitation
in using a limited number of recognition classes, since some
emotion cannot be judged under ambiguous conditions if
more than one expression reported by the participant.
Guo et al. [34] used LBP-TOP features in their micro-
expression recognition experiment. To classify these fea-
tures, they used the nearest neighbour method to compare
the distance between unknown samples with entire known
samples. Euclidean distance has been used as distance mea-
surement. This method was evaluated on SMIC database. In
evaluation, ﬁrstly they used Leave-One-Subject-Out (LOSO)
and Leave-One-Expression-Out (LOEO) and achieved a
recognition accuracy of 53.72% and 65.83% for LOSO
and LOEO respectively. In addition, they have conducted


## Page 7


PREPRINT SUBMITTED TO IEEE JOURNAL.
7
TABLE 6
Summary (Part I: 2009 - 2015) of the feature types, classiﬁer and metrics used over the past decade for micro-expression recognition by year and
authors.
Year
Authors
Datasets
Feature type
Classiﬁer
Metrics (Best Result)
2009
Polikovsky et al. [14]
Polikovsky
3DHOG
K-means
AUs Classiﬁcation
2011
Pﬁster et al. [23]
Earlier version of SMIC
LBP-TOP
SVM, MKL and RF
Accuracy: 71.4% using MKL
2011
Pﬁster et al. [32]
SPOS
CLBP-TOP
SVM, MKL and LINEAR
Accuracy: 80% using MKL
2013
Polikovsky
and Kameda [30]
Polikovsky
3DHOG
K-means
Recognition of 11 AUs
2013
Li et al. [24]
SMIC(HS, VIS and NIR)
LBP-TOP
SVM
Accuracy: 52.11% on VIS
2013
Song et al. [33]
SEMAINE corpus
HOG+HOF
SVR
N/A
2014
Guo et al. [34]
SMIC
LBP-TOP
nearest neighbour
Accuracy: 65.83%
2014
Yan et al. [26]
CASME II
LBP-TOP
SVM
Accuracy: 63.41%
2014
Wang et al. [35]
CASME and CASME II
TICS
SVM
Accuracy: 61.85% on CASME
58.53% on CASME II
2014
Le et al. [36]
CASME II and SMIC
LBP-TOP+STM
AdaBoost
Accuracy: 43.78% on CASME II
44.34% on SMIC
2014
Lu et al. [37]
SMIC, CASME B
and CASME II
DTCM
SVM, RF
Accuracy:82.86% on SMIC, 64.95%
on CASME and 64.19% on CASME II
2014
Liong et al. [38]
CASME II and SMIC
OSW-LBP-TOP
SVM
Accuracy:57.54% on SMIC
66.40% on CASME II
2014
Wang et al. [39]
CASME
DTSA
ELM
Accuracy: 46.90%
2014
Davison et al. [40]
CASME II
LBP-TOP+GDs
RF, SVM
92.6 % when RF used
2015
House and Meyer [41]
SMIC
LGCP-TOP
SVM
Accuracy 48.1%
2015
Wang et al. [42]
CAMSE II and SMIC
LBP-SIP and LBP-MOP
SVM
Accuracy:66.8% on CASME
using LBP-MOP
2015
Wang et al. [43]
CASME and CASME II
TICS, CIELuv and CIELab
SVM
Accuracy:61.86% on CASME
62.30% on CASME II
2015
Le et al. [44]
CASME II
DMDSP+LBP-TOP
SVM, LDA
F1-score: 0.52
2015
Huang et al. [45]
CASME II and SMIC
STLBP-IP
SVM
Accuracy:59.51% on CASME II
57.93% on SMIC
2015
Liu et al. [46]
SMIC, CASME
and CASME II
MDMO
SVM
Accuracy:68.86% on CASME
67.37% on CASME II and 80% on SMIC
2015
Li et al. [47]
CASME II and SMIC
LBP, HOG and HIGO
LSVM
Accuracy:57.49% on CASME II
53.52% on SMIC
2015
Kamarol et al. [48]
CASME II
STTM
SVM one-against-one
Accuracy:91.71%
experiments for different values of LBP-TOP parameters
(RX, RY , RT , PX, PY , PT ) which refer to the radii in axis X,
Y and T, and the number of neighbourhood points in the XY,
XT and YT planes respectively. The best result was achieved
when they set the value to (1,1,2,8,8,8) for parameters. A
different distribution of training set and testing set also have
been tested and the best result of 63% was achieved when
portion of training and testing data with a 5:1 split.
Yan et al. [26] carried out a micro-expression recognition
experiments on clips from the CASME II dataset, developed
by the same authors. LBP-TOP was used in this experiment
to extract the features. SVM was employed as the classiﬁer.
With radii varying from 1 to 4 for X and Y, and from 2 to 4
for T (they do not consider T=1 due to little change between
two neighbouring frames on a sample rate of 200 fps), and
SVM was used as the classiﬁer which classify between ﬁve
main categories of emotions provided in this experiment
(happiness, disgust, surprise, repression and others). The
best performance is 63.41% shown when the radii are 1, 1
and 4 for XY, YT and XT planes respectively. Developing
high quality datasets with higher temporal (200 fps) and
spatial resolution (about 280×340 pixels on facial area),
and classify 5 categories of expression with performance
63.41% are the advantages of this method, however they
use same method which used for classifying ordinary facial
expressions which may not work well for micro-expressions.
Liong et al. [38] proposed Optical Strain Weighted LBP-
TOP (OSW-LBP-TOP) method which used optical strain fea-
tures for micro-expression recognition. They evaluated this
feature on CASME II and SMIC. They used SVM as classiﬁer
and test different kernel. Their method outperformed the
two baseline methods [24], [26] when evaluated on two
datasets and achieved accuracy of 57.54% on SMIC when
using poly kernel and 66.40% on CASME II when RBF
kernel was used.
Davison et al. [40] developed a method to differentiate
between micro-movements (MFMs) and neutral expression.
This method has been evaluated on CASME II database.
LBP-TOP and Gaussian Derivatives (GDs) features are ob-
tained. RF and SVM used as classiﬁers. Normalization has
been done before extract the features to make sure that all
faces are in the same position. The images have been divided
into 9x8 blocks with no overlapping. Local features obtained
for each block after being processed separately using GDs.
These local features concatenated into the overall global
feature description. LBP-TOP has been calculated for each
block through all three planes X, Y and T. In the classiﬁcation
phase data has been separated into testing and training. 100-
fold cross-validation was used for testing. The best accuracy
achieved is 92.60% when RF has been used and separate
testing and training data into 50% and a combination of
LBP-TOP and GDs features were used.
House and Meyer [41] implemented a method for micro-
expression recognition and detection. They used LBP-TOP


## Page 8


PREPRINT SUBMITTED TO IEEE JOURNAL.
8
and local gray code patterns on three orthogonal planes
(LGCP-TOP) as features descriptors. SVM has been used as
classiﬁer and SMIC database used to evaluate the method.
LGCP-TOP is modiﬁed version of LGCP [54] that originally
worked for facial expressions and re-worked for analysing
the dynamic texture of micro-expressions. They did not
overcome the result of LBP-TOP from [24] and they returned
this to the feature vectors of LGCP-TOP, which is too large to
be classiﬁed without over-ﬁtting. They claimed that LGCP-
TOP had advantage over LBP-TOP in computational time of
the feature descriptor.
Wang et al. [42] inspired two feature descriptors for
micro-expressions recognition from the concept of LBP-
TOP, LBP-Six Intersection Points (SIP) and LBP-Three Mean
Orthogonal Planes (MOP). LBP-SIP is an extension of LBP-
TOP and more compact form. This compaction is based
on the duplication in computing neighbour points through
three planes. Therefore, they only considered the 6 unique
points on intersection lines of three orthogonal planes. They
claimed that these 6 points carry sufﬁcient information to
describe dynamic textures. Vector dimensions in LBP-SIP is
20, in contrast LBP-TOP produce 48 dimensions.
The basic idea of LBP-MOP is to compute features of
mean planes rather than all frames in the video. Those
two descriptors were evaluated on CASME II and SMIC
databases use baseline settings for both datasets [24],
[26]. Leave-one-video-out (LOVO) and Leave-one-subject-
out (LOSO) cross-validation conﬁgurations have been tested
on two datasets with different popular kernels for SVM.
Also a Wiener ﬁlter has been applied for image smoothing
to remove noise. LBP-MOP achieved best result (66.8%) on
CASME II with linear kernel for SVM using LOVO cross
validation and Wiener ﬁlter applied in preprocessing step.
On SMIC the two methods did not achieve better results
than the original LBP-TOP, which achieved 66.46% with
Wiener ﬁlter and RBF kernel for SVM using LOVO cross
validation.
Wang et al. [35] proposed a novel color space model
for micro-expressions recognition using dynamic textures
on Tensor Independent Color Space (TICS) in which the
color components are as independent as possible. They
claimed it will enhance the performance of micro-expression
recognition. It differs from other literature [26] [24] in getting
LBP-TOP features from color as a fourth-order tensor in
addition to width, height and time. These experiments were
conducted on two micro-expression databases, CASME and
CASME II. SVM has been used as classiﬁer. The results show
that the performance in TICS is better than that in RGB or
grayscale, where the best result achieved on CASME class B
is 61.85% and 58.53% on CASME II. Although the accuracy
is lower than other state of the art in same area [25], [26]
but reveals that TICS may provide useful information more
than RGB and grayscale.
In addition to TICS, Wang et al. [43] further show that
CIELab and CIELuv are also could be helpful in recog-
nising micro-expressions. They achieved 61.86% accuracy
on CASME class B using TICS, CIELuv and CIELab with
different parameters for LBP-TOP. An accuracy of 62.30%
was achieved on CASME II using TICS and CIELuv with
different parameters for LBP-TOP.
Le et al. [44] proposed a preprocessing step that may
enhance recognition rate for micro-expressions. Due to the
redundant frames without signiﬁcant motion which gener-
ated when recording with high-speed camera which have
high fps, they proposed to use Sparsity-Promoting Dy-
namic Mode Decomposition (DMDSP) [55] to analyse and
eliminate this redundancy. They used LBP-TOP to extract
features, with SVM and Linear Discriminant Analysis (LDA)
[56] as classiﬁers. This method was evaluated on CASME II.
F1-score, recall and precision have been used to measure
the performance. The percentages of reserved frame using
DMDSP were varied between 45% and 100% of original
frame length. The performance increased while the percent-
ages of reserved frames decreased. The best performance
was achieved when 45% of frames were reserved with
F1-score, precision and recall equal to 0.52, 0.48 and 0.56
respectively when SVM was used, and 0.47, 0.42 and 0.53
when LDA was used. The performance was compared to
the benchmark of CASME II [26] and outperformed the
benchmark.
Le et al. [36] deﬁned three difﬁculties that faced Micro-
Expression recognition systems: difﬁculty of being able to
differentiate between two micro-expressions for one sub-
ject, namely inter-class similarity, dissimilarity of the same
micro-expression between two subjects due to the different
facial morphology and behaviour, the uneven distribution
of each classes and subjects. They aimed to resolved two
latter problems by using facial registration, cropping and
interpolation as preprocessing to remove morphological
differences. They have proposed variant of AdaBoost to deal
with imbalanced characteristics of micro-expressions. The
experiments were evaluated on CASME II and SMIC. In
addition, TIM has been used to avoid the biases that can
be caused by the different frame lengths. For feature extrac-
tion LBP-TOP was used and a Selective Transfer Machine
(STM) has been used to avoid imbalances which came from
the mismatch between distributions of training and testing
samples that caused by leave-one-subject-out (LOSO) cross
validation to evaluate the datasets. The best result was
achieved on CASME II (43.78% recognition rate) when STM
used with AdaBoost and ﬁxed frame length of 15 frames,
for SMIC, 10 frames give the best result (44.34% recognition
rate).
More recently, Talukder et al. [57] used LBP-TOP as
features extraction and SVM as classiﬁer after magniﬁed the
motion to enhance the low intensity of micro-expression.
They conducted their method on the SMIC dataset. They
claimed that there is improvement on the recognition re-
sult due to the motion magniﬁcation applied with average
recognition rate up to 62% on SMIC-NIR.
Unlike other studies Duan et al. [58] extracted LBP-TOP
from the eye region, not from the whole face. They tested
this method on CASME II. They used more than 20 classi-
ﬁers to train the features. Their method performed better
than other methods when classifying happy and disgust
expressions.
Huang et al. [45] proposed Spatio-Temporal Local Binary
Pattern with Integral Projection (STLBP-IP). They used in-
tegral projection to boost the capability of LBP-TOP with
experiments conducted on the CASME II and SMIC datasets
using SVM as a classiﬁer. When they tested this method on
CASME II, it was been compared with several methods from


## Page 9


PREPRINT SUBMITTED TO IEEE JOURNAL.
9
different studies and was used different parameters for LBP-
TOP and different kernel for SVM, and also compared with
LBP-SIP [42] and LOCP-TOP [59] that achieved a promising
performance over these methods with an accuracy rate of
59.51%. When they evaluated their method on SMIC they
compared it with [24], [49], [60], [61] and achieved 57.93%.
Huang et al. [62] proposed facial micro-expression recog-
nition method using discriminative spatio-temporal local
binary pattern with an improved integral projection. They
proposed this method to preserve the shape attribute of
micro-expressions. They claimed that extracting features
from the global face region lead to ignoring the discrimina-
tive information between different classes. They conducted
this method on three publicly available datasets: SMIC,
CASME and CASME II. They compared this new method
with their previous study [45] and demonstrated better
results across three datasets with accuracy rate up to 64.33%
on CASME, 64.78% on CASME II and 63.41% on SMIC.
Wang et al. [63] used LBP-TOP features to recognise
micro-expressions after pre-processed the CASME II dataset
with Eulerian Video Magniﬁcation (EVM). SVM and k-
nearest neighbour (KNN) have been used as classiﬁers to
classify between 5 motions from CASME II dataset. They
used leave-one-subject validation with comparison with
baseline [26] and other methods [38], [42], [64], [65]. Their
proposed method achieved accuracy of up to 75.30%.
Zhang et al. [66] combined local LBP-TOP and local
Optical Flow (OF) features after extracted them from local
regions of face based on AUs and conducted it on CASME II.
They claimed that different local features can perform better
than single global features. They compare between different
classiﬁers with different parameters (KNN, SVM and RF),
also a comparison between global features and local features
has been conducted to prove their hypothesis. Accuracy up
to 62.50% has been achieved when they combined two local
features with RF classiﬁer.
To solve the cross-database ME recognition problem
Zong et al. [67] proposed a method to regenerate the target
sample in the process of recognition to have the similar fea-
ture distributions as source sample, they called their method
Target Sample Re-Generator (TSRG). They evaluated this
method on CASME II and three types of SMIC, therefore
six experiments have been conducted where the databases
served as source and target. Uniform LBP-TOP have been
used as features extractor and UAR and WAR used as per-
formance measurement. Comparing to some state-of-the-art
method TSRG overcome them in seven experiments in both
weighted average recall (WAR) and unweighted average
recall (UAR) of 12 in total. They improve their work in [68]
and proposed a frame work called it Domain Regeneration
(DR) the difference is the generating from both source and
target for more similar feature distributions. And they used
here three domains to regenerating samples DR-face space
for target (DRFS-T), DR-face space for sample (DRFS-S) and
DR-line space (DRLS).
By combining heuristic and automatic approaches Li-
ong et al. [69] introduced a method to recognize micro-
expression by selecting facial regions statically based on
AUs frequency occurring(ROI-selective). They used a hy-
brid features (Optical Strain Flow (OSF) and block-based
LBP-TOP). They tested their method on CASME II and
SMIC using SVM as classiﬁer with LOSOCV and LOVOCV
to validate the effectiveness. The results have been reported
using more than one measurements including accuracy and
F-measure and compared with baseline of OSF and LBP-
TOP. the method overcome the baseline of two features in
all measurement and with both validations, in term of F-
measure the best result was 0.51 and 0.31 on SMIC and
CASME II respectively.
Zong et al. [70] argued that extracting features of ﬁxed-
sized facial blocks for micro-expression recognition is not
suitable technique. This is due to the fact that it may ignore
some information about the AU if it is small or may get
overlapping if it is large, leading to the extraction of confus-
ing information. To solve the mentioned problem, they pro-
posed hierarchical division scheme which is dividing face
into regions with different densities and different size. They
also proposed a learning model called it kernelized group
sparse learning (KGSL). More than one feature types have
extracted from those hierarchical divisions such as LBP-TOP,
LBP-SIP and STLBP-IP. Evaluating of hierarchical division
and KGSL have been done on CASME II and SMIC using
LOSOCV. The best result achieved on CASME II, when
using Hierarchical STLBP-IP + KGSL and it was 63.97% and
0.6125 in term of accuracy and F1-score respectively.
3.3
Histogram of Oriented Optical Flow (HOOF)
Liu et al. [46] proposed Main Directional Mean Optical-ﬂow
(MDMO) as features for recognition micro-expression. Their
MDMO consist of Regions of Interest (ROIs) based partially
on AUs. One of the signiﬁcant advantages of MDMO is the
small features dimension, where the features vector length
equal to 72 which is 2 features extracted from each region
of 36 ROIs. Aligned all frames to the ﬁrst frame has been
applied to reduce the noise result from head movements.
SVM classiﬁer has been adopted for recognition. SMIC,
CASME and CASME II datasets were used to evaluate their
method. The result compared to the benchmark which used
LBP-TOP and histogram of oriented optical ﬂow (HOOF)
features and achieve better result compare to benchmark
which 68.86%, 67.37% and 80% on CASME, CASME II and
SMIC respectively.
Song et al. [33] used a Harris3D detector with combina-
tion of HOG and the Histograms of Oriented Optical Flow
(HOOF) features, and used codebook to encode features in
a sparse manner of micro-expressions. To predict expression
they used Support Vector Regression (SVR) [87]. They eval-
uated this method on a subset of the SEMAINE corpus [88]
dataset.
Happy and Routray [83] they claimed that the changes
on the face during a micro-expression is temporal changes
more than spatial. Based on this claim they proposed tem-
poral features descriptor called Fuzzy Histogram of Optical
Flow Orientation (FHOFO) and its an extension of HOOF.
They evaluated their method on CASME, CASME II and
SMIC. The best result was achieved in term of F1 score
was 0.5489, 0.5248 and 0.5243 on the mentioned datasets
respectively. In [89] They used Pair-wise feature proximity
(PWFP) as features selection to improve the result in the
previous study which has been slightly improved.
To enhance micro-expression recognition Zhu et al. [86]
transfer learning from speech to micro-expression and call


## Page 10


PREPRINT SUBMITTED TO IEEE JOURNAL.
10
TABLE 7
Summary (Part II: 2016 - 2018) of the feature type, classiﬁer and metrics used over the past decade for micro-expression recognition by year and
authors.
Year
Authors
Datasets
Feature type
Classiﬁer
Metrics (Best Result)
2016
Chen et al. [31]
CASME II(36 samples)
3DHOG
Fuzzy
Accuracy: 86.67%.
2016
Talukder et al. [57]
SMIC
LBP-TOP
SVM
Accuracy: 62% on SMIC-NIR
2016
Duan et al. [58]
CASME II
LBP-TOP from eye region
26 classiﬁers
Perform better on happy and disgust
2016
Huang et al. [62]
SMIC, CASME
and CASME II
improved of STLBP-IP
SVM
Accuracy:64.33% on CASME
64.78% on CASME II and 63.41% on SMIC
2016
Wang et al. [63]
CASME II
LBP-TOP
SVM and KNN
Accuracy: 75.30%
2016
Zhang et al. [71]
CASME II
gabor ﬁlter+ PCA and LDA
SVM
Good performance on static image
2016
Huang et al. [72]
SMIC, CASME
and CASME II
STCLQP
Codebook
Accuracy:64.02% on SMIC
57.31% CASME and 58.39% CASME II
2016
Ben et al. [73]
CASME
MMPTR
Euclidean distance
Accuracy: 80.2%
2016
Liong et al. [74]
SMIC and CASME II
Bi-WOOF
SVM
F1-score:0.61 on CASME II, 0.62 on SMIC-HS
2016
Liong et al. [75]
SMIC and CASME II
Bi-WOOF
SVM
F1-score:0.59 on CASME II
Accuracy:53.52 on SMIC-VIS
2016
Liong et al. [76]
CASME II and SMIC
Optical Strain
SVM
Accuracy:63.41% on CSME II
52.44% on SMIC
2016
Oh et al. [77]
CASME II and SMIC
I2D
SVM
F1-score: 0.41 and 0.44 on CASME II and SMIC
2016
Wang et al. [78]
CASME and CASME II
STCCA
Nearest Neighbor, SVM
Mean recognition accuracy : 41.20% on CASME
38.39 on CASME II
2016
Zheng et al. [79]
CASME and CASME II
LBP-TOP, HOOF
RK-SVD
Accuracy:69.04% on CASME
63.25% on CASME II
2016
Kim et al. [80]
CASME II
CNN
LSTM
Accuracy: 60.98%
2017
Zhang et al. [66]
CASME II
LBP-TOP,Optical Flow
KNN, SVM and RF
Accuracy: 62.50%
2017
Zheng [81]
SMIC, CASME
and CASME II
2DGSR
SRC
Accuracy:71.19% and 64.88%
on CASME and CASME II
2017
Ben et al. [82]
CASME II
HWP-TOP
SSVM
Recognition rate of 0.868
2017
Zong et al. [67]
CASME II and SMIC
LBP-TOP
TSRG
UAR 60.15
2017
Happy and Routray [83]
CASME II,
CASME and SMIC
FHOFO
SVM, KNN and LDA
F1-score was 0.5489, 0.5248 and 0.5243
CASME, CASME II and SMIC
2017
Hao et al. [84]
JAFFE
WLD and DBN
DBN
Recognition rate: 92.66
2017
Peng et al. [85]
CASMEI/II
OF
DTSCNN
Accuracy up to 66.67%
2018
Liong et al. [69]
CASME II and SMIC
OSF and LBP-TOP
SVM
F-measure: 0.51 and 0.31 SMIC and CASME II
2018
Zhu et al. [86]
CASME II
LBP-TOP and OF
SVM
accuracy of 53.3%
2018
Zong et al. [70]
CASME II and SMIC
LBP-TOP, LBP-SIP and STLBP-IP
KGSL
F1: 0.6125 on CASME II
their method coupled source domain targetized with updat-
ing tag vectors. LBP-TOP and OF have been used as features
extractor with different vector dimension. They used SVM
as classiﬁer and evaluated their method on CASME II. The
best accuracy of 53.3% achieved by OF with dictionary
dimensions at 50.
3.4
Deep Learning Approaches
Over the past few years, deep learning approaches, such as
convolutional neural networks (CNNs), have grown rapidly
with a growing number of successful applications [90], [91].
A core feature of CNNs is the network architecture that
produces the features to represent the input data. Popu-
lar architectures include LeNet [92], GoogLeNet [93] and
AlexNet [94]. Many deep learning approaches focus on
static images for classiﬁcation, object detection or segmen-
tation. Spatio-temporal based analysis methods using 3D
CNNs are emerging with new applications, primarily on
action recognition [95], [96], [97], [98].
As the datasets associated with these new methods are
very large in number, for example the Sports-1M Dataset
by Karpathy et al. [96], gaining discriminative data for 3D
CNNs is a much easier task than collecting spontaneously
induced micro-expressions. Therefore, there are very few
approaches to detecting and recognising subtle motion us-
ing deep learning.
One of the ﬁrst to use CNNs in micro-expressions analy-
sis is by Kim et al. [80]. They proposed a new feature repre-
sentation for micro-expressions where the spatial informa-
tion at different temporal states (i.e. onset, apex and offset)
are encoded using a CNN. This method used the extracted
features attempted to help discriminate micro-expression
classes when the model is passed to the long short-term
memory (LSTM) recurrent neural network, where the tem-
poral characteristics of the data are analysed. The overall
achieved accuracy when comparing with the state-of-the-art
was 60.98%, which is still relatively similar to many micro-
expression recognition systems that only use accuracy for
the evaluation metric. Further, the method only evaluated
on single dataset, i.e. CASME II [26] dataset and does not
consider more modern micro-expression datasets such as
SAMM [27] and CAS(ME)2 [28].
In 2017, Peng et al. [85] proposed a new method
named Dual Temporal Scale Convolutional Neural Net-
work (DTSCNN). Due to the data deﬁciency in available
datasets, they designed a shallower neural network for
micro-expression recognition with only 4 layers for both
convolutional and pooling layers. As stated in its name,
DTSCNN is a two streams network. The network has been
fed with the optical-ﬂow sequences. CASMEI/II datasets
were used in the experiment and have been merged by
the authors using selected data from both datasets, CASME
I/II have been categorized into 4 classes: Negative, Others,
Positive and Surprise. They achieved the best accuracy of
66.67%.
Hao and Tian [84] used deep belief network (DBN) as
the second stage features extractor to extract more global


## Page 11


PREPRINT SUBMITTED TO IEEE JOURNAL.
11
feature with less computation cost. DBN classiﬁcation has
been done by pre-training and ﬁne-tuning in DBN. This was
fused with the ﬁrst stage local features was Weber Local
Descriptor (WLD). However, their method only evaluated
on a non-spontaneous dataset JAFFE [99], which was dated
and difﬁcult to compare with current literature.
The review reﬂects the existing CNN-based methods
faced similar problem in terms of data. Overall, micro-
expression recognition using deep learning is still in its
infancy due to a lack of available dataset. A large amount
of data is crucial when training CNNs like many machine
learning approaches. Micro-expressions are very complex
and cannot easily be categorised into distinct classes as
many approaches attempt to do [10], [23], [100]. Using 3D
CNN features to understand the subtle movement would be
a better approach to generalise the problem of discriminat-
ing a micro-expression on the face.
3.5
Other Feature Extraction Methods
Lu et al. [37] proposed Delaunay-Based Temporal Coding
Model (DTCM) for Micro-Expression Recognition. Active
Appearance Model (AAM) used to deﬁne facial feature
points (68 points). Delaunay triangulation has been imple-
mented based on the feature points. This process divides
the facial area into number of sub-regions with triangle
shape. Normalisation has been done based on standard face
(neutral), this remove personal appearance difference irrel-
ative. They used local temporal variations (LTVs) to code
the features space, where the difference between mean of
grayscale values of subregion and sub-region in neighbour
frame were computed. Delaunay triangulation generates a
large number of subregions which leads to large number
of local features. To overcome this problem, they selected
just subregions related to micro-expression, this selection
based on standard deviation analysis. ﬁnally, the code se-
quences of all subregions concatenated into one feature
vector. RF [101] and SVM have been used as classiﬁers. This
method evaluated on SMIC, CASME class B and CASME II.
They achieved better result than state of the art, with 82.86%,
64.95% and 64.19% on SMIC, CASME class B and CASME II
respectively.
Zhang et al. [71] developed micro-expression recognition
system or visual platform as they claimed that there has not
been much work done in designing these kind of systems.
Their system includes two main parts: feature extraction
and dimensional reduction, they used a gabor ﬁlter for
feature extraction and principal components analysis (PCA)
and LDA for dimension reduction. For classiﬁcation stage,
SVM has been used. To evaluate their system, CASME II
and real-time videos were used. They claimed that the
system have a good performance on static images counter
to real-time videos. Gabor ﬁlter also been used by Wu et
al. [53] but they evaluated the performance on Cohn and
Kanades dataset (CK) [102], which was developed for facial
expression analysis.
Li et al. [47] evaluated the performance of three feature
types (LBP, HOG and histograms of image gradient orienta-
tion (HIGO)) on two publicly available datasets (CASME
II and SMIC). They extracted these three features from
different planes. LSVM was employed as the classiﬁer using
LOSO validation. On CASME II, the best accuracy was
57.49%. This is achieved when they extracted HOG from
both 3 orthogonal planes (HOG-TOP) and XT, YT planes
(HOG-XYOT). On the other hand, three versions of SMIC
were tested - VIS, NIR, HS and sub of HS, with the last
one achieved the best accuracy and when features were
extracted using HIGO-TOP and HOG-TOP. In addition, an
effect of the interpolation length was tested with different
frame lengths from 10 to 80 with ﬁxed incremental steps
of 10 frames. The best performance was achieved with an
interpolation to 10 frames and it was 53.52%, 45.12% and
38.02% on SMIC-VIS, SMIC-HS and SMIC-NIR respectively.
Huang et al. [72] outlined two problems of LBP-TOP. The
ﬁrst problem is LBP-TOP does not consider useful informa-
tion, the second problem is the classical pattern used by
LBP-TOP may not be good for describing local structure. To
avoid those two problems, they proposed Spatio-Temporal
Completed Local Quantization Patterns (STCLQP), which
extracted sign, magnitude and orientation. In addition, a
codebook were developed for each component in both ap-
pearance and temporal domains.Their method was evalu-
ated on SMIC, CASME and CASME II with accuracy of
64.02%, 57.31% and 58.39%, respectively.
Spatio-Temporal Texture Map (STTM) was developed
by Kamarol et al. [48]. STTM used a modiﬁed version of
Harris corner function [103] to extract the micro-expression
features. This method evaluated on CASME II, and com-
pared with other features (Volume Local Binary Pattern
(VLBP) and LBP-TOP). They used SVM with one-against-
one classiﬁcation between four classes. In terms of accuracy,
the average recognition rate of STTM performed slightly
better than the other features which is reached to 91.71%
in contrast LBP-TOP achieved 91.48%. On the other hand,
in terms of computation time, there is a large difference
between STTM and other features, where STTM process one
frame in 1.53 seconds in contrast to 2.57 and 2.70 seconds for
VLBP and LBP-TOP respectively.
Wang et al. [39] introduced a micro-expression algorithm
called discriminant tensor subspace analysis (DTSA). This
method was evaluated on the CASME dataset. Extreme
learning machine (ELM) was used as classiﬁer. They have
tested the method with various optimal dimensionality
and different sets of training and testing. The best accu-
racy, 46.90%, was achieved when dimensionality was set to
40×40×40 and the training sample is 15.
Maximum margin projection with tensor representation
(MMPTR) is a micro-expression recognition algorithm con-
tributed by Ben et al. [73]. They tested their algorithm on
CASME. The best average recognition rate, which is 80.2%
was achieved on tensor size of 64×64×64 and training
sample was same as [39] with 15 samples.
Liong et al. [74] questioned whether all frames of micro-
expressions need to be processed for effective analysis. They
used only the apex and the onset frame for experiments
to test this theory. The frames were extracted using their
proposed Bi-Weighted Oriented Optical Flow (Bi-WOOF).
These features were then evaluated on CASME II and the
three formats of SMIC. The best performance achieved on
CASME II and SMIC-HS in terms of F1-score was 0.61 and
0.62 respectively. Bi-WOOF also used by Liong et al. [75]
to extract features from just the apex frame after proposing


## Page 12


PREPRINT SUBMITTED TO IEEE JOURNAL.
12
a method using an eye mask to spot it. This method was
evaluated on CASME II and SMIC and achieved 0.59 on
CASME II in terms of F1-score.
Liong et al. [76] proposed two sets of features: optical
strain and optical strain weighted. These two features con-
structed by utilising facial optical strain magnitudes. They
performed the features on the CASME II and SMIC and
they overcame the baseline of two datasets [24], [26] with
recognition rate reach to 52.44% on SMIC and 63.16% on
CASME II.
Oh et al. [77] claimed that there is changes on facial
contour which are located in different part of face are crucial
for the recognition micro-expressions. According to that
they proposed a feature extraction method to represent these
changes called Intrinsic Two-Dimensional local structuresm
(I2D). This method was evaluated on the CASME II and
SMIC dataset.The result was better than two state of the art
[24], [26] with the best F1-score of 0.41 and 0.44 on CASME
II and SMIC respectively.
Sparse Tensor Canonical Correlation Analysis (STCCA)
was proposed by Wang et al. [78] to improve the recognition
rate of micro-expressions. They conducted the experiment
on CASME and CASME II. They proved that their method
can perform better than 3D-Canonical Correlation Analysis
and three-order Discriminant Tensor Subspace Analysis. In
addition to that they proved that Multi-linear Principal
Component Analysis is not suitable for micro-expression
recognition.
Zheng et al. [79] proposed a a relaxed K-SVD classiﬁer
(RK-SVD) and tested it on LBP-TOP and HOOF features to
be used for micro-expression recognition. They evaluated
this proposed classiﬁer on CASME and CASME II, and
compared it with different classiﬁers such as SVM, MKL
and RF. The results was better than other classiﬁers for both
features and on two datasets [25], [26] with best accuracy of
69.04% and 60.82% for LBP-TOP and HOOF respectively on
CASME, and on CASME II the accuracy was 63.25% 58.64%
for the same features respectively.
Zheng [81] proposed a method for micro-expression
recognition named 2D Gabor ﬁlter and Sparse Representa-
tion (2DGSR). They evaluated their method on three pub-
licly available datasets (SMIC, CASME and CASME II) and
compared it with other popular methods (LBP-TOP, HOOF-
whole and HOOF-ROIs). For classiﬁcation Sparse Repre-
sentations Classiﬁer (SRC) has been used with LOSO cross
validation. In terms of accuracy they achieved a result up to
71.19% and 64.88% on CASME and CASME II respectively.
Ben et al. [82] proposed local binary feature descriptor
called hot wheel patterns from three orthogonal planes
(HWP-TOP) which has been inspired by dual-cross patterns
from three orthogonal planes (DCP-TOP) with some rota-
tions. They used smooth SVM (SSVM) as a classiﬁer. They
evaluated their descriptor on 61 samples from CASME II
with three classes(except fear and sadness) and achieved
recognition rate of 0.868. They try to solve the problem
of micro-expression limited samples by leverage labeled
macro-expression and shared feature between macro and
micro expression, however this may be not so accurate due
the difference between macro and micro characteristic.
After extracting features using distance estimation be-
tween points which have been predicted using ASM Jain
et al [104] using Random Walk-based (RW) to learn the
features before providing it to Artiﬁcial Neural Network
(ANN) classiﬁer. RW reduces the dimensionality of the
feature and this minimize the complexity of computation.
They evaluated their method on CASME and SMIC and
provide the result in term of AUC, which is up to 0.8812
and 0.9456 on SMIC and CASME respectively.
As shown in this section many methods and feature
descriptors have been used for micro-expression recogni-
tion, summarization of these methods shown in Table 6.
These methods have been evaluated on different datasets
which have varying on properties such as frame rates and
resolution. In this paper, we contribute to the research by
addressing the challenge of how different features react on
spatial temporal settings, particularly focusing on resolu-
tions, which has not done in previous research.
4
PERFORMANCE
METRICS
AND
VALIDATION
TECHNIQUES
The spotting accuracy of humans peaks around 40% [8].
Analysis using computer algorithms incorporating machine
learning and computer vision can only be evaluated fairly
with a standardised metrics. This section elaborates the
metrics used in the literature. Drawing from detailed review
in Section 3, we summarised and explain the evaluation
metrics.
4.1
Metrics
The metrics for micro-expressions analysis are commonly
used for binary classiﬁcation purposes, and so is adequate
for quantifying True Positive (TP), False Positive (FP), True
Negative (TN) and False Negative (FN) detections. More de-
tailed information on these measures can be found in [105].
The earlier work, as illustrated in Table 6, the majority of the
results in micro-expressions analysis are based on Accuracy.
as deﬁned in equation 1.
Accuracy =
TP + TN
TP + FP + TN + FN
(1)
In the later stage, as illustrated in Table 7, the measurement
of performance were reported in F1-Score (or F-Measure).
Other metrics such as Recall, Precision, and Matthews Cor-
relation Coefﬁcient (MCC) are also gradually used to report
the results. By using the Precision measure of exactness, and
determines a fraction of relevant responses from results. Re-
call, or sensitivity, is a fraction of the results that are relevant
to the experiment and that are successfully retrieved.
Precision =
TP
TP + FP
(2)
Recall =
TP
TP + FN
(3)
It is unlikely to use these measures on their own as
both these measure are commonly used together to form
an understanding of the relevance of the results returned
from experimental classiﬁcation. The F-Measure is useful in
determining the harmonic mean between the Precision and


## Page 13


PREPRINT SUBMITTED TO IEEE JOURNAL.
13
Recall and is used in place of accuracy as it provides a more
detailed analysis of the data. The equation can be deﬁned as
F-Measure =
2TP
2TP + FP + FN .
(4)
A downside to this measure is that it does not take
into account TN, a value that is required to create ROC
curves. The MCC uses all detection types to output a value
between −1, which indicates total disagreement and +1,
which indicates total agreement. A value of 0 would be
classed as a random prediction, and therefore both variables
can be deemed independent. It can be provide a much more
balanced evaluation of prediction than previous measure-
ments, however it is not always possible to obtain all four
detection types (i.e. TP, FP, FN, TN). The coefﬁcient can be
calculated by
MCC =
TP × TN −FP × FN
p
(TP + FP)(TP + FN)(TN + FP)(TN + FN)
(5)
4.2
Validation Techniques
Two commonly used validation techniques in computer
vision are n-fold cross validation and leave-one-subject-out
(LOSO). From our review, the evaluation system by differ-
ent researchers reported in different validation techniques,
where LOSO is more widely used. While some reported
their results in both validation techniques [27], [46], and
some only reported in LOSO [32], [79], [80].
5
CHALLENGES
Research on automated micro-expressions recognition using
machine learning has witnessed good progress in recent
years. A number of promising methods based on texture
features, gradient features and optical ﬂow features have
been proposed. Many datasets was generated but lack of
standardisation is indeed a great challenge. This section
provides the challenges of the research in micro-expressions
analysis into details.
5.1
The effect of Spatial Temporal Settings in Data Col-
lection
Due to lack of communication between different research
groups on experimental settings, the datasets are varied
in resolution and frame rates. Some researchers [24], [47]
investigated on the effect of Temporal setting to micro-
expression recognition. Using TIM [32] to adjust the tem-
poral settings is a well-known method in micro-expression
analysis. However, there is a lack of thorough research
in further investigating the implication of spatial-temporal
changes for micro-expression recognition.
We believe resolution plays an important role for fea-
tures extraction. We downscale the CASME II dataset to
four scales, 100% (original resolution), 75% of the original
resolution, 50% of the original resolution and 25% of the
original resolution, as depicted by Figure 5. To address the
research gap, we experiment this four resolutions with three
feature types (LBP-TOP, 3DHOG and HOOF) with 10-fold
cross validation and LOSO. To reduce the effect of learning
Fig. 5. An example of different resolution by downscaling an image from
CASME II dataset. From left to right: 100% (Original resolution), 75%
of the original resolution, 50% of the original resolution and 25% of the
original resolution.
Fig. 6. The effect of image resolution on micro-expression recognition
using LBP-TOP, 3DHOG and HOOF on two different evaluation method:
(a) 10-fold cross validation, and (b) LOSO.
algorithm, we used a standard SVM method as the classiﬁer.
Figure 6 compares the performance of the experiments.
From the observation, LBP-TOP performed better in high
resolution images than 3DHOG and HOOF. It is noted that
HOOF performed better when we downscale the resolution
to 50% and 3DHOG worked best at 25%. These results
showed LBP-TOP relied on spatial information (XY), but
HOOF and 2DHOG are more dependent on temporal (XT
and YT). The conventional methods are relies on feature
descriptors and varies from one to another.
5.2
Emotional Classes versus Objective Classes in
Data Labelling
A large focus on micro-expression research has been on
the detection and recognition of emotion-based classed (i.e.


## Page 14


PREPRINT SUBMITTED TO IEEE JOURNAL.
14
TABLE 8
A breakdown of the number of clips categorised into estimated emotion
classes for the SAMM dataset.
Estimated Emotion
Number of Clips
Anger
57
Contempt
12
Disgust
9
Fear
8
Happiness
26
Sadness
6
Surprise
15
Other
26
discreet groups that micro-expression ﬁt into during classiﬁ-
cation). Objective classes attempt to take away the potential
bias of labelling difﬁcult to distinguish micro-expressions
into classes suited to a particular muscle movement pattern.
To date, SAMM [27] is the only dataset that moves the
focus from an emotional-based classiﬁcation system, to an
objective one, and is designed around analysing objective
physical movement of muscles. Emotion classiﬁcation re-
quires the context of the situation for an interpreter to
make a meaningful interpretation. Most spontaneous micro-
expression datasets have FACS ground truth labels and
estimated or predicted emotion. These have been annotated
by an expert and self-reports written by participants. In
SAMM, Davison et al. [27] focused on objectiveness and
did not report emotional classes in their dataset release.
Due to this reason, it has not been widely experimented by
other researchers. To address this issue, we introduced the
emotional classes for SAMM in this paper.
SAMM has estimated emotional classes based on the
AUs and the emotional stimuli presented to participants to
allow for comparison with previous emotion class focused
papers such as CASME II [26] and SMIC [24]. The amount of
clips in the SAMM dataset in each estimated emotion class
can be seen in Table 8. Note that the categories are based
around EMFACS labelling of reliable AUs to emotion [106],
so any that did not ﬁt into these categories are placed in the
‘Other’class.
To this end it can be argued that keeping classiﬁcation
to well-deﬁned muscles (that cannot be changed or bias)
is a more optimal solution to micro-expression recognition
than discreet emotion classes. Further, Yan et al. [107] state
that its inappropriate to categorise micro-expressions into
emotion categories, and that using FACS AU research to
inform the eventual emotional classiﬁcation would be a
more logical approach. In 2017, Davison et al. [108] pro-
posed new objective classes based on FACS coding. They
have coded the two state-of-the-art FACS-coded datasets
into seven objective classes as illustrated in Table 9. This
research could potentially be the new challenge for micro-
expression research.
5.3
Face Regions in Data Analysis
Recent work on the micro-expressions recognition have
provided promising results on successful detection tech-
niques, however there is room for improvement. To begin
detection, current approaches follow methods of extracting
local feature information of the face by splitting the face into
regions, as illustrated in Figure 7.
TABLE 9
Each class represents AUs that can be linked to emotion.
Class
Action Units
I
AU6, AU12, AU6+AU12, AU6+AU7+AU12, AU7+AU12
II
AU1+AU2, AU5, AU25, AU1+AU2+AU25, AU25+AU26,
AU5+AU24
III
A23, AU4, AU4+AU7, AU4+AU5, AU4+AU5+AU7,
AU17+AU24, AU4+AU6+AU7, AU4+AU38
IV
AU10, AU9, AU4+AU9, AU4+AU40, AU4+AU5+AU40,
AU4+AU7+AU9, AU4 +AU9+AU17, AU4+AU7+AU10,
AU4+AU5+AU7+AU9, AU7+AU10
V
AU1, AU15, AU1+AU4, AU6+AU15, AU15+AU17
VI
AU1+AU2+AU4, AU20
VII
Others
Fig. 7. Illustration of face regions: (a) 5 × 5 blocks, (b) 8 × 8 blocks, (c)
Delaunay triangulation, and (d) FACS-based regions.
The state of the art can be categorised into:
•
Four quadrants. Shreve et al. [114] split the face into
4 quadrants and analyse each quarter as individual
temporal sequences. The advantage of this method
is that it is simple to analyse larger regions, how-
ever the information to retrieve from the areas are
restricted to whether there was some form of move-
ment in a more global area.
•
m × n blocks. Another method is to split the face
into a speciﬁc number of blocks [26], [40], [113]. The
movement on the face is analysed locally, rather than
a global representation of the whole face, and can
focus on small changes in very speciﬁc temporal
blocks. A disadvantage to this method is that it
is computationally expensive to process the whole
images as m × n blocks. It can also include features
around the edge of the face, including hair, that do
not relate to movement but could still effect the ﬁnal
feature vector. Figure 7(a) and Figure 7(b) illustrate


## Page 15


PREPRINT SUBMITTED TO IEEE JOURNAL.
15
TABLE 10
A Summary of the current micro-movement methods [109]. Each result metric changes depending on the method. * = true positives/recall, ** =
area under curve.
Method
Feature
Dataset
Result
Moilanen et al. [110]
LBP
CASME II/SMIC
71%*
Shreve et al. [21]
Optical Strain
USF-HD
74%*
Li et al. [47]
LBP
CASME II
92.98%**
Xia et al. [111]
ASM Geometric
Deformation
CASME/CASME
92.08%*
Patel et al. [112]
Optical Flow
SMIC
95%**
Davison et al. [113]
LBP/HOG
SAMM
91.25%*
Davison et al. [108]
3D HOG
CASME II/SAMM
68.04%*
the samples of block-based face regions.
•
Delaunay triangulation. Delaunay triangulation, as
shown if Figure 7(c), has also been used to form
regions on just the face and can exclude hair and
neck [37], however this approach can still extract
areas of the face that would not be useful as a feature
and adds further computational expense.
•
FACS-based region. A more recent and less researched
approach is to use deﬁned regions of interest (ROIs)
to correspond with one or more FACS AUs [35],
[43]. These regions have more focus on local parts
of the face that move due to muscle activation.
Some examples of ROI selection for micro-expression
recognition and detection include discriminative re-
sponse map ﬁtting [46], Delaunay triangulation [37]
and facial landmark based region selection [112]. Un-
fortunately, currently deﬁned regions do not cover
all AUs and miss some potentially important move-
ments such as AU5 (Upper Lid Raiser), AU23 (Lip
Tightener) and AU31 (Jaw Clencher). To overcome
the problem, Davison et al. [108] proposed FACS-
based regions to improve local feature representation
by disregarding face region that do not contribute
to facial muscle movements. The deﬁned region is
presented in Figure 7(b).
Figure 7 compares different face region splitting meth-
ods. Due to FACS-based region is more relevant to facial
muscle movements and suitable for AUs detection, more
research should be focusing on FACS-based region than split
the face into m × n blocks.
5.4
Deep Learning versus Conventional Approaches
The pipeline of conventional micro-expression recognition
approach is very similar to macro-expressions in terms of
preprocessing techniques, hand-crafted features and, if ap-
plicable, machine learning classiﬁcation. However, geomet-
ric feature-based methods are rarely used as tracking feature
points on a face that barely moves will not produce good
results. Instead, appearance-based features are primarily
used to attempt to describe the micro-movement or train
machine learning to classify micro-expressions into classes.
Spatial temporal settings during data collection, prepro-
cessing stage of dataset including face alignment and face
regions split, feature extraction methods and the type of
classiﬁers are the main factors for conventional approaches.
Moving forward, end-to-end solution that is capable of
handling these issues is required. Deep learning approaches
have yet to have much impact on micro-expression analysis,
however to ensure a rounded review of current techniques
we shall provide a preliminary study on deep learning and
its applications to micro-expression.
As the temporal nature of micro-expressions are a
key feature to understand, modern video-analysis tech-
nique, namely 3D convolutional neural networks (3D Con-
vNets) [98], may be used to exploit the temporal dimen-
sion. This network expands on the typical 2D convolutional
neural network (CNN) by using 3×3×3 convolutional ker-
nels where the third dimension is in the temporal domain
(frames in a video). It was originally used for analysis for
action recognition, however it can be expanded for any
other video-analysis task easily. Using the deconvolution
method described by Zeiler and Fergus [115], Tran et al. [98]
was able to show that the features extracted from the 3D
ConvNet focuses on the appearance of the ﬁrst few frames
and then tracks salient motion over the next frames. The key
difference in using 2D ConvNets is the ability to extract and
learn from features from both motion and appearance.
With minimal data available to train from, deep learn-
ing methods have a much more difﬁcult time in learning
meaningful patterns [91]. When independent test samples
were used for validation, the model showed that further
investigation is required for deep learning with micro-
expression to be effective, including the use of more data.
The biggest disadvantage to using video-data is not being
able to load such large amounts of data into memory, even
on GPUs that have 12GB of on-board memory. This leads
to the minimisation of the batch size and reduction of
resolution to allow for training to proceed. Further ways of
being able to handle micro-expression data without having
to reduce the amount of data available would be vital to
retaining the discriminative information required for micro-
expression analysis. Further, the time required to train the
model shows the challenge of the ability to train long video-
based deep learning methods.
5.5
Spotting Micro-movement on the Face
Micro-expressions analysis tends to focus on the emotion
recognition, meaning assumptions are commonly made.
Focusing on micro-facial movements, which describe the
facial muscle activations, removes these assumptions [27].


## Page 16


PREPRINT SUBMITTED TO IEEE JOURNAL.
16
Table 10 summarised the benchmark publications in micro-
movement [109], it is notably less publication when com-
pared to micro-expressions recognition. However, this is
equally important as not all the AUs are linked with emo-
tional context. Future challenge will be focusing on spotting
micro-movements on long videos. There are limited datasets
provide long video clips. One of the dataset provides is
SAMM, where the researchers can received it by posting
a physical hard disk to obtain the full dataset (700GB).
5.6
Standardisation of Metrics
We recommend the researchers to standardised the perfor-
mance metrics that they used in evaluation. As the majority
of datasets are inbalanced [36], reporting the result in F-
Measure (or F1-Score) seems to be the best option. Using the
conventional Accuracy measure may result in a bias towards
classes with large number of samples, hence overestimating
the capability of the evaluated method. F-Measure micro-
average across the whole dataset and is computed based on
the total true positives, false negatives and false positives,
across 10-fold cross validation and Leave-one-subject-out
(LOSO).
Due to each dataset with small micro-expression sam-
ples, the researchers are encourage to use more datasets for
their experiment. For cross datasets evaluation, unweighted
average recall (UAR) and weighted average recall (WAR) are
recommended as these measurements were shown promis-
ing in speech emotion recognition [116]. WAR is deﬁned
as number of correctly classiﬁed samples divided by the
total number of samples, while UAR is deﬁned as sum of
accuracy of each class divided by the number of classes
without considerations of samples per class. To obtain the
overall scores, the results from all the folds are averaged.
These metrics had been recommended in the First Micro-
expressions Grand Challenge Workshop in conjunction with
Face and Gesture 2018 Conference.
5.7
Real-world Implementation
For implementation of the micro-expressions recognition in
real-world, the challenges to be addressed include:
•
Cross-Cultural Analysis Micro-facial expressions oc-
cur when people attempt to hide their true emotion,
and so the possibility of how well some cultures
manage this suppression would be interesting to
learn. By using software to detect micro-expressions
across cultures, the results of different suppression
of emotion can be studied. Therefore people in East
Asian cultures could be different from Western cul-
tures, which can be analysed to ﬁnd any correlation
between the psychological studies and automated
micro-expressions recognition. Something to note in
this type of investigation would be to ensure the
different participants originate and live in their re-
spective countries, as people living with different
cultures for a long time may not exhibit the same
behaviour.
•
Dataset Improvements. Further work can be done
to improve micro-movement datasets. Firstly, more
datasets or expanding previous sets would be a sim-
ple improvement that can help move the research for-
ward faster. Secondly, a standard procedure on how
to maximise the amount of micro-movements in-
duced spontaneously in laboratory controlled exper-
iments would be beneﬁcial. If collaboration between
established datasets and researchers from psychol-
ogy occurred, dataset creation would be more con-
sistent. As using human participants is required, and
emotions are induced, ethical concerns are always
going to play a part in future studies of this kind.
Any work moving forward must take into account
these concerns and draw from previous experiments
to ensure no harm will come to the psychological
welfare of participants.
•
Real-Time Micro-Facial Expressions Recognition.
To be able to implement any form of micro-
movement detection system into a real-world sce-
nario, it must perform the processes required in real-
time (or near to real-time). As the accuracy of facial
expression analysis is already quite high, transition-
ing to real-time has already produced decent results.
However there is currently no known systems that is
able to detect micro-expressions.
The accuracy of many state-of-the-art methods is still too
low to be deployed effectively in a real-world environment.
The progress in research of micro-expressions recognition
can aid in the paradigm shift in affect computing for real-
world applications in psychology, health study and security
control.
6
CONCLUSION
We have presented a comprehensive review on datasets,
features and metrics for micro-expressions analysis. The
ultimate goal of this paper is to provide new insights
and recommendations to advancing the micro-expression
analysis research. We have provided a good guidelines for
beginners and a detailed challenges and recommendations
for those who are already working in this area. In addition,
we contribute to the research by addressing the effect of
resolutions on different feature types and introducing the
new emotional classes for SAMM.
To summarise, the future direction to advance auto-
mated micro-expression recognition should take into con-
sideration on how the dataset is capture (spatial temporal
settings), labeling of the dataset based on Action Unit based
objective classes, FACS-based face regions for better locali-
sation, end-to-end solution using deep learning, fair evalua-
tion using standardised metrics (ideally F1-Score and MCC)
and LOSO as the validation technique. More importantly,
the openness and better communication within the research
communities are crucial to crowd-source the data labelling
and using the standard evaluation system.
As micro-expression recognition is still in its infancy
when compared to the macro-expression, it requires com-
bined efforts from multidisciplinary (including psychology,
computer science, physiology, engineer and policy maker) to
achieve reliable results for practical real-world application.
A controversial point is whether or not it should be allowed


## Page 17


PREPRINT SUBMITTED TO IEEE JOURNAL.
17
to detect these micro-expressions, as the theory behind it
states that the person attempting to conceal their emotion
experience these movements involuntarily and likely un-
knowingly. If we are able to detect them with high accuracy,
then we are effectively robbing a person of being able to hide
something that is private to them. From an ethical point of
view, knowing when someone is being deceptive would be
advantageous but takes away the freedom you had in your
emotions.
ACKNOWLEDGMENTS
The authors would like to thank Prof. Xiaolan Fu of The
Institute of Psychology, Chinese Academy of Sciences for
offering CASME II micro-expression database for this re-
search. The authors would like to thank The Royal Society
Industry Fellowship (Grant number: IF160006, awarded to
Dr. Moi Hoon Yap).
REFERENCES
[1]
P. Ekman, “An argument for basic emotions,” Cognition and
Emotion, vol. 6, pp. 169–200, 1992.
[2]
Paul Ekman, Emotions Revealed: Understanding Faces and Feelings.
Phoenix, 2004.
[3]
P. Ekman and E. L. Rosenberg, What the Face Reveals: Basic and
Applied Studies of Spontaneous Expression Using the Facial Action
Coding System (FACS), ser. Series in Affective Science.
Oxford
University Press, 2005.
[4]
J. A. Russell and J. M. Fern´andez-Dols, The psychology of facial
expression.
Cambridge university press, 1997.
[5]
P. Ekman, “Lie catching and microexpressions,” in The Philosophy
of Deception, C. W. Martin, Ed.
Oxford University Press, 2009,
pp. 118–133.
[6]
D. Matsumoto, S. H. Yoo, and S. Nakagawa, “Culture, emotion
regulation, and adjustment.” Journal of personality and social psy-
chology, vol. 94, no. 6, p. 925, 2008.
[7]
M. O’Sullivan, M. G. Frank, C. M. Hurley, and J. Tiwana, “Police
lie detection accuracy: The effect of lie scenario.” Law and Human
Behavior, vol. 33, no. 6, p. 530, 2009.
[8]
M. G. Frank, C. J. Maccario, and V. l. Govindaraju, “Behavior
and security,” in Protecting airline passengers in the age of terrorism.
Greenwood Pub. Group, 2009.
[9]
M. Frank, M. Herbasz, K. Sinuk, A. M. Keller, A. Kurylo, and
C. Nolan, “I see how you feel: Training laypeople and profession-
als to recognize ﬂeeting emotions,” in International Communication
Association, 2009.
[10]
W.-J. Yan, Q. Wu, J. Liang, Y.-H. Chen, and X. Fu, “How fast are
the leaked facial expressions: The duration of micro-expressions,”
Journal of Nonverbal Behavior, vol. 37, no. 4, pp. 217–230, 2013.
[11]
P. Ekman, Telling Lies: Clues to Deceit in the Marketplace, Politics,
and Marriage.
Norton, 2001.
[12]
P. Ekman and W. V. Friesen, “Nonverbal leakage and clues to
deception,” Psychiatry, vol. 32, no. 1, pp. 88–106, 1969.
[13]
X.-B. Shen, Q. Wu, and X.-L. Fu, “Effects of the duration of
expressions on the recognition of microexpressions,” Journal of
Zhejiang University SCIENCE B, vol. 13, no. 3, pp. 221–230, 2012.
[14]
S. Polikovsky, Y. Kameda, and Y. Ohta, “Facial micro-expressions
recognition using high speed camera and 3d-gradient descrip-
tor,” in Crime Detection and Prevention (ICDP 2009), 3rd Interna-
tional Conference on.
IET, 2009, pp. 1–6.
[15]
I. A. Essa and A. P. Pentland, “Coding, analysis, interpretation,
and recognition of facial expressions,” IEEE transactions on pattern
analysis and machine intelligence, vol. 19, no. 7, pp. 757–763, 1997.
[16]
S. Kimura and M. Yachida, “Facial expression recognition and
its degree estimation,” in Computer Vision and Pattern Recogni-
tion, 1997. Proceedings., 1997 IEEE Computer Society Conference on.
IEEE, 1997, pp. 295–300.
[17]
M. Pantic and L. J. M. Rothkrantz, “Automatic analysis of facial
expressions: The state of the art,” IEEE Transactions on pattern
analysis and machine intelligence, vol. 22, no. 12, pp. 1424–1445,
2000.
[18]
B. Fasel and J. Luettin, “Automatic facial expression analysis: a
survey,” Pattern recognition, vol. 36, no. 1, pp. 259–275, 2003.
[19]
M. McCabe, “Best practice recommendation for the capture of
mugshots,” http://www. itl. nist. gov/iaui/894.03/face/bprmug3. htm,
2009.
[20]
S. Afzal and P. Robinson, “Natural affect datacollection & anno-
tation in a learning context,” in Affective Computing and Intelligent
Interaction and Workshops, 2009. ACII 2009. 3rd International Con-
ference on.
IEEE, 2009, pp. 1–7.
[21]
M. Shreve, S. Godavarthy, D. Goldgof, and S. Sarkar, “Macro- and
micro-expression spotting in long videos using spatio-temporal
strain,” in 2011 IEEE International Conference on Automatic Face
Gesture Recognition and Workshops (FG 2011), 2011, pp. 51–56.
[22]
G. Warren, E. Schertler, and P. Bull, “Detecting deception from
emotional and unemotional cues,” Journal of Nonverbal Behavior,
vol. 33, no. 1, pp. 59–69, 2009.
[23]
T. Pﬁster, X. Li, G. Zhao, and M. Pietik¨ainen, “Recognising spon-
taneous facial micro-expressions,” in Computer Vision (ICCV),
2011 IEEE International Conference on.
IEEE, 2011, pp. 1449–1456.
[24]
X. Li, T. Pﬁster, X. Huang, G. Zhao, and M. Pietikainen, “A
spontaneous micro-expression database: Inducement, collection
and baseline,” in Automatic Face and Gesture Recognition (FG), 2013
10th IEEE International Conference and Workshops on.
IEEE, 2013,
pp. 1–6.
[25]
W.-J. Yan, Q. Wu, Y.-J. Liu, S.-J. Wang, and X. Fu, “Casme
database: a dataset of spontaneous micro-expressions collected
from neutralized faces,” in Automatic Face and Gesture Recognition
(FG), 2013 10th IEEE International Conference and Workshops on.
IEEE, 2013, pp. 1–7.
[26]
W.-J. Yan, X. Li, S.-J. Wang, G. Zhao, Y.-J. Liu, Y.-H. Chen, and
X. Fu, “Casme ii: An improved spontaneous micro-expression
database and the baseline evaluation,” PloS one, vol. 9, no. 1,
2014.
[27]
A. K. Davison, C. Lansley, N. Costen, K. Tan, and M. H. Yap,
“Samm: A spontaneous micro-facial movement dataset,” IEEE
Transactions on Affective Computing, vol. 9, no. 1, pp. 116–129, Jan
2018.
[28]
F. Qu, S.-J. Wang, W.-J. Yan, H. Li, S. Wu, and X. Fu, “Cas
(me)ˆ 2: A database for spontaneous macro-expression and micro-
expression spotting and recognition,” IEEE Transactions on Affec-
tive Computing, 2017.
[29]
P. Ekman and W. V. Friesen, Facial Action Coding System: A
Technique for the Measurement of Facial Movement.
Palo Alto:
Consulting Psychologists Press, 1978.
[30]
S. Polikovsky and Y. Kameda, “Facial micro-expression detection
in hi-speed video based on facial action coding system (facs),”
IEICE transactions on information and systems, vol. 96, no. 1, pp.
81–92, 2013.
[31]
M. Chen, H. T. Ma, J. Li, and H. Wang, “Emotion recognition
using ﬁxed length micro-expressions sequence and weighting
method,” in Real-time Computing and Robotics (RCAR), IEEE In-
ternational Conference on.
IEEE, 2016, pp. 427–430.
[32]
T. Pﬁster, X. Li, G. Zhao, and M. Pietik¨ainen, “Differentiating
spontaneous from posed facial expressions within a generic facial
expression recognition framework,” in Computer Vision Workshops
(ICCV Workshops), 2011 IEEE International Conference on.
IEEE,
2011, pp. 868–875.
[33]
Y. Song, L.-P. Morency, and R. Davis, “Learning a sparse code-
book of facial and body microexpressions for emotion recogni-
tion,” in Proceedings of the 15th ACM on International conference on
multimodal interaction.
ACM, 2013, pp. 237–244.
[34]
Y. Guo, Y. Tian, X. Gao, and X. Zhang, “Micro-expression recogni-
tion based on local binary patterns from three orthogonal planes
and nearest neighbor method,” in Neural Networks (IJCNN), 2014
International Joint Conference on.
IEEE, 2014, pp. 3473–3479.
[35]
S.-J. Wang, W.-J. Yan, X. Li, G. Zhao, and X. Fu, “Micro-expression
recognition using dynamic textures on tensor independent color
space,” in Pattern Recognition (ICPR), 2014 22nd International
Conference on.
IEEE, 2014, pp. 4678–4683.
[36]
A. C. Le Ngo, R. C.-W. Phan, and J. See, “Spontaneous subtle
expression recognition: Imbalanced databases and solutions,” in
Computer Vision–ACCV 2014.
Springer, 2014, pp. 33–48.
[37]
Z. Lu, Z. Luo, H. Zheng, J. Chen, and W. Li, “A delaunay-
based temporal coding model for micro-expression recognition,”
in Asian Conference on Computer Vision.
Springer, 2014, pp. 698–
711.


## Page 18


PREPRINT SUBMITTED TO IEEE JOURNAL.
18
[38]
S.-T. Liong, J. See, R. C.-W. Phan, A. C. Le Ngo, Y.-H. Oh, and
K. Wong, “Subtle expression recognition using optical strain
weighted features,” in Asian Conference on Computer Vision.
Springer, 2014, pp. 644–657.
[39]
S.-J. Wang, H.-L. Chen, W.-J. Yan, Y.-H. Chen, and X. Fu, “Face
recognition and micro-expression recognition based on discrim-
inant tensor subspace analysis plus extreme learning machine,”
Neural processing letters, vol. 39, no. 1, pp. 25–43, 2014.
[40]
A. K. Davison, M. H. Yap, N. Costen, K. Tan, C. Lansley,
and D. Leightley, “Micro-facial movements: An investigation
on spatio-temporal descriptors,” in Computer Vision-ECCV 2014
Workshops.
Springer, 2014, pp. 111–123.
[41]
C. House and R. Meyer, “Preprocessing and descriptor features
for facial micro-expression recognition,” 2015.
[42]
Y. Wang, J. See, R. C.-W. Phan, and Y.-H. Oh, “Efﬁcient spatio-
temporal local binary patterns for spontaneous facial micro-
expression recognition,” PloS one, vol. 10, no. 5, p. e0124674, 2015.
[43]
S.-J. Wang, W.-J. Yan, X. Li, G. Zhao, C.-G. Zhou, X. Fu, M. Yang,
and J. Tao, “Micro-expression recognition using color spaces,”
IEEE Transactions on Image Processing, vol. 24, no. 12, pp. 6034–
6047, 2015.
[44]
A. C. Le Ngo, S.-T. Liong, J. See, and R. C.-W. Phan, “Are subtle
expressions too sparse to recognize?” in 2015 IEEE International
Conference on Digital Signal Processing (DSP).
IEEE, 2015, pp.
1246–1250.
[45]
X. Huang, S.-J. Wang, G. Zhao, and M. Piteikainen, “Facial micro-
expression recognition using spatiotemporal local binary pattern
with integral projection,” in Proceedings of the IEEE International
Conference on Computer Vision Workshops, 2015, pp. 1–9.
[46]
Y.-J. Liu, J.-K. Zhang, W.-J. Yan, S.-J. Wang, G. Zhao, and X. Fu,
“A main directional mean optical ﬂow feature for spontaneous
micro-expression recognition,” IEEE Transaction of Affective Com-
puting, 2015.
[47]
X. Li, X. Hong, A. Moilanen, X. Huang, T. Pﬁster, G. Zhao,
and M. Pietik¨ainen, “Reading hidden emotions: spontaneous
micro-expression
spotting
and
recognition,”
arXiv
preprint
arXiv:1511.00423, 2015.
[48]
S. K. A. Kamarol, N. S. Meli, M. H. Jaward, and N. Kamrani,
“Spatio-temporal texture-based feature extraction for sponta-
neous facial expression recognition,” in Machine Vision Applica-
tions (MVA), 2015 14th IAPR International Conference on.
IEEE,
2015, pp. 467–470.
[49]
G. Zhao and M. Pietikainen, “Dynamic texture recognition using
local binary patterns with an application to facial expressions,”
Pattern Analysis and Machine Intelligence, IEEE Transactions on,
vol. 29, no. 6, pp. 915–928, 2007.
[50]
Z. Guo, L. Zhang, and D. Zhang, “A completed modeling of
local binary pattern operator for texture classiﬁcation,” Image
Processing, IEEE Transactions on, vol. 19, no. 6, pp. 1657–1663, 2010.
[51]
T. F. Cootes, C. J. Taylor, D. H. Cooper, and J. Graham, “Active
shape models-their training and application,” Computer vision and
image understanding, vol. 61, no. 1, pp. 38–59, 1995.
[52]
Z. Niu, S. Shan, S. Yan, X. Chen, and W. Gao, “2d cascaded
adaboost for eye localization,” in Pattern Recognition, 2006. ICPR
2006. 18th International Conference on, vol. 2.
IEEE, 2006, pp.
1216–1219.
[53]
Q. Wu, X. Shen, and X. Fu, “The machine knows what you are
hiding: an automatic micro-expression recognition system,” in
Affective Computing and Intelligent Interaction.
Springer, 2011, pp.
152–162.
[54]
M. S. Islam et al., “Local gray code pattern (lgcp): A robust feature
descriptor for facial expression recognition,” International Journal
of Science and Research (IJSR), India Online ISSN, pp. 2319–7064,
2013.
[55]
M. R. Jovanovi´c, P. J. Schmid, and J. W. Nichols, “Sparsity-
promoting dynamic mode decomposition,” Physics of Fluids
(1994-present), vol. 26, no. 2, p. 024103, 2014.
[56]
J.-T. Chien and C.-C. Wu, “Linear discriminant analysis (lda),”
2005.
[57]
B. B. Talukder, B. Chowdhury, T. Howlader, and S. M. Rahman,
“Intelligent recognition of spontaneous expression using motion
magniﬁcation of spatio-temporal data,” in Paciﬁc-Asia Workshop
on Intelligence and Security Informatics.
Springer, 2016, pp. 114–
128.
[58]
X. Duan, Q. Dai, X. Wang, Y. Wang, and Z. Hua, “Recognizing
spontaneous micro-expression from eye region,” Neurocomputing,
vol. 217, pp. 27–36, 2016.
[59]
L.-b. S. A. Spatiotemporal, “Local ordinal contrast pattern his-
tograms for spatiotemporal, lip-based speaker authentication,”
2011.
[60]
P. Doll´ar, V. Rabaud, G. Cottrell, and S. Belongie, “Behavior recog-
nition via sparse spatio-temporal features,” in Visual Surveillance
and Performance Evaluation of Tracking and Surveillance, 2005. 2nd
Joint IEEE International Workshop on.
IEEE, 2005, pp. 65–72.
[61]
S. Jain, C. Hu, and J. K. Aggarwal, “Facial expression recognition
with temporal modeling of shapes,” in Computer Vision Workshops
(ICCV Workshops), 2011 IEEE International Conference on.
IEEE,
2011, pp. 1642–1649.
[62]
X. Huang, S. Wang, X. Liu, G. Zhao, X. Feng, and M. Pietikainen,
“Spontaneous facial micro-expression recognition using discrim-
inative spatiotemporal local binary pattern with an improved
integral projection,” arXiv preprint arXiv:1608.02255, 2016.
[63]
Y. Wang, J. See, Y.-H. Oh, R. C.-W. Phan, Y. Rahulamathavan,
H.-C. Ling, S.-W. Tan, and X. Li, “Effective recognition of facial
micro-expressions with video motion magniﬁcation,” Multimedia
Tools and Applications, pp. 1–26, 2016.
[64]
Y. Wang, J. See, R. C.-W. Phan, and Y.-H. Oh, “Lbp with six in-
tersection points: Reducing redundant information in lbp-top for
micro-expression recognition,” in Asian Conference on Computer
Vision.
Springer, 2014, pp. 525–537.
[65]
S. Y. Park, S. H. Lee, and Y. M. Ro, “Subtle facial expression
recognition using adaptive magniﬁcation of discriminative facial
motion,” in Proceedings of the 23rd ACM international conference on
Multimedia.
ACM, 2015, pp. 911–914.
[66]
S. Zhang, B. Feng, Z. Chen, and X. Huang, “Micro-expression
recognition by aggregating local spatio-temporal patterns,” in
International Conference on Multimedia Modeling.
Springer, 2017,
pp. 638–648.
[67]
Y. Zong, X. Huang, W. Zheng, Z. Cui, and G. Zhao, “Learning
a target sample re-generator for cross-database micro-expression
recognition,” in Proceedings of the 2017 ACM on Multimedia Con-
ference.
ACM, 2017, pp. 872–880.
[68]
Y. Zong, W. Zheng, X. Huang, J. Shi, Z. Cui, and G. Zhao, “Do-
main regeneration for cross-database micro-expression recogni-
tion,” IEEE Transactions on Image Processing, vol. 27, no. 5, pp.
2484–2498, 2018.
[69]
S.-T. Liong, J. See, R. C.-W. Phan, K. Wong, and S.-W. Tan, “Hy-
brid facial regions extraction for micro-expression recognition
system,” Journal of Signal Processing Systems, vol. 90, no. 4, pp.
601–617, 2018.
[70]
Y. Zong, X. Huang, W. Zheng, Z. Cui, and G. Zhao, “Learn-
ing from hierarchical spatiotemporal descriptors for micro-
expression recognition,” IEEE Transactions on Multimedia, 2018.
[71]
P. Zhang, X. Ben, R. Yan, C. Wu, and C. Guo, “Micro-expression
recognition system,” Optik-International Journal for Light and Elec-
tron Optics, vol. 127, no. 3, pp. 1395–1400, 2016.
[72]
X. Huang, G. Zhao, X. Hong, W. Zheng, and M. Pietik¨ainen,
“Spontaneous facial micro-expression analysis using spatiotem-
poral completed local quantized patterns,” Neurocomputing, vol.
175, pp. 564–578, 2016.
[73]
X. Ben, P. Zhang, R. Yan, M. Yang, and G. Ge, “Gait recognition
and micro-expression recognition based on maximum margin
projection with tensor representation,” Neural Computing and
Applications, vol. 27, no. 8, pp. 2629–2646, 2016.
[74]
S.-T. Liong, J. See, R. C.-W. Phan, and K. Wong, “Less is more:
Micro-expression recognition from video using apex frame,”
arXiv preprint arXiv:1606.01721, 2016.
[75]
S.-T. Liong, J. See, K. Wong, and R. C.-W. Phan, “Automatic
micro-expression recognition from long video using a single
spotted apex.”
[76]
S.-T. Liong, J. See, R. C.-W. Phan, Y.-H. Oh, A. C. Le Ngo,
K. Wong, and S.-W. Tan, “Spontaneous subtle expression detec-
tion and recognition based on facial strain,” Signal Processing:
Image Communication, vol. 47, pp. 170–182, 2016.
[77]
Y.-H. Oh, A. C. Le Ngo, R. C.-W. Phari, J. See, and H.-C. Ling,
“Intrinsic two-dimensional local structures for micro-expression
recognition,” in Acoustics, Speech and Signal Processing (ICASSP),
2016 IEEE International Conference on.
IEEE, 2016, pp. 1851–1855.
[78]
S.-J. Wang, W.-J. Yan, T. Sun, G. Zhao, and X. Fu, “Sparse tensor
canonical correlation analysis for micro-expression recognition,”
Neurocomputing, vol. 214, pp. 218–232, 2016.
[79]
H. Zheng, X. Geng, and Z. Yang, “A relaxed k-svd algorithm
for spontaneous micro-expression recognition,” in Paciﬁc Rim


## Page 19


PREPRINT SUBMITTED TO IEEE JOURNAL.
19
International Conference on Artiﬁcial Intelligence.
Springer, 2016,
pp. 692–699.
[80]
D. H. Kim, W. J. Baddar, and Y. M. Ro, “Micro-expression recog-
nition with expression-state constrained spatio-temporal feature
representations,” in Proceedings of the 2016 ACM on Multimedia
Conference.
ACM, 2016, pp. 382–386.
[81]
H. Zheng, “Micro-expression recognition based on 2d gabor ﬁlter
and sparse representation,” in Journal of Physics: Conference Series,
vol. 787, no. 1.
IOP Publishing, 2017, p. 012013.
[82]
X. Ben, X. Jia, R. Yan, X. Zhang, and W. Meng, “Learning effective
binary descriptors for micro-expression recognition transferred
by macro-information,” Pattern Recognition Letters, 2017.
[83]
S. Happy and A. Routray, “Fuzzy histogram of optical ﬂow
orientations for micro-expression recognition,” IEEE Transactions
on Affective Computing, 2017.
[84]
X.-l. Hao and M. Tian, “Deep belief network based on double
weber local descriptor in micro-expression recognition,” in Ad-
vanced Multimedia and Ubiquitous Engineering.
Springer, 2017,
pp. 419–425.
[85]
M. Peng, C. Wang, T. Chen, G. Liu, and X. Fu, “Dual temporal
scale convolutional neural network for micro-expression recogni-
tion,” Frontiers in psychology, vol. 8, p. 1745, 2017.
[86]
X. Zhu, X. Ben, S. Liu, R. Yan, and W. Meng, “Coupled source do-
main targetized with updating tag vectors for micro-expression
recognition,” Multimedia Tools and Applications, vol. 77, no. 3, pp.
3105–3124, 2018.
[87]
A. J. Smola and B. Sch¨olkopf, “A tutorial on support vector
regression,” Statistics and computing, vol. 14, no. 3, pp. 199–222,
2004.
[88]
G. McKeown, M. Valstar, R. Cowie, M. Pantic, and M. Schroder,
“The semaine database: Annotated multimodal records of emo-
tionally colored conversations between a person and a limited
agent,” IEEE Transactions on Affective Computing, vol. 3, no. 1, pp.
5–17, 2012.
[89]
S. Happy and A. Routray, “Recognizing subtle micro-facial ex-
pressions using fuzzy histogram of optical ﬂow orientations
and feature selection methods,” in Computational Intelligence for
Pattern Recognition.
Springer, 2018, pp. 341–368.
[90]
Y. LeCun, Y. Bengio, and G. Hinton, “Deep learning,” Nature, vol.
521, no. 7553, pp. 436–444, 2015.
[91]
L. Deng and D. Yu, “Deep learning: Methods and applications,”
Foundations and Trends in Signal Processing, vol. 7, no. 34, pp.
197–387, 2014. [Online]. Available: http://dx.doi.org/10.1561/
2000000039
[92]
Y. LeCun, L. Bottou, Y. Bengio, and P. Haffner, “Gradient-based
learning applied to document recognition,” Proceedings of the
IEEE, vol. 86, no. 11, pp. 2278–2324, 1998.
[93]
C. Szegedy, W. Liu, Y. Jia, P. Sermanet, S. Reed, D. Anguelov,
D. Erhan, V. Vanhoucke, and A. Rabinovich, “Going deeper with
convolutions,” in Proceedings of the IEEE Conference on Computer
Vision and Pattern Recognition, 2015, pp. 1–9.
[94]
A. Krizhevsky, I. Sutskever, and G. E. Hinton, “Imagenet classiﬁ-
cation with deep convolutional neural networks,” in Advances in
neural information processing systems, 2012, pp. 1097–1105.
[95]
S. Ji, W. Xu, M. Yang, and K. Yu, “3d convolutional neural
networks for human action recognition,” IEEE transactions on
pattern analysis and machine intelligence, vol. 35, no. 1, pp. 221–231,
2013.
[96]
A. Karpathy, G. Toderici, S. Shetty, T. Leung, R. Sukthankar, and
L. Fei-Fei, “Large-scale video classiﬁcation with convolutional
neural networks,” in Proceedings of the IEEE conference on Computer
Vision and Pattern Recognition, 2014, pp. 1725–1732.
[97]
J. Yue-Hei Ng, M. Hausknecht, S. Vijayanarasimhan, O. Vinyals,
R. Monga, and G. Toderici, “Beyond short snippets: Deep net-
works for video classiﬁcation,” in Proceedings of the IEEE confer-
ence on computer vision and pattern recognition, 2015, pp. 4694–4702.
[98]
D. Tran, L. Bourdev, R. Fergus, L. Torresani, and M. Paluri,
“Learning spatiotemporal features with 3d convolutional net-
works,” in Proceedings of the IEEE International Conference on
Computer Vision, 2015, pp. 4489–4497.
[99]
M. J. Lyons, S. Akamatsu, M. Kamachi, J. Gyoba, and J. Budynek,
“The japanese female facial expression (jaffe) database,” in Pro-
ceedings of third international conference on automatic face and gesture
recognition, 1998, pp. 14–16.
[100] M. H. Yap, H. Ugail, and R. Zwiggelaar, “Facial behavioral
analysis: A case study in deception detection,” British Journal of
Applied Science & Technology, vol. 4, no. 10, p. 1485, 2014.
[101] L. Breiman, “Random forests,” Machine learning, vol. 45, no. 1, pp.
5–32, 2001.
[102] T. Kanade, J. F. Cohn, and Y. Tian, “Comprehensive database
for facial expression analysis,” in Automatic Face and Gesture
Recognition, 2000. Proceedings. Fourth IEEE International Conference
on.
IEEE, 2000, pp. 46–53.
[103] C. Harris and M. Stephens, “A combined corner and edge detec-
tor.” in Alvey vision conference, vol. 15, no. 50.
Citeseer, 1988, pp.
10–5244.
[104] D. K. Jain, Z. Zhang, and K. Huang, “Random walk-based feature
learning for micro-expression recognition,” Pattern Recognition
Letters, 2018.
[105] P. Baldi, S. Brunak, Y. Chauvin, C. A. Andersen, and H. Nielsen,
“Assessing the accuracy of prediction algorithms for classiﬁca-
tion: an overview,” Bioinformatics, vol. 16, no. 5, pp. 412–424, 2000.
[106] P. Ekman and W. V. Friesen, Facial Action Coding System: Investi-
gator’s Guide.
Consulting Psychologists Press, 1978.
[107] W.-J. Yan, S.-J. Wang, Y.-J. Liu, Q. Wu, and X. Fu, “For micro-
expression recognition: Database and suggestions,” Neurocomput-
ing, vol. 136, pp. 82–87, 2014.
[108] A. K. Davison, W. Merghani, and M. H. Yap, “Objective
classes for micro-facial expression recognition,” arXiv preprint
arXiv:1708.07549, 2017.
[109] A. K. Davison, “Micro-facial movement detection using spatio-
temporal features,” Ph.D. dissertation, Manchester Metropolitan
University, 2016.
[110] A. Moilanen, G. Zhao, and M. Pietikainen, “Spotting rapid
facial movements from videos using appearance-based feature
difference analysis,” in Pattern Recognition (ICPR), 2014 22nd
International Conference on, Aug 2014, pp. 1722–1727.
[111] Z. Xia, X. Feng, J. Peng, X. Peng, and G. Zhao, “Spontaneous
micro-expression spotting via geometric deformation modeling,”
Computer
Vision
and
Image
Understanding,
2015.
[Online].
Available:
http://www.sciencedirect.com/science/article/pii/
S1077314215002702
[112] D. Patel, G. Zhao, and M. Pietik¨ainen, “Spatiotemporal integra-
tion of optical ﬂow vectors for micro-expression detection,” in
Advanced Concepts for Intelligent Vision Systems.
Springer, 2015,
pp. 369–380.
[113] A. K. Davison, M. H. Yap, and C. Lansley, “Micro-facial move-
ment detection using individualised baselines and histogram-
based descriptors,” in Systems, Man, and Cybernetics (SMC), 2015
IEEE International Conference on.
IEEE, 2015, pp. 1864–1869.
[114] M. Shreve, J. Brizzi, S. Feﬁlatyev, T. Luguev, D. Goldgof, and
S. Sarkar, “Automatic expression spotting in videos,” Image and
Vision Computing, vol. 32, no. 8, pp. 476 – 486, 2014.
[115] M. D. Zeiler and R. Fergus, “Visualizing and understanding con-
volutional networks,” in European conference on computer vision.
Springer, 2014, pp. 818–833.
[116] B. Schuller, B. Vlasenko, F. Eyben, M. Wollmer, A. Stuhlsatz,
A. Wendemuth, and G. Rigoll, “Cross-corpus acoustic emotion
recognition: Variances and strategies,” IEEE Transactions on Affec-
tive Computing, vol. 1, no. 2, pp. 119–131, 2010.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1805_02397v1_a_review_on_facial_micro_expressions_analysis_datasets_features_and_metrics
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2018/1805_02397V1_A_REVIEW_ON_FACIAL_MICRO_EXPRESSIONS_ANALYSIS_DATASETS_FEATURES_AND_METRICS.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
canon-group: reference
rscf-state: source-claim
arxiv_id: 2409.10230v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 2409.10230v1_Speech as a Biomarker for Disease Detection

> Source: 2409.10230v1_Speech as a Biomarker for Disease Detection.pdf

> Pages: 25

---


## Page 1


1
Speech as a Biomarker for Disease Detection
Catarina Botelho†, Alberto Abad†, Tanja Schultz‡ and Isabel Trancoso†
†INESC-ID & Instituto Superior Técnico, University of Lisbon, Portugal
‡Cognitive Systems Lab (CSL), University of Bremen, Germany
{catarina.t.botelho,alberto.abad,isabel.trancoso}@inesc-id.pt,tanja.schultz@uni-bremen.de
Abstract—Speech is a rich biomarker that encodes substantial
information about the health of a speaker, and thus it has
been proposed for the detection of numerous diseases, achieving
promising results. However, questions remain about what the
models trained for the automatic detection of these diseases are
actually learning and the basis for their predictions, which can
significantly impact patients’ lives. This work advocates for an
interpretable health model, suitable for detecting several diseases,
motivated by the observation that speech-affecting disorders
often have overlapping effects on speech signals. A framework
is presented that first defines "reference speech" and then
leverages this definition for disease detection. Reference speech is
characterized through reference intervals, i.e., the typical values
of clinically meaningful acoustic and linguistic features derived
from a reference population. This novel approach in the field
of speech as a biomarker is inspired by the use of reference
intervals in clinical laboratory science. Deviations of new speakers
from this reference model are quantified and used as input to
detect Alzheimer’s and Parkinson’s disease. The classification
strategy explored is based on Neural Additive Models, a type
of glass-box neural network, which enables interpretability. The
proposed framework for reference speech characterization and
disease detection is designed to support the medical community
by providing clinically meaningful explanations that can serve as
a valuable second opinion.
Index Terms—Alzheimer’s Disease, Automatic disease detec-
tion, Interpretability, Neural Additive Models, Parkinson’s Dis-
ease, Reference intervals, Reference Speech, Speech.
I. INTRODUCTION
Overburdened health systems worldwide face numerous
challenges, exacerbated by an aging population. Speech, a rich
and ubiquitous biomarker, allied with highly accurate machine
learning systems, offers the potential for low-cost, widespread
detection of several diseases. This potential stems from the
involvement of the respiratory, nervous, and muscular systems
in speech production. This implies that disruptions in any of
these systems can perturb the speech signal. Consequently,
speech can encode information indicative of diseases affecting
these systems, going beyond the so-called speech and language
disorders (e.g. sigmatism, stuttering), and including1 neurode-
generative diseases, such as Parkinson’s Disease (PD) [2]–
[4], Alzheimer’s Disease (AD) [5]–[8], and Multiple Scle-
rosis [9]; psychiatric disorders such as depression [3], [10],
and schizophrenia [11]; and diseases that concern respiratory
organs, such as Obstructive Sleep Apnea (OSA) [12], [13], and
COVID-19 [14]. Beyond the mentioned examples, there is a
1The following categories do not constitute a formal classification. For an
official categorization, refer to the International Classification of Diseases,
11th Revision (ICD-11) [1].
vast literature on automatic classification systems leveraging
speech to perform the binary classification of healthy controls
and each of these diseases, reporting very promising results.
In real scenarios however, these diseases often co-exist.
The coexistence of two or more chronic conditions in the
same individual, or multimorbidity, has been rising in preva-
lence over recent years [15]–[17]. The World Health Orga-
nization emphasizes that healthcare of people with multiple
conditions should be provided by medical generalists who
combine a community base and comprehensive clinical skills
with “interpretive medicine”, integrating multiple sources of
knowledge with individual needs assessment [15]. Likewise,
we hypothesize that a speech-based tool to support medical
diagnosis and monitoring of chronic conditions should adopt
a holistic approach, facilitating the interpretative assessment
of multiple diseases. This is relevant, as some diseases are
risk factors for others, and their effects on speech signals
can overlap. Moreover, the ongoing diversification of medical
disciplines increases the difficulty of identifying all diseases
for a single specialist. This further underscores the need for
a comprehensive, speech-based diagnostic tool that can assist
in the identification and monitoring of multiple conditions.
However, existing datasets for disease detection are often
small and labeled only for individual diseases. The naive
combination of different datasets containing recordings from
individuals with a single specific disease to perform a cross-
corpora study for multi-disease classification can result in un-
reliable results that would not generalize to unseen recording
conditions [8], [18]. It has also been established that small
datasets may lead to overoptimistic estimation of performance,
with models learning confounding variables and overfitting to
the dataset [19]. In light of the aforementioned considerations,
we claim that a valuable step towards the adoption of speech
and language technologies in real health applications would be
to obtain a definition of reference speech that could be used
independently of the dataset of origin, and subsequently be
applied for the identification of disease signatures.
In this study, reference speech refers to the speech charac-
teristics common to a reference population, ideally comprising
healthy individuals of varying ages and biological sexes.
Acknowledging the challenges of defining health and the
prevalence of subclinical disease2, we do not assert that our
reference population consists exclusively of healthy speakers.
2Unlike a clinical disease which has identifiable signs and symptoms, a
subclinical disease lacks recognizable clinical findings. Many diseases (e.g.
diabetes) often remain subclinical before manifesting clinically [20].
arXiv:2409.10230v1  [eess.AS]  16 Sep 2024


## Page 2


2
Instead, we utilize the speech of individuals who self-report
as disease-free.
We propose to characterize reference speech through ref-
erence intervals (RIs) of clinically meaningful speech and
language features. RIs represent the typical range of values
for specific parameters within a reference population. In this
context, RIs are computed as the 2.5th and 97.5th percentiles
of the distribution of each parameter within the reference
population. Ideally, the speech characteristics of an unseen
healthy individual should fall within the RIs derived from the
reference population. The concept of RIs is commonly applied
in clinical laboratory science to interpret laboratory results and
assess individual health. The idea of characterizing reference
speech using reference intervals was first introduced in our
previous work [21].
The definition of reference speech is subsequently used
to perform the detection of speech affecting diseases. Each
disease detection task is formulated as a binary classification
problem (patients versus controls) and addressed using Neural
Additive Models (NAMs) [22]. These are interpretable neural
networks that provide an insight into the decision process,
which can be of utmost importance in the medical domain,
especially to avoid the models learning spurious correlations.
While the proposed framework is designed to be suitable
for different speech affecting diseases, we showcase it for AD
and PD due to the availability of public datasets annotated for
each of these diseases. This work presents a unified framework
with distinct models for disease detection. In the future, this
framework could enable the simultaneous detection of multiple
diseases, provided that datasets with similar tasks collected
under comparable conditions are available.
The primary contributions of this research are: (1) an
overview of the most notorious effects on speech commonly
associated with frequently studied speech-affecting diseases,
along with their mediating mechanisms, highlighting the im-
portance of a holistic perspective of speech as a biomarker for
health; (2) a framework for defining reference speech building
on our prior work [23]; and (3) the application of NAMs
for the detection of speech-affecting diseases, leveraging the
reference speech definition and providing interpretable deci-
sions. These contributions are foundations to our overall vision
that goes beyond the experiments described in this work, and
advocates for the usage of speech as a biomarker for health
monitoring in general, rather than focusing on single diseases.
The rest of this document is organized as follows. Section II
discusses challenges in the current state of the art on the de-
tection of speech affecting diseases, particularly their partially
overlapping manifestations on speech, and the overoptimistic
performance estimates in the literature. Section III presents
related work on characterizing healthy speech, and on refer-
ence interval estimation. Section IV introduces the corpus that
constitutes the reference population for RI estimation, and the
corpora used for disease detection. Section V dives into the
first stage of this work, the definition of reference speech,
describing the methodology and presenting the results. Sec-
tion VI presents the methodology and the results for the second
stage of this work, where the definition of reference speech
is leveraged for the detection of AD and PD. Section VII
discusses the limitations of our approach. Finally, section VIII
presents the main conclusions. Further details are provided in
the appendices and in [24].
II. CHALLENGES IN THE AUTOMATIC DETECTION OF
SPEECH AFFECTING DISEASES
A. Overlapping manifestations in speech and multimorbidity
The diagram in Fig. 1 illustrates several speech affecting dis-
eases, the mechanisms through which they impact the speech
signal, and examples of speech features that capture such
alterations. This figure is not exhaustive but aims to provide
an overview of the most notable speech effects associated
with these diseases. Some of the references depicted in this
figure provide very complete overviews on the use of speech
analysis for the detection of some of these diseases. For
example, Boschi et al. [58] provided an exhaustive review on
the use of spontaneous speech tasks to characterize language
disorders in prevalent neurodegenerative diseases. Hecker et
al. [44] systematically reviewed voice analysis for recogniz-
ing neurological and psychiatric diseases. Voleti et al. [25]
reviewed speech and language features for cognitive and
thought disorder analysis. Cummins et al. [59] described the
impact of depression and suicidality on paralinguistic speech
characteristics and their application in classification systems.
Ma et al. [41] discussed voice changes in PD patients, linking
these changes to physiological and anatomical characteristics.
Deshpande and Schuller [60] provided an overview of COVID-
19 screening and monitoring through speech and other human
generated audio signals, also reviewing relevant research on
respiratory conditions such as asthma and OSA.
However, to the best of our knowledge, no existing works
systematize the overlapping effect of multiple diseases in
speech together with the main mediating mechanisms. Our di-
agram represents an effort in this direction, aiming to enhance
the understanding of how speech could serve as a biomarker
for multidisease detection. Singh [36] defends that causal
relationships between parameters and voice must be sought,
or reasonably guessed, and then features should be selected
to capture these causal relationships. This diagram facilitates
such reasoning. For instance, if COVID-19 is hypothesized
to cause vocal fold inflammation due to repetitive coughing,
features that capture such inflammation should be derived to
predict COVID-19. Furthermore, when studying a different
disease not included in the diagram, one can consider whether
it shares any listed mechanisms, such as association with over-
weight or reduced lung capacity, to anticipate potential speech
alterations. It should be emphasized that most mechanisms il-
lustrated are hypotheses presented in the literature and may not
be present in all cases. Further research and multidisciplinary
discussion are needed to validate these hypotheses.
In the diagram, it is notorious that the impact of certain
diseases on the speech signal may overlap with that of other
diseases. For example, both depression and PD are associated
with psychomotor retardation, and thus have similar manifes-
tations on the speech signal. It also becomes clear that often
these speech features that capture speech alterations are non
specific for a single disease, and thus, when considered alone,


## Page 3


3
Fig. 1.
Examples of mechanisms through which speech affecting diseases impact the speech signal. The diagram includes references [9], [25]–[56].
(*) articulation rate and pauses have been reported to be associated with depression, via psychomotor retardation, however, although psychomotor retardation is
also present in PD, these features have inconsistent reports for PD [57]. (**) Disturbed nasalization, as a consequence of impaired velum control, is associated
with PD via psychomotor retardation and with OSA. In PD an increase in nasal airflow is reported [52], while for OSA, a smaller difference between nasal
and oral sounds is reported [49].
may be insufficient for the automatic detection of diseases.
F0 based features, for instance, appear to be altered as a
result of several diseases, not to mention possible alterations
associated with healthy aging [36], or even healthy changes
across the menstrual cycle in fertile women [61]. It is also
important to refer that some of the features depicted in the
diagram have had inconsistent reports in the literature. For
example, voicing onset time (VOT) has been found both higher
and lower in people suffering from PD when compared with
healthy controls [62]. The frequencies of formants have also
been inconsistently reported to change with depression [40].
Furthermore, there are many other factors that directly or
indirectly impact the speech production process, and thus
introduce alterations on the speech signal. Some of these
factors include medication [41], [63], [64], or other medical
interventions, emotions or mental states.
Besides the fact that these diseases have overlapping effects
on the speech signal, it is important to note that they are
often considered risk factors for each other, and thus are
likely to co-exist. PD and AD, for instance, are risk factors
for depression, and the converse is also true [34], [65]. OSA
is also associated with depression, potentially mediated by
disturbed sleep patterns and obesity, a major risk factor for
OSA. Additionally, OSA is linked to cognitive impairments,
possibly due to repetitive hypoxemia [66].
B. Data scarcity
Despite promising results, the literature on disease detection
from voice and language analysis often reports overoptimistic
findings. Berisha et al. [19] found that smaller sample sizes
are associated with inflated accuracy in dementia detection
from speech, suggesting publication bias and overfitting. In a
recent survey talk3, Cummins has also referred to this problem
and cautioned against the Clever Hans Effect in this context.
Ozbolt et al. [67] identified several methodological issues that
could lead to overoptimistic results in classifying PD patients
and healthy controls using sustained vowels, including age-
unmatched classes, large feature vectors, and data leakage
between train and test sets. Espinoza et al. [68] highlighted two
main limitations in OSA detection from speech analysis: the
influence of confounding factors (e.g., age, height, sex), and
overfitting of feature selection and validation methods when
working with a high dimensional feature set compared to the
number of samples.
The frequently reported overoptimistic results due to con-
founding factors and overfitting on small datasets, call for
more trustworthy research on the use of speech as a biomarker
for disease detection. Namely, using interpretable models
may represent a step towards assuring that the models are
learning properties indeed attributable to the disease, and not
confounding factors.
Our previous work [69] observed the consequences of un-
expected confounding factors, specifically how the bandwidth
of the speech signal affected the ComParE 2021 challenge
corpus for COVID-19 detection [70], questioning the validity
of black-box classifiers. Another study [18] found that standard
features for disease detection contain substantial information
about recording conditions, enabling both supervised and
unsupervised detection of the source dataset.
3N. Cummins. Machine Learning for Speech-based Health Analysis: State-
of-the-art and Future Challenges. Survey talk at Interspeech 2022 https://www.
interspeech2022.org/program/surveytalk.php


## Page 4


4
III. RELATED WORK
A. Characterizing reference speech
Some researchers have delved into characterizing features in
the context of healthy speech, providing means and standard
deviations. Teixeira and Fernandes [71] studied jitter, shimmer,
and harmonics-to-noise ratio (HNR) in 34 female and 7
male speakers, focusing on sustained vowels /a/, /i/, and /u/
at various tones. No other acoustic features were included
in this study. Shivkumar et al. [72] proposed a toolkit for
extracting clinically meaningful linguistic features, and present
statistics for these features for the healthy speakers in the AMI
meeting corpus [73]. This study, however, did not include any
acoustic feature, since its purpose was to illustrate the toolkit.
Hence, the aim of these two studies was not to define or
comprehensively characterize reference speech.
Schwoebel et al. [74], on the other hand, introduced the
Voiceome Protocol and the corresponding Voiceome Dataset
as standards to characterize healthy speech. The authors re-
ported means and standard deviations for several acoustic and
linguistic features, broken down by age range and gender, on
their GitHub4, though the dataset is not publicly available.
B. Reference intervals in clinical laboratory science
Reference intervals (RIs) are crucial in clinical laboratory
science for interpreting quantitative pathology results, such as
those from hematology tests [75]. RIs, defined by a lower and
upper reference limit, represent the expected range of values
in a reference population [76]. Laboratory results outside the
RI do not necessarily imply disease but indicate the need for
further medical evaluation [76].
The traditional, or direct approach, for determining RIs
involves selecting a reference population (minimum of 120
individuals per partition, e.g. sex, age range) respecting pre-
defined criteria, collecting samples for that population, per-
forming statistical evaluation using non parametric methods
and outlier removal, and estimating the RI between the two
reference limits [77]. This method faces challenges such as
defining health, the presence of subclinical disease, and selec-
tion bias associated with small cohorts [75]. Further guidelines
can be found in [77].
An alternative approach, known as the indirect approach,
mines data from existing pathology databases, i.e., it is based
on laboratory results collected for other purposes, usually for
routine clinical care. These databases include results from dis-
eased patients but also from healthy subjects, allowing for the
extraction of the underlying reference distributions [76]. This
approach is faster, cheaper, avoids patient inconvenience, and
circumvents ethical issues related to informed consent from
vulnerable populations [75], [78], while providing extensive
data for analysis. However, the presence of diseased sub-
populations can influence RIs, and at least 400 subjects per
partition are recommended [75].
While guidelines favor the direct approach [77], the indirect
approach is increasingly popular, especially in pediatric and
geriatric populations where data sampling is more challenging.
4https://github.com/jim-schwoebel/voiceome
If the underlying distribution of the data in the reference
population is Gaussian, the reference limits that constitute
the RI corresponds to the mean ± 1.96 × std, in which std
stands for standard deviation [79]. If such assumption cannot
be made, which is frequently the case for the studies of RI
estimation, either data must be first transformed to a Gaussian
distribution, e.g. using a Box-Cox power transformation, or
a non-parametric estimation can be made. In the case of a
non-parametric estimation, the limits of the RI correspond to
the 2.5th and 97.5th percentile [79]. Both the non-parametric
approach and the power transformation of data followed by
the parametric approach provide similar results according to
[79], but the non-parametric method is recommended in some
studies [77].
IV. CORPORA
The analysis conducted in this work can be subdivided into
two main stages: first, the definition of reference speech, and
second, leveraging this definition to perform the detection of
speech affecting diseases. Each stage demands for specific
data. Below, we introduce the corpora used for this study.
A. Reference Population Data
Aligned with the indirect approach for estimating RIs de-
scribed in Section III, in this study, the reference popula-
tion used to derive RIs was sourced from already existing
databases. Since routine pathology databases typically lack
speech recordings, we used the the Crowdsourced Language
Assessment Corpus (CLAC) [80], a corpus spoken in En-
glish, created to provide a collection of audio samples from
healthy speakers. CLAC includes speech from 1,832 speakers,
claiming to have no health-related symptoms that might affect
their speech. Besides presumably having a low incidence of
unhealthy subjects, and including standard speech tasks for
disease detection, CLAC offers the advantage of being larger
than other publicly available speech corpora in the field that
studies speech as a biomarker.
The subsets of the corpus used in this study include two
picture description tasks (Cookie Theft picture and Picnic
picture), and a sustained vowel task (/a/). The 13 speakers that
identify as "other" in terms of gender were excluded from the
analysis because the sample size was too small. Information
on the gender and age of the included speakers is provided
later on, in Table II.
Although integrating multiple datasets would be ideal, this
study focuses on picture description and sustained vowel tasks
to enable comparison with publicly available datasets for
Alzheimer’s disease and Parkinson’s disease detection. To the
best of our knowledge, no other publicly available datasets
include these tasks with healthy speakers, or speakers claiming
to be disease-free.
B. Datasets for disease detection
Two additional datasets were used to investigate disease
detection and to conduct a comparative analysis with the ref-
erence speech. The datasets employed were ADReSS [81] and


## Page 5


5
Fig. 2. Overview of the steps entailed for reference speech characterization.
PC-GITA [82], for the analysis of Alzheimer’s and Parkinson’s
disease, respectively.
ADReSS comprises speech recordings of 156 subjects de-
scribing the Cookie Theft picture, 78 controls and 78 AD
patients, matched for age and gender. This dataset is a sub-
set of the Pitt corpus [83] curated for the 2020 ADReSS
Challenge [81]. Although the audios released in the ADReSS
challenge were acoustically enhanced, the experiments con-
ducted used the original version made available in the Pitt
Corpus [83]. The interviewers’ interventions were removed,
using the annotations provided in the manual transcriptions.
The Parkinson’s disease corpus from the Applied Telecom-
munications Group (PC-GITA) includes recordings of 100
subjects, 50 PD patients, and 50 controls matched by age and
gender. The corpus is spoken in Colombian Spanish, and the
recordings were captured in noise controlled conditions. To
allow a fair comparison with the reference intervals determined
for an English speaking reference population, the only task ex-
plored in this work is the enunciation of a sustained vowel /a/
(three repetitions per subject). PC-GITA was made available
for the 2015 ComParE challenge [84], for the assessment of
PD severity.
V. REFERENCE SPEECH CHARACTERIZATION (RSC)
This section describes our proposed approach to character-
ize reference speech by defining reference intervals for a set of
literature-informed, knowledge-based features. This method is
inspired by the indirect approach for RI estimation, described
in section III.
A. Reference Speech Characterization Pipeline
The definition of reference speech started by a pre-
processing step which included Automatic Speech Recognition
(ASR) or vowel segmentation whenever appropriate (step 1).
This step was followed by the extraction of interpretable
acoustic and linguistic features (step 2), and by the removal
of outliers (step 3). Subsequently, we assessed the necessity
of partitioning the reference population based on gender, age
ranges, or speech tasks (step 4). The RIs for each feature
were then established using the refined reference population
(step 5). Additionally, a dimensionality reduction strategy was
investigated to enhance interpretability (step 6). Fig. 2 presents
an overview of these steps. The method follows our previous
work [23], with some enhancements in each step, and with the
addition of step 6.
Step 1. Data pre-processing
The data pre-processing step involves the application of dif-
ferent sub-steps depending on the nature of the speech task.
If the task involves a sustained vowel, vowel segmentation is
employed. Conversely, for spontaneous speech tasks, ASR is
applied.
Vowel segmentation: Due to its crowdsourced nature,
CLAC includes recordings with anomalies, particularly in
sustained vowels (e.g., low energy, gain decrease due to
unrecognized speech). To improve the overall quality of the
recordings that constitute the reference population, data fil-
tering was performed to remove or segment sustained vowel
recordings from CLAC, as detailed in Appendix A.
Automatic speech recognition: The extraction of linguis-
tic features required transcriptions of the speech recordings.
Unlike previous studies optimizing ASR systems for indi-
viduals with Parkinson’s or Alzheimer’s disease (e.g., [85]),
this study adopted a zero-shot approach suitable for the
general population and various speech-affecting diseases. Our
previous analysis in [86], which compared five state-of-the-art
ASR systems (wavlm-libri-clean-100h-large [87], wav2vec2-
large-960h [88], wav2vec2-large-robust-ft-swbd-300h [89],
wav2vec2-large-xlsr-53-english [90], whisper-large [91]), con-
cluded that whisper-large (henceforth referred to as whisper)
achieves the lowest word error rate (26.9%) on ADReSS,
likely due to its training on 680,000 hours of supervised data
from the web [91]. Therefore, our analysis was conducted
based on whisper transcriptions. However, whisper often out-
puts transcriptions cleaner than the actual audio in terms of
fluency, namely by removing fillers or repetitions, which may
encode relevant information for studying cognitive impair-
ment. Therefore, additional experiments were conducted on
the second-best model, wav2vec2-large-robust-ft-swbd-300h,
which retains such disfluencies but sometimes produces non-
existent words, potentially affecting downstream tasks. The
results of these experiments are reported in the appendices.
It is noteworthy that whisper’s training data has not been
disclosed, raising the possibility that datasets such as ADReSS
and CLAC may have been seen during training.
Step 2. Feature Extraction
Singh [36] distinguishes three processes for computational
profiling of humans from their voice: knowledge-driven, data
driven, or a combination of both. This work explores the
latter. The mechanisms through which the different diseases
impact speech, summarized in Fig. 1, motivated the definition
of a knowledge-driven feature set containing 41 interpretable


## Page 6


6
TABLE I
DESCRIPTION OF THE FEATURES USED. OBSERVATIONS: IN RHYTHM-RELATED FEATURES, WHEN THE DESCRIPTIONS REFER TO THE TOTAL TIME, IT
ASSUMES THAT SILENCES BEFORE THE START AND AFTER THE END OF THE SPEECH SIGNAL WERE REMOVED, UNLESS EXPLAINED OTHERWISE. TTR
STANDS FOR TYPE-TO-TOKEN RATIO, AND HNR TO HARMONICS-TO-NOISE RATIO.
Category
Feature Name
Functional
Method
Description
Content density
–
BlaBla
Proportion of number of open class words, i.e. nouns, verbs, adjectives and adverbs, to
the number of close class words, i.e. determiners, pronouns, conjunctions and preposi-
tions [72].
Idea density
–
BlaBla
Proportion of verbs, adjectives, adverbs, prepositions and conjunctions to all words across
sentences [72].
Honoré statistic
–
BlaBla
Calculated as (100 ∗log(N))/(1 −(V 1)/(V )), where V is number of unique words,
V 1 is the number of words in the vocabulary only spoken once, and N is overall text
length [72].
Brunet’s Index
–
BlaBla
Calculated as N(V −0.165), where V is number of unique words and N is overall text
length. Measures the lexical richness. It is a version of TTR, insensitive to text-length [72].
TTR
–
BlaBla
The number of word types divided by the number of word tokens [72] .
Discourse marker
rate
–
BlaBla
The rate of discourse markers across all sentences [72] (eg. "so, ok, anyway, right" [92]).
Polarity
–
TextBlob
Varies between [−1, 1], where −1 defines a negative sentiment and 1 defines a positive
sentiment.
Content
Repetition ratio
–
dedicated
script
Number of repeated words over total number of words
First person
pronouns
–
dedicated
script
Ratio of number of personal pronouns ("i", "me", "mine", "my"), to the text length.
Coherence
mean, variability
cosine
similarity
Cosine similarity between sentence embeddings of adjacent text segments (14 tokens),
computed with the pretrained sentence-transformer model all-mpnet-base-v2. (More details
in the text.)
Coreference chain
ratio
–
wl-coref
Number of coreference chains over text length.
Ambiguous
coreference chain
–
wl-coref
Number of coreference chains that start with a third-person pronoun over the number of
coreference chains.
Speech rate
–
praat
Approximated number of syllables over total time [93].
Articulation rate
–
praat
Approximated number of syllables over phonation time [93].
Average syllable
duration
–
praat
Average syllable duration [93].
Mean pause dura-
tion
–
praat
Mean duration of silence segments, excluding silences before and after speech, motivated
by [94].
Rhythm
Mean speech dura-
tion
–
praat
Mean duration of speech segments [94].
Silence rate
–
praat
Total silence time over total time, motivated by [94].
Silence-to-speech
ratio
–
praat
Number of silent segments over the number of speech segments, motivated by [94].
Mean silence count
–
praat
Number of silence segments over total time, motivated by [94]].
F0
mean, std
praat
Fundamental frequency of vibration of the vocal folds.
HNR
–
praat
Compares the energy in the harmonics to the energy in the non-harmonic (noisy)
components of the speech signal [36].
local Jitter
–
praat
Jitter refers to cycle-to-cycle perturbations of F0 in frequency. Speech with high jitter
is perceived as roughness [36]. Local jitter is the average absolute difference between
consecutive periods, divided by the average period [95], measured in %.
local absolute Jitter
–
praat
Average absolute difference between consecutive periods, measured in seconds [95].
Voice
quality
RAP Jitter
–
praat
Relative average perturbation - the average absolute difference between a period and the
average of it and its two neighbours, divided by the average period [95].
ppq5 Jitter
–
praat
Five-point Period Perturbation Quotient – same as RAP jitter but based but computed with
it and its four closest neighbours [95].
local Shimmer
–
praat
Shimmer refers to cycle-to-cycle variation of F0 in amplitude. Speech with high shimmer
is perceived as buzzing [36]. Local shimmer is the average absolute difference between
the amplitudes of consecutive periods, divided by the average amplitude [95], measured
in %.
local db Shimmer
–
praat
Average absolute base-10 logarithm of the difference between the amplitudes of consec-
utive periods, multiplied by 20 [95].
apq3 Shimmer
–
praat
Three-point Amplitude Perturbation Quotient – average absolute difference between the
amplitude of a period and the average of the amplitudes of its neighbours, divided by the
average amplitude [95].
aqpq5 Shimmer
–
praat
Five-point Amplitude Perturbation Quotient – same as apq3, but computed with it and its
four closest neighbours [95].
apq11 Shimmer
–
praat
11-point Amplitude Perturbation Quotient – same as apq3, but computed with it and its
ten closest neighbours [95].
F1
mean, median
praat
Formants occur around frequencies that correspond to the resonances of the vocal tract.
First formant frequency – relates to the shape of the area behind the tongue (on the throat).
If the ressonator has a small area, then the formant frequency should be higher.
Vocal
tract
F2
mean, median
praat
Second formant – relates to the shape of the area from the hump of the tongue to the tip
of the lips
F3
mean, median
praat
Third formant.
F4
mean, median
praat
Fourth formant.


## Page 7


7
features. Later, feature selection was conducted using a data
driven approach. This knowledge driven feature set contains
both acoustic (28) and linguistic (13) features which are thor-
oughly described in Table I. We group the features into four
categories: content-, rhythm-, voice quality- and vocal tract
shape-related features. Content-related features were derived
from automatically generated transcriptions. While the analy-
sis of the picture description task encompassed all features, the
analysis of sustained vowels was solely based on voice-quality
and vocal-tract related features.
Different methods were used to extract the features, as listed
in Table I. The content-related features were extracted using
the BlaBla toolkit [72], dedicated scripts, or pretrained models.
The coherence features were based on the cosine similar-
ity between sentence embeddings of adjacent text segments,
computed with the pretrained sentence-transformer model all-
mpnet-base-v25. At the time this work was conducted, this
model, trained with over 1 billion training pairs, provided the
state of the art on the Sentence Embeddings Benchmark [96].
The embeddings were extracted for chunks of 14 tokens. The
choice of 14 tokens was rooted on two reasons: (i) in CLAC,
in the task where subjects describe the cookie theft picture,
the average number of words per sentence in the provided
transcriptions was 15, and in the task where subjects are
describing the picnic picture, the average number of words per
sentence is 13 words; and (ii) according to the [97], readers
understand over 90% of the information when sentences have
14 words. After computing the cosine similarity of adjacent
sentences, the mean and the variance are computed for the
entire picture description. This measure of coherence was
based on the incoherence model, described in [26] and [27] for
the assessment of speech of subjects suffering from psychosis
and schizophrenia. The use of the variance was inspired in the
concept of ongoing semantic variability, proposed by [28] as
a text-level semantic marker of Alzheimer’s Disease.
Ambiguous coreference chains are sequences of words or
phrases in a text that refer to the same entity or concept,
which start with an ambiguous pronoun. Ambiguous pronouns
refer to entities not explicitly mentioned or mentioned only
cataphorically, i.e., after the pronoun. The usage of ambiguous
pronouns, or referential incoherence, is a common pattern in
incoherent speech. The usage of ambiguous pronouns was
captured following the approach of [27]: (1) a pretrained
coreference resolver extracts the reference chains (i.e., the lists
of terms that should refer to the same entity), and (2) if the
first term in the reference chain is a third-person pronoun (he,
she, they, etc.), then it is considered an ambiguous pronoun.
The pretrained coreference resolver was the wl-coref6 [98],
that detained the state of the art on the CoNLL-2012 Shared
Task7 [99] at the time this work was conducted. The entire
transcription of the picture description was used to compute
this feature.
The remaining three feature categories – rhythm, voice
quality, and vocal tract shape – were derived directly from the
5available at https://www.sbert.net/docs/pretrained_models.html
6available at https://github.com/vdobrovolskii/wl-coref.
7score
board
available
at
http://nlpprogress.com/english/coreference_
resolution.html.
TABLE II
NUMBER OF AUDIO FILES AND SPEAKERS, AND AVERAGE FILE DURATION
IN THE REFERENCE POPULATION, PER SPEECH TASK, AND BY GENDER
AND AGE RANGE, AFTER VOWEL SEGMENTATION AND OUTLIER
REMOVAL.
CLACpicture
CLACvowel
All
Files
Speakers
Files
Speakers
Files
Speakers
Count
M
<50
1115
772
1040
598
2155
782
M
≥50
142
104
133
77
275
106
F
<50
1081
749
1044
641
2125
756
F
≥50
188
139
179
113
367
140
All
2526
1764
2396
1429
4922
1784
Average duration ± standard deviation (s)
All
38 ± 22
–
3 ± 1
–
–
–
audio samples, using Praat [100], through the Python package
praat-parselmouth [101]. Praat was chosen for its frequent use
in clinical practice.
Step 3. Outlier Removal
The identification of outliers in the reference population, i.e.,
samples that differ substantially from the other observations,
was based on the Mahalanobis distance [102] to the mean
of the population, an approach well-suited for multivariate
data. The cutoff threshold was set to three times the standard
deviation from the mean of the Mahalanobis distance. This
analysis was conducted separately for the picture description
and the sustained vowel tasks, using rhythm, voice-quality,
and vocal-tract related features. Content features were not
considered to ensure that results are independent of the ASR
model.
Approximately 1% of the audio samples in CLAC were
considered outliers. By excluding these samples, we expect to
exclude bad quality audios and possibly samples from speakers
affected by subclinical diseases. Table II presents the number
of audio samples and speakers in the reference population for
each speech task after outlier removal.
Step 4. Reference population partition
Most features in the feature set are strongly influenced by
various factors, such as recording conditions [103]–[105] and
speaker dependent attributes, including gender, age, body mass
index, accent, education, smoking habits, etc. The features may
also exhibit substantial differences depending on the speech
task (e.g. in spontaneous versus read speech). These factors
could have a more substantial impact on the speech signal
than speech-affecting diseases, potentially biasing results. It
becomes important to determine whether different RIs should
be estimated for different ranges of each of these factors.
Our previous work [21] analysed when to partition the
reference population and derive different RIs, based on gender,
age range (above and below 50 years old), and speech task.
This analysis involved assessing the statistical significance of
differences between subgroups, by employing Mann-Whitney
U tests [106]. The study recommended deriving distinct RIs
for different genders and speech tasks. While different RIs for
various age ranges are ideal, the data was deemed insufficient.
Furthermore, to compare data from different source datasets,
it is recommended that datasets be normalized separately,
e.g. using zero-mean and unit-variance normalization. Based


## Page 8


8
on these findings, in this work, we partition the reference
population by gender and speech task. These are simplifying
assumptions, that we believe to be reasonable in this proof-
of-concept exploring the feasibility of defining RIs for speech.
Future work should not only study a larger reference popula-
tion, but also consider other methods for partitioning the RIs,
such as the Lahti criteria [107], or the Ichiahara method [79],
[108].
Step 5. Reference intervals estimation
In this work, an RI, i.e., the interval between the 2.5th and
97.5th percentiles [79], is derived for each feature, using the
non-parametric approach. Following the guidelines in [78],
90% confidence intervals (CIs) were derived for both the lower
and upper limits of the RI via boostrapping [109], to provide a
confidence measure on the estimated RI. Data was resampled
1000 times to estimate the confidence interval.
We acknowledge that for certain features, it is more appro-
priate to provide a single boundary, either an upper or lower
limit. For instance, elevated values of jitter and shimmer are
considered pathological, possibly indicating affected laryngeal
control, whereas there is no lower limit below which these
values are deemed unhealthy. We believe that determining
whether each feature should have a reference interval or a
single limit should be guided by domain-specific knowledge,
and we encourage further research on this topic. Our data-
driven approach does not allow us to draw conclusions on
this matter; therefore, reference intervals with two limits are
derived for all features.
Step 6. Feature correlation analysis
Some of the features in the proposed feature set are very
correlated with each other. It is expected, for instance, that
the mean and median of the formants are very correlated with
each other, and also measures of shimmer, and measures of
jitter should be correlated amongst each other. Additionally, a
high dimensionality feature space hinders the interpretability
of the results by the medical community.
Therefore, a feature correlation analysis is carried out to
exclude redundant features and reduce the dimensionality.
Features were grouped into clusters of similar information
using hierarchical clustering based on the Pearson correlation
between all feature pairs. Different correlation thresholds,
CT ∈{0.5, 0.6, 0.7, 0.8, 0.9, 1}, were explored to fix the final
clusters. For CT = 1, each cluster corresponded to a single
feature. For other correlation thresholds, a "prototype feature"
was selected to represent each cluster, resulting in the final
reduced-dimensionality feature set.
To promote robustness to dataset shifts, prototype features
were chosen based on the similarity of the standard deviation
of their distributions across different datasets. Ideally, other
corpora of control individuals would be available for this
analysis. Since that is not the case, the standard deviation of
each feature in the reference population was compared to that
of control subjects in the disease detection population. The
feature with the most similar standard deviation in both groups
within each cluster was designated the prototype feature.
Means were not considered, as they can be adjusted by adding
a bias term. Future work should explore more sophisticated
methods for selecting prototype features.
This dimensionality reduction approach, which involves
Pearson correlation analysis followed by hierarchical clus-
tering on the reference population, was motivated by two
primary objectives: first, to establish a feature set suitable
for characterizing reference speech independently of disease-
specific deviations; second, to mitigate the risks of unstable
results, overfitting, and poor generalization associated with
supervised feature selection on small datasets [110]–[112].
Detailed results of the correlation analysis are provided in
the next section.
B. Reference Speech Results
Reference intervals were derived for each feature in the full-
dimensionality feature set8, with the corresponding confidence
intervals on the upper and lower bound. The analysis was
conducted separately for the sustained vowel /a/ and the picture
description task.
Feature correlation analysis
As described in section V-A (step 6), a reduced-dimensionality
feature set was derived to exclude features highly correlated
with each other. Fig. 3 (a) shows a heatmap with the Pearson
correlation values between all feature pairs. Strong colored
cells correspond to pairs of strongly correlated features –
red for positively correlated features, and blue for inversely
correlated features. The values above the diagonal correspond
to features derived for female subjects, while the values below
the diagonal correspond to values derived for male subjects.
As expected, one can observe that mean and median values
of formant frequencies are strongly correlated, as well as
the different measures of jitter and different measures of
shimmer. HNR also appears inversely correlated with shimmer
measures. Other patterns appear, for example speech rate is
inversely correlated with silence rate, average syllable duration
is inversely correlated with the articulation rate, and the repe-
tition ratio is positively correlated with the Brunet’s index and
inversely correlated with the type-to-token ratio. Correlations
between features are similar for both female and male subjects.
The clusters of highly correlated features achieved via hier-
archical clustering are presented in Fig. 3 (b). The prototype-
features of each cluster, i.e., the features that were selected to
represent the information encoded in each cluster, are listed
in Table III. The higher the correlation threshold (CT) that
defines the clusters, the larger the number of clusters, and
thus the higher the dimensionality of the final set.
Comparison of reference and patient speech
Figs. 4 and 5 show the RIs represented in a radar chart,
normalized to zero mean and unit variance, for the sustained
vowel task and picture description task, respectively.
8Although the feature ratio of ambiguous coreference chains may be inter-
esting for the detection of several diseases, including Alzheimer’s disease and
schizophrenia, it was excluded from further analysis because the confidence
intervals on the upper bound for both genders were larger than the RI itself,
indicating a poor confidence on the derived RI. Further discussion is provided
in Appendix B.


## Page 9


9
Fig. 3.
Correlation analysis of the features extracted from vowel recordings (top) and picture description transcriptions (bottom). (a) shows the Pearson
correlation between the features. The values above the diagonal refer to features extracted for female subjects, while the values below the diagonal refer
to male subjects. (b) shows the dendrogram results from the hierarchical clustering of features, based on their Pearson correlation correlation. The y axis
corresponds to 1 −CorrelationTreshold, to capture the distance between features of the same cluster.
In the top plots, light green lines indicate the lower and
upper bound of the reference interval, with the shaded region
representing the confidence interval on the reference interval
limits. The dark green line represents the mean values, which
are always zero due to normalization. The first and third
column of each figure display the reference intervals for the
entire feature set, while the second and forth columns refer
to the feature subset obtained after the Pearson correlation-
based feature selection, with CT = 0.5. This reduced, less
correlated, feature set aims to highlight which groups of
features are more impacted by each disease. The speech of any
subject, while performing one of the speech tasks analysed,
can be projected into the radar plot, and compared to the
reference population. Ideally, if a subject is healthy, their
speech should be represented within the area delimited by the
reference intervals.
On the second and third row plots, we overlay individual
data from the disease detection population onto the reference
interval radar charts. Following the discussion in section V-A–
step 4, the population for disease detection was also normal-
ized to zero-mean and unit variance, using only the control
subjects to compute the statistics for normalization. Each
subject is represented by a different line, control subjects in
blue and patients in magenta, shown in separate plots. The
entire area within the reference interval is shaded to enhance
visibility.
By visual inspection, the confidence intervals on the limits
of the RIs derived for the sustained vowel task (Fig. 4) appear
relatively narrow, with the exception of the standard deviation
of F0 and the mean of the second formant for male subjects.
For the picture description task (Fig. 5), the feature with a
wider confidence interval is silence-to-speech ratio. One can
interpret these wide confidence intervals as an indication of
lack of confidence on the exact margins of the RI. Future
research should aim at improving the confidence of these
intervals with a larger reference population, collected under


## Page 10


10
Fig. 4. Radar plots to characterize reference speech, using the task sustained vowel /a/. The dark green line corresponds to the mean value of each feature,
while the light green lines correspond to the RI, computed using the reference population. Blue lines correspond to control speakers, whereas pink lines
correspond to patients (PD).
controlled recording conditions.
When visually inspecting the plots representing the PD pa-
tients enunciating a sustained vowel /a/ (Fig. 4), it is clear that
they deviate from the reference values more frequently than
controls in the axis that correspond to HNR, jitter, shimmer
and F0 related features. This is notorious for both genders,
however it appears that HNR, jitter and shimmer features are
more relevant for female subjects, while F0 features are more
relevant for male subjects.
When analyzing the Cookie Theft image descriptions
(Fig. 5), differences between AD patients and controls also
exist. For instance, several female AD patients exhibit a
discourse marker rate (feature 33) substantially above the
reference interval. Specifically, 26% of female AD patients
surpass the RI for discourse marker rate, compared to only
7% of female controls. Additionally, speech rate (feature 20)
for both male and female AD patients is more frequently below
the RI than that of control subjects.
However, these differences appear more notorious in the
sustained vowel task than in the picture description. This may
indicate that the task of enunciating a sustained vowel may be
more suitable for this RI analysis, as it entails less sources
of variability. It is also possible that the noisy recording
conditions in ADReSS play a strong role.
This radar chart visualization is particularly well-suited
for the analysis of speech as a biomarker for health in two
scenarios. When studying a disease population, the radar chart
visualization enables the identification of features that appear
to be strong markers of a disease, and simultaneously still
robust to dataset shifts. Taking the example of PD female
patients vs Control females (Fig. 4 – left): there are 6 features
(all jitter-, shimmer- and HNR-related) for which more than
95% of the controls stay inside the RI and over 20% of the
patients fall outside the RI. Alternatively, this visualization
provides a simple way to compare the speech features of one
individual to the speech features of a reference population,
and quickly identify if there are any deviations on groups of
features that are expected to be affected by a certain disease.


## Page 11


11
Fig. 5. Radar plots to characterize reference speech, using the task picture description. The dark green line corresponds to the mean value of each feature,
while the light green lines correspond to the reference interval, computed using the reference population. Blue lines correspond to control speakers, whereas
pink lines correspond to patients (AD).
Radar plots have been previously employed to visualize
speech features in the context of speech as a biomarker. Jiao et
al. [55] used radar plots to illustrate phonological disturbances
in dysarthric speakers, while Behrendt et al. [113] introduced
DemVis, a prototype system for extracting and visualizing
speech features, which also performs AD detection.
A quantitative comparison of disease-affected speech with
the RIs derived for the reference population was conducted,
namely to compare the distance of the features in disease-
affected speech to the reference intervals. This distance is,
on average, higher for patients than for controls, and the
difference between the two groups is considered statistically
significant for female and male subjects, both in PC-GITA and
ADReSS. Further details are available in Appendix C.
VI. CLASSIFICATION OF SPEECH AFFECTING DISEASES
This section focuses on the automatic detection of speech-
affecting diseases leveraging the definition of reference speech
described before. Deviation-scores are introduced to quantify
how much an individual’s speech feature deviates from ref-
erence values. These scores are then used as inputs for the
detection task. The detection of each speech affecting disease
is formulated as a binary classification problem (patients
versus controls) and addressed using Neural Additive Mod-
els (NAMs) [22]. NAMs provide full transparency, enabling
explanations that are compatible with clinical reasoning.
This analysis focuses on the detection of Alzheimer’s dis-
ease and Parkinson’s disease separately, but ultimately it is
aimed at defining an approach suitable for multiple speech-
affecting diseases. In fact, we propose a single framework that
could be used for the detection of several diseases, differing
slightly on the subsets of features to be used, depending on the
speech task at hand, and on the model used for classification.
As described earlier in section V-A (step 2), for the picture
description task, all feature groups should be used, while for
sustained vowels, only voice quality and vocal tract related
features are suitable. We expect that future work analysing
reading tasks should include all feature groups, except content


## Page 12


12
Fig. 6. Overview of the steps entailed in the detection of diseases.
TABLE III
PROTOTYPE-FEATURES, PER CORRELATION THRESHOLD, CT .
CT
Champion-features
Sustained vowel
0.5 / 0.6
/ 0.7
F1_median, F2_mean, F3_mean, F4_mean, HNR, localabsoluteJitter, meanF0, stdevF0
0.8
apq11Shimmer, aqpq5Shimmer, F1_median, F2_mean, F3_mean, F4_mean, HNR, lo-
calabsoluteJitter, meanF0, stdevF0
0.9
apq11Shimmer, aqpq5Shimmer, F1_median, F2_mean, F3_mean, F4_mean, HNR, lo-
calabsoluteJitter, localdbShimmer, meanF0, stdevF0
0.5 / 0.6
First person pronouns, articulation rate, content density, discourse marker rate, F1_mean,
F2_median, F3_mean, F4_median, HNR, Honoré statistic, idea density, localabsolute-
Jitter, meanF0, mean coherence, mean silence count, polarity, ppq5Jitter, coreference
chain ratio, repetition ratio, speech rate, stdevF0, coherence variability
0.7
First person pronouns, articulation rate, content density, discourse marker rate, F1_mean,
F2_median, F3_mean, F4_mean, F4_median, HNR, Honoré statistic, idea density,
localabsoluteJitter, localdbShimmer, meanF0, mean coherence, mean pause duration,
mean silence count, polarity, ppq5Jitter, coreference chain ratio, repetition ratio, silence-
to-speech ratio, speech rate, stdevF0, TTR, coherence variability
0.8
First person pronouns, articulation rate, content density, discourse marker rate, F1_mean,
F1_median, F2_median, F3_mean, F4_mean, F4_median, HNR, Honoré statistic, idea
density, localabsoluteJitter, localdbShimmer, meanF0, mean coherence, mean pause du-
ration, mean silence count, polarity, ppq5Jitter, coreference chain ratio, repetition ratio,
silence rate, silence-to-speech ratio, speech rate, stdevF0, TTR, coherence variability
0.9
First person pronouns, apq11Shimmer, articulation rate, content density, discourse
marker rate, F1_mean, F1_median, F2_median, F3_mean, F4_mean, F4_median, HNR,
Honoré statistic, idea density, localabsoluteJitter, localdbShimmer, meanF0, mean co-
herence, mean pause duration, mean silence count, mean speech duration, polarity,
ppq5Jitter, coreference chain ratio, repetition ratio, silence rate, silence-to-speech ratio,
speech rate, stdevF0, TTR, coherence variability
related features, and spontaneous speech tasks should leverage
all feature groups.
A. Disease detection pipeline
The proposed method entails several steps, some of them –
pre-processing, feature extraction, and dimensionality reduc-
tion – shared with the previous stage for reference speech
definition, as depicted in Fig. 6. The vowel segmentation step
(section V-A–step 1) led to the exclusion of 12 PC-GITA
samples from PC-GITA (further details in Appendix A). These
samples were not used for classifier training or hyperparameter
optimization. However, to ensure a fair comparison with previ-
ous literature, these excluded samples are arbitrarily assigned
the prediction "control" when reporting performance on the
test set. This reflects a 50% a priori probability of a correct
prediction due to the balanced nature of the datasets.
After data pre-processing, feature extraction, and dimen-
sionality reduction, data underwent normalization (step 7),
and deviation scores were computed (step 8). This process
culminated in binary classification (Step 9), which outputs an
interpretable prediction. Detailed descriptions of these steps
are provided below. While steps 3 to 5 pertain exclusively to
the speech characterization pipeline and are not part of the
disease detection pipeline, the numbering is retained across
both pipelines for consistency, reflecting the shared nature of
some steps.
Step 7. Stratified normalization
Prior to comparing reference intervals with disease datasets
and calculating deviation scores, stratified normalization by
gender and source dataset was performed. This approach
preserves the intrinsic characteristics of each group, acknowl-
edging that the relationship between controls and patients
may differ between male and female subjects, and that the
distribution of each feature may differ in each dataset. Only
the control subjects in the training set within each stratification
group were used to compute the statistics for normalization.
We compared two normalization strategies, zero mean and
unit variance scaling, and MinMax scaling between zero and
one. Both strategies were implemented using the scikit-learn
toolkit [114]. This approach assumes the gender of speakers
in the test set is known, a reasonable assumption given the
high performance of automatic speech-based gender detection
methods [115].
Step 8. Computation of deviation-scores
In the previous stage, reference speech was characterized using
the distribution of acoustic and linguistic features within a
reference population. The hypothesis explored here is that
deviations of a new audio sample relative to the reference
population can indicate the presence of a specific disease in
the speaker. Five deviation scores (DS) were compared to
assess the extent to which each feature value xi in a new audio
sample diverges from the corresponding feature distribution
in the reference population. The five deviation scores are:
DSMST D, inspired by
[116], DSMST D−no−cap, DSQ123,
DSRI, and DSMahalanobis. Further details on these deviation
scores, together with exhaustive experiments using them are
reported in the Appendices.
Step 9. Binary classification
Classification experiments were conducted with Neural Addi-
tive Models (NAMs) [22], a type of glass-box models inher-
ently interpretable. NAMs are part of the model family called
Generalized Additive Models (GAMs), which are described
by
g(E[y]) = β + f1(x1) + f2(x2) + · · · + fK(xK) ,
(1)
where x= (x1, x2, ..., xK) is the input with K features, y is
the target variable, g is the link function, and fi is a univariate
shape function with E[fi] = 0.


## Page 13


13
The idea of NAMs is to parameterize each fi in Equation 1
by a neural network (subnet). In short, NAMs are a linear
combination of neural networks, each attending to a single
feature, that are trained jointly using backpropagation. It is this
modularity that makes NAMs’ predictions very easily inter-
pretable. NAMs’ predictions can be interpreted by visualizing
each of the learned shape functions, e.g. plotting fi(xi) vs xi.
The graphs learnt by NAMs are not a posteriori explanations,
but rather an exact description of how the model comes to a
prediction.
The NAM architecture is also compatible with a multitask-
scenario, particularly suitable for the simultaneous detection
of multiple speech affecting diseases, when adequate data is
available. The multitask architecture is identical to that of
single task NAM, except that each feature is associated with
multiple subnets and the model jointly learns a task-specific
weighted sum over their outputs that determines the shape
function for each feature and task [22]. We expect that this
property will be key to enable the simultaneous detection of
multiple diseases, provided that datasets with similar tasks
collected under comparable conditions are available.
The binary classification experiments were based on
ADReSS for Alzheimer’s disease detection, and PC-GITA
for Parkinson’s disease detection. Given the limited size of
these corpora, the experiments were conducted in a 10-fold
cross validation (CV) setting. For ADReSS, because a held-
out test set was defined for the challenge in which the corpus
was introduced, the 10-fold cross validation was applied on
the training set, for hyperparameter tuning. Afterwards, the
predictions for the test set of the 10 models trained during
CV are aggregated via majority voting. For PC-GITA, there
was no held out test set, hence the 10-fold CV was conducted
on the entire dataset. In each run, one of the 9 training folds
was assigned as development fold, to perform hyperparameter
tuning. Folds were defined to ensure that all data from the
same speaker is assigned to the same fold, to avoid leakage
of speaker information across training, development and test
folds. Folds ensure a balance between healthy controls and
patients, in terms of number of speakers, gender and age.
Data was normalized separately for both genders, as de-
scribed in section VI-A–step 7, with the normalization statis-
tics being computed based on the controls in the training
folds. Distance scores were also computed separately for
both genders, given that the reference intervals were derived
separately for both genders. The classifiers, however, are
gender-independent.
Initially, an exhaustive set of binary classification experi-
ments were conducted with Support Vector Machines (SVMs)
and Logistic Regression, using the two transcription types,
three normalization strategies (zero-mean and unit variance,
MinMax, and no normalization), six correlation threshold
values, and five deviation-scores were compared. An extra
scenario where the raw features are directly fed to the clas-
sifiers after the stratified normalization was also considered.
The results obtained are thoroughly described in Appendix E.
The configurations that yielded the best results were used to
restrict the range of experiments conducted with NAMs, given
their higher computational burden. Hyperparameter tuning was
performed with Bayesian optimization using Gaussian Pro-
cesses, implemented on scikit-optimize [117], with 100 calls
to the optimizer. Further details on training hyperparameters
and network architecture are reported in the Appendix F.
B. Disease detection results
The results obtained with NAMs on the different configura-
tions explored are reported in Table IV. For PD classification,
NAMs were able to achieve 75% accuracy on the development
folds, 69% of the test folds, and a speaker-level accuracy
after majority vote of 73%. For AD detection, NAMs yielded
84% on the development folds, and 75% on the held-out
test set. The NAM performance for PD detection on the test
folds is lower than that achieved with LR/SVM classifiers.
Conversely, for AD detection, the NAM results are better that
those obtained with LR/SVM classifiers (based on the best
development performance). The best classification results for
PD were obtained with the entire feature set, while for AD
were obtained with the reduced dimensionality feature set,
with CT = 0.5, similarly to the SVM and LR results (detailed
in Appendix E). Notably, the dimension of the entire feature
set used to study sustained vowels (20 features) is very similar
to the dimension of the reduced set used for studying the
picture description task (23 features).
More importantly than surpassing the classification perfor-
mance, the advantage of NAMs lies in their inherent inter-
pretablity. The modularity and transparency of NAMs allow
for precise visualization of what the models learn during
training and how each prediction is computed. Figs. 7 and
8 depict the features that contribute most to the predictions,
and present the corresponding learned shape functions. These
graphs are not a posteriori explanations, but rather an exact
description of how the model comes to a prediction. Each
semi-transparent blue line corresponds to one model of the
ensemble, trained on a given run of the cross-validation, i.e.
the lines correspond to 30 models (an ensemble of 3 models
was trained for each of the 10 runs in the 10-fold cross-
validation, as detailed in Appendix F). The solid blue line
corresponds to the average of each model. Following [22], the
average score of each feature (each shape function) was set to
zero, by subtracting the mean score, averaged over the entire
training set. This results that, on binary classification tasks,
positive scores increase the probability of the positive class,
compared to the baseline probability of observing that class,
while negative scores decrease the probability. On the same
plots, the normalized data density is also visible, in the form
of pink bars. The darker the shade of pink, the more data there
is in that region.
One can observe substantial variability in the shape func-
tions learnt by each model, particularly when less data is
available for training, indicated by lighter shades of pink.
This is very evident in the ADReSS corpus, which is half the
size of PC-GITA. This variability gives a sense of confidence
on the patterns learnt and emphasizes the need for research
with larger corpora to enable more robust conclusions. Nev-
ertheless, in most cases, the models learned curves that align
with the expected manifestations of each disease in the speech
signal.


## Page 14


14
TABLE IV
CLASSIFICATION RESULTS, USING NAMS, IN TERMS OF ACCURACY (ACC), MACRO PRECISION (P), MACRO RECALL (R), AND MACRO F1, IN [%].
Dev Folds
Test
Test – Speaker MV
CT
DT
norm
Acc
P
R
F1
Acc
P
R
F1
Acc
P
R
F1
Parkinson’s Disease
CT=1.0
DTRI
MinMax
75.0
75.8
74.9
74.8
68.7
69.9
68.7
68.2
73.0
74.7
73.0
72.5
CT=0.9
DTQ123
MinMax
72.6
73.2
72.5
72.4
62.7
64.0
62.7
61.8
67.0
69.2
67.0
66.0
CT=1
DTQ123
MinMax
72.2
73.0
72.2
72.0
66.3
67.3
66.3
65.9
68.0
69.1
68.0
67.5
Alzheimer’s Disease
CT=1.0
Raw feats
MinMax
83.3
83.4
83.3
83.3
72.9
73.3
72.9
72.8
–
–
–
CT=0.7
DTRI
none
73.1
75.7
73.1
72.5
70.8
70.8
70.8
70.8
–
–
–
–
CT=0.5
DTRI
MinMax
79.6
80.3
79.6
79.5
70.8
72.2
70.8
70.4
–
–
–
–
CT=0.5
Raw feats
MinMax
84.3
84.4
84.3
84.2
75.0
75.0
75.0
75.0
–
–
–
–
CT=0.5
DTRI
none
75.9
77.8
75.9
75.5
72.9
73.0
72.9
72.9
–
–
–
–
CT=1.0
Raw feats
none
81.5
81.9
81.5
81.4
72.9
73.0
72.9
72.9
–
–
–
–
Fig. 7.
NAM trained for PD classification, for female (top) and male (bottom) subjects. The left plots represent the features that most contribute to the
predictions; the plots on the right depict the shape functions learnt by the NAM, for the top three most important features.
Upon analysing the NAM trained for PD detection which
achieved the best accuracy on the test set (Fig. 7), it becomes
evident that the outcomes differ between genders, although
local jitter appears on the top three most important features
for both genders. This feature is, by far, the most important for
female speakers. The following features in terms of importance
for female speakers are also jitter and shimmer-related. This
is consistent with expectations, as a high jitter and shimmer
reflect cycle-to-cycle perturbations of F0, associated with
impaired laryngeal control typical of PD patients. Previous
studies have also found higher jitter values in PD patients
when compared to control subjects (e.g. [118], [119]).
For male subjects, the most important features are the
standard deviation and mean of F0. The corresponding shape
functions indicate that higher values of mean F0 and of F0
standard deviation are associated with a higher risk of PD.
Other works have also found increased F0 standard deviation
in sustained vowels produced by PD patients compared to
control subjects (e.g. [63], [120]). Goberman et al. [63]
suggested that this increase may be due to laryngeal instability,
potentially caused by weakness of the laryngeal musculature
resulting from rigidity or tremor. The author mentions that
tremor-related weakness has been found in other body sys-
tems, such as wrists [121]. Although not studied here, it is
noteworthy that, in continuous speech, as opposed to sustained
vowels, the F0 standard deviation is expected to decrease in


## Page 15


15
Fig. 8.
NAM trained for AD classification, for female (top) and male (bottom) subjects. The left plots represents the features that most contribute to the
predictions; the plots on the right depict the shape functions learnt by the NAM, for the top three most important features.
PD patients, typically described as mono-pitch [41], [122],
[123].
The mechanism underlying the increased mean F0 in PD
patients is suggested to be the increased rigidity of the
laryngeal musculature (e.g. cricothyroid and thyroarytenoid
muscles) [41], [124]. Biomechanical models of phonation
demonstrate that increased vocal fold stiffness leads to higher
fundamental frequency and jitter [41]. Various works have
identified differences in mean F0 in PD patients and controls,
although not always significant for both genders, nor in the
same direction. For example, Goberman et al. [63] found that
mean F0 was higher in PD patients than controls, particularly
in male speakers; Midi et al. [120] found that mean F0
was higher in PD patients than healthy controls, but this
difference was only significant in female subjects; and Yang
et al. [125] found the opposite, i.e., that mean F0 was lower
in patients suffering from PD than controls. It is important
to acknowledge that F0 is more than just a marker for vocal
fold behaviour, it carries information about different speaker
states and traits [59], and even physiological aspects such
as hormonal balance and aging [36]. Thus, results should
be interpreted with caution, and further research should be
conducted with a larger dataset of age- and gender-matched
controls and patients of PD and other diseases.
The patterns learnt by the NAM trained for PD detection
are consistent with those represented on the radar plot of
the sustained vowel for PD patients (Fig. 4). Both the NAM
and radar plot flag jitter and F0 as important features for
characterizing the speech of female and male PD patients.
Upon examination of the NAM trained for Alzheimer’s
disease detection which achieved the best performance, as
depicted in Fig. 8, it is evident that each model in the en-
semble/cross validation run learnt different patterns, yet some
general trends can be inferred when averaging the predictions
of those models. The first consideration is that the foremost
contributing feature to prediction, for both male and female
subjects, is speech rate. It is clear that the slower the speech
rate, the higher the risk of the person suffering from AD. This
behaviour is expected, as a slower speech with more pauses
is expected to be associated with a higher risk of AD. In
fact, other works (e.g.
[33], [44]) have also identified the
importance of speech rate for AD detection from speech.
Idea density is also among the top three most important
features for detecting AD in both female and male speakers.
The shape function learnt reflects a U-shape, indicating that
low and high values of the feature idea density are associated
with a higher risk of Alzheimer’s disease. Low idea density
has been associated with Alzheimer’s disease at least since the
well-known "Nun Study" by by Snowdon et al. [126], which
found that low idea density in early life strongly predicted
reduced cognitive ability or the presence of AD in later life.
Boschi et al. [58] conducted a comprehensive review and
reported that AD patients have significantly lower idea density
compared to controls.
A similar U-shape pattern was learnt by the subnet attending
to the Type-to-token ratio (TTR) feature, which is one of


## Page 16


16
the top-three most important features for AD detection in
male subjects. TTR, a measure of lexical diversity, is also
associated with cognitive impairments. For example, Bucks et
al. [127] found TTR to be significantly lower in AD patients
compared to control subjects. Berisha et al. [128] suggested
that measures of lexical diversity, including the number of
unique words, are strong predictors of pre-clinical AD onset.
Contrarily, the fact that the NAM learnt to associate high
values of these features with a higher risk of AD is more
surprising, and not frequently reported in the literature, to
the best of our knowledge. However, this pattern observed
by the NAM is present in the data. We manually inspected
data samples labelled with AD associated high idea density
and/or TTR and identified several patterns: some examples,
although not very frequent, included whisper hallucinations;
some examples corresponded to correct transcriptions, but
were confusing or nonsensical despite high idea density or
TTR; and occasionally, they were perfectly coherent descrip-
tions of the Cookie Theft picture. These findings reinforce
the idea that features such idea density or TTR alone are not
sufficient to make a prediction.
Nevertheless, this illustrates the advantage of having a fully
transparent model, despite its imperfections. For instance,
let us consider a scenario where a new individual under-
goes testing with this system and receives a prediction of
Alzheimer’s disease. A healthcare practitioner could examine
the reasons provided by the system for this prediction. If the
sole reason provided was a high idea density or high TTR,
the healthcare practitioner would have the information needed
to make an informed decision or recommend further testing.
Such reasoning would not be possible with a black-box model,
or with a model that operates on uninterpretable features.
Finally, the Discourse marker rate is also among the top-
three most influential features for AD detection in female
subjects. As the discourse marker rate increases, there is a
higher risk associated with Alzheimer’s Disease, consistent
with the findings of Boschi et al. [58].
VII. LIMITATIONS
This exploratory work has some limitations, and further re-
search is needed to address these potential drawbacks. One ob-
vious limitation concerns feature extraction. Some of the fea-
tures used, particularly vocal tract and voice-quality features,
have been noted for their limited robustness across diverse
recording conditions, including various devices–especially mo-
bile platforms–background noise, and reverberation [103]–
[105]. Therefore, these features may not consistently yield
reliable results across corpora recorded under different condi-
tions. We advocate for the need to come up with guidelines to
standardize how researchers record corpora and extract these
features, which would enhance robustness and facilitate fair
comparisons among different studies.
Another limitation pertains to corpora availability. The
CLAC dataset, while valuable and larger than most speech
corpora in clinical research, is crowdsourced, resulting in noise
and lack of medical verification despite data filtering. Addi-
tionally, its size conditions the reliability of results, particularly
for RI estimation, which ideally requires a minimum of 400
subjects per gender and age range. The small size of PC-
GITA and ADReSS also adversely affects disease detection,
specifically impacting the shape functions learned by NAMs’
subnets. It is noteworthy that different hyperparameters result
in different feature contributions and shape functions, and
research with a larger dataset is essential to enhance robustness
of results.
A third limitation relates to data normalization. To enable
meaningful RI comparisons across datasets, we applied zero-
mean and unit-variance normalization. Ideally, under consis-
tent recording conditions, uniform speech task instructions,
and robust feature extraction methods, such analyses could
proceed without shifting the underlying data distribution.
A key limitation of this study is that AD and PD detection
tasks were addressed separately due to differences in the pub-
licly available datasets. These datasets vary in speech tasks and
recording conditions, which substantially influence the features
extracted [18], [23]. Future work could explore simultaneous
detection using the proposed framework when datasets with
comparable tasks and recording conditions become available.
Finally, it is important to to emphasize that the diseases,
mechanisms, and their corresponding effects on the speech
signal illustrated Fig. 1 serve as an initial foundation. We
propose that further research and interdisciplinary dialogue are
necessary to refine and expand this figure.
VIII. CONCLUSION
This work introduced a framework for the use of speech
as an interpretable biomarker for multiple diseases. Although
focusing on Alzheimer’s and Parkinson’s diseases, the pro-
posed framework is suitable for using speech as a biomarker
in general, including the detection of other speech affecting
diseases or even general health perturbations not typically
categorized as diseases. This work started by discussing that
speech affecting diseases should not be regarded individually
for two reasons: (1) they often have overlapping effects on
the speech signal, and (2) they often are risk factors for each
other. Therefore, it is argued here that a valuable first step is to
characterize the speech of a reference population. This charac-
terization was based on reference intervals, a concept common
in clinical laboratory science, but novel in the field of speech
analysis for disease detection. In this study, reference intervals
were established for a reference population. Nevertheless, our
vision encompasses the potential of individualized definition of
reference speech. This self-definition would facilitate precise
identification of early signs of disease, and would enable
personalized healthcare.
The initial feature set was defined to capture manifestations
of various speech-affecting diseases, focusing exclusively on
interpretable features. However, a high-dimensional feature
space complicates result interpretation. Thus, feature selection
was based on a reference population, rather than the disease
detection datasets, to establish a reference speech feature set
and to avoid possible overfitting frequently observed with
supervised feature selection on small datasets [110]–[112].
Future research should expand the initial feature set to in-
clude additional knowledge-based features, capturing broader


## Page 17


17
dimensions of reference speech, and further validate these
features with other corpora for disease detection.
Finally, the definition of reference speech was leveraged
for the detection of AD and PD, by comparing how much
controls and patients deviate from the reference population.
Although the classification performance falls below other
works in the literature, we advocate for the exploration of this
approach due to its transparency, thereby advancing speech
as a reliable biomarker. In fact, it is well-documented that
small sample sizes in clinical speech analysis studies often
lead to overoptimistic estimates of model performance [19],
[67]. Therefore, we underscore the importance of interpretable
outcomes. Particularly, the shape-functions learnt by NAMs
correspond exactly to the decision process, instead of a
posterior explanations. This transparency is crucial not only
as a "second opinion" for clinicians, but also for early-stage
research into speech as a biomarker. It facilitates multidis-
ciplinary discussions among teams regarding the validity of
model assumptions, and informs decisions regarding subse-
quent iterations, including data collection and feature refine-
ment. Moreover, NAMs are suitable for multitask learning,
enabling simultaneous detection of multiple diseases provided
there is annotated speech data across different diseases, for the
same speech tasks.
IX. ACKNOWLEDGEMENTS
This
work
was
supported
by
Portuguese
national
funds through Fundação para a Ciência e a Tecnologia,
with
references
DOI:
10.54499/UIDB/50021/2020
and
SFRH/BD/149126/2019, and by the Portuguese Recovery and
Resilience Plan and Next Generation EU European Funds,
through project C644865762-00000008 (Accelerat.AI).
REFERENCES
[1] International classification of diseases 11th revision (icd-11).
[2] Anna Pompili, Alberto Abad, Paolo Romano, Isabel P Martins,
Rita Cardoso, Helena Santos, Joana Carvalho, Isabel Guimarães, and
Joaquim J Ferreira. Automatic detection of parkinson’s disease: An
experimental analysis of common speech production tasks used for
diagnosis. In International Conference on Text, Speech, and Dialogue,
pages 411–419. Springer, 2017.
[3] Joana Correia, Francisco Teixeira, Catarina Botelho, Isabel Trancoso,
and Bhiksha Raj. The in-the-wild speech medical corpus. In ICASSP.
IEEE, 2021.
[4] Laureano Moro-Velazquez, Jesus Villalba, and Najim Dehak. Using
x-vectors to automatically detect parkinson’s disease from speech.
In ICASSP 2020-2020 IEEE International Conference on Acoustics,
Speech and Signal Processing (ICASSP), pages 1155–1159. IEEE,
2020.
[5] Sayed Soroush Haj Zargarbashi and Bagher Babaali. A multi-modal
feature embedding approach to diagnose alzheimer disease from spoken
language. arXiv preprint arXiv:1910.00330, 2019.
[6] Jochen Weiner, Christian Herff, and Tanja Schultz.
Speech-Based
Detection of Alzheimer’s Disease in Conversational German.
In
Interspeech, 2016.
[7] Karmele Lopez-de Ipina, Unai Martinez-de Lizarduy, Pilar M Calvo,
Jiri Mekyska, Blanca Beitia, Nora Barroso, Ainara Estanga, Milkel
Tainta, and Mirian Ecay-Torres.
Advances on automatic speech
analysis for early detection of alzheimer disease: a non-linear multi-
task approach. Current Alzheimer Research, 15(2):139–148, 2018.
[8] Ayimnisagul Ablimit, Catarina Botelho, Alberto Abad, Tanja Schultz,
and Isabel Trancoso. Exploring dementia detection from speech: Cross
corpus analysis. In ICASSP 2022-2022 IEEE International Conference
on Acoustics, Speech and Signal Processing (ICASSP), pages 6472–
6476. IEEE, 2022.
[9] Gustavo Noffs, Thushara Perera, Scott C Kolbe, Camille J Shanahan,
Frederique MC Boonstra, Andrew Evans, Helmut Butzkueven, Anneke
van der Walt, and Adam P Vogel. What speech can tell us: A systematic
review of dysarthria characteristics in multiple sclerosis. Autoimmunity
reviews, 17(12):1202–1209, 2018.
[10] Amber Afshan, Jinxi Guo, Soo Jin Park, Vijay Ravi, Jonathan Flint,
and Abeer Alwan. Effectiveness of voice quality features in detecting
depression. Interspeech 2018, 2018.
[11] Alberto Parola, Arndis Simonsen, Vibeke Bliksted, and Riccardo
Fusaroli.
Voice patterns in schizophrenia: A systematic review and
bayesian meta-analysis. Schizophrenia research, 216:24–40, 2020.
[12] Catarina Botelho, Isabel Trancoso, Alberto Abad, and Teresa Paiva.
Speech as a biomarker for obstructive sleep apnea detection.
In
ICASSP, pages 5851–5855. IEEE, 2019.
[13] Juan M Perero-Codosero, Fernando Espinoza-Cuadros, Javier Antón-
Martín, Miguel A Barbero-Álvarez, and Luis A Hernández-Gómez.
Modeling obstructive sleep apnea voices using deep neural network
embeddings and domain-adversarial training. IEEE Journal of Selected
Topics in Signal Processing, 14(2):240–250, 2019.
[14] Gauri Deshpande and Björn Schuller.
An overview on audio, sig-
nal, speech, & language processing for covid-19.
arXiv preprint
arXiv:2005.08579, 2020.
[15] WHO.
Multimorbidity:
Technical
series
on
safer
primary
care,
https://apps.who.int/iris/bitstream/handle/10665/252275/
9789241511650-eng.pdf, 2016.
[16] Karen Barnett, Stewart W Mercer, Michael Norbury, Graham Watt,
Sally Wyke, and Bruce Guthrie. Epidemiology of multimorbidity and
implications for health care, research, and medical education: a cross-
sectional study. The Lancet, 380(9836):37–43, 2012.
[17] Harry HX Wang, Jia Ji Wang, Samuel YS Wong, Martin CS Wong,
Fang Jian Li, Pei Xi Wang, Zhi Heng Zhou, Chun Yan Zhu, Sian M
Griffiths, and Stewart W Mercer.
Epidemiology of multimorbidity
in china and implications for the healthcare system: cross-sectional
survey among 162,464 community household residents in southern
china. BMC medicine, 12(1):1–12, 2014.
[18] Catarina Botelho, Tanja Schultz, Alberto Abad, and Isabel Trancoso.
Challenges of using longitudinal and cross-domain corpora on studies
of pathological speech. Interspeech 2022, pages 2516–2520, 2022.
[19] Visar Berisha, Chelsea Krantsevich, Gabriela Stegmann, Shira Hahn,
and Julie Liss. Are reported accuracies in the clinical speech machine
learning literature overoptimistic? In Interspeech, pages 2453–2457,
2022.
[20] Melissa Conrad Stöppler. Definition of subclinical disease (accessed on
July 15, 2022). https://www.rxlist.com/subclinical_disease/definition.
htm. https://www.rxlist.com/subclinical_disease/definition.htm, 2021.
[21] Catarina Botelho, Alberto Abad, Tanja Schultz, and Isabel Trancoso.
Towards reference speech characterization for health applications.
Interspeech, 2023.
[22] Rishabh Agarwal, Levi Melnick, Nicholas Frosst, Xuezhou Zhang, Ben
Lengerich, Rich Caruana, and Geoffrey E Hinton.
Neural additive
models: Interpretable machine learning with neural nets. Advances in
Neural Information Processing Systems, 34:4699–4711, 2021.
[23] Catarina Botelho, Alberto Abad, Tanja Schultz, and Isabel Trancoso.
Towards reference speech characterization for health applications. In
Interspeech, 2023.
[24] Catarina Botelho. Speech as Biomarker for Multidisease Screening.
PhD thesis, Instituto Superior Técnico, University of Lisbon, 2024.
[25] Rohit Voleti, Julie M Liss, and Visar Berisha. A review of automated
speech and language features for assessment of cognitive and thought
disorders.
IEEE journal of selected topics in signal processing,
14(2):282–298, 2019.
[26] Gillinder Bedi, Facundo Carrillo, Guillermo A Cecchi, Diego Fer-
nández Slezak, Mariano Sigman, Natália B Mota, Sidarta Ribeiro,
Daniel C Javitt, Mauro Copelli, and Cheryl M Corcoran. Automated
analysis of free speech predicts psychosis onset in high-risk youths.
npj Schizophrenia, 1(1):1–7, 2015.
[27] Dan Iter, Jong Yoon, and Dan Jurafsky.
Automatic detection of
incoherent speech for diagnosing schizophrenia.
In Workshop on
Computational Linguistics and Clinical Psychology: From Keyboard
to Clinic, pages 136–146, 2018.
[28] Camila Sanz, Facundo Carrillo, Andrea Slachevsky, Gonzalo Forno,
Maria Luisa Gorno Tempini, Roque Villagra, Agustín Ibáñez, Enzo
Tagliazucchi, and Adolfo M García.
Automated text-level semantic
markers of alzheimer’s disease. Alzheimer’s & Dementia: Diagnosis,
Assessment & Disease Monitoring, 14(1):e12276, 2022.


## Page 18


18
[29] Anna Maria Pompili.
Speech and language technologies applied
to diagnostics and therapy of brain diseases.
PhD thesis, Instituto
SUperior Técnico - University of Lisbon, 2019.
[30] Daniel B Hier, Karen Hagenlocker, and Andrea Gellin Shindler. Lan-
guage disintegration in dementia: Effects of etiology and severity. Brain
and language, 25(1):117–133, 1985.
[31] Katrina E Forbes, Annalena Venneri, and Michael F Shanks. Distinct
patterns of spontaneous speech deterioration: an early predictor of
alzheimer’s disease. Brain and Cognition, 48(2-3):356–361, 2002.
[32] Gerald Oppenheim. The earliest signs of alzheimer’s disease. Journal
of geriatric psychiatry and neurology, 7(2):116–120, 1994.
[33] Ildikó Hoffmann, Dezso Nemeth, Cristina D Dye, Magdolna Pákáski,
Tamás Irinyi, and János Kálmán. Temporal parameters of spontaneous
speech in alzheimer’s disease. International journal of speech-language
pathology, 12(1):29–34, 2010.
[34] K Ranga R Krishnan, Mahlon Delong, Helena Kraemer, Robert Carney,
David Spiegel, Christopher Gordon, William McDonald, Mary Amanda
Dew, George Alexopoulos, Kathleen Buckwalter, et al. Comorbidity
of depression with other medical diseases in the elderly. Biological
psychiatry, 52(6):559–588, 2002.
[35] Kelsey T Laird, Beatrix Krause, Cynthia Funes, and Helen Lavretsky.
Psychobiological factors of resilience and depression in late life.
Translational Psychiatry, 9(1):1–18, 2019.
[36] Rita Singh. Profiling humans from their voice, volume 41. Springer,
2019.
[37] Katrine Bønneland Tølbøll. Linguistic features in depression: a meta-
analysis. Journal of Language Works-Sprogvidenskabeligt Studenter-
tidsskrift, 4(2):39–59, 2019.
[38] Stephanie Rude, Eva-Maria Gortner, and James Pennebaker. Language
use of depressed and depression-vulnerable college students. Cognition
& Emotion, 18(8):1121–1133, 2004.
[39] Alistair J Flint, Sandra E Black, Irene Campbell-Taylor, Gillian F Gai-
ley, and Carey Levinton. Abnormal speech articulation, psychomotor
retardation, and subcortical dysfunction in major depression. Journal
of psychiatric research, 27(3):309–319, 1993.
[40] Nicholas
Cummins,
Stefan
Scherer,
Jarek
Krajewski,
Sebastian
Schnieder, Julien Epps, and Thomas F Quatieri. A review of depression
and suicide risk assessment using speech analysis. Speech Communi-
cation, 71:10–49, 2015.
[41] Andrew Ma, Kenneth K Lau, and Dominic Thyagarajan. Voice changes
in parkinson’s disease: What are they telling us? Journal of Clinical
Neuroscience, 72:1–7, 2020.
[42] Juan Camilo Vásquez-Correa, Juan Rafael Orozco-Arroyave, and El-
mar Nöth.
Convolutional neural network to model articulation im-
pairments in patients with Parkinson’s disease. In Interspeech, pages
314–318, 2017.
[43] Lorraine O Ramig, Cynthia Fox, and Shimon Sapir. Speech treatment
for parkinson’s disease. Expert Review of Neurotherapeutics, 8(2):297–
309, 2008.
[44] Pascal Hecker, Nico Steckhan, Florian Eyben, Björn W Schuller, and
Bert Arnrich. Voice analysis for neurological disorder recognition–a
systematic review and perspective on emerging trends. Frontiers in
Digital Health, 4, 2022.
[45] Maral Asiaee, Amir Vahedian-Azimi, Seyed Shahab Atashi, Abdal-
samad Keramatfar, and Mandana Nourbakhsh. Voice quality evaluation
in patients with covid-19: An acoustic analysis. Journal of Voice, 2020.
[46] Mahmoud Al Ismail, Soham Deshmukh, and Rita Singh. Detection of
covid-19 through the analysis of vocal fold oscillations. In ICASSP
2021-2021 IEEE International Conference on Acoustics, Speech and
Signal Processing (ICASSP), pages 1035–1039. IEEE, 2021.
[47] Rubén Fernández Pozo, Jose Luis Blanco Murillo, Luis Hernández
Gómez, Eduardo López Gonzalo, José Alcázar Ramírez, and Doroteo T
Toledano. Assessment of severe apnoea through voice analysis, auto-
matic speech, and speaker recognition techniques. EURASIP Journal
on Advances in Signal Processing, 2009(1):982531, 2009.
[48] Atul Malhotra and David P White.
Obstructive sleep apnoea.
The
lancet, 360(9328):237–245, 2002.
[49] Patricia K Monoson and Arthur W Fox.
Preliminary observation
of speech disorder in obstructive and mixed sleep apnea.
Chest,
92(4):670–675, 1987.
[50] D Chamith Halahakoon, Glyn Lewis, and Jonathan P Roiser. Cogni-
tive impairment and depression—cause, consequence, or coincidence?
JAMA psychiatry, 76(3):239–240, 2019.
[51] John G Kerns and Howard Berenbaum.
Cognitive impairments as-
sociated with formal thought disorder in people with schizophrenia.
Journal of abnormal psychology, 111(2):211, 2002.
[52] Ronald B Hoodin and Harvey R Gilbert. Nasal airflows in parkinsonian
speakers. Journal of Communication Disorders, 22(3):169–180, 1989.
[53] Francisco
Martínez-Sánchez,
Juan
Meilán,
Juan
Carro,
Conso-
lación
Gomez
Íñiguez,
Lymarie
Millian-Morell,
Isabel
Pujante
Valverde, Tomás López-Alburquerque, and Doloroes Lopez. Speech
rate in Parkinson’s disease: a controlled study. Neurologia (English
Edition), 31(7):466–472, 2016.
[54] Gustavo Noffs, Frederique Boonstra, TThushara Perera, Helmut
Butzkueven, Scott Kolbe, et al. Speech metrics, general disability, brain
imaging and quality of life in multiple sclerosis. European Journal of
Neurology, 28(1):259–268, 2021.
[55] Yishan Jiao, Visar Berisha, and Julie Liss. Interpretable phonological
features for clinical applications. In ICASSP, pages 5045–5049. IEEE,
2017.
[56] Michael Saxon, Julie Liss, and Visar Berisha. Objective measures of
plosive nasalization in hypernasal speech. In ICASSP, pages 6520–
6524. IEEE, 2019.
[57] Sabine Skodda. Aspects of speech rate and regularity in Parkinson’s
disease. Journal of the neurological sciences, 310(1-2):231–236, 2011.
[58] Veronica Boschi, Eleonora Catricala, Monica Consonni, Cristiano
Chesi, Andrea Moro, and Stefano F Cappa. Connected speech in neu-
rodegenerative language disorders: a review. Frontiers in psychology,
8:208495, 2017.
[59] Nicholas Cummins, Vidhyasaharan Sethu, Julien Epps, Sebastian
Schnieder, and Jarek Krajewski. Analysis of acoustic space variability
in speech affected by depression. Speech Communication, 75:27–49,
2015.
[60] Gauri Deshpande and Björn W Schuller.
Audio, speech, language,
& signal processing for covid-19: A comprehensive overview. arXiv
preprint arXiv:2011.14445, 2020.
[61] Gregory A Bryant and Martie G Haselton. Vocal cues of ovulation in
human females. Biology Letters, 5(1):12–15, 2009.
[62] Emily Fischer and Alexander M Goberman.
Voice onset time in
parkinson disease. Journal of Communication Disorders, 43(1):21–34,
2010.
[63] Alexander Goberman, Carl Coelho, and Michael Robb. Phonatory char-
acteristics of parkinsonian speech before and after morning medication:
the on and off states. Journal of communication disorders, 35(3):217–
239, 2002.
[64] Anna Pompili, Rubén Solera-Urena, Alberto Abad, Rita Cardoso,
Isabel Guimaraes, Margherita Fabbri, Isabel P Martins, and Joaquim
Ferreira. Assessment of Parkinson’s disease medication state through
automatic speech analysis. Interspeech, 2020.
[65] Blaine S Greenwald. Depression in Alzheimer’s disease and related
dementias. American Psychiatric Press, Washington, 1995.
[66] Jakub Vanek, Jan Prasko, Samuel Genzor, Marie Ociskova, Krystof
Kantor, Michaela Holubova, Milos Slepecky, Vlastimil Nesnidal, An-
tonin Kolek, and Milan Sova. Obstructive sleep apnea, depression and
cognitive impairment. Sleep medicine, 72:50–58, 2020.
[67] Alex S Ozbolt, Laureano Moro-Velazquez, Ioan Lina, Ankur A Butala,
and Najim Dehak. Things to consider when automatically detecting
parkinson’s disease using the phonation of sustained vowels: analysis
of methodological issues. Applied Sciences, 12(3):991, 2022.
[68] Fernando Espinoza-Cuadros, Rubén Pozo, Doroteo Toledano, José
Alcázar-Ramírez, Eduardo Gonzalo, and Luis Hernandez-Gomez et al.
Reviewing the connection between speech and obstructive sleep apnea.
Biomedical engineering online, 15(1):20, 2016.
[69] Rubén Solera-Ureña, Catarina Botelho, Francisco Teixeira, Thomas
Rolland, Alberto Abad, and Isabel Trancoso.
Transfer learning-
based cough representations for automatic detection of covid-19. In
Interspeech, 2021.
[70] Björn W. Schuller, Anton Batliner, Christian Bergler, Cecilia Mascolo,
Jing Han, Iulia Lefter, Heysem Kaya, Shahin Amiriparian, Alice
Baird, Lukas Stappen, Sandra Ottl, Maurice Gerczuk, Panaguiotis
Tzirakis, Chloë Brown, Jagmohan Chauhan, Andreas Grammenos,
Apinan Hasthanasombat, Dimitris Spathis, Tong Xia, Pietro Cicuta,
Leon J. M. Rothkrantz, Joeri Zwerts, Jelle Treep, and Casper Kaandorp.
The INTERSPEECH 2021 Computational Paralinguistics Challenge:
COVID-19 Cough, COVID-19 Speech, Escalation & Primates.
In
Interspeech, Brno, Czechia, Sept. 2021.
[71] João Paulo Teixeira and Paula Odete Fernandes. Jitter, shimmer and
HNR classification within gender, tones and vowels in healthy voices.
Procedia technology, 16:1228–1237, 2014.
[72] Abhishek Shivkumar, Jack Weston, Raphael Lenain, and Emil Fristed.
Blabla: Linguistic feature extraction for clinical analysis in multiple
languages. In Interspeech, 2020.


## Page 19


19
[73] Jean Carletta, Simone Ashby, Sebastien Bourban, Mike Flynn, Mael
Guillemot, Thomas Hain, Jaroslav Kadlec, Vasilis Karaiskos, Wessel
Kraaij, Melissa Kronenthal, et al. The ami meeting corpus: A pre-
announcement.
In International workshop on machine learning for
multimodal interaction, pages 28–39. Springer, 2005.
[74] James W Schwoebel, Joel Schwartz, Lindsay A Warrenburg, Roland
Brown, Ashi Awasthi, Austin New, Monroe Butler, Mark Moss, and
Eleftheria K Pissadaki. A longitudinal normative dataset and protocol
for speech and language biomarker research. medrxiv, pages 2021–08,
2021.
[75] Graham RD Jones, Rainer Haeckel, Tze Ping Loh, Ken Sikaris,
Thomas Streichert, Alex Katayev, Julian H Barth, Yesim Ozarda,
et al.
Indirect methods for reference interval determination–review
and recommendations. Clinical Chemistry and Laboratory Medicine
(CCLM), 57(1):20–29, 2018.
[76] Yesim
Ozarda,
Ken
Sikaris,
Thomas
Streichert,
Joseph
Macri,
IFCC Committee on Reference intervals, and Decision Limits (C-
RIDL). Distinguishing reference intervals and clinical decision limits–a
review by the ifcc committee on reference intervals and decision limits.
Critical reviews in clinical laboratory sciences, 55(6):420–431, 2018.
[77] Gary L Horowitz, S Altaie, JC Boyd, F Ceriotti, U Garg, P Horn,
A Pesce, ES Harrison, and J Zakowski. Ep28-a3c defining, establishing,
and verifying reference intervals in the clinical laboratory; approved
guideline.
San Diego: Clinical and Laboratory Standards Institute,
2010.
[78] Yesim Ozarda. Reference intervals: current status, recent developments
and future considerations.
Biochemia medica: Biochemia medica,
26(1):5–16, 2016.
[79] Kiyoshi Ichihara, James C Boyd, et al.
An appraisal of statistical
procedures used in derivation of reference intervals. Clinical chemistry
and laboratory medicine, 48(11):1537–1551, 2010.
[80] R’mani Haulcy and James Glass. CLAC: A Speech Corpus of Healthy
English Speakers. In Interspeech, pages 2966–2970, 2021.
[81] Saturnino Luz, Fasih Haider, Sofia de la Fuente, Davida Fromm,
and Brian MacWhinney.
Alzheimer’s dementia recognition through
spontaneous speech: the adress challenge. Interspeech, 2020.
[82] Juan
Rafael
Orozco-Arroyave,
Julián
David
Arias-Londoño,
Jesús
Francisco
Vargas-Bonilla,
María
Claudia
Gonzalez-Rátiva,
and Elmar Nöth.
New spanish speech corpus database for the
analysis of people suffering from Parkinson’s disease. In LREC, pages
342–347, 2014.
[83] James T. Becker, François Boiler, Oscar L. Lopez, Judith Saxton, and
Karen L. McGonigle. The Natural History of Alzheimer’s Disease:
Description of Study Cohort and Accuracy of Diagnosis. Archives of
Neurology, 51(6):585–594, 1994.
[84] Björn Schuller, Stefan Steidl, Anton Batliner, Simone Hantke, Florian
Hönig, Juan Rafael Orozco-Arroyave, Elmar Nöth, Yue Zhang, and
Felix Weninger. The interspeech 2015 computational paralinguistics
challenge: nativeness, Parkinson’s & eating condition. In Interspeech
2015, 2015.
[85] Shujie Hu, Xurong Xie, Zengrui Jin, Mengzhe Geng, Yi Wang, Mingyu
Cui, Jiajun Deng, Xunying Liu, and Helen Meng.
Exploring self-
supervised pre-trained asr models for dysarthric and elderly speech
recognition. In ICASSP 2023-2023 IEEE International Conference on
Acoustics, Speech and Signal Processing (ICASSP), pages 1–5. IEEE,
2023.
[86] Catarina Botelho, John Mendonça, Anna Pompili, Tanja Schultz, Al-
berto Abad, and Isabel Trancoso. Macro-descriptors for Alzheimer’s
disease detection using large language models. In Interspeech, 2024.
[87] Sanyuan Chen, Chengyi Wang, Zhengyang Chen, Yu Wu, Shujie Liu,
Zhuo Chen, Jinyu Li, Naoyuki Kanda, Takuya Yoshioka, Xiong Xiao,
Jian Wu, Long Zhou, Shuo Ren, Yanmin Qian, Yao Qian, Micheal
Zeng, and Furu Wei.
WavLM: Large-Scale Self-Supervised Pre-
Training for Full Stack Speech Processing. IEEE Journal of Selected
Topics in Signal Processing, 16:1505–1518, 2021.
[88] Alexei Baevski, Henry Zhou, Abdelrahman Mohamed, and Michael
Auli.
wav2vec 2.0: A Framework for Self-Supervised Learning of
Speech Representations. In Advances in Neural Information Processing
Systems, volume 33, pages 12449–12460. Curran Associates Inc., 2020.
[89] Wei-Ning Hsu, Anuroop Sriram, Alexei Baevski, Tatiana Likhoma-
nenko, Qiantong Xu, Vineel Pratap, Jacob Kahn, Ann Lee, Ronan
Collobert, Gabriel Synnaeve, and Michael Auli.
Robust wav2vec
2.0: Analyzing Domain Shift in Self-Supervised Pre-Training.
In
Interspeech, pages 721–725, 2021.
[90] Jonatas Grosman.
Fine-tuned XLSR-53 large model for speech
recognition
in
English.
https://huggingface.co/jonatasgrosman/
wav2vec2-large-xlsr-53-english, 2021.
[91] Alec Radford, Jong Wook Kim, Tao Xu, Greg Brockman, Christine
McLeavey, and Ilya Sutskever. Robust speech recognition via large-
scale weak supervision.
In International Conference on Machine
Learning, pages 28492–28518, 2023.
[92] Discourse markers (so, right, okay).
[93] David R Feinberg. Parselmouth praat scripts in python, Jan 2022.
[94] Jochen Weiner, Christian Herff, and Tanja Schultz. Speech-based de-
tection of alzheimer’s disease in conversational german. In Interspeech,
pages 1938–1942, 2016.
[95] Paul Boersma and David Weenink. Praat: doing phonetics by computer
[computer program]. Retrieved May 2024 from http://www.praat.org/,
2024.
[96] Nils Reimers and Iryna Gurevych. Sentence-bert: Sentence embeddings
using siamese bert-networks. EMNLP-IJCNLP, 2019.
[97] API. Readers’ degree of understanding, 2009.
[98] Vladimir Dobrovolskii.
Word-level coreference resolution.
In Pro-
ceedings of the 2021 Conference on Empirical Methods in Natural
Language Processing, pages 7670–7675, Online and Punta Cana,
Dominican Republic, November 2021. Association for Computational
Linguistics.
[99] Sameer Pradhan, Alessandro Moschitti, Nianwen Xue, Olga Uryupina,
and Yuchen Zhang. CoNLL-2012 shared task: Modeling multilingual
unrestricted coreference in OntoNotes. In Joint Conference on EMNLP
and CoNLL - Shared Task, pages 1–40, Jeju Island, Korea, July 2012.
Association for Computational Linguistics.
[100] Paul Boersma. Praat, a system for doing phonetics by computer. Glot.
Int., 5(9):341–345, 2001.
[101] Yannick Jadoul, Bill Thompson, and Bart de Boer.
Introducing
Parselmouth: A Python interface to Praat. Journal of Phonetics, 71:1–
15, 2018.
[102] Prasanta Chandra Mahalanobis. On the generalized distance in statis-
tics. Sankhy¯a: The Indian Journal of Statistics, Series A (2008-), 80:S1–
S7, 2018.
[103] Youri Maryn, Femke Ysenbaert, Andrzej Zarowski, and Robby
Vanspauwen.
Mobile communication devices, ambient noise, and
acoustic voice measures. Journal of Voice, 31(2):248–e11, 2017.
[104] Stephen Jannetts, Felix Schaeffler, Janet Beck, and Steve Cowen.
Assessing voice health using smartphones: bias and random er-
ror of acoustic voice parameters captured by different smartphone
types. International journal of language & communication disorders,
54(2):292–305, 2019.
[105] Judith Dineley, Ewan Carr, Faith Matcham, Johnny Downs, Richard
Dobson, Thomas F Quatieri, and Nicholas Cummins. Towards robust
paralinguistic assessment for real-world mobile health (mhealth) mon-
itoring: an initial study of reverberation effects on speech. Interspeech,
2023.
[106] Patrick E McKnight and Julius Najab.
Mann-whitney u test.
The
Corsini encyclopedia of psychology, pages 1–1, 2010.
[107] Ari Lahti, Per Hyltoft Petersen, James C Boyd, Callum G Fraser, and
Nils Jørgensen. Objective criteria for partitioning gaussian-distributed
reference values into subgroups. Clinical chemistry, 48(2):338–352,
2002.
[108] Kiyoshi Ichihara, Yoshihisa Itoh, and Christopher WK Lam et al.
Sources of variation of commonly measured serum analytes in 6
Asian cities and consideration of common reference intervals. Clinical
chemistry, 54(2):356–365, 2008.
[109] Luciana Ferrer and Pablo Riera. Confidence intervals for evaluation
in machine learning [computer software], https://github.com/luferrer/
ConfidenceIntervals.
[110] David Dernoncourt, Blaise Hanczar, and Jean-Daniel Zucker. Analysis
of feature selection stability on high dimension and small sample data.
Computational statistics & data analysis, 71:681–693, 2014.
[111] Inês Soares, Joana Dias, Humberto Rocha, Maria do Carmo Lopes, and
Brígida Ferreira. Feature selection in small databases: a medical-case
study. In XIV Mediterranean Conference on Medical and Biological
Engineering and Computing 2016: MEDICON 2016, March 31st-April
2nd 2016, Paphos, Cyprus, pages 814–819. Springer, 2016.
[112] Andrius Vabalas, Emma Gowen, Ellen Poliakoff, and Alexander J
Casson. Machine learning algorithm validation with a limited sample
size. PloS one, 14(11):e0224365, 2019.
[113] Jordan Behrendt. Demvis: Modular system for speech-based dementia
screening. Master’s thesis, University of Bremen, 2023.
[114] F. Pedregosa, G. Varoquaux, A. Gramfort, V. Michel, B. Thirion,
O. Grisel, M. Blondel, P. Prettenhofer, R. Weiss, V. Dubourg, J. Vander-
plas, A. Passos, D. Cournapeau, M. Brucher, M. Perrot, and E. Duch-
esnay. Scikit-learn: Machine learning in Python. Journal of Machine
Learning Research, 12:2825–2830, 2011.


## Page 20


20
[115] Damian Kwasny and Daria Hemmerling. Gender and age estimation
methods based on speech using deep neural networks.
Sensors,
21(14):4785, 2021.
[116] Mario Zusag, Laurin Wagner, and Theresa Bloder. Careful Whisper -
leveraging advances in automatic speech recognition for robust and
interpretable aphasia subtype classification.
In Interspeech, pages
3013–3017, 2023.
[117] Tim Head, Manoj Kumar, Holger Nahrstaedt, Gilles Louppe, and
Iaroslav Shcherbatyi. Scikit-optimize/scikit-optimize, Oct 2021.
[118] Félix Javier Jiménez-Jiménez, Javier Gamboa, Alberto Nieto, Josana
Guerrero, Miguel Orti-Pareja, Jose Antonio Molina, Esteban García-
Albea, and Ignacio Cobeta.
Acoustic voice analysis in untreated
patients with Parkinson’s disease. Parkinsonism & Related Disorders,
3(2):111–116, 1997.
[119] Savitha S Upadhya, AN Cheeran, and JH Nirmal. Statistical compar-
ison of jitter and shimmer voice features for healthy and parkinson
affected persons. In International conference on electrical, computer
and communication technologies (ICECCT), pages 1–6. IEEE, 2017.
[120] Ipek
Midi,
Muzeyyen
Dogan,
Mesrure
Koseoglu,
Gunay
Can,
Mehmet Ali Sehitoglu, and Dilek Ince Gunal.
Voice abnormalities
and their relation with motor dysfunction in parkinson’s disease. Acta
Neurologica Scandinavica, 117(1):26–34, 2008.
[121] P Brown, DM Corcos, and JC Rothwell. Does parkinsonian action
tremor contribute to muscle weakness in Parkinson’s disease? Brain:
a journal of neurology, 120(3):401–408, 1997.
[122] Leah K Bowen, Gabrielle L Hands, Sujata Pradhan, and Cara E Stepp.
Effects of parkinson’s disease on fundamental frequency variability
in running speech.
Journal of medical speech-language pathology,
21(3):235, 2013.
[123] Brian Harel, Michael Cannizzaro, and Peter Snyder.
Variability
in fundamental frequency during speech in prodromal and incipient
Parkinson’s disease: A longitudinal case study. Brain and cognition,
56(1):24–29, 2004.
[124] J Duffy. Speech motor disorders: substrates, differential diagnosis, and
management. St. Louis: Mosby, 1995.
[125] Shu Yang, Fengbo Wang, Liqiong Yang, Fan Xu, Man Luo, Xiaqing
Chen, Xixi Feng, and Xianwei Zou. The physical significance of acous-
tic parameters and its clinical significance of dysarthria in parkinson’s
disease. Scientific Reports, 10(1):11776, 2020.
[126] David A Snowdon, Susan J Kemper, James A Mortimer, Lydia H
Greiner, David R Wekstein, and William R Markesbery.
Linguistic
ability in early life and cognitive function and alzheimer’s disease in
late life: Findings from the nun study. Jama, 275(7):528–532, 1996.
[127] Romola S Bucks, Sameer Singh, Joanne M Cuerden, and Gordon K
Wilcock. Analysis of spontaneous, conversational speech in dementia
of alzheimer type: Evaluation of an objective technique for analysing
lexical performance. Aphasiology, 14(1):71–91, 2000.
[128] Visar Berisha, Shuai Wang, Amy LaCross, and Julie Liss. Tracking
discourse complexity preceding alzheimer’s disease diagnosis: A case
study comparing the press conferences of presidents ronald reagan and
george herbert walker bush. Journal of Alzheimer’s Disease, 45(3):959–
963, 2015.
Catarina Botelho received the B.S. and M.S. de-
grees in Biomedical Engineering from Instituto Su-
perior Técnico (IST), University of Lisbon, in 2018.
Currently, she is a doctoral candidate in Electrical
and Computer Engineering, at INESC-ID and In-
stituto Superior Técnico. She was a research intern
at Google AI, Toronto, and a visitor researcher at
the Cognitive Systems Lab, University of Bremen.
She was involved in the student advisory committee
of the International Speech Communication Asso-
ciation (ISCA-SAC), from 2020 to 2023, acting as
Coordinator in 2022. Her scientific interests focus on speech and language
technology and applied machine learning for healthcare.
Alberto Abad received the Telecommunication En-
gineering degree from the Technical University of
Catalonia (UPC), Barcelona, Spain, in 2002 and the
Ph.D. degree from UPC, in 2007. Currently, he is
an Associate Professor at the Department of Com-
puter Science and Engineering (DEI) of Instituto
Superior Técnico (IST) and a researcher at INESC-
ID. He is the coordinator of the Human Language
Technologies laboratory at INESC-ID and the deputy
coordinator of the Master in Computer Science and
Engineering of IST. He is also an IEEE Senior
member. His research interests include robust speech recognition, speaker and
language characterization, applied machine learning, healthcare applications,
and privacy-preserving speech processing and machine learning.
Tanja Schultz received the diploma and doctoral
degrees in Informatics from University of Karlsruhe,
Germany, and spent over 20 years as Researcher
and adjunct Research Professor at Carnegie Mellon
University, PA USA. Since 2015 she is Professor for
Cognitive Systems at the University of Bremen, Ger-
many. In 2007, she founded the Cognitive Systems
Lab where she and her team combine machine learn-
ing methods with innovations in biosignal processing
to create biosignal-adaptive cognitive systems. She
received several awards for her work and is a fellow
of ISCA (2016), EASA (2017), IEEE (2020), and AAIA (2021). Currently,
she leads the University’s high-profile area “Minds, Media, Machines”, is
a speaker of the DFG Research Unit Lifespan AI, and co-speaker of two
research training groups. Recently, she established the international Master’s
program on Artificial Intelligence and Intelligent Systems.
Isabel Trancoso is a former full professor at IST
(University of Lisbon) and President of the Scientific
Council of INESC-ID. She got her PhD in ECE
from IST in 1987. She chaired the ECE Depart-
ment of IST. She was Editor-in-Chief of the IEEE
Transactions on Speech and Audio Processing and
had many leadership roles in SPS (Signal Processing
Society of IEEE) and ISCA (International Speech
Communication Association), namely having been
President of ISCA and Chair of the Fellow Evalua-
tion Committees of both SPS and ISCA. Although
recently retired, she is still actively supervising students and playing relevant
roles in professional associations, such as Vice-Chair and Chair of the IEEE
Fellow Committee (2023, 2024). She was elevated to IEEE Fellow in 2011,
and to ISCA Fellow in 2014.


## Page 21


21
APPENDIX A
DATA PRE-PROCESSING AND FEATURE EXTRACTION
A. Sustained vowel pre-processing
As described in step 1, in section V.A, CLAC is a
crowdsourced corpus, thus it includes recordings that exhibit
anomalies, particularly in the recordings of sustained vowels.
Examples of these anomalies include recordings with very
little energy, recordings with a decrease in gain after a couple
seconds because the tool used for data collection did not
recognize the sound as speech, etc. For this reason, and to
improve the overall quality of the recordings that constitute the
reference population, data filtering was performed to remove
or segment sustained vowel recordings from CLAC, following
the twelve pre-processing steps described in Table V. The
parameters (e.g. minimum acceptable RMSE of 0.005, the
threshold of 15% for abrupt changes, and the threshold of 100
Hz for standard deviation of F0) were empirically defined.
Steps 1-12 were applied to the sustained vowel recordings
in CLAC, resulting in the exclusion of 355 (out of 2811)
recordings. Step 11 was applied to PC-GITA, resulting in the
exclusion of 12 vowel recordings, because no "stable" segment
was identified. In this dataset, there are no files with a standard
deviation of F0 larger than 100 Hz.
TABLE V
SUSTAINED VOWEL PRE-PROCESSING STEPS.
Step
Notes
1:
Exclude any files whose maximum RMSE
is below 0.005.
2:
Search for abrupt changes in the RMSE.
Changes above 15% of the RMSE
of the signal are considered abrupt
changes.
3:
IF no abrupt changes are detected
4:
Keep the recording.
5:
ELSE
6:
Extract the segments between each
abrupt change.
7:
Discard the segment after the last abrupt
change until the end of the recording.
This segment may correspond to a gain
reduction.
8:
Select the segment with the largest du-
ration (without abrupt RMSE changes) for
analysis.
9:
ENDIF
10:
Split all segments longer than 4 seconds
into chunks of 3 s, with a sliding window
of 2 s.
To approximate the average duration of
vowel segments in PC-GITA.
11:
Before feature extraction, identify a "sta-
ble" sustained vowel segment.
A "stable" segment corresponds to at
least 110 periods without voice breaks.
A voice break is considered if a period
is larger than the maximum phonation
period, set to 0.02 s. This criteria was
defined based on a speech pathologist
advice.
12:
After feature extraction, exclude the seg-
ment if the standard deviation of F0 is
larger than 100 Hz.
B. Audio samples excluded during data pre-processing and
feature extraction
Besides vowel segmentation, other steps in the method
resulted in the exclusion of audio samples from the original
pool of available samples.
The wav2vec ASR system failed to produce an output for
6 files in ADReSS (3 from the train set and 3 from the test
set).
Additionally, for some data samples, it was not possible
to extract all linguistic features. Particularly, for 9 wav2vec
Fig. 9. Distribution of ratio of ambiguous correference chains on the reference
population, based on whisper transcriptions.
transcriptions in ADReSS (4 in the test set), 15 wav2vec tran-
scriptions in CLAC, and 16 whisper transcriptions in CLAC.
Feature extraction failed because the generated transcriptions
were either too short (for example, did not contain more than
14 tokens to compute coherence), or no English words were
recognized.
The outlier removal method excluded 70 samples (28 vowels
and 42 picture description) from CLAC, out of the pool of
4,992 audio samples for which it was possible to extract all
features. These outliers represent approximately 1% of the
audio samples.
The excluded samples that belong to ADReSS and PC-
GITA were not used to train the classifiers nor to define the
best hyperparameters. However, to ensure a fair comparison
with previous literature, these excluded samples are arbitrarily
assigned the prediction "control" when reporting performance
on the test set. This reflects a 50% a priori probability of a
correct prediction due to the balanced nature of the datasets.
APPENDIX B
THE FEATURE "RATIO OF AMBIGUOUS COREFERENCE
CHAINS"
As described in section V.B of the main document, the
feature ratio of ambiguous coreference chains was excluded
from the analysis because the confidence intervals on the
upper bound for both genders and both ASR systems were
larger than the RI itself, which indicates a poor confidence
on the derived RI. Fig. 9 shows the distribution of the ratio
of ambiguous coreference chains on the reference population.
It is clear that the bulk of the distribution is very narrow
as most samples correspond to zero. This resulted in a very
narrow reference interval, and a very large confidence interval
on the upper limit upon bootstrapping. Intuitively, one can
understand that in a healthy population describing an image,
there would rarely be any ambiguous pronouns, i.e., entities
not explicitly mentioned or mentioned only cataphorically.
Table VI shows examples of picture descriptions in CLAC
and the corresponding coreference chains identified by the
coreference resolver.
Although the feature was excluded from further analysis, it
may be an interesting feature to explore, mainly when studying
the speech of schizophrenia patients [26], [27].


## Page 22


22
TABLE VI
EXAMPLES OF PICTURE DESCRIPTIONS IN CLAC AND THE
CORRESPONDING COREFERENCE CHAINS IDENTIFIED BY THE
COREFERENCE RESOLVER.
ASR
Description
Coref.
chains
wav2vec "i see a mother not paying attention to what’s hap-
pening in her kitchen she’s drying the dishes and
appears to be day dreaming while looking out the
window because she’s not paying attention the sink
is overflowing causing a flood in the kitchen and her
children are about to steal cookies from a cabinet
well most likely about to get hurt because the stoolis
about to tip over."
[’Mother’,
’Her’,
"She’S",
"She’S",
’Her’],
[’Kitchen’,
’Kitchen’]
whisper
"A young boy is walking down a path while at-
tempting to fly a kite and his dog is following him.
Behind him, there is a lake with a young girl on
the beach, building a sand castle. On that same lake
there is a gentleman on a dock, landing a fish. And
on that lake out in the distance, there’s a sailboat
sailing. Meanwhile, in the foreground, there is a
couple having a picnic. The woman is pouring a
glass of wine. There’s a stereo playing, and the man
is reading a book. Down the street, there is a house
with a car in the driveway and a tree in the front
yard and a flag at Polstaff."
[’Boy’,
’His’,
’Him’,
’Him’],
[’Lake’,
’Lake’,
’Lake’]
TABLE VII
(I) NUMBER OF AUDIO SAMPLES. (II) AVERAGE NUMBER OF FEATURES
OUTSIDE OF THE RIS, PER AUDIO SAMPLE. (III) AVERAGE FEATURE
DISTANCE TO THE LIMIT OF THE RI, PER AUDIO SAMPLE. BECAUSE WE
COULD NOT ASSUME THE VALUES FOLLOW A NORMAL DISTRIBUTION,
p −values WERE COMPUTED WITH A MANN-WHITNEY U TEST. (*)
INDICATES STATISTICALLY SIGNIFICANT DIFFERENCES BETWEEN
CONTROLS AND PATIENTS. C AND P STAND FOR CONTROLS AND
PATIENTS, AND F AND M STAND FOR FEMALE AND MALE SPEAKERS.
(i) #Samples
(ii) #Feats outside the RI
(iii) Feat dist to the RI
C
P
C
P
p-value
C
P
p-value
PC-GITA
F
75
74
1.5
3.5
0.0092*
0.006
0.131
0.0003*
M
70
69
1.4
2.0
0.327
0.008
0.038
0.0392*
ADReSS
F
43
43
3.0
4.8
0.0034*
0.014
0.050
0.0001*
M
35
35
3.3
4.6
0.004*
0.013
0.037
0.0005*
APPENDIX C
QUANTITATIVE COMPARISON OF REFERENCE AND
DISEASE-AFFECTED SPEECH
The main document includes a qualitative comparison of
reference speech and disease-affected speech. Here, a quanti-
tative analysis is provided. Table VII reports (i) the number
of samples under analysis, (ii) the average number of features
per audio sample that fall outside the RI, and (iii) the average
distance of an audio sample’s features from the RI limit.
The distance was computed as the difference between the
feature value and the RI margin, divided by the length of the
interval. If the feature value lies within the RI, the distance is
considered 0.
The table shows that AD patients have a higher average
number of features outside the RI per sample compared to
control subjects. This difference is statistically significant in
all cases, except for male speakers in PC-GITA.
More relevant than the number of features outside the
reference interval, is the distance of these features from the
interval. Table VII (iii) reports the average distance per group,
and Fig. 10 illustrates the distribution of these vales. This
distance is, on average, higher for patients, and the difference
between the two groups is considered statistically significant
for all cases.
Future work could analyse this average distance per groups
of features considered relevant for each disease.
APPENDIX D
DEVIATION-SCORES
The five deviation-scores (DS) compared were the follow-
ing:
1) DSMST D: This deviation-score, inspired by [116], is
based on the mean, µ, and standard deviation, σ, of
the feature distributions within the reference population.
For each feature i, it is computed as DSMST Di =
1 −
σi
|µi−xi| if |µi −xi| > σi else it is set to 0.
2) DSMST D−no−cap: This deviation-score is similar to the
previous one, except it is not capped at 0 when the
feature values are inside the interval [µi −σi, µi + σi].
The idea with this deviation-score was to approxi-
mate it to the log-likelihood ratio. It is computed as:
DSMST D−no−capi = |µi−xi|
σi
.
3) DSQ123: This deviation-score is proposed as an alter-
native to DSMST D, that is based on the median (Q2)
and the first and third quartiles (Q1 and Q3), instead of
the mean and standard deviation. A second modification
introduced in this deviation-score is that it yields nega-
tive or positive scores depending on whether the feature
values fall below or above the interval [Q1, Q3]. This
approach reflects the intuition that for certain features,
deviating below or above the normal range does not
carry the same implications, as discussed earlier in
section V-A–step 5. For each feature i, DSQ123i is
computed as:
DSQ123i =





2|Q3i−xi|
|Q3i−Q1i|
if xi > Q3i,
−2|Q1i−xi|
|Q3i−Q1i|
if xi < Q1i,
0
elsewhere.
(2)
4) DSRI: This deviation-score yields the same score for all
feature values inside the reference interval, i.e., between
the lower and upper bound of the reference interval,
[RILB, RIUB]. It also yields negative values for feature
values below the reference interval. For each feature i,
DSRIi is computed as:
DSRIi =





2|RIUBi−xi|
|RIUBi−RILBi|
if xi > RIUBi,
−
2|RILBi−xi|
|RIUBi−RILBi|
if xi < RILBi,
0
elsewhere.
(3)
5) DSMahalanobis: This deviation-score consists of com-
puting the Mahalanobis distance of each new audio
sample to the median (Q2) of the reference population.
Unlike the other deviation scores that are computed at
the feature level, this deviation score is multivariate and
considers the deviation of the vector of all features, x


## Page 23


23
Fig. 10. Distribution of the average distance of the features to the RI limits, per audio sample. (a) represents PC-GITA, and (b) represents ADReSS.
to the reference population. Thus, it provides a single
value for each audio sample. It is computed as follows:
DSMahalanobis =
p
(x −Q2)V −1(x −Q2)T , where V
is the covariance computed on the reference population.
The Mahalanobis distance has been employed in [55] to
compute the distance of a dysarthric speaker from the
healthy distribution, based on phonological features.
APPENDIX E
CLASSIFICATION EXPERIMENTS WITH SVM AND LR
Prior to the NAM experiments described in the main
document, classification experiments were conducted using
Support Vector Machines (SVMs) and Logistic Regression
(LR). For these experiments, two transcription types (whisper
and wav2vec based), three normalization strategies (zero-
mean and unit variance, MinMax, and no normalization), six
correlation threshold values, and five deviation-scores were
compared. To evaluate whether the deviation scores provide
an advantage over using directly the features as input to the
classifiers, an extra scenario was also considered, where the
features are directly fed to the classifiers after the stratified
normalization strategy.
The SVM hyperparameters were chosen based on a grid
search on the development folds, although on a relatively
small parameter space, to avoid getting high complexity
models, which are more prone to overfitting. The hyper-
parameters compared were: kernel ∈{linear, rbf, poly},
C ∈{0.01, 0.1, 1}, and degree ∈{2, 3}.
The best classification results on the development and test
sets are reported in Table VIII. The results obtained on the
complete set of configurations, including the different ASR
systems, deviation-scores, correlation thresholds, and normal-
ization strategies, are fully reported in [24].
For PD detection, the best classification results on the
development and test sets were achieved using deviation
score DSRI, without dimensionality reduction, with MinMax
normalization, and a logistic regression classifier. This con-
figuration achieved 71.7% accuracy on the test set. If the 12
files excluded during data preprocessing (arbitrarily labeled as
controls for a fair comparison with other works reporting on
the entire dataset) were not included, the performance would
increase to 73%. Each subject uttered 3 sustained vowels,
thus performance was also evaluated at the speaker level,
after computing the majority vote of the three predictions
per subject, resulting in 75% accuracy. The highest speaker-
level accuracy (77%) was achieved combining the deviation
score DTQ1,2,3, and the reduced dimensionality feature set
with CT = 0.9.
For AD detection in ADReSS, the best classification results
on the development folds were obtained using directly the
features that constitute the full dimensionality feature set
(CT = 1), combined with MinMax normalization, and an
SVM classifier with second degree polynomial kernel, based
on whisper transcriptions. This configuration reached 76%
accuracy on the development folds, and 69% on the held-
out test set. The best results on the held-out test set were
obtained using the deviation score DTRI, and the reduced
dimensionality feature set with CT = 0.7. Pre-processing
and feature extraction using whisper transcriptions did not
lead to the exclusion of any files from analysis. ADReSS
only contains one picture description per subject, thus the
performance reported at sample level is the same as at speaker
level.
Given the numerous variables involved in these classifica-
tion experiments, Table IX summarizes the average perfor-
mance across all experiments for each ASR model, for each
deviation-score, for each feature selection correlation thresh-
old, for each normalization strategy, and for each classifier.
Overall, whisper transcriptions yield better results than
wav2vec transcriptions. This difference is partly due to
wav2vec failing to generate a transcription for six files, and the
extraction of linguistic features based on wav2vec transcrip-
tions failing for nine additional files, which resulted in the
exclusion of 15 files from further analysis. For consistency
with other studies, the seven files in the test set were treated
as if the prediction was control.


## Page 24


24
TABLE VIII
BEST DISEASE CLASSIFICATION RESULTS, USING SVM AND LOGISTIC REGRESSION, IN TERMS OF ACCURACY (ACC), MACRO PRECISION (P), MACRO
RECALL (R), AND MACRO F1, IN [%].
Dev Folds
Test
Test – Speaker MV
CT
DT
norm
classifier
ASR
Acc
P
R
F1
Acc
P
R
F1
Acc
P
R
F1
Parkinson’s Disease
1
DTRI
MinMax
LR
–
72.2
72.7
72.2
72.1
71.7
72.2
71.7
71.5
75.0
75.5
75.0
74.9
0.9
DTQ123
MinMax
SVM (linear, C = 0.01)
–
69.4
69.9
69.4
69.2
69.7
70.2
69.7
69.5
77.0
77.9
77.0
76.8
Alzheimer’s Disease
1.0
Raw features
MinMax
SVM (poly, C = 1, d = 2)
Whisper
75.9
76.8
75.9
75.7
68.8
68.8
68.8
0.687
–
–
–
–
0.7
DTRI
None
LR
Whisper
70.4
71.8
70.4
69.9
77.1
77.5
77.1
77.0
–
–
–
–
TABLE IX
ABLATION STUDY ON THE DIFFERENT VARIABLES FOR EACH
CONFIGURATION USED IN THE DISEASE DETECTION EXPERIMENTS, USING
SVM AND LOGISTIC REGRESSION. ACCURACY IS REPORTED IN [%].
test† REFERS TO THE TEST SET DISREGARDING THE FILES THAT WERE
EXCLUDED DURING PRE-PROCESSING OR FEATURE EXTRACTION.
Parkinson’s Disease
Alzheimer’s Disease
dev
test†
test
MV
dev
test†
test
ASR
whisper
–
–
–
–
62.0
63.7
63.7
wav2vec
–
–
–
–
58.5
65.4
60.0
DT
DTMST D
61.1
61.2
60.4
63.2
62.0
63.3
60.7
DTMST D−no−cap
60.1
60.1
59.4
61.9
61.5
66.1
63.4
DTQ123
64.8
65.1
64.2
67.4
60.7
66.7
63.7
DTRI
60.8
61.2
60.4
62.6
60.7
66.9
64.1
DTMahalanobis
60.2
59.4
58.7
61.5
54.1
58.8
56.6
Raw features
63.8
64.9
64.0
66.6
62.5
65.4
62.6
CT
CT = 0.5
60.9
60.8
60.0
62.8
60.9
66.1
63.2
CT = 0.6
CT = 0.7
60.0
64.7
62.0
CT = 0.8
62.5
63.1
62.2
64.9
60.2
63.8
61.1
CT = 0.9
62.6
62.8
61.9
64.5
59.9
63.7
61.1
CT = 1
63.0
63.6
62.8
65.4
59.4
63.0
60.5
Normalization
0-mean 1-var
61.7
62.2
61.3
63.7
59.8
64.5
61.8
MinMax
65.5
65.5
64.5
68.2
59.5
65.6
62.7
None
58.2
58.3
57.6
59.7
61.4
63.5
61.0
Classifier
SVM
61.6
61.3
60.5
63.1
61.9
64.2
61.5
LR
62.0
62.6
61.8
64.6
58.6
64.8
62.2
In terms of deviation-scores, the best average performance
for PD detection was achieved by DTQ1,2,3. This trend is
not observed for AD. One partial explanation is that, with
whisper transcriptions, it was not possible to compute the
DTQ1,2,3 for the discourse marker rate feature. This issue
arose because the bulk of discourse marker rate’s data within
the reference population corresponds to a very narrow range,
leading to identical first and third quartiles, and resulting in
an indeterminate DTQ1,2,3. This feature is important for AD
detection, as discussed in the main document, and its absence
may hinder the performance of this deviation score. Using
the features directly as input to the classifier, i.e. without pre-
computing a deviation-score, yielded the best average results
on the ADReSS development folds. The best results on the
ADReSS held-out test set were obtained with DTRI.
Regarding the decision to reduce the dimensionality of the
feature set based on Pearson correlation between features,
it appears that the detection of PD benefits from using the
entire feature set, while the detection of AD benefits from the
reduced dimensionality feature set, with CT = 0.5. Notably,
the dimension of the entire feature set used to study sustained
vowels (20 features) is very similar to the dimension of the
reduced set used for studying the picture description task (23
features).
The normalization strategy that appears to provide the best
average results, for both PD and AD, is MinMax scaling, with
the exception of the development folds in AD detection. Future
work should further investigate the different normalization
strategies, understand their impact, and discuss their inherent
assumptions.
Finally, logistic regression appears to achieve better results
than support vector machines. It is possible that the deviation-
scores already provide substantial information, and thus a
simpler classifier is sufficient. In fact, for AD detection, SVM
achieves better results than LR on the development folds, but
these are not generalized to the test set.
APPENDIX F
NEURAL ADDITIVE MODELS: ARCHITECTURE AND
HYPERPARAMETERS
The hyperparameter tuning for NAM was performed with
Bayesian optimization using Gaussian Processes, as imple-
mented in scikit-optimize [117], with 100 calls to the opti-
mizer. The hyperparameters considered for tuning, with minor
variations from those described in [22], were as follows:
• learning rate: {0.001, 0.002, 0.005, 0.01, 0.02, 0.05, 0.1},
• dropout
coefficient:
{0, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6,
0.7, 0.8, 0.9},
• weight decay: [0.000001, 0.0001],
• feature dropout coefficient: {0, 0.05, 0.1, 0.2}
• output penalty coefficient: [0.001, 0.1].
Additionally, the feature subnetworks were configured in
one of the following ways: (i) one feedforward layer with 1024
hidden units, (ii) one feedforward layer with 512 hidden units,
or (iii) three feedforward layers with 64, 64, and 32 hidden
units. The activation functions for the hidden units were either
ReLU or ExU, as introduced by [22]. The batch size was set
to 64.
Agarwal et al. [22] suggested using an ensemble of 10 to
100 models for each NAM. In this work, given the 10-fold
cross-validation setting, we defined each NAM as an ensemble
of 3 models, which after cross-validation results in a total of 30
models. Future work should investigate increasing the number
of models.


## Page 25


25
TABLE X
BEST PARAMETERS FOUND FOR NAMS ON CLASSIFICATION OF PD AND
AD, ON PC-GITA AND ADRESS, RESPECTIVELY. “HIDDEN UNITS”
SHOWS THE NUMBER OF HIDDEN LAYERS AS WELL AS THE NUMBER OF
NEURONS USED IN EACH LAYER FOR EACH FEATURE NETWORK.
PC-GITA
ADReSS
Learning rate
0.01
0.1
Dropout
0.8
0.6
Weight decay
1 × 10−6
1 × 10−6
Feature dropout
0.0
0.2
Output penalty
0.001
0.001
Num units
1024
1024
Activation
ExU
ExU
Table X reports the hyperparameters that yielded the best
performance for the classification of PD and AD.
## Related

- [[11_KNOWLEDGE/_arxiv_md/2024/2024-09/2409.12071v2_Quantifying_the_role_of_supernatural_entities_and_the_effect_of_missing_data_in_.md|2409.12071v2_Quantifying_the_role_of_supernatural_entities_and_the_effect_of_missing_data_in_]]
- [[11_KNOWLEDGE/_arxiv_md/2024/2024-09/2409.10096v3_Robust_Reinforcement_Learning_with_Dynamic_Distortion_Risk_Measures.md|2409.10096v3_Robust_Reinforcement_Learning_with_Dynamic_Distortion_Risk_Measures]]
- [[11_KNOWLEDGE/_arxiv_md/2024/2024-09/2409.10138v1_A_Method_for_Accurate_Spatial_Focusing_Simulation_via_Numerical_Integration_and_.md|2409.10138v1_A_Method_for_Accurate_Spatial_Focusing_Simulation_via_Numerical_Integration_and_]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: 2409_10230v1_speech_as_a_biomarker_for_disease_detection
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2024/2024-09/2409_10230V1_SPEECH_AS_A_BIOMARKER_FOR_DISEASE_DETECTION.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

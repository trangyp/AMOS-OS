---
canon-group: reference
rscf-state: source-claim
arxiv_id: 2402.07645v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 2402.07645v1_Detecting the Clinical Features of Difficult-to-Treat Depression using Synthetic Data from Large Language Models

> Source: 2402.07645v1_Detecting the Clinical Features of Difficult-to-Treat Depression using Synthetic Data from Large Language Models.pdf

> Pages: 23

---


## Page 1


Detecting the Clinical Features of Difficult-to-Treat Depression using
Synthetic Data from Large Language Models.
Isabelle Lorge∗, Dan W. Joyce†‡, Niall Taylor∗, Alejo Nevado-Holgado∗,
Andrea Cipriani∗§¶, Andrey Kormilitzin∗
Abstract
Difficult-to-treat depression (DTD) has been
proposed as a broader and more clinically com-
prehensive perspective on a person’s depressive
disorder where despite treatment, they continue
to experience significant burden. We sought
to develop a Large Language Model (LLM)-
based tool capable of interrogating routinely-
collected, narrative (free-text) electronic health
record (EHR) data to locate published prognos-
tic factors that capture the clinical syndrome
of DTD. In this work, we use LLM-generated
synthetic data (GPT3.5) and a Non-Maximum
Suppression (NMS) algorithm to train a BERT-
based span extraction model. The resulting
model is then able to extract and label spans
related to a variety of relevant positive and neg-
ative factors in real clinical data (i.e. spans
of text that increase or decrease the likelihood
of a patient matching the DTD syndrome). We
show it is possible to obtain good overall perfor-
mance (0.70 F1 across polarity) on real clinical
data on a set of as many as 20 different factors,
and high performance (0.85 F1 with 0.95 pre-
cision) on a subset of important DTD factors
such as history of abuse, family history of affec-
tive disorder, illness severity and suicidality by
training the model exclusively on synthetic data.
Our results show promise for future healthcare
applications especially in applications where
traditionally, highly confidential medical data
and human-expert annotation would normally
be required.
1
Introduction
Major depressive disorder (MDD) is highly preva-
lent with a heavy economic, social and personal
∗Department of Psychiatry, University of Oxford, UK
†Civic Health Innovation Lab and Institute of Population
Health, University of Liverpool, UK
‡Mersey Care NHS Foundation Trust, UK
§Oxford Health NHS Foundation Trust, Warneford Hos-
pital, UK
¶Oxford Precision Psychiatry Lab, NIHR Oxford Health
Biomedical Research Centre, UK
burden of disability worldwide and affecting up
to 6-12% of the adult global population, a propor-
tion which has been rising in the last few years
(Santomauro et al., 2021). The DSM-V (Diagnos-
tic and Statistical Manual of Mental Disorders V)
operationalises MDD as a continuous period of at
least two weeks characterised by a change in mood
leading to loss of interest or pleasure in activities,
along with other symptoms such as weight loss or
gain, sleep or cognitive issues and suicidal thoughts
causing substantial distress or impairment to func-
tioning (American Psychiatric Association et al.,
2013).
Depressive disorders are conditions with sub-
optimal treatment outcomes, with up to 70% of
patients failing to achieve remission after receiv-
ing pharmacological treatment (Caldiroli et al.,
2021). This led to the development of the con-
cept of treatment-resistant depression (TRD) and
although definitions vary (Brown et al., 2019) a
common point of consensus is the failure to achieve
treatment response after sequential, adequate-
duration and minimally-effective dosed trials of
two antidepressant-class medications. Designating
a patient as having TRD focuses on acute-phase
symptom improvement in response to pharmaco-
logical intervention.
Despite these efforts at refining the definition
of depression to address treatment responsiveness,
the cumulative rate of chronicity and lack of re-
sponse or remission amongst MDD patients re-
mains high, with around 30% of patients not achiev-
ing remission even after four courses of antidepres-
sants (Rush et al., 2006). In addition, treatment
resistant depression may be associated with higher
risks of suicide (Papakostas et al., 2003). This
underlines the importance of improving the iden-
tification of the relevant features (or signature) of
people with depression where treatment has not
provided adequate remission.
The relatively new concept of difficult-to-treat
1
arXiv:2402.07645v1  [cs.CL]  12 Feb 2024


## Page 2


depression is proposed McAllister-Williams et al.
(2020) as a more comprehensive model that empha-
sises biomedical, psychological and social factors
and interventions that may influence response to
treatment beyond the acute symptomatic response
to pharmacological interventions in TRD.
2
Machine learning models for treatment
outcome prediction
A number of studies have examined the use of ma-
chine learning (ML) techniques to directly identify
treatment response (Perlis, 2013; Nie et al., 2018).
Several of these re-use the Sequenced Treatment
Alternatives to Relieve Depression (STAR*D) co-
hort dataset (Rush et al., 2006), where four suc-
cessive treatment steps were administered, patients
having the option of exiting the study if they ex-
perienced sufficient remission of symptoms after
a given step. These ML studies identified pre-
dictive features including depression severity, the
presence of co-morbid physical illness, psychosis,
Post-Traumatic Stress Disorder (PTSD), anxiety
disorder alongside minority ethnic heritage, work
and poor social adjustment. Other factors identi-
fied in later studies include recurrence of depressive
episodes, age, response to a first antidepressant, sui-
cidality, educational attainment and occupational
status (Kautzky et al., 2017, 2019). Another re-
cent study uses age, gender, race, diagnostic codes
(including both ICD-9 and ICD-10), current pro-
cedural terminology codes and medications with
a tree-based algorithm (Lage et al., 2022). These
studies achieved relatively good performance us-
ing traditional ML models such as random forests,
GBDT (gradient-boosted decision trees) and logis-
tic regression, however they use data from struc-
tured data fields in electronic health records (EHRs)
and focus on delivering a binary TRD outcome.
In addition to the above studies using structured
data fields, a few studies have used terms extracted
from narrative EHR notes, notably Perlis et al.
(2012), who leverage regular expressions to ex-
tract terms identified by clinicians as important for
prediction and compare the outcome of a model
trained with billing data to a logistic regression
model trained with concepts extracted from narra-
tive notes, finding that the latter performs substan-
tially better. Similarly, Sheu et al. (2023) use a
variety of deep learning models with features from
both categorical variables and terms extracted from
narrative notes using regular expressions (pattern
matching) as well as Longformer vectors of the
clinical note history to predict treatment outcome.
Thus, previous works leveraged either structured
categorical data (e.g., registered comorbidity, socio-
demographic factors etc.), overall scores on stan-
dardised questionnaires, terms extracted from notes
using rule-based techniques such as regular expres-
sions or, in the case of Sheu et al. (2023), a non-
explainable vectorised representation of the full
patient history.
An alternative is to use Natural Language Pro-
cessing (NLP) models trained to extract informa-
tion from the narrative clinical notes (Vaci et al.,
2020; Kormilitzin et al., 2021). For example, re-
cent work by Kulkarni et al. (2024) uses a BERT
model for extracting suicidality and anhedonia in
mental health records using ground-truth manually
annotated EHR data.
NLP models are both flexible and ecologically
valid, and have been increasingly used successfully
for various applications in psychiatry (Vaci et al.,
2021; Senior et al., 2020) and clinical neuroscience
in recent years (Le Glaz et al., 2021; Liu et al.,
2022). The models can be trained either to directly
predict a phenotype based on treatment outcome
using text features as in Sheu et al. (2023) or, as
in the current study, to extract relevant features
suggestive of a phenotype or syndrome (e.g., in
the case of DTD, a history of abuse, self-harm
and suicidality) to present to clinicians for decision
making. However, there are significant hurdles
to obtaining training data, such as data scarcity
and the high financial and time cost of manual
annotations.
3
Difficult-to-treat depression
Difficult-to-treat depression or DTD is a more re-
cent framework than TRD which was developed
following a number of issues becoming apparent
with using the latter concept.
As described in
McAllister-Williams et al. (2020):
• The current definition of TRD largely ig-
nores psychotherapy and neurostimulation
treatments
• The definition does not allow for differential
levels of success in response or remission
• The phrasing could imply treatment failure is a
property of the patient, rather than inadequacy
of the intervention


## Page 3


• The term implies a medical model which may
exclude social and environmental factors pre-
viously shown to be significant predictors of
treatment response
For these reasons, the more inclusive and flexi-
ble concept of difficult-to-treat depression was put
forward by an international consensus group and
a number of factors were identified through litera-
ture review and expert consensus, grouped under
the categories of PATIENT, ILLNESS and TREAT-
MENT factors (McAllister-Williams et al., 2020).
Given the novelty of the framework, there have
been few attempts to operationalise it, with the
exception of Costa et al. (2022) who partitioned
patients from five specialist mental health National
Health Service (NHS) Trusts according to a crite-
rion encompassing both recurrence and resistance
(at least 4 unsuccessful treatments including two an-
tidepressant medications) and analysed correlations
with environmental and clinical factors, confirming
previous findings. In the current work, we use the
concept of difficult-to-treat depression rather than
treatment-resistant depression.
4
Large Language Models and synthetic
data for medical and mental health
research
The recent development of large language mod-
els (LLMs) with substantially increased size and
capabilities allowed great strides of improvement
across domains such as question answering and
text summarisation, including in the biomedical
domain (Agrawal et al., 2022; Hu et al., 2023;
Liu et al., 2023; Tang et al., 2023a; Taylor et al.,
2023); becoming potentially able to perform in-
formation extraction on large quantities of data.
However, privacy considerations prevent directly
feeding highly-confidential patient data into LLM
APIs such as OpenAI’s chatGPT (Brown et al.,
2020). In addition, while LLMs show impressive
performance in applications related to text gener-
ation, they still fall short of specifically trained
SOTA systems on biomedical NLP tasks (Ateia
and Kruschwitz, 2023). A recent paper demon-
strated that even when fine-tuned on target tasks,
a LLaMA model, (Touvron et al., 2023) orders of
magnitude bigger (7B vs 100M) and requiring sub-
stantially more compute power still underperforms
compared to BERT-based discriminative models
by up to 10% (Yang et al., 2023). For these rea-
sons, a paradigm is emerging whereby a smaller
local domain or task-specific model is fine-tuned
on synthetic labelled data generated by an LLM,
mitigating concerns of privacy as well as efficiency.
This paradigm has been used successfully for
diagnosis and mortality prediction by Kweon et al.
(2023), who generated synthetic clinical notes us-
ing GPT3.5-turbo (Brown et al., 2020) and trained a
domain specific LlaMA model, and for Named En-
tity Recognition and Relation Extraction by Tang
et al. (2023b), who used prompts involving named
entities and gene/disease relations from PubMed
and fine-tuned BERT family models. Another re-
cent work uses LLM-generated synthetic data to
augment gold annotated data training a Flan-T5
model to perform multilabelling of sentences for
social determinants of health (SDoH) such as hous-
ing, employment, transportation, parental status, re-
lationship status and social support (Guevara et al.,
2024). However, perhaps due to the small amount
of added synthetic data (1800 synthetic sentences
added to over 30k gold sentences), the synthetic
addition does not lead to substantial or consistent
improvement in performance (in fact it sometimes
worsens it) and the performance training with syn-
thetic data only is extremely poor (< 0.1 F1). In
the domain of psychiatry, another study augmented
training data with LLM-generated interviews and
used traditional machine learning classifiers for
binary classification of Post-Traumatic Disorder
(PTSD) with a 10% increase in performance (Wu
et al., 2023).
The generated synthetic data has the potential to
mimic important statistical properties and patterns
of real data while avoiding the expensive and effort-
ful process of obtaining large quantities of labelled
data. Therefore, we intend to attempt training a
DTD feature span extraction model exclusively on
synthetic data obtained from LLMs.
5
Aims
Previous studies used machine learning techniques
to predict treatment response or identify treatment-
resistant depression. In contrast, the more com-
prehensive concept of difficult-to-treat depression
allows us to leverage a wider variety of factors –
rather than relying on a strict ‘two-course’ acute-
phase response to pharmacological interventions –
that potentially enables early detection and more
personalised care that addresses reasons for sub-
optimal treatment response. Recent research has
indeed been focusing on early detection and linking


## Page 4


prognostic factors with a continuum of treatment
response (Lage et al., 2022; Sheu et al., 2023).
Furthermore, previous works mostly focused on
sentence classification rather than the more com-
plex process of span extraction. Contrary to multi-
labelling, span extraction presents clinicians with
the specific part of the text which is linked to a
particular label, allowing them to focus more ef-
ficiently on relevant information. Finally, to our
knowledge no previous study successfully trained a
model exclusively on synthetic data for the purpose
of extracting prognostic factors. Success, even par-
tial, would represent an extremely important step
in developing AI applications for healthcare, given
the known issues of data scarcity and manual la-
belling costs.
Therefore, the present paper aims to:
• Add to the recent body of works demonstrat-
ing the utility of leveraging synthetic data for
decision-supporting information extraction in
biomedical domains
• Introduce an annotation scheme (abductive
annotation) that leverages domain experts on
narrative clinical notes to facilitate explicit ex-
traction of PATIENT, ILLNESS and TREAT-
MENT related-factors for DTD
• Build a curated synthetic dataset of annotated
narrative clinical notes which can be freely
shared with the research community
• Build and train a model which extracts spans
of text and labels them with the relevant factor
with the goal of downstream clinician decision
guidance 1
6
The DTD Phenotype
In consultation with a clinician expert, we opera-
tionalise the prognostic factors originally reported
in McAllister-Williams et al. (2020) into the an-
notation schema presented in Table 1. There are
several reasons for the changes made. First, we aim
to develop a schema which could potentially be ex-
tended to other conditions or strata of populations
(e.g. we created general categories for physical
and mental comorbidities). Second, because we
leverage the use of a large language model for gen-
erating and annotating data, we endeavour to create
labels which are semantically transparent enough
1The code and synthetic data are available at https://
github.com/isabellelorge/dtd
that they are likely to be understood by the model
and yield better annotation accuracy.
Finally, When a clinician interprets the data con-
tained in a patient’s EHR (e.g., to establish a di-
agnosis) they will employ abductive (rather than
inductive or deductive) reasoning (Douven, 2021;
Rapezzi et al., 2005; Altable, 2012; Reggia et al.,
1985) meaning they will seek evidence to support
or refute a number of competing hypotheses (e.g.,
differential diagnoses). Consequently, we wish to
be able to extract both positive and negative evi-
dence in favour or against a designation of difficult-
to-treat depression in order to provide clinicians
with a comprehensive picture of the patient’s cur-
rent presentation, illness and treatment history for
downstream decision making.
7
Synthetic dataset
In the first instance, we prompt ChatGPT (GPT3.5-
turbo-0613) through its Python API to generate
and annotate a dataset of 1000 clinical notes with
labels from our annotation schema (e.g., [PA-
TIENT_FACTOR(POSITIVE):older_age]).
We
used a temperature of 1.2 and default values for
remaining parameters. Experimenting with vari-
ous prompts, we find that the best prompts balance
the need to provide examples to correct recurrent
mistakes in model’s behaviour against the tendency
for the model to frequently repeat given examples,
even with a high temperature parameter to encour-
age diversity in token generation. We thus add
examples as needed to correct various errors (ten-
dency to not label age, to output only positive la-
bels, to group all labels after the sentence rather
than after the relevant span, etc.). An example gen-
erated annotated note can be found in Appendix A
and the final prompt used can be found in Appendix
B. We notice from manual inspection of examples
that the output is relatively accurate, though the
model does output errors, meaning that the labels
are noisy and should be considered as a silver rather
than gold standard.
We use a combination of regular expressions
and heuristics to extract labels from each sentence,
discarding labels which do not fit our schema
(in a small proportion of notes the model hallu-
cinates new factors or uses a different formatting).
We first experiment with a syntactic heuristic to
extract shorter spans (labelling the closest finite
verb phrase with each label) but eventually set-
tle on a simpler heuristic of labelling all text be-


## Page 5


Factor
Orig.
New
NO_ANNOTATION
10708
35884
family_member_mental_disorder_POS
1188
2337
childhood_abuse_POS
1052
2116
non_adherence_POS
954
1919
side_effects_POS
883
1768
recurrent_episodes_POS
876
1774
multiple_antidepressants_POS
862
1744
multiple_psychotherapies_POS
860
1726
physical_comorbidity_POS
824
1673
long_illness_duration_POS
796
1603
severe_illness_POS
732
1447
anhedonia_POS
731
1449
suicidality_POS
706
1396
antidepressant_dosage_increase_POS
705
1420
multiple_hospitalizations_POS
668
1345
older_age_POS
545
1138
mental_comorbidity_POS
473
941
improvement_POS
403
786
substance_abuse_POS
400
787
illness_early_onset_POS
382
751
substance_abuse_NEG
314
787
multiple_hospitalizations_NEG
247
1375
suicidality_NEG
160
1178
older_age_NEG
140
960
physical_comorbidity_NEG
135
1133
abuse_POS
94
187
improvement_NEG
78
721
mental_comorbidity_NEG
64
680
non_adherence_NEG
60
709
abuse_NEG
53
690
childhood_abuse_NEG
42
805
family_member_mental_disorder_NEG
34
996
side_effects_NEG
29
701
antidepressant_dosage_increase_NEG
18
506
multiple_psychotherapies_NEG
16
746
multiple_antidepressants_NEG
11
587
long_illness_duration_NEG
7
567
severe_illness_NEG
6
488
recurrent_episodes_NEG
6
718
illness_early_onset_NEG
5
382
anhedonia_NEG
4
541
Table
1:
Annotation
schema
labels
and
span
counts for original and new (final) datasets.
We
shorten the polarity words in the table for space
considerations (the labels used in prompts and
GPT3.5-turbo outputs use full words, e.g., [PA-
TIENT_FACTOR(POSITIVE):older_age]).
fore each label up to sentence boundary (e.g., for
’XXXXX [label_X] YYYYY [label_Y]’, we extract
XXXXX as span for label X and YYYYY for label
Y). This is because early prompt attempts showed
that when prompting chatGPT for span boundaries
(e.g., ’YYYYY{XXX} [label_X]’), the boundaries ob-
tained were very error-prone and unreliable, while
a strategy of simply asking the model to insert the
label after each relevant span yielded much better
results.
From the span counts in Table 1, it can be seen
that the label distribution is heavily skewed, with a
very strong bias in favour of positive factors against
negative factors. We believe this would reflect clin-
icians’ annotations, as positive evidence is much
more likely to be expressed and noticed than nega-
tive evidence and arguably contributes more heav-
ily to final decision making. However, to reduce
data imbalance we prompt the model for another
1000 notes with the same prompt and a third set
of 1000 notes with a prompt asking exclusively
for negative labels. The final dataset thus contains
3000 notes which yield 75094 sentences. The up-
dated factor counts of the final dataset can be seen
in Table 1 and the negative prompt can be found in
Appendix C.
We explore the word distribution for each factor
to try and get a sense of the synthetic dataset’s
diversity and/or repetitiveness. To achieve this, we
extract words from labelled spans for each label
and calculate their TF-IDF score, defined as:
tfidf_score = (wl/Wl)/ log(w/wl + 1)
(1)
Where wl is the frequency of a given word for
a given label, Wl is the total number of words
for the label and w is the total frequency for the
word across labels. A sample of labels and their
10 highest scoring words can be seen in Table
2, along with their prevalence (number of occur-
rences/number of label spans). Interestingly, while
there is a tendency for the model to repeat exam-
ples given in the prompt, the extent of this be-
haviour varies substantially depending on specific
examples. Indeed, while our prompt example for
family_member_mental_disorder_POSITIVE men-
tions anxiety, the most frequent disorder which
appears for this label is bipolar disorder (48% of
spans), whereas an overwhelming 80% of spans
labelled with mental_comorbidity_POSITIVE do
include the word ‘anxiety’ without having been
prompted with it. Similarly, our prompt example
for childhood_abuse_POSITIVE mentions moth-
erly abuse but only 19% of spans with this label
contain the word ‘mother’, superseded by 34% of
spans mentioning the word ‘father’. The physi-
cal_comorbidity_POSITIVE factor is more evenly
distributed than mental_ comorbidity_POSITIVE,
with most frequent conditions split between hyper-
tension, diabetes and fibromyalgia. The model
displays strong biases which are not driven by
prompt examples, as evidenced by 70% of sub-
stance_abuse_POSITIVE spans mentioning the
word ‘alcohol’. We hypothesise that the above
biases result from the distribution of the model’s
training data.


## Page 6


We also note that spans from some labels
have a high probability of mentioning all label
words explicitly: abuse, both NEGATIVE (91%)
and POSITIVE (80%), side_effects, both POSI-
TIVE (88%) and NEGATIVE (84%), improvement,
both POSITIVE (84%) and NEGATIVE (73%),
substance_abuse_NEGATIVE (84%) and child-
hood_abuse, both NEGATIVE (76%) and POS-
ITIVE (75%). There is a tendency for the model to
mention label words explicitly more often for neg-
ative than positive labels, probably due to higher
variety for spans providing positive evidence. Only
10% of spans for physical_comorbidity_POSITIVE
and mental_comorbidity_POSITIVE mention label
words explicitly, suggesting that the model still re-
lies on its training data for phrasing and does not
systematically repeat prompt labels. The numbers
for all labels can be seen in Figure 3 in Appendix
D.
Finally, to assess the similarity in word overlap
between pairs of spans for a given label we cal-
culate the Jaccard similarity between lemmatized
words of each pair of spans within a label. The
similarities range from 0.02 for spans with no label
to 0.35 for substance_abuse_NEGATIVE. The full
numbers for all labels can be seen in Figure 4 in
Appendix D.
8
Real-World clinical data
To evaluate the performance of the developed
model on real clinical data, we utilised a sample of
de-identified secondary mental health records from
the Oxford Health NHS Foundation Trust, which
provides mental healthcare services to approxi-
mately 1.2 million individuals across all ages in
Oxfordshire and Buckinghamshire in England. Ac-
cess to the de-identified data was obtained through
the Clinical Record Interactive Search (CRIS) sys-
tem powered by Akrivia Health, which enables
searching and extraction of de-identified clinical
case notes across 17 National Health Service Men-
tal Health Trusts in England. For this study, we
sampled clinical summaries for 100 adult patients
over 18 years old, randomly selected from 19,921
patients with confirmed diagnosis of depression
(ICD-10 codes F32 and F33) readily available from
structured data fields in CRIS.
Access to and use of de-identified patient records
from the CRIS platform has been granted exemp-
tion by the NHS Health Research Authority for
research reuse of routinely collected clinical data.
Factor
Words
%
family
member
mental
disorder
family
bipolar
history
disorder
mental
mother
illness
diagnosed
reports
sister
0.72
0.48
0.87
0.65
0.68
0.44
0.65
0.39
0.41
0.16
childhood
abuse
childhood
abuse
emotional
neglect
father
history
physical
experienced
discloses
mother
0.83
0.95
0.56
0.30
0.34
0.46
0.35
0.22
0.11
0.19
physical
comor-
bidity
hypertension
physical
diabetes
comorbidities
pain
chronic
fibromyalgia
medical
comorbidity
history
0.38
0.62
0.29
0.31
0.19
0.22
0.14
0.25
0.24
0.41
mental
comor-
bidity
anxiety
generalized
disorder
comorbid
also
mental
panic
diagnosis
diagnosed
comorbidity
0.80
0.47
0.77
0.28
0.31
0.23
0.08
0.14
0.16
0.15
substance
abuse
alcohol
substance
abuse
history
use
mechanism
patient
specifically
cope
also
0.70
0.82
0.85
0.53
0.20
0.10
0.34
0.17
0.10
0.23
Table 2: Sample factors with their 10 highest TFIDF
scoring words and their % or prevalence (n occur-
rences/n spans).
The project was reviewed and approved by the
Oversight Committee of the Oxford Health NHS
Foundation Trust and the Research and Develop-
ment Team.


## Page 7


9
Task
We extract character indexes of start, end and corre-
sponding label for labelled spans in each sentence
and remove label text from sentence text. There
are 41 labels (positive and negative polarity label
for each factor and a ’NO_ANNOTATION’ label).
10
Models
Figure 1: Span-level model architecture.
We experiment with a variety of models trading
off complexity and granularity.
10.1
Token-level
The first model simply leverages a BERT (base,
cased) layer for classification at the token level,
thus spans are represented as contiguous series
of tokens labelled with a specific label. We use
one linear layer and no IOB flags (given that each
span starts where the previous span ends). The
output of the classification layer for each token
is fed to a softmax activation layer which outputs
probabilities for each label. This is similar to the
traditional technique used for Named Entity Recog-
nition (NER). We use a custom Pytorch class and
Huggingface’s transformers library (Wolf et al.,
2019) implementation for the BERT layer.
10.2
Span-level
Given the longer lengths of our spans compared
to traditional NER tasks, we also experiment with
a model inspired from Question Answering (QA)
systems, where the model does not predict a label
for each token in the sequence but instead predicts
a ‘start’ and ‘end’ position. However, traditional
Question Answering systems are generally limited
to one response span, restricting the scope of the
classification task, while in our case there can po-
tentially be any number of spans within a given
sequence, each of which could be of any length, ex-
panding the training search space exponentially. To
solve this issue, we follow Hu et al. (2019) and take
inspiration from computer vision by using a variant
of Non-Maximum Suppression (NMS), whereby
non-overlapping outputs are selected in decreasing
order of confidence. To achieve this, a separate
classifier is trained to predict the number (N) of
spans within a sequence from the sequence output
of a BERT (base, cased) layer, and subsequently the
top N non-overlapping start/end pairs with the high-
est combined probabilities are selected. We find
that given start and end of sentences consistently
have very high probabilities for our dataset (since
spans are full sentences in cases where there is a
single factor in the sentence), a greedy approach
on combined start/end probabilities as used by Hu
et al. (2019) does not work. Instead, we predict
the number (N) of spans and separately select the
top N starts and N ends with highest probabilities,
which we order by token number so that we select
non-overlapping start/end combinations in order
by taking the closest end for each start (e.g., if 2
predicted spans with top starts [1, 10] and top ends
[20, 10], the indexes are ordered so that the first
span is not [1, 20] but [1, 10], and the second span
is [10, 20]). The model goes through each selected
start/end pair and uses a linear layer span classifier
to label the relevant tokens from the sequence. For
training (given possible inconsistencies between
true and predicted number of spans), the output
of the span classifier is passed through a softmax
layer and all predicted spans are max pooled into
a single vector to match the ground truth multil-
abel one-hot encoded vector for the full sentence
(soft selection). At inference time, the indices of
the maximum probability for each predicted span
are taken as labels (hard selection). We also exper-
iment with a version of the model where factors
are merged together across polarities and a separate
classifier is trained to predict negative polarity from
a concatenation of the BERT sequence output and
predicted labels 2. As for the token-level model,
we implement a custom class and loss function in
Pytorch and leverage Huggingface’s implementa-
tion of the BERT layer. The architecture of the
2The results are substantially worse and in the interest of
space considerations we do not report them.


## Page 8


span-level model can be seen in Figure 1.
10.3
Sentence-level
Finally, we also model the task in a simplified way
as a multilabel sentence classification task. For this,
we again leverage the sequence output of a BERT
(base, cased) layer which we feed to a linear classi-
fier layer. The output of the classifier is then passed
through a sigmoid activation layer and labels with
probabilities above a 0.5 threshold are taken as pre-
dictions. In this case the start and end positions of
spans for the predicted labels are unknown. Again,
we use Huggingface’s BERT layer implementation
and a custom Pytorch class for classification with
one linear layer.
11
Training
We split the synthetic dataset into train, develop-
ment and test sets with proportions 0.8, 0.1 and 0.1.
We use a batch size of 16, learning rate of 3e-05,
dropout rate of 0.1 and weight decay of 0.001. We
experiment with different forms of class weights
to mitigate the imbalance in labels. For the span
model, we find the model performs better with a
logarithmically scaled class weighted loss, whereas
there is no difference for the token level model, and
the sentence-level model performs better without
class weights. We train until convergence, 4 epochs
for span, 5 epochs for the token model and 7 epochs
for the sentence-level model.
12
Experiments
12.1
Synthetic data
We first test the model on a held-out test set of
synthetic data.
12.1.1
Results
The results on the synthetic test set for the three
models can be seen in table 3 and a log-scaled con-
fusion matrix can be seen in Figure 2 3. Given the
imbalance in labels, we present precision, recall
and F1 for each class as well as F1 averaged across
classes, with macro averaged F1 being the accepted
standard metric in similar tasks. The three models
3While we used simplified terms in our labels to ensure
the best LLM output after prompting trial and error, the ap-
propriate medical terms should be used in the final output
of the model for the following: episodes severity for severe
illness, episode remission for improvement, medical comor-
bidity for physical comorbidity, substance use for substance
abuse, adequate dosage for antidepressant dosage increase
and adherence medication for non-adherence.
perform fairly well. We find our custom span-level
model outperforms the simpler, token-level model
by a large margin (0.65 vs 0.57). To our surprise,
we also find that our span level model slightly out-
performs the sentence-level classification model,
despite the added difficulty of having to predict the
correct start and end of spans in order to be able
to accurately predict labels. The models tend to
perform substantially better on the positive classes.
The sentence and span level models perform
similarly across factors, each claiming best per-
formance for an approximately equal number of
factors, whereas the token-level model only out-
performs other models for the abuse_POSITIVE
class. There appears to be little difference between
the performance for the different factor domains
(PATIENT, ILLNESS and TREATMENT).
We notice that the model struggles with the cat-
egory ‘older age’, which points to a well-known
shortcoming of language models (along with nega-
tion) regarding ability to count and evaluate quan-
tities. The confusion matrix in Figure 2 shows
how the category gets confused with most other
classes (lit up vertical line). The worst performing
positive classes is abuse_POSITIVE (most likely
due to scarcity of training examples) and worst per-
forming negative class is improvement_NEGATIVE.
Examination of synthetic data reveals GPT3.5
particularly struggled with correctly labelling
negative examples of improvement, which led
to many being in fact positive examples (e.g.,
There has been improvement in symptoms [ILL-
NESS_FACTOR:improvement(NEGATIVE)]). This
seems in fact to be a side-effect of GPT3.5’s ‘com-
mon sense’, indeed all other negative classes indi-
cate a positive outlook (e.g., no history of abuse
or disorder, no substance use, no hospitalisations,
etc.), thus when prompted for negative examples
the LLM produced sentences coherent with the rest
of the note, i.e., sentences mentioning improve-
ment. The secondary lit up diagonal on the left
of the confusion matrix confirms that the model
struggles with negation, with a tendency to predict
the positive counterpart for negative classes and
vice versa (right-hand side diagonal).
12.2
Clinical data
While performance of the span extraction model is
well above chance, it still appears low given that we
are testing the model within distribution (i.e., on the
same synthetic data it was trained with) with the ex-


## Page 9


Figure 2: Log-scaled confusion matrix (synthetic data).


## Page 10


pectation of a drop in performance when taken out-
of-distribution (i.e., to EHR clinical data). Grounds
for this concern are confirmed by a first test on a
test set of 482 sentences from the above mentioned
electronic health records annotated by a consultant
psychiatrist for our target features, which yields
quite a low overall performance (0.30 F1). This
prompts us to further examine the synthetic train-
ing data and to perform in-depth error analysis to
understand the reasons underlying the low perfor-
mance both on the synthetic and on the clinical test
sets. The analysis reveals the following issues:
• Many spans are mislabelled across labels
• Many spans tend to be repetitive/reuse the
same words for a given label (e.g., ‘family’ for
family disorder, ‘abuse’ for substance abuse,
etc.)
• The style and format of the synthetic notes
(articulate, using possessives, articles, pro-
nouns, auxiliary verbs, punctuation and con-
nectors consistently) differs substantially from
that of the real clinical data (telegraphic, with
frequent ellipsis of articles, pronouns, verbs
and connectors, deidentification placeholders,
missing spaces and punctuation, inconsistent
casing, etc.) which leads to lack of robust-
ness in the model predictions (i.e., predictions
changing when a pronoun is changed, period
is removed, etc.)
• In up to 30% of cases (from manually exam-
ining 100 spans), spans with negative labels
are in fact positive spans, which means 1) the
model is confused between negative and pos-
itive factors and fails to properly learn them
and 2) many ‘errors’ in the synthetic test set
are in fact correct predictions with incorrect
ground truth labels
To address these challenges, we thus perform the
following changes:
• We use heuristics to remove the bulk of
wrongly labelled spans (by removing most
spans for a given label which contain key-
words from other labels, leaving a few to avoid
overfitting)
• For each label, we upsample the ‘diverse’
spans (i.e., spans that do not mention label
words explicitly, e.g., spans that do include
‘family’ or ‘disorder’ for family disorder, or
‘sustance‘ and ‘abuse’ for substance abuse)
• We add ‘noise’ to the data by randomly re-
moving possessives, articles, pronouns, aux-
iliary verbs and punctuation and replacing
some pronouns with deidentification place-
holder strings (“FFFFF” and “XXXXX”) that
are used to pseudonymise our research EHR
data
• We switch to BERT-base-uncased to avoid cas-
ing issues
• We remove the older age category (which is
available as structured data in an EHR) and
merge childhood abuse and abuse classes into
a single abuse category (due to the scarcity of
the latter class)
• We remove the sentences with no labels from
the original dataset and specifically prompt
GPT3.5-turbo for 3000 clinical sentences
which do not mention our target features. This
is done both because the original unlabelled
sentences had a high amount of noise (the plan
would mention prognostic/risk factors or fea-
tures but was not annotated by the language
model) and to ensure more diversity in unla-
belled sentences.
The resulting dataset contains 55924 sentences.
We retrain our model on this new synthetic data and
obtain an average F1 of 0.75 on the synthetic test
set (keeping in mind that since a percentage of test
set examples are wrongly labelled, this does not
reflect the real performance of the model). We then
re-test the model on the annotated EHR sentences.
12.2.1
Results
The results on the clinical data can be seen in Table
4. The overall performance is 0.60 F1, with manual
perturbation analysis indicating that the model is
much more robust to changes in style or format
(e.g., removing pronouns or punctuation). The per-
formance varies widely across classes, with some
classes performing very well (0.95 F1 for recurrent
episodes POSITIVE) while others show poor per-
formance (0.19 F1 for non-adherence NEGATIVE).
Performance for negative classes is again unsurpris-
ingly worse than for positive classes. In general,
recall is higher than precision, with a tendency for
the model to overpredict factors. This is unsupris-
ing given the high overlap in topic and broad range


## Page 11


of our factors. Indeed, negative classes such as
negative multiple antidepressants (e.g., She takes
antidepressant X), negative anhedonia (e.g., She
enjoys hobbies like painting and reading or neg-
ative abuse e.g., She likes spending time with her
family might be virtually indistinguishable from
NO_ANNOTATION spans, and arguably most sen-
tences could be said to contain a span within our
target factors if we include negative classes. We
come back to this issue in the Discussion.
To remedy the model’s oversensitivity, we can
increase the confidence threshold for predicting
factors, that is only outputting factor predictions
above 0.5 probability and no label otherwise. This
also has the advantage that it ensures any output
predictions are robust (i.e., made with high con-
fidence rather than being ‘lucky guesses’), which
is particularly desirable in medical settings. Fi-
nally, it increases recall of the NO_ANNOTATION
class to 0.90. When this threshold is increased to
0.5, four high confidence classes emerge (abuse
POSITIVE, family member mental disorder POS-
ITIVE, severe illness POSITIVE and suicidality
POSITIVE) which can be confidently predicted
with 0.85 average F1 and 0.95 precision (see Table
5.)
A significant factor contributing to the model’s
lower performance is the model confusing posi-
tive and negative classes (partially due to noise
in the synthetic training data as mentioned previ-
ously). This is demonstrated by collapsing pre-
dictions across polarities, which increases average
F1 to 0.70 (see Table 6). Given the goal of the
model is to present clinicians with evidence from
extracted spans for their consideration, the non-
polarised model could also have clinical utility.
13
Example extractions
Here we show some examples of successful span
extractions in synthetic test sentences with (start,
end, label) for each extracted span:
• Treatment History: patient already tried mul-
tiple antidepressant medications from differ-
ent classes including SSRIs and SNRIs but
did not experience significant improvement.
spans:
(0, 46, multiple antidepressants
POSITIVE); (47, 74, improvement NEG-
ATIVE)
• XXXXX has been inpatient twice for men-
tal health treatment due to severity of illness
with recurrent episodes of major depressive
disorder occurring approximately every 3-4
months. spans: (0, 81, multiple hospital-
izations POSITIVE); (82, 175, recurrent
episodes POSITIVE
• FFFFF reports no family history of mental
disorders and denies any history of abuse
spans: (0, 51, family member mental dis-
order NEGATIVE); (52, 83, abuse NEGA-
TIVE)
• patient reports no significant physical comor-
bidities but mentions mild anxiety symptoms
spans: (0, 53, physical comorbidity NEGA-
TIVE); (54, 88, mental comorbidity POSI-
TIVE)
• has been on citalopram, fluoxetine and sertra-
line spans: (0, 57, multiple antidepressants
POSITIVE)
• patient recalls being severely bullied at school
spans: (0, 48, abuse POSITIVE)
• she battles with heroin addiction spans: (0,
33, substance abuse POSITIVE)
• he denies intent to end his own life spans: (0,
36, suicidality NEGATIVE)
• she did not suffer any neglect as a child spans:
(0, 41, abuse NEGATIVE)
• he talked about how his friend was bullied
spans: (0, 42, NO ANNOTATION)
• her brother was diagnosed with ptsd spans:
(0, 35, family member mental disorder
POSITIVE)
14
Discussion
In the synthetic test dataset, we find that our cus-
tom span-level model which uses a variant of Non-
Maximum Suppression (NMS) outperforms the
simpler token-level model which is standardly used
for span extraction. Additionally, we find that the
sentence-level model performs slightly under the
span-level model overall. We hypothesise that this
might be because the model learns to more specif-
ically map labels with the relevant tokens, rather
than relying on fuzzier learning over full sentences.
Performance on positive classes is significantly
higher than for negative classes. This is due to a


## Page 12


Sentence-level model
Span-level model
Token-level model
Class
Precision
Recall
F1 Score
Precision
Recall
F1 Score
Precision
Recall
F1 Score
older age POSITIVE
0.46
0.57
0.51
0.42
0.83
0.56
0.5
0.57
0.54
family member mental disorder POSITIVE
0.75
0.9
0.82
0.74
0.9
0.81
0.7
0.89
0.78
abuse POSITIVE
0.6
0.25
0.35
0.69
0.38
0.49
0.84
0.4
0.54
childhood abuse POSITIVE
0.77
0.87
0.81
0.73
0.89
0.8
0.78
0.85
0.81
long illness duration POSITIVE
0.72
0.76
0.74
0.79
0.64
0.7
0.7
0.69
0.69
severe illness POSITIVE
0.45
0.33
0.38
0.47
0.39
0.43
0.34
0.22
0.26
suicidality POSITIVE
0.61
0.64
0.63
0.69
0.61
0.65
0.48
0.63
0.55
multiple hospitalizations POSITIVE
0.8
0.84
0.82
0.76
0.88
0.81
0.66
0.75
0.7
recurrent episodes POSITIVE
0.63
0.62
0.63
0.65
0.73
0.69
0.55
0.65
0.59
improvement POSITIVE
0.58
0.64
0.61
0.55
0.57
0.56
0.47
0.58
0.52
physical comorbidity POSITIVE
0.72
0.76
0.74
0.64
0.83
0.73
0.72
0.8
0.76
mental comorbidity POSITIVE
0.81
0.75
0.78
0.78
0.72
0.74
0.81
0.72
0.76
substance abuse POSITIVE
0.74
0.64
0.68
0.71
0.83
0.77
0.67
0.78
0.72
anhedonia POSITIVE
0.58
0.67
0.62
0.62
0.8
0.7
0.59
0.7
0.64
illness early onset POSITIVE
0.65
0.63
0.64
0.67
0.75
0.7
0.61
0.55
0.58
multiple antidepressants POSITIVE
0.82
0.78
0.8
0.79
0.83
0.81
0.7
0.79
0.74
antidepressant dosage increase POSITIVE
0.73
0.86
0.79
0.82
0.78
0.8
0.68
0.65
0.66
multiple psychotherapies POSITIVE
0.64
0.75
0.69
0.73
0.72
0.72
0.66
0.8
0.72
side effects POSITIVE
0.81
0.71
0.76
0.74
0.74
0.74
0.67
0.68
0.68
non adherence POSITIVE
0.75
0.66
0.7
0.76
0.77
0.76
0.68
0.68
0.68
older age NEGATIVE
0.44
0.55
0.49
0.58
0.41
0.48
0.49
0.39
0.43
family member mental disorder NEGATIVE
0.71
0.62
0.66
0.72
0.71
0.72
0.62
0.5
0.55
abuse NEGATIVE
0.54
0.76
0.63
0.6
0.8
0.69
0.55
0.7
0.62
childhood abuse NEGATIVE
0.73
0.74
0.74
0.64
0.69
0.66
0.53
0.49
0.51
long illness duration NEGATIVE
0.49
0.4
0.44
0.58
0.43
0.5
0.42
0.35
0.38
severe illness NEGATIVE
0.37
0.31
0.34
0.62
0.41
0.49
0.31
0.41
0.35
suicidality NEGATIVE
0.68
0.85
0.75
0.61
0.77
0.68
0.64
0.71
0.67
multiple hospitalizations NEGATIVE
0.76
0.83
0.8
0.77
0.79
0.78
0.72
0.68
0.7
recurrent episodes NEGATIVE
0.75
0.48
0.59
0.76
0.49
0.6
0.58
0.39
0.46
improvement NEGATIVE
0.42
0.42
0.42
0.35
0.49
0.4
0.34
0.26
0.29
physical comorbidity NEGATIVE
0.66
0.71
0.68
0.67
0.68
0.68
0.59
0.61
0.6
mental comorbidity NEGATIVE
0.65
0.68
0.67
0.72
0.65
0.68
0.5
0.56
0.53
substance abuse NEGATIVE
0.7
0.91
0.79
0.69
0.89
0.78
0.62
0.75
0.68
anhedonia NEGATIVE
0.55
0.3
0.39
0.61
0.34
0.44
0.56
0.3
0.39
illness early onset NEGATIVE
0.7
0.57
0.63
0.75
0.53
0.62
0.53
0.5
0.51
multiple antidepressants NEGATIVE
0.32
0.2
0.25
0.59
0.37
0.45
0.37
0.3
0.33
antidepressant dosage increase NEGATIVE
0.56
0.57
0.56
0.54
0.59
0.56
0.53
0.41
0.46
multiple psychotherapies NEGATIVE
0.58
0.52
0.55
0.63
0.37
0.47
0.47
0.2
0.28
side effects NEGATIVE
0.58
0.67
0.62
0.58
0.64
0.61
0.56
0.37
0.44
non adherence NEGATIVE
0.39
0.43
0.41
0.37
0.44
0.4
0.33
0.42
0.37
NO ANNOTATION
0.81
0.79
0.8
0.84
0.77
0.8
0.8
0.81
0.81
POSITIVE
0.68
0.68
0.68
0.69
0.73
0.70
0.64
0.67
0.64
NEGATIVE
0.59
0.59
0.58
0.63
0.58
0.59
0.53
0.49
0.50
PATIENT
0.63
0.66
0.63
0.64
0.70
0.65
0.63
0.59
0.59
ILLNESS
0.64
0.63
0.63
0.66
0.64
0.64
0.57
0.59
0.57
TREATMENT
0.62
0.62
0.61
0.65
0.62
0.63
0.58
0.52
0.54
All
0.63
0.63
0.63
0.66
0.65
0.65
0.58
0.57
0.57
Table 3: Precision, recall and macro averaged F1 for each model and factor (synthetic data). best in bold


## Page 13


Class
Precision
Recall
F1 Score
N
NO ANNOTATION
0.59
0.34
0.43
99
anhedonia POSITIVE
0.76
0.59
0.67
27
antidepressant dosage increase POSITIVE
0.31
0.83
0.45
12
abuse POSITIVE
0.94
0.80
0.86
20
family member mental disorder POSITIVE
0.61
0.92
0.73
12
illness early onset POSITIVE
0.50
1.00
0.67
8
improvement POSITIVE
0.68
0.42
0.52
31
long illness duration POSITIVE
1.00
0.80
0.89
5
mental comorbidity POSITIVE
0.43
0.38
0.40
8
physical comorbidity POSITIVE
0.50
0.67
0.57
9
multiple antidepressants POSITIVE
0.75
0.62
0.68
29
multiple psychotherapies POSITIVE
0.38
0.38
0.38
13
non adherence POSITIVE
0.50
0.19
0.27
16
recurrent episodes POSITIVE
1.00
0.90
0.95
10
severe illness POSITIVE
0.55
1.00
0.71
6
side effects POSITIVE
0.79
0.44
0.57
34
substance abuse POSITIVE
0.71
0.62
0.67
13
suicidality POSITIVE
0.80
0.75
0.77
32
antidepressant dosage increase NEGATIVE
0.50
0.56
0.53
16
improvement NEGATIVE
0.60
0.16
0.25
19
multiple antidepressants NEGATIVE
0.20
1.00
0.33
3
multiple psychotherapies NEGATIVE
0.51
0.93
0.66
28
multiple hospitalizations NEGATIVE
0.75
1.00
0.86
3
non adherence NEGATIVE
0.12
0.40
0.19
5
severe illness NEGATIVE
0.64
1.00
0.78
7
side effects NEGATIVE
0.65
0.68
0.67
19
substance abuse NEGATIVE
0.33
0.33
0.33
3
suicidality NEGATIVE
0.78
0.78
0.78
9
POSITIVE
0.66
0.67
0.63
285
NEGATIVE
0.51
0.68
0.54
98
All
0.60
0.66
0.60
482
Table 4: Precision, recall and macro averaged F1 for each factor (clinical data). Classes with n <2 excluded.
Class
Precision
Recall
F1 Score
abuse POSITIVE
1.00
0.80
0.89
family member mental disorder POSITIVE
0.85
0.92
0.88
severe illness POSITIVE
1.00
0.67
0.80
suicidality POSITIVE
0.96
0.75
0.84
All
0.95
0.78
0.85
Table 5: Precision, recall and macro averaged F1 for each factor (clinical data -high confidence classes with 0.5
confidence threshold).


## Page 14


Class
Precision
Recall
F1 Score
NO ANNOTATION
0.59
0.34
0.43
anhedonia
0.75
0.86
0.80
antidepressant dosage increase
0.48
0.86
0.62
abuse
0.95
0.90
0.93
family member mental disorder
0.61
0.92
0.73
illness early onset
0.33
1.00
0.50
improvement
0.88
0.42
0.57
long illness duration
0.67
0.57
0.62
mental comorbidity
0.38
0.38
0.38
physical comorbidity
0.50
0.80
0.62
multiple antidepressants
0.79
0.97
0.87
multiple psychotherapies
0.64
1.00
0.78
multiple hospitalisations
0.75
0.75
0.75
non adherence
0.55
0.57
0.56
recurrent episodes
0.92
1.00
0.96
severe illness
0.59
1.00
0.74
side effects
0.87
0.64
0.74
substance abuse
0.88
0.79
0.83
suicidality
0.87
0.83
0.85
All
0.68
0.77
0.70
Table 6: Precision, recall and macro averaged F1 for each factor (clinical data -non-polarised).
number of reasons. First, despite our additional
prompting for negative factors exclusively, there
is still an imbalance with more positive than neg-
ative labels. Second, it is a well-known fact that
language models struggle with negation (Ettinger,
2020). Finally, negation will often be present in
the sentence but not necessarily in each negated
span, even if the scope of the negation encompasses
the span, e.g., The patient denies suicidality [sui-
cidality NEGATIVE] and substance abuse [sub-
stance abuse NEGATIVE], where the text of the
second span does not contain an explicit negation.
While each span’s tokens contextual embeddings
should have some signal which indicates there is a
negation somewhere in the sentence, it might not
be strong enough compared to classifying a span
which contains an explicit negation token.
While average F1 on real data is 0.60, our model
trained exclusively on synthetic data already has
practical clinical use, as it can be used out of the
box with a confidence threshold of 0.5 to extract
abuse, family disorder, severe illness and suicidal-
ity with 0.85 F1 and 0.95 precision, a performance
comparable to Kulkarni et al. (2024), who used
real data annotated manually in a costly and time-
consuming way to train a model to extract two
clinical factors (suicidality and anhedonia). This is
despite the high syntactic and semantic variability
among spans expressing these factors. For exam-
ple, our model is able to identify spans mentioning
events as varied as emotional neglect, violence or
bullying as abuse, and a wide range of combination
of family member and various conditions (brother,
aunt, schizophrenia, bipolar disorder, etc.) as a fam-
ily history of mental disorder. Obtaining such high
performance with a model trained on synthetic data
only shows this is a promising direction of research
for cost-efficient AI applications in healthcare. In-
deed, the cost of producing the synthetic training
data used in this study was under £10, versus the
thousands of pounds required for compensating
expert annotators.
We believe there are several reasons the model
fails to achieve higher average performance across
all factors. First, many classes are very close to one
another, for example long duration and early onset,
classes which mention antidepressants, physical
comorbidities and side effects, etc. It is no coin-
cidence that the model performs best on classes
which are most distinctive (abuse, family disorder,
suicidality). Secondly, many classes are highly sub-
jective, e.g., early onset (how early?), long duration
(how long?), substance abuse (how much consump-
tion?) and spans are often ambivalent (e.g., ‘some
improvement then worsening’; ‘some side effects
then none’, etc.) Finally, many negative classes are
not well defined or consistent, e.g, negative multi-
ple psychotherapies (mentions only one therapy?
any span mentioning therapy?), negative multiple
antidepressants (any span mentioning a single an-
tidepressant?), negative multiple hospitalisations?
(having been hospitalised once? Never?), negative
anhedonia (any span mentioning subject perform-
ing activities?), negative severe illness (moderate


## Page 15


illness? mild symptoms?), etc. In view of these
challenges, it is likely that training a model to ex-
tract a wide range of factors requires some real
annotated clinical data, however impressively high
performance can already be achieved on a subset
of factors by exclusively training on synthetic data.
15
Future work
The paradigm we used could be extended and
scaled to other phenotypes with a different set
of risk/prognostic factors or clinical features in
the future. Future research could also investigate
whether using a model which has been domain
pretrained on mental health data (such as Men-
talBERT, (Ji et al., 2021) would improve perfor-
mance. Works such as (Guevara et al., 2024) sug-
gest that a sequence-to-sequence model such as
T5 could achieve even better performance than a
BERT-based classifier model. Using GPT4 instead
of GPT3.5 could help generate synthetic data with
reduced noise and more accurate labelling of nega-
tive factors. Finally, an optimal weighting scheme
for the extracted factors which would best allow
identification of difficult-to-treat depression could
be developed in consultation with clinicians.
16
Conclusion
The goal of this study was to train a model to ex-
tract spans which contain factors associated with
the syndrome of difficult-to-treat depression. To
achieve this, we generated annotated synthetic clin-
ical notes with both positive and negative factors of
interest using a Large Language Model (GPT3.5-
turbo) and subsequently trained various BERT-
based classifier models (sentence, token and span
level) to extract factors. We show it is possible
to obtain good performance on real clinical data
on a set of as many of 20 different factors, and
high performance on a subset of clinically-relevant
factors by training exclusively on LLM-generated
synthetic data.
17
Acknowledgements
I.L., A.K. and D.W.J. were supported in part by
the NIHR AI Award for Health and Social Care
(AI-AWARD02183), A.K. by a research grant from
GlaxoSmithKline. The views expressed are those
of the authors and not necessarily those of the UK
National Health Service, the NIHR or the UK De-
partment of Health. This study was supported by
CRIS Powered by Akrivia Health, using data, sys-
tems and support from the NIHR Oxford Health
Biomedical Research Centre (BRC-1215-20005)
Research Informatics Team. We would also like
to acknowledge the work and support of the Ox-
ford Research Informatics Team: Tanya Smith, Re-
search Informatics Manager, Adam Pill, Suzanne
Fisher, Research Informatics Systems Analysts and
Lulu Kane Research Informatics Administrator.


## Page 16


References
Monica Agrawal, Stefan Hegselmann, Hunter Lang,
Yoon Kim, and David Sontag. 2022. Large language
models are few-shot clinical information extractors.
In Proceedings of the 2022 Conference on Empiri-
cal Methods in Natural Language Processing, pages
1998–2022.
Carlos Rejón Altable. 2012. Logic structure of clinical
judgment and its relation to medical and psychiatric
semiology. Psychopathology, 45(6):344–351.
DSMTF American Psychiatric Association, Ameri-
can Psychiatric Association, et al. 2013. Diagnostic
and statistical manual of mental disorders: DSM-5,
volume 5. American psychiatric association Wash-
ington, DC.
Samy Ateia and Udo Kruschwitz. 2023. Is chatgpt a
biomedical expert?–exploring the zero-shot perfor-
mance of current gpt models in biomedical tasks.
arXiv preprint arXiv:2306.16108.
Sage Brown, Katherine Rittenbach, Sarah Cheung, Gail
McKean, Frank P MacMaster, and Fiona Clement.
2019. Current and common definitions of treatment-
resistant depression: findings from a systematic re-
view and qualitative interviews. The Canadian Jour-
nal of Psychiatry, 64(6):380–387.
Tom Brown, Benjamin Mann, Nick Ryder, Melanie
Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind
Neelakantan, Pranav Shyam, Girish Sastry, Amanda
Askell, et al. 2020. Language models are few-shot
learners. Advances in neural information processing
systems, 33:1877–1901.
Alice Caldiroli, Enrico Capuzzi, Ilaria Tagliabue, Mar-
tina Capellazzi, Matteo Marcatili, Francesco Mucci,
Fabrizia Colmegna, Massimo Clerici, Massimiliano
Buoli, and Antonios Dakanalis. 2021. Augmenta-
tive pharmacological strategies in treatment-resistant
major depression: a comprehensive review. Interna-
tional Journal of Molecular Sciences, 22(23):13070.
Tiago Costa, Bayar Menzat, Tomas Engelthaler, Ben-
jamin Fell, Tarso Franarin, Gloria Roque, Yiran Wei,
Xinyue Zhang, and R Hamish McAllister-Williams.
2022. The burden associated with, and management
of, difficult-to-treat depression in patients under spe-
cialist psychiatric care in the united kingdom. Jour-
nal of Psychopharmacology, 36(5):545–556.
Igor Douven. 2021. Abduction. In Edward N. Zalta, ed-
itor, The Stanford Encyclopedia of Philosophy, Sum-
mer 2021 edition. Metaphysics Research Lab, Stan-
ford University.
Allyson Ettinger. 2020. What bert is not: Lessons from
a new suite of psycholinguistic diagnostics for lan-
guage models.
Marco
Guevara,
Shan
Chen,
Spencer
Thomas,
Tafadzwa L. Chaunzwa, Idalid Franco, Benjamin H.
Kann, Shalini Moningi, Jack M. Qian, Madeleine
Goldstein, Susan Harper, Hugo J. W. L. Aerts, Paul J.
Catalano, Guergana K. Savova, Raymond H. Mak,
and Danielle S. Bitterman. 2024. Large language
models to identify social determinants of health in
electronic health records.
npj Digital Medicine,
7(1):6.
Minghao Hu, Yuxing Peng, Zhen Huang, and Dong-
sheng Li. 2019. A multi-type multi-span network for
reading comprehension that requires discrete reason-
ing. CoRR, abs/1908.05514.
Yan Hu, Iqra Ameer, Xu Zuo, Xueqing Peng, Yujia
Zhou, Zehan Li, Yiming Li, Jianfu Li, Xiaoqian Jiang,
and Hua Xu. 2023. Zero-shot clinical entity recogni-
tion using chatgpt. arXiv preprint arXiv:2303.16416.
Shaoxiong Ji, Tianlin Zhang, Luna Ansari, Jie Fu,
Prayag Tiwari, and Erik Cambria. 2021. Mental-
bert: Publicly available pretrained language models
for mental healthcare. CoRR, abs/2110.15621.
Alexander Kautzky, Markus Dold, Lucie Bartova, Marie
Spies, Georg S Kranz, Daniel Souery, Stuart Mont-
gomery, Julien Mendlewicz, Joseph Zohar, Chiara
Fabbri, et al. 2019. Clinical factors predicting treat-
ment resistant depression: affirmative results from
the european multicenter study. Acta Psychiatrica
Scandinavica, 139(1):78–88.
Alexander Kautzky, Markus Dold, Lucie Bartova, Marie
Spies, Thomas Vanicek, Daniel Souery, Stuart Mont-
gomery, Julien Mendlewicz, Joseph Zohar, Chiara
Fabbri, et al. 2017. Refining prediction in treatment-
resistant depression: results of machine learning anal-
yses in the trd iii sample. The Journal of clinical
psychiatry, 79(1):14989.
Andrey Kormilitzin, Nemanja Vaci, Qiang Liu, and
Alejo Nevado-Holgado. 2021. Med7: A transfer-
able clinical natural language processing model for
electronic health records. Artificial Intelligence in
Medicine, 118:102086.
Deepali Kulkarni, Abhijit Ghosh, Amey Girdhari,
Shaomin Liu, L Alexander Vance, Melissa Unruh,
and Joydeep Sarkar. 2024. Enhancing pre-trained
contextual embeddings with triplet loss as an effec-
tive fine-tuning method for extracting clinical fea-
tures from electronic health record derived mental
health clinical notes. Natural Language Processing
Journal, 6:100045.
Sunjun Kweon, Junu Kim, Jiyoun Kim, Sujeong Im,
Eunbyeol Cho, Seongsu Bae, Jungwoo Oh, Gyubok
Lee, Jong Hak Moon, Seng Chan You, et al. 2023.
Publicly shareable clinical large language model
built on synthetic clinical notes.
arXiv preprint
arXiv:2309.00237.
Isaac Lage, Thomas H McCoy Jr, Roy H Perlis, and
Finale Doshi-Velez. 2022. Efficiently identifying in-
dividuals at high risk for treatment resistance in major
depressive disorder using electronic health records.
Journal of Affective Disorders, 306:254–259.


## Page 17


Aziliz Le Glaz, Yannis Haralambous, Deok-Hee Kim-
Dufor, Philippe Lenca, Romain Billot, Taylor C Ryan,
Jonathan Marsh, Jordan Devylder, Michel Walter,
Sofian Berrouiguet, et al. 2021. Machine learning
and natural language processing in mental health:
systematic review. Journal of Medical Internet Re-
search, 23(5):e15708.
Qiang Liu, Nemanja Vaci, Ivan Koychev, Andrey Ko-
rmilitzin, Zhenpeng Li, Andrea Cipriani, and Alejo
Nevado-Holgado. 2022. Personalised treatment for
cognitive impairment in dementia: development and
validation of an artificial intelligence model. BMC
medicine, 20(1):1–12.
Z Liu, X Yu, L Zhang, Z Wu, C Cao, H Dai, L Zhao,
W Liu, D Shen, Q Li, et al. 2023. Deid-gpt: zero-shot
medical text de-identification by gpt-4. arxiv. arXiv.
RH McAllister-Williams, C Arango, P Blier, K Demyt-
tenaere, P Falkai, P Gorwood, M Hopwood, A Javed,
S Kasper, GS Malhi, et al. 2020. The identification,
assessment and management of difficult-to-treat de-
pression: an international consensus statement. Jour-
nal of Affective Disorders, 267:264–282.
Zhi Nie, Srinivasan Vairavan, Vaibhav A Narayan,
Jieping Ye, and Qingqin S Li. 2018. Predictive mod-
eling of treatment resistant depression using data
from star* d and an independent clinical study. PloS
one, 13(6):e0197268.
George I Papakostas, Timothy Petersen, Joel Pava, Ella
Masson, JOHN J WORTHINGTON III, Jonathan E
Alpert, Maurizio Fava, and Andrew A Nierenberg.
2003. Hopelessness and suicidal ideation in outpa-
tients with treatment-resistant depression: prevalence
and impact on treatment outcome. The Journal of
nervous and mental disease, 191(7):444–449.
RH Perlis, DV Iosifescu, VM Castro, SN Murphy,
VS Gainer, Jessica Minnier, T Cai, S Goryachev,
Q Zeng, PJ Gallagher, et al. 2012. Using electronic
medical records to enable large-scale studies in psy-
chiatry: treatment resistant depression as a model.
Psychological medicine, 42(1):41–50.
Roy H Perlis. 2013. A clinical risk stratification tool for
predicting treatment resistance in major depressive
disorder. Biological psychiatry, 74(1):7–14.
Claudio Rapezzi, Roberto Ferrari, and Angelo Branzi.
2005. White coats and fingerprints: diagnostic rea-
soning in medicine and investigative methods of fic-
tional detectives. Bmj, 331(7531):1491–1494.
James A Reggia, Barry T Perricone, Dana S Nau, and
Yun Peng. 1985. Answer justification in diagnos-
tic expert systems-part i: Abductive inference and
its justification. IEEE transactions on biomedical
engineering, (4):263–267.
A John Rush, Madhukar H Trivedi, Stephen R Wis-
niewski, Andrew A Nierenberg, Jonathan W Stew-
art, Diane Warden, George Niederehe, Michael E
Thase, Philip W Lavori, Barry D Lebowitz, et al.
2006. Acute and longer-term outcomes in depressed
outpatients requiring one or several treatment steps:
a star* d report. American Journal of Psychiatry,
163(11):1905–1917.
Damian F Santomauro, Ana M Mantilla Herrera,
Jamileh Shadid, Peng Zheng, Charlie Ashbaugh,
David M Pigott, Cristiana Abbafati, Christopher
Adolph, Joanne O Amlag, Aleksandr Y Aravkin, et al.
2021. Global prevalence and burden of depressive
and anxiety disorders in 204 countries and territories
in 2020 due to the covid-19 pandemic. The Lancet,
398(10312):1700–1712.
Morwenna Senior, Matthias Burghart, Rongqin Yu, An-
drey Kormilitzin, Qiang Liu, Nemanja Vaci, Alejo
Nevado-Holgado, Smita Pandit, Jakov Zlodre, and
Seena Fazel. 2020.
Identifying predictors of sui-
cide in severe mental illness: A feasibility study of
a clinical prediction rule (ox ford m ental i llness
and s uicide tool or oxmis). Frontiers in psychiatry,
11:268.
Yi-han Sheu,
Colin Magdamo,
Matthew Miller,
Sudeshna Das, Deborah Blacker, and Jordan W
Smoller. 2023. Ai-assisted prediction of differential
response to antidepressant classes using electronic
health records. NPJ Digital Medicine, 6(1):73.
Liyan Tang, Zhaoyi Sun, Betina Idnay, Jordan G Nestor,
Ali Soroush, Pierre A Elias, Ziyang Xu, Ying Ding,
Greg Durrett, Justin Rousseau, et al. 2023a. Eval-
uating large language models on medical evidence
summarization. medrxiv.
Ruixiang Tang, Xiaotian Han, Xiaoqian Jiang, and Xia
Hu. 2023b. Does synthetic data generation of llms
help clinical text mining?
Niall Taylor, Yi Zhang, Dan W Joyce, Ziming Gao, An-
drey Kormilitzin, and Alejo Nevado-Holgado. 2023.
Clinical prompt learning with frozen language mod-
els. IEEE Transactions on Neural Networks and
Learning Systems.
Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier
Martinet, Marie-Anne Lachaux, Timothée Lacroix,
Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal
Azhar, Aurelien Rodriguez, Armand Joulin, Edouard
Grave, and Guillaume Lample. 2023. Llama: Open
and efficient foundation language models.
Nemanja Vaci, Ivan Koychev, Chi-Hun Kim, Andrey
Kormilitzin, Qiang Liu, Christopher Lucas, Azad De-
hghan, Goran Nenadic, and Alejo Nevado-Holgado.
2021. Real-world effectiveness, its predictors and on-
set of action of cholinesterase inhibitors and meman-
tine in dementia: retrospective health record study.
The British Journal of Psychiatry, 218(5):261–267.
Nemanja Vaci, Qiang Liu, Andrey Kormilitzin, Franco
De Crescenzo, Ayse Kurtulmus, Jade Harvey, Bessie
O’Dell, Simeon Innocent, Anneka Tomlinson, An-
drea Cipriani, et al. 2020. Statistics: Natural lan-
guage processing for structuring clinical text data


## Page 18


on depression using uk-cris. Evidence-based mental
health, 23(1):21.
Thomas Wolf, Lysandre Debut, Victor Sanh, Julien
Chaumond, Clement Delangue, Anthony Moi, Pier-
ric Cistac, Tim Rault, Rémi Louf, Morgan Funtowicz,
and Jamie Brew. 2019. Huggingface’s transformers:
State-of-the-art natural language processing. CoRR,
abs/1910.03771.
Yuqi Wu, Jie Chen, Kaining Mao, and Yanbo Zhang.
2023. Automatic post-traumatic stress disorder diag-
nosis via clinical transcripts: A novel text augmen-
tation with large language models. In 2023 IEEE
Biomedical Circuits and Systems Conference (Bio-
CAS), pages 1–5. IEEE.
Kailai Yang, Tianlin Zhang, Ziyan Kuang, Qianqian Xie,
Sophia Ananiadou, and Jimin Huang. 2023. Mental-
lama: Interpretable mental health analysis on social
media with large language models.


## Page 19


A
Appendix A
Patient presentation: The patient is a 45-year old female [PATIENT_FACTOR(POSITIVE):older_age] who
presents with a history of mental illness in her family, with her sister suffering from bipolar disorder
[PATIENT_FACTOR(POSITIVE):family_member_mental_disorder]. She reports a childhood marked by
abuse, specifically physical abuse from her father [PATIENT_FACTOR(POSITIVE):childhood_abuse]. The
patient further elaborates that she experienced emotional neglect from her mother for several years [PA-
TIENT_FACTOR(POSITIVE):childhood_abuse].
Illness history:
The patient’s psychiatric illness began at the age of 18 with the onset of major de-
pressive episodes.
Over the past 27 years [ILLNESS_FACTOR(POSITIVE):long_illness_duration], she
has experienced multiple episodes of severe depression, including thoughts of ending her life [ILL-
NESS_FACTOR(POSITIVE):suicidality]. Despite the severity of her illness, she has never been hospitalized
[ILLNESS_FACTOR(NEGATIVE):multiple_hospitalizations]. The patient has a history of recurrent depressive
episodes [ILLNESS_FACTOR(POSITIVE):recurrent_episodes].
Treatment
history:
The
patient’s
treatment
history
has
involved
a
variety
of
interven-
tions.
She has been prescribed multiple antidepressant medications over the years [TREAT-
MENT_FACTOR(POSITIVE):multiple_antidepressants]
at
varying
dosages,
including
increases
in
dose [TREATMENT_FACTOR(POSITIVE):antidepressant_dosage_increase]. However, she has experienced
side effects such as weight gain, sedation, and sexual dysfunction, prompting changes in medication
regimens [TREATMENT_FACTOR(POSITIVE):side_effects]. The patient has also been engaged in multiple
psychotherapies [TREATMENT_FACTOR(POSITIVE):multiple_psychotherapies].
Current presentation: During today’s session, the patient reports some improvement in her symptoms. She
notes a decrease in depressive symptoms such as sadness and hopelessness. However, she still experiences
anhedonia [ILLNESS_FACTOR(POSITIVE):anhedonia] and struggles with maintaining positive relationships.
There is evidence of physical comorbidity as the patient shares that she was recently diagnosed with diabetes
[ILLNESS_FACTOR(POSITIVE):physical_comorbidity]. Additionally, she has a comorbid diagnosis of gener-
alized anxiety disorder [ILLNESS_FACTOR(POSITIVE):mental_comorbidity]. The patient denies any current
substance abuse [ILLNESS_FACTOR(NEGATIVE):substance_abuse].
Discussion and plan:
The patient’s depressive symptoms seem to have an early onset [ILL-
NESS_FACTOR(POSITIVE):illness_early_onset], starting at 18 years old. Her history of multiple episodes of
depression, suicidal ideation, and non-adherence to medication regimens suggest a severe and chronic illness
course [ILLNESS_FACTOR(POSITIVE):severe_illness, ILLNESS_FACTOR(POSITIVE):recurrent_episodes,
ILLNESS_FACTOR(POSITIVE):non_adherence]. We will continue to monitor her progress and consider
further adjustments to her medication regimen based on her response and any side effects. Therapy sessions will
focus on enhancing coping skills, reducing anhedonia, and improving interpersonal relationships. We will also
explore strategies to address the impact of childhood abuse on her current mental health. Emergency contact
information will be reviewed, emphasizing the importance of seeking help during times of intense distress
or suicidal thoughts. Follow-up appointments will be scheduled to assess treatment response and assess any
additional needs.
Table 7: Example synthetic annotated note
B
Appendix B


## Page 20


""" Create a narrative psychiatric clinical note (about 500 words) and annotate sentences with
PATIENT-RELATED factors (older age, family member mental disorder, abuse, childhood abuse), ILLNESS-
RELATED factors (long illness duration, severe illness, suicidality, multiple hospitalizations, recurrent episodes,
improvement, physical comorbidity, mental comorbidity, substance abuse, anhedonia, illness early onset) and
TREATMENT-RELATED factors (multiple antidepressants, antidepressant dosage increase, multiple psychothera-
pies, side effects, non adherence).
Make sure to annotate all relevant text for each factor. The annotation must indicate if the evidence is POSITIVE
(presence of factor) or NEGATIVE (absence of factor) in the exact same format as the following examples:
"The patient is a 32-year old male [PATIENT_FACTOR(NEGATIVE):older_age]." "The patient reports
a history of mental illness in her family, with her brother suffering from generalised anxiety [PA-
TIENT_FACTOR(POSITIVE):family_member_mental_disorder] and that she visits him regularly.";
"She experienced childhood abuse, suffering emotional neglect from her mother for several years [PA-
TIENT_FACTOR(POSITIVE):childhood_abuse].";
Annotate each factor separately within each sentence after the relevant text, e.g.:
"The dosage was gradually increased [TREATMENT_FACTOR(POSITIVE):antidepressant_dosage_increase] until
severe gastrointestinal distress emerged [TREATMENT_FACTOR(POSITIVE):side_effects] leading to a review of
current approach."
"She experienced multiple periods of depression [ILLNESS_FACTOR(POSITIVE):recurrent_episodes] but was
never hospitalized [ILLNESS_FACTOR(NEGATIVE):multiple_hospitalizations] as she opposed it repeatedly.";
"He was treated with various antidepressants [ILLNESS_FACTOR(POSITIVE):multiple_antidepressants] and
experienced relapses upon discontinuation [ILLNESS_FACTOR(POSITIVE):non_adherence] which was due to a
general distrust in medications."
Do not annotate the plan. """
Table 8: ChatGPT prompt
C
Appendix C


## Page 21


""" Create a narrative psychiatric clinical note (about 500 words) and annotate sentences with negative examples of
the following factors:
PATIENT-RELATED factors (older age, family member mental disorder, abuse, childhood abuse), ILLNESS-
RELATED factors (long illness duration, severe illness, suicidality, multiple hospitalizations, recurrent episodes,
improvement, physical comorbidity, mental comorbidity, substance abuse, anhedonia, illness early onset) and
TREATMENT-RELATED factors (multiple antidepressants, antidepressant dosage increase, multiple psychothera-
pies, side effects, non adherence).
Make sure to annotate all relevant text for each factor. The annotation must indicate that the evidence is NEGATIVE
(absence of factor) in the exact same format as the following examples:
"The patient is a 32-year old male [PATIENT_FACTOR(NEGATIVE):older_age]."
"She was never hospitalized [ILLNESS_FACTOR(NEGATIVE):multiple_hospitalizations] as she opposed it
repeatedly.";
Do not annotate the plan. """
Table 9: ChatGPT negative prompt
D
Appendix D


## Page 22


Figure 3: Average explicit mentions of all label words.


## Page 23


Figure 4: Average Jaccard similarities of span pairs.
## Related

- [[11_KNOWLEDGE/_arxiv_md/2024/2024-11/2411.07645v1_Desingularization_of_vortices_for_the_incompressible_Euler_equation_on_a_sphere.md|2411.07645v1_Desingularization_of_vortices_for_the_incompressible_Euler_equation_on_a_sphere]]
- [[13_MODELS/MODELS_README.md|README]]
- [[13_MODELS/MODELS_MODEL_CONTRACT.md|13 Models Contract]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: 2402_07645v1_detecting_the_clinical_features_of_difficult_to_treat_depression_using_synthetic_data_f
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2024/2024-02/2402_07645V1_DETECTING_THE_CLINICAL_FEATURES_OF_DIFFICULT_TO_TREAT_DEPRESSION_USING_SYNTHETIC_DATA_FROM_LARGE_LANGUAGE_MODELS.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1910.06792v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1910.06792v1_Early_Prediction_of_Sepsis_From_Clinical_Datavia_Heterogeneous_Event_Aggregation

> Source: 1910.06792v1_Early_Prediction_of_Sepsis_From_Clinical_Datavia_Heterogeneous_Event_Aggregation.pdf

> Pages: 4

---


## Page 1


Early Prediction of Sepsis From Clinical Data
via Heterogeneous Event Aggregation
Luchen Liu∗, Haoxian Wu∗, Zichang Wang, Zequn Liu, Ming Zhang
Department of Computer Science, Peking University, Beijing, China
Abstract
Sepsis is a life-threatening condition that seriously en-
dangers millions of people over the world. Hopefully, with
the widespread availability of electronic health records
(EHR), predictive models that can effectively deal with
clinical sequential data increase the possibility to predict
sepsis and take early preventive treatment. However, the
early prediction is challenging because patients’ sequen-
tial data in EHR contains temporal interactions of multi-
ple clinical events. And capturing temporal interactions
in the long event sequence is hard for traditional LSTM.
Rather than directly applying the LSTM model to the event
sequences, our proposed model ﬁrstly aggregates hetero-
geneous clinical events in a short period and then captures
temporal interactions of the aggregated representations
with LSTM. Our proposed Heterogeneous Event Aggrega-
tion can not only shorten the length of clinical event se-
quence but also help to retain temporal interactions of both
categorical and numerical features of clinical events in the
multiple heads of the aggregation representations. In the
PhysioNet/Computing in Cardiology Challenge 2019 [1],
with the team named PKU_DLIB, our proposed model, in
high efﬁciency, achieved utility score (0.321) in the full test
set .
1.
Introduction
Sepsis is a life-threatening condition that arises when
the body’s response to infection causes injury to its tissues
and organs. And the early prediction of the sepsis onset is
important for physicians to take early preventive treatment.
However, sepsis prediction is a difﬁcult task, because there
are complex sepsis risk factors including the age of pa-
tient, immune system weakness, complication (e.g. can-
cer, diabetes), conditions (e.g. trauma, burns) and so on.
Hopefully, with the help of the widespread availability of
electronic health records (EHR), well-designed predictive
models, which can effectively make use of clinical sequen-
tial data, will be able to increase the sepsis prediction per-
* The two authors have equal contribution to this work.
formance.
The early sepsis prediction is challenging because pa-
tients’ sequential data in EHR contains temporal interac-
tions of multiple clinical events [2,3]. The interactions of
multiple clinical events include event co-occurrence in a
short period (e.g. two related symptoms occur together)
and event temporal dependency at large time-scale (e.g.
A vital signal abnormally arises several hours after cer-
tain drug injection). One possible solution is directly ap-
plying deep sequential models, such as LSTM [4], Trans-
former[5], on the clinical event sequence. However, cap-
turing temporal interactions in the long event sequence is
hard for traditional LSTM because the length of clinical
sequences exceeds the modeling ability of LSTM.
Rather than directly applying the LSTM model to the
event sequences, some works design hierarchical neural
networks to model the long sequence[6]. For example, ag-
gregating events in a short period into a vector helps to
shorten the original long sequence[7]. However, the infor-
mation of each kind of clinical events is mixed in the ag-
gregation vector, so temporal interactions of these events
are hard to capture.
To address these issues, our proposed model ﬁrstly ag-
gregates heterogeneous clinical events in a short period and
then captures temporal interactions of the aggregated rep-
resentations with LSTM. The Heterogeneous Event Ag-
gregation module can not only shorten the length of clini-
cal event sequence but also help to retain temporal interac-
tions of both categorical and numerical features of clinical
events in the multiple heads of the aggregation representa-
tions. The separated clinical information in different heads
makes it easier to capture event temporal interactions in
different aggregation vectors. Experiments on the Phys-
ioNet/Computing in Cardiology Challenge 2019 show that
our proposed model is effective and efﬁcient compared to
traditional methods. The contributions of this work is sum-
marised as following:
• We propose a model to capture temporal interactions
among multiple types of clinical event streams from EHR
data for early sepsis prediction.
• The proposed heterogeneous event aggregation module
can reduce the length of long clinical event sequences and
arXiv:1910.06792v1  [cs.LG]  14 Oct 2019


## Page 2


retain their temporal interactions.
• Our proposed model achieves good prediction perfor-
mance and time efﬁciency.
2.
Dataset and Preprocessing
2.1.
Dataset
The EHR data provided publicly for this challenge is
sourced from two separate ICU, containing 20000 and
20643 records respectively. Each record is made up of
hourly clinical data for a speciﬁc patient. Each row rep-
resents a single hour’s data with 40 variables and an ad-
ditional label indicating whether the patient will get sep-
sis within 6 hours. With a positive sample proportion of
7.21%, there are 2932 sepsis patients in total. Sepsis and
normal patients are divided into train and test set at the
same ratio respectively. 5-fold cross validation is estab-
lished over the train set.
2.2.
Data Preprocessing
In this competition, our goal is to make an early sep-
sis detection within 6 hours for every time-point without
causal model. For a patient’s record, We use a ﬁx-length
sliding window, with 1 hour step, to sample ﬁx-length
records xt = rt−L+1:t (zero ﬁlling if t < L).
The 40 columns of the record contain 37 numerical vari-
ables and 3 binary variables. At the preprocessing stage,
we relabel the 3 variables of two-categorical from 0 to 6
(6 clinical categories and one empty category for NaN).
Finally we reorder the categorical variables to the last
columns. As for numerical variables, in order to make the
deep model converge easily, for each numerical variable,
z-score normalization is applied.
3.
Proposed Model
In this section,
Heterogeneous Event Aggregation
(HEA) module is designed to effectively capture the in-
teraction information among the heterogeneous clinical
events. The motivations of HEA are listed following: (1)
Modeling interaction of both categorical and numerical
heterogeneous clinical events from their embedding. (2)
Grouping events into multiple heads in different aspects.
(3) Shortening the length of clinical event sequence.
After the feature is extracted from HEA, the temporary
dependency is captured by bidirectional LSTM. At last, the
ﬁnal outputs of 2 direction is sum up and forwarded to a
single dense layer with sigmoid activation to get the detec-
tion.
The proposed architecture is shown in Figure 1. Given
a sequential clinical record (X1, X2, X3...XL) Xi ∈R40,
our objective is to generate an early prediction of sepsis
Figure 1. The architecture of our proposed model
for the last time step XL. Heterogeneous Event Aggrega-
tion (HEA) module is composed of two parts, Heteroge-
neous Events Embedding and Attentional Multihead Ag-
gregation, which are speciﬁcally explained as follows.
3.1.
Heterogeneous Events Embedding
Given the sequential clinical data, the ﬁrst step of our
model is to generate the embedding that can be used to
capture the interaction representation among the heteroge-
neous clinical events [8]. For each time step Xt ∈R40
(the ﬁrst 37 columns are numerical variables, and the last 3
are categorical variables). Randomly initialized numerical
event vector book Wne ∈R37×d, categorical event lookup
table Wce ∈R7×d and value vector table Wvn ∈R37×d
are generated. The embedding for Xt is then generated as:
Et = Mask(Concat(Ent, Ect))
(1)
Ent = Wne + Xt[: 37]Wvn
(2)
Ect = Embedding_lookup(Xt[37 :], Wce)
(3)
Kt = Concat(Wne, Ect)
(4)
Mask function is used to mask the event embedding to
zero if the corresponding variable is default. d is the di-
mensional numbers of embedding. Et ∈R40×d is com-
bination of both numerical and categorical embedding,
Ent ∈R37×d is the numerical embedding, Ect ∈R3×d is
the categorical embedding, Kt ∈R40×d is the Key matrice
of both numerical and categorical events.


## Page 3


Figure 2. An example of two-heads events aggregation
3.2.
Attentional Events Aggregation
It is difﬁcult to extract the information through the long
sequential data for the two reasons: (1) Within the long
sequential record, the interaction among heterogeneous
events could be complex, it is difﬁcult to capture the dy-
namic interaction events representation; (2) The total di-
mensional numbers of the heterogeneous events embed-
ding could be disastrously vast, making it impossible for
the sequential model to capture the temporal representa-
tion.
To effectively capture the dynamic heterogeneous events
representation, we propose attentional multihead aggrega-
tion. Given a time step events embedding Et ∈R40×d, M
randomly initialized mask-vectors are generated. Differ-
ent masks are used to capture different aspects of events-
interaction at timet with attention-based mechanism. At
last, all heads are concatenated to produce the eventual ag-
gregation representation. The details of the aggregation are
shown as follows:
hi =
40
X
j=1
attscorei(Kt[j], mi)(WviEt[j])
(5)
attscorei(k, m) = Softmax((Wkik) · m)
(6)
a = Concat(h1, h2, ..., hm)
(7)
Where hi ∈Rd is the ith head of aggregation represen-
tation, a ∈RM·d concatenates all heads, attscorei is the
attention mechanism of the ith Head, getting the aggrega-
tion proportion of each event with calculating the dot prod-
uct between events and Mask. Each head could capture its
own concerned events information with its corresponding
formed transform matrices Wk, Wv and Mask vector m.
An example of two-heads aggregation is shown as Figure
2.
3.3.
Sequential Model and Prediction
For each time step, we get an aggregation representa-
tion. Given X ∈RL×40, a temporal events aggregation
representation a ∈RL×(M·d) is captured. As LSTM is
successfully used in sequential data, we pass on A to one-
layer bidirectional LSTM module. We sum up the last-
time outputs of both forward and backward units and get
the logits through a single dense layer with sigmoid activa-
tion. Our objective is a binary classiﬁcation, we use cross
entropy:
L(y, ˆy) = −(ˆy · log(y) + (1 −ˆy) · log(1 −y))
(8)
4.
Experiment Results
Table 1. local partitioned test metrics for different model
Model
AUC
APC
Utility score
MLP
0.7723
0.0711
0.2413
Transformer
0.8013
0.0923
0.3619
LSTM
0.8165
0.1040
0.3723
1-head-HEA-Transformer
0.8092
0.0955
0.3775
1-head-HEA-LSTM
0.8241
0.1120
0.3877
8-heads-HEA-Transformer
0.8264
0.1236
0.3968
8-heads-HEA-LSTM
0.8400
0.1307
0.4096
16-heads-HEA-LSTM
0.8410
0.1314
0.4126
4.1.
Implementation Details
The provided data is divided into train and test sets at
the ratio of 7 to 3. To conduct a further experiment, we
divide the data into train and held sets at the ratio of 9
to 1, and then 5-fold cross validation is established. To
evaluate our proposed module, we directly use a MLP pre-
diction model, Transformer and LSTM with dense layer
embedding, set various numbers of heads to gain different
models. The results show that our proposed model, with
high efﬁciency, can obviously improve the performance.
We keep L as 24 (one day) in all experiments.
Multihead aggregation:
We keep dimensional num-
bers(d) as 16 and set heads to be 1, 8 and 16 as 3 different
aggregation modules.
We measure Area Under the Receiver Operating Char-
acteristic curve (AUC) and Area Under The Precision Re-
call Curve (APC) as our evaluation metrics. What’s more,
the utility score function deﬁned in CinC2019 challenge is
used as the extra metric.
4.2.
Baseline
MLP: Without considering the temporal information,
Multi-layer perception can be used to directly model the
raw record.


## Page 4


Table 2. local cross-validation metrics for HEA
Model
AUC
APC
Utility score(average/major vote/any vote)
8-heads-HEA-Transformer
0.8186
0.1049
0.3641/0.3635/0.3658
8-heads-HEA-LSTM
0.8206
0.1031
0.3656/0.3613/0.3643
16-heads-HEA-LSTM
0.8224
0.1052
0.3817/0.3750/0.3830
Dense Layer Embedding: Given a one-time sampled
record x, the dense representation layer use a single dense
layer with activation to generate the representation ˆx ∈R.
Transformer / LSTM: Conventional sequential model
Transformer and LSTM use a single dense layer embed-
ding to capture the events representation.
4.3.
Result
We ﬁrstly conduct an experiment for different models
over train and test sets. The results over the test set are
shown as Table 1. It should be noticed that all the met-
rics on both Table 1 and Table 2 are based on the locally
partitioned test set from the public dataset.
The result shows that heterogeneous events aggregation
modules could improve the metrics obviously, then we
have the further experiment over 5-fold cross validation.
The results over the held set are as Table 2 shows.
What’s more, our proposed model is in high efﬁciency,
for it just needs to calculate the attention score between
events and multiple heads. With a GeForce GTX 1080
10G, our proposed model with 16 heads cost 10 minutes
per epoch to train over 10240000 training samples.
In thePhysioNet/Computing in Cardiology Challenge
2019, we got the results of score (0.402, 0.386, -0.169)
on the test set A,B and C, with the overall utility score of
0.321, ranking the 13th out of 78 teams.
5.
Conclusion
We proposed an attention-based sequential representa-
tion model to do early sepsis prediction from clinical data.
Our proposed model includes two main parts: clinical
events interaction extraction with heterogeneous events ag-
gregation and temporal interaction capture with LSTM.
Experiments in the PhysioNet/Computing in Cardiology
Challenge 2019 show that the heterogeneous event ag-
gregation module can shorten the length of clinical event
sequence for better temporal dependency modeling, and
the separated storage strategy of aggregation representa-
tion with different heads retains temporal interactions of
events.
Acknowledgments
This paper is partially supported by National Key
Research and Development Program of China with
Grant No. 2018AAA0101900, Beijing Municipal Com-
mission of Science and Technology under Grant No.
Z181100008918005, and the National Natural Science
Foundation of China (NSFC Grant No. 61772039 and No.
91646202).
References
[1] Reyna M, Josef C, Jeter R, Shashikumar S, Westover M,
Nemati S, Clifford G, Sharma A. Early prediction of sep-
sis from clinical data: the physionetcomputing in cardiology
challenge 2019. Critical Care Medicine 2019 In press;.
[2] Miotto R, Wang F, Wang S, Jiang X, Dudley JT.
Deep
learning for healthcare: review, opportunities and challenges.
Brieﬁngs in Bioinformatics 2017;.
[3] Qian F, Gong C, Liu L, Sha L, Zhang M. Topic medical
concept embedding: Multi-sense representation learning for
medical concept. In 2017 IEEE International Conference on
Bioinformatics and Biomedicine (BIBM). IEEE, 2017; 404–
409.
[4] Hochreiter S, Schmidhuber J.
Long short-term memory.
Neural computation 1997;9(8):1735–1780.
[5] Vaswani A, Shazeer N, Parmar N, Uszkoreit J, Jones L,
Gomez AN, Kaiser Ł, Polosukhin I.
Attention is all you
need. In Advances in Neural Information Processing Sys-
tems. 2017; 5998–6008.
[6] Che Z, Purushotham S, Li G, Jiang B, Liu Y.
Hierarchi-
cal deep generative models for multi-rate multivariate time
series. In International Conference on Machine Learning.
2018; 783–792.
[7] Liu L, Li H, Hu Z, Shi H, Wang Z, Tang J, Zhang M. Learn-
ing hierarchical representations of electronic health records
for clinical outcome prediction. In AMIA Annual Sympo-
sium. 2019; .
[8] Liu L, Shen J, Zhang M, Wang Z, Tang J. Learning the joint
representation of heterogeneous temporal events for clinical
endpoint prediction. In Thirty-Second AAAI Conference on
Artiﬁcial Intelligence. 2018; .
Address for correspondence:
Ming Zhang
1628, No.1 Science Building, Peking University, Beijing, China
mzhang_cs@pku.edu.cn

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
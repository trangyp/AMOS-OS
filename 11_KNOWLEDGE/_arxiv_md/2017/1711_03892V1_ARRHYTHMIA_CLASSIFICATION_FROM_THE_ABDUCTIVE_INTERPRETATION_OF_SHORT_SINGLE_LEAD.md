---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1711.03892v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1711.03892v1_Arrhythmia_Classification_from_the_Abductive_Interpretation_of_Short_Single-Lead

> Source: 1711.03892v1_Arrhythmia_Classification_from_the_Abductive_Interpretation_of_Short_Single-Lead.pdf

> Pages: 4

---


## Page 1


Arrhythmia Classiﬁcation from the Abductive Interpretation of Short
Single-Lead ECG Records
Tomás Teijeiro*, Constantino A. García, Daniel Castro and Paulo Félix
Centro Singular de Investigación en Tecnoloxías da Información (CITIUS), University of Santiago de
Compostela, Santiago de Compostela, Spain
Abstract
In this work we propose a new method for the rhythm
classiﬁcation of short single-lead ECG records, using a set
of high-level and clinically meaningful features provided
by the abductive interpretation of the records. These fea-
tures include morphological and rhythm-related features
that are used to build two classiﬁers: one that evaluates the
record globally, using aggregated values for each feature;
and another one that evaluates the record as a sequence,
using a Recurrent Neural Network fed with the individual
features for each detected heartbeat. The two classiﬁers
are ﬁnally combined using the stacking technique, provid-
ing an answer by means of four target classes: Normal si-
nus rhythm (N), Atrial ﬁbrillation (A), Other anomaly (O)
and Noisy (~). The approach has been validated against
the 2017 Physionet/CinC Challenge dataset, obtaining a
ﬁnal score of 0.83 and ranking ﬁrst in the competition.
1.
Introduction
The potential of Artiﬁcial Intelligence and machine
learning techniques to improve the early detection of car-
diac diseases using low-cost ECG tests is still largely un-
tapped.
The 2017 Physionet/Computing in Cardiology
challenge deﬁes the scientiﬁc community to propose solu-
tions to the automatic detection of Atrial Fibrillation from
short single lead ECG signals [1]. The challenge is posed
as a classical machine learning problem: A labeled train-
ing set is provided, and the proposals are evaluated against
a hidden test set of records. However, even if the only
metric for the ﬁnal ranking is the accuracy of the proposed
models, a number of additional properties should be con-
sidered for the ﬁnal adoption of each proposal in the clin-
ical practice. Here, we emphasize on the interpretability
of the automatic detection of Atrial Fibrillation, a major
concern to ensure trust by the care staff [2].
In this sense, our proposal is based on a high-level de-
scription of the target signal by means of the same features
used by cardiologists in ECG analysis. This description
is generated with a pure knowledge-based approach, using
an abductive framework for time series interpretation [3]
that looks for the set of explanatory hypotheses that best
account for the observed evidence. Only after this descrip-
tion has been built, machine learning methods were used
to make up for the lack of the expert criteria applied in the
labeling of the training set, and to alleviate the effect of
possible errors in the interpretation process.
2.
Methods
The global architecture of the proposal is depicted in
Figure 1, and the processing stages are explained in the
following subsections.
2.1.
Preprocessing
The preprocessing stage aims at improving the quality
of the data to be interpreted in the following stages, and
involves two different tasks:
2.1.1. Data relabeling: The labeling of the training set
was performed by a single expert in a single pass, and as a
consequence some inconsistencies appear in the classiﬁca-
tion criteria. Thus, a thorough manual relabeling was car-
ried out, but trying to be conservative and guided by pre-
liminary classiﬁcation results. We focused on records clas-
siﬁed as N but showing what we consider clear anomalies.
A total number of 197 out of 8528 records were relabeled.
2.1.2. Lead inversion detection: A number of records in
the training set were found to be inverted, probably due to
electrode misplacement. Inverted records are more likely
to be classiﬁed as abnormal due to the presence of infre-
quent QRS and T wave morphologies, as well as to the
greater difﬁculty to identify P waves. The inverted records
were ﬁrst identiﬁed manually, and then a simple logistic
regression classiﬁer was trained considering 14 features
obtained from the raw signal and a tentative delineation
of the P wave, QRS complex and T wave of every heart-
beat detected by the gqrs application from the Physionet
library [4]. This delineation was performed using the Con-
strue algorithm [3], limiting the interpretation to the con-
duction level, that is, avoiding the rhythm interpretation.
arXiv:1711.03892v1  [cs.AI]  10 Nov 2017


## Page 2


ECG Signal
Abductive
Interpretation
Per-Beat Features
Global 
Classiﬁcation
Sequence
Classiﬁcation
Classiﬁcation
Stacking
Final Class
Global Features
Lead Inversion
Detection
Figure 1. Classiﬁcation algorithm steps.
2.2.
Abductive interpretation
The abductive interpretation of the ECG signal is the
most signiﬁcant stage in the proposed approach. Its ob-
jective is to characterize the physiological processes un-
derlying the signal behavior, building a description of the
observed phenomena in multiple abstraction levels. This
responsibility lies with the Construe algorithm, which ap-
plies a non-monotonic reasoning scheme to ﬁnd the set
of hypotheses that best explain the observed evidence, by
means of a domain-speciﬁc knowledge base composed of
a set of observables and a set of abstraction grammars.
The knowledge base is the same used in [3], that allows to
explain the ECG at the conduction and rhythm abstraction
levels, thus providing the same features used by cardiol-
ogists in ECG analysis. The initial evidence is the set of
waves identiﬁed in the wave delineation step, that are ab-
stracted by a set of rhythm patterns to describe the full sig-
nal as a sequence of cardiac rhythms, including normal si-
nus rhythms, bradycardias, tachycardias, atrial ﬁbrillation
episodes, etc. The non-monotonic nature of the interpreta-
tion process allows us to modify the initial set of evidence,
by discarding heartbeats that cannot be abstracted by any
rhythm pattern, or by looking for missed beats that are pre-
dicted by the pattern selected as the best explanatory hy-
pothesis for a signal fragment. This ability to correct the
initial evidence is the main strength of our proposal, since
it discards many false anomalies generated by the presence
of noise and artifacts in the signal. Figure 2 shows an ex-
ample of a noisy signal in which the gqrs application de-
tects many false positive beats, that are removed or modi-
ﬁed in the ﬁnal interpretation that concludes with a single
normal rhythm hypothesis that explains the full fragment.
As we can also see in the Figure, the result of the inter-
pretation stage is a sequence of P waves, QRS complexes
and T waves observations, as well as a sequence of cardiac
rhythms abstracting all those waves.
2.3.
Global feature extraction
Considering that each ECG record has to be classiﬁed
globally, providing a single label for the entire signal du-
ration, after the interpretation stage a set of features are
calculated trying to summarize the information provided
by Construe. A total number of 79 features are calculated,
that are comprehensively described in the published soft-
ware documentation. The feature set is divided into three
main groups:
• Rhythm features: This includes statistical measures on
the RR sequence, such as the limits, median or median ab-
solute deviation; heart rate variability features such as the
PNN5, PNN10, PNN50 and PNN100 measures [5]; and
information about the rhythm interpretation, such as the
median duration of each rhythm hypothesis.
• Morphological features:
This includes information
about the duration, amplitude and frequency spectrum of
the observations in the conduction abstraction level, in-
cluding P and T waves, QRS complexes, PR and QT in-
tervals, and the TP segments.
• Signal quality features: Their purpose is to assess the
importance of the morphological features showing conduc-
tion anomalies, such as wide QRS complexes or long PR
intervals. They are based on the sum of the absolute dif-
ferences of the signal, which we refer to as proﬁle. Some
of the proﬁled areas of the signal are the baseline segments
and the P wave area before each heartbeat (taking a con-
stant window of 250 ms).
2.4.
Global classiﬁcation
If a precise deﬁnition of the expert knowledge leading
to the labeling of the training set were available, then the
ﬁnal classiﬁcation could be directly developed with a basic
rule-based system operating on the features extracted from
the abductive interpretation stage, and the accuracy of the
system would depend mainly on the accuracy of the inter-
pretations. However, the challenge does not publish any
guidelines for the classiﬁcation, specially for the O class.
Therefore, an automatic classiﬁer was trained with two ob-
jectives: 1) To reveal the criteria leading to the training set
labeling; and 2) to make the classiﬁcation more accurate
by learning possible mistakes of the abductive interpreta-
tion.
The classiﬁcation method selected for this stage was
the Tree Gradient Boosting algorithm, and particularly the
XGBoost implementation [6], which showed a high per-
formance and a certain level of interpretability through the
importance given to the classiﬁcation features. The opti-
mization of the hyperparameters was performed using ex-
haustive grid search and 8-fold cross-validation, leading to
the following values: Maximum tree depth: 6, Learning
rate: 0.2, Gamma: 1.0, Column subsample by tree: 0.9,
Min. child weight: 20, Subsample: 0.8, and Number of
boosting rounds: 60.


## Page 3


Figure 2. How the abductive interpretation can ﬁx errors in the initial evidence. [Source: First 10 seconds of the A02080 record.
Grey: Original gqrs annotations. Blue: QRS observations. Yellow: T wave observations. Green: P wave observation and Normal rhythm hypothesis.]
With respect to the ﬁrst objective, we were able to for-
malize a number of speciﬁc anomalies that lead to classify
a record as O. This identiﬁcation helped to optimize the
training set by deﬁning more speciﬁc features to be calcu-
lated from the interpretation results. Some of the identiﬁed
anomalies sharing this class were:
• Tachycardia (Mean heart rate over 100 bpm).
• Bradycardia (Mean heart rate under 50 bpm).
• Wide QRS complex (Longer than 110 milliseconds).
• Presence of ventricular or fusion beats.
• Presence of at least one extrasystole.
• Long PR interval (Longer than 210 milliseconds).
• Ventricular tachycardia.
• Atrial ﬂutter.
For some of these anomalies the classiﬁcation in the
training set seems a bit inconsistent, since examples can
be found in several classes. For example, there are vari-
ous records labeled as normal with PR interval longer than
210 milliseconds, as long as examples of records labeled
as atrial ﬁbrillation showing an atrial ﬂutter pattern.
Regarding the second objective, even after discovering
some of the expert criteria distinguishing the target classes
a rule-based system was not still competitive against auto-
matic learned models. From our point of view this shows
that the XGBoost classiﬁer is able to improve the results
of the interpretation alone.
2.5.
Per-beat feature extraction
Some of the conditions leading to a certain classiﬁca-
tion may not be present for the entire duration of a record,
so the global features are not the best option to charac-
terize episodic events of abnormalities. For example, a
normal record with a single ectopic ventricular beat that
does not break the rhythm is quite difﬁcult to classify as
abnormal by the global classiﬁer. For this reason, some
of the features calculated from the abductive interpretation
are disaggregated to the individual heartbeat scope, such as
the morphology, duration and amplitude of the P wave, the
QRS complex and the T wave. Also the RR interval and
the RR variation before and after each beat is included, as
long as the proﬁle of the P wave area. A sequence classiﬁ-
cation approach is then used to learn characteristic tempo-
ral patterns of each target class.
2.6.
Sequence classiﬁcation
In the proposed approach, sequence classiﬁcation relies
on Recurrent Neural Networks (RNNs), a family of neural
networks specialized for recognizing sequences of values.
Among the different RNN implementations, we focused
on Long Short Term Memory networks (LSTMs) [7], since
they are capable of remembering information for long pe-
riods of time through the use of a cell state. Furthermore,
they are able to avoid vanishing and exploding gradients
when doing backpropagation through time. The architec-
ture of the neural net is shown in Figure 3. The time-
distributed Multilayer Perceptron (MLP) preprocesses the
features described in Section 2.5 to transform the data into
a space with easier temporal dynamics. The number of
hidden units of the MLP was 256, and the dimension of
the output space 128.
A Rectiﬁed Linear Unit (ReLU)
was used as activation function. The LSTM_0 layer pre-
processes the resulting sequence of transformed features
and returns a new sequence, which is subsequently used
by the other LSTMs. The LSTM_2 layer just returns the
ﬁnal state of the network, whereas LSTM_1 and LSTM_3
return new transformed sequences. The pooling layers af-
ter LSTM_1 and LSTM_3 remove the temporal dimension
by computing the temporal mean and maximum of each
feature of the sequences, respectively. All the LSTMs used
128 units. Another MLP (with the same conﬁguration of
the time-distributed one) joins and transforms the outputs
of each LSTM before a Softmax layer, which outputs a
probability for each of the 4 classes. L2-regularization was
applied to all layers, using 10−4 as regularization strength.
Finally, dropout was also used to improve generalization
by preventing feature co-adaptation [8].
The neural network was trained using the categorical
cross-entropy as loss function, a batch size of 32, and
Adam [9] as optimizer. Furthermore, 15% of all the data
was used as validation set to monitor the performance of
the neural network.
This permitted us to decrease the
learning rate when the validation loss got stuck in a plateau
and to avoid overﬁtting by using early stopping. The ini-
tial learning rate was set to 0.002 and it was decreased by
√
2 when the validation loss did not improve for at least 3
epochs. Training was ended after 15 epochs without im-
provement.


## Page 4


Padded sequence
of 
beat features
LSTM_0
Temporal
mean pooling
Temporal 
max pooling
MLP
Sequence
 Class
Time-distributed
MLP
LSTM_3
Softmax
LSTM_2
LSTM_1
Figure 3. The neural network architecture.
2.7.
Classiﬁcation stacking
The XGBoost classiﬁer based on global features and the
RNN classiﬁer based on the per-beat features were com-
bined using the stacking technique. Stacking (also referred
to as stacked generalization) involves training a new clas-
siﬁcation algorithm to combine the predictions of several
classiﬁers [10]. Usually, the stacked model achieves better
performance than the individual models due to its ability
to discern when each base model performs best and when
it performs poorly. Prior to the application of stacking, the
predictions of 3 RNNs were averaged to decrease the vari-
ance of the RNN classiﬁer arising from the random ini-
tialization of the RNN weights and the random split be-
tween test and validation set. Averaging similar models
also helps in reducing overﬁtting. Note that this averag-
ing can be seen as a simple bagging method. The proba-
bilities predicted by the XGBoost and the averaged RNNs
are then combined through a Linear Discriminant Analysis
(LDA) classiﬁer, which acts as stacker. To avoid possible
collinearity issues, only 3 probabilities from each model
are used.
3.
Evaluation
To evaluate the performance of the algorithm, we fol-
lowed the challenge guidelines and metrics. The ﬁnal score
is assigned as the mean F1 measure of the N, A, and O
classes. Table 1 shows an example of the results that the
proposed method is able to achieve using 8-fold cross-
validation. Note that the stacker usually achieves better
scores than the base models and, furthermore, it has lower
variance (not shown in the Table).
Table 1. Example of stratiﬁed 8-fold cross-validation.
Fold Number
Mean
Method
0
1
2
3
4
5
6
7
XGBoost
0.84 0.84 0.85 0.85 0.82 0.80 0.82 0.82
0.83
RNN
0.82 0.81 0.84 0.83 0.86 0.83 0.83 0.83
0.83
LDA-stacker 0.85 0.84 0.86 0.86 0.85 0.83 0.84 0.85
0.85
4.
Conclusions
This work proves that the combination of knowledge-
based and learning-based approaches is effective to build
classiﬁcation systems that exploit sophisticated machine
learning methods while maintaining a remarkable degree
of interpretability by the use of high-level and meaningful
features.
Acknowledgements
This work was supported by the Spanish Ministry of
Economy and Competitiveness under project TIN2014-
55183-R. Constantino A. García is also supported by the
FPU Grant program from the Spanish Ministry of Educa-
tion (MEC) (Ref. FPU14/02489).
References
[1]
Clifford G, Liu C, Moody B, Lehman L, Silva I, Li Q, John-
son A, Mark R. AF classiﬁcation from a short single lead
ECG recording: The Physionet Computing in Cardiology
Challenge 2017. In Computing in Cardiology. 2017; .
[2]
Caruana R, Lou Y, Gehrke J, Koch P, Sturm M, Elhadad
N.
Intelligible Models for HealthCare.
In 21th ACM
SIGKDD International Conference on Knowledge Discov-
ery and Data Mining. ACM Press, 2015; .
[3]
Teijeiro T, Félix P, Presedo J, Castro D. Heartbeat classi-
ﬁcation using abstract features from the abductive interpre-
tation of the ECG. IEEE Journal of Biomedical and Health
Informatics 2016;.
[4]
Goldberger A, et al. PhysioBank, PhysioToolkit and Phys-
ioNet: Components of a New Research Resource for Com-
plex Physiologic Signals. Circulation 2000;101:215–220.
[5]
Mietus JE, Peng CK, Henry I, Goldsmith RL, Goldberger
AL. The pNNx ﬁles: re-examining a widely used heart rate
variability measure. Heart British Cardiac Society oct 2002;
88(4):378–80. ISSN 1468-201X.
[6]
Chen T, Guestrin C. XGBoost: A Scalable Tree Boosting
System. In 22nd ACM SIGKDD International Conference
on Knowledge Discovery and Data Mining. mar 2016; .
[7]
Hochreiter S, Schmidhuber J.
Long short-term memory.
Neural computation 1997;9(8):1735–1780.
[8]
Srivastava N, Hinton GE, Krizhevsky A, Sutskever I,
Salakhutdinov R. Dropout: a simple way to prevent neu-
ral networks from overﬁtting. Journal of machine learning
research 2014;15(1):1929–1958.
[9]
Kingma D, Ba J. Adam: A method for stochastic optimiza-
tion. arXiv preprint arXiv14126980 2014;.
[10] Wolpert DH.
Stacked generalization.
Neural networks
1992;5(2):241–259.
Address for correspondence:
Tomás Teijeiro Campo
Rúa de Jenaro de la Fuente Domínguez, S/N, CITIUS Building
15782 Santiago de Compostela, SPAIN
tomas.teijeiro@usc.es

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
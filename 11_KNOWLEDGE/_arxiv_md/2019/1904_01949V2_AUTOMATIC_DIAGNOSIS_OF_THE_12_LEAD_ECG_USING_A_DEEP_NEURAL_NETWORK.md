---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1904.01949v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1904.01949v2_Automatic_diagnosis_of_the_12-lead_ECG_using_a_deep_neural_network

> Source: 1904.01949v2_Automatic_diagnosis_of_the_12-lead_ECG_using_a_deep_neural_network.pdf

> Pages: 17

---


## Page 1


Automatic diagnosis of the 12-lead ECG using a
deep neural network
Antˆonio H. Ribeiroa, b, 1, Manoel Horta Ribeiroa, Gabriela M.M. Paix˜aoa, c, Derick M. Oliveiraa, Paulo R. Gomesa, c,
J´essica A. Canazarta, c, Milton P. S. Ferreiraa, c, Carl R. Anderssonb, Peter W. Macfarlaned, Wagner Meira Jr.a,
Thomas B. Sch¨onb, 2, and Antonio Luiz P. Ribeiroa, c, 3
aUniversidade Federal de Minas Gerais, Brazil, bUppsala University, Sweden, cTelehealth Center from Hospital das Cl´ınicas da Universidade Federal de
Minas Gerais, Brazil, dGlasgow University, Scotland, 1antonio-ribeiro@ufmg.br, 2thomas.schon@it.uu.se, 3tom@hc.ufmg.br
Abstract
The role of automatic electrocardiogram (ECG) analysis in clinical practice is limited by the accuracy of
existing models. Deep Neural Networks (DNNs) are models composed of stacked transformations that learn
tasks by examples. This technology has recently achieved striking success in a variety of task and there
are great expectations on how it might improve clinical practice. Here we present a DNN model trained
in a dataset with more than 2 million labeled exams analyzed by the Telehealth Network of Minas Gerais
and collected under the scope of the CODE (Clinical Outcomes in Digital Electrocardiology) study. The
DNN outperform cardiology resident medical doctors in recognizing 6 types of abnormalities in 12-lead ECG
recordings, with F1 scores above 80% and speciﬁcity over 99%. These results indicate ECG analysis based
on DNNs, previously studied in a single-lead setup, generalizes well to 12-lead exams, taking the technology
closer to the standard clinical practice.
Preprint. The ﬁnal version of this paper was published in Nature Communications – volume: 11, article number: 1760 (2020).
https://doi.org/10.1038/s41467-020-15432-4.
@article{ribeiro_automatic_2020,
title = {Automatic diagnosis of the 12-lead {{ECG}} using a deep neural network},
author = {Ribeiro, Ant{\^o}nio H. and Ribeiro, Manoel Horta and Paix{\~a}o, Gabriela M. M. and Oliveira, Derick M. and Gomes,
Paulo R. and Canazart, J{\’e}ssica A. and Ferreira, Milton P. S. and Andersson, Carl R. and Macfarlane, Peter W. and Meira
Jr., Wagner and Sch{\"o}n, Thomas B. and Ribeiro, Antonio Luiz P.},
journal = {Nature Communications}
year = {2020},
volume = {11},
number = {1},
pages = {1760},
issn = {2041-1723},
doi = {10.1038/s41467-020-15432-4},
url = {https://doi.org/10.1038/s41467-020-15432-4},
}
1
arXiv:1904.01949v2  [cs.LG]  14 Apr 2020


## Page 2


C
ardiovascular diseases are the leading cause of death worldwide [1] and the electrocardiogram (ECG) is a
major tool in their diagnoses. As ECGs transitioned from analog to digital, automated computer analysis
of standard 12-lead electrocardiograms gained importance in the process of medical diagnosis [2, 3]. However,
limited performance of classical algorithms [4, 5] precludes its usage as a standalone diagnostic tool and relegates
them to an ancillary role [6, 3].
Deep neural networks (DNNs) have recently achieved striking success in tasks such as image classiﬁcation [7]
and speech recognition [8], and there are great expectations when it comes to how this technology may improve
health care and clinical practice [9, 10, 11]. So far, the most successful applications used a supervised learning
setup to automate diagnosis from exams.
Supervised learning models, which learn to map an input to an
output based on example input-output pairs, have achieved better performance than a human specialist on
their routine work-ﬂow in diagnosing breast cancer [12] and detecting retinal diseases from three-dimensional
optical coherence tomography scans [13]. While eﬃcient, training DNNs in this setup introduces the need for
large quantities of labeled data which, for medical applications, introduce several challenges, including those
related to conﬁdentiality and security of personal health information [14].
A convincing preliminary study of the use of DNNs in ECG analysis was recently presented in [15]. For
single-lead ECGs, DNNs could match state-of-the-art algorithms when trained in openly available datasets (e.g.
2017 PhysioNet Challenge data [16]) and, for a large enough training dataset, present superior performance
when compared to practicing cardiologists. However, as pointed out by the authors, it is still an open question
if the application of this technology would be useful in a realistic clinical setting, where 12-lead ECGs are the
standard technique [15].
The short-duration, standard, 12-lead ECG (S12L-ECG) is the most commonly used complementary exam
for the evaluation of the heart, being employed across all clinical settings, from the primary care centers to
the intensive care units. While long-term cardiac monitoring, such as in the Holter exam, provides information
mostly about cardiac rhythm and repolarization, the S12L-ECG can provide a full evaluation of the cardiac
electrical activity.
This includes arrhythmias, conduction disturbances, acute coronary syndromes, cardiac
chamber hypertrophy and enlargement and even the eﬀects of drugs and electrolyte disturbances. Thus, a deep
learning approach that allows for accurate interpretation of S12L-ECGs would have the greatest impact.
S12L-ECGs are often performed in settings, such as in primary care centers and emergency units, where
there are no specialists to analyze and interpret the ECG tracings. Primary care and emergency department
health professionals have limited diagnostic abilities in interpreting S12-ECGs [17, 18]. The need for an accurate
automatic interpretation is most acute in low and middle-income countries, which are responsible for more than
75% of deaths related to cardiovascular disease [19], and where the population, often, do not have access to
cardiologists with full expertise in ECG diagnosis.
The use of DNNs for S12L-ECG is still largely unexplored. A contributing factor for this is the shortage of
full digital S12L-ECG databases, since most recordings are still registered only on paper, archived as images,
or stored in PDF format [20]. Most available databases comprise a few hundreds of tracings and no systematic
annotation of the full list of ECG diagnoses [21], limiting their usefulness as training datasets in a supervised
learning setting. This lack of systematically annotated data is unfortunate, as training an accurate automatic
method of diagnosis from S12L-ECG would be greatly beneﬁcial.
In this paper, we demonstrate the eﬀectiveness of DNNs for automatic S12L-ECG classiﬁcation. We build a
large-scale dataset of labelled S12L-ECG exams for clinical and prognostic studies (the CODE - Clinical Out-
comes in Digital Electrocardiology study) and use it to develop a DNN to classify 6 types of ECG abnormalities
considered representative of both rhythmic and morphologic ECG abnormalities.
1
Results
1.1
Model speciﬁcation and training
We collected a dataset consisting of 2,322,513 ECG records from 1,676,384 diﬀerent patients of 811 counties
in the state of Minas Gerais/Brazil from the Telehealth Network of Minas Gerais (TNMG) [22]. The dataset
characteristics are summarized in Table 1.
The acquisition and annotation procedures of this dataset are
described in Methods. We split this dataset into a training set and a validation set. The training set contains
98% of the data. The validation set consists of the remaining 2% (˜50,000 exams) of the dataset and it was
used for hyperparameter tuning.
We train a DNN to detect: 1st degree AV block (1dAVb), right bundle branch block (RBBB), left bundle
branch block (LBBB), sinus bradycardia (SB), atrial ﬁbrillation (AF) and sinus tachycardia (ST). These 6
abnormalities are displayed in Figure 1.
We used a DNN architecture known as the residual network [23], commonly used for images, which we here
have adapted to unidimensional signals. A similar architecture has been successfully employed for detecting
abnormalities in single-lead ECG signals [15]. Furthermore, in the 2017 Physionet challenge [16], algorithms for
2


## Page 3


Figure 1: (Abnormalities examples) A list of all the abnormalities the model classiﬁes. We show only 3
representative leads (DII, V1 and V6).
3


## Page 4


Abnormality
Train+Val (n = 2,322,513)
Test (n = 827)
1dAVb
35,759 (1.5 %)
28 (3.4 % )
RBBB
63,528 (2.7% )
34 (4.1 %)
LBBB
39,842 (1.7%)
30 (3.6 %)
SB
37,949 (1.6%)
16 (1.9 %)
AF
41,862 (1.8%)
13 (1.6 %)
ST
49,872 (2.1%)
36 (4.4 %)
Age group
16-25
155,531 (6.7 %)
43 (5.2 % )
26-40
406,239 (17.5 %)
122 (14.8 % )
41-60
901.456 (38.8 %)
340 (41.1 % )
61-80
729,300 (31.4 %)
278 (33.6 % )
≥81
129,987 (5.6 %)
44 (5.3 % )
Sex
Male
922,780 (39.7 %)
321 (38.8 % )
Female
1,399,733 (60.3 %)
506 (61.2 % )
Table 1: (Dataset summary) Patient characteristcs and abnormalities prevalence, n (%).
detecting AF have been compared in an open dataset of single lead ECGs and, both the architecture described
in [15] and other convolutional architectures [24, 25] have achieved top scores.
The DNN parameters were learned using the training dataset and our design choices were made in order
to maximize the performance on the validation dataset. We should highlight that, despite using a signiﬁcantly
larger training dataset, we got the best validation results with an architecture with, roughly, one quarter the
number of layers and parameters of the network employed in [15].
1.2
Testing and perfomance evaluation
For testing the model we employed a dataset consisting of 827 tracings from distinct patients annotated by 3
diﬀerent cardiologists with experience in electrocardiography (see Methods). The test dataset characteristics
are summarized in Table 1. Table 2 shows the performance of the DNN on the test set. High-performance
measures were obtained for all ECG abnormalities, with F1 scores above 80% and speciﬁcity indexes over 99%.
We consider our model to have predicted the abnormality when its output — a number between 0 and 1 — is
above a threshold. Figure 2 shows the precision-recall curve for our model, for diﬀerent values of this threshold.
Neural networks are initialized randomly, and diﬀerent initialization usually yield diﬀerent results. In order
to show the stability of the method, we have trained 10 neural networks with the same set of hyperparameters
and diﬀerent initializations. The range between the maximum and minimum precision among these realizations,
for diﬀerent values of thereshold, are the shaded regions displayed in Figure 2. These realizations have micro
average precision (mAP) between 0.946 and 0.961, we choose the one with mAP imediatly above the median
value of all executions (the one with mAP = 0.951)1. All the analysis from now on will be for this realization of
the neural network, which correspond both to the strong line in Figure 2 and to the scores presented in Table 2.
For this model, Figure 2 shows the point corresponding to the maximum F1 score for each abnormality. The
threshold corresponding to this point is used for producing the DNN scores displayed in Table 2.
The same dataset was evaluated by: i) two 4th year cardiology residents; ii) two 3rd year emergency residents;
and, iii) two 5th year medical students. Each one annotated half of the exams in the test set. Their average
performances are given, together with the DNN results, in the Table 2 and their precision-recall scores are
plotted on Figure 2. Considering the F1 score, the DNN matches or outperforms the medical residents and
students for all abnormalities. The confusion matrices and the inter-rater agreement (kappa coeﬃcients) for the
DNN, the resident medical doctors and students are provided, respectively, in Supplementary Tables 1 and 2(a).
Additionally, in Supplementary Table 2(b) we compare the inter-rater agreement between the neural network
and the certiﬁed cardiologists that annotated the test set.
A trained cardiologist reviewed all the mistakes made by the DNN, the medical residents and the students,
trying to explain the source of the error. The cardiologist had meetings with the residents and students where
they together agreed on which was the source of the error. The results of this analysis are given in Table 3.
In order to compare of the performance diﬀerence between the DNN and resident medical doctors and
students, we compute empirical distributions for the precision (PPV), recall (sensitivity), speciﬁcity and F1
score using bootstraping [26]. The boxplots corresponding to these bootstrapped distributions are presented
in Supplementary Figure 1.
We have also applied the McNemar test [27] to compare the misclassiﬁcation
1We couldn’t choose the model with mAP equal to the median value because 10 is even number, hence there is no single middle
value.
4


## Page 5


Precision (PPV)
Recall (Sensitivity)
Speciﬁcity
F1 Score
DNN
cardio.
emerg.
stud.
DNN
cardio.
emerg.
stud.
DNN
cardio.
emerg.
stud.
DNN
cardio.
emerg.
stud.
1dAVb
0.867
0.905
0.639
0.605
0.929
0.679
0.821
0.929
0.995
0.997
0.984
0.979
0.897
0.776
0.719
0.732
RBBB
0.895
0.868
0.963
0.914
1.000
0.971
0.765
0.941
0.995
0.994
0.999
0.996
0.944
0.917
0.852
0.928
LBBB
1.000
1.000
0.963
0.931
1.000
0.900
0.867
0.900
1.000
1.000
0.999
0.997
1.000
0.947
0.912
0.915
SB
0.833
0.833
0.824
0.750
0.938
0.938
0.875
0.750
0.996
0.996
0.996
0.995
0.882
0.882
0.848
0.750
AF
1.000
0.769
0.800
0.571
0.769
0.769
0.615
0.923
1.000
0.996
0.998
0.989
0.870
0.769
0.696
0.706
ST
0.947
0.968
0.946
0.912
0.973
0.811
0.946
0.838
0.997
0.999
0.997
0.996
0.960
0.882
0.946
0.873
Table 2: (Performance indexes) Scores of our DNN are compared on the test set with the average performance
of: i) 4th year cardiology resident (cardio.); ii) 3rd year emergency resident (emerg.); and, iii) 5th year medical
students (stud.). (PPV = positive predictive value)
DNN
cardio.
emerg.
stud.
meas.
noise
unexplain.
meas.
noise
concep.
atte.
meas.
noise
concep.
atte.
meas.
noise
concep.
atte.
1dAVb
3
2
1
8
3
15
3
13
3
3
RBBB
3
1
4
2
1
8
3
2
LBBB
1
1
1
1
4
2
3
SB
4
4
4
1
5
2
1
AF
2
1
4
2
2
5
3
7
ST
2
1
2
1
5
1
1
1
1
1
2
1
5
Table 3: (Error analysis) Present the analysis of misclassiﬁed exams. The errors were classiﬁed into the
following categories: i) measurements errors (meas.)
were ECG interval measurements preclude the given
diagnosis by its textbook deﬁnition ; ii) errors due to noise, were we believe that the analyst or the DNN failed
due to a lower than usual signal quality; and, iii) other type of errors (unexplain.). Those were further divided,
for the medical residents and students, into two categories: conceptual errors (concep.), where our reviewer
suggested that the doctor failed to understand the deﬁnitions of each abnormality, and attention errors (atte.),
where we believe the error could be avoided if the reviewer had been more careful.
distribution of the DNN, the medical residents and the students. Supplementary Table 3 show the p-values of
the statistical test. Both analyses do not indicate a statistically signiﬁcant diﬀerence in performance among the
DNN and the medical residents and students for most of the classes.
Finally, to asses the eﬀect of how we structure our problem, we have considered alternative scenarios where
we use the 2,322,513 ECG records in 90%-5%-5% splits, stratiﬁed randomly, by patient or in chronological order.
Being the splits used, respectively, for training, validation and as a second larger test set. The results indicate
no statistically signiﬁcant diﬀerence between the original DNN used in our analysis and the alternative models
developed in the 90%-5%-5% splits. The exception is the model developed using the chronologically order split,
for which the changes along time in the telehealth center operation have aﬀected the splits (cf. Supplementary
Figure 2).
2
Discussion
This paper demonstrates the eﬀectiveness of ”end-to-end” automatic S12L-ECG classiﬁcation. This presents
a paradigm shift from the classical ECG automatic analysis methods [28].
These classical methods, such
as the University of Glasgow ECG analysis program [29], ﬁrst extract the main features of the ECG signal
using traditional signal processing techniques and then use these features as inputs to a classiﬁer. End-to-end
learning presents an alternative to these two-step approaches, where the raw signal itself is used as an input to
the classiﬁer which learns, by itself, to extract the features. This approach have presented, in a emergency room
setting, performance superior to commercial ECG software based on traditional signal processing techniques [30]
Neural networks have previously been used for classiﬁcation of ECGs both in a classical — feature-based
— setup [31, 32] and in an end-to-end learn setup [33, 34, 15]. Hybrid methods combining the two paradigms
are also available: the classiﬁcation may be done using a combination of handcrafted and learned features [35]
or by using a two-stage training, obtaining one neural network to learn the features and another to classify the
exam according to these learned features [36].
The paradigm shift towards end-to-end learning had a signiﬁcant impact on the size of the datasets used for
training the models. Many results using classical methods [28, 34, 36] train their models on datasets with few
examples, such as the MIT-BIH arrhythmia database [37], with only 47 unique patients. The most convincing
papers using end-to-end deep learning or mixed approaches, on the other hand, have constructed large datasets,
ranging from 3,000 to 100,000 unique patients, for training their models [35, 16, 15, 30].
Large datasets from previous work [35, 16, 15], however either were obtained from cardiac monitors and
Holter exams, where patients are usually monitored for several hours and the recordings are restricted to one or
two leads. Or, consist of 12-lead ECGs obtained in a emergency room setting [38, 30]. Our dataset with well over
5


## Page 6


0.0
0.2
0.4
0.6
0.8
1.0
0.0
0.2
0.4
0.6
0.8
1.0
Precision (PPV)
DNN
cardio.
emerg.
stud.
(a) 1dAVb
0.0
0.2
0.4
0.6
0.8
1.0
0.0
0.2
0.4
0.6
0.8
1.0
(b) RBBB
0.0
0.2
0.4
0.6
0.8
1.0
0.0
0.2
0.4
0.6
0.8
1.0
(c) LBBB
0.0
0.2
0.4
0.6
0.8
1.0
Recall (Sensitivity)
0.0
0.2
0.4
0.6
0.8
1.0
Precision (PPV)
(d) SB
0.0
0.2
0.4
0.6
0.8
1.0
Recall (Sensitivity)
0.0
0.2
0.4
0.6
0.8
1.0
(e) AF
0.0
0.2
0.4
0.6
0.8
1.0
Recall (Sensitivity)
0.0
0.2
0.4
0.6
0.8
1.0
(f) ST
Figure 2: (Precision-recall curve) Show precision-recall curve for our nominal prediction model on the test
set (strong line) with regard to each ECG abnormalities. The shaded region show the range between maximum
and minimum precision for neural networks trained with the same conﬁguration and diﬀerent initialization.
Points corresponding the performance of resident medical doctors and students are also displayed, together
with the point corresponding to the DNN performance for the same threshold used for generating Table 2.
Gray dashed curves in the background correspond to iso-F1 curves (i.e. curves in the precision-recall plane with
constant F1 score).
2 million entries, on the other hand, consists of short duration (7 to 10 seconds) S12L-ECG tracings obtained
from in-clinic exams and is orders of magnitude larger than those used in previous studies. It encompasses not
only rhythm disorders, like AF, SB and ST, as in previous studies [15], but also conduction disturbances, such
as 1dAVb, RBBB and LBBB. Instead of beat to beat classiﬁcation, as in the MIT-BIH arrhythmia database,
our dataset provides annotation for S12L-ECG exams, which are the most common in clinical practice.
The availability of such a large database of S12L-ECG tracings, with annotation for the whole spectrum of
ECG abnormalities, opens up the possibility of extending initial results of end-to-end DNN in ECG automatic
analysis [15] to a system with applicability in a wide range of clinical settings. The development of such tech-
nologies may yield high-accuracy automatic ECG classiﬁcation systems that could save clinicians considerable
time and prevent wrong diagnoses. Millions of S12L-ECGs are performed every year, many times in places
where there is a shortage of qualiﬁed medical doctors to interpret them. An accurate classiﬁcation system could
help to detect wrong diagnoses and improve the access of patients from deprived and remote locations to this
essential diagnostic tool of cardiovascular diseases.
The error analysis shows that most of the DNN mistakes were related to measurements of ECG intervals.
Most of those were borderline cases, where the diagnosis relies on a consensus deﬁnitions [39] that can only be
ascertained when a measurement is above a sharp cutoﬀpoint. The mistakes can be explained by the DNN
failing to encode these very sharp thresholds. For example, the DNN wrongly detecting a SB with a heart rate
slightly above 50 bpm or a ST with a heart rate slightly below 100 bpm. Supplementary Figure 3 illustrate this
eﬀect. Noise and interference in the baseline are established causes of error [40] and aﬀected both automatic
and manual diagnosis of ECG abnormalities. Nevertheless, the DNN seems to be more robust to noise and it
made fewer mistakes of this type compared to the medical residents and students. Conceptual errors (where our
reviewer suggested that the doctor failed to understand the deﬁnitions of each abnormality) were more frequent
for emergency residents and medical students than for cardiology residents. Attention errors (where we believe
that the error could have been avoided if the manual reviewer were more careful) were present at a similar ratio
for cardiology residents, emergency residents and medical students.
Interestingly, the performance of the emergency residents is worse than medical students for many abnormal-
ities. This might seem counter-intuitive because they do have less years of medical training. It might, however,
6


## Page 7


be justiﬁed by the fact that emergency residents, unlike cardiology residents, do not have to interpret these
exams on a daily basis, while medical students still have these concepts fresh from their studies.
Our work is perhaps best understood in the context of its limitations. While we obtained the highest F1 scores
for the DNN, the McNemar statistical test and bootstrapping suggest that we do not have conﬁdence enough
to assert that the DNN is actually better than the medical residents and students with statistical signiﬁcance.
We attribute this lack of conﬁdence in the comparison to the presence of relatively infrequent classes, where a
few erroneous classiﬁcations may signiﬁcantly aﬀect the scores. Furthermore, we did not test the accuracy of
the DNN in the diagnosis of other classes of abnormalities, like those related to acute coronary syndromes or
cardiac chamber enlargements and we cannot extend our results to these untested clinical situations. Indeed,
the real clinical setting is more complex than the experimental situation tested in this study and, in complex
and borderline situations, ECG interpretation can be extremely diﬃcult and may demand the input of highly
specialized personnel. Thus, even if a DNN is able to recognize typical ECG abnormalities, further analysis by
an experienced specialist will continue to be necessary to these complex exams.
This proof-of-concept study, showing that a DNN can accurately recognize ECG rhythm and morpholog-
ical abnormalities in clinical S12L-ECG exams, opens a series of perspectives for future research and clinical
applications. A next step would be to prove that a DNN can eﬀectively diagnose multiple and complex ECG
abnormalities, including myocardial infarction, cardiac chamber enlargement and hypertrophy and less com-
mon forms of arrhythmia, and to recognize a normal ECG. Subsequently, the algorithm should be tested in a
controlled real-life situation, showing that accurate diagnosis could be achieved in real-time, to be reviewed by
clinical specialists with solid experience in ECG diagnosis. This real-time, continuous evaluation of the algo-
rithm, would provide rapid feedback that could be incorporated as further improvements of the DNN, making
it even more reliable.
The TNMG, the large telehealth service from which the dataset used was obtained [22], is a natural laboratory
for these next steps, since it performs more than 2,000 ECGs a day and it is currently expanding its geographical
coverage over a large part of a continental country (Brazil). An optimized system for ECG interpretation, where
most of the classiﬁcation decisions are made automatically would imply that the cardiologists would only be
needed for the more complex cases. If such a system is made widely available, it could be of striking utility to
improve access to health care in low and middle-income countries, where cardiovascular diseases are the leading
cause of death and systems of care for cardiac diseases are lacking or not working well [41].
In conclusion, we developed an end-to-end DNN capable of accurately recognizing six ECG abnormalities
in S12L-ECG exams, with a diagnostic performance at least as good as medical residents and students. This
study shows the potential of this technology, which, when fully developed, might lead to more reliable automatic
diagnosis and improved clinical practice. Although expert review of complex and borderline cases seems to be
necessary even in this future scenario, the development of such automatic interpretation by a DNN algorithm
may expand the access of the population to this basic and useful diagnostic exam.
3
Methods
3.1
Dataset acquisition
All S12L-ECGs analyzed in this study were obtained by the Telehealth Network of Minas Gerais (TNMG), a
public telehealth system assisting 811 out of the 853 municipalities in the state of Minas Gerais, Brazil [22].
Since September 2017, the TNMG has also provided telediagnostic services to other Brazilian states in the
Amazonian and Northeast regions.
The S12L-ECG exam was performed mostly in primary care facilities
using a tele-electrocardiograph manufactured by Tecnologia Eletrnica Brasileira (So Paulo, Brazil) model TEB
ECGPC - or Micromed Biotecnologia (Brasilia, Brazil) - model ErgoPC 13. The duration of the ECG recordings
is between 7 and 10 seconds sampled at frequencies ranging from 300 to 600 Hz. A speciﬁc software developed
in-house was used to capture ECG tracings, to upload the exam together with the patients clinical history and
to send it electronically to the TNMG analysis center. Once there, one cardiologist from the TNMG experienced
team analyzes the exam and a report is made available to the health service that requested the exam through
an online platform.
We have incorporated the University of Glasgow (Uni-G) ECG analysis program (release 28.5, issued in
January 2014) in the in-house software since December 2017. The analysis program was used to automatically
identify waves and to calculate axes, durations, amplitudes and intervals, to perform rhythm analysis and to give
diagnostic interpretation [42, 29]. The Uni-G analysis program also provides Minnesota codes [43], a standard
ECG classiﬁcation used in epidemiological studies [44]. Since April 2018 the automatic measurements are being
shown to the cardiologists that give the medical report. All clinical information, digital ECGs tracings and the
cardiologist report were stored in a database. All previously stored data was also analyzed by Uni-G software
in order to have measurements and automatic diagnosis for all exams available in the database, since the ﬁrst
recordings. The CODE study was established to standardize and consolidate this database for clinical and
7


## Page 8


epidemiological studies. In the present study, the data (for patients above 16 years old) obtained between 2010
and 2016 was used in the training and validation set and, from April to September 2018, in the test set.
3.2
Labelling training data from text report
For the training and validation sets, the cardiologist report is available only as a textual description of the
abnormalities in the exam. We extract the label from this textual report using a three-step procedure. First,
the text is pre-processed by removing stop-words and generating n-grams from the medical report. Then, the
Lazy Associative Classiﬁer (LAC) [45], trained on a 2800-sample dictionary created from real diagnoses text
reports, is applied to the n-grams. Finally, the text label is obtained using the LAC result in a rule-based
classiﬁer for class disambiguation. The classiﬁcation model reported above was tested on 4557 medical reports
manually labeled by a certiﬁed cardiologist who was presented with the free-text and was required to choose
among the pre-speciﬁed classes. The classiﬁcation step recovered the true medical label with good results, the
macro F1 score achieved were: 0.729 for 1dAVb; 0.849 for RBBB; 0.838 for LBBB; 0.991 for SB; 0.993 for AF;
0.974 for ST.
3.3
Training and validation set annotation
To annotate the training and validation datasets, we used: i) the Uni-G statements and Minnesota codes
obtained by the Uni-G automatic analysis (automatic diagnosis); ii) automatic measurements provided by
the Uni-G software; and, iii) the text labels extracted from the expert text reports using the semi-supervised
methodology (medical diagnosis). Both the automatic and medical diagnosis are subject to errors: automatic
classiﬁcation has limited accuracy [4, 5, 3, 6] and text labels are subject both to errors of the practicing expert
cardiologists and the labeling methodology.
Hence, we combine the expert annotation with the automatic
analysis to improve the quality of the dataset. The following procedure is used for obtaining the ground truth
annotation:
1. We:
(a) Accept a diagnosis (consider an abnormality to be present) if both the expert and either the Uni-G
statement or the Minnesota code provided by the automatic analysis indicated the same abnormality.
(b) Reject a diagnosis (consider an abnormality to be absent) if only one automatic classiﬁer indicates
the abnormality in disagreement with both the doctor and the other automatic classiﬁer.
After this initial step, there are two scenarios where we still need to accept or reject diagnoses. They are:
i) both classiﬁers indicate the abnormality, but the expert does not; or ii) only the expert indicates the
abnormality, whereas none of the classiﬁers indicates anything.
2. We used the following rules to reject some of the remaining diagnoses:
(a) Diagnoses of ST where the heart rate was below 100 (8376 medical diagnoses and 2 automatic
diagnoses) were rejected.
(b) Diagnoses of SB where the heart rate was above 50 (7361 medical diagnoses and 16427 automatic
diagnosis) were rejected.
(c) Diagnoses of LBBB or RBBB where the duration of the QRS interval was below 115 ms (9313 medical
diagnoses for RBBB and 8260 for LBBB) were rejected.
(d) Diagnoses of 1dAVb where the duration of the PR interval was below 190 ms (3987 automatic
diagnoses) were rejected.
3. Then, using the sensitivity analysis of 100 manually reviewed exams per abnormality, we came up with
the following rules to accept some of the remaining diagnoses:
(a) For RBBB, d1AVb, SB and ST, we accepted all medical diagnoses. 26033, 13645, 12200 and 14604
diagnoses were accepted in this fashion, respectively.
(b) For AF, we required not only that the exam was classiﬁed by the doctors as true, but also that the
standard deviation of the NN intervals was higher than 646. 14604 diagnoses were accepted using
this rule.
According to the sensitivity analysis, the number of false positives that would be introduced by this
procedure was smaller than 3% of the total number of exams.
8


## Page 9


4. After this process, we were still left with 34512 exams where the corresponding diagnoses could neither
be accepted nor rejected. These were manually reviewed by medical students using the Telehealth ECG
diagnostic system, under the supervision of a certiﬁed cardiologist with experience in ECG interpretation.
The process of manually reviewing these ECGs took several months.
It should be stressed that information from previous medical reports and automatic measurements were used
only for obtaining the ground truth for training and validation sets and not on later stages of the DNN training.
3.4
Test set annotation
The dataset used for testing the DNN was also obtained from TNMG’s ECG system. It was independently
annotated by two certiﬁed cardiologists with experience in electrocardiography. The kappa coeﬃcients [46]
indicate the inter-rater agreement for the two cardiologist and are: 0.741 for 1dAVb; 0.955 for RBBB; 0.964 for
LBBB; 0.844 for SB; 0.831 for AF; 0.902 for ST. When they agreed, the common diagnosis was considered as
ground truth. In cases where there was any disagreement, a third senior specialist, aware of the annotations
from the other two, decided the diagnosis. The American Heart Association standardization [47] was used as
the guideline for the classiﬁcation.
It should be highlighted that the annotation was performed in an upgraded version of the TNMG software,
in which the automatic measurements obtained by the Uni-G program are presented to the specialist, that has
to choose the ECG diagnosis among a number of pre-speciﬁed classes of abnormalities. Thus, the diagnosis was
codiﬁed directly into our classes and there was no need to extract the label from a textual report, as it was
done for the training and validation sets.
3.5
Neural network architecture and training
We used a convolutional neural network similar to the residual network [23], but adapted to unidimensional
signals. This architecture allows deep neural networks to be eﬃciently trained by including skip connections.
We have adopted the modiﬁcation in the residual block proposed in [48], which place the skip connection in the
position displayed in Figure 3.
Figure 3: (DNN architecture) The uni-dimensional residual neural network architecture used for ECG clas-
siﬁcation.
All ECG recordings are re-sampled to a 400 Hz sampling rate. The ECG recordings, which have between 7
and 10 seconds, are zero-padded resulting in a signal with 4096 samples for each lead. This signal is the input
for the neural network.
The network consists of a convolutional layer (Conv) followed by 4 residual blocks with two convolutional
layers per block. The output of the last block is fed into a fully connected layer (Dense) with a sigmoid activation
function, σ, which was used because the classes are not mutually exclusive (i.e. two or more classes may occur
in the same exam). The output of each convolutional layer is rescaled using batch normalization, (BN), [49] and
fed into a rectiﬁed linear activation unit (ReLU). Dropout [50] is applied after the nonlinearity.
The convolutional layers have ﬁlter length 16, starting with 4096 samples and 64 ﬁlters for the ﬁrst layer
and residual block and increasing the number of ﬁlters by 64 every second residual block and subsampling by a
factor of 4 every residual block. Max Pooling [51] and convolutional layers with ﬁlter length 1 (1x1 Conv) are
included in the skip connections to make the dimensions match those from the signals in the main branch.
The average cross-entropy is minimized using the Adam optimizer [52] with default parameters and learning
rate lr = 0.001. The learning rate is reduced by a factor of 10 whenever the validation loss does not present
any improvement for 7 consecutive epochs. The neural network weights was initialized as in [53] and the bias
9


## Page 10


were initialized with zeros. The training runs for 50 epochs with the ﬁnal model being the one with the best
validation results during the optimization process.
3.6
Hyperparameter tuning
This ﬁnal architecture and conﬁguration of hyperparameters was obtained after approximately 30 iterations of
the procedure: i) ﬁnd the neural network weights in the training set; ii) check the performance in the validation
set; and, iii) manually chose new hyperparameters and architecture using insight from previous iterations. We
started this procedure from the set of hyperparameters and architecture used in [15].
It is also important
to highlight that the choice of architecture and hyperparameters was done together with improvements in the
dataset. Expert knowledge was used to take decision about how to incorporate, on the manual tuning procedure
, information about previous iteration that were evaluated on slightly diﬀerent versions of the dataset.
The hyperparameters were choosen among the following options: residual neural networks with {2, 4, 8, 16}
residual blocks, kernel size {8, 16, 32}, batch size {16, 32, 64}, initial learning rate {0.01, 0.001, 0.0001}, opti-
mization algorithms {SGD, ADAM}, activation functions {ReLU, ELU}, dropout rate {0, 0.5, 0.8}, number of
epochs without improvement in plateus between 5 and 10, that would result in a reduction in the learning rate
between 0.1 and 0.5. Besides that, we also tried to: i) use vectorcardiogram linear transformation to reduce
the dimensionality of the input; ii) include LSTM layer before convolutional layers; iii) use residual network
without the preactivation architecture proposed in [48]; iv) Use the convolutional architecture known as VGG;
v) swiching the order of activation and batch normalization layer.
3.7
Statistical and empirical analysis of test results
We computed the precision-recall curve to assess the model discrimination of each rhythm class. This curve
shows the relationship between precision (PPV) and recall (sensitivity), calculated using binary decision thresh-
olds for each rhythm class. For imbalanced classes, such as our test set, this plot is more informative than
the ROC plot [54]. For the remaining analyses we ﬁxed the DNN threshold to the value that maximized the
F1 score, which is the harmonic mean between precision and recall. The F1 score was chosen here due to its
robustness to class imbalance [54].
For the DNN with a ﬁxed threshold, and for the medical residents and students, we computed the precision,
the recall, the speciﬁcity, the F1 score and, also, the confusion matrix. This was done for each class. Boot-
strapping [26] was used to analyze the empirical distribution of each of the scores: we generated 1000 diﬀerent
sets by sampling with replacement from the test set, each set with the same number samples as in the test set,
and computed the precision, the recall, the speciﬁcity and the F1 score for each. The resulting distributions
are presented as a boxplot. We used the McNemar test [27] to compare the misclassiﬁcation distribution of
the DNN and the medical residents and students on the test set and the kappa coeﬃcient [46] to compare the
inter-rater agreement.
All the misclassiﬁed exams were reviewed by an experienced cardiologist and, after an interview with the
ECG reviewers, the errors were classiﬁed into: measurement errors, noise errors and unexplained errors (for the
DNN only) and conceptual and attention errors (for medical residents and students only).
We evaluate the F1 score for alternative scenarios where we use 90%-5%-5% splits of the 2,322,513 records.
With the splits ordered: randomly; by date; and, stratiﬁed by patients. The neural networks developed in these
alternative scenarios are evaluated on both the original test set (n=827) and on the additional test splits (last
5% split). The distribution of the performance in each scenario is computed by a bootstrap analysis (with 1000
and 200 samples, respectively) and the resulting boxplots are displayed in the supplementary material.
Data availability
The test dataset used in this study is openly available, and can be downloaded at
[https://doi.org/10.5281/zenodo.3625006] The weights of all deep neural network models we developed
for this paper are available at [https://doi.org/10.5281/zenodo.3625017]. Restrictions apply to the avail-
ability of the training set. Requests to access the training data will be considered on an individual basis by
the Telehealth Network of Minas Gerais. Any data use will be restricted to non-commercial research purposes,
and the data will only be made available on execution of appropriate data use agreements. The source data
underlying Supplementary Figures 1 and 2 are provided as a Source Data ﬁle.
Code availability
The code for training and evaluating the DNN model, and, also, for generating ﬁgures and tables in this paper,
is available at: [https://github.com/antonior92/automatic-ecg-diagnosis].
10


## Page 11


Research ethics statement
This study complies with all relevant ethical regulations. It was approved by the Research Ethics Committee
of the Universidade Federal de Minas Gerais, protocol 68496317.7.0000.5149.
Acknowledgments
This research was partly supported by the Brazilian Agencies CNPq, CAPES, and FAPEMIG, by projects
IATS, MASWeb, INCT-Cyber and Atmosphere, and by the Wallenberg AI, Autonomous Systems and Software
Program (WASP) funded by Knut and Alice Wallenberg Foundation. We also thank NVIDIA for awarding our
project with a Titan V GPU. ALR and WMJr are recipients of unrestricted research scholarships from CNPq;
AHR receives a scholarship from CAPES and CNPq; and, MHR and DMO receives a Google Latin America
Research Award scholarship. None of the funding agencies had any role in the design, analysis or interpretation
of the study.
Author contribution statement
A.H.R., M.H.R., G.P., D.M.O., P.R.G., J.A.C, M.P.S.F and A.L.R were responsible for the study design. A.L.R
conceived the project and acted as project leader. A.H.R., M.H.R and C.A. choose the architecture, implemented
and tuned the deep neural network. A.H.R did the statistical analysis of the test data and generated the ﬁgures
and tables.
M.H.R., G.M.M.P, J.A.C. were responsible for the preprocessing and annotating the datasets.
G.M.M.P was responsible for the error analysis.
D.M.O. implemented the semi-supervised methodology to
extract the text label. P.R.G. implemented the user interface used to generate the dataset. P.R.G. and M.P.S.F
were responsible for maintenance and extraction of the database. P.W.M., W.M.Jr., and T.B.S helped in the
interpretation of the data.
A.H.R., M.H.R, P.W.M., T.B.S. and A.L.R. contributed to the writing and all
authors revised it critically for important intellectual content. All authors read and approved the submitted
manuscript.
Competing interesting statement
The authors declare no competing interests.
References
[1] G. A. Roth et. al., “Global, regional, and national age-sex-speciﬁc mortality for 282 causes of death in 195
countries and territories, 1980–2017: A systematic analysis for the Global Burden of Disease Study 2017,”
The Lancet, vol. 392, pp. 1736–1788, Nov. 2018.
[2] J. L. Willems, C. Abreu-Lima, P. Arnaud, J. H. van Bemmel, C. Brohet, R. Degani, B. Denis, I. Graham,
G. van Herpen, and P. W. Macfarlane, “Testing the performance of ECG computer programs: The CSE
diagnostic pilot study,” Journal of Electrocardiology, vol. 20 Suppl, pp. 73–77, Oct. 1987.
[3] J. Schl¨apfer and H. J. Wellens, “Computer-Interpreted Electrocardiograms: Beneﬁts and Limitations,”
Journal of the American College of Cardiology, vol. 70, p. 1183, Aug. 2017.
[4] J. L. Willems, C. Abreu-Lima, P. Arnaud, J. H. van Bemmel, C. Brohet, R. Degani, B. Denis, J. Gehring,
I. Graham, and G. van Herpen, “The diagnostic performance of computer programs for the interpretation
of electrocardiograms,” The New England Journal of Medicine, vol. 325, pp. 1767–1773, Dec. 1991.
[5] A. P. Shah and S. A. Rubin, “Errors in the computerized electrocardiogram interpretation of cardiac
rhythm.,” Journal of Electrocardiology, vol. 40, no. 5, pp. 385–390, 2007 Sep-Oct.
[6] N. A. M. Estes, “Computerized interpretation of ECGs: Supplement not a substitute,” Circulation. Ar-
rhythmia and Electrophysiology, vol. 6, pp. 2–4, Feb. 2013.
[7] A. Krizhevsky, I. Sutskever, and G. E. Hinton, “Imagenet classiﬁcation with deep convolutional neural
networks,” in Advances in Neural Information Processing Systems, pp. 1097–1105, 2012.
[8] G. Hinton, L. Deng, D. Yu, G. E. Dahl, A. Mohamed, N. Jaitly, A. Senior, V. Vanhoucke, P. Nguyen,
T. N. Sainath, and B. Kingsbury, “Deep Neural Networks for Acoustic Modeling in Speech Recognition:
The Shared Views of Four Research Groups,” IEEE Signal Processing Magazine, vol. 29, pp. 82–97, Nov.
2012.
11


## Page 12


[9] W. W. Stead, “Clinical implications and challenges of artiﬁcial intelligence and deep learning,” JAMA,
vol. 320, pp. 1107–1108, Sept. 2018.
[10] Naylor C, “On the prospects for a (deep) learning health care system,” JAMA, vol. 320, pp. 1099–1100,
Sept. 2018.
[11] G. Hinton, “Deep learning—a technology with the potential to transform health care,” JAMA, vol. 320,
pp. 1101–1102, Sept. 2018.
[12] B. E. Bejnordi, M. Veta, P. Johannes van Diest, B. van Ginneken, N. Karssemeijer, G. Litjens, J. A. W. M.
van der Laak, and the CAMELYON16 Consortium, M. Hermsen, Q. F. Manson, M. Balkenhol, O. Geessink,
N. Stathonikos, M. C. van Dijk, P. Bult, F. Beca, A. H. Beck, D. Wang, A. Khosla, R. Gargeya, H. Irshad,
A. Zhong, Q. Dou, Q. Li, H. Chen, H.-J. Lin, P.-A. Heng, C. Haß, E. Bruni, Q. Wong, U. Halici, M. U.
¨Oner, R. Cetin-Atalay, M. Berseth, V. Khvatkov, A. Vylegzhanin, O. Kraus, M. Shaban, N. Rajpoot,
R. Awan, K. Sirinukunwattana, T. Qaiser, Y.-W. Tsang, D. Tellez, J. Annuscheit, P. Hufnagl, M. Valko-
nen, K. Kartasalo, L. Latonen, P. Ruusuvuori, K. Liimatainen, S. Albarqouni, B. Mungal, A. George,
S. Demirci, N. Navab, S. Watanabe, S. Seno, Y. Takenaka, H. Matsuda, H. Ahmady Phoulady, V. Kovalev,
A. Kalinovsky, V. Liauchuk, G. Bueno, M. M. Fernandez-Carrobles, I. Serrano, O. Deniz, D. Racoceanu,
and R. Venˆancio, “Diagnostic Assessment of Deep Learning Algorithms for Detection of Lymph Node
Metastases in Women With Breast Cancer,” JAMA, vol. 318, p. 2199, Dec. 2017.
[13] J. De Fauw, J. R. Ledsam, B. Romera-Paredes, S. Nikolov, N. Tomasev, S. Blackwell, H. Askham, X. Glo-
rot, B. O’Donoghue, D. Visentin, G. van den Driessche, B. Lakshminarayanan, C. Meyer, F. Mackinder,
S. Bouton, K. Ayoub, R. Chopra, D. King, A. Karthikesalingam, C. O. Hughes, R. Raine, J. Hughes,
D. A. Sim, C. Egan, A. Tufail, H. Montgomery, D. Hassabis, G. Rees, T. Back, P. T. Khaw, M. Suleyman,
J. Cornebise, P. A. Keane, and O. Ronneberger, “Clinically applicable deep learning for diagnosis and
referral in retinal disease,” Nature Medicine, vol. 24, pp. 1342–1350, Sept. 2018.
[14] E. J. Beck, W. Gill, and P. R. De Lay, “Protecting the conﬁdentiality and security of personal health
information in low- and middle-income countries in the era of SDGs and Big Data,” Global Health Action,
vol. 9, p. 32089, 2016.
[15] A. Y. Hannun, P. Rajpurkar, M. Haghpanahi, G. H. Tison, C. Bourn, M. P. Turakhia, and A. Y. Ng,
“Cardiologist-level arrhythmia detection and classiﬁcation in ambulatory electrocardiograms using a deep
neural network,” Nature Medicine, vol. 25, pp. 65–69, Jan. 2019.
[16] G. D. Cliﬀord, C. Liu, B. Moody, L.-w. H. Lehman, I. Silva, Q. Li, A. E. Johnson, and R. G. Mark,
“AF Classiﬁcation from a Short Single Lead ECG Recording: The PhysioNet/Computing in Cardiology
Challenge 2017,” Computing in Cardiology, vol. 44, Sept. 2017.
[17] J. Mant, D. A. Fitzmaurice, F. D. R. Hobbs, S. Jowett, E. T. Murray, R. Holder, M. Davies, and G. Y. H.
Lip, “Accuracy of diagnosing atrial ﬁbrillation on electrocardiogram by primary care practitioners and
interpretative diagnostic software: Analysis of data from screening for atrial ﬁbrillation in the elderly
(SAFE) trial,” BMJ (Clinical research ed.), vol. 335, p. 380, Aug. 2007.
[18] G. Veronese, F. Germini, S. Ingrassia, O. Cutuli, V. Donati, L. Bonacchini, M. Marcucci, A. Fabbri, and
Italian Society of Emergency Medicine (SIMEU), “Emergency physician accuracy in interpreting electro-
cardiograms with potential ST-segment elevation myocardial infarction: Is it enough?,” Acute Cardiac
Care, vol. 18, pp. 7–10, Mar. 2016.
[19] World Health Organization, Global Status Report on Noncommunicable Diseases 2014: Attaining the Nine
Global Noncommunicable Diseases Targets; a Shared Responsibility. Geneva: World Health Organization,
2014. OCLC: 907517003.
[20] R. Sassi, R. R. Bond, A. Cairns, D. D. Finlay, D. Guldenring, G. Libretti, L. Isola, M. Vaglio, R. Poeta,
M. Campana, C. Cuccia, and F. Badilini, “PDF-ECG in clinical practice: A model for long-term preser-
vation of digital 12-lead ECG data,” Journal of Electrocardiology, vol. 50, no. 6, pp. 776–780, 2017 Nov -
Dec.
[21] A. Lyon, A. Minchol´e, J. P. Mart´ınez, P. Laguna, and B. Rodriguez, “Computational techniques for ECG
analysis and interpretation in light of their contribution to medical advances,” Journal of the Royal Society
Interface, vol. 15, Jan. 2018.
[22] M. B. Alkmim, R. M. Figueira, M. S. Marcolino, C. S. Cardoso, M. Pena de Abreu, L. R. Cunha, D. F.
da Cunha, A. P. Antunes, A. G. d. A. Resende, E. S. Resende, and A. L. P. Ribeiro, “Improving patient
access to specialized health care: The Telehealth Network of Minas Gerais, Brazil,” Bulletin of the World
Health Organization, vol. 90, pp. 373–378, May 2012.
12


## Page 13


[23] K. He, X. Zhang, S. Ren, and J. Sun, “Deep Residual Learning for Image Recognition,” in Proceedings of
the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), pp. 770–778, 2016.
[24] S. Hong, M. Wu, Y. Zhou, Q. Wang, J. Shang, H. Li, and J. Xie, “ENCASE: An ENsemble ClASsiﬁEr for
ECG Classiﬁcation Using Expert Features and Deep Neural Networks,” in 2017 Computing in Cardiology
Conference, Sept. 2017.
[25] R. Kamaleswaran, R. Mahajan, and O. Akbilgic, “A robust deep convolutional neural network for the clas-
siﬁcation of abnormal cardiac rhythm using single lead electrocardiograms of variable length,” Physiological
Measurement, vol. 39, p. 035006, Mar. 2018.
[26] B. Efron and R. J. Tibshirani, An Introduction to the Bootstrap. CRC press, 1994.
[27] Q. McNemar, “Note on the sampling error of the diﬀerence between correlated proportions or percentages,”
Psychometrika, vol. 12, pp. 153–157, June 1947.
[28] S. H. Jambukia, V. K. Dabhi, and H. B. Prajapati, “Classiﬁcation of ECG signals using machine learning
techniques: A survey,” in Proceedings of the International Conference on Advances in Computer Engineer-
ing and Applications (ICACEA), pp. 714–721, IEEE, Mar. 2015.
[29] P. W. Macfarlane, B. Devine, and E. Clark, “The university of glasgow (Uni-G) ECG analysis program,”
in Computers in Cardiology, pp. 451–454, 2005.
[30] S. W. Smith, B. Walsh, K. Grauer, K. Wang, J. Rapin, J. Li, W. Fennell, and P. Taboulet, “A deep neural
network learning algorithm outperforms a conventional algorithm for emergency department electrocardio-
gram interpretation,” Journal of Electrocardiology, vol. 52, pp. 88–95, Jan. 2019.
[31] D. CUBANSKI, D. CYGANSKI, E. M. ANTMAN, and C. L. FELDMAN, “A Neural Network System
for Detection of Atrial Fibrillation in Ambulatory Electrocardiograms,” Journal of Cardiovascular Electro-
physiology, vol. 5, pp. 602–608, July 1994.
[32] R. K. Tripathy, A. Bhattacharyya, and R. B. Pachori, “A Novel Approach for Detection of Myocardial
Infarction From ECG Signals of Multiple Electrodes,” IEEE Sensors Journal, vol. 19, pp. 4509–4517, June
2019.
[33] J. Rubin, S. Parvaneh, A. Rahman, B. Conroy, and S. Babaeizadeh, “Densely Connected Convolutional
Networks and Signal Quality Analysis to Detect Atrial Fibrillation Using Short Single-Lead ECG Record-
ings,” arXiv:1710.05817, Oct. 2017.
[34] U. R. Acharya, H. Fujita, S. L. Oh, Y. Hagiwara, J. H. Tan, and M. Adam, “Application of deep convo-
lutional neural network for automated detection of myocardial infarction using ECG signals,” Information
Sciences, vol. 415-416, pp. 190–198, Nov. 2017.
[35] S. P. Shashikumar, A. J. Shah, G. D. Cliﬀord, and S. Nemati, “Detection of Paroxysmal Atrial Fibrillation
Using Attention-based Bidirectional Recurrent Neural Networks,” in Proceedings of the 24th ACM SIGKDD
International Conference on Knowledge Discovery & Data Mining, KDD ’18, (New York, NY, USA),
pp. 715–723, ACM, 2018.
[36] M. A. Rahhal, Y. Bazi, H. AlHichri, N. Alajlan, F. Melgani, and R. Yager, “Deep learning approach for
active classiﬁcation of electrocardiogram signals,” Information Sciences, vol. 345, pp. 340–354, June 2016.
[37] A. L. Goldberger, L. A. N. Amaral, L. Glass, J. M. Hausdorﬀ, P. C. Ivanov, R. G. Mark, J. E. Mietus,
G. B. Moody, C.-K. Peng, and H. E. Stanley, “PhysioBank, PhysioToolkit, and PhysioNet: Components
of a New Research Resource for Complex Physiologic Signals,” Circulation, vol. 101, June 2000.
[38] S. Goto, M. Kimura, Y. Katsumata, S. Goto, T. Kamatani, G. Ichihara, S. Ko, J. Sasaki, K. Fukuda, and
M. Sano, “Artiﬁcial intelligence to predict needs for urgent revascularization from 12-leads electrocardiog-
raphy in emergency patients,” PLOS ONE, vol. 14, p. e0210103, Jan. 2019.
[39] P. M. Rautaharju, B. Surawicz, and L. S. Gettes, “AHA/ACCF/HRS Recommendations for the Stan-
dardization and Interpretation of the Electrocardiogram: Part IV: The ST Segment, T and U Waves, and
the QT Interval A Scientiﬁc Statement From the American Heart Association Electrocardiography and
Arrhythmias Committee, Council on Clinical Cardiology; the American College of Cardiology Foundation;
and the Heart Rhythm Society Endorsed by the International Society for Computerized Electrocardiology,”
Journal of the American College of Cardiology, vol. 53, pp. 982–991, Mar. 2009.
13


## Page 14


[40] S. Luo and P. Johnston, “A review of electrocardiogram ﬁltering,” Journal of Electrocardiology, vol. 43,
pp. 486–496, Nov. 2010.
[41] B. R. Nascimento, L. C. C. Brant, B. C. A. Marino, L. G. Passaglia, and A. L. P. Ribeiro, “Implementing
myocardial infarction systems of care in low/middle-income countries,” Heart, vol. 105, p. 20, Jan. 2019.
[42] P. Macfarlane, B. Devine, S. Latif, S. McLaughlin, D. Shoat, and M. Watts, “Methodology of ECG in-
terpretation in the Glasgow program,” Methods of information in medicine, vol. 29, no. 04, pp. 354–361,
1990.
[43] P. W. Macfarlane and S. Latif, “Automated serial ECG comparison based on the Minnesota code,” Journal
of Electrocardiology, vol. 29, pp. 29–34, 1996.
[44] R. J. Prineas, R. S. Crow, and Z.-M. Zhang, The Minnesota Code Manual of Electrocardiographic Findings.
Springer Science & Business Media, 2009.
[45] A. Veloso, W. Meira Jr, and M. J. Zaki, “Lazy Associative Classiﬁcation,” in Proceedingsof the 6th Inter-
national Conference on Data Mining (ICDM), pp. 645–654, 2006.
[46] J. Cohen, “A Coeﬃcient of Agreement for Nominal Scales,” Educational and Psychological Measurement,
vol. 20, pp. 37–46, Apr. 1960.
[47] P. Kligﬁeld, L. S. Gettes, J. J. Bailey, R. Childers, B. J. Deal, E. W. Hancock, G. van Herpen, J. A.
Kors, P. Macfarlane, D. M. Mirvis, O. Pahlm, P. Rautaharju, and G. S. Wagner, “Recommendations for
the Standardization and Interpretation of the Electrocardiogram,” Journal of the American College of
Cardiology, vol. 49, p. 1109, Mar. 2007.
[48] K. He, X. Zhang, S. Ren, and J. Sun, “Identity Mappings in Deep Residual Networks,” in Computer Vision
– ECCV 2016 (B. Leibe, J. Matas, N. Sebe, and M. Welling, eds.), pp. 630–645, Springer International
Publishing, 2016.
[49] S. Ioﬀe and C. Szegedy, “Batch Normalization: Accelerating Deep Network Training by Reducing Internal
Covariate Shift,” in Proceedings of the 32nd International Conference on Machine Learning, pp. 448–456,
PMLR, June 2015.
[50] N. Srivastava, G. E. Hinton, A. Krizhevsky, I. Sutskever, and R. Salakhutdinov, “Dropout: A simple
way to prevent neural networks from overﬁtting.,” Journal of Machine Learning Research, vol. 15, no. 1,
pp. 1929–1958, 2014.
[51] D. Hutchison, T. Kanade, J. Kittler, J. M. Kleinberg, F. Mattern, J. C. Mitchell, M. Naor, O. Nierstrasz,
C. Pandu Rangan, B. Steﬀen, M. Sudan, D. Terzopoulos, D. Tygar, M. Y. Vardi, G. Weikum, D. Scherer,
A. M¨uller, and S. Behnke, “Evaluation of Pooling Operations in Convolutional Architectures for Object
Recognition,” in Artiﬁcial Neural Networks – ICANN 2010 (K. Diamantaras, W. Duch, and L. S. Iliadis,
eds.), vol. 6354, pp. 92–101, Springer Berlin Heidelberg, 2010.
[52] D. P. Kingma and J. Ba, “Adam: A Method for Stochastic Optimization,” in Proceedings of the 3rd
International Conference for Learning Representations (ICLR), Dec. 2014.
[53] K. He, X. Zhang, S. Ren, and J. Sun, “Delving deep into rectiﬁers: Surpassing human-level performance
on imagenet classiﬁcation,” in Proceedings of the IEEE International Conference on Computer Vision,
pp. 1026–1034, 2015.
[54] T. Saito and M. Rehmsmeier, “The Precision-Recall Plot Is More Informative than the ROC Plot When
Evaluating Binary Classiﬁers on Imbalanced Datasets,” PLOS ONE, vol. 10, p. e0118432, Mar. 2015.
14


## Page 15


Supplementary Information
predicted label
DNN
cardio.
emerg.
stud.
true label
not present
present
not present
present
not present
present
not present
present
1dAVb
not present
795
4
797
2
786
13
782
17
present
2
26
9
19
5
23
2
26
RBBB
not present
789
4
788
5
792
1
790
3
present
0
34
1
33
8
26
2
32
LBBB
not present
797
0
797
0
796
1
795
2
present
0
30
3
27
4
26
3
27
SB
not present
808
3
808
3
808
3
807
4
present
1
15
1
15
2
14
4
12
AF
not present
814
0
811
3
812
2
805
9
present
3
10
3
10
5
8
1
12
ST
not present
788
2
789
1
788
2
787
3
present
1
36
7
30
2
35
6
31
Supplementary Table 1: (Confusion matrices) Show the absolute number of: i) false posives; ii) false nega-
tives; iii) true positives; and, iv) true negatives, for each abnormality on the test set.
1dAVb
RBBB
LBBB
SB
AF
ST
DNN vs cardio.
0.656
0.917
0.945
0.830
0.780
0.864
DNN vs emerg.
0.684
0.792
0.909
0.796
0.595
0.930
DNN vs stud.
0.642
0.928
0.912
0.760
0.574
0.855
cardio. vs emerg.
0.656
0.824
0.923
0.912
0.515
0.847
cardio. vs stud.
0.612
0.871
0.889
0.880
0.700
0.792
emerg. vs stud.
0.615
0.799
0.852
0.907
0.508
0.897
(a)
1dAVb
RBBB
LBBB
SB
AF
ST
DNN vs Cert. cardiol. 1
0.758
0.928
0.964
0.770
0.696
0.847
DNN vs Certif. cardiol. 2
0.852
0.942
1.000
0.770
0.746
0.884
Cert. cardiol. 1 vs Certif. cardiol. 2
0.741
0.955
0.964
0.844
0.831
0.902
(b)
Supplementary Table 2: (Kappa coeﬃcients) Show the Kappa scores measuring the inter-rater agreement
on the test set. In (a), we compare the DNN, the medical residents and the students two at a time. In (b),
we compare the DNN, and the certiﬁed cardiologists that annotated the test set (certif.
cardiol.). If the
raters are in complete agreement then it is equal to 1. If there is no agreement among the raters other than
what would be expected by chance it is equal to 0.
15


## Page 16


1dAVb
RBBB
LBBB
SB
AF
ST
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1.0
(a) Precision (PPV)
1dAVb
RBBB
LBBB
SB
AF
ST
0.2
0.4
0.6
0.8
1.0
(b) Recall (Sensitivity)
1dAVb
RBBB
LBBB
SB
AF
ST
0.96
0.97
0.98
0.99
1.00
(c) Speciﬁcity
1dAVb
RBBB
LBBB
SB
AF
ST
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1.0
DNN
cardio.
emerg.
stud.
(d) F1 score
Supplementary Figure 1: (Bootstrapped scores) Display boxplots of empirical distribution of precision,
recall, speciﬁcity and F1 score on the test set. Sampling with replacement (i.e. bootstrapping) from the test
set was used to generate n = 1000 samples. The results are given for the DNN, the medical residents and
students. Source data are provided as a Source Data ﬁle. The boxplots should be read as follows: the central
line correspond to the median value of the empirical distribution, the box region correspond to the range of
values between the ﬁrst and third quartile (also knonw as interquartile range or IQR), the whiskers extend from
1.5 IQR below and above the ﬁrsth and third quartiles, values outside of that range are considered outliers and
show as diamonds.
1dAVb
RBBB
LBBB
SB
AF
ST
DNN vs cardio.
0.225
0.414
0.083
1.000
0.180
0.096
DNN vs emerg.
0.007
0.166
0.025
0.705
0.157
0.655
DNN vs stud.
0.009
0.655
0.025
0.157
0.052
0.058
cardio. vs emerg.
0.108
0.366
0.317
0.564
0.763
0.206
cardio. vs stud.
0.102
0.739
0.414
0.046
0.206
0.782
emerg. vs stud.
0.853
0.248
1.000
0.083
0.439
0.059
Supplementary Table 3: (McNemar test) Display the p-values for the McNemar test comparing the misclassi-
ﬁcation on the test set. The DNN, the medical residents and the students were compared two at a time. Entries
with statistical signiﬁcance (with 0.05 signiﬁcance level) are displayed in boldface.
16


## Page 17


1dAVb
SB
AF
ST
RBBB
LBBB
0.4
0.5
0.6
0.7
0.8
0.9
1.0
F1 score
random
by date
by patient
original DNN
(a) original test set
1dAVb
SB
AF
ST
RBBB
LBBB
0.4
0.5
0.6
0.7
0.8
0.9
1.0
F1 score
random
by date
by patient
(b) secondary test set (last 5% split)
Supplementary Figure 2: (Bootstrapped scores for alternative splits) Boxplots for the bootstrapped F1 scores for the
DNN using alternative 90%-5%-5% splits for training, validation and as a secondary test set. For the splits ordered: randomly; by
date; and, stratiﬁed by patients. In all cases, the performance is evaluated on: (a) the original test set for n = 1000 bootstraped
samples; and, on (b) the secondary test set (last 5% split) for n = 200 bootstraped samples. On (a), we also present the original
DNN performance for comparison, which was developed using a 98%-2% split. The performance gap between (a) and (b) is due to
the diﬀerence in the gold standard. The secondary test set obtained from the last 5% has a less accurate annotation, since it has
not been annotated by multiple doctors and it uses natural language processing to extract the diagnosis from a written report. This
extra noise result in worse F1 score in (b) when compared with (a). On the other hand, the secondary 5% test split contain more
than 100,000 records, which yield more stable performance in the bootstrap analysis, with more concentrated empirical distributions
for the F1 score. Both RBBB and LBBB (highlighted on the plot) present on (b) a statistically signiﬁcant diﬀerence between the
performance of the split ordered by date and the other two splits, that diﬀerence is due to some changes in personal that took
place in the the Telehealth center, that aﬀected the period used in the test set (10-2016 to 06-2017), resulting in lower annotation
quality. A certiﬁed cardiologist reviewed cases for which the neural network have been considered wrong when compared to the
gold standard from the 5% split collected from 10-2016 to 06-2017, 100 supposedly wrong RBBB and 100 supposedly wrong LBBB.
The certiﬁed cardiologist reported that the neural network is actually correct, respectively, 86% and 83% percent of the cases. This
analysis show the importance of a test set with a good annotation quality to obtain reliable estimation of the DNN performance.
And, also, that periods of lower annotation quality in the dataset are overcome by a very high number of examples. Source data
are provided as a Source Data ﬁle. See Supplementary Figure 1 caption for the deﬁnition of all elements in the boxplot.
False
True
SB
0
25
50
75
100
125
150
175
200
heart rate
correct prediction
False
True
(a)
False
True
ST
0
25
50
75
100
125
150
175
200
heart rate
correct prediction
False
True
(b)
Supplementary Figure 3: (Heart rate vs DNN predictions) Heart rate measured by the Uni-G software for
samples in the test set is given on the y-axis. The color indicates if the DNN make the correct prediction or
not. The x-axis separates the dataset accordingly to the presence of: SB in (a); and, ST in (b). A horizontal
line show the threshold of 50 bpm for SB in (a); and, of 100 bpm for ST in (b), which delimit the consensus
deﬁnition of SB and ST. Notice that most exams for which the neural network fails to get the correct result
are very close to this threshold line and are the borderline cases we mentioned in the discussion. It should be
highlighted that this automatic measurement system is not perfect, and measurements that may indicate some
of the conditions do not necessarily agree with our board of cardiologist (e.g. there are exams with heart rate
above 100 acording to Uni-G that are not classiﬁed by our cardiologist as ST).
17

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1904_01949v2_automatic_diagnosis_of_the_12_lead_ecg_using_a_deep_neural_network
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1904_01949V2_AUTOMATIC_DIAGNOSIS_OF_THE_12_LEAD_ECG_USING_A_DEEP_NEURAL_NETWORK.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

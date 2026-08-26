---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1810.10664v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1810.10664v1_Automated_Process_Incorporating_Machine_Learning_Segmentation_and_Correlation_of

> Source: 1810.10664v1_Automated_Process_Incorporating_Machine_Learning_Segmentation_and_Correlation_of.pdf

> Pages: 9

---


## Page 1


JOURNAL OF BIOMEDICAL AND HEALTH INFORMATICS
1
Automated Process Incorporating Machine
Learning Segmentation and Correlation of Oral
Diseases with Systemic Health
Gregory Yauney, Aman Rana, Lawrence C. Wong, Perikumar Javia, Ali Muftu and Pratik Shah†
Abstract— Imaging ﬂuorescent disease biomarkers in
tissues and skin is a non-invasive method to screen for
health conditions. We report an automated process that
combines intraoral ﬂuorescent porphyrin biomarker imag-
ing, clinical examinations and machine learning for correla-
tion of systemic health conditions with periodontal disease.
1215 intraoral ﬂuorescent images, from 284 consenting
adults aged 18-90, were analyzed using a machine learning
classiﬁer that can segment periodontal inﬂammation. The
classiﬁer achieved an AUC of 0.677 with precision and
recall of 0.271 and 0.429, respectively, indicating a learned
association between disease signatures in collected im-
ages. Periodontal diseases were more prevalent among
males (p=0.0012) and older subjects (p=0.0224) in the
screened population. Physicians independently examined
the collected images, assigning localized modiﬁed gingival
indices (MGIs). MGIs and periodontal disease were then
cross-correlated with responses to a medical history ques-
tionnaire, blood pressure and body mass index measure-
ments, and optic nerve, tympanic membrane, neurological,
and cardiac rhythm imaging examinations. Gingivitis and
early periodontal disease were associated with subjects di-
agnosed with optic nerve abnormalities (p <0.0001) in their
retinal scans. We also report signiﬁcant co-occurrences
of periodontal disease in subjects reporting swollen joints
(p=0.0422) and a family history of eye disease (p=0.0337).
These results indicate cross-correlation of poor periodon-
tal health with systemic health outcomes and stress the
importance of oral health screenings at the primary care
level. Our screening process and analysis method, using
images and machine learning, can be generalized for auto-
mated diagnoses and systemic health screenings for other
diseases.
Index Terms— machine learning, segmentation, imaging,
health informatics
I. INTRODUCTION
Biomarkers provide a fast, accurate, and non-invasive way
to diagnose several diseases and can be used for prognostic
screening along with clinical response monitoring. Gingivitis
is the inﬂammation of gingiva around the tooth, making the
Manuscript received September 25, 2018.
G. Yauney, A. Rana, P. Javia and Pratik Shah are with MIT Media
Lab, Massachusetts Institute of Technology, Cambridge, MA, USA e-
mail: {gyauney,arana,pjavia,pratiks}@media.mit.edu
L. C. Wong and A. Muftu are with School of Dental Medicine,
Tufts
University,
Boston,
MA,
USA
e-mail:
{lawrence.wong,
ali.muftu}@tufts.edu
†Corresponding author: pratiks@media.mit.edu
gums sensitive and likely to bleed. Gingivitis can progress and
lead to periodontitis, with severe inﬂammation and infections
in the surrounding structures of the teeth. Periodontal disease
is a major cause of tooth loss in adults, due to soft tissue
inﬂammation and bone loss. Periodontal disease has been
found to be an important indicator of oral-systemic health [1]
and has been linked to cardiovascular disease, osteoporosis,
and diabetes [2], [3]. Clinical assessment of periodontal dis-
ease is usually done using visual examinations and probing.
Standard diagnostic practices of alveolar bone height and
clinical attachment levels, while helpful, do not account for
patient-to-patient variation or identify disease progression risk
[2], [4].
Biomarkers indicative of periodontal and gingival disease
can be detected from crevicular ﬂuid using biochemical assays,
but doing so is impractical in many clinical settings. Gingivitis
results in an increased blood ﬂow around the inﬂamed gingiva,
leading in turn to increased red ﬂuorescence (650 nm) from
porphyrin in the surrounding vasculature. Gums when illumi-
nated with a blue light (405-450 nm), ﬂuoresce in the presence
of porphyrin from hemoglobin in the blood due to inﬂamma-
tion and microbial bioﬁlms [5]. Trained dental experts, without
the aid of porphyrin ﬂuorescence, can also discern periodontal
diseases and gingivitis in whitelight images. Computer vision,
machine learning, and deep neural networks can perform
automated and accurate diagnoses of several diseases from
images [6]. We have previously described an automated system
that performs pixel-wise segmentation of the inﬂamed gingiva
to detect gingivitis and periodontal disease using ﬂuorescent
images acquired by an FDA-approved intraoral camera [7].
In this study, we present a new medical imaging and in-
formatics based process for demonstrating the generalizability
of automated oral health screenings and cross correlations of
oral-systemic health (Figure 1). Intraoral ﬂuorescent images
were collected from 284 consenting adults and analyzed for
periodontal diseases using our previously described machine
learning classiﬁer. Segmentation results from the classiﬁer
were compared with localized labels provided by dentists
for the same images. We then analyzed co-occurrence rates
between subjects’ MGIs, a measure of periodontal health
provided by expert dentists, and three sources of screenings:
1) a self-reported medical history questionnaire, 2) a group of
routine health screenings: blood pressure (BP) and body mass
index (BMI) measurements, and 3) a group of technology-
arXiv:1810.10664v1  [cs.LG]  25 Oct 2018


## Page 2


2
JOURNAL OF BIOMEDICAL AND HEALTH INFORMATICS
Medical history 
questionnaire
Routine health screenings 
Technology-enabled 
screenings
Intraoral ﬂuorescent 
imaging
Segmentation 
classiﬁer
Localized annotation
Oral-systemic 
cross-correlations
Patients
Remote annotation
Patient summaries
Fig. 1: The process starts with non-invasive imaging and
health screening in an out-patient setting. Expert annotations
of localized and patient-level condition signatures were used
to evaluate a segmentation classiﬁer and oral-systemic cross-
correlations. Routine health screenings include blood pressure
and body mass index measurements, and technology-enabled
screenings consist of imaging examinations of blood oxygena-
tion levels, optic nerve, tympanic membrane, coordination, and
gait.
enabled screenings (TES): single-lead echocardiogram (ECG)
arrhythmias, tympanic membrane disorders, blood oxygena-
tion levels, optic nerve disorders, and neurological ﬁtness
exams conducted using FDA approved devices. Higher MGIs
were signiﬁcantly correlated with males, older age, swollen
joints, and a family history of eye disease. Gingivitis was sig-
niﬁcantly correlated with optic nerve exam abnormalities. Our
automated process and results thus indicate that periodontal
health is an important aspect of systemic and overall subject
health.
II. RELATED WORK
A. Convolutional neural networks
Deep neural networks allow for representation learning and
complex feature extraction. Convolutional neural networks
(CNNs) require fewer total parameters because matrix multi-
plication is replaced by convolution, with each neuron sharing
weights. The convolutional layers are followed by non-linear
functions which are in turn generally followed by pooling
layers. The initial layers extract spatial features, and pooling
provides translational invariance, making CNNs robust for
visual classiﬁcation tasks [8].
B. Medical image segmentation and disease diagnosis
process
CNNs are widely used for automatic detection and seg-
mentation of various diseases in medical images. CNNs have
recently been used to segment lesions from computed tomog-
raphy images and magnetic resonance imaging of the brain
and liver [9]. Recent work on medical image segmentation
includes using a CNN for classiﬁcation of cancerous oral
cavity regions and classiﬁcation in quantitative light-induced
images [10], [11]. CNNs have also been used explicitly for
gingival health tasks with intraoral whitelight and ﬂuorescence
images, such as full-image segmentation of gingivitis and
patch-based segmentation of plaque and periodontal diseases
[7], [12].
Medical imaging, especially low-cost imaging provided by
mobile phones and specialized imaging devices, provides non-
invasive measures of patient health and has been used for
applications of remote diagnosis in addition to the segmen-
tation work described above [13], [14]. Past work on remote
and automated diagnosis of medical images did not afford a
holistic consideration of the systemic health of patients whose
images were analyzed [15]. Automated processes integrating
imaging and remote annotation informatics for diagnosis and
systemic health analysis have recently been described by us
[16]. These processes provide opportunities for gathering the
data required to build accurate machine learning models for
disease segmentation while also providing the ability to link
systemic health of the patients to images.
C. Periodontal health epidemiology
Periodontal disease is correlated with coronary heart disease
and peripheral vascular disease in American adults [17], [18].
The former was especially more likely in young adult males
than in other age and gender cohorts [17]. Signiﬁcant links
between periodontal disease and diabetes, both types I and
II, were found in multiple studies of thousands of Pima
Indians of the Gila River Indian Community in Arizona, US,
and in Danish men [19]. Periodontal disease was correlated
with obesity in Japanese adults irrespective of age and, in
a sample of over ten thousand American adults, in younger
American adults. In the same study, low BMI was signif-
icantly associated with decreased prevalence of periodontal
disease among young American adults [20]. Separate studies
of thousands of American adults found that recent tooth loss
was signiﬁcantly correlated with primary open-angle glaucoma
and that periodontal disease was signiﬁcantly correlated with
macular degeneration in adults under the age of 60 [21], [22].
In various populations in India, periodontal disease has been
found to be highly prevalent and signiﬁcantly correlated with
older age, coronary artery disease, tobacco use, smoking, and
lower socioeconomic status [23], [24]. However, all the above
studies relied on clinical examinations by human experts and
none used intraoral images, TES, or machine learning for
diagnosing periodontal diseases to detect novel oral-systemic
cross correlations.
III. METHODS
A. Data acquisition
Data from 284 consenting adults aged 18-90 in Maharash-
tra, India, was used for this study. The Mahatma Gandhi
Vidyamandir Karmaveer Bhausaheb Hiray Dental College &
Hospital institutional ethics committee reviewed and approved
protocol MGVKBHDC/15-16/571 for clinical data collec-
tion. De-identiﬁed data was transferred and analyzed at the
Massachusetts Institute of Technology (MIT) in Cambridge,
MA, according to MIT Committee on the Use of Humans
as Experimental Subjects approval for protocol 1512338971.
SOPROCARE (SOPRO Acteon Imaging, France) was used for
intraoral imaging using white light and 405nm light-emitting
diodes. Optic nerve, ECG, tympanic membrane, oxygen sat-
uration, gait and coordination exams and BMI and blood
pressure measurements recorded with FDA-approved devices
were used for oral-systemic cross correlations [16].


## Page 3


YAUNEY et al.: AUTOMATED PROCESS INCORPORATING MACHINE LEARNING SEGMENTATION AND CORRELATION OF ORAL DISEASES WITH SYSTEMIC
HEALTH
3
B. Data preprocessing and clinical examinations
De-identiﬁed data assigned to unique subject identiﬁers
was split into separate pools consisting of optic nerve, tym-
panic membrane, periodontal, and neurological images for
all study participants. BMI and blood pressure are routinely
measured by most primary care providers and have been
collectively annotated as routine health screenings throughout
this study. Other imaging and smartphone-based tests have
been designated TES methods. Routine health screenings and
responses to medical questionnaires were grouped together
for computational analyses. For BMI, numbers less than 19
were labeled low, between 19 and 25 were characterized
as normal, and 25 and above were considered high (Panel,
1998). For blood pressure, systolic pressure below 90 mmHg
or diastolic pressure below 60 mmHg was considered low,
systolic pressure between 90 and 140 mmHg and diastolic
pressure between 60 and 90 mmHg was labeled normal, and
systolic pressure above 140 mmHg or diastolic pressure above
90 mmHg was labeled high [25]. Blood oxygen levels of 90%
or less were annotated low.
Optic nerve, tympanic membrane, gait, and coordination
images captured in TES were categorized by patient ID and
TES examination and displayed directly to expert physicians
via a web-based examination portal [7], [16]. Annotators were
able to mark speciﬁc clinical features that were present in each
video, and a condition was kept if it was noted by a majority
of experts [16]. The outputs from the AliveCor mobile app
were readily used as annotations for ECG tests because they
were labeled ‘Normal’ or ‘Possible atrial ﬁbrillation’ [26].
C. Periodontal examinations using images
Using the same web-based examination portal, dental ex-
perts examined de-identiﬁed intraoral ﬂuorescence images and
annotated periodontal disease on the gingival margin and left
and right papillae. The experts also assigned each image
a modiﬁed gingival index (MGI) ranging from 0 (healthy
gingiva) to 5 (severe periodontal disease) [27]. A majority
MGI was calculated for each subject. For subjects with no
clear majority, the greater tied MGI was taken so as to not
understate the prevalence of periodontal disease.
D. Disease segmentation
In a previously described study we used 405 (from a
total 1215) intraoral images for training and validation of
a segmentation classiﬁer [7]. The model accepts an RGB
image of size 640 × 480 × 3 and outputs a binary mask
indicating the locations of periodontal disease. In this study
the trained model was used to segment periodontal disease
in additional 810 images. Ground truth segmentation masks
were prepared by spatially bounding the locations of all
expert annotations for all 810 images. The bounded region
was thresholded based on the augmented color signature of
periodontal disease to capture ﬁner signatures of inﬂammation.
We evaluated classiﬁer performance by calculating standard
measures like true and false positive rates, precision, recall,
and mean intersection over union (IOU).
E. Cross-correlations and statistical methods
Since periodontal disease segmentations on images and
localized annotations have not been clinically used to as-
sign MGIs and are too ﬁne-grained, we used expert-assigned
MGIs for correlation of imaging results with systemic health
outcomes. We investigated correlations between periodontal
health MGIs provided by expert dentists and gender and age
across the dataset. Correlations between periodontal health
MGIs and other conditions identiﬁed by 1) the medical history
questionnaire, 2) routine health screenings, and 3) TES tests
were also analyzed. We ﬁrst calculated the numbers of patients
with all possible co-occurrences of each MGI and condition
identiﬁed by the three groups of screenings. We then com-
pared incidence rates between each co-occurrence and between
genders and age cohorts. Fisher’s exact test was used to
establish statistical signiﬁcance when comparing between two
populations with unequal numbers of subjects and possibly
unequal means and variances, and we accept as signiﬁcant all
comparisons with a p-value less than 0.05. For example, to
ﬁnd that subjects with an MGI of 4 are more likely to also
have reported swollen joints than subjects with other MGIs,
we calculate two ratios: the number of subjects who reported
swollen joints and have an MGI of 4 (14) over the number of
subjects with an MGI of 4 (30), and the number of subjects
who reported swollen joints and have an MGI that is not 4 (56)
over the number of subjects with an MGI that is not 4 (254).
Comparing the two ratios with Fisher’s exact test yields a p-
value of 0.0422, and we conclude the correlation is signiﬁcant.
We separately investigated the extent to which automated MGI
prediction could provide an end-to-end pipeline for MGI and
correlated systemic health prediction.
IV. RESULTS
A. Segmentation of periodontal disease in subjects by
machine learning classiﬁer
The classiﬁer was tested on 810 images, producing a true
positive rate of 0.429 and a false positive rate of 0.075
when individual predictions for all pixels in each image are
considered. The area under the resulting receiver operating
characteristic curve was 0.677, interpretable as a 67.7% chance
that a pixel labeled with periodontal disease would be more
likely to be predicted as periodontal disease than a pixel
labeled as healthy. Precision was 0.271. Figure 2 shows these
values in the form of a receiver operating characteristic (ROC)
curve and a precision-recall curve, both in context with base-
line random chance, which the classiﬁer outperforms. Mean
intersection over union (IOU) was 0.1710 ± 0.1544 when aver-
aged across images. The classiﬁer robustly segments numerous
conﬁgurations of gingival and periodontal disease (Figure 3,
columns i-iv). When segmenting an image of healthy gingiva,
the classiﬁer predicts a commensurately smaller disease extent
though it does produce some false positives (Figure 3, column
v). On rare occasions, the classiﬁer understates the extent of
disease (Figure 3, column vi).


## Page 4


4
JOURNAL OF BIOMEDICAL AND HEALTH INFORMATICS
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1.0
False positive rate
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1.0
True positive rate
(a)
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1.0
Recall
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1.0
Precision
(b)
Fig. 2: The trained segmentation classiﬁer, shown as a solid
line, outperforms random chance, shown as a dashed line,
on 810 intraoral images. The classiﬁer is marked in both
graphs. (a) Receiver operating characteristic (ROC) curve. The
marked point occurs at a false positive rate of 0.075 and a true
positive rate of 0.429. Area under the ROC curve is 0.677. (b)
Precision-recall curve. The marked point occurs at a recall of
0.429 and a precision of 0.271.
B. Periodontal health of subjects using MGI scores
Table 1 shows summary MGI scores for all 284 subjects,
aggregated across all images from each subject. 42.3% of
subjects had an aggregated MGI of 2 and another 32.4% had an
MGI of 3, indicating a moderate presence of gingival diseases
in the majority of subjects. Two subjects were deemed to be
in good gingival health with an MGI of 0. Females were
more likely than males to have an MGI of 2 (p=0.0389), and
(A)
(B)
(C)
(D)
(i)
(ii)
(iii)
(iv)
(v)
(vi)
Fig. 3: Representative segmentation inputs and results. Row
(A): intraoral ﬂuorescence images captured during screening;
row (B): corresponding ground truth signatures of periodontal
disease constructed from localized expert annotation; row (C):
corresponding predictions from the segmentation classiﬁer;
row (D): visualization of localized prediction errors. Each
column contains an image from a different subject.
males were more likely than females to have an MGI of 3
(p=0.0012). This indicates that males in our dataset tended
to have higher MGIs and periodontal diseases than females.
Higher MGIs were correlated with middle-aged (p=0.0013,
p=0.0213) and old-aged (p=0.0224, p=0.0004) cohorts.
C. Periodontal health correlations: medical history
questionnaire
Table 2 shows the number of subjects with a particular MGI
score and who answered yes to each question on the medical
history questionnaire. Subjects with an MGI of 4 were more
likely to report swollen joints (p=0.0422) and a family history
of eye disease (p=0.0337).
Supplementary Table I shows the number of subjects of
each gender with a particular MGI and who answered yes to
each question on the medical history questionnaire. Males and
females in our study both showed prevalence of periodontal
diseases. Among individual genders, females with an MGI of
4 were more likely than females with other MGIs to report
swollen joints (p=0.0195), difﬁculty hearing (p=0.0245), and
difﬁculty walking (p=0.0193). Males with an MGI of 4 were
more likely than males with other MGIs to report a family
history of eye diseases (p=0.0163).
Supplementary Table II shows the number of subjects of
Adolescent (18-19)
Young adult (20-39)
Middle age (40-64)
Old age (65-90)
All ages
MGI
Female
Male
Total
Female
Male
Total
Female
Male
Total
Female
Male
Total
Female
Male
Total
0
1
0
1
0
0
0
0
1
1
0
0
0
1
1
2
1
9
4
13
10
5
15
3
5
8
0
3
3
22
17
39
2
20
8
28
17
23
40
19
21
40
2
10
12
58
62
120
3
3
7
10
10
21
31
9
24
33
3
15
18
25
67
92
4
0
0
0
0
5
5
8
8
16
2
7
9
10
20
30
5
0
0
0
0
0
0
1
0
1
0
0
0
1
0
1
I. The distribution of patient-level modiﬁed gingival indices (MGIs) split by gender and age cohort. The majority of subjects
(74.6%) had MGIs of 2 or 3, indicating prevalent gingival diseases.


## Page 5


YAUNEY et al.: AUTOMATED PROCESS INCORPORATING MACHINE LEARNING SEGMENTATION AND CORRELATION OF ORAL DISEASES WITH SYSTEMIC
HEALTH
5
MGI
No. patients
Glasses
Dental
Swollen joints
Hearing
FH diabetes
FH high BP
Tobacco
Difﬁculty walking
High BP
Diabetes
High BP Rx
Asthma
Smoking
FH cardiac
Cardiac Rx
Cardiovascular
Low BP
FH stroke
FH eye disease
Heart attack
Coronary bypass
Drinking
Eye treatment
Memory loss
Ear treatment
FH ear disease
0
2
1 (50.0)
0 (0)
0 (0)
0 (0)
1 (50.0)
0 (0)
1 (50.0)
0 (0)
0 (0)
1 (50.0)
0 (0)
0 (0)
0 (0)
0 (0)
0 (0)
0 (0)
0 (0)
0 (0)
0 (0)
0 (0)
0 (0)
0 (0)
0 (0)
0 (0)
0 (0)
0 (0)
1
39
23 (59.0)
11 (28.2)
4 (10.3)
7 (18.0)
13 (33.3)
7 (18.0)
1 (2.6)
3 (7.7)
1 (2.6)
1 (2.3)
1 (2.3)
3 (7.7)
1 (2.3)
3 (7.7)
0 (0)
0 (0)
0 (0)
1 (2.6)
0 (0)
0 (0)
1 (2.6)
0 (0)
0 (0)
0 (0)
1 (2.6)
0 (0)
2
120
59 (49.2)
27 (22.5)
23 (19.2)
17 (14.2)
30 (25.0)
22 (18.3)
7 (5.8)
8 (6.7)
6 (5.0)
8 (6.7)
5 (4.2)
5 (4.2)
3 (2.5)
2 (1.7)
2 (1.7)
1 (0.8)
1 (0.8)
2 (1.7)
0 (0)
0 (0)
0 (0)
1 (0.8)
0 (0)
0 (0)
1 (0.8)
0 (0)
3
92
43 (46.7)
25 (27.2)
29 (31.5)
22 (23.9)
12 (13.0)
12 (13.0)
11 (12.0)
12 (13.0)
8 (8.7)
7 (7.6)
6 (6.5)
2 (2.2)
2 (2.2)
3 (3.3)
3 (3.3)
1 (1.1)
2 (2.2)
1 (1.1)
1 (1.1)
2 (2.2)
0 (0)
1 (1.1)
0 (0)
0 (0)
0 (0)
0 (0)
4
30
15 (50.0)
8 (26.7)
14 (46.7)*
11 (36.7)
5 (16.7)
2 (6.7)
3 (10.0)
5 (16.7)
2 (6.7)
4 (13.3)
1 (3.3)
1 (3.3)
3 (10.0)
0 (0)
1 (3.3)
0 (0)
0 (0)
0 (0)
2 (6.7)*
0 (0)
0 (0)
0 (0)
1 (3.3)
0 (0)
0 (0)
1 (3.3)
5
1
0 (0)
0 (0)
0 (0)
0 (0)
0 (0)
0 (0)
0 (0)
0 (0)
0 (0)
0 (0)
0 (0)
0 (0)
0 (0)
0 (0)
0 (0)
0 (0)
0 (0)
0 (0)
0 (0)
0 (0)
0 (0)
0 (0)
0 (0)
0 (0)
0 (0)
0 (0)
II. Numbers and percentages (in parentheses) of subjects with each modiﬁed gingival index (MGI) who responded yes to each
question on a medical history questionnaire. ∗p < 0.05, shown in bold: subjects with the row’s MGI are more likely to have
responded yes to the column’s question than subjects with other MGIs. BP: blood pressure; FH: family history; Rx: treatment.
Routine health screenings
Technology-enabled screenings
MGI
No. patients
High BP
Low BP
High BMI
Low BMI
Low O2
Retinal
TM
Finger-nose
Gait
0
2
1 (50.0)
0 (0)
2 (100)
0 (0)
0 (0)
0 (0)
0 (0)
0 (0)
0 (0)
1
39
4 (10.3)
1 (2.6)
18 (46.2)
5 (12.8)
1 (2.6)
5 (12.8)*
3 (7.7)
0 (0)
0 (0)
2
120
24 (20.0)
0 (0)
55 (45.8)
19 (15.8)
6 (5.0)
0 (0)
8 (6.7)
0 (0)
0 (0)
3
92
14 (15.2)
2 (2.2)
11 (12.0)
18 (19.6)
4 (4.4)
0 (0)
10 (10.9)
2 (2.2)
1 (1.1)
4
30
9 (30.0)
0 (0)
11 (36.7)
7 (23.3)
1 (3.3)
0 (0)
2 (6.7)
0 (0)
1 (3.3)
5
1
0 (0)
0 (0)
0 (0)
0 (0)
0 (0)
0 (0)
0 (0)
0 (0)
0 (0)
III. Numbers and percentages (in parentheses) of subjects with each modiﬁed gingival index (MGI) who were reported as
abnormal in each routine health screening and technology-enabled screening. ∗p < 0.05, shown in bold: subjects with the
row’s MGI are more likely to have the column’s condition than subjects with other MGIs. BP: blood pressure; BMI: body
mass index; O2: blood oxygen level; TM: tympanic membrane.
each age cohort with a particular MGI and who answered
yes to questions on the medical history questionnaire. Among
middle-aged subjects, those with an MGI of 1 were more likely
to report asthma MGIs (p=0.0475). Young adults with an MGI
of 4 were more likely to report a family history of eye diseases
(p=0.0049).
D. Periodontal health correlations: routine health
screenings
Table 3 shows the number of subjects with a particular
MGI and who were found to have tested positive in each
of the routine health screenings consisting of blood pressure
and BMI measurements. Supplementary Table III shows the
number of subjects of each gender with a particular MGI and
who were found to have tested positive in each of the routine
health screenings. Supplementary Table IV shows the number
of subjects in each age cohort with a particular MGI and who
were found to have tested positive in each of the routine health
screenings. MGIs were not found to be signiﬁcantly correlated
with routine health screening outcomes in this dataset.
E. Periodontal health correlations: technology-enabled
screenings
Table 3 shows the number of subjects with each MGI
score who were found to have an abnormality in each of
the TES tests. Subjects with an MGI of 1 were signiﬁcantly
more likely to have an optic nerve exam abnormality than
subjects with other MGIs (p<0.0001). Supplementary Table
III shows the number of subjects of each gender with a
particular MGI and who were found to have tested positive
in each TES. Males with an MGI of 1 were more likely than
males with other MGIs to also have an optic nerve exam
abnormality (p=0.0002). Supplementary Table IV shows the
number of subjects in each age cohort with a particular MGI
and who were found to have tested positive in each TES. Old-
aged subjects with an MGI of 1 were more likely than old-
aged subjects with other MGIs to have an optic nerve exam
abnormality (p=0.0002).
V. DISCUSSION
A. Generalization of the classiﬁer on new dataset
Our previously published results reported an AUC of 0.746
for segmentation of periodontal diseases in intraoral images
[7]. The 0.677 AUC we report for this dataset is consis-
tent with expected generalization error and indicates a good
performance. Precision and recall experienced similar modest
decreases, from 0.347 and 0.621 to .271 and .429, respec-
tively [7]. Mean IOU for the classiﬁer’s previously reported
validation dataset was 0.1824 ± 0.1547 when averaged across
images, only slightly higher than the mean IOU of 0.1710 ±
0.1544 we report for this dataset. The difference in IOU is
not signiﬁcant when compared with a two-sample student’s
t-test that accounts for different numbers of samples and pos-
sibly unequal variances (p=0.4099). The classiﬁer accurately
segments many instances of periodontal disease (Figure 3,
columns i-iv). When the classiﬁer does produce false positives
(Figure 3, column v), it is likely due to the high prevalence of
periodontal disease in the training dataset. Specular reﬂection
and possible disease conﬁgurations may contribute to false
negatives (Figure 3, column vi). Such errors may be reduced
by training the classiﬁer with an increased number of images
that capture more varied instances of periodontal disease and
healthy patients. The ROC and precision-recall curves have
few constituent points because the classiﬁer is extremely
conﬁdent in all of its predictions. This was also reported
in the previous study with this classiﬁer [7]. Regulariza-
tion may help the classiﬁer temper its prediction conﬁdence,
leading to increased generalization performance. Overall, our


## Page 6


6
JOURNAL OF BIOMEDICAL AND HEALTH INFORMATICS
results further validate our previously published model [7]
and demonstrate that meaningful periodontal health diagnoses
can be annotated remotely and subsequently associated with
ﬂuorescent image regions.
B. Oral-systemic health cross correlations
our sample of 284 adults in an out-patient setting in
Maharashtra, India, is an accurate reﬂection of health in the
surrounding community since it was collected at random,
with no admission requirements other than age and general
good health. Approximately one quarter of all subjects with
periodontal disease reported dental problems on the medical
health questionnaire, and no group of subjects—even that
containing the subjects with the highest MGIs—was more
likely to have done so than another (Table 2). More frequent
periodontal exams, perhaps of the type described in this study,
may keep subjects better apprised of their periodontal and
dental health.
Since only 2 subjects had an MGI of 0 and only 1 subject
had an MGI of 5, no signiﬁcant cross-correlations between
MGIs of 0 or 5 and any of the questionnaire responses, routine
health screening results, or TES results were found (Table
1). A larger sample size would allow more conﬁdence in
determining if such correlations are signiﬁcant or if they are
not.
We report for the ﬁrst time, in an Indian population or
otherwise, a signiﬁcant difference in the periodontal health
of males and females: males were more likely to have MGIs
of 3 while females were more likely to have MGIs of 2.
High prevalence of both gingivitis and more severe periodontal
disease in older subjects was found in this study in agreement
with previous literature [23], [24].
Periodontal health was found to be signiﬁcantly associated
with several diseases and conditions measured in this study.
We report signiﬁcant correlations between an MGI of 4 and
swollen joints and a family history of eye diseases. We
also found a signiﬁcant correlation between an MGI of 1
and optic nerve exam abnormalities, reported for the ﬁrst
time in an Indian population (Table 3), which is in agree-
ment with established links between oral and opthalmologic
health measured in other populations [21], [22]. We did not
ﬁnd signiﬁcant correlations between periodontal disease and
cardiovascular health. This may be because our screenings
only performed a single-lead ECG and otherwise relied on
medical history questions as proxies for cardiovascular health.
Higher percentages of subjects who reported having diabetes,
smoking, and using tobacco were had high MGIs (Table 2) as
previously reported by others [19], [24]. High and low BMI
were both prevalent across all MGIs (Table 3). A relatively low
sample size may have contributed to lack of observed cross-
correlations in our population. Training a machine learning
classiﬁer that can associate image segmentation results with
MGI scores and systemic health insights is ongoing in our
research group.
C. Summary
A novel process for oral and TES systemic health screenings
and cross-correlations, enabled by imaging, clinical exam-
inations, machine learning, is reported in this manuscript.
Association of poor periodontal health with systemic out-
comes and poor ophthalmic health reported by us stresses
the importance of oral health screenings at the primary care
level. Our work shows that one aspect of patient health, such
as periodontal health, cannot be fully analyzed in isolation.
The methods and ﬁndings communicated in this manuscript
can help clinicians and computer scientists in automating the
diagnosis and correlation of oral and linked systemic health
conditions, ultimately helping patients who might otherwise
have limited health care access.


## Page 7


YAUNEY et al.: AUTOMATED PROCESS INCORPORATING MACHINE LEARNING SEGMENTATION AND CORRELATION OF ORAL DISEASES WITH SYSTEMIC
HEALTH
7
VI. APPENDIX
This appendix provides additional classiﬁcation results and further granularity for oral-systemic cross-correlations by age
and gender.
MGI
Glasses
Dental
Swollen joints
Hearing
FH diabetes
FH high BP
Tobacco
Difﬁculty walking
High BP
Diabetes
High BP Rx
Asthma
Smoking
FH cardiac
Cardiac Rx
Cardiovascular
Low BP
FH stroke
FH eye disease
Heart attack
Coronary bypass
Drinking
Eye treatment
Memory loss
Ear treatment
FH ear disease
0
0 / 1
0 / 0
0 / 0
0 / 0
1 / 0
0 / 0
0 / 1
0 / 0
0 / 0
0 / 1
0 / 0
0 / 0
0 / 0
0 / 0
0 / 0
0 / 0
0 / 0
0 / 0
0 / 0
0 / 0
0 / 0
0 / 0
0 / 0
0 / 0
0 / 0
0 / 0
1
15 / 8
4 / 7
1 / 3
2 / 5
8 / 5
5 / 2
0 / 1
0 / 3
0 / 1
0 / 1
0 / 1
1 / 2
0 / 1
1 / 2
0 / 0
0 / 0
0 / 0
1 / 0
0 / 0
0 / 0
0 / 1
0 / 0
0 / 0
0 / 0
0 / 1
0 / 0
2
18 / 31
10 / 17
10 / 13
6 / 11
11 / 11
14 / 8
1 / 6
5 / 3
2 / 4
3 / 5
2 / 3
2 / 3
0 / 3
0 / 2
0 / 2
0 / 1
1 / 0
1 / 1
0 / 0
0 / 0
0 / 0
0 / 1
0 / 0
0 / 0
1 / 0
0 / 0
3
15 / 28
6 / 19
9 / 20
4 / 18
4 / 18
4 / 8
0 / 11
2 / 10
3 / 5
2 / 5
1 / 5
0 / 2
0 / 2
2 / 1
0 / 3
0 / 1
2 / 0
1 / 0
1 / 0
0 / 2
0 / 0
0 / 1
0 / 0
0 / 0
0 / 0
0 / 0
4
6 / 9
3 / 5
7∗/ 7
5∗/ 6
1 / 6
0 / 2
0 / 3
4∗/ 1
0 / 2
0 / 3
1 / 0
1 / 0
0 / 3
0 / 0
1 / 0
0 / 0
0 / 0
0 / 0
0 / 2∗
0 / 0
0 / 0
0 / 0
1 / 0
0 / 0
0 / 0
0 / 1
5
0 / 0
0 / 0
0 / 0
0 / 0
0 / 0
0 / 0
0 / 0
0 / 0
0 / 0
0 / 0
0 / 0
0 / 0
0 / 0
0 / 0
0 / 0
0 / 0
0 / 0
0 / 0
0 / 0
0 / 0
0 / 0
0 / 0
0 / 0
0 / 0
0 / 0
0 / 0
I. Numbers of subjects of each gender with each modiﬁed gingival index (MGI) who responded yes to each question on a
medical history questionnaire. Each cell is in the form females / males. ∗p < 0.05, shown in bold: subjects with the row’s
MGI and the given gender are more likely to have responded yes to the column’s question than subjects of the same gender
with other MGIs. BP: blood pressure; FH: family history; Rx: treatment.
MGI
Glasses
Dental
Swollen joints
Hearing
FH diabetes
FH high BP
Tobacco
Difﬁculty walking
High BP
Diabetes
High BP Rx
Asthma
Smoking
0
0 / 0 / 1 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
1 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 1 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 1 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
1
7 / 7 / 8 / 1
1 / 3 / 5 / 2
0 / 1 / 1 / 2
0 / 2 / 3 / 2
4 / 7 / 2 / 0
3 / 4 / 0 / 0
0 / 1 / 0 / 0
0 / 0 / 0 / 3
0 / 0 / 1 / 0
0 / 0 / 1 / 0
0 / 0 / 1 / 0
0 / 0 / 3∗/ 0
0 / 0 / 1 / 0
2
10 / 13 / 29 / 7
1 / 8 / 14 / 4
0 / 5 / 13 / 5
1 / 1 / 9 / 6
7 / 9 / 13 / 1
6 / 8 / 8 / 0
0 / 3 / 2 / 2
0 / 1 / 4 / 3
0 / 0 / 5 / 1
0 / 1 / 6 / 1
0 / 0 / 4 / 1
0 / 1 / 3 / 1
0 / 1 / 1 / 1
3
3 / 12 / 16 / 12
2 / 6 / 12 / 5
0 / 1 / 18 / 10
0 / 2 / 14 / 6
3 / 6 / 3 / 0
2 / 6 / 2 / 2
0 / 1 / 5 / 5
0 / 0 / 9 / 3
0 / 0 / 2 / 6
0 / 0 / 4 / 3
0 / 0 / 1 / 5
0 / 0 / 2 / 0
0 / 0 / 2 / 0
4
0 / 1 / 10 / 4
0 / 1 / 5 / 2
0 / 1 / 7 / 6
0 / 0 / 7 / 4
0 / 3 / 2 / 0
0 / 1 / 1 / 0
0 / 1 / 1 / 1
0 / 0 / 4 / 1
0 / 0 / 1 / 1
0 / 0 / 3 / 1
0 / 0 / 1 / 0
0 / 0 / 1 / 0
0 / 0 / 1 / 2
5
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
MGI
FH cardiac
Cardiac Rx
Cardiovascular
Low BP
FH stroke
FH eye disease
Heart attack
Coronary bypass
Drinking
Eye treatment
Memory loss
Ear treatment
FH ear disease
0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
1
0 / 2 / 1 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 1 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 1
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 1 / 0
0 / 0 / 0 / 0
2
0 / 1 / 1 / 0
0 / 0 / 2 / 0
0 / 0 / 1 / 0
1 / 0 / 0 / 0
0 / 1 / 1 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 1 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 1 / 0
0 / 0 / 0 / 0
3
0 / 2 / 0 / 1
0 / 0 / 0 / 3
0 / 0 / 1 / 0
0 / 1 / 1 / 0
1 / 0 / 0 / 0
0 / 0 / 1 / 0
0 / 0 / 1 / 1
0 / 0 / 0 / 0
0 / 0 / 1 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
4
0 / 0 / 0 / 0
0 / 0 / 1 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 2∗/ 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 1
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 1 / 0 / 0
5
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
II. Numbers of subjects of each age cohort with each modiﬁed gingival index (MGI) who responded yes to each question on
a medical history questionnaire. Each cell is in the form adolescents (18-19) / young adults (20-39) / middle-aged (40-64) /
old-aged (65-90). ∗p < 0.05, shown in bold: subjects with the row’s MGI and in the given age cohort are more likely to have
responded yes to the column’s question than subjects in the same age cohort with other MGIs. BP: blood pressure; FH: family
history; Rx: treatment.
Routine health screenings
Technology-enabled screenings
MGI
High BP
Low BP
High BMI
Low BMI
Low O2
Retinal
TM
Finger-nose
Gait
0
0 / 1
0 / 0
1 / 1
0 / 0
0 / 0
0 / 0
0 / 0
0 / 0
0 / 0
1
1 / 3
1 / 0
11 / 7
3 / 2
1 / 0
1 / 4∗
2 / 1
0 / 0
0 / 0
2
7 / 17
0 / 0
24 / 31
12 / 7
1 / 5
0 / 0
5 / 3
0 / 0
0 / 0
3
1 / 13
1 / 1
8 / 25
6 / 12
1 / 3
0 / 0
1 / 10
0 / 2
0 / 1
4
2 / 7
0 / 0
4 / 7
2 / 5
1 / 0
0 / 0
1 / 1
0 / 0
0 / 1
5
0 / 0
0 / 0
0 / 0
0 / 0
0 / 0
0 / 0
0 / 0
0 / 0
0 / 0
III. Numbers of subjects of each gender with each modiﬁed gingival index (MGI) who were reported as abnormal in each
routine health screening and technology-enabled screening. Each cell is in the form females / males. ∗p < 0.05, shown in bold:
subjects with the row’s MGI and the given gender are more likely to have the column’s condition than subjects of the same
gender with other MGIs. BP: blood pressure; BMI: body mass index; O2: blood oxygen level; TM: tympanic membrane.


## Page 8


8
JOURNAL OF BIOMEDICAL AND HEALTH INFORMATICS
Routine health screenings
Technology-enabled screenings
MGI
High BP
Low BP
High BMI
Low BMI
Low O2
Retinal
TM
Finger-nose
Gait
0
0 / 0 / 1 / 0
0 / 0 / 0 / 0
1 / 0 / 1 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
1
0 / 3 / 1 / 0
0 / 1 / 0 / 0
5 / 6 / 6 / 1
4 / 1 / 0 / 0
0 / 0 / 1 / 0
1 / 1 / 1 / 2∗
0 / 2 / 1 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
2
1 / 6 / 12 / 5
0 / 0 / 0 / 0
8 / 16 / 28 / 3
7 / 9 / 1 / 2
2 / 1 / 2 / 1
0 / 0 / 0 / 0
1 / 2 / 3 / 2
0 / 0 / 0 / 0
0 / 0 / 0 / 0
3
0 / 1 / 9 / 4
1 / 0 / 1 / 0
2 / 8 / 16 / 7
3 / 4 / 5 / 6
0 / 1 / 1 / 2
0 / 0 / 0 / 0
2 / 2 / 4 / 3
0 / 0 / 2 / 0
0 / 0 / 0 / 1
4
0 / 1 / 6 / 2
0 / 0 / 0 / 0
0 / 2 / 8 / 1
0 / 2 / 3 / 2
0 / 0 / 1 / 0
0 / 0 / 0 / 0
0 / 0 / 1 / 1
0 / 0 / 0 / 0
0 / 1 / 0 / 0
5
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
0 / 0 / 0 / 0
IV. Numbers of subjects of each age cohort with each modiﬁed gingival index (MGI) who were reported as abnormal in each
routine health screening and technology-enabled screening. Each cell is in the form adolescents (18-19) / young adults (20-39)
/ middle-aged (40-64) / old-aged (65-90). ∗p < 0.05, shown in bold: subjects with the row’s MGI and in the given age cohort
are more likely to have the column’s condition than subjects in the same age cohort with other MGIs. BP: blood pressure;
BMI: body mass index; O2: blood oxygen level; TM: tympanic membrane.


## Page 9


YAUNEY et al.: AUTOMATED PROCESS INCORPORATING MACHINE LEARNING SEGMENTATION AND CORRELATION OF ORAL DISEASES WITH SYSTEMIC
HEALTH
9
REFERENCES
[1] S. F. Kane, “The effects of oral health on systemic health.” General
dentistry, vol. 65, no. 6, pp. 30–34, 2017.
[2] C. A. Ramseier, J. S. Kinney, A. E. Herr, T. Braun, J. V. Sugai,
C. A. Shelburne, L. A. Rayburn, H. M. Tran, A. K. Singh, and
W. V. Giannobile, “Identiﬁcation of pathogen and host-response markers
correlated with periodontal disease,” Journal of periodontology, vol. 80,
no. 3, pp. 436–446, 2009.
[3] W. Giannobile, J. McDevitt, R. Niedbala, and D. Malamud, “Trans-
lational and clinical applications of salivary diagnostics,” Advances in
dental research, vol. 23, no. 4, pp. 375–380, 2011.
[4] J. L. Ebersole, R. Nagarajan, D. Akers, and C. S. Miller, “Targeted
salivary biomarkers for discrimination of periodontal health and disease
(s),” Frontiers in cellular and infection microbiology, vol. 5, p. 62, 2015.
[5] P. Rechmann, S. W. Liou, B. M. Rechmann, and J. D. Featherstone,
“Performance of a light ﬂuorescence device for the detection of mi-
crobial plaque and gingival inﬂammation,” Clinical oral investigations,
vol. 20, no. 1, pp. 151–159, 2016.
[6] A. Esteva, B. Kuprel, R. A. Novoa, J. Ko, S. M. Swetter, H. M. Blau,
and S. Thrun, “Dermatologist-level classiﬁcation of skin cancer with
deep neural networks,” Nature, vol. 542, no. 7639, p. 115, 2017.
[7] A. Rana, G. Yauney, L. C. Wong, O. Gupta, A. Muftu, and P. Shah,
“Automated segmentation of gingival diseases from oral images,” in
Healthcare Innovations and Point of Care Technologies, 2017 IEEE.
IEEE, 2017, pp. 144–147.
[8] A. Krizhevsky, I. Sutskever, and G. E. Hinton, “Imagenet classiﬁcation
with deep convolutional neural networks,” in Advances in neural infor-
mation processing systems, 2012, pp. 1097–1105.
[9] X. Gao and Y. Qian, “Segmentation of brain lesions from ct images
based on deep learning techniques,” in Medical Imaging 2018: Biomed-
ical Applications in Molecular, Structural, and Functional Imaging,
vol. 10578.
International Society for Optics and Photonics, 2018, p.
105782L.
[10] M. Aubreville, C. Knipfer, N. Oetter, C. Jaremenko, E. Rodner, J. Den-
zler, C. Bohr, H. Neumann, F. Stelzle, and A. Maier, “Automatic
classiﬁcation of cancerous tissue in laserendomicroscopy images of the
oral cavity using deep learning,” Scientiﬁc reports, vol. 7, no. 1, p.
11979, 2017.
[11] S. Imangaliyev, M. H. van der Veen, C. Volgenant, B. G. Loos, B. J.
Keijser, W. Crielaard, and E. Levin, “Classiﬁcation of quantitative light-
induced ﬂuorescence images using convolutional neural network,” arXiv
preprint arXiv:1705.09193, 2017.
[12] G. Yauney, K. Angelino, D. Edlund, and P. Shah, “Convolutional
neural network for combined classiﬁcation of ﬂuorescent biomarkers
and expert annotations using white light images,” in Bioinformatics and
Bioengineering (BIBE), 2017 IEEE 17th International Conference on.
IEEE, 2017, pp. 303–309.
[13] Y. Granot, A. Ivorra, and B. Rubinsky, “A new concept for medical
imaging centered on cellular phone technology,” Plos one, vol. 3, no. 4,
p. e2075, 2008.
[14] K. Angelino, P. Shah, D. A. Edlund, M. Mohit, and G. Yauney, “Clinical
validation and assessment of a modular ﬂuorescent imaging system and
algorithm for rapid detection and quantiﬁcation of dental plaque,” BMC
oral health, vol. 17, no. 1, p. 162, 2017.
[15] G. Litjens, T. Kooi, B. E. Bejnordi, A. A. A. Setio, F. Ciompi,
M. Ghafoorian, J. A. van der Laak, B. van Ginneken, and C. I. S´anchez,
“A survey on deep learning in medical image analysis,” Medical image
analysis, vol. 42, pp. 60–88, 2017.
[16] P. Shah, G. Yauney, O. Gupta, V. Patalano II, M. Mohit, R. Merchant,
and S. V. Subramanian, “Technology-enabled examinations of cardiac
rhythm, optic nerve, oral health, tympanic membrane, gait and coordi-
nation evaluated jointly with routine health screenings: an observational
study at the 2015 kumbh mela in india,” BMJ Open, vol. 8, no. 4, 2018.
[17] F. DeStefano, R. F. Anda, H. S. Kahn, D. F. Williamson, and C. M. Rus-
sell, “Dental disease and risk of coronary heart disease and mortality.”
Bmj, vol. 306, no. 6879, pp. 688–691, 1993.
[18] M. V. Mendez, T. Scott, W. LaMorte, P. Vokonas, J. O. Menzoian, and
R. Garcia, “An association between periodontal disease and peripheral
vascular disease,” The American journal of surgery, vol. 176, no. 2, pp.
153–157, 1998.
[19] H. L¨oe, “Periodontal disease: the sixth complication of diabetes melli-
tus,” Diabetes care, vol. 16, no. 1, pp. 329–334, 1993.
[20] M. S. Al-Zahrani, N. F. Bissada, and E. A. Borawski, “Obesity and
periodontal disease in young, middle-aged, and older adults,” Journal of
periodontology, vol. 74, no. 5, pp. 610–615, 2003.
[21] L. R. Pasquale, L. Hyman, J. L. Wiggs, B. A. Rosner, K. Joshipura,
M. McEvoy, Z. E. McPherson, J. Danias, and J. H. Kang, “Prospective
study of oral health and risk of primary open-angle glaucoma in men:
data from the health professionals follow-up study,” Ophthalmology, vol.
123, no. 11, pp. 2318–2327, 2016.
[22] S. Wagley, K. V. Marra, R. A. Salhi, S. Gautam, R. Campo, P. Veale,
J. Veale, and J. G. Arroyo, “Periodontal disease and age-related macular
degeneration: results from the national health and nutrition examination
survey iii,” Retina, vol. 35, no. 5, pp. 982–988, 2015.
[23] A. H. Shewale, D. R. GAttAni, N. Bhatia, R. Mahajan, and S. Saravanan,
“Prevalence of periodontal disease in the general population of india-a
systematic review,” Journal of clinical and diagnostic research: JCDR,
vol. 10, no. 6, p. ZE04, 2016.
[24] J. P. Shaju, R. Zade, and M. Das, “Prevalence of periodontitis in the
indian population: A literature review,” Journal of Indian Society of
Periodontology, vol. 15, no. 1, p. 29, 2011.
[25] T. G. Pickering, J. E. Hall, L. J. Appel, B. E. Falkner, J. Graves,
M. N. Hill, D. W. Jones, T. Kurtz, S. G. Sheps, and E. J. Roccella,
“Recommendations for blood pressure measurement in humans and
experimental animals: part 1: blood pressure measurement in humans: a
statement for professionals from the subcommittee of professional and
public education of the american heart association council on high blood
pressure research,” Circulation, vol. 111, no. 5, pp. 697–716, 2005.
[26] M. Nitzan, A. Romem, and R. Koppel, “Pulse oximetry: fundamentals
and technology update,” Medical Devices (Auckland, NZ), vol. 7, p. 231,
2014.
[27] R. Lobene, T. Weatherford, N. Ross, R. Lamm, and L. Menaker, “A
modiﬁed gingival index for use in clinical trials.” Clinical preventive
dentistry, vol. 8, no. 1, pp. 3–6, 1986.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
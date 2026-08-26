---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1912.05345
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1912.05345_Severity_Detection_Tool_for_Patients_with_Infectious_Disease

> Source: 1912.05345_Severity_Detection_Tool_for_Patients_with_Infectious_Disease.pdf

> Pages: 8

---


## Page 1


Severity Detection Tool for Patients with Infectious Disease
Girmaw Abebe Tadesse1∗, Tingting Zhu1∗, Nhan Le Nguyen Thanh2, Nguyen Thanh Hung2,
Ha Thi Hai Duong3, Truong Huu Khanh2, Pham Van Quang2, Duc Duong Tran3, Lam
Minh Yen4, H Rogier Van Doorn5,6, Nguyen Van Hao3, John Prince1, Hamza Javed1, Dani
Kiyasseh1, Le Van Tan4, Louise Thwaites4,6 and David A. Clifton1
1Institute of Biomedical Engineering, University of Oxford, Oxford, UK
2Children’s Hospital Number 1, Ho Chi Minh City, Vietnam
3Hospital for Tropical Diseases, Ho Chi Minh City, Vietnam
4Oxford Clinical Research Unit, Ho Chi Minh City, Vietnam
5Oxford University Clinical Research Unit, Hanoi, Vietnam
6Centre for Tropical Medicine and Global Health, Oxford University, UK
Corresponding Email:girmaw.abebe@eng.ox.ac.uk
Hand foot and mouth disease (HFMD) and tetanus are serious infectious diseases in low and middle income
countries. Tetanus in particular has a high mortality rate and its treatment is resource-demanding. Furthermore,
HFMD often affects a large number of infants and young children. As a result, its treatment consumes enormous
healthcare resources, especially when outbreaks occur. Autonomic nervous system dysfunction (ANSD) is the
main cause of death for both HFMD and tetanus patients. However, early detection of ANSD is a difﬁcult and
challenging problem. In this paper, we aim to provide a proof-of-principle to detect the ANSD level automatically
by applying machine learning techniques to physiological patient data, such as electrocardiogram (ECG) and
photoplethysmogram (PPG) waveforms, which can be collected using low-cost wearable sensors. Efﬁcient features
are extracted that encode variations in the waveforms in the time and frequency domains. A support vector
machine is employed to classify the ANSD levels. The proposed approach is validated on multiple datasets of
HFMD and tetanus patients in Vietnam. Results show that encouraging performance is achieved in classifying
ANSD levels. Moreover, the proposed features are simple, more generalisable and outperformed the standard
heart rate variability (HRV) analysis. The proposed approach would facilitate both the diagnosis and treatment
of infectious diseases in low and middle income countries, and thereby improve overall patient care.
1. Introduction:
Infectious diseases, such as tetanus
and hand foot and mouth disease (HFMD), still pose
life-threatening risks to patients in low and middle
income countries [1]. Tetanus is a severe disease, often
necessitating lengthy hospital treatment (up to six weeks),
which was estimated to have caused 48-80,000 deaths
in 2015 [2]. It tends to affect the poorest in society in
low and middle income countries where unvaccinated
individuals, particularly manual workers and farmers, are
at high risk of contracting it [1, 3, 4, 20]. A recent study
showed that tetanus prevalence is still high in a part of
* Joint ﬁrst authors
This paper is a preprint of a paper submitted to Healthcare
Technology Letters. If accepted, the copy of record will
be available at the IET Digital Library
Asia, and that it is associated with high morbidity and
mortality rates [17, 20, 25].
Comparatively, HFMD is typically a benign self-
limited illness in infants and young children. In recent
years, large outbreaks have been reported in the Asia
Paciﬁc region, affecting millions of children [5, 6, 18].
For example, 90% of HFMD incidents in China occur
among children under the age of 5 years [18]. Although
most HFMD cases are mild, a small number of affected
children progress rapidly to severe or fatal manifestations
of the disease. Moreover, survivors may still be afﬂicted
with neurocognitive impairments later in life, despite
having apparently full recovered from severe HFMD [18].
Inability to predict those who will progress to severe cases
means that huge numbers of children are admitted to
1
arXiv:1912.05345v1  [eess.SP]  10 Dec 2019


## Page 2


hospital as a precautionary measure, placing an enormous
burden on healthcare systems [5, 6, 7].
Autonomic nervous system dysfunction (ANSD) is
the main cause of death in the aforementioned infectious
diseases [2, 6, 7, 22, 23]. It is not clinically apparent in the
early stages of disease, but once it is established, treatment
is challenging and, in the case of HFMD, deterioration
can occur rapidly. In tetanus, early diagnosis may enable
preventative intervention and allow differentiation from
other causes of tachycardia and hypertension.
Data-driven approaches have been employed to
assist clinicians making informed decisions during the
diagnosis of infectious diseases [8, 9, 15, 16]. The
physiological data from patients (see Fig. 1) mainly
include electrocardiogram (ECG) [8, 21] followed by
photoplethysmogram (PPG) [9, 16] waveforms.
Existing methods are mainly focused on heart rate
variability (HRV) analysis based on a prior detection of
morphological features [8, 9, 15, 16, 21]. This means
ECG-based features were derived from P-wave, R-peak,
T-wave and the PQ, QRS and ST segments. Similarly,
PPG-based features were derived from the systolic and
diastolic segments.However, morphology-based feature
extraction requires, in addition to more computational
resources, domain-speciﬁc knowledge; and these features
are hardly transferable across different physiological
waveforms (e.g. ECG, PPG, and IP). Furthermore, these
morphological features could easily be affected by noise
and motion artefacts, especially when wearable devices
are employed and/or the patients are children who
are prone to make random movements. The traditional
approach that employs a speciﬁc clinical monitor or
Holter device has been found to have limitations in
clinical practice, especially with small children in the out-
patient setting [7, 24]. As a result, these features are less
robust and have limited generalisability across variations
in patient characteristics and device speciﬁcations.
Figure 1: Example of ECG waveforms (amplitude vs.
time) from two randomly selected tetanus patients
In this paper, we present our preliminary work
on automatic ANSD detection using multivariate
physiological data collected from tetanus and HFMD
patients in Southern Vietnam (see Fig. 2). The proposed
approach could be integrated into the clinical pathway
to provide a low-cost care tool to triage patients. We
collected physiological waveforms from children using
wearable devices, which are low-cost, non-invasive and
easy to wear. In addition, these devices are cost-effective
for resource-limited settings such as low and middle
income countries [9, 10]. After data collection, feature
extraction is applied to encode the variability of these
waveforms both in the time and frequency domains.
The proposed features are designed to be simple and
generalisable across different physiological waveforms
(e.g. PPG and ECG) without a prior detection of domain-
speciﬁc morphological variations. Later, a state-of-the-
art classiﬁer is applied to discriminate the ANSD levels
of patients. We also applied feature-level fusion when
multivariate data was available. This automatic tool for
ANSD detection aims to support efﬁcient allocation of
resources, and hence improve patient care. In addition, as
patients with these diseases are often given antibiotics,
the creation of a robust and reliable detection tool may
also reduce unnecessary use of antibiotics and therefore
limit antimicrobial resistance.
2. Related Works:
As the heart is under autonomic
nervous system control, changes in beat-to-beat variability
of the heart rate, detected by the ECG, have been linked
to changes in autonomic system balance [8].
Lin et al. [15] showed that patients with different
stages of HFMD experienced different levels of central
nervous system complications, which was reﬂected by
their HRV measures. Though HRV has been principally
inferred from ECG signals, PPGs could be promising
alternatives as existing methods in the literature reported
HRV parameters derived from PPG had high correlation
with those derived from ECG [9, 16]. It is encouraging
to be able to carry out PPG-based HRV analysis, as ECG
acquisition is relatively complex, requiring electrodes to
be mounted on speciﬁc anatomical positions, which may
cause skin irritations and be less practical in non-clinical
settings [9, 16].
However, existing HRV-based approaches to evaluate
autonomous dysfunction mainly require the detection of
morphological shapes and features (e.g. QRS complex
and RR intervals) [8, 9, 25], which incurs an additional
pre-processing step. In addition, these features are not
generalisable across different vital signs which follow
different morphological shapes that could be easily
affected by artefacts. Furthermore, HRV parameters
obtained with non-linear modes, such as standard
2


## Page 3


Figure 2: Block diagram of the proposed approach
deviations of short and long diagonal axes in the Poincare
plot (SD1 and SD2), necessitate additional computational
cost.
The
signiﬁcance
of
our
approach
lies
in
the
development of more generic features rather than domain-
speciﬁc ones (e.g. PQRST characteristics for EEG and
systolic and diastolic features for PPG). That means there
is no need for prior detection of these morphologies. As a
result, our approach can be employed across a variety of
modalities that are time-series bio-signals. Bio-signals
are easier and cheaper to collect, typically involving
less obtrusive collection compared to clinical tests. This
approach could therefore also enable remote monitoring
of patients by their care giver, using existing wearable
sensor technologies.
3. Proposed Method: The proposed approach consists
of pre-processing, feature extraction and classiﬁcation
stages as shown in Figure 2. Physiological data collected
using wearable sensors are often susceptible to noise and
movement artefacts. Hence, a high pass ﬁlter followed by
a Gaussian ﬁlter is applied to mitigate these challenges
during the pre-processing stage. Moreover, we aim
to ensemble multiple but simple time- and frequency-
domain features to form a more robust feature set
overall. In addition, the gradient-based feature extraction
(described later) helps to further encode noise-free
features. Feature extraction is applied to each window
of data points segmented from a waveform. The window
duration determines the number of samples extracted from
a continuous waveform.
Given a time-series of physiological data, x = (xn)L
n=1,
where L represents the number of data points in
a window, we propose to extract both time- and
frequency-domain features. The time-domain features
are further grouped into gradient- and non-gradient-
based features. Non-gradient-based time-domain features
encode the basic statistics of the signal, such as minimum,
maximum, median, mean, standard deviation, energy,
kurtosis and zero-crossing [11]. Energy is obtained as
PL
n=1 x2
n. Kurtosis, kx, measures the deviation of a
signal distribution from a Gaussian distribution, that
is kx = L
PL
n=1(xn−µ)4
(PL
n=1(xn−µ)2)2 , where µ is the mean of xn.
Zero-crossing refers to the number of times a signal
amplitude crosses the zero-magnitude threshold and
encodes oscillation characteristics.
Gradient-based
features
help
to
extract
more
dynamic information in the time-domain [12]. The
gradient is computed by applying ﬁrst-order derivative,
i.e. x′
n = xn+1 −xn. Two speciﬁc gradient pooling
features, count (hx) and sum (sx) of the gradient
histogram are extracted. Count pooling counts positive
(h+
x ) and negative gradients (h−
x ), whereas sum pooling
sums all positive (s+
x ) and negative gradients (s−
x ). For
example, h+
x of xn is computed as h+
x = PL−1
n=1 s(x′
n),
where
s(x′
n) =
(
1,
if x′
n ≥0
0,
otherwise.
Frequency-domain features provide more detailed
dynamic information using the fast Fourier transform
(FFT).
The frequency-domain features can be grouped into
two groups: low-frequency (f(l) and whole-frequency
features (fw). Low-frequency features contain the
magnitude of Nl low frequency coefﬁcients after the
Fourier transform. Full-frequency group includes the
sum of frequency response magnitude of frequency bins
clustered into Nb consecutive bins. The signiﬁcance of
the frequency features is as follows. fl contains high-
resolution low-frequency characteristics, as much of
the energy rests in this frequency band. On the other
hand, fw contains the whole spectrum (both the low and
high frequency patterns) with lower resolution. This is
motivated by the need to include the high frequency
characteristics and their comparison with lower frequency
3


## Page 4


ones. As a result, fw encodes the complete frequency
spectrum compared to fl. We tend to cluster the frequency
components into bins to have lower resolution since
higher resolution might result in unnecessarily long
feature dimensions.
Let fx = F(xn) be the frequency response of xn,
fl = {fx(c)}Nl
c=1 and the fw feature (with Nb bands) is
computed as fw(j) = Pσf
l=σi fx(l), where
j ∈[1, Nb], σi = 1 + (j −1) ∗L
2Nb
, σf = 1 + j ∗L
2Nb .
The ﬁnal feature vector is obtained using a simple
concatenation, C(·), of both time- and frequency-
domain features into a single vector. Given two feature
vectors, f1 ∈Rd1 and f2 ∈Rd2, their concatenation fc =
C(f1, f2) results in fc ∈Rdc, where dc = d1 + d2. Similar
concatenation approach is applied for features from
different modalities, (e.g. ECG and PPG). Finally, we
employ support vector machines (SVM) to classify the
ANSD severity levels.
4. Complexity Analysis:
In this section, we present
the complexity analysis of the feature extraction step,
per feature type, in the proposed framework. Given a
time-series signal of L time steps, the computational
complexity of the majority of the time-domain features
(e.g. mean and median) have linearly growing complexity,
i.e. O(L). However, the gradient features may have
additional complexity of O(2L) due to the ﬁrst-
order derivative and the summing/counting of positive
and negative gradients. The Fourier transform for
the frequency-domain features (fl and fw) pose a
computational cost of O(L log(L)) associated with the
FFT computation. In addition, we provide Table 1 that
summarises the wall-clock computation time elapsed for
the extraction of the proposed features for a randomly
selected PPG signal that is ≈5 minutes long. The
whole feature extraction takes ≈21.15 ms, of which
time-domain features elapse ≈17 ms and frequency-
domain features elapse ≈4.15 ms. The experiments were
conducted using Matlab2017a, Intel(R) Xeon(R) CPU
E5-1630 v3 @ 3.70GHz, Ubuntu 16.04 OS and 32GB
RAM.
5. Data Collection: We validate the proposed approach
on datasets of HFMD and tetanus patients admitted in
hospitals in Vietnam1. The HFMD dataset was collected
1 The study was approved by the relevant Ethical
Committees and carried out in line with the declaration
of Helsinki.
Table 1 Summary of wall-clock time elapsed for the
computation of time and frequency features, experimented
on a randomly selected ≈5-mins PPG signal.
Feature group
Feature
Elapsed time (ms)
Time
Mean
3.1
STD
1.6
Zero-crossing
1.2
Minimum
0.1
Maximum
0.1
Median
3.0
Energy
0.3
Kurtosis
3.2
Gradient
4.4
Frequency
Low Freq.
2.9
Whole Freq.
4.1
from Children Hospital No. 1, Ho Chi Minh City, and
contains 74 HFMD patients, with a majority of children
less than three years old. Commercial devices such as
E-patch2 were used to collect ECG (256 Hz) waveforms
in the HFMD dataset. Speciﬁcally, 24 hour-patch ECGs
are recorded at least twice, when patients are admitted to
the infectious disease department and on the penultimate
day of hospitalisation. We used the clinical diagnosis
of the HFMD patients (based on the clinical grading
system developed by the Vietnamese Ministry of Health)
as the ground truth and it contains ﬁve levels (in the
increasing order of severity): 2a(33), 2b1(9), 2b2(11),
3(20) and 4(1). The number of patients per class is shown
in brackets. There is a signiﬁcant imbalance in the number
of cases (patients) of ANSD severity levels. Therefore, we
merged 2b1 and 2b2 into a single class. Similarly, level-3
and -4 were also merged together.
The tetanus dataset contains ECG, PPG and IP
waveforms, each lasting up to 24 hours, collected from a
total of 10 patients (four moderate disease, Ablett Grade
3 and six severe disease Ablett Grade 4) admitted to the
intensive care units (ICU) in the Hospital for Tropical
Diseases, Ho Chi Minh City. The sampling rates of ECG,
PPG and IP waveforms are 300 Hz, 100 Hz and 25 Hz,
respectively. ECG and PPG were time synchronised and
recorded from all the patients, which makes the feature-
fusion of these different modalities easier. However, it is
worth noting that IP signals are missing in four subjects.
A Datex Ohmeda monitor and a pulse oximeter were
employed for data acquisition. VS Capture software [14]
was used to download the signal from the monitor. The
clinical diagnosis of tetanus patients (i.e. moderate or
severe) is used as a ground truth for the experiments. For
a window duration of 5 minutes, the number of samples
extracted from each modality are 3, 077 (ECG), 3, 070
(PPG) and 1, 895 (IP). From HFMD dataset, a total of
60, 373 samples are extracted from the ECG signal.
2 epatch.madebydelta.com
4


## Page 5


6. Parameter Setup: During the feature extraction step,
we set the window duration to be at least ﬁve minutes,
similar to the duration in the clinical baseline method [8]
extracted using a publicly available software solution [13].
The baseline method was selected because it has been a
gold standard for many existing works that focused on
HRV analysis [9, 15, 16, 20]. Recently, a similar method
has been used to study HRV among tetanus patients. We
set the high-pass and low-pass cutoff frequencies to 0.05
Hz and 150 Hz, respectively, in the pre-processing step to
ﬁlter out artefacts in the physiological signals. A temporal
resolution of two is applied to extract gradient pooling
features. A temporal resolution refers to the number of
chunks the original sample is divided into. E.g. given a
5-minute long waveform, a temporal resolution of two
means divide the signal into two chunks (each 2.5 minutes
long) and extract gradient-based features on each of them.
We set Nl = 200 and Nb = 200 in order to achieve a
balance between higher frequency resolution and smaller
feature dimension, i.e. lower values of Nl and Nb result in
lower frequency resolution but smaller feature dimension,
whereas their higher values result in better frequency
resolution but longer feature dimension. Both linear and
Gaussian kernels are experimented with the SVM-based
classiﬁcation. We split the data to train and test sets with a
ratio of 80% and 20%, respectively. The classiﬁcation is
repeated 100 times, each with with different initialisation
of the classiﬁer, and their average performance is reported
(along with the standard deviation across the iterations).
We employ the following performance metrics:
accuracy
(A),
precision
(P),
sensitivity
or
recall
(R),
speciﬁcity
(S)
and
F-score
(F1),
deﬁned
for
a
binary
classiﬁcation
as
follows.
P =
T P
T P +F P ,
R =
T P
T P +F N ,
S =
T N
T N+F P , A =
T P +T N
T P +T N+F P +F N ,
F1 = 2×P ×R
P +R where
TP:
true
positive, TN: true negative, FP: false positive, and
FN: false negative samples. For example, in Mild vs.
Severe classiﬁcation of tetanus patients, TP refers to the
number of samples correctly identiﬁed as Severe and
similar to the ground truth label; TN refers to the number
of samples correctly identiﬁed as Mild and similar to the
ground truth label; FP refers to the number of samples
incorrectly classiﬁed as Severe but labelled as Mild in
the ground truth; and FN refers to the number of samples
misclassiﬁed as Mild but labelled as Severe in the ground
truth. For the HFMD dataset, which involves multi-class
classiﬁcation, an SVM with one-vs-all (OVA) strategy is
used. For example, during the classiﬁcation of class 2a,
samples from this class are positive samples and all the
samples from the remaining classes (i.e. 2b, 3 and 4)
are treated as negative samples. For example, during the
classiﬁcation of class 2a, samples from this class are
positive samples and all the samples from the remaining
classes (i.e. 2b, 3 and 4) are treated as negative samples.
The performance metrics are initially computed for each
OVA classiﬁcation and the average performance across
the classes is reported as a ﬁnal result.
Table 2 ANSD level classiﬁcation of HFMD patients.
SVM (%) - Linear Kernel
Features
A
P
R
S
F1
Baseline [8]
57.1 ± 0.2
35.0 ± 0.2
35.2 ± 0.2
67.6 ± 0.1
34.6 ± 0.2
Proposed
64.7 ± 0
49.1 ± 0.1
46.9 ± 0.1
73.4 ± 0
43.2 ± 0.1
Concatenated
66.9 ± 0.1
52.0 ± 0.1
50.1 ± 0.2
75.0 ± 0.1
48.0 ± 0.2
SVM (%) - Gaussian Kernel
Features
A
P
R
S
F1
Baseline [8]
57.7 ± 0.7
36.2 ± 0.4
36.3 ± 0.7
68.2 ± 0.4
35.7 ± 0.6
Proposed
70.9 ± 0.1
60.6 ± 0.1
55.9 ± 0.2
78.0 ± 0.1
55.7 ± 0.2
Concatenated
70.2 ± 0.1
60.0 ± 0.1
54.5 ± 0.1
77.3 ± 0.1
53.9 ± 0.2
7. Results and Discussion:
The proposed approach
provides encouraging results in both HFMD (see Table 2)
and tetanus (see Table 3) datasets. It is evident from
Table 2 and Figure 3 that the baseline features, which
require detection of QRS complex prior to the feature
extraction, fail to discriminate the severity levels of
ANSD in HFMD patients. Moreover, the confusion
matrices in Figure 3 show a misclassiﬁcation of 2a
and 2b classes as there is no well-deﬁned clinical
threshold to separate them. The higher classiﬁcation
of class-3 to 2a than to 2b is partly due to the
class imbalance, and requires further investigation. We
experimented with both linear and Gaussian kernels
for the SVM, and Table 2 shows that Gaussian kernel
performs signiﬁcantly better than the linear kernel,
particularly for the proposed method where about 5%
F1-score improvement is achieved using the Gaussian
kernel. It is clear that the baseline set of features are
less effective at discriminating ANSD levels, and even
their concatenation with the proposed features does not
provide a signiﬁcant improvement. The accuracy (A) and
speciﬁcity (S) classiﬁcation metrics are expectedly higher
than the remaining performance metrics, precision (P),
recall (R) and their F1 score. This is due to the one-
vs-all classiﬁcation strategy employed in the SVM
Table 3 Severity-level classiﬁcation of tetanus patients.
SVM (%) - Gaussian Kernel
Data
A
P
R
S
F1
Baseline-ECG[8]
73.9 ± 0.9
75.48 ± 1.5
77.5 ± 0.4
67.73 ± 3.1
76.48 ± 0.6
IP
65.7 ± 1.3
63.2 ± 1.0
94.7 ± 0.2
27.8 ± 2.8
75.8 ± 0.7
PPG
70.2 ± 1.0
70.4 ± 0.8
92.6 ± 0.3
29.5 ± 2.9
80.0 ± 0.5
ECG
80.2 ± 0.7
78.4 ± 0.9
95.3 ± 0.5
53.4 ± 2.5
86.0 ± 0.4
ECG+PPG
78.2 ± 1.0
75.3 ± 1.0
98.1 ± 0.0.3
43.1 ± 3.3
85.2 ± 0.6
5


## Page 6


Figure 3: Normalised confusion matrices (%) of baseline, proposed features and their concatenation for ANSD level
classiﬁcation of HFMD patients, with dark colours representing higher magnitudes.
implementation for multi-class classiﬁcation in the
HFMD dataset.
Similarly, the severity-level classiﬁcation results of
tetanus patients are shown in Table 3. IP achieves the
lowest performance compared to ECG and PPG due to
the following reasons. First, the number of IP samples is
the lowest among all modalities since only six (among ten)
subjects had IP waveforms. In addition, the IP waveforms
have low sampling rate (25 Hz) in the dataset compared to
those of PPG (100 Hz) and ECG (300 Hz). As a result, the
IP-based features suffer from the low-temporal resolution
of IP waveforms. Higher sampling rate of ECG could
also partly explain why ECG performance is better than
PPG. In addition, ECG waveforms are relatively stable
compared to PPG waveforms as the former are often
collected from patient’s chest while the latter are collected
from motion-prone ﬁngers/toes. The fusion of features
from ECG and PPG waveforms improved the recall to
98.1% from their separate recall values of 92.6% (PPG)
and 95.3% (ECG).
In clinical practices, 5-min window duration is
often applied for HRV. Accordingly, we have used
the same duration for comparison with the baseline
method in previous experiments. However, we have also
experimented the proposed feature extraction method
for different window duration (see Table 4.) The results
demonstrated that the proposed approach is able to encode
time and frequency domain features even for shorter
window duration. This is partly due to the repetitive
nature of physiological signal characteristics, e.g. QRS
complex in ECG. Furthermore, shorter window duration
provides higher number of samples for training and hence
improved classiﬁcation performance, as shown in Table 4.
Comparatively, we found that it was difﬁcult to
classify the severity levels of HFMD patients, which we
hypothesize could be for the following reasons. First,
the HFMD dataset was collected from children which
Table 4 Comparison of 5-minute and 1-minute window
duration on the classiﬁcation of tetanus severity levels.
SVM (%) - Gaussian Kernel
Data
A
P
R
S
F1
IP-5
65.7 ± 1.3
63.2 ± 1.0
94.7 ± 0.2
27.8 ± 2.8
75.8 ± 0.7
IP-1
81.2 ± 0.9
78.0 ± 1.2
93.2 ± 0.5
65.5 ± 2.7
84.9 ± 0.5
PPG-5
70.2 ± 1.0
70.4 ± 0.8
92.6 ± 0.3
29.5 ± 2.9
80.0 ± 0.5
PPG-1
78.0 ± 0.8
77.9 ± 0.9
92.1 ± 0.4
52.5 ± 2.7
84.4 ± 0.4
ECG-5
80.2 ± 0.7
78.4 ± 0.9
95.3 ± 0.5
53.4 ± 2.5
86.0 ± 0.4
ECG-1
91.2 ± 0.2
90.7 ± 0.5
96.1 ± 0.3
82.5 ± 1.1
93.3 ± 0.1
are highly likely to move compared to the more static
adult tetanus patients. The motion artefacts affect the data
quality and degrade the classiﬁcation performance. As a
result, the features extracted from the PPG waveforms in
HFMD patients are less discriminative compared to ECGs
shown in Figure 3. In addition, a multi-class classiﬁcation
in HFMD dataset (i.e. three classes) is more challenging
than the binary classiﬁcation problem in the tetanus
dataset.
8. Conclusions:
We presented our proof-of-principle
study to triage patients with infectious diseases (tetanus
and HFMD) using low-cost and unobtrusive wearable
sensors that collect artefact-prone physiological patient
data. For this task, we proposed simple and more generic
(across modalities) features to encode the waveform
dynamics in time and frequency domains. Our approach
was validated on two independent datasets collected
from tetanus and HFMD patients in Southern Vietnam.
In addition, the proposed approach provides efﬁcient
hospital resource utilisation in low resource-settings,
which could in turn help improve overall patient care. The
proposed approach still depends on a manual encoding
of features. Thus, future works include collecting more
patient data and employing data-intensive models, such
as deep learning, that generalise better than handcrafted
6


## Page 7


features across variations in patients and acquisition
devices.
9. Acknowledgment:
We would like to thank Dr
Nguyen Van Vinh Chau, Director of the Hospital for
Tropical Diseases, staff in ICU at the Hospital for Tropical
Diseases and Children’s Hospital Number 1, Ho Chi Minh
City.
10. Funding and Declaration of Interests: The study
was funded by the Wellcome Trust Grants 107367/Z/15/Z
and 089276/B/09/7, the Royal Academy of Engineering
grant FoRDF1718_3_19, and the RAEng Frontiers
of Engineering for Development under the Global
Challenges Research Fund.
11
References
[1] D. B. Thuy et al., Tetanus in Southern Vietnam:
Current Situation. Am J Trop Med Hyg, 96(1): 93-
96, 2017.
[2] V. L. Feigin et al., Global, regional, and national
burden of neurological disorders during 1990-2015:
a systematic analysis for the Global Burden of
Disease Study 2015. The Lancet Neurology 16.11:
877-897, 2017.
[3] P. K. Lam et al., Prognosis of neonatal tetanus in the
modern management era: an observational study in
107 Vietnamese infants. Int J Infect Dis 33C, 2014.
[4] H. T. Trieu et al., Neonatal tetanus in Vietnam:
comprehensive intensive care support improves
mortality rates. J Pediatric Infect Dis Soc 5: 227-
230, 2015.
[5] L. N. T. Nhan et al., Severe enterovirus A71
associated hand, foot and mouth disease, Vietnam,
2018: preliminary report of an impending outbreak.
Eurosurveillance 23.46, 2018.
[6] T. Y. Lin et al., Enterovirus 71 outbreaks, Taiwan:
occurrence and recognition. Emerg Infect Dis
9:291-3, 2003.
[7] N. J. Schmidt et al., An apparently new enterovirus
isolated from patients with disease of the central
nervous system. J Infect Dis 129:304-9, 1974.
[8] M. Malik et al., Heart rate variability: Standards
of measurement, physiological interpretation, and
clinical use. European Heart Journal, 17(3),
pp.354-381, 1996.
[9] V. Jeyhani et al., Comparison of HRV parameters
derived
from
photoplethysmography
and
electrocardiography signals. In Proc. of the
IEEE Engineering in Medicine and Biology Society
(EMBC). pp. 5952-5955, 2015.
[10] D. Saadi et al., ePatch - A Clinical Overview, 2014.
[11] G. Abebe et al., Robust multidimensional motion
features for ﬁrst-person vision activity recognition.
Computer Vision and Image Understanding (CVIU),
Vol. 149, pp.229-248, 2016.
[12] M. S. Ryoo et al., Pooled motion features for ﬁrst-
person videos. In Proc. of IEEE Conference on
Computer Vision and Pattern Recognition (CVPR),
pp. 896-904, 2015.
[13] V. Pichot et al., HRV analysis: a free software
for analyzing cardiac autonomic activity. Front.
Physiol. 22 November 2016.
[14] J. G. Karippacheril and T. Y. Ho, Data acquisition
from S/5 GE Datex anesthesia monitor using
VSCapture: An open source. NET/Mono tool.
Journal of Anaesthesiology, Clinical Pharmacology
29, no. 3: 423, 2013.
[15] L. Ming-Tai, et al., Heart rate variability monitoring
in the detection of central nervous system
complications in children with enterovirus infection.
Journal of Critical Care 21.3 (2006): 280-286.
[16] P. Rong-Chao, et al., Extraction of heart rate
variability from smartphone photoplethysmograms.
Computational and Mathematical Methods in
Medicine, 2015.
[17] K. M. Saleh et al., Tetanus: still a killer in adults.
Anaesthesia, Pain & Int. Care (2019): 149-153.
[18] L. Kuanrong, et al., Identifying risk factors
for neurological complications and monitoring
long-term neurological sequelae: protocol for the
Guangzhou prospective cohort study on hand-foot-
and-mouth disease. BMJ Open 9.2, 2019
[19] World Health Organization. A Guide to Clinical
Management and Public Health Response for Hand,
Foot and Mouth Disease (HFMD), 2011.
[20] F. Zhe et al., Clinical features and outcomes of
tetanus: a retrospective study. Infection and Drug
Resistance 12 (2019): 1289.
[21] E. G. Rosenstock et al., Heart rate variability
in the neonate and infant: analytical methods,
physiological and clinical observations. Acta
Paediatrica 88.5 (1999): 477-482.
[22] F. J. Carod-Artal, Infectious diseases causing
autonomic
dysfunction.
Clinical
Autonomic
Research 28.1 (2018): 67-81.
[23] T. Q. Phan, Severe Hand Foot and Mouth Disease
in Vietnamese Children: Clinical Features and
Management Strategies. Doctoral Dissertation. The
7


## Page 8


Open University, 2018.
[24] M. Macinnes et al., Comparison of a smartphone-
based ECG recording system with a standard
cardiac event monitor in the investigation of
palpitations in children. Archives of Disease in
Childhood 104.1 (2019): 43-47.
[25] H. T. H. Duong et al., Heart rate variability as an
indicator of autonomic nervous system disturbance
in tetanus. American Journal of Tropical Medicine
& Hygiene (2019), to appear.
8

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1912_05345_severity_detection_tool_for_patients_with_infectious_disease
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1912_05345_SEVERITY_DETECTION_TOOL_FOR_PATIENTS_WITH_INFECTIOUS_DISEASE.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

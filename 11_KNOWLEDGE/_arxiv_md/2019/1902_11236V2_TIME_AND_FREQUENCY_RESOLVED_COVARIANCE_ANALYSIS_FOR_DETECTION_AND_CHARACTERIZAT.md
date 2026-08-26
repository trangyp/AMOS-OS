---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1902.11236v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1902.11236v2_Time-_and_frequency-resolved_covariance_analysis_for_detection_and_characterizat

> Source: 1902.11236v2_Time-_and_frequency-resolved_covariance_analysis_for_detection_and_characterizat.pdf

> Pages: 21

---


## Page 1


arXiv:1902.11236v2  [q-bio.NC]  15 Jun 2020
Time- and frequency-resolved covariance analysis for detection and
characterization of seizures from intracraneal EEG recordings
Melisa Maidana Capit´an12, Nuria C´ampora23, Claudio Sebasti´an Sigvard1,
Silvia Kochen23 and In´es Samengo12
1: Instituto Balseiro and Departamento de F´ısica M´edica, Centro At´omico Bariloche, Argentina.
2: Consejo Nacional de Investigaciones Cient´ıﬁcas y T´ecnicas, Argentina.
3: Neurosciences and Complex Systems Unit (ENyS), Hospital El Cruce “N´estor Kirchner”, Universidad
Nacional Arturo Jauretche, Argentina.
Abstract
The amount of power in different frequency bands of the electroencephalogram (EEG)
carries information about the behavioral state of a subject. Hence, neurologists treating
epileptic patients monitor the temporal evolution of the different bands. We propose a
covariance-based method to detect and characterize epileptic seizures operating on the
band-ﬁltered EEG signal. The algorithm is unsupervised, and performs a principal compo-
nent analysis of intra-cranial EEG recordings, detecting transient ﬂuctuations of the power
in each frequency band. Its simplicity makes it suitable for online implementation. Good
sampling of the non-ictal periods is required, while no demands are imposed on the amount
of data during ictal activity. We tested the method with 32 seizures registered in 5 pa-
tients. The area below the resulting receiver-operating characteristic curves was 87% for
the detection of seizures and 91% for the detection of recruited electrodes. To identify the
behaviorally relevant correlates of the physiological signal, we identiﬁed transient changes
in the variance of each band that were correlated with the degree of loss of conscious-
ness, the latter assessed by the so-called Consciousness Seizure Scale, summarizing the
performance of the subject in a number of behavioral tests requested during seizures. We
concluded that those crisis with maximal impairment of consciousness tended to exhibit an
increase of variance approximately 40 seconds after seizure onset, with predominant power
in the theta and alpha bands, and reduced delta and beta activity.
Keywords: EEG - epilepsy - consciousness - principal component analysis.
Accepted in Biological Cybernetics, June 2020.
1


## Page 2


1
Introduction
The last decades have witnessed an explosion in computational techniques aimed at automat-
ically detecting and characterizing epileptic seizures [Tzallas et al., 2012, Orosco et al., 2013,
Alotaiby et al., 2014, Ulate-Campos et al., 2016, Boubchir et al., 2017].
Some are based on
simple measures, that assess the amount of power in different frequency bands [Bartolomei et al., 2008].
These methods are easily implemented, but their performance is limited, since a single dimen-
sion, as the ratio of high-to-low frequency power, is often not enough to encompass different
types of seizures. Others focus on detecting some of the speciﬁc features that neurologists are
trained to look for, when scrutinizing a recording [Harner, 2009, Liu et al., 2013]. These meth-
ods can achieve a good detection performance, but are limited by the fuzziness of the deﬁnition
of the targeted features, since there is no precise consensus among experts of what exactly con-
stitutes a feature [Wilson and Emerson, 2002]. Other approaches decide in terms of the visual
properties of the EEG signal when plotted in the time-frequency domain [Boubchir et al., 2014,
Boubchir et al., 2015], or of the total amount of synchrony [Schevon et al., 2007, Warren et al., 2010,
Evangelista et al., 2015, Courtens et al., 2016, Bonini et al., 2016], or of the coherence [Wang et al., 2017,
Aggarval and Ghandi, 2017] or of the phase-to-amplitude coupling [Edakawa et al., 2016, Liu et al., 2017,
C´ampora et al., 2019, Dellavale et al., 2020]. Yet others [Kharbouch et al., 2011, Liu et al., 2012,
Donos et al., 2015, Heller et al., 2018, Hugle et al., 2018], make no assumptions on the dis-
tinctive features tagging seizures, and by means of supervised-learning algorithms, employ
machine-learning techniques to discover the function that maps EEG signals to an output that
distinguishes between “seizure” and “no seizure”.
Many of these methods, though sometimes effective in their detection precision and recall,
ﬁt literally thousands of parameters, and are hard to interpret, since their outcome is not based
on quantities on which clinical intuition is based. Neurologists analyze EEG data in terms of
frequency bands, and they are able to associate speciﬁc features of the EEG signal with speciﬁc
changes in the behavioral state of the patient. Therefore, when developing a tool for automatic
analysis of EEG signals, it is important to ﬁrst decide whether the aim is to produce an accurate
algorithm for seizure detection, or rather, to design a tool that assists neurologists to identify
the features that mark the onset of the seizure, to characterize its propagation, and to reveal
the features that co-vary with the clinical manifestations. This paper ascribes to this second
goal. We ﬁlter the EEG signal in the same frequency bands neurologists usually analyze them,
and we propose an unsupervised seizure-detection algorithm based on covariance analysis. The
approach is simple enough to be implemented online, and discloses the temporal properties of
2


## Page 3


the EEG signal that are correlated with the degree of loss of consciousness, the latter, assessed
by a standard behavioral test.
Covariance analysis has long been used in neuroscience when analyzing electrophysiologi-
cal recordings of the activity of single sensory neurons that are selective to speciﬁc stimulus fea-
tures [Bryant and Segundo, 1976, de Ruyter van Steveninck and Bialek, 1988, Simoncelli et al., 2004,
Samengo and Gollisch, 2013]. The physiological signal is typically discrete (spike or no spike)
and the stimulus varies from trial to trial, testing the effect of a collection of features that are
are the candidate relevant dimensions to which the neuron might be sensitive to. The stimulus
dimension along which spiking probability is modulated maximally is identiﬁed as the most
relevant one. We here extend this technique to the study of time-continuous EEG signals, and
search for the temporal structures that are maximally modulated by seizures. We later use the
same idea to identify the temporal features in the signal that are modulated by the degree of loss
of consciousness in each seizure.
2
Materials and Methods
2.1
EEG data sets
Long-term intra-cranial EEG recordings were obtained from 5 hospitalized patients during 24-
hour video-EEG monitoring, lasting for 5 days. The electrodes were implanted as a pre-surgery
evaluation, and their anatomical targeting was decided for each patient on the base of available
non-invasive information about the localization of the epileptogenic zone. The ictal clinical
semiology was obtained from the videos of seizures. EEG signals were obtained at 2 kHz sam-
pling rate from 32 seizures of variable duration (mean: 78 seconds, SD: 41 seconds) recorded
from 5 patients with hypothesis of temporal epilepsy, each patient with a different number of
implanted macro electrodes (Ad-Tech depth electrodes, 0.86mm diameter, 5mm contact spac-
ing, between 5-10 contacts). The total number of analyzed segments was 1599. Each segment
contributing to this total number corresponds to a single patient, a single crisis, and a single
recording site on a single electrode. Segments also included non-epileptic activity, both before
and after the seizure. On average, the seizure took 9% (SD 5%) of each segment. The study has
been performed in accordance with the ethical standards as laid down in the 1964 Declaration
of Helsinki and its later amendments, and was approved by the ethics committee of the El Cruce
N´estor Kirchner and the Ramos Mej´ıa Hospitals. All patients signed a written informed consent
3


## Page 4


form before their voluntary participation in the study.
2.2
Identiﬁcation of epileptic seizures by expert evaluation
Two experts trained and experienced in video-EEG interpretation reviewed all video-EEG record-
ings. Each seizure was reviewed 3 to 4 times in its entirety to identify pathological signs. The
onset of a seizure was established at the ﬁrst electroencephalographic change. The termination
of the seizure was ascribed to the moment when rhythmic activity concluded, the EEG showed
a diffused attenuation or slowing, or more than 90% of the EEG channels were slow and the
patient’s stereotyped behavior ceased.
2.3
Assessment of the degree of loss of consciousness
In 29 of the 32 crisis, the degree of loss of consciousness was assessed by a clinical evaluation
performed by a trained examiner [C´ampora and Kochen, 2016]. The result was summarized by
a value on the Consciousness Seizure Scale (CSS) [Arthuis et al., 2009], derived on the base of
the degree and adequacy of responsiveness of the patient, visual awareness, identiﬁcation of the
seizure as such, and the degree and type of induced amnesia. The index varies between 0 and 9,
with 0-1 representing full awareness, 2-5 moderate consciousness impairment, and 6-9, severe
loss of consciousness.
2.4
Representation of the signals
Neurologists typically inspect EEG signals visually, often ﬁltering speciﬁc frequency bands.
Figure 1A shows the raw signal (top) obtained from a given recording site on a given macro-
electrode, and the same signal ﬁltered in different frequency bands. We represented the signal
as a 5-dimensional vector
st = (sδ, sθ, sα, sβ, sγ),
where the supra-index t stands for vector transposition, and the components representing the
voltage traces in the delta (1-3.4 Hz), theta (3.4-7.4 Hz), alpha (7.4-12.4 Hz), beta (12.4 - 24
Hz) and gamma (24 - 97 Hz) bands, respectively. The variance of each ﬁltered signal in a
one-second non-overlapping sliding window is shown in Fig. 1B.
4


## Page 5


Time (sec)
Amplitude (μV)
Power (μV2)
A
B
Figure 1: Representation of the EEG signal. A: Voltage traces. Top: raw recorded signal ob-
tained in a given contact. Rows 2-6: Same signal ﬁltered in different frequency bands. Vertical
lines: Initiation and termination of the ictal activity. Insets: Detail of the signal in a 2-second
window outside the ictal period (seconds 88-90). Gray band on the left: temporal span of the
19-second window used to sample each covariance matrix. B: Power of each ﬁltered signal as
a function of the position of the 1-second sliding window. The seizure is more evident on the
right panel, which represents the variance of the signals on the left.
2.5
Covariance analysis
We deﬁne the mean vector ⟨s⟩as the temporal average of the whole collection of vectors s(t),
and C0 as the 5 × 5 covariance matrix with entries (C0)ij = ⟨si sj⟩−⟨si⟩⟨sj⟩. The matrix C0
can be taken to its diagonal form D by a coordinate transformation D = Ot C0 O, where O
is an orthogonal matrix. Following [Samengo and Gollisch, 2013], in order to spot departures
from the normal state, all sampled vectors s are transformed into vectors s′ = D−1/2Os. The
new coordinates are here referred to as the symmetric ones. The total covariance matrix of the
entire collection of points once transformed to the symmetric coordinates is the unit matrix.
To detect the seizures, we deﬁned a sliding window lasting for 19 seconds, that was shifted
along the entire recording, one second at a time. For each position t of the window, the 19
symmetric data points contained in it were used to calculate a local covariance matrix C(t). The
largest eigenvalue of this local matrix deﬁned a temporal sequence λ(t) capturing the variance
of the data along the direction of maximal variance inside each 19-second temporal window.
5


## Page 6


Signiﬁcantly increases of λ(t) above unity are candidates to tag the onset of seizures. In order
to avoid false positives due to transient ﬂuctuations induced by limited samples, the departure
was required to last for at least an interval τ. This requirement was instantiated by deﬁning a
temporally ﬁltered signal
¯λ(t) =
Z t+τ/2
t−τ/2
λ(t′) dt′.
Seizures were detected at those points in time where ¯λ(t) surpassed a given threshold.The value
of τ = 54 s was chosen to maximize the agreement between our criterion and that obtained
from the trained neurologists.
3
Results
3.1
An unsupervised method based on PCA of the power in each band
Our ﬁrst goal is to develop an unsupervised method for detecting seizures based on features that
physicians are accustomed to work with. First, the signal is ﬁltered in the delta, theta, alpha, beta
and gamma frequency bands (Sect. 2.4). Covariance analysis is based on a principal-component
analysis of the ﬁltered signals. Our ﬁrst aim is to identify the direction in 5-dimensional space in
which the variance displays an anomalous behavior when entering into the seizure. Our second
aim is to reveal the dimension in which the variance varies systematically with the degree of
loss of consciousness.
In Fig. 2A we show the distribution of voltages of the 5-dimensional vectors st inside and
outside the seizure. The low- and high-frequency (A2) components are displayed in different
panels (A1 and A2, respectively) for better visualization. The α component appears in both.
In Fig. 2 A, the gray points (red online) correspond to the ictal period, and their values oc-
cupy a larger region of space than the black points (non-ictal), most particularly in panel A2.
The variance of the ictal distribution, hence, is larger than the non-ictal one, and the difference
is most evident in the high-frequency subspace (lower panel), where the black points cluster at
the center, and the red ones, lie at the periphery. Our goal is to design an algorithm that can
identify ictal from non-ictal activity by detecting transient increases in the variance. To that
end, in Fig. 2B we depict the ictal and non-ictal voltage distributions. The two conditions are
most clearly differentiated in the higher frequency bands, from alpha to gamma (Fig. 2B, lower
6


## Page 7


Figure 2: 5-dimensional representation of the EEG signal. A: Distribution of ﬁltered signals
of Fig. 1A. A1: Voltages of the delta, theta and alpha components. A2: Variances of the alpha,
beta and gamma components. Black: Non-ictal period. Gray (red online): Ictal period. The
same number of ictal and non-ictal data points is shown, though the ictal voltages have a smaller
variance, so the tend to appear more tightly clustered around the center of the distribution.
B1: Voltage histograms of each component in ictal (striped, pink online) and non-ictal (gray)
temporal windows. C: Ellipsoids describing the contour lines of the best Gaussian ﬁt to the
data of 3 selected seizures of a single patient, in the delta, theta, alpha (C1) and the alpha,
beta, gamma (C2) subspaces. The ellipsoid marked as “Total” ﬁts the whole collection of data,
including ictal and non-ictal activity. Numbers indicate the CSS of each crisis.
panels). From this example, one would be tempted to conclude that an adequate method to
detect ictal activity should be based on identifying anomalous increases in the variance in the
high-frequency bands. This conclusion, however, does not take into account the considerable
patient-to-patient variability in the statistical properties of seizures, nor the variability from cri-
sis to crisis in one given patient. Although the epileptogenic zone [Bancaud et al., 1965] (the
neural network responsible for seizure onset) is always the same for a given subject, the prop-
agation dynamics may vary from one seizure to the next. Therefore, there need not be such
thing as “a typical seizure”. Fig. 2C shows the contour ellipsoids corresponding to the best
Gaussian ﬁt of the data points of 3 different seizures from the same patient. The gamma dimen-
sion is indeed convenient to identify one of the seizures (marked with “1” in Fig. 2C), but this
result cannot be generalized to other seizures. Based on this evidence, we here relinquish the
7


## Page 8


aspiration to identify the seizures by their behavior in some ﬁxed frequency band. Instead, we
focus on characterizing the statistical properties of the non-epileptic state. The aim is to con-
struct a reliable description of the so-called “normal” distribution, and then identify the seizures
as dramatic departures from normality, irrespective of the direction in which the abnormality
manifests itself. This strategy ensures that even a collection of seizures with highly variable
properties can be identiﬁed, as long as they all clearly deviate from the non-epileptic state.
In the full recording, the non-epileptic state contains a number of samples that is overwhelm-
ingly larger than that of the epileptic state. In our data, in which all segments contain a crisis,
seizures comprise about 9% of the signal. The statistical properties of the non-ictal activity,
hence, can be determined even when analyzing the whole collection of data, containing both
the ictal and the non-ictal time segments, since the latter vastly dominate. As a consequence,
we may calculate the ﬁrst two moments of the normal state using the entire recorded signal.
The covariance matrix C0 of the whole collection of vectors s(t) can be easily calculated
(Sect. 2.5). The eigenvectors of C0 are the principal directions of the ellipsoid that encom-
passes the best Gaussian ﬁt of the entire recording, and the eigenvalues are the variances of the
data along these directions. We have veriﬁed that typically, the eigenvectors are aligned with
the coordinate axes, and the eigenvalues decrease monotonously from the delta to the gamma
dimensions. In other words, in normal circumstances, both the mean value and the variance
along the low-frequency components are much larger than the mean and the variance along the
high-frequency components. This property is also evident in the range covered by the horizon-
tal axes of Fig. 2 B. Following [Samengo and Gollisch, 2013], in order to spot departures from
the normal state, we make a coordinate transformation that turns the ellipsoidal distribution of
the normal state into a spherical distribution, with unit variance in all directions. The resulting
symmetric distribution is seen as a gray sphere in Fig. 3A, and the regions of space occupied by
each crisis, as elongated (colored online) ellipsoids.
In order to detect the time windows where the data departed signiﬁcantly from the normal
state (gray sphere of unit radio in Fig. 3A), we deﬁned a sliding window lasting for 19 seconds,
that was shifted along the entire recording, one second at a time. For each position of the
window, the ﬁltered signals (once transformed to the symmetric space) were used to calculate a
local covariance matrix. If the window fell on a non-ictal segment, the eigenvalues of the local
matrix should be approximately unity, coinciding with the spherical distribution–with some
unavoidable ﬂuctuations, due to limited sampling. As the window enters into a seizure, the
eigenvalues are expected to differ from unity, since as shown above, seizures correspond to
8


## Page 9


Figure 3: Detection of seizures as departures from the normal state. A: Ellipsoids describ-
ing the contour lines of the best Gaussian ﬁt to the data of each crisis, in the symmetric space.
In A1, the coordinate axes are the ﬁrst three eigenvectors of C0, and in A2, the 3rd, 4th and 5th.
The inner gray sphere ﬁts the whole collection of data, including ictal and non-ictal activity,
and the associated distribution has unit variance in all directions. Numbers indicate the CSS
of each seizure. Insets depict the spectra of eigenvalues of a local matrix encompassing each
crisis. Each eigenvalue is the square of the length of one of the principal axes of the corre-
sponding ellipsoid. B: Largest eigenvalue of the local matrix, as a function of the position of
the sliding window. Vertical lines indicate the initiation and termination of each crisis, as di-
agnosed by a trained neurologist. The dashed horizontal line marks the unit variance. C and
D: Receiver-operating characteristic (ROC) curves with the performance of the detection al-
gorithm in identifying seizures (C) and recruited electrodes (D), as compared with the ground
truth provided by neurologists. The dashed line represents random detection. Green and blue
areas: With and without transformation to the symmetric space.
collections of data points whose variance deviates from the normal state. In this paper, we
propose to identify the onset of an epileptic seizure in a single channel as the point in time in
which the largest eigenvalue of the local matrix is signiﬁcantly larger than unity. In order to
avoid false positives due to local ﬂuctuations, the deviation of the anomalous eigenvalue was
required to last for a time interval of duration τ (technical details in Sect. 2.5). The seizure was
assumed to last for as long as the local matrix sustained the signiﬁcant departure.
9


## Page 10


Figure 3B shows the temporal evolution of the largest eigenvalue of the local matrices com-
puted in each of the positions of the sliding window. The maximal eigenvalue increases dramat-
ically during the epileptic seizures diagnosed by trained neurologists (shaded rectangles). The
algorithm detects a seizure when the eigenvalue crosses a pre-deﬁned threshold, and remains
above it for an interval of duration τ = 54 seconds. As the threshold is increased, the receiver-
operating characteristic (ROC) curves of Figs. 3C and D are traversed from right to left. The
local nature of the detection procedure can be used to identify the onset of the crisis in each of
the recording channels, and thereby provide a spatio-temporal description of the propagation of
the seizure.
3.2
Performance of the detection algorithm
Assuming that the detection performed by trained neurologists is the ground truth, receiver-
operating curves (ROC) can be constructed to assess the performance of the algorithm. ROC
curves are constructed by plotting the number of true positives as a function of the number of
false positives for each value of the detection threshold. A given crisis is detected when at least
one of the recording channels indicated by physicians produces an eigenvalue that surpasses the
chosen threshold inside the temporal window marked by physicians. A given electrode is iden-
tiﬁed if it produces an outlier eigenvalue inside the temporal window marked by neurologists.
Figures 3C and D display the ROC curves thus obtained.
The performance of the algorithm is assessed by the area beneath the ROC curve. The
optimal operating point is the value of the threshold for which the precision (number of true
detections / total number of detections) equates the recall (number of true detections / total
number of crisis). Table 1 summarizes the effectiveness of the detection procedure. We have
included the performance of the method when the traces are not symmetrized, to highlight the
relevance of the normalization step.
Of all the algorithms discussed in the literature, the only one that has been previously for-
mulated solely in terms of the amount of power in different frequency bands, that can be imple-
mented online, and that has been reported in intra-cranial signals is the so-called epileptogenic
index (EI) [Bartolomei et al., 2008], in which seizures are detected when the power in the high-
frequency bands increases with respect to that of low-frequency bands. We therefore compared
the performance of our algorithm with that of the EI using our corpus of signals. The results are
also included in Table 1, for comparison. The main differences between the two methods are
10


## Page 11


Table 1: Comparison between the performance of the method proposed here (Normalized co-
variance) with the same method without normalization (Na¨ıve covariance), and with the Epilep-
togenic Index (EI)
.
Detection of
Method
Area below ROC curve
True Positives
False Positives
Crisis
Normalized covariance
87%
83%
17%
Electrodes
Normalized covariance
91%
81%
19%
Crisis
Na¨ıve covariance
73%
63%
37%
Electrodes
Na¨ıve covariance
71%
60%
40%
Crisis
EI
75%
70%
30%
Electrodes
EI
71%
60%
40%
that (a) our method makes no a priori assumptions about the frequency bands in which seizures
manifest themselves, and (b) our method requires a transformation to the symmetric space, so
that the asymmetry of the normal state is evened out.
Quite remarkably, the seizures that our algorithm fails to identify are those in which all
eigenvalues are notably smaller than unity, implying that there are some seizures in which the
power in all frequency bands is abnormally small. As far as we know, this is a novel result.
Unfortunately, those seizures cannot be detected by identifying the eigenvalues that are smaller
than a given threshold, because in the normal state, small eigenvalues accumulate near zero.
Hence, detecting seizures by pinpointing abnormally small eigenvalues produces a huge number
of false positives.
3.3
Transient characteristics observed during the loss of consciousness
For each local matrix, the magnitude of the largest eigenvalue is a measure of the degree of
departure from normality. We therefore veriﬁed whether such magnitude co-varied with the
degree of loss of consciousness. In Fig. 4A we see that both quantities are indeed correlated,
and in Fig. 4B, the correlation is shown to be maximal at approximately 50 seconds after seizure
onset.
Interestingly, the seizures that the algorithm fails to detect have small CSS values. Since all
the eigenvalues of these crisis are small, if these crisis were included in Fig. 4A, the correlation
between the magnitude of the largest eigenvalue and the CSS would be even larger.
11


## Page 12


CSS
vδ
c = -0.53
CSS
vα
c = -0.4
CSS
vβ
c = -0.57
2 4

6
8

0.5
-0.5
0
0
Time (s)
Pearson correlation
0.01
1
0.05
α
β


δ
CSS
v

c = 0.43
CSS
vα
c = 0.33
CSS
v

c = 0.46
CSS
λ1
corr = 0.68
A
20
40
60
80
100
-20
1
0.05
0.01
Time (s)
Pearson
correlation
-0.5
0.5
B
C
Figure 4: Correlation between eigenvalues and CSS. A: Average of the magnitude of the
largest eigenvalue of all the local covariance matrices corresponding to all recording channels
involved in each seizure as a function of the CSS. Matrices were located at the 46th second
after seizure onset, as detected by our algorithm. The Pearson correlation coefﬁcient is 0.68
(signiﬁcantly different from zero, p = 7 × 10−5). B: Pearson correlation coefﬁcient (calculated
as in panel A) as a function of the temporal location of the window used to calculate the local
covariance matrices, measured with respect to the onset of the crisis, as determined by our algo-
rithm. The saturation of each data point represents the p-value obtained from a null hypothesis
of uncorrelated variables (inset). C: Temporal evolution of the Pearson correlation coefﬁcient
between the CSS and the absolute value of each component of the eigenvector associated with
the largest eigenvalue (after transforming back to the original space and normalizing), averaged
between all the electrodes recruited by the seizure. The saturation of each data point represents
the p-value obtained from a null hypothesis of uncorrelated variables (inset). Scatter plots: Data
from which the chosen Pearson correlation values were calculated.
The eigenvectors associated with the largest eigenvalue, when transformed to the original
space, exhibited several transient features that were signiﬁcantly correlated with the degree of
loss of consciousness (Fig. 4C). Inside the temporal window (40−60) seconds after seizure on-
set, when also the eigenvalue was signiﬁcantly correlated with the CSS (Fig. 4B), the eigenvec-
tor associated with seizures with severe consciousness impairment tended to have particularly
12


## Page 13


large components in the theta band, and to a lesser degree, also in the alpha band. In addition,
the power in the delta and the beta bands was signiﬁcantly reduced.
4
Discussion
Many of the methods proposed so far for discriminating ictal from non-ictal activity require
extensive training iterations, due to the fact that the distinctive features of epileptic seizures
vary markedly from patient to patient, and sometimes, even from crisis to crisis in a single
patient. Here we propose to identify the seizures only by diagnosing a signiﬁcant deviation of
the variance of the distribution of the ﬁltered signals from the so-called “normal” distribution, no
matter the direction in which the anomaly arises. The performance of the detection algorithm
is around 90%. Although more precise methods exist [Tzallas et al., 2012], our method has
the advantage of being fully transparent, of requiring no training, of being amenable to online
implementation, and of imposing no requirements on the amount of data during the epileptic
state.
The crucial ingredient is the variance of the different frequency bands. In the normal state,
the delta band is the one with largest variance. For the method to work, the transient amount
of power in each band has to be compared with the baseline power. From the methodological
point of view, this means to work in the so called normalized or symmetric space, where the
variance of different frequency bands in the inter-ictal state is evened out. In the symmetric
space, “normality” appears spherical, and seizures are detected as departures from normality.
Deviations in the variance of slow and intermediate frequencies becomes relevant when as-
sessing the degree of loss of consciousness, as revealed by the components of the most relevant
eigenvector. Several studies have started to characterize the spatio-temporal features of those
seizures that diminish or abolish consciousness [Bonini et al., 2016, C´ampora and Kochen, 2016,
Arthuis et al., 2009, Blumenfeld, 2012]. In particular, in [Blumenfeld, 2012], loss of conscious-
ness was associated with increased synchronization in the alpha band. In addition, an increase
of power in the theta band has been previously associated with states of minimal consciousness
[Blumenfeld, 2012, Schiff et al., 2014]. Hence, some previous studies seem to indicate that in-
termediate frequency bands are correlated with impaired consciousness. Our method conﬁrms
this result, since loss of consciousness is maximal in those seizures with large power in the
range of 3-12 Hz, some 50 seconds after seizure onset.
13


## Page 14


The components of the eigenvectors in different bands ﬂuctuate rapidly, implying a complex
dynamics, dominated by transient phenomena. The prominence of each band lasts for only a
few tens of seconds, a time scale that is slower than the induced loss of consciousness. Seizures
are therefore conﬁrmed to be a highly non-stationary process, structured into several phases.
Our analysis reveals that those seizures with signiﬁcant compromise of consciousness are
represented by eigenvectors that display larger amounts of theta power 30-50 seconds after
seizure onset. To a lesser degree, the same effect was observed with the amount of alpha power.
Contrastingly, in the same temporal window, the delta and the beta components of the eigenvec-
tor manifested the opposite trend: Higher CSS was associated with lower power. To relate these
ﬁndings with the present theories of consciousness, we note that temporal lobe complex partial
seizures often involve abnormal theta spike-wave activity [Blumenfeld, 2012]. The network
inhibition hypothesis postulates that loss of consciousness is induced by selective inhibiting
subcortical arousal systems leading to depressed function of the higher order association cor-
tex, including the default-mode network areas [Danielson et al., 2011]. As a consequence, slow
activity emerges, with the typical pattern observed in slow-wave sleep [Englot et al., 2010]. The
association between loss of consciousness and high theta + alpha components reported here, if
conﬁrmed in a larger population of patients, is compatible with the hypothesis that initial focal
activity in the temporal lobe triggers anterior thalamic nuclei [Norden and Blumenfeld, 2002] to
produce polyspike epileptic discharges that propagate the seizure to several cortical regions, and
simultaneously inducing ventral posteromedial nuclei to produce sleep-like spindles interrupt-
ing thalamo-cortical information ﬂow [Feng et al., 2017]. Our results, however, do not conﬁrm
the hypothesis that the amount of delta power can serve to discriminate between seizures with
high and low compromise of consciousness, at least not with intracraneal electrodes, after aver-
aging over all recruited channels. Visual inspection of seizures with different CSS values reveals
that delta power evolves signiﬁcantly throughout the crisis, but is not exclusively enhanced in
those with high CSS. Therefore, though slow activity may indeed be required to inhibit the
default-mode network, as hypothesized by other studies [Englot et al., 2010], our results sug-
gest that, if such is the case, some other source of slow activity is likely to exist, which is present
in seizures with low CSS.
The alpha rhythm has long been known to be suppressed during the acquisition of bottom-up
sensory information [Berger, 1929], as well as during semantic information processing [Klimesch et al., 1997,
Klimesch et al., 1999], directed attentional shifts [Sauseng et al., 2005, Sauseng et al., 2011],
and conscious stimulus detection [Romei et al., 2007]. Indeed, during the normal, physiologi-
cal state, alpha synchronization is often seen as a functional correlate of inhibition of cognitive
14


## Page 15


and motor tasks [Klimesch et al., 2007]. In turn, beta activity has long been associated with
sensory events and information processing during wakefulness. Our results, in which alpha
power increases and beta power diminishes during the seizures that induce unconsciousness, is
consistent with these ﬁndings.
Finally, in the late 80-ies and early 90-ties, several studies proposed that consciousness
requires the synchronization of populations of neurons via rhythmic discharges in the gamma
range [Cauller and Kulics, 1988, Gray et al., 1989, Crick and Koch, 1989]. Our results do not
conﬁrm a prominent role of gamma power, at least, not in the time window where the anomalous
variance is maximal. This negative result is aligned with more recent ﬁndings, in which gamma
power is more linked to the process of reporting conscious information processing, than to
actually experiencing it [Koch et al., 2016, Redinbaugh et al., 2020].
To our knowledge, this is the ﬁrst study that not only reports the performance of an algorithm
in the detection of the crisis, but also, in the detection of the individual electrodes involved in the
onset and the propagation of the crisis, and to correlate the variance of each frequency band with
the CSS. We therefore believe that the method has the potential to characterize the temporal,
the spatial and some of the cognitive properties of seizures.
Acknowledgements
This work was supported by Agencia Nacional de Investigaciones Cient´ıﬁcas y T´ecnicas PICT
Ra´ıces 2014 N. 1004, Consejo Nacional de Investigaciones Cient´ıﬁcas y T´ecnicas PIP 0256.
Conﬂict of interest
The authors declare that they have no conﬂict of interest.
15


## Page 16


References
[Aggarval and Ghandi, 2017] Aggarval, G. and Ghandi, T. K. (2017). Prediction of epileptic
seizures based on mean phase coherence. BioArXiv, pages 1–4.
[Alotaiby et al., 2014] Alotaiby, T. N., Alshebeili, S. A., Alshawi, T., Ahmad, I., and Abd El-
Samie, F. E. (2014). Eeg seizure detection and prediction algorithms: a survey. EURASIP
Journal on Advances in Signal Processing, 183:1–21.
[Arthuis et al., 2009] Arthuis, M., Valton, L., R`egis, J., Chauvel, P., Wendling, F., Naccache,
L., Bernard, C., and Bartolomei, F. (2009). Impaired consciousness during temporal lobe
seizures is related to increased long-distance cortical-subcortical synchronization. Brain,
132(8):2091–2101.
[Bancaud et al., 1965] Bancaud, J., Talairach, J., Bonis, A., Schaub, C., Szikla, G., Borel, P.,
and Bordas Ferrer, M. (1965). La st´erpeo-´electro-enc´ephalographie dans l’ ´epilepsie: infor-
mations neurophysiopathologiques apport´ees par l’investigation fonctionnelle stereotaxique.
Masson, Paris.
[Bartolomei et al., 2008] Bartolomei, F., Chauvel, P., and Wendling, F. (2008). Epileptogenic-
ity of brain structures in human temporal lobe epilepsy: a quantiﬁed study from intracerebral
eeg. Brain, 131(7):1818–1830.
[Berger, 1929] Berger, H. (1929). ¨uber das elektroenkephalogramm des menschen. Archiv f¨ur
Psychiatrie und Nervenkrankheiten, 87:527.570.
[Blumenfeld, 2012] Blumenfeld, H. (2012). Impaired consciousness in epilepsy. Lancet Neu-
rology, 11(9):814–826.
[Bonini et al., 2016] Bonini, F., Lambert, I., Wendling, F. W., McGonigal, A., and Bartolomei,
F. (2016). Altered synchrony and loss of consciousness during frontal lobe seizures. Lancet
Neurology, 12(2):1170–1175.
[Boubchir et al., 2014] Boubchir, L., Al-Maadeed, S., and Bouridane, A. (2014). Haralick fea-
ture extraction from time-frequency images for epileptic seizure detection and classiﬁcation
of eeg data. In 26th International Conference on Microelectronics, pages 32–35. IEEE.
[Boubchir et al., 2015] Boubchir, L., Al-Maadeed, S., Bouridane, A., and Ch`erif, A. A. (2015).
Time-frequency image descriptors-based features for eeg epileptic seizure activities detection
and classiﬁcation. In IEEE 40th International Conference on Acoustics, Speech and Signal
Processing, pages 867–871. IEEE.
16


## Page 17


[Boubchir et al., 2017] Boubchir, L., Boubaker, D., and Pangracious, V. (2017). A review of
feature extraction for eeg epileptic seizure detection and classiﬁcation. In IEEE 40th Inter-
national Conference on Telecommunications and Signal Processing, pages 456–460. IEEE.
[Bryant and Segundo, 1976] Bryant, H. L. and Segundo, J. P. (1976). Spike initiation by trans-
membrane current: A white-noise analysis. Journal of Physiology, 260(2):279–314.
[C´ampora and Kochen, 2016] C´ampora, N. and Kochen, S. (2016). Subjective and objective
characteristics of altered consciousness during epileptic seizures. Epilepsy and Behavior,
55:128–132.
[C´ampora et al., 2019] C´ampora, N., Mininni, C. J., Kochen, S., and Lew, S. E. (2019). Seizure
localization using pre ictal phase-amplitude coupling in intracranial electroencephalography.
Scientiﬁc Reports, 9(1):20022.
[Cauller and Kulics, 1988] Cauller, L. J. and Kulics, A. T. (1988). Comparison of awake and
sleeping cortical states by analysis of the somatosensory-evoked response of postcentral area
1 in rhesus monkey. Experimental Brain Research, 72(3):884–592.
[Courtens et al., 2016] Courtens, S., Colombet, B. C., Tr`ebuchon, A. T., and B`enar, C. (2016).
Graph measures of node strength for characterizing preictal synchrony in partial epilepsy.
Brain Connectivity, 6(7):530–539.
[Crick and Koch, 1989] Crick, F. and Koch, C. (1989). Towards a neurobiological theory of
consciousness. Seminars in the Neurosciences, 2:263–275.
[Danielson et al., 2011] Danielson, N. B., Guo, J. N., and Blumenfeld, H. (2011). The default
mode network and altered consciousness in epilepsy. Behavioral Neurology, 24(1):55–65.
[de Ruyter van Steveninck and Bialek, 1988] de Ruyter van Steveninck, R. and Bialek, W.
(1988). Real-time performance of a movement-sensitive neuron in the blowﬂy visual sys-
tem: Coding and information transmission in short spike sequences. Proceedings of the
Royal Society of London, Series B, Biological Sciences, 234(1277):379–414.
[Dellavale et al., 2020] Dellavale, D., Urdapilleta, E., C´ampora, N., Velarde, O. M., Kochen,
S., and Mato, G. (2020). Prediction of epileptic seizures based on mean phase coherence.
BioArXiv, pages 1–60.
[Donos et al., 2015] Donos, C., D¨umpelmann, M., and Schulze-Bonhage, A. (2015). Early
seizure detection algorithm based on intracranial eeg and random forest classiﬁcation. Inter-
national Journal of Neural System, 25(5):1550023.
17


## Page 18


[Edakawa et al., 2016] Edakawa, K., Yanagisawa, T., Kishima, H., Fukuma, R., Oshino, S.,
Koo, H. M., Kobayashi, M., Tanake, M., and Yoshimine, T. (2016). Detection of epileptic
seizures using phase–amplitude coupling in intracranial electroencephalography. Scientiﬁc
Reports, 6:25422.
[Englot et al., 2010] Englot, D. J., Yang, L. Y., Hamid, H., Danielson, N., Bai, X., Marfeo,
A., Yu, L. Y., Gordon, A., Purcaro, M. J., Motelow, J. E., Agarwal, R., Ellens, D. J.,
Golomb, J. D., Shamy, M. C. F., Zhang, H., Carlson, C. C., Doyle, W., Devinsky, O.,
Vives, K., Spencer, D. D., Spencer, S. S., Schevon, C., Zaveri, H. P., and Blumenfeld,
H. (2010). Impaired consciousness in temporal lobe seizures:role of cortical slow activity.
Brain, 133(12):3764–3777.
[Evangelista et al., 2015] Evangelista, E., B`enar, C., Bonini, F., Carron, R., Colombet, B.,
R`egis, J., and Bartolomei, F. (2015). Does the thalamo-cortical synchrony play a role in
seizure termination? Frontiers in Neurology, 6:192.
[Feng et al., 2017] Feng, L., Motelow, J. E., Ma, C., Biche, W., McCafferty, C., Smith, N., Liu,
M., Zhan, Q., Jia, R., Xiao, B., Duque, A., and Blumenfeld, H. (2017). Seizures and sleep
in the thalamus: Focal limbic seizuresshow divergent activity patterns in different thalamic
nuclei. The Journal of Neuroscience, 37(47):11441–11454.
[Gray et al., 1989] Gray, C. M., K¨onig, P., Engel, A. K., and Singer, W. (1989). Oscillatory
responses in cat visual cortex exhibit intercolumnar synchronization which reﬂects global
stimulus properties. Nature, 338(6213):334.
[Harner, 2009] Harner, R. (2009). Automatic eeg spike detection. Clinical EEG and neuro-
science, 40(4):262–270.
[Heller et al., 2018] Heller, S. M. H., Nematollahi, I., Manzouri, F., D¨umpelmann, M., A., S.-
B., Boedecker, J., and P., W. (2018). Hardware implementation of a performance and energy-
optimized convolutional neural network for seizure detection. In 40th Annual International
Conference of the IEEE Engineering in Medicine and Biology Society., pages 2268–2271.
[Hugle et al., 2018] Hugle, M., Heller, S., Watter, M., Blum, M., Manzouri, F., Dumpelmann,
M., Schulze-Bonhage, A., Woias, P., and Boedecker, J. (2018). Early seizure detection with
an energy-efﬁcient convolutional neural network on an implantable microcontroller. ArXiv,
page 1806.04549.
[Kharbouch et al., 2011] Kharbouch, A., Shoeb, A., Guttag, J., and Cash, S. S. (2011).
An algorithm for seizure onset detection using intracranial eeg. Epilepsy and Behavior,
22(1):S29–S35.
18


## Page 19


[Klimesch et al., 1997] Klimesch, W., Doppelmayr, M., Pachinger, T., and H., R. (1997).
Event-related desynchronization in the alpha band and the processing of semantic informa-
tion. Cognitive Brain Research, 6(2):83–94.
[Klimesch et al., 1999] Klimesch, W., Doppelmayr, M., Schwaiger, J., Auinger, P., and Win-
kler, T. (1999). Paradoxical’ alpha synchronization in a memory task. Epilepsy and Be-
havioer, 7(4):493–501.
[Klimesch et al., 2007] Klimesch, W., Sauseng, P., and Hanslmayr, S. (2007). Eeg alpha oscil-
lations: The inhibition–timing hypothesis. Brain Research Reviews, 53(7):63–88.
[Koch et al., 2016] Koch, C., Massimini, M., Boly, M. B., and Tononi, G. (2016).
Neu-
ral correlates of consciousness: progress and problems. Nature Reviews in Neuroscience,
17:307–321.
[Liu et al., 2017] Liu, Y., Wang, J., Wang, Cai, L., Chen, Y., and Qin, Y. (2017). Epileptic
seizure detection from eeg signals with phase–amplitude cross-frequency coupling and sup-
port vector machine. International Journal of Modern Physics, 32(8):1850086.
[Liu et al., 2012] Liu, Y., Zhou, W., Yuan, Q., and Chen, S. (2012). Automatic seizure detection
using wavelet transform and svm in long-term intracranial eeg. IEEE Transactions on Neural
Systems and Rehabilitation Engineering, 20(6):749–755.
[Liu et al., 2013] Liu, Y.-C., Lin, Chou-Ching K. Lin, J.-J. T., and Sun, Y.-N. (2013). Model-
based spike detection of epileptic eeg data. Sensors, 13(9):12536–12547.
[Norden and Blumenfeld, 2002] Norden, A. D. and Blumenfeld, H. (2002). The role of sub-
cortical structures in human epilepsy. Epilepsy & Behavior, 3(3):219–231.
[Orosco et al., 2013] Orosco, L., Garc´es Correa, A., and Laciar, E. (2013). Review: A survey
of performance and techniques for automatic epilepsy detection. Journal of Medical and
Biological Engineering, 33(6):526–537.
[Redinbaugh et al., 2020] Redinbaugh, M. J., Phillips, J. M., Kambi, N. A., Mohanta, S.,
Andryk, S., Dooley, G. L., Afrasiabi, M., Raz, A., and Saalmann, Y. B. (2020). Thalamus
modulates consciousness via layer-speciﬁc control of cortex. Neuron, 106(1):66–75.
[Romei et al., 2007] Romei, V. R., Gross, J., and Thut, G. (2007). On the role of prestimulus al-
pha rhythms over occipito-parietal areas in visual input regulation: Correlation or causation?
The Journal of Neuroscience, 30(25):8692–8697.
19


## Page 20


[Samengo and Gollisch, 2013] Samengo, I. and Gollisch, T. (2013). Spike-triggered covari-
ance revisited: Geometric proof, symmetry properties and extension beyond gaussian stim-
uli. Journal of Computational Neuroscience, 34(1):137–161.
[Sauseng et al., 2011] Sauseng, P., Feldheim, J. F., Freunberger, R., and Hummel, F. C. (2011).
Right prefrontal tms disrupts interregional anticipatory eeg alpha activity during shifting of
visuospatial attention. Frontiers in Psychology, 2:241.
[Sauseng et al., 2005] Sauseng, P., Klimesch, W., Stadler, W., Schabus, M., Doppelmayr, M.,
Hanslmayr, S., Gruber, W. R., and Birbaumer, N. (2005). A shift of visual spatial attention
is selectively associated with human eeg alpha activity. European Journal of Neuroscience,
22(11):2917–2926.
[Schevon et al., 2007] Schevon, C. A., Cappell, J., Emerson, R. G., Isler, J. R., Grieve, P. G.,
Goodman, R. R., McKhann, G. M., Wiener, H., Doyle, W. K., Kuzniecky, R., Devinsky, O.,
and Gillian, F. G. (2007). Cortical abnormalities in epilepsy revealed by local eeg synchrony.
Neuroimage, 35(1):140–148.
[Schiff et al., 2014] Schiff, N. D., Nauvel, T. N., and Victor, J. D. (2014). Large-scale brain
dynamics in disorders of consciousness. Current Opinion in Neurobiology, 25:7–14.
[Simoncelli et al., 2004] Simoncelli, E. P., Paninski, L., Pillow, J., and Schwartz, O. (2004).
Characterization of neural responses with stochastic stimuli. In Gazzaniga, M., editor, The
cognitive neurosciences, chapter 23, page 327–338. MIT Press, Cambridge, 3 edition.
[Tzallas et al., 2012] Tzallas, A. T., Tsipouras, M. G., Tsalikakis, D. G., Karvounis, E. C.,
Astrakas, L., Konitsiotis, S., and Tzaphlidou, M. (2012). Automated epileptic seizure detec-
tion methods: A review study. In Stevanovic, D., editor, Epilepsy-Histological, Electroen-
cephalographic and Psychological Aspects, chapter 4, pages 75–98. IntechOpen, Croatia.
[Ulate-Campos et al., 2016] Ulate-Campos,
A.,
Couhlin,
F.,
Ga´ınza-Lein,
M.,
S´anchez Fern´andez, I., Pearl, P. L., and Loddenkemper, T. (2016).
Automated seizure
detection systems and their effectiveness for each type of seizure. Seizure, 40:88–101.
[Wang et al., 2017] Wang, G., Sun, Z., Tao, R., Li, K., Bao, G., and Yan, X. (2017). Epileptic
seizure detection based on partial directed coherence analysis. IEEE Journal of Biomedical
and Health Informatics, 20(3):873–879.
[Warren et al., 2010] Warren, C. P., Hu, S., Stead, M., Brinkmann, B. H., Bower, M. R. B., and
Worrell, G. A. (2010). Synchrony in normal and focal epileptic brain: the seizure onset zone
is functionally disconnected. Journal of Neurophysiology, 104(6):3530–3539.
20


## Page 21


[Wilson and Emerson, 2002] Wilson, S. B. and Emerson, R. (2002). Spike detection: A review
and comparison of algorithms. Clinical Neurophysiology, 113(12):1873–1881.
21

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1902_11236v2_time_and_frequency_resolved_covariance_analysis_for_detection_and_characterizat
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1902_11236V2_TIME_AND_FREQUENCY_RESOLVED_COVARIANCE_ANALYSIS_FOR_DETECTION_AND_CHARACTERIZAT.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

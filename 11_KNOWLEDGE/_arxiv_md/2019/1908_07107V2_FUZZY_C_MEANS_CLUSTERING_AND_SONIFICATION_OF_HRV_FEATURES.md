---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1908.07107v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1908.07107v2_Fuzzy_C-Means_Clustering_and_Sonification_of_HRV_Features

> Source: 1908.07107v2_Fuzzy_C-Means_Clustering_and_Sonification_of_HRV_Features.pdf

> Pages: 5

---


## Page 1


Fuzzy C-Means Clustering and Soniﬁcation of HRV
Features
1st Debanjan Borthakur
McMaster University
Hamilton, Canada
borthakd@mcmaster.ca
2nd Victoria Grace
Muvik Labs
New York, USA
vic@muviklabs.io
3rd Paul Batchelor
Muvik Labs
New York, USA
paul@muviklabs.io
4th Harishchandra Dubey
UT Dallas, TX, USA
& Microsoft Corporation, Redmond, WA, USA
Harishchandra.dubey@utdallas.edu
5th Kunal Mankodiya
University of Rhode Island, Kingston, RI
kunalm@uri.edu
Abstract—Linear and non-linear measures of heart rate vari-
ability (HRV) are widely investigated as non-invasive indicators
of health. Stress has a profound impact on heart rate, and
different meditation techniques have been found to modulate
heartbeat rhythm. This paper aims to explore the process of
identifying appropriate metrices from HRV analysis for soniﬁ-
cation. Soniﬁcation is a type of auditory display involving the
process of mapping data to acoustic parameters. This work
explores the use of auditory display in aiding the analysis of
HRV leveraged by unsupervised machine learning techniques.
Unsupervised clustering helps select the appropriate features to
improve the soniﬁcation interpretability. Vocal synthesis soniﬁ-
cation techniques are employed to increase comprehension and
learnability of the processed data displayed through sound. These
analyses are early steps in building a real-time sound-based
biofeedback training system.
Index Terms—HRV, Soniﬁcation, clustering
I. INTRODUCTION
Several previous studies have investigated the importance
of heart rate variability (HRV) measures as a non-invasive
indicator of the state of health. HRV is a non-invasive indicator
that reﬂects the balance of the autonomic nervous system [1].
By indicating how much the heart rate varies over time, HRV
can imply the health status of the person. Meditation has a
profound effect on HRV. Several studies have investigated the
effect of breathing on HRV [2]. Along with linear measures of
HRV, studies have shown that nonlinear measures of HRV are
sensitive to changes in breathing pattern but not light exercise
[3]. Several nonlinear metrices of heart rate variability such as
Symbolic analysis, Shannon Entropy, Rnyi Entropy, Approx-
imate Entropy, Sample Entropy, and Detrended Fluctuation
Analysis are there. Studies have found signiﬁcantly higher De-
trended Fluctuation Analysis during slow breathing exercises
[4]. They also observed signiﬁcantly reduced Approximate
Entropy during slow breathing. They concluded that nonlinear
behaviour is decreased in slow breathing exercises of heart rate
NSERC-CREATE: Complex Dynamics and Muvik Labs
dynamics in healthy young men analyzed through detrended
Fluctuation Analysis (DFA) and various entropies. Previous
studies have also found that rhythmic recitation of mantra
and ava maria produces narrower spectral peaks whereas free
talking produces broader peaks as compared to spontaneous
breathing [5]. Visual representation of these changes in the
HRV and respiration is a standard method for data display.
These physiological signals can also be represented through
sound, which is a process referred to as soniﬁcation. Although
biofeedback systems typically use graphic displays to present
information, auditory displays can have advantages over vi-
sual displays because of the high temporal, amplitude, and
frequency resolution of the auditory system. Since human
hearing is especially adept at detecting temporal patterns,
soniﬁcation of biometric data can lead to better mindfulness
practice. Viewing images or graphs can be distracting and
wearisome for individuals that want to practice meditations.
Sound can also improve listeners focus and pleasure during
biofeedback training [6]. This paper used data collected from
individuals practicing different meditation techniques. Medi-
tation and mindfulness embody many similarities. Practicing
mindfulness encompasses a number of various approaches
that bring user awareness to focus on the present moment. A
growing number of mindfulness exercises concentrate on the
tradition of focused-attention meditation. Using this technique,
the practitioner is led to shift mental attention away from exter-
nal stresses toward internal sensations such as breathing. The
practice of sustained focused attention on breathing has been
shown to improve well-being and reduce stress. Perhaps most
importantly, this technique cultivates introspective awareness,
the ability to receive and attend to the signals that originate
within the body. This awareness has been shown to improve
attention-task performance and regulation of emotions [7].
Soniﬁcation can be a useful tool for practicing mindfulness or
biofeedback training. Visualization of data lacks in its ability
to represent data that dynamically changes over time, which
makes soniﬁcation a suitable complement or alternative.
arXiv:1908.07107v2  [cs.HC]  30 Sep 2019


## Page 2


Parameter mapping and model-based mapping of the data to
acoustic parameters are common in soniﬁcation. Soniﬁcation
can have multiple utilities. Bio-feedback might also ﬁnd its use
in intelligent health recommend systems [19]. In [8] authors
have investigated the effectiveness of representing HRV data
with auditory interfaces as a supplement or complement to
visual displays. In this paper, we have adopted a similar
approach. We extracted the HRV features from the beat to
beat intervals of three data sets, namely, chi, yoga, and
normal breathing, and applied Fuzzy C-Means clustering. The
clustering of the data gives us a hint of the features that can
be useful in classiﬁcation. Based on the plots we selected one
feature for soniﬁcation.
II. RELATED WORK
A. Soniﬁcation
The basic principles of soniﬁcation are analogous to visu-
alization. Visual displays employ shapes, lines, and colors, to
represent data, while soniﬁcation maps data to sonic attributes
such as frequency, spectrum, duration, and intensity, and their
musical correlates pitch, timbre, rhythm, and volume. Soniﬁca-
tion can be used for various types of applications. An auditory
display typically represents a data series with a succession
of non-speech sounds. Some examples where it has been
useful include weather pattern monitoring, volcanic activity
detection, and medical and surgical tools. Soniﬁcation of heart
rate or heart rate variability can allow for many applications in
self-regulation of biometrics. Soniﬁcation can map biometric
data to different sound dimensions, as well as capture the
interactions between these dimensions [9]. The soniﬁed sound
can be used to provide feedback to the user to assist them
in achieving exercise, breathing, and meditation goals. In [10]
authors describe Cardiosound, which is a portable system to
sonify ECG heart rhythm disturbances. Authors mention three
different soniﬁcation designs employed. 1) Polarity pitch, 2)
ECGrains and 3) Marimba. The polarity pitch soniﬁcation
intends to magnify the time difference between expected and
actual R peaks in the ECG waveform. In ECGrains a gran-
ulated sound is triggered whenever an R peak is found. The
difference between actual and expected R peaks is considered.
The rhythmic pattern between pathological and healthy signals
will thus differ based on the grain quantity they will have. The
Marimba soniﬁcation is similar to ECGrains. It uses Marimba
sound instead of sine waves. The Breathing pattern can be
a useful metric for soniﬁcation. In [11] authors have used a
sound synthesis software to sonify the heart rate variability
data. They mapped each cardiac inter beat interval to a pitch
sounded by an oscillator that produces short sine wave sounds
or grains. They also used inter beat intervals as a clock to
provide the timing for each granular event. In [8] author have
examined the categorization task performance of their soniﬁed
signals. They found the accuracy of meditation types and states
based on their developed auditory interface as 85.6 percent. It
shows the effectiveness of soniﬁcation. The paper does not
directly mention which HRV metrics are soniﬁed and what
was the basis of selection of those metrics. In our work we
have used Fuzzy C-Means clustering, which graphically shows
the features best at classifying the three different meditation
techniques used in this study.
B. Fuzzy clustering
Fuzzy clustering or soft clustering is a form of clustering
technique where each data point can belong to one or more
clusters. This is different to hard clustering. Authors in [12]
discusses K-means clustering, which is a hard clustering
method. This technique is developed by J.C Dunn in 1973
and improved by J.C. Bezdek in 1981. The steps involved in
Fuzzy C-Means algorithms are listed below:
• Number of clusters are chosen.
• Coefﬁcients are randomly assigned to the cluster.
• Process is repeated until the algorithm converges.
• Centroids are calculated for each cluster and coefﬁcients
are calculated for each data point.
This algorithms is based on the minimization of the objec-
tive function:
Jm =
N
X
i=1
C
X
j=1
um
ij||Xi −Cj||2
Here m is any real number greater than 1. Here u is the degree
of membership of X in the cluster, C is the center of the cluster.
The norm expresses the similarity of the measured data and
the center. In [13] authors took a similar approach as discussed
in this paper. They applied Fuzzy C-Means clustering and
Euclidian distance measure on the statistical features, such as
heart rate, approximate entropy, mean R amplitude, mean R-R
interval, standard deviation of normal to normal R-R intervals
(SDNN) and root mean square of successive heartbeat interval
differences (RMSSD).
C. Data Collection
The dataset is collected from physionet.org. Dataset consists
of 1) Chi meditation group (age range 26 to 35, mean 29
yrs), 2) Kundalini Yoga meditation group (age range 20 to
52, mean 33 yrs), 3) Spontaneous breathing group (age range
20 to 35, mean 29). The Chi mediator were all graduate and
post-doctoral students. The Kundalini Yoga subjects were at
an advanced level of meditation training as mentioned in [14].
We select 4 subjects’ data from each group for the meditation
period for analysis. So total 4*3=12 subjects data is analyzed
in this paper. The authors in [14] quantiﬁed the heart rate
dynamics using the dataset. They observed prominent heart
rate oscillations, which are associated with slow breathing.
D. Data Analysis
Raw heart rate data is collected from physionet. Figure 1
shows the soniﬁcation architecture. A Matlab based toolbox
mhrv is used for calculation of heart rate variability metric
from the inter-beat intervals [15]. We have used the function
mhrv.hrv.hrv time to get the HRV metrices. They consist of
the following: 1) Average of all NN intervals (AVNN, SDNN,
RMSSD), and 2) The percentage of NN intervals which differ
by at least x (ms) from their preceding interval (pNNX)


## Page 3


Fig. 1. Soniﬁcation Architecture
Fig. 2. Fuzzy -C Means Clustering
respectively. The results are z score normalized prior to clus-
tering by Fuzzy C-Means algorithm. We have used Matlab’s
fcm function for clustering: [centers,U] = fcm(data,Nc) , for
clustering the heart rate variability metrices that are calculated
using the mhrv toolbox. Here centers is the center of the
clusters, U is the fuzzy partition matrix. Nc is the number
of clusters.
Figure 2 shows the Fuzzy C-Means clustering plot for HRV
features. The data is plotted as combination of two dimensions.
The parameters for the Fuzzy C-Means are chosen as number
of clusters=3, Fuzzy partition matrix overlap= 2.0, Maximum
number of iterations=100. In each iteration the fcm calculates
the cluster centers and updates the fuzzy partition matrix and
then computes the objective function value. The clustering
ends when the objective function is not improved further.
We have considered six combinations of features, which are,
SDNN vs AVNN, RMSSD vs AVNN, pNN50 vs AVNN,
RMSSD vs SDNN, pNN50 vs SDNN, pNN50 vs RMSSD.
The next step was the soniﬁcation of the HRV metrics. We
initially used ’sonify’ function in R [16] to represent the
features of HRV through sound, which involved a simple
mapping of the normalized data values to pitch. Then we tried
a different soniﬁcation technique involving formant synthesis
using an audio synthesis engine developed by Muvik Labs.
The sampling rate of the sound is 44100 Hz. AVNN features
from HRV analysis were soniﬁed using a combination of fre-
quency mapping reinforced with a form of formant synthesis.
The formant synthesis approach utilizes a bandlimited narrow
pulse wave put through a bank of four Butterworth bandpass
ﬁlters in series, tuned to approximate the ﬁrst four formants
of a tenor voice [18]. The data mappings control an alpha
parameter that linearly interpolates between two ﬁlter bank
states, shifting between a tenor ’a’ and a tenor ’i’ vowel sound.


## Page 4


Fig. 3. Spectrogram of the soniﬁed features of Meditation Techniques Chi
Fig. 4. Spectrogram of the soniﬁed features of Normal breathing
The intuition behind choosing to use formant synthesis was
that it could potentially activate the linguistic centers of the
brain, making it easier to comprehend and recall patterns in
the sound. Instead of ’sonify’ function of R, we have chosen
the aforesaid method for improved intelligibility. The ﬁgures
3,4,5 shows the spectrogram of the soniﬁed HRV features of
Chi meditation technique, Normal breathing technique, and
Yoga meditation technique respectively.
III. RESULTS AND DISCUSSIONS
Fuzzy C-Means is effective in showing visual difference
between classes [13]. The three classes that we have used
were Chi meditation group, Kundalini Yoga meditation group
and Spontaneous breathing group. The dataset was converted
to RR intervals for analysis. The RR interval is the interbeat
interval. For the HRV analysis we restricted ourselves to the
time domain analysis only. Study [17] has found changes in
relative very low frequency (VLF) power before and during
exercise. Spectral domain features can also be calculated by
the toolbox we are using, but we restricted this analysis to
time domain analysis as the goal is not to compare different
metrices in the three different meditation techniques. Rather
we aimed at clustering the data pairwise to investigate the
Fig. 5. Spectrogram of the soniﬁed features of Meditation Techniques Yoga
features which are best at classifying or clustering the three
groups.
In Figure 2 the pairwise FCM clustering plots are shown.
FCM clustering plots of SDNN vs AVNN and RMSSD vs
AVNN shows three distinct clusters accurately. Visual inspec-
tion of other pairs such as pNN50 vs AVNN and pNN50 vs
SDNN does not show distinct clusters. The Euclidean distance
measurement of each pair of feature center points will provide
more quantiﬁed assessment which is not shown in this work.
The centers of each of the clusters for all four HRV features
are shown in the Table I. The rows in the table are for different
cluster centers.
The next phase of the work was the soniﬁcation of the
HRV features. In [8] authors soniﬁed the HRV features using
a linear mapping. Although which time and frequency domain
features were soniﬁed was not explicitly mentioned. They
also investigated the learnability, conﬁdence, performance and
latency in the classiﬁcation of soniﬁed data by subjects. We
did not yet evaluate the soniﬁed output of the HRV features.
This will be a future step that will be taken. For soniﬁcation
we have chosen the HRV feature metric AVNN. Figures 3,
4, 5 are the spectrogram of the soniﬁed signals for the three
meditation techniques respectively.
Cluster
AVNN
STDNN
RMSSD
pNN50
Cluster1
1.30863
1.37284
1.7099
1.57552
Cluster2
-0.88163
-0.76224
-0.77548
-0.82544
Cluster3
0.15849
0.03227
-0.10038
0.01418
TABLE I
CLUSTER CENTERS FOR ALL THE FEATURES
SoX, a command line sound processing tool, was used
to generate the spectrogram plots with the Discrete Fourier
Transform (DFT) algorithm. Each soniﬁcation WAV ﬁle was
rendered into a Portable Network Graphic (PNG) ﬁle showing
time in the X-axis, frequency in the Y-axis, and audio signal
magnitude in the Z-axis represented by the colour [12]. Visual
inspection of the spectrograms reveals the distinctive nature of
the soniﬁed sounds. An evaluation done by [8] can be helpful


## Page 5


in validating the effectiveness of the soniﬁed signals. We adpot
a formant synthesis soniﬁcation approach with the intuition
that it could potentially activate the linguistic centers of the
brain, which will make it easy to learn and recall the sound
better. Although no quantitative measures have been taken yet
to evaluate the efﬁciency of this soniﬁcation technique, an ini-
tial validation of the technique’s appropriateness was provided
from verbal feedback of four individuals (two musicians and
two non-musicians). A simple A-B test compared individual
responses to the simple sonifcation technique, mapping the
normalized data to frequency (using R toolbox), with the
multi-dimensional vocal synthesis technique (using Muvik
Labs audio synthesis engine). Four out of four individuals
reported they found the vocal synthesis soniﬁcations more
interesting, and easily memorable. The vocal-like soniﬁcations
evoked noticeably more excitement in two of the listeners,
who attempted to imitate the ﬂuctuating soniﬁcation sound.
This response was not perceived after the playing the simple
frequency mapping soniﬁcation technique.
IV. CONCLUSION
Soniﬁcation has more extended scopes as an effective
method of biofeedback training. In this work, we have clus-
tered the HRV metrices and have shown the potential of
sonifying the HRV features. It is also visible from the plots
that FCM clustering can reveal distinct differences between the
classes. It can have applications in classifying different types
of stress, and the effects of different mindfulness exercises for
managing reactions to stress. The soniﬁcation of the relevant
metric can help provide real-time feedback to a person while
performing an exercise in a guided manner. As future work,
we should look for other techniques to effectively identify
the appropriate HRV features to be used for soniﬁcation.
Additionally, we plan to expand on the formant synthesis
technique for soniﬁcation by exploring different mappings of
sonic attributes in the future.
ACKNOWLEDGMENT
We thank NSERC-CREATE: Complex Dynamics and Mu-
vik labs or supporting this research.
REFERENCES
[1] George E. Billman. 2011. Heart rate variability - A historical per-
spective. Frontiers in Physiology 2 NOV, November (2011), 113.
https://doi.org/10.3389/fphys.2011.00086
[2] Anilesh Dey, D.K. Bhattacharya, D.N. Tibarewala, Nilanjan Dey, Amira
S. Ashour, and Dac-Nhuong Le. 2016. Chinese-chi and Kundalini yoga
meditations effects on the autonomic nervous system: comparative study.
[3] Weippert, M., Behrens, K., Rieger, A., Kumar, M., & Behrens, M.
(2015). Effects of breathing patterns and light exercise on linear
and nonlinear heart rate variability. Applied Physiology,Nutrition, and
Metabolism, 40(8), 762-768.
[4] JPorto, A. A., Tavares, B. S., Vidigal, G., Garner, D. M., Raimundo, R.
D., de Abreu, L. C.,...& Valenti, V. E. (2018). Nonlinear Dynamics of
Heart Rate During Slow Breathing Exercise. Indian J Physiol Pharmacol,
62(2), 160-169. International Journal of Interactive Multimedia and
Artiﬁcial Intelligence 3, 7 (2016), 87.
[5] Bernardi, L., Sleight, P., Bandinelli, G., Cencetti, S., Fattorini, L.,
Wdowczyc-Szulc, J., & Lagi, A. (2001). Effect of rosary prayer and
yoga mantras on autonomic cardiovascular rhythms: comparative study.
Bmj, 323(7327), 1446-1449.
[6] Yu, B., Feijs, L., Funk, M., & Hu, J. (2015). Designing auditory display
of heart rate variability in biofeedback context. Georgia Institute of
Technology.
[7] Doll, A., Hlzel, B. K., Bratec, S. M., Boucard, C. C., Xie, X.,
Wohlschlger, A. M., & Sorg, C. (2016). Mindful attention to breath
regulates emotions via increased amygdalaprefrontal cortex connectivity.
Neuroimage, 134, 305-313.
[8] Bahameish, M. (2019, April). Can Changes in Heart Rate Variability
Represented in Sound be Identiﬁed by Non-Medical Experts?. In Ex-
tended Abstracts of the 2019 CHI Conference on Human Factors in
Computing Systems (p. SRC01). ACM.
[9] Dubus, G., & Bresin, R. (2013). A systematic review of mapping
strategies for the soniﬁcation of physical quantities. PloS one, 8(12),
e82491.
[10] Blanco, A., Lorena, A., Grautoff, S., & Hermann, T. (2018). Car-
dioSounds: A portable system to sonify ECG rhythm disturbances in
real-time. Georgia Institute of Technology.
[11] Ballora, M., Pennycook, B., Ivanov, P. C., Glass, L., & Goldberger, A.
L. (2004). Heart rate soniﬁcation: A new approach to medical diagnosis.
Leonardo, 37(1), 41-46.
[12] Borthakur, D., Peltier, A., Dubey, H., Gyllinsky, J., & Mankodiya,
K. (2018, September). SmartEAR: Smartwatch-based Unsupervised
Learning for Multi-modal Signal Analysis in Opportunistic Sensing
Framework. In 2018 IEEE/ACM International Conference on Connected
Health: Applications, Systems and Engineering Technologies (CHASE)
(pp. 75-80). IEEE.
[13] Zheng, B. S., Murugappan, M., & Yaacob, S. (2013, April). FCM
clustering of emotional stress using ECG features. In 2013 International
Conference on Communication and Signal Processing (pp. 305-309).
IEEE.
[14] Peng C-K, Mietus JE, Liu Y, Khalsa G, Douglas PS, Benson H, Gold-
berger AL. Exaggerated Heart Rate Oscillations During Two Meditation
Techniques. International Journal of Cardiology 70:101-107, 1999.
[15] Behar J. A., Rosenberg A. A. et al. (2018) PhysioZoo: a novel open
access platform for heart rate variability analysis of mammalian elec-
trocardiographic data. Frontiers in Physiology
[16] R Core Team (2017). R: A language and environment forstatistical
computing. R Foundation for Statistical Computing, Vienna, Austria.
URL https://www.R-project.org/
[17] Jovanov, E. (2006, January). On spectral analysis of heart rate vari-
ability during very slow yogic breathing. In 2005 IEEE Engineering in
Medicine and Biology 27th Annual Conference (pp. 2467-2470). IEEE.
[18] Csounds.com. (2019). Appendix D. Formant Values. [online] Available
at: http://csounds.com/manual/html/MiscFormants.html.
[19] Sound eXchange: HomePage. (n.d.). Retrieved August 3, 2019, from
http://sox.sourceforge.net/l.
[20] Sahoo, A. K., Pradhan, C., Barik, R. K., & Dubey, H. (2019). DeepReco:
Deep Learning Based Health Recommender System Using Collaborative
Filtering. Computation, 7(2), 25.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
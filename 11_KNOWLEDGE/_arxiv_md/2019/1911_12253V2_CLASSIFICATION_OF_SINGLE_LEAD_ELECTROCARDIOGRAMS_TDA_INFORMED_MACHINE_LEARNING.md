---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1911.12253v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1911.12253v2_Classification_of_Single-lead_Electrocardiograms__TDA_Informed_Machine_Learning

> Source: 1911.12253v2_Classification_of_Single-lead_Electrocardiograms__TDA_Informed_Machine_Learning.pdf

> Pages: 6

---


## Page 1


Classiﬁcation of Single-lead Electrocardiograms:
TDA Informed Machine Learning
Christopher Dunstan
University of Maryland Baltimore County
Baltimore, MD, USA
cdun2@umbc.edu
Esteban Escobar
California Polytechnic State University Pomona
Pomona, CA, USA
estebane@cpp.edu.edu
Paul Samuel Ignacio
University of the Philippines Baguio
Baguio City, Philippines
ppignacio@up.edu.ph
Luke Trujillo
Harvey Mudd College
Claremont, CA, USA
ltrujillo@g.hmc.edu
David Uminsky
University of San Francisco
San Francisco, CA, USA
duminsky@usfca.edu
Abstract—Atrial Fibrillation is a heart condition characterized
by erratic heart rhythms caused by chaotic propagation of
electrical impulses in the atria, leading to numerous health com-
plications. State-of-the-art models employ complex algorithms
that extract expert-informed features to improve diagnosis. In
this note, we demonstrate how topological features can be used to
help accurately classify single lead electrocardiograms. Via delay
embeddings, we map electrocardiograms onto high-dimensional
point-clouds that convert periodic signals to algebraically com-
putable topological signatures. We derive features from persistent
signatures, input them to a simple machine learning algorithm,
and benchmark its performance against winning entries in the
2017 Physionet Computing in Cardiology Challenge.
Index Terms—Topological data analysis, time series classiﬁca-
tion, machine learning.
I. INTRODUCTION
Cardiac arrhythmia, or abnormal heart rhythm, is the most
prevalent heart disorder that encompasses a wide array of
conditions from heart rate abnormalities (like Bradycardia and
Tachycardia), to premature heartbeats, and erratic rhythms.
Among these, Atrial Fibrillation (AFib) is the most common,
affecting 33.5 million people worldwide in 2010 (Chugh et al.
[3]). AFib is characterized by erratic heart rhythms caused by
chaotic propagation of electrical impulses in the atria. This
triggers atrial spasms and irregular opening and premature
closing of the atrioventricular valves, resulting in an increased
risk of clot formation, and in the extreme case, stroke.
An electrocardiogram (ECG or EKG) is the main tool that
medical professionals use to diagnose AFib, measuring electric
activity in the heart at different stages of the cardiac cycle.
Central to the analysis of ECG measurements is the PQRST
complex, an important slice of an ECG reading composed of a
series of wave patterns that mark speciﬁc events in the cardiac
rhythm. There is much existing literature on the analysis of
speciﬁc features in the PQRST complex and other parts of
a standard 12-lead ECG recording that help in the diagnosis
of many heart conditions. In particular, state-of-the-art mod-
els employ advanced algorithms that extract expert-informed
features from the PQRST complex to diagnose AFib, and a
large majority of these focus on two features: the P waves
and the RR intervals. P waves record atrial depolarization and
correspond to electrical activity in the atria prior to transfer of
blood to the ventricles, whereas RR intervals measure the time
between the peaks of ventricular depolarization, the cardiac
event corresponding to the ventricles pumping the blood out
of the heart. Because electrical impulses in the atria are in
chaos, clear P waves tend to be absent in ECG readings of
people with AFib, and ventricular activity become irregular
causing the RR intervals to be highly variable. These two
features demonstrate how speciﬁc (i.e. local) landmarks in the
structure of an ECG reading can be used to examine tell-tale
signs of abnormal cardiac activity.
In this paper, we explore whether the local and global
topology of ECG readings, paired with minimal medical
knowledge, could be utilized to aid in the diagnosis of AFib.
Our goal is to provide experimental answer to the following
question: Is there signal in the topological features of ECG
readings in diagnosing Atrial Fibrillation? This query is
important as it explores the call for increased collaboration
between theoretical focus and advances of topologists and the
medical researchers.
A. Pipeline
Our approach consists of four stages: ECG cleanup, point
cloud generation, topological feature extraction, and classiﬁ-
cation via random forest.
Integral to our objective of detecting signal from the topol-
ogy of ECG readings as time series is to mitigate the effects of
measurement error and noise. We implement a simple signal
frequency-based approach in extracting the longest and “clean-
est” portion of an ECG recording. We then transform each time
series as a point cloud in high-dimensional space and examine
its topological features using novel tools from topological data
analysis. This step assigns to each point cloud a distance-
parameterized summary of its evolving topological features.
Finally, we derive statistical features from this summary to
train a simple random forest classiﬁer.
arXiv:1911.12253v2  [q-bio.QM]  28 Nov 2019


## Page 2


Fig. 1. The pipeline of our topology-based classiﬁcation of ECG readings.
It is worth noting that the idea of studying the topology of
high-dimensional point-clouds as embeddings of time series
data is fairly recent and has been explored in several applica-
tions. The basic difference among these applications is on the
treatment of the computed features. Perea et al. [13] used the
most signiﬁcant 1-dimensional topological signature from the
summary to score periodicity in gene expression time series
data. Seversky et al. [15] also followed the same pipeline,
but used metrics and kernels on the space of topological
summaries to study classiﬁcation of time series data. Finally,
Umeda [18] introduced a variation of the output topological
summary compatible as input to Convolutional Neural Net-
works for classifying volatile time series.
B. The Data
In 2017, Physionet and Computing in Cardiology launched
a challenge to develop algorithms able to classify single lead
electrocardiogram readings ranging in length from 9 to 60
seconds into four categories: normal sinus rhythm, AFib, other
sinus rhythm, or noisy. A total of 12,186 electrocardiogram
recordings, donated by AliveCor (www.alivecor.com), split
into a training set (8,528) and a hidden test set (3,658)
were used in the challenge. Initial labeling of the released
training set follows a distribution of 60.4% normal, 9% AFib,
30% other rhythms, and 0.5% noisy. This distribution is later
revised to 59.5% normal, 8.9% AFib, 28.3% other rhythms,
and 3.3% noisy following a re-labeling step due to inter-
expert disagreement on a signiﬁcant fraction of the labels
— a testament to the challenge’s difﬁculty and the existing
disagreements in real practice. A comprehensive report on the
challenge is provided by the organizers (Clifford et al. [4]).
We utilize the data set used in this challenge with the ﬁnal
labeling information.
II. METHODS
A. Noise Removal
We adapt the strategy for noise clean up from Datta et al.
[6] to our approach. The spectogram of each ECG reading
is computed and portions along the time axis with spectral
power above 50 Hz are cut-off. This produces segments of the
original ECG reading sanitized from extreme noise (literature
pegs important cardiac information to be within 20 Hz) caused
by measurement irregularities. We use the ﬁrst 3000 time
points of the longest clean segment when possible, otherwise
we use the ﬁrst 3000 time points of the original ECG reading.
B. Sliding Window Embeddings
The method of converting time series data into point clouds
via sliding window embedding (or delay embedding) has been
explored in many types of applications. The general idea of
capturing rich local information within slices (i.e. windows)
of the time series, and recording them as vectors in high-
dimensional space circumvents many issues that come with
sampling within the time series given its discrete nature. It
also illuminates global structures of time series as artifacts of
the local dynamics, a powerful consequence of the famous em-
bedding theorems of Whitney [20] and Takens [17], provided
parameters are chosen appropriately. Furthermore, it has been
shown that this technique increases precision of parameter
estimates for modeling variability in recurring phenomenon
for time-dependent data (von Oertzen and Boker [19]).
The embedding process begins by selecting a window size
w and embedding dimension d. These two respectively control
the scope and resolution at which local dynamics will be
observed. A window of length w corresponding to the starting
w time units of the time series is ﬁrst considered from which d
time point measurements are extracted. These d measurements
together deﬁne a vector in Rd, and is the ﬁrst element in
the point-cloud embedding. The window then slides at step
size τ, and the process is repeated, mapping the next window
to another vector in the high-dimensional space (see ﬁrst
time series in Figure 2). One advantage of this approach is
that the topological features of the embedded space remain
invariant under inversion, i.e. ﬂipping upside down (see third
time series in Figure 2), of the time series, bypassing the
problem of identifying whether or not an ECG reading is
inverted — an existent issue in the data set. It is clear that
changing the window size and/or the embedding dimension
would drastically alter the resulting embedded structure (see
second time series in Figure 2), prompting a careful selection
of these input parameters in our analysis of the ECG readings.
We now discuss these choices.
An ECG reading is naturally periodic, mimicking the
cardiac cycle. The embedding process converts the periodic
patterns present in the time series to attractor cycles in the
high-dimensional point-cloud. For ECG readings, this pattern
pertains to the PQRST complex, suggesting that parameters
must be chosen to capture local dynamics within and around it.
Furthermore, in view of the succeeding stage in our approach,
we also would like that the resulting point-cloud be as “round”
as possible to maximize the diameter of the resulting cycle
attractors. This has been shown to hold when the window size
is chosen to be as close as possible to the period of the pattern


## Page 3


Fig. 2. Multi-dimensional scaling to R3 of the high-dimensional point clouds
generated from delay embeddings with varying window sizes (respectively
100, 35, and 100 time units). Here, the embedding dimensions are set equal
to the window sizes and the delay parameter τ is set to 1. Projection to R3
is only used for visualization.
(Perea and Harer [14]). After close inspection of the ECG
readings, we determine that this is approximately 250 ms.
For the embedding dimension, we select the optimal choice
based on computational efﬁciency and stability of the resulting
topological summary, that is, we choose the embedding dimen-
sion producing a topological summary that is most similar to
those with neighboring dimensions. We compare topological
summaries using the bottleneck distance, a standard metric
used in topological data analysis that measures the cost of
tranforming one topological summary to another, and is central
to the discussion on stability of the output summaries under
slight perturbation of data [5]. Figure 3 shows the boxplots of
the bottleneck distances between paired topological summaries
from neighboring dimensions. We maintain a balance between
selecting bottleneck differences that are not too spread while
accounting for sparsity of points in the embedded point cloud
since a dimension that is too low selects too few points
from the window and too high produces very expensive
computations.
Fig. 3.
Boxplots of bottleneck distances between paired barcodes from
neighboring embedding dimensions. Examination of boxplot number 10
suggests an optimal embedding dimension of 50.
C. Feature Extraction via Persistent Homology
To each point cloud, we apply a tool from topological data
analysis known as persistent homology to extract evolving
topological features. This is a relatively new approach in data
analysis that has been growing in popularity because of its
novel treatment of data as topological objects, and has been
applied to a wide array of data sets including images [2], brain
data [9], [16], migration data [8], and recently, time series
[14], [15]. In this section, we discuss the fundamental ideas
of this approach, and provide insights as to the meaning of
computable topological signatures in time series data. For a
more in-depth introduction to persistent homology, we refer
the interested reader to [11], [12], [21].
To start, given a ﬁxed threshold ε, we endow the point
cloud with a Vietoris-Rips Complex structure by treating as n-
dimensional objects a collection {p0, p1, ..., pn} of n+1 points
(called an n-simplex) whenever d(pi, pj) ≤ε for all pairs
0 ≤i, j ≤n, where d is a deﬁned metric in the ambient space
(see [1], [11] for a more detailed description of the Vietoris-
Rips Complex). For our point cloud embeddings generated
from sliding windows, the points live in R50 and the metric is
the Euclidean distance. A way to visualize these objects is to
consider a 0-simplex {pi} as a point, a 1-simplex {pi, pj} as an
edge through pi and pj, a 2-simplex {pi, pj, pk} as a triangle
having pi, pj, and pk as vertices, and so on. This allows
one to view the point cloud as a collection of mathematical
pieces, called Vector Spaces, Λ0, Λ1, Λ2, ..., Λn, ... where each
Λi is built up from the i-dimensional simplices and related
by maps ∂n : Λn →Λn−1 sending a n-dimensional object
σn ∈Λn to its boundary ∂n(σn) ∈Λn−1. This construction
further generates abstract algebraic objects, called homology
groups, whose signatures (Betti numbers) β0, β1, ... encode
topological information about the underlying point cloud: β0
counts connected components, β1 loops or holes, β2 voids,
and so on. These are the features that we are interested in. The
reader may consult standard references in algebraic topology
such as [7], [10] for a thorough exposition on these ideas.
There is, however, one caveat: the signatures that homology
captures depend on the simplicial structure constructed via
a choice for the threshold ε. From this, a natural question
arises: how must ε be chosen? A solution that topological
data analysis proposes circumvents this by instead considering
a sequence of simplicial structures induced by increasing
the threshold parameter ε, and keeping track of topological
features that survive as ε varies. This process then records
the evolution of topological features of the point cloud and
is the main idea of persistent homology. The topological
features detected by persistent homology are recorded in a
summary called a persistence barcode (see Figure 4), showing
the lifetime of a detected feature and its relative signiﬁcance
with respect to all features detected — in persistent homology,
long bars represent signiﬁcant features while short bars detect
noise.
For non-geometric data, it can be a challenge to interpret
what kind of information topological features reveal. However,


## Page 4


●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
●
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
1.1
1.2
Fig. 4.
The persistence barcode of a point cloud sampled from a cardioid
superimposed with simplicial complexes and the correspoding Betti numbers
at different thresholds.
in our setting, these features have clear meaning. For the 1-
dimensional case, the features represent cycles in the point
cloud induced from sliding window embeddings. Since cycle
attractors in this point cloud correspond to periodic patterns
in the corresponding time series, the 1-dimensional features
detect periodic information about the original time series. This
observation is the basis for the SW1PerS algorithm proposed
by Perea et al. [13] for scoring periodicity in time series data.
To examine if these topological features contain signal for
ECG diagnosis, we derive simple statistical summaries from
the features based on the barcode of each ECG. Table I
summarizes those that are found to improve the accuracy
of the random forest when included in the feature set. The
summary measures in this table follow the standard deﬁnitions
in Statistics: Mean refers to the arithmetic average, Standard
Deviation (SD) measures the spread of the values around the
mean, Skewness quantiﬁes the symmetry or asymmetry of a
set of values, Kurtosis measures the weight of the tails of the
distribution relative to the center, and Sum refers to the total.
In addition to these features, three others were included
namely, the ratio of the length of the longest clean segment
of the ECG with respect to the original length, and the mean
and standard deviation of dimension 0 persistence obtained
by ﬁltering the ECG time series, considered as functions, via
super-level sets.
D. Random Forest
Once the feature set is extracted using persistent homology,
we input this set into a random forest, an ensemble of decision
trees each using a randomized set of features to decide the
classiﬁcation of an object. The idea is that if topological
features are preserved within ECGs of the same type, then
the random forest will learn about these intra-class descriptors
and use these as basis to provide a good classiﬁcation for a
previously unseen ECG.
TABLE I
STATISTICAL FEATURES FROM BARCODES
Barcode Feature
Mean
SD
Skewness
Kurtosis
Sum
Dimension 0
Death
✓
✓
✓
Dimension 0∗
Death
✓
✓
✓
Dimension 1
Birth
✓
✓
Death
✓
Persistence
✓
✓
Dimension 1∗
Persistence
✓
✓
Dimension 2
Birth
✓
Death
✓
Dimension 2∗
Birth
✓
∗These bars do not include the 5% most persistent bars.
To examine if these topological features contain useful
information for ECG diagnosis, we set up two random forest
models. Since the hidden test set from the Physionet Challenge
was never released, we extract a test set of 1000 ECG readings
proportionally chosen randomly within each class to reproduce
the same distribution as the competition test set. We then
bootstrap the remaining ECGs for training to recover a training
set of comparable size to the original competition training
set. The ﬁrst model is trained using four statistical features
based on the RR intervals — a known good differentiator of
ECG readings. In addition to these four features, the second
model includes the other statistical features derived from the
barcodes. Both models are given the same training and test
set. We perform this approach 100 times, each time changing
both the training and test set and recording the classiﬁcation
scores based on the Physionet Challenge metric
F1 = (F1a + F1n + F1o)/3
where each of the scores F1a, F1n, and F1o are computed
using the formula
F1a = 2Aa/(ΣA + Σa),
F1n = 2Nn/(ΣN + Σn),
F1o = 2Oo/(ΣO + Σo)
according to the table below:
TABLE II
TABLE OF VALUES USED FOR THE F1 SCORE FORMULA
Predicted Classiﬁcation
AFib
Normal
Others
Noisy
Total
Aﬁb
Aa
An
Ao
Ap
ΣA
Normal
Na
Nn
No
Np
ΣN
Others
Oa
On
Oo
Op
ΣO
Noisy
Pa
Pn
Po
Pp
ΣP
Total
Σa
Σn
Σo
Σp
Finally, a paired t-test is performed to examine if the
differences in classiﬁcation scores when topological features


## Page 5


are included in the feature set are signiﬁcant (as opposed to
just the four basic RR interval features).
III. RESULTS AND DISCUSSIONS
Table III shows the ﬁnal F1 scores of the two random forest
models. For comparison, we include the scores of the winning
models in the Physionet Challenge. The scores for validation
come from validation set of 300 ECG readings prepared by
the Physionet Challenge. It must be pointed out that the test
set used for our random forest models are only about one-
third in size of the hidden test set from the challenge but has
the same distribution. Moreover, since our test set is set aside
from the training set, it also means that the training set used
by the forests are reduced in size of distinct ECG readings
(across classes) by the same amount.
TABLE III
FINAL F SCORES OF DIFFERENT MODELS
Model
No. of Features
Train
Validation
Test∗
Teijeirio et al.
86
0.893
0.912
0.831
Datta et al.
150
0.970
0.990
0.829
Zabihi et al.
150
0.951
0.968
0.826
Hong et al.
622
0.970
0.990
0.825
RF w. RR Features
4
0.926
0.920
0.684
RF w. RR & TDA
23
0.997
0.975
0.722
∗The test sets used by the two random forest models in each of the 100
cycles of training and testing are comparable to each other but not with the
hidden test set used by the ﬁrst four models from the Physionet Challenge.
We highlight that with just twenty-three features, most
of which are statistics from the persistence barcodes, the
random forest model already performs relatively well with
respect to the winning models. It is worth noting that all the
winning models from the Physionet Challenge used features
based on the RR intervals, and that just the four statistical
features from the RR intervals already account for a signiﬁcant
portion of the F1 scores. In addition, most of the features
used by the winning highly tuned models (some include deep
learning algorithms) are engineered based on features known
to be helpful in diagnosing AFib and either employ advanced
algorithms for extraction or medical expertise for processing.
On the other hand, we purposely did not ﬁne tune our model as
we wanted to focus on whether or not there was any noticeable
increase using TDA-based features.
Table IV provides a more detailed summary of the random
forest model’s performance across classes. Here, we see that
features from the RR intervals are the main drivers of accuracy
for all models, and that topology-based features consistently
increase the accuracy across classes. More importantly, per-
forming a paired one-tailed t-test at α = 0.05 between the
class F1 scores of the two random forests reveals that these
increases in F1 scores across classes are signiﬁcant (see Table
V).
ACKNOWLEDGMENT
We are grateful to the Mathematical Sciences Research
Institute for providing the best environment for research col-
laboration. We also would like to acknowledge the NSF (DMS-
TABLE IV
F1 CLASS SCORES OF DIFFERENT MODELS
Model
F1a
F1n
F1o
Teijeirio et al.
0.854
0.903
0.737
Datta et al.
0.823
0.916
0.750
Zabihi et al.
0.835
0.909
0.734
Hong et al.
0.823
0.912
0.751
RF w. RR Features
0.649
0.867
0.536
RF w. RR & TDA
0.688
0.896
0.580
TABLE V
SIGNIFICANT INCREASE IN F1 SCORES BETWEEN THE TWO RANDOM
FOREST MODELS
F1a
F1n
F1o
F1p
F1
Signiﬁcant Increase (%)
3.46
2.69
3.87
8.6
3.43
p value
0.049
0.042
0.049
0.048
0.044
1659138), the NSA (H98230-18-1-0008), and the Sloan Foun-
dation (G-2017-9876) for providing the grants that allowed us
to complete the project. Author DU was partially supported by
the Wicklow AI and Medical Research Initiative (WAMRI).
REFERENCES
[1] Attali, D., Lieutier, A., Salinas, D., (2013), Vietoris-Rips complexes
also provide topologically correct reconstructions of sampled shapes,
Computational Geometry, 46(4), pp. 448-465
[2] Carlsson, G.,Ishkhanov, T., de Silva, V., Zomorodian, A., “On the local
behavior of spaces of natural images”, Int. J. Comput. Vis., 76(1), pp
1-12
[3] Chugh, S., Havmoeller, R., Narayanan, K., Singh, D., Rienstra, M.,
Benjamin, E., Gillum, R., Kim, Y., McAnulty, J., Zheng, Z., Forouzanfar,
M., Naghavi, M., Mensah, G., Ezzati, M. and Murray, C. (2014).
Worldwide Epidemiology of Atrial Fibrillation. Circulation, 129(8),
pp.837-847.
[4] Clifford, G., Liu, C., Moody, B., Lehman, L., Silva, I., Li, Q., Johnson,
A., Mark, R., (2017), AF Classiﬁcation from a Short Single Lead ECG
Recording: the PhysioNet/Computing in Cardiology Challenge 2017. In:
Computing in Cardiology 2017. [online] Rennes: IEEE, 065-469. Avail-
able at: http://www.cinc.org/archives/2017/pdf/065-469.pdf [Accessed
01 07 2018].
[5] Cohen-Steiner, D., Edelsbrunner, H., Harer, J., (2007), Stability of
Persistence Diagrams, Discrete and Computational Geometry, 37, pp.
103-120
[6] Datta, S., Puri, C., Mukherjee, A., Banerjee, R., Choudhury, A.D.,
Singh, R., Ukil, A., Bandyopadhyay, S., Pal, A., Khandelwal, S., (2017)
“dentifying normal, AF and other abnormal ECG rhythms using a
cascaded binary classiﬁer,” 2017 Computing in Cardiology (CinC),
Rennes, pp. 1-4. doi: 10.22489/CinC.2017.173-154
[7] Hatcher, A. (2002), Algebraic Topology, Cambridge University Press
[8] Ignacio, P.S., Darcy, I.K. (2019), “Tracing Patterns and Shapes in
Remittance and Migration Networks via Persistent Homology”, EPJ
Data Science, 8(1)
[9] Levi, R., Hess, K., Dlotko, P., Markram, H., Scolamiero, M., Turner, K.,
Nolte, M., Reimann, M., Chindemi, G., Perrin, R. (2017), “Cliques of
Neurons Bound into Cavities Provide a Missing Link between Structure
and Function,” Frontiers in Computational Neuroscience, 11
[10] Munkres, J., (1984), Elements of algebraic topology, Volume 7, Addison-
Wesley Reading
[11] Otter, N., Porter, M., Tillmann, U., Grindrod, P., and Harrington, H.
(2017), “A roadmap for the computation of persistent homology”, EPJ
Data Science, 6 (17)
[12] Patania, A., Vaccarino, F., Petri, G., (2017), “Topological Analysis of
Data,” EPJ Data Science, 6(7)
[13] Perea, J., Deckard, A., Haase, S., Harer, J. (2015), SW1PerS: Sliding
windows and 1-persistence scoring; discovering periodicity in gene
expression time series data. BMC Bioinformatics, 16:257, pp.1-12


## Page 6


[14] Perea, J., & Harer, J. (2015), Sliding Windows and Persistence: An
Application of Topological Methods to Signal Analysis. Foundations of
Computational Mathematics, 15(3), pp.799-838
[15] Seversky, L., Davis, S., Berger, M. (2016). On Time-Series Topological
Data Analysis: New Data and Opportunities. In: IEEE Conference on
Computer Vision and Pattern Recognition Workshops (CVPRW), Las
Vegas, pp. 1014-1022. doi: 10.1109/CVPRW.2016.131
[16] Singh, G., M´emoli, F., Ishkhanov, T., Sapiro, G., Carlsson, G., Ringach,
D., (2008), “Topological analysis of population activity in visual cortex,”
j., Vis., 8(11).
[17] Takens, F (1985). Detecting strange attractors in turbulence. In: Dold
A, Eckman B, editors. Lecture notes in mathematics 1125: Dynamical
systems and bifurcations. pp. 99-106.
[18] Umeda, Y. (2017), Time Series Classiﬁcation via Topological Data
Analysis. Transactions of the Japanese Society for Artiﬁcial Intelligence,
32(3), D-G72-1-12
[19] von Oertzen, T., & Boker, S. M. (2010), Time Delay Embedding
Increases Estimation Precision of Models of Intraindividual Variability.
Psychometrika, 75(1), 158-175.
[20] Whitney, H. (1936), Differentiable manifolds. Annals of Mathematics
37, pp.645-680.
[21] Zomorodian, A., Carlsson, G. (2005) “Computing Persistent Homology,”
Discrete & Computational Geometry, 33(2), pp. 249-274

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
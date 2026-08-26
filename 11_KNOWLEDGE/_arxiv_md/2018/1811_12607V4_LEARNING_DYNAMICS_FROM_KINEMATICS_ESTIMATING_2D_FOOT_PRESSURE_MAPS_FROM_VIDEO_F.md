---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1811.12607v4
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1811.12607v4_Learning_Dynamics_from_Kinematics__Estimating_2D_Foot_Pressure_Maps_from_Video_F

> Source: 1811.12607v4_Learning_Dynamics_from_Kinematics__Estimating_2D_Foot_Pressure_Maps_from_Video_F.pdf

> Pages: 14

---


## Page 1


Learning Dynamics from Kinematics:
Estimating 2D Foot Pressure Maps from Video Frames
Christopher Funk1,3∗, Savinay Nagendra1∗, Jesse Scott1∗, Bharadwaj Ravichandran1,
John H. Challis2, Robert T. Collins1, Yanxi Liu1
1School of Electrical Engineering and Computer Science.
2Biomechanics Laboratory.
The Pennsylvania State University, University Park, PA 16802 USA
3Kitware, Inc
christopher.funk@kitware.com, sxn265@psu.edu, jescott@cse.psu.edu, bzr49@psu.edu,
jhc10@psu.edu, rcollins@cse.psu.edu, yanxi@cse.psu.edu
Abstract
Pose stability analysis is the key to understanding lo-
comotion and control of body equilibrium, with applica-
tions in numerous ﬁelds such as kinesiology, medicine, and
robotics. In biomechanics, Center of Pressure (CoP) is used
in studies of human postural control and gait. We propose
and validate a novel approach to learn CoP from pose of a
human body to aid stability analysis. More speciﬁcally, we
propose an end-to-end deep learning architecture to regress
foot pressure heatmaps, and hence the CoP locations, from
2D human pose derived from video. We have collected a set
of long (5min +) choreographed Taiji (Tai Chi) sequences
of multiple subjects with synchronized foot pressure and
video data. The derived human pose data and correspond-
ing foot pressure maps are used jointly in training a convo-
lutional neural network with residual architecture, named
PressNET. Cross-subject validation results show promis-
ing performance of PressNET, signiﬁcantly outperforming
the baseline method of K-Nearest Neighbors. Furthermore,
we demonstrate that our computation of center of pres-
sure (CoP) from PressNET is not only signiﬁcantly more
accurate than those obtained from the baseline approach
but also meets the expectations of corresponding lab-based
measurements of stability studies in kinesiology.
1. Introduction
In the realm of health and sports, precise and quantita-
tive digital recording and analysis of human motion provide
rich content for performance characterization and training,
health status assessment, and diagnosis or preventive ther-
apy of neurodegenerative syndromes. Analysis of gait and
∗Contributed equally, order chosen alphabetically
Figure 1. Our proposed PressNET network learns to predict a foot
pressure heatmap from 2D human body joints extracted from a
video frame using OpenPose [10]. The blue layers signify residual
layers, the red layers signify fully connected layers.
control of balance/equilibrium has received increasing in-
terest from the research community [40, 41, 54] as a way to
study the complex mechanisms of the human postural sys-
tem for maintaining stable pose. Stability analysis has a
wide range of applications in the ﬁelds of Healthcare, Kine-
siology and Robotics to understand locomotion and repli-
cate human body movements. Understanding body dynam-
ics, such as foot pressure, is essential to study the effects of
perturbations caused by external forces and torques on the
human postural system, which changes body equilibrium in
static posture as well as during locomotion [55].
We have chosen 24-form simpliﬁed Taiji Quan [53] as
a testbed for validating our computer vision and machine
learning algorithms. Taiji was selected because it is low-
cost, hands-free, and slow-motion sequence while contain-
ing complex body poses and movements. Taiji is practiced
worldwide by millions of people of all genders, races, and
ages. Each routine lasts about 5 minutes and consists of
controlled choreographed movements where the subject at-
1
arXiv:1811.12607v4  [cs.CV]  28 May 2019


## Page 2


tempts to remain balanced and stable at all times.
We explore an end-to-end deep learning approach called
PressNET (Figure 1) to transform kinematics (body pose)
to dynamics (foot pressure), and to obtain Center of Pres-
sure (CoP) locations from the regressed foot pressure. In
order to achieve this goal, we have created the largest hu-
man motion sequence dataset of synchronized video and
foot pressure data, with a total of over 700k frames (Figure
2). We represent foot pressure by an intensity heatmap that
provides the distribution of pressure applied by different
points of the foot against the ground, measured in kilopas-
cals (kPa) over discretized foot sole locations. Body pose
is represented by 2D human joint locations extracted using
the Openpose [10] Body25 model on the video frames. We
record video and foot pressure maps simultaneously so that
there is a foot pressure map for both feet corresponding to
each video frame.
Current computer vision research focuses mainly on ex-
tracting skeletal kinematics from videos, using body pose
estimation and tracking to infer pose in each frame as well
as the movement of body and limbs over time [3, 8, 10, 12,
13, 17, 35, 50]. However, little is known whether quan-
titative information about dynamics can be inferred from
single-view video. While body joints and their degrees of
freedom constrain the types of motion, it is the properties
Figure 2. Column 1: (A), Body25 joint set labeled by Open-
pose [10]. Column 2: (B1 to B4), Video data. Column 3: (C1
to C4), Corresponding Openpose detections showing the detected
skeleton joints used as input to PressNET. Column 4: (D1 to D4),
The corresponding measured left and right foot pressure maps.
and actions of the muscles and weight distributions, i.e.
body dynamics, that dictate the range of motion and speed
produced with these degrees of freedom. Consideration of
human body dynamics has been successful in explaining
performance in athletics, for example the triple jump [2]
and vertical jump [15]. Similarly, analysis of dynamics has
been used to show that strength is the limiting factor in the
ability of the elderly to rise from a chair [26], and to de-
termine the causes of stiff-knee gait in subjects with cere-
bral palsy [19]. An effective analysis of human movement
must take into account the dynamics of the human body, and
we seek an answer to the question: Can human motion dy-
namics be inferred from video sensors that are incapable of
observing muscle activations, physical loads, and external
forces directly?
In biomechanics, Center of Pressure (CoP), also called
Zero Moment Point (ZMP), is the point of application of the
ground reaction force vector at which the moment generated
due to gravity and inertia equals zero. Analysis of CoP is
common in studies on human postural control and gait. Pre-
vious studies have shown that foot pressure patterns can be
used to discriminate between walking subjects [38, 51]. In-
stability of the CoP of a standing person is an indication of
postural sway and thus a measure of a person’s ability to
maintain balance [23, 24, 28, 37]. Knowledge of CoP tra-
jectory during stance can elucidate possible foot pathology,
provide comparative effectiveness of foot orthotics, and al-
low for appropriate calculation of balance control and joint
kinetics during gait. CoP is usually measured directly by
force plates or insole foot pressure sensors.
We present a method to predict foot pressure heatmaps
directly from video. The major contributions and novelty of
this paper are: 1) Data: Creating the largest synchronized
video and foot pressure dataset ever recorded of a long com-
plex human movement sequence. 2) Method: Presenting a
novel deep convolutional residual architecture, PressNET,
which is the ﬁrst vision-based network to regress human
dynamics (foot pressure) from kinematics (body pose). 3)
Application: This is the ﬁrst work seeking to compute CoP
locations from video, yielding a key component for analy-
sis of human postural control and gait stability with applica-
tions in multiple ﬁelds such as kinesiology, biomechanics,
healthcare, and robotics.
2. Related Work
After the introduction of Deep Pose by Toshev et al. [50],
there was a paradigm shift in the ﬁeld of human pose esti-
mation from classical approaches to deep networks. The
idea of using heatmaps for ground truth data and visualiza-
tion in a human pose regression problem was introduced by
Tompson et al. [49], who also combine convolution layers
jointly with a graphical model to represent and learn spa-
tial relationships between joints. Many architectures use a
2


## Page 3


network based on Tompson’s approach [3, 8, 10, 12, 13, 17,
35, 50]. Stacked hourglass networks by Newell et al. [35]
compute pose estimates using heat map regression with re-
peated bottom-up, top-down inferencing. An hourglass net-
work, before stacking, is also similar to an encoder-decoder
architecture, where skip connections help in preserving spa-
tial coherence at each scale [18], and Encoder-Decoder ar-
chitectures have been extensively used for human pose esti-
mation. Having deep residual/skip connections to preserve
spatial information across multiple resolutions through the
network is essential for unsupervised/semi-supervised fea-
ture learning [25] and is a principle extensively used by
densely connected convolutional networks with feed for-
ward connections between convolution layers.
Success in 2D human pose estimation has encouraged
researchers to detect 3D skeletons from image/video by ex-
tending existing 2D human pose detectors [7, 11, 32, 33,
36, 45] or by directly using image features [1, 39, 44, 46,
57]. State-of-the-art methods for 3D human pose estima-
tion from 2D images have concentrated on deep systems.
Tome et al. [47] proposed an estimator that reasons about
2D and 3D estimation to improve both tasks.
Zhou et
al. [56] augmented a 2D estimator with a 3D depth regres-
sion sub-network. Martinez et al. [32] showed that given
high-quality 2D joint information, the process of lifting 2D
pose to 3D pose can be done efﬁciently using a relatively
simple deep feed-forward network.
All the papers discussed above concentrate on pose es-
timation by learning to infer joint angles or joint locations,
which can be broadly classiﬁed as learning basic kinematics
of a body skeleton. These methods do not delve into the ex-
ternal torques/forces exerted by the environment, balance,
or physical interaction of the body with the scene.
There have been many studies on human gait analy-
sis [4, 16, 29, 30] using qualitative approaches. Grimm et
al. [21] predict the pose of a patient using foot pressure
mats. Liu et al. [30] used frieze patterns to analyze gait
sequences. Although these are some insightful ways to ana-
lyze gait stability, there has been no deep learning approach
to tackle this problem. In [9], a depth regularization model
is trained to estimate dynamics of hand movement from 2D
joints obtained from RGB video cameras. Papers [5, 42, 43]
focus on stability analysis of 3D printed models. In this
paper, we aim to use a body’s kinematics to predict its dy-
namics and hence develop a quantitative method to analyze
human stability using foot pressure derived from video.
3. Our Approach
3.1. Data Collection
We present the ﬁrst tri-modal choreographed 24-Form
Taiji sequences data set of synchronized video, motion cap-
ture,and foot pressure data (Table 1). The subjects wear mo-
tion capture markers and insole foot pressure measurement
sensors while being recorded. Foot pressure sensor arrays,
connected to the Tekscan F-scan measurement system, are
inserted as insoles in the shoes of the subject during the
performance. Vicon Nexus software is used to spatiotem-
porally record motion capture and video data in hardware
while Tekscan F-scan software is used to simultaniously
record foot pressure sensor measurements that are then syn-
chronized to the other data post collection. Motion capture
data is not used in any of the experiments in this paper be-
cause:
1. We intend to create an end-to-end system to regress
foot pressure maps, and hence Center of Pressure lo-
cations, directly from video;
2. Video data collection is inexpensive and has very few
hardware requirements as compared to the cumber-
some process of motion capture data collection and
processing; and
3. There are multiple existing pose prediction networks
that can be used to extract 2D human body keypoints
directly from video, to use as input to our network.
3.1.1
Video and Pose Extraction
Raw video data is collected at 50 fps and processed us-
ing Vicon Nexus and FFmpeg to transcode to a com-
pressed video, with each video having its own spatiotem-
poral calibration.
Human pose predictions are extracted
from the compressed video using OpenPose [10]. Open-
Pose Body25 model uses non-parametric representations
called Part Afﬁnity Fields to regress joint positions and
body segment connections between the joints. The output
from OpenPose thus has 3 channels, (X, Y, conﬁdence), de-
noting the X and Y pixel coordinates and conﬁdence of pre-
diction for each of the 25 joints, making it an array of size
(25 × 3).
Figure 2 (A) shows the Body25 joints labeled by
OpenPose.
The 25 keypoints are {0:Nose,
1:Neck,
2:RShoulder, 3:RElbow, 4:RWrist, 5:LShoulder, 6:LEl-
bow, 7:LWrist, 8:MidHip, 9:RHip, 10:RKnee, 11:RAn-
kle, 12:LHip, 13:LKnee, 14:LAnkle, 15:REye, 16:LEye,
17:REar, 18:LEar, 19:LBigToe, 20:LSmallToe, 21:LHeel,
22:RBigToe, 23:RSmallToe, 24:RHeel}. Figure 2 (C and
D) portrays sample input-output pairs used to train our net-
work. The video frames of a subject performing 24-form
Taiji, shown in Figure 2 (B1 to B4), are processed through
the OpenPose network to extract 25 body joint locations
with respect to a ﬁxed coordinate axis. Figure 2 (C1 to
C4) shows the joints extracted from OpenPose. For train-
ing PressNET, we directly use arrays of 2D joint locations
as inputs. The conﬁdence of keypoints 15 to 18 (Eyes and
Ears) are zero for more than 50% of the video frames due
to occlusions.
3


## Page 4


Subject
Session
Take
# frames
Mean
Std
Median
Max
1
1
1
17995
3.73
11.14
3.67
282
2
17625
3.48
10.61
3.67
299
3
17705
3.29
10.34
3.21
219
2
1
17705
6.18
20.21
6.01
417
2
17355
5.75
19.18
5.55
476
3
17625
5.41
18.56
5.23
521
3
1
17580
5.40
19.69
5.26
617
2
17645
5.34
19.39
5.21
636
3
17685
5.35
19.47
5.15
582
2
1
1
13230
7.80
37.62
7.72
1000
2
13335
6.71
35.20
6.68
1000
3
9500
6.13
33.93
6.03
1000
2
1
14105
5.26
30.18
5.18
1000
2
6475
4.81
30.64
4.73
1000
3
13885
4.68
28.62
4.56
1000
4
12185
3.02
21.05
2.83
1000
3
1
5600
2.95
21.15
2.71
1000
2
6845
3.25
23.23
3.09
1000
3
12135
3.08
21.22
2.86
1000
4
8725
2.93
20.05
2.71
1000
3
1
1
11210
4.41
17.37
4.45
614
2
10605
3.88
15.39
3.91
614
3
11075
3.34
14.23
3.34
683
2
1
11295
6.17
28.09
6.15
1000
2
10700
5.69
26.88
5.67
1000
3
10945
5.19
25.53
5.26
1000
3
1
12410
5.80
30.57
5.59
1000
2
11805
5.31
28.58
5.18
1000
3
11950
5.49
28.95
5.48
1000
4
1
1
13115
7.37
24.76
7.40
679
2
13715
6.05
21.75
6.10
775
3
13015
5.25
20.07
5.27
650
2
1
15405
8.12
31.11
8.24
1000
2
14370
7.62
30.11
7.68
1000
3
9370
6.05
25.72
6.05
781
3
1
14340
8.05
35.20
8.05
1000
2
13685
7.60
32.50
7.66
1000
3
13675
7.45
32.15
7.57
1000
4
13015
7.38
32.69
7.46
1000
5
13045
7.27
31.52
7.26
1000
5
1
1
18000
6.85
25.81
6.95
1000
2
17300
6.83
25.81
6.90
1000
3
18005
7.49
28.11
7.58
1000
4
16750
8.18
30.21
8.26
1000
2
1
16545
8.06
32.01
7.84
1000
2
4000
8.39
32.42
8.40
1000
3
16910
8.94
34.47
8.60
1000
4
16440
9.63
37.12
9.34
1000
6
1
1
17395
6.79
30.20
6.78
887
2
16330
6.87
30.43
6.87
1000
3
15760
7.04
31.26
7.01
1000
4
15575
7.23
31.93
7.20
1000
5
15810
7.46
32.90
7.44
983
6
16095
7.61
33.54
7.60
1000
2
1
15520
6.39
27.98
6.30
764
2
15000
6.69
29.88
6.53
951
3
15200
6.87
30.38
6.70
979
4
15140
7.13
31.43
7.07
924
Table 1. Foot pressure data statistics showing number of frames,
mean, standard deviation, median, and maximum intensity of foot
pressure in kilopascals (kPa) per take and session for each subject.
As a results, we have a total of 794,035 video-foot pressure frame
pairs for training-testing.
Subject
Training Set
Validation Set
Test Set
1
569,815
65,300
158,920
2
603,755
74,260
116,020
3
622,835
69,205
101,995
4
582,555
64,730
146,750
5
603,075
67,010
123,950
6
572,590
63,620
157,825
Table 2. The number of training, validation, and test frames of
each train-test split for the leave one subject out segmentation of
the 794,035 frame dataset.
Subject
Total Frames
Weight (kg)
Height (m)
Gender
1
158,920
52
1.60
Female
2
116,020
67
1.72
Male
3
101,995
64
1.60
Female
4
146,750
77
1.70
Male
5
123,950
60
1.56
Female
6
157,825
55
1.54
Female
Table 3. Dataset statistics showing demographic information in-
cluding subject weight(kg), height(mm) and gender. We have 3
professionals (20+ years experience) and 3 amateurs (5-10 years
experience).
3.1.2
Foot Pressure
Foot pressure is collected at 100 fps using a Tekscan F-
Scan insole pressure measurement system (Figure 2 right
column). Each subject is provided a pair of canvas shoes
outﬁtted with cut-to-ﬁt capacitive pressure measurement in-
soles. Sensor noise ﬂoor is approximately 3 KPa. The foot
pressure heatmaps generated are 2-channel images of size
60 × 21 as shown in Figure 2 (D1 to D4), and synched with
the mocap data (and thus to the video).
3.1.3
Data Statistics
To justify the adequacy of our data set for a machine learn-
ing task, we make few initial data statistics observations.
Ultimately, our leave-one-subject-out cross validation ex-
perimental results provide a quantiﬁed validation of our
method and dataset used.
Table 1 provides complete information about the foot
pressure dataset. A "take" refers to >5 min long continu-
ous motion sequences. A "session" refers to a collection of
"takes". Each subject performs 2 to 3 sessions of 24-form
Taiji at an average of 3 takes per session, amounting to a
total of 794,035 frames of video-foot pressure paired data.
We have observed that:
• (1) Subject demographics: there is sufﬁcient demo-
graphics diversity in the subjects in terms of their gen-
der, age, weight, height and years of experience in Taiji
practice and professional levels (Table 3). The range
of experience in Taiji of our subjects varies from am-
ateurs (5-10 years) to professionals (20+ years). We
currently have 3 amateurs and 3 professionals in our
dataset.
4


## Page 5


Figure 3. Per body joint Kernel Density plots and 2D scatter plots of OpenPose [10] data for all subjects. The datapoints for different
subjects are represented with different colors. (Sub1 - Blue, Sub2 - Orange, Sub3 - Green, Sub4 - Red, Sub5 - Purple, Sub6 - Brown)
• (2) Body joint (from video) value statistical distribu-
tions: Figure 3 shows per feature kernel density plots
of joints extracted from the OpenPose network. These
distributions support the hypothesis that the subjects
are statistically similar.
• (3) Foot-pressure variation under the same pose: In
order to depict inter/intra-subject foot pressure covari-
ance information for the opening pose of 24-form Taiji,
Figure 4 (A) shows a color coded table. It can be ob-
served from Figure 4 (B) that the foot pressure maps
are visually different for the same pose, therefore es-
tablishing a lower bound on errors for estimating foot
pressure from a single pose. The learning system can-
not do better than this inherent difference.
• (4) PCA analysis: Figure 5 highlights the inter-subject
and intra-subject variance of foot pressure data via
PCA analysis.
The left portion of Figure 5 shows
the mean foot pressure for each individual subject on
the diagonal and the difference of means for pairs of
subjects off-diagonal, for all the subjects.
The dif-
ference of mean pressure highlights that each subject
has a unique pressure distribution relative to other sub-
jects. The right portion of Figure 5 highlights the top-
5 principal components of the foot pressure map data
for each subject, with the rows represent individual
subjects. From Figure 5 we can see that each princi-
pal component encodes different types of information
(variability in left/right foot pressure, in toe/heel pres-
sure, and so on), and that the collection of top PCs
encode similar modes of variation, although not in the
exact same order (for example, Subject 1’s 1st prin-
cipal component encodes pressure shifts between the
left and right foot, whereas, Subject 2’s 2nd principal
component encodes that information).
5


## Page 6


Figure 4. (A): Inter- and intra(yellow)- subject foot pressure mean absolute difference for the opening pose of 24-form Taiji. Rowwise
colors (Red, Green, Blue, Orange, Grey and Purple) represent information of Subjects 1, 2, 3, 4, 5, and 6 respectively (B): Opening pose
(video), extracted skeleton and corresponding foot pressure of the six subjects.
Figure 5. Left: Pairwise absolute difference between the mean foot pressure across all 6 subjects. Mean pressure is provided on diagonal
(yellow bounding box). Right: Top-5 Principal Components of Foot Pressure data per subject.
6


## Page 7


3.2. Network and Training
The design of our network is initially motivated by the
residual generator of the Improved Wasserstein GAN [22].
We use a generator-inspired architecture since our input is
1D and the output is a 2D heatmap. This design aids in
capturing information at different resolutions, acting like a
decoder network for feature extraction. The primary aim
of our network is to extract features without loss of spa-
tial information across different resolutions. We try to learn
the correlation between the pose, encoded as 25 joint lo-
cations, and the corresponding foot pressure map intensity
distribution. We train a Convolutional Residual architec-
ture, PressNET, to regress foot pressure distributions from a
given pose, over data from multiple subjects using a leave-
one-subject-out strategy. We do not use any discriminator
since ground truth data is available. Thus, this is formulated
as a supervised learning (regression) problem.
3.2.1
Data Pre-Processing
Input body pose data from openpose is an array of size
(25×3). We use hip joint as the center point to remove cam-
era speciﬁc offsets during video recording. The hip joint
is (0, 0) after centering and is removed from the training
and testing data sets. Data is normalized per body joint by
subtracting the feature’s mean and dividing by its standard
deviation, leading to a zero-mean, unit variance distribu-
tion. Zero conﬁdence (undetected) OpenPose joints are not
considered during normalization. Conﬁdence of joint de-
tections is then removed and not used for training. After
pre-processing and normalization, the input array is of size
(24 × 2), which is ﬂattened to a 1D vector of size (48 × 1)
and used as input to our network.
Foot pressure data, which is originally recorded in kilo-
pascals (kPa), has invalid prexels marked as Not a Num-
ber (NaN) representing regions outside the footmask. These
prexels are set to zero since the network library cannot train
with NaN values.
Any prexel values greater than 1000
kilopascals are clipped to 1000 to remove noise from the
dataset. Data is converted from kilopascals to PSI (Pounds
per Square Inch) by multiplying with a constant 0.145.
The dimension of a single cell in the insole sensor array
is (0.508cm × 0.508cm), thus having an area of 0.258cm2
or 0.039inch2. The data in PSI is multiplied by this sensor
area and divided by the weight of the subject reported in
Table 2. Thus, the foot pressure distribution is now weight-
normalized, unit-less and independent of the subject. Fur-
thermore, the data is normalized by dividing each prexel by
its max intensity in the distribution. The left and right nor-
malized foot pressure maps are concatenated as two chan-
nels of a resulting ground truth foot pressure heatmap of
size (60×21×2), with prexel intensities in the range [0, 1].
3.2.2
Network
The PressNET network is a feed forward Convolutional
Neural Network which inputs a 1D vector of joints and out-
puts a 2D foot pressure (Figure 1). The input layer is a
ﬂattened vector of joint coordinates of size 48×1 (24 joints
× 2 coordinates since the mid hip joint is removed), which
contains the kinematic information about a pose. The input
is processed through a fully connected layer with an out-
put dimension of 6144 × 1. This output is reshaped into an
image of size 4 × 3 with 512 channels. The network con-
tains four residual convolution blocks that perform nearest
neighbor upsampling. The ﬁrst block upsamples the input
by (2, 1) and the other three upsample by 2.
The residual block of PressNET, shown in Figure 6 Left,
has three parallel convolution layers with kernel sizes 5 × 5
and 3×3 and a residual 1×1. There is an additional parallel
fully connected layer, which takes the upsampled input and
returns a ﬂattened array of dimension equal to the output di-
mension of the residual block. This output is reshaped and
added to the output of the other three parallel layers to con-
stitute the output of the block. The number of channels of
each residual block is progressively halved as the resolution
doubles, starting at 512 channels and decreasing to 64.
The output of the ﬁnal residual block is split, ﬂattened
and sent to a convolutional branch and a fully connected
branch. The convolutional branch contains a 3 × 3 nor-
mal convolution layer to get a 2 channel output of shape
64 × 24 and cropped to size of the foot pressure map
(60 × 21 × 2). On the fully connected branch, the acti-
vations are run through multiple fully connected layers and
then reshaped to the size of the foot pressure map. The sizes
of the fully connected layers for PressNET are 10 and 2520
(Figure 6 Right). The output of these branches are added
together and then a foot pressure mask is applied to only
learn the valid parts of the data. Finally, a sigmoid activa-
tion is used to compress the output into the range [0,1]. The
convolutional branch serves to preserve spatial coherence
while the fully connected branch has a ﬁeld of view over
the entire prediction. With the combined spatial coherence
of the concurrent branch and fully connected layers in ev-
ery residual convolutional block, PressNET has ∼3 million
parameters.
All convolutional layers are separable convolution lay-
ers that split a kernel into two to perform depth-wise and
point-wise convolutions.
Separable convolutions reduce
the number of network parameters as well as increase
the accuracy [14].
Batch normalization [27] and spatial
dropouts [48] are applied after every convolution layer.
Leaky ReLU [31] is used as a common activation function
throughout the network, except the output layer.
7


## Page 8


Figure 6. Left: A residual block, one of the building blocks of PressNET network, upsamples the data and computes features. Right: Final
set of layers of PressNET include a fully connected layer layer and a concurrent branch to preserve spatial consistency.
3.2.3
Training Details
We evaluate our network on six splits of the dataset. Our
dataset is split by subject in a leave-one-subject-out cross-
validation. The validation data consists of the last take from
each subject used in the training data. The goal of this cross-
subject validation is to show how well this network gener-
alizes to an unseen individual. PressNET is trained with a
learning rate of 1e−3 for 20 epochs at a batch size of 32
for all splits on a NVIDIA Tesla P100 GPU cluster with
8GB of memory. Data pre-processing is carried out before
training as mentioned in Section 3.2.1. PressNET takes 3 to
3.5 hours to train on each split. The problem is formulated
as a regression with a sigmoid activation layer as the last
activation layer since the output data is in the range [0, 1].
A binary footmask having ones marked for valid prexels
and zeros marked for invalid prexels (produced by the foot
pressure capturing system) is element-wise multiplied in the
network. This enables the network to not have to learn the
approximate shape of the foot in the course of training and
solely learn foot pressure. The learning rate is reduced to
1e−5 after 12 epochs to ensure a decrease in validation loss
with training. Mean Squared Error (MSE) is used as the
loss function along with Adam Optimizer for supervision,
as we are learning the distribution of prexels [6].
4. Results
4.1. KNN Baseline
K-Nearest Neighbor (KNN) regression [6] has been em-
ployed as a baseline. For the KNN regression, the data is
temporally subsampled by a factor of 5. This is done to
decrease the search time required for the KNN algorithm,
without much information loss. The foot pressure data is
sampled at 100Hz, i.e., a frame of foot pressure is recorded
every 10 milliseconds. Since the data is sequential, picking
every other frame of training data does not affect the tem-
poral consistency of foot pressure data as the change in the
heatmaps in 20 milliseconds is negligible. Pre-processing
is carried out similar to training PressNET. The input pose
data is normalized by mean and standard deviation of in-
put, calculated using hip joint centered data by ignoring
zero conﬁdence values. The distance metric for the KNN
algorithm is calculated as the mean of the distances between
corresponding joints that do not have zero conﬁdence val-
ues. This distance d can be represented for two OpenPose
human pose detections (a and b) with conﬁdence ca for a
and cb for b and J joints by:
d(a, b) =
P
j∈J ∥(aj −bj)∥2
2 ∗δ
 ca
j cb
j > 0

P
j∈J δ
 ca
j cb
j > 0

+ ϵ
(1)
where δ is the Kronecker Delta which is 1 if the argument
is true and 0 if false, and a small ϵ avoids division by 0.
This enables KNN to adapt to missing joint detections in the
8


## Page 9


Figure 7. Overview of concepts in stability. Depiction of the com-
ponents of stability CoP, CoM, and BoS as well as the relation of
those components to stability metrics.
human pose predictions. The KNN algorithm with K=1 is
applied to all the six leave-one-subject-out splits. For each
pose in the test split, which consists of data from any one
subject, the corresponding “nearest” pose is picked from
the training split consisting of data from the other ﬁve sub-
jects. The foot pressure map corresponding to this nearest
neighbor is the prediction for the input pose in the train-
ing split. KNN with K=1 is a natural choice as a baseline
because of the reasonable intuition/assumption that similar
poses may lead to similar foot pressures. In our Leave-One-
Out setting, KNN provides a measure of similarity between
two poses of different subjects, thus establishing an upper-
bound on foot pressure errors inherent in the dataset.
4.2. Stability
A major motivation for computing foot pressure maps
from video is the application to stability analysis. Funda-
mental concepts used in stability analysis are illustrated in
Figure 7. These include Center of Mass (CoM), Base of
Support (BoS), and Center of Pressure (CoP). CoM, also
known as Center of Gravity, is the ground projection of the
body’s 3D center of mass [20]. Generally speaking, human
gait is stable if the CoM is contained withing the convex hull
of the BoS, also called the support polygon [34]. If the CoM
point is outside the support polygon, it is equivalent to the
presence of an uncompensated moment acting on the foot,
causing rotation around a point on the polygon boundary,
resulting in instability and a potential fall. Center of Pres-
sure (CoP), also known as the Zero Moment Point, is a point
where the total moment generated due to gravity and iner-
tia equals zero. Figure 7 shows a diagram of foot pressure
annotated with the CoP, shown as a red star, with pressure
from both feet shown as regions color-coded from low pres-
sure (yellow) to moderate pressure (red) to high pressure
(brown). Considering CoP as the ground reaction force and
KNN versus PressNET Testing Mean Absolute Errors (kPa)
Subject
Mean
Std
Median
Max
Min
1
10.5
3.6
1.8
1.8
10.3
3.3
18.4
11.6
2.3
1.3
2
12.1
5.9
2.7
1.8
11.8
5.8
24.1
16.3
1.8
2.0
3
11.4
5.0
2.4
1.6
10.7
4.8
21.6
14.9
1.6
1.9
4
11.6
5.5
2.9
1.9
11.3
5.2
25.7
18.0
2.2
1.4
5
12.6
6.1
2.7
1.8
12.2
5.9
22.9
19.8
2.4
2.4
6
11.2
4.9
2.3
1.5
10.9
4.6
20.2
14.0
2.8
2.3
Means
11.6
5.16
2.47
1.73
11.2
4.93
22.15
15.76
2.18
1.88
Table 4. Results for KNN baseline and PressNET, showing the
mean absolute error for each split of the data and the mean among
the splits. For every statistic, PressNET has lower error than the
baseline (lowest mean error values are shown in bold).
CoM as the opposing force, larger distances between the
two 2D points could indicate reduced stability. Speciﬁcally,
the CoP location relative to the whole body center of mass
has been identiﬁed as a determinant of stability in a variety
of tasks [23, 24, 37]. Note that the CoP is usually mea-
sured directly by force plates or insole foot pressure sen-
sors, whereas in this paper we infer it from video alone. We
quantitatively evaluate our results using ground truth data
collected by insole foot pressure sensors.
4.3. Quantitative Evaluation
Two metrics for quantitative evaluation of our networks
have been used:
1. Mean Absolute Error of Estimated Foot Pressure maps
(kPa) as compared to ground truth pressure and
2. Euclidean (ℓ2) distance of Center of Pressure (mm) as
compared to CoP calculated directly from ground truth
foot pressure.
To quantify these results with respect to physical units, the
foot pressure data is un-normalized by reversing the pre-
processing normalization.
4.3.1
Mean Absolute Error of Predicted Foot Pressure
Mean absolute error E is used to quantify the difference
between ground truth foot pressure Y and predicted foot
pressure ˆY on N foot pressure prexels as:
E =
1
|N|
X
n∈N
Yn −ˆ
Yn

(2)
Mean across all the cross-validation splits is taken for our
ﬁnal accuracy rates.
Table 4 shows the mean absolute errors of predicted foot
pressure for each data split, for both PressNET and the KNN
baseline. For PressNET, the worst two individuals to predict
foot pressure on are Subjects 2 and 5. This is also true for
the nearest neighbor classiﬁer as well, which could be be-
cause these subject foot pressures have a higher mean foot
pressure than the other subjects and thus the networks are
under-predicting the error. PressNET has a mean classiﬁca-
tion error of 5.16 kPa which is less than double the 3 kPa
9


## Page 10


Figure 8. Example frames from each of the 6 subjects. Each frame provides KNN, Ground Truth, PressNET, KNN error from Ground
Truth, PressNET error from Ground Truth, and the pose data extracted from the video frame.
10


## Page 11


Figure 9. The 2D center of pressure error plots for KNN (red) and PressNET (green) difference from ground truth (blue) for each subject.
measurement noise level of the foot pressure recording de-
vices, as mentioned in Section 3.1.2.
In order to test whether these results are signiﬁcant, a
two tailed paired t-test was performed between the mean
errors for each frame for PressNET compared with KNN
over each split of the data. This test showed that the results
from PressNET are statistically signiﬁcantly better than the
KNN baseline.
4.3.2
Computation for Center of Pressure
As a step towards analyzing gait stability from video, Cen-
ter of Pressure (CoP) from regressed foot pressure maps of
KNN and PressNET have been computed and quantitatively
compared to ground truth (GT) CoP locations computed
from the insole foot pressure maps. CoP is calculated as
the weighted mean of the pressure elements (prexels) in the
XY ground plane. The ℓ2 distance is used as a 1D met-
ric to quantify the 2D error between ground truth and pre-
dicted CoP locations. Table 5 shows the mean and stan-
dard deviations of ℓ2 errors calculated for the KNN base-
line and PressNET. This table clearly shows that the mean
distance error of COP computed from the PressNET net-
work pressure map predictions is approximately 5-6 times
smaller than that of KNN, with a standard deviation that is
approximately 2-3 times smaller. The PressNET average
error for all leave one subject out experiments yields a CoP
Euclidean error of 10.52 ± 23.05 mm for the left foot and
9.63 ± 20.0 for the right.
As shown in Figure 9, the distribution of PressNET dis-
tance errors are concentrated more tightly around zero mil-
limeters, showing that the spatial accuracy of PressNET
based CoP calculations are better than KNN, with smaller
variance. As a point of reference, it is known that a Center
KNN (Baseline) versus PressNET
Left Foot
Right Foot
Subject
mean
std
mean
std
1
62.99
7.52
64.75
18.37
55.59
8.02
53.65
17.07
2
68.86
14.02
58.24
29.01
69.89
13.78
50.43
28.22
3
56.78
11.23
54.64
24.44
64.85
10.98
55.55
22.47
4
74.50
11.87
64.99
27.29
67.56
9.40
55.63
20.20
5
47.63
10.14
47.23
21.33
51.21
8.82
48.43
17.61
6
52.77
8.34
55.92
17.84
42.45
6.76
38.02
14.44
All
60.59
10.52
57.63
23.05
58.59
9.63
50.28
20.00
Table 5. Mean and standard deviation of Euclidean errors in mm
of CoP locations computed from predicted foot pressure maps of
KNN and PressNET as compared to ground truth CoP evaluated
on the left and right foot separately. Bold indicates minimum error.
See Figure 9 for a display in 2D.
of Mass (CoM) localization accuracy of about 18 mm (or
1% of the subject’s height) is as accurate as the variation
between multiple existing CoM calculation methods [52].
4.4. Qualitative Evaluation
4.4.1
Qualitative Evaluation of Mean Absolute Error
Figure 8 visualizes foot pressure predictions and their mean
absolute errors for some example frames. The foot pressure
predictions, ground truth and absolute difference heatmaps
are rendered on the same color scale. The color bar in each
sub-frame represents foot pressure intensity in kilopascals
(kPa). It starts from a shade of blue, representing 0 foot
pressure to a dark shade of red, corresponding to maximum
foot pressure observed during the performance. The colors
in between represent different levels of pressure intensities
between 0 and the maximum. It can be visually observed
that the PressNET errors are small compared to KNN er-
rors. In addition to the qualitative comparison by visual-
ization, the respective mean absolute errors with respect to
ground truth frames have also been calculated to provide a
11


## Page 12


quantitative comparison of performance. The frames have
been chosen to show the ability of PressNET to generalize
to different poses, similar poses from different subjects and
different views with respect to a ﬁxed camera. The frames
have also been chosen to show some failure cases.
It is evident that the heatmaps generated by PressNET
are more similar to ground truth heatmaps. This is sup-
ported by the mean absolute frame errors of the networks.
KNN results are visually very poor when compared to
PressNET because 1-KNN is merely picking the frame with
the shortest distance between joints in a cross-subject eval-
uation. As the style of performance and body dynamics
differs for each subject, KNN is unable to generalize to a
change in subjects, leading to high mean absolute error.
Observing foot pressure predictions temporally over a
sequence of frames, it was observed that KNN predic-
tions are highly inconsistent and ﬂuctuating, whereas the
PressNET predictions are temporally smooth and consis-
tent. Since the system operates on a per-frame basis, KNN
picks the frame with the nearest pose in the dataset to the
current frame. This makes the predictions ﬂuctuate over
time. Even though our network is trained using the same
per-frame basis mechanism, it has learned to predict the
mean foot pressure heatmaps over a window of frames, i.e.,
our network has learned to be temporally stable, making the
predictions smooth and more similar to ground truth.
4.4.2
Qualitative Evaluation of Center of Pressure
Table 5 showed mean and standard deviation of Euclidean
errors in millimeters of CoP locations computed from pre-
dicted foot pressure maps of KNN and PressNET as com-
pared to ground truth CoP evaluated on the left and right
foot separately. Figure 9 shows the 2D CoP distance error
scatter plots for Subjects 1, 2, 3, 4, 5 and 6. It can be ob-
served from the ﬁgures that the spread of errors of CoP for
PressNET is signiﬁcantly lower that that of KNN and con-
centrated around (0,0).
5. Summary and Conclusion
In this research, the feasibility of regressing foot pres-
sure from 2D joints detected in video has been explored.
This is the ﬁrst work in the computer vision community to
establish a direct mapping from 2D human body kinematics
to foot pressure dynamics. The effectiveness of our Press-
NET network has been shown both quantitatively and qual-
itatively on a challenging, long, multi-modality Taiji per-
formance dataset. Statistically signiﬁcant improved results
over a standard K-Nearest Neighbor method in foot pres-
sure map estimation from video have been demonstrated.
The outcome of PressNET is encouraging since it is also
within the range of inter-subject variance of the same pose
observed (Figure 4). Furthermore, we demonstrate the use
of regressed foot pressure results for estimation of Center
of Pressure, a key component of postural and gait stabil-
ity. The errors (Table 5) are within the accepted range for
kinesiology studies of Center of Mass (CoM) [52], a corre-
sponding dynamics concept to CoP in stability analysis.
We hope to extend this work to include more aspects of
human body dynamics such as regressing directly to muscle
activations, weight distributions, balance, and force. Our
goal is to build precision computer vision tools that esti-
mate various human body dynamics using passive and inex-
pensive visual sensors, with outcomes validated using bio-
mechanically derived data (rather than approximations by
human labelers).
We foresee introducing a new and ex-
citing sub-ﬁeld in computer vision going beyond visually
satisfactory human joint/pose detection to the more chal-
lenging problems of capturing accurate, quantiﬁable human
body dynamics for scientiﬁc applications.
6. Acknowledgments
We would like to thank the six volunteers who con-
tributed 24-form Taiji performances to this study. We would
like to acknowledge Andy Luo for his help in rendering the
images and videos for demonstration. We thank the College
of Engineering Dean’s ofﬁce of Penn State University for
supporting our motion capture lab for research and educa-
tion. This human subject research is approved through Penn
State University IRB Study8085. This work is supported in
part by NSF grant IIS-1218729.
References
[1] A. Agarwal and B. Triggs.
3d human pose from silhou-
ettes by relevance vector regression.
In Computer Vision
and Pattern Recognition, 2004. CVPR 2004. Proceedings of
the 2004 IEEE Computer Society Conference on, volume 2,
pages II–II. IEEE, 2004.
[2] S. J. Allen, M. A. King, and M. R. Yeadon. Is a single or
double arm technique more advantageous in triple jumping?
Journal of Biomechanics, 43(15):3156–3161, 2011.
[3] R. Alp Güler, N. Neverova, and I. Kokkinos. Densepose:
Dense human pose estimation in the wild.
In The IEEE
Conference on Computer Vision and Pattern Recognition
(CVPR), June 2018.
[4] M. Arvin, M. Hoozemans, M. Pijnappels, J. Duysens,
S. M. P. Verschueren, and J. Van Dieen. Where to step? con-
tributions of stance leg muscle spindle afference to planning
of mediolateral foot placement for balance control in young
and older adults. Frontiers in Physiology, 9:1134, 2018.
[5] M. Bächer, E. Whiting, B. Bickel, and O. Sorkine-Hornung.
Spin-it: Optimizing moment of inertia for spinnable objects.
ACM Trans. Graph., 33(4):96:1–96:10, July 2014.
[6] C. M. Bishop.
Pattern Recognition and Machine Learn-
ing (Information Science and Statistics).
Springer-Verlag,
Berlin, Heidelberg, 2006.
[7] F. Bogo, A. Kanazawa, C. Lassner, P. Gehler, J. Romero,
and M. J. Black. Keep it smpl: Automatic estimation of 3d
12


## Page 13


human pose and shape from a single image. In European
Conference on Computer Vision, pages 561–578. Springer,
2016.
[8] A. Bulat and G. Tzimiropoulos. Human pose estimation via
convolutional part heatmap regression. In European Confer-
ence on Computer Vision, pages 717–732. Springer, 2016.
[9] Y. Cai, L. Ge, J. Cai, and J. Yuan. Weakly-supervised 3d
hand pose estimation from monocular rgb images. In ECCV,
pages 678–694. Springer International Publishing, 2018.
[10] Z. Cao, T. Simon, S.-E. Wei, and Y. Sheikh. Realtime multi-
person 2d pose estimation using part afﬁnity ﬁelds. In The
IEEE Conference on Computer Vision and Pattern Recogni-
tion (CVPR), volume 1, page 7, 2017.
[11] C.-H. Chen and D. Ramanan. 3d human pose estimation=
2d pose estimation+ matching.
In The IEEE Conference
on Computer Vision and Pattern Recognition (CVPR), vol-
ume 2, page 6, 2017.
[12] W. Chen, H. Wang, Y. Li, H. Su, Z. Wang, C. Tu, D. Lischin-
ski, D. Cohen-Or, and B. Chen. Synthesizing training images
for boosting human 3d pose estimation. In 3D Vision (3DV),
2016 Fourth International Conference on, pages 479–488.
IEEE, 2016.
[13] X. Chen and A. L. Yuille. Articulated pose estimation by a
graphical model with image dependent pairwise relations. In
Advances in Neural Information Processing Systems (NIPS),
pages 1736–1744, 2014.
[14] F. Chollet. Xception: Deep learning with depthwise sepa-
rable convolutions. In The IEEE Conference on Computer
Vision and Pattern Recognition (CVPR), July 2017.
[15] Z. J. Domire and J. H. Challis. Maximum height and min-
imum time vertical jumping.
Journal of Biomechanics,
48(11):2865–2870, 2015.
[16] N. Eckardt and N. J. Rosenblatt. Healthy aging does not im-
pair lower extremity motor ﬂexibility while walking across
an uneven surface.
Human Movement Science, 62:67–80,
2018.
[17] X. Fan, K. Zheng, Y. Lin, and S. Wang.
Combining lo-
cal appearance and holistic view: Dual-source deep neural
networks for human pose estimation. In Proceedings of the
IEEE Conference on Computer Vision and Pattern Recogni-
tion, pages 1347–1355, 2015.
[18] A. Gilbert, M. Trumble, C. Malleson, A. Hilton, and J. Col-
lomosse. Fusing visual and inertial sensors with semantics
for 3d human pose estimation. International Journal of Com-
puter Vision, pages 1–17, 2018.
[19] S. R. Goldberg, S. Ounpuu, and S. L. Delp. The importance
of swing-phase initial conditions in stiff-knee gait. Journal
of Biomechanics, 36(8):1111–1116, 2003.
[20] A. Goswami.
Foot rotation indicator (fri) point: a new
gait planning tool to evaluate postural stability of biped
robots. In Proceedings 1999 IEEE International Conference
on Robotics and Automation (Cat. No.99CH36288C), vol-
ume 1, pages 47–52 vol.1, May 1999.
[21] R. Grimm, J. Sukkau, J. Hornegger, and G. Greiner. Au-
tomatic patient pose estimation using pressure sensing mat-
tresses.
In Bildverarbeitung für die Medizin 2011, pages
409–413. Springer, 2011.
[22] I. Gulrajani, F. Ahmed, M. Arjovsky, V. Dumoulin, and
A. C. Courville. Improved training of wasserstein gans. In
Advances in Neural Information Processing Systems, pages
5767–5777, 2017.
[23] A. L. Hof. The equations of motion for a standing human
reveal three mechanisms for balance. Journal of Biomechan-
ics, 40(2):451–457, 2007.
[24] A. L. Hof. The ‘extrapolated center of mass’ concept sug-
gests a simple control of balance in walking. Human Move-
ment Science, 27(1):112–125, 2008.
[25] G. Huang, Z. Liu, L. Van Der Maaten, and K. Q. Wein-
berger. Densely connected convolutional networks. In The
IEEE Conference on Computer Vision and Pattern Recogni-
tion (CVPR), volume 1, page 3, 2017.
[26] M. A. Hughes, B. S. Myers, and M. L. Schenkman. The role
of strength in rising from a chair in the functionally impaired
elderly. Journal of Biomechanics, 29(12):1509–1513, 1996.
[27] S. Ioffe and C. Szegedy. Batch normalization: Accelerating
deep network training by reducing internal covariate shift.
In Proceedings of the 32Nd International Conference on In-
ternational Conference on Machine Learning - Volume 37,
ICML’15, pages 448–456. JMLR.org, 2015.
[28] J. H. Ko, Z. Wang, J. H. Challis, and K. M. Newell. Compen-
satory mechanisms of balance to the scaling of arm-swing
frequency.
Journal of Biomechanics, 48(14):3825–3829,
2015.
[29] E. D. Lemaire, A. Biswas, and J. Kofman. Plantar pressure
parameters for dynamic gait stability analysis. In Engineer-
ing in Medicine and Biology Society, 2006. EMBS’06. 28th
Annual International Conference of the IEEE, pages 4465–
4468. IEEE, 2006.
[30] Y. Liu, R. Collins, and Y. Tsin. Gait sequence analysis using
frieze patterns. In European Conference on Computer Vision,
pages 657–671. Springer, 2002.
[31] A. L. Maas, A. Y. Hannun, and A. Y. Ng. Rectiﬁer nonlin-
earities improve neural network acoustic models. In Proc.
icml, volume 30, page 3, 2013.
[32] J. Martinez, R. Hossain, J. Romero, and J. J. Little. A simple
yet effective baseline for 3d human pose estimation. In IEEE
International Conference on Computer Vision, volume 206,
page 3, 2017.
[33] F. Moreno-Noguer. 3d human pose estimation from a single
image via distance matrix regression. In 2017 IEEE Confer-
ence on Computer Vision and Pattern Recognition (CVPR),
pages 1561–1570. IEEE, 2017.
[34] J. Mrozowski, J. Awrejcewicz, and P. Bamberski. Analysis
of stability of the human gait. Journal of Theoretical and
Applied Mechanics, 45(1):91–98, 2007.
[35] A. Newell, K. Yang, and J. Deng. Stacked hourglass net-
works for human pose estimation. In European Conference
on Computer Vision, pages 483–499. Springer, 2016.
[36] B. X. Nie, P. Wei, and S.-C. Zhu. Monocular 3d human pose
estimation by predicting depth on joints. In IEEE Interna-
tional Conference on Computer Vision, 2017.
[37] Y.-C. Pai. Movement termination and stability in standing.
Exercise and Sport Sciences Reviews, 31(1):19–25, 2003.
[38] T. Pataky, T. Mu, K. Bosch, D. Rosenbaum, and J. Gouler-
mas. Gait recognition: Highly unique dynamic plantar pres-
sure patterns among 104 individuals. Journal of The Royal
Society Interface, 9:790–800, 2012.
[39] G. Pavlakos, X. Zhou, K. G. Derpanis, and K. Daniilidis.
13


## Page 14


Coarse-to-ﬁne volumetric prediction for single-image 3d
human pose.
In Computer Vision and Pattern Recogni-
tion (CVPR), 2017 IEEE Conference on, pages 1263–1272.
IEEE, 2017.
[40] J. Perry, J. R. Davids, et al.
Gait analysis: normal and
pathological function.
Journal of Pediatric Orthopaedics,
12(6):815, 1992.
[41] R. J. Peterka and P. J. Loughlin. Dynamic regulation of sen-
sorimotor integration in human postural control. Journal of
neurophysiology, 91(1):410–423, 2004.
[42] R. Prévost, M. Bächer, W. Jarosz, and O. Sorkine-Hornung.
Balancing 3d models with movable masses. In Conf. on Vi-
sion, Modeling and Visualization, pages 9–16. Eurographics
Association, 2016.
[43] R. Prévost, E. Whiting, S. Lefebvre, and O. Sorkine-
Hornung. Make it stand: Balancing shapes for 3d fabrica-
tion. ACM Trans. Graph., 32(4):81:1–81:10, July 2013.
[44] G. Rogez, P. Weinzaepfel, and C. Schmid. Lcr-net++: Multi-
person 2d and 3d pose detection in natural images. CoRR,
abs/1803.00455, 2018.
[45] E. Simo-Serra, A. Ramisa, G. Alenyà, C. Torras, and
F. Moreno-Noguer.
Single image 3d human pose estima-
tion from noisy observations. In Computer Vision and Pat-
tern Recognition (CVPR), 2012 IEEE Conference on, pages
2673–2680. IEEE, 2012.
[46] X. Sun, J. Shang, S. Liang, and Y. Wei. Compositional hu-
man pose regression. In The IEEE International Conference
on Computer Vision (ICCV), volume 2, 2017.
[47] D. Tomè, C. Russell, and L. Agapito. Lifting from the deep:
Convolutional 3d pose estimation from a single image. The
IEEE Conference on Computer Vision and Pattern Recogni-
tion (CVPR), pages 2500–2509, 2017.
[48] J. Tompson, R. Goroshin, A. Jain, Y. LeCun, and C. Bre-
gler. Efﬁcient object localization using convolutional net-
works. In Proceedings of the IEEE Conference on Computer
Vision and Pattern Recognition, pages 648–656, 2015.
[49] J. A. L. Y. B. C. Tompson, J.J. Joint training of a convo-
lutional network and a graphical model for human pose es-
timation. In: Advances in Neural Information Processing
Systems. (2014) 1799â ˘A¸S1807, 2014.
[50] A. Toshev and C. Szegedy. Deeppose: Human pose estima-
tion via deep neural networks. In Proceedings of the IEEE
Conference on Computer Vision and Pattern Recognition,
pages 1653–1660, 2014.
[51] R. Vera-Rodriguez, M. JSD., J. Fierrez, and J. Ortega-Garcia.
Comparative analysis and fusion of spatiotemporal informa-
tion for footstep recognition. IEEE Transactions on Pattern
Analysis and Machine Intelligence, 35:823–34, 2013.
[52] M. Virmavirta and J. Isolehto. Determining the location of
the bodyŒ¸s s center of mass for different groups of physi-
cally active people. Journal of biomechanics, 47(8):1909–
1913, 2014.
[53] C. Wang, R. Bannuru, J. Ramel, B. Kupelnick, T. Scott, and
C. Schmid. Tai chi on psychological well-being: systematic
review and meta-analysis. BMC complementary and alter-
native medicine, pages 10–23, 2010.
[54] D. A. Winter. Biomechanics and motor control of human
gait: normal, elderly and pathological. University of Water-
loo Press, 1991.
[55] D. A. Winter. Human balance and posture control during
standing and walking.
Gait and Posture, 3:193–214, 12
1995.
[56] X. Zhou, Q. Huang, X. Sun, X. Xue, and Y. Wei. Towards
3d human pose estimation in the wild: a weakly-supervised
approach. In IEEE International Conference on Computer
Vision, 2017.
[57] X. Zhou, M. Zhu, S. Leonardos, K. G. Derpanis, and
K. Daniilidis. Sparseness meets deepness: 3d human pose
estimation from monocular video.
In Proceedings of the
IEEE Conference on Computer Vision and Pattern Recog-
nition, pages 4966–4975, 2016.
14

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
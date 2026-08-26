---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1806.04564v7
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1806.04564v7_Detection_of_Premature_Ventricular_Contractions_Using_Densely_Connected_Deep_Con

> Source: 1806.04564v7_Detection_of_Premature_Ventricular_Contractions_Using_Densely_Connected_Deep_Con.pdf

> Pages: 10

---


## Page 1


LATEX Detection of Premature Ventricular Contractions Using Densely Connected
Deep Convolutional Neural Network with Spatial Pyramid Pooling Layer
Jianning Li
Abstract
Premature ventricular contraction(PVC) is a type of pre-
mature ectopic beat originating from the ventricles. Auto-
matic method for accurate and robust detection of PVC is
highly clinically desired.Currently, most of these methods
are developed and tested using the same database divided
into training and testing set and their generalization perfor-
mance across databases has not been fully validated. In this
paper, a method based on densely connected convolutional
neural network and spatial pyramid pooling is proposed for
PVC detection which can take arbitrarily-sized QRS com-
plexes as input both in training and testing. With a much
more straightforward architecture,the proposed network
achieves comparable results to current state-of-the-art deep
learning based method with regard to accuracy,sensitivity
and speciﬁcity by training and testing using the MIT-BIH
arrhythmia database as benchmark.Besides the benchmark
database,QRS complexes are extracted from four more open
databases namely the St-Petersburg Institute of Cardiolog-
ical Technics 12-lead Arrhythmia Database,The MIT-BIH
Normal Sinus Rhythm Database,The MIT-BIH Long Term
Database and European ST-T Database. The extracted QRS
complexes are different in length and sampling rate among
the ﬁve databases.Cross-database training and testing is
also experimented achieving a 0.9943 overall accuracy with
0.9819 sensitivity and 0.9952 speciﬁcity demonstrating the
advantage of using multiple databases for training over us-
ing only a single database.The network also achieves satis-
factory scores on the other four databases showing good
generalization capability. Keywords: Premeture ventric-
ular contraction,detection, denseNet,spatial pyramid pool-
ing,deep learning
1. Introduction
Frequent premature ventricular contraction(PVC) is of-
ten associated with organic heart diseases and should be
treated medically or surgically if it bothers life quality[1]
while sporadic PVC can happen to most healthy population
and is usually considered benign if it does not trigger se-
vere ventricular arrhythmia such as supraventricular tachy-
cardia and ventricular ﬁbrillation.The two types of PVC are
usually treated differently and the classiﬁcation is based on
how many times it occurs in a long-term ECG recording.
Therefore,its clinically signiﬁcant to develop accurate and
robust methods to detect PVC automatically. Up until now,
various methods for PVC detection have been developed
with the aim of reducing doctors workload and these meth-
ods can be categorized into two classes.First,hand-craft fea-
tures combining a classiﬁer.These kind of methods are often
seen in earlier published works that utilize hand-craft ECG
features and a classiﬁer to distinguish between PVC and
non-PVC.The hand-craft features include morphology[9],
wavelet[12, 5, 26, 29, 24] and temporal domain[18] etc.
Some works also studied methods for the selection of hand-
craft features to improve detection performance [11, 14,
21].Various classiﬁers are used in the studies of PVC detec-
tion including artiﬁcial neural network[15, 20, 34],support
vector machine[4] as well as clustering[3].Second, deep
convolutional neural network (CNN)is showing advantages
over traditional methods by providing a way of learn-
ing highly discriminative features automatically.
Many
works have studied its application in detecting abnormal
heart beats including atrial ﬁbrillation[2, 27, 30, 7, 25] and
PVC[33, 31, 8] or other arrhythmia[22].
Currently,[33]
achieves state-of-the-art results for PVC detection using a
architecture combining multiple one-dimensional CNN and
LSTM.However,all of the methods mentioned above are de-
veloped and tested using the same database and their cross-
database generalization capability has not been fully vali-
dated.In clinic,however,the sampling rate of ECG data can
be different from different devices.In such cases,its natu-
ral to think of training several networks for each speciﬁc
ECG data which is time-consuming and sometimes impos-
sible when the ECG data are limited.Therefore,its necessary
to develop a generalized method that can maintain good
performance across ECG data of varied sampling rates.In
our study ,we propose a method based on densely con-
nected convolutional neural network [10]and spatial pyra-
mid pooling [13] for automatic PVC detection.The pro-
posed network can take as input QRS complexes of arbitrary
1
arXiv:1806.04564v7  [cs.CV]  10 Oct 2019


## Page 2


length and can be trained using multiple ECG databases
with different sampling rates.Its cross-database generaliza-
tion capability is veriﬁed on ﬁve open databases namely
the MIT-BIH arrhythmia database,St-Petersburg Institute of
Cardiological Technics 12-lead Arrhythmia Database,The
MIT-BIH Normal Sinus Rhythm Database,The MIT-BIH
Long Term Database and European ST-T Database.The per-
formance on the MIT-BIH arrhythmia database which is
a commonly used benchmark for arrhythmia detection is
comparable to current state-of-the-art deep learning based
method and our proposed network is much less complicated
and easier to implement.
2. Databases
Five open ECG databases from PhysioNet[6] are
involved in our study namely the MIT-BIH arrhythmia
database(DS1)[19],St-Petersburg Institute of Cardiological
Technics
12-lead
Arrhythmia
Database(DS2)[6],MIT-
BIH
Normal
Sinus
Rhythm
Database(DS3),MIT-
BIH
Long
Term
Database(DS4)and
European
ST-T
Database(DS5)[28].Half of the recordings in each database
are used for training and the other half for testing. QRS
complexes are selected from these recordings and cate-
gorized to PVC and non-PVC based on the location of
R-peaks and beat annotations provided along with the
databases.For DS1,the selection of training set and testing
set is the same as that of [33, 8] for comparison purpose.For
other databases,equal number of non-PVC beats are se-
lected from each long-term recording and all PVC beats
are considered.The length of the extracted QRS complexes
is different across databases due to different sampling
rates.According to published literature[9, 8],about 150
sampling points are selected around R-peak to represent the
QRS complex(50 and 99 sampling points before and after
R-peak respectively ) for DS1 in our study.For DS2-DS5,
the number of sampling points li for the QRS complex is
decided by the following equation:
li = l0
fi
f0
(1)
where l0 =150 is the the length of QRS complex from DS1
and f0 is the sampling rate of DS1.fi(i = 2, 3, 4, 5)is the
sampling rate for DS2-DS5.
Table 1 shows the details of the extracted QRS com-
plex from DS1-DS5.Altogether,the training set of the mixed
database contains 32569 PVC beats and 139015 non-PVC
beats.The testing set contains 62200 and 122771 beats for
PVC and non-PVC respectively.Figure 1 illustrates the QRS
wave morphology of PVC and non-PVC.
Among the ﬁve databases described above,the MIT-BIH
arrhythmia database is a commonly used benchmark for
developing and evaluating arrhythmia detection algorithms
while the other four databases are built for various pur-
poses.
For example,the European ST-T database is in-
tended to be used for evaluating algorithms related to S-
T segment and T wave.For all databases, the location of
R peaks and beat-by-beat annotations are provided.The di-
versity of ECG data is greatly improved compared to us-
ing only a single database.On the one hand,the ECG data
in these databases are collected from more unique indi-
viduals using different devices with varied sampling rates
and analog-to-digital resolution.On the other hand,more ar-
rhythmia types can be included to the non-PVC category us-
ing multiple databases.Note that not all beats of these long-
term ECG recordings are considered. Training and testing
on databases of greater diversity helps the network general-
ize better and the testing results can be more reliable.
3. Methodology
The proposed diagram for PVC detection is shown
in Figure.2.
First,the ECG signals are bandpass-ﬁltered
from 0.4Hz to 50Hz using a 4-level Butterworth ﬁlter
before the QRS complexes are extracted.Second,our net-
work takes as input the QRS complex of arbitrary length
for processing.Third, a nonlinear transformation is ap-
plied to the input to compute highly discriminative fea-
tures.The nonlinear transformation is done through three
dense blocks connected by convolutional and max pooling
operations.Fourth,the extracted features are vectorized by
a spatial pyramid pooling layer.Different from traditional
pooling operations that produce variable sized outputs if the
input size is not ﬁxed, the spatial pyramid pooling layer
accepts arbitrarily-sized inputs but outputs a ﬁxed-length
vector.Finally,the fully connected layer with sigmoid acti-
vation function produces the probability of an input belong-
ing to PVC.Both dense blocks and spatial pyramid pooling
helps reduce over-ﬁtting and improve generalization capa-
bility which is crucial for PVC detection algorithms when it
comes to real clinical application. Details of each procedure
will be speciﬁed in the following sections.
3.1. Densely connected block
Proposed in [10],dense connections between layers al-
leviate the problem of vanishing-gradient as the network
goes deeper.With smaller number of ﬁlters for each con-
volutional layer, the total number of trainable parameters in
the network can maintain small even if its deep which helps
reduce over-ﬁtting and improve generalization capability.
Figure.3(a) shows a dense block with 3 1-dimensional con-
volutional layers where all the layers are connected to each
other so that the input of each layer is the output feature
map of all the preceding layers.By using dense connections
among layers,the features can be made best use of. In our
study,we use three dense blocks ,each having 3,6, and 9 1-
dimensional convolutional layers respectively with no bot-
2


## Page 3


Table 1. Mixed Database of QRS Complexes(SR=Sampling Rate)
Database
SR
Length
PVC(train)
non-PVC (train)
PVC (test)
non-PVC(test)
DS1
360
150
3788
47213
3220
46478
DS2
257
108
8467
41264
10711
32838
DS3
128
52
21
5000
5
1000
DS4
128
52
19867
20000
44224
20000
DS5
250
105
426
25538
4040
22455
Total
/
/
32569
139015
62200
22771
Figure 1. QRS complex extracted from long-term ECG in DS1-DS5, PVC(top row) and non-PVC(bottom row).
tleneck layer1. The number of ﬁlters for all convolutional
layers in all dense blocks is 32 and the kernel width is set
to 3. Between dense blocks are transition layers which con-
duct convolutional,batch normalization and average pooling
operations followed by a relu activation function . The size
of feature maps produced within a dense block are the same
because theres no pooling operations in a dense block.The
transition layer is responsible for change feature-map sizes
through convolutional and pooling operations.Note that the
convolutional operations in a dense block does not change
the size of feature maps for layer concatenation purpose.
1A bottleneck in a dense block is a convolutional operation with kernel
width set to 1 [10]
3.2. Spatial pyramid pooling layer
To address the issue of varying sizes of the extracted
QRS complex due to varied sampling rate,1-dimensional
spatial pyramid pooling[13]is adopted in our network to
replace the traditional max pooling operations in the last
layer.Figure 3(b) shows the 1-dimensional spatial pyramid
pooling layer we use for vectorizing feature maps produced
by preceding convolutional layer.Assuming that the length
of current input QRS is 152 and the densely connected com-
ponent extracts 272 feature maps of length 19 from the in-
put.For each feature map, max-pooling is done on two levels
of feature pyramid.First, pooling on the entire feature map
which produces one max value. Second,pooling on 4 local
subsections ,each a quarter the size of the feature map pro-
ducing 4 max values,each for one subsection. After spatial
3


## Page 4


pyramid pooling, a vector of length 5 is generated.The vec-
tors of each feature map are then ﬂattened to form the ﬁnal
feature vector of length 1360(5 × 272).From Figure3(b) we
can see that the size of the ﬁnal feature vector depends only
on the number of subsections of each feature map as well as
the number of ﬁlters of the preceding convolutional layer so
that the spatial pyramid pooling layer can produce a feature
vector of ﬁxed length given an arbitrarily-sized input.The
advantage of using spatial pyramid pooling layer is that we
can train our network with arbitrarily-sized QRS complex
and sampling rate which increase scale-invariance and re-
duce over-ﬁtting[13].Besides, the trained network can be
applied to a wider range of ECG data with different length
and sampling rate collected using different devices. Simi-
lar to the spatial pyramid pooling is the global max pooling
inspired from global average pooling in[16].It replaces the
ﬁnal fully connected layer by performing a max-pooling op-
eration on the entire feature map to accept arbitrarily-sized
input.As can be seen,global max pooling is in fact a special
case of spatial pyramid pooling when max pooling is only
applied to the entire feature map.
3.3. Weighted binary cross-entropy loss
As can be seen in Table 1,the number of PVC and non-
PVC beats is highly imbalanced. For each training epoch,
non-PVC samples contribute much more than PVC samples
to updating network parameters which will severely under-
mines the performance of the network to detect PVC.To
address the problem,a weighted binary cross-entropy loss
function is adopted as in Eq.2:
l =
X
x∈X
ηι(x)[ytruelnyout + (1 −ytrue)ln(1 −yout))]
(2)
Where ι(x) is the target label for sample x and |Xι(x)|
is the number of samples belong to target ι(x) in train-
ing batch X. yout and ytrue are the model output and
groundtruth respectively.ηι(x) is the weight coefﬁcient:
ηι(x) = 1 −|Xι(x)|
X
(3)
Eq.2 means that classes with fewer samples are given
a larger weight so that PVC samples contribute to the loss
equally as non-PVC samples in each training epoch. −l is
minimized in training.
4. Experiments and Results
Three experiments are conducted in this section.First,to
have a comparison with the results of other published meth-
ods, the proposed network is trained and tested using only
DS1. The splitting strategy for training set and testing set
is the same as in[8, 33].Second,to demonstrate how training
on multiple databases affect the performance of the network
compared to training using a single database,all the training
set of the ﬁve databases described in Table 1 are used for
training in our second experiment.Testing is also carried out
on the test sets of DS1-DS5.The third experiment we con-
duct is a simple ablation study to remove the weighted loss
function and spatial pyramid pooling layer for training.This
experiment is to demonstrate that weighted loss function
and a spatial pyramid pooling layer is necessary to guar-
antee good performance.The experiment is carried out on
DS1.Metrics used in our experiments to quantify the per-
formance of PVC detection are accuracy,sensitivity, speci-
ﬁcity,positive predictive value(PPV), and Youdens index γ.
4.1. Training details
For all the experiments, the training strategy and model
conﬁguration are kept the same.The network is imple-
mented in Keras and Tensorﬂow on a machine with 32GB
memory and Core i7-6700 CPU(8 cores with 16 threads)
and a 8Gb Nvidia Quadro M4000 GPU.The computation
power of the machine is fully exploited to accelerate train-
ing. The initial learning rate is set to 0.001 and decreases by
5 percent every 100 epochs.The batch size is set to 100.20
percent of the training set is used for validation and train-
ing stops when validation loss stops to decrease.Adam op-
timizer is used for updating network parameters. For all
experiments,the input are normalized to the range[-1,1] be-
fore feeding into the network. The network contains ap-
proximately 360000 trainable parameters. Our codes and
checkpoint will be available upon acceptance2
4.2. Training and testing on DS1
In our ﬁrst experiment,the network is trained and tested
on DS1.In this case, our network accepts single input size
of 150 both in training and testing.The splitting strategy for
training and testing set in Table 1 is the same with that of
[8, 33] for comparison purpose.Results are shown in Table
2.
As can be seen from table 2,our proposed method pro-
duces results comparable to current state-of-the-art method
by[33]on the test set of DS1 and the network architecture
and training procedure of our method is much less compli-
cated than theirs.
4.3. Training and testing on DS1-DS5
Previous deep learning based methods for PVC de-
tection require that the length of input QRS complex
be ﬁxed.Training and testing are conducted on the same
database splitting into training set and testing set where
the QRS complexes are of the same length and sampling
rate.As is detailed in Methodology,our network can take
2https://www.github.com/Eric-THU/PVC-Detection
4


## Page 5


Figure 2. The proposed diagram for PVC detection.
Table 2. Comparison with other published methods on DS1
methods
Acc
Sensitivity
Speciﬁcity
PPV
γ
Zarei[8]
98.77
96.12
98.96
86.48
95.08
Fei-yan Zhou[33]
99.41
97.59
99.54
93.55
97.13
Proposed
99.26
97.37
99.39
92.23
96.76
Figure 3. (a)A 3-layer dense block with no bottleneck.The ﬁlter
number of each convolutional layer is 32 and the kernel width is
3.(b)A two-level spatial pyramid pooling layer used in our net-
work.
as input QRS complex of arbitrary length.Therefore, we
can use multiple databases for training and testing .In this
experiment,the network is trained using all the training
sets of DS1 DS5 detailed in Table 1 and tested on all
the test sets.Altogether,there are 4 sizes for input which
is 150,52,108 and 257. Training on multi-size QRS com-
plexes is a tricky task.We train our network iteratively
from one database to another.In our study,the network is
trained 20 epochs on one database before switching to an-
other.When the validation loss while training on a database
stops decreasing,the database is discarded and does not in-
volve in the next training iteration.This is iterated until all
databases are discarded.Testing results are shown in Table
3.
By comparing Table 2-3, we can see that the perfor-
mance on DS1 is improved by training on multi-size input
(Table 2 row 3 and Table 3 row 1).Whats worthy of note
in this experiment is that the improvement on DS1 is not
merely because of more training data.A sensible explana-
tion should be that by training on multiple databases with
multi-size ECG data sampled at different rates and from
more unique individuals, the network can learn more gener-
alized and abstract features of PVC and non-PVC.In other
words, the generalization capability of the network can be
improved through training on a database of greater diver-
sity compared to training using a single database. The net-
work also achieves satisfactory results on the test sets of
DS2 DS5.Note that ,in DS3,4 out of 5 PVC beats are cor-
rectly identiﬁed. Altogether,our network achieves an over-
all accuracy of 95.58 percent with sensitivity and speciﬁcity
being 92.68% and 97.05% respectively on a mixed database
containing 62200 PVC samples and 122771 non-PVC sam-
ples.
5


## Page 6


Table 3. Testing results on DS1-DS5
Database
Acc
Sensitivity
Speciﬁcity
PPV
γ
DS1
99.43
98.19
99. 52
93.95
97.71
DS2
93.92
89.13
95.49
86.57
84.62
DS3
95.92
80.00
96.00
/
76.00
DS4
94.34
93.26
96.73
98.44
89.99
DS5
94.08
91.36
94.57
75.17
85.93
Overall
95.58
92.68
97.05
94.09
89.73
4.4. Ablation study
A simple ablation study is conducted to quantitatively
evaluate how weighted loss function and the spatial pyra-
mid layer affect the network performance.In this exper-
iment,three simpliﬁcations of the proposed network is
trained and tested on DS1.First, a standard 20-layer CNN
without dense connection components and spatial pyramid
pooling layer.The ﬁrst 19 layers are convolutional layers
followed by max-pooling and the last layer is the single-
node fully connected layer with sigmoid activation func-
tion for binary classiﬁcation.
Second ,the weight coef-
ﬁcient of the loss function is removed.Third,the spatial
pyramid pooling layer is replaced by a global max pool-
ing(GMP)layer.For comparison purpose, all the networks
have approximately the same number of trainable param-
eters.Results is shown in Table 4.
By analyzing the results in Table 4, we can ﬁnd that both
dense connection components and spatial pyramid pool-
ing helps improve PVC detection performance.More specif-
ically,sensitivity is severely degenerated when the weight
coefﬁcient in Eq.2 is removed which is in accordance with
our assumption that the contribution of PVC samples to
the loss is overwhelmed when non-PVC samples far out-
number PVC samples.This causes the network fail to learn
adequately the features of PVC leading to a poor PVC
distinguishability.To further illustrate,we visualize the his-
togram of the output of the ﬁnal fully connected layer for
each training step in Figure 4.In Figure 4 (a), the net-
work output is totally biased towards non-PVC samples
(output value well below 0.5) while Figure 4 (a),the net-
work is able to distinguish between PVC samples and non-
PVC samples with good decision margin.
On the other
hand,more levels of pyramid in the spatial pyramid pool-
ing layer improve overall performance.Compared with the
2-level pyramid 1 × 1,2 × 2 we use in our network,we see
a drop in accuracy,sensitivity and speciﬁcity when its re-
placed by global max pooling which can be seen as a 1-level
pyramid1×1.This phenomenon can be explained that by us-
ing more levels of pyramid,the network can become more
robust to the variations of QRS complex due to individual
difference.However,it remains to be experimented whether
the PVC detection performance can keep improving as the
level of pyramid in the spatial pyramid pooling layer goes
higher. The standard 20-layer CNN without dense connec-
tion components and spatial pyramid pooling performs the
worst.Whats interesting is that the network converges at a
high accuracy (near 100 percent) and a low loss (near 0)
at the end of training but can not generalize well in testing
set showing that its over-ﬁtted and has poor generalization
capability.
Figure 4. The histogram of the output of the ﬁnal fully connection
layer for each training step without(a) and with(b) weighted loss
function.
4.5. PVC detection with focal loss
In 3.3, a weighted binary cross-entropy loss function is
adopted to address the issue of high class imbalance. By in-
troducing the weight coefﬁcient to the loss function, the loss
generated by PVC samples can avoid being overwhelmed
by the loss from non-PVC samples.
In our experiments
we also ﬁnd that its an easy task to achieve a high speci-
ﬁcity even with an ordinary network while a well-designed
network is required to guarantee high sensitivity. In other
words, the non-PVC samples which are dominant in num-
ber are easy negative samples while the PVC samples be-
long to hard positive samples , quoting the term from[17].
To address the problem, its natural to think of paying less at-
tention to these easy negative samples while focusing more
on the hard positive samples in the loss function for each
training epoch. Inspired by [17], we also experiment us-
ing a modulating factor (1 −pt)γ together with the weight
coefﬁcient ηι(x) in Eq.2.
pt =

yout, (ytrue = 1)
1 −yout, (ytrue = 0)
(4)
By rewriting Eq.2. we get the focal loss function as in
6


## Page 7


Table 4. Ablation study results on DS1
methods
Acc
Sensitivity
Speciﬁcity
PPV
γ
Standard 20-layer CNN
94.08
80.10
95.05
53.03
75.15
DenseNet+GMP+weighted loss
97.50
92.43
97.85
75.21
90.28
DenseNet+Spp+unweighted loss
96.47
83.26
97.63
70.25
80.89
DenseNet+Spp+Weighted loss
99.26
97.37
99.39
92.23
96.76
Eq.4:
lfocal =
X
x∈X
ηι(x)(1 −pt)γln(pt), γ = 3
(5)
Its apparent from Eq.3 and Eq.4 that if a QRS complex
is correctly classiﬁed as non-PVC , yout can be small.In this
situation, pt = 1 −yout so that pt is large and the modu-
lating factor (1 −pt)γ in Eq.4 is small. On the contrary, if
a PVC QRS complex is misclassiﬁed as non-PVC,the mod-
ulating factor will be large. By using Eq.4 as loss func-
tion, the easily misclassiﬁed hard positive samples (PVC
samples) contribute more to the loss than the easy negative
samples so that the network can be more sensitive to PVC.
Figure.5 shows the comparison between weighted loss and
focal loss under the framework of denseNet with spatial
pyramid pooling (spp) layer.
Figure 5. Comparison between weighted loss and focal loss with
regard to sensitivity,speciﬁcity,accuracy,positive predictive value
and Youden’s index.
We can see that sensitivity(true positive rate TPR) is im-
proved which means that the network becomes more sensi-
tive to hard positive samples by training with focal loss.
4.6. Looking deeper into deep convolutional neural
network for PVC detection
A human doctor can easily distinguish PVC beat from
non-PVC beat through the obvious morphology features of
PVC depicted in electrocardiogram (ECG) caused by abnor-
mal electrical event of ventricles .As can be seen in Figure 1
top row,the QRS complex of a PVC beat is wider compared
to normal beat and depicts abnormality.And the direction of
the S-T segment and T wave is opposite to the QRS com-
plex.These are the most apparent morphology features to
which doctors are paying attention while detecting PVC.
The morphology of a PVC QRS complex can have num-
berous variations due to individuals difference and different
ECG devices.However,experienced doctors are still able to
correctly identify PVC regardless of these variations.This
is because they have learned the general features of PVC
and rely on those features for making diagnosis.Contrary
to general features are patient-speciﬁc features which are
unique to only a small number of individuals. If doctors
rely on patient-speciﬁc features to make diagnosis, theres
big chance of missed diagnosis.In other words,the sensitiv-
ity is expected to be low.The same is true to deep convo-
lutional neural network when its used to detect PVC. To
generalize well, the features learned by convolutional lay-
ers should be general and independent from speciﬁc indi-
viduals and ECG sampling rates.One way to know whether
features learned by a trained network is general or not is to
visualize what part of the input QRS complex the network
is focusing on in order to classify it as PVC. Using the tech-
niques described in [32], attention maps are generated for
some PVC inputs . The one-dimensional attention map is
of the same length as the input QRS complex. The inten-
sity value represents how much the network is focusing on
the part to generate the prediction. As can be seen in Fig-
ure 6 (a f),the highest attention intensity values are around
the location of S wave.This shows that the network thinks
an reverse S-T segment should be the criterion to classify
an QRS complex as PVC which is in accordance with doc-
tors experience.On the contrary,it can be imagined that if
the attention intensity values are distributed evenly across
the entire QRS complex or peaks at irrelevant locations,the
network is expected to have poor generalization capability.
5. Conclusion and discussion
We propose in our study an automated method combin-
ing densely connected convolutional neural network and a
2-level spatial pyramid pooling layer for PVC detection.The
proposed network can be trained using multiple databases
where the QRS complexes have different length and sam-
pling rates.Our method achieves comparable results on the
MIT-BIH arrhythmia database with current state-of -the -
art PVC detection network based on deep learning.And the
architecture of our proposed network is much more straight-
7


## Page 8


Figure 6. Examples of input QRS complex(top row) and the corresponding attention map(bottom row).
forward and easier to implement.
We demonstrate that
training using QRS complex of varied input size and sam-
pling rates helps improve overall performance compared us-
ing only a single database. The generalization capability of
our method is validated on 4 more databases other than the
MIT-BIH arrhythmia database and can be applied to a wider
range of ECG data collected by different devices.It remains
to be experimented whether the network can maintain good
performance when testing on ECG data with sampling rate
not included in training set. From the point of view of ob-
ject detection in 2-dimensioanl images, a bounding box is
predicted around the targeted object in an image.For the de-
tection of PVC ,the prediction should be a bounding box
in one-dimensional ECG time-series which is equivalent to
segmenting the QRS complex from an ECG cycle.An one-
dimensional DenseUNet which is trained end-to-end is pro-
posed to perform the task.As can be seen in Figure 7, the
max pooling operations between two transition layers in
Figure 2 are replaced by down-sampling and up-sampling
operation respectively as in UNet[23]. Different from tra-
ditional PVC detection methods which performs a binary
classiﬁcation towards a QRS complex, the proposed one-
dimensional DenseUNet performs a point-wise classiﬁca-
tion on a ECG cycle.As is illustrated in Figure.5, the net-
work takes as input an ECG cycle and outputs a sequence
of the same size as input that indicate the QRS complex
of PVC.The size of input can be arbitrary since there is no
fully connected layer in the network.The performance of de-
tecting PVC in the way as object detection in 2-dimensional
images needs further experiments.Besides,the proposed net-
work can be easily extended to the detection of other ar-
rhythmia such as atrial ﬁbrillation,premature atrial contrac-
tion(PAC) ,etc with a suitable database for training.
References
[1] J. L. M. A Perez-Silva.
Frequent ventricular extrasys-
toles: signiﬁcance, prognosis andtreatment.e-journal of the
esc council for cardiology practice. Biomedical Signal Pro-
cessing and Control, 9:17–28, 2011.
[2] S. C. Bollepalli, S. S. Challa, S. Jana, and S. Patidar. Atrial
ﬁbrillation detection using convolutional neural networks. In
Computing in Cardiology Conference, 2017.
[3] V. Chudek, G. Georgoulas, C. Stylios, M. Stavia, M. Hanu-
liak, and L. Lhotsk. Comparison of methods for premature
ventricular beat detection.
In International Special Topic
Conference on Information Technology in Biomedicine,
2008.
[4] A. et al. Detection of premature ventricular contraction ar-
rhythmias in electrocardiogram signals with kernel methods.
Signal Image and Video Processing, pages 931–942, 2014.
8


## Page 9


Figure 7. A deep learning network based on 1-dimensional denseUNet for PVC detection.
[5] C. et al. High-precision real-time premature ventricular con-
traction (pvc) detection system based on wavelet transform.
Journal of Signal Processing Systems, pages 289–296, 2014.
[6] G. et al. Physiobank, physiotoolkit, and physionet: com-
ponents of a new research resource for complex physiologic
signals. Circulation, 101(23):E215, 2000.
[7] M. L. et al. Atrial ﬁbrillation detection and ecg classiﬁcation
based on convolutional recurrent neural network. 2017.
[8] Z. R. et al. Effective and efﬁcient detection of premature
ventricular contractions based on variation of principal di-
rections. Digital Signal Processing, pages 93–102, 2016.
[9] R. Hadia, D. Guldenring, D. Finlay, A. Kennedy, G. Janjua,
R. Bond, and J. Mclaughlin. Morphology-based detection of
premature ventricular contractions. In Computing in Cardi-
ology Conference, 2017.
[10] G. Huang, Z. Liu, and K. Q. Weinberger. Densely connected
convolutional networks. pages 2261–2269, 2016.
[11] I. Jekova, G. Bortolan, I. Christov, I. Jekova, G. Bortolan,
and I. Christov. Pattern recognition and optimal parameter
selection in premature ventricular contraction classiﬁcation.
In Computers in Cardiology, pages 357 – 360, 2005.
[12] Y. Jung and H. Kim. Detection of pvc by using a wavelet-
based statistical ecg monitoring procedure. Biomedical Sig-
nal Processing and Control, 36:176–182, 2017.
[13] H. Kaiming, Z. Xiangyu, R. Shaoqing, and S. Jian. Spatial
pyramid pooling in deep convolutional networks for visual
recognition. IEEE Transactions on Pattern Analysis and Ma-
chine Intelligence, 37(9):1904–16, 2014.
[14] Y. e. a. Kaya. Feature selection using genetic algorithms for
premature ventricular contraction classiﬁcation. In nterna-
tional Conference on Electrical and Electronics Engineer-
ing, pages 1229–1232), 2015.
[15] J. S. Lim. Finding features for real-time premature ventric-
ular contraction detection using a fuzzy neural network sys-
tem.
IEEE Transactions on Neural Networks, 20(3):522–
527, 2009.
[16] M. e. a. Lin. Network in network. Computer Science, 2013.
[17] T. Y. Lin, P. Goyal, R. Girshick, K. He, and P. Dollar. Focal
loss for dense object detection. IEEE Transactions on Pat-
tern Analysis and Machine Intelligence, PP(99):2999–3007,
2017.
[18] M. S. Manikandan, B. Ramkumar, P. S. Deshpande, and
T. Choudhary.
Robust detection of premature ventricular
contractions using sparse signal decomposition and tempo-
ral features. Healthc Technol Lett, 2(6):141–148, 2015.
[19] G. B. Moody and R. G. Mark. The impact of the mit-bih
arrhythmia database. IEEE Engineering in Medicine and Bi-
ology Magazine, 20(3):45–50, 2002.
[20] A. A. Nugroho, N. Nuryani, I. Yahya, A. D. Sutomo, B. Hai-
jito, and A. Lestari. Premature ventricular contraction detec-
tion using artiﬁcial neural network developed in android ap-
plication. In Electric Vehicular Technology and Industrial,
Mechanical, Electrical and Chemical Engineering, pages
212–214, 2016.
[21] N. Nuryani, I. Yahya, and A. Lestari.
Premature ventric-
ular contraction detection using swarm-based support vec-
tor machine and qrs wave features. International Journal
of Biomedical Engineering and Technology, 16(4):306–316,
2014.
[22] P. Rajpurkar, A. Y. Hannun, M. Haghpanahi, C. Bourn, and
A. Y. Ng. Cardiologist-level arrhythmia detection with con-
volutional neural networks. 2017.
[23] O. Ronneberger, P. Fischer, and T. Brox. U-net: Convolu-
tional networks for biomedical image segmentation. In In-
ternational Conference on Medical Image Computing and
Computer-Assisted Intervention, pages 234–241, 2015.
[24] M. S. RS Kumar. Detection and classiﬁcation of premature
ventricular contraction using cross wavelet transform.
9


## Page 10


[25] J. Rubin,
S. Parvaneh,
A. Rahman,
B. Conroy,
and
S. Babaeizadeh. Densely connected convolutional networks
and signal quality analysis to detect atrial ﬁbrillation using
short single-lead ecg recordings. 2017.
[26] O. Sayadi, M. B. Shamsollahi, and G. D. Clifford. Robust
detection of premature ventricular contractions using a wave-
based bayesian framework. IEEE Transactions on Biomedi-
cal Engineering, 57(2):353–362, 2010.
[27] D. Smolen. Atrial ﬁbrillation detection using boosting and
stacking ensemble. In Computing in Cardiology Conference,
2017.
[28] A. e. a. Taddei. The european st-t database: standard for eval-
uating systems for the analysis of st-t changes in ambulatory
electrocardiography. European Heart Journal, 13(9):1164–
1172, 1992.
[29] I. D. G. H. Wisana, T. S. Widodo, M. Sja’Bani, and A. Su-
santo.
Identiﬁcation of premature ventricular contraction
ecg signal using wavelet detection. International Journal of
Computer Applications, 46(16):11–15, 2012.
[30] Y. Xia, N. Wulan, K. Wang, and H. Zhang. Atrial ﬁbrilla-
tion detection using stationary wavelet transform and deep
learning. In Computing in Cardiology Conference, 2017.
[31] J. Yang, Y. Bai, G. Li, M. Liu, and X. Liu. A novel method
of diagnosing premature ventricular contraction based on
sparse auto-encoder and softmax regression.
Bio-medical
materials and engineering, 26 Suppl 1(s1):S1549, 2015.
[32] M. D. Zeiler and R. Fergus. Visualizing and understanding
convolutional networks. 8689:818–833, 2013.
[33] F. Y. Zhou, L. P. Jin, and J. Dong. Premature ventricular
contraction detection combining deep neural networks and
rules inference. Artiﬁcial Intelligence in Medicine, 79, 2017.
[34] J. Zhou. Automatic detection of premature ventricular con-
traction using quantum neural networks. In Bioinformatics
and Bioengineering, 2003. Proceedings. Third IEEE Sympo-
sium on, pages 169–173, 2003.
10

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
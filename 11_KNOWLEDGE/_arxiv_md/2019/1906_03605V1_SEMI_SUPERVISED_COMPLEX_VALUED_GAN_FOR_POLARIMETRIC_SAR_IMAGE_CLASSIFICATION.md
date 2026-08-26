---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1906.03605v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1906.03605v1_Semi-supervised_Complex-valued_GAN_for_Polarimetric_SAR_Image_Classification

> Source: 1906.03605v1_Semi-supervised_Complex-valued_GAN_for_Polarimetric_SAR_Image_Classification.pdf

> Pages: 4

---


## Page 1


SEMI-SUPERVISED COMPLEX-VALUED GAN FOR POLARIMETRIC SAR IMAGE
CLASSIFICATION
Qigong Sun, Xiufang Li, Lingling Li, Xu Liu, Fang Liu, Licheng Jiao
Key Laboratory of Intelligent Perception and Image Understanding of Ministry of Education,
International Research Center for Intelligent Perception and Computation,
Joint International Research Laboratory of Intelligent Perception and Computation,
School of Artiﬁcial Intelligence, Xidian University, Xian, Shaanxi Province 710071, China
ABSTRACT
Polarimetric synthetic aperture radar (PolSAR) images are
widely used in disaster detection and military reconnaissance
and so on. However, their interpretation faces some chal-
lenges, e.g., deﬁciency of labeled data, inadequate utilization
of data information and so on. In this paper, a complex-valued
generative adversarial network (GAN) is proposed for the ﬁrst
time to address these issues. The complex number form of
model complies with the physical mechanism of PolSAR data
and in favor of utilizing and retaining amplitude and phase
information of PolSAR data. GAN architecture and semi-
supervised learning are combined to handle deﬁciency of la-
beled data. GAN expands training data and semi-supervised
learning is used to train network with generated, labeled and
unlabeled data. Experimental results on two benchmark data
sets show that our model outperforms existing state-of-the-art
models, especially for conditions with fewer labeled data.
Index Terms— PolSAR image classiﬁcation, complex-
valued operations, semi-supervised learning, generative ad-
versarial network
1. INTRODUCTION
Many researches have been done on PolSAR image classiﬁca-
tion, and breakthrough beneﬁts from the development and ap-
plication of deep convolutional neural networks(DCNN) [1].
As we all know, PolSAR data are usually expressed by coher-
ent matrices or covariance matrices which contain amplitude
and phase information in complex number form. However,
a general real-valued DNN loses signiﬁcant phase informa-
tion when it is applied to interpret PolSAR data directly. [2]
converts a complex-valued coherent or covariance matrix into
a normalized 6-D real-valued vector for PolSAR data clas-
siﬁcation, while ignoring important phase information. Dif-
ferent from direct conversion of complex number into a real
This work was supported in part by the State Key Program of National
Natural Science of China (No. 61836009, No. 91438201 and No. 91438103),
the National Natural Science Foundation of China (No.
61871310, No.
61876220).
number, some other strategies are introduced. Besides the
coherency matrix extended to the rotation domain, Chen et
al. [3] also take the null angle and roll-invariant polarimetric
features as input to extract ample polarimetric features. Liu et
al. [4] propose a novel polarimetric scattering coding method
for gaining more polarimetric features in classiﬁcation. How-
ever, their operations are all in the real number domain.
Instead, in order to make full use of PolSAR data in-
formation, some complex-valued DNN models are proposed.
Inspired by the application of complex-valued convolutional
neural network (CV-CNN) [5], Zhang et al [6] proposed the
application of CV-CNN on PolSAR data classiﬁcation and
obtained a great success. This is the beginning of CV-CNN
to classify PolSAR data. Besides retaining information, CV-
CNN has the strengths of faster learning and converenge [7].
In addition, deep learning is a data-driven approach. How-
ever, the labeled samples are extremely deﬁcient in PolSAR
data. Thus, unsupervised or semi-supervised networks are
used for the classiﬁcation of PolSAR data, for example, deep
convolutional autoencoder [8]. Meanwhile, GAN [9] is able
to expand data. It can learn the potential distribution of ac-
tual data and generate fake data that has the same distribu-
tion with actual data. With the successful application in many
ﬁelds (the generation of natural images [10] and Neural Di-
alogue [11] and so on), the GAN architecture has received
increasing attention in recent years. In order to further solve
the deﬁciency of labeled data, it is advisable to combine GAN
architecture and semi-supervised learning. Therefore, in this
paper, we propose a complex-valued GAN framework.
Our novel model has three advantages: 1) The complex-
valued neural network complies with the physical mechanism
of the complex numbers, and it can retain amplitude and
phase information of PolSAR data; 2) GAN extended to
complex number ﬁeld can expand PolSAR samples, which
have similar distribution with actual samples. Increased sam-
ples can improve the classiﬁcation performance of PolSAR
data. 3) Besides labeled data, unlabeled data are also used
to update model parameters by semi-supervised learning and
improve network performance to a certain extent.
arXiv:1906.03605v1  [eess.IV]  9 Jun 2019


## Page 2


2. SEMI-SUPERVISED COMPLEX-VALUED GAN
2.1. Network Architecture
The data generated by general real-valued GAN is differ-
ent from PolSAR data in feature and distribution.
There-
fore, we extend real-valued GAN to the complex number
domain and propose a complex-valued GAN. Figure 1 il-
lustrates the framework of our model, and it is composed
by Complex-valued Generator and Complex-valued Dis-
criminator.
This framework consists of complex-valued
full connection, complex-valued deconvolution, complex-
valued convolution, complex-valued activation function and
complex-valued batch normalization, which are represented
by ”CFC”, ”CDeConv”, ”CConv”, ”CA” and ”CBN”, respec-
tively. In addition, a complex-valued network also makes full
use of the amplitude and phase features of PolSAR data.
CA
CBN
CA
CA
-
-
...
+
+
...
-
+
CBN
CBN
CA
CA
-
+
C=1
C=2
C=3
C=4
C=K-1
C=K
.
.
.
Fake
Real
CA
...
...
CFC
CDeConv
CConv
CConv
Complex-valued Discriminator
Complex-valued Generator
1
3
2
Real Part
Imaginary Part
Reshape
Reshape
Fig. 1: The framework of semi-supervised complex-valued GAN for image
classiﬁcation. ⊖denotes minus arguments in element-wise and ⊕denotes
adds arguments in element-wise.
In the Complex-valued Generator, after a serious of
complex-valued operations, two randomly generated vec-
tors shown as the green block and blue block are translated
into a complex-valued matrix, which has the same shape
and distribution with PolSAR data. In the Complex-valued
Discriminator, we use complex-valued operations to extract
complete complex-valued features, which are in the form
of a pair. Then we concatenate the real part and imaginary
part of the last feature to the real domain for ﬁnal classiﬁca-
tion. In the training processing, generated fake data, labeled
and unlabeled actual data are used to alternately train this
complex-valued GAN by semi-supervised learning, and until
the network can effectively identify the authenticity of input
data and achieve correct classiﬁcation.
2.2. Complex-Valued Operation Mask
For simplifying the calculation, we choose the algebraic form
to express a complex number. In the algebraic form, the num-
bers in real part and imaginary part are real numbers with one
dimension. We use z1 = a + ib and z2 = c + id to denote
two complex numbers, the multiplication and addition are re-
deﬁned as follows:
z1 ∗z2
=
(a + ib) ∗(c + id)
(1)
=
(a ∗c −b ∗d) + i(a ∗d + b ∗d)
z1 ± z2
=
(a ± c) + i(b ± d)
(2)
To indicate the complex-valued operation mentioned in
detail, a complex-valued operation mask is proposed, as
shown in Figure 2. The green and the blue block represents
the real and imaginary part, respectively. This mask can make
some complex number calculations, whose input data (IN r,
IN i), the weight (W r, W i) and output data (OUT r,
OUT i) are consisted of a real part and an imaginary part.
Therefore, this type of operation can be decomposed to four
traditional real operations, one addition operation and one
subtraction operation. Each complex-valued operation in our
network complies with this mask. The same expression and
physical mechanism of data and network parameters in favor
of obtaining full data features used for classiﬁcation.
+
op
op
op
op
OUT_r
OUT_i
IN_r
IN_i
W_r
W_i
Complex-Valued 
Operation Mask
Fig. 2: Complex-Valued Operation Mask. The circular block denotes real-
valued operations, the red circles are undetermined operations and the violet
are explicit operations. ”op” can be full connection, convolution or deconvo-
lution.
2.3. Complex-Valued Batch Normalization
Batch normalization has been widely used in deep neural net-
works for unifying data and accelerate convergence rate. In
addition, complex-valued batch normalization can stabilize
the performance of GANs. However, scanty training samples
and less batch sizes restrict the effect of batch normalization.
In order to address this issue, a novel batch normalization
is proposed in this paper. The expectation and covariance ma-
trices are replaced by constantly updated average expectation
and covariance matrices, so that they hold all sample informa-
tion in training proceeding. The following formulation shows
the normalization of the tth batch xt :
ˆxt = ( ¯Vt)−1
2 (xt −¯σt)
(3)
where ¯σt and ¯Vt represent the average expectation and co-
variance matrix from t −m to t batches, which is computed
as follows:
¯σt
=
1
m
t
X
t−m
E [xt]
(4)
¯Vt
=
 ¯V t
rr
¯V t
ri
¯V t
ir
¯V t
ii

(5)
=
 1
m
Pt
t−m V t
rr
1
m
Pt
t−m V t
ri
1
m
Pt
t−m V t
ir
1
m
Pt
t−m V t
ii

where m denotes the length of state remembered, and ¯Vri is
equal to ¯Vir. The square root of a Matrix of 2 times 2 ¯Vt is
computed:


## Page 3


St
=
( ¯V t
rr × ¯V t
ii −¯V t
ri × ¯V t
ri)
1
2
(6)
Tt
=
( ¯V t
rr + ¯V t
ii + 2St)
1
2
(7)
¯V
−1
2
t
=
" ( ¯V t
ii+St)
StTt
−
¯V t
ri
StTt
−
¯V t
ri
StTt
( ¯V t
rr+St)
StTt
#
(8)
This operation can translate the data mean to 0 and vari-
ance to 1. Ultimately, we use the following computing to de-
note complex-valued batch normalization:
BN(ˆxt) = γˆxt + β
(9)
where γ and β are deﬁned as two parameters to reconstruct
the distribution.
2.4. Semi-Supervised Learning
In this complex-valued GAN, for further utilizing features of
unlabeled data, we use semi-supervised learning to optimize
network with a classiﬁer of softmax. The output of genera-
tor (G) is a K + 1 dimensional vector {p1, p2, ..., pK, pK+1},
where from p1 to pK are the probability of ﬁrst K classes and
pK+1 is the probability of input image being fake. In order to
optimize the generator (G) and discriminator (D), we deﬁne
the loss function as follows:
L
=
Llabeled + Lunlabeled + Lgenerated
(10)
Llabeled
=
−E [logP(C|Xreal, C < K + 1)]
(11)
Lunlabeled
=
−E [log [1 −P(C = K + 1|Xreal)]] (12)
Lgenerated
=
−E [logP(C = K + 1|Xfake)]
(13)
where Llabeled, Lunlabeled and Lgenerated represent classiﬁ-
cation loss of labeled samples, unlabeled samples, and gener-
ated samples, respectively. Therefore, classiﬁcation losses of
labeled and generated samples are easily acquired. However,
the classiﬁcation loss of unlabeled samples is not easy to ex-
press because of inexplicit ground truth. With this inevitable
problem, the output probability of softmax is operated as fol-
lows:
psum = log
K
X
i=1
e(p−pmax) + pmax
(14)
where pmax denotes the max value in pi (i < K + 1), and
logistic regression as a binary classiﬁcation is utilized. When
the output approaches 1, the probability pK+1 << psum ac-
cordingly, the facticity of data is discriminated. By this de-
duction, unlabeled data can also be used to update our net-
work model.
3. EXPERIMENTS
In our experiments, two benchmarks data sets of Flevoland
and San Francisco are used. In order to verify the effective-
ness of our method, our model is compared with complex-
valued convolutional neural network (CV-CNN) and real-
valued convolutional neural network (RV-CNN), they have
similar conﬁgurations with our Complex-valued Discrimina-
tor. The overall accuracy (OA), average accuracy (AA), and
Kappa coefﬁcient are used to measure the performance of all
the methods.
3.1. Experiments on Standard Data Set
We use a coherent matrix T, which is a 3 × 3 conjugate sym-
metrical complex value matrix and follows complex Wishart
distribution, to express all information of the corresponding
pixel on PolSAR images. In Flevoland data, 0.2%, 0.5%,
0.8%, 1.0%, 1.2%, 1.5%, 1.8%, 2.0%, 3.0%, 5.0% labeled
data in each of 15 categories are randomly selected as training
data, and the remained labeled data for testing. In addition,
10% unlabeled samples are used to train our semi-supervised
complex-valued GANs. In San Francisco data, we randomly
chose 10, 20, 30, 50, 80, 100, 120,150, 200, 300 labeled data
in each of the 5 categories for training and 10% data, no mat-
ter whether labeled, as actual samples.
0.75
0.8
0.85
0.9
0.95
1
0
0.5
1
1.5
2
2.5
3
3.5
4
4.5
5
Overall Accuracy (% )
Sample Rate (% )
0.75
0.8
0.85
0.9
0.95
1
0
0.5
1
1.5
2
2.5
3
3.5
4
4.5
5
Average Accuracy (% )
Sample Rate (% )
0.75
0.8
0.85
0.9
0.95
1
0
0.5
1
1.5
2
2.5
3
3.5
4
4.5
5
Kappa
Sample Rate (% )
RC
CC
Ours
RC
CC
Ours
RC
CC
Ours
Fig. 3: Flevoland OA, AA, and Kappa in different sample ratios.
55
60
65
70
75
80
85
90
95
100
0
50
100
150
200
250
300
Overall Accuracy (% )
Sample Number
RC
CC
Ours
55
60
65
70
75
80
85
90
95
100
0
50
100
150
200
250
300
Average Accuracy (% )
Sample Number
RC
CC
Ours
60
65
70
75
80
85
90
95
100
0
50
100
150
200
250
300
Kappa
Sample Number
RC
CC
Ou
rs
Fig. 4: San Francisco OA, AA, and Kappa in different sample numbers.
Table 1: Classiﬁcation accuracy(%), OA(%), AA(%) and Kappa
Flevoland
methods
1
2
3
4
5
6
7
8
9
RC
87.18
97.85
95.56
94.58
86.72
93.96
98.17
98.89
96.70
CC
90.79
98.39
95.95
89.71
93.00
93.21
97.46
99.24
97.54
ours
98.22
99.25
99.29
86.71
95.40
95.27
99.85
99.85
98.59
methods
10
11
12
13
14
15
OA
AA
Kappa
RC
94.88
97.70
83.45
95.56
99.00
52.95
95.12
91.54
94.68
CC
98.02
97.01
91.18
90.48
98.91
65.57
95.12
93.10
94.68
ours
97.56
97.76
96.07
99.06
100.0
87.38
97.21
96.68
96.97
San Francisco
methods
1
2
3
4
5
OA
AA
Kappa
RC
99.16
86.86
59.93
19.29
31.52
74.36
59.35
63.37
CC
99.07
84.05
53.81
65.51
50.14
80.83
70.51
72.41
ours
99.45
88.33
86.72
61.91
90.61
89.23
85.41
84.48
The parameters of all experiments in this paper are set as
follows: the patch size is 32 × 32, the learning rate is 0.0005,
and the optimization method is Adam with β1 = 0.5 and
β2 = 0.999. Figure 3 and Figure 4 show the change of OA,
AA, and Kappa with the sample ratio in two data sets. In
Flevoland data, the results veriﬁed the superiority of our new
network with less labeled samples, and this law especially
obvious when training samples less than 3.0%. This same
advantage also is shown in San Francisco data, especially if
numbers of training data less than 50. In order to exhibit the
contributions of our model on each category, we list all test
accuracy of Flevoland data with 0.8% sampling ratio and of
San Francisco data with 10 labeled training samples in Table
1. In Flevoland data, we can ﬁnd that accuracies of different


## Page 4


categories have generally improved especially for the ﬁfteenth
category, which has the least training samples and achieves in-
crease of 65.1% and 33.17% compare to the real-valued and
complex-valued neural networks in accuracy, respectively. In
San Francisco data, comparing to the complex-valued neural
network, complex-valued GAN further improves classiﬁca-
tion accuracy than the real-valued neural network, especially
for Developed, Low-Density Urban and High-Density Urban
with the increase of 44.7%, 220.9%, 187.4%.
3.2. Generated Data Analysis
In order to analyze the effectiveness of our complex-valued
GAN, we discuss the similarity of actual and generated data
in appearance and distribution. Take Flevoland data for ex-
ample, we randomly select 100 pcolors of the real part in di-
agonal elements of T, as shown in Figure 5. We can clearly
ﬁnd that generated data have high similarity with actual data.
Based on the known data distribution of T matrix [12], we
further count the distribution of actual and generated data in
Figure 6. For actual data, the real and imaginary part statis-
tic histograms of T11 shown in (a1) and (a2) and of T12 in
(a3) and (a4). (b1) - (b4) represent the corresponding statistic
histograms of generated T11 and T12. We can ﬁnd the high
similarity of generated data with actual data.
(a1)
(a2)
(a3)
(a4)
(b1)
(b2)
(b3)
(b4)
Fig. 5: Pcolor comprised by real parts of T11, T22, T33. (a1 - a4) show the
actual data image patches. (b1 - b4) show the generated data image patches.
(a1)
(a2)
(a3)
(a4)
(b1)
(b2)
(b3)
(b4)
Fig. 6: Histograms of representative variables. (a1 - a4) are the statistics of
actual data, and (b1 - b4) are the statistics of generated data.
4. CONCLUSION
In this paper, a complex-valued GAN is proposed to classify
PolSAR data. Nearly all operations are extended to the com-
plex number ﬁeld, and this model obeys the physical mean-
ing of PolSAR data and holds complete phase and amplitude
feature. To the best of our knowledge, this is the ﬁrst time
that complex-valued data is generated by a network, and the
generated data is similar to actual complex-valued data in ap-
pearance and distribution The complex-valued GAN is alter-
nately trained with generated data, labeled data and unlabeled
data by semi-supervised learning. With the utilization of un-
labeled and generated samples features, our complex-valued
semi-supervised GAN obtains obviously precede over other
models especially when labeled samples are insufﬁcient. It
opens up a new way for our researches on solving the prob-
lem of lacking complex-valued samples.
5. REFERENCES
[1] Alex Krizhevsky, Ilya Sutskever, and Geoffrey E Hinton, “Im-
agenet classiﬁcation with deep convolutional neural networks,”
in NIPS, 2012, pp. 1097–1105.
[2] Yu Zhou, Haipeng Wang, Feng Xu, and Ya-Qiu Jin, “Polari-
metric sar image classiﬁcation using deep convolutional neural
networks,” IEEE Geoscience and Remote Sensing Lett., vol.
13, no. 12, pp. 1935–1939, 2016.
[3] Si-Wei Chen and Chen-Song Tao, “Polsar image classiﬁca-
tion using polarimetric-feature-driven deep convolutional neu-
ral network,” IEEE Geoscience and Remote Sensing Lett., vol.
15, no. 4, pp. 627–631, 2018.
[4] Xu Liu, Licheng Jiao, Xu Tang, Qigong Sun, and Dan Zhang,
“Polarimetric convolutional network for polsar image classiﬁ-
cation,” IEEE Trans. Geosci. Remote Sens., 2018.
[5] Nitzan Guberman, “On complex valued convolutional neural
networks,” arXiv preprint arXiv:1602.09046, 2016.
[6] Zhimian Zhang, Haipeng Wang, Feng Xu, and Ya Qiu Jin,
“Complex-valued convolutional neural network and its appli-
cation in polarimetric sar image classiﬁcation,” IEEE Trans.
Geosci. Remote Sens., vol. PP, no. 99, pp. 1–12, 2017.
[7] T Nitta,
“On the critical points of the complex-valued
neural network,”
in Neural Information Processing, 2002.
ICONIP’02. Proceedings of the 9th International Conference
on. IEEE, 2002, vol. 3, pp. 1099–1103.
[8] Jie Geng, Jianchao Fan, Hongyu Wang, Xiaorui Ma, Baom-
ing Li, and Fuliang Chen, “High-resolution sar image clas-
siﬁcation via deep convolutional autoencoders,” IEEE Geo-
science and Remote Sensing Lett., vol. 12, no. 11, pp. 2351–
2355, 2015.
[9] Ian Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing
Xu, David Warde-Farley, Sherjil Ozair, Aaron Courville, and
Yoshua Bengio, “Generative adversarial nets,” in NIPS, 2014,
pp. 2672–2680.
[10] Alec Radford, Luke Metz, and Soumith Chintala, “Unsuper-
vised representation learning with deep convolutional genera-
tive adversarial networks,” arXiv preprint:1511.06434, 2015.
[11] Jiwei Li, Will Monroe, Tianlin Shi, S´ebastien Jean, Alan Ritter,
and Dan Jurafsky, “Adversarial learning for neural dialogue
generation,” arXiv preprint:1701.06547, 2017.
[12] Nathaniel R Goodman, “Statistical analysis based on a certain
multivariate complex gaussian distribution (an introduction),”
The Annals of mathematical statistics, vol. 34, no. 1, pp. 152–
177, 1963.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
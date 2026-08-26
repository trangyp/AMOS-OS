---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1906.03607v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1906.03607v1_Pixel_DAG-Recurrent_Neural_Network_for_Spectral-Spatial_Hyperspectral_Image_Clas

> Source: 1906.03607v1_Pixel_DAG-Recurrent_Neural_Network_for_Spectral-Spatial_Hyperspectral_Image_Clas.pdf

> Pages: 4

---


## Page 1


PIXEL DAG-RECURRENT NEURAL NETWORK FOR SPECTRAL-SPATIAL
HYPERSPECTRAL IMAGE CLASSIFICATION
Xiufang Li, Qigong Sun, Lingling Li, Zhongle Ren, Fang Liu, Licheng Jiao
Key Laboratory of Intelligent Perception and Image Understanding of Ministry of Education,
International Research Center for Intelligent Perception and Computation,
Joint International Research Laboratory of Intelligent Perception and Computation,
School of Artiﬁcial Intelligence, Xidian University, Xian, Shaanxi Province 710071, China
ABSTRACT
Exploiting rich spatial and spectral features contributes to
improve the classiﬁcation accuracy of hyperspectral images
(HSIs). In this paper, based on the mechanism of the popula-
tion receptive ﬁeld (pRF) in human visual cortex, we further
utilize the spatial correlation of pixels in images and propose
pixel directed acyclic graph recurrent neural network (Pixel
DAG-RNN) to extract and apply spectral-spatial features for
HSIs classiﬁcation. In our model, an undirected cyclic graph
(UCG) is used to represent the relevance connectivity of pix-
els in an image patch, and four DAGs are used to approximate
the spatial relationship of UCGs. In order to avoid overﬁtting,
weight sharing and dropout are adopted. The higher classiﬁ-
cation performance of our model on HSIs classiﬁcation has
been veriﬁed by experiments on three benchmark data sets.
Index Terms—
Hyperspectral images classiﬁcation,
spectral-spatial, structural sequentiality, recurrent neural net-
works, directed acyclic graphs (DAGs)
1. INTRODUCTION
HSIs usually provide abundant spectral and spatial informa-
tion of ground targets. Therefore, their interpretations such
as the classiﬁcation has been widely used in the geological
survey, vegetation research and so on. However, the sufﬁ-
cient and efﬁcient utilization of spectral and spatial informa-
tion in HSIs classiﬁcation is challenging such as Hughes phe-
nomenon [1]. A large number of researches have been done
on the classiﬁcation of HSIs from traditional methods such
as independent component analysis (ICA) [2] to popular deep
convolutional neural network (DCNN) [3].
Due to the increase of spectral dimension and nonlinear of
spectral space, some traditional methods are not appropriate
to classify HSIs. Subsequently, ensemble learning method
is proposed for HSIs classiﬁcation such as [4].
However,
This work was supported in part by the State Key Program of National
Natural Science of China (No.61836009, No. 91438201 and No. 91438103),
the National Natural Science Foundation of China (No.
61871310, No.
61876220, No. 61801351)).
most of ensemble learning methods only consider the spectral
rather than spectral-spatial information. Then, some sparsity-
based algorithms, for instance [5], are used to extract spatial-
spectral features. These methods are incapable of capturing
robust and abstract features with the complex and varied en-
vironment.
Recently, deep neural network (DNN) has attracted more
attentions due to its advantages of extracting high-rank ab-
stract features and achievements in computer vision and natu-
ral language process, such as the images classiﬁcation [6] and
speech recognition [7]. Y. Chen et al. [8] proposed 3-D CNN,
it is the ﬁrst time to extract spectral-spatial features of HSIs
simultaneously by DCNN, and this method improves classi-
ﬁcation performance obviously. L. Mou et al. [9] take hyper-
spectral pixels as sequential data and apply recurrent neural
network (RNN) to classify HSIs. These above methods ex-
tract robust spatial-spectral information in HSIs classiﬁcation
by multilayer convolutional neural network. We know, these
convolution processes used to extract pixel features utilize the
ideology of receptive ﬁeld. However, this operation only ex-
tracts the feature of every pixel and ignore the correlation of
adjacent pixels which is signiﬁcant to realize category in the
pRF. For detail, the perception ability of the pRF in the hu-
man visual cortex [10] is related to the focus of the vision and
surrounding scenes. The inﬂuence of surrounding scenes on
the central target reduces with the increase of interval. Here,
we use UCG and DAG to describe this relation. Due to the
ability of RNN on dealing with sequence data, we proposed a
Pixel DAG-RNN model for HSIs classiﬁcation.
This new method has three advantages: (1) Our model fur-
ther applies the pRF mechanism of the human visual system
in identifying the pixel category. Besides the pixel feature,
we further consider the spatial correlation of adjacent pixels.
(2) We apply UCGs and DAGs to represent the correlation of
pixels and RNN to apply spatial sequence features for HSIs
classiﬁcation. This model makes full use of both spectral in-
formation and spatial correlations of pixels. (3) In order to
prevent the overﬁtting phenomenon caused by a limited num-
ber of training samples, weight sharing and dropout are used.
arXiv:1906.03607v1  [cs.CV]  9 Jun 2019


## Page 2


2. PIXEL DAG-RECURRENT NEURAL NETWORK
2.1. Motivation
Distance
Correlation
(c)
(d)
(a)
(b)
hV4
20
0
-20
-20
0
20
hV4
Fig. 1: (a) Schematic diagram of the human cerebral cortex, where hV4 is
marked by red rectangle box. (b) The pRFs spatial array of hV4. A series of
different size circles are used to denote pRFs. (c) An 9 × 9 image patch with
the center pixel represents target unit. (d) The diagram of correlation with
distance
We know, in the human vision system, that sounding
scenes also affect the realization of the central target and
these effects obey visual mechanism.
In the pRF mecha-
nism of the human visual system, which illustrated in Fig.1
(a), more intensive attentions are focused on the central target
and the attentions on sounding scenes because blur and sparse
with increased distance as shown in Fig.1 (b). Based on this
theoretical mechanism, we utilize the same principle of iden-
tifying pixel categories. The importance of surrounding layer
pixels on central pixel reduces with the increased interval.
Fig.1 (c) shows the reduced importance of surrounding pixel
layers on a central pixel by shallower color. Fig.1 (d) express
the variance curve of the importance of surrounding pixel
layers on the central pixel with the distance.
These rules
demonstrate the importance of spatial structure sequentiality
in understanding images. In addition, RNN is more suitable
for processing sequence data. Therefore, on the basis of the
mechanism of pRF mechanism of the human visual system
in HSIs classiﬁcation, we used UCGs and DAGs to connect
pixels and design Pixel DAG-RNN to extract spectral-spatial
features.
2.2. Pixel DAG-RNN
h
v
vij
hij
hi-1j
hij-1
hi-1j-1
v11
v12
v1n
v21
v22
vnn
v2n
vn2
vn1
...
...
...
...
...
...
...
hnn
...
...
yˆ
Fig. 2: Architecture of Pixel DAG-RNN for classiﬁcation. The leftmost is
a sample of 8-neighborhood DAG in the southeast direction.
As shown in Fig. 2, a sample of directed acyclic graph
(DAG) can be represented as G = {V, A}, where V = {vij}
denotes the vertex set and A = {−−−→
vijvpq} denotes the arc
set, which i, p represent the row and j, q represent the col-
umn from 1 to n, −−−→
vijvpq represents the arc from vertex vij to
vpq. We can get a series of contextual dependencies among
vertexes and input them to a recurrent neural network. Subse-
quently, hidden layer h are generated with the same structure
as G. h(vij) denotes the value of hidden layer at vij, which
is related to its local input x(vij) and the hidden representa-
tion of its predecessors. Due to the special structure of hidden
layer h, we should calculate it sequentially. The hidden layer
h and output ˆy are computed as follows:
ˆh(vij)
=
X
vpq∈PG(vij)
G(Sh(vpq) + a)
(1)
h(vij)
=
H(Ux(vij) + V ˆh(vij) + b)
(2)
ˆy
=
F(Wh(vnn) + c)
(3)
where S, U, V, W and a, b, c represent the connection weights
and biases. PG(vij) is the direct predecessor set of vertex vij
in the DAG, F(·), G(·) and H(·) are the nonlinear activation
functions. From the above formulas, we can see that this is an
autoregressive model with the following conditional distribu-
tions:
p(h(vij)|h(vi−1j−1), h(vi−1j), h(vij−1), x(vij))
(4)
The recurrent weights S, U, V are shared in order to avoid
overﬁtting. When calculating the hidden layer h, we start at
the DAG’s source vertex v11 and calculate the next vertex of
the hidden layer according to the structure of DAG, until to
the last vertex vnn. Therefore, h(vnn) include the information
of all the DAG’s vertex. A nonlinear function F(·) is used to
obtain the ﬁnal output ˆy. Loss l is denoted as follows:
l = L(ˆy, y)
(5)
where y represents real label, L(·) denotes loss function.
2.3. Pixel DAG-RNN for HSIs Classiﬁcation
In HSIs classiﬁcation, each pixel having hundreds of spec-
tral data is classiﬁed into a class of object. In order to apply
the neighborhood information, we use UCG to represent the
spatial relationship of the image
patch and then apply four different DAGs to approximate
the topology of the UCG. Based on DAG’s deﬁnition in spa-
tial structural sequentiality of pixels, we apply DAG-RNNs
model to classify HSIs for making full use of the spatial struc-
tural sequentiality of pixels as shown in Fig. 3. The spectral-
spatial features are extracted by Pixel DAG-RNNs, and then
we concatenate the four feature vectors at the end vertex to a
ﬁnal vector. Two full connection layers and softmax are used
for the ﬁnal classiﬁcation.
The detail of using DAGs to approximate UCG is illus-
trated in Fig.
4.
Suppose we make an image patch with
the size of n × n. The black unit denotes the target pixel.
8 neighborhood UCG is used to represent the spatial rela-
tionship of pixels. Because of its loopy property, we can’t
get a ﬁxed sequence applied in RNNs. In order to fully use
the semantic contextual dependencies of the image patch, we
use the combination of a set of small DAGs with the height
and width being (n/2 + 1) to represent the UCG. Four 8
neighborhood DAGs are respectively used in the end vertex as


## Page 3


Pixel DAG-RNN
Pixel DAG-RNN
Pixel DAG-RNN
Pixel DAG-RNN
Pixel DAG-RNN
Pixel DAG-RNN
Feature Extraction
Feature Fusion
Original HSI
Classification Result
Image Decomposition
Fig. 3: Architecture of Pixel DAG-RNN for HSIs classiﬁcation
the target unit. Those four dictionaries are southeast, south-
west, northeast, and northwest. Therefore, we can route any-
where orderly and use the information of any pixel in the im-
age patch. The order of calculation is row by row and pixel
by pixel within every row, suggested by [11]. Pixel DAG-
RNN is applied to each DAG to generate the hidden layer hd
(d ∈{southeast, southwest, northeast, northwest}), so
as to take advantage of the local feature with a broader view
of contextual awareness. Those operations can be expressed
as follows:
ˆh(vij)
d
=
X
vpq∈PGd(vij)
G(Sh(vpq) + a)
(6)
h(vij)
d
= H(Ux(vij) + V ˆh(vij)
d
+ b)
(7)
where S, U, V and a, b are the connection weights and biases,
h(vij)
d
is the hidden layer at vertex vij in d direction DAG.
PGd(vij) is the direct predecessor set of vertex vij in direc-
tion d . Here, the weights and biases are shared across all
vertexes in direction d. The memory length is (n/2 + 1). Our
Fig. 4: Schematic diagram of image patch decomposition. The black unit
denotes target pixel.
proposed model can sequentially get the feature from edge
to center, because of the accumulation of the parameters in
the forward process, the information of the neighborhood is
gradually weakened. It is consistent with the principle: the
importance of surrounding pixel to central pixel reduces with
the increased interval.
3. EXPERIMENTAL RESULTS AND ANALYSIS
In this experiment, we use three benchmark datasets: Indian
Pines data, University of Pavia data, and Kennedy Space Cen-
ter data and their size are 145×145, 610×340, and 512×614,
respectively. Their usable number of bands are 200, 115 and
176 respectively. In addition, in order to verify the effective-
ness of our method, we choose the RBF-SVM, SOMP, 3D-
CNN as contrast experiments and take overall accuracy (OA),
average accuracy (AA), and Kappa coefﬁcient in the form of
mean standard deviation to measure the performance of our
model.
3.1. Parameters Setting and Experiment Results
For all experiments, the numbers of labeled samples for train-
ing and testing are the same as 3-D CNN experiments [8]. The
experiment parameters in Indian Pines data as follows: SOMP
uses 7 × 7 square window. The window size of 3D-CNN is
31 × 31, and the convolution kernel size is 4 × 4. For Pixel
DAG-RNN, we use 8 neighborhood information and DAG-
RNN with 128 dimensions to extract features. In addition, the
block size is 13 × 13, the learning rate is 0.005 and dropout
is 0.4. The parameters of experiments on University of Pavia
data are listed: the window sizes of SOMP and 3-D CNN are
9×9 and 27×27 respectively. For Pixel DAG-RNN, four 6×6
DAGs are used to represent the 11 × 11 image patch. In KSC
data, SOMP uses 7 × 7 window, and the parameters of 3-D
CNN is the same as University of Pavia data. In Pixel DAG-
RNN, the patch size is 13 × 13. An 8 neighborhood UCG
to represent the contextual awareness, and then combine four
DAGs to approximate the topology of UCG. Besides 8 neigh-
borhood UCG, we also use a 4 neighborhood UCG to repre-
sent an image patch. The overall results of different methods
on three data sets are listed in Table 1.
In Table 1, we can ﬁnd that 8-P-DAG-RNN obtains the
best classiﬁcation performance compared with other meth-
ods on OA, AA and Kappa. Compare to other four mod-
els which apply spatial-spectral features, RBF-SVM obtain
lower classiﬁcation accuracy because of its only feature ex-
traction on spectral dimension. In University of Pavia and
KSC data, 3-D CNN obtains slightly higher accuracies on
OA,AA and Kappa. However, in Indian Pines data, SOMP
and 3-D CNN obtain nearly the same classiﬁcation perfor-


## Page 4


mances due to more categories with fewer training samples
which is adverse condition for deep neural network. Because
4-P-DAG-RNN don’t consider diagonal connections between
units in UCG, it obtains some losses on classiﬁcation accu-
racy compared to 8-P-DAG-RNN. On the whole, our novel
model 8-P-DAG-RNN has the best classiﬁcation performance
because of its further use of the spatial contextual depen-
dency.
Table 1: OA(%), AA(%) and Kappa
method
RBF-SVM
SOMP
3D-CNN
4-P-DAG-
RNN
8-P-DAG-
RNN
Pines
OA
82.20±0.39
95.10±0.39
94.93±0.65
95.13±0.76
96.42±0.24
AA
87.95±0.86
93.71±1.33
95.37±1.04
95.18±1.23
96.58±0.31
Kappa
0.863±0.005
0.943±0.005
0.941±0.008
0.944±0.009
0.959±0.003
Pavia
OA
89.42±0.40
97.34±0.54
98.61±0.57
98.75±0.29
99.29±1.75
AA
89.62±0.24
95.68±0.54
98.47±0.40
98.28±0.36
99.07±0.28
Kappa
0.859±0.005
0.964±0.007
0.981±0.008
0.983±0.004
0.990±0.002
KSC
OA
89.04±1.35
92.65±1.43
94.29±0.90
96.00±0.52
97.45±0.72
AA
85.61±1.62
92.34±1.71
92.71±1.35
93.13±0.73
95.75±1.17
Kappa
0.878±0.015
0.918±0.016
0.936±0.010
0.956±0.006
0.972±0.008
For further expressing contributions of our model on each
class, we listed the classiﬁcation accuracies of all categories
on KSC data in Table 2. From Table 2, we ﬁnd that 8-P-
DAG-RNN obtains the highest accuracy in 8 of 13 categories,
such as ”Surb”, ”Slash pine”, ”Graminoid marsh”, ”Spartina
marsh”, ”Cattail marsh”, ”Salt marsh”, ”Mud ﬂats”, ”Water”.
Other ﬁve classes obtain the second or third high accuracy
because of their fewer training samples. In addition, we anal-
yse the inﬂuence of memory length on classiﬁcation accuracy.
As mentioned in 3.2, an image patch can be decomposed into
four small image patches and the size of small image patch
is called as memory length, such as the memory length of
Fig.
4 is 4.
Through experiments with different memory
length(m={5,6,7,8}) of image patches on three datasets, we
ﬁnd that when the memory length is 6, the University of Pavia
dataset can reach the best performance(OA = 99.29length for
the Indian Pines and KSC datasets is 7
Table 2: classiﬁcation accuracy for every class(%)on the KSC data set.
Method
RBF-SVM
SOMP
3D-CNN
4-P-DAG-
RNN
8-P-DAG-
RNN
Scrub
92.37±2.92
98.13±1.31
94.48±2.32
97.75±1.36
98.27±1.31
Willow swamp
85.39±4.08
95.34±4.88
84.08±10.77
90.61±5.64
95.28±3.80
CP hammock
90.58±1.91
97.84±2.14
83.30±5.94
93.82±5.11
97.34±1.34
Slash pine
74.19±5.71
85.20±4.43
83.67±7.62
85.32±6.74
89.63±4.61
Oak/Broadleaf
70.36±6.08
92.33±6.22
92.86±3.65
73.13±7.93
85.09±8.29
Hardwood
55.58±8.61
91.53±4.29
89.87±4.79
84.02±4.99
88.18±4.81
Swamp
94.34±3.95
100.00±0.00
99.09±1.52
92.11±6.14
95.30±4.24
Graminoid marsh
75.09±7.41
78.76±5.84
93.55±4.70
97.24±2.01
97.73±1.92
Spartina marsh
98.27±1.35
94.63±3.08
91.91±4.66
99.83±0.26
99.95±0.10
Cattail marsh
95.31±2.75
95.11±2.40
96.39±6.34
99.54±0.47
99.69±0.40
Salt marsh
95.66±2.23
99.18±0.52
97.48±2.57
99.15±0.31
99.50±4.12
Mud ﬂats
87.68±5.11
72.43±10.27
98.59±2.42
98.11±1.92
98.78±1.23
Water
98.16±0.50
100.00±0.00
100.00±0.00
100.00±0.00
100.00±0.00
4. CONCLUSION
In this paper, we use Pixel DAG-RNN to extract spectral-
spatial features for HSIs classiﬁcation. It can effectively ex-
ploit the spatial correlation of pixels by UCG and then combi-
nation of four directed acyclic graphs (DAGs) to approximate
the UCGs topology. In addition, this model also utilizes the
advantage of RNN on extracting and using sequence data in
network architecture. The superiority of Pixel DAG-RNN has
been veriﬁed by experiments on three benchmark HSIs data
sets. Further, weights sharing and dropout are used to prevent
overﬁtting. The future work will devote to use pixel informa-
tion efﬁciently.
5. REFERENCES
[1] Antonio Plaza, Jon Atli Benediktsson, Joseph W Boardman,
Jason Brazile, Lorenzo Bruzzone, Gustavo Camps-Valls, Jo-
celyn Chanussot, Mathieu Fauvel, Paolo Gamba, Anthony
Gualtieri, et al.,
“Recent advances in techniques for hyper-
spectral image processing,” Remote sensing of environment,
vol. 113, pp. S110–S122, 2009.
[2] Alberto Villa, J´on Atli Benediktsson, Jocelyn Chanussot, and
Christian Jutten, “Hyperspectral image classiﬁcation with in-
dependent component discriminant analysis,”
IEEE Trans.
Geosci. Remote Sens., vol. 49, no. 12, pp. 4865–4876, 2011.
[3] Jun Yue, Wenzhi Zhao, Shanjun Mao, and Hui Liu, “Spectral–
spatial classiﬁcation of hyperspectral images using deep con-
volutional neural networks,” Remote Sensing Letters, vol. 6,
no. 6, pp. 468–477, 2015.
[4] Bj¨orn Waske, Sebastian van der Linden, J´on Atli Benedikts-
son, Andreas Rabe, and Patrick Hostert, “Sensitivity of support
vector machines to random feature selection in classiﬁcation of
hyperspectral data,” IEEE Trans. Geosci. Remote Sens., vol.
48, no. 7, pp. 2880–2889, 2010.
[5] Jianing Wang, Licheng Jiao, Hongying Liu, Shuyuan Yang,
and Liu Fang,
“Hyperspectral image classiﬁcation by spa-
tialspectral derivative-aided kernel joint sparse representation,”
IEEE Journal of Selected Topics in Applied Earth Observations
Remote Sensing, vol. 8, no. 6, pp. 2485–2500, 2015.
[6] Alex Krizhevsky, Ilya Sutskever, and Geoffrey E Hinton, “Ima-
genet classiﬁcation with deep convolutional neural networks,”
in Advances in neural information processing systems, 2012,
pp. 1097–1105.
[7] Alex Graves, Abdel-rahman Mohamed, and Geoffrey Hinton,
“Speech recognition with deep recurrent neural networks,” in
Acoustics, speech and signal processing (icassp), 2013 ieee in-
ternational conference on. IEEE, 2013, pp. 6645–6649.
[8] Yushi Chen, Hanlu Jiang, Chunyang Li, Xiuping Jia, and Pe-
dram Ghamisi, “Deep feature extraction and classiﬁcation of
hyperspectral images based on convolutional neural networks,”
IEEE Trans. Geosci. Remote Sens., vol. 54, no. 10, pp. 6232–
6251, 2016.
[9] Lichao Mou, Pedram Ghamisi, and Xiang Zhu Xiao, “Deep
recurrent neural networks for hyperspectral image classiﬁca-
tion,” IEEE Transactions on Geoscience Remote Sensing, vol.
55, no. 7, pp. 3639–3655, 2017.
[10] Brian A Wandell and Jonathan Winawer, “Computational neu-
roimaging and population receptive ﬁelds,” Trends in cognitive
sciences, vol. 19, no. 6, pp. 349–357, 2015.
[11] Aaron van den Oord, Nal Kalchbrenner, Lasse Espeholt, Oriol
Vinyals, Alex Graves, et al., “Conditional image generation
with pixelcnn decoders,” in Advances in Neural Information
Processing Systems, 2016, pp. 4790–4798.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
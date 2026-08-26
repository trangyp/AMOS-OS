---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1812.09648v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1812.09648v1_Chinese_Herbal_Recognition_based_on_Competitive_Attentional_Fusion_of_Multi-hier

> Source: 1812.09648v1_Chinese_Herbal_Recognition_based_on_Competitive_Attentional_Fusion_of_Multi-hier.pdf

> Pages: 16

---


## Page 1


Chinese Herbal Recognition based on Competitive Attentional Fusion of
Multi-hierarchies Pyramid Features
Yingxue Xu, Guihua Wen ∗, Yang Hu †, Mingnan Luo, Dan Dai, Yishan Zhuang
School of Computer Science & Engineering, South China University of Technology
Panyu, Guangzhou, Guangdong, China
{201530381885@mail., crghwen@, cssuperhy@mail., csluomingnan@mail., csdaidan@mail., cszhuangyishan@mail.}scut.edu.cn
Abstract
Convolution neural netwotks (CNNs) are successfully
applied in image recognition task. In this study, we explore
the approach of automatic herbal recognition with CNNs and
build the standard Chinese herbs datasets ﬁrstly. According
to the characteristics of herbal images, we proposed the
competitive attentional fusion pyramid networks to model the
features of herbal image, which mdoels the relationship of
feature maps from different levels, and re-weights multi-level
channels with channel-wise attention mechanism. In this way,
we can dynamically adjust the weight of feature maps from
various layers, according to the visual characteristics of
each herbal image. Moreover, we also introduce the spatial
attention to recalibrate the misaligned features caused by
sampling in features amalgamation. Extensive experiments
are conducted on our proposed datasets and validate the
superior performance of our proposed models. The Chinese
herbs datasets will be released upon acceptance to facilitate
the research of Chinese herbal recognition.
1. Introduction
Deep convolution neural networks (CNNs) have achieved
a grate success on in the ﬁeld of image processing[30,
31, 17, 11] and been applied on object detection and
recognition[13, 24, 28] and get a better performance. As
a kind of poor side effect, simple and noninvasive treatment,
Chinese herbs are widely used in China and a number of
Asian countries for healthcare[39, 37]. Therefore, there are
wide application values and signiﬁcance for recognizing Chi-
nese herbs automatically. However, as far as we know, there
is no research on this task and meanwhile it is difﬁcult to
train models for herbal recognition due to a lack of sufﬁcient
herbs data.
In this paper, we ﬁrst propose a CNN model to deal with
∗corresponding author
†equal contribution with Guihua Wen
Chinese herbal recognition task, based on which we present
a standard dataset for Chinese herbal recognition. Distin-
guishing from regular task of object recognition[13, 17] and
ﬁne-grained image recognition[10, 43], the former focus on
distinguishing the outline and shape of object and the lat-
ter need more detailed features to identify so that they can
classify with similar shape but different details. For Chinese
Herbal recognition, we would be confronted with the above
two cases: (a) some herbs are so distinguishing that they
are easy to be classiﬁed with the shape features instead of
detailed features. (b) some herbs with similar shapes usually
need to be classiﬁed by more ﬁne-grained features. The fea-
tures extracted from convolution layers of different depth are
rich in diversity that the features from earlier layers are more
representational and from deeper layers are more abstract
and contain more semantics in contrast[24, 22]. According
to the aforementioned challenges of herbal recognition, we
choose Feature Pyramid Networks[22] (FPN) to merge fea-
tures from different levels so that we can diversify image
features overall to improve the performance of herbal recog-
nition with CNNs.
Compared with the traditional FPN[22], in this study, we
ﬁrst introduce channel-wise attention[16] in the process of
fusing features from different levels. In this way, our models
can dynamically adjust the weights of features from differ-
ent levels, which makes it possible to adjust the extent of
selecting features encoding from various levels adaptively.
Furthermore, we also combine spatial attention[21] to spa-
tially recalibrate the misaligned features caused by serveral
upsampling or downsampling operators during feed-forward
propagation.
More importantly, the channel-wise and spatial attention
are both improved in this paper as follows: (a) The origi-
nal SE mechanism is limited on re-scaling the weights of
features from the same layers, while the competitive atten-
tion proposed in this paper extends the modeling ranges
of channel-wise attention, as same as spatial attention, and
explicitly model the competitive channel dependencies be-
tween spatial and semantic informations in the process of
1
arXiv:1812.09648v1  [cs.CV]  23 Dec 2018


## Page 2


fusion on various levels. (b) The feature maps from bottom-
up pathway, which are abundant in more spatial informa-
tions to provide references for the misaligned and spatially
coarser features from top-down pathway, are introduced into
the process of spatial attentional modeling to recalibrate the
misaligned features. Based on the above improvement of
attention according to our speciﬁc structures and tasks, we
can jointly model channel relationship of various levels and
channel dependencies between spatial and semantic infor-
mation ﬂows, as well as recalibration on misaligned features
spatially.
With aforementioned methods we proposed, we try our
best to improve the performance of Chinese herbal recog-
nition. Consequently, the contributions in this study can be
concluded as follows:
1. We build and present the standard Chinese-Herbs recogni-
tion dataset (CNH-98), further, we build the corresponding
tiny-Chinese-Herbs dataset (TCNH-98), which is used to
train models for locally recognition of herbs.
2. We introduce both channel-wise and spatial attention
mechanism into pyramid networks and further improve their
structures to propose channel-wise competitive attention and
spatial reference attention. The former focus on modeling
channel dependencies between spatial and semantic informa-
tion ﬂows and the latter tends to recalibrate the misaligned
features with spatial information ﬂows for reference.
3. We ﬁrst apply pyramid ConvNet to Chinese herbal recog-
nition according to the characteristic of recognition task.
4. We conduct experiments on the datasets we proposed to
validate the superior performance of presented models on
the task of Chinese herbal recognition.
2. Related Work
Feature Pyramid. Feature pyramid network is proposed
to get image features at different scales[22], based on this
motivation, numerous methods with multi-level features in
CNN have been proposed, such as RoI pooling[11] or us-
ing skip-connection to construct pyramid[26]. With RoI
pooling on proposal region, HyperNet[20], ParseNet[25]
and ION[3] concatenate features of multiple layers before
computing predictions and [4, 38] also aggregate context
in different scales with spatial pooling. Feature pyramid
like Stacked Hourglass network[26] is the typical structure
with skip-connection, which combines different levels fea-
tures for key point estimation. Inspired by Hourglass Mod-
ule, FPN[22] designs a network with strong semantic at all
scales for object detection and FANet[42] improves it further
by augmenting lower-level feature maps. Several other ap-
proaches including PRM[40] for pose estimation, U-Net[29]
for segmentation and RON[19] for object detection handling
features at multi-level by skip connections. In our work, we
introduce an attentional fusion method based on FPN[22] to
competively model the relationship between spatial informa-
tion and semantics for Chinese Herbal Recognition.
Attention in CNN. With the trend of attention widely
applied on the modeling process of CNNs[27], it is com-
monly used for two primary aspects: channel-wise atten-
tion [16] to explicitly model interdependencies between
channels and the other one to re-weight the image spatial
signals[33, 21, 35, 43]. Furthermore, some models com-
bine both spatial and channel-wise attention, such as SCA-
CNN[6, 23]. However, the mentioned models are limited
on local region. To solve this problem, self-attention [34, 9]
is proposed to capture long-range dependencies between
local and global. Additionally, there are some attention mod-
els based on domain knowledge [5, 7]. Interaction-aware
pyramid[8] also introduce attention to the network for mod-
eling long-range relationship. Different from [8], our pro-
posed attention mechanism based on the speciﬁc structure
of FPN[22] explicitly models a trade off between spatial and
semantic informations for Chinese Herbal recognition.
CNN Applied on Tasks like Herbal Recognition.
There are some similar tasks using CNN with Chinese Herbal
recognition such as plants recognition [32], which mainly
focus on leaf recognition[15, 2]. Moreover, another similar
tasks like ﬂower recognition[12, 36] can also use CNN to
achieve. As far as we konw, there has been no one using
CNN to recognize Chinese Herbs so far and we propose this
approach ﬁrstly.
3. Chinese-Herbs Dataset Collection
The Chinese-Herbs Dataset (CNH-98) is a collection of
9184 images of 98 categories covering the common Chinese
herbs. Furthermore, we make a crop of each image into
serveral tiny images without overlapping to construct a
Tiny-Chinese-Herbs Dataset (TCNH-98) including 51198
images, because each image always contains multiple
repeated herbs. These two datasets are divided randomly
into training and validation sets with the proportion of 4:1.
Fig. 1 shows some examples of CNH-98 (left) and their
crop TCNH-98 (right). The sample datasets are available1.
3.1. Chinese-Herbs Dataset
In this dataset, most of the images were acquired by
taking photos ourselves in the medicinal herbs stores,
hospitals and so on. And the others were collected from the
Google images[1]. The smallest dimension of images is
about 250 pixels. Each class contains 94 images on average
and more than 41 classes include over 100 images. In order
to ensure the availability and matching of labels and data,
the labels were reviewed by the human annotators.
1https://github.com/scut-aitcm/
Chinese-Herbs-Dataset
2


## Page 3


Angelica, Szechuan Lovage Rhizome, Unibract Fritillary Bulb, Thorowax Root, 
Flos Daturae, glossy ganoderma, Lotus seed, Star Anise, Momordica charantia,  
Desert Cistanche
Star Anise, Momordica Charantia, Red Dates, Dried Tangerine Peel,  Phaseolus Calcaratus, 
Thorowax Root, Saffron, Chinese Wolfberry, Poris Cocos, SElfheal, Lophatherum Gracile, 
Liquorice, ...
Figure 1: Examples from the proposed CNH-98 dataset (left) and TCNH-98 dataset (right).
3.2. Tiny-Chinese-Herbs Dataset
Tiny dataset was sampled from above CNH-98 dataset
with the size of 32 × 32 and we ensured that there was
no overlapping. Considering that there are some factors
interfering with the quality of the image, such as blank place
in the origin and so on, we dropped some images in the
following conditions, as judged by the annotators: (i) the
images were blank or the proportion of herbs in images is
too small, (ii) not contain herbs (like some containers or
background), (iii) the annotators cannot recognize such as
the parts of original herbs. Overall, we gained an average of
522 images per class and minimum 100 per class.
We need to make a statement that the Tiny-Chinese-Herbs
dataset may bring more severe challenges in herbal recogni-
tion, due to the limited image size and incomplete features
of herbs, although the scale of this dataset is bigger.
4. Competitive Attentional Fusion Pyramid
Networks
In this section, considering the characteristics of Chi-
nese herbal recognition tasks, we ﬁrst extend applications
on Feature Pyramid Network (FPN[22]) to Chinese herbal
recognition tasks. Next, we propose a competitive attentional
fusion mechanism based on the original FPN to adapt to the
aforementioned tasks. Finally, in terms of existing problem
of misaligned features, a spatial recalibtration method is pro-
posed, which will be combined with the above attentional
fusion mechanism.
4.1. Apply FPN to Chinese Herbal Recognition
Figure 2: FeaturePyramid. Here we extract feature maps
from four levels of ResNet-18 to form a feature pyramid.
For herbal recogniton tasks, there is a characteristic that
the shapes of some herbs are so distinguishing that they
are easy to be classiﬁed using the high-resolution features
from the lower level of networks, while some herbs with
similar shapes usually need to be classiﬁed by features from
the higher level, which contain more ﬁne-grained semantic
informations. The feature maps from various layers of net-
works are shown in Fig. 2. Therefore, we choose FPN[22]
applied to Chinese herbal recognition, because FPN can fuse
multi-hierarchies features with its pyramid structure.
Consisting of two pathway, a bottom-up pathway and a
top-down pathway, and lateral connections, FPN can build
a feature pyramid with high-level semantics throughout by
naturally exploiting a ConvNet’s pyramid feature hierarchy.
The bottom-up pathway is the feed-forward computation of
3


## Page 4


the backbone ConvNet, which results in a feature hierarchy
containing feature maps at several scales with a scaling step
of 2. And the top-down pathway generates higher resolution
features by upsampling the last groups of feature maps by a
factor of 2 on the bottom-up pathway. Here we record the
output of upsampling as XUi ∈RWi×Hi×Cd. As opposed to
the features on the same level from the bottom-up pathway,
these feature maps are spaitally coarser, but semantically
stronger, hence we natrually refer the bottom-up pathway to
the spatial ﬂow and the top-down pathway to the semantic
ﬂow. As described in the design of FPN, the output of last
layer of ith level via lateral connections XLi ∈RWi×Hi×Cd
merges with the corresponding feature maps with the same
size from top-down pathway, as follows:
XPi = XLi + XUi,
(1)
where XPi will be fed into the next upsampling process. The
result is a fusion feature pyramid that has strong semantic
and spatial informations at all scales.
4.2. Competitive Attention between Spatial and Se-
mantic Flows
The aforementioned fusion mode of features in FPN is
to indiscriminately treat spatial and semantic ﬂows at all
scales, which is likely to cause redundencies in fusion fea-
tures. From an intuitional point of view, we propose a com-
petive attention mechanism that allows the network to explic-
itly modeling the competition between spatial and semantic
ﬂows in the process of fusion, such that the network can
selectively emphasis richer semantic or spatial features and
suppress redundant ones.
To achieve this, we gain the global information ˆuspa and
ˆusem, embedding from feature maps via lateral connections
of spatial ﬂow XL = [x1
L, x2
L, . . . , xC
L] and upsampling fea-
ture maps of semantic ﬂow XU = [x1
U, x2
U, . . . , xC
U] respec-
tively:
ˆuc
spa = Fsq(xc
L) =
1
W × H
W
X
i=1
H
X
j=1
xc
L(i, j),
(2)
ˆuc
sem = Fsq(xc
U) =
1
W × H
W
X
i=1
H
X
j=1
xc
U(i, j),
(3)
where Fsq(·) denotes the operation of global pooling. The
combination of ˆuspa and ˆusem will be used as joint input for
the excitation operation to capture channel-wise dependen-
cies between spatial and semantic ﬂows:
s = Fex([ˆu1
spa, ˆu2
spa, . . . ,
ˆuC
spa, ˆu1
sem, ˆu2
sem, . . . , ˆuC
sem], wex)
= Fex([ˆuspa, ˆusem], wex)
= σ(ReLU([ˆuspa, ˆusem], w1), w2),
(4)
where [·] refers to the concatenation of the feature-
maps produced in the above squeeze operation from
two ﬂows, and parameters w1 ∈R
2C
t ×2C and w2 ∈
R2C× 2C
t .
The result s of Excitation operator Fex(·) is
[s1, s2, . . . , sC, sC+1, sC+2, . . . , s2C] that will divide into
two parts to rescaling the weights of features XL and XU
respectively as follows:
˜xc
spa = Fscale(sc
spa, xc
L)
= Fse(XL)[·] × XL = sc
spa · xc
L,
(5)
˜xc
sem = Fscale(sc
sem, xc
U)
= Fse(XU)[·] × XU = sc
sem · xc
U,
(6)
where sspa refers to [s1, s2, . . . , sC] and ssem means
[sC+1, sC+2, . . . , s2C].
The competition between spatial
and semantic ﬂows is modeled by the Competitive Atten-
tion module proposed above and react to each channel of
both spatial and semantic ﬂow. On the one hand, the afore-
mentioned mergence mode of features can be regarded as a
adaptive competition between two ﬂows and its recalibration
depends on two ﬂows adaptively to dynamically adjust the
complement weights for each other. On the other hand, a
trade off between spatial and semantic ﬂows is indicated.
Finally, the Competitive Attention module is reformulated
as:
XP = Fse(XL) · XL + Fse(XU) · XU,
(7)
Fig. 3 shows the overview of our Competitive Attentional
Fusion Pyramid Network and its more details in Competi-
tive Attention module. It is concluded that the difference
between the typical SE and the Competitive Attention is
that based on the particular structure and meanings of FPN
we simultaneously introduced two ﬂows into SE to model
their channel relationship competitively and trade off, and
meanwhile we adjust two ﬂows at the same time.
4.3. Spatial Reference Recalibration
As we discuss above, the upsampling features before
merging are spatially coarser because they are products of
several downsampling or upsampling operators. In other
words, their spatial informations such as location are less
accurate and even misaligned. That is also why we need
fusion features.
However, it should be noted that the above amalgamation
means of element-wise addition extremely rely on the spatial
informations, thus it is likely that the fusion features merged
in this way are sub-optimal. Consequently, we introduced
a method to spatially recalibrate the misaligned features
through modeling spatial attention on pixel-level with spatial
ﬂows for reference. As discussed in Harmonious-Spatial-
Attention[21] (HA), similarly we compresses the feature
maps in the following ways (global cross-channel averaging
4


## Page 5


N
W
1 (
)
−
N
N
U
P
X
X
Global Pool
Global Pool
FC
FC
concatenate
iL
X
i
U
X
/
C
t
C
1
1
d
C


1
1
d
C


1
1
2
d
C


1
1
2
d
C


iP
X
…
Competitive 
Attention
…
…
…
Residual
Blocks
Residual
Blocks
Up Sampling
Up Sampling
Up Sampling
concatenate
Residual
Blocks
i
W
i
H
i
C
N
W
N
H
N
C
i
W
i
H
d
C
d
C
N
W
N
H
d
C
d
C
d
C
d
C
d
C
d
C
1 1
d
C

1 1
d
C

1 1
d
C

1 1
d
C

i
W
i
H
i
H
1
i
W +
1
i
H +
1
i
H +
1
i
W +
1
N
W
−
1
N
H
−
N
H
1
1
Nd
C

Top-down
Bottom-up
1
+
iL
X
1
+
i
U
X
i
U
X
1
−
N
P
X
1
+
iP
X
iP
X
i
X
Residual
Blocks
1
N
W
−
1
N
H
−
1
N
C
−
1
N
W
−
1
N
H
−
1
N
C
−
1
i
W +
1
i
H +
1
i
C +
1
i
W +
1
i
H +
1
i
C +
d
C
1
i
W +
1
i
H +
d
C
1
i
W +
1
i
H +
1
−
N
L
X
Competitive 
Attention
i
W
iL
X
Competitive 
Attention
Stacked Residual 
Blocks
Stacked Residual 
Blocks
any shape
any color
any shape
any color
1×1 Conv
1×1 Conv
Global Pool
Global Pool
Up Sampling
Up Sampling
Stacked Residual 
Blocks
any shape
any color
1×1 Conv
Global Pool
Up Sampling
Legends 
d
C
1
N
W
−
1
N
H
−
d
C
1
N
W
−
1
N
H
−
N
W
1 (
)
−
N
N
U
P
X
X
Global Pool
Global Pool
FC
FC
concatenate
iL
X
i
U
X
/
C
t
C
1
1
d
C


1
1
d
C


1
1
2
d
C


1
1
2
d
C


iP
X
…
Competitive 
Attention
…
…
…
Residual
Blocks
Residual
Blocks
Up Sampling
Up Sampling
Up Sampling
concatenate
Residual
Blocks
i
W
i
H
i
C
N
W
N
H
N
C
i
W
i
H
d
C
d
C
N
W
N
H
d
C
d
C
d
C
d
C
d
C
d
C
1 1
d
C

1 1
d
C

1 1
d
C

1 1
d
C

i
W
i
H
i
H
1
i
W +
1
i
H +
1
i
H +
1
i
W +
1
N
W
−
1
N
H
−
N
H
1
1
Nd
C

Top-down
Bottom-up
1
+
iL
X
1
+
i
U
X
i
U
X
1
−
N
P
X
1
+
iP
X
iP
X
i
X
Residual
Blocks
1
N
W
−
1
N
H
−
1
N
C
−
1
i
W +
1
i
H +
1
i
C +
d
C
1
i
W +
1
i
H +
1
−
N
L
X
Competitive 
Attention
i
W
iL
X
Competitive 
Attention
Stacked Residual 
Blocks
any shape
any color
1×1 Conv
Global Pool
Up Sampling
Legends 
d
C
1
N
W
−
1
N
H
−
Competitive 
Attention Module
A group of 
Feature Maps
Figure 3: Overview of Competitive Attentional Fusion Pyramid Network and Competitive Attention modules.
pooling) to reduce parameters for the subsequent conv layer,
but unlike HA we Simultaneously model two ﬂows:
Si
spa = 1
c
C
X
j=1
XL
i
1:h,1:w,j,
(8)
Si
sem = 1
c
C
X
j=1
XU
i
1:h,1:w,j,
(9)
where Si
spa and Si
sem will be concatenated to Si
=
[Si
spa, Si
sem] fed into the next conv layer of 3 × 3 ﬁlters
with stride 2 and then resized to original size by bilinear
interpolation with the factor of 2. Finally, we add the scaling
conv layer of 1 × 1 ﬁlters for reducing aliasing effect of
bilinear upsampling. As a result, we gain 2 feature maps
to rescale values of features from two ﬂows on pixel-level
respectively. In addition, this mechanism also contributes
to the robustness of network which allows it to use different
upsampling methods on the top-down pathway.
Aming to combine the competitive attention with spatial
recalibration, we further attach two 1 × 1 × Cd convolution
layer after tensor multiplication on two ﬂows respectively,
since the two procosses are not mutually independent. Fi-
nally, we deploy the sigmoid operations to normalise. More
details of SRR-module and its combination with Competitive
attention are shown in Fig. 4.
5. Experiments
5.1. Implementation Details
For fair comparison, each plain FPN and its correspond-
ing CA, SRR and SRR-CA counterparts are trained with
identical optimisation schemes. For CNH-98 and TCNH-98
datasets, we train our all models with three degrees of data
augmentation: no data augmentation, standard data augmen-
tation (+) and mixup[41], an advanced data augmentation
technology. On CNH-98, the standard data augmentation
(translation/mirroring) is adopted for training set and the
224x224 crop is randomly sampled. All images normalized
with mean values and standard deviations. When testing, our
implementation follows the practice in [16]. On TCNH-98,
we follows the standard practice and data augmentation in
[13] for CIFAR. All models were trained by optimizer SGD
with 0.9 Nesterov momentum from scratch.
During training on CNH-98, we train our models with
batch size 64 and 300 epochs for standard augmentation and
mixup, 120 epochs for no augmentation. The learning rate
is initialized to 0.1 and divided by 5 at epochs 120, 200, 260
for standard augmentation and mixup and at epochs 30, 60,
90 for no augmentation , and weight decay are adopted with
0.0005 and 0.0001 respectively. In particular, we train mod-
els for mixup on the last 20 epochs with traditional strategy.
During training on TCNH-98, our models are trained for
5


## Page 6


Spatial Reference Recalibration Module
 Spatial Reference Recalibration Module
Global Pool
Global Pool
FC
FC
concatenate
iL
X
i
U
X
/
C
t
C
1
1
d
C


1
1
d
C


1
1
2
d
C


1
1
2
d
C


iP
X
Global Cross-
Channel Pool
Global Cross-
Channel Pool
{3×3×2, 2}
Resize
{1×1×2, 1}
Sigmoid
Sigmoid
concatenate
1
H W

1
H W

2
H W

2
H W

d
H W C


d
H W C


SRR-CA Module
1 1
1
{
, }
dC

1 1
1
{
, }
dC

1 1
1
{
, }
dC

1 1
1
{
, }
dC

a conv layer: filter shape and stride
a fully-connected layer
 Spatial Reference Recalibration Module
Global Pool
Global Pool
FC
FC
concatenate
iL
X
i
U
X
/
C
t
C
1
1
d
C


1
1
d
C


1
1
2
d
C


1
1
2
d
C


iP
X
Global Cross-
Channel Pool
Global Cross-
Channel Pool
{3×3×2, 2}
Resize
{1×1×2, 1}
Sigmoid
Sigmoid
concatenate
1
H W

1
H W

2
H W

2
H W

d
H W C


d
H W C


SRR-CA Module
1 1
1
{
, }
dC

1 1
1
{
, }
dC

a conv layer: filter shape and stride
a fully-connected layer
Figure 4: Spatial Reference Recalibration module and its
combination with Competitive Attention module. The Batch
Normalisation[18] (BN) (attached to two conv layers after
tensor multiplication) is not shown for brevity. We resize
feature maps in SRR module with the factor of 2 by bilinear
interpolation.
300 epochs with batch size 128 and the initial learning rate
is 0.1 and is divided by 10 at 100th, 150th, 200th epochs.
We also set the weight decay as 0.0001 following [13] for
CIFAR. Especially, learning rate during training without data
augmentation was divided by 5 at epochs 30, 60, 90.
5.2. Results of Chinese Herbal Recognition
We evaluate our methods on the CNH-98 and TCNH-98
datasets with pre-act ResNet[14] for backbone networks and
the results of contrastive experiments for FPN with/without
CA and SRR-CA modules are shown in Table. 1, and we
can make a summary as follows:
First of all, as shown in D1 and D2 in the Table. 1, we
can see FPN indeed gets a better results than pre-act ResNet
whether on CNH-98 or TCNH-98, which veriﬁes the guess in
Section 4.1 that FPN is more suitable to accomplish the task
of Chinese herbal recognition, and here we record the exper-
iment on FPN as baseline. Furthermore, for both CNH-98
and TCNH-98, FPN-CA can achieve superior performance
than baseline and FPN-SRR-CA can further improve per-
formance across different depth or keep the effect at least
without too much extra parameters.
Secondly, FPN-SRR almost can exceed FPN except on
CNH-98 without data augmentation, proving the effective-
ness of SRR modules in most case and suggesting that CA
and SRR modules are not two separate processes but need to
model jointly, hence it is reasonable to attach 1 × 1 convolu-
tion layer after combination of SRR and CA modules. For
the reason of performance of SRR on CNH-98 with no aug-
mentation, we infer that there is an overﬁtting phenomenon
owing to the small size of CNH-98 dataset. Moreover, on
CNH-98 dataset, compared with FPN-34, FPN-SRR-CA-
18 even increases validation accuracy rates by 1.7% for no
augmentation, 1.2% for standard augmentation and achieve
or slightly go beyond of FPN-34 for mixup. In particular,
FPN-SRR-CA-18 has higher accuracy rates than FPN-SRR-
CA-34 for no augmentation, for which we infer that the
depth 34 of networks for small dataset like CNH-98 is too
deep to ﬁt and our CA and SRR-CA modules can reduce
overﬁtting as well as improving the generalization ability of
models thus perform better with deeper networks. On the
contrary, during training on TCNH-98 that consists of 40958
images with standard augmentation and mixup, we notice
that there is an underﬁtting for the depth 20 of networks,
which indicates the representation of the models with depth
20 is too limited, and we increased the depth of networks,
which can reduce this phenomenon, proving the performance
of models with deeper networks can get better.
The mixup[41] can be seen as an advanced method of
data augmentation. However, for TCNH-98 dataset, mod-
els with mixup achieve the worse results, for which we
argue that mixup as augmentation approaches would further
aggravate underﬁtting, leading to a worse result natrually.
Due to the limited representation of networks with depth 20,
actually TCNH-98 dataset is suitable for deeper networks,
proved by results of experiments on models with depth 56,
which reduces underﬁtting.
5.3. Further Analysis and Discussion
The analysis of last section 5.2 has proven the effective-
ness of CA and SRR-CA modules. In this section, from
an intuitive angle of view, we discuss the effects of our ap-
proaches. The internal feature maps from different levels
of three models, FPN-18, FPN-CA-18, FPN-SRR-CA-18,
are shown in the top part of Fig. 5, from which we can con-
clude that our methods can strengthen the representation of
networks. By observing the representation of feature maps,
the previous layers of FPN almost extract contour features,
while the features are increased with more detailed infor-
mations using our FPN-CA models, compared with feature
maps of FPN with/without CA on level 1 and 2 in Fig. 5. It
is worth mentioning that the features extracted by the models
with CA modules are more sparse and accurate, compared
to the original FPN, especially for feature maps of level 3.
Moreover, SRR-CA modules can further spatially recalibrate
the misaligned feature maps, mainly for deeper features, typ-
ically shown in level 3 of Fig. 5, which makes the features
with stronger spatial informations and richer in semantic.
6


## Page 7


D1: Chinese-Herbs
Model
backbone depth
parames
CNH-98
CNH-98+
CNH-98 mixup
pre-act ResNet-18[14]
18
11.7M
74.5
91.7
93.3
FPN-pre-act ResNet-18[22]
18
13.3M
74.7
91.9
93.5
FPN-CA-18(Ours)
18
13.4M
75.3
92.9
94.2
FPN-SRR-18(Ours)
18
13.3M
72.5
92.5
93.8
FPN-SRR-CA-18(Ours)
18
13.8M
76.8
93.5
94.1
FPN-pre-act ResNet-34[22]
34
23.4M
75.1
92.3
94.1
FPN-CA-34(Ours)
34
23.5M
76.1
93.5
94.6
FPN-SRR-34(Ours)
34
23.4M
-
92.7
-
FPN-SRR-CA-34(Ours)
34
23.9M
76.3
93.8
94.8
D2: Tiny-Chinese-Herbs
Model
backbone depth
parames
TCNH-98
TCNH-98+
TCNH-98 mixup
pre-act ResNet-20[14]
20
0.28M
63.0
74.8
72.8
FPN-pre-act ResNet-20[22]
20
0.31M
63.1
75.2
72.9
FPN-CA-20(Ours)
20
0.31M
62.8
75.8
73.6
FPN-SRR-20(Ours)
20
0.31M
-
75.5
73.3
FPN-SRR-CA-20(Ours)
20
0.31M
63.8
75.8
73.7
FPN-pre-act ResNet-56[22]
56
0.89M
64.3
77.4
77.4
FPN-CA-56(Ours)
56
0.89M
63.1
77.7
76.7
FPN-SRR-CA-56(Ours)
56
0.90M
62.8
77.6
77.6
Table 1: Accuracy rates(%) of different methods on datasets CNH-98 and TCNH-98, the best records of our models are bold.
We compare our models with the original FPN and its backbone networks, trained with either no data augmentation, standard
augmentation (+) and mixup.
Additionally, we statistics the distributions of the activation
of CA modules on FPN-CA and FPN-SRR-CA models, and
we can see that the attentional activation values of CA and
SRR modules are very vigorous and distinguish, and the
heatmap of SRR modules can reconstruct the distribution
of the origin, which suggests that our methods indeed con-
tribute to re-weighting and recalibrating features.
As shown in the distribution of channel-wise attentional
outputs, we can see the activation values of features from
deeper layers are always uniform and tend to 0.5, for the
reason that features from deeper layers have been adjusted
during training, thus CA modules perform less adjustment.
It is noticed that the activation values on the deepest level
of spatial ﬂow are almost higher than the ones from seman-
tic ﬂow, while from deep to previous, the activation from
semantic ﬂow would stand out from the competition gradu-
ally. This conﬁrmes our conjecture that high-level features
is spatially coarser and strongly semantic, in contrast to low-
level features, and simultaneously indicates the mechanism
we proposed can complement spatial or semantic informa-
tions for requirements of different levels. Correspondingly,
there are same conclusion on the analysi of heatmap activa-
tion of SRR modules. Compared with channel-wise atten-
tional outputs between FPN-CA and FPN-SRR-CA, there is
a trend that channel-wise activation of FPN-SRR-CA would
be more stable than FPN-CA owing to the effectiveness of
SRR, which enables features more accurate and the effects
of SRR can be passed through the network.
6. Conclusion
In this paper, we ﬁrstly propose the standard Chinese
Herbs dataset for recognition. Based on the characteristic
of Chinese herbal recognition task, we introduce attention
mechanism into pyramid networks to model channel relation-
ship of features from various levels. Furthermore, we also
improve channel-wise and spatial attention and propose com-
petitive attention and spatial reference recalibration module,
which respectively model channel dependencies between
spatial and semantic ﬂows in the process of feature fusion
and spatially recalibrate the misaligned feature maps with
spatial ﬂow for reference. With improved pyramid network,
we apply it to the Chinese herbal recognition and evaluate
our methods on CNH-98 and TCNH-98 dataset we proposed
as well as getting superior performance to the traditional
pyramid networks.
References
[1] Google images.
Website.
http://images.google.
com/.
[2] F. Ayaz, A. Ari, and D. Hanbay. Leaf recognition based on ar-
tiﬁcial neural network. In International Artiﬁcial Intelligence
and Data Processing Symposium, pages 1–5, 2017.
7


## Page 8


(a)
(a)
(b)
(b)
(c)
(c)
Feature maps of four level from bottom to top on models: (a) FPN, (b) FPN-CA, (c) FPN-SRR-CA
(level 1 to 2)
(level 2 to 3)
(level 3 to 4)
(b) Activation of CA on FPN-CA
(c) Activation of CA on FPN-SRR-CA
(level 1 to 2)
(level 2 to 3)
(level 3 to 4)
(a)
(a)
(b)
(b)
Heatmaps of SRR 
Attention of 
(a) spatial flows on 
bottom-up 
pathway,
(b) semantic flows 
on top-down 
pathway.
(level 1 to 2)
(level 2 to 3)
(level 3 to 4)
Lateral
Top-down
 Unibract Fritillary Bulb
(a)
(b)
(c)
Feature maps of four level from bottom to top on models: (a) FPN, (b) FPN-CA, (c) FPN-SRR-CA
(level 1 to 2)
(level 2 to 3)
(level 3 to 4)
(b) Activation of CA on FPN-CA
(c) Activation of CA on FPN-SRR-CA
(level 1 to 2)
(level 2 to 3)
(level 3 to 4)
(a)
(b)
Heatmaps of SRR 
Attention of 
(a) spatial flows on 
bottom-up 
pathway,
(b) semantic flows 
on top-down 
pathway.
(level 1 to 2)
(level 2 to 3)
(level 3 to 4)
Lateral
Top-down
 Unibract Fritillary Bulb
Figure 5: Top: internal feature maps of an example from four levels on three models: (a) FPN, (b) FPN-CA, (c) FPN-SRR-CA.
Middle: the activation values (solid lines for bottom-up pathway via lateral connections and dotted lines for top-down pathway)
of competitive attention on (b) and (c). Bottom: the heatmaps of SRR attention.
[3] S. Bell, C. L. Zitnick, K. Bala, and R. Girshick. Inside-
outside net: Detecting objects in context with skip pooling and
recurrent neural networks. In IEEE Conference on Computer
Vision and Pattern Recognition, pages 2874–2883, 2016.
[4] J.-R. Chang and Y.-S. Chen. Pyramid stereo matching net-
work. In Proceedings of the IEEE Conference on Computer
Vision and Pattern Recognition, pages 5410–5418, 2018.
[5] J. Chen, H. Zhang, X. He, L. Nie, W. Liu, and T.-S. Chua.
Attentive collaborative ﬁltering: Multimedia recommendation
with item-and component-level attention. In Proceedings of
the 40th International ACM SIGIR conference on Research
and Development in Information Retrieval, pages 335–344.
ACM, 2017.
[6] L. Chen, H. Zhang, J. Xiao, L. Nie, J. Shao, W. Liu, and T.-S.
Chua. Sca-cnn: Spatial and channel-wise attention in convo-
lutional networks for image captioning. In 2017 IEEE Con-
ference on Computer Vision and Pattern Recognition (CVPR),
pages 6298–6306. IEEE, 2017.
[7] E. Choi, M. T. Bahadori, L. Song, W. F. Stewart, and J. Sun.
Gram: graph-based attention model for healthcare represen-
tation learning. In Proceedings of the 23rd ACM SIGKDD
International Conference on Knowledge Discovery and Data
Mining, pages 787–795. ACM, 2017.
[8] Y. Du, C. Yuan, B. Li, L. Zhao, Y. Li, and W. Hu. Interaction-
aware spatio-temporal pyramid attention networks for action
classiﬁcation. arXiv preprint arXiv:1808.01106, 2018.
[9] J. Fu, J. Liu, H. Tian, Z. Fang, and H. Lu.
Dual at-
tention network for scene segmentation.
arXiv preprint
arXiv:1809.02983, 2018.
[10] J. Fu, H. Zheng, and T. Mei. Look closer to see better: Recur-
rent attention convolutional neural network for ﬁne-grained
image recognition. In CVPR, volume 2, page 3, 2017.
[11] R. Girshick. Fast r-cnn. In Proceedings of the IEEE inter-
national conference on computer vision, pages 1440–1448,
2015.
[12] I. Gogul and V. S. Kumar. Flower species recognition system
using convolution neural networks and transfer learning. In
International Conference on Signal Processing, pages 1–6,
2017.
[13] K. He, X. Zhang, S. Ren, and J. Sun. Deep residual learning
for image recognition. In Proceedings of the IEEE conference
on computer vision and pattern recognition, pages 770–778,
2016.
[14] K. He, X. Zhang, S. Ren, and J. Sun. Identity mappings in
deep residual networks. In European conference on computer
vision, pages 630–645. Springer, 2016.
[15] J. Hu, Z. Chen, M. Yang, R. Zhang, and Y. Cui. A multiscale
fusion convolutional neural network for plant leaf recognition.
IEEE Signal Processing Letters, 25(6):853–857, 2018.
[16] J. Hu, L. Shen, and G. Sun. Squeeze-and-excitation networks.
arXiv preprint arXiv:1709.01507, 7, 2017.
8


## Page 9


[17] G. Huang, Z. Liu, L. Van Der Maaten, and K. Q. Weinberger.
Densely connected convolutional networks. In CVPR, vol-
ume 1, page 3, 2017.
[18] S. Ioffe and C. Szegedy. Batch normalization: Accelerating
deep network training by reducing internal covariate shift.
arXiv preprint arXiv:1502.03167, 2015.
[19] T. Kong, F. Sun, A. Yao, H. Liu, M. Lu, and Y. Chen. Ron:
Reverse connection with objectness prior networks for ob-
ject detection. In IEEE Conference on Computer Vision and
Pattern Recognition, volume 1, page 2, 2017.
[20] T. Kong, A. Yao, Y. Chen, and F. Sun. Hypernet: Towards
accurate region proposal generation and joint object detec-
tion. In IEEE Conference on Computer Vision and Pattern
Recognition, pages 845–853, 2016.
[21] W. Li, X. Zhu, and S. Gong. Harmonious attention network
for person re-identiﬁcation. In CVPR, volume 1, page 2, 2018.
[22] T.-Y. Lin, P. Doll´ar, R. B. Girshick, K. He, B. Hariharan, and
S. J. Belongie. Feature pyramid networks for object detection.
In CVPR, volume 1, page 4, 2017.
[23] D. Linsley, D. Scheibler, S. Eberhardt, and T. Serre. Global-
and-local attention networks for visual recognition. arXiv
preprint arXiv:1805.08819, 2018.
[24] W. Liu, D. Anguelov, D. Erhan, C. Szegedy, S. Reed, C.-
Y. Fu, and A. C. Berg. Ssd: Single shot multibox detector.
In European conference on computer vision, pages 21–37.
Springer, 2016.
[25] W. Liu, A. Rabinovich, and A. C. Berg. Parsenet: Looking
wider to see better. arXiv preprint arXiv:1506.04579, 2015.
[26] A. Newell, K. Yang, and J. Deng. Stacked hourglass net-
works for human pose estimation. In European Conference
on Computer Vision, pages 483–499. Springer, 2016.
[27] T. V. Nguyen, Q. Zhao, and S. Yan. Attentive systems: A
survey. International Journal of Computer Vision, 126(1):86–
110, 2018.
[28] J. Redmon, S. Divvala, R. Girshick, and A. Farhadi. You only
look once: Uniﬁed, real-time object detection. In Proceed-
ings of the IEEE conference on computer vision and pattern
recognition, pages 779–788, 2016.
[29] O. Ronneberger, P. Fischer, and T. Brox. U-net: Convolutional
networks for biomedical image segmentation. In Interna-
tional Conference on Medical image computing and computer-
assisted intervention, pages 234–241. Springer, 2015.
[30] K. Simonyan and A. Zisserman. Very deep convolutional
networks for large-scale image recognition. arXiv preprint
arXiv:1409.1556, 2014.
[31] C. Szegedy, W. Liu, Y. Jia, P. Sermanet, S. Reed, D. Anguelov,
D. Erhan, V. Vanhoucke, and A. Rabinovich. Going deeper
with convolutions. In Proceedings of the IEEE conference on
computer vision and pattern recognition, pages 1–9, 2015.
[32] B. P. T´oth, M. J. T´oth, D. Papp, and G. Sz¨ucs. Deep learning
and svm classiﬁcation for plant recognition in content-based
large scale image retrieval. In CLEF (Working Notes), pages
569–578, 2016.
[33] F. Wang, M. Jiang, C. Qian, S. Yang, C. Li, H. Zhang,
X. Wang, and X. Tang. Residual attention network for image
classiﬁcation. arXiv preprint arXiv:1704.06904, 2017.
[34] X. Wang, R. Girshick, A. Gupta, and K. He. Non-local neural
networks. arXiv preprint arXiv:1711.07971, 10, 2017.
[35] S. Woo, J. Park, J.-Y. Lee, and I. S. Kweon. Cbam: Convolu-
tional block attention module. In Proc. of European Conf. on
Computer Vision (ECCV), 2018.
[36] X. Xia, C. Xu, and B. Nan. Inception-v3 for ﬂower classi-
ﬁcation. In International Conference on Image, Vision and
Computing, pages 783–787, 2017.
[37] C. C. Yang and P. Veltri. Intelligent healthcare informatics in
big data era. Artiﬁcial intelligence in medicine, 65(2):75–77,
2015.
[38] H. Yang, D. Huang, Y. Wang, and A. K. Jain. Learning
face age progression: A pyramid architecture of gans. arXiv
preprint arXiv:1711.10352, 2017.
[39] J. Yang, Y. Hong, and S. Ma. Impact of the new health care
reform on hospital expenditure in china: A case study from a
pilot city. China Economic Review, 39:1–14, 2016.
[40] W. Yang, S. Li, W. Ouyang, H. Li, and X. Wang. Learning
feature pyramids for human pose estimation. In The IEEE
International Conference on Computer Vision (ICCV), vol-
ume 2, 2017.
[41] H. Zhang, M. Cisse, Y. N. Dauphin, and D. Lopez-Paz.
mixup: Beyond empirical risk minimization. arXiv preprint
arXiv:1710.09412, 2017.
[42] J. Zhang, X. Wu, J. Zhu, and S. C. Hoi. Feature agglomera-
tion networks for single stage face detection. arXiv preprint
arXiv:1712.00721, 2017.
[43] H. Zheng, J. Fu, T. Mei, and J. Luo. Learning multi-attention
convolutional neural network for ﬁne-grained image recogni-
tion. In Int. Conf. on Computer Vision, volume 6, 2017.
9


## Page 10


Appendices
A. Details of Chinese Herbs Datasets
A.1. Distributions of Examples in CNH-98 Dataset
Main Categories
Herbs Examples
Fruits & Seeds
Star Anise, Siraitia Grosvenorii,
Ginkgo, Chinese Wolfberry,
SElfheal, Fructus Arctii, etc.
Rhizome
Liquorice, Thorowax Root,
Rhizoma Alismatis,
Unibract Fritillary Bulb, etc.
Flowers
Saffron, Flos Daturae,
Cloves, Magnolia, Coltsfoot,
Flos Jasmine, Lily, etc.
Bark
Cinnamon, Cortex Moutan,
Eucommia Ulmoides, etc.
Thallophyte
Glossy Ganoderma, Tremella ,
Cordyceps Sinensis, etc.
Whole Herbs
Abrus cantoniensis,
Anoectochilus roxburghii, etc.
Leaves
Lophatherum Gracile, etc.
Resin
Frankincense, Myrrh, etc.
Table 2: Main categories of CNH dataset and their corre-
sponding examples.
Chinese Herbs are usually acquired from natural plants
and the parts of fungus and algae, and our Chinese-Herbs
Dataset (CNH-98) is a collection of 9184 images of 98
classes, which can be divided into 8 categories including
Fruits & Seeds, Rhizome, Flowers, Bark, Thallphyte, Whole
Herbs, Leaves, Resin, whose examples are shown in Table.
2 correspondingly.
Fig. 6 (left) has shown the distibution of number of
Chinese herbs classes in the 8 categories, where a majority
of classes are Fruits & Seeds and Rhizome, including 42
and 32 classes respectively. It can be seen that the CNH-98
dataset is relatively unbalanced. Moreover, as shown in Fig.
6 (right) , there is an unbalance of images quantities between
98 classes, the largest number of which is 247 images of
Amomum Tsaoko and the least is 14 images of Chestnut
Shell in Fruits & Seeds.
A.2. Exhibition of Main Categories
In this section, we exhibit the examples of primary cate-
gories in CNH-98 and their corresponding cropping exam-
ples in TCNH-98, as shown in Fig. 7. From the exhibition in
Fig. 7, we can see that although examples in TCNH-98 are
just local parts, each example in TCNH-98 almost contains
one herb with integrated shape at least, thanks to repeata-
bility of examples in CNH-98. Furthermore, the shapes of
Chinese herbs in various categories are extremely distin-
guishing, while the appearances of various classes in the
same categories are similar, which is just the motivation
of our proposed methods that the herbs with distinguishing
shape can be classiﬁed by features from earlier layers of
network, while the herbs with similar shape but different de-
tails need to be recognized by more semantic features from
deeper levels.
B. Evaluate with Other Upsampling Strategies
In order to validate the robustness of our models for dif-
ferent upsampling strategies, which mentioned in Section
4.3, we evaluate our methods with other upsampling meth-
ods including nearest neighbor and deconvolution and the
results are shown in Table. 3. By analyzing the results, we
can conclude that the accuracy rates of FPN ﬂuctuate more
greatly than our models and the maximum discrepancy is
by 1% while only 0.1 0.5% for our models. Even only us-
ing spatial attention SRR modules, our models can perform
more stable, which reﬂects our SRR modules contribute to
adapt for various upsamping strategies and perform more
robustly.
C. Further Analysis of Intermediate Results in
FPN-CA/SRR-CA
In this section, we extract the intermediate features from
our models FPN-CA/SRR-CA-18 with ResNet-18 as back-
bone networks. We deﬁne layers producing output maps of
same size as one pyramid level and the features extracted
from the last layer of various levels are shown in Fig. 8-10
for three examples. Additionally, we statistics activation val-
ues of competitve attention from two pathway in the process
of merging features and their spatial attention heatmaps.
By observing intuitively, we can obviously see that the
informathons of some features on many channels are sup-
pressed, either re-scaling with a small weight or retaining
more local features, and with this adjustment models can
get better performance, which does conﬁrm our inference
in the section 4.2 that the fusion method of original FPN
will lead to redundancies in feature maps. That is also one
of the motivations for us to propose attention mechanism.
Moreover, the attentional regions can be apparently seen
such as serrated petals shape of Flos Chrysanthemum in Fig.
8 and we can also see some fuzzy features are recalibrated
spatially and presented more clearly.
The aforementioned changes always occur in the low-
level of networks for both FPN-CA and FPN-SRR-CA and
features from high-level have not been adjusted too much,
shown in level 3 of Fig. 8 - 10, which can be veriﬁed by the
activation values statistics in Fig. 11. The activation values
of level 4 to 3 are always kept at about 0.5 and ﬂuctuate
sightly, for the reason that the features of spatial and seman-
10


## Page 11


Figure 6: Distribution of Chinese Herbs Categories (left) and amount of images for each classes in CNH-98 (right).
Model
Backbone Depth
Nearest
Deconvolution(# params)
Bilinear*
FPN-18
18
91.0
90.9(16.5M)
91.9
FPN-34
34
91.5
-
92.3
FPN-SRR-CA-18 (ours)
18
93.4
93.0(16.9M)
93.5
FPN-SRR-CA-34 (ours)
34
93.6
-
93.8
FPN-SRR-18 (ours)
18
92.3
92.3(16.5M)
92.5
FPN-SRR-34 (ours)
34
92.7
-
92.7
Table 3: Accuracy rates(%). Compare our models(*) with FPN using different upsampling strategies.
tics ﬂows before merging are extracted from the deep layers,
which are adjusted enough. However, on the low-level, fea-
tures from sematics ﬂows represent more vigorously and
the others from spatial ﬂow represent more sparsely, which
reﬂects that there is high information density on the semantic
ﬂows, which is more beniﬁcal to classifying. Furthermore,
a majority of features from spatial ﬂows with weak ability
of classiﬁcation are redundant and suppressed, and only a
small part of features are selected to make the supplement
for semantic ﬂows.
Compared with activation values of competitive attention
of FPN-CA, the features on various channels of FPN-SRR-
CA are less suppressed. We infer that SRR modules con-
tribute to restoring the spatial informations for misaligned
features, which results in higher information density of se-
mantic ﬂow, hence its representation are more vigorous (acti-
vation values of CA are almost non-zero), and this situation
reﬂects the SRR-CA module will be more cautious when
reducing redundancies of feature maps.
As shown in heatmaps of SRR attention modules, we
can see that the attention outputs of different regions are
obviously distinguishing and the absolute values of target
activation are usually bigger. Howerver, for the examples
of Flos Chrysanthemum in Fig. 8 of appendix and Unibract
Fritillary Bulb in Fig. 5 of main text, we can see the SRR
attention focus more on the background on level 1 and we
infer that the activation values of SRR attention are closely
related to the original images, especially for low-level of net-
works. The low-level features can highly restore the original
images and are more sensitive to colors. Therefore, due to
the dark colors of background, the absolute values of back-
gound activation are bigger than target. Despite all this, SRR
attention has played a role in distinguishing from different
regions and recalibrated the misaligned features.
11


## Page 12


CNH-98
CNH-98
TCNH-98
TCNH-98
Fruits & Seeds
Fruits & Seeds
Fructus Amomi
Croton
Semen Dolichos
Cocklebur Fruit
Fruits & Seeds
Fructus Amomi
Croton
Semen Dolichos
Cocklebur Fruit
Rhizome
Rhizome
Liquorice
Radix Angelicae Dahuricae
Rhizoma Imperatae
Thorowax Root
Rhizome
Liquorice
Radix Angelicae Dahuricae
Rhizoma Imperatae
Thorowax Root
Flowers
Flowers
Flos Chrysanthemum
Flos Jasmine
Magnolia
Coltsfoot
Flowers
Flos Chrysanthemum
Flos Jasmine
Magnolia
Coltsfoot
Bark
Bark
Cinnamon
Eucommia ulmoides
Phellodendron
Cortex Moutan
Bark
Cinnamon
Eucommia ulmoides
Phellodendron
Cortex Moutan
Thallophyte
Thallophyte
Glossy Ganoderma
Tremella
Poris Cocos
Cordyceps Sinensis
Thallophyte
Glossy Ganoderma
Tremella
Poris Cocos
Cordyceps Sinensis
Figure 7: Examples of Main Categories in CNH-98 and their Corresponding Examples in TCNH-98. From left to right, the
left examples in CNH-98 corresponds to the right in TCNH-98 from top to bottom.
12


## Page 13


FPN-CA
FPN-SRR-CA
FPN-CA
FPN-SRR-CA
FPN-CA
FPN-SRR-CA
FPN-CA
FPN-SRR-CA
CA -
CA
SRR-CA -
SRR-CA
CA -
CA
SRR-CA -
SRR-CA
CA -
CA
SRR-CA -
SRR-CA
Level 1
Flos Chrysanthemum
Level 2
Level 3
Level 4
(Without CA or SRR-CA)
Sptial flows
from bottom to up
Semantic flows
from top to down
Heatmaps of SRR Attention
(from level 4 to 3)
Sptial flows
from bottom to up
Semantic flows
from top to down
Heatmaps of SRR Attention
(from level 2 to 1)
Sptial flows
from bottom to up
Semantic flows
from top to down
Heatmaps of SRR Attention
(from level 3 to 2)
Figure 8: Flos Chrysanthemum: intermediate features on various channels from 4 levels of models FPN-CA/SRR-CA-18,
and their heatmaps of SRR Attention. Features on level 4 are initial on the top-down pathway, thus they are not fusion features.
For each block (excepted for level 4), the top (-) are not re-scaled by attention and the bottom refers features reweighted on
the corresponding channel.
13


## Page 14


FPN-CA
FPN-SRR-CA
FPN-CA
FPN-SRR-CA
FPN-CA
FPN-SRR-CA
FPN-CA
FPN-SRR-CA
CA -
CA
SRR-CA -
SRR-CA
CA -
CA
SRR-CA -
SRR-CA
CA -
CA
SRR-CA -
SRR-CA
Level 1
Level 2
Level 3
Level 4
(Without CA or SRR-CA)
Sptial flows
from bottom to up
Semantic flows
from top to down
Heatmaps of SRR Attention
(from level 2 to 1)
Sptial flows
from bottom to up
Semantic flows
from top to down
Heatmaps of SRR Attention
(from level 3 to 2)
Sptial flows
from bottom to up
Semantic flows
from top to down
Heatmaps of SRR Attention
(from level 4 to 3)
Szechuan Lovage Rhizome
Figure 9: Szechuan Lovage Rhizome: intermediate features on various channels from 4 levels and their heatmaps of SRR
Attention. For each block (excepted for level 4), the top (-) are not re-scaled by attention and the bottom refers features
reweighted on the corresponding channel.
14


## Page 15


FPN-CA
FPN-SRR-CA
FPN-CA
FPN-SRR-CA
FPN-CA
FPN-SRR-CA
FPN-CA
FPN-SRR-CA
Level 1
Level 2
Level 3
Level 4
(Without CA or SRR-CA)
Sptial flows
from bottom to up
Semantic flows
from top to down
Heatmaps of SRR Attention
(from level 2 to 1)
Sptial flows
from bottom to up
Semantic flows
from top to down
Heatmaps of SRR Attention
(from level 3 to 2)
Sptial flows
from bottom to up
Semantic flows
from top to down
Heatmaps of SRR Attention
(from level 4 to 3)
CA -
CA
SRR-CA -
SRR-CA
CA -
CA
SRR-CA -
SRR-CA
CA -
CA
SRR-CA -
SRR-CA
SElfheal
Figure 10: SElfheal: intermediate features on various channels from 4 levels and their heatmaps of SRR Attention. For
each block (excepted for level 4), the top (-) are not re-scaled by attention and the bottom refers features reweighted on the
corresponding channel.
15


## Page 16


Flos Chrysanthemum
Szechuan Lovage Rhizome
SElfheal
CA
CA
CA
SRR-CA
SRR-CA
SRR-CA
Level 4 to 3
Level 3 to 2
Level 2 to 1
Activation Values of Competitive Attention
Lateral
Top-down
Lateral
Top-down
Lateral
Top-down
Lateral
Top-down
Lateral
Top-down
Lateral
Top-down
Figure 11: Outputs of Competitive Attention on models FPN-CA/SRR-CA. (solid lines for bottom-up pathway via lateral
connections and dotted lines for top-down pathway)
16

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
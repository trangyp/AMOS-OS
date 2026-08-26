---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1907.09160v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1907.09160v2_Extended_Local_Binary_Patterns_for_Efficient_and_Robust_Spontaneous_Facial_Micro

> Source: 1907.09160v2_Extended_Local_Binary_Patterns_for_Efficient_and_Robust_Spontaneous_Facial_Micro.pdf

> Pages: 13

---


## Page 1


1
Extended Local Binary Patterns for Efﬁcient and
Robust Spontaneous Facial Micro-Expression
Recognition
Chengyu Guo, Jingyun Liang, Geng Zhan, Zhong Liu, Matti Pietik¨ainen, and Li Liu
Abstract—Facial Micro-Expressions (MEs) are spontaneous,
involuntary facial movements when a person experiences an
emotion but deliberately or unconsciously attempts to conceal
his or her genuine emotions. Recently, ME recognition has
attracted increasing attention due to its potential applications
such as clinical diagnosis, business negotiation, interrogations,
and security. However, it is expensive to build large scale ME
datasets, mainly due to the difﬁculty of inducing spontaneous
MEs. This limits the application of deep learning techniques
which require lots of training data.
In this paper, we propose a simple, efﬁcient yet robust
descriptor called Extended Local Binary Patterns on Three
Orthogonal Planes (ELBPTOP) for ME recognition. ELBPTOP
consists of three complementary binary descriptors: LBPTOP
and two novel ones Radial Difference LBPTOP (RDLBPTOP)
and Angular Difference LBPTOP (ADLBPTOP), which explore
the local second order information along the radial and angular
directions contained in ME video sequences. ELBPTOP is a novel
ME descriptor inspired by unique and subtle facial movements.
It is computationally efﬁcient and only marginally increases
the cost of computing LBPTOP, yet is extremely effective for
ME recognition. In addition, by ﬁrstly introducing Whitened
Principal Component Analysis (WPCA) to ME recognition, we
can further obtain more compact and discriminative feature
representations, then achieve signiﬁcantly computational savings.
Extensive experimental evaluation on three popular sponta-
neous ME datasets SMIC, CASME II and SAMM show that
our proposed ELBPTOP approach signiﬁcantly outperforms the
previous state-of-the-art on all three single evaluated datasets
and achieves promising results on cross-database recognition.
Our code will be made available.
Index Terms—Micro-expression recognition, local binary pat-
tern, feature extraction.
I. INTRODUCTION
Facial Micro-Expressions (MEs) are spontaneous, involun-
tary facial movements when a person experiences an emotion
but deliberately or unconsciously attempts to conceal his
or her genuine emotions [1]–[3]. MEs are more likely to
occur in high-risk environments because there are more risks
to show true emotions [4]. Recently, automatic facial ME
analysis has attracted increasing attention of affective com-
puting researchers and psychologists because of its potential
C. Guo (chloeguo@yeah.net), J. liang (michaelliang12@163.com), Z. Liu
(liuzhong@nudt.edu.cn) and L. Liu (li.liu@oulu.ﬁ) was with the College of
Systems Engineering, National University of Defense Technology, Changsha
410073, China.
L. Liu and M. Pietik¨ainen (mkp@ee.oulu.ﬁ) was with the Center for
Machine Vision and Signal analysis, University of Oulu, Finland.
G. Zhan (geng.zhan@sydney.edu.au) was with School of Electrical and
Information Engineering, The University of Sydney, NEW 2006, Australia.
applications such as clinical diagnosis, business negotiation,
interrogations, and security [5], [6]. The study of facial MEs
is a well established ﬁeld in psychology, however, it is a
relatively new area from the computer vision perspective with
many unsolved and challenging problems [7], [8]. There are
three main challenges in automatic ME analysis.
(1) MEs have a very short duration, local and subtle
facial movements. Compared to ordinary facial expressions,
the duration of a ME is usually very short, typically being
no more than 500 ms [9]. Besides short duration, MEs also
have other unique characteristics such as local and subtle facial
movements [10]. Because of these unique characteristics, it is
very difﬁcult for human beings to recognize MEs.
(2) Lack of large scale spontaneous ME datasets. Datasets
have played a key role in visual recognition problems, espe-
cially in the era of deep learning which requires large scale
datasets for training [11]. ME analysis is not an exception.
However, another challenging issue faced by automatic facial
ME analysis is the lack of benchmark datasets (especially
large scale ME datasets) due to the difﬁculties in inducing
spontaneous MEs
and labeling them [1], [7]. To the best
of our knowledge [12] , there are eight ME datasets: USF-
HD [13], Polikovsky’s database [14], YorkDDT [15], SMIC
[1], CASME [16], CASME II [2], CAS(ME)2 [17], and
SAMM [3]. The ﬁrst two are posed and not publicly-available.
Posed MEs are different from naturally occurring spontaneous
MEs signiﬁcantly. Thus recent works focus on spontaneous
ME datasets.
All of the datasets are small. Besides, the
emotion categories of the collected samples in these datasets
are unevenly distributed, because some emotions are easier to
elicit hence they have more samples.
(3) Lack of efﬁcient and discriminative feature represen-
tations. Above challenges make ME analysis much harder and
more demanding than ordinary facial tasks. Therefore, the ex-
traction of efﬁcient and discriminative feature representations
becomes especially important for automatic ME analysis.
In automatic ME analysis, there are mainly two tasks: ME
spotting and ME recognition. The former refers to the problem
of automatically and accurately locating the temporal interval
of a micro-movement in a video sequence, where extended
versions of SMIC [1], CAS(ME)2 [17], and SAMM [3] are
widely used; while the latter is to classify the ME in the
video into one of the predeﬁned emotion categories (such
as Happiness, Sadness, Surprise, Disgust, etc), where SMIC
[1], CASME II [2], and SAMM [3] are widely adopted. ME
recognition is the focus of this paper.
arXiv:1907.09160v2  [cs.CV]  17 Sep 2019


## Page 2


2
Like ordinary facial expression recognition, ME recognition
consists of three steps: preprocessing, feature representation
and classiﬁcation [7]. As we discussed previously, the de-
velopment of powerful feature representations plays a very
important role in ME recognition, and thus has been one main
focus of research [18]. Representative feature representation
approaches for ME recognition are mainly based on Local
Binary Patterns (LBP) [18], [19], Local Phase Quantization
(LPQ)
[20], Histogram of Oriented Gradients (HOG)
[21]
and Optical Flow (OF) [22].
Despite these efforts, there is still signiﬁcant room for
improvement towards achieving good performance. The small
scale of existing ME datasets and the imbalanced distribution
of samples are the primary obstacles to applying existing
data hungry deep convolutional neural networks which have
brought signiﬁcant breakthroughs in various visual recognition
problems in computer vision due to their ability to learn pow-
erful feature representations directly from raw data. Therefore,
state-of-the-art methods for ME recognition are still dominated
by traditional handcrafted features like Local Binary Patterns
on Three Orthogonal Planes (LBPTOP)
[23], 3D Gradient
Oriented Histogram (HOG 3D) [14] and Histograms of Ori-
ented Optical Flow (HOOF) [24].
Due to its prominent advantages such as theoretical simplic-
ity, computational efﬁciency, and robustness to monotonic grey
scale changes, the texture descriptor LBP [25] has emerged as
one of the most prominent features for face recognition [26].
Its 3D extension LBPTOP [23] is widely used for facial
expression and ME recognition [27]. Many variants of LBP
have been proposed to improve robustness, and discriminative
power, as summarized in recent surveys [28], [29]. However,
most LBP variants [30], [31] have not been explored for
ME recognition. In other words, in contrast to LBP-based
face recognition, LBPTOP type ME recognition is surprisingly
underexplored. Moreover, current state-of-the-art ME features
like LBPTOP and its variants LBPSIP [32], LBPMOP [33],
STLBP-IP [34], and STRBP [35] suffer from some drawbacks,
such as limited representation power of using only one type of
binary feature, limited robustness, and increased computational
complexity.
In this paper, in order to build more discriminative features
that can inherit the advantages of LBP type features without
suffering the shortcoming of using ﬁlters as complemental
features [25] (i.e., the expensive computation cost), we pro-
pose a novel binary feature descriptor named Extended Local
Binary Patterns on Three Orthogonal Planes (ELBPTOP) for
ME recognition. ELBPTOP is a descriptor that, we argue,
nicely balances the three concerns: high distinctiveness, good
robustness and low computational cost. In addition, LBPTOP
can be considered as a special case of the proposed ELBPTOP
descriptor. Our contributions of this paper are summarized as
follows.
• Inspired by the unique texture information of human faces
and the subtle intensity variations of local subtle facial
movements, the novel ELBPTOP encodes not only the
ﬁrst order information, i.e. the pixel difference informa-
tion between a central pixel and its neighbours (called
Center Pixel Difference Vector, CPDV), but also encodes
the second order discriminative information in two di-
rections: the radial direction (Radial Pixel Difference
Vector, RPDV) and the angular direction (Angular Pixel
Difference Vector, APDV). They are named ADLBPTOP
and RDLBPTOP respectively. The proposed ELBPTOP is
more effective to capture local, subtle intensity changes
and thus delivers stronger discriminative power.
• To achieve our goal of being computationally efﬁcient
while preserving distinctiveness, we then apply Whitened
Principal Component Analysis (WPCA) to get a more
compact, robust, and discriminative global descriptor. We
are aware of the fact that WPCA has proven to be
effective in face recognition. However, we argue that
we are the ﬁrst to apply WPCA to the problem of
ME recognition, which has its own unique challenges
compared to the extensively studied face recognition
problem.
• We provide extensive experimental evaluation on three
popular spontaneous ME datasets CASME II, SMIC, and
SAMM to test the effectiveness of the proposed approach,
and ﬁnd that our proposed ELBPTOP approach signiﬁ-
cantly outperforms previous state-of-the-art on all three
evaluated datasets. Our proposed ELBPTOP achieves
73.94% on CASMEII, which is 6.6% higher than state-
of-the-art on this dataset. More impressively, ELBPTOP
increases recognition accuracy from 44.7% to 63.44% on
the SAMM dataset.
Although our method is simple and handcrafted, the very
strong quality results obtained on three popular ME datasets
in addition with the low computational complexity prove the
efﬁciency of our approach for ME recognition.
The remainder of the paper is organized as follows. Sec-
tion II reviews related work in micro-expression recognition
and gives a brief outline of LBP and LBPTOP. The main model
and more details are represented in Section III, including
the proposed ADLBPTOP and the RDLBPTOP descriptors
and our ME recognition scheme. Experimental results are
presented in Section IV, leading to conclusions in Section V.
II. RELATED WORKS
Feature representation approaches of ME recognition can
be divided into two distinct categories: geometric-based and
appearance-based [36] methods. Speciﬁcally, geometric-based
features describe the face geometry such as the shapes and
locations of facial landmarks, so they need precise landmark-
ing and alignment procedures. By contrast, appearance-based
features describe the intensity and textural information such
as wrinkles and shading changes, and they are more robust to
illumination changes and alignment error. Thus, appearance-
based feature representation methods, including LBPTOP [23],
HOG 3D [14], HOOF [24] and deep learning, have been more
popular in ME recognition [7].
LBPTOP variants: Since the pioneering work by Pﬁster et
al. [6], LBPTOP has emerged as the most popular approach for
spontaneous ME analysis, and quite a few variants have been
proposed. LBP Six Interception Points (LBPSIP) [32] is based
on three intersecting lines crossing over the center point. LBP


## Page 3


3
Mean Orthogonal Planes (LBPMOP) [33] ﬁrst computes an
average plane for three orthogonal planes, and then computes
the LBP on the three orthogonal average planes. By reducing
redundant information, LBPSIP and LBPMOP achieved better
performance. [37] explores two effective binary face descrip-
tors: Hot Wheel Patterns [37] and Dual-Cross Patterns [38] and
makes use of abundant labelled micro-expressions. Besides
computing the sign of pixel differences, Spatio-Temporal
Completed Local Quantized Patterns (STCLQP) [39] also
exploits the complementary components of magnitudes and
orientations. Decorrelated Local Spatiotemporal Directional
Features (DLSTD) [40] uses Robust Principal Component
Analysis (RPCA) [41] to extract subtle emotion information
and division of 16 Regions of Interest (ROIs) to utilize the
Action Unit (AU) information. Spatio-Temporal Local Radon
Binary Pattern (STRBP) [35] uses Radon Transform to obtain
robust shape features, while Spatiotemporal Local Binary
Pattern with Integral Projection (STLBP-IP) [34] turns to
integral projections to preserve shape attributes.
HOOF variants: Histograms of Oriented Optical Flow
(HOOF) [24] is one of the baseline methods that makes use
of optical ﬂow in ME recognition. Facial Dynamics Map
(FDM) [42] describes local facial dynamics by extracting
principal OF direction of each cuboid. Similarly, [43] designs
Main Directional Mean Optical Flow (MDMO) features that
utilize the AU information from partitioning facial area into 36
ROIs. Different from these methods, Consistent Optical Flow
Maps [44] estimates consistent OF to characterize facial move-
ments, which are calculated from 25 ROIs and the OF of each
ROI could be in multiple directions. Recently, Bi-Weighted
Oriented Optical Flow (BI-WOOF) [45] makes use of only
the apex frame and the onset frame. The majority of OF-
based methods need to partition the face area precisely to make
use of AU information. This improves the performance but
increases the complexity of preprocessing. [46] calculates the
LBPTOP and HOOF fusion features for automatic Necessary
Morphological Patches (NMPs) extraction which combines the
AU-based method and the feature selection method.
HOG 3D variants: HOG 3D [14] is ﬁrstly used to rec-
ognize posed MEs and then as a baseline on spontaneous
MEs. Its variants, the Histogram of Image Gradient Orientation
(HIGO) [47] ignores the magnitude weighting, hence can
suppress the inﬂuence of illumination. This makes HIGO
become one of the most accurate descriptors at present. How-
ever, it is worth noting that HOG is an edge-based gradient
descriptor. It is sensitive to noise when not being ﬁltered,
and the use of low pass ﬁlters could lead to the loss of
subtle motion change information in ME recognition. Besides,
the computation process is time-consuming and cumbersome,
resulting in slow speed.
Deep
learning
methods: [48] adopts a shallow net-
work with Convolutional Neural Networks (CNN) and Long
Short-Term Memory (LSTM). Other neural networks are ex-
plored in Dual Temporal Scale Convolutional Neural Network
(DTSCNN) [49], 3D Flow Convolutional Neural Network
(3DFCNN) [50], 3D Spatiotemporal Convolutional Neural
Networks (3DCNN) [51] and Micro-Expression Recognition
algorithm using Recurrent CNNs (MER-RCNN) [52]. These
61
61
71
80
79
84
78
82
77
61
61
71
80
79
84
78
82
77
0
0
0
1
1
1
1
1
0
0
0
1
1
1
1
1
Binary: 11110001
Decimal: 241
2
p
2
p
2
p
1,
0
( )
0,
0
x
s x
x


= 


1
0
2
p
i
i
i
b
−
=
0b
1
p
b −
1b
0b
1
p
b −
1b
Example:
LBP on
Three 
Orthogonal 
Planes
(a) LBP
(b) LBPTOP
XY
XT
YT
, ,1
r p
x
, ,0
r p
x
, ,
1
r p p
x
−
, ,
(
)
i
r p i
c
b
s x
x
=
−
Fig. 1:
(a) LBP pattern: The sample neighborhood is the
center pixel xc with p equally spaced pixels on a circle of
radius r. Then the binary code is calculated by comparing
the differences between the center pixel and its neighbors. An
example is in the ﬁgure. (b) The process of LBPTOP.
methods achieve some improvements in ME recognition, but
they are still signiﬁcantly below state-of-the-art handcrafted
features, mainly due to lack of large scale ME data.
Cross-database ME recognition (CDMER) is a new topic
in micro-expression analysis. CDMER considers the large
difference of feature distributions existing between the train-
ing and testing ME samples in a real scenario to exploit
more generalizing approach on different datasets collected by
different cameras or under different environments. Besides,
a combination of different datasets increased the number of
subjects and samples, which is beneﬁcial to the data-driven
methods and deep-learning methods. The fundamental works
of 1st Micro-Expression Grand Challenge (MEGC2018) [53]
, 2nd Micro-Expression Grand Challenge (MEGC2019) [54]
, and
[55] facilitate the development of CDMER. Macro
to Micro Transfer Learning [56] utilizes transfer learning to
implement CNN from big macro-expression datasets to small
ME datasets, ranking top in MEGC2018. Besides transfer
learning, [57] adopt two domain adaptation techniques includ-
ing adversarial training and expression magniﬁcation obtain
the best results on the full composite database in MEGC2019.
Other methods [58]–[63] also show promising performance in
cross-database challenges.
A. LBP and LBPTOP
LBP was ﬁrstly proposed in [19], and a completed version
was developed in [18]. Later on, it was introduced to face
recognition in [26] and its 3D extended version LBPTOP was
proposed in [23] with application to facial expression analysis.
LBP characterizes the special structure of p pixels, that are
evenly distributed in angle on a circle of radius r centered at
pixel xc. In speciﬁc, as shown in Figure 1(a), for a central pixel


## Page 4


4
xc and its p neighboring equally spaced pixels {xr,p,n}p−1
n=0 on
the circle of radius r, the LBP pattern is computed via:
LBPr,p(xc) =
p−1
X
n=0
s(xr,p,n −xc)2n, s(x) =
(
1,
x ≥0
0,
x < 0 ,
(1)
where s(·) is the sign function. The gray values of points
that do not fall exactly in the center of pixels are estimated
by interpolation. The decimal value of LBP pattern is given
by the binary sequence of the circular neighborhood, such as
241 = (11110001)2 in Figure 1(a). LBP is gray scale invariant
and is able to encode important local patterns like lines, edges,
and blobs because it measures the differences between the
center pixel and its neighbors.
Given an N*M texture image, a LBP pattern LBPr,p(xc)
can be the computed at each pixel c, such that a textured
image can be characterized by the distribution of LBP values,
representing the whole image by a LBP histogram vector.
By altering r and p, one can compute LBP features for any
quantization of the angular space and for any spatial resolution.
LBPTOP [23] is the 3D extension of LBP by extracting
LBP patterns separately from three orthogonal planes: the
spatial plane (XY) similar to the regular LBP, the vertical
spatiotemporal plane (YT) and the horizontal spatiotemporal
plane (XT), as illustrated in Figure 1(b).
Clearly, LBPTOP encodes temporal changes, and compo-
nential information. A video can be represented by concate-
nating LBP on TOP. Despite a little more complex than the
static LBP, LBPTOP can achieve real time processing speed
depending on the size of the local sampling neighborhood.
The dimensionality of LBPTOP is higher than LBP. Since
LBPTOP, which extracts features from TOP, becomes popular
when extending 2D spatial appearance descriptors to the
spatiotemporal domain.
III. PROPOSED APPROACH
In this section, we ﬁrst introduce the proposed novel binary
descriptor ELBPTOP and then present how to use it for ME
recognition.
A. ELBPTOP
LBPTOP has emerged as one of the dominant descriptors
for ME recognition. Despite this fact, it has several limitations.
• Currently, LBPTOP [23] usually only exploit the uniform
patterns for ME representation. This results in informa-
tion loss since the proportion of uniform patterns may be
too small to capture the variations.
• It encodes the difference between each pixel and its
neighboring pixels only. It is common to combine com-
plementary features like Gabor ﬁlters to improve dis-
criminative power. However, this brings a signiﬁcant
computational burden.
• A large sampling size is helpful since it encodes more lo-
cal information and provides better representation power.
However, increasing the number of sampling points of
LBPTOP increases its feature dimensionality signiﬁ-
cantly.
(1)LBP
(2)ADLBP
(3)RDLBP
ELBP
cx
3
6
2
7
3
2
5
3
4
2
9
2
1
8
4
3
1
0
2
3
-1
1
0
4
-1
2
1
-4
2
-1
4
-5
1
-2
-3
-4
-1
4
1
-4
7
(3)
(2)
(1)
1
1
1
0
1
1
1
0
1
1
0
1
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
1
119 171 176
(3)
(2)
(1)
(a)
(b)
binary code
r - δ
r
2π
p
1
,
, ,
0
(
)
(
)2
p
n
r p
c
r p n
c
n
LBP
x
s x
x
−
=
=
−

1
,
, ,
1
, ,
0
(
)
(
)2
p
n
r p
c
r p n
r p n
n
ADLBP
x
s x
x
−
+
=
=
−

1
, ,
, ,
, ,
0
(
)
(
)2
p
n
r p
c
r p n
r
p n
n
RDLBP
x
s x
x


−
−
=
=
−

, ,1
r p
x
, ,2
r p
x
, ,3
r p
x
, ,4
r p
x
, ,5
r p
x
, ,6
r p
x
, ,
r p n
x
, ,0
r p
x
Fig. 2: (a) A local circularly symmetric neighbor sampling of
ELBP. Two circles of p = 8 neighbor points are around the
central pixel xc. The radius of the inner circle is r −δ, and
the radius of the outer circle is r. (b) An illustration of the
process to calculate ELBP pattern.
The above analysis leads us to propose novel binary type
descriptors, which should not be competitive with LBPTOP,
but complement and extend a set of binary feature candidates.
We propose to explore the second order discriminative infor-
mation in two directions of a local patch: the radial differences
(RDLBPTOP) and the angular differences (ADLBPTOP), as
complement to the differences between a pixel and its neigh-
bors (LBPTOP). The proposed RDLBPTOP and ADLBPTOP
preserve the advantages of LBP, such as a computational
efﬁciency and gray scale invariance.
(1) Radial Difference Local Binary Pattern (RDLBP)
As illustrated in Section II, LBP is computed by thresholding
the neighboring pixel values on a ring against its center pixel
value. It only encodes the relationship between the neighboring
pixels on the same ring (i.e. a single scale) and the center one,
failing to capture the second order information of neighboring
pixels between different rings (different scales). For every
pixel in the image, we look at two rings of radii r and r −δ
centered on the pixel xc and p pixels distributed evenly on
each ring, as shown in Figure 2. To produce the RDLBP codes,
we ﬁrst compute the radial differences {xr,p,n −xr−δ,p,n}n
between pixels on the two rings and then threshold them
against 0. The formal deﬁnition of the RDLBP code is as
follows:
RDLBPr,p,δ(xc) =
p−1
X
n=0
s(xr,p,n −xr−δ,p,n)2n,
(2)


## Page 5


5
LBP
112
AD
25
29
RD
50
112
112
86
87
86
87
88
89
89
85
88 88
86
88
88
89
89 89
87
86
87
86
87
88
89
89
85
88 88
86
88
88
89
89 89
87
84
85
83
87
90
92
88 88
88
86
86
86
86
88
87
90
90
84
85
83
87
90
92
88 88
88
86
86
86
86
88
87
90
90
Fig. 3: The two given patterns in the left would be considered
equivalent by LBP. However, the patterns are, in some ways,
quite different from one to others. Fortunately, this underlying
change properties can be revealed via angular and radial
differences.
where r and r −δ denote the outer ring and the inner ring
respectively. As can be seen from Figure 3, the LBP values
of two different pixels can be same in some cases, but for
RDLBP, they are totally different. This is because RDLBP
encodes radial pixel difference information.
(2) Angular Difference Local Binary Pattern (ADLBP)
LBP also fails to encode the second order information between
pixels on the ring. Therefore, ADLBP is composed of neigh-
boring pixel comparisons in angular (like clockwise) direction
for all pixels except the center pixel.
Formally, it can be calculated as follows:
ADLBPr,p(xc) =
p−1
X
n=0
s(xr,p,n+1 −xr,p,n)2n.
(3)
Similarly, Figure 3 shows that ADLBP encodes angular dif-
ference information, which is different from the original LBP
descriptor . It is very compact and provides useful information.
We can see that both RDLBP and ADLBP are gray scale
invariant and computationally efﬁcient. They can also beneﬁt
from rotation invariant extension, uniform extension and 3D
extension of LBP.
(3) Extended LBP (ELBP) We use ELBP to represent the
combination of all three binary descriptors: LBP, RDLBP, and
ADLBP. The three operators LBP, RDLBP and ADLBP can
be combined in two ways, jointly or independently. Because
the joint way (3D joint histogram) leads to huge dimension,
we use the latter way.
For ME recognition, as shown in Figure 1(b), we extend
ELBP to ELBPTOP. Most LBPTOP based ME descriptors
use uniform LBP patterns and group the nonuniform patterns
into one bin. However, this leads to lots of information loss
because uniform LBPs may not be the majority of LBPs,
as illustrated in Figure 4. This is more obvious in the case
of ADLBP, where the nonuniform patterns are the dominant
patterns. Therefore, in this paper, we use all 2p patterns, rather
than uniform patterns only.
B. ELBPTOP for ME recognition
In this section, the ME representation is addressed using
our proposed ELBPTOP approach to explicitly handle the
encountered challenges.
To enhance the discrimination power, we propose to fuse
the information extracted by three binary descriptors LBPTOP,
RDLBPTOP and ADLBPTOP. The ME feature representation
algorithm is illustrated in Figure 6(a). For each binary descrip-
tor LBPTOP (or RDLBPTOP or ADLBPTOP), the ME video
sequences are represented as the concatenated spatiotemporal
histograms of the binary codes. In speciﬁc, a video sequence
is divided into m × q × l blocks, then for every single binary
descriptor, the dimension of the histogram is m × q × l × 2p.
For instance, if we divide the video sequence into 8 × 8 × 2
blocks, and we choose p = 8, the histogram dimension of a
single descriptor would be 8 × 8 × 2 × 2p = 32768.
An efﬁcient and effective feature representation scheme is
equally important for ME recognition as an efﬁcient and good
local descriptor. For each binary code (LBPTOP, RDLBPTOP
or ADLBPTOP), the dimension of the feature representation
for each ME video sequence is m × q × l × 2p, which is in
fact very high. This would cause a computational burden for
later classiﬁcation stage. Therefore, to improve efﬁciency and
preserve distinctiveness, Whitened Principal Component Anal-
ysis (WPCA) [64], [65] is ﬁrstly introduced for dimensionality
reduction before feature fusion.
The idea behind WPCA is that discriminative information
is equally distributed along all principle components. The
whitening transformation is applied to normalize the con-
tribution of each principal component. Speciﬁcally, given a
feature representation h, standard PCA is used to get the
projected feature hpca = Wpcah at ﬁrst, where Wpca is
the projection matrix of with k orthonormal columns. Then,
the sorted eigenvectors corresponding to the descending sorted
ﬁrst k principal components are transformed to normalized
eigenvectors hwpca whose variances equal to 1.
In summary, ﬁgure 6(a) illustrates the overview of the
proposed feature extraction framework. At ﬁrst, the video
sequences are spatially divided into multiple nonoverlapping
subblocks, from each of which three sub-region histograms are
extracted via the three proposed binary codes. Each subblock
histogram is normalized to sum one. Then, histograms of dif-
ferent subblocks are concatenated and projected by WPCA for
dimensionality reduction. Finally, three feature representation
vectors with low dimensionality from LBPTOP, RDLBPTOP
and ADLBPTOP, are concatenated as a single vector hF ,
which is used for ﬁnal ME feature representation.
C. The ME recognition pipeline
The ME recognition problem is illustrated in Figure 6(b).
The proposed overall pipeline for ME classiﬁcation is shown in
Figure 5. Following [47], raw ME video sequences are gener-
ally processed by the following steps: face alignment, motion
magniﬁcation, temporal interpolation, feature extraction and
classiﬁcation.
Our main contribution in this work is the feature representa-
tion step, which is presented in detail in the previous sections.


## Page 6


6
nonuniform
13.55%
nonuniform
57.24%
nonuniform
23.44%
nonuniform
79.35%
nonuniform
21.76%
nonuniform
26.24%
nonuniform
74.28%
nonuniform
34.71%
nonuniform
33.56%
Fig. 4: Proportions of the uniform1 LBPs for the ELBP descriptors (LBP, ADLBP, and RDLBP) on three planes (XY,XT,YT)
from the CASME II dataset. The ﬁrst 9 bins of each histogram are the uniform patterns, and others are the nonuniform patterns.
We could observe that the uniform patterns may not account for the major proportion of overall patterns. This is especially
obvious in the case of ADLBP.
 Happiness
 Happiness 
Training
Testing
√ 
 Surprise
 Disgust
Repression
 Others
Fig. 5: Illustration of the ME classiﬁcation problem. Samples
frames are from CASME II [2].
A very brief introduction of the other involved steps are given
below. Readers are requested to referred to [3], [6], [47] for
more information.
Face Alignment: For CASME II [2], SMIC [1] datasets,
we use the given cropped images so that face alignment is not
required. For SAMM [3] dataset, Active Shape Model [66]
is used to detect 77 facial landmarks and then all the facial
images are normalized using afﬁne transformation and cropped
into the same size according to the eye center points and the
outermost points.
Motion Magniﬁcation: Since local intensity changes and
facial movement changes in ME are subtle, effective ME
characteristics are difﬁcult to capture. To tackle these issues,
following [47], [67] we use Eulerian Video Magniﬁcation
(EVM) [68] to magnify the subtle motions in videos. The goal
is to consider the time series of intensity values at any spatial
location (pixel) and amplify variation in a given temporal
frequency band of interest. The ﬁltered spatial bands are then
ampliﬁed by a given factor α, added back to the original signal,
and collapsed to generate the output video.
Temporal Interpolation: To address the issue that ME
clips are short and have varied duration, we use the Temporal
Interpolation Model (TIM)
[69] and the code provided by
[6]. The model ﬁrst seeks a low-dimensional manifold where
visual features extracted from the frames of a video can be
projected onto a continuous deterministic curve embedded in a
path graph. Moreover, it can map arbitrary points on the curve
back into the image space, making it suitable for temporal
interpolation.
1For clear illustration, we transform the “full” pattern into “rotation invari-
ant (ri)” pattern [18]. Accordingly, the “uniform (u2)” pattern is transformed
into “rotation invariant uniform (riu2)” pattern. Meanwhile, the proportion of
the “u2” pattern in the ”full” pattern is equal to the proportion of the ”riu2”
pattern in the ”ri” pattern. The transformation has no effect on our conclusion.


## Page 7


7
Face
Alignment
Temporal 
Interpolation
Motion
Magnification
Classification
x
t
y
x
t
y
LBPTOP
ADLBPTOP
RDLBPTOP
Video 
Sequences
Local 
Descriptors
Subblock
Histograms
Concatenated 
Histograms (h)
Features 
Projected With 
WPCA (hwpca)
Fused Features 
(hF)
ME Feature
Representation
ME Feature
Representation
ME Feature Representation Stage
Fig. 6: Overview of the proposed ME recognition framework.
Classiﬁcation: For classiﬁcation, we use Linear Support
Vector Machine (LSVM) [70] as the classiﬁer. Leave-one-
subject-out cross-validation (LOSOCV) method is adopted to
determine the penalty parameter c in SVM. For each test
subject, LOSOCV is applied to the training samples, where
in each fold the samples belonging to one subject are served
as validation set and the rest of samples compose the new
training set to select the best c and the selected c is used for
testing.
IV. EXPERIMENTS
A. Datasets
Three
most
popular
spontaneous
datasets,
including
CASME II [2], SMIC [1] and SAMM [3], are used to evaluate
the performance of the proposed method. The dataset statistics
are summarized in Table I.
SMIC [1]: SMIC consists of 164 sample video clips of 16
subjects belonging to 3 different classes , e.g., Positive (51
samples), Negative (70 samples) and Surprise (43 samples).
The SMIC data has three versions: a high-speed camera (HS)
version at 100 fps, a normal visual camera (VIS) version at
25 fps and a near-infrared camera (NIR) version at 25 fps.
The HS camera was used to record all data, while VIS and
NIR cameras were only used for the recording of the last
eight subjects’ data. The emotion classes are only based on
participants’ self-reports. In this paper, we use the HS samples
for experiments, and the resolution of average face size is 160
× 130.
CASME II [2]: CASME II contains 247 ME video clips
from 26 subjects. All samples are recorded by a high speed
camera at 200 fps. The resolution of samples is 640 × 480
pixels and the cropped area has 340 × 280 pixels. These
samples are categorized into ﬁve ME classes: Happiness
(32 samples), Surprise (25 samples), Disgust (64 samples),
Repression (27 samples) and Others (99 samples). Different
from SMIC, CASME II has AU labels following Facial Action
Coding System (FACS). These classes are used in the whole
parameter evaluation and they are used for comparison in Table
VII. To remove the bias of human reporting, [71] reorganized
the classes based on AU instead of original estimated emotion
classes. Performance on the reorganized objective classes are
also reported in Table VIII.
SAMM [3]: SAMM database contains 159 ME video clips
from 29 subjects. All samples are recorded by a high speed
camera at 200 fps. The resolution of samples is 2040 ×
1088 pixels and the cropped facial area has about 400 × 400
pixels. These samples are categorized into seven AU based
objective classes. Classes I-VI are linked with Happiness (24
samples), Surprise (13 samples), Anger (20 samples), Disgust
(8 samples), Sadness (3 samples), and Fear (7 samples). Class
VII (84 samples) relates to contempt and other AUs that have
no emotional link in FACS [72]. We carry on experiment on
SAMM with classes I-V and the results are shown in Table
VIII.
B. Implementation details
We conduct two set of experiments: (1) Single database
experiment involving SMIC and CASME II with their original
estimated emotion classes, and CASME II and SAMM with
the reorganized objective classes I-V. (2) Cross-database exper-
iments involving SMIC, CASME II , and SAMM following
the Guidelines of the 1st MEGC [53] and the 2nd MEGC [54].


## Page 8


8
Feature
SMIC-HS [1]
CASME II [2]
SAMM [3]
No. of Samples
164
247
159
No. of Subjects
16
26
29
Resolution
640 × 480
640 × 480
2040 × 1088
Facial Area
160 × 130
340 × 280
400 × 400
FPS
100
200
200
FACS Coded
NO
Yes
Yes
Classes
3
5
7
TABLE I: A summary of the different features of the SMIC,
CASME II and SAMM datasets.
Most of the methods adopt leave-one-subject-out (LOSO)
strategy for evaluation. For each fold, all samples from one
subject are used as a testing set and the rest for training. A
few works [40], [46] use leave-one-sample/video-out (LOVO)
protocol, in which one sample is used as a testing set and the
rest for training. Some works use their own protocols, such
as random sampling of test partition [37], [51] , ﬁve-fold [52]
and others [49]. Leave one subject out (LOSO) strategy is
used for evaluation in all the experiments. Mean accuracy,
F1-score, Weighted F1-score, and Unweighted Average Recall
(UAR) are used to measure the performance. Mean accuracy
is obtained by averaging accuracies of subjects. F1-score is
deﬁned as F =
1
c
Pc
i=1
2pi×ri
pi+ri , where pi and ri are the
precision and recall of the ith ME class, respectively, and c
is the number of classes. Weighted F1-scores are weighted by
the number of samples in the corresponding classes before
averaging. UAR is the “balanced” accuracy (averaging the
accuracy of each class without consideration of the number
of samples per class).
Parameters: For block division parameters (m × q × l),
8 × 8 × 2 is for CASME II and SMIC, and 5 × 5 × 2 is for
SAMM. For EVM [67], we choose the second-order bandpass
ﬁlter with cutoff frequencies ω1 = 0.4, ω2 = 0.05 and spatial
frequency cutoff λc = 16. Magniﬁcation value α is set to 20
for CASME II and SAMM, while α = 8 is chosen for SMIC.
TIM [69] is used to interpolate all ME sequences into the
same length 10 according to [47]. Values of the number of
neighboring pixels p, outer ring radius r and inner ring radius
r −δ can be found in tables. The WPCA dimension is v −1,
where v is the number of video clips of each dataset, e.g., 163
for SMIC and 246 for CASME II.
C. Parameter evaluation
The effect of encoding scheme: Table II compares the
performance of two encoding schemes, full patterns (all 2P
patterns) and uniform patterns, on SMIC. Results on single
binary descriptor without WPCA are reported. From table II,
we can see those histogram representations generated by the
full patterns signiﬁcantly outperform the uniform patterns, on
all binary descriptors by a large margin (2.22% to 6.46% in
accuracy, and 0.03 to 0.04 in F1-score), clearly demonstrating
the insufﬁciency of the uniform patterns for representing ME
videos. As a result, we conduct rest experiments using the full
patterns encoding scheme.
The effect of WPCA: Table III illustrates the effect of
WPCA dimensionality reduction on SMIC. Clearly, the accu-
Method
full patterns
uniform patterns
Acc. (%) / F1-score
(r, p, δ)
Acc. (%) / F1-score
(r, p, δ)
LBPTOP
52.07 / 0.48
(3,8)
49.85 / 0.45
(3,8)
ADLBPTOP
53.11 / 0.51
(3,8)
49.89 / 0.47
(3,8)
RDLBPTOP
53.26 / 0.50
(3,8,2)
46.80 / 0.46
(3,8,2)
TABLE II: ME recognition accuracy (%) of single descriptors
on SMIC using two different encoding schemes: full patterns
and uniform patterns. p, r and r −δ indicates the number
of neighboring points, the outer ring and the inner ring
respectively. All experiments are conducted without WPCA
and EVM.
Method
original (h)
WPCA (hpca)
Acc. (%) / F1-score
(r, p, δ)
Dim.
Acc. (%) / F1-score
(r, p, δ)
Dim.
LBPTOP
51.09 / 0.47
(2,8)
98304
52.29 / 0.49
(2,8)
163
ADLBPTOP
55.11 / 0.53
(2,8)
98304
58.45 / 0.54
(2,8)
163
RDLBPTOP
52.61 / 0.49
(2,8,1)
98304
52.61 / 0.49
(2,8,1)
163
TABLE III: ME recognition accuracy (%) of different binary
descriptors on SMIC with or without WPCA. (m × q × l) is
set to 8 × 8 × 2. Experiments are conducted without EVM.
racy and F1-score of all descriptors is consistently improved
by WPCA. Besides, due to much lower feature dimensionality
(163 compared with 98304), WPCA could lead to great
computational saving. Therefore, further experiments are con-
ducted using WPCA.
Evaluation of single binary descriptor: To explore the
characteristics of different binary descriptors, we conduct
experiments under various (r, p, δ) settings. As shown in
Table IV, the radius r has great impacts on the performance
of the three descriptors. The best accuracy often exceeds
the second best by a large gap. Therefore, the choice of
the best radius r is of great importance. It’s the same for
F1-score. In some cases, the highest accuracy and F1-score
do not appear on the same parameters. In the following
experiments, we choose the parameter setting with the highest
accuracy. Similarly, δ is very important for the performance of
RDLBP. Comparing the best results of ADLBPTOP, LBPTOP
and RDLBPTOP, we can ﬁnd that the proposed ADLBPTOP
and RDLBPTOP outperform LBPTOP on both SMIC and
CASME II in accuracy, which shows the importance of radial
dataset
ADLBPTOPr,p
LBPTOPr,p
RDLBPTOPr,p,δ
Acc. / F1-score
(r, p)
Acc. / F1-score
(r, p)
Acc. / F1-score
(r, p, δ)
SMIC
62.27 / 0.58
(1,8)
52.19 / 0.53
(1,8)
52.55 / 0.53
(1,8,0)
58.45 / 0.54
(2,8)
52.29 / 0.49
(2,8)
52.61 / 0.49
(2,8,1)
53.11 / 0.51
(3,8)
52.07 / 0.48
(3,8)
50.67 / 0.46
(3,8,1)
53.11 / 0.51
(3,8)
52.07 / 0.48
(3,8)
53.26 / 0.50
(3,8,2)
47.95 / 0.49
(4,8)
54.50 / 0.53
(4,8)
55.97 / 0.50
(4,8,1)
47.95 / 0.49
(4,8)
54.50 / 0.53
(4,8)
52.89 / 0.48
(4,8,2)
47.95 / 0.49
(4,8)
54.50 / 0.53
(4,8)
55.45 / 0.50
(4,8,3)
CASME II
48.35 / 0.34
(1,8)
50.15 / 0.38
(1,8)
49.14 / 0.35
(1,8,0)
56.45 / 0.39
(2,8)
52.79 / 0.37
(2,8)
50.89 / 0.38
(2,8,1)
44.36 / 0.35
(3,8)
50.92 / 0.36
(3,8)
49.49 / 0.35
(3,8,1)
44.36 / 0.35
(3,8)
50.92 / 0.36
(3,8)
55.10 / 0.37
(3,8,2)
47.23 / 0.35
(4,8)
49.49 / 0.29
(4,8)
40.64 / 0.31
(4,8,1)
47.23 / 0.35
(4,8)
49.49 / 0.29
(4,8)
43.19 / 0.28
(4,8,2)
47.23 / 0.35
(4,8)
49.49 / 0.29
(4,8)
45.60 / 0.32
(4,8,3)
TABLE IV: ME recognition accuracy (%) of the single binary
descriptors on SMIC and CASME II under various parameter
settings. (m×q ×l) is set to 8×8×2. The WPCA dimension
k for SMIC is 163, and 246 for CASME II. Experiments are
conducted without EVM.


## Page 9


9
Method
SMIC
CASME II
Acc. (%) / F1-score
(r, p, δ)
Acc. (%) / F1-score
(r, p, δ)
ADLBPTOP
62.27 / 0.58
(1,8)
56.45 / 0.39
(3,8)
ADLBPTOP+EVM
63.73 / 0.61
(1,8)
69.12 / 0.64
(3,8)
54.61 / 0.56
(4,4)
70.20 / 0.69
(2,4)
LBPTOP
54.50 / 0.53
(4,8)
52.97 / 0.37
(2,8)
LBPTOP+EVM
60.83 / 0.60
(3,8)
67.08 / 0.58
(4,8)
65.16 / 0.58
(3,4)
71.55 / 0.65
(3,4)
RDLBPTOP
55.97 / 0.51
(4,8,1)
55.10 / 0.37
(3,8,2)
RDLBPTOP+EVM
61.04 / 0.58
(4,8,3)
67.62 / 0.66
(3,8,2)
62.57 / 0.56
(4,4,3)
69.24 / 0.64
(3,4,1)
TABLE V: ME recognition accuracy using different numbers
of neighbors p as well as with or without EVM. The parame-
ters of (m × q × l) and the WPCA dimensions k are the same
as Table IV.
Method
SMIC
CASME II
Acc. (%) / F1-score
(r, p, δ)
Acc. (%) / F1-score
(r, p, δ)
ADLBP
TOP
63.73 / 0.63
(1,8)
69.12 / 0.64
(3,8)
XYOT
55.91 / 0.57
(1,8)
64.12 / 0.60
(3,8)
XOT
55.92 / 0.58
(1,8)
61.47 / 0.58
(3,8)
YOT
60.22 / 0.58
(1,8)
62.87 / 0.57
(3,8)
XY
55.69 / 0.51
(1,8)
56.46 / 0.41
(3,8)
LBP
TOP
60.83 / 0.59
(3,8)
67.08 / 0.61
(4,8)
XYOT
60.47 / 0.60
(3,8)
65.04 / 0.60
(4,8)
XOT
57.24 / 0.58
(3,8)
61.38 / 0.56
(4,8)
YOT
55.47 / 0.57
(3,8)
67.65 / 0.59
(4,8)
XY
45.97 / 0.45
(3,8)
60.26 / 0.43
(4,8)
RDLBP
TOP
61.04 / 0.58
(4,8,3)
67.62 / 0.65
(3,8,2)
XYOT
57.84 / 0.59
(4,8,3)
68.85 / 0.66
(3,8,2)
XOT
56.06 / 0.56
(4,8,3)
62.91 / 0.60
(3,8,2)
YOT
58.76 / 0.55
(4,8,3)
66.56 / 0.63
(3,8,2)
XY
48.85 / 0.47
(4,8,3)
57.14 / 0.43
(3,8,2)
TABLE VI: ME recognition accuracy (%) of three binary de-
scriptors on different combinations of planes. The parameters
(m × q × l) and k are the same as Table IV. Experiments are
conducted with EVM.
and angular difference information. Especially, ADLBPTOP
performs much better than LBPTOP in accuracy and F1-score
(3.66% and 8.27% higher in accuracy, 0.01 and 0.05 higher
in F1-score on two datasets respectively).
Evaluation of EVM and parameter p: Evaluation of the
number of neighboring pixels p and the effect of EVM are
summarized in Table V. Note that all the results are reported
with their best radii. We can see that EVM can generally
increase the recognition accuracy and F1-score, sometimes
signiﬁcantly (such as for ADLBPTOP and LBPTOP). Table
V also indicates that for each single ELBPTOP descriptor, the
performance achieved by p = 4 is better than that by p = 8,
with ADLBPTOP on SMIC being an exception.
Evaluation of orthogonal planes: Table VI illustrates the
performance of three binary features (LBP, ADLBP, RDLBP)
on ﬁve combinations of planes. TOP, XYOT, XOT, YOT and
XY are abbreviations for XY+XT+YT, XT+YT, XT, YT and
original spatial plane XY respectively. It can be observed
that TOP and XYOT generally yields the best performance,
which indicates that the dynamic information along the time
dimension represents the most important information for ME
recognition. In contrast, the results on XY plane are almost the
worst. This is possibly because the XY plane contains much
redundant information about the facial appearance. Maybe
not all areas in the facial area contain useful discriminative
information for ME recognition.
Method
CASME II
SMIC
Acc. (%)
F1-score
Acc. (%)
F1-score
LBPTOP [1]
–
–
48.78
–
LBPMOP [33]
44.13
–
50.61
–
FDM [42]
45.933
0.411
54.883
0.541
LBPSIP [32]
46.56
–
44.51
–
3DFCNN [50]
59.11
–
55.49
–
STCLQP [39]
58.392
0.58
64.022
0.64
STLBP-IP [34]
59.51
–
57.93
–
CNN+LSTM [48]
60.98
–
–
–
BiWOOF + Phase [73]
62.553
0.65
68.293
0.67
Hierahical STLBP-IP [74]
63.833
0.61
60.783
0.61
STRBP [35]
64.37
–
60.98
–
Discriminative STLBP-IP [75]
64.78
–
63.41
–
OF Maps [44]
65.35
–
–
–
HIGOTOP [47]
67.31
–
68.29
–
ELBPTOP
73.94
0.69
69.06
0.62
1 The F1-score here is different, which is deﬁned as F = 2p×r
p+r ,
where p and r are the average precision and recall of all the ME class.
2 Mean recognition rate, which is obtained by averaging accuracies of classes.
3 Overall recognition rate, which is the number of correctly classiﬁed
samples over the total samples.
TABLE VII: Comparison between ELBPTOP and previous
state-of-the-art methods on CASME II (with original classes)
and SMIC.
Feature Fusion: In order to ﬁnd a good fusion of LBP*,
RDLBP*, and ADLBP* (here, * represents one of TOP,
XYOT, XOT, YOT and XY), we test all 215 (63 −1) possible
feature fusion schemes on SMIC and CASME II. All results
are shown in Figure 7 in descending order. We can see that the
highest accuracy is achieved by combining the three type of
binary codes. The best results on SMIC-HS is 69.06%, given
by ADLBPTOP1,8 + LBPTOP3,4 + RDLBPXOT4,4,3,
and on CASME II is 73.94%, given by ADLBPTOP2,4 +
LBPTOP3,4 + RDLBPXOT3,4,1.
As it can be seen from Figure 7, that the fused feature
increases the accuracy by 3.90%, 5.33% and 6.49% respec-
tively compared with using LBPTOP, ADLBPTOP or RDLBP-
TOP alone on SMIC. Similarly, the accuracy is improved by
2.39%,3.74% and 4.70% on the three binary codes respectively
on CASME II. The strong performance improvement shows
that the fused approach indeed captures complementary infor-
mation.
D. Comparative evaluation
(1) Single database results
We compare the best results achieved by our ELBPTOP
with the baseline method and recent and relevant works on
CASME II and SMIC with their original estimated emotion
classes in Table VII , and on CASME II and SAMM with
the reorganized objective classes in Table VIII. Since the
performance with different protocols is quite different, we only
compare the methods using the same LOSO strategy. For the
same method, results with LOSO are usually lower than those
with other protocols (LOVO, k-fold, and so on).
From Tables VII and VIII, we can observe that our pro-
posed approach consistently gives the best results on all three
datasets, signiﬁcantly outperforming the state-of-the-art. As
illustrated in Table VII, it is clear that our proposed method


## Page 10


10
ADLBPTOP2,4+
LBPTOP3,4+
RDLBPXOT3,4,1
Acc(%):73.94
ADLBPTOP1,8+     
LBPTOP3,4+
RDLBPXOT4,4,3
Acc(%):69.06
SMIC
CASME II
LBPTOP3,4
Acc(%):71.55
ADLBPTOP2,4
Acc(%):70.20
RDLBPXOT3,4,1
Acc(%):69.24
LBPTOP3,4
Acc(%):65.16
ADLBPTOP1,8
Acc(%):63.73
RDLBPXOT4,4,3
Acc(%):62.57
A1
A2
A3
A4
B1
B2
B3
B4
A1
A2
A3
A4
B1
B2
B3
B4
Fig. 7: ME recognition accuracy(%) of different feature fusion schemes on SMIC and CASME II. In the boxes, we show the
accuracy of the best fused descriptor and three single binary descriptors.
Method
SAMM
CASME II
Acc. (%)
F1-score
Acc. (%)
F1-score
LBPTOP [71]
44.70
0.35
67.80
0.51
HOOF [71]
42.17
0.33
69.64
0.56
HOG 3D [71]
34.16
0.22
69.53
0.51
ELBPTOP
63.44
0.48
79.55
0.66
TABLE VIII: Comparison between ELBPTOP and previous
state-of-the-art methods on SAMM and CASME II (with
reorganized classes).
produces the highest accuracy (73.94%) and the highest F1-
score (0.69), which is 6.63% higher in accuracy and 0.04
higher in F1-score than the second best on CASME II (with
original classes). In Table VIII, our method also surpasses
all other methods on CASME II (with reorganized classes)
signiﬁcantly, improving a margin of 9.91% in accuracy and
0.10 in F1-score. The effectiveness of our method is further
demonstrated by the large improvement on SAMM, with an
increase from 44.70% to 63.44% (a margin of 18.74%). The
strong performance on all ME datasets clearly proves that our
proposed ELBPTOP is effective for ME recognition.
(2) Cross database results
To test the generalization of our method, we also conduct
cross database experiments introduced in MEGC2018 1 and
MEGC2019 2 Composite Database Evaluation (CDE) are used
to test the performance. Following MEGC2018, all samples
from CASME II and SAMM with their reorganized objective
classes I-V
are combined into a single composite database.
There are total of 47 subjects (26 from CASME II and 29 from
SAMM) and 253 samples (185 from CASME II and 68 from
SAMM). The results are shown in Table IX. It can be seen
from the table that our method achieves the best F1-score and
the second weighted F1-score, conﬁrming the generalization
of our method.
Following MEGC2019, all samples from CASME II and
1http://www2.docm.mmu.ac.uk/STAFF/m.yap/FG2018Workshop.htm
2 https://facial-micro-expressiongc.github.io/MEGC2019/
Method
F1-score
Weighted F1-score
HOG 3D [76]
0.27
0.44
ELRCN [58]
0.39
0.52
LBPTOP [76]
0.40
0.52
HOOF [76]
0.40
0.53
Transfer learning [56]
0.64
0.73
ELBPTOP
0.64
0.71
TABLE IX: The results of composite database evaluation
according to MEGC 2018.
SAMM and SMIC are combined into a single composite
database, and the original emotion classes are grouped into
three main classes: negative, positive and surprise. There are
total of 68 subjects and 442 samples. Results in Table X. show
that our method is extremely powerful on the CASME II ,
achieving the highest UAR and F1-score. But there is still a
need for further exploration on SMIC and SAMM. We infer
that the following factors affect the performance on these two
datasets: (1) Different pre-processing methods and cropping
areas on SAMM. (2) Big differences in age and ethnicity in
SAMM. (3) The lower frame rate and lower resolution on
SMIC. These factors make the optimal parameters on each
data set inconsistent, which in turn affects performance.
V. CONCLUSION AND FUTURE WORK
In this paper, we proposed a simple, efﬁcient and robust
descriptor ELBPTOP for ME recognition. ELBPTOP consists
of three complementary binary descriptors: LBPTOP and
two novel ones RDLBPTOP and ADLBPTOP, which explore
the local second order information along radial and angular
directions contained in ME video sequences. For dimension
reduction, WPCA is used to obtain efﬁcient and discriminative
features. Extensive experiments on three benchmark sponta-
neous ME datasets, SMIC, CASME II and SAMM have shown
that our proposed approach surpasses state-of-the-art by a large
margin in single database recognition, and also achieve more
promising results on cross-database recognition.


## Page 11


11
Method
Full
SMIC
CASME II
SAMM
F1-score
UAR
F1-score
UAR
F1-score
UAR
F1-score
UAR
LBPTOP [23]
0.59
0.58
0.20
0.53
0.70
0.74
0.40
0.41
Bi-WOOF [45]
0.63
0.62
0.57
0.58
0.78
0.80
0.52
0.51
CapsuleNet [63]
0.65
0.65
0.58
0.59
0.71
0.70
0.62
0.60
OFF-ApexNet [59]
0.72
0.71
0.68
0.67
0.88
0.87
0.54
0.54
Dual-Inception Network [61]
0.73
0.73
0.66
0.67
0.86
0.86
0.59
0.57
STSTNet [60]
0.74
0.76
0.68
0.70
0.84
0.87
0.66
0.68
EMR with Adversarial Training [57]
0.79
0.78
0.75
0.75
0.83
0.82
0.78
0.72
ELBPTOP
0.71
0.69
0.65
0.66
0.89
0.88
0.49
0.49
TABLE X: The results of composite database evaluation according to MEGC 2019.
It is worth noting that there are some difﬁculties for micro-
expression analysis: (1) Lack of standard evaluation protocol.
Different evaluation protocols, performance metrics, number
of samples, and emotion classes are chosen by different
researchers. It raises the barriers of entry to this topic and
increases difﬁculties for a fair comparison. (2) Lack of large
scale spontaneous ME datasets. Small sample size and uneven
distribution are still the key to restriction the acquisition
of effective features and application to real life. Especially,
there are single emotion class in some subject, making it
more difﬁcult to obtain features that are distinguishable from
expressions rather than distinguishing from subjects.
Hand-crafted features conﬁrm that effective discriminant
characteristics can be learned. And in the current micro-
expression ﬁeld, many of the deep learning methods are based
on hand-crafted features. But some hyper parameters need to
be artiﬁcially selected, which restricts the performance in cross
database problem to some extent. In our future work, we plan
to design data-driven methods to learn binary codes directly
from data for ME recognition. In addition, in many works,
the AU information is very useful but we have not used it in
this paper. We will design a better area division algorithm to
utilize the AU information.
REFERENCES
[1] X. Li, T. Pﬁster, X. Huang, G. Zhao, and M. Pietik¨ainen, “A spontaneous
micro-expression database: Inducement, collection and baseline,” in
2013 10th IEEE International Conference and Workshops on Automatic
Face and Gesture Recognition (FG).
IEEE, 2013, pp. 1–6. 1, 6, 7, 8,
9
[2] W.-J. Yan, X. Li, S.-J. Wang, G. Zhao, Y.-J. Liu, Y.-H. Chen, and X. Fu,
“Casme ii: An improved spontaneous micro-expression database and the
baseline evaluation,” PloS one, vol. 9, no. 1, p. e86041, 2014. 1, 6, 7, 8
[3] A. K. Davison, C. Lansley, N. Costen, K. Tan, and M. H. Yap, “Samm:
A spontaneous micro-facial movement dataset,” IEEE Transactions on
Affective Computing, vol. 9, no. 1, pp. 116–129, 2018. 1, 6, 7, 8
[4] P. Ekman, “Darwin, deception, and facial expression,” Annals of the New
York Academy of Sciences, vol. 1000, no. 1, pp. 205–221, 2003. 1
[5] Q. Wu, X. Shen, and X. Fu, “Micro-expression and its applications,”
Advances in Psychological Science, vol. 18, no. 9, pp. 1359–1368, 2010.
1
[6] T. Pﬁster, X. Li, G. Zhao, and M. Pietik¨ainen, “Recognising spontaneous
facial micro-expressions,” in 2011 international conference on computer
vision.
IEEE, 2011, pp. 1449–1456. 1, 2, 6
[7] Y.-H. Oh, J. See, A. C. Le Ngo, R. C.-W. Phan, and V. M. Baskaran,
“A survey of automatic facial micro-expression analysis: Databases,
methods and challenges,” Frontiers in psychology, vol. 9, p. 1128, 2018.
1, 2
[8] B. Martinez and M. F. Valstar, “Advances, challenges, and opportunities
in automatic facial expression recognition,” in Advances in face detection
and facial image analysis.
Springer, 2016, pp. 63–100. 1
[9] W.-J. Yan, Q. Wu, J. Liang, Y.-H. Chen, and X. Fu, “How fast are the
leaked facial expressions: The duration of micro-expressions,” Journal
of Nonverbal Behavior, vol. 37, no. 4, pp. 217–230, 2013. 1
[10] S. Porter and L. Ten Brinke, “Reading between the lies: Identifying
concealed and falsiﬁed emotions in universal facial expressions,” Psy-
chological science, vol. 19, no. 5, pp. 508–514, 2008. 1
[11] L. Liu, J. Chen, P. Fieguth, G. Zhao, R. Chellappa, and M. Pietik¨ainen,
“From bow to cnn: Two decades of texture representation for texture
classiﬁcation,” International Journal of Computer Vision, vol. 127, no. 1,
pp. 74–109, 2019. 1
[12] W. Merghani, A. K. Davison, and M. H. Yap, “A review on facial micro-
expressions analysis: datasets, features and metrics,” arXiv preprint
arXiv:1805.02397, 2018. 1
[13] M. Shreve, S. Godavarthy, D. Goldgof, and S. Sarkar, “Macro-and
micro-expression spotting in long videos using spatio-temporal strain,”
in Face and Gesture 2011.
IEEE, 2011, pp. 51–56. 1
[14] S. Polikovsky, Y. Kameda, and Y. Ohta, “Facial micro-expressions
recognition using high speed camera and 3d-gradient descriptor,” 2009.
1, 2, 3
[15] G. Warren, E. Schertler, and P. Bull, “Detecting deception from emo-
tional and unemotional cues,” Journal of Nonverbal Behavior, vol. 33,
no. 1, pp. 59–69, 2009. 1
[16] W.-J. Yan, Q. Wu, Y.-J. Liu, S.-J. Wang, and X. Fu, “Casme database:
a dataset of spontaneous micro-expressions collected from neutralized
faces,” in 2013 10th IEEE international conference and workshops on
automatic face and gesture recognition (FG).
IEEE, 2013, pp. 1–7. 1
[17] F. Qu, S.-J. Wang, W.-J. Yan, H. Li, S. Wu, and X. Fu, “Cas (me)
2: A database for spontaneous macro-expression and micro-expression
spotting and recognition,” IEEE Transactions on Affective Computing,
vol. 9, no. 4, pp. 424–436, 2017. 1
[18] T. Ojala, M. Pietik¨ainen, and T. M¨aenp¨a¨a, “Multiresolution gray-scale
and rotation invariant texture classiﬁcation with local binary patterns,”
IEEE Transactions on Pattern Analysis & Machine Intelligence, no. 7,
pp. 971–987, 2002. 2, 3, 6
[19] T. Ojala, M. Pietik¨ainen, and D. Harwood, “A comparative study of
texture measures with classiﬁcation based on featured distributions,”
Pattern recognition, vol. 29, no. 1, pp. 51–59, 1996. 2, 3
[20] S. ul Hussain and B. Triggs, “Visual recognition using local quantized
patterns,” in European conference on computer vision.
Springer, 2012,
pp. 716–729. 2
[21] N. Dalal and B. Triggs, “Histograms of oriented gradients for human
detection,” 2005. 2
[22] B. K. Horn and B. G. Schunck, “Determining optical ﬂow,” Artiﬁcial
intelligence, vol. 17, no. 1-3, pp. 185–203, 1981. 2
[23] G. Zhao and M. Pietikainen, “Dynamic texture recognition using local
binary patterns with an application to facial expressions,” IEEE Trans-
actions on Pattern Analysis & Machine Intelligence, no. 6, pp. 915–928,
2007. 2, 3, 4, 11
[24] R. Chaudhry, A. Ravichandran, G. Hager, and R. Vidal, “Histograms of
oriented optical ﬂow and binet-cauchy kernels on nonlinear dynamical
systems for the recognition of human actions,” in 2009 IEEE Conference
on Computer Vision and Pattern Recognition.
IEEE, 2009, pp. 1932–
1939. 2, 3
[25] L. Liu, P. Fieguth, Y. Guo, X. Wang, and M. Pietik¨ainen, “Local binary
features for texture classiﬁcation: Taxonomy and experimental study,”
Pattern Recognition, vol. 62, pp. 135–160, 2017. 2
[26] T. Ahonen, A. Hadid, and M. Pietikainen, “Face description with local
binary patterns: Application to face recognition,” IEEE Transactions on
Pattern Analysis & Machine Intelligence, no. 12, pp. 2037–2041, 2006.
2, 3


## Page 12


12
[27] T.-H. Oh, R. Jaroensri, C. Kim, M. Elgharib, F. Durand, W. T. Free-
man, and W. Matusik, “Learning-based video motion magniﬁcation,” in
Proceedings of the European Conference on Computer Vision (ECCV),
2018, pp. 633–648. 2
[28] D. Huang, C. Shan, M. Ardabilian, Y. Wang, and L. Chen, “Local binary
patterns and its application to facial image analysis: a survey,” IEEE
Transactions on Systems, Man, and Cybernetics, Part C (Applications
and Reviews), vol. 41, no. 6, pp. 765–781, 2011. 2
[29] A. Fern´andez, M. X. ´Alvarez, and F. Bianconi, “Texture description
through histograms of equivalent patterns,” Journal of mathematical
imaging and vision, vol. 45, no. 1, pp. 76–102, 2013. 2
[30] L. Liu, P. Fieguth, G. Zhao, M. Pietik¨ainen, and D. Hu, “Extended local
binary patterns for face recognition,” Information Sciences, vol. 358, pp.
56–72, 2016. 2
[31] L. Liu, S. Lao, P. W. Fieguth, Y. Guo, X. Wang, and M. Pietik¨ainen,
“Median robust extended local binary pattern for texture classiﬁcation,”
IEEE Transactions on Image Processing, vol. 25, no. 3, pp. 1368–1381,
2016. 2
[32] Y. Wang, J. See, R. C.-W. Phan, and Y.-H. Oh, “Lbp with six intersection
points: Reducing redundant information in lbp-top for micro-expression
recognition,” in Asian conference on computer vision.
Springer, 2014,
pp. 525–537. 2, 9
[33] ——, “Efﬁcient spatio-temporal local binary patterns for spontaneous fa-
cial micro-expression recognition,” PloS one, vol. 10, no. 5, p. e0124674,
2015. 2, 9
[34] X. Huang, S.-J. Wang, G. Zhao, and M. Piteikainen, “Facial micro-
expression recognition using spatiotemporal local binary pattern with
integral projection,” in Proceedings of the IEEE international conference
on computer vision workshops, 2015, pp. 1–9. 2, 3, 9
[35] X. Huang and G. Zhao, “Spontaneous facial micro-expression analysis
using spatiotemporal local radon-based binary pattern,” in 2017 Inter-
national Conference on the Frontiers and Advances in Data Science
(FADS).
IEEE, 2017, pp. 159–164. 2, 3, 9
[36] Z. Zeng, M. Pantic, G. I. Roisman, and T. S. Huang, “A survey of affect
recognition methods: Audio, visual, and spontaneous expressions,” IEEE
transactions on pattern analysis and machine intelligence, vol. 31, no. 1,
pp. 39–58, 2008. 2
[37] X. Ben, X. Jia, R. Yan, X. Zhang, and W. Meng, “Learning effective bi-
nary descriptors for micro-expression recognition transferred by macro-
information,” Pattern Recognition Letters, vol. 107, pp. 50–58, 2018. 3,
8
[38] C. Ding, J. Choi, D. Tao, and L. S. Davis, “Multi-directional multi-level
dual-cross patterns for robust face recognition,” IEEE transactions on
pattern analysis and machine intelligence, vol. 38, no. 3, pp. 518–531,
2015. 3
[39] X. Huang, G. Zhao, X. Hong, W. Zheng, and M. Pietik¨ainen, “Sponta-
neous facial micro-expression analysis using spatiotemporal completed
local quantized patterns,” Neurocomputing, vol. 175, pp. 564–578, 2016.
3, 9
[40] S.-J. Wang, W.-J. Yan, G. Zhao, X. Fu, and C.-G. Zhou, “Micro-
expression recognition using robust principal component analysis and
local spatiotemporal directional features,” in European Conference on
Computer Vision.
Springer, 2014, pp. 325–338. 3, 8
[41] J. Wright, A. Ganesh, S. Rao, Y. Peng, and Y. Ma, “Robust principal
component analysis: Exact recovery of corrupted low-rank matrices via
convex optimization,” in Advances in neural information processing
systems, 2009, pp. 2080–2088. 3
[42] F. Xu, J. Zhang, and J. Z. Wang, “Microexpression identiﬁcation and
categorization using a facial dynamics map,” IEEE Transactions on
Affective Computing, vol. 8, no. 2, pp. 254–267, 2017. 3, 9
[43] Y.-J. Liu, J.-K. Zhang, W.-J. Yan, S.-J. Wang, G. Zhao, and X. Fu,
“A main directional mean optical ﬂow feature for spontaneous micro-
expression recognition,” IEEE Transactions on Affective Computing,
vol. 7, no. 4, pp. 299–310, 2016. 3
[44] B. Allaert, I. M. Bilasco, and C. Djeraba, “Consistent optical ﬂow maps
for full and micro facial expression recognition,” 2017. 3, 9
[45] S.-T. Liong, J. See, K. Wong, and R. C.-W. Phan, “Less is more: Micro-
expression recognition from video using apex frame,” Signal Processing:
Image Communication, vol. 62, pp. 82–92, 2018. 3, 11
[46] Y. Zhao and J. Xu, “An improved micro-expression recognition method
based on necessary morphological patches,” Symmetry, vol. 11, no. 4,
p. 497, 2019. 3, 8
[47] X. Li, X. Hong, A. Moilanen, X. Huang, T. Pﬁster, G. Zhao, and
M. Pietik¨ainen, “Towards reading hidden emotions: A comparative study
of spontaneous micro-expression spotting and recognition methods,”
IEEE Transactions on Affective Computing, vol. 9, no. 4, pp. 563–577,
2018. 3, 5, 6, 8, 9
[48] D. H. Kim, W. J. Baddar, and Y. M. Ro, “Micro-expression recognition
with expression-state constrained spatio-temporal feature representa-
tions,” in Proceedings of the 24th ACM international conference on
Multimedia.
ACM, 2016, pp. 382–386. 3, 9
[49] M. Peng, C. Wang, T. Chen, G. Liu, and X. Fu, “Dual temporal
scale convolutional neural network for micro-expression recognition,”
Frontiers in psychology, vol. 8, p. 1745, 2017. 3, 8
[50] J. Li, Y. Wang, J. See, and W. Liu, “Micro-expression recognition
based on 3d ﬂow convolutional neural network,” Pattern Analysis and
Applications, pp. 1–9, 2018. 3, 9
[51] S. P. T. Reddy, S. T. Karri, S. R. Dubey, and S. Mukherjee, “Spontaneous
facial micro-expression recognition using 3d spatiotemporal convolu-
tional neural networks,” arXiv preprint arXiv:1904.01390, 2019. 3, 8
[52] Z. Xia, X. Feng, X. Hong, and G. Zhao, “Spontaneous facial micro-
expression recognition via deep convolutional network,” in 2018 Eighth
International Conference on Image Processing Theory, Tools and Ap-
plications (IPTA).
IEEE, 2018, pp. 1–6. 3, 8
[53] M. H. Yap, J. See, X. Hong, and S.-J. Wang, “Facial micro-expressions
grand challenge 2018 summary,” in 2018 13th IEEE International
Conference on Automatic Face & Gesture Recognition (FG 2018).
IEEE, 2018, pp. 675–678. 3, 7
[54] J. See, M. H. Yap, J. Li, X. Hong, and S.-J. Wang, “Megc 2019–the
second facial micro-expressions grand challenge,” in 2019 14th IEEE
International Conference on Automatic Face & Gesture Recognition (FG
2019).
IEEE, 2019, pp. 1–5. 3, 7
[55] Y. Zong, W. Zheng, X. Hong, C. Tang, Z. Cui, and G. Zhao, “Cross-
database micro-expression recognition: A benchmark,” in Proceedings of
the 2019 on International Conference on Multimedia Retrieval.
ACM,
2019, pp. 354–363. 3
[56] M. Peng, Z. Wu, Z. Zhang, and T. Chen, “From macro to micro
expression recognition: deep learning on small datasets using transfer
learning,” in 2018 13th IEEE International Conference on Automatic
Face & Gesture Recognition (FG 2018).
IEEE, 2018, pp. 657–661. 3,
10
[57] Y. Liu, H. Du, L. Zheng, and T. Gedeon, “A neural micro-expression
recognizer,” in 2019 14th IEEE International Conference on Automatic
Face Gesture Recognition (FG 2019).
IEEE, 2019, pp. 1–4. 3, 11
[58] H.-Q. Khor, J. See, R. C. W. Phan, and W. Lin, “Enriched long-term
recurrent convolutional network for facial micro-expression recognition,”
in 2018 13th IEEE International Conference on Automatic Face &
Gesture Recognition (FG 2018).
IEEE, 2018, pp. 667–674. 3, 10
[59] S.-T. Liong, Y. Gan, W.-C. Yau, Y.-C. Huang, and T. L. Ken,
“Off-apexnet on micro-expression recognition system,” arXiv preprint
arXiv:1805.08699, 2018. 3, 11
[60] S.-T. Liong, Y. Gan, J. See, and H.-Q. Khor, “A shallow triple stream
three-dimensional cnn (ststnet) for micro-expression recognition sys-
tem,” arXiv preprint arXiv:1902.03634, 2019. 3, 11
[61] L. Zhou, Q. Mao, and L. Xue, “Dual-inception network for cross-
database micro-expression recognition,” in 2019 14th IEEE International
Conference on Automatic Face & Gesture Recognition (FG 2019).
IEEE, 2019, pp. 1–5. 3, 11
[62] M. Peng, C. Wang, T. Bi, T. Chen, X. Zhou et al., “A novel apex-time
network for cross-dataset micro-expression recognition,” arXiv preprint
arXiv:1904.03699, 2019. 3
[63] N. Van Quang, J. Chun, and T. Tokuyama, “Capsulenet for micro-
expression recognition,” in 2019 14th IEEE International Conference
on Automatic Face & Gesture Recognition (FG 2019).
IEEE, 2019,
pp. 1–7. 3, 11
[64] M. Turk and A. Pentland, “Eigenfaces for recognition,” Journal of
cognitive neuroscience, vol. 3, no. 1, pp. 71–86, 1991. 5
[65] H. V. Nguyen, L. Bai, and L. Shen, “Local gabor binary pattern whitened
pca: A novel approach for face recognition from single image per
person,” in International conference on biometrics.
Springer, 2009,
pp. 269–278. 5
[66] T. F. Cootes, C. J. Taylor, D. H. Cooper, and J. Graham, “Active
shape models-their training and application,” Computer vision and image
understanding, vol. 61, no. 1, pp. 38–59, 1995. 6
[67] Y. Wang, J. See, Y.-H. Oh, R. C.-W. Phan, Y. Rahulamathavan, H.-
C. Ling, S.-W. Tan, and X. Li, “Effective recognition of facial micro-
expressions with video motion magniﬁcation,” Multimedia Tools and
Applications, vol. 76, no. 20, pp. 21 665–21 690, 2017. 6, 8
[68] H.-Y. Wu, M. Rubinstein, E. Shih, J. Guttag, F. Durand, and W. Freeman,
“Eulerian video magniﬁcation for revealing subtle changes in the world,”
2012. 6
[69] Z. Zhou, G. Zhao, and M. Pietik¨ainen, “Towards a practical lipreading
system,” in CVPR 2011.
IEEE, 2011, pp. 137–144. 6, 8


## Page 13


13
[70] C.-C. Chang and C.-J. Lin, “Libsvm: a library for support vector
machines,” ACM transactions on intelligent systems and technology
(TIST), vol. 2, no. 3, p. 27, 2011. 7
[71] A. Davison, W. Merghani, and M. Yap, “Objective classes for micro-
facial expression recognition,” Journal of Imaging, vol. 4, no. 10, p.
119, 2018. 7, 10
[72] P. Ekman and W. V. Friesen, Facial action coding system: Investigator’s
guide.
Consulting Psychologists Press, 1978. 7
[73] S.-T. Liong and K. Wong, “Micro-expression recognition using apex
frame with phase information,” in 2017 Asia-Paciﬁc Signal and Infor-
mation Processing Association Annual Summit and Conference (APSIPA
ASC).
IEEE, 2017, pp. 534–537. 9
[74] Y. Zong, X. Huang, W. Zheng, Z. Cui, and G. Zhao, “Learning from hi-
erarchical spatiotemporal descriptors for micro-expression recognition,”
IEEE Transactions on Multimedia, vol. 20, no. 11, pp. 3160–3172, 2018.
9
[75] H. Xiaohua, S.-J. Wang, X. Liu, G. Zhao, X. Feng, and M. Pietikainen,
“Discriminative spatiotemporal local binary pattern with revisited in-
tegral projection for spontaneous facial micro-expression recognition,”
IEEE Transactions on Affective Computing, 2017. 9
[76] W. Merghani, A. Davison, and M. Yap, “Facial micro-expressions grand
challenge 2018: evaluating spatio-temporal features for classiﬁcation
of objective classes,” in 2018 13th IEEE International Conference on
Automatic Face & Gesture Recognition (FG 2018).
IEEE, 2018, pp.
662–666. 10

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
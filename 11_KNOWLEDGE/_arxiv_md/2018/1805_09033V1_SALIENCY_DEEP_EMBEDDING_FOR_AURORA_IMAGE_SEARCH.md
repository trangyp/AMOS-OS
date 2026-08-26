---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1805.09033v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1805.09033v1_Saliency_deep_embedding_for_aurora_image_search

> Source: 1805.09033v1_Saliency_deep_embedding_for_aurora_image_search.pdf

> Pages: 6

---


## Page 1


SALIENCY DEEP EMBEDDING FOR AURORA IMAGE SEARCH
Xi Yang1, Xinbo Gao2, Bin Song1, Nannan Wang1 and Dong Yang3
1State Key Laboratory of Integrated Services Networks, School of Telecommunications Engineering, Xidian University, China
2State Key Laboratory of Integrated Services Networks, School of Electronic Engineering, Xidian University, China
3Xi’an Institute of Space Radio Technology, China
ABSTRACT
Deep neural networks have achieved remarkable success in
the ﬁeld of image search. However, the state-of-the-art al-
gorithms are trained and tested for natural images captured
with ordinary cameras. In this paper, we aim to explore a
new search method for images captured with circular ﬁsh-
eye lens, especially the aurora images. To reduce the inter-
ference from uninformative regions and focus on the most
interested regions, we propose a saliency proposal network
(SPN) to replace the region proposal network (RPN) in the
recent Mask R-CNN. In our SPN, the centers of the anchors
are not distributed in a rectangular meshing manner, but ex-
hibit spherical distortion. Additionally, the directions of the
anchors are along the deformation lines perpendicular to the
magnetic meridian, which perfectly accords with the imaging
principle of circular ﬁsheye lens. Extensive experiments are
performed on the big aurora data, demonstrating the superior-
ity of our method in both search accuracy and efﬁciency.
Index Terms— Aurora image search, convolutional neu-
ral network, saliency proposal network
1. INTRODUCTION
The powerful learning capacity of deep neural networks, es-
pecially the convolutional neutral network (CNN), has pro-
moted the development in various computer tasks [1]. In the
ﬁeld of image search, researchers introduce the CNN as an ef-
fective feature extraction tool into the content-based image re-
trieval (CBIR) framework. Although the existing CNN-based
methods greatly improve the search accuracy compared with
the SIFT-based methods, the images they process are captured
with ordinary cameras without imaging distortion.
In practice, there are still a lot of images captured with cir-
cular ﬁsheye lens with spherical aberration. Especially in the
natural science ﬁeld, phenomena in the sky are imaged from
observation stations via the all sky imagers (ASI) to achieve
This work was supported in part by the National Natural Science Foun-
dation of China (61602355, 61432014 and U1605252), the China Post-
Doctoral Science Foundation (2016M590926), the Shaanxi Province Natural
Science Foundation (2017JQ6007 and 2017JM6085) and Shaanxi Province
Post-Doctoral Science Foundation.
(a)
(b)
Fig. 1. Related images of the ASI in YRS and the captured
aurora images. (a) ASI in YRS. (b) Example aurora images.
bigger imaging vision. Thus, applying the CNN-based meth-
ods for the search of images captured with circular ﬁsheye
lens is a new task and of great signiﬁcance.
In this paper, we select the aurora images as a typical ex-
ample to present our search method for circular ﬁsheye lens.
Generally, aurora is a natural light occurred in the high lati-
tude regions caused by the collision of solar wind and parti-
cles in earth’s magnetic ﬁeld. As one of the most important
natural phenomenon, scientists utilize multiple ways to cap-
ture it. In speciﬁc, the Yellow River Station (YRS) located
at geographic coordinates 78.921N, 11.931E uses the ASIs to
capture aurora occurred in the sky above, and the output im-
age is in grayscale with size 512 × 512. Fig. 1 shows related
images of the ASI in YRS and the captured aurora images.
Traditional aurora image search is conducted based on the
visual observation. This manual way is time consuming and
easily contaminated with visual fatigue. Hence, Yang et. al.
proposed a polar embedding (PE) model to realize automatic
aurora image search. The PE model [2] leveraged the bag-of-
words (BoW) framework [3] and extracted the SIFT feature
and deep local binary pattern (DLBP) feature for each key-
point. Although it achieved comparable performance in the
big ASI aurora image dataset, its hand-crafted feature extrac-
tion and full domain computation limit the improvement of
search accuracy and efﬁciency.
To this end, we propose a saliency deep embedding (SDE)
model in this paper. On one hand, we exploit the power-
ful CNN model for feature extraction, and thus achieve a
“deep” understanding of aurora images. On the other hand,
978-1-5386-1737-3/18/$31.00 c⃝2018 IEEE
arXiv:1805.09033v1  [cs.CV]  23 May 2018


## Page 2


we present a “saliency” domain computation way to reduce
the memory cost and accelerate the online search time.
Speciﬁcally, the SDE model is inherited from the ad-
vanced Mask R-CNN [4] and reﬁned in consideration of the
imaging principles of circular ﬁsheye lens. Notably, Mask R-
CNN is trained in the COCO dataset whose images are cap-
tured with ordinary cameras. Thus, the RPN is designed with
rectangular meshing scheme, i.e., the centers of the sliding
windows and anchors are distributed uniformly with horizon-
tal surrounding boxes. In contrast, for ASI aurora images
with spherical distortion, we revise the RPN as a SPN by
combining the information of geomagnetic coordinates and
circular imaging procedure.
In our SPN, the locations of
the anchors are distributed along the line of deformed lati-
tude, while the shapes of anchors are determined based on the
geometrical morphology of aurora structures. Also, the fea-
ture pyramid network (FPN) is applied in our SPN to achieve
multi-scale feature representation. The proposed SDE model
greatly facilitates the physics research, which liberates re-
searchers from burdensome visual observation and is helpful
for their further study of solar-terrestrial space.
2. BACKGROUND
2.1. CNN-Based Image Search
As one of the most famous deep neural network, CNN was
proposed for the task of image classiﬁcation with the last
fully-connected layer exporting category labels. Commonly
used models comprise AlexNet [5], VGG [6], ResNet [7] and
its variants (e.g., ResNeXt [8]).
For the ﬁeld of image search, CNN is utilized as a feature
extraction tool while the fully-connected layers (e.g., FC6 in
AlexNet) are ﬁrst used as the high level semantic features.
Also, region partition schemes, such as the spatial pyramid
matching (SPM) [9], are explored to introduce spatial infor-
mation and generate regional CNN feature. Related work in-
cludes the multi-scale orderless pooling (MOP) model [10]
which cascades regional CNN features as a global signature,
and the probabilistic analysis (PA) model [11] which com-
bines the CNN features in global image and multi-scale re-
gions together. Subsequently, researchers observe that out-
puts of the convolutional layers are capable of representing
mid-level features and thus achieve remarkable performance,
e.g., maximum activation of convolutions (MAC) model [12].
In practice, the search target is not always the whole im-
age but the objects therein. Hence, it is necessary to review
the CNN models for object recognition. One of the most fa-
mous model is the regions with CNN features (R-CNN) [13].
However, this approach is memory consuming because the
region determination is outside the deep network.
To this
end, numerous improved models are presented to design a
region generation module which can be trained jointly with
the main CNN structure. This series of work encompasses
(a)
(b)
M.N.
M.S.
arc
vortex
Fig. 2. Characteristic of the ASI aurora image. (a) Auroral
structures. (b) Deformation lines and magnetic meridian.
Fast R-CNN [14], Faster R-CNN [15], YOLO [16], SSD [17],
YOLO2 [18], etc. Especially, in the Faster R-CNN, the re-
gion generation module is designed as a fully convolutional
neural network called region proposal network (RPN). Re-
cently, the Mask R-CNN is proposed to realize pixel-level
image segmentation, object detection and recognition simul-
taneously. It utilizes the feature pyramid network (FPN) for
RPN to achieve multi-scale representation. Also, the replace-
ment of RoIPool as RoIAlign promotes the precision of loca-
tion projection between feature maps and the original image,
thus achieving amazing performance.
2.2. Characteristic of the ASI aurora image
The ASI aurora images are captured from the ground to the
sky above by circular ﬁsheye lens with expanded ﬁeld of view.
Hence, the contents in ASI aurora image are distributed non-
uniformity. Speciﬁcally, based on the imaging principle of
circular ﬁsheye lens, the peripheral zone exhibits more serious
deformation than the central zone. Additionally, because of
the gap between geomagnetic and geophysical coordinates in
YRS, there is an offset angle ϕ from the horizontal center line
to the connection line of magnetic north (M.N.) and magnetic
south (M.S.), i.e., magnetic meridian.
Furthermore, the key factor affecting aurora image search
results is the “arc” or “vortex” structures therein (as illus-
trated in Fig. 2(a)). If images in the dataset contain simi-
lar auroral structures with the query image, they can be ex-
ported as search results. Generally, as shown in Fig. 2(b)
these auroral structures are located along the deformation
lines (marked with orange dashed lines) perpendicular to the
magnetic meridian (marked with red solid line).
3. THE PROPOSED METHOD
This paper reﬁnes the Mask R-CNN model based on the
characteristic of ASI aurora image, and thus proposes a
SDE model for aurora image search.
Our model focuses
on saliency regions with informative auroral structures and
presents a SPN to replace the traditional RPN. We ﬁrst review


## Page 3


Pre-Training on COCO
COCO
ASI Aurora
Fine-Tuning on ASI Aurora
Online Search
Hyper-Parameter Transferring 
SPN
…
…
…
…
Regional
Indexing
Search Results
Query Image
Ranking
R-P2
R-P4
R-P3
R-P5
C1
C2
C3
C4
C5
RPN with FPN 
RoIAlign
Mask
class
box
segmentation
C1
C2
C3
C4
C5
RoIAlign
P2
P3
P4
P5
R-P2
R-P4
R-P3
R-P5
G-P2
G-P4
G-P3
G-P5
Global
Comparing
Fig. 3. The diagram of the proposed SDE model.
the proposed method, and then explain the main innovations
in detail.
3.1. Overview of the proposed SDE model
As illustrated in Fig. 3, the proposed SDE model is composed
of three parts, i.e., pre-training on COCO, ﬁne-tuning on ASI
aurora and online search.
Pre-Training on COCO. To inherit the strong power of
existing CNN structure, we prefer the Mask R-CNN trained
on COCO dataset as our pre-training model.
Generally,
the backbone architecture in Mask R-CNN is the Faster R-
CNN with ResNet/ResNeXt and FPN. To preserve exact spa-
tial locations in the feature maps, Mask R-CNN presents a
RoIAlign layer which achieves prominent performance. In
practice, we conduct hyper-parameters transferring on the
convolutional layers (abbreviated as C2 to C5) as the initial
setting for our SDE model, while the RPN module is dis-
carded to redesign.
Fine-Tuning on ASI Aurora. Since images in the COCO
dataset are captured with ordinary cameras, we perform ﬁne-
tuning on our ASI aurora images to conform to the proper-
ties of circular ﬁsheye lens. At ﬁrst, data augmentation is
conducted to make training data big enough. Then, hyper-
parameters are ﬁne-tuned for adapting our aurora dataset. No-
tably, the RPN is replaced as a SPN module. Here, the pro-
posed SPN determines the locations of anchors based on the
deformation lines and geomagnetic lines. While the direc-
tions and shapes of the bounding boxes around the anchors are
trained individually. Subsequently, the FPN is leveraged to
achieve multi-scale feature, and the RoIAlign layer is applied
to realize precise location mapping between feature maps and
the original image. Finally, top regions are outputted with
their features normalized to the same length. Together with
the global CNN feature, all features related to each image are
saved and the ofﬂine indexing is accomplished.
Online Search. When given a query image, same opera-
tions are conducted to extract multi-scale CNN feature. Af-
terwards, referring to the indexing table, the global CNN fea-
tures are ﬁrst compared to compute a global similarity score.
For each regional CNN feature in the query image, we scan
all regional CNN features of the compared image to get a re-
gional similarity score. After processing all images in the
dataset with the outputted similarity scores, search result is
determined with the highest score regarded as the most simi-
lar one.
3.2. SPN layer for feature extraction
The proposed SDE model extracts both global and regional
CNN features for searching, the regional CNN feature de-
scribes the speciﬁc auroral structure in an image, while the
global CNN feature supplies the distribution of these auro-
ral structures. In practice, only images achieve high similar-
ity scores on both global feature and regional features can be
treated as a similar result.
For the global CNN feature, we directly cascade the out-
puts of FPN {Pi} = {P2, P3, P4, P5} without the region gen-
eration module. For the regional CNN feature, we propose a
SPN layer to determine region proposals and directly link the
SPN to FPN for generating multi-scale features. By consid-
ering the imaging principle of circular ﬁsheye lens and the
characteristic of the ASI aurora image, our SPN is mainly
composed of three parts, i.e., circular anchors determination,
region proposals detection and multi-scale feature extraction.
Circular Anchors Determination.
Traditional R-CNN


## Page 4


Fig. 4.
Circular anchors and region proposals determined
by SPN. The circular anchors are marked with red dots and
the corresponding region proposals are marked with red solid
bounding boxes.
based methods regard the intersections of rectangular mesh-
ing as anchors, which is not suitable for images captured with
circular ﬁsheye lens. By analyzing the characteristic of ASI
aurora image, our SPN considers both radial distortion and
equatorial distortion. With the camera parameters and loca-
tion information, the SPN draws the longitude and latitude
deformation lines while treats their intersections as our circu-
lar anchors (see Fig. 4). If the magnetic meridian is divided
into l segments, all the deformation lines are cut into l parts,
thus resulting in l2 anchors. It can be seen that our circular
anchors not only accord with the shape of auroral structure,
but reﬂect the information of geomagnetic latitude and longi-
tude as well, which is capable of promoting the physical study
in the future.
Region Proposals Detection. Following the idea of Mask
R-CNN, we generate bounding boxes centered at the circular
anchors with different length-width ratios and scales. As il-
lustrated in Fig.4, the directions of the bounding boxes are not
horizontal as traditional methods, but along the deformation
lines perpendicular to magnetic meridian. Hence, the result-
ing bounding boxes are able to enclose auroral structures with
minimum area. Inspired by the work of YOLO2, we conduct
K-means clustering to ASI aurora image dataset with regions
labeled by polar experts. In practice, with the increase of
clustering numbers K, the average IOU scores ﬁrst increase
rapidly and then attain a high value with small improvement.
To strike a balance between precision and complexity, we ﬁ-
nally choose K = 6 bounding boxes priors. Thanks to these
superior priors, the trained SPN is easy to learn and predict
promising detections. Also, the FPN scheme is leveraged to
achieve multi-scale region proposals generated from different
pyramid layer Pi. Finally, region proposals with high proba-
bility carrying auroral structures are exported.
Multi-Scale Feature Extraction.
For each region pro-
posal, we directly project its location to the corresponding
feature maps with RoIAlign layer which is much more pre-
cise than the previous RoIPool. Afterwards, for each region
proposal in each pyramid layer Pi, max-pooling is performed
on the related tensors in feature maps and thus results in a fea-
ture vector {R−P2, R−P3, R−P4, R−P5}. By scanning all
the region proposals in all pyramid layers, the regional CNN
features in multi-scale are extracted. The same operations are
conducted for the global image to obtain the global CNN fea-
ture {G−P2, G−P3, G−P4, G−P5}. Here, each R−Pi or
G −Pi is set to 256-D. Consequently, the multi-scale feature
we extracted covers multi-level sematic information.
3.3. Indexing and querying
For the ASI aurora dataset composing of D images, the pro-
posed SPN outputs rd regional CNN feature vectors and one
global CNN feature vector for each image. Here, rd is de-
pends on the number of auroral structures in the dth image.
Hereafter, we save the image ID and the corresponding multi-
scale CNN features into the indexing table.
In the stage of online search, we leverage the proposed
SPN to extract CNN features for the query image following
the same steps used in the ofﬂine training procedure. Also, the
exported CNN feature in multi-scale consists of one global
part and rq regional parts. By measuring the similarities in
both global and regional parts between the query image Q and
image in the ASI aurora dataset I, the total similarity score
can be computed as SS(Q, I) = SSG(Q, I) + SSR(Q, I),
where SSG(Q, I) and SSR(Q, I) are the global similarity
score and regional similarity score, respectively, i.e.,
SSG(Q, I) =
1
1 + dis(GQ, GI),
(1)
dis(GQ, GI) =
5
X
i=2
d(GQ −Pi, GI −Pi),
(2)
SSR(Q, I) =
1
1 + 1
rq
rq
P
r=1
dis(RQ
r , RI)
,
(3)
dis(RQ
r , RI) = 1
rd
rd
X
r′=1
5
X
i=2
d(RQ
r −Pi, RI
r′ −Pi).
(4)
Here, dis(GQ, GI) is the distance between the global CNN
feature in Q and I, and it is actually the addition of the Eu-
clidean distances between each G −Pi(i = 2, · · · 5). For the
regional CNN features, dis(RQ
r , RI) is the average value of
Euclidean distance addition between each R−Pi(i = 2, · · · 5)
of one region in Q and all other rd regions in I. By scanning
all rq regions in the query image, its average value of the ad-
dition of dis(RQ
r , RI) can be computed. The lower of this
value, the higher of the SSR(Q, I), indicating that Q and I
are more similar in region proposals.
Notably, the regional similarity score SSR(Q, I) mea-
sures the matching degree of every auroral structure, while
the global similarity score SSG(Q, I) represents the match-
ing degree of the distributions of auroral structures. Only im-
ages similar on both global distribution and regional detailed
structures can be treated as satisfying results. Finally, we rank


## Page 5


Table 1.
Comparison of mAPs(%) using traditional RPN
layer and the proposed SPN layer.
Methods
8K
14K
100K
500K
1M
RA+HD
66.72
65.12
63.21
61.01
55.21
CA+HD
70.14
68.15
65.47
64.89
59.01
CA+DD
73.16
72.10
71.90
70.42
69.85
the candidate images based on the total similarity score from
highest to lowest.
4. EXPERIMENTS ON AURORA IMAGE SEARCH
To demonstrate the effectiveness of the proposed SDE model,
extensive experiments are conducted on the ASI aurora im-
age dataset. Our dataset are labeled with aurora experts, and
they manually construct a query dataset “ASI8K” including
10 special categories with 800 images for each one [2]. Other
datasets with different sizes comprise ASI14K, ASI100K,
ASI500K and ASI1M.
4.1. Effectiveness of the SPN layer
The major innovation of our SDE model is the SPN layer de-
signed for images captured with circular ﬁsheye lens. Our
SPN layer determines the locations of circular anchors and
the corresponding region proposals. To prove the effective-
ness of these two aspects, we compare the rectangular mesh-
ing for anchors location determination and the horizontal di-
rection for region proposals. Both of them are widely used in
the RPN layer of CNN-based object detection methods.
Table 1 gives the comparison of mAPs using traditional
RPN layer and the proposed SPN layer on datasets with in-
creasing sizes. Noting that the datasets are abbreviated as
their sizes (e.g., 8K for ASI8K), RA and CA stands for an-
chors with rectangular meshing and circular meshing, while
HD and DD stands for anchors with horizontal direction and
deformational direction.
It can be seen that the traditional RPN layer, which is ac-
tually the RA+HD approach, obtains the lowest mAP due to
the inappropriate region proposals it determined. In contrast,
CA+HD improves the mAP by 3.28% on average, demon-
strating the effectiveness of the circular anchors determina-
tion. Subsequently, CA+DD, which is actually the proposed
SPN layer, further improves the mAP by 5.95% on average
and achieves the highest accuracy, indicating that the DD is
superior than HD. Since the DD approach is based on the lo-
cations of CA, there is no RA+DD approach. Therefore, we
can conclude that our SPN layer greatly promotes the perfor-
mance of aurora image search.
4.2. Importance of the multi-scale feature
Our SDE model leverages the multi-scale CNN feature for
indexing and querying. This “multi-scale” lies in two aspects.
Table 2.
Comparison of mAPs(%) using different scales of
CNN features.
CNN feature
8K
14K
100K
500K
1M
R −P2
68.41
67.45
66.32
64.95
62.54
R −P3
68.21
67.55
66.00
64.21
61.95
R −P4
67.12
67.23
65.49
64.15
61.25
R −P5
67.03
66.98
65.12
63.95
61.02
R −Pi
70.54
69.51
68.39
66.83
65.21
G −P2
66.25
65.98
64.21
63.22
60.98
G −P5
65.84
64.32
63.54
61.11
59.87
G −Pi
68.74
67.24
66.52
64.81
63.14
R −Pi&G −Pi
73.16
72.10
71.90
70.42
69.85
On one hand, we adopt the FPN to fuse features from different
pyramid layers with different levels of semantic information
and different resolutions. On the other hand, we extract not
only regional CNN features to compare the similarity between
auroral structures, but also global CNN feature to measure the
overall distribution of related structures.
Table 2 illustrates the comparison of mAPs using differ-
ent scales of CNN features. The ﬁrst four rows present results
with single pyramid regional CNN feature, from which we
can see that the R−P2 performs a little better than other layers
due to its ﬁnest semantic level combining the information of
C2 to C5. By merging all pyramid regional layers, the R −Pi
improves the search accuracy signiﬁcantly, demonstrating the
effectiveness of the usage of FPN in our framework. Similar
results can be observed in the single pyramid global CNN fea-
ture and their combination G −Pi, and their mAPs are lower
than the regional ones because of the rough description. Here,
results of G −P3 and G −P4 are omitted for simplicity.
Remarkably, our multi-scale CNN feature R −Pi&G −Pi
gathers the advantages of regional and global information in
different layers, and thus achieves the highest mAP.
4.3. Comparison with the state-of-the-art methods
We compare the proposed SDE model with the state-of-the-
art methods including BoW (baseline) [3], PE [2], MOP [10],
PA [11], MAC [12], R-CNN [13] and Mask R-CNN [4]. All
experiments are conducted on the same environment for ASI
aurora image search. The comparison results are shown in
Table 3, and the ﬁrst ﬁve columns are mAPs for datasets with
increasing sizes, while the last column indicates the average
query time for one image. By analyzing the comparison re-
sults, we can draw the following conclusions.
Accuracy. 1) The PE outperforms the BoW because of the
introduction of polar meshing scheme. 2) Compared with the
BoW and PE, other methods leveraging CNN features achieve
higher values of mAP, demonstrating the powerful represen-
tational capacity of CNN feature. 3) In the CNN-based meth-
ods, the Mask R-CNN yields outstanding performance be-
cause of the strong network design and RoIAlign layer for
accurate location projection. 4) Remarkably, the proposed
SDE model attains the highest mAP in all datasets with dif-


## Page 6


Table 3.
Comparison with the state-of-the-art methods in
accuracy measured by mAP(%) and efﬁciency measured by
average query time (s).
Methods
8K
14K
100K
500K
1M
time
BoW (baseline)
49.01
47.65
46.65
42.32
39.09
1.98
PE
62.88
61.09
60.35
58.31
57.99
0.82
MOP
67.12
66.49
65.12
64.58
63.22
2.32
PA
68.00
67.15
66.87
65.41
64.98
1.76
MAC
65.58
64.02
61.58
59.12
58.87
1.22
R-CNN
66.54
65.42
64.85
63.52
62.12
1.25
Mask R-CNN
69.01
68.47
67.95
66.24
64.12
0.62
SDE (our)
73.16
72.10
71.90
70.42
69.85
0.59
ferent sizes. In particular, we gets satisfying mAP of 69.85%
in ASI1M, which is far ahead of other comparison methods.
Efﬁciency. Due to the introduction of region proposal
network, Mask R-CNN and the proposed SDE achieve favor-
able efﬁciency compared with other methods. The best value
of our method lies in two aspects. 1) We only process the
“saliency” regions with abundant auroral structures, thus re-
ducing the computational complexity compared with the full
domain approach. 2) The circular anchors are more effective
for aurora images, which allow us to leverage less region pro-
posals without reducing the search accuracy.
5. CONCLUSION
This paper proposes a SDE model for aurora image search.
By analyzing the imaging principle of circular ﬁsheye lens,
the SPN is presented into the Mask R-CNN framework to
generate region proposals suitable for aurora images. The lo-
cations and directions of the obtained region proposals are
along the deformation lines perpendicular to magnetic merid-
ian, which facilitates physicists for their research on solar-
terrestrial space. In practice, by ignoring the uninformative
regions and only excavating the saliency regions encompass-
ing auroral structures, the computational complexity is greatly
reduced without losing the accuracy. Additionally, to supple-
ment the local similarity measured by SPN, the global CNN
feature is extracted to evaluate the global similarity. Thus, our
method improves the search accuracy with high efﬁciency.
In the future, we will apply our method to other images
captured by unordinary cameras. Also, how to reﬁne the fea-
ture saving approach to achieve efﬁcient indexing and query-
ing is also an interesting problem.
6. REFERENCES
[1] S. Liu, B. Li, Y. Fan, Z. Quo, and A. Samal, “Facial
attractiveness computation by label distribution learning
with deep CNN and geometric features,” in ICME, 2017.
[2] X. Yang, X. Gao, and Q. Tian, “Polar embedding for
aurora image retrieval,” IEEE Trans. Image Process.,
vol. 24, no. 11, pp. 3332–3344, 2015.
[3] E. Nowak, F. Jurie, and B. Triggs, “Sampling strate-
gies for bag-of-features image classiﬁcation,” in ECCV,
2006.
[4] K. He, G. Gkioxariand P. Doll´ar, and R. Girshick,
“Mask R-CNN,” in ICCV, 2017.
[5] A. Krizhevsky, I. Sutskever, and G. Hinton, “ImageNet
classiﬁcation with deep convolutional neural networks,”
in NIPS, 2012.
[6] K. Simonyan and A. Zisserman, “Very deep convolu-
tional networks for large-scale image recognition,” in
ICLR, 2015.
[7] K. He, X. Zhang, S. Ren, and J. Sun, “Deep residual
learning for image recognition,” in CVPR, 2016.
[8] S. Xie, R. Girshick, P. Doll´ar, Z. Tu, and K. He, “Ag-
gregated residual transformations for deep neural net-
works,” in CVPR, 2017.
[9] S. Lazebnik, C. Schmid, and J. Ponce, “Beyond bags
of features: Spatial pyramid matching for recognizing
natural scene categories,” in CVPR, 2006.
[10] Y. Gong, L. Wang, R. Guo, and S. Lazebnik, “Multi-
scale orderless pooling of deep convolutional activation
features,” in ECCV, 2014.
[11] L. Zheng, S. Wang, J. Wang, and Q. Tian, “Accurate im-
age search with multi-scale contextual evidences,” Int.
J. Comput. Vis., vol. 120, no. 1, pp. 1–13, 2016.
[12] G. Tolias, R. Sicre, and H. J´egou,
“Particular object
retrieval with integral max-pooling of CNN activations,”
in ICLR, 2016.
[13] R. Girshick, J. Donahue, T. Darrell, and J. Malik, “Rich
feature hierarchies for accurate object detection and se-
mantic segmentation,” in CVPR, 2014.
[14] R. Girshick, “Fast R-CNN,” in ICCV, 2015.
[15] S. Ren, K. He, R. Girshick, and J. Sun, “Faster R-CNN:
Towards real-time object detection with region proposal
networks,” in NIPS, 2015.
[16] J. Redmon, S. Divvala, R. Girshick, and A. Farhadi,
“You only look once: Uniﬁed, real-time object detec-
tion,” in CVPR, 2016.
[17] W. Liu, D. Anguelov, D. Erhan, C. Szegedy, S. Reed,
C. Fu, and A. Berg, “SSD: Single shot multibox detec-
tor,” in ECCV, 2016.
[18] J. Redmon and A. Farhadi, “YOLO9000: better, faster,
stronger,” in CVPR, 2017.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
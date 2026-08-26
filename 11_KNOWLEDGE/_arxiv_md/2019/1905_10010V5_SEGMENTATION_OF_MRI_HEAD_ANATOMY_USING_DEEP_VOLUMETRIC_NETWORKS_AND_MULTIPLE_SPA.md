---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1905.10010v5
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1905.10010v5_Segmentation_of_MRI_head_anatomy_using_deep_volumetric_networks_and_multiple_spa

> Source: 1905.10010v5_Segmentation_of_MRI_head_anatomy_using_deep_volumetric_networks_and_multiple_spa.pdf

> Pages: 20

---


## Page 1


Segmentation of MRI head anatomy using deep volumetric
networks and multiple spatial priors
Lukas Hirsch, Yu Huang∗, and Lucas C Parra †‡
ABSTRACT
Purpose: Conventional automated segmentation of the head anatomy in MRI distinguishes diﬀerent brain and
non-brain tissues based on image intensities and prior tissue probability maps (TPM). This works well for normal
head anatomies, but fails in the presence of unexpected lesions. Deep convolutional neural networks leverage
instead spatial patterns and can learn to segment lesions, but often ignore prior probabilities.
Approach: We add three sources of prior information to a three-dimensional convolutional network, namely,
spatial priors with a TPM, morphological priors with conditional random ﬁelds, and spatial context with a wider
ﬁeld-of-view at lower resolution. We train and test these networks on 3D images of 43 stroke patients and 4
healthy individuals which have been manually segmented.
Results: We demonstrate the beneﬁts of each sources of prior information, and we show that the new
architecture, which we call Multiprior network, improves the performance of existing segmentation software,
such as SPM, FSL, and DeepMedic for abnormal anatomies. The relevance of the diﬀerent priors was compared
and the TPM was found to be most beneﬁcial. The beneﬁt of adding a TPM is generic in that it can boost
the performance of established segmentation networks such as the DeepMedic and a UNet. We also provide an
out-of-sample validation and clinical application of the approach on an additional 47 patients with disorders of
consciousness. We make the code and trained networks freely available.
Conclusions: Biomedical images follow imaging protocols that can be leveraged as prior information into
deep convolutional neural networks to improve performance. The network segmentations match human manual
corrections performed in 3D, and are comparable in performance to human segmentations obtained from scratch
in 2D for abnormal brain anatomies.
1. INTRODUCTION
Clinical and basic research require segmentation of magnetic resonance images (MRI) of human heads, including
abnormal anatomies such as tumors or lesions. In the case of brain tumors, it is helpful to measure the tumor
volume across successive scans to monitor tumor growth or the response to treatment.1 In the case of a stroke,
lesion studies can provide important insights on brain function.2 In patients with traumatic brain injury, volu-
metric analysis can provide diagnostic information such as hydrocephalus.3 When analyzing large populations
this is only possible with automated segmentation.4 Finally, transcranial electric stimulation techniques rely on
accurate head segmentations of individual subjects.5 Such a segmentation needs to capture not only the brain
and lesion but also the cerebrospinal ﬂuid, ventricles, air cavities, skull, etc.6 It is not feasible to do this manually
even on a moderate number of cases.
A number of tools have been developed to automate the task of segmenting the brain. This includes algo-
rithms that are part of neuroimaging software packages such as SPM7 and FSL.8 These algorithms traditionally
distinguish diﬀerent tissues based on the brightness of voxels. For instance, in T1-weighted MRI white mat-
ter is bright, gray matter is gray, and surrounding CSF and skull are black. Segmentation also relies on prior
information on the type of tissues that can be expected at diﬀerent location of the head, e.g., with very high
probability the surface of the head is skin. These probabilities are derived from manual segmentations of a
large number of heads and are stored as tissue probability maps (TPM).7 TPMs are available only for normal
∗Both authors contributed equally.
†This work was supported in part by NIH with Grants R01MH111896, R01NS095123, R21NS115018 and R44NS092144.
‡L. Hirsch and L. Parra are with the Department of Biomedical Engineering, City College New York, New York City, NY, 10031
USA e-mail: parra@ccny.cuny.edu. Y. Huang is with the Department of Radiology, Memorial Sloan Kettering Cancer Center, New
York City, NY, 10065 USA.
arXiv:1905.10010v5  [eess.IV]  19 May 2021


## Page 2


anatomies. Therefore, traditional algorithms that are based on these TPMs work well for subjects with normal
anatomy, but often fail in the presence of lesions. For example, in chronic stroke patients, areas that typically
contain brain (bright) are ﬁlled with cerebrospinal ﬂuid (dark in T1 images). This leads to ambiguities that
confuse the traditional algorithms and can result in errors that extend beyond the lesions. As a result, MRIs
from stroke patients require manual correction of the automated segmentations, despite eﬀorts to improve on
these traditional tools.9–11
A breakthrough was achieved recently with deep convolutional networks that can identify tissues based
on complex three-dimensional intensity patterns, instead of relying on single intensity values.
For example,
DeepMedic is a 3D convolutional network that achieves good segmentation of stroke lesions or brain tumors.12
Convolutional networks can learn to identify complex features while limiting the number of parameters to be
learned. This is accomplished by making feature extraction invariant to location. Yet, location is important in
many medical imaging tasks. To take location into account one can provide the coordinates of each voxel as
input to the network.13–18
An alternative is to provide prior probabilities explicitly as input using traditional
TPMs.13,14,19,20 This is the approach we adopt in this work.
Another important factor guiding medical segmentation is shape or morphology of a region. One approach has
been to parameterize morphology using auto-encoders.21–23
Another approach is to use conditional random ﬁelds
(CRF), which implement morphological constraints.12,24 For instance, one might a-priori disallow segmentations
where the brain touches the skin. Here we implement such morphological constraints as tissue-speciﬁc penalties
in a fully connected 3D conditional random ﬁeld.
Spatial prior information can also be derived from context in an image. For instance, when segmenting breast
tumors, it helps to know if a given voxel is part of the breast. This can be implemented by ﬁrst identifying the
breast in an image, and then providing this as input for the breast tumor segmentation.25 We follow the approach
of DeepMedic12 and VoxResNet26 where the network learns contextual information from a wider ﬁeld-of-view
(FOV) at lower resolution.
In total, we implement three spatial priors: location priors with a TPM, neighborhood priors with a CRF,
and context prior with a wider FOV, which are combined here for the ﬁrst time in a deep network architecture.
We therefore call this new deep, three-dimensional network, Multiprior. The resulting network is fully trainable,
including the prior probabilities.
Thus, the Multiprior architecture represents a convolutional network with
learnable spatial memories. These memories have a simple interpretation, and can be manually instantiated
based on prior spatial knowledge.
In this work we focus on the task of segmenting the whole head in subjects with abnormal brain anatomy,
which remains a challenging problem.
We train networks on available manual segmentations of stroke patients
and normal subjects. Based on this reference we objectively judge the beneﬁts of adding prior information and
spatial context. We then compare the results to human expert segmentations, as well as conventional and state
of the art segmentation methods. The utility of the technique is demonstrated on a separate data set of patients
with disorders of consciousness. We make the Multiprior tool freely available27 in the hope that this will spawn
further development and that it will be used in clinical research project.
2. METHODS
2.1 Detail CNN
The Detail CNN (Figure 1, black path), aims to extract detailed intensity features at full image resolution. It
takes as input a 3D image patch surrounding the target volume (green cube). The network consists of successive
convolutional layers with kernels of size 33. By limiting the convolutions to the patch boundaries the output
of each layer reduces the patch size by 2 voxels in each direction. At the same time we increase the number
of features extracted from this patch. After 8 layers, an input patch of 173 is reduced to an output of a single
voxel – this layer is said to have a ‘receptive ﬁeld’ or 173. Meanwhile, we increased the number of features to
50 per voxel. This spatial shrinking and feature expansion is a common practice for CNNs to convert spatial
information into increasingly diverse and complex features. Algebraically, this network can be described as:
yl+1
i
= f(
X
j
wl
ij ∗yl
j + bl
i) ,
(1)


## Page 3


T1  
      
TPM
33 x 30 x 1
33 x 30 x 30
33 x 30 x 30
33 x 30 x 30
33 x 50 x 30
33 x 50 x 50
33 x 50 x 50
33 x 50 x 50
Context
Detail
Spatial Priors
 
13  x 150 x 106
13  x 200 x 150
13  x 7 x 200
Downsample  /3 
Argmax
Upsample x 3  
  T1 
CRF
...
Figure 1. Multiprior network structure. The Detail network (black path) consists of a 3D convolutional neural network
(CNN) with 8 layers. During training, this network takes as input a patch of 253 voxels around a target patch of 93 to be
classiﬁed (green cube). The size of the convolutional kernels mapping between layer is indicated by numbers to the right.
For instance, 33x50x30 indicates a 3D convolution kernel of size 33 transforming 30 features to 50 features. The “Context”
network (red path) is identical in structure to the “Detail” network, except that it processes a downsampled version of a
larger ﬁeld-of-view of 573 voxels during training. It includes an upsampling layer at the end in order to merge features
at the same scale as the Detail network. Prior probabilities for the target patch are extracted from a tissue probability
map (TPM) and added as input to the ﬁnal classiﬁcation (Blue arrow). The “Classiﬁcation” network (purple) takes the
concatenated output of all three pathways as input and classiﬁes the target patch with three fully-connected layers and
no additional spatial mixing (kernel of size 13). After the entire image has been segmented, a 3D conditional random
ﬁeld (CRF) processes the resulting output segmentation while taking the original input image into account (green arrow).
Arrows indicate copying.
where ∗represents a 3D convolution, yl
i represents the activity in a 3D patch (tensor) for feature i in layer l, wl
ij
is a 3D convolution kernel connecting features j from layer l to feature i in layer l + 1, bl
i is a bias term, and f()
is a LeakyReLU as element-wise non-linearity. For the ﬁrst layer, yl
j represents the input to the network. For
the last layer yl
j represents the output (here l = 8). Learnable parameters are the convolution kernels wl
ij and
bias terms bl
i. These are adjusted using gradients of the cost function (see below). The size of the kernels wl
ij is
indicated as numbers between each layer in Figure 1.
2.2 Context CNN
Following,12 we also include a CNN that operates in parallel on a wider FOV. The increased FOV allows the
segmentation to rely on the surrounding context. For instance, in T1-weighted images of the head, areas with
uniform black patches are not background, but instead ventricles if they are in the interior of the skull. This
wider FOV is ﬁrst downsampled (by a factor 3). The network itself has then the identical structure to the Detail
CNN. The output is then upsampled (by the same factor of 3). The size of the receptive ﬁeld for this network
including the downsampling is 513.


## Page 4


2.3 Classiﬁcation network
Segmentation implies classifying each voxel into one of several possible tissue types. Here this is skin, skull,
CSF, white matter, gray matter, air cavity, and background air - seven classes in total. The output of the
preceding paths is concatenated and serves as the input to a ﬁnal Classiﬁcation network (Figure 1, purple). The
Classiﬁcation network has three fully-connected layers with no spatial mixing. Algebraically the classiﬁcation
network can be described as:
yl+1
i
= f(
X
j
wl
ijyl
j + bl
i) ,
(2)
which is the same as the network deﬁned in Equation (1) except we are no longer implementing convolutions on
3D patches, so wl
ij is no longer a 3D tensor. The index l goes now from 9 (the output of the previous network)
to 11 (the classiﬁcation output). We use again LeakyReLU as element-wise non-linearity f(), except for the last
layer, which uses a softmax function to encode the class probability. This output is used to compute the cost
function during training, namely, the generalized Dice score in Equation (3) below. The ﬁnal segmentation is
obtained as the argmax operation of these seven tissue probabilities at each voxel.
2.4 Tissue probability Map (TPM)
Spatial priors are included by providing the TPM values corresponding to the target voxel location (Figure 1,
blue path). This requires registering the TPM to the individual MRI to ﬁnd the corresponding locations. This
was done with the warped coregistration of the segmentation routine in SPM8.7 We used a TPM that covers
the full head down to the neck28 as shown in Figure 2A. These prior probability values are given as input to the
Classiﬁcation network for each voxel as a vector with one values per tissue class. These values are concatenated
to the output of the Detail network and Context networks.
Figure 2. Location and neighborhood priors: (A) Tissue probability map (TPM) representing prior probabilities for ﬁnding
each of 6 tissues at various locations: Gray Matter (1), White Matter (2), CSF (3), Bone (4), Skin (5) and background
(6). (B) Penalty terms for conditional random ﬁeld (CRF). Weights on this matrix represents the prior belief we have
on observing a neighboring tissues. High penalties are speciﬁed for tissue pairs that are not supposed to be next to one
another (impossible boundaries), intermediate penalties for tissues that are expected to be adjacent (possible boundaries),
and low penalty for neighboring voxels to be in the same tissue class (expected continuity). Note that the TPM available
to us has 6 tissue types, while the CRF has 7, as we expect the classiﬁer to distinguish between internal and external air,
i.e. air cavities vs exterior background.
2.5 Fully connected CRF
Topological prior expectations such as connectivity of tissues are useful for producing realistic segmentation
maps. A standard approach to implementing such priors is to use Conditional Random Fields.12,24,29,30
A
CRF can assign an additive penalty to certain combination of segmentation labels. In brain images we expected


## Page 5


a-priori that tissues share a boundary with other tissues while others may not touch, e.g. white matter and
gray matte or skin and bone are commonly found together, while we never expect to ﬁnd cerebrospinal ﬂuid
next to air, or brain tissue next to skin.
We express these prior probabilities of label conﬁguration with a
penalty matrix that is speciﬁc to each tissue pair (Figure 2B). This is more general than the conventional Potts
model commonly used with CRFs, and is similar to what we used previously for head segmentation.31 The
Potts model does not distinguish between class labels, and is typically used only for smoothing segmentation
boundaries and removing small disconnected regions. By fully exploiting the ﬂexibility of the penalty matrix we
implement tissue-speciﬁc constraints. Here we use a fully-connected CRF, which allows segmentations to exert an
inﬂuence on distant voxels.32 Additionally, we extend to 3D the existing 2D implementations of fully-connected
CRF.32 The algorithm is initialized with the softmax output segmentation of the classiﬁer and iterates to force
segmentation labels to comply with the neighborhood constraints, while taking the single-voxel intensity of the
original image into account. We iterate the CRF for 5 cycles.
2.6 UNet
We also implemented a volumetric version of the UNet,33 that takes as input image patches of size 323 voxels,
and learns volumetric features through 3 downsampling and subsequently 3 upsampling convolution blocks with
residual connections.
Each convolution block consists of two consecutive convolutional layers with ﬁlters of
size 33 and one downsampling or upsampling layer respectively. The TPM module was added before the last
classiﬁcation layer of the network, by simply concatenating the feature maps with the probabilities per tissue.
2.7 Cost function
Training was set to reduce the Generalized Dice Loss between the predicted segmentation by the network and the
ground-truth provided by the manual segmentations.34,35 The Generalized Dice Loss extends the conventional
binary Dice Loss to the case of multiple target classes, and is deﬁned here as:
D = 1 −1
C
C
X
i=1
2yi · ti
yi · yi + ti · ti
,
(3)
where yi is the output of the classiﬁcation network (at the last layer, l = 11) and ti is the desired output
classiﬁcation (truth label in the training data with one-hot encoding), therefore i now represents the class labels.
The inner product · sums over all elements of the 3D volume. C is the total number of classes (C = 7 in this
case). This loss function (3) is equal to zero when the network output matches the target classes in all voxels,
and equal to one when no class probability is the same as the target in any location. The generalized Dice loss
intends to account for class imbalance often observed in image segmentations.35 Our deﬁnition diﬀers slightly
in that the denominator takes the L2 norm of the class probabilities. This emphasizes large probability values
and discounts small probabilities present in the vast majority of voxels, which tend to dominate in an L1 norm
as used by.35 We also omit class-speciﬁc weights here as they were not necessary for our data. When we report
performance we give only the second term (without the minus sign), or report individual terms of the sum when
reporting the results for each class, which is the conventional binary Dice score for each class.
2.8 Training and testing data
The training data consists of T1-weighted MRI scans from 4 healthy subjects and 43 individuals who suﬀered a
stroke. The strokes occurred at least 6 month prior to the MRI scan, at which point the lesion is largely replaced
by CSF. MRI scans from normal subjects were obtained on a 3T Siemens Trio scanner (Erlangen, Germany)
(Huang et al. 2013). The stroke scans were collected at Georgetown University and the University of North
Carolina, Chapel Hill, also on a 3T Siemens Trio scanner. The trained network was also applied to MRI images
of 47 patients with disorders of consciousness collected at the Piti´e-Salpˆetri`ere University Hospital in Paris, on
a 3T General Electric Signa system (Milwaukee, WI).36 Image resolution was 1 mm in all three axis.
Target labels for training and testing consist of semi-manual segmentations. Speciﬁcally, the 43 stroke heads
are ﬁrst segmented automatically28,37 and then manually corrected for errors in particular around the stroke


## Page 6


lesions and boundaries between CSF, gray matter and skull, resulting in 7 classes (background, air cavities,
skin, bone, cerebrospinal ﬂuid, white matter and gray matter). The T1 images from the 4 healthy subjects
were segmented following the same procedure and have been previously published.28 We used the graphic user
interface of Simpleware ScanIP (Synopsys, Mountain View, CA) for manually correcting the segmentation. We
obtained an additional independent manual correction for six of these stroke heads, starting from the same SPM8
results. Manual corrections in 3D were performed by technical staﬀat Soterix Medical Inc. as part of a clinical
research project. Manual segmentations in 2D (see Section 2.9) were performed in Simpleware from scratch by
research staﬀat CCNY. All segmenters were trained on several images by author YH, based on38 and were
supervised by YH during segmenting.
During network training, 4 heads were kept out for validation purposes, measuring generalization performance
during training epochs and used to deﬁne the stopping point, i.e., the epoch with maximum Dice score on the
validation set. This procedure was used for training all convolutional neural networks (Multiprior, DeepMedic
and U-Net variants).
2.9 Evaluation on an independent test set and reader study
To evaluate the performance of the Multiprior network, we compared the segmentation results with traditional
and state-of-the-art brain segmentation methods: FSL, SPM, and DeepMedic. We manually segmented 2D slices
on an independent test set of 10 stroke heads and 10 patients with disorders of consciousness. For each head
one slice was selected to include all tissue types and the major abnormal anatomy.
To assess reliability of the
human segmenters we obtained in addition a second independent human segmentation on 9 of these 10 stroke
heads.
2.10 Statistics
Performance of a model is evaluated on Dice scores of each scan, averaged over classes unless otherwise noted.
To evaluate statistical signiﬁcance between results of two models, we compare the distribution of the Dice scores
across scans. Whenever the scan samples are equal we use the Wilcoxon rank-sum test. For unpaired data
we use the Mann-Whitney U test. For multiple group comparison with paired data we use the non-parametric
equivalent of repeated-measurements ANOVA, namely the Friedman chi-square test. Bonferroni correction was
used to account for multiple comparisons when doing pairwise comparison of multiple models. A paired t-test
was performed to compare Dice scores for the disagreement between machine and segmenters and disagreement
between segmenters.
3. RESULTS
3.1 Prior probabilities, morphological priors and spatial context all improve
performance
We designed a three-dimensional convolutional neural network for segmentation with the architecture deﬁned
in Figure 1. In its simplest form the network extracts detailed spatial features in a small volume around the
voxel to be segmented (Figure 1, Detail). We refer to this as the Detail CNN. The features extracted by this
network are then classiﬁed by the Classiﬁcation network into one of seven tissue types. We will consider three
sources of prior information to be added to this classiﬁcation network: image context by adding a low-resolution
wide ﬁeld-of-view input (Context, Figure 1); spatial prior information through a tissue probability map (TPM,
Figure 1 & 2); morphological constraints implemented with conditional random ﬁelds (CRF, Figure 1 & 2).
Network parameters are trained on semi-manual segmentations from 43 stroke patients with chronic lesions
and 4 healthy subjects with normal anatomy (data collected at diﬀerent clinical sites; see Methods). These heads
have been segmented using SPM8 and manually corrected by expert segmenters. Dice scores between the SPM8
results and the corrected segmentations give a sense of extent of the corrections (Figure 3A). They are minor in
some instances, but substantial in others. Typically this manual correction process takes 16-32 hours of work for
the entire volume (segmenting entire volumes by hand from scratch is prohibitive). Examples of the corrections
are shown in Figure 3B. These focused on errors in the stroke lesions and gaps in thin structures that border on


## Page 7


A
B
Figure 3. Semi-manual segmentation of T1-weighted MRI images of the head. (A) Dice score comparing SPM8 automated
segmentation with segmentation after manual correction by an expert human segmenter. Each point represents the average
Dice score across all 7 tissues (gray matter, white matter, CSF, bone, skin, air and background) in each subject. Dice
scores here can be seen as a performance metric for SPM8, or alternatively, as an indication of the level of manual eﬀort of
correcting for each volume. Generally only minor corrections were performed for the healthy subjects (N=4) as compared
to some of the stroke patients (N= 43). Colored lines indicate 6 patients shown in more detail in panel B. (B) Corrections
of expert human segmenters (red) overlaid on T1-weighted MRI for 6 exemplary stroke cases.
the resolution limit of 1mm in this data, e.g. skull, CSF, gray matter; all of which represent small areas relative
to the whole head. The corrections are small on healthy subjects where SPM8 performs well, resulting in an
average higher Dice score than stroke heads. The manually corrected segmentations were used here to train the
network by minimizing the Generalize Dice Loss (Eq. 3) on training data (N=35 heads), and to evaluate network
performance using the Dice Score on test data (N=12 head).We repeat this on diﬀerent train/test partitions of
the data to obtain test set result for all 47 heads.
Test set performance is shown in Figure 4. To test for the beneﬁts of each possible source of prior information
we compare each addition individually to the results with the Detail network alone: Detail vs Detail+CRF (p=2.9
x 10−9, N=47, here and in the following all paired tests are rank-sum Wilcoxon test); Detail vs Detail+TPM
(p=2.4 x 10−9); Detail vs Detail+Context (p=5.5 x 10−9). Evidently all sources of prior information signiﬁcantly
improve segmentation performance, with the largest numerical increase with the addition of the TPM (Figure 4).
Note that the Detail + Context network (denoted as +Context in 4) is essentially a previous approach known as
the DeepMedic network.12 When combining all three enhancements (Detail + Context + TPM, + CRF), referred
to here as the Multiprior network, we obtain the strongest performance. Notably, when removing the TPM from
the Multiprior network performance drop signiﬁcantly (p=2 x 10−9, N=47), as well as when removing the CRF
(p=2 x 10−7), but not when removing Context (p=0.46). This analysis is the equivalent of an “ablation” study.
To gain a sense of the types of errors and corrections of each network we show sagittal cross-sections for 3
stroke cases (Figure 5). In the ﬁrst example (Figure 5A) we see that the Detail+Context network err in labeling
the CSF that has ﬁlled the stroke lesion as background air. Both are dark in the T1 weighted image, but the
location inside the skull strictly prohibits this erroneous label, something that is readily corrected once adding
the TPM. The second example (Figure 5B) shows erroneous gray matter labels outside the skull or brain stem
(in the neck), which again is readily corrected once the TPM is added. In the third example (Figure 5C) we show
the overall beneﬁts of the Multprior network as compared to the traditional segmentation with SPM8. Evidently
SPM8 mistakenly labeled much of the dark CSF in the stroke lesion as white matter.
Since the addition of the TPM leads to the most signiﬁcant improvement we analyze this result in more
detail (Figure 6). All tissue types improve substantially in performance (p < 10−8; Figure 6A), only for air
in sinus cavities and background the results are somewhat mixed but still statistically signiﬁcant (p < 0.0003).
When inspecting the changes in the confusion matrix (Figure 6B), we see that the most signiﬁcant corrections
are in correctly distinguishing between white and gray matter, between air cavities and bone (both black in


## Page 8


Figure 4. Additions of prior information or context improve segmentation performance. Here we are showing the Dice Score
average over all tissue types (second term of Eq. 3) for each test subject obtained with 4-fold cross validation on 43 stroke
and 4 healthy individuals (blue and orange lines respectively, and black line for the mean value). Dice score are measured
between semi-manual and automated segmentations obtained with diﬀerent network architectures. All networks contain
the Detail CNN. Additions are a Conditional Random Field (+CRF), a Context CNN with wider ﬁeld of view (+Ctxt),
and a Tissue Probability Maps (+TPM). Multiprior (MP) is the combination of all networks (Detail+Ctxt+TPM+CRF).
Stars indicate a statistically signiﬁcant diﬀerence in Dice score between pairs of network architectures (* : p < 0.05, ** :
p < 10−7, alpha level corrected for multiple comparison with Bonferroni correction and C=28 multiple comparisons).
T1-weighted images), and generally correcting erroneous “skin” labels (a catch-all label for other soft-tissues)
which is readily confused without prior knowledge.
Adding a TPM should confer a generic beneﬁt to other convolutional networks. To test this, we adapted the
popular UNet structure33 for the current task and added at the last classiﬁcation layer an input from a TPM
(see Methods). Adding a TPM to the UNet shows a signiﬁcant increment in the performance on the stroke
dataset (Figure 6C; p = 3 x 10−9, Wilcoxon ranksum test). For reference we also show the summary for the
whole head for the DeepMedic structure with and without an added TPM. As we saw previously this also results
in a signiﬁcant improvement (p = 7 x 10−9, Wilcoxon ranksum test). Both networks were trained with identical
data and show comparable performance once the TPM is added.
3.2 Multiprior network matches human segmentation performance
Segmenting MRI images is a subjective process even for expert human segmenters39,40 This leaves us without
an absolute ground truth to evaluate machine performance. It is therefore customary to take the agreement
between independent manual segmentations as a point of reference.
For a full 3D evaluation we obtained an additional independent manual correction for six of the stroke heads,
starting from the same automated SPM8 results. We focus the evaluations on the areas that have been corrected
by at least one of the two human segmenters (e.g. Figure 3). Dice scores between the two human segmenters
in these areas are relatively low (Figure 7A) and increase substantially between the human and the machine
segmentation using the Multiprior network (p=0.011, Friedman-chi square, F=9.0, N=6). This suggests that
wherever the human decided to make a correction, the machine provided a similar segmentation, but the two
humans did not make the same set of corrections. The result is similar when evaluating Dice score for individual
tissues (Figure 7B). An example of this for CSF is shown in Figure 7C.
The previous evaluation focuses on correcting an automated segmentation (from SPM8). To evaluate perfor-
mance without the bias of the automated segmentation we also obtained fully-manual segmentations. As this is
a laborious process, and because manual segmentations are performed naturally one slice at a time, we restricted
this evaluation to 2D segmentations. Two individual manual segmentations were obtained for axial slices of 9


## Page 9


Manual                      T1 MRI                        SPM8                        Multiprior 
                                                                                                
         Manual                    T1 MRI                  Detail + Context      Detail + Context + TPM      
      
A
B
C
    Manual                     T1 MRI                 Detail + Context      Detail + Context + TPM
  
Figure 5. Examples of common segmentation errors for three stroke subjects and corrections by the Multiprior network.
Each row corresponds to one subject. The manual segmentation is on the ﬁrst column, followed by the T1 weighted MRI
that is used as an input for the network, next are segmentations from the Detail + Context network (A,B) and SPM8
(C) compared to the segmentation from the Multiprior. Each color represents one of each of seven tissue-classes used
for classiﬁcation: Black = background; brown = skin; yellow = bone/skull; green = air/sinus cavities; light blue = CSF;
white = white matter and gray = gray matter. Notice the large CSF ﬁlled lesion in panel A.
stroke heads that were not part of the training set. These were segmented by research staﬀat CCNY and were
reviewed by authors YH and LH. Additionally, for these heads we had the semi-automated segmentations that
were left out from the training set. Given that there is no absolute ground truth, we compare all segmentations
to one another by computing the Dice score between all pairs including the Multiprior segmentations. We com-
pare the Dice score of these comparisons for each tissue (Figure 8A), and for all tissues combined (Figure 8B).
Overall, the disagreement between machine and segmenters is comparable to that of the disagreement between
segmenters (see Figure 8C) (mean of Dice H1 vs M and H2 vs M = 0.763, Dice H1 vs H2 = 0.762, paired t-test:
t(8)=-0.08, p=0.94). Evidently, even the human segmenters disagree in their judgement (see Figure 1 in the
Supplement) with H2 being closer to the semi-automated and automated methods as compared to H1 (Fig. 8B).
Discrepancies between the manual segmentations are mainly due to ambiguities around lesions, where it is hard
to decide where CSF ends and where gray matter starts, or how to characterize “gray” tissue in T1 images for
areas where one would expect white-matter and which are likely pathological. Other discrepancies are on how to
characterize bright cancellous bone (fatty soft-tissue is equally bright) and where the exact boundary is between
sinus air cavities and cortical bone, or cortical bone and CSF, which are equally dark in T1 images.
3.3 Utility to a diﬀerent clinical population of patients with disorders of consciousness
To demonstrate the utility of the Multiprior network in practical use, we tested it on a diﬀerent clinical population.
Speciﬁcally, we used the Multiprior network trained as before (stroke and healthy) to segment a new set of MRI
images from patients with disorders of consciousness collected at a diﬀerent clinical site. This included patients


## Page 10


A
C
B
**
**
D
Human Correction           Multiprior           Difference  
Figure 6. Beneﬁts of adding a Tissue Probability Map (TPM). (A) Dice scores for each tissue class are shown for all 47
individuals for the Multiprior network including a TPM (+) or excluding the TPM (-). Black lines correspond to mean
across all heads. Scans from healthy subjects are in orange and in blue for stroke cases. (B) Change in the confusion
matrix when adding a TPM. Blue, positive values on the diagonal indicate more voxels correctly classiﬁed when the TPM
is added; Red, negative values on the oﬀ-diagonal indicates fewer voxels that are incorrectly classiﬁed with the addition
of the TPM. By deﬁnition, each row of this diﬀerence matrix must sum to zero, as corrections on the oﬀ-diagonal equate
the improvements on the diagonal. (Bkg: background; Air: air cavities; GM: gray matter; WM: white matter; CSF:
cerebrospinal ﬂuid.) (C) Beneﬁt of adding a TPM for DeepMedic and UNet for the same stroke cases using Dice score
for the entire head. DeepMedic is equivalent to Detail CNN + Context (** : p < 10−7). (D) Diﬀerence between manual
segmentation and automatic segmentation with the MultiPrior network. The errors are mainly along boundaries, which
can be extensive due to cortical folding, as well as the boundary of the stroke lesion with ambiguous intensities.
in vegetative state (VS, N=20) and minimally conscious state (MCS, N=27).36 MCS patients show intermittent
signs of consciousness and have higher chances of improvement. In contrast, VS patients exhibit no signs of
consciousness and usually have a worse prognosis. A clinical diagnosis distinguishing between these two conditions
is not trivial and some anatomical features have been shown to correlate with the patient’s diagnosis as VS or
MCS.41,42 The segmentation task is challenging because these patients have severe anatomical abnormalities
(Figure 9A). We segmented these heads with the trained Multiprior network, quantiﬁed the volume of diﬀerent
tissues and compare that to a clinical diagnosis of their level of consciousness.
We ﬁnd smaller volume of gray matter and larger volume of cerebrospinal ﬂuid in vegetative state patients as
compared to minimally conscious patients (Figure 9B, N=47, p=2x10−3 and p=2x10−2, Mann-Whitney U test
for unpaired data). Both these metrics have been previously linked to these conditions.41,42 In contrast, white
matter volume, not an established biomarker, showed no signiﬁcant diﬀerence (Figure 9B, p=0.26, N=47). This
demonstrates the utility of this automated segmentation approach in clinical applications.
3.4 Multiprior netwoork outperforms existing segmentation approaches on abnormal
brain anatomies
Finally, we wanted to compare the performance of the Multiprior model with existing automated segmenta-


## Page 11


C
Figure 7. Multiprior network and human manual corrections in 3D volumes. (A) Dice scores comparing two humans
segmenters to one another (H1, H2) and to the Multiprior network. For this test, six stroke heads (colored lines) were
manually corrected independently by the two human segmenters.
The network was trained on a diﬀerent set of 41
segmentations. (B) Dice scores between H1 and H2 or Multiprior network (M) now separated by tissue class. (C) Two
example scans (ﬁrst column), uncorrected segmentation from SPM8 (second column), and corrections of segmentation
shown with overlaps between Humans 1 and 2 (third column), Human 1 and Multiprior (fourth column) and Human 2
and Multiprior (ﬁfth column). In the example of the ﬁrst row the human segmenters chose to make corrections in diﬀerent
locations. In the second row corrections overlap (yellow) but were more extensive for H1. In both instances the machine
segmentation overlaps more extensively with each of the human corrections as compared to the two humans (more yellow).
tion methods, including traditional approaches (SPM and FSL), as well as newer deep convolutional networks
(DeepMedic and U-Net). Given the present focus on lesioned anatomies we evaluated this on new manually
segmented 2D slices for the stroke dataset (N=10) and the disorder of consciousness patients (N=10). Note that
this also provided an out-of-sample evaluation, as the Multiprior network was trained on the stroke patients
but tested here also on disorder of consciousness patients. Figure 10 shows the result sorted by overall perfor-
mance. In the average over all tissues, Multiprior numerically outperforms the UNet, the DeepMedic followed
by SPM and FSL (with mean Dice 0.73, 0.73, 0.72, 0.68, 0.54, respectively for the stroke dataset, and 0.73,
0.66, 0.63, 0.63, 0.61, respectively for the disorder of consciousness (DOC) dataset). The Multiprior network
has similar performance to the UNet on the stroke data, and performs better numerically than the UNet on
the DOC patients. On healthy tissues with normal anatomy all these tools perform well (on GM, WM, Bone,
Skin). Lesions in this dataset are present as CSF-ﬁlled regions, which is where these tools fail to recognize the
abnormality. Performance on CSF in stroke is the single instance where the DeepMedic numerically outperforms
the Multiprior.
4. DISCUSSION
The main contribution of this work is a network architecture that can segment the head anatomy with human-level
performance speciﬁcally in the presence of brain lesions. When tested on normal head anatomy of the proposed
architecture, it is no worse than current state-of-the-art automatic segmentation software, and outperforms these
methods in the presence of abnormal anatomy and lesions, including an out-of-sample dataset. We provided the


## Page 12


Dice score
Segmentation
Reference
A
B
C
Figure 8. Multiprior network and human manual segmentation in 2D slices. (A) Dice score comparison for 9 stroke images
that were not part of the training set, for ﬁve tissues (gray matter -GM-, white matter -WM-, cerebrospinal ﬂuid -CSF-,
bone and skin). Comparison is made between fully-manual segmentation (H1, H2) and MultiPrior (M) against the human
segmentation (pooled average between H1 vs M and H2 vs M). (B) Dice score comparing fully-manual segmentations (H1,
H2), manual correction of automated segmentation (HC) and Multiprior segmentation (M). The Dice score is averaged
over all tissues and heads for all possible pairwise comparisons. (C) Comparison of human fully-manual segmentations
with Multiprior segmentation (for human-machine comparison Dice score are pooled over H1 and H2).
ﬁrst detailed analysis of the relative merits of each type of spatial priors equivalent to an “ablation” study. In
particular, we have shown that adding a prior probability map can beneﬁt several existing network architectures.
The same pre-trained network performed well on two diﬀerent clinical populations, and we therefore make it
freely available to facilitate broader testing.
Convolutional neural networks are by design shift invariant. They are thus able to recognize objects regardless
of the position in an image. This has made these networks a powerful tool in parsing of images, such as those
found in the Imagenet database,43 where objects have no intrinsic correlation with their absolute position. This
is however not the case in biomedical images, where anatomical structures are in a well-deﬁned location relative
to other tissues and organs. Prior knowledge of location is probably just as important as image intensity in
clinical diagnosis.
In T1-weighted MRIs, the CSF ﬁlled area in the brain created by a chronic stroke, appears black with a
similar intensity to that of background and air-ﬁlled sinus cavities. Despite similar intensity, a human observer
can readily discern the diﬀerence based on locations: black areas inside the head are either sinus cavities or
CSF-ﬁlled lesions of the brain. Therefore, prior probability maps can easily resolve such conﬂicts. Indeed, we
ﬁnd that the largest gains can be achieved with a tissue probability map. This beneﬁt of TPM was not speciﬁc
to the network architecture we focused on here, which was based on the DeepMedic architecture. We found a
comparable gain in performance when adding a TPM to a UNet segmentation architecture. A convolutional
network that does not take prior information into account should in theory still be capable of correcting these
mistakes in anatomy, by enlarging the ﬁeld-of-view to recognize relevant contextual information for each region.
Therefore, learning this context information also improved segmentation performance here.
The performance of the ﬁnal models is in the range of 75-92% in Dice score (Figure 4). Most of the residual
errors are edge/boundary mistakes, which dominate in brain images, due to cortical folding (Figure 6D), as well
as errors in stroke lesions with ambiguous intensities and abnormal anatomy. Labeling the highly folded surface
of the cortex and gray-matter is a laborious and subjective task, even for human segmenters, given that biological
boundaries are seldom clear. For instance, in T1-weighted images bone and CSF are both dark and the boundary
between the two must be surmised, rather than derived from the image intensities. An important criterion in this
context is smoothness and continuity of these thin structures. Indeed, the addition of the conditional random
ﬁeld to the network serves this purpose and improved performance whenever it was added to the network.
Aside of being subjective, manual segmentation is also very labor intensive. Segmenting an entire head volume
from scratch takes typically two to four weeks of labor, in particular if one wants to avoid typical continuity
errors between slices as the manual segmentation is done one slice at a time. The process we used here of only


## Page 13


Figure 9. Segmentation of head and brain for patient in minimally conscious state. (A) Segmentation is based on T1-
weighted MRI. The Multiprior network correctly identiﬁes CSF (light blue) in the enlarged ventricles. SPM8 mistakes
some of this as gray matter (gray) as it expects smaller ventricles typical for normal anatomy. As a consequence this
also aﬀects recognition of white and gray matter elsewhere. (B) Anatomical diﬀerences between vegetative and minimally
conscious state. Subjects in vegetative state (VS, N=20) diﬀer from subjects in a minimally conscious state (MCS, N=27)
on relative volume of gray matter tissue, cerebrospinal ﬂuid (CSF), but not white matter volume ( * : p< 0.05).
*
*
*
*
*
*
*
*
*
Figure 10. Comparison of multiple segmentation methods against 2D manual segmentations. (Left) stroke patients (N=10)
(Right) disorder of consciousness patients (N=10). Methods are compared on the ﬁve diﬀerent tissue classes (gray matter,
GM, white matter, WM, cerebrospinal ﬂuid, CSF, bone and skin).
Signiﬁcant diﬀerences between Dice scores across
methods is indicated with * (p < 0.05, repeated measurements ANOVA)


## Page 14


correcting automated segmentations takes about two to four days of work. It is therefore not surprising that two
human segmenters chose to make corrections in diﬀerent locations of the automated segmentations. The main
advantage of the Multiprior network is that it has no such penalty for “eﬀort” and segments the entire head
from scratch. It matches the corrections of both human segmenters better than they match one another, as they
often choose to make corrections in diﬀerent locations. In this sense, the Multiprior improves on the corrections
of human segmenters. When manual segmentations are performed from scratch on 2D slices the performance of
the Multiprior network is equivalent to that of the human. The two human raters deviate in their segmentations
from one another as much as they deviate from the segmentation of the network (Figure 8). However, a caveat
of this study is that we only performed comparison on 2D slices instead of fully 3D segmentations, which are
time-prohibitive.
Comparison of common segmentation tools with Multiprior network was done also on 2D manual segmenta-
tions of two diﬀerent patients populations. On these data normal tissue is segmented similarly by all methods,
while lesions containing CSF is only recognized by our deep convolutional networks. Both DeepMedic and the
Multiprior surpass SPM and FSL (Figure 10).
In this work we have extended the conditional random ﬁeld32 to work over four dimensions (intensity and
three spatial coordinates). We also added multiclass conditional probabilities, which are particularly well suited
to implement anatomical constraints. The CRF was added as a post-processing step. Recent work recasts the
CRF computations into a recurrent convolutional neural network.44 While we have not implemented this here,
a ﬁxed number of iterations of this recurrence can be readily added as an additional layer to the Multiprior
network. In this way the fully-integrated network could be trained coupling the learning of the parameters of the
fully-connected CRF with the learning of the parameters of the deep convolutional network. This would allow to
train the spatial priors (unary potentials in the CRF) as well as the neighborhood priors (pairwise potentials),
along with the features extracted.
We note that the biggest improvement was achieved by adding the location priors in the form of a TPM
(Figure 4).
In this dataset, the deep network improved most with the tissue-speciﬁc location priors. It is
possible that on a diﬀerent dataset, a TPM is less beneﬁcial than the other two sources of prior information, but
this remains to be tested in future work.
One caveat to the proposed approach is that the tissue probability map has to be spatially aligned to
the images before segmentation. In contrast, neural-network methods typically do not require this initial pre-
processing and can operate in a stand-alone fashion.
We have used SPM8 for this initial co-registration to
warp the TPM to the target image, but we could have used other powerful warped registration methods such
as ANTS.45 Future work may incorporate newer network methods that implement registration as part of the
network architecture.46 We note that incorporating the CRF and co-registration into the network itself adds
signiﬁcant algorithmic complexity. Avoiding this added complexity was a deliberate choice given that they can
be readily implemented as pre- and post-processing steps.
In general, as the amount of training data increases, there is decreased need to implement prior informa-
tion. We currently speciﬁed prior information “by hand”, namely, neighborhood priors were selected based on
anatomical knowledge, and location priors were taken from existing tissue probability maps. However, the net-
work architecture we have developed here can in principle also update these priors based on additional training
data. As such, one can conceive of the Multiprior architecture as having dedicated storage modules to memorize
prior information in a concise and interpretable code. As long as datasets are limited in size, explicit priors will
aid segmentation performance. And even if data volumes grow in time, good initial priors will remain useful
starting points to accelerate training.
All source code and pre-trained networks are available at github.com/lkshrsch/MultiPrior_Brain.
Disclosures
No conﬂicts of interest, ﬁnancial or otherwise, are declared by the authors. The present study was exempt from
IRB review at the City College of New York as it only used preexisting de-identiﬁed data.


## Page 15


Acknowledgment
The authors would like to thank Chris Thomas at Soterix Medical Inc. for manually segmenting most of the
41 stroke heads and providing the data. We would also like to thank Peter Turkeltaub, Adam Woods, and
Abhisheck Datta for collecting and sharing the stroke MRI data. Similarly we would like to thank Jacobo Sitt
and Bertrand Herman to sharing the MRI data from the minimally conscious patients. We also want to thank
Noor-E-Jannat Anindita and Humna Khan from the City College of New York for manually segmenting 2D slices
of 20 heads.
REFERENCES
1. S. Bauer, R. Wiest, L.-P. Nolte, and M. Reyes, “A survey of MRI-based medical image analysis for brain
tumor studies,” Physics in Medicine and Biology, vol. 58, no. 13, pp. R97–R129, Jul. 2013.
2. L. D. Alexander, S. E. Black, F. Gao, G. Szilagyi, C. J. Danells, and W. E. McIlroy, “Correlating lesion size
and location to deﬁcits after ischemic stroke: the inﬂuence of accounting for altered peri-necrotic tissue and
incidental silent infarcts,” Behavioral and Brain Functions, vol. 6, no. 1, p. 6, Jan. 2010.
3. N. Miskin, H. Patel, A. M. Franceschi, B. Ades-Aron, A. Le, B. E. Damadian et al., “Diagnosis of Normal-
Pressure Hydrocephalus: Use of Traditional Measures in the Era of Volumetric MR Imaging,” Radiology,
vol. 285, no. 1, pp. 197–205, 2017.
4. X. Llado, A. Oliver, M. Cabezas, J. Freixenet, J. C. Vilanova, A. Quiles et al., “Segmentation of multiple
sclerosis lesions in brain MRI: A review of automated approaches,” Information Sciences, vol. 186, no. 1,
pp. 164–185, Mar. 2012.
5. J. P. Dmochowski, A. Datta, Y. Huang, J. D. Richardson, M. Bikson, J. Fridriksson et al., “Targeted
transcranial direct current stimulation for rehabilitation after stroke,” NeuroImage, vol. 75, pp. 12–19, Jul.
2013.
6. A. Datta, J. M. Baker, M. Bikson, and J. Fridriksson, “Individualized model predicts brain current ﬂow
during transcranial direct-current stimulation treatment in responsive stroke patient,” Brain Stimulation,
vol. 4, no. 3, pp. 169–174, Jul. 2011.
7. J. Ashburner and K. J. Friston, “Uniﬁed segmentation,” NeuroImage, vol. 26, no. 3, pp. 839–851, Jul. 2005.
8. S. M. Smith, M. Jenkinson, M. W. Woolrich, C. F. Beckmann, T. E. J. Behrens, H. Johansen-Berg et al.,
“Advances in functional and structural MR image analysis and implementation as FSL,” NeuroImage,
vol. 23, pp. S208–S219, Jan. 2004.
9. D. Pustina, H. B. Coslett, P. E. Turkeltaub, N. Tustison, M. F. Schwartz, and B. Avants, “Automated
segmentation of chronic stroke lesions using LINDA: Lesion identiﬁcation with neighborhood data analysis,”
Human Brain Mapping, vol. 37, no. 4, pp. 1405–1421, 2016.
10. R. McKinley, L. H¨ani, J. Gralla, M. El-Koussy, S. Bauer, M. Arnold et al., “Fully automated stroke tissue
estimation using random forest classiﬁers (FASTER),” Journal of Cerebral Blood Flow & Metabolism, vol. 37,
no. 8, pp. 2728–2741, Aug. 2017.
11. M. L. Seghier, A. Ramlackhansingh, J. Crinion, A. P. Leﬀ, and C. J. Price, “Lesion identiﬁcation using
uniﬁed segmentation-normalisation models and fuzzy clustering,” NeuroImage, vol. 41, no. 4, pp. 1253–
1266, Jul. 2008.
12. K. Kamnitsas, C. Ledig, V. F. J. Newcombe, J. P. Simpson, A. D. Kane, D. K. Menon et al., “Eﬃcient multi-
scale 3d CNN with fully connected CRF for accurate brain lesion segmentation,” Medical Image Analysis,
vol. 36, pp. 61–78, Feb. 2017.
13. D. Zikic, B. Glocker, and A. Criminisi, “Encoding atlases by randomized classiﬁcation forests for eﬃcient
multi-atlas label propagation,” Medical Image Analysis, vol. 18, no. 8, pp. 1262–1273, Dec. 2014.
14. M. Ghafoorian, N. Karssemeijer, T. Heskes, I. W. M. van Uden, C. I. Sanchez, G. Litjens et al., “Loca-
tion Sensitive Deep Convolutional Neural Networks for Segmentation of White Matter Hyperintensities,”
Scientiﬁc Reports, vol. 7, no. 1, p. 5110, Dec. 2017.
15. C. Wachinger, M. Reuter, and T. Klein, “DeepNAT: Deep convolutional neural network for segmenting
neuroanatomy,” NeuroImage, vol. 170, pp. 434–445, Apr. 2018.


## Page 16


16. A. Guha Roy, S. Conjeti, N. Navab, and C. Wachinger, “QuickNAT: A Fully Convolutional Network for
Quick and Accurate Segmentation of Neuroanatomy,” arXiv e-prints, vol. 1801, p. arXiv:1801.04161, Jan.
2018.
17. M. F. Rachmadi, M. D. C. Vald´es-Hern´andez, M. L. F. Agan, C. Di Perri, T. Komura, and Alzheimer’s
Disease Neuroimaging Initiative, “Segmentation of white matter hyperintensities using convolutional neural
networks with global spatial information in routine clinical brain MRI with none or mild vascular pathology,”
Computerized Medical Imaging and Graphics: The Oﬃcial Journal of the Computerized Medical Imaging
Society, vol. 66, pp. 28–43, 2018.
18. P. Novosad, V. Fonov, and D. L. Collins, “Accurate and robust segmentation of neuroanatomy in T1-
weighted MRI by combining spatial priors with deep convolutional neural networks,” arXiv:1902.01478
[q-bio], Feb. 2019, arXiv: 1902.01478.
19. K. Kushibar, S. Valverde, S. Gonz´alez-Vill`a, J. Bernal, M. Cabezas, A. Oliver et al., “Automated sub-
cortical brain structure segmentation combining spatial and deep convolutional features,” Medical Image
Analysis, vol. 48, pp. 177–186, Aug. 2018.
20. Q. Yue, X. Luo, Q. Ye, L. Xu, and X. Zhuang, “Cardiac segmentation from lge mri using deep neural
network incorporating shape and spatial priors,” in International Conference on Medical Image Computing
and Computer-Assisted Intervention.
Springer, 2019, pp. 559–567.
21. O. Oktay, E. Ferrante, K. Kamnitsas, M. Heinrich, W. Bai, J. Caballero et al., “Anatomically Constrained
Neural Networks (ACNNs): Application to Cardiac Image Enhancement and Segmentation,” IEEE Trans-
actions on Medical Imaging, vol. 37, no. 2, pp. 384–395, Feb. 2018.
22. A. V. Dalca, J. Guttag, and M. R. Sabuncu, “Anatomical priors in convolutional networks for unsuper-
vised biomedical segmentation,” in Proceedings of the IEEE Conference on Computer Vision and Pattern
Recognition, 2018, pp. 9290–9299.
23. A. J. Larrazabal, C. Martinez, and E. Ferrante, “Anatomical Priors for Image Segmentation via Post-
Processing with Denoising Autoencoders,” arXiv:1906.02343 [cs, eess], Jun. 2019, arXiv: 1906.02343.
24. L. Chen, G. Papandreou, I. Kokkinos, K. Murphy, and A. L. Yuille, “DeepLab: Semantic Image Segmenta-
tion with Deep Convolutional Nets, Atrous Convolution, and Fully Connected CRFs,” IEEE Transactions
on Pattern Analysis and Machine Intelligence, vol. 40, no. 4, pp. 834–848, Apr. 2018.
25. J. Zhang, A. Saha, Z. Zhu, and M. A. Mazurowski, “Hierarchical Convolutional Neural Networks for Seg-
mentation of Breast Tumors in MRI With Application to Radiogenomics,” IEEE Transactions on Medical
Imaging, vol. 38, no. 2, pp. 435–447, Feb. 2019.
26. H. Chen, Q. Dou, L. Yu, J. Qin, and P.-A. Heng, “VoxResNet: Deep voxelwise residual networks for brain
segmentation from 3D MR images,” NeuroImage, vol. 170, pp. 446–455, Apr. 2018.
27. L. Hirsch, Y. Huang, and L. C. Parra, “Tissue segmentation with deep 3d networks and spatial priors,”
arXiv preprint arXiv:1905.10010, 2019.
28. Y. Huang, J. P. Dmochowski, Y. Su, A. Datta, C. Rorden, and L. C. Parra, “Automated MRI segmentation
for individualized modeling of current ﬂow in the human head,” J. Neural Eng., vol. 10, no. 6, p. 066004,
Dec. 2013.
29. A. G. Schwing and R. Urtasun, “Fully Connected Deep Structured Networks,” arXiv:1503.02351 [cs], Mar.
2015, arXiv: 1503.02351.
30. S. Chandra, N. Usunier, and I. Kokkinos, “Dense and Low-Rank Gaussian CRFs Using Deep Embeddings,”
in 2017 IEEE International Conference on Computer Vision (ICCV).
Venice: IEEE, Oct. 2017, pp.
5113–5122.
31. Y. Huang and L. C. Parra, “Fully Automated Whole-Head Segmentation with Improved Smoothness and
Continuity, with Theory Reviewed,” PLOS ONE, vol. 10, no. 5, p. e0125477, May 2015.
32. P. Kr¨ahenb¨uhl and V. Koltun, “Eﬃcient Inference in Fully Connected CRFs with Gaussian Edge Potentials,”
in Advances in neural information processing systems, 2011, pp. 109–117.
33. O. Ronneberger, P. Fischer, and T. Brox, “U-Net: Convolutional Networks for Biomedical Image Segmen-
tation,” arXiv:1505.04597 [cs], May 2015, arXiv: 1505.04597.


## Page 17


34. W. R. Crum, O. Camara, and D. L. G. Hill, “Generalized Overlap Measures for Evaluation and Validation
in Medical Image Analysis,” IEEE Transactions on Medical Imaging, vol. 25, no. 11, pp. 1451–1461, Nov.
2006.
35. C. H. Sudre, W. Li, T. Vercauteren, S. Ourselin, and M. J. Cardoso, “Generalised Dice overlap as a deep
learning loss function for highly unbalanced segmentations,” arXiv:1707.03237 [cs], vol. 10553, pp. 240–248,
2017, arXiv: 1707.03237.
36. B. Hermann, F. Raimondo, L. Hirsch, Y. Huang, M. Denis-Valente, P. P´erez et al., “Combined behavioral
and electrophysiological evidence for a direct cortical eﬀect of prefrontal tDCS on disorders of consciousness,”
bioRxiv, p. 612309, Apr. 2019.
37. Y. Huang, A. Datta, M. Bikson, and L. C. Parra, “Realistic volumetric-approach to simulate transcranial
electric stimulation—ROAST—a fully automated open-source pipeline,” Journal of Neural Engineering,
vol. 16, no. 5, p. 056006, Jul. 2019.
38. R. Ettarh, “Pocket Atlas of Sectional Anatomy: Computed Tomography and Magnetic Resonance Imaging,
Volume I: Head and Neck; Volume II: Thorax, Heart, Abdomen, and Pelvis, 4th edn,” Journal of Anatomy,
vol. 224, no. 6, pp. 737–738, Jun. 2014.
39. C. Egger, R. Opfer, C. Wang, T. Kepp, M. P. Sormani, L. Spies et al., “MRI FLAIR lesion segmentation in
multiple sclerosis: Does automated segmentation hold up with manual annotation?” NeuroImage: Clinical,
vol. 13, pp. 264–270, Jan. 2017.
40. Q. Qiu, J. Duan, Z. Duan, X. Meng, C. Ma, J. Zhu et al., “Reproducibility and non-redundancy of radiomic
features extracted from arterial phase CT scans in hepatocellular carcinoma patients: impact of tumor
segmentation variability,” Quantitative Imaging in Medicine and Surgery, vol. 9, no. 3, pp. 453–464, Mar.
2019.
41. C. Schnakers, A. Vanhaudenhuyse, J. Giacino, M. Ventura, M. Boly, S. Majerus et al., “Diagnostic accuracy
of the vegetative and minimally conscious state: Clinical consensus versus standardized neurobehavioral
assessment,” BMC Neurol, vol. 9, no. 1, p. 35, Dec. 2009.
42. A. Bender, R. J. Jox, E. Grill, A. Straube, and D. Lul´e, “Persistent Vegetative State and Minimally Con-
scious State,” Dtsch Arztebl Int, vol. 112, no. 14, pp. 235–242, Apr. 2015.
43. J. Deng, W. Dong, R. Socher, L.-J. Li, K. Li, and L. Fei-Fei, “Imagenet: A large-scale hierarchical image
database,” in 2009 IEEE conference on computer vision and pattern recognition.
Ieee, 2009, pp. 248–255.
44. S. Zheng, S. Jayasumana, B. Romera-Paredes, V. Vineet, Z. Su, D. Du et al., “Conditional Random Fields
as Recurrent Neural Networks,” in 2015 IEEE International Conference on Computer Vision (ICCV).
Santiago, Chile: IEEE, Dec. 2015, pp. 1529–1537.
45. B. B. Avants, C. L. Epstein, M. Grossman, and J. C. Gee, “Symmetric Diﬀeomorphic Image Registration
with Cross-Correlation: Evaluating Automated Labeling of Elderly and Neurodegenerative Brain,” Medical
image analysis, vol. 12, no. 1, pp. 26–41, Feb. 2008.
46. M. Jaderberg, K. Simonyan, A. Zisserman, and k. kavukcuoglu, “Spatial Transformer Networks,” in Ad-
vances in Neural Information Processing Systems 28, C. Cortes, N. D. Lawrence, D. D. Lee, M. Sugiyama,
and R. Garnett, Eds.
Curran Associates, Inc., 2015, pp. 2017–2025.


## Page 18


APPENDIX A. EXAMPLES OF MANUAL SEGMENTATIONS
Volumetric segmentation labels were obtained in a semi-automatic process using SPM8 and applying manual
corrections, which were used to train the neural network. In order to have an unbiased set of labels; manual
segmentations were done from scratch in 2D slices containing visible lesions. To obtain a reference for variability
between manual segmentations, ten scans were segmented twice, each independently by a separate segmenter.
We show ﬁve examples of these duplicated segmentations, displaying regions were there is disagreement.
 
A          B         C
Figure 11. Examples of T1-weighted MRIs (column A) from ﬁve diﬀerent stroke patients and their corresponding segmen-
tation. Manual segmentations done from scratch by two diﬀerent trainees are displayed in columns B and C. Segmentation
colors are arbitrarily chosen to represent the following tissues: CSF = light-blue, white-matter = white, gray-matter =
gray, bone = yellow, skin = brown, air = green, background = black.


## Page 19


Figure 12. Ten examples of SPM8 segmentations and manual corrections of lesion areas. Each row displays a lesion area
in three orthogonal planes (axial, sagittal and coronal in this order) for each subject. For every presented MRI, the
corresponding segmentation from SPM8 is shown directly on its right, which often fails to capture the CSF-ﬁlled lesion,
and right next to it, the segmentation after manual correction, which was used as the target label for the training set.
Segmentation colors are arbitrarily chosen to represent the following tissues: CSF = light-blue, white-matter = white,
gray-matter = gray, bone = yellow, skin = brown, air = green, background = black.


## Page 20


Figure 13. Additional ten examples of SPM8 segmentations and manual corrections of lesion areas. Each row displays
a lesion area in three orthogonal planes (axial, sagittal and coronal in this order) for each subject. For every presented
MRI, the corresponding segmentation from SPM8 is shown directly on its right, which often fails to capture the CSF-ﬁlled
lesion, and right next to it, the segmentation after manual correction, which was used as the target label for the training
set. Segmentation colors are arbitrarily chosen to represent the following tissues: CSF = light-blue, white-matter = white,
gray-matter = gray, bone = yellow, skin = brown, air = green, background = black.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
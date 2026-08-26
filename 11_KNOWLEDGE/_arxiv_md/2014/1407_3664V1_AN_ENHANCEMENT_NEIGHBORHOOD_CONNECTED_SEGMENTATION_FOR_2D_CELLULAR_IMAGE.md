---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1407.3664v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1407.3664v1_An_Enhancement_Neighborhood_connected_Segmentation_for_2D-Cellular_Image

> Source: 1407.3664v1_An_Enhancement_Neighborhood_connected_Segmentation_for_2D-Cellular_Image.pdf

> Pages: 6

---


## Page 1


 
 
Abstract— a good segmentation result depends on a set of 
“correct” choice for the seeds. When the      input images are 
noisy, the seeds may fall on atypical pixels that are not 
representative of the region statistics. This can lead to 
erroneous segmentation results. 
In this paper, an automatic seeded region growing algorithm is 
proposed for cellular image segmentation. First, the regions of 
interest (ROIs) extracted from the preprocessed image. Second, 
the initial seeds are automatically selected based on ROIs 
extracted from the image. Third, the most reprehensive seeds 
are selected using a machine learning algorithm. Finally, the 
cellular image is segmented into regions where each region 
corresponds to a seed. The aim of the proposed is to 
automatically extract the Region of Interests (ROI) from in the 
cellular images in terms of overcoming the explosion, under 
segmentation and over segmentation problems. Experimental 
results show that the proposed algorithm can improve the 
segmented image and the segmented results are less noisy as 
compared to some existing algorithms. 
 
Index Terms—Image Segmentation, Seeded Region Growing, 
Machine Learning, Leaking problem. 
 
I. INTRODUCTION 
   
Quantitative studies have been performed based on 
populations of biological images. Such studies extremely 
require methods for segmentation, feature extraction, and 
classification.  
 
A first step in many analysis pipelines is segmentation, 
which can occur at several levels (e.g., separating nuclei, 
cells, tissues). This task has been an active field of research 
in image processing over the last 30 years, and various 
methods have been proposed and analysed depending on the 
modality, quality, and resolution of the microscopy images 
to analyze. 
 
For image segmentation, there are four main approaches: 
threshold techniques, boundary based techniques, region 
based techniques, and hybrid techniques [1].  
 
 
 
 
Preprint submitted to International Journal of International Journal of 
Bioscience, Biochemistry and Bioinformatics 
 
 
 
 
 
In threshold techniques [2] all pixels whose value (gray 
level, color value, or other) lie within a certain range can be 
classified as one class. Such methods neglect all of the 
spatial information of the image and do not cope well with. 
 
Boundary based methods [3] use the postulate of the rapid 
changes of the pixel values at the boundary between two 
regions. The basic method here is to apply a gradient 
operator (e.g., Sobel, Roberts filter). High values of this 
filter provide candidates for region boundaries, which must 
then be modified to produce closed curves representing the 
boundaries between regions. Converting the edge pixel 
candidates to boundaries of the regions of interest is a 
difficult task. The complement of the boundary-based 
approach is to work with the regions.  
 
Region based methods [4] rely on the postulate that all 
neighbouring pixels within the one region have similar value 
or a specific range. This leads to the class of algorithms 
known as region growing of which the “split and merge” 
technique is probably the best known. The general procedure 
is to compare a specific feature of one pixel to its 
neighbor(s) feature. If a criterion of homogeneity is satisfied, 
the pixel is classified to the same class as one or more of its 
neighbors. The choice of the homogeneity criterion is 
critical for even moderate success and in all instances the 
results are upset by noise. 
 
The fourth type is the hybrid techniques [5] which 
combine boundary and region criteria. This class includes 
morphological watershed segmentation and variable-order 
surface fitting. The watershed method is generally applied to 
the gradient of the image. This gradient image can be viewed 
as topography with boundaries between regions as ridges. 
Segmentation is equivalent to flooding the topography from 
the seed points with region boundaries being erected to keep 
water from different seed points from meeting. As same as 
all pervious method the technique encounters difficulties 
with images in which regions are both noisy and have 
blurred or indistinct boundaries. Furthermore, method is also 
computationally very expensive. 
 
In this paper, an accurate segmentation method is 
proposed based on the seeded region growing method to be 
less sensitive to the noisy image and quantified and avoid 
explosion, 
leaking, 
under 
segmentation, 
and 
over 
segmentation problems. 
 
 An Enhancement Neighborhood connected 
Segmentation for 2D-Cellular Image 
 
 
 
 
Mohammed. M. Abdelsamea  
Mathematics Department, Assiut University, Egypt


## Page 2


II. RELATED WORK 
 
Jie Wu et al [6] proposed a new texture feature-based 
seeded 
region 
growing 
algorithm 
for 
automated 
segmentation of organs in abdominal MR images. The 
proposed seed point determination method is based on a 
cost-minimization approach. An ideal candidate seed point 
should have these properties: i) It should be inside the region 
and near the center of the region ii) Assume most of the 
pixels in the ROI belong to the region (i.e. ROI is not too big 
compared to the region), the feature of this seed point should 
be close to the region average iii) The distances from the 
seed pixel to its neighbors should be small enough to allow 
continuous growing. 
 
Mehnert and Jackway [7] pointed out that Seeded Region 
Growing (SRG) has two inherent pixel order dependencies 
that cause different resulting segments. The first-order 
dependency occurs whenever several pixels have the same 
difference measure to their neighboring regions. The second-
order dependency occurs when one pixel has the same 
difference measure to several regions. They used parallel 
processing and re-examination to eliminate the order 
dependencies. 
 
Frank et al [8] present an automatic seeded region 
growing algorithm for color image segmentation. In this 
paper, they apply the SRG to color images with automatic 
seed selection. They develop strategies to avoid the two 
order dependencies. For automatic seed selection, the 
following three criteria must be satisfied. First, the seed 
pixel must have high similarity to its neighbors. Second, for 
an expected region, at least one seed must be generated in 
order to produce this region. Third, seeds for different 
regions must be disconnected. 
 
 
 
 
 
 
 
 
 
 
 
 
 
    Whitney et al. [9] overcomes the need to manually select 
threshold values by analyzing the histogram of voxel 
similarity to automatically determine a stopping criterion, 
but they still require the user to choose a seed point.  
 
Law et al. [10] proposed a Genetic Algorithm based seed 
selection method and a threshold value optimization method, 
but their algorithm has the problem of possible under-
segmentation and speed can also be an issue although they 
did not address them.  
 
There are a number of known issues associated with SRG 
scheme: 
 
A good segmentation result depends on a set of “correct” 
choice for the seeds. When the  input images are noisy, the 
seeds may fall on atypical pixels that are not representative of 
the region statistics. This can lead to erroneous segmentation 
results. 
 
     The seed selection process in itself requires manual 
interventions, and is error-prone. Even though automatic 
segmentation can be achieved in a limited sense, it is 
application specific and will require domain-specific 
knowledge and training sets.  
 
    All of these make SRG unsuitable for segmentation where a 
priori knowledge is limited. The main idea of the proposed 
algorithm is to overcoming these drawbacks. 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Fig. 1. Outline of the proposed algorithm.


## Page 3


III. METHODOLOGY OVERVIEW 
 
   The system consist of three stages: i) After the 
preprocessed image is loaded into the system, the ROIs 
extracted via Otsu image segmentation from the image as a 
binary object; ii) a proposed method is applied for 
automatically selected seeds based on positions and 
intensities of pixels located in ROIs extracted; iii) a region 
growing procedure is recursively called for segment an input 
image as a seeded region growing based on seeded 
candidates and Otsu threshold. Fig 1 illustrates the overview 
of the proposed algorithm. 
 
IV. THE METHOD FOR SEED SELECTION 
 
Seeded region growing performs a segmentation of an 
image with respect to a set of points, known as seeds. We 
start with a number of seeds which have been grouped into n 
sets, say, A1, A2, . . . ,An. Given a seed point, the region 
growing method searches the seed point’s neighbors to 
determine whether they belong to the same region. If they 
are determined to be so, their neighbors are searched. The 
process is recursively executed until no more new neighbors 
can be added to the region [11]. 
 
The criterion is when the distance is lower than a 
threshold value a neighbor point is added. So we need to 
determine 
the 
distance 
measure, 
linkage 
strategy, 
connectivity strategy and a threshold value [12], See Fig.2. 
 
 
For automatic seed selection, an ideal candidate must 
have the following properties and satisfy the following 
criteria. 
   
i) Make sure that the seed point candidate is not on the 
boundary of two regions and/or not outlier. 
  
 ii) Check whether this candidate seed point has high 
similarity to its neighbours, which it should be inside the 
selected ROI and has the highest similarity between its 
neighbors to accurately represent the region. 
 
 iii) At least one seed pixel must be generated for each 
extracted ROI. 
 
 iv) The distances measured from the seed pixel to its 
neighbors should be inside extracted region to allow 
continuous growing. 
 
For satisfy these criteria the proposed segmentation 
describes as follow: 
 
The first segmentation step after image acquisition tries to 
reduce the noise present in the image. To reduce noise 
several non-linear filters can be employed. One of the 
simplest techniques, the median filter, can be employed here 
given that it provided good noise reduction without affecting 
the borders of the objects on the image. 
 
Secondly, an Otsu segmentation method is applied in 
order to: extract ROIs from the input image and extract Otsu 
threshold, threshold that classifies the image into two 
clusters such that we minimize the area under the histogram 
for one cluster that lies on the other cluster’s side of the 
threshold, to be used later as input in region growing 
procedure.  
 
 
 
 
 
 
 
 
 
 
 
 
The aim of the filtering step is to remove outliers points 
and points located on the boundary of ROIs by considering 
and using R X R neighborhood mask to make sure that all 
the tested seed point's neighbors located within this mask, A 
particular pixel will be considered as a boundary pixel or 
outlier if at least one of all its neighbours is determined as a 
background pixel. The size of the neighbourhood to be 
considered around the pixel is determined by a radius value 
R. 
 
Thirdly, candidate seeds positions and its intensity values 
are extracted as features to represent the training set, which 
in this case the candidate seeds are the patterns of the 
training set, and apply it for clustering via machine learning 
Fig.2, 6-(squares), 18-(circles), and 26-neighbors (dots). 
Fig. 3. (a1) Original image, (a2) the result of 
segmentation using the proposed algorithm with K = 4 
and R = 3, (a3) the segmentation result using Otsu 
method, (a4) the segmentation result using watershed 
method with L = .08 and T = .08.


## Page 4


technique; in this work K-mean clustering technique has 
been used. 
 
After training process, the training pattern is applied as a 
test pattern to the learned algorithm and K is specified 
accordingly, which K is number of seeds or number of 
object that user would like to extract, to get the most 
representive point to use as seeds for the Region Growing 
method for segment image into region where each region 
corresponds to a seed.   
 
 
 
 
 
 
 
 
 
 
 
 
 
 
In Seed Extraction, we can consider extracting of the seed 
as a Missing Value Imputation problem which can be solved 
by extracting the prototypes of the positions of the centroids 
to act as an ideal seeds. By this step we make sure that this 
candidate seed has the highest similarity between its 
neighbors, at least one seed must be generated for each 
expected region, and the distances measured from the seed 
pixel to its neighbors should be inside extracted region to 
allow continuous growing.  
 
It’s obviously clear that this proposed method can avoid 
the explosion, under-segmentation and over-segmentation 
problems.  
 
 
 
 
How to quantify an explosion?  
By using the concept of considering the neighbors for 
growing the region, the object will not grow over its 
boundary. 
 
How to avoid under-segmentation?  
1. Using Otsu threshold with the main concepts of the 
growing region strategy have been used in this work, allow 
extract the whole region and make a stop before explosion. 
2. make sure that the seed point candidate is not on the 
boundary of two regions.  
 
How to avoid over-segmentation? 
At least one seed pixel must be generated for each 
expected region, and Make sure that this candidate seed has 
the highest similarity between its neighbors to accurately 
represent the region. 
 
How to determine whether a neighbor pixel belongs to the 
same region? 
      The criterion is when the distance is lower than a 
threshold value a neighbor point is added. So we need to 
determine 
the 
distance 
measure, 
linkage 
strategy, 
connectivity strategy and a threshold value. 
 
Distance measure:  
 The Euclidean distance in the feature space is used as the 
distance measure. For example, the distance between two 
pixels is the Euclidean distance of their feature vectors. 
 
Linkage strategy:  
    In single linkage, the pairs of neighboring pixels are 
compared for merging, is one of the conceptually simplest 
approaches.  
    In centroid linkage, a pixel’s value is compared with the 
mean of an already existing but not necessarily completed 
region.  
 
    Single linkage strategy has been chosen over centroid 
linkage because it is faster and more memory efficient 
considering the calculation of texture features and 
recursively running SRG requires much memory. 
 
Connectivity strategy:  
  
     In 2D region growing, there are two connectivity 
strategies that people use: four-neighbor and eight- neighbor. 
Four-neighbor region growing checks only the vertically and 
horizontally connected four  neighbors, while eight-neighbor 
region 
growing 
checks 
vertically, 
horizontally 
and 
diagonally connected eight neighbors. The choice of 
neighbor connection strategy is usually case dependent. 
 
     An optimal threshold value is the value that can make a 
stop to the region growing and the obtained region is 
optimal. It is desirable that the threshold value is high 
enough to extract the whole region; however if the threshold 
value is higher than the optimal one, the extracted region 
may grow over the actual region boundary and grow to a 
much larger region. This case is called ‘explosion’ 
 
V. SEEDED REGION GROWING 
 
For growing the region based on the extracted seed, it’s 
desirable to use the same principle of the filtering which has 
been used in this work to avoid the explosion and under 
Fig. 4, (a1) Original image, (a2) the result of 
segmentation using the proposed algorithm with K 
= 4 and R = 3, (a3) the segmentation result using 
Otsu method, (a4) the segmentation result using 
watershed method with L = .05 and T = .05.


## Page 5


segmentation that might be happen because of the leaking 
problem of the region growing. For this reason a 
neighbourhood condition has been applied for accepting the 
pixel to be including in the region, these conditions based on 
the intensity value by considering an Otsu Threshold as an 
optimal threshold. 
 
By the principle of neighbourhood connected, growing 
the region is not completely depend on the feature of interest 
determined by the seed, the feature of interest that 
determined by the seed is just a position. 
 
 
VI. EXPERIMENTAL RESULTS     
 
I have performed the experiments using the proposed 
segmentation algorithm and performed comparisons with 
some existing segmentation algorithm. In Fig 3, 4, 5, and 6, 
we show the comparison with Otsu algorithm, Watershed 
algorithm, and JSEG algorithm [13]. 
    
 By observing Fig 3(a3, a4), Fig 4(a3, a4), and Fig 5(a3, a4) 
we can realize that their results are over segmented. 
Segmented objects in Fig 3(a5), Fig 4(a5), and Fig 6 are 
inappropriately merged to background. 
  
 By comparing these results with results of our proposed 
algorithm in Fig 3(a2), Fig 4(a2), and Fig 5(a2) we can 
clearly notice that the proposed segmentation algorithm 
overcoming the over-segmentation problem and is less noisy 
as compared to other algorithms.   
 
VII. CONCLUSION  
 
The issues of SRG Algorithm can be summarized as: The 
selection of the seeds determines what a feature of interest is 
and what is irrelevant. So, growing the region is completely 
depending on the feature of interest determined by the seed. 
 
In this paper, an automatic seeded region growing 
framework (as an extension to [14]) for automatically 
segment 2D cellular image is proposed. One of the 
advantages of this algorithm is obvious, as it provides a 
parameter free production environment to allow minimum 
user intervention. This can be especially helpful for batch 
work or to novice computer users. The other benefit of this 
algorithm is overcoming the explosion, under segmentation 
and over segmentation problems. 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
  Furthermore, it is clearly that the proposed algorithm 
able to consuming time because only specific regions are 
used to produce seeds.   
 
       However, the selection of k, number of expected regions 
might lead to miss-segmentation. Check whether this 
candidate seed has the highest similarity between its 
neighbors is sensitivity to the selection of the number of the 
expected regions, which might lead to miss-segmentation. 
  
    The issue can be summarized as: The sensitivity to how to 
expect the region and the number of expected regions might 
lead to extract seed inaccurately represent the region. 
 
The future work includes investigation of other features 
like texture features as a feature for selecting seeds and 
growing the region. 
 
 
 
 
 
Fig. 5, (a1) Original image, (a2) the result of 
segmentation using the proposed algorithm with K = 3 
and R = 3, (a3) the segmentation result using Otsu 
method, (a4) the segmentation result using watershed 
method with L = .5 and T = .5, (a5) the segmentation 
result using JSEG.


## Page 6


References 
 
 
[1] P. J. Besl and R. C. Jain, “Segmentation through variable-order 
surface fitting,” IEEE Trans. Pattern Anal. Machine Intell., vol. 
PAMI-IO, pp. 167-192, 1988. 
 
[2] P. K. Sahoo, S. Soltani, A. K.C. Wong, and Y. C. Chen. 1988. A 
survey of thresholding techniques. Comput. Vision Graph. Image 
Process. 41, 2 (February 1988), 233-260.  
 
[3] L.  S. Davis, “A survey of edge detection techniques,” Comput. 
Graph. Image Process., vol.  4, pp.  248-270, 1975. 
 
[4]  S. W. Zucker, “Region growing: Childhood and adolescence,” 
Comput. Graph. Image Process., vol. 5, pp. 382-399, 1976.s 
 
[5] F. Meyer and S. Beucher, “Morphological segmentation,” J. Vis. 
Commun. Image Represent. vol.  1, pp.  2146, 1990. 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
[6] J. Wu, S. Poehlman, M. D. Noseworthy, M. Kamath, (2008) Texture 
Feature based Automated Seeded Region Growing in Abdominal 
MRI Segmentation, 2008 International Conference on Biomedical 
Engineering and Informatics, Sanya, China, May 27-30. 
 
[7] A. Mehnert, P. Jackway, An improved seeded region growing 
algorithm, Pattern Recognition Letters 18 (1997) 1065–1071. 
 
[8] FY Shih and S. Cheng, "Automatic seeded region growing for color 
image segmentation", Image and Vision Computing, Vol. 23, 2005, 
pp. 877-886 
 
[9] R. Adams and L. Bischof.  Seeded region growing. IEEE Trans. 
Pattern Anal. Mach. ntelligence, 16(6):641-647, 1994. 
 
[10] B. W. Whitney, N. J. Backman, J. D. Furst, D. S. Raicu, (2006) 
“Single click     volumetric segmentation of abdominal organs in 
Computed Tomography images”, Proceedings of SPIE Medical 
Imaging Conference, San Diego, CA, Februar. 
 
[11]  T.-Y. Law and P. A. Heng, (2000) “Automated extraction of 
bronchus from 3-D CT images of lung based on genetic algorithm 
and 3-D region growing”, Proc. SPIE 3979, Medical Imaging 2000: 
Image Processing, 906-916. 
 
[12] Jie Wu, Skip Poehlman, Michael D. Noseworthy, Markad V. Kamath, 
"Texture Feature-based Automated Seeded Region Growing in 
Abdominal MRI Segmentation", Journal of Biomedical Science and 
Engineering, (Feb. 2009), pp.1-8. 
 
 
[13] Y.Deng, and B.S.Manjunath, "Unsupervised segmentation of color-
texture regions in images and video," IEEE Transactions on Pattern 
Analysis and Machine Intelligence (PAMI '01), August 2001. 
 
[14]   M. M. Abdelsamea. An Automatic Seeded Region Growing for 2D 
Biomedical Image Segmentation. In Proceedings of theInternational 
Conference on Environment and BioScience, Singapore 2011. 
 
Fig. 6, the result of segmentation using the JSEG 
algorithm.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1407_3664v1_an_enhancement_neighborhood_connected_segmentation_for_2d_cellular_image
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2014/1407_3664V1_AN_ENHANCEMENT_NEIGHBORHOOD_CONNECTED_SEGMENTATION_FOR_2D_CELLULAR_IMAGE.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

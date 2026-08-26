---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1901.02529
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1901.02529_A_Spatial-temporal_3D_Human_Pose_Reconstruction_Framework

> Source: 1901.02529_A_Spatial-temporal_3D_Human_Pose_Reconstruction_Framework.pdf

> Pages: 11

---


## Page 1


www.kips.or.kr                                                                                                Copyright©  XXXX  KIPS 
J  Inf  Process  Syst,           
ISSN  1976-­913X (Print) 
http://dx.doi.org/10.3745/JIPS 
ISSN  2092-­805X (Electronic)  
  
 
 
A  Spatial-­temporal  3D  Human  Pose      
Reconstruction  Framework  
 
  
Xuan  Thanh  Nguyen  *,  Thi  Duyen  Ngo  **  and  Thanh  Ha  Le  **  
 
 
Abstract  
3D human pose reconstruction from single-view camera is a difficult and challenging topic. Many approaches 
have been proposed, but almost focusing on frame-by-frame independently while inter-frames are highly 
correlated in a pose sequence. In contrast, we introduce a novel spatial-temporal 3D reconstruction 
framework that leverages both intra and inter frame relationships in consecutive 2D pose sequences. 
Orthogonal Matching Pursuit (OMP) algorithm, pre-trained Pose-angle Limits and Temporal Models have 
been implemented. We quantitatively compare our framework versus recent works on CMU motion capture 
dataset and Vietnamese traditional dance sequences. Our method outperforms others with 10 percent lower of 
Euclidean reconstruction error and robustness against Gaussian noise. Additionally, it is also important to 
mention that our reconstructed 3D pose sequences are smoother and more natural than others. 
Keywords  
3D human pose, Reconstruction, Spatial-temporal model  
 
1.  Introduction  
Reconstruction of 3D human pose from single-view camera plays an important role in many computer 
vision research fields such as animation, human-computer interaction and video surveillance 
applications [1]. A human action is naturally represented by a sequence of poses which is usually 
described by a hierarchy skeleton structure of joint positions. Finding 3D corresponding pose of 2D 
pose is obviously ambiguous since many plausible 3D poses satisfy a single 2D pose [2]. 
Previous approaches were introduced to reconstruct 3D human pose from monocular/multi-view 
image, video, depth channel. However, these approaches typically focus on single frame independently 
while all frames in a sequence are highly correlated [3] [4] [5] [6]. Others lay on fixed joint angle limit 
models which are not general enough for the diverse of human poses and sometimes leading to invalid 
reconstructed 3D poses [7] [8]. 
Our goal is taking advantages of frame correlation in a sequence of poses. In this paper, we focus on 
input data of 2D pose sequences, the key idea of our framework is combining intra and inter frames 
relationships in a consecutive pose sequence. Given a 2D human pose sequence, we firstly use 
Orthogonal Matching Pursuit algorithm and pre-trained Pose-angle Limits model to estimate prior 3D 
pose results. This pre-trained pose-dependent model was introduced by [3] that solved the fixed joint 
angle problems. Secondly, temporal models independently correct and smooth sequence of 3D poses to 
generate final 3D poses. Our method have been tested on CMU dataset and recorded Vietnamese 
Traditional Dance sequences to show state-of-the-art reconstruction results compare to other existing 
methods. 
※   This   is   an   Open   Access   article  distributed   under   the   terms   of   the   Creative   Commons   Attribution   Non-­Commercial   License   (http://creativecommons.org/licenses/by-­nc/3.0/)   which  
permits  unrestricted  non-­commercial  use,  distribution,  and  reproduction  in  any  medium,  provided  the  original  work  is  properly  cited.  
Manuscript  received    Month  06,  20XX;  accepted  Month  06,  20XX.  
Corresponding  Author:  Xuan  Thanh  Nguyen(thanhxuan.nguyen@esiee.fr)  
*        ESIEE  Paris,  France(thanhxuan.nguyen@esiee.fr)  
**      UET-­VNU  Hanoi,  Vietnam  (lthavnu@gmail.com)


## Page 2


A  Spatial-­temporal  3D  Human  Pose  Reconstruction  Framework  
 
2  |  J  Inf  Process  Syst, 
Our contribution are:  
• Proposing a spatial-temporal 3D reconstruction framework that takes advantage of both intra and 
inter frame relationships in consecutive 2D pose sequences.  
• Using temporal models as an post-processing step to smooth reconstructed motion sequences, this 
module can be re-used independently in other methods.  
The remainder of this paper is organized as follows: Section 2 gives a short literature review of state-
of-the-art 3D human pose estimation studies. Section 3 describes our proposed framework using 
Orthogonal Matching Pursuit (OMP) algorithm, pre-trained Pose-angle Limits and Temporal Models. 
Experimental results on CMU motion capture dataset and Vietnamese traditional dance sequences are 
given in Section 4. Finally, in Section 5, we briefly conclude our method.  
 
2.  Related  Works  
  Fundamentally, 3D human pose reconstruction from single color camera is an under-constrained 
problem which is much more challenging than multi-view or depth channel reconstruction since lacking 
of three-dimensional information. Typically, 2D human poses are firstly estimated from image/video, 
then 2D-to-3D poses conversion is the second step. Within scope of this work, our paper specifically 
focuses on major contribution of 3D poses temporal model reconstruction from 2D poses. For the first 
step of singe-view image/video to 2D pose, this paper re-use Deepcut [9] which is a widely known deep 
learning-based framework for 2D pose detection.  
  Many approaches have been proposed to reconstruct 3D human pose from only monocular view data 
[3] [10] [11] or video sequences [4] [5]. Ramakrishna et al. [3] presented an activity-independent 
method to recover 3D configuration from a single image using a orthogonal matching pursuit (OMP) 
algorithm and 3D pose sparse representation on an over-completed dictionary of basic poses. They take 
advantage of a large motion capture corpus as a proxy for visual memory to draw a plausible 3D 
configuration. However, this model has problem with strong perspective effects image where weak 
perspective assumptions on the camera model are violated and mean pose is not a reasonable initialized. 
Tekin et al. [11] proposed a deep learning regression for structure prediction of 3D human pose from 
monocular image. This method relies on an overcomplete auto-encoder to learn a high-dimensional 
latent pose representation and using CNN to map pose into learned latent space. Drawback of the 
Tekin’s machine learning-based method is requirement of a huge manual annotation dataset and 
computational complexity. 
  Chen et al. [5] seeks to estimate and track human upper-body pose from an image or a video sequence, 
they used prior data-driven models typically learned from 3D motion capture data which are expensive 
and time-consuming to collect. Besides, only upper body pose result is their main disadvantages 
compare to other full body pose reconstruction models. Recently, Akhter et al. [4] published a Pose-
angle Limits model for 3D human pose reconstruction which is state-of-the-art outperforms existing. 
This method trains a Pose-angle Limits model that adaptively constraints joints angle to eliminate 
abnormal poses based on prior knowledge. However, this model still processes frame-by-frame 
independently while all frames in a sequence are highly correlated. In this paper, we consider [4] as the 
baseline, more details on Section 4. 
  This paper emphasizes the novel idea of taking advantage of inter-frames temporal relationship in a 
sequence of poses. Given a 2D human pose sequence, we firstly use Orthogonal Matching Pursuit 
algorithm and pre-trained Pose-angle Limits model to estimate prior 3D pose results. This pre-trained 
pose-dependent model were introduced by [3] that solve the fixed joint angle problems. Secondly, 
temporal models independently correct and smooth sequence of 3D poses to generate final 3D poses. 
Our method have been tested on CMU dataset and recorded Vietnamese Traditional Dance sequences to 
show state-of-the-art reconstruction results compare to other existing methods.


## Page 3


Xuan  Thanh  Nguyen  *,  Thi  Duyen  Ngo  **  and  Thanh  Ha  Le  **  
 
J  Inf  Process  Syst,  |  3  
3.  Proposed  Methods  
3.1  Framework  Overview  
 
 
Figure 1: Overview of our framework 
 The outline of our 3D human pose reconstruction from 2D human pose framework is shown in Figure 1. 
Given a 2D skeleton (15 joints model), we firstly use a greedy Orthogonal Matching Pursuit (OMP) 
algorithm [3] to estimate 3D poses that minimizes projection errors. However, there always exist a set 
of satisfied 3D poses corresponding to a single 2D pose. In this research, we use a pre-trained Pose-
angle Limits model to eliminate invalid poses and choose the best candidate. Invalid poses stand for 
abnormal and impossible joint angles which was introduced by [4]. Now, considering a sequence of 2D 
skeleton, the second step leverages temporal relationship between consecutive frames to reduce high 
frequency pose movements by applying temporal models which are explained detail in Subsection 3.3. 
Finally, the framework outputs a smooth sequence of 3D human poses. 
 
3.2  Pose-­angle  Limits  model  and  OMP  Algorithm  
 
  We firstly re-cap the concept of Pose-angle Limits model which was originally introduced by [4]. In 
2015, Akhter et al. captured a dataset of motions where actors were asked to keep their upper-arm fixed, 
fully flex and extend their lower-arms and then turn them inwards to outwards. Similar motions were 
recorded for the legs. From this data, a Pose-angle Limits model of kinematic skeleton was trained. 
Given a skeleton of P joints: 𝑋= [𝑋$
%,…, 𝑋(
%]% ∈𝑅,(×$, Pose-angle Limit provides a function to 
determine either an joint is in a valid pose or not. We re-use this pre-trained Pose-angle Limit in our 
framework. 
𝑖𝑠𝑣𝑎𝑙𝑖𝑑(𝑋): 𝑅,×( →{0,1}(. 
1 
In [3], a linear combination of basis poses are used to represent a sparse form of 3D human pose: 
𝑋= 𝜇+ Σ?@$
A 𝑤?𝑏? = 𝜇+ 𝐵∗𝑤, 
{𝑏?}?∈FG∗∈𝐵∗⊂𝐵I. 
2 
where 𝜇 is mean-pose obtained by averaging poses from the CMU motion capture dataset; 𝐾 is the 
number of basis poses; 𝑏? are the basis poses, 𝑤 is a vector of pose coefficients 𝑤?; matrix 𝐵∗ is a 
column-wise concatenation of basis poses 𝑏? selected with column indices 𝐼L∗; 𝐵I	
  is an over-complete 
dictionary of basis components; 𝐵∗ is optimal subset from 𝐵I, contains a number of basis pose  represent 
𝑋.  
  In order to find the unknown 3D pose X, they minimize projection error to find 𝑤, 𝐼L∗,𝑠 (camera scale) 
and R (camera rotation) using Orthogonal Matching Pursuit (OMP) algorithm subject to anthropometric 
regularization: 
 
 
 
 
 
 
 
 
 
 
             3 
𝐶O(𝑤,𝐼L∗, 𝑠, 𝑅) = P𝑥−𝑠(𝐼⊗𝑅$:T)(𝐵∗𝑤+ 𝜇) PT
T	
  . 
where ⊗ denotes Kronecker product, 𝑅$:T	
  gives first two rows of matrix R. Once 𝑤, 𝐼L∗,𝑠 are known, 
the 3D pose is estimated as:  
𝑋= (𝐼⊗𝑅)(𝐵∗𝑤+ 𝜇). 
4


## Page 4


A  Spatial-­temporal  3D  Human  Pose  Reconstruction  Framework  
 
4  |  J  Inf  Process  Syst, 
  Pose-angle Limits model and OMP algorithm are integrated in the first stage of our framework to 
estimate a single 3D human pose for each 2D pose input frame. While OMP algorithm tends to 
minimize projection error, Pose-angle Limits model try to eliminate invalid poses based on pre-trained 
3D pose dataset. 
 
3.3  Temporal  Models  
 
  Many approaches have been proposed on topics of 3D human pose reconstruction, but they almost 
focus on single frame, in other words, only intra-frame relationship is used. In fact, borrowing idea from 
video coding, it is obvious that consecutive frames always have a high correlation, then consecutive 3D 
skeletons should also have a high correlation. From this point of view, we propose a novel approach 
using temporal models to utilize the inter-frame relationship. Those temporal models are not only 
reduce the high frequency joint movements, but also smooth the actions. 
  Given a sequence of N frames 3D skeleton (15 joints model), we consider each joint 3D coordinate 
(𝑥,𝑦, 𝑧) as discrete-time signals S. 
𝑆= (𝑆$,𝑆T,…, 𝑆X). 
5 
In order to smooth sequence of 3D skeleton, we basically apply temporal models to all the discrete-time 
signals S length N. In this study, four temporal models are implemented, including Simple, Exponential, 
Weighted and Modified Moving Average. 
 
3.3.1  Simple  Moving  Average  
 
  The most basic Simple Moving Average (SMA) is averaging signal from the left most period with a 
chosen sliding window size 𝑤. SMA is mathematically simple, but it efficiently removes high 
frequency data. The bigger number of 𝑤, the smoother the SMA. 
	
  𝑆Y
Z[\ = ]
𝑆Y,
𝑡∈[1, 𝑤]
𝑆Y + 𝑆Y_$ + ⋯+ 𝑆Y_a + 1
𝑤
,
𝑡∈[𝑤+ 1,𝑁].	
   
 
6 
where 
S indicates a length N signal; 
𝑤 is a pre-defined window size. 
 
3.3.2    Exponential  Moving  Average  
 
   Exponential moving averages are another form of weighted averaging. EMA allows user control data 
smoothness by adjusting either window size parameter w or smoothing factor α ∈	
  [0,1]. In this paper, 
we use smooth factor of 𝛼=
T
ad$, following formula below: 
 
𝑆Y
e[\ = f
𝑆Y,
𝑡	
   = 	
  1
(1 −𝛼)𝑆Y_$
e[\ + 𝛼𝑆Y,
𝑡∈(1,𝑁]. 
 
7 
where 
S indicates a length N signal; 
𝑤 is an user-defined window size; 
𝛼=
T
ad$ is smoothing factor. 
 
3.3.3    Weighted  Moving  Average


## Page 5


Xuan  Thanh  Nguyen  *,  Thi  Duyen  Ngo  **  and  Thanh  Ha  Le  **  
 
J  Inf  Process  Syst,  |  5  
  Weighted moving average mathematically is the convolution between data series and a fixed 
weighting function. Basically, weighting function give current data more weight than older data to 
reduce proportionally the implication of previous data points. In this paper, we use weighted function as 
below: 
𝑆Y
a[\ = g
𝑆Y,
𝑡∈[1,𝑤]
𝑤𝑆Y + (𝑤−1)𝑆Y_$ + ⋯+ 2𝑆Y_(a_T) + 1𝑆Y_(a_$)
𝑤+ (𝑤−1) + (𝑤−2) + ⋯+ 2 + 1
,
𝑡∈[𝑤+ 1, 𝑁]. 
 
 
8 
where 
S indicates a length N signal; 
𝑤 is an user-defined window size. 
 
3.3.4    Modified  Moving  Average  
 
  Modified moving average is a short form of exponential moving average, with 𝛼=
$
a. 
𝑆Y
[[\ = ]
𝑆Y,
𝑡	
   = 	
  1
(1 −1
𝑤)𝑆Y_$
[[\ + 1
𝑤𝑆Y,
𝑡∈(1,𝑁]. 
9 
where 
S indicates a length N signal; 
𝑤 is an use-defined window size. 
 
4    Experiments  
  We demonstrate the performance of our framework in 3D human pose reconstruction in three 
experiments. First, we compare our method with state-of-the art methods running on CMU dataset. 
Secondly, we test the normal distribution (Gaussian) noise sensitivity by observing average error versus 
signal-to-noise ratio. Another test uses a Vietnamese Traditional Dace dataset to indicate the 
smoothness of our reconstructed pose sequence. Basically, our proposed method outperform existing 
works with lower Euclidean reconstruction error and producing naturally smooth 3D human pose 
sequence. 
 
4.1    Quantitative  Evaluation  on  CMU  Dataset  
 
CMU  data  acquisition  
 
  We use a subset of 11 sequences (approximate 25 thousands of frames) from the CMU Motion 
Capture Database which was introduced by Carnegie Mellon University [12]. The subset is then 
normalized in several steps. First, we retarget subset motions into a unique skeleton because of CMU 
was performed by multiple actors. As a consequence, all retargeted motion have the same bone lengths. 
Secondly, we convert original rotational skeleton into 3D positional data, selecting 17 major joints, then 
translating local origin of the skeleton (hip joint) to global origin.  
 
Euclidean  comparison  metric  
 
  We use obtained CMU 3D poses as ground-truth, named Sgtr. Beside, a camera model has been 
implemented to orthogonally project 3D skeleton onto a 2D plane, produces images of corresponding 
2D poses, named S2d. Then, we feed projected 2D poses to 3D pose reconstruction frameworks, output


## Page 6


A  Spatial-­temporal  3D  Human  Pose  Reconstruction  Framework  
 
6  |  J  Inf  Process  Syst, 
estimated 3D poses, called Srec. For comparison, we calculate average Euclidean distance between 
reconstructed poses and ground-truth poses correspondingly, as shown in Table 1 and Figure 2. 
  Additionally, ground-truth Sgtr and Reconstruction Srec are both tend to represent a 3D pose, but they 
are likely to have different coordinate because of different camera parameter models. In order to 
overcome this problem, we implemented a Proscrustes Alignment (PA) which determines a linear 
transformation (combination of translation, reflection, orthogonal rotation, and scaling) [13] to conform  
Srec to Sgtr as small dissimilarity as possible.  
 
(𝑃𝐴klmn,𝑃𝐴kopl) = 𝑃𝐴(klmn,kopl), 
𝐸𝑟𝑟= 𝑀𝑒𝑎𝑛(𝐷wxy?ze\{(𝑃𝐴klmn,𝑃𝐴kopl)). 
10 
 
	
   
Results  on  CMU  dataset  
  In this paper, we consider the work of Akhter et al. [4] as the baseline. Table 1 numerically depicts 
joint-by-joint reconstruction error percentages of our temporal frameworks compared to baseline 
method [4]. The lower percentage of error, the better the method is. In total, there are four trials 
including varieties of temporal models: SMA, EMA, WMA and MMA. It is clearly that temporal 
models are useful to smooth the pose sequences and reduce reconstruction errors while four temporal 
models perform better than the baseline. In average, our framework using Modified Moving Average 
(MMA) model have lowest error percentage, about ten percent lower than baseline, as shown in Table 
1. Additionally, Figure 2 specifically indicates joint-by-joint Euclidean reconstruction errors of MMA 
and baseline model visually. 
 
  
Table 1: Reconstruction error percentages comparison joint-by-joint.


## Page 7


Xuan  Thanh  Nguyen  *,  Thi  Duyen  Ngo  **  and  Thanh  Ha  Le  **  
 
J  Inf  Process  Syst,  |  7  
  
Figure 2: Euclidean reconstruction error of our framework using MMA model vs. baseline. 
 
  It is important to mention the smoothness of estimated 3D pose sequences. Due to our temporal model 
takes advantage of inter-frame relationship, reconstructed pose sequence clearly look more natural and 
smooth than others methods, as shown in Figure 3 and Figure 6. 
  
  
Figure 3: Signal smoothing visualization. 
 
4.2    Gaussian  Noise  Sensitivity  
 
  In this experiment, we add Gaussian noise on 2D poses input to check method’s sensitivity against 
noise. Then we observe the change of reconstruction error versus signal-to-noise ratio (SNR in dB). The 
bigger the SNR, the noisier of the signal and the lower reconstruction error, the better the method 
against Gaussian noise. Figure 4 visualizes an original signal and the added noises respectively by


## Page 8


A  Spatial-­temporal  3D  Human  Pose  Reconstruction  Framework  
 
8  |  J  Inf  Process  Syst, 
SNR={ 1, 9, 17} dB. Figure 5 shows the percentage error of our framework versus Akhter et al. [4]. It is 
clear that our method have lower reconstruction error, outperforms others in terms of sensitivity against 
Gaussian noise. 
  
  
Figure 4: Visualization of noisy signals. 
  
 
 
Figure 5: The change of reconstruction error versus Gaussian SNR 
 
4.3    Result  on  Apsara  Vietnamese  Traditional  Dance  Dataset  
  In terms of practical applications, our framework have chances to be tested in a cultural heritage 
preservation project which attempts to protect Vietnamese traditional dances using computer vision


## Page 9


Xuan  Thanh  Nguyen  *,  Thi  Duyen  Ngo  **  and  Thanh  Ha  Le  **  
 
J  Inf  Process  Syst,  |  9  
techniques. This work targets to store, synthesize and render traditional dances not only in single-view 
video, but also in corresponding 3D human poses.  
  In details, our group manually record Apsara’s performances (a Vietnamese traditional dance) in 
format of 2D videos. Then, we use YOLO [14] and Deepcut [9] to estimate 2D actor’s poses from 2D 
recorded videos. YOLO and Deepcut are two state-of-the-art machine learning-based methods for 
character segmentation and 2D pose estimation. Next step, our framework is applied to reconstruct 3D 
poses from 2D poses sequences. Figure 6 the process from 2D video to 3D poses. Our dance’s 
reconstructed 3D pose sequences are reasonable and smooth enough for later synthesis and rendering.  
  
  
Figure 6: Apsara dance 3D pose reconstruction: Upper-parts are 2D poses; Lower-parts are 
corresponding 3D poses. 
5    Conclusion  
  In this paper, we propose a spatial-temporal 3D human pose reconstruction framework. The key idea 
of our approach is combining intra and inter frames relationships in a consecutive pose sequences. 
Orthogonal Matching Pursuit (OMP) algorithm, pre-trained Pose-angle Limits and temporal models 
have been used to estimate 3D poses from 2D poses. Additionally, temporal models can be re-used 
independently as an post-processing step to smooth reconstructed motion sequences in other methods. 
Experiment results on CMU dataset and Vietnamese Traditional Dance clearly show that our 
framework outperform existing methods in terms of Euclidean reconstruction error. In details, using 
Modified Moving Average model, our framework have lower reconstruction error (about 10 percent) 
compare to the baseline [4]. On the other hand, our method have better sensitivity of dealing with 
Gaussian noise. It is also important to mention that our 3D pose sequences are more smooth and 
realistic than others. 
 
 
Acknowledgement  
This research is supported/funded by EU project "Multimedia Application Tools for Intangible 
Cultural Heritage Conservation and Promotion" - H2020-MSCA-RISE ANIAGE (691215) and 
Ministry of Science and Technology Vietnam (ĐTĐL.CN-34/16).


## Page 10


A  Spatial-­temporal  3D  Human  Pose  Reconstruction  Framework  
 
10  |  J  Inf  Process  Syst, 
References  
 
[1]   Nguyen, X. T., Le, T. H., & Yu, H. (2018). Motion Style Extraction Based on Sparse Coding 
Decomposition. arXiv preprint arXiv:1811.06616.  
[2]   Sminchisescu, Cristian, and Bill Triggs. "Building roadmaps of local minima of visual 
models." Computer VisionÑECCV 2002 (2002): 566-582.  
[3]   V. Ramakrishna, T. Kanade, and Y. Sheikh. Reconstructing 3D human pose from 2D image 
landmarks. European Conference on Computer Vision, pages 573Ð586, 2012.  
[4]   Akhter, Ijaz, and Michael J. Black. "Pose-conditioned joint angle limits for 3D human pose 
reconstruction." Proceedings of the IEEE Conference on Computer Vision and Pattern 
Recognition. 2015.  
[5]   C. Sminchisescu and B. Triggs. Estimating articulated human motion with covariance scaled 
sampling. The International Journal of Robotics Research, 22(6):371Ð391, 2003.  
[6]   Kien, H. K., et al. "Single view image based—3D human pose reconstruction." Knowledge 
and Systems Engineering (KSE), 2017 9th International Conference on. IEEE, 2017.  
[7]   J. Chen, S. Nie, and Q. Ji. Data-free prior model for upper body pose estimation and tracking. 
IEEE Trans. Image Proc., 22(12):4627Ð4639, Dec. 2013.  
[8]   J. M. Rehg, D. D. Morris, and T. Kanade. Ambiguities in visual tracking of articulated objects 
using two-and three- dimensional models. The International Journal of Robotics Research, 
22(6):393Ð418, 2003.  
[9]   Pishchulin, Leonid, et al. "Deepcut: Joint subset partition and labeling for multi person pose 
estimation." Proceedings of the IEEE Conference on Computer Vision and Pattern 
Recognition. 2016.  
[10]  Bogo, Federica, et al. "Keep it SMPL: Automatic estimation of 3D human pose and shape 
from a single image." European Conference on Computer Vision. Springer International 
Publishing, 2016.  
[11]  Tekin, Bugra, et al. "Structured prediction of 3D human pose with deep neural networks." 
arXiv preprint arXiv:1605.05180 (2016).  
[12]  http://mocap.cs.cmu.edu/  
[13]  Bookstein, Fred L. Morphometric Tools for Landmark Data. Cambridge, UK: Cambridge 
University Press, 1991.  
[14]  Redmon, Joseph, and Ali Farhadi. "YOLO9000: Better, faster, stronger." arXiv preprint 
arXiv:1612.08242(2016). 
 
 
 
Xuan Thanh Nguyen/ http://orcid.org/0000-­0001-­5464-­0327 
 
He is Ph.D. student at ESIEE Paris, working on mathematical morphology, computer 
vision and machine learning. He received B.S. in Computer Science from  University 
of Engineering  and  Technology,  Vietnam  National  University (UET, VNU),  
Hanoi,  Vietnam  in  2013. He got M.Sc at JAIST-Japan in 2016.  
 
 
Thi Duyen Ngo/  https://orcid.org/0000-0002-1557-9153 
 
Thi Duyen Ngo received her Bachelor degree in Information Technology in 2005 
from University of Engineering and Technology (UET), Vietnam National University 
– Hanoi (VNUH), where she has been working as a lecturer since 2006. She received


## Page 11


Xuan  Thanh  Nguyen  *,  Thi  Duyen  Ngo  **  and  Thanh  Ha  Le  **  
 
J  Inf  Process  Syst,  |  11  
a Ph.D. at UET, VNUH in 2016. Her research interests are speech processing and 
computer vision.  
 
 
 
 
 
 
Thanh Ha Le/ http://orcid.org/0000-­0002-­7288-­0444 
 
Ha  Le  Thanh  received  B.S.  and  M.S.  degrees  in  Information  Technology  from  
the  College  of  Technology,  Vietnam  National  University,  Hanoi  in  2005.  He  
received a Ph.D. at the Department of Electronics Engineering  at  Korea  University.  
In  2010, he joined the Faculty of Information Technology, University of  
Engineering  and  Technology, Vietnam  National University,  Hanoi  as an associate 
professor. His research interests are multimedia processing, coding satellite image  
processing  and  computer  vision.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
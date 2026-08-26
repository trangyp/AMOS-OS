---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1604.03443v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1604.03443v1_Multi-modal_Fusion_for_Diabetes_Mellitus_and_Impaired_Glucose_Regulation_Detecti

> Source: 1604.03443v1_Multi-modal_Fusion_for_Diabetes_Mellitus_and_Impaired_Glucose_Regulation_Detecti.pdf

> Pages: 9

---


## Page 1


JOURNAL OF XX CLASS FILES, VOL. XX, NO. X, XX 2016
1
Multi-modal Fusion for Diabetes Mellitus and
Impaired Glucose Regulation Detection
Jinxing Li, David Zhang, Fellow, IEEE, Yongcheng Li, and Jian Wu
Abstract—Effective and accurate diagnosis of Diabetes Mellitus
(DM), as well as its early stage Impaired Glucose Regulation
(IGR), has attracted much attention recently. Traditional Chinese
Medicine (TCM) [3], [5] etc. has proved that tongue, face and
sublingual diagnosis as a noninvasive method is a reasonable
way for disease detection. However, most previous works only
focus on a single modality (tongue, face or sublingual) for diag-
nosis, although different modalities may provide complementary
information for the diagnosis of DM and IGR. In this paper, we
propose a novel multi-modal classiﬁcation method to discriminate
between DM (or IGR) and healthy controls. Specially, the tongue,
facial and sublingual images are ﬁrst collected by using a non-
invasive capture device. The color, texture and geometry features
of these three types of images are then extracted, respectively.
Finally, our so-called multi-modal similar and speciﬁc learning
(MMSSL) approach is proposed to combine features of tongue,
face and sublingual, which not only exploits the correlation but
also extracts individual components among them. Experimental
results on a dataset consisting of 192 Healthy, 198 DM and
114 IGR samples (all samples were obtained from Guangdong
Provincial Hospital of Traditional Chinese Medicine) substantiate
the effectiveness and superiority of our proposed method for the
diagnosis of DM and IGR, compared to the case of using a single
modality.
Index Terms—Diabetes mellitus (DM), Impaired Glucose Regu-
lation (IGR), multi-modal, tongue image, facial image, sublingual
image.
I. INTRODUCTION
T
HE number of people suffering from diabetes mellitus
(DM) is increasing each year, which is predicted to reach
366 million by 2030 [1], causing disabilities, economic hard-
ship and even death. An accurate diagnosis of DM, especially
for its early stage also known as Impaired Glucose Regulation
(IGR), is becoming more and more important. Until now, the
fasting plasma glucose (FPG) test is a standard method to
diagnose DM in many hospitals. FPG test is performed by
analyzing the patient’s blood glucose level after the patient has
gone at least 12 hours without taking any food. This method
is accurate, but inconvenient and painless. This blood required
detecting method can be consider invasive and slightly painful,
and even has a risk of infection (piercing process).
J. Li is with the Department of Computing, Hong Kong Polytechnic
University, Hung Hom, Kowloon (e-mail: csjxli@comp.polyu.edu.hk).
D. Zhang is with the Department of Computing, Hong Kong Polytechnic
University, Hung Hom, Kowloon (e-mail: csdzhang@comp.polyu.edu.hk).
Y. Li is with the Department of Computer ScienceHarbin Institute
of Technology Shenzhen graduate school, Shenzhen, China (email: liy-
ongchengem@126.com).
J. Wu is with the Department of Computer ScienceHarbin Institute of
Technology Shenzhen graduate school, Shenzhen, China (email: wujian-
hitsz@gmail.com).
Manuscript received XXX; revised XXX.
(a)
(b)
Healthy
DM
Fig. 1.
Example classiﬁcations using Sparse Representation Classiﬁcation.
A green border indicates correct classiﬁcation and a red border represents
incorrect classiﬁcation. The ﬁrst row represents experimental results using
facial images, followed by the tongue images and sublingual images in the
second row and third row of the ’Healthy’ part. So does the ’DM’ part.
In recent years, some works have been done on non-invasive
methods to diagnose speciﬁc diseases by using body surface
features (the tongue, face, and sublingual vein). The human
tongue, face and sublingual vein contain numerous valuable
information that can be used for diagnosis [12], [13], [14],
[15], [16], [17] with color, texture and geometry features being
the most prominent.
The experimental results of disease diagnosis based on
tongue, facial and sublingual images have proved the ef-
fectiveness and reasonability of aforementioned non-invasive
methods. [2] ﬁrst captured a precise facial image for diagnosis
using a chamber with LED light and digital camera. They
established a ﬁve color scale for facial image to measure
the changes caused by internal organs. Wang et al. [2] pro-
posed a mathematically described tongue color space. They
statistically studied main 12 types of color distribution in
tongue with over 9000 tongue images, and their corresponding
experiments illustrated that these colors contributed to the
disease classiﬁcation. In [3], Zhang et al. used facial block
color with sparse representation classiﬁer (SRC) [4] for DM
detection. Moreover, extracted color, texture and geometry
features of tongue feature were exploited to detect DM and
arXiv:1604.03443v1  [cs.CV]  12 Apr 2016


## Page 2


JOURNAL OF XX CLASS FILES, VOL. XX, NO. X, XX 2016
2
nonproliferative diabetic retinopathy (DR) [5]. A heart disease
diagnostic system based on facial color [18] was proposed.
Five facial blocks were extracted from the facial image to
detect hepatitis in [19], and the average accuracy achieved
73.6% using the average RGB pixel intensities features. Zhang
and Wang etc. [23] took both color and texture features into
account for computerized facial diagnosis.
However, despite of various tongue, face or sublingual
diagnosis methods proposed for disease detection, most of
them regarded either tongue, face or sublingual vein as an
independent one and ignored the relationship among them
which may have an effect on the overall classiﬁcation per-
formance. As shown in Fig. 1, it is easy to see that some
healthy or DM samples can not be classiﬁed with tongue
features but facial features or sublingual features do. Similarly,
some samples can be detected by the tongue task or the
sublingual task but the facial task is unable. In particular, some
patients are difﬁcult to be diagnosed with tongue, face and
sublingual vein (e.g., the last column in ’Healthy’ part of Fig.
1), while a combination of these tasks may have a possibility
for accurate diagnosis. Thus, an effective exploitation of the
complementary information is beneﬁcial for the diagnosis of
diseases. A naive way of taking the tongue, face and sublingual
vein into account is to concatenate these three task vectors as a
single one. However, it is not an efﬁcient way since these three
modalities are different. Furthermore, the concatenated feature
dose not exploit the cross correlated information among the
original data. Therefore, it is necessary to have a research
in modal combination with the tongue, facial and sublingual
tasks.
In this paper, we propose a novel multi-modal classiﬁer
to discriminate between DM (or IGR) and healthy controls.
In particular, our proposed method jointly represents three
modal features obtained from tongue, facial and sublingual
images and shares a similarity between them. In addition,
consider differences between those tasks which contain use-
ful information for classiﬁcation, we also extract individual
components that keeps the diversity between them. In this
case, both similarity and distinctiveness of multiple modalities
are exploited, being beneﬁcial for the disease detection. An
optimal algorithm based on Linearized Alternating Directions
Method (LADM) [24] and Augmented Lagrangian Multiplier
(ALM) method [6] is applied to solve the presented strategy.
The rest of this paper is organized as follows. In Section
2, we brieﬂy describe our previous work including the image
capture device and the corresponding feature extraction. In
Section 3, we analyzes the proposed multi-modal classiﬁer.
Section 4 illustrates the experimental results, followed by
concluding remarks in Section 5.
II. IMAGE CAPTURE DEVICE AND FEATURE EXTRACTION
In this section, we will ﬁrst introduce the image capture
device of the tongue, face and sublingual vein, and then
describe the feature extraction of these three types of images.
A. Tongue and Facial Capture Device
The image capture (tongue, face and sublingual) device is
shown in Fig. 2. consisting of a SONY 3-CCD video camera
45°
Human
Tongue 
or face
Fluorescent lamp
Video
Camera
Fluorescent lamp
(a)
(b)
Fig. 2.
Image capture device. (a) Viewing geometry and imaging path of
the imaging device. (b) Appearance of the device and the system.
placed in the center and two D65 ﬂuorescent tubes situated
symmetrically on either sides of the camera in order to produce
a uniform illumination. Particularly, the angle between the
incident light and emergent light is 45 (shown in Fig. 2(a)),
recommended by Commission Internationale de l’Eclairage
(CIE). For the tongue and sublingual image capture, patients
placed their chin on a chin rest and show their tongue to the
camera (shown in Fig. 2(b)), while for the facial image capture,
patient placed their chin on a chin rest and show their face to
the camera (change the height or position of the chin rest to
obtain the tongue, facial and sublingual images). Each image
saved in JPEG format with 640×480 size is color corrected
[20] to eliminate any variability in color images caused by
changes of the illumination and device dependence. Using this
correction model, original tongue, facial and sublingual images
are corrected, and pixels are transformed in the standard RGB
(sRGB) color space.
B. Feature Extraction
In our previous work [3], [5], we have proposed a method to
extract color, texture and geometry features of the three types
of images. In this subsection, we will brieﬂy introduce them.
It should be noted that refer to [21], four blocks with 64×64
size strategically located around the face are extracted, which
contain the information of the health status of the human.
Details of the location of blocks can be found in [30]. Both
color and texture extraction for facial images are based on
these blocks. Similarly, we also have deﬁned eight blocks
with 64×64 size for tongue texture feature extraction. More
details can be found in [5]. For the sublingual images, the
main domain about the vein is ﬁrst decomposed and its color
and geometry features are then extracted.
1) Color Feature: The RGB values of captured tongue
or facial images are ﬁrst calculated and then converted to
CIEXYZ 

X
Y
Z

=


0.4124
0.3576
0.1805
0.2126
0.7152
0.0722
0.0193
0.1192
0.9505




R
G
B


(1)
followed by CIEXYZ to CIELAB [?]
L = 166f(Y/Y0) −16
a = 500[f(X/X0) −f(Y/Y0)]
b = 200[f(Y/Y0) −f(Z/Z0)]
(2)


## Page 3


JOURNAL OF XX CLASS FILES, VOL. XX, NO. X, XX 2016
3
where X0, Y0 and Z0 are the CIEXYZ tristimulus values of
the reference white point; f(x) = x1/3 if x > 0.008856 or
f(x) = 7.787x + 16/116 if x ≤0.008856.
We then compare the obtained LAB values with 12 pre-
deﬁned colors for the tongue [5], 6 predeﬁned colors for
the face [3] and 6 predeﬁned colors (the method of deﬁning
these colors is same in the three types of images) for the
sublingual vein to assign the color value which is closest to
it using Euclidean distance. After evaluating all tongue, facial
or sublingual pixels, the total of each color is summed and
divided by the total number of pixels. We regard these ratios as
the color feature. For tongue image, we statistically extract 12
different colors as the feature. Thus, a 12 dimensional vector
for the tongue is obtained. Similarly, we select 6 different
colors and 6 different colors for face and sublingual (more
detailed color feature extraction for sublingual images will be
published soon), respectively. Finally, a 6 dimensional vector
for each block of the face and a 6 dimensional vector for the
sublingual vein are acquired.
2) Texture Feature: The 2-D Gabor ﬁlter is applied to
calculate the texture of each block.
Gk(x, y) = exp
 
x
′2 + γ2y
′2
−2σ2
!
cos

2π x′
λ

(3)
where x′ = x cos θ + y sin θ, y′ = −x sin θ + y, θ is the
orientation, γ is the aspect ratio of the sinusoidal function, σ
is the variance, and λ is the wavelength. A response Rk(x, y)
is produced by convolving each ﬁlter with a texture block.
Rk(x, y) = Gk(x, y) ∗im(x, y)
(4)
where the symbol ∗denotes 2-D convolution and the func-
tion im(x, y) represents the texture block. Then the max-
imum pixel intensity is selected following FR(x, y)
=
max(R1(x, y), · · · , Rn(x, y)). Apart from the texture value
of each block, we also add the mean of these values as an
additional texture value. Thus, we can get a 9 dimensional
vector for the tongue and 5 dimensional vector for each block
of the face.
3) Geometry Feature: Statistically, a person who suffers
from DM or IGR would affect the geometry of the tongue [5]
and the sublingual vein [25]. In our previous work, we have
introduced the details of the geometry feature extraction [5]
and these features are based on measurements, distances, areas,
and their ratios. For tongue images, 13 geometry features
are selected (width, length, length-width ratio, smaller half-
distance, center distance, center distance ratio, area, circle
area, circle area ratio, square area, square area ratio, triangle
area, and triangle area ratio). For sublingual images (more
detailed geometry feature extraction for sublingual images
will be published soon), 6 geometry features are selected
(length, width, length ratio of each side vein). Note that, before
extracting the geometry feature of sublingual images, we ﬁrst
decompose the image to get the sublingual vein.
III. MULTI-MODAL SIMILAR AND SPECIFIC LEARNING
A general framework for multi-modal fusion is proposed in
this section. Before introducing our proposed method, we ﬁrst
brieﬂy review the sparse representation classiﬁer (SRC).
A. Sparse Representation Classiﬁer
Given a set of training samples and a test sample, the main
idea of SRC is that the test sample is represented as a linear
combination of the training samples, and the representation
coefﬁcients are required to be as sparse as possible. In practice,
the l1-norm minimization is applied to ensure the sparsest
linear representation of the test sample over the training
samples. Suppose that matrix D = [D1, D2, ·, ·, ·, DJ] called
dictionary is the set of training samples, where J is the number
of classes, Di ∈Rm×ni is the training set of the i-th class
with m dimension and ni samples. Each column in D is called
atom. A test sample y can be denoted by
ˆα = min
α ∥y −Dα∥2
F + λ ∥α∥1
(5)
where λ is the penalty parameter, ∥·∥F is the Frobenius norm
and ∥·∥1 is l1 norm. ˆα = [ ˆα1; ˆα2; · · ·; ˆαJ] is the sparse
coefﬁcient, and ˆαi is the sparse coefﬁcient corresponding to
Di.
If the test sample y is from class i, then it can be well
represented by the training samples from i-th class. In other
words, among its representation coefﬁcients ˆα over all the
training samples, only coefﬁcients in class i will be signiﬁcant
while others will be insigniﬁcant. Then the class label of the
test sample is determined by the following Eq. (6)
i∗= min ∥y −Di ˆαi∥2
F
(6)
More information about the SRC can be found in [4].
B. Multi-Modal Similar and Speciﬁc Learning Model
As mentioned above, different modal or feature vectors from
a same sample may share some similarity. It is reasonable to
assume that representation coefﬁcients coded on their asso-
ciated dictionaries of different modalities should be similar
which would make the representation stable. For example, a
test sample, containing tongue modality, facial modality and
sublingual modality, is represented as a linear combination of
the training samples; since all tasks are belonging to a same
sample, they will be well represented by the training samples
of their corresponding class, and hence the position and values
of signiﬁcant coefﬁcients are similar. To achieve the above
goal, we use [7] the following term to achieve the similarity
of different modalities .
min
αk
K
X
k=1
∥αk −¯α∥2
F
(7)
where αk is the representation coefﬁcient of the k-th modality
and ¯α =
1
K
PK
k=1 αk is the mean vector of all αk (K
is the number of different types of modalities). It is easy
to see that Eq. (7) aims to reduce the variance of different
representation coefﬁcients αk, making them similar to each
one. However, this assumption is too restrictive since there is
also distinctiveness among them. Therefore, it is necessary to
not only exploit the similarity among all tasks but also keep
the ﬂexibility of each task. In this case, the balance between
similarity and distinctiveness among all tasks will represent the


## Page 4


JOURNAL OF XX CLASS FILES, VOL. XX, NO. X, XX 2016
4
]
,
,
,
[
1
1
2
1
1
1
1
n
d
d
d
D


Feature extraction
1
y
3
y
+
+
[
]
[
]
1
D
1
y =
=
similarity




K
k
j
s
k
j
c
k
j
k
k D
w
j
1
,
,
*
)
(


Classification
Multi-modal 
training
Sparse 
Representation
Multi-modal 
Classification
distinctiveness
]
,
,
,
[
2
2
2
2
1
2
2
n
d
d
d
D


2
D
2
y
]
,
,
,
[
3
3
2
3
1
3
3
n
d
d
d
D


+
[
]
=
3
D
3
y
Fig. 3.
The framework of our proposed method MMSSL. MMSSL contains three parts: multi-modal training, sparse representation and multi-modal
classiﬁcation. Firstly, the dictionary consists of training samples; secondly, multi-modal features of a given test sample is represented sparsely with the
dictionary, and the representation coefﬁcients are divided into two parts which are common components and individual components; thirdly, the label of the
test sample is decided according to the total reconstruction error.
original sample more stable and accurate which is beneﬁcial
for classiﬁcation.
To address aforementioned problem, we divide the represen-
tation coefﬁcients αk into two parts: the similar part and the
modal-speciﬁc part. Speciﬁcally, αk = αc
k + αs
k, where αc
k
denotes the similarity, while αs
k denotes the distinctiveness.
The framework of our proposed method is shown in Fig. 3.
The formulation of our model is
min
K
X
k=1
n
∥yk −Dk (αc
k + αs
k)∥2
F + τ ∥αc
k −¯αc∥2
F
o
+
K
X
k=1
λ (∥αc
k∥1 + ∥αs
k∥1)
(8)
where yk is the test sample, Dk = [D1
k, D2
k, ·, ·, ·, DJ
k] is train-
ing samples of the k-th task, and Di
k ∈Rmk×ni
k is the training
set of the k-th task of the i-th class with mk dimension and
ni
k samples; ¯αc =
1
K
PK
k=1 αc
k is the mean value of similar
sparse representation coefﬁcients of all tasks, and τ and λ
are the non-negative penalty constants. From Eq. (8), we can
see that our model aims to extract the similar components of
each task through xc
k, while also keeps individual components
of each task through xs
k. Note that at the step of exploiting
correlation, we do not directly set each αc
k to be equal, but
instead of minimizing the distance between them. This way
also makes our approach more ﬂexible. In addition, consider
the test sample would be linearly represented by atoms of the
dictionary belonging to its own class, we apply l1 norm on
both αc
k and αs
k.
C. Optimization of MMSSL
We alternatively update the similar coefﬁcients αc
k and
special coefﬁcient αs
k. For example, we update αc
k by ﬁxing
αs
k, and vice versa.
Update αc
k: By ﬁxing αs
k, the optimization solution of Eq.
(8) with respect to αc
k equals to the following problem
αc
k = arg min ∥yk −Dk (αc
k + αs
k)∥2
F + τ ∥αc
k −¯αc∥2
F
+ λ ∥αc
k∥1
(9)
we apply Augmented Lagrangian method (ALM) algorithm to
modify Eq. (9).
Applying the ALM, the problem of (9) can be modiﬁed as
follows.
αc
k = arg min ∥yk −Dk (αc
k + αs
k)∥2
F + τ ∥αc
k −¯αc∥2
F
+ λ


αc
k
′

1 + µ
2




αc
k −αc
k
′ + zk
µ




2
F
(10)
where αc
k
′ is the relaxed variable, zk is the k-th lagrangian
multiplier, and µ is the step value. Then we can optimize αc
k
and αc
k
′ alternatively.
(a) Firstly, we ﬁx αc
k
′ to get αc
k
αc
k = arg min ∥yk −Dk (αc
k + αs
k)∥2
F + τ ∥αc
k −¯αc∥2
F
+ µ
2




αc
k −αc
k
′ + zk
µ




2
F
(11)
Follow the Ref. [7], a closed-form solution of αc
k can be
derived:
αc
k = αc
0,k + τ
K PkQ
K
X
η=1
αc
0,η
(12)
where Pk = (DT
k Dk + (τ + µ
2 )I)−1, αc
0,k = Pk(DT
k (yk −
Dkαs
k) + µ
2 αc′
k −zk
2 ), and Q = (I −τ
K
PK
η=1 Pη)−1.
(b) Secondly, after ﬁxing αc
k, the optimization solution of
Eq. (10) can be reduced to Eq. (13) at the step of updating
αc
k
′.
αc
k
′ = arg min λ


αc
k
′

1 + µ
2




αc
k −αc
k
′ + zk
µ




2
F
(13)


## Page 5


JOURNAL OF XX CLASS FILES, VOL. XX, NO. X, XX 2016
5
Algorithm 1 Algorithm of updating αs
k in MMSSL
Input: σ, γ = λ/2, yk, Dk, and αc
k, k = 1, · · · , K
Initialization: ˜αs(1)
k
= 0 and h = 1,
1: for k = 1, ..., K do
2:
while not converged do
3:
h=h+1
4:
˜αs(1)
k
=Sγ/σ

˜αs(h−1)
k
−1
σ ▽F( ˜αs(h−1)
k
)

where ▽F( ˜αs(h−1)
k
) is the derivative of the left of Eq.
(15) ∥yk −Dk(αc
k + αs
k)∥2
F , and Sγ/σ is a soft threshold
operator that deﬁned in Eq. (14);
5:
end while
6: end for
Output: αs
k = ˜αs(h)
k
, k = 1, · · · , K
Algorithm 2 Multi-Modal Similar and Special Learning
(MMSSL)
Input: λ, τ, yk, Dk, k = 1, · · · , K
Initialization: αc
k= 0, αs
k= 0,
1: while not converged do
2:
Update coefﬁcients αc
k: ﬁx αs
k
(a) compute αc
k following Eq. (12)
(b) compute αc
k
′ following Eq. (13)
(c) zk = zk + µ(αc
k −αc
k
′)
3:
Update coefﬁcients αs
k: ﬁx αc
k, and solve αs
k following
Algorithm 1
4: end while
Output: αc
k and αs
k k = 1, · · · , K
Then αc
k
′ could be derived by operating Threshold(αc
k +
zk
µ , λ
µ). The operation of soft threshold is shown as follows.

Sλ/µ(β)

i =

0
|βj| ≤λ/µ
βi −sign(βi)λ/µ
otherwise
(14)
where βi means the value of the i-th component of β. After
getting αc
k and αc
k
′, zk and µ can be updated following zk =
zk + µ(αc
k −αc
k
′) and µ = 1.2µ.
Update αs
k: After acquiring αc
k, the optimization of Eq. (9)
can be reformulated to Eq. (15) at the step of updating αs
k.
αs
k = arg min ∥yk −Dk(αc
k + αs
k)∥2
F + λ ∥αs
k∥1
(15)
In fact, there are many methods to tackle the problem (13). For
example, both ALM and Iterative Projection Method (IPM) [9]
could deal with it. In this paper, we use IPM to address Eq.
(13), as described in Algorithm 1.
The complete algorithm of MMSSL is summarized in
Algorithm 2. Note that, since we introduce a new variable
αc′
k at the step of updating αc
k, another reasonable way is that
we could alternatively update αc′
k and αc
k until convergence,
and then get the solution of αc
k. At this time, the value of αc
k
and αc′
k is similar.
D. The Classiﬁcation Rule of MMSSL
After obtaining the representation coefﬁcients, the decision
is ruled in favor of the class with total lowest reconstruction
residual over all K tasks.
j∗= min
K
X
k=1
wk


yk −Dk,j(αc
k,j + αs
k,j)


2
F
(16)
where Dk,j, αc
k,j and αs
k,j are the elements of the dictionary
Dk, the similar coefﬁcient αc
k and the speciﬁc coefﬁcient
αj
k of j-th category, respectively; wk is the weight value
corresponding to the k-th task, which could be obtained by
exploiting the method mentioned in [8].
IV. EXPERIMENTAL RESULTS
In this section, we conduct two types of experiments.
Healthy versus DM classiﬁcation is ﬁrst provided. Then we
present the numerical results of Healthy versus IGR classiﬁ-
cation. In both experiments, KNN [29], SVM [27], [28], SRC
[4], GSRC (group sprase) [26] which are general and effective
classiﬁers are used for each individual modal classiﬁcation.
Without loss of generality, we concatenate different features
of different modalities as a single vector and refer it as tongue
feature, facial feature or sublingual feature, respectively. Thus,
the K in Eq. (8) is equal to 3.
A. Image Dataset
The tongue, facial and sublingual sample database com-
prises 434 samples split into 192 Healthy samples, 198 DM
samples and 114 IGR samples. Each sample has three dif-
ferent modal images including tongue image, facial image
and sublingual image, respectively. All images were captured
at the Guangdong Provincial TCM Hospital, Guangdong,
China, from the early 2014 to the late 2015. Healthy samples
were veriﬁed through a blood test and other examination. If
indicators from these tests fall within a certain range (set by
the Guangdong Provincial TCM Hospital), they were regarded
as healthy. The FPG test was applied to diagnose whether a
sample was suffering from the DM or IGR. When using the
FPG test, all the samples had gone at least 12 hours without
taking any food. For the DM patients, the blood glucose
level was equal or larger than 7.11mmol/L, while the blood
glucose level of IGR samples was between 6.1mmol/L and
7.11mmol/L. All these standard indictors are decided by the
Guangdong Provincial TCM Hospital.
B. Healthy Versus DM Classiﬁcation
We ﬁrst test the performance of our proposed multi-modal
classiﬁcation method in identiﬁcation of DM for healthy
controls, with the tongue, facial and sublingual tasks. We
randomly select the number of training samples from 30
to 100, and the rest samples are used for testing. Fig. 4
illustrates the experimental results of our MMSSL approach,
compared with the strategies using each individual modality
with different classiﬁers. Note that Fig. 4 only shows the
averaged results of 5 independent experiments. It is easy
to see that the combined measurements of tongue, facial
and sublingual features consistently achieve more accurate
discrimination between DM patients and healthy controls.
Particularly, compared with single tongue modal feature, our
method MMSSL achieves about more than 15% accuracy. The
classiﬁcation accuracies obtained MMSSL are gradually rising
with the increasing number of training samples, and they are
all higher than 80%. In contrast, the best accuracy on face
based modality is only close to 80%.


## Page 6


JOURNAL OF XX CLASS FILES, VOL. XX, NO. X, XX 2016
6
(a)
(b)
(c)
Fig. 4.
Comparison of Healthy and DM performance of single-modal and multi-modal classiﬁcation methods. (a) Comparison of our method with the tongue
image based feature. (b) Comparison of our method with the facial image based feature. (c) Comparison of our method with the sublingual image based
feature.
Fig. 5.
ROC curves of different methods and different features for DM
classiﬁcation.
In addition, Fig. 5 further plots the ROC curves of different
classiﬁcation methods for DM detection when the number of
training samples is 70. Note that we only show the ROC
curves of SRC and GSRC methods with the single modality to
compare with our approach. As the output of SRC and GSRC
is reconstruction errors. We use the ratio of different classes
to represent the percentage. From Fig. 5, we can see that the
area covered by MMSSL based ROC curve is obviously larger
than other methods and modalities based curves.
Besides, we also illustrate the maximal and minimal clas-
siﬁcation rate in 5 independent experiments in Table 1. Note
that we only make a comparison between MMSSL and the
best performance on the single modality (face modality in this
experiment). As we can observe from Table 1, the maximal
and minimal rates increase with the increasing number of
training samples. Compared with other methods, our proposed
methods have a visible improvement both in maximal and
minimal accuracies. Specially, when the number of the train-
ing samples reaches 100, the discrimination of maximization
and minimization obtained by MMSSL achieve 89.01% and
84.29% respectively, while the best values acquired by other
approaches are only 83.77% and 75.39%.
Some exemplar results of classiﬁcation on DM and Healthy
are shown in Fig. 6 (the corresponding exemplar results of
SRC are shown in Fig. 1). As expected, SVM, SRC and
GSRC are capable of discriminating healthy samples using
tongue images, but fail to detect DM patients at many times.
In contrast, SRC and GSRC have a prominent result on
classifying DM using facial images, but fail to detect healthy
samples. Different from aforementioned methods using an
individual modality, our presented approach get an accurate
result of each sample by jointly taking tongue, face and
sublingual into account.
C. Healthy Versus IGR Classiﬁcation
In this subsection, we then apply our proposed multi-modal
classiﬁcation method in identiﬁcation of IGR for healthy
controls, with the tongue, facial and sublingual tasks, and make
a comparison between MMSSL and other existing methods.
Similar with the experiment on DM detection, the number of
training samples from 30 to 70 are randomly selected with
5 times, and the rest samples are used for testing. Fig. 7
illustrates the averaged experimental results of our MMSSL
approach, compared with the strategies using each individ-
ual modality with different classiﬁers. Our presented multi-
modal classiﬁcation strategy accomplishes a prominent rise
in classiﬁcation accuracy compared with other methods based
on tongue, facial or sublingual features. For comparison with
SVM, SRC and GSRC on sublingual features, the proposed
method also get a slight enhancement in the averaged accuracy.
Specially, the rate arrives at 76.68% after combination with
tongue, facial and sublingual tasks, while SVM with the


## Page 7


JOURNAL OF XX CLASS FILES, VOL. XX, NO. X, XX 2016
7
TABLE I
THE MAXIMAL AND MINIMAL CLASSIFICATION RATE IN 5 INDEPENDENT EXPERIMENTS FOR DM DETECTION.
Training samples
Methods
Value
30
40
50
60
70
80
90
100
MMSSL
max
84.29%
83.28%
84.88%
85.98%
86.06%
86.15%
86.73%
89.01%
min
77.34%
79.10%
80.76%
80.07%
82.27%
83.35%
80.57%
84.29%
K-NN (face)
max
75.23%
74.59%
74.23%
74.91%
75.30%
78.79%
76.78%
75.92%
min
68.88%
64.31%
64.60%
67.53%
68.92%
68.40%
69.67%
69.63%
libSVM (face)
max
77.95%
78.78%
81.10%
79.70%
82.07%
82.68%
81.52%
83.77%
min
72.81%
71.38%
72.85%
75.28%
73.71%
73.59%
76.30%
74.87%
SRC (face)
max
76.13%
78.14%
78.35%
78.60%
76.89%
79.22%
80.57%
79.58%
min
65.86%
66.56%
74.23%
69.37%
68.92%
66.67%
72.99%
72.25%
GSRC (face)
max
74.92%
78.78%
79.04%
81.55%
79.28%
82.25%
81.99%
82.72%
min
71.60%
70.10%
73.20%
74.17%
73.71%
69.26%
75.83%
75.39%
TABLE II
THE MAXIMAL AND MINIMAL CLASSIFICATION RATE IN 5 INDEPENDENT EXPERIMENTS FOR IGR DETECTION.
Training samples
Methods
Value
30
40
50
60
70
MMSSL
max
75.30%
77.97%
77.29%
79.14%
81.44%
min
70.85%
70.48%
73.91%
73.80%
73.05%
K-NN (sublingual)
max
71.90%
67.52%
69.76%
66.84%
69.46%
min
64.35%
60.77%
60.14%
57.75%
57.08%
libSVM (sublingual)
max
68.83%
72.69%
73.91%
77.01%
77.84%
min
66.40%
68.28%
71.50%
72.19%
74.25%
SRC (sublingual)
max
76.44%
74.89%
75.36%
79.68%
79.64%
min
69.18%
63.44%
69.08%
67.91%
68.86%
GSRC (sublingual)
max
76.92%
74.01%
76.81%
79.68%
78.44%
min
64.37%
66.08%
66.67%
66.84%
70.06%
Fig. 8.
ROC curves of different methods and different features for IGR
classiﬁcation.
sublingual task, which obtains the best result in all individual
modalities, only performs 75.87%.
The ROC curves of different classiﬁcation methods for
IGR diagnosis when the number of training samples reaches
70 is plotted in Fig. 8. Similarly, we only show the ROC
curves of SRC and GSRC methods with the single modality
to compare with our approach. The ROC curves demonstrate
that the MMSSL has further performance compared with SRC
(tongue), GSRC (tongue) and SRC(sublingual). Additionally,
there is a slight improvement acquired by the MMSSL than
that of GSRC (sublingual), GSRC (face) and SRC (face).
Table 2 illustrates the maximal and minimal classiﬁca-
tion rates in 5 independent experiments for IGR diagnosis.
Similarly, only a comparison between MMSSL and the best
performance on the single modality (sublingual modality in
this experiment) is shown. Although at some times SVM have
a better result than ours, our method carries out the best values
of both maximization and minimization in most conditions.
When the number of training samples is 70, the accurate
discrimination is 81.44% which is a slightly higher than that
of SVM whose value is 79.64%.
V. CONCLUSION
In this paper, a multi-modal fusion method for the Dia-
betes Mellitus and Impaired Glucose Regulation detection is
proposed. The tongue, face and sublingual images are ﬁrst


## Page 8


JOURNAL OF XX CLASS FILES, VOL. XX, NO. X, XX 2016
8
Healthy
DM
GSRC
libSVM
KNN
MMSSL
Fig. 6.
Example classiﬁcation results of various classiﬁcation methods on the individual modality for healthy and DM diagnosis. For each image, the red
border indicates incorrect classiﬁcation, and the green border indicates correct classiﬁcation. KNN, SVM and GSRC fail in some images. In contrast, MMSSL
has successfully classiﬁed all images. Particularly, MMSSL can also detect some samples that can not be classiﬁed by other methods with the individual
modality.
captured by using a non-invasive capture device. Different
features of these three types of images are then extracted. In
order to exploit the correlation among them, we propose a
novel fusion method to learn the common components and
speciﬁc components of different modalities. Two types of
experiments in identiﬁcation of DM (or IGR) from healthy
controls are conducted. The experimental results substantiate
the effectiveness and superiority of our fusion method, com-
pared with the case of using a single modality.
ACKNOWLEDGMENT
The work is partially supported by the GRF fund from
the HKSAR Government, the central fund from Hong
Kong Polytechnic University, the NSFC fund (61332011,
61272292, 61271344) and Shenzhen Fundamental Research
fund (JCYJ20150403161923528, JCYJ20140508160910917).
REFERENCES
[1] World Health Organization, Prevention of blindness from diabetes melli-
tus,World Health Organization, 2006.


## Page 9


JOURNAL OF XX CLASS FILES, VOL. XX, NO. X, XX 2016
9
(a)
(b)
(c)
Fig. 7.
Comparison of Healthy Vs IGR performance of single-modal and multi-modal classiﬁcation methods. (a) Comparison of our method with tongue
image based feature. (b) Comparison of our method with facial image based feature. (c) Comparison of our method with sublingual image based feature.
[2] Wang X, Zhang B, Yang Z, et al, Statistical analysis of tongue images for
feature extraction and diagnostics,Image Processing, IEEE Transactions
on, 2013, 22(12): 5336-5347.
[3] Zhang B, Kumar B V K, Zhang D, Noninvasive diabetes mellitus
detection using facial block color with a sparse representation classiﬁer,
Biomedical Engineering, IEEE Transactions on, 2014, 61(4): 1027-1033.
[4] Wright J, Yang A Y, Ganesh A, et al, Robust face recognition via
sparse representation,Pattern Analysis and Machine Intelligence, IEEE
Transactions on, 2009, 31(2): 210-227.
[5] Zhang B, Kumar B V K, Zhang D, Detecting diabetes mellitus and
nonproliferative diabetic retinopathy using tongue color, texture, and
geometry features,Biomedical Engineering, IEEE Transactions on, 2014,
61(2): 491-501.
[6] Lin Z, Chen M, Ma Y, The augmented lagrange multiplier method
for exact recovery of corrupted low-rank matrices,arXiv preprint
arXiv:1009.5055, 2010.
[7] Yang M, Zhang L, Zhang D, et al, Relaxed collaborative representa-
tion for pattern classiﬁcation,Computer Vision and Pattern Recognition
(CVPR), 2012 IEEE Conference on. IEEE, 2012: 2224-2231.
[8] Yuan X T, Liu X, Yan S, Visual classiﬁcation with multitask joint sparse
representation,Image Processing, IEEE Transactions on, 2012, 21(10):
4349-4360.
[9] Rosasco L, Verri A, Santoro M, et al, Iterative projection methods for
structured sparsity regularization,2009.
[10] Shu T, Zhang B, Non-invasive Health Status Detection System Using
Gabor Filters Based on Facial Block Texture Features,Journal of medical
systems, 2015, 39(4): 1-8.
[11] Pang B, Zhang D, Li N, et al, Computerized tongue diagnosis based on
Bayesian networks,Biomedical Engineering, IEEE Transactions on, 2004,
51(10): 1803-1810.
[12] Zhang D, Pang B, Li N, et al, Computerized diagnosis from tongue ap-
pearance using quantitative feature classiﬁcation,The American Journal
of Chinese Medicine, 2005, 33(06): 859-866.
[13] Zhang Y, Liang R, Wang Z, et al, Analysis of the color characteristics
of tongue digital images from 884 physical examination cases,Journal
of Beijing University of Traditional Chinese Medicine, 2005, 28(001):
73-75.
[14] Su W, Xu Z, Wang Z, et al, Objectiﬁed study on tongue images
of patients with lung cancer of different syndromes,Chinese Journal of
Integrative Medicine, 2011, 17: 272-276.
[15] Huang B, Wu J, Zhang D, et al, Tongue shape classiﬁcation by geometric
features,Information Sciences, 2010, 180(2): 312-324.
[16] Li B, Huang Q, Lu Y, et al, A method of classifying tongue colors
for traditional chinese medicine diagnosis based on the CIELAB color
space,Medical Biometrics. Springer Berlin Heidelberg, 2008: 153-159.
[17] Li C H, Yuen P C, Tongue image matching using color content,Pattern
Recognition,2002, 35(2): 407-419.
[18] Kim B, Lee S, Cho D, et al, A proposal of heart diseases diagnosis
method using analysis of face color,Advanced Language Processing and
Web Information Technology, 2008. ALPIT’08. International Conference
on. IEEE, 2008: 220-225.
[19] Liu M, Guo Z, Hepatitis diagnosis using facial color image,Medical
Biometrics. Springer Berlin Heidelberg, 2008: 160-167.
[20] Wang X, Zhang D, An optimized tongue image color correction
scheme,Information Technology in Biomedicine, IEEE Transactions on,
2010, 14(6): 1355-1364.
[21] Maciocia G, The foundations of Chinese medicine,Churchill Livingstone,
1989.
[22] Zhang H Z, Wang K Q, Jin X S, et al, SVR based color calibration for
tongue image,Machine Learning and Cybernetics, 2005. Proceedings of
2005 International Conference on. IEEE, 2005, 8: 5065-5070.
[23] Zhang B, Wang X, Karray F, et al, Computerized facial diagnosis using
both color and texture features,Information Sciences, 2013, 221: 49-59.
[24] Lin Z, Liu R, Su Z, Linearized alternating direction method with adap-
tive penalty for low-rank representation,Advances in neural information
processing systems. 2011: 612-620.
[25] Chiu C C, Lan C Y, Chang Y H, Objective assessment of blood stasis
using computerized inspection of sublingual veins,Computer methods and
programs in biomedicine, 2002, 69(1): 1-12.
[26] Bengio S, Pereira F, Singer Y, et al, Group sparse coding,Advances in
neural information processing systems. 2009: 82-89.
[27] Hsieh C J, Chang K W, Lin C J, et al, A dual coordinate descent
method for large-scale linear SVM,Proceedings of the 25th international
conference on Machine learning. ACM, 2008: 408-415.
[28] Fan R E, Chang K W, Hsieh C J, et al, LIBLINEAR: A library for large
linear classiﬁcation,The Journal of Machine Learning Research, 2008, 9:
1871-1874.
[29] Cover
T
M,
Hart
P
E,
Nearest
neighbor
pattern
classiﬁca-
tion,Information Theory, IEEE Transactions on, 1967, 13(1): 21-27.
[30] Wang X, Zhang B, Guo Z, et al, Facial image medical analysis system
using quantitative chromatic feature,Expert Systems with Applications,
2013, 40(9): 3738-3746.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
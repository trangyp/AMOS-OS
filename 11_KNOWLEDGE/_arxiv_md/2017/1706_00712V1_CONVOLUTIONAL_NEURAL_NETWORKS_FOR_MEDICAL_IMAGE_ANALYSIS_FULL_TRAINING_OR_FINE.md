---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1706.00712v1
source: arxiv
tags: [arxiv, fractal, knowledge, math, reference]
---
# 1706.00712v1_Convolutional_Neural_Networks_for_Medical_Image_Analysis__Full_Training_or_Fine_

> Source: 1706.00712v1_Convolutional_Neural_Networks_for_Medical_Image_Analysis__Full_Training_or_Fine_.pdf

> Pages: 17

---


## Page 1


1
Convolutional Neural Networks for Medical Image
Analysis: Full Training or Fine Tuning?
Nima Tajbakhsh∗, Member, IEEE, Jae Y. Shin∗, Suryakanth R. Gurudu, R. Todd Hurst, Christopher B. Kendall,
Michael B. Gotway, and Jianming Liang, Senior Member, IEEE
Abstract—Training
a
deep
convolutional
neural
network
(CNN) from scratch is difﬁcult because it requires a large amount
of labeled training data and a great deal of expertise to ensure
proper convergence. A promising alternative is to ﬁne-tune a
CNN that has been pre-trained using, for instance, a large set
of labeled natural images. However, the substantial differences
between natural and medical images may advise against such
knowledge transfer. In this paper, we seek to answer the following
central question in the context of medical image analysis: Can the
use of pre-trained deep CNNs with sufﬁcient ﬁne-tuning eliminate
the need for training a deep CNN from scratch? To address this
question, we considered 4 distinct medical imaging applications
in 3 specialties (radiology, cardiology, and gastroenterology)
involving classiﬁcation, detection, and segmentation from 3 dif-
ferent imaging modalities, and investigated how the performance
of deep CNNs trained from scratch compared with the pre-
trained CNNs ﬁne-tuned in a layer-wise manner. Our experiments
consistently demonstrated that (1) the use of a pre-trained CNN
with adequate ﬁne-tuning outperformed or, in the worst case,
performed as well as a CNN trained from scratch; (2) ﬁne-tuned
CNNs were more robust to the size of training sets than CNNs
trained from scratch; (3) neither shallow tuning nor deep tuning
was the optimal choice for a particular application; and (4) our
layer-wise ﬁne-tuning scheme could offer a practical way to reach
the best performance for the application at hand based on the
amount of available data.
Index Terms—carotid intima-media thickness; computer-aided
detection; convolutional neural networks; deep learning; ﬁne-
tuning; medical image analysis; polyp detection; pulmonary
embolism detection; video quality assessment.
An accepted version of N. Kajbakhsh, J. Y. Shin, S. Gurudu, R. T. Hurst, C. B. Kendall, M. B. Gotway, and J. Liang. “Convolutional neural networks for
medical image analysis: Full training or ﬁne tuning?” IEEE Transactions on Medical Imaging. 35(5):1299-1312, 2016
I. INTRODUCTION
Convolutional neural networks (CNNs) have been used in
the ﬁeld of computer vision for decades [1]–[3]. However,
their true value had not been discovered until the ImageNet
competition in 2012, a success that brought about a revolution
through the efﬁcient use of graphics processing units (GPUs),
rectiﬁed linear units, new dropout regularization, and effective
data augmentation [3]. Acknowledged as one of the top 10
breakthroughs of 2013 [4], CNNs have once again become a
popular learning machine, now not only within the computer
N. Tajbakhsh, J. Y. Shin, and J. Liang are with the Department of
Biomedical Informatics, Arizona State University, 13212 East Shea Boule-
vard, Scottsdale, AZ 85259, USA (e-mail: {Nima.Tajbakhsh, Sejong, Jian-
ming.Liang}@asu.edu). Nima Tajbakhsh and Jae Y. Shin have contributed
equally.
S. R. Gurudu (Division of Gastroenterology and Hepatology); R. T. Hurst,
C. Kendall (Division of Cardiovascular Diseases); and M. B. Gotway (Depart-
ment of Radiology) are with Mayo Clinic, 13400 E. Shea Blvd., Scottsdale,
AZ 85259, USA (e-mail: {Hurst.R, Kendall.Christopher, Gurudu.Suryakanth,
Gotway.Michael}@mayo.edu).
vision community but across various applications ranging from
natural language processing to hyperspectral image processing
and to medical image analysis. The main power of a CNN lies
in its deep architecture [5]–[8], which allows for extracting a
set of discriminating features at multiple levels of abstraction.
However, training a deep CNN from scratch (or full train-
ing) is not without complications [9]. First, CNNs require
a large amount of labeled training data—a requirement that
may be difﬁcult to meet in the medical domain where expert
annotation is expensive and the diseases (e.g., lesions) are
scarce in the datasets. Second, training a deep CNN requires
extensive computational and memory resources, without which
the training process would be extremely time-consuming.
Third, training a deep CNN is often complicated by overﬁtting
and convergence issues, whose resolution frequently requires
repetitive adjustments in the architecture or learning parame-
ters of the network to ensure that all layers are learning with
comparable speed. Therefore, deep learning from scratch can
be tedious and time-consuming, demanding a great deal of
diligence, patience, and expertise.
A promising alternative to training a CNN from scratch
is to ﬁne-tune a CNN that has been trained using a large
labeled dataset from a different application. The pre-trained
models have been applied successfully to various computer
vision tasks as a feature generator or as a baseline for
transfer learning [10]–[12]. Herein, we address the following
central question in the context of medical image analysis: Can
the use of pre-trained deep CNNs with sufﬁcient ﬁne-tuning
eliminate the need for training a deep CNN from scratch?
This is an important question because training deep CNNs
from scratch may not be practical, given the limited labeled
data in medical imaging. To answer this central question,
we conducted an extensive set of experiments for 4 medi-
cal imaging applications: 1) polyp detection in colonoscopy
videos, 2) image quality assessment in colonoscopy videos,
3) pulmonary embolism detection in computed tomography
(CT) images, and 4) intima-media boundary segmentation in
ultrasonographic images. We have chosen these applications to
represent the most common clinically used imaging modality
systems (i.e., CT, ultrasonography, and optical endoscopy) and
the most common medical image analysis tasks (i.e., lesion
detection, image segmentation, and image classiﬁcation). For
each application, we compared the performance of the pre-
trained CNNs through ﬁne-tuning with that of the CNNs
trained from scratch entirely based on medical imaging data.
We also compared the performance of the CNN-based systems
with their corresponding handcrafted counterparts.
arXiv:1706.00712v1  [cs.CV]  2 Jun 2017


## Page 2


2
II. RELATED WORKS
Applications of CNNs in medical image analysis can be
traced to the 1990s, when they were used for computer-
aided detection of microcalciﬁcations in digital mammography
[13], [14] and computer-aided detection of lung nodules in
CT datasets [15]. With revival of CNNs owing to the de-
velopment of powerful GPU computing, the medical imaging
literature has witnessed a new generation of computer-aided
detection systems that show superior performance. Examples
include automatic polyp detection in colonoscopy videos [16]
[17], computer-aided detection of pulmonary embolism (PE)
in CT datasets [18], automatic detection of mitotic cells
in histopathology images [19], computer-aided detection of
lymph nodes in CT images [20], and computer-aided anatomy
detection in CT volumes [21]. Applications of CNNs in
medical image analysis are not limited to only computer-aided
detection systems, however. CNNs have recently been used
for carotid intima-media thickness measurement in ultrasound
images [22], pancreas segmentation in CT images [23], brain
tumor segmentation in magnetic resonance imaging (MRI)
scans [24], multimodality isointense infant brain image seg-
mentation [25], neuronal membrane segmentation in electron
microscopy images [26], and knee cartilage segmentation in
MRI scans [27].
One important aspect of CNNs is the “transferability”
of knowledge embedded in the pre-trained CNNs. Recent
research conducted by Azizpour et al. [11] suggests that
the success of knowledge transfer depends on the distance,
or dissimilarity, between the database on which a CNN is
trained and the database to which the knowledge is to be
transferred. Although the distance between natural image and
medical imaging databases is considerable, recent studies show
the potential for knowledge transfer to the medical imaging
domain.
The recent research on transfer learning in medical imaging
can be categorized into two groups. The ﬁrst group [28]–[30]
consists of works wherein a pre-trained CNN is used as a
feature generator. Speciﬁcally, the pre-trained CNN is applied
to an input image and then the CNN outputs (features) are
extracted from a certain layer of the network. The extracted
features are then used to train a new pattern classiﬁer. For
instance, in [28], pre-trained CNNs were used as a feature
generator for chest pathology identiﬁcation. A similar study
[29] by Ginneken et al. showed that although the use of
pre-trained CNNs could not outperform a dedicated nodule
detection system, the integration of CNN-based features with
the handcrafted features enabled improved performance.
The second group [31]–[36] consists of works wherein a
pre-trained CNN is adapted to the application at hand. For
instance, in [33], the fully connected layers of a pre-trained
CNN were replaced with a new logistic layer, and then the
labeled data were used to train only the appended layer while
keeping the rest of the network the same. This treatment
yielded promising results for classiﬁcation of unregistered
multiview mammogram. Chen et al. [32] suggested the use of
a ﬁne-tuned pre-trained CNN for localizing standard planes in
ultrasound images. In [35], the authors ﬁne-tuned all layers of
a pre-trained CNN for automatic classiﬁcation of interstitial
lung diseases. They also suggested an attenuation rescale
scheme to convert 1-channel CT slices to RGB-like images
needed for tuning the pre-trained model. Shin et al. [34] used
ﬁne-tuned pre-trained CNNs to automatically map medical
images to document-level topics, document-level sub-topics,
and sentence-level topics. In [36], ﬁne-tuned pre-trained CNNs
were used to automatically retrieve missing or noisy cardiac
acquisition plane information from magnetic resonance imag-
ing and predict the ﬁve most common cardiac views. Different
from the previous approaches, Schlegl et al. [31] considered
the ﬁne-tuning of an unsupervised network. They explored
unsupervised pre-training of CNNs to inject information from
sites or image classes for which no annotations were available,
and showed that such across site pre-training improved clas-
siﬁcation accuracy compared to random initialization of the
model parameters.
III. CONTRIBUTIONS
In this paper, we systematically study knowledge transfer
to medical imaging applications, making the following contri-
butions:
• We demonstrated how ﬁne-tuning a pre-trained CNN in
a layer-wise manner leads to incremental performance
improvement. This approach distinguishes our work from
[28]–[30], which downloaded the features from the fully
connected layers of a pre-trained CNN and then trained a
separate pattern classiﬁer. Our approach also differs from
[31]–[33] wherein the entire pre-trained CNN underwent
ﬁne-tuning.
• We analyzed how the availability of training samples
inﬂuences the choice between pre-trained CNNs and
CNNs trained from scratch. To our knowledge, this issue
has not yet been systematically addressed in the medical
imaging literature.
• We compared the performance of pre-trained CNNs, not
only against handcrafted approaches but also against
CNNs trained from scratch using medical imaging data.
This analysis is in contrast to [28], [29], who pro-
vided only limited performance comparisons between
pre-trained CNNs and handcrafted approaches.
• We presented consistent results with conclusive outcomes
for 4 distinct medical imaging applications involving
classiﬁcation, detection, and segmentation in 3 different
medical imaging modalities, which add substantially to
the state of the art where conclusions are based solely on
1 medical imaging application.
IV. CONVOLUTIONAL NEURAL NETWORKS (CNNS)
CNNs are so-named because of the convolutional layers in
their architectures. Convolutional layers are responsible for
detecting certain local features in all locations of their input
images. To detect local structures, each node in a convolutional
layer is connected to only a small subset of spatially connected
neurons in the input image channels. To enable the search
for the same local feature throughout the input channels, the


## Page 3


3
connection weights are shared between the nodes in the convo-
lutional layers. Each set of shared weights is called a kernel,
or a convolution kernel. Thus, a convolutional layer with n
kernels learns to detect n local features whose strength across
the input images is visible in the resulting n feature maps. To
reduce computational complexity and achieve a hierarchical
set of image features, each sequence of convolution layers
is followed by a pooling layer, a workﬂow reminiscent of
simple and complex cells in the primary visual cortex [37].
The max pooling layer reduces the size of feature maps by
selecting the maximum feature response in overlapping or non-
overlapping local neighborhoods, discarding the exact location
of such maximum responses. As a result, max pooling can
further improve translation invariance. CNNs typically consist
of several pairs of convolutional and pooling layers, followed
by a number of consecutive fully connected layers, and ﬁnally
a softmax layer, or regression layer, to generate the desired
outputs. In more modern CNN architectures, computational
efﬁciency is achieved by replacing the pooling layer with a
convolution layer with a stride larger than 1.
Similar to multilayer perceptrons, CNNs are trained with
the back-propagation algorithm by minimizing the following
cost function with respect to the unknown weights W:
L = −1
|X|
|X|
X
i
ln(p(yi|Xi))
(1)
where |X| denotes the number of training images, Xi denotes
the ith training image with the corresponding label yi, and
p(yi|Xi) denotes the probability by which Xi is correctly
classiﬁed. Stochastic gradient descent is commonly used for
minimizing this cost function, where the cost over the entire
training set is approximated with the cost over mini-batches
of data. If W t
l denotes the weights in lth convolutional layer
at iteration t, and ˆL denotes the cost over a mini-batch of size
N, then the updated weights in the next iteration are computed
as follows:
γt = γ⌊tN
|X|⌋
V t+1
l
= µV t
l −γtαl
∂ˆL
∂Wl
W t+1
l
= W t
l + V t+1
l
(2)
where αl is the learning rate of the lth layer, µ is the
momentum that indicates the contribution of the previous
weight update in the current iteration, and γ is the scheduling
rate that decreases learning rate α at the end of each epoch.
V. FINE-TUNING
The iterative weight update in Eq. 2 begins with a set of ran-
domly initialized weights. Speciﬁcally, before the commence-
ment of the training phase, weights in each convolutional layer
of a CNN are initialized by values randomly sampled from
a normal distribution with a zero mean and small standard
deviation. However, considering the large number of weights
in a CNN and the limited availability of labeled data, the
iterative weight update, starting with a random weight ini-
tialization, may lead to an undesirable local minimum for the
cost function. Alternatively, the weights of the convolutional
layers can be initialized with the weights of a pre-trained CNN
with the same architecture. The pre-trained net is generated
with a massive set of labeled data from a different application.
Training a CNN from a set of pre-trained weights is called ﬁne-
tuning and has been used successfully in several applications
[10]–[12].
Fine-tuning begins with copying (transferring) the weights
from a pre-trained network to the network we wish to train.
The exception is the last fully connected layer whose number
of nodes depends on the number of classes in the dataset. A
common practice is to replace the last fully connected layer
of the pre-trained CNN with a new fully connected layer that
has as many neurons as the number of classes in the new
target application. In our study, we deal with 2-class and 3-
class classiﬁcation tasks; therefore, the new fully connected
layer has 2 or 3 neurons depending on the application under
study. After the weights of the last fully connected layer are
initialized, the new network can be ﬁne-tuned in a layer-wise
manner, starting with tuning only the last layer, then tuning
all layers in a CNN.
Consider a CNN with L layers where the last 3 layers are
fully connected layers. Also let αl denote the learning rate of
the lth layer in the network. We can ﬁne-tune only the last
(new) layer of the network by setting αl = 0 for l ̸= L. This
level of ﬁne-tuning corresponds to training a linear classiﬁer
with the features generated in layer L−1. Likewise, the last 2
layers of the network can be ﬁne-tuned by setting αl = 0 for
l ̸= L, L −1. This level of ﬁne-tuning corresponds to training
an artiﬁcial neural network with 1 hidden layer, which can
be viewed as training a nonlinear classiﬁer using the features
generated in layer L−2. Similarly, ﬁne-tuning layers L, L−1,
and L −2 are essentially equivalent to training an artiﬁcial
neural network with 2 hidden layers. Including the previous
convolution layers in the update process further adapts the pre-
trained CNN to the application at hand but may require more
labeled training data to avoid overﬁtting.
In general, the early layers of a CNN learn low level image
features, which are applicable to most vision tasks, but the
late layers learn high-level features, which are speciﬁc to the
application at hand. Therefore, ﬁne-tuning the last few layers is
usually sufﬁcient for transfer learning. However, if the distance
between the source and target applications is signiﬁcant, one
may need to ﬁne-tune the early layers as well. Therefore, an
effective ﬁne-tuning technique is to start from the last layer and
then incrementally include more layers in the update process
until the desired performance is reached. We refer to tuning
the last few convolutional layers as “shallow tuning” and we
consider tuning all the convolutional layers as “deep tuning”.
We would like to note that the suggested ﬁne-tuning scheme
differs from [10], [12] wherein the network remains the same
and serves as a feature generator, and also differs from [11]
wherein the entire network undergoes ﬁne-tuning at once.
VI. APPLICATIONS AND RESULTS


## Page 4


4
TABLE I: The AlexNet architecture used in our experiments. Of note, C is the number of classes, which is 3 for intima-media
interface segmentation and is 2 for colonoscopy frame classiﬁcation, polyp detection, and pulmonary embolism detection.
layer
type
input
kernel
stride
pad
output
data
input
3x227x227
N/A
N/A
N/A
3x227x227
conv1
convolution
3x227x227
11x11
4
0
96x55x55
pool1
max pooling
96x55x55
3x3
2
0
96x27x27
conv2
convolution
96x27x27
5x5
1
2
256x27x27
pool2
max pooling
256x27x27
3x3
2
0
256x13x13
conv3
convolution
256x13x13
3x3
1
1
384x13x13
conv4
convolution
384x13x13
3x3
1
1
384x13x13
conv5
convolution
384x13x13
3x3
1
1
256x13x13
pool5
max pooling
256x13x13
3x3
2
0
256x6x6
fc6
fully connected
256x6x6
6x6
1
0
4096x1
fc7
fully connected
4096x1
1x1
1
0
4096x1
fc8
fully connected
4096x1
1x1
1
0
Cx1
TABLE II: Learning parameters used for training and ﬁne-tuning of AlexNet in our experiments. µ is the momentum, α is
the learning rate of the weights in each convolutional layer, and γ determines how α decreases over epochs. The learning
rate for the bias term is always set twice as large as the learning rate of the corresponding weights. Of note, “ﬁne-tuned
AlexNet:layer1-layer2” indicates that all layers between and including these 2 layers undergo ﬁne-tuning.
CNNs
Parameters
µ
αconv1
αconv2
αconv3
αconv4
αconv5
αfc6
αfc7
αfc8
γ
Fine-tuned AlexNet:conv1-fc8
0.9
0.001
0.001
0.001
0.001
0.001
0.001
0.001
0.01
0.95
Fine-tuned AlexNet:conv2-fc8
0.9
0
0.001
0.001
0.001
0.001
0.001
0.001
0.01
0.95
Fine-tuned AlexNet:conv3-fc8
0.9
0
0
0.001
0.001
0.001
0.001
0.001
0.01
0.95
Fine-tuned AlexNet:conv4-fc8
0.9
0
0
0
0.001
0.001
0.001
0.001
0.01
0.95
Fine-tuned AlexNet:conv5-fc8
0.9
0
0
0
0
0.001
0.001
0.001
0.01
0.95
Fine-tuned AlexNet:fc6-fc8
0.9
0
0
0
0
0
0.001
0.001
0.01
0.95
Fine-tuned AlexNet:fc7-fc8
0.9
0
0
0
0
0
0
0.001
0.01
0.95
Fine-tuned AlexNet:only fc8
0.9
0
0
0
0
0
0
0
0.01
0.95
AlexNet scratch
0.9
0.001
0.001
0.001
0.001
0.001
0.001
0.001
0.001
0.95
In our study, we considered 4 different medical imaging
applications from 3 imaging modality systems. We study the
performance of polyp detection and PE detection using a
free-response operating characteristic (FROC) analysis, an-
alyze the performance of frame classiﬁcation by means of
an ROC analysis, and evaluate the performance of boundary
segmentation through a boxplot analysis. To perform statistical
comparisons, we have computed the error bars corresponding
to 95% conﬁdence intervals for both ROC and FROC curves
according to the method suggested in [38]. The error bars
enable us to compare each pair of performance curves at
multiple operating points from a statistical perspective. Specif-
ically, if the error bars of a pair of curves do not overlap at
a ﬁxed false positive rate, then the two curves are statistically
different (p<.05) at the given operating point. An appealing
feature of this statistical analysis is that we can compare
the performance curves at a clinically acceptable operating
point rather than comparing the curves as a whole. While
we have discussed the statistical comparisons throughout the
paper, we have further summarized them in a number of
tables in supplementary material, which can be found in the
supplementary ﬁles/multimedia tab.
We used the Caffe library [39] for both training and ﬁne-
tuning CNNs. For consistency and ease of comparison, we
used the AlexNet architecture for the 4 applications under
study. Training and ﬁne-tuning of each AlexNet took approxi-
mately 2-3 hours depending on the size of the training set. To
ensure the proper convergence of each CNN, we monitored
the area under the receiver operating characteristic curve.
Speciﬁcally, for each experiment, we divided the training set
into a smaller training set with 80% of the training data and a
validation set with the remaining 20% of the training data
and then computed area under the curve on the validation
set. The training process was terminated when the highest
accuracy on the validation set was observed. All training was
performed using an NVIDIA GeForce GTX 980TI (6GB on-
board memory). The fully trained CNNs were initialized with
random weights sampled from Gaussian distributions. We also
experimented with other initialization techniques such as those
suggested in [40] and [41], but we observed no signiﬁcant
performance gain after convergence, even though we noticed
varying speed of convergence using these initialization tech-
niques.
For both full training and ﬁne-tuning scenarios, we used
a stratiﬁed training set of image patches where the positive
and negative classes were equally present. For this purpose,
we randomly down-sampled the majority (negative) class,
while keeping the minority class (positive) unchanged. For the
ﬁne-tuning scenario, we used the pre-trained AlexNet model
provided in the Caffe library. The pre-trained AlexNet consists


## Page 5


5
Fig. 1: Variations in shape and appearance of polyps in
colonoscopy videos.
of approximately 5 million parameters in the convolution
layers and about 55 million parameters in its fully connected
layers, and is trained using 1.2 million images labeled with
1000 semantic classes. The model used in our study is the
snapshot taken after 360,000 training iterations. As shown
in Table I, AlexNet begins with 2 pairs of convolutional
and pooling layers, mapping the 227x227 input images to
13x13 feature maps. This architecture then proceeds with a
sequence of 3 convolutional layers that efﬁciently implement
a convolutional layer with 9x9 kernels, yet with a larger degree
of nonlinearity. The sequence of convolutional layers is then
followed by a pooling layer and 3 fully connected layers. The
ﬁrst fully connected layer can be viewed as a convolution layer
with 6x6 kernels and the other 2 fully connected layers as
convolutional layers with 1x1 kernels.
Table II summarizes the learning parameters used for train-
ing and ﬁne-tuning of AlexNet in our experiments. The listed
parameters were tuned through an extensive set of trial and
error experiments. According to our exploratory experiments,
the learning rate and scheduling rate heavily inﬂuenced the
convergence of CNNs. A learning rate of 0.001 however
ensured proper convergence for all 4 applications. A smaller
learning rate slowed down convergence and a larger learning
rate often caused convergence failures. Our exploratory ex-
periments also indicated that the value of γ depended on the
speed of convergence. During a fast convergence, the learning
rate can be safely decreased after a few epochs, allowing for
the use of a small scheduling rate. However, during a slow
convergence, a larger scheduling rate is required to maintain a
relatively large learning rate. For all 4 applications, we found
γ = .95 to be a reasonable choice.
A. Polyp detection
Colonoscopy is the preferred technique for colon cancer
screening and prevention. The goal of colonoscopy is to
ﬁnd and remove colonic polyps—precursors to colon cancer.
Polyps, as shown in Fig. 1, can appear with substantial
variations in color, shape, and size. The challenging appear-
ance of polyps can often lead to misdetection, particularly
during long and back-to-back colonoscopy procedures where
fatigue negatively affects the performance of colonoscopists.
Polyp miss-rates are estimated to be about 4% to 12% [43]–
[46]; however, a more recent clinical study [47] is suggestive
that this misdetection rate may be as high as 25%. Missed
polyps can lead to the late diagnosis of colon cancer with
an associated decreased survival rate of less than 10% for
metastatic colon cancer [48]. Computer-aided polyp detection
may enhance optical colonoscopy screening by reducing polyp
misdetection.
Several computer-aided detection (CAD) systems have
been suggested for automatic polyp detection in colonoscopy
videos. The early systems [49]–[51] relied on polyp color
and texture for detection. However, limited texture visibility
on the surface of polyps and large color variations among
polyps hindered the applicability of such systems. More recent
systems [52]–[56] relied on temporal information and shape
information to enhance polyp detection. Shape features proved
more effective than color and texture in this regard; however,
these features can be misleading without consideration of the
context in which the polyp is found. In our previous works
[57]–[59], culminated in [42], we attempted to overcome the
limitation of approaches based solely on polyp shape. Speciﬁ-
cally, we suggested a handcrafted approach for combining the
shape and context information around the polyp boundaries
and demonstrated the superiority of this approach over the
other state-of-the-art methods.
For training and evaluation, we used our database of 40
short colonoscopy videos. Each colonoscopy frame in our
database comes with a binary ground truth image. We ran-
domly divided the colonoscopy videos into a training set con-
taining 3,800 frames with polyps and 15,100 frames without
polyps and into a test set containing 5,700 frames with polyps
and 13,200 frames without polyps. We applied our handcrafted
approach [42] to the training and test frames to obtain a set
of polyp candidates with the corresponding bounding boxes.
At each candidate location, given the available bounding box,
we extracted a set of image patches with data augmentation.
Speciﬁcally, for each candidate, we extracted patches at 3
scales by enlarging the corresponding bounding box by a
factor of 1.0x, 1.2x, and 1.5x. At each scale, we extracted
patches after we translated the candidate location by 10% of
the resized bounding box in horizontal and vertical directions.
We further rotated each resulting patch 8 times by horizontal
and vertical mirroring and ﬂipping. We then labeled a patch as
positive if the underlying candidate fell inside the ground truth
for polyps; otherwise, the candidate was labeled as negative.
Because of the relatively large number of negative patches,
we collected a stratiﬁed set of 100,000 training patches for
training and ﬁne-tuning the CNNs. During the test stage, all
test patches extracted from a polyp candidate were fed to the
trained CNN. We then averaged the probabilistic outputs of
the test patches at the candidate level and performed an FROC
analysis for performance evaluation.
Fig. 2(a) compares the FROC curve of our handcrafted ap-
proach with that of ﬁne-tuned CNNs and a CNN trained from
scratch. To avoid clutter in the ﬁgure, we have shown only a
subset of representative FROC curves. Statistical comparisons


## Page 6


6
10
−4
10
−3
10
−2
10
−1
10
0
10
1
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
 
FROC Analysis
False Positives Per Frame
 
Sensitivity
Fine−tuned AlexNet:only fc8
Fine−tuned AlexNet:fc7−fc8
Fine−tuned AlexNet:conv4−fc8
Fine−tuned AlexNet:conv1−fc8
AlexNet scratch
hand−crafted method
(a)
0.01
0.02
0.03
0.04
0.05
0.06
0.07
0.08
0.09
0.1
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
 
FROC Analysis
False Positives Per Frame
 
Sensitivity
Fine−tuned AlexNet:conv1−fc8 using 25% training data
AlexNet scratch using 25% training data
Fine−tuned AlexNet:conv1−fc8 using 50% training data
AlexNet scratch using 50% training data
Fine−tuned AlexNet:conv1−fc8 using 100% training data
AlexNet scratch using 100% training data
(b)
Fig. 2: FROC analysis for polyp detection. (a) Comparison between incremental ﬁne-tuning, training from scratch, and a
handcrafted approach [42]. (b) Effect of reduction in the training data on the performance of CNNs trained from scratch and
deeply ﬁne-tuned CNNs.
between each pair of FROC curves at three operating points
are also presented in Table S1. The handcrafted approach
is signiﬁcantly outperformed by all CNN-based scenarios
(p<.05). This result is probably because our handcrafted
approach used only geometric information to remove false-
positive candidates. For ﬁne-tuning, the lowest performance
was obtained when only the last layer of AlexNet was updated
with colonoscopy data. However, ﬁne-tuning the last two
layers (FT:fc7-fc8) achieved a signiﬁcantly higher sensitivity
(p<.05) at nearly all operating points compared to the pre-
trained AlexNet with only 1 ﬁne-tuned layer (FT:only fc8). We
also observed incremental performance improvement when we
included more convolutional layers in the ﬁne-tuning process.
Speciﬁcally, the pre-trained CNN with shallow ﬁne-tuning
(FT:fc7-fc8) was signiﬁcantly outperformed by the pre-trained
CNNs with a moderate level of ﬁne-tuning (FT:conv5,4,3-
fc8) at most of the operating points. Furthermore, the deeply-
tuned CNNs (FT:conv1,2-fc8) achieved a signiﬁcantly higher
sensitivity than the pre-trained CNNs with a moderate level
of ﬁne-tuning particularly at low false positive rates. Also, as
seen in Fig. 2(a), ﬁne-tuning the last few convolutional layers
was sufﬁcient to outperform an AlexNet model trained from
scratch in a low false positive setting.
The performance gap between fully trained AlexNet model
and their deeply ﬁne-tuned counterparts becomes more evident
when fewer training samples are used for training and tuning.
To demonstrate this effect, we trained a CNN from scratch
and ﬁne-tuned the entire AlexNet using 50% and 25% of the
entire training samples. We reduced training data at the video
level to exclude a fraction of unique polyps from the training
set. The results are shown in Fig. 2(b). With a 50% reduction
in training data, a signiﬁcant performance gap was observed
between the CNN trained from scratch and the deeply ﬁne-
tuned CNN. With a 25% reduction in the training data, the
fully trained CNN showed dramatic performance degradation,
but the deeply ﬁne-tuned CNN still exhibited relatively high
Fig. 3: 5 different PEs in the standard 3-channel representation
and in our suggested 2-channel representation. PEs appear
more consistently in our representation. We use our PE rep-
resentation for the experiments presented herein because it
achieves greater classiﬁcation accuracy and enables improved
convergence.
performance. These ﬁndings strongly favor the use of the ﬁne-
tuning approach over full training of a CNN from scratch.
B. Pulmonary embolism detection
A PE is a blood clot that travels from a lower extremity
source to the lung, where it causes blockage of the pulmonary
arteries. The mortality rate of untreated PE may approach
30% [61], but it decreases to as low as 2% with early diagnosis
and appropriate treatment [62]. CT pulmonary angiography
(CTPA) is the primary means for PE diagnosis, wherein a
radiologist carefully traces each branch of the pulmonary
artery for any suspected PEs. CTPA interpretation is a time-
consuming task whose accuracy depends on human factors,
such as attention span and sensitivity to the visual character-


## Page 7


7
0
1
2
3
4
5
6
7
8
9
10
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
 
FROC
False Positives Per Volume
 
Sensitivity
Fine−tuned AlexNet:only fc8
Fine−tuned AlexNet:fc7−fc8
Fine−tuned AlexNet:fc6−fc8
Fine−tuned AlexNet:conv1−fc8
AlexNet scratch
hand−crafted method
(a)
0
1
2
3
4
5
6
7
8
9
10
0
0.5
1
Sensitivity
100% training data
 
 
AlexNet scratch
Fine−tuned AlexNet:conv1−fc8
0
1
2
3
4
5
6
7
8
9
10
0
0.5
1
Sensitivity
50% training data
 
 
AlexNet scratch
Fine−tuned AlexNet:conv1−fc8
0
1
2
3
4
5
6
7
8
9
10
0
0.5
1
False Positives Per Volume
Sensitivity
25% training data
 
 
AlexNet scratch
Fine−tuned AlexNet:conv1−fc8
(b)
Fig. 4: FROC analysis for pulmonary embolism detection. (a) Comparison between incremental ﬁne-tuning, training from
scratch, and a handcrafted approach [60]. To avoid clutter in the ﬁgure, error bars are displayed for only a subset of plots.
A more detailed analysis is presented in Table S2. (b) Effect of reduction in the training data on the performance of CNNs
trained from scratch and deeply ﬁne-tuned CNNs.
istics of PEs. CAD can have a major role in improving PE
diagnosis and decreasing the reading time of CTPA datasets.
We based our experiments on the PE candidates generated
by our previous work [60] and the image representation that
we suggested for PE in our recently published study [18].
Our candidate generation method is an improved version of
the tobogganing algorithm [63] that aims to ﬁnd an embolus
as a dark region surrounded by a brighter background. Our
image representation consistently results in 2-channel image
patches, which capture PEs in cross-sectional and longitudinal
views of vessels (see Fig. 3). This unique representation
dramatically decreases the variability in the appearance of
PEs, enabling us to train more accurate CNNs. However,
since the AlexNet architecture receives color images as its
input, the 2-channel image patches must be converted to color
patches. For this purpose, we simply repeated the second
channel and produced 3-channel RGB-like image patches. The
resulting patches were then used for training and ﬁne-tuning an
AlexNet. For performance comparison, we used a handcrafted
approach [60], which is arguably one of the most, if not the
most, accurate PE CAD system. The handcrafted approach
utilizes the same candidate generation method [60], but uses
vessel-based features along with Haralick [64] and wavelet-
based features for PE characterization, and ﬁnally uses a multi-
instance classiﬁer for candidate classiﬁcation.
For experiments, we used a database consisting of 121
CTPA datasets with a total of 326 PEs. We ﬁrst applied the
tobogganing algorithm to obtain a crude set of PE candidates.
This application resulted in 6,255 PE candidates, of which
5,568 were false positives and 687 were true positives. The
number of true positives was far larger than the number of PEs
because the tobogganing algorithm can cast several candidates
for the same PE. We divided the collected candidates at the
patient level into a training set with 434 true positives (199
unique PEs) and 3,406 false positives, and a test set with 253
true positives (127 unique PEs) and 2,162 false positives. For
training the CNNs, we extracted patches of 3 different physical
sizes, resulting in 10 mm-, 15 mm-, and 20 mm-wide patches.
We also translated each candidate location along the direction
of the affected vessel 3 times, up to 20% of the physical
size of the patches. We further augmented the training dataset
by rotating the longitudinal and cross-sectional vessel planes
around the vessel axis, resulting in 5 additional variations for
each scale and translation. We formed a stratiﬁed training set
with 81,000 image patches for training and ﬁne-tuning the
CNNs. For testing, we performed the same data augmentation
for each test candidate and then computed the overall PE
probability by averaging the probabilistic scores generated for
the data-augmented patches for each PE candidate.
For evaluation, we performed an FROC analysis by chang-
ing a threshold on the probabilistic scores generated for the
test PE candidates. Fig. 4(a) shows the FROC curves for the
handcrafted approach, a deep CNN trained from scratch, and
a subset of representative pre-trained CNNs that are ﬁne-
tuned in a layer-wise manner. We have further summarized
statistical comparisons between each pair of FROC curves in
Table S2. As shown, the pre-trained CNN with two ﬁne-tuned
layers (FT:fc7-fc8) achieved a signiﬁcantly higher sensitivity
(p<0.05) than that of the pre-trained CNN with only one
ﬁne-tuned layer (FT:only fc8). The improved sensitivity was
observed at most of the operating points. However, inclusion
of each new layer in the ﬁne-tuning process resulted in only
marginal performance improvement, even though the accumu-
lation of such marginal improvements yielded a substantial
margin between the deeply ﬁne-tuned CNNs and those with
1, 2, or 3 ﬁne-tuned layers. Speciﬁcally, the deeply ﬁne-tuned
CNN (FT:conv1-fc8) yielded signiﬁcantly higher sensitivity
(p<0.05) than that of the pre-trained CNN with 2 ﬁne-tuned


## Page 8


8
Fig. 5: (a) An informative colonoscopy frame. (b,c,d) Ex-
amples of non-informative colonoscopy images. The non-
informative frames are usually captured during the rapid
motion of the scope or during wall contact.
layers (FT:fc7-fc8) at the majority of the operating points
shown in Fig. 4(a). At 3 false positives per volume, the deeply
ﬁne-tuned CNN also achieved signiﬁcantly higher sensitivity
(p<0.05) than that of the pre-trained CNN with three ﬁne-
tuned layers (FT:fc7-fc8). From Fig. 4(a), it is also evident
that the deeply ﬁne-tuned CNN yielded a non-signiﬁcant
performance improvement over the handcrafted approach. This
is probably because the handcrafted approach is an accurate
system whose underlying features are speciﬁcally and incre-
mentally designed to remove certain types of false detections.
Yet, we ﬁnd it interesting that an end-to-end learning machine
can learn such a sophisticated set of features with minimal
engineering effort. From Fig. 4(a), we also observed that the
deeply ﬁne-tuned CNN performs on a par with the CNN
trained from scratch.
We further analyzed how the size of training samples
inﬂuences the competitive performance between the CNN
trained from scratch and the deeply ﬁne-tuned CNN. For this
purpose, we reduced the training samples at the PE-level to
50% and 25%. The results are shown in Fig. 4(b). With a
50% reduction in training data, a signiﬁcant performance gap
was observed between the CNN trained from scratch and
the deeply tuned CNN in all the operating points. With a
25% reduction in the training data, we observed a decrease
in the overall performance of both CNNs with a smaller yet
signiﬁcant gap between the two curves in most of the operating
points. These ﬁndings not only favor the use of a deeply
ﬁne-tuned CNN but also underscore the importance of large
training sets for effective training and ﬁne-tuning of CNNs.
C. Colonoscopy frame classiﬁcation
Image quality assessment can have a major role in objective
quality assessment of colonoscopy procedures. Typically, a
colonoscopy video contains a large number of non-informative
images with poor colon visualization that are not suitable for
inspecting the colon or performing therapeutic actions. The
larger the fraction of non-informative images in a video, the
lower the quality of colon visualization, and thus the lower
the quality of colonoscopy. Therefore, one way to measure the
quality of a colonoscopy procedure is to monitor the quality
of the captured images. Such quality assessment can be used
during live procedures to limit low-quality examinations or in
a post-processing setting for quality monitoring purposes.
Technically, image quality assessment at colonoscopy can
be viewed as an image classiﬁcation task whereby an input
image is labeled as either informative or non-informative.
Fig. 5 shows examples of non-informative and informative
colonoscopy frames. In our previous work [65], we suggested
a handcrafted approach based on local and global features that
were pooled from the image reconstruction error. We showed
that our handcrafted approach outperformed the other major
methods [66], [67] for quality assessment in colonoscopy
videos. In the current effort, we explored the use of deep CNNs
as an alternative to a carefully engineered method. Speciﬁcally,
we compared the performance of our handcrafted approach
with that of a deep CNN trained from scratch and a pre-trained
CNN that was ﬁne-tuned using the labeled colonoscopy frames
in a layer-wise manner..
For experiments, we used 6 complete colonoscopy videos.
Considering the expenses associated with annotation of all
video frames, we instead sampled each colonoscopy video
by selecting 1 frame from every 5 seconds of each video
and thereby removed many similar colonoscopy frames. The
resulting set was further reﬁned to create a balanced dataset
of 4,000 colonoscopy images in which both informative and
non-informative classes were represented equally. A trained
expert then manually labeled the collected images as informa-
tive or non-informative. A gastroenterologist further reviewed
the labeled images for corrections. We divided the labeled
frames at the video-level into training and test sets, each
containing approximately 2,000 colonoscopy frames. For data
augmentation, we extracted 200 sub-images of size 227x227
pixels from random locations in each 500x350 colonoscopy
frame, resulting in a stratiﬁed training set with approximately
40,000 sub-images. During the test stage, the probability of
each frame being informative was computed as the average
probabilities assigned to its randomly cropped sub-images.
We used an ROC analysis for performance comparisons
between the CNN-based scenarios and handcrafted approach.
The results are shown in Fig. 6(a). To avoid clutter in the
ﬁgure, we have shown only a subset of representative ROC
curves. We have, however, summarized the statistical com-
parisons between all ROC curves at 10%, 15%, and 20%
false positive rates in Table S3. We observed that all CNN-
based scenarios signiﬁcantly outperformed the handcrafted
approach in at least one of the above 3 operating points. We
also observed that ﬁne-tuning the pre-trained CNN halfway
through the network (FT:conv4-fc8 and FT:conv5-fc8) not
only signiﬁcantly outperformed shallow-tuning but also was
superior to a deeply ﬁne-tuned CNN (FT:conv1-fc8) at 10%
and 15% false positive rates. This was probably because the
kernels learned in the early layers of the CNN were suitable
for image quality assessment and thus their ﬁne-tuning was
unnecessary. Furthermore, while the CNN trained from scratch
outperformed the pre-trained CNN with shallow ﬁne-tuning
(FT:only fc8), it was outperformed by the pre-trained CNN
with a moderate level of ﬁne-tuning (FT:conv5-fc8). Therefore,
the ﬁne-tuning scheme was superior to the full training scheme
from scratch.
To examine how the performance of CNNs changes with
respect to the size of the training data, we decreased the
number of training samples by factors of 1/10, 1/20, and 1/100.
Comparing these with other applications, we considered a
further reduction in the size of the training dataset because


## Page 9


9
0.05
0.1
0.15
0.2
0.25
0.3
0.35
0.4
0.45
0.5
0.5
0.55
0.6
0.65
0.7
0.75
0.8
0.85
0.9
0.95
1
ROC Analysis
1−specificity
Sensitivity
 
 
Fine−tuned AlexNet:only fc8
Fine−tuned AlexNet:conv5−fc8
Fine−tuned AlexNet:conv1−fc8
AlexNet scratch
hand−crafted method
(a)
0.2
0.4
0.6
0.8
0.5
0.6
0.7
0.8
0.9
1
Sensitivity
100% training data
 
 
AlexNet scratch
Fine−tuned AlexNet:conv1−fc8
0.2
0.4
0.6
0.8
0.5
0.6
0.7
0.8
0.9
1
10% training data
 
 
AlexNet scratch
Fine−tuned AlexNet:conv1−fc8
0.2
0.4
0.6
0.8
0.5
0.6
0.7
0.8
0.9
1
1− specificity
Sensitivity
5% training data
 
 
AlexNet scratch
Fine−tuned AlexNet:conv1−fc8
0.2
0.4
0.6
0.8
0.5
0.6
0.7
0.8
0.9
1
1− specificity
1% training data
 
 
AlexNet scratch
Fine−tuned AlexNet:conv1−fc8
(b)
Fig. 6: ROC analysis for image quality assessment. (a) Comparison between incremental ﬁne-tuning, training from scratch, and
a handcrafted approach [65]. (b) Effect of reduction in the training data on the performance of convolutional neural networks
(CNNs) trained from scratch vs deeply ﬁne-tuned CNNs.
a moderate decrease did not inﬂuence the performance of
CNNs substantially. As shown in Fig. 6(b), both deeply ﬁne-
tuned CNNs and fully trained CNN showed insigniﬁcant
performance degradation even when using 10% of the original
training set. However, further reduction in the size of the
training set substantially degraded the performance of fully
trained CNNs and, to a largely less extent, the performance of
deeply ﬁne-tuned CNNs. The relatively high performance of
the deeply ﬁne-tuned CNNs, even with a limited training set,
indicates the usefulness of the kernels learned from ImageNet
for colonoscopy frame classiﬁcation.
D. Intima-media boundary segmentation
Carotid intima-media thickness (CIMT), a noninvasive ul-
trasonography method, has proven valuable for cardiovascular
risk stratiﬁcation. The CIMT is deﬁned as the distance between
the lumen-intima and media-adventitia interfaces at the far
wall of the carotid artery (Fig. 7). The CIMT measurement is
performed by manually tracing the lumen-intima and media-
adventitia interfaces in a region of interest (ROI), followed
by calculation of the average distance between the traced
interfaces. However, manual tracing of the interfaces is time-
consuming and tedious. Therefore, several methods [68]–
[71] have been developed to allow automatic CIMT image
interpretation. The suggested methods are more or less based
on handcrafted techniques whose performance may vary ac-
cording to image quality and the level of artifacts present
within the images.
We formulated this interface segmentation task as a 3-class
classiﬁcation problem wherein the goal was to classify every
pixel in the ROI into 3 categories: a pixel on the lumen-
intima interface, a pixel on the media-adventitia interface, or a
non-interface pixel. For this classiﬁcation problem, we trained
a 3-way CNN using the training patches collected from the
lumen-intima interface and media-adventitia interface, as well
Fig. 7: Intima media thickness (IMT) is measured within a
region of interest after the lumen-intima and media-adventitia
interfaces are segmented. For automatic interface segmenta-
tion, we trained a 3-way convolutional neural network whose
training patches were extracted from each of these interfaces
(highlighted in red and green) and far from the interfaces
(highlighted in gray).
as from other random locations far from the desired interfaces.
Fig. 7 illustrates how these patches are extracted from an
ultrasonography frame.
Fig. 8 shows how a CNN-based system traces the interfaces
for a given test ROI. The trained CNN is ﬁrst applied to each
pixel within the test ROI in a convolutional manner, generating


## Page 10


10
Fig. 8: The test stage of lumen-intima and media-adventitia interface segmentation. (a) A test region of interest. (b) The
corresponding conﬁdence map generated by the convolutional neural network. The green and red colors indicate the likelihood
of a lumen-intima interface and media-adventitia interface, respectively. (c) The thick probability band around each interface
is thinned by selecting the largest probability for each interface in each column. (d) The step-like boundaries are smoothed
using 2 open snakes. (e) Interface segmentation from the ground truth.
0
50
100
150
200
250
300
350
400
450
500
µ = 100.97, 
σ = 132.64
µ = 34.67, 
σ = 14.77
µ = 27.87, 
σ = 11.83
µ = 25.32, 
σ = 11.02
µ = 25.01, 
σ = 9.94
µ = 24.37, 
σ = 10.79
µ = 24.71, 
σ = 10.25
µ = 24.74, 
σ = 11.42
µ = 28.11, 
σ = 13.79
µ = 98.17, 
σ = 16.57
FT:only fc8
FT:fc7-fc8
FT:fc6-fc8
FT:conv5-fc8
FT:conv4-fc8
FT:conv3-fc8
FT:conv2-fc8
FT:conv1-fc8
AlexNet scratch
Hand-Crafted
Lumen-intima interface
Segmentation error (
µm)
(a)
0
50
100
150
200
250
300
350
400
450
500
µ = 103.26, 
σ = 58.48
µ = 43.93, 
σ = 21.79
µ = 34.63, 
σ = 14.49
µ = 31.94, 
σ = 13.13
µ = 30.55, 
σ = 11.97
µ = 31.80, 
σ = 11.98
µ = 31.74, 
σ = 12.37
µ = 31.21, 
σ = 12.56
µ = 33.45, 
σ = 16.17
µ = 106.62, 
σ = 21.00
FT:only fc8
FT:fc7-fc8
FT:fc6-fc8
FT:conv5-fc8
FT:conv4-fc8
FT:conv3-fc8
FT:conv2-fc8
FT:conv1-fc8
AlexNet scratch
Hand-Crafted
Media-adventitia interface
Segmentation error (
µm)
(b)
Fig. 9: Box plots of segmentation error for (a) the lumen-intima interface and (b) the media-adventitia interface.
2 conﬁdence maps of the same size as the ROI, with the ﬁrst
map showing the probability of a pixel residing on the lumen-
intima interface and the second map showing the probability
of a pixel residing on the media-adventitia interface. For
visualization convenience, we merged these 2 conﬁdence maps
into 1 color-coded conﬁdence map in which the green and
red colors indicate the likelihood of being a lumen-intima
interface and a media-adventitia interface, respectively. As
shown in Fig. 8(b), the probability band of each interface is
too thick to accurately measure intima-media thickness. To
resolve this issue, we obtained thinner interfaces by scanning
the conﬁdence map column by column to search for rows with
the maximum response for each of the 2 interfaces, yielding a
1-pixel boundary with a step-like shape around each interface,
as shown in Fig. 8(c). To smooth the boundaries, we used 2
active contour models (snakes) [72], one for the lumen-intima
interface and one for the media-adventitia interface. The open
snakes were initialized with the current step-like boundaries
and then kept deforming until they took the actual shapes of
the interfaces. Fig. 8(d) shows the converged snakes for the
test ROI. We computed intima-media thickness as the average
of the vertical distances between the 2 open snakes.
For the experiments, we used a database of 92 CIMT videos.
The expert reviews each video to determine 3 ROIs for which
the CIMT can be measured reliably. To create the ground truth,
lumen-intima and media-adventitia interfaces were annotated
as the consensus of 2 experts for each of the 276 ROIs.
We divided the ROIs at the subject-level into a training set
with 144 ROIs and a test set with 132 ROIs. For training
and ﬁne-tuning the CNNs, we extracted a stratiﬁed set of
200,000 training patches from the training ROIs. Because
the AlexNet architecture used in our study required color
patches as its input, each extracted gray-scale patch was
converted to a color patch by repeating the gray channel
thrice. Note that we did not perform data augmentation for
the positive patches, for 2 reasons. First, 92x60 ROIs allow
us to collect a large number of patches around the lumen-
intima and media-adventitia interfaces, eliminating the need
for any further data augmentation. Second, given the relatively
small distance between the 2 interfaces, translation-based data
augmentation would inject a large amount of label noise,
which would negatively affect the convergence and the overall


## Page 11


11
performance of the CNNs. In the test stage, we measured
the error of interface segmentation as the average distance
between the expert-annotated interfaces and those produced
by the systems. For a more detailed analysis, we measured
segmentation error for the lumen-intima and media-adventitia
interfaces separately.
Fig. 9 shows the box plots of segmentation error for each
interface. The whiskers were plotted according to Tukey
method. For easier quantitative comparisons, we have also
shown the average and standard deviation of the localiza-
tion error above each boxplot. The segmentation error for
the media-adventitia interface was generally greater than the
lumen-intima interface, which was expected because of the
relatively more challenging image characteristics of the media-
adventitia interface. For both interfaces, holding all the layers
ﬁxed except the last layer (FT: only fc8) resulted in the
lowest performance, which was comparable to that of the
handcrafted approach [73]. However, inclusion of layer fc7
in the ﬁne-tuning process (FT:fc7-fc8) led to a signiﬁcant
decrease (p<.0001) in segmentation error for both interfaces.
The reduced localization error was also signiﬁcantly lower (p<
.0001) than that of the handcrafted approach. We observed
another signiﬁcant drop (p<.001) in the localization error of
both interfaces after ﬁne-tuning layer fc6; however, this error
was still signiﬁcantly larger (p<.001) than that of the deeply
ﬁne-tuned AlexNet (FT:conv1-fc8). We observed a localization
error comparable to that of the deeply ﬁne-tuned AlexNet
only after inclusion of layer conv5 in the ﬁne-tuning process.
With deeper ﬁne-tuning, we obtained only marginal decrease
in the localization error for both interfaces. Furthermore, the
localization error obtained by the deeply ﬁne-tuned CNN
was signiﬁcantly lower than that of the CNN trained from
scratch for media-adventitia interface (p<.05) and for Lumen-
intima interface (p<.0001), indicating the superiority of the
ﬁne-tuning scheme over the training scheme from scratch.
Of note, we observed no signiﬁcant performance degradation
for either deeply ﬁne-tuned CNNs or fully trained CNNs,
even after reducing the training patches to a single patient.
This outcome resulted because each patient in our database
provided approximately 12 ROIs, which enabled the extraction
of a large number of distinct training patches that could be
used for training and for ﬁne-tuning the deep CNNs.
VII. DISCUSSION
In this study, to ensure generalizability of our ﬁndings,
we considered 4 common medical imaging problems from 3
different imaging modality systems. Speciﬁcally, we chose PE
detection as representative of computer-aided lesion detection
in 3-dimensional volumetric images, polyp detection as repre-
sentative of computer-aided lesion detection in 2-dimensional
images, intima-media boundary segmentation as representative
of machine learning-based medical image segmentation, and
colonoscopy image quality assessment as representative of
medical image classiﬁcation. These applications differ because
they require solving problems at different image scales. For in-
stance, although intima-media boundary segmentation and PE
detection may require the examination of a small sub-region
within the images, polyp detection and frame classiﬁcation
demand far larger receptive ﬁelds. Therefore, we believe that
the chosen applications encompass a variety of applications
relevant to the ﬁeld of medical imaging.
We thoroughly investigated the potential for ﬁne-tuned
CNNs in the context of medical image analysis as an alterna-
tive to training deep CNNs from scratch. We performed our
analyses using both large training sets and reduced training
sets. When using complete datasets, we observed that shallow
tuning of the pre-trained CNNs most often led to a perfor-
mance inferior to CNNs trained from scratch, whereas with
deeper ﬁne-tuning, we obtained performance comparable and
even superior to CNNs trained from scratch. The performance
gap between deeply ﬁne-tuned CNNs and those trained from
scratch widened when the size of training sets was reduced,
which led us to conclude that ﬁne-tuned CNNs should always
be the preferred option regardless of the size of training sets
available.
Another advantage of ﬁne-tuned CNNs is the speed of
convergence. To demonstrate this advantage, we compare the
speed of convergence for a deeply ﬁne-tuned CNN and a CNN
trained from scratch in Fig. 10. For a thorough comparison,
we used 3 different techniques to initialize the weights of
the fully trained CNNs: 1) a method commonly known as
Xavier, which was suggested in [40], 2) a revised version of
Xavier called MSRA, which was suggested in [41], and a basic
random initialization method based on Gaussian distributions.
In this analysis, we computed the AUC on the validation data
as a measure of convergence. Speciﬁcally, each snapshot of
the model was applied to the patches of the validation set
and then the classiﬁcation performance was evaluated using an
ROC analysis. Because we dealt with a 3-class classiﬁcation
problem for the ask of intimia-media boundary segmentation,
we merged the 2 interface classes into a positive class and
then computed the AUC for the resulting binary classiﬁcation
(interface vs. background). As shown, the ﬁne-tuned CNN
quickly reaches its maximum performance, but the CNNs
trained from scratch require longer training in order to reach
their highest performance. Furthermore, the use of different
initialization techniques led to different trends of convergence,
even though we observed no signiﬁcant performance gain after
complete convergence except for PE detection.
We observed that the depth of ﬁne-tuning is fundamental to
achieving accurate image classiﬁers. Although shallow tuning
or updating the last few convolutional layers is sufﬁcient for
many applications in the ﬁeld of computer vision to achieve
state-of-the-art performance, we discovered that a deeper level
of tuning is essential for medical imaging applications. For
instance, we observed a marked performance gain using deeply
ﬁne-tuned CNNs, particularly for polyp detection and intima-
media boundary segmentation, probably because of the sub-
stantial difference between these applications and the database
with which the pre-trained CNN was constructed. However,
we did not observe a similarly profound performance gain
for colonoscopy frame classiﬁcation, which we attribute to
the relative similarity between ImageNet and the colonoscopy
frames in our database. Speciﬁcally, both databases use high-
resolution images with similar low-level image information,


## Page 12


12
10
1
10
2
10
3
0
0.2
0.4
0.6
0.8
1
#mini−batches
AUC
Polyp detection
 
 
FT:conv1−fc8
AlexNet scratch with Gaussian Init
AlexNet scratch with Xavier Init
AlexNet scratch with MSRA Init
10
3
0
0.2
0.4
0.6
0.8
1
#mini−batches
AUC
PE detection
 
 
FT:conv1−fc8
AlexNet scratch with Gaussian Init
AlexNet scratch with Xavier Init
AlexNet scratch with MSRA Init
10
1
10
2
10
3
0
0.2
0.4
0.6
0.8
1
#mini−batches
AUC
Colonoscopy frame classification
 
 
FT:conv1−fc8
AlexNet scratch with Gaussian Init
AlexNet scratch with Xavier Init
AlexNet scratch with MSRA Init
10
0
10
1
10
2
10
3
0
0.2
0.4
0.6
0.8
1
#mini−batches
AUC
Intima−media boundary segmentation
 
 
FT:conv1−fc8
AlexNet scratch with Gaussian Init
AlexNet scratch with Xavier Init
AlexNet scratch with MSRA Init
Fig. 10: Convergence speed for a deeply ﬁne-tuned CNN and CNNs trained from scratch with three different initialization
techniques.
which is why ﬁne-tuning the late convolutional layers, which
have application-speciﬁc features, is sufﬁcient to achieve high-
level performance for colonoscopy frame classiﬁcation.
We based our experiments on the AlexNet architecture
because a pre-trained AlexNet model was available in the
Caffe library and that this architecture was deep enough that
we could investigate the impact of the depth of ﬁne-tuning on
the performance of pre-trained CNNs. Alternatively, deeper
architectures—such as VGGNet and GoogleNet—could have
been used. Deeper architectures have recently shown relatively
high performance for challenging computer vision tasks, but
we do not anticipate a signiﬁcant performance gain through the
use of deeper architectures for medical imaging applications.
We emphasize that the objective of this work was not to
achieve the highest performance for a number of different
medical imaging tasks but to examine the capabilities of ﬁne-
tuning in comparison with the training scheme from scratch.
For these purposes, AlexNet is a reasonable architectural
choice.
We would like to acknowledge that the performance curves
reported for different models and applications may not be the
best that we could achieve for each experiment. This sub-
optimal performance is related to the choice of the hyper-
parameters of CNNs that can inﬂuence the speed of conver-
gence and ﬁnal accuracy of a model. Although we attempted
to ﬁnd the working values of these parameters, ﬁnding the
optimal values was not feasible given the large number of
CNNs studied in our paper and that training each CNN was
a time-consuming process even on the high-end GPUs. Nev-
ertheless, this issue may not change our overall conclusions
as the majority of the CNNs used in our comparisons are
pre-trained models that may be less affected by the choice of
hyper-parameters than the CNNs trained from scratch.
In this study, due to space constraints, we were not able
to cover all medical imaging modalities. For instance, we did
not study the performance of ﬁne-tuning in MR images or
histopathology images, for which full training of CNNs from
scratch had shown promising performance. However, consid-
ering the successful knowledge transfer from natural images
to CT, ultrasound, and endoscopy applications, we surmise
that ﬁne-tuning would succeed in other medical applications
as well. Furthermore, our study was focused on ﬁne-tuning of
a pre-trained supervised model. However, a pre-trained unsu-
pervised model such as those obtained by restricted Boltzmann
machines (RBMs) or convolutional RBMs [74] could also be
considered, even though the availability of ImageNet database
with millions of labeled images from 1000 semantic classes
may make the use of a pre-trained supervised model a natural
choice for ﬁne-tuning. Nevertheless, unsupervised models are
still useful for 1D signal processing due to the absence of
a large database of labeled 1D signals. For instance, ﬁne-
tuning of an unsupervised model was used in [75] for acoustic


## Page 13


13
speech recognition and in [76] for detection of epilepsy in EEG
recordings.
VIII. CONCLUSION
In this paper, we aimed to address the following central
question in the context of medical image analysis: Can the
use of pre-trained deep CNNs, with sufﬁcient ﬁne-tuning,
eliminate the need for training a deep CNN from scratch? Our
extensive experiments, based on 4 distinct medical imaging
applications from 3 different imaging modality systems, have
demonstrated that deeply ﬁne-tuned CNNs are useful for
medical image analysis, performing as well as fully trained
CNNs and even outperforming the latter when limited training
data are available. Our results are important because they
show that knowledge transfer from natural images to medical
images is possible, even though the relatively large difference
between source and target databases is suggestive that such
application may not be possible. We also have observed that
the required level of ﬁne-tuning differed from one application
to another. Speciﬁcally, for PE detection, we achieved per-
formance saturation after ﬁne-tuning the late fully connected
layers; for colonoscopy frame classiﬁcation, we achieved the
highest performance through ﬁne-tuning the late and middle
layers; and for interface segmentation and polyp detection, we
observed the highest performance by ﬁne-tuning all layers in
the pre-trained CNN. Our ﬁndings suggest that for a particular
application, neither shallow tuning nor deep tuning may be
the optimal choice. Through the layer-wise ﬁne-tuning, one
can learn the effective depth of tuning, as it depends on the
application at hand and the amount of labeled data available
for tuning. Layer-wise ﬁne-tuning may offer a practical way
to achieve the best performance for the application at hand
based on the amount of available data. Our experiments
further conﬁrm the potential of CNNs for medical imaging
applications because both deeply ﬁne-tuned CNNs and fully
trained CNNs outperformed the corresponding handcrafted
alternatives.
REFERENCES
[1] K. Fukushima, “Neocognitron: A self-organizing neural network model
for a mechanism of pattern recognition unaffected by shift in position,”
Biological cybernetics, vol. 36, no. 4, pp. 193–202, 1980.
[2] Y. LeCun, L. Bottou, Y. Bengio, and P. Haffner, “Gradient-based learning
applied to document recognition,” Proceedings of the IEEE, vol. 86,
no. 11, pp. 2278–2324, 1998.
[3] Y. LeCun, Y. Bengio, and G. Hinton, “Deep learning,” Nature, vol. 521,
no. 7553, pp. 436–444, 2015.
[4] “Online: available at http://www.technologyreview.com/featuredstory/
513696/deep-learning/,.”
[5] C. Szegedy, W. Liu, Y. Jia, P. Sermanet, S. Reed, D. Anguelov, D. Erhan,
V. Vanhoucke, and A. Rabinovich, “Going deeper with convolutions,”
arXiv preprint arXiv:1409.4842, 2014.
[6] K. Simonyan and A. Zisserman, “Very deep convolutional networks for
large-scale image recognition,” arXiv preprint arXiv:1409.1556, 2014.
[7] M. D. Zeiler and R. Fergus, “Visualizing and understanding convolu-
tional networks,” in Computer Vision–ECCV 2014.
Springer, 2014, pp.
818–833.
[8] D. Eigen, J. Rolfe, R. Fergus, and Y. LeCun, “Understanding deep
architectures using a recursive convolutional network,” arXiv preprint
arXiv:1312.1847, 2013.
[9] D. Erhan, P.-A. Manzagol, Y. Bengio, S. Bengio, and P. Vincent, “The
difﬁculty of training deep architectures and the effect of unsupervised
pre-training,” in International Conference on artiﬁcial intelligence and
statistics, 2009, pp. 153–160.
[10] A. S. Razavian, H. Azizpour, J. Sullivan, and S. Carlsson, “CNN
features off-the-shelf: an astounding baseline for recognition,” in Com-
puter Vision and Pattern Recognition Workshops (CVPRW), 2014 IEEE
Conference on.
IEEE, 2014, pp. 512–519.
[11] H. Azizpour, A. S. Razavian, J. Sullivan, A. Maki, and S. Carlsson,
“From generic to speciﬁc deep representations for visual recognition,”
arXiv preprint arXiv:1406.5774, 2014.
[12] O. Penatti, K. Nogueira, and J. Santos, “Do deep features generalize
from everyday objects to remote sensing and aerial scenes domains?” in
Proceedings of the IEEE Conference on Computer Vision and Pattern
Recognition Workshops, 2015, pp. 44–51.
[13] W. Zhang, K. Doi, M. L. Giger, Y. Wu, R. M. Nishikawa, and R. A.
Schmidt, “Computerized detection of clustered microcalciﬁcations in
digital mammograms using a shift-invariant artiﬁcial neural network,”
Medical Physics, vol. 21, no. 4, pp. 517–524, 1994.
[14] H.-P. Chan, S.-C. B. Lo, B. Sahiner, K. L. Lam, and M. A. Helvie,
“Computer-aided detection of mammographic microcalciﬁcations: Pat-
tern recognition with an artiﬁcial neural network,” Medical Physics,
vol. 22, no. 10, pp. 1555–1567, 1995.
[15] S.-C. B. Lo, S.-L. Lou, J.-S. Lin, M. T. Freedman, M. V. Chien,
S. K. Mun et al., “Artiﬁcial convolution neural network techniques
and applications for lung nodule detection,” Medical Imaging, IEEE
Transactions on, vol. 14, no. 4, pp. 711–718, 1995.
[16] N. Tajbakhsh, S. R. Gurudu, and J. Liang, “A comprehensive computer-
aided polyp detection system for colonoscopy videos,” in Information
Processing in Medical Imaging.
Springer, 2015, pp. 327–338.
[17] ——, “Automatic polyp detection in colonoscopy videos using an
ensemble of convolutional neural networks,” in Biomedical Imaging
(ISBI), 2015 IEEE 12th International Symposium on.
IEEE, 2015,
pp. 79–83.
[18] N. Tajbakhsh and J. Liang, “Computer-aided pulmonary embolism
detection using a novel vessel-aligned multi-planar image representation
and convolutional neural networks,” in Medical Image Computing and
Computer-Assisted Intervention MICCAI 2015, 2015.
[19] D. C. Cires¸an, A. Giusti, L. M. Gambardella, and J. Schmidhuber,
“Mitosis detection in breast cancer histology images with deep neu-
ral networks,” in Medical Image Computing and Computer-Assisted
Intervention–MICCAI 2013.
Springer, 2013, pp. 411–418.
[20] H. Roth, L. Lu, A. Seff, K. Cherry, J. Hoffman, S. Wang, J. Liu,
E. Turkbey, and R. Summers, “A new 2.5d representation for lymph
node detection using random sets of deep convolutional neural network
observations,” in Medical Image Computing and Computer-Assisted
Intervention
MICCAI 2014, ser. Lecture Notes in Computer Science,
P. Golland, N. Hata, C. Barillot, J. Hornegger, and R. Howe, Eds.
Springer International Publishing, 2014, vol. 8673, pp. 520–527.
[21] Y. Zheng, D. Liu, B. Georgescu, H. Nguyen, and D. Comaniciu, “3d
deep learning for efﬁcient and robust landmark detection in volumetric
data,” in Medical Image Computing and Computer-Assisted Intervention
MICCAI 2015, 2015.
[22] J. Y. Shin, N. Tajbakhsh, R. T. Hurst, C. B. Kendall, and J. Liang,
“Automating carotid intima-media thickness video interpretation with
convolutional neural networks,” to appear in Proceedings of the IEEE
Conference on Computer Vision and Pattern Recognition, 2016.
[23] H. R. Roth, A. Farag, L. Lu, E. B. Turkbey, and R. M. Summers, “Deep
convolutional networks for pancreas segmentation in ct imaging,” in
SPIE Medical Imaging. International Society for Optics and Photonics,
2015, pp. 94 131G–94 131G.
[24] M. Havaei, A. Davy, D. Warde-Farley, A. Biard, A. Courville, Y. Bengio,
C. Pal, P.-M. Jodoin, and H. Larochelle, “Brain tumor segmentation with
deep neural networks,” arXiv preprint arXiv:1505.03540, 2015.
[25] W. Zhang, R. Li, H. Deng, L. Wang, W. Lin, S. Ji, and D. Shen, “Deep
convolutional neural networks for multi-modality isointense infant brain
image segmentation,” NeuroImage, vol. 108, pp. 214–224, 2015.
[26] D. Ciresan, A. Giusti, L. M. Gambardella, and J. Schmidhuber, “Deep
neural networks segment neuronal membranes in electron microscopy
images,” in Advances in Neural Information Processing Systems 25,
F. Pereira, C. Burges, L. Bottou, and K. Weinberger, Eds.
Curran
Associates, Inc., 2012, pp. 2843–2851.
[27] A. Prasoon, K. Petersen, C. Igel, F. Lauze, E. Dam, and M. Nielsen,
“Deep feature learning for knee cartilage segmentation using a tripla-
nar convolutional neural network,” in Medical Image Computing and
Computer-Assisted Intervention–MICCAI 2013.
Springer, 2013, pp.
246–253.
[28] Y. Bar, I. Diamant, L. Wolf, and H. Greenspan, “Deep learning with
non-medical training used for chest pathology identiﬁcation,” in SPIE
Medical Imaging. International Society for Optics and Photonics, 2015,
pp. 94 140V–94 140V.


## Page 14


14
[29] B. van Ginneken, A. A. Setio, C. Jacobs, and F. Ciompi, “Off-the-shelf
convolutional neural network features for pulmonary nodule detection
in computed tomography scans,” in Biomedical Imaging (ISBI), 2015
IEEE 12th International Symposium on, April 2015, pp. 286–289.
[30] J. Arevalo, F. Gonzalez, R. Ramos-Pollan, J. Oliveira, and M. Gue-
vara Lopez, “Convolutional neural networks for mammography mass
lesion classiﬁcation,” in Engineering in Medicine and Biology Society
(EMBC), 2015 37th Annual International Conference of the IEEE, Aug
2015, pp. 797–800.
[31] T. Schlegl, J. Ofner, and G. Langs, “Unsupervised pre-training across
image domains improves lung tissue classiﬁcation,” in Medical Com-
puter Vision: Algorithms for Big Data.
Springer, 2014, pp. 82–93.
[32] H. Chen, D. Ni, J. Qin, S. Li, X. Yang, T. Wang, and P. A. Heng, “Stan-
dard plane localization in fetal ultrasound via domain transferred deep
neural networks,” Biomedical and Health Informatics, IEEE Journal of,
vol. 19, no. 5, pp. 1627–1636, Sept 2015.
[33] G. Carneiro, J. Nascimento, and A. Bradley, “Unregistered multiview
mammogram
analysis
with
pre-trained
deep
learning
models,”
in Medical Image Computing and Computer-Assisted Intervention
MICCAI 2015, ser. Lecture Notes in Computer Science, N. Navab,
J. Hornegger, W. M. Wells, and A. F. Frangi, Eds.
Springer
International Publishing, 2015, vol. 9351, pp. 652–660. [Online].
Available: http://dx.doi.org/10.1007/978-3-319-24574-4 78
[34] H.-C. Shin, L. Lu, L. Kim, A. Seff, J. Yao, and R. M. Summers,
“Interleaved text/image deep mining on a very large-scale radiology
database,” in Proceedings of the IEEE Conference on Computer Vision
and Pattern Recognition, 2015, pp. 1090–1099.
[35] M. Gao, U. Bagci, L. Lu, A. Wu, M. Buty, H.-C. Shin, H. Roth, G. Z.
Papadakis, A. Depeursinge, R. M. Summers et al., “Holistic classiﬁ-
cation of ct attenuation patterns for interstitial lung diseases via deep
convolutional neural networks,” in the 1st Workshop on Deep Learning
in Medical Image Analysis, International Conference on Medical Image
Computing and Computer Assisted Intervention, at MICCAI-DLMIA’15,
2015.
[36] J. Margeta, A. Criminisi, R. Cabrera Lozoya, D. C. Lee, and N. Ay-
ache, “Fine-tuned convolutional neural nets for cardiac mri acquisition
plane recognition,” Computer Methods in Biomechanics and Biomedical
Engineering: Imaging & Visualization, pp. 1–11, 2015.
[37] D. H. Hubel and T. N. Wiesel, “Receptive ﬁelds of single neurones in
the cat’s striate cortex,” The Journal of physiology, vol. 148, no. 3, pp.
574–591, 1959.
[38] D. C. Edwards, M. A. Kupinski, C. E. Metz, and R. M. Nishikawa,
“Maximum likelihood ﬁtting of FROC curves under an initial-detection-
and-candidate-analysis model,” Medical physics, vol. 29, no. 12, pp.
2861–2870, 2002.
[39] Y. Jia, E. Shelhamer, J. Donahue, S. Karayev, J. Long, R. Girshick,
S. Guadarrama, and T. Darrell, “Caffe: Convolutional architecture for
fast feature embedding,” arXiv preprint arXiv:1408.5093, 2014.
[40] X. Glorot and Y. Bengio, “Understanding the difﬁculty of training deep
feedforward neural networks,” in International conference on artiﬁcial
intelligence and statistics, 2010, pp. 249–256.
[41] K. He, X. Zhang, S. Ren, and J. Sun, “Delving deep into rectiﬁers:
Surpassing human-level performance on imagenet classiﬁcation,” arXiv
preprint arXiv:1502.01852, 2015.
[42] N. Tajbakhsh, S. Gurudu, and J. Liang, “Automated polyp detection
in colonoscopy videos using shape and context information,” Medical
Imaging, IEEE Transactions on, vol. PP, no. 99, pp. 1–1, 2015.
[43] A. Pabby, R. E. Schoen, J. L. Weissfeld, R. Burt, J. W. Kikendall,
P. Lance, M. Shike, E. Lanza, and A. Schatzkin, “Analysis of colorectal
cancer occurrence during surveillance colonoscopy in the dietary polyp
prevention trial,” Gastrointest Endosc, vol. 61, no. 3, pp. 385–91, 2005.
[44] J. van Rijn, J. Reitsma, J. Stoker, P. Bossuyt, S. van Deventer, and
E. Dekker, “Polyp miss rate determined by tandem colonoscopy: a
systematic review,” American Journal of Gastroenterology, vol. 101,
no. 2, pp. 343–350, 2006.
[45] D. H. Kim, P. J. Pickhardt, A. J. Taylor, W. K. Leung, T. C. Winter,
J. L. Hinshaw, D. V. Gopal, M. Reichelderfer, R. H. Hsu, and P. R. Pfau,
“Ct colonography versus colonoscopy for the detection of advanced
neoplasia,” N Engl J Med, vol. 357, no. 14, pp. 1403–12, 2007.
[46] D. Heresbach, T. Barrioz, M. Lapalus, D. Coumaros, P. Bauret, P. Potier,
D. Sautereau, C. Bousti`ere, J. Grimaud, C. Barth´el´emy et al., “Miss rate
for colorectal neoplastic polyps: a prospective multicenter study of back-
to-back video colonoscopies.” Endoscopy, vol. 40, no. 4, pp. 284–290,
2008.
[47] A. Leufkens, M. van Oijen, F. Vleggaar, and P. Siersema, “Factors
inﬂuencing the miss rate of polyps in a back-to-back colonoscopy study,”
Endoscopy, vol. 44, no. 05, pp. 470–475, 2012.
[48] L. Rabeneck, H. El-Serag, J. Davila, and R. Sandler, “Outcomes of
colorectal cancer in the united states: no change in survival (1986-
1997).” The American journal of gastroenterology, vol. 98, no. 2, p.
471, 2003.
[49] S. A. Karkanis, D. K. Iakovidis, D. E. Maroulis, D. A. Karras, and
M. Tzivras, “Computer-aided tumor detection in endoscopic video using
color wavelet features,” Information Technology in Biomedicine, IEEE
Transactions on, vol. 7, no. 3, pp. 141–152, 2003.
[50] D. K. Iakovidis, D. E. Maroulis, S. A. Karkanis, and A. Brokos, “A
comparative study of texture features for the discrimination of gastric
polyps in endoscopic video,” in Computer-Based Medical Systems, 2005.
Proceedings. 18th IEEE Symposium on.
IEEE, 2005, pp. 575–580.
[51] L. A. Alexandre, N. Nobre, and J. Casteleiro, “Color and position versus
texture features for endoscopic polyp detection,” in BioMedical Engi-
neering and Informatics, 2008. BMEI 2008. International Conference
on, vol. 2.
IEEE, 2008, pp. 38–42.
[52] S. Hwang, J. Oh, W. Tavanapong, J. Wong, and P. de Groen, “Polyp
detection in colonoscopy video using elliptical shape feature,” in Image
Processing, 2007. ICIP 2007. IEEE International Conference on, vol. 2,
2007, pp. II–465–II–468.
[53] J. Bernal, J. Snchez, and F. Vilario, “Towards automatic polyp detection
with a polyp appearance model,” Pattern Recognition, vol. 45, no. 9,
pp. 3166–3182, 2012.
[54] J. Bernal, J. S´anchez, and F. Vilarino, “Impact of image preprocessing
methods on polyp localization in colonoscopy frames,” in Engineering in
Medicine and Biology Society (EMBC), 2013 35th Annual International
Conference of the IEEE.
IEEE, 2013, pp. 7350–7354.
[55] Y. Wang, W. Tavanapong, J. Wong, J. Oh, and P. de Groen, “Part-
based multi-derivative edge cross-section proﬁles for polyp detection
in colonoscopy,” Biomedical and Health Informatics, IEEE Journal of,
vol. PP, no. 99, pp. 1–1, 2013.
[56] S. Y. Park, D. Sargent, I. Spofford, K. Vosburgh, and Y. A-Rahim,
“A colon video analysis framework for polyp detection,” Biomedical
Engineering, IEEE Transactions on, vol. 59, no. 5, pp. 1408–1418, 2012.
[57] N. Tajbakhsh, S. Gurudu, and J. Liang, “A classiﬁcation-enhanced
vote accumulation scheme for detecting colonic polyps,” in Abdominal
Imaging. Computation and Clinical Applications, ser. Lecture Notes in
Computer Science, 2013, vol. 8198, pp. 53–62.
[58] N. Tajbakhsh, C. Chi, S. R. Gurudu, and J. Liang, “Automatic polyp
detection from learned boundaries,” in Biomedical Imaging (ISBI), 2014
IEEE 10th International Symposium on, 2014.
[59] N. Tajbakhsh, S. R. Gurudu, and J. Liang, “Automatic polyp detection
using global geometric constraints and local intensity variation patterns,”
in Medical Image Computing and Computer-Assisted Intervention–
MICCAI 2014.
Springer, 2014, pp. 179–187.
[60] J. Liang and J. Bi, “Computer aided detection of pulmonary embolism
with tobogganing and multiple instance classiﬁcation in CT pulmonary
angiography,” in Information Processing in Medical Imaging. Springer,
2007, pp. 630–641.
[61] K. K. Calder, M. Herbert, and S. O. Henderson, “The mortality
of untreated pulmonary embolism in emergency department patients.”
Annals of emergency medicine, vol. 45, no. 3, pp. 302–310, 2005.
[Online]. Available: http://dx.doi.org/10.1016/j.annemergmed.2004.10.
001
[62] G. Sadigh, A. M. Kelly, and P. Cronin, “Challenges, controversies,
and hot topics in pulmonary embolism imaging,” American Journal
of
Roentgenology,
vol.
196,
no.
3,
2011.
[Online].
Available:
http://dx.doi.org/10.2214/AJR.10.5830
[63] J. Fairﬁeld, “Toboggan contrast enhancement for contrast segmentation,”
in Pattern Recognition, 1990. Proceedings., 10th International Confer-
ence on, vol. 1.
IEEE, 1990, pp. 712–716.
[64] R. M. Haralick, K. Shanmugam, and I. H. Dinstein, “Textural features
for image classiﬁcation,” Systems, Man and Cybernetics, IEEE Trans-
actions on, no. 6, pp. 610–621, 1973.
[65] N. Tajbakhsh, C. Chi, H. Sharma, Q. Wu, S. R. Gurudu, and J. Liang,
“Automatic assessment of image informativeness in colonoscopy,” in Ab-
dominal Imaging. Computational and Clinical Applications.
Springer,
2014, pp. 151–158.
[66] M. Arnold, A. Ghosh, G. Lacey, S. Patchett, and H. Mulcahy, “Indistinct
frame detection in colonoscopy videos,” in Machine Vision and Image
Processing Conference, 2009. IMVIP’09. 13th International.
IEEE,
2009, pp. 47–52.
[67] J. Oh, S. Hwang, J. Lee, W. Tavanapong, J. Wong, and P. C. de Groen,
“Informative frame classiﬁcation for endoscopy video,” Medical Image
Analysis, vol. 11, no. 2, pp. 110–127, 2007.


## Page 15


15
[68] R.-M. Mench´on-Lara and J.-L. Sancho-G´omez, “Fully automatic seg-
mentation of ultrasound common carotid artery images based on ma-
chine learning,” Neurocomputing, vol. 151, pp. 161–167, 2015.
[69] R.-M. Mench´on-Lara, M.-C. Bastida-Jumilla, A. Gonz´alez-L´opez, and
J. L. Sancho-G´omez, “Automatic evaluation of carotid intima-media
thickness in ultrasounds using machine learning,” in Natural and Artiﬁ-
cial Computation in Engineering and Medical Applications.
Springer,
2013, pp. 241–249.
[70] S. Petroudi, C. Loizou, M. Pantziaris, and C. Pattichis, “Segmentation
of the common carotid intima-media complex in ultrasound images
using active contours,” Biomedical Engineering, IEEE Transactions on,
vol. 59, no. 11, pp. 3060–3069, 2012.
[71] X. Xu, Y. Zhou, X. Cheng, E. Song, and G. Li, “Ultrasound intima–
media segmentation using hough transform and dual snake model,”
Computerized Medical Imaging and Graphics, vol. 36, no. 3, pp. 248–
258, 2012.
[72] J. Liang, T. McInerney, and D. Terzopoulos, “United snakes,” Medical
image analysis, vol. 10, no. 2, pp. 215–233, 2006.
[73] H. Sharma, R. G. Golla, Y. Zhang, C. B. Kendall, R. T. Hurst,
N. Tajbakhsh, and J. Liang, “Ecg-based frame selection and curvature-
based roi detection for measuring carotid intima-media thickness,” in
SPIE Medical Imaging. International Society for Optics and Photonics,
2014, pp. 904 016–904 016.
[74] H. Lee, R. Grosse, R. Ranganath, and A. Y. Ng, “Convolutional deep
belief networks for scalable unsupervised learning of hierarchical repre-
sentations,” in Proceedings of the 26th Annual International Conference
on Machine Learning.
ACM, 2009, pp. 609–616.
[75] O. Abdel-Hamid, A.-r. Mohamed, H. Jiang, L. Deng, G. Penn, and
D. Yu, “Convolutional neural networks for speech recognition,” Audio,
Speech, and Language Processing, IEEE/ACM Transactions on, vol. 22,
no. 10, pp. 1533–1545, 2014.
[76] D. Wulsin, J. Gupta, R. Mani, J. Blanco, and B. Litt, “Modeling
electroencephalography waveforms with semi-supervised deep belief
nets: fast classiﬁcation and anomaly measurement,” Journal of neural
engineering, vol. 8, no. 3, p. 036015, 2011.


## Page 16


16
SUPPLEMENTARY MATERIAL
TABLE S1: Statistical comparisons between the FROC curves shown in Fig. 2 for polyp detection (level of signiﬁcance is
α = 0.05). The curves are compared at 0.01 and .001 false positives per frame, because they coincide with the elbows of
the performance curves where they yield relatively higher sensitivity. A red cell indicates that a pair of curves are statistically
different in neither of the chosen operating point whereas a green cell indicates at which operating points a statistically
signiﬁcant difference is observed.
FT:only fc8
FT:fc7-fc8
FT:fc6-fc8
FT:conv5-fc8
FT:conv4-fc8
FT:conv3-fc8
FT:conv2-fc8
FT:conv1-fc8
AlexNet scratch
FT:only fc8
FT:fc7-fc8
10−2,−3
FT:fc6-fc8
10−2,−3
FT:conv5-fc8
10−2,−3
10−2,−3
10−2,−3
FT:conv4-fc8
10−2,−3
10−2,−3
10−2,−3
FT:conv3-fc8
10−2,−3
10−2,−3
10−2,−3
10−3
FT:conv2-fc8
10−2,−3
10−2,−3
10−2,−3
10−2,−3
10−2,−3
10−2,−3
FT:conv1-fc8
10−2,−3
10−2,−3
10−2,−3
10−2,−3
10−2,−3
10−2,−3
AlexNet scratch
10−2,−3
10−2
10−2,−3
10−2,−3
10−2,−3
10−3
10−3
10−2,−3
Handcrafted [42]
10−2,−3
10−2,−3
10−2,−3
10−2,−3
10−2,−3
10−2,−3
10−2,−3
10−2,−3
10−2,−3
TABLE S2: Statistical comparisons between the FROC curves shown in Fig. 4 for pulmonary embolism detection (level of
signiﬁcance is α=0.05). Each cell presents a statistical comparison between a pair of FROC curves at 1, 2, 3, 4, and 5 false
positives per volume. A red cell indicates that the two curves are not statistically different at any of the ﬁve operating points,
but a green cell contains the operating points at which the two curves are statistically different.
FT:only fc8
FT:fc7-fc8
FT:fc6-fc8
FT:conv5-fc8
FT:conv4-fc8
FT:conv3-fc8
FT:conv2-fc8
FT:conv1-fc8
AlexNet scratch
FT:only fc8
FT:fc7-fc8
2,3,4,5
FT:fc6-fc8
1,2,3,4,5
FT:conv5-fc8
1,2,3,4,5
1,2
FT:conv4-fc8
1,2,3,4,5
1,2,3
FT:conv3-fc8
1,2,3,4,5
1,2,3,5
1
FT:conv2-fc8
1,2,3,4,5
1,2,3,4,5
FT:conv1-fc8
1,2,3,4,5
1,2,3,4,5
3
AlexNet scratch
1,2,3,4,5
1,2,3
Handcrafted [60]
1,2,3,4,5
1,2,3,5


## Page 17


17
TABLE S3: Statistical comparisons between the ROC curves shown in Fig. 6 for frame classiﬁcation (level of signiﬁcance is
α=0.05). Each cell presents a statistical comparison between a pair of ROC curves at false positive rate of 10%, 15%, and
20% (0.1, 0.15, and 0.2 on the horizontal axis). A red cell indicates that the two curves are not statistically different at any of
the two operating points, but a green cell contains the operating points at which the two curves are statistically different.
FT:only fc8
FT:fc7-fc8
FT:fc6-fc8
FT:conv5-fc8
FT:conv4-fc8
FT:conv3-fc8
FT:conv2-fc8
FT:conv1-fc8
AlexNet scratch
FT:only fc8
FT:fc7-fc8
0.1
FT:fc6-fc8
0.1
FT:conv5-fc8
0.1,0.15
FT:conv4-fc8
0.1,0.15
FT:conv3-fc8
0.1,0.15
FT:conv2-fc8
0.1,0.15
FT:conv1-fc8
0.1,0.15
AlexNet scratch
0.1
0.1,0.15
0.1,0.15
0.15
Handcrafted [65]
0.2
0.1,0.15,0.2
0.1,0.15,0.2
0.1,0.15,0.2
0.1,0.15,0.2
0.1,0.15,0.2
0.1,0.15,0.2
0.1,0.15,0.2
0.15,0.2
TABLE S4: Statistical comparisons between the boxplots shown in Fig. 9. The p-values larger than 0.05 are highlighted in
red.
Lumen-intima interface
FT:only fc8
FT:fc7-fc8
FT:fc6-fc8
FT:conv5-fc8
FT:conv4-fc8
FT:conv3-fc8
FT:conv2-fc8
FT:conv1-fc8
AlexNet scratch
FT:only fc8
FT:fc7-fc8
p<.0001
FT:fc6-fc8
p<.0001
p<.0001
FT:conv5-fc8
p<.0001
p<.0001
p<.001
FT:conv4-fc8
p<.0001
p<.0001
p<.0001
0.5808
FT:conv3-fc8
p<.0001
p<.0001
p<.0001
0.0638
0.0758
FT:conv2-fc8
p<.0001
p<.0001
p<.0001
0.2501
0.3570
0.2284
FT:conv1-fc8
p<.0001
p<.0001
p<.0001
0.4183
0.5491
0.4650
0.9530
AlexNet scratch
p<.0001
p<.0001
0.7829
p<.05
p<.0001
p<.0001
p<.0001
p<.0001
handCrafted
0.8148
p<.0001
p<.0001
p<.0001
p<.0001
p<.0001
p<.0001
p<.0001
p<.0001
Media-adventitia interface
FT:only fc8
FT:fc7-fc8
FT:fc6-fc8
FT:conv5-fc8
FT:conv4-fc8
FT:conv3-fc8
FT:conv2-fc8
FT:conv1-fc8
AlexNet scratch
FT:only fc8
FT:fc7-fc8
p<.0001
FT:fc6-fc8
p<.0001
p<.0001
FT:conv5-fc8
p<.0001
p<.0001
p<.05
FT:conv4-fc8
p<.0001
p<.0001
p<.0001
p<.05
FT:conv3-fc8
p<.0001
p<.0001
p<.05
0.7904
p<.05
FT:conv2-fc8
p<.0001
p<.0001
p<.05
0.7160
p<.05
0.8854
FT:conv1-fc8
p<.0001
p<.0001
p<.001
0.2474
0.2456
0.2915
0.2313
AlexNet scratch
p<.0001
p<.0001
0.3954
0.2106
p<.05
0.1369
0.0981
p<.05
handCrafted
0.5109
p<.0001
p<.0001
p<.0001
p<.0001
p<.0001
p<.0001
p<.0001
p<.0001

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
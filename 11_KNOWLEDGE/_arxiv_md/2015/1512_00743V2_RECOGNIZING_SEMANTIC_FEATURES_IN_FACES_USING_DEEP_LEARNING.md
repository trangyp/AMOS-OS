---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1512.00743v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1512.00743v2_Recognizing_Semantic_Features_in_Faces_using_Deep_Learning

> Source: 1512.00743v2_Recognizing_Semantic_Features_in_Faces_using_Deep_Learning.pdf

> Pages: 9

---


## Page 1


Recognizing Semantic Features in Faces using Deep Learning
Amogh Gudi
VicarVision
Amsterdam
amogh@vicarvision.nl
Abstract
Human face constantly conveys information, both con-
sciously and subconsciously. However, as basic as it is for
humans to visually interpret this information, it is quite a
big challenge for machines. Conventional semantic facial
feature recognition and analysis techniques mostly lack ro-
bustness and suffer from high computation time. This paper
aims to explore ways for machines to learn to interpret se-
mantic information available in faces in an automated man-
ner without requiring manual design of feature detectors,
using the approach of Deep Learning. In this study, the ef-
fects of various factors and hyper-parameters of deep neu-
ral networks are investigated for an optimal network conﬁg-
uration that can accurately recognize semantic facial fea-
tures like emotions, age, gender, ethnicity etc. Furthermore,
the relation between the effect of high-level concepts on low
level features is explored through the analysis of the similar-
ities in low-level descriptors of different semantic features.
This paper also demonstrates a novel idea of using a deep
network to generate 3-D Active Appearance Models of faces
from real-world 2-D images.
For a more detailed report on this work, please see [1].
1. Introduction
A picture is worth a thousand words, but how many
words is the picture of a face worth? As humans, we make
a number of conscious and subconscious evaluations of a
person just by looking at their face. Identifying a person
can have a deﬁning inﬂuence on our conversation with them
based on past experiences; estimating a person’s age, and
making a judgement on their ethnicity, gender, etc. makes
us sensitive to their culture and habits. We also often form
opinions about that person (that are often highly prejudiced
and wrong); we analyse his or her facial expressions to
gauge their emotional state (e.g. happy, sad), and try to
identify non-verbal communication messages that they in-
tent to convey (e.g. love, threat). We use all of this informa-
tion when interacting with each other. In fact, it has been
argued that neonates, only 36 hours old, are able to inter-
pret some very basic emotions from faces and form prefer-
ences [2]. In older humans, this ability is highly developed
and forms one of the most important skills for social and
professional interactions. Indeed, it is hard to imagine ex-
pression of humour, love, appreciation, grief, enjoyment or
regret without facial expressions.
1.1. Semantic Features in Faces
Predominantly, the following semantic features from the
human face form the primary set of information that can be
directly inferred (or roughly estimated) from faces (with-
out contextual knowledge) by humans (apart from identity):
expressed emotion, age, gender and ethnicity. In addition
to these, certain other ‘add-on’ features like presence of
glasses and facial hair (beard, moustache), that are inher-
ent properties of the face are also considered in this study.
1.2. Objectives and Research Questions
The main objective of this paper is to build and study a
Deep Learning based solution to extract semantic features
from images of faces. This sub-section describes the main
questions that will be researched in the course of achieving
this objective.
The design of a deep neural network for any particu-
lar task involves determining multiple conﬁgurations and
parameters that can ensure that the network is well suited
for the task at hand.
Every such combination of hyper-
parameters affects the output of the system differently.
Therefore, one of the questions that will be researched as
part of this paper is: How could a deep learning tech-
nique adapt to the task of semantic facial feature recogni-
tion? This question is closely followed by determining how
different conﬁgurations, hyper-parameters (of the network),
scale of the input, and addition of pre-processing steps af-
fect the performance and accuracy of the system.
It is known that during the training of a multi-layered
deep neural network, lower layers of the network learn to
recognize low-level patterns (like edges), while the higher
1
arXiv:1512.00743v2  [cs.LG]  19 Oct 2016


## Page 2


Raw Image
Pre-processing
Low Level 
Encoding
Feature 
Transformation
High Level Representation
An
Di
Fe
Ha
Sa
Su
Ne
5
15
25
35
45
55
65
75
85
M
F
Figure 1: Conventional facial feature extraction pipeline
[7].
layers combine these low-level information to determine
higher-level concepts.
With respect to a deep network
trained to recognize different semantic features in faces, the
question that can be asked is: How are the high-level seman-
tic descriptions related to their low-level feature descrip-
tors? How are the low-level descriptors of deep networks,
trained to classify different semantic features in faces, re-
lated to each other?
Finally, there are several attributes in human faces whose
semantics are not easily deﬁned. For example, the contrac-
tion of speciﬁc facial muscles, or the locations of certain
landmarks on the face may not lead to easily interpretable
semantic information. However, such information can be
useful for certain in-depth analysis (e.g., psychological re-
search on human subconsciousness, lie-detection, etc.). A
good representation of this information can be achieved
through a 3-D Active Appearance Model [3] of the face.
This leads to the following research question: Is a deep
learning based method capable of generating 3-D Active
Appearance Models of faces from a 2-D images?
2. Related Work
The typical conventional approach for the task of facial
feature recognition essentially follows the pipeline shown
in Figure 1. Majority of the conventional and commercial
facial analysis methods rely on the Facial Action Coding
System (FACS) [4], which involves identifying various fa-
cial muscles that can cause changes in physical facial ap-
pearance. [3] uses a model based approach called the Ac-
tive Appearance Model [5] to classify emotion while build-
ing a 3-D model of the face that encodes over 500 facial
landmarks from which facial muscular movements (Action
Units, deﬁned by the FACS) can be derived. The Active
Appearance Model is generated using PCA [6] directly on
the pre-processed pixels, and is encoded as the deviation of
a face from the average face. This model is then used to
classify the emotions expressed by the face using a single
layered neural network.
Some of the primary tasks within the ﬁeld of computer
vision are detection, tracking and classiﬁcation. With the
advent of deep learning, the state-of-the-art in all three
of these tasks has considerably improved.
A successful
demonstration of the capability of Deep Learning for the
task of image classiﬁcation/detection was done by Le et al.
in [8]. Their results also showed that the detector can be
sensitive to other non-target high-level categories which it
encounters in the dataset (i.e. the unsupervised face detector
also shows sensitivity to images of human bodies, cats and
other high-level concepts). The study in [9] presents how
important the pooling, rectiﬁcation and contrast normaliza-
tion steps can be in Deep Convolutional Neural Networks.
Hinton and Srivastava successfully demonstrate further im-
provements in training by the use of dropouts in [10, 11].
One of the most successful papers from 2012 showing the
application of Deep Learning methods, speciﬁcally Deep
Convolutional Networks, in image classiﬁcation is [12] by
Krizhevsky et al. Their work focuses on image recogni-
tion on ImageNet [13]. On the same dataset in 2013, work
by Sermanet et al. [14] demonstrated an integrated solu-
tion by the use of Deep Convolutional Neural Networks for
all the three tasks of detection, localization and classiﬁca-
tion. This work attained the state-of-the-art in the Classiﬁ-
cation+Localization task. Baccouche et al. in [15] demon-
strated the use of 3-Dimensional Convolutional Neural Net-
works in combination with Recurrent Neural Networks for
human-action classiﬁcation in videos, thus making use of
spatial as well as temporal information in the frame se-
quences to generate state-of-the-art results.
In the context of this paper, we focus on the task of fa-
cial feature recognition. There is a large body of research
dedicated to this problem, and deep learning has emerged
as a highly promising approach in solving such tasks. A re-
cent study [16] has shown near-human performance using
deep networks in the task of recognizing the identity of a
person from faces. With the use of preprocessing steps like
face alignment and frontalization, and the use of a very large
dataset, a robust and invariant classiﬁer is produced that sets
the state-of-the-art in the Labelled Faces in the Wild dataset
[17]. This work utilises a modiﬁed version of deep convo-
lutional networks, with certain convolutional layers using
unshared weights (while regular convolutional layers share
weights).
In the task of emotion recognition from faces, Tang’s
[18] sets the state-of-the-art on the Facial Expression
Recognition Challenge (FERC) dataset. This is achieved
by implementing a two stage network: a convolutional net-
work trained in a supervised manner on the ﬁrst stage, and a
Support Vector Machine as the second stage trained on the
output of the ﬁrst stage. Recent work by Kahou et al. in
[19] successfully demonstrates a multi-modal deep learning
based framework for emotion recognition in videos.
3. The Experimental Set-up
3.1. The Task
The task of recognizing semantic features in faces is
essentially an umbrella term for deciphering information
encoded in faces in general, both apparent and not-so-
apparent. Thus, it can be viewed as a task of extracting


## Page 3


Figure 2: Dataset examples (Top Row: FERC Dataset, Bot-
tom Row: VV Dataset).
3995
436
4097
7215
4830
3171
4965
467
56
496
895
653
415
607
ANGRY
DISGUST
FEAR
HAPPY
SAD
SURPRISE
NEUTRAL
NUMBER OF SAMPLES
FERC-2013 DATASET DISTRIBUTION
32298 SAMPLES
Train Set
Test Set
(a) FERC Dataset.
200 235
73
79 117
967
551
362 284
67
18
96
44
57
61
17
6
NUMBER OF SAMPLES
AGE
3234 SAMPLES
3266
161
4557
252
47
NUMBER OF SAMPLES
ETHNICITY
8283 SAMPLES
3009
2649
MALE
FEMALE
NUMBER OF SAMPLES
GENDER
5658 SAMPLES
1315 1183 1123
2004
1329 1317 1480
NUMBER OF SAMPLES
EMOTION 
9751 SAMPLES
2979
145
53
NONE
LIGHT HEAVY
NUMBER OF SAMPLES
BEARD
3177 SAMPLES
2956
118
138
NONE
LIGHT
HEAVY
NUMBER OF SAMPLES
MOUSTACHE
3212 SAMPLES
2037
4832
PRESENT
ABSENT
NUMBER OF SAMPLES
GLASSES
6869 SAMPLES
(b) VV Dataset.
Figure 3: Distribution of classes in the datasets.
information from images with the prior knowledge that the
images represent human faces.
A list of such informa-
tion encoded in images of human faces is provided in sub-
section 1.1.
3.2. The Datasets
Two datasets were used for the training and testing of the
network in this paper: The emotion-annotated dataset from
the Facial Expression Recognition Challenge 1, and the
multi-annotated private dataset from VicarVision2 (hereby
referred to as the VV dataset). Examples and the statistics
of the datasets are shown in ﬁgure 2 and 3.
3.3. Pre-processing Steps
It can be difﬁcult for the deep network to be able to han-
dle high variations in the pose of faces, and in lighting con-
ditions of the image. Thus, it becomes necessary to pre-
process the input so as to make the faces more uniform.
1http://www.kaggle.com/c/challenges-in-representation-learning-
facial-expression-recognition-challenge/data
2http://www.vicarvision.nl/
Input Image
Face Localization
Face Alignment
Face Location Normalization
Contrast Normalization
Local Mean Removal
& Image Norm Setting
Global Mean Removal 
& Standardization
Figure 4: The pre-processing pipeline.
The pre-processing steps can be divided into two parts
as they seek to minimize two distinct properties of the input
image: the variation in location and pose of the face, and
the variations in lighting conditions and contrast. The basic
pipeline of the pre-processing steps is illustrated in Figure
4.
Face Location Normalization:
• Find faces in the image using the a face detection al-
gorithm (speciﬁcally, the Viola/Jones face detection al-
gorithm [20]) and extract the face-crop.
• Perform in-plane rotate so as to remove tile of the faces
in the X-Y plane.
• Resize the image such that the approximate scale of
the face is constant. This is done by ensuring that the
distance between the two eyes in the faces is constant.
Global Contrast Normalization
• For each image, subtract the local mean of all pixel
values from the image.
• Set the image norm to be equal to 100.
• For each pixel in each image, subtract the global mean
of pixels at that location throughout the dataset (the
train set), and divide by the standard deviation.
3.4. Training Method
Throughout the experiments mentioned in this paper,
training of the network is done using stochastic gradient de-
scent with momentum in mini-batch mode, with batches of
100 data samples. Negative log-likelihood is used as the ob-
jective function. Learning rate for the training is initialized
to 0.0025, and is linearly decreased to 0.001 over 50 epochs
of training.
Training is evaluated using a validation set, which is
roughly 10% of the size of the total dataset (train set + valid
set + test set). Stopping criteria of the network training is
based on the misclassiﬁcation rate/mean squared error on
the validation set. The network is tested on a test set which
also contains about 10% of the data samples in the dataset.
4. Experiments and Results
In this section, a description of all experiments is given,
and results of the performance of the network on various
test sets are provided. All experiments have been performed
on Nvdia GTX 7603. The theano framework [21] based
pylearn2 library [22] has been primarily used for these ex-
periments.
3http://www.nvidia.com/gtx-700-graphics-cards/gtx-760/


## Page 4


4.1. Experiments on the FERC Dataset
This sub-section describes the experiments conducted
for the emotion recognition task on the FERC Dataset un-
der different network conﬁgurations as well as training pa-
rameters. As a baseline, it is useful to note that a random
classiﬁer produces an accuracy of 14.3%, and a single-layer
softmax regression model gives 28.16% accuracy.
4.1.1
Best Performing Deep Network
The architecture and hyper-parameters for this network are
obtained on the basis of empirical results described later.
The input image in the form of 48 × 48 grayscale pixels
arranged in a 2D matrix is fed to the ﬁrst hidden layer of
the network: A convolutional layer with a kernel size of
5 × 5 having a stride of 1 both dimensions. The number of
parallel feature-maps in this layer is 64. The 44 × 44 out-
put image produced by this layer is passed to a local con-
trast normalization and a max-pooling layer [9] of kernel
size 3 × 3 with a stride of 2 in each dimension (selection
based on previous work in [12, 18]). This results in a sub-
sampling factor of 1/2, and hence the resulting image is of
size 22 × 22. The second hidden layer is also a 64 feature-
map convolutional layer with a kernel size of 5 × 5 (and
stride 1). The output of this layer is a 18 × 18 pixel image,
and this feeds directly into the third hidden layer of the net-
work, which is a convolutional layer of 128 feature maps
with a kernel size of 4 × 4 (and stride 1). Finally, the output
of this layer, which is of dimension 15 × 15, is fed into the
last hidden layer of the network, which is a fully connected
linear layer with 3072 neurons. Dropout is applied to this
fully connected layer, with a dropout probability of 0.2. The
output of this layer is connected to the output layer, which
is composed of 7 neurons, each representing one class la-
bel. Because this dataset has mutually exclusive emotional
expression labels, a softmax operation is performed on the
output of these 7 neurons and the class with the highest ac-
tivation is chosen. All layers in the network are made up of
ReLu units/neurons [23]. This architecture is illustrated in
Figure 5. The network is trained using stochastic gradient
descent, as described in Section 3.4.
The performance of this network on the test set can be
viewed in Figure 6. The network is able to correctly classify
67.12% of the test samples, maintaining an average preci-
sion per class of 59.6%. It can be seen that the network
has over 50% precision for all classes except fear (which is
49.1%). This could be because the visual appearance of a
face expressing fear varies considerably for different peo-
ple, and is often confused with surprise and sadness. It can
be noted from ROC plot that disgust, happy and surprised
show very good discrimination qualities, despite having rel-
atively very few samples in the training set 3a. This could
be due to a relatively large difference in the visual appear-
[48 x 48]
Input 
Layer
Pre-processing
[3 x 3]
Max Pooling
(Stride of 2)
[5x5] x 64
Convolution
al Layer
Local Contrast 
Normalization
[5x5] x 64
Convolution
al Layer
[4x4] x 128
Convolutional 
Layer
[3072]
Fully Connected 
Layer
[7]
Softmax Output 
Layer
[3072]
[15x15]
[18x18]
[22x22]
[44x44]
[44x44]
[48x48]
[48x48]
Figure 5: Architecture of the deep network.
Angry
Disguist
Fear
Happy
Sad
Surprise Neutral
Ground Truth
Neutral Surprise
Sad
Happy
Fear
Disguist Angry
Classification
57.2%
59.5%
49.1%
86.7%
51.0%
81.7%
62.0%
(a) FERC Test set classiﬁcation
confusion matrix.
0.0
0.2
0.4
0.6
0.8
1.0
False Positive Rate
0.0
0.2
0.4
0.6
0.8
1.0
True Positive Rate
Angry [AUC: 0.889]
Disguist [AUC: 0.965]
Fear [AUC: 0.832]
Happy [AUC: 0.960]
Sad [AUC: 0.837]
Surprise [AUC: 0.964]
Neutral [AUC: 0.887]
(b) FERC test set ROC curves
(one-vs-all classes).
Figure 6: Best performance on the FERC Test set: The total
classiﬁcation accuracy of the network was 67.12%, with the
average precision per class being 59.6%.
ance of disgusted faces as compared to other emotions.
Comparison with Sate-of-the-art
The state-of-the-art
results on the complete FERC test set is 69.4% total clas-
siﬁcation accuracy (as reported by Charlie Tang in [18]).
This is achieved by a network with similar architecture, but
with the absence of the face location normalization pre-
processing step and the sofmax layer, along with the ad-
dition of a 2nd stage SVM classiﬁer.
4.1.2
Experiments with Network Size
In this experiment, the width (average number of neurons
per layer) of a convolutional network was altered by chang-
ing the number of feature maps in the network (while keep-
ing the size of the convolutional kernel ﬁxed). The depth
(number of layers) of the network was altered by the ad-
dition or removal of a convolutional layer in the network,
while keeping the fully connected layer always at the last
position.
Figure 7 shows a heat-map table with accuracy for differ-
ent depths and widths of the network. As can be seen, lower
depth and width gives the lowest accuracy, while higher
depth and width provide the highest accuracy. This suggests
the very intuitive fact that larger the network, the better the
performance. Closer examination of these results and the
surface plot in ﬁgure 7 also show that the depth of the net-
work has a higher impact when compared to the width of
the network. However, after 3 layers, this impact seems to


## Page 5


NETWORK DEPTH
NETWORK WIDTH
C
Convolutional Layer
FC Fully Connected Layer
1 Layer 
[ C ]
2 Layers        
[ C + C ]
3 Layers               
[C + C + C ]  
4 Layers                      
[ C + C + C + FC ]
4K
43.57
51.87
56.48
59.25
6K
46.37
61.24
8K
50.17
61.44
10K
52.51
56.74
56.93
61.66
12K
54.53
61.27
14K
55.34
61.96
20K
55.44
57.37
59.17
63.65
(a) Classiﬁcation accuracies of net-
works with varying depth and width.
1 Layer
2 Layers
3 Layers
4 Layers
43
48
53
58
63
4K
6K
8K
10K
12K
14K
16K
18K
20K
ACCURACY (%)
63-64
58-63
53-58
48-53
43-48
(b) Surface plot of clas-
siﬁcation accuracy in the
network depth vs width
space.
Figure 7: Network performance in terms of accuracy with
varying depth vs witdh.
LCN LAYERS
POOLING LAYERS
None
1st        
Layer      
1st, 2nd         
Layers          
1st, 2nd, 3rd            
Layers                  
None 63.65 63.37
63.93
62.50
1st 
Layer 65.17 65.26
64.56
63.97
1st, 2nd 
Layers 64.49 64.74
64.71
64.14
1st, 2nd, 3rd 
Layers 62.79 64.15
64.02
62.37
(a) Classiﬁcation accuracies of net-
works with varying applications of
LCN and max-pooling.
None
1st
1st, 2nd
1st, 2nd, 3rd
62
62.5
63
63.5
64
64.5
65
65.5
66
None
1st
1st, 2nd
1st, 2nd, 3rd
ACCURACY (%)
64.5-65
64-64.5
63.5-64
63-63.5
62.5-63
(b) Surface plot of classiﬁ-
cation accuracy in the ap-
plication of pooling vs LCN
space.
Figure 8: Network performance in terms of accuracy with
varying applications of pooling vs local contrast normaliza-
tion.
get smaller. Similar effects can be seen with the width of
the network.
4.1.3
Experiments with LCN and Pooling
This experiment was conducted in order to determine the
closest-to-optimal combination of Local Contrast Normal-
ization (LCN) and max-pooling within the neural network
layers.
Max-pooling essentially results in a non-linear
down-sampling step, introducing translation invariance and
reducing computational complexity. Local contrast normal-
ization is another well-used step in designing deep architec-
tures, which ensures competition among the activations of
nearby neurons by normalizing them locally with respect to
each other.
For the purpose of this experiment, a network similar to
the one shown in ﬁgure 5, without the pooling and LCN
layers, is considered as the baseline. Max-pooling (with a
kernel size of 3×3 in strides of 2) and LCN are then applied
at three locations within the network: at the outputs of the
ﬁrst, second and third convolutional layers.
The results of this experiment can be seen in Figure 8.
DROPOUT IN FULLY CONNECTED LAYER (LAST HIDDEN LAYER)
DROPOUT IN CONV. LAYERS
(1ST, 2ND, 3RD HIDDEN LAYERS)
0
0.1
0.2
0.3
0.4
0.5
0 65.26 66.93
66.83
67.12
66.41
66.30
0.1 65.26 66.12
66.14
66.77
66.20
65.94
0.2 65.24 65.30
65.35
64.87
64.14
62.80
(a) Classiﬁcation Accuracies of Net-
works with varying dropouts in the
convolutional and fully connected
layers. The dimensions of each cell
are proportional to the dropout prob-
ability.
0
0.1
0.2
0.3
0.4
0.5
62
63
64
65
66
67
68
0
0.1
0.2
ACCURACY (%)
67-68
66-67
65-66
64-65
63-64
62-63
(b) Surface plot of classiﬁca-
tion accuracy in the network
depth vs width space.
Figure 9: Network performance in terms of accuracy with
varying magnitudes of the dropout probability in the ﬁnal
fully connected layer vs the convolutional layers.
Max-pooling the outputs of the ﬁrst convolution layer, after
applying LCN, gives the best results. Simply applying LCN
without pooling the outputs degrades the results, and this
might be because in the absence of pooling, normalizing
the outputs locally leads to extra emphasis on certain non-
informative activations (which otherwise would not have
propagated beyond the pooling stage). Also, applying pool-
ing to the network is relatively more advantageous in the
starting layers of the network. This could be attributed to
the fact that activations of deeper layers represent more in-
formation than the activations of starting layers, and hence
down-sampling these outputs lead to loss of useful informa-
tion.
4.1.4
Experiments with Dropout
Dropout essentially means randomly omitting the neurons
of a layer by a certain probability. Dropout is an important
recent improvement for neural networks. It works equiva-
lent to adding random noise to the representation (randomly
setting outputs of neurons to zero), or performing model av-
eraging, and this helps reduce overﬁtting [10, 11].
In this experiment, the neural network described in Fig-
ure 5 is used, and dropout is applied on its layers during the
training phase with varying magnitudes.
The results of this experiment are shown in Figure 9. It
can be observed that a fully-connected layer with a dropout
probability of 0.3 gives the best performance, and apply-
ing any dropout to the convolutional layers only results in
reduction in performance. These results support the opti-
mzsed network architecture used in [12] where the best per-
formance was obtained by using dropouts only on fully con-
nected layers. This can be attributed to the fact that fully-
connected layers are more prone to overﬁtting, while the
additional noise caused by dropouts could be adversely af-
fecting the convolutional feature detector.


## Page 6


60
62
64
66
68
72 x 72
60 x 60
48 x 48
36 x 36
24 x 24
Figure 10: Classiﬁcation accuracies for various input image
sizes provided to the network.
4.2. Experiments on the VV Dataset
In this sub-section, the details and results of the experi-
ments conducted on the VV Dataset are provided. This time
the experiments do not focus on network optimisation. The
network used for training and testing for recognition of var-
ious features in the dataset has the same architecture as de-
ﬁned in Section 4.1.1, which is the most optimized network
for the FERC dataset. In all the experiments that follow, the
training of the network was done as described in Section
3.4.
4.2.1
Emotion Classiﬁcation
The task of emotion classiﬁcation on the VV Dataset is very
similar to that on the FERC dataset. However, a key differ-
ence between the two datasets is that all the emotion classes
are more uniformly distributed, as can be seen in Figure 3b.
The network produced a total classiﬁcation accuracy of
66.56%, while the average precision was 65.64%. The per-
formance of the network is quite similar to the one seen for
the FERC dataset. The average precision score is closer to
the total classiﬁcation accuracy due to the uniform class dis-
tribution in the dataset. The ROC curves of Happy and Neu-
tral show that they are the best-learned classiﬁcation cate-
gories of the network, although all the other labels also have
a decent amount of area under their curves (>0.9).
Experiments with Input Image Resolution
The results
of ethe experiments using different image sizes can be ob-
served in Figure 10.The performance of the network is
about the same for image sizes of 60 × 60 and 48 × 48,
and reduces smoothly for smaller image sizes. The perfor-
mance of the network drops when image size in increased
to 72 × 72 pixels, and this could be due to the fact that we
are using a constant 5 × 5 sized convolution kernel, and not
scaling it up with the input image size (due to limitations of
computational resources).
Experiments with Pre-processing
It is found that the
global contrast normalization pre-processing step gives a
performance boost of around 3% to the classiﬁcation accu-
racy, while the face alignment step improves the accuracy
by roughly 5%.
4.2.2
Age Classiﬁcation
In this experiment, the age annotations in the VV dataset are
considered, which contain one of 17 exclusive age labels for
0-2
3-7
8-12
13-17
18-22
23-27
28-32
33-37
38-42
43-47
48-52
53-57
58-62
63-67
68-72
73-77
78+
Ground Truth
78+
73-77
68-72
63-67
58-62
53-57
48-52
43-47
38-42
33-37
28-32
23-27
18-22
13-17
8-12
3-7
0-2
Classification
(a) VV dataset age classiﬁcation
confusion matrix.
50
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
±2.5
±5
±7.5
±10
±12.5
±15
ACCURACY (%)
AGE ESTIMATION RESOLUTION (YEARS)
Deep Network Estimation
Human Estimation
(b) Age estimation:
humans
(FG-NET)
[24]
vs
machines
(VV Dataset)
Figure 11: Age classiﬁcation on the VV dataset: The to-
tal classiﬁcation accuracy was 53.12%/72.13% for ±2.5
year/±5 year resolution. The average precision for younger
than 50 years age group was 33.3%/51.7%.
each image. The age labels represent 5 year age intervals
around ages that are multiples of 5 (except for the range [0-
2]). To accommodate this, the ﬁnal softmax layer of our
network architecture is set to have 17 neurons, one for each
age class. The network is trained as usual (as explained in
sub-section 3.4).
Performance of the network on the test set can be seen
in Figure 11: the green squares represent correct classiﬁca-
tion within ±2.5year resolution, while the orange squares
represent correct classiﬁcation within ±5year resolution. It
can be seen that the distribution of age within this dataset
is quite skewed towards the age range of [23-27] (refer Fig-
ure 3b), and the result of this can be seen in the confusion
matrix: there is a bias in the network towards [23-27] age
class. Also note that due to the extreme lack of data sam-
ples in the above 50 age range, the network performance is
severely degraded. This is the main reason for a low average
precision while having a high total classiﬁcation accuracy.
The task of age estimation from faces is something that
humans do inherently. It has been observed that age esti-
mation by humans is accurate only up to a range of ±4.2 to
±7.4 [24]. Figure 11b shows the performance of the deep
network approach to automated age estimation for the VV
dataset vs the age estimation by humans at various resolu-
tions for the FG-NET ageing dataset. Due to the similarity
in the type of images and the reasonably large size of the
FG-NET dataset and the VV dataset, we can assume the
performance of humans to be similar on the VV dataset. As
can be seen, the performance of the deep network estima-
tion is fairly close that of humans.
4.2.3
Gender Classiﬁcation
For this experiment, the deep network was trained on the
gender annotated part of the VV dataset by modifying the
ﬁnal softmax output layer to only contain two neurons (for
male and female).


## Page 7


0.0
0.2
0.4
0.6
0.8
1.0
False Positive Rate
0.0
0.2
0.4
0.6
0.8
1.0
True Positive Rate
Female
(a)
VV
dataset
gender
classiﬁcation ROC (female).
Class. Acc = 90.68%, AP =
88.9%
0.0
0.2
0.4
0.6
0.8
1.0
False Positive Rate
0.0
0.2
0.4
0.6
0.8
1.0
True Positive Rate
Glasses Present [AUC: 0.990]
No Moustache [AUC: 0.906]
Light Moustache [AUC: 0.845]
Heavy Moustache [AUC: 0.974]
No Beard [AUC: 0.865]
Light Beard [AUC: 0.840]
Heavy Beard [AUC: 0.918]
(b) The ROC plot for the network
performance for glasses and facial
hair detection.
Figure 12: Gender and facial hair classiﬁcation on the VV
dataset
M
F M
F M
F M
F F
M
F
M
F
M M
F
Figure 13: Gender misclassiﬁcation examples.
Legend:
Green = Ground Truth, Red = Network classiﬁcation.
The test set performance of the network is plotted in Fig-
ure 12a.The network is able to correctly classify 90.86% of
the faces in the test set, and the ROC curve shows good
discrimination characteristics. Examples of the falsely clas-
siﬁed faces can be seen in Figure 13 where a large portion
of the misclassiﬁed faces are those of young children. The
misclassiﬁed images also include difﬁcult to classify faces
with non-prominent or mixed gender features (see third
from right and second from left in the ﬁgure). Lastly, there
also exist a small portion of examples with incorrect ground
truth (fourth image from left). Overall, a classiﬁcation accu-
racy of above 90% and the presence of such hard-to-classify
faces in the test set suggests that the network performs on a
near human level on the task of gender classiﬁcation.
4.2.4
Ethnicity Classiﬁcation
The VV dataset contains annotations for ﬁve classes of
ethnicity, the ﬁfth one being ‘others’ which includes all
other non-listed ethnic groups like Middle-Eastern, Latin-
American, etc.
The deep network’s ﬁnal softmax output layer was again
altered to ﬁt the annotation by setting the number of neurons
to 5. The network produced a total classiﬁcation accuracy
of 92.24%, with the average precision for all classes being
61.52%. It is also apparent from Figure 3b that the distribu-
tion of classes is highly uneven, with the Caucasian and East
Asian samples being more abundant than African, South
Asian and others. The effect of this can be seen in the per-
formance of the network: the network performs very well
for Caucasian and East Asian faces (above 95% precision),
but the average precision of all classes is only 61.52%. An-
Figure 14: Examples of synthetic faces used for training
the network (bottom), and their source images (top). The
synthetic faces are obtained using AAM.
other important point here is that the network does not use
the color information in the images, and ethnicity is one of
the facial attributes that exhibits a high variance in the color
of the skin.
4.2.5
Detection of Glasses and Facial Hair
The network is trained using the same setup as described
in the previous experiments, with the ﬁnal softmax later al-
tered to have only two neurons for the presence of glasses,
and 3 neurons for the amount of mustache and amount of
beard (none, light, heavy). The performance of the network
on the test sets were as follows: 94.52% accuracy for the
presence of glasses, and 88.1% for the amount of beard and
89.13% for the amount of mustache. The ROC curves for
the classiﬁcation labels are plotted in Figure 12b. As can
be seen, the network’s precision for detecting the presence
of glasses and heavy mustache is very high. However, due
to the slightly ambiguous deﬁnition of light beard class in
the dataset, the network does not learn a very precise light
beard (and no beard) classiﬁers.
4.2.6
AAM Modelling of Faces using Deep Learning
The Active Appearance Model (AAM) [3] produces a 3-D
model of the face using a compressed representation that
encodes the shape and appearance (including texture) of the
face together. As brieﬂy mentioned in Section 2, the AAM
is conventionally produced by applying PCA directly on the
pre-processed pixels of the face image. The shape and ap-
pearance parameters within it are encoded as the deviation
of a face from the average face. Apart from this, it also con-
sists of the pose of the face: the angles made by the normal
of the face with respect to the X, Y and Z axes. However,
as mentioned before in pre=processing sub-section 3.3, the
in-plane rotation of the image removes the X-Y plane tilt of
the face. Finally, this annotation is expressed to the network
in terms of a compressed vector of AAM parameters plus 2
angles.
The network was trained on synthetic faces and their
corresponding Active Appearance Models generated by the
conventional face modelling method described above (see
Figure 14). The reason for using synthetic faces instead of
real faces is that because these synthetic faces are generated
by their corresponding AAM, the modelling error between


## Page 8


Figure 15: Face models generated by the deep network.
the face and the AAM vector is zero.
A cosine similarity score of 0.768 is obtained with the
ground truth when tested on real faces, and a similarity
score of 0.862 when tested on synthetic faces. Moreover,
the pose estimation for the test faces produced an average
error of 2.92◦/1.89◦in the Y/X axes for real faces, and
2.23◦/1.66◦in the Y/X axes for synthetic faces. As can be
seen in Figure 15, the generated face models resemble the
real faces in terms of shape and pose quite well.
4.2.7
Relation between High-level Concepts and Low-
level Descriptors
In all the experiments explained above, the deep network
was required to be trained on speciﬁc annotation-image
pairs for the given task. However, it can be argued that high-
level features in faces (like age, emotions) are just combina-
tions of certain low-level features in faces (like eye-edges,
lip-curl), and many of these low-level features can be com-
mon among different high-level feature descriptions.
Similarity in First-Layer Weights
To study the above
mentioned argument, this sub-section compares the low-
level descriptors that combine to form different higher level
concepts. Careful observation of the ﬁrst convolution layer
reveals a similarity in the general pattern of the weights of
the feature-maps.
Figure 16 illustrates a heat-table of cosine similarity
scores between the ﬁrst layer weights of networks trained
for different high level feature recognition (classiﬁcation
task).
Certain patterns can be observed in these results.
Weights for facial-hair and gender are very similar to those
of age: this could be related to the fact that all females and
all young children have no facial hair, and hence the pres-
ence or absence of facial-hair can be a good indicator of the
person’s gender and age. This could also be the reason for a
high similarity between age and gender weights. Weights of
emotions are dissimilar from the weights of age, ethnicity,
gender, glasses and facial-hair, as these factors do not inﬂu-
ence the facial expressions of a person. On the other hand,
weights of joint classiﬁcation (explained later) are similar
to all the other tasks since joint classiﬁcation involves the
classiﬁcation of all those features.
In general, it could be observed that the given task seems
to have a strong effect on the lower-level descriptors. A
higher correlation in the weights for similar visual tasks is
also observed, while it is seen that visually dissimilar tasks
Emotion 
(VV)
0.83
Age
0.75
0.86
Ethnicity
0.73
0.82
0.87
Gender
0.73
0.83
0.89
0.82
Joint
0.78
0.88
0.93
0.86
0.90
AAM
0.73
0.80
0.81
0.76
0.84
0.86
Glasses
0.69
0.77
0.84
0.76
0.82
0.85
0.84
Moustache
0.74
0.84
0.95
0.85
0.90
0.94
0.84
0.85
Beard
0.71
0.81
0.90
0.79
0.90
0.92
0.89
0.91
0.93
Random
0.03
0.02
0.04
0.04
0.03
0.05
0.03
0.01
0.03
0.03
Emotion 
(FERC)
Emotion 
(VV)
Age
Ethnicity
Gender
Joint
AAM
Glasses
Moustache
Beard
Figure 16:
Cosine inter-similarity scores for ﬁrst-layer
weights learnt by the network for different tasks.
exhibit a lower correlation.
Joint Classiﬁcation Experiment
In order to exploit the
low-level similarity observations from the previous sub-
section, a single network needs to be trained to jointly
classify multiple non-exclusive facial features. In order to
achieve this, the different annotations per image in the VV
Dataset are combined into one single set of image – an-
notation pair, where the annotations are represented by 37
non-exclusive class labels.
The difference between the performance of the joint clas-
siﬁcation network and individual networks was found to be
very small: on average 1.84% ([0.91% - 4.71%]) lower than
the accuracy of individual networks. This suggests that the
deep network is capable of learning to classify multiple se-
mantic features in faces in a joint manner.
5. Conclusion
In this paper, a deep learning based approach has been
demonstrated for the task of semantic facial feature recogni-
tion. This approach is primarily based on the use of convo-
lutional neural networks on two dimensional pre-processed
and aligned images of faces.
A study exploring the ef-
fects of network hyper-parameters on the classiﬁcation per-
formance has been conducted, leading to estimation of the
near-optimal conﬁguration of the network. The study sug-
gests that a deep convolutional network based approach is
naturally well suited for the task of image based facial ex-
pression recognition.
It is shown that addition of deter-
ministic pre-processing and alignment steps for the input
data greatly aids in improving the performance.
Such a
deep network can easily be adapted to the tasks of recog-
nizing additional semantic features. Experimental results
have shown near-human performance. However, the dis-
crimination power of deep networks are highly dependent
on the distribution and quality of the training data. The rela-
tion between the high-level semantic features and low-level
descriptors has also been studied. Speciﬁc intuitive similar-
ities have been observed between the low-level descriptors
for different tasks. Use of this commonality among low-
level descriptors is demonstrated by training a single net-
work to jointly classify multiple semantic facial features.


## Page 9


Finally, a novel scheme for training deep networks to gener-
ate complete 3-D Active Appearance Models of faces from
2-D images has been shown. To our best knowledge this is
the ﬁrst time deep networks is used to predict a compressed
image representation and this task has also been success-
fully achieved by the network.
References
[1] Amogh Gudi. Recognizing semantic features in faces using
deep learning.
Master’s thesis, University of Amsterdam,
2015. arXiv preprint arXiv:1512.00743v1. 1
[2] Teresa Farroni, Enrica Menon, Silvia Rigato, and Mark H
Johnson. The perception of facial expressions in newborns.
European Journal of Developmental Psychology, 4(1):2–13,
2007. 1
[3] Hans Van Kuilenburg, Marco Wiering, and Marten Den Uyl.
A model based method for automatic facial expression
recognition. In Machine Learning: ECML 2005, pages 194–
205. Springer, 2005. 2, 7
[4] Paul Ekman and Erika L Rosenberg. What the face reveals:
Basic and applied studies of spontaneous expression using
the Facial Action Coding System (FACS). Oxford University
Press, 1997. 2
[5] Timothy F Cootes, Christopher J Taylor, et al.
Statistical
models of appearance for computer vision, 2004. 2
[6] Lawrence Sirovich and Michael Kirby.
Low-dimensional
procedure for the characterization of human faces. JOSA A,
4(3):519–524, 1987. 2
[7] Haoqiang Fan, Zhimin Cao, Yuning Jiang, Qi Yin, and Chin-
chilla Doudou. Learning deep face representation. arXiv
preprint arXiv:1403.2802, 2014. 2
[8] Quoc Le, Marc’Aurelio Ranzato, Rajat Monga, Matthieu
Devin, Kai Chen, Greg Corrado, Jeff Dean, and Andrew Ng.
Building high-level features using large scale unsupervised
learning. In International Conference in Machine Learning,
2012. 2
[9] Yann LeCun, Koray Kavukcuoglu, and Cl´ement Farabet.
Convolutional networks and applications in vision. In Cir-
cuits and Systems (ISCAS), Proceedings of 2010 IEEE In-
ternational Symposium on, pages 253–256. IEEE, 2010. 2,
4
[10] Geoffrey E Hinton, Nitish Srivastava, Alex Krizhevsky, Ilya
Sutskever, and Ruslan R Salakhutdinov. Improving neural
networks by preventing co-adaptation of feature detectors.
arXiv preprint arXiv:1207.0580, 2012. 2, 5
[11] Nitish Srivastava. Improving neural networks with dropout.
PhD thesis, University of Toronto, 2013. 2, 5
[12] Alex Krizhevsky, Ilya Sutskever, and Geoffrey E Hinton.
Imagenet classiﬁcation with deep convolutional neural net-
works. In Advances in neural information processing sys-
tems, pages 1097–1105, 2012. 2, 4, 5
[13] Jia Deng, Wei Dong, Richard Socher, Li-Jia Li, Kai Li,
and Li Fei-Fei.
Imagenet: A large-scale hierarchical im-
age database. In Computer Vision and Pattern Recognition,
2009. CVPR 2009. IEEE Conference on, pages 248–255.
IEEE, 2009. 2
[14] Pierre Sermanet, David Eigen, Xiang Zhang, Micha¨el Math-
ieu, Rob Fergus, and Yann LeCun.
Overfeat: Integrated
recognition, localization and detection using convolutional
networks. arXiv preprint arXiv:1312.6229, 2013. 2
[15] Moez
Baccouche,
Franck
Mamalet,
Christian
Wolf,
Christophe Garcia, and Atilla Baskurt.
Sequential deep
learning for human action recognition. In Human Behavior
Understanding, pages 29–39. Springer, 2011. 2
[16] Yaniv Taigman, Ming Yang, Marc’Aurelio Ranzato, and Lior
Wolf.
Deepface: Closing the gap to human-level perfor-
mance in face veriﬁcation. In Proceedings of the IEEE Con-
ference on Computer Vision and Pattern Recognition, pages
1701–1708, 2013. 2
[17] Gary B Huang and Erik Learned-Miller. Labeled faces in the
wild: Updates and new reporting procedures. 2
[18] Yichuan Tang. Deep learning using linear support vector ma-
chines. In Workshop on Challenges in Representation Learn-
ing, ICML, 2013. 2, 4
[19] Samira Ebrahimi Kahou, Xavier Bouthillier, Pascal Lam-
blin, Caglar Gulcehre, Vincent Michalski, Kishore Konda,
S´ebastien Jean, Pierre Froumenty, Aaron Courville, Pascal
Vincent, et al.
Emonets: Multimodal deep learning ap-
proaches for emotion recognition in video. arXiv preprint
arXiv:1503.01800, 2015. 2
[20] Paul Viola and Michael Jones. Rapid object detection using
a boosted cascade of simple features. In Computer Vision
and Pattern Recognition, 2001. CVPR 2001. Proceedings of
the 2001 IEEE Computer Society Conference on, volume 1,
pages I–511. IEEE, 2001. 3
[21] James Bergstra, Olivier Breuleux, Fr´ed´eric Bastien, Pascal
Lamblin, Razvan Pascanu, Guillaume Desjardins, Joseph
Turian, David Warde-Farley, and Yoshua Bengio. Theano:
a CPU and GPU math expression compiler. In Proceedings
of the Python for Scientiﬁc Computing Conference (SciPy),
June 2010. Oral Presentation. 3
[22] Ian J. Goodfellow, David Warde-Farley, Pascal Lamblin,
Vincent Dumoulin, Mehdi Mirza, Razvan Pascanu, James
Bergstra, Fr´ed´eric Bastien, and Yoshua Bengio. Pylearn2:
a machine learning research library.
arXiv preprint
arXiv:1308.4214, 2013. 3
[23] Vinod Nair and Geoffrey E Hinton. Rectiﬁed linear units im-
prove restricted boltzmann machines. In Proceedings of the
27th International Conference on Machine Learning (ICML-
10), pages 807–814, 2010. 4
[24] Hu Han, Charles Otto, and Anil K Jain.
Age estimation
from face images: Human vs. machine performance. In Bio-
metrics (ICB), 2013 International Conference on, pages 1–8.
IEEE, 2013. 6

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
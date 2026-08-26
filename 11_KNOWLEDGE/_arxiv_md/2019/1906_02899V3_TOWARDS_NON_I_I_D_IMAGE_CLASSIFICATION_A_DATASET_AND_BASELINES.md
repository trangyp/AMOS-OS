---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1906.02899v3
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1906.02899v3_Towards_Non-I_I_D__Image_Classification__A_Dataset_and_Baselines

> Source: 1906.02899v3_Towards_Non-I_I_D__Image_Classification__A_Dataset_and_Baselines.pdf

> Pages: 28

---


## Page 1


Towards Non-I.I.D. Image Classiﬁcation: A Dataset and
Baselines
Yue Hea,1, Zheyan Shena,1, Peng Cui a,2,∗
aLab of Media and Network, Room 9-316, East Main Building, Tsinghua University, Beijing 100084,
P.R.China
Abstract
I.I.D.1 hypothesis between training and testing data is the basis of numerous image
classiﬁcation methods. Such property can hardly be guaranteed in practice where the
Non-IIDness is common, causing instable performances of these models. In literature,
however, the Non-I.I.D.2 image classiﬁcation problem is largely understudied.
A key
reason is lacking of a well-designed dataset to support related research. In this paper,
we construct and release a Non-I.I.D. image dataset called NICO3, which uses contexts
to create Non-IIDness consciously. Compared to other datasets, extended analyses prove
NICO can support various Non-I.I.D. situations with suﬃcient ﬂexibility. Meanwhile, we
propose a baseline model with ConvNet structure for General Non-I.I.D. image classiﬁca-
tion, where distribution of testing data is unknown but diﬀerent from training data. The
experimental results demonstrate that NICO can well support the training of ConvNet
model from scratch, and a batch balancing module can help ConvNets to perform better
in Non-I.I.D. settings.
Keywords:
Non-I.I.D., Dataset, Context, Bias, ConvNet, Batch Balancing.
1I.I.D.: Independent and Identically Distributed
2Non-I.I.D: Non-Independent and Identically Distributed
3NICO: Non-I.I.D. Image dataset with Contexts
∗Corresponding author
Email addresses: heyue18@mails.tsinghua.edu.cn (Yue He ), shenzy17@mails.tsinghua.edu.cn
(Zheyan Shen ), cuip@tsinghua.edu.cn (Peng Cui )
1Ph.D candidate, Department of Computer Science and Technology, Tsinghua University
2Associate Professor (Tenured), Department of Computer Science and Technology, Tsinghua Univer-
sity
arXiv:1906.02899v3  [cs.CV]  14 Aug 2019


## Page 2


1. Introduction
In recent years, machine learning has achieved remarkable progress, mainly owing
to the development of deep neural networks [1, 2, 3, 4, 5, 6]. One basic hypothesis of
machine learning models is that the training and testing data should consist samples In-
dependent and Identically Distributed (I.I.D.). However, this ideal hypothesis is fragile
in real cases where we can hardly impose constraints on the testing data distribution.
This implies that the model minimizing empirical error on training data does not nec-
essarily perform well on testing data, leading to the challenge of Non-I.I.D. learning.
The problem is more serious when the training samples are not suﬃcient to approximate
the training distribution itself. How to develop Non-I.I.D. learning methods that are
robust to distribution shifting is of paramount signiﬁcance for both academic research
and industrial applications.
Benchmark datasets, providing a common ground for competing approaches, are al-
ways important to promote the development of a research direction. Take image classi-
ﬁcation, a prominent learning task, as an example. Its development beneﬁts a lot from
the benchmark datasets, such as PASCAL VOC [7], MSCOCO [8], and ImageNet [9].
In particular, it is the ImageNet, a large-scale and well-structured image dataset, that
successfully demonstrates the capability of deep learning and thereafter signiﬁcantly ac-
celerates the advancement of deep convolutional neural networks. On these datasets, it
is easy to establish an I.I.D. image classiﬁcation setting by random data splitting. But
they do not provide an explicit option to simulate a Non-I.I.D. setting. The dataset that
can well support the research on Non-I.I.D. image classiﬁcation is still in vacancy.
In this paper, we construct and release a dataset that is dedicately designed for Non-
I.I.D. image classiﬁcation, named NICO (Non-I.I.D. Image dataset with Contexts). The
basic idea is to label images with both main concept and contexts. For example, in the
category of ‘dog’, images are divided into diﬀerent contexts such as ‘grass’, ‘car’, ‘beach’,
meaning the ‘dog’ is on the grass, in the car, or on the beach respectively. With these
contexts, one can easily design an Non-I.I.D. setting by training a model in some contexts
and testing it in the other unseen contexts. Meanwhile, the degree of distribution shift
2


## Page 3


can be ﬂexibly controlled by adjusting the proportions of diﬀerent contexts in training
and testing data. Till now, NICO contains 19 classes, 188 contexts and nearly 25,000
images in total.
The scale is still increasing, and the current scale has been able to
support the training of deep convolution networks from scratch.
The NICO dataset can support, but not limited to, two typical settings of Non-I.I.D.
image classiﬁcation. One is Targeted Non-I.I.D. image classiﬁcation, where testing data
distribution is known but diﬀerent from training data distribution. The other is General
Non-I.I.D. image classiﬁcation, where testing data distribution is unknown and diﬀerent
from training data distribution. Apparently, the latter one is much more realistic and
challenging. A model learned in one environment could be possibly applied in many
other environments. In this case, the robustness of a model in the environments with
unknown distribution shift is a highly favorable characteristic. It is especially critical in
risk-sensitive applications like medical and security.
Due to the lack of a well-structured and reasonable-scaled dataset, there is still no
convolutional neural network model proposed to address the general Non-I.I.D. image
classiﬁcation problem. In this paper, we propose a novel model CNBB3 (ConvNet with
Batch Balancing) as a baseline of exploiting CNN model for general Non-I.I.D. image
classiﬁcation.The experimental results show that the proposed batch balancing mecha-
nism can help a ConvNet model to resist, to some extent, the negative eﬀect brought by
Non-IIDness.
2. Non-I.I.D. Image Classiﬁcation
2.1. Problem Deﬁnition
We ﬁrst give a formal deﬁnition of Non-I.I.D. image classiﬁcation as follow:
Problem 1. (Non-I.I.D. Image Classiﬁcation) Given the training data Dtrain =
(Xtrain, Ytrain), where Xtrain ∈Rn×(c×h×w) represents the images and Ytrain ∈Rn×1
represents the labels. The task is to learn a feature extractor gϕ(·) and a classiﬁer fθ(·),
3CNBB: ConvNet with Batch Balancing
3


## Page 4


so that fθ(gϕ(·)) can predict the labels of testing data Dtest = (Xtest, Ytest) precisely,
where gϕ(·) ∈Rn×p and ψ(Dtrain) ̸= ψ(Dtest). Moreover, according to the availability
of the prior knowledge on testing data, we further deﬁne two diﬀerent tasks. One is Tar-
geted Non-I.I.D. Image Classiﬁcation where the testing data distribution ψ(Dtest)
is known. The other is General Non-I.I.D. Image Classiﬁcation, which corresponds
to a more realistic scenario where the testing data distribution ψ(Dtest) is unknown.
In order to intuitively quantify the degree of distribution shift between ψ(Dtrain) and
ψ(Dtest), we deﬁne the Non-I.I.D. Index as follow:
Deﬁnition 1. Non-I.I.D. Index (NI) Given a feature extractor gϕ(·) and a class C,
the degree of distribution shift between training data DC
train and testing data DC
test is
deﬁned as:
NI(C) =





gϕ(XC
train) −gϕ(XC
test)
σ(gϕ(XC))





2
,
where XC = XC
train ∪XC
test, (·) represents the ﬁrst order moment, σ(·) is the std used to
normalize the scale of features and ∥·∥2represents the 2-norm.
2.2. Existence of Non-IIDness
In real cases, the I.I.D. hypothesis can never be strictly satisﬁed, meaning that Non-
IIDness ubiquitously exists in previous datasets [10].
Here we take ImageNet as an
example. ImageNet is in a hierarchical structure, where each class (e.g. dog) contains
multiple subclasses (e.g. diﬀerent kinds of dogs). For each subclass, it provides training
and testing (validation) subsets of images. To verify the Non-IIDness in ImageNet, we
select 10 common animal classes (e.g.
dog, cat) and construct a new dataset using
10 instantiated subclasses (e.g. Labrador, Persian), each randomly drawn from those
classes. Using the training and testing subsets, we train and evaluate a ConvNet on
image classiﬁcation task. The structure of the ConvNet used in this paper is similar to
AlexNet (details seen in Appendix), and we take the last FC layer of the ConvNet as
the feature extractor gϕ. Note that model structure is used in all subsequent analysis
(including on NICO) for fair comparison, and thus selected by trading-oﬀperformance
and required training data scale. But as a base model with suﬃcient learning capacity,
4


## Page 5


Figure 1: NI (represented by the bar-type) and testing error (represented by the curve-type) of each
class in Dataset A.
the speciﬁc model structure does not aﬀect the conclusions. We repeat this collection
procedure for 3 times, obtain 3 new datasets (Dataset A, Dataset B and Dataset C)
and calculate the NI and testing error for each class respectively. As an example, we
plot the results of DatasetA in Figure 1. We can ﬁnd that:
• NI is above zero for all classes, which implies the Non-IIDness between training
and testing data is ubiquitous even in large-scale datasets like ImageNet.
• Diﬀerent classes have diﬀerent NI values and higher NI value corresponds to higher
testing error.
The strong correlation between NI and testing error can be further proved by their
high pearson correlation [11] coeﬃcients (r = 0.95) and small p value (2e-15).
The
showcase and statistical analysis well support an plausible conclusion that the degree of
distribution shift quantiﬁed by NI is a key factor inﬂuencing classiﬁcation performance.
Although the numerical value of NI is conditioned on speciﬁc feature extractor, we could
use it to analyse the trend of distribution bias by some intervention between training
and testing data, if feature extractor is ﬁxed. In later paragraph, we use NI to make
an empirical analysis on the new dataset we construct to prove that NICO can support
various Non-I.I.D. situations ﬂexibly and consciously.
5


## Page 6


Figure 2: NI of each class in 3 diﬀerent datasets constructed from ImageNet. Diﬀerent datasets instan-
tiate the same classes with diﬀerent subclasses.
2.3. Limitations of Existing Datasets
Throughout the development of computer vision research, benchmark datasets have
always played a critical role on both providing a common ground for algorithm evaluation
and driving new directions. Speciﬁcally, for image classiﬁcation task, we can enumerate
several milestone datasets such as PASCAL VOC, MSCOCO and ImageNet. However,
existing benchmark datasets cannot well support the Non-I.I.D image classiﬁcation. First
of all, despite the manifested Non-IIDness in ImageNet and other datasets, as shown in
Figure 1, the overall degree of distribution shift between training and testing data for
each class is relatively small, making these datasets less challenging from the angle of
Non-I.I.D. image classiﬁcation. More importantly, there is no explicit way to control the
degree of distribution shift between training and testing data in the existing datasets.
As illustrated in Figure 2, if we instantiate the same class with diﬀerent subclasses in
ImageNet and obtain 3 datasets with identical structure, the NI of a given class is fairly
unstable across diﬀerent datasets. Without a controllable way to simulate diﬀerent levels
of Non-IIDness, competing approaches cannot be evaluated fairly and systematically on
those datasets. Those said, a dataset that is dedicatedly designed for Non-I.I.D. image
classiﬁcation is demanded.
6


## Page 7


3. The NICO Dataset
In this section, we introduce the properties and collection process of the dataset,
followed by preliminary empirical results in diﬀerent Non-I.I.D. settings supported by
this dataset.
3.1. Context for Non-I.I.D. Images
The essential idea of generating Non-I.I.D. images is to enrich the labels of an image
with both conceptual and contextual labels. Diﬀerent from previous datasets that only
label an image with the major concept (e.g. dog), we also label the concrete context (e.g.
on grass) that the concept appears in. Then it is easy to simulate an Non-I.I.D. setting
by training and testing the model of a concept with diﬀerent contexts. A good model
for Non-I.I.D. image classiﬁcation is expected to perform well in both training contexts
and testing contexts.
In NICO, we mainly incorporate two kinds of contexts.
One is the attributes of
a concept (or object), such as color, action, and shape. Some examples of ‘context +
concept’ pairs include white bear, climbing monkey and double decker etc. The other kind
of contexts is the background or scene of a concept. The examples of ‘context + concept’
pairs include cat on snow, horse aside people and airplane in sunrise etc. Samples of
diﬀerent contexts in the NICO dataset are shown in Figure 3.
In order to provide more ﬂexible Non-I.I.D. settings, we tend to select the contexts
that occur in multiple concepts.
Then for a given concept, a context may occur in
both positive samples and negative samples (that are sampled from other concepts).
This provides another ﬂexibility to let a context included in training positive samples
appear or do not appear in training negative samples, which will yield diﬀerent Non-I.I.D.
settings.
3.2. Data Collection and Statistics
Referring to ImageNet, MSCOCO and other classical datasets [12, 13], we ﬁrst conﬁrm
two superclasses: Animal and V ehicle. For each superclass, we select classes from the
272 candidates in MSCOCO, with the criterion that the selected classes in a superclass
7


## Page 8


Figure 3: Samples with contexts in NICO. Images in the ﬁrst row are dogs of Animal, assigned to
diﬀerent contexts below it.
The second and third row correspond to horse of Animal and boat of
V ehicle respectively.
should have large inter-class diﬀerences. For context selection, we exploit YFCC100m[14]
broswer4 and ﬁrst derive the frequently co-occurred tag list for a given concept (i.e. class
label). We then ﬁlter out the tags that occur in only a few concepts. Finally, we manually
screen all tags and select the ones that are consistent with our deﬁnition of contexts (i.e.
object attributes or backgrounds and scenes).
After obtaining the conceptual and contextual tags, we concatenate a given conceptual
tag and each of its contextual tags to form a query, input the query into the API of Google
and Bing image search, and collect the top-ranked images as candidates. Finally, in the
phase of screening, we select images into the ﬁnal dataset according to the following
criteria:
• The content of an image should correctly reﬂects its concept and context.
• Given a class, the number of images in each context should be adequate and as
balance as possible across contexts.
Note that we do not conduct image registration or ﬁltering by object centralization,
so that the selected images are more realistic and in wild than those in ImageNet.
4http://www.yfcc100m.org/
8


## Page 9


Table 1: Data size of each class in NICO.
Animal
Data Size
V ehicle
Data Size
Bear
1609
Airplane
930
Bird
1590
Bicycle
1639
Cat
1479
Boat
2156
Cow
1192
Bus
1009
Dog
1624
Car
1026
Elephant
1178
Helicopter
1351
Horse
1258
Motorcycle
1542
Monkey
1117
Train
750
Rat
846
Truck
1000
Sheep
918
The NICO dataset will be continuously updated and expanded. Till now, there are
two superclasses: Animal and V ehicle, with 10 classes for Animal and 9 classes for
vehicle. Each class has 9 or 10 contexts. The average size of contexts per class ranges
from 83 to 215, and the average size of classes is about 1300 images, which is similar
to ImageNet. In total, there are 25,000 images in the NICO dataset. As NICO is in a
hierarchical structure, it is easy to be expanded. More statistics on NICO is reported in
Table 1. The dataset can be downloaded through the link5 or the link6 for Chinese.
3.3. Supported Non-I.I.D. Settings
By dividing a class into diﬀerent contexts, NICO provides the ﬂexibility of simulating
Non-I.I.D. settings in diﬀerent levels. To name a few, here we list 4 typical settings.
Setting 1. Minimum bias. Given a class, we can ignore the contexts, and randomly
split all images of the class into training and testing subsets as positive
samples. Then we can randomly sample images belonging to other classes
5https://www.dropbox.com/sh/8mouawi5guaupyb/AAD4fdySrA6fn3PgSmhKwFgva?dl=0
6https://pan.baidu.com/s/1277mgM-Nju6REd5h3xXlrA
9


## Page 10


into training and testing subsets as negative samples. In this setting, the way
of random sampling lead to minimum distribution shift between training and
testing distributions in the dataset, which simulates a nearly i.i.d. scenario.
Setting 2. Proportional bias. Given a class, when sampling positive samples, we use
all contexts for both training and testing, but the percentage of each context
is diﬀerent in training and testing subsets.
For example, we can let one
context take the majority in training data while taking minority in testing,
which is consistent with the natural phenomena that visual concepts follow
a power law distribution[15].The negative sampling process is the same as
Setting 1. In this setting, the level of distribution shift can be tuned by
adjusting the proportion diﬀerence between training and testing subsets for
each context.
Setting 3. Compositional bias.
Given a class, not every testing context that the
positive samples belong to appears in training subset simultaneously.Such a
setting is quite common in real scene, because available datasets could not
contain all the potential contexts in nature due to the limitations of sampling
time and space.Intuitively, the distribution shift from observed contexts to
unseen contexts is usually large. The less number of testing contexts ob-
served in training generally leads to the higher distribution shift.A more
radical distribution shift can be further achieved by combining compositional
bias and proportional bias.
Setting 4. Adversarial bias. Given a class, the positive sampling process is the same
as Setting 3. For negative sampling, we tend to select the negative samples
from the contexts that have not been (or have been) included in positive
training samples to form the negative training (or testing) subset. In this
way, the distribution shifting is even higher than Setting 3, and the existing
classiﬁcation model developed under i.i.d. assumption are more prone to be
confused.
The above 4 settings are designed to generate Non-I.I.D. training and testing sub-
10


## Page 11


(a) Average NI over all classes in Animal superclass with respect to various dominant ratio of training
data, while the dominant ratio of testing data is ﬁxed to 1:1 (uniform sampling).
(b) Average NI over all classes in Animal superclass with respect to various dominant ratio of testing
data, while the dominant ratio of training data is ﬁxed to 5:1.
Figure 4: NI in proportional bias setting.
sets. Under each setting, we can conduct either Targeted or General Non-I.I.D. image
classiﬁcation by assuming the distribution of testing subset is known or unknown.
3.4. Empirical Analysis
To verify the eﬀectiveness of NICO in supporting Non-I.I.D image classiﬁcation, we
conduct a series of empirical analysis. It is worth noting that, in each setting, only the
distribution of training or testing data change, while the structure of ConvNet and the
size of training data keep the same.
3.4.1. Minimum Bias Setting
In this setting, we randomly sample 8000 images for training and 2000 images for
testing from Animal and V ehicle superclasses respectively. The average testing accuracy
and NI over all the classes are 49.6%, 3.85 for Animal superclass and 63.0%, 3.20 for
V ehicle superclass. We can ﬁnd that NI in NICO is much higher than NI in ImageNet
even if there is no explicit bias (due to random sampling) when we construct the training
11


## Page 12


Figure 5: NI in compositional bias setting: average NI over all classes in V ehicle superclass with respect
to the number of contexts used in training data.
and testing subsets. This is because the images in NICO are typically non-iconic images
with rich contextual information and non-canonical viewpoints, which is more challenging
from the perspective of image classiﬁcation.
Figure 6: NI in the combined setting of compotisional bias and proportional bias: average NI over all
classes in V ehicle superclass with respect to various dominant ratio of training data, where contexts in
testing data is totally unseen in training.
3.4.2. Proportional Bias Setting
In this setting, we let all the contexts appear in both training and testing data, and
randomly select one dominant context in training data (or testing data) for each class
in Animal superclass. Such experimental settings comply with the natural phenomena
that a majority of visual contexts are rare except a few common ones [15]. Speciﬁcally,
we deﬁne the dominant ratio as follow:
Dominant Ratio = Ndominant
Nminor
,
12


## Page 13


where Ndominant refers to the sample size of the dominant context and Nminor refers to
the average size of other contexts where we uniformly sample other contexts. We conduct
two experiments where either dominant ratio of training data or testing data is ﬁxed,
and vary the other one. We plot the results in Figure 4 (a) and Figure 4 (b). From
the ﬁgures, we can clearly ﬁnd a consistent pattern that the NI becomes higher as the
discrepancy between dominant ratio of training data and testing data becomes larger.
As a result, by tuning the dominant ratio of training data (or testing data), we can easily
simulate diﬀerent extents of distribution shift as we want.
Figure 7: NI in the adversarial bias setting: NI of target class with respect to the number of confounding
contexts.
3.4.3. Compositional Bias Setting
Compared to proportional bias setting, compositional bias setting simulates a condi-
tion where the knowledge obtained from training data is insuﬃcient to characterize the
whole distribution. To doing so, we choose a subset of contexts for a given class when
constructing the training data and test the model with all the contexts. By varying the
number of contexts observed in training data, we can simulate diﬀerent extents of infor-
mation loss and distribution shift. From Figure 5, we can ﬁnd that the NI consistently
decreases when we observed more contexts in training data. A more radical distribution
shift can be achieved by combining the notion of proportional bias and compositional
bias. Given a particular class in V ehicle superclass, We choose 7 contexts for training
13


## Page 14


and the other 3 contexts for testing, and further let one context dominate the training
data. By doing so, we can obtain a more severe Non-I.I.D. condition between training
and testing data than previous two settings, as illustrated by the results from Figure 6.
3.4.4. Adversarial Bias Setting
Given a target class, we deﬁne a context as confounding context if it only appears
in the negative samples of training data and positive samples of testing data. In this
experiment, we choose four classes in Animal superclass as target classes and report the
NI w.r.t various number of confounding contexts in Figure 7. The experimental results
indicate that the number of confounding contexts has consistent inﬂuence on the NI of
diﬀerent classes. Given any target class, we can simulate a more harsh distribution shift
and further confuse the ConvNet by adding more confounding contexts.
Figure 8: Range of average NI over Animal superclass for diﬀerent settings supported in NICO.
Finally, we show the range of NI in diﬀerent Non-I.I.D. settings in Figure 8. We can
see the level of NI in NICO is signiﬁcantly higher than ImageNet, and there is an obvious
ascending trend from Minimum Bias to Adversarial Bias settings.
4. General Non-I.I.D. Image Classiﬁcation
In this section, we propose a novel model for General Non-I.I.D. image classiﬁcation.
In the literature of Non-I.I.D. image classiﬁcation, most previous methods are pro-
posed for Targeted Non-I.I.D. image classiﬁcation. Domain adaptation and covariate
shift methods [16, 17, 18, 19] are proposed to match distributions, transform feature
14


## Page 15


Conv Extractor
Classifier
0.9…0.1…0.11
0.1…0.99…0.9
…
…
…
Batch
Samples
Features
Global Balancer
Dog
Cat
…
0.3
0.1
…
Weights
Decisions
Figure 9: Info ﬂow in CNBB. The gray and purple lines refer to the forward and backward processes
respectively.
space or learn invariant features between training data and testing data. These methods
can achieve good performances but are less feasible in practice due to the fact that they
need prior knowledge on testing data distribution. On the other hand, several methods
are proposed to liberalize the need of testing data information in Targeted Non-I.I.D.
image classiﬁcation. For example, domain generalization methods [20, 21] only use train-
ing data to learn a domain-agnostic model or invariant representations. However, these
methods about transfer learning [22] require the training data has multiple domains and
we know which domain each sample belongs to. Moreover, the performance of these
methods is highly dependent on the diversity of training data.
Recently, growing attention has been paid on General Non-I.I.D. learning. In the lit-
erature of causality [23], an ideal model to resolve selection bias is to make policy based
on causal variables, which keep stable across diﬀerent domains[24]. Popular methods
based one observational data to estimate the causal eﬀect of a treatment on the outcome
include propensity score matching [25, 26], markov blankets [27, 28] and confounder bal-
ancing [29, 30] and etc [31]. Lately [32] leverage causality for predictive modeling. By
performing global confounder balancing, one can accurately identify the stable features
that are insensitive to unknown distribution shift for prediction. [33] proposes a causally
regularized logistic regression called CRLR7for General Non-I.I.D. image classiﬁcation
7CRLR: Causally Regularize Logistic Regression
15


## Page 16


and achieve good performance in a relatively small dataset. However, due to the lack of
well-structured and reasonable-scaled dataset, these methods cannot leverage the power-
ful representation learning techniques (e.g. ConvNets) and therefore are not favourable
for large-scale image classiﬁcation tasks.
In this work, with the help of NICO, we extend the notion of global confounder
balancing into ConvNet, and propose a novel model called CNBB, ConvNet with Batch
Balancing.
Algorithm 1 ConvNets with Batch Balancing (CNBB)
Input: Train dataset Dtrain = {(xi, yi)|i = 1, ..., n}
Output: Non-linear parameters θ and ϕ
Initialize θ(0), ϕ(0) and t1 ←0
repeat
Sample batch of images {(x1, y1), ..., (xm, ym)}
Extract image features {gϕ(t1)(xi), ..., gϕ(t1)(xm)}
Calculate indicator matrix I of features
Initialize sample weights W (0) and t2 ←0
repeat
Optimize W (t2+1) to minimize Lossb in Eq.2
t2 ←t2 + 1
until Lossb converges or t2 reaches maximum
Predict {fθ(t1)(gϕ(t1)(x1)), .., fθ(t1)(gϕ(t1)(xm))}
Optimize θ(t1+1) and ϕ(t1+1) to minimize Lossp in Eq.3
t1 ←t1 + 1
until Lossp converges or t1 reaches maximum
return: θ and ϕ
4.1. ConvNet with Batch Balancing
The key idea in CRLR is global confounder balancing, which successively sets each
feature as treatment variable, and learns an optimal set of sample weights that can
16


## Page 17


balance the distribution of treated and control groups for any treatment variable. There-
after, the correlations among features will be disentangled and their true eﬀects on class
label can be more accurately estimated.
To introduce the notion of global confounder balancing into deep learning, we mainly
face two challenges:
• Confounder balancing methods assume features to be in binary form, while we
generally have continuous features in ConvNet.
• For global confounder balancing, we need to learn a new set of sample weights for
all the training samples in one iteration.
This is not feasible for ConvNet where we cannot feed all the training data into the
model at once.
To overcome these challenges, we introduce a quantization loss for feature binarization
and propose a batch confounder balancing method. Speciﬁcally, given a batch of training
images, we deﬁne the quantization loss as follows:
Lossq = −
n
X
i=1
∥gϕ(xi))∥2
2 ,
(1)
where n refers to the batch size, xi refers to the ith sample in a batch and gϕ refers to
the feature extractor (here we use the last FC layers in ConvNet as gϕ). By minimizing
Lossq, we can amplify the feature activated by tanh function from (−1, 1) to approach
to {−1, 1}.
Following the CRLR, we successively regard each feature as treatment, calculate the
balancing loss of confounders and sum it over all the features globally. Formally, we solve
the batch confounder balancing problem as follows:
min
W Lossb =
p
X
j=1





gϕ(X)T
−j · (W ⊙Ij)
W T · Ij
−gϕ(X)T
−j · (W ⊙(1 −Ij))
W T · (1 −Ij)





2
2
+ α ∥W∥2
2
s.t.
n
X
i=1
Wi = 1, W ≥0,
(2)
where W represents sample weights, Ij means the jth column of I, and Iij refers to the
treatment status of sample i when setting feature j as treatment variable, and ∥W∥2
2 can
17


## Page 18


reduce the variance of weights to prevent the weights from overﬁtting outlier samples.
Diﬀerent from CRLR, we deﬁne the confounder balancing loss w.r.t. a batch of training
samples instead of the whole training samples. Moreover, the sample weights and model
parameters are jointly optimized through a supervised way in CRLR, while in CNBB we
ﬁrst ﬁx the model parameters (a.k.a. representation) and learn the sample weights W
through an unsupervised way.
As far as we have learnt an optimal set of sample weights for a batch which can
balance the confounder distribution, then we combine the weighted softmax loss and
quantization loss and propose our CNBB model:
min
θ,ϕ Lossp =
n
X
i=1
wi ln(fθ(gϕ(xi)) · yi) + λLossq,
(3)
where fθ refers to softmax layer and λ is a trade-oﬀparameter between classiﬁcation
and quantization.
Algorithm 1 gives the complete steps of the batch balancing method and Figure 9
illustrates it intuitively.
4.2. Experiments on NICO
In this section, we evaluate the proposed ConvNet with batch balancing (CNBB) in
the task of General Non-I.I.D. image classiﬁcation based on NICO.
4.2.1. Experimental Settings
For fair comparison, we choose a typical structure of CNN and CNN with batch nor-
malization [34] (CNN+BN) as baselines. The latter is a popular method in deep learning
to improve the generalization ability of CNN by normalizing the scale of activations. All
the methods are implemented using PyTorch [35] and optimized by stochastic gradient
descent.
We design four experiments according to the supported Non-I.I.D. settings of NICO
in Sec 3.3:
• Minimum bias (Exp 1): In this experiment, we randomly sample 8000 images for
training and 2000 images for testing.
18


## Page 19


• Proportional bias (Exp 2): In this experiment, we ﬁx the dominant ratio of training
data to 5:1, and vary the dominant ratio of testing data from 1:5 to 4:1.
• Compositional bias (Exp 3): In this experiment, we vary the number of contexts
observed in training data from 3 to 7 while let all the contexts appear in testing
data.
• Combined Proportional & Compositional bias (Exp 4): To simulate a more harsh
condition, for each class, we randomly select 7 contexts for training and the other
3 contexts for testing. Furthermore, we vary the dominant ratio of training data
from 1:1 to 5:1 while ﬁx the dominant ratio of testing data to 1:1.
Exp2
1 : 5
1 : 1
2 : 1
3 : 1
4 : 1
CNN
37.17
37.80
41.46
42.50
43.23
CNN+BN
38.70
39.60
41.64
42.00
43.85
CNBB
39.06
39.60
42.12
43.33
44.15
Table 2: Performances of diﬀerent methods on test accuracy (%) for proportional bias in Animal super-
class.
Exp3
3
4
5
6
7
CNN
40.61
42.32
43.34
44.03
44.03
CNN+BN
41.98
38.85
43.12
44.71
44.31
CNBB
41.41
43.34
44.54
45.96
45.16
Table 3: Performances of diﬀerent methods on test accuracy (%) for composional bias in V ehicle super-
class.
4.2.2. Experimental Results
We calculate the average testing accuracy of all the methods for each experiment.
First of all, CNBB is comparable with CNN in the minimum bias setting, with a slightly
higher accuracy (49.94% v.s. 49.60%), and CNN+BN performs worst (46.48%). For
19


## Page 20


Exp4
1 : 1
2 : 1
3 : 1
4 : 1
5 : 1
CNN
37.07
35.20
34.53
34.13
33.73
CNN+BN
33.87
32.93
31.20
30.93
30.67
CNBB
38.98
36.89
35.87
35.33
35.02
Table 4: Performances of diﬀerent methods of test accuracy (%) for combined proportional & composi-
tional bias in V ehicle superclass.
the other three experiments with explicit distribution shift between training data and
testing data, CNBB outperforms the other baselines at almost every setting, as shown
in Table 2,3,4, indicating its eﬀectiveness in Non-I.I.D. image classiﬁcation. Note that
the performance of CNN with batch normalization is relatively unstable compared to
original CNN across diﬀerent experiments. It is mainly because, in the General Non-
I.I.D. setting, the agnostic distribution shift between training and testing data cannot
be eﬀectively normalized only based on the training data.
Comparatively, the batch
balancing module enable CNBB to identify more stable features and therefore resist the
negative eﬀect brought by distribution shift to some extent.
Experiment
Improvement
NI
Exp1
0.33%
3.81 - 3.93
Exp2
1.22%
4.17 - 4.53
Exp3
1.22%
4.13 - 4.34
Exp4
1.49%
4.44 - 4.90
Table 5: The range of NI with respect to the average improvement of performance to CNN.
We further summarize the improvement of CNBB over the best baseline in diﬀerent
experiments. From Table 5, we can clearly ﬁnd that with the discrepancy between the
training and testing data getting larger (indicated by higher NI), CNBB gains larger
improvement over baselines, which demonstrate the advantage of our method in more
challenging Non-I.I.D. settings.
20


## Page 21


Figure 10: Parameter sensitivity analysis of Exp4. Testing accuracy with respect to the trade-oﬀpa-
rameter λ in Eq.2 while we set dominant ratio of training data to 3:1. The blue area represents the
improvement of CNBB against CNN.
Finally, we analyze the hyperparameter α. α eventually plays the role of trading-oﬀ
the valid sample size and degree of batch balancing. In theory, when α is extremely
large, the weights of samples tend to be uniform, resulting in a largest valid sample size.
When α is zero, the algorithm tend to converge to a situation where sample weights
concentrate on only a few images, but lead to an optimal batch balancing. Both of valid
sample size and degree of batch balancing are critical for the performances of Non-I.I.D.
image classiﬁcation. As in Eq 2, we tune the hyperparameter α with 9 values (1e3 to 5e5)
in all the experiments. Taking the case where training dominant ratio is 3:1 in Table 4
as an example, a convex hull is clear in Figure 10. Along with the increasing α, the gain
of CNBB will tend to vanish eventually. The results fully demonstrate the eﬀectiveness
of batch balancing module.
5. Conclusion and Future Works
In this paper, we introduce a new dataset NICO for promoting the research on Non-
I.I.D. image classiﬁcation. To the best of our knowledge, NICO is the ﬁrst well-structured
Non-I.I.D. image dataset with reasonable scale to support the training of ConvNets. By
incorporating the idea of context, NICO can provide various Non-I.I.D. settings and
create diﬀerent levels of Non-IIDness consciously.
We also propose a simple baseline
21


## Page 22


model with ConvNet structure for General Non-I.I.D. image classiﬁcation problem, where
testing data bear agnostic distribution shift from training data. Empirical results clearly
demonstrate the capability of NICO on training the ConvNets and the superiority of the
proposed model in various Non-I.I.D. settings.
Our future works will focus on the followings.
Firstly, both quality and quantity
of NICO continue to be improved. Orthogonal contexts, denoised images and proper
area ratio of objects will be explored to make NICO more controllable to tune bias and
response to the Non-I.I.D uniquely. And we will expand the scale of dataset from all the
levels for adequate demands. Secondly, more settings about diﬀerent forms of Non-I.I.D
are expected to be exploited. So other visual concepts may be added to NICO if needed
and the ways of using NICO to meet new settings will be given in detail. Thirdly, more
eﬀective models will be designed for addressing problems in diﬀerent settings of Non-I.I.D
image classiﬁcation.
22


## Page 23


6. Appendix
Table 1: Basic structure of ConvNet used in this paper.
Structure of ConvNet
Layer
Filter
height & width
input
3
(64 * 64)
conv
64
(64 * 64)
relu
maxpool
64
(32 * 32)
conv
128
(32 * 32)
relu
maxpool
128
(16 * 16)
conv
256
(16 * 16)
relu
maxpool
256
(8 * 8 )
conv
512
(8 * 8 )
relu
maxpool
512
(4 * 4 )
conv
1024
(4 * 4 )
relu
maxpool
1024
(2 * 2 )
fc
512
1
relu
fc
50
1
tanh
fc
10/9
1
softmax
23


## Page 24


Table 2: Data size of each context for every class in Animal superclass.
Animal
Bear
black
brown
eating grass
in forest
in water
lying
on ground
on snow
on tree
white
245
220
133
243
169
217
97
111
70
104
Bird
eating
flying
in cage
in hand
in water
on branch
on grass
on ground
on shoulder
standing
187
203
90
94
81
239
242
276
77
101
Cat
at home
eating
in cage
in river
in street
in water
on grass
on snow
on tree
walking
274
270
109
141
177
50
140
137
50
131
Cow
aside people
at home
eating
in forest
in river
lying
on grass
on snow
spotter
standing
56
77
147
131
139
162
147
135
75
123
Dog
at home
eating
in cage
in street
in water
lying
on beach
on grass
on snow
running
92
264
122
87
139
143
280
158
238
101
Elephant
eating
in circus
in forest
in river
in street
in zoo
lying
on grass
on snow
standing
122
114
160
178
90
162
69
103
69
111
Horse
aside people
at home
in forest
in river
in street
lying
on beach
on grass
on snow
running
124
86
146
73
77
141
165
165
138
143
Monkey
climbing
eating
in cage
in forest
in water
on beach
on grass
on snow
sitting
walking
88
168
77
140
118
50
106
102
168
100
Rat
at home
eating
in cage
in forest
in hole
in water
lying
on grass
on snow
running
126
169
57
85
50
85
50
124
50
50
Sheep
aside people
at sunset
eating
in forest
in water
lying
on grass
on road
on snow
walking
50
66
116
95
71
109
132
111
87
81
24


## Page 25


Table 3: Data size of each context for every class in V ehicle superclass.
V ehicle
Airplane
around cloud
aside mountain
at airport
at night
in city
in sunrise
on beach
on grass
taking off
with pilot
87
76
153
76
55
70
104
53
128
128
Bicycle
in garage
in street
in sunset
on beach
on grass
on road
on snow
shared
velodrome
with people
143
113
134
131
219
125
163
225
220
166
Boat
at wharf
cross bridge
in city
in river
in sunset
on beach
sailboat
with people
wooden
yacht
219
190
194
265
196
168
252
143
248
281
Bus
aside traffic light
aside tree
at station
at yard
double decker
in city
on bridge
on snow
with people
35
165
95
74
221
199
45
124
51
Car
at park
in city
in sunset
on beach
on booth
on bridge
on road
on snow
on track
with people
80
149
89
102
112
36
146
184
89
39
Helicopter
aside mountain
at heliport
in city
in forest
in sunset
on beach
on grass
on sea
on snow
with people
165
185
69
124
160
107
147
156
180
58
Motorcycle
in city
in garage
in street
in sunset
on beach
on grass
on road
on snow
on track
with people
194
148
173
157
122
99
162
134
185
168
Train
aside mountain
at station
cross tunnel
in forest
in sunset
on beach
on bridge
on snow
subway
63
158
36
100
94
46
54
129
70
Truck
aside mountain
in city
in forest
in race
in sunset
on beach
on bridge
on grass
on road
on snow
62
77
91
134
155
97
44
78
145
117
25


## Page 26


References
References
[1] A. Krizhevsky, I. Sutskever, G. E. Hinton, Imagenet classiﬁcation with deep convolutional neural
networks, in: F. Pereira, C. J. C. Burges, L. Bottou, K. Q. Weinberger (Eds.), Advances in Neural
Information Processing Systems 25, 2012, pp. 1097–1105.
[2] K. Simonyan, A. Zisserman, Very deep convolutional networks for large-scale image recognition,
Computer Science (2014).
[3] K. He, X. Zhang, S. Ren, J. Sun, Deep residual learning for image recognition, in: Proceedings of
the IEEE conference on computer vision and pattern recognition, 2016, pp. 770–778.
[4] S. Ren, K. He, R. Girshick, J. Sun, Faster r-cnn: towards real-time object detection with region
proposal networks (2015).
[5] J. Long, E. Shelhamer, T. Darrell, Fully convolutional networks for semantic segmentation, in:
Proceedings of the IEEE conference on computer vision and pattern recognition, 2015, pp. 3431–
3440.
[6] Y. Ma, Y. He, F. Ding, S. Hu, J. Li, X. Liu, Progressive generative hashing for image retrieval.,
2018.
[7] M. Everingham, S. M. A. Eslami, L. V. Gool, C. K. I. Williams, J. Winn, A. Zisserman, The pascal
visual object classes challenge: A retrospective, International Journal of Computer Vision 111 (1)
(2015) 98–136.
[8] T. Y. Lin, M. Maire, S. Belongie, J. Hays, P. Perona, D. Ramanan, P. Dollr, C. L. Zitnick, Microsoft
coco: Common objects in context (2014).
[9] J. Deng, W. Dong, R. Socher, L. J. Li, K. Li, F. F. Li, Imagenet: A large-scale hierarchical image
database, in: IEEE Conference on Computer Vision & Pattern Recognition, 2009.
[10] A. Torralba, A. A. Efros, Unbiased look at dataset bias (2011).
[11] S. Tutorials, Pearson correlation, Retrieved on February 4 (2014).
[12] A. Krizhevsky, G. Hinton, et al., Learning multiple layers of features from tiny images, Tech. rep.,
Citeseer (2009).
[13] A. Kuznetsova, H. Rom, N. Alldrin, J. Uijlings, I. Krasin, J. Pont-Tuset, S. Kamali, S. Popov,
M. Malloci, T. a. Duerig, The open images dataset v4: Uniﬁed image classiﬁcation, object detection,
and visual relationship detection at scale (2018).
[14] B. Thomee, D. A. Shamma, G. Friedland, B. Elizalde, K. Ni, D. Poland, D. Borth, L.-J. Li,
Yfcc100m: The new data in multimedia research, arXiv preprint arXiv:1503.01817 (2015).
[15] A. Clauset, C. R. Shalizi, M. E. Newman, Power-law distributions in empirical data, SIAM review
51 (4) (2009) 661–703.
[16] M. Long, H. Zhu, J. Wang, M. I. Jordan, Deep transfer learning with joint adaptation networks,
26


## Page 27


in: Proceedings of the 34th International Conference on Machine Learning-Volume 70, JMLR. org,
2017, pp. 2208–2217.
[17] M. Long, Y. Cao, J. Wang, M. I. Jordan, Learning transferable features with deep adaptation
networks, arXiv preprint arXiv:1502.02791 (2015).
[18] E. Sangineto, G. Zen, E. Ricci, N. Sebe, We are not all equal: Personalizing models for facial expres-
sion analysis with transductive parameter transfer, in: Proceedings of the 22nd ACM international
conference on Multimedia, ACM, 2014, pp. 357–366.
[19] E. Tzeng, J. Hoﬀman, T. Darrell, K. Saenko, Simultaneous deep transfer across domains and tasks,
in: Proceedings of the IEEE International Conference on Computer Vision, 2015, pp. 4068–4076.
[20] M. Ghifary, W. Bastiaan Kleijn, M. Zhang, D. Balduzzi, Domain generalization for object recogni-
tion with multi-task autoencoders, in: Proceedings of the IEEE international conference on com-
puter vision, 2015, pp. 2551–2559.
[21] K. Muandet, D. Balduzzi, B. Sch¨olkopf, Domain generalization via invariant feature representation,
in: International Conference on Machine Learning, 2013, pp. 10–18.
[22] S. J. Pan, Q. Yang, A survey on transfer learning, IEEE Transactions on knowledge and data
engineering 22 (10) (2010) 1345–1359.
[23] J. Pearl, Causality: models, reasoning and inference, Vol. 29, Springer.
[24] P. R. Rosenbaum, D. B. Rubin, The central role of the propensity score in observational studies for
causal eﬀects, Biometrika 70 (1) (1983) 41–55.
[25] H. Bang, J. M. Robins, Doubly robust estimation in missing data and causal inference models,
Biometrics 61 (4) (2005) 962–973.
[26] P. C. Austin, An introduction to propensity score methods for reducing the eﬀects of confounding
in observational studies, Multivariate behavioral research 46 (3) (2011) 399–424.
[27] I. Tsamardinos, C. F. Aliferis, A. Statnikov, Time and sample eﬃcient discovery of markov blankets
and direct causal relations, in: Proceedings of the ninth ACM SIGKDD international conference
on Knowledge discovery and data mining, ACM, 2003, pp. 673–678.
[28] J.-P. Pellet, A. Elisseeﬀ, Using markov blankets for causal structure learning, Journal of Machine
Learning Research 9 (Jul) (2008) 1295–1342.
[29] J. Hainmueller, Entropy balancing for causal eﬀects: A multivariate reweighting method to produce
balanced samples in observational studies, Political Analysis 20 (1) (2012) 25–46.
[30] K. Kuang, P. Cui, B. Li, M. Jiang, S. Yang, Estimating treatment eﬀect in the wild via diﬀerentiated
confounder balancing, in: Proceedings of the 23rd ACM SIGKDD International Conference on
Knowledge Discovery and Data Mining, ACM, 2017, pp. 265–274.
[31] F. Li, K. L. Morgan, A. M. Zaslavsky, Balancing covariates via propensity score weighting, Journal
of the American Statistical Association 113 (521) (2018) 390–400.
[32] K. Kuang, P. Cui, S. Athey, R. Xiong, B. Li, Stable prediction across unknown environments, in:
Proceedings of the 24th ACM SIGKDD International Conference on Knowledge Discovery & Data
27


## Page 28


Mining, ACM, 2018, pp. 1617–1626.
[33] Z. Shen, P. Cui, K. Kuang, B. Li, P. Chen, Causally regularized learning with agnostic data selection
bias, in: 2018 ACM Multimedia Conference on Multimedia Conference, ACM, 2018, pp. 411–419.
[34] S. Ioﬀe, C. Szegedy, Batch normalization: Accelerating deep network training by reducing internal
covariate shift, arXiv preprint arXiv:1502.03167 (2015).
[35] A. Paszke, S. Gross, S. Chintala, G. Chanan, E. Yang, Z. DeVito, Z. Lin, A. Desmaison, L. Antiga,
A. Lerer, Automatic diﬀerentiation in pytorch (2017).
28

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
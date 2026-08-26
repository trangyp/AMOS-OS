---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1904.01219v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1904.01219v2_Deep_Learning_for_Face_Recognition__Pride_or_Prejudiced_

> Source: 1904.01219v2_Deep_Learning_for_Face_Recognition__Pride_or_Prejudiced_.pdf

> Pages: 10

---


## Page 1


Deep Learning for Face Recognition: Pride or Prejudiced?
Shruti Nagpal, Maneet Singh, Richa Singh, Mayank Vatsa
IIIT-Delhi, India
{shrutin, maneets, rsingh, mayank}@iiitd.ac.in
Abstract
Do very high accuracies of deep networks suggest pride
of effective AI or are deep networks prejudiced? Do they
suffer from in-group biases (own-race-bias and own-age-
bias), and mimic the human behaviour? Is in-group speciﬁc
information being encoded sub-consciously by the deep net-
works?
This research attempts to answer these questions and
presents an in-depth analysis of ‘bias’ in deep learning
based face recognition systems. This is the ﬁrst work which
decodes if and where bias is encoded for face recognition.
Taking cues from cognitive studies, we inspect if deep net-
works are also affected by social in- and out-group effect.
Networks are analyzed for own-race and own-age bias, both
of which have been well established in human beings. The
sub-conscious behavior of face recognition models is exam-
ined to understand if they encode race or age speciﬁc fea-
tures for face recognition. Analysis is performed based on
36 experiments conducted on multiple datasets. Four deep
learning networks either trained from scratch or pre-trained
on over 10M images are used. Variations across class ac-
tivation maps and feature visualizations provide novel in-
sights into the functioning of deep learning systems, sug-
gesting behavior similar to humans. It is our belief that a
better understanding of state-of-the-art deep learning net-
works would enable researchers to address the given chal-
lenge of bias in AI, and develop fairer systems.
1. Introduction
Deep learning based systems show extremely high ac-
curacy in many computer vision application such as object
detection and recognition, and image synthesis [20, 22, 29].
In particular, signiﬁcantly better results have been shown in
many face analytic tasks including face detection, age and
gender prediction, and face recognition leading many re-
searchers to claim super human performance in face recog-
nition. However, recently reported bias in face analytics
shows the issues with the current state of the art deep learn-
ing face analytic systems [28].
(a) (L-R): Recent incident of bias in AI (image taken from the internet);
own-race bias already established in humans
Model 
Trained 
on Race B
Input Images
Average Final 
Feature Maps Input Images
Average Final
Feature Maps
Model 
Trained 
on Race A
Own-race Bias in Deep Learning Networks
(b) Pride or Prejudiced? Own-race bias observed in deep learning models
Figure 1: Bias observed in (a) AI systems and humans, and
(b) deep learning networks obtained via this research. Cur-
rent state-of-the-art deep learning models appear to mimic
the human in-group biases by focusing on different facial
regions when trained on speciﬁc sub-groups for face recog-
nition. Best viewed in color.
In July 2018, Amazon’s facial recognition tool, ‘Rekog-
nition’, falsely identiﬁed 28 members of the US Congress as
criminals [1]. The US Congress contains around 20% mem-
bers of color, out of which 40% were mis-classiﬁed. The
study, conducted by the American Civil Liberties Union
(ACLU), is one of the recent incidents shedding light on
the emerging biased behavior of Artiﬁcial Intelligence sys-
tems, and the need to develop fairer AI. Earlier examples
include the ProPublica study of algorithms being used by
US courts and parole boards to predict future behaviour of
criminals [3]. It was observed that the system was biased
against black defendants, and gave them a higher score as
compared to their white counterparts. Another popular in-
stance which shook the Machine Learning community was
1
arXiv:1904.01219v2  [cs.CV]  19 Jun 2019


## Page 2


of the Google Photos application’s mis-classiﬁcation of a
black couple as gorilla (Figure 1(a)) [2]. Multiple repeated
incidents suggesting existence of bias demand dedicated re-
search in order to ensure the development of AI systems
for the better, and not for the worse. This research focuses
on understanding the hidden biases of face recognition sys-
tems, speciﬁcally, current state-of-the-art deep learning net-
works. The existence of bias with respect to the race and
age of an individual has been analyzed in face recognition
models, by answering if and where the bias is encoded.
Bias is often deﬁned as an inclination or prejudice for
or against one person or group, especially in a way con-
sidered to be unfair. While bias in AI is a relatively new
ﬁeld, humans have shown to possess biases across differ-
ent parameters since the very beginning. Neuro-cognitive
researchers have long established the presence of in-group
biases1 in humans, wherein we tend to recognize individ-
uals of our race or age easily, as compared to individu-
als of an out-group [27]. One such instance dates back to
1971, when ﬁve black men were acquitted for the murder
of Khomas Revels [25]. Despite the lack of any forensic
evidence, ﬁve eyewitnesses testiﬁed and identiﬁed them as
offenders. However, during the third trial, private investi-
gators located the actual culprits, who were later convicted.
Interestingly, all the ﬁve men initially acquitted were black
and all the ﬁve eyewitnesses were white. Social Psychol-
ogist, Dr. William Haythorn identiﬁed the reason for mis-
identiﬁcations to be the cross-racial identiﬁcations, because
of which people of the other race look alike, resulting in bi-
ased outcomes (Figure 1(a)). Several studies later, this phe-
nomenon was termed as the own race bias, or other race or
cross-race effect, where people of the other race look alike.
We believe that the human trait of making biased deci-
sions has also made its way into the recent AI systems for
computer vision (Figure 1(b)). Since most of these systems
today are based on deep learning, they provide limited in-
sights into the decision making process. Thus, understand-
ing the models and their corresponding biases is of utmost
importance, in order to prevent the inclusion of biases that
existed in the past into our future.
1.1. Literature Review: Bias in Facial Analysis
A majority of research has focused on understanding
bias in models developed on textual data [7], with limited
attention to computer vision tasks [6]. However, recent re-
search has focused on understanding the presence of bias in
commercial-off-the-shelf systems and deep learning mod-
els primarily for gender and ethnicity classiﬁcation in face
images [8, 11, 32] and not face recognition. Buolamwini
and Gebru [8] categorized face images into four categories
based on their skin color: darker males, darker females,
1In-group bias refers to the tendency to have an afﬁnity towards mem-
bers belonging to the same group as the individual.
lighter males, and lighter females.
The performance of
three commercial gender classiﬁcation systems was ana-
lyzed with respect to the proposed categorization. It was
observed that, out of the four categories, dark-skinned fe-
males were the most mis-classiﬁed group, thereby creating
a need for fairer unbiased facial analysis algorithms. It is
important to note that the authors analyzed gender classiﬁ-
cation using three commercial systems, without exploring
the performance of deep learning models.
The establishment of bias for tasks such as gender clas-
siﬁcation, led to the requirement of fairer algorithms, capa-
ble of performing a particular task, unbiased of other re-
lated covariates. Das et al. [11] proposed a Multi-Task
Convolutional Neural Network (MTCNN) for joint gender,
race, and age classiﬁcation of face images. The proposed
model demonstrates improved performance for the given
tasks across multiple subgroups of gender, age, and ethnic-
ity. Simultaneously, Alvi et al. [4] proposed a joint learning
and unlearning (JLU) technique for eliminating bias from
CNN networks. Experiments are performed for multiple
tasks of age, gender, race, and pose classiﬁcation of face
images, independently, while the other covariates are used
for inducing bias. Ryu et al. [32] proposed using transfer
learning to develop attribute prediction models inclusive of
different race and gender subgroups via a novel Inclusive-
FaceNet model. It demonstrates improved performance of
attribute classiﬁcation across different subgroups.
1.2. Research Contributions
This research extends beyond the existing literature by
analyzing deep learning based face recognition models for
bias existence. This is the ﬁrst of its kind research which at-
tempts to understand what deep networks are encoding, and
whether they learn features similar to the human brain, with
respect to different co-variates of face recognition. Four
deep learning networks (LightCNN-9 [36], LightCNN-29
[36], ResNet50 [17], and SENet50 [19]), either trained from
scratch or pre-trained on large scale datasets containing
about 10M images have been evaluated to establish our ﬁnd-
ings. The key ﬁndings of this research are:
• Result-1: Upon simulating the real world scenario of
limited exposure to other races/age-groups by training
on data belonging to a speciﬁc class, we observe that
deep learning networks mimic the human tendency of
in-group bias across race and age.
• Result-2: Similar to the human behavior of face recog-
nition, race-speciﬁc regions of interest are encoded in
networks trained on a particular race.
• Result-3: Extending upon the existing cognitive liter-
ature, different regions of interest are also observed for
varying age-groups, suggesting own-age bias in deep
learning networks.


## Page 3


• Result-4: Networks pre-trained on large-scale data
with varying distribution (eg.
VGGFace2 [9] and
MSCeleb-1M [16] datasets), demonstrate high gener-
alization abilities, however, bias across age persists to
be a major challenge.
• Result-5: Fine-tuning a pre-trained network results in
change of region of interest, which might reduce its
generalization abilities.
It is our belief that insights into the functioning of deep net-
works can help develop fairer AI systems, capable of unbi-
ased decisions. Since deep learning models appear to mimic
the human brain, ﬁndings of this research can also enable
better utilization of pre-trained systems by applying suitable
cognitive techniques (designed for humans) for de-biasing.
The remainder of this paper is organized as follows: the fol-
lowing section provides the experiments and protocols used
for both the case studies of race and age. Sections 3 and
4 present the ﬁndings, along with the key takeaways and
insights, followed by the conclusions of this research.
2. Experiments and Protocols
In this research, deep-learning based face recognition
networks are analyzed to answer two key questions:
• Does deep learning encode race-speciﬁc information?
• Does deep learning encode age-speciﬁc information?
We analyze the behavior of deep learning networks with
respect to well established cognitive studies on humans,
and identify the regions used by deep learning models to
learn features for face recognition. We further delve deeper
to observe if these regions are consistent across different
races and age-groups, and how deep learning models be-
have when trained from scratch on selective data i.e. data
highly biased towards speciﬁc subgroups.
Network Details: Four deep learning based face recogni-
tion networks are analyzed to answer the two key ques-
tions pertaining to the effect and existence of bias due to
race and age: (i) LightCNN-9 [36], (ii) Light CNN-29 [36],
(iii) ResNet50 [17], and (iv) SENet50 [19]. LightCNN-9 is
trained from scratch, while the remaining three networks
are pre-trained on large-scale face datasets.
LightCNN-
29 is pre-trained on the MS-Celeb-1M dataset2 [16], which
contains 10M images corresponding to nearly 10k identities
in the training set. ResNet50 and SENet50 are pre-trained
on the VGG-Face2 [9] and MS-Celeb-1M datasets for face
recognition3. VGG-Face2 dataset contains 3.31M images
pertaining to 9,131 identities. Therefore, the two models
are trained on over 13M images, the largest corpus used for
training a single face recognition model.
Datasets Used for Case-study-1 (Effect of Race): The be-
havior of deep learning networks is analyzed with respect
2https://github.com/AlfredXiangWu/LightCNN
3https://github.com/cydonia999/VGGFace2-pytorch
Figure 2: Samples from the datasets used for understand-
ing racial bias in face recognition: (i) CMU Multi-PIE
(Race-A), (ii) MORPH (Race-B), and (iii) RFW: Race-A
and Race-B.
to two races: Race-A (Caucasoid) and Race-B (Congoid)4
Three datasets are used for performing the said analysis:
(i) CMU Multi-PIE [15]: Over 44K images of 336 subjects
images are selected which correspond to frontal face images
having illumination and expression variations.
(ii) Craniofacial Longitudinal Morphological (MORPH)
Album-2 [30]: Over 52k frontal face images pertaining to
10,409 subjects are used.
(iii) Racial Faces in the Wild (RFW) [34] is an uncon-
strained dataset of African (Race-B), Caucasian (Race-A),
Asian, and Indian face images, collected from the Internet.
Its test set contains labeled images across races, with lim-
ited labeled Caucasian faces in the training set. For analysis,
the test set containing 10,196 Race-A and 10,145 Race-B
face images of 2,959 and 2,995 subjects, respectively, has
been used.
The CMU Multi-PIE dataset is used for analyzing the
networks for Race-A, while the MORPH dataset is used for
Race-B. Both the datasets are captured in constrained set-
tings, and for both, 70% of the subjects are used to create the
training (or ﬁne-tuning) partition, while the remaining 30%
subjects form the test set. This ensures disjoint training and
testing partitions, in terms of images and subjects. Due to
the availability of limited labeled training data in the RFW
datset, only the test data is used to evaluate our hypothe-
sis. Therefore, unless explicitly speciﬁed, analysis is drawn
using the CMU Multi-PIE and MORPH datasets. Figure 2
presents sample images from the three datasets demonstrat-
ing facial images across the two races.
Datasets Used for Case-study-2 (Effect of Age): Deep
learning networks are analyzed for face recognition with
respect to three age groups: (i) (0-14) years, (ii) (15-32)
years, and (iii) (33+) years.
To the best of our knowl-
edge, there does not exist any large scale dataset contain-
ing the identity and age information for such a large range.
IMDB-Wiki [31] is a large dataset containing face images
with age and identity information, however, it has been ob-
served that the dataset contains erroneous age information.
Therefore, in this study we combined face images from
4For this study, we use the existing classiﬁcation of races, namely Cau-
casoid and Congoid to understand machine learning based face recognition
systems. The races are referred to as Race-A and Race-B in the manuscript.


## Page 4


(0-14) Years
(15-32) Years
(33+) Years
(a) Adience Dataset
(0-14) Years
(15-32) Years
(33+) Years
(b) Cross-Age Celebrity Dataset
Figure 3: Sample images of the two datasets used for ana-
lyzing the effect of varying age on deep learning networks.
two datasets: Adience dataset [12] and Cross-Age Celebrity
Dataset (CACD) [10].
Both the datasets contain images
collected from the Internet, having pose, illumination, and
background variations. Figure 3 presents sample images
from both the datasets, displaying variations in age. The
CACD dataset contains over 1,60,000 face images belong-
ing to the age range of 14-62 years. In our experiments, the
CACD dataset has been used for training (or ﬁne-tuning)
the deep learning networks. However, since it does not con-
tain subjects below the age of 14 years, 70% of the Adience
dataset has also been used for training. Thus, the training or
ﬁne-tuning set is a combination of images from CACD and
Adience datasets. The remaining 30% of data pertaining to
the Adience dataset is used for testing. Mutual exclusion
(for both images and subjects) has been ensured between
the training and testing partitions.
Details Regarding Experiments and Analysis: Analysis
is drawn from 36 experiments (Table 1) conducted across
different case-studies, networks, and training data. At the
time of training from scratch, models are trained on data
pertaining to a single sub-group only (race or age), to ob-
serve the regions being learned for face recognition; and
on equal number of samples belonging to different sub-
groups. Cross sub-group experiments have also been per-
formed on the trained models to understand what regions
are being used in each case to perform classiﬁcation. For
example, LightCNN-9 trained on Race-A subjects is used
for evaluation on Race-B subjects, to study the difference in
processing (if any). Three pre-trained networks ResNet50,
SENet50, and LightCNN-29 have also been evaluated for
performance and visualizations. The effect of ﬁne-tuning
has also been studied to understand how the regions of in-
terest evolve for different sub-groups with pre-trained net-
works. Fine-tuning is performed on the entire network for
the given train set. Feature-level analysis is performed with
respect to the learned feature maps, where the ﬁnal convolu-
tion layer maps are interpolated and super-imposed on the
input image, to obtain the region of interest for the given
input image and network. Class Activation Maps (CAMs)
[37] are used to obtain the most discriminative regions of
Table 1: List of 36 experiments performed to understand
face recognition in deep learning models w.r.t. race and age
bias. Results have been shown using three datasets for race:
CMU Multi-PIE, MORPH, and RFW; and two datasets for
age: Adience and CACD. LCNN: LightCNN; MSC: MS-
Celeb-1M, VF2: VGG-Face2; RA: Race-A, RB: Race-B;
A1: (0-14) years, A2: (15-32) years, A3: (33+) years.
Exp.#
Network
Pre-train
Train
Fine-tune
Test
Effect of Race
1 / 2
LCNN-9
-
RA
-
RA / RB
3 / 4
RB
-
RA / RB
5 /6
RA, RB
-
RA / RB
7 / 8
LCNN-29
MSC (10M)
-
-
RA / RB
9-12
RA / RB
RA / RB
13 / 14
ResNet50
MSC (10M),
-
-
RA / RB
15-18
-
RA / RB
RA / RB
19 / 20
SENet50
VF2 (3M)
-
-
RA / RB
21-24
-
RA / RB
RA / RB
Effect of Age
25
LCNN-9
-
A1
-
A1
26
A2
-
A2
27
A3
-
A3
28-30
LCNN-29
MSC (10M)
-
-
A1/A2/A3
31-33
ResNet50
MSC (10M),
-
-
A1/A2/A3
34-36
SENet50
VF2 (3M)
-
-
A1/A2/A3
face images, focused upon by the CNNs. Results are also
reported in terms of the veriﬁcation accuracy (Genuine Ac-
ceptance Rate) obtained at 1% False Acceptance Rate. In
order to ensure consistency across analysis and fair com-
parisons, ﬁxed protocols have been used for all experiments.
Model ﬁles will be released for reproducibility of ﬁndings.
3. Does Deep Learning Encode Race-speciﬁc
Information?
The own-race bias in humans has been well established,
where we are able to recognize people of our own race more
easily as compared to individuals of other race [14, 26].
Also referred to as the other-race bias or cross-race effect, it
has extensively been studied in humans in the form of cog-
nitive, behavioural, and neuro-imaging studies. Depending
on the racial identity of the individual and the person to be
identiﬁed, different facial regions have shown more contri-
bution during the decision making process. In this study,
we understand the behaviour of deep learning models to ob-
serve if they also focus on speciﬁc facial regions based on
the race, as observed in humans.
3.1. Are Deep Learning Networks Prejudiced?
Experiments 1-6 (Table 1) are performed to analyze the
presence of prejudice in deep learning networks via class
activation maps and feature visualizations.
LightCNN-9
models are trained from scratch on data belonging to dif-
ferent races. The aim is to understand if faces of different


## Page 5


Figure 4: Veriﬁcation accuracy (%) at 1% False Acceptance
Rate of LightCNN-9 architecture. Models trained on im-
ages pertaining to a particular race demonstrate poor per-
formance on face images of the other race.
Figure 5: Visualization of salient regions obtained from exp.
1-5 (Table 1), where networks are trained from scratch on
(a) only Race-A, (b) only Race-B, and (c) both Race-A and
Race-B face images. Best viewed in color.
races are learned in a similar manner, or does the model
utilize race-speciﬁc features for identifying individuals.
Figure 4 presents the GAR values obtained at 1%FAR
with LightCNN-9 models, for the two races. The model
trained on face images of Race-A only reports an accuracy
of 79.2% on the testing set of same race (Race-A). On the
other hand, the model trained on Race-B faces, tested on
Race-A individuals, reports a GAR of 28.9%. This sug-
gests the presence of race-speciﬁc prejudice being encoded
in the network due to the variations in the input data. Simi-
lar trends are observed when testing race-speciﬁc models on
data belonging to Race-B individuals only. The LightCNN-
9 network trained on faces of Race-B subjects only reports a
GAR of 84.3% on samples of Race-B (same race), while the
network trained on Race-A faces achieves a GAR of 34.3%
(different race).
We also evaluated the models trained on a speciﬁc race
on the RFW test set, and observed a similar trend, thus
demonstrating that the drop in accuracy is caused due to the
other-race bias and not dataset bias. When testing on the
RFW Race-A test set, the network trained on Race-B faces
in comparison to the network trained on Race-A, demon-
strates a decrease of around 22% of its performance. It is
our belief that network prejudice occurs due to differences
in the learned networks for varying input data.
Feature visualizations allow us to compare models be-
yond the veriﬁcation accuracy, and analyze the regions be-
ing learned by the network to extract features with the high-
est discriminative information across races. Figure 5(a-b)
presents the salient regions used for feature extraction by
the learned networks.
These are obtained by interpolat-
ing the ﬁnal convolution layer ﬁlter responses and super-
imposing on the input image.
It can be observed that
both models focus on different regions for feature extrac-
tion. Figure 5(c) shows the visualizations of salient regions
learned by a LCNN-9 model trained on equal Race-A and
Race-B faces. The network learns a union of salient re-
gions obtained for each race independently. While for the
Race-B, salient regions correspond to the lips and above the
eyes, Race-A appear to be distinguished on a more holistic
view, with more focus on face boundary. The differences
obtained in the feature maps, along with the accuracy vari-
ations strengthen the hypothesis that faces belonging to dif-
ferent race are encoded differently in a classiﬁcation model,
thereby suggesting presence of bias.
3.2. Do Deep Networks Mimic Humans?
Cognitive studies in humans have analyzed how Race-A
and Race-B individuals perform face recognition [13, 18].
Across different studies, it has been observed that Race-B
participants focus more on certain facial features such as
mouth, lips, and nose while identifying other individuals of
the same race [13]. On the other hand, Race-A subjects used
traits such as the iris color, face shape, hair color and texture
for describing and identifying other people of the same race
[13, 33]. Such studies suggest a higher level of difference
between the regions useful for distinguishing between in-
dividuals of different race. For example, information such
as the eye color or hairstyle might not be useful for iden-
tifying a Race-B individual, whereas it could be of utmost
importance for identifying an individual of Race-A.
Intrigued by the ﬁndings of human behavior, in this
study, deep learning based face recognition systems are an-
alyzed to investigate if they follow a similar pattern. In or-
der to understand the behavior of deep learning networks,
in terms of the useful regions of interest, class activation
maps of the LightCNN-9 models trained on data pertain-
ing to Race-A and Race-B for face recognition are analyzed
(Experiment 1-6, Table 1). Networks trained on a particu-
lar race simulate the functioning of the human brain which
has been in contact with individuals of a speciﬁc race only,
thereby enabling us to understand own-race effect in deep
networks. Figures 6 and 7 present sample mean class acti-
vation maps. Each map corresponds to the mean activation
associated with a particular class. It is interesting to note
that the activation maps vary signiﬁcantly between races,
however, demonstrate a similar behavior within a particular


## Page 6


Figure 6: Sample average class activation maps obtained
from the LightCNN-9 model trained on Race-A subjects.
The model focuses heavily on the eye region for recogni-
tion. Best viewed in color.
Figure 7: Sample average class activation maps obtained
from the LightCNN-9 model on trained Race-B subjects.
The model focuses heavily on the nose region (below the
eyes), and the chin region. Best viewed in color.
race. The network trained on subjects belonging to Race-A
only, identiﬁes primarily on the basis of the eye region (Fig-
ure 6). These results are in conjunction with the cognitive
studies reported in literature, where researchers have identi-
ﬁed the eye color as one of the most identiﬁable traits used
by humans as well [13]. This suggests that the behavior of
deep learning networks and the human brain is alike. Apart
from the eyes, we also observe regions around the face be-
ing highlighted, which could mean face shape or hair type,
both of which have been identiﬁed earlier from behavioural
studies [13]. Similarly, Figure 7 presents sample mean class
activation maps from the LightCNN-9 network trained on
the Race-B dataset. Regions of the lip, nose, and cheek-
bones appear to contribute more towards face recognition,
as compared to other facial regions. Similar results have
also been reported in cognitive studies, wherein Race-B in-
dividuals utilized the eyes and lips for describing and rec-
ognizing other Race-B subjects [13]. The regions of interest
used by models trained on speciﬁc races demonstrate the
presence of different discriminative regions, suggesting that
networks sub-consciously encode race-speciﬁc information,
thereby resulting in an own-race bias.
3.3. More the Merrier: Does Large-scale Data Help
in Mitigating Own-race Bias?
The presence of own-race bias in individuals is often at-
tributed to limited exposure to other race people [23]. In lit-
erature, studies have shown reduced effect of other-race bias
upon training subjects to recognize face images of a differ-
ent race. Since deep learning models rely heavily on the
training samples, networks trained on large datasets may ex-
hibit a similar behavior. In order to understand whether pre-
trained networks suffer from the challenge of bias, deep net-
works trained on large-scale datasets are analyzed (Table 1:
Exp. 7-24). The performance of three pre-trained networks
- ResNet50, SENet50, and LightCNN-29 is studied. Fea-
ture maps and class activation maps are also computed to
better understand their behaviour. Upon testing on the rela-
tively constrained data belonging to Race-A, ResNet50 ob-
tains an accuracy of 98.7%, while for Race-B, the network
attains a classiﬁcation accuracy of 96.3%. Similar results
are obtained with the SENet50 network: 98.8% and 96.5%,
respectively. The performance of LightCNN-29 network
further depicts that the generalization of a network highly
depends upon the training data used. It achieves an accu-
racy of 96.47% and 78.12% on Race-A and Race-B data,
respectively. The results depict that pre-trained models are
biased towards Race-A and achieve better performance on
Race-A faces as compared to samples belonging to Race-B.
Similar trend in results is observed on the unconstrained
in-the-wild RFW dataset. The pre-trained ResNet-50 net-
work achieves 77.3% on Race-B and 90.6% on Race-A,
while the pre-trained SENet-50 model attains an accuracy
of 76.4% on Race-B versus 90.4% on Race-A. Similar to
the performance on the constrained data, the performance
of the LCNN-29 model reduces to 58.2% and 82.1% for
Race-B and Race-A, respectively. The consistent reduced
performance on Race-B suggests that the generalization ca-
pability of a network depends heavily upon the amount and
variability of the training data. Figure 8 presents the fea-
ture visualizations (region of interest) for the pre-trained
networks. Both ResNet50 and SENet50 models learn fea-
ture maps which cover an entire circular region of the face,
thereby using almost the entire face for recognition, which
might result in higher generalizability.
Fine-tuning has emerged as a common practice for en-
hancing a network’s performance for a chosen task and
dataset. Experiments 9-12, 15-18, and 21-24 of Table 1
are performed to understand the behaviour of deep net-
works after ﬁne-tuning. It is interesting to note the tran-
sition in region of interest from pre-trained networks to
ﬁne-tuned networks (Figure 8). Initially, for both SENet50
and ResNet50, feature maps of both the races (Race-A and
Race-B) are similar, and focus on a circular region covering
almost the entire face. After ﬁne-tuning, the updated feature
maps appear similar to the ones discussed earlier (Figure 5).


## Page 7


(a) Original Images
(b) SENet Features
(I) Feature Visualizations
(II) t-SNE plots
(III) Bar graph
(b) Race-A
(i) Pre-trained 
SENet50
(ii) Pre-trained 
ResNet50
(iii) Pre-trained 
LightCNN-29
(iv) Trained 
LightCNN-9
(v) Fine-tuned 
SENet50
(vi) Fine-tuned 
ResNet50
(i) Pre-trained 
SENet50
(ii) Pre-trained 
ResNet50 
(iii) Pre-trained 
LightCNN-29
(iv) Trained 
LightCNN-9
(v) Fine-tuned 
SENet50
(vi) Fine-tuned 
ResNet50
(a) Race-B
Figure 8: (I) Visualization of salient regions obtained from pre-trained, ﬁne-tuned, and trained from scratch networks. Differ-
ences in the region of focus are observed across models. (II) t-SNE visualizations of raw pixels and features extracted from
SENet50. (III) Veriﬁcation accuracy (%) at 1%FAR for three pre-trained networks on the three age based sub-groups.
The feature maps obtained after ﬁne-tuning with images of
Race-B are similar to the network trained only on Race-
B, demonstrating a shift to only the nose region and face
center. In case of Race-A individuals, the networks start
focusing on the eye-region only. This demonstrates the im-
portance of ﬁne-tuning for speciﬁc problems. However, it
also establishes that ﬁne-tuning should only be performed
when the test set is highly speciﬁc as it might reduce the
generalization abilities of the network.
4. Does Deep Learning Encode Age-speciﬁc In-
formation?
Similar to the own-race bias, recently researchers have
established the presence of own-age bias in human beings
[5]. Own-age bias refers to the phenomenon of an individ-
ual being able to identify other people of a similar/same age
with a greater accuracy (and more easily) as compared to
individuals of other ages. Research has focused on under-
standing the own-age bias on three age-groups: children,
adults, and older people. While initial studies appeared con-
ﬂicted in terms of an own-age bias in older people, how-
ever, across different studies, researchers have established
its presence across different age groups [35]. This is the
ﬁrst research which analyzes and studies the bias effect
due to the factor of age in deep learning models. Previ-
ously, Kemelmacher-Shlizerman et. al [21] presented the
MegaFace dataset and studied the impact of age on face
recognition with respect to the data used for training a net-
work. However, no analysis of deep models has been per-
formed for the same. This section focuses on analyzing the
own-age bias in deep learning models, speciﬁcally in terms
of questioning its existence and investigating if distinguish-
ing features vary across age.
4.1. How Well Do Deep Networks Recognize Chil-
dren, Youngsters, and Adults?
In order to analyze the behavior of deep learning net-
works in terms of own-age bias, a similar set of experi-
ments are performed as the previous case study. Models
(both trained from scratch (Table 1 1: exp.
25-27) and
pre-trained (Table 1: expt. 28-26)) are analyzed on face
images of varying age-groups. The pre-trained networks
of ResNet50, SENet50 and LightCNN-29 are evaluated for
the three different age-groups: (i) 0-14 years, (ii) 15-32
years, (iii) 33+ years. The networks which are pre-trained
on a large set of data capturing multiple variations, that is,
ResNet50 and SENet50 obtained an accuracy of 77.9% and
75.5%, respectively for the oldest age group of (33+) years.
Both the networks achieve a slightly higher performance
on the age-group of (15-32) years, by reporting around 81-
83% (Figure 8(III)), and less than 45% for the youngest age
group. On the other hand, LightCNN-29 reports a veriﬁca-
tion accuracy of 30.5%, 54.45%, and 66.03% for the three
age groups, in ascending order of age. The consistent lower
face veriﬁcation performance across different networks sug-
gests the presence of an own-age bias in these networks.
Figure 8(II) presents the t-SNE [24] plots for the images of
the test set (across all three age-groups), and the features
extracted from SENet50. It is interesting to note that fea-
tures of the youngest age-group (orange colour) appear to
form a separate cluster, thereby suggesting that the network
is able to distinguish between adults and children, how-
ever, the lower recognition performance suggest lower dis-
crimination between the extracted features. The relatively
improved performance of SENet50 and ResNet50 models
(pre-trained on MS-Celeb-1M and VGGFace2) suggest that
similar to the contact hypothesis given in cognitive stud-


## Page 8


(0-14) Years
(15-32) Years
(33+) Years
Figure 9: Class activation maps of sample images obtained from the trained LightCNN-9 networks. Best viewed in color.
ies, where more exposure to a particular out-group results
in increased recognition capabilities, more contact (train-
ing) with a sub-group of individuals might result in an im-
proved classiﬁcation performance for that sub-group. Thus,
reinstating the importance of training data for modeling the
different co-variates of face recognition.
4.2. What Does the Model See Based on the Age?
Cognitive research has established the presence of own-
age bias, however, limited research has focused on analyz-
ing the speciﬁc regions of focus or discriminative facial fea-
tures across different age groups. While there exist studies
which analyze the gaze pattern or scan pattern of individu-
als belonging to different age-groups, they do not contribute
much to the current study, since they do not speciﬁcally an-
alyze the discriminative regions of interest. In this study,
we analyze the behavior of face recognition models to in-
vestigate different regions of interest.
Three LightCNN-9 models are trained, one for each age
group, and corresponding class activation maps are pre-
sented in Figure 9. The class activation maps demonstrate
the discriminative regions of focus used by the model for
classifying the input images. An interesting trend of activa-
tion is observed across the images of different age groups.
Face images of kids (ﬁrst four columns) appear to use more
soft biometric information such as hair and face shape for
classiﬁcation, while models trained on individuals of (15-
32) years focus more on the lip, lower face, and forehead
regions. Models trained on the third category, (33+) years
rely heavily on the eye information for classiﬁcation, along
with other facial features. The activation suggests the pres-
ence of different discriminative regions across age-groups,
thereby suggesting the presence of an own-age bias, espe-
cially for young children below 15 years. The presence of
different discriminative regions across varying age-groups
provides new insights into the face recognition process,
which opens the avenues for novel research directions in
both deep learning and cognitive studies.
5. Conclusion
Multiple instances have unfolded the hidden biases of
AI systems, creating a need for developing fairer systems.
In this direction, this research analyzes deep learning net-
Race-B
All Seem Similar!
John
Lisa Mark
Own-race Bias in Humans
R1: Deep learning models mimic humans and exhibit in-group bias!
0-14 years
15-32 years
At least 
24% gap
Mean Images
LightCNN-9
Race-A
R2: Racial Bias
R3, R4: Age Bias
Pre-trained Fine-tuned 
Race-A on SENet50
R5: Generalizability
Figure 10: Deep learning for face recognition- Prejudiced!
works for the existence of bias in automated face recog-
nition systems. This is the ﬁrst work which attempts to
answer if and where bias is encoded in face recognition
systems, with respect to two case studies of race and age.
Analysis across multiple deep learning networks suggests
the presence of own-race and own-age bias in face recog-
nition models. Similar to human behavior, deep learning
networks demonstrate strong tendency of focusing on se-
lected facial regions for a particular race, with variations
across different race. To the best of our knowledge, this is
the ﬁrst study which suggests that the biased behavior of
deep learning networks is similar to that observed in hu-
mans, therefore presenting opportunities of applying well
established human cognitive results for bias elimination in
deep learning networks. Our analysis also demonstrates the
beneﬁt of using large-scale data for training; however, does
not recommend it as a complete solution for bias elimina-
tion. On the other hand, caution must be ensured while cu-
rating the training data for deep learning models, in order to
incorporate maximum variability possible. Similar behavior
is observed for the cross-age study, where face recognition
networks appear to sub-consciously encode the age infor-
mation pertaining to the training samples resulting in vary-
ing regions of interest across groups, and presence of own-
age bias. Lower recognition performance of state-of-the-art
face recognition systems on child face images further reaf-
ﬁrms the biased nature of such systems with respect to age
as well. We believe that the insights provided in this pa-
per can help facilitate research across multiple disciplines,


## Page 9


and enable development of novel techniques for de-biasing
existing face recognition systems.
References
[1] Facial recognition, and bias. https://tinyurl.com/
y7rat8vb. 1
[2] Google photos labels dark skinned people as gorillas.
https://tinyurl.com/y7c7dxso. 2
[3] Propublica study of algorithms.
https://tinyurl.
com/gvtccpq. 1
[4] M. Alvi, A. Zisserman, and C. Nellker. Turning a blind eye:
Explicit removal of biases and variation from deep neural
network embeddings. In European Conference of Computer
Vision Workshops, 2018. 2
[5] J. S. Anastasi and M. G. Rhodes. An own-age bias in face
recognition for children and older adults. Psychonomic bul-
letin & review, 12(6):1043–1047, 2005. 7
[6] L. Anne Hendricks, K. Burns, K. Saenko, T. Darrell, and
A. Rohrbach. Women also snowboard: Overcoming bias in
captioning models. In European Conference on Computer
Vision, pages 771–787, 2018. 2
[7] T. Bolukbasi, K.-W. Chang, J. Zou, V. Saligrama, and
A. Kalai.
Man is to computer programmer as woman is
to homemaker? debiasing word embeddings.
In Interna-
tional Conference on Neural Information Processing Sys-
tems, pages 4356–4364, 2016. 2
[8] J. Buolamwini and T. Gebru. Gender shades: Intersectional
accuracy disparities in commercial gender classiﬁcation. In
Conference on Fairness, Accountability and Transparency,
volume 81 of Proceedings of Machine Learning Research,
pages 77–91, 2018. 2
[9] Q. Cao, L. Shen, W. Xie, O. M. Parkhi, and A. Zisserman.
Vggface2: A dataset for recognising faces across pose and
age. In IEEE International Conference on Automatic Face &
Gesture Recognition, pages 67–74, 2018. 3
[10] B. Chen, C. Chen, and W. H. Hsu.
Face recognition
and retrieval using cross-age reference coding with cross-
age celebrity dataset.
IEEE Transactions on Multimedia,
17(6):804–815, 2015. 4
[11] A. Das, A. Dantcheva, and F. Bremond. Mitigating bias in
gender, age and ethnicity classiﬁcation: a multi-task convo-
lution neural network approach. In European Conference of
Computer Vision Workshops, 2018. 2
[12] E. Eidinger, R. Enbar, and T. Hassner. Age and gender es-
timation of unﬁltered faces. IEEE Transactions on Informa-
tion Forensics and Security, 9(12):2170–2179, 2014. 4
[13] H. D. Ellis, J. B. Deregowski, and J. W. Shepherd. Descrip-
tions of white and black faces by white and black subjects.
International Journal of Psychology, 10(2):119–123, 1975.
5, 6
[14] S. Fu, H. He, and Z.-G. Hou. Learning race from face: A
survey. IEEE Transactions on Pattern Analysis and Machine
Intelligence, 36(12):2483–2509, 2014. 4
[15] R. Gross, I. Matthews, J. Cohn, T. Kanade, and S. Baker.
Multi-pie.
Image and Vision Computing, 28(5):807–813,
2010. 3
[16] Y. Guo, L. Zhang, Y. Hu, X. He, and J. Gao. MS-Celeb-1M:
A dataset and benchmark for large-scale face recognition. In
European Conference on Computer Vision, pages 87–102,
2016. 3
[17] K. He, X. Zhang, S. Ren, and J. Sun. Deep residual learning
for image recognition.
In IEEE Conference on Computer
Vision and Pattern Recognition, pages 770–778, 2016. 2, 3
[18] P. J. Hills and M. B. Lewis. Reducing the own-race bias in
face recognition by shifting attention. The Quarterly Journal
of Experimental Psychology, 59(6):996–1002, 2006. 5
[19] J. Hu, L. Shen, and G. Sun.
Squeeze-and-excitation net-
works. In IEEE Conference on Computer Vision and Pattern
Recognition, 2018. 2, 3
[20] P. Hu and D. Ramanan. Finding tiny faces. In IEEE Con-
ference on Computer Vision and Pattern Recognition, 2017.
1
[21] I. Kemelmacher-Shlizerman, S. M. Seitz, D. Miller, and
E. Brossard. The megaface benchmark: 1 million faces for
recognition at scale. In IEEE Conference on Computer Vi-
sion and Pattern Recognition, pages 4873–4882, 2016. 7
[22] E. Learned-Miller, G. B. Huang, A. RoyChowdhury, H. Li,
and G. Hua. Labeled faces in the wild: A survey. In Advances
in face detection and facial image analysis, pages 189–248.
2016. 1
[23] S. Lebrecht, L. J. Pierce, M. J. Tarr, and J. W. Tanaka. Per-
ceptual other-race training reduces implicit racial bias. PloS
one, 4(1):e4215, 2009. 6
[24] L. v. d. Maaten and G. Hinton. Visualizing data using t-sne.
Journal of machine learning research, 9:2579–2605, 2008.
7
[25] C. Meissner and J. Brigham. Thirty years of investigating the
own-race bias in memory for faces: A meta-analytic review.
Psychology, Public Policy, and Law, 7:3–35, 2001. 2
[26] C. A. Meissner and J. C. Brigham. Thirty years of investigat-
ing the own-race bias in memory for faces: A meta-analytic
review. Psychology, Public Policy, and Law, 7(1), 2001. 4
[27] M. M. Nicholls, O. Churches, and T. Loetscher. Perception
of an ambiguous ﬁgure is affected by own-age social biases.
Scientiﬁc Reports, 8, 12 2018. 2
[28] I. D. Raji and J. Buolamwini. Actionable auditing: Inves-
tigating the impact of publicly naming biased performance
results of commercial ai products. In AAAI/ACM Conf. on AI
Ethics and Society, 2019. 1
[29] R. Ranjan, V. M. Patel, and R. Chellappa. Hyperface: A deep
multi-task learning framework for face detection, landmark
localization, pose estimation, and gender recognition. IEEE
Transactions on Pattern Analysis and Machine Intelligence,
41(1):121–135, 2019. 1
[30] A. W. Rawls and K. Ricanek. MORPH: Development and
optimization of a longitudinal age progression database. In
J. Fierrez, J. Ortega-Garcia, A. Esposito, A. Drygajlo, and
M. Faundez-Zanuy, editors, Biometric ID Management and
Multimodal Communication, pages 17–24, 2009. 3
[31] R. Rothe, R. Timofte, and L. V. Gool. DEX: Deep expec-
tation of apparent age from a single image. In IEEE Inter-
national Conference on Computer Vision Workshops, 2015.
3


## Page 10


[32] H. J. Ryu, H. Adam, and M. Mitchell. Inclusivefacenet: Im-
proving face attribute detection with race and gender diver-
sity. In Workshop on Fairness, Accountability, and Trans-
parency in Machine Learning, 2018. 2
[33] P. Sinha, B. Balas, Y. Ostrovsky, and R. Russell. Face recog-
nition by humans: Nineteen results all computer vision re-
searchers should know about.
Proceedings of the IEEE,
94(11):1948–1962, 2006. 5
[34] M. Wang, W. Deng, J. Hu, J. Peng, X. Tao, and Y. Huang.
Racial faces in-the-wild: Reducing racial bias by deep unsu-
pervised domain adaptation. CoRR, abs/1812.00194, 2018.
3
[35] H. Wiese, J. Komes, and S. R. Schweinberger. Ageing faces
in ageing minds: a review on the own-age bias in face recog-
nition. Visual Cognition, 21(9-10):1337–1363, 2013. 7
[36] X. Wu, R. He, Z. Sun, and T. Tan. A light CNN for deep face
representation with noisy labels. IEEE Transactions on In-
formation Forensics and Security, 13(11):2884–2896, 2018.
2, 3
[37] B. Zhou, A. Khosla, A. Lapedriza, A. Oliva, and A. Tor-
ralba. Learning deep features for discriminative localization.
In IEEE Conference on Computer Vision and Pattern Recog-
nition, 2016. 4

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1904_01219v2_deep_learning_for_face_recognition_pride_or_prejudiced
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1904_01219V2_DEEP_LEARNING_FOR_FACE_RECOGNITION_PRIDE_OR_PREJUDICED.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

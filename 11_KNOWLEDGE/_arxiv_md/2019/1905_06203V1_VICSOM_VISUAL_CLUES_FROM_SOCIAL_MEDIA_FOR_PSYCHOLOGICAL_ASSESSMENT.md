---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1905.06203v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1905.06203v1_VICSOM__VIsual_Clues_from_SOcial_Media_for_psychological_assessment

> Source: 1905.06203v1_VICSOM__VIsual_Clues_from_SOcial_Media_for_psychological_assessment.pdf

> Pages: 12

---


## Page 1


International Journal of Computer Vision manuscript No.
(will be inserted by the editor)
VICSOM: VIsual Clues from SOcial Media for psychological assessment
Mohammad Mahdi Dehshibi · Gerard Pons · Bita Baiani ·
David Masip
Received: date / Accepted: date
Abstract Sharing multimodal information (typically images, videos or text) in Social Network Sites
(SNS) occupies a relevant part of our time. The particular way how users expose themselves in SNS can
provide useful information to infer human behaviors. This paper proposes to use multimodal data gath-
ered from Instagram accounts to predict the perceived prototypical needs described in Glasser’s choice
theory. The contribution is two-fold: (i) we provide a large multimodal database from Instagram public
proﬁles (more than 30,000 images and text captions) annotated by expert Psychologists on each perceived
behavior according to Glasser’s theory, and (ii) we propose to automate the recognition of the (uncon-
sciously) perceived needs by the users. Particularly, we propose a baseline using three diﬀerent feature
sets: visual descriptors based on pixel images (SURF and Visual Bag of Words), a high-level descrip-
tor based on the automated scene description using Convolutional Neural Networks, and a text-based
descriptor (Word2vec) obtained from processing the captions provided by the users. Finally, we pro-
pose a multimodal fusion of these descriptors obtaining promising results in the multi-label classiﬁcation
problem.
Keywords Image database · Social networks · Multimodality · Glasser’s choice theory · Computer
vision · Neural networks
1 Introduction
The complexity of the human mind can manifest through a dynamic and organized set of characteristics
which uniquely inﬂuences the environment, cognition, emotions, motivations, and behaviors in various
situations. These characteristics, which can disclose how people are individually diﬀerent, are known as
personality [14]. Not only psychologists but also sociologists and humanities researchers are also interested
in knowing more about human personality and have been in collaboration with computer and data
scientists to ﬁnd computational models of personality trait inferences at diﬀerent levels ([37, 40]). On the
other hand, analyzing the complex and subconscious behavior of humans has an impact on health, security,
human-computer/machine/robot interaction, and even entertainment. The emergence of social network
sites (SNS) provides a massive amount of visual and multimodal information and helps researchers to
recognize clues associated with the subconscious behavior and situations of their users.
Social network sites enable individuals to construct and display their identities in favor of interacting
with other members [4]. Therefore, many individuals have increasingly invested in developing an idealized
online self that they can present to the world [16]. Instagram is an image-based SNS and a simple way to
capture and share life’s moments, and follow friends and family to see their interests. Instagram allows
users to upload photos and videos to the service, write captions, add tags, and location information. The
Mohammad Mahdi Dehshibi, Gerard Pons, and David Masip
Department of Computer Science, Universitat Oberta de Catalunya, Barcelona, Spain
E-mail: {mdehshibi,gponro,dmasipr}@uoc.edu
Bita Baiani
Department of Psychology, Islamic Azad University, Science and Research Branch, Tehran, Iran
arXiv:1905.06203v1  [cs.CV]  15 May 2019


## Page 2


2
Dehshibi et al.
service also supports messaging features, the ability to include multiple images or videos in a single post,
as well as “Stories”, i.e. temporary posts that disappear after 24 hours.
This pool of data, as a mirror of society on a smaller scale, can provide valuable clues about users’
physical/mental health conditions, as well as personality features which have recently been used in ana-
lytical screening. Analytical screening methods have successfully identiﬁed markers in social media data,
and this trend has been followed up in two directions including (i) physical ailments, and (ii) mental
health issues, e.g., addiction [33], depression [7, 23, 38], Post-Traumatic Stress Disorder (PTSD) [17],
suicidal ideation [8], sense of love [36], happiness [13], and enhance life satisfaction [34]. However, studies
in health screening using SNS data are not mature enough and need to be developed in order to be
eﬀectively used in health care systems. Supporting pieces of evidence for this claim are (i) lack of publicly
available data sets, (ii) lack of ground-truth, provided by psychologists, and (iii) focusing on a speciﬁc
physical or mental health problem which decreases the generalizability.
This research aims at studying how humans intrinsically contribute towards behavioral motivation
(i.e., human needs) by sharing their interest on Instagram. The analysis of human needs has always been
important for many psychologists who have put forward many eﬀorts to characterize these needs and have
proposed a structure for the treatment of their subjects according to this classiﬁcation. Two well-deﬁned
psychological theories known as the Maslow’s hierarchy of needs [28] and Glasser’s choice theory [15]
make the foundation of our study. Based on the Maslow’s hierarchy of needs, human motivations generally
move through “physiological,” “safety,” “belonging and love,” “esteem,” “cognition,” “aesthetic,” “self-
actualization,” and “transcendence” patterns, respectively. Indeed, the individual must be satisﬁed by
each level to ﬁnd enough motivation for thinking about at the next level and completing their hierarchy.
(a)
(b)
Fig. 1: Maslow’s hierarchy of needs represented as (a) pyramid [29], and (b) a dynamic hierarchy with
overlaps of diﬀerent needs at the same time [41].
This psychological theory is an infrastructure for understanding the correlation between drive and
motivation in human behavior [9, 29] because Maslow stated that “Instead of stating that the individual
focuses on a certain need at any given time, it must be stated that a certain need ‘dominates’ the human
organism.” This well-deﬁned hierarchy which is used in sociology research, management training, and
secondary and higher psychology instruction, states that these levels overlap with each other. Fig. 1
shows the original hierarchy and its alternative illustration as a dynamic and overlapping hierarchy of
needs.
Although the human complex brain can think about diﬀerent phenomena in parallel, this theory
states that if a human is struggling to meet their physiological needs, he might not be able to pursue
safety, belongingness, esteem, and self-actualization. These concepts, associated with each level of needs,
are abstract and need to be clariﬁed by in-detail words and synonyms. For instance, physiological needs
include homeostasis, food, water, sleep, shelter, and sex [27, 28, 29]. Safety and Security needs include
personal security, emotional security, ﬁnancial security, and health and well-being [18, 19, 20]. Social Be-


## Page 3


VICSOM: VIsual Clues from SOcial Media for psychological assessment
3
longing needs include friendships, intimacy, family [42]. Self-actualization can include parenting, utilizing
abilities, utilizing talents, pursuing a goal, seeking happiness [30].
When it comes to analyzing posts from SNS, for some cases providing descriptions about higher levels
in the pyramid is not possible. Consequently, to ﬁnd some visual/textual clues for a better representation
of the perception of human needs within shared media on Instagram, we restrict this research on Glasser’s
choice theory [15]. Based on this, human behavior is driven by ﬁve categories of needs, namely: ‘Survival’
(e.g. food, clothing, shelter, personal safety, or sex), ‘Belonging’ (e.g. connecting, love), ‘Power’ (e.g.
signiﬁcance, competence), ‘Freedom’ (i.e. autonomy), ‘Fun’ (i.e. learning).
In this research, we introduce a new database from Instagram user proﬁles enriched with ground-truth
provided by an expert psychologist (following Glasser’s choice theory). We propose an automated method
for predicting the perception of human needs from Instagram proﬁles based on three informational cues:
(i) visual information extracted from state-of-the-art computer vision image descriptors, (ii) high level de-
scriptors from the scene contents (both in terms of scene categorization and object recognition), extracted
using two Convolutional Neural Networks, and (iii) the processed textual information accompanying each
image (captions). We also propose a multimodal fusion of the three signals, obtaining promising results in
which is, to the best of our knowledge, the ﬁrst contribution towards the automated analysis of perceived
human needs using SNS data. Related work is surveyed in Section 2. Section 3 dedicates to the description
of the database, its organization, associated meta-data, and distribution conditions. Automatic recogniz-
ing the perceived subject’s needs along with the analytical evaluations of the proposed methodology form
the content of Sections 4 and 5, respectively. Finally, concluding remarks are drawn in Section 6.
2 Related work
Sharing multimodal data (pictures, videos, texts) has become an essential part of the online social ex-
perience. This data can provide valuable clues about the physical, mental health conditions, personality
features, characters, and needs of its users even if users are not yet aware that their health has changed.
From another perspective, analyzing human needs can reveal individual motives for their behaviors.
Diﬀerent researchers have used SNS data to plan the path of disease occurrences [5, 39]. Predictive
screening methods have also successfully found signs of mental health issues in social media data [7, 38, 43].
Reece et al. [38] used a computational model to predict depression signs in users’ Twitter data and
showed that screening the posts on Twitter can eﬀectively identify this condition earlier and more accu-
rately than the health professionals. Results of this study showed that depression indicators are identiﬁable
within six months before the trauma appears in an individual. This progress, compared to the average
19-month delay between trauma event and diagnosis experienced by the individuals, can provide a frame-
work for an accessible, accurate, and inexpensive depression screening, where in-person assessments are
diﬃcult or costly.
Kim and Kim [24] utilized computer vision approaches to ﬁnd whether there is a positive relation be-
tween shared images characteristics and personality traits. The data consists of 25,394 photos shared over
179 Instagram proﬁles where the owners were university students. They measured user’s characteristics
with an online survey. Content categorization was done by counting the number of faces, analyzing the
emotions on the faces, and the pixel derived features using Microsoft Azure Computer Vision API [31].
Finally, they concluded that Instagram users’ extraversion, openness, agreeableness, and conscientious-
ness are associated with the features of photos they have shared. Although this study put a step forward
by analyzing the content, they stated that the photo, itself, is enough for concluding and they did not
consider texts which usually appear in proﬁle biography, captions, and comments. They believed that
expressing oneself by photo is simple because the individual does not need to care much about word
selection and grammatical errors. However, observing the contradiction between the image content and
the written caption for it helps to discover some hidden parts of a person’s mental state. Indeed, photos
context, caption of posts, textual reply to comments, proﬁle image, and proﬁle biography are all clues
that can provide an insight view to the mental state of a user.
Kircaburun and Griﬃths [25] examined the relationships between personality, self-liking, daily Inter-
net use, and Instagram addiction. They asked 752 university students to complete a self-report survey,
including the Instagram Addiction Scale and the Self-Liking Scale. They reported that agreeableness,
conscientiousness, and self-liking are negatively associated with Instagram addiction while daily Internet
usage is positively associated with Instagram addiction. However, the majority of shared contents on


## Page 4


4
Dehshibi et al.
Instagram is not only about selﬁe and self-liking and users also tend to share personal interests through
image, videos, and text over a photo, as well.
Pampouchidou et al. [35] surveyed methods published from 2005 to 2017 about automatic depres-
sion assessment based on visual cues. They addressed several research questions, including the number
of modalities employed, facial signs, experimental protocols for dataset acquisition, feature descriptors,
decision methods, and scores. They concluded that results are consistent with the social withdrawal,
emotion-context insensitivity, reduced reactivity hypotheses of depression, and the importance of dy-
namic features/multimodal approaches through the quantitative analysis. They also mentioned that the
multitude of reported approaches on automatic depression assessment is not mature enough because clin-
ical research questions such as the capacity to distinguish between diﬀerent depression sub-types or the
inﬂuence of ethnicity and culture on the progress of mental health were not addressed systematically.
Finally, they argued that visual cues need to be supplemented by information from other modalities to
achieve clinically useful results.
Most of the studies covering social media analysis have targeted some speciﬁc personality disor-
der/traits. The foundation was created based on answers to an online questionnaire to reveal if the SNS
user has a particular personality disorder. Therefore, apart from the truth level of the answers, unavail-
ability of this information causes the contextual photo analysis to become meaningless. In this study, we
resolve the mentioned shortcomings by introducing the VICSOM database which contains multimodal
data of 86 Instagram proﬁles from both Persian and Spanish users with 30,080 photos. Moreover, we
investigated the relationship between activity in Instagram and the perceived needs the individual seeks
according to the Glasser’s choice theory.
3 VICSOM Database
Instagram is a data pool in which we can perceive the user’s needs, feelings, and thoughts by analyzing
shared contents. Moreover, Instagram users can enrich this expression by adding textual and hashtag-
based captions to images. In collecting the VICSOM, we targeted public accounts at the time of scraping
from two regions, i.e., Iran from the Middle East and Spain from Europe. Recruitment and data collection
procedures were identical for both regions. We made a one-time collection of participants’ Instagram
proﬁle. In total, we collected 30,080 images from 86 Instagram users for the analysis of human needs.
Commercial and celebrity proﬁles were ignored in the proﬁle selection. We used the Instagram developer’s
Application Programming Interface (API) to harvest data from public pages.
The expert psychologist has then visited the pages and provided a description of the need-level of
users based on Glasser’s theory. Both Persian and English versions of these descriptions are available in
the database. We also provided the labels for each proﬁle according to the ﬁve categories in the Glasser’s
choice theory, i.e. each proﬁle was labeled with l ∈P(L) −∅, where P(L) is the power set of L and
L = {survival, belonging, power, freedom, fun}.
The expert psychologist also provided a description to label 32 proﬁles according to Maslow’s hierarchy
of need. This data is not used in the experiments, but it is available in the database.
3.1 Data Statistics and subject demographics
We collected data from 86 Instagram users, totaling 30,080 images. The mean number of posts per user
was 286.47 (SD = 198.18). This distribution was skewed by a smaller number of frequent posters, as
evidenced by a median value of just 286.47 posts per user. The subjects were coming from 2 diﬀerent
cultural backgrounds, i.e., Iranian and Spanish. 54 of the subjects are males, 32 are females, resulting in
a gender ratio (male/female) of 1.68. See Table 1 for summary of statistics.
Table 1: Summary statistics and Demographics for VICSOM
Female
Male
Age range
Iran
12
30
15-50
Spain
20
24
15-50


## Page 5


VICSOM: VIsual Clues from SOcial Media for psychological assessment
5
VICSOM 1 has two sets as follows:
– Set 1 contains 42 multimodal data of Iranian individuals who are the owner of public pages. Note that
the proﬁles were public at the time when the data was acquired and, since the users can change their
privacy settings, we can not ensure the proﬁle is publicly available anymore. Following the suggestion
of expert psychologist and the use of previous experience [1, 10, 11], we decided to mine pages that
look more realistic considering the current cultural, social, political, and economic conditions of Iran.
The data is composed of a set of images (with a maximum of 1000) posted by the subject and a JSON
ﬁle containing the caption of the photos including hashtags, and the geographical tags.
– Set 2 contains 44 multimodal data of Spanish individuals who are the owner of public pages. The
mentioned situations for gathering Iranian Instagram proﬁles were also observed in selecting Spain
proﬁles.
The expert psychologist visited each user’s proﬁle, and provided labels for them based on Glasser’s
choice theory. Therefore, one subject could be perceived as to be looking for any combination of all ﬁve
needs. Fig. 2 shows the perceived needs distribution for the two countries (Iran and Spain).
Fig. 2: Diversity of labels per country.
4 Automatic recognition of subject needs using SNS multimodal data
In this section, we propose a baseline approach for classifying the visual/textual data obtained from
the Instagram proﬁles of this database. In terms of machine learning, this is a multi-label classiﬁcation
problem given the fact that one or more categories can be perceived in the assessment of a subject. To
learn a classiﬁcation model, we used three diﬀerent feature representation methods:
– A feature space consisting of a bag of visual words using the SURF descriptor.
– A histogram of visual tags provided by two diﬀerent Convolutional Neural Networks.
– Textual descriptors from captions using word2vec [32] latent space.
We also explored a multimodal fusion of both visual and textual cues for the multi-label classiﬁcation.
4.1 Bag of Visual Words
The idea of bag-of-visual-words (BoVW) [6] was borrowed from natural language processing [44] in which
a histogram containing the frequency of word occurrence represents a document. In Bag of Visual Words,
the image is the equivalent of the document, and the words are cluster centers of local descriptors.
Diﬀerent feature descriptors can be used, and salient point detectors (SIFT or SURF descriptors) have
demonstrated their performance [21].
1 The database is available for research purposes upon request and EULA signature.


## Page 6


6
Dehshibi et al.
In this study, we used speeded-up robust features (SURF) [2]. To compute the keypoints and descrip-
tors, ﬁrst, a square-shaped ﬁlter of size 8 × 8 is applied to the integral image to produce the Laplacian
of Gaussians. Then, the Hessian matrix is calculated by using a blob detector to detect interest points.
Given a point p = (x, y) in an image I, the Hessian matrix H(p, σ) at point p and scale σ, is:
H(p, σ) =
 Dxx(p, σ) Dxy(p, σ)
Dxy(p, σ)v Dyy(p, σ)

(1)
where D•(p, σ) is the convolution of the second-order derivative of Gaussian with the image I at the
point p. The square-shaped ﬁlter of size 8 × 8 is an approximation of a Gaussian with σ = 1.2 which
represents the highest spatial resolution for blob-response maps. Afterwards a square window with the
size of 20 × 20 is extracted, centered on the interest point and oriented along the orientation to describe
the region around the point. Then, the interest region is split into smaller 4 × 4 square sub-regions, and
the Haar wavelets with a size of 2σ are calculated for each one. This results in feature vectors containing
64 dimensions which are invariant to rotation, change of scale and contrast. In order to convert vector-
represented patches into visual words and generate a representative dictionary, the vectors are clustered
into k (in this study k = 256) groups using k-means [22] and the cluster centers consider as a vocabulary
of k visual words. SURF feature descriptor [2] was applied to 30% of all images to construct the visual
vocabulary (BoVW). In our implementation, the block width is [32 64 96 128], and 80 percent of the
strongest features were kept, obtaining a feature vector x ∈XBoV W ⊆R256.
4.2 CNN-based Bag of Words for context information extraction
Another approach used to extract relevant clues and features from the images posted on SNS was utilizing
the scene information as well as the presence of certain objects. We used two diﬀerent pre-trained Deep
Neural Networks for this purpose: Microsoft Azure Cognitive Services [12, 31] to obtain information
regarding the objects that appear in the pictures as well as tags related to the image, and Places-CNN [45]
for a description of the scene. Fig. 3 shows the results of applying these state-of-the-art methods.
top-1: indoor (0.978)
top-2: person (0.866)
top-3: people (0.619)
(a)
top-1: restaurant (0.247)
top-2: cafeteria (0.236)
top-3: restaurant patio (0.172)
(b)
Fig. 3: (a) Results provided by Microsoft Cognitive Services [12, 31] with top provided tags, (b) the
Places-CNN [45] with the top provided results.
Places-CNN is a AlexNet [26] trained with Places365 [45], which is the latest subset of Places2
Database. This network has been trained with more than 1.8 million images from 365 scene categories. In
order to obtain information from the components of the scene, we also use the Microsoft Azure Cognitive
Services [12, 31] Computer Vision API, which provides a list of objects appearing in the image, relevant
tags, and dominant colors.


## Page 7


VICSOM: VIsual Clues from SOcial Media for psychological assessment
7
To generate a representative feature vector for each subject to be used for classiﬁcation, we used the
information obtained by the CNNs to create a Bag of Words. Speciﬁcally, for the outputs of the Azure
approach, we created a dictionary of tags, taking all the diﬀerent tags detected in all the images of the
database. In this case, the number of diﬀerent tags is 734. Therefore, for each subject, we generated a
histogram of occurrence of these tags in the photos that the subject has posted, obtaining a feature vector
x ∈XAzure ⊆R734.
For the information gathered from the Places-CNN, we generated a similar histogram, obtaining a
feature vector x ∈XP laces−CNN ⊆R344. However, since the results are exclusive from each other, we
decided to weight the occurrences in the histogram according to the score obtained in AlexNet.
4.3 Textual analysis
To investigate in textual information provided by users and understand its importance, we ﬁrst created
a word cloud model for each textual information which records the number of times that words appear
in each document in a collection. Figures (4a-4e) shows the top words used by the expert Psychologist
describing all proﬁles, Figures (4b-4f) show the word clouds from textual captions, Figures (4c, 4g, 4d,
and 4f) show the word clouds obtained from tags provided by visual object detectors. The ﬁrst row
is associated with Iranian proﬁles and the second row with Spanish proﬁles. Psychologist descriptions
literally ﬁt better with textual captions provided by users. For instance, one can see that the most intense
word in Fig. 4a is ‘belonging’ where the top-5 frequent words are {‘belonging’, ‘page’, ‘love’, ‘connect’,
‘satisfy’}.
In Fig. 4b, we have the cloud of captions which the boldest word is
2 and the top-5 words
translated into English are {‘day’, ‘love’, ‘eye’, ‘friend’, ‘window’}. Comparing these two sets, we can as-
sociate friend and love to ‘belonging’. However, the cases for Fig. 4c and 4d are almost diﬀerent. The top-5
words in these ﬁgures are {‘beautysalon’, ‘stage’, ‘artgalleries’, ‘artstudio’, ‘musicstudio’}, {‘man’, ‘white’,
‘wear’, ‘woman’, ‘black’}, respectively, which are not literally related to ‘Belonging/connecting/love,’.
(a)
(b)
(c)
(d)
(e)
(f)
(g)
(h)
Fig. 4: The word cloud of (a,e) psychologist deductions, (b,f) all captions provided by Instagram users,
(c,g) tags provided by Microsoft Cognitive Services, (d,h) tags provided by Place network applied to
images of Instagram proﬁle. [Top row] Iran proﬁles, [Bottom row] Spain proﬁles.
In order to use the textual information provided by the users in their SNS posts, we followed a similar
approach to the visual data. We generated a feature vector for each user to be classiﬁed in a further
2 The meaning in English is ‘day’.


## Page 8


8
Dehshibi et al.
step. The feature vector is the result of training a Word2vec [32] network, which learns an embedding
representation of a dataset of words. Therefore, all the tokenized words extracted from all the users’ posts
were used to train the network. Note that given the diﬀerences in Persian and Spanish languages, we
trained two diﬀerent networks. Once trained, the words of each user were passed through the network to
obtain their embedded representation. Finally, all the embedded vectors were averaged in order to obtain
an unique feature vector per user, x ∈Xtext ⊆R128.
4.4 Multi-label classiﬁcation
The natural way to tackle this problem is to follow a multi-label classiﬁcation rule. For example, a
psychologist can perceive from a user proﬁle that the individual tries to satisfy Power, Freedom, and Fun
needs simultaneously. Therefore, we decided to use Multi-Label Learning with GLObal and loCAL Label
Correlation (GLOCAL) method [47].
Let C = {c1, · · · , cl} be the set of l class labels. The d-dimensional feature vector of an instance is
denoted by x ∈X ⊆Rd, and the ground-truth label vector is denoted by ˜y ∈Y ⊆{−1, 1}l, where [˜y]j = 1
if x is with class label cj, and -1 otherwise. GLOCAL classiﬁer provides outputs by solving the following
optimization (Eq. 2). The outputs are encouraged to be similar on highly positively correlated labels, and
dissimilar on highly negatively correlated labels.
min
U,V,W,Z ∥J ◦(Y −UV ) ∥2
F +λ ∥V −W T X ∥2
F +
g
X
m=1
λ3nm
n
tr(F T
0 ZmZT
mF0) + λ4tr(F T
mZmZT
mFm)

+ λ2R(U, V, W)
subject to
diag(ZmZT
m) = 1, m = 1, 2, · · · , g.
(2)
where λ, λ2, λ3, λ4 are trade-oﬀparameters, R(U, V, W) is a regularizer, F is the vector containing pre-
dictions on all n instances, J = [Jij] is the indicator matrix, V represents the latent labels and U reﬂects
how the original labels are correlated to the latent labels. Y is the observed labels and W ∈Rd×k is used
to map instances to the latent labels. The W can be obtained by minimizing the square ∥V −W T X ∥2
F ,
where X = [x1, · · · , xn] ∈Rd×n is the matrix containing all the instances. L is a learning Laplacian
matrix which preserves the label correlation and can be written as a learning Z ≡{z1, · · · , Zg} for
m ∈{1, · · · , g}. tr(•) is the trace of •, ∥• ∥F is its Frobenius norm, diag(•) returns a vector containing
the diagonal elements of •. For two matrices of the same size, A and B, A ◦B denotes the Hadamard
(element-wise) product.
5 Experiments
We used cross-validation (leave one subject out) approach to evaluate the GLOCAL model due to the
limited number of the data samples. Therefore, we selected N −1 of the instances for training, and the
remaining for testing. This validation approach repeats N times for two subsets and results are averaged
over N independent repetitions to reduce statistical variability. The method received as input the four
feature spaces used in this paper (BoVW, Azure, Places-CNN and text). Due to the fact that the expert
psychologist uses both information from images and captions when carrying out the psychological assess-
ment, we also included a Fusion feature space where all the generated feature spaces were concatenated
and normalized.
Table 2 reports the evaluation criteria which are Average precision (Ap), Area under the ROC curve
(Auc), Hamming loss (Hl), and Jaccard similarity score (Jsc).
– Average precision (Ap) summarizes a precision-recall curve as the weighted mean of precision values
achieved at each threshold, with the increase in recall from the previous threshold used as the weight:
Ap = P
i(Ri −Ri−1)Pi where Pi and Ri are the precision and recall at the i-th threshold.
– Area under the ROC curve (Auc) deﬁnes the area under the plot of the fraction of true positives out
of the positives (TPR = true positive rate) vs. the fraction of false positives out of the negatives (FPR
= false positive rate), at various threshold settings.


## Page 9


VICSOM: VIsual Clues from SOcial Media for psychological assessment
9
– Hamming loss (Hl) is the fraction of labels that are incorrectly predicted. Hamming loss deﬁnes as
Hl =
1
LN
PL
l=1
PN
i=1 ˜yi,l ⊕f(xi,l), where ⊕is exclusive-or, L = card(C), N is the number of instances.
˜yi,l and f(xi,l) stand for Boolean that, in turn, the i-th data and prediction contains the l-th label.
– Jaccard similarity score (Jsc) is the size of the intersection of the predicted labels f(x) and the true
labels ˜y divided by the size of the union of the predicted and true labels. Jsc is given by Jsc(f(x), ˜y) =
f(x)∩˜y
f(x)∪˜y
Moreover we calculated Ranking loss and Coverage as in [46]. Let p be the number of test instances,
C+
i , C−
i be the sets of positive and negative labels associated with the i-th instance; and Z+
j , Z−
j be the
sets of positive and negative instances belonging to the j-th label. Given input x, let (rank)f(x, y) be
the rank of label y in the predicted label ranking (sorted in descending order).
– Ranking loss (Rkl): This is the fraction that a negative label is ranked higher than a positive label. For
instance i, deﬁne Qi = {(j
′, j
′′)|fj′(xi) ≤fj′′(xi), (j
′, j
′′) ∈C+
i ×C−
i }. Then, Rkl = 1
p
Pp
i=1
|Qi|
|C+
i ||C−
i |.
– Coverage (Cvg): This counts how many steps are needed to move down the predicted label ranking
so as to cover all the positive labels of the instances. Cvg = 1
p
Pp
i=1 max{rankf(xi, j)|j ∈C+
i } −1.
For Auc, Ap and Jsc, the higher are the better; whereas for Rkl, Cvg and Hl, the lower are the better.
Table 2: Results of applying GLOCAL to public proﬁles of Iran (42 users) and Spain (46 users) Instagram
considering ranking loss (Rkl), average area under curve (Auc), coverage (Cvg), average precision (Ap),
Hamming loss (Hl), and Jaccard similarity score (Jsc).‘#dim’ is the dimension of feature vector. We show
the mean measurement with 95% conﬁdence intervals.
Feature Space
#dim
Rkl
Auc
Cvg
Ap
Hl
Jsc
Iran
BoVW
256
0.079 ± 0.01
0.778 ± 0.08
1.549 ± 0.05
0.814 ± 0.07
0.285 ± 0.07
0.714 ± 0.08
Places-CNN
344
0.086 ± 0.02
0.671 ± 0.12
1.574 ± 0.12
0.693 ± 0.12
0.406 ± 0.09
0.593 ± 0.09
Azure
734
0.079 ± 0.01
0.760 ± 0.09
1.552 ± 0.08
0.756 ± 0.11
0.351 ± 0.07
0.648 ± 0.07
Word2Vec
128
0.145 ± 0.04
0.805 ± 0.08
1.808 ± 0.31
0.835 ± 0.07
0.250 ± 0.07
0.750 ± 0.07
Fusion
1462
0.142 ± 0.06
0.803 ± 0.09
1.768 ± 0.33
0.785 ± 0.10
0.339 ± 0.07
0.660 ± 0.07
Spain
BoVW
256
0.060 ± 0.01
0.927 ± 0.05
1.426 ± 0.06
0.928 ± 0.05
0.156 ± 0.05
0.843 ± 0.05
Places-CNN
344
0.063 ± 0.01
0.789 ± 0.11
1.504 ± 0.06
0.805 ± 0.09
0.281 ± 0.07
0.718 ± 0.07
Azure
734
0.051 ± 0.01
0.875 ± 0.07
1.442 ± 0.05
0.913 ± 0.05
0.250 ± 0.08
0.750 ± 0.08
Word2Vec
128
0.064 ± 0.03
0.927 ± 0.04
1.442 ± 0.20
0.889 ± 0.07
0.200 ± 0.05
0.800 ± 0.05
Fusion
1462
0.064 ± 0.04
0.933 ± 0.05
1.491 ± 0.250
0.917 ± 0.07
0.143 ± 0.06
0.856 ± 0.06
As we can see in Table 2, classiﬁcation using features generated with Word2vec from the textual
information of captions outperforms the rest of the methods using most of the metrics for the case of
users from Iran. For Spanish users the fusion of features from images and text works the best. These
ﬁndings show the relevance of the textual information in the classiﬁcation. Therefore, one could say that
the information shared by the users in the captions of the photos are important cues for perceiving their
pursuit of needs.
Among the methods using information from images, SURF-based BoVW is the one with the best
results. Since these features are extracted directly from the images, they represent better their information.
On the other hand, features obtained with Places-CNN or Azure are generated from the occurrence of
objects and tags at a higher level, missing features present on the images themselves. We conjecture that
more sophisticated models of scene understanding that could take into account high level relationships
between objects could increase the performance of these descriptors. Similarly, a more robust captioning
about the scene contents (speciﬁcally regarding to the nature of the interactions among the people present
in the scene) would improve the predicted perception of needs.
6 Conclusion
We introduced the VICSOM database, a multimodal database of 86 public Instagram accounts, containing
30,080 images, assessed by an expert psychologist with a focus on human needs. We considered gender
and age diversities in harvesting proﬁles where the subjects belong to the age interval of 15-50 with a
gender ratio (male/female) of 1.68. To perceive needs, the expert psychologist took the Glasser’s choice
theory into account in which it is stated that human behaviors are driven by ﬁve genetically driven


## Page 10


10
Dehshibi et al.
needs including survival, love and belonging, freedom, fun, and power. The VICSOM DB has also been
made publicly available to the research community, representing a benchmark for eﬀorts in automatic
categorizing human needs over Instagram as a trending social network site (SNS).
We provided exhaustive baseline experiments to assess textual/visual features in advancing the ﬁeld
of multimodal SNS analysis which would help in screening mental health. In the line of experiments, a
multi-label classiﬁer was trained and evaluated by three diﬀerent feature representation methods which
are (1) a bag of visual words formed by SURF descriptor, (2) a histogram of visual tags provided by
two diﬀerent Convolutional Neural Networks, and (3) textual descriptors by creating vectors that are
distributed numerical representations of word features using Word2vec. We also explored a multimodal
fusion of both visual and textual cues for the multi-label classiﬁcation. We believe this data corpus will be
helpful to the community, both in the psychological ﬁeld in helping test hypothesis and in the computer
science ﬁeld to advance the state of automatic SNS analysis.
We observed that the subjects’ needs had experienced an evolution during the time. Therefore, one
open research line is to investigate this evolution rather than considering static information at the moment
of analysis. Furthermore, users of a speciﬁc SNS usually have proﬁles in other social networking sites which
can be used for the screening together. Since the Instagram introduced ‘live’ and ‘story’ features, the taste
of users is also shifting into sharing this kind of posts. In this way, further study can be performed using
the visual and textual information from this data. In addition, further developments could include the use
of other modalities, such as data from wearable devices (accelerometers, global localization) or regular
communications (email, blogs, ...).
We noticed that scene description algorithms lack in ﬁnding the emotional state of a scene in which
humans have social interactions. Indeed, not only objects, scenes, and sentiments but also relationships
among scene components could be considered. For instance, if users shared images of themselves in a
family gathering with intimate partners, it is likely to perceive that they look for a way to satisfy the
need of belonging. However, if the image shows the interaction of users with religious groups, the inference
about their need could be diﬀerent.
There are other categorizations of human needs that could be explored in the future. For instance, one
can consider the Transactional theory proposed by Eric Berne et al. [3] in which the principal characters
are child, parent, and mature. We also plan as a future works to explore more robust fusion rules for
multimodal exploration and the use of alternative multilabel classiﬁers.
Acknowledgements
This research was supported by TIN2015-66951-C2-2-R, RTI2018-095232-B-C22 grant from the Spanish
Ministry of Science, Innovation and Universities (FEDER funds), and NVIDIA Hardware grant program.
Additional Information
Implementations are available at https://github.com/dehshibi/VICSOM
References
1. Bastanfard A, Nik MA, Dehshibi MM (2007) Iranian face database with age, pose and expression.
Machine Vision pp 50–55
2. Bay H, Tuytelaars T, Van Gool L (2006) Surf: Speeded up robust features. In: European conference
on computer vision, Springer, pp 404–417
3. Berne E, Steiner CM, Dusay JM (1996) Transactional analysis. Essential papers on short term dy-
namic therapy Essential papers in psychoanalysis New York University Press, New York pp 149–170
4. Boyd DM, Ellison NB (2007) Social network sites: Deﬁnition, history, and scholarship. Journal of
computer-mediated Communication 13(1):210–230
5. Christakis NA, Fowler JH (2010) Social network sensors for early detection of contagious outbreaks.
PloS one 5(9):e12948
6. Csurka G, Dance CR, Fan L, Willamowski J, Bray C (2004) Visual categorization with bags of
keypoints. In: In Workshop on Statistical Learning in Computer Vision, ECCV, pp 1–22


## Page 11


VICSOM: VIsual Clues from SOcial Media for psychological assessment
11
7. De Choudhury M, Counts S, Horvitz E (2013) Predicting postpartum changes in emotion and behavior
via social media. In: Proceedings of the SIGCHI Conference on Human Factors in Computing Systems,
ACM, pp 3267–3276
8. De Choudhury M, Kiciman E, Dredze M, Coppersmith G, Kumar M (2016) Discovering shifts to sui-
cidal ideation from mental health content in social media. In: Proceedings of the 2016 CHI conference
on human factors in computing systems, ACM, pp 2098–2110
9. Deckers L (2018) Motivation: Biological, psychological, and environmental. Routledge
10. Dehshibi MM, Bastanfard A (2010) A new algorithm for age recognition from facial images. Signal
Processing 90(8):2431–2444
11. Dehshibi MM, Shanbehzadeh J (2017) Cubic norm and kernel-based bi-directional pca: toward age-
aware facial kinship veriﬁcation. The Visual Computer pp 1–18
12. Del Sole A (2018) Introducing microsoft cognitive services. In: Microsoft Computer Vision APIs
Distilled, Springer, pp 1–4
13. Dodds PS, Harris KD, Kloumann IM, Bliss CA, Danforth CM (2011) Temporal patterns of happiness
and information in a global social network: Hedonometrics and twitter. PloS one 6(12):e26752
14. Friedman HS, Schustack MW (1999) Personality: Classic theories and modern research. Allyn and
Bacon Boston, MA
15. Glasser W (1999) Choice theory: A new psychology of personal freedom. HarperPerennial
16. Gonzales AL, Hancock JT (2011) Mirror, mirror on my facebook wall: Eﬀects of exposure to facebook
on self-esteem. Cyberpsychology, Behavior, and Social Networking 14(1-2):79–83
17. Harman G, Dredze MH (2014) Measuring post traumatic stress disorder in twitter. In ICWSM
18. Harries T (2008) Feeling secure or being secure? why it can seem better not to protect yourself against
a natural hazard. Health, risk & society 10(5):479–490
19. Henwood BF, Derejko KS, Couture J, Padgett DK (2015) Maslow and mental health recovery: A
comparative study of homeless programs for adults with serious mental illness. Administration and
Policy in Mental Health and Mental Health Services Research 42(2):220–228
20. Howell RT, Kurai M, Tam L (2013) Money buys ﬁnancial security and psychological need satisfaction:
Testing need theory in aﬄuence. Social Indicators Research 110(1):17–29
21. Juan L, Gwon L (2007) A comparison of sift, pca-sift and surf. International Journal of Signal
Processing, Image Processing and Pattern Recognition 8(3):169–176
22. Kanungo T, Mount DM, Netanyahu NS, Piatko CD, Silverman R, Wu AY (2002) An eﬃcient k-
means clustering algorithm: analysis and implementation. IEEE Transactions on Pattern Analysis
and Machine Intelligence 24(7):881–892
23. Katikalapudi R, Chellappan S, Montgomery F, Wunsch D, Lutzen K (2012) Associating internet
usage with depressive behavior among college students. IEEE Technology and Society Magazine
31(4):73–80
24. Kim Y, Kim JH (2018) Using computer vision techniques on instagram to link users personalities and
genders to the features of their photos: An exploratory study. Information Processing & Management
54(6):1101–1114
25. Kircaburun K, Griﬃths MD (2018) Instagram addiction and the big ﬁve of personality: The mediating
role of self-liking. Journal of behavioral addictions 7(1):158–170
26. Krizhevsky A, Sutskever I, Hinton GE (2012) Imagenet classiﬁcation with deep convolutional neural
networks. In: Advances in neural information processing systems, pp 1097–1105
27. Mak BL, Sockel H (2001) A conﬁrmatory factor analysis of is employee motivation and retention.
Information & management 38(5):265–276
28. Maslow AH (1943) A theory of human motivation. Psychological review 50(4):370
29. Maslow AH (1954) Motivation and personality. Motivation and personality., American Psychological
Association, Oxford, England
30. Maslow AH (2013) Toward a psychology of being. Simon and Schuster
31. Microsoft
(2019)
Microsoft
Computer
Vision
API.
https://azure.microsoft.com/en-us/
services/cognitive-services/computer-vision/, online; Accessed: 2019-02-26
32. Mikolov T, Chen K, Corrado G, Dean J (2013) Eﬃcient estimation of word representations in vector
space. In: 1st International Conference on Learning Representations, ICLR 2013,Scottsdale, Arizona,
USA, May 2-4, 2013, Workshop Track Proceedings
33. Moreno MA, Christakis DA, Egan KG, Brockman LN, Becker T (2012) Associations between dis-
played alcohol references on facebook and problem drinking among college students. Archives of


## Page 12


12
Dehshibi et al.
pediatrics & adolescent medicine 166(2):157–163
34. Oh HJ, Ozkaya E, LaRose R (2014) How does online social networking enhance life satisfaction? the
relationships among online supportive interaction, aﬀect, perceived social support, sense of commu-
nity, and life satisfaction. Computers in Human Behavior 30:69–78
35. Pampouchidou A, Simos P, Marias K, Meriaudeau F, Yang F, Pediaditis M, Tsiknakis M (2017)
Automatic assessment of depression based on visual cues: A systematic review. IEEE Transactions
on Aﬀective Computing
36. Persson G (2017) Love, aﬃliation, and emotional recognition in# k¨ampamalm¨o:the social role of
emotional language in twitter discourse. Social Media+ Society 3(1):2056305117696522
37. Ponce-L´opez V, Chen B, Oliu M, Corneanu C, Clap´es A, Guyon I, Bar´o X, Escalante HJ, Escalera S
(2016) Chalearn lap 2016: First round challenge on ﬁrst impressions-dataset and results. In: European
Conference on Computer Vision, Springer, pp 400–418
38. Reece AG, Danforth CM (2017) Instagram photos reveal predictive markers of depression. EPJ Data
Science 6(1):15
39. Reece AG, Reagan AJ, Lix KL, Dodds PS, Danforth CM, Langer EJ (2017) Forecasting the onset
and course of mental illness with twitter data. Scientiﬁc reports 7(1):13006
40. Rojas M, Masip D, Todorov A, Vitri`a J (2010) Automatic point-based facial trait judgments eval-
uation. In: 2010 IEEE Computer Society Conference on Computer Vision and Pattern Recognition,
IEEE, pp 2715–2720
41. Steere BF (1988) Becoming an Eﬀective Classroom Manager. SUNY Press
42. Taormina RJ, Gao JH (2013) Maslow and the motivation hierarchy: Measuring satisfaction of the
needs. The American journal of psychology 126(2):155–177
43. Weiser EB (2015) # me: Narcissism and its facets as predictors of selﬁe-posting frequency. Personality
and Individual Diﬀerences 86:477–481
44. Zhang Y, Jin R, Zhou ZH (2010) Understanding bag-of-words model: a statistical framework. Inter-
national Journal of Machine Learning and Cybernetics 1(1-4):43–52
45. Zhou B, Lapedriza A, Khosla A, Oliva A, Torralba A (2018) Places: A 10 million image database for
scene recognition. IEEE transactions on pattern analysis and machine intelligence 40(6):1452–1464
46. Zhou ZH, Zhang ML, Huang SJ, Li YF (2012) Multi-instance multi-label learning. Artiﬁcial Intelli-
gence 176(1):2291–2320
47. Zhu Y, Kwok JT, Zhou ZH (2018) Multi-label learning with global and local label correlation. IEEE
Transactions on Knowledge and Data Engineering 30(6):1081–1094

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1905_06203v1_vicsom_visual_clues_from_social_media_for_psychological_assessment
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1905_06203V1_VICSOM_VISUAL_CLUES_FROM_SOCIAL_MEDIA_FOR_PSYCHOLOGICAL_ASSESSMENT.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

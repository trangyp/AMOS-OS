---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1912.12012v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1912.12012v1_Graduate_Employment_Prediction_with_Bias

> Source: 1912.12012v1_Graduate_Employment_Prediction_with_Bias.pdf

> Pages: 9

---


## Page 1


Graduate Employment Prediction with Bias
Teng Guo,1 Feng Xia,1,2 Shihao Zhen,1 Xiaomei Bai,3 Dongyu Zhang,1∗Zitao Liu,4 Jiliang Tang5
1Key Laboratory for Ubiquitous Network and Service Software of Liaoning Province,
Dalian University of Technology, Dalian 116620, China
2School of Science, Engineering and Information Technology, Federation University Australia, Ballarat, VIC 3353, Australia
3Computing Center, Anshan Normal University, Anshan 114007, China
4TAL AI Lab, TAL Education Group, Beijing 100080, China
5Department of Computer Science and Engineering, Michigan State University, East Lansing, MI 48824, USA
Abstract
The failure of landing a job for college students could cause
serious social consequences such as drunkenness and suicide.
In addition to academic performance, unconscious biases can
become one key obstacle for hunting jobs for graduating stu-
dents. Thus, it is necessary to understand these unconscious
biases so that we can help these students at an early stage
with more personalized intervention. In this paper, we de-
velop a framework, i.e., MAYA (Multi-mAjor emploYment
stAtus) to predict students’ employment status while consid-
ering biases. The framework consists of four major compo-
nents. Firstly, we solve the heterogeneity of student courses
by embedding academic performance into a uniﬁed space.
Then, we apply a generative adversarial network (GAN) to
overcome the class imbalance problem. Thirdly, we adopt
Long Short-Term Memory (LSTM) with a novel dropout
mechanism to comprehensively capture sequential informa-
tion among semesters. Finally, we design a bias-based regu-
larization to capture the job market biases. We conduct exten-
sive experiments on a large-scale educational dataset and the
results demonstrate the effectiveness of our prediction frame-
work.
1
Introduction
Education, as the basic means of improving individual abil-
ities, makes students competitive in recruitment. However,
not every graduate can succeed in job hunting. The data from
the statistical ofﬁce of the European Union (EU) shows that
the employment rate in the EU of 20-34 years old is 83.4%
for tertiary education and 65.8% for upper secondary general
education in 2018 (Eurostat 2019). The failure of job hunt-
ing could cause serious consequences like suicide (Drum et
al. 2009; Westefeld et al. 2005). Therefore, detecting stu-
dents with trouble in landing a job timely and providing
personalized intervention and guidance at an early stage are
greatly desired.
However, detecting these students faces tremendous chal-
lenges because recruitment might be impacted by various
factors (Luo and Pardos 2018). Every recruiter aims to hire
the best employees. However, in addition to academic per-
formance (Kong et al. 2018), recruitment decisions can be
∗Corresponding
author:
Dongyu
Zhang
(email:
zhang-
dongyu@dlut.edu.cn)
affected by unconscious biases, such as gender (Clauset,
Arbesman, and Larremore 2015). These biases not only lead
to imbalance in the hiring process, resulting in uniformity
in the workplace instead of diversity, but also result in the
inequality of employment (Giannakas, Fulton, and Awada
2017; Ford et al. 2018; Liang, Hong, and Gu 2018), espe-
cially for fresh graduates who have no work experience.
Therefore, it is necessary to understand biases in recruit-
ment, which can further be exploited for the prediction of
graduates’ employment. Nevertheless, previous related re-
searches have been mainly based on questionnaires, which
are time- and cost-consuming and hardly applicable to large-
scale students.
Thanks to the advance of information technology, we are
able to digitalize records of students in schools which prod-
uct rich data about students. It enables the data-driven de-
velopment(Wu et al. 2013; Liu et al. 2018) and provides
us an opportunity to deepen our understandings on the em-
ployment of students. However, to achieve the goal, we face
tremendous challenges. First, such data is much more com-
plex than that based on questionnaires, thus advanced tech-
niques are needed. Second, the number of graduates that
cannot land a job is much smaller compared to these who
can successful obtain jobs, thus employment analysis and
prediction are highly imbalanced. Third, there may exist bi-
ases in employment that can be varied by majors; while the
majority of existing algorithms seldom consider possible bi-
ases.
In this paper, we are devoted to exploring the biases in
different majors from demographics aspects, and predicting
students with trouble in landing a job at an early stage. First,
we analyze the employment biases for each major from 4
aspects including gender, nation, hometown, and enroll sta-
tus. Second, based on possible employment biases, we pro-
pose a MAYA (Multi-mAjor emploYment stAtus) predic-
tion framework, with four important components. In the ﬁrst
component, we solve the heterogeneity of students’ courses
through embedding academic performance into a space of
uniﬁed dimension by autoencoder. Then GAN (Generative
Adversarial Networks) is applied to generate data of the mi-
nority class, to overcome the label imbalance problem. Next,
considering the sequential information between semesters,
arXiv:1912.12012v1  [cs.LG]  27 Dec 2019


## Page 2


the Long Short-Term Memory (LSTM) with a novel dropout
mechanism is utilized. Finally, we design a model to cap-
ture the employment biases of different majors. Our contri-
butions can be summarized as follows:
• We provide a comprehensive and systematic analysis on
employment biases.
• We model the employment biases in different majors and
incorporate them into our proposed prediction framework.
• We conduct comprehensive experiments on a large-scale
educational dataset and the extensive results demonstrate
the effectiveness of our prediction framework.
This paper is organized as follows. In Section 2, related
work is reviewed. The problem formulation is presented in
Section 3. In Section 4, we analyze the employment biases
by majors. In Section 5, the MAYA prediction framework is
introduced in detail. In Section 6, we analyze the results of
our experiment. We present the discussion and conclusion of
our work in Section 7.
2
Related Work
2.1
Employment of College Graduates
Whether a college student can ﬁnd a job after graduation
attracts tons of attention in recent decades. Liu et al (Liu,
Silver, and Bemis 2018) develop a tool for career explo-
ration based on the intuitiveness of node-link diagrams and
the scalability of aggregation-based techniques to help the
student understand the process of employment. Kong et al
(Kong et al. 2018) carry out a series of experiments to
explore the relationship between students’ academic per-
formance and their graduation whereabouts. Uosaki et al
(Uosaki et al. 2018) develop a career support system to help
the international student ﬁnd a job in Japan through their log
record and eBook reading. Liu et al (Liu et al. 2017) design
a job recommendation service framework for university stu-
dents. According to a student proﬁling based re-ranking rule,
users are recommended a list of potential jobs. Soumya et al
(Soumya and Sugathan 2017) make a framework to identify
student’s eligibility for a speciﬁc job by calculating the do-
main competencies and job competency score.
2.2
Dropout in Recurrent Neural Network
Dropout is a mechanism that stops a part of neurons to im-
prove generalization performance (Srivastava et al. 2014).
Zaremba et al (Zaremba, Sutskever, and Vinyals 2014) ap-
ply dropout technology on RNN with 0 memory loss through
only applying the dropout operator on the non-recurrent con-
nection. Moon et al (Moon et al. 2015) propose an effective
solution to better preserve memory when applying dropout
through generating a mask on input sequence and moving
it at every time step. Gal et al (Gal and Ghahramani 2016)
propose a Bayesian interpretation-based RNN dropout vari-
ant method. They generate a dropout mask according to the
theory of the Bayesian posterior and keep the same mask for
each time step in the sequence. Zhu et al (Zhu et al. 2016)
propose a dropout method for multilayer LSTM. To keep
information stored in memory, they only allow the dropout
mechanism to ﬂow along with layers and prohibit it to ﬂow
along with the timeline. Billa Jayadev (Billa 2018) test the
dropout mechanism on LSTM algorithm based on a speech
recognition system and the results with two datasets are im-
proved about 24.64% and 13.75%, respectively.
3
Problem Statement
In this section, we will introduce some notations and then
formally deﬁne the problem in this work. In a univer-
sity, let M
=
{1, 2, ..., M} denote the set of majors
and the set of students in every major is deﬁned as Q
= {N1,N2,...,NM}. For student i in major m, we deﬁne
the academic vector as am
i
∈Rn that will be intro-
duced in the following section. The feature vector and ﬁ-
nal employment status are denoted as dm
i
∈Rp and
ym
i
∈{0, 1}. Let Dm = [dm
1 , dm
2 , ...dm
|NM|] ∈R|NM|×p,
Am
=
[am
1 , am
2 , ...am
|NM|]
∈
R|NM|×n and ym
=
[ym
1 , ym
2 , ...ym
|NM|] ∈R|NM| represent the feature matrix,
the academic performance matrix and the employment sta-
tus vector. The details of features used in this research are
described in the following section.
Employment Status Prediction Problem: given the fea-
ture vector dm
i
and the corresponding academic perfor-
mance vector am
i , then we predict the ﬁnal employment sta-
tus ym
i .
4
Bias Analysis
4.1
Dataset
The dataset used in this experiment includes 2,133 students
from a Chinese university. They all enrolled in 2013 and
graduated in 2017. They are from 64 different majors in-
volved in 13 colleges. This dataset consists of three types of
information, which are described as follows:
Demographic Data
Students are required to submit per-
sonal information at the time of admission, like hometown,
gender, and nation. For the privacy concern, the students are
already pseudonymous in the raw data. The demographic
data includes 2,133 records.
Academic Performance Data
Students’ academic perfor-
mance data contains scores and credits of courses. There are
in total 195,234 academic records.
Employment Data
When ﬁnding a job, students need to
sign tripartite agreements to guarantee their legal rights, thus
universities own records of students’ employment status in-
formation about related companies and government agen-
cies. This dataset consists of 2,133 records.
4.2
Bias in Employment
In this subsection, we analyze the bias in employment from
two levels: major-level and college-level. We only show the
results of the major-level and leave these of school-level in
the Supplemental Material. We check the bias from four as-
pects: gender (Ford et al. 2018), nation (the minority or the
majority) (Al-Ubaydli and List 2019), administrative level
of hometown (city or county) (Liang, Hong, and Gu 2018),


## Page 3


0
1 0
2 0
3 0
4 0
0 . 0 0
0 . 2 5
0 . 5 0
0 . 7 5
1 . 0 0
P - v a l u e
M
a j o r s
H o m e t o w n
0
1 0
2 0
3 0
4 0
5 0
0 . 0 0
0 . 2 5
0 . 5 0
0 . 7 5
1 . 0 0
N a t i o n
P - v a l u e
M
a j o r s
0
1 0
2 0
3 0
4 0
0 . 0 0
0 . 2 5
0 . 5 0
0 . 7 5
1 . 0 0
E n r o l l  s t a t u s
P - v a l u e
M
a j o r s
0
1 0
2 0
3 0
4 0
5 0
0 . 0 0
0 . 2 5
0 . 5 0
0 . 7 5
1 . 0 0
G e n d e r
P - v a l u e
M
a j o r s
Figure 1: The distribution of p-value with respective to majors on employment status. Subﬁgures denote the results of chi-
square test in terms of hometown, nation, enroll status and gender, respectively. Each black dot represents the p-value of a
certain major. When p-value is less than the threshold (e.g., 0.05 shown as red stars), the hypothesis is acceptable, that is, bias
exists.
Figure 2: The illustration of MAYA.
and enroll status (whether passing the college entrance ex-
amination at one time). Chi-square test is used here to ex-
amine the impact of these features on 64 different majors
involved in our dataset. Bias analysis of employment status
is shown in Figure 1 . From the ﬁgure, the majors with bias
in recruitment are shown as follows:
• Gender: English, Applied Psychology, Electronic Infor-
mation Science and Technology.
• Administrative Level of Hometown: Physical Educa-
tion.
• Enroll Status: Preschool education, English, Electronic
Information Science and Technology, Food Science and
Engineering.
• Nation: Information and Computing Science, Computer
Science and Technology.
These observations suggest that employment bias do exists
in some majors and the existence of bias does affect grad-
uates’ employment. Note that we also analyze the bias in
employment choice and results are provided in the Supple-
mental Material.
5
The Proposed MAYA Prediction
Framework
In this section, we provide a detailed description of the pro-
posed framework, MAYA. Figure 2 shows an illustration of
the MAYA framework. The framework has four components
including representation learning of academic performance,
data augmentation for label imbalance, prediction model,
and bias-based optimization. Next we detail each compo-
nent.


## Page 4


5.1
Academic Performance Representation
When taking academic performance as features, the hetero-
geneity of curriculum is always a challenge, due to the dif-
ference in students who take courses for each semester. In
this work, we propose a C matrix and based on C, we use an
auto-encoder to get the embedding representation to tackle
the heterogeneity.
C Matrix
To solve the problem caused by the heterogene-
ity, we create the matrix Cs ∈Rns×ms where ns and ms
represent the number of students and the number of courses,
respectively. In our dataset, s = 1, 2, ...6 since students have
valid grades of 6 semesters except for the two-semester grad-
uation project and social practice. cij is the grade of student
i on course j. If a student does not attend a particular course,
the corresponding element remains 0. The size of this matrix
is different for each semester as shown in the following ma-
trix. For example, there are 300 students and 500 courses in
the ﬁrst semester, then the size of C1 matrix is 300 × 500.







c11
c12
· · ·
c1n
c21
c22
· · ·
c2n
...
...
...
...
cm1
cm2
· · ·
cmn







Representation Learning
C matrix is quite sparse, thus
we use the autoencoder to get the embedding representation
that is the academic performance matrix A. The hidden lay-
ers of the autoencoder are divided into two parts: the encoder
part and the decoder part. The layers consistently encode and
decode the input data. The input of the ith layer is consid-
ered as the output of (i −1)th layer. The hidden layers can
automatically capture the characteristics of input data and
keep them unchanged. To capture the temporality among
semesters, we use autoencoder to embed the matrix of each
semester, respectively. In each hidden layer, we adopt the
following nonlinear transformation function:
h(2) = f(W (2)h(1) + b(2))
h(3) = f(W (3)h(2) + b(3))
h(i) = f(W (i)h(i−1) + b(i)), i = 1, 2, ...k
(1)
where f is the activation function and W (i), b(i) are the
transformation matrix and the bias vector. We use C as the
input and minimize the reconstruction error between the out-
put and the original input. Then, we take the output of the
encoder as the academic performance matrix A.
5.2
Data Augmentation for Label Imbalance
In general, the number of students who fail to land a job is
smaller, leading to a label imbalance problem. Thus, we em-
ploy generative adversarial networks (GAN) (Goodfellow et
al. 2014) to augment data in order to improve the generaliza-
tion performance. GAN consist of two components: a gen-
erator G and a discriminator D that compete in a two-player
mini-max game on V (D, G):
min
G max
D V (D, G) = Ex∼pdata[logD(x)]+
Ex∼pz(z)[log(1 −D(G(z))]
(2)
Figure 3: The diagram of LSTM.
The generator G shown in Figure 2 takes a random vector
from a uniform distribution as input. It outputs a vector in-
cluding all features of the corresponding class (i.e., the stu-
dents failed in job hunting). Then, the generated data and the
real data are entered into discriminator D for classiﬁcation.
Through repeated training, the D can not identify the gener-
ated data from the real data. Then we use G to generate data
of students failed in job hunting until the two categories are
balanced. In other words, we aim to implicitly learn the dis-
tribution of data of students failed in job hunting, to further
generate new samples.
5.3
Prediction Model
We utilize LSTM to capture the sequentiality between
semesters for prediction. LSTM is an RNN architecture
that uses a vector of cells ct ∈Rn with several element-
wise multiplication gates to manage information. Generally,
dropout aims to combine many ’thinned’ networks to im-
prove the performance of prediction. Some neurons are ran-
domly dropped during the training stage in order to force the
remaining sub-network to compensate. Then all the neurons
are used for predictions during the testing stage.
In this work, we design a temporal dropout structure
to improve the generalization performance. Previous re-
searches show that it’s not expected to erase information
from a unit who remembers events that occurred many
timestamps back in the past (Pham et al. 2014; Zhu et al.
2016). However, using complex models on a relatively sim-
ple dataset can easily cause overﬁtting. Moreover, the time
span is not very long in our problem. Thus we allow the
information of dropout in LSTM to ﬂow along the time di-
mension. We utilize the classical LSTM framework shown
as follows:
it = σ(W xixt + W hiht−1 + W cict−1 + bi)
f t = σ(W xfxt + W hfht−1 + W cfct−1 + bf)
ct = (f t ⊙ct−1 + it ⊙tanh(W xc + W hcht−1 + bc))
ot = σ(W xoxt + W hoht−1 + W coct + bo)
ht = ot ⊙tanh(ct)
(3)
where σ(x) is the sigmoid function deﬁned as σ(x) =
1
1+e−x . W αβ denotes the weight matrix between α and β
(e.g., W xi is the weight matrix from input xt to the input
gate it), bα is the bias term of α ∈{i, f, c, o}.
Inspired by (Zhu et al. 2016), we design an LSTM vari-
ant that allows the information of dropout in LSTM to ﬂow


## Page 5


along the time dimension through designing the mask vec-
tor m to drop the gates. The structure is shown in Figure 3,
deﬁned by the following equations:
it = σ(W xixt + W hiht−1 + W cict−1 + bi) ⊙mi
f t = σ(W xfxt + W hfht−1 + W cfct−1 + bf) ⊙mf
ct = (f t ⊙ct−1 + it ⊙tanh(W xc + W hcht−1 + bc))
⊙mc
ot = σ(W xoxt + W hoht−1 + W coct + bo) ⊙mo
ht = ot ⊙tanh(ct) ⊙mh
(4)
where ⊙represents element-wise product and mf, mc, mo
and mh are dropout binary mask vectors, with an element
value of 0 indicating that dropout happens, for input gates,
forget gates, cells, output gates and output gates, respec-
tively.
In our case, since we use single-layer LSTM, we only
need to consider error back-propagation in the same network
layer and the errors to output responses ht are:
ϵt
h = ϵt
h+1 ⊙mh
(5)
where ϵh+1 represents the back-propagation error vectors
from the next time in the same network layer.
Based on the Eq. 4, we get the errors from ht to ot which
represents the errors from next time with dropout involved:
ϵt
o = (ϵt
h ⊙∂ht
∂ot
) ⊙mo = ϵt
h ⊙tanh(ct) ⊙mo
(6)
Using the same approach, we can get the back-propagation
errors of other gates and the details are provided in the Sup-
plemental Material.
5.4
Bias-based Optimization
Modeling Employment Bias
As mentioned above, bias is
varied by majors in employment. This ﬁnding motivates us
to eliminate the inﬂuence of bias in various majors. There-
fore, we propose a smoothed regularization for the steady
change of weight, deﬁned as follow:
ΩM = 1
2
M
X
m=1
M
X
n>m
||W · (um −un)||2
F
(7)
where W is the weight matrix of LSTM mentioned above.
|| · ||2
F denotes the Frobenius norm. um ∈Rp indicates the
importance of the p tested aspects in prediction for students
in major m. It is represented by the p-value of chi-square test
calculated in the Section 4 through a transformation function
for emphasizing the importance of biases. In other words,
the lower the p value, the greater the weight of the bias. The
transformation function is deﬁned as follows:
f(u) = e1−u −e1+u
e1−u + e1+u
(8)
Optimization
Based on the discussion above, we formu-
late the whole loss function of our MAYA prediction frame-
work as follows:
3
6
1 2
2 4
3 2
6 4
8 0
9 6
0 . 0 0 5
0 . 0 1 0
0 . 0 1 5
0 . 0 2 0
V a l u e  o f  l o s s
D i m e n s i o n s  o f  a u t o - e n c o d e r
 S 1  
 S 2  
 S 3
 S 4  
 S 5  
 S 6
Figure 4: The results of representation learning.
L = 1
2
M
X
m=1
(W xm
i −ym
i )2 + ΩM
(9)
Its corresponding gradient is shown as follows:
∇L(W ) =
M
X
m=1
W xm
i (xm
i )T −ym
i (xm
i )T+
M
X
m=1
N
X
n>m
W (um −un)(um −un)T
(10)
6
Experiment
In this section, we would present the experimental results
in detail to demonstrate the effectiveness of our proposed
MAYA. We ﬁrst introduce the experimental settings, then
present comparison results and ﬁnally investigate important
parameters of the proposed framework.
6.1
Experimental Settings
To deal with the heterogeneity of courses enrolled by stu-
dents each semester, we design a C matrix to denote
students’ academic performance. The four-year university
life involves 8 semesters. Campus recruitment takes place
densely at the beginning of the last year. Hence, only the
academic performance of the previous three years (or six
semesters S1 to S6) would affect students’ employment.
Autoencoder is applied to embed academic performance
data to overcome the heterogeneity of course selection. We
test the different dimensions including 3, 6, 12, 24, 32, 64,
80, 96 and the performance is shown in Figure 4. The value
of loss function ﬂuctuates slightly. That is, even vectors with
low dimensions can still effectively represent the academic
performance of each student. Thus, we choose 3 as the di-
mension of representation for computational efﬁciency.
6.2
Prediction Results
We predict employment status with features including aca-
demic performance, gender, nation, enroll status, hometown
and their major. To verify the effectiveness of our MAYA
framework, we design prediction experiments including two
settings: comparison with LSTM-based MAYA’s variants
and comparison with representative baselines.


## Page 6


0 . 5
0 . 6
0 . 7
0 . 8
0 . 9
0 . 8 2
0 . 8 3
0 . 8 4
0 . 8 5
0 . 8 6
0 . 8 7
0 . 8 8
 M
A Y A
 X G B O O S T
 S V M
 G B D T
 R a n d o m  F o r e s t
A c c u r a c y
F r a c t i o n  o f  R a w  D a t a s e t  
0 . 5
0 . 6
0 . 7
0 . 8
0 . 9
0 . 4 6
0 . 4 8
0 . 5 0
0 . 5 2
 M
A Y A
 X G B O O S T
 S V M
 G B D T
 R a n d o m  F o r e s t
R e c a l l
F r a c t i o n  o f  R a w  D a t e s e t
0 . 5
0 . 6
0 . 7
0 . 8
0 . 9
0 . 4 6
0 . 4 8
0 . 5 0
0 . 5 2
 M
A Y A
 X G B O O S T
 S V M
 G B D T
 R a n d o m  F o r e s t
F 1 - s c o r e
F r a c t i o n  o f  R a w  D a t a s e t
Figure 5: Prediction performance on raw training dataset a.
0 . 6
0 . 7
0 . 8
0 . 9
1 . 0
0 . 8 5
0 . 8 6
0 . 8 7
0 . 8 8
 M
A Y A
 X G B O O S T
 S V M
 G B D T
 R a n d o m  F o r e s t
A c c u r a c y
F r a c t i o n  o f  T r a i n i n g  S e t  a '
0 . 6
0 . 7
0 . 8
0 . 9
1 . 0
0 . 6 0
0 . 6 3
0 . 6 6
0 . 6 9
0 . 7 2
0 . 7 5
0 . 7 8
 M
A Y A
 X G B O O S T
 S V M
 G B D T
 R a n d o m  F o r e s t
R e c a l l
F r a c t i o n  o f  T r a i n i n g  S e t  a '
0 . 6
0 . 7
0 . 8
0 . 9
1 . 0
0 . 6 3
0 . 6 6
0 . 6 9
0 . 7 2
0 . 7 5
0 . 7 8
0 . 8 1
0 . 8 4
 M
A Y A
 X G B O O S T
 S V M
 G B D T
 R a n d o m  F o r e s t
F 1 - s c o r e
F r a c t i o n  o f  T r a i n i n g  S e t  a '
Figure 6: Prediction performance on balanced training dataset a′.
Variants
Accuracy
Recall
F1-score
LSTM+Raw Data
0.862
0.500
0.463
LSTM+GAN
0.869
0.670
0.717
LSTM+Dropout
+GAN
0.876
0.712
0.761
LSTM+Dropout+
GAN+New Loss
0.880
0.766
0.810
Table 1: Prediction performance of MAYA variants.
Comparison with LSTM-based MAYA’s Variants
Table
1 displays the prediction performance of MAYA and its vari-
ants. We design a four-step experiment to test the perfor-
mance with metrics, i.e., accuracy, recall and F1-score, to
understand the results collectively.
In the ﬁrst step, we use raw data to ﬁt the LSTM algo-
rithm. The imbalance label issue exists in raw data, leading
to the occurrence of unexpected results on precision and re-
call. First, the algorithm could achieve a low loss value by
ignoring the minority class and predicting all the samples
into the majority class. It results in a recall with 0.5. Second,
the precision is relatively low because no samples are pre-
dicted as a minority. In other words, for the minority class,
the correct ratio of prediction results is 0.
In the second step, GAN is used to solve the label imbal-
ance and the data generation process is shown as follows:
• First, raw data is divided into two categories: training set
a and testing set b by stratiﬁed sampling.
• Second, we use GAN on the training set a to generate
samples of the minority class. Then in the new training
set a′, the number of students in the two classes is equal.
Then, we use the training set a′ to ﬁt the model and test
it on the original testing set b. The performance shown in
Table 1 veriﬁes its effectiveness.
In the third step, a new dropout mechanism of LSTM is
employed to alleviate the overﬁtting problem caused by the
relatively small experimental dataset. We add the dropout
mechanism based on the experiment of the second step. In
the ﬁnal step, we add the bias-based regularization into the
optimization loss based on the last step and the results sug-
gest its importance.
Comparison with Baseline Methods
In addition to the
comparison with deep learning-based variants, we com-
pare the MAYA framework with several popular algorithms
shown as follows:
• SVM (Scholkopf and Smola 2001): SVM is a classic al-
gorithm and is widely used in the ﬁeld of data mining.
• Random Forest (Breiman 2001): is a classic ensemble
algorithm that achieves good performance in various ap-
plications.
• GBDT (Friedman 2001): GBDT is an additive regression
model consisting of regression trees.
• XGBoost (Chen and Guestrin 2016): XGBoost is a
boosting-tree-based method and is widely used in various
data mining scenarios with good performance.
Note that, we test the performance of these algorithms
from two aspects. On one hand, we ﬁt algorithms based on
the raw training set a and test them on testing set b. The re-
sults are shown in Figure 5. It’s shown that the prediction is


## Page 7


0 . 1
0 . 2
0 . 3
0 . 4
0 . 5
0 . 6
0 . 7
0 . 8
0 . 9
0 . 6 6
0 . 7 2
0 . 7 8
0 . 8 4
0 . 9 0
0 . 9 6
 A c c u r a c y    
 P r e c i s i o n
 R e c a l l        
 F 1  s c o r e
D r o p o u t  R a t e
Figure 7: Performance of MAYA with different dropout pro-
portions.
Semester
Accuracy
Precision
Recall
F1
1
0.73469
0.60848
0.62668
0.61484
2
0.82287
0.71878
0.65398
0.67470
3
0.86666
0.92909
0.654762
0.69820
4
0.86758
0.92944
0.658824
0.70311
5
0.87631
0.93264
0.69898
0.74856
6
0.88073
0.93172
0.757463
0.80326
Table 2: Performance of MAYA with different numbers of
semesters.
not accurate and the ﬂuctuation is quite large due to the label
imbalance of raw data. To overcome this problem, we ﬁt al-
gorithms based on the balanced training set a′ and test them
on b. The results are shown in Figure 6. The performance is
improved signiﬁcantly.
6.3
Parameter Sensitivity
Dropout Proportions
As mentioned above, a dropout
mechanism is utilized to improve the generalization perfor-
mance and we test the sensitivity of MAYA framework on
dropout proportions (Figure 7). The change of dropout pro-
portions generates a slight impact and 0.3 is the best.
Input Features
It’s of great signiﬁcance to distinguish
early the students who might encounter difﬁculties in em-
ployment. Then teachers can intervene at an early stage.
Therefore, we conduct a test on the number of semesters
involved in academic performance data. As shown in Ta-
ble 2, prediction performance grows slowly since the fourth
semester. In other words, we can predict the students with
trouble in landing a job with high accuracy at the end of the
second year. We also design an experiment to test the ef-
fectiveness of demographic features and leave the results in
Supplemental Material.
Learning Rate
Learning rate that controls the update
speed of the model is an important parameter in the MAYA
framework. In Figure 8, we analyze the performance of var-
ious learning rates and ﬁnd that the model can achieve the
best prediction performance when the learning rate is set to
0.01.
0 . 0 0 0 1
0 . 0 0 1
0 . 0 5
0 . 0 1
0 . 1
0 . 7 2
0 . 7 6
0 . 8 0
0 . 8 4
0 . 8 8
0 . 9 2
0 . 9 6
L e a r n i n g  R a t e
 A c c u r a c y
 P r e c i s i o n
 R e c a l l
 F 1  s c o r e
Figure 8: Performance of MAYA with different learning
rates.
Optimization Function
Accuracy
Recall
F1-score
Eq.11
0.873
0.689
0.738
Eq.9
0.880
0.766
0.810
Table 3: Performance of Different Optimization.
Bias-based Regularization
We design an experiment to
test the effectiveness of bias based regularization. We use
Eq.11 and Eq.9 as loss function separately and the predic-
tion performance is shown in Table 3. The bias-based regu-
larization can improve the performance remarkably.
L1 = 1
2
M
X
m=1
(W xm
i −ym
i )2 + ||W ||2
F
(11)
7
Conclusion and Discussion
In this paper, we analyze a large-scale educational data for
predicting graduates’ employment status. For the reason that
bias cannot be ignored in employment, we analyze the em-
ployment bias of different majors ﬁrst of all and verify the
existence of employment bias. Then based on such bias,
MAYA, a prediction framework, is proposed in this paper
to predict graduates’ employment status. We incorporate
the autoencoder to ease the data-sparse issue and deal with
the imbalance label data using GAN. LSTM is combined
with dropout and a bias-based regularization to overcome
the over-ﬁtting problem and capture the impact of biases.
Our extensive experiments based on an education dataset
demonstrate the proposed framework can improve the pre-
diction performance signiﬁcantly and MAYA outperforms
other baselines like LSTM and XGBoost signiﬁcantly.
There are multiple directions for future work. Firstly, we
plan to expand our dataset and explore this issue from more
aspects. Secondly, we would conduct data acquisition from
various companies and further study this issue from the com-
pany’s perspective. Last but not least, we also intend to inte-
grate MAYA framework into the modern educational man-
agement system and apply it to detect the employment status
of graduating students.


## Page 8


References
[Al-Ubaydli and List 2019] Al-Ubaydli, O., and List, J. A.
2019. How natural ﬁeld experiments have enhanced our un-
derstanding of unemployment. Nature Human Behaviour
3(1):33–39.
[Billa 2018] Billa, J.
2018.
Dropout approaches for lstm
based speech recognition systems. In 2018 IEEE Interna-
tional Conference on Acoustics, Speech and Signal Process-
ing (ICASSP), 5879–5883. IEEE.
[Breiman 2001] Breiman, L. 2001. Random forests. Ma-
chine learning 45(1):5–32.
[Chen and Guestrin 2016] Chen, T., and Guestrin, C. 2016.
Xgboost: A scalable tree boosting system. In Proceedings of
the 22nd acm sigkdd international conference on knowledge
discovery and data mining, 785–794. ACM.
[Clauset, Arbesman, and Larremore 2015] Clauset,
A.;
Arbesman, S.; and Larremore, D. B.
2015.
Systematic
inequality and hierarchy in faculty hiring networks. Science
advances 1(1):e1400005.
[Drum et al. 2009] Drum, D. J.; Brownson, C.; Burton Den-
mark, A.; and Smith, S. E. 2009. New data on the nature
of suicidal crises in college students: Shifting the paradigm.
Professional Psychology: Research and Practice 40(3):213.
[Eurostat 2019] Eurostat. 2019. Employment rates of recent
graduates. https://ec.europa.eu/eurostat/statistics-explained/
index.php/Employment rates of recent graduates#
Employment rates of recent graduates.
[Ford et al. 2018] Ford, H. L.; Brick, C.; Blaufuss, K.; and
Dekens, P. S. 2018. Gender inequity in speaking opportuni-
ties at the american geophysical union fall meeting. Nature
communications 9(1):1358.
[Friedman 2001] Friedman, J. H. 2001. Greedy function ap-
proximation: a gradient boosting machine. Annals of statis-
tics 29(5):1189–1232.
[Gal and Ghahramani 2016] Gal, Y., and Ghahramani, Z.
2016. A theoretically grounded application of dropout in
recurrent neural networks. In Advances in neural informa-
tion processing systems, 1019–1027. Curran Associates Inc.
[Giannakas, Fulton, and Awada 2017] Giannakas, K.; Ful-
ton, M.; and Awada, T. 2017. Hiring leaders: Inference and
disagreement about the best person for the job. Palgrave
Communications 3(1):17.
[Goodfellow et al. 2014] Goodfellow, I.; Pouget-Abadie, J.;
Mirza, M.; Xu, B.; Warde-Farley, D.; Ozair, S.; Courville,
A.; and Bengio, Y. 2014. Generative adversarial nets. In
Advances in neural information processing systems, 2672–
2680.
[Kong et al. 2018] Kong, J.; Ren, M.; Lu, T.; and Wang, C.
2018. Analysis of college students employment, unemploy-
ment and enrollment with self-organizing maps. In Inter-
national Conference on E-Learning and Games, 318–321.
Springer.
[Liang, Hong, and Gu 2018] Liang, C.; Hong, Y.; and Gu, B.
2018. Home bias in hiring: Evidence from an online labor
market. In PACIS, 49.
[Liu et al. 2017] Liu, R.; Rong, W.; Ouyang, Y.; and Xiong,
Z. 2017. A hierarchical similarity based job recommenda-
tion service framework for university students. Frontiers of
Computer Science 11(5):912–922.
[Liu et al. 2018] Liu, J.; Kong, X.; Xia, F.; Bai, X.; Wang, L.;
Qing, Q.; and Lee, I. 2018. Artiﬁcial intelligence in the 21st
century. IEEE Access 6:34403–34421.
[Liu, Silver, and Bemis 2018] Liu, L.; Silver, D.; and Bemis,
K. 2018. Application-driven design: Help students under-
stand employment and see the big picture. IEEE computer
graphics and applications 38(3):90–105.
[Luo and Pardos 2018] Luo, Y., and Pardos, Z. A.
2018.
Diagnosing university student subject proﬁciency and pre-
dicting degree completion in vector space.
In Thirty-
Second AAAI Conference on Artiﬁcial Intelligence, 7920–
7927. AAAI Press.
[Moon et al. 2015] Moon, T.; Choi, H.; Lee, H.; and Song, I.
2015. Rnndrop: A novel dropout for rnns in asr. In 2015
IEEE Workshop on Automatic Speech Recognition and Un-
derstanding (ASRU), 65–70. IEEE.
[Pham et al. 2014] Pham, V.; Bluche, T.; Kermorvant, C.;
and Louradour, J. 2014. Dropout improves recurrent neural
networks for handwriting recognition. In 2014 14th Interna-
tional Conference on Frontiers in Handwriting Recognition,
285–290. IEEE.
[Scholkopf and Smola 2001] Scholkopf, B., and Smola, A. J.
2001. Learning with kernels: support vector machines, reg-
ularization, optimization, and beyond. MIT press.
[Soumya and Sugathan 2017] Soumya, M., and Sugathan, T.
2017.
Improve student placement using job competency
modeling and personalized feedback. In 2017 International
Conference on Advances in Computing, Communications
and Informatics (ICACCI), 1751–1755. IEEE.
[Srivastava et al. 2014] Srivastava,
N.;
Hinton,
G.;
Krizhevsky, A.; Sutskever, I.; and Salakhutdinov, R.
2014. Dropout: a simple way to prevent neural networks
from overﬁtting. The journal of machine learning research
15(1):1929–1958.
[Uosaki et al. 2018] Uosaki, N.; Mouri, K.; Yin, C.; and
Ogata, H.
2018.
Seamless support for international stu-
dents’ job hunting in japan using learning log system and
ebook.
In 2018 7th International Congress on Advanced
Applied Informatics (IIAI-AAI), 374–377. IEEE.
[Westefeld et al. 2005] Westefeld,
J.
S.;
Homaifar,
B.;
Spotts, J.; Furr, S.; Range, L.; and Werth, J. L.
2005.
Perceptions concerning college student suicide: Data from
four universities.
Suicide and Life-Threatening Behavior
35(6):640–645.
[Wu et al. 2013] Wu, X.; Zhu, X.; Wu, G.-Q.; and Ding, W.
2013. Data mining with big data. IEEE transactions on
knowledge and data engineering 26(1):97–107.
[Zaremba, Sutskever, and Vinyals 2014] Zaremba,
W.;
Sutskever, I.; and Vinyals, O.
2014.
Recurrent neural
network regularization. arXiv preprint arXiv:1409.2329.
[Zhu et al. 2016] Zhu, W.; Lan, C.; Xing, J.; Zeng, W.; Li, Y.;
Shen, L.; and Xie, X. 2016. Co-occurrence feature learning


## Page 9


for skeleton based action recognition using regularized deep
lstm networks. In Thirtieth AAAI Conference on Artiﬁcial
Intelligence, 3697–3703. AAAI Press.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
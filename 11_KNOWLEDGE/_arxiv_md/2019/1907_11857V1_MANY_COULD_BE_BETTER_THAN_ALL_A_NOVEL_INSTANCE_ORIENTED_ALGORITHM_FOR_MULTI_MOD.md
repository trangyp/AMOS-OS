---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1907.11857v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1907.11857v1_Many_could_be_better_than_all__A_novel_instance-oriented_algorithm_for_Multi-mod

> Source: 1907.11857v1_Many_could_be_better_than_all__A_novel_instance-oriented_algorithm_for_Multi-mod.pdf

> Pages: 6

---


## Page 1


MANY COULD BE BETTER THAN ALL: A NOVEL INSTANCE-ORIENTED ALGORITHM
FOR MULTI-MODAL MULTI-LABEL PROBLEM
Yi Zhang, Cheng Zeng, Hao Cheng, Chongjun Wang, Lei Zhang∗
National Key Laboratory for Novel Software Technology at Nanjing University
Nanjing University, Nanjing 210023, China
{mg1733091, njuzengc, chengh}@smail.nju.edu.cn, {chjwang, zhangl}@nju.edu.cn
ABSTRACT
With the emergence of diverse data collection techniques, ob-
jects in real applications can be represented as multi-modal
features. What’s more, objects may have multiple semantic
meanings. Multi-modal and Multi-label [1] (MMML) prob-
lem becomes a universal phenomenon. The quality of data
collected from different channels are inconsistent and some
of them may not beneﬁt for prediction. In real life, not all
the modalities are needed for prediction. As a result, we pro-
pose a novel instance-oriented Multi-modal Classiﬁer Chains
(MCC) algorithm for MMML problem, which can make con-
vince prediction with partial modalities. MCC extracts dif-
ferent modalities for different instances in the testing phase.
Extensive experiments are performed on one real-world herbs
dataset and two public datasets to validate our proposed al-
gorithm, which reveals that it may be better to extract many
instead of all of the modalities at hand.
Index Terms— multi-modal, multi-label, extraction cost
1. INTRODUCTION
In many natural scenarios, objects might be complicated with
multi-modal features and have multiple semantic meanings
simultaneously.
For one thing, data is collected from diverse channels
and exhibits heterogeneous properties: each of these domains
present different views of the same object, where each modal-
ity can have its own individual representation space and se-
mantic meanings. Such forms of data are known as multi-
modal data.
In a multi-modal setting, different modalities
are with various extraction cost. Previous researches, i.e., di-
mensionality reduction methods, generally assume that all the
multi-modal features of test instances have been already ex-
tracted without considering the extraction cost. While in prac-
tical applications, there is no aforehand multi-modal features
prepared, modality extraction need to be performed in the
testing phase at ﬁrst. While for the complex multi-modal data
collection nowadays, the heavy computation burden of feature
∗Corresponding author
extraction for different modalities has become the dominant
factor that hurts the efﬁciency.
For another, real-world objects might have multiple se-
mantic meanings. To account for the multiple semantic mean-
ings that one real-world object might have, one direct solution
is to assign a set of proper labels to the object to explicitly
express its semantics. In multi-label learning, each object is
associated with a set of labels instead of a single label. Previ-
ous researches, i.e., classiﬁer chains algorithm is a high-order
approach considering the relationship among labels, but it is
affected by the ordering speciﬁed by predicted labels.
To address all the above challenges, this paper intro-
duces a novel algorithm called Multi-modal Classiﬁer Chains
(MCC) inspired by Long Short-Term Memory (LSTM)
[2][3]. Information of previous selected modalities can be
considered as storing in memory cell.
The deep-learning
framework simultaneously generates next modality of fea-
tures and conducts the classiﬁcation according to the input
raw signals in a data-driven way, which could avoid some bi-
ases from feature engineering and reduce the mismatch be-
tween feature extraction and classiﬁer. The main contribu-
tions are:
• We propose a novel MCC algorithm considering not
only interrelation among different modalities, but also
relationship among different labels.
• MCC algorithm utilizes multi-modal information under
budget, which shows that MCC can make a convince
prediction with less average modality extraction cost.
The remainder of this paper is organized as follows. Section
2 introduces related work. Section 3 presents the proposed
MCC model. In section 4, empirical evaluations are given
to show the superiority of MCC. Finally, section 5 presents
conclusion and future work.
2. RELATED WORK
In this section, we brieﬂy present state-of-the-art methods in
multi-modal and multi-label [4] ﬁelds. As for modality ex-
traction in multi-modal learning, it is closely related to fea-
arXiv:1907.11857v1  [cs.LG]  27 Jul 2019


## Page 2


ture extraction [5]. Therefore, we brieﬂy review some related
work on these two aspects in this section.
Multi-label learning is a fundamental problem in machine
leaning with a wide range of applications.
In multi-label
learning, each instance is associated with multiple interde-
pendent labels. Binary Relevance (BR) [6] algorithm is the
most simple and efﬁcient solution of multi-label algorithms.
However, the effectiveness of the resulting approaches might
be suboptimal due to the ignorance of label correlations. To
tackle this problem, Classiﬁer Chains (CC) [7] was proposed
as a high-order approach to consider correlations between la-
bels. It is obviously that the performance of CC is seriously
affected by the training order of labels. To account for the
effect of ordering, Ensembles of Classiﬁers Chains (ECC) [7]
is an ensemble framework of CC, which can be built with n
random permutation instead of inducing one classiﬁer chain.
Entropy Chain Classiﬁer (ETCC) [8] extends CC by calcu-
lating the contribution between two labels using information
entropy theory while Latent Dirichlet Allocation Multi-Label
(LDAML) [9] exploiting global correlations among labels.
LDAML mainly solve the problem of large portion of sin-
gle label instance in some special multi-label datasets. Due to
high dimensionality of data , dimensionality reduction [10] or
feature extraction should be taken into consideration.
Originally, feature selection and dimensionality reduction
are generally used for reducing the cost of feature extraction.
[11] proposed regularized multilinear regression and selection
for automatically selecting a set of features while optimizing
prediction for high-dimensional data. Feature selection algo-
rithms do not alter the original representation of the variables,
but merely select part of them. Most of existing multi-label
feature selection algorithms either boil down to solving mul-
tiple single-label feature selection problems or directly make
use of imperfect labels. Therefore, they may not be able to
ﬁnd discriminative features that are shared by multiple labels.
To reduce the negative effects of imperfect label information
in ﬁnding label correlations, [12] decomposes the multi-label
information into a low-dimensional space and then employs
the reduced space to steer the feature selection process. Fur-
thermore, we always extract multiple features rather than sin-
gle feature for classiﬁcation, several adaptive decision meth-
ods for multi-modal feature extraction are proposed [13] [14].
To further reduce the number of features for testing, [15] pro-
poses a novel Discriminative Modal Pursuit (DMP) approach.
In this paper, taking both multi-label learning and feature
extraction into consideration, we propose MCC model with
an end-to-end approach [16] for MMML problem, which is
inspired by adaptive decision methods. Different from pre-
vious feature selection or dimensionality reduction methods,
MCC extracts different modalities for different instances and
different labels. Consequently, when presented with an un-
seen instance, we would extract the most informative and
cost-effective modalities for it. Empirical study shows the ef-
ﬁciency and effectiveness of MCC, which can achieve better
classiﬁcation performance with less average modalities.
3. METHODOLOGY
This section ﬁrst summarizes some formal symbols and def-
initions used throughout this paper, and then introduces the
formulation of the proposed MCC model. An overview of
our MCC algorithm is shown in Fig.1.
instance M
MCC
instance 1
instance 2
instance 3
Training Phase
Testing Phase
instance 1
instance 2
instance 3
modal 1
modal 2
modal  P
labels
instance N
Fig. 1. Diagrammatic illustration of MCC model. In the test-
ing phase, circles shadowed with red represent the features
used for categorization prediction.
3.1. Notation
In the following, bold character denotes vector (e.g., X).
The task of this paper is to learn a function h: X →
2Y from a training dataset with N data samples D
=
{(Xi, Yi)}N
i=1. The i-th instance (Xi, Yi) contains a feature
vector Xi ∈X and a label vector Yi ∈Y.
Xi = [X1
i , X2
i , . . . , XP
i ] ∈Rd1+d2+···+dP is a combi-
nation of all modalities and dm is the dimensionality of fea-
tures in m-th modality. Yi = [y1
i , y2
i , . . . , yL
i ] ∈{−1, 1}L
denotes the label vector of Xi. P is the number of modalities
and L is the number of labels.
Moreover, we deﬁne c = {c1, c2, . . . , cP } to represent
the extraction cost of P modalities. Modality extraction se-
quence of Xi is denoted as Si = {S1
i , S2
i , . . . , Sm
i }, m ∈
{1, 2, . . . , P}, m ≤P, where Sm
i
∈{1, 2, . . . , P} represents
m-th modality of features to extract of Xi and satisﬁes the
following condition: ∀m, n(m ̸= n) ∈{1, 2, . . . , P}, Sm
i
̸=
Sn
i . It is noteworthy that different instances not only cor-
respond to different extraction sequences but also may have
different length of modalities of features extraction sequence.
Furthermore, we deﬁne some notations used for testing phase.
Suppose there is a testing dataset with M data samples
T
= {(Xi, Yi)}M
i=1. We denote predicted labels of T as
Z = {Zi}M
i=1, in which Zi = (z1
i , z2
i , . . . , zL
i ) represents


## Page 3


all predicted labels of Xi in T and Zj = (zj
1, zj
2, . . . , zj
M)T
represents j-th predicted labels of all testing dataset.
3.2. MCC algorithm
On one hand, MMML is related to multi-label learning and
here we extend Classiﬁer Chains to deal with it. On the other
hand, each binary classiﬁcation problem in Classiﬁer Chains
can be transferred into multi-modal problem and this proce-
dure aims at making a convince prediction with less average
modality extraction cost.
3.2.1. Classiﬁer Chains
Considering correlation among labels, we extend Classiﬁer
Chains to deal with Multi-modal and Multi-label problem.
Classiﬁer Chains algorithm transforms the multi-label learn-
ing problem into a chain of binary classiﬁcation problems,
where subsequent binary classiﬁers in the chain is built upon
the predictions of preceding ones [4], thus to consider the full
relativity of the label hereby. The greatest challenge to CC is
how to form a recurrence relation chain τ. In this paper, we
propose a heuristic Gini index based Classiﬁer Chains algo-
rithm to specify τ.
First of all, we split the multi-label dataset into several
single-label datasets, i.e, for j-th label in {y1, y2, . . . , yL},
we rebuild dataset Dj = {(Xi, yj
i )}N
i=1 as j-th dataset of
single-label. Secondly, we calculate Gini index [17] of each
rebuilt single-label dataset Dj, (j = 1, 2, . . . , L).
Gini(Dj) =
|Y|
X
k=1
X
k̸=k′
pkpk′ = 1 −
|Y|
X
k=1
p2
k
(1)
where pk represents the probability of randomly choosing two
samples with same labels, pk′ represents the probability of
randomly choosing two samples with different labels and |Y|
represents number of labels in Dj.
And then we get predicted label chain τ = {τi}L
i=1, com-
posed of indexes of sorted {Gini(Di)}L
i=1 which is sorted in
descending order. For L class labels {y1, y2, . . . , yL}, we are
supposed to split the label set one by one according to τ and
then train L binary classiﬁers.
For the j-th label yτj, (j = 1, 2, . . . , L) in the ordered list
τ, a corresponding binary training dataset is reconstructed by
appending a set of labels preceding yτj
i to each instance Xi:
Dτj = {([Xi, xdτj
i ], yτj
i )}N
i=1
(2)
where xdτj
i
= (yτ1
i , . . . , yτj−1
i
) represents the binary as-
signment of those labels preceding yτj
i
on Xi (speciﬁcally
xdi,τ1 = ∅) and [Xi, xdτj
i ] represents concatenating vector
Xi and xdτj
i . We denote cl as extraction cost of xdτj
i . If
j > 1, we combine the new set xdτj
i
as a new modality in
Dτj. Moreover, each instance in Dτj is composed of P + 1
modalities of features and extraction cost needs to be updated
by appending cl to c. We denote the new extraction cost as c′
and c′ = [c, cl].
Meanwhile, a corresponding binary testing dataset is con-
structed by appending each instance with its relevance to
those labels preceding yτj:
Tτj = {([Xi, xtτj
i ], yτj
i )}M
i=1
(3)
where xtτj
i
= (zτ1
i , . . . , zτj−1
i
) represents the binary as-
signment of those labels preceding zτj
i
on Xi (speciﬁcally
xtτ1
i
= ∅) and [Xi, xtτj
i ] represents concatenating vector Xi
and xtτj
i . We denote cl as extraction cost of xtτj
i , which is
the same as extraction cost of xdτj
i . If j > 1, each instance
in Tτj is composed of P + 1 modalities of features and one
label yτj
i .
After that, we propose an efﬁcient Multi-modal Classi-
ﬁer Chains (MCC) algorithm, which will be introduced in the
following paragraph. By passing a combination of training
dataset Dτj and extraction cost c′ as parameters of MCC, we
get Zτj. The ﬁnal predicted labels of T is the concatenation
of Zτj, (j = 1, 2, . . . , L), i.e., Z = (Zτ1, Zτ2, . . . , ZτL)
3.2.2. Multi-modal Classiﬁer Chains
In order to induce a binary classiﬁer fl : X × {−1, 1} with
less average modality extraction cost and better performance
in MCC, we design Multi-modal Classiﬁer Chains (MCC) al-
gorithm which is inspired by LSTM. MCC extracts modali-
ties of features one by one until it’s able to make a conﬁdent
prediction. MCC algorithm extracts different modalities se-
quence with different length for difference instances, while
previous feature extraction method extract all modalities of
features and use the same features for all instances.
MCC adopts LSTM network to convert the variable X′
i ∈
X into a set of hidden representations Ht
i = [h1
i , h2
i , . . . , ht
i],
ht
i ∈Rh. Here, ˆ
XSt
i
i
= [ ˆ
X1
i , . . . , ˆ
Xm
i , . . . , ˆ
XP
i ] is an adap-
tation of Xi. In the t-th step, the modality to be extracted is
denoted as St
i. If m = St
i, ˆ
Xm
i
= XSt
i
i , 0 otherwise. For
example, if St
i = 3, ˆ
X3
i = [0, 0, X3
i , . . . , 0].
Similar to peephole LSTM, MCC has three gates as well
as two states: forget gate layer, input gate layer, cell state
layer, output gate layer, hidden state layer, listed as follows:
ft = σ([Wfc, Wfh, Wfx][Ct−1, ht−1, ˆ
Xt]T + bf)
it = σ([Wic, Wih, Wix][Ct−1, ht−1, ˆ
Xt]T + bi)
Ct = ft·Ct−1+it·tanh([Wch, Wcx][ht−1, ˆ
Xt]T +bC)
ot = σ([Woc, Woh, Wox][Ct, ht−1, ˆ
Xt]T + bo)
ht = ot · tanh(Ct)
Different from LSTM, MCC adds two full connections to
predict current label and next modality to be extracted. For
one thing, there is a full connection between hidden layer and
label prediction layer, with weight vector ˆ
W l. For another,
there is a full connection between hidden layer and modality
prediction layer, with weight vector ˆ
W m. Moreover, bias
vector are denoted as bl and bm respectively.


## Page 4


• Label prediction layer: This layer predicts label accord-
ing to a nonlinear softmax function f lj(.).
f lj(Ht
i ) = σ(Ht
i ˆ
Wl + bl)
(4)
• Modality prediction layer:
This layer predicts next
modality according to a linear function fmj(.) and se-
lects maximum as next modality to be extracted.
f mj(Ht
i ) = Ht
i ˆ
Wm + bm
(5)
We use FL
=
[fl1, fl2, . . . , flL] and FM
=
[fm1, fm2, . . . , fmL] to denote the label prediction function
set and modality prediction function set respectively.
Next, we design loss function composed of loss term and
regularization term for producing optimum and faster results.
Above all, we design loss of instance ˆ
Xi with St
i modality as
follows.
Lt
i = Ll(f lj(Ht
i ), yi) + Lm(f mj(Ht
i ), ˆ
Xt
i)
(6)
Here we adopt log loss for label prediction loss function
Ll and hinge loss for modality prediction loss function Lm,
where modality prediction is measured by distances to K
Nearest Neighbors [18].
Meanwhile, we add Ridge Regression (L2 norm) to the
overall loss function.
Ωt
i = || ˆ
Wm||2 + || ˆ
Wl||2 + ||c · f mj(Ht
i )||
(7)
where ||.|| represents L2 norm and c represents extraction cost
of each modality.
The loss term is the sum of loss in all instances at t-th
step. The overall loss function is as follows.
Lt =
N
X
i
(Lt
i + λ · Ωt
i)
(8)
where λ = 0.1 is trade-off between loss and regularization.
In order to optimize the aforementioned loss function Lt,
we adopt a novel pre-dimension learning rate method for gra-
dient descent called AdaDelta [19]. Here, we denote all the
parameters in Eq.8 as W = [ ˆ
W m, ˆ
W l, λ].
At t-th step, we start by computing gradient gt =
∂Lt
∂Wt
and accumulating decaying average of the squared gradients:
E[g2]t = ρE[g2]t−1 + (1 −ρ)g2
t
(9)
where ρ is a decay constant and ρ = 0.95.
The resulting parameter update is then:
△Wt = −
p
E[(△W )2]t−1 + ϵ
p
E[g2]t + ϵ
gt
(10)
where ϵ is a constant and ϵ = 1e−8.
Algorithm 1 The pseudo code of MCC algorithm
Input:
D ={(Xi, Yi)}N
i=1: Training dataset;
c ={ci}P
i=1: Extraction cost of P modalities;
Output:
FL : set of label prediction function
FM : set of modality prediction function
1: Calculate predicted label chain τ = {τi}L
i=1 with Eq.1
2: for j in τ do
3:
Construct Dτj with Eq.2
4:
while cnt < Niter, cnt++ do
5:
Initial E[g2]0 = E[△W 2]0 = 0
6:
Choose Nb samples in Dτj
7:
for i = 1 : Nb do
8:
for t = 1 : P do
9:
Select St
i with Eq.5 and calculate ˆ
XSt
i
i
10:
ˆct
i = ˆct
i + cSt
i
11:
if ˆct
i > Cth or at
i > Ath then
12:
break
13:
end if
14:
Calculate Lt with Eq.8
15:
Compute gradient gt = ∂Lt
∂Wt
16:
Accumulate gradient E[g2]t with Eq.9
17:
Compute Update △Wt with Eq.10
18:
Accumulate Updates E[△W 2]t with Eq.11
19:
Update Wt+1 = Wt + △Wt
20:
end for
21:
end for
22:
end while
23:
Update flj and fmj as in Eq.4 and Eq.5
24: end for
25: return FL, FM;
And then, we accumulate update:
E[△W 2]t = ρE[△W 2]t−1 + (1 −ρ)△W 2
t
(11)
The pseudo-code of MCC is summarized in Algorithm
1. Nb denotes batch size of training phase. Niter represents
maximum number of iterations. Cth represents the thresh-
old of cost. Ath represents the threshold of accuracy of the
predicted label. ˆct
i denotes the sum of extraction cost and at
i
denotes accuracy of current predicted label.
4. EXPERIMENT
4.1. Dataset Description
We manually collect one real-world Herbs dataset and adapt
two publicly available datasets including Emotions [20] and
Scene [6].
As for Herbs, there are 5 modalities with ex-
plicit modal partitions: channel tropism, symptom, function,
dosage and ﬂavor. As for Emotions and Scene, we divide the


## Page 5


features into different modalities according to information en-
tropy gain. The details are summarized in Table 1.
Table 1. Datasets description. N, L and P denote the num-
ber of instances, labels and modalities in each dataset, respec-
tively. D shows the dimensionality of each modality.
Datasets
N
L
P
D
Herbs
11104
29
5
[13, 653, 433, 768, 36]
Emotions
593
6
3
[32, 32, 8]
Scene
2407
6
6
[49, 49, 49, 49, 49, 49]
4.2. Experimental Settings
All the experiments are running on a machine with 3.2GHz
Inter Core i7 processor and 64GB main memory.
We compare MCC with four multi-label algorithms: BR,
CC, ECC, MLKNN[21] and one state-of-the-art multi-modal
algorithm: DMP[15]. For multi-label learner, all modalities
of a dataset are concatenated together as a single modal input.
For multi-modal method, we treat each label independently.
F-measure is one of the most popular metrics for eval-
uation of binary classiﬁcation[22]. To have a fair compari-
son, we employ three widely adopted standard metrics, i.e.,
Micro-average, Hamming-Loss, Subset-Accuracy[4]. In ad-
dition, we use Cost-average to measure the average modality
extraction cost. For the sake of convenience in the regulariza-
tion function computation, extraction cost of each modality
is set to 1.0 in the experiment. Furthermore, we set the cost
of new modality (predicted labels) to 0.1 to demonstrate its
superiority compared with DMP.
4.3. Experimental Results
For all these algorithms, we report the best results of the opti-
mal parameters in terms of classiﬁcation performance. Mean-
while, we perform 10-fold cross validation (CV) and take the
average value of the results in the end.
For one thing, table 2 shows the experimental results of
our proposed MCC algorithm as well as other ﬁve comparing
algorithms. It is obvious that MCC outperforms the other ﬁve
algorithms on all metrics. For another, as shown in table 3,
MCC uses less average modality extraction cost than DMP,
while other four multi-label algorithms use all the modalities.
5. CONCLUSION
Complex objects, i.e., the articles, the images, etc can al-
ways be represented with multi-modal and multi-label infor-
mation. However, the quality of modalities extracted from
Table 2. Comparison results (mean±std). ↑/ ↓indicates that
the larger/smaller the better of a criterion. The best perfor-
mance on each dataset is bolded.
Algorithm
Evaluation Metrics
Micro-
average↑
Hamming-
Loss↓
Subset-
Accuracy↑
Herbs
BR
0.621±0.061
0.033±0.004
0.349±0.060
CC
0.624±0.060
0.033±0.004
0.363±0.072
ECC
0.675±0.010
0.035±0.001
0.376±0.018
MLKNN
0.544±0.047
0.039±0.005
0.281±0.068
DMP
0.635±0.073
0.032±0.004
0.398±0.063
MCC
0.706±0.014
0.029±0.004
0.437±0.067
Emotions
BR
0.536±0.036
0.240±0.021
0.175±0.036
CC
0.541±0.034
0.240±0.022
0.184±0.037
ECC
0.647±0.038
0.202±0.023
0.283±0.042
MLKNN
0.529±0.030
0.278±0.022
0.212±0.038
DMP
0.607±0.072
0.206±0.023
0.253±0.061
MCC
0.659±0.081
0.190±0.023
0.292±0.084
Scene
BR
0.672±0.140
0.098±0.037
0.552±0.160
CC
0.678±0.119
0.109±0.041
0.624±0.117
ECC
0.705±0.015
0.094±0.005
0.596±0.016
MLKNN
0.660±0.114
0.113±0.033
0.553±0.112
DMP
0.815±0.077
0.061±0.020
0.704±0.118
MCC
0.842±0.040
0.057±0.015
0.738±0.082
Table 3. Comparison results of the average modality extrac-
tion cost, the smaller the better. OTHERS denotes BR, CC,
ECC and MLKNN algorithms. The best performance on each
dataset is bolded.
Algorithm
Herbs
Emotions
Scene
OTHERS
5.0±0.0
3.0±0.0
6.0±0.0
DMP
3.031±0.258
1.738±0.279
3.202±0.432
MCC
2.520±0.182
1.519±0.313
2.109±0.324
various channels are inconsistent. Using data from all modal-
ities is not a wise decision. In this paper, we propose a novel
Multi-modal Classiﬁer Chains (MCC) algorithm to improve
supplements categorization prediction for MMML problem.
Experiments in one real-world dataset and two public datasets
validate the effectiveness of our algorithm. MCC makes great
use of modalities, which can make a convince prediction with
many instead of all modalities. Consequently, MCC reduces
modality extraction cost, but it has the limitation of time-
consuming compared with other algorithms.
In the future
work, how to improve extraction parallelism is a very inter-
esting work.


## Page 6


6. ACKNOWLEDGEMENT
This paper is supported by the National Key Research and De-
velopment Program of China (Grant No. 2016YFB1001102),
the National Natural Science Foundation of China (Grant
No. 61876080), the Collaborative Innovation Center of Novel
Software Technology and Industrialization at Nanjing Univer-
sity.
7. REFERENCES
[1] Han-Jia Ye, De-Chuan Zhan, Xiaolin Li, Zhen-Chuan
Huang, and Yuan Jiang, “College student scholarships
and subsidies granting: A multi-modal multi-label ap-
proach,” in Data Mining (ICDM), 2016 IEEE 16th In-
ternational Conference on. IEEE, 2016, pp. 559–568.
[2] Alex Graves and J¨urgen Schmidhuber,
“Framewise
phoneme classiﬁcation with bidirectional lstm and other
neural network architectures,” Neural Networks, vol. 18,
no. 5-6, pp. 602–610, 2005.
[3] R Bertolami, H Bunke, S Fernandez, A Graves, M Li-
wicki, and J Schmidhuber, “A novel connectionist sys-
tem for improved unconstrained handwriting recogni-
tion,” IEEE Transactions on Pattern Analysis and Ma-
chine Intelligence, vol. 31, no. 5, 2009.
[4] Min-Ling Zhang and Zhi-Hua Zhou,
“A review on
multi-label learning algorithms,” IEEE transactions on
knowledge and data engineering, vol. 26, no. 8, pp.
1819–1837, 2014.
[5] Yvan Saeys, I˜naki Inza, and Pedro Larra˜naga, “A re-
view of feature selection techniques in bioinformatics,”
bioinformatics, vol. 23, no. 19, pp. 2507–2517, 2007.
[6] Matthew R Boutell, Jiebo Luo, Xipeng Shen, and
Christopher M Brown, “Learning multi-label scene clas-
siﬁcation,” Pattern recognition, vol. 37, no. 9, pp. 1757–
1771, 2004.
[7] Jesse Read, Bernhard Pfahringer, Geoff Holmes, and
Eibe Frank, “Classiﬁer chains for multi-label classiﬁ-
cation,” Machine learning, vol. 85, no. 3, pp. 333, 2011.
[8] Yue Peng, Ming Fang, Chongjun Wang, and Junyuan
Xie,
“Entropy chain multi-label classiﬁers for tradi-
tional medicine diagnosing parkinson’s disease,”
in
Bioinformatics and Biomedicine (BIBM), 2015 IEEE In-
ternational Conference on. IEEE, 2015, pp. 856–862.
[9] Yue Peng, Chi Tang, Gang Chen, Junyuan Xie, and
Chongjun Wang, “Multi-label learning by exploiting la-
bel correlations for tcm diagnosing parkinson’s disease,”
in Bioinformatics and Biomedicine (BIBM), 2017 IEEE
International Conference on. IEEE, 2017, pp. 590–594.
[10] Sam T Roweis and Lawrence K Saul, “Nonlinear di-
mensionality reduction by locally linear embedding,”
science, vol. 290, no. 5500, pp. 2323–2326, 2000.
[11] Xiaonan Song and Haiping Lu, “Multilinear regression
for embedded feature selection with application to fmri
analysis.,” in AAAI, 2017, pp. 2562–2568.
[12] Ling Jian, Jundong Li, Kai Shu, and Huan Liu, “Multi-
label informed feature selection.,” in IJCAI, 2016, pp.
1627–1633.
[13] Joseph Wang,
Kirill Trapeznikov,
and Venkatesh
Saligrama, “An lp for sequential learning under bud-
gets,” in Artiﬁcial Intelligence and Statistics, 2014, pp.
987–995.
[14] Joseph Wang,
Kirill Trapeznikov,
and Venkatesh
Saligrama,
“Efﬁcient learning by directed acyclic
graph for resource constrained prediction,” in Advances
in Neural Information Processing Systems, 2015, pp.
2152–2160.
[15] Yang Yang, De-Chuan Zhan, Ying Fan, and Yuan Jiang,
“Instance speciﬁc discriminative modal pursuit: A se-
rialized approach,”
in Asian Conference on Machine
Learning, 2017, pp. 65–80.
[16] Wei Li, Zheng Yang, and Xu Sun, “Exploration on gen-
erating traditional chinese medicine prescription from
symptoms with an end-to-end method,” arXiv preprint
arXiv:1801.09030, 2018.
[17] Leo Breiman, Classiﬁcation and regression trees, Rout-
ledge, 2017.
[18] Shemim Begum, Debasis Chakraborty, and Ram Sarkar,
“Data classiﬁcation using feature selection and knn ma-
chine learning approach,” in Computational Intelligence
and Communication Networks (CICN), 2015 Interna-
tional Conference on. IEEE, 2015, pp. 811–814.
[19] Matthew D Zeiler, “Adadelta: an adaptive learning rate
method,” arXiv preprint arXiv:1212.5701, 2012.
[20] Konstantinos Trohidis, Grigorios Tsoumakas, George
Kalliris, and Ioannis P Vlahavas, “Multi-label classiﬁ-
cation of music into emotions.,” in ISMIR, 2008, vol. 8,
pp. 325–330.
[21] Min-Ling Zhang and Zhi-Hua Zhou,
“Ml-knn:
A
lazy learning approach to multi-label learning,” Pattern
recognition, vol. 40, no. 7, pp. 2038–2048, 2007.
[22] Krzysztof Dembczynski, Arkadiusz Jachnik, Wojciech
Kotlowski, Willem Waegeman, and Eyke H¨ullermeier,
“Optimizing the f-measure in multi-label classiﬁcation:
Plug-in rule approach versus structured loss minimiza-
tion,” in International Conference on Machine Learn-
ing, 2013, pp. 1130–1138.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
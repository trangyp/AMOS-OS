---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1610.06987v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1610.06987v1_Multitask_Learning_of_Vegetation_Biochemistry_from_Hyperspectral_Data

> Source: 1610.06987v1_Multitask_Learning_of_Vegetation_Biochemistry_from_Hyperspectral_Data.pdf

> Pages: 5

---


## Page 1


MULTITASK LEARNING OF VEGETATION BIOCHEMISTRY FROM HYPERSPECTRAL
DATA
Utsav B. Gewali 1 and Sildomar T. Monteiro 1,2
1Chester F. Carlson Center for Imaging Science
2Department of Electrical Engineering
Rochester Institute of Technology, Rochester, NY
ubg9540@rit.edu
ABSTRACT
Statistical models have been successful in accurately
estimating the biochemical contents of vegetation from
the reﬂectance spectra. However, their performance de-
teriorates when there is a scarcity of sizable amount of
ground truth data for modeling the complex non-linear
relationship occurring between the spectrum and the
biochemical quantity.
We propose a novel Gaussian
process based multitask learning method for improv-
ing the prediction of a biochemical through the transfer
of knowledge from the learned models for predicting
related biochemicals.
This method is most advanta-
geous when there are few ground truth data for the
biochemical of interest, but plenty of ground truth data
for related biochemicals. The proposed multitask Gaus-
sian process hypothesizes that the inter-relationship
between the biochemical quantities is better modeled
by using a combination of two or more covariance func-
tions and inter-task correlation matrices. In the experi-
ments, our method outperformed the current methods
on two real-world datasets.
Index Terms— Biochemistry prediction, Hyperspec-
tral data, Gaussian processes, Multitask learning
1. INTRODUCTION
Biochemistry prediction is the problem of estimating
the contents of chemicals in vegetation from the mea-
sured reﬂectance spectrum. The presence of a certain
chemical is manifested in the reﬂectance spectra as spec-
tral absorption features, and the depth of the spectral
feature is correlated to the contents of that chemical. It
is, hence, possible to develop regression models to pre-
dict the contents of biochemicals from the reﬂectance
spectrum [1]. Recently, Gaussian processes have been
successfully applied for this purpose [2, 3, 4].
Gaus-
sian processes, being non-parametric, can model the
complex non-linear relationship that exists between the
spectrum and the biochemical quantity very well. But,
similar to other statistical models used for biochem-
istry prediction [5], they suffer in performance due to
insufﬁcient availability of training examples.
Biochemistry prediction datasets commonly have
very few ground truth data, due to the difﬁculties in the
collection and the cost of chemical analysis of the vege-
tation samples. Moreover, many times, a single dataset
may have few ground truth for a biochemical, while
having plenty ground truth for other biochemicals. In
this case, the task of predicting the contents of a bio-
chemical may signiﬁcantly beneﬁt from the information
learned from the task of predicting the contents of other
related biochemicals.
Multitask learning is the idea
of learning a set of related tasks simultaneously such
that the inter-relationship between the tasks can be ex-
ploited to improve the performance of each task. It is
called transfer learning when the objective is to improve
the performance of only a subset of tasks. Transfer and
multitask learning have seen successful applications in
many domains such as natural language processing [6],
computer vision [7] and biomedical engineering [8].
In this paper, we propose a novel multitask Gaussian
process, inspired by [9], with the motivation of improv-
ing the predictive performance of a biochemical, for
which few training examples are available, using the
information from related biochemicals.
We evaluate our method with experiments on two
real world datasets, and compare the results with the
results from two state-of-the-art Gaussian process based
multitask methods [9, 10]. In [9], a task correlation ma-
trix, learned from the data itself, is used to deﬁne a
shared covariance representation over the tasks. Our
method extends [9] by using a combination of several
task correlation matrices and covariance functions, in-
stead of using a single task correlation matrix and a
single covariance function, to model the covariance
between the tasks. We postulate that our formulation
gives the model more ﬂexibility to learn the relation-
arXiv:1610.06987v1  [cs.CV]  22 Oct 2016


## Page 2


ships between the tasks, and hence improves the pre-
diction. The second method [10] is similar to [9], except
for that it also models a noise correlation matrix be-
tween the tasks. Modeling noise correlation helps to
account for hidden sources effecting the tasks that are
not included in the input. Our method could also be ex-
tended to include correlated noise. This paper is orga-
nized as follows. Section 2 provides a brief background
on Gaussian process regression, Section 3 introduces
the proposed method, Section 4 provides the evaluation
of the proposed method on real datasets, and Section 5
discusses the implications of this study.
2. GAUSSIAN PROCESSES FOR REGRESSION
Gaussian process (GP) regression is a probabilistic
model where the output variable values at all the train-
ing and the testing data points are considered to be
samples of a joint multivariate normal distribution,
having the mean vector zero and the covariance matrix
given by a covariance function [11]. Inference about
the posterior distribution of the output values at the
test data points, which is also a multivariate normal
distribution, is made by conditioning the joint normal
distribution by the output values at the training points,
and is given by
f∗|X, y, X∗∼N ( ¯f∗, cov( f∗)),
(1)
where
¯f∗=K(X∗, X) [K(X, X) + σ2
nI]
−1y,
(2)
cov( f∗) =K(X∗, X∗)−
K(X∗, X)[K(X, X) + σ2
nI]
−1K(X, X∗),
(3)
and f∗is a vector of output values at the test data
points stored in the rows of the matrix X∗, and y is a
vector of observed output values at the training data
points stored in the rows of the matrix X. σn is the in-
dependent and identically distributed Gaussian noise
variance observed at the output, and K(X, X′) is a co-
variance matrix whose i-th row and j-th column element
is the k(x, x′) of i-th row of X and j-th row of X′. k(x, x′)
is a covariance function. It is usually parameterized by
few free hyperparameters, which are learned from the
data, along with σn, by maximizing the log marginal
likelihood function of the GP.
3. MULTITASK LEARNING WITH COMPOSITE
COVARIANCE FUNCTION
We propose a new method to extend the method by
Bonilla et al. [9] and call it multitask learning with com-
posite covariance function (MTGP-COMP). In [9], the
relationship between the tasks is modeled with a single
inter-task correlation matrix. We extend this by model-
ing the inter-task covariance by the sum of a set of co-
variance functions, weighted by a set of inter-task cor-
relation matrices. The rationale behind our method is
that by using a set of covariance functions and inter-
task correlation matrices, more free parameters are in-
troduced in the model and, subsequently, the model be-
comes more expressive and can better learn the complex
relationship between the biochemicals and the spectra.
Let X = (x1, ..., xN)T be the N distinct inputs, YN×M
be the corresponding M task to learn and y = vec(Y) =
(y11, ..., yN1..., y1M, ..., yNM)T such that yil is the output
of xi on lth task. The inter-task covariance is deﬁned as

fl(xi), fk(xj)

=
P f
l,k kx
1(xi, xj) + Q f
l,k kx
2(xi, xj),(4)
where P f and Q f are the M × M positive semi-
deﬁnite task correlation matrices for the two covariance
functions k1(x, x′) and k2(x, x′), respectively. The (l, k)th
element of P f and Q f represent the correlation between
the lth and the kth tasks relating to the covariance func-
tions respectively. Then, the output is modeled as
yil
=
N ( fl(xi), σ2
l ),
(5)
where σ2
l is the noise variance in task l.
3.1. Inference and learning hyperparameters
The standard Gaussian process formulation can be used
to make inference on this model [11]. The mean of the
predictive distribution at point x∗for the lth task, ¯fl(x∗),
is given by
¯fl(x∗)
=
(p f
l ⊗kx
1∗+ q f
l ⊗kx
2∗)
T
Σ-1y,
(6)
where
Σ
=
P f ⊗Kx
1 + Q f ⊗Kx
2 + D ⊗I
(7)
and, p f
l and q f
l are the lth row or column of P f and
Q f respectively. kx
1∗and kx
2∗are the vectors of covari-
ances between the point and the training points using
two covariance functions respectively. Kx
1 and Kx
2 are
the MN × MN matrices of covariance between all pairs
of training points using two covariance functions re-
spectively. D is a M × M matrix with noise variance in
each task l as its lth diagonal element and I is a N × N
identity matrix.
The matrices P f and Q f should be constrained to
be positive semi-deﬁnite. For this purpose, similar to
in [10], each correlation matrix can be modeled as a2
0 +
∑k
i=1 bT
i bi, where k is the rank of the correlation matrix,


## Page 3


a is a scalar and bi for i = 1...k are column vectors of
length equal to the dimension of the correlation matrix.
The rank, k, is manually set, while a and bi are learned,
along with the hyperparameters of kx
1∗and kx
2∗, by min-
imizing the negative log likelihood
log(y|X) = −1
2yTΣ-1y −1
2 log |Σ| −NM
2
log(2π). (8)
Extending this formulation to include more than
two covariance functions to make the relationship be-
tween the task more ﬂexible, or to have correlated noise,
as in [10], is straightforward. However, with addition
of every new covariance funtion or addition of corre-
lated noise, more parameters have to be learned and
more covariance matrices need to be computated. This
could lead to over-ﬁtting of the parameters and in-
creased computational overhead. Hence, in this paper
as a proof-of-concept, we focus on the case with two
covariance functions with uncorrelated noise.
4. EXPERIMENTS
We present experiments using two datasets. We exam-
ine the common situation where it is harder or more
expensive to obtain analysis about some biochemical
quantities, leading to the datasets having few ground
truth for some quantities while having plenty ground
truth for other quantities. The methods compared are
multitask learning with composite covariance function
(MTGP-COMP), multitask learning with shared covari-
ance (MTGP-SC) [9], multitask learning with structured
noise (MTGP-SN) [10] and single-task Gaussian Process
(GP).
4.1. Datasets
The ﬁrst dataset contains 103 reﬂectance spectra of sed-
iments containing algal bio-ﬁlms, and the contents of
the chlorophyll-a and the chlorophyll-b in µg cm−2.
The dataset was acquired by Murphy et al. [12] from
two mudﬂats, each of an area about 500 m2, in Syd-
ney, Australia. The reﬂectance spectra is measured in
visible and near infrared region (350-1050 nm at 1 nm
interval).
The second dataset contains 54 reﬂectance
spectra of foliage and the corresponding nitrogen and
carbon contents of the samples, measured in terms of
percentage dry foliage weight, collected as part of a
ﬁeld campaign by The National Ecological Observatory
Network (NEON)1. It contains visible to shortwave in-
frared spectra (350-2050 nm at 1 nm interval). It also
1National Ecological Observatory Network. 2015. Available on-
line http://data.neoninc.org/ from National Ecological Observatory
Network, Boulder, CO, USA.
contains an airborne hyperspectral image of a 250 m ×
250 m test area.
4.2. Methodology
Out of the two biochemical quantities in each dataset,
one was chosen to be the primary quantity and the other
to be the secondary quantity (similar to [13, 14]). We as-
sume that there are few training examples for the pri-
mary quantities while a large number of training exam-
ples for the secondary quantities. We evaluate the ef-
ﬁcacy of the multitask method by estimating the miss-
ing values of the primary quantities of the samples for
which the values of the secondary quantities are avail-
able. We repeat the same process by making the pri-
mary quantity in the ﬁrst step as the secondary quan-
tity and the secondary quantity in the ﬁrst step as the
primary quantity.
The examples in the datasets were randomly sepa-
rated into the training and the test sets. The test set con-
tained one-third of the ground truth instances of the pri-
mary quantity. All the instances of the secondary quan-
tity and the remaining two-third instances of the pri-
mary quantity were included in the training set. Eighty
percent of the training set was used to train models with
different rank approximations of the correlation matri-
ces in the multitask models. Hyperparameters of the
covariance functions and the correlation matrices were
learned by minimizing the log likelihood using quasi-
Newton method. Five trials of this optimization were
performed using random initial guesses to prevent local
minima. The ranks of the correlation matrices and the
hyperparameters that produced the best r2 in predicting
the remaining twenty percent of the training examples
were chosen as ﬁnal correlation matrix ranks and hy-
perparameters. Using them, predictions were made on
the testing set and the performance was measured by r2
value. This procedure was repeated for 50 independent
trials, and the mean and the standard deviation of the
measured r2 value are reported.
4.3. Results
Table 1 summarizes the results of the experiment on
both the datasets. The covariance functions used with
each method is given in the parenthesis alongside
method’s name. All the covariance functions used were
isotropic.
SE stands for the squared exponential co-
variance function, NN stands for the neural network
covariance function and SUM stands for the sum co-
variance function formed by summing the squared
exponential and the neural network covariance func-
tions. Both squared exponential (SE) and neural net-
work (NN) covariance functions were used with the


## Page 4


Table 1: Performance measured by the mean and the standard deviation of the predictive r2 over 50 independent
trials.
Method
Chlorophyll-a
Chlorophyll-b
Nitrogen
Carbon
GP (SE)
0.5972 (±0.112)
0.4986 (±0.136)
0.4515 (±0.201)
0.4535 (±0.162)
GP (NN)
0.6405 (±0.114)
0.5329 (±0.129)
0.5331 (±0.132)
0.5162 (±0.168)
GP (SUM)
0.6238 (±0.115)
0.5203 (±0.133)
0.5166 (±0.132)
0.5192 (±0.164)
MTGP-SC (SE)
0.6284 (±0.079)
0.5805 (±0.119)
0.5833 (±0.130)
0.5518 (±0.150)
MTGP-SC (NN)
0.6263 (±0.093)
0.5763 (±0.118)
0.6283 (±0.112)
0.6015 (±0.151)
MTGP-SC (SUM)
0.6591 (±0.109)
0.6343 (±0.146)
0.6686 (±0.124)
0.6231 (±0.153)
MTGP-SN (SE)
0.6427 (±0.083)
0.5474 (±0.133)
0.4621 (±0.148)
0.5021 (±0.140)
MTGP-SN (NN)
0.6430 (±0.098)
0.5803 (±0.151)
0.5895 (±0.131)
0.5927 (±0.155)
MTGP-SN (SUM)
0.6796 (±0.100)
0.6575 (±0.147)
0.6629 (±0.109)
0.6000 (±0.160)
MTGP-COMP (SE, NN)*
0.6869 (±0.116)
0.6177 (±0.142)
0.7262 (±0.107)
0.6569 (±0.142)
*proposed method.
proposed method (MTGP-COMP). For illustration, ﬁg.
1 shows the nitrogen and the carbon contents predic-
tion map generated from the test hyperspectral image
by the MTGP-COMP model (one out of the 50 trials).
As pre-processing, the water absorption bands were
removed and the sampling wavelengths of the ground
spectra and the image spectra were matched using lin-
ear interpolation.
Non-vegetation pixels (pixels with
Normalized Difference Vegetation Index less than 0.3)
have been masked out.
5. DISCUSSION
The proposed method presented the best result for three
out of four biochemicals. This demonstrates that using
a combination of covariance functions and task correla-
tion matrices can produce more ﬂexible models yielding
more accurate results, compared to the previous multi-
task methods. Also, all multitask methods performed
better than the single-task GP for all biochemicals, con-
ﬁrming the hypothesis that multitask learning improves
the biochemical content prediction when few training
data are available.
The difference in the mean r2 of
the single task GP and the proposed method is quite
signiﬁcant.
However, the standard deviation of r2 is
fairly large for all the methods. It is probably due to
the limited number of training examples. The standard
deviation of r2 is consistent between all the methods,
indicating that the mean r2 value is good representa-
tive of the trend in the performance. The learning in
the current implementation of the proposed method is
slow and not scalable to cases where there are multiple
secondary quantities. As future work, sparse Gaussian
processes [15] could be used with the proposed method
to reduce the computational complexity.
(a) RGB Image
(b)
Predicted
Nitrogen
Contents
(%
leaf
weight)
(c) Predicted Carbon Contents (% leaf weight)
Fig. 1: The proposed method applied to a 250 m × 250 m
airborne hyperspectral image.


## Page 5


6. REFERENCES
[1] R. F. Kokaly and R. N. Clark, “Spectroscopic de-
termination of leaf biochemistry using band-depth
analysis of absorption features and stepwise mul-
tiple linear regression,” Remote sensing of environ-
ment, vol. 67, no. 3, pp. 267–287, 1999.
[2] G. Camps-Valls, L. Gomez-Chova, J. Muoz-Mari,
J. Vila-Frances, J. Amoros, S. del Valle-Tascon, and
J. Calpe-Maravilla, “Biophysical parameter estima-
tion with adaptive Gaussian processes,” in IEEE
International Geoscience and Remote Sensing Sympo-
sium (IGARSS), July 2009, vol. 4, pp. 69–72.
[3] J. Verrelst, L. Alonso, G. Camps-Valls, J. Delegido,
and J. Moreno, “Retrieval of vegetation biophysical
parameters using Gaussian process techniques,” in
IEEE Transactions on Geoscience and Remote Sensing,
May 2012, vol. 50, pp. 1832–1843.
[4] J. Verrelst, L. Alonso, J.P.R. Caicedo, J. Moreno,
and G. Camps-Valls, “Gaussian process retrieval
of chlorophyll content from imaging spectroscopy
data,” IEEE Journal of Selected Topics in Applied Earth
Observations and Remote Sensing, vol. 6, no. 2, pp.
867–874, April 2013.
[5] Y. Bazi and F. Melgani, “Semisupervised PSO-SVM
regression for biophysical parameter estimation,”
IEEE Transactions on Geoscience and Remote Sensing,
vol. 45, no. 6, pp. 1887–1895, June 2007.
[6] S. J. Pan and Q. Yang, “A survey on transfer learn-
ing,” IEEE Transactions on Knowledge and Data En-
gineering, vol. 22, no. 10, pp. 1345–1359, Oct 2010.
[7] M. Lapin, B. Schiele, and M. Hein, “Scalable mul-
titask representation learning for scene classiﬁca-
tion,”
in IEEE Conference on Computer Vision and
Pattern Recognition (CVPR), June 2014, pp. 1434–
1441.
[8] Q. Xu, S. J. Pan, H. H. Xue, and Q. Yang, “Mul-
titask learning for protein subcellular location pre-
diction,” IEEE/ACM Trans. Comput. Biol. Bioinfor-
matics, vol. 8, no. 3, pp. 748–759, May 2011.
[9] E. Bonilla, K. M. Chai, and C. Williams, “Multi-task
Gaussian process prediction,” Advances in Neural
Information Processing Systems (NIPS), pp. 153–160,
2008.
[10] B. Rakitsch, C. Lippert, K. Borgwardt, and O. Ste-
gle, “It is all in the noise: Efﬁcient multi-task Gaus-
sian process inference with structured residuals,”
Advances in Neural Information Processing Systems
(NIPS), pp. 1466–1474, 2013.
[11] C. E. Rasmussen and C. Williams,
Gaussian Pro-
cesses for Machine Learning, The MIT Press, 2005.
[12] R. J. Murphy, T. J. Tolhurst, M. G. Chapman,
and A. J. Underwood,
“Estimation of surface
chlorophyll-a on an emersed mudﬂat using ﬁeld
spectrometry: accuracy of ratios and derivative-
based approaches,” International Journal of Remote
Sensing, vol. 26, no. 9, pp. 1835–1859, 2005.
[13] M. Schneider and F. Ramos, “Transductive learn-
ing for multi-task copula processes,” in European
Conference on Artiﬁcial Intelligence (ECAI), 2014, pp.
1089–1090.
[14] M. Alvarez and N. D. Lawrence,
“Sparse con-
volved gaussian processes for multi-output regres-
sion,” in Advances in neural information processing
systems (NIPS), 2009, pp. 57–64.
[15] E. Snelson and Z. Ghahramani, “Sparse gaussian
processes using pseudo-inputs,” Advances in Neu-
ral Information Processing Systems (NIPS), pp. 1257–
1264, 2005.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
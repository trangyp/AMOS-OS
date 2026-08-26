---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1907.00782v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1907.00782v1_Collecting_and_Analyzing_Multidimensional_Data_with_Local_Differential_Privacy

> Source: 1907.00782v1_Collecting_and_Analyzing_Multidimensional_Data_with_Local_Differential_Privacy.pdf

> Pages: 12

---


## Page 1


This full paper appears in the Proceedings of the IEEE 35th Annual International Conference on Data Engineering (ICDE),
held in April 2019.
Collecting and Analyzing Multidimensional Data
with Local Differential Privacy
Ning Wang1, Xiaokui Xiao2, Yin Yang3, Jun Zhao4, Siu Cheung Hui4, Hyejin Shin5, Junbum Shin5, Ge Yu6
1School of Information Science and Engineering, Ocean University of China
2School of Computing, National University of Singapore, Singapore
3Division of Information and Computing Techologies, College of Science and Engineering, Hamad Bin Khalifa University, Qatar
4School of Computer Science and Engineering, Nanyang Technological University, Singapore
5Samsung Research, Samsung Electronics, Korea
6School of Computer Science and Engineering, Northeastern University, China
1wangning8687@ouc.edu.cn,
2xkxiao@nus.edu.sg,
3yyang@hbku.edu.qa,
4{junzhao, asschui}@ntu.edu.sg,
5{hyejin1.shin, junbum.shin}@samsung.com,
6yuge@mail.neu.edu.cn
Abstract—Local differential privacy (LDP) is a recently pro-
posed privacy standard for collecting and analyzing data, which
has been used, e.g., in the Chrome browser, iOS and macOS. In
LDP, each user perturbs her information locally, and only sends
the randomized version to an aggregator who performs analyses,
which protects both the users and the aggregator against private
information leaks. Although LDP has attracted much research
attention in recent years, the majority of existing work focuses
on applying LDP to complex data and/or analysis tasks. In this
paper, we point out that the fundamental problem of collecting
multidimensional data under LDP has not been addressed
sufﬁciently, and there remains much room for improvement
even for basic tasks such as computing the mean value over
a single numeric attribute under LDP. Motivated by this, we
ﬁrst propose novel LDP mechanisms for collecting a numeric
attribute, whose accuracy is at least no worse (and usually better)
than existing solutions in terms of worst-case noise variance.
Then, we extend these mechanisms to multidimensional data
that can contain both numeric and categorical attributes, where
our mechanisms always outperform existing solutions regarding
worst-case noise variance. As a case study, we apply our solutions
to build an LDP-compliant stochastic gradient descent algorithm
(SGD), which powers many important machine learning tasks.
Experiments using real datasets conﬁrm the effectiveness of our
methods, and their advantages over existing solutions.
Index Terms—Local differential privacy, multidimensional
data, stochastic gradient descent.
I. INTRODUCTION
Local differential privacy (LDP), which has been used in
well-known systems such as Google Chrome [18], Apple iOS
and macOS [36], and Microsoft Windows Insiders [12], is a
rigorous privacy protection scheme for collecting and analyz-
ing sensitive data from individual users. Speciﬁcally, in LDP,
each user perturbs her data record locally to satisfy differential
privacy [16], and sends only the randomized, differentially
private version of the record to an aggregator. The latter then
performs computations on the collected noisy data to estimate
statistical analysis results on the original data. For instance,
in [18], Google as an aggregator collects perturbed usage
information from users of the Chrome browser, and estimates,
e.g., the proportion of users running a particular operating
system. Compared with traditional privacy standards such
as differential privacy in the centralized setting [16], which
typically assume a trusted data curator who possesses a set of
sensitive records, LDP provides a stronger privacy assurance
to users, as the true values of private records never leave their
local devices. Meanwhile, LDP also protects the aggregator
against potential leakage of users’ private information (which
happened to AOL1 and Netﬂix2 with serious consequences),
since the aggregator never collects exact private information
in the ﬁrst place. In addition, LDP satisﬁes the strong and
rigorous privacy guarantees of differential privacy; i.e., the
adversary (which includes the aggregator in LDP) cannot infer
sensitive information of an individual with high conﬁdence,
regardless of the adversary’s background knowledge.
Although LDP has attracted much attention in recent years,
the majority of existing solutions focus on applying LDP to
complex data types and/or data analysis tasks, as reviewed in
Section VII. Notably, the fundamental problem of collecting
numeric data has not been addressed sufﬁciently. As we
explain in Section III-A, in order to release a numeric value
in the range [−1, 1] under LDP, currently the user has only
two options: (i) the classic Laplace mechanism [16], which
injects unbounded noise to the exact data value, and (ii) a
recent proposal by Duchi et al. [14], which releases a perturbed
value that always falls outside the original data domain, i.e.,
[−1, 1]. Further, it is non-trivial to extend these methods to
handle multidimensional data. As elaborated in Section IV,
a straightforward extension of a single-attribute mechanism,
using the composition property of differential privacy, leads to
suboptimal result accuracy. Meanwhile, the multidimensional
version of [14], though asymptotically optimal in terms of
worst-case error, is complicated and involves a large constant.
Finally, to our knowledge, there is no existing solution that
1https://en.wikipedia.org/wiki/AOL search data leak
2https://www.wired.com/2009/12/netﬂix-privacy-lawsuit/
1
arXiv:1907.00782v1  [cs.CR]  28 Jun 2019


## Page 2


This full paper appears in the Proceedings of the IEEE 35th Annual International Conference on Data Engineering (ICDE),
held in April 2019.
TABLE I: Main theoretical results comparing the proposed
mechanisms PM and HM, as well as Duchi et al.’s solu-
tion [14]. The terms MaxVarPM, MaxVarHM, and MaxVarDu
denote the worst-case noise variance of these three methods,
respectively, for perturbing a d-dimensional numeric tuple
under ϵ-local differential privacy (elaborated in Section II).
In addition, ϵ# = ln

7+4
√
7+2√
20+14
√
7
9

≈1.29 and
ϵ∗= ln

−5+2
3√
6353−405
√
241 + 2
3√
6353+405
√
241
27

≈0.61.
Setting
Result
d > 1
ϵ > 0
MaxVarHM < MaxVarPM < MaxVarDu
d = 1
ϵ > ϵ#
MaxVarHM < MaxVarPM < MaxVarDu
ϵ = ϵ#
MaxVarHM < MaxVarPM = MaxVarDu
ϵ∗< ϵ < ϵ#
MaxVarHM < MaxVarDu < MaxVarPM
0 < ϵ ≤ϵ∗
MaxVarHM = MaxVarDu < MaxVarPM
can perturb multidimensional data containing both numeric
and categorical data with optimal worst-case error.
This paper addresses the above challenges and makes
several major contributions. First, we propose two novel
mechanisms, namely Piecewise Mechanism (PM) and Hybrid
Mechanism (HM), for collecting a single numeric attribute
under LDP, which obtain higher result accuracy compared to
existing methods. In particular, HM is built upon PM, and
has a worse-case noise variance that is at least no worse (and
usually better) than existing solutions. Then, we extend both
PM and HM to multidimensional data with both numeric and
categorical attributes with an elegant technique that achieves
asymptotic optimal error, while remaining conceptually simple
and easy to implement. Further, our ﬁne-grained analysis
reveals that although both [14] and the proposed methods ob-
tain asymptotically optimal error bound on multidimensional
numeric data, the former involves a larger constant than our
solutions. Table I summarizes the main theoretical results in
this paper, which are conﬁrmed in our experiments.
As a case study, using the proposed mechanisms as building
blocks, we present an LDP-compliant algorithm for stochastic
gradient descent (SGD), which can be applied to train a broad
class of machine learning models based on empirical risk
minimization, e.g., linear regression, logistic regression and
SVM classiﬁcation. Speciﬁcally, SGD iteratively updates the
model based on gradients of the objective function, which
are collected from individuals under LDP. Experiments using
several real datasets conﬁrm the high utility of the proposed
methods for various types of data analysis tasks.
In the following, Section II provides the necessary back-
ground on LDP. Sections III presents the proposed funda-
mental mechanisms for collecting a single numeric attribute
under LDP, while Section IV describes our solution for col-
lecting and analyzing multidimensional data with both numeric
and categorical attributes. Section V applies our solution to
common data analytics tasks based on SGD, including linear
regression, logistic regression, and support vector machines
(SVM) classiﬁcation. Section VI contains an extensive set
of experiments. Section VII reviews related work. Finally,
Section VIII concludes the paper.
II. PRELIMINARIES
In the problem setting, an aggregator collects data from
a set of users, and computes statistical models based on the
collected data. The goal is to maximize the accuracy of these
statistical models, while preserving the privacy of the users.
Following the local differential privacy model [5], [14], [18],
we assume that the aggregator already knows the identities
of the users, but not their private data. Formally, let n be the
total number of users, and ui (1 ≤i ≤n) denote the i-th user.
Each user ui’s private data is represented by a tuple ti, which
contains d attributes A1, A2, . . . , Ad. These attributes can be
either numeric or categorical. Without loss of generality, we
assume that each numeric attribute has a domain [−1, 1], and
each categorical attribute with k distinct values has a discrete
domain {1, 2, . . . , k}.
To protect privacy, each user ui ﬁrst perturbs her tuple ti
using a randomized perturbation function f. Then, she sends
the perturbed data f(ti) to the aggregator instead of her true
data record ti. Given a privacy parameter ϵ > 0 that controls
the privacy-utility tradeoff, we require that f satisﬁes ϵ-local
differential privacy (ϵ-LDP) [18], deﬁned as follows:
Deﬁnition 1 (ϵ-local differential privacy). A randomized func-
tion f satisﬁes ϵ-local differential privacy if and only if for
any two input tuples t and t′ in the domain of f, and for any
output t∗of f, we have:
Pr

f(t) = t∗
≤exp(ϵ) · Pr

f(t′) = t∗
.
(1)
The notation Pr[·] means probability. If f’s output is con-
tinuous, Pr[·] in (1) is replaced by the probability density
function. Basically, local differential privacy is a special case
of differential privacy [17] where the random perturbation is
performed by the users, not by the aggregator. According to the
above deﬁnition, the aggregator, who receives the perturbed
tuple t∗, cannot distinguish whether the true tuple is t or
another tuple t′ with high conﬁdence (controlled by parameter
ϵ), regardless of the background information of the aggregator.
This provides plausible deniability to the user [9].
We aim to support two types of analytics tasks under ϵ-LDP:
(i) mean value and frequency estimation and (ii) machine
learning models based on empirical risk minimization. In the
former, for each numerical attribute Aj, we aim to estimate the
mean value of Aj over all n users, 1
n
Pn
i=1 ti[Aj]. For each
categorical attribute A′
j, we aim to estimate the frequency of
each possible value of A′
j. Note that value frequencies in a
categorical attribute A′
j can be transformed to mean values
once we expand A′
j into k binary attributes using one-hot
encoding. Regarding empirical risk minimization, we focus
on three common analysis tasks: linear regression, logistic
regression, and support vector machines (SVM) [11].
Unless otherwise speciﬁed, all expectations in this paper are
taken over the random choices made by the algorithms con-
sidered. We use E[·] and Var[·] to denote a random variable’s
expected value and variance, respectively.
2


## Page 3


This full paper appears in the Proceedings of the IEEE 35th Annual International Conference on Data Engineering (ICDE),
held in April 2019.
III. COLLECTING A SINGLE NUMERIC ATTRIBUTE
This section focuses on the problem of estimating the mean
value of a numeric attribute by collecting data from individuals
under ϵ-LDP. Section III-A reviews two existing methods,
Laplace Mechanism [16] and Duchi et al.’s solution [14],
and discusses their deﬁciencies. Then, Section III-B describes
a novel solution, called Piecewise Mechanism (PM), that
addresses these deﬁciencies and usually leads to higher (or
at least comparable) accuracy than existing solutions. Section
III-C presents our main proposal, called Hybrid Mechanism
(HM), whose worst-case result accuracy is no worse than PM
and existing methods, and is often better than all of them.
A. Existing Solutions
Laplace mechanism and its variants. A classic mechanism
for enforcing differential privacy is the Laplace Mechanism
[16], which can be applied to the LDP setting as follows. For
simplicity, assume that each user ui’s data record ti contains
a single numeric attribute whose value lies in range [−1, 1]. In
the following, we abuse the notation by using ti to denote this
attribute value. Then, we deﬁne a randomized function that
outputs a perturbed record t∗
i = ti + Lap
  2
ϵ

, where Lap(λ)
denotes a random variable that follows a Laplace distribution
of scale λ, with the following probability density function:
pdf(x) =
1
2λ exp

−|x|
λ

.
Clearly, this estimate t∗
i is unbiased, since the injected
Laplace noise Lap
  2
ϵ

in each t∗
i has zero mean. In addition,
the variance in t∗
i is
8
ϵ2 . Once the aggregator receives all
perturbed tuples, it simply computes their average 1
n
Pn
i=1 t∗
i
as an estimate of the mean with error scale O
 1
ϵ√n

.
Soria-Comas and Domingo-Ferrer [35] propose a more
sophisticated variant of Laplace mechanism, hereafter re-
ferred to as SCDF, that obtains improved result accuracy
for multi-dimensional data. Later, Geng et al. [21] propose
Staircase mechanism, which achieves optimal performance for
unbounded input values (e.g., from a domain of (−∞, +∞)).
Speciﬁcally, for a single attribute value ti, both methods inject
random noise ni drawn from the following piece-wise constant
probability distribution:
pdf(ni = x) =







a(m)
ejϵ ,
if x ∈[−m −2(j + 1), −m −2j] , j ∈N,
a(m),
if x ∈[−m, m],
a(m)
ejϵ ,
if x ∈[m + 2j, m + 2(j + 1)] , j ∈N.
(2)
In SCDF, m = 2· 1−exp(−ϵ)−ϵ exp(−ϵ)
ϵ−ϵ exp(−ϵ)
and a(m) = ϵ
4; in Stair-
case mechanism, m =
2
1+eϵ/2 and a(m) =
1−e−ϵ
2m+4e−ϵ−2me−ϵ .
Note that the optimality result in [21] does not apply to the
case with bounded inputs. We experimentally compare the
proposed solutions with both SCDF and Staircase in Section
VI.
Duchi et al.’s solution. Duchi et al. [14] propose a method
to perturb multidimensional numeric tuples under LDP. Al-
gorithm 1 illustrates Duchi et al.’s solution [14] for the one-
dimensional case. (We discuss the multidimensional case in
Algorithm
1:
Duchi
et
al.’s
Solution
[14]
for
One-Dimensional Numeric Data.
input : tuple ti ∈[−1, 1] and privacy parameter ϵ.
output: tuple t∗
i ∈
n
−eϵ+1
eϵ−1,
eϵ+1
eϵ−1
o
.
1 Sample a Bernoulli variable u such that
Pr[u = 1] = eϵ −1
2eϵ + 2 · ti + 1
2 ;
2 if u = 1 then
3
t∗
i = eϵ+1
eϵ−1;
4 else
5
t∗
i = −eϵ+1
eϵ−1;
6 return t∗
i
Section IV.) In particular, given a tuple ti ∈[−1, 1], the
algorithm returns a perturbed tuple t∗
i that equals either eϵ+1
eϵ−1
or −eϵ+1
eϵ−1, with the following probabilities:
Pr

t∗
i = x | ti

=



eϵ−1
2eϵ+2 · ti + 1
2,
if x = eϵ+1
eϵ−1,
−eϵ−1
2eϵ+2 · ti + 1
2,
if x = −eϵ+1
eϵ−1.
(3)
Duchi et al. prove that t∗
i is an unbiased estimator of the input
value ti. In addition, the variance of t∗
i is:
Var[t∗
i ] = E

(t∗
i )2
−(E[t∗
i ])2
= ( eϵ+1
eϵ−1)2 · ti·(eϵ−1)+eϵ+1
2eϵ+2
+(−eϵ+1
eϵ−1)2 · −ti·(eϵ−1)+eϵ+1
2eϵ+2
−ti2
=

eϵ+1
eϵ−1
2
−ti2.
(4)
Therefore, the worst-case variance of t∗
i equals

eϵ+1
eϵ−1
2
, and
it occurs when ti = 0. Upon receiving the perturbed tuples
output by Algorithm 1, the aggregator simply computes the
average value of the attribute over all users to obtain an
estimated mean.
Deﬁciencies of existing solutions. Fig. 1 illustrates the
worst-case variance of the noisy values returned by the
Laplace mechanism and Duchi et al.’s solution, when ϵ varies.
Duchi et al.’s solution offers considerably smaller variance
than the Laplace mechanism when ϵ ≤2, but is signiﬁcantly
outperformed by the latter when ϵ is large. To explain, recall
that Duchi et al.’s solution returns either t∗
i
=
eϵ+1
eϵ−1 or
t∗
i = −eϵ+1
eϵ−1, even when the input tuple ti = 0. As such,
the noisy value t∗
i output by Duchi et al.’s solution always
has an absolute value eϵ+1
eϵ−1 > 1, due to which t∗
i ’s variance
is always larger than 1 when ti = 0, regardless of how large
the privacy budget ϵ is. In contrast, the Laplace mechanism
incurs a noise variance of 8/ϵ2, which decreases quadratically
with the increase of ϵ, due to which it is preferable when ϵ is
large. However, when ϵ is small, the relatively “fat” tail of the
Laplace distribution leads to a large noise variance, whereas
Duchi et al.’s solution does not suffer from this issue since it
conﬁnes t∗
i within a relatively small range

−eϵ+1
eϵ−1, eϵ+1
eϵ−1

.
3


## Page 4


This full paper appears in the Proceedings of the IEEE 35th Annual International Conference on Data Engineering (ICDE),
held in April 2019.
0
1
2
3
4
5
6
7
8
0
1
2
3
4
5
6
Fig. 1: Different mechanisms’ worst-case noise variances for
one-dimensional numeric data versus the privacy budget ϵ.
Our Piecewise Mechanism and Hybrid Mechanism will be
discussed in Sections III-B and III-C, respectively.
SCDF and Staircase mechanism suffer from the same issue as
the Laplace mechanism, as demonstrated in our experiments
in Section VI.
A natural question is: can we design a perturbation method
that combines the advantages of the Laplace mechanism and
Duchi et al.’s solution to minimize the variance of t∗
i across a
wide spectrum of ϵ? Intuitively, such a method should conﬁne
t∗
i to a relatively small domain (as Duchi et al.’s solution
does), and should allow t∗
i to be close to ti with reasonably
large probability (as the Laplace mechanism does). In what
follows, we will present a new perturbation method based on
this intuition.
B. Piecewise Mechanism
Our ﬁrst proposal, referred to as the Piecewise Mechanism
(PM), takes as input a value ti ∈[−1, 1], and outputs a
perturbed value t∗
i in [−C, C], where
C = exp(ϵ/2) + 1
exp(ϵ/2) −1.
The probability density function (pdf) of t∗
i is a piecewise
constant function as follows:
pdf(t∗
i = x | ti) =



p,
if x ∈[ℓ(ti), r(ti)],
p
exp(ϵ),
if x ∈[−C, ℓ(ti)) ∪(r(ti), C].
(5)
where
p = exp(ϵ) −exp(ϵ/2)
2 exp(ϵ/2) + 2
,
ℓ(ti) = C + 1
2
· ti −C −1
2
, and
r(ti) = ℓ(ti) + C −1.
Let pdf(t∗
i ) be short for pdf(t∗
i = x | ti). Fig. 2 illustrates
pdf(t∗
i ) for the cases of ti = 0, ti = 0.5, and ti = 1.
Observe that when ti = 0, pdf(t∗
i ) is symmetric and con-
sists of three “pieces”, among which the center piece (i.e.,
t∗
i ∈[ℓ(ti), r(ti)]) has a higher probability than the other two.
When ti increases from 0 to 1, the length of the center piece
remains unchanged (since r(ti)−ℓ(ti) = C−1), but the length
Algorithm 2: Piecewise Mechanism for One-Dimensional
Numeric Data.
input : tuple ti ∈[−1, 1] and privacy parameter ϵ.
output: tuple t∗
i ∈[−C, C] .
1 Sample x uniformly at random from [0, 1];
2 if x <
eϵ/2
eϵ/2+1 then
3
Sample t∗
i uniformly at random from [ℓ(ti), r(ti)];
4 else
5
Sample t∗
i uniformly at random from
[−C, ℓ(ti)) ∪(r(ti), C];
6 return t∗
i
of the rightmost piece (i.e., t∗
i ∈(r(ti), C]) decreases, and is
reduced to 0 when ti = 1. The case when ti < 0 can be
illustrated in a similar manner.
Algorithm 2 shows the pseudo-code of PM, assuming the
input domain is [−1, 1]. In general, when the input domain
is ti ∈[−r, r], r > 0, the user (i) computes t′
i = ti/r, (ii)
perturbs t′
i using PM, since t′
i ∈[−1, 1], and (iii) submits
r · t∗
i to the server, where t∗
i denotes the noisy value output
by Algorithm 2. It can be veriﬁed that r · t∗
i is an unbiased
estimator of ti. The above method requires that the user knows
r, which is a common assumption in the literature, e.g., in
Duchi et al.’s work [14].
The following lemmas establish the theoretical guarantees
of Algorithm 2.
Lemma 1. Algorithm 2 satisﬁes ϵ-local differential privacy.
In addition, given an input value ti, it returns a noisy value
t∗
i with E[t∗
i ] = ti and
Var[t∗
i ] =
ti2
eϵ/2 −1 +
eϵ/2 + 3
3(eϵ/2 −1)2 .
The proof appears in the full version [2].
By Lemma 1, PM returns a noisy value t∗
i whose variance
is at most
1
eϵ/2 −1 +
eϵ/2 + 3
3(eϵ/2 −1)2 =
4eϵ/2
3(eϵ/2 −1)2 .
The purple line in Fig. 1 illustrates this worst-case variance of
PM as a function of ϵ. Observe that PM’s worst-case variance
is considerably smaller than that of Duchi et al.’s solution
when ϵ ≥1.29, and is only slightly larger than the latter when
ϵ < 1.29, where 1.29 is x-coordinate of the point that the
Duchi et al.’ solution curve intersects that of PM in Fig. 1.
Furthermore, it can be proved that PM’s worst-case variance
is strictly smaller than Laplace mechanism’s, regardless of the
value of ϵ. This makes PM be a more preferable choice than
both the Laplace mechanism and Duchi et al.’s solution.
Furthermore, Lemma 1 also shows that the variance of
t∗
i in PM monotonically decreases with the decrease of |ti|,
which makes PM particularly effective when the distribution
of the input data is skewed towards small-magnitude values.
(In Section VI, we show that |ti| tends to be small in a large
4


## Page 5


This full paper appears in the Proceedings of the IEEE 35th Annual International Conference on Data Engineering (ICDE),
held in April 2019.
C
-C
0
pdf(ti )

ti

C
-C
0.5
pdf(ti )

ti

C
-C
1
pdf(ti )

ti

(a) ti = 0
(b) ti = 0.5
(c) ti = 1
Fig. 2: The noisy output t∗
i ’s probability density function pdf(t∗
i ) in the Piecewise Mechanism.
class of applications.) In contrast, Duchi et al.’s solution incurs
a noise variance that increases with the decrease of |ti|, as
shown in Equation 4.
Now consider the estimator 1
n
Pn
i t∗
i used by the aggregator
to infer the mean value of all ti. The variance of this estimator
is 1/n of the average variance of t∗
i . Based on this, the fol-
lowing lemma establishes the accuracy guarantee of 1
n
Pn
i t∗
i .
Lemma 2. Let Z =
1
n
Pn
i=1 t∗
i and X =
1
n
Pn
i=1 ti. With
at least 1 −β probability,
Z −X
 = O
 p
log(1/β)
ϵ√n
!
.
We omit the proof of Lemma 2 as it is a special case of
Lemma 5 to be presented in Section IV-B.
Remark. PM bears some similarities to SCDF [35] and
Staircase mechanism [21] described in Section III-A, in the
sense that the added noise in PM also follows a piece-
wise constant distribution, as in SCDF and Staircase. On the
other hand, there are two crucial differences between PM and
SCDF/Staircase. First, SCDF and Staircase mechanism assume
an unbounded input, and produce an unbounded output (i.e.,
with range (−∞, +∞)) accordingly. In contrast, PM has both
bounded input (with domain [−1, 1]) and output (with range
[−C, C]). Second, the noise distribution of SCDF/Staircase
consists of an inﬁnite number of “pieces” that are data
independent, whereas the output distribution of the piecewise
mechanism consists of up to three “pieces” whose lengths and
positions depend on the input data.
C. Hybrid Mechanism
As discussed in Section III-B, the worst-case result accuracy
of PM dominates that of the Laplace mechanism, and yet it can
still be (slightly) worse than Duchi et al’s solution, since the
noise variance incurred by the former (resp. latter) decreases
(resp. increases) with the decrease of |ti|. Can we construct
a method that that preserves the advantages of PM and is at
the same time always no worse than Duchi et al’s solution?
The answer turns out to be positive: that we can combine
PM and Duchi et al’s solution into a new Hybrid Mechanism
(HM). Further, the combination used in HM is non-trivial; as
a result, the noise variance of HM is often smaller than both
PM and Duchi et al’s solution, as shown in Fig. 1 on Page 4.
In particular, given an input value ti, HM ﬂips a coin whose
head probability equals a constant α; if the coin shows a head
(resp. tail), then we invoke PM (resp. Duchi et al.’s solution)
to perturb ti. Given ti and ϵ, the noise variance incurred by
HM is
σ2
H(ti, ϵ) = α · σ2
P (ti, ϵ) + (1 −α) · σ2
D(ti, ϵ),
where σ2
P (ti, ϵ) and σ2
D(ti, ϵ) denote the noise variance in-
curred by PM and Duchi et al.’s solution, respectively, when
given ti and ϵ as input. We have the following lemma.
Lemma 3. Let ϵ∗be deﬁned as:
ϵ∗= ln

−5+2
3√
6353−405
√
241 + 2
3√
6353+405
√
241
27

≈0.61.
(6)
The term maxti∈[−1,1] σ2
H(ti, ϵ) is minimized when
α =
(
1 −e−ϵ/2,
for ϵ > ϵ∗,
0,
for ϵ ≤ϵ∗.
(7)
The proof appears in the full version [2].
By Lemma 3, when α satisﬁes Equation 7, the worst-case
noise variance of HM is:
max
ti∈[−1,1] σ2
H(ti, ϵ) =





eϵ/2+3
3eϵ/2(eϵ/2−1) +
(eϵ+1)2
eϵ/2(eϵ−1)2 , for ϵ > ϵ∗,

eϵ+1
eϵ−1
2
,
for ϵ ≤ϵ∗.
(8)
Based on Equation 8, Lemma 1, and Equation 4, which present
σ2
H(ti, ϵ), σ2
P (ti, ϵ), and σ2
D(ti, ϵ), respectively, we can show
that HM often dominates both PM and Duchi et al.’s solution
in minimizing the worst-case noise variance. The detailed
results are summarized under d = 1 (meaning one dimension)
in Table I of Section I, where ϵ∗follows from Equation 6 and
ϵ# is derived by solving ϵ which makes maxti∈[−1,1] σ2
P (ti, ϵ)
and maxti∈[−1,1] σ2
D(ti, ϵ) equal. We highlight some results as
follows.
Corollary 1. Suppose that α satisﬁes Equation 7. If ϵ > ϵ∗,
max
ti∈[−1,1]σ2
H(ti, ϵ) < min

max
ti∈[−1,1]σ2
P (ti, ϵ),
max
ti∈[−1,1]σ2
D(ti, ϵ)

;
otherwise,
max
ti∈[−1,1] σ2
H(ti, ϵ) =
max
ti∈[−1,1] σ2
D(ti, ϵ) <
max
ti∈[−1,1] σ2
P (ti, ϵ).
The red line in Fig. 1 on Page 4 shows the worst-case noise
variance incurred by HM, which is consistently no higher than
5


## Page 6


This full paper appears in the Proceedings of the IEEE 35th Annual International Conference on Data Engineering (ICDE),
held in April 2019.
Algorithm
3:
Duchi
et
al.’s
Solution
[14]
for
Multidimensional Numeric Data.
input : tuple ti ∈[−1, 1]d and privacy parameter ϵ.
output: tuple t∗
i ∈{−B, B}d.
1 Generate a random tuple v ∈{−1, 1}d by sampling each
v[Aj] independently from the following distribution:
Pr[v[Aj] = x] =



1
2 + 1
2ti[Aj],
if x = 1
1
2 −1
2ti[Aj],
if x = −1
;
2 Let T + (resp. T −) be the set of all tuples
t∗∈{−B, B}d such that t∗· v ≥0 (resp. t∗· v ≤0);
3 Sample a Bernoulli variable u that equals 1 with
eϵ/(eϵ + 1) probability;
4 if u = 1 then
5
return a tuple uniformly at random from T +;
6 else
7
return a tuple uniformly at random from T −;
those of all other three methods (HM reduces to Duchi et al.’s
solution for ϵ ≤ϵ∗). In addition, observe that PM’s accuracy
is close to HM’s, which demonstrates the effectiveness of PM.
IV. COLLECTING MULTIPLE ATTRIBUTES
We now consider the case where each user’s data record
contains d > 1 attributes. In this case, a straightforward
solution is to collect each attribute separately using a single-
attribute perturbation algorithm, such that every attribute is
given a privacy budget ϵ/d. Then, by the composition theo-
rem [17], the collection of all attributes satisﬁes ϵ-LDP. This
solution, however, offers inferior data utility. For example,
suppose that all d attributes are numeric, and we process each
attribute using PM, setting the privacy budget to ϵ/d. Then, by
Lemma 2, the amount of noise in the estimated mean of each
attribute is O

d√log d
ϵ√n

, which is super-linear to d, and hence,
can be excessive when d is large. To address the problem, the
ﬁrst and only existing solution that we are aware of is by
Duchi et al. [14] for the case of multiple numeric attributes,
presented in Section IV-A.
A. Existing Solution for Multiple Numeric Attributes
Algorithm 3 shows the pseudo-code of Duchi et al.’s so-
lution for multidimensional numeric data. It takes as input
a tuple ti ∈[−1, 1]d of user ui and a privacy parameter ϵ,
and outputs a perturbed vector t∗
i ∈{−B, B}d, where B is
a constant decided by d and ϵ. Upon receiving the perturbed
tuples, the aggregator simply computes the average value for
each attribute over all users, and outputs these averages as the
estimates of the mean values for their corresponding attributes.
Next, we focus on the calculation of B, which is rather
complicated.
Essentially, B is a scaling factor to ensure that the expected
value of a perturbed attribute is the same as that of the exact
attribute value. First, we compute:
Algorithm
4:
Our
Method
for
Multiple
Numeric
Attributes.
input : tuple ti ∈[−1, 1]d and privacy parameter ϵ.
output: tuple t∗
i ∈[−C · d, C · d]d.
1 Let t∗
i = ⟨0, 0, . . . , 0⟩;
2 Let k = max

1, min

d,
 ϵ
2.5
		
;
3 Sample k values uniformly without replacement from
{1, 2, . . . , d};
4 for each sampled value j do
5
Feed ti[Aj] and ϵ
k as input to PM or HM, and obtain
a noisy value xi,j;
6
t∗
i [Aj] = d
kxi,j;
7 return t∗
i
Cd =







2d−1
(
d−1
(d−1)/2),
if d is odd,
2d−1+ 1
2(
d
d/2)
(
d−1
d/2)
,
otherwise.
(9)
Then, B is calculated by:
B = exp(ϵ) + 1
exp(ϵ) −1 · Cd.
(10)
Duchi et al. show that 1
n
Pn
i=1 t∗
i [Aj] is an unbiased estimator
of the mean of Aj, and
E
"
max
j∈[1,d]

1
n
n
X
i=1
t∗
i [Aj] −1
n
n
X
i=1
ti[Aj]

#
= O
√d log d
ϵ√n

,
(11)
which is asymptotically optimal [14].
Although Duchi et al’s method can provide strong privacy
assurance and asymptotic error bound, it is rather sophisti-
cated, and it cannot handle the case that a tuple contains
numeric attributes as well as categorical attributes. To address
this issue, we present extensions of PM and HM that (i)
are much simpler than Duchi et al.’s solution but achieve
the same privacy assurance and asymptotic error bound, and
(ii) can handle any combination of numeric and categorical
attributes. For ease of exposition, we ﬁrst extend PM and HM
for the case when each ti contains only numeric attributes in
Section IV-B, and then discuss the case of arbitrary attributes
in Section IV-C.
B. Extending PM and HM for Multiple Numeric Attributes
Algorithm 4 shows the pseudo-code of our extension of PM
and HM for multidimensional numeric data. Given a tuple
ti ∈[−1, 1]d, the algorithm returns a perturbed tuple t∗
i that
has non-zero value on k attributes, where
k = max
n
1, min
n
d,
j ϵ
2.5
koo
.
(12)
In particular, each Aj of those k attributes is selected uni-
formly at random (without replacement) from all d attributes
of ti, and t∗
i [Aj] is set to d
k · x, where x is generated by PM
or HM given ti[Aj] and ϵ
k as input.
6


## Page 7


This full paper appears in the Proceedings of the IEEE 35th Annual International Conference on Data Engineering (ICDE),
held in April 2019.
The intuition of Algorithm 4 is as follows. By requiring
each user to submit k (instead of d) attributes, it increases the
privacy budget for each attribute from ϵ/d to ϵ/k, which in turn
reduces the noise variance incurred. As a trade-off, sampling
k out of d attributes entails additional estimation error, but this
trade-off can be balanced by setting k to an appropriate value,
which is shown in Equation 12. We derive the setting of k
by minimizing the worst-case noise variance of Algorithm 4
when it utilizes PM (resp. HM)3.
Lemma 4. Algorithm 4 satisﬁes ϵ-local differential privacy.
In addition, given an input tuple ti, it outputs a noisy tuple
t∗
i , such that for any j ∈[1, d], E [t∗
i [Aj]] = ti[Aj].
The proof appears in the full version [2].
By Lemma 4, the aggregator can use
1
n
Pn
i=1 t∗[Aj] as
an unbiased estimator of the mean of Aj. The following
lemma shows that the accuracy guarantee of this estimator
matches that of Duchi et al.’s solution for multidimensional
numeric data (see Equation 11), which has been proved to be
asymptotically optimal [14]. This indicates that Algorithm 4’s
accuracy guarantee is also optimal in the asymptotic sense.
Lemma 5. For any j ∈[1, d], let Z[Aj] =
1
n
Pn
i=1 t∗
i [Aj]
and X[Aj] = 1
n
Pn
i=1 ti[Aj]. With at least 1 −β probability,
max
j∈[1,d]
Z[Aj] −X[Aj]
 = O
 p
d log(d/β)
ϵ√n
!
.
The proof appears in the full version [2].
Lemma
6
discusses
the
noise
variances
induced
by
Duchi et al.’s solution, PM and HM, respectively.
Lemma 6. For a d-dimensional numeric tuple ti which is
perturbed as t∗
i under ϵ-LDP, and for each Aj of the d
attributes, the variance of t∗
i [Aj] induced by Duchi et al.’s
solution is
VarD

t∗
i [Aj]

=

eϵ+1
eϵ−1
2
Cd
2 −(ti[Aj])2 ,
(13)
where Cd is deﬁned by Equation 9. Meanwhile, the variance
of t∗
i [Aj] induced by PM is
VarP

t∗
i [Aj]

=
d(eϵ/(2k)+3)
3k(eϵ/(2k)−1)2 +
h
d·eϵ/(2k)
k(eϵ/(2k)−1) −1
i
(ti[Aj])2 ;
(14)
and the variance of t∗
i [Aj] induced by HM is
VarH

t∗
i [Aj]

=







d
k
h
eϵ/(2k)+3
3eϵ/(2k)(eϵ/(2k)−1) +
(eϵ/k+1)2
eϵ/(2k)(eϵ/k−1)2
i
+
  d
k −1

(ti[Aj])2 ,
for ϵ/k > ϵ∗,
d
k

eϵ/k+1
eϵ/k−1
2
+
  d
k −1

(ti[Aj])2 ,
for ϵ/k ≤ϵ∗,
(15)
where ϵ∗is deﬁned by Equation 6.
From Equations 13, 14, and 15, we can prove the following:
3We discuss how to obtain the value of k in the full version [2].
Corollary 2. For any d > 1 and ϵ > 0, both PM and HM
outperform Duchi et al.’s solution in minimizing the worst-case
noise variance; more speciﬁcally, for any d > 1 and ϵ > 0,
max
ti[Aj]∈[−1,1] VarH

t∗
i [Aj]

<
max
ti[Aj]∈[−1,1] VarP

t∗
i [Aj]

<
max
ti[Aj]∈[−1,1] VarD

t∗
i [Aj]

. (16)
To illustrate Corollary 2, Fig. 3 shows the worst-case
variance of PM (resp. HM) as a fraction of the worst-case
variance of Duchi et al.’s solution, for various d and privacy
budget ϵ. Observe that for d = 5, 10, 20, 40, the wort-case
variance of HM is at most 77% of that of Duchi et al.’s
solution, and PM’s worst-case variance is also smaller than
the latter. In our experiments, we demonstrate that both HM
and PM outperform Duchi et al.’s solution in terms of the
empirical accuracy for multidimensional numeric data.
C. Handling Categorical Attributes
So far our discussion is limited to numeric attributes. Next
we extend Algorithm 4 to handle data with both numeric
and categorical attributes. Recall from Section II that for
each categorical attribute A, our objective is to estimate the
frequency of each value v in A over all users. We note
that most existing LDP algorithms (e.g., [5], [18], [38]) for
categorical data are designed for this purpose, albeit limited
to a single categorical attribute.
Formally, we assume that we are given an algorithm f
that takes an input a privacy budget ϵ and a one-dimensional
tuple ti with a categorical attribute A, and outputs a perturbed
tuple t∗
i while ensuring ϵ-LDP. In addition, we assume there
is a function g(x, y) that g(x, y) = 1 if x = y; and 0,
otherwise. Then for any value v ∈A,
1
n
P
i∈S g(t∗
i , v) is an
estimator of the frequency of v over all users, where S is
the set of {1, 2, . . . n}. Then, for the general case when ti
contains d (numeric or categorical) attributes A1, A2, . . . , Ad,
the extended version of Algorithm 4 would request each user
to perform the following:
1) Sample k values uniformly at random from {1, 2, . . . , d},
where k is as deﬁned in Equation 12;
2) For each sampled j, if Aj is a numerical attribute, then
submit a noisy version of t[Aj] computed as in Lines
3–5 of Algorithm 4; otherwise (i.e., Aj is a categorical
attribute), submit f(t[Aj], ϵ/k), where f can be any ex-
isting solution for perturbing a single categorical attribute
under ϵ-LDP;
Once the aggregator collects data from all users, she can
estimate the mean of each numeric attribute A in the same way
as in Algorithm 4.
In addition, for any categorical attribute
A′ and any value v in the domain of A′, she can estimate
the frequency of v among all users as
d
kn
P
v∗∈V ∗g(v∗, v),
where V ∗denotes the set of perturbed A′ values submitted by
users. The accuracy of this estimator depends on both d and
the accuracy of single-attribute perturbation algorithm used
for A′. In our experiments, we apply the optimized unary
7


## Page 8


This full paper appears in the Proceedings of the IEEE 35th Annual International Conference on Data Engineering (ICDE),
held in April 2019.
Piecewise Mechanism
Hybrid Mechanism
0
1
2
3
4
5
6
7
8
0
0.2
0.4
0.6
0.8
1
0
1
2
3
4
5
6
7
8
0
0.2
0.4
0.6
0.8
1
0
1
2
3
4
5
6
7
8
0
0.2
0.4
0.6
0.8
1
0
1
2
3
4
5
6
7
8
0
0.2
0.4
0.6
0.8
1
(a) d = 5
(b) d = 10
(c) d = 20
(d) d = 40
Fig. 3: The worst-case variance of PM (resp. HM) as a fraction of the worst-case variance of Duchi et al.’s solution, for various
privacy budget ϵ and data dimensionality d.
encoding (OUE) protocol of Wang et al. [38] to perturb a
single categorical attribute, which is the current state of the
art to our knowledge.
V. STOCHASTIC GRADIENT DESCENT UNDER
LOCAL DIFFERENTIAL PRIVACY
This section investigates building a class of machine learn-
ing models under ϵ-LDP that can be expressed as empirical
risk minimization, and solved by stochastic gradient descent
(SGD). In particular, we focus on three common types of learn-
ing tasks: linear regression, logistic regression, and support
vector machines (SVM) classiﬁcation.
Suppose that each user ui has a pair ⟨xi, yi⟩, where xi ∈
[−1, 1]d and yi ∈[−1, 1] (for linear regression) or yi ∈
{−1, 1} (for logistic regression and SVM classiﬁcation). Let
ℓ(·) be a loss function that maps a d-dimensional parameter
vector β into a real number, and is parameterized by xi and
yi. We aim to identify a parameter vector β∗such that
β∗= arg min
β
"
1
n
 n
X
i=1
ℓ(β; xi, yi)
!
+ λ
2 ∥β∥2
2
#
,
where λ > 0 is a regularization parameter. We consider three
speciﬁc loss functions:
1) Linear regression: ℓ(β; xi, yi) = (xT
i β −yi)2;
2) Logistic regression: ℓ(β; xi, yi) = log

1 + e−yixT
i β
;
3) SVM (hinge loss): ℓ(β; xi, yi) = max

0, 1 −yixT
i β
	
.
For convenience, we deﬁne
ℓ′(β; xi, yi) = ℓ(β; xi, yi) + λ
2 ∥β∥2
2.
The proposed approach solves β∗using SGD, which starts
from an initial parameter vector β0, and iteratively updates it
into β1, β2, . . . based on the following equation:
βt+1 = βt −γt · ∇ℓ′(βt; x, y),
where ⟨x, y⟩is the data record of a randomly selected user,
∇ℓ′(βt; x, y) is the gradient of ℓ′ at βt, and γt is called the
learning rate at the t-th iteration. The learning rate γt is
commonly set by a function (called the learning schedule)
of the iteration number t; a popular learning schedule is
γt = O(1/
√
t).
In the non-private setting, SGD terminates when the differ-
ence between βt+1 and βt is sufﬁciently small. Under ϵ-LDP,
however, ∇ℓ′ is not directly available to the aggregator, and
needs to be collected in a private manner. Towards this end,
existing studies [14], [22] have suggested that the aggregator
asks the selected user in each iteration to submit a noisy ver-
sion of ∇ℓ′, by using the Laplace mechanism or Duchi et al.’s
solution (i.e., Algorithm 3). Our baseline approach is based on
this idea, and improves these existing methods by perturbing
∇ℓ′ using Algorithm 4. In particular, in each iteration, we
involve a group G of users, and ask each of them to submit a
noisy version of the gradient using Algorithm 4. Here, if any
entry of ∇ℓi is greater than 1 (resp. smaller than −1), then the
user should clip it to 1 (resp. −1) before perturbation, where
∇ℓi is the gradient generated by the i-th user in group G. That
is a common technique referred to as “gradient clipping” in the
deep learning literature. After that, we update the parameter
vector βt with the mean of the noisy gradients, i.e.,
βt+1 = βt −γt ·
1
|G|
P|G|
i=1 ∇ℓ∗
i ,
where ∇ℓ∗
i is the noisy gradient submitted by the i-th user
in group G. This helps because the amount of noise in the
average gradient is O
 √d log d
ϵ√
|G|

, which could be acceptable
if |G| = Ω
 d(log d)/ϵ2
.
Note that in the non-private case, the aggregator often allows
each user to participate in multiple iterations (say m iterations)
to improve the accuracy of the model. But it does not work in
the local differential privacy setting. To explain this, suppose
that the i-th (i ∈[1, m]) gradient returned by the user
satisﬁes ϵi-differential privacy. By the composition property
of differential privacy [29], if we enforce ϵ-differential privacy
for the user’s data, we should have Pm
i=1 ϵi ≤ϵ. Consider that
we set ϵi = ϵ/m. Then, the amount of noise in each gradient
becomes O

m√d log d
ϵ

; accordingly, the group size becomes
|G| = Ω
 m2d log d/ϵ2
, which is m2 times larger compared
to the case where each user only participates in at most one
iteration. It then follows that the total number of iterations
in the algorithm is inverse proportional to 1/m; i.e., setting
m > 1 only degrades the performance of the algorithm.
VI. EXPERIMENTS
We have implemented the proposed methods and evaluated
them using two public datasets extracted from the Integrated
Public Use Microdata Series [1], BR and MX, which contains
8


## Page 9


This full paper appears in the Proceedings of the IEEE 35th Annual International Conference on Data Engineering (ICDE),
held in April 2019.
 1e-006
 1e-005
 0.0001
 0.001
 0.01
0.5
1
2
4
MSE
privacy budget ε
Laplace
Staircase
Duchi
PM
HM
 1e-006
 1e-005
 0.0001
 0.001
 0.01
0.5
1
2
4
MSE
privacy budget ε
Laplace
SCDF
Duchi
PM
HM
 1e-007
 1e-006
 1e-005
 0.0001
 0.001
0.5
1
2
4
MSE
privacy budget ε
OUE
Proposed solution
 1e-006
 1e-005
 0.0001
 0.001
0.5
1
2
4
MSE
privacy budget ε
OUE
Proposed solution
(a) BR-Numeric
(b) MX-Numeric
(c) BR-Categorical
(d) MX-Categorical
Fig. 4: Result accuracy for mean estimation (on numeric attributes) and frequency estimation (on categorical attributes).
Laplace
Duchi et al.
PM
HM
SCDF
 1e-006
 1e-005
 0.0001
 0.001
 0.01
0.5
1
2
4
MSE
privacy budget ε
 1e-006
 1e-005
 0.0001
 0.001
 0.01
0.5
1
2
4
MSE
privacy budget ε
 1e-005
 0.0001
 0.001
 0.01
0.5
1
2
4
MSE
privacy budget ε
 1e-005
 0.0001
 0.001
 0.01
0.5
1
2
4
MSE
privacy budget ε
(a) µ = 0
(b) µ = 1/3
(c) µ = 2/3
(d) µ = 1
Fig. 5: Result accuracy on synthetic datasets with 16 dimensions, each of which follows a Gaussian distribution N(µ, 1/16)
truncated to [−1, 1].
census records from Brazil and Mexico, respectively. BR
contains 4M tuples and 16 attributes, among which 6 are
numerical (e.g., age) and 10 are categorical (e.g., gender);
MX has 4M records and 19 attributes, among which 5 are
numerical and 14 are categorical. Both datasets contain a
numerical attribute “total income”, which we use as the
dependent attribute in linear regression, logistic regression,
and SVM (explained further in Section VI-B). We normalize
the domain of each numerical attribute into [−1, 1]. In all
experiments, we report average results over 100 runs.
A. Results on Mean Value / Frequency Estimation
In the ﬁrst set of experiments, we consider the task of
collecting a noisy, multidimensional tuple from each user, in
order to estimate the mean of each numerical attribute and
the frequency of each categorical value. Since no existing
solution can directly support this task, we take the follow-
ing best-effort approach combining state-of-the-art solutions
through the composition property of differential privacy [29].
Speciﬁcally, let t be a tuple with dn numeric attributes and
dc categorical attributes. Given total privacy budget ϵ, we
allocate dnϵ/d budget to the numeric attributes, and dcϵ/d
to the categorical ones, respectively. Then, for the numeric
attributes, we estimate the mean value for each of them using
either (i) Duchi et al.’s solution (i.e., Algorithm 3), which
directly handles multiple numeric attributes, (ii) the Laplace
mechanism or (iii) SCDF [35], which is applied to each
numeric attribute individually using ϵ/d budget. The Staircase
mechanism leads to similar performance as SCDF, and we
omit its results for brevity. Regarding categorical attributes,
since no previous solution addresses the multidimensional
case, we apply the optimized unary encoding (OUE) protocol
of Wang et al. [38], the state of the art for frequency estimation
on a single categorical attribute, to each attribute independently
Laplace
Duchi et al.
PM
HM
SCDF
 1e-006
 1e-005
 0.0001
 0.001
 0.01
0.5
1
2
4
MSE
privacy budget ε
 1e-005
 0.0001
 0.001
 0.01
0.5
1
2
4
MSE
privacy budget ε
(a) Uniform distribution
(b) Power law distribution
Fig. 6: Result accuracy vs. privacy budget on different data
distributions.
with ϵ/d budget. Clearly, by the composition property of
differential privacy [29], the above approach satisﬁes ϵ-LDP.
We evaluate both the above best-effort approach using
existing methods, and the proposed solution in Section IV,
on the two real datasets BR and MX. For each method,
we measure the mean square error (MSE) in the estimated
mean values (for numeric attributes) and value frequencies
(for categorical attributes). Fig. 4 plots the MSE results as a
function of the total privacy budget ϵ. Overall, the proposed
solution consistently and signiﬁcantly outperforms the best-
effort approach combining existing methods. One major rea-
son is that the estimation error of the proposed solution is
asymptotically optimal, which scales sublinearly to the data
dimensionality d; in contrast, the best-effort combination of
existing approaches involves privacy budget splitting, which is
sub-optimal. For instance, on the categorical attributes, apply-
ing OUE [38] on each attribute individually leads to O

d
ϵ√n

error (where n is the number of users), which grows linearly
with data dimensionality d. This also explains the consistent
performance gap between Duchi et al.’s solution [14] and the
Laplace mechanism (SCDF mechanism) on numeric attributes.
9


## Page 10


This full paper appears in the Proceedings of the IEEE 35th Annual International Conference on Data Engineering (ICDE),
held in April 2019.
 1e-005
 0.0001
 0.001
 0.01
 0.1
0.25
0.5
1
2
4
MSE
Number of users (x106)
Laplace
SCDF
Duchi
PM
HM
 1e-005
 0.0001
 0.001
 0.01
1/16
1/8
1/4
1/2
1
MSE
Number of users (x106)
OUE
Proposed solution
(a) Numeric
(b) Categorical
Fig. 7: Result accuracy vs. number of users.
 1e-006
 1e-005
 0.0001
 0.001
5
10
15
19
MSE
dimensionality
Laplace
SCDF
Duchi
PM
HM
 1e-006
 1e-005
 0.0001
 0.001
5
10
15
19
MSE
dimensionality
OUE
Proposed solution
(a) Numeric
(b) Categorical
Fig. 8: Result accuracy vs. dimensionality.
Meanwhile, on numeric attributes, the proposed solutions
PM and HM outperform Duchi et al.’s solution in all settings.
This is because (i) although all three methods are asymptoti-
cally optimal, Duchi et al.’s solution incurs a larger constant
than the proposed algorithms and (ii) Duchi et al.’s solution
cannot handle categorical attributes, and, thus, needs to be
combined with OUE through privacy budget splitting, which
is sub-optimal. To eliminate the effect of (ii), we run an
additional set of experiments with only numeric attributes
on several synthetic datasets. Speciﬁcally, the ﬁrst synthetic
data contains 16 numeric attributes (i.e., same number of
attributes in BR), where each attribute value is generated
from a Gaussian distribution with mean value u and standard
deviation of 1/4, but discarding any value that fall out of
[−1, 1]. Fig. 5 shows the results with varying privacy budget
ϵ, and 4 different values for u. In all settings, PM and HM
outperform Duchi et al.’s solution, and the performance gap
slightly expands with increasing ϵ, which agrees with our
analysis in Section IV. Finally, comparing PM and HM, the
difference in their performance is small, and the relative
performance of the two can be different in different settings.
Note that the main advantage of HM over PM is that on a
single numeric attribute, HM is never worse than Duchi et al.,
whereas PM does not have this guarantee.
We repeat the experiments on two additional synthetic
datasets with the same properties as the ﬁrst synthetic one,
except that their attribute values are drawn from different
distributions. One follows the uniform distribution where each
attribute value is sampled from [−1, 1] uniformly; the other
one follows the power law distribution where each attribute
value x is sampled from [−1, 1] with probability proportional
to c · (x + 2)−10. Fig. 6 presents the results, which lead
to similar conclusions as the results on real and Gaussian-
distributed data.
Lastly, Figs. 7 and 8 show the result accuracy in terms of
MSE with varying the number of users n and dimensionality
d on the MX dataset. Observe that more users and lower
dimensionality both lead to more accurate results, which
agrees with the theoretical analysis in Lemma 5. Meanwhile,
in all settings the proposed solutions consistently outperform
their competitors by clear margins. In the next subsection, we
omit the results for SCDF, which are comparable to that of
the Laplace mechanism.
B. Results on Empirical Risk Minimization
In the second set of experiments, we evaluate the accuracy
performance of the proposed methods for linear regression,
logistic regression, and SVM classiﬁcation on BR and MX.
For both datasets, we use the numeric attribute “total income”
as the dependent variable, and all other attributes as inde-
pendent variables. Following common practice, we transform
each categorical attribute Aj with k values into k −1 binary
attributes with a domain {0, 1}, such that (i) the l-th (l < k)
value in Aj is represented by 1 on the l-th binary attribute
and 0 on each of the remaining k −2 attributes, and (ii) the
k-th value in Aj is represented by 0 on all binary attributes.
After this transformation, the dimensionality of BR (resp. MX)
becomes 90 (resp. 94). For logistic regression and SVM, we
also covert “total income” into a binary attribute by mapping
the values larger than the mean value to 1, and 0 otherwise.
Since each user sends gradients to the aggregator, which
are all numeric, the experiment involves the 4 competitors in
Section VI-A for numeric data: PM, HM, Duchi et al. [14], and
the Laplace mechanism applied to each attribute independently
with equally split privacy budget (i.e., ϵ/d for each attribute).
Additionally, we also include the result in the non-private
setting. For all methods, we set the regularization factor
λ = 10−4. On each dataset, we use 10-fold cross validation 5
times to assess the performance of each method.
Fig. 9 and Fig. 10 show the misclassiﬁcation rate of each
method for logistic regression and SVM classiﬁcation, respec-
tively, with varying values of the privacy budget ϵ. Similar to
the results in Section VI-A, the Laplace mechanism leads to
signiﬁcantly higher than the other three solutions, due to the
fact that its error rate is sub-optimal. The proposed algorithms
PM and HM consistently outperform Duchi et al.’s solution
with clear margins, since (i) the former two have smaller
constant as analyzed in Section IV, and (ii) the gradient of
each user often consists of elements whose absolute values
are small, for which PM and HM are particularly effective,
as we mention in Section III-B. Further, in some settings
such as SVM with ϵ ≥2 on BR, the accuracy of PM and
HM approaches that of the non-private method. Comparing
the results with those in Section VI-A, we observe that
the misclassiﬁcation rates for logistic regression and SVM
classiﬁcation do not drop as quickly with increasing privacy
budget ϵ as in the case of MSE for mean values and frequency
estimates. This is due to the inherent stochastic nature of
SGD: that accuracy in gradients does not have a direct effect
on the accuracy of the model. For the same reason, there is
10


## Page 11


This full paper appears in the Proceedings of the IEEE 35th Annual International Conference on Data Engineering (ICDE),
held in April 2019.
Laplace
Duchi et al.
PM
HM
Non-private
 0.1
 0.15
 0.2
 0.25
 0.3
 0.35
 0.4
0.5
1
2
4
misclassification rate
privacy budget ε
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
1
2
4
misclassification rate
privacy budget ε
(a) BR
(b) MX
Fig. 9: Logistic Regression.
Laplace
Duchi et al.
PM
HM
Non-private
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
1
2
4
misclassification rate
privacy budget ε
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
1
2
4
misclassification rate
privacy budget ε
(a) BR
(b) MX
Fig. 10: Support Vector Machines (SVM).
no clear trend for the performance gap between PM/HM and
Duchi et al.’s solution.
Fig. 11 demonstrates the mean squared error (MSE) of
the linear regression model generated by each method with
varying ϵ. We omit the MSE results for the Laplace mecha-
nism, since they are far higher than the other three methods.
The proposed solutions PM and HM once again consistently
outperform Duchi et al.’s solution. Overall, our experimental
results demonstrate the effectiveness of PM and HM for empir-
ical risk minimization under local differential privacy, and their
consistent performance advantage over existing approaches.
VII. RELATED WORK
Differential privacy [16] is a strong privacy standard that
provides semantic, information-theoretic guarantees on indi-
viduals’ privacy, which has attracted much attention from var-
ious ﬁelds, including data management [8], [10], [27], machine
learning [4], theory [5], [13], [25], and systems [6]. Earlier
models of differential privacy [16], [17], [29] rely on a trusted
data curator, who collects and manages the exact private
information of individuals, and releases statistics derived from
the data under differential privacy requirements. Recently,
Laplace
Duchi et al.
PM
HM
Non-private
 1e-005
 0.0001
 0.001
 0.01
 0.1
 1
0.5
1
2
4
MSE
privacy budget ε
 0.0001
 0.001
 0.01
 0.1
 1
0.5
1
2
4
MSE
privacy budget ε
(a) BR
(b) MX
Fig. 11: Linear Regression.
much attention has been shifted to the local differential privacy
(LDP) model (e.g., [13], [25]), which eliminates the data
curator and the collection of exact private information.
LDP can be connected to the classical randomized response
technique in surveys [41]. Erlingsson et al. [18] propose
the RAPPOR framework, which is based on the random-
ized response mechanism for publishing a value for binary
attributes under LDP. They use this mechanism with a Bloom
ﬁlter, which intuitively adds another level of protection and
increases the difﬁculty for the adversary to infer private
information. A follow-up paper [19] extends RAPPOR to
more complex statistics such as joint-distributions and asso-
ciation testing, as well as categorical attributes that contain
a large number of potential values, such as a user’s home
page. Wang et al. [38] investigate the same problem, and
propose a different method: they transform k possible values
into a noisy vector with k elements, and send the latter
to curator. Bassily and Smith [5] propose an asymptotically
optimal solution for building succinct histograms over a large
categorical domain under LDP. Note that all of the above
methods focus on a single categorical attribute, and, thus, are
orthogonal to our work on multidimensional data including
numeric attributes. Ren et al. [34] investigate the problem
of publishing multiple attributes, and employ the idea of k-
sized vector, similar to [38]. This approach, however, incurs
rather high communication costs between the aggregator and
the users, since it involves the transmission of multiple k-sized
vectors. Duchi et al. [13] propose the minimax framework for
LDP based on information theory, prove upper and lower error
bounds of LDP-compliant methods, and analyze the trade-off
between privacy and accuracy. Besides, Kairouz et al. [24]
propose the extremal mechanisms, which are a family of
LDP mechanisms for data with discrete inputs, i.e., each
input domain X contains a ﬁnite number of possible values.
These mechanisms have an output distribution pdf with a key
property: for any input x ∈X and any output y, Pr[y | x]
has only two possible values that differ by a factor of exp(ϵ).
Kairouz et al. show that for any given utility measure, there
exists an extremal mechanism with optimal utility under this
measure, using a linear program with 2|X| variables. It is
unclear how to apply extremal mechanisms to continuous input
domains with an inﬁnite number of possible values, which is
the focus on this paper.
Various data analytics and machine learning problems have
been studied under LDP, such as probability distribution esti-
mation [15], [23], [30], [32], [42], heavy hitter discovery [4],
[7], [33], [39], frequent new term discovery [37], frequency
estimation [5], [38], frequent itemset mining [40], marginal
release [10], clustering [31], and hypothesis testing [20].
Finally, a recent work [3] introduces a hybrid model that
involves both centralized and local differential privacy. Bit-
tau et al. [6] evaluate real-world implementations of LDP.
Also, LDP has been considered in several applications includ-
ing the collection of indoor positioning data [26], inference
control on mobile sensing [28], and the publication of crowd-
sourced data [34].
11


## Page 12


This full paper appears in the Proceedings of the IEEE 35th Annual International Conference on Data Engineering (ICDE),
held in April 2019.
VIII. CONCLUSION
This work systematically investigates the problem of col-
lecting and analyzing users’ personal data under ϵ-local dif-
ferential privacy, in which the aggregator only collects ran-
domized data from the users, and computes statistics based on
such data. The proposed solution is able to collect data records
that contain multiple numerical and categorical attributes, and
compute accurate statistics from simple ones such as mean
and frequency to complex machine learning models such as
linear regression, logistic regression and SVM classiﬁcation.
Our solution achieves both optimal asymptotic error bound
and high accuracy in practice. In the next step, we plan to
apply the proposed solution to more complex data analysis
tasks such as deep neural networks.
ACKNOWLEDGMENT
This research was supported by National Natural Science
Foundation of China (61672475, 61433008), by Samsung via
a GRO grant, by the National Research Foundation, Prime
Minister’s Ofﬁce, Singapore under its Strategic Capability
Research Centres Funding Initiative, by Qatar National Re-
search Fund (NPRP10-0208-170408), and by Nanyang Tech-
nological University Startup Grant (M4082311.020). We thank
T. Nguyen for his contributions to an earlier version of this
work.
REFERENCES
[1] Integrated public use microdata series, 2017. https://www.ipums.org.
[2] Collecting
and
analyzing
multidimensional
data
with
local
differential
privacy
(technical
report),
2018.
https://sites.google.com/site/icde2019tr/tr.
[3] B. Avent, A. Korolova, D. Zeber, T. Hovden, and B. Livshits.
BLENDER: Enabling local search with a hybrid differential privacy
model. In USENIX Security Symposium, pages 747–764, 2017.
[4] R. Bassily, K. Nissim, U. Stemmer, and A. Thakurta. Practical locally
private heavy hitters. In NIPS, pages 2285–2293, 2017.
[5] R. Bassily and A. Smith. Local, private, efﬁcient protocols for succinct
histograms. In ACM STOC, pages 127–135, 2015.
[6] A. Bittau, U. Erlingsson, P. Maniatis, I. Mironov, A. Raghunathan,
D. Lie, M. Rudominer, U. Kode, J. Tinnes, and B. Seefeld. PROCHLO:
Strong privacy for analytics in the crowd. In ACM SOSP, pages 441–
459, 2017.
[7] M. Bun, J. Nelson, and U. Stemmer. Heavy hitters and the structure of
local privacy. In ACM PODS, pages 435–447, 2018.
[8] R. Chen, H. Li, A. K. Qin, S. P. Kasiviswanathan, and H. Jin. Private
spatial data aggregation in the local setting. In IEEE ICDE, pages 289–
300, 2016.
[9] G. Cormode, S. Jha, T. Kulkarni, N. Li, D. Srivastava, and T. Wang.
Privacy at scale: Local differential privacy in practice. In ACM SIGMOD
Tutorials, 2018.
[10] G. Cormode, T. Kulkarni, and D. Srivastava. Marginal release under
local differential privacy. In ACM SIGMOD, 2018.
[11] C. Cortes and V. Vapnik. Support-vector networks. Machine Learning,
20(3):273–297, 1995.
[12] B. Ding, J. Kulkarni, and S. Yekhanin.
Collecting telemetry data
privately. In NIPS, pages 3574–3583, 2017.
[13] J. C. Duchi, M. I. Jordan, and M. J. Wainwright. Local privacy and
statistical minimax rates. In IEEE FOCS, pages 429–438, 2013.
[14] J. C. Duchi, M. I. Jordan, and M. J. Wainwright.
Minimax optimal
procedures for locally private estimation.
Journal of the American
Statistical Association, 113(521):182–201, 2018.
[15] J. C. Duchi, M. J. Wainwright, and M. I. Jordan. Local privacy and
minimax bounds: Sharp rates for probability estimation. In NIPS, pages
1529–1537, 2013.
[16] C. Dwork, F. McSherry, K. Nissim, and A. Smith. Calibrating noise to
sensitivity in private data analysis. In TCC, pages 265–284, 2006.
[17] C. Dwork and A. Roth.
The algorithmic foundations of differential
privacy. Foundations and Trends in Theoretical Computer Science, 9(3-
4):211–407, 2014.
[18]
´U. Erlingsson, V. Pihur, and A. Korolova.
RAPPOR: Randomized
aggregatable privacy-preserving ordinal response. In ACM CCS, pages
1054–1067, 2014.
[19] G. Fanti, V. Pihur, and ´U. Erlingsson.
Building a RAPPOR with
the unknown: Privacy-preserving learning of associations and data
dictionaries. PoPETs, 2016(3):41–61, 2016.
[20] M. Gaboardi and R. Rogers. Local private hypothesis testing: Chi-square
tests. arXiv preprint arXiv:1709.07155, 2017.
[21] Q. Geng, P. Kairouz, S. Oh, and P. Viswanath. The staircase mechanism
in differential privacy. J. Sel. Topics Signal Processing, 9(7):1176–1184,
2015.
[22] J. Hamm, A. C. Champion, G. Chen, M. Belkin, and D. Xuan. Crowd-
ML: A privacy-preserving learning framework for a crowd of smart
devices. In IEEE ICDCS, pages 11–20, 2015.
[23] P. Kairouz, K. Bonawitz, and D. Ramage. Discrete distribution estima-
tion under local privacy. In ICML, 2016.
[24] P. Kairouz, S. Oh, and P. Viswanath. Extremal mechanisms for local
differential privacy. In NIPS, pages 2879–2887, 2014.
[25] S. P. Kasiviswanathan, H. K. Lee, K. Nissim, S. Raskhodnikova, and
A. Smith. What can we learn privately? In IEEE FOCS, pages 531–540,
2008.
[26] J. W. Kim, D.-H. Kim, and B. Jang. Application of local differential
privacy to collection of indoor positioning data. IEEE Access, 6:4276–
4286, 2018.
[27] S. Krishnan, J. Wang, M. J. Franklin, K. Goldberg, and T. Kraska.
PrivateClean: Data cleaning and differential privacy. In ACM SIGMOD,
pages 937–951, 2016.
[28] C. Liu, S. Chakraborty, and P. Mittal. DEEProtect: Enabling inference-
based access control on mobile sensing applications.
arXiv preprint
arXiv:1702.06159, 2017.
[29] F. McSherry and K. Talwar. Mechanism design via differential privacy.
In IEEE FOCS, pages 94–103, 2007.
[30] T. Murakami, H. Hino, and J. Sakuma.
Toward distribution estima-
tion under local differential privacy with small samples.
PoPETs,
2018(3):84–104, 2018.
[31] K. Nissim and U. Stemmer. Clustering algorithms for the centralized and
local models. In Algorithmic Learning Theory (ALT), pages 619–653,
Apr 2018.
[32] A. Pastore and M. Gastpar. Locally differentially-private distribution
estimation. In IEEE International Symposium on Information Theory
(ISIT), pages 2694–2698, 2016.
[33] Z. Qin, Y. Yang, T. Yu, I. Khalil, X. Xiao, and K. Ren. Heavy hitter
estimation over set-valued data with local differential privacy. In ACM
CCS, pages 192–203, 2016.
[34] X. Ren, C. M. Yu, W. Yu, S. Yang, X. Yang, J. A. McCann, and P. S.
Yu. LoPub: High-dimensional crowdsourced data publication with local
differential privacy. IEEE Transactions on Information Forensics and
Security, 13(9):2151–2166, Sept 2018.
[35] J. Soria-Comas and J. Domingo-Ferrer. Optimal data-independent noise
for differential privacy. Inf. Sci., 250:200–214, 2013.
[36] J. Tang, A. Korolova, X. Bai, X. Wang, and X. Wang. Privacy loss in
Apple’s implementation of differential privacy on macOS 10.12. arXiv
preprint arXiv:1709.02753, 2017.
[37] N. Wang, X. Xiao, Y. Yang, T. D. Hoang, H. Shin, J. Shin, and G. Yu.
PrivTrie: Effective frequent term discovery under local differential
privacy. In IEEE ICDE, 2018.
[38] T. Wang, J. Blocki, N. Li, and S. Jha.
Locally differentially private
protocols for frequency estimation. In USENIX Security, 2017.
[39] T. Wang, N. Li, and S. Jha. Locally differentially private heavy hitter
identiﬁcation. arXiv preprint arXiv:1708.06674, 2017.
[40] T. Wang, N. Li, and S. Jha. Locally differentially private frequent itemset
mining. In IEEE Symposium on Security and Privacy (S&P), 2018.
[41] S. L. Warner. Randomized response: A survey technique for eliminating
evasive answer bias. Journal of the American Statistical Association,
60(309):63–69, 1965.
[42] M. Ye and A. Barg. Optimal schemes for discrete distribution estimation
under local differential privacy. In IEEE International Symposium on
Information Theory (ISIT), pages 759–763, 2017.
12

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
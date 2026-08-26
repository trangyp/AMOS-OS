---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1802.02558v3
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1802.02558v3_Intentional_Control_of_Type_I_Error_over_Unconscious_Data_Distortion__a_Neyman-P

> Source: 1802.02558v3_Intentional_Control_of_Type_I_Error_over_Unconscious_Data_Distortion__a_Neyman-P.pdf

> Pages: 50

---


## Page 1


Intentional Control of Type I Error over Unconscious Data
Distortion: a Neyman-Pearson Approach to Text Classiﬁcation
Lucy Xia1, Richard Zhao2, Yanhui Wu3,5, and Xin Tong4,5
1Department of ISOM, School of Business and Management, Hong Kong University of Science and Technology.
2Department of Computer Science and Software Engineering, The Behrend College, The Pennsylvania State
University.
3Faculty of Business and Economics, University of Hong Kong; Department of Economics and Finance, University
of Southern California.
4Department of Data Sciences and Operations, Marshall School of Business, University of Southern California.
5To whom correspondence should be addressed. yanhuiwu@marshall.usc.edu, xint@marshall.usc.edu
Abstract
This paper addresses the challenges in classifying textual data obtained from open online
platforms, which are vulnerable to distortion. Most existing classiﬁcation methods minimize
the overall classiﬁcation error and may yield an undesirably large type I error (relevant textual
messages are classiﬁed as irrelevant), particularly when available data exhibit an asymmetry
between relevant and irrelevant information.
Data distortion exacerbates this situation and
often leads to fallacious prediction. To deal with inestimable data distortion, we propose the
use of the Neyman-Pearson (NP) classiﬁcation paradigm, which minimizes type II error under a
user-speciﬁed type I error constraint. Theoretically, we show that the NP oracle is unaﬀected by
data distortion when the class conditional distributions remain the same. Empirically, we study
a case of classifying posts about worker strikes obtained from a leading Chinese microblogging
platform, which are frequently prone to extensive, unpredictable and inestimable censorship. We
demonstrate that, even though the training and test data are susceptible to diﬀerent distortion
and therefore potentially follow diﬀerent distributions, our proposed NP methods control the
type I error on test data at the targeted level.
The methods and implementation pipeline
1
arXiv:1802.02558v3  [stat.ME]  16 Sep 2020


## Page 2


proposed in our case study are applicable to many other problems involving data distortion.
Keywords: text classiﬁcation, type I error, data distortion, censorship, social media, Neyman-
Pearson classiﬁcation paradigm
1.
INTRODUCTION
The rise of social media platforms has spurred the extensive use of large-scale textual data for both
academic and non-academic purposes. However, textual data on open digital platforms are suscep-
tible to manipulation, evident from the continuous debates about fake news, censorship, internet
trolls, and social bots [Woolley and Howard, 2016a,b]. Within an environment of data distortion,
the utilization of textual data for information collection (e.g., gauging public opinion) and event
discovery (e.g., monitoring social unrest) can be challenging. In the context of textual classiﬁca-
tion, this paper shows the powerlessness of existing classiﬁcation approaches to handling unknown
or inestimable data distortion. We then propose and illustrate the use of the recently developed
Neyman-Pearson (NP) classiﬁcation approach that aims to asymmetrically control classiﬁcation
errors [Cannon et al., 2002, Scott, 2005, Rigollet and Tong, 2011, Li and Tong, 2016, Tong et al.,
2018] in some common situations of data distortion, such as data obtained from censored Chinese
social media.
Since 2009 when Sina Weibo – the Chinese equivalent to Twitter – was launched, social media
have created an unprecedented informational shock to the Chinese society. Notably, Sina Weibo
enables millions of citizens to generate and communicate political information that is scarce in
traditional media.
Government agents, media outlets, NGOs and ﬁrms, and researchers have
invested heavily in machine learning techniques to mine the wealth of textual information circulated
on Sina Weibo [Economist, 2013, Center, 2013, 2014].
However, due to the potential eﬀect of
widespread political information on social unrest and regime stability, the Chinese government
extensively censors social media [Chen and Ang, 2011, King et al., 2013, 2014]. Such censorship
gives rise to two major challenges faced by data analysts in their endeavor of text mining. First,
although the Chinese government allows for relatively free information ﬂow on social media for the
purposes of surveillance and monitoring oﬃcials [Qin et al., 2017], censorship substantially reduces
the amount of information circulating on social media that can practically be used to classify data
2


## Page 3


and predict hidden social events. The objective of minimizing the overall classiﬁcation error, which
is used by most existing machine learning algorithms, can cause an undesirably large error of missing
important information. Second, social media censorship in China relies mostly on ad hoc human
manipulation to ﬁne-tune the extent of censorship in response to the changing local and temporal
social conditions ([Bamman et al., 2012, Zhu et al., 2013]).
This censorship strategy makes it
infeasible to infer the censorship rate. Thus, the traditional solution that corrects the potential
bias due to data truncation through a parametric estimation of the censorship rate is hardly a
practical choice. We propose the use of the NP classiﬁcation approach to precisely overcome these
two challenges.
To make our discussion more concrete, consider that a decision maker wishes to use social media
posts about political issues and social events to discover and monitor grass-root political actions
such as protests, petitions, or worker strikes. To this end, the decision maker must use algorithms
trained on labeled data to classify a large number of posts, i.e., to predict discrete outcomes (class
labels) for upcoming posts. In a binary classiﬁcation setting, a post is coded in {0, 1}, where class
0 means relevant to a speciﬁc topic, and class 1 means irrelevant. Two types of errors occur: type
I error (mislabel class 0 as class 1) and type II error (mislabel class 1 as class 0).1 The default
classiﬁcation objective in practice, which is referred to as the classical classiﬁcation paradigm in
this paper, is the one that minimizes the overall classiﬁcation error, which is a weighted sum of
type I and type II errors, with weights being the proportions of classes. When controlling one type
of error is dominantly important, a conﬂict occurs between the need for asymmetric control over
classiﬁcation errors and the neglect of such consideration in the overall classiﬁcation error. Data
distortion can exacerbate such a conﬂict. If a fraction of class 0 data is eliminated, then in the
objective function of the classical paradigm, the weight of type I error is reduced. Minimizing this
objective naturally increases type I error, which is undesirable when controlling type I error to
avoid overlooking relevant events is crucial to decision making.
In this paper, we ﬁrst derive the classical oracle classiﬁer (theoretically optimal classiﬁer under
the classical paradigm) regarding the post-distortion population, and then demonstrate that, with-
out precise knowledge about the data distortion rates, the pre-distortion classical oracle classiﬁer
1In the verbal discussion, type I and type II errors can also be thought of as the probability of making such errors.
3


## Page 4


cannot be recovered even if we have access to the entire post-distortion population. As a solution,
we propose to use the Neyman-Pearson classiﬁcation paradigm (NP paradigm) which minimizes
type II error under a user-speciﬁed type I error constraint. The NP paradigm has the advantage
that the NP oracle classiﬁer (theoretically optimal classiﬁer under the NP paradigm) is invariant
to the class size proportion in the population. This property guarantees the invariance of the NP
oracle under any distortion scheme as long as the class conditional distributions of the features
remain the same.
To bring our theoretical discussion to live, we focus on an exemplary case in the general setting
of Chinese social media, in which we classify a large number of posts about worker strikes published
on Sina Weibo. Accurately identifying strike events in a timely manner is highly valuable for many
decision makers, including governments, ﬁrms, and social scientists studying social movement. On
the other hand, as a type of collective action, posts about strikes are prone to censorship, the
extent of which varies across regions and over time. We show that applying existing classiﬁcation
methods leads to a considerable type I error, which can result in oversight or fallacious outcomes
in decision making. We then use an NP umbrella algorithm [Tong et al., 2018] in combination with
state-of-the-art machine learning techniques to classify the posts. Consistent with the NP oracle’s
invariance property to data distortion, we ﬁnd that even though the training and test data are
susceptible to diﬀerent distortion rates and are thus diﬀerently distributed, the NP classiﬁers hold
type I errors well controlled at the targeted level on the test data. Furthermore, we demonstrate
that for the purpose of controlling type I errors, the NP classiﬁcation methods allow decision makers
to borrow data generated in an information-abundant environment to classify data generated in an
information-scarce environment. This advantage is important when decision making is constrained
by time and resources.
Our study of data distortion is essentially an inquiry into the validity of statistical prediction
when the process of data generation is a primary concern. This concern is not dismissible even in
the era of big data. Instead, it can be exacerbated when data sources are vulnerable to human
intervention. One candidate solution to data distortion is to estimate and correct potential bias
by assuming precise knowledge regarding data generation and distortion. This is analogous to the
parametric estimation of censored or truncated data in classical statistical inference [Chung et al.,
4


## Page 5


1991]. Unfortunately, such a solution is infeasible when data are generated from diverse sources
and are aﬀected by complex interactions.
Another potential solution, which is popular in the
traditional statistics literature, is the development of sampling techniques that aim to obtain more
representative samples from the population [Luborsky and Rubinstein, 1995]. However, sampling
methods do not solve the data distortion problem in our study because even if the entire post-
distortion population were available, knowledge about the pre-distortion population is still limited
by unknown or inestimable distortion rates. In contrast, the NP classiﬁcation approach we propose
allows researchers to bypass one common kind of distortion which changes the class proportions
but not the class conditional feature distributions.
The setting in this paper might seem similar to domain adaptation [Ben-David et al., 2010,
Chen et al., 2011], a type of transfer learning. However, the data distortion problem in our study
diﬀers fundamentally from the problems studied in domain adaptation. In domain adaptation, a
key assumption is that the “source domain” and “target domain” share the same feature space, but
have diﬀerent feature distributions. A domain adaptation algorithm takes not only labeled data
from the source domain, but also data (labeled or unlabeled) from the target domain. In contrast,
the only available training data in our study are the labeled data from the post-distortion population
(i.e., the source domain) without using any data (regardless of being labeled or unlabeled) from
the pre-distortion population (i.e., the target domain). In this sense, the data-distortion problem
we address is more challenging because data from the target domain is not available. To overcome
such a challenge, the NP classiﬁcation approach invokes the assumption that the features have the
same conditional distributions in the source and target domains.
2.
CLASSIFICATION AND UNKNOWN DISTORTION SCHEME
Binary classiﬁcation is a supervised learning procedure frequently used in textual analysis. It aims
to classify a piece of textual message into a category that is relevant to either a speciﬁc purpose
or an irrelevant category. Formally, the aim of binary classiﬁcation is to accurately predict class
labels (i.e., Y = 0 or 1) for new observations (i.e., features X ∈Rd) on the basis of labeled training
data. For the rest of the discussion, we treat the relevant information category as class 0 and the
irrelevant one as class 1, so that missing a class 0 message is more consequential than missing a class
5


## Page 6


1 message. Concretely, let h : Rd →{0, 1} be a binary classiﬁer, R0(h) := IP(h(X) ̸= Y |Y = 0)
denote type I error, and R1(h) := IP(h(X) ̸= Y |Y = 1) denote type II error. Then, the (population)
classiﬁcation error R(h) can be decomposed as R(h) = R0(h) · IP(Y = 0) + R1(h) · IP(Y = 1) . We
use the term classical paradigm to refer to the learning objective of minimizing R(·). The classical
oracle classiﬁer, i.e., the classiﬁer that minimizes R(·) among all functions, is h∗(x) = 1I(η(x) > 1/2),
where η(x) = IE(Y |X = x) = IP(Y = 1|X = x). The classical oracle h∗is achievable only if the
entire population is available. In practice, we have to train a classiﬁer based on a ﬁnite sample.
2.1
Data Distortion Scheme
In this paper, we restrict our attention primarily to the type of distortion that changes the class
proportion of the population without changing the class conditional distributions of the features.
In other words, we assume that distortion changes IP(Y = 0) and IP(Y = 1), but does not change
the distributions of X|(Y = 0) or X|(Y = 1). The assumption that features have the same class-
conditional distributions is justiﬁed if the distortion scheme in the dataset (e.g., deleting sensitive
social media posts) is random. We will show that this assumption can be approximated by the data
distortion situation in our case study and other real world applications. We discuss more general
conditions in Appendix C.
2.2
Oracle under Data Distortion
Denote the class 0 distortion rate by β0 = β−
0 −β+
0 , where β−
0 is the class 0 downward-distortion rate
and β+
0 is the class 0 upward-distortion rate. These rates are the proportions of class 0 texts that
are randomly deleted or injected, respectively. For example, (β−
0 , β+
0 ) = (.2, .1) means 20% of class
0 texts are randomly deleted from the population, and 10% of class 0 texts are artiﬁcially injected,
so the net eﬀect is a β0 = 10% = 20% −10% decrease in class 0 texts. Since we cannot disentangle
the upward and downward forces just from the post-distortion population, we will formulate the
theory only on the net decrease eﬀect β0. Similarly, β1 is deﬁned for class 1. Below, we derive the
formula of the (classical) oracle classiﬁer regarding the post-distortion population.
Theorem 1. Let f0 and f1 denote the pre-distortion probability density functions of X|(Y = 0)
and X|(Y = 1), and π0 = IP(Y = 0) and π1 = IP(Y = 1) be the class priors.
Suppose the
distortion scheme does not change the distributions for X|(Y = 0) and X|(Y = 1) but only the
6


## Page 7


class proportions. Let β0 and β1 be the distortion rates of class 0 and class 1 respectively. Then,
the classical oracle classiﬁer regarding the pre-distortion population is
h∗(x) = 1I
f1(x)
f0(x) > π0
π1

,
and that regarding the post-distortion population is
h∗
(β0,β1)(x) = 1I
f1(x)
f0(x) > 1 −β0
1 −β1
· π0
π1

.
In this theorem, the explicit analytic form of the classical pre-distortion oracle classiﬁer h∗is a
well-known result, while that of h∗
(β0,β1) is new. See Appendix A for its proof. The thresholds of
f1/f0 in oracle classiﬁers h∗(pre-distortion) and h∗
(β0,β1) (post-distortion) diﬀer by a multiplicative
constant (1 −β0)/(1 −β1). This diﬀerence in thresholds reﬂects a change in the class proportions
in the population. If the entire post-distortion population is available, we can calculate the class
conditional densities f0 and f1 as well as the post-distortion class proportions
π(β0,β1)
0
=
(1 −β0)π0
(1 −β0)π0 + (1 −β1)π1
, π(β0,β1)
1
=
(1 −β1)π1
(1 −β0)π0 + (1 −β1)π1
.
Then, h∗
(β0,β1) can be recovered. However, there is no hope to recover or estimate h∗, unless β0 and
β1 are known or estimable.
2.3
Impact of Censorship Rate under the Gaussian Model
To visualize and quantify the result in Theorem 1, we study an example with β0 > 0 and β1 = 0
under a canonical linear discriminant analysis model. Let f0 ∼N(µ0, Σ) and f1 ∼N(µ1, Σ), where
µ0 and µ1 represent mean vectors for classes 0 and 1 respectively, and Σ is the common covariance
matrix. In this model, the decision boundary of the oracle h∗is
x⊤Σ−1(µ0 −µ1) −1
2(µ0 −µ1)⊤Σ−1(µ0 + µ1) + log
π0
π1

= 0 .
(1)
When only (1 −β0) proportion of observations from class 0 remains, the post-distortion oracle
classiﬁer h∗
β0 := h∗
(β0,0) has the following decision boundary:
x⊤Σ−1(µ0−µ1)−1
2(µ0−µ1)⊤Σ−1(µ0+µ1)+log
(1−β0)π0
π1

=0 .
(2)
7


## Page 8


Figure 1: The left panel shows the shift of the oracle decision boundary due to distortion under a linear discriminant
analysis model: µ0 = (0, 0)⊤, µ1 = (2, 2)⊤, Σ = I, π0 = .5. The horizontal axis and vertical axis are the two feature
measurements, and the contours represent diﬀerent density levels of each class. The black line is the original oracle
decision boundary; the red dashed line and the orange dashed line are the oracle decision boundaries after censorship
on class 0 with β0 = .5 and β0 = .95, respectively. The right panel plots type I error of h∗
β0 as a function of β0.
Comparing (1) and (2), the shape of the decision frontier remains the same, but the left hand
of the equations diﬀers by a constant log(1−β0). To visualize the diﬀerence in decision boundaries,
we plot an example in Figure 1. Proposition 1 below further explores the relationship between type
I error and the censorship rate of class 0 for balanced classes.
Proposition 1. Suppose the probability densities of class 0 (X|Y = 0) and class 1 (X|Y = 1)
follow distributions N(µ0, Σ) and N(µ1, Σ) respectively, and the two classes are balanced in the
pre-distortion population (i.e., π0 = π1 = .5).
Suppose that the censorship rate of class 0 is
β0 ∈(0, 1) and class 1 is not distorted (β1 = 0). To keep notations simple, let h∗
β0 = h∗
(β0,0) be the
classical oracle classiﬁer in the post-distortion population. Then, the type I error of h∗
β0 is:
R0(h∗
β0) = Φ
 
−1
2C −log (1 −β0)
√
C
!
,
(3)
where C = (µ0 −µ1)⊤Σ−1(µ0 −µ1). Clearly, R0(h∗
β0) increases with β0 ∈(0, 1).
Proposition 1 is proved in Appendix E. When censorship on class 0 texts intensiﬁes, class 0 in
the post-distortion population represents a smaller proportion, and the post-distortion oracle will
favor class 1 more, leading to a rise in type I error. Note that C captures the diﬃculty of the
8


## Page 9


classiﬁcation problem: the larger C, the better class separation, and the easier the classiﬁcation
problem.
3.
NEYMAN-PEARSON (NP) CLASSIFICATION PARADIGM
One existing solution to the problem of data distortion is to collect information so as to better
understand the data generation process.
For example, one might spend eﬀorts estimating the
distortion rates β0 and β1. However, such a solution is usually costly and practically infeasible.
Another idea is to adjust the weight placed on each of the two types of errors in the objective func-
tion of the classical classiﬁer. This is the cost-sensitive learning paradigm [Elkan, 2001, Zadrozny
et al., 2003], in which users impose diﬀerent costs to the two types of errors to address the issue of
asymmetric error importance. However, such a method does not solve the data distortion problem,
as discussed in Appendix B. To tackle the data distortion issue and type I error control objective
simultaneously, we propose to adopt the NP paradigm.
3.1
NP Oracle Invariant to Distortion
The NP oracle φ∗
α arises from the famous Neyman-Pearson Lemma in statistical hypothesis testing
(attached in Appendix F). Instead of minimizing R(h) = R0(h) · IP(Y = 0) + R1(h) · IP(Y = 1) as
in the classical paradigm, the NP classiﬁcation paradigm aims to mimic the NP oracle φ∗
α, where
φ∗
α = arg min
φ: R0(φ)≤α
R1(φ) ,
(4)
in which α is a user-speciﬁed upper bound on type I error. Under the NP classiﬁcation paradigm,
α reﬂects the level of a user’s conservativeness towards the type I error.
In some biomedical
applications, there is clear choice of α, such as .01 and .05, due to either government regulation
or common practice.
In social sciences applications, the choice of α is more subjective.
Some
suggestions in choosing α can be found in Tong et al. [2018].
The NP classiﬁcation paradigm has three advantages: i) bypass data distortion, ii) address the
class imbalance issue, and iii) control the more severe error type (typically, type I error) under a
user-speciﬁed level. The third advantage is self-evident; the ﬁrst two are illustrated as follows.
Theorem 2. Suppose that the distortion scheme does not change the distributions for X|(Y = 0)
9


## Page 10


and X|(Y = 1). The NP oracle classiﬁer φ∗
α deﬁned in (4) is invariant under distortion at various
rates β0 (on class 0) and β1 (on class 1), regardless of whether pre-distortion classes are balanced.
Theorem 2 (proof in Appendix A) implies that in an idealized situation when one has access
to the entire post-distortion population, he/she can reconstruct the NP oracle classiﬁer as if the
entire pre-distortion population is available. The rationale is that the NP oracle depends only on
the conditional distributions of X|(Y = 0) and X|(Y = 1) but not on the marginal distribution of
Y . This means that, as long as these conditional distributions do not change, the NP oracle will
stay the same.
Figure 2 illustrates the diﬀerence between a classical oracle classiﬁer and its NP counterpart
in both balanced and imbalanced Gaussian settings. While the classical oracles are diﬀerent, the
NP oracle is the same in both settings. As the type of data distortion in our study amounts to a
change in the class proportion, this ﬁgure also demonstrates a contrast between a shift in decision
boundary of the classical oracle and the invariance of the NP oracle under data distortion.
The main theoretical results, Theorem 1 and Theorem 2, do not require any parametric as-
sumptions. We only use parametric Gaussian examples as an illustration of these two theorems.
Speciﬁcally, we use Proposition 1 and Figures 1 and 2 to illustrate (1) the impact of data distortion
on classical oracles and (2) the invariance of the NP oracles to data distortion.
Theorem 2 suggests that, using samples from the post-distortion population, we can train
classiﬁers to mimic the pre-distortion NP oracle classiﬁer due to its invariance to distortion, and
thus bypass the need to estimate the data distortion scheme. Another key implication is that one
could train an NP classiﬁer on data from a distorted population with distortion rates β′
0 and β′
1
and test the classiﬁer on data from another distorted population with diﬀerent distortion rates β′′
0
and β′′
1. In other words, if the training and test data undergo diﬀerent censorship schemes, the
NP paradigm can still be applied. Regarding the practical implementation of the NP paradigm,
we will introduce the NP umbrella algorithm [Tong et al., 2018], which is compatible with all the
scoring-type classiﬁcation methods (e.g., logistic regression, support vector machines and random
forest), parametric or nonparametric.
In Appendix C, we discuss a situation in which the class conditional densities of features are
also changed by distortion. We derive the necessary and suﬃcient condition for the invariance
10


## Page 11


Figure 2: NP vs. Classical oracle classiﬁers in a Gaussian model example. The conditional distributions of X under
the two classes are N(0, 1) and N(2, 1) respectively. Suppose that a user prefers a type I error ≤α = .05. When
the two classes are balanced (i.e.,IP(Y = 0) = IP(Y = 1)), the classical oracle 1I(X > 1) that minimizes the risk
would result in a type I error = .159. On the other hand, the NP oracle 1I(X > 1.65) that minimizes the type II
error under the type I error constraint (≤.05) delivers the desirable type I error. In an imbalanced situation where
2IP(Y = 0) = IP(Y = 1), while the NP oracle does not change and retains the desirable type I error, the decision
boundary of the classical oracle shifts left to .6534 and results in a much larger type I error = .257.
property of the NP oracles in such a more general situation. Essentially, the general condition
requires that the post-distortion class conditional density ratio is a multiple of the pre-distortion
one, and that a good tail behavior is satisﬁed for the density ratios. We also construct concrete
examples showing that these abstract generalization conditions could materialize in common model
settings. Nevertheless, we choose to present the more-speciﬁc condition in Theorem 2 because it is
transparent and easy to interpret.
3.2
NP Umbrella Algorithm
To construct a classiﬁer under the NP paradigm, one can plug the class conditional feature densities
and the threshold estimates into the NP oracle classiﬁer suggested by the Neyman-Pearson Lemma
(Appendix F). Plug-in NP classiﬁers have been constructed in two settings: low-dimensional [Tong,
11


## Page 12


2013] and high-dimensional with independent features [Zhao et al., 2016]. However, plug-in proce-
dures suﬀer from the curse of dimensionality in more general high-dimensional settings. To make
the NP paradigm more practical, Tong et al. [2018] propose an NP umbrella algorithm, a wrapper
method that allows users to apply their favorite scoring-type classiﬁcation methods, such as logistic
regression, support vector machines, and random forests, under the NP paradigm. Figure 3 illus-
trates the pseudocode of the NP umbrella algorithm. This umbrella algorithm uses part of class 0
data and all class 1 data to train a scoring-function and use the left-out class 0 data to determine
a threshold for the scoring function. To use the algorithm, a user speciﬁes a desired upper bound
α for the (population) type I error and an upper bound for the type I error violation rate δ (i.e.,
the probability that type I error exceeds α). Proposition 2 and Corollary 1 provide a theoretical
warranty for the control of type I error using the classiﬁers constructed based on samples.
Proposition 2 (adapted from Tong et al. [2018]). Suppose that we divide the training data into
two parts, one with data from both classes 0 and 1 for training a base algorithm (e.g. svm, random
forest and etc.) to obtain f and the other as a left-out class 0 sample for choosing the threshold.
Applying f to the left-out class 0 sample of size n, we denote the resulting classiﬁcation scores as
T1, . . . , Tn, which are real-valued random variables. Then, we denote by T(k) the k-th order statistic
(i.e., T(1) ≤. . . ≤T(n)). For a new observation X, if we denote its classiﬁcation score f(X) as
T, we can construct classiﬁers ˆφk(X) = 1I(T > T(k)), k ∈{1, . . . , n}. Then, the population type I
error of ˆφk, denoted by R0(ˆφk), is a function of T(k) and hence a random variable, and it holds that
IP
h
R0(ˆφk) > α
i
≤
n
X
j=k
n
j

(1 −α)jαn−j .
(5)
That is, the probability that the type I error of ˆφk exceeds α is under a constant that only depends
on k, α and n. We call this probability the violation rate of ˆφk and denote its upper bound by
v(k) = Pn
j=k
 n
j

(1 −α)jαn−j.
Corollary 1. Suppose that the distortion scheme does not change the distributions for X|(Y = 0)
and X|(Y = 1). The NP umbrella algorithm (with M = 1) presented in Figure 3 yields a classiﬁer
ˆφ such that ˆφ has type I error violation rate controlled, i.e., IP(R0(ˆφ) ≤α) ≥1 −δ, and attains the
smallest type II error given a user-speciﬁed method.
12


## Page 13


1: input:
training data: a mixed i.i.d. sample S = S0 ∪S1, where S0 and S1 are class 0 and
class 1 samples respectively
α: type I error upper bound, 0 ≤α ≤1; [default α = 0.05]
δ: a small tolerance level, 0 < δ < 1; [default δ = 0.05]
M: number of random splits on S0; [default M = 1]
2: function RANKTHRESHOLD(n, α, δ)
3:
for k in {1, . . . , n} do
▷for each rank threshold candidate k
4:
v(k) ←Pn
j=k
 n
j

(1 −α)jαn−j
▷calculate the violation rate upper bound
5:
k∗←min {k ∈{1, . . . , n} : v(k) ≤δ}
▷pick the rank threshold
6:
return k∗
7: procedure NPCLASSIFIER(S, α, δ, M)
8:
n = ⌈|S0|/2⌉
▷denote half of the size of |S0| as n
9:
k∗←RANKTHRESHOLD(n, α, δ)
▷ﬁnd the rank threshold
10:
for i in {1, . . . , M} do
▷randomly split S0 for M times
11:
S0
i,1, S0
i,2 ←random split on S0
▷each time randomly split S0 into two halves with
equal sizes
12:
Si ←S0
i,1 ∪S1
▷combine S0
i,1 and S1
13:
S0
i,2 = {x1, . . . , xn}
▷write S0
i,2 as a set of n data points
14:
fi ←classification algorithm(Si)
▷train a scoring function fi on Si
15:
Ti = {ti,1, . . . , ti,n} ←{fi(x1), . . . , fi(xn)}
▷apply the scoring function fi to S0
i,2 to
obtain a set of score threshold candidates
16:

ti,(1), . . . , ti,(n)
	
←sort(Ti)
▷sort elements of Ti in an increasing order
17:
t∗
i ←ti,(k∗)
▷ﬁnd the score threshold corresponding to the chosen rank threshold k∗
18:
φi(X) = 1I (fi(X) > t∗
i ) ▷construct an NP classiﬁer based on the scoring function fi
and the threshold t∗
i
19: output:
an ensemble NP classiﬁer ˆφα(X) = 1I

1
M
PM
i=1 φi(X) ≥1/2

▷by majority vote
Figure 3: Pseudocode for the NP umbrella algorithm adapted from Tong et al. [2018] with permission.
Corollary 1 follows from Proposition 2. The proof of Corollary 1 can be brieﬂy described as
following. It is obvious that v(k) decreases as k increases. To choose from ˆφ1, . . . , ˆφn such that
a classiﬁer achieves minimal type II error with type I error violation rate less than or equal to a
user’s speciﬁed δ, the right order is
k∗= min {k ∈{1, . . . , n} : v(k) ≤δ} .
(6)
13


## Page 14


Notice that the NP umbrella algorithm does not guarantee the type II error to be close to the
oracle level, because it does not rely on assumptions of the distribution of (X, Y ) or the chosen
classiﬁcation method.
4.
CASE STUDY
We present a case study regarding how to classify posts about strike events in Chinese social
media. This case empirically illustrates the problem of unknown data distortion in text classiﬁcation
and the relevance of the NP classiﬁcation approach to real-world decision making. Moreover, we
demonstrate how to implement and assess various NP classiﬁcation methods so that researchers of
interest can adopt them.
Information regarding collective action events such as worker strikes and protests is important
for citizens’ participation in politics, policy implementation by governments, the accountability of
political leaders, and business decisions of ﬁrms. In authoritarian countries, however, this type
of information has been scarce in the public sphere because of strict government control over the
mass media. The emergence of social media enables citizens to circulate information about social
events and voice their opinions on political issues.
This has inspired local governments, non-
government organizations, ﬁrms and investors, and particularly social scientists to gather, decode
and analyze the information produced on social media in authoritarian countries. However, in their
endeavor to utilize information found on social media, these decision makers face the challenge of
data distortion caused by extensive censorship of social media information. The NP classiﬁcation
approach is intended to help make use of the limited set of useful information that remains on
social media to better discover and predict hidden social events.
In this section, we ﬁrst depict the Chinese government’s social media censoring strategy and
explain how it ﬁts the theoretical setup outlined in Section 2. Second, we describe our research
design and data collection.
Third, we detail the pipeline of data analysis including data pre-
processing, feature engineering, and the implementation of each NP classiﬁcation method. As a
preview, Figure 4 shows the entire chain of empirical analysis. Finally, we present the results in a
baseline sample and then in four augmented samples to further illustrate the advantage of the NP
classiﬁcation approach.
14


## Page 15


Figure 4: Illustration of the data processing pipeline with the pre-processing steps in the solid squares.
4.1
Data Distortion in Chinese Social Media
In China, social media are typically owned by private service providers. For example, Sina Weibo–
the microblogging platform in this study– is owned by Sina Corp., which is a company listed in
NASDAQ. However, the Chinese central government controls the infrastructure based on which the
social media platform operates and thus has the de facto right of censoring social media. Numerous
studies have documented that the Chinese government extensively censors social media information,
particularly political information that may undermine the leadership of the Chinese Communist
Party, trigger large-scale collective action, and cause social unrest ([Chen and Ang, 2011, King et al.,
2013, 2014]). Nevertheless, this does not mean that all politically sensitive information is censored.
Using a dataset of 13.2 billion posts published in Sina Weibo from 2009 to 2013, Qin et al. [2017]
document millions of posts published in Sina Weibo that discussed protests, demonstrations, strikes,
and corruption. Based on the posting activities of users who had published this politically sensitive
information, they conclude that the Chinese government allows for the circulation of some political
information on social media with an intention to encourage participation and collect information
for surveillance and monitoring local oﬃcials. Other studies ([Lorentzen, 2014, Qin et al., 2019])
suggest that the Chinese government’s strategy of censoring social media revolves around a trade-
oﬀbetween utilizing bottom-up information and avoiding accumulation and spread of information
that may scale up existing events (e.g., protests and strikes) or spur new action. Such a tradeoﬀ
leads to the following common censorship practice: information about small local social events is
not censored until a scale shift of information is detected ([Bamman et al., 2012, Zhu et al., 2013]).
In other words, when the quantity of sensitive information exceeds some threshold, censorship is
triggered.
15


## Page 16


Unlike in Russia where the manipulation of online information is mostly through the deployment
of bots to perform automated tasks, in China, censorship of social media is largely implemented
in an ad hoc manner. The threshold of censorship depends on local social and political conditions
([Chen and Ang, 2011, Bamman et al., 2012]). It is well known that during the period of Con-
gressional meetings or national celebration and in regions where social conﬂicts are pronounced,
the Chinese government tends to tighten censorship to contain potential social unrest. This ad
hoc censorship policy provides an explanation for the wide range of censorship rates estimated in
existing studies. ([Chen and Ang, 2011, Bamman et al., 2012, Fu et al., 2013]).
In practice, the censorship on Chinese social media involves three additional parties other than
the central government: (1) social media providers, private IT companies which implement censor-
ship, (2) government information oﬃcers who enforce the implementation of censorship, and (3)
local governments who ﬁnd ways to interfere with the operation of social media. These parties may
have diﬀerent objectives than the central government. For example, to maintain a high level of
information traﬃc, social media providers do not completely comply with the government’s censor-
ship demands. Moreover, the enforcement of censorship by government information oﬃcers is based
on ad hoc issuing of directives, depending on the involving oﬃcers’ collection and interpretation of
information ([Chen and Ang, 2011, Zhu et al., 2013]). Finally, although local governments do not
have the right to censor social media, they may bribe employees of social media providers to delete
information that may reﬂect negatively on them.
The above characteristics regarding censorship make the Chinese social media an ideal setting
to study the problem of classiﬁcation in the presence of data distortion and the NP classiﬁcation
methods as a solution to the problem. A decision maker who wishes to extract useful information
about certain issues or events from post-censorship social media posts faces the problem of data
distortion as we formulate in the previous sections. The quantity-based censorship suggests that
the features of information in the relevant class are likely to remain stable despite that censorship
signiﬁcantly reduces the quantity of this type of information. Therefore, the key assumption under
which the invariance property of the NP oracle classiﬁer is approximately true. Importantly, the
ad hoc nature of censorship and the involvement of multiple parties in its implementation render
the actual censorship scheme highly volatile and unpredictable. It is practically infeasible for a
16


## Page 17


decision maker to infer the rate of data distortion due to censorship.
4.2
Data Collection and Research Design
For this study, we collected public user posts related to sensitive social issues from the microblog-
ging site Sina Weibo. Through a third-party content crawling agency, we obtained a dataset of
approximately 10 million raw posts about public issues and social events in 2012. We are interested
in classifying posts about the subject “worker strikes.” We focus on strikes for several reasons.
First, the number of strikes in China has surged in the last decade, and strikes have become an
important form of worker movement ([Bulletin, 2012, 2018]). Accurately identifying strike events
in a timely manner is important for a wide range of decision makers, including governments, ﬁrms,
and social scientists. Second, as an indicator of collective action, posts about strikes are prone to
censorship. Third, the degree of censorship of posts about strikes varies across regions and over
time. For instance, censorship tends to be more intense towards the end of the year when workers’
yearly compensation is due and in regions where economic conditions are worse and unemployment
rates have increased. As explained below, this variation provides a partial test of the assumptions
that entail the application of our proposed NP classiﬁcation methods as well as an opportunity to
demonstrate the advantage of the NP classiﬁcation approach.
We extract a subset of posts ﬁltered according to a pre-selected list of keywords.2 This ﬁltering
generates 221, 229 posts linguistically relating to strikes. From this dataset, we extract a random
sample of 2, 500 posts that were published in the ﬁrst quarter of 2012 and were originated from
Guangdong – a coastal province where strike incidence occurred most frequently among all provinces
in China during the sample period. This sample serves as a baseline for our data analysis as well as
an illustration of various NP classiﬁcation methods. We then extract three random samples of the
same size (2, 500 posts) in the 2nd, 3rd, and 4th quarters of 2012 from Guangdong, respectively. We
will apply an NP classiﬁer trained in the baseline sample to these three samples in other periods.
Good performance (in terms of controlling type I error) of this classiﬁer across diﬀerent samples
provides suggestive evidence on the stable distribution of features in the presence of data distortion.
Finally, we select a random sample of 2, 500 posts from all the posts originated from three inland
2The ﬁlter for strike includes the following list of keywords, which commonly appear with the subject: “罢
工(worker strike)”, “工潮(worker strike)”,“罢市(shopkeeper strike)”, “罢课(class boycott)”, “罢驶(stop driving)”, “罢
驾(stop driving)”, “罢运(transportation worker strike)”.
17


## Page 18


provinces–Gansu, Qinghai, and Xinjiang–during the entire year of 2012. Evidence shows that these
three provinces were among regions where censorship on social media was most intense ([Bamman
et al., 2012]). Therefore, information that can be used to discover and predict strikes is expected to
be scarce in these provinces. Again, we will apply the NP classiﬁer trained in the baseline sample
to this non-Guangdong sample. If this classiﬁer performs well on the new sample, decision makers
can use a classiﬁer trained in an environment with relatively abundant information to overcome the
challenge of classiﬁcation in an information-scarce environment where labelling of posts is likely to
be much more costly and cannot be done in a timely manner. This is a potential advantage of the
NP classiﬁcation approach in its ability to transfer knowledge from one domain to another.
4.3
Data Pre-processing
We now describe how we process the unstructured raw Sina Weibo posts so that they can be fed to
learning algorithms. The ﬁrst step is to generate post labels. A decision maker’s interest is to learn
strike events which are a form of workers’ collective action and reﬂect ongoing social and economic
problems. Labeling posts according to the decision makers’ interest turns out to be non-trivial for
two reasons. First, in terms of substance, some posts related to strikes are about events in history or
in other countries without implications for current events. Second, linguistically, the word “strike”
is widely used in many diﬀerent contexts, literally and metaphorically. For example, in Chinese, in
the sentence “my computer / my cell phone is on strike,” “strike” means ”has stopped working.” In
the sentence “A person’s body / brain is on strike,” “strike” means “is not functioning normally.”
This type of linguistic ambiguity exists in many languages. We speciﬁed a set of rules to capture
these subtleties.
As a trial, we outsourced the labeling task to Amazon Mechanical Turk. Despite the active
responses, the label quality was subpar, having many errors and inconsistencies. Realizing the
diﬃculty of the task, we switched to expert labeling. We hired two Chinese-speaking experts to
manually categorize the raw posts into “strike related” (class 0) and “strike unrelated” (class 1).
Class 0 are posts about worker strikes, including student strikes, taxi driver strikes, and merchant
strikes, whereas class 1 posts contain the keyword “strike” but are using the word metaphorically
to describe the malfunctioning of computers, elevators or other objects.
After trial and error, the two experts achieved high quality and consistent labeling in several
18


## Page 19


trial samples. They then labeled the ﬁve aforementioned random samples: the baseline sample
(GD-Q1), the three other samples in Guangdong after the ﬁrst quarter in 2012 (GD-Q2, GD-Q3,
and GD-Q4), and the sample outside of Guangdong (NGD). Overall, among the 12, 500 posts
in these ﬁve samples, 3, 237 posts are labeled as “strike related” (Class 0) and 9, 263 as “strike
unrelated” (Class 1).
To decipher which Chinese characters form meaningful words, we apply The Stanford Segmenter
[Tseng et al., 2005], which uses a Chinese treebank (CTB) segmentation model and breaks down
input messages into disjointed words.
After removing non-meaningful stop words, we create a
dictionary of unique words and generate a frequency matrix that counts the number of times each
word appears in each post, based on the dictionary. The strikes matrix, containing 12, 500 rows
(posts) and 34, 968 columns (features), is used to engineer features in topic modeling.
4.4
Feature Engineering
In the pre-processed strikes dataset, the size of vocabulary dictionaries is much larger than the
number of posts. This high-dimensional problem can be handled with various techniques. For
example, one can use marginal screening methods such as sure independence screening [Fan and
Lv, 2008], nonparametric independence screening [Fan et al., 2011] and the Kolmogorov-Smirnov
(KS) test, interaction screening methods [Hao and Zhang, 2014, Fan et al., 2015], the forward
stepwise selection, shrinkage methods such as LASSO [Tibshirani, 1996] and SCAD [Fan and Li,
2001], or dimension reduction methods such as principal component analysis.
These methods, however, all overlook the semantic structures possessed by corpora datasets.
Thus, we adopt Latent Dirichlet Allocation (LDA) [Blei et al., 2003, Teh et al., 2007, Grimmer
and Stewart, 2013], which is a popular generative probabilistic model designed for large corpora.
In this model, documents (posts) are represented as random mixtures over latent topics and each
topic is represented as a distribution over words. We train the LDA model using the R package
topicmodels and select “Gibbs sampling” as the ﬁtting method. With a pre-determined K, we
extract K topics that serve as new features. The posterior distribution over these K topics in each
document will be the feature values.
19


## Page 20


4.5
Results
In this subsection, we present the main results of the analysis which follows the pipeline depicted
in Figure 4.
Alongside the results, we discuss their real-world implications.
We also address
several nuanced technical issues that are important for the implementation of classiﬁcation methods,
hoping to provide quantitative social scientists some implementation guidelines to analyze their
classiﬁcation problems in various empirical settings.
4.5.1.
Topic Modelling
In the use of LDA for feature engineering, specifying the number of topics K is essential. We
use a stability criterion to select K. Concretely, for a candidate K, we randomly select half of the
posts to apply LDA. This process is repeated 50 times. Every time, LDA outputs K topics. Each
document is represented by posterior probabilities over these K topics, and each topic is represented
by posterior probabilities over the vocabulary dictionary. We look at the top 20 keywords that have
the largest posterior probabilities in each of the K topics. Based on these words, we decide whether
a topic is truly related to the subject. We consider the number of topics K to be suitable if over
50 repetitions, the proportions of relevant topics have low variance. For illustrative purpose, we
compare K = 5 and K = 10.
Table 1 lists the top 20 keywords for each topic in one repetition when K = 10, using the
entire dataset of 12,500 strike posts.
Even a casual reader (of the Chinese characters or their
corresponding English translation) will recognize the 4th, 6th and 10th topics as about actual
worker strikes. In particular, the 4th topic is mostly about students boycotting classes, evident
from the keywords “school,” “student,” “teacher,” “student strike,” and “demonstration.” The 6th
topic is about worker strikes in ﬁrms, evident from the keywords “company,” “employee,” “wage,”
“protest,” “collective,” “factory,” and “staﬀ.” The 10th topic is about strikes in the transportation
sector, evident from the keywords “strike,” “driver,” “vehicle,” “taxi,” “public transportation,”
“collective,” “road,” “bus,” and “traﬃc.” The remaining 7 topics are irrelevant.
Thus, in this
repetition, the proportion of relevant topics is 3/10. Over the 50 repetitions, we calculated the
variances of these proportions. In this regard, K = 5 and 10 output variances .0037 and .0018
respectively. By the stability criterion, we prefer K = 10 .
20


## Page 21


One interesting observation is that, for a diﬀerent choice of K, the feature words in a speciﬁc
topic may contain diﬀerent information. For example, the topic regarding “strikes in the trans-
portation sector (topic 10 in Table 1)” appears both when K = 5 and when K = 10. In addition
to relating to the subject, the topic keywords also contain information about the location of the
events, which is valuable for decision making. However, when K = 5, only one location “汕头”
(Shantou) appears as a feature in the selected topic; whereas when K = 10, two locations, “汕头”
(Shantou) and “江门” (Jiangmen), appear. To investigate the cause of this diﬀerence, we manually
read through the 2, 500 posts we selected from GD-Q1. Of them, 230 posts are about strikes in
“Shantou” and 161 posts are about strikes in “Jiangmen.” We suspect that it is the relatively low
frequency of “Jiangmen” that makes it vanish as a feature in the selected topic when K = 5. Thus,
choosing a larger K may have the advantage of capturing a greater amount of valuable information.
In the remaining part of the paper, we set K = 10 unless otherwise speciﬁed.
It should be noted that, in this study, we choose K = 5 or K = 10 simply for an illustrative
purpose. Practitioners can select a set of desirable K’s based on their domain knowledge, time
constraint, and ﬁnancial budget.
4.5.2.
NP Classiﬁcation in the Baseline Sample
Fixing K = 10 in LDA, we apply both the classical and NP classiﬁcation algorithms to the
baseline dataset GD-Q1. The NP algorithms are implemented through the R package nproc (also
available in Python). To better demonstrate the performance of NP classiﬁers, we implement three
settings.
• Setting 1: We randomly split GD-Q1 into training and test sets of equal sizes (half of class 0
and half of class 1 data in training) 100 times. Hence, the class 0 proportion in a training set
is the same as that in a test set. We set NP parameters: α = .2 and δ = .3.
• Setting 2: We randomly split class 0 data into three folds of equal sizes, and split class 1 data
into two halves. We take 1/3 (one fold) class 0 data and 1/2 class 1 data as the training set
and use the other 2/3 class 0 data and the other half class 1 data as the test set. Thus, the
class 0 proportion in the training set is half as much as in the test set. We again repeat the
experiment 100 times. We set NP parameters: α = .2 and δ = .3.
21


## Page 22


topic 1
去
今天
吃
明天
做
上班
爱
睡觉
今晚
偷笑
go
today
eat
tomorrow
do
work
love
sleep
tonight
smirk
下午
然后
鼻屎
挖
回来
回家
睡
买
晚上
累
afternoon afterwards
mucus
pick
come back
go home
sleep
buy
night
tired
topic 2
罢工
电脑
手机
打
发现
居然
电话
突然
开
发
strike
computer
cellphone
beat
realize
surprisingly
telephone
sudden
open
send
换
最近
直接
结果
系统
部
问题
彻底
博
家里
change
recently
directly
consequence
system
part
problem
thoroughly
broad
home
topic 3
罢工
天
说
现在
小
点
今天
后
下
三
strike
day
speak
now
small
bit
today
after
down
three
前
真的
早上
知道
去
分钟
走
思考
一直
真是
before
really
morning
know
go
minute
walk
think
always
indeed
topic 4
年
工人
罢课
中国
上
月
工会
游行
政府
老师
year
worker
student strike
China
previous
month
union
demonstration
government
teacher
学生
学校
美国
国家
生活
组织
人民
中
领导
举行
student
school
United States
country
life
organization
people
in
leader
hold
topic 5
能
让
可以
时候
没有
还是
这个
种
上
觉得
can
let
may
time
none
still
this
plant
up
feel
希望
出来
里
工作
身体
感觉
太阳
还有
出
一定
hope
come out
inside
work
body
feel
Sun
still
out
deﬁnitely
topic 6
公司
员工
事件
工资
工作
抗议
对
罢市
中
发生
company
employee
event
wage
work
protest
right
shopkeeper strike
in
happen
新闻
集体
问题
三
分享
月日
工厂
人员
新
政府
news
collective
problem
three
share
month-date
factory
staﬀ
new
government
topic 7
罢工
抓
狂
泪
系
今日
可怜
地
生病
衰
strike
clutch
crazy
tear
be
today
pity
ground
sick
unfortunate
抓狂
泪泪
天气
委屈
话
鄙视
住
空调
搞到
甘
go crazy
tears
weather
be wronged
word
despise
reside
air-conditioner
get
this
topic 8
罢工
想
人
玩
哈哈
事
找
为什么
心情
回复
strike
think
human
play
haha
thing
ﬁnd
why
mood
reply
汗
看到
伤心
事情
很多
闹钟
放假
二
个人
双
sweat
see
sad
thing
many
alarm clock
holiday
two
individual
pair
topic 9
罢工
次
开始
时间
过
已经
终于
最后
继续
嘻嘻
strike
time
begin
time
pass
already
ﬁnally
at last
continue
LOL
第一
对
周
所有
下
第二
机场
地方
草草
完全
ﬁrst
right
week
all
down
second
airport
place
hasty
completely
topic 10
罢工
司机
车
出租车
的士
公交
集体
小时
汕头
路
strike
driver
car
taxi
taxi
public transportation collective
hours
Shantou
road
钱
没有
回
公交车
江门
半
交通
事
全部
广州
money
none
back
bus
Jiangmen
half
traﬃc
thing
all
Guangzhou
Table 1: top 20 keywords for ten topics from one repetition on the entire strikes dataset. The English translation
of some keywords in Topic 7 are based their Cantonese meaning.
22


## Page 23


• Setting 3: The same as in Setting 1, except that we now set NP parameters: α = .1 and
δ = .3.
In each training set, we run LDA (K = 10) and construct a transformed training set which
utilizes the learned topics as new features and the posterior probabilities over these topics as
feature values.
We then train classiﬁers based on the transformed training datasets.
Type I
and type II errors are calculated using the corresponding transformed test set. The classiﬁcation
methods implemented include the classical versions of penalized logistic regression (PLR), naive
bayes (NB), support vector machines (SVM), random forest (RF) and sparse linear discriminant
analysis (sLDA), together with their NP counterparts with corresponding parameters (e.g., α = .2
and δ = .3 for Setting 1 and Setting 2; α = .1 and δ = .3 for Setting 3).
Table 2 summarizes the average type I and type II errors in Setting 1 using the above classiﬁ-
cation methods under the classical approach (odd columns) and the NP approach (even columns,
named with a preﬁx NP) over all 100 repetitions. Notably, all the classical methods produce a large
type I error and a small type II error, with Naive Bayes being the most extreme one, where the
type I error is 1. This is in part caused by the relatively large size of Class 1 in the training dataset.
By contrast, all NP methods successfully control the type I error within the target level, while pro-
ducing a larger type II error than that of the classical methods. This means that a decision maker
using the NP methods can more accurately discover true information about strike events at the
cost of screening some extra irrelevant information. In the current study, missing a strike-related
post (class 0) may lead to delayed government responses, oversight in business decisions, and under-
estimates of the strike incidence frequency in social studies. It is particularly costly when a hidden
event may compound into a large scale issue and spread to other regions. Generally, a decision
maker cares more about type I error than type II error. The larger type II error associated with
the NP classiﬁers implies that an excessive amount of irrelevant information has been collected and
another round of screening may be needed. The cost of such further screening appears insigniﬁcant
[Qin et al., 2017]. Overall, the NP classiﬁer is preferable in many real-world applications.
Table 3 summarizes the average type I and type II errors in Setting 2, in which the class
0 proportion in the training set is half as much as its proportion in the test set. This mimics
the real life scenario when censorship of the more-sensitive information is tightened, resulting
23


## Page 24


Error rates
PLR
NP-PLR
NB
NP-NB
SVM
NP-SVM
RF
NP-RF
sLDA
NP-sLDA
type I
.914
.196
1
.193
.816
.179
.684
.184
.825
.194
type II
.005
.427
0
.482
.014
.598
.047
.502
.014
.423
Table 2: Average error rates with α = .2, δ = .3 for the strike dataset over 100 repetitions, under Setting 1.
Error rates
PLR
NP-PLR
NB
NP-NB
SVM
NP-SVM
RF
NP-RF
sLDA
NP-sLDA
type I
.965
.184
1
.183
.918
.166
.822
.169
.872
.185
type II
.002
.498
0
.571
.005
.732
.023
.588
.010
.494
Table 3: Average error rates with α = .2, δ = .3 for the strike dataset over 100 repetitions, under Setting 2.
in more scarce relevant information (a smaller class 0) in the observed data. According to our
previous theoretical discussion, such more stringent censorship would shift the decision boundary
of the classical oracle classiﬁer more drastically, worsening type I error of the classical classiﬁcation
methods.
For example, PLR produces a type I error of .965, which is larger than .914 – its
counterpart in Setting 1. By contrast, the NP oracle is unaﬀected by data distortion, and NP-PLR
has a type I error controlled below the pre-speciﬁed α = .2 in both Setting 1 and Setting 2. This
phenomenon is consistent across all the ﬁve methods we implemented.
Table 4 summarizes the average type I and type II errors of these methods in Setting 3, which
is the same as in Setting 1 except that we now use a new set of parameters α = .1, δ = .3. This
second set of parameters is chosen to represent a scenario when decision makers face a higher cost
of missing a strike event and wish to impose more stringent control over type I error. Tables 2
and 4 demonstrate that, across diﬀerent NP classiﬁers, type I errors are uniformly controlled under
the target level. In particular, when the upper bound of type I error is reduced from (α = .2)
to (α = .1), type I errors of the NP classiﬁers are reduced below the new target level .1. These
observations suggest that the NP methods provide an instrument for decision makers to ﬁne-tune
the target level of type I errors according to circumstances.
In summary, the parameters α and δ in NP classiﬁcation methods govern the trade-oﬀbetween
type I and type II errors, and the balance of this trade-oﬀdepends on the decision maker’s objective
and resources available. In the strikes example, the consequence of making type I errors is severe –
it could threaten government stability, jeopardize a politician’s career, or mislead business decisions,
whereas the cost of dealing with type II errors is small. Considering this preference for controlling
24


## Page 25


Error rates
PLR
NP-PLR
NB
NP-NB
SVM
NP-SVM
RF
NP-RF
sLDA
NP-sLDA
type I
.912
.095
1
.089
.824
.084
.690
.083
.826
.097
type II
.006
.659
0
.733
.014
.806
.047
.740
.014
.651
Table 4: Average error rates with α = .1, δ = .3 for the strike dataset over 100 repetitions, under Setting 3.
type I error, together with the data distortion problem, it is highly valuable to use classiﬁcation
methods under the NP paradigm rather than under the classical paradigm. In Appendix D, we
also demonstrate how sparsity-inducing methods, such as NP-sLDA, help select meaningful topics,
so that our approach achieves both good prediction performance and good interpretability.
4.5.3.
Knowledge Transfer: NP Classiﬁers across Datasets
In practice, decision makers often need to make decisions quickly. This time constraint some-
times restricts the amount of information available for developing predictive algorithms. For in-
stance, a decision maker wants to assess the work conditions of a region (e.g., province) in April
using social media posts. However, the number of relevant posts may be too small to train an
eﬀective classiﬁer, or there might not be enough time and resources to hire experts to label posts.
If this decision maker could use a classiﬁer trained with data collected in the ﬁrst quarter of the
year, his or her learning would be more eﬃcient and timely. Similarly, in a region where information
related to worker strikes is scarce because of extensive censorship or limited supply, data analysis
based on machine learning will beneﬁt substantially from information collected in other regions
with less censorship or more information supply.
The above discussion conveys the notion of knowledge transfer, which is implied by the invariance
property of the NP classiﬁcation paradigm.
We now examine its validity empirically.
We use
classiﬁers trained on all posts in the baseline sample (GD-Q1) to classify posts in other datasets
(GD-Q2, GD-Q3, GD-G4, and NGD). From the previous section (recall Tables 2, 3 and 4), we ﬁnd
that NP-sLDA performs the best among all methods we compared in terms of type II errors. Thus,
in this section, we focus on NP-sLDA only. In Table 5, we ﬁrst present the results with parameters
α = .1 and δ = .3. Note that the type I errors are slightly larger than the target control level
α = .1. Nevertheless, this does not mean the failure of applying the classiﬁers trained in GD-Q1
because some regional and time-varying features are speciﬁc to a dataset and cannot be used for
25


## Page 26


Error rates
Guangdong-Q2
Guangdong-Q3
Guangdong-Q4
non-Guangdong
type I
.133
.141
.109
.106
type II
.558
.563
.516
.533
Table 5: Average error rates with α = .1, δ = .3 for posts from GD-Q2, GD-Q3, GD-Q4 and NGD.
learning in other datasets. For example, “ 汕头” (Shantou) is a prefecture in Guangdong province
where taxi-driver strikes occurred multiple times in the ﬁrst quarter of 2012, and thus this locality
appeared as a pronounced feature in topics selected from the baseline dataset. Unless the strike
events in this locality lasted for a long period and became national, we would not expect it to
appear as an important feature for data from samples in other periods or from non-Guangdong
provinces. In other words, we expect that the underlying populations over time or in diﬀerent
regions are not identical.
Being aware of the above learning barrier caused by features that are speciﬁc to a particular
sample, we propose to have a smaller tolerance level to control the desirable type I error.
In
particular, we trained the classiﬁer using (α = .1, δ = .05). Table 6 presents the results under this
new criterion. In contrast to the results in Table 5, the type I error is now well controlled under
the target level .1.
The above results demonstrate that, armed with NP classiﬁers, a decision maker, who is con-
strained by available information and time, can leverage information collected from previous periods
or in circumstances where useful information was not severely censored. Of course, this knowledge
transfer is feasible only if the post-censorship feature distributions remain suﬃciently stable across
datasets. Therefore, the results in Tables 5 and 6 provide suggestive evidence that censorship does
not distort feature distributions that are important for the algorithm’s learning process. In other
words, the assumption that warrants the invariance property of the NP oracle classiﬁer is partially
justiﬁable in the current empirical setting, although this assumption is not directly testable because
uncensored data are not available. As mentioned in the introduction, our practice of using the NP
algorithm to handle the data distortion problems diﬀers from any existing practice in domain adap-
tation in that we do not use any data (labeled or unlabeled) on the target domain in the algorithm
training process.
26


## Page 27


Error rates
Guangdong-Q2
Guangdong-Q3
Guangdong-Q4
non-Guangdong
type I
.094
.100
.087
.078
type II
.642
.654
.622
.611
Table 6: Average error rates with α = .1, δ = .05 for posts from GD-Q2, GD-Q3, GD-Q4 and NGD.
NP-PLR
NP-NB
NP-SVM
NP-RF
NP-sLDA
Error rates
GD-Q1
GD-ALL
GD-Q1
GD-ALL
GD-Q1
GD-ALL
GD-Q1
GD-ALL
GD-Q1
GD-ALL
type I
.095
.094
.089
.093
.084
.090
.083
.091
.097
.093
type II
.659
.420
.733
.491
.806
.587
.740
.476
.651
.425
Table 7: Average error rates using NP-methods with α = .1, δ = .3 over 100 repetitions. A comparison between
using GD-Q1 and all data from Guangdong.
4.5.4.
Knowledge Accumulation: NP Classiﬁers with Enlarged Training Data
In reality, a decision maker often accumulates information from the past. In view of the invari-
ance property of the NP methods, this accumulated information can be used to facilitate learning if
the feature distributions remain stable. We illustrate this point in the current case study. We ﬁrst
repeat Setting 3 using all posts from the Guangdong province, and compare the results with those
in Table 4. In the comparison (presented in Table 7), GD-Q1 recollects the results in Table 4, and
GD-ALL reports the results obtained from information in Guangdong over the entire four quarters.
Clearly, when we use the larger dataset, the type II error decreases, while the type I error remains
under control at .1. Furthermore, we include all posts from Guangdong as the training data, and
test on the NGD dataset. We keep the parameters (α = .1, δ = .05) the same for comparison with
Table 6. Table 8 shows that, with type I error under control using NP-sLDA, the larger size of
the training data decreases the type II error one would achieve on the posts from non-Guangdong,
even if the underlying population distributions in the GD and NGD datasets can be diﬀerent.
5.
CONCLUSION
Digital texts have become an important source of data for social scientists. With increasing sophis-
tication in text mining to discover social events and to predict social behaviors, accurate classiﬁ-
cation of textual data for speciﬁc purposes is key to successful empirical analysis. However, while
a wide range of textual analysis and machine learning techniques have been introduced into the
27


## Page 28


Error rates
trained over GD-Q1 only
trained over all data from GD
type I
.078
.059
type II
.611
.407
Table 8: Average error rates with α = .1, δ = .05 for posts from NGD, using classiﬁer NP-sLDA trained on GD-Q1
only and trained on all data from GD (including GD-Q1, GD-Q2, GD-Q3 and GD-Q4), respectively.
social sciences [Grimmer and Stewart, 2013, Wilkerson and Casas, 2017, Gentzkow et al., 2017], the
problem of data distortion has received relatively little attention. Being a fundamental data gener-
ation issue in statistical analysis, data distortion can cause serious problems in sampling, inference,
and prediction. The current paper is among the ﬁrst eﬀorts to study data distortion problems in
the context of classifying large-scale textual data. Theoretically, we show that in the presence of
unknown data distortion, the classical oracle classiﬁer cannot be recovered even when the entire
post-distortion population is available. By contrast, the NP oracle classiﬁer is unaﬀected by data
distortion. Practically, we study a case in which a decision maker classiﬁes posts about worker
strikes obtained from Sina Weibo – a leading Chinese microblogging platform that is subject to
government censorship. We demonstrate that when one type of classiﬁcation error (e.g., type I
error) is dominantly important, the NP classiﬁcation algorithms allow users to control that type of
error below a pre-speciﬁed level. Although our problem setup involves the distortion parameters,
our objective is not to estimate them, but to bypass the estimation needs for prediction purpose.
In other words, we target a prediction problem rather than an inference problem. Our approach
is to construct classiﬁers under the NP paradigm, and the theoretical underpinning behind this
construction is the invariance property of the NP oracle classiﬁer. It is important to note that
the NP classiﬁcation approach we propose is not speciﬁc to text classiﬁcation. Instead, it can be
used to handle more-general classiﬁcation problems in the big data era when classiﬁcation errors
are asymmetric in importance. Plausible applications include control of epidemic diseases, crime
detection, social surveillance, and monitoring risky ﬁnancial decisions, among many others.
ACKNOWLEDGEMENT
The authors would like to thank the editor, associate editor, two statistical content referees and
the referee for reproducibility, for many constructive comments which have greatly improved the
paper. We would also like to thank Professor Jingyi Jessica Li for rounds of thoughtful discussions
28


## Page 29


and suggestions, and the seminar participants at UCLA. This work was partially supported by
National Science Foundation grant NSF DMS 1613338.
29


## Page 30


REFERENCES
Samuel C. Woolley and Philip N. Howard. Automation, algorithms, and politics. international
journal of communication. International Journal of Communication, 10:4882–4890, 2016a.
Samuel C. Woolley and Philip N. Howard. Social media, revolution, and the rise of the political
bot. Handbook of Media, Conﬂict, and Security, 2016b.
A. Cannon, J. Howse, D. Hush, and C. Scovel. Learning with the neyman-pearson and min-max
criteria. Technical Report LA-UR-02-2951, 2002.
C. Scott. Comparison and design of neyman-pearson classiﬁers. Unpublished, 2005.
P. Rigollet and X. Tong.
Neyman-pearson classiﬁcation, convexity and stochastic constraints.
Journal of Machine Learning Research, 12:2831–2855, 2011.
Jingyi Jessica Li and Xin Tong.
Genomic applications of the neyman–pearson classiﬁcation
paradigm. In Big Data Analytics in Genomics, pages 145–167. Springer, 2016.
Xin Tong, Yang Feng, and Jingyi Li. Neyman-Pearson (NP) Classiﬁcation algorithms and NP
receiver operating characteristic (NP-ROC) curves. Science Advances, page eaao1659, 2018.
Economist. China’s internet: A giant cage. The Economist, 2013.
China Internet Network Information Center. The 32nd statistical report on internet development
in china. 2013.
China Internet Network Information Center. The 33rd statistical report on internet development
in china. 2014.
Xiaoyan Chen and Peng Hwa Ang. Internet police in china: Regulation, scope and myths. Online
Society in China: Creating, Celebrating, and Instrumentalising the Online Carnival, pages 40–52,
2011.
Gary King, Jennifer Pan, and Margaret E Roberts. How censorship in china allows government
criticism but silences collective expression. American Political Science Review, 107(2):326–343,
2013.
30


## Page 31


Gary King, Jennifer Pan, and Margaret E Roberts. Reverse-engineering censorship in china: Ran-
domized experimentation and participant observation. Science, 345(6199):1251722, 2014.
Bei Qin, David Str¨omberg, and Yanhui Wu. Why does china allow freer social media? protests
versus surveillance and propaganda. The Journal of Economic Perspectives, 31(1):117–140, 2017.
David Bamman, Brendan O’Connor, and Noah Smith. Censorship and deletion practices in chinese
social media. First Monday, 17(3), 2012.
Tao Zhu, David Phipps, Adam Pridgen, Jedidiah R Crandall, and Dan S Wallach. The velocity of
censorship: High-ﬁdelity detection of microblog post deletions. In USENIX Security Symposium,
pages 227–240, 2013.
Ching-Fan Chung, Peter Schmidt, Ann D. Witte, and Ana D. Witte. Survival analysis: A survey.
Journal of Quantitative Criminology, 7(1):59–98, 1991.
Mark R. Luborsky and Robert L. Rubinstein. Sampling in qualitative research: Rationale, issues,
and methods. Research on aging, 17(1):89–113, 1995.
Shai Ben-David, John Blitzer, Koby Crammer, Alex Kulesza, Fernando Pereira, and Jennifer Wort-
man Vaughan. A theory of learning from diﬀerent domains. Machine Learning, 79:151–175, 2010.
Minmin Chen, Kilian Q. Weinberger, and John Blitzer. Co-training for domain adaptation. Ad-
vances in neural information processing systems, pages 2456–2464, 2011.
C. Elkan. The foundations of cost-sensitive learning. In Proceedings of the Seventeenth International
Joint Conference on Artiﬁcial Intelligence, pages 973–978, 2001.
B. Zadrozny, J. Langford, and N. Abe.
Cost-sensitive learning by cost-proportionate example
weighting. IEEE International Conference on Data Mining, page 435, 2003.
Xin Tong. A plug-in approach to neyman-pearson classiﬁcation. Journal of Machine Learning
Research, 14:3011–3040, 2013.
Anqi Zhao, Yang Feng, Lie Wang, and Xin Tong. Neyman-Pearson classiﬁcation under high di-
mensional settings. Journal of Machine Learning Research, 17(213):1–39, 2016.
31


## Page 32


Peter Lorentzen. China’s strategic censorship. American Journal of Political Science, 58(2):402–
414, 2014.
Bei Qin, David Stromberg, and Yanhui Wu. Social media and protests in china. Working paper,
2019.
King-wa Fu, Chung-hong Chan, and Michael Chau. Assessing censorship on microblogs in china:
Discriminatory keyword analysis and the real-name registration policy. IEEE Internet Comput-
ing, 17(3):42–50, 2013.
China Labour Bulletin. A decade of change: the workers’ movement in china 2000–2010. Hong
Kong: China Labour Bulletin, 2012.
China Labour Bulletin. The workers’ movement in china: 2015–2017. Hong Kong: China Labour
Bulletin, 2018.
Huihsin Tseng, Pichuan Chang, Galen Andrew, Daniel Jurafsky, and Christopher Manning. A
conditional random ﬁeld word segmenter for sighan bakeoﬀ2005. In Proceedings of the fourth
SIGHAN workshop on Chinese language Processing, 2005.
Jianqing Fan and Jinchi Lv. Sure independence screening for ultrahigh dimensional feature space
(with discussion). J. Roy. Statist. Soc., Ser. B: Statistical Methodology, 70(5):849–911, 2008.
Jianqing Fan, Yang Feng, and Rui Song. Nonparametric independence screening in sparse ultra-
high-dimensional additive models. Journal of the American Statistical Association, 106(494):
544–557, 2011. doi: 10.1198/jasa.2011.tm09779. URL https://doi.org/10.1198/jasa.2011.
tm09779. PMID: 22279246.
Ning Hao and Hao Helen Zhang. Interaction screening for ultrahigh-dimensional data. Journal of the
American Statistical Association, 109(507):1285–1301, 2014. doi: 10.1080/01621459.2014.881741.
URL https://doi.org/10.1080/01621459.2014.881741.
Yingying Fan, Yinfei Kong, Daoji Li, and Zemin Zheng. Innovated interaction screening for high-
dimensional nonlinear classiﬁcation. Ann. Statist., 43(3):1243–1272, 06 2015. URL https://
doi.org/10.1214/14-AOS1308.
32


## Page 33


Robert Tibshirani. Regression shrinkage and selection via the lasso. J. Roy. Statist. Soc., Ser. B,
58:267–288, 1996.
Jianqing Fan and Runze Li. Variable selection via nonconcave penalized likelihood and its oracle
properties. J. Amer. Statist. Assoc., 96(456):1348–1360, 2001.
David M Blei, Andrew Y Ng, and Michael I Jordan. Latent dirichlet allocation. Journal of machine
Learning research, 3(Jan):993–1022, 2003.
Yee W Teh, David Newman, and Max Welling. A collapsed variational bayesian inference algorithm
for latent dirichlet allocation. In Advances in neural information processing systems, pages 1353–
1360, 2007.
Justin Grimmer and Brandon M Stewart. Text as data: The promise and pitfalls of automatic
content analysis methods for political texts. Political analysis, 21(3):267–297, 2013.
John Wilkerson and Andreu Casas. Large-scale computerized text analysis in political science:
Opportunities and challenges. Annual Review of Political Science, 20:529–544, 2017.
Matthew Gentzkow, Bryan T Kelly, and Matt Taddy. Text as data. Technical report, National
Bureau of Economic Research, 2017.
33


## Page 34


A.
PROOFS
A.1
Proof of Theorem 1
Proof. Recall that the (classical) oracle classiﬁer regarding the pre-distortion population is h∗(x) =
1I(η(x) > 1/2), where the regression function η(x) = IE(Y |X = x) can be calculated as
η(x) =
π1f1(x)/f0(x)
π1f1(x)/f0(x) + π0
.
Therefore, h∗(x) = 1I

f1(x)
f0(x) > π0
π1

. When distortion with rates β0 and β1 is applied to class 0 and
class 1 respectively, the class proportions become π(β0,β1)
0
and π(β0,β1)
1
which are deﬁned as
π(β0,β1)
0
=
(1 −β0)π0
(1 −β0)π0 + (1 −β1)π1
,
π(β0,β1)
1
=
(1 −β1)π1
(1 −β0)π0 + (1 −β1)π1
,
while class conditional densities remain f0 and f1. Then, the oracle classiﬁer regarding the post-
distortion population is to replace π0 and π1 in h∗by π(β0,β1)
0
and π(β0,β1)
1
respectively:
h∗
(β0,β1)(x) = 1I
 
f1(x)
f0(x) > π(β0,β1)
0
π(β0,β1)
1
!
= 1I
f1(x)
f0(x) > 1 −β0
1 −β1
· π0
π1

.
A.2
Proof of Theorem 2
Proof. The constrained optimization program (4) in the main text that deﬁnes φ∗
α does not involve
the class priors π0 = IP(Y = 0) and π1 = IP(Y = 1), so φ∗
α does not depend on π0 or π1. Now
suppose distortion with rates β0 and β1 is imposed on class 0 and class 1 respectively, then the
post-distortion population have class 0 proportion [(1 −β0)π0]/[(1 −β0)π0 + (1 −β1)π1] and class 1
proportion [(1 −β1)π1]/[(1 −β0)π0 + (1 −β1)π1], while keeping the distributions of X|(Y = 0) and
X|(Y = 1) unchanged. Since distortion at rates β0 and β1 only changes class proportion, which
NP oracle does not depend upon, the NP oracle is invariant under distortion.
34


## Page 35


B.
COST-SENSITIVE (CS) LEARNING
An insight from studying the classical classiﬁcation paradigm is that the relative size of classiﬁcation
errors comes largely from the relative weights placed on type I and type II errors in the objective
function. So a natural candidate to adjust classiﬁcation errors is to change the weights. This is the
so-called cost-sensitive (CS) learning paradigm, in which users impose costs C0 and C1 to type I and
type II errors, respectively. On the population level, instead of minimizing the overall classiﬁcation
error R(·), one minimizes the CS learning objective:
min
h Rc(h) := C0π0R0(h) + C1π1R1(h) ,
(A.1)
or the following variant of (A.1):
min
h R¯c(h) := C0R0(h) + C1R1(h) .
(A.2)
Then, the CS oracle classiﬁer hc∗under the cost-sensitive learning paradigm (A.1) can be calculated
by
hc∗(x) = 1I
f1(x)
f0(x) > C0
C1
· π0
π1

,
and the CS oracle h¯c∗under (A.2) can be calculated by
h¯c∗(x) = 1I
f1(x)
f0(x) > C0
C1

.
Similar to its counterpart in the classical paradigm, the post-distortion CS oracle classiﬁer is
diﬀerent from the pre-distortion CS oracle, and the pre-distortion CS oracle cannot be recovered
in view of an unknown distortion scheme. Lemma 1 follows from arguments similar to the proof of
Theorem 1 in the main text.
Lemma 1. Suppose that X|(Y = 0) and X|(Y = 1) have probability density functions f0 and f1,
and that class priors are π0 and π1 respectively. Let β0 and β1 be the distortion rates of class 0 and
class 1 respectively. Then, the oracle classiﬁer under the cost-sensitive learning paradigm (A.1)
35


## Page 36


regarding the post-distortion population is
hc∗
(β0,β1)(x) = 1I
f1(x)
f0(x) > 1 −β0
1 −β1
· C0
C1
· π0
π1

.
Similarly, the oracle classiﬁer under the paradigm (A.2) regarding the post-distortion population is
h¯c∗
(β0,β1)(x) = 1I
f1(x)
f0(x) > 1 −β0
1 −β1
· C0
C1

.
Lemma 1 implies that even if we have the entire post-distortion population, we can only mimic
hc∗
(β0,β1) or h¯c∗
(β0,β1). However, unless β0 and β1 are known or estimable, there is no hope to mimic
hc∗or h¯c∗.
C.
ORACLE CLASSIFIERS WHEN WE RELAX THE FIXED CLASS CONDITIONAL
DENSITIES ASSUMPTION
Proposition 3. Suppose that pre-distortion, X|(Y = 0) and X|(Y = 1) have probability density
functions f0 and f1, and that class priors are π0 = IP(Y = 0) and π1 = IP(Y = 1). Let β0 and β1
be the distortion rates of class 0 and class 1 respectively. Further suppose that the post-distortion
class conditional densities of features are f′
0 and f′
1. Then, the classical oracle classiﬁer regarding
the pre-distortion population is
h∗(x) = 1I
f1(x)
f0(x) > π0
π1

,
and that regarding the post-distortion population is
h∗′
(β0,β1)(x) = 1I
f′
1(x)
f′
0(x) > 1 −β0
1 −β1
· π0
π1

.
The proof is omitted due to its similarity to that for Theorem 1 in the main text. Note that
when f′
1/f′
0 = f1/f0, that is when the ratio of class conditional densities of features is preserved
under data distortion, the post-distortion classical oracle classiﬁer h∗′
(β0,β1)(x) reduces to h∗
(β0,β1)(x)
in Theorem 1, even if the class conditional densities themselves are changed. On the other hand,
without assuming any relations between pre and post distortion feature distributions, f1/f0 cannot
be recovered.
36


## Page 37


The invariance property (Theorem 2 in the main text) of Neyman-Pearson (NP) oracle classiﬁers
no longer holds in general when the class conditional densities of features are diﬀerent pre and post
distortion. The next proposition illustrates suﬃcient and necessary conditions under which this
invariance property does hold for a ﬁxed α.
Proposition 4. Denote pre-distortion distributions of X|(Y = 0) and X|(Y = 1) by f0 and f1 and
those post-distortion by f′
0 and f′
1. When f′
1/f′
0 = a · (f1/f0) and
a · min{C ∈R : IPf0(f1(X)/f0(X) > C) ≤α} = min{C ∈R : IPf′
0(f′
1(X)/f′
0(X) > C) ≤α} ,
for some a > 0, the NP oracle classiﬁer φ∗
α deﬁned in (4) in the main text is invariant under
distortion at various rates β0 (on class 0) and β1 (on class 1), regardless of whether pre-distortion
classes are balanced. Moreover, these conditions are also necessary for the invariance property.
Proof. From the NP Lemma, it is easy to see that the two conditions are suﬃcient for the invariance
property of the NP oracles. For the necessary part, again by the NP lemma, the NP oracles pre
and post distortion can be written respectively as
φ∗
α(x) = 1I(f1(x)/f0(x) > Cα), and φ∗′
α (x) = 1I(f′
1(x)/f′
0(x) > C′
α) ,
for some constants Cα and C′
α as determined in the NP Lemma. In other words,
Cα = min{C ∈R : IPf0(f1(X)/f0(X) > C) ≤α} ,
C′
α = min{C ∈R : IPf′
0(f′
1(X)/f′
0(X) > C) ≤α} .
Since Cα and C′
α are constants, to have φ∗
α(x) = φ∗′
α (x), it is necessary to have f′
1/f′
0 = a·(f1/f0)
for some positive constants a, and this further demands C′
α = a · Cα.
Note that in general, the constant a in Proposition 4 depends on α.
In the following, we
demonstrate that within certain distribution classes, the more general condition in Proposition 4
falls back to the special case of unchanged class conditional feature distributions, while in others,
there are a ̸= 1 cases where class conditional feature distributions are diﬀerent pre and post
37


## Page 38


distortion.
Case I: Exponential Distribution Assume that f0(x) = λ0e−λ0x, f1(x) = λ1e−λ1x; f′
0(x) =
λ′
0e−λ′
0x, f′
1(x) = λ′
1e−λ′
1x, where x > 0. For identiﬁability concern, let us assume λ0 < λ1, λ′
0 < λ′
1.
Then,
f1(x)
f0(x) = λ1
λ0
e−(λ1−λ0)x ,
and
f′
1(x)
f′
0(x) = λ′
1
λ′
0
e−(λ′
1−λ′
0)x .
When we demand
f′
1(x)
f′
0(x) = a · f1(x)
f0(x)
∀x ,
it follows that
λ1 −λ0 = λ′
1 −λ′
0 ,
(A.3)
and
λ′
1
λ′
0
= a · λ1
λ0
.
(A.4)
Note that
Pf0
f1(X)
f0(X) > C

=
Pf0
λ1
λ0
e−(λ1−λ0)X > C

=
Pf0

e−(λ1−λ0)X > λ0
λ1
C

=
Pf0

X < −
1
λ1 −λ0
ln
λ0
λ1
C

=
1 −exp

−λ0 ·

−
1
λ1 −λ0
ln
λ0
λ1
C

=
1 −
λ0
λ1
C

λ0
λ1−λ0 .
To choose the minimum C such that Pf0

f1(X)
f0(X) > C

≤α, we get
Cα = λ1
λ0
(1 −α)
λ1−λ0
λ0
.
38


## Page 39


Similarly,
C′
α = λ′
1
λ′
0
(1 −α)
λ′
1−λ′
0
λ′
0
.
Then the condition a · Cα = C′
α implies that
a · λ1
λ0
(1 −α)
λ1−λ0
λ0
= λ′
1
λ′
0
(1 −α)
λ′
1−λ′
0
λ′
0
.
(A.5)
For any given 0 < α < 1, combining three equations (A.3), (A.4) and (A.5) implies that
(1 −α)
1
λ0 = (1 −α)
1
λ′
0 ,
which implies that λ0 = λ′
0. And then, λ1 = λ′
1 and a = 1. Therefore, we have shown that when the
class conditional feature distributions are restricted to the exponential distributions, the invariant
property only occurs when f0 = f′
0 and f1 = f′
1.
Case II: Gaussian Distribution Assume that f0 : N(µ0, σ2), f1 : N(µ1, σ2), f′
0 : N(µ′
0, σ′2),
and f′
1 : N(µ′
1, σ′2), where µ0 < µ1, µ′
0 < µ′
1, and σ ̸= σ′. Then,
f1(x)
f0(x) = exp
2(µ1 −µ0)x + µ2
0 −µ2
1
2σ2

and
f′
1(x)
f′
0(x) = exp
2(µ′
1 −µ′
0)x + µ′2
0 −µ′2
1
2σ′2

.
To obtain
f′
1(x)
f′
0(x) = a · f1(x)
f0(x) ,
the parameters µ0, µ1, σ, µ′
0, µ′
1, σ′, a must satisfy
2(µ1 −µ0)
2σ2
= 2(µ′
1 −µ′
0)
2σ′2
,
(A.6)
and
a = exp
µ′2
0 −µ′2
1
2σ′2
−µ2
0 −µ2
1
2σ2

.
39


## Page 40


Furthermore, denote by Φ(·) the cumulative distribution function of standard normal distribution,
Cα = minC
n
C ∈R : Pf0

f1(X)
f0(X) > C

≤α
o
and C′
α = minC
n
C ∈R : Pf′
0
 f′
1(X)
f′
0(X) > C

≤α
o
.
Pf0
f1(X)
f0(X) > C

=
Pf0

exp
2(µ1 −µ0)X + µ2
0 −µ2
1
2σ2

> C

=
Pf0
 2(µ1 −µ0)X + µ2
0 −µ2
1 > 2σ2 ln C

=
Pf0

X > 2σ2 ln C + µ2
1 −µ2
0
2(µ1 −µ0)

=
Pf0
X −µ0
σ
> 2σ2 ln C + (µ1 −µ0)2
2(µ1 −µ0)σ

.
Based on Pf0

f1(X)
f0(X) > C

≤α, we get
Φ−1(1 −α) ≤2σ2 ln C + (µ1 −µ0)2
2(µ1 −µ0)σ
,
where Φ−1(·) is the inverse function of Φ(·), that is,
C ≥exp
2σ(µ1 −µ0)Φ−1(1 −α) −(µ1 −µ0)2
2σ2

.
Therefore,
Cα = exp
2σ(µ1 −µ0)Φ−1(1 −α) −(µ1 −µ0)2
2σ2

.
Similarly,
C′
α = exp
2σ′(µ′
1 −µ′
0)Φ−1(1 −α) −(µ′
1 −µ′
0)2
2σ′2

.
From the relationship a · Cα = C′
α, we can obtain
µ′2
0 −µ′2
1
2σ′2
−µ2
0 −µ2
1
2σ2
+ 2σ(µ1 −µ0)Φ−1(1 −α) −(µ1 −µ0)2
2σ2
=
2σ′(µ′
1 −µ′
0)Φ−1(1 −α) −(µ′
1 −µ′
0)2
2σ′2
,
(A.7)
40


## Page 41


i.e.,
µ′2
0 −µ′2
1
2σ′2
+ (µ′
1 −µ′
0)2
2σ′2
−µ2
0 −µ2
1
2σ2
−(µ1 −µ0)2
2σ2
=
(µ′
1 −µ′
0)Φ−1(1 −α)
σ′
−(µ1 −µ0)Φ−1(1 −α)
σ
,
which is equivalent to,
µ′
0(µ′
0 −µ′
1)
σ′2
−µ0(µ0 −µ1)
σ2
=
(µ′
1 −µ′
0)
σ′
−(µ1 −µ0)
σ

Φ−1(1 −α) .
(A.8)
From equation (A.6)
µ′
1 −µ′
0
σ′
= σ′
σ2 (µ1 −µ0) .
(A.9)
Putting (A.9) into (A.8),
(µ0 −µ1)
σ2
(µ′
0 −µ0) =
 σ′
σ2 (µ1 −µ0) −(µ1 −µ0)
σ

Φ−1(1 −α) ,
that is,
Φ−1(1 −α) = µ0 −µ′
0
σ′ −σ .
Putting the above arguments together, we have shown that under Gaussian distributions, for a
given α ∈(0, 1), the invariance property is satisﬁed precisely when
(µ1 −µ0)
σ2
= (µ′
1 −µ′
0)
σ′2
,
Φ−1(1 −α) = µ0 −µ′
0
σ′ −σ ,
and
a = exp
µ′2
0 −µ′2
1
2σ′2
−µ2
0 −µ2
1
2σ2

.
Example of Case II: Let f0 : N(0, 22), f1 : N(1, 22) and f′
0 : N(−4, 42), and f′
1 : N(0, 42).
41


## Page 42


We show that when α = 0.023, the invariant property holds. First, it is easy to check that the
above three equations hold with these density speciﬁcations and the choice of α. In the following,
we provide an alternative direct proof.
Note that
f1(x)
f0(x) = exp
2x −1
8

,
and
f′
1(x)
f′
0(x) = exp
8x + 16
32

,
Hence,
f′
1(x)
f′
0(x) = exp
5
8

· f1(x)
f0(x) .
We can take a = exp
 5
8
	
. Let α = 0.023. Then Φ−1(1 −α) = 2. We solve for Cα and C′
α from
Pf0
f1(X)
f0(X) > Cα

= α
and
Pf′
0
f′
1(X)
f′
0(X) > C′
α

= α .
That is,
Pf0

exp
2X −1
8

> Cα

= α
and
Pf′
0

exp
8X + 16
32

> C′
α

,
Or equivalently,
Pf0

X > 8 ln Cα + 1
2

= α
and
Pf′
0
 X > 4 ln C′
α −2

= α .
That is,
(8 ln Cα + 1)/2
2
= 2
and
4 ln C′
α −2 −(−4)
4
= 2,
which implies that
Cα = exp
7
8

and
C′
α = exp
3
2

.
Obviously,
a · Cα = C′
α ,
42


## Page 43


i.e.,
a · min
C

C ∈R : Pf0
f1
f0
> C

≤α

= min
C

C ∈R : Pf′
0
f′
1
f′
0
> C

≤α

.
Therefore, we have constructed a concrete NP oracle invariant example in which f0 ̸= f′
0 and
f1 ̸= f′
1.
D.
SPARSITY-INDUCING METHODS IN SELECTING MEANINGFUL TOPICS
Among the implemented methods, NP-sLDA performs the best in terms of power and it is a
penalized sparsity-inducing method, which means it eliminates certain unimportant features as
part of the classiﬁer training process. In this section, we elaborate that such methods are eﬀective
in terms of selecting meaningful topics. In particular, we look at results from the ﬁrst two random
repetitions under Setting 1 in Section 4.5.2 (random seed being set and results are readily available
online) with K = 10.
In the ﬁrst repetition, Table 9 displays the selected ten topics and it’s
obvious that only topics 4 and 10 are the strike-related topics. Following the common practice
of NP umbrella algorithms, we randomly split the training data M times for training the scoring
function and thresholds. Here we use M = 7, and the ﬁnal classiﬁer is a majority vote. Figure 5
shows that, over the seven splits, NP-sLDA consistently selects only topics 4 and 10, and all the rest
of the topics have corresponding coeﬃcient 0. Similarly, in repetition 2, Table 10 shows that only
topics 5 and 6 are the strike-related topics, and Figure 6 shows that NP-sLDA consistently selects
topics 5 and 6 over the 7 splits. In summary, these sparsity-inducing methods, such as NP-sLDA,
help select meaningful topics.
E.
PROOF AND GENERALIZATION OF PROPOSITION 1 IN MAIN TEXT
Proposition 1 in the main text follows as a special case of the next Proposition. Proposition 5
below explores the relationship between type I error R0(·), the distortion rate β0 of class 0 and the
class size ratio π0/π1 for the classical post-distortion oracle classiﬁer h∗
β0,π0.
Proposition 5. Suppose probability densities of class 0 (X|Y = 0) and class 1 (X|Y = 1) follow
distributions N(µ0, Σ) and N(µ1, Σ) respectively; class 0 composes π0 ∈(0, 1) proportion of the
population and β0 ∈(0, 1) is the censorship rate of class 0 (i.e., the proportion of class 0 posts that
were removed from some government censorship scheme). Suppose class 1 is not distorted (i.e.,
43


## Page 44


topic 1
罢工
终于
学校
时间
一下
事件
彻底
哼哼
开
对
strike
ﬁnally
school
time
a bit
event
complete
humph
open
right
电话
集体
分钟
失望
胃
为了
好多
疑问
多少
忙
phone
collective
minute
disappoint
stomach
for
many
question
how many
busy
topic 2
罢工
今天
上班
发生
年
上
发现
问题
种
衰
strike
today
work
happen
year
go
discover
problem
type
decline
回来
太阳
话
公交车
宿舍
冷
块
过节
东西
思考
come back
Sun
words
bus
dorm
cold
block
festival
things
think
topic 3
人
让
说
吃
时候
事
罢课
过
哈哈
小
people
let
speak
eat
time
thing
student strike
pass
haha
small
里
妈妈
老师
今晚
去
很多
找
出门
最近
班
inside
mom
teacher
tonight
go
many
ﬁnd
go out
recent
class
topic 4
年
公司
员工
中
工人
工作
工资
最后
月
鄙视
year
company
employee
within
worker
work
salary
ﬁnally
month
despise
小时
后
广州
抗议
今日
知道
请
月日
要求
中国
hour
after
Guangzhou
protest
today
know
please
month-date
request
China
topic 5
抓
狂
罢工
电脑
泪
早上
现在
抓狂
天气
回家
clutch
crazy
strike
computer
tear
morning
now
go crazy
weather
go home
想
潮湿
下午
结果
集
继续
部
修
人
委屈
think
moist
afternoon
result
gather
continue
department
ﬁx
people
be wronged
topic 6
罢工
去
做
次
能
生病
地
系
偷笑
没有
strike
go
do
times
can
sick
ground
systems
smirk
without
睡觉
鼻屎
挖
第一
今晚
怒
回
真的
叫
汗
sleep
mucus
pick
ﬁrst
tonight
angry
back
real
shout
sweat
topic 7
天
手机
还是
知道
能
竟然
突然
说
玩
这个
day
cellphone
still
know
can
unexpectedly
suddenly
say
play
this
出来
换
已经
点
郁闷
鼓掌
听
一下
真是
好不容易
out
exchange
already
bit
depressed
applaud
listen
a bit
really
hard
topic 8
罢工
想
可怜
居然
买
发
明天
累
点
但是
strike
think
pity
unexpectedly
buy
give
tomorrow
tired
bit
but
星期
然后
休息
家里
半
悲伤
一直
本来
听说
心情
week
therefore
rest
home
half
sad
always
originally
heard
mood
topic 9
罢工
草草
明天
可以
开始
好好
真的
新闻
爱
开
strike
hastily
tomorrow
can
start
nicely
really
news
love
open
心情
点
还有
刚刚
这个
之后
一定
为什么
晚
上午
mood
a bit
also
just
this
after
must
why
evening
morning
topic 10
的士
汕头
出租车
司机
现在
车
罢工
打
下
辆
taxi
Shantou
taxi
driver
now
car
strike
call
get oﬀ
vehicle
营运
三
原因
政府
集体
今日
希望
四
市民
月日
operate
three
reason
government
collective
today
hope
four
citizen
month-date
Table 9: top 20 keywords for the ten topics selected from repetition 1.
44


## Page 45


(Intercept)   2.526526 
x1            .        
x2            .        
x3            .        
x4           -5.914467 
x5            .        
x6            .        
x7            .        
x8            .        
x9            .        
x10         -19.521468 
 
 (Intercept)   2.286663 
x1            .        
x2            .        
x3            .        
x4           -5.279157 
x5            .        
x6            .        
x7            .        
x8            .        
x9            .        
x10         -17.663786 
 (Intercept)   2.592229 
x1            .        
x2            .        
x3            .        
x4           -7.982268 
x5            .        
x6            .        
x7            .        
x8            .        
x9            .        
x10         -17.877815 
  
(Intercept)   3.21628 
x1            .       
x2            .       
x3            .       
x4          -11.65932 
x5            .       
x6            .       
x7            .       
x8            .       
x9            .       
x10         -20.64825 
(Intercept)   2.811912 
x1            .        
x2            .        
x3            .        
x4           -7.691559 
x5            .        
x6            .        
x7            .        
x8            .        
x9            .        
x10         -20.608779 
 
(Intercept)   2.438294 
x1            .        
x2            .        
x3            .        
x4           -7.726201 
x5            .        
x6            .        
x7            .        
x8            .        
x9            .        
x10         -16.653843 
(Intercept)   2.067274 
x1            .        
x2            .        
x3            .        
x4           -4.295535 
x5            .        
x6            .        
x7            .        
x8            .        
x9            .        
x10         -16.470045 
Figure 5: regression coeﬃcients for the 7 splits in NP-sLDA, repetition 1.
45


## Page 46


topic 1
今天
天
可以
没有
开始
点
真的
日子
明天
能
today
day
can
without
start
bit
really
day
tomorrow
can
前
回家
还有
吃饭
吃
号
那些
地铁
哈哈
玩
forward
go home
also
eat
eat
day
those
subway
haha
play
topic 2
罢工
上
上班
能
终于
抓狂
拿
小时
里
东西
strike
go to
work
can
ﬁnally
go crazy
get
hour
inside
thing
真是
三
为了
生活
之后
超级
只是
开心
觉得
对
really
three
for
life
after
super
just
happy
feel
right
topic 3
罢工
去
系
做
今日
地
睡觉
后
起来
听
strike
go
be
do
today
ground
sleep
after
get up
listen
搞
过
怒
公交
求
人
甘
吃
街
说
do
over
angry
public transportation
beg
people
willing
eat
street
speak
topic 4
想
人
让
说
罢课
累
发
衰
生病
找
think
people
let
speak
student strike
tired
happen
decline
sick
ﬁnd
次
鄙视
很多
新
但是
哦
感冒
虽然
委屈
竟然
time
despise
many
new
but
oh
a cold
although
be wronged
unexpectedly
topic 5
年
公司
月
员工
工人
工资
最后
月日
工作
还是
year
company
month
employee
worker
salary
ﬁnally
month-date
work
still
集体
第一
国际
次
要求
劳动
无法
机场
买
法国
collective
ﬁrst
international
time
demand
labor
unable
airport
buy
France
topic 6
罢工
的士
汕头
现在
出租车
司机
车
打
集体
辆
strike
taxi
Shantou
now
taxi
driver
car
call
collective
vehicle
下
广州
出门
已经
政府
事件
出
路
钱
问题
get oﬀ
Guangzhou
go out
already
government
event
out
street
money
problem
topic 7
可怜
小
结果
偷笑
发现
昨天
今晚
早上
能
一直
pity
small
result
smirk
ﬁnd
yesterday
tonight
morning
can
always
生病
竟然
郁闷
开
星期
罢工
三
今天
出来
结局
sick
unexpectedly
depressed
open
week
strike
three
today
go out
end
topic 8
罢工
天
知道
天气
时候
挖
鼻屎
太阳
种
周
strike
day
know
weather
time
pick
mucus
Sun
type
week
今天
时间
电视
突然
奥特曼
好像
应该
全部
水
点
today
time
TV
sudden
Ultraman
maybe
should
whole
water
bit
topic 9
罢工
抓
狂
泪
电脑
居然
今晚
鼓掌
泪泪
学校
strike
clutch
crazy
tear
computer
unexpectedly
tonight
applaud
tear
school
事
搞到
部
学生
结
啊啊
手机
明天
闹
闹钟
thing
get
department
student
form
ah
cellphone
tomorrow
alarm
alarm clock
topic 10
罢工
手机
中
最近
哼哼
一下
哈哈
电梯
停播
玩
strike
cellphone
within
recent
humph
a bit
haha
elevator
stop playing
play
女
怒骂
分钟
时候
过
晚
深圳
第一
迟到
下班
female
curse
minute
time
over
late
Shenzhen
ﬁrst
late
oﬀwork
Table 10: top 20 keywords for the ten topics selected from repetition 2.
46


## Page 47


(Intercept)   2.890680 
x1            .        
x2            .        
x3            .        
x4            .        
x5           -7.087097 
x6          -21.213795 
x7            .        
x8            .        
x9            .        
x10           .    
     
(Intercept)   2.682391 
x1            .        
x2            .        
x3            .        
x4            .        
x5           -4.826610 
x6          -21.347954 
x7            .        
x8            .        
x9            .        
x10           .        
(Intercept)   2.541224 
x1            .        
x2            .        
x3            .        
x4            .        
x5           -7.949472 
x6          -17.069710 
x7            .        
x8            .        
x9            .        
x10           .        
 
(Intercept)   2.450597 
x1            .        
x2            .        
x3            .        
x4            .        
x5           -5.872407 
x6          -18.176870 
x7            .        
x8            .        
x9            .        
x10           .        
(Intercept)   2.588368 
x1            .        
x2            .        
x3            .        
x4            .        
x5           -6.654200 
x6          -18.605443 
x7            .        
x8            .        
x9            .        
x10           .        
  
(Intercept)   2.917165 
x1            .        
x2            .        
x3            .        
x4            .        
x5           -9.101548 
x6          -19.616616 
x7            .        
x8            .        
x9            .        
x10           .        
(Intercept)   2.523783 
x1            .        
x2            .        
x3            .        
x4            .        
x5           -6.538955 
x6          -18.279681 
x7            .        
x8            .        
x9            .        
x10           .     
Figure 6: regression coeﬃcients for the 7 splits in NP-sLDA, repetition 2.
47


## Page 48


β1 = 0). Let h∗
β0,π0 be the classical oracle classiﬁer in the post-distortion population. Then the type
I error of h∗
β0,π0 (regarding either the pre-distortion or the post-distortion population) is calculated
as :
R0(h∗
β0,π0) = Φ
 
−1
2C −log ((1 −β0)p)
√
C
!
,
(A.10)
where C = (µ0 −µ1)⊤Σ−1(µ0 −µ1) and p = π0/(1 −π0). Equation (A.10) implies that
1. Keeping π0 ﬁxed (hence p is ﬁxed), R0(h∗
β0,π0) is a monotone increasing function of the class
0 censorship rate β0 ∈(0, 1). Moreover, we have i). if pe3C/2 ≤1, R0(h∗
β0,π0) is a concave
function of β0 ∈(0, 1); and ii). if pe3C/2 > 1, R0(h∗
β0,π0) is a convex function of β0 for
β0 ∈

0, 1 −
1
pe3C/2

, and a concave function for β0 ∈

1 −
1
pe3C/2 , 1

.
2. Keeping β0 ﬁxed, R0(h∗
β0,π0) is a monotone decreasing function of the class ratio p = π0/(1 −
π0). In other words, the larger the proportion of class 0 in the uncensored population, the
smaller the type I error of h∗
β0,π0. Moreover, R0(h∗
β0,π0) is a convex function of p for p >
1
(1−β0)e3C/2 , and it is a concave function of p for p ≤
1
(1−β0)e3C/2 .
Proof. Since equation (2) in the main text is the decision boundary of h∗
β0,π0, we have
R0(h∗
β0,π0) = PX∼N(µ0,Σ)

X⊤Σ−1(µ0 −µ1) −1
2(µ0 −µ1)⊤Σ−1(µ0 + µ1) + log
(1 −β0)π0
π1

≤0

.
For X in class 0, X⊤Σ−1(µ0−µ1) =: Z′ ∼N(µ⊤
0 Σ−1(µ0−µ1), (µ0−µ1)⊤Σ−1(µ0−µ1)). Therefore,
R0(h∗
β0,π0) = PZ′∼N(µ⊤
0 Σ−1(µ0−µ1),(µ0−µ1)⊤Σ−1(µ0−µ1))

Z′ ≤1
2(µ0 −µ1)⊤Σ−1(µ0 + µ1) −log
(1 −β0)π0
π1

= Φ


−1
2(µ0 −µ1)⊤Σ−1(µ0 −µ1) −log

(1−β0)π0
π1

p
(µ0 −µ1)⊤Σ−1(µ0 −µ1)

.
Regarding part 1, for ﬁxed π0, let f(β0) = R0(h∗
β0,π0).
f ′(β0) = φ
−1
2C −log ((1 −β0)p)
√
C

·
1
√
C(1 −β0)
,
where φ(·) is the probability density function of the standard normal random variable. This implies that for
β0 ∈(0, 1), f ′(·) is positive, so R0(h∗
β0,π0) is a monotone increasing function of β0 for ﬁxed π0. Taking the
48


## Page 49


second derivative of f, we have
f ′′(β0) = φ′
−1
2C −log ((1 −β0)p)
√
C

·
1
C(1 −β0)2 + φ
−1
2C −log ((1 −β0)p)
√
C

·
1
√
C(1 −β0)2 .
Let g(w) = φ′(w) +
√
Cφ(w). Then
g(w) =
1
√
2π e−w2
2 · (−w) +
√
C
√
2π e−w2
2 .
Note that g(w) > 0 iﬀw <
√
C.
Therefore, f ′′(β0) > 0 iﬀg( −1
2 C−log((1−β0)p)
√
C
) > 0 iﬀ−1
2 C−log((1−β0)p)
√
C
<
√
C iﬀβ0 < 1−
1
pe3C/2 . Similarly
f ′′(β0) < 0 iﬀβ0 > 1 −
1
pe3C/2 .
Regarding part 2, for ﬁxed β0, let k(p) = R0(h∗
β0,π0), then
k′(p) = φ
−1
2C −log ((1 −β0)p)
√
C

· −1
√
Cp
.
Clearly, k′(p) < 0 for all p > 0.
k′′(p) = φ′
−1
2C −log ((1 −β0)p)
√
C

·
1
Cp2 + φ
−1
2C −log ((1 −β0)p)
√
C

·
1
√
Cp2 .
Note that k′′(p) > 0 iﬀ−1
2 C−log((1−β0)p)
√
C
<
√
C iﬀp >
1
(1−β0)e3C/2 .
The constant C can be considered as a measure of separability of the two classes. Note that
when p = 1, that is when π0 = 1−π0 = 1/2, if C is large (i.e., it is easy to separate the two classes),
1/(pe3C/2) ≈0, then R0(h∗
β0,π0) is a convex function of β0 ∈(0, 1). On the other hand, when C is
so small (i.e., two classes are hard to separate) that pe3C/2 ≤1, R0(h∗
β0,π0) is a concave function of
β0 ∈(0, 1).
F.
NEYMAN-PEARSON LEMMA
The oracle classiﬁer under the NP paradigm (NP oracle) arises from its close connection to the
Neyman-Pearson Lemma in statistical hypothesis testing. Hypothesis testing bears strong resem-
blance to binary classiﬁcation if we assume the following model. Let P1 and P0 be two known
probability distributions on X ⊂Rd.
Assume that Y ∼Bern(ζ) for some ζ ∈(0, 1), and the
conditional distribution of X given Y is PY . Given such a model, the goal of statistical hypothesis
49


## Page 50


testing is to determine if we should reject the null hypothesis that X was generated from P0. To
this end, we construct a randomized test φ : X →[0, 1] that rejects the null with probability φ(X).
Two types of errors arise: type I error occurs when P0 is rejected yet X ∼P0, and type II error
occurs when P0 is not rejected yet X ∼P1. The Neyman-Pearson paradigm in hypothesis testing
amounts to choosing φ that solves the following constrained optimization problem
maximize IE[φ(X)|Y = 1] , subject to IE[φ(X)|Y = 0] ≤α ,
where α ∈(0, 1) is the signiﬁcance level of the test. A solution to this constrained optimization
problem is called a most powerful test of level α. The Neyman-Pearson Lemma gives mild suﬃcient
conditions for the existence of such a test.
Lemma 2 (Neyman-Pearson Lemma). Let P1 and P0 be two probability measures with densities
f1 and f0 respectively, and denote the density ratio as r(x) = f1(x)/f0(x). For a given signiﬁcance
level α, let Cα be such that P0{r(X) > Cα} ≤α and P0{r(X) ≥Cα} ≥α. Then, the most powerful
test of level α is
φ∗
α(X) =











1
if r(X) > Cα ,
0
if r(X) < Cα ,
α−P0{r(X)>Cα}
P0{r(X)=Cα}
if r(X) = Cα .
Under mild continuity assumption, we take the NP oracle classiﬁer
φ∗
α(x) = 1I{f1(x)/f0(x) > Cα} = 1I{r(x) > Cα} ,
(A.11)
as our plug-in target for NP classiﬁcation.
50

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
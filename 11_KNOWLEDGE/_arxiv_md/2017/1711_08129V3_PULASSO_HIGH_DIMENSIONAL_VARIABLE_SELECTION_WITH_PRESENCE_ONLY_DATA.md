---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1711.08129v3
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1711.08129v3_PULasso__High-dimensional_variable_selection_with_presence-only_data

> Source: 1711.08129v3_PULasso__High-dimensional_variable_selection_with_presence-only_data.pdf

> Pages: 75

---


## Page 1


PUlasso: High-dimensional variable selection with
presence-only data
Hyebin Song
Department of Statistics, University of Wisconsin-Madison
and
Garvesh Raskutti ∗
Department of Statistics, University of Wisconsin-Madison
November 1, 2018
Abstract
In various real-world problems, we are presented with classiﬁcation problems with
positive and unlabeled data, referred to as presence-only responses. In this paper, we
study variable selection in the context of presence only responses where the number of
features or covariates p is large. The combination of presence-only responses and high
dimensionality presents both statistical and computational challenges. In this paper,
we develop the PUlasso algorithm for variable selection and classiﬁcation with positive
and unlabeled responses. Our algorithm involves using the majorization-minimization
(MM) framework which is a generalization of the well-known expectation-maximization
(EM) algorithm. In particular to make our algorithm scalable, we provide two compu-
tational speed-ups to the standard EM algorithm. We provide a theoretical guarantee
where we ﬁrst show that our algorithm converges to a stationary point, and then prove
that any stationary point within a local neighborhood of the true parameter achieves
the minimax optimal mean-squared error under both strict sparsity and group spar-
sity assumptions. We also demonstrate through simulations that our algorithm out-
performs state-of-the-art algorithms in the moderate p settings in terms of classiﬁcation
performance. Finally, we demonstrate that our PUlasso algorithm performs well on a
biochemistry example.
Keywords: PU-learning, majorization-minimization, non-convexity, regularization.
∗Both HS and GR were partially supported by NSF-DMS 1407028. GR was also partially supported by
ARO W911NF-17-1-0357.
1
arXiv:1711.08129v3  [stat.ME]  30 Oct 2018


## Page 2


1
Introduction
In many classiﬁcation problems, we are presented with the problem where it is either pro-
hibitively expensive or impossible to obtain negative responses and we only have positive
and unlabeled presence-only responses (see e.g. Ward et al. (2009)). For example, presence-
only data is prevalent in geographic species distribution modeling in ecology where pres-
ences of species in speciﬁc locations are easily observed but absences are diﬃcult to track
(see e.g. Ward et al. (2009)), text mining (see e.g. Liu et al. (2003)), bioinformatics (see
e.g. Elkan and Noto (2008)) and many other settings. Classiﬁcation with presence-only data
is sometimes referred to as PU-learning (see e.g. Liu et al. (2003); Elkan and Noto (2008)).
In this paper we address the problem of variable selection with presence-only responses.
1.1
Motivating application: Biotechnology
Although the theory and methodology we develop apply generally, a concrete application
that motivates this work arises from biological systems engineering. In particular, recent
high-throughput technologies generate millions of biological sequences from a library for
a protein or enzyme of interest (see e.g. Fowler and Fields (2014); Hietpas et al. (2011)).
In Section 5 the enzyme of interest is beta-glucosidase (BGL) which is used to decompose
disaccharides into glucose which is an important step in the process of converting plant
matter to bio-fuels (Romero et al. (2015)). The performance of the BGL enzyme is measured
by the concentration of glucose that is produced and a positive response arises when the
disaccharide is decomposed to glucose and a negative response arises otherwise.
Hence
there are two scientiﬁc goals: ﬁrstly to determine how the sequence structure inﬂuences
the biochemical functionality; secondly, using this relationship to engineer and design BGL
sequences with improved functionality.
Given these two scientiﬁc goals, we are interested in both the variable selection and
classiﬁcation problem since we want to determine which positions in the sequence most
2


## Page 3


inﬂuence positive responses as well as classify which protein sequences are functional. Fur-
thermore the number of variables here is large since we need to model long and complex
biological sequences. Hence our variable selection problem is high-dimensional. In Section 5
we demonstrate the success of our algorithm in this application context.
1.2
Problem setup
To state the problem formally, let x ∈Rp be a p-dimensional covariate such that x ∼PX,
y ∈{0, 1} an associated response, and z ∈{0, 1} an associated label.
If a sample is
labeled (z = 1), its associated outcome is positive (y = 1).
On the other hand, if a
sample is unlabeled (z = 0), it is assumed to be randomly drawn from the population with
only covariates x not the response y being observed. Given nℓlabeled and nu unlabeled
samples, the goal is to draw inferences about the relationship between y and x. We model
the relationship between the probability of a response y being positive and (x, θ) using the
standard logistic regression model:
P(y = 1|x; θ) =
eηθ(x)
1 + eηθ(x) ,
ηθ(x) = θT x
(1)
and y|x ∼P(·|x; θ∗) where θ∗∈Rp refers to the unknown true parameter. Also, we assume
the label z is assigned only based on the latent response y independent from x. Viewing
z as a noisy observation of latent y, this assumption corresponds to a missing at random
assumption, a classical assumption in latent variable problems.
Given such z, we select nl labeled and nu unlabeled samples from samples with z = 1
and z = 0 respectively. An important issue is how positive and unlabeled samples are
selected. In this paper we adopt a case-control approach (for example, McCullagh and
Nelder (1989)) which is suitable for our biotechnology application and many others. In
particular we introduce another binary random variable s ∈{0, 1} representing whether
a sample is selected (s = 1) or not (s = 0) to model diﬀerent sampling rates in selecting
3


## Page 4


labeled and unlabeled samples. Since there are nℓlabeled and nu unlabeled samples, we
have
P(z = 1|s = 1)
P(z = 0|s = 1) = nℓ
nu
,
and we see only selected samples, (xi, zi, si = 1)nℓ+nu
i=1
.
It is further assumed that the
selection is only based on the label z, independent of x and y. We note that this case-control
scheme (Lancaster and Imbens (1996); Ward et al. (2009)), opposed to the single-training
sampling scheme (Elkan and Noto (2008)) is needed to model the case where unlabeled
samples are random draws from the original population, since positive samples have to be
over-represented in the dataset to satisfy such model assumption.
In our biotechnology application the case-control setting is appropriate since the high-
throughput technology leads to the unlabeled samples being drawn randomly from the
original population (see Romero et al. (2015) for details). As is displayed in Fig. 1, sequences
are selected randomly from a library and positive samples are generated through a screening
step. Hence the positive sequences are sampled randomly from the positive sequences while
the unlabeled sequences are based on random sampling from the original sequence library.
This experiment corresponds exactly to the case-control sampling scheme discussed.
Figure 1: High-throughput sequencing diagram
Furthermore, the true positive prevalence is
π := P(y = 1) =
Z
eηθ∗(x)
1 + eηθ∗(x) dPX(x) ∈(0, 1)
(2)
4


## Page 5


and π is assumed known. In our biotechnology application, π is estimated precisely using
an alternative experiment (Romero et al. (2015)).
In the biological sequence engineering example, (xi)nℓ+nu
i=1
correspond to binary covari-
ates of biological sequences. In the BGL example, for each of the d positions, there are
M possible categories of amino acids. Therefore the covariates correspond to the indicator
of an amino acid appearing in a given position (p = O(dM)) as well as pairs of amino
acids (p = O(d2M2)), and so on.
Here d = O(1000) and M ≈20 make the problem
high-dimensional.
High-dimensional PU-learning presents computational challenges since the standard lo-
gistic regression objective leads to a non-convex likelihood when we have positive and
unlabeled data. To address this challenge, we build on the expectation-maximization (EM)
procedure developed in Ward et al. (2009) and provide two computational speed-ups. In
particular we introduce the PUlasso for high-dimensional variable selection with positive
and unlabeled data. Prior work that involves the EM algorithm in the low-dimensional
setting in Ward et al. (2009) involves solving a logistic regression model at the M-step.
To adapt to the high-dimensional setting and make the problem scalable, we include an
ℓ1-sparsity or ℓ1/ℓ2-group sparsity penalty and provide two speed-ups. Firstly we use a
quadratic majorizer of the logistic regression objective, and secondly we use techniques
in linear algebra to exploit sparsity of the design matrix X which commonly arises in
the applications we are dealing with. Our PUlasso algorithm ﬁts into the majorization-
minimization (MM) framework (see e.g. Lange et al. (2000); Ortega and Rheinboldt (2000))
for which the EM algorithm is a special case.
1.3
Our contributions
In this paper, we make the following major contributions:
• Develop the PUlasso algorithm for doing variable selection and classiﬁcation with
5


## Page 6


presence-only data. In particular we build on the existing EM algorithm developed
in Ward et al. (2009) and add two computational speed-ups, quadratic majorization
and exploiting sparse matrices. These two speed-ups improve speed by several orders
of magnitude and allows our algorithm to scale to datasets with millions of samples
and covariates.
• Provide theoretical guarantees for our algorithm. First we show that our algorithm
converges to a stationary point of the non-convex objective, and then show that
any stationary point within a local neighborhood of θ∗achieves the minimax optimal
mean-squared error for sparse vectors. To provide statistical guarantees we extend the
existing results of generalized linear model with a canonical link function (Negahban
et al. (2012); Loh and Wainwright (2013)) to a non-canonical link function and show
optimality of stationary points of non-convex objectives in high-dimensional statistics.
To the best of our knowledge the PUlasso is the ﬁrst algorithm where PU-learning is
provably optimal in the high-dimensional setting.
• Demonstrate through a simulation study that our algorithm performs well in terms
of classiﬁcation compared to state-of-the-art PU-learning methods in Du Marthinus
et al. (2015); Elkan and Noto (2008); Liu et al. (2003), both for low-dimensional and
high-dimensional problems.
• Demonstrate that our PUlasso algorithm allows us to develop improved protein-
engineering approaches. In particular we apply our PUlasso algorithm to sequences
of BGL (beta-glucosidase) enzymes to determine which sequences are functional. We
demonstrate that sequences selected by our algorithm have a good predictive accuracy
and we also provide a scientiﬁc experiment which shows that the variables selected
lead to BGL proteins that are engineered with improved functionality.
The remainder of the paper is organized as follows: in Section 2 we provide the back-
6


## Page 7


ground and introduce the PUlasso algorithm, including our two computational speed-ups
and provide an algorithmic guarantee that our algorithm converges to a stationary point;
in Section 3 we provide statistical mean-squared error guarantees which show that our PU-
lasso algorithm achieves the minimax rate; Section 4 provides a comparison in terms of
classiﬁcation performance of our PUlasso algorithm to state-of-the-art PU-learning algo-
rithms; ﬁnally in Section 5, we apply our PUlasso algorithm to the BGL data application
and provide both a statistical validation and simple scientiﬁc validation for our selected
variables.
Notation:
For scalars a, b ∈R, we denote a ∧b = min{a, b}, a ∨b = max{a, b}. Also,
we denote a ≳b if there exists a universal constant c > 0 such that a ≥cb. For v, w ∈Rp,
we denote ℓ1, ℓ2, and ℓ∞norm as ∥v∥1 = Pn
i=1 |vi|, ∥v∥2 =
√
vT v, and ∥v∥∞= supj |vj|
and use v ◦w ∈Rp to denote Hadamard product (entry-wise product) of v, w. For a set S,
we use |S| to denote the cardinality of S. For any subset S ⊆{1, . . . , p}, vS ∈R|S| denotes
the sub-vector of the vector v by selecting the components with indices in S. Likewise for
matrix A ∈Rn×p, AS ∈Rn×|S| denotes a sub-matrix by selecting columns with indices in
S. For a group ℓ1/ℓ2 norm, the norm is characterized by a partition G := (g1, . . . , gJ) of
{1, . . . , p} and associated weights (wj)J
1 . We let G := (G, (wj)J
1 ) and deﬁne the ℓ1/ℓ2 norm
as ∥v∥G,2,1 := P
j wj∥vgj∥2. We often need a dual norm of ∥·∥G,2,1. We use ¯G to denote
¯G := (G, (w−1
j )J
1 ) and write ∥v∥¯G,2,∞= maxj w−1
j ∥vgj∥2. Finally we write Bq(r, v) for an ℓq
ball with radius r centered at v ∈Rp, and denote as Bq(r) if v = 0.
For a convex function f : Rp →R, we use ∂f(x) to denote the set of sub-gradients at
the point x and ▽f(x) to denote an element of ∂f(x). Also for a function f + g such that
f is diﬀerentiable (but not necessarily convex) and g is convex, we deﬁne ∂(f + g)(x) :=
{▽f(x) + h ∈Rp; h ∈∂g(x)} with a slight abuse of notation. Also, we say f(n) = O(g(n)),
f(n) = Ω(g(n)), and f(n) = Θ(g(n)) if |f| is asymptotically bounded above, bounded
below, and bounded above and below by g.
7


## Page 8


For a random variable x ∈R, we say x is a sub-Gaussian random variable with sub-
Gaussian parameter σx > 0 if E[exp(t(x−E[x]))] ≤exp(t2σ2
x/2) for all t ∈R and we denote
as x ∼subG(σ2
x) with a slight abuse of notation. Similarly, we say x is a sub-exponential
random variable with sub-exponential parameter (ν, b) if E[exp(t(x−E[x]))] ≤exp(t2ν2/2)
for all |t| ≤1/b and we denote as x ∼subExp(ν, b).
A collection of random variables
(x1, . . . , xn) is referred to as xn
1.
2
PUlasso algorithm
In this section, we introduce our PUlasso algorithm. First, we discuss the prior EM algo-
rithm approach developed in Ward et al. (2009) and apply a simple regularization scheme.
We then discuss our two computational speed-ups, the quadratic majorization for the M-
step and exploiting sparse matrices.
We prove that our algorithm has the descending
property and converges to a stationary point, and show that our two speed-ups increase
speed by several orders of magnitude.
2.1
Prior approach: EM algorithm with regularization
First we use the prior result in Ward et al. (2009) to determine the observed log-likelihood (in
terms of the zi’s) and the full log-likelihood (in terms of the unobserved yi’s and zi’s). The
following lemma, derived in Ward et al. (2009), gives the form of the observed and the full
log-likelihood in the case-control sampling scheme.
Lemma 2.1 (Ward et al. (2009)). The observed log-likelihood log L(θ; xn
1, zn
1 ) for our
8


## Page 9


presence-only model in terms of (xi, zi, si = 1)n
i=1 is:
log L(θ; xn
1, zn
1 ) = log
 Y
i
Pθ(zi|xi, si = 1)
!
=
n
X
i=1
log
 
nl
πnu eθT x
1 + (1 +
nl
πnu )eθT x
!zi  
1 + eθT x
1 + (1 +
nl
πnu )eθT x
!1−zi
(3)
The full log-likelihood log Lf(θ; xn
1, yn
1 , zn
1 ) in terms of (xi, yi, zi, si = 1)n
i=1 is
log Lf(θ; xn
1, yn
1 , zn
1 ) = log
 Y
i
Pθ(yi, zi|xi, si = 1)
!
∝
n
X
i=1
[yi(xT
i θ + log nℓ+ πnu
πnu
) −log(1 + exp(xT
i θ + log nℓ+ πnu
πnu
))]
(4)
where nℓ, nu are the number of positive and unlabeled observations, n = nℓ+ nu and π is
deﬁned in (2).
The proof can be found in Ward et al. (2009).
Our goal is to estimate the parameter
θ∗:= argminθ∈Rp E[−log L(θ; xn
1, zn
1 )], which we assume to be unique. In the setting where
p is large, we add a regularization term. We are interested in cases when there exists or does
not exist a group structure within covariates. To be general we use the group ℓ1/ℓ2-penalty
for which ℓ1 is a special case. Hence our overall optimization problem is:
minimize
θ
−1
n
n
X
i=1
log L(θ; xi, zi) + Pλ(θ)
(5)
where log L(θ; xi, zi) is the observed log-likelihood. For a penalty term, we use the group
sparsity regularizer
Pλ(θ) := λ∥θ∥G,2,1 = λ
J
X
j=1
wj∥θgj∥2
(6)
with G = (G, (wj)J
j=1), such that G := (g1, ..., gJ) is a partition of (1, . . . , p) and wj > 0. We
note that ∥θ∥G,2,1 = ∥θ∥1 if J = p, gj = {j} and wj = 1, ∀j. For notational convenience we
9


## Page 10


denote the overall objective Fn(θ) as
Fn(θ) := −1
n
n
X
i=1
log L(θ; xi, zi) + Pλ(θ) = Ln(θ) + Pλ(θ)
(7)
where we deﬁne the loss function Ln(θ) as Ln(θ) := −n−1 Pn
i=1 log L(θ; xi, zi) and Pλ(θ) =
λ∥θ∥G,2,1 = λ PJ
j=1 wj∥θgj∥2.
In the original proposal of the group lasso, Yuan and Lin (2006) recommended to use (6)
for orthonormal group matrices Xgj, i.e. XT
gjXgj/n = I|gj|×|gj|. If group matrices are not
orthonormal however, it is unclear whether we should orthonormalize group matrices prior
to application of the group lasso. This question was addressed in Simon and Tibshirani
(2012), and the authors provide a compelling argument that prior orthonormalization has
both theoretical and computational advantages. In particular, Simon and Tibshirani (2012)
demonstrated that the following orthonormalization procedure is intimately connected with
the uniformly most powerful invariant testing for inclusion of a group. To describe this
orthonormalization explicitly, we obtain standardized group matrices Qgj ∈Rn×|gj| and
scale matrices Rgj ∈R|gj|×|gj| for j ≥2 using the QR-decomposition such that
P0Xgj = QgjRgj and QT
gjQgj = nI|gj|×|gj|
(8)
where P0 = (In×n −1n1T
n
n
) is the projection matrix onto the orthogonal space of 1n. Let-
ting Q := [1n, Qg2, . . . , QgJ] = [qT
1 , . . . , qT
n ], the original optimization problem (5) can be
expressed in terms of qi’s and becomes:
argmin
ν


−1
n
n
X
i=1
log L(ν; qi, zi) + λ
J
X
j=1
wj∥νgj∥2



(9)
where we use the transformation θ to ν:
θgj =





ν1 −PJ
j=2
1T
n
n XgjR−1
gj νgj
j = 1
R−1
gj νgj
j ≥2.
(10)
10


## Page 11


We note that this corresponds to the standard centering and scaling of the predictors in
the case of standard lasso. For more discussion about group lasso and standardization, see
e.g. Huang et al. (2012).
A standard approach to performing this minimization is to use the EM-algorithm ap-
proach developed in Ward et al. (2009).
In particular we treat yn
1 as hidden variables
and estimate them in the E-step. Then use estimated ˆyn
1 to obtain the full log-likelihood
log Lf(θ; xn
1, ˆyn
1 , zn
1 ) in the M-step.
Algorithm 1: Regularized EM algorithm for the optimization problem (5)
1 Input: an initialization θ0 such that Fn(θ0) ≤Fn(θnull)
2 for m=0,1,2,. . . , do
• E-step : estimate yi at θ = θm by
ˆyi(θm) =
 
exT
i θm
1 + exT
i θm
!1−zi
(11)
• M-step : obtain θm+1 by
θm+1 ∈argmin
θ
(
−1
n
n
X
i=1

ˆyi(θm)
 xT
i θ + b

−log(1 + exT
i θ+b)

+ Pλ(θ)
)
(12)
where b := log nℓ+ πnu
πnu
3 end
The E-step follows from Eθm[yi|zi, xi, si = 1] =
 
exT
i θm
1 + exT
i θm
!1−zi
since zi = 1 implies
yi = 1 and when zi = 0, observations in the unlabeled data are random draws from the
population. An initialization θ0 can be any Rp vector such that Fn(θ0) ≤Fn(θnull) where
θnull is the parameter corresponding to the intercept-only model. If we are provided with
no additional information, we may use θnull for the initialization. We use θ0 = θnull as the
initialization for the remainder of the paper. For the M-step it was originally proposed to
use a logistic regression solver. We can use a regularized logistic regression solver such as
11


## Page 12


the glmnet R package to solve (12). We discuss a computationally more eﬃcient way of
solving (12) in the subsequent section.
2.2
PUlasso : A Quadratic Majorization for the M-step
Now we develop our PUlasso algorithm which is a faster algorithm for solving (5) by using
quadratic majorization for the M-step. The main computational bottleneck in algorithm 1
is the M-step which requires minimizing a regularized logistic regression loss at each step.
This sub-problem does not have a closed-form solution and needs to be solved iteratively,
causing ineﬃciency in the algorithm. However the most important property of the objective
function in the M-step is that it is a surrogate function of the likelihood which ensures the
descending property (see e.g. Lange et al. (2000)). Hence we replace a logistic loss function
with a computationally faster quadratic surrogate function. In this aspect, our approach is
an example of the more general majorization-minimization (MM) framework (see e.g. Lange
et al. (2000); Ortega and Rheinboldt (2000)).
On the other hand, our loss function itself belongs to a generalized linear model family,
as we will discuss in more detail in the subsequent section.
A number of works have
developed methods for eﬃciently solving regularized generalized linear model problems.
A standard approach is to make a quadratic approximation of the log-likelihood and use
solvers for a regularized least-square problem. Works include using an exact Hessian (Lee
et al. (2006); Friedman et al. (2010)), an approximate Hessian (Meier et al. (2008)) or a
Hessian bound (Krishnapuram et al. (2005); Simon and Tibshirani (2012); Breheny and
Huang (2013)) for the second order term. Solving a second-order approximation problem
amounts to taking a Newton step, thus convergence is not guaranteed without a step-size
optimization (Lee et al. (2006); Meier et al. (2008)), unless a global bound of the Hessian
matrix is used. Our work can be viewed as in the line of these works where a quadratic
approximation of the loss function is made and then an upper bound of the Hessian matrix
12


## Page 13


is used to preserve a majorization property.
A coordinate descent (CD) algorithm (Wu and Lange (2008); Friedman et al. (2010)) or
a block coordinate descent (BCD) algorithm (Yuan and Lin (2006); Puig et al. (2011); Simon
and Tibshirani (2012); Breheny and Huang (2013)) has been a very eﬃcient and standard
way to solve a quadratic problem with ℓ1 penalty or ℓ1/ℓ2 penalty and we also take this
approach. When a feature matrix X ∈Rn×p is sparse, we can set up the algorithm to exploit
such sparsity through a sparse linear algebra calculation. We discuss this implementation
strategy in the Section 2.2.1.
Now we discuss the PUlasso algorithm and the construction of quadratic surrogate
functions in more details. Using the MM framework we construct the set of majorization
functions −Q(θ; θm) with the following two properties:
Q(θm; θm) = Q(θm; θm),
Q(θ; θm) ≤Q(θ; θm), ∀θ
(13)
where our goal is to minimize −Q where Q(θ; θm) := n−1Eθm[log Lf(θ)|zn
1 , xn
1, sn
1 = 1].
Using the Taylor expansion of Q(θ; θm) at θ = θm, we obtain Q(θ; θm)
= Q(θm; θm) + 1
n[XT (ˆy(θm) −µ∗(θm))]T ∆m −1
2n
Z 1
0
∆T
mXT W(θ + s∆m)X∆mds
≥Q(θm; θm) + 1
n(ˆy(θm) −µ∗(θm))T X∆m −1
8n∆T
mXT X∆m
where we deﬁne ∆m := θ −θm, µ∗(θm)i :=
exT
i θm+b
1 + exT
i θm+b , b := log nℓ+ πnu
πnu
and W ∈Rn×n
is a diagonal matrix with [W(θ)]ii := µ∗(θ)i(1 −µ∗(θ)i).
The inequality follows from
W(θ) ≺1
4In×n, ∀θ. Thus setting Q as follows:
Q(θ; θm) := Q(θm; θm) + 1
n(ˆy(θm) −µ∗(θm))T (Xθ −Xθm) −1
8n(θ −θm)T XT X(θ −θm),
Q satisﬁes both conditions in (13). Also with some algebra, it follows that
Q(θ; θm) = −1
8n(4(ˆy(θm)−µ∗(θm))+Xθm −Xθ)T (4(ˆy(θm)−µ∗(θm))+Xθm −Xθ)+c(θm)
13


## Page 14


for some c(θm) which does not depend on θ.
Hence −Q acts as a quadratic surrogate
function of −Q which replaces our M-step for the original EM algorithm. Therefore our
PUlasso algorithm can be represented as follows.
Algorithm 2: PUlasso : QM-EM algorithm for the optimization problem (5)
1 Input: an initialization θ0 such that Fn(θ0) ≤Fn(θnull)
2 for m=0,1,2,. . . , do
• E-step : estimate yi at θ = θm by
ˆyi(θm) =
 
exT
i θm
1 + exT
i θm
!1−zi
(14)
• QM-EM step : obtain θm+1 by
1. create a working response vector u(θm) at θ = θm
u(θm) := 4(ˆy(θm) −µ∗(θm)) + Xθm
(15)
2. solve a quadratic loss problem with a penalty
θm+1 ∈argmin
θ
 1
2n(u(θm) −Xθ)T (u(θm) −Xθ) + 4Pλ(θ)

(16)
3 end
Now we state the following proposition to show that both the regularized EM and
PUlasso algorithms have the desirable descending property and converge to a stationary
point. For convenience we deﬁne the feasible region f
Θ0, which contains all θ whose objective
function value is better than that of the intercept-only model, deﬁned as:
f
Θ0 := {θ ∈Rp; Fn(θ) ≤Fn(θnull)}
(17)
where θnull = [log
π
1−π, 0, ..., 0]T , an estimate corresponding to the intercept-only model.
We let S be the set of stationary points satisfying the ﬁrst order optimality condition, i.e.,
S := {θ; ∃▽Fn(θ) ∈∂Fn(θ) such that ▽Fn(θ)T (θ′ −θ) ≥0, ∀θ′ ∈f
Θ0}.
(18)
One of the important conditions is to ensure that all iterates of our algorithm lie in f
Θ0
14


## Page 15


which is trivially satisﬁed if θ0 = θnull.
Proposition 2.1. The sequence of estimates (θm) obtained by Algorithms 1 or 2 satisﬁes
(i) Fn(θm) ≥Fn(θm+1), and Fn(θm) > Fn(θm+1) if θm ̸∈S.
(ii) All limit points of (θm)∞
1 are elements of the set S, and Fn(θm) converges monotoni-
cally to Fn(eθ) for some eθ ∈S.
(iii) The sequence (θm) has at least one limit point, which must be a stationary point of
Fn(θ) by (ii).
Proposition 2.1 shows that we obtain a stationary point of the objective (7) as an
output of both the regularized EM algorithm and our PUlasso algorithm. The proof uses
the standard arguments based on Jensen’s inequality, convergence of EM algorithm and
MM algorithms and is deferred to the supplement S1.1.
2.2.1
Block Coordinate Descent Algorithm for M-step and Sparse Calculation
In this section, we discuss the speciﬁcs of ﬁnding a minimizer for the M-step (16) for each
iteration of our PUlasso algorithm. After pre-processing the design matrix as described
in (9), (10), we solve the following optimization problem using a standard block-wise coor-
dinate descent algorithm.
argmin
ν



1
2n∥u −Qν∥2
2 + 4λ
J
X
j=1
wj∥νgj∥2



(19)
15


## Page 16


Algorithm 3: Fitting (19) using Block Coordinate Descent
1 Given initial parameter ν = [ν1, νT
g2 . . . , νT
gJ]T , a residual vector r = u −PJ
j=1 Qgjνgj
2 for j=1 do
3
update ν1 and r using (20)-(22)
4 end
5 repeat
6
for j=2,. . . ,J do
7
zj = n−1QT
gjr + νgj
(20)
ν′
gj ←S(zj, 4λwj)
(21)
r′ ←r + Qgj(νgj −ν′
gj)
(22)
r ←r′, νgj ←ν′
gj
8
end
9 until convergence;
S(., λ) is the soft thresholding operator deﬁned as follows:
S(z, λ) :=





(∥z∥2 −λ)
z
∥z∥2
if ∥z∥2 > λ
0
otherwise.
Note that we do not need to keep updating the intercept ν1 since Qgj, j ≥2 are orthogonal
to Qg1 ≡1n. For more details, see e.g. Breheny and Huang (2013).
For our biochemistry example and many other examples, X is a sparse matrix since
each entry is an indicator of whether an amino acid is in a position. In Algorithm 3, we do
not exploit this sparsity since Q will not be sparse even when X is sparse. If we want to
exploit sparse X we use the following algorithm.
16


## Page 17


Algorithm 4: Fitting (19) and exploiting sparse X
1 Given initial parameter ν = [ν1, νT
g2 . . . , νT
gJ]T , r = u −P0(PJ
j=1 XgjR−1
gj νgj)
2 for j=1 do
3
update ν1 and r using (20)-(22).
4 end
5 repeat
6
for j=2,. . . ,J do
7
zj = n−1R−1
gj XT
gjr −R−1
gj

XT
gj1n/n
  1T
nr/n

+ νgj
(23)
ν′
gj ←S(zj, 4λwj)
(24)
r′ ←r + XgjR−1
gj (νgj −ν′
gj)
(25)
aj ←1T
nXgjR−1
gj (νgj −ν′
gj)/n
(26)
r ←r′, νgj ←ν′
gj
8
end
9
r ←r −(
J
X
j=2
aj)1n
(27)
10 until convergence;
To explain the changes to this algorithm, we modify (20) and (22) so that we directly
use X rather than Q to exploit the sparsity of X. Using (8), we ﬁrst substitute Qgj with
P0XgjR−1
gj to obtain
zj = n−1R−1
gj XT
gjP0r + νgj
(28)
r′ ←r + P0XgjR−1
gj (νgj −ν′
gj).
(29)
However carrying out (28)-(29) instead of (20)-(22) incurs a greater computational cost.
Calculating QT
gjr requires n|gj| operations. On the contrary, the minimal number of oper-
ations required to do a matrix multiplication of R−1
gj XT
gjP0r is n2 + n|gj| + |gj|2, when it is
parenthesized as R−1
gj (XT
gj(P0r)). In many cases |gj| is small (for standard lasso, |gj| = 1, ∀j
and for our biochemistry example, |gj| is at most 20), but the additional increase in n can
17


## Page 18


be very costly (especially in our example where n is over 4 million).
For a more eﬃcient calculation, we ﬁrst exploit the structure of P0 = In×n −1n1T
n
n
when
multiplying P0 with a vector, which reduces the cost from n2 operations to 2n operations.
Also, we carry out calculations using Xgj instead of P0Xgj when calculating residuals and
do the corrections all at once.
Before going into detail about (23)-(26), we ﬁrst discuss the computational complexity.
Comparing (23) with (20), the ﬁrst term only requires an additional |gj|2 operations. The
second term (XT
gj1n)/n can be stored during the initial QR decomposition; thus the only
potentially expensive operation is calculating an average of r which requires n operations.
Comparing (25) with (22), only |gj|2 additional operations are needed when we parenthesize
as Xgj(R−1
gj (νgj −ν′
gj)). Note that if we had kept P0, there would have been an additional
2n operations even though we had used the structure of P0. In the calculation of (27), we
note that n operations are involved in subtracting PJ
j=2 aj from r because aj are scalars. In
summary, we essentially reduce additional computational cost from O(n2) to nJ per cycle
by carrying out (23)-(26) instead of (28)-(29).
Now we derive/explain the formulas in Algorithm 4. To make quantities more explicit,
we use rj and r′
j to denote a residual vector before/after update at j using Algorithm 3
and ˜rj and ˜r′
j using Algorithm 4. By deﬁnition, rj+1 = r′
j and ˜rj+1 = ˜r′
j. Also we note
that in the beginning of the cycle r2 = ˜r2. Equation (23) can be obtained from (28) by
replacing P0 with In×n −1n1T
n
n
. Now we show that modiﬁed residuals still correctly update
coeﬃcients. Starting from j = 2, a calculated residual ˜r′
j is a constant vector oﬀfrom a
correct residual r′
j, as we see below:
r
′
j = rj + P0XgjR−1
gj (νgj −ν′
gj)
(30)
= rj + XgjR−1
gj (νgj −ν′
gj) −1n
1T
n
n XgjR−1
gj (νgj −ν′
gj)
(31)
= ˜r′
j −1naj
(32)
18


## Page 19


where we recall that aj = 1T
n
n XgjR−1
gj (νgj −ν′
gj). We note P0r′
j = P0˜r′
j because P01n = 0.
Then the next zj+1, thus new νgj+1, are still correctly calculated since
zj+1 = n−1R−1
gj+1XT
gj+1P0rj+1 + νgj+1 = n−1R−1
gj+1XT
gj+1P0˜rj+1 + νgj+1.
(33)
The next residual ˜r′
j+1 is again oﬀby a constant from the correct residual r′
j+1. To see
this, r′
j+1 = rj+1 +P0Xgj+1R−1
gj+1(νgj+1 −ν′
gj+1) = ˜rj+1 +P0Xgj+1R−1
gj+1(νgj+1 −ν′
gj+1)−aj1n
by (29). Going through (30)-(32) with j being replaced by j + 1, we obtain
r′
j+1 = ˜r′
j+1 −(aj + aj+1)1n.
Inductively, we have correct zj, thus νgj for all j ≥2. At the end of the cycle, we correct
the residual vector all at once by letting r ←r −(PJ
j=2 aj)1n.
2.3
R Package details
We provide a publicly available R implementation of our algorithm in the PUlasso pack-
age. For a fast and eﬃcient implementation, all underlying computation is implemented
in C++. The package uses warm start and strong rule (Friedman et al. (2007); Tibshirani
et al. (2012)), and a cross-validation function is provided as well for the selection of the
regularization parameter λ. Our package supports a parallel computation through the R
package parallel.
2.4
Run-time improvement
Now we illustrate the run-time improvements for our two speed-ups. Note that we only
include p up to 100 so that we can compare to the original regularized EM algorithm. For
our biochemistry application p = O(104) and n = O(106) which means the regularized EM
algorithm is too slow to run eﬃciently. Hence we use smaller values of n and p in our run-
time comparison. It is clear from our results that the quadratic majorization step is several
19


## Page 20


orders of magnitude faster than the original EM algorithm, and exploiting the sparsity of
X provides a further 30% speed-up.
(n,p)
PUlasso
EM
time reduction(%)
Dense matrix
n=1000, p=10
0.94
443.72
99.79
n=5000, p=50
2.52
1844.98
99.86
n=10000, p=100
9.45
5066.86
99.81
Sparse matrix
n=1000, p=10
0.40
196.86
99.80
n=5000, p=50
2.01
614.65
99.67
n=10000, p=100
4.29
1201.09
99.64
Table 1: Timings (in seconds). Sparsity level in X = 0.95, nℓ/nu = 0.5. Total time for
100 λ values, averaged over 3 runs.
(n,p)
sparse calculation
dense calculation
time reduction(%)
n=10000, p=100
12.91
19.24
32.89
n=30000, p=100
25.64
38.73
33.79
n=50000, p=100
39.47
57.18
30.97
Table 2: Timings (in seconds) using sparse and dense calculation for ﬁtting the same
simulated data.
Sparsity level in X = 0.95, nℓ/nu = 0.5.
Total time for 100 λ values,
averaged over 3 runs.
3
Statistical Guarantee
We now turn our attention to statistical guarantees for our PUlasso algorithm under the
statistical model (1). In particular we provide error bounds for any stationary point of
the non-convex optimization problem (5).
Proposition 2.1 guarantees that we obtain a
stationary point from our PUlasso algorithm.
20


## Page 21


We ﬁrst note that the observed likelihood (3) is a generalized linear model (GLM) with
a non-canonical link function. To see this, we rewrite the observed likelihood (3) as
L(θ; xn
1, zn
1 ) =
n
Y
i=1
exp (ziηi −A(ηi))
(34)
after some algebraic manipulations, where we deﬁne ηi := log(nℓ/πnu)+xT
i θ−log(1+exT
i θ)
and A(ηi) := log(1 + eηi). Also, we let µ(ηi) := A′(ηi), which is the conditional mean of
zi given xi, by the property of exponential families. For the convenience of the reader, we
include the derivation from (3) to (34) in the supplementary material S2.1. The mean of
zi is related with θT xi via the link function g through g(µ(ηi)) = θT xi, where g satisﬁes
(g ◦µ)−1(θT xi) = log(nℓ/πnu) + xT
i θ −log(1 + exT
i θ). Because (g ◦µ)−1 is not the identity
function, the likelihood is not convex anymore.
For a more detailed discussion about
the GLM with non-canonical link, see e.g. McCullagh and Nelder (1989); Fahrmeir and
Kaufmann (1985).
A number of works have been devoted to sparse estimation for generalized linear models.
A large number of previous works have focused on generalized linear models with convex
loss functions (negative log-likelihood with a canonical link) plus ℓ1 or ℓ1/ℓ2 penalties.
Results with the ℓ1 penalty include a risk consistency result (van de Geer (2008)) and
estimation consistency in ℓ2 or ℓ1 norms (Kakade et al. (2010)). For a group-structured
penalty, a probabilistic bound for the prediction error was given in Meier et al. (2008). An
ℓ2 estimation error bound in the case of the group lasso was given in Blaz`ere et al. (2014).
Negahban et al. (2012) re-derived an ℓ2 error bound of an ℓ1-penalized GLM estimator
under the uniﬁed framework for M-estimators with a convex loss function.
This result
about the regularized GLM was generalized in Loh and Wainwright (2013) where penalty
functions are allowed to be non-convex, while the same convex loss function was used. Since
the overall objective function is non-convex, authors discuss error bounds obtained for any
stationary point, not a global minimum. In this aspect, our work closely follows this idea.
21


## Page 22


However, our setting diﬀers from Loh and Wainwright (2013) in two aspects: ﬁrst, the loss
function in our setting is non-convex, in contrast with a convex loss function (a negative
log-likelihood with a canonical link) with non-convex regularizer in Loh and Wainwright
(2013). Also, an additive penalty function was used in the work of Loh and Wainwright
(2013), but we consider a group-structured penalty.
After the initial draft of this paper was written, we became aware of two recent papers
(Elsener and van de Geer (2018); Mei et al. (2018)) which studied non-convex M-estimation
problems in various settings including binary linear classiﬁcation, where the goal is to
learn θ∗such that E[zi|xi] = σ(xT
i θ∗) for a known σ(·).
The proposed estimators are
stationary points of the optimization problem: argminθ n−1 Pn
i=1(zi −σ(xT
i θ))2 + λ∥θ∥1 in
both papers. As the focus of our paper is to learn a model with a structural contamination in
responses, our choice of mean and loss functions diﬀer from both papers. In particular, our
choice of mean function is diﬀerent from the sigmoid function, which was the representative
example of σ(·) in both papers, and we use the negative log-likelihood loss in contrast
to the squared loss. We establish error bounds by proving a modiﬁed restricted strong
convexity condition, which will be discussed shortly, while error bounds of the same rates
were established in Elsener and van de Geer (2018) through a sharp oracle inequality, and
a uniform convergence result over population risk in Mei et al. (2018).
Due to the non-convexity in the observed log-likelihood, we limit the feasible region Θ0
to
Θ0 := {θ ∈Rp; ∥θ∥2 ≤r0, ∥θ∥G,2,1 ≤Rn}
(35)
for theoretical convenience. Here r0, Rn > 0 must be chosen appropriately and we discuss
these choices later. Similar restriction is also assumed in Loh and Wainwright (2013).
22


## Page 23


3.1
Assumptions
We impose the following assumptions. First, we deﬁne a sub-Gaussian tail condition for a
random vector x ∈Rp; we say x has a sub-Gaussian tail with parameter σ2
x, if for any ﬁxed
v ∈Rp, there exists σx > 0 such that E[exp(t(x −E[x])T v)] ≤exp(t2∥v∥2
2σ2
x/2) for any
t ∈R. We recall that θ∗is the true parameter vector, which minimizes the population loss.
Assumption 1. The rows xi ∈Rp, i = 1, 2, . . . , n of the design matrix are i.i.d. samples
from a mean-zero distribution with sub-Gaussian tails with parameter σ2
x. Moreover, Σx :=
E[xixT
i ] is a positive deﬁnite and with minimum eigenvalue λmin(Σx) ≥K0 where K0 is a
constant bounded away from 0. We further assume that (xij)j∈gj are independent for all
j ∈gj and gj ∈G.
Similar assumptions appear in for e.g. Negahban et al. (2012). This restricted minimum
eigenvalue condition (see e.g. Raskutti et al. (2010) for details) is satisﬁed for weakly cor-
related design matrices. We further assume independence across covariates within groups
since sub-Gaussian concentration bound assuming independence within groups is required.
Assumption 2. For any r > 0, there exists Kr
1 such that maxi |xT
i θ| ≤Kr
1 a.s. for all θ
in the set {θ : ∥θ −θ∗∥2 ≤r ∩supp(θ −θ∗) ⊆gj for some gj ∈G}.
Assumption 2 ensures that |xT
i θ∗| is bounded a.s., which guarantees that the underlying
probability (1 + e−xT
i θ∗)−1 is between 0 and 1, and |xT
i θ| is also bounded within a compact
sparse neighborhood of θ∗which ensures concentration to the population loss. Comparable
assumptions are made in Elsener and van de Geer (2018); Mei et al. (2018) where similar
non-convex M estimation problems are investigated.
Assumption 3. The ratio of the number of labeled to unlabeled data , i.e. nℓ/nu is lower
bounded away from 0 and upper bounded for all n = nℓ+nu, as n →∞. Equivalently, there
is a constant K2 such that | log (nℓ/πnu) | ≤K2
23


## Page 24


Assumption 3 ensures that the number of labeled samples nℓis not too small or large
relative to n. The reason why nℓcan not be too large is that the labeled samples are only
positives and we need a reasonable number of negative samples which are a part of the
unlabeled samples.
Assumption 4 (Rate conditions). We assume a high-dimensional regime where both (n, p) →
∞and log p = o(n).
For G = ((g1, . . . , gJ), (wj)J
1 )) and m := maxj |gj|, we assume
J = Ω(nβ) for some β > 0, m = o(n ∧J), minj wj = Ω(1), and maxj wj = o(n ∧J).
Assumption 4 states standard rate conditions in a high-dimensional setting. In terms of
the group structure, we assume that growth of p is not totally attributed to the expansion
of a few groups; the number of groups J increases with n, and the maximum group size m
is of small order of both n and J. Also we note that a typical choice of wj =
p
|gj| satisﬁes
Assumption 4 because minj wj ≥1, maxj wj = √m and √m/n, √m/J = o(1).
Finally we deﬁne the restricted strong convexity assumption for a loss function following
the deﬁnition in Loh and Wainwright (2013).
Deﬁnition 3.1 (Restricted strong convexity). We say Ln satisﬁes a restricted strong
convexity (RSC) condition with respect to θ∗with curvature α > 0 and tolerance function
τ over Θ0 if the following inequality is satisﬁed for all θ ∈Θ0:
(▽Ln(θ) −▽Ln(θ∗))T ∆≥α∥∆∥2
2 −τ(∥∆∥G,2,1)
(36)
where ∆:= θ −θ∗and τ(∥∆∥G,2,1) = τ1∥∆∥2
G,2,1
log J + m
n
+ τ2∥∆∥G,2,1
r
log J + m
n
.
In the special case where ∥∆∥G,2,1 = ∥∆∥1 and hence τ(∥∆∥1) = τ1∥∆∥2
1
log p
n +τ2∥∆∥1
r
log p
n ,
similar RSC conditions were discussed in Negahban et al. (2012) and Loh and Wainwright
(2013) with diﬀerent τ and Θ0. One of the important steps in our proof is to prove that
RSC holds for the objective function Ln(θ).
24


## Page 25


3.2
Guarantee
Under Assumptions 1-4, we will show in Theorem 3.2 that the RSC condition holds with
high probability over {θ; ∥θ∥2 ≤r0} and therefore over Θ0, for Θ0 deﬁned in (35). Under
the RSC assumption, the following proposition, which is a modiﬁcation of Theorem 1 in
Loh and Wainwright (2013), provides ℓ1/ℓ2 and ℓ2 bounds of an error vector ˆ∆:= ˆθ −θ∗.
Recall that m = maxj |gj| (the size of the largest group) and J is the number of groups.
Proposition 3.1. Suppose the empirical loss Ln satisﬁes the RSC condition (36) with
τ(∥∆∥G,2,1) = τ1∥∆∥2
G,2,1
log J + m
n
+ τ2∥∆∥G,2,1
r
log J + m
n
over Θ0 where Θ0 is feasible
region for the objective (5), as deﬁned in (35), and the true parameter vector θ∗is feasible,
i.e. θ∗∈Θ0. Consider λ such that
4 max
(
∥▽Ln(θ∗)∥¯G,2,∞,
 
τ1
2Rn(log J + m)
n
+ τ2
r
(log J + m)
n
!)
≤λ.
(37)
Let ˆθ be a stationary point of (5). Then the following error bounds
∥ˆ∆∥2 ≤(max
j∈S wj)3√sλ
2α
and
∥ˆ∆∥G,1,2 ≤(max
j∈S wj)2 6sλ
α ,
(38)
hold where S := {j ∈(1, . . . , J); θ∗
gj ̸= 0} and s := |S|.
The proof for Proposition 3.1 is deferred to the supplementary material S2.3. From (38),
we note the squared ℓ2-error to grow proportionally with s and λ2. If θ∗∈Θ0 and the choice
of λ = Θ
q
log J+m
n

satisﬁes the inequality (37), we obtain squared ℓ2 error which scales
as slog J+m
n
, provided that the RSC condition holds over Θ0. In the case of lasso we recover
s log p
n
parametric optimal rate since J = p, m = 1.
With the choice of r0 ≥∥θ∗∥2 and Rn = Θ
q
n
log J+m

1, we ensure θ∗is feasi-
1We note that the group ℓ1 constraint is active only if
q
n
log J+m = O

(maxj wj)r0
√
J

.
If Rn ≥
(maxj wj)r0
√
J, Θ0 = {θ; ∥θ∥2 ≤r0, ∥θ∥G,2,1 ≤Rn} ⊇{θ; ∥θ∥2 ≤r0, ∥θ∥G,2,1 ≤(maxj wj)r0
√
J} ⊇
{θ; ∥θ∥2 ≤r0} by the ℓ1-ℓ2 inequality, i.e. if ∥θ∥2 ≤r0, ∥θ∥G,2,1 ≤(maxj wj)r0
√
J. The other direction is
trivial, and thus Θ0 is reduced to Θ0 = {θ; ∥θ∥2 ≤r0}.
25


## Page 26


ble and λ = Θ
q
log J+m
n

satisﬁes the inequality (37) with high probability.
Clearly

τ1
2Rn(log J+m)
n
+ τ2
q
log J+m
n

is of the order
q
log J+m
n
with the choice of Rn = Θ
q
n
log J+m

,
and following Lemma 3.1, we have ∥▽Ln(θ∗)∥¯G,2,∞= O
q
log J+m
n

with high probability.
Thus inequality (37) is satisﬁed with λ = Θ
q
log J+m
n

w.h.p. as well.
Lemma 3.1. Under Assumptions 1-4, for any given ϵ > 0, there is a positive constant c
such that
P
 
∥▽Ln(θ∗)∥¯G,2,∞≥c
r
log J + m
n
!
≤ϵ
given a sample size n ≳(log p + m) ∨(1/ϵ)1/β.
The proof for Lemma 3.1 is provided in the supplement S2.4. Now we state the main
theorem of this section which shows that RSC condition holds uniformly over a neighbor-
hood of the true parameter.
Theorem 3.2. For any given r > 0 and ϵ > 0, there exist strictly positive constants α, τ1
and τ2 depending on σx, K0, Kr
1 and K2 such that
(▽Ln(θ) −▽Ln(θ∗))T ∆≥α∥∆∥2
2 −τ1∥∆∥2
G,2,1
log J + m
n
−τ2∥∆∥G,2,1
r
log J + m
n
(39)
holds for all θ such that ∥∆∥2 := ∥θ −θ∗∥2 ≤r with probability at least 1 −ϵ, given (n, p)
satisfying n ≳(log J + m) ∨(1/ϵ)1/β.
The proof of Theorem 3.2 is deferred to the supplement S2.5. There are a couple of
notable remarks about Theorem 3.2 and Proposition 3.1.
• The application of the Proposition 3.1 requires for a RSC condition to hold over
a feasible region Θ0.
Setting r = 2r0 in Theorem 3.2, inequality (39) holds over
{θ; ∥θ −θ∗∥2 ≤2r0} w.h.p, therefore over Θ0 ⊆{θ; ∥θ −θ∗∥2 ≤2r0}.
26


## Page 27


• We discuss how underlying parameters r0, σx, and constants K0-K2 in Assump-
tions 1-3 are related to the ℓ2-error bound.
From Proposition 3.1, we see that
ℓ2-error is proportional to τ1/α and τ2/α. The proof of Theorem 3.2 reveals that
τ1/α ≲(σxK3/K0)2 and τ2/α ≲σx(1 + K2r0
1
)/K0L0, where L0 and K3 are also
constants deﬁned as L0 :=
inf
|u|≤K2+K2r0
1
+2r0K3
(eu/(1 + eu)2)(1 + eK2r0
1
+2r0K3)−2 and
K3 ≲σx log(σ2
x/K0)1/2. As L0 is inversely related to K2 and r0, ℓ2-error is propor-
tional to the r0, σx, K2r0
1
and K2 in Assumptions 2 and 3, but inversely related to
the minimum eigenvalue bound K0 in Assumption 1.
• The mean-squared error s log p
n
in the case of J = p is veriﬁed below in Fig. 2 and
both the mean-squared error and ℓ1 errors are minimax optimal for high-dimensional
linear regression (Raskutti et al. (2011)).
To validate the mean-squared error upper bound of
s log p
n
in Section 3, a synthetic
dataset was generated according to the logistic model (1) with p = 500 covariates and
X ∼N(0, I500×500). Varying s and n were considered to study the rate of convergence of
∥ˆθ −θ∗∥2. The ratio nℓ/nu was ﬁxed to be 1. For each dataset, ˆθ was obtained by applying
PUlasso algorithm with a lambda sequence λn := cs
q
log p
n
for a suitably chosen cs for each
s. We repeated the experiment 100 times and average ℓ2−error was calculated. In Figure
2, we illustrate the rate of convergence of ∥ˆθ −θ∗∥2. In particular, ∥ˆθ −θ∗∥2 against
q
s log p
n
is plotted with varying s and n. The error appears to be linear in
q
s log p
n
, and thus we also
empirically conclude that our algorithm achieves the optimal
q
s log p
n
rate.
4
Simulation study: Classiﬁcation performance
In this section, we provide a simulation study which validates the classiﬁcation performance
for PUlasso. In particular we provide a comparison in terms of classiﬁcation performance to
state-of-the-art methods developed in Du Marthinus et al. (2015); Elkan and Noto (2008);
27


## Page 28


G
G
G
G
G
G
G
G
0.3
0.6
0.9
0.02
0.04
0.06
0.08
slogp n
E^ θ^ −θ*
2
G s=3
s=5
s=7
Figure 2: ˆE[∥ˆθ −θ∥2] plotted against
p
s log p/n with ﬁxed p=500 and varying s and n
Liu et al. (2003). The focus of this section is classiﬁcation rather than variable selection since
many of the state-of-the-art methods we compare to are developed mainly for classiﬁcation
and are not developed for variable selection.
4.1
Comparison methods
Our experiments compare six algorithms: (i) logistic regression model assuming we know
the true responses (oracle estimator); (ii) our PUlasso algorithm; (iii) a bias-corrected
logistic regression algorithm in Elkan and Noto (2008); (iv) a second algorithm from Elkan
and Noto (2008) that is eﬀectively a one-step EM algorithm; (v) the biased SVM algorithm
from Liu et al. (2003) and (vi) the PU-classiﬁcation algorithm based on an asymmetric loss
from Du Marthinus et al. (2015).
The biased SVM from Liu et al. (2003) is based on the supported vector machine (SVM)
classiﬁer with two tuning parameters which parameterize mis-classiﬁcation costs of each
kind. The ﬁrst algorithm from Elkan and Noto (2008) estimates label probabilities P(z =
1|x) and corrects the bias in the classiﬁer via the estimation of P(z = 1|y = 1) under the
28


## Page 29


assumption of a disjoint support between P(x|y = 1) and P(x|y = 0). Their second method
is a modiﬁcation of the ﬁrst method; a unit weight is assigned to each labeled sample, and
each unlabeled example is treated as a combination of a positive and negative example
with weight P(y = 1|x, z = 0) and P(y = 0|x, z = 0), respectively. Du Marthinus et al.
(2015) suggests using asymmetric loss functions with ℓ2-penalty. Asymmetric loss function
is considered to cancel the bias induced by separating positive and unlabeled samples rather
than positive and negative samples. Any convex surrogate of 0-1 loss function can be used
for the algorithm. There is a publicly available matlab implementation of the algorithm
when a surrogate is the squared loss on the author’s webpage2 and since we use their code
and implementation, the squared loss is considered.
4.2
Setup
We consider a number of diﬀerent simulation settings: (i) small and large p to distinguish
the low and high-dimensional setting; (ii) weakly and strongly separated populations; (iii)
weakly and highly correlated features; and (iv) correctly speciﬁed (logistic) or mis-speciﬁed
model. Given dimensions (n, p), sparsity level s, predictor auto-correlation ρ, separation
distance d, and model speciﬁcation scheme (logistic, mis-speciﬁed), our setup is the follow-
ing:
• Choose the active covariate set S ⊆{1, 2, . . . , p} by taking s elements uniformly at
random from (1, 2, . . . , p). We let true θ∗∈Rp such that θ∗
j = 1S(j).
• Draw samples x ∈Rp, i.i.d from PX = 0.5P1 + 0.5P0 where P1 := N(µ1, Σρ), P0 :=
N(µ2, Σρ). More concretely, ﬁrstly draw u ∼Ber(0.5). If u = 1, draw x from P1 and
draw x from P0 otherwise.
– Mean vectors µ1, µ2 ∈Rp are chosen so that they are s-sparse, i.e. supp(µi) =
2available at http://www.ms.k.u-tokyo.ac.jp/software.html
29


## Page 30


S, E[∥µ1 −µ2∥2
2] = d2 and variance of µi does not depend on d. Speciﬁcally,
we sample µ1, µ2 such that for j ∈S, we let µ1j ∼N(
p
(2d2 −1)/8s, 1/
√
8s),
µ2j = −µ1j, and for j /∈S, µij = 0 for i ∈(1, 2).
– A covariance matrix Σρ ∈Rp×p is taken to be Σρ,ij = Kρρ|i−j| where Kρ is
chosen so that 1T
SΣρ1S = s. This scaling of Σρ is made to ensure that the signal
strength V ar(xT θ∗) = 1T
SΣρ1S stays the same across ρ.
• Draw responses y ∈{0, 1}. If scheme = logistic, we draw y such that y ∼Ber(Pθ∗(y =
1|x)) where Pθ∗(y = 1|x) = 1/(1+exp(−θ∗T x)). In contrast, if scheme = mis-speciﬁed,
we let y = 1 if x was drawn from P1, and zero otherwise; i.e. y = 1{u = 1}.
To compare performances both in low and high dimensional setting, we consider (p =
10, s = 5) and (p = 5000, s = 5). We set the sample size nℓ= nu = 500 in both cases. Auto-
correlation level ρ takes values in (0, 0.2, 0.4, 0.6, 0.8). In the high dimensional setting, we
excluded algorithm (v), since (v) requires a grid search over two dimensions, which makes
the computational cost prohibitive. For algorithms (i)-(iv), tuning parameters λ are chosen
based on the 10-fold cross validation.
4.3
Classiﬁcation comparison
We use two criteria, mis-classiﬁcation rate and F1 score, to evaluate performances. F1 is the
harmonic mean of the precision and recall, which is calculated as F1 := 2· precision+recall
precision·recall .
The F1 score ranges from 0 to 1, where 1 corresponds to perfect precision and recall.
Experiments are repeated 50 times and the average score and standard errors are reported.
The result for the mis-classiﬁcation rate under correct model speciﬁcation is displayed in
Figure 3.
Not surprisingly the oracle estimator has the best accuracy in all cases. PUlasso and
algorithm (vi) performs almost as well as the oracle in the low-dimensional setting and
30


## Page 31


G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
d = 1.5
d = 2.5
d = 3.5
p = 10
p = 5000
0.0 0.2 0.4 0.6 0.8 0.0 0.2 0.4 0.6 0.8 0.0 0.2 0.4 0.6 0.8
0.1
0.2
0.3
0.4
0.5
0.1
0.2
0.3
0.4
0.5
rho
misclassification rate
Algorithm
G (i) Reference
(ii) PUlasso
(iii) EN1
(iv) EN2
(v) biased−SVM
(vi) PNS
Figure 3: Mis-classiﬁcation rates of algorithms (i)-(vi) under correct (logistic) model spec-
iﬁcation. Each error bar represents two standard errors of the mean.
better than remaining methods in most cases. It must be pointed out that both PUlasso
and algorithm (vi) use additional knowledge π of the true prevalence in the unlabeled
samples. PUlasso performs best in the high-dimensional setting while the performance of
algorithm (vi) becomes signiﬁcantly worse because estimation errors can be greatly reduced
by imposing many 0’s on the estimates in PUlasso due to the ℓ1-penalty (compared to ℓ2-
penalty in algorithm (vi)). The performance of (iii)-(iv) are greatly improved when positive
and negative samples are more separated (large d), because algorithms (iii)-(iv) assume
disjoint support between two distributions. The algorithms show similar performance when
evaluated with the F1 score metric and in the mis-speciﬁed setting. Due to space constraints,
we defer the full set of remaining results in the supplementary material Section S3.
31


## Page 32


5
Analysis of beta-glucosidase sequence data
Our original motivation for developing the PUlasso algorithm was to analyze a large-
scale dataset with positive and unlabeled responses developed by the lab of Dr.Philip
Romero (Romero et al. (2015)). The prior EM algorithm approach of Ward et al. (2009)
did not scale to the size of this dataset. In this section, we discuss the performance of our
PUlasso algorithm on a dataset involving mutations of a natural beta-glucosidase (BGL)
enzyme. To provide context, BGL is a hydrolytic enzyme involved in the deconstruction of
biomass into fermentable sugars for biofuel production. Functionality of the BGL enzyme
is measured in terms of whether the enzyme deconstructs disaccharides into glucose or not.
Dr. Romero used a microﬂuidic screen to generate a BGL dataset containing millions of
sequences (Romero et al. (2015))3.
Main eﬀects and two-way interaction models are ﬁtted using our PUlasso algorithm
with ℓ1 and ℓ1/ℓ2 penalties (we discuss how the groups are chosen shortly) over a grid of λ
values. We test stability of feature selection and classiﬁcation performance using a modiﬁed
ROC and AUC approach. Finally a scientiﬁc validation is performed based on a follow-up
experiment conducted by the Romero lab. The variables selected by PUlasso were used to
design a new BGL enzyme and the performance is compared to the original BGL enzyme.
5.1
Data description
The dataset consists of nℓ= 2647877 labeled and functional sequences and nu = 1567203
unlabeled sequences where each of the observation σ = (σ1, . . . , σ500) is a sequence of amino
acids of length d = 500. Each of the position σj ∈(A, R, . . . , V, ∗) takes one of M = 21
discrete values, which correspond to the 20 amino acids in the DNA code and an extra to
include the possibility of a gap(∗).
3The raw data is available in https://github.com/RomeroLab/seq-fcn-data.git
32


## Page 33


Another important aspect of the millions of sequences generated is that a “base wild-
type BGL sequence” was considered and known to be functional (y = 1), and the millions
of sequences were generated by mutating the base sequence. Single mutations (changing
one position from the base sequence) and double mutations (changing two positions) from
the base sequence were common but higher-order mutations were not prevalent using the
deep mutational scanning approach in Romero et al. (2015). Hence the sequences generated
were not random samples across the entire enzyme sequence space, but rather very local
sequences around the wild-type sequence.
Hence the number of possible mutations in
each position and consequently the total number of observed sequences is also reduced
dramatically. With this dataset, we want to determine which mutations should be applied
to the wild-type BGL sequence.
Categorical variables σ are converted into indicator variables: x = (1{σj = l})j,l where
1 ≤j ≤500, l ∈(A, R, . . . , V, ∗)\(σWT
l
) for the main-eﬀects model, x = (1{σj = l}, 1{σj =
l, σk = m})j,k,l,m where 1 ≤j, k ≤500, j ̸= k, l, m ∈(A, R, . . . , V, ∗) \ (σWT
l or m) for the pair-
wise interaction models, where σWT
l
represents the amino acid of the wild-type sequence
at the lth position. In other words, each variable corresponds to an indicator of mutation
from the base sequence or interaction between mutations. Although there are in princi-
ple p ≈d(M −1) variables for a main-eﬀects model and p ≈d2(M −1)2 if we include
main-eﬀects and two-way interactions, there are many amino acids that never appear in
any position or appear only a small number of times. For features corresponding to the
main-eﬀects (1{σj = l} for some j and l), those sparse features are aggregated within
each position until the number of mutations of the aggregated column reaches 100 or 1%
of the total number of mutations in each position; accordingly, each aggregated column
is an indicator of any mutations to those sparse amino acids. For two-way interactions
features (1{σj = l, σk = m} for some j, k, l, and m), sparse features (≤25 out of 4215080
samples) are simply removed from the feature space. Using this basic pre-processing we ob-
33


## Page 34


tained only 3075 corresponding to single mutations and 930 binary variables corresponding
to double mutations. They correspond to 500 unique positions and 820 two-way interac-
tions between positions respectively. As mentioned earlier, we consider both ℓ1 and group
ℓ1/ℓ2 penalties. We use the ℓ1-penalty for the main-eﬀects model and the ℓ1/ℓ2 for the
two-way interaction models. For the two-way interaction model each group gj corresponds
to a diﬀerent position (500 total) and pair of positions (820 total) where mutations occur
in the pre-processed design matrix and the group size |gj| corresponds to the number of
diﬀerent observed mutations in each position or pair of mutations in pair of positions (for
this dataset m = maxj |gj| = 8). Higher-order interactions were not modeled as they did
not frequently arise. Hence the main-eﬀects and two-way interaction model we consider
have p = 3076 (1 + 3075) and p = 4006 (1 + 3075 + 930) and J = 1320 (500 + 820) groups
respectively. In summary, we consider the following two models and corresponding design
matrices
Xmain := [Intercept(1)+ main eﬀects(3075)] ∈{0, 1}4215080×3076
Xint := [Intercept(1)+ main eﬀects(3075)+ two way interactions(930)] ∈{0, 1}4215080×4006
and the response vector z = [1, . . . , 1, 0, . . . , 0]T ∈{0, 1}4215080.
5.2
Classiﬁcation validation and model stability
Next we validate the classiﬁcation performance for both the main-eﬀect and two-way inter-
action models. We ﬁt models using 90% of the randomly selected samples both from the
positive and unlabeled set and use Area Under the ROC Curve (AUC) to evaluate the classi-
ﬁcation performance on the 10% of the hold-out set. Since positive and negative samples are
mixed in the unlabeled test dataset this is a non-trivial task with presence-only responses.
A naive approach is to treat unlabeled samples as negative and estimate AUC, but if we
do so, the AUC is inevitably downward-biased because of the inﬂated false positive (FP)
34


## Page 35


rate. We note that a true positive (TP) rate can be estimated in an unbiased manner using
positive samples. To adjust such bias, we follow the methodology suggested in Jain et al.
(2017) and adjust false positive rate and AUC value using the following equation:
FPadj = FPnaive −πTP
1 −π
,
AUCadj = AUCnaive −π/2
1 −π
where π is the prevalence of positive samples.
AUC(M)=0.7933
AUC(M+I)=0.7938
0.00
0.25
0.50
0.75
1.00
0.00
0.25
0.50
0.75
1.00
False positive
True positive
Model
M
M+I
Figure 4: ROC curves of main eﬀects (M) and two-way interaction model (M+I) with λ
chosen based on 10-fold cross validation.
As Fig. 4 shows, we have a signiﬁcant improvement in AUC over random assign-
ment (AUC=.5) in both the main eﬀect (AUC=.7933) and two-way interaction (AUC=.7938)
models. The performances of the two models in terms of AUC values are very similar at
their best λ values chosen by 10-fold cross validation. This is not very surprising as only a
small number of two-way interactions are observed in the experiments.
We also examined the stability of the selected features for both models as the training
35


## Page 36


data changes.
Following the methodology of
Kalousis et al. (2007), we measure sim-
ilarity between two subsets of features s, s′ using SS(s, s′) deﬁned as SS(s, s′) := 1 −
|s| + |s′| −2|s ∩s′|
|s| + |s′| −|s ∩s′| . SS takes values in [0, 1], where 0 means that there is no overlap be-
tween the two sets, and 1 that the two sets are identical. Ss is computed for each pair
of two training folds (i.e. we have 9·10
2
pairs) using selected features and computed values
are ﬁnally averaged over all pairs. Feature selection turned out to be very stable across
all tuning parameter λ values: on average we had about 95% overlap of selection in main
eﬀect model (M) and about 98% overlap in main eﬀect+interaction model (M+I). Stability
score is higher in the latter model since we do a feature selection on groups, whose number
is much less than individual variables (1320 groups versus 3076 individual variables).
1st Qu.
Median
Mean
3rd Qu.
M
93.3%
94.9%
94.9%
96.8%
M+I
97.9%
98.8%
98.4%
99.3%
Table 3: Summary of stability scores across all tuning parameter λ values
5.3
Scientiﬁc validation: Designed BGL sequence
Finally we provide a scientiﬁc validation of the mutations estimated by our PUlasso algo-
rithm. In particular, we ﬁt the model with the PUlasso algorithm and selected the best
λ = 0.0001 based on the 10-fold cross validation. We use the top 10 mutations based on the
largest size of coeﬃcients with positive signs from our PUlasso algorithm because we are
interested in mutations that enhance the performance of the sequence. Dr. Romero’s lab
designed the BGL sequence with the 10 positive mutations from Table 4. This sequence was
synthesized, expressed, and assayed for its hydrolytic activity. Hence the designed sequence
has 10 mutations compared to the wild-type (base) BGL sequence.
Figure 5 shows ﬁrstly that the designed protein sequence folds which in itself is re-
36


## Page 37


markable given that 10 positions are mutated. Secondly Figure 5 shows that the designed
sequence decomposes disaccharides into glucose more quickly than the wild-type sequence.
These promising results suggest that our variable selection method is able to identify posi-
tions of the wild-type sequences with improved functionality.
Base/Position/Mutated
T197P
E495G
K300P
A38G
G327A
S486P
A150D
T478S
D164E
D481N
Table 4: Ten positive mutations
Figure 5: kinetics
10 positive mutations used in the lab(Base state/Position/Mutated state) and kinetics of
designed BGL enzyme versus wild-type (WT) BGL sequence. The designed BGL enzyme
based on mutations from Table 4 displays faster kinetics than the WT BGL sequence.
6
Conclusion
In this paper we developed the PUlasso algorithm for both variable selection and classiﬁ-
cation for high-dimensional classiﬁcation with presence-only responses. Theoretically, we
showed that our algorithm converges to a stationary point and every stationary point within
a local neighborhood of θ∗achieves an optimal mean squared error (up to constant). We
also demonstrated that our algorithm performs well on both simulated and real data. In
particular, our algorithm produces more accurate results than the existing techniques in
simulations and performs well on a real biochemistry application.
37


## Page 38


References
M. Blaz`ere, J. M. Loubes, and F. Gamboa. Oracle Inequalities for a Group Lasso Proce-
dure Applied to Generalized Linear Models in High Dimension. IEEE Transactions on
Information Theory, 60(4):2303–2318, April 2014.
Patrick Breheny and Jian Huang. Group descent algorithms for nonconvex penalized linear
and logistic regression models with grouped predictors. Statistics and Computing, 25(2):
173–187, 2013.
Plessis Du Marthinus, Gang Niu, and Masashi Sugiyama. Convex Formulation for Learning
from Positive and Unlabeled Data. Proceedings of The 32nd International Conference on
Machine Learning, pages 1386–1394, 2015.
Charles Elkan and Keith Noto.
Learning Classiﬁers from Only Positive and Unlabeled
Data. In Proceedings of the 14th ACM SIGKDD International Conference on Knowledge
Discovery and Data Mining, KDD ’08, pages 213–220, New York, NY, USA, 2008. ACM.
Andreas Elsener and Sara van de Geer. Sharp oracle inequalities for stationary points of
nonconvex penalized m-estimators. February 2018.
Ludwig Fahrmeir and Heinz Kaufmann. Consistency and Asymptotic Normality of the
Maximum Likelihood Estimator in Generalized Linear Models. The Annals of Statistics,
13(1):342–368, March 1985.
Douglas M Fowler and Stanley Fields. Deep mutational scanning: a new style of protein
science. Nature Methods, 11:801–807, 2014.
Jerome Friedman, Trevor Hastie, Holger H¨oﬂing, and Robert Tibshirani. Pathwise coordi-
nate optimization. The Annals of Applied Statistics, 1(2):302–332, 2007.
38


## Page 39


Jerome Friedman, Trevor Hastie, and Robert Tibshirani. Regularization Paths for Gen-
eralized Linear Models via Coordinate Descent. Journal of Statistical Software, 33(1),
2010.
Ryan T Hietpas, Jeﬀrey D Jensen, and Daniel N A Bolon. Experimental illumination of a
ﬁtness landscape. Proceedings of the National Academy of Sciences of the United States
of America, 108(19):7896–7901, 2011.
Jian Huang, Patrick Breheny, and Shuangge Ma. A Selective Review of Group Selection in
High-Dimensional Models. Statistical Science, 27(4):481–499, November 2012.
Shantanu Jain, Martha White, and Predrag Radivojac. Recovering True Classiﬁer Perfor-
mance in Positive-Unlabeled Learning. In Proceedings of the Thirty-First AAAI Con-
ference on Artiﬁcial Intelligence, February 4-9, 2017, San Francisco, California, USA.,
pages 2066–2072, 2017.
Sham Kakade, Ohad Shamir, Karthik Sindharan, and Ambuj Tewari. Learning Exponential
Families in High-Dimensions: Strong Convexity and Sparsity.
In Proceedings of the
Thirteenth International Conference on Artiﬁcial Intelligence and Statistics, pages 381–
388, March 2010.
Alexandros Kalousis, Julien Prados, and Melanie Hilario. Stability of Feature Selection
Algorithms: A Study on High-dimensional Spaces. Knowl. Inf. Syst., 12(1):95–116, May
2007.
B. Krishnapuram, L. Carin, M. A. T. Figueiredo, and A. J. Hartemink. Sparse multinomial
logistic regression: fast algorithms and generalization bounds. IEEE Transactions on
Pattern Analysis and Machine Intelligence, 27(6):957–968, June 2005.
Tony Lancaster and Guido Imbens. Case-control studies with contaminated controls. Jour-
nal of Econometrics, 71(1):145 –160, 1996.
39


## Page 40


Kenneth Lange, David R. Hunter, and Ilsoon Yang. Optimization Transfer Using Surrogate
Objective Functions. Journal of Computational and Graphical Statistics, 9(1):1–20, 2000.
Su-in Lee, Honglak Lee, Pieter Abbeel, and Andrew Y. Ng. Eﬃcient l1 regularized logis-
tic regression. In In Proceedings of the Twenty-ﬁrst National Conference on Artiﬁcial
Intelligence (AAAI-06), pages 1–9, 2006.
Bing Liu, Yang Dai, Xiaoli Li, Wee Sun Lee, and Philip Yu. Building Text Classiﬁers
Using Positive and Unlabeled Examples. Proceedings of the Third IEEE International
Conference on Data Mining (ICDM’03), 2003.
P-L. Loh and M. J. Wainwright. Regularized M-estimators with nonconvexity: Statistical
and algorithmic theory for local optima. Journal of Machine Learning Research, 1:1–9,
2013.
P. McCullagh and J. A. Nelder. Generalized Linear Models, volume 28. 1989.
Song Mei, Yu Bai, and Andrea Montanari. The landscape of empirical risk for nonconvex
losses. Ann. Stat., 46(6A):2747–2774, December 2018.
Lukas Meier, Van De S Geer, Peter Buhlmann, Sara Van De Geer, and Peter B¨uhlmann.
The group lasso for logistic regression. Journal of the Royal Statistical Society, Series B,
70(1):53–71, 2008.
S. N. Negahban, R. Pradeep, Bin Yu, and M. J. Wainwright. A Uniﬁed Framework for
High-Dimensional Analysis of M-Estimators with Decomposable Regularizers. Statistica
Sinica, 27(4):538–557, 2012.
J. M. Ortega and W. C. Rheinboldt. Iterative solution of nonlinear equations in several
variables. Classics in applied mathematics. SIAM, New York, 2000.
40


## Page 41


A. T. Puig, A. Wiesel, G. Fleury, and A. O. Hero. Multidimensional Shrinkage-Thresholding
Operator and Group LASSO Penalties. IEEE Signal Processing Letters, 18(6):363–366,
June 2011.
G. Raskutti, M. J. Wainwright, and B. Yu. Restricted eigenvalue conditions for correlated
Gaussian designs. Journal of Machine Learning Research, 11:2241–2259, 2010.
Garvesh Raskutti, Martin J. Wainwright, and Bin Yu. Minimax Rates of Estimation for
High-Dimensional Linear Regression Over ℓq-Balls. IEEE Transactions on Information
Theory, 57(10):6976–6994, October 2011.
Philip A Romero, Tuan M Tran, and Adam R Abate. Dissecting enzyme function with
microﬂuidic-based deep mutational scanning. Proceedings of the National Academy of
Sciences of the United States of America, 112(23):7159–7164, 2015.
Noah Simon and Robert Tibshirani. Standardization and the Group Lasso Penalty. Sta-
tistica Sinica, 22(3):1–21, 2012.
Robert Tibshirani, Jacob Bien, Jerome Friedman, Trevor Hastie, Noah Simon, Jonathan
Taylor, and Ryan J. Tibshirani.
Strong rules for discarding predictors in lasso-type
problems. Journal of the Royal Statistical Society. Series B: Statistical Methodology, 74
(2):245–266, 2012.
Sara A. van de Geer. High-dimensional generalized linear models and the lasso. The Annals
of Statistics, 36(2):614–645, April 2008.
Gill Ward, Trevor Hastie, Simon Barry, Jane Elith, and John R. Leathwick. Presence-only
data and the em algorithm. Biometrics, 65(2):554–563, 2009.
Tong Tong Wu and Kenneth Lange. Coordinate descent algorithms for lasso penalized
regression. The Annals of Applied Statistics, 2(1):224–244, 2008.
41


## Page 42


Ming Yuan and Yi Lin. Model selection and estimation in regression with grouped variables.
J. R. Statist. Soc. B, 68(1):49–67, 2006.
42


## Page 43


SUPPLEMENTARY MATERIAL
S1
Proofs for results in Section 2
S1.1
Proof of Proposition 2.1
We prove (i) in Proposition 2.1 for both Algorithm 1 and 2. First we deﬁne Q, eQ, H as
follows:
Q(θ; θm) := n−1Eθm[log Lf(θ)|zn
1 , xn
1]
eQ(θ; θm) := −Q(θ; θm) + Pλ(θ)
H(θ; θm) := n−1Eθm[log Pθ(yn
1 |zn
1 , xn
1)|zn
1 , xn
1].
Note that for any θm, Fn(θ) = eQ(θ; θm) + H(θ; θm) holds and H(θm; θm) ≥H(θ; θm) by
Jensen’s inequality. Also since θm+1 is a minimizer of eQ(θ; θm), we have
Fn(θm+1) = eQ(θm+1; θm) + H(θm+1; θm) ≤eQ(θm; θm) + H(θm; θm) = Fn(θm).
(S1)
To show that the inequality is strict, it suﬃces to show that if θm ̸∈S, θm is not a stationary
point of eQ. Since θm ̸∈S, there exists θ′ such that
▽Fn(θm)T (θ′ −θm) < 0, ∀▽Fn(θm) ∈∂Fn(θm)
(S2)
Since θm is a maximizer of H(·; θm), ▽H(θm; θm) = 0. Then ∂Fn(θm) = ∂eQ(θm; θm). Thus
by (S2), θm is not a stationary point of eQ(·; θm).
For Algorithm 2 (PUlasso algorithm), since Q is a surrogate function of Q which satisﬁes
following two properties
Q(θm; θm) = Q(θm; θm),
Q(θ; θm) ≤Q(θ; θm), ∀θ
(S3)
1


## Page 44


and θm+1 is a minimizer of −Q(θ; θm) + Pλ(θ), we have
Fn(θm) = −Q(θm; θm) + Pλ(θm) + H(θm; θm)
= −Q(θm; θm) + Pλ(θm) + H(θm; θm)
≥−Q(θm+1; θm) + Pλ(θm+1) + H(θm; θm)
≥−Q(θm+1; θm) + Pλ(θm+1) + H(θm+1; θm) = Fn(θm+1)
The strict inequality follows from the fact that ▽Q(θm; θm) = ▽Q(θm; θm).
Now we address (ii) and (iii) in Proposition 2.1. Using the same argument as in Wu
(1983), we appeal to the global convergence theorem stated below as Theorem S1.1 in Zang-
will (1969) with Γ = S, α = Fn, and letting A be a mapping from θm to θm+1 deﬁned by
Algorithm 1 or 2. As stated in Wu (1983), condition (iii) in Theorem S1.1 follows from the
continuity of −Q(θ, θ′) + Pλ(θ) or −¯Q(θ; θ′) + Pλ(θ) in both θ, θ′. Therefore, if we show
that f
Θ0 is compact, both (ii) and (iii) follow from the fact that (θm)∞
m=0 lie in a compact
set. Since f
Θ0 ⊆Rp it suﬃces to show that f
Θ0 is closed and bounded in Rp. f
Θ0 is bounded
since Fn(θ) →∞whenever ∥θ∥2 →∞since ∥θ∥G,2,1 ≥minj wj∥θ∥2 →∞. For closedness
of the set, consider (θk)k≥1 such that θk ∈f
Θ0 and θk →θ′. We have Fn(θk) ≤Fn(θnull) for
all k. Then by the continuity of Fn, Fn(θ′) ≤Fn(θnull) thus θ′ ∈f
Θ0.
Theorem S1.1 (Global Convergence Theorem, Zangwill (1969)). Let the sequence {xk}∞
k=0
be generated by xk+1 ∈A(xk), where A is a point-to-set map on X. Let a solution set Γ ∈X
be given, and suppose that:
(i) The sequence {xk}∞
k=0 ⊂S for S ⊂X a compact set.
(ii) There is a continuous function α on X such that (a) if x ̸∈Γ, then α(y) < α(x) for
all y ∈A(x). (b) if x ∈Γ, then α(y) ≤α(x) for all y ∈A(x).
(iii) The mapping A is closed at all points of X \ Γ.
2


## Page 45


Then all the limit points of any convergent subsequence of (xk)∞
k=0 are in the solution set
Γ and α(xk) converges monotonically to α(x) for some x ∈Γ.
S2
Proofs for results in Section 3
S2.1
Derivation of the log-likelihood in the form of GLMs
log L(θ; x, z, s = 1) = log
 Y
i
Pθ(zi|xi, si = 1)
!
=
X
i
zi log Pθ(zi = 1|xi, si = 1) + (1 −zi) log Pθ(zi = 0|xi, si = 1)
=
X
i
zi log Pθ(zi = 1|xi, si = 1)
Pθ(zi = 0|xi, si = 1) + log Pθ(zi = 0|xi, si = 1).
From Lemma 2.1, we have Pθ(z = 1|x, s = 1) =
nl
πnu eθT x
1 + (1 +
nl
πnu )eθT x . Then,
log Pθ(z = 1|x, s = 1)
Pθ(z = 0|x, s = 1) = log
nl
πnu eθT x
1 + eθT x = log nl
πnu
+ θT x −log(1 + eθT x).
and,
log Pθ(z = 0|x, s = 1) = −log
 
1 + (1 +
nl
πnu )eθT x
1 + eθT x
!
= −log
 
1 +
nl
πnu eθT x
1 + eθT x
!
= −log

1 + elog
nl
πnu +θT x−log(1+eθT x)

.
Therefore we obtain,
log
 Y
i
Pθ(zi|xi, si = 1)
!
=
X
i
ziηi −log(1 + eηi)
where ηi = log
nl
πnu + θT x −log(1 + eθT x).
3


## Page 46


S2.2
Useful inequalities and technical lemmas
In this section, we provide some results that will be useful for our proofs. First we state the
symmetrization inequality, which shows relationships between empirical and Rademacher
processes.
Theorem S2.1. (Symmetrization theorem[van der Vaart and Wellner (1996)]) Let U1, . . . , Un
be independent random variables with values in U and (ϵi) be an i.i.d. sequence of Rademacher
variables, which take values ±1 each with probability 1/2. Let Γ be a class of real-valued
functions on U. then
E
 
sup
γ∈Γ

n
X
i=1
{γ(Ui) −E(γ(Ui))}

!
≤2E
 
sup
γ∈Γ

n
X
i=1
ϵiγ(Ui)

!
.
The next theorem is Ledoux-Talagrand contraction theorem.
The stated version is
Theorem 2.2 in Koltchinskii (2011), which allows T be any subset in Rn, thus slightly more
general than the original theorem in Ledoux and Talagrand (1991) where T needs to be
bounded.
Theorem S2.2. (Contraction theorem[Ledoux and Talagrand (1991)]) Let T ⊂Rn and let
ϕi : R →R, i = 1, . . . , n be contractions which satisfy |ϕi(s) −ϕi(t)| ≤|s −t|, s, v ∈R and
ϕi(0) = 0. Let (ϵi) be independent Rademacher random variables. Then
E
 
sup
t∈T

n
X
i=1
ϵiϕi(ti)

!
≤2E
 
sup
t∈T

n
X
i=1
ϵiti

!
.
Finally, we state the bounded diﬀerences inequality, also sometimes called as Hoeﬀding-
Azuma inequality.
Theorem S2.3. (Bounded diﬀerence inequality[McDiarmid (1989)]) Let X1, . . . , Xn be
arbitrary independent random variables on set A and ϕ : An →R satisfy the bounded
diﬀerence assumption: there exists constants ci, i = 1, . . . , n such that for all i = 1, . . . , n
4


## Page 47


and all x1, x2, . . . , xi, x′
i, . . . , xn,
|ϕ(x1, . . . , xi, . . . , xn) −ϕ(x1, . . . , x′
i, . . . , xn)| ≤ci
Then ∀t > 0,
P (ϕ(X1, . . . , Xn) −E[ϕ(X1, . . . , Xn)] ≥t) ≤exp(−2t2/
n
X
i=1
c2
i )
Now we state and prove some useful results about sub-Gaussian and sub-exponential
random variables.
Lemma S2.4. Let v, u ∈Rp and (g1, . . . , gJ) be a partition of (1, . . . , p).
For G =
((g1, . . . , gJ), (wj)J
1 ) and ¯G = ((g1, . . . , gJ), (w−1
j )J
1 ) such that all gj are non-empty and
wj > 0, |vT u| ≤∥v∥G,2,1∥u∥¯G,2,∞.
Proof. We note ∥v∥G,2,1 = PJ
j=1 wj∥vgj∥2 and ∥u∥¯G,2,∞:= max1≤j≤J∥w−1
j ugj∥2. By Cauchy-
Schwarz inequality, we have
|vT u| ≤
J
X
j=1
|wjvT
gjw−1
j ugj| ≤
J
X
j=1
∥wjvgj∥2∥w−1
j ugj∥2.
Taking the maximum of the second quantity,
|vT u| ≤max
1≤j≤J∥w−1
j ugj∥2
J
X
j=1
wj∥vgj∥2 = ∥v∥G,2,1∥u∥¯G,2,∞.
Lemma S2.5. Let x ∈Rp such that xT v ∼subG(∥v∥2
2σ2
x) for any ﬁxed v ∈Rp and
E[x] = 0. For any i ∈(1, . . . , p), k ≥1,
E[|xi|k] ≤k(2σ2
x)k/2Γ(k/2).
5


## Page 48


Proof. Taking v = ei where ei is an ith coordinate vector, we have E(exp(tvT x)) =
E[exp(txi)] ≤exp(t2σ2
x/2) for t ∈R. Then following a standard argument for sub-Gaussian
random variables,
E[|xi|k] =
Z ∞
s=0
P(|xi| ≥s1/k)ds
≤2
Z ∞
s=0
exp(−s2/k/2σ2
x)ds
= k(2σ2
x)k/2
Z ∞
s=0
e−uuk/2−1du = k(2σ2
x)k/2Γ(k/2)
where the third inequality comes from the change of variable u = s2/k/2σ2
x.
The next lemma concerns distribution of x ◦x = [x2
1, . . . , x2
s] for independent sub-
Gaussian (xi)s
i=1.
Lemma S2.6. Let x ∈Rs such that xT v ∼subG(∥v∥2
2σ2
x) for any ﬁxed v ∈Rs and
E[x] = 0. Also, assume (xi)s
i=1 are independent. Then we have vT (x ◦x) ∼subExp(ν, b)
with ν = 16σ2
x∥v∥2, b = 16σ2
x∥v∥∞for any ﬁxed v ∈Rs.
Proof. Let z := x ◦x −E[x ◦x]. For any given v ∈Rs and t > 0,
E[exp(tvT z)] = E[exp(tv1z1 + . . . tvszs)]
=
s
Y
i=1
E[exp(tvizi)]
where we use independence. Then by Taylor series expansion,
E[exp(tvT z)] =
s
Y
i=1
E

1 + tvizi + t2(vizi)2
2
+ . . .

=
s
Y
i=1
 
1 +
∞
X
k=2
tkE
 vi(x2
i −E[x2
i ])
k
k!
!
By Jensen’s inequality, we have,
E(vix2
i −E[vix2
i ])k ≤|vi|k2k−1(E[x2k
i ] + E[x2
i ]k),
6


## Page 49


and by applying Jensen’s inequality again, we get
E[exp(tvT z)] ≤
s
Y
i=1
 
1 +
∞
X
k=2
tk|vi|k2kE[x2k
i ]
k!
!
.
(S4)
We let ti = t|vi|. By Lemma S2.5, we have,
E[x2k
i ] ≤(2k)(2σ2
x)kΓ(k) = 2(k!)(2σ2
x)k
(S5)
Substituting (S5) into (S4),
E[exp(tvT z)] ≤
s
Y
i=1
 
1 +
∞
X
k=2
tk
i 8k(σ2
x)k
!
=
s
Y
i=1
 
1 + (8tiσ2
x)2
∞
X
k=0
(8tiσ2
x)k
!
≤
s
Y
i=1
 1 + 128t2
i σ4
x

if t|vi| ≤1/(16σ2
x), for all i. By the fact that 1 + 128t2
i σ4
x ≤exp(128t2
i σ4
x)
E[exp(tvT z)] ≤
s
Y
i=1
exp(128t2
i σ4
x) = exp(
s
X
i=1
128t2v2
i σ4
x) = exp(128t2∥v∥2
2σ4
x)
for t ≤1/(16σ2
x maxi |vi|).
Therefore vT x ◦x ∼subExp(ν, b) with ν = 16σ2
x∥v∥2, b =
16σ2
x∥v∥∞).
Also, we have a lemma about maximum of sum of variables with sub-exponential tails.
Lemma S2.7. Consider (uj)J
j=1 where uj ∈Rmj such that 1T uj ∼subExp(νj, b) with
E[uj] = 0 for 1 ≤j ≤J.
We let m := maxj mj.
Also, assume ∃ν∗> 0 such that
νj ≤ν∗
√m for all j and ∃c > 0 such that b ≤cν∗. Then we have,
E[ max
1≤j≤J 1T uj] ≤cν∗(log J + m/(2c2)).
In particular, when c = 1, E[ max
1≤j≤J 1T uj] ≤ν∗(log J + m/2).
7


## Page 50


Proof. For |t| ≤1/b we have,
E[exp(t1T uj)] ≤exp(t2ν2
j /2) ≤exp(mt2ν2
∗/2)
(S6)
Then,
E[ max
1≤j≤J 1T uj] = 1
t E

log emax1≤j≤J t(1T uj)
≤1
t log E

emax1≤j≤J t(1T uj)
= 1
t log E

max
1≤j≤J et(1T uj)

.
where the second inequality comes from Jensen’s. Using a union bound,
1
t log E

max
1≤j≤J et(1T uj)

≤1
t log


J
X
j=1
E

et(1T uj)


≤1
t log

Jemt2ν2
∗/2
.
(S7)
where the last inequality uses (S6). Since 1/(cν∗) ≤1/b by assumption, the inequality (S7)
holds for t = 1/(cν∗). Plugging t = 1/(cν∗) into (S7), we obtain,
E[ max
1≤j≤J 1T uj] ≤cν∗(log J + m/(2c2))
as claimed.
Finally, in Lemma S2.8 and S2.9, we provide expectation and probability tail bounds
of a dual ℓ1/ℓ2 norm of a sub-Gaussian vector.
Lemma S2.8. Let G = ((g1, . . . , gJ), (wj)J
1 ). Consider a random vector v ∈Rp such that
for each j and any ﬁxed u ∈R|gj|, uT vgj ∼subG(σ2∥u∥2
2) with E[vgj] = 0 and uT (vgj ◦vgj) ∼
subExp(ν∥u∥2, ν∥u∥∞). Then,
E[∥v∥¯G,2,∞] ≤c
p
log J + m
for c = (min1≤j≤J wj)−1p
max(ν, 8σ2), where we deﬁne ¯G = ((g1, . . . , gJ), (w−1
j )J
1 ) and
m := maxj |gj|, the largest group size.
8


## Page 51


Proof. First we let mj = |gj|. By Holder’s inequality, we have,
E[ max
1≤j≤J∥w−1
j vgj∥2] ≤E[ max
1≤j≤J∥w−1
j vgj∥2
2]1/2 = E[ max
1≤j≤J w−2
j (v2
gj,1 + . . . v2
gj,mj)]1/2
Then,
E[ max
1≤j≤J w−2
j (v2
gj,1 + . . . v2
gj,mj)] ≤( max
1≤j≤J w−2
j )E[ max
1≤j≤J(v2
gj,1 + . . . v2
gj,mj)]
= ( max
1≤j≤J w−2
j )E[ max
1≤j≤J
mj
X
i=1
(ugj,i + E[v2
gj,i]))]
≤( max
1≤j≤J w−2
j )

E[ max
1≤j≤J 1T ugj] + 4mσ2

where ugj
d:= vgj ◦vgj −E[vgj ◦vgj] and the last inequality uses Lemma S2.5 and mj ≤m,
for all j. By assumption, we have, 1T ugj ∼subExp(ν√mj, ν) and E[ugj] = 0. Then, by
Lemma S2.7,
LHS ≤( max
1≤j≤J w−2
j )[ν(log J + m/2) + 4mσ2]
≤( max
1≤j≤J w−2
j ) max(ν, 8σ2)(log J + m).
Since max1≤j≤J w−2
j
= 1/(min1≤j≤J wj)2, deﬁning c = (min1≤j≤J wj)−1p
max(ν, 8σ2), we
obtain
∥v∥¯G,2,∞≤c
p
log J + m
as desired.
Lemma S2.9. Let G = ((g1, . . . , gJ), (wj)J
1 ).
Consider a random vector v ∈Rp such
that for each j and for any ﬁxed u ∈R|gj|, uT vgj ∼subG(σ2∥u∥2
2) with E[vgj] = 0 and
uT (vgj ◦vgj) ∼subExp(ν∥u∥2, ν∥u∥∞). Then,
P

∥v∥¯G,2,∞≥δ

≤J exp

−1
2 min(C2
δ /ν2, Cδ/ν)

9


## Page 52


where we deﬁne Cδ := (minj w2
j)δ2/m−4σ2, ¯G = ((g1, . . . , gJ), (w−1
j )J
1 ), and m := maxj |gj|,
the largest group size.
Proof. By the union bound, we have
P

max
1≤j≤J∥w−1
j vgj∥2 ≥δ

≤
J
X
j=1
P

∥w−1
j vgj∥2
2 ≥δ2
.
Deﬁning ugj
d:= vgj ◦vgj −E[vgj ◦vgj] and mj := |gj|.
P

max
1≤j≤J∥w−1
j vgj∥2 ≥δ

≤
J
X
j=1
P
 mj
X
k=1
v2
gj,k ≥w2
jδ2
!
≤
J
X
j=1
P

1T ugj ≥(min
j
w2
j)δ2 −4mjσ2

where the last inequality uses Lemma S2.5. By assumption, we have 1T ugj ∼subExp(ν√mj, ν)
and E[ugj] = 0. We use Bernstein type inequality to bound the probability. More concretely
for any s > 0 such that |s| ≤1/ν, we have,
P

1T ugj ≥(min
j
w2
j)δ2 −4mjσ2

≤P
 s1T ugj ≥smCδ

≤exp(−smCδ)E

exp
 s1T ugj

≤exp(−smCδ + s2mν2/2).
In the ﬁrst and third inequality, the bound mj ≤m was also used. Optimizing over s > 0,
we take s = min{Cδ/ν2, 1/ν}. Hence, we have,
P

max
1≤j≤J∥w−1
j vgj∥2 ≥δ

≤J exp

−m
2 min(C2
δ /ν2, Cδ/ν)

10


## Page 53


S2.3
Proof for Proposition 3.1
The proof of this result follows similar lines to the proof of Theorem 1 in Loh and Wainwright
(2013), which established the result with a diﬀerent tolerance function and an additive
penalty. Since θ∗is feasible, by the ﬁrst order optimality condition, we have the following
inequality
(▽Ln(ˆθ) + ▽Pλ(ˆθ))T (θ∗−ˆθ) ≥0.
Letting ˆ∆:= ˆθ −θ∗, since ˆθ ∈Θ0 by the setup of the problem, we can apply RSC condition
to obtain
α∥ˆ∆∥2
2 −τ(∥ˆ∆∥G,2,1) ≤(−▽Pλ(ˆθ) −▽Ln(θ∗))T ˆ∆.
(S8)
On the other hand, convexity of Pλ(θ) implies
Pλ(θ∗) −Pλ(ˆθ) ≥−▽Pλ(ˆθ)T ˆ∆.
(S9)
Combining (S8) with (S9), we obtain
α∥ˆ∆∥2
2 −τ(∥ˆ∆∥G,2,1) ≤(−▽Pλ(ˆθ) −▽Ln(θ∗))T ˆ∆
≤Pλ(θ∗) −Pλ(ˆθ) + ∥▽Ln(θ∗)∥¯G,2,∞∥ˆ∆∥G,2,1.
by Lemma S2.4. Since τ(∥ˆ∆∥G,2,1) = τ1
log J + m
n
∥ˆ∆∥2
G,2,1 + τ2
r
log J + m
n
∥ˆ∆∥G,2,1,
α∥ˆ∆∥2
2 ≤Pλ(θ∗)−Pλ(ˆθ)+∥ˆ∆∥G,2,1
 
τ1
log J + m
n
∥ˆ∆∥G,2,1 + τ2
r
log J + m
n
+ ∥▽Ln(θ∗)∥¯G,2,∞
!
,
By the choice of λ,
τ1
log J + m
n
∥ˆ∆∥G,2,1 + τ2
r
log J + m
n
+ ∥▽Ln(θ∗)∥¯G,2,∞≤λ
2 .
11


## Page 54


Then by using the triangle inequality
α∥ˆ∆∥2
2 ≤Pλ(θ∗) −Pλ(ˆθ) + λ
2 ∥ˆ∆∥G,2,1
= λ
X
j∈S
wj∥θ∗
gj∥2 −λ
X
j∈S
wj∥ˆθgj∥2 −λ
X
j∈Sc
wj∥ˆθgj∥2 + λ
2
J
X
j=1
wj∥ˆ∆gj∥2
≤λ
X
j∈S
wj∥ˆ∆gj∥2 −λ
X
j∈Sc
wj∥ˆθgj∥2 + λ
2
J
X
j=1
wj∥ˆ∆gj∥2
where S := {j ∈(1, . . . , J); θ∗
gj ̸= 0} where the last inequality comes from the triangle
inequality. Since for j ∈Sc, ˆθgj = ˆθgj −θ∗
gj,
α∥ˆ∆∥2
2 ≤λ
X
j∈S
wj∥ˆ∆gj∥2 −λ
X
j∈Sc
wj∥ˆ∆gj∥2 + λ
2
J
X
j=1
wj∥ˆ∆gj∥2
= 3λ
2
X
j∈S
wj∥ˆ∆gj∥2 −λ
2
X
j∈Sc
wj∥ˆ∆gj∥2.
In particular, we have
X
j∈Sc
wj∥ˆ∆gj∥2 ≤3
X
j∈S
wj∥ˆ∆gj∥2
(S10)
and
α∥ˆ∆∥2
2 ≤3λ
2
X
j∈S
wj∥ˆ∆gj∥2.
(S11)
Then,
α∥ˆ∆∥2
2 ≤(max
j∈S wj)3λ
2 (
X
j∈S
∥ˆ∆gj∥2
2)1/2(
X
j∈S
1)1/2 ≤(max
j∈S wj)3λ
2
p
|S|∥ˆ∆∥2.
The ℓ1/ℓ2 upper bound follows from the ℓ2-bound and
∥ˆ∆∥G,2,1 =
X
j∈S
wj∥ˆ∆gj∥2 +
X
j∈Sc
wj∥ˆ∆gj∥2 ≤4(max
j∈S wj)
X
j∈S
∥ˆ∆gj∥2 ≤4(max
j∈S wj)
p
|S|∥ˆ∆∥2
.
12


## Page 55


S2.4
Proof of Lemma 3.1
Recalling Ln(θ) = 1
n
Pn
i=1
 −zif(θT xi) −A(f(θT xi))

, we have
▽Ln(θ∗) = 1
n
n
X
i=1

−zi + µ(f(θ∗T xi))

1
1 + eθ∗T xi xi,
where we deﬁne A(η) = log(1+eη), µ(η) = A′(η) = eη/(1+eη) and f(θT x) = log(nℓ/πnu)+
θT x−log(1+eθT x). For 1 ≤i ≤n and 1 ≤j ≤p, deﬁne Vij :=
 −zi + µ(f(θ∗T xi))

1
1 + eθ∗T xi xij.
We note ▽Ln(θ∗)j = 1
n
Pn
i=1 Vij.
Considering the event, with C := 36σ2
x,
E =
(
max
1≤j≤p
1
n
n
X
i=1
x2
ij ≤C
)
.
we have,
P

∥▽Ln(θ∗)∥¯G,2,∞≥δ

≤P(Ec) + P

∥▽Ln(θ∗)∥¯G,2,∞≥δ|E

P(E).
First we show that P(Ec) is small. Since each xij is a sub-Gaussian variable with sub-
Gaussian parameter σx, deﬁning zij = x2
ij −E[x2
ij],
P(Ec) ≤pP
 
1
n
n
X
i=1
x2
ij ≥36σ2
x
!
≤pP
 
1
n
n
X
i=1
zij ≥32σ2
x
!
where we use the fact that E[x2
ij] ≤4σ2
x. We note that (zij)n
i=1 are i.i.d. samples from
mean-zero distribution with sub-Exponential tail with parameter ν = b = 16σ2
x by applying
Lemma S2.6 with s = 1. By Bernstein-type tail bound of the sub-exponential random
variable,
P(Ec) ≤pP
 
1
n
n
X
i=1
zij ≥32σ2
x
!
≤exp(−n
2 (2 −2 log p
n
)) ≤exp(−n/2),
(S12)
by the sample size condition n ≳log J +m, assuming suﬃciently large n. Now we show that
1
n
Pn
i=1 Vij is a sub-Gaussian variable on E. In particular, we show that E[exp(t 1
n
Pn
i=1 Vij)|E] ≤
exp(t2v2/2) for some v > 0.
13


## Page 56


Deﬁning ti :=
t
n(1 + eθ∗T xi)
, by deﬁnition of Vij, we have
E

exp( t
nVij)|xi

= E

exp (−tizixij) · exp
 tiµ(f(xT
i θ∗))xij

|xi

= E [exp (−tizixij) |xi] · exp
 tiµ(f(xT
i θ∗))xij

.
(S13)
By the property of exponential family, we obtain
E [exp (−tizixij) |xi] =
Z
exp (−tizxij) · exp(zf(xT
i θ∗) −A(f(xT
i θ∗))dz
= exp

A(f(xT
i θ∗) −tixij) −A(f(xT
i θ∗))
	
.
(S14)
Therefore combining (S13) and (S14), we obtain
E

exp( t
nVij)|xi

= exp

A(f(xT
i θ∗) −tixij) −A(f(xT
i θ∗)) + tiµ(f(xT
i θ∗))xij
	
≤exp
 1
8n2 (txij)2

where the second inequality comes from the second order Taylor expansion, µ(·) = A′(·),
supu A′′(u) ≤1/4, and ti ≤t/n. Therefore
n
Y
i=1
E

exp( t
nVij)|xi

≤exp
 
t2
8n2
n
X
i=1
x2
ij
!
,
and conditioned on E, we have the bound
exp
 
t2
8n2
n
X
i=1
x2
ij
!
≤exp
t2C
8n

.
Therefore, 1
n
Pn
i=1 Vij ∼subG(C/4n), i.e. ▽Ln(θ∗)j ∼subG(C/4n) for all j.
Now we discuss the distribution of uT ▽Ln(θ∗)gj and uT ▽Ln(θ∗)gj ◦▽Ln(θ∗)gj on E, for
any u ∈R|gj|, to apply Lemma S2.9. By Assumption 1, (▽Ln(θ∗)j)j∈gj are independent.
With independence, it is easy to see for any j and any ﬁxed u ∈R|gj|, uT ▽Ln(θ∗)gj ∼
subG(∥u∥2
2(C/4n)) and E[▽Ln(θ∗)] = 0. Then Lemma S2.6 gives
uT (▽Ln(θ∗)gj ◦▽Ln(θ∗)gj) ∼subExp(∥u∥2(4C/n), ∥u∥∞(4C/n))
14


## Page 57


for any j and ﬁxed u ∈R|gj|. Therefore the condition of Lemma S2.9 is satisﬁed with
σ2 = C/4n and ν = 16σ2 = 4C/n.
We let δ2 = 16C(log J + m)/(minj w2
jn) and note that
Cδ =
(minj w2
j)δ2
m
−C
n = 16C(log J + m)
mn
−C
n = 4C
n
16 log J
4m
+ 15
4

By Lemma S2.9,
P

∥▽Ln(θ∗)∥¯G,2,∞≥δ|E

≤exp

−m
2 min

C2
δ
(4C/n)2 ,
Cδ
4C/n

+ log J

,
and because log J/m ≥0, Cδ ≥4C/n, and min

C2
δ
(4C/n)2 ,
Cδ
4C/n

=
Cδ
4C/n if Cδ ≥4C/n, we
have,
P

∥▽Ln(θ∗)∥¯G,2,∞≥δ|E

≤exp

−m
2
4 log J
m
+ 15
4

+ log J

≤exp (−log J −m) .
(S15)
Putting (S12) and (S15) together, and noting δ = (24σx/ minj wj)
q
log J+m
n
, we obtain
P
 
∥▽Ln(θ∗)∥¯G,2,∞≥(24σx/ min
j
wj)
r
log J + m
n
!
≤exp(−0.5n) + exp(−log J −m) ≤ϵ
where the last inequality follows from the sample size condition n ≳(log J + m) ∨(1/ϵ)1/β.
S2.5
Proof of Theorem 3.2
S2.5.1
Proof Outline
Deﬁning f(θT x) = log(nl/πnu) + θT x −log(1 + eθT x), we recall that
Ln(θ) = 1
n
n
X
i=1

−zif(θT xi) + log(1 + ef(θT xi))

.
15


## Page 58


Taking a derivative with respect to θ of Ln(θ), we obtain
▽Ln(θ) = 1
n
n
X
i=1
 −zi + µ(f(θT xi))

f′(θT xi)xi
and
(▽Ln(θ) −▽Ln(θ∗))T ∆
=
 
1
n
n
X
i=1
 µ(f(θT xi)) −zi

f′(θT xi) −

µ(f(θ∗T xi)) −zi

f′(θ∗T xi)
!
xT
i ∆
(S16)
where ∆is deﬁned as ∆:= θ −θ∗, and A(·), µ(·) deﬁned as A(η) := log(1 + eη), µ(η) :=
A′(η) = eη/(1 + eη). Also we let ei := µ(f(θ∗T xi)) −zi.
To prove that (S16) is positive with high probability, we decompose (S16) into two terms,
whose ﬁrst term I has a positive expectation and the second term II has an expectation
zero. To do so, we add and subtract 1
n
Pn
i=1 eif′(θT xi)xi to (S16) to obtain
(S16) = 1
n
n
X
i=1

µ(f(θT xi)) −µ(f(θ∗T xi)

)f′(θT xi)xT
i ∆+ ei(f′(θT xi) −f′(θ∗T xi))xT
i ∆.
Applying a Taylor expansion around f(θ∗T xi), we obtain
(▽Ln(θ) −▽Ln(θ∗))T ∆
= 1
n
n
X
i=1
A′′(f(θ∗T xi) + vi(f(θT xi) −f(θ∗T xi)))(f(θT xi) −f(θ∗T xi))f′(θT xi)xT
i ∆
|
{z
}
I
(S17)
+ 1
n
n
X
i=1
ei(f′(θT xi) −f′(θ∗T xi))xT
i ∆
|
{z
}
II
for vi ∈[0, 1]
(S18)
where A′′(η) = eη/(1 + eη)2.
We will show that the expectation of I is positive.
We
immediately see E[ei(f′(θT xi) −f′(θ∗T xi))xT
i ∆] = 0 because E[ei|xi] = 0.
16


## Page 59


We aim to show each inequality
I ≥κ0∥∆∥2
2 −κ1∥∆∥G,2,1∥∆∥2
r
log J + m
n
(S19)
|II| ≤κ2∥∆∥G,2,1
r
log J + m
n
(S20)
holds for all ∆∈{∆; ∥∆∥2 ≤r} with probability at least 1 −ϵ/2 for some κ0, κ1, κ2 > 0.
Then
I + II ≥κ0∥∆∥2
2 −κ1∥∆∥G,2,1∥∆∥2
r
log J + m
n
−κ2∥∆∥G,2,1
r
log J + m
n
holds for all ∆∈{∆; ∥∆∥2 ≤r} with probability at least 1 −ϵ. Finally, by the inequality
a2 + b2 ≥2ab, we obtain,
I + II ≥(κ0/2)∥∆∥2
2 −(2κ2
1/κ0)
log J + m
n

∥∆∥2
G,2,1 −κ2
r
log J + m
n
∥∆∥G,2,1
for all ∆∈{∆; ∥∆∥2 ≤r} with probability at least 1 −ϵ.
S2.5.2
Obtaining a lower bound of term I
We use a similar argument in Negahban et al. (2012) to obtain a lower bound of the ﬁrst
term. The main diﬀerence is that we get the dependence on θ for a curvature term, which
is not the case for a canonical link f(θT x) = θT x. Since f′(u) =
1
1 + eu , the ﬁrst term I
becomes
I = 1
n
n
X
i=1
A′′(f(θ∗T xi) + vi(f(θT xi) −f(θ∗T xi)))
(xT ∆)2
(1 + exT
i θ∗+v′
ixT
i ∆)(1 + exT
i θ)
.
for some v′
i ∈[0, 1] by Taylor expansion. We note
I ≥1
n
n
X
i=1
A′′(f(θ∗T xi) + vi(f(θT xi) −f(θ∗T xi)))
(1 + exT
i θ∗+v′
ixT
i ∆)(1 + exT
i θ)
(xT
i ∆)21{|∆T xi| ≤τ∥∆∥2}
17


## Page 60


for any τ ≥0, as A′′(u) =
eu
(1+eu)2 ≥0, ∀u. A suitable τ will be chosen shortly. Since on
the event
|∆T xi| ≤τ∥∆∥2,
(S21)
we have θT xi ≤|θ∗T xi| + |∆T xi| ≤Kr
1 + τr and
|f(θ∗T xi) + vi(f(θ∗T xi) −f(θT xi))| ≤|f(θ∗T xi)| + |f(θ∗T xi) −f(θT xi)|
≤
log nl
πnu
 + |θ∗T xi| + |∆T xi|,
by Assumption 3 and the fact that xT θ −log(1 + exT θ) is 1-Lipschitz in xT θ, I can be
further lower-bounded by
I ≥L0(τ)
n
n
X
i=1
(xT
i ∆)21{|∆T xi| ≤τ∥∆∥2},
where L0(τ) is deﬁned as L0(τ) :=
inf
|u|≤K2+Kr
1+τr
A′′(u)
(1 + eKr
1+τr)2 . Finally, we truncate each
term (xT
i ∆)21{|∆T xi| ≤τ∥∆∥2} so that each term is Lipschitz in (xT
i ∆). For a truncation
level τ > 0, we deﬁne the following function:
ϕτ(u) =













u2
if |u| ≤τ
2
(τ −u)2
if τ
2 ≤|u| ≤τ
0
otherwise
and note that I ≥1
n
Pn
i=1 L0(τ)ϕτ∥∆∥2(∆T xi), since if the event (S21) holds, (∆T xi)2 ≥
ϕτ∥∆∥2(∆T xi), and both left and right-hand sides are 0 if the event does not hold.
Deﬁning Iℓas
Iℓ:= L0(τ)
n
n
X
i=1
ϕτ∥∆∥2(∆T xi),
(S22)
we note that it is suﬃcient to show the inequality
Iℓ≥κ0∥∆∥2
2 −κ1∥∆∥G,2,1∥∆∥2
r
log J + m
n
(S23)
18


## Page 61


holds with high probability for all ∆∈{∆; ∥∆∥2 ≤r} to prove (S19). To do so, ﬁrst we
will show the inequality (S23) is true for ∆∈S(δ, t), where we deﬁne
S(δ, t) := {∆∈Rp; ∥∆∥2 = δ, ∥∆∥G,2,1/∥∆∥2 ≤t}.
(S24)
If ∆= 0, the inequality (S23) is trivially true. Otherwise, we show that
L0(τ)
nδ2
n
X
i=1
ϕτ∥∆∥2(∆T xi) ≥κ0 −κ1t
r
log J + m
n
,
(S25)
is true for all ∆∈S(δ, t) with high probability. Then we will use a homogeneity property
of ϕ and peeling argument to obtain a uniform result over (δ, t).
S2.5.3
Bounding Expectation of Term I
We note that Iℓis lower bounded by,
Iℓ= E[Iℓ] + (Iℓ−E[Iℓ]) ≥E[Iℓ] −
sup
∆∈S(δ,t)
|Iℓ−E[Iℓ]|.
In this sub-section, we obtain the lower bound of E[Iℓ], which is strictly positive with a
suitably chosen τ. In the next sub-section, we will control the deviation term sup∆∈S(δ,t) |Iℓ−
E[Iℓ]|. First we have E[Iℓ] = L0(τ)E
h
ϕτ∥∆∥2(∆T x)
i
where x d= xi, and
E
h
ϕτ∥∆∥2(∆T x)
i
= E[(∆T x)2] −E[(∆T x)2 −ϕτ∥∆∥2(∆T x)].
We lower and upper bound each two terms on the right-hand side by
E[(∆T x)2] ≥K0∥∆∥2
2
and
E[(∆T x)2 −ϕτ∥∆∥2(∆T x)] ≤E

(∆T x)21

|∆T x| ≥τ∥∆∥2
2

19


## Page 62


Applying the Cauchy-Schwarz inequality, we obtain
E

(∆T x)21

|∆T x| ≥τ∥∆∥2
2

≤
q
E(∆T x)4
s
P

|∆T x| ≥τ∥∆∥2
2

≤4
√
2σ2
x exp

−τ 2
16σ2x

∥∆∥2
2
by using expectation and tail-bound of sub-Gaussians, since ∆T x ∼subG(∥∆∥2
2σ2
x). As
4
√
2σ2
x

exp

−τ 2
16σ2x

≤K0
4 for τ 2 ≥16σ2
x log 16
√
2σ2
x
K0
, we take τ = K3 := 4σx

log 16
√
2σ2
x
K0
1/2
to have
E[Iℓ] = L0(K3)E
h
ϕK3∥∆∥2(∆T x)
i
≥L0(K3)∥∆∥2
2

K0 −4
√
2σ2
x exp

−τ 2
16σ2x

≥∥∆∥2
2
3L0(K3)K0
4
.
(S26)
For simplicity, we write L0 := L0(K3) for future references.
S2.5.4
Controlling the diﬀerence of Term I from its expectation
We now bound the term
sup
∆∈S(δ,t)
|Iℓ−E[Iℓ]| using the concentration property of an empirical
process. We have
sup
∆∈S(δ,t)
|Iℓ−E[Iℓ]| = δ2L0U1(t), where we deﬁne U1(t) as
U1(t) :=
sup
∆∈S(δ,t)

1
n∥∆∥2
2
n
X
i=1
ϕK3∥∆∥2(∆T xi) −E
h
ϕK3∥∆∥2(∆T x)
i ,
since ∥∆∥2 = δ for all ∆∈S(δ, t). Since we have ∥ϕK3∥∆∥2∥∞≤K2
3∥∆∥2
2
4
by deﬁnition of
ϕτ(·), we apply bounded diﬀerence inequality with ci = K2
3/2n (Theorem S2.3) to obtain
P(U1(t) ≥EU1(t) + u1) ≤2 exp

−8nu2
1
K4
3

.
Setting u1 = K0/4,
P(U1(t) ≥E[U1(t)] + K0
4 ) ≤2 exp(−c1n)
(S27)
20


## Page 63


where c1 = K2
0/2K4
3 is a constant depending on K0 and K3. Now we calculate EU1(t). By
symmetrization and contraction inequalities (Theorems S2.1, S2.2), we have
E[U1(t)] ≤2E
"
sup
∆∈S(δ,t)

1
n∥∆∥2
2
n
X
i=1
ϵiϕK3∥∆∥2(∆T xi)

#
≤8K3δ
δ2
E
"
sup
∆∈S(δ,t)

1
n
n
X
i=1
ϵi∆T xi

#
≤8K3δ−1
 
sup
∆∈S(δ,t)
∥∆∥G,2,1
!
E
"
∥1
n
n
X
i=1
ϵixi∥¯G,2,∞
#
≤8K3K4t
r
log J + m
n
(S28)
where (ϵi)n
i=1 are i.i.d Rademacher variables and K4 := 20σx(minj wj)−1. Note that ϕK3∥∆∥2
is a Lipschitz function with the Lipschitz constant = 2K3∥∆∥2 = 2K3δ for ∆∈S(δ, t)
which allows us to apply the Ledoux-Talagrand contraction theorem.
The second last
inequality is from Lemma S2.4 and the last inequality follows from E
h
∥1
n
Pn
i=1 ϵixi∥¯G,2,∞
i
≤
K4
q
log J+m
n
, which will be proven shortly in Lemma S2.10.
Therefore, combining (S26), (S27) and (S28), we have
inf
∆∈S(δ,t)
L0
n∥∆∥2
2
n
X
i=1
ϕK3∥∆∥2(∆T xi) ≥κ0 −κ′
1t
r
log J + m
n
(S29)
with probability at least 1−exp(−c1n) where κ0 = K0L0/2 and κ′
1 = 8L0K3K4. It remains
to prove Lemma S2.10.
Lemma S2.10.
E
"
∥1
n
n
X
i=1
ϵixi∥¯G,2,∞
#
≤c
r
log J + m
n
(S30)
for n ≥log p, where c := 20σx(minj wj)−1 is a constant depending on σx, (wj)J
1 .
Proof. Conditioned on xn
1, 1
n
Pn
i=1 ϵixij is a sub-Gaussian with a parameter
1
n2
P
i x2
ij, since
ϵi ∼subG(1). Then 1
n
Pn
i=1 ϵixij ∼subG(C(x)/n), where we deﬁne C(x) = max1≤j≤p 1
n
P
i x2
ij
21


## Page 64


conditioned on xn
1. Deﬁning u := [u1, . . . , up]T ∈Rp as uj =
1
n
Pn
i=1 ϵixij, we have in-
dependence of (uj)j∈gj by Assumption 1.
Following similar arguments as in the proof
of Lemma 3.1, we obtain for any j and v ∈R|gj|, vT ugj ∼subG((C(x)/n)∥v∥2
2) and
vT (ugj ◦ugj) ∼subExp(ν∥v∥2, ν∥v∥∞) with ν = 16C(x)/n. Then Lemma S2.8 gives,
E
"
∥1
n
n
X
i=1
ϵiui∥¯G,2,∞|xn
1
#
≤4(min
j
wj)−1p
C(x)
r
log J + m
n
.
Therefore,
E
"
∥1
n
n
X
i=1
ϵixi∥¯G,2,∞
#
≤4(min
j
wj)−1
r
log J + m
n
E[
p
C(x)]
Now we upper-bound E[
p
C(x)]. By Holder’s inequality,
E


v
u
u
t max
1≤j≤p
1
n
n
X
i=1
x2
ij

≤E
"
max
1≤j≤p
1
n
n
X
i=1
x2
ij
#1/2
Now we deﬁne zij := x2
ij −E[x2
ij] for each 1 ≤i ≤n and 1 ≤j ≤p and zj = [z1j, . . . , znj]T .
Using Lemma S2.5, we have,
E
"
max
1≤j≤p
1
n
n
X
i=1
x2
ij
#
≤E
"
max
1≤j≤p
1
n
n
X
i=1
zij
#
+ 4σ2
x.
Since 1T zj ∼subExp(16σ2
x
√n, 16σ2
x) by Lemma S2.6, we apply Lemma S2.7 with ν∗=
16σ2
x
√n, c = 1/√n (taking mj = 1, ∀j) to obtain
n−1E[ max
1≤j≤p 1T zj] ≤n−116σ2
x(log p + n/2) = 16σ2
x
log p
n
+ 8σ2
x,
Hence,
E[
p
C(x)] ≤4σx
p
log p/n + 1/2 ≤5σx
by the condition of log p/n ≤1, and thus,
E
"
∥1
n
n
X
i=1
ϵixi∥¯G,2,∞
#
≤20σx(min
j
wj)−1
r
log J + m
n
22


## Page 65


S2.5.5
Extending the inequality (S29) for all ∆∈B2(r)
In this section, we show
L0
n∥∆∥2
2
n
X
i=1
ϕK3∥∆∥2(∆T xi) ≥κ0 −κ1
∥∆∥G,2,1
∥∆∥2
 r
log J + m
n
(S31)
holds for all ∥∆∥2 = δ with probability at least 1 −ϵ/2 where κ1 = 2κ′
1. Note if (S31)
holds, for any ∆′ such that ∥∆′∥2 = δ′ ̸= δ, we can apply (S31) to ∆= ∆′(δ/δ′) to obtain
L0
n∥∆′∥2
2
n
X
i=1
ϕK3∥∆′∥2(∆′T xi) ≥κ0 −κ1
∥∆′∥G,2,1
∥∆′∥2
 r
log J + m
n
by using homogeneity property of ϕ,i.e. ϕτ(x) = c−2ϕcτ(cx) for any c > 0. Thus proving
that (S31) holds for all ∥∆∥2 = δ with probability at least 1 −ϵ/2 is enough to prove
that the same inequality holds for all ∥∆∥2 ≤r with the same high probability. We let
S2(δ) := {∆∈Rp; ∥∆∥2 = δ} and Kw > 0 be a constant such that minj wj ≥Kw, where
the existence of Kw is guaranteed by Assumption 4.
P (∃∆∈S2(δ) such that inequality (S31) fails )
≤
NL
X
l=1
P

∃∆∈S2(δ); Kw2l−1 ≤∥∆∥G,2,1
∥∆∥2
≤Kw2l s.t inequality (S31) fails

(S32)
where 2NL ≤(maxj wj/Kw)
√
J, i.e. NL :=
l
log2

maxj wj
√
J/Kw
m
, by the inequality
Kw∥∆∥2 ≤(minj wj)∥∆∥2 ≤∥∆∥G,2,1 ≤(maxj wj)
√
J∥∆∥2.
NL
X
l=1
P

∃∆∈S2(δ); Kw2l−1 ≤∥∆∥G,2,1
∥∆∥2
≤Kw2l such that inequality (S31) fails

≤
NL
X
l=1
P


inf
∆∈S2(δ);
∥∆∥G,2,1
∥∆∥2
≤(Kw2l)
L0
n∥∆∥2
2
n
X
i=1
ϕK3∥∆∥2(∆T xi) < κ0 −κ1(Kw2l−1)
r
log J + m
n


=
NL
X
l=1
P
 
inf
∆∈S(δ,(Kw2l))
L0
n∥∆∥2
2
n
X
i=1
ϕK3∥∆∥2(∆T xi) < κ0 −κ′
1(Kw2l)
r
log J + m
n
!
≤exp(−c1n + log NL)
23


## Page 66


by κ1 = 2κ′
1 and the inequality (S29). Finally,
exp(−c1n + log NL) ≤exp

−c1n + log log2(J3/2/Kw)

≲exp (−c1n + log log J) ≤ϵ/2
by the sample size condition n ≳(log J + m) ∨(1/ϵ)1/β and maxj wj/J ≤1.
S2.5.6
Controlling the diﬀerence of Term II from its expectation
For the second term, we recall the deﬁnition :
II = 1
n
n
X
i=1
ei(f′(θT xi) −f′(θ∗T xi))xT
i ∆,
and note that E[II] = 0 by E[ei|xi] = 0. Similar to U1(t), we deﬁne a following quantity,
U2(t) :=
sup
(1/2)t≤∥∆∥G,2,1≤t

1
n∥∆∥G,2,1
n
X
i=1
ei(f′(θT xi) −f′(θ∗T xi))xT
i ∆.

, and bound E(U2(t)) using symmetrization and contraction theorem. First we deﬁne
gi(∆T xi) := ei

f′(θ∗T xi + ∆T xi) −f′(θ∗T xi)

∆T xi.
and prove that gi/Lg is a contraction map where Lg := 3 + (Kr
1/4).
Lemma S2.11. gi(s)/Lg is a contraction map with gi(0) = 0.
Proof. We consider the ﬁrst derivative of gi. For ease of notation, we let u∗
i := θ∗T xi. We
note f′(u) = 1/(1 + eu),f′(u) = −eu/(1 + eu)2. Thus supu |f′(u)| ≤1, supu |f′′(u)| ≤1/4.
Also, elementary calculation shows that supu |uf′(u)|, supu |uf′′(u)| ≤1/2. Since,
gi(u) = ei(f′(u∗
i + u) −f′(u∗
i ))u
we have,
|g′
i(u)| = |ei(f′′(u∗
i + u)u + f′(u∗
i + u) −f′(u∗
i ))|
≤|f′′(u∗
i + u)(u∗
i + u) −f′′(u∗
i + u)u∗
i + f′(u∗
i + u) −f′(u∗
i ))|
≤3 + (1/4)|u∗
i |
24


## Page 67


where |ei| ≤1 was used in the ﬁrst inequality. By Assumption 2, u∗
i := |θ∗T xi| ≤Kr
1, thus
we can take Lg := 3 + (1/4)Kr
1.
Back to E(U2(t)), by symmetrization and contraction theorem (Theorems S2.1,S2.2),
E(U2(t)) ≤4LgE
"
sup
(1/2)t≤∥∆∥G,2,1≤t

1
n∥∆∥G,2,1
n
X
i=1
ϵi∆T xi

#
≤4LgE
"
sup
(1/2)t≤∥∆∥G,2,1≤t
1
(1/2)t∥∆∥G,2,1∥1
n
n
X
i=1
ϵixi∥¯G,2,∞
#
≤8K4Lg
r
log J + m
n
.
(S33)
where the second inequality uses the fact that (1/2)t ≤∥∆∥G,2,1 ≤t and Lemma S2.4, and
the last inequality comes from Lemma S2.10.
Now, we apply bounded diﬀerence inequality to show that U2(t) is close to E(U2(t))
with probability at least 1 −exp(−c′n). We have,
sup
i,θ
1
n∥∆∥G,2,1
|gi(∆T xi)| = sup
i,θ
1
n∥∆∥G,2,1
ei

f′(θ∗T xi + ∆T xi) −f′(θ∗T xi)

∆T xi

≤sup
i,θ
2
n∥∆∥G,2,1
|∆T xi| ≤2
n max
i,j w−1
j ∥(xi)gj∥2
by Lemma S2.4. We note for any w ∈Rp such that wgc
j = 0 and ∥w∥2 = 1, u ∈Rp, deﬁned
as u := θ∗+rw, satisﬁes ∥u−θ∗∥2 ≤r and supp(u−θ∗) ⊆gj. By Assumption 2, |xT
i u| ≤Kr
1
a.s. for all i. Then |xT
i w| = |xT
i (u −θ∗)|/r ≤2Kr
1/r a.s., which implies ∥(xi)gj∥2 ≤2Kr
1/r
since ∥(xi)gj∥2 =
sup
v∈R|gj|;∥v∥2=1
|(xi)T
gjv| =
sup
w∈Rp;∥w∥2=1,wgc
j =0
|xT
i w|. As the bound holds for
any i, j, we have maxi,j ∥(xi)gj∥2 ≤2Kr
1/r.
Hence by applying Theorem S2.3 with ci = (8Kr
1/Kwr)n−1, we obtain
P(U2(t) ≥EU2(t) + u2) ≤exp(−2u2
2/
n
X
i=1
c2
i )
25


## Page 68


Taking u2 = K4Lg
r
log J + m
n
, we get
P
 
U2(t) ≥9K4Lg
r
log J + m
n
!
≤exp(−c2(log J + m))
where c2 := (KwrK4Lg)2/32(Kr
1)2. In other words, we have shown, for any t > 0,
P
 
1
n
n
X
i=1
ei(f′(θ∗T xi + ∆T xi) −f′(θ∗T xi))xT
i ∆
 ≤κ′
2∥∆∥G,2,1
r
log J + m
n
, ∀(1/2)t ≤∥∆∥G,2,1 ≤t
!
≥1 −exp(−c2(log J + m))
(S34)
where we deﬁne κ′
2 := 9K4Lg.
S2.5.7
Extending the inequality (S34) for all ∆∈B2(r)
In this section, we obtain a uniform result for term II. More concretely, we consider the
following inequality:

1
n
n
X
i=1
ei(f′(θ∗T xi + ∆T xi) −f′(θ∗T xi))xT
i ∆
 ≤κ2∥∆∥G,2,1
r
log J + m
n
(S35)
where κ2 := 10K4Lg. Equivalently, deﬁning
φ(∆; xn
1, zn
1 ) :=
1
n∥∆∥G,2,1
n
X
i=1
ei(f′(θ∗T xi + ∆T xi) −f′(θ∗T xi))xT
i ∆
for ∆̸= 0, we aim to establish the result,
P
 
|φ(∆; xn
1, zn
1 )| ≤κ2
r
log J + m
n
, ∀∆∈B2(r)
!
≥1 −ϵ/2.
We ﬁrst deﬁne
A(r1, r2) := {∆∈Rp; r1 < ∥∆∥G,2,1 ≤r2}
26


## Page 69


and decompose B2(r) into diﬀerent regions. We have,
P (∃∆∈B2(r) such that inequality (S35) fails )
≤P (∃∆∈A(0, Cn) such that inequality (S35) fails )
(S36)
+
NK
X
k=1
P (∃∆∈A(rk−1, rk) such that inequality (S35) fails )
(S37)
where we deﬁne
Cn := K4Lg
(minj wj)r
Kr
1
2 r
log J + m
n
rk := Cn2k.
Here Cn is chosen to ensure the probability (S36) to be small enough, which will be
shown shortly. We take NK such that rNK = Cn2NK ≥r maxj wj
√
J since ∥∆∥G,2,1 ≤
(maxj wj)
√
J∥∆∥2 ≤r(maxj wj)
√
J. Then we can let,
NK :=
&
log2
 
c max
j
wj
s
nJ
log J + m
!'
for c := (Kr
1)2/(rK2
wK4Lg)∨1. By the sample size assumption, maxj wj/n ≤1 and J ≳nβ,
thus
NK ≤log2
 
c max
j
wj
s
nJ
log J + m
!
≤2 log

c′n(3+β)/2
.
for some c′ > 1. Since P (∃∆∈A(rk−1, rk) such that inequality (S35) fails ) ≤exp(−c2(m+
log J)) for any k by (S34), we have for (S37),
(S37) ≤exp(−c2(m + log J) + log NK)
≤2 exp

−c2(m + log J) + log log c′n(3+β)/2
≤c3 exp(−c2(m + log J) + log log n)
27


## Page 70


for c3 = 2((3 + β)/2 + log c′) > 1, as log log c′n(3+β)/2 ≤log log n + log((3 + β)/2 + log c′).
Now we address (S36):
(S36) = P
 
∃∆∈A(0, Cn); |φ(∆; xn
1, zn
1 )| > κ2
r
log J + m
n
!
For s ∈(0, Cn], we deﬁne a function eφ : R+ × Rp →R , whose ﬁrst argument takes the size
(measured in ∥·∥G,2,1 norm ), second argument takes normalized direction (i.e. ∥d∥G,2,1 = 1)
such that
eφ(s, d; xn
1, zn
1 ) := 1
n
n
X
i=1
ei(f′(θ∗T xi + sxT
i d) −f′(θ∗T xi))xT
i d = φ(sd; xn
1, zn
1 )
In particular, for any ∆∈A(0, Cn), we have eφ(∥∆∥G,2,1, ∆/∥∆∥G,2,1; xn
1, zn
1 ) = φ(∆; xn
1, zn
1 ).
Now we calculate how much φ changes when the size of the input vector varies while
ﬁxing the direction. In other words, we calculate the rate of change of eφ with respect to its
ﬁrst argument. To ease the notation, we suppress the dependence of φ, eφ on (xn
1, zn
1 ).
| d
ds
eφ(s, d)| =

d
ds
 
1
n
n
X
i=1
eif′(θ∗T xi + sxT
i d) −f′(θ∗T xi))xT
i d
!
≤1
n
n
X
i=1
eif′′(θ∗T xi + sxT
i d)
 (xT
i d)2
≤1
4∥xi∥2¯G,2,∞∥d∥2
G,2,1 ≤

Kr
1
(minj wj)r
2
by |ei| ≤1 and ∥f′′∥∞≤(1/4).
Then for any normalized direction d ∈Rp such that
∥d∥G,2,1 = 1, we have,
|eφ(s, d) −eφ(u, d)| ≤

Kr
1
(minj wj)r
2
|s −u|
In particular, for any 0 < s ≤Cn,
|eφ(s, ∆/∥∆∥G,2,1)| ≤|eφ(Cn, ∆/∥∆∥G,2,1)| +

Kr
1
(minj wj)r
2
Cn
28


## Page 71


Therefore,
(S36) = P
 
∃∆∈A(0, Cn); |eφ(∥∆∥G,2,1, ∆/∥∆∥G,2,1)| > κ2
r
log J + m
n
!
≤P
 
∃∆∈A(0, Cn); |eφ(Cn, ∆/∥∆∥G,2,1)| > κ2
r
log J + m
n
−

Kr
1
(minj wj)r
2
Cn
!
= P
 
∃∆∈A(0, Cn); |eφ(Cn, ∆/∥∆∥G,2,1)| > 9K4Lg
r
log J + m
n
!
where the last line uses the fact

Kr
1
(minj wj)r
2
Cn = K4Lg
q
log J+m
n
. Since eφ(Cn, ∆/∥∆∥G,2,1) =
φ(Cn∆/∥∆∥G,2,1) and Cn∆/∥∆∥G,2,1 ∈{∆′ ∈Rp; ∥∆′∥G,2,1 = Cn}, we have,
(S36) ≤P
 
sup
∥∆∥G,2,1=Cn
|φ(∆)| > 9K4Lg
r
log J + m
n
!
≤P
 
sup
(1/2)Cn≤∥∆∥G,2,1≤Cn
|φ(∆)| > 9K4Lg
r
log J + m
n
!
≤exp(−c2(log J + m))
by (S34). Therefore,
(S36) + (S37) ≤exp(−c2(log J + m)) + c3 exp(−c2(m + log J) + log log n)
≤2c3 exp(−c2(m + log J) + log log n) ≤ϵ/2
by the sample size condition n ≳(log J + m) ∨(1/ϵ)1/β, noting log log n = o(log J).
29


## Page 72


S3
Supplementary simulation results in Section 4
In this section, we display additional classiﬁcation performance results. We recall the sim-
ulation setting: dimension of features p ∈(10, 5000), auto-correlation level among features
ρ ∈(0, 0.2, 0.4, 0.6, 0.8), separation distance d ∈(1.5, 2.5, 3.5), and the model speciﬁca-
tion scheme (logistic, misspeciﬁed). The sample size is nℓ= nu = 500 in all setting and
experiments are repeated 50 times.
S3.1
The logistic model scheme
S3.1.1
F1 scores under the logistic model scheme
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
d = 1.5
d = 2.5
d = 3.5
p = 10
p = 5000
0.0 0.2 0.4 0.6 0.8 0.0 0.2 0.4 0.6 0.8 0.0 0.2 0.4 0.6 0.8
0.65
0.70
0.75
0.80
0.85
0.90
0.65
0.70
0.75
0.80
0.85
0.90
rho
F1score
Algorithm
G (i) Reference
(ii) PUlasso
(iii) EN1
(iv) EN2
(v) biased−SVM
(vi) PNS
Figure S1: F1 scores of algorithms (i)-(vi) under correct (logistic) model speciﬁcation
30


## Page 73


S3.2
The misspeciﬁed model scheme
Heavy-tailed distribution tends to generate more separated samples, leading to better classi-
ﬁcation performance. The scaling of Σρ, which sets V ar(xT
i θ∗) the same across ρ, indirectly
changes the separation between the two classes. As a result, we observe improved classiﬁca-
tion performance with higher ρ in the misspeciﬁed setting. PUlasso algorithm continues to
out-perform other algorithms in most cases, but performance diﬀerence among algorithms
decreases under the model misspeciﬁcation scheme.
S3.2.1
Mis-classiﬁcation rates under the misspeciﬁed model
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
d = 1.5
d = 2.5
d = 3.5
p = 10
p = 5000
0.0 0.2 0.4 0.6 0.8 0.0 0.2 0.4 0.6 0.8 0.0 0.2 0.4 0.6 0.8
0.0
0.1
0.2
0.3
0.4
0.5
0.0
0.1
0.2
0.3
0.4
0.5
rho
misclassification rate
Algorithm
G (i) Reference
(ii) PUlasso
(iii) EN1
(iv) EN2
(v) biased−SVM
(vi) PNS
Figure S2: Mis-classiﬁcation rates of algorithms (i)-(vi) under model misspeciﬁcation.
31


## Page 74


S3.2.2
F1 scores under the misspeciﬁed model
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
d = 1.5
d = 2.5
d = 3.5
p = 10
p = 5000
0.0 0.2 0.4 0.6 0.8 0.0 0.2 0.4 0.6 0.8 0.0 0.2 0.4 0.6 0.8
0.6
0.7
0.8
0.9
1.0
0.6
0.7
0.8
0.9
1.0
rho
F1score
Algorithm
G (i) Reference
(ii) PUlasso
(iii) EN1
(iv) EN2
(v) biased−SVM
(vi) PNS
Figure S3: F1 scores of algorithms (i)-(vi) under model misspeciﬁcation
References
Vladimir Koltchinskii. Oracle Inequalities in Empirical Risk Minimization and Sparse Re-
covery Problems: ´Ecole D’´Et´e de Probabilit´es de Saint-Flour XXXVIII-2008. Springer
Science & Business Media, July 2011.
M. Ledoux and M. Talagrand. Probability in Banach Spaces: Isoperimetry and Processes.
32


## Page 75


Springer-Verlag, New York, NY, 1991.
P-L. Loh and M. J. Wainwright. Regularized M-estimators with nonconvexity: Statistical
and algorithmic theory for local optima. Journal of Machine Learning Research, 1:1–9,
2013.
Colin McDiarmid. On the method of bounded diﬀerences. Surveys in combinatorics, 141
(1):148–188, 1989.
S. N. Negahban, R. Pradeep, Bin Yu, and M. J. Wainwright. A Uniﬁed Framework for
High-Dimensional Analysis of M-Estimators with Decomposable Regularizers. Statistica
Sinica, 27(4):538–557, 2012.
A W van der Vaart and J Wellner. Weak Convergence and Empirical Processes: With
Applications to Statistics. Springer Series in Statistics. Springer, 1996.
C. F. JeﬀWu.
On the Convergence Properties of the EM Algorithm.
The Annals of
Statistics, 11(1):95–103, 1983.
W I Zangwill. Nonlinear programming: a uniﬁed approach. Prentice-Hall international
series in management. Prentice-Hall, 1969.
33

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
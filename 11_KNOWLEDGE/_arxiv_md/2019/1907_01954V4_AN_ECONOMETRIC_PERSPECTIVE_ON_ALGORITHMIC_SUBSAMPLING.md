---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1907.01954v4
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1907.01954v4_An_Econometric_Perspective_on_Algorithmic_Subsampling

> Source: 1907.01954v4_An_Econometric_Perspective_on_Algorithmic_Subsampling.pdf

> Pages: 63

---


## Page 1


AN ECONOMETRIC PERSPECTIVE ON ALGORITHMIC SUBSAMPLING
Sokbae Lee∗
Serena Ng†
May 1, 2020
Abstract
Datasets that are terabytes in size are increasingly common, but computer bottlenecks often
frustrate a complete analysis of the data. While more data are better than less, diminishing
returns suggest that we may not need terabytes of data to estimate a parameter or test a hypoth-
esis. But which rows of data should we analyze, and might an arbitrary subset of rows preserve
the features of the original data? This paper reviews a line of work that is grounded in theo-
retical computer science and numerical linear algebra, and which ﬁnds that an algorithmically
desirable sketch, which is a randomly chosen subset of the data, must preserve the eigenstructure
of the data, a property known as a subspace embedding. Building on this work, we study how
prediction and inference can be aﬀected by data sketching within a linear regression setup. We
show that the sketching error is small compared to the sample size eﬀect which a researcher can
control. As a sketch size that is algorithmically optimal may not be suitable for prediction and
inference, we use statistical arguments to provide ‘inference conscious’ guides to the sketch size.
When appropriately implemented, an estimator that pools over diﬀerent sketches can be nearly
as eﬃcient as the infeasible one using the full sample.
Keywords: sketching, coresets, subspace embedding, countsketch, uniform sampling.
JEL Classiﬁcation: C2, C3.
∗Department of Economics, Columbia University and Institute for Fiscal Studies
†Department of Economics, Columbia University and NBER
The authors would like to thank David Woodruﬀand Shusen Wang for helpful discussions. The ﬁrst author would
like to thank the European Research Council for ﬁnancial support (ERC-2014-CoG- 646917-ROMIA) and the UK
Economic and Social Research Council for research grant (ES/P008909/1) to the CeMMAP. The second author would
like to thank the National Science Foundation for ﬁnancial support (SES: 1558623).
arXiv:1907.01954v4  [econ.EM]  30 Apr 2020


## Page 2


1
Introduction
The availability of terabytes of data for economic analysis is increasingly common. But analyzing
large datasets is time consuming and sometimes beyond the limits of our computers. The need to
work around the data bottlenecks was no smaller decades ago when the data were in megabytes
than it is today when data are in terabytes and petabytes. One way to alleviate the bottleneck is to
work with a sketch of the data.1 These are data sets of smaller dimensions and yet representative
of the original data. We study how the design of linear sketches aﬀects estimation and inference
in the context of the linear regression model. Our formal statistical analysis complements those
in the theoretical computer science and numerical linear algebra derived using diﬀerent notions of
accuracy and whose focus is computation eﬃciency.
There are several motivations for forming sketches of the data from the full sample. If the data
are too expensive to store and/or too large to ﬁt into computer memory, the data would be of
limited practical use. It might be cost eﬀective in some cases to get a sense from a smaller sample
whether an expensive test based on the full sample is worth proceeding. Debugging is certainly
faster with fewer observations. A smaller dataset can be adequate while a researcher is learning
how to specify the regression model, as loading a gigabyte of data is much faster than a terabyte
even we have enough computer memory to do so. With conﬁdentiality reasons, one might only
want to circulate a subset rather than the full set of data.
For a sketch of the data to be useful, the sketch must preserve the characteristics of the original
data. Early work in the statistics literature used a sketching method known as ‘data squashing’. The
idea is to approximate the likelihood function by merging data points with similar likelihood proﬁles.
There are two diﬀerent ways to squash the data. One approach is to construct subsamples randomly.
While these methods work well for the application under investigation, its general properties are
not well understood. An alternative is to take the data structure into account. Du Mouchel et
al. (1999) also forms multivariate bins of the data, but they match low order moments within the
bin by non-linear optimization. Owen (1990) reweighs a random sample of X to ﬁt the moments
using empirical likelihood estimation. Madigan et al. (1999) uses likelihood-based clustering to
select data points that match the target distribution. While theoretically appealing, modeling the
likelihood proﬁles can itself be time consuming and not easily scalable.
Data sketching is of also interest to computer scientists because they are frequently required
to provide summaries (such as frequency, mean, and maximum) of data as they stream by contin-
uously.2 Instead of an exact answer which would be costly to compute, pass-eﬃcient randomized
1The term ‘synopsis’ and ‘coresets’ have also been used. See Comrode et al. (2011), and Agarwal and Varadarajan
(2004). We generically refer to these as sketches.
2The seminal paper on frequency moments is Alon et al. (1999). For a review of the literature, he reader is referred
1


## Page 3


algorithms are designed to run fast, requires little storage, and guarantee the correct answer with
a certain probability. But this is precisely the underlying premise of data sketching in statistical
analysis.3
Though randomized algorithms are increasingly used for sketching in a wide range of applica-
tions, the concept remains largely unknown to economists except for a brief exposition in Ng (2017).
This paper provides a gentle introduction to these algorithms in Sections 2 to 4. To our knowledge,
this is the ﬁrst review on sketching in the econometrics literature. We will use the term algorithmic
subsampling to refer to randomized algorithms designed for the purpose of sketching, to distinguish
them from bootstrap and subsampling methods developed for frequentist inference. In repeated
sampling, we only observe one sample drawn from the population. Here, the complete data can
be thought of as the population which we observe, but we can only use a subsample. Algorithmic
subsampling does not make distributional assumptions, and balancing between fast computation
and favorable worst case approximation error often leads to algorithms that are oblivious to the
properties the data. In contrast, exploiting the probabilistic structure is often an important aspect
of econometric modeling.
Perhaps the most important tension between the algorithmic and the statistical view is that
while fast and eﬃcient computation tend to favor sketches with few rows, eﬃcient estimation and
inference inevitably favor using as many rows as possible. Sampling schemes that are optimal from
an algorithmic perspective may not be desirable from an econometric perspective, but it is entirely
possible for schemes that are not algorithmically optimal to be statistically desirable. As there
are many open questions about the usefulness of these sampling schemes for statistical modeling,
there is an increased interest in these methods within the statistics community. Recent surveys on
sketching with a regression focus include Ahfock et al. (2017) and Geppert, Ickstadt, Munteanu,
Quedenfeld and Sohler (2017), among others. Each paper oﬀers distinct insights, and the present
paper is no exception.
Our focus is on eﬃciency of the estimates for prediction and inference within the context of the
linear regression model. Analytical and practical considerations conﬁne our focus eventually back
to uniform sampling, and to a smaller extent, an algorithm known as the countsketch. The results
in Sections 5 and 6 are new. It will be shown that data sketching has two eﬀects on estimation, one
due to sample size, and one due to approximation error, with the former dominating the later in all
quantities of empirical interest. Though the sample size eﬀect has direct implications for the power
of any statistical test, it is at the discretion of a researcher. We show that moment restrictions
to Comrode et al. (2011).
3Pass-eﬃcient algorithms read in data at most a constant number of times. A computational method is referred
to as a streaming model if only one pass is needed.
2


## Page 4


can be used to guide the sketch size, with fewer rows being needed when more moments exist. By
targeting the power of a test at a prespeciﬁed alternative, the size of the sketch can also be tuned
so as not to incur excessive power loss in hypothesis testing. We refer to this as the ‘inference
conscious’ sketch size.
There is an inevitable trade-oﬀbetween computation cost and statistical eﬃciency, but the sta-
tistical loss from using fewer rows of data can be alleviated by combining estimates from diﬀerent
sketches. By the principle of ‘divide and conquer’, running several estimators in parallel can be
statistically eﬃcient and still computationally inexpensive. Both uniform sampling and the counts-
ketch are amenable to parallel processing which facilitates averaging of quantities computed from
diﬀerent sketches. We assess two ways of combining estimators: one that averages the parameter
estimates, and one that averages test statistics. Regardless of how information from the diﬀerent
sketches are combined, pooling over subsamples always provides more eﬃcient estimates and more
powerful tests. It is in fact possible to bring the power of a test arbitrarily close to the one using
the full sample, as will be illustrated in Section 6.
1.1
Motivating Examples
The sketching problem can be summarized as follows. Given an original matrix A ∈Rn×d, we are
interested in eA ∈Rm×d constructed as
eA = ΠA
where Π ∈Rm×n, m < n. In a linear regression setting, A = [y X] where y is the dependent
variable, and X indicates the regressors. Computation of the least squares estimator takes O(nd2)
time which becomes costly when the number of rows, n is large. Non-parametric regressions ﬁt into
this setup if X is a matrix of sieve basis. Interest therefore arises to use fewer rows of A without
sacriﬁcing too much information.
To motivate why the choice of the sampling scheme (ie. Π) matters, consider as an example a
5 × 2 matrix
A =
1
0
−.25
.25
0
0
1
.5
−.5
0
T
.
The rows have diﬀerent information content as the row norm is (1, 1, 0.559, 0.559, 0)T . Consider
3


## Page 5


now three 2 × 2 eA matrices constructed as follows:
Π1 =
1
0
0
0
0
0
1
0
0
0

,
eA1 = Π1A =
1
0
0
1

Π2 =
1
0
0
0
0
0
0
0
0
1

,
eA2 = Π2A =
1
0
0
0

Π3 =
0
0
1
1
0
0
1
−1
1
1

,
eA3 = Π3A =
0
0
.5
0

.
Of the three sketches, only Π1 preserves the rank of A. The sketch deﬁned by Π2 fails because
it chooses row 5 which has no information. The third sketch is obtained by taking a linear com-
bination of rows that do not have independent information. The point is that unless Π is chosen
appropriately, eA may not have the same rank as A.
Of course, when m is large, changing rank is much less likely and one may also wonder if this
pen and pencil problem can ever arise in practice. Consider now estimation of a Mincer equation
which has the logarithm of wage as the dependent variable, estimated using the IPUMS (2020)
dataset which provides a preliminary but complete count data for the 1940 U.S. Census. This data
is of interest because it was the ﬁrst census with information on wages and salary income. For
illustration, we use a sample of n = 24 million white men between the age of 16 and 64 as the
‘full sample’. The predictors that can be considered are years of education, denoted (edu), and
potential experience, denoted (exp).
Figure 1: Distribution of Potential Experience
Two Mincer equations with diﬀerent covariates are considered:
log wage
=
β0 + β1edu + β2exp + β3exp2 + error
(1a)
log wage
=
β0 + β1edu +
11
X
j=0
β2+j1{5j ≤exp < 5(j + 1)} + error.
(1b)
4


## Page 6


Model (1a) uses exp and exp2 as control variables. Model (1b) replaces potential experience with
indicators of experience in ﬁve year intervals. Even though there are three predictors including the
intercept, the number of covariates K is 4 in the ﬁrst model and 14 in the second. In both cases,
the parameter of interest is the coeﬃcient for years of education (β1). The full sample estimate of
β1 is 0.12145 in speciﬁcation (1a) and 0.12401 in speciﬁcation (1b).
Figure 1 shows the histogram of exp. The values of exp range from 0 to 58. The problem in this
example arises because there are few observations with over 50 years of experience. Hence there is
no guarantee that an arbitrary subsample will include observations with exp > 50. Without such
observations, the subsampled covariate matrix may not have full rank. Speciﬁcation (1b) is more
vulnerable to this problem especially when m is small.
We verify that rank failure is empirically plausible in a small experiment with sketches of size
m = 100 extracted using two sampling schemes. The ﬁrst method is uniform sampling without
replacement which is commonly used in economic applications. The second is the countsketch which
will be further explained below. Figure 2 and Figure 3 show the histograms of subsample estimates
for uniform sampling and the countsketch, respectively. The left panel is for speciﬁcation (1a)
and the right panel is for speciﬁcation (1b). In our experiments, singular matrices never occurred
with speciﬁcation (1a); the OLS estimates can be computed using both sampling algorithms and
both performed pretty well. However, uniform sampling without replacement produced singular
matrices for speciﬁcation (1b) 77% of the time. The estimates seem quite diﬀerent from the full
sample estimates, suggesting not only bias in the estimates, but also that the bias might not be
random. In contrast, the countsketch failed only once out of 100 replications. The estimates are
shown in the right panel of Figure 3 excluding the singular case.
This phenomenon can be replicated in a Monte Carlo experiment with K = 3 normally dis-
tributed predictors. Instead of X3, it is assumed that we only observe a value of one if X3 is three
standard deviation from the mean. Together with an intercept, there are four regressors. As in the
Mincer equation, the regressor matrix has a reduced rank of 3 with probability of 0.58, 0.25, 0.076
when m = 200, 500, 1000 rows are sampled uniformly; it is always full rank only when m = 2000. In
contrast, the countsketch never encounters this problem even with m = 100. The simple example
underscores the point that the choice of sampling scheme matters. As will be seen below, the issue
remains in a more elaborate regression with several hundred covariates. This motivates the need
to better understand how to form sketches for estimation and inference.
5


## Page 7


Figure 2: Distributions of Estimates from Uniform Sampling without Replacement
Figure 3: Distributions of Estimates from CountSketch Sampling
2
Matrix Sketching
This section presents the key concepts in algorithmic sampling.
The material is based heavily
on the monographs by Mahoney (2011) and Woodruﬀ(2014), as well as the seminal work of
Drineas, Mahoney and Muthukrishnan (2006), and subsequent reﬁnements developed in Drineas et
al. (2011), Nelson and Nguyen (2013a), Nelson and Nguyen (2014), Cohen, Nelson and Woodruﬀ
(2015), Wang, Gittens and Mahoney (2018), among many others.
We begin by setting up the notation. Consider an n × d matrix positive-deﬁnite A. Let A(j)
denote its j-th column of A and A(i) be its i-th row. Then
A =



A(1)
...
A(n)


=
 A(1)
. . .
A(d)
and AT A = Pn
i=1 AT
(i)A(i). The singular value decomposition of A is A = UΣV T where U and
V are the left and right eigenvectors of dimensions (n × d) and (d × d) respectively. The matrix
Σ is d × d diagonal with entries containing the singular values of A denoted σ1, . . . , σd, which are
ordered such that σ1 is the largest. Since AT A is positive deﬁnite, its k-th eigenvalue ωk(AT A)
6


## Page 8


equals σk(AT A) = σ2
k(A), for k = 1, . . . d. The best rank k approximation of A is given by
Ak = UkUT
k A ≡PUkA
where Uk is an n × k orthonormal matrix of left singular vectors corresponding to the k largest
singular values of A, and PUk = UkUT
k is the projection matrix.
The Frobenius norm (an average type criterion) is ∥A∥F =
qPn
i=1
Pd
j=1 |Aij|2 =
qPk
i=1 σ2
i .
The spectral norm (a worse-case type criterion) is ∥A∥2 = sup∥x∥2=1 ∥Ax∥2 =
p
σ2
1, where ∥x∥2 is
the Euclidean norm of a vector x. The spectral norm is bounded above by the Frobenius norm
since ∥A∥2
2 = |σ1|2 ≤Pn
i=1
Pd
j=1 |Aij|2 = ∥A∥2
F = Pd
i=1 σ2
i .
Let f and g be real valued functions deﬁned on some unbounded subset of real positive numbers
n. We say that g(n) = O(f(n)) if |g(n)| ≤k|f(n)| for some constant k for all n ≥n0. This means
that g(n) is at most a constant multiple of f(n) for suﬃciently large values of n. We say that
g(n) = Ω(f(n)) if g(n) ≥kf(n) for all n ≥n0. This means that g(n) is at least kf(n) for some
constant k. We say that g(n) = Θ(f(n)) if k1f(n) ≤g(n) ≤k2f(n) for all n ≥n0. This means
that g(n) is at least k1f(n) and at most k2f(n).
2.1
Approximate Matrix Multiplication
Suppose we are given two matrices, A ∈Rn×d and B ∈Rn×p and are interested in the d × p matrix
C = AT B. The textbook approach is to compute each element of C by summing over dot products:
Cij = [AT B]ij =
n
X
k=1
AT
ikBkj.
Equivalently, each element is the inner product of two vectors A(i) and B(j). Computing the entire
C entails three loops through i ∈[1, d], j ∈[1, p], and k ∈[1, n]. An algorithmically more eﬃcient
approach is to form C from outer products:
C = AT B
| {z }
d×p
=
n
X
i=1
AT
(i)B(i)
| {z }
(d×1)×(1×p)
,
making C a sum of n matrices each of rank-1.
Viewing C as a sum of n terms suggests to
approximate it by summing m < n terms only. But which m amongst the
n!
m!(n−m)! possible terms
to sum? Consider the following Approximate Matrix Multiplication algorithm (AMM). Let pj be
the probability that row j will be sampled.
7


## Page 9


Algorithm AMM:
Input: A ∈Rn×d, B ∈Rn×p, m > 0, p = (p1, . . . , pn).
1 for s = 1 : m do
2
sample ks ∈[1, . . . n] with probability pks independently with replacement;
3
set eA(s) =
1
√mpks A(ks) and eB(s) =
1
√mpks B(ks)
Output: eC = eAT eB.
The algorithm essentially produces
eC
=
(ΠA)T ΠB = 1
m
m
X
s=1
1
pks
AT
(ks)B(ks)
(2)
where ks denotes the index for the non-zero entry in the s row of the matrix
Π =
1
√m



0
1
√pk1
0
. . .
0
. . .
. . .
. . .
. . .
. . .
0
0
. . .
1
√pkm
0


.
The Π matrix only has only one non-zero element per row, and the (i, j)-th entry Πij =
1
√mpj with
probability pj. In the case of uniform sampling with pk = 1
n for all i, Π reduces to a sampling
matrix scaled by
√n
√m.
While eC deﬁned by (2) is recognized in econometrics as the estimator of Horvitz and Thompson
(1952) which uses inverse probability weighting to account for diﬀerent proportions of observations
in stratiﬁed sampling, eC is a sketch of C produced by the Monte Carlo algorithm AMM in the
theoretical computer science literature.4 The Monte-Carlo aspect is easily understood if we take A
and B to be n × 1 vectors. Then AT B = Pn
i=1 AT
(i)B(i) = Pn
i=1 f(i) ≈
R n
0 f(x)dx = f(a)n where
the last step follows from mean-value theorem for 0 < a < n. Approximating f(a) by 1
m
Pm
s=1 f(ks)
gives n
m
Pm
s=1 f(ks) as the Monte Carlo estimate of
R n
0 f(x)dx.
Two properties of eC produced by AMM are noteworthy. Under independent sampling,
E
 1
m
m
X
s=1
AiksBksj
pks

= 1
m
m
X
s=1
n
X
k=1
pk
AikBkj
pk
= [AT B]ij.
Hence regardless of the sampling distribution, eC is unbiased. The variance of eC deﬁned in terms
of the Frobenius norm is
E
h
∥eC −C∥2
F
i
=
1
m
n
X
k=1
1
pk
∥AT
(k)∥2
2∥B(k)∥2
2 −1
m∥C∥2
F
4In Mitzenmacher and Upfal (2006), a Monte Carlo algorithm is a randomized algorithm that may fail or return
an incorrect answer but whose time complexity is deterministic and does not depend on the particular sampling. This
contrasts with a Las Vegas algorithm which always returns the correct answer but whose time complexity is random.
See also Eriksson-Bique et al. (2011).
8


## Page 10


which depends on the sampling distribution p. Drineas, Kannan and Mahoney (2006, Theorem
1) shows that minimizing Pn
k=1
1
pk ∥AT
(k)∥2
2∥B(k)∥2
2 with respect to p subject to the constraint
Pn
k=1 pk = 1 gives5
pk =
∥A(k)∥2∥B(k)∥2
Pn
s=1 ∥A(s)∥2∥B(s)∥2
.
This optimal p yields a variance of
E
h
∥eC −C∥2
F
i
≤1
m
h
n
X
k=1
∥A(k)∥2∥B(k)∥2
i2
≤1
m∥A∥2
F ∥B∥2
F .
It follows from Markov’s inequality that for given error of size ε and failure probability δ > 0,
P

∥eC −C∥2
F > ε2∥A∥2
F ∥B∥2
F

<
E
h
∥eC −C∥2
F
i
ε2∥A∥2
F ∥B∥2
F
<
1
mε2 ,
implying that to have an approximation error no larger than ε with probability 1 −δ, the number
of rows used in the approximation must satisfy m = Ω( 1
δε2 ).
The approximate matrix multiplication result ∥AT B −eAT eB∥F ≤ε∥A∥F ∥B∥F is the building
block of many of the theoretical results to follow. The result also holds under the spectral norm
since it is upper bounded by the Frobenius norm. Since AT
(i)B(i) is a rank one matrix, ∥AT
(i)B(i)∥2 =
∥AT
(i)∥2∥B(i)∥2. Many of the results to follow are in spectral norm because it is simpler to work
with a product of two Euclidean vector norms. Furthermore, putting A = B, we have
P(∥(ΠA)T (ΠA) −AT A)∥2 ≥ϵ∥A∥2
2) < δ.
One may think of the goal of AMM as preserving the second moment properties of A. The challenge
in practice is to understand the conditions that validate the approximation. For example, even
though uniform sampling is the simplest of sampling schemes, it cannot be used blindly. Intuitively,
uniform sampling treats all data points equally, and when information in the rows are not uniformly
dispersed, the inﬂuential rows will likely be omitted.
From the above derivations, we see that
var( eC) = O( n
m) when pk =
1
n, which can be prohibitively large.
The Mincer equation in the
Introduction illustrates the pitfall with uniform sampling when m is too small, but that the problem
can by and large be alleviated when m > 2000. Hence, care must be taken in using the algorithmic
sampling schemes. We will provide some guides below.
5The ﬁrst order condition satiﬁes 0 = −1
p2
k ∥AT
(k)∥2
2∥B(k)∥2
2 + λ.
Solving for
√
λ and imposing the constraint
gives the result stated. Eriksson-Bique et al. (2011) derives probabilities that minimize expected variance for given
distribution of the matrix elements.
9


## Page 11


2.2
Subspace Embedding
To study the properties of the least squares estimates using sketched data, we ﬁrst need to make
clear what features of A need to be preserved in eA. Formally, the requirement is that Π has a
‘subspace embedding’ property. An embedding is a linear transformation of the data that has the
Johnson-Lindenstrauss (JL) property, and a subspace embedding is a matrix generalization of an
embedding. Hence it is useful to start with the celebrated JL Lemma.
The JL Lemma, due to Johnson and Lindenstauss (1994), is usually written for linear maps
that reduce the number of columns from an n × d matrix (i.e., d) to k. Given that our interest
is ultimately in reducing the number of rows from n to m while keeping d ﬁxed, we state the JL
Lemma as follows:
Lemma 1 (JL Lemma) Let 0 < ϵ < 1 and {a1, . . . , ad} be a set of d points in Rn with n > d.
Let m ≥8 log d/ϵ2. There exists a linear map Π : Rn →Rm such that ∀ai, aj
(1 −ϵ)||ai −aj||2
2 ≤||Πai −Πaj||2
2 ≤(1 + ϵ)||ai −aj||2
2.
In words, the Lemma states that every set of d points in Euclidean space of dimension n can
be represented by a Euclidean space of dimension m = Ω(log d/ϵ2) with all pairwise distances
preserved up to a 1 ± ϵ factor. Notice that m is logarithmic in d and does not depend on n. A
sketch of the proof is given in the Appendix.
The JL Lemma establishes that d vectors in Rn can be embedded into m = Ω(log d/ϵ2) dimen-
sions. But there are situations when we need to preserve the information in the d columns jointly.
This leads to the notion of ‘subspace embedding’ which requires that the norm of vectors in the
column space of A be approximately preserved by Π with high probability.
Deﬁnition 1 (Subspace-Embedding) Let A be an n×d matrix. An L2 subspace embedding for
the column space of A is an m(ϵ, δ, d) × n matrix Π such that ∀x ∈Rd,
(1 −ϵ)∥Ax∥2
2 ≤∥ΠAx∥2
2 ≤(1 + ϵ)∥Ax∥2
2.
(3)
Subspace embedding is an important concept and it is useful to understand it from diﬀerent
perspectives. Given that ∥Ax∥2
2 = xT AT Ax, preserving the column space of A means preserving
the information in AT A. The result can analogously be written as
∥ΠAx∥2
2 ∈

(1 −ϵ)∥Ax∥2
2, (1 + ϵ)∥Ax∥2
2

.
10


## Page 12


Since Ax = UΣV T x = Uz where z = ΣV T x ∈Rd and U is orthonormal, a change of basis gives:
∥ΠUz∥2
2
∈

(1 −ϵ)∥Uz∥2
2, (1 + ϵ)∥Uz∥2
2

=

(1 −ϵ)∥z∥2
2, (1 + ϵ)∥z∥2
2

⇔
∥(ΠU)T (ΠU) −UT U∥2 ≤ϵ
⇔
zT

(ΠU)T (ΠU) −Id

z ≤ϵ.
The following Lemma deﬁnes subspace embedding in terms of singular value distortions.
Lemma 2 Let U ∈Rn×d be a unitary matrix and Π be a subspace embedding for the column space
of A. Let σk is the k-th singular value of A. Then (3) is equivalent to
σ2
k(ΠU) ∈[1 −ϵ, 1 + ϵ]
∀k ∈[1, d].
To understand Lemma 2, consider the Rayleigh quotient form of ΠU:6
ωk((ΠU)T (ΠU)) = vT
k (ΠU)T (ΠU)vk
vT
k vk
for some vector vk ̸= 0. As ωk(AT A) = σ2
k(A),
ωk((ΠU)T (ΠU))
=
vT
k vk −vT
k

Id −(ΠU)T (ΠU)

vk
vT
k vk
=
1 −ωk

Id −(ΠU)T (ΠU)

.
This implies that |1 −σ2
k(ΠU)| = |ωk(Id −(ΠU)T (ΠU))| = σk(Id −(ΠU)T (ΠU)). It follows that
|1 −σ2
k(ΠU)|
=
σk

UT U −(ΠU)T (ΠU)

≤
σmax(UT U −(ΠU)T (ΠT U))
=
∥UT U −(ΠU)T (ΠU)∥2 ≤ϵ
⇔σ2
k(ΠU)
∈
[1 −ϵ, 1 + ϵ]
∀k ∈[1, d].
Hence the condition ∥(ΠU)T ΠU −Id∥2 ≤ϵ is equivalent to Π generating small singular value
distortions. Nelson and Nguyen (2013a) relates this condition to similar results in random matrix
theory.7
6For a Hermitian matrix M, the Rayleigh quotient is cT Mc
cT c
for a nonzero vector c. By Rayleigh-Ritz Theorem,
min(σ(M)) ≤cT Mc
cT c
≤max(σ(M)) with equalities when c is the eigenvector corresponding to the smallest and largest
eigenvalues of M, respectively. See, e.g. Hogben (2007, Section 8.2).
7 Consider a T × N matrix of random variables with mean zero and unit variance with c = limN,T →∞N
T . In
random matrix theory, the largest and smallest eigenvalues of the sample covariance matrix have been shown to
converge to (1 + √c)2, (1 −√c)2, respectively. See, e.g., Yin et al. (1988) and Bai and Yin (1993).
11


## Page 13


But where to ﬁnd these embedding matrices? We can look for data dependent or data oblivious
ones. We say that Π is a data oblivious embedding if it can be designed without knowledge of the
input matrix. The idea of oblivious subspace-embedding ﬁrst appeared in Sarlos (2006) in which
it is suggested that Π can be drawn from a distribution with the JL properties.
Deﬁnition 2 A random matrix Π ∈Rm×n drawn from a distribution F forms a JL transform with
parameters ϵ, δ, d if there exists a function f such that for any 0 ≤ϵ, δ ≤1 and m = Ω(log( d
ϵ2 f(δ))),
(1 −ϵ)∥x∥2
2 ≤∥Πx∥2
2 ≤(1 + ϵ)∥x∥2
2 holds with probability at least 1 −δ for all d-vector x ⊂Rn.
A JL transform is often written JLT(ϵ, δ, d) for short. Embedding matrices Π that are JLT guarantee
good approximation to matrix products in terms of Frobenius norm. This means that for such Πs,
an m can be chosen such that for conformable matrices A, B having n rows:
P

∥(ΠA)T (ΠB) −AT B∥F ≤ϵ∥A∥F ∥B∥F

≥1 −δ.
(4)
The Frobenius norm bound has many uses. If A = B, then ∥ΠA∥2
F = (1 ± ϵ)∥A∥2
F with high
probability. The result also holds in the spectral norm, Sarlos (2006, Corollary 11).
3
Random Sampling, Random Projections, and the Countsketch
There are two classes of Πs with the JL property: random sampling which reduces the row dimension
by randomly picking rows of A, and random projections which form linear combinations from the
rows of A. A scheme known as a countsketch that is not a JL transform can also achieve subspace
embedding eﬃciently. We will use a pen and pencil example with m = 3 and n = 9 to provide a
better understanding of the three types of Πs. In this example, A has 9 rows given by A1, . . . , A9.
3.1
Random Sampling (RS)
Let D be a diagonal rescaling matrix with
1
√mpi in the i-th diagonal and pi is the probability that
row i is chosen. Under random sampling,
Π
=
DS,
where Sjk = 1 if row k is selected in the j-th draw and zero otherwise so that the j-th row of
the selection matrix S is the jth-row of an n dimensional indentity matrix. Examples of sampling
schemes are:
RS1. Uniform sampling without replacement: Π ∈Rm×n, D ∈Rm×m, pi = 1
n for all i. Each row is
sampled at most once.
12


## Page 14


RS2. Uniform sampling with replacement: Π ∈Rm×n, D ∈Rm×m, pi = 1
n for all i. Each row can
be sampled more than once.
RS3. Bernoulli sampling uses an n × n matrix Π = DS, where D = p n
mIn, S is initialized to be
0n×n and the j-th diagonal entry is updated by
Sjj =
(
1
with probability m
n
0
with probability 1 −m
n
Each row is sampled at most once, and m is the expected number of sampled rows.
RS4. Leverage score sampling: the sampling probabilities are taken from importance sampling
distribution
pi =
ℓi
Pn
i=1 ℓi
= ℓi
d ,
(5)
where for A with svd(A) = UDV T ,
ℓi = ∥U(i)∥2
2 = ∥eT
i U∥2
2,
is the leverage score for row i, P
i ℓi = ∥U∥2
F = d, and ei is a standard basis vector.
Notably, the rows of the sketch produced by random sampling are the rows of the original
matrix A. For example, If rows 9,5,1 are randomly chosen by uniform sampling, RS1 would give
eA = D


0
0
0
0
0
0
0
0
1
0
0
0
0
1
0
0
0
0
1
0
0
0
0
0
0
0
0

A =
√
9
√
3


A9
A5
A1

.
Ipsen and Wentworth (2014, Section 3.3) shows that sampling schemes RS1-RS3 are similar
in terms of the condition number and rank deﬁciency in the matrices that are being subsampled.
Unlike these three sampling schemes, leverage score sampling is not data oblivious and warrants
further explanation.
As noted above, uniform sampling may not be eﬃcient. More precisely, uniform sampling does
not work well when the data have high coherence, where coherence refers to the maximum of the
row leverage scores ℓi deﬁned above. Early work suggests to use sampling weights that depend on
the Euclidean norm, pi = ∥Ai∥2
2
∥A∥2
F . See, e.g., Drineas, Kannan and Mahoney (2006) and Drineas and
Mahoney (2005). Subsequent work ﬁnds that a better approach is to sample according to the lever-
age scores which measure the correlation between the left singular vectors of A with the standard
basis, and thus indicates whether or not information is spread out. The idea of leverage-sampling,
ﬁrst used in Jolliﬀe (1972), is to sampling a row more frequently if it has more information.8 Of
8There are other variations of leverage score sampling. McWilliams et al. (2014) considers subsampling in linear
regression models when the observations of the covariances may be corrupted by an additive noise. The inﬂuence of
observation i is deﬁned by di =
e2
i ℓi
(1−ℓi)2 , where ei is the OLS residual and ℓi is the leverage score. Unlike leverage
scores, di takes into account the relation between the predictor variables and the y.
13


## Page 15


course, ℓi is simply the i-th diagonal element of the hat matrix A(AT A)−1AT , known to contain
information about inﬂuential observations. In practice, computation of the leverage scores requires
an eigen decomposition which is itself expensive. Drineas et al. (2012) and Cohen, Lee, Musco,
Musco, Peng and Sidford (2015) suggest fast approximation of leverage scores.
3.2
Random Projections (RP)
Some examples of random projections are:
RP1. Gaussian: Π ∈Rm×n where Πij =
1
√mN(0, 1).
RP2. Rademacher random variables: with entries of {+1, −1}, Sarlos (2006), Achiloptas (2003).
RP3. Randomized Orthogonal Systems: Π = p n
mPHD where D is an n×n is diagonal Rademacher
matrix with entries of ±1, P is a sparse matrix, and H is an orthonormal matrix.
RP4. Sparse Random Projections (SRP)
Π = DS
where D ∈Rm×m is a diagonal matrix of p s
m and S ∈Rm×n
Sij =





−1
with probability
1
2s
0
with probability 1 −1
s
1
with probability
1
2s
RP1 and RP2 form sub-Gaussian random projections:9 The rows of the sketch produced by
random projections are linear combinations of the rows of the original matrix. For example, RP4
with s = 3 could give
eA = D


0
0
1
1
0
−1
0
0
0
1
0
−1
0
−1
0
0
0
1
0
1
0
0
0
0
1
0
−1

A =
√
3
√
9


A3 + A4 −A6
A1 −A3 −A5 + A9
A2 + A7 −A9


Early work on random projections such as Dasgupta et al. (2010) uses Πs that are dense, an
example being RP1. Subsequent work favors sparser Πs, an example being RP4. Achiloptas (2003)
initially considers s = 3. Li et al. (2006) suggests to increase s to √n. Given that uniform sampling
is algorithmically ineﬃcient when information is concentrated, the idea of randomized orthogonal
systems is to ﬁrst randomize the data by the matrix H to destroy uniformity, so that sampling in a
data oblivious manner using P and rescaling by D remains appropriate. The randomization step is
9A mean-zero vector s ∈Rn is sub-Gaussian if for any u ∈Rn and for all ϵ > 0, P{|uT s| ≥ϵ∥u∥2} ≤2e−ϵ2/K2 for
some absolute constant K > 0.
14


## Page 16


sometimes referred to as ‘preconditioning’. Common choices of H are the Hadamard matrix as in
the SRHT of Ailon and Chazelle (2009)10 and the discrete Fourier transform as in FJLT of Woolfe
et al. (2008).
3.3
Countsketch
While sparse Πs reduce computation cost, Kane and Nelson (2014, Theorem 2.3) shows that each
column of Π must have Θ(d/ϵ) non-zero entries to create an L2 subspace embedding. This would
seem to suggest that Π cannot be too sparse. However, Clarkson and Woodruﬀ(2013) argues that
if the non-zero entries of Π are carefully chosen, Π need not be a JLT and a very sparse subspace
embedding is actually possible. Their insight is that Π need not preserve the norms of an arbitrary
subset of vectors in Rn, but only those that sit in the d-dimensional subspace of Rn. The sparse
embedding matrix considered in Clarkson and Woodruﬀ(2013) is the countsketch.11
A countsketch of sketching dimension m is a random linear map Π = PD : Rn →Rm where
D is an n × n random diagonal matrix with entries chosen independently to be +1 or −1 with
equal probability. Furthermore, P ∈{0, 1} is an m × n binary matrix such that Ph(i),i = 1 and
Pj,i = 0 for all j ̸= h(i), and h : [n] →[m] is a random map such that for each i ∈[n], h(i) = m′
for m′ ∈[m] with probability
1
m. As an example, a countsketch might be
eA =


0
0
1
0
1
−1
0
0
1
−1
0
0
−1
0
0
0
−1
0
0
−1
0
0
0
0
1
0
0

A =


A3 + A5 −A6 + A9
−A1 −A4 −A8
−A2 + A7

.
Like random projections, the rows of a countsketch are also a linear combinations of the rows of A.
Though the countsketch is not a JLT, Nelson and Nguyen (2013b) and Meng and Mahoney
(2013) show that the following spectral norm bound holds for the countsketch with appropriate
choice of m:
P

∥(ΠU)T (ΠU) −Id∥2 > 3ϵ

≤δ
(6)
which implies that countsketch provides a 1 + ε subspace embedding for the column space of A in
spite of not being a JLT, see Woodruﬀ(2014, Theorem 2.6).
The main appeal of the countsketch is that the run time needed to compute ΠA can be reduced
to O(nnz(A)), where nnz(A) denotes the number of non-zero entries of A. The eﬃciency gain is
due to extreme sparsity of a countsketch Π which only has one non-zero element per column. Still,
10The Hadamard matrix is deﬁned recursively by Hn =
Hn/2
Hn/2
Hn/2
−Hn/2

,
H2 =
1
1
1
−1

. A constraint is that
n must be in powers of two.
11The deﬁnition is taken from Dahiya et al. (2018). Given input j, a count-sketch matrix can also be characterized
by a hash function h(j) such that ∀j, j′, j ̸= j′ →h(j) ̸= h(j′). Then Πh(j),j = ±1 with equal probability 1/2.
15


## Page 17


the Π matrix can be costly to store when n is large. Fortunately, it is possible to compute the
sketch without constructing Π.
The streaming version of the countsketch is a variant of the frequent-items algorithm where we
recall that having to compute summaries such as the most frequent item in the data that stream by
was instrumental to the development of sketching algorithms. The streaming algorithm proceeds
by initializing eA to an m × n matrix of zeros. Each row A(i) of A is updated as
eAh(i) = eAh(i) + g(i)A(i)
where h(i) sampled uniformly at random from [1, 2, . . . m] and gi sampled from {+1, −1} are in-
dependent. Computation can be done one row at a time.12 The Appendix provides the streaming
implementation of the example above.
3.4
Properties of the Πs
To assess the actual performance of the diﬀerent Πs, we conduct a small Monte Carlo experiment
with 1000 replications. For each replication b, we simulate an n × d matrix A and construct the
seven JL embeddings considered above. For each embedding, we count the number of times that
∥|Π(ai −aj)||2
2 is within (1 ± ϵ) of ||ai −aj||2
2 for all d(d + 1)/2 pairs of distinct (i, j). The success
rate for the replication is the total count divided by d((d + 1)/2. We also record ||σ(ΠA)
σ(A) −1||2
where σ(ΠA) is a vector of d singular values of ΠA. According to theory, the pairwise distortion
of the vectors should be small if m ≥C log d/ϵ2. We set (n, d) = (20, 000) and ϵ = 0.1. Four
values of C = {1, 2, 3, 4, 5, 6, 8, 16} are considered. We draw A from the (i) normal distribution,
and (ii) the exponential distribution.
In matlab, these are generated as X=randn(n,d) and
X=exprnd(d,[n d]). Results for the Pearson distribution using X=pearsrnd(0,1,1,5,n,d) are
similar and not reported.
Table 1 reports the results averaged over 1000 simulations. With probability around 0.975, the
pairwise distance between columns with 1000 rows is close to the pairwise distance between columns
with 20000 rows. The average singular value distortion also levels oﬀwith about 1000 rows of data.
Hence, information in n rows can be well summarized by a smaller matrix with m rows. However,
note that more rows are generally needed for uniform sampling, while fewer rows are needed for
leverage score sampling, to have the same error as the remaining methods. The takeaway from
Table 1 is that the performance of the diﬀerent Πs are quite similar, making computation cost and
analytical tractability two important factor in deciding which ones to use.
12See Ghashami et al. (2016). Similar schemes have been proposed in Charika et al. (2002); Conmode and Muthukr-
ishnan (2005).
16


## Page 18


Choosing a Π is akin to choosing a kernel function in nonparametric regression and many will
work well, but there are analytical diﬀerences. Any ΠT Π can be written as In + R11 + R12 where
R11 is a generic diagonal and R12 is a generic n × n matrix with zeros in each diagonal entry. Two
features will be particularly useful.
ΠT Π = In + R11
(7a)
ΠΠT = n
mIm
(7b)
Property (7a) imposes that ΠT Π is a diagonal matrix, allowing R11 ̸= 0 but restricting R12 = 0.
Each ΠΠT can also be written as ΠΠT = n
mIm + R21 + R22 where R21 is a generic diagonal and
R22 is a generic m × m matrix with zeros in each diagonal entry. Property (7b) requires that ΠΠT
is proportional to an identity matrix, and hence that R21 = R22 = 0m×m.
For the Πs previously considered, we summarize their properties as follows:
(7a)
(7b)
RS1 (Uniform,w/o)
yes
yes
RS2 (Uniform,w)
yes
no
RS3 (Bernoulli)
yes
no
RS4 (Leverage)
yes
no
RP1 (Gaussian)
no
no
RP2 (Rademacher)
no
no
RP3 (SRHT)
yes
yes
RP4 (SRP)
no
no
CS (Countsketch)
no
no
Property (7a) holds for all three random sampling methods but of all the random projection methods
considered, the property only holds for SRHT. This is because SRHT eﬀectively performs uniform
sampling of the randomized data. For property (7b), it is easy to see that R21 = 0 and R22 =
0m×m when uniform sampling is done without replacement and ΠΠT =
n
mIm. By implication,
the condition also holds for SRHT if sampling is done without replacement since H and D are
orthonormal matrices. But uniform sampling is computationally much cheaper than SRHT and
has the distinct advantage over the SRHT that the rows of the sketch are those of the original
matrix and hence interpretable. For this reason, we will subsequently focus on uniform sampling
and use its special structure to obtain precise statistical results. Though neither condition holds for
the countsketch, the computation advantage due to its extreme sparse structure makes it worthy
of further investigation.
17


## Page 19


4
Algorithmic Results for the Linear Regression Model
The linear regression model with K regressors is y = Xβ+e. The least squares estimator minimizes
∥y −Xb∥2 with respect to b and is deﬁned by
ˆβ = (XT X)−1XT y = V Σ−1UT y.
We are familiar with the statistical properties of ˆβ under assumptions about e and X. But even
without specifying a probabilistic structure, ∥y −Xb||2 with n > K is an over-determined system of
equations and can be solved by algebraically. The svd solution gives β∗= X−y where svd(X) =
UΣV T , the pseudoinverse is X−= V Σ−1UT .
The ’Choleski’ solution starts with the normal
equations XT Xβ = XT y and factorizes XT X. The algebraic properties of these solutions are well
studied in the matrix computations literature when all data are used.
Given an embedding matrix Π and sketched data (Πy, ΠX), minimizing ∥Π(y −Xb)∥2
2 with
respect to b gives the sketched estimator
eβ =

(ΠX)T ΠX
−1
(ΠX)T Πy.
Let d
ssr = ∥y −X ˆβ∥2
2 be the full sample sum of squared residuals.
For an embedding matrix
Π ∈Rm×n, let g
ssr = ∥ey −e
X eβ∥2
2 be the sum of squared residuals from using the sketched data.
Assume that the following two conditions hold with probability 1 −δ for 0 < ϵ < 1:
|1 −σ2
k(ΠU)|
≤
1
√
2
∀k = 1, . . . , K;
(8a)
∥(ΠU)T Π(y −X ˆβ)∥2
2
≤
ϵ d
ssr2/2.
(8b)
Condition (8a) is is equivalent to ∥(ΠU)T (ΠU)−UT U∥2 ≤
1
√
2 as discussed above. Since σi(U) = 1
for all k ∈[1, K], the condition requires the smallest singular value, σK(ΠU), to be positive so that
ΠX has the same rank as X. A property of the least squares estimator is for the least squares
residuals to be orthogonal to X, ie. UT (y −X ˆβ) = 0. Condition (8b) requires near orthogonality
when both quantities are multiplied by Π. The two algorithmic features of sketched least squares
estimation are summarized below.
Lemma 3 Let the sketched data be (Πy, ΠX) = (ey, e
X) where Π ∈Rm×n is a subspace embedding
matrix. Let σmin(X) be the smallest singular value of X. Suppose that conditions (8a) and (8b)
hold. Then with probability at least (1 −δ) and for suitable choice of m,
(i). g
ssr ≤(1 + ϵ)d
ssr;
(ii). ∥eβ −ˆβ∥2 ≤ϵ · d
ssr/σmin.
18


## Page 20


Sarlos (2006) provides the proof for random projections, while Drineas, Mahoney and Muthukrish-
nan (2006) analyzes the case of leverage score sampling. The desired m depends on the result and
the sampling scheme.
Part (i) is based on subspace embedding arguments. By optimality of eβ and JL Lemma,
g
ssr
=
∥Π(y −X eβ)|2
≤
∥Π(y −X ˆβ)∥2
by optimality of eβ
≤
(1 + ϵ)∥y −X ˆβ∥2
by subspace embedding
=
(1 + ϵ)d
ssr.
Part (ii) shows that the sketching error is data dependent.
Consider a reparameterization of
X ˆβ = UΣV T ˆβ = U ˆθ and X eβ = UΣV T eβ = U eθ. As shown in the Appendix, ∥eθ −ˆθ∥2 ≤√ϵ d
ssr.
Taking norms on both sides of X(eβ −ˆβ) = U(eθ −ˆθ) and since U is orthonormal,
∥eβ −ˆβ∥2
≤
∥U(eθ −ˆθ)∥2
σmin
.
Notably, diﬀerence between ˆβ and eβ depends on the minimum singular value of X. Recall that for
consistent estimation, we also require that the minimum eigenvalue to diverge.
The non-asymptotic worse case error bounds in Lemma 3 are valid for any subspace embedding
matrix Π, though more precise statements are available for certain Πs. For leverage score sampling,
see Drineas, Mahoney and Muthukrishnan (2006), for uniform sampling and SRHT, see Drineas
et al. (2011); and for the countsketch, Woodruﬀ(2014, Theorem 2.16), Meng and Mahoney (2013,
Theorem 1), Nelson and Nguyen (2013a). These algorithmic results are derived without reference
to the probabilistic structure of the data. Hence the results do not convey information such as
bias and sampling uncertainty. An interesting question is whether optimality from an algorithmic
perspective implies optimality from a statistical perspective. Using Taylor series expansion, Ma
et al. (2014) shows that leverage-based sampling does not dominate uniform sampling in terms
of bias and variance, while Raskutti and Mahoney (2016) ﬁnds that prediction eﬃciency requires
m to be quite large. Pilanci and Wainwright (2015) shows that the solutions from sketched least
squares regressions have larger variance than the oracle solution that uses the full sample. Pilanci
and Wainwright (2015) provides a result that relates m to the rank of the matrix. Wang, Gittens
and Mahoney (2018) studies four sketching methods in the context of ridge regressions that nests
least squares as a special case. It is reported that sketching schemes with near optimal algorithmic
properties may have features that not statistically optimal. Chi and Ipsen (2018) decomposes the
variance of eβ into a model induced component and an algorithm induced component.
19


## Page 21


5
Statistical Properties of eβ
We consider the linear regression model with K regressors:
y = XT β + e,
ei ∼(0, Ωe)
where y is the dependent variable, X is the n × K matrix of regressors, β is the K × 1 vector of
regression coeﬃcients whose true value is β0. It should be noted that K is the number of predictors
which is generally larger than d, which is the number of covariates available since the predictors
may include transformation of the d covariates. In the Mincer example, we have data for edu, exp
collected into A with d = 2 columns. From these two covariates, K = 4 regressors are constructed
for regression (1a), while K = 14 regressors are constructed for regression (1b).
The full sample estimator using data (y, X) is ˆβ = (XT X)−1XT y. For a given Π, the estimator
using sketched data (ey, e
X) = (Πy, ΠX) is
eβ = ( e
XT e
X)−1 e
XT ey.
Assumption OLS:
(i) the regressors X are non-random, has svd X = UΣV T , and XT X is non-singular;
(ii) E[ei] = 0 and E[eeT ] = Ωe is a diagonal positive deﬁnite matrix.
Assumption PI:
(i) Π is independent of e;
(ii) for given singular value distortion parameter εσ ∈(0, 1), there exists failure parameter δσ ∈
(0, 1) such that P

|1 −σ2
k(ΠU)| ≤εσ for all k = 1, . . . K

≥1 −δσ.
(iii) ΠT Π is an n × n diagonal matrix and ΠΠT = n
mIm.
Assumption OLS is standard in regression analyses. The errors are allowed to be possibly het-
eroskedastic but not cross-correlated. Under Assumption OLS, ˆβ is unbiased, i.e. E[ˆβ] = β0 with
a sandwich variance
V(ˆβ) = (XT X)−1(XT ΩeX)(XT X)−1.
Assumption PI.(i) is needed for eβ to be unbiased.
Assumption PI.(ii) restricts attention to Π
matrices that have subspace embedding property. As previously noted, the condition is equivalent
20


## Page 22


to ∥Id −(ΠU)T (ΠU)∥2 ≤εσ holding with probability 1 −δσ. We use PI2 to refer Assumptions PI
(i) and (ii) holding jointly. Results under PI2 are not speciﬁc to any Π.
Assumption PI.(iii) simpliﬁes the expression for V(eβ|Π), the variance of eβ conditional on Π,
and we will use PI3 to denote Assumptions PI (i)-(iii) holding jointly. PI3 eﬀectively narrows the
analysis to uniform sampling and SRHT without replacement. We will focus on uniform sampling
without replacement for a number of reasons. It is simple to implement, and unlike the SRHT,
the rows have meaningful interpretation. In a regression context, uniform sampling has an added
advantage that there is no need to reconstruct (ey, e
X) each time we add or drop a variable in the
X matrix. In contrast, most other Πs require (ey, e
X) to be reconstructed. This can be cumbersome
when variable selection is part of the empirical exercise. Uniform sampling without replacement is
an exception since the columns are unaﬀected once the rows are randomly chosen.
For regressions, we need to know not only the error in approximating XT X, but also the error
in approximating (XT X)−1. This is made precise in the next Lemma.
Lemma 4 Suppose that PI2 is satisﬁed. For given non-random matrix X ∈Rn×K of full rank with
svd(X) = UΣV T , consider any non-zero K × 1 vector c. It holds with probability at least 1 −δσ
that

cT [(XT X)−1 −( e
XT e
X)−1]c
cT (XT X)−1c
 ≤
εσ
1 −εσ
.
The Lemma follows from the fact that
(XT X)−1
=
V Σ−2V T ≡PP T

(ΠX)T (ΠX)
−1
=
PQP T
where P = V Σ−1 and Q−1 = (ΠU)T (ΠU). By the property of Rayleigh quotient, the smallest
eigenvalue of (UT ΠT ΠU) is bounded below by (1 −εσ). Hence

cT (PQP T −PP T )c
cT PP T c

=

cT P(Id −Q−1)QP T c
cT PP T c
 ≤∥Q∥2∥Id −Q−1∥2 ≤
εσ
(1 −εσ).
The approximation error (XT X)−1 is thus larger than that for XT X, which equals εσ.
Under Assumptions OLS and PI3, eβ is unbiased and has sandwich variance
V(eβ|Π)
=
n
m( e
XT e
X)−1( e
XT Ωe e
X)−1( e
XT e
X)−1
since ΠΠT = n
mIm. The variance of eβ is inﬂated over that of ˆβ through the sketching error on the
‘bread’ ( e
XT e
X)−1, as well as on the ‘meat’ because XT ΩeX is now approximated by e
XT ΠΩeΠT e
X.
If e ∼(0, σ2
eIn) is homoskedastic, then eβ has variance
V(eβ|Π)
=
σ2
e
n
m( e
XT e
X)−1.
(9)
21


## Page 23


Though ˆβ is the best linear unbiased estimator under homoskedasticity, eβ may not be best in the
class of linear estimators using sketched data.
5.1
Eﬃciency of eβ Under Uniform Sampling
Suppose we are interested in predicting y at some x0. According to the model, E[y|x = x0] =
βT x0. Feasible predictions are obtained upon replacing β with ˆβ and eβ. Since both estimators are
unbiased, their respective variance is also the mean-squared prediction error.
Theorem 1 Suppose that ei ∼(0, σ2
e) and Assumptions OLS and PI3 hold. Let mse(xT
0 ˆβ) and
mse(xT
0 eβ|Π) be the mean-squared prediction error of y at x0 using ˆβ and eβ conditional on Π,
respectively. Then with probability at least 1 −δσ, it holds that
mse(xT
0 eβ|Π)
mse(xT
0 ˆβ)
≤
n
m
|{z}
sample size

1
1 −εσ

|
{z
}
sketching error
.
The prediction error has has two components: a sample size eﬀect given by n
m > 1, and a sketching
eﬀect given by
1
1−εσ > 1. The result arises because under homoskedasticity,
xT
0 ( e
XT e
X)−1x0 −xT
0 (XT X)−1x0 = n
mxT
0
h XT ΠT ΠX
−1 −(XT X)−1i
x0 + n −m
m
xT
0 (XT X)−1x0.
It follows that

xT
0 V(eβ|Π)x0 −xT
0 V(ˆβ)x0
xT
0 V(ˆβ)x0
 =

n
m
xT
0 [
 (ΠX)T ΠX
−1 −(XT X)−1]x0
xT
0 (XT X)−1x0
+ n −m
m

≤n
m
εσ
1 −εσ
+ n −m
m
.
We will subsequently be interested in the eﬀect of sketching for testing linear restrictions as given
by a K × 1 vector c. The estimated linear combination cT eβ has variance V(cT eβ|Π) = cT V(eβ|Π)c.
When c is a vector of zeros except in the k-th entry, var(cT eβ|Π) is the variance of eβk. When c is a
vector of ones, var(cT eβ|Π) is the variance of the sum of estimates. A straightforward generalization
of Theorem 1 leads to the following.
Corollary 1 Let c be a known K × 1 vector. Under the Assumptions of Theorem 1, it holds with
probability 1 −δσ that
cT V(eβ|Π)c
cT V(ˆβ)c
≤n
m

1
1 −εσ

.
The relative error is thus primarily determined by the relative sample size. As m is expected
to be much smaller than n, the eﬃciency loss is undeniable.
22


## Page 24


A lower bound in estimation error can be obtained for embedding matrices Φ ∈Rm×n satisfying
∥ΦU∥2
2 ≤1 + εσ. For a sketch size of m rows, deﬁne a class of OLS estimators as follows:
B(m, n, εσ) :=
n
˘β := ((XΦ)T ΦX)−1(XΦ)T Φy
o
.
For such ˘β, let V(˘β|Φ) denote its mse for given Φ. Assuming that ei ∼(0, σ2
e),
cT V(˘β|Φ)c
cT V(ˆβ)c
= m−1σ2
ecT ((ΦX)T ΦX)−1c
n−1σ2ecT (XT X)−1c
= n
m
cT ((ΦX)T ΦX)−1c
cT (XT X)−1c
= n
m
cT (V ΣUT ΦT ΦUΣV T )−1c
cT (V Σ2V T )−1c
= n
m
cT V Σ−1(UT ΦT ΦU)−1Σ−1V T c
cT V Σ−2V T c
≥n
mσmin[(UT ΦT ΦU)−1].
But by the deﬁnition of spectral norm, ∥ΦU∥2
2 = σ2max(ΦU) for any Φ. Thus the subspace embed-
ding condition ∥ΦU∥2
2 ≤1 + εσ implies σ2max(ΦU) = σmax((ΦU)T ΦU) ≤1 + εσ, and hence
σmin

(UT ΦT ΦU)−1

≥
1
1 + εσ
.
This leads to the following lower bound for ˘β:
cT V(˘β|Φ)c
cT V(ˆβ)c
≥n
m

1
1 + εσ

.
Combining the upper and lower bounds leads to the following:
Theorem 2 Under OLS and PI3, the estimator eβ with ei ∼(0, σ2
e) has mean-squared error relative
to the full sample estimator ˆβ bounded by
n
m

1
1 + εσ

≤cT V(eβ|Π)c
cT V(ˆβ)c
≤n
m
1
1 −εσ
.
These are the upper and lower bounds for uniform sampling when implemented by sampling
without replacement.
It is also of interest to know how heteroskedasticity aﬀects the sketching error. Let Ωe,ii denote
the ith diagonal element of Ωe. Under OLS and PI3, it holds with probability at least 1 −δσ that
mse(xT
0 eβ|Π)
mse(xT
0 ˆβ)
≤
maxi Ωe,ii
mini Ωe,ii
 n
m
 (1 + εσ)
(1 −εσ)2 .
Hence heteroskedasticity independently interacts with the structure of Π to inﬂate the mean-squared
prediction error. The upper and lower bound for V(cT eβ|Φ) are larger than under homoskedasticity
by a magnitude that depends on the extent of dispersion in Ωe,ii. A formal result is given in the
appendix.
23


## Page 25


5.2
Eﬃciency of eβ under Countsketch
Condition PI.(iii) puts restrictions on ΠT Π and holds for uniform sampling. But the condition does
not hold for the countsketch. In its place, we assume the following to obtain a diﬀerent embedding
result for the countsketch:
Assumption CS:
For given εΠ > 0 and for all U ∈Rn×K satisfying UT U = IK, there exists an
n × n matrix A(Ωe, m, n), which may depend on (Ωe, m, n), and a constant δΠ ∈(0, 1) such that
P

∥UT ΠT ΠΩeΠT ΠU −UT A(Ωe, m, n)U∥2 ≤n
mεΠ

≥1 −δΠ.
The conditions for Assumption CS are veriﬁed in Appendix B. The Assumption is enough to provide
a subspace embedding result for ΠT ΠΩeΠT Π because as shown in the Appendix, the following holds
for Countsketch,



UT ΠT ΠΩeΠT ΠU −n
mUT ΩeU



2
≤


UT ΠT ΠΩeΠT ΠU −UT A(Ωe, m, n)U


2 +



UT A(Ωe, m, n)U −n
mUT ΩeU



2
≤n
m
h
εΠ +



m
n A(Ωe, m, n) −Ωe



2
i
(10)
where
A(Ωe, m, n) = Ωe + 1
m

tr(Ωe)In −Ωe

.
Hence under OLS, PI2, and CS it holds with probability at least 1 −δΠ −δσ that
mse(xT
0 eβ|Π)
mse(xT
0 ˆβ)
≤
maxi Ωe,ii
mini Ωe,ii
 n
m

1
1 −εσ

1 + εΠ + ∥m
n A(Ωe, m, n) −Ωe∥2

(1 −εσ)
.
The prediction error of the countsketch depends on the quantity A(Ωe, m, n). But if Ωe = σ2
eIn,


m
n A(Ωe, m, n) −Ωe


2 = σ2
e(m−1
n ), which will be negligible if m/n = o(1). Hence to a ﬁrst approxi-
mation, Theorem 1 also holds under the countsketch. This result is of interest since the countsketch
is computationally inexpensive.
5.3
Hypothesis Testing
The statistical implications of sketching in a regression setting have primarily focused on properties
of the point estimates. The implications for inference are largely unknown. We analyze the problem
from view point of hypothesis testing.
Consider the goal of testing q linear restrictions formulated as H0 : Rβ = r where R is a q × K
matrix of restrictions with no unknowns. In this subsection, we further assume that ei ∼N(0, σ2
e).
24


## Page 26


Under normality, the F test is exact and has the property that at the true value of β = β0,
Fn
=
R(ˆβ −β0)T

ˆV(R ˆβ)
−1
R(ˆβ −β0) ∼Fq,n−d.
Under the null hypothesis that β0 is the true value of β, Fn has a Fisher distribution with q and
n −d degrees of freedom. The power of a test given a data of size n against a ﬁxed alternative
β1 ̸= β0 depends on V(ˆβ) only through non-centrality parameter φn,13 deﬁned in Wallace (1972) as
φn = (Rβ0 −r)T V(R ˆβ)−1(Rβ −r)
2
.
The non-centrality parameter is increasing in |Rβ0 −r| and the sample size through the variance,
but decreasing in σ2
e. In the case of one restriction (q = 1),
φn = (Rβ0 −r)2
V(R ˆβ)
> (Rβ0 −r)2
V(Reβ|Π)
= φm.
This leads to the relative non-centrality
φn
φm
= V(Reβ|Π)
V(R ˆβ)
≤n
m
1
(1 −εφ).
which also has a sample size eﬀect and an eﬀect due to sketching error. The eﬀective size of the
subsample from the viewpoint of power can be thought of as m(1 −εφ).
A loss in power is to be expected when eβ is used. But by how much? Insights can be performed
from some back of the envelope calculations. Recall that if U and V are independent χ2 variables
with ν1 and ν2 degrees of freedom, V is central and U has non-centrality parameter φ,
E[F] = E
(U/ν1)
(V/ν2)

= ν2(ν1 + φn)
ν1(ν2 −2) .
In the full sample case, ν1 = q and ν2 = n −d and hence
E[Fn]
≈
(n −d)(q + φn)
q(n −d −2)
.
For the subsampled estimator, ν1 = q and ν2 = m −d, giving
E[Fm|Π]
≈
(m −d)(q + φm)
q(m −d −2)
.
While q and φm aﬀect absolute power, the relative power of testing a hypothesis against a ﬁxed
alternative is mainly driven by the relative sample size, m
n . However, the power loss from using
eβ to test hypothesis can be made negligible because in a big data setting, we have the luxury of
allowing m to be as large as we wish, irrespective of q. We will return to the choice of m.
13The deﬁnition of non-centrality is not universal, sometimes the factor of two is omitted. See, for example, Cramer
(1987) and Rudd (2000).
25


## Page 27


6
Econometrically Motivated Reﬁnements
As more and more data are being collected, sketching continues to be an active area of research.
For any sketching scheme, a solution of higher accuracy can be obtained by iteration. The idea
is to approximate the deviation from an initial estimate ∆= ˆβ −eβ(1) by solving, for example,
ˆ∆(1) = argmin∆∥y −(X(eβ(1) + ∆)∥2
2 and update eβ(2) = eβ(1) + ˆ∆(1).
Pilanci and Wainwright
(2016) starts with the observation that since the least squares objective function is ∥y −Xβ∥2
2 =
∥y∥2
2 + ∥Xβ∥2
2 −2yT Xβ, it is possible to sketch the quadratic term ∥Xβ∥2
2 but not the linear term
yT Xβ. The result is a Hessian sketch of β, deﬁned as ((ΠX)T (ΠX))−1XT y. Wang et al. (2017)
suggests that this can be seen as a type of Newton updating with the true Hessian replaced by the
sketched Hessian, and the iterative Hessian sketch is also a form of iterative random projection.
In the rest of this section, we consider statistically motivated ways to improve upon eβ. Subsec-
tion 6.1 considers pooling estimates from multiple sketches. Subsection 6.2 suggests an m that is
motivated by hypothesis testing.
6.1
Combining Sketches
The main result of the previous section is that the least squares estimates using sketched data has
two errors, one due to a smaller sample size, and one due to sketching. The eﬃciency loss is hardly
surprising, and there are diﬀerent ways to improve upon it. Dhillon et al. (2013) proposes a two-
stage algorithm that uses m rows of (y, X) to obtain an initial estimate of ΣXX and ΣXy. In the
second stage, the remaining rows are used to estimate the bias of the ﬁrst stage estimator. The ﬁnal
estimate is a weighted average of the two estimates. An error bound of O(
√
K
√n ) is obtained. This
bound is independent of the amount of subsampling provided m > O(
p
K/n). Chen et al. (2016)
suggests to choose sample indices from an importance sampling distribution that is proportional
to a sampling score computed from the data. They show that the optimal pi depends on whether
minimizing mean-squared error of eβ or of X eβ is the goal, though E[e2
i ] plays a role in both objectives.
The sample size eﬀect is to be expected, and is the cost we pay for not being able to use the
full data. But if it is computationally simple to create a sample of size m, the possibility arises
that we can better exploit information in the data without hitting the computation bottleneck by
generating many subsamples and subsequently pool estimates constructed from the subsamples.
Breiman (1999) explored an idea known as pasting bites that, when applied to regressions, would
repeatedly form training samples of size m by random sampling from the original data, then make
prediction by ﬁtting the model to the training data. The ﬁnal prediction is the average of the
predictions. Similar ideas are considered in Chawla et al. (2004) and Christmann et al. (2007). Also
related is distributed computing which takes advantage of many nodes in the computing cluster.
26


## Page 28


Typically, each machine only sees a subsample of the full data and the parameter of interest is
updated. Heince et al. (2016) studies a situation when the data are distrubuted across workers
according to features of X rather than the sample and show that their dual loco algorithm has
bounded approximation error that depends only weakly on the number of workers.
Consider eβ1, . . . , eβJ computed from J subsamples each of size K. As mentioned above, uniform
sampling with too few rows is potentially vulnerable to omitting inﬂuential observations. Comput-
ing multiple sketches also provides the user with an opportunity to check the rank across sketches.
Let etj =
eβj−β0
se(eβj) be the t test from sketch j. For a given m, we consider sampling without replacement
and J is then at most n/m. Deﬁne the average quantities
¯β = 1
J
J
X
j=1
eβj,
se(¯β) =
v
u
u
t
1
J(J −1)
J
X
j=1
h
se(eβj)
i2
,
¯t2 = 1
J
J
X
j=1
etj,
se(¯t2) =
v
u
u
t
1
J −1
J
X
j=1
 etj −¯t2
2.
Strictly speaking, pooling requires that subsamples are non-overlapping and observations are in-
dependent across diﬀerent subsamples. Assuming independence across j, the pooled estimator ¯β
has var(¯β) =
1
J2
PJ
j=1 var(eβj). Thus, se(¯β) ≈
r
1
J2
PJ
j=1
h
se(eβj)
i2
≥
1
√
J
h
1
J
PJ
j=1 se(eβj)
i
because
of Jansen’s inequality. Our estimator for the standard error ¯β uses J −1 in the denominator to
allow for a correction when J is relatively small.
Consider two pooled t statistics:
¯T1
=
¯β −β0
se(¯β)
(11a)
¯T2
=
√
J
¯t2
se(¯t2).
(11b)
Critical values from the standard normal distribution can be used for ¯T1. For example, for the
5%-level test, we reject H0 if | ¯T1| > 1.96. For ¯T2, we recommend using critical values from the
t distribution with J −1 degrees of freedom. For example, for the 5%-level test, we reject H0 if
| ¯T2| > 2.776 for J = 5.
Assumption PI-Avg:
(i) (Π1, . . . , ΠJ) is independent of e;
(ii) for all j, k such that j ̸= k, ΠjΠT
j = n
mIm and ΠjΠT
k = Om where Om is an m × m matrix of
zeros.
27


## Page 29


(iii) for given singular value distortion parameter εσ ∈(0, 1), there exists failure parameter δσ ∈
(0, 1) such that P

|1 −σ2
k(ΠjU)| ≤εσ for all k = 1, . . . K and for all j = 1, . . . , J

≥1 −δσ.
Condition (ii) is crucial; it is satisﬁed, for example, if Π1, . . . , ΠJ are non-overlapping subsamples
and each of them is sampled uniformly without replacement. Assumptions OLS and PI-Avg (i)
and (ii) along with the homoskedastic error assumption ensure that
cT V(¯β|Π1, . . . , ΠJ)c = σ2
e
n
mJ2
J
X
j=1
cT  XT ΠT
j ΠjX
−1c.
Condition (iii) is equivalent to the statement that 1 −εσ ≤σk(UT ΠT
j ΠjU) ≤1 + εσ
∀k =
1, . . . , K, ∀j = 1, . . . , J.
Theorem 3 Consider J independent sketches obtained by uniform sampling. Suppose that ei ∼
(0, σ2
e), Assumptions OLS and PI-Avg hold. Then with probability at leat 1 −δσ, the mean squared
error of cT ¯β conditional on (Π1, . . . , ΠJ) satisiﬁes
cT V(˘β|Π1, . . . , ΠJ)c
cT V(ˆβ)c
≤
n
mJ
1
(1 −εσ).
The signiﬁcance of the Theorem is that by choice of m and J, the pooled estimator can be almost
as eﬃcient as the full sample estimator. If we set J = 1, the theorem reduces to Theorem 1.
We use a small Monte Carlo experiment to assess the eﬀectiveness of combining statistics com-
puted from diﬀerent sketches. The data are generated as y = Xβ+e where e is normally distributed,
and X is drawn from a non-normal distribution. In matlab, we have X=pearsrnd(0,1,1,5,n,K).
With n = 1e6, we consider diﬀerent values of m and J. Most of our results above were derived for
uniform sampling, so it is also of interest to evaluate the properties of the eβ using data sketched
by Πs that do not satisfy PI.(iii). Four sketching schemes are considered: uniform sampling with-
out replacement labeled as rs1, srht, the countsketch labeled cs, and leverage score sampling,
labeled lev. It should be mentioned that results for shrt and lev took signiﬁcantly longer time
to compute than rs1 and cs.
The top panel of Table 2 reports results for ˆβ3 when K = 3. All sampling schemes precisely
estimate β3 whose true value is one. The standard error is larger the smaller is m, which is the
sample size eﬀect. But averaging eβj over j reduces variability. The lev is slightly more eﬃcient.
The size of the t test for β3 = 1.0 is accurate, and the power of the test against β3 < 1 when
β3 = 0.98 is increasing in the amount of total information used. Combining J sketches of size m
generally gives a more powerful test than a test based on a sketch size of mJ. The bottom panel of
Table 2 reports for K = 9, focusing on uniform sampling without replacement and the countsketch.
28


## Page 30


The results are similar to those for K = 3. The main point to highlight is that while there is a
sample size eﬀect from sketching, it can be alleviated by pooling across sketches.
6.2
The Choice of m
The JL Lemma shows that m = O(log dϵ−2) rows are needed for d vectors from Rn to be embedded
into an m dimensional subspace. A rough and ready guide for embedding a d dimensional subspace
is m = Ω(d log dϵ−2). This is indeed the generic condition given in, for example, Sarlos (2006),
though more can be said for certain Πs.14 Notably, these desired m for random projections depend
only on d but not on n.
As shown in Boutidis and Gittens (2013, Lemma 4.3), subspace embedding by uniform sampling
without replacement requires that
m ≥6ε−2
σ nℓmax log(2J · K/δσ).
(12)
where ℓmax = maxiℓi is the maximum leverage score, also known as coherence. When coherence
is large, the information in the data is not well spread out, and more rows are required for uniform
sampling to provide subspace embedding.
Hence unlike random projections, the desired m for
uniform sampling is not data oblivious.
But while this choice of m is algorithmically desirable, statistical analysis often cares about
the variability of the estimates in repeated sampling, and a larger m is always desirable for V(eβ).
The question arises as to whether m can be designed to take both algorithmic and statistical
considerations into account. We suggest two ways to ﬁne-tune the algorithmic condition. Now
ℓi = ∥U(i)∥2 = XT
(i)(XT X)−1X(i) = 1
nXT
(i)S−1
X X(i)
≤σ1(S−1
X ) 1
n∥X(i)∥2
2 = σ−1
K (SX) 1
n∥X(i)∥2
2.
where σK(SX) is the minimum eigenvalue of SX = n−1XT X, XT
(i) denotes the i-th row of X, and
X(i,j) the (i, j) element of X. But


X(i)


2
2 =
K
X
j=1

X(i,j)
2 ≤K · maxj=1,...,K

X(i,j)
2 = K · X2max,
where Xmax = maxi=1,...,nmaxj=1,...,d
X(i,j)
. This implies n·ℓmax ≤σ−1
K (SX)·K·X2max. Recalling
that pi =
ℓi
K deﬁnes the importance sampling distribution, we can now restate the algorithmic
condition for m when J = 1 as
m = Ω

nK log(K) · pmax

where
pmax ≤σ−1
K (SX)X2max
n
.
(13)
14The result for SRHT is proved in Lemma 4.1 of Boutidis and Gittens (2013). The result for count sketch is from
Theorem 2 of Nelson and Nguyen (2013a).
29


## Page 31


It remains to relate Xmax with quantities of statistical interest.
Assumption M:
a. σK(SX) is bounded below by cX with probability approaching one as n →∞;
b. E[|X(i,j)|r] ≤CX for some CX and some r ≥2.
Condition (a) is a standard identiﬁcation condition for SX to be positive deﬁnite so that it will
converge in probability to E
h
X(i)XT
(i)
i
. Condition (b) requires the existence of r moments so as to
bound extreme values.15 If the condition holds,
Xmax = op((nK)1/r).
Proposition 1 Suppose that Assumption M holds. A deterministic rule for sketched linear regres-
sions by uniform sampling is



m1
= Ω

(nK)1+2/r log K/n

if
r < ∞
m1
= Ω(K log(nK))
if
E[exp(tX(i,j))] ≤CX
holds additionally.
Proposition 1 can be understood as follows. Suppose that r = 6 moments are known to exist.
Proposition 1 suggests a sketch of m1 = Ω(log K(nK)4/3/n) rows which will generally be larger
than Ω(K log K), which is the sketch size suggested for data with thin tails. For such data, the
moment generating function is uniformly bounded and E[exp(tX(i,j))] ≤CX for some constant CX
and some t > 0 so that Xmax = op(log(nK)). In both cases, the desired m increases with the row
sample size n, the number of regressors K, as well as n · K, which is the number of data points
in the regressor matrix X. This contrasts with the algorithmic condition for m which does not
depend on n.
To use Proposition 1, we can either (i) ﬁx r to determine m1 or (ii) target ‘observations-per-
regressor ratio’. As an example, suppose n = 1e7 and K = 10. If r = 6, Proposition 1 suggests to
sample m1 = 10, 687 rows, implying m1
K ≈1000. If instead we ﬁx m
K at 100 and uniformly sample
m1 = 1000 rows, we must be ready to defend the existence of r =
2 log(nK)
log( m
K )−log(log K) ≈10 moments.
There is a clear trade-oﬀbetween m1 and r.
Though m1 depends on n, it is still a deterministic rule. To obtain a rule that is data dependent,
consider again cT eβ, where c is a K × 1 vector, and assume that ei ∼N(0, σ2) so that var(eβ) =
n
mσ2
e( e
XT e
X)−1 where β0 is the true (unknown) value of β. Deﬁne
τ0(m) = cT (eβ −β0)
se(cT eβ)
= cT (eβ −β0) + cT (β0 −β0)
se(cT eβ)
.
15Similar conditions are used to obtain results for the hat matrix. See, for example, Section 6.23 of Hansen (2019)’s
online textbook.
30


## Page 32


It holds that Pβ0(τ0 > z|Π, X1, . . . , Xn) = Φ(−z) for some z, where Φ(·) is the cdf of the standard
normal distribution. Now consider a one-sided test τ1 based on eβ against an alternative, say, β0.
The test τ1 is related to τ0 by
τ1(m) = cT (eβ −β0)
se(cT eβ)
−cT (β0 −β0)
se(cT eβ)
= τ0(m) + τ2(m).
The power of τ1 at nominal size α is then
Pβ0(τ0 + τ2 > Φ−1
(1−α)|Π, X1, . . . , Xn) = Φ

−Φ−1
(1−α) + τ2

≡γ.
Deﬁne
S(α, γ) = Φ−1
γ
+ Φ−1
1−α.
Common values of α and γ give the following:
Selected values of S(α, γ)
γ
α
0.500
0.600
0.700
0.800
0.900
0.010
2.326
2.580
2.851
3.168
3.608
0.050
1.645
1.898
2.169
2.486
2.926
0.100
1.282
1.535
1.806
2.123
2.563
Proposition 2 Suppose that ei ∼N(0, σ2
e) and the Assumptions of Theorem 1 hold. Let ¯γ be the
target power of a one-sided test τ1 and ¯α be the nominal size of the test.
• Let eβ be obtained from a sketch of size m1. For a given eﬀect size of β0−β0, a data dependent
‘inference conscious’ sketch size is
m2(m1) = S2(¯α, ¯γ) m1var(cT eβ)
[cT (β0 −β0)]2 = m1
S2(¯α, ¯γ)
τ 2
2 (m1) .
(14)
• For a pre- speciﬁed τ2(∞), a data oblivious ‘inference conscious’ sketch size is
m3 = nS2(¯α, ¯γ)
τ 2
2 (∞) .
(15)
Inference considerations suggests to adjust m1 by a factor that depends on S(¯α, ¯γ) and τ2. For
instance, when ¯γ ≥0.8 and/or ¯α ≤0.01, m1 will be adjusted upwards when the τ2 is less than two.
The precise adjustment depends on the choice of τ2.
The proposed m2 in Part (i) requires an estimate of var(cT eβ) from a preliminary sketch. Table
3 provides an illustration for one draw of simulated data with n = 1e7 and K = 10. We consider
three values of σe, ¯γ, as well as diﬀerent eﬀect size β0
1 −β10. Assuming r = 10 and σe = 0.5, an eﬀect
31


## Page 33


size of 0.025 gives an m1 of roughly 1000. Using a sketch of this size to obtain an estimate of τ2
will almost hit the target power of 0.5. However, a target power of 0.9 would require m2 = 3, 759,
almost four times as many rows as a target power of 0.5. The larger is σe, the less precise is eβ for
a given m, and more rows are needed. It is then up to the user how to trade of computation cost
and power of the test.
The proposed m3 in Part (ii) is motivatead by the fact that setting m1 to n gives m2(n) =
n S2(¯α,¯γ)
τ 2
2 (n) . Though computation of τ2(n) is infeasible, τ2(n) is asymptotically normal as n →∞.
Now if the full sample t-statistic cannot reject the null hypothesis, a test based on sketched data
will unlikely reject the null hypothesis. But when full sample t statistic is expected to be relatively
large (say, 5), the result can be used in conjunction with S(¯α, ¯γ) to give m3. Say if S(¯α, ¯γ) is 2,
m3 = (2/5)2n. This allows us to gauge the sample size eﬀect since n
m =
τ 2
2 (∞)
S2(¯α,¯γ). Note that m3 only
requires the choice of ¯α, ¯γ, and τ2(∞) which, unlike m2, can be computed without a preliminary
sketch.
Though Propositions 1 and 2 were derived for uniform sampling, they can still be used for other
choice of Π. The one exception in which some caution is warranted is the countsketch. The rule
given for the countsketch in Nelson and Nguyen (2013a, Theorem 5) of m ≥ε−2K(K + 1)δ−1.
Though such an m is data oblivious, it is generally larger than the rule given by Boutidis and
Gittens (2013) for uniform sampling. The larger m required for countsketch can be seen as a cost
of specifying a sparse Π. Thus, one might want to ﬁrst use a small r to obtain a conservative m1
for the countsketch. One can then use Proposition 2 to obtain an ‘inference conscious’ guide.
To illustrate how to use m1, m2 and m3, we consider Belenzon et al. (2017) which studies ﬁrms’
performance from naming the company after its owners, a phenomenon known as eponymy. The
parameter of interest is α1 in a ‘return on assets’ regression
roait = α0 + α1eponymousit + ZT
itβ + ηi + τt + ci + ϵit.
The coeﬃcient gives the eﬀect of the eponymous dummy after controlling for time varying ﬁrm
speciﬁc variables Zit, SIC dummies ηi, country dummies ci, and year dummies τt.
The panel
of data includes 1.8 million companies from 2002-2012, but we only use data for one year. An
interesting aspect of this regression is that even in the full sample with n = 562160, some dummies
are sparse while others are collinear, giving an eﬀective number of K = 423 regressors. We will
focus on the four covariates: the indicator variable for being eponymous, the log of assets, the log
number of shareholders, and equity dispersion.
Given the values of (n, K) for this data, any assumed value of r less than 8 would give an m1
larger than n which is not sensible.16 This immediately restricts us to r ≥6. As point of reference,
16This is based on m1 = (nK)1+2/r log K/n. A smaller r is admissible if m1 = c1(nK)1+2/r log K/n for some
32


## Page 34


(r, m1) = (8, 317657) and (r, m1) = (15, 33476). The smallest m1 is obtained by assuming that the
data have thin tails, resulting in m1 = K log(nK) = 8158.
Table 4 presents the estimation results for several values of m. The top panel presents results
for uniform sampling. Note that more than 50 covariates for uniform sampling are omitted due
to colinearity, even with a relatively large sketch size.
The ﬁrst column shows the full sample
estimates for comparison. Column (2) shows that the point estimates given by the smallest sketch
with m1 = 8158 are not too diﬀerent from those in column (1), but the precision estimates are
much worse. To solve this problem, we compute m2(m1) by plugging in the t statistic for equity
dispersion (ie. ˆτ0 = 0.67) as τ2. This gives an m2 of 112358. A similar sketch size can be obtained
by assuming r = 10 for m1, or by plugging in τ2(∞) = 5 for m3. As seen from Table 4, the point
estimates of all sketches are similar, but the inference conscious sketches are larger in size and give
larger test statistics.
The bottom panel of Table 4 presents results for the countsketch. Compared to uniform sampling
in the top panel, only one or two covariates are now dropped. Though the estimate of α1 is almost
almost identical to the one for the full sample and for uniform sampling, the estimated coeﬃcient
for equity dispersion is somewhat diﬀerent. This might be due to the fact that uniform sampling
drops much more covariates than countsketch.
7
Concluding Remarks
This paper provides an gentle introduction to sketching and studies its implications for prediction
and inference using a linear model. Sample codes for constructing the sketches are avaialble in
matlab, R, and stata. Our main ﬁndings are as follows:
1. Sketches incur an approximation error that is small relative to the sample size eﬀect.
2. For speed and parallelization, it is best to use countsketch.
3. For simple implementation, it is best to use uniform sampling.
4. For improved estimates, it is best to average over multiple sketches.
5. Statistical analysis may require larger sketch size than what is algorithmically desirable. We
propose two inference conscious rules for the sketch size.
Sketching has also drawn attention of statisticians in recent years. Ahfock et al. (2017) pro-
vides an inferential framework to obtain distributional results for a large class of sketched estima-
tors. Geppert, Ickstadt, Munteanu, Quedenfeld and Sohler (2017) considers random projections in
constant 0 < c1 < 1. We limit our attention to c1 = 1.
33


## Page 35


Bayesian regressions and provides suﬃcient conditions for a Gaussian likelihood based on sketched
data to have an error of 1 + O(ϵ) in terms of L2 Wasserstein distance. In the design of experi-
ments literature, the goal is to reveal as much information as possible given a ﬁxed budget.17 Since
sketching is about forming random samples, it is natural to incorporate the principles in design of
experiments. Wang, Zhu and Ma (2018) considers the design of subsamples for logistic regressions.
A-optimality and practical considerations suggest to use pi =
|ˆei|∥xi∥
P
i |ˆei|∥xi∥, which may be understood
as score based sampling. Wang et al. (2019) considers the homoskedastic normal linear regression
model. The principle of D-optimality suggests to recursively selecting data according to extreme
values of covariances. The algorithm is suited for distributed storage and parallel computing.
Though analysis of the linear regression is an absolute ﬁrst step in understanding the use and
implications of sketching, the real beneﬁts are expected to be in estimation problems that are
complex. For example, Deaton and Ng (1998) uses ‘binning methods’ and uniform sampling to
speed up estimation of non-parametric average derivatives. Portnoy and Koenker (1997) uses a
fast interior point method for quantile regression by preprocessing a random subsample of data
to reduce the eﬀective sample size. More generally, if the full-sample Hessian matrix is diﬃcult
to estimate, one can consider an approximation of it by subsampling. This paper provides a new
perspective to evaluating the eﬀectiveness of matrix approximations and aims to better understand
their implications for inference.
While using sketches to overcome the computation burden is a step forward, sometimes we need
more than a basic sketch. We have been silent about how to deal with data that are dependent
over time or across space, such as due to network eﬀects. We may want our sketch to preserve,
say, the size distribution of ﬁrms in the original data.
The sampling algorithms considered in
this review must then satisfy additional conditions. When the data have a probabilistic structure,
having more data is not always desirable, Boivin and Ng (2006). While discipline-speciﬁc problems
require discipline-speciﬁc input, there is also a lot to learn from what has already been done in
other literatures. Cross-disciplinary work is a promising path towards eﬃcient handling of large
volumes of data.
17A criterion that uses the trace norm for ordering matrices is A-optimality. A criterion that uses the determinant
to order matrices is a D-optimal design.
34


## Page 36


Appendices
A
Proof of Lemma 3
Proof of Lemma 3
By an orthogonal decomposition of the least squares residuals,
∥y −X eβ∥2
2
=
∥y −X ˆβ∥2
2 + ∥X eβ −X ˆβ∥2
2
=
∥y −U ˆθ∥2
2 + ∥U(eθ −ˆθ)∥2
2
=
d
ssr2 + ∥U(eθ −ˆθ)∥
=
d
ssr2 + ∥eθ −ˆθ∥2,
(16)
where
∥eθ −ˆθ∥2
=
∥(ΠU)T ΠU(eθ −ˆθ) + (eθ −ˆθ) + (ΠU)T ΠU(ˆθ −eθ)∥2
≤
∥(ΠU)T ΠU(eθ −ˆθ)∥2 + ∥(ΠU)T ΠU(ˆθ −eθ) −(ˆθ −eθ)∥2
≤
∥(ΠU)T ΠU(eθ −ˆθ)∥2 + ∥(ΠU)T ΠU −Id∥2∥(eθ −ˆθ)∥2
≤
∥(ΠU)T (ΠU)(eθ −ˆθ)∥2 + 1
√
2∥eθ −ˆθ∥2
≤
√
2∥(ΠU)T ΠU(eθ −ˆθ)∥2
by triangle inequality, Cauchy-Schwarz inequality, condition (8a), and rearranging terms. Now the
normal equations implies (ΠU)T (ΠU)eθ = (ΠU)T Π(y −X eβ). Hence
∥eθ −ˆθ∥2
≤
√
2∥(ΠU)T Π(y −U ˆθ)∥2
≤
√ϵ0 d
ssr
by condition (8b) and for some failure probability δ0. It follows from (16) that g
ssr2 ≤(1 + ϵ2)d
ssr2
holds with probability 1 −δ2 where ϵ2 = ϵ2
0 and δ2 < 2δ0. This probability can be made higher
with suitable choice of ϵ0 and m, which can be controlled by the researcher.
Proof of Theorem 3
Note that
cT (¯β −β)
=
1
J
J
X
j=1
cT  XT ΠT
j ΠjX
−1 XT ΠT
j Πje

.
Thus,
E[cT (¯β −β)|Π1, . . . , ΠJ] = 1
J
J
X
j=1
cT  XT ΠT ΠX
−1 XT ΠT ΠE[e|Π1, . . . , ΠJ]

= 0.
35


## Page 37


Write
E[{cT (¯β −β)}2|Π1, . . . , ΠJ]
= 1
J2
J
X
j=1
J
X
k=1
cT  XT ΠT
j ΠjX
−1 XT ΠT
j ΠjE[eeT |Π1, . . . , ΠJ]ΠT
k ΠkX
 XT ΠT
k ΠkX
−1c
= σ2
e
1
J2
J
X
j=1
cT  XT ΠT
j ΠjX
−1 XT ΠT
j ΠjΠT
j ΠjX
 XT ΠT
j ΠjX
−1c
+ σ2
e
1
J2
J
X
j=1
J
X
k=1,k̸=J
cT  XT ΠT
j ΠjX
−1 XT ΠT
j ΠjΠT
k ΠkX
 XT ΠT
k ΠkX
−1c
= σ2
e
n
mJ2
J
X
j=1
cT  XT ΠT
j ΠjX
−1c.
Then, the desired result is obtained by arguments identical to those used in proving Theorem 1.
In particular, we can show that
n
m
cT  XT ΠT
j ΠjX
−1c
cT (XT X)−1c
≤n
m
1
(1 −εσ)
(17)
jointly for all j = 1, . . . , J with probability at least 1 −δσ. Q.E.D.
B
Veriﬁcation of Assumption CS for Countsketch
In this part of the appendix, we verify Assumption CS for the countsketch. Here, we use d to
denote the column dimension of Π.
Lemma 5 Let Π ∈Rn×d be a random matrix such that (i) the (i, j) element Πij of Π is Πij = δijσij,
where σij’s are i.i.d. ±1 random variables and δij is an indicator random variable for the event
Πij ̸= 0; (ii) Pm
i=1 δij = 1 for each j = 1, . . . , n; (iii) for any S ⊂[n], E (Πj∈Sδij) = m−|S|; (iv) the
columns of Π are i.i.d. Furthermore, there is a universal constant Ce such that maxi=1,...,nΩe,ii ≤Ce.
Suppose that
(d2 + 1)m
n
+ (d2 + d)
m
≤δΠε2
Π
8C2e
.
(18)
Let
A(Ωe, m, n) = Ωe + 1
m {tr(Ωe)In −Ωe} .
(19)
Then, we have that
P


UT ΠT ΠΩeΠT ΠU −UT A(Ωe, m, n)U


2 > n
mεΠ

≤δΠ.
36


## Page 38


This lemma states that Condition CS is satisﬁed for countsketch, provided that all the diagonal
elements of Ωe are bounded by a universal constant, d2m/n = o(δΠε2
Π) and d2/m = o(δΠε2
Π). The
rate conditions in (18) are not stringent. When n is very large, d is of a moderate size and δΠ and
εΠ are given, there is a range of m that satisﬁes (18).
Proof of Lemma 5
Since we assume that each diagonal element of Ωe is bounded by a universal
constant Ce,
tr(Ω2
e) ≤C2
en, tr(Ωe) = Cen, and ∥Ωe∥2 = Ce.
Then Lemma F.1, which is given in Appendix F, implies that
P
 

UT ΠT ΠΩeΠT ΠU −UT A(Ωe, m, n)U


2 > ϵ

≤2ϵ−2
2d2(m −1)
m2
tr(Ω2
e) + 2d2
m2 ∥Ωe∥2tr(Ωe) + d2
m3
n
[tr(Ωe)]2 + 2∥Ωe∥2
2
o
+ 2
mtr(Ω2
e) + 2
m2 tr(Ωe) + 1
m3
n
d [tr(Ωe)]2 + 2tr(Ω2
e)
o 
≤2ϵ−2
2d2(m −1)
m2
C2
en + 2d2
m2 C2
en + d2
m3

C2
en2 + 2C2
e
	
+ 2
mC2
en + 2
m2 Cen + 1
m3

dC2
en2 + 2C2
en
	 
≤8C2
eϵ−2
(d2 + 1)n
m
+ (d2 + d)n2
m3

.
If we take ϵ = n
mεΠ, then
P


UT ΠT ΠΩeΠT ΠU −UT A(Ωe, m, n)U


2 > n
mεΠ

≤8C2
eε−2
Π
(d2 + 1)m
n
+ (d2 + d)
m

.
To satisfy the probability above is bounded by δΠ, we need to assume that
8C2
eε−2
Π
(d2 + 1)m
n
+ (d2 + d)
m

≤δΠ,
which is imposed by (18). Q.E.D.
C
Proof of JL Lemma
The original proof assumes that Π is Gaussian.18
We highlight arguments for this case using
properties of sub-exponential random variables. For arbitrary (i, j), deﬁne u = (ai −aj) ∈Rn and
18Subsequent proofs by Dasgupta and Gupta (2003), Indyk and Motwani (1998), Matousek (2008) use diﬀerent
proof techniques to obtain tighter bounds. Fedoruk et al. (2018) summaries the evolution of the Lemma. Others
consider non-Gaussian Π matrices that are less costly to store.
37


## Page 39


v = Πai −Πaj =
1
√mΠu ∈Rm. Note that vi =
1
√m
P
j Πijuj ∼N(0, ||u||2
2
m ). The Lemma then says

||v||2
2
||u||2
2 −1
 ≤ϵ. The proof of this statement proceeds in three steps.
(i) show that the expected value of the Euclidean distance of the random projection is equal to
the Euclidean distance of the original subspace:
E[||v||2
2]
=
E[
m
X
i=1
v2
i ] =
m
X
i=1
E[v2
i ]
=
m
X
i=1
1
mE

(
X
j
Πijui)2

=
m
X
i=1
1
m
X
1≤j,k≤n
ujukΠijΠik
=
m
X
i=1
1
m
X
1≤j,k≤n
ujukδjk =
m
X
i=1
1
m
X
1≤j≤n
u2
j
=
X
j≤n
u2
j = ||u||2
2.
(ii) show that (i) holds with high probability. For this, let Zi = Πiu
||u||. Then Pm
i=1 Z2
i = m||v||2
2
||u||2
2
is
χ2
m, hence sub-exponential.19: A two-sided tail bound yields
P
 1
m

m
X
k=1
Z2
k −1
 ≥ϵ

= P

||v||2
2
||u||2
−1
 > ϵ

≤2e−mϵ2/8.
(iii) apply union bound: step (ii) holds for all d2 pairs of (i, j), so the overall failure probability
is at most 2
d
2

e−mϵ2/8. Given a error rate ϵ, this failure probability can be driven below δ
by making m ≥C
ϵ2 (log d/δ) for large enough C.
19A random variable X with mean µ is sub-exponential with parameters (ν, b) if E[eλ(X−µ)] ≤eν2λ2/2. If Zk ∼
N(0, 1), Z2
k ∼χ2
m is sub-exponential with (ν, b) = (2, 4) and has two-sided tail bound P

1
√m
Pm
k=1 Z2
k −1
 ≥ϵ

≤
2e−mϵ2/8,
ϵ ∈(0, 1). See, for example, Wainwright (2019, Chapter 2) or Vershynin (2017, lecture 1).
38


## Page 40


D
Streaming Implementation of Countsketch
CountSketch, Streaming:
Input: Given A ∈Rn×d and m < n
Output: eA ∈Rm×d, initialized to zero
1 for s = 1 : n do
2
sampled h (from [1, . . . m])
3
sample g from [+1, −1]
4
eA(h(s)) := eA(h(s)) + g × A(h(s))
The example considered in the main text is the same as C = ΠA, where n = 9,
Π
=


0
0
1
0
1
−1
0
0
1
−1
0
0
−1
0
0
0
−1
0
0
−1
0
0
0
0
1
0
0

and A =


A3 + A5 −A6 + A9
A1 −A4 −A8
A2 + A7

.
Hence if d = 4,
eA =


A31 + A51 −A61 + A91
A32 + A52 −A62 + A92
A33 + A53 −A63 + A93
A34 + A54 −A64 + A94
−A11 −A41 −A81
−A12 −A42 −A82
−A13 −A43 −A83
−A14 −A44 −A84
−A21 + A71
−A22 + A72
−A23 + A73
−A24 + A74

.
Consider now the streaming approach when the random draws of h and g are
h
g

=
 2
3
1
2
1
1
3
2
1
−1
−1
+1
−1
+1
−1
+1
−1
1

1. s = 1: A(1) =
 A11
A12
A13
A14

, h = 2, g = −1. Updating Ah(1) = A2 gives
eA
=


0
0
0
0
A11 × −1
A12 × −1
A13 × −1
A14 −1
0
0
0
0

.
2. s = 2: A(2) =
 A21
A22
A23
A24

, h = 3, g = −1. Updating Ah(2) = A3 gives
eA
=


0
0
0
0
−A11
−A12
−A13
−A14
A21 × −1
A22 × −1
A23 × −1
A24 × −1


3. s = 3: A(3) =
 A31
A32
A33
A34

, h = 1, g = 1. Updating Ah(3) = A1 gives
eA
=


A31
A32
A33
A34
−A11
−A12
−A13
−A14
−A21
−A22
−A23
−A24


4. s = 4: A(4) =
 A41
A42
A43
A44

, h = 2, g = −1. Updating Ah(4) = A2 gives
eA
=


A31 × 1
A32 × 1
A33 × 1
A34 × 1
−A11 + (A41 × −1)
−A12 + (A42 × −1)
−A13 + (A43 × −1)
−A14 + (A44 × −1)
−A21
−A22
−A23
−A24


39


## Page 41


5. s = 5: A(5) =
 A51
A52
A53
A54

, h = 1, g = 1. Updating Ah(5) = A1 gives
eA
=


A31 + A51
A32 + A52
A33 + A53
A34 + A54
−A11 −A41
−A12 −A42
−A13 −A43
−A14 −A44
A21 × −1
A22 × −1
A23 × −1
A24 × −1


6. s = 6: A(6) =
 A61
A62
A63
A64

, h = 1, g = −1. Updating Ah(6) = A1 gives
eA
=


A31 + A51 −A61
A32 + A52 −A62
A33 + A53 −A63
A34 + A54 −A64
−A11 −A41
−A12 −A42
−A13 −A43
−A14 −A44
A21 × −1
A22 × −1
A23 × −1
A24 × −1


7. s = 7: A(7) =
 A71
A72
A73
A74

, h = 3, g = 1. Updating Ah(7) = A3 gives
eA
=


A31 + A51 −A61
A32 + A52 −A62
A33 + A53 −A63
A34 + A54 −A64
−A11 −A41
−A12 −A42
−A13 −A43
−A14 −A44
−A21 + A71
−A22 + A72
−A23 + A73
−A24 + A74


8. s = 8: A(8) =
 A81
A82
A83
A84

, h = 2, g = −1. Updating Ah(8) = A2 gives
eA
=


A31 + A51 −A61
A32 + A52 −A62
A33 + A53 −A63
A34 + A54 −A64
−A11 −A41 −A81
−A12 −A42 −A82
−A13 −A43 −A83
−A14 −A44 −A84
−A21 + A71
−A22 + A72
−A23 + A73
−A24 + A74


9. s = 9: A(9) =
 A91
A92
A93
A94

, h = 1, g = 1. Updating Ah(9) = A1 gives
e
A
=


A31 + A51 −A61 + A91
A32 + A52 −A62 + A92
A33 + A53 −A63 + A93
A34 + A54 −A64 + A94
−A11 −A41 −A81
−A12 −A42 −A82
−A13 −A43 −A83
−A14 −A44 −A84
−A21 + A71
−A22 + A72
−A23 + A73
−A24 + A74

.
This is precisely ΠA.
40


## Page 42


E
General Version of Theorem 1
In this section, we give a general version of Theorem 1 under heteroskedasticity.
Theorem 4 Let c be a known K × 1 vector. Assume that ei ∼(0, Ωe,ii), where Ωe,ii denote the ith
diagonal element of Ωe. Under OLS and PI3, it holds with probability at least 1 −δσ that
mse(xT
0 eβ|Π)
mse(xT
0 ˆβ)
≤
maxi Ωe,ii
mini Ωe,ii
 n
m
 (1 + εσ)
(1 −εσ)2 .
Proof of Theorem 4
We have V(eβ|Π) = ( e
XT e
X)−1 e
XT ΠΩeΠT e
X( e
XT e
X)−1.
The quantity of
interest is
cT V(eβ|Π)c −n
mcT V(ˆβ)c
= cT A1B1A1c −cT A2B2A2c
= cT (A1 −A2)B1(A1 −A2)c + 2cT A2B1(A1 −A2)c + cT A2(B1 −B2)A2c,
where A1 =
 XT ΠT ΠX
−1, B1 = XT ΠT ΠΩeΠT ΠX, A2 =
 XT X
−1, and B2 =
n
m
 XT ΩeX

.
Write
cT V(eβ|Π)c −n
mcT V(ˆβ)c

≤
cT (A1 −A2)B2(A1 −A2)c
 +
cT (A1 −A2)(B1 −B2)(A1 −A2)c

+ 2
cT A2B2(A1 −A2)c
 + 2
cT A2(B1 −B2)(A1 −A2)c
 +
cT A2(B1 −B2)A2c
 .
Let
C(Ωe) = maxi Ωe,ii
mini Ωe,ii
.
We will bound each of the terms above by establishing the following lemma.
Lemma 6 The following statements hold with probability at least 1 −δσ :

cT A2B2(A1 −A2)c
cT V(ˆβ)c
 ≤n
mC(Ωe)1/2
εσ
(1 −εσ),
(20a)

cT (A1 −A2)B2(A1 −A2)c
cT V(ˆβ)c
 ≤n
mC(Ωe)
ε2
σ
(1 −εσ)2 ,
(20b)

cT (A1 −A2)(B1 −B2)(A1 −A2)c
cT V(ˆβ)c
 ≤n
mC(Ωe)
ε2
σ
(1 −εσ)2 εσ,
(20c)

cT A2(B1 −B2)(A1 −A2)c
cT V(ˆβ)c
 ≤n
mC(Ωe)1/2
εσ
(1 −εσ)εσ,
(20d)

cT A2(B1 −B2)A2c
cT V(ˆβ)c
 ≤n
mεσ.
(20e)
41


## Page 43


Proof of Lemma 6
To show part (20a), deﬁne W = (UT ΩeU)1/2Σ−1V T . Note that
V(ˆβ) = (XT X)−1(XT ΩeX)(XT X)−1
= V Σ−1UT ΩeUΣ−1V T
= W T W.
Write
A2B2(A1 −A2) = n
m
 XT X
−1 XT ΩeX
 h XT ΠT ΠX
−1 −
 XT X
−1i
= n
mV Σ−1UT ΩeU

(UT ΠT ΠU)−1 −In

Σ−1V T
= n
mV Σ−1UT ΩeU

(UT ΠT ΠU)−1 −In

(UT ΩeU)−1/2(UT ΩeU)1/2Σ−1V T
= n
mW T (UT ΩeU)1/2 
(UT ΠT ΠU)−1 −In

(UT ΩeU)−1/2W.
Then

cT A2B2(A1 −A2)c
cT V(ˆβ)c
 = n
m

cT W T (UT ΩeU)1/2 
(UT ΠT ΠU)−1 −In

(UT ΩeU)−1/2Wc
cT W T Wc

≤n
m



(UT ΩeU)1/2


2


(UT ΠT ΠU)−1 −In


2



(UT ΩeU)−1/2


2
≤n
mC(Ωe)1/2
εσ
(1 −εσ),
which proves part (20a).
For the second part, write
(A1 −A2)B2(A1 −A2)
= n
m
h XT ΠT ΠX
−1 −
 XT X
−1i  XT ΩeX
 h XT ΠT ΠX
−1 −
 XT X
−1i
= n
mV Σ−1 
(UT ΠT ΠU)−1 −In

UT ΩeU

(UT ΠT ΠU)−1 −In

Σ−1V T
= n
mW T (UT ΩeU)−1/2 
(UT ΠT ΠU)−1 −In

UT ΩeU

(UT ΠT ΠU)−1 −In

(UT ΩeU)−1/2W.
Thus,

cT (A1 −A2)B2(A1 −A2)c
cT V(ˆβ)c
 ≤n
mC(Ωe)
ε2
σ
(1 −εσ)2 ,
which proves part (20b).
42


## Page 44


For the third part, write
(A1 −A2)(B1 −B2)(A1 −A2)
= V Σ−1 
(UT ΠT ΠU)−1 −In
 h
UT Ω1/2
e
ΠT ΠΠT ΠΩ1/2
e
U −n
mUT Ω1/2
e
Ω1/2
e
U
i 
(UT ΠT ΠU)−1 −In

Σ−1V T
= W T (UT ΩeU)−1/2 
(UT ΠT ΠU)−1 −In

(UT ΩeU)1/2
× (UT ΩeU)−1/2 h
UT Ω1/2
e
ΠT ΠΠT ΠΩ1/2
e
U −n
mUT Ω1/2
e
Ω1/2
e
U
i
(UT ΩeU)−1/2
× (UT ΩeU)1/2 
(UT ΠT ΠU)−1 −In

(UT ΩeU)−1/2W.
Deﬁne Ue = Ω1/2
e
U(UT ΩeU)−1/2, so that
(UT ΩeU)−1/2 h
UT Ω1/2
e
ΠT ΠΠT ΠΩ1/2
e
U −n
mUT Ω1/2
e
Ω1/2
e
U
i
(UT ΩeU)−1/2
= UT
e ΠT ΠΠT ΠUe −n
mUT
e Ue.
Now observe that



UT
e ΠT ΠΠT ΠUe −n
mUT
e Ue



2
≤



UT
e ΠT ΠΠT ΠUe −n
mUT
e ΠT ΠUe



2 + n
m


UT
e ΠT ΠUe −UT
e Ue


2
≤n
mεσ.
(21)
Thus,

cT (A1 −A2)(B1 −B2)(A1 −A2)c
cT V(ˆβ)c
 ≤C(Ωe)
ε2
σ
(1 −εσ)2
n
mεσ,
which proves part (20c).
Similarly,
A2(B1 −B2)(A1 −A2)
= V Σ−1 h
UT Ω1/2
e
ΠT ΠΠT ΠΩ1/2
e
U −n
mUT Ω1/2
e
Ω1/2
e
U
i 
(UT ΠT ΠU)−1 −In

Σ−1V T .
Then

cT A2(B1 −B2)(A1 −A2)c
cT V(ˆβ)c
 ≤C(Ωe)1/2
εσ
(1 −εσ)
n
mεσ,
which proves part (20d).
Finally,
A2(B1 −B2)A2 = V Σ−1 h
UT Ω1/2
e
ΠT ΠΠT ΠΩ1/2
e
U −n
mUT Ω1/2
e
Ω1/2
e
U
i
Σ−1V T .
43


## Page 45


Therefore,

cT A2(B1 −B2)A2c
cT V(ˆβ)c
 ≤n
mεσ,
which proves part (20e).
Q.E.D.
We now return to the proof of the theorem. Applying (20a)-(20e) and simplifying,

cT V(eβ|Π)c −n
mcT V(ˆβ)c
cT V(ˆβ)c
 ≤C(Ωe) n
m
εσ(2 −εσ)
(1 −εσ)2 (1 + εσ) + εσ


cT V(eβ|Π)c −cT V(ˆβ)c
cT V(ˆβ)c
 ≤C(Ωe) n
m
εσ(2 −εσ)
(1 −εσ)2 (1 + εσ) + εσ)

+ n −m
m
with probability at least 1 −δσ −δΠ. This in turn implies that with the same probability,
cT V(eβ|Π)c
cT V(ˆβ)c
≤C(Ωe) n
m
(1 + εσ)
(1 −εσ)2 .
Q.E.D.
44


## Page 46


F
Subspace embedding for ΠT ΠΨΠT Π
In this appendix, we consider ΠT ΠΨΠT Π for a diagonal matrix Ψ in the case of countsketch.
Lemma 7 Let Π ∈Rn×d be a random matrix such that (i) the (i, j) element Πij of Π is Πij = δijσij,
where σij’s are i.i.d. ±1 random variables and δij is an indicator random variable for the event
Πij ̸= 0; (ii) Pm
i=1 δij = 1 for each j = 1, . . . , n; (iii) for any S ⊂[n], E (Πj∈Sδij) = m−|S|; (iv) the
columns of Π are i.i.d. Choose
A(Ψ, m, n) = Ψ + 1
m {tr(Ψ)In −Ψ} .
(22)
Then
P
 

UT ΠT ΠΨΠT ΠU −UT A(Ψ, m, n)U


2 > ϵ

≤2ϵ−2
2d2(m −1)
m2
tr(Ψ2) + 2d2
m2 ∥Ψ∥2tr(Ψ) + d2
m3
n
[tr(Ψ)]2 + 2∥Ψ∥2
2
o
+ 2
mtr(Ψ2) + 2
m2 tr(Ψ) + 1
m3
n
d [tr(Ψ)]2 + 2tr(Ψ2)
o 
.
Proof of Lemma 7
To show the desired result, we follow Nelson and Nguyen (2013). That is,
we start with the following moment inequality:
P
 

UT ΠT ΠΨΠT ΠU −UT A(Ψ, m, n)U


2 > ϵ

≤ϵ−2E
h

UT ΠT ΠΨΠT ΠU −UT A(Ψ, m, n)U


2
F
i
.
For countsketch, we have one non-zero entry for each column. This implies that ΠΨΠT is a
diagonal matrix. Hence,
[ΠΨΠT ]ii =
n
X
k=1
ΨkkΠ2
ik =
n
X
k=1
Ψkkδik.
Now
[ΠT ΠΨΠT Π]ℓℓ′ =
m
X
i=1
n
X
k=1
ΠiℓΨkkδikΠiℓ′ =
m
X
i=1
n
X
k=1
Ψkkδikδiℓδiℓ′σiℓσiℓ′,
where the last equality comes from the fact that Πij = δijσij. Then
[UT ΠT ΠΨΠT ΠU]uv =
n
X
ℓ=1
n
X
ℓ′=1
[ΠT ΠΨΠT Π]ℓℓ′UℓuUℓ′v
=
n
X
ℓ=1
n
X
ℓ′=1
m
X
i=1
n
X
k=1
Ψkkδikδiℓδiℓ′σiℓσiℓ′UℓuUℓ′v.
45


## Page 47


Write
[UT ΠT ΠΨΠT ΠU]uv =
n
X
ℓ=1
m
X
i=1
n
X
k=1
ΨkkδikδiℓUℓuUℓv
+
n
X
ℓ=1
n
X
ℓ′=1,ℓ′̸=ℓ
m
X
i=1
n
X
k=1
Ψkkδikδiℓδiℓ′σiℓσiℓ′UℓuUℓ′v
=
n
X
ℓ=1
m
X
i=1
ΨℓℓδiℓUℓuUℓv
+
n
X
ℓ=1
m
X
i=1
n
X
k=1,k̸=ℓ
ΨkkδikδiℓUℓuUℓv
+
n
X
ℓ=1
n
X
ℓ′=1,ℓ′̸=ℓ
m
X
i=1
n
X
k=1
Ψkkδikδiℓδiℓ′σiℓσiℓ′UℓuUℓ′v
=
n
X
ℓ=1
ΨℓℓUℓuUℓv
+
n
X
ℓ=1
m
X
i=1
n
X
k=1,k̸=ℓ
ΨkkδikδiℓUℓuUℓv
+
n
X
ℓ=1
n
X
ℓ′=1,ℓ′̸=ℓ
m
X
i=1
n
X
k=1
Ψkkδikδiℓδiℓ′σiℓσiℓ′UℓuUℓ′v
since Pm
i=1 δiℓ= 1 for each ℓ. Recall that we have assumed that for any S ⊂[n], E (Πj∈Sδij) =
m−|S|. Then, note that
E


n
X
ℓ=1
m
X
i=1
n
X
k=1,k̸=ℓ
ΨkkδikδiℓUℓuUℓv


=
n
X
ℓ=1
m
X
i=1
n
X
k=1,k̸=ℓ
ΨkkE (δikδiℓ) UℓuUℓv
= 1
m
n
X
ℓ=1
n
X
k=1,k̸=ℓ
ΨkkUℓuUℓv
= 1
m
n
X
ℓ=1
" n
X
k=1
Ψkk −Ψℓℓ
#
UℓuUℓv
= tr(Ψ)
m
1(u = v) −m−1
n
X
ℓ=1
ΨℓℓUℓuUℓv.
Since
n
X
k=1
ΨkkUkuUkv = [UT ΨU]uv,
46


## Page 48


UT ΠT ΠΨΠT ΠU should center on
tr(Ψ)
m
UT U +

1 −1
m

UT ΨU = UT

Ψ + 1
m {tr(Ψ)In −Ψ}

U.
If Ψ = σ2
eIn, then its form is
σ2
e
n
mUT U + σ2
e

1 −1
m

UT U = σ2
e
n + m −1
m

UT U.
Now

UT ΠT ΠΨΠT ΠU −UT

Ψ + 1
m {tr(Ψ)In −Ψ}

U

uv
=
n
X
ℓ=1
n
X
k=1,k̸=ℓ
Ψkk
" m
X
i=1
δikδiℓ−1
m
#
UℓuUℓv
+
n
X
ℓ=1
n
X
ℓ′=1,ℓ′̸=ℓ
n
X
k=1
Ψkk
" m
X
i=1
δikδiℓδiℓ′σiℓσiℓ′
#
UℓuUℓ′v
=: T1,uv + T2,uv.
First consider T1,uv. Deﬁne
km(k, ℓ) :=
m
X
i=1
δikδiℓ−1
m.
Write
km(k, ℓ)km(k′, ℓ′)
=
m
X
i=1
δikδiℓδik′δiℓ′ +
m
X
i=1
m
X
i′=1,i′̸=i
δikδiℓδi′k′δi′ℓ′ −1
m
m
X
i=1
δikδiℓ−1
m
m
X
i′=1
δi′k′δi′ℓ′ + 1
m2 .
Then for any ℓ̸= k and ℓ′ ̸= k′,
m
X
i=1
δikδiℓδik′δiℓ′ =







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







Pm
i=1 δikδiℓ
if ℓ= ℓ′, k = k′
Pm
i=1 δikδiℓδik′
if ℓ= ℓ′, k ̸= k′
Pm
i=1 δikδiℓδiℓ′
if ℓ̸= ℓ′, k = k′
Pm
i=1 δikδiℓ
if ℓ̸= ℓ′, k ̸= k′, k = ℓ′, ℓ= k′
Pm
i=1 δikδiℓδik′
if ℓ̸= ℓ′, k ̸= k′, k = ℓ′, ℓ̸= k′
Pm
i=1 δikδiℓδiℓ′
if ℓ̸= ℓ′, k ̸= k′, k ̸= ℓ′, ℓ= k′
Pm
i=1 δikδiℓδik′δiℓ′
if ℓ̸= ℓ′, k ̸= k′, k ̸= ℓ′, ℓ̸= k′.
47


## Page 49


Then
E
 m
X
i=1
δikδiℓδik′δiℓ′
!
=







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







m−1
if ℓ= ℓ′, k = k′
m−2
if ℓ= ℓ′, k ̸= k′
m−2
if ℓ̸= ℓ′, k = k′
m−1
if ℓ̸= ℓ′, k ̸= k′, k = ℓ′, ℓ= k′
m−2
if ℓ̸= ℓ′, k ̸= k′, k = ℓ′, ℓ̸= k′
m−2
if ℓ̸= ℓ′, k ̸= k′, k ̸= ℓ′, ℓ= k′
m−3
if ℓ̸= ℓ′, k ̸= k′, k ̸= ℓ′, ℓ̸= k′.
In addition, since there is one non-zero entry for each column in count sketch,
m
X
i=1
m
X
i′=1,i′̸=i
δikδiℓδi′k′δi′ℓ′ =







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







0
if ℓ= ℓ′, k = k′
0
if ℓ= ℓ′, k ̸= k′
0
if ℓ̸= ℓ′, k = k′
0
if ℓ̸= ℓ′, k ̸= k′, k = ℓ′, ℓ= k′
0
if ℓ̸= ℓ′, k ̸= k′, k = ℓ′, ℓ̸= k′
0
if ℓ̸= ℓ′, k ̸= k′, k ̸= ℓ′, ℓ= k′
Pm
i=1
Pm
i′=1,i′̸=i δikδiℓδi′k′δi′ℓ′
if ℓ̸= ℓ′, k ̸= k′, k ̸= ℓ′, ℓ̸= k′.
Hence,
E


m
X
i=1
m
X
i′=1,i′̸=i
δikδiℓδi′k′δi′ℓ′

=







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







0
if ℓ= ℓ′, k = k′
0
if ℓ= ℓ′, k ̸= k′
0
if ℓ̸= ℓ′, k = k′
0
if ℓ̸= ℓ′, k ̸= k′, k = ℓ′, ℓ= k′
0
if ℓ̸= ℓ′, k ̸= k′, k = ℓ′, ℓ̸= k′
0
if ℓ̸= ℓ′, k ̸= k′, k ̸= ℓ′, ℓ= k′
m−1
m3
if ℓ̸= ℓ′, k ̸= k′, k ̸= ℓ′, ℓ̸= k′.
Combining the results above yields
E

km(k, ℓ)km(k′, ℓ′)

=







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







m−1
m2
if ℓ= ℓ′, k = k′
0
if ℓ= ℓ′, k ̸= k′
0
if ℓ̸= ℓ′, k = k′
m−1
m2
if ℓ̸= ℓ′, k ̸= k′, k = ℓ′, ℓ= k′
0
if ℓ̸= ℓ′, k ̸= k′, k = ℓ′, ℓ̸= k′
0
if ℓ̸= ℓ′, k ̸= k′, k ̸= ℓ′, ℓ= k′
0
if ℓ̸= ℓ′, k ̸= k′, k ̸= ℓ′, ℓ̸= k′.
48


## Page 50


Note that
E

T 2
1,uv

=
n
X
ℓ=1
n
X
ℓ′=1
n
X
k=1,k̸=ℓ
n
X
k′=1,k′̸=ℓ′
ΨkkΨk′k′E

km(k, ℓ)km(k′, ℓ′)

UℓuUℓvUℓ′uUℓ′v
= m −1
m2
n
X
ℓ=1
n
X
k=1,k̸=ℓ
Ψ2
kkU2
ℓuU2
ℓv + m −1
m2
n
X
ℓ=1
ΨℓℓUℓuUℓv
n
X
ℓ′=1,ℓ′̸=ℓ
Ψℓ′ℓ′Uℓ′uUℓ′v
= m −1
m2
n
X
ℓ=1

tr(Ψ2) −Ψ2
ℓℓ

U2
ℓuU2
ℓv
+ m −1
m2
n
X
ℓ=1
ΨℓℓUℓuUℓv
" n
X
ℓ′=1
Ψℓ′ℓ′Uℓ′uUℓ′v −ΨℓℓUℓuUℓv
#
≤m −1
m2

tr(Ψ2) + [UT ΨU]2
uv
	
Therefore,
d
X
u=1
d
X
v=1
E

T 2
1,uv

≤d2(m −1)
m2
tr(Ψ2) + m −1
m2
d
X
u=1
d
X
v=1
[UT ΨU]2
uv
= d2(m −1)
m2
tr(Ψ2) + m −1
m2


UT ΨU


2
F
= 2d2(m −1)
m2
tr(Ψ2).
Now consider T2,uv. Recall that
T2,uv =
n
X
ℓ=1
n
X
ℓ′=1,ℓ′̸=ℓ
n
X
k=1
Ψkk
" m
X
i=1
δikδiℓδiℓ′σiℓσiℓ′
#
UℓuUℓ′v.
Deﬁne
qn,m(ℓ, ℓ′) :=
n
X
k=1
Ψkk
" m
X
i=1
δikδiℓδiℓ′σiℓσiℓ′
#
.
Note that
E

T 2
2,uv

=
n
X
ℓ=1
n
X
eℓ=1
n
X
ℓ′=1,ℓ′̸=ℓ
n
X
eℓ′=1,eℓ′̸=eℓ
E
h
qn,m(ℓ, ℓ′)qn,m(eℓ, eℓ′)
i
UℓuUℓ′vUeℓuUeℓ′v.
Write
qn,m(ℓ, ℓ′)qn,m(eℓ, eℓ′)
=
n
X
k=1
n
X
k′=1
m
X
i=1
m
X
i′=1
ΨkkΨk′k′δikδiℓδiℓ′δi′k′δi′eℓδi′eℓ′σiℓσiℓ′σi′eℓσi′eℓ′.
49


## Page 51


Then for any ℓ̸= ℓ′ and eℓ̸= eℓ′,
E
h
qn,m(ℓ, ℓ′)qn,m(eℓ, eℓ′)
i
=





Pn
k=1
Pn
k′=1
Pm
i=1 ΨkkΨk′k′E [δikδiℓδiℓ′δik′]
if ℓ= eℓ, ℓ′ = eℓ′
Pn
k=1
Pn
k′=1
Pm
i=1 ΨkkΨk′k′E [δikδiℓδiℓ′δik′]
if ℓ= eℓ′, ℓ′ = eℓ
0
otherwise.
Thus,
E

T 2
2,uv

=
n
X
ℓ=1
n
X
ℓ′=1,ℓ′̸=ℓ
E

q2
n,m(ℓ, ℓ′)

U2
ℓuU2
ℓ′v
+
n
X
ℓ=1
n
X
ℓ′=1,ℓ′̸=ℓ
E

qn,m(ℓ, ℓ′)qn,m(ℓ′, ℓ)

UℓuUℓ′vUℓ′uUℓv.
Further, write
n
X
k=1
n
X
k′=1
m
X
i=1
ΨkkΨk′k′E [δikδiℓδiℓ′δik′]
=
n
X
k=1
m
X
i=1
Ψ2
kkE [δikδiℓδiℓ′] +
n
X
k=1
n
X
k′=1,k′̸=k
m
X
i=1
ΨkkΨk′k′E [δikδiℓδiℓ′δik′] .
Note that for any ℓ̸= ℓ′,
E [δikδiℓδiℓ′] =
(
1
m2
if k = ℓor k = ℓ′
1
m3
otherwise,
so that
n
X
k=1
m
X
i=1
Ψ2
kkE [δikδiℓδiℓ′] =
 2
m2 + m −2
m3

tr(Ψ2)
=
n
X
k=1
Ψ2
kk

1(k = ℓor k = ℓ′) 1
m + 1(k ̸= ℓand k ̸= ℓ′) 1
m2

≤tr(Ψ2)
m
.
Similarly, for any ℓ̸= ℓ′ and k ̸= k′,
E [δikδiℓδiℓ′δik′] =


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


1
m2
if k = ℓ, k′ = ℓ′
1
m2
if k = ℓ′, k′ = ℓ
1
m3
if k = ℓ, k′ ̸= ℓ′
1
m3
if k ̸= ℓ, k′ = ℓ′
1
m4
if k ̸= ℓ, k′ ̸= ℓ′
50


## Page 52


Thus,
n
X
k=1
n
X
k′=1,k′̸=k
m
X
i=1
ΨkkΨk′k′E [δikδiℓδiℓ′δik′]
= 2
mΨℓℓΨℓ′ℓ′ + 1
m2 Ψℓℓ
n
X
k′=1,k′̸=ℓ,k′̸=ℓ′
Ψk′k′ + 1
m2 Ψℓ′ℓ′
n
X
k=1,k̸=ℓ′,k̸=ℓ
Ψkk
+ 1
m3
n
X
k=1,k̸=ℓ
n
X
k′=1,k′̸=k,k′̸=ℓ′
ΨkkΨk′k′
= 2
mΨℓℓΨℓ′ℓ′ + 1
m2 (Ψℓℓ+ Ψℓ′ℓ′) [tr(Ψ) −Ψℓℓ−Ψℓ′ℓ′]
+ 1
m3

[tr(Ψ) −Ψℓℓ] [tr(Ψ) −Ψℓ′ℓ′] −

tr(Ψ2) −Ψ2
ℓℓ
	
= 2
mΨℓℓΨℓ′ℓ′ −1
m2 (Ψℓℓ+ Ψℓ′ℓ′)2
+ 1
m2 (Ψℓℓ+ Ψℓ′ℓ′) tr(Ψ) −1
m3 (Ψℓℓ+ Ψℓ′ℓ′) tr(Ψ) −1
m3 tr(Ψ2)
+ 1
m3
n
[tr(Ψ)]2 + ΨℓℓΨℓ′ℓ′ + Ψ2
ℓℓ
o
≤2
mΨℓℓΨℓ′ℓ′ + 1
m2 (Ψℓℓ+ Ψℓ′ℓ′) tr(Ψ) + 1
m3
n
[tr(Ψ)]2 + ΨℓℓΨℓ′ℓ′ + Ψ2
ℓℓ
o
.
Note that
n
X
ℓ=1
n
X
ℓ′=1,ℓ′̸=ℓ
ΨℓℓΨℓ′ℓ′U2
ℓuU2
ℓ′v ≤∥Ψ∥2
2,
n
X
ℓ=1
n
X
ℓ′=1,ℓ′̸=ℓ
ΨℓℓU2
ℓuU2
ℓ′v ≤∥Ψ∥2,
n
X
ℓ=1
n
X
ℓ′=1,ℓ′̸=ℓ
Ψℓ′ℓ′U2
ℓuU2
ℓ′v ≤∥Ψ∥2,
n
X
ℓ=1
n
X
ℓ′=1,ℓ′̸=ℓ
Ψ2
ℓℓU2
ℓuU2
ℓ′v ≤∥Ψ∥2
2,
n
X
ℓ=1
n
X
ℓ′=1,ℓ′̸=ℓ
U2
ℓuU2
ℓ′v ≤1.
Using these to obtain
n
X
ℓ=1
n
X
ℓ′=1,ℓ′̸=ℓ
E

q2
n,m(ℓ, ℓ′)

U2
ℓuU2
ℓ′v
≤2
m∥Ψ∥2
2 + 2
m2 ∥Ψ∥2tr(Ψ) + 1
m3
n
[tr(Ψ)]2 + 2∥Ψ∥2
2
o
.
51


## Page 53


Now
n
X
ℓ=1
n
X
ℓ′=1,ℓ′̸=ℓ
ΨℓℓΨℓ′ℓ′UℓuUℓ′vUℓ′uUℓv
=
n
X
ℓ=1
ΨℓℓUℓuUℓv


n
X
ℓ′=1,ℓ′̸=ℓ
Ψℓ′ℓ′Uℓ′vUℓ′u


=
n
X
ℓ=1
ΨℓℓUℓuUℓv

[UT ΨU]uv −ΨℓℓUℓvUℓu
	
≤[UT ΨU]2
uv.
Similarly,
n
X
ℓ=1
n
X
ℓ′=1,ℓ′̸=ℓ
ΨℓℓUℓuUℓ′vUℓ′uUℓv ≤[UT ΨU]uv[UT U]uv,
n
X
ℓ=1
n
X
ℓ′=1,ℓ′̸=ℓ
Ψℓ′ℓ′UℓuUℓ′vUℓ′uUℓv ≤[UT ΨU]uv[UT U]uv,
n
X
ℓ=1
n
X
ℓ′=1,ℓ′̸=ℓ
Ψ2
ℓℓUℓuUℓ′vUℓ′uUℓv ≤[UT Ψ2U]uv[UT U]uv,
n
X
ℓ=1
n
X
ℓ′=1,ℓ′̸=ℓ
UℓuUℓ′vUℓ′uUℓv ≤[UT U]uv.
Then
n
X
ℓ=1
n
X
ℓ′=1,ℓ′̸=ℓ
E

qn,m(ℓ, ℓ′)qn,m(ℓ′, ℓ)

UℓuUℓ′vUℓ′uUℓv
≤2
m[UT ΨU]2
uv + 2
m2 [UT ΨU]uv[UT U]uv
+ 1
m3
n
[tr(Ψ)]2 [UT U]uv + [UT ΨU]2
uv + [UT Ψ2U]uv[UT U]uv
o
.
Combing the results above together gives
E

T 2
2,uv

≤2
m∥Ψ∥2
2 + 2
m2 ∥Ψ∥2tr(Ψ) + 1
m3
n
[tr(Ψ)]2 + 2∥Ψ∥2
2
o
+ 2
m[UT ΨU]2
uv + 2
m2 [UT ΨU]uv[UT U]uv
+ 1
m3
n
[tr(Ψ)]2 [UT U]uv + [UT ΨU]2
uv + [UT Ψ2U]uv[UT U]uv
o
.
52


## Page 54


Thus,
d
X
u=1
d
X
v=1
E

T 2
2,uv

≤2d2
m ∥Ψ∥2
2 + 2d2
m2 ∥Ψ∥2tr(Ψ) + d2
m3
n
[tr(Ψ)]2 + 2∥Ψ∥2
2
o
+ 2
mtr(Ψ2) + 2
m2 tr(Ψ) + 1
m3
n
d [tr(Ψ)]2 + 2tr(Ψ2)
o
.
Choose A(Ψ, m, n) as in (22). Then
P
 

UT ΠT ΠΨΠT ΠU −UT A(Ψ, m, n)U


2 > ϵ

≤ϵ−2E
h

UT ΠT ΠΨΠT ΠU −UT A(Ψ, m, n)U


2
F
i
≤2ϵ−2
d
X
u=1
d
X
v=1
E

T 2
1,uv + T 2
2,uv

= 2ϵ−2
2d2(m −1)
m2
tr(Ψ2) + 2d2
m2 ∥Ψ∥2tr(Ψ) + d2
m3
n
[tr(Ψ)]2 + 2∥Ψ∥2
2
o
+ 2
mtr(Ψ2) + 2
m2 tr(Ψ) + 1
m3
n
d [tr(Ψ)]2 + 2tr(Ψ2)
o 
.
Q.E.D.
53


## Page 55


Table 1: Assessment of JL Lemma: n = 20, 000, d = 5.
m
Random Sampling
Random Projections
rs1
rs2
rs3
rp1
rp2
rp3
rp4
cs
lev
Normal
Norm approximation
161
0.627
0.624
0.538
0.628
0.633
0.631
0.640
0.642
0.757
322
0.801
0.792
0.700
0.790
0.795
0.795
0.800
0.793
0.909
644
0.931
0.931
0.871
0.926
0.929
0.927
0.931
0.928
0.982
966
0.978
0.972
0.932
0.971
0.974
0.974
0.975
0.972
0.997
1288
0.990
0.987
0.973
0.990
0.991
0.989
0.990
0.991
1.000
2576
1.000
1.000
0.998
1.000
1.000
1.000
1.000
1.000
1.000
Eigenvalue distortion
161
0.189
0.191
0.191
0.189
0.187
0.188
0.189
0.188
0.158
322
0.126
0.128
0.127
0.127
0.127
0.128
0.126
0.129
0.105
644
0.082
0.085
0.084
0.086
0.084
0.085
0.085
0.086
0.071
966
0.065
0.067
0.065
0.067
0.066
0.067
0.067
0.068
0.055
1288
0.055
0.056
0.055
0.056
0.056
0.056
0.055
0.055
0.045
2576
0.033
0.036
0.033
0.036
0.037
0.036
0.035
0.037
0.029
Exponential
Norm approximation
161
0.432
0.429
0.402
0.627
0.624
0.636
0.628
0.637
0.717
322
0.580
0.578
0.548
0.796
0.795
0.794
0.800
0.791
0.875
644
0.747
0.738
0.717
0.925
0.930
0.929
0.930
0.928
0.972
966
0.851
0.840
0.812
0.971
0.968
0.973
0.969
0.972
0.992
1288
0.899
0.894
0.866
0.990
0.988
0.989
0.991
0.989
0.998
2576
0.986
0.974
0.975
1.000
1.000
1.000
1.000
1.000
1.000
Eigenvalue distortion
161
0.263
0.257
0.259
0.188
0.193
0.188
0.190
0.188
0.158
322
0.176
0.177
0.175
0.126
0.128
0.127
0.127
0.127
0.104
644
0.116
0.118
0.116
0.084
0.083
0.083
0.082
0.085
0.069
966
0.090
0.094
0.090
0.066
0.067
0.066
0.065
0.065
0.055
1288
0.076
0.079
0.075
0.055
0.055
0.055
0.054
0.055
0.045
2576
0.048
0.052
0.048
0.036
0.036
0.037
0.035
0.036
0.030
54


## Page 56


Table 2: Monte Carlo Experiments: Properties of Combining Sketches, n = 1e6
K = 3
m
J
rs1
srht
cs
lev
rs1
srht
cs
lev
ˆβ3 with β3 = 1.0
se(ˆβ3)
500
1
0.999
1.002
0.999
1.000
0.046
0.044
0.045
0.039
500
5
0.999
1.000
1.000
1.001
0.021
0.020
0.020
0.018
500
10
1.000
1.000
1.000
1.000
0.014
0.015
0.015
0.012
1000
1
1.000
0.999
0.998
1.000
0.032
0.032
0.031
0.026
1000
5
1.000
1.000
1.000
1.000
0.014
0.015
0.015
0.012
1000
10
1.000
0.999
1.000
1.000
0.010
0.010
0.010
0.008
2000
1
1.001
1.000
1.001
1.000
0.021
0.022
0.022
0.019
2000
5
1.000
1.000
1.000
1.000
0.010
0.010
0.010
0.008
2000
10
1.000
1.000
1.000
1.000
0.007
0.007
0.007
0.006
5000
1
1.000
1.001
0.999
1.000
0.014
0.014
0.014
0.012
5000
5
1.000
1.000
0.999
1.000
0.006
0.006
0.006
0.005
5000
10
1.000
1.000
1.000
1.000
0.005
0.005
0.004
0.004
Size
Power, β3 = 0.98
500
1
0.050
0.040
0.062
0.063
0.081
0.069
0.071
0.104
500
5
0.035
0.029
0.021
0.045
0.114
0.115
0.123
0.185
500
10
0.039
0.051
0.053
0.037
0.276
0.258
0.265
0.345
1000
1
0.048
0.044
0.050
0.052
0.101
0.101
0.085
0.113
1000
5
0.024
0.046
0.032
0.023
0.221
0.218
0.233
0.320
1000
10
0.041
0.035
0.044
0.042
0.461
0.454
0.452
0.617
2000
1
0.045
0.052
0.058
0.055
0.136
0.142
0.147
0.189
2000
5
0.034
0.022
0.035
0.025
0.436
0.432
0.451
0.545
2000
10
0.040
0.043
0.038
0.053
0.763
0.761
0.767
0.902
5000
1
0.053
0.046
0.040
0.047
0.298
0.322
0.275
0.399
5000
5
0.026
0.018
0.026
0.019
0.835
0.832
0.829
0.930
5000
10
0.045
0.046
0.036
0.054
0.987
0.993
0.989
0.999
K = 9
m
J
rs1
cs
rs1
cs
rs1
cs
rs1
cs
Size
Power
ˆβ9
se(ˆβ9)
500
1
0.049
0.067
0.076
0.079
0.999
0.998
0.046
0.047
500
5
0.038
0.029
0.129
0.120
1.000
1.000
0.021
0.020
500
10
0.032
0.039
0.241
0.268
0.999
1.000
0.014
0.015
1000
1
0.052
0.041
0.099
0.087
1.000
1.000
0.032
0.031
1000
5
0.036
0.027
0.219
0.214
1.000
1.000
0.014
0.014
1000
10
0.033
0.042
0.461
0.484
1.000
1.000
0.010
0.010
2000
1
0.043
0.050
0.143
0.128
1.000
0.999
0.022
0.022
2000
5
0.025
0.028
0.411
0.400
1.000
1.000
0.010
0.010
2000
10
0.041
0.044
0.782
0.773
1.000
1.000
0.007
0.007
5000
1
0.051
0.057
0.260
0.292
0.999
1.000
0.014
0.015
5000
5
0.021
0.037
0.839
0.813
1.000
1.000
0.006
0.007
5000
10
0.033
0.044
0.988
0.990
1.000
1.000
0.005
0.005
55


## Page 57


Table 3: Inference Conscious Choice of m
n = 1e7, r = 10, K = 10, m0 = 1000, ¯α = 0.05
(β0
1 −β10)
¯γ
σe
.005
.01
.015
.02
.025
0.50
0.50
29686
7421
3298
1855
1187
0.80
0.50
67837
16959
7537
4240
2713
0.90
0.50
93965
23491
10441
5873
3759
0.50
1.00
98296
24574
10922
6143
3932
0.80
1.00
224620
56155
24958
14039
8985
0.90
1.00
311136
77784
34571
19446
12445
0.50
3.00
981128
245282
109014
61321
39245
0.80
3.00
2242020
560505
249113
140126
89681
0.90
3.00
3105562
776391
345062
194098
124222
56


## Page 58


Table 4: Example of Belenzon et al. (2017)
(1)
(2)
(3)
(4)
Uniform Sampling
Full Sample
m1
m2(m1)
m3
K log(nK)
(¯α, ¯γ) = (.05, .8)
τ2(∞) = 5
Dummy for eponymous
0.031**
0.035**
0.031**
0.031**
(0.001)
(0.010)
(0.003)
(0.002)
ln(assets)
0.005**
0.000
0.006**
0.007**
(0.001)
(0.004)
(0.001)
(0.001)
ln(no. shareholders)
-0.032**
-0.025**
-0.030**
-0.031**
(0.001)
(0.007)
(0.002)
(0.002)
Equity dispersion
-0.012**
-0.007
-0.016**
-0.017**
(0.001)
(0.011)
(0.003)
(0.003)
Omitted Covariates
132
58
54
Observations
562,170
8,158
112,355
139,022
(1)
(2)
(3)
(4)
Countsketch
Full Sample
m1
m2
m3
Dummy for eponymous
0.031**
0.035**
0.030**
0.032**
(0.001)
(0.011)
(0.003)
(0.003)
ln(assets)
0.005**
0.009**
0.004**
0.005**
(0.001)
(0.003)
(0.001)
(0.001)
ln(no. shareholders)
-0.032**
-0.028**
-0.032**
-0.032**
(0.001)
(0.008)
(0.002)
(0.002)
Equity dispersion
-0.012**
-0.024
-0.010*
-0.011**
(0.001)
(0.014)
(0.004)
(0.004)
Omitted Covariates
2
1
1
Observations
562,170
8,147
112,347
139,015
Robust standard errors in parentheses
** p<0.01, * p<0.05
57


## Page 59


References
Achiloptas, D. 2003, Database Friendly Random Projections: Johnson-Lindenstrauss with Binary
Coins, Journal of Computer and System Sciences 66(4), 671–687.
Agarwal, P. S. H.-P. and Varadarajan, K. 2004, Approximating Extent Measures of Points, Journal
of the ACM 51(4), 606–635.
Ahfock, D., Astle, W. and Richardson, S. 2017, Statistical Properties of Sketching Algorithms,
arXiv:1706.03665v1.
Ailon, N. and Chazelle, B. 2009, The Fast Johnson-Lindenstrauss Transform and Approximate
Nearest Neighbors, SIAM Journal Computing 39(1), 302–322.
Alon, N., Matias, Y. and Onak, K. 1999, The Space Complexity of Approximating the Frequency
Moments, Journal of Computational Systems Science 58(1), 137–147.
Bai, Z. and Yin, Y. 1993, Limit of the Smallest Eigenvalue of a Large Dimensional Sample Covari-
acne Matrix, Annals of Probability 21:3, 1275–1294.
Belenzon, S., Chatterji, A. and Dailey, B. 2017, Eponymous Enterpreneurs, American Economic
Reivew 107:6, 1638–1655.
Boivin, J. and Ng, S. 2006, Are More Data Always Better for Factor Analysis, Journal of Econo-
metrics 132, 169–194.
Boutidis, C. and Gittens, A. 2013, Improved Matrix Algorithms via the Subsampled Randomized
Hadamadr Transform, SIAM Journal on Matrix Analysis 34:3, 1301–1340.
Breiman, L. 1999, Pasting Bites Together for Prediction in Large Data Sets and On-Line, Machine
Learning 36(2), 85–103. https://www.stat.berkeley.edu/ breiman/pastebite.pdf.
Charika, M., Chen, K. and Farach-Colton, M. 2002, Finding Frequent Items in Data Streams, In
Proceedings of International Colloquium on Automata, Languages, and Programming (ICALP)
pp. 693–703.
Chawla, N., Hall, L., Bowyer, K. and Kegelmeyer, P. 2004, Learning Ensembles from Bites: A
Scalable and Accurate Approach, Journal of Machine Learning Research 5, 421–451.
Chen, S., Varma, R., Singh, A. and Kovacevic, J. 2016, A Statistical Perspective of Sampling Scores
for Linear Regresson, IEEE International Symposium on Information theory.
Chi, J. and Ipsen, I. 2018, Randomized Least Squares Regression: Combining Model and Algorithm
Induced Uncertainties, xrXiv:1808.05924v1.
Christmann, A., Steinwart, I. and Hubert, M. 2007, Robust Learning from Bites for Data Mining,
Computational Statistics and Data Analysis 52, 347–361.
Clarkson, K. and Woodruﬀ, D. 2013, Low Rank Approximation and Regression in Input Sparsity
Time, Proceedings of the 45th ACM Symposium on the Theory of Computing.
Cohen, M., Lee, Y., Musco, C., Musco, C., Peng, R. and Sidford, A. 2015, Uniform Sampling for
Matrix Approximation, Proceedings of the 46th ACM Symposium on the Theory of Computing
pp. 181–190.
Cohen, M., Nelson, J. and Woodruﬀ, D. 2015, Optimal Approximate Matrix Product in Terms of
Stable Rank, arXiv:1507.02268.
58


## Page 60


Comrode, G., Garofalakis, M., Haas, P. and Jermaine, C. 2011, Synposes for Massive Data: Sam-
ples, Histograms, Wavelets,Sketches, Foundations and Trends in Databases 4(1), 1–294.
Conmode, G. and Muthukrishnan, S. 2005, An Improved Data Stream Summary: The Count-Min
Sketch and Applications, Journal of Algorithms 55, 29–38.
Cramer, J. S. 1987, Mean and Variance of R2 in Small and Moderate Samples, Journal of Econo-
metrics 35, 253–266.
Dahiya, Y., Konomis, D. and Woodruﬀ, D. 2018, An Empirical Evaluation of Sketching for Nu-
merical Linear Algebra, KDD, http://www.cs.cmu.edu/afs/cs/user/dwoodruf/www/dkw18.pdf.
Dasgupta, S. and Gupta, A. 2003, An Elementary Proof of a Theorem of Johnson and Lindenstrauss,
Random Structure and Algorithms 22(1), 60–65.
Dasgupta, A., Kumar, R. and Sarlos, T. 2010, A Sparse Lindenstrauss Transform, STOC pp. 341–
350.
Deaton, A. and Ng, S. 1998, Parametric and Nonparametric Approaches to Tax Reform, Journal
of the American Statistical Association 93(443), 900–909.
Dhillon, P., Lu, Y., Foster, D. and Ungar, L. 2013, New Subsampling Algorithms for Faster Least
Squares Regression, Advances in Neural Information Processing Systems (NIPS) 26, 360–368.
Drineas, P. and Mahoney, M. 2005, On the Nystrom Method for Approximating a Gram Matrix
for Improved Kernel Based Learning, Journal of Machine Learning Research 6, 2152–2125.
Drineas, P., Kannan, R. and Mahoney, M. 2006, Fast Monte Carlo Algorithms for Matrices I:
Approximating Matrix Multiplications, SIAM Journal on Computing 36, 132–157.
Drineas, P., Magdon-Ismail, M., Mahoney, M. and Woodruﬀ, D. 2012, Fast Approximation of
Matrix Coherence and Statistical Leverage, Journal of Machine Learning Research 13, 3441–
3472.
Drineas, P., Mahoney, M. and Muthukrishnan, S. 2006, Sampling Algorithms for L2 Regression and
Applications, Proceedings of the 17th Annual ACM-SIAM Symposium on Discrete Algorithms
pp. 1127–1136.
Drineas, P., Mahoney, M., Muthukrishnan, S. and Sarlos, T. 2011, Faster Least Squares Approxi-
mation, Numerical Mathematics 117, 219–249.
Du Mouchel, W., Volinsky, C., Johnson, T., Cortes, C. and Pregibon, D. 1999, Squashing Flat Files
Flatter, Proceedings of the Fifth ACM Conference on Knowledge Discovery and Data Mining
pp. 6–15.
Eriksson-Bique, S., Solberg, M., Stefanelli, M., Warkentin, S., Abbey, R. and Ipsen, I. 2011, Im-
portance Sampling for a Monte Carlo Matrix Multiplication Algorithm with Application to In-
formation Retrieval, SIAM Journal Computing 33(4), 1689–1706.
Fedoruk, J., Schmuland, B., Johnson, J. and Heo, G. 2018, Dimensionality Reduction via the
Johnson-Lindenstrauss Lemma: Theoretical Empirical Bounds on Embedding Dimension, Jour-
nal of Supercomputing 74:4, 3933–3949.
Geppert, L., Ickstadt, K., Munteanu, A., Quedenfeld, J. and Sohler, C. 2017, Random Projections
for Bayesian Regression, Statistics and Computing 27(1), 79–101.
59


## Page 61


Ghashami, M., Liberty, E., Phillips, M. and Woodruﬀ, D. 2016, Frequent Directions: Simple and
Deterministic Matrix Sketching, SIAM Journal Computing 45(5), 1762–1792.
Heince, C., McWilliams, B. and Meinshausen, N. 2016, Dual Loco: Distributing Statistical Es-
timation Using Random Projections, 19th International Conference on Artiﬁcial Intelligence
51, 875–883.
Hogben, L. 2007, Handbook of Linear Algebra, Chapman and Hall.
Horvitz, D. and Thompson, D. 1952, A Generalization of Sampling Replacement from a Finite
Universe, Journal of the American Statistical Association 47, 663–685.
Indyk, P. and Motwani, R. 1998, Approximate Nearest Neighborhood and the Fast Johnson-
Lindenstrauss Transform, Proceedings of the 30th ACM Symposium on Theory of Computing
pp. 604–613.
Ipsen, I. and Wentworth, T. 2014, The Eﬀect of Coherence on Sampling From Matrices with
Orthonormal Columns and Preconditioned Least Squares Problems, Siam Journal of Matrix
Analysis and Applicatons 35(4), 1490–1520.
IPUMS 2020, Ruggles, S. and S. Flood and R. Goeken and J. Grover and E. Meyer and J. Pacas
and M. Sobek, Vol. Version 10, Minneapolis, p. https://doi.org/10.18128/D010.V10.0.
Johnson, W. and Lindenstauss, J. 1994, Extensions of Lipschitz Maps into a Hilbert Space, Con-
temporary Mathematics, 26: 189–206.
Jolliﬀe, I. 1972, Discarding Variables in a Principal Component Analysis: Artiﬁcial Data, Applied
Statistics 21(2), 160–173.
Kane, D. and Nelson, J. 2014, Sparser Johnson-Lindenstrauss Transforms, Journal of the ACM
61:1, 4.1–4.10.
Li, P., Hastie, T. and Church, K. 2006, Very Sparse Random Projections, KDD pp. 287–296.
Ma, P., Mahoney, M. W. and Yu, B. 2014, A Statistical Perspective on Algorithmic Leveraging,
Proceedings of the 31st ICML Conference, Vol. arXiv: 1306.5362.
Madigan, D., Raghavan, N., Dumouchel, W., Nason, M., Posse, C. and Ridgeway, G. 1999,
Likelihood-Based Data Squashing: A Modeling Approach to Instance Construction, Technical
report, AT and T Labs Ressearch.
Mahoney, M. W. 2011, Randomized Algorithms for Matrices and Data, Foundations and Trends
in Machine Learning, http://dx.doi.org/10.1561/2200000035 edn, Vol. 3:2, NOW, pp. 123–224.
Matousek, J. 2008, On Variants of the Johnson-Lindenstrauss Lemma, Random Structure and
Algorithms 33(2), 142–156.
McWilliams, B., Krummenacher, C., Lucic, G. and Buhmann, J. 2014, Fast and Robust Least
Squares Estimation in Corrupted Linear Models, Advances in Neural Information Processing
Systems (NIPS) pp. 415–423.
Meng, X. and Mahoney, M. 2013, Low Distortion Subspace Embeddings in Input-Sparsity time
and Applications to Robust Linear Regression, Proceedings of the 45th ACM Symposium on the
Theory of Computing.
Mitzenmacher, M. and Upfal, E. 2006, Probability and Computing: Randomized Algorithms and
Probabilistic Analysis, Cambridge University Press.
60


## Page 62


Nelson, J. and Nguyen, H. 2013a, OSNAP: Faster Numerical Linear Algebra Algorithms via Sparser
Subspace Embeddings, Proceedings of the 54th Annual IEEE Symposium on Foundations of
Computer Science (FOCS).
Nelson, J. and Nguyen, H. 2013b, Sparsity Lower Bounds for Dimensionality Reducing Maps, STOC
pp. 101–110.
Nelson, J. and Nguyen, H. 2014, Lower Bounds for Oblvious Subspace Embeddings, Proceedings of
the 41st Interational Colluqium on Automata, Langauges and Programming (ICALP), pp. 883–
894.
Ng, S. 2017, Opportunities and Challenges: Lessons from Analyzing Terabytes of Scanner Data, in
B. Honore, A. Pkes, M. Piazzesi and L. Samuelson (eds), Advances in Economics and Economet-
rics, Eleventh World Congress of the Econometric Society, Vol. II, Cambridge University Press,
pp. 1–34.
Owen, A. 1990, Empirical Likelihood Ratio Conﬁdence Region, Annals of Statistics 18, 90–120.
Pilanci, M. and Wainwright, M. 2015, Randomized Sketches of Convex Programs with Sharp Guar-
antees, IEEE Transactions of Information Theory 61(9), 5096–5115.
Pilanci, M. and Wainwright, M. 2016, Iterative Hessian Sketch: and Accurate Solution Approxi-
mation for Constrained Least Squares, Journal of Machine Learning Research pp. 1–33.
Portnoy, S. and Koenker, R. 1997, The Gaussian Hare and the Laplacian Tortoise: Computability
of Squared-Error versus Absolute-Error Estimation, Statistical Science 12:4, 279–300.
Raskutti, G. and Mahoney, M. 2016, A Statistical Perspective on Randomized Sketching for Ordi-
nary Least Squares, Journal of Machine Learning Research pp. 1–31.
Rudd, P. 2000, An Introduction to Classical Econometric Theory, Oxford University Press.
Sarlos, T. 2006, Improved Approximation Algorithms for Large Matrices via Random Projections,
Proceedings of the 47 IEEE Symposium on Foundations of Computer Science, Berkeley, CA,
2006, pp. 143–152.
Vershynin, R. 2017, Four Lectures on Probabilistic Methods for Data Science, arXiv:1612.06661v2.
Wainwright, M. 2019, High-Dimensional Statistics: A Non-Asymptotic Viewpoint, Cambridge Se-
ries in Statistical and Probabilistic Mathematics. manuscript in preparation.
Wallace, T. 1972, Weaker Criteria and Tests for Linear Restrictions, Econometrica 40(4), 689–698.
Wang, H., Yang, M. and Stufken, J. 2019, Information-Based Optimal Subdata Selection for Big
Data Linear Research, Journal of the American Statistical Association 114:525, 393–405.
Wang, H., Zhu, R. and Ma, P. 2018, Optimal Subsampling for Large Sample Logistic Regression,
Journal of the American Statistical Association 113(522), 849–844.
Wang, J., Lee, J., Mahdav, M., Kolar, M. and Srebo, N. 2017, Sketching Meets Random Projection
in the Dual: A Provable Recovery Algorithm for Big and High Dimensional Data, Electronic
Journal of Statistics 11, 4896–4944.
Wang, S., Gittens, A. and Mahoney, M. 2018, Sketched Ridge Regression: Optimization Per-
spective, Statistical Perspective, and Model Averaging, Proceedings of the 34th International
Conference on Machine Learning 19, 1–50.
61


## Page 63


Woodruﬀ, D. 2014, Sketching as a Tool for Numerical Linear Algebra, Foundations and Trends in
Theoretical Computer Science 10(1-2), 1–157.
Woolfe, F., Liberty, E., Vladmir, R. and Mark, T. 2008, A Fast Randomized Algorithm for the
Approximation of matrices, Applied and Computational Harmonic Analysis 25:3, 335–366.
Yin, Y., Bai, Z. and Krishnaiah, P. 1988, On the Limit of the Largest Eigenvalue of the Largest
Dimensional Sample Covariance Matrix, 78:4, 509–521.
62

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
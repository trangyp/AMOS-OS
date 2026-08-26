---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1303.1927v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1303.1927v1_The_linear_stochastic_order_and_directed_inference_for_multivariate_ordered_dist

> Source: 1303.1927v1_The_linear_stochastic_order_and_directed_inference_for_multivariate_ordered_dist.pdf

> Pages: 41

---


## Page 1


arXiv:1303.1927v1  [math.ST]  8 Mar 2013
The Annals of Statistics
2013, Vol. 41, No. 1, 1–40
DOI: 10.1214/12-AOS1062
c
⃝Institute of Mathematical Statistics, 2013
THE LINEAR STOCHASTIC ORDER AND DIRECTED
INFERENCE FOR MULTIVARIATE ORDERED DISTRIBUTIONS
By Ori Davidov1 and Shyamal Peddada2
University of Haifa and National Institute of Environmental
Health Sciences
Researchers are often interested in drawing inferences regarding
the order between two experimental groups on the basis of multivari-
ate response data. Since standard multivariate methods are designed
for two-sided alternatives, they may not be ideal for testing for order
between two groups. In this article we introduce the notion of the
linear stochastic order and investigate its properties. Statistical the-
ory and methodology are developed to both estimate the direction
which best separates two arbitrary ordered distributions and to test
for order between the two groups. The new methodology generalizes
Roy’s classical largest root test to the nonparametric setting and is
applicable to random vectors with discrete and/or continuous compo-
nents. The proposed methodology is illustrated using data obtained
from a 90-day pre-chronic rodent cancer bioassay study conducted
by the National Toxicology Program (NTP).
1. Introduction.
In a variety of applications researchers are interested in
comparing two treatment groups on the basis of several, potentially depen-
dent outcomes. For example, to evaluate if a chemical is a neuro-toxicant,
toxicologists compare a treated group of animals with an untreated control
group in terms of various correlated outcomes such as tail-pinch response,
click response and gait score, etc.; cf. Moser (2000). The statistical problem
of interest is to compare the multivariate distributions of the outcomes in
the control and treatment groups. Moreover, the outcome distributions are
expected to be ordered in some sense. The theory of stochastic order rela-
Received August 2011; revised July 2012.
1Supported in part by the Israeli Science Foundation Grant No 875/09.
2Supported in part by the Intramural Research Program of the NIH, National Institute
of Environmental Health Sciences (Z01 ES101744-04).
AMS 2000 subject classiﬁcations. 60E15, 62E20, 62G10, 62G20, 62H99, 62P15.
Key words and phrases. Nonparametric tests, order-restricted statistical inference,
stochastic order relations.
This is an electronic reprint of the original article published by the
Institute of Mathematical Statistics in The Annals of Statistics,
2013, Vol. 41, No. 1, 1–40. This reprint diﬀers from the original in pagination and
typographic detail.
1


## Page 2


2
O. DAVIDOV AND S. PEDDADA
tions [Shaked and Shanthikumar (2007)] provides the theoretical foundation
for such comparisons.
To ﬁx ideas let X and Y be p-dimensional random variables (RVs);
X is said to be smaller than Y in the multivariate stochastic order, de-
noted X ⪯st Y, provided P(X ∈U) ≤P(Y ∈U) for all upper sets U ∈Rp
[Shaked and Shanthikumar (2007)]. If for some upper set the above inequal-
ity is sharp, we say that X is strictly smaller than Y (in the multivariate
stochastic order) which we denote by X ≺st Y. Recall that a set U ∈Rp
is called an upper set if u ∈U implies that v ∈U whenever u ≤v, that
is, if ui ≤vi, i = 1,...,p. Note that comparing X and Y with respect to
the multivariate stochastic order requires comparing their distributions over
all upper sets in Rp. This turns out to be a very high-dimensional prob-
lem. For example, if X and Y are multivariate binary RVs, then X ⪯st Y
provided P
t∈U pX(t) ≤P
t∈U pY(t) where pX(t) and pY(t) are the corre-
sponding probability mass functions. Here U ∈Up where Up is the family
of upper sets deﬁned on the support of a p-dimensional multivariate binary
RV. It turns out that the cardinality of Up, denoted by Np, grows super-
exponentially with p. In fact N1 = 1, N2 = 4, N3 = 18, N4 = 166, N5 = 7579
and N6 = 7,828,352. The values of N7 and N8 are also known, but N9 is not.
However, good approximations for Np are available for all p; cf. Davidov and
Peddada (2011). Obviously the number of upper sets for general multivari-
ate RVs is much larger. Since in many applications p is large, it would seem
that the analysis of high-dimensional stochastically ordered data is practi-
cally hopeless. As a consequence, the methodology for analyzing multivariate
ordered data is underdeveloped. It is worth mentioning that Sampson and
Whitaker (1989) as well as Lucas and Wright (1991) studied stochastically
ordered bivariate multinomial distributions. They noted the diﬃculty of ex-
tending their methodology to high-dimensional data due to the large num-
ber of constraints that need to be imposed. Recently Davidov and Peddada
(2011) proposed a framework for testing for order among K, p-dimensional,
ordered multivariate binary distributions.
In this paper we address the dimensionality problem by considering an
easy to understand stochastic order which we refer to as the linear stochastic
order.
Definition 1.1.
The RV X is said to be smaller than the RV Y in
the (multivariate) linear stochastic order, denoted X ⪯l-st Y, if for all s ∈
Rp
+ = {s:s ≥0},
sT X ⪯st sT Y,
(1.1)
where ⪯st in (1.1) denotes the usual (univariate) stochastic order.
Note that it is enough to limit (1.1) to all nonnegative real vectors sat-
isfying ∥s∥= 1, and accordingly we denote by Sp−1
+
the positive part of the


## Page 3


INFERENCE FOR THE LINEAR STOCHASTIC ORDER
3
unit sphere in Rp. We call each s ∈Sp−1
+
a “direction.” In other words the
RVs X and Y are ordered by the linear stochastic order if every nonnegative
linear combination of their components is ordered by the usual (univariate)
stochastic order. Thus instead of considering all upper sets in Rp we need
for each s ∈Sp−1
+
to consider only upper sets in R. This is a substantial re-
duction in dimensionality. In fact we will show that only one value of s need
be considered. Note that the linear stochastic order, like the multivariate
stochastic order, is a generalization of the usual univariate stochastic order
to multivariate data. Both of these orders indicate, in diﬀerent ways, that
one random vector is more likely than another to take on large values. In this
paper we develop the statistical theory and methodology for estimation and
testing for linearly ordered multivariate distributions. For completeness we
note that weaker notions of the linear stochastic order are discussed by Hu,
Homem-de Mello and Mehrotra (2011) and applied to various optimization
problems in queuing and ﬁnance.
Comparing linear combinations has a long history in statistics. For exam-
ple, in Phase I clinical trials it is common to compare dose groups using an
overall measure of toxicity. Typically, this quantity is an ad hoc weighted av-
erage of individual toxicities where the weights are often known as “severity
weights;” cf. Bekele and Thall (2004) and Ivanova and Murphy (2009). This
strategy of dimension reduction is not new in the statistical literature and
has been used in classical multivariate analysis when comparing two or more
multivariate normal populations. For example, using the union-intersection
principle, the comparison of multivariate normal populations can be reduced
to the comparison of all possible linear combinations of their mean vectors.
This approach is the basis of Roy’s classical largest root test [Roy (1953),
Johnson and Wichern (1998)]. Our proposed test may be viewed as nonpara-
metric generalization of the classical normal theory method described above
with the exception that we limit consideration only to nonnegative linear
combinations (rather than all possible linear combinations) since our main
focus is to make comparisons in terms of stochastic order. We emphasize
that the linear stochastic order will allow us to address the much broader
problem of directional ordering for multivariate ordered data, that is, to ﬁnd
the direction which best separates two ordered distributions. Based on our
survey of the literature, we are not aware of any methodology that addresses
the problems investigated here.
This paper is organized in the following way. In Section 2 some proba-
bilistic properties of the linear stochastic order are explored, and its rela-
tionships with other multivariate stochastic orders are clariﬁed. In Section 3
we provide the background and motivation for directional inference under
the linear stochastic order and develop estimation and testing procedure for
independent as well as paired samples. In particular the estimator of the
best separating direction is presented and its large sampling properties de-


## Page 4


4
O. DAVIDOV AND S. PEDDADA
rived. We note that the problem of estimating the best separating direction
is a nonsmooth optimization problem. The limiting distribution of the best
separating direction is derived in a variety of settings. Tests for the linear
stochastic order based on the best separating direction are also developed.
One advantage of our approach is that it avoids the estimation of multivari-
ate distributions subject to order restrictions. Simulation results, presented
in Section 4, reveal that for large sample sizes the proposed estimator has
negligible bias and mean squared error (MSE). The bias and MSE seem to
depend on the true value of the best separating direction, the dependence
structure and the dimension of the problem. Furthermore, the proposed test
honors the nominal type I error rate and has suﬃcient power. In Section 5 we
illustrate the methodology using data obtained from the National Toxicol-
ogy Program (NTP). Concluding remarks and some open research problems
are provided in Section 6. For convenience all proofs are provided in the
Appendix where additional concepts are deﬁned when needed.
2. Some properties of the linear stochastic order.
We start by clarify-
ing the relationship between the linear stochastic order and the multivari-
ate stochastic order. First note that X ⪯l-st Y if and only if P(sT X ≥t) ≤
P(sT Y ≥t) for all (t,s) ∈R × Rp
+ which is equivalent to P(X ∈H) ≤P(Y ∈
H) for all H ∈H where H is the collection of all upper half-planes, that is,
sets which are both half planes and upper sets. Thus X ⪯st Y ⇒X ⪯l-st Y.
The converse does not hold in general.
Example 2.1.
Let X and Y be bivariate RVs such that P(X = (1,1)) =
P(X = (0,1)) = P(X = (1,0)) = 1/3 and P(Y = (3/4,3/4)) = P(Y = (1,2)) =
P(Y = (2,1)) = 1/3. It is easy to show that X is smaller than Y in the linear
stochastic order but not in the multivariate stochastic order.
The following theorem provides some closure results for the linear stochas-
tic order.
Theorem 2.1.
(i) If X ⪯l-st Y, then g(X) ⪯l-st g(Y) for any aﬃne in-
creasing function; (ii) if X ⪯l-st Y, then XI ⪯l-st YI for each subset I ∈
{1,... ,p}; (iii) if X|Z = z ⪯l-st Y|Z = z for all z in the support of Z, then
X ⪯l-st Y; (iv) if X1,...,Xn are independent RVs with dimensions pi and
similarly for Y1,...,Yn and if in addition Xi ⪯l-st Yi, then (X1,...,Xn) ⪯l-st
(Y1,...,Yn); (v) ﬁnally, if Xn →X and Yn →Y where convergence can
be in distribution, in probability or almost surely and if Xn ⪯l-st Yn for all
n, then X ⪯l-st Y.
Theorem 2.1 shows that the linear stochastic order is closed under in-
creasing linear transformations, marginalization, mixtures, conjugations and
convergence. In particular parts (ii) and (iii) of Theorem 2.1 imply that if


## Page 5


INFERENCE FOR THE LINEAR STOCHASTIC ORDER
5
X ⪯l-st Y, then Xi ⪯st Yi and Xi + Xj ⪯st Yi + Yj for all i and j; that is,
all marginals are ordered as are all convolutions. Although the multivariate
stochastic order is in general stronger than the linear stochastic order, there
are situation in which both orders coincide.
Theorem 2.2.
Let X and Y be continuous elliptically distributed RVs
supported on Rp with the same generator. Then X ⪯l-st Y if and only if
X ⪯st Y.
Note that the elliptical family of distributions is large and includes the
multivariate normal, multivariate t and the exponential power family; see
Fang, Kots and Ng (1989). Thus Theorem 2.2 shows that the multivariate
stochastic order coincides with the linear stochastic order in the normal
family. Incidentally, in the proof of Theorem 2.2 we generalize the results of
Ding and Zhang (2004) on multivariate stochastic ordering of elliptical RVs.
Another interesting example is the following:
Theorem 2.3.
Let X and Y be multivariate binary RVs. Then X ⪯l-st
Y is equivalent to X ⪯st Y if and only if p ≤3.
Remark 2.1.
In the proof of Theorem 2.2 distributional properties of
the elliptical family play a major role. In contrast, Theorem 2.3 is a conse-
quence of the geometry of the upper sets of multivariate binary RVs which
turn out to be upper half planes if and only if p ≤3.
We now explore the role of the dependence structure.
Theorem 2.4.
Let X and Y have the same copula. Then X ⪯l-st Y if
and only if X ⪯st Y.
Theorem 2.4 establishes that if two RVs have the same dependence struc-
ture as quantiﬁed by their copula function [cf. Joe (1997)], then the linear
and multivariate stochastic orders coincide. Such situations arise when the
correlation structure among outcomes is not expected to vary with dose.
The orthant orders are also of interest in statistical applications. We say
that X is smaller than Y in the upper orthant order, denoted X ⪯uo Y,
if P(X ∈O) ≤P(Y ∈O) for all O ∈O where O is the collection of upper
orthants, that is, sets of the form {z:z ≥x} for some ﬁxed x ∈Rp. The lower
orthant order is similarly deﬁned; cf. Shaked and Shanthikumar (2007) or
Davidov and Herman (2011). It is obvious that the orthant orders are weaker
than the usual multivariate stochastic order, that is, X ⪯st Y ⇒X ⪯uo Y
and X ⪯lo Y. In general the linear stochastic order does not imply the upper
(or lower) orthant order, nor is the converse true. However, as stated below,
under some conditions on the copula functions, the linear stochastic order
implies the upper (or lower) orthant order.


## Page 6


6
O. DAVIDOV AND S. PEDDADA
Theorem 2.5.
If X ⪯l-st Y and CX(u) ≤CY(u) for all u ∈[0,1]p, then
X ⪯lo Y. Similarly if X ⪯l-st Y and ¯CX(u) ≤¯CY(u) for all u ∈[0,1]p, then
X ⪯uo Y.
Note that CX(u) and ¯CX(u) above are the copula and tail-copula func-
tions for the RV X [cf. Joe (1997)] and are deﬁned in the Appendix and sim-
ilarly for CY(u) and ¯CY(u). Further note that the relations CX(u) ≤CY(u)
and/or ¯CX(u) ≤¯CY(u) indicate that the components of Y are more strongly
dependent than the components of X. This particular dependence ordering
is known as positive quadrant dependence. It can be further shown that
strong dependence and the linear stochastic order do not in general imply
stochastic ordering.
Additional properties of the linear stochastic order as they relate to esti-
mation and testing problems are given in Section 3.
3. Directional inference.
3.1. Background and motivation.
There exists a long history of well-
developed theory for comparing two or more multivariate normal (MVN)
populations. Methods for assessing whether there are any diﬀerences be-
tween the populations [which diﬀer? in which component(s)? and by how
much?] have been addressed in the literature using a variety of simultane-
ous conﬁdence intervals and multiple comparison methods; cf. Johnson and
Wichern (1998). Of particular interest to us is Roy’s largest root test. To
ﬁx ideas consider two multivariate normal random vectors X and Y with
means µ and ν, respectively, and a common variance matrix Σ. Using the
union-intersection principle Roy (1953) expressed the problem of testing
H0 :µ = ν versus H1 :µ ̸= ν as a collection of univariate testing problems,
by showing that H0 and H1 are equivalent to T
s∈Rp H0,s and S
s∈Rp H1,s
where H0,s :sT µ = sT ν and H1,s :sT µ ̸= sT ν. Implicitly Roy’s test identiﬁes
the linear combination sT
max(ν −µ) that corresponds to the largest “dis-
tance” between the mean vectors, that is, the direction which best separates
their distributions. The resulting test, known as Roy’s largest root test, is
given by the largest eigenvalue of BS−1 where B is the matrix of between
groups (or populations) sums of squares and cross products, and S is the
usual unbiased estimator of Σ. In the special case when there are only two
populations, this test statistic is identical to Hotelling’s T 2 statistic. From
the simultaneous conﬁdence intervals point of view, the critical values de-
rived from the null distribution of this statistic can be used for constructing
Scheﬀe’s simultaneous conﬁdence intervals for all possible linear combina-
tions of the diﬀerence (µ −ν). Further note that the estimated direction
corresponding to Roy’s largest root test is S−1( ¯Y −¯X) where ¯X and ¯Y are
the respective sample means.


## Page 7


INFERENCE FOR THE LINEAR STOCHASTIC ORDER
7
Our objective is to extend and generalize the classical multivariate method,
described above, to nonnormal multivariate ordered data. Our approach
will be nonparametric. Recall that comparing MVNs is done by consider-
ing the family of statistics Tn,m(s) = sT ( ¯Y −¯X) for all s ∈Rp. In the case
of nonnormal populations, the population mean alone may not be enough
to characterize the distribution. In such cases, it may not be suﬃcient to
compare the means of the populations but one may have to compare entire
distributions. One possible way of doing so is by considering rank statistics.
Suppose X1,...,Xn and Y1,...,Ym are independent random samples from
two multivariate populations. Let
Rk(s) =
n
X
i=1
I(sT Xi≤sT Xk) +
m
X
j=1
I(sT Yj≤sT Xk)
be the rank of sT Xk in the combined sample sT X1,...,sT Xn,sT
1 Y1,...,sT Ym.
For ﬁxed s ∈Rp the distributions of sT X and sT Y can be compared using
a rank test. For example, if we use Wn,m(s) = Pn
i=1 Ri(s) our comparison is
done in terms of Wilcoxon’s rank sum statistics. It is well known that rank
tests are well suited for testing for univariate stochastic order [cf. H´ajek,
ˇSid´ak and Sen (1999), Davidov (2012)] where the restrictions that s ∈Sp−1
+
must be made. Although any rank test can be used, the Mann–Whitney form
of Wilcooxon’s (WMW) statistic is particularly attractive in this applica-
tion. Therefore in the rest of this paper we develop estimation and testing
procedures for the linear stochastic order based on the family of statistics
Ψn,m(s) =
1
nm
n
X
i=1
m
X
j=1
I(sT Xi≤sT Yj),
(3.1)
where s varies over Sp−1
+
. Note that (3.1) unbiasedly estimates
Ψ(s) = P(sT X ≤sT Y).
(3.2)
The following result is somewhat surprising.
Proposition 3.1.
Let X and Y be independent MVNs with means µ ≤
ν and common variance matrix Σ. Then Roy’s maximal separating direction
Σ−1(ν −µ) also maximizes P(sT X ≤sT Y).
Proposition 3.1 shows that the direction which separates the means, in
the sense of Roy, also maximizes (3.2). Thus it provides further support for
choosing (3.1) as our test statistic. Note that in general Σ−1(ν −µ) may not
belong to Sp−1
+
. Since we focus on the linear statistical order, we restrict our-
selves to s ∈Sp−1
+
. Consequently we deﬁne smax := arg maxs∈Sp−1
+
Ψ(s) and


## Page 8


8
O. DAVIDOV AND S. PEDDADA
refer to smax as the best separating direction. Further note that if X and
Y are independent and continuous and if X ⪯l-st Y, then Ψ(s) ≥1/2 for all
s ∈Sp−1
+
. This simply means that sT X tends to be smaller than sT Y more
than 50% of the time. Note that probabilities of type (3.2) were introduced
by Pitman (1937) and further studied by Peddada (1985) for comparing esti-
mators. Random variables satisfying such a condition are said to be ordered
by the precedence order [Arcones, Kvam and Samaniego (2002)].
Once smax is estimated we can plug it into (3.1) to get a test statistic.
Hence our test may be viewed as a natural generalization of Roy’s largest
root test from MVNs to arbitrary ordered distributions. However, unlike
Roy’s method, which does not explicitly estimate smax, we do. On the other
hand the proposed test does not require the computation of the inverse of
the sample covariance matrix whereas Roy’s test and Hotteling’s T 2 test
require such computations. Consequently, such tests cannot be used when
n < p whereas our test can be used in all such instances.
Remark 3.1.
In the above description Xi and Yj are independent for
all i and j and therefore the probability P(sT Xi ≤sT Yj) is independent of
both i and j. However, in many applications such as repeated measurement
and crossover designs, the data are a random sample of dependent pairs
(X1,Y1),...,(XN,YN) for which Zi = Yi −Xi are i.i.d. For example, such
a situation may arise when Yi = Y′
i + ǫi and Xi = X′
i + ǫi, where ǫi are
pair-speciﬁc random eﬀects and the RVs Y′
i (as well as X′
i) are i.i.d. In
this situation P(sT Xi ≤sT Yi) is independent of i and smax is well deﬁned.
Moreover the objective function analogous to (3.1) is
ΨN(s) = 1
N
N
X
i=1
I(sT Xi≤sT Yi).
(3.3)
In the following we consider both sampling designs which we refer to as:
(a) independent samples and (b) paired or dependent samples. Results are
developed primarily for independent samples, but modiﬁcation for paired
samples are mentioned as appropriate.
3.2. Estimating the best separating direction.
Consider ﬁrst the case of
independent samples, that is, X1,...,Xn and Y1,...,Ym are random sam-
ples from the two populations. Rewrite (3.1) as
Ψn,m(s) =
1
nm
n
X
i=1
m
X
j=1
I(sT Zij≥0),
(3.4)
where Zij = Yj −Xi. The maximizer of (3.4) is denoted by ˆsmax, that is,
ˆsmax = arg max
s∈Sp−1
+
Ψn,m(s).
(3.5)


## Page 9


INFERENCE FOR THE LINEAR STOCHASTIC ORDER
9
Finding (3.5) with s ∈Sp−1
+
is a nonsmooth optimization problem. Consider
ﬁrst the situation where p = 2. In this case we maximize (3.4) subject to
s ∈S1
+ = {(s1,s2):s2
1 + s2
2 = 1,(s1,s2) ≥0}. Geometrically S1
+ is a quarter
circle spanning the ﬁrst quadrant. Now let Z = (Z1,Z2), and without any
loss of generality assume that ∥Z∥= 1. We examine the behavior of the
function I(sT Z≥0) as a function of s. Clearly if Z ≥0, that is, if Z1 ≥0,Z2 ≥0,
then for all s ∈S1
+ we have I(sT Z≥0) = 1. In other words any value of s on
the arc S1
+ maximizes I(sT Z≥0). Similarly if Z < 0 then for all s ∈S1
+ we
have I(sT Z≥0) = 0 and again the entire arc S1
+ maximizes I(sT Z≥0). Now let
Z1 ≥0 and Z2 < 0. It follows that I(sT Z≥0) = 1 provided cos(sT Z) ≥0. Thus
I(sT Z≥0) = 1 for all s on the arc [0,θ] for some θ. If Z1 < 0 and let Z2 ≥0 the
situation is reversed and I(sT Z≥0) = 1 for all angles s on the arc [θ,π/2]. The
value of θ is given by (3.6). In other words each Z is mapped to an arc on
S1
+ as described above. Now, the function (3.4) simply counts the number of
arcs covering each s ∈S1
+. The maximizer of (3.4) lies in the region where the
maximum number of arcs overlap. Clearly this implies that the maximizer
of (3.4) is not unique. A quick way to ﬁnd the maximizer is the following:
Algorithm 3.1.
Let M denote the number of Zij’s which belong to
the second or fourth quadrant. Map
Zij 7→θij =

π/2 −cos−1(Zij,1),
if Zij,1 ≥0,Zij,2 < 0,
cos−1(Zij,1) −π/2,
if Zij,1 < 0,Zij,2 ≥0.
(3.6)
Relabel and order the resulting angles as θ[1] < ··· < θ[M]. Also deﬁne θ[0] = 0
and θ[M+1] = π/2. Evaluate Ψn,m(s[i]) i = 1,...,M where s[i],1 = cos(θ[i]) and
s[i],2 = sin(θ[i]). If a maximum is attained at θ[j], then any value in [θ[j−1],θ[j]]
or [θ[j],θ[j+1]] maximizes (3.1).
In light of the above discussion we can be easily prove the following:
Proposition 3.2.
For p = 2 Algorithm 3.1 maximizes (3.1).
In the general case, that is, for p ≥3, each observation Zij is associated
with a “slice” of Sp−1
+
. The boundaries of the slice are the intersection of
Sp−1
+
and some half-plane. Note that when p = 2 the slices are arcs. The
shape of the slice depends on the quadrant to which Zij belongs. The maxi-
mizer of (3.1) is again the value of s which belongs to the largest number of
slices. Although the geometry of the resulting optimization problem is easy
to understand, we have not been able to devise a simple algorithm, which
scales with p, based on the ideas above. However, we have found that (3.5)
can be obtained by converting the data into polar coordinates and then using
the Nelder–Mead algorithm which does not require the objective function


## Page 10


10
O. DAVIDOV AND S. PEDDADA
to be diﬀerentiable. We emphasize that this maximization process results
in a single maximizer of (3.1) and we do not attempt to ﬁnd the entire set
of maximizers. For completness we note that there are methods for opti-
mizing (3.1) speciﬁcally designed for nonsmooth problems. For more details
see Price, Reale and Robertson (2008) and Audet, B´echard and Le Diga-
bel (2008) and the references therein for both algorithms and convergence
results.
Remark 3.2.
It is clear that the estimation procedure for paired sam-
ples is the same as for independent samples.
3.3. Large sample behavior.
We ﬁnd three diﬀerent asymptotic regimes
for ˆsmax depending on distributional assumptions and the sampling scheme
(paired versus independent samples).
Note that the parameter space is the unit sphere not the usual Euclidian
space. There are several ways of dealing with this irregularity, one of which is
to re-express the last coordinate of s ∈Sp−1
+
as sp =
q
1 −s2
1 −··· −s2
p−1 and
consider the parameter space {s ≥0:s2
1 +···+s2
p−1 ≤1} which is a compact
subset of Rp−1. Clearly these parameterizations are equivalent, and without
any further ambiguity we will denote them both by Sp−1
+
. Thus in the proofs
below both views of Sp−1
+
are used interchangeably as convenient.
We begin our discussion with independent samples assuming continuous
distributions for both X and Y.
Theorem 3.1.
Let X and Y have continuously diﬀerentiable densities.
If Ψ(s) is uniquely maximized by smax ∈interior(Sp−1
+
). Then ˆsmax, the max-
imizer of (3.1), is strongly consistent, that is, ˆsmax
a.s.
→smax. Furthermore
ˆsmax = smax + Op(N −1/2) where N = n + m. Finally, if n/(n + m) →λ ∈
(0,1), then
N 1/2(ˆsmax −smax) ⇒N(0,Σ),
where the matrix Σ is deﬁned in the body of the proof.
Although (3.1) is not continuous (nor diﬀerentiable) its U-statistic struc-
ture guarantees that it is “almost” so [i.e., it is continuous up to an op(1/N)
term], and therefore its maximizer converges at a
√
N rate to a normal limit
[Sherman (1993)]. We also note that it is diﬃcult to estimate the asymptotic
variance Σ directly since it depends on unknown functions (∇ψj and ∇2ψj
for j = 1,2 are deﬁned in the body of the proof). Nevertheless bootstrap
variance estimates are easily derived.
Remark 3.3.
Note that if either X or Y are continuous RVs, then Ψ(s)
is continuous. This is a necessary condition for the uniqueness of smax.


## Page 11


INFERENCE FOR THE LINEAR STOCHASTIC ORDER
11
We have not been able to ﬁnd general condition(s) for a unique maximizer
for Ψ(s), although important suﬃcient conditions can be found. For example:
Proposition 3.3.
If Z = Y −X and there exist δ = ν −µ ≥0 and Σ
so the distribution of
sT Z −sT δ
√
sT Σs
is independent of s, then the maximizer of Ψ(s) is unique.
The condition above is satisﬁed by location scale families, and it may be
convenient to think of δ and Σ as the location and scale parameters for Z. In
general, however, Ψ(s) may not have a unique maximum nor be continuous.
For example, if both X and Y are discrete RVs, then Ψ(s) is a step function.
In such situations smax is set valued, and we may denote it by Smax. As we
have seen earlier the maximizer of Ψn,m(s) is always set valued (typically,
however, we ﬁnd only one maximizer). Consider, for example, the case where
P(X = (−1,−1)) = P(X = (1,1)) = 1/2 and let P(Y = (−1,−1)) = 1/2 −ε,
and P(Y = (1,1)) = 1/2+ ε for some ε > 0. It is clear that X ≺st Y. Further
note that Z ∈{(2,2),(0,0),(−2,−2)}, and it follows that Ψ(s) is constant on
S1
+ which implies that Smax coincides with S1
+. Similarly Ψn,m(s) is constant
on S1
+ and therefore ˆsmax ∈Smax for all n,m. This means that consistency is
guaranteed and the limiting distribution is degenerate. More generally, we
have:
Theorem 3.2.
If X and Y have discrete distributions with ﬁnite sup-
port and ˆsmax is a maximizer of (3.1), then
P(ˆsmax /∈Smax) ≤C1 exp(−C2N)
for some positive constants C1 and C2.
Theorem 3.2 shows that the probability that a maximizer of Ψn,m is not
in Smax is exponentially small when the underlying distributions of X and
Y are discrete. Hence ˆsmax is consistent and converges exponentially fast.
In fact the proof of Theorem 3.2 implies that ˆSmax →Smax; that is, the set
of maximizers of Ψn,m(·) converges to the set of maximizers of Ψ(·); that is,
ρH(ˆSmax,Smax) →0 where ρH is the Hausdroﬀmetric deﬁned on compact
sets. A careful reading of the proof shows that Theorem 3.2 also holds under
paired samples.
Finally, we consider the case of continuous RVs under paired samples.
Then under the conditions of Theorem 3.1 and provided the density of Z =
Y −X is bounded we have:
Theorem 3.3.
Under the above mentioned conditions ˆsmax, the maxi-
mizer of (3.3), is strongly consistent, that is, ˆsmax
a.s.
→smax, converges at a


## Page 12


12
O. DAVIDOV AND S. PEDDADA
cube root rate, that is, ˆsmax = smax + Op(N −1/3), and
N 1/3(ˆsmax −smax) ⇒W,
where W has the distribution of the almost surely unique maximizer of the
process s 7−→−[Q(s)+W(s)] on Sp−1
+
where Q(s) is a quadratic function and
W(s) is a zero mean Gaussian process described in the body of the proof.
Theorem 3.3 shows that in paired samples ˆsmax is consistent, but in con-
trast with Theorem 3.1 it converges at a cube-root rate to a nonnormal
limit. The cube root rate is due to the discontinuous nature of the objec-
tive function (3.3). General results dealing with this kind of asymptotics for
independent observations are given by Kim and Pollard (1990). The main
diﬀerence between Theorems 3.1 and 3.3 is that the objective function (3.1)
is smoothed by its U-statistic structure while (3.3) is not.
3.4. A conﬁdence set for ˆsmax.
Since the parameter space is the surface
of a unit sphere it is natural to deﬁne the (1 −α) × 100% conﬁdence set for
smax centered at ˆsmax by
{s ∈Sp−1
+
:ˆsT
maxs ≤Cα,N},
where Cα,N satisﬁes P(ˆsT
maxs ≤Cα,N) = 1 −α. For more details see Fisher
and Hall (1989) or Peddada and Chang (1996). Hence the conﬁdence set is
the set of all s ∈Sp−1
+
which have a small angle with ˆsmax. In theory one may
appeal to Theorem 3.1 to derive the critical value for any α ∈(0,1). However
the limit law in Theorem 3.1 requires knowledge of unknown parameters and
functions. For this reason, we explore the bootstrap for estimating Cα,N.
Remark 3.4.
Since in the case of paired samples, the estimator con-
verges at cube root rate rather than the square root rate, the standard boot-
strap methodology may yield inaccurate coverage probabilities; see Abrevaya
and Huang (2005) and Sen, Banerjee and Woodroofe (2010). For this reason
we recommend the “M out of N” bootstrap methodology. For further dis-
cussion on the “M out of N” bootstrap methodology one may refer to Lee
(1999), Delagdo, Rodriguez-Poo and Wolf (2001), Bickel and Sakov (2008).
3.5. Testing for order.
Consider ﬁrst the case of independent samples
where interest is in testing the hypothesis
H0 :X =st Y
versus
H1 :X ≺st Y.
(3.7)
Thus (3.7) tests whether the distributions of X and Y are equal or ordered
(later on we brieﬂy discuss testing H0 :X ⪯st Y versus H1 :X ⊀st Y). In
this section we propose a new test for detecting an ordering among two
multivariate distributions based on the maximal separating direction. The
test is based on the following observation:


## Page 13


INFERENCE FOR THE LINEAR STOCHASTIC ORDER
13
Theorem 3.4.
Let X and Y be independent and continuous RVs. If
X =st Y, then P(sT X ≤sT Y) = 1/2 for all s ∈Sp−1
+
, and if both (i) X ⪯st Y
and (ii) P(sT X ≤sT Y) > 1/2 for some s ∈Sp−1
+
hold, then X ≺st Y.
Theorem 3.4 says that if it is known a priori that {X ⪯st Y} = {X =st
Y}∪{X ≺st Y}, that is, the RVs are either equal or ordered [which is exactly
what (3.7) implies], then a strict linear stochastic ordering implies a strict
ordering by the usual multivariate stochastic order. In particular under the
alternative there must exist a direction s ∈Sp−1
+
for which sT X ≺l-st sT Y.
Remark 3.5.
The assumption that X ⪯st Y is natural in applications
such as environmental sciences where high exposures are associated with
increased risk. Nevertheless if the assumption that X ⪯st Y is not warranted
then the alternative hypothesis formulated in terms of the linear stochastic
order actually tests whether there exists a s ∈Sp−1
+
for which P(sT X ≤
sT Y) > 1/2. This amounts to a precedence (or Pitman) ordering between
sT X and sT Y.
Remark 3.6.
In the proof of Theorem 3.4 we use the fact that given
that X ⪯st Y we have X ≺st Y provided Xi ≺st Yi for some 1 ≤i ≤p. Note
that if Xi ≺st Yi, then E(Xi) < E(Yi). Thus it is possible to test (3.7) by
comparing means (or any other monotone function of the data). Although
such a test will be consistent it may lack power because tests based on
means are often far from optimal when the data is not normally distributed.
The WMW procedure, however, is known to have high power for a broad
collection of underlying distributions.
Hence (3.7) can be reformulated in terms of the linear stochastic. In par-
ticular it justiﬁes using the statistic
Sn,m = N 1/2(Ψn,m(ˆsmax) −1/2).
(3.8)
To the best of our knowledge this is the ﬁrst general test for multivariate
ordered distributions. In practice we ﬁrst estimate ˆsmax and then deﬁne
ˆUi = ˆsT
maxXi and ˆVj = ˆsT
maxYj where i = 1,...,n and j = 1,...,m. Hence
(3.8) is nothing but a WMW test based on the ˆU ′’s and ˆV ’s. It is also a
Kolmogorov–Smirnov type test.
The large sample distribution of (3.8) is given in the following.
Theorem 3.5.
Suppose the null (3.7) holds. Let n,m →∞and n/(n +
m) →λ ∈(0,1). Then
Sn,m ⇒S = sup
s∈Sp−1
+
G(s),
where G(s) is a zero mean Gaussian process with covariance function given
by (A.20).


## Page 14


14
O. DAVIDOV AND S. PEDDADA
Remark 3.7.
Since ˆsmax
a.s.
→smax by Slutzky’s theorem the power of
test (3.8) converges to the power of a WMW test comparing the samples
(sT
maxX1,...,sT
maxXn) and (sT
maxY1,...,sT
maxYm). The “synthetic” test, as-
suming that smax is known, serves as a gold standard as veriﬁed by our
simulation study.
Remark 3.8.
Furthermore, the power of the test under local alterna-
tives, that is, when Y =st X + N −1/2δ and N →∞is bounded by the
power of the WMW test comparing the distributions of sT
maxX and sT
maxY =
sT
maxX + N −1/2sT
maxδ.
Alternatives to the “sup” statistic (3.8) are the “integrated” statistics
In,m =
Z
s∈Sp−1
+
[N 1/2(Ψn,m(s) −1/2)]ds
and
(3.9)
I+
n,m =
Z
s∈Sp−1
+
[N 1/2(Ψn,m(s) −1/2)]+ ds,
where [x]+ = max(0,x). It is clear that In,m ⇒N(0,σ2) where
σ2 =
Z
u∈Sp−1
+
Z
v∈Sp−1
+
C(u,v)dudv
and C(u,v), the covariance function of G, is given by (A.20). Also
I+
n,m ⇒
Z
s∈Sp−1
+
[G(s)]+ ds.
This distribution does not have a closed form. The statistics In,m and I+
n,m
have univariate analogues; cf. Davidov and Herman (2012). Finally, we have
the following theorem:
Theorem 3.6.
The tests (3.8) and (3.9) are consistent. Furthermore if
X ⪯l-st Y ⪯l-st Z, then all three tests for H0 :X =st Z versus H1 :X ≺st Z are
more powerful than the respective tests for H0 :X =st Y versus H1 :X ≺st Y.
Theorem 3.6 shows that the tests are consistent and that their power
function is “monotone” in the linear stochastic order.
Remark 3.9.
Qualitatively similar results are obtainable in the paired
sampling case; the only diﬀerence being the limiting process. For example,
it easy to see that the paired sample analogue of (3.8) satisﬁes
N 1/2(ΨN(ˆsmax) −1/2) ⇒sup
s∈Sp−1
+
Q(s),


## Page 15


INFERENCE FOR THE LINEAR STOCHASTIC ORDER
15
where Q(s) is the empirical process on Sp−1
+
associated with (3.3). Analogues
of In,m and I+
n,m are similarly deﬁned and analyzed. Tests for paired samples
may be similarly implemented using bootstrap or permutation methods.
4. Simulations.
For simplicity of exposition, and motivated by the fact
that the example we analyzed in this paper deals with independent samples,
we limit our simulations to the case of independent samples.
4.1. The distribution of ˆsmax.
We start by investigating the distribution
of ˆsmax by simulation. For simplicity we choose p = 3 and generated Xi
(i = 1,...,n) distributed as N3(0,Σ) and Yj (j = 1,...,m) distributed as
N3(δ,Σ) where Σ = (1 −ρ)I + ρJ, I is the identity matrix and J is a square
matrix of 1s. We simulated 1000 realizations of ˆsmax for various sample
sizes and correlation coeﬃcients. To get a visual description of the density
of ˆsmax, we provide a pair of plots for each conﬁguration of ρ and sample
size n. In Figure 1 we provide the joint density of the two-dimensional polar
angles (θ,φ) of ˆsmax. There are four panels in Figure 1, corresponding to all
combinations of ρ = 0,0.9 and n = 10,100. The mean vector δ in this plot
was taken to be δ = (2,2,2)T . In Figure 2 we provide the density of the polar
residual deﬁned by 1 −ˆsT
max smax. The four panels of Figure 2 correspond
to all combinations of ρ = 0,0.9 and n = 10,100 and two patterns of δ,
namely, (2,2,2)T and (3,2,1)T . We see from Figure 1 that ˆsmax converges
to a unimodal, normal looking distribution as the sample size increases.
Interestingly, from Figure 2 we see that the concentration of the distribution
around the true parameter depends upon the values of δ and ρ (which
together determine smax). If the components of the underlying random vector
are exchangeable [e.g., δ = (2,2,2)T ], the residuals tend to concentrate more
closely around zero [Figure 2(a) and (c)] compared to the case when they
are not exchangeable [Figure 2(b) and (d)].
4.2. Study design.
The simulation study consists of three parts. In the
ﬁrst part we evaluate the accuracy and precision of ˆsmax by estimating its
bias and mean squared error (MSE). In the second part we investigate the
coverage probability of bootstrap conﬁdence intervals. In the third part we
estimate type I errors and powers of the proposed test Sn,m as well as the
integral tests In,m and I+
n,m.
To evaluate the bias and MSEs we generated X1,...,Xn ∼N3(0,Σ) and
Y1,...,Ym ∼N3(δ,Σ) where n = m = 20 or 100 observations. The common
variance matrix is assumed to have intra-class correlation structure, that is,
Σ = (1 −ρ)I + ρJ where I is the identity matrix and J is a matrix of ones.
Various patterns of the mean vectors δ and correlation coeﬃcient ρ were
considered as described in Table 1.


## Page 16


16
O. DAVIDOV AND S. PEDDADA
Fig. 1.
Plot of (simulated) polar angles.


## Page 17


INFERENCE FOR THE LINEAR STOCHASTIC ORDER
17
Fig. 2.
Plot of (simulated) polar residuals.


## Page 18


18
O. DAVIDOV AND S. PEDDADA
Table 1
Bias and MSE of ˆsmax
δ
ρ
Bias
MSE
n = m = 20
(1,1,1)
−0.25
0.001
0.072
(1,1,1)
0
0.004
0.129
(1,1,1)
0.25
0.009
0.187
(1,1,1)
0.50
0.012
0.216
(1,1,1)
0.90
0.010
0.203
(3,2,1)
−0.25
0.018
0.090
(3,2,1)
0
0.001
0.066
(3,2,1)
0.25
0.053
0.114
(3,2,1)
0.50
0.060
0.113
(3,2,1)
0.90
0.112
0.170
n = m = 100
(1,1,1)
−0.25
0.00009
0.014
(1,1,1)
0
0.00021
0.027
(1,1,1)
0.25
0.00045
0.041
(1,1,1)
0.50
0.00079
0.056
(1,1,1)
0.90
0.00050
0.044
(3,2,1)
−0.25
0.02400
0.039
(3,2,1)
0
0.00004
0.012
(3,2,1)
0.25
0.05200
0.065
(3,2,1)
0.50
0.06400
0.077
(3,2,1)
0.90
0.14100
0.158
We conducted extensive simulation studies to evaluate the performance of
the bootstrap conﬁdence intervals. In this paper we present a small sample
of our study. We generated data from two 5-dimensional normal populations
with means 0 and δ, respectively, and a common covariance Σ = (1 −ρ)I +
ρJ. We considered 5 patterns of ρ and 2 patterns of sample sizes (n = m = 20
and 40). The nominal coverage probability was 0.95. Results are summarized
in Table 2.
The goal of the third part of our simulation study is to evaluate the
type I error and the power of the test (3.8). To evaluate the type I error
three diﬀerent baseline distributions for the two populations X and Y were
employed as follows: (1) both distributed as N(0,Σ);(2) both distributed as
πN(0,Σ)+(1−π)N(δ,Σ) with π = 0.2 or π = 0.8; and (3) both distributed
as exp(Z) = (exp(Z1),...,exp(Zp)) where Z follows a N(δ,Σ). We refer
to this distribution as the multivariate lognormal distribution. Throughout
the variance matrix is assumed to have the intra-class structure described
above. Various patterns of the mean vectors δ and correlation coeﬃcient ρ


## Page 19


INFERENCE FOR THE LINEAR STOCHASTIC ORDER
19
Table 2
Coverage probabilities for the bootstrap conﬁdence intervals for
p = 5 normal data. Pattern i = 1,2 corresponds to
δ1 = (0.1,0.25,0.5,0.75,0.9) and δ2 = (0.5,0.5,0.5,0.5,0.5)
Set up
Coverage probability
Pattern
ρ
n = m = 20
n = m = 40
1
−0.25
0.981
0.971
1
0
0.913
0.918
1
0.25
0.916
0.933
1
0.50
0.971
0.969
1
0.90
0.993
0.989
2
−0.25
0.982
0.967
2
0
0.984
0.972
2
0.25
0.986
0.978
2
0.50
0.968
0.968
2
0.90
0.950
0.954
the dimension p were considered as described in Table 3. Sample sizes of
n = m = 15 or 25 are reported.
Power comparisons were carried out for data generated from X1,...,Xn ∼
Np(0,Σ) and Y1,...,Ym ∼Np(δ,Σ) where p = 3 or 5 and a variety of
patterns for δ as described in Table 4. If Roy’s maximal separating direction
(cf. Proposition 3.1) was known then a “natural gold standard” would be
the test based on Ψn,m(smax). We shall refer to this test as the true maximal
direction (TMD) test. Clearly the TMD test cannot be used in practice since
it involves the unknown direction smax. Nevertheless the TMD test provides
an upper bound for the power of the proposed test which uses the estimated
direction. Hence we compute the eﬃciency of the proposed test relative to
TMD test. An additional test, referred to as the RMD test is also compared.
The RMD test has the same form but uses Roy’s maximal direction given
by S−1( ¯Y −¯X). As suggested by a reviewer we also evaluated the power
of the two integral based tests, described in (3.9), which do not require the
determination of the best separating direction.
Additionally, in Table 5 we evaluate the type I error and power of our
test when X1,...,Xn ∼Np(0,Σ) and Y1,...,Ym ∼Np(δ,Σ) and n = m =
p = 10 and n = m = 10 and p = 20 (i.e., p < n set up). Note that in neither
of these cases the standard Hotteling’s T 2 (or Roy’s largest root test) can
be computed whereas the proposed test can be calculated.
Simulation results reported in this paper are based on 1000 simulation
runs. Conﬁdence sets are calculated using 1000 bootstrap samples. The boot-
strap critical values for estimating type I error were based on 500 bootstrap


## Page 20


20
O. DAVIDOV AND S. PEDDADA
Table 3
Type I errors for the proposed procedure with
nominal level α = 0.05. Three types of distributions are considered:
MVNs, MV-LogN (multivariate lognormal) and Mix-MVN
(mixtures of MVNs)
Set up
Type I error
Distribution
p
ρ
n = m = 15
n = m = 25
MVNs
3
−0.25
0.041
0.037
MVNs
3
0.00
0.023
0.044
MVNs
3
0.25
0.037
0.033
MVNs
3
0.50
0.027
0.032
MVNs
3
0.90
0.031
0.036
MVNs
5
−0.25
0.035
0.035
MVNs
5
0.00
0.040
0.041
MVNs
5
0.25
0.045
0.032
MVNs
5
0.50
0.038
0.043
MVNs
5
0.90
0.044
0.031
MV-LogN
3
−0.25
0.025
0.040
MV-LogN
3
0.00
0.038
0.049
MV-LogN
3
0.25
0.025
0.027
MV-LogN
3
0.50
0.028
0.037
MV-LogN
3
0.90
0.026
0.034
MV-LogN
5
−0.25
0.026
0.039
MV-LogN
5
0.00
0.035
0.018
MV-LogN
5
0.25
0.039
0.039
MV-LogN
5
0.50
0.036
0.046
MV-LogN
5
0.90
0.034
0.042
Mix-MVNs
3
−0.25
0.032
0.040
Mix-MVNs
3
0.00
0.038
0.028
Mix-MVNs
3
0.25
0.039
0.032
Mix-MVNs
3
0.50
0.036
0.035
Mix-MVNs
3
0.90
0.041
0.028
Mix-MVNs
5
−0.25
0.042
0.035
Mix-MVNs
5
0.00
0.040
0.031
Mix-MVNs
5
−0.25
0.041
0.028
Mix-MVNs
5
0.50
0.034
0.040
Mix-MVNs
5
0.90
0.042
0.036
samples. Since the results between 100 bootstrap samples and 500 boot-
strap samples did not diﬀer by much, all powers were estimated using 100
bootstrap samples.
4.3. Simulation results.
The Bias and MSEs for the patterns considered
are summarized in Table 1. It is clear that the bias decreases with the sample
size as do the MSEs. We observe that the bias tends to be smaller under


## Page 21


INFERENCE FOR THE LINEAR STOCHASTIC ORDER
21
Table 4
Type I errors and power for some settings with p ≥n. Here n = m = 10 and δ1 has
components 1/2 and δ2 has components i/p
Type I error and power p=10, n=m=10
Type I error and power p=20, n=m=10
δ
ρ
Type I error
δ
ρ
Type I error
0
0.00
0.054
0
0.00
0.081
0
0.25
0.051
0
0.25
0.050
0
0.50
0.028
0
0.50
0.046
0
0.90
0.038
0
0.90
0.048
Power
Power
δ1
0.00
0.83
δ1
0.00
0.97
δ1
0.25
0.48
δ1
0.25
0.53
δ1
0.50
0.26
δ1
0.50
0.42
δ1
0.90
0.20
δ1
0.90
0.22
δ2
0.00
0.98
δ2
0.00
0.98
δ2
0.25
0.80
δ2
0.25
0.59
δ2
0.50
0.67
δ2
0.50
0.43
δ2
0.90
0.71
δ2
0.90
0.40
independence and negative dependence compared with positive dependence.
It also tends to be smaller when the data are exchangeable. Although results
are not presented, we evaluated squared bias and MSE for larger values of
p (e.g., p = 5,10 and 20) and as expected the total squared bias and total
MSE increased with the dimension p.
In Table 2 we summarize the estimated coverage probabilities of the boot-
strap conﬁdence intervals when p = 5. Our simulation study suggests that
the proposed bootstrap methodology seems to perform better for larger sam-
ple sizes but rather poorly for smaller samples sizes.
Type I errors for diﬀerent patterns considered in our simulation study are
summarized in Table 3. Our simulation studies suggest that in every case
the proposed bootstrap based test maintains the nominal level of 0.05. In
general it is slightly conservative. The performance of the test is not aﬀected
by the shape of the underlying distribution. This is not surprising, owing to
the nonparametric nature of the test. Furthermore, we evaluated the type
I error of the proposed bootstrap test for testing the null hypothesis (3.7)
for p as large as 20 with n = m = 10 and discovered that the proposed test
attains the nominal level of 0.05 even n ≤p. See Table 4. As commented
earlier in the paper, Hotelling’s T 2 statistic cannot be applied here since the
Wishart matrix is singular in this case. However, the proposed method is
still applicable since the estimation of the best direction does not require
the inversion of a matrix.


## Page 22


22
O. DAVIDOV AND S. PEDDADA
Table 5
Power comparisons of the two proposed test procedures with type I error of 0.050. Here
δ1 = (0.1,0.5,0.9), δ2 = (0.1,0.25,0.5,0.75,0.9), δ3 = (0.5,0.5,0.5) and
δ4 = (0.5,0.5,0.5,0.5,0.5)
Power and RE % (n = m = 15)
Set up
Directional tests
Integral tests
p
δ
ρ
Sn,m
RMD test
TMD test
In,m
I+
n,m
3
δ1
−0.25
0.79 (90%)
0.62 (71%)
0.88
0.89 (100%)
0.89 (100%)
3
δ1
0.00
0.64 (82%)
0.45 (57%)
0.78
0.68 (87%)
0.68 (87%)
3
δ1
0.25
0.53 (78%)
0.38 (56%)
0.68
0.54 (79%)
0.54 (79%)
3
δ1
0.50
0.51 (73%)
0.41 (59%)
0.70
0.47 (67%)
0.47 (67%)
3
δ1
0.90
0.62 (64%)
0.85 (99%)
0.97
0.40 (41%)
0.41 (42%)
5
δ2
−0.25
0.93 (95%)
0.74 (76%)
0.98
0.97 (99%)
0.97 (99%)
5
δ2
0.00
0.80 (87%)
0.56 (60%)
0.92
0.86 (93%)
0.86 (93%)
5
δ2
0.25
0.59 (73%)
0.39 (47%)
0.81
0.66 (81%)
0.66 (81%)
5
δ2
0.50
0.56 (67%)
0.42 (50%)
0.84
0.48 (57%)
0.48 (57%)
5
δ2
0.90
0.63 (64%)
0.88 (89%)
0.99
0.40 (40%)
0.40 (40%)
3
δ3
−0.25
0.74 (89%)
0.54 (64%)
0.83
0.83 (100%)
0.83 (100%)
3
δ3
0.00
0.56 (87%)
0.34 (53%)
0.64
0.59 (92%)
0.59 (92%)
3
δ3
0.25
0.42 (87%)
0.23 (48%)
0.49
0.46 (93%)
0.46 (93%)
3
δ3
0.50
0.33 (86%)
0.15 (40%)
0.38
0.37 (97%)
0.37 (97%)
3
δ3
0.90
0.27 (83%)
0.12 (38%)
0.32
0.27 (83%)
0.27 (83%)
5
δ4
−0.25
0.92 (95%)
0.65 (68%)
0.96
0.95 (99%)
0.95 (99%)
5
δ4
0.00
0.75 (90%)
0.43 (51%)
0.83
0.82 (99%)
0.82 (99%)
5
δ4
0.25
0.49 (87%)
0.20 (35%)
0.57
0.60 (100%)
0.60 (100%)
5
δ4
0.50
0.41 (90%)
0.16 (34%)
0.45
0.43 (100%)
0.43 (100%)
5
δ4
0.90
0.29 (92%)
0.10 (32%)
0.31
0.33 (100%)
0.33 (100%)
The power of tests (3.8) and (3.9) for various patterns considered in our
simulation study are summarized in Table 5.
As expected, in every case the power of the TMD test is higher than
that of Sn,m test and the RMD test. The Sn,m test is almost always more
powerful than the RMD test. The relative eﬃciency of Sn,m compared to
the TMD test is quite high in most cases. When n = m = 15 the relative
eﬃciency ranges between 65–95%. It is almost always above 90% when the
sample size increases to 25 per group. In general the two integral tests had
very similar power. They had larger power than Sn,m when ρ < 0. As ρ
increased, the power of Sn,m improved relative to the two integral tests.
Test (3.8) seems to perform better when the components of δ were unequal.
We also note that when the integral tests outperform Sn,m the diﬀerence
is usually small, whereas the Sn,m test can outperform the integral tests
substantially. For example, observe pattern 2 where the powers of Sn,m and


## Page 23


INFERENCE FOR THE LINEAR STOCHASTIC ORDER
23
Table 5
(Continued)
Power and RE % (n = m = 25)
Set up
Directional tests
Integral tests
p
δ
ρ
Sn,m
RMD test
TMD test
In,m
I+
n,m
3
δ1
−0.25
0.96 (98%)
0.90 (91%)
0.98
0.98 (100%)
0.98 (100%)
3
δ1
0.00
0.85 (92%)
0.72 (78%)
0.92
0.85 (92%)
0.86 (92%)
3
δ1
0.25
0.80 (88%)
0.69 (76%)
0.90
0.75 (83%)
0.75 (83%)
3
δ1
0.50
0.75 (84%)
0.67 (75%)
0.89
0.66 (74%)
0.66 (74%)
3
δ1
0.90
0.89 (89%)
0.98 (99%)
1.00
0.59 (59%)
0.61 (61%)
5
δ2
−0.25
1.00 (100%)
0.98 (98%)
1.00
1.00 (100%)
1.00 (100%)
5
δ2
0.00
0.96 (97%)
0.85 (86%)
0.99
0.98 (99%)
0.98 (99%)
5
δ2
0.25
0.85 (88%)
0.74 (76%)
0.97
0.83 (86%)
0.83 (86%)
5
δ2
0.50
0.81 (84%)
0.74 (77%)
0.96
0.70 (73%)
0.70 (73%)
5
δ2
0.90
0.90 (90%)
0.99 (100%)
1.00
0.57 (57%)
0.58 (58%)
3
δ3
−0.25
0.94 (96%)
0.85 (87%)
0.98
0.96 (98%)
0.96 (98%)
3
δ3
0.00
0.75 (92%)
0.57 (69%)
0.82
0.79 (96%)
0.79 (96%)
3
δ3
0.25
0.62 (89%)
0.39 (56%)
0.70
0.66 (94%)
0.66 (94%)
3
δ3
0.50
0.54 (90%)
0.31 (52%)
0.60
0.55 (92%)
0.55 (92%)
3
δ3
0.90
0.44 (90%)
0.20 (42%)
0.49
0.42 (86%)
0.42 (86%)
5
δ4
−0.25
0.99 (99%)
0.94 (94%)
1.00
1.00 (100%)
1.00 (100%)
5
δ4
0.00
0.94 (96%)
0.72 (74%)
0.97
0.97 (100%)
0.97 (100%)
5
δ4
0.25
0.71 (90%)
0.41 (52%)
0.79
0.79 (100%)
0.79 (100%)
5
δ4
0.50
0.58 (91%)
0.25 (39%)
0.63
0.64 (100%)
0.64 (100%)
5
δ4
0.90
0.42 (87%)
0.18 (36%)
0.49
0.46 (94%)
0.46 (94%)
In,m are 0.93 and 0.97, respectively, when ρ = −0.25 and 0.63 versus 0.40
when ρ = 0.90.
5. Illustration.
Prior to conducting a two-year rodent cancer bioassay to
evaluate the toxicity/carcinogenicity of a chemical, the National Toxicology
Program (NTP) routinely conducts a 90-day pre-chronic dose ﬁnding study.
One of the goals of the 90-day study is to determine the maximum tolerated
dose (MTD) that can be used in the two-year chronic exposure study. Ac-
curate determination of the MTD is critical for the success of the two-year
cancer bioassay. Cancer bioassays are typically very expensive and time con-
suming. Therefore their proper design, that is, choosing the correct dosing
levels, is very important. When the highest dose used in the two-year study
exceeds the MTD, a large proportion of animals in the high dose group(s)
may die well before the end of the study, and the data from such group(s)
cannot be used reliably. This results in ineﬃciency and wasted resources.


## Page 24


24
O. DAVIDOV AND S. PEDDADA
Typically the NTP uses the 90-day study to determine the MTD on the
basis of a large number of correlated endpoints that provide information
regarding toxicity. These include body weight, organ weights, clinical chem-
istry (red blood cell counts, cell volume, hemoglobin, hematocrit, lympho-
cytes, etc.), histopathology (lesions in various target organs), number of
deaths and so forth. The dose response data is analyzed for each variable
separately using Dunnett’s or the Williams’s test (or their nonparametric
versions, Dunn’s test and Shirley’s test, resp.). NTP combines results from
all such analyses qualitatively and uses other biological and toxicological
information when making decisions regarding the highest dose for the two-
year cancer bioassay. Analyzing correlated variables one at a time may result
in loss of information. The proposed methodology provides a convenient
method to combine information from several outcome variables to make
comparisons between groups.
We now illustrate our methodology by re-analyzing data obtained from a
recent NTP study of the chemical Citral [NTP (2003)]. Citral is a ﬂavoring
agent that is widely used in a variety of food items. The NTP assigned a ran-
dom sample of 10 male rats to the control group and 10 to the 1785 mg/kg
dose group. Hematological and clinical chemistry measurements such as the
number of platelets (in 1000 per l), urea nitrogen (UN) (in mg/dl), alkaline
phosphatase (AP) (in IU/l) and bile acids (BA) (in mol/l) were recorded on
each animal at the end of the study. The NTP performed univariate anal-
ysis on each of these variables and found no signiﬁcant diﬀerence between
the control and dose group except for the concentration of urea nitrogen
which was increased in the high dose group. This increase was marginally
signiﬁcant at the 5% level and not at all after correcting for multiplicity. We
applied the proposed methodology to compare the control with the high-dose
group (1785 mg/kg) in terms of all nonnegative linear combinations of the
above mentioned four variables. We test the null hypothesis of no diﬀerence
between the control and the high-dose group against the alternative that the
high-dose group is stochastically larger (in the above four variables) than
the control group. The resulting p-value based on 10,000 bootstrap samples
was 0.025, which is signiﬁcant at a 5% level of signiﬁcance. The estimated
value of smax was (0.074,0.986,0.012,0.150)T and the estimated 95% conﬁ-
dence region is given by {s ∈Sp−1
+
:ˆsT
maxs ≤0.93}. Hence the conﬁdence set
includes any s which is within 21.5◦degrees of ˆsmax. This is a relatively
large set due to the small sample sizes. Clearly our methodology appears to
be sensitive to detect statistical diﬀerences which were not noted by NTP.
Furthermore, our methodology allows us to infer that indeed 1785 mg/kg
dose group is larger in the multivariate stochastic order than the control
group. This is a much stronger conclusion than the simple ordering of their
means. Thus we believe that the proposed framework and methodology for
studying ordered distributions can serve as a useful tool in toxicology and is
also applicable to a wide range of other problems as alluded to in this paper.


## Page 25


INFERENCE FOR THE LINEAR STOCHASTIC ORDER
25
6. Concluding remarks and some open problems.
In many applications,
researchers are interested in comparing two experimental conditions, for ex-
ample, a treatment and a control group, in terms of a multivariate response.
In classical multivariate analysis one addresses such problems by comparing
the mean vectors using Hotelling’s T 2 statistic. The assumption of MVN,
underlying Hotelling’s T 2 test, may not hold in practice. Moreover if the
data is not MVN, then the comparison of population means may not al-
ways provide complete information regarding the diﬀerences between the
two experimental groups. Secondly, Hotelling’s T 2 statistics are designed for
two-sided alternatives and may not be ideal if a researcher is interested in
one-sided, that is, ordered alternatives. Addressing such problems requires
one to compare the two experimental groups nonparametrically in terms of
the multivariate stochastic order. Such comparisons, however, are very high
dimensional and not easy to perform.
In this article we circumvent this challenge by considering the notion of
the linear stochastic order between two random vectors. The linear stochas-
tic order is a “weak” generalization of the univariate stochastic order. The
linear stochastic order is simple to interpret and has an intuitive appeal.
Using this notion of ordering, we developed nonparametric directional infer-
ence procedures. Intuitively, the proposed methodology seeks to determine
the direction that best separates two multivariate populations. Asymptotic
properties of the estimated direction are derived. Our test based on the best
separating direction may be viewed as a generalization of Roy’s classical
largest root test for comparing several MVN populations. To the best of our
knowledge this is the ﬁrst general test for multivariate ordered distributions.
Since in practice sample sizes are small, we use the bootstrap methodology
for drawing inferences.
We illustrated the proposed methodology using a data obtained from a
recent toxicity/carcinogenicity study conducted by the US National Toxi-
cology Program (NTP) on the chemical Citral. A re-analysis of their 90-day
data using our proposed methodology revealed a linear stochastic increase
in platelets, urea nitrogen, alkaline phosphatase and bile acids in the high-
dose group relative to the control group, which was not seen in the original
univariate analysis conducted by the NTP. These ﬁndings suggest that the
proposed methodology may have greater sensitivity than the commonly used
univariate statistical procedures. Our methodology is suﬃciently general
since it is nonparametric and can be applied to discrete and/or continuous
outcome variables. Furthermore, our methodology exploits the underlying
dependence structure in the data, rather than analyzing one variable at a
time.
We note that our example and some of our results pertain to continuous
RVs. However, the methodology may be used, with appropriate modiﬁcation
(e.g., methods for dealing with ties) with discrete (or mixed) data with


## Page 26


26
O. DAVIDOV AND S. PEDDADA
no problem. Although the focus of this paper has been the comparison of
two multivariate vectors, in many applications, especially in dose response
studies, researchers may be interested in determining trends (order) among
several groups. Similarly to classical parametric order restricted inference
literature, one could generalize the methodology developed in this paper
to test for order restrictions among multiple populations. For example, one
could extend the results to K ≥2 RVs ordered by the simple ordering, that
is, X1 ≺l-st X2 ≺l-st ··· ≺l-st XK or to RVs ordered by the tree ordering,
that is, X1 ≺l-st Xj where j = 2,...,K. As pointed out by a referee the
hypotheses H0 :X ⪯st Y versus H1 :X ⊀st Y can also be formulated and
tested using the approach described. First note that the null hypothesis
implies Ψ(s) ≥1/2 for all s ∈Sp−1
+
. On the other hand under the alternative
there is an s ∈Sp−1
+
for which Ψ(s) < 1/2. Thus a test may be based on the
statistic
N 1/2(Ψn,m(ˆsmin) −1/2),
where ˆsmin is the value which minimizes Ψn,m(s). It is also clear that the
least favorable conﬁguration occurs when Ψ(s) = 1/2 for all s ∈Sp−1
+
which
is equivalent to X =st Y.
We believe that the result obtained here may be useful beyond order
restricted inference. Our simulation study suggests that our estimator of the
best separating direction, that is, (3.5) may be useful even in the context of
classical multivariate analysis where it may be viewed as a robust alternative
to Roy’s classical estimate. Finally we note that the linear stochastic order
may be useful in a variety of other statistical problems. For example, we
believe that it provides a useful framework for linearly combining the results
of several diagnostic markers. This is a well-known problem in the context
of ROC curve analysis in diagnostic medicine.
APPENDIX: PROOFS
Proof of Theorem 2.1.
(i) Let g :Rp →Rn be an aﬃne increasing
function. Clearly g(x) = v + Mx for some n vector v and n × p matrix M
with nonnegative elements. Thus for any u ∈Rn
+ we have s = MT u ∈Rp
+.
Hence
uT g(X)=uT (v+MX)=uT v+sT X ⪯st uT v+sT Y=uT (v+MY)=uT g(Y)
as required where the inequality holds because X ⪯l-st Y. (ii) Fix I ∈{1,... ,
p}. Let X = (XI,X¯I), Y = (YI,Y¯I) where ¯I is the complement of I in
{1,... ,p}. Further deﬁne sT = (sT
I ,sT¯I ) where s ∈Rp
+, and set sT¯I = 0. It
follows that for all sI ∈Rdim(I) we have
sT
I XI = sT X ⪯st sT Y = s
T
I YI


## Page 27


INFERENCE FOR THE LINEAR STOCHASTIC ORDER
27
as required. (iii) Let φ:R →R be any increasing function. Note that
E(φ(sT X)) = E(E(φ(sT X)|Z)) ≤E(E(φ(sT Y)|Z)) = E(φ(sT Y)).
The inequality is a consequence of X|Z = z ⪯l-st Y|Z = z. Since φ is arbi-
trary it follows that X ⪯l-st Y as required. (iv) Let X = (X1,...,Xn), and
deﬁne Y similarly. Let s ∈Rp
+ where p = p1 + ··· + pn. Now
sT X = sT
1 X1 + ··· + sT
nXn
and
sT Y = sT
1 Y1 + ··· + sT
nYn
by assumption sT
i Xi ⪯st sT
i Yi for i = 1,...,n. In addition sT
i Xi and sT
j Xj
are independent for i ̸= j. It follows from Theorem 1.A.3 in Shaked and
Shanthikumar (2007) that sT
1 X1 + ··· + sT
nXn ⪯st sT
1 Y1 + ··· + sT
nYn, that
is, X ⪯l-st Y as required. (v) By assumption Xn ⇒X and Yn ⇒Y where the
symbol ⇒denotes convergence in distribution. By the continuous mapping
theorem sT Xn ⇒sT X and sT Yn ⇒sT Y. It follows that
P(sT Xn ≥t) →P(sT X ≥t)
and
P(sT Yn ≥t) →P(sT Y ≥t).
(A.1)
Moreover since Xn ⪯l-st Yn we have
P(sT Xn ≥t) ≤P(sT Yn ≥t)
for all n ∈N.
(A.2)
Combining (A.1) and (A.2) we have P(sT X ≥t) ≤P(sT Y ≥t), that is,
X ⪯l-st Y as required.
□
Before proving Theorem 2.2, we provide a deﬁnition and a preliminary
lemma.
Definition A.1.
We say that the RV X has an elliptical distribution
with parameters µ and Σ and generator φ(·), denoted X ∼Ep(µ,Σ,φ), if
its characteristic function is given by exp(itT µ)φ(tT Σt).
For this and other facts about elliptical distributions which we use in the
proofs below, see Fang, Kots and Ng (1989).
Lemma A.1.
Let X ∼E1(µ,σ,φ) and Y ∼E1(µ′,σ′,φ) be univariate
elliptical RVs supported on R. Then X ⪯st Y if and only if µ ≤µ′ and σ = σ′.
Proof.
Since X and Y have the same generator they have the stochastic
representation:
X =st µ + σRU
and
Y =st µ′ + σ′RU,
(A.3)
where R is a nonnegative RV, independent of the RV U, satisfying P(U =
±1) = 1/2; cf. Fang, Kots and Ng (1989). It follows that RU is a symmetric
RV supported on R with a strictly increasing DF which we denoted by F0.
Let FX and FY denote the DFs of X and Y , respectively. Note that X ⪯st Y
if and only if FX(t) ≥FY (t) for all t ∈R, or equivalently by (A.3), if and


## Page 28


28
O. DAVIDOV AND S. PEDDADA
only if
F0
t −µ
σ

≥F0
t −µ′
σ′

(A.4)
for all t ∈R. It is obvious that (A.4) holds when µ ≤µ′ and σ = σ′, estab-
lishing suﬃciency. Now assume that X ⪯st Y . Put t = µ in (A.4), and use
the strict monotonicity of F0 to get 0 ≥(µ −µ′)/σ′, that is, µ′ ≥µ. Suppose
now that σ′ > σ. It follows from (A.4) and the the strict monotonicity of F0
that (t −µ)/σ ≥(t −µ′)/σ′ which is equivalent to t ≥(µσ′ −µ′σ)/(σ′ −σ).
The latter, however, contradicts the fact that (A.4) holds for all t ∈R. A
similar argument shows that σ′ < σ cannot hold; hence we must have σ = σ′
as required.
□
Remark A.1.
Note that Lemma A.1 may not hold for distributions
with a ﬁnite support. For example, if R ∼U(0,1), then by (A.3) X ∼U(µ −
σ,µ + σ) and Y ∼U(µ′ −σ′,µ′ + σ′). It is easily veriﬁed that in this case
X ⪯st Y if and only if ∆= µ′ −µ ≥0 and −∆≤σ′ −σ ≤∆; that is, it is not
required that σ = σ′. Hence the assumption that X and Y are supported on
R is necessary.
We continue with the proof of Theorem 2.2.
Proof of Theorem 2.2.
Let X and Y be be Ep(µ,Σ,φ) and Ep(µ′,
Σ′,φ) supported on Rp. Suppose that X ⪯l-st Y. Choose s = ei where eik = 1
if i = k and 0 otherwise. It now follows from Deﬁnition 1.1 that Xi ⪯st Yi.
Since Xi and Yi are marginally elliptically distributed RVs with the same
generator and supported on R, then by Lemma A.1 we must have
µi ≤µ′
i
and
σii = σ′
ii.
(A.5)
The latter holds, of course, for all 1 ≤i ≤p. Choosing s = ei + ej we have
Xi + Xj ⪯st Yi + Yj. Note that Xi + Xj and Yi + Yj are supported on R and
follow a univariate elliptical distribution with the same generator [Fang,
Kots and Ng (1989)]. Applying Lemma A.1 again we ﬁnd that
µi + µj ≤µ′
i + µ′
j
and
σii + σjj + 2σij = σ′
ii + σ′
jj + 2σ′
ij.
(A.6)
The latter holds, of course, for all 1 ≤i ̸= j ≤p. It is easy to see that equa-
tions (A.5) and (A.6) imply that µ ≤µ′ and Σ = Σ′. Recall [cf. Fang, Kots
and Ng (1989)] that we may write X =st µ + RSU and Y =st µ′ + RSU
where Σ = ST S, U is a uniform RV on Sp−1
+
, and R is a nonnegative RV.
Let S be an upper set in Rp. Clearly the set [S −µ] := {x−µ :x ∈S} is also
an upper set and [S −µ] ⊆[S −µ′] since µ ≤µ′. Now,
P(X ∈S) = P(X0 ∈[S −µ]) ≤P(X0 ∈[S −µ′]) = P(Y ∈S),
where X0 = RSU, hence X ⪯st Y. This proves the “if” part. The “only if”
part follows immediately.
□


## Page 29


INFERENCE FOR THE LINEAR STOCHASTIC ORDER
29
Proof of Theorem 2.3.
Let Xp = {x:(x1,...,xp) ∈{0,1}p} denote
the support of a p-dimensional multivariate binary (MVB) RV. By deﬁnition
the relationship X ⪯l-st Y implies that for all (t,s) ∈R+ × Rp
+,
P(sT X > t) ≤P(sT Y > t).
(A.7)
Now note that
P(sT X > t) =
X
x∈Xp
f(x)I(sT x>t)
and
P(sT Y > t) =
X
x∈Xp
g(x)I(sT x>t),
(A.8)
where f and g are the probability mass functions of X and Y, respectively.
Let U be an upper set on Xp. It is well known [cf. Davey and Priestley
(2002)] that U can be written as
U =
[
j∈J
U(xj),
(A.9)
where xj are the distinct minimal elements of U, and U(xj) = {x:x ≥xj}
are themselves upper sets [in fact U(xj) is an upper orthant]. The set {xj :
j ∈J} is often referred to as an anti-chain. Now observe that for any s ∈Rp
+
the set {x:sT x > t} is an upper set. Hence it must be of the form of (A.9)
for some anti-chain {xj : j ∈J}. Suppose now, that for some U ∈Xp there
is a vector sU ∈Rp
+ such that U = {x:sT
Ux > t} for some ﬁxed t > 0. Then
using (A.7) and (A.8) we have
P(X ∈U) =
X
x∈{x : sT
Ux>t}
f(x) = P(sT
UX > t) ≤P(sT
UY > t)
=
X
x∈{x : sT
Ux>t}
g(x) = P(Y ∈U).
We will complete the proof by showing that for each upper set U ∈Xp, we can
ﬁnd a vector sU for which sT
Ux > t for x ∈U and sT
Ux ≤t for x ∈U c = X \ U
if and only if p ≤3. To do so we will ﬁrst solve the system of equations
sT xj = t for j ∈J. This system can also be written as Xs = t where
X =


x1...
xJ


is a J × p matrix whose rows are the member of the anti-chain deﬁning
U, and t = (t,...,t) has dimension J. Clearly the elements of X are ones
and zeros. If J ≤p, the matrix X is of full rank since its rows are linearly
independent by the fact that they are an anti-chain. Hence a solution for
s exists. With a bit of algebra, we can further show that a solution s ≥0


## Page 30


30
O. DAVIDOV AND S. PEDDADA
exists. This, of course, is trivially veriﬁed when p ≤3. Now set sU = s + ε
for some ε ≥0. It is clear that we can choose ε small enough to guarantee
that sT
Ux > t if and only if x ∈U. Hence if J ≤p, upper set (A.9) can be
mapped to a vector sU. However, the inequality J ≤p for all upper sets
U ⊂Xp holds if and only if p ≤3. This can be easily shown by enumerating
all 18 upper sets belonging to X3 [cf. Davidov and Peddada (2011)] and
noting that they have at most three minimal elements. Hence if p ≤3, then
X ⪯l-st Y ⇐⇒X ⪯st Y as required.
Now let p = 4, and consider the upper set U generated by the anti-chain
xj, j = 1,...,J where xj are all the distinct permutations of the vector
(1,1,0,0). Clearly J = 6. Note that although J > p, the system of equations
Xs = t is uniquely solved by sT
∗= (t/2,t/2,t/2,t/2). However, this solution
coincides with the solution of the system X′s = t where X′ is any matrix
obtained from X by deleting any two (or just one) of its rows. Note that
the rows of X′ correspond to an upper set U ′ ⊂U. This, in turn, implies
that for any such U ′ one cannot ﬁnd a vector sU′ satisfying sT
U′x > t if and
only if x ∈U ′ because the inequality will hold for all x ∈U. Thus U ′ does
not deﬁne an upper half plane. This shows that the linear stochastic order
and the multivariate stochastic order do not coincide when p = 4. A similar
argument may be used for any p ≥5. This completes the proof.
□
We ﬁrst deﬁne the term copula.
Definition A.2.
Let F be the DF of a p-dimensional RV with marginal
DFs F1,...,Fp. The copula C associated with F is a DF such that
F(x) = C(x) = C(F1(x1),...,Fp(xp)).
It follows that the tail-copula ¯C(·) is nothing but the tail of the DF C(·).
Proof of Theorem 2.4.
Suppose that X and Y have the same copula.
Let X ⪯l-st Y. Choosing s = ei where eik = 1 if i = k and 0 otherwise, we
ﬁnd using the deﬁnition that Xi ⪯st Yi. The latter holds, of course, for all
1 ≤i ≤p. Applying Theorem 6.B.14 in Shaked and Shanthikumar (2007),
we ﬁnd that X ⪯st Y. The reverse direction is immediate.
□
Proof of Theorem 2.5.
Note that for any x ∈Rp we have
F(x) = CX(F1(x1),...,Fp(xp)) ≥CX(G1(x1),...,Gp(xp))
≥CY(G1(x1),...,Gp(xp)) = G(x).
This means that X ⪯lo Y. The other part of the theorem is proved similarly.
□


## Page 31


INFERENCE FOR THE LINEAR STOCHASTIC ORDER
31
Proof of Proposition 3.1.
Let X and Y be independent MVNs with
means µ ≤ν and common variance matrix Σ. Clearly
P(sT X ≤sT Y) = Φ

−sT (µ −ν)
√
2sT Σs

,
where Φ is the DF of a standard normal RV. It follows that P(sT X ≤sT Y)
is maximized when the ratio sT (ν −µ)/
√
sT Σs is maximized. From the
Cauchy–Schwarz inequality we have
sT (ν −µ)
√
sT Σs
≤
q
(ν −µ)T Σ−1(ν −µ)
(A.10)
for all s. It is now easily veriﬁed that s = Σ−1(ν −µ) maximizes the left-
hand side of (A.10).
□
Proof of Proposition 3.2.
Let Qq, q = 1,...,4, be the four quad-
rants. It is clear that maximizing (3.1) is equivalent to maximizing
Ψ′
n,m(s) =
X
Zij∈Q2
I(sT Zij≥0) +
X
Zij∈Q4
I(sT Zij≥0).
(A.11)
It is also clear that for any s the indicators I(sT Zij≥0) are independent of
the length of Zij which we therefore take to have length unity. Observe that
the value of (A.11) is constant in the intervals (θ[i],θ[i+1]) where θ[i] are
deﬁned in Algorithm 3.1. At each point θ[i], i = 0,...,M + 1, the value of
(A.11) may increase or decrease. It follows that for all s ∈Sp−1
+
Ψ′
n,m(s) ∈
{Ψ′
n,m(s[0]),...,Ψ′
n,m(s[M+1])} where s[i] are deﬁned in Algorithm 3.1. There-
fore the maximum value of (3.1) is an element of the above list. Now sup-
pose that s[i] is a global maximizer of (A.11). Clearly either Ψ′
n,m(s[i]) =
Ψ′
n,m(s[i−1]) or Ψ′
n,m(s[i]) = Ψ′
n,m(s[i+1]) must hold, in which case any value
in [θ[i−1],θ[i]] or [θ[i],θ[i+1]] is a global maximizer. This concludes the proof.
□
Proof of Theorem 3.1.
Using Hajek’s projection and for any s, we
may write
Ψn,m(s) = Ψ(s) + n−1
n
X
i=1
ψ1(Xi,s) + m−1
m
X
j=1
ψ2(Yj,s) + Rn,m(s),
(A.12)
where
ψ1(Xi,s) = ¯G(sT Xi) −Ψ(s),
ψ2(Yj,s) = F(sT Yj) −Ψ(s)
and Rn,m(s) is a remainder term. Here ¯G(sT x) = P(sT Y ≥sT x), F(sT y) =
P(sT X ≤sT y) and Ψ(s) = E( ¯G(sT Xi)) = E(F(sT Yj)). Clearly E[ψ1(Xi,s)] =


## Page 32


32
O. DAVIDOV AND S. PEDDADA
E[ψ2(Yj,s)] = 0 for all i and j, so by the strong law of large numbers
n−1 Pn
i=1 ψ1(Xi,s) and m−1 Pm
j=1 ψ2(Yj,s) both converge to zero with prob-
ability one. Now,
sup
s∈Sp−1
+
|Ψn,m(s) −Ψ(s)| ≤sup
s∈Sp−1
+
n−1
n
X
i=1
ψ1(Xi,s)
 + sup
s∈Sp−1
+
m−1
m
X
j=1
ψ2(Yj,s)

+ sup
s∈Sp−1
+
|Rn,m(s)|.
The set Sp−1
+
is compact, and the function ψ1(x,s) is continuous in s ∈Sp−1
+
for all values of x and bounded [in fact |ψ1(x,s)| ≤2]. Thus the condi-
tions in Theorem 3.1 in DasGupta (2008) are satisﬁed, and it follows that
sups∈Sp−1
+
|n−1 Pn
i=1 ψ1(Xi,s)| a.s.
→0 as n →∞. Similarly sups∈Sp−1
+
|m−1 ×
Pm
i=1 ψ2(Yi,s)| a.s.
→0 as m →∞. Since Ψn,m(s) is bounded all its moments
exist; therefore from Theorem 5.3.3 in Serﬂing (1980) we have that with
probability one Rn,m(s) = o(1/N). Moreover it is clear that the latter holds
uniformly for all s. Thus,
sup
s∈Sp−1
+
|Ψn,m(s) −Ψ(s)| a.s.
→0
as n,m →∞.
By assumption Ψ(smax) > Ψ(s) for all s ∈Sp−1
+
\ smax so we can apply The-
orem 2.12 in Kosorok (2008) to conclude that
ˆsmax
a.s.
→smax;
that is, ˆsmax is strongly consistent. This completes the ﬁrst part of the proof.
Since the densities of X and Y are diﬀerentiable, it follows that Ψ(s) is
continuous and twice diﬀerentiable. In particular at smax ∈Sp−1
+
, the matrix
−∇2Ψ(smax) exists and is positive deﬁnite. A Taylor expansion implies that
sup
∥s−smax∥<δ
Ψ(s) −Ψ(smax) ≤−Cδ2.
It is also obvious that
n−1
n
X
i=1
ψ1(Xi,smax) = Op(1/
√
N)
and
m−1
m
X
j=1
ψ2(Yj,smax) = Op(1/
√
N).
Finally as noted above |Rn,m(s)| = O(1/N) for all s as n,m →∞. There-
fore by Theorem 1 in Sherman (1993) we have that
ˆsmax = smax + Op(N −1/2);
(A.13)


## Page 33


INFERENCE FOR THE LINEAR STOCHASTIC ORDER
33
that is, ˆsmax converges to smax at a N 1/2 rate. This completes the second
part of the proof.
The functions Ψ(s),ψ1(Xi,s) and ψ2(Yj,s) on the right-hand side of
(A.12) all admit a quadratic expansion. A bit of algebra shows that for
s in an Op(N −1/2) neighborhood of smax, we have
Ψn,m(s) = Ψ(smax) + (s −smax)T Mn,m
N 1/2
(A.14)
+ 1
2(s −smax)T V(s −smax) + op(1/N),
where
Mn,m =
1
p
λn,m
Pn
i=1 ∇ψ1(Xi,smax)
n1/2
+
1
p
1 −λn,m
Pm
j=1 ∇ψ2(Yj,smax)
m1/2
λn,m = n/N, for j = 1,2 the function ∇ψj(·,smax)T is the gradient of ψj(·,s)
evaluated at smax, and the matrix V is given by
V = E(∇2ψ1(X,smax)) + E(∇2ψ2(Y,smax)).
Note that the op(1/N) term in (A.14) absorbs Rn,m(s) in (A.12) as well as
the higher-order terms in the quadratic expansions of Ψ(s),n−1 Pn
i=1 ψ1(Xi,s)
and m−1 Pm
j=1 ψ2(Yj,s). Now by the CLT and Slutzky’s theorem, we have
that
Mn,m ⇒N(0,∆),
where
∆= 1
λE(∇ψ1(X,smax)∇ψ1(X,smax)T )
+
1
1 −λE(∇ψ2(Y,smax)∇ψ2(Y,smax)T ).
Finally it follows by Theorem 2 in Sherman (1993) that
N 1/2(ˆsmax −smax) ⇒N(0,Σ),
where Σ = V−1∆V −1, completing the proof.
□
Proof of Theorem 3.2.
Suppose that X and Y are discrete RVs
with ﬁnite support. Let pa = P(X = xa) > 0 and qb = P(Y = yb) > 0 where
a = 1,...,A and b = 1,...,B; A and B are ﬁnite. Deﬁne the set Sab = {s ∈
Sp−1
+
:sT xa ≤sT yb}. A simple argument shows that
Ψ(s) = P(sT X ≤sT Y) =
A
X
a=1
B
X
b=1
I(s∈Sab)paqb =
K
X
k=1
αkI(s∈Sk),


## Page 34


34
O. DAVIDOV AND S. PEDDADA
where K ≤2AB is ﬁnite, the sets Sk are distinct, SK
k=1 Sk = Sp−1
+
and
αk = P
(a,b)∈Jk paqb with Jk = {(a,b):Sk ∩Sab ̸= ∅}. Thus Ψ(s) is a sim-
ple function on Sp−1
+
, and Smax is the set associated with the largest αk. We
will assume, without any loss of generality, that α1 > αk for all k ≥2. Now
note that
Ψn,m(s) =
1
nm
n
X
i=1
m
X
j=1
I(sT Xi≤sT Yj) =
A
X
a=1
B
X
b=1
namb
nm I(s∈Sab),
where na = Pn
i=1 I(Xi=xa),mb = Pm
j=1 I(Yi=yb) where a = 1,...,A and b =
1,...,B. Clearly Ψn,m(s) is also a simple function. Moreover for large enough
n and m we will have na > 0 and mb > 0 for all a = 1,...,A and b = 1,...,B,
and consequently Ψn,m(s) is deﬁned over the same sets as Ψ(s), that is,
Ψn,m(s) =
K
X
k=1
ˆαkI(s∈Sk),
where ˆαk = P
(a,b)∈Jk ˆpaˆqb with ˆpa = na/n and ˆqb = mb/m. Furthermore the
maximizer of Ψn,m(s) is any s ∈Sk provided that Sk is associated with the
largest ˆαk. Hence,
P(ˆsmax /∈Smax) = P

arg max
1≤k≤K ˆαk ̸= 1

= P
 K
[
k=2
{ˆα1 ≤ˆαk}
!
(A.15)
≤
K
X
k=2
P(ˆα1 ≤ˆαk) ≤(K −1) max
2≤k≤K P(ˆα1 ≤ˆαk).
A bit of rearranging shows that
P(ˆα1 ≤ˆαk) = P
 X
(a,b)∈J1
ˆpaˆqb −
X
(a,b)∈Jk
ˆpaˆqb ≤0

= P
 
n−1m−1
n
X
i=1
m
X
j=1
Z(k)
ij ≤0
!
,
where
Z(k)
ij =
X
(a,b)∈J1\Jk
I(Xi=xa)I(Yj=yb) −
X
(a,b)∈Jk\J1
I(Xi=xa)I(Yj=yb).
Note that Z(k)
ij
may be viewed as a kernel of a two sample U-statistic. More-
over
−|Jk \ J1| ≤Z(k)
ij ≤|Jk \ J1|
is bounded (here | · | denotes set cardinality) and E(Z(k)
ij ) = µk = E(ˆα1 −
ˆαk) > 0 by assumption. Applying Theorem 2 and the derivations in Sec-


## Page 35


INFERENCE FOR THE LINEAR STOCHASTIC ORDER
35
tion 5b in Hoeﬀding (1963) we have that
P
 
n−1m−1
n
X
i=1
m
X
j=1
Z(k)
ij ≤0
!
≤exp

−N min(λn,m,1 −λn,m)µ2
k
2(|Jk \ J1| + |J1 \ Jk|)2

,
(A.16)
where λn,m = n/N →λ ∈(0,1) as n,m →∞. Finally from (A.15) and (A.16)
we have that
P(ˆsmax /∈Smax) ≤C1 exp(−C2N),
where C1 = K −1 and C2 = min(λ,1 −λ)min 2µ2
k(|Jk \ J1| + |J1 \ JK|)−2
completing the proof.
□
Proof of Theorem 3.3.
Choose ε > 0. We have already seen that
under the stated conditions, Ψ(s) is continuous, and therefore for each s the
set Bs,ε = {s′ :|Ψ(s′) −Ψ(s)| < ε} is open. The collection {Bs,ε :s ∈Sp−1
+
} is
an open cover for Sp−1
+
. Since Sp−1
+
is compact there exists a ﬁnite subcover
Bs1,ε,...,BsK ,ε for Sp−1
+
where K < ∞. Hence each s belongs to some Bsi,ε
and therefore
sup
s∈Sp−1
+
|ΨN(s) −Ψ(s)|
≤max
1≤i≤K sup
s∈Bsi,ε
|ΨN(s) −ΨN(si)|
+ max
1≤i≤K|ΨN(si) −Ψ(si)| + max
1≤i≤K sup
s∈Bsi,ε
|Ψ(si) −Ψ(s)|.
By construction sups∈Bsi,ε |Ψ(si) −Ψ(s)| < ε for all i. By the law of large
numbers ΨN(si) a.s.
→Ψ(si) as N →∞for each i = 1,...,K. Since K is ﬁnite,
max
1≤i≤K|ΨN(si) −Ψ(si)| ≤
K
X
i=1
|ΨN(si) −Ψ(si)| a.s.
→0.
Now for any s′ ∈Bsi,ε, ΨN(s′) a.s.
→Ψ(s′), ΨN(si) a.s.
→Ψ(si) and |Ψ(s′)−Ψ(si)| <
ε. This implies that we can choose N large enough so |ΨN(s′)−ΨN(si)| < 2ε.
Moreover this bound holds for all s′ ∈Bsi,ε and i so
limsup|ΨN(s) −Ψ(s)| ≤3ε
on Sp−1
+
. Since ε is arbitrary we conclude that sups∈Sp−1
+
|ΨN(s)−Ψ(s)| a.s.
→0
as N →∞. By assumption Ψ(smax) > Ψ(s) for all s ∈Sp−1
+
\smax, so we can
apply Theorem 2.12 in Kosorok (2008) to conclude that
ˆsmax
a.s.
→smax,
that is, ˆsmax is strongly consistent. This completes the ﬁrst part of the proof.


## Page 36


36
O. DAVIDOV AND S. PEDDADA
We have already seen that
sup
∥s−smax∥<δ
Ψ(s) −Ψ(smax) ≤−Cδ2
holds. We now need to bound E∗sup∥s−smax∥<δ N 1/2|(PN(¯Ψ(s) −¯Ψ(smax))|,
where E∗denotes the outer expectation and ¯Ψ(s) = I(sT Z≥0) −Ψ(s). We ﬁrst
note that the bracketing entropy of the upper half-planes is of the order δ/ε2.
The envelope function of the class I(sT z≥0) −I(sTmaxz≥0) where ∥s −smax∥< δ
is bounded by I(sT z≥0>sTmaxz) + I(sTmaxz≥0>sT z) whose squared L2 norm is
P(sT Z ≥0 > sT
maxZ) + P(sT
maxZ ≥0 > sT Z).
(A.17)
Note that we may replace the RV Z in (A.17) with the RV Z′ = Z/∥Z∥whose
mass is concentrated on the unit sphere. The condition that ∥s −smax∥< δ
implies that the angle between s and smax is of the order O(δ), and therefore
P(sT Z′ ≥0 > sT
maxZ′) is computed as surface integral on a spherical wedge
with maximum width δ. It follows that (A.17) is bounded by 2Ap−1δ∥h′∥∞
where Ap−1 is the area of Sp−1
+
, and ∥h′∥∞is the supremum of the density
of Z′. Clearly ∥h′∥∞< ∞since the density of Z is bounded by assumption.
Thus by Corollary 19.35 in van der Vaart (2000) we have
E∗
sup
∥s−smax∥<δ
N 1/2|PN(¯Ψ(s) −¯Ψ(smax))| ≤Cδ1/2.
It now follows that
ΨN(ˆsmax) ≥sup
s∈Sp−1
+
ΨN(s) −op(N −2/3),
(A.18)
which implies by Theorem 5.52 in van der Vaart (2000) and Theorem 14.4
of Kosorok (2008) that
ˆsmax = smax + Op(N −1/3);
that is, ˆsmax converges to smax at a cube root rate. This completes the second
part of the proof.
The limit distribution is derived by verifying the conditions in Theo-
rem 1.1 of Kim and Pollard (1990), denoted henceforth by KP. First note
that (A.18) is condition (i) in KP. Since ˆsmax is consistent, condition (ii)
also holds, and condition (iii) holds by assumption. The diﬀerentiability
of the density of Z implies that Ψ(s) is twice diﬀerentiable. The unique-
ness of the maximizer implies that −∇2Ψ(smax) is positive deﬁnite, and
hence condition (iv) holds; see also Example 6.4 in KP for related cal-
culations. Condition (v) in KP is equivalent to the existence of the limit
H(u,v) = limα→∞αE(¯Ψ(smax + u/α)¯Ψ(smax + v/α)) which can be rewrit-


## Page 37


INFERENCE FOR THE LINEAR STOCHASTIC ORDER
37
ten as
lim
β→0
1
β [P((smax + βu)T Z ≥0,(smax + βv)T Z ≥0)
−P((smax + βu)T Z ≥0)P((smax + βv)T Z ≥0)].
With some algebra we ﬁnd that this limit exists and equals
Z
z∈Sp−1
+
δ(sT
maxz)(zT (u + v))h(z)dz
−
Z
z∈Sp−1
+
δ(sT
maxz)(zT u)h(z)dz
Z
z∈Sp−1
+
δ(sT
maxz)(zT v)h(z)dz,
where δ(sT
maxz) is the usual Dirac function; hence integration is with respect
to the surface measure on {sT
maxz = 0}. It follows that condition also (v)
holds. Conditions (vi) and (vii) were veriﬁed in the second part of the proof.
Thus we may apply Theorem 1.1 in KP to get
N 1/3(ˆsmax −smax) ⇒arg max{−Q(s) + W(s):s ∈Sp−1
+
},
where by KP Q(s) = sT ∇2Ψ(smax)s and W(s) is a zero mean Gaussian pro-
cess with covariance function H(u,v). This completes the proof.
□
Proof of Proposition 3.3.
Note that
Ψ(s) = P(sT X ≤sT Y) = P(sT Z ≥0) = P
sT Z −sT δ
√
sT Σs
≥−
sT δ
√
sT Σs

= 1 −F

−
sT δ
√
sT Σs

.
Now, by assumption the DF F is independent of s. Therefore Ψ(s) is uniquely
maximized on Sp−1
+
if and only if the function
κ(s) =
sT δ
√
sT Σs
is uniquely maximized on Sp−1
+
. If Σ = I, then κ(s) = sT δ, and we wish to
maximize a linear function on Sp−1
+
. It is easily veriﬁed (by using ideas from
linear programming) that the maximizer is unique if δ ≥0 which is true by
assumption. Incidentally, it is easy to show directly that κ(s) is maximized
at s∗/∥s∗∥where
s∗= (δ1I(δ1≥0),...,δpI(δp≥0)).
Now let Σ ̸= I and assume that a unique maximizer does not exist; that
is, suppose that κ(s) is maximized by both s1 and s2. It is clear that
κ(λ1s1) = κ(λ2s2) for all λ1,λ2 > 0; that is, the value of κ(·) is constant
along rays through the origin. The rays passing through s1 and s2, respec-


## Page 38


38
O. DAVIDOV AND S. PEDDADA
tively, intersect the ellipsoid sT Σs = 1 at the points p1 and p2. It follows
that κ(p1) = κ(p2), moreover p1 and p2 maximize κ(·) on the ellipsoid.
Now since pT
1 Σp1 = 1 = pT
2 Σp2 we must have pT
1 δ = pT
2 δ. Recall that a
linear function on ellipsoid is uniquely maximized (just like on a sphere; see
the comment above). Therefore we must have p1 = p2 which implies that
s1 = s2 as required.
□
Proof of Theorem 3.4.
If X =st Y, then for all s we have sT X =st
sT Y. By assumption both sT X and sT Y are continuous RVs, so P(sT X ≤
sT Y) = 1/2. Suppose now that both X ⪯st Y and P(sT X ≤sT Y) > 1/2 for
some s ∈Sp−1
+
, hold. Then we must have X ≺l-st Y. Since X ⪯st Y we have
Xj ⪯st Yj for 1 ≤j ≤p. One of these inequalities must be strict; otherwise
X =st Y contradicts the fact that X ≺l-st Y. Now use Theorem 1 in Davidov
and Peddada (2011) to complete the proof.
□
Proof of Theorem 3.5.
The functions ψ1 and ψ2 deﬁned in the proof
of Theorem 3.1 are Donsker; cf. Example 19.7 in van der Vaart (2000). Hence
by the theory of empirical processes applied to (A.12), we ﬁnd that
N 1/2(Ψn,m(s) −Ψ(s)) ⇒G(s),
(A.19)
where G(s) is a zero mean Gaussian process, and convergence holds for all
s ∈Sp−1
+
. We also note that (A.19) is a two-sample U-processes. A central
limit theorem for such processes is described by Neumeyer (2004). Hence by
the continuos mapping theorem, and under H0, we have N 1/2(Ψn,m(ˆsmax) −
1/2)) ⇒sups∈Sp−1
+
G(s) where the covariance function of G(s), denoted by
C(u,v), is given by
1
λP(uT X1 ≤uT X2,vT X1 ≤vT X3)
(A.20)
+
1
1 −λP(uT X1 ≤uT X2,vT X3 ≤vT X2) −
1
4λ(1 −λ),
where X1,X2,X3 are i.i.d. from the common DF.
□
Proof of Theorem 3.6.
Suppose that X ≺l-st Y. Then for some s∗∈
Sp−1
+
we have sT
∗X ≺st sT
∗Y which implies that P(sT
∗X ≤sT
∗Y) > 1/2. By
deﬁnition P(sT
maxX ≤sT
maxY) ≥P(sT
∗X ≤sT
∗Y) so Ψ(smax) > 1/2. It follows
from the proof of Theorem 3.1 that Ψn,m(ˆsmax) →Ψ(smax) with probability
one. Thus,
Sn,m = N 1/2(Ψn,m(ˆsmax) −1/2) a.s.
−→∞
as n,m →∞.
Therefore by Slutzky’s theorem,
P(Sn,m > qn,m,1−α;H1) →1
as n,m →∞,


## Page 39


INFERENCE FOR THE LINEAR STOCHASTIC ORDER
39
where qn,m,1−α is the critical value for an α level test based on samples of size
n and m and qn,m,1−α →q1−α. Hence the test based on Sn,m is consistent.
Consistency for In,m and I+
n,m is established in a similar manner.
Now assume that X ⪯l-st Y ⪯l-st Z so that sT Y ⪯st sT Z for all s ∈Sp−1
+
.
Fix xi, i = 1,...,n, and choose s ∈Sp−1
+
. Without any loss of generality
assume that sT x1 ≤sT x2 ≤··· ≤sT xn. Deﬁne Uj = Pn
i=1 I(sT xi≤sT Yj) and
Vj = Pn
i=1 I(sT xi≤sT Zj). Clearly Uj and Vj take values in J = {0,... ,n}. Now,
for k ∈J we have
P(Uj ≥k) = P(sT Yj ≥sT xk) ≤P(sT Zj ≥sT xk) = P(Vj ≥k),
where we use the fact that sT Y ⪯st sT Z. It follows that Uj ⪯st Vj for
j = 1,...,m. Moreover {Uj} and {Vj} are all independent and it follows
from Theorem 1.A.3 in Shaked and Shanthikumar (2007) that Pm
j=1 Uj ⪯st
Pm
j=1 Vj. Thus Pn
i=1
Pm
j=1 I(sT xi≤sT Yj) ⪯st
Pn
i=1
Pm
j=1 I(sT xi≤sT Zj). The lat-
ter holds for every value of x1,...,xn, and therefore it holds unconditionally
as well, that is,
n
X
i=1
m
X
j=1
I(sT Xi≤sT Yj) ⪯st
n
X
i=1
m
X
j=1
I(sT Xi≤sT Zj).
It follows that ΨX,Y
n,m (s) ⪯st ΨX,Z
n,m(s) for all s ∈Sp−1
+
where ΨX,Y
n,m (s) and
ΨX,Z
n,m(s) are deﬁned in (3.1) and the superscripts emphasize the diﬀerent
arguments used to evaluate them. Thus
ΨX,Y
n,m (ˆsX,Y
max ) ⪯st ΨX,Z
n,m(ˆsX,Y
max ) ⪯st ΨX,Z
n,m(ˆsX,Z
max)
and as a consequence P(SX,Y
n,m > qn,m,1−α) ≤P(SX,Z
n,m > qn,m,1−α) as required.
The monotonicity of the power function of In,m and I+
n,m follows immediately
from the fact that ΨX,Y
n,m (s) ⪯st ΨX,Z
n,m(s) for all s ∈Sp−1
+
.
□
Acknowledgments.
We thank Grace Kissling (NIEHS), Alexander Gold-
enshluger, Yair Goldberg and Danny Segev (University of Haifa), for their
useful comments and suggestions. We also thank the Editor, Associate Edi-
tor and two referees for their input which improved the paper.
REFERENCES
Abrevaya, J. and Huang, J. (2005). On the bootstrap of the maximum score estimator.
Econometrica 73 1175–1204. MR2149245
Arcones, M. A., Kvam, P. H. and Samaniego, F. J. (2002). Nonparametric estimation
of a distribution subject to a stochastic precedence constraint. J. Amer. Statist. Assoc.
97 170–182. MR1947278
Audet, C., B´echard, V. and Le Digabel, S. (2008). Nonsmooth optimization through
mesh adaptive direct search and variable neighborhood search. J. Global Optim. 41
299–318. MR2398937


## Page 40


40
O. DAVIDOV AND S. PEDDADA
Bekele, B. N. and Thall, P. F. (2004). Dose-ﬁnding based on multiple toxicities in a
soft tissue sarcoma trial. J. Amer. Statist. Assoc. 99 26–35. MR2061885
Bickel, P. J. and Sakov, A. (2008). On the choice of m in the m out of n bootstrap
and conﬁdence bounds for extrema. Statist. Sinica 18 967–985. MR2440400
DasGupta, A. (2008). Asymptotic Theory of Statistics and Probability. Springer, New
York. MR2664452
Davey, B. A. and Priestley, H. A. (2002). Introduction to Lattices and Order, 2nd ed.
Cambridge Univ. Press, New York. MR1902334
Davidov, O. (2012). Ordered inference, rank statistics and combining p-values: A new
perspective. Stat. Methodol. 9 456–465. MR2871445
Davidov, O. and Herman, A. (2011). Multivariate stochastic orders induced by case-
control sampling. Methodol. Comput. Appl. Probab. 13 139–154. MR2755136
Davidov, O. and Herman, A. (2012). Ordinal dominance curve based inference for
stochastically ordered distributions. J. R. Stat. Soc. Ser. B Stat. Methodol. 74 825–
847.
Davidov, O. and Peddada, S. (2011). Order-restricted inference for multivariate binary
data with application to toxicology. J. Amer. Statist. Assoc. 106 1394–1404. MR2896844
Delagdo, M., Rodriguez-Poo, J. M. and Wolf, M. (2001). Subsampling inference
in cube root asymptotics with an application to Manski’s maximum score estimator.
Econom. Lett. 73 241–250.
Ding, Y. and Zhang, X. (2004). Some stochastic orders of Kotz-type distributions.
Statist. Probab. Lett. 69 389–396. MR2091758
Fang, K. T., Kots, S. and Ng, K. W. (1989). Symmetric Multivariate and Related
Distributions. Chapman & Hall, London.
Fisher, N. I. and Hall, P. (1989). Bootstrap conﬁdence regions for directional data.
J. Amer. Statist. Assoc. 84 996–1002. MR1134489
H´ajek, J., ˇSid´ak, Z. and Sen, P. K. (1999). Theory of Rank Tests, 2nd ed. Academic
Press, San Diego, CA. MR1680991
Hoeffding, W. (1963). Probability inequalities for sums of bounded random variables.
J. Amer. Statist. Assoc. 58 13–30. MR0144363
Hu, J., Homem-de-Mello, T. and Mehrotra, S. (2011). Concepts and applications
of stochastically weighted stochastic dominance. Unpublished manuscript. Available at
http://www.optimization-online.org/DB_FILE/2011/04/2981.pdf.
Ivanova, A. and Murphy, M. (2009). An adaptive ﬁrst in man dose-escalation study of
NGX267: Statistical, clinical, and operational considerations. J. Biopharm. Statist. 19
247–255. MR2518371
Joe, H. (1997). Multivariate Models and Dependence Concepts. Chapman & Hall, London.
MR1462613
Johnson, R. and Wichern, D. (1998). Applied Multivariate Statistical Analysis. Prentice
Hall, New York.
Kim, J. and Pollard, D. (1990). Cube root asymptotics. Ann. Statist. 18 191–219.
MR1041391
Kosorok, M. R. (2008). Introduction to Empirical Processes and Semiparametric Infer-
ence. Springer, New York. MR2724368
Lee, S. M. S. (1999). On a class of m out of n bootstrap conﬁdence intervals. J. R. Stat.
Soc. Ser. B Stat. Methodol. 61 901–911. MR1722246
Lucas, L. A. and Wright, F. T. (1991). Testing for and against a stochastic order-
ing between multivariate multinomial populations. J. Multivariate Anal. 38 167–186.
MR1131713


## Page 41


INFERENCE FOR THE LINEAR STOCHASTIC ORDER
41
Moser, V. (2000). Observational batteries in neurotoxicity testing. International Journal
of Toxicology 19 407–411.
Neumeyer, N. (2004). A central limit theorem for two-sample U-processes. Statist.
Probab. Lett. 67 73–85. MR2039935
NTP (2003). NTP toxicology and carcinogenesiss studies of citral (microencapsulated)
(CAS No. 5392-40-5) in F344/N rats and B6C3F1 mice (feed studies).
Peddada, S. D. (1985). A short note on Pitman’s measure of nearness. Amer. Statist. 39
298–299. MR0817793
Peddada, S. D. and Chang, T. (1996). Bootstrap conﬁdence region estimation of the
motion of rigid bodies. J. Amer. Statist. Assoc. 91 231–241. MR1394077
Pitman, E. J. G. (1937). The closest estimates of statistical parameters. Proceedings of
the Cambridge Philosophical Society 33 212–222.
Price, C. J., Reale, M. and Robertson, B. L. (2008). A direct search method for
smooth and non-smooth unconstrained optimization problems. ANZIAM J. 48 927–
948.
Roy, S. N. (1953). On a heuristic method of test construction and its use in multivariate
analysis. Ann. Math. Statist. 24 220–238. MR0057519
Sampson, A. R. and Whitaker, L. R. (1989). Estimation of multivariate distributions
under stochastic ordering. J. Amer. Statist. Assoc. 84 541–548. MR1010343
Sen, B., Banerjee, M. and Woodroofe, M. (2010). Inconsistency of bootstrap: The
Grenander estimator. Ann. Statist. 38 1953–1977. MR2676880
Serfling, R. J. (1980). Approximation Theorems of Mathematical Statistics. Wiley, New
York. MR0595165
Shaked, M. and Shanthikumar, J. G. (2007). Stochastic Orders. Springer, New York.
MR2265633
Sherman, R. P. (1993). The limiting distribution of the maximum rank correlation esti-
mator. Econometrica 61 123–137. MR1201705
van der Vaart, A. W. (2000). Asymptotic Statistics. Cambridge Univ. Press, Cambridge.
Department of Statistics
University of Haifa
Mount Carmel, Haifa 31905
Israel
E-mail: davidov@stat.haifa.ac.il
Biostatistics Branch
National Institute
of Environmental Health Sciences
111 T.W. Alexander Drive
Research Triangle Park, North Carolina 27709
USA
E-mail: peddada@niehs.nih.gov

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
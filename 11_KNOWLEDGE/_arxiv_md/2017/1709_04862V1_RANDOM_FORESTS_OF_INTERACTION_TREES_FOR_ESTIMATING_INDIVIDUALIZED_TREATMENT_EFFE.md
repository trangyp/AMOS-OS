---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1709.04862v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1709.04862v1_Random_Forests_of_Interaction_Trees_for_Estimating_Individualized_Treatment_Effe

> Source: 1709.04862v1_Random_Forests_of_Interaction_Trees_for_Estimating_Individualized_Treatment_Effe.pdf

> Pages: 32

---


## Page 1


arXiv:1709.04862v1  [stat.ML]  14 Sep 2017
Random Forests of Interaction Trees for Estimating
Individualized Treatment Eﬀects in Randomized Trials
Xiaogang Su, Annette T. Pe˜na
Department of Mathematical Sciences
University of Texas, El Paso, TX 79968
Lei Liu
Department of Preventive Medicine
Northwestern University, Chicago, IL 60611
and Richard A. Levine
Department of Mathematics and Statistics
San Diego State University, San Diego, CA 92182
Abstract
Assessing heterogeneous treatment eﬀects has become a growing interest in ad-
vancing precision medicine. Individualized treatment eﬀects (ITE) play a critical
role in such an endeavor. Concerning experimental data collected from random-
ized trials, we put forward a method, termed random forests of interaction trees
(RFIT), for estimating ITE on the basis of interaction trees (Su et al., 2009).
To this end, we ﬁrst propose a smooth sigmoid surrogate (SSS) method, as an
alternative to greedy search, to speed up tree construction. RFIT outperforms
the traditional ‘separate regression’ approach in estimating ITE. Furthermore,
standard errors for the estimated ITE via RFIT can be obtained with the in-
ﬁnitesimal jackknife method. We assess and illustrate the use of RFIT via both
simulation and the analysis of data from an acupuncture headache trial.
Keywords: Individualized treatment eﬀects, Inﬁnitesimal jackknife, Precision medicine,
Random forests, Treatment-by-covariates interaction.
1


## Page 2


1
Introduction
Precision medicine aims to optimize the delivery of stratiﬁed or individualized therapies
by integrating comprehensive patient data. This emerging approach has become a growing
interest in many biomedical applications. To advance precision medicine, it is crucial to
understand the diﬀerential eﬀects of a treatment as opposed to its overall main eﬀect in the
conventional practice of medical decisions.
There are many approaches in this endeavor; see Lipkovich, Dmitrienko, and D’Agostino
(2016) for a recent survey. Among them, tree-based methods are dominant for several rea-
sons. Built simply on the basis of a two-sample test statistic, trees facilitate a powerful
comprehensive modeling by recursively grouping data. Diﬀerential treatment eﬀects essen-
tially involve treatment-by-covariates interactions, which may be of nonlinear forms and of
high orders. Trees excel in dealing with complex interactions. Tree models are capable of
handling high-dimensional covariates of mixed types and an oﬀ-the-shelf tool in the sense
that minimal data preparation is required.
Interaction trees (IT; Su et al., 2009) extend tree procedures to subgroup analysis by
explicitly assessing the treatment-by-covariate interaction.
Foster, Taylor, Ruberg (2011)
identiﬁes subgroups by estimating the potential outcomes, which they rebranded as ‘vir-
tual twins’. Another approach, SIDES (Subgroup Identiﬁcation based on Diﬀerential Eﬀect
Search) proposed by Lipkovich et al. (2011), addresses issues such as subgroups with en-
hanced treatment eﬀects, taking into account both eﬃcacy and toxicity. QUINT (QUalitative
INteraction Trees; Dusseldorp and van Mechelen, 2014) focuses on qualitative interactions.
Loh, He, and Man (2015) proposes a tree procedure for identifying subgroups that is less
prone to biased variable selection. The optimal treatment regime (Murphy, 2003) oﬀers an
alternative way of looking at the problem. Along this direction, tree-based approaches are
also common; see, e.g., (Zhang et al., 2012) and (Laber and Zhao, 2015).
There are typically two types of precision medicine: stratiﬁed medicine and personalized
medicine. The aforementioned methods belong to the former scope, with focus on stratiﬁed
treatment eﬀects or regimes where groups of individuals showing homogeneous treatment
eﬀects are sought. That said, individualized treatment eﬀects (ITE) are of key importance
in deploying tailored treatment plans as part of personalized medicine. The ITE also aﬀords
deeper study of treatment eﬃcacy. Furthermore, ITE estimation is a necessary ﬁrst step for
a number of methods used in stratiﬁed medicine and optimal treatment regime; see, e.g.,
Foster, Taylor, Ruberg (2011), Zhang et al. (2012), and Laber and Zhao (2015).
The focus of this article is on the estimation of ITE with data collected from randomized
trials. We examine an ensemble learning approach that we coin as RFIT for random forests on
the basis of interaction trees (Su et al., 2009). Our methodological contribution is twofold:
2


## Page 3


ﬁrst, we introduce a faster alternative splitting method, called smooth sigmoid surrogate
(SSS), to speed up IT; second, we extend the inﬁnitesimal jackknife method (Efron, 2014)
to compute the standard errors for ITE estimates.
Moreover, we compare our proposed
approach to the commonly applied separate regression (SR). RFIT is superior to SR by
working on an easier problem. We demonstrate the outperformance of RFIT over SR in
estimating ITE via extensive numerical experiments.
The remainder of the article is organized as follows. In Section 2, we ﬁrst introduce
the concept of ITE within Rubin’s causal model framework. RFIT with SSS splitting for
estimating ITE and the standard error formula for estimated ITE are then presented in detail.
Section 3 contains simulation experiments that are designed to investigate the performance of
SSS in splitting data, to compare RFIT with the conventional separate regression approach,
and to demonstrate the validity of the SE formula. We illustrate our proposed RFIT approach
with data from an acupuncture headache trial in Section 4.
2
Random Forests of Interaction Trees (RFIT)
Concerning randomized trials, consider data D = {(yi, Ti, xi) : i = 1, . . . , n} consisting of n
IID copies of (Y, T, X), where yi is the continuous response or outcome for the i-th subject,
Ti is the binary treatment assignment indicator: 1 for the treated group and 0 for control,
and xi = (xi1, . . . , xip)T ∈Rp is a p-dimensional covariate vector of mixed types.
The Neyman–Rubin causal model (see, e.g., Neyman, 1923; Rubin, 1974 & 2005) provides
a way of ﬁnely calibrating the causal eﬀect of treatment T on the response via the concept
of potential outcomes. Let Y ′
1 and Y ′
0 denote the response values for a subject when assigned
to the treated and the control group, respectively. Either Y ′
1 or Y ′
0, but not both, can be
observed. The observed outcome is given by Y = Y ′
1 T + Y ′
0 (1 −T). Within this framework,
the treatment eﬀect can be evaluated at three levels: the population level E(Y ′
1 −Y ′
0), the
subpopulation level E(Y ′
1 −Y ′
0 | X ∈A) for a subset A ⊂Rp, and the unit or subject level
Y ′
1 −Y ′
0. These three levels form a hierarchy of causal inference in increasing order of strength,
in the sense that a lower-level inference can be obtained from that of an upper-level inference,
but not vice versa. Let δ be a generic notation for treatment eﬀect.
Deﬁnition 1. The individualized treatment eﬀect (ITE) is deﬁned as δ(x) = E(Y ′
1 −Y ′
0 | X =
x).
Note that δ(x) is diﬀerent from the (random) unit-level eﬀect (Y ′
1−Y ′
0). Strictly speaking,
δ(x) is a subpopulation-level eﬀect among individuals with X = x. Nevertheless, δ(x) is the
ﬁnest approximation to the unit-level inference that is possibly available in practice.
3


## Page 4


Causal inference is essentially concerned with estimating δ at diﬀerent levels through the
available data D. The diﬃculty in causal inference stems primarily from the convoluted roles
(e.g., confounder, eﬀect modiﬁer or moderator, or mediator) played by each covariate in
X. For experimental data from trials with random treatment assignment mechanisms, T is
independent of other variables. As a result, the unconfoundedness condition (Y1, Y0) ⊥⊥T | X
(Rubin, 2005), being suﬃcient for obtaining population-level inference from D, is trivially
met.
Randomization renders the confounding issue of little concern; however, covariate
modiﬁcation to the treatment eﬀects remains across both the subpopulation and unit levels.
Interaction trees (IT; Su et al., 2009) seek subgroups with heterogeneous treatment ef-
fects by following the paradigm of CART (Breiman et al., 1984); hence IT supplies causal
inference at the subpopulation level. Nevertheless, results from IT can be building blocks for
inferences at other levels: one has the ﬂexibility to move backward to the overall eﬀect esti-
mation by integration and move forward to ITE via ensemble learning. The main objective
of this article is to examine the use of random forests of interaction trees (RFIT) in esti-
mating δ(x). Random forests (Breiman, 2001) is an ensemble learning method, constructing
a collection of tree models and integrating results across the tree models. Among its many
merits, RF is among the top-performers in predictive modeling and provides many useful
features such as proximity matrix, variable importance ranking, and partial dependence plot
(Liaw and Wiener, 2002).
2.1
SSS for Identifying the Best CutoﬀPoint
To extend random forests on the basis of interaction trees, one essential ingredient is the
splitting statistics. IT bisects data by maximizing the diﬀerence in treatment eﬀects between
two child nodes.
A split on data is induced by a binary variable of general form ∆=
∆(Xj; c) = I(Xj ≤c) that applies a threshold on covariate Xj at cutoﬀpoint c; recall that
nominal variables can be made ordinal by sorting its levels according to the treatment eﬀect
estimate at each level (see Appendix A of Su et al., 2009). Any binary split s results in the
following 2 × 2 table, where n1L denotes the number of treated subjects in the left child
node; ¯y1L denotes the sample mean response for treated subjects in the left child node; and
similarly for other notations.
Child Node
Treatment
Left
Right
0
(¯y0L, n0L)
(¯y0R, n0R)
1
(¯y1L, n1L)
(¯y1R, n1R)
4


## Page 5


The splitting statistic in IT can be based on the Wald test for H0 : β3 = 0 in the interaction
model:
yi = β0 + β1Ti + β2∆i + β3Ti · ∆i + εi with εi
IID
∼N(0, σ2),
(1)
where ∆i = ∆(xij; c). The least squares estimate of β3 is given by ˆβ3 = (¯y1L −¯y0L) −(¯y1R −
¯y0R), corresponding to the concept of ‘diﬀerence in diﬀerences’ (DID). The resultant Wald
test statistic amounts to
Q(c) =
{(¯y1L −¯y0L) −(¯y1R −¯y0R)}2
ˆσ2(1/n1L + 1/n0L + 1/n1R + 1/n0R),
(2)
where
ˆσ2 =
1
n −4


n
X
i=1
y2
i −
X
k=0,1
X
t∈{L,R}
nkt ¯y2
kt


(3)
is the pooled estimator of σ2. Q(c) measures the diﬀerence in treatment eﬀects between two
child nodes. With the conventional greedy search (GS) approach, the best cutoﬀpoint ˆc for
Xj is ˆc = argmaxc Q(c). It is worth noting that minimizing the least squares (LS) criterion
with Model (1) does not serve well in IT. A cutoﬀpoint can yield the minimum LS criterion
merely for its strong additive eﬀect (i.e., associated with β2).
GS evaluates the splitting measure at every possible cutoﬀpoint for Xj. This can be
slow when the number of cutoﬀpoints to be evaluated is large, even though GS can be
implemented by updating the computation of Q(c) for neighboring c’s. Furthermore, this
discrete optimization procedure yields erratic measures, as exempliﬁed by the orange line in
Figure 1(b). As a result, GS may mistakenly select a local spike due to large variation. These
deﬁciencies motivate us to consider a smooth alternative to GS. Noting that the discreteness
steps from the threshold indicator function ∆i involved in many components of the splitting
statistics, our approach is to approximate ∆i with a smooth sigmoid function.
For this
reason, we call the method ‘smooth sigmoid surrogate’ or SSS in short. While many sigmoid
functions can be used, it is natural to consider the logistic or expit function
s(x; a, c) = [1 + exp{−a(x −c)}]−1 =
exp{a (x −c)}
1 + exp{a (x −c)},
(4)
where c is the cutoﬀpoint and a > 0 is a shape or scale parameter. Figure 1(a) depicts the
expit function at c = 0 for diﬀerent a values.
To approximate Q(c), we start with approximating nlτ with ˜nlt for l = 0, 1 and t = {L, R}
5


## Page 6


as follows:









n1L = Pn
i=1 Ti∆i
≈
˜n1L = Pn
i=1 Tisi,
n1R = n1 −n1L
≈
˜n1R = n1 −˜n1L,
n0L = Pn
i=1 (1 −Ti) δi
≈
˜n0L = Pn
i=1(1 −Ti)si,
n0R = n0 −n0L
≈
˜n0R = n0 −˜n0L,
where si = s(xij; a, c) approximates ∆i, n1 = P
i Ti is the total number of treated individuals,
and n0 = Pn
i=1(1 −Ti) is the total number of untreated individuals. Let Slt = P
i∈t & Ti=l yi
denote the associated sum of responses values, which can be approximated in a similar
manner:









S1L = Pn
i=1 yiTi∆i
≈
˜S1L = Pn
i=1 yiTisi,
S1R = S1 −S1L
≈
˜S1R = S1 −˜S1L,
S0L = Pn
i=1 yi (1 −Ti) ∆i
≈
˜S0L = Pn
i=1 yi (1 −Ti) si,
S0R = S0 −S0L
≈
˜S0R = S0 −˜S0L,
where S1 = P
i Tiyi is the sum of response values for all treated individuals and similarly
S0 for the untreated. Note that quantities n1, n0 = n −n1, S1, and S0 = P
i yi −S1 do
not involve the split variable ∆i and can be computed beforehand. It follows that ¯ylt =
Slt/nlt ≈
˜Slt/˜nlt = ˜ylt for l = 0, 1 and t = {L, R}. Next, bringing (˜nlt, ˜ylt) into (3) yields
its approximation ˜σ2. Finally, plugging all the approximated quantities into Q(c) in (2) yields
eQ(c) =
{(˜y1L −˜y0L) −(˜y1R −˜y0R)}2
˜σ2(1/˜n1L + 1/˜n0L + 1/˜n1R + 1/˜n0R).
(5)
Now eQ(c) is a smooth objective function for c only and can be directly maximized to obtain
the best cutoﬀpoint ˆc.
Besides c, there is a scale parameter a involved in eQ(c) given by (5).
As shown by
simulation in Section 3, the performance of the SSS method is quite robust with respect
to the choice of a for a wide range of values. Thus a can be ﬁxed a priori. In order to
do so, we standardize the predictor xij := (xij −¯xj)/ˆσj, where (¯xj, ˆσj) denote the sample
mean and standard deviation of variable Xj, respectively. For standardized covariates, we
recommend ﬁxing a a value in [10, 50]. With ﬁxed a, the best cutoﬀpoint ˆc can be obtained
by maximizing ˜Q(c) with respect to c and then transformed back to the original data scale
for interpretability.
This is a one-dimensional smooth optimization problem, which can
be conveniently solved by many standard optimization routines. We use the Brent (1973)
method available in the R (R Core Team, 2017) function optimize in our implementation.
Given the nonconcave nature of the maximization problem, further techniques such as multi-
start or partitioning the search range may be used in combination with Brent’s method.
6


## Page 7


However, as shown in our numerical studies, a plain application of Brent’s method, without
further eﬀorts for locating the global optimum, works quite eﬀectively in estimating the
cutpoint.
SSS smooths out local spikes in GS splitting measures and hence helps signify the true
cutoﬀpoint; see Figure 1(b) for one example. Our simulation in Section 3 shows that SSS
outperforms GS in most scenarios, especially when dealing with weak signals.
Another
immediate advantage of SSS over GS is computational eﬃciency. The following proposition
provides an asymptotic quantiﬁcation of the computational complexity involved in both GS
and SSS splitting.
Proposition 2.1. Consider a typical data set of size n in the interaction tree setting, where
both GS and SSS are used to ﬁnd the best cutoﬀpoint ˆc for a continuous predictor X with
O(n) distinct values. In terms of computation complexity, GS is at best O{ln(n) n} with the
updating scheme and O(n2) without the updating scheme while SSS is O(mn), where m is
the number of iterations in Brent’s method.
A proof of Proposition 2.1 is relegated to the Supplementary Materials. Implementation
of tree methods beneﬁts from incremental updating; see, e.g., LeBlanc and Crowley (1993)
and Utgoﬀ, Berkman, and Clouse (1997). However, it is a common wrong impression that
the GS splitting with updating is only of order O(n). Updating the IT splitting statistic
entails sorting the response values according to the X values within both treatment groups.
It turns out that this sorting step would dominate the algorithm in complexity asymptotically
with a rate of O{ln(n) n}. Comparatively, SSS depends on the number of iterations in Brent’s
method, m. Although the number of iterations is aﬀected by the convergence criterion and
the desired accuracy, m is generally small since Brent’s method has guaranteed convergence
at a superlinear rate. Based on our limited numerical experience, m rarely gets over 15 even
for large n. In other words, the O(mn) rate for SSS essentially amounts to the linear rate
O(n).
2.2
Estimating ITE via RFIT
RFIT follows the standard paradigm of random forests (Breiman, 2001). Take a bootstrap
sample Db from data D and then construct an IT using Db. To split a node, a subset of
m covariates are randomly selected and the best cut for each covariate is identiﬁed and
compared to determine the best split of data. The step is iterated till a large tree Tb is
grown. Each terminal node τ in Tb is summarized with an estimated treatment eﬀect ˆδτb,
which is simply the diﬀerence in mean response between treated and untreated individuals
7


## Page 8


falling into τ, i.e.,
ˆδτb =
X
i: xi∈Db∩τb
Tiyi
n1τb
−(1 −Ti)yi
n0τb

,
where n1τb = P
i:xi∈Db∩τb Ti is the number of treated individuals in Db that fall into τ and
n0τb for the untreated.
The entire tree construction procedure is then repeated on a number of B bootstrap
samples, which results in a sequence of bootstrap trees {Tb : b = 1, 2, . . . , B}. For each tree
Tb, an individual with covariate vector x would fall into one and only one of its terminal
node, which we denote as τb(x). Letting ˆδb(x) = ˆδτb(x), the ITE for this individual can then
be estimated as
ˆδ(x) = 1
B
B
X
i=1
ˆδb(x).
(6)
Efron (2014) discussed methods for computing standard errors for bootstrap-based esti-
mators and advocated the use of inﬁnitesimal jackknife (IJ). The IJ approach is found prefer-
able in random forests, as further explored by Wager, Hastie, and Efron (2014). Proposition
2.2 applies the IJ method to obtain a standard error formula for estimated ITE ˆδ(x). Its
proof is outlined in the Supplementary Materials.
Proposition 2.2. The IJ estimate of variance of ˆδ(x) is given by
ˆV =
n
X
i=1
¯Z2
i ,
(7)
where ¯Zi = PB
b=1 Zbi/B and Zbi = (Nbi −1){ˆδb(x)−ˆδ(x)} with Nbi being the number of times
that the i-th observation appears in the b-th bootstrap resample. In other words, the quan-
tity ¯Zi is the bootstrap covariance between Nbi and ˆδb(x). In practice, ˆV is biased upwards,
especially for small or moderate B. A bias-corrected version is given by
ˆVc = ˆV −1
B2
n
X
i=1
B
X
b=1
(Zbi −¯Zi)2.
(8)
Further assuming approximate independence of Nbi and ˆδb(x), another bias-corrected version
is given by
ˆVc = ˆV −n −1
B2
B
X
b=1
{ˆδb(x) −ˆδ(x)}2,
(9)
which is easier to compute than (8).
8


## Page 9


The validity of these SE formulas will be investigated by simulation in Section 3. The
bias-corrected SE formulas in (8) and (9) generally yield very similar results with superior
performance to the uncorrected version (7). Note that computing (8) entails evaluation of
the matrix Z = (Zbi) at each diﬀerent x. Therefore, the SE given in (9) is recommended for
its enhanced computational eﬃciency.
2.3
Comparison with SR
Under the potential outcome framework, separate regression (SR) is conventionally used to
estimate δ(x); see, e.g., van der Laan, Polley, Hubbard (2006) and Foster, Taylor, Ruberg
(2011). The basic idea is to build a model based on data for treated individuals only to
estimate µ1(x) = E(Y1 | X = x) and build a model based on data for untreated individuals
only to estimate µ0(x) = E(Y0 | X = x). Let ˆµ0(x) and ˆµ1(x) denote the resultant estimates
of µ0(x) and µ1(x), respectively. Then ITE can be estimated as
˜δ(x) = ˆµ1(x) −ˆµ0(x).
(10)
Since SR essentially involves predictive modeling, random forests (Breiman, 2001) are com-
monly used in the literature.
We would like to argue that RFIT is superior to SR. This is primarily because RFIT
works on a simpler problem. To explain, consider the model form Y = µ0(x) + Tδ(x) + ε,
where µ1(x) = µ0(x)+δ(x). Functions µ0(x) and δ(x) may involve diﬀerent sets of covariates.
In the clinical setting, covariates showing up in µ0(x) only are called prognostic factors while
covariates showing up in δ(x) are called predictive factors (see, e.g., Ballman, 2015). In other
words, predictive factors interact with the treatment and hence cause diﬀerential treatment
eﬀects. In SR, both µ1(x) and µ0(x) have to be estimated to have the diﬀerence δ(x); thus it
has to take both prognostic and predictive factors into consideration. Comparatively, RFIT
estimates δ(x) directly by focusing on predictive factors only. This is because a prognostic
factor won’t cause a diﬀerence in diﬀerences, referring to its splitting statistic in (2). In the
following, we introduce a performance measure for RFIT and SE in estimating ITE δ(x) and
a theoretical understanding of the measure is attempted.
Both RFIT and SR take the bootstrap-based ensemble learning approach; the ITE esti-
mates ˆδ(x) in (6) and ˜δ(x) in (10) involve randomness owing to bootstrap resampling, the
current data D, and the point x at which the estimation is made. To compare RFIT with
SR, we consider an average mean squares error (AMSE) measure deﬁned by
AMSE = EX,D,B{ˆδ(X) −δ(X)}2,
(11)
where the expectation is taken with respect to the bootstrap distribution B given the current
data D, the sampling distribution of data D, and then the distribution of X.
9


## Page 10


Deﬁne
¯δ(x; D) = EB {ˆδ(x)},
and
¯δ(x) = ED {¯δ(x; D)},
(12)
where ¯δ(x; D) is the RFIT estimate of δ(x) obtained with perfect bootstrap or B →∞and
¯δ(x) is the perfect bootstrap RFIT estimate if, furthermore, we are allowed to recollect data
D freely. Similarly, we deﬁne {¯µ0(x; D), ¯µ0(x)} on the basis of ˆµ0(x) and {¯µ1(x; D), ¯µ1(x)}
on the basis of ˆµ1(x) in SR. In addition, deﬁne
¯µ0 = EX {¯µ0(x)}
and
µ0 = EX{µ0(X)} = E(Y0),
(13)
and similarly {¯µ1, µ1}. Proposition 2.3 provides a decomposition of AMSE for the ITE esti-
mate ˆδ(x) by RFIT and for ˜δ(x) by SR.
Proposition 2.3. For the RFIT estimate ˆδ(x) in (6),
AMSE = EX,D,B
n
ˆδ(X) −¯δ(X; D)
o2
+ EX,D
¯δ(X; D) −¯δ(X)
	2 + EX
¯δ(X) −δ(X)
	2 .
(14)
For the SR estimate ˜δ(x) in (10),
AMSE
=
EX,D,B {ˆµ1(X) −¯µ1(X; D)}2 + EX,D {¯µ1(X; D) −¯µ1(X)}2 + EX {¯µ1(X) −µ1(X)}2
+
EX,D,B {ˆµ0(X) −¯µ0(X; D)}2 + EX,D {¯µ0(X; D) −¯µ0(X)}2 + EX {¯µ0(X) −µ0(X)}2
−
2EX [{¯µ1(X) −µ1(X)}{¯µ0(X) −µ0(X)}] .
(15)
The ﬁrst term of AMSE in (14) corresponds to Monte Carlo variation resulted from using
a ﬁnite number of B bootstrap samples. The second term represents the sampling variation
owing to lack of endless supply of training data in reality.
The third term is the bias.
Similar interpretation holds true for the terms in (15), yet with an additional covariance
term −2EX [{¯µ1(X) −µ1(X)}{¯µ0(X) −µ0(X)}] .
Ensemble learners such as RF and bagging aim for variance reduction by imitating the
endless supply of replicate data via bootstrap resampling. This is why we have the additional
decomposition
EX,D,B{ˆδ(X) −¯δ(X)}2 = EX,D,B
n
ˆδ(X) −¯δ(X; D)
o2
+ EX,D
¯δ(X; D) −¯δ(X)
	2
in (14); similarly for ˆµ1(X) and ˆµ0(X) in (15). However, ensemble learning has little eﬀect
on the bias term EX{¯δ(X) −δ(X)}2 in (14); similarly for the two bias terms in (15) as
well as the covariance term −2EX [{¯µ1(X) −µ1(X)}{¯µ0(X) −µ0(X)}] . The bias problem
for ensemble learners such as random forests has been noted by Breiman (1999) and others.
10


## Page 11


From another perspective, RF facilitates a smoothing procedure by averaging data over an
adaptive neighborhood; as a result, it cuts the hill and ﬁlls the valley.
While both RFIT and SR would suﬀer from certain bias, the AMSE in SR tends to
be larger than that of RFIT in general as we shall demonstrate numerically in Section 3.
Numerical evidence shows that SR is more prone to the bias problem because it tends to
underestimate a large ITE and overestimate a small ITE. In fact, such a bias also has an
eﬀect on the last covariance term in (15). A large ITE δ(x) occurs when µ1(x) is large
and/or µ0(x) is small. The smoothing eﬀect yields ¯µ1(X) −µ1(x) < 0 with cut hills and
¯µ0(X) −µ0(X) > 0 with ﬁlled valleys. Thus {¯µ1(X) −µ1(X)}{¯µ0(X) −µ0(X)} tends to
be negative. A similar observation holds for a small ITE, which occurs when µ1(x) is small
and/or µ0(x) is large. As a result, the last term in (15) tends to be negative, leading to a
more inﬂated AMSE for SR.
3
Simulation Studies
This section presents results from simulation studies designed to compare the smooth sigmoid
surrogate (SSS) splitting method with greedy search (GS) in ﬁnding the best cutoﬀpoint;
compare RFIT with separate regression (SR) in estimating the individualized treatment
eﬀects (ITE); and investigate the standard error (SE) formulas for the estimated ITE.
3.1
Comparison of SSS versus GS
To compare SSS with GS, we generated data from model
y = 0.5 + 0.5 T + 0.5 ∆+ 0.5 · T ∆+ ε,
(16)
where ∆= ∆(x; c0) = I(x ≥c0), x ∼uniform[0, 1], c0 = 0.5, and ε ∼N(0, 1). We
considertwo sample sizes n = 50 and n = 500, corresponding to relatively fewer and larger
numbers of observations in a node. For each simulated data, both GS and SSS are used to
identify the best cutoﬀpoint ˆc. Diﬀerent a = 1, 2, . . . , 100 values are used in SSS. For each
model conﬁguration, 500 simulation runs are made.
Figure 2 presents the empirical density and the MSE measure, deﬁned as MSE =
P500
k=1(ˆcm −c0)2/500, for the estimated cutoﬀpoint ˆc by SSS and GS. It can be seen that
SSS compares favorably to GS in terms of MSE. From the empirical density plots, it can
be seen that one important contribution made by SSS is the reduced variation as compared
to GS. In most scenarios, SSS shows considerable stability with respect to the choice of the
shape parameter a, especially with relatively larger a values. Too small an a ≤5 value can
11


## Page 12


result in deteriorated performance and hence is not advisable. It seems desirable to balance
a more accurate approximation to the indicator function with a relatively larger a value and
the more smooth objective function for optimization with a relatively smaller a value. We
would like to comment that estimating a is not a good idea in the tree setting for several
reasons: tree models seek threshold eﬀects which entail a relatively large a value; estimat-
ing a unnecessarily slows down the computation at each node split; having a diﬀerent a for
each covariate will make the results less comparable across covariates in order to ﬁnd the
best split. Recall that SSS works with standardized X and transfers ˆc back to its original
scale; we recommend ﬁxing a = 10 in SSS for standardized x based on our more extensive
numerical explorations that are not presented here. Henceforth, SSS with a = 10 is used by
default in the RFIT implementation.
To compare the computing time, we generated data from the same model; a slight mod-
iﬁcation was made in the way of simulating the covariate: x follows a discrete uniform
distribution over {1/K, 2/K, . . ., K/K} so that x has a total of K distinct values. This
allows us to investigate the computing time with diﬀerent K. The choices for n and K are
n ∈{50, 100, 500, 1000, 2000, 10000} and K ∈{10, 100, 500}. Table 1 tabulates the comput-
ing time in seconds for GS and SSS splitting, averaged over 10 simulation runs for each
setting. It can be seen that SSS is superior to GS in terms of computational eﬃciency. As
expected, it takes longer for both GS and SSS as n increases in general. It takes longer for
GS as K increases; but this is not the case for SSS.
3.2
Comparison of RFIT versus SR
We compare SSS to SR in estimating ITE. The data are generated with the following scheme:
ﬁrst simulate ﬁve (p = 5) predictors xj ∼uniform[0, 1] for j = 1, . . . , 5; then we generate
y′
0 = µ0(x) + α + ε0 with a nonlinear polynomial
µ0(x) = −2 −2x1 −2x2
2 + 2x3
3
and α and ε0 being independent from N (0, 1); next, we generate y′
1 = µ1(x) + α + ε1, where
µ1(x) = µ0(x)+δ(x) and ε1 ∼N (0, 1) is independent of both α and ε0. A random eﬀect term
α is introduced to mimic some common characteristics shared by repeated measures Y ′
0 and
Y ′
1 taken from the same subject. The unit-level eﬀect Y ′
1 −Y ′
0 equals δ(x) + (ε1 −ε0), where
(ε1 −ε0) represents additional random errors that can not be accounted for by covaraites x.
12


## Page 13


Four models (I)–(IV) are considered for the ITE δ(x), as given below:
Model I:
δ(x) = −2 + 2x1 + 2x2
(17)
Model II:
δ(x) = −2 + 2 I(x1 ≤0.5) + 2 I(x2 ≤0.5) I(x3 ≤0.5)
(18)
Model III:
δ(x) = −6 + 0.1 exp(4x1) + 4 exp{20(x2 −0.5)} + 3x3 + 2x4 + x5
(19)
Model IV:
δ(x) = −10 + 10 sin(πx1x2) + 20(x3 −0.5)2 + 10x4 + 5x5.
(20)
Model I exempliﬁes a linear ITE; Model II represents a tree-structured model; Model III
& IV are derived from two nonlinear models in Friedman (1991). Finally, we simulate the
randomized treatment assignment variable T independently from Bernoulli(0.5) and hence
the observed response y = Ty′
1 + (1 −T)y′
0.
For each training data set D, both RFIT and SR are used to learn a model on ITE.
In order to evaluate their performance, a test sample D′ of size n′ = 2000 is generated
beforehand. The ITE models trained with RFIT and SR in each simulation are applied to
estimate the ITE for D′ and a mean square error (MSE) measure MSE = Pn′
i=1{ˆδ(xi) −
δ(xi)}2/n′ is computed. Two sample sizes n = 100 and n = 500 are considered for the
training data D and a total of 200 simulation runs is used for each simulation setting.
Figure 3 plots the parallel boxes of MSE measures from 200 simulation runs for RFIT and
SR. The averages are highlighted with blue bars, corresponding to estimates of the AMSE in
(11). It can be seen that RFIT outperforms SR consistently in all the scenarios considered
here. Again, the superiority of RFIT can be explained by the fact that it works on an easier
task than SR by estimating δ(x) directly. Additional numerical insight into the bias problem
is provided by plotting the estimated ITE ˆδ(x) (averaged over 200 simulated runs) versus
the actual ITE δ(x). See Section B of the Supplementary Material.
3.3
Standard Error Formulas
To investigate the validity and performance of the standard error (SE) formulas for estimated
ITE, we generated training data sets of size n = 500 from Model III in (19) and one test
data set D′ of size n′ = 50. For each training data set D, B = 2000 bootstrap samples is used
to train RFIT and then the trained RFIT is applied to estimate ITE for each observation
in D′ together with standard errors. We repeat the experiment for 200 simulation runs. At
the end of the experiment, we have 200 predicted ITE ˆδ for each observation in D′, together
with 200 SEs. Accordingly, we compute the standard deviation (SD) of these ITE estimates
ˆδ and average the SE values. If the SE formula works well, the SE values should be close to
their corresponding SD values.
Figure 4 plots the averaged SE versus SD for each observation in the test sample D′. It
can be seen that the uncorrected standard errors are overly conservative. After the bias-
13


## Page 14


correction, they become reasonably close to the SD values. The bias-corrected SE presented
here is computed from (9).
The other version (8) that is somewhat harder to compute
provides very similar results, which have been omitted from the plotting.
We experimented with other models in Section 3.2 and similar results were obtained. One
issue pertains to the number B of bootstrap samples needed. According to Efron (2014), a
large B, e.g., B = 2, 000 is needed to guarantee the validity of IJ-based standard errors. We
experimented with diﬀerent B values. Generally speaking, ITE estimation stabilizes quickly
even with a small B, e.g., B = 100; however, negative values may frequently occur to the
bias-corrected variance estimates in both (8) and (9) when B is small or moderate, e.g.,
B = 500. Thus a large number B of bootstrap samples are needed to have sensible results
for the SE formulas.
4
Application: Acupuncture Trial
For further illustration of RFIT, we consider data collected from a acupuncture headache
trial (Vickers et al., 2004), available at
https://trialsjournal.biomedcentral.com/articles/10.1186/1745-6215-7-15
In this randomized study, 401 patients with chronic headache, predominantly migraine, were
randomly assigned either to receive up to 12 acupuncture treatments over three months or
to a control intervention oﬀering usual care. Among many other measurements, the primary
end point of the trial is the change in headache severity score from baseline to 12 months
since study entry. The acupuncture treatment was concluded eﬀective overall by signiﬁcantly
bringing down the headache score and other outcome measures. More details of the trial
and the results are reported in Vickers et al. (2004).
To apply RFIT, we consider only the 301 participants who completed the trial. The
response variable is taken as the diﬀerence in headache severity score between baseline and
12 months, while the score at baseline is treated as a covariate. A total of 18 covariates
are included in the analysis, which are essentially demographic, medical, or treatment vari-
ables measured at baseline. See Table I in the Supplementary Materials for a brief variable
description.
A total of B = 2, 000 trees are used to build RFIT, where the scale parameter a is
set as a = 10 in SSS splitting.
ITE is estimated for each individual in the same data
set and the IJ-based standard error (SE) with bias correction is also computed. Figure 5
provides a bar plot of the estimated ITE, plus and minus one SE, sorted by ITE. It can
be seen that a majority of ITE are above 0, indicating the eﬀectiveness of acupuncture.
Overall speaking, the treatment eﬀects in this trial show certain heterogeneity, but not by
much. It is interesting to note that the averaged ITE is 3.9. Comparatively, the unadjusted
14


## Page 15


mean diﬀerence in headache score is 6.5 while the adjusted eﬀect from ANCOVA is 4.6, as
reported in Table 2 of Vickers et al. (2004). Figure 5 also shows many individuals, for whom
the acupuncture treatment did not help much, including two individuals, the 44-th (with
patient ID 222) and the 224th (with patient ID 630). Both are female patients aged 60
and 58, suﬀer migraine, and were assigned to the control group, but surprisingly achieved a
reduction of 36 and 29.75 in severity score, respectively. Their initial severity scores are also
relatively similar: 44.25 and 37. Their estimated ITEs turn out to be −14.81 and −9.09,
indicating a detrimental eﬀect from acupuncture. Although the performances of these two
patients are quite unusual relative the the remainder of the patients, they may indicate a
small subgroup that is worth further investigation.
5
Discussion
We have tackled the problem of estimating individualized treatment eﬀect (ITE) by using
the random forests of interaction trees (RFIT). Smooth sigmoid surrogate (SSS) splitting is
introduced to speed up RFIT and possibly improve its performance. We have also applied the
inﬁnitesimal jackknife method to derive a standard error for the estimated ITE. Altogether,
RFIT provides enlightening results in deploying personalized medicine by informing a new
patient about the potential eﬃcacy of the treatment on him/her.
According to our numerical experiments, RFIT outperforms the commonly used separate
regression (SR) approach for estimating ITE. SR estimates the potential outcomes separately
and then takes diﬀerence. In RFIT, however, we ﬁrst group individuals so that those with
similar treatment eﬀects are put together and then estimate the treatment eﬀect by taking
diﬀerences within each group. Comparatively, RFIT focuses on predictive covariates and
estimation of ITE directly while SR has to deal with prognostic covariates and works on
a harder problem. Since SR has been widely used as an intermediary step in other causal
inference procedures, our method might contribute to their improvement as well.
To conclude, we identify several avenues for future research. First of all, our discussion
has been restricted to data from randomized experiments. Assessing treatment eﬀects with
data from observational data can be very diﬀerent, entailing adjustment for potential con-
founders. See, e.g., Su et al. (2012) and Wager and Athey (2016). Secondly, the standard
error formula provides some assessment for precision in estimating ITE; however, issues such
as consistency of RFIT, asymptotic normality of estimated ITE (see comments in Efron,
2014) and multiplicity have not been thoroughly addressed as of yet. Thirdly, besides vari-
able importance ranking, several other useful features from random forests including partial
dependence plots and proximity matrix (Liaw and Wiener, 2002) have yet to be explored for
RFIT.
15


## Page 16


Acknowledgements
XS was partially supported by NIMHD grant 2G12MD007592 from NIH; LL was partially
supported by AHRQ grant HS 020263; RL was supported in part by NSF grant 1633130.
References
Ballman, K. V. (2015). Biomarker: Predictive or Prognostic? Journal of Clinical Oncology,
33: 3968–3971.
Breiman, L. (1999). Using adaptive bagging to debias regressions. Technical Report # 547,
Department of Statistics, University of California at Berkely.
Breiman, L. (2001). Random Forests. Machine Learning, 45: 5–32.
Breiman, L., Friedman, J., Olshen, R., and Stone, C. (1984). Classiﬁcation and Regression
Trees. Belmont, CA: Wadsworth International Group.
Brent, R. (1973). Algorithms for Minimization without Derivatives. Englewood Cliﬀs, NJ:
Prentice-Hall.
Dusseldorp, E. and van Mechelen, I. (2014). Qualitative interaction trees: a tool to identify
qualitative treatment-subgroup interactions. Statistics in Medicine, 33: 219–237.
Efron, B. (1982). The jackknife, the bootstrap and ohter resampling plans. CBMS-NSF
Regional COnference Series in Applied Mathematics 38. Philadelphia, PA: Society for
Industrial and Applied Mathematics (SIAM).
Efron, B. (2014). Estimation and accuracy after model selection (with discussion). Journal
of the American Statistical Association, 109: 991–1007.
Foster, J. C., Taylor, J. M. C., and Ruberg, S. J. (2011). Subgroup identiﬁcation from
randomized clinical trial data. Statistics in Medicine, 30: 2867–2880.
Friedman, J. H. (1991). Multivariate adaptive regression splines. Annals of Statistics, 19:
1–67.
Imai, K. and Ratkovic, M. (2013). Estimating treatment eﬀect heterogeneity in randomized
program evaluation. The Annals of Applied Statistics, 7: 443–470.
16


## Page 17


Laber, E. B. and Zhao, Y. Q. (2015). Tree-based methods for individualized treatment
regimes. Biometrika, 102: 501–514.
LeBlanc, M. and Crowley, J. (1993). Survival trees by goodness of split. Journal of the
American Statistical Association, 88: 457–467.
Liaw, A. and Wiener, M. (2002). Classiﬁcation and Regression by randomForest. R News,
2/3: 18–22.
Lipkovich, I., Dmitrienko, A., D’Agostino, R. B. (2017). Tutorial in biostatistics: data-driven
subgroup identiﬁcation and analysis in clinical trials. Statistics in Medicine, 36: 136–196.
Lipkovich, I., Dmitrienko, A., Denne, J., and Enas, G. (2011). Subgroup identiﬁcation based
on diﬀerential eﬀect search (SIDES): a recursive partitioning method for establishing re-
sponse to treatment in patient subpopulations. Statistics in Medicine, 30: 2601–2621.
Loh, W.-Y., He, X., and Man, M. (2015). A regression tree approach to identifying subgroups
with diﬀerential treatment eﬀects. Statistics in Medicine, 34: 1818–1833.
Murphy, S. A. (2003). Optimal dynamic treatment regimes (with discussion). Journal of the
Royal Statistical Society, Series B, 65: 331–366.
Neyman, J. (1923). On the application of probability theory to agricultural experiments.
Essay on Principles, Section 9. Statistical Science, 5: 465–472, 1990. Translated by Dorota
M. Dabrowska and Terence P. Speed.
R Core Team (2017). R: A language and environment for statistical computing. R Foundation
for Statistical Computing, Vienna, Austria. URL https://www.R-project.org/.
Rosenbaum, P. R. and Rubin, D. B. (1983). The central role of the propensity score in
observational studies for causal eﬀects. Biometrika, 70: 41–55.
Rubin, D. B. (1974). Estimating Causal Eﬀects of Treatments in Randomized and Nonran-
domized Studies. Journal of Educational Psychology, 66: 688–701.
Rubin, D. B. (2005). Causal inference using potential outcomes: Design, modeling, decisions.
Journal of the American Statistical Association, 100: 322–331.
Shen, J. and He, X. (2015). Inference for Subgroup Analysis with a Structured Logistic-
Normal Mixture Model. Journal of the American Statistical Association, 110: 303–312.
17


## Page 18


Su, X., Kang, J., Fan, J., Levine, R., and Yan, X. (2012). Facilitating score and causal
inference trees for large observational data. Journal of Machine Learning Research, 13:
2955–2994.
Su, X., Tsai, C.-L., Wang, H., Nickerson, D. M., and Li, B. (2009). Subgroup analysis via
recursive partitioning. Journal of Machine Learning Research, 10: 141–158.
Utgoﬀ, P. E., Berkman, N. C., and Clouse, J. A. (1997). Decision tree induction based on
eﬃcient tree restructuring. Machine Learning, 29: 5–44.
Wager, S., Hastie, T., and Efron, B. (2014). Conﬁdence intervals for random forests: The
jackknife and the inﬁnitesimal jackknife. Journal of the Machine Learning Research, 15:
1625–1651.
Wager, S. and Athey, S. (2016). Estimation and inference of heterogeneous treatment eﬀects
using random forests. arXiv preprint, arXiv:1510.04342v3.
van der Laan, M., Polley, E., and Hubbard, A. (2007). Super Learner. Statistical Applications
in Genetics and Molecular Biology, 6(1).
Vickers, A. J., Rees, R. W., Zollman, C. E., McCarney, R., Smith, C., Ellis, N., Fisher, P.,
and Van Haselen, R. (2004). Acupuncture for chronic headache in primary care: large,
pragmatic, randomised trial. British Medical Journal, Primary Care, 328: 744–749.
Zhang, B., Tsiatis, A. A., Davidian, M., Zhang, M., and Laber, E. (2012). Estimating optimal
treatment regimes from a classiﬁcation perspective. STAT, 1: 103–114.
18


## Page 19


Table 1: Computing time comparison between smooth sigmoid surrogate (SSS) and greedy
search (GS) in ﬁnding the best cutoﬀpoint for one covariate. Entries are the computing
times (in seconds) averaged over 10 runs.
K = 10
K = 100
K = 500
GS
SSS
GS
SSS
GS
SSS
n =
50
0.000
0.001
0.003
0.000
0.003
0.000
100
0.000
0.000
0.006
0.000
0.003
0.004
500
0.002
0.000
0.012
0.003
0.047
0.000
1000
0.004
0.000
0.023
0.002
0.100
0.000
2000
0.003
0.004
0.038
0.005
0.201
0.003
5000
0.008
0.002
0.094
0.002
0.462
0.001
10,000
0.017
0.005
0.182
0.005
0.899
0.010
19


## Page 20


−3
−2
−1
0
1
2
3
0.0
0.2
0.4
0.6
0.8
1.0
(a)
x
expit(a.x)
a=1
a=2
−2
−1
0
1
2
0
1
2
3
4
(b)
cutoff point c
Q(c)
Figure 1: Illustration of Smooth Sigmoid Surrogate (SSS) for Splitting Data: (a) The discrete
threshold function ∆(x; c) = I(x ≥c) with c = 0 (in orange) and its expit approximation
s(x; c) = expit{a x −c)} (in gray); (b) The splitting statistic Q(c) computed at each cutoﬀ
point c in greedy search and its SSS approximations with a = {1, 2, . . . , 100}. In panel (b),
data of size n = 500 are generated from model y = 0.5 + 0.5 T + 0.5 ∆+ 0.5 · T ∆+ ε, where
∆= ∆(x; c0) with true cutoﬀpoint c0 = 0 (indicated by the green dashed vertical line) and
both x and ε are from N(0, 1). The best cutoﬀfound by GS is denoted by the red triangle
while the black diamond dots indicate the best cutoﬀpoints found by SSS with diﬀerent a
values.
20


## Page 21


0.0
0.2
0.4
0.6
0.8
1.0
0.0
0.5
1.0
1.5
c
Density
(a)
0
20
40
60
80
100
0.04
0.05
0.06
0.07
0.08
0.09
a
MSE
(b)
0.0
0.2
0.4
0.6
0.8
1.0
0.0
0.5
1.0
1.5
2.0
2.5
3.0
c
Density
(c)
0
20
40
60
80
100
0.010
0.015
0.020
0.025
0.030
a
MSE
(d)
Figure 2: Comparing SSS with GS in Finding the Best CutoﬀPoint: the left panels present
the empirical density of ˆc from 500 runs found by GS (shaded in orange) and SSS (in
grayscale) with a = 1, 2, . . . , 100, where the true cutoﬀpoint c0 = 0.5 is indicated by the
green vertical bar; the right panels present MSE measures of SSS for diﬀerent a values, where
the horizonal orange line corresponds to the MSE from GS. Panels diﬀer in terms of sample
size n: n = 50 in Panels (a) & (b); n = 500 in Panels (c) & (d).
21


## Page 22


RFIT
SR
0.2
0.4
0.6
0.8
(a) Model I, n= 100
MSE
RFIT
SR
0.15
0.20
0.25
0.30
0.35
(b) Model I, n= 500
MSE
RFIT
SR
0.5
1.0
1.5
2.0
(c) Model II, n= 100
MSE
RFIT
SR
0.3
0.4
0.5
0.6
0.7
(d) Model II, n= 500
MSE
RFIT
SR
1.0
1.5
2.0
2.5
3.0
3.5
(e) Model III, n= 100
MSE
RFIT
SR
0.4
0.6
0.8
1.0
1.2
1.4
(f) Model III, n= 500
MSE
RFIT
SR
0.6
0.8
1.0
1.2
1.4
1.6
1.8
2.0
(g) Model IV, n= 100
MSE
RFIT
SR
0.5
0.6
0.7
0.8
0.9
(h) Model IV, n= 500
MSE
Figure 3: Comparing RFIT with Separate Regression (SR) in Estimating ITE: parallel
boxplots of MSE values are based on a test sample of n′ = 2000 with 200 simulation runs.
The blue middle bar indicates the average of MSE measures.
22


## Page 23


0.55
0.60
0.65
0.70
0.75
0.6
0.8
1.0
1.2
SD
Averaged SE
Uncorrected
Bias−Corrected
Figure 4: Plot of averaged standard errors (SE) versus sample standard deviation (SD) of
predicted ITE ˆδ(x) for n′ = 50 observations in a test sample. The standard deviation (SD)
are computed based on 200 simulation runs while the standard errors (SE) are averaged
over the 200 runs. In each simulation run, a training sample of size n = 500 is generated
from Model III in (19) and a bootstrap size B = 2000 is used to build RFIT. The bias-
corrected and uncorrected SE averages for the same observation are connected with a gray
line segment. The reference line in green is y = x.
23


## Page 24


0
50
100
150
200
250
300
−10
0
10
20
Error Bar for Estimated ITE: The Headache Data
rank by ITE
δ^
Figure 5: RFIT Analysis of the Headache Data: the error bar plot of the estimated ITE ± SE.
Individuals are ranked by estimated ITE. The gray horizontal line indicates the unadjusted
average treatment eﬀect 6.484, i.e., the mean diﬀerence in headache severity score.
24


## Page 25


Supplementary Materials to
“Random Forests of Interaction Trees for Estimating
Individualized Treatment Eﬀects in Randomized
Trials”
A
Proofs
This section contains proofs to the propositions.
A.1
Proof of Proposition 2.1
When the GS splitting is conducted without updating, GS evaluates the splitting criterion
Q(c) for every distinct splitting points of X. For each c, computation of Q(c) is O(n). Note
that extracting the unique values of X is O(n) in general. Therefore, the total complexity
amounts to O(Kn) in this case, where K is the number of distinct values of X. Since X is
continuous with K = O(n), the complexity becomes O(n2).
GS can be alternatively done via an updating formula. This entails sorting the yi and Ti
values in the ascending (or descending) order of distinct X values so that the Q(c) value at
cutoﬀpoint c can be conveniently obtained by utilizing its previous value at the neighboring
cutoﬀpoint. The computation involved in the updating step itself is negligible and does
not escalate the computational complexity level O(n) asymptotically. Nevertheless, a stable
algorithm for general-purpose sorting is at best O{ln(n) n}. For example, the sort function
in R is either O(n4/3) if Shellsort is used or O{ln(n) n} if the Quicksort method is used.
For SSS, each iterative step in Brent’s method involves evaluation of Q(c), which is O(n).
SSS requires standardization of X and transformation of ˆc back to the original scale, both
operations being O(n). Put together, its complexity is O(mn), where m is the number of
iterative steps in the optimization algorithm.
■
A.2
Proof of Proposition 2.2
The proof essentially follows Efron (2014) and Wager, Hastie, and Efron (2014), with more
details added and some rewriting mainly for our own understanding. The arguments are
based on the the ‘ideal bootstrap’ and treat the current data D as ﬁxed, where B = nn
corresponds to all possible choices when taking a bootstrap sample from D.
Let Db denote the b-th re-sample for b = 1, . . . , B. Introduce random vector Nb =
(Nb1, . . . , Nbn)T, where Nbi counts the frequency that the i-th observation in D shows up in Db
1


## Page 26


with Pn
i=1 Nb = n. It follows that Nb ∼Multinomial(n; p0) with p0 = (1/n, . . . , 1/n)T ∈Rn.
Fixing D, Nb completely determines Db. Thus, the ITE estimate ˆδb(x) based on Db can be
written as a function ˆδb = T(Nb) of Nb. The RFIT estimate ˆδ(x) with ideal bootstrap is
the expectation of T(Nb), i.e., ˆδ(x) = ENb{T(Nb)}. Since the distribution of Nb is fully
determined by the probability vector p0, rewrite ˆδ(x) as a function ˆδ(x) = S(p) of p if
more generally Nb ∼Multinomial(n; p). The symbol S(·) is used to denote this function,
for ensemble learners such as ˆδ(x) are essentially obtained via ‘bootstrap smoothing’.
Deﬁne the inﬂuence function ˙Si
˙Si = lim
ǫ→0+
S(p0 + ǫ(ei −p0)) −S(p0)
ǫ
(A.1)
for i = 1, 2, . . . , n, where ei = (0, . . . , 0, 1, 0, . . ., 0)T ∈Rn with 1 in the ith place and 0
elsewhere is a special case of p that assigns mass 1 to the i-th observation. Namely, the
inﬂuence function ˙Si is the directional derivative of S(p) at p0 in the direction of ei −p0,
which essentially inspects the eﬀect of an inﬁnitesimal contamination at the ith observation
on the estimator.
The inﬁnitesimal jackknife method (Efron, 1982) provides an estimate of variance for
ˆδ(x) given by
ˆ
var(ˆδ(x)) =
n
X
i=1
˙S2
i /n2.
(A.2)
Thus it remains to compute ˙Si.
For a multinomial probability p = (pi)n
i=1, consider
S(p) =
B
X
b=1
(
ˆδb(x) ·
n
Y
i=1
pNbi
i
)
=
B
X
b=1
wb(p)ˆδb(x)
B
,
(A.3)
where wb(p) = Qn
i=1(npi)Nbi is the ratio of the product of probabilities in p to that in p0.
Note that the multinomial coeﬃcient
 n
Nb1,Nb2,...,Nbn

does not show up in the summand of
(A.3) since all B = nn choices of bootstrap samples are listed in the sum, in which case some
of the bootstrap samples can be identical when ignoring the order of observations.
When
p = p0 + ǫ(ei −p0) =
1 −ǫ
n
, . . . , 1 −ǫ
n
, 1 + ǫ(n −1)
n
, 1 −ǫ
n
, . . . , 1 −ǫ
n
T
2


## Page 27


with (1 + ǫ(n −1))/n in the i-th position and (1 −ǫ)/n elsewhere, we have, letting ǫ →0+,
wb(p)
=
(1 −ǫ)
P
i′̸=i Nbi′{1 + (n −1)ǫ}Nbi
≈
(1 −ǫ
X
i′̸=i
Nbi′) · {1 + (n −1)ǫNbi} ;
=
1 −ǫ
X
i′̸=i
Nbi′ + (n −1)ǫNbi + Op(ǫ2)
≈
1 + nǫ(Nbi −1)
where the second step uses the fact (1+x)a ≈1+ax for |x| < 1 and any constant a obtained
from the bionomial series and the fourth step ignores a second-order term of ǫ. Bringing
wb(p) into (A.3), it follows that
S(p0 + ǫ(ei −p0)) ≈S(p0) + nǫ
B
X
b=1
(Nbi −1)ˆδ/B = S(p0) + nǫ ¯Zi,
using the fact that Pm
i=1(xi −¯x)(yi −¯y) = P
i(xi −¯x)yi for any m real-valued pairs (xi, yi).
According to its deﬁnition in (A.1), it is clear that ˙Si = n ¯Zi. Bringing it back into (A.2)
yields the needed result for ˆV in (7). An alternative way of deriving ˆVc is via H´ajek projection
as in Wager, Hastie, and Efron (2014).
□
In practice, a total of ﬁnite B bootstrap sample is taken instead, which makes ˆV subject to
additional Monte Carlo noise. Following the bias correction step suggested by Efron (2014),
let ˜Zi = PB
b=1 Zbi/B denote the ¯Zi value obtained from B bootstrap samples, as opposed to
¯Z obtained from the ideal bootstrap. Thus ˜Zi has bootstrap mean ¯Zi and bootstrap variance
ν2
i /B, where ν2
i denote the bootstrap variance of Zbi. It follows that
EB ˜V = EB(
n
X
i=1
˜Z2
i ) =
n
X
i=1
¯Z2
i +
n
X
i=1
ν2
i /B,
where EB(·) denotes bootstrap expectation. Therefore, a bias-corrected version for ˆV is given
by
ˆVc = ˆV −1
B
n
X
i=1
ˆν2
i ,
(A.4)
where v2
i is replaced with its estimate ˆν2
i = PB
b=1(Zbi −˜Zi)2/B. This gives the expression in
(8).
3


## Page 28


Wager, Hastie, and Efron (2014) further assumed that Nbi and ˆδ(x) in Zbi are approxi-
mately independent. Under this assumption, we have
ν2
i = varB(Zbi)
=
varB
h
(Nbi −1){ˆδb(x) −ˆδb(x)}
i
=
varB(Nbi) · varB(ˆδb(x))
=
n −1
n
· varB(ˆδb(x)),
where varB(Nbi) = n(1/n)(1 −1/n) = (n −1)/n.
Thus Zbi becomes homoscedastic for
diﬀerent i (i.e., with equal bootstrap variance). A natural estimate of v2
i is
ˆv2
i = n −1
n
· 1
B
B
X
b=1
{ˆδb(x) −ˆδ(x)}2.
Bringing ˆv2
i into (A.4) yields the bias-corrected version in (9). This completes the proof. ■
A.3
Proof of Proposition 2.3
For the RFIT estimate ˆδ(X), rewrite EX,D,B{ˆδ(X) −δ(X)}2 as
EX,D,B
hn
ˆδ(X) −¯δ(X; D)
o
+
¯δ(X; D) −¯δ(X)
	
+
¯δ(X) −δ(X)
	i2
.
(A.5)
By the deﬁnitions of {¯δ(X; D), ¯δ(X)}, each of the cross-product terms amounts to 0, which
leads immediately to (14).
For the SR estimate ˆδ(X) in (10),
AMSE
=
EX,D,B [{ˆµ1(X) −µ1(X)} −{ˆµ0(X) −µ0(X)}]2
=
EX,D,B {ˆµ1(X) −µ1(X)}2 + EX,D,B {ˆµ0(X) −µ0(X)}2
−2EX,D,B {ˆµ1(X) −µ1(X)} {ˆµ0(X) −µ0(X)}
The ﬁrst two terms can be rewritten in a similar manner to (A.5), with all cross-product
terms being 0. For the last term, note that ˆµ1(X) and ˆµ0(X) are based on the separate parts
of data D and hence are independent given D. It follows that
EX,D,B {ˆµ1(X) −µ1(X)} {ˆµ0(X) −µ0(X)}
=
EX [ED,B {ˆµ1(X) −µ1(X)} · ED,B {ˆµ0(X) −µ0(X)} | X]
=
EX [{¯µ1(X) −µ1(X)}{¯µ0(X) −µ0(X)}] .
The proof is completed.
■
4


## Page 29


B
Additional Numerical Results
We have implemented RFIT with R (R Core Team, 2017) and an R package RFIT is un-
derway. This section contains additional numerical results that we have omitted from the
manuscript due to page limitation and presents a variable description for the headache data
set used in Section 4.
B.1
Bias in Section 3.2
As we have discussed in Section 2.3, SR may suﬀer more from the bias problem.
This
perspective can be further explored by plotting the predicted ITE ˆδ versus the true ITE δ.
With the same settings as in Section 3.2, Figure I provides such a plot for Model III in
(19) as an example. Here the predicted ˆδ(x) for each of n′ = 2000 observations in a test
sample are averaged over 200 simulation runs, yielding an estimate of ED,B(ˆδ(x)) or ¯δ(x)
in Proposition 2.3, and then plotted versus the true ITE δ(x). The smoothed scatterplot
is used because of the large sample size and hence many overlapping dots. The left panels
(a) & (c) have RFIT predictions on the vertical axis while the right panels (b) & (d) have
SR predictions on the vertical axis. Each panel is superimposed with the LS ﬁtted line, as
well as the reference line y = x with perfect prediction. Panels (a) & (b) are based on same
training data sets of size n = 100; for comparison purposes, we have made the ranges for the
vertical axis the same; similarly for Panels (c) & (d).
Referring to the line y = x, both RFIT and SR are subject to bias in predicting high
and low values of ITE. They tend to cut the hill (predicting high ITE values lower) and ﬁll
the valley (predicting low ITE values high). However, this bias problem is more prominent
for SR than for RFIT. With increased sample sizes (n = 500), the bias is diminishing for
RFIT but remains substantial for SR. For the same reason, the range of SR estimates is
narrower than that of RFIT, resulting in smaller variances though. Similar patterns can
be observed with other models and conﬁgurations, for which the plots are omitted here.
Another potential source of bias for RFIT stems from unbalanced covariates within terminal
nodes. Although the treatment assignment is randomized for the entire study, the balance
among covariate distributions might be lost as the tree grows. Thus, additional adjustment
for confounders within terminal nodes might further improve RFIT.
B.2
Variable Description for the Headache Data
The headache data set that was used for illustration of RFIT in Section 4 contains 21
variables on 301 subjects who completed the trial.
There are three subjects with some
5


## Page 30


missing data, which are imputed with random forests (see R pacakge missForest; Stekhoven
and Buehlmann, 2012). A brief variable description for the ﬁnal compiled data is provided
in Table I, where the variable names are consistent with those in the original data ﬁle from
(Vickers et al., 2004) and Vickers (2006).
Additional References
R Core Team (2017). R: A language and environment for statistical computing. R Founda-
tion for Statistical Computing, Vienna, Austria. URL https://www.R-project.org/.
Stekhoven, D. J. and Buehlmann, P. (2012). missForest – nonparametric missing value
imputation for mixed-type data. Bioinformatics, 28: 112–118.
Vickers, A. J. (2006). Whose data set is it anyway? Sharing raw data from randomized
trials. Trials, 7: 15. doi: 10.1186/1745-6215-7-15.
6


## Page 31


−4
−2
0
2
4
6
8
−3
−2
−1
0
1
2
3
4
(a) Model III, n= 100
true ITE
Averaged ITE via RFIT
−4
−2
0
2
4
6
8
−3
−2
−1
0
1
2
3
4
(b) Model III, n= 100
true ITE
Averaged ITE via SR
−4
−2
0
2
4
6
−4
−2
0
2
4
(c) Model III, n= 500
true ITE
Averaged ITE via RFIT
−4
−2
0
2
4
6
−4
−2
0
2
4
(d) Model III, n= 500
true ITE
Averaged ITE via SR
Figure I: Smoothed scatterplot of the predicted ITE ˆδ(x) averaged over 200 runs versus the
true ITE δ(x): RFIT (in gray and SR (in orange). Predictions are based on a test sample
of n′ = 2000 generated from Model III in (19). Two sample sizes n = 100 and n = 500 are
considered for the training sample. The green dashed line highlights the reference line y = x
with perfect prediction.
7


## Page 32


Table I: Variable Description for the Headache Data.
Name
Description
id
Patient ID code
diff
Diﬀerence in headache severity score between one year follow-up
and baseline, i.e., (pk5 - pk1)
group
0 is control; 1 is acupuncture
age
Age
sex
sex: 0 male; 1 female
migraine
Migraine: 0 No and 1 Yes
chronicity
Chronicity
pk1
Severity score at baseline
f1
Headache frequency at baseline
pf1
Baseline SF36 physical functioning
rlp1
Baseline SF36 role limitation physical
rle1
Baseline SF36 role limitation emotional
ef1
Baseline SF36 energy fatigue
ewb1
Baseline SF36 emotional well being
sf1
Baseline SF36 social functioning
p1
Baseline SF36 pain
gen1
Baseline SF36 general health
hc1
Baseline SF36 health change
painmedspk1
MQS at baseline
prophmqs1
MQS of prophylactic medication at baseline
allmedsbaseline
Total MQS at baseline
8

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1709_04862v1_random_forests_of_interaction_trees_for_estimating_individualized_treatment_effe
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2017/1709_04862V1_RANDOM_FORESTS_OF_INTERACTION_TREES_FOR_ESTIMATING_INDIVIDUALIZED_TREATMENT_EFFE.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1710.03496v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1710.03496v2_Admissible_multi-arm_stepped-wedge_cluster_randomized_trial_designs

> Source: 1710.03496v2_Admissible_multi-arm_stepped-wedge_cluster_randomized_trial_designs.pdf

> Pages: 31

---


## Page 1


Admissible multi-arm stepped-wedge cluster randomized
trial designs
M. J. Grayling1, A. P. Mander1, J. M. S. Wason1,2
1. Hub for Trials Methodology Research, MRC Biostatistics Unit, Cambridge, UK,
2. Institute of Health and Society, Newcastle University, Newcastle, UK.
Abstract: Numerous publications have now addressed the principles of designing, analyzing, and reporting the
results of, stepped-wedge cluster randomized trials. In contrast, there is little research available pertaining to the
design and analysis of multi-arm stepped-wedge cluster randomized trials, utilized to evaluate the eﬀectiveness of
multiple experimental interventions. In this paper, we address this by explaining how the required sample size in
these multi-arm trials can be ascertained when data are to be analyzed using a linear mixed model. We then go on
to describe how the design of such trials can be optimized to balance between minimizing the cost of the trial, and
minimizing some function of the covariance matrix of the treatment eﬀect estimates. Using a recently commenced trial
that will evaluate the eﬀectiveness of sensor monitoring in an occupational therapy rehabilitation program for older
persons after hip fracture as an example, we demonstrate that our designs could reduce the number of observations
required for a ﬁxed power level by up to 58%. Consequently, when logistical constraints permit the utilization of
any one of a range of possible multi-arm stepped-wedge cluster randomized trial designs, researchers should consider
employing our approach to optimize their trials eﬃciency.
Keywords: Admissible design, Cluster randomized trial, Multiple comparisons, Optimal design, Stepped-wedge.
Address correspondence to M. J. Grayling, MRC Biostatistics Unit, Forvie Site, Robinson Way, Cambridge CB2 0SR,
UK; Fax: +44-(0)1223-330365; E-mail: mjg211@cam.ac.uk.
1
arXiv:1710.03496v2  [stat.ME]  28 Jun 2018


## Page 2


1.
Introduction
In a cluster randomized trial (CRT), groups of participants, not individuals, are randomized. The advantages this
can bring are today recognized as numerous.
For example, CRTs can aid the control of contamination between
participants, and can bring increased administrative eﬃciency, helping to overcome the barriers of recruiting large
numbers of participants.[29] Unfortunately, there are also several well-noted disadvantages to CRTs.[7, 8] Speciﬁcally,
double blinding should ideally be present in every trial, however, it is often impossible in CRTs. Moreover, missing
data can quickly become a problem if whole clusters are lost to follow-up.
Nevertheless, there has now been much work conducted on design and analysis procedures for CRTs. One type of
CRT that has received considerable attention recently, and which we focus on here, is the stepped-wedge (SW)-CRT
(see, e.g., Hussey and Hughes (2007)[14]). In a SW-CRT, an intervention is introduced over several time periods, and
typically all clusters receive the intervention by the end of the trial. Numerous potential advantages to this design have
been forwarded. Principally, all clusters receiving the intervention is advantageous if it is expected to do more good
than harm. The design’s sequential implementation can also increase feasibility when there are logistical or practical
constraints. However, these alleged advantages have been disputed. Primarily, it has been argued that an intervention
should not be implemented in every cluster when it has not yet been proven to be eﬀective. For brevity, we refer the
reader elsewhere for further discussion of these points.[23, 11, 15, 16, 17, 18, 5, 10, 26]
Methodological developments in this area include Hussey and Hughes (2007),[14] who provided guidance on sample
size calculations for cross-sectional SW-CRTs analyzed with a particular linear mixed model. Here, cross-sectional
designs refer to a scenario in which measurements are accrued on diﬀerent participants in each time period. This work
was later built upon to establish a design eﬀect for cross-sectional SW-CRTs,[31] and also to allow for transition periods
and multiple levels of clustering.[12] Recently, similar results for cohort SW-CRTs, in which repeated measurements
are accrued on a single group of patients, have been presented.[13] Finally, explanations on determining the sample
size required by SW-CRTs through simulation have also been presented[2].
Thus, sample size determination for SW-CRTs has been well studied. However, the above articles only discuss
sample size calculations for a particular design. That is, a design with prescribed rules about how the experimental
intervention will be allocated across the clusters. Moreover, with the exception of Baio et al. (2015),[2] each paper deals
only with a speciﬁc analysis model. Addressing these limitations, recent research has ascertained optimal treatment
allocation rules for several general classes of cross-sectional SW-CRT design, analyzed with a highly ﬂexible linear
mixed model.[19, 9, 28] A subset of these results has subsequently been extended to cohort SW-CRTs.[20] Nonetheless,
there is still a need for guidance on the optimal design of SW-CRTs with more specialized analysis models.
Furthermore, the above publications relate only to the design of two-arm SW-CRTs. Very little research has been
conducted on the design of CRTs with multiple experimental treatment arms, and in particular scenarios in which
clusters may switch between interventions. We refer to such designs in this article as multi-arm stepped-wedge cluster
randomized trials (MA-SWs). Formulae for the variance of the treatment eﬀect estimators of several possible designs
with three treatment arms, using a speciﬁc linear mixed model for data analysis, are available.[27] An additional paper
recently proposed, and compared the eﬃciencies of, several simple variants of the classical SW-CRT design that could
2


## Page 3


be used to accommodate multiple interventions.[21] Finally, utilizing experimental design theory, the performance of
several analysis models for the same such MA-SW designs was recently examined.[22] However, these are the only
works that we are aware of pertaining to the design of MA-SWs. This is perhaps surprising since several studies
have recently been conducted in such a manner.[4, 25] Furthermore, intuitively these designs could have numerous
advantages that it would be beneﬁcial to highlight. Explicitly, evaluating multiple interventions within the same CRT
could bring the same sort of eﬃciency gains multi-arm trials bring to individually randomized studies.[24] That is, the
required number of clusters or observations could be reduced relative to conducting several separate trials. Moreover,
it could allow for a reduction in required funding as a consequence of reduced administrative costs, and may allow
for the assessment of intervention interactions. Furthermore, one would anticipate that such designs could on average
decrease the time taken for each cluster to receive a particular intervention, which may improve cluster and patient
participation. However, the potential of MA-SWs can only be realised if we design such studies eﬀectively; poorly
designed MA-SW trials would likely result in a poor answer being acquired to numerous important questions.
Therefore, here, we ﬁrst discuss how one can compute the sample size required by, and optimized treatment
sequence allocations for, a MA-SW design when a linear mixed model is used for data analysis. We then consider one
particular analysis model, and utilizing a recently undertaken trial as our principal motivation, discuss how large the
eﬃciency gains made using our methods could be in practice.
2.
Methods
2.1.
Notation, hypotheses, and analysis
We designate a MA-SW as any trial conforming to the following requirements
• The trial is carried out in C ≥2 clusters, over T ≥2 time periods, with m > 1 measurements made in each
cluster in each time period;
• In each time period, each cluster receives a combination of a set of D interventions (indexed by d = 0, . . . , D−1);
• The sequence of intervention allocations for each cluster is speciﬁed randomly.
We make no assumptions about whether the m measurements from each time period are on diﬀerent patients; a
cross-sectional design, or the same patients; a cohort design. We do not require each cluster to begin on, receive, or
conclude the trial on any particular intervention. We also do not enforce the usual one-directional switching associated
with conventional SW-CRTs, so as to allow for transitions between experimental interventions in any order, if this
is desired. As a consequence of this, the methodology we describe is applicable to the design of multi-arm cluster
randomized crossover trials. We keep in mind, however, that each of the interventions must be received by at least
one cluster in some time period for its eﬀect to be estimable.
Throughout we assume that the accrued data from the trial will be normally distributed, and an identiﬁable linear
mixed model will be utilized for data analysis, denoted as
3


## Page 4


y = Aβ + Zu + ϵ,
where
• y is the vector of responses;
• β = (β1, . . . , βp)⊤is a vector of p ﬁxed eﬀects;
• A is the design matrix which links y to β;
• u is a vector of random eﬀects, with u ∼N(0, G), where G is a speciﬁed (assumed known) matrix;
• Z is the design matrix which links y to u;
• ϵ is a vector of residuals, with ϵ ∼N(0, R), where R is a speciﬁed (assumed known) matrix.
We suppose that β has been speciﬁed such that its ﬁrst q, q ≤p, elements, (β1, . . . , βq)⊤, are our parameters of
interest. Typically, we may have that q = D −1, with these parameters representing either the direct eﬀects of a set of
experimental interventions relative to some control, or the direct eﬀect of intervention arm d relative to intervention
arm d −1, for d = 1, . . . , D −1. However, we do not require that this be the case. Then, we assume that we will test
the following one-sided hypotheses
H0f : βf ≤0,
H1f : βf > 0,
f = 1, . . . , q.
We note though that the determination of MA-SW designs for alternative hypotheses of interest, e.g., two-sided
hypotheses, is also easily achievable by adapting what follows.
To test these hypotheses, following trial completion, we estimate β using the maximum likelihood estimator of a
linear mixed model
ˆβ = (ˆβ1, . . . , ˆβp)⊤= {A(ZGZ⊤+ R)−1A}−1A⊤(ZGZ⊤+ R)−1y.
Then
cov(ˆβ, ˆβ) = Λ = {A(ZGZ⊤+ R)−1A}−1.
We set ˆβq = (ˆβ1, . . . , ˆβq)⊤, and denote the covariance matrix of ˆβq by Λq. That is, cov(ˆβq, ˆβq) = Λq.
Our conclusions are then based upon the following Wald test statistics
Zf =
ˆβf
q
var(ˆβf)
= ˆβfΛ−1/2
[f,f] = ˆβfI1/2
f
,
f = 1, . . . , q.
Explicitly, we reject H0f if Zf > e, for critical boundary e. Given e, we can determine for any vector of true ﬁxed
eﬀects βq the probability each particular H0f is rejected, and the probability we reject at least one of H01, . . . , H0q,
via the following integrals
4


## Page 5


P(Reject H0f | βf) =
Z ∞
e
φ(x, βfI1/2
f
, 1)dx,
P(Reject at least one of H01, . . . , H0q | βq) = 1 −
Z e
−∞
· · ·
Z e
−∞
φ{x, βq ◦I1/2, diag(I1/2)Λqdiag(I1/2)}dxq . . . dx1.
Here
• φ(x, µ, Σ) is the probability density function of a multivariate normal distribution with mean µ = (µ1, . . . , µk)⊤
and covariance matrix Σ, dim(Σ) = k × k, evaluated at vector x = (x1, . . . , xk)⊤;
• (a1, . . . , an)⊤◦(b1, . . . , bn)⊤= (a1b1, . . . , anbn)⊤;
• I1/2 = (I1/2
1
, . . . , I1/2
q
)⊤is the element-wise square root of the vector of information levels for βq;
• diag(v) for a vector v indicates the matrix formed by placing the elements of v along the leading diagonal.
Determining an appropriate value for e depends upon whether a correction for multiple testing is to be utilized.
Without such a correction, e can be chosen to control the per-hypothesis error-rate to α by setting e as the solution
to
α =
Z ∞
e
φ(x, 0, 1)dx.
Alternatively, the familywise error-rate, the probability of one or more false rejections, can be controlled for example
using the Bonferroni correction, which sets in this instance e to be the solution of
α
q =
Z ∞
e
φ(x, 0, 1)dx.
The choice of whether to utilize a multiple testing correction is not a simple one, with much debate in the literature
around when it is necessary. It seems reasonable for MA-SWs however to extrapolate from previous discussions, and
note that one should correct in conﬁrmatory settings, but should not always feel the need to in exploratory settings.[30]
2.2.
Power considerations
The above fully speciﬁes a hypothesis testing procedure for a MA-SW. However, at the design stage, it is important to
be able to determine values of m, C, and T that provide both the desired per-hypothesis or familywise error-rate, and
the desired power. Here, we describe two types of power that could be required, since power is not a simple concept
in multi-arm trials.
We suppose that power of at least 1 −β is required either to reject each H0f (individual power), or at least one
of H01, . . . , H0q (combined power), when βq = δ = (δ1, . . . , δq)⊤. The element δf here represents a clinically relevant
diﬀerence for the eﬀect βf. Using our notation from earlier, these requirements can be written as
5


## Page 6


min
f∈{1,...,q} P(Reject H0f | δf) ≥1 −β,
P(Reject at least one of H01, . . . , H0q | δ) ≥1 −β.
The choice between these requirements should be made based on several considerations. The latter will likely
require smaller sample sizes, however it would leave a trial less likely to reject all false null hypotheses. Therefore,
trialists must weigh up the cost restrictions and goals of their trial.
2.3.
Design speciﬁcation
We can now return to our considerations on determining appropriate values for m, C, and T. We must also determine
as part of the same process a matrix X that indicates the planned allocation of interventions to each cluster across
the time periods. Extending the notation commonly utilised for SW-CRTs, X is a C × T matrix, with Xij indicating
which intervention(s) cluster i receives in time period j. If only a single intervention is given to each cluster in each
time period, then Xij will be a single number. Otherwise, it may be some combination of values, indicating allocation
to multiple interventions. With this, it will now be useful to denote the design utilized by a trial by D = {m, C, T, X},
and the associated covariance matrix for βq by ΛD. Our goal is then to optimize D.
Most of the work on sample size determination for SW-CRTs pre-supposes that two of the three parameters m, C,
and T are ﬁxed (with one usually T), and then looks to identify the third. In addition, the matrix X is usually speciﬁed,
if not explicitly (in the case where C and T are ﬁxed), then through some rule such as balanced stepping. Here, we
take an alternate approach to the determination of the preferred design. We assume that a set of allowed values for T
has been speciﬁed, T = {T1, . . . , T|T|}. We then suppose that sets of allowed values for C, for each element of T, have
been speciﬁed. We denote these by C = {CT1, . . . , CT|T|}, with CTi = {C1, . . . , C|CTi|}. Furthermore, we suppose that
for each allowed C,T combination, a set of allowed values for m have been provided; MC,T = {m1, . . . , m|MC,T |}. We
then take M = {MC,T : T ∈T, C ∈CT }. We allow for such an interrelated speciﬁcation of the values for m, C, and T
to cover many possible design scenarios. For example, increasing the value of T may mean logistical constraints force
only lower values of m and C to be possible. In actuality, it is likely a trialist would not need such a complicated
structure. For example, the classical case of ﬁxed T and m, searching for the correct value for C, would require only
T = {T}, MC,T = {m}, and C = {CT }, with CT = {2, . . . , Cmax}, and Cmax some suitably large value.
Finally, for each C, T combination, we also specify a set of allowed X, which we denote by XC,T . Similar to the
above, we then take X = {XC,T : T ∈T, C ∈CT }. Shortly, we will describe several possible ways in which XC,T could
be speciﬁed.
Now, with T, C, M, and X chosen, formally our set D of all allowed possible designs is
D = {D : T ∈T, C ∈CT , m ∈MC,T , X ∈XC,T }.
6


## Page 7


2.4.
Admissible design determination
As was discussed, previous research has assessed which is the optimal SW-CRT design to maximize power in an array
of possible design scenarios. This was achieved by developing formulae for the eﬃciency of designs under particular
linear mixed models. Such considerations could in theory be extended to MA-SWs, or to alternate analysis models.
However, it is not practical to conduct such derivations for every value of D, or every analysis model that may need
to be utilized. In addition, it is not actually necessary following speciﬁcation of the set D: preferable designs can be
determined using exhaustive or stochastic heuristic searches.
Explicitly, for some D, modern computing makes an exhaustive search possible using parallelisation. Alternatively,
in the case where C and T are ﬁxed (either in advance or after some initial design identiﬁcation), we can employ a
diﬀerent method to determine our ﬁnal design: a stochastic search. This is sensible when, even with C and T ﬁxed,
the design space D remains large. Here, we accomplish this optimization using CEoptim in R.[3]
To perform a search, an optimality criterion is required. Previous research on SW-CRTs has focused on determining
designs that minimize the variance of the treatment eﬀect estimator. Here, we extend this to consider designs that
minimize some weighted combination of a trial cost function, and some factor formed from the covariance matrix of
the treatment eﬀect estimators, ΛD.
Speciﬁcally, we allocate a function f(D) that sets the cost associated with a trial using design D. This could be as
simple as the required number of observations, or something more complex that factors in the speed the interventions
would need to be rolled out according to X, for example.
For ΛD, numerous possible optimality criteria have been suggested in the literature. We consider D-, A-, and
E-optimal designs, which all have a long history within the ﬁeld of experimental design. D-optimality corresponds
to minimizing the determinant of ΛD, det(ΛD). This can be interpreted as minimizing the volume of the conﬁdence
ellipsoid for the βf.
For A-optimality the average value of the elements along the diagonal of ΛD, tr(ΛD)/q, is
minimized.
That is, we minimize the average variance of the βf.
And ﬁnally, in E-optimality, we minimize the
maximal value of the elements along the diagonal of ΛD, max Diag(ΛD), i.e., we minimize the most extreme, or
largest, of the variances of the βf. We refer the reader elsewhere for greater detail on these criteria.[1, 6]
Then, for example, our admissible design using the D-optimality criteria will be the D∗, conforming to the trials
power requirements, that minimizes
w
f(D∗) −minD∈D f(D)
maxD∈D f(D) −minD∈D f(D) + (1 −w)
det(ΛD∗) −minD∈D det(ΛD)
maxD∈D det(ΛD) −minD∈D det(ΛD).
(2.1)
Here, f(D∗) and det(ΛD∗) are rescaled precisely because they exist on diﬀerent scales. Additionally, 0 ≤w ≤1 is
the weight given to minimizing the trials cost relative to the eﬃciency of ΛD. Note that the case w = 1 should often
be ignored since many designs will likely share equal values of f(D). Admissible designs using the A- or E-optimality
criteria are formed by replacing det(ΛD) in the above by tr(ΛD)/q or max Diag(ΛD) respectively.
Note that if all of the designs in D cannot attain the desired power, no admissible design will exist. To counteract
this, we can increase the value of β. In an extreme scenario where no design will likely meet any reasonable power
7


## Page 8


requirement, we can set β = 1 and w = 0 and look to determine the design D that simply minimises some function of
ΛD.
Finally, the rescaling in Equation 2.1 is only possible in the case of an exhaustive search where minimal and maximal
values can be identiﬁed. Therefore, in the case of a stochastic search, we consider only meeting the conventional D-,
A- and E-optimality criteria, without rescaling.
2.5.
Example trial design scenarios and associated linear mixed model
In what follows, we frame our examples within the context of studies in which there is a nested natural order upon the
D interventions. That is, as in Chinbuah et al. (2012)[4] and Pol et al. (2017),[25] for d = 1, . . . , D −1, intervention
d consists of intervention d −1 and some additional factor (e.g., intervention d may include additional components of
some wider multi-faceted intervention over intervention d−1). We therefore now in all instances enforce the restrictions
that each cluster receives only a single intervention in each time period, and that if a cluster receives intervention d
in time period j, it cannot receive interventions 0, . . . , d −1 in time periods j + 1, . . . , T. Relating this restriction to
our matrix X, it implies Xij ≥Xij−1 for j = 2, . . . , T and i = 1 . . . , C.
Our methodology for the determination of admissible MA-SW designs is now fully speciﬁed. Code to implement
our methods and replicate our results is available from https://github.com/mjg211/article code. Next, several example
trial design scenarios are considered to demonstrate the eﬃciency gains our designs could bring. In each we assume
that the goal is to compare the eﬃcacy of intervention 1 to intervention 0, intervention 2 to intervention 1, and so on,
giving q = D −1. Moreover, in all examples the following linear mixed model, an extension of that used in Girling
and Hemming (2016)[9] and Hooper et al. (2016)[13] to a multi-arm setting, is employed for data analysis
yijk = µ + πj + β1I{Xij ≥1} + · · · + βD−1I{Xij ≥D −1} + ci + θij + sik + ϵijk.
Here
• I(x) is the indicator function on event x;
• yijk is the kth response (k = 1, . . . , m), in the ith cluster (i = 1, . . . , C), in the jth time period (j = 1, . . . , T);
• µ is an intercept term;
• πj is the ﬁxed eﬀect for the jth time period (with π1 = 0 for identiﬁability);
• ci is the random eﬀect for cluster i, with ci ∼N(0, σ2
c);
• θij is a random interaction eﬀect for cluster i and period j, with θij ∼N(0, σ2
θ);
• sik is a random eﬀect for repeated measures in individual k from cluster i, with sik ∼N(0, σ2
s);
• ϵijk is the residual error, with ϵijk ∼N(0, σ2
ϵ );
8


## Page 9


Thus, we specify our model to be applicable to a cohort MA-SW trial. We can then recover a model appropriate for
a cross-sectional design by setting σ2
s = 0. Note that by the above, the variance of response yijk is σ2 = σ2
c +σ2
θ+σ2
s+σ2
ϵ .
In Section 3, we will make reference to the following three correlation parameters
• ρ0 = (σ2
c + σ2
θ)/σ2: the within-period correlation (the correlation between the responses from two distinct
individuals, in the same cluster, in the same time period);
• ρ1 = σ2
c/σ2: the inter-period correlation (the correlation between the responses from two distinct individuals, in
the same cluster, in distinct time periods);
• ρ2 = (σ2
c + σ2
s)/σ2: the individual auto-correlation (the correlation between the responses from the same indi-
vidual in distinct time periods).
Finally, note that we also restrict the sets XC,T in all instances to those X which imply the above model is
identiﬁable, which can be veriﬁed for any X using the implied design matrix A. However, for brevity, we do not
explicitly state this requirement in our forthcoming speciﬁcations of the sets XC,T .
3.
Results
3.1.
D = 2: Girling and Hemming (2016) and Thompson et al. (2017)
It was previously demonstrated that the eﬃciency of a conventional SW-CRT (i.e., the case D = 2), analysed with
the above linear mixed model, could be assessed using the cluster mean correlation, given by[9]
E(ρ) =
mTρ
1 + (mT −1)ρ,
where ρ is the intra-cluster correlation for the means of the observations at each time-point, in each cluster. The
optimal X matrices to minimise the variance of ˆβ1, when T = 6 and C = 10, were also provided in this paper. We
now demonstrate how our exhaustive search procedure can identify such optimal designs.
First, we set I = {6} and C = {C6} = {10}. We place no further restrictions on X10,6 than those outlined in
Section 2.5, and thus
X6,10 = {X : dim(X) = 6 × 10, Xij ≥Xij−1 for j = 2, . . . , 6 and i = 1 . . . , 10}.
To minimize var(ˆβ1), we take w = 0 and β = 1. Since D = 2, the D-, A-, and E-optimality criteria are equivalent,
and we do not need to specify a multiple comparison correction. Whilst with β = 1, our choices for α, δ, and desire
for individual or combined power are irrelevant. Finally, for simplicity, we reduce our model to that from Hussey
and Hughes (2007)[14] by supposing that σ2
θ = σ2
s = 0. Then, ρ = ρ0 = ρ1 = ρ2 is the conventional intra-cluster
correlation associated with cross-sectional SW-CRTs. Accordingly, to ﬁnd optimal designs for diﬀerent ranges of E(ρ),
as in Girling and Hemming (2016),[9] we take as an example σ2 = 1, M6,10 = {10}, and set ρ as those values which
imply E(ρ) ∈{0.1, 0.15, 0.3, 0.45, 0.75, 0.9}.
9


## Page 10


Factor
Results
E(ρ)
0.1
0.15
0.3
X




















0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1








































0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
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
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1








































0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
1
1
0
0
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1




















E(ρ)
0.45
0.75
0.9
X




















0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
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
1
0
0
1
1
1
1
0
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1








































0
0
0
0
0
0
0
0
0
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
1
0
0
0
1
1
1
0
0
0
1
1
1
0
0
1
1
1
1
0
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1








































0
0
0
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
0
1
0
0
0
0
1
1
0
0
0
1
1
1
0
0
0
1
1
1
0
0
1
1
1
1
0
1
1
1
1
1
0
1
1
1
1
1
1
1
1
1
1
1




















Table 1: Optimal allocation matrices for cross-sectional designs with D = 2. The optimal allocation matrices in the
case I = {6}, C = {C6} = {10}, M = M6,6 = {10}, and σ2 = 1, with w = 0 and β = 1 are shown for a range of
possible values of E(ρ). No restrictions are placed on X other than the identiﬁability of Equation 2.1. Each allocation
matrix was identiﬁed via our exhaustive search method, and matches that identiﬁed by previous research.
10


## Page 11


The results of our exhaustive searches are shown in Table 1. In each instance the optimal design is, as would be
expected, identical to that found previously. We have thus conﬁrmed the ability of our search procedure to easily
identify optimal designs for a given set of input parameters and chosen linear mixed model. Of course, in this scenario,
it would likely in practice be easier to utilize the methodology of Girling and Hemming (2016).[9]
More recently, Thompson et al. (2017)[28] demonstrated that when σ2
θ = σ2
s = 0, if an equal number of clusters
must be allocated to each sequence, then the optimal number of sequences to utilise would be
F(ρ) =
1
1 −
p
E(ρ)
.
We now verify their ﬁndings by restricting our set X6,10 as follows
X6,10 = {X : dim(X) = 6 × 10, Xij ≥Xij−1 for j = 2, . . . , 6 and i = 1 . . . , 10,
(Xi1, . . . , Xi6) = (Xi′1, . . . , Xi′6) for a values of i′ = 1, . . . , i −1, i + 1, . . . , 10 and i = 1, . . . , 10},
where a can be any value such that C/a is an integer.
For the design parameters utilised to construct Table 1, we repeated our exhaustive searches but with the modiﬁed
X6,10 given above. For E(ρ) ∈{0.10, 0.15, 0.30} we found that the optimal X was
X =





























0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1





























.
This should not surprise us as for E(ρ) ∈{0.10, 0.15, 0.30} we have F(ρ) ∈{1.46, 1.63, 2.21} to 2 decimal places,
and the X listed above is one of the few matrices belonging to the modiﬁed X6,10 which utilises two sequences.
In contrast, for E(ρ) = 0.45, we ﬁnd F(ρ) = 3.04. However, for C = 10 the only way equal allocation to sequences
can be achieved is to utilize either two or ﬁve sequences. It should therefore not surprise us that the optimal X was
identiﬁed as
11


## Page 12


X =





























0
0
0
0
0
0
0
0
0
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
0
1
0
0
0
1
1
1
0
0
0
1
1
1
0
1
1
1
1
1
0
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1





























,
which uses ﬁve sequences. Finally, for E(ρ) ∈{0.75, 0.9} we have F(ρ) ∈{7.46, 19.49}, and the optimal X was
again one which employs ﬁve sequences.
3.2.
D = 2: Sensitivity of the optimal designs to the variance parameter speciﬁcation
It is important to note that our admissible design determination procedure, like the articles on optimal SW-CRTs that
have come before, is dependent upon the speciﬁcation of all relevant variance parameters. It is for this reason that
Girling and Hemming (2016)[9] assessed the sensitivity of the performance of their optimised designs to the value of
E(ρ), via a simulation study in which E(ρ) was speciﬁed using a prior.
Here, we consider an alternative approach to visualising the performance of optimal designs across possible values
of the variance parameters. First, in Figure 1, for w = 0, β = 1, σ2
θ = σ2
s = 0, I = {6}, C = {C6} = {10}, and
M = M10,6 = {10}, we present the locations on an equally spaced grid within (σ2
c, σ2
ϵ ) ∈[0.001, 0.25] × [0.25, 4] at
which we identiﬁed various designs to be optimal using an exhaustive search (placing no restrictions on X6,10). In
total 11 designs were found to be optimal for at least one (σ2
c, σ2
ϵ ) combination. We list these in full in Appendix A.
It would be reasonable to be troubled by this result, as it suggests a design that we believe to be optimal may not in
reality be optimal if the variance parameters are even minorly misspeciﬁed.
We can, however, inspect how large our concern should be by examining the performance of any of these optimal
designs across the possible values of the variance parameters, relative to the performance of the true optimal design
at each point. That is, we inspect the ratio of the variance of the intervention eﬀect estimate of a particular design to
that of the optimal design at each (σ2
c, σ2
ϵ ) combination. We present such an evaluation in Figure 2 for the following
design matrices
12


## Page 13


G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G
G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G
G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G
G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G
G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G
G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G
G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G
G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G
G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G
G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G
G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G
G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G
G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G
G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G
G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G
G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G
G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G
G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G
G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G
G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G
G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G
G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G
G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G
G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G
G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G
G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G
G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G
G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G
G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G
G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G
1
2
3
4
0.00
0.05
0.10
0.15
0.20
0.25
σc
2
σε
2
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
Design 1
Design 2
Design 3
Design 4
Design 5
Design 6
Design 7
Design 8
Design 9
Design 10
Design 11
Figure 1: Optimal allocation matrices for cross-sectional designs with D = 2. The optimal allocation matrices in the
case I = {6}, C = {C6} = {10}, M = M10,6 = {10}, and σ2 = 1, with w = 0 and β = 1 are shown for a range of
possible combinations of (σ2
c, σ2
ϵ ) ∈[0.001, 0.25]×[0.25, 4]. No restrictions are placed on X other than the identiﬁability
of Equation 2.1. Each allocation matrix was identiﬁed via our exhaustive search method.
13


## Page 14


X1 =





























0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1





























,
X2 =





























0
0
0
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
0
1
0
0
0
0
1
1
0
0
0
1
1
1
0
0
0
1
1
1
0
0
1
1
1
1
0
1
1
1
1
1
0
1
1
1
1
1
1
1
1
1
1
1





























,
which are Designs 8 and 3 from Figure 1 respectively. As must obviously be the case, the value of the ratio of
the variances is in all instances at least one. We observe that with the matrix X1, the variance of the intervention
eﬀect estimate is substantially larger than that for the optimal design when the values of σ2
c and σ2
ϵ are mis-speciﬁed,
particularly when the value of ρ is in fact large. In contrast, using the matrix X2 retains eﬃcient performance in many
instances. However, if ρ is small then the variance of the intervention eﬀect provided by this design is still more than
40% larger than that of the optimal design.
3.3.
D = 2: Li et al. (2018)
Li et al. (2018)[20] recently extended the results of Lawrie et al. (2015)[19] to cohort SW-CRTs. Speciﬁcally, they
considered a case in which all clusters have to begin in the control condition (intervention 0), and conclude in the
experimental (intervention 1). They then demonstrated that the optimal X could be speciﬁed by ensuring that the
proportion, pt, of clusters allocated to a sequence with t ones preceded by T −t zeros satisﬁes
p1 = pT −1 = ψ + 3ξ
2γ
,
pt = ξ
γ ,
for t = 2, . . . , T −2,
where
ψ = 1 −(m −1)ρ0 −(m −1)ρ1 −ρ2,
ξ = (m −1)ρ1 + ρ2,
γ = ψ + Tξ.
Here, we explore their ﬁndings for several example design scenarios, again via an exhaustive search. As above, we
consider the case in which I = {6}, C = {C6} = {10}, and M = M10,6 = {10}, with σ2 = 1, w = 0, and β = 1. To
14


## Page 15


follow their restrictions on the allowed X we enforce that
X6,10 = {X : dim(X) = 6 × 10, Xij ≥Xij−1 for j = 2, . . . , 6 and i = 1 . . . , 10, Xi1 = 0 and XiT = 1 for i = 1, . . . , C}.
Then, we denote by pth = (p1, . . . , pT −1)⊤the vector of the pt for the theoretical optimal designs derived by Li et
al. (2018),[20] and denote by pemp the vector of the empirical values of the pt for our identiﬁed optimal designs.
Our ﬁndings are presented in Table 2 for (ρ0, ρ1, ρ2) ∈{0.05, 0.1} × {0.001, 0.002} × {0.25, 0.5}. They illustrate one
potential issue with applying the results of Li et al. (2018)[20] in practice; that the theoretically optimal values of the
pt will likely not be achievable because C is an integer. However, it is clear that the empirical values of the proportions
of clusters changing to the experimental intervention in each time period are close to their theoretical values, even in
this case where C is small.
Factor
Results
ρ0
0.050
0.050
0.050
0.050
ρ1
0.001
0.001
0.002
0.002
ρ2
0.250
0.500
0.250
0.500
X




















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
0
1
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
0
1
0
0
0
0
1
1
0
0
0
1
1
1
0
0
1
1
1
1
0
1
1
1
1
1
0
1
1
1
1
1
0
1
1
1
1
1








































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
0
1
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
1
0
0
0
1
1
1
0
0
0
1
1
1
0
0
1
1
1
1
0
1
1
1
1
1
0
1
1
1
1
1
0
1
1
1
1
1








































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
0
1
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
0
1
0
0
0
0
1
1
0
0
0
1
1
1
0
0
1
1
1
1
0
1
1
1
1
1
0
1
1
1
1
1
0
1
1
1
1
1








































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
0
1
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
1
0
0
0
1
1
1
0
0
0
1
1
1
0
0
1
1
1
1
0
1
1
1
1
1
0
1
1
1
1
1
0
1
1
1
1
1




















p⊤
th
(0.30,0.08,0.08,0.08,0.30)
(0.24,0.10,0.10,0.10,0.24)
(0.29,0.08,0.08,0.08,0.29)
(0.24,0.10,0.10,0.10,0.24)
p⊤
emp
(0.4,0.1,0.1,0.1,0.3)
(0.3,0.1,0.2,0.1,0.3)
(0.4,0.1,0.1,0.1,0.3)
(0.3,0.1,0.2,0.1,0.3)
ρ0
0.100
0.100
0.100
0.100
ρ1
0.001
0.001
0.002
0.002
ρ2
0.250
0.500
0.250
0.500
X




















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
0
1
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
0
1
0
0
0
0
1
1
0
0
1
1
1
1
0
1
1
1
1
1
0
1
1
1
1
1
0
1
1
1
1
1
0
1
1
1
1
1








































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
0
1
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
1
0
0
0
1
1
1
0
0
0
1
1
1
0
0
1
1
1
1
0
1
1
1
1
1
0
1
1
1
1
1
0
1
1
1
1
1








































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
0
1
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
0
1
0
0
0
0
1
1
0
0
1
1
1
1
0
1
1
1
1
1
0
1
1
1
1
1
0
1
1
1
1
1
0
1
1
1
1
1








































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
0
1
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
1
0
0
0
1
1
1
0
0
0
1
1
1
0
0
1
1
1
1
0
1
1
1
1
1
0
1
1
1
1
1
0
1
1
1
1
1




















p⊤
th
(0.32,0.07,0.07,0.07,0.32)
(0.26,0.10,0.10,0.10,0.26)
(0.31,0.07,0.07,0.07,0.31)
(0.26,0.10,0.10,0.10,0.26)
p⊤
emp
(0.4,0.1,0,0.1,0.4)
(0.3,0.1,0.2,0.1,0.3)
(0.4,0.1,0,0.1,0.4)
(0.3,0.1,0.2,0.1,0.3)
Table 2: Optimal allocation matrices for cohort designs with D = 2. The optimal allocation matrices in the case
I = {6}, C = {C6} = {10}, M = M10,6 = {10}, and σ2 = 1, with w = 0 and β = 1 are shown for a range of possible
combinations of ρ0, ρ1, and ρ2. Restrictions are placed on X such that Equation 2.1 is identiﬁable, and that each
cluster must start in the control intervention (arm 0) and conclude in the experimental intervention (arm 1). Each
allocation matrix was identiﬁed via our exhaustive search method.
15


## Page 16


3.4.
D = 3: SO-HIP Study
The SO-HIP study is a cross-sectional MA-SW, with D = 3, to evaluate the eﬀectiveness of sensor monitoring in an
occupational therapy rehabilitation program for older people after hip fracture. Speciﬁcally, arm 0 corresponds to
providing participants with care as usual. Arm 1 then involves the additional use of occupational therapy without
sensor monitoring, in contrast to arm 2 that incorporates occupational therapy with cognitive behavioural therapy
coaching using sensor monitoring as a coaching tool. Thus, as discussed earlier, intervention d −1 is nested within
intervention d, for d = 1, 2.
SO-HIP plans to enrol six clusters (C = 6), and have six time periods (T = 6), with eight observations made per
cluster per period (m = 8), using the following matrix for treatment allocation
X =
















0
0
0
1
1
2
0
0
0
1
1
2
0
0
1
1
2
2
0
0
1
1
2
2
0
1
1
2
2
2
0
1
1
2
2
2
















.
The trial has δ = (1.5σ, 0.75σ)⊤, and assumes that σ2
s = σ2
θ = 0 and ρ(= ρ0 = ρ1 = ρ2) = 0.05. With this, when
σ2 = 1, using our methods described above we can identify that the proposed design will have an individual power of
0.88 (β = 0.12) when the familywise error-rate is controlled to α = 0.05 using the Bonferroni correction. For further
information on this trial, see the published protocol.[25]
We now consider how much eﬃciency could be gained by utilizing an alternative design. We presume that in the
trial any number of time periods two through six could have been employed (I = {2, . . . , 6}), and any number of clusters
two through six could have actually been utilized (C = {C2, . . . , C6}, with CT = {2, . . . , 6} for each T ∈T). Finally,
we assume that the trials plan to recruit 48 patients in total from each cluster would allow MC,T = {2, . . . , ⌊48/T⌋}.
Here, we enforce that
XC,T = {X : dim(X) = C × T, Xij ≥Xij−1 for j = 2, . . . , T and i = 1 . . . , C}.
Taking our cost function to be the total number of observations, f(D) = mCT, we present several admissible designs
in Table 3. Explicitly, in this case, we ﬁnd that the optimal designs when using the D-, A-, and E-optimality criteria
coincide for w = 0 and w = 0.5. Note that we also considered the optimal designs for w = 1 −10−4, but they were
found to be identical to those for w = 0.5.
We can see that the individual power of the trial could be increased by as much as 12.1%, as a result of reducing
the maximum value of the variances of the treatment eﬀect estimators by 44.3% (w = 0). Alternatively, the individual
power could be maintained and the required number of observations reduced by up to 58.3% (w = 0.5).
Now, in Table 4, we present corresponding evaluations, but with further restrictions placed on the sets XC,T , as
16


## Page 17


Design
Factor
Proposed
D/A/E-Optimal: w = 0
D/A/E-Optimal: w = 0.5
C
6
6
6
T
6
6
5
m
8
8
4
X










0
0
0
1
1
2
0
0
0
1
1
2
0
0
1
1
2
2
0
0
1
1
2
2
0
1
1
2
2
2
0
1
1
2
2
2




















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
1
0
0
0
1
1
2
0
1
1
2
2
2
1
1
2
2
2
2
1
2
2
2
2
2




















0
0
1
1
1
0
0
1
1
1
1
1
1
2
2
1
1
2
2
2
2
2
2
2
2
2
2
2
2
2










P(Reject H01|δ1)
1.000
1.0000 (±0%)
0.9937 (−0.6%)
P(Reject H02|δ2)
0.8815
0.9878 (+12.1%)
0.8818 (±0%)
f(D)
288
288 (±0%)
120 (−58.3%)
det(ΛD)
3.090 × 10−3
9.990 × 10−4 (−67.7%)
6.377 × 10−3 (+106.4%)
(D −1)−1tr(ΛD)
5.696 × 10−2
3.175 × 10−2 (−44.3%)
8.508 × 10−2 (+49.4%)
maxDiag(ΛD)
5.696 × 10−2
3.175 × 10−2 (−44.3%)
1.132 × 10−1 (+98.8%)
Table 3: Optimal allocation matrices for cross-sectional designs with D = 3. Several optimal allocation matrices in
the case I = {2, . . . , 6}, C = {C2, . . . , C6}, CT = {2, . . . , 6}, MC,T = {2, . . . , ⌊48/T⌋}, σ2 = 1, ρ = 0.05, α = 0.05 with
the Bonferroni correction, and β = 0.12 for the individual power when δ = (1.5σ, 0.75σ)⊤are shown. Speciﬁcally, the
optimal design for the optimality criteria is given for w ∈{0, 0.5}. No restrictions are placed on X other than the
identiﬁability of Equation 2.1. Each allocation matrix was identiﬁed via our exhaustive search method. The utilized
design is also shown for comparison.
follows
XC,T = {X : dim(X) = C × T, Xij ≥Xij−1 for j = 2, . . . , T and i = 1 . . . , C, Xij = d for some j = 1, . . . , T
for all d = 0, . . . , D −1 and i = 1, . . . , C}.
That is, we enforce that each cluster receives interventions 0, 1, and 2. This allows us to perform an assessment of
the advantages optimisation can bring in the likely common case in which it is desired that each cluster receive all of
the interventions. Note that in this case certain combinations of C and T considered above are no longer are possible
(e.g., for T = 2 a cluster cannot receive all three interventions).
We now ﬁnd that whilst the optimal designs are equivalent when using the A- or E-optimality criteria, the D-
optimal designs are distinct. Overall, while the potential eﬃciency gains that are possible when restricting to these
more classical designs are more modest than those in Table 3, they are still substantial. In particular, the admissible
designs with w = 0.5 provide a 37.5% reduction in the required number of observations compared to the utilised
design. Moreover, we can still increase the individual power by up to 8.6%.
17


## Page 18


Design
Factor
Proposed
D-Optimal: w = 0
D-Optimal: w = 0.5
A/E-Optimal: w = 0
A/E-Optimal: w = 0.5
C
6
6
6
6
6
T
6
6
6
6
6
m
8
8
5
8
5
X










0
0
0
1
1
2
0
0
0
1
1
2
0
0
1
1
2
2
0
0
1
1
2
2
0
1
1
2
2
2
0
1
1
2
2
2




















0
0
0
0
1
2
0
0
0
0
1
2
0
0
0
1
2
2
0
0
1
2
2
2
0
1
2
2
2
2
0
1
2
2
2
2




















0
0
0
0
1
2
0
0
0
0
1
2
0
0
1
1
2
2
0
1
1
2
2
2
0
1
2
2
2
2
0
1
2
2
2
2




















0
0
0
0
1
2
0
0
0
0
1
2
0
0
1
1
2
2
0
0
1
2
2
2
0
1
2
2
2
2
0
1
2
2
2
2




















0
0
0
0
1
2
0
0
0
0
1
2
0
0
1
1
2
2
0
0
1
2
2
2
0
1
2
2
2
2
0
1
2
2
2
2










P(Reject H01|δ1)
1.0000
1.0000 (±0%)
1.0000 (±0%)
1.0000 (±0%)
1.0000 (±0%)
P(Reject H02|δ2)
0.8815
0.9528 (+8.1%)
0.8507 (−3.5%)
0.9570 (+8.6%)
0.8440 (−4.3%)
f(D)
288
288 (±0%)
180 (−37.5%)
288 (±0%)
180 (−37.5%)
det(ΛD)
3.090 × 10−3
1.670 × 10−3 (−46.0%)
3.881 × 10−3 (+25.6%)
1.712 × 10−3 (−44.6%)
3.973 × 10−3 (+25.6%)
(D −1)−1tr(ΛD)
5.696 × 10−2
4.264 × 10−2 (−25.1%)
6.392 × 10−2 (+12.2%)
4.160 × 10−2 (−27.0%)
6.373 × 10−2 (+11.9%)
maxDiag(ΛD)
5.696 × 10−2
4.264 × 10−2 (−25.1%)
6.531 × 10−2 (+14.7%)
4.160 × 10−2 (−27.0%)
6.373 × 10−2 (+11.9%)
Table 4: Optimal allocation matrices for cross-sectional designs with D = 3.
Several optimal allocation matrices in the case I = {2, . . . , 6}, C = {C2, . . . , C6},
CT = {2, . . . , 6}, MC,T = {2, . . . , ⌊48/T⌋}, σ2 = 1, ρ = 0.05, α = 0.05 with the Bonferroni correction, and β = 0.12 for the individual power when δ = (1.5σ, 0.75σ)⊤
are shown. Speciﬁcally, the optimal design for the optimality criteria is given for w ∈{0, 0.5}. Restrictions are placed on X such that Equation 2.1 is identiﬁable, and
that each cluster must receive each of the interventions. Each allocation matrix was identiﬁed via our exhaustive search method. The utilized design is also shown for
comparison.
18


## Page 19


3.5.
D = 3: Optimal cross-sectional designs according to the value of the cluster mean
correlation
We have now noted the fact that previous papers have described how the optimal cross-sectional SW-CRT design when
D = 2 changes according to the value of the cluster mean correlation E(ρ) (where ρ = ρ0 = ρ1 = ρ2 for σ2
s = σ2
θ = 0).
In fact, in Table 1 we provide an example of this for a case with C = 10 and T = 6. In it, we observe that the optimal
design as E(ρ) increases changes from one resembling a parallel group CRT, to a more classical SW-CRT design. Here,
we provide a brief assessment of whether such a pattern exists for designs with D = 3, in a setting motivated by the
SO-HIP trial. Thus, we set I = {6}, C = {C6} = {6}, M = M6,6 = {8}, σ2 = 1, w = 0, β = 1 and
X6,6 = {X : dim(X) = 6 × 6, Xij ≥Xij−1 for j = 2, . . . , 6 and i = 1 . . . , 6}.
We then consider which design is optimal according to the D-, A-, and E-optimality criteria for E(ρ) ∈
{0, 0.01, . . . , 1}. We present our ﬁndings for E-optimality in Table 5, and for D- and A-optimality in Appendix B.
Speciﬁcally we can see that whilst the pattern to the way in which the optimal X changes is arguably less clear than
in the case with D = 2, there is still a trend that the best possible choice shifts from a longitudinal parallel group
CRT, to a design resembling an extension of a classical SW-CRT.
3.6.
D = 4: Stochastic determination of optimal designs
Finally, we suppose that the SO-HIP study is to actually be conducted with a fourth intervention arm. This hypo-
thetical trial is to again be conducted in six clusters (C = 6), with eight measurements taken per cluster per period
(m = 8), but will now run across eight periods (T = 8). Furthermore, the following natural extension of the design
for D = 3 will be used for X
X =
















0
0
0
1
1
2
2
3
0
0
0
1
1
2
2
3
0
0
1
1
2
2
3
3
0
0
1
1
2
2
3
3
0
1
1
2
2
3
3
3
0
1
1
2
2
3
3
3
















.
We assume that the trial will control the familywise error-rate to α = 0.05 using the Bonferroni correction. Pre-trial,
the variance parameters have been set as σ2 = 1 and ρ = 0.05, and we take δ = (1.5σ, 0.75σ, 0.75σ)⊤.
We then suppose that we desire to determine how much the trials eﬃciency could be improved if an alternative
design was utilized. For this we employ a stochastic search, as I = {8}, C = {C8} = {6}, and M = {M6,8} = {8} with
D = 4 confer a design space too large for an exhaustive comparison.
In Table 6 we present the stochastically identiﬁed optimal designs for the D-, A-, and E-optimality crtieria. We can
see that, in particular, the average variance of our intervention eﬀects could be reduced by up to 49.8% (A-optimality),
19


## Page 20


Factor
E-optimal designs
E(ρ)
{0, . . . , 0.06}
0.07
{0.08, . . . , 0.11}
{0.12, . . . , 0.34}
{0.35, 0.36}
{0.37, . . . , 0.65}
X










0
0
0
0
0
0
0
0
0
0
0
1
1
1
1
1
1
1
1
1
1
1
1
1
1
2
2
2
2
2
2
2
2
2
2
2




















0
0
0
0
0
0
0
0
0
0
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
2
2
2
2
2
2
2
2
2
2




















0
0
0
0
0
0
0
0
0
0
1
1
0
1
1
1
1
1
1
1
1
1
1
2
1
1
2
2
2
2
2
2
2
2
2
2




















0
0
0
0
0
0
0
0
0
0
1
1
0
0
1
1
1
1
1
1
1
1
2
2
1
1
2
2
2
2
2
2
2
2
2
2




















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
1
0
0
1
1
1
1
1
1
1
1
2
2
1
1
2
2
2
2
1
2
2
2
2
2




















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
1
0
0
1
1
1
2
0
1
1
1
2
2
1
1
2
2
2
2
1
2
2
2
2
2










E(ρ)
{0.66, . . . , 0.83}
0.84
0.85
{0.86, . . . , 0.94}
{0.95, . . . , 0.99}
1.00
X










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
1
0
0
0
1
1
2
0
1
1
2
2
2
1
1
2
2
2
2
1
2
2
2
2
2




















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
1
0
0
0
1
1
2
0
1
2
2
2
2
1
1
1
2
2
2
1
2
2
2
2
2




















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
2
0
0
0
1
1
1
0
1
1
2
2
2
1
1
2
2
2
2
1
2
2
2
2
2




















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
1
0
0
0
1
2
2
0
0
1
2
2
2
1
1
2
2
2
2
1
2
2
2
2
2




















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
2
0
0
0
1
2
2
0
0
1
2
2
2
0
1
2
2
2
2
1
2
2
2
2
2




















0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
1
2
2
2
2
2
1
2
2
2
2
2
1
2
2
2
2
2










Table 5: E-optimal allocation matrices for cross-sectional designs with D = 3. The E-optimal allocation matrices in the case I = {6}, C = {C6} = {6}, M = M6,6 = {8},
and σ2 = 1, with w = 0 and β = 1 are shown for E(ρ) ∈{0, 0.01, . . . , 1}. No restrictions are placed on X other than the identiﬁability of Equation 2.1. Each allocation
matrix was identiﬁed via our exhaustive search method.
20


## Page 21


or the maximal variance of the intervention eﬀects reduced by up to 48.2% (E-optimality). It is thus clear that a
stochastic search can allow the identiﬁcation of eﬃcient designs when an exhaustive search would not be feasible.
4.
Discussion
We have presented a method to determine admissible MA-SW designs. Our work builds on previous results for SW-
CRTs to allow trialists to determine eﬃcient designs when any linear mixed model is to be used for data analysis, and
when there is any number of treatment arms.
For our primary motivating example, the SO-HIP study, we demonstrated for the considered parameters that
the individual power could have been maintained with the number of required observations reduced by 58%. Whilst
for some possible design parameter combinations this reduction would likely not be so pronounced, it is clear that
admissible designs in this context could bring notable eﬃciency gains.
It is important to note, however, that there are some scenarios in which our approach would likely not be applicable.
This includes cases where the design space D is extremely large, even after C and T have been speciﬁed precisely. A
trialist must then either look to extend the approach of Girling and Hemming (2016),[9] or look to reduce the size of
D to make an exhaustive or stochastic search possible.
More signiﬁcantly, our methodology, like all others on optimal SW-CRT design, assumes that the variance param-
eters of the analysis model of interest are known. Accordingly, our approach may not be a wise one when substantial
uncertainty exists about their values. When conﬁdence does exist around their speciﬁcation, it remains important to
assess the sensitivity of the chosen design to the underlying assumptions, using for example an approach like that in
Section 3.2.
Our methodology is also limited to linear mixed models, and assumes that the employed analysis model is appro-
priate for the trial’s data. For large sample sizes our methods may still be appropriate for alternate endpoints such as
binary or count data, but they would not always be acceptable in these domains. In Appendix C we provide a brief
demonstration of how our methods can be applied to binary outcome variables. In addition, for some linear mixed
models, allowing the number of time periods T to vary may cause issues if a complex correlation structure is assumed
for the accrued responses. As for any trial, the analysis model should be chosen carefully, as the chosen design may
not be optimal for an alternative potential model. However, we highlight again that our approach is applicable to
any linear mixed model. Thus, more complex models than that considered here are supported, including for example
those which allow for the decay of treatment eﬀects over time.
We made few principal assumptions about the nature of the trial design. Our method is applicable to both cross-
sectional and cohort studies, and to cases where either a single or multiple interventions are allocated to each cluster
in each time period. Nonetheless, from those MA-SW trials conducted so far, it appears that a common likelihood will
be that there is some natural ordering to the interventions. Lyons et al. (2017),[21] however, do provide a detailed
description of alternative possibilities to this.
In Section 3 we employed several diﬀerent types of restrictions on the sets XC,T . In particular, we demonstrated
our approach can be easily applied to attain classical designs where the clusters receive all interventions, and to cases
21


## Page 22


Design
Factor
Proposed
D-optimal
A-optimal
E-optimal
X










0
0
0
1
1
2
2
3
0
0
0
1
1
2
2
3
0
0
1
1
2
2
3
3
0
0
1
1
2
2
3
3
0
1
1
2
2
3
3
3
0
1
1
2
2
3
3
3




















0
0
0
0
0
0
1
1
0
0
0
0
1
1
2
3
0
0
1
2
2
3
3
3
0
1
1
1
1
2
2
2
1
2
2
2
3
3
3
3
2
2
3
3
3
3
3
3




















0
0
0
0
0
0
1
1
0
0
0
0
1
1
3
3
0
0
1
1
1
2
2
2
1
1
1
1
2
2
2
2
1
1
2
2
2
3
3
3
2
2
2
3
3
3
3
3




















0
0
0
0
0
0
1
3
0
0
0
0
1
1
2
2
0
0
0
1
1
3
3
3
1
1
1
1
2
2
2
2
1
1
2
2
3
3
3
3
2
2
3
3
3
3
3
3










P(Reject H01|δ1)
1.000
1.000 (±0%)
1.000 (±0%)
1.000 (±0%)
P(Reject H02|δ2)
0.852
0.992 (+11.6%)
0.996 (+11.7%)
0.989 (+11.6%)
P(Reject H03|δ3)
0.852
0.990 (+11.6%)
0.984 (+11.6%)
0.989 (+11.6%)
det(ΛD)
1.559 × 10−4
1.985 × 10−5 (−87.3%)
2.108 × 10−5 (−86.5%)
2.090 × 10−5 (−86.6%)
(D −1)−1tr(ΛD)
5.590 × 10−2
2.873 × 10−2 (−48.6%)
2.806 × 10−2 (−49.8%)
2.886 × 10−2 (−48.4%)
maxDiag(ΛD)
5.590 × 10−2
3.024 × 10−2 (−45.9%)
3.085 × 10−2 (−44.8%)
2.893 × 10−2 (−48.2%)
Table 6: Optimal allocation matrices for cross-sectional designs with D = 4. Several optimal allocation matrices in the case I = {8}, C = {C6} = {8}, M6,8 = {8},
σ2 = 1, ρ = 0.05, α = 0.05 with the Bonferroni correction, w = 0, and β = 0.12 for the individual power when δ = (1.5σ, 0.75σ, 0.75σ)⊤, are shown. No restrictions are
placed on X other than the identiﬁability of Equation 2.1. Each allocation matrix was identiﬁed via our stochastic search method. The proposed design is also shown
for comparison.
22


## Page 23


where there must be equal allocation to sequences. In general, not placing restrictions on XC,T , beyond those which
are absolutely required, will result in the determination of the most eﬃcient design. However, particularly through
Table 4, we were able to demonstrate that optimisation is still useful when such restrictions are considered necessary.
Finally, it is important to discuss the fact that in practice a choice must be made around which optimality
criteria to use, and what value to use for w. Unfortunately, there is no simple solution to this. Previous authors have
highlighted that D-optimality is an easy quantity to explain to practitioners from many ﬁelds.[6] However, it is diﬃcult
to claim that A- and E-optimality would be more complex to describe. Arguably, A-optimality is most useful when
the parameters of interest are of equal importance. In contrast, D- and E-optimality may favour more specialised
considerations. However, note that in certain situations, as in Table 1, we may ﬁnd that the optimal design for each
of these criteria is equivalent. Thus, such a choice may not always be required. Finally, when choosing w, if gathering
observations is cheap we may anticipate that setting w approximately equal to 0 is logical. This would also be the case
when we have a ﬁxed number of observations in mind, and simply want to optimize X, as in many of the discussions
in Section 3. Most typically though, it is likely we would need to ﬁnd a balance between cost and eﬃciency. In this
case, larger values of w would seem appealing. But, we would rarely recommend setting w = 1, as even placing a tiny
weight on the D-, A-, or E- optimality criteria can result in the choice of a much more eﬃcient X, for only slightly
increased cost.
In conclusion, we have presented methodology to identify highly eﬃcient MA-SWs. Of course, the most important
factor for any real trial is that a design and analysis procedure are chosen that are appropriate for the complexities
of the data the trial will likely accrue. However, when logistical, practical, and statistical, constraints permit the
possibility to use one of a range of designs, researchers should consider the use of our approach to optimize their trials
eﬃciency. As we have demonstrated, restrictions can readily be placed on the sets XC,T to retain the needs of the
trial, but still allow more eﬃcient designs to be identiﬁed.
Acknowledgements
This work was supported by the Medical Research Council [grant number MC UP 1302/2 to APM and MJG]; and
the National Institute for Health Research Cambridge Biomedical Research Centre [MC UP 1302/6 to JMSW].
A.
Optimal cross-sectional designs from Section 3.2
In Table 7 we list the optimal designs from Figure 1, discussed in Section 3.2.
B.
D- and A-optimal designs from Section 3.5
Here, in Tables 8 and 9, we provide the D- and A-optimal designs discussed in Section 3.5.
23


## Page 24


Design 1
Design 2
Design 3
Design 4




















0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
1
1
0
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1








































0
0
0
0
0
0
0
0
0
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
1
0
0
0
1
1
1
0
0
0
1
1
1
0
0
1
1
1
1
0
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1








































0
0
0
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
0
1
0
0
0
0
1
1
0
0
0
1
1
1
0
0
0
1
1
1
0
0
1
1
1
1
0
1
1
1
1
1
0
1
1
1
1
1
1
1
1
1
1
1








































0
0
0
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
1
0
0
0
0
1
1
0
0
0
1
1
1
0
0
0
1
1
1
0
0
1
1
1
1
0
1
1
1
1
1
0
1
1
1
1
1
1
1
1
1
1
1




















Design 5
Design 6
Design 7
Design 8




















0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
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
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1








































0
0
0
0
0
0
0
0
0
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
1
0
0
0
1
1
1
0
0
1
1
1
1
0
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1








































0
0
0
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
0
1
0
0
0
0
1
1
0
0
0
1
1
1
0
0
1
1
1
1
0
0
1
1
1
1
0
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1








































0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1




















Design 9
Design 10
Design 11




















0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
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
1
0
0
1
1
1
1
0
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1








































0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
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
1
0
0
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1








































0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
1
1
0
0
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1




















Table 7: The optimal designs from Figure 1 are presented.
24


## Page 25


Factor
D-optimal designs
E(ρ)
{0, . . . , 0.10}
{0.11, . . . , 0.19}
{0.20, . . . , 0.46}
{0.47, 0.48}
0.49
X










0
0
0
0
0
0
0
0
0
0
0
0
1
1
1
1
1
1
1
1
1
1
1
1
2
2
2
2
2
2
2
2
2
2
2
2




















0
0
0
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
1
1
1
1
1
1
1
1
1
1
2
1
2
2
2
2
2
2
2
2
2
2
2




















0
0
0
0
0
0
0
0
0
0
1
1
0
0
1
1
1
1
1
1
1
1
2
2
1
1
2
2
2
2
2
2
2
2
2
2




















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
1
0
0
1
1
1
2
1
1
1
2
2
2
1
1
2
2
2
2
2
2
2
2
2
2




















0
0
0
0
0
0
0
0
0
0
1
1
0
0
0
1
1
1
0
1
1
1
2
2
1
1
2
2
2
2
1
2
2
2
2
2










E(ρ)
{0.50, . . . , 0.53}
{0.54, 0.55, 0.56}
0.57
{0.58, . . . , 0.79}
0.80
X










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
1
0
0
1
1
1
2
1
1
1
2
2
2
1
1
2
2
2
2
2
2
2
2
2
2




















0
0
0
0
0
0
0
0
0
0
1
1
0
0
0
1
1
1
0
1
1
1
2
2
1
1
2
2
2
2
1
2
2
2
2
2




















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
1
0
0
1
1
1
2
1
1
1
2
2
2
1
1
2
2
2
2
2
2
2
2
2
2




















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
1
0
0
0
1
1
2
0
1
1
2
2
2
1
1
2
2
2
2
1
2
2
2
2
2




















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
1
0
0
0
1
1
2
0
0
1
2
2
2
1
1
2
2
2
2
1
2
2
2
2
2










E(ρ)
0.81
0.82
0.83
0.84
0.85
X










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
1
0
0
0
1
2
2
0
1
1
2
2
2
1
1
2
2
2
2
1
2
2
2
2
2




















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
1
0
0
0
1
1
2
0
0
1
2
2
2
1
1
2
2
2
2
1
2
2
2
2
2




















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
1
0
0
0
1
2
2
0
1
1
2
2
2
1
1
2
2
2
2
1
2
2
2
2
2




















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
1
0
0
0
1
1
2
0
0
1
2
2
2
1
1
2
2
2
2
1
2
2
2
2
2




















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
1
0
0
0
1
2
2
0
0
1
2
2
2
1
1
2
2
2
2
1
2
2
2
2
2










E(ρ)
0.86
{0.87, 0.88, 0.89}
0.90
{0.91, . . . , 0.99}
1.00
X










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
1
0
0
0
1
1
2
0
0
1
2
2
2
0
1
2
2
2
2
1
2
2
2
2
2




















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
2
0
0
0
1
2
2
0
1
1
2
2
2
1
1
2
2
2
2
1
2
2
2
2
2




















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
1
0
0
0
1
2
2
0
0
1
2
2
2
0
1
2
2
2
2
1
2
2
2
2
2




















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
2
0
0
0
1
2
2
0
0
1
2
2
2
0
1
2
2
2
2
1
2
2
2
2
2




















0
0
0
0
0
0
0
0
0
1
2
2
0
0
0
1
2
2
0
0
0
1
2
2
0
0
0
1
2
2
0
0
0
1
2
2










Table 8: D-optimal allocation matrices for cross-sectional designs with D = 3. The D-optimal allocation matrices in the case I = {6}, C = {C6} = {6}, M = M6,6 = {8},
and σ2 = 1, with w = 0 and β = 1 are shown for E(ρ) ∈{0, 0.01, . . . , 1}. No restrictions are placed on X other than the identiﬁability of Equation 2.1. Each allocation
matrix was identiﬁed via our exhaustive search method.
25


## Page 26


Factor
A-optimal designs
E(ρ)
{0, . . . , 0.06}
0.07
{0.08, . . . , 0.11}
{0.12, . . . , 0.30}
{0.31, 0.32, 0.33}
X










0
0
0
0
0
0
0
0
0
0
0
1
1
1
1
1
1
1
1
1
1
1
1
1
1
2
2
2
2
2
2
2
2
2
2
2




















0
0
0
0
0
0
0
0
0
0
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
2
2
2
2
2
2
2
2
2
2




















0
0
0
0
0
0
0
0
0
0
1
1
0
1
1
1
1
1
1
1
1
1
1
2
1
1
2
2
2
2
2
2
2
2
2
2




















0
0
0
0
0
0
0
0
0
0
1
1
0
0
1
1
1
1
1
1
1
1
2
2
1
1
2
2
2
2
2
2
2
2
2
2




















0
0
0
0
0
0
0
0
0
0
1
1
0
0
1
1
1
1
1
1
1
1
2
2
1
1
2
2
2
2
1
2
2
2
2
2










E(ρ)
{0.34, 0.35}
{0.36, . . . , 0.39}
{0.40, . . . , 0.62}
{0.63, . . . , 0.66}
0.67
X










0
0
0
0
0
0
0
0
0
0
1
1
0
0
1
1
1
1
0
1
1
1
2
2
1
1
2
2
2
2
1
2
2
2
2
2




















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
1
0
0
1
1
1
2
1
1
1
1
2
2
1
1
2
2
2
2
2
2
2
2
2
2




















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
1
0
0
1
1
1
2
0
1
1
1
2
2
1
1
2
2
2
2
1
2
2
2
2
2




















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
1
0
0
0
1
1
2
0
1
1
1
2
2
1
1
2
2
2
2
1
2
2
2
2
2




















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
1
0
0
1
1
1
2
0
1
1
2
2
2
1
1
2
2
2
2
1
2
2
2
2
2










E(ρ)
{0.68, 0.69}
{0.70, . . . , 0.81}
0.82
0.83
{0.84, 0.85, 0.86}
X










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
1
0
0
0
1
1
2
0
1
1
1
2
2
1
1
2
2
2
2
1
2
2
2
2
2




















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
1
0
0
0
1
1
2
0
1
1
2
2
2
1
1
2
2
2
2
1
2
2
2
2
2




















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
1
0
0
0
1
1
2
0
0
1
2
2
2
1
1
2
2
2
2
1
2
2
2
2
2




















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
1
0
0
0
1
2
2
0
1
1
2
2
2
1
1
2
2
2
2
1
2
2
2
2
2




















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
1
0
0
0
1
1
2
0
0
1
2
2
2
1
1
2
2
2
2
1
2
2
2
2
2










E(ρ)
{0.87, 0.88, 0.89}
{0.90, 0.91, 0.92}
0.93
0.94
{0.95, 0.96}
X










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
2
0
0
1
1
2
2
0
1
1
2
2
2
1
1
2
2
2
2
1
2
2
2
2
2




















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
1
0
0
0
1
1
2
0
0
1
2
2
2
0
1
2
2
2
2
1
2
2
2
2
2




















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
2
0
0
0
1
2
2
0
1
1
2
2
2
1
1
2
2
2
2
1
2
2
2
2
2




















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
1
0
0
0
1
1
2
0
0
1
2
2
2
0
1
2
2
2
2
1
2
2
2
2
2




















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
1
0
0
0
1
2
2
0
0
1
2
2
2
0
1
2
2
2
2
1
2
2
2
2
2










E(ρ)
0.97
{0.98, 0.99}
1.00
X










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
1
0
0
0
2
2
2
0
0
1
1
1
2
0
1
2
2
2
2
1
1
1
1
2
2




















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
2
0
0
0
1
2
2
0
0
1
2
2
2
0
1
2
2
2
2
1
2
2
2
2
2




















0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
1
2
2
2
2
2
1
2
2
2
2
2
1
2
2
2
2
2










Table 9: A-optimal allocation matrices for cross-sectional designs with D = 3. The A-optimal allocation matrices in the case I = {6}, C = {C6} = {6}, M = M6,6 = {8},
and σ2 = 1, with w = 0 and β = 1 are shown for E(ρ) ∈{0, 0.01, . . . , 1}. No restrictions are placed on X other than the identiﬁability of Equation 2.1. Each allocation
matrix was identiﬁed via our exhaustive search method.
26


## Page 27


C.
Application to binary outcome variables
In this section, we provide a brief description of how our methods can be applied to binary outcome variables (in the
case D = 2 for a cross-sectional design). Analysing at the cluster level, the following hierarchical model can be utilised
for data analysis
rij ∼Bin(m, pij),
logit(pij) = µ + πj + β1Xij + ci + ϵij,
where ci ∼N(0, σ2
c) and ϵij ∼N(0, σ2
ϵ /m). Moreover, rij is the number of responses observed in cluster i in period j,
and pij is therefore the probability of response in cluster i in period j.
We can then apply our methodology by assuming that σ2
e/m = 1/{m¯p(1 −¯p)}, where ¯p is the average response
rate. In practice, one would need to then assess the performance of the approximation via a simulation study to assess
the empirical power of identiﬁed eﬃcient designs. As discussed in Section 4, we may reasonably anticipate that such
approximation based results are likely to only be reliable for large sample sizes.
27


## Page 28


0
1
2
3
4
0.0
0.1
0.2
σc
2
σε
2
5
10
15
0
1
2
3
4
0.0
0.1
0.2
σc
2
σε
2
1.0
1.1
1.2
1.3
1.4
Figure 2:
The ratio of the variance of the intervention eﬀect when using design matrices X1 (top) and X2
(bottom) relative to the optimal design (given in Figure 1) is shown for a range of possible combinations of
(σ2
c, σ2
ϵ ) ∈[0.001, 0.25] × [0.25, 4].
28


## Page 29


References
[1] A. Atkinson and A. Donev. Optimum Experimental Designs. Oxford University Press, 1992.
[2] G. Baio, A. Copas, G. Ambler, J. Hargreaves, E. Beard, and R. Omar. Sample size calculation for a stepped
wedge trial. Trials, 16:354, 2015.
[3] T. Benham, Q. Duan, D. Kroese, and B. Liquet. Ceoptim: Cross-entropy r package for optimization. J Stat Soft,
76, 2017.
[4] M. Chinbuah, P. Kager, M. Abbey, M. Gyapong, E. Awini, J. Nonvignon, M. Adjuik, M. Aikins, F. Pagnoni,
and J. Gyapong. Impact of community management of fever (using antimalarials with or without antibiotics)
on childhood mortality: a cluster-randomized controlled trial in ghana. Am J Trop Med Hyg, 87:11–20, 2012.
[5] E. de Hoop, I. van der Tweel, R. van der Graaf, K. Moons, J. van Delden, J. Reitsma, and H. Koﬁjberg. The
need to balance merits and limitations from diﬀerent disciplines when considering the stepped wedge cluster
randomized trial design. BMC Med Res Methodol, 15:93, 2015.
[6] A. Dmitrienko, C. Chuang-Stein, and R. D’Agostino. Pharmaceutical Statistics Using SAS: A Practical Guide.
SAS Institute, 2007.
[7] A. Donner and N. Klar. Pitfalls of and controversies in cluster randomization trials. Am J Public Health, 94:
416–422, 2004.
[8] S. Edwards, D. Braunholtz, R. Lilford, and A. Stevens.
Ethical issues in the design and conduct of cluster
randomised controlled trials. BMJ, 318:1407, 1999.
[9] A. Girling and K. Hemming. Statistical eﬃciency and optimal design for stepped cluster studies under linear
mixed eﬀects models. Stat Med, 35:2149–2166, 2016.
[10] J. Hargreaves, A. Copas, E. Beard, D. Osrin, J. Lewis, C. Davey, J. Thompson, G. Baio, K. Fielding, and
A. Prost. Five questions to consider before conducting a stepped wedge trial. Trials, 16:350, 2015.
[11] K. Hemming, A. Girling, J. Martin, and S. Bond. Stepped wedge cluster randomized trials are eﬃcient and
provide a method of evaluation without which some interventions would not be evaluated. J Clin Epidemiol, 66:
1058–1059, 2013.
[12] K. Hemming, R. Lilford, and A. Girling. Stepped-wedge cluster randomised controlled trials: a generic framework
including parallel and multiple level designs. Stat Med, 34:181–196, 2015.
[13] R. Hooper, S. Teerenstra, E. de Hoop, and S. Eldridge. Sample size calculation for stepped wedge and other
longitudinal cluster randomised trials. Stat Med, 35:4718–4728, 2016.
[14] M. Hussey and J. Hughes. Design and analysis of stepped wedge cluster randomized trials. Contemp Clin Trials,
28:182–191, 2007.
29


## Page 30


[15] M. Keriel-Gascou, K. Buchet-Poyau, M. Rabilloud, A. Duclos, and C. C. A stepped wedge cluster randomized
trial is preferable for assessing complex health interventions. J Clin Epidemiol, 67:831–833, 2014.
[16] D. Kotz, M. Spigt, I. Arts, R. Crutzen, and W. Viechtbauer. Researchers should convince policy makers to
perform a classic cluster randomized controlled trial instead of a stepped wedge design when an intervention is
rolled out. J Clin Epidemiol, 65:1255–1256, 2012.
[17] D. Kotz, M. Spigt, I. Arts, R. Crutzen, and W. Viechtbauer.
Use of the stepped wedge design cannot be
recommended: a critical appraisal and comparison with the classic cluster randomized controlled trial design. J
Clin Epidemiol, 65:1249–1252, 2012.
[18] D. Kotz, M. Spigt, I. Arts, R. Crutzen, and W. Viechtbauer. The stepped wedge design does not inherently
have more power than a cluster randomized controlled trial. J Clin Epidemiol, 66:1059–1060, 2013.
[19] J. Lawrie, J. Carlin, and A. Forbes. Optimal stepped wedge designs. Stat Probabil Lett, 99:210–214, 2015.
[20] F. Li, E. Turner, and J. Preisser. Optimal allocation of clusters in cohort stepped wedge designs. Stat Probabil
Lett, 137:257–263, 2018.
[21] V. Lyons, L. Li, J. Hughes, and A. Rowhani-Rahbar. Proposed variations of the stepped-wedge design can be
used to accommodate multiple interventions. Stat Med, 86:160–167, 2017.
[22] J. Matthews and A. Forbes. Stepped wedge designs: insights from a design of experiments perspective. Stat
Med, 36:3772–3790, 2017.
[23] N. Mdege, M.-S. Man, C. Taylor nee Brown, and D. Torgerson.
There are some circumstances where the
stepped-wedge cluster randomized trial is preferable to the alternative: no randomized trial at all. response to
the commentary by kotz and colleagues. J Clin Epidemiol, 65:1253–1254, 2012.
[24] M. Parmar, J. Carpenter, and M. Sydes. More multiarm randomised trials of superiority are needed. Lancet,
384:283–284, 2014.
[25] M. Pol, G. Ter Riet, M. van Hartingsveldt, B. Krose, S. de Rooij, and B. Buurman. Eﬀectiveness of sensor
monitoring in an occupational therapy rehabilitation program for older persons after hip fracture, the so-hip
study: study protocol of a three-arm stepped wedge cluster randomized trial. BMC Health Serv Res, 17:3, 2017.
[26] A. Prost, A. Binik, I. Abubakar, A. Roy, M. De Allegri, C. Mouchoux, T. Dreischulte, H. Ayles, J. Lewis, and
D. Osrin. Logistic, ethical, and political dimensions of stepped wedge trials: critical review and case studies.
Trials, 16:351, 2015.
[27] S. Teerenstra and H. Calsbeek. Stepped-wedge like designs to compare active implementation strategies with
natural development in absence of active implementation.
Presented at the 36th Annual Conference of the
International Society for Clinical Biostatistics, Utrecht, The Netherlands, August 23-27, 2015.
30


## Page 31


[28] J. Thompson, K. Fielding, J. Hargreaves, and A. Copas. The optimal design of stepped wedge trials with equal
allocation to sequences and a comparison to other trial designs. Clin Trials, 14:639–647, 2017.
[29] A. Vickers. Clinical trials in crisis: four simple methodologic ﬁxes. Clin Trials, 11:615–621, 2014.
[30] J. Wason, L. Stecher, and A. Mander. Correcting for multiple-testing in multi-arm trials: is it necessary and is
it done? Trials, 15:364, 2014.
[31] W. Woertman, E. de Hoop, M. Moerbeek, S. Zuidema, D. Gerritsen, and S. Teerenstra. Stepped wedge designs
could reduce the required sample size in cluster randomized trials. J Clin Epidemiol, 66:752–758, 2013.
31

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1710_03496v2_admissible_multi_arm_stepped_wedge_cluster_randomized_trial_designs
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2017/1710_03496V2_ADMISSIBLE_MULTI_ARM_STEPPED_WEDGE_CLUSTER_RANDOMIZED_TRIAL_DESIGNS.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL
